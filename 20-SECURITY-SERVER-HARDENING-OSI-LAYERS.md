# 20 — Secure AI-Built Apps: SQL Injection, Server Exposure, Defense in Depth and OSI Layers

Captured 2026-10-25. **Defensive education and verification only.** All reconnaissance, scans and configuration changes require authorization for the target. No live production changes performed as part of this archive.

## 1. Short “Claude, protect my website” reel: requirements vs proof

Spoken requirements: protect API keys, environment variables and admin routes; correct authentication, authorization, forms, XSS, rate limits, CORS, security headers, debug settings, dependencies, exposed files, database controls, passwords, Git history and a full audit.

A credible implementation requires **threat model → checks → changes → independent verification**. The phrase “make no mistakes” cannot prove correctness.

| Failure | Concrete defensive requirement | Verification evidence |
| --- | --- | --- |
| Secrets exposed in browser/build/Git | Server-side secrets manager or environment configuration; least-privilege, revocable credentials; distinguish legitimate public keys | Build artifact and Git/history secret scans; rotate any exposed key |
| Admin pages/API exposed | Server-side authorization per action and resource; tenant isolation; RLS if DB supports | Anonymous, ordinary-user, cross-account and stale-session negative tests |
| Bad session management | Secure cookies/tokens, refresh revocation, timeouts, step-up authentication where needed | Sign out, account termination, stolen/stale token tests |
| SQL injection | Parameterized SQL, query builders used safely, allowlisted identifiers | Review raw SQL, fuzz tests and authorized DAST; never trust stripped punctuation |
| XSS / unsafe HTML | Context-aware output escaping, vetted sanitization for actual HTML, CSP as defense-in-depth | Inject harmless inert test values in authorized staging; verify rendered escaping |
| CSRF / CORS | CSRF defenses for credentialed state-changing requests; CORS narrowly scoped by intended origins | Wrong-origin browser tests, CSRF denial tests, credential handling review |
| Public endpoint abuse | IP/user/API-key/route-aware quotas, concurrency caps, timeouts and cost budgets | 429 behavior, load/abuse simulations and billing alerts |
| Passwords | Established slow password-hashing algorithms (Argon2id/scrypt/bcrypt as appropriate), salts, secret-reset flow | Tests and audit against OWASP recommendations; no reversible password storage |
| Vulnerable packages | Lockfiles, SBOM, update and vulnerability scans, reviewed untrusted dependencies | Versioned scan report, prioritized fixes |
| Unsafe deployment | Disabled debug, restricted exposed files, HTTPS/security headers, backups, readiness alerts | Production-config snapshot, external surface check, restore test |

Security scanners find classes of risks; **no single scanner proves an app is secure**.

## 2. SQL injection reel — important correction

The attack described arises when **untrusted input is concatenated into a SQL command string**, letting it be interpreted as SQL instructions rather than a literal value. The reel's suggestion to remove “code-looking” characters, braces and semicolons is **not sufficient** and can reject legitimate names or text.

**Primary defense: use prepared statements with bound parameters;** the database parser keeps the SQL structure separate from input data. Apply allowlist validation for *domain data* (e.g. length and permitted username format) and separately for dynamic SQL identifiers such as sort columns. Enforce least-privilege database permissions. Escaping alone is fragile.

Illustrative JavaScript pattern (library-specific parameter placeholder syntax):

~~~js
// Good: query structure is fixed; the user's value stays data.
const result = await db.query(
  "SELECT id FROM users WHERE username = $1",
  [userSuppliedUsername]
);
~~~

Avoid creating SQL by interpolating untrusted text into the query string. ORM and stored procedure usage still require reviewing raw SQL and dynamic query construction.

Reference: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html .

## 3. Protecting your own server from internet exposure — no lockout

Reel describes authorized inspection of running services, listening ports, firewall rules, SSH credentials and environment variables **before** tightening ingress.

**Safe operational order**:
1. Confirm ownership, approved change window, recovery console/out-of-band access and backups. Identify cloud/network firewalls as well as host firewall.
2. Inventory **expected services and their business purpose** and note actual listening addresses (loopback vs 0.0.0.0/::). Web typically uses 80/443; SSH commonly 22, but actual custom ports and architectures vary. Databases should usually not be publicly reachable.
3. Map each open port to process/container, account, public route and load balancer or reverse proxy. Unexpected port ≠ automatically malicious; inspect.
4. Establish working SSH **key-based access** and verify a second connection before disabling password login. Consider MFA, bastion/SSM/VPN, IP allowlists and logging.
5. Propose firewall rules in an approved change set; **preserve your current management route before enforcing**. Do not “close everything” from the only SSH session.
6. After each change, verify legitimate app and admin functionality from outside, monitor logs and keep rollback access.
7. Restrict secrets and backups independently of open ports. Environment variables are configuration surfaces, **not magic encryption**; logs, process dumps and client bundles can leak them.

**Audit before modify.** Example read-only host observations on an authorized Linux host include listening socket inventory and firewall policy *inspection*. Do not run blind block commands on production.

