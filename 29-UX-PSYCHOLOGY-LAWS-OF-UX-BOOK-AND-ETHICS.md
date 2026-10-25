# 29 — UX Psychology: Laws of UX, Perceived Waiting, Defaults and Ethical Patterns

Captured: 2026-10-25. **Original study notes**, not reproduction or a replacement copy of a copyrighted book.

## Publication and provenance

**Jon Yablonski, _Laws of UX: Using Psychology to Design Better Products & Services_, 2nd edition, O'Reilly Media, English edition 2024 (ISBN 9781098146955).** Official catalog: https://www.oreilly.com/library/view/laws-of-ux/9781098146955/ ; author article https://jonyablonski.com/articles/2024/laws-of-ux-the-2nd-edition/ .

**Verified structure**: ten named-law chapters (Jakob, Fitts, Miller, Hick, Postel, Peak–End, Aesthetic–Usability, Von Restorff, Tesler, Doherty), then an application-of-psychology chapter and an ethics/responsibility chapter. The associated website https://lawsofux.com/ covers additional related laws and effects. The earlier [07 — 45 UX principles](07-45-UX-LAWS-ENGLISH.md) is **a curated 45-item reference**, not 45 book chapters or the actual 45-episode Instagram series.

**Copyright boundary:** the user asked to “take everything” from the book. We cannot reproduce its complete protected text, illustrations, chapters, examples or full paraphrased substitute without authorized copy and appropriate rights. These notes provide original, concise insights, ethical implications and fresh product examples; the publisher/author links point to lawful editions.

## Independent chapter/topic study guide (newly written)

| Book chapter | Learn this distinction | Fresh application |
| --- | --- | --- |
| Jakob's Law | Familiar patterns lower relearning, but copying competitors isn't inherently good UX | Keep search and checkout controls where users expect, while differentiating the underlying service |
| Fitts's Law | Movement and selection time depend on target distance and size | Make accessible tap areas for icon controls |
| Miller's Law | Short-term memory is limited; “7±2” is not a hard menu rule | Group a 20-field form by meaning; retain previously entered context |
| Hick's Law | Complex decisions take more time, not all extra choices are equally bad | Show relevant choices, offer filters without hiding needed alternatives |
| Postel's Law | Input robustness must coexist with security validation | Accept common date formats, reject invalid/unauthorized data |
| Peak–End Rule | Ending and intense moments may dominate overall recollection | Clearly end checkout with real success/next steps, not fake celebration |
| Aesthetic–Usability Effect | Attractive appearance can improve *perceived* usability, not actual task success | Test a gorgeous form that may still fail mobile validation |
| Von Restorff Effect | Distinctive items are remembered; endless emphasis dilutes effect | One meaningful primary CTA, not 20 colored pills |
| Tesler's Law | Complexity cannot always be eliminated, only allocated | Pre-fill known context securely rather than making users repeat data |
| Doherty Threshold | Timely perceived response supports interaction flow | Ack action quickly; show true pending work and recovery |

The application chapter motivates conscious translation from psychological principle to design decision: define target user/task, formulate a hypothesis, prototype, check accessibility and validate with real behavior. The responsibility chapter raises dark patterns, variable rewards, infinite feeds, defaults, social influence and unintended consequences. **This is an independently authored interpretation, not a copy of chapter prose.**

## Extra effects in the new reel batch

### Paradox of the Active User

People often start acting instead of reading manuals, onboarding slides or tooltips. **Design implication:** make first use safely discoverable, provide meaningful inline guidance and contextual help. Don't bury the first task behind a five-screen slideshow. “Nobody ever reads anything” is rhetorical exaggeration.

### Mental models

A user forms internal expectations of how a system behaves. When an app violates that expectation, mistakes increase: “archiving” shouldn't silently permanently delete content; “save” shouldn't publish. Research language, use conventional semantics, and make departures explicit.

### Labor illusion vs actual progress

A **labor illusion** is the perceived value or effort signaled when a product visibly shows it is “working.” Pizza trackers and staged loading can reassure. But a false tracker is manipulative. Use actual state (order accepted → preparing → courier picked up) or a truthful indeterminate indicator when progress isn't measurable. **Do not manufacture fake work merely to increase perceived value.**

### Default effect

Preselected options can become sticky because users often retain a default. **Ethics:** never opt users into optional marketing, unwanted sharing or recurring fees through deceptive defaults. Defaults should be transparent, easily reversible, and appropriate for consent/privacy law.

### F-pattern and banner blindness

Eye-tracking sometimes shows F-like scan paths on text-heavy pages; users may overlook ad-like banners. **Not every user scans every layout in an F**, nor is the “50 milliseconds” attractiveness claim a universal success predictor. Test actual tasks and reading order.

### Peak-End, wait perception and loading spinners

The reel conflates **Peak–End Rule** with perceived waits and skeleton screens. Skeleton UI can indicate expected layout and reduce perceived uncertainty, but **fake skeletons violate truthful feedback** and are not required on every app. Use spinner/placeholder only where genuine wait justifies it. Accessibility and reduced motion matter.

### Dark patterns named in clips

- Mailing-list signup placed where the user expects legally required Terms agreement: **consent misdirection**.
- Tiny/invisible unsubscribe action or swapping primary/secondary button positions to impede exit: **obstruction and deceptive hierarchy**.
- Friction that surprises users only when cancelling, unlike easy signup: **asymmetric obstruction**.
- Artificial urgency, manipulative timers, involuntary defaults: **avoid**.

Design principle: protect user autonomy, use clear actions, easy opt-out, plain language, honest confirmation, and transparent billing.

## Practical checklist

1. Label the real user task and *applicable* principle; not all 45 should be applied simultaneously.
2. State a testable hypothesis and define success beyond aesthetic preference.
3. Verify legibility, touch targets, keyboard navigation, real system status and error handling.
4. Flag dark patterns and fake metrics/progress even if they increase short-term clicks.
5. Compare prototype with actual users; observe comprehension, mistakes, completion and trust.
6. Record evidence and keep a correction log rather than guessing universal numbers.

## Primary references

- O'Reilly 2nd edition official: https://www.oreilly.com/library/view/laws-of-ux/9781098146955/
- Author edition notes: https://jonyablonski.com/articles/2024/laws-of-ux-the-2nd-edition/
- Web principle index: https://lawsofux.com/
- Nielsen Norman Group heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- Related own references: [07](07-45-UX-LAWS-ENGLISH.md), [18](18-LEARNING-UI-CRITIQUE-VISUAL-TAXONOMY.md), [22](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md).

## Fifth reel batch: preventing avoidable mistakes

[38 — UX Error Prevention](38-UX-ERROR-PREVENTION-AND-DECISION-SAFETY.md) turns NN/g's Error Prevention heuristic into testable constraints, ethical defaults, feedback and recovery. Avoid prechecking marketing consent or recurring subscriptions; don't confuse a front-end disabled button with server-authoritative business validation.
