# 53 — Claude Motion Graphics: Brand Guide, Script, Speech and Render

Captured 2026-10-26 from dictated Instagram excerpts. Separate **the creator's claimed process**, independently researched possible tools, and **missing proprietary materials**. No software installed, paid account accessed, or video rendered.

## Clip A — “No plugins” workflow (as stated, not verified as repeatable)

1. Open Claude and upload a creator-provided **skill file**, which the reel promises through “comment kit”. **We do not have that file.** The phrase “without plugins” still depends on supplying custom agent instructions and using services elsewhere.
2. Give the agent a legitimate website to derive a brand guide: logos permitted to use, color roles, typefaces, layout grammar and overall tone. The agent must not assert that a scraped page is authorized brand source unless this is the user's website.
3. Explain the intended story and produce a script, speech lines and visual beat sheet.
4. Make narration using **ElevenLabs** and its applicable expressive/performance tags. The exact syntax, license and availability change across TTS models; do not assume every model accepts the same tags.
5. Supply voice timing/audio to the editing/rendering environment, paste the creator's promised prompts (also **not supplied**) and request a new animation brief.
6. The reel says “Open Claude Design, select Animation and upload files.” **The exact product/workspace surface is not confirmed**; do not invent product menus or claim a native animation button exists for every account.
7. Generate an initial draft, inspect every scene and refine by edit instructions.
8. Claims of “first draft in ten minutes” are promotional and depend on duration, model, rendering and hardware.

**Missing:** the actual skill, prompt library, original guide, references, sound samples and working example from this particular creator. The written steps are **not** a recovered kit.

## Clip B — three techniques

1. **Use existing code effects with licensing checks.** The reel says “Ripple link”; **exact Ripple project not identified**. A library can supply reusable visual primitives, easing or renderer code, not automatic rights to copy a particular composition.
2. **Use persistent project context.** Store actual preferred typography, previous edits, palette and pacing in a DESIGN.md / project brief and link to reviewed examples. Do not confuse memory of preferences with permission to access unrelated private assets.
3. **Plan music as part of the timeline.** The reel names **Suno**, an AI music generator. Music creation, commercial use, training, distribution and sync rights depend on the service and chosen plan. Generated audio is not automatically copyright-free.

## Repeatable independent production workflow

| Stage | Input | Output/check |
| --- | --- | --- |
| Ownership & brief | audience, brand permissions, message, duration, aspect ratio | signed-off creative brief |
| Brand tokens | fonts with licensing, real colors, spacing, logomark assets | reusable brand-guide file and fallbacks |
| Script/storyboard | factual claims and source citations | voice script and beat timing map |
| Voice generation | approved speaker model, pronunciation, emotion direction | WAV/MP3 + speech timestamps, no unauthorized cloning |
| Scene system | motion grammar, keyframes, camera and layer hierarchy | deterministic scene graph; no unapproved brand cloning |
| Render | frame rate, size, codec, fonts, accessible captions | actual MP4, thumbnails/contact sheets and render logs |
| Audit | subtitles, audio clipping, safe margins, scene continuity, rights | explicit pass/fail evidence, not an agent's confidence |
| Distribution | social platform/campaign | real preview with legal copy and metadata |

### Structured brief template

- Message: one main claim and the evidence source.
- Audience, voice, output duration and export dimensions.
- Brand: exact permitted fonts, colors, logos, anti-patterns and preferred compositions.
- Scenes: ID, start/end, narration line, visual metaphor, transition, motion curve, camera, call-to-action.
- Audio: licensed TTS, voice pacing, foley, music mood, loudness target and ducking.
- Rendering: chosen stack and actual dependencies; source asset paths; subtitles and language.
- Acceptance: each scene legible, no missing audio, audio-sync verified, rights checked, exported/played on target device.

## Tool options (real public projects, not necessarily used in the reel)

- **HyperFrames** — https://github.com/heygen-com/hyperframes ; HTML/CSS/JS composition rendered to video. The repository ships multiple agent skills and current setup may require dependencies.
- **Remotion** — https://github.com/remotion-dev/remotion ; React-driven programmatic video.
- **OpenMontage** — https://github.com/Open-Montage-app/OpenMontage ; stage-based AI-assisted video production; advertised local/free routes and optional paid providers.
- **Lemo Opuscar** — https://github.com/lemomo-ai/lemo-opuscar ; code-rendered films with style/director/technical guides.
- **FFmpeg** — https://github.com/FFmpeg/FFmpeg ; render/encode/mix, not a creative director.
- **Claude Animation Base** — https://github.com/JohnHeibel/ClaudeAnimationBase ; p5.js brush-driven Clawd animation kit.

## Constraints

A legitimate **one-off single prompt** can work for simple animation, but precise motion relies on coherent source, deterministic timing and actual frame-by-frame inspection. Do not assume matching a screenshot means matching the final video. License fonts, voice likeness, music and image assets separately. Open-source code licenses may not cover reference demo footage.

Related: [25 — Stickman Animation](25-STICKMAN-PROGRAMMATIC-VIDEO-WORKFLOWS.md), [48 — Design Video SEO](48-AI-DESIGN-VIDEO-SEO-MARKETING-REFERENCES.md), [19 — Agent Skills](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md).
