# 115 — Tencent Octop: Self-Hosted, Multiuser AI Agent Orchestration

**Source:** screenshot 13, a social reel from account `skip_ci`. Exact creative claim: **“Tencent Open-Sources Octop, a Free ChatGPT Alternative”**. Visible marketing paragraphs claim “no subscription, no cloud account, no monthly fee,” a single process bridging WeChat, Telegram, Discord and more apps, per-family-member agents/personas, dashboard, “one command” install, 6,000+ stars and MIT license, and ability to completely replace paid AI subscriptions. These are **reel statements**, not independent tests or economic guarantees.

## Canonical verified software

- GitHub **https://github.com/TencentCloud/Octop**
- Docs **https://docs.octop.cloud/**
- Repo description **“A smarter, self-hosted AI assistant — multi-user, multi-agent.”**
- Main architecture (README): Python/FastAPI backend, local SQLite control plane by default (Postgres optional), React UI, connector/channel gateway, agent harness, memory, scheduling, RAG/skills, ACP bridging and desktop clients (varying platform/release readiness).
- Channels listed include Telegram, Discord, Feishu, DingTalk, QQ, WeChat, WeCom; individual integrations can require service credentials/approved bot accounts and service limitations.
- Product claims MIT-licensed code. **Actual third-party model providers, connectors and bundled plugins may have different terms**.

## Critical “fully local” clarification

Self-hosting the **agent control plane, user database and app** does **not** make arbitrary remote models local. Official provider documentation supports hosted APIs for Google Gemini, Anthropic, OpenAI, Qwen and others **and local Ollama**. Cloud provider calls can transmit prompts, files and metadata outside your machine. You must choose local providers and disable external integrations to keep inference fully local.

No subscription for **Octop source** does not mean models, GPU electricity, provider keys, third-party connectors, hosting or account usage are free.

## Security boundary of a multiagent desktop platform

- Restrict admin dashboard to authenticated/trusted interfaces; no open internet binding without proper TLS, firewall, MFA/access controls.
- Limit each persona's filesystem, shell, browser, credentials, tools, network and external chat channel scopes.
- Prevent cross-family/cross-user conversation/memory leaks and secrets exposure through “shared experts”/connector configuration.
- Scheduler runs unattended, so set resource budgets, idempotent task runs, failure alerts and explicit user approvals for consequential actions.
- Remote browser/desktop control is powerful; avoid ambient admin access, malicious prompt injection and raw screenshot sharing with third-party channels.
- Beware publisher's **pipe remote install script into shell** examples. Inspect downloaded scripts and pinned commit/digest first; no unaudited one-liner installation on a personal main PC.

## Why it may matter to your archive

Complement/compare [69 — Hermes](69-HERMES-UNIFIED-AGENT-ECOSYSTEM-CAROUSEL.md), [99 — Hitodama](99-WINDOWS-HITODAMA-AI-DESKTOP-ASSISTANT.md), [27 — AI Agent Devices](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md) as *control plane + communications + memory + scheduling*, not “replace ChatGPT for free” as a proven statement.

## Evidence gap

The reel is a sales-style static screenshot. No Octop dashboard inspected, integrations authenticated, performance/privacy audited or self-hosted app launched. Source: https://github.com/TencentCloud/Octop and https://docs.octop.cloud/en/guides/llm-providers .
