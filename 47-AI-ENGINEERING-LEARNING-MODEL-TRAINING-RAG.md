# 47 — AI Engineering From Scratch, Training Budgets, LoRA and RAG

Captured: 2026-10-25, Hindi-English and English reels. Original educational model; not an inference service, not a purchased course.

## Confirmed open-source AI curriculum

**Project:** https://github.com/rohitg00/ai-engineering-from-scratch ; https://aiengineeringfromscratch.com/ . Its October 2026 readme advertises **542 lessons, 20 phases**, with Python, TypeScript, Rust and Julia. Includes mathematics, ML, deep learning, transformers, vision, speech, model internals, agents, retrieval and production. It has an installable agent-tutor skill that may give a placement quiz and sequential study help. **No skill installed.**

### Teaching principle from the Hindi reel

“Knowing what React, Next.js, NestJS, PostgreSQL, MySQL, tables and backends do helps you ask AI to build better software—even if you cannot personally debug complex brackets yet.” This is directionally reasonable, but understanding *names* alone does not guarantee software correctness. Learn conceptual models and practice tests, not only prompt engineering.

**Translate these terms clearly:**

- React: a UI library for building components and interactive browser applications.
- Next.js: a React-oriented full-stack web framework with rendering/routing/data features.
- NestJS: server framework commonly built on Node.js/TypeScript for structured backend APIs.
- PostgreSQL / MySQL: relational databases with SQL interfaces and transactional semantics.
- Database table: structured rows/columns with keys, constraints and relations.
- API: defined interface through which software exchanges requests, actions and responses.
- Rust: systems-oriented language emphasizing safety and performance; preferred by user's software rules by default when a legitimate technical fit exists.

## Three different approaches to enterprise AI

### 1. Pretraining a model from scratch

Start with an architecture and parameter initialization; train on extremely large token datasets using gradient descent to minimize a predictive objective. Requires model design, data acquisition/rights, compute, distributed training, evaluation, safety, serving. Costs range widely and **“$100 million” is not a universal baseline**. A small toy model can be trained cheaply; frontier-scale training is enormously costly. Compute-hour figures from a reel are unverified unless the actual model/technical report supports them.

### 2. Fine-tuning a pretrained model

Update parameters using curated examples so an existing model better performs a target behavior, style, domain task or output schema. **LoRA** (low-rank adaptation) freezes base weights and trains small low-rank parameter matrices. It can reduce memory and compute compared to updating all weights; percentage, GPU needs, license and total cost depend on model and dataset. **“Under $100” is one narrow hypothetical**, not an estimate for all production training.

Fine-tuning can teach some domain facts but is often **poor at maintaining frequently changing source-of-truth documents**. A fine-tuned model may still hallucinate.

### 3. Retrieval-augmented generation (RAG)

Retain your company documents in an authorized knowledge store. Index source passages using keyword search and/or vector embeddings. On each authorized question, retrieve relevant, up-to-date passages; put them in the model's context; demand grounded answers with citations. **The model weights need not change.** RAG still has retrieval misses, version conflicts and permission leakage risks.

| Requirement | Pretrain | Fine-tune / LoRA | RAG |
|---|---|---|---|
| New general foundational capability | Potentially | Limited adaptation | No model change |
| Consistent task-specific output | Maybe | Often useful | Prompt/template may suffice |
| Frequently updated company policy | Expensive/wrong fit | Requires retraining | Usually preferable |
| Citations to original documents | Not inherent | Not inherent | Can retain cited passages |
| Small project budget | Not frontier-scale | Possibly | Common first choice |
| Private data controls | Data governance needed | Data/inference governance | Index and row-level retrieval permission critical |

### Example: company refund policy

Question: “May my order be refunded?” First verify account eligibility and retrieve the exact refund policy version, then answer with a citation and clarify exceptions. **Do not train the company's private policy into base weights by default.** If there are structured eligibility criteria, implement them deterministically in code rather than asking a model to invent a decision.

### For a “$50k AI budget”

Start with process evaluation, data governance, model/API selection, secure RAG, small offline benchmarks and a monitoring plan. Only consider LoRA if it clearly improves measured task performance over a strong baseline. Do not promise any specific training cost without data size, model, tokens, GPUs, iteration count, hosting and staffing.

## Learning roadmap from first principles

Math/linear algebra → probability and losses → Python/Rust fundamentals → relational data/SQL → API design and testing → embeddings and retrieval → model inference → tool schemas and agent loops → evaluation and deployment. Run small reproducible exercises at each step.

## Primary references

- https://github.com/rohitg00/ai-engineering-from-scratch
- https://arxiv.org/abs/2106.09685 (LoRA original research)
- https://arxiv.org/abs/2005.11401 (retrieval-augmented generation)
- [39 — Embeddings](39-AI-FUNDAMENTALS-EMBEDDINGS-STUDY.md)
- [30 — Agent Harness](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md)

**Research status:** curriculum verified; promotional star counts, exact “60k+,” course completion percentages and cost predictions aren't independently guaranteed.
