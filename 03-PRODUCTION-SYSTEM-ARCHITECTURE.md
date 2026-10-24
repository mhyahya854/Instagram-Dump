# 03 — Production Readiness, Backend Architecture & System Design

> **Scope:** real deployment defects, security risks, databases, performance, distributed systems, resilience, test strategy and operations. This is a **consider-when-relevant engineering inventory**, not an instruction to implement every item.

## A. Release defects to prevent / verify

| Avoid / detect | Employ / verify |
| --- | --- |
| Missing environment variables | Validate required variables for each environment; fail safely. |
| Hardcoded localhost or local URLs | Use correct runtime/environment-specific origins and endpoints. |
| Database connection issues | Check credentials, network access, migrations, TLS where appropriate, and pools. |
| Build errors only in production | Run release/production build and smoke-test the deployed artifact. |
| CORS errors | Configure allowed origins, credentials, methods, and headers correctly; do not mistake CORS for authorization. |
| Secrets exposed in code or frontend bundles | Use protected server-side secret storage and scan for leaks. |
| Deploys that succeed but break user flows | Verify runtime functionality, telemetry, and critical workflows. |
| Schema changes breaking active deployments | Plan backward-compatible migrations and rollback paths. |

## B. Security: prevent / verify

| Avoid / vulnerability | Control or verification |
| --- | --- |
| RLS: missing/incorrect row-level policies | Define and test Row-Level Security policies if data platform relies on RLS. |
| Race conditions | Protect critical concurrent updates through transactions, constraints, locks, and idempotency where needed. |
| IDOR / broken object-level authorization | Check access server-side for every requested resource. |
| CSRF | Apply CSRF controls where the auth/session model requires them. |
| Missing server-side validation | Validate untrusted inputs on the server, not only in the browser. |
| Unsafe database transactions | Ensure atomicity and appropriate rollback and isolation. |
| Secret exposure | Keep secrets out of source, logs, browser bundles, and error messages. |
| Authorization bypass | Test roles, tenancy boundaries, and privilege escalation. |
| Missing webhook verification | Verify provider signatures and replay protection when available. |
| Dependency vulnerabilities | Scan, update, and assess vulnerable dependencies. |
| Injection vulnerabilities | Prevent SQL/command/template injection using parameterization and safe APIs. |
| Missing abuse controls | Appropriate rate limiting and throttling. |
| XSS (cross-site scripting) | Contextual output encoding, safe DOM handling, and suitable CSP. |
| SSRF (server-side request forgery) | Constrain server-originated network requests and destination access. |
| Unsafe file uploads | Validate type/content/size, isolate storage, scan where appropriate. |
| Public access to private objects | Use scoped access and signed URLs where useful; check expiry. |
| Improper session lifecycle | Session expiration, secure cookies, renewal and revocation. |
| Excessive privileges | Least-privilege accounts and permissions. |
| No accountability for security-sensitive changes | Privacy-aware audit logs. |
| Missing security headers | Verify appropriate CSP, frame restrictions, HSTS, etc. |
| Weak API security | API authentication/authorization and input handling checks. |
| AI-specific vulnerabilities when AI components exist | Review prompt injection, tool permissions and data leakage as applicable; original dictation unclear. |

## C. Database, caching and data integrity

| Avoid / inspect | Consider / verify |
| --- | --- |
| Unindexed important query paths | Database indexing based on actual query patterns. |
| Slow query patterns | Query optimization and execution-plan checks. |
| N+1 database queries | Detect and fix with batching, joins or prefetching. |
| Database connection exhaustion | Connection pooling and resource limits. |
| Stale or incoherent cache | Cache invalidation and appropriate consistency expectations. |
| Caching complexity without use case | Consider eviction, stampede prevention, CDN, write-through, write-back, cache-aside. |
| Choosing storage models without tradeoff analysis | Normalization and denormalization; ACID, BASE and isolation levels. |
| Unexamined transaction coordination | Distributed transactions, Saga pattern, CQRS/event sourcing only when justified. |
| Improper workload distribution | Sharding, replication and partitioning when needed. |
| Unproven restore ability | Database backup AND restore testing. |
| Unsafe database changes | Migrations and rollback strategy. |
| Inefficient search or routing at scale | Full-text search/indexing, Bloom filters, consistent hashing when relevant. |

## D. Architecture and distributed-systems concepts

