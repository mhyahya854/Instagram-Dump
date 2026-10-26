# 56 — JWT Revocation, Banned Users and AI Dependency Supply-Chain Security

Captured 2026-10-26. Two security reels. Keep the story as an **illustrative failure mode**, not verified incident evidence. No security test against a real application performed.

## A. A banned user still makes purchases

### Reel scenario

A malicious user is banned or deleted, yet an old browser continues to send purchases using a **self-contained bearer JWT**. If the server validates only signature, expiration and limited claims without checking current account state or revocation, token access can remain valid until token expiry. **Security lesson:** user account deletion alone may not invalidate cached authorization.

**Important corrections to the spoken explanation:**
- JWTs are a **token format**, not inherently stateless auth and not inherently “faster.” Systems may combine JWT validation with session checks, a denylist, key rotation or introspection.
- Opaque session IDs can be invalidated centrally; actual revocation depends on caches, API gateway and consistency.
- Five-minute access JWTs plus revocable refresh tokens **bound typical residual access** to five minutes, but do **not** provide **instant** termination by themselves. High-risk operations should re-check ban/account/payment status directly, or use a shared revocation/version store/denylist.
- A signed token prevents claim tampering only if algorithms, issuer, audience, signing keys and verification are configured correctly. Token **theft and replay** remain risks.
- A 30-day token is not a secure default for sensitive purchases; expiry is app-specific.
- Refresh tokens need hashing/secure storage where applicable, rotation, theft detection, expiry and full family revocation; logout, password reset and account deletion should revoke sessions.

### Options and trade-offs

| Pattern | Revocation | Trade-off |
| --- | --- | --- |
| Opaque session ID with server store | Invalidate session record (allow cache lag) | Central lookup/scaling/storage costs |
| Short-lived signed access JWT + revocable refresh token | Revoke refresh immediately; access JWT expires later unless separately denied | Residual token validity, issuer/audience/key discipline |
| JWT + account status/version check on high-risk actions | Can enforce effective block without waiting for expiry | Requires authoritative current state and failure behavior |
| Access JWT denylist/token family tracking | Faster targeted revocation | Stateful list distribution, expiry and operational complexity |
| Reference token/introspection | Centralized policy at token use | Network dependency and availability considerations |

### Correct purchase authorization

1. Authenticate an access token with strict signature/issuer/audience/algorithm checks.
2. **Authorize the current principal:** exists, active/not banned, allowed purchase scope, correct tenant, linked account status. Use authoritative state for payment and costly operations.
3. Check card/token ownership/permission with payment provider; never trust client price/card status or editable quota.
4. Enforce rate limits, fraud signals, purchase caps and idempotent transaction keys.
5. Audit failed ban/old-token test; do not process a charge then hide it behind UI.
6. Test every denial: banned user, deleted account, expired/revoked refresh, cross-tenant, stale JWT, copied/forged token.

**Acceptance:** a banned account must not successfully initiate *new purchases*, even if the access JWT hasn't expired. Use direct account-state authorization at the critical action boundary.

Primary background: OWASP Session Management and JSON Web Token cheat sheets:
https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html

## B. Agent downloads malicious dependencies

A dependency is external software whose package, update script or transitive import runs in the developer's or application environment. An AI coding assistant can pick a typo-squatted, compromised or maliciously packaged dependency while trying to “fix a missing module.” The speaker's anecdote is **plausible, not verified** for any named agent.

### Practical policy

**Avoid automatic install-on-error**: no arbitrary npm/pip/cargo/PowerShell/bash commands from a retrieved README, webpage or tool output without permission and inspection.

1. Identify **why** a new package is needed; prefer existing dependencies/standard library.
2. Verify package name **character by character**, publisher/repository, registry ownership, age, maintainers and installation scripts.
3. Pin versions/lockfiles; use hashes/signatures/SLSA provenance where supported.
4. Inspect scripts, particularly preinstall/postinstall, dynamic URL fetches, obfuscated code, telemetry and credential access.
5. Run dependency and SBOM checks in CI; do not automatically accept all warnings or force upgrading into incompatibility.
6. Run tests and scan transitive dependencies. A clean scan does **not prove absence of malware**.
7. Restrict build agent rights: no production secrets, separate CI credentials, minimal network egress, read-only filesystem where possible.
8. Make ongoing checks automatic at pull request/merge, with human-approved remediation and a reliable rollback.

### Tools for this class of risk

- OSV-Scanner: https://github.com/google/osv-scanner
- TruffleHog secret scanning: https://github.com/trufflesecurity/trufflehog
- Dependency-Track SBOM risk: https://github.com/DependencyTrack/dependency-track
- GitHub Dependabot: https://docs.github.com/en/code-security/dependabot
- Socket package risk context: https://socket.dev/
- npm audit / pip-audit / cargo audit, ecosystem specific.
- SkillSpector for agent skill security: https://github.com/NVIDIA/SkillSpector

**Caution:** vulnerable/deprecated dependencies and intentionally malicious packages are different threat classes. CVE scanners don't necessarily catch fresh typosquatting attacks. A “suspicious” warning needs investigation, not automatic deletion.

## Verification examples

- Old JWT: use test users in staging; set account banned and prove payment API denies even with otherwise-valid token.
- Dependency injection: substitute a benign fixture package with a dangerous postinstall flag; install must be blocked or approved by policy.
- CI: verify lockfile changes and audit results are attached to the specific commit, never invented.
- Secrets: scan git history and rotate exposed credentials; deleting a committed key from new code is not enough.

Related: [09 — Sessions Security](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md), [20 — App Security](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md), [03 — Production Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).

## URL-boundary protection complement to JWT/session rules

[84 — URL Security Guide](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md) covers access tokens in URLs/logs, session-protected direct deep links, short-lived signed file URLs, account-state checks and URL-derived domain/redirect risks. URL obfuscation is **not** an authorization policy; client hidden buttons cannot protect backend operations.
