# GitHub Repositories & AI Agent Skills for Preventing Common AI-Built App Failures

_Last curated: 2026-10-25._

> **Discovery reference, not an installation script.** These public repositories were checked for existence through the connected GitHub account. Existence is **not** proof of quality, safety, ongoing maintenance or fitness for a specific project. No new items in this file are user-approved, security-cleared, installed or run. Existing user approvals are recorded separately in [05-THINGS-TO-FIND.md](05-THINGS-TO-FIND.md).

## Additional reel-derived references

- [08 — Agent Repositories & Skill Wishlist](08-AGENT-REPOS-AND-SKILL-WISHLIST.md): Agency Agents, Hallmark, Agent Reach, gstack, Task Master, Serena, specific skill wishlist and provenance.
- [09 — Sessions & Security](09-IDENTITY-SESSIONS-SECURITY-AND-AI-RISKS.md): JWT revocation, authorization matrices, cost abuse and scanners.
- [10 — Database Transactions & Migrations](10-DATABASE-TRANSACTIONS-AND-MIGRATIONS.md): ACID, concurrency, idempotency, restore-tested backups, production isolation.
- [11 — Data Pipeline Quality](11-DATA-PIPELINE-QUALITY.md): row counts, null keys, duplicates and freshness publish-gates.
- [13 — UI Interactions & Icons](13-DESIGN-INTERACTIONS-ICON-STYLES.md): anti-slop and icon style vocabulary.
- [14 — Agent Project Handoff](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md): goals, users, flows, stack, boundaries, acceptance criteria.

## Scope and selection rules

The goal is to cover the existing three rulebook categories with GitHub tools **and** agent skills that counteract mistakes made by AI-generated apps: (1) design/UX clichés, inaccessible UI and broken mobile/interaction states; (2) fabricated product content and incomplete functionality; (3) production security, backend reliability, testing and deployment. This is a broad curated inventory, **not an exhaustive inventory of GitHub**.

- **Agent skill:** instructions that steer a coding assistant; not a deterministic test or guarantee.
- **Tool / library:** executable technology that requires appropriate integration, tests and permissions.
- **Guideline / reference:** criteria for review; does not fix code automatically.
- **Use when relevant:** do **not** install the complete collection, or force a tool or pattern into an unrelated project. Match the stack and failure mode.
- **Review trust boundaries:** inspect scripts, transitive dependencies, required credentials and network access before using any outside skill or tool; use [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) where appropriate and manually review findings.
- **User approval vs security review:** the approved eight previously discussed items are approved **as choices for this catalog**, not automatically approved for privileged execution.
- **Not a substitute for real tests:** a skill can suggest an audit, but the actual build, integration, browser, security and deployment checks must be executed and assessed.

## Coverage by failure mode

| Typical AI-generated failure | Most relevant group |
| --- | --- |
| Purple gradient, generic three-card landing page, invented style | A; see rulebook [01](01-DESIGN-UX.md) |
| Beautiful screens but inaccessible buttons/forms/mobile | B |
| Fake demos, untested user journeys or misleading success states | B + C; authenticity policy in [02](02-VIBE-CODED-APP-QUALITY.md) |
| Agent overengineering, incomplete tasks, unverified changes | C |
| A skill silently reading credentials or manipulating the agent | D |
| XSS/SSRF, leaked API keys, dependency and cloud misconfiguration | D + E |
| Wrong Python APIs, input assumptions and untested edge cases | F |
| RLS bypass, slow SQL, broken schema changes, API contract drift | G |
| Production-only bugs, missing metrics, untested load and CI failures | H |


