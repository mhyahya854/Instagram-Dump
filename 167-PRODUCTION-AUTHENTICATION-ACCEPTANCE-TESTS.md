# 167 — Authentication and authorization: production acceptance-test contract

**Source:** five-point user-typed production security prompt archived verbatim in [149](149-PRODUCTION-AUTHENTICATION-SECURITY-FIVE-POINT-PROMPT-AND-AUDIT.md). This file adds concrete **tests**, not a claim that an application has been audited or fixed. Consult [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html) and [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/).

## The five original checks and corrected engineering decisions

1. **JWT/session in localStorage:** XSS can read browser storage. HttpOnly, Secure cookies reduce token exfiltration but remain subject to browser requests and CSRF. Apply explicit `SameSite` appropriate to flow, CSRF tokens/origin checks for state mutations, narrow Domain/Path, session rotation on privilege changes and logout invalidation. Secure cookie flags do not remove XSS vulnerability.
2. **Client-only roles:** UI hiding is presentation, not enforcement. Backend checks authentication *and* resource-scoped authorization for each request, including GraphQL resolvers, WebSocket subscriptions, admin exports, bulk APIs and background jobs. Test cross-tenant object ID substitution (BOLA/IDOR).
3. **Missing 2FA/OTP:** prefer passkeys/WebAuthn phishing-resistant factors where supported; TOTP can be a fallback. SMS OTP is less phishing-resistant and exposed to SIM swap. Recovery codes, factor enrollment and recovery require reauthentication and alerts.
4. **No per-route rate controls:** protect signup, login, password reset, token exchange, MFA verification and recovery using a combination of per-account, per-device, per-IP, per-network and global limits, with suspicious-activity alerts. Avoid lockout designs allowing attackers to deny real users indefinitely. Generic reset responses reduce enumeration.
5. **Password rules:** apply currently applicable NIST guidance; screen commonly used/compromised values, allow password managers/paste, Unicode carefully, long passphrases, and strong adaptive password hashing. Don't require arbitrary mixtures of uppercase/numbers/symbols as a universal best practice. NIST 800-63B-4 specifies 15 characters minimum for single-factor passwords and at least 8 when used with MFA in its stated scope; local regulation/policy may differ.

## Test matrix (execute only on authorized test systems)

| ID | Setup and action | Required result |
|---|---|---|
| AUTH-01 | Authenticated user A requests B's object by URL, GraphQL query and background task | Every path denies, logs without leaking B's content |
| AUTH-02 | Regular user calls each admin endpoint with UI bypassed | HTTP 403; backend verifies current roles and resource scope |
| AUTH-03 | Revoke role midway through session | Server stops privileges within documented revocation window |
| AUTH-04 | Logout/revoke all sessions, replay old token | Old session rejected; cookies expired, server sessions invalidated |
| AUTH-05 | Cross-site HTML form triggers authenticated mutation | CSRF defense denies without valid origin/token; approved SSO still works |
| AUTH-06 | XSS fixture attempts `document.cookie` theft | HttpOnly session secret inaccessible to JS; CSP/escaping tested separately |
| AUTH-07 | Session fixation: reuse anonymous session after login | Auth session identifier rotated |
| AUTH-08 | Excess failed passwords and distributed stuffing | Progressive defense blocks abuse without long-term victim lockout |
| AUTH-09 | Valid versus invalid email on forgot-password | Similar generic response/timing; no account existence disclosure |
| AUTH-10 | Repeated/replayed/expired OTP, wrong factor binding | All rejected; one-time-use enforced with bounded retries |
| AUTH-11 | Factor removal/recovery without fresh reauthentication | Denied; recovery event logged/alerted |
| AUTH-12 | Weak/common/breached password and long valid passphrase | Blocklisted rejected; long password accepted; no composition-only restriction |
| AUTH-13 | Concurrent password-reset links after one succeeds | Older links invalid; privilege/security event recorded |
| AUTH-14 | Missing session key, Redis down, stale roles | Protected route fails safely, never accidentally anonymous admin |
| AUTH-15 | Browser secure contexts / staging domain behavior | Cookie flags, redirects, CORS and SameSite validated for deployment topology |

## Implementation checklist

- Inventory trust boundaries, authentication provider, session storage, role graph, privileges, APIs and data classifications. Write a threat model covering credential stuffing, token theft, CSRF, account recovery takeover, privilege escalation and enumeration.
- Adopt server-side deny-by-default policy checks: `authorize(actor, action, resource)`, including owner/tenant binding and audit event on denied sensitive access.
- Use parameterized queries, password-hashing libraries, sensitive-value redaction, secret managers and security headers with a tested CSP. No client-side secret storage can substitute for secure backend design.
- MFA rollout: protect enrollment and recovery, supply backup methods, require factor freshness for sensitive actions; do not require vulnerable SMS for everybody by default.
- Rate limits: use atomic counters, safe fallbacks, metrics and high-signal alerts, and distinguish honest network-shared users from attackers.
- Regression suite: browsers including Safari/Firefox/Chromium where supported, mobile flows, locale/accessibility for passkeys, user-signout behavior, OAuth redirect anti-CSRF state and cookie configurations.
- Evidence per test: code reference, environment, test timestamp, redacted sample request/response, expected/actual result, reviewer and unresolved risk. Never mark a checkbox “passed” merely because the design exists on paper.

## Risk assessment and non-goals

This note does **not** introduce code to a live app, bypass production security or guarantee compliance. The Instagram source asked for drastic changes (“immediately” and universal `SameSite=Strict`); actual changes must account for federated login, embedded contexts, CSRF and user experience. Cross-reference [09](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md), [56](56-AUTHENTICATION-JWT-REVOCATION-DEPENDENCY-SECURITY.md), [84](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md), [149](149-PRODUCTION-AUTHENTICATION-SECURITY-FIVE-POINT-PROMPT-AND-AUDIT.md).
