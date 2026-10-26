# 152 — OpenViking: Context Database for AI Agents

**Original image:** `image(20261026-172849).png`: title **“OpenViking: The Context Database for AI Agents”**, with large play icon across `AI Agents`. This image alone does **not** include architecture, setup details or performance benchmarks.

**Canonical verified project:** [volcengine/OpenViking](https://github.com/volcengine/OpenViking), documentation [docs.openviking.ai](https://docs.openviking.ai/). The upstream README directly says “The Context Database for AI Agents”; the repo identifies **AGPLv3** (check exact license for the pinned version before embedding in a proprietary project).

## Purpose and design

OpenViking is a structured **agent context and memory database** intended to organize user/project information, resources and skills so an AI agent can navigate relevant context rather than re-read a whole repo each turn. Main architectural ideas: hierarchical/virtual filesystem abstraction, metadata, retrieval/indexing, persistent data, and programmable access for agents.

### Conceptual architecture (not a claim that each feature exists in every release)

```text
project files / docs / skill content / observations
        ↓ parse, index, provenance, access scope
   structured context database
        ↓ scoped search / navigation / relevance
   model context packing (token budget)
        ↓ user-authorized action + tests
 verified result, refreshed memory and citations
```

### What to check before adoption

- Version/build maturity, Python/server prerequisites, disk/index footprint, embeddings provider and exact API; verify the release README rather than guessing setup commands.
- Private repos and PHI-sensitive information must remain in access-controlled storage; distinguish a **locally hosted index** from an **external embeddings/model API** that may transmit content.
- RAG retrieval is a *citation* and *relevance* tool, not a trustworthy instruction channel. Mark stored page text as untrusted, require provenance and test prompt-injection resistance.
- Stale information must be superseded/revalidated against files, Git history and current commits; apply deletion/export/retention controls.
- The real win is lower repeated exploration **while preserving correctness**: benchmark retrieval accuracy, latency, actual tokens spent, stale-answer rate and tool calls against a naive `rg`/code search baseline.

## Position among the user's other agent tools

- [127 — Graft](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md): multiple unrelated name collisions; codebase-memory option relates to this problem.
- [148 — Context + memory matrix](148-CONTEXT-MEMORY-TOKEN-BURN-CUT-AGENT-TOOL-MATRIX.md): Context7, codegraph, Codebase Memory MCP, Mem0 and other choices; *not* automatically compatible.
- [139 — Forecast-vs-actual observability](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md): measure benefit rather than asserting magic token savings.

**Status:** source title captured, repo identified and README checked; no server, index, account, search or agent connection started.
