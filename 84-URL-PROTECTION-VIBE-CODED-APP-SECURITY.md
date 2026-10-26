# 84 — URL Protection for Vibe-Coded Apps: Routes, Links, Redirects, SSRF and Share Tokens

**Captured 2026-10-26.** Source: user's typed topic **“url protection in vibecoded apps”**. No specific application, framework, source repo, or video was supplied. The risks, examples, tests and sources below are **independently researched security guidance**, not a completed penetration test. This belongs under the security/production category of Instagram-Dump; **no change has been made to Universal-Rules**.

## Core rule

**A URL is untrusted input and not an authorization credential by itself.** A page might be hidden in navigation, use an unguessable UUID, or have a seemingly private link, but the server must still enforce who is allowed to use each endpoint and read or modify each object. Validate every URL before using it for navigation, embedding or server-side fetching.

An AI coding agent must not report “all URLs are protected” because a route is behind a React page or the homepage has a login button. Test the **underlying API** with an unauthorized user and an authenticated user who owns a different object.

## 1. Threat model: different meanings of “URL security”

| Area | Failure mechanism | Correct control |
|---|---|---|
| **Protected pages/routes** | Typing a private URL directly bypasses frontend navigation or middleware | Real server-side session/auth check, role policy and per-object permission |
| **IDOR / BOLA** | Change `/invoices/1042` to `/invoices/1043` and receive another person's invoice | Derive requester identity from verified session, enforce tenant+object owner on every read/write |
| **Exposed IDs and secrets** | Signed session token, private API key, password, or personal data in query parameters | Avoid sensitive secrets in URLs, use secure cookies/headers, redact logs; narrowly scoped short-lived one-time recovery links when required |
| **Open redirects** | `/login?next=https://evil.example` sends a trusted site's visitors elsewhere | Server-side route identifiers, strict local path policy or validated canonical destination allowlist |
| **Unsafe outbound URL fetch / SSRF** | `/api/preview?url=...` fetches cloud metadata/internal network/localhost | Strict allowlist or robust URL/IP/DNS validation at connection time, outbound network isolation, no unsafe redirects |
| **Unsafe clickable links** | User profile/Markdown/AI output makes `javascript:`, `data:` or misleading URL executable | Use URL parser, safe scheme policy, contextual escaping, safe rendering and confirmation for external destinations |
| **Download/share URLs** | Public file link allows indefinite access, guesses IDs or leaks other tenants' files | Authentication when required, short-lived least-scope signed links, storage permission checks, revocation plan |
| **OAuth/callback URLs** | Attacker controls redirect URI or login return destination, steals authorization flow | Exact allowlisted redirect URI, state, PKCE where applicable, secure callback handling |
| **Webhook/callback registration** | External user sets callback to internal endpoint or privileged network | Treat registered callback URLs as SSRF input; verification, allowlist/network controls, signing, replay rejection |
| **Unsecured APIs** | “Hidden” admin routes, GraphQL mutations or server actions usable by direct HTTP | Authorization in handler/domain service, ownership validation and negative tests |
| **URL-based XSS** | Query/hash parameters are rendered as HTML or dangerous link/sink | Framework escaping, maintained sanitization, URL validation, CSP as defense in depth |
| **Phishing/link previews** | App displays a misleading short link or opens an untrusted site without clarity | Canonical destination preview; user-visible origin; suspicious domain/scheme checks where relevant |
| **Caching/crawlers** | Private results cached by CDN or exposed in sitemaps / indexed previews | Appropriate Cache-Control, authenticated cache keys, private URL removal from indexable pages |

**Use-case priority:** an authenticated private personal journal needs object authorization and share controls; a public URL-shortener or web screenshot service also needs strong open-redirect, abuse and SSRF defenses; a marketplace must protect purchase/payment/order URLs.

## 2. Protection is enforced at the server, not just in the UI

### A common bad pattern

```ts
// Illustrative vulnerable design — do not copy into production:
const invoice = await db.invoice.findUnique({
  where: { id: request.params.invoiceId }
});
return invoice; // Missing tenant/user authorization
```

