# 97 — For testing before you ship

**Source:** one user-uploaded Instagram carousel screenshot supplied 2026-10-26. **Screenshot subtitle:** “because ‘it works on my laptop’ isn't enough”. This page preserves **all 4 named items, in the exact source order, with the screenshot's descriptive text**. Links and technical limitations are independently researched and are **not part of the original image**. Resource entries are catalog references, not instructions to automatically install/copy designs.

| # | Exact screenshot label | Exact screenshot description | Identified destination | Research note / status |
|---:|---|---|---|---|
| 1 | **PageSpeed Insights** | Find website speed problems | [https://pagespeed.web.dev/](https://pagespeed.web.dev/) | Lab + field data when available; results vary by device/network and traffic. |
| 2 | **GTmetrix** | See what makes your pages slow | [https://gtmetrix.com/](https://gtmetrix.com/) | Waterfall/profiling of tested routes; region/network matters. |
| 3 | **WebPageTest** | Analyze loading performance | [https://www.webpagetest.org/](https://www.webpagetest.org/) | Detailed real-browser waterfalls, repeat runs across relevant devices/regions. |
| 4 | **Design Lint** | Catch inconsistent Figma styles | [https://lintyour.design/](https://lintyour.design/) | Figma design style plugin—not a runtime E2E or production-security test; code https://github.com/destefanis/design-lint . |

## Practical use and limits

Observe a **specific transferable mechanism** (hierarchy, information density, layout structure, animation purpose, component behavior, visual asset role, user flow or validation signal) rather than automatically copying full designs. Adapt to actual product requirements, test mobile/keyboard/focus/contrast/reduced-motion as relevant, and respect asset and software licenses. Aesthetic quality is not proof that an application works; use real data, authentic screenshots and functional tests. 

**Verification statement:** this document records original screenshot wording separately from externally researched URLs/caveats. Not every link was live-tested; unresolved destinations are labeled. No website cloned, dependency installed, proprietary asset downloaded, application tested, or Universal-Rules changed.

[Resource Index](98-DESIGN-RESOURCE-CAROUSEL-MASTER-INDEX.md) · [Original directory](17-DESIGN-WEBSITES-AND-COMPONENT-LIBRARIES.md) · [Design principles](01-DESIGN-UX.md)
