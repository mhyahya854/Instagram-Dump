# 25 — Real Stickman Stories: Programmatic Animation Workflow

_Captured 2026-10-25. Source: supplied transcript attributed to Instagram account "Real Stickman Stories". The original “comment stickman for guide” document, account ownership, video source files and exact prompts are **not available** from the spoken excerpt. This is a newly authored technical reconstruction, **not** a recovered creator guide._

## What the video actually describes

A story is selected from viewer suggestions. An AI coding agent and human author convert a script into animation code. **Stickmen** are vector shapes (circles/head, lines or joint chains for limbs) rather than hand-drawn frame images. A **timeline** changes shape positions/angles over time. Speech comes from a free text-to-speech model; effects like rain, doors and footsteps can be synthesized or constructed algorithmically. Frames and audio are combined into a video.

**Key distinction:** “Every frame is code” usually means a deterministic renderer draws each frame from a reusable description; it does **not** mean programmers manually write distinct instructions for every individual frame.

## Eight stages of a full production workflow

1. **Story selection** — collect user/comment ideas with consent, decide genre, constraints, content rating, duration and narration language. Don't imply a commenter transferred copyright.
2. **Writing** — prepare an original script, scene beats, dialogue with speaking roles, shots and recurring visual motif. Preserve consistent characters and screen geography across scenes.
3. **Storyboard and shot sheet** — number each shot, define duration, camera crop/pan, foreground/background layers, character positions, action and required sound. All shot durations must sum to the video duration.
4. **Stickman rig and graphics** — create reusable head circle, torso segment, upper/lower arms/legs and optional eyes/mouth. Associate joints in a parent-child hierarchy, define body scale, line width and palettes.
5. **Animate mathematically** — keyframe joint coordinates/angles and interpolate positions/easing across frames. Walk-cycle movement follows a repeatable oscillator; physically plausible motion uses pose constraints, foot contact and anticipation. Avoid inconsistent limb lengths or popping.
6. **Speech and effects** — generate synthetic voices with a locally usable licensed model or record consenting actors. Make sound effects via simple wave synthesis/filters/noise/envelopes or appropriately licensed effect libraries. Generated voice, model weights and music each have separate terms.
7. **Render/composite** — draw backgrounds/characters at fixed size/fps; overlay text/captions; mix synchronized dialogue, effects and optional music; export MP4 with video/audio encoders.
8. **Review and publish** — inspect story pacing, missing frames, audio clipping, voice consent, legibility, captions, audio levels, scene continuity and final export. Record source licenses and original credits.

## Independent example architecture

```
story.json (scenes, beats, dialogue, timing)
  -> shot_sheet.json (camera, characters, action, timeline)
  -> scene_renderer (SVG/Canvas/WebGL/HTML or Python)
  -> PNG frames or raw video at 24/30 fps
tts output -> WAV narration & timestamps -> captions
procedural sound -> WAV effects (rain, door, steps)
frames + voices + sounds -> FFmpeg composition -> MP4 -> playback QC
```

**Possible tools, not confirmed as the creator's exact stack:** HTML Canvas, SVG, JavaScript animations, Python drawing libraries, WebGL, FFmpeg; Python libraries for WAV synthesis; offline/open TTS models such as Piper or Kokoro where licenses allow use; Remotion for programmatic React video; `blixvip/html-anime` for agent-directed HTML drawing.

### Minimal rigging and timing pseudocode

```text
for frame in 0 .. totalFrames-1:
    seconds = frame / fps
    shot = shotAt(seconds)
    joints = evaluateKeyframes(shot.characterPose, seconds)
    enforceLimbLengthsAndFootContact(joints)
    drawBackground(shot)
    drawStickman(headCircle, torsoLine, limbSegments(joints))
    drawForegroundAndCaptions(shot)
    saveFrame(frame)
```

For a **30-second video at 30 fps**, plan **900 video frames**, plus a consistent soundtrack. Compression means the final MP4 need not store 900 full independent still pictures.

## Simple procedural sound: conceptual examples

- **Rain:** filtered white/pink noise blended with randomized droplet transients and stereo space, tapering with envelopes.
- **Door:** short creak with pitch modulation plus a percussive latch impulse; timing tied to on-screen swing.
- **Footsteps:** short filtered impacts whose intervals follow the walk cycle; different material textures use different filtering/decay.
- **Zombie ambience:** layered low-frequency drones, filtered vocal/growl samples only with appropriate rights, rhythmic variation and reverberation.

**Audio caution:** A procedure “made with code” can still incorporate copyrighted training samples or output. Verify model and sample licenses; don't clone an identifiable person's voice without authorization.

## Alternative video repositories found in neighboring research

| Project | Known use | Limit |
| --- | --- | --- |
| https://github.com/blixvip/html-anime | Agent-directed HTML animation/shot sheets | Not demonstrated to be the Real Stickman Stories tool |
| https://github.com/OpenCut-app/OpenCut | Open-source editor; classic branch for currently usable UI | Main repository is undergoing rewrite |
| https://github.com/jub0t/Concat | Local editor, captions, TTS, effects, MCP/API candidate | Project maturity/features need version checking |
| https://github.com/debpalash/VoiceStudio | Local TTS, voice design, cloning and dubbing | App/model licenses differ; resource requirements vary |
| https://github.com/FFmpeg/FFmpeg | Render/encode/mux audio and video | CLI toolkit, not one-prompt storyboard generator |

## From concept to reproducible offline project

Preserve editable `story.json`, `shot_sheet.json`, character-rig specification, deterministic RNG seed, renderer version/lockfile, fonts and licenses, local TTS weights/voice permission, audio sources, FFmpeg version and final exported video. Without model weights and source assets, Markdown notes alone will not re-create the result offline.

## Provenance

**Verified:** the general engineering pipeline is technically feasible. **Unverified:** source Instagram account identity, the precise “Real Stickman Stories” GitHub repository, direct download of the “stickman” guide, the creator's private prompt, and which free model generated the voices. Do not pretend to have recovered these.

## Addendum — related code-driven editing reels

**“Modern box” effect and 27,000-character code prompt:** the clip contrasts vague instructions with a detailed effect specification and claims 28 other premium effects. The actual 27K prompt is **not supplied**. The transferable lesson is to specify visual layers, sizes, color, camera perspective, timeline/keyframes, transition curves, lighting, video size, constraints and acceptance playback, **not** that long prompts inherently guarantee quality. A 27,000-character prompt can also be redundant or contradictory. Preserve compact canonical shot sheets rather than blindly maximizing character count.

**“500 viral Claude motion-video prompts”**: a credible related curated public lead is https://github.com/coolbat/awesome-opus-5.5-usecase and the separately referenced `awesome-opus5-5-videos` ecosystem. **Neither is proved to be the exact Instagram repo.** Browse/read examples and licensing before adapting; model/version and rendering results can change.

**Creator video 'Waffle' and six daily animations:** truncated anecdote. “Six videos a day,” “one-day editor challenge,” exact source filmmaker and elapsed production time are not independently validated. Don't use as a production benchmark. Use storyboards, full render checks and originality instead.