The client may hide the page, but direct API requests still return the record.

### Correct pattern, framework-neutral pseudocode

```text
request = authenticated session
currentUser = verifySession(request)
if not currentUser.active: deny 401/403
invoice = database.getInvoiceByIdAndOwner(
  invoiceId = validatedRequestPathId,
  ownerId = currentUser.id
)
if invoice not found: return 404 (or policy-appropriate 403)
return permittedFieldsOnly(invoice)
```

Every operation—including update, delete, export, batch fetch, nested GraphQL resolver, storage download and signed file URL issuance—must apply the same policy. UUID or slug obscurity **supplements** but never replaces authorization. Roles need current-state checks where account suspension/revocation matters. Avoid trusting `userId` or `role` sent by browser.

**Supabase implementation note:** enforce Row Level Security policies for exposed Postgres data with correct JWT identity, and test both read and write; privileged service-role credentials must stay server-side. **Appwrite implementation note:** use collection/document-level server-enforced permissions and avoid shipping privileged API keys to browser/mobile clients.

## 3. Safe links: distinguish validation from escaping

- **Parse** using standard library URL parser (not a regex-only or `startsWith` domain check).
- Only permit appropriate schemes: generally `https:` for external web links; same-site paths can be internal routes. Explicitly reject `javascript:`, `data:`, `file:` and unsupported schemes in browser navigation and HTML links.
- For an external domain allowlist, compare normalized hostname + effective port + scheme, not string prefixes such as `trusted.com.evil.example` or `trusted.com@evil.example`.
- Percent-encode **query parameter values**, not a whole raw URL; validate URL before rendering into `href`/`src` and use correct HTML attribute/context escaping.
- Treat AI-generated Markdown links and social profile URLs as user-controlled inputs.
- New-tab external links should avoid exposing `window.opener`: use suitable `rel="noopener noreferrer"` and explicit destination disclosure where warranted.
- A suspicious-looking URL does not necessarily mean malware; validation/security scanners have false positives.

**Do not** strip all punctuation from URLs or rely solely on browser HTML sanitization; this can break valid links without preventing parser differentials.

## 4. Safe redirects after login and in OAuth

**Never blindly do:** `redirect(request.query.next)`.

Preferred design:
1. Define internal route **names** or approved relative paths that map to application destinations.
2. For external destinations, resolve an explicit approved destination ID into a stored URL instead of taking arbitrary full URLs.
3. If parsing untrusted URLs is necessary, enforce canonical origin/scheme/port/path allowlists using the same parser semantics as the eventual redirect API.
4. Reject `//attacker.example` (scheme-relative), encoded/backslash variants where relevant, userinfo `@host` confusion, unexpected scheme and unsupported port.
5. For OAuth use precisely registered redirect URI(s), state validation, PKCE for public clients where appropriate, and never echo arbitrary callback URL parameters.

Note: A login redirect cannot simply be “relative-looking”; strings with two leading slashes or parser discrepancies may still navigate off origin. Use framework-supported **local redirect** functions that actually reject external URLs.

## 5. SSRF: when your server fetches a user-supplied URL

Dangerous features: link previews, web page summarization, image-from-URL import, screenshot services, remote-file import, webhook callbacks, PDF conversion, avatar fetch and AI browser tools.

**Risk:** the server has network access the requester lacks. A crafted URL may target private service IPs, localhost, instance metadata, cloud control interfaces or intranet endpoints. URL parsing alone is insufficient.

