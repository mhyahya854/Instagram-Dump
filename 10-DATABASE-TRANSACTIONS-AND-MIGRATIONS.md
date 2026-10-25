# Reel Notes 10 — Safe Database Changes, Financial Transactions and Race Conditions

_Captured 2026-10-25. Keep backups and permission safeguards in scope for all potentially destructive work._

## Scene A: “Add a referral program” accidentally deletes the production database

The reel illustrates a coding agent asked for a small feature but given uncontrolled production access. It modifies the schema, runs code intended for a development database against production, and wipes real customers. The *lesson is not that AI always deletes databases*: high-impact changes must have **environment isolation, defined approval boundaries, reviewed migrations and recoverable backups**.

### Three safeguards from the reel, corrected

**1. Migration files.** Every schema change should be a version-controlled migration with a clear intent, review, dependencies and preconditions. Run against a representative staging dataset and test on production-like versions. Do not assume a migration safe on an empty test database is safe at scale. For large tables, watch lock durations and index-build strategy.

**2. Backups and point-in-time recovery.** Backups need retention, physical separation where appropriate, restricted access, encryption, and measured restore tests. A “backup succeeded” status is not evidence data is recoverable. Agree on recovery point objective (maximum tolerable data loss) and recovery time objective (maximum tolerable outage).

**3. Rollback or forward-recovery strategy.** The reel says “every migration ships with an undo step.” **This is unsafe as a universal rule**: dropping columns or rewriting data may be irreversible, and downgrading a schema may lose newer application writes. Prefer reversible expand-and-contract changes, safe forward fixes, application rollback compatibility, and tested restore or point-in-time recovery procedures for destructive failures.

### Deployment plan

1. Confirm target environment explicitly (local/staging/production) and block destructive commands in production without human approval.
2. Create a verified restore point and inspect storage/billing.
3. Prepare migration with non-destructive defaults, preconditions, backfill and postcondition checks.
4. Run staging migration, seed realistic rows and measure duration/locking.
5. Validate application version compatibility and feature-flag rollout.
6. Back up production, obtain approval, execute migration under scoped credentials.
7. Check row counts, constraints, app behavior, logs and key reports.
8. If failures occur: stop writes if necessary, choose forward fix versus restore using a recovery plan; preserve logs.

**Safe permissions:** local agents should not hold always-on production DBA credentials. Read-only analysis and explicitly approved migration runner are separate privileges.

## Scene B: transfer button clicked a thousand times

Reel story: sender has $50; simultaneous transfer requests see $50 and some credit the recipient repeatedly, possibly draining/duplicating funds. This illustrates **race conditions**, stale reads, missing atomicity and missing idempotency.

### ACID, precisely

| Letter | Meaning | What it means in the transfer example |
| --- | --- | --- |
| **A: Atomicity** | A transaction's effects commit together or are rolled back together. | Debit and credit shouldn't be persisted separately after mid-flight crash. |
| **C: Consistency** | Committed transactions must preserve enforced data invariants. | A balance-check/constraint and ledger integrity should remain valid. |
| **I: Isolation** | Concurrent transactions should not interfere outside the guarantees of the chosen isolation level. | Concurrent transfers need protection against two requests both spending the same available balance. |
| **D: Durability** | Committed data survives according to configured DB durability and failure assumptions. | A completed transfer must remain recorded after an application crash. |

**Correction:** “Just put both calls into one database transaction” addresses partial writes **but not automatically** every overspending race; transaction isolation, serialization/row locks, atomic conditional updates and idempotency are also needed.

### Illustrative PostgreSQL transaction design (pseudo-SQL)

The illustration assumes a ledger/transfer schema, two accounts in a single database, authenticated ownership/authorization and nonnegative integer minor units (e.g. cents). It is **not** ready-made payment code.

~~~sql
BEGIN;
-- First reserve the idempotency key with a unique constraint:
-- (tenant_id, client_request_id) must be unique.
-- Lock both account rows in a fixed ID order to minimize deadlocks:
SELECT id, balance_cents
FROM accounts
WHERE id IN (:sender_id, :recipient_id)
ORDER BY id FOR UPDATE;
-- Check sender exists, owns funds, and balance >= amount_cents > 0.
-- Debit only if sufficient (also check affected-row count).
UPDATE accounts
SET balance_cents = balance_cents - :amount_cents
WHERE id = :sender_id AND balance_cents >= :amount_cents;
-- Require exactly one sender row updated.
UPDATE accounts
SET balance_cents = balance_cents + :amount_cents
WHERE id = :recipient_id;
-- Require exactly one recipient row updated.
-- Insert balanced double-entry ledger records with same transfer ID.
-- Commit only after checking all conditions:
COMMIT;
~~~

**Critical:** sample leaves authorization checks, idempotency-key reservation and error rollback as explanatory comments. The *real application must implement and test them* before moving money. Lock order can prevent some deadlocks; isolation/retry behavior and credit correctness matter too.

### Recommended reliability features for money/credits/quotas

- **Unique idempotency key** scoped to user/tenant and request, with safe response replay on retries; repeated clicks should never repeat a charged operation.
- **Integer minor currency units or exact decimals**, not binary floats for balances.
- **Atomic invariant** such as a conditional debit plus check; balance constraints and a transaction ledger.
- **Row-level locking or appropriate isolation**, with tested concurrency.
- **Double-entry ledger** where financial correctness requires audit/reconciliation, not just a mutable balance field.
- **Payment provider webhook verification** and deduplication; retries after uncertain network outcomes.
- **Failure tests** for duplicate requests, concurrent requests, timeouts, partial outages and retries.

### Supabase-specific design caution

A Postgres RPC/database function can perform multiple operations transactionally, but SECURITY DEFINER ownership, EXECUTE permissions, SQL injection, schema exposure and RLS privileges must be inspected. “Use a single Supabase function” does not automatically guarantee authorization, isolation or safety.

## Testing matrix

| Test | Expected property |
| --- | --- |
| Two duplicate requests at same time | One transfer applied, replayed/idempotent duplicate response |
| Many concurrent debits exceeding $50 total | No negative balance or unearned credits |
| Crash before commit | No partial committed transfer |
| Crash immediately after commit before client receives reply | Retried request does not double-charge |
| User tries a different sender ID | Server denies unauthorized transfer |
| Migration interrupted | Safe recovery with no silent table loss |
| Restore from backup | Actual restored dataset, permissions and application validated |

## Sources

- PostgreSQL transaction tutorial: https://www.postgresql.org/docs/current/tutorial-transactions.html
- PostgreSQL explicit locking: https://www.postgresql.org/docs/current/explicit-locking.html
- PostgreSQL transaction isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- Supabase Security Advisors: https://supabase.com/docs/guides/observability/advisors
- Previous architecture rulebook: [03-PRODUCTION-SYSTEM-ARCHITECTURE.md](03-PRODUCTION-SYSTEM-ARCHITECTURE.md)
