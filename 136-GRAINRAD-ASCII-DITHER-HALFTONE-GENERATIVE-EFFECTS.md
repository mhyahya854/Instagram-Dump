# 136 — Grainrad.com: ASCII, Dithering, Halftone, and Image/Video/3D Effects

**Source:** image 9 (sixteenth batch). A black-and-white textured horse, bold overlay **“Grainrad.com”**, and an editor sidebar are visible. **This is not evidence of which settings produced that specific horse composition**; original file and slider values are unavailable.

## Verified website

- **https://www.grainrad.com/** / https://grainrad.com/
- Online editor accepts PNG/JPG still images, animated GIF, MP4/WebM video, and GLB 3D models according to the current UI. It shows an input-dropzone, effects, preview adjustments and export controls. Current effect categories on the site:

```text
ASCII
Dithering
Halftone
Matrix Rain
Dots
Contour
Pixel Sort
Blockify
Threshold
Edge Detection
Crosshatch
Wave Lines
Noise Field
Voronoi
VHS
```

**Controls observed in site UI:** ASCII scale, spacing, output width, character set, brightness/contrast/saturation/hue rotation/sharpness/gamma; adjustable color mode/background/intensity; processing/post-processing, presets and export selection.

**Output choices displayed:** PNG, JPEG, GIF, MP4, SVG, **text `.txt`**, Three.js `.html`. *These are interface options, not proof every input and filter supports every output, free-tier size, resolution or offline processing.* No license/source repo was verified, so do not label the website open source or imply free commercial asset rights.

## Distinctive visual reference

High-contrast isolated subject (horse) with procedural screen-tone texture, rough scanning/line raster appearance, typographic overlay and grayscale aesthetic. Use to study the **image-to-glyph mapping**, dithering, scale/contrast thresholds, ordered diffusion versus error diffusion, export formats and motion coherence.

### Reproduction workflow without copying creator's protected source

1. Pick **licensed original image** or user-owned asset.
2. Convert to luminance; decide pixel cell width and glyph aspect ratio; separate source image colors from display/ink palette.
3. For ordered/error-diffusion dithering, test pattern spacing and moiré at 100% display size.
4. For motion, ensure cell/glyph stability across frames (temporal coherence), avoid seizure-triggering flashes, allow motion reduction and cap GPU/CPU time.
5. Preserve alpha/background and export to target media type with correct pixel-density/rasterization.
6. Compare readability, compression and accessibility; never hide crucial text inside decorative ASCII.

## Related earlier source

[117 — PixiJS ASCII Lily Bouquet](117-PIXIJS-ASCII-LILY-FLOWERS-AND-BRILLIANT-DISCOVERY.md) identifies **PixiJS + vector flowers + PixiJS ASCII filter** as a separately described web animation approach. [100 — Pure Python ASCII](100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py) is an independent standard-library example, not Grainrad's code. [101 — Python Research](101-PURE-PYTHON-ASCII-ART-RESEARCH-NOTES.md) explains algorithmic approaches. Grainrad web editor is a **service reference**, not a verified Python implementation.

**Status:** website verified and screenshot archived. No images uploaded, effect edited, website assets saved, original horse artwork reused or code installed.