**Defense in depth:**
1. Avoid fetching arbitrary URLs; prefer fixed provider APIs and preapproved hostnames.
2. Permit only necessary protocols (typically HTTPS), hostnames and ports. Reject credentials/userinfo, fragments if unnecessary, and overly long URLs.
3. Resolve DNS and **validate every resolved A/AAAA address** against blocked ranges; account for IPv4/IPv6, private, loopback, link-local, multicast, reserved and cloud metadata. Validate final socket destination, not DNS only once, to resist rebinding or proxy behavior.
4. Disable redirects by default; if product requires them, re-run URL and destination IP validation on **every hop** with strict hop count.
5. Use network-level outbound restrictions and deny internal/private destinations even if validation code fails. No broad access to cloud metadata APIs.
6. Set connect/read/total timeouts, response byte/streaming limits, content-type handling, request method controls and per-user quotas.
7. Don't forward app cookies, credentials or Authorization headers to unknown destinations.
8. Record safe structured audit metadata and denied attempts without saving private response bodies unnecessarily.

**Critical:** `!hostname.includes("localhost")`, `url.startsWith("https://")`, or a one-time DNS check before the actual HTTP client fetch are **not** complete SSRF protection. Different clients/proxies can resolve, normalize or follow redirects differently.

## 6. Signed download URLs and public sharing

Useful for storage files that need temporary access. Treat **signed URLs as bearer capabilities**: anyone with the complete link may exercise whatever scope it grants until it expires or is revoked.

- Store objects private by default; verify owner/tenant permissions **before generating** share URLs.
- Limit link to specific file/action, short suitable expiry, optional max downloads/one-time use or additional auth for high-risk data.
- Use unpredictable cryptographically secure values and an authenticated server-side signing method or storage provider's presign API.
- Prevent path traversal or arbitrary object-path creation; never let an untrusted client choose another tenant's storage key.
- Avoid logging full signed URLs, leaking them through analytics, referrers, screenshots, third-party previews and support tickets.
- Revocation may require deleting the object, rotating signing credentials, issuing revocation records or changing storage policies; **short expiry alone is not instant revocation**.
- For file uploads validate size/type server-side and scan where product threat model calls for it; presigned upload permission must not become read access to all objects.
- **Password reset and email verification links** are special one-time bearer tokens; don't send raw token values to trackers, and enforce expiry and single use.

## 7. Protect sensitive URLs from accidental disclosure

- Do not put access tokens, API secrets, session IDs, medical data, or complete private documents directly in ordinary query strings. HTTPS encrypts transit but URL paths and queries may still reach browser history, logs, third-party telemetry, and in some circumstances referrers.
- For protected pages, set appropriate **Cache-Control** and restrict CDN caching. Personal data should not be rendered into shareable Open Graph meta tags.
- Use appropriate `Referrer-Policy` such as `strict-origin-when-cross-origin`, `same-origin` or `no-referrer` according to data sensitivity. **This is defense in depth, not permission to embed long-lived secrets in URLs.**
- For session authentication prefer robust HttpOnly, Secure, SameSite cookies where framework supports; keep CSRF protection consistent with auth scheme. Client-side URL fragments are not a safe permanent secrets store.
- Remove private routes from sitemaps; `robots.txt` is **not** a protection mechanism.

## 8. Test matrix — required evidence for vibe-coded apps

| Test ID | Example on an app you own (staging/test fixtures) | Expected proof |
|---|---|---|
| URL-01 | Open `/dashboard` logged out | Redirect to real login or reject, and underlying API inaccessible |
| URL-02 | User A requests user B's invoice ID or UUID | 403/404; no private fields, update or export |
| URL-03 | Request admin endpoint as ordinary signed-in user | Forbidden at server handler, not only hidden nav |
| URL-04 | `/login?next=https://attacker.example` | Never sends browser off site automatically |
| URL-05 | Try scheme-relative `//attacker.example` and deceptive host variants | Local/external destination validation denies |
| URL-06 | Insert `javascript:` or `data:` into user profile link | Rejected or rendered harmless; no script execution |
| URL-07 | Link-preview fetch attempts loopback/private/link-local/mock metadata target | Outbound network request denied at connection |
| URL-08 | Approved URL redirects to private address | Redirect blocked; no internal fetch or response |
| URL-09 | Repeated URL fetch with DNS changes, IPv4/IPv6 and malformed encodings | Validated at actual connection; no bypass |
| URL-10 | Share link with expired/revoked signature | No file bytes returned |
| URL-11 | User A asks server to sign user B's private file | No signed URL issued |
| URL-12 | Sensitive route with telemetry and external resource | No token/private query leaked to Referer, logs or analytics |
| URL-13 | OAuth callback with unregistered `redirect_uri` | Rejected; state/PKCE checks work |
| URL-14 | Malformed, unusually long, nested, or ambiguous URL | Stable error; no crash, open redirect, high bill or excessive resource use |
| URL-15 | Logout/ban then call privileged action with still-valid token | Current authorization denies high-risk actions |
| URL-16 | Query/list/export/webhook/GraphQL variants of same record | Same ownership and permission checks |
| URL-17 | Malicious/unexpected markdown link in agent-generated UI | Scheme validated, origin displayed and no unauthorized redirect |
| URL-18 | CDN or reverse proxy caches an authenticated response | User B cannot receive User A's cached response |

