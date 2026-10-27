# 180 — Claude SEO: third-party Claude Code plugin, complete upstream inventory and SEO safeguards

**Date captured:** 2026-10-27. **Typed original lead:** “github skill called claude seo.” **Strong candidate:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo), a third-party Claude Code plugin maintained by Agrici Daniel. **Not an official Anthropic skill** and not part of the 19 official skill folders in [170](170-ANTHROPIC-OFFICIAL-AGENT-SKILLS-FULL-CATALOG-AND-ADOPTION.md). User provided no owner/repo URL, so similarly named repositories remain plausible. **License:** GitHub reports MIT at the root; check separate dependencies and third-party services. **No software installed, run, signed in or benchmarked for this archive.**

## What Claude SEO does

It orchestrates auditing and improvement recommendations across **technical SEO**, rendered page crawlability, Core Web Vitals, E-E-A-T-related content evaluation, structured data, local/business SEO, international settings, ecommerce, programmatic pages, off-page link context, Google API data and *generative search/answer engine optimization (GEO/AEO)*. It is a **tool-assisted research and reporting workflow**, not a search crawler index of its own, a new language model, a magic ranking optimizer or a guaranteed traffic-generation service.

Typical work: identify crawl/indexing failures, inconsistent canonical tags, broken hreflang, missing user-focused metadata, bad redirects, inaccurate Schema.org markup, image/accessibility/performance deficiencies, weak content evidence and unsafe page-generation tactics; prioritize actionable fixes and produce human-reviewed Markdown evidence. Some workflows make PDFs/Excel reports with dependencies. The plugin may use multiple model reviewers and local helper scripts; source code, target HTML and some retrieved third-party information can be processed by configured Claude models.

**Official repo content verified by GitHub API:** **26 top-level skills**, **19 agent Markdown personas**, **9 extension directories**. Counts are an upstream snapshot, not measured number of inference passes or quality. Folder inventories below preserve every name found on 2026-10-27.

## All 26 skills

