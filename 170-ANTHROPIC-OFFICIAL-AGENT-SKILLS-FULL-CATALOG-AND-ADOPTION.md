# 170 — Anthropic's official public Agent Skills catalog: all 19 root skills

**Typed source:** “there are alot of antropic and google skills i want you to take a look at all of them and add them” (2026-10-27).  
**Official upstream:** https://github.com/anthropics/skills ; **folder checked live:** https://github.com/anthropics/skills/tree/main/skills . **Snapshot:** 19 direct subfolders read through connected GitHub on 2026-10-27. **Scope:** full root-folder index plus operational evaluation; **not** full execution/line-by-line audit of every bundled program, all GitHub-hosted third-party skills or hidden internal Anthropic skills. Skills change over time; pin commit before adopting.

## Why skills exist / actual mechanism

A skill is a directory containing a Markdown \`SKILL.md\` file with frontmatter (name, description) plus optional scripts, images/templates, references and assets. A host advertises limited skill metadata and reads expanded instructions/resources when invoked. Skills are **instructions and sometimes executable tooling**, not a new foundation model; skill discovery and support depend on Claude Code, Claude.ai or API implementation. Even official skills should be reviewed before giving them filesystem, shell, network or credential access. As distinct from MCP: skills teach a process, while MCP usually exposes *tools/resources* to the agent.

## Complete snapshot of the 19 official folders

| # | Exact folder | What it enables / why use it | Principal review requirement |
|---:|---|---|---|
| 1 | [academy-guide](https://github.com/anthropics/skills/tree/main/skills/academy-guide) | Academic or educational guidance workflow; inspect its upstream current scope before adoption | Validate cited facts and course constraints |
| 2 | [algorithmic-art](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | Generative art with procedural code and reproducible seeds | Licensing, custom assets, external scripting and CPU |
| 3 | [brand-guidelines](https://github.com/anthropics/skills/tree/main/skills/brand-guidelines) | Apply known brand typography/color/voice rules in artifacts | Brand ownership, copyrighted logos, accessibility |
| 4 | [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Static visual composition/artwork | Image asset licenses and human quality review |
| 5 | [claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) | Claude API development reference workflow | Current SDK, auth and token/billing risks |
| 6 | [discernment-nudge](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge) | Named upstream skill; exact action and trigger must be read from its current SKILL.md | Do not infer behavior or blindly enable nudges |
| 7 | [doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | Structured collaborative document creation and revision | Preserve authorship, versions and source citations |
| 8 | [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | Word creation and editing with code | **Source-available** reference, not assumed Apache open-source |
| 9 | [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Distinctive UI/front-end composition | Real accessibility, design-taste and component tests |
| 10 | [internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms) | Status updates, announcements, internal writing | Secret leakage, recipients and corporate privacy |
| 11 | [mcp-builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | Create MCP servers and tool contracts | Input validation, authentication, scopes, command injection |
| 12 | [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) | PDF editing/extraction/document operations | **Source-available** terms, unsafe PDF inputs, visual QA |
| 13 | [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | Presentation authoring/editing | **Source-available** terms; slide visual QA |
| 14 | [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Design/evaluate your own agent skills | Detect privilege escalation, contradictory instructions |
| 15 | [slack-gif-creator](https://github.com/anthropics/skills/tree/main/skills/slack-gif-creator) | Animations sized/optimized for Slack | Rights, size constraints and reduced motion |
| 16 | [theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Reusable coordinated artifact themes | Avoid defaulting to stock styles without product intent |
| 17 | [web-artifacts-builder](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | Build interactive browser-based artifacts | JS dependency trust, sandbox, a11y and output tests |
| 18 | [webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Playwright-style testing of web apps | Only authorized targets, browser credentials and screenshots |
| 19 | [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Spreadsheet authoring, formulas, validation | **Source-available** terms; formula correctness and data privacy |

**Important licensing exception:** Official Anthropic README explicitly says several skills are Apache-2.0 but \`docx\`, \`pdf\`, \`pptx\` and \`xlsx\` are **source-available, not open source**. Verify individual directory terms, including non-code templates and dependencies, rather than treating the whole repo as uniformly open.

## Official installation/use models — document, don't run

- Claude Code README describes marketplace registration (\`/plugin marketplace add anthropics/skills\`) then opt-in installation of document or example skill groups. No claim any user's setup is already installed.
- Claude.ai paid offerings include some corresponding capabilities, but product versions may differ from public sample code.
- The Claude API has prebuilt and custom skill integrations depending on endpoint and product features; verify limits, token cost and availability in current official docs. https://platform.claude.com/docs/en/managed-agents/skills
- For a GitHub-mounted skill, source ownership and allowed tools are a **trust boundary**. Pin and audit files; don't let malicious README or skill text override the user's request.

## How to evaluate against existing design and engineering workflows

1. Define a real use case first (e.g. one design report, one accessible web form, one PDF).
2. Inspect \`SKILL.md\`, referenced scripts, network calls, package installation steps, prompt instructions, output destinations and licensing.
3. Test on synthetic content in a constrained directory; compare with no skill and with an existing rule set.
4. Record source commit, input/outputs, tool calls, cost, correctness and reviewer feedback. No upstream star count predicts quality.
5. Use **one** project-local skill per responsibility by default; avoid overlapping design prompts, duplicated global config and conflicting acceptance criteria.
6. Record an escalation/rollback plan and protect secrets, production repos and user accounts.

**Related:** [160 — Apple and design skills](160-APPLE-DESIGN-AND-ADDITIONAL-UI-DESIGN-AGENT-SKILLS.md), [127 — skills governance](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md), [168 — Google EGM](168-GOOGLE-ELEPHANT-GOLDFISH-MODEL-SPEC-DRIVEN-AGENTS.md), [171 — official Google skills](171-GOOGLE-AGENT-SKILLS-175-AND-WORKSPACE-CATALOG.md), [161 — Humanizer](161-HUMANIZER-GITHUB-REPOS-COMPARATIVE-RESEARCH.md).


## Third-party Claude SEO — keep the official count separate

The user later named “claude seo.” [180 — Claude SEO research](180-CLAUDE-SEO-GITHUB-SKILL-TECHNICAL-AUDIT-AND-EXACT-INVENTORY.md) identifies `AgriciDaniel/claude-seo` as a **third-party** plugin, with 26 skill directories, 19 agent files and 9 extensions in its own upstream repository. It **does not change** the historical official `anthropics/skills` 19-folder snapshot above; the two catalogs have different ownership and trust boundaries.