## 4. OSI seven-layer security: a mental checklist, not literal deployment boundaries

OSI layers describe network communication. Actual TLS, HTTP, cloud controls and application protocols span conceptual layers; **do not assume TLS is always precisely only “L6” or that a firewall only protects L4**.

| Layer | Role | Common defensive controls | Reel wording / qualification |
| --- | --- | --- | --- |
| **L7 Application** | HTTP APIs, apps, parsers and user operations | Parameterization, input/schema validation, authZ, rate limits, WAF, logging, CSRF/XSS/SSRF defenses | “WEP, input params people” likely web app validation and parameters |
| **L6 Presentation** | Data representation/encoding and encryption (conceptual) | TLS version/cipher/cert validation, secure serialization, encryption posture | TLS 1.2+, certs; modern TLS handled across protocol stack |
| **L5 Session** | Session establishment/continuity | Session IDs, secure cookie flags, expiry, refresh revocation, reauthentication | Cookie flags (Secure, HttpOnly, SameSite), timeouts |
| **L4 Transport** | TCP/UDP flows and ports | Stateful firewall/security groups, SYN flood protection, connection limits, encrypted transport termination as applicable | “Close ports” only after mapping legitimate routes |
| **L3 Network** | IP addressing/routing | Default-deny ingress, network segmentation, anti-spoofing, safe ICMP rules, routing ACLs | ICMP is not universally unsafe; diagnostic and PMTUD needs exist |
| **L2 Data Link** | Frames, switches, local broadcast domains | Switch port security, DHCP snooping, Dynamic ARP Inspection, unused port shutdown | DAI/DHCP snooping need supported switch/network topology |
| **L1 Physical** | Cables, radio medium and hardware | Locks, access-controlled rooms, camera coverage, hardware inventory, physical port controls | **MAC addressing is mainly L2, not L1** |

**Defense-in-depth** means the layers combine so one failure doesn't open every system. It is not a promise that 7 checkboxes defeat all adversaries.

## 5. Stolen-selfies / photo ID leak reel: claims vs transferable lesson

Viral story: a vibe-coded app allegedly exposed about 13,000 identity photos and faced lawsuits/delisting. **Specific incident, user count and legal outcome are unverified from the supplied material; do not quote as established fact.**

The suggested tiers contain useful but incomplete lessons:
- **D:** “We're too small to be attacked” is not a security control.
- **C:** A login wall alone isn't authorization; any registered user might access another's records.
- **B:** Secrets moved server-side help but cannot fix a publicly readable database/bucket.
- **A:** Per-user/tenant DB and storage access rules (Supabase RLS/Firebase security rules), **tested under anonymous and cross-user cases**, are meaningful.
- **“S”:** Ask an AI to test the authorized app as one additional source of findings; it is **not above tested access controls**, nor a substitute for expert security review, verified remediation and independent testing.

For identity photos, minimize collection, restrict access, encrypt and shorten retention, use signed URLs where warranted, audit exports and test direct object access. Preventing public access matters more than an arbitrary tier label.

## 6. Validation and verification before release

- Explicit asset inventory, user roles, permission/access matrix and abuse scenarios.
- RLS object/tenant permission tests, storage bucket policy checks, API authZ tests and old-session revocation.
- Parameterized queries and context-appropriate output encoding.
- Dependency/SBOM scanning, Git secret scan, access logs without sensitive tokens.
- Tested rate limits and cloud budgets.
- Secure deployment configuration, SSH and firewall rules without lockout.
- Staging penetration tests only within authorized scope; production changes reviewed and recoverable.
- Incident monitoring, backups/restore tests, audit trail and owners for remediation.

## Source references

- OWASP SQL injection: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- OWASP ASVS: https://github.com/OWASP/ASVS
- OWASP session management: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- Cloud and access rules: https://supabase.com/docs/guides/database/postgres/row-level-security
- NIST Zero Trust: https://csrc.nist.gov/projects/zero-trust-architecture
- Related existing file: [09 — JWT and Security](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md)

## Eleventh source batch: numbered checks 55–70

[78 — AI-App Security Checks 55–70](78-SECURITY-CHECKS-55-70-GRAPHQL-AND-AI-PERMISSIONS.md) records all sixteen screenshot items **verbatim** with risk-based defensive tests. Topics include MFA, account enumeration, abuse, races, webhook replay, secure CI/actions/dependencies, fail-open checks, timeouts, log redaction, AI output validation/permissions, browser storage, redirects and endpoint/GraphQL authorization. No live penetration test or application security clearance is claimed.

## URL protection additions — route and transport security

[84 — URL Protection in Vibe-Coded Apps](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md) includes IDOR/BOLA, unvalidated redirects, SSRF, URL XSS, data leaks in query strings, CDN/private caches, signed links, domain/takeover/TLS and private staging. 23 defensive test cases are provided with no claim of actual execution. See [85](85-URL-PROTECTION-RESEARCH-SOURCE-REGISTER.md).
