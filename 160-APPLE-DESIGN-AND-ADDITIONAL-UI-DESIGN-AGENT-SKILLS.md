# 160 — Apple Design Skill and More Verified Design-Engineering Skills

**Source:** explicitly typed user request on 2026-10-26: **“APPLE DESIGN SKILL FROM GITHUB AND LOOK FOT MORE DESIGN SKILLS”**. This is a new research directive, not text in the accompanying ten screenshots. Source names and research identities are kept distinct.

## Emil Kowalski's Apple Design — exact canonical skill

- **Verified parent repo:** https://github.com/emilkowalski/skills
- **Direct skill file:** https://github.com/emilkowalski/skills/blob/main/skills/apple-design/SKILL.md
- **Skill ID:** `apple-design`. We read its actual `SKILL.md`, not just a social excerpt. Description: **Apple's approach to interface design and fluid, physical motion, translated for the web**.
- Main topics: gesture-driven UI, spring animations, drag/swipe sheets, momentum, **interruptible** transitions, translucent materials and depth, typography metrics, reduced motion, feedback, spatial consistency and restraint.
- **Not Apple Inc.'s official SDK or endorsement.** It distills WWDC ideas into web conventions; native iOS/macOS details still require Apple’s current official HIG and API docs. A repo license does not grant permission to redistribute proprietary SF font files or brand assets.
- Parent repository also exposes `emil-design-eng`, `animate`, `animate-expo`, `review-animations`, `improve-animations`, `find-animation-opportunities` and `animation-performance` (verify current file list/pinned version on adoption). Skill scripts and their configuration should be inspected before running.

**Reference-only example command (NOT executed):**
```bash
npx skills add emilkowalski/skills --skill apple-design
```
Use project-local scope, inspect the exact revision and skill scripts first.

## Additional Apple HIG-focused independent repos

| Source | Why useful | Caveat |
|---|---|---|
| [tzzs/apple-design-skill](https://github.com/tzzs/apple-design-skill) | Curated HIG references for iOS, iPadOS, macOS, watchOS, visionOS, accessibility, controls, gestures, layout and safe areas | Community-maintained; paraphrase may lag official HIG |
| [ykswang/apple-hig-skill](https://github.com/ykswang/apple-hig-skill) | HIG reference pack and scripts to refresh from primary pages | Verify copying terms/source attribution, platform freshness and content rights |
| [SudewaJay/apple-design-skill](https://github.com/SudewaJay/apple-design-skill) | Liquid Glass, typography, native-like interactions, CSS/React/Figma examples | Visual resemblance is not actual HIG compliance; may overapply glass |
| [naplesblue/apple-design-skill](https://github.com/naplesblue/apple-design-skill) | Token-level layout, components and review checklist | Independent derivative; some motion content credits Emil; verify attribution |

## Broader design skills: verified catalog leads

| Skill/repo | Function | Integration precautions |
|---|---|---|
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | Accessibility, typography, forms, navigation, responsive behavior, focus/motion/performance | Code review requires actual files, not just a screenshot |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Official skill `web-design-guidelines`, React performance and composition patterns | Read source revision; skill fetches remote guidelines at run time unless content cached |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Visual taste and avoiding generic AI patterns | Re-check permission and examples; aesthetic assertions are contextual |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI design patterns, styles and project suggestions | Catalog heuristics not tests; accessibility still necessary |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Design critique/polish and anti-slop improvements | No automatic pixel matching |
| [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | Intentional state transitions, timing, easing, Lottie/GSAP/CSS | Ensure reduced motion and component state correctness |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Editorial diagrams in HTML/SVG with brand design | Validate diagram links, accessibility and data |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | GSAP best-practice agent instructions | Library/plugin runtime still separate |
| [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills) | Scene/3D architecture, cameras, materials, interactions | Memory/GPU resource lifecycle |
| [zanwei/design-dna](https://github.com/zanwei/design-dna) | Extract design direction/tokens from reference | Recreate own design; do not copy protected assets |
| [AThevon/genjutsu](https://github.com/AThevon/genjutsu) | Web design concepts and interaction polish | Review repo and license before agent access |

### Apply to a real product

Goal → use/reference appropriate original product → specify typography, spacing, colors, asset rights and breakpoints → build functional flows → annotate flawed UI → run keyboard/mobile/E2E tests → audit performance, reduced-motion and real error states. Design skills enhance judgment but cannot replace genuine user research or QA.

**Status:** research and source references only. No skills installed, copied, executed or used to alter a website. Crosslinks [112](112-THREEJS-GSAP-DESIGN-DNA-LOTTIE-GENJUTSU-AGENT-SKILLS.md), [144](144-TASTE-AWESOMEDESIGN-IMAGETOCODE-WEB-GUIDELINES-PLAYWRIGHT.md).
