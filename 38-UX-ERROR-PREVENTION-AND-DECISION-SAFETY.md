# 38 — UX Rule Five: Prevent Errors Before They Happen

Captured 2026-10-25, short English reel. Principle: **prevention is often more useful than a polished error message**, especially when mistakes are costly, irreversible, confusing or expose private information.

## Speaker's normalized guidance

“Stop mistakes before they happen. Every error costs time and trust. Block choices that cannot work. Fill in smart defaults. Confirm only the risky stuff.” The extra “Again, return before you leave” is incomplete dictation; do not invent meaning.

This overlaps Nielsen Norman Group's **Error Prevention** heuristic and the earlier original 45-law reference. Not every error is preventable, and removing all user freedom in the name of “safety” is its own UX failure.

## Four distinct techniques

| Technique | Example | Test / tradeoff |
| --- | --- | --- |
| Constraints | Disable “book” only when slot truly unavailable; don't allow negative quantities in valid positive-only forms | Don't silently disable with no explanation; recalculate state server-side |
| Helpful defaults | Preselect user's locale/timezone from explicit setting | Avoid preselecting paid add-ons, marketing consent or recurring billing |
| Timely validation | Explain why required email format is invalid; provide example and inline recovery | Don't erase user's entire form or block legitimate uncommon names |
| Consequence-aware confirmation | “Delete workspace and 43 files?” with cancel and consequence | Avoid generic “Are you sure?” for harmless routine actions; use undo when genuinely available |

## Error prevention vs error recovery

**Prevention** reduces the chance of mistake; **recovery** helps when it occurs anyway. A destructive action may need a labeled confirmation *and* a backup/undo policy; a financial transfer needs server-side atomicity and duplicate prevention, not a pretty modal.

### Action-specific checklist

- Define valid range, ownership, eligibility and authorization rules on server.
- Distinguish transient errors (retry may help) from invalid states (user must correct).
- Apply constraints to prevent wasted clicks but keep disabled-state reason discoverable.
- Use accessible readable error text, focus management and keyboard support.
- Preserve entered data unless intentionally sensitive or invalid.
- Confirm high-cost irreversible actions with consequence-specific language.
- Audit defaults for privacy, subscription consent and deceptive nudges.
- For repeated requests, use idempotency and concurrency controls: UX click guard alone is insufficient.

## Worked example: booking with no remaining seats

Before submitting, show clearly that selected slot is full and provide alternatives; during submission, transactionally recheck inventory under concurrency; if rejected, explain the exact conflict and allow another choice. The front-end state is advisory; final correctness comes from server behavior.

## Source

- NN/g error prevention heuristic: https://www.nngroup.com/articles/ten-usability-heuristics/
- Related [29 UX Psychology](29-UX-PSYCHOLOGY-LAWS-OF-UX-BOOK-AND-ETHICS.md), [13 Design Interactions](13-DESIGN-INTERACTIONS-ICON-STYLES.md).

## Thirteenth collection — actionable error prevention from 20 UI terms

[107 — 20 UI Tips](107-TWENTY-UI-TIPS-FOR-CLAUDE-WITH-ACCEPTANCE-CHECKS.md): optimistic UIs need **rollback**, undo toast needs **real undo**, pre-rendered stale data needs **freshness handling**, swipe-dismiss needs **a visible non-gesture escape**, OTP autofill needs token expiry/origin validation, and **idempotency keys** need backend coordination. Do not copy these patterns blindly or show unverified success; test negative states.