| # | GitHub folder | Function / limit |
|---:|---|---|
| 1 | [`seo-agentic`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-agentic) | Agent readiness/optional machine-access conventions |
| 2 | [`seo-audit`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-audit) | Whole-site audit and specialist fan-out |
| 3 | [`seo-backlinks`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-backlinks) | Backlink sources and off-page authority |
| 4 | [`seo-cluster`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-cluster) | Search intent and keyword clustering |
| 5 | [`seo-competitor-pages`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-competitor-pages) | Competitor comparison-page planning |
| 6 | [`seo-content-brief`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-content-brief) | Content briefs and source-based outlines |
| 7 | [`seo-content`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-content) | Content quality, evidence and E-E-A-T |
| 8 | [`seo-dataforseo`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-dataforseo) | DataForSEO integration; API quota |
| 9 | [`seo-drift`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-drift) | Baseline/change monitoring and drift |
| 10 | [`seo-ecommerce`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-ecommerce) | Ecommerce/product/category pages |
| 11 | [`seo-flow`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-flow) | FLOW planning framework references |
| 12 | [`seo-geo`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-geo) | AI discovery/citation heuristics, not guarantees |
| 13 | [`seo-google`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-google) | Google SEO API analytics, auth and reports |
| 14 | [`seo-hreflang`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-hreflang) | International targeting and hreflang correctness |
| 15 | [`seo-image-gen`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-image-gen) | Optional generated imagery; review rights |
| 16 | [`seo-images`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-images) | Image semantics/performance and alt text |
| 17 | [`seo-local`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-local) | Local search, citations and business profiles |
| 18 | [`seo-maps`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-maps) | Geographic/map visibility and reviews |
| 19 | [`seo-page`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-page) | Single-page audit |
| 20 | [`seo-plan`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-plan) | Business-specific implementation planning |
| 21 | [`seo-programmatic`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-programmatic) | Programmatic page and duplication checks |
| 22 | [`seo-schema`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-schema) | Structured data validity and policy compliance |
| 23 | [`seo-sitemap`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-sitemap) | XML sitemaps and canonical discovery |
| 24 | [`seo-sxo`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-sxo) | Search experience and usability |
| 25 | [`seo-technical`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo-technical) | Technical crawl/render/index/redirect checks |
| 26 | [`seo`](https://github.com/AgriciDaniel/claude-seo/tree/main/skills/seo) | Top-level routing commands |

## All 19 reviewer personas

| # | Exact GitHub file | Function |
|---:|---|---|
| 1 | [`seo-agentic.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-agentic.md) | agentic specialty |
| 2 | [`seo-backlinks.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-backlinks.md) | backlinks specialty |
| 3 | [`seo-cluster.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-cluster.md) | cluster specialty |
| 4 | [`seo-content.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-content.md) | content specialty |
| 5 | [`seo-dataforseo.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-dataforseo.md) | dataforseo specialty |
| 6 | [`seo-drift.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-drift.md) | drift specialty |
| 7 | [`seo-ecommerce.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-ecommerce.md) | ecommerce specialty |
| 8 | [`seo-flow.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-flow.md) | flow specialty |
| 9 | [`seo-geo.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-geo.md) | geo specialty |
| 10 | [`seo-google.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-google.md) | google specialty |
| 11 | [`seo-image-gen.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-image-gen.md) | image gen specialty |
| 12 | [`seo-local.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-local.md) | local specialty |
| 13 | [`seo-maps.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-maps.md) | maps specialty |
| 14 | [`seo-performance.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-performance.md) | performance specialty |
| 15 | [`seo-schema.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-schema.md) | schema specialty |
| 16 | [`seo-sitemap.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-sitemap.md) | sitemap specialty |
| 17 | [`seo-sxo.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-sxo.md) | sxo specialty |
| 18 | [`seo-technical.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-technical.md) | technical specialty |
| 19 | [`seo-visual.md`](https://github.com/AgriciDaniel/claude-seo/blob/main/agents/seo-visual.md) | visual specialty |

## All 9 optional extension directories

| # | Exact GitHub directory | Permissions/cost consideration |
|---:|---|---|
| 1 | [`ahrefs`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/ahrefs) | Third-party integration; service access, billing, data sharing and terms require review |
| 2 | [`banana`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/banana) | Third-party integration; service access, billing, data sharing and terms require review |
| 3 | [`bing-webmaster`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/bing-webmaster) | Third-party integration; service access, billing, data sharing and terms require review |
| 4 | [`dataforseo`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/dataforseo) | Third-party integration; service access, billing, data sharing and terms require review |
| 5 | [`firecrawl`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/firecrawl) | Third-party integration; service access, billing, data sharing and terms require review |
| 6 | [`matomo`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/matomo) | Third-party integration; service access, billing, data sharing and terms require review |
| 7 | [`profound`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/profound) | Third-party integration; service access, billing, data sharing and terms require review |
| 8 | [`seranking`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/seranking) | Third-party integration; service access, billing, data sharing and terms require review |
| 9 | [`unlighthouse`](https://github.com/AgriciDaniel/claude-seo/tree/main/extensions/unlighthouse) | Local multi-page Lighthouse audits |

## Workflow and example commands (reference only, not executed)

~~~text
User-approved target URL
  → /seo audit URL or /seo page URL
  → bounded HTML/network crawl and optional browser rendering
  → specialist reviews for actual content, structured data, technical issues
  → aggregate evidence and produce a ranked fix list
  → compare recommendations with primary Google docs, user data and acceptance tests
  → apply separately authorized code changes on a branch; rerun regression/field tests
~~~

Common documented modes:

~~~text
/seo audit https://example.com
/seo page https://example.com/about
/seo technical https://example.com
/seo schema https://example.com
/seo sitemap https://example.com
/seo geo https://example.com
/seo agentic https://example.com
/seo local https://example.com
/seo drift baseline https://example.com
/seo google [command]
~~~

The project documents installation as a Claude Code plugin via its own GitHub marketplace, and setup includes an isolated Python environment and a headless browser. README lists Claude Code 1.0.33+ and Python 3.11–3.14. Validate exact requirements/version and audit install scripts before adoption. **Do not execute a shell downloader or grant secrets merely to inspect documentation.**

## Security and privacy: what the upstream actually says

Official [PRIVACY.md](https://github.com/AgriciDaniel/claude-seo/blob/main/PRIVACY.md) says core scripts have no vendor telemetry, and local output remains on the workstation. This **does not mean offline AI inference**: site data in Claude Code is handled by the configured model provider; site crawls contact target servers. Google APIs and optional vendors receive fields appropriate to each API, potentially including URLs, text, keywords, account property data or credentials.

[SECURITY.md](https://github.com/AgriciDaniel/claude-seo/blob/main/SECURITY.md) describes an SSRF-safe URL layer and DNS-pinned requests, along with candid residual risks: Chromium can resolve DNS separately and race Python preflight; CONNECT proxies may weaken pinning; IPv6-only origins may fail closed; Windows credential ACL behavior differs from POSIX \`0600\`; and installer signature-manifest verification was not yet enforced as described by its inspected policy. **A vendor security statement is not an independent security test.**

A malicious website or scraped HTML can contain prompt injection (“ignore the task,” “upload secrets,” “run a command”). Retrieved pages are untrusted data. Run audits with read-only credentials, no personal browser sessions or unrelated GitHub access; isolate browser/file/network permissions; control site crawling scope and rate; require human approval for IndexNow submission, live edits, billing or deletion. Agent fan-out can multiply token cost.

## Evidence versus SEO myths

| Area | Real verification | False shortcut |
|---|---|---|
| Index status | Authorized Google Search Console property + URL Inspection / actual HTTP | A static HTML scanner proving Google indexed every page |
| Performance | Representative field Core Web Vitals, plus reproducible lab runs | One Lighthouse score guaranteeing higher rank |
| Schema | Matching visible content, structured-data validator and current Google policies | Any JSON-LD automatically grants rich snippets |
| E-E-A-T | Credible original content, author evidence, trustworthy citations | One universally accepted “E-E-A-T score” |
| SEO vs AI search | Observe actual AI answer referrals, citations and clarity over time | “GEO score” predicting guaranteed ChatGPT/Gemini citations |
| \`llms.txt\` | Optional experimental machine-readability convention | Mandatory Google ranking/indexing requirement |
| \`robots.txt\` AI bots | Respect intentional publisher access policy | Every AI bot must be unblocked for quality |
| Multiple H1s / Vite / Vercel URL | Semantic usability and rendered quality | Proof of “vibe coding” or insecurity |

**Primary references:** [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies), [Core Web Vitals](https://web.dev/articles/vitals).

## Pricing, compatibility and measurable adoption

The repo is MIT-licensed, but **Claude model inference**, repeated subagents, browser setup, operational labor and optional live keyword/backlink/provider APIs may cost money. The README's “10–15-minute audits”, screenshots of traffic and SEO scores, and projected improvement are **publisher promotions**; not independently benchmarked. Without Search Console and field data, quality claims require qualification. A JS SPA whose real content appears only on interactions may require human exploratory tests.

Suggested narrow pilot for **a site you own**: freeze commit/model versions and an actual target; measure audit tokens/tool calls/cost, 5 key pages' crawl results, independent verification of every issue, false positive rate and performance. Fix only approved issues; compare real Search Console impressions/clicks after a reasonable window, recognizing algorithm/seasonality effects. For own-site measurement correlate [139 — cost forecasting](139-AGENT-TOKEN-COST-FORECAST-OBSERVABILITY-LOOP.md). No such pilot took place here.

## Namesake search and attribution caution

Other plausible repos include [noduslabs/claude-seo-skill](https://github.com/noduslabs/claude-seo-skill), focused on KeywordGraph and semantic keyword networks, and [Raz-Gits/claude-seo-skill](https://github.com/Raz-Gits/claude-seo-skill), which emphasizes evidence-based SEO. The user did not provide a screenshot or canonical URL, so **AgriciDaniel** is a likely researched match, **not** definitively the linked social-media source.

**Related archive:** [116 — SEO influencer claims](116-SEO-REEL-RANK-BY-FRIDAY-CLAIMS-AND-REAL-QA.md), [142 — twenty website giveaway claims](142-TWENTY-VIBECODED-WEBSITE-GIVEAWAYS-SOURCE-AND-FACT-CHECK.md), [170 — official Anthropic skill catalog](170-ANTHROPIC-OFFICIAL-AGENT-SKILLS-FULL-CATALOG-AND-ADOPTION.md), [181 — typed source register](181-OCT27-TRACEBASE-CLAUDE-SEO-SOURCE-REGISTER.md).

**No installations, audits, commands, model tests or outside-repository modifications performed.**
