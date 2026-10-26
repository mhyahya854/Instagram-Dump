# 54 — Five Claude Video Styles: Source-Matched GitHub Repositories

Captured 2026-10-26. Source reel lists five styles and says they are all available on GitHub. Project identity confirmed against repository README wherever possible. **Not an install list and not a production-quality guarantee.**

| Reel # | Name | Strongest public source | What it actually does | Notes |
| --- | --- | --- | --- | --- |
| 1 | **HyperFrames by HeyGen** | https://github.com/heygen-com/hyperframes | Open-source HTML/CSS/GSAP-oriented video composition/rendering framework, skills and CLI | **Verified**; “HTML in, motion graphics out” is simplified. Requires authoring and asset decisions. |
| 2 | **One Take** | https://github.com/feitangyuan/onetake | One continuous camera and connected motion states instead of slideshow cuts | **Verified**; README documents continuous product/launch films and temporal continuity checks. |
| 3 | **Collage B-roll** | https://github.com/pyang5166/gbro-collage-broll | Editorial half-tone paper collage assembled as B-roll, with approval gates and Gemini image/video generation | **Strong match**; code/skill opens process but Gemini provider/API costs and rights may apply. English adaptation https://github.com/MegaTroll222/VOX-COLLAGE-BROLL integrates MaxFusion and optional ElevenLabs. |
| 4 | **Claude Animation Base** | https://github.com/JohnHeibel/ClaudeAnimationBase | Hand-painted p5.js/p5.brush animation using Clawd character, model sheets, storyboard and headless renderer | **Verified**; licensing of code vs character/demo assets should be examined. |
| 5 | **Lemo Opuscar** | https://github.com/lemomo-ai/lemo-opuscar | Director/technical/style guides plus code-rendered film examples in Canvas/WebGL with TTS and procedural audio | **Verified**; “43 styles” was true in an earlier snapshot. The repository has since expanded beyond 43; numbers are versioned. |

## What separates the five

- **HyperFrames:** underlying renderer/platform (can build many styles).
- **One Take:** cinematography *continuity constraint* (one continuous moving composition).
- **Collage B-roll:** visual asset/material technique (paper-cut editorial effect).
- **Claude Animation Base:** character rig and hand-painted 2D style with emotions.
- **Lemo Opuscar:** a library of directed narrative style references and reproducible source systems.

These are *not five equivalent plugins*. Three can be integrated into a broader rendering production system; one is a character base; one a style collection. Repeated instructions from distinct authors may conflict—choose the one that fits a brief instead of activating all simultaneously.

## Film pipeline details worth retaining offline

### One Take

A smooth passage between moments should preserve spatial continuity: the same object/camera path, a coherent easing curve, no sudden teleport without a deliberate transformation, meaningful story connection, and an explicit continuity metric or human playback review.

### Collage B-roll

Take a line of narration → draft an original visual metaphor → obtain approval → assemble licensed still layers and typography → animate the pieces entering the frame → synchronize speech/subtitles → run playback QA. The original project's Gemini-first/last-frame generation makes this a **hybrid** rather than fully deterministic code-rendered film; don't claim every frame is handwritten code.

### Clawd painted character

Rig position/face/emotions, scenes and effects using p5.js/p5.brush. Check line quality, consistent shape, eye/mouth position, joints, scene boundaries, render dependencies and export. The README documents a storyboard-first workflow and a video render script.

### Lemo Opuscar

The repository's technical guide describes timeline → visual scene renderer → rendered frames → narrated speech/time stamps → sound/music → subtitles → FFmpeg mixing/muxing. It has 43 initial films and a later **expanded collection**, so pin a commit and list licenses for source code, demos and third-party assets separately.

### HyperFrames

Build a real HTML composition with defined viewport, animation timeline, reusable elements and renderer-specific API; render to video; compare frames and technical log. It is not merely recording the user's website and pressing a button.

## Comparison checks for a potential project

| Criterion | Ask |
| --- | --- |
| Source quality | Is there real code, current maintainer, tests and version-pinned docs? |
| Output | GIF, MP4, scene source, timeline, captions, audio stems? |
| Determinism | Is output code-generated or generative model video? Repeatable render? |
| Rights | License for code, demos, fonts, voice models, music and brand look? |
| Offline | Which stages can run without API keys, GPU, cloud or external models? |
| Agent safety | Which scripts write files or execute binaries? Permission boundaries? |
| QA | Contact sheets, golden frames, actual playback and audio checks? |

**No cloning or installation performed.** Store project links as provenance; Markdown preserves the workflows but does not include upstream dependencies, demo samples or model weights.

Related [53 — Motion Guide](53-MOTION-GRAPHICS-BRAND-GUIDE-VOICE-WORKFLOW.md), [25 — Programmatic Video](25-STICKMAN-PROGRAMMATIC-VIDEO-WORKFLOWS.md).
