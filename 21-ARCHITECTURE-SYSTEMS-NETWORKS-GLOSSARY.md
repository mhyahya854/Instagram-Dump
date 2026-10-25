# 21 — System Design, Networking and Operations: Extended Concept Glossary

Captured 2026-10-25. This is a **catalog of ideas to understand and consider**, not a directive to run a microservice cluster, Kafka, Terraform or Kubernetes for a small site. Read with [03-PRODUCTION-SYSTEM-ARCHITECTURE.md](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).

## 1. Client traffic and API boundaries

| Term | Meaning and when relevant |
| --- | --- |
| DNS | Name-to-address resolution and records. Incorrect DNS or caching can make a valid deployed app unreachable. |
| TCP vs UDP | TCP provides an ordered reliable byte stream; UDP transmits datagrams with fewer built-in guarantees. Protocol choice depends on application needs. |
| HTTP/2 vs HTTP/3 | Multiplexed modern HTTP transports; HTTP/3 commonly runs over QUIC/UDP. Test proxies/network compatibility and fallbacks. |
| TLS / encryption in transit | Protect application data over an untrusted network with validated certificates and modern configurations. |
| Reverse proxy | Accepts requests and forwards to internal services, often managing TLS, routing and buffering. |
| API gateway | Central interface for routing, auth, limits or policy across APIs; can become a dependency and bottleneck. |
| Rate limiting / throttling | Bound request rates and concurrency to prevent resource exhaustion and abuse; identity and IP-based keys serve different needs. |
| CDN / edge caching | Replicate cacheable assets near users; avoid caching user-private responses publicly. |
| WAF and DDoS protection | Layered network/application abuse mitigation; not a substitute for fixing insecure business logic. |
| CORS / CSRF | CORS governs browser sharing of responses across origins; CSRF guards unwanted credentialed state-changing requests. Different problems. |
| OAuth / IAM | Delegated authorization frameworks / access-management policies; validate scopes, roles and tenant boundaries. |
| API versioning / semantic versioning | Manage backward compatibility and release contracts; consumers may not update together. |
| Webhooks | Server-to-server notifications with signature, idempotency, retries and event ordering concerns. |
| WebSockets / long polling | Persistent bidirectional transport vs periodic long-held HTTP requests; choose for real-time needs. |

## 2. Services, reliability and communication

| Term | Meaning / key tradeoff |
| --- | --- |
| Load balancing | Spread requests among healthy instances; avoid per-instance hidden session state unless handled. |
| Service discovery | Locate active service endpoints as instances move or scale. |
| Containers / Docker | Package app process and dependencies reproducibly; containers are not an access-control guarantee. |
| Kubernetes / orchestration | Schedule, scale, restart and expose containers; substantial operational overhead. |
| Circuit breaker | Stop hammering a failing dependency until recovery criteria are met. |
| Timeout / retries / exponential backoff | Bound waiting, retry only where safe, add exponential delay and jitter; don't retry forever. |
| Idempotency | Replaying one operation has no extra intended effect; crucial for payments, jobs, webhooks and backfills. |
| Message queues / pub-sub | Decouple producers and consumers, buffering work or broadcasting events. Acknowledgment and replay semantics matter. |
| Event-driven architecture / cron | Process triggered events vs scheduled tasks; neither removes idempotency requirements. |
| Dead-letter queue | Quarantine repeatedly failing messages for inspection, alerting and controlled replay. |
| Backpressure / load shedding | Slow upstream producers or reject work when consumers cannot keep up. |
| Distributed transaction / saga | Coordinate steps across services by protocol or compensating actions; added failure complexity. |
| Consistency / availability / CAP | Under network partition, a distributed system faces specific consistency/availability tradeoffs; CAP doesn't imply only “two of three” at all times. |
| Network partition | Connection between nodes is disrupted; protect against split brain and uncertain commits. |
| Eventual consistency | Replica/state convergence after updates in absence of new writes; not “random” correctness. |

## 3. Data performance, correctness and concurrency

