# 166 — Redis in AI: deployment patterns, trust boundaries and technology choice

**Provenance:** [141](141-REDIS-IN-AI-CACHE-VECTOR-RAG-AGENT-STATE.md) archives a screenshot headed “Redis in AI Explained.” The mechanisms below are independent engineering guidance; the screenshot contained **no code, benchmark or vendor architecture**. Redis docs checked 2026-10-27: [AI and search](https://redis.io/docs/latest/develop/ai/), [vector concepts](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/), [RedisVL cache](https://redis.io/docs/latest/develop/ai/redisvl/user_guide/how_to_guides/llmcache/).

## Decision table

| Job | Redis works when | Prefer alternative when |
|---|---|---|
| Exact LLM response cache | Repeated deterministic, scope-safe inputs; bounded TTL | In-process LRU works on one instance with low cost |
| Semantic cache | Meaning-preserving repetitions and acceptable false-hit risk | Medical/legal/safety-critical or highly personalized outputs cannot tolerate a wrong reused response |
| Session state | Fast access, shared horizontal instances, TTL | Database/audited append-only store is canonical history |
| Vector retrieval | Modest-to-large searchable embeddings, metadata filters, low-latency retrieval | PostgreSQL + pgvector already sufficient; dedicated vector DB needed for specialized scale/operations |
| Rate limiting | Distributed counters and atomically enforced policies | One-process prototype or upstream edge rate limiter already owns quotas |
| Queues/background jobs | Redis Streams/consumer groups or a well-defined job framework with retries and reconciliation | Durable workflows require guarantees that a purpose-built queue/DB provides better |
| Distributed coordination | Short-lived leases with explicit expiry, careful fencing/ownership | Database transactions/advisory locks provide correctness with fewer moving parts |
| Live updates | Pub/Sub for noncritical ephemeral fan-out, Streams for consumable logs | Need durable event log and replay with separate retention/ordering requirements |
| Agent memory | Small fast working state, retrieval candidates, TTL and known tenant | Long-term source-of-truth provenance requires DB/object storage and deletion controls |

## Correctness-oriented architecture

```text
Browser / API  -- verified identity and tenant --> application
                                             |-- Postgres: canonical users, documents, audit and durable tasks
                                             |-- Redis: scoped hot cache, rate counters, ephemeral agent state
                                             |-- Object store: source documents / authorized blobs
                                             |-- Embedding model: versioned vectors (only for authorized data)
                                             |-- Worker: idempotent background tasks with replay + dedup
LLM result --> validation / attribution / abuse checks --> persist if appropriate
```

Redis should normally be an acceleration and coordination layer, **not the only copy** of legally important content or a magical “agent brain.”

## Cache correctness contract

Build an exact-match key from a *canonical serialization* of model ID+revision, instructions fingerprint, retrieval corpus revision, user/tenant scope, permissions, generation settings, safety policy version, locale, and normalized question. Hash the serialized composite key; **never** let one user's private result be served to another user. Don't put secrets in key strings or metrics. Cache only successful, validated, non-sensitive eligible responses. Set TTL based on volatility. Invalidate by document/version or access-control change; explicit deletion requests must remove derivative indexes/caches.

Semantic similarity must not be treated as equivalence: even two highly similar questions can differ in entity, negation, numeric constraint, user entitlement or freshness. A safe implementation checks similarity threshold **and** tenant+policy+model+knowledge-version filters; then revalidates returned answer against task intent. Tune threshold on labeled false-hit data and measure correctness, not only hit rate.

```python
# Schematic pseudocode; intentionally no Redis connection, package install or credentials.
def answer(request, authenticated_tenant, corpus_revision):
    key = stable_hash({
        "tenant": authenticated_tenant,
        "model": MODEL_REVISION,
        "prompt_policy": PROMPT_POLICY_REVISION,
        "corpus": corpus_revision,
        "settings": GENERATION_SETTINGS,
        "query": canonicalize(request.question),
    })
    hit = redis_get(key)
    if hit is not None and allow_cached_result(request, hit):
        return hit
    # Use coalesced in-flight work to avoid a thundering herd.
    validated = call_model_with_verified_retrieval(request)
    if cache_eligible(request, validated):
        redis_set_ex(key, ttl_seconds=300, value=validated)
    return validated
```

No `redis_get`, `redis_set_ex` or policy functions are provided or invoked; an implementation must define them and test failure modes. The TTL of 300 seconds is **illustrative**, not a universal recommendation.

## Vectors and retrieval

Redis Search can index vectors in HASH/JSON fields with `FLAT` or approximate algorithms such as `HNSW`; choose `DIM` and numeric type to match the embedding model. Queries can combine vector similarity and structured metadata filters. **Never** omit a tenant/access filter during retrieval. Re-embed all vectors after an incompatible embedding-model change; store source ID, chunk index, content fingerprint, embedding revision, ACL revision and deletion flag. Evaluate recall@k and precision with relevant-domain test questions, memory/cost consumption, p95 query time and indexing lag. Embeddings may reveal sensitive information and require protection.

## Reliability runbook

- Explicitly choose persistence (RDB/AOF settings, acceptable data-loss window) and backup/restore proof for every durable Redis workload.
- Set maxmemory, eviction policy per namespace/workload, noeviction or partition for critical rate-limiter/queue keys. Monitor memory fragmentation and hot-key distribution.
- Queue jobs should carry idempotency keys, deadlines, retries with exponential backoff/jitter, poison-message handling and a dead-letter audit; a completed consumer acknowledgement without a canonical DB write can lose work.
- Locking: expiring locks do not guarantee exclusive access after pauses; use fencing tokens or source-of-truth transactions for safety-critical writes.
- Require TLS in transit, authentication/ACLs, secret rotation, network isolation, bounded input size and latency timeouts; no anonymous public Redis service.
- Fail closed for authorization checks. Define separate safe degradation for caches (fall through) versus abuse/rate limiting (protect login) versus worker queues (reconcile).
- Cost model includes memory replication, index overhead, egress, operations, backups and recovery time—do not assume “Redis is faster” without a baseline.

**Validation scenarios:** tenant A question never hits B's private cache, corpus update invalidates, eviction does not violate business truth, Redis outage does not bypass auth/rate controls, partial worker failure replays exactly-once *effects* via idempotency, and a memory deletion removes indexed derivatives.
