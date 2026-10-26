# 162 — Vercel Labs vgpu + Web Interface Guidelines (Two Distinct Tools)

**Source:** user-typed **“vervel vgpu and web design guidelines”** on 2026-10-26. **Source typo “vervel” is preserved**; independently identified concrete official repository **`vercel-labs/vgpu`**, which is **not a hosted virtual GPU or a cloud AI inference credit program**. Web design guidelines are separate.

## A. Official Vercel Labs vgpu

- **Verified repo:** https://github.com/vercel-labs/vgpu
- **Docs/examples:** https://vgpu.sh/
- **Project description:** modular cross-runtime **WebGPU** TypeScript library for shaders, 3D scenes, GPU tensors, neural networks and mathematical visualization, not a free cloud GPU service.
- Type-safe WGSL imports, explicit GPU context and pass sequence, browser canvas and headless Node/Dawn, mock adapter for deterministic CI, sample/CLI library, shader validation, interactive effects and agent-facing skill/docs.
- README identifies **MIT** license at time of review; maintainers can update APIs, so use a pinned revision and check package docs.

**Reference-only example (NOT executed):**
```bash
pnpm add vgpu
pnpm add -D @webgpu/types
# Optional agent skill: npx skills add vercel-labs/vgpu
# Inspect repo, versions, scripts and license first.
```

### Best applications

WebGPU fluid simulations, procedural animated backgrounds, particle effects, dither/ASCII shaders, math explainers, performant image-processing demos and 3D scenes. It is not a replacement for CSS accessibility, GPU-neutral fallbacks or an actual rendering budget. Compare [151 — GSAP/Vanta](151-LENIS-GSAP-VANTA-REACT-BITS-ANIMATION-SOURCE-REPOS.md), [112 — Three.js](112-THREEJS-GSAP-DESIGN-DNA-LOTTIE-GENJUTSU-AGENT-SKILLS.md), [117 — Pixi ASCII](117-PIXIJS-ASCII-LILY-FLOWERS-AND-BRILLIANT-DISCOVERY.md) and [136 — Grainrad](136-GRAINRAD-ASCII-DITHER-HALFTONE-GENERATIVE-EFFECTS.md).

**Technical gate:** WebGPU availability and permissions vary by browser/OS/device. Test with a fallback, low-power mode, resize/device-pixel ratio budgets, hidden tab disposal, context/device-loss, mobile FPS and `prefers-reduced-motion`. Never demand heavy GPU visuals merely for “premium” design.

## B. Vercel Web Interface Guidelines

- **Verified primary guidelines:** https://github.com/vercel-labs/web-interface-guidelines
- **Official agent skill:** https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines
- **Skill ID:** `web-design-guidelines`, distinct from rendering library vgpu.
- Reviews semantic HTML, keyboard and visible focus, ARIA, form error help, input/autocomplete, loading states, image sizing/alt, typography, motion/reduced motion, responsive layouts, hit targets, dark mode, URLs and state, and performance.
- Agent skill fetches a current external guidelines file before review; offline-use case needs a **versioned allowed copy with provenance**, not an assertion that live fetching works without internet.
- Output should include real **file:line** findings, severity and reproducible tests; a generic quality score without code access cannot verify the result.

**Reference-only skill invocation (NOT executed):**
```bash
npx skills add vercel-labs/agent-skills --skill web-design-guidelines
```

## Joint working pattern

Design/implement a GPU effect with vgpu → constrain it to a semantic, accessible layout → review Web Interface Guidelines → test both GPU and fallback → measure LCP, CLS, INP/FPS and battery responsiveness → decide whether motion genuinely improves comprehension.

**Naming caution:** “vervel vgpu” is likely a misspelling of **Vercel vgpu**, now resolved with official repo verification. No association with “Vercel GPU hosting” or paid GPU quota may be inferred.

**Status:** both repos verified; no package, WebGPU workload or agent skill installed, app modified or usage bill incurred.
