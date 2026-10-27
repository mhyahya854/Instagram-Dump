# 173 — Fleetbase, Pullfrog and Dagu: logistics platform, GitHub bot, workflow scheduler

**Typed source:** “Fleetbase, Pullfrog, Dagu” (2026-10-27). All three upstream GitHub repositories and declared license IDs were verified through the connected GitHub integration on 2026-10-27. Sources describe software projects; no deployments, CI changes or credentials were used.

## 1. Fleetbase

**Upstream:** https://github.com/fleetbase/fleetbase ; specialized modules: https://github.com/fleetbase/core-api , https://github.com/fleetbase/fleetops . **GitHub repository license:** AGPL-3.0.

Fleetbase is a modular **Logistics and Supply Chain Operating System (LSOS)**. Typical domains: fleet and vehicle/driver records, delivery jobs/dispatch, tracking, operational dashboards, order status and location-centric logistics workflows. It may be used by last-mile delivery operations, courier management or logistics-as-a-service. The brand's various repositories offer separate modules; do not assume every module is within the monorepo or licensed identically.

**Architecture to inspect:** backend API/services, authenticated control console, maps/geolocation providers, database/queues, location event ingestion, mobile driver apps and customer tracking interfaces. GPS data is highly sensitive: document driver consent, retention/deletion, tenant boundaries, role-based dispatch permissions and breach response. Test offline mobile reconciliation, idempotent shipment state transitions, delayed position updates, map outages and rate/cost of geocoding.

**Self-hosting concerns:** database backup, upgrades/migrations, map API fees, mobile compatibility, push notifications and local delivery regulations. **AGPL-3.0** can impose corresponding-source duties for modified AGPL-covered program offered over a network; seek appropriate legal review for proprietary extensions and redistribution. “Open source” is not “free-to-operate production logistics.”

## 2. Pullfrog

**Upstream:** https://github.com/pullfrog/pullfrog ; GitHub App listing https://github.com/apps/pullfrog ; **repo license:** MIT.

An **open-source GitHub automation bot** that routes issues, pull requests, code-review comments, CI failure events and maintenance actions to coding agents. It uses GitHub Actions plus your selected agent/model credentials (BYOK / supported subscriptions where allowed), rather than being a standalone frontier language model. README describes integrations with Claude Code, Codex and OpenCode; review exact current capabilities before adopting.

**Example pipeline:** PR opened → GitHub webhook/Action event → least-privileged agent receives diff, issue and test context → generates suggestions on branch → CI verifies → human reviews → authorized merge. Other flows can summarize issues, triage labels, propose fix PRs, respond to human comments or attempt CI repairs.

**High-risk failure modes:** untrusted PR descriptions/comments are prompt-injection vectors; bot token scopes can expose private repository or perform unwanted writes; Actions secrets may leak through logs/commands; CI auto-retry loops burn tokens and trigger cascading changes. Require protected branches, read-only-by-default planning, job concurrency limits, author/actor allowlist, scoped credentials, budget caps, explicit human merge authorization and auditable review evidence. Run only on a toy repository first. A free personal/open-source plan is not a guarantee of unlimited inference cost.

## 3. Dagu

**Upstream:** https://github.com/dagucloud/dagu ; **repo license:** GPL-3.0 according to live GitHub metadata.

Dagu is a **self-hosted workflow/job orchestrator** emphasizing human-readable, declarative YAML definitions of dependencies and command/script/container steps, a web UI and local operational simplicity. It can coordinate extraction, build pipelines, database housekeeping, scheduled tasks, ETL and controlled agent tooling. The repository describes a single binary and no mandatory external database for its basic deployment style; consult current docs before choosing HA/durable workloads.

**Conceptual workflow definition** (illustration — verify syntax in pinned Dagu docs before deployment):

~~~yaml
# Illustrative job graph, not a tested Dagu config
steps:
  - name: extract
    command: "python extract.py"
  - name: validate
    command: "python validate.py"
    depends: [extract]
  - name: archive
    command: "python archive.py"
    depends: [validate]
~~~

Security: executed commands run with scheduler privileges; unsafe YAML, secrets in environment/logs, shell injection, network exposure, overlapping schedules, cron timezone/DST behavior, restart semantics and idempotent retry logic matter. Design job state, lock ownership, backoff, cancellation and alerting before relying on it for financial, health or operational systems. Check GPL obligations when distributing derived programs.

## Decision comparisons

- **Fleetbase:** business domain **logistics**; not a generic CI agent or cron replacement.
- **Pullfrog:** **GitHub event-driven coding agent bot**; ideal for authorized repository operations, PR assistance and triage.
- **Dagu:** generic **workflow orchestration**; runs scripts and dependencies, irrespective of whether they use AI.
- **Complementary approach:** Dagu schedules data preparation, GitHub Actions runs Pullfrog on code review, Fleetbase provides an application domain. No product should be silently granted another product's secrets or production permissions.

**Related:** [03 — production architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [28 — automation risk](28-AUTOMATION-TEMPLATES-AGENT-REVIEWS-AND-SAFETY.md), [46 — prompt injection](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md), [139 — token usage forecast](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md). Source descriptions are not proof of reliability, scale or safe deployments.
