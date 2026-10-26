# 128 — Clicky: AI Screen Companion, Plus Other GitHub Projects Named Clicky

**Source:** user's typed phrase **“someone made something called clicky”** with no accompanying URL, video or description, 2026-10-26. A name match alone cannot identify the specific project. Two unrelated public GitHub matches were verified. Both descriptions below come from each project's README; **neither has been installed, executed or granted computer access**.

## Candidate A (probable visual/agent-related match): Farza's Clicky

**Official open-source repo:** https://github.com/farzaa/clicky
**Current product link in README:** https://www.heyclicky.com/ (the old README also mentions `clicky.so` as its original download page).
**README statement updated April 27, 2026:** existing codebase remains MIT open source; the creator keeps **new development private**, and directs users to heyclicky.com for the latest product.

> “It's an AI teacher that lives as a buddy next to your cursor. It can see your screen, talk to you, and even point at stuff.”

### Capabilities and architecture cues

- Original Mac desktop companion beside cursor with screen/cursor context, interactive speech and pointers to UI elements.
- Supports explaining visible content, step-by-step help and task learning through a talking character/overlay.
- Its README describes setup with **Claude Code, Xcode and a Cloudflare Worker proxy** and the user's own API keys. It is **not** a trivial one-file fully-offline Windows app.
- Screen access + microphone + outbound model calls are significant privacy/consent concerns. Audit exact permissions, screenshot capture conditions, redaction and key handling.
- The archived MIT code does not necessarily reproduce the **current** commercial/private Clicky product, nor guarantee Windows/Linux support.

### How to adapt concepts safely, without cloning assets

A local “teach me this screen” mode could combine an explicit push-to-talk button, screenshot region selection, pointer target highlighting, user-owned notes and keyboard-accessible explanations. Never silently capture screens or record private credentials. Provide review before outbound uploads, allow cancel and clear history; don't install globally without explicit authorization.

## Candidate B (different product): Clicky security agent

**Repo:** https://github.com/goldenapplestudios/Clicky

README names it **“Clicky - If Claude were a Pentester”**, with multiple agents for scoped, authorized infrastructure security assessments and an MCP privacy gateway. This **does not** appear to be a cursor-teaching desktop assistant. It requires defined testing scope and permission. Do not use it to scan third-party systems and do not equate the project with Farza's Clicky.

## Unresolved identity

Without a source URL/reel, **candidate A is more plausible** in the context of the user's GUI/AI agent inspiration, but remains **probable rather than confirmed**. Preserve the exact phrase “someone made something called clicky”; do not claim that a particular screenshot displays either Clicky.

## Project ties

[99 — Hitodama](99-WINDOWS-HITODAMA-AI-DESKTOP-ASSISTANT.md) has a distinct Windows AI overlay; [126 — Jev/Browser Use](126-JEV-ULTRAFAST-AND-BROWSER-USE-AGENT-OPERATION-GUIDE.md) concerns live browser operation; [118 — Agentation](118-FIVE-HUNDRED-AI-AGENTS-AND-AGENTATION-UI-FEEDBACK.md) concerns DOM-aware visual feedback in development. Clicky is better categorized as **real-time UI tutoring/desktop overlay** rather than interchangeable with those.

**No software installed, external API called, screen or microphone accessed, computer controlled or user's other repositories edited.**
