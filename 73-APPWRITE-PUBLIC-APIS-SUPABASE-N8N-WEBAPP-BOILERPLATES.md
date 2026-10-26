# 73 — Developer Discovery: Appwrite, Public APIs, Supabase, n8n and Web-App Boilerplates

**Source:** five separate keywords dictated by user on 2026-10-26: “github repos appwrite public apis supabase n8n boilerplate for webapps.” The screenshot carousel does **not** explain those products; the following descriptions are **independent current project research**. All listed GitHub repositories were existence-verified through connected GitHub.

## Original five leads

| Spoken | Canonical source | Category | What it can actually do |
| --- | --- | --- | --- |
| **Appwrite** | https://github.com/appwrite/appwrite ; https://appwrite.io/ | Backend-as-a-service/application infrastructure | Cloud/self-hosted authentication, database, Storage, Functions, messaging, Realtime and web hosting/Sites. Appwrite's storage backend/edition/version matters; don't assume all providers work identically. |
| **Public APIs** | https://github.com/public-apis/public-apis | Community-curated **directory**, not itself a hosted API | Links to APIs by category, usually with notes about keys/HTTPS/CORS. Each provider's docs, quotas, data rights and uptime differ; entries can go stale. |
| **Supabase** | https://github.com/supabase/supabase ; https://supabase.com/docs | Postgres-centered backend platform | Postgres database, Auth, Storage, Realtime, Edge Functions, admin tooling, auto-generated APIs and Row Level Security. Exposing a database with weak RLS is a common serious data breach risk. |
| **n8n** | https://github.com/n8n-io/n8n ; https://n8n.io/workflows | Workflow automation and integrations | Build/operate trigger→action workflows, AI nodes, webhooks, scheduled jobs, connectors, self-host/cloud. Can help orchestrate Appwrite/Supabase/API calls but is **not** by itself the main application backend. |
| **Webapp boilerplate** | https://github.com/ixartz/Next-js-Boilerplate ; https://github.com/vercel/nextjs-postgres-auth-starter | Starter apps/templates, not a hosting platform | Preconfigured code organization, auth and Postgres examples, tests, styles, CI, SEO and deployments depending on template. Audit every included service and version. |

## Critical licensing distinction: n8n is source-available, not OSI-open-source

As of October 2026, n8n's **Sustainable Use License** covers its free self-hosted community edition. Official FAQ explicitly distinguishes permitted internal agency workflows from allowing outside clients to edit/build workflows inside a hosted service. Some SaaS/white-labeling or client-facing custom-automation models need a commercial license. **Don't label the n8n backend as unrestricted MIT/Apache open source**.

Official: https://docs.n8n.io/sustainable-use-license/ and https://support.n8n.io/article/can-i-use-your-license-for-my-use-case .

## Appwrite vs Supabase: choose deliberately

**Appwrite:** broad product-ready application APIs with uniform SDK abstraction and self-host/cloud deployment, including auth, storage, messaging, functions and hosting. New versions can support multiple backend database engines; evaluate current documented version and backup/restore.

**Supabase:** best suited when you want direct PostgreSQL strength, SQL migrations, relational modeling, Postgres extensions, query access and Row Level Security. A service-role key must never be exposed to the browser. Every user's data access needs owner/tenant enforcement; test negative account cases.

**Neither substitutes for UI, business logic, backups, threat modeling or release tests.** Choosing one is usually sufficient for a simple product.

### Comparison

| Decision | Appwrite | Supabase | Build own backend |
| --- | --- | --- | --- |
| Fast auth/CRUD/storage | Designed for it | Designed for it | More code and security ownership |
| Relational SQL and direct Postgres logic | Depends on version/backing database and API | First-class Postgres approach | Fully controlled if you choose Postgres |
| Self-host | Yes, with ops | Yes, with ops | Yes, highest custom ops |
| Vendor SDK APIs | Yes | Yes | You define |
| Tenant permissions | Server-side Appwrite permissions and scopes | RLS policies, app service auth | Must implement independently |
| Risks | Server exposure, misconfigured project permissions and backups | Bad RLS, leaked service keys, SQL migrations | Custom auth bugs, missing monitoring, runtime cost |

## Public APIs: before integrating one

1. Pick the API's official documentation, not an aggregator's description alone.
2. Check authentication (none, API key, OAuth), data rights, regional availability, version and deprecation schedule.
3. Read quotas/rate limits, payload schemas, error codes, commercial-use and caching restrictions.
4. Store secret credentials server-side; never put API keys in browser bundles or public GitHub.
5. Use contract tests and mocked fixtures; design failure modes for outage and unexpected cost.
6. Don't treat an API directory listing as permission to scrape private data or avoid access controls.

## Starter templates: when they help / when they hurt

Examples verified:
- https://github.com/ixartz/Next-js-Boilerplate — a feature-rich Next.js/TypeScript/Tailwind/Drizzle starter with tests, agents guidance, optional monitoring and security integrations.
- https://github.com/vercel/nextjs-postgres-auth-starter — a leaner Next.js + database/auth template in the Vercel ecosystem.
- Supabase example applications within https://github.com/supabase/supabase .
- Appwrite template examples from its official docs: https://appwrite.io/docs .

**Risks:** starters can include unnecessary vendors, obsolete packages, insecure environment examples or unnecessary UX patterns. Review software license, package lockfile, build, tests, actual costs, deployment assumptions, privacy and permissions before adoption. **A template isn't a finished production app.**

## Example small product stack

For an authenticated personal journal with private entries:
- Frontend: accessible web UI in appropriate framework, or mobile native UI.
- Backend: **choose one** of Appwrite, Supabase, or a custom Rust API with Postgres/SQLite according to needs.
- Data: user-owned entries, attachments with per-user RLS/permissions, repeatable migrations and backups.
- Automation: n8n for selected approved reminders/exports, **not** to replace core database validation.
- External APIs: use a documented provider only when necessary.
- Security: scoped auth, permission tests, input validation, rate limits, secret storage, logs and restore drills.
- Verification: actual mobile/desktop flows, negative cross-account tests and real release checks.

This is an **illustrative architecture**, not an auto-selected stack or an instruction to migrate existing apps.

## Sources and status

https://github.com/appwrite/appwrite ; https://github.com/public-apis/public-apis ; https://github.com/supabase/supabase ; https://github.com/n8n-io/n8n ; https://github.com/ixartz/Next-js-Boilerplate ; https://github.com/vercel/nextjs-postgres-auth-starter .

All sources verified at GitHub; no new account, database, workflow, API key or paid service was created, installed or activated. Related [03 Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [28 Workflows](28-AUTOMATION-TEMPLATES-AGENT-REVIEWS-AND-SAFETY.md), [50 Engineering Guides](50-PROGRAMMING-SYSTEM-DESIGN-GUIDES-FREE-LLM-APIS.md).
