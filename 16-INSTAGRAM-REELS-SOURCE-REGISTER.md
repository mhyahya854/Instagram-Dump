# Reel Source Register — 2026-10-25 Batch

## Archive policy for the hypothetical “internet no longer exists” scenario

This repository is a **human-readable, self-contained interpretation archive**. Each topic file must explain terminology, rationale, examples, failure conditions and application checks *inside the Markdown text*; URLs and star counts are optional provenance, **not the only place where knowledge lives**. Distinguish verbatim user-supplied fragments from paraphrase and from independent research. When later combining into a large unified document, preserve provenance and conflicts instead of flattening every clip into “truth.”

**Not guaranteed:** This archive cannot preserve the entire internet, original video visuals or all source-code dependencies. It records these supplied spoken clips and verified context only.

## Clip index and destinations

| # | Reel topic / opening remembered | Normalized gist | Detailed file |
| ---: | --- | --- | --- |
| 01 | Rick/Morty “Agency Dash Agents” | 230+ role-based agent personas; structured instruction files | [08](08-AGENT-REPOS-AND-SKILL-WISHLIST.md) |
| 02 | “Agent Reach ... internet Claude can't normally read” | Platform-specific internet tools with login and support caveats | [08](08-AGENT-REPOS-AND-SKILL-WISHLIST.md), [15](15-HERMES-AGENT-ECOSYSTEM.md) |
| 03 | Fired employee still logged in | Server sessions vs JWT; refresh, revocation and authorization | [09](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md) |
| 04 | Goran: 4-step app-marketing routine | Directory launches, daily content, short landing page, quick value | [12](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md) |
| 05 | Claude startup pricing skill | Price based on value/cost/market economics, not magic fixed tiers | [12](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md) |
| 06 | Bad cover homepage vs clear good one | Immediate offer, visitor goals, CTA, verified proof | [12](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md) |
| 07 | “vibe coded apps hacked / $20K AWS bill” | Rate limits, server secrets, permissions matrix, abuse budget | [09](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md) |
| 08 | Green pipeline missing orders | Row-count, null, duplicate, freshness checks before publish | [11](11-DATA-PIPELINE-QUALITY.md) |
| 09 | Long AI design slop anti-pattern list | Borders/eyebrows/monospace/glass/neon/fake proof defaults | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md), [01](01-DESIGN-UX.md) |
| 10 | Five free security tools | Supabase advisors, TruffleHog, Security Guidance, OSV, Observatory | [09](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md) |
| 11 | Hermes five-tool stack | GBrain, Skills Hub, Agent Reach, Open Design, Hermes Studio | [15](15-HERMES-AGENT-ECOSYSTEM.md) |
| 12 | Desired installable skills | Ponytail, Matt Pocock, Superpowers, design, diagrams, etc. | [08](08-AGENT-REPOS-AND-SKILL-WISHLIST.md) |
| 13 | Icon categories | Pixel, glyph, outline, material, dimensional, adaptive, animated, etc. | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |
| 14 | AI deletes production DB during referral addition | Migrations, restore-tested backups, safe rollout/rollback | [10](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md) |
| 15 | Boss says website looks like “slop” | Impeccable, unknown AwesomeDesigns.fd, Hallmark | [08](08-AGENT-REPOS-AND-SKILL-WISHLIST.md), [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |
| 16 | Send button + repeated money transfer | ACID, race conditions, row locking and idempotency | [10](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md) |
| 17 | “Build a golf app” vague handoff | Goal, target user, core flows, stack, scope, boundaries, done | [14](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md) |
| 18 | Geo-locate photo with GPS removed | Photo appearance can reveal location independent of EXIF | [09](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md) |
| 19 | “One hero, two support” hierarchy | One prominent element with quiet supporting information | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |
| 20 | “60-30-10” color | Optional color-distribution heuristic, not a mandated palette | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |
| 21 | “10 out of 10 GitHub repos” | Ponytail, UI UX Pro Max, gstack, Taskmaster, Serena, Superpowers, Trail of Bits and unclear names | [08](08-AGENT-REPOS-AND-SKILL-WISHLIST.md) |
| 22 | Invisible triangle in hover menus | Intent corridor to submenu prevents accidental closing | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |
| 23 | Don't design generic “Are you sure?” modals | Clear action verbs, readable alignment and meaningful consequences | [13](13-DESIGN-INTERACTIONS-ICON-STYLES.md) |

## Provenance classification

- **[U] User-supplied transcript:** words and examples came from the user-provided clip transcription; no original video opened.
- **[R] Researched repository/technical docs:** primary project sources checked on 2026-10-25; links stored locally in each note.
- **[I] Interpretation:** corrected sound-alike names, consequences or usability application; not asserted as exact reel wording.
- **[?] Unresolved:** missing creator, clip source, wording, repo or numerical claim; preserve gap.

## High-impact corrections before future consolidation

1. A JWT is not automatically unrevocable; non-stateful access tokens need a revocation strategy.
2. A refresh-token revoke prevents new access tokens but may leave existing tokens valid until expiry unless access is separately rejected.
3. A database transaction alone does not prevent every concurrency race; test locks/isolation/constraints/idempotency.
4. Not every schema migration has a safe inverse; plan backward-compatible forward fixes and recovery separately.
5. Exact data row counts can be compared only if transformation/filtering rules justify equal counts.
6. Screenshot/visual similarity to a brand does not guarantee licensed reuse.
7. Marketing “one video beats paid ads,” security-study ratios, stars, claimed fortunes and effectiveness are anecdotal/unverified unless an independent method is supplied.
8. Scan scores (Mozilla, SkillSpector, OSV) cannot prove a full site secure.
9. Menu “hover triangle” is a pointer-specific solution; touch and keyboard require separate accessibility patterns.
10. Icon styles are vocabulary; no requirement to use one style everywhere, and generic Lucide/emoji ubiquity remains avoided.

## Offline consolidation policy (for a future user-directed merge)

- Keep individual Markdown sources **immutable snapshots** or maintain versioned history in Git.
- Preserve source identifiers, confidence grades, worked examples, caveats and issue dates.
- Merge duplicate ideas by canonical concept, but keep contradictory claims with provenance and resolution.
- Prefer embedded definitions and procedures to “go read this URL”; for external code, source URLs alone are **not offline execution archives**.
- A truly offline execution bundle would require separately authorized snapshotting of specific upstream repos, licenses, dependencies, toolchains, models, sample data and reproducible tests; **this task creates knowledge notes only**, not those software mirrors.
