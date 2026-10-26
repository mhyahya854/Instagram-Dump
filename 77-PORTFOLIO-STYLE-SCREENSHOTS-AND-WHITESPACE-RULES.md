# 77 — Swiss Editorial, Floating Node, Brutalist Billboard, Bento Box, Architectural Split and Whitespace Rules

Captured 2026-10-26. Source comprises **six portfolio-style screenshots**, some showing repeated Swiss Editorial and Floating Node frames, plus the user's separately typed style **Architectural Split**. These are STYLE REFERENCES, never required UI defaults. The visible play triangle is a reel/player overlay, not established as part of the shown site.

## Screenshot labels and visual mechanisms

| Style | What screenshot actually supports | When and how to adapt | Pitfall |
|---|---|---|---|
| Swiss Editorial (shown twice) | High-contrast black “ROLE TITLE”, “SELECTED WORKS”, white grid and gray portfolio modules | Editorial hierarchy, alignment, type rhythm, readable content | Empty template, excessive all-caps title, clone of original visual identity |
| Floating Node (shown twice) | Oversized “FULL NAME”, small detached rounded chip/node shapes, below a dark personal/agency hero with “ANDRIY YURCHENKO” | Relational/network concepts when nodes have real semantic meaning | Floating decorative pills, overlays that crop or obstruct small viewports |
| Brutalist Billboard | White rectangle and huge cropped bold “FULL NAME”, sparse secondary copy | Strong brand statement when contrast, layout and readable labels support it | Giant typography overwhelms content, unusable at zoom/mobile |
| Bento Box | Unequal gray modular blocks with text/images/contact/resume | Show clearly differentiated content categories at a glance | Cards inside cards, uniform empty tiles and fake stats |
| Architectural Split (typed lead) | The label is typed by user, not shown as named screenshot in this batch | Two intentional panels: content and navigation, proof and explanation, diagram and detail | Forced 50/50 split, permanent empty panel, broken keyboard/mobile flow |

## What to do with empty spaces (core UI and UX research request)

**Decorative negative space** communicates hierarchy, grouping, clarity and pacing. It generally needs NO filler. **Functional empty state** appears when there is no data/item/task: explain what is absent, why it matters and the next valid action. **Accidental gap** happens from broken layout, poor vertical rhythm or missing content: diagnose rather than decorating.

### Eight decisions before filling a gap

1. Is the gap intentional to separate related groups? Keep it and preserve consistent alignment.
2. Does the screen lack an actual task/action or status? Add truthful needed content.
3. Is a list empty? Explain the empty state and show one relevant create/import action.
4. Is the top screen all hero with no real product? Bring value/primary task into view.
5. Is the gap caused by device width, viewport-height min rules or hidden UI? Fix responsive CSS.
6. Is the gap making scan order confusing? Improve headings, proximity, type sizes and readable width.
7. Is the area unused only on large monitors? An asymmetric breathing region can be intentional.
8. Are cards/animations/icons being invented solely to fill space? Leave it empty instead.

### Practical layout/testing rules

- Establish visual anchors and use proximity more than ornamental borders.
- Keep text line lengths reasonable; preserve room for focus and touch targets.
- Align related text fields, labels, errors and actions, but vary spacing between unrelated sections.
- Use real data and authentic photography; placeholders and fake demos do not count as content.
- Small-screen stack for split layouts; avoid hidden nav, oversized typography, sideways scroll.
- Use one dominant information priority and genuine secondary hierarchy, not identical card shadows/rounded corners across everything.
- Respect reduced motion, color contrast, text zoom and logical reading order.
- Verify empty/loading/error/success/disabled states, not just happy-path screenshot.

## Example use case

Portfolio: headline → brief promise → selected verified work → contact. The white space supports the reading sequence. Dashboard: overview/status → actionable projects or a useful no-projects empty state. No fake metrics or decorative widgets.

**Source integrity:** screenshot text is partial; exact original pages, fonts, links and interactions were not supplied. Never attribute fabricated details to the source.

Related: [01 — Design Rules](01-DESIGN-UX.md), [04 — Styles](04-DESIGN-STYLE-LIBRARY.md), [33 — UI/UX/CX](33-UI-UX-CX-SCOPE-AND-QUALITY-FRAMEWORK.md), [38 — Error Prevention](38-UX-ERROR-PREVENTION-AND-DECISION-SAFETY.md).
