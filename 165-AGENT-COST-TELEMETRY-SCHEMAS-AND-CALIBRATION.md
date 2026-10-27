# 165 — Agent cost forecasts, telemetry and bounded learning: implementation workbook

**Source:** user-typed pre-run forecast → post-run delta → cluster misses → refine heuristics. Full original wording in [139](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md). This is an independent specification and illustrative code; **no live runs, model invoices, benchmarks or observed error patterns** are claimed.

## Problem statement and guardrails

Optimize for **completed, correct, safely authorized work per unit cost**, not minimum input tokens. Before any task, show the predicted input/output/cache tokens, inferred context size, estimated tool calls, inference calls, runtime range and cost range. Forecasts are estimates, not promises. After, use provider-reported usage as the authoritative count where possible; separate estimated from actual fields. Do not log raw prompts, API keys, document contents or user identifiers.

## Canonical task event schema

```json
{
  "schema_version": "1.0",
  "task_id": "opaque-random-id",
  "forecast_version": "heuristic-2026-10",
  "project_id": "non-personal-workspace-alias",
  "task_class": "repo-documentation",
  "model": "model-identifier",
  "forecast": {
    "input_tokens": 12000, "output_tokens": 4000,
    "cached_input_tokens": 0, "tool_calls": 18,
    "inference_passes": 6, "context_peak_tokens": 24000,
    "cost_usd_low": null, "cost_usd_high": null,
    "latency_seconds_low": null, "latency_seconds_high": null
  },
  "actual": {
    "input_tokens": null, "output_tokens": null,
    "cached_input_tokens": null, "tool_calls": null,
    "inference_passes": null, "context_peak_tokens": null,
    "cost_usd": null, "latency_seconds": null,
    "retries": null, "acceptance_passed": null
  },
  "events": [],
  "source_of_actual": "not-measured",
  "data_retention_days": 30
}
```

All numeric values above in **forecast** are **illustrative fixture values, not predictions for this GitHub archive or observed user workloads**. Null actuals deliberately mean *not measured*; never replace them with zero.

## Event structure and calculation

For each model pass, append a monotonically sequenced event with: task_id, parent span, provider, model/version, operation type, start/end monotonic timestamps, reported input/output/cache read/cache write tokens, response status, retry count, tool type, tool payload *byte count only*, tool result byte count, acceptance-test outcome and sanitized failure category. For non-model tools token values are `null`. Providers' cache token accounting varies; preserve raw billing units, do not double count cache hits already included in input.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Tokens:
    input: Optional[int]
    output: Optional[int]
    cached_input: Optional[int]

def relative_error(predicted: int, observed: int):
    if predicted < 0 or observed < 0:
        raise ValueError("nonnegative counts required")
    if predicted == 0:
        return None  # avoid dividing by zero; report absolute delta separately
    return (observed - predicted) / predicted

def evaluate(predicted: Tokens, actual: Tokens):
    results = {}
    for field in ("input", "output", "cached_input"):
        p, a = getattr(predicted, field), getattr(actual, field)
        results[field] = {
            "delta": None if p is None or a is None else a - p,
            "relative_error": None if p is None or a is None else relative_error(p, a)
        }
    return results
```

The code above computes errors only. It does not send telemetry, calculate provider charges or modify any system.

**Cost formula:** `sum(model_pass.input_billable * dated_input_price + output_billable * dated_output_price + cache_read * cache_read_price + cache_write * cache_write_price + tool_metered_fees)`; only use each category once according to provider billing conventions. Store currency, price schedule timestamp, tier/contract, discount, rounding and attribution method. A *token estimate is not an invoice*. Context peak is max active message window, not cumulative input across multiple calls.

## Forecast features and calibration

| Feature | Why it matters | Safe data collection |
|---|---|---|
| Task class, repo size, source count | Research-heavy requests drive retrieval and synthesis | Counts, not contents |
| Tool chain length and external dependency count | Fan-out, retries, API errors | Tool names and status codes only |
| Baseline context/token budget | Large histories repeat prompt tokens | Count/model token API |
| Number of branches/subagents | Parallel spans increase total spend | Span IDs and topology |
| Acceptance-test complexity | Rework from failures and missing evidence | Pass/fail and failure class |
| Structured response/long-document requirement | Drives output tokens | Estimated output budget |
| Cache state | Cold-start and warm-cache differ | Hits/misses and provider usage |

Use robust cohort summaries (median, p90/p95, sample size, confidence intervals); compare signed bias `mean(actual-predicted)`, absolute error `MAE`, relative `wMAPE = sum(|a-p|)/sum(a)` for nonzero aggregate actual, and calibration coverage of promised ranges. Report samples too small for reliable estimates as inconclusive. Use time-ordered training/test partitions; keep final holdout sealed and compare a naive baseline before choosing new complexity.

## Feedback loop (bounded, explainable)

1. Forecast and **freeze** assumptions before execution; append start timestamp.
2. Observe actual provider usage after each span; label missing data without imputing.
3. Diagnose error categories: repeated context, unplanned tool fanout, permission denials, retry storms, long synthesis, compaction losses, cache misses and evaluator failures.
4. Propose a specific rule change, e.g. add a bounded retry reserve for API-heavy workflows; **never assert a percentage without observed records**.
5. Replay against historical *development* tasks and a held-out sample; evaluate quality, cost, latency and worst-case tail.
6. Promote only if evidence exceeds a predefined minimum improvement with no correctness/privacy regression. Version the rule and provide rollback.
7. Drift monitoring: revalidate after provider pricing/model changes, new tool schemas and agent harness updates.

**Stopping rules:** fixed max agent steps, time and money budgets; circuit breaker on repeated identical errors; make authorization and high-risk actions human-controlled. A calibration loop must not mutate production billing or execution policy without review.

## SQL sketch — local analysis database

```sql
CREATE TABLE agent_task_metrics (
 task_id TEXT PRIMARY KEY,
 started_at TEXT NOT NULL,
 class TEXT NOT NULL,
 forecast_version TEXT NOT NULL,
 predicted_input INTEGER,
 observed_input INTEGER,
 predicted_output INTEGER,
 observed_output INTEGER,
 predicted_tool_calls INTEGER,
 observed_tool_calls INTEGER,
 predicted_passes INTEGER,
 observed_passes INTEGER,
 observed_cost_usd NUMERIC,
 source_of_actual TEXT NOT NULL,
 accepted BOOLEAN,
 CHECK (predicted_input IS NULL OR predicted_input >= 0),
 CHECK (observed_input IS NULL OR observed_input >= 0)
);
-- Example read-only audit query (no results claimed):
SELECT class, forecast_version, COUNT(*) AS n,
 AVG(observed_input - predicted_input) AS mean_input_delta
FROM agent_task_metrics
WHERE observed_input IS NOT NULL AND predicted_input IS NOT NULL
GROUP BY class, forecast_version
HAVING COUNT(*) >= 20;
```

**Security:** keep task IDs unlinkable to personal identity unless necessary; redact prompts and tool payloads, encrypt at rest, control analyst access, set retention, protect logs from untrusted tool-result injection. Cross-ref [148](148-CONTEXT-MEMORY-TOKEN-BURN-CUT-AGENT-TOOL-MATRIX.md), [46](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md).

**Acceptance criteria:** each task has immutable pre-run forecast; missing usage is explicit; sums reconcile with provider invoices when possible; 100% of forecasts are versioned; predictions are tested prospectively, and no “savings” figures are published without data and unchanged quality.
