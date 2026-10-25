# Reel Notes 11 — A Green Pipeline Can Still Produce Bad Data

_Captured 2026-10-25. Topic: reliable ETL / ELT, analytics, data contracts, publish gates._

## Scenario preserved

The source system supplies **10,000 orders**. The destination table contains **4,812 rows**. Some orders are missing; **212 rows** have null customer IDs. The script finishes without throwing an exception and its pipeline dashboard glows green. The analytics dashboard is nevertheless wrong.

**Arithmetic:** 4,812 / 10,000 = **48.12%** retained; **5,188** source rows are missing *if* a one-to-one mapping with no intended filtering is the correct contract. Do not assume that comparison is correct when deduplication, filtering, time-zone windows, splits or aggregations legitimately change row counts.

### Four quality checks from the reel

| Check | Example | What failure means |
| --- | --- | --- |
| **Completeness / count** | Expected 10,000 rows, actual 4,812 | Missing/dropped records *if* an equal count is required |
| **Required fields / nulls** | 212 rows have `customer_id IS NULL` | Broken foreign-key join, attribution or contract |
| **Uniqueness / duplicates** | Check repeated `order_id`; sample returns 0 duplicates | Passes this particular check, but doesn't prove records are valid |
| **Freshness / latency** | Newest order is 12 minutes old, below an agreed delay budget | Passes this check; stale data would fail if over threshold |

**Distinction:** “Pipeline executed” reports operational success; “data is correct” needs domain-aware quality validation. Do not make every quality check pass simply by changing thresholds after failure.

### Example checks for a simple orders table

~~~sql
-- Count after a known synchronized extraction window.
SELECT COUNT(*) AS row_count FROM orders;

-- Required join keys should be present.
SELECT COUNT(*) AS null_customer_ids
FROM orders WHERE customer_id IS NULL;

-- ID must be unique within the agreed data scope.
SELECT order_id, COUNT(*) AS copies
FROM orders GROUP BY order_id HAVING COUNT(*) > 1;

-- Evaluate freshness against an agreed maximum delay.
SELECT MAX(order_created_at) AS newest_order_time FROM orders;
~~~

The destination and source counts must be compared using the **same business window, schema/version, eligibility rules and time-zone logic**. Missing counts may also reflect out-of-order events or late-arriving batches.

## Proper gate between load and publish

1. Extract/ingest into a **staging or candidate** dataset; log extraction window and source watermark.
2. Transform with deterministic mappings, valid foreign keys and clearly specified filter rules.
3. Run schema, row-count, key-null, uniqueness, freshness, referential-integrity, amount/range and reconciliation checks.
4. Store check results with counts, thresholds, dataset/build identifiers, source watermark, and sample failures.
5. **On pass:** atomically promote candidate tables/views or published partition when supported.
6. **On fail:** alert with structured evidence; hold publishing of the incorrect candidate. Continue serving the **last known good** data only if clearly marked as stale and acceptable for that data product.
7. Investigate, repair, re-run checks and record outcome. If downstream consumers already saw the bad dataset, define backfill and correction behavior.

### Additional data contracts

- **Schema:** required columns, types, allowed enums, nonnullable keys, valid currency units.
- **Accuracy/ranges:** amounts within legal/expected bounds, no accidental negative totals, no lost decimal precision.
- **Referential integrity:** each `customer_id` refers to a valid or intentionally anonymized customer.
- **Distribution/drift:** unusual changes in revenue or volume may indicate upstream bugs even when row counts pass.
- **Exactly-once effects:** use idempotent event IDs, deduplication rules and replay-safe ingestion, not wishful claims of exactly-once networks.
- **PII hygiene:** scrub sample errors of sensitive user data; enforce dataset access control.
- **Timeliness:** alert on missing schedules and freshness delay, but account for weekends/holidays and planned inactivity.

## Example checks as acceptance criteria

- For direct 1:1 ingest, expected destination orders = source orders for the same cutoff, allowing only a documented exception list.
- `order_id` unique in the defined scope; `customer_id` required unless the business rule explicitly permits guest customers.
- No partition promoted when a **critical** rule fails.
- The dashboard displays last successful run time and stale-data state, not a misleading green success.
- Audit output shows exactly **which assertion failed and what rows or counts demonstrate it**.

## Related tools to research, not mandatory

- Great Expectations: https://github.com/great-expectations/great_expectations
- dbt tests: https://docs.getdbt.com/docs/build/data-tests
- Soda Core: https://github.com/sodadata/soda-core
- Apache Airflow: https://github.com/apache/airflow

## Why the reel matters for AI-coded systems

AI can generate plausible ETL code that runs and produces a table while silently dropping data. Correctness must be defined as **data properties** and validated before downstream publication. Retry policies, metrics, API schemas and database indexes alone cannot replace a business-data quality gate.


## Replaying/backfilling historical data

A pipeline can also be “green” while doubling revenue by **appending** a complete month's reprocessed data instead of replacing/reconciling it. See **[23 — Data Backfills, Replay & Idempotency](23-DATA-BACKFILLS-REPLAY-AND-IDEMPOTENCY.md)** for stable keys, safe UPSERT/overwrite, validation and immutable-ledger exceptions.

## Historical backfill safety

A green pipeline can still **double a month's totals** when historical data is appended instead of reconciled. See [23 — Idempotent Data Backfills](23-DATA-BACKFILLS-REPLAY-AND-IDEMPOTENCY.md) for stable event keys, safe merge/overwrite, quality gates and append-only ledger exceptions.
