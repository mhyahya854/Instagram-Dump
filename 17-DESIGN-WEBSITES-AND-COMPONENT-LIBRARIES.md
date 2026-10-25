# 17 — Design Websites, Galleries, Components and Motion Resources

Captured: 2026-10-25. Source: spoken Instagram-reel list. **These are reference resources, not automatic dependencies or default styling orders.**

## How to use the directory offline

A **gallery** helps observe real design decisions; a **component registry** supplies source or examples that must be reviewed and adapted to the app's stack; a **design-system document** encodes repeatable tokens and interaction rules; an **animation library** provides implementation machinery, not a reason to animate a screen. A **3D icon library** supplies assets whose license must be checked. Recording a site does not give permission to copy its commercial designs, trademarks or photos.

Statuses: **Verified** (official website located), **likely** (plausible voice-transcription correction but unconfirmed as the speaker's intended site), **unresolved** (no reliable exact website), **variant** (related concept with more than one product).

## Complete dictated website list, in original order

| # | As spoken | Resolved reference, URL and category | Identification | Use / guardrail |
|---:|---|---|---|---|
| 1 | Minimal Gallery | https://minimal.gallery/ — hand-curated real-site design gallery | Verified | Compare real websites, layouts and typography; screenshot inspiration is not a working component. |
| 2 | Kage | https://kage.design/ — searchable real website/component inspiration, offers AI-ready prompts | Verified | Explore real product screens and page sections; independently test any agent-generated recreation. |
| 3 | Upshot Gallery | **Unknown**; no reliable canonical domain found | Unresolved | Preserve name. Do not invent URL or substitute another gallery by guess. |
| 4 | Component Gallery | https://component.gallery/ — real design-system component examples | Verified | Learn canonical component names and compare patterns, without assuming popularity proves correctness. |
| 5 | Design.md | https://designmd.ai/ and https://github.com/google-labs-code/design.md — DESIGN.md format; alternatively https://designmd.cc/ analyzes existing sites | Verified **concept**, ambiguous specific website | Plain-text design system file containing colors, typography, spacing and component instructions. Distinguish specification, community site and independent extraction service. |
| 6 | Files | **Unknown** | Unresolved | “Files” alone does not identify a specific design gallery/site. |
| 7 | Referro Styles | https://styles.refero.design/ — **Refero Styles**, AI-readable site-derived DESIGN.md references | Verified (spelling corrected) | Capture colors, typography, component intent; do not copy brands/assets without rights. |
| 8 | Chio | **Unknown** | Unresolved | Keep the raw voice spelling; several unrelated uses exist. |
| 9 | Vipro | **Unknown** | Unresolved | No trustworthy UI-design site match for that exact term. |
| 10 | 21st Dev | https://21st.dev/ or https://www.21st.sh/ — component/prompt registry | Verified | React components and templates by varied creators; license, dependencies and accessibility vary per item. |
| 11 | Shaden UI | https://ui.shadcn.com/ — **shadcn/ui** | Likely correction | Copy-into-project components for custom styling; not a license to impose default shadcn look everywhere. |
| 12 | Astrinity UI | https://ui.aceternity.com/ — **Aceternity UI** | Strong phonetic match | React/Tailwind/Motion components and templates; abundant effects do not mandate decorative animation. |
| 13 | Magic UI | https://magicui.design/ — React components, patterns and effects | Verified | Many glow/gradient/animated elements; choose only if function and style warrant them. |
| 14 | Motion Primitives | https://motion-primitives.com/ — copy-paste Motion/Tailwind React microinteractions | Verified | Animation should clarify state, be performant and respect reduced-motion preferences. |
| 15 | Microkit UI | https://microkit.co/ — MicroKit UI microinteractions | Verified | Consider click feedback, deletion/undo and input states; review hover-only patterns for touch support. |
| 16 | Anime.js | https://animejs.com/ — JavaScript animation engine | Verified | Timelines, SVG motion and transforms; engineering library, not a design authority. |
| 17 | Map CN | https://www.mapcn.dev/ — mapcn React components built on MapLibre | Verified | Verify tile/provider licensing, OpenStreetMap attribution, API limits and mobile performance. |
| 18 | Uverse | **Possibly Uiverse** | Possible duplicate | Do not invent a second website until source confirms two different references. |
| 19 | UIverse | https://uiverse.io/ — Uiverse community-made UI components | Verified | Copy HTML/CSS, React and Figma examples; inspect code and provenance individually. |
| 20 | Liquid Class | **Likely “Liquid Glass”**, not a unique website: e.g. https://liqui.design/ or https://liquikit.dev/ | Unconfirmed correction | Fluid-refraction/glass examples are optional visual reference; the existing rulebook avoids blanket liquid glass. |
| 21 | Kitbits | **Possibly Kibo UI**: https://www.kibo-ui.com/ | **Unconfirmed** | Kibo is a real shadcn-compatible component registry, but no evidence this is the user's exact “Kitbits”. |
| 22 | 3D Icons | https://3dicons.co/ — 3dicons by Vijay Verma | Likely / verified site category | 3D asset library; site's V1 describes CC0. Verify chosen asset's license; don't replace authentic avatars with icons. |

## Working classification

**Website inspiration:** Minimal Gallery, Kage; unresolved Upshot Gallery, Files, Chio, Vipro.
**Design systems and references:** Component Gallery, DESIGN.md, Refero Styles.
**Copyable component libraries:** 21st, shadcn/ui, Aceternity, Magic UI, Uiverse, Kibo candidate, MicroKit UI, Motion Primitives.
**Animation engine:** Anime.js.
**Maps:** mapcn on MapLibre/OSM.
**Asset library:** 3dicons.
**Visual effect only / ambiguous:** “Liquid Class” → Liquid Glass candidate.

## DESIGN.md: why it matters

The design system must **encode decisions** rather than merely listing aesthetic references. A useful portable text specification describes: brand and audience; color tokens (semantic state as well as accents), typography/line heights, grid/spacing rules, responsiveness, component variants, interactive states, accessibility, and anti-patterns. A short illustration:

~~~md
# Project UI Design System
Audience: [actual intended users]
Primary task: [actual user outcome]
Colors: semantic roles, contrast pairs and allowed palettes
Typography: body, headings, captions, line-height, platform fallback fonts
Spacing: a chosen scale for real components
Components: buttons, inputs, tables, loading, errors, empty and success
Responsive: touch/keyboard/mobile breakpoints
Motion: feedback only, with reduced motion
Avoid by default: purple gradients, decorative card triples, meaningless badges
~~~

A file is **a reference for an agent**, not guaranteed enforcement; browser tests and design review still matter.

## Applying these sites while preserving earlier preferences

- No source authorizes compulsory purple gradients, glass, dot grids, animated arrows, three feature cards, Lucide on every screen or meaningless labels.
- Use licensed assets. Attribution/redistribution rights depend on the exact asset and library, not this list.
- Copying code requires inspecting dependencies, security, focus/keyboard behavior, reduced motion and breakpoints.
- Real sites can supply inspiration but do not give permission for brand impersonation.
- A gallery screenshot is not a user-tested product. Test live prototypes.

## Research gaps and verification status

**Do not assign a link yet:** Upshot Gallery, Files, Chio, Vipro. **Do not treat the tentative correction as fact:** Kitbits → Kibo, Liquid Class → Liquid Glass, Uverse as a second site.

Verified official reference pages: https://minimal.gallery/ ; https://kage.design/ ; https://component.gallery/about/ ; https://designmd.ai/about ; https://styles.refero.design/ ; https://21st.dev/ ; https://ui.aceternity.com/ ; https://microkit.co/ ; https://motion-primitives.com/ ; https://animejs.com/ ; https://www.mapcn.dev/ ; https://uiverse.io/ ; https://3dicons.co/ .

Related original design list: [01-DESIGN-UX.md](01-DESIGN-UX.md). Visual aesthetic vocabulary: [04-DESIGN-STYLE-LIBRARY.md](04-DESIGN-STYLE-LIBRARY.md).
