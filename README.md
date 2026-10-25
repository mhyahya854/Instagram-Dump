# Instagram Dump

Personal, evolving design, UX, vibe-coded app and production engineering notes. Collected from spoken transcripts, normalized cautiously, and grouped by category.

**Core principle:** avoid generic AI-generated clichés, build real usable products, prevent real technical failures, and consider advanced patterns only when justified by the project.

## Rulebook files

| File | Scope |
| --- | --- |
| [01 — Design & UX](01-DESIGN-UX.md) | UX laws, visual anti-patterns, UI features and design references |
| [02 — Vibe-Coded App Quality](02-VIBE-CODED-APP-QUALITY.md) | Authenticity, functioning demos, product completeness and launch readiness |
| [03 — Production & System Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md) | Deployment, security, databases, distributed systems, performance, reliability and tests |
| [04 — Design Style Library](04-DESIGN-STYLE-LIBRARY.md) | Visual aesthetic vocabulary, **not** mandatory styling |
| [05 — Things to Find](05-THINGS-TO-FIND.md) | Original discoveries, eight user-approved catalog selections, open leads and skill scanning |
| [06 — AI Failure Mitigation Repositories & Skills](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md) | 68 verified GitHub repos mapped to design, app-quality and production failure modes |
| [07 — 45 UX Laws (English Reference)](07-45-UX-LAWS-ENGLISH.md) | Translated Hindi Instagram excerpts, 30-source principles + 15 researched additions, explicit uncertainty notes |
| [08 — Agent Repositories & Skill Wishlist](08-AGENT-REPOS-AND-SKILL-WISHLIST.md) | Agency Agents, Agent Reach, Hallmark, gstack, Serena, Task Master and skill wishlist; verified versus uncertain sources |
| [09 — Sessions, Security & AI Risk](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md) | Server sessions vs JWT, refresh revocation, authorization, API cost abuse, security scanners, image privacy |
| [10 — Database Transactions & Migrations](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md) | ACID, race conditions, idempotency, production migrations, backup/restore, safe recovery |
| [11 — Data Pipeline Quality](11-DATA-PIPELINE-QUALITY.md) | Source-to-destination count reconciliation, null keys, duplicates, freshness, publish gates |
| [12 — Marketing, Pricing & Homepages](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md) | Launch routine, distribution, first value, verified proof, pricing economics |
| [13 — Design Interactions & Icon Styles](13-DESIGN-INTERACTIONS-ICON-STYLES.md) | Hierarchy, color proportion, menu safe triangle, consequence-based modals, icon style taxonomy |
| [14 — Project Handoff & Agent Workflows](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md) | App specification: goal, user, flows, stack, permissions, done, test evidence |
| [15 — Hermes Agent Ecosystem](15-HERMES-AGENT-ECOSYSTEM.md) | GBrain, Skills Hub, Agent Reach, Open Design, Hermes Studio |
| [16 — Reel Source Register](16-INSTAGRAM-REELS-SOURCE-REGISTER.md) | All 23 reel segments mapped to detailed notes, claim corrections and offline-consolidation policy |
| [Transcription Notes](TRANSCRIPTION-NOTES.md) | Unclear phrases and tentative corrections retained transparently |

## Decision labels

- **Avoid by default unless explicitly requested:** anti-patterns, clichés and nonfunctional ornament.
- **Prevent / verify:** genuine defects such as broken production configuration, privilege bypass, leaks, fake form success, or irrecoverable backups.
- **Consider / employ when relevant:** optional features, genuine usability rules, technologies and architecture patterns.
- **Reference only:** design styles and inspiration sources; listing a style is not a request to implement it.

## Boundaries

- Visual aesthetics are **not** the same as software security or system design.
- An informational site does not need every feature (e.g. accounts, site search, Kafka, or multi-tenancy).
- When the user explicitly requests an otherwise avoided visual treatment, that project-specific choice takes precedence.
- Preserve original wording where possible and flag uncertain transcription instead of inventing a formal rule.
- Avoid fake reviews, fake metrics, unverifiable social proof and fake demos.
- Test real functionality in production-like environments, not just screenshots or a local development server.

_Last organized: 2026-10-25._

## Offline-first archive principles

The October 25, 2026 user-supplied Instagram reel batch is organized into **nine separate topic/source Markdown files (08–16)** rather than merged into a single giant document. Every topic contains a plain-English definition, retained example, failure modes, applicability/guardrails, and source links. See [16 — Reel Source Register](16-INSTAGRAM-REELS-SOURCE-REGISTER.md) for the 23-clip coverage map, uncertainties, claim verification and the policy for any future, user-requested consolidation.

- **Knowledge must remain intelligible without links.** A URL is provenance, not the only explanation.
- **Original spoken claims are not automatically facts.** Distinguish research-confirmed projects, incomplete transcriptions, historical marketing claims, and corrected security/engineering explanations.
- **Do not merge now.** Keep clear file boundaries; preserve Git history and issue dates for later comparison.
- **Not a software mirror or fully offline executable stack.** Upstream source, dependencies, models and licenses would require separate authorized preservation.
- **Research approval ≠ install permission.** No third-party skills or repositories from these notes have been installed or executed by this archival task.
