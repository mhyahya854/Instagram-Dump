# 144 — Five Design-Aware AI Coding Resources: TasteSkill, Web Design Guidelines, AwesomeDesign, ImageToCode and Playwright CLI

**Source:** screenshot #6 (2026-10-26), an English text block containing exactly the five labels below. No GitHub URLs are given in the image; author/product identity of two labels remains **ambiguous**.

## Full source transcription

> TasteSkill helps Claude apply better design taste using premium references. Web Design Guidelines audits your UI against modern design principles and catches weak areas before you ship. AwesomeDesign gives Claude a complete design system covering colors, typography, spacing, buttons, and more.
>
> Then there's ImageToCode, which turns design references into usable code while preserving the important details, and Playwright CLI, which lets Claude open your website, take screenshots, and catch broken UI automatically.

## Researched mapping

### TasteSkill

**Probable canonical:** https://github.com/Leonxlnx/taste-skill · https://www.tasteskill.dev/docs . A skills set providing constraints/guidance for non-generic frontends. The repository says v2 is **experimental**, versioning and rule texts may change. No evidence its recommendations consistently beat real designer evaluation without testing. Avoid unquestioned copying of third-party reference sites.

### Web Design Guidelines

**Probable canonical:** https://github.com/vercel-labs/web-interface-guidelines . Design/UX code review guidelines for practical web interfaces and accessibility. This repo was also catalogued in prior research; don't treat it as a mandatory full design system or a substitute for user testing.

### AwesomeDesign

**Original source name:** `AwesomeDesign`. **Exact official repository unresolved** from screenshot alone. Could be a project, toolkit, asset gallery or shorthand. Do not misattribute it to a random “awesome-design” GitHub repository. Source sentence says it supplies design tokens for color/typography/spacing/buttons but this is only a creator's description. Retain as research candidate, not verified install.

### ImageToCode

**Original source name:** `ImageToCode`. **Exact official repository unresolved**. This describes an image/screenshot-to-code workflow which may use multiple implementations. Correct approach requires image rights, reference dimensions, asset licensing, semantic HTML, keyboard control, responsive breakpoints and pixel/screenshot comparison. Even a visual match can hide broken behavior.

### Playwright CLI

**Verified repo:** https://github.com/microsoft/playwright-cli · browser test framework https://github.com/microsoft/playwright .

Can drive a browser, capture screenshots and test interactions. For reliable regression tests prefer deterministic assertions, UI fixtures and CI. Browser startup/profile handling must not expose private cookies or unsafe remote debugging endpoints. CLI does **not** inherently guarantee detection of “ugly” UI without reference design/tolerances or structured inspection. Separate from [Playwright MCP](https://github.com/microsoft/playwright-mcp).

## A practical workflow

1. Requirements, users, original design direction and content first.
2. Define project tokens: type scale, color roles, spacing, icons, responsive grids and motion timing.
3. Inspect reference sites and licensed assets; extract transferable mechanics, never blindly clone logos/source code.
4. Implement semantic components with real product flows.
5. Review against Web Interface Guidelines + WCAG/keyboard/motion constraints.
6. Use Playwright to check actual pages/interactions/screenshots in chosen reference viewports and reduced motion.
7. Fix objective differences and regressions, then test with real users. Mark unresolved decisions and claims honestly.

**No skills installed, screenshot cloned, browser opened or user app changed.** Related [01 — UX](01-DESIGN-UX.md), [112 — Skills](112-THREEJS-GSAP-DESIGN-DNA-LOTTIE-GENJUTSU-AGENT-SKILLS.md), [118 — Agentation](118-FIVE-HUNDRED-AI-AGENTS-AND-AGENTATION-UI-FEEDBACK.md).