## A. Design direction and anti-generic UI (Category 1)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`anthropics/skills`](https://github.com/anthropics/skills) | Agent skills | Frontend design and artifact-building guidance | Generic, template-like visual output |
| [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) | Agent skill + UI audit | Visual critique, design workflows, deterministic frontend checks | Purple gradients, repetitive cards, low-quality hierarchy |
| [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) | Agent skills | Design-taste direction and UI auditing | Repetitive AI visual clichés; verify against our rules |
| [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Agent skills | Frontend engineering, browser testing, security, review, launch workflows | Beautiful but brittle or inaccessible AI-written apps |
| [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Agent skill | Searchable palettes, UI styles and UX rules | Arbitrary, inconsistent design decisions |
| [`podo/design-agent-skills`](https://github.com/podo/design-agent-skills) | Agent-skill directory | Find focused design, accessibility, content and motion skills | Installing huge overlapping skills sets blindly |
| [`aladicf/better-web-ui`](https://github.com/aladicf/better-web-ui) | Agent skills | Design hierarchy, typography, empty states, interactions | Generic visual layouts and incomplete states |
| [`PyModel/react-frontend-skills`](https://github.com/PyModel/react-frontend-skills) | Agent skills | React/Next.js UI, testing, current APIs, performance | Outdated React patterns and inconsistent frontend work |
| [`ryktara/design-engineering-skill`](https://github.com/ryktara/design-engineering-skill) | Agent skill | Context-sensitive design engineering across platforms | Applying one template to every project |
| [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) | Agent skills | Web-design-guidelines and React best-practices skills | Accessibility, React/Next.js, and web-performance misses |

## B. Real UI behavior, accessibility and product completeness (Categories 1–2)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`vercel-labs/web-interface-guidelines`](https://github.com/vercel-labs/web-interface-guidelines) | Reference + audit source | Interaction, accessibility, form and layout guidelines | Pretty UI with poor semantics, feedback, keyboard support |
| [`storybookjs/storybook`](https://github.com/storybookjs/storybook) | Component workbench | Develop/test individual components and visual states | Missing loading, empty, error, disabled and success states |
| [`microsoft/playwright`](https://github.com/microsoft/playwright) | Browser E2E framework | Functional tests in real browsers and viewport sizes | Fake demos, broken navigation, forms, mobile behavior |
| [`microsoft/playwright-mcp`](https://github.com/microsoft/playwright-mcp) | Agent-browser bridge | Let an agent inspect and interact with pages via browser | Claiming success without testing rendered behavior |
| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | Accessibility engine | Automated accessibility checks | Obvious detectable accessibility errors |
| [`pa11y/pa11y`](https://github.com/pa11y/pa11y) | Accessibility CLI | Automated site/page a11y testing | Uncaught accessibility regressions |
| [`GoogleChrome/lighthouse`](https://github.com/GoogleChrome/lighthouse) | Performance/a11y audit | Performance, accessibility and SEO checks | Slow loading, poor Core Web Vitals and some a11y issues |
| [`radix-ui/primitives`](https://github.com/radix-ui/primitives) | Accessible component primitives | Build custom-styled interactive controls with proper behavior | Broken keyboard focus and inconsistent dialogs/menus |
| [`tailwindlabs/headlessui`](https://github.com/tailwindlabs/headlessui) | Headless accessible components | Behavior without forcing a visual aesthetic | Nonfunctional menus/dialogs; styling remains project-defined |
| [`shadcn-ui/ui`](https://github.com/shadcn-ui/ui) | Component source + patterns | Reusable components to customize deliberately | Reinventing basic controls; avoid default-template aesthetics |
| [`react-hook-form/react-hook-form`](https://github.com/react-hook-form/react-hook-form) | Form-state library | Reliable validation feedback, submit and error states | Broken form state and misleading success feedback |
| [`colinhacks/zod`](https://github.com/colinhacks/zod) | Schema validation | Typed boundary validation for appropriate TypeScript stacks | Inconsistent client/server input schemas |
| [`mswjs/msw`](https://github.com/mswjs/msw) | API mocking for tests | Test network failures and alternate API responses | Missing offline/error/empty states |
| [`vitest-dev/vitest`](https://github.com/vitest-dev/vitest) | Test runner | Fast JavaScript/TypeScript unit and component tests | Untested UI logic and regressions |

## C. Agent planning, review and workflow discipline (Categories 2–3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`obra/superpowers`](https://github.com/obra/superpowers) | Agent skills | Structured planning, implementation and testing workflows | Agent rushing to code without a plan |
| [`mattpocock/skills`](https://github.com/mattpocock/skills) | Agent skills | Code reviews, problem isolation, specifications, testing workflows | Weak debugging, missed acceptance criteria |
| [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) | Agent skill | Keep changes surgically scoped and verifiable | AI overengineering, unnecessarily broad changes |
| [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | Third-party agent skills | Simplicity, think-before-coding, focused edits | Unneeded abstractions and excessive code; not official Karpathy publication |
| [`pengelbrecht/ticks`](https://github.com/pengelbrecht/ticks) | Issue tracker + skill | Tracked tasks and epics across agent sessions | Lost tasks or half-finished work |
| [`agentskills/agentskills`](https://github.com/agentskills/agentskills) | Format specification | Evaluate portable SKILL.md skill structure | Unclear skill packaging and interoperability |

## D. AI-agent and skill supply-chain security (Category 3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`NVIDIA/SkillSpector`](https://github.com/NVIDIA/SkillSpector) | Skill scanner | Review agent skills for prompt injection and exfiltration risks | Malicious skills collecting keys or leaking data |
| [`trailofbits/skills`](https://github.com/trailofbits/skills) | Security agent skills | Security review, diff auditing, threat/entry-point analysis | AI overlooking attack paths or risky code changes |
| [`snyk/agent-scan`](https://github.com/snyk/agent-scan) | Agent/MCP scanner | Scan MCP/agent integrations for documented security issues | Untrusted agent tools and servers |
| [`promptfoo/promptfoo`](https://github.com/promptfoo/promptfoo) | LLM test/security tool | Evaluate prompts and adversarial behaviors | Prompt injection and untested LLM behavior |

## E. Application, dependency and infrastructure security (Category 3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`semgrep/semgrep`](https://github.com/semgrep/semgrep) | Static analysis | Pattern-based code checks and custom detection rules | Known classes of injection, auth and code mistakes |
| [`gitleaks/gitleaks`](https://github.com/gitleaks/gitleaks) | Secret scanner | Scan repository/commit history for exposed credentials | Leaked API keys and tokens |
| [`trufflesecurity/trufflehog`](https://github.com/trufflesecurity/trufflehog) | Secret scanner | Discover and help validate exposed secrets | Secrets in repos and other scanned surfaces |
| [`aquasecurity/trivy`](https://github.com/aquasecurity/trivy) | Vulnerability/misconfiguration scanner | Scan images, dependencies and infrastructure | Unpatched packages and insecure container configs |
| [`google/osv-scanner`](https://github.com/google/osv-scanner) | Dependency vulnerability scanner | Check dependencies against OSV advisories | Known vulnerable open-source packages |
| [`ossf/scorecard`](https://github.com/ossf/scorecard) | Supply-chain assessment | Evaluate open-source dependency security posture | Blind trust in external repositories |
| [`OWASP/ASVS`](https://github.com/OWASP/ASVS) | Security verification standard | Define testable application security requirements | Authorization, validation, session and API gaps |
| [`OWASP/CheatSheetSeries`](https://github.com/OWASP/CheatSheetSeries) | Security reference | Implementation guidance for CSRF, SSRF, XSS, uploads, auth | Reinvented or unsafe security mechanisms |
| [`zaproxy/zaproxy`](https://github.com/zaproxy/zaproxy) | Web security testing tool | Authorized web-app dynamic scanning | Web-layer vulnerabilities missed by static checks |
| [`bridgecrewio/checkov`](https://github.com/bridgecrewio/checkov) | IaC static analysis | Check cloud, IaC and deployment configurations | Exposed buckets, overly permissive infra settings |

## F. Python correctness, tooling and maintainability (Categories 2–3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`astral-sh/ruff`](https://github.com/astral-sh/ruff) | Python linter/formatter | Static checks, formatting, error-prone patterns | Sloppy, inconsistent Python code |
| [`astral-sh/uv`](https://github.com/astral-sh/uv) | Python package/project manager | Reproducible Python dependencies and environments | Environment drift and dependency confusion |
| [`pytest-dev/pytest`](https://github.com/pytest-dev/pytest) | Python test framework | Automate correctness checks | Changes breaking previously working behavior |
| [`HypothesisWorks/hypothesis`](https://github.com/HypothesisWorks/hypothesis) | Property-based testing | Generate unexpected inputs and edge cases | Agent assumptions about perfect inputs |
| [`pydantic/pydantic`](https://github.com/pydantic/pydantic) | Data validation library | Validate typed data at boundaries | Malformed payloads and unchecked input |
| [`pre-commit/pre-commit`](https://github.com/pre-commit/pre-commit) | Local hook framework | Run formatters, lint and selected scanners before commits | Known easy-to-catch defects entering Git |

## G. Databases, migrations, transactions and API contracts (Category 3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`prisma/orm`](https://github.com/prisma/orm) | TypeScript ORM | Typed database queries and migrations when this stack fits | Unsafe schema drift and brittle query integration |
| [`sqlfluff/sqlfluff`](https://github.com/sqlfluff/sqlfluff) | SQL linter | Consistency and SQL correctness checks | Unreadable and inconsistent SQL |
| [`ankane/pghero`](https://github.com/ankane/pghero) | PostgreSQL performance tool | Inspect slow queries, indexes and connection issues | N+1 patterns, slow SQL and missing indexes |
| [`ankane/strong_migrations`](https://github.com/ankane/strong_migrations) | Rails migration guard | Catch risky migrations in Rails/Postgres stacks | Blocking or unsafe database migrations |
| [`supabase/supabase`](https://github.com/supabase/supabase) | Backend stack + docs | Postgres/Auth/RLS patterns for Supabase apps | Missing auth/RLS policy discipline; tests still essential |
| [`testcontainers/testcontainers-node`](https://github.com/testcontainers/testcontainers-node) | Integration test framework | Real disposable databases/services in tests | Passing tests against unrealistic mocks |
| [`pact-foundation/pact-js`](https://github.com/pact-foundation/pact-js) | Contract testing | Consumer/provider API compatibility verification | Frontends/backends breaking each other's contracts |

## H. Performance, deploys, monitoring and reliability (Category 3)

| Verified GitHub repository | Type | How it helps | AI-built failure addressed |
| --- | --- | --- | --- |
| [`grafana/k6`](https://github.com/grafana/k6) | Load-test framework | Test API performance and throughput | Production load failures |
| [`locustio/locust`](https://github.com/locustio/locust) | Load-test framework | Python-driven concurrency and workload tests | Unmeasured capacity or latency |
| [`getsentry/sentry`](https://github.com/getsentry/sentry) | Error monitoring | Capture and triage runtime errors | Silent production failures |
| [`open-telemetry/opentelemetry-collector`](https://github.com/open-telemetry/opentelemetry-collector) | Telemetry infrastructure | Process traces, metrics and logs | Undiagnosable multi-service failures |
| [`open-telemetry/opentelemetry-js`](https://github.com/open-telemetry/opentelemetry-js) | Telemetry library | Instrument JavaScript services/clients | Missing traces and useful telemetry |
| [`grafana/grafana`](https://github.com/grafana/grafana) | Observability dashboards | Visualize operational metrics and alerts | Blind spots after deployment |
| [`prometheus/prometheus`](https://github.com/prometheus/prometheus) | Metrics/alerting system | Collect time-series operational metrics | No service health/SLO visibility |
| [`hadolint/hadolint`](https://github.com/hadolint/hadolint) | Dockerfile linter | Catch Docker build and security anti-patterns | Fragile production container builds |
| [`actions/starter-workflows`](https://github.com/actions/starter-workflows) | CI workflow examples | Build/test/security checks in GitHub Actions | Code merges with no automated checks |
| [`renovatebot/renovate`](https://github.com/renovatebot/renovate) | Dependency update automation | Managed dependency update PRs | Long-lived vulnerable or outdated dependencies |
| [`dependabot/dependabot-core`](https://github.com/dependabot/dependabot-core) | Dependency update engine | Automated dependency update support | Neglected dependency maintenance |

## Adoption and audit workflow

1. Start from a *concrete bug or product need* and pick **one skill and one testing/scanning tool**, not every item in a group.
2. Check primary README, release dates, license, compatibility, known issues, dependencies, and whether the project is actively maintained.
3. For agent skills, read **the exact skill content**, scripts and linked files; scan before running. External skills are untrusted instructions.
4. For production-impacting tools, perform a scoped dry run (where possible) in staging, without exposing live secrets or customer data.
5. Record command outputs, failing tests and measured behavior; never substitute a generated summary for actual evidence.
6. Classify any selection as **Discovered → Reviewed → Tested → Approved for project → Installed**; the user's earlier approval is **catalog approval**, not execution permission.
7. Retain the user's existing [anti-pattern defaults](01-DESIGN-UX.md) even if a third-party skill advocates trendy visual styles.

**Notes:** Some entries are overlapping alternatives (axe-core versus Pa11y; k6 versus Locust; Renovate versus Dependabot; Radix versus Headless UI). Treat them as choices, not a combined mandatory stack. The original unresolved dictated names remain in [05-THINGS-TO-FIND.md](05-THINGS-TO-FIND.md) for historical traceability; this inventory deliberately favors concrete verified repositories rather than forced transcription matches.


## Second reel batch: new references, NOT included in the original 68 count

- [17 — Component Sites](17-DESIGN-WEBSITES-AND-COMPONENT-LIBRARIES.md): official reference links and uncertainty notes.
- [19 — Skills and Hooks](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md): Apple Design, CodeRabbit, GSD, SlopMonster, hooks.
- [20 — Security/OSI](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md) and [23 — Data Backfills](23-DATA-BACKFILLS-REPLAY-AND-IDEMPOTENCY.md): deeper defensive tests and replay safety.

No new entries have been automatically approved, security-cleared or installed.
