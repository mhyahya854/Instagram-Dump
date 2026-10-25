# Things to Find — GitHub Repositories, AI Skills & Educational Projects

> **Status:** Research backlog and user-approved shortlist, **not** an installation manifest. Eight candidate entries below have the user's **catalog approval**; this is not a security audit, permission to execute, or confirmation of installation.
>
> **Source:** User's dictated list, 2026-10-24. Preserve raw names when voice transcription is uncertain. An identified candidate is not automatically the intended project.

## Related researched reels — new, not automatically approved

The [October 25 Agent Repository & Skill Wishlist](08-AGENT-REPOS-AND-SKILL-WISHLIST.md) documents newly found **Agency Agents**, **Agent Reach**, **Hallmark**, **gstack**, **Serena**, **Task Master** and the **Hermes ecosystem**; unresolved names are explicitly marked. The [Hermes ecosystem note](15-HERMES-AGENT-ECOSYSTEM.md) covers GBrain, Skills Hub, Open Design, Agent Reach and multiple similarly named Studio dashboards.

These are **catalog discoveries**, not installation approvals. Preserve the eight previously approved catalog selections in section 0 below.

## 0. User-approved strongest matches — catalog selection (2026-10-25)

**User-approved for keeping and considering in this repository, not approved for automatic installation or privileged use.** A probable transcription match stays marked probable even if selected.