Results must be actual tests on the correct commit/build with fixture identities. Classify **PASS / FAIL / BLOCKED / NOT RUN** and attach logs/request results without secrets. A URL that looks normal in Chrome isn't evidence of backend security.

## 9. Checklist for the AI coding agent

```text
Audit URL and route security in this application using source code and
authorized staging/test fixtures only. Do not make destructive production
changes. Enumerate protected pages, every underlying API/server action,
object IDs in paths and queries, return/redirect links, OAuth callbacks,
file/share/signed URLs, webhook targets, Markdown/user-created links,
and all code that fetches a user-controlled URL server-side.

For every entry point:
- Identify identity, roles, tenant/object ownership and expected behavior.
- Verify server-side authN/authZ (including suspended account and negative
  cross-account scenarios); don't rely on frontend route hiding.
- Validate canonical URL scheme/host/port/path and close open redirects.
- Review SSRF controls with DNS, IP and redirect revalidation plus egress
  restrictions. Never fetch a real internal endpoint during testing.
- Protect signed URLs/tokens, sensitive query strings, caches/referrers,
  unsafe DOM URLs, OAuth callbacks, and insecure share permissions.
- Add unit/integration/browser tests covering permitted and denied cases.
- Run existing test suite and record actual command results; preserve behavior.
- Present a route-by-route matrix with severity, repro, change, exact files,
  evidence, remaining risk and things not tested.
- Never say "protected" if checks were not actually run.
```

This is a **reusable goal-oriented audit prompt**, not evidence that any app has been audited. For production secrets, payments, live customer accounts and network changes, require explicit human authorization and qualified review.

## 10. Resources and reading (high-authority)

- OWASP: **Insecure Direct Object Reference Prevention** — https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html
- OWASP API Security: **Broken Object Level Authorization** — https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/
- OWASP: **Unvalidated Redirects and Forwards** — https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
- OWASP: **Server-Side Request Forgery Prevention** — https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- MDN: **SSRF** — https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/SSRF
- OWASP: **Cross-Site Scripting Prevention** — https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet
- OWASP: **Information Exposure Through Query Strings** — https://community.owasp.org/vulnerabilities/Information_exposure_through_query_strings_in_url
- MDN: **Referrer-Policy** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referrer-Policy

## 11. Related archive documents

[03 — Production Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md); [09 — Authentication and Session Risks](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md); [20 — App/Server Security](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md); [56 — JWT and Dependencies](56-AUTHENTICATION-JWT-REVOCATION-DEPENDENCY-SECURITY.md); [57 — Security Verification](57-RETICLE-ADVERSARIAL-REVIEWS-SECURITY-GATES.md); [78 — Security Checks 55–70](78-SECURITY-CHECKS-55-70-GRAPHQL-AND-AI-PERMISSIONS.md); [37 — Prelaunch Checklist](37-WEBSITE-PRELAUNCH-RELEASE-CHECKLIST.md).

**Status:** thorough URL security research note and test plan completed; no code repository, deployed URL, network, browser session, payment route or public site tested. No third-party scanning, package installations, production updates, or Universal-Rules changes.