| Avoid / question | Consider when applicable |
| --- | --- |
| No reliability/performance expectations | Scalability, availability, reliability, fault tolerance, resilience. |
| Unknown traffic and response characteristics | Latency, throughput, capacity planning. |
| Unexamined data guarantees | Consistency, durability, partition tolerance and CAP tradeoffs. |
| Applying scaling mechanisms automatically | Choose as justified: load balancing, horizontal/vertical scaling, autoscaling. |
| Single points of failure for services requiring HA | High availability, redundancy, failover, disaster recovery. |
| Overloaded servers | Load shedding and backpressure where needed. |
| Distributed coordination without safeguards | Quorum, leader election, consensus, distributed locks. |
| Duplicate processing or timing anomalies | Idempotency, race/deadlock handling and clock synchronization considerations. |
| Assuming one transport suits every API | REST, GraphQL, gRPC, API gateway, service discovery as appropriate. |
| Poor access control at services | Authentication, authorization, throttling/rate limiting. |
| Premature microservices | Assess monoliths vs. microservices according to actual needs. |
| Event-driven infrastructure without real use cases | Event-driven architecture, event streaming, message queues, publish–subscribe, Kafka. |
| Uncontrolled retries and cascading failures | Exponential backoff, circuit breakers, bulkheads and timeouts. |
| Unprocessed queue failures | Dead-letter queues and retry policies. |
| Needlessly complex data flow | Event sourcing, CQRS, Saga pattern only with justification. |
| Inappropriate real-time mechanism | WebSockets vs. long polling. |
| Poor separation of tenants | Multi-tenancy isolation if application supports tenants. |
| Inappropriate storage choice | Object storage and blob storage as appropriate. |

## E. Observability, operations and deployment

| Avoid / inspect | Consider / verify |
| --- | --- |
| Silent failures | Error monitoring, health checks, actionable alerting. |
| Incomprehensible or unsafe logs | Structured logging and privacy-aware audit logs. |
| No cross-service diagnostic visibility | Distributed tracing, observability, metrics. |
| Undefined service health targets | SLI and SLO (and SLA where contractually needed). |
| Dangerous all-at-once deployments | Blue-green, canary, rolling and zero-downtime deployments when needed. |
| Unmanaged runtime differences | Containerization/orchestration as appropriate, not automatically. |
| Broken background processing | Background jobs, timeouts, retries, DLQs. |
| Large unreviewed feature rollouts | Feature flags and safe rollback when valuable. |
| Missing backups, recovery or resilience rehearsal | Backup restore tests and disaster-recovery exercises. |
| Uncontrolled cloud costs | Cost monitoring and capacity planning. |
| Undefined retention of logs/data | Data retention policies aligned with purpose and law. |

## F. Testing / release assurance

| Avoid / failure mode | Verify / consider |
| --- | --- |
| Only running locally | Staging environments and production-like smoke tests. |
| No realistic full-flow validation | End-to-end testing. |
| Breaking service/API contracts | Contract testing. |
| Duplicate, forged or missed payment events | Payment webhook testing, signatures and idempotency. |
| Inaccessible released experiences | Accessibility testing. |
| Desktop browser-only checks | Mobile browser and responsive testing. |
| Systems that collapse under realistic load | Load testing and capacity assessment. |
| Schema or release failures with no recovery path | Migration, rollback and zero-downtime release validation. |
| Untested disaster recovery | Backups plus restore drills and recovery targets. |

## Engineering interpretation and selection rules

1. **Prevent real defects first:** missing environment variables, hardcoded local URLs, bad database connections, production-only failures, dangerous CORS, exposed secrets, authorization bugs, and incomplete testing.
2. **Select technologies from requirements:** CAP, consensus, Kafka, CQRS, sharding, microservices, orchestration, and autoscaling are *not* mandatory for a basic website.
3. **Recognize alternatives and tradeoffs:** a monolith vs. microservices, REST vs. GraphQL vs. gRPC, strong vs. eventual consistency, write-through vs. write-back vs. cache-aside, and different deployment strategies are choices, not boxes to check simultaneously.
4. **Validate in the real deployment environment:** check health, errors, security boundaries, cost, recovery, and relevant user journeys.
5. **Keep secrets and sensitive data out of logging, monitoring, and uploaded test artifacts.**
6. **Do not implement unnecessary complexity.** Document why a technique is or is not relevant.

## Voice-transcription ambiguities preserved

- “CE” has no confident mapping and is not converted into an architecture mandate.
- “Database sharing” was likely **database sharding**.
- “Database shedding” was likely **load shedding**.
- “Database application partitioning” may mean **database replication/partitioning**.
- “Asset properties / base properties” likely **ACID / BASE**.
- “Adm potency” = **idempotency**; “waste conditions” = **race conditions**.
- “Cash stem” likely **cache stampede**; “weight limiting” = **rate limiting**.
- “Events training” likely **event streaming**; “exponential backup” = **exponential backoff**.
- “Built head pattern” = **bulkhead pattern**; “so you can break our” = **circuit breaker**.
- “That letter Q” = **dead-letter queue**; “observing ability” = **observability**.
- “Blue wind” = **blue-green**; “ruling deployment” = **rolling deployment**.
- “Pop storage” possibly **blob storage**; “long pulling” = **long polling**.
- “The book verification” = **webhook verification**; “feature packs” = **feature flags**.
- “State attention policies” likely **data retention policies**.

All mappings above are retained as interpretation notes, not treated as quotes from a formal specification.
