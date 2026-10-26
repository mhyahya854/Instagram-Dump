# 145 — Forty Claude Repos: Exact Instagram List, Match Confidence and Adoption Safety

**Source:** screenshot #7, heading **“40 Claude repos worth every penny”** with two numbered columns (1–20 and 21–40). All **40 labels** transcribed in original order below. Screenshot contains **NO full owner/repo paths**, so some “common” identities must remain **unverified**, and a generic name should not be turned into an arbitrary repo. None is automatically installed or recommended as a mandatory package.

## The full original 40-name inventory

| # | Screenshot wording | Independently known candidate / research status |
|---:|---|---|
| 1 | `learn-claude-code` | **Unresolved exact owner / source not displayed** |
| 2 | `karpathy-skills` | **Unresolved exact owner / source not displayed** |
| 3 | `superpowers` | [Research match](https://github.com/obra/superpowers) |
| 4 | `ponytail` | [Research match](https://github.com/DietrichGebert/ponytail) |
| 5 | `gstack` | **Unresolved exact owner / source not displayed** |
| 6 | `ECC` | **Unresolved exact owner / source not displayed** |
| 7 | `oh-my-claudecode` | **Unresolved exact owner / source not displayed** |
| 8 | `Archon` | **Unresolved exact owner / source not displayed** |
| 9 | `taste-skill` | [Research match](https://github.com/Leonxlnx/taste-skill) |
| 10 | `anthropics skills` | [Research match](https://github.com/anthropics/skills) |
| 11 | `mattpocock skills` | [Research match](https://github.com/mattpocock/skills) |
| 12 | `wshobson agents` | **Unresolved exact owner / source not displayed** |
| 13 | `claude-plugins` | **Unresolved exact owner / source not displayed** |
| 14 | `addyosmani skills` | [Research match](https://github.com/addyosmani/agent-skills) |
| 15 | `ui-ux-pro-max` | [Research match](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| 16 | `awesome-claude-skills` | **Unresolved exact owner / source not displayed** |
| 17 | `planning-with-files` | **Unresolved exact owner / source not displayed** |
| 18 | `claude-mem` | **Unresolved exact owner / source not displayed** |
| 19 | `codegraph` | **Unresolved exact owner / source not displayed** |
| 20 | `graphify` | **Unresolved exact owner / source not displayed** |
| 21 | `repomix` | [Research match](https://github.com/yamadashy/repomix) |
| 22 | `agentmemory` | **Unresolved exact owner / source not displayed** |
| 23 | `beads` | [Research match](https://github.com/steveyegge/beads) |
| 24 | `multica` | **Unresolved exact owner / source not displayed** |
| 25 | `firecrawl` | [Research match](https://github.com/firecrawl/firecrawl) |
| 26 | `cc-switch` | **Unresolved exact owner / source not displayed** |
| 27 | `context7` | [Research match](https://github.com/upstash/context7) |
| 28 | `vibe-kanban` | **Unresolved exact owner / source not displayed** |
| 29 | `github-mcp` | **Unresolved exact owner / source not displayed** |
| 30 | `playwright-mcp` | [Research match](https://github.com/microsoft/playwright-mcp) |
| 31 | `serena` | [Research match](https://github.com/oraios/serena) |
| 32 | `claude-code-router` | **Unresolved exact owner / source not displayed** |
| 33 | `awesome-mcp-serv` | **Unresolved exact owner / source not displayed** |
| 34 | `system-prompts-ai` | **Unresolved exact owner / source not displayed** |
| 35 | `best-practice` | **Unresolved exact owner / source not displayed** |
| 36 | `codex-plugin-cc` | **Unresolved exact owner / source not displayed** |
| 37 | `claude-hud` | [Research match](https://github.com/jarrodwatts/claude-hud) |
| 38 | `rtk` | [Research match](https://github.com/rtk-ai/rtk) |
| 39 | `headroom` | **Unresolved exact owner / source not displayed** |
| 40 | `caveman` | **Unresolved exact owner / source not displayed** |
 
**Important original source ambiguities:** `awesome-mcp-serv` is visibly truncated, likely a longer name but **do not silently expand it**. `multica` may be the start of a repo owner or project, not necessarily `multica-ai/andrej-karpathy-skills`. `system-prompts-ai`, `best-practice` and `claude-plugins` are insufficiently unique to identify safely. `ECC` may refer to Everything Claude Code or another project; do not conflate solely by acronym. `repomix` appears in the screenshot as a word, verified candidate `yamadashy/repomix` is a tooling ecosystem but still requires matching to the reel owner.

## How to turn a trending list into a useful skill catalog

| Functional cluster | Source-number candidates | Meaningful concrete checks |
|---|---|---|
| Planning/execution | 3 superpowers, 4 ponytail, 5 gstack, 7 oh-my-claudecode, 17 planning-with-files, 28 vibe-kanban | Specs, task boundaries, rejection criteria, deterministic tests, no unbounded loops |
| Design and visual critique | 9 taste-skill, 14 addyosmani skills, 15 ui-ux-pro-max | Project visual identity, real screenshot comparison, WCAG, reduced motion, anti-slop without copying brands |
| Agent ecosystem and skills | 1, 2, 10, 11, 12, 13, 16, 24, 33, 34, 35, 36 | Real repo ownership, SKILL.md scripts, prompt injection, permissions and licensing |
| Context/memory | 18 claude-mem, 19 codegraph, 20 graphify, 21 repomix, 22 agentmemory, 23 beads, 27 context7, 31 serena | Relevant evidence/retrieval, stale context supersession, user isolation and sensitivity |
| Tools and connectivity | 25 firecrawl, 26 cc-switch, 29 github-mcp, 30 playwright-mcp, 32 claude-code-router | Authentication scope, browser permissions, read/write actions, secrets and data exfiltration |
| Spend/context observability | 6 ECC, 37 claude-hud, 38 rtk, 39 headroom, 40 caveman | Token cost instrumentation, context compression quality and actual correctness after change |

## Repeated previously catalogued items

`ponytail`, `superpowers`, `taste-skill`, `anthropics skills`, `mattpocock skills`, `addyosmani skills`, `ui-ux-pro-max`, `context7`, `playwright-mcp` are already covered in earlier Instagram-Dump notes. **Do not duplicate their installed copies or create competing global agent instructions**. Cross-reference [05 — Things to Find](05-THINGS-TO-FIND.md), [06 — Failure Mitigation](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md), [124 — AI Coding Workflow](124-COST-CONSCIOUS-STACK-GSD-ROO-RALPH-CODERABBIT-LINKEDIN.md), [127 — Skills Governance](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md).

## Claims and limitations

The title “worth every penny” is a subjective reel recommendation; repos can be free, paid, outdated, unsafe or abandoned. **Names, not versioned repo URLs, are what the screenshot supplies**. Candidate links above are research matches (not every match was reverified at this instant). Source existence, security quality, current compatibility and commercial rights are distinct. Never install a 40-item list blindly: pin commit, inspect prompts/install scripts/permissions, test with fake data, measure resource cost and keep a rollback.

**Status:** source-exact 40 entries archived; no skill installed, no version fixed, no user's agent settings changed.
