# 49 — CarLink, Tiny Speech Models and Local Open-Source Tools

Captured 2026-10-25. These are unrelated projects grouped by *local device/edge use*, not a required technical stack.

## CarLink: reusing an Android tablet as a CarPlay display

**Strong primary match:** https://github.com/F-e-n-y-x/CarLink . Installs CarLink APK on the **Android head unit/tablet/phone used as the display**, not on the iPhone. When paired over supported USB or Bluetooth + Wi-Fi, it can accept **CarPlay from a compatible iPhone** and **Android Auto from an Android phone**, with auto-detection. It integrates DiPlay/DiAuto originally designed for BYD DiLink; generic devices are supported in the project's documented scope.

**Requirements:** Android 7.1+ on supported ARM architectures according to the repo; actual Wi-Fi Direct/USB compatibility and system permissions vary. Use only official release downloads and verify SHA-256/signature information, not a third-party APK mirror. Review microphone, Wi-Fi, Bluetooth, location and overlay permissions.

**Do not mistake this for:** iPhone running arbitrary Android apps, CarPlay running on every tablet, an official Apple-issued CarPlay host, or confirmed compatibility with every older device. Never operate driver-distracting settings while driving.

The original transcript said “BYT cards,” likely **BYD cars**, and described connecting the Android display to an iPhone; this matches CarLink. Another source is DiPlay https://github.com/shihabal3amri/DiPlay, but the generic cross-platform CarLink appears closer to the reel.

## Cactus Compute Whistle: 16.9 MB local speech recognition

**Official primary source:** https://cactuscompute.com/blog/whistle ; code runtime https://github.com/cactus-compute/needle ; model https://huggingface.co/Cactus-Compute/whistle .

Announced 2026-10-02. Whistle is a 16.9 MB quantized speech model using the Needle/Cactus CPU engine. Local transcription, word-level timestamps and speech embeddings. Seven documented languages: English, German, French, Spanish, Italian, Dutch, Polish. **Arabic is not listed** in this snapshot, so do not claim it suits the entire Hindi/Arabic reels workflow. Reported speed comparisons are vendor benchmarks, not proof fastest speech model everywhere.

For live usage add microphone consent, local/on-device VAD, chunk handling, text confidence, optional keyword boost and correction interface. Music can hallucinate words; monitor false triggers.

## Tiger S1 (unresolved)

A reel describes a “5 MB” CPU model clicking 47 FreeCAD actions in three seconds with ~2 ms decision latency, and calls it Tiger S1. No dependable official source matching **all** specs was found. “5 MB” may refer to quantized weights or a controller, not a general reasoning assistant. Do not claim those benchmark metrics as fact or recommend unverified binary installation.

## Other researched open-source tools

| Tool | Verified project | Purpose / limitations |
|---|---|---|
| OpenCut | https://github.com/OpenCut-app/OpenCut | Open-source video editing; main branch in major rewrite, inspect classic release status |
| AnythingLLM | https://github.com/Mintplex-Labs/anything-llm | Local/self-hosted document chat and RAG; inspect selected model/cloud providers and privacy |
| Nuclear | https://github.com/nukeop/nuclear | Free open-source music player on Windows/macOS/Linux, with search and plugin extensibility |
| Cap | https://github.com/CapSoftware/Cap | Screen recording and shareable clips; compare license and actual hosted features |
| Handy | https://github.com/cjpais/Handy | Offline dictation with local speech models, system permissions |
| OpenPrinter | Several unrelated repositories share name | Exact intended AI-safety tool unidentified |
| Halal AI Guidelines | Multiple similarly named repos | Third-party research candidates; cultural/religious evaluation is user-controllable and requires correct attribution |

## Local software decision checks

Source code/license; release signatures; binary provenance; offline runtime and network access; hardware compatibility; paid inference or account prerequisites; local permissions (microphone, accessibility, clipboard); data storage/export; support/update status; benchmark validity and negative/failure tests.

Existing related [26 — Open Source Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md), [27 — Emerging Devices](27-EMERGING-AI-AGENTS-DEVICES-AND-MEDIA-TOOLS.md).
