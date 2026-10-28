# 185 — AI tutor that teaches until a chosen learning goal is demonstrably met

**New direct typed source:** 2026-10-28, user wrote: "there is a github repo that makes ai teaches us anything until we achieve thr goal we have set did we add if if not can you ifnd the github repo". **Exact repo name not provided.** This research identifies and compares independently verified candidate repositories rather than falsely claiming a particular reel or repo was supplied. No screenshots attached and no skills installed or run.

## Research outcome: previously archived at a generic level, but not the teaching workflow

The original forty Claude repository screenshot archive [145](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md) included **`mattpocock skills`** as item #11, with owner `mattpocock/skills` verified. However the **specific `teach` skill**, its `MISSION.md` mechanism, the learning-goal acceptance criteria, and the independent `learn-anything` alternatives were **not yet individually documented** in this research archive. A scoped live GitHub code search of Instagram-Dump for `/teach`, `MISSION.md`, `Nar101` and `learn-anything` found no relevant dedicated prior entry at time of research.

## Strongest candidate A: Matt Pocock /teach — mission-based teaching across sessions

**Canonical repository:** https://github.com/mattpocock/skills  
**Exact upstream skill:** https://github.com/mattpocock/skills/tree/main/skills/productivity/teach  
**Official in-repo explanation:** https://github.com/mattpocock/skills/blob/main/docs/productivity/teach.md  
**Live source inspected:** `skills/productivity/teach/SKILL.md` and `MISSION-FORMAT.md` through GitHub API on 2026-10-28. **Root license:** MIT, subject to actual component terms.

### What it does

It turns one dedicated folder into a **persistent educational workspace**. On `/teach`, it asks why the learner needs a topic in the real world. It creates `MISSION.md` to describe a concrete desired outcome and success criteria, then sources trustworthy references, writes short, attractive self-contained HTML lessons and remembers progress across sessions. Next topics are selected against mission relevance and the learner's **zone of proximal development**, based on observed learning records rather than simply repeating a canned syllabus.

Example file structure:

~~~text
learning-project/
  MISSION.md              # concrete real-world outcome and success conditions
  RESOURCES.md            # curated/dated trusted primary sources
  learning-records/       # demonstrated knowledge, corrected misconceptions
  lessons/0001-topic.html # one actionable HTML lesson
  reference/              # reusable cheatsheets, diagrams, glossary
  assets/                 # shared CSS/widgets
  NOTES.md                # learner's teaching preferences and corrections
~~~

It emphasizes **retrieval, spacing and interleaving** to develop retention, not just temporary familiarity. The upstream documentation openly notes **limitations**: no fully explicit diagnostic assessment when the course starts (prior knowledge can be assumed incorrectly), and reports of answer-position bias in a quiz widget design. Therefore do not claim infallible mastery testing or that it autonomously *continues running unattended until any goal is achieved*. The learning program advances during authorized sessions and when the person returns.

### Why this might be the exact repo

Its `MISSION.md` specifically captures **why** the student is learning and defines **“Success looks like”** as an observable change, very close to the user's phrase “until we achieve the goal we have set.” This is an inference, **not confirmation** that the user saw this specific creator's reel.

**Safe usage outline:** In an isolated learning folder, ask the compatible agent to use the `teach` skill and set `MISSION.md`, e.g. “I want to independently explain and solve ten progressively harder physiology acid-base questions and correctly justify compensatory responses, using approved course references.” Inspect the agent's skill installation and scripts before enabling. Keep medical educational content anchored to authoritative course material; simulated exams don't establish clinical qualification.

## Strongest candidate B: naeemdev360/learn-anything-skill — strict goal and mastery gating

**Canonical repo:** https://github.com/naeemdev360/learn-anything-skill  
**Live GitHub source inspected:** `SKILL.md`, `README.md`; root MIT license.

This Claude Code skill asks for the topic, target depth (**Tour / Practitioner / Deep / Mastery**), current level, file format, course folder and a practical application/final build. It creates:

- `course.json`: explicit curriculum and passing thresholds
- `progress.json` and `progress.html`: attempts, session time, completed lessons, scores, review schedule
- Per-lesson explanations, worked examples, quizzes, explain-back tasks and graded assignments
- Module tests and a final project
- `.grading/`: answer keys and rubrics intended for tutor use

**Key distinction:** The repo supplies an actual state-machine script `scripts/course.py` to enforce course progression gates, instead of trusting a model to remember whether the student passed. Its `SKILL.md` says **don't advance until passing**, **don't expose keys**, **don't invent scores**, and **resume existing work before generating a new course**. Passing can require quiz, explanation and applied assignment thresholds; failed components get remedial instruction. Spaced review is scheduled after passing. A missed score can be wrong if the model grading is inaccurate, but the *gate logic* is software-enforced.

**Best fit:** A learner who explicitly wants to **continue until they demonstrably meet a target** with formal assessments and persistent progress. Compared with Matt Pocock, it has a stronger specified gate and dashboard, but is more heavyweight and includes locally executed Python scripts that need a security review first. Avoid equating 100% course completion with real professional competence.

## Strongest candidate C: Nar101/learn-anything — source-grounded adaptive mastery evidence

**Canonical repo:** https://github.com/Nar101/learn-anything  
**Live source:** `SKILL.md`; MIT declared.

This portable Skill for Codex, Claude Code, Cursor and compatible clients turns a learning goal into a source-grounded adjustable course with **current lesson generation only**. It distinguishes:
- **exposure** to material;
- success **with hints**;
- **independent** success;
- ability to **transfer** to new cases;
- **delayed recall** after time has passed.

