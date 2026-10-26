# 59 — Website Performance: Real Measurements, Core Web Vitals and Full-Stack Competence

Captured 2026-10-26. Two reels: one offers a performance-fix prompt; a Hindi/English clip reminds vibe coders that a website is more than one UI-generating prompt.

## Reel A — “my website takes forever”

The creator asks an agent to compress/convert images, lazy-load below-fold content, remove unused code, reduce JS, optimize fonts, cache static assets, stop unnecessary scripts, reduce layout shifts, fix Largest Contentful Paint and interaction delay, test slow mobile and compare Lighthouse before/after.

These are **diagnostic hypotheses**, not modifications required on every website. Some can conflict: aggressive lazy-loading of a hero image may *worsen* LCP; blindly deleting code can break flows; overly long caching can cause stale deployments.

### Measure before modifying

- Fix the exact target route, deployed build, commit SHA, device/viewport, network/CPU throttling and browser.
- Capture lab Lighthouse runs and production field evidence, where available, across typical user groups. Lab results can vary; don't compare runs under completely different conditions.
- Core Web Vitals:
  - **LCP**: Largest Contentful Paint — main content load, good ≤ 2.5s at 75th percentile.
  - **INP**: Interaction to Next Paint — responsiveness, good ≤ 200ms at 75th percentile.
  - **CLS**: Cumulative Layout Shift — layout stability, good ≤ 0.1 at 75th percentile.
- Audit transfer size, JavaScript execution, blocking scripts, third-party widgets, image formats and caching headers. Record accessibility and feature correctness alongside speed.

Official reference: https://web.dev/articles/vitals and https://developer.chrome.com/docs/lighthouse/overview .

## Practical performance improvements and possible trade-offs

| Issue | Candidate change | Verification / caution |
| --- | --- | --- |
| Slow hero image | resize, responsive srcset/sizes, AVIF/WebP, prioritization/preload where relevant | Do not lazy-load the actual LCP image; verify visible quality |
| Too many large images | responsive images, compress and lazy-load genuinely off-screen | Reserve width/height to avoid layout shifts |
| Web fonts | reduce font variants, subset, self-host where warranted, font-display and sensible fallback | Check licensing, CLS/font swap and privacy law; not every font requires preload |
| Long main-thread JS | tree-shaking, code splitting, profiling, remove unused packages | Watch hydration mismatch and missing behavior |
| Unneeded analytics/widgets | disable or delay nonessential third-party scripts with proper consent | Don't break essential form, checkout or legal preference behavior |
| Slow backend APIs | DB plan/index analysis, caching with correct invalidation, avoid N+1 | Never cache tenant-private data across users |
| Weak static caching | hashed asset filenames, immutable cache-control, CDN | Serve HTML/config differently; verify deploy freshness |
| Shifting UI | fixed image dimensions, reserve slots, avoid intrusive late banners | Test real loading and error states |
| Sluggish interaction | inspect event handlers, main-thread blocking, render churn | Measure INP rather than optimizing only initial paint |
| Bad mobile | real phone tests at realistic CPU/network speed, zoom, input focus | Device emulation alone is insufficient |

### Example acceptance report (without inventing measurements)

| Route | Before LCP/INP/CLS | After LCP/INP/CLS | Functionality evidence |
| --- | --- | --- | --- |
| Home | Not measured | Not measured | Not tested |
| Contact | Not measured | Not measured | Not tested |
| Checkout | Not measured | Not measured | Payment sandbox not tested |

Do not fill these with plausible-looking scores. Attach real Lighthouse JSON/traces/screenshots and CI outputs. **“Make no mistakes” is not a runnable verification command.**

## Reel B (Hindi/English): beyond one-prompt website generation

Normalized translation:
> “Okay, a single prompt can make me a website—but what about coding, CDN, authentication, permissions, testing, architecture, rate limiting, cloud hosting, error tracking, logging, frontend, staging, databases, security, CI/CD, version control, monitoring, notifications, APIs, backend logic and system design?”

That is a sound reminder that *front-end appearance isn't production readiness*. However, a personal portfolio or journal app may not need a CDN, microservices, enterprise monitoring and complex distributed storage. Requirements should be proportional to users, safety, reliability, cost and deployment context.

### System-design checklist

1. Users/tasks/data sensitivity/privacy.
2. Frontend/UI/accessibility and real task correctness.
3. Server/domain layer: validation, role matrix, business invariants, payments (if needed).
4. API contracts and errors: typed inputs, versioning, rate limits and idempotency.
5. Storage/DB: schema/indexes, migrations, backups, restore tests, tenancy.
6. Authentication, sessions/refresh lifecycle and current-state authorization.
7. Hosting/edge/CDN: network exposure, TLS, DNS, cost, caching.
8. Continuous integration/deployment, staging, regression tests and rollbacks.
9. Observability: logs without secrets, metrics, alerts and incident ownership.
10. Release: actual mobile/performance, legal disclosure where applicable, accessibility, data recovery.

These are **decision dimensions**, not necessarily ten new services.

## Cross-references

- [03 — Production Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md)
- [21 — Systems Glossary](21-ARCHITECTURE-SYSTEMS-NETWORKS-GLOSSARY.md)
- [37 — Website Prelaunch](37-WEBSITE-PRELAUNCH-RELEASE-CHECKLIST.md)
- [50 — Engineering Guides](50-PROGRAMMING-SYSTEM-DESIGN-GUIDES-FREE-LLM-APIS.md)
- [57 — Reticle/Adversarial Testing](57-RETICLE-ADVERSARIAL-REVIEWS-SECURITY-GATES.md)
