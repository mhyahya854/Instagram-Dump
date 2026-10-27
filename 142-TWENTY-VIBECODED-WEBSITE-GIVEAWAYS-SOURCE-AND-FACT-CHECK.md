# 142 — “20 (hidden) vibecoded website giveaways”: Complete Source and Technical Audit

**Source:** image #2 of the seventeenth Instagram screenshot batch, creator talking-head overlay, two-column list and three visible public comments. This is a **creator's set of clues**, **NOT proof of AI authorship** or a universal shipping checklist. Screenshot spelling and exact numbering preserved first.

## All 20 EXACT source labels

| # | Original wording | Technical assessment |
|---:|---|---|
| 1 | `vercel.app url` | Legitimate free preview and production hosting; custom domains help brands, but this is not evidence of AI |
| 2 | `view source empty` | Client-side rendered apps may ship a light HTML shell. SSR/prerendering can improve search/social usability but client rendering is legitimate |
| 3 | `no 404 page` | User-facing fallback UX recommended; **actual HTTP 404** for missing resources is more important than decorative custom page |
| 4 | `vite + react browser` | Vite and React are professional tools, not AI fingerprints |
| 5 | `same page titles` | Inappropriately identical title text on distinct public content pages harms navigation/search clarity |
| 6 | `no meta desc` | Missing description can be improved for search snippets, but search engines can create snippets automatically |
| 7 | `no og:image` | Poor link-share previews possible; optional for nonshared/private routes |
| 8 | `no structured data` | Use JSON-LD only when content qualifies; not mandatory for every site |
| 9 | `multiple H1's` | **Not inherently invalid HTML or a reliable clue of AI**; clear document heading hierarchy matters more |
| 10 | `no H1's` | May obscure primary document heading. Fix semantic hierarchy where content supports it |
| 11 | `no canonical tag` | Canonical hints recommended for duplicated/variant URLs; absence doesn't itself prove indexing failure |
| 12 | `no llms.txt` | Optional, emerging proposal; **not an SEO standard or AI-built detection criterion** |
| 13 | `AI blocked robots.txt` | Site owners may intentionally block AI crawlers; robots.txt directives are publisher decisions, not evidence of AI origin |
| 14 | `no favicon` | Small branding/UX gap, not proof of code origin |
| 15 | `no sitemap.xml` | XML sitemaps help with discoverability, particularly larger sites; optional for tiny navigable sites |
| 16 | `no lang attribution` | Missing `<html lang="...">` is a real accessibility/assistive technology concern |
| 17 | `missing alt text` | Content-bearing images need useful descriptions; decorative images correctly use `alt=""` |
| 18 | `source maps` | Public debug source maps can reveal internals; not always insecure, and sometimes intentionally available. Check for secrets/ownership; don't judge origin |
| 19 | `console errors` | Reproducible uncaught runtime errors or failed resources indicate real defects; benign warnings need context |
| 20 | `massive JS bundles` | Can harm real-world performance; budget on device/network, split code, remove unused scripts |

## Three visible comments — distinct from the list

- `omarcopisco`: **“multiple H1s or no H1s? Is another giveaway that it's made in HTML?”**
- `stuff.prv`: **“I literally do some of these without vibecoding”**
- `petrovic_ko`: **“Not facing this issue with manus”**

These reflect public reactions, **not test results**. The source is teasing/critical; do not silently turn it into binding engineering rules.

## Meaningful launch QA

Check accessible semantics (landmarks, headings, language, image alt), SEO intent (public route indexing, truthful metadata/canonicals/sitemap if applicable), real errors (404 status, JS exceptions, broken links), social previews, responsive performance (LCP/INP/CLS on mobile), permissions and server behavior. Keep sensitive/auth routes private even if a crawler misses them. Do not advise unblocking AI bots or adding arbitrary FAQ/schema merely to pass a reel checklist.

## Related research and sources

[116 — SEO “Rank #1 Friday” Claims](116-SEO-REEL-RANK-BY-FRIDAY-CLAIMS-AND-REAL-QA.md), [76 — Prelaunch](76-TWENTY-WEBSITE-PRELAUNCH-CHECKS-SCREENSHOT.md), [37 — Website QA](37-WEBSITE-PRELAUNCH-RELEASE-CHECKLIST.md). External authoritative references: https://developers.google.com/search/docs/fundamentals/seo-starter-guide ; https://html.spec.whatwg.org/multipage/sections.html ; https://www.w3.org/WAI/tutorials/images/ .

**Status:** all 20 source items + three comments transcribed; no user site checked, deployed or altered.


## Complementary legitimate SEO tool

A user-typed lead produced [180 — Claude SEO](180-CLAUDE-SEO-GITHUB-SKILL-TECHNICAL-AUDIT-AND-EXACT-INVENTORY.md): its checks can help discover meaningful SEO release defects, but optional \`llms.txt\`/AI-agent visibility heuristics do not establish a search-engine obligation or prove a site was “vibe-coded.” Original twenty source labels above remain unchanged.
