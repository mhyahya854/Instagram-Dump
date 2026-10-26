# 76 — 20 Things to Have Claude Check Before Website Launch

Captured 2026-10-26 from uploaded screenshot. The heading says “in under 28 seconds”, a promotional duration—not proof these tests can actually run in that time. Screenshot-derived names below; verification guidance is independently added. No live website tested.

| # | Exact screenshot check | Proper acceptance and caution |
|---:|---|---|
| 1 | Privacy policy page | Actual data/third parties and applicable user rights, not invented legal text |
| 2 | Terms & conditions page | Terms appropriate to the product/jurisdiction, real links |
| 3 | Secrets off the frontend | No server keys or secrets in JS, source maps, git history; rotate leaked credentials |
| 4 | Force HTTPS | Valid cert, correct redirects, no mixed content, secure cookies |
| 5 | Cookie consent banner | Only as applicable to actual tracking and law; meaningful reject/accept controls |
| 6 | Meta titles + descriptions | Specific truthful titles/metadata per relevant route |
| 7 | Social preview image | Public Open Graph image, correct URL, test link preview |
| 8 | Add a favicon | Correct linked icon asset, browsers and theme variants if useful |
| 9 | Sitemap + robots.txt | Public sitemap of canonical indexable pages; robots is not authentication |
| 10 | Alt text on images | Descriptive alt for meaningful content, empty alt for decoration |
| 11 | Compress your images | Resize, WebP/AVIF where suited, avoid hero-image lazy-load |
| 12 | Check page load speed | Record Lighthouse and Core Web Vitals: LCP, INP, CLS |
| 13 | Fix color contrast | WCAG-aware legible labels/controls/focus/disabled meanings |
| 14 | Make it mobile friendly | Real touch, Safari/Chrome, zoom, keyboards, portrait and landscape |
| 15 | Custom 404 page | Helpful missing-page content with actual HTTP 404 status |
| 16 | Fix broken links | Test navigation/footer/CTA/mailto/tel and protected routes appropriately |
| 17 | Form validation | Client feedback AND server validation, real successful delivery/state |
| 18 | Spam protection | Server rate limits, abuse prevention, accessibility and safe logging |
| 19 | Set up analytics | Actual event tracking and consent/privacy choices; not obligatory in every app |
| 20 | One clear call to action | Dominant honest next step in each decision context, not single button everywhere |

## Prioritize by harm

Security/privacy and payments, server correctness, contact/forms, backups and broken user flows are launch blockers when applicable. Then test mobile and accessibility, metadata and content, performance, and marketing refinements. Every check gets PASS, FAIL, NOT TESTED, BLOCKED or NOT APPLICABLE with reproducible results—not “Claude says good.”

The screenshot does not establish that any of these were actually performed on a specific app. No automatic analytics integrations, domain changes or legal approvals were executed.

Related: [37 — Website Prelaunch](37-WEBSITE-PRELAUNCH-RELEASE-CHECKLIST.md), [41 — Legal Risk](41-LEGAL-PRIVACY-COMPLIANCE-CLAIMS.md), [59 — Web Performance](59-WEB-PERFORMANCE-CORE-WEB-VITALS-AND-INFRASTRUCTURE.md).
Official: https://www.w3.org/WAI/WCAG22/quickref/ and https://web.dev/articles/vitals .