| Term | Meaning / guardrail |
| --- | --- |
| Database indexing / query optimization | Data structures and query plans to accelerate lookups; indexes cost write time/storage. |
| N+1 queries | A query-per-item pattern that scales badly; batch/prefetch relevant reads. |
| Connection pooling | Reuse limited database connections to avoid exhaustion, especially with serverless concurrency. |
| Read replicas / replication | Copies for reads and resilience; replication lag affects consistency. |
| Sharding / partitioning | Split data horizontally for scale/maintenance; adds routing and rebalance complexity. |
| Optimistic locking | Update if a version hasn't changed; reject/retry on conflict. |
| Pessimistic locking | Acquire appropriate lock before a conflicting update; watch contention and deadlocks. |
| Distributed locking | Coordinate across nodes; safe leases, fencing tokens and failure handling may be needed. |
| Race conditions / deadlocks | Timing-dependent correctness failures vs cycles of waiting on resources. |
| Data migrations / schema validation | Controlled schema evolution; staging, backups, backward compatibility and validated rollback/forward recovery. |
| Read/write cache, cache invalidation | Fast answers with defined ownership, TTL and invalidation; never assume cached authorization remains current. |
| Block storage vs object storage | Attached block-level volumes vs object-keyed remote storage; different durability and access models. |
| Memory leak / garbage collection / thread safety | Resource-retention bug / reclaiming unreachable memory / correctness across concurrent threads. GC doesn't prevent all leaks. |

## 4. Scaling, deployments and operations

| Term | Meaning / guardrail |
| --- | --- |
| Horizontal vs vertical scaling | Add instances vs enlarge one machine; examine state, costs and bottlenecks. |
| Autoscaling / capacity planning | Adjust or provision ahead of demand; account for ramp-up, quotas, baselines and peak load. |
| Serverless / cold starts | On-demand function/container instances may need start-up latency; billing and max duration vary by provider. |
| CDN / edge caching | Deliver eligible cacheable content near requesters; private data isolation matters. |
| CI/CD and build caching | Verified automated build/test/deploy pipeline; caches must be safe and invalidated for changed inputs. |
| Infrastructure as Code / Terraform | Version and review infrastructure changes; secrets and plans require controls. |
| Helm charts | Package declarative Kubernetes resources and their templates; not universally necessary. |
| Immutable deployments | Deploy fresh artifacts, avoid hidden changes on live hosts; requires configuration discipline. |
| Blue-green / canary / rolling deployment | Alternate release strategies; choose by rollback speed, capacity and risk. |
| Feature flags / rollbacks | Change rollout independently from code deployment; flags may need expiry and audit. |
| Health checks, liveness and readiness probes | Distinguish “process alive” from “can receive traffic”; incorrect probes can worsen an outage. |
| Monitoring, logging, tracing, metrics | Observe state and request paths; redact secrets/PII, establish meaningful alert thresholds. |
| SLI / SLO / P99 and tail latency | Measure reliability goals and slowest-user experience, not only average response. |
| Incident response / on-call / postmortems | Roles, runbooks, rollback, communication and learning without blame. |
| Chaos engineering | Controlled failure experiments only with safe environments, scope, rollback and observability. |
| Disaster recovery / failover / multi-region | Recovery-time/data-loss tradeoffs; cost and consistency impacts. |
| Cost optimization | Budget alerts, capacity rightsizing, quota controls, data egress and measured workloads. |

## 5. Security concepts that also sit in system design

Secrets management, IAM/least privilege, OAuth, credential rotation, TLS, encryption at rest, CORS/CSRF, XSS, SQL injection, secure uploads, WAF, DDoS protection and security audits. Details and OSI mapping: [20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md).

**Note:** “Encryption at rest” is storage encryption, distinct from “TLS in transit.” An OAuth token is not an authentication policy. A WAF cannot enforce a complete authorization matrix.

## 6. Source transcription corrections retained

| Heard | Likely term | Confidence |
| --- | --- | --- |
| idiompetency | idempotency | Strong |
| message queries | message queues | Strong |
| dead-lettered queries | dead-letter queues | Strong |
| optimism locking | optimistic locking | Strong |
| after scaling | autoscaling | Probable |
| lights mix | liveness checks/probes | Probable |
| C throughput | throughput / requests per second | Unclear |
| block screw | block storage | Unclear |
| “HE, as immutable charts” | Helm charts (possibly) and immutable deployment | Unclear |
| delayed copies, flips | Possibly replicas and failover | Unclear |
| jailbreakability | Likely LLM prompt-injection/jailbreak resilience | Category noted, exact meaning uncertain |
| C inless | Unresolved | Preserve |
| uptime, availability, reliability | Distinct concepts already covered in file 03 | Confirmed |

## 7. Choosing architecture proportionately

The order is **requirements → workload assumptions → failure tolerance → evidence → simplest sufficient design**. For a private single-user journal, start with local-first security, reliable backups and a responsive UI, not Kafka or global consensus. For a high-volume financial application, isolation, transactions, audit logs, resilience and replication demand deeper analysis. Both deserve testing, but not identical architecture.

Primary source families: PostgreSQL documentation (https://www.postgresql.org/docs/current/), OWASP ASVS (https://github.com/OWASP/ASVS), Cloudflare Learning Center (https://www.cloudflare.com/learning/), Google SRE books (https://sre.google/books/), OpenTelemetry (https://opentelemetry.io/docs/).
