# 157 — Seven Useful Agent Repositories: Complete Source Transcription and Repo Research

**Original image:** `image(20261026-181444).png`. Source headline: **“These 7 repos give your agents some seriously useful capabilities:”**. The following seven items are **all** transcribed in original order:

1. **Browser Use** — lets your agent operate a real browser, click through pages, and complete workflows.
2. **Agent Memory** — gives your coding agent persistent memory so it can carry context across tasks.
3. **Scientific Agent Skills** — 160+ skills designed to turn an AI agent into a powerful research assistant.
4. **Diagram Design** — a collection of diagrams built specifically for Claude Code workflows.
5. **Anthropic Cybersecurity Skills** — cybersecurity capabilities designed for modern coding agents.
6. **Awesome Harness Engineering** — orchestration patterns and resources for building better agent systems.
7. **Open Viking** — a context system for giving agents better access to the information they need.

## Independently verified matches and role

| Label | GitHub source / status | What matters |
|---|---|---|
| Browser Use | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Navigate unfamiliar web UIs with observation/action loops; log-in and mutation boundaries; see [126](126-JEV-ULTRAFAST-AND-BROWSER-USE-AGENT-OPERATION-GUIDE.md) |
| Agent Memory | **Ambiguous**, may reference [agentmemory](148-CONTEXT-MEMORY-TOKEN-BURN-CUT-AGENT-TOOL-MATRIX.md) or other memory repos | Memory must have provenance, scope, retention, invalidation and privacy constraints |
| Scientific Agent Skills | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | Official repo README currently advertises **177 skills**; screenshot says **160+**, so don't conflate dynamic current catalog with source claim |
| Diagram Design | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Self-contained **HTML + SVG** diagrams, 45 diagram types per README; not merely arbitrary Mermaid graph snippets |
| Anthropic Cybersecurity Skills | **Unresolved precise canonical owner** from this screenshot | Distinguish official Anthropic plugins from [trailofbits/skills](https://github.com/trailofbits/skills), project-specific defensive training and generic names |
| Awesome Harness Engineering | [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | Curated architectures/templates for orchestrator, approvals, context compaction, testing and recovery |
| Open Viking | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Database/index for scoped agent context, [152](152-OPENVIKING-AGENT-CONTEXT-DATABASE-RESEARCH.md) |

## Bounded workflow

1. Plan goal and ownership; define data that an agent may see.
2. Build minimal plugin/tool manifest and grant least privileges per agent.
3. Retrieve evidence-backed source context; do not elevate retrieved page instructions.
4. Execute only permitted actions. All sensitive external writes, device control and user-account interactions need authorization.
5. Test agent output with independent deterministic assertions. Diagram creation requires rendered correctness; scientific work requires accurate citations and reproducible calculations.
6. Record outcome, token/tool costs, failure reasons and changes to memory. Use [139 — forecast loop](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md).

**Status:** seven source labels preserved, six candidate categories linked, at least two exact product identities (Agent Memory, Anthropic Cybersecurity Skills) are not proven by the screenshot. No packages installed, browser driven, experiments conducted or code modified.
