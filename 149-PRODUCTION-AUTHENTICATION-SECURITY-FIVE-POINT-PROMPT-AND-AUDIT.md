# 149 — Five-Point Production Authentication Security Prompt: Exact Source + Safer Audit Contract

**Source:** the user's **directly typed text** after the seventeenth Instagram screenshots, starting “This is a production app.” In the established Instagram-Dump context, this is preserved as a **research prompt**. **No actual production application or codebase was identified in this turn**, and the prompt is **not authorization to change any existing deployed system**. Original instructions are reproduced exactly below first; technical corrections and a replacement safer audit goal follow.

## Exact supplied text (unaltered)

```text
This is a production app.
1. SESSION TOKEN IN LOCALSTORAGE:
Check if you are storing session tokens / JWTs in localStorage. If you are, move them to httpOnly, Secure, SameSite=Strict cookies immediately. localStorage is vulnerable to XSS / cross-site scripting. Implement proper session handling.
2. CLIENT-SIDE ADMIN CHECKS:
Find all places where admin checks / role checks are happening only on the client-side / frontend. All authorization logic must be enforced on the SERVER / BACKEND. Remove any `if (user.isAdmin)` checks from frontend and add middleware on every admin API route.
3. NO 2FA OR OTP:
You didn't implement 2FA. Add support for 2FA / OTP. Add:
- TOTP / authenticator app support OR email OTP
- Backup codes
- Enforce 2FA for admin users
- Proper OTP expiry and rate limiting
4. /LOGIN HAS NO RATE LIMITING:
Add aggressive rate limiting to /login, /signup, /forgot-password, /reset-password, and /verify-otp endpoints.
- Implement IP-based rate limiting (e.g., 5 attempts per 15 min)
- Implement account lockout after failed attempts
- Add CAPTCHA after 3 failed attempts
- Add exponential backoff
- Log all failed attempts
5. NO PASSWORD STRENGTH CHECK:
You have no password strength enforcement on frontend OR backend.
- Add zxcvbn or similar on frontend with real-time feedback
- Enforce on backend: min 12 chars, require upper/lower/number/symbol, check against haveibeenpwned / common passwords list (top 10k)
- Block passwords like "password123", "12345678"
- Show password strength meter
After fixing, run a final security audit and list what you changed.
Do NOT skip any.
```

## Why some advice must be corrected before a real deployment

### 1 — Token in localStorage

**Substantively supported.** Browser `localStorage` is script-readable; XSS can steal bearer tokens. Prefer secure HttpOnly session cookies or a backend-for-frontend with server-held tokens. **But don't blindly migrate a live app immediately without testing** existing OAuth flows, browser clients, callback redirects, logout, refresh rotations and session invalidation. **`SameSite=Strict` is a strong default for many first-party apps but can break valid cross-site login/redirect workflows**; choose based on threat model (possibly Lax). `HttpOnly` is not an XSS cure; cookies also need correct CSRF protections, Secure, path, TTL, access controls and rotation.

### 2 — Server-side admin authorization

**Correct principle:** server enforces authorization on *every* sensitive resource/action, not just routes labelled `/admin`. **Do not literally remove all frontend `if (user.isAdmin)` checks**: client controls can still hide/show navigation for usability, provided all server routes independently validate role, tenant, record ownership and permission. Add deny-by-default enforcement, negative tests (normal user, unauthenticated, deleted user, wrong tenant) and recheck after role revocation. Protect GraphQL/actions/webhooks/background jobs and storage URLs too.

### 3 — 2FA/OTP

MFA is important for admins/high-risk actions. Prefer **phishing-resistant passkeys/WebAuthn** where appropriate; TOTP authenticator apps can be useful, but **email OTP is weaker** when mailbox is compromised. Backup codes must be hashed securely, single-use, rotatable/recoverable with account takeover defenses. Define enrollment/recovery, device loss, lockout and admin step-up flows before launch; blindly forcing MFA could lock out existing users/operators.

### 4 — Login and recovery rate limiting

Use distributed rate limiting per IP **and** per account/identifier/device/risk context, with privacy-respecting monitoring. The source `5 per 15 min` and CAPTCHA at `3` failures are **illustrative thresholds**, not universal OWASP/NIST requirements. Fixed hard account lockout can be abused for denial-of-service; prefer progressive delays, throttling, challenge/notification and careful recovery policy. Avoid leaking whether accounts exist; mask personally identifying log data.

### 5 — Password requirements

**Critical conflict with current NIST SP 800-63B-4 guidance:** standard recommends **do not impose character-type composition requirements** (uppercase/lowercase/numeric/symbol). Instead use length, blocked compromised/common passwords, whole password acceptance, password managers/paste/autofill, Unicode policy, safe hashing (Argon2id or otherwise recommended slow salted verifier), throttling and breach checking with privacy-preserving methods. NIST requires **minimum 15 characters for passwords used as the sole factor**, but permits **8 minimum when used as part of MFA**; support at least 64-character max. The original arbitrary `min 12` and forced symbols are **not** universal defaults. Zxcvbn can provide helpful client feedback but **backend validation is authoritative**. HIBP Pwned Passwords k-anonymity or other privacy-preserving mechanism must be evaluated; never send raw passwords in telemetry.

## Corrected production goal for a future authorized code agent

> Audit the **specified repository, branch, staging deployment and auth flows** using read-only discovery first. Build an access-control matrix and threat model. Enumerate login/session/refresh/recovery/MFA and privilege boundaries. Report current evidence and negative tests for token exposure, CSRF/XSS/session lifecycle, server-side authorization, admin recovery, brute force/account enumeration and password policy. Propose safe isolated patches in reviewed commits; never mutate production database, auth provider settings, live sessions, secrets or schema without explicit approval and rollback plan. Implement standards-conformant defenses chosen for the actual app architecture, then run deterministic unit/integration/E2E, permission-crossing, race/retry and logout/revocation tests. Include before/after evidence, residual risks, settings that still require human operator action, and explicit not-applicable status. No blanket “secure” claim or invented green audit.

## Evidence and acceptance checklist

| Area | Acceptance evidence | Negative test |
|---|---|---|
| Session | Cookies configured, secure transport, rotation/expiry/logout | Stolen/expired/revoked token fails; XSS cannot read HttpOnly session secret |
| Authorization | Deny-by-default server policy across routes, jobs, files, tenants | Client modifies role/local flag; server still refuses |
| MFA | Enrollment/recovery/admin step-up, single-use backup, replay and anti-phishing consideration | Reused OTP or backup code rejected |
| Rate limit | Budgeted distributed throttles and monitoring | Rapid distributed attempts throttled; account enumeration minimized |
| Passwords | NIST-aligned minimum, compromise blocklist, correct hash | Common leaked/password breached rejected; long passphrase accepted |
| Migration | Planned change, staging regression, rollback, incident controls | Existing allowed login/OAuth flows still work; no lockouts introduced |

## References (independent, not in original typed text)

- NIST SP 800-63B-4 https://pages.nist.gov/800-63-4/sp800-63b.html
- OWASP Session Management https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- OWASP Authentication https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- OWASP Authorization https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP CSRF https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html
- OWASP Password Storage https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

**Status:** original prompt fully archived with corrected analysis; no source application specified, scanned, changed, deployed or claimed secure. Related [03 — Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [84 — URL Protection](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md), [85 — URL Protection Source Register](85-URL-PROTECTION-RESEARCH-SOURCE-REGISTER.md), [143 — Strix](143-STRIX-PAGE-AGENT-MEETILY-TRENDING-THREE.md).
