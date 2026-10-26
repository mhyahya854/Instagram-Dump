# 50 — Programming Fundamentals, System Design and Legitimate Free LLM API Sources

Captured from sixth reel collection, 2026-10-25. Designed as an offline-readable teaching index for selecting learning paths; not a directive to build every infrastructure component.

## Requested topics and trustworthy sources

| Topic | Definition / reason to learn | Primary reference |
| --- | --- | --- |
| Data structures and algorithms | Arrays/maps/sets, queues, trees, graphs, complexity, sorting/searching and correctness | https://github.com/TheAlgorithms/Python ; https://github.com/TheAlgorithms/Rust |
| Git and version control | Commits, branches, diffs, PRs, review, conflict recovery | https://git-scm.com/book/en/v2 |
| SQL and relational databases | Tables, joins, keys, indexes, transactions, locking, backup/restore | https://www.postgresql.org/docs/current/ |
| Spring Boot / Java | Web service framework, dependency injection, validation, security and integration tests | https://docs.spring.io/spring-boot/ |
| API design and contracts | Resource/action definition, schema, status/errors, authentication, idempotency | https://github.com/OAI/OpenAPI-Specification |
| System architecture | Requirements, capacity, resilience, consistency, storage/caching, monitoring | https://github.com/donnemartin/system-design-primer |
| DevOps and delivery | Versioned builds, automated tests, CI/CD, deployments, rollback and monitoring | https://docs.github.com/en/actions ; https://sre.google/books/ |
| Cloud / AWS | IAM, VPC, network, shared responsibility, compute, database, costs and backups | https://docs.aws.amazon.com/ |
| Security | Threat models, auth/authZ, secret handling, RLS, OWASP verification | https://github.com/OWASP/ASVS ; https://cheatsheetseries.owasp.org/ |
| Coding practices | Types, modularity, minimality, lint/tests, dependency safety, review | https://github.com/obra/superpowers ; https://github.com/Leonxlnx/unlazy |
| Database design | Stable IDs, privacy boundary, normalization/denormalization, migrations, isolation | https://www.postgresql.org/docs/current/ |
| API/back-end guide | Typed validation, versioning, rate limiting, handling failure, authorization | https://owasp.org/www-project-api-security/ |
| Distributed systems | Queues, retries, service discovery, eventual consistency, CAP, sagas and fault handling | https://sre.google/books/ |
| Observability | Metrics/traces/logs, SLIs/SLOs, alerts and recovery | https://opentelemetry.io/docs/ |
| Mobile integrations | Android semantics, iOS accessibility, tool APIs and controlled computer use | https://github.com/google/artemis ; https://github.com/modelcontextprotocol/modelcontextprotocol |

**Rust-first policy note:** prefer Rust when feasible for new implementations, but choose framework/language on project-specific technical grounds; e.g. Spring Boot is a Java ecosystem resource for understanding existing services, not a mandatory switch from Rust.

## Reference architecture: ten dimensions to decide before coding

1. **Product goal and users**: user tasks, constraints, privacy, latency and availability.
2. **APIs and business logic**: input/output contracts, validation, state machine, authorization and error semantics.
3. **Database and storage**: relational vs object, schema, indexes, migrations and backup/restore.
4. **Authentication and permissions**: sessions, account status, tenant isolation, RLS and audit.
5. **Hosting/cloud**: local-first vs self-host vs managed, ingress, secrets, reliability and cost.
6. **CI/CD and version control**: branches, test gates, review and safe deployment.
7. **Security and abuse controls**: risk model, input escaping, rate limits, quotas and key rotation.
8. **Caching and performance**: demand-driven caches, invalidation, database queries and load tests.
9. **Operations and observability**: structured errors, log redaction, alerts, SLOs and incident response.
10. **Testing, scaling and recovery**: unit, integration, real UI, concurrency and destructive-failure restore drills.

A small private application may need a simple modular monolith rather than Kubernetes, sharding and microservices. Complexity must be justified by actual requirements.

## Free LLM API research — no fixed free-tier promises

Verified GitHub inventories:
- https://github.com/pacocartones/free-llm-api-hub (lists live/dated verification, card requirements and commercial-use notes)
- https://github.com/devanasolver/awesome-free-llm-apis (compares permanent tiers with credits/trials)
- https://github.com/Reveritus/Free-LLM-API-resources (catalog; read version/date).
- https://github.com/SidSharma010/free-llm-api-hub (machine-readable provider inventory).

**What “free” can mean:** no payment method to experiment, a monthly quota, temporary trial credits, a rotating model lineup, noncommercial-only usage or lower priority. Never assume a free endpoint is available forever or may be resold. Examine official provider documentation for region, model, token pricing, retention/training of prompts, personal-data rules, tool availability, quotas and throttling.

Typical evaluation dimensions: context window, instruction reliability, function calling/JSON, multilingual support, latency, input/output tokens, image/audio models, privacy, failure/retry, uptime, provider lock-in and cost guardrails. **Do not use leaked keys or reverse-engineered unauthorized chat endpoints** as “free API”.

## Example evaluation matrix (create from direct live tests)

| Workload | Test | Quality metric |
|---|---|---|
| Data extraction | 30 diverse invoices/synthetic fixtures | exact-match fields, missing-data reporting |
| Code patching | chosen repo unit/integration tests | pass/fail, broken behavior, diff quality |
| Agent tool use | structured tool schema tests | correct tool calls, forbidden-action refusals |
| Retrieval | document questions with known passages | source correctness and citations |
| Speech | locally consented test clips | word error rate by language/noise |
| User trust | adversarial sample docs | prompt-injection resistance and no exfiltration |

Document real outcomes rather than claiming “model A always beats model B.”

## More materials already preserved

[03 — Production Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md); [10 — DB Transactions](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md); [21 — Systems Glossary](21-ARCHITECTURE-SYSTEMS-NETWORKS-GLOSSARY.md); [32 — Build Your Own X](32-BUILD-YOUR-OWN-X-FIRST-PRINCIPLES-LEARNING.md); [47 — AI Engineering](47-AI-ENGINEERING-LEARNING-MODEL-TRAINING-RAG.md).

## Fourteenth batch — FreeLLMAPI provider-router caveats

[113 — FreeLLMAPI](113-FREELLMAPI-FREE-TIER-ROUTER-VERIFICATION.md) documents its source claims of **34 providers / 635 endpoints / 7.4 billion tokens**, the concrete GitHub candidate, `/v1` model routing and encrypted key handling, while clarifying these totals are **theoretical combined catalog limits**, not promised free quota for an individual. Any nonlocal model means prompts/data leave the computer and provider terms apply.

## Seventeenth reel — Redis and AI fine-tuning

[141 — Redis for AI](141-REDIS-IN-AI-CACHE-VECTOR-RAG-AGENT-STATE.md) distinguishes cache, vector retrieval and memory from authoritative durable databases. [146 — Fine-Tuning](146-LIBRARIES-DEV-AND-FINE-TUNING-AI-MODELS.md) preserves the screenshot's conditional small-model advantage, separating prompt design, RAG, SFT and LoRA/QLoRA. No model trained.