A crucial protection is that the rubric or answer is frozen **before** the learner answers, reducing moving-goalpost grading. It maintains separate “content delivered” versus “mastery demonstrated” statuses. The creator also documents validation scripts and constraints for using high-stakes material: a lesson doesn't certify safe professional practice.

**Best fit:** Actual knowledge retention, adaptive plans and teaching from an uploaded PDF, textbook notes or source documents, with transparent mastery evidence. Do not claim a portable SKILL.md guarantees persistence in a chat-only host without file-write capability.

## Additional independently located alternatives (separate repos, not aliases)

| Repository | Specific difference | Caution |
|---|---|---|
| [vesperchinn/learn-anything-skill](https://github.com/vesperchinn/learn-anything-skill) | Creates a durable learning repo with `START_HERE.md`, `TODAY.md`, sourced material coverage, Day 1 in chat and per-session progress; multilingual adapters | Beta/platform adapters and capability differences, check license and release |
| [read2017/learn-anything-with-AI](https://github.com/read2017/learn-anything-with-AI) | Portable project-driven learning workflow, diagnostic, roadmap, practice and mastery checks | README available in Chinese and English; exact repo structure/skill location differs |
| [LEARNableLabs/opentutor](https://github.com/LEARNableLabs/opentutor) | Portable skill or web/Telegram tutor; Socratic daily teaching and spaced review | Web app may need Node dependencies and provider API key; “local” does not necessarily mean local inference |
| [TerraByte-Dev/OpenEdu](https://github.com/TerraByte-Dev/OpenEdu) | Tauri desktop app with generated 6-level curriculum, practice tests, local SQLite and local Ollama as an option | Distinct full app; memory/requirements and model quality vary |
| [Integralist/agent-skills](https://github.com/Integralist/agent-skills/blob/main/.agents/skills/teach/SKILL.md) | A separately maintained `teach` skill with `MISSION.md`, resources and learning-records | Similar patterns do not establish origin/fork relationship to Matt Pocock |
| [casankalppawar/teach-upgrade](https://github.com/casankalppawar/teach-upgrade) | `/teach` iterative assess → map → test → teach-back, written to disk | Independent implementation, inspect grading and safety controls |

## Side-by-side selection

| Constraint | Best candidate(s) | Key verification |
|---|---|---|
| “Make AI teach based on the specific goal I set” | **Matt Pocock `teach`** | `MISSION.md`, grounded lessons, learning records |
| “Do not let me move ahead until I actually pass” | **naeemdev360 `learn-anything-skill`** | Deterministic course state/gate script and tutor rubric |
| “Make sure I can recall/apply it independently later” | **Nar101 `learn-anything`** | Rubric before answer, transfer + delayed retrieval |
| “I want a full graphical app, maybe offline” | **OpenEdu** or **OpenTutor** | Provider choices, persistence, operating system, privacy |
| “Learn from my PDFs while tracking citations and gaps” | **Nar101** or **vesperchinn** | Source-bound lessons and explicit unreadable content handling |

**None is proven to be the exact originally intended unnamed repository** without a screenshot/title/owner. Keep this as an *identified-candidates* file. No repo was installed or executed.

## Principles before adoption

1. **Initial diagnostic:** establish what the learner knows through a short skills/knowledge assessment; avoid forcing review of mastered material.
2. **Outcome contract:** define observable behaviors, domain, deadlines and what counts as success (e.g., independent problem set, project or oral explanation), not vague “become an expert.”
3. **Source provenance:** authoritative textbooks/docs, dated links, exact lesson references. For medicine, restrict factual scoring to approved curricular or current clinical sources and acknowledge educational limits.
4. **Adaptive lesson loop:** one learning segment → active recall/task → pre-stated rubric → feedback → retry/remediation → advance on evidence → schedule delayed review.
5. **Reliable state:** save progress and misconceptions locally with file access; no claim of background teaching in chat-only sessions.
6. **Cost/safety:** long lessons and model graders have token and bias costs; track false passes/false failures. No learning skill gets implicit shell privileges, permission to share private courseware, or ability to modify unrelated code.
7. **Accessibility:** if HTML dashboard is offered, test reading order, keyboard navigation, mobile scaling, focus and reduced motion. Course progress metrics are motivational aids, not clinical/educational licensure.

## Suggested one-prompt example to try manually after approving an appropriate skill

> Goal: I want to be able to independently solve, explain and retain [specific topic/skill] at [target level] by [date]. Start with a diagnostic, identify gaps, propose a source-grounded roadmap and success criteria. Teach one segment at a time. Ask me to retrieve and apply ideas rather than just read explanations. Grade against a rubric established in advance, explain mistakes, revisit weak prerequisites, and test transfer and delayed recall before treating a topic as mastered. Save progress across sessions only if my environment can actually persist it. Never claim mastery from reading alone, and never run untrusted code or change unrelated repositories.

**Archive cross-references:** [145 — original 40 Claude names](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md), [164 — verified GitHub owners](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md), [170 — Anthropic's official skills, a different catalog](170-ANTHROPIC-OFFICIAL-AGENT-SKILLS-FULL-CATALOG-AND-ADOPTION.md), [171 — Google's official skill catalog](171-GOOGLE-AGENT-SKILLS-175-AND-WORKSPACE-CATALOG.md), [182 — blind spot and leverage prompt](182-TWO-QUESTION-BLIND-SPOT-AND-HIGH-LEVERAGE-DECISION-PROMPT.md).

**Source limitations:** user described function but did not provide identifying media. Links/metadata were checked 2026-10-28 through connected GitHub and public repository documentation, and the selected skills were not personally tested for learning outcomes. This archive is research only, not an installation or endorsement.
