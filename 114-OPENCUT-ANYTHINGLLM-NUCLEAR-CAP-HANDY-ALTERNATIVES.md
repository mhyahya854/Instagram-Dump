# 114 — Five Open-Source/Local-First App Alternatives: OpenCut, AnythingLLM, Nuclear, Cap and Handy

**Source:** screenshots 8–12 of the fourteenth Instagram batch. Each screenshot presents one product with heading, a subtitle and a sales description, UI screenshot and competitor logos. These are **five independent products**, not one integrated app. Exact wording from the screenshot is preserved before independently verified current status.

## Screenshot-derived transcription (original order)

### 1. OpenCut

**Exact title:** “OpenCut” · **subtitle:** “(Best CapCut Alternative)”.

**Visible description:** “Browser-based, open source video editor built for privacy. No installs, no account required, works on any platform.”

**Screenshot's ‘Open Source Alternative to’ list:** CapCut, Adobe Premiere Pro, DaVinci Resolve, Filmora, Final Cut Pro.

**Verified:** https://github.com/OpenCut-app/OpenCut · https://opencut.app/ .

**Critical current status:** maintainer README says **OpenCut is being rewritten from scratch**. Its **classic release** remains at https://github.com/opencut-app/opencut-classic and current opencut.app points to classic; planned Rust shared core, plugin-first editor, mobile/desktop/web, MCP and headless modes are **roadmap**, not all shipped. Source screenshot's claim “best alternative” is opinion, not confirmed feature parity.

### 2. AnythingLLM

**Exact title:** “AnythingLLM” · **subtitle:** “(Self-Hostable AI App)”.

**Visible description:** “AnythingLLM is a desktop application and self-hostable platform that lets you chat with your documents, run AI agents, and work with large language models entirely on your own machine. No account required.”

**Competitor captions visible:** Claude, ChatGPT, Grok, Perplexity, Gemini, TypingMind, T3.chat, Poe, BoltAI, Msty Studio, Monica, Alice.

**Verified:** https://github.com/Mintplex-Labs/anything-llm · https://anythingllm.com/ .

**Caution:** “on your own machine” applies to local deployment/storage; **remote model providers can still receive text** when selected. Privileged agent tools and document RAG connectors need correct scope/permissions. Multiuser hosting requires authentication and data segregation.

### 3. Nuclear

**Exact title:** “Nuclear” · **subtitle:** “(Open-source Desktop Music Player)”.

**Visible description:** “Nuclear is a desktop music player that pulls audio from multiple online sources, with no ads, no tracking, and no subscription required. The full source code is publicly auditable, and there's no telemetry or data collection of any kind.”

**Competitor names visible:** Spotify, YouTube, YouTube Music, SoundCloud, Apple Music, Deezer, Tidal.

**Verified:** https://github.com/nukeop/nuclear · https://nuclearplayer.com/ .

**Caution:** Playback comes through external plugins/online sources. Network access and third-party services have their own rights and privacy policies. The screenshot's blanket “no telemetry of any kind” is a publisher claim, **not independent network audit**. Check region-specific streaming rights.

### 4. Cap

**Exact title:** “Cap” · **subtitle:** “(Record and Edit your screenrecording in seconds)”.

**Visible description:** “Cap is a cross-platform screen recorder built for people who share work asynchronously. It runs natively on macOS, Windows, and Linux, and covers three distinct workflows in one app.”

**Competitors visible:** Loom, Screen Studio, CleanShot, Bandicam, ScreenFlow, Kite, Shotbase, Camtasia.

**Verified:** https://github.com/CapSoftware/Cap · https://cap.so/ .

**Caution:** Project README calls itself a shareable screen recording tool and Loom alternative. **Platform support may vary by particular release and recording mode**; don't assert a single binary and every function is supported equally on all OSs without running the release. Local recording, cloud sharing, paid plan features and data retention are distinct decisions. Review screen/mic permissions and private-window capture.

### 5. Handy

**Exact title:** “Handy” · **subtitle:** “(Free alternative of Whisper Flow)”.

**Visible description:** “Handy is a desktop speech-to-text tool that works with any text field on your computer. Press a keyboard shortcut, speak, release, and your words appear wherever your cursor is. No cloud. No subscription. No copy-paste step.”

**Competitor names visible:** Wispr Flow, Superwhisper, Typeless, Aqua Voice, Willow, Voibe, Monologue, AudioPen.

**Verified:** https://github.com/cjpais/Handy · https://handy.computer/ .

**Caution:** README describes **offline local speech transcription** using user-selected local models. Initial model downloads, OS permissions, accessibility APIs, keyboard simulation and hardware speed still matter; sending transcript to the focused app can involve that app's own cloud sync. Transcription errors require review.

## Comparison and selection

| Product | Domain | Strongest use | Does not automatically provide |
|---|---|---|---|
| OpenCut | Video editing | Timeline/story editing, local/web-first | Full CapCut/Premiere feature parity or all roadmap items today |
| AnythingLLM | AI + documents | Private/local-model document chat and agent shell | A private data path if a remote model is selected |
| Nuclear | Music | Streaming/search/playlists from multiple sources | Licensed access to every paid commercial catalog |
| Cap | Screen recording | Demo/bug reports/asynchronous communication | Equal platform support and zero-cost hosted storage on all tiers |
| Handy | Dictation | Speech into active desktop field | Perfect recognition on every microphone/language/app |

## Relevance to your projects

- OpenCut/Cap/Handy are useful as *independent tools* for the motion/video and project-dump workflow.
- AnythingLLM is an optional reference for the private Life OS agent/knowledge browser but is not itself a full journal/location/calendar app.
- Nuclear is an example of modular local-first media UX, plugin architecture and truthful offline/online boundaries.

**No installation, login, media upload, screen/mic access, subscription or test completed.** Source URLs are independently identified repo matches; original screenshot images have not been mirrored on GitHub. Related [26 — Local Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md), [48 — Media](48-AI-DESIGN-VIDEO-SEO-MARKETING-REFERENCES.md).
