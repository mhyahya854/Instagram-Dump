# 176 — Humaniser/Humanizer, Stop Slop and Affaan's agent ecosystem

**Typed input:** “affna repo”, “Humaniser”, “Stop Slop” (2026-10-27). Spellings kept exactly as supplied. **Main match for “affna” is researcher/maintainer Affaan Mustafa \`affaan-m\`, but the user supplied no owner URL.** Connected GitHub confirmed specific upstreams below. No system configuration, agents or skills were installed; no scans executed.

## Humaniser / Humanizer — collision awareness

| Exact source/alternate | Independently located repo | Function |
|---|---|---|
| \`Humaniser\` (UK spelling) | **Unresolved which repository user means** | Generic class of editing workflows; name alone cannot identify publisher |
| \`Humanizer\` | https://github.com/blader/humanizer | Confirmed live MIT GitHub **agent skill** for revising generic, patterned AI writing |
| Other humanizer GitHub repositories | [Existing detailed comparison](161-HUMANIZER-GITHUB-REPOS-COMPARATIVE-RESEARCH.md) | Several unrelated prose editors and rewrite packages |
| \`Humanizer\` .NET library | Different software package | Text and data formatting/inflection, **not** editing to hide writing provenance |

### Useful editing process (not “undetectable AI” marketing)

1. Preserve the actual writer's facts, tone, intent, citations and names. Record version history and human decisions.
2. Diagnose template-like opening sentences, empty transitions, repetition, unnatural rhythm, excessive hedging and default AI promotional clichés.
3. Rework at semantic level: specific evidence, verbs, concrete examples, appropriate pacing, direct language, relevant voice.
4. Validate no invented personal experience, fake citations, altered medical/legal facts, plagiarism or unauthorized copying.
5. For academic, workplace or legal settings, follow disclosure/policy rules. **No repository guarantees an “undetectable” outcome or passes all detectors**; detectors themselves are imperfect and may misclassify human writing.

Avoid automatically rewriting official quoted transcripts in Instagram-Dump—preserve literal source and put stylistic edits in the research interpretation only.

## Stop Slop — distinct MIT editing skill

**Canonical repository:** https://github.com/hardikpandya/stop-slop ; confirmed MIT, not archived during audit. It ships a \`SKILL.md\` and reference examples/rules for reducing recognizable prose clichés and increasing directness and density. Many rules are **stylistic opinions** rather than correctness standards: forbidding all adverbs or all em dashes across every context can harm clarity, voice, literature or accessibility. Apply selectively; don't copy its prohibitions automatically into Universal-Rules.

**Review process:** run controlled A/B rewriting tasks with genuine human editorial assessment and verifiable fact preservation. Compare to \`blader/humanizer\` on factual error rate, readability, intended voice, semantic similarity and edit reversibility. Do not use success claims from AI-detector screenshots as reliable metrics.

## “affna repo” — probable Affaan Mustafa (\`affaan-m\`) catalog

**Verified maintainer profile:** https://github.com/affaan-m ; user wording “affna” is ambiguous, so distinguish **candidate maintainer** from exact source transcript. Major GitHub repositories directly verified:

| Repo | Actual function | Key risks |
|---|---|---|
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Everything Claude Code agent harness: skills, orchestration/memory, security and development workflows; MIT in live metadata | Broad prompt injection/skills supply chain, overlapping plugins, unmeasured token savings |
| [affaan-m/agentshield](https://github.com/affaan-m/agentshield) | AI agent configuration security scanner across secrets, hooks, MCP permissions, with CLI/GitHub Action; MIT | False positives/negatives; scan output may reveal keys; automatic fixes may change configs |
| [affaan-m/claude-swarm](https://github.com/affaan-m/claude-swarm) | Multi-agent Claude Code orchestration and TUI; MIT | Shell/model access, cost fan-out, merge conflicts |
| [affaan-m/JARVIS](https://github.com/affaan-m/JARVIS) | Agentic OSINT/research interface described by publisher | Privacy, surveillance ethics, external data handling, legal constraints |

**AgentShield specificity:** the project's README advertises secret scans, permission rules, hook/MCP checks, JSON/SARIF/HTML reports, GitHub Action and optional model-powered audit. These are source features, **not proof its vulnerability coverage is complete**. A config scanner cannot guarantee runtime isolation or absence of exploit chains; red-team evaluation and explicit human review matter. It may have opt-in model-assisted modes that send config content to an API—read exact privacy implications first. Never run \`--fix\`, \`init\`, \`--deep\` or cloud scanning merely for archiving.

**ECC adoption:** evaluate project-local skills and system prompts for conflicts against the established workflow, install only needed pinned modules, keep experiment rollback and trace actual tokens/quality. Its star counts, author claims, testimonials and marketing numbers are transient, not independent performance audits.

## Side-by-side recommendation by job

- **Prose polishing:** \`blader/humanizer\`, \`hardikpandya/stop-slop\` or a human editor, depending on genre. They are writing interventions, **not** security or identity-evasion tools.
- **Coding-agent behavior and workflows:** ECC; compare with [Superpowers](137-SUPERPOWERS-SKILL-CLAUDE-CODE-CODEX-AGENT-PLANNING.md) and [EGM](168-GOOGLE-ELEPHANT-GOLDFISH-MODEL-SPEC-DRIVEN-AGENTS.md).
- **Static agent-config review:** AgentShield with sandboxed synthetic project, not a replacement for pentesting or policy review.
- **Parallel orchestration:** claude-swarm or [Orca](172-MULTICA-LANGWATCH-ORCA-CODING-AND-AGENT-ORCHESTRATION.md), with carefully bounded permissions.

**Additional crosslinks:** [161 — original humanizer catalog](161-HUMANIZER-GITHUB-REPOS-COMPARATIVE-RESEARCH.md), [164 — ECCC/40 repo follow-up](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md), [170 — Anthropic skills](170-ANTHROPIC-OFFICIAL-AGENT-SKILLS-FULL-CATALOG-AND-ADOPTION.md). Source originals kept, no changes to Universal-Rules.


## Stop Slop confirmed again (new typed lead, 2026-10-27)

The user repeated the exact name **`Stop Slop`**, separately recorded in [184](184-OCT27-TWO-QUESTIONS-STOP-SLOP-UNDERSTAND-AGENT-BROWSER-REGISTER.md). The actual [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) `SKILL.md` was fetched in this follow-up: it advises cutting filler, formulaic contrasts, abstract claims and imitative quotables, using direct/active language, specific facts and varied rhythm. It also strongly discourages *all adverbs, passive voice and em dashes*. Those are **subjective writing constraints**, not universal quality or correctness principles; they can damage a text's meaning, genre, readability or original voice if applied blindly. Keep original transcripts verbatim and avoid claiming that this improves AI-detection scores or gives a provenance guarantee. No skill was installed, no Universal-Rules edit made.