| Original reference | Approved candidate | Identification confidence | Execution status |
| --- | --- | --- | --- |
| Ponytail | [`DietrichGebert/ponytail`](https://github.com/DietrichGebert/ponytail) | Confirmed | Not installed or security-audited here |
| Carpety Skills | [`multica-ai/andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | Strong likely transcription | Not installed or security-audited here |
| Math + Popo | [`mattpocock/skills`](https://github.com/mattpocock/skills) | Strong likely combined transcription | Not installed or security-audited here |
| Tick Skills | [`pengelbrecht/ticks`](https://github.com/pengelbrecht/ticks) | Probable | Not installed or security-audited here |
| UI UX programs | [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Plausible specific project | Not installed or security-audited here |
| Design Engineering | [`ryktara/design-engineering-skill`](https://github.com/ryktara/design-engineering-skill) | Plausible specific project | Not installed or security-audited here |
| Version Web guidelines | [`vercel-labs/web-interface-guidelines`](https://github.com/vercel-labs/web-interface-guidelines) | Probable Vercel correction | Reference only |
| Version Web design guidelines | [`vercel-labs/agent-skills`](https://github.com/vercel-labs/agent-skills) (`web-design-guidelines`) | Probable Vercel correction | Not installed or security-audited here |

### Scope of current search

Additional **verified GitHub tools and agent skills** grouped by the existing design, product-quality and production-engineering failures live in **[06 — AI Failure Mitigation Repositories & Skills](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md)**. There are 68 entries there, none automatically approved.

As requested, **pause the name-guessing search** for unclear spoken fragments such as KFM, Dropit Skills, MPEG-VLD Skills and EMFIM; retain them below as archival leads, not actionable recommendations. Python instead gets a concrete set of relevant test/lint/validation repositories in file 06.

## 1. Security-first: scan skills before installing

| As spoken | Identified project | Status | Link | Why it matters |
| --- | --- | --- | --- | --- |
| "Skill Specter" / NVIDIA scanner | **NVIDIA SkillSpector** | **Verified name + repository** | https://github.com/NVIDIA/SkillSpector | Scan untrusted AI agent skills for prompt injection, secret collection, exfiltration and supply-chain risks *before* installing. |

**Original anecdote retained:** NVIDIA's README includes an example report in which `scripts/sync.py:23` harvests environment variables and a later line posts to an external endpoint. **This is the repository's illustrative scan result, not independent proof that a particular third-party skill stole keys.**

**Safety review before any proposed installation:**
- Find the original author and canonical repository, inspect license, commits, dependencies, and exact skill files (including executable helpers/scripts).
- Pin to a specific reviewed commit/version; rerun scanning after updates.
- Run SkillSpector *before installation or execution*. Read its findings manually; a low risk score is not a guarantee of safety.
- Prefer least privilege, isolated environments, scoped credentials and no network access when not needed.
- **Privacy caveat:** By default, optional LLM analysis can send scanned file contents to the configured LLM provider. The dependency-vulnerability lookup can also send package coordinates to OSV.dev. Investigate `--no-llm` and network isolation if reviewing private code.
- **Do not execute, install, or auto-approve any candidate simply because it is listed here.**

## 2. AI agent skills — to research

| Original phrase | Possible identification | Confidence/status | Reference |
| --- | --- | --- | --- |
| Agent Skills | Anthropic's public skills collection and the Agent Skills specification | Verified examples; verify intended choice | https://github.com/anthropics/skills ; https://github.com/agentskills/agentskills |
| KFM | Multiple unrelated repositories use KFM. Example: `kongfoo-ai/KFM` is a large-language-model research repository with biomedical agent skills, **not confirmed as the user's intended one**. | **Ambiguous; candidate exists** | https://github.com/kongfoo-ai/KFM |
| Python | Python-oriented agent skills (category, not a unique named repository) | **Category only; no canonical match** | https://github.com/anthropics/skills |
| UI UX programs | **UI/UX Pro Max**: searchable design styles, palettes, typography, accessibility guidelines and stack-specific UI advice | **Repository verified; phrase match tentative** | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| Ponytail | **Ponytail** by DietrichGebert, AI coding agent skill/rules for minimal changes, review and testing without dropping safeguards | **Confirmed GitHub repository** | https://github.com/DietrichGebert/ponytail |
| Dropit skills | **dropit** Obsidian plugin by smart-kits found; transfers notes/media across devices and can optionally send incoming items to a local AI agent. **Not proven to be the spoken “Dropit skills”**. | **Related-name candidate only; exact skill repo unresolved** | https://github.com/smart-kits/dropit-obsidian |
| Carpety skills | **Andrej Karpathy Skills**: third-party rules for think-before-coding, simplicity, surgical changes and verification. Multiple implementations exist; NOT an official Karpathy release. | **Strong phonetic match; specific source unconfirmed** | https://github.com/multica-ai/andrej-karpathy-skills ; https://github.com/duolahypercho/andrej-karpathy-skills |
| Math | Likely first half of **Matt Pocock**. The transcript separated a name as “Math, Popo”. | **Strong combined phonetic match, unconfirmed** | https://github.com/mattpocock/skills |
| Popo | Likely second half of **Matt Pocock**, whose engineering skills cover debugging, testing, reviewing and specifications. | **Strong combined phonetic match, unconfirmed** | https://github.com/mattpocock/skills |
| Tick skills | **Ticks** (`pengelbrecht/ticks`), Git-tracked issue/epic tracker with a bundled `skills/ticks/SKILL.md`; possible alternative `tick-md` is a different project. | **Verified repo and skill; spoken match probable, not proven** | https://github.com/pengelbrecht/ticks ; https://github.com/Purple-Horizons/tick-md |
| Superpowers | `obra/superpowers` software-development skill collection | Verified candidate | https://github.com/obra/superpowers |
| More GitHub repos | Ongoing discovery backlog | Open-ended | — |

## 3. GitHub projects / educational repositories — to investigate

| Original phrase | Candidate / description | Status | Link |
| --- | --- | --- | --- |
| Gods Eye View | `AWardPublications/gods-eye-view`, public geospatial/3D globe console | Possible match; verify original source | https://github.com/AWardPublications/gods-eye-view |
| Paperclip | `paperclipai/paperclip`, agent team/task orchestration | Verified match | https://github.com/paperclipai/paperclip |
| Vibe Trading | `HKUDS/Vibe-Trading`, trading-agent project | Verified match; research only, no live trading | https://github.com/HKUDS/Vibe-Trading |
| Voice Studio | `voicestudiohq/voicestudio`, macOS AI voice skills/MCP/CLI | Possible match; name is not unique | https://github.com/voicestudiohq/voicestudio |
| OpenMAI C | **OpenMAIC**, multi-agent interactive classroom | Verified probable transcription correction | https://github.com/THU-MAIC/OpenMAIC |
| Magnitude | `magnitudedev/browser-agent`, vision-first browser automation | Probable match | https://github.com/magnitudedev/browser-agent |
| OpenCV | OpenCV computer-vision library | Known project, verify intended use | https://github.com/opencv/opencv |

## 4. Additional AI / interface-design skills — to research

| Original phrase | Candidate identification | Status | Link |
| --- | --- | --- | --- |
| Anti UI scope | **Anti-UI-Slop** | Likely transcription correction; multiple projects exist | https://github.com/tuanphung2005/anti-ui-slop ; https://github.com/uizze/uizze/tree/main/plugins/claude-directory/skills/anti-ui-slop |
| MPEG-VLD skills | Search did not find a credible AI-agent skill/repository under this exact phrase; technical results about MPEG video decoding are unrelated. | **Unresolved** | — |
| EMFIM | Search did not establish an AI-agent skill or GitHub project of this name. | **Unresolved** | — |
| Design Engineering | `ryktara/design-engineering-skill`: context-first UI/UX guidance across web, mobile, desktop, TV and kiosk; inspects existing code and verifies through rendering. Other similarly named projects exist. | **Verified candidate, intended source ambiguous** | https://github.com/ryktara/design-engineering-skill ; https://github.com/AgentsORG/design-engineering |
| Version Web guidelines | **Vercel Web Interface Guidelines**: living accessibility, interaction, animation, responsive, form and performance guidelines. | **Confirmed repo; likely transcription correction** | https://github.com/vercel-labs/web-interface-guidelines |
| Version Web design guidelines | **Vercel web-design-guidelines**: agent skill that fetches current Web Interface Guidelines and audits UI files. Related to the preceding repository, not a wholly independent design framework. | **Confirmed skill; likely transcription correction** | https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md |

## 5. Research workflow (not automatic installation)

For each lead, record:
1. **Exact original name** and **confirmed canonical owner/repository URL**, distinguishing confirmed, probable, possible or unresolved.
2. Purpose and category: educational repository, application, agent skill, tool, framework, or inspiration.
3. Compatibility with intended runtime and platform (Windows, macOS, Linux, Claude Code, Codex, etc.).
4. License, maintenance activity, dependency and execution risks, and network/secret access.
5. SkillSpector scan findings where relevant; manual review and isolation before any installation.
6. Overlap or conflicts with already adopted rules/skills.
7. Keep **catalog approval** separate from security/installation status: **Discovered → Reviewed → Scanned → Tested → Authorized for installation → Installed**. Catalog approval alone never advances the execution status.

## Notes on terminology

- **SkillSpector** (not "Skill Specter") is confirmed from NVIDIA's own GitHub repository.
- **OpenMAIC**, **Anti-UI-Slop**, and **Vercel** are suggested corrections of speech-to-text wording. Record original phrases for traceability.
- **Ponytail** is confirmed as `DietrichGebert/ponytail`. **Carpety → Karpathy Skills** and **Tick → Ticks** are strong/probable phonetic matches. **KFM**, **Dropit skills**, **MPEG-VLD skills**, and **EMFIM** still need an exact original source for identification. Do not upgrade a candidate into a confirmed match solely because the repository exists.
- A working public GitHub URL verifies a project exists, **not** that its code or skill is trustworthy.

## 6. Follow-up research — 2026-10-24

**No installation or execution performed.** Research-status terms: *repo confirmed* means a public project was found; *spoken match probable* is not identification proof; *unresolved* means do not fabricate a URL.

### Repo facts and compatibility

| Lead | Verified observation | Fit / limitation |
| --- | --- | --- |
| **Ponytail** | Maintainer `DietrichGebert`; `skills/ponytail/SKILL.md` plus `AGENTS.md`; adapters for Claude Code and Codex. | Useful for reducing needless implementation while retaining tests/security. Its performance statistics are project-authored claims, not independent validation. |
| **Karpathy Skills** | `multica-ai/andrej-karpathy-skills` packages coding-agent rules; `duolahypercho/andrej-karpathy-skills` adapts them for Codex. | Third-party distillations of Karpathy's ideas; not skills officially published by Andrej Karpathy. |
| **Matt Pocock Skills** | `mattpocock/skills` is an engineering-agent skills collection with spec writing, task decomposition, bug diagnosis, TDD and code review. | Strong transcription candidate for combined “Math, Popo”, not user-confirmed. |
| **Ticks** | `pengelbrecht/ticks` is an issue tracker; provides `skills/ticks/SKILL.md` and a Git-tracked task workflow. | Fits persistent planning between agent sessions; do not confuse with `Purple-Horizons/tick-md`. |
| **UI/UX Pro Max** | Repo includes searchable UI/UX guidance, multiple stacks and design systems, supporting Claude Code/Codex. | Candidate for the UI/UX phrase; must not override this repository's anti-cliché rules by default. |
| **Design Engineering** | `ryktara/design-engineering-skill` inspects actual apps, emits context-sensitive design guidance, and includes verification aids and documented limitations. | Candidate; repo author says personal-production-ready, *not* a stable release. |
| **Vercel Guidelines** | `vercel-labs/web-interface-guidelines` has the guideline source; `vercel-labs/agent-skills` provides a corresponding `web-design-guidelines` audit skill. | Separate source and consuming skill; network fetch of current guidance should be considered a trust boundary. |
| **Dropit** | `smart-kits/dropit-obsidian` is an Obsidian sync/inbox plugin with optional AI-agent processing, **not verified as an agent-skill pack**. | May involve untrusted incoming text and tool permissions; avoid unattended or unrestricted execution. |
| **KFM** | `kongfoo-ai/KFM` is a candidate sharing the acronym; repository includes a biomedical-research agent skill. | No evidence that this is the intended KFM; the acronym is too broad. |
| **Voice Studio** | `voicestudiohq/voicestudio` includes skills, MCP server and CLI for local AI voice production. | Requires macOS 12+ on Apple Silicon and the Voice Studio app; **not directly Windows-compatible** as documented. |
| **Paperclip** | `paperclipai/paperclip` manages agent teams, tasks and workflows. | Evaluate agent permissions, operational cost and telemetry before deployment. |
| **Magnitude** | `magnitudedev/browser-agent` is a vision-first browser agent. | Browser automation may require session/credential and action-approval boundaries. |
| **Vibe Trading** | `HKUDS/Vibe-Trading` is a trading-agent application. | Educational/research review only; do not connect brokerage funds or authorize trading from this list. |

### Still lacking reliable identification

- **“Math, Popo”** may be one name, **Matt Pocock Skills** (`mattpocock/skills`); the original video/source is needed to confirm. **MPEG-VLD skills** and **EMFIM** remain unresolved.
- **KFM**: multiple unrelated uses of the acronym; the specific original project is unknown.
- **Dropit skills**: a related-name Obsidian tool exists; there is no evidence it is the intended skill collection.
- **Python** remains a category rather than a unique repository. **“Math, Popo”** is now tentatively mapped as one creator name rather than two distinct skills.
- **Gods Eye View**, **Anti UI scope** and **Voice Studio**: plausible public GitHub candidates already recorded; exact identity still depends on matching the original source/video.

### Research links (original projects)

- Ponytail: https://github.com/DietrichGebert/ponytail
- Karpathy Skills: https://github.com/multica-ai/andrej-karpathy-skills
- Matt Pocock Skills: https://github.com/mattpocock/skills
- Ticks: https://github.com/pengelbrecht/ticks
- UI/UX Pro Max: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Dropit Obsidian: https://github.com/smart-kits/dropit-obsidian
- Vercel guidelines: https://github.com/vercel-labs/web-interface-guidelines
- Vercel skill: https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md
- Design Engineering: https://github.com/ryktara/design-engineering-skill

**Research is not a security clearance.** Scanner runs, code audits, dependency inspection and execution tests remain TODO for every candidate.

## Additional website and skill research: second reel batch

- [17 — Design Websites and Component Libraries](17-DESIGN-WEBSITES-AND-COMPONENT-LIBRARIES.md) catalogs 22 spoken names with confidence labels and unresolved leads.
- [19 — Agent Skills, Hooks and Code Animation](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md) catalogs Get Shit Done, CodeRabbit, Emil Kowalski Apple Design, SlopMonster and uncertain names.
- These entries are **not approved for privileged installation or execution** by being written down.

## VoiceStudio source identity correction — third reel batch

The earlier `voicestudiohq/voicestudio` is **not the same product** as the local cross-platform **`debpalash/VoiceStudio`** (https://github.com/debpalash/VoiceStudio), which the later reels specifically describe as Windows/macOS/Linux local voice clone/design/dubbing. Record both source identities separately. Do **not** treat the earlier macOS-only compatibility note as applying to `debpalash/VoiceStudio`. Review the license for the app **and** model weights separately. Details in [26 — Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md).

## Third source batch: newly researched GitHub projects (catalog only)

See [27 — Emerging Agents, Devices & Tools](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md): **google/artemis**, **usestrix/strix**, **OpenCut-app/OpenCut**, **jub0t/Concat**, **blixvip/html-anime**, **JCodesMore/ai-website-cloner-template**, **SaarthurR/atticus-mac**, **Adolanium/hermes-gadget-sdk** and other uncertain devices. See [26 — Open Source Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md) for AppFlowy, OpenHiggsfield, VoiceStudio, OpenProject, OpenWhisper and Cal.diy. None is automatically approved for installation merely by being researched.

## Addition — xtool (iOS development, 2026-10-25)

| Name | Verified repository | Category | Status |
| --- | --- | --- | --- |
| **xtool for iOS** | [`xtool-org/xtool`](https://github.com/xtool-org/xtool), official https://xtool.sh/ | SwiftPM-based iOS app building, signing, installing and launching from Linux/Windows via WSL/macOS, plus Apple Developer Services and device CLI | **Verified; user-requested reference. Not installed/security-reviewed.** |

This is a **developer tool rather than an agent skill**. Its platform setup, Apple credential handling and supported SwiftPM workflows matter. See [27 — Emerging AI Agents, Devices & Media Tools](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md) for the practical scope and limitations.

## Fourth reel batch: education, local fitness and agent skill research

- **Build Your Own X:** [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) — verified educational tutorial index; [first-principles learning notes](32-BUILD-YOUR-OWN-X-FIRST-PRINCIPLES-LEARNING.md).
- **openGym:** [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) — verified local/self-hostable workout tracker, subject to source/media licenses; [review](35-OPENGYM-MOCK-INTERVIEW-REVERSE-ENGINEERING-RESEARCH.md).
- **Reverse Engineer Anything (REA):** [morluto/rea](https://github.com/morluto/rea) — verified agent-based application analysis, **not** authorization to bypass subscriptions/DRM or copy protected code; [review](35-OPENGYM-MOCK-INTERVIEW-REVERSE-ENGINEERING-RESEARCH.md).
- **Five Claude avatar interview panel:** source website/repo **unresolved**, preserve as functional concept; [panel design notes](35-OPENGYM-MOCK-INTERVIEW-REVERSE-ENGINEERING-RESEARCH.md).
- **“Sunehra” 40+ editing skill kit:** creator's promised DM guide/repo **not provided/verified**; [conceptual editing study notes](34-VIDEO-EDITING-TASTE-STORYTELLING-AND-SUNEHRA-KIT.md).

**All new choices are catalog entries only; none installed, automatically trusted or security-approved.**

## Fifth reel batch: verified AI/design project names

- **Doory (spoken “Dory”)** — [shaongitbd/doory](https://github.com/shaongitbd/doory), browser graphic editor with MP4/GIF export; **not installed**.
- **MiroFish** — [oneseanlee/MiroFish](https://github.com/oneseanlee/MiroFish), agent-simulation engine; synthetic scenarios **cannot predict everything**.
- **REA (spoken “RIA”)** — [morluto/rea](https://github.com/morluto/rea), already recorded; this clip concerns a smart light/AC anecdote, not an independently confirmed demo.
- **AI embeddings interactive lesson** — original website unknown; related real examples in [39 — Embeddings](39-AI-FUNDAMENTALS-EMBEDDINGS-STUDY.md).

Detailed scope and limits: [40 — Project Research](40-DOORY-MIROFISH-REA-RESEARCH.md). All are *research entries*, not automatic installation or security approval.

## Sixth reel batch — confirmed and uncertain discovery leads

[44 — Agent Skills & Wishlist](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md) records **Replica** (Jakeschincariol/replica-skill), **Unlazy** (Leonxlnx/unlazy), Ralph, Brag, the AI Engineering tutor, and uncertain “Zero Code,” “Soup,” “OpenPrinter,” “Halal AI Guidelines,” and others. [49 — Devices & Local Tools](49-CARLINK-SMALL-SPEECH-MODELS-AND-LOCAL-OSS.md) distinguishes **CarLink** and **Whistle**. [52 — Source Register](52-INSTAGRAM-REELS-SIXTH-BATCH-REGISTER.md) preserves all 48 fragments. **Catalog only; no install or security clearance.**
