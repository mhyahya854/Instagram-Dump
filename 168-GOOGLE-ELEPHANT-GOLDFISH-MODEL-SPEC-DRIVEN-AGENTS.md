# 168 — Google Elephant-Goldfish Model (EGM): spec-driven development with context-rich design and isolated review

**Date researched:** 2026-10-27  
**Source type:** NEW DIRECTLY TYPED USER RESEARCH LEAD (not an Instagram screenshot).  
**Original user wording:** “google has a github repo called the elephant goldfish model add that and what is its use”  
**Exact canonical repository:** https://github.com/google/elephant-goldfish-model  
**Official project site:** https://egm.dev/  
**Google Open Source announcement (2026-10-22):** https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html  
**Independent GitHub verification:** Live GitHub repository metadata and README, getting-started guide, harness integration, architecture and test record read on 2026-10-27. Canonical owner \`google\`, repo \`elephant-goldfish-model\`, default branch \`main\`, not archived, declared repository license **Apache-2.0**. The inspected current upstream head was \`b3a35956759bf7f024af2ff061b2e0b44b438e4c\` (point-in-time reference, not an installation pin).  
**No installation, subagent run, source modification or benchmark was performed.**

## 1. What is it, precisely?

Despite its name, **Elephant-Goldfish Model is NOT a separate trained language model or downloadable neural-network checkpoint.** It is Google's published **open-source agent plugin, skill collection, reviewer-prompt framework and engineering methodology** for **specification-driven development (SDD)**. It is designed to improve what AI coding agents build by surfacing missing requirements and contradictions **before implementation**.

Google says EGM was initially developed inside Google and used by its engineers. This is Google's own statement, not a user-run independent evaluation. The repository says the project is **not an officially supported Google product**. The Apache-2.0 repository license is not a guarantee that every external dependency, model, third-party design asset or installation workflow has the same license.

**What it does not do:** does not train or fine-tune an LLM; does not by itself give an agent flawless memory; does not replace a full SDLC, test suite, threat model, formal verification or human judgment; does not promise zero bugs; and does not automatically lower token cost.

## 2. Why “Elephant” and “Goldfish”?

| Role | Input / mental model | Work produced | Main failure avoided | New risks |
|---|---|---|---|---|
| **Elephant** (deep context) | Existing codebase, product goals, user journeys, earlier decisions, architecture constraints, relevant documentation | Feature concept brief and detailed living design specification | Premature coding with unstated assumptions; forgotten architecture and contradictory requirements | Context overload, inaccurate remembered facts, anchoring and unnecessary complexity |
| **Goldfish** (fresh isolated review) | **Approved draft specification plus referenced source material** and review rubric, but **NOT the Elephant's earlier conversational history** | Independent comprehension check, architectural critique, edge-case findings and implementation-readiness report | Reviewer “knowing what the author meant” despite it never being written into the document; self-confirmation in one chat context | Same model can share biases; reviewers can invent findings; subagent compute/tool fan-out |
| **Human engineer** | Business context, trade-offs, risk tolerance, evidence and Goldfish objections | Final decision; accept/reject findings; PR approval; implementation authorization | Automated feedback becoming an unquestionable authority | Bottlenecks and rubber-stamp approvals |

**Important precision:** “Zero-context” is *relative to the previous conversational context*, **not** literal absence of information. Goldfish reviewers must have the design document, relevant source code and standards to perform a useful review. Opening a new in-thread paragraph or telling the same chat to “pretend to forget” is not equivalent to an actually isolated session.

Google's stated design principle: **design before code** for ambiguous/large features. For a tiny, well-bounded bug fix, the upstream getting-started guide explicitly advises using a lighter workflow.

## 3. End-to-end operating model

~~~text
User proposes feature
  ↓
Elephant: interview, dependencies, trade-offs, boundary assumptions
  ↓
egm-brainstorm: structured concepts_brief.md + idea stress test
  ↓
egm-draft: versioned design specification, e.g. docs/designs/feature.md
  ↓
egm-review: fresh Goldfish reviewer session(s)
    1. Zoom out — avoid overengineering; reuse existing code
    2. Comprehension — can an uninformed reader reconstruct the intent?
    3. Critic — scaling, security, edge cases, missing failure states
    4. Implementation readiness — paths, interfaces, tests, migrations
  ↓
egm-resolve: examine findings, accept/reject, revise spec
  ↓
Human/peer review approves specification (pull request)
  ↓
Coding agent implements against the approved artifact
  ↓
Unit/integration/e2e/security tests + source review
  ↓
egm-drift-report: check changed code versus living specifications
~~~

The Goldfish reviewer pipeline is intended to expose what was never explicitly written into the spec, not guarantee that the spec is correct. Architecture decisions remain with the human, and implementation testing still matters.

### Skills and what they are for

| Official skill | Actual purpose | Typical inputs / output |
|---|---|---|
| \`/egm-brainstorm\` | Clarify feature boundaries, argue alternatives, stress-test an idea; upstream describes multiple reviewer lenses | Loose proposal → structured concept brief |
| \`/egm-draft\` | Create a detailed design document section-by-section | Brief and repo context → Markdown spec, e.g. \`docs/designs/<feature>.md\` |
| \`/egm-review\` | Run staged design validation using fresh reviewer sessions | Spec + source → comprehension, critique, readiness findings |
| \`/egm-review-loop\` | Dispatch/synthesize reviewer agents, including hierarchical paths when host supports them | Review subjobs and reviewer outputs |
| \`/egm-resolve\` | Triage review comments and apply approved changes to design | Findings → reconciled spec and decisions |
| \`/egm-bootstrap\` | Generate hierarchical documentation to help understand existing codebases | Code directory tree → leaf/parent/root README summaries for human review |
| \`/egm-drift-report\` | Compare live implementation against checked-in design docs for divergence | Specs + code → drift candidate report |

**Nuance:** upstream docs variously refer to a \`design_draft.md\` interim artifact and a final \`docs/designs/<feature>.md\` path; do not hard-code one path without checking the active skill and returned artifact location. “Drift” is a candidate mismatch and needs human diagnosis; docs can be intentionally updated and code can evolve legitimately.

## 4. Practical example: implementing passwordless sign-in safely

**Goal:** Add passkey login to an existing application without corrupting existing email login/recovery.

**Elephant investigation:** Who can enroll credentials? Are users on mobile/desktop? Which authentication provider and cookies are currently in use? What is the recovery mechanism? Must an account have multiple passkeys? How is lost-device handling audited? Define CSRF, rate limits, cross-tenant authorization, recovery, migration and feature-flag rollout in the specification.

**Goldfish review:** An isolated reader must explain the flow from the design alone. The skeptical reviewer asks: “Can an attacker replace a victim's passkey during recovery? What happens with a partially enrolled credential? Are API routes protected on the server? How do users log in without passkey support? Are session cookies valid after reauthentication?” The readiness reviewer checks endpoint contracts, schema migration, rollback and negative tests.

**Implementation:** Only after review, a coding agent implements the approved spec on an authorized branch, with test results and code review. An EGM review does not prove the app secure.

A second appropriate use is a feature spanning frontend, API, migrations, third-party services and operations where inconsistent agent assumptions can produce expensive rework.

## 5. Setup and integrations (documentation only — DO NOT auto-run)

From the official [harness guide](https://github.com/google/elephant-goldfish-model/blob/main/docs/harnesses.md):

| Environment | Supported entry point as documented | Limitations |
|---|---|---|
| Google Antigravity | \`agy plugin install https://github.com/google/elephant-goldfish-model\` | Requires the relevant plugin/subagent facilities |
| Claude Code | \`claude plugin marketplace add google/elephant-goldfish-model\` then \`claude plugin install egm@egm\` | Different command namespace: \`/egm:egm-brainstorm\` rather than bare \`/egm-brainstorm\` |
| OpenAI Codex | \`codex plugin marketplace add google/elephant-goldfish-model\` then \`codex plugin add egm@egm\` | Must discover available native spawn/wait tools and validate fresh-context sessions |
| Claude Cowork | Plugin marketplace import per upstream guide | Cloud trace verification still incomplete in upstream testing record |
| ChatGPT Work | Personal upload or workspace marketplace import, according to upstream docs | *Not all ChatGPT modes* offer isolated native subagents; upstream cites an open verification gap and instructs stopping instead of pretending to isolate |

**Critical installation detail:** install the **whole** package, not only \`skills/\`. It depends on \`agents/\` reviewer personas and \`resources/document_standards/\` files at runtime. As with any agent plugin, inspect every manifest, prompt, bundled script, hook and permissions before using it on private source code. These installation commands are **source references**, not commands run or endorsed for unconditional installation.

**Platform compatibility:** workflow is a set of agent skill files, so the main determinant is the AI agent harness and its subagent ability rather than Windows vs macOS vs Linux. Browser/desktop-specific installation and CLI runtime details depend on the chosen host; this archive has not validated them across operating systems.

**Official upstream source files:**
- [README](https://github.com/google/elephant-goldfish-model)
- [Setup / workflows](https://github.com/google/elephant-goldfish-model/blob/main/docs/getting_started.md)
- [Harness matrix, installation and limitations](https://github.com/google/elephant-goldfish-model/blob/main/docs/harnesses.md)
- [EGM architecture specification](https://github.com/google/elephant-goldfish-model/blob/main/docs/designs/architecture.md)
- [Testing record and scope](https://github.com/google/elephant-goldfish-model/blob/main/TESTING.md)
- [Google's announcement and original rationale](https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-plugin.html)

## 6. Architecture and technical mechanism

The upstream plugin separates **four layers**:

1. **Skills** — Markdown-based task procedures and orchestrators; the skills decide what to ask, which artifact to write, and when to request review.
2. **Personas** — reviewer prompt files in \`agents/\` (e.g., naive reader, architecture/technical critic, code auditor), ideally each operating inside separately spawned context.
3. **Document standards** — explicit rubrics in \`resources/document_standards/\` rather than vague “make it good” prompts.
4. **Living documentation** — checked-in specs and optionally \`egm-bootstrap\` documentation, which connect implementation back to intent.

Reviewer fan-out can increase the number of model inference calls. The orchestrator collects findings, deduplicates repeated criticisms, and enables interactive human triage. The plugin does not supply a novel pre-trained “Elephant” or “Goldfish” model; it relies on whichever compatible LLM/harness is configured.

**Cost / reliability evaluation design:** Measure extra input+output tokens, independent model calls, retrieval bytes, wall-clock duration, spec review findings adjudicated true/false, implementation rework, escaped defects and maintenance drift. Compare EGM to normal spec-first and Superpowers workflows on **matched tasks** with stable acceptance tests. Do not claim that isolated critics automatically make implementations unbiased or error-free. No benchmark results exist in this research note.

## 7. Strengths, limitations and operational security

**Why use it:** (1) Turns vague product intent into durable, revisable documentation; (2) adversarially challenges specs before code is generated; (3) checks whether a reader without prior chat can understand the feature; (4) connects implementation drift to explicit architectural decisions; (5) offers cross-agent portability within tested harnesses.

**Where not to use it:** trivial changes or already-complete, mechanically verified requirements; contexts with no reliable subagent isolation; work where reviewer cost outweighs expected rework; environments where code/context cannot leave a trusted boundary without approval.

**Risks:**
- **False reviewer independence:** separate sessions still share training biases and may receive contaminated source documents. Prompt-injected repository README or malicious reviewer text must be treated as untrusted.
- **Review theater:** many opinions ≠ truth. Triage findings by source line, reproducible test, severity, exploitability and implementation scope; false positives get rejected.
- **Privacy:** code, architecture, PII and customer secrets may be sent to the chosen underlying AI model/provider, depending on configuration. The repository being open source does not mean local processing or privacy.
- **Execution:** reviewer personas should be read-only; never let a critique skill silently rewrite production code or access unrelated repositories.
- **Costs:** extra model calls and artifact tokens can exceed implementation savings. Forecast before use, measure afterward, put hard budgets and stop conditions in place.
- **Release risk:** an accepted spec is not a deployed or verified change; still require QA, auth checks, threat modeling, accessibility and rollback plans.

**License:** Upstream repo declares Apache-2.0. Confirm current \`LICENSE\`, plugin manifest, per-component attribution and dependencies before distribution or embedding. Google branding/trademarks and third-party content are distinct from code licensing. The framework is free to read as source code, but LLM inference and tools may cost money.

## 8. Relationship to other Instagram-Dump knowledge

- [137 — Superpowers](137-SUPERPOWERS-SKILL-CLAUDE-CODE-CODEX-AGENT-PLANNING.md): both encourage disciplined software design and checkpoints. EGM's distinctive element is the **Elephant with history / truly fresh Goldfish reviewer** separation, plus explicit review phases and drift checks. The two are complementary but duplicative if both create contradictory workflows.
- [138 — PRD and ARCHITECTURE contracts](138-PRD-ARCHITECTURE-SEPARATE-SPEC-DOC-CONTRACT.md): EGM's \`docs/designs/FEATURE.md\` is a feature-level specification; it should **reference** overarching requirements and architecture rather than replace agreed business goals or architectural decisions.
- [139 — Cost forecast and calibration](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md): measure the added “Goldfish swarm” costs and actual downstream defect reduction before calling EGM a savings strategy.
- [127 — Agent skills governance](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md): review any installed prompt skills and bound the host permissions; source files are untrusted inputs.
- [145 — Forty Claude repos](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md) and [164 — verified owners](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md): EGM is a separate new research lead, not silently inserted into the original screenshot's exact forty labels.
- [46 — Prompt injection](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md): the review agent must not obey arbitrary instructions embedded inside retrieved specs/source.

## 9. Source claims vs independent checks / unresolved

| Claim | Evidence class | Conclusion |
|---|---|---|
| “Google has an Elephant-Goldfish Model repo” | **Direct live GitHub metadata** | Confirmed \`google/elephant-goldfish-model\` |
| “It is a trained AI model” | Name could imply this, but **contradicted by README and code/doc layout** | False: methodology/plugin/agent skill suite |
| “Developed at Google and used by thousands of Google engineers” | **Google Open Source Blog and README** | Vendor-reported claim; not independently audited |
| “Plugin supports Codex and other harnesses” | **Official harness docs and upstream testing record** | Installation and fixture tests claimed for Antigravity, Claude Code, Codex; Cowork/ChatGPT cloud traces have open gaps |
| “Zero-context reviewers avoid bias” | **Architectural goal, not an objective guarantee** | Context isolation may catch unstated assumptions but cannot eliminate shared model bias |
| “Reduces AI coding defects/cost” | **Aspirational engineering hypothesis** | No comparative task benchmark or user project measurement performed here |
| “Is automatically enabled in the user's coding tools” | **Not checked or authorized** | No installation/change made; availability depends on environment |

**Source register entry:** \`IGD-TYPED-2026-10-27-EGM\` → this file, [README](README.md) link, [137](137-SUPERPOWERS-SKILL-CLAUDE-CODE-CODEX-AGENT-PLANNING.md) and [138](138-PRD-ARCHITECTURE-SEPARATE-SPEC-DOC-CONTRACT.md) cross-references. Original input was user-typed text and official public URLs, **not uploaded media**.
