# 106 — Lemo Opuscar + Remotion: Code-Rendered Film and Motion Graphics

**Source:** two separate user-uploaded screenshots: (a) GitHub preview of `lemomo-ai/lemo-opuscar`, saying “A toolbox of film styles made in code for Claude Code: 59 ready to use, and your own,” badges **59 film styles**, **free**, **MIT**, **6.6k stars** (snapshot claim); (b) cropped word **“remotion”** with no features shown. These are different projects. The item counts, license badge and stars reflect the source image time—not an enduring guarantee.

## I. Lemo Opuscar — exact GitHub source

**Verified:** https://github.com/lemomo-ai/lemo-opuscar

### What the actual repository offers

- A Claude Code agent plugin/skill and code-driven rendering toolkit for **59 film styles** (upstream description at this capture).
- Each style has its own `STYLE.md`, a demo film, and guidance files `DIRECTOR.md` / `TECHNIQUE.md` for storytelling, rendering and audio.
- The agent can use a library style, adapt it into a personal reusable style or start from a blank style spec with a preview/approval step.
- Typically uses **Node 20+, ffmpeg and Python 3.11+ or uv**. The repo describes original code-rendered frames and audio workflows, not a universal one-line video-model call.
- Output example: 1920×1080 at 24 fps, with alternative aspect ratios if requested.
- **Licensing:** repository says **code/docs MIT**, but demo films/stills are generally **CC BY 4.0**, and certain included voice clips / third-party assets have exceptions. **Do not use “MIT” badge to imply every video, asset or audio track is MIT.**

### Original screenshot exemplars (all five screenshot preview labels)

- Watercolor Brush
- 16-bit Pixel RPG
- Mid-century Cartoon
- Crayon Picture Book
- Ukiyo-e
- “+53 more” shown in preview, i.e. 59 total advertised styles.

### Other styles independently found in README (not screenshot)

- Evidence-film techniques: Satellite Briefing, LiDAR Survey, Engineering Briefing Board, Microscope Story.
- Art/media: One-line Drawing, Chinese Ink Wash, Blueprint, Swiss Motion Graphics, Pictogram Motion, **ASCII / CRT Terminal**.
- Narrative/3D: 1930s Cartoon, 80s Cel Anime, Brick Toy, Tilt-Shift Miniature, Isometric Island.
- Diagram/video: Data Storytelling, Isometric Infographic, Living Screencast, Dark Tech Keynote.
- These are examples of the upstream library taxonomy, **not a request to copy exact copyrighted artwork**.

### Important trust boundaries

A plugin installer can download and execute code, create many frames and incur AI model/tool usage. Read `SKILL.md`, install scripts, `package.json`, ffmpeg calls, permissions, remote network requirements and included media licenses before using it. Generate only original footage/voice/music with permissions.

## II. Remotion — confirmed independent repository

**Verified:** https://github.com/remotion-dev/remotion · https://www.remotion.dev/

- React/JavaScript/TypeScript-based programmatic video creation. The application describes **React code as source of truth**, plus agentic and editor workflows.
- Component trees, composition frames, CSS/SVG/animation values, audio layers and rendering/export pipelines can be used to build scripted videos from data.
- Reusable design tokens/animated modules can standardize motion across videos, but do not guarantee storytelling quality.
- **Important license difference:** Remotion has its **own special license**, and certain commercial/company usages require a paid company license. Do not classify it automatically as MIT or unrestricted open source.

## III. Compare their roles

| Dimension | Lemo Opuscar | Remotion |
|---|---|---|
| Identity | Agent skill / styled film production workflow | React-first video framework and tooling |
| Starting point | Topic, film style, guide/storyboard | Timeline/compositions built from React code/data |
| Style inventory | 59 declared style categories (at capture) | Bring your own reusable code/style system |
| Narrative advice | Director/Technique/style guidance built in | You supply production direction; templates can help |
| Output | Video rendered from code and associated assets | Programmatic React-rendered video |
| License | MIT code/docs; CC BY and exceptions for media | Special commercial license |
| Safety | Plugin/skill may execute code and download tools/assets | Renderer, browser/runtime, user media and dependencies |

**Potential use together:** a structured film style guide informs design/story choices while Remotion renders a custom original video. Compatibility is **a design possibility, not a tested official integration**. Preserve per-frame verification, voice legality, captions, logo/font license, frame pacing and actual export files.

## Internal project references

[19 — Agent Skills/Animation](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md), [48 — AI Media](48-AI-DESIGN-VIDEO-SEO-MARKETING-REFERENCES.md), [63 — HyperFrames](63-TEN-AGENT-SKILLS-WEB-ASSETS-SLIDES-IOS-SUPABASE-MARKETING.md), [100 — Pure Python ASCII](100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py), [104 — ln Line Art](104-FOGLEMAN-LN-3D-VECTOR-LINE-ART-ENGINE.md).

**Status:** public repos verified, no skill installation, video generation, audio cloning, renderer execution or output-comparison test performed.
