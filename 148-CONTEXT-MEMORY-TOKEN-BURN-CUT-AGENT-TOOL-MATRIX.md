# 148 — Four Agent Tool Layers: Get Context In, Remember It, See the Burn, Cut the Burn

**Source:** user directly typed **four uppercase category headings and exactly 23 named tools** after uploading the seventeenth screenshot batch, 2026-10-26. This source is **typed, not part of any of the ten screenshots**. Exact order and names are preserved below; URLs/descriptions are independent researched matches or clearly unresolved.

## GET CONTEXT IN — 6 names

| # | Exact source name | Verified link or research status |
|---:|---|---|
| 1 | `OmniRoute` | Possible multi-model routing/context gateway; unique canonical repository unresolved |
| 2 | `9router` | Provider/route switching candidate; unique canonical source unresolved |
| 3 | `context7` | https://github.com/upstash/context7 — fresh versioned library/framework documentation delivered to coding agents; tool responses remain untrusted |
| 4 | `codegraph` | Codebase graph/symbol analysis theme; exact intended repo unresolved |
| 5 | `codebase-memory-mcp` | MCP code-context/memory candidate; exact repository owner unresolved |
| 6 | `haystack` | https://github.com/deepset-ai/haystack — RAG/retrieval AI pipeline framework; some other packages use the same name |

## REMEMBER IT — 6 names

| # | Exact source name | Verified link or research status |
|---:|---|---|
| 1 | `claude-mem` | Persistent memory for Claude Code; exact intended owner unverified from typed name |
| 2 | `mem0` | https://github.com/mem0ai/mem0 — AI memory extraction/retrieval and storage, subject to privacy controls |
| 3 | `mempalace` | Ambiguous; possible Memory Palace tool, no unique verified canonical repo |
| 4 | `cognee` | https://github.com/topoteretes/cognee — AI memory/knowledge graph and retrieval |
| 5 | `agentmemory` | Many similarly named memory repos; no uniquely verified user reference |
| 6 | `beads` | https://github.com/steveyegge/beads — durable task/issue graph for coding agents, not the same as autobiographical personal memory |

## SEE THE BURN — 4 names

| # | Exact source name | Verified link or research status |
|---:|---|---|
| 1 | `claude-hud` | Terminal usage/context/cost visualization for Claude Code; exact original owner unresolved in typed list |
| 2 | `ccusage` | https://github.com/ccusage/ccusage — CLI analysis of Claude Code token usage/cost logs, not a billing authority |
| 3 | `CodexBar` | https://github.com/steipete/CodexBar — usage/status menu-bar visualization for coding AI providers |
| 4 | `ECC` | Acronym ambiguous: may refer to Everything Claude Code; do not claim a specific repo/metrics without URL |

## CUT THE BURN — 7 names

| # | Exact source name | Verified link or research status |
|---:|---|---|
| 1 | `ponytail` | https://github.com/DietrichGebert/ponytail — overengineering prevention and engineering focus |
| 2 | `caveman` | Agent skill/product name ambiguous; no canonical resolved |
| 3 | `rtk` | Agent/CLI token-output compression candidate; verify exact upstream before installing |
| 4 | `headroom` | Agent context headroom/compression candidate; original repository unspecified |
| 5 | `oh-my-openagent` | https://github.com/code-yeongyu/oh-my-openagent — multi-agent coding workflow |
| 6 | `deer-flow` | https://github.com/bytedance/deer-flow — agent workflow framework |
| 7 | `superpowers` | https://github.com/obra/superpowers — disciplined planning, implementation and verification skills |

## Why these four categories matter together

An agent can fail from the **wrong context**, **forgotten decisions**, **opaque token/cost use**, or **unnecessary reasoning/tool calls**. These are distinct failures; none of the listed tools solves all four. Multiple overlapping plugins can produce contradictory instructions and increase token spend, which defeats the stated goal.

```text
Task spec / repository truth / package docs
  → authorized & relevance-ranked retrieval (GET CONTEXT IN)
  → working state, cited durable knowledge and task graph (REMEMBER IT)
  → measure prompt/context, completion, tool overhead, latency and cost (SEE THE BURN)
  → remove unnecessary history & improve workflow/tool selection (CUT THE BURN)
  → verify that answer correctness and user intent did not deteriorate
```

### Instrumentation and trade-offs

- Log **provider, model, model version, project, task class, input/output token counts, cached-token counts, tool-call count, latency, billed cost, retry count, context occupancy, pass/fail tests**, and confidence/source quality. Respect privacy: no raw user secrets/prompts in telemetry unless authorized.
- Measure **forecast vs actual** and include p50/p95 tail cost, not only averages. Large tool schemas, duplicate repo text, repeated recursive agent steps and retry loops often dominate.
- A compression algorithm that saves 20% tokens but removes requirements or causes 2× retries may increase total cost and regression risk.
- A memory store must support provenance, expiration, correction, user/tenant boundaries, forget/delete and protection against malicious retrieved “instructions.”
- A docs retrieval tool (Context7) is **not a source of credentials/authorization**; injected docs remain untrusted data.
- For context packing, choose file/symbol/range granularity to keep task-relevant info without dragging in irrelevant directory trees.
- Use one canonical provider router/memory store/task graph per project by default, with alternatives justified by reproducible tests.

### Suggested adoption order (research choice, no installation)

1. Define one reproducible task and baseline success/cost/latency.
2. Add one context source (current code/API docs) and source provenance.
3. Add only necessary durable state for decisions/tests, with human correction.
4. Add read-only usage instrumentation; check whether provider reports match local estimates.
5. Try one token saving mechanism (shorter tool result, selective retrieval, caching, compression or fewer agents).
6. Run same tests and compare quality, cost, latency and security incidents.
7. Roll back if a metric improves at the expense of real correctness/user control.

## Strong related references already archived

[139 — Agent Cost Forecast Learning Loop](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md) documents forecast/actual/calibration and variance clustering. [145 — Exact 40 Claude Repos](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md) shares many names. [127 — Agent Skills and Graft](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md), [126 — Browser Use](126-JEV-ULTRAFAST-AND-BROWSER-USE-AGENT-OPERATION-GUIDE.md).

**Status:** all 23 named tools preserved, no tools automatically installed and no agent memory/account accessed. Some canonical names remain unresolved because the typed list includes no URLs; don't make up owners.

## Eighteenth collection — concrete context repository and owner verification

[152 — volcengine OpenViking Context DB](152-OPENVIKING-AGENT-CONTEXT-DATABASE-RESEARCH.md) verifies `volcengine/OpenViking` (source title: “The Context Database for AI Agents”). [154 — Graft / Codebase Memory MCP](154-AGENT-RESOURCES-GRAFT-OPENMONTAGE-AGENCY-CODEBASE-RESEARCH.md) adds the later screenshot's practical description of these tools, distinguishing probable codebase-memory Graft from other homonymous products. Evaluate retrieval quality, provenance, prompt injection, privacy, real token cost and stale-memory failure. No ingestion performed.


## October 27 upstream disambiguation appendix

A live GitHub API existence check now confirms research candidates for several previously unverified labels. These are **independent project matches** (typed list had names only): [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem), [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) (also [codegraph-ai/CodeGraph](https://github.com/codegraph-ai/CodeGraph)), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), [affaan-m/ECC](https://github.com/affaan-m/ECC), [rtk-ai/rtk](https://github.com/rtk-ai/rtk), [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom), [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), and [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud). See [164](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md). **Potentially conflicting same-name projects persist**, and tool vendors' cost-saving claims remain unmeasured in this archive.
