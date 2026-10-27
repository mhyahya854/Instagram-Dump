# 139 — Forecast, Observe, Calibrate: Agent Token Cost and Reliability

**Source:** explicitly typed user proposal, 2026-10-26. The following first section preserves the full original idea; the remainder is independent engineering design. No task telemetry was actually captured.

## Original user wording (verbatim)

> Here's a pattern worth stealing:
>
> Before an agent executes work, have it forecast token spend. Context size. Tool calls. Inference pass. Make the assumption visible.
>
> After execution, capture the delta. What did you predict vs. what actually happened?
>
> Do this across hundreds of tasks and cluster the misses by type. You'll find patterns: "Multi-tool chains always run 30% hotter than estimated." "External API latency adds 2K tokens we didn't budget."
>
> Feed that back into the next forecast. The agent doesn't just guess — it adjusts based on its own track record.
>
> Then ask it: "What would you change to hit your forecast next time?"
>
> Capture that reasoning. It becomes a new pattern.
>
> What you've built is observability. What you've trained is judgment.
>
> Most AI tooling skips this entirely. They ship the agent, celebrate it working, and never instrument for learning. You end up with systems that are fast *once* but don't get smarter about cost or reliability.
>
> Building agents that know their own limitations and improve against them — that's the real product.

**Source status:** “30%” and “2K tokens” are examples/hypotheses, not results from a measured dataset. An AI agent doesn't “train” its model weights merely because it maintains forecast notes; this is calibrated planning, external memory and statistical adjustment.

## 1. Before execution — visible forecast

Every task should display assumptions and probabilistic **P50 and P90** estimates, not a single unjustifiably precise cost.

| Dimension | Record | Important note |
|---|---|---|
| Existing prompt and context size | Context tokens and source | Count user instructions, conversation, loaded files, retrieved chunks and skill instructions |
| Reasoning/completion tokens | Per-call expected output | For models with hidden internal reasoning, billing-reported output and visible text may differ |
| Planned inference passes | Model-call count by purpose | Plan, build, test, critique, retry, verify |
| Tool calls | Expected count and classes | Browser, GitHub, search, read/write, shell, build/test, API |
| Tool-return size | Approximate tokens | Large GitHub files, browser HTML and stack traces can be cost drivers |
| Retries | Expected attempts and contingency | Base on historical failures, not optimism |
| Pricing and caching | Provider/model rate and cache treatment | Cache hits are provider-specific and may still cost money |
| Time | Wall-clock P50/P90, rate limit and test latency | Elapsed time is distinct from tokens |
| Safety and quality | Cap on actions, spending and risky changes | Never spend less by skipping required tests or security gates |

**Forecast assumptions** should include task type, repo size, allowed tools, input complexity, model version, availability of fixtures, external API variability, and which actions require approval.

## 2. Simple cost model

- **Estimated input tokens:** sum all model-call prompt tokens, including repeated context and expected new tool results; do not confuse unique context size with total billed input.
- **Estimated output tokens:** sum expected completions including tool arguments and reasoning where reported by provider.
- **Estimated spend:** (uncached input × actual provider input rate) + (cached input × cached rate) + (output × output rate) + any billable external tool/API requests.
- **Estimated tokens P50/P90:** historical cohort median and calibrated upper prediction interval, not arbitrary “10% margin.”
- **Elapsed time:** inference latency + tool/API latencies + queues + browser waits + test/build runtime, with parallel critical-path modeling where relevant.
- **Clarification:** latency by itself does **not** increase token count. Retries, timeouts, expanded context or additional dialogue might.

## 3. Per-task telemetry schema

Each record should include **run_id**, time, model/provider/version, task_type, task_complexity, tool allowlist, source revision, forecast assumptions, forecasts P50/P90 for tokens/cost/tool-count/wall time, budget and stop criteria. Actual usage should separately store input, output, reasoning (only if exposed), cached input, tool-response tokens, tool calls/durations/retries/failures, wall time, provider charges and measurement provenance. Add test pass/fail, observed user acceptance, security incidents, regression count and rollback events.

