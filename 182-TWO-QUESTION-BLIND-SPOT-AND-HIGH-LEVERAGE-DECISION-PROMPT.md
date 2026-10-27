# 182 — Two-question blind spot and highest-leverage intervention prompt

**Directly typed user source:** 2026-10-27 (original retained verbatim, including spelling). **This is a reusable reasoning and decision-making prompt**, not a GitHub repository, an app, a psychological diagnosis, or evidence that a given “blind spot” actually exists. No model run, background automation or user-specific analysis was undertaken.

## Verbatim original user text

> a prompt to save  
> what ois the most important thing i am missing about the situation  
> what is the most high leverage thing we can do to fix it or move closer to the goal

Do not silently correct the source transcription. The following is an independently refined reusable version.

## Copy-ready prompt (refined working version)

> Analyze the situation below with the goal in mind. Challenge my assumptions rather than simply agreeing with me.
>
> **Question 1 — Biggest blind spot:** What is the single most important thing I might be missing, misunderstanding, or underweighting about this situation? Identify the assumption, missing evidence, hidden dependency, risk, or opportunity with the largest potential effect on the outcome. Explain why it matters and distinguish facts from hypotheses.
>
> **Question 2 — Highest-leverage move:** What is the single highest-leverage action we can take now to solve the problem or move meaningfully closer to the goal? Choose an action with a plausible mechanism, clear ownership, reasonable effort and low downside compared with alternatives. Explain why this move beats the next-best option.
>
> **Output:** State the goal as you understand it; name the blind spot, evidence/confidence, the recommended first move, one concrete next step, a measurable success signal, major trade-offs, and the condition that would make you change course. If the evidence is insufficient, identify the most valuable small test or question instead of inventing certainty. Do not prescribe irreversible, high-risk or unauthorized actions.
>
> **Situation:** [Paste the situation, constraints, available resources and actions already attempted.]  
> **Desired goal:** [Define the observable outcome and important non-goals.]

## Compact two-line version (for fast daily decisions)

1. **What is the most important thing I'm missing about this situation?**
2. **What's the highest-leverage thing we can do to fix it or move closer to the goal?**

## Practical use and failure modes

**When to use:** blocked engineering work, planning drift, conflicts between priorities, uncertain project direction, feature backlogs, study planning, logistics, research gaps and evaluating failed iterations. The best answer could be “we don't yet know,” rather than a dramatic hidden truth.

| Decision element | A useful answer | Weak/harmful answer |
|---|---|---|
| Goal | Specific observable desired result | “Be better” without a defined outcome |
| Blind spot | Distinguishes assumption from verified information and shows impact | Makes unsupported claims about people's motives or psychological states |
| Leverage | Prioritizes a plausible bottleneck/constraint or compounding opportunity | Recommends a huge project with weak causal relevance |
| Action | Bounded first step, reversible where possible, owner and deadline/context | Demand for intrusive personal data, speculative urgency or unapproved system changes |
| Measurement | Concrete acceptance test, leading indicator or milestone | Vanity metrics or fabricated certainty |
| Falsification | Explains which facts would overturn the recommendation | Insists on one story after evidence contradicts it |

### Engineering application

**Situation:** An AI agent wrote lots of code but the app still fails acceptance tests.
**Possible missing factor:** No frozen acceptance contract, or no evidence-based validation on the actual commit. This is **an example hypothesis**, not a diagnosis of any current project.
**High-leverage move:** Define one end-to-end acceptance test of the primary user journey, reproduce the failure, fix the earliest bottleneck, and rerun the test before more feature work.
**Signal:** Passing test and verified artifact/commit, not token volume or commits alone.

### Research-archive application

**Situation:** A very large Instagram source backlog produces duplicates and uncertain names.
**Possible missing factor:** Lack of a reconciled source ledger distinguishing original screenshots from independently sourced research.
**High-leverage move:** Give each input a unique source ID and final destination, then validate GitHub links and unresolved identities.
**Signal:** Every accessible original item has exactly one documented mapping; evidence gaps remain flagged.

### Personal-decision application

Use the prompt to generate **alternative hypotheses**, not to assert a friend's hidden motives as fact. For sensitive issues, include consent and care; choose safer, reversible actions and real-world support where needed. The assistant should not overrule the person's own judgment or pressure them into confrontation.

## Extended iterative method

1. Specify the intended result and constraints.
2. Generate at most three candidate blind spots; rank by **impact × plausibility × evidence gap** while keeping confidence explicit.
3. Select the most useful one and name what would disprove it.
4. Generate at most three possible moves; compare expected benefit, effort, time-to-feedback, reversibility and risk.
5. Run the smallest **authorized** test that yields new information.
6. Compare forecast to actual outcome, update beliefs and repeat if needed.
7. Stop when the goal is met or further investigation costs more than its expected value.

**Related archive:** [125 — Forced Connection and Five Whys](125-FORCED-CONNECTION-AND-FIVE-WHYS-PRACTICAL-PLAYBOOK.md), [138 — PRD and Architecture contract](138-PRD-ARCHITECTURE-SEPARATE-SPEC-DOC-CONTRACT.md), [139 — Forecast/observe/calibrate](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md), [168 — Elephant-Goldfish speculative design review](168-GOOGLE-ELEPHANT-GOLDFISH-MODEL-SPEC-DRIVEN-AGENTS.md).

**Source provenance:** exact user message preserved separately above; all examples and expansions are independently authored. The prompt is **not a standing instruction automatically imposed on all other projects**.
