# Reel Notes 09 — Sessions, JWTs, Access Controls and Security of AI-Built Apps

_Captured 2026-10-25. Corrected technical teaching notes, not production-ready authentication code._

## Reel scenario: dismissed employee still logged in

A former employee's *account* is deleted, but their browser still has a previously issued authentication credential. Whether they can continue accessing the admin portal depends on the token/session model, its revocation, and **server-side authorization policy**. Revocation must be designed and tested, especially for admin actions.

### Server-side session identifier vs signed JWT

| Aspect | Opaque server-side session | Stateless signed access JWT |
| --- | --- | --- |
| Browser holds | A random unpredictable session identifier, typically in an HttpOnly, Secure, SameSite cookie | A signed access token containing claims such as user ID, issuer, audience and expiry |
| Server checks | Looks up session state in database/cache, checks account status and permissions | Validates signature, accepted algorithm, issuer, audience, expiry and relevant authorization policy |
| Immediate revocation | Delete/disable session at shared session store | **Not automatic** if pure stateless validation; can use denylist/introspection/security version or short expiry |
| Typical tradeoff | Stateful central lookup and session-store availability | Fewer lookups, but claims may be stale and revocation needs explicit design |
| Security warning | Never use guessable session IDs | Signed does not mean encrypted; payload often readable and must contain no secrets |

**Correction to reel:** “JWTs can't be revoked” is false. Stateless JWTs are not *inherently* individually revocable, but a denylist, status/introspection, signing-key rotation (broad), token versioning, or an authentication gateway can implement revocation. Five-minute JWT lifetimes limit the *remaining window* only if no other route accepts the old credential.

### Access token and refresh-token pattern

1. After authentication, issue a short-lived access token and a more tightly protected refresh token.
2. Keep a revocable server-side record of refresh sessions (prefer hashed refresh-token values); rotate refresh tokens on use and detect reuse when appropriate.
3. When access expires, an authorized refresh request exchanges the valid refresh credential for a new access token; users need not enter passwords every five minutes.
4. On user termination, **disable the account, revoke all refresh sessions, invalidate server sessions, remove active elevated grants** and consider access-token denylisting/introspection for immediate high-risk revocation.
5. On every privileged request, enforce permissions using authoritative data or sufficiently current security state. A valid JWT signature does **not** mean the holder is still authorized.

**Test:** issue token, disable account, retry admin endpoint with existing access token, retry refresh, and test multiple devices and cache propagation. Expected access denial time must be a documented requirement.

## Another reel: “vibe-coded apps will get hacked / huge cloud bill”

This is a warning scenario, **not statistical proof**. Relevant failure paths:
- Unauthenticated public endpoint flooded by scripted calls causing service/API/cloud costs.
- User-based rate limiting alone failing for unauthenticated visitors.
- Browser-side API keys, production credentials or “secret” environment values appearing in bundles or logs.
- Absent server-side access-control matrix; the agent lacks rules for who can perform which actions.
- Missing input validation, unsafe redirects/uploads, CSRF/XSS/SSRF, insecure webhooks and expensive unbounded model calls.

### Rate limiting and cost control, defense in depth

Consider limits on **IP/network** (account for proxies and shared IPs), account, authenticated identity, session, API key, endpoint, concurrent jobs, request size, token/output costs, daily budgets, and expensive third-party actions. Add upstream quotas and billing alarms. Rate limiting is **not a substitute** for abuse detection or authorization. Prefer accurate HTTP 429 with retry hints, and avoid per-IP limits that indiscriminately block shared users.

### API key rules

- Publicly deliverable browser bundles are **not a secure place** for server secrets.
- Store privileged keys on server-side platforms or a secrets manager; rotate and scope them, or issue limited short-lived credentials where the service supports it.
- Some identifiers intentionally exposed as *public client keys* are not secrets (e.g. a publishable key), but still require correctly enforced RLS, quotas and server checks.
- Do not log raw passwords, authorization headers, refresh tokens, private cookies or signing keys.

### Permission matrix the coding agent must be given

