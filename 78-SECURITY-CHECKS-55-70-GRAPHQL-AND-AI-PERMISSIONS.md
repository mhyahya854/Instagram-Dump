# 78 — Security Checks 55–70, AI-Built Apps, Part 4

Captured 2026-10-26. **All sixteen numbered labels are transcribed exactly as visible in the screenshot.** The bottom says “GraphQL”; this list is not limited to GraphQL, and the code snippet inset is unreadable and not reproduced. Practical defensive guidance below is an independently researched elaboration. No external system tested.

| # | Screenshot's exact label | Defensive security verification |
|---:|---|---|
| 55 | No MFA | Require appropriate MFA/passkeys for privileged accounts; test login/recovery/step-up |
| 56 | Account Enumeration | Compare signup/login/reset errors and timing; throttle user discovery |
| 57 | Business logic abuse | Enforce prices, quotas, role limits and ownership on server, not client |
| 58 | Race conditions | Concurrent writes to balance/inventory must remain transactional, locked or constrained |
| 59 | Webhook replay | Validate provider signatures/timestamps; process event IDs idempotently |
| 60 | Insecure CI/CD | Protect branches, deploy permissions, secrets and untrusted PR workflows |
| 61 | Untrusted build actions | Inspect/limit/pin actions, workflows and install scripts to reviewed immutable versions |
| 62 | Unpinned build dependencies | Pin reproducible dependency/CI/container versions and lockfiles |
| 63 | Checks fail open | Auth/entitlement/security policy outage must deny sensitive operations, not allow them |
| 64 | Missing timeouts | Bound requests, tool/database/model calls, cancellation, retries and budgets |
| 65 | Sensitive info logs | Redact tokens, credentials, cards, addresses and private AI documents |
| 66 | Invalid AI output | Typed schema validation, escaping, allowlisted actions and independent authorization |
| 67 | Excessive AI permissions | Minimize agent tools, filesystem, browser/account scopes; require consequential-action approvals |
| 68 | Sensitive browser storage | Avoid privileged API secrets in localStorage/IndexedDB; evaluate XSS and session/token design |
| 69 | Open redirects | Validate allowed destinations and prevent attacker-controlled login-like redirections |
| 70 | Unsecured endpoints | Test every REST/GraphQL sensitive action and object/field for proper authZ and rate limits |

## GraphQL-specific checklist

Authenticate and authorize fields/resolvers and object/tenant access, not merely the /graphql endpoint. Check query depth, aliases, batching, complexity budgets, introspection decisions, mutations' ownership/state validation, subscription/WebSocket authorization and rate limiting. Treat complex queries as resource-cost risks; use measured authorization tests with safe staging fixtures.

## QA protocol

(1) Inventory routes, data, roles and agent permissions; (2) write risk-specific negative tests; (3) check token/account revocation and payment/webhook idempotency; (4) inspect CI package scripts and credentials; (5) test failure/timeout/error paths; (6) save reproducible results by commit. An “AI security checked” success message, or two reviewing models agreeing, is not a proof of safety.

**No live exploitation or third-party scanning authorized.** Tests apply to owned/staging assets.

Related: [20 — Security](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md), [56 — JWT & Dependencies](56-AUTHENTICATION-JWT-REVOCATION-DEPENDENCY-SECURITY.md), [57 — Adversarial Review](57-RETICLE-ADVERSARIAL-REVIEWS-SECURITY-GATES.md).
Official references: https://cheatsheetseries.owasp.org/ , https://graphql.org/learn/security/ .

## URL vulnerabilities complement checks 55–70

[84 — URL Protection](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md) expands checks 69 (open redirects) and 70 (unsecured endpoints) with SSRF, account/object ownership tests, unsafe user/AI links, signed URLs, host header validation, callback allowlists and private staging. Contains **23 proposed tests** for authorized app fixtures, not scan results.
