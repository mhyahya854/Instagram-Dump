# 85 — Source Register: URL Protection in Vibe-Coded Apps

**Captured:** 2026-10-26, user-typed request **“url protection in vibecoded apps”**. This is **one direct research subject, not a verified reel or source screenshot**. No specific app, stack, GitHub repo, target domain or deployment environment was supplied.

## What was researched and where

Full offline-readable engineering guide: [84 — URL Protection in Vibe-Coded Apps](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md).

| Topic | Source provenance | How the archive treats it |
|---|---|---|
| Protect private pages and APIs | Independent OWASP access control research | Auth must be server-enforced; UI route hiding insufficient |
| IDOR / BOLA (changing URL record IDs) | OWASP IDOR prevention and OWASP API1 | Every path ID, UUID, storage key and object query must enforce ownership |
| Redirects and OAuth return URLs | OWASP Unvalidated Redirects | Use canonical validated destinations and exact callback policy |
| Unsafe URL preview/fetch (SSRF) | OWASP/MDN SSRF guidance | Allowlist, DNS/IP and redirect revalidation, egress restrictions |
| Malicious clickable / AI-generated links | OWASP XSS Prevention | Validate schemes and origins; use contextual escaping/rendering |
| Private share/download and presigned links | Original independent engineering analysis | Treat signed links as bearer capabilities with scoped access, expiry, revocation considerations |
| Sensitive URL leakage | OWASP query-string exposure + MDN Referrer-Policy | Don't place sensitive tokens in URLs; manage logs/caches/referrers |
| DNS, subdomains, TLS, host headers, staging, deep links | Independent operational security checklist | Inventory domains and protect preview endpoints and host-based link generation |
| QA | 23 original suggested URL safety test cases in file 84 | Suggested authorized test plan; **not tests actually run** |

## The user did NOT supply

No suspicious URL, actual exploited endpoint, application source, framework, token, deployed site, original video/creator, production log or test results. Therefore this collection is **general defensive knowledge**, not a vulnerability report for a particular app.

## Security and quality constraints

- Research notes include **illustrative examples only**, with clearly distinguished vulnerable and safe patterns.
- Testing is appropriate only on user-owned/authorized staging systems.
- Route protection, API authorization, network URL fetching safety, web link display safety and domain management are **separate control families**; no single regex, login component, reverse proxy or AI security skill solves all of them.
- No scans, installs, staging attacks, code changes, credential rotations, live app tests, purchases or Universal-Rules edits were done.
- Proposed future project quality rule: *For every URL-driven operation, identify trust boundary and enforce safe policy at the server/data/action boundary, then verify success and denial cases with evidence.* This note is **not a ratified rule update**.

## Authoritative resources

- OWASP IDOR: https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html
- OWASP URL redirects: https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
- OWASP SSRF: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- OWASP XSS: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet
- MDN Referrer Policy: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy

Earlier registers: [16](16-INSTAGRAM-REELS-SOURCE-REGISTER.md), [24](24-INSTAGRAM-REELS-OCT25-BATCH-REGISTER.md), [31](31-INSTAGRAM-REELS-THIRD-BATCH-REGISTER.md), [36](36-INSTAGRAM-REELS-FOURTH-BATCH-REGISTER.md), [43](43-INSTAGRAM-REELS-FIFTH-BATCH-REGISTER.md), [52](52-INSTAGRAM-REELS-SIXTH-BATCH-REGISTER.md), [60](60-INSTAGRAM-REELS-SEVENTH-BATCH-REGISTER.md), [65](65-INSTAGRAM-REELS-EIGHTH-BATCH-REGISTER.md), [67](67-INSTAGRAM-REELS-NINTH-BATCH-REGISTER.md), [75](75-INSTAGRAM-REELS-TENTH-BATCH-REGISTER.md), [83](83-INSTAGRAM-REELS-ELEVENTH-BATCH-REGISTER.md).