| Action | Anonymous | Ordinary user | Owner of record | Admin |
| --- | --- | --- | --- | --- |
| View public landing page | Yes | Yes | Yes | Yes |
| Read private record | No | No for other users | Yes | Only by authorized support policy |
| Edit private record | No | No for other users | Yes | Explicitly scoped/admin-audited |
| Export all users | No | No | No | Only with approved business need |
| Change roles or billing settings | No | No | No | Restricted/high-risk, step-up auth |

This is **an illustrative example**. Adapt to product roles, ownership, tenancy, actions and data sensitivity. Store rules alongside specifications (\`CLAUDE.md\`/\`AGENTS.md\`), **enforce them in server/database code**, and test denied cases and IDOR across tenants. Prompt instructions alone do not protect endpoints.

## Five named security resources from the reel

| Source | Description and application | Limitation |
| --- | --- | --- |
| **Supabase advisors / MCP** — https://supabase.com/docs/guides/observability/advisors | \`get_advisors\` security/performance finds missing or permissive RLS policies, exposed data, etc. Use least privilege; inspect suggestions before applying. | Cannot prove every RLS policy is safe; add deny/allow policy tests. |
| **TruffleHog** — https://github.com/trufflesecurity/trufflehog | Search for leaked credentials in code/history, and check certain credential validity. | Rotate any confirmed compromise; removal from Git alone is insufficient. |
| **Anthropic Security Guidance** — https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance | Hook-based warnings plus optional LLM reviews for suspicious edits/diffs/commits; can flag injection, XSS, SSRF and auth problems. | LLM reviews can send changed code to configured provider and add cost. Best-effort only. |
| **Google OSV-Scanner** — https://github.com/google/osv-scanner | Compare dependency versions against known open-source vulnerability advisories. | A package without known CVEs is not proven “safe”; inventory, license, maintenance and configuration also matter. |
| **Mozilla HTTP Observatory** — https://developer.mozilla.org/en-US/observatory | Assess observable web security posture, especially HTTPS and security headers. | Grade does not constitute penetration test; a perfect score cannot establish secure business logic. |

Related independent resources: OWASP Application Security Verification Standard (https://github.com/OWASP/ASVS), OWASP Cheat Sheet Series (https://cheatsheetseries.owasp.org/), Gitleaks, ZAP, Semgrep, Trivy.

**Unverified viral figures:** “1.5 million leaked API keys,” “twice as often,” “one in five safe packages,” “15 apps all failing” are promotional numbers with no independently validated methodology supplied. Do not encode them as verified findings.

## Image-location inference and privacy threat

One clip claims an AI could infer where a photographed oven and field are located even when camera GPS is disabled. **The specific clip's claimed accuracy is unverified.** Images can reveal *visual* location clues independent of metadata (plants, weather, landmarks, road features, architecture, reflections and distinctive objects); disabling geotagging removes only one evidence source. Before public posting, consider cropping sensitive backgrounds, checking shadows/reflections and metadata, reducing precise timing or combining multiple photos. Avoid sharing a precise private location through posted visual clues. Do not treat “no EXIF GPS” as anonymity.

## Verification checklist

- [ ] Account termination revokes sessions, refresh tokens and access to sensitive operations within documented time.
- [ ] Server/API/database enforce a written access matrix; user/tenant ID changes cannot expose others' records.
- [ ] Tokens: signature, algorithm allowlist, expiry, issuer and audience validated; transport and storage safe.
- [ ] Credentials are scoped, short-lived or rotatable; production keys never exposed to untrusted clients.
- [ ] Public and authenticated endpoints have tested abuse controls and cost limits.
- [ ] RLS audited for all relevant tables/views/functions and tested for negative/anonymous access.
- [ ] Input/upload validation, CSRF/XSS/SSRF, webhook verification and dependency scanning covered.
- [ ] Security logs/audits and incident response work without recording raw secrets.
- [ ] Relevant scanners run on authorized systems only, with reviewed outputs.

## Sources

- OWASP JWT guidance and revocation options: https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html
- OWASP Session Management: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Supabase advisors: https://supabase.com/docs/guides/observability/advisors
- Security Guidance: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/security-guidance/README.md
- HTTP Observatory limits: https://developer.mozilla.org/en-US/observatory/docs/faq
