# 147 — Twenty-Two Design Styles in the Instagram Reel: Exact Source Order

**Source:** seventeenth-batch screenshot #10, a comment by `talhaxcodes` headed **“Full list of styles shown:”**. The source is a list of **22 named aesthetics**, not screenshots of examples and not a license or a set of compulsory universal UI patterns. The names below are transcribed in original order.

## Original text — 22 complete items

1. Claymorphism
2. Cybercore
3. Neo-Brutalism
4. Scrapbook
5. Surrealism
6. Y2K Aesthetic
7. Pixel Art
8. Synthwave
9. Glassmorphism
10. Neumorphism
11. Bento Grid
12. Editorial Design
13. Swiss Design
14. Minimalism
15. Maximalism
16. Luxury Typography
17. Conceptual Sketch
18. Ethereal
19. Bohemian
20. Victorian
21. Cyberpunk
22. Wabi-Sabi

## Brief application distinctions (independent interpretation)

| Aesthetic/family | Possible visual mechanic | Engineering / usability warning |
|---|---|---|
| Claymorphism / Neumorphism / Glassmorphism | Soft raised layers, subtle depth, translucent materials | Often poor contrast and hidden control boundaries; avoid decorative overlays blocking content |
| Cybercore / Cyberpunk / Synthwave / Y2K | Tech cues, luminous accents, expressive type, saturated retro graphics | Avoid overused neon slop, seizure/flash concerns and low-contrast body text |
| Neo-Brutalism / Maximalism | High contrast, hard dividers, deliberate density | Visual volume ≠ legibility; maintain hierarchy, spacing and consistency |
| Scrapbook / Conceptual Sketch | Collage, imperfect strokes, personal imagery | Accessibility and reading order; maintain actual semantics beyond texture |
| Surrealism / Ethereal | Dreamlike imagery and unusual composition | Do not obscure interactions or force users to interpret metaphors |
| Pixel Art | Grid-bound coarse raster and bitmap shapes | Scale crisp pixels appropriately; controls still require normal touch regions |
| Bento Grid | Modular grid composition | Don't turn every app page into too many identical cards; responsive reading order |
| Editorial / Swiss Design / Luxury Typography | Rigorous hierarchy, whitespace, typography and grid | Licensing and responsive text contrast, don't copy another brand's identity |
| Minimalism / Wabi-Sabi | Reduction and intentional imperfection | Empty is not automatically useful; preserve affordances, status and content |
| Bohemian / Victorian | Ornamental historical/craft patterns | Watch overloaded borders/serif display text and weak readability |

## How to apply without generic “AI style swapping”

First define product goal/users/context and identify the *underlying mechanism* (hierarchy, contrast, symbolism, typography, texture, composition). Then select a coherent style and make reusable tokens for type/color/spacing/corner/motion; derive components for real user flows. Test mobile, keyboard, screen readers and reduced motion. Don't merge all styles into one design by default. A style may be appropriate for marketing editorial but poor for a dense data-entry screen.

**Cross-reference:** [04 — Existing Design Style Library](04-DESIGN-STYLE-LIBRARY.md) already catalogs additional styles; this file preserves a new independent 22-item Instagram source. [01 — UX Laws](01-DESIGN-UX.md), [77 — Whitespace](77-PORTFOLIO-STYLE-SCREENSHOTS-AND-WHITESPACE-RULES.md).

**Status:** all 22 names extracted; no visuals copied or CSS/theme built.
