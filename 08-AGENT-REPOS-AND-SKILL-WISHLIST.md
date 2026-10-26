# Reel Notes 08 — AI Agent Repositories, Coding Skills and Design Tools

_Captured 2026-10-25. Research notes, not an installation order._

## How to read this without an internet connection

A **repository** is a versioned project directory. An **agent persona** is usually an instruction file assigning a domain role and workflow; it is **not** a separately trained model. An **agent skill** is a reusable instruction package (often `SKILL.md`) loaded for a particular task. A **plugin** may execute code, call services or intercept agent actions and needs stronger security review. A **design asset** may be licensed intellectual property rather than a reusable open-source component.

Tags: **CONFIRMED REPOSITORY** = canonical owner and repo verified, not source-code audited. **LIKELY** = spoken phrase plausible but attribution unverified. **UNRESOLVED** = no defensible identity. **WISHLIST** = user wants to examine/install eventually, not approval to run it now.

## A. Newly discovered projects from reels

| Spoken name | Resolved name and source | What it actually does | Caveat |
| --- | --- | --- | --- |
| “Agency Dash Agents” / “230 agents” | **The Agency / Agency Agents**, https://github.com/msitarzewski/agency-agents | Collection of 230+ specialist **Markdown agent personas**: engineering, design, backend, QA, security, marketing, sales, product, operations, etc. Each persona supplies goals, workflow, success measures and deliverables; installers/converters support Claude Code, Cursor and other coding agents. | Not 230 separately trained models; specialization is prompt/workflow scaffolding and quality varies. The related https://agencyagents.dev may show a different agent count at a given date. |
| “Agent Reach” | **Agent Reach**, https://github.com/Panniantong/Agent-Reach | Agent-oriented command-line interface routing requests to tools for web, YouTube, GitHub, X, Bilibili and selected platforms. Diagnostics check which channels work. | Access depends on platform, login, cookies, rate limits and current versions. **Oct 23 2026 v1.6.0**: web/YouTube/GitHub/Bilibili defaults; some other networks optional/experimental. No guarantee of Instagram, LinkedIn, or private-site access. |
| “AwesomeDesigns.fd” | **UNRESOLVED** | Reel claims ready-made design files inspired by brands like Raycast and Vercel to use as references. | “.fd” may be misheard; **do not fabricate a GitHub URL or license**. Replicating a commercial site's protected design is not automatically licensed. |
| “Hallmark” | **Hallmark**, https://github.com/Nutlope/hallmark | Anti-generic AI-design skill; builds, audits, redesigns and studies site design; tests recurring slop such as eyebrow labels, redundant decoration and fake form success. | Counts of styles or “slop tests” change by version. Original reel's 57 tests is an old snapshot, not a permanent invariant. Skill output still needs real screenshots and browser checks. |
| “Impeccable” | **Impeccable**, https://github.com/pbakaus/impeccable | Design guidance and UI quality workflows for agents; useful for detecting generic template output. | Do not assume star count, effectiveness or exact command names without inspecting a pinned release. |
| “Garry Tan’s workflow” / “few staff” | **gstack**, https://github.com/garrytan/gstack | Opinionated Claude Code workflows for planning, CEO/product review, QA, release, code review and related engineering roles. | Can install browser/runtime tooling; inspect version and scripts first. |
| “Taskmaster” | **Task Master**, https://github.com/eyaltoledano/claude-task-master | Structure a larger project into tasks, dependencies, tracking and agent workflow. | Project may add process overhead for small apps. |
| “Serena” | **Serena**, https://github.com/oraios/serena | Semantic codebase navigation/editing using language tooling, so agents can locate symbols and references instead of guessing. | Requires compatible languages and tool setup; review file-modifying operations. |
| “Trail of Bits” | **Trail of Bits Skills**, https://github.com/trailofbits/skills | Security-focused agent skill repository for vulnerability and code review work. | Skills are advisory; scanners and threat-model tests remain essential. |

## B. Expressed skill-installation wishlist (NOT installed)

User reel: “I want … Ponytail, Matt Pocock skills, I have ADHD, security, artist skills, Superpowers, design, diagram design, humanizer, graphic design, Handy, … Impeccable.”

