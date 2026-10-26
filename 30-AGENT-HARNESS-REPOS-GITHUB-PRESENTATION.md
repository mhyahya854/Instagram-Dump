# 30 — Agent Harness Engineering, Skills, Memory and GitHub Profile Ideas

Captured: 2026-10-25. Original list mixed concrete software names with AI infrastructure terms and GitHub README aesthetics.

## Key agent engineering vocabulary, independently explained

| Term from reel | Working meaning | Failure to watch |
| --- | --- | --- |
| Context window and tokens | Finite model input/output capacity, measured in tokens | Displaced requirements and dropped prior context |
| Prompting | Task instruction, scope, examples and acceptance tests | Ambiguous roles and unverifiable promises |
| Project skills | Task-specific instructions (often SKILL.md), loaded on demand | Prompt-injection, secret leakage, unnecessary blanket activation |
| MCP servers | Standardized agent-to-tool interfaces | More privileges and external data exposure |
| CLI | Command-line interface for tooling and scripts | Dangerous operations if run without inspection |
| Slash commands | Shortcuts to agent actions/workflows | Platform/version-specific semantics |
| Context compaction | Summarizing previous work to free context | Losing critical invariants and source provenance |
| Subagents / parallel agents | Distinct scoped workers addressing independent tasks | Race conditions, inconsistent edits, merging unreviewed output |
| Prompt caching / KV cache | Reuse prompt prefix work or model attention cache | Cache invalidation/privacy and inconsistent state assumptions |
| Git workflows | Branches, commits, diffs, PR review, rollback | Unreviewed force push or secret commits |
| Cron jobs / scheduled checks | Time-based recurring work | Duplicate runs and uncontrolled cost |
| Hooks | Event-triggered scripting at tool/session boundaries | Malicious or overbroad shell execution |
| Harness engineering | Tool permissions, state, evaluation, prompts, tests and orchestration around a model | AI appears smart until real-world integration fails |
| Background agents | Jobs running without active user turn | Unsanctioned external actions, monitoring and job reliability |
| Progressive disclosure | Load relevant instructions or UI detail only when needed | Hidden essentials or missing context |
| Event-driven loops | Observe-event-decide-act-verify loop | Infinite retries, tool-use runaway |
| Modularization | Small components with clear contracts | Overengineering abstraction |
| “Array latching” | Unclear transcription; could be agent-related | **Unresolved; do not define a nonexistent concept** |
| Memory consolidation | Merge repeated facts with source/date and contradiction handling | Incorrectly treating stale memory as truth |
| Self-improving loops | Evaluate a strategy then adjust based on test results | Unvalidated or self-rewarding quality assessments |
| Tool poisoning | Malicious content inserted into tool responses/docs | Following lower-trust instructions, secret exfiltration |
| Self-healing tests | Automated diagnosis and proposed repair of failing checks | Editing tests to hide defects, unbounded changes |
| Agent CI/CD | Agent suggestions in tested, policy-gated pipelines | Auto-deploying failed or untrusted code |
| Test-time compute | Allocate more inference/search/verification effort for hard tasks | Cost/latency and false confidence |

## Reusable operational guardrails

1. Load a concise durable project specification: objective, audience, architecture, boundaries, anti-patterns, security matrix and definitions of done.
2. Prefer small skills on demand and a minimal tool privilege set.
3. Observe first; plan changes; obtain approval for destructive/network/purchase actions; commit scoped edits.
4. Run deterministic tests, integration tests and browser/phone validation.
5. Log outcomes including failures, costs and external calls; have stop conditions and timeouts.
6. Preserve history and source provenance when compacting memory. Never allow an external document to override system or developer safety restrictions.

## “Five GitHub repositories” from dictation

