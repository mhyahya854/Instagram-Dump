# 175 — Huashu Motion, Frontend Slides, Diagram Design and Understand Anything

**Original typed names, 2026-10-27:** \`huashu-motion\`, \`Slide 4\`, \`Understand Anything\`, \`Frontend Slides\`, \`Diagram Design\`. Some names have confirmed GitHub roots, and one—**“Slide 4”**—does not. **GitHub repository metadata** was read directly for the four confirmed paths; no skills were installed and no videos, slide decks, diagrams or knowledge graphs were rendered.

## 1. Huashu Motion — creative director workflow as editable code

**Official upstream:** https://github.com/alchaincyf/huashu-motion ; **English instructions:** https://github.com/alchaincyf/huashu-motion/blob/main/README.en.md . GitHub reports repository-level **MIT** licensing. It is an **AI coding-agent skill + command-line tooling and templates** for creating *editable programmatic motion graphics*, promotional videos, short launch films and explainers, not a generative human-video model.

**Workflow:** choose a motion language/template and collect brand/product assets (\`om grab\`); scaffold project (\`om new\`, \`om templates\`); edit scenes in live studio (\`om studio\`); make frame-targeted change requests (\`om inbox\`, \`om look\`, \`om done\`); synchronize voice/sound; QA still frames; render, package or export HTML. Its README advertises around 20 motion languages, 12 starter templates, sound/effect resources and editable preview UI. These counts are source snapshot claims, not independently audited file counts.

**Dependencies:** Node 22+, Chrome/Chromium/Edge and FFmpeg for normal rendering/export. Optional voices/music may download samples or speech models and require additional dependencies. Cross-platform use is plausibly available wherever those dependencies work, but actual Windows/Linux/macOS coverage was **not independently tested** here.

**Quality risks:** source says the agent cannot actually *hear* output; it can inspect scores/waveforms/spectrograms, but musical taste and the final listening check need a person. It does not create authentic live actors; you supply real footage if needed. Inspect license of bundled fonts, music, samples, images and contributed templates, and avoid copying copyrighted reference films pixel-for-pixel.

**Evaluation protocol:** storyboard + brand fidelity checklist; compare 10 reference frames, timing and typography against output; reduced motion and subtitle legibility, audio peak/clipping, 1080p/export framerate, codec compatibility, font embedded rights, render reproducibility, media provenance and privacy.

## 2. Frontend Slides — interactive HTML decks driven by frontend coding skills

**Canonical GitHub:** https://github.com/zarazhangrui/frontend-slides ; repo-level MIT. A standalone agent skill for building browser-rendered slide decks using HTML, CSS and JavaScript/animation, often easier for coding agents to customize than low-level PPTX shapes.

**What it can do:** translate a story/outline into visually structured web slides, use layouts/typography/transitions responsive to screen size, iterate with browser screenshots and host/publish a static deck when intentionally authorized. Some workflows convert or refer to PowerPoint content, but **do not assume output is editable native PPTX or pixel-perfect in all browsers**; verify actual supported export.

**Files:** upstream contains \`SKILL.md\`, style presets, animation patterns, HTML templates and script assets. Review any browser automation, installed JS packages, autoplay, external font/image requests, and accessibility. Protect speaker notes and confidential research; an exported public web deck may reveal all HTML source.

**Acceptance criteria:** design hierarchy, one argument per visual, readable distance/zoom, keyboard navigation, reduced-motion fallback, correct slide order/page numbers, offline export where required, actual source-backed claims and link validation.

## 3. Diagram Design — accessible schematic storytelling

**Canonical GitHub:** https://github.com/cathrynlavery/diagram-design ; repo-level MIT. Promotes editorial technical diagrams with **self-contained HTML+SVG**, focusing on readable structure rather than decorative AI flowchart cliché. Repository describes roughly 45 diagram types (publisher assertion). Useful for architecture diagrams, control/data-flow, sequence concepts, security boundaries, model pipelines, research explanation and publication-quality illustrations.

**Architecture:** code-driven SVG vector shapes/typography inside HTML; create nodes, layout constraints, arrows, annotations, groupings, and labeled edges; export or render in a controlled browser. Avoid interpreting a pretty infographic as a tested architecture—check semantics, direction of flow, technology names, redaction and fidelity to actual code.

**QA:** inspect at screen and print scales, color-blind palettes, proper text labels/alt descriptions, line crossings/edge meanings, device pixel ratio, overflow and accessibility. Use validated graph generation tools when graph topology matters and this skill for editorial direction.

## 4. Understand Anything — explorable codebase knowledge graph

**Canonical GitHub:** https://github.com/Egonex-AI/Understand-Anything ; repo-level MIT. Codebase comprehension tool that produces an **interactive graph of code entities and relationships** with navigation/search/question-driven exploration, compatible with several coding agents per its README. Valuable for onboarding, reverse engineering, finding dependencies, architecture audit and narrowing context before complex edits.

**Conceptual pipeline:** authorized repo snapshot → language-aware symbol/file/entity extraction → relationship graph (imports, calls, ownership depending on parser) → interactive browser exploration and optional AI query layer. Verify the actual extractor/parser support and external inference before assuming purely local/accurate output. A graph is **a hypothesis/index**, not proof of complete call graph or dataflow correctness: dynamic dispatch, generated code, reflection and runtime behavior can be missed.

**Security:** isolate private repo source, redact keys, review network requests and model API destinations, control persistence/deletion of cached graph and don't expose an indexed private graph publicly. Benchmark against source navigation, code search and [CodeGraph](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md)/Serena alternatives on deterministic search tasks.

## 5. “Slide 4” — original label unresolved

The exact source **\`Slide 4\`** is NOT enough to identify one official app, repository, framework, fourth slide screenshot or numbered skill. GitHub searches for \`slide4\` returned several unrelated low-confidence matches; web queries for \`Slide 4\` returned diverse slide content, none established as the user's intended project. **No canonical URL assigned.** Do not quietly replace it with \`frontend-slides\`, \`slide-skill\`, \`Slidev\` or a fourth item from another list. An example unrelated project https://github.com/hunkim/slide-skill is a *different* slide-design skill, not proof of identity.

**Needed evidence:** screenshot, exact capitalization/logo, social creator, GitHub owner, browser/app link or repo description. Filed as an independent unresolved source entry until then.

## Practical selection matrix

| Task | Research lead | What to test |
|---|---|---|
| Motion-rich product launch explainer | Huashu Motion | Scene timing, image/video export and audio consistency |
| Browser-based presentation | Frontend Slides | Responsiveness, a11y, source attribution and offline usability |
| Architecture/process diagrams | Diagram Design | Edge meaning, semantic topology, typography and SVG accessibility |
| Understand unfamiliar source code | Understand Anything | Graph correctness, source provenance and privacy |
| “Slide 4” | Unresolved | Exact identity before adoption |

**Related:** [106 — Remotion media](106-LEMO-OPUSCAR-REMOTION-CODE-FILM-MOTION.md), [112 — Three.js & GSAP](112-THREEJS-GSAP-DESIGN-DNA-LOTTIE-GENJUTSU-AGENT-SKILLS.md), [117 — PixiJS](117-PIXIJS-ASCII-LILY-FLOWERS-AND-BRILLIANT-DISCOVERY.md), [157 — diagram research](157-SEVEN-AGENT-CAPABILITY-REPOS-SCIENTIFIC-SKILLS-DIAGRAMS.md), [160 — design skills](160-APPLE-DESIGN-AND-ADDITIONAL-UI-DESIGN-AGENT-SKILLS.md).


## Reconfirmed direct typed lead, 2026-10-27: “Undetstand anything”

Source was typed with the exact spelling **\`Undetstand anything\`**, now mapped through [184](184-OCT27-TWO-QUESTIONS-STOP-SLOP-UNDERSTAND-AGENT-BROWSER-REGISTER.md) to the already archived **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** rather than creating a duplicate article. Live GitHub README confirms a **Tree-sitter + LLM hybrid**: deterministic structure extraction for imports, functions, classes and call sites, plus semantic explanations and business-domain maps synthesized by models. Its multi-agent process includes \`project-scanner\`, \`file-analyzer\`, \`architecture-analyzer\`, \`tour-builder\`, \`graph-reviewer\`, and specialized domain/article analyzers. Original commands include \`/understand\`, \`/understand-domain\`, \`/understand-knowledge\`; a generated graph is kept in \`.ua/knowledge-graph.json\` (older projects retain \`.understand-anything/\`). The initial analysis of large repos can consume substantial model tokens; subsequent refresh is incremental by default. Sharing generated graphs can expose **private code relationships and business logic**, so require repository permission/secret review before committing such derived artifacts. Counts and features are upstream statements, not independent runtime tests.
