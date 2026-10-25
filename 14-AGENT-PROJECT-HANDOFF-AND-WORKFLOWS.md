# Reel Notes 14 — Engineering Handoff Before Telling an Agent to Build

_Captured 2026-10-25. Applies to AI coding agents, contractors, multi-agent teams and project specifications._

## Reel example: “Claude, build me a golf app. Make no mistakes.”

“Golf app” is only a category, not a specification. The reel's five anchors are **goal, user, features/flows, stack, boundaries**; add measurable acceptance evidence so the agent knows when it is done.

### A complete but concise handoff

| Field | Questions to settle | Example from the reel, clarified |
| --- | --- | --- |
| Goal | What outcome and success measure? | Help weekend golfers reduce handicap through actionable tracking |
| User | For whom, on which platform and under what circumstances? | Weekend players, novice/intermediate, often outside with limited connection |
| Core flows | What are the top jobs and their end-to-end behavior? | Record score → save round → review trend; optional tee times/swing later |
| Feature priority | Must-have vs later, explicit exclusions | Score tracking as MVP; tee time integration requires separate permissions/sources |
| Stack | Frontend/backend/database/hosting and existing code/tools? | Don't silently replace the project's chosen framework |
| Boundaries | Which files, environments, accounts, secrets, modules can change? | No production migration, paid API signup or live deployment without approval |
| Acceptance/done | Which tests, screenshots, QA and outputs demonstrate completion? | New score saved; reload persists; invalid score rejected; mobile flow works |
| Privacy/security | Sensitive personal data, permissions, session/access controls? | Each golfer reads/writes only their own rounds; export/delete requirements |
| Recovery | Backups, rollback compatibility, feature flag, risk mitigation? | Preserve existing data and ability to recover after migration |

The reel suggests “set boundaries first” before writing. Capture **decisions already made** (naming, design language, tech stack, module ownership, rejected approaches) so agents don't re-open them without reason.

## Agent-ready handoff template

~~~markdown
# Project handoff

Goal and success metric:
Target audience and main use cases:
Current state / existing repository / chosen stack:
Must-have flows with inputs and outputs:
Not in scope:
Design references and UX anti-patterns:
Data model and access-control matrix:
Environment boundaries (local, staging, production):
Files/services that MAY be changed:
Files/services that MUST NOT be changed:
Allowed tool actions vs actions requiring approval:
Definition of done and acceptance tests:
Expected artifacts (diff, test results, screenshots, migration plan):
Risks and recovery strategy:
Open unknowns (do not guess silently):
~~~

### Engineering workflow to consider

1. Inspect codebase, available docs, relevant branch, tests, deployment environment.
2. Restate planned scope and invariants; identify ambiguous essential dependencies before coding.
3. Implement smallest coherent change, with no unrelated rewrites.
4. Add/update tests for success, failure, security and concurrency where relevant.
5. Run build, lint, relevant tests, production-like tests and actual browser checks.
6. Describe exactly what changed, what passed, what failed and evidence. Do not invent test outputs.
7. For database or production work, pause on destructive actions for explicit authorization, not just a vague “go ahead.”

## GitHub agent workflow repositories (verified)

| Repo | Function | Use case |
| --- | --- | --- |
| https://github.com/garrytan/gstack | Opinionated workflows and review/QA | Product plan, engineering review and release verification |
| https://github.com/eyaltoledano/claude-task-master | Task breakdown and dependencies | Longer project tracking |
| https://github.com/oraios/serena | Semantic codebase understanding | Targeted changes to existing source trees |
| https://github.com/obra/superpowers | Brainstorming, TDD and agent workflows | Reliable small-step implementation |
| https://github.com/DietrichGebert/ponytail | Low-complexity focused edits | Prevent unnecessary abstraction and broad rewrites |
| https://github.com/mattpocock/skills | Specifications, debugging and code-quality skills | Improve plan and review rigor |
| https://github.com/msitarzewski/agency-agents | Role-specific agent personas | Assign narrowly scoped design/backend/security/marketing tasks |

**Important:** Using multiple agents doesn't substitute for a responsible reviewer; an agent that reviews its own work is not independent security evidence.

## Rules for future offline synthesis

Keep the project-specific handoff file alongside the source rulebook. When consolidating into a giant knowledge document, separate *standing rules*, *project-specific decisions*, *workflow templates*, *reference examples*, and *uncertain source transcripts*. Offline completeness depends on clear definitions and examples, not repo names alone.
