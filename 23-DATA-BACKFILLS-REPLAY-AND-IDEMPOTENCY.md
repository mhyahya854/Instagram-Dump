# 23 — Data Backfills: Replace Correctly, Don't Accidentally Double Revenue

Captured 2026-10-25. Related to existing [11 — Data Pipeline Quality](11-DATA-PIPELINE-QUALITY.md) and [10 — Transactions & Migrations](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md).

## Reel scenario

A previous month's data is reprocessed (“backfilled”) to correct one bug. Instead of **replacing or reconciling** the affected results, the pipeline **appends** the full historical set to the existing historical set. A March revenue dashboard now shows roughly double the true total. The pipeline may still be green because no process crashed.

**Key concept:** an ingestion or calculation should be **replay-safe / idempotent**: re-running the same input over the same logical window should not count the same business event twice.

## Pick the right strategy for the destination model

| Model | Safe replay technique | Guardrail |
| --- | --- | --- |
| Snapshot table by date/period | Transactional partition overwrite or stage-and-atomic-swap when supported | Do not expose half-rebuilt periods; keep a valid previous snapshot |
| Event fact table | Unique event/business ID + idempotent INSERT/UPSERT/MERGE | Deduplicate source duplicates before MERGE; define conflict behavior |
| Incremental aggregations | Recalculate affected partitions from deduplicated facts and **replace aggregates** | Never add the new aggregate to last month's stored aggregate without a justified delta model |
| Change-data capture | Maintain stable event version/ordering, replay checkpoints and merge semantics | Late/out-of-order events, deletes and corrections need explicit handling |
| Financial ledger | Append legitimate *new adjustment entries*, never blindly mutate or duplicate history | “Replace, not add” is **not universal**: immutable ledgers need correcting entries and reconciliation |

### PostgreSQL illustrative replay-safe pattern

~~~sql
-- Assumes an agreed unique constraint on (source_system, order_id).
-- This is a conceptual example; production schema and conflict rules vary.
INSERT INTO orders (source_system, order_id, customer_id, amount_cents, order_time)
VALUES ($1, $2, $3, $4, $5)
ON CONFLICT (source_system, order_id)
DO UPDATE SET
  customer_id = EXCLUDED.customer_id,
  amount_cents = EXCLUDED.amount_cents,
  order_time = EXCLUDED.order_time;
~~~

**Caution:** actual replacements must address immutable/audited history, deleted records, event versions and concurrent writes. Generic UPSERT can overwrite newer data with stale events unless version/cutoff guards are in place.

## Before rerunning a past interval

1. Pin **source date window, timezone, schema/version and code version**. State intended row count and reconciliation logic.
2. Snapshot or checkpoint the current published output for recovery.
3. Materialize the candidate result in staging; use deterministic inputs and stable business keys.
4. Run completeness, duplicates, null keys, freshness, monetary totals, and referential-integrity checks.
5. Compare old/new totals and key-level diffs; document why changes are justified.
6. Apply a **transactional, idempotent promotion** (swap/partition replacement/guarded merge/compensating ledger entries as appropriate).
7. Rerun identical backfill in staging; verify no second change or duplicate revenue occurs.
8. Publish only after checks pass; alert on drift and keep clear lineage/restore plan.

## Acceptance tests

- Reprocess March twice → same expected revenue, not 2×.
- Incoming duplicate order ID → deduplicated or deterministic conflict resolution.
- Late-arriving correction → correct version wins.
- Crash halfway → published table is previous valid version or complete new version, not half a rewrite.
- Legitimate adjustments recorded exactly once and auditable.

Source: PostgreSQL ON CONFLICT: https://www.postgresql.org/docs/current/sql-insert.html . Domain verification: dbt data testing https://docs.getdbt.com/docs/build/data-tests .
