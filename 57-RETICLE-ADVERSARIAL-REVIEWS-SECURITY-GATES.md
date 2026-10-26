# 57 — Reticle Verification, Adversarial Agent Reviews and PR Security Gates

Captured: 2026-10-26. Two reels describe an agent that breaks old flows when fixing buttons, and a developer whose own application was compromised after AI reported “security looked fine.” The specific hack anecdote is **unverified**, but the verification methods are useful.

## A. Reticle: verify actual app behavior after code changes

**Confirmed source:** https://github.com/reticlehq/reticle ; https://www.reticle.sh/ . The repository describes instrumentation of the running developer application using DOM, network, console, application state and source mapping. It lets agents record and replay meaningful flows, detect when one change breaks another, and issue actual **pass/fail outcomes with evidence**.

### What it adds versus generic Playwright

- **Playwright** (https://github.com/microsoft/playwright) drives browsers and can measure visible and network outcomes. Use it for cross-browser, real rendered pages, keyboard and device emulation.
- **Reticle** integrates deeper into **an app you control**, can watch runtime state and record reusable flows; its published CLI includes setup, try/verify, gate and reporting functions.
- A runtime instrumentation tool is **not security boundary enforcement**; tests can pass while untested attack classes remain. Inspect its SDK, scopes, background service, optional cloud data transfer, telemetry and any account/trial requirements.
- The project advertises open-source local verification; the optional **Harness/cloud exploration** has its own terms, limits and potential costs. Do not conflate the two.

### Example quality gate

| Change | Test before | Test after | Expected proof |
| --- | --- | --- | --- |
| Button no longer responds | reproduce click and observe failed network | press button with real form data | request returns correct response and actual saved state |
| Form fix breaks navigation | navigate full checkout journey | re-run same saved flow | every step completes, no unexpected errors |
| Login UI refresh | valid and invalid credentials | role-specific E2E | only authorized pages/API calls accessible |
| Cart coupon | correct price math under concurrency | replay same request | total correct, no double-charging |

**Do not claim 100% verification coverage** just because Reticle is installed. Include acceptance inventory and explicit not-tested cases.

## B. Multi-agent adversarial security review

The reel recommends writing a security-specific skill, then having **Codex and Claude Code challenge the feature implementation**, followed by Greptile PR review. This is a process proposal, **not a proven penetration test or guarantee the majority of defects are found**.

The original author describes users editing their own metered **usage limits**, a serious business logic/authorization defect. The appropriate rule is: usage limits, billing quota and entitlements must be enforced and protected server-side; the client may display but must not authoritatively change them.

### Role separation

1. **Implementation agent:** explains what changed and the intended data/role invariants.
2. **Adversarial reviewer:** receives threat model and permission matrix; tests realistic **authorized staging fixtures**, including cross-account IDs, editable quotas, stale JWTs, webhook spoofing, race conditions and replay.
3. **Automated scanner/PR reviewer:** inspects diff, dependencies, hardcoded secrets and potentially dangerous patterns; findings are hypotheses requiring validation.
4. **Independent functional tester:** runs actual app interactions and negative integration tests.
5. **Human owner:** approves risk decisions, deployment, exceptions and production changes.

Two LLMs can share blind spots, and expensive thinking settings do not prove security. Never confuse the specific model/version names in a dated reel with guaranteed available configurations.

### Greptile project

**Verified source:** https://github.com/greptileai/skills . Includes PR check/review workflows and a greploop. Greptile https://www.greptile.com/ is a PR/code-review provider; review status “no comments” is not a security certificate. Looping review/fix can introduce regression or consume credits; set bounds and gates.

## C. Recommended reproducible delivery policy

1. **Define tests before code**: success, failure, security, accessibility, performance and user expectations.
2. **Changed-files and dependent-flow map**: test direct feature and any affected old flows.
3. **Static gates**: formatting/lint, types, unit tests, dependency check and secrets exposure.
4. **Runtime gates**: authenticated and unauthenticated API tests, browser replay, role matrix, concurrency where applicable.
5. **Adversarial review**: inspect current permissions/quotas/money flows for non-happy-path behavior.
6. **Report evidence by commit SHA**: commands, results, scenarios, known coverage, screenshots/logs with secrets redacted.
7. **Deployment approval**: only qualified human authorization for production, migrations, purchases or sensitive account actions.
8. **Postdeploy smoke checks and rollback**: maintain recovery time and update alerting.

### Suggested status wording

- **Passed:** exact checked scenario demonstrated a correct observable outcome.
- **Failed:** scenario produced an incorrect outcome, with reproduction.
- **Incomplete:** runner timeout, missing fixture, unavailable account/credentials, inaccessible simulator.
- **Not evaluated:** no test executed.
- **Partial:** subset passed, but required checks remain incomplete. **Never write “all fixed” for partial.**

## Note on ethical testing

Test only owned/authorized assets and avoid exfiltrating actual customer data. For production security, an authenticated permission check is not authorization to run aggressive exploitation or uncontrolled fuzzing.

Related: [14 — Handoff](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md), [44 — Unlazy](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md), [56 — Token/Dependency Security](56-AUTHENTICATION-JWT-REVOCATION-DEPENDENCY-SECURITY.md).
