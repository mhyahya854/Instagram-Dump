# Things to Find — GitHub Repositories, AI Skills & Educational Projects

> **Status:** Research backlog, not an installation manifest. Nothing listed here has been installed, approved, or run by this document.
>
> **Source:** User's dictated list, 2026-10-24. Preserve raw names when voice transcription is uncertain. An identified candidate is not automatically the intended project.

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
| KFM | **Unresolved** | Exact target unknown | — |
| Python | Python-oriented agent skills (category, not a named product) | Search category | — |
| UI UX programs | UI/UX design agent skills (category). Possible candidate: UI UX Pro Max | Possible example, not asserted match | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| Ponytail | **Unresolved transcription/name** | Exact target unknown | — |
| Dropit skills | **Unresolved transcription/name** | Exact target unknown | — |
| Carpety skills | **Unresolved transcription/name** | Exact target unknown | — |
| Math | Mathematics agent skills (category, not a named repository) | Search category | — |
| Popo | **Unresolved transcription/name** | Exact target unknown | — |
| Tick skills | **Unresolved transcription/name** | Exact target unknown | — |
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
| MPEG-VLD skills | **Unresolved** | Do not guess the expansion | — |
| EMFIM | **Unresolved** | Do not guess the expansion | — |
| Design Engineering | One or more design-engineering skill projects | Ambiguous name; compare candidates | https://github.com/ryktara/design-engineering-skill ; https://github.com/AgentsORG/design-engineering |
| Version Web guidelines | Likely **Vercel Web Interface Guidelines** | Probable transcription correction | https://github.com/vercel-labs/web-interface-guidelines |
| Version Web design guidelines | Likely **Vercel Web Design Guidelines** skill | Probable transcription correction; related to previous row | https://github.com/vercel-labs/agent-skills |

## 5. Research workflow (not automatic installation)

For each lead, record:
1. **Exact original name** and **confirmed canonical owner/repository URL**, distinguishing confirmed, probable, possible or unresolved.
2. Purpose and category: educational repository, application, agent skill, tool, framework, or inspiration.
3. Compatibility with intended runtime and platform (Windows, macOS, Linux, Claude Code, Codex, etc.).
4. License, maintenance activity, dependency and execution risks, and network/secret access.
5. SkillSpector scan findings where relevant; manual review and isolation before any installation.
6. Overlap or conflicts with already adopted rules/skills.
7. Installation decision: **Not reviewed → Researching → Scanned → Manually reviewed → Approved / Rejected**. Do not change to Installed without execution evidence.

## Notes on terminology

- **SkillSpector** (not "Skill Specter") is confirmed from NVIDIA's own GitHub repository.
- **OpenMAIC**, **Anti-UI-Slop**, and **Vercel** are suggested corrections of speech-to-text wording. Record original phrases for traceability.
- **KFM, Ponytail, Dropit, Carpety, Popo, Tick, MPEG-VLD, EMFIM** need an exact source, video screenshot or link before mapping.
- A working public GitHub URL verifies a project exists, **not** that its code or skill is trustworthy.
