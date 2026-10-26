# 137 — Superpowers: Verified Agentic Development Skills for Codex, Claude Code and Others

**User source:** explicit typed **“SUPERPOWERS SKILL”**, sixteenth Instagram batch, 2026-10-26. There is no screenshot of Superpowers in this batch.

**Canonical source:** **https://github.com/obra/superpowers** . Official creator Jesse Vincent / Prime Radiant; public MIT license in the verified repository. The same repo already appeared in the archive [06 — 68 Repositories](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md), so this is an *expanded use guide*, not a newly discovered brand.

## What is distinctive

Superpowers is a **development method implemented through multiple agent skills**, not “one prompt that writes apps perfectly”. It pushes brainstorming/design agreement, detailed plan, isolated worktrees, task execution, red/green test-driven development, systematic debugging, code review, and actual verification. Read current README: https://github.com/obra/superpowers#readme .

### Typical verified workflow

1. `brainstorming` — clarify goal, users, requirements, tradeoffs and design decisions; obtain human approval of design where requested.
2. `using-git-worktrees` — isolate changes from main (repo baseline, clean worktree).
3. `writing-plans` — tasks referencing exact real files, expected behavior, tests and estimates.
4. `subagent-driven-development` or `executing-plans` — implement scoped tasks, verify spec compliance before style or quality review.
5. `test-driven-development` — write failing test first; implement minimum passing behavior, refactor.
6. `requesting-code-review` and `systematic-debugging` — independent review and root-cause investigation rather than “looks good”.
7. `verification-before-completion` and `finishing-a-development-branch` — actual test outputs, merge/PR choices, no unverified success declarations.

## Installation discovery (documentation only; not executed)

**Codex App:** official repository documents **Plugins → Coding → Superpowers → Install**.
**Codex CLI:** `/plugins` → search `superpowers` → install using official menu.
**Claude Code:** creator documents official plugin marketplace `/plugin install superpowers@claude-plugins-official`.
**Cursor:** `/add-plugin superpowers` through marketplace.
**Antigravity:** official README gives `agy plugin install https://github.com/obra/superpowers`.
**Hermes:** `hermes plugins install obra/superpowers --enable` with restart of an existing session.
**Other clients:** check the platform-specific upstream install before using scripts or plugins; availability changes.

**Do not run these commands automatically in this archive**. Installing means trusting third-party skill instructions/hooks and potentially executable scripts.

## Practical project-local evaluation

- Verify owner, immutable commit and all `SKILL.md`/hooks; check network fetch, shell, workspace permissions and license.
- In disposable repo with synthetic data, compare same task **with and without** Superpowers: spec adherence, unit/E2E pass rate, time/tokens/tool calls, bugs found, inadvertent file edits, and cost.
- Ensure skill lifecycle follows **user permission constraints** rather than overriding explicit “no restart/deletion/install” requirements.
- Require review and a genuine exit condition for long-running agents; don't let subagents run indefinitely or mass-commit untested changes.
- Source README describes optional remote visual-companion logo telemetry; review privacy controls (`SUPERPOWERS_DISABLE_TELEMETRY`) if that feature is used.
- Combine **[125 — Five Whys](125-FORCED-CONNECTION-AND-FIVE-WHYS-PRACTICAL-PLAYBOOK.md)** for root causes and **[139 — Cost Forecast Calibration](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md)** for bounded task budgets and feedback.

## Relationship to Universal-Rules and Instagram-Dump

Do not install Superpowers globally or copy its skill logic into the Universal-Rules repository merely because it is catalogued here. When the user moves from research to building, a **separate, explicit** approval can pick an appropriate pinned version, target project and review procedure.

**Status:** canonical GitHub and platform workflows verified. No plugin installed, scripts run, permissions changed, telemetry configured or unrelated repository modified.
