# 69 — Hermes Agent: All-in-One Skills, Memory, Automation and Messaging (7-Slide Screenshot Capture)

**Source:** eight sequential user-uploaded carousel screenshots dated 2026-10-26. Captions/UI are **creator-generated illustrations**, not an audited live Hermes installation or a commitment that each feature exists in every release or deployment. Previous notes: [15 — Hermes](15-HERMES-AGENT-ECOSYSTEM.md), [27 — Device Tools](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md), [30 — Agent Harness](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md).

## Screenshot-by-screenshot semantic transcription

| Slide | Visible heading / claims | Transferable system architecture idea |
| ---: | --- | --- |
| **1** | “The thing I like about Hermes is how much is already under one roof.” Skills, MCPs, files, browser, chats, agents and scheduled tasks live inside the same setup; fewer separate tools to manage. Diagram merges a **skills app, MCP config, file manager, browser tool and cron jobs** into one Hermes screen showing Skills, MCPs, Files, Browser, Chats, Agents, Scheduled Tasks. | **One control plane:** centralize configuration/navigation across agent tools while isolating their permissions. |
| **2** | “You don’t have to build every capability yourself.” Boxes marked built-in: **computer use, automations, image generation, task planning, delegation, text-to-speech**. “Decide what your agent should do.” | Discoverable capability catalog and task delegation instead of custom integration for every feature; verify actual availability and providers. |
| **3** | “Memory is where Hermes gets really useful.” Without memory, repeated questions; with memory example: **works in marketing**, **reports: 1 page, summary first**, **tone: casual, no jargon**, **main clients: 3 retainers**. “Same job every week → already has context.” | Durable preferences and project-specific records, with source/date/authorization and correction/deletion controls. These sample details are **illustrative, not user facts**. |
| **4** | “Hermes can also get better at those jobs over time.” Week 1 correction: **put summary at top**; week 2: **use client template**; week 3: **always add sources**. Becomes a reusable **client-report** process (summary on top, client template, add sources). | Promote repeatedly approved corrections to a versioned reusable skill or workflow. Don't automatically “learn” misinformation or override the user. |
| **5** | “Take Hermes away from your computer.” Telegram/Slack interactions send a task while user is out; desktop host does work and replies when done. Example: research three competitors before 3pm and return pricing/news summary. | Channel-agnostic task queue with explicit authentication, allowed actions, timeouts, results, and sensitive-data limits. Phone/chat channel alone does not grant desktop or production permission. |
| **6** | “Have work happen without messaging it first.” Examples in slide: **morning brief daily 07:00**, **competitor research Monday 09:00**, **weekly report Friday 16:00**, **inbox summary daily 18:00**; outputs arrive without repeated user prompt. | Scheduler/cron with timezone, reliability, deduplication, permissions, receipts, retries and cancellation. Slide's times are examples only—not tasks to schedule for the user. |
| **7** | “Hermes worth looking at.” Diagram connects **Memory, Tools, Skills, Automations, Communication, Agent Workflows** to Hermes; “all together”. | Unified user-facing product with isolated, observable action services and durable preference/workflow state. |

*Source count:* The user supplied **seven blue-grid Hermes screenshots**: unified setup, capabilities, memory, reusable workflow, external messaging, recurring jobs and summary diagram. Each row numbered 1–7 represents exactly one screenshot. Screenshots are user-uploaded source material, not audited proof of installation. Use seven as the real source count.

## Core capability model to retain

```text
USER (desktop / Telegram / Slack)
  → message and approval gateway
  → identity, tool scope and task policy
  → HERMES WORKFLOW ORCHESTRATOR
      ├─ memory + vetted preferences
      ├─ reviewed skills / templates
      ├─ permission-scoped MCP / connectors
      ├─ browser and computer controls
      ├─ files/search
      ├─ task planner + delegated workers
      └─ scheduler / durable job queue
  → observable tool results, checkpoints, audit, notifications
```

Each skill's code and input documents remain **untrusted**. Do not install executables or grant browser, filesystem, Telegram/Slack, Gmail/Calendar, GitHub or cloud access merely because a carousel shows a green checkmark.

## Reusable workflow: turn corrections into expertise

1. Ask user for explicit approved task preferences and verify scope/project relevance.
2. Track corrections as versioned **candidate rules**, with timestamps, source and context.
3. Consolidate duplicates carefully without confusing client-specific tasks with global preferences.
4. Encode repeatable behavior in a small skill/task recipe with inputs, expected outputs and acceptance tests.
5. Test on fake/safe examples and ask for approval before recurring automated posting, deletion, customer messaging or billing.
6. Permit user revision/revocation; don't silently learn secrets or private client data from every message.

## Scheduled-job and messaging safety

- Explicit owner approval, timing/timezone, recipient/channel, frequency and stop behavior.
- Least-privilege Slack/Telegram integration and verified account identity; no auto-sending sensitive notes to arbitrary chat IDs.
- Idempotent jobs, capped retry, concurrency policy, logs redacted, budget and monitoring.
- Scheduled research must verify fresh sources; a user's personal brief could include private records not suitable for group channels.

## What is *not* verified from the carousel

Hermes exact version/provider, “built-in” feature availability, actual model costs, persisted memory internals, Telegram/Slack security properties, 24/7 host availability, first-try job accuracy, security/certification and whether any tasks were actually executed.

**Related:** [15 Hermes Ecosystem](15-HERMES-AGENT-ECOSYSTEM.md), [30 Harness](30-AGENT-HARNESS-REPOS-GITHUB-PRESENTATION.md), [45 Agent-Navigable Apps](45-AGENT-NAVIGABLE-APP-ARCHITECTURE.md), [51 Workflow Proposals](51-UNIVERSAL-RULES-RESEARCH-PROPOSALS.md).

## Fourteenth source batch — Tencent Octop comparison lead

[115 — TencentCloud/Octop](115-TENCENT-OCTOP-SELF-HOSTED-MULTIAGENT-CLAIMS.md) is a distinct multi-user agent shell/control plane with messaging, memory, scheduler, web dashboard and local/remote model providers. Self-hosted app state **does not guarantee local LLM inference**, and the Instagram claim “free replaces ChatGPT” is not established. Compare Hermes and Octop feature/version maturity and security scopes before deployment.

## Fifteenth collection — distinct memory and browser agent strategies

[126 — JEV and Browser Use](126-JEV-ULTRAFAST-AND-BROWSER-USE-AGENT-OPERATION-GUIDE.md) documents a bounded browser-action loop and high-risk existing-profile access; [127 — Graft Candidates](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md) includes repo memory plus enterprise/API agent tools; [129 — Agent Memory](129-AGENCY-AGENTS-AGENT-MEMORY-OPENMONTAGE-VISUAL-CARDS.md) records the source visual and conceptual split between temporary context and durable evidence-backed knowledge. Don't assume these are Hermes official modules.
