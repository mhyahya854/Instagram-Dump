# 27 — Emerging AI Agents, Devices, Media and Experimental Projects

_Captured 2026-10-25. This file deliberately keeps uncertain 2026 claims and maker names separate from verified source links. A demo is not a verified independent benchmark._

## Identified with credible source

| Reel term | Candidate and what it does | Status, compatibility and caution |
| --- | --- | --- |
| **Google Artemis** | https://github.com/google/artemis — Android agent automation, tests, screenshots/logcat and MCP integrations for coding assistants | **Verified project.** Android device/emulator and developer tools required. Project reports 99%+ on **AndroidWorld benchmark**, not 99% on all real-world apps. Android accessibility helper requires clear control, consent and test-device scope. |
| **Atticus for Mac** | https://github.com/SaarthurR/atticus-mac — voice-controlled macOS windows, app/file search, on-screen actions and memorized shortcuts | **Verified**. README calls for macOS 26+, Claude plan/Claude Code in core setup. Running desktop automation requires careful app permissions and human approval for sending/deleting/buying. |
| **Hermes Gadget** | https://github.com/Adolanium/hermes-gadget-sdk — plugin/firmware bridge from a microphone+speaker+screen device to user's Hermes Agent | **Verified** community plugin, documented on https://hermes-agent.nousresearch.com/docs/plugins/gadget . Device firmware, network connection, pairing, STT/TTS and agent service may be needed. |
| **OpenCut** | https://github.com/OpenCut-app/OpenCut — open source CapCut-like video editor | **Verified**, but main repo is an active rewrite. Previous runnable app is `OpenCut-app/opencut-classic`; roadmap is not shipped features. |
| **Concat** | https://github.com/jub0t/Concat — local video editor with captions, voice, effects, timeline and MCP/API integrations | **Verified candidate**. Forks/copies exist; pin maintainer and inspect current platform availability, beta status and licenses. |
| **HTML Anime** | https://github.com/blixvip/html-anime — code-based agent-directed anime/animation, shot-sheet and skills | **Verified**; possible companion to programmatic stickman/video learning, *not* creator's confirmed pipeline. |
| **Strix** | https://github.com/usestrix/strix — autonomous AI security testing platform | **Verified.** Highly capable **active penetration-testing** tooling: use solely for assets with explicit permission, sandbox scope and clear safety/stop conditions. |
| **JCodesMore AI Website Cloner Template** | https://github.com/JCodesMore/ai-website-cloner-template — Next.js project scaffolding plus agent skill for reconstructing observed page layouts/behaviors | **Verified**. Can aid learning/design parity; **do not clone others' sites for deceptive impersonation or unlicensed asset/brand reuse**. Version 0.5.1 fixed vulnerable dependencies; use pinned latest-reviewed release. |

## Named project, but identity or claims unresolved

| Spoken term | What was claimed or what it might mean | Research/record decision |
| --- | --- | --- |
| **37 Studio** | “Free open-source AI studio made ad locally”; animation/video creation | Exact canonical GitHub origin unresolved. |
| **Kuku** | Voice message triggers an entire AI agent team | Brand/project unclear. |
| **Bots Commander** | Free desktop application coordinating agents | No definitive matching main repo found; preserve raw phrase. |
| **Cursor computer use, announced October 23** | Agent allegedly manipulates desktop apps, simulators and screenshots | A versioned, changing public-product claim; no validated current official docs in this pass. Not evidence all platform/app permissions work. |
| **Kimi 3D Make** | Text/photo to printable 3D object, attributed to Moonshot/Kimi | Original official project/product unverified; avoid equating generated mesh with safe printable watertight geometry. |
| **print 3D** | Skill/plugin for Hermes/Claude/Codex/Cursor/Gemini to turn image into printable model | Exact repo unconfirmed. Geometry needs scale, manifoldness, tolerances and slicer tests. |
| **Vault E4B** | 4GB “Gemini 4 + Nematron” 64k model | Claims are internally unusual and unverified; do not assert model provenance or weights. |
| **Herald OS** | Free proactive “Jarvis OS” coordinating a day | Candidate https://github.com/iamlukethedev/Herald-OS found by name search but intended canonical product not verified. |
| **Quer Spaces** | Claimed Hermes cloud/computer-use plugin | Strong *name-adjacent* candidate https://github.com/trycua/hermes-cua-spaces ; not yet matched to original reel; cloud-computer permissions and costs matter. |
| **Mochi / tiny blue face** | Visual pet/agent status companion | Name not enough to identify exact repo. |
| **Kimi 3D, Moonshot**, **3D cube button** | Generative geometry and complex WebGL button effects | Not verified as specific code or supplier. Shader effects can be expensive on low-end devices. |
| **Free AI coding agent with ads** | Claimed zero-price agent subsidized by advertising | No brand/source supplied. Avoid claiming privacy, price or eligibility. |

