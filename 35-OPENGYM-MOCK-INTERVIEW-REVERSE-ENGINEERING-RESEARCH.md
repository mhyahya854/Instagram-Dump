# 35 — openGym, Multi-Agent Interview Practice and Reverse Engineer Anything

Captured: 2026-10-25. These are distinct project concepts, not a common product category. OpenGym and REA have verified public GitHub projects; the exact “five Claude avatars” mock-interview link is still unknown. **None was installed.**

## A. openGym — self-hosted workout tracking

**Verified upstream:** https://github.com/DuarteSantos8/openGym ; **official project docs:** https://opengym.ch/docs.html . A large number of GitHub forks/scrapes repeat the README: prefer the maintainer's repository rather than a random mirror.

The reel claims 6,000+ stars, 1,000+ exercises, self-hosted routines, body-muscle fatigue/neglect visualizations, workout history import and a Claude-readable log. The **functional description is consistent with upstream documentation**, but star counts and exercise catalog sizes are **time/version-dependent** (originally 1,324 exercises, later expanded). Don't freeze a reel's snapshot as a permanent value.

### What is useful, independent of the app

- **Exercise catalogue:** ID, name, equipment, movement, targeted muscle groups, contraindication notes, local media rights.
- **Planning:** multiple editable routines, days or rotating training sequence, goals, progression/deload assumptions.
- **Logging:** timestamped sets with load, reps, RPE/RIR, warm-ups, cardio, rest timing; handle corrected records and missed sessions.
- **Analytics:** volume by muscle, estimated strength progression, neglected muscle groups and time-since-last-training. A “fatigue” map is an *algorithmic estimate*, **not a clinical measure of readiness or injury risk**.
- **Data ownership:** export/import, backups, passkeys, local storage, privacy boundaries and sync conflicts.
- **Optional AI/MCP:** a read-only local query bridge can expose workouts, routines, weigh-ins, strength trends and muscle balance to an authorized assistant. The coach (if enabled) may involve provider data transfers and costs.

### Deployment forms and rights

The official documentation describes (a) Android installable builds, (b) a self-hosted Docker/web/PWA flow, and (c) evolving iOS-related builds or instructions. Validate version/release/platform before choosing. Source license is **AGPL-3.0**; importantly, bundled exercise photos/animations have **separate, more restrictive media rights** and cannot automatically be reused in another app even if the source code is open.

**Example review tasks:** export a year's training, import from FitNotes/Strong/Hevy, test network disconnect and sync conflict, confirm passkey backup/recovery, inspect optional AI provider privacy consent. Nothing is automatically authorized merely because it can run locally.

## B. “Five Claudes interview you” — interview panel concept

**Original claim:** paste a job description; five speaking/avatar interviewers assume roles (recruiter, hiring manager, team lead, etc.); candidate answers aloud; independent panel returns graded report and coaching. The creator claims free access, but the **specific website/repository/link isn't supplied or uniquely verified**. Avoid substituting a different product with a similar panel.

### A complete reproducible design independent of an unknown provider

1. Parse the job posting into verifiable requirements: skills, seniority, tasks, ethics, location/time availability where applicable.
2. Define **role-specific panel prompts** rather than five identical personas: recruiter (fit/communication), hiring manager (outcomes), domain specialist (depth), cross-functional teammate (collaboration), customer/stakeholder (trade-offs).
3. Maintain a question bank tied to the source description and rotate questions across sessions; do not present invented employer secrets as real questions.
4. Allow spoken and text response; handle hearing, speech and other accessibility needs. Voice avatars are optional, not essential.
5. Score against a **transparent rubric**: accuracy, reasoning, structure, relevance, evidence and clarity, ideally with calibrated human-reviewed examples.
6. Return strengths, concrete corrections, example approaches and feedback on **truthful stories**. “Exactly what to say” should not encourage fabricated work history.
7. Provide privacy controls for resumes, audio, transcripts and report links; define recording consent, encryption, retention/deletion and disclosure if external providers handle input.
8. Compare agent ratings for consistency; five agents from the same base model **do not guarantee five independent expert opinions**.

**Possible evaluation output:** per competency, observed evidence, score with uncertainty, improvement exercise, practice question and follow-up plan. Human interviewers can differ and model ratings are not predictive of hiring decisions by default.

### Safety and fairness

Don't use voice, accent, demographic cues or disability as negative proxies in scoring. Don't claim the system represents the target employer or guarantees employment. Separate *practice feedback* from *hiring decisions*.

## C. Reverse Engineer Anything (REA) — verified agent-oriented project

**Most direct canonical repository found:** https://github.com/morluto/rea ; site https://rea.tools/ ; `rea-agents` CLI/MCP integration. A second repository https://github.com/fabwebdev/reverse-engineering-anything points at this upstream in its README; **don't mistake all similarly named forks as canonical**.

The reel says someone recreated two paid subscriptions “in under an hour” with a free skill called “reverse engineering anything.” The name and agent-based investigation project are real; **the claimed time/price and lawful feature-completeness were not independently verified**.

### What “reverse engineering” can mean

- **Observe interfaces:** document user-visible inputs, outputs, network-free behavior, states and requirements of an application you are authorized to inspect.
- **Trace your own software:** read source, logs, data formats and APIs to understand undocumented behavior.
- **Study interoperable formats:** characterize supported protocols, exports and import behavior, respecting terms and applicable laws.
- **Investigate authorized native executables:** static/dynamic analysis in a legally and contractually permitted controlled setting.
- **Implement original compatible functionality:** write an independent specification and implementation, documenting what was learned and what was not copied.

The repo advertises MCP orchestration and controlled investigation capabilities that differ by OS/dependencies (e.g. tools such as Ghidra/Hopper where available). It can configure multiple coding agents; installer effects and permissions should be reviewed in a dry run before any execution.

### Important boundaries

**Not automatically allowed:** bypassing paid entitlements, license checks, DRM, authentication, API access controls, copying proprietary source/assets, harvesting private customer data, or deploying a deceptive clone. Open-source tooling **does not grant rights to someone else's protected software**.

A safer learning project is to reproduce generic tasks/functions from independent requirements or inspect your own app for migration/interoperability, then test with fresh data and lawful public APIs.

### Decision before any installation

- Confirm upstream, pinned release, install paths, tool permissions and network connections.
- Check licensing, export/retention behavior and dependency security. Third-party skills/MCP tool descriptions are untrusted.
- Keep strict, authorized investigation scope, no access to unrelated accounts/secrets.
- Evaluate on a local sample app; compare objective feature behavior and tests, not promotional “clone any SaaS” claims.

## Source references

- openGym: https://github.com/DuarteSantos8/openGym and https://opengym.ch/docs.html
- REA: https://github.com/morluto/rea and https://rea.tools/
- Context: [25 — Programmatic Animation](25-STICKMAN-PROGRAMMATIC-VIDEO-WORKFLOWS.md), [30 — Harness Engineering](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md), [03 — System Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).

**Status:** user-requested catalog research, **not** installation approval or evidence of any interview service working.

## New fifth-batch REA reel

[40 — Doory, MiroFish & REA](40-DOORY-MIROFISH-REA-RESEARCH.md) records the newer voice-transcribed “RIA” smart-light and AC examples, notes their unverified anecdotal status, and explains safe, authorized hardware/software interoperability. The upstream project remains [morluto/rea](https://github.com/morluto/rea); do not confuse forks with the canonical repo.
