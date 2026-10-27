# 164 — Forty Claude repositories: live GitHub owner verification and risk matrix

**Audit:** 2026-10-27; supplement to the **original screenshot-order transcript** in [145](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md). The screenshot provided names but mostly **no owners**. A live GitHub repository API check establishes that the linked repositories exist; it **does not establish** that the Instagram creator intended them, nor audit their code, security, performance or license at every asset level. Numbers refer exclusively to file 145 and retain the exact source order.

## Live repository existence checks

The entries marked **strong** have a distinctive project name and an upstream repository that matches its function. **Candidate** means name alone admits several matches. **Unresolved** means no sufficiently convincing original-project identity was established.

| Screenshot # | Literal name | Live GitHub repository | Match assessment | Role and significant caution |
|---:|---|---|---|---|
| 1 | learn-claude-code | [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) | Strong candidate | Educational minimal agent harness, not Anthropic's proprietary implementation |
| 2 | karpathy-skills | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Candidate | CLAUDE.md coding guidance; attribution to Karpathy is descriptive, not endorsement |
| 3 | superpowers | [obra/superpowers](https://github.com/obra/superpowers) | Previously matched | Planning/test discipline; inspect skill privileges |
| 4 | ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Previously matched | Design for simpler agent changes; savings not benchmarked |
| 5 | gstack | [garrytan/gstack](https://github.com/garrytan/gstack) | Strong candidate | Opinionated role-specific Claude workflow and QA |
| 6 | ECC | [affaan-m/ECC](https://github.com/affaan-m/ECC) | Candidate | Everything Claude Code ecosystem; acronym is not unique, distinguish source, plugin and npm identifiers |
| 7 | oh-my-claudecode | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | Strong candidate | Multi-agent coordination; package identity differs from repository branding |
| 8 | Archon | [archondevio/archondev](https://github.com/archondevio/archondev) | **Unresolved** | This is one different project called Archon; cannot attribute the screenshot's Archon to it |
| 9 | taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Previously matched | UI style skill; evaluate a11y and consistency |
| 10 | anthropics skills | [anthropics/skills](https://github.com/anthropics/skills) | Previously matched | Official examples; permissioned scripts still merit review |
| 11 | mattpocock skills | [mattpocock/skills](https://github.com/mattpocock/skills) | Previously matched | Agent skill author library |
| 12 | wshobson agents | [wshobson/agents](https://github.com/wshobson/agents) | Strong candidate | Agent/plugin marketplace; third-party tools extend attack surface |
| 13 | claude-plugins | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | **Candidate only** | Official plugin directory exists; source could mean a different plugin collection |
| 14 | addyosmani skills | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Previously matched | Web-quality skills |
| 15 | ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Previously matched | Aesthetic/UI help, not automated correctness |
| 16 | awesome-claude-skills | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | **Candidate only** | Several unrelated repositories share this exact title |
| 17 | planning-with-files | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Strong candidate | Durable task files and recovery; don't copy secrets into plans |
| 18 | claude-mem | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Strong candidate | Persistent agent memory; retention, injection, access controls |
| 19 | codegraph | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | **Candidate only** | Alternative [codegraph-ai/CodeGraph](https://github.com/codegraph-ai/CodeGraph) also exists; distinguish owners |
| 20 | graphify | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Candidate | AST/code knowledge graph and retrieval; do not mistake graph for definitive program analysis |
| 21 | repomix | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Previously matched | Repo text packaging; redact secrets and private paths |
| 22 | agentmemory | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | **Candidate only** | Competing similarly named memory projects; provenance and deletion |
| 23 | beads | [steveyegge/beads](https://github.com/steveyegge/beads) | Previously matched | Task state, not autobiographical memory |
| 24 | multica | [multica-ai/multica](https://github.com/multica-ai/multica) | Candidate | Collaboration platform; separate from the Karpathy skills repository |
| 25 | firecrawl | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | Previously matched | Web extraction; honor site permissions, privacy, scale and cost |
| 26 | cc-switch | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | Strong candidate | Cross-agent provider/config switch; protect provider keys |
| 27 | context7 | [upstash/context7](https://github.com/upstash/context7) | Previously matched | Library docs retrieval; retrieved instructions are untrusted |
| 28 | vibe-kanban | [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Strong candidate | Task board/agent execution; review write privileges |
| 29 | github-mcp | [github/github-mcp-server](https://github.com/github/github-mcp-server) | Strong candidate | Official GitHub MCP; use least-privilege tokens and protected branches |
| 30 | playwright-mcp | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Previously matched | Browser automation, credentials and untrusted sites risk |
| 31 | serena | [oraios/serena](https://github.com/oraios/serena) | Previously matched | Code intelligence tools |
| 32 | claude-code-router | [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Strong candidate | Local model routing; compatibility and key exposure |
| 33 | awesome-mcp-serv | **Unresolved original truncated name** | Unresolved | User-supplied expansion `awesome-mcp-servers` is a lead, not pixel evidence |
| 34 | system-prompts-ai | **Unresolved** | Unresolved | Multiple model/system-prompt collections; copyright and provenance issues |
| 35 | best-practice | **Unresolved** | Unresolved | Generic name, many non-equivalent projects |
| 36 | codex-plugin-cc | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | Strong candidate | Codex delegation from Claude Code; verify action scope and credentials |
| 37 | claude-hud | [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | Previously matched | Usage visualization; local logs may undercount provider bill |
| 38 | rtk | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | Previously matched | CLI output reduction; must preserve error context |
| 39 | headroom | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Strong candidate | Tool-output/context compression; verify semantic preservation |
| 40 | caveman | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Strong candidate | Aggressive text brevity/proxy skill; headline savings are project claims |

**How these were verified:** GitHub connected integration: repository metadata API responses showing full owner/name, description, archival flag, public status, license metadata where supplied, and pushed dates on **2026-10-27**. Links here are recorded upstream URLs; no packages or READMEs from these projects were executed. Star counts deliberately omitted because they change and are not evidence of code quality. An existence check is not a security review.

## Operational installation models

- **Skill or rules document** (e.g., Karpathy skills, taste-skill): read markdown carefully for destructive shell commands, invisible hooks, spoofed policies and credential requests; use project-specific scope where possible.
- **Plugin/marketplace** (ECC, oh-my-claudecode, wshobson): check both marketplace manifest and transitive installers, network calls, model-routing secrets, tool permissions, auto-update behavior.
- **CLI/server/MCP** (GitHub MCP, Playwright MCP, Context7, routers): authorize minimal actions, pin artifact hashes, sandbox untrusted code, review exposed tools; MCP results are data, not privileged instructions.
- **Memory/context system** (claude-mem, CodeGraph, graphify, agentmemory): apply tenant boundaries, source provenance, freshness/expiry and deletion before ingesting real user or private repository data.
- **Monitoring/cost-saving** (claude-hud, rtk, headroom, caveman): benchmark *end-to-end task correctness* and total cost, not compression percentage alone.

## A reproducible evaluation protocol

1. Record exact upstream URL, commit SHA, release, license paths and dependent services. Check upstream's actual code, scripts and third-party assets: a top-level MIT label cannot license everything.
2. Define three realistic but non-sensitive tasks per tool. Baseline without tool and run test with a pinned tool version and consistent model/settings.
3. Measure correctness/acceptance tests, p50/p95 cost, input/output/cache tokens, wall time, retries, exposed data, prompts injected and required permissions.
4. Trial an untrusted retrieved document that says to ignore system instructions; require the agent to treat it as task data. Review OS/filesystem/network isolation.
5. Classify outcome: adopt, sandbox further, retain only as reference, or reject. Record failures and re-evaluate when the release changes.

## Archive navigation

- Original numbered screenshot **must remain in** [145](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md).
- Four-layer functional taxonomy: [148](148-CONTEXT-MEMORY-TOKEN-BURN-CUT-AGENT-TOOL-MATRIX.md).
- Cost and quality instrumentation: [139](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md) and [165](165-AGENT-COST-TELEMETRY-SCHEMAS-AND-CALIBRATION.md).
- External source descriptions change; original screenshot labels never change.