## Screenshot and biometric privacy

The reel on **FaceCheck.id** describes online face matching. Facial-recognition searches can expose or falsely associate real people; they are not reliable identity proof and should not be used for stalking, doxxing or unauthorized tracking. Do not infer a person's identity from a screenshot alone. For educational/privacy use, discuss image privacy and false positives, not procedures for identifying someone in private photos.

## Stalkerware security-awareness clip

A viral story claims a concealed Android spy app exfiltrated photos and documents for 18 months. The specific anecdote, “2,300 Indian phones” and prevalence statistics are **unverified**. Stalkerware is a genuine surveillance threat class. For a suspected device, prioritize personal safety, secure an independent device for sensitive communications, preserve evidence appropriately, and consider trusted specialized support. Removing suspicious software hastily can notify an abusive person or destroy evidence. Do not assume a generic coding agent can reliably find every malicious service on a phone.

## What “free/local” really means

Local apps still need compute/storage and sometimes optional downloads, models or service subscriptions. A UI working offline does not imply its models or every integration are usable offline. Inspect device requirements, source, licensing and whether telemetry or remote calls are configurable.

## Security research boundary

Do not install unknown agents, grant accessibility/admin permissions, test arbitrary IPs or run malware scans on other people's devices from a viral claim. Every new repo is **research-only** until separately audited and user-authorized.

## Addition — xtool for iOS development (2026-10-25)

**Verified project:** [xtool-org/xtool](https://github.com/xtool-org/xtool) · Official site: https://xtool.sh/

**Category:** Cross-platform iOS development / SwiftPM build and deployment tooling, **not** an agent persona or autonomous UI testing tool.

**What it does:** xtool provides Xcode-like command-line workflows for Swift Package Manager-based iOS applications on Linux, Windows via WSL, and macOS. The documented commands let developers initialize a SwiftPM iOS project, build/run in its supported workflow, authenticate with Apple Developer Services, list compatible connected devices, and sign/install/launch iOS applications. Its **XKit** library also exposes Apple developer/device integration for custom tooling.

**Why it matters for an AI coding workflow:** an agent working on a supported SwiftPM iOS project can potentially use CLI commands in a controlled development environment, rather than assuming every iOS workflow requires direct access to the Xcode graphical interface. This can complement design and test processes, but is **not** equivalent to a complete Xcode replacement or real iOS UI testing.

**Compatibility and trust caveats:** The project is documented for Linux, **Windows/WSL**, and macOS, with platform-specific setup. iOS SDK/toolchain and Apple Developer authentication/signing requirements still apply; Apple account credentials and signing identities are **sensitive**. Confirm project/build compatibility, supported iOS target devices, WSL USB passthrough (if relevant), licensing, dependency security, Apple tooling/legal constraints, and device permissions. Validate on an actual test device; no guarantee of App Store submission or every Xcode feature.

**Status:** GitHub repository and documentation verified, **user-requested catalog addition**, **not installed, security-audited, or approved for privileged execution**.

**Further reading:** https://github.com/xtool-org/xtool/blob/main/README.md ; https://xtool.sh/documentation/xtool/ .

## Sixth batch — new mobile/edge sources

[49 — CarLink / Whistle](49-CARLINK-SMALL-SPEECH-MODELS-AND-LOCAL-OSS.md) covers reuse of an Android display with an iPhone CarPlay connection, official APK integrity checks and a 16.9 MB on-device speech model. The alleged Tiger S1 FreeCAD model is unverified and remains explicitly unresolved.

## Sixth batch — CarLink and Whistle

[49 — CarLink, Whistle and Local OSS](49-CARLINK-SMALL-SPEECH-MODELS-AND-LOCAL-OSS.md) covers Android devices reused for iPhone CarPlay, official release hashes, device permissions and a 16.9 MB Cactus speech model. Alleged Tiger S1 FreeCAD click model is not verified.

## Eleventh batch — xtool and Raspberry Pi projects

[80 — xtool, ReactOS, Laravel, Pi](80-XTOOL-REACTOS-LARAVEL-SIGNUP-RASPBERRY-PI.md) documents xtool-org/xtool's iOS SwiftPM build/sign/deploy capability on Linux/WSL/macOS, separate from Apple's Mac-only GUI Simulator, and a Raspberry Pi beginner project overview. Original screenshot only says “a Raspberry Pi”; no specific sensor, firmware or device is identifiable. [82 — Hardware Shopping](82-PROJECT-BUILDING-HARDWARE-PURCHASE-SHORTLIST.md) keeps monitor/keyboard research separate from development requirements.
