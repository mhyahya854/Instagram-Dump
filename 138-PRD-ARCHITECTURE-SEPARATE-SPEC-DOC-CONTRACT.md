# 138 — PRD.md + ARCHITECTURE.md: Screenshot-Sourced Two-Document Planning Contract

**Source:** image 10 in sixteenth Instagram batch. It shows side-by-side file headings **`PRD.md`** and **`ARCHITECTURE.md`** with short bullets, not a full specification.

### Exact screenshot text

```text
PRD.md
■ WHAT YOU'RE BUILDING
■ WHO IT'S FOR

ARCHITECTURE.md
■ THE STACK
■ THE DATA MODELS
```

The bullet colors are blue (PRD) and yellow (architecture). Cropping means **no other list items or text can be inferred** from this frame.

## How to expand this idea into a correct software workflow

### `PRD.md` — problem, user, product

- Problem and measurable desired outcome: why product needs to exist.
- Target user(s), primary jobs-to-be-done, use cases, **explicit non-goals**.
- User journey map, screens/states, rules, permissions, accessibility and responsive acceptance criteria.
- Prioritization and constraints: must-have vs optional; integration boundaries, budget, privacy/data retention and launch metrics.
- Evidence: reference to interviews, screenshots, owned design assets and uncertainties; avoid fabricated user stats.
- “Done” contract: user-visible flows and negative/failure states that automated and manual tests can verify.

### `ARCHITECTURE.md` — implementation reality

- Approved stack/runtime versions and repository/environment topology.
- Data model entities, fields, ownership, relationships, migrations and rollback/restore strategy.
- AuthN/AuthZ matrix, secrets, external API call boundaries, key rotation and audit logs.
- Client/server/mobile architecture, state sync/cache, concurrency and idempotency.
- CI/CD and environments, deployment, backups, disaster recovery, monitoring/alerts, cost model.
- Decisions and rationale (ADRs): why technologies chosen and what would justify revisiting.

### Cross-document agreement gate

```text
PRD requirement → Architecture mapping → Code owner/file → Test(s) → Release evidence
```

Example: “User can delete only their own private location note” → DB row-level ownership + API auth check + deletion lifecycle + E2E negative test + restore/purge semantics.

## Keep two docs separate

Don't stuff architecture into PRD or design aspirations into technical contracts; interlink both, use versioned change proposals and resolve inconsistency with stakeholder approval before touching production.

## Agent prompt skeleton

> Read PRD.md and ARCHITECTURE.md before changes. If requirements conflict, list conflicts with source references and do not invent a resolution. Implement the smallest approved vertical slice on a branch. Confirm unit, integration and UI acceptance tests and show true results. Never modify protected paths or perform destructive operations without explicit user authorization.

**Status:** screenshot transcribed, independent authoring framework provided; no project created or specifications generated in another repository. Related [124 — Three Docs and Execution](124-COST-CONSCIOUS-STACK-GSD-ROO-RALPH-CODERABBIT-LINKEDIN.md), [137 — Superpowers](137-SUPERPOWERS-SKILL-CLAUDE-CODE-CODEX-AGENT-PLANNING.md).


### Complementary implementation — Elephant-Goldfish specification reviews

[168 — Google Elephant-Goldfish Model](168-GOOGLE-ELEPHANT-GOLDFISH-MODEL-SPEC-DRIVEN-AGENTS.md) can produce a **feature-level living design spec** that references `PRD.md` and `ARCHITECTURE.md` rather than replacing either. The Elephant reads project context and drafts, the isolated Goldfish reviewers check what the spec leaves unexplained, and human approval precedes changes. Check architecture drift separately; no spec generation was executed for this archive.
