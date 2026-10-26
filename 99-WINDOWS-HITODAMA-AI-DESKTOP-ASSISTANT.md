# 99 — Hitodama for Windows: Voice AI Desktop Assistant and Workflow Inspiration

**Source:** user's exact typed lead **“windows + Hitodama”** (2026-10-26). **Verified official product** https://hitodama.in/ . This is a *Windows desktop agent and productivity app*, not confirmed as an animated background, a Hitodama visual effect, a GitHub repository, or an open-source project. The official site is the primary source; its advertised features and prices are **publisher claims**, not independently tested entitlements.

## What the official site advertises

| Feature | Described interaction | Engineering/UX significance |
|---|---|---|
| Voice computer agent | Spoken requests open apps and operate desktop tools | Permission-scoped computer use, action preview and safe failure modes |
| **Circle to Ask** | Hold `Ctrl+Shift`, circle content on the screen and ask about it | Region-select screenshot capture, OCR/vision and context-specific answer with consent |
| **Dictation** | Hold `Ctrl+Win`, speak; speech edits false starts and inserts final text | Push-to-talk, post-processing and text insertion; avoid unwanted microphone capture |
| Tasks and to-do | Create and manage planned work | Persistent state, reminders and explicit editing/review |
| Scheduled search and routines | Time-based tasks and app opening, e.g. open Unity and Spotify in morning | Scheduler, proper timezone, safe automation scope, idempotency and notifications |
| Search and desktop control | Search via voice and manage desktop contexts | URL security, trusted links and clear action boundaries |
| Dashboard/island | One surface for music, settings, tasks, clipboard, apps and wallpapers | Integrated command center, but no forced overfull UI |
| Configurable visual slots | Site calls them “five slots” for shaping agent appearance/behavior | User customization rather than assumed global visual identity |

## Source and practical cautions

- **Windows:** the publisher shows a downloadable Windows edition. Exact minimum Windows build, installer signature, supported PCs and availability should be verified before purchase/install.
- **Prices:** the same live marketing page contained *inconsistent one-time price/edition and Google API billing statements* during research (₹499/$14 versus a sample $9 receipt; free-tier versus billing-enabled Gemini key). **Do not quote one definitive price** without checking actual checkout, region and current terms.
- **Bring-your-own Gemini key:** the site says Gemini handles language and desktop tooling is local. A service key or paid-tier policy may incur provider charges; “one-time software purchase” does **not** imply free model usage for all users.
- **Screen and voice privacy:** Circle-to-Ask can expose private app content; dictation requires microphone permission and may process speech via an external AI provider. Review exactly what is uploaded, retained and logged.
- **Agent action security:** a tool that can type, open URLs, read clipboard or control apps can execute consequential actions. Require explicit approvals for deletion, purchasing, outbound messages, scripts, secrets, accounts and system changes.
- **Source-code status:** no verified official public GitHub repository or software license established here; do not say Hitodama is open source or treat the site as code download authorization.
- **Accessibility:** shortcut collisions, keyboard layouts, voice-disabled alternatives, cancel/undo and feedback are essential to a usable desktop overlay.

## Inspired independent project idea — not a clone

An optional **Windows personal desktop agent** built with existing project standards could combine: command palette, push-to-talk transcription, safe screenshot selection, task queue, local memory with deletion/correction controls, program launcher and scheduled workflows, and explicit tool permissions. Preserve a versioned rulebook, no stealth monitoring and no outside API by default without clear provider consent. This is a concept only—**nothing has been built, run or installed**.

## Reuse with other archive sections

[69 — Hermes Unified Control Plane](69-HERMES-UNIFIED-AGENT-ECOSYSTEM-CAROUSEL.md), [45 — Agent-Navigable Apps](45-AGENT-NAVIGABLE-APP-ARCHITECTURE.md), [56 — Security](56-AUTHENTICATION-JWT-REVOCATION-DEPENDENCY-SECURITY.md), [85 — URL Security](85-URL-PROTECTION-RESEARCH-SOURCE-REGISTER.md), [101 — ASCII Art (unrelated)](101-PURE-PYTHON-ASCII-ART-RESEARCH-NOTES.md).

**Not performed:** no installers, no API key, no demo login, no macOS/Linux port, no paid purchase, no account action. [Master Index](98-DESIGN-RESOURCE-CAROUSEL-MASTER-INDEX.md).
