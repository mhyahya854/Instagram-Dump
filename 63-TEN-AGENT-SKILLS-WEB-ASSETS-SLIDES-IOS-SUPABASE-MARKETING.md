# 63 — Ten Agent Skills: Web Assets, Slides, iOS, Supabase, Marketing and Design

**Captured 2026-10-26.** The original reel calls these “10 out of 10 skills,” describing a mix of tools, vendors, and open-source packages. **Verified repo** means public repository exists; **not** that the speaker named that exact fork or that code was installed.

## The ten dictated skill leads, in order

| # | Spoken name | Upstream / candidate | What it's useful for | Identity and guardrail |
| ---: | --- | --- | --- | --- |
| 1 | **Web asset generator** | https://github.com/alonw0/web-asset-generator | Generate consistent favicons, app icons and social preview images; often multiple sizes | **Matching named repo confirmed, exact speaker's package unverified.** Assets need originality, correct format/size, licensing and preview tests. |
| 2 | **Front-end slides** | https://github.com/zarazhangrui/frontend-slides | HTML/CSS/JS-based slide decks and presentations with editable layouts | **Strong named repo**, inspect scripts, fonts, exports and whether presentation must work offline. Also see https://github.com/BunsDev/frontend-slides-skills (alternative). |
| 3 | **iOS simulator skill** | https://github.com/conorluddy/ios-simulator-skill | Automated iOS simulator interaction/screen inspection for AI coding workflows | **Confirmed repo name, exact creator ambiguous**; **Apple simulator typically requires macOS/Xcode**, not Windows. For cross-platform iOS building see existing xtool entry; these are different functions. |
| 4 | **Supabase Skills** | https://github.com/supabase/agent-skills | Official database/Auth/Storage/Edge/Realtimes and Postgres best practices, RLS and query/operations guidance | **Official verified**. Skills give procedural knowledge; Supabase MCP has separate live project access. Read-only is preferable for initial exploration. |
| 5 | **Marketing skills** | Various catalogs, e.g. https://github.com/duncan-buildroom/freeskills | SEO, conversion, offer, copywriting, launch and measuring actual outcomes | **Exact reel pack unspecified**. Do not fabricate prices, testimonials, rankings, clients or conversion results. |
| 6 | **“Mills Design skill”** | **Likely Emil Kowalski's Design Engineering skill**: https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md | Motion restraint, perceived responsiveness, polish, feedback and interaction details | **Probable transcription correction**, exact clip phrase uncertain. Other independent “Mills” projects may exist. |
| 7 | **HyperFrames** | https://github.com/heygen-com/hyperframes | Render HTML-driven motion graphics to video | **Verified**. Renderer + agent workflow, not just one arbitrary animation button; check code, model/asset rights and export quality. |
| 8 | **Impeccable** | https://github.com/pbakaus/impeccable | Review and improve generic-looking UI, hierarchy, responsive polish | **Verified**, improvement must be measured with rendering, accessibility and brand rules. |
| 9 | **“Test skill”** | **Probably Taste Skill** https://github.com/Leonxlnx/taste-skill | Design direction; discourage stock AI patterns | **Likely**, not confirmed exact transcription. Do not silently equate an unrelated QA test skill with visual Taste. |
| 10 | **Find Skills** | skills.sh / Skills CLI: https://skills.sh/ and https://github.com/vercel-labs/skills | Discover a relevant skill instead of assuming all agents need all skills | **Verified ecosystem**, but any discovered skill requires source/permission/security audit. |

### Official descriptions, distinct from reel claims

**Supabase:** Its Agent Skills documentation says the agent checks current docs/changelog and accounts for RLS, views, migrations and performance. https://supabase.com/docs/guides/ai-tools/ai-skills . **Do not** infer installing a skill directly gives permission to mutate a live database. Supabase MCP authentication and operations are separate.

**Emil Design Engineering:** an actual skill in emilkowalski/skills emphasizing animation decisions, interaction details and usable “feel.” It is not a guarantee all produced UI will match Linear. https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md .

**iOS testing:** an iOS simulator agent skill isn't compatible with every Windows/Android device. For macOS workflows verify Xcode/simulator version, app bundle identifier, permissions and required test fixture before allowing UI actions. For remote sessions protect Apple IDs and developer certificates.

**Find Skills:** discovery command is **not safety approval**. Read SKILL.md and its scripts, install scopes, auto-updates and credentials first. No blanket install-all policy.

## How these fit together without making generic UI

First define an original product brief, user flow, design tokens and anti-patterns; then retrieve **one suitable component or art reference**, write/test the implementation, optionally add motion, review on actual devices and preserve outcomes.

A possible bounded workflow:
1. **Research**: look up actual design references for the user task, not “ten libraries to install”.
2. **Assets**: generate licensed favicons/OG images only where needed.
3. **UI**: use tailored visual direction and reviewed shadcn or 21st components.
4. **Behavior**: test working actions, errors, focus, touch and reduced-motion settings.
5. **Data**: use Supabase skill only for a Supabase app, with RLS and tested migrations.
6. **Video/marketing**: invoke HyperFrames or a slide renderer only for a project needing these outputs.
7. **Acceptance**: annotate actual tests, before/after and unresolved requirements; don't claim universal improvement from a viral ranking.

## Source/status summary

**Verified repos:** alonw0/web-asset-generator, zarazhangrui/frontend-slides, conorluddy/ios-simulator-skill, supabase/agent-skills, emilkowalski/skills, heygen-com/hyperframes, pbakaus/impeccable, Leonxlnx/taste-skill (as named project).

**Unconfirmed exactly as spoken:** “Mills Design”, “Test skill”, marketing pack owner, the chosen “web asset generator”, “frontend slides” and iOS simulator forks. Different projects can share names.

**Security:** no packages downloaded, software run, API tokens connected, Apple simulator accessed or server/database changed.

Related: [44 — Agent Skills](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md), [55 — Research](55-HERMES-AGENT-SKILLS-RESEARCH-CATALOG.md), [62 — Immersive Web MCP](62-IMMERSIVE-WEB-GSAP-TASTE-21ST-SHADCN-MCP.md), [19 — Skills](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md).