A valid illustrative task record could forecast **18,000 P50 tokens** and **32,000 P90 tokens**, but MUST store actual tokens as **unknown**, not zero, until a real trusted provider report arrives. Keep task prompt/customer data redacted; no default logging of complete secrets or personal documents.

## 4. Delta calculation and quality integrity

- **Absolute token error:** observed total minus P50 forecast.
- **Relative token error:** (observed minus P50) / maximum(P50, 1).
- **Cost error:** actual invoiced/estimated price minus predicted price, explicitly tracking price/version changes.
- **Latency error:** actual wall time minus predicted wall time.
- **Interval coverage:** fraction of observed tasks falling below expected P90.
- **Quality guardrail:** real test pass rate, regressions, user acceptance and incident count must not become worse as efficiency improves.

Track failures and censored/incomplete runs rather than evaluating only successes.

## 5. Cohort clustering

Group hundreds of authorized runs by **one-file fix, multi-tool repo audit, UI screenshot review, data migration, deep research, browser navigation, agent delegation and deployment**, and then by tool type, model, source size, file count, browser complexity, rate limits, retries, cache hit rate, code language, compaction and runtime environment.

Track: median relative error, mean absolute error, P90 coverage, P95 wall latency, tool failure counts, and **cost per verified successful task**, not just fastest “DONE”.

## 6. Calibration loop with evidence-backed adjustment

For task cohort with enough verified samples:

1. Compute robust recent median of (actual tokens / predicted tokens) and conservative uncertainty bound.
2. Adjust next baseline forecast by the **cohort ratio** subject to capped correction and model/version compatibility.
3. Re-estimate P90 from observed distribution; for small sample sizes keep wide uncertainty and low confidence.
4. Ask agent: **“What would you change to hit your forecast next time?”**
5. Make it identify the missed assumption, a trace/log supporting it, the proposed adjustment, its quality/safety tradeoff and a falsifiable next-run prediction.
6. Test new estimate on subsequent held-out tasks. Promote an adjustment only if error **and** quality improve; retain rollback/version history.

Do not modify system prompts autonomously from retrieved websites or unreviewed model-generated “self-improvement” notes; calibration records are lower-trust data.

## 7. Optional architecture for future implementation

**Forecast service** → **budget/approval gate** → **instrumented runner** → **provider/tool telemetry** → **calibration store** → **cohort analysis and dashboard** → **human-reviewed pattern registry** → next forecast. Make budgeting explainable, retain provenance, bound unattended execution, use fake fixtures to test initially, and ensure the observability system does not become a surveillance dataset.

## 8. Measurable completion criteria

Prediction displayed before every scoped run; actually reported tokens distinguish measured from estimated; P50/P90 calibration audited against future runs; quality/reliability/regressions tracked; repeated known failure types have documented interventions; unsafe actions remain blocked regardless of spend; source data privacy preserved; monitoring cost itself measured.

**Related:** [125 — Five Whys and Forced Connection](125-FORCED-CONNECTION-AND-FIVE-WHYS-PRACTICAL-PLAYBOOK.md), [137 — Superpowers Skill](137-SUPERPOWERS-SKILL-CLAUDE-CODE-CODEX-AGENT-PLANNING.md), [127 — Skills and Graft](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md).

**Status:** exact user idea + concrete conceptual specification committed. No actual tasks sampled, monitoring code deployed, scheduled checks created, forecasts calibrated or API-billing records accessed.


### New agent workflow cost study candidate (2026-10-27)

[168 — Google Elephant-Goldfish Model](168-GOOGLE-ELEPHANT-GOLDFISH-MODEL-SPEC-DRIVEN-AGENTS.md) separates deeply contextual spec-writing from fresh multi-agent Goldfish reviews. For a cost/quality experiment, forecast the additional reviewer calls, output tokens and tool-read work **before** running, then observe true billed usage, spec ambiguity found, false-positive findings, rework and escaped defects. This is a **proposed measurement protocol**, not an observed optimization.
