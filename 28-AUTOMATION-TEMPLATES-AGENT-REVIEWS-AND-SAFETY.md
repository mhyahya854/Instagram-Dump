# 28 — Workflow Templates, Agent Code Review, Human-Mediated Safety

Captured: 2026-10-25. The clips describe a mix of GitHub repositories, slash commands, no-code templates and claims of autonomous performance. All references **research only**.

## “100 days of making you an engineer”, Day 13 (Hindi-English translation)

Spoken: “First, check three things. This is Day 13 in 100 Days of Making You an Engineer. First is /code-review: Claude Code reads your new code and identifies bugs; if you write --fix, it may fix them. Second, /security-review: it checks potential ways attackers might enter your app, such as password leaks, login bypass and SQL injection; the speaker says this is already built in. Third, my favorite: CodeRabbit.”

**Correction:** Slash-command availability, flags and default plugin inclusion **depend on actual Claude Code version/configuration**. Do not assume `/code-review`, `/security-review` or `--fix` always exist or that edits have passed a test just because the agent says they were fixed. Use project-approved code review, diffs, tests and explicit merge approval.

**CodeRabbit**: https://www.coderabbit.ai — GitHub PR review integration; review suggestions, don't let a reviewer auto-merge an unsafe change.

## 13,000+ n8n workflows: reuse, don't blindly trust

**Official index:** https://n8n.io/workflows/ ; **13,708 templates** displayed when checked in October 2026 (time-dependent).

**Concept:** a workflow is a directed graph: trigger → fetch/transform/classify → branching → action. For email sorting:
1. Gmail inbox trigger or scheduled poll for new message IDs.
2. Read sender, subject/body under authorized Gmail scope.
3. Optional classifier outputs a small valid category with confidence.
4. Guard against duplicates, spoofed instructions in email text and sensitive attachments.
5. Apply or propose one Gmail label to authorized messages.
6. Store processing history, monitor failures, allow manual override.

**Reel references to “2,000+ workflows GitHub collection” and “280 hand-picked workflows”** are not uniquely identified; many forks/mirrors exist. Don't invent canonical authors. A JSON export may omit credentials, but it can still contain **secrets in inline fields, sensitive URLs, or dangerous JavaScript and HTTP nodes**. Never paste/run third-party workflow JSON before review.

### Workflow safety checklist

- Review owner/license/last update and every node/credential scope.
- Inspect embedded scripts, curl/HTTP requests, outbound domains, webhooks, community nodes and AI prompt injection surfaces.
- Use a sandbox inbox/test spreadsheet and fake data first.
- Require approval for external sending, bulk deletions, sharing, payments and irreversible actions.
- Verify retry/idempotency so the same incoming message doesn't trigger duplicate actions.
- Keep a working kill switch, cost/rate limits, error alerts and data deletion policy.

## Handify AI: handwriting presentation vs authentic submissions

The reel presents **Handify AI** as a service that converts typed text to a handwriting-style document. Official site and product identity were not conclusively verified in this pass. A handwriting font **does not demonstrate handwritten authorship**; use only where assignment rules allow generated handwriting and disclose assistance when required. For legitimate design use, check legibility, pages, printer margins and accessible alternatives.

## Open source software vs “free” hype

The reel's “agent is free with ads” lacks a named service. No privacy or price conclusions are possible without inspecting its terms. Do not connect email, repo credentials or personal files to an unidentified advertising-supported agent.

## Website and app page completeness

**Checklist Design:** https://www.checklist.design/ contains real checklists for mobile apps, web apps, websites, screens, components and flows, including blog, 404, login, payments and onboarding. The reel mocks an agent claiming everything was shipped while omitting blog and 404 pages. Define routes/page inventory **before coding** and test required pages, internal links and fallbacks in the deployed build.

Suggested acceptance table: required route; actual route; critical blocks; interactive actions; mobile pass; accessibility pass; metadata; reviewer evidence. **Not every site needs a blog**: checklist must come from project scope, not a generic page list.

## Agent review acceptance

- Read the **actual code diff**; distinguish review advice from lint, tests, build and security scan results.
- Validate business-level invariants, especially authZ, RLS, race conditions, file uploads and data loss.
- Have the coding agent report exactly what commands/tests ran and which were not run.
- Never treat a GitHub repo, test badge, chat transcript or promotional headline as a security guarantee.

Related notes: [14 — Project Handoff](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md), [20 — Security Hardening](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md), [22 — UX Prelaunch](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md).

## The “AI video editor made 6 videos a day” and “instant workflows” claims

Both are creator promotional anecdotes. For credible reuse of automation, maintain sample data, expected outputs, task ownership and actual production runtime metrics. Verify third-party workflow JSON before any Gmail or account connection. Disentangle *one-click copying* from *safe deployment*.