| Name / intent | Link when confidently identified | Status |
| --- | --- | --- |
| Ponytail | https://github.com/DietrichGebert/ponytail | Previously user-approved for **catalog** |
| Matt Pocock Skills (“mark, Poco, Poco”) | https://github.com/mattpocock/skills | Previously user-approved for **catalog** |
| Karpathy-style engineering simplicity | https://github.com/multica-ai/andrej-karpathy-skills | Previously user-approved for **catalog**, community implementation |
| Superpowers | https://github.com/obra/superpowers | Verified and on wishlist |
| UI/UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Previously user-approved for **catalog** |
| Impeccable | https://github.com/pbakaus/impeccable | Confirmed repo, requested on wishlist |
| Hallmark | https://github.com/Nutlope/hallmark | Confirmed repo, requested reference |
| Security Guidance | https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance | Confirmed official Claude Code plugin |
| Trail of Bits Skills | https://github.com/trailofbits/skills | Confirmed security skill catalog |
| Design Engineering | https://github.com/ryktara/design-engineering-skill | Previously approved as catalog candidate |
| Design and diagram-design skills | Multiple possible choices; see existing 06 catalog | Category, no exact repository asserted |
| Humanizer / graphic-design skills | Exact author/source unknown | **UNRESOLVED**; assess provenance and any misleading content risk |
| “Handy” | Ambiguous project name | **UNRESOLVED** |
| “I have ADHD” | Could be creator's comment, separate name or request for ADHD-friendly skills | **UNRESOLVED**; do not assume it is a repository |
| “GitHub stack to take everything clear” | Possibly gstack but uncertain | Preserve transcript |
| “specs code” / “stricts for uptests” | Uncertain possible specification and test skills | Do not invent links |

## C. What “specialized” should mean in practice

A helpful specialist file has: a narrow role, explicit inputs, domain criteria, a sequence of checks, artifact outputs, defined stop conditions, and verification steps. A renamed system prompt without evidence, tools or scoped procedures is **not independently validated expertise**. Compare personas against actual tests and humans, not just claims.

Example: a **frontend specialist** could review accessibility, focus, responsiveness, visual hierarchy and real UI states; a **security reviewer** could examine authentication, database permissions, data flow and attacker paths. These are different evaluations even if both use the same language model.

## D. Skill supply-chain safeguards

1. Only shortlist canonical sources; pin reviewed commits and licenses.
2. Inspect `SKILL.md`, every script, helper, install hook and external URL. Treat downloaded instructions as untrusted.
3. Scan with NVIDIA SkillSpector and standard secrets/dependency tools when applicable. No scanner is an all-clear certificate.
4. Never send production secrets, real customer data, or unscoped session cookies to unreviewed tools; use sandboxed scopes, limited permissions and isolated test accounts.
5. Approval to **keep in this catalog** does **not** authorize installation, code execution, broad GitHub write access, unattended posting or cloud charges.
6. Verify tool actions (logs/tests/screenshots), not merely an agent's natural-language “done.”

## Attribution and verification ledger

- **Confirmed repo identities** in this file: Agency Agents, Agent Reach, Hallmark, Impeccable, gstack, Task Master, Serena, Trail of Bits, Ponytail, Matt Pocock, Karpathy Skills, Superpowers.
- **Reel promotional claims not independently verified:** exact stars (e.g., 75K, 78K, 120K), exact numbers of themes/tests, effectiveness and “specialized not reskinned” characterization.
- **Unidentified:** AwesomeDesigns.fd, Handy, humanizer/graphic-design author, “I have ADHD” as name, “specs code” and “stricts.”
- Original larger discovery backlog: [05-THINGS-TO-FIND.md](05-THINGS-TO-FIND.md); expanded verified projects: [06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md).

## Primary references

- Agency Agents README: https://github.com/msitarzewski/agency-agents/blob/main/README.md
- Agent Reach release history: https://github.com/Panniantong/Agent-Reach/releases
- Hallmark README: https://github.com/Nutlope/hallmark/blob/main/README.md
- gstack README: https://github.com/garrytan/gstack
- Anthropic Security Guidance documentation: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/security-guidance/README.md


## More agent/quality research from second reel batch

[19 — Agent Skills, Hooks & Code-Drawn Animation](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md) adds Get Shit Done, an unresolved “RAL flow”, CodeRabbit, SlopMonster, Emil Kowalski's Apple Design, Claude Code hooks, the Figma-to-Playwright workflow and unresolved “UI UX Comma Design”. These are **research leads**, not installed skills.

## Additional agents/skills — second reel batch

[19 — Agent Skills, Hooks and Programmatic Animation](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md) records GSD, CodeRabbit, SlopMonster, Apple Design, Claude Code hooks, Figma-to-browser-QA workflows and uncertain titles. Research mention is not installation permission.

## Eighth reel batch: design and engineering skills (research only)

[63 — Ten Skills](63-TEN-AGENT-SKILLS-WEB-ASSETS-SLIDES-IOS-SUPABASE-MARKETING.md) adds source candidates for app/web assets, frontend slides, iOS simulator operation, official Supabase agent guidance, relevant marketing prompts, Emil design engineering, HyperFrames, Impeccable, Taste and skill discovery. [62 — Immersive Web MCP](62-IMMERSIVE-WEB-GSAP-TASTE-21ST-SHADCN-MCP.md) documents the official 21st and shadcn MCP interfaces. Their external code/dependency installation and permissions require a separate review. [64](64-DESIGNER-RESOURCE-LEADS-REVERSAL-LAB-SKILLS.md) preserves Reversal Lab as unresolved.
