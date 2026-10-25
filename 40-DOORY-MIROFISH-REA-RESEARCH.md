# 40 — Doory, MiroFish and REA: Verified Repositories vs Viral Claims

Captured 2026-10-25. All three GitHub repos were confirmed as publicly available. **Research only: no downloads, execution, sign-in or permissions granted.**

## A. “Dory,” the free browser-based Canva alternative

**Verified likely match: Doory** — https://github.com/shaongitbd/doory . Original speaker said “Dory”; README spells it **Doory**.

**Capabilities from its primary README:** browser design editor for posters, cards, social images, stories, slides, resumes and thumbnails; blank canvases and starter templates; text/shapes/layers, grouping/reordering; enter/exit/emphasis animations and page transitions; output PNG, JPG, SVG, PDF, **MP4 and GIF**. Guest design work can start without an account. Self-hosting is possible with or without Docker.

**Limitations:** early-stage project, about ten starter templates in the contemporary README, not a fully equivalent replacement for Canva's vast templates, managed hosting, collaboration, licensed stock content and integrated AI tools. Browser video rendering can consume memory/CPU and behave differently across browsers. Verify any claimed export type with a real sample.

**License caution:** a project's “open source Canva alternative” label isn't a license grant. Inspect the actual current LICENSE and attribution obligations; assets/fonts/dependencies can have independent rights. The public index reports an Attribution Assurance License and prominent credit requirement; confirm against the precise upstream license file before reusing components.

**Adoption test:** create a two-page sample, export PNG and MP4, check animations, fonts, actual browser performance, saved-work recovery, print dimensions, mobile usability and whether any server receives private content.

## B. “Mirofish,” the free Palantir / simulated-society prediction engine

**Verified project:** https://github.com/oneseanlee/MiroFish (the README also refers to a historic creator/owner account). **Purpose:** open-source multi-agent *social simulation*, not a demonstrated replacement for all Palantir products.

MiroFish models a scenario using a collection of agent personas, relationships, information exposure and iterative interactions, enabling users to explore hypothesized responses across simulated crowds or narratives. Its README describes a “predicting anything” ambition and acknowledges OASIS (Open Agent Social Interaction Simulations) from CAMEL-AI. It may use language-model inference, memory, graph/agent coordination and data ingestion.

**What it can meaningfully do:** generate *scenario hypotheses*, illustrate feedback loops, stress-test narratives and discover possible stakeholder reactions under given assumptions. **What it cannot establish:** causal truth, reliable market forecasting, real population representativeness, individual human intention or ethical authority over decisions.

### Simulation evaluation protocol

1. Define a bounded question: “How might five stakeholder groups react to a new pricing policy?” rather than “Predict our launch perfectly.”
2. Document factual inputs and their dates, agent attributes, decision rules and assumptions. Never assume synthetic personas represent actual customers.
3. Separate variables you control from uncertain outcomes; explore baseline and alternative interventions.
4. Run multiple seeds, inspect variance, compare output to historical observed cases where appropriate.
5. Log model versions, inference cost, source privacy, error bounds and human reviewer disagreements.
6. Treat findings as questions for real interviews/experiments, **not predictive guarantees**.

**Privacy:** avoid uploading identifiable customer data, surveillance information, private messages or confidential company documents without lawful basis and model-provider safeguards.

## C. “RIA / REA: Reverse Engineer Anything”

**Verified upstream:** https://github.com/morluto/rea ; site https://rea.tools . The phonetic “RIA” is likely **REA**. The author describes local MCP/CLI tooling for agent-guided inspection of binaries, app behavior, JavaScript/Electron/.NET artifacts, resources and other formats depending on host/provider.

**Technical limitations:** software compiled into binaries usually cannot be reconstructed into identical original source. Static decompilation produces approximations (pseudocode, symbols when present); dynamic observation samples behavior and may miss paths. Native analysis may require approved Ghidra/Hopper/IDA installations; some tooling has OS and licensing restrictions. Running unknown binaries is itself risky.

**Reel anecdote:** “Reverse engineered my room light in five minutes without writing code; someone made an AC controller.” Neither story was independently verified from original media. Hardware integration may require authorization, valid pairing, local network control, non-invasive observation of documented interfaces and safe failure behavior.

**The 180,000-star statistic is a snapshot from the speaker, not verified as the current count**; social popularity isn't a capability/security endorsement.

### Authorized hardware-learning scenario

Study your own smart light: document manufacturer/app pairing, supported official API or local protocol, capability negotiation, failure recovery and physical override. Test on your device and network only. Prefer public SDKs, official home-automation integrations or explicit interoperability rights. Don't bypass another user's access controls, DRM, paid license requirements or proprietary service authentication.

## Comparison

| Tool | Primary purpose | Output | Why not interchangeable |
| --- | --- | --- | --- |
| Doory | Graphic content creation | Posters, slides, images, videos | Not a forecasting or binary-analysis tool |
| MiroFish | Multi-agent thought experiment | Synthetic scenario trajectories and reports | Not factual predictive certainty or a business intelligence replacement |
| REA | Authorized software investigation | Evidence and analysis, possible original implementations | Not permission to copy paid products or a magic exact-source decompiler |

## Existing related references

- [26 — OSS Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md)
- [27 — Emerging Agent Tools](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md)
- [35 — REA Research](35-OPENGYM-MOCK-INTERVIEW-REVERSE-ENGINEERING-RESEARCH.md)
- [30 — Agent Harness](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md)

Primary projects: https://github.com/shaongitbd/doory ; https://github.com/oneseanlee/MiroFish ; https://github.com/morluto/rea .
