# 51 — Candidate Additions for Universal-Rules (RESEARCH / NOT RATIFIED)

Captured 2026-10-25. **This file lives in Instagram-Dump, NOT in Universal-Rules.** The user asked to investigate guides and agent-workflow improvements for Universal-Rules. Their existing ratified repository deserves a separate specification review and explicit merge process. These are **proposed** integrations rather than edits to current agreed rules.

## Source principle

Never convert every viral reel into a mandatory rule. Collect evidence, map each concept to the correct category, check conflicts with existing ratified requirements and decide only then. Avoid redundant instructions competing for attention.

### Proposed topic A — agent task completion evidence

Potential standing policy: every meaningful agent operation has a task contract and acceptance ledger. Requirements are enumerated; verification commands and expected results are defined before code change; claims in reports are traceable to actual output. **Do not declare success for untested work**. A failed or omitted requirement remains visible as partial/blocked.

Suggested sources: Unlazy (https://github.com/Leonxlnx/unlazy), Superpowers (https://github.com/obra/superpowers), Ponytail (https://github.com/DietrichGebert/ponytail), Matt Pocock Skills (https://github.com/mattpocock/skills). Treat tools as optional implementations of the principle, not permanent dependencies.

**Acceptance tests before ratification:** 100% mapping of scoped requirements to outcome evidence; no false completion on missing tests; no unreviewed privileged shell execution; safe shutdown of endless work loops; owner-approved deviations.

### Proposed topic B — skill-only workflow composition

User's dictation: “Focus on a proper workflow for all our projects. This needs to be added only with skills.” Interpretation: expose reusable project workflows as **scoped skills**, rather than filling every global prompt with huge always-on playbooks. Suggested skill groups:

- Discovery / brief / requirements / acceptance
- Architecture and data security
- Design/UX reference analysis
- Implementation, focused changes and code review
- Verification: tests, accessibility, browser/device, performance
- Security: threat model, secrets and permission test
- Deployment: staging, backup, migrations, rollback
- Documentation and handoff

**Rules vs skills:** a small set of immutable universal safeguards remains always-on; detailed how-to workflows are loaded only when relevant. Skills cannot override authorization, user privacy, security or rollback requirements. Require scan and review before adding an untrusted skill.

### Proposed topic C — make apps accessible to AI without weakening them

Provide semantics in accessible UI, versioned APIs/actions, option for MCP integration only where needed. Use same domain service for humans and agents, explicit scopes, confirmations for consequential actions, idempotency and audit. Reference [45](45-AGENT-NAVIGABLE-APP-ARCHITECTURE.md).

### Proposed topic D — untrusted content and prompt-injection gateways

Before the agent consumes external docs/skill files, distinguish task data from orders. Scan or review suspicious hidden text, prevent source-to-tool authority escalation, and preserve original bytes/provenance. No third-party scanner grants a security guarantee. Reference [46](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md).

### Proposed topic E — architecture learning guide, not architecture mandates

Offer a modular on-demand guide for API, backend, DB, cloud, CI/CD, auth, security, rate limiting, caching, monitoring, testing and scaling. Prefer the simplest technically adequate implementation. Reference [50](50-PROGRAMMING-SYSTEM-DESIGN-GUIDES-FREE-LLM-APIS.md). No automatic requirement for Spring Boot, AWS, Kubernetes or one vendor.

### Proposed topic F — additional visual style labels (REFERENCE ONLY)

Candidates not already recorded: claymorphism, neo-futurism, flat design, Material Design, pop art, industrial, aurora, real-object UI and soft-surface variants. Keep them in the design vocabulary alongside brutalism, bento, Swiss, pixel, glass, cyberpunk, Y2K and skeuomorphism; **do not activate automatically**.

### Proposed topic G — safer SEO/marketing guidance

Avoid unverifiable results (“number 1 by Friday”, invented client numbers or Forbes backlinks). Demand real product proof, measurable site checks and honest public claims. Reference [48](48-AI-DESIGN-VIDEO-SEO-MARKETING-REFERENCES.md).

## Workflow for adopting these candidates

1. Compare proposals against current Universal-Rules main, design-rulebook integration branch and previously ratified Topic 2 policies.
2. Deduplicate existing requirements rather than append overlapping contradictory lines.
3. Mark each item “already covered”, “new candidate”, “conflict” or “needs user decision.”
4. Draft a branch diff and run tests/docs link checks.
5. Seek approval to merge into main **before** changing previously ratified rules.
6. Never silently install the external skills to “enforce” a rule. Use a separate permissions/installation review.

## What has NOT happened

No file in Universal-Rules was changed as part of this collection; no new software tool or agent skill was installed. The exact dictation “two universal rules” did **not** identify the two rules precisely; A and B above are candidate interpretations, not ratified decisions.
