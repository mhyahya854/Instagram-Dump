# 172 — Multica, LangWatch and Orca: agent collaboration, evaluation and the name collision

**Typed source:** original list “multica, Langwatch, Orca” (2026-10-27), without URLs. Live repository API checks on 2026-10-27 verify the candidates below, but **do not prove which Orca the user intended**. This document distinguishes upstream features from untested promotional claims.

## 1. Multica — open-source human + AI team coordination

**Upstream:** https://github.com/multica-ai/multica ; **exact identity verified by GitHub API:** \`multica-ai/multica\`, not archived, actively updated in the checked snapshot. **License API identifier:** \`NOASSERTION\` — review LICENSE and component-specific terms; don't claim MIT solely from a README or vendor phrasing.

Multica positions itself as a **self-hostable space where people collaborate with agent teammates**. Its relevant value is organizing task ownership, messages/agents, shared context, approvals and artifact handoffs across humans and automations; compare with separate task-graph systems such as [beads](https://github.com/steveyegge/beads), parallel-agent coordination tools and traditional ticketing. Self-hostability does not mean zero hosting cost, completely local LLM inference or a verified privacy guarantee.

**Research/adoption:** inspect documented container/services and deployment diagrams, SSO/roles, credential vault, audit trail, per-agent permissions, context retention/deletion, tenant isolation, backups, network endpoints and cloud inference. Test escalation scenarios where an untrusted agent submits an external URL or tries to assume a higher-trust role. Use one small, reversible proof of concept. Avoid mixing up the distinct repo \`multica-ai/andrej-karpathy-skills\` with the Multica app.

## 2. LangWatch — agent observability, evaluation and governance

**Upstream:** https://github.com/langwatch/langwatch ; **GitHub API:** Apache-2.0 repository license; current description: open-source agent observability & evals, tracing/testing/routing/governance for AI platform teams.

**What it actually addresses:** LLM traces/spans, model/tool-call logs, prompt variants, evaluation datasets, performance and failure analysis, workflow monitoring and regression detection. Instrument applications in a bounded manner using supported APIs/SDKs and OpenTelemetry integration when available, then correlate traces with task IDs and acceptance-test outcomes. It is an observability/evaluation application, **not itself an LLM or a code-writing agent**.

**Useful for the existing agent cost objective:** collect input/output/cached tokens, reported charges versus estimates, tool count, errors/retries, context length, time to first token, tail latency, evaluator correctness and privacy risk. Compare against the requested forecast-vs-actual self-correction loop in [139](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md) and the existing [148](148-CONTEXT-MEMORY-TOKEN-BURN-CUT-AGENT-TOOL-MATRIX.md). Use synthetically generated traces before connecting production data.

**Limits:** a vendor dashboard cannot make wrong or invented telemetry true; LLM-as-judge results need human calibration. Sensitive prompt content, API keys and documents must be redacted, access-controlled and retained only as needed. Understand hosted pricing vs self-host ops costs, runtime overhead, versioned metrics, license in each distribution and data-export portability.

## 3. “Orca” — several different active GitHub projects

| Name and canonical upstream | What it is | Concrete security/engineering tradeoff |
|---|---|---|
| [stablyai/orca](https://github.com/stablyai/orca) and https://www.onorca.dev/ | Desktop **agent IDE/parallel coding agents**; worktrees and mobile companion for Claude/Codex/etc, bringing your own subscription | Git worktree isolation is not OS/container sandboxing; mobile pairing, repo access, agents' shell permissions and telemetry |
| [orca-ae organization](https://github.com/orca-ae) / https://www.runorca.ai/ | **Orca Agent Engine**, StreamNative-sponsored managed agent runtime and AI gateway with Anthropic-compatible interface and budgets; developer preview | Model credentials/gateway policy, event logs, trust boundaries, explicit preview limitations |
| [Nethyric/orca](https://github.com/Nethyric/orca) | Another desktop autonomous agent, providers/MCP support and local system tools | Broad file/process/browser permissions; validate signed builds, tool safety and credential management |
| [orcaagent.dev](https://orcaagent.dev/) | Separate DeepSeek-focused Rust terminal coding-agent product | Different project; upstream repository owner not established from this source-only identity |

**Most plausible for the user's agent-workflow archive:** \`stablyai/orca\` given surrounding GitHub agents. **But the exact source remains unresolved** because no link or screenshot was supplied. Never silently merge these products. Do not claim any of the competing Orca codebases are subsidiaries/forks of each other without primary evidence.

## Compare the three named choices

| Need | Best-fit product (provisional) | Why |
|---|---|---|
| Humans and multiple AI agents sharing a workspace | Multica | Team handoffs, collaborative work management |
| Measure traces, agent quality and cost | LangWatch | Observability + evaluation pipeline |
| Several coding agents working in independent worktrees | stablyai Orca | Local orchestration IDE with parallel sessions |
| Externally governed agent runtime and model gateway | Orca Agent Engine, **different product** | Agent execution control plane |

**Do not install or activate any agents automatically.** Evaluate versions, actual permissions, installation scripts, licensing, network transmission, restore tests and acceptance metrics. This archive records investigated upstream identities, not installed tools.
