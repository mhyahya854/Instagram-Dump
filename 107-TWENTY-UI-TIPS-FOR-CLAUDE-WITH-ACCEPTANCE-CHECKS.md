# 107 — Twenty UI Tips to Send to Claude for Better Design

**Source:** one user-supplied screenshot dated 2026-10-26. Heading: **“20 UI tips to send to Claude for better design.”** Two-column numbered list transcribed below exactly in screenshot order. Definitions, implementation patterns and testing criteria are independent engineering expansions; they're **not demonstrated in the screenshot**.

## All 20 source labels and how to use them

| # | Exact screenshot label | What it means | Testable implementation / caveat |
|---:|---|---|---|
| 1 | **Skeleton loaders** | Reserve realistic space for content while loading | Match final shape/dimensions, avoid layout shifts; provide accessible loading status and don't keep it indefinitely |
| 2 | **Optimistic updates** | Show a likely successful result immediately while server processes | Reconcile server truth and rollback on error; never fake payments, bank balances or irreversible results |
| 3 | **Command menu** | Keyboard-invoked searchable actions/navigation | Search and category labels, permissions, ESC/focus handling, accessible role; no unauthenticated privileged actions |
| 4 | **Shortcut hints** | Reveal available keyboard combinations close to relevant action | OS-compatible shortcuts, discoverability, nonconflicting keys, custom remapping if needed |
| 5 | **Undo toasts** | Inform users and provide brief reversal of reversible actions | Actual undo must work; destructive irreversible actions need different safeguards; dismissal/read time accessible |
| 6 | **Stale-while-revalidate** | Display cached prior information while asynchronously refreshing | Mark stale state where material; refresh and error handling; don't show outdated financial/medical/security status without warning |
| 7 | **Pre-rendering** | Render or prepare likely destination views early | Avoid exposing private user data in HTML/static caches; only prefetch with budget and permissions |
| 8 | **BlurHash placeholders** | Tiny hash-generated blurred representation before full image loads | Requires image preprocessing; alt text still necessary, avoid flashing and unnecessary blur for critical info |
| 9 | **View transitions** | Visually maintain continuity when navigating between interface states | Optional with reduced-motion fallback, maintain browser history/focus and don't gate navigation on long animation |
| 10 | **Swipe-to-dismiss sheets** | Dismiss a modal/bottom sheet with touch gesture | Provide visible non-gesture Close control, guard unsaved changes, use touch/mouse/keyboard alternatives |
| 11 | **Interruptible animations** | Allow a new gesture/navigation to change an in-flight transition | Cancel/retarget cleanly; preserve state; no jank or broken double taps |
| 12 | **Predictive Back** | Preview the destination/state while the user starts a back gesture | Platform-specific Android behavior and APIs; match actual navigation and don't expose background private screens |
| 13 | **Hit slop** | Expand interactive touch area beyond an icon's visible rectangle | Preserve gesture disambiguation and neighboring targets; accessible touch targets without bloating art |
| 14 | **Safe area insets** | Account for notches, rounded screens, gesture bars and device chrome | Respect iOS/Android safe-area APIs and dynamic keyboard/landscape; don't double-apply insets |
| 15 | **One-time code autofill** | Let user paste/autofill time-based SMS/email verification codes | Use platform-specific autocomplete semantics, appropriate one-time codes, anti-phishing origin binding and expiry |
| 16 | **Tabular numbers** | Numerals occupy equal width for stable alignment in columns/counters | Use `font-variant-numeric: tabular-nums` where supported; keep currency/decimal/locale correct |
| 17 | **Balanced headlines** | Avoid awkward single-word final lines | Use responsive text balancing where supported; don't break logical heading semantics or accessibility |
| 18 | **Continuous corners** | Smooth corner curvature across cards/buttons/sheets | Apply deliberately with platform tools/CSS support fallback; don't make every object equally rounded |
| 19 | **Idempotency keys** | Use client-generated stable request identifier to prevent repeated server-side action | Server persist/check key with scope and expiry, same payload yields same outcome; critical for payments and retries. **Backend correctness more than UI aesthetics** |
| 20 | **Amazon safe triangle** | Infer cursor movement toward a hover submenu via a triangular trajectory zone | Avoid accidental submenu switches; still provide click, touch and keyboard activation and close delay; test diagonal hover |

### Original screenshot grouping

The screenshot has **1–10 in left column**, **11–20 in right column**, using exactly these phrases. There are no screenshots of actual working examples, no code, and no claim that the mechanisms belong in every product. The wording **“Hit slop”** is a real interaction term, not a direction to generate low-quality “AI slop.”

## Three functional groups, not a universal shopping list

**Perceived performance and responsiveness:** skeletons, optimistic updates, stale-while-revalidate, pre-rendering, BlurHash; monitor loading honesty, stable layouts, cache invalidation and consistency.

**Navigation and control:** command menu, shortcut hints, undo, view transitions, swipe sheets, interruptibility, predictive back, larger hit regions, insets, autofill, Amazon hover triangle. Each needs input device/accessibility parity.

**Typography, visual finish and correctness:** tabular nums, headline balancing and continuous corners affect polish; **idempotency keys** protect server actions and transaction integrity, making them one of the most important *engineering* entries.

## Five implementation anti-patterns to avoid

1. Skeleton screen that never ends or falsely portrays real progress.
2. Optimistic financial action that displays success even when server rejected it.
3. All navigation hidden behind a keyboard command palette, making mobile/first-time use inaccessible.
4. Motion/gestures that replace real keyboard and reduced-motion paths.
5. Fancy rounded components and transitions over broken data, missing permissions or fabricated content.

## Reusable bounded goal for a coding agent

> Inspect the actual product flows and UI, identify which of the 20 patterns help users complete a specific task, implement only justified ones, and test each with realistic loading, failure, retry, keyboard, touch, reduced-motion, zoom and offline states. Preserve existing product style. For optimistic actions and idempotency, include server-side tests. Report what is implemented versus not applicable; don't add animation merely for decoration.

## Cross-references

[01 — Design Laws](01-DESIGN-UX.md), [02 — Functional Quality](02-VIBE-CODED-APP-QUALITY.md), [22 — Motion, Touch](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md), [38 — Error Prevention](38-UX-ERROR-PREVENTION-AND-DECISION-SAFETY.md), [03 — Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [77 — Empty Space](77-PORTFOLIO-STYLE-SCREENSHOTS-AND-WHITESPACE-RULES.md).

**Status:** exact 20 list archived, independent implementation criteria added, **no existing app modified or UI QA executed**.
