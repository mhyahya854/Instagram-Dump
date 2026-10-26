# 26 — Open-Source Alternatives, Self-Hosting and Local Apps

_Captured 2026-10-25. Reel presents nine “replacements.” Record the actual type and ownership, not a claim that one tool fully replaces all features of another._

## Original nine names and researched match

| # | Spoken | Likely / verified project | Product category and use | Confidence / important limits |
| ---: | --- | --- | --- | --- |
| 1 | “OpenHixfield” (replaces Hixfield) | **OpenHiggsfield**, https://github.com/wide-trace/open-higgsfield | Browser image/video studio for selecting models, submitting prompts and managing output | **Strong transcription match.** Studio code may be open but generation requires paid provider keys, cloud storage and model licenses; “free” UI is not free inference. Other repos have similar names. |
| 2 | “Voice Studio” (replaces ElevenLabs) | **VoiceStudio**, https://github.com/debpalash/VoiceStudio | Fully local speech design, cloning, captions, dubbing, transcription and audiobooks | **Verified match.** Windows/macOS/Linux; CPU can be slower. **App is AGPL-3.0, bundled model weights may restrict commercial use.** Not the macOS-only `voicestudiohq/voicestudio` previously shortlisted. |
| 3 | “OSEO” (replaces SEMrush) | **Unresolved** | Claimed rank tracking, backlinks and SEO site audits | Do not confuse with https://github.com/ansvisor/ansvisor (**verified adjacent AI-search visibility tool**, not a proven SEMrush-equivalent and not evidence of “OSEO”). |
| 4 | “AppSway” (replaces Notion) | **AppFlowy**, https://github.com/AppFlowy-IO/AppFlowy | Local/self-hosted wiki, notes, collaborative docs, databases/tasks and optional AI/local-model support | **Strong phonetic match.** Check version, feature parity, privacy and sync before migration. |
| 5 | “OpenWhisper” (replaces Wispr Flow) | **OpenWhisper**, https://github.com/fsouza-dot/OpenWhisper | Global push-to-talk dictation; local Whisper or optional cloud transcription | **Matching named repo** but multiple unrelated OpenWhisper projects and platforms exist; check which app reel featured. |
| 6 | “Open Project” (replaces Asana) | **OpenProject**, https://github.com/opf/openproject | Project planning, tickets, boards, Gantt, time tracking and collaboration | **Verified.** Some team functionality/deployment requires server administration or commercial tier. |
| 7 | “Cal.com” (replaces Calendly) | **Cal.com hosted** https://cal.com and **Cal.diy OSS** https://github.com/calcom/cal.diy | Public booking pages, calendar integrations and scheduling | **Important 2026 change:** hosted Cal.com code is no longer represented by same public app repo; Cal.diy community edition omits team/workflow features and is advised for personal/nonproduction use. |
| 8 | “Chat” (replaces Intercom) | **Possibly Chatwoot**, https://github.com/chatwoot/chatwoot | Customer support live chat, multi-channel conversation inbox, help desk | **Likely but not confirmed** from truncated “Chat.” Authenticated integrations and hosting/operations needed. |
| 9 | “Snap” (replaces Loom) | **Unresolved exact name**; related verified **Cap**, https://github.com/CapSoftware/Cap | Screen/video recording and sharable clips | Do not silently replace “Snap” with “Cap” as a fact; Cap is a credible *alternative*, not the verified reel subject. |

## Why “open-source alternative” is not equal to “same product for free”

Review four separate issues:
- **Application license** (MIT/Apache/AGPL/etc.), license compatibility and redistribution rules.
- **Models and weights** (may restrict commercial use even when app code is open).
- **Compute/storage** (GPU, electricity, VPS, provider calls, cloud data, external API, backups).
- **Feature parity and lifecycle** (self-hosting responsibility, missing managed integrations, security upgrades, import/export, sync).

### VoiceStudio identity correction

Previously [05 — Things to Find](05-THINGS-TO-FIND.md) described **voicestudiohq/voicestudio**, a separate similarly named Mac-focused developer tool. The reels here explicitly discuss a local cross-platform voice studio with ~80k GitHub stars, voice cloning/design and Windows/Linux support, matching **debpalash/VoiceStudio**. These two should remain separate, not be conflated.

### OpenWhisper ambiguity

At least two unrelated products use this name. **fsouza-dot/OpenWhisper** documents local/cloud-mode hotkey dictation across Windows, Mac and Linux; **openwhisper.io** advertises a separate local macOS dictation app. Confirm actual screenshot/source before assigning one definitively.

### OpenProject / Cal.diy adoption caution

Self-hosted scheduling/project management requires calendar OAuth credentials, HTTPS, email delivery, backups, access roles, time-zone and daylight-saving testing. Cal.diy **does not** provide the full hosted Cal.com team features in 2026.