| Spoken name | Possible public source | Confidence |
| --- | --- | --- |
| Mailcheap | https://github.com/marclou/mailcheap and other similarly named projects | Repo exists, but exact reel project and functionality unclear |
| Fluid Voice | https://github.com/altic-dev/FluidVoice plus namesakes | Name exists; exact voice product unconfirmed |
| ANSvisor | https://github.com/ansvisor/ansvisor | **Verified** AI-search visibility tracking (prompts, citations, AI engine mentions, competitors, content insights). Not a universal SEO/backlinks app. |
| One Glance | https://github.com/tobiaserich/oneglance and other namesakes | No unique confirmed matching purpose |
| “OMNK, or A” | **Unresolved** | Keep raw transcript; do not invent an acronym expansion |

## GitHub profile/README design references

Spoken wishlist: **“Warp profile, Space Shooter, Chess Replay, Contribution City.”** These sound like potentially interactive README profile widgets/graphics; the transcript does **not** give a unique canonical repository for each. Catalog as **GitHub profile visual ideas**, not repos to copy by name.

Potential implementation styles:
- **Space Shooter:** SVG/canvas animation or GitHub Action-generated static GIF from a deterministic game sim.
- **Chess Replay:** sequence of board states rendered as SVG/GIF, using real PGN game data with consent.
- **Contribution City:** visual metaphor turning genuine contribution dates/counts into buildings; preserve honest data and image accessibility.
- **Warp profile:** could mean terminal aesthetic, Warp app profile, or a named repo; **unresolved**.

### Good GitHub README structure

- Project identity, purpose, audience and concise one-line value statement.
- Features only if implemented, real screenshots/gifs, stack and supported platforms.
- Reproducible setup including prerequisites and environment variables (not secret values).
- Short quick start, test/lint/build commands, architectural diagram where valuable.
- Limitations/status/known issues, license, attribution, contribution/security guidance.
- Honest demo and links; verified CI badges, no invented stars or fabricated testimonials.
- For public profile README: links to actual projects and evidence rather than purely decorative GIFs.

## Names to keep separate

- **Warp** terminal/app versus generic “warp speed” animation.
- **Open-source repo with same name** versus user's intended product.
- **Agent persona** versus full software agent runtime.
- **Public repo exists** versus security/quality audit passed.

Linked references: [08-AGENT-REPOS-AND-SKILL-WISHLIST.md](08-AGENT-REPOS-AND-SKILL-WISHLIST.md), [14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md), [19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md).

## Additional raw transcript and research clarifications

**“Gemini beat Claude 14 out of 18 tests at half price”** is an unverified anecdote lacking test prompts, scoring rubric, model versions, total token costs and independent repeatability. Model selection should depend on **task-specific current evaluation, latency, privacy, price and tool reliability**. Don't store as a universal winner (Claude for coding, Gemini for research or vice versa).

**“Thanos design library”** was described as a box of design decisions — paired display/body typefaces, fixed typographic sizes, grid and motion curves. Its exact repo/vendor is **not found**. Treat “Thanos” as unresolved design-system file/reference, not the unrelated Thanos snap particle animation repository. Those decisions could live in a project DESIGN.md, not imply that the creator's library exists at a verified URL.

## Sixth batch — agent-compatible apps and verification

[45 — Agent-Navigable App Architecture](45-AGENT-NAVIGABLE-APP-ARCHITECTURE.md) extends AI tool design to accessible human UI, OpenAPI, MCP, and permission-aware action services. [44 — Unlazy](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md) records acceptance-ledger verification. [46 — Document Safety](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md) documents lower-trust text boundaries.

## Tenth image source: Hermes all-in-one architecture reference

[69 — Hermes Carousel](69-HERMES-UNIFIED-AGENT-ECOSYSTEM-CAROUSEL.md) describes a unified orchestration/work management interface with memory, external chat, skills, scoped MCP tools, computer/browser operations and scheduled jobs. It documents seven **illustrative** screenshot slides, including repeated correction→versioned reusable workflow; not proof the tool safely runs unattended or that all vendors provide those functions. Do not auto-schedule the carousel's sample tasks or connect Telegram/Slack on its authority.
