# 135 — Free Developer Subdomain: runs-on.dev (Exact Screenshot Match)

**Source:** image 8 of sixteenth Instagram batch. The tilted page shows **“Vercel links are dead”**, a large `[yourname].runs-on.dev` example, a dot-map and a claim UI. This is **marketing wording from a screenshot**, NOT evidence that Vercel services or `.vercel.app` URLs have stopped working.

## Correct service and code source

- **https://runs-on.dev/** — verified active subdomain registry.
- Public GitHub: **https://github.com/zordhalo/runs-on.dev** .
- Quickstart: **https://runs-on.dev/docs/quickstart** .
- FAQ: **https://runs-on.dev/faq** .
- Abuse/reclaim policy: **https://runs-on.dev/policy** .
- Original screenshot sample: `[yourname].runs-on.dev` (literal placeholder, **not** a name automatically reserved for the user).

## What a free subdomain actually provides

A unique host **`yourname.runs-on.dev`** under the provider-owned **`runs-on.dev`** second-level domain, with HTTPS for the provider's own initial GitHub profile card and the ability to point the name at your own hosting with supported DNS record configuration. Registry data is public as `domains/<name>.json`, including GitHub account ownership and claim timestamps. This is **not** a transferable purchased top-level domain.

According to the provider's current docs:
- **One name per GitHub account**.
- Account must be **at least 30 days old** and have **at least one public repository**.
- Label **2–32 characters**, lowercase letters/numbers/internal hyphens, no leading/trailing hyphen.
- Authenticate through GitHub OAuth. Review OAuth scopes before approving; do **not** send credentials to a third-party agent, paste GitHub tokens into chat or allow unreviewed browser automation to register names.
- Naming availability is live and **not checked or reserved in this task**.
- Site and GitHub docs state **free forever**, but the **policy allows reclamation for dormant names** and immediate reclamation for impersonation/phishing/malware/illegal use. There is **no guaranteed uptime** and shutdown of the parent domain would affect subdomains.

## Safe claim process (reference only — no claim submitted)

1. Choose a non-impersonating label and an account with required age/public repo; verify intended public exposure.
2. Open official https://runs-on.dev, verify hostname and inspect GitHub OAuth grants.
3. Enter label and check live availability, then initiate claim **only if user explicitly approves** the specific label and service terms.
4. Confirm public `domains/<label>.json` record associates correct authorized GitHub owner. Don't insert secrets or private customer data into the JSON.
5. Use published docs for DNS target (A/AAAA/CNAME or provider's supported target). Verify TXT/SSL/certificate ownership as needed, TLS/redirect and CAA, and ensure hosting actually works.
6. Add health checks and separate primary domain if business continuity matters; document expiry/reclaim risk and migration plan.

## Why it belongs in a developer resource archive

Convenient memorable demo URLs without paying for a domain, good for portfolios, proofs of concept, prototypes and learning. **Not an uptime/service-level equivalent to a registered company domain**, and “free forever” can change.

## Security/operations caveats

Public GitHub OAuth and owner metadata; prevent hosting private data under new public URL; verify HTTPS end-to-end, cookies SameSite/Secure/domain scopes, proper CORS/origin allowlist, OAuth redirect URIs and anti-takeover policies. Browser/agent attempts to claim must require explicit user action.

**Status:** official site, repo and FAQ verified. **No GitHub OAuth requested, label checked, claim submitted, hosting configured, domain or DNS updated, or Universal-Rules changed.**