## Status

Recorded as **discovery**, not approved for installation or migration. The known named projects and confidence labels are preserved; no accounts, calendar connections or speech models were installed or accessed.

## Sixth batch — additional local projects

[49 — CarLink, Whistle and OSS](49-CARLINK-SMALL-SPEECH-MODELS-AND-LOCAL-OSS.md) includes CarLink/DiPlay, Cactus Whistle speech-to-text, Handy offline dictation, Nuclear music player, AnythingLLM, Cap and OpenCut. Distinguish source-code license, bundled models, app permissions and real hardware compatibility.

## Sixth batch — local and edge project additions

[49 — CarLink, Whistle & Local OSS](49-CARLINK-SMALL-SPEECH-MODELS-AND-LOCAL-OSS.md) covers CarLink/DiPlay, Cactus Whistle, Handy, Nuclear, AnythingLLM, Cap and OpenCut, with licensing, privacy and platform caveats.

## Tenth source batch — ten verified self-hosted alternatives

[72 — Paperless, Karakeep, Vaultwarden, Anytype, AdGuard Home, Syncthing, Home Assistant, Audiobookshelf, Stirling-PDF & Bitwarden Send](72-TEN-SELF-HOSTED-PRIVACY-ALTERNATIVES-SCREENSHOTS.md) records each screenshot's original claimed paid-service replacement **separately** from actual supported functions, maintenance, rights and limitations. Important: Syncthing is sync, not backup; AdGuard Home cannot filter every ad; self-hosting does not guarantee total privacy or zero cost. [74 — PrivacyPack](74-PRIVACYPACK-AND-PLUG-IN-PHONE-MALWARE-DIAGNOSTICS.md) is an independent in-browser privacy-switch *share card*, not a virus scanner.

## Eleventh batch — ToffeeShare, ReactOS and VoxelWall distinctions

[81 — ToffeeShare](81-TOFFEESHARE-PEER-TO-PEER-PRIVATE-FILE-TRANSFER.md) is an ephemeral encrypted browser-to-browser transfer service, **not backup/storage or verified fully open-source**. [80 — ReactOS](80-XTOOL-REACTOS-LARAVEL-SIGNUP-RASPBERRY-PI.md) is an alpha Windows-compatible OS best explored in VM, not installed on a primary laptop. [79 — VoxelWall-Inspired Cross-Platform Plan](79-VOXELWALL-CROSS-PLATFORM-WINDOWS-LINUX-MAC-PLAN.md) is a planned original multi-OS wallpaper app, **not a first-party free VoxelWall port**.

## Fourteenth batch — five additional open/local app references

[114 — OpenCut, AnythingLLM, Nuclear, Cap and Handy](114-OPENCUT-ANYTHINGLLM-NUCLEAR-CAP-HANDY-ALTERNATIVES.md) preserves source captions, compared services and independently verified GitHub repos. Current OpenCut README identifies an ongoing rewrite and classic editor; AnythingLLM's local app may connect to remote LLMs. Cap's features vary with OS/release; Handy is designed for local speech transcription. [115 — Tencent Octop](115-TENCENT-OCTOP-SELF-HOSTED-MULTIAGENT-CLAIMS.md) is local orchestration but may still use remote model providers. None installed.

## Fifteenth collection — offline and hosted are different claims

[122 — Qalb/Bonsai-2](122-QALB-URDU-BONSAI2-ARENA-OMNIVOICE-RESEARCH.md) describes Urdu model lead and PrismML compression, with model footprint distinct from total inference RAM. [128 — Clicky](128-CLICKY-AI-SCREEN-BUDDY-AND-NAME-COLLISIONS.md) documents original open-source Mac helper versus newer private product development. [124 — Cost Stack](124-COST-CONSCIOUS-STACK-GSD-ROO-RALPH-CODERABBIT-LINKEDIN.md) preserves Neon/Cloudflare/R2 snapshot pricing claims, not permanent guarantees. [121 — RuView](121-RUVIEW-WIFI-SPATIAL-SENSING-RESEARCH.md) needs supported RF hardware and calibration.

## Sixteenth collection — Edge0 and free infrastructure caveats

[131 — Edge0 SSD-streamed MoE](131-EDGE0-SSD-STREAMED-MOE-LOCAL-LLM-FACT-CHECK.md) notes low active allocator vs **whole system memory**, 23GB 35B model weights, experimental Windows runtime and SSD performance needs. [135 — runs-on.dev](135-RUNS-ON-DEV-FREE-SUBDOMAIN-GITHUB-CLAIM-GUIDE.md) is free developer subdomain hosting identity, **not** an owned standalone DNS domain; operational provider/reclamation risk remains. Research only; no local software tested.
