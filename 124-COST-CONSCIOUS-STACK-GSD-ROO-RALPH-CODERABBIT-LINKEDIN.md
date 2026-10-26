# 124 — Cost-Efficient Stack, AI Coding Workflow and LinkedIn Agent Skill

**Source:** screenshots #11–15 in the fifteenth Instagram batch (2026-10-26). The screenshots mix suggestions, app names, a repository image and detailed agent setup directions. Source claims are transcribed separately from fact checks.

## Screenshot 11 — four-line infrastructure and cost advice (exact)

```text
database → neon, not supabase (idle = $0)
hosting → cloudflare, not vercel (unlimited free bandwidth)
files → r2, not s3 ($0 egress)
build → claude code or codex ($20)
```

### Reality checks (not source text)

- **Neon** offers free-tier/Postgres autosuspend compute, not unlimited free production database capacity/storage or guaranteed all costs zero; current plans/limits need checking. See https://neon.com/pricing .
- **Cloudflare** has different pricing for Workers, Pages and other products, with usage/CPU/build restrictions. “Unlimited free bandwidth” is not unconditional for every use-case; examine current https://developers.cloudflare.com/workers/platform/pricing/ .
- **Cloudflare R2** does not charge egress, but storage, write/read operations and infrequent-access retrieval can be billable. Official docs https://developers.cloudflare.com/r2/pricing/ .
- **Claude Code or Codex $20** is a screenshot estimate, not a guaranteed current license/API bill or feature entitlement. Validate plan and usage before budgeting.
- Provider selection is project-specific: Neon and Supabase are not equivalent products in auth, realtime and storage; Cloudflare and Vercel have different runtime/deployment characteristics; R2 vs S3 hinges on egress, performance, compatibility and ecosystem.

## Screenshot 12 — exact tool list

```text
These 4 tools can seriously upgrade your AI coding workflow:
⚡ GSD— Better planning & execution
🤖 Roo Code — Multi-model AI coding
🔁 Ralph Loop — Long-running agent loops
🐰 CodeRabbit — AI-powered code reviews
```

### Verified GitHub/research sources

| Source | Canonical known reference | Scope / caveat |
|---|---|---|
| GSD | https://github.com/gsd-build/get-shit-done | Goal→spec/plan/implementation/verification sequencing; user approval + actual tests, not “no mistakes” |
| Roo Code | https://github.com/RooCodeInc/Roo-Code | **Original Roo Code extension/cloud/router shut down May 15, 2026**, confirmed by official repo/docs; **historical** screenshot recommendation, not a currently active official product. Community forks include Cline and ZooCode |
| Ralph Loop | https://github.com/snarktank/ralph | Autonomous iteration pattern and sample implementation; many unrelated Ralph forks; repeat until real passing exit criteria/budget, not unbounded loops |
| CodeRabbit | https://www.coderabbit.ai/ and https://github.com/coderabbitai | Commercial AI review service and official GitHub org, not a guarantee that every PR issue or bug is detected |

### Recommended engineering rule

Take a user goal → **PRD** (why, for whom, constraints, success criteria) → **Design document** (product behaviors/visual rules, responsive UX) → **Tech stack and architecture** (risk, versions, data/auth/deployment) → **bounded atomic implementation tasks** → automated unit/integration/E2E tests → adversarial review → user validation. Prevent silent rewriting of production data and require approval for disruptive operations. Stop loops at budgets and evidence-defined goals; no guessed “done”.

## Screenshot 13 — LinkedIn agent skill

**Visible screenshot repo owner/name:** `Jakeschincariol/linkedin-agent-skill`.

**Verified:** https://github.com/Jakeschincariol/linkedin-agent-skill . README offers **eleven skills** for post drafts, comment/reply drafts, profile feedback, planning, carousel outlines and “humanizer” heuristics. **Important provider-specific condition:** upstream itself says **it does not automatically post** to LinkedIn. LinkedIn automated browser posting may violate service rules and cause account restriction. Emphasize authentic facts, user approval and no fabricated metrics; an “AI detector score” is not proof text is human-written.

## Screenshots 14–15 — exact workflow transcript

The first partial screenshot (#14) reads:

```text
✅ PRD Docs — Explain your idea to an LLM, it will build the doc for you
✅ Design Docs — Copy any inspirational website URL and let AI generate it
✅ Tech Stack Docs — Do a little research and finalize your best stack
⚙️ Execution:
```

The second screenshot (#15) repeats those lines and continues:

```text
Upload all 3 files to your source folder
Paste the prompt in Antigravity
It will create a proper to-do list that executes one task at a time
🔐 Auth & Database:

Use Better Auth — copy home page URL & secret key → paste in
.env
Use Neon Database — copy database URL → paste in .env
Antigravity handles the rest!
🐛 Bug Fixing:

Install Code Rabbit on GitHub
It highlights all errors & bugs after every commit
```

### Critical correction: credential safety

Store user-managed Better Auth/DB keys ONLY in locally managed environment configuration **excluded from version control** and in production secrets managers with least privilege. **Do not copy secret keys into chat, into a public homepage, screenshots, shared PRD docs, a third-party web form, or this research repo**. Test DB URL role privileges, migrations/rollback, encryption, access control and real session behavior; a model cannot “handle the rest” without a specified acceptance suite.

“Copy inspirational website URL and generate it” must be limited to analyzing transferable design principles and permitted assets; it is not permission to clone copyrighted branding or scrape third-party private content.

**No software installed, migrations applied, secrets handled, third-party account connected or real project created.** Related [02 — Quality](02-VIBE-CODED-APP-QUALITY.md), [03 — Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [95 — Prompts](95-BETTER-VIBE-CODING-PROMPTS-SIX-SOURCES.md).
