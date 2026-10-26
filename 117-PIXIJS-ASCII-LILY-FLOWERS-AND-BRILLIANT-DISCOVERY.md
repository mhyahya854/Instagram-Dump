# 117 — ASCII Lily Bouquet with PixiJS + Brilliant.org Lead

**Source:** two independent Instagram comment screenshots, not a single demonstrated project. **Image 15** shows account `arimecoa` caption **“ASCII lilly bouquet”** and hashtag `#uxui #vibecoding #ascii #motion #design`; visible comment by `mekayalar` says **“Pixi js + vectoral flowers + pixi js ascii filter 👏”**. Preserve misspelling **“lilly”** and phrase **“vectoral flowers”** as exact quoted source, not an identified official tool named “vectoral.” **Image 16** shows commenter `chatpati._mahila01` asking **“Name ?”** and account `elle.tutors` answering **“brilliant.org”**. The referent of “Name?” is not shown.

## 1. ASCII Lily Bouquet — grounded technical reconstruction *concept*, not original source code

Screenshot supports **PixiJS**, **vector-drawn flowers**, **PixiJS ASCII filter**, and animated/ASCII appearance as creator/commenter explanation. **No complete original video, repository, full frame sequence or source code was provided**, so an exact reproduction or effect algorithm **cannot** be claimed.

### Verified technical components

- **PixiJS:** https://github.com/pixijs/pixijs — GPU-backed web graphics engine for 2D scene graphs, particle/shape rendering, filters and animation.
- **pixi-filters:** https://github.com/pixijs/filters — community filter package with **`AsciiFilter`**. Upstream README lists `pixi-filters/ascii` with examples.
- **Vector flowers** can be generated from mathematical Bézier paths/petal polar formulas using PixiJS Graphics or prebaked SVG converted into textures. “Vectoral flowers” isn't necessarily a library name.
- Composite: draw bouquet shape/petals/stems with vectors, animate growth/sway/bloom, apply character-grid luminance mapping as a screen-space post-processing filter. Sample resolution, contrast, font/glyph cells, antialiasing and performance dramatically affect result.
- Export: browser animation remains interactive until frames are captured and encoded separately, with rights-cleared audio if included.

### Potential project plan (independent proposal)

1. Build one SVG/vector lily with five/six petals and stem, visible on a plain high-contrast canvas.
2. Create multiple flower instances from seeded values to make a repeatable bouquet.
3. Animate easing and stem bending with small temporal phase shifts, respecting reduced-motion preference.
4. Render to PixiJS stage and apply the **version-compatible `AsciiFilter`** (verify PixiJS v8 / pixi-filters compatibility before importing).
5. Tune character density, color handling, frame rate, scale and snapshot/export quality.
6. Compare to *actual full video* only if subsequently available; present as an inspired original rather than exact reconstruction.

**Important difference from earlier user request “ASCII art IN PYTHON ENTIRELY”:** this technique is JavaScript/PixiJS/WebGL, not standard-library Python. The independent [100 — Python ASCII demo](100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py) is a different method and cannot be described as the video's original code.

## 2. Brilliant.org, a separate clue

**Source exact reply:** `brilliant.org`.

**Verified site:** https://brilliant.org/ — interactive lessons for math, computer science, science and quantitative reasoning. It is **educational interactive content**, not a GitHub ASCII rendering framework or guaranteed free/open-source asset library. Source screenshot provides **no context about the specific lesson, video or tool** being named, so avoid attributing a particular curriculum or effect.

## License/privacy/performance notes

Review PixiJS and filter versions/licenses, inspect untrusted npm packages, preserve original creators' art rights. Never copy an Instagram user's art or brand assets without authorization. Disable heavy animations for reduced-motion/low-power devices. Do not infer Brilliant endorsement by the ASCII creator: these were different screenshots.

**Status:** two comment references captured, repo/site existence verified; no Pixi scene written or rendered, image/video recreated, lesson account opened or plugin installed. Related [101 — ASCII Notes](101-PURE-PYTHON-ASCII-ART-RESEARCH-NOTES.md), [88 — Motion Sites](88-UI-UX-ANIMATIONS-SIX-SOURCES.md).
