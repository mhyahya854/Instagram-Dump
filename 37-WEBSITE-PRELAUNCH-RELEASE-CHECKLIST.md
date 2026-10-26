# 37 — Website Launch Tomorrow: Practical Preflight, Evidence and Safe Release

Captured 2026-10-25. Source: user-collected Instagram example addressed to “Claude.” **This is a reusable checklist, not evidence any particular website has been audited or launched.** No domain, account, payments or website supplied. Never claim an external site is secure or compliant without inspecting it.

## Release principles

- **Prepare a scope inventory first.** Which routes and subdomains should exist? Which forms, payments, contact methods and integrations should work?
- **Staging first** for functional changes, analytics, pricing and payment integration; back up current deploy and data.
- **Test the actual public build**, not only the editor/localhost preview. Save results, screenshots, error logs and known limitations.
- **Critical blockers:** broken payment flow, unprotected private records/admin routes, exposed secrets, failed contact delivery, wrong billing, lost user data, missing legally required disclosures.
- “Make no mistakes” is not a test. Separate **checked, passing, failing, untested and not applicable**.

## Original reel requests, organized for verification

| Task | Actions | Evidence / acceptance |
| --- | --- | --- |
| Mobile layout | Test common phone viewport widths, landscape, text enlargement, touch targets, sticky headers, menus, forms and keyboard | No unintended horizontal scroll, accessible interaction, no overlapping content |
| Every link | Crawl all known routes, buttons, nav/footer/internal/outbound links, email and social links | Every intended destination loads or reports expected state; no 404 for required pages |
| Contact form | Send approved test submission to a designated inbox, test required/invalid fields and spam protection | Actual message delivered, stored only if intended; client sees real success only after server confirmation |
| Speed | Measure real Lighthouse/Web Vitals in production-like browser and device conditions | Baseline and post-fix results for LCP, INP, CLS, page size; avoid claiming zero latency |
| Images | Right-size, compress, responsive srcset/sizes, avoid lazy loading primary LCP image; preserve quality and licensing | Reduced transferred bytes, stable layout and no broken aspect ratio |
| HTTPS “padlock” | Valid certificate, correct hostnames, redirect HTTP to HTTPS, secure cookies, fix mixed content, HSTS only after readiness | Browser connection secure; certificate/redirect checks pass. Modern browsers don't always show a literal padlock icon. |
| Chrome and Safari | Test real Chromium and WebKit/Safari, desktop/mobile as relevant, fonts, scroll, forms and media | Record devices/versions tested and browser-specific defects |
| Typos and content | Proofread titles, CTAs, error messages, checkout, policies, addresses, pricing and RTL if used | Reviewed copy matches real product; no placeholders or fake proof |
| WhatsApp button | Use approved https://wa.me/number format with international digits; percent-encode optional prefilled message | Opens intended business conversation in mobile app/browser, without exposing a private number unintentionally |
| Domain email | Configure intended mailbox (e.g. hello@domain), MX, SPF, DKIM, DMARC and inbound/outbound mail | Mail successfully sent and received from external account; authentication checks pass |
| Google Analytics | Set up appropriate GA4 property/data stream and event tracking; check user consent/jurisdiction | Realtime or DebugView test event visible; no unauthorized PII sent |
| Google indexing | Verify domain in Google Search Console; create sitemap; ensure robots/indexability and canonical URLs; submit sitemap | Sitemap accepted/processed; **submission does not guarantee indexing or rank** |
| WhatsApp link preview | Correct public canonical URL, Open Graph title/description/image, public reachable metadata, share cache refresh as available | New link pasted in WhatsApp shows intended title/image on tested platform |
| Backups | Database, uploaded user content, important settings, deployment/source, DNS/config recovery with retention | **Actual restore drill**, not just “backup enabled” badge |
| Payment page | Sandbox card and wallet flows, success/failure/cancel, currency/tax, webhooks with signed/idempotent handling, receipts and refunds | Tested real processor sandbox behavior; no charge without consent |
| Go-live observability | Errors, logs, health checks, incident rollback, uptime and cost monitoring | Working alert destination and known owner |
| Security/legal gates | Authorization, privacy/consent, email, subscriptions, copyright uploads where applicable | Evidence of reviewed requirements for applicable jurisdictions; see file 41 |

## Suggested priority order

**Before launch:** domain/HTTPS and DNS → auth and data access → working contact/payment → backup/restore plan → legal/consent review → mobile critical path → analytics/indexing and SEO → performance/copy polish. Fix blockers before launch. An honest delayed launch is preferable to a known dangerous payment or authorization bug.

### Practical example: booking/contact business

1. Open mobile homepage at real domain. Identify service within seconds. Tap a real contact CTA.
2. Fill a sample form with valid/invalid data, submit, confirm delivered message and no duplicate sends.
3. Tap WhatsApp and verify number and optional message, test on app and web fallback.
4. Confirm email reply-to, no personal secrets exposed, and no unconsented tracking.
5. Exercise all legal/price claims and support links.
6. Inspect browser console/network warnings and ensure required pages work without login.

## Why “domain email” has extra DNS requirements

**MX** routes inbound mail. **SPF** advertises allowed senders. **DKIM** signs authenticated mail. **DMARC** specifies alignment/reporting policy. Correct configuration varies by provider. Starting with enforcement without verifying legitimate senders can cause deliverability failures.

## Social preview details

WhatsApp/link aggregators generally look at publicly accessible Open Graph HTML. Use secure full URLs for image, reasonable image dimensions, correct content type, stable redirects and relevant meta tags such as og:title, og:description, og:image and og:url. A WhatsApp chat link is a separate object from the *preview of your website URL*.

## Guardrails

Do not submit a sitemap, turn on analytics, issue live refunds/charges or change DNS without the operator's access and approval. Do not log private form content, card numbers, WhatsApp messages or secret tokens to troubleshooting tools.

Sources:
- Google Search sitemap: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Web Vitals: https://web.dev/articles/vitals
- Lighthouse: https://developer.chrome.com/docs/lighthouse/overview
- Open Graph: https://ogp.me/
- WhatsApp click-to-chat: https://faq.whatsapp.com/5913398998672934
- Related: [02 Product Completeness](02-VIBE-CODED-APP-QUALITY.md), [20 Server Security](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md), [41 Legal Privacy](41-LEGAL-PRIVACY-COMPLIANCE-CLAIMS.md).

## Eleventh source batch: 20 things to check before website launch

[76 — Exact 20-Point Screenshot Checklist](76-TWENTY-WEBSITE-PRELAUNCH-CHECKS-SCREENSHOT.md) keeps the original list in order: privacy, terms, frontend secrets, HTTPS, consent, metadata, social previews, favicon, sitemap/robots, alt text, compression, speed, contrast, mobile, proper HTTP 404, links, form validation, spam control, analytics and CTA. A video mentioning “under 28 seconds” is not proof of testing; all acceptance criteria require real evidence.
