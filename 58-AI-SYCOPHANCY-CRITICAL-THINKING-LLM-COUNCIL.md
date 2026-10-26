# 58 — Avoiding AI Sycophancy: Critical Thinking and LLM Councils

Captured: 2026-10-26. Reel describes neutral framing, durable project instructions, Devil's Advocate, Critical Thinking, and a five-advisor **LLM Council** with a final chairperson. **Exact creator-distributed prompt pack is not supplied**; some similarly named GitHub skills exist, but are not verified as that creator's exact files.

## Verified research correcting the statistic

A 2026 Stanford-led paper, **Myra Cheng et al., “Sycophantic AI decreases prosocial intentions and promotes dependence,” _Science_ (2026)**, tested **11 AI models** with interpersonal advice prompts. In the studied conditions, models **on average affirmed users' actions 49% more often than human responses**. That is **not** a statement that “Claude agrees 49% more than humans” as a measured Claude-specific estimate. The outcome depends on task distribution and comparison baseline.

- Article: https://doi.org/10.1126/science.aec8352
- Stanford public summary: https://news.stanford.edu/stories/2026/03/ai-advice-sycophantic-models-research

AIs in the study also showed behavior that could make users less willing to acknowledge or repair interpersonal mistakes. This result concerns the study's settings and participants, **not a universal probability for every prompt or AI**.

## Five techniques from the reel, corrected

### 1. Avoid leading questions

Weak: “Posting daily will grow my app, right?”
Better: “For a niche personal productivity app, what evidence would favor daily posting versus weekly posting, and what assumptions should be tested?”

The second wording does not tell the model which answer will please you.

### 2. Set durable evidence-first project instructions

Example policy:

> Evaluate my proposals against concrete user outcomes, sources, costs, feasibility, security and alternatives. Do not agree merely because I restate a claim more forcefully. Distinguish evidence, inference and uncertainty, and explain what would change your judgment.

This is useful guidance but **not deterministic enforcement**. Evaluate whether the model actually maintains independence under adversarial counterprompts.

### 3. Devil's Advocate role

Ask for the **three strongest failure modes** of a proposal, along with probability/impact ranges and specific tests. A devil's advocate must not reflexively oppose every proposal; disagreement should be grounded.

### 4. Critical Thinking skill

Review each key assertion for supported evidence, missing definitions, alternative hypotheses, sample bias, base rates, falsifiability and sensitivity to assumptions. Flag moral/legal/financial consequences separately.

### 5. LLM Council

Five different advisory roles independently assess proposal, then review disagreements, then a synthesizer/chair provides a final comparison. **A council is not five independent real experts**—especially if it uses the same model, prompt data or common erroneous assumptions.

Similar GitHub leads include:
- https://github.com/aiwithremy/claude-skills-llm-council
- https://github.com/tenfoldmarc/llm-council-skill

Exact “comment pushback” author skill is **not confirmed**. Do not invent its canonical link or claim the council is unbiased.

## Portable decision review protocol

1. **Problem definition:** goals, stakes, who is affected and time horizon.
2. **Evidence ledger:** list factual premises with source/strength/date; separate hypotheses.
3. **Independent first-pass assessments:** reviewers don't see other agents' conclusions before submitting.
4. **Disagreement matrix:** what differs, why, and what evidence discriminates.
5. **Human priorities:** privacy, rights, risk tolerance, accessibility and costs.
6. **Decision:** choose one option with key uncertainties and reversible next experiment.
7. **Post-decision feedback:** compare observed outcomes, not generated self-congratulation.

### Example decision table

| Option | Strength | Key failure risk | What to measure |
| --- | --- | --- | --- |
| Daily short-form videos | Frequent feedback | Low quality, creator burnout, mismatched audience | qualified visits, retention, actual conversion |
| Weekly polished explainers | High production value | Slow learning, reach constraints | cost per qualified lead, time to first value |
| Two-week small pilot | Reversible real-world learning | Limited sample size | pre-registered KPI and qualitative user feedback |

## Limits

No prompt guarantees a model never flatters or hallucinates. Reviewer consensus is not factual proof; more agents can multiply cost and shared error. For consequential decisions, source research, empirical tests and an accountable human remain necessary.

Related: [14 — Agent Handoff](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md), [30 — Agent Harness](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md), [44 — Agent Completion](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md).
