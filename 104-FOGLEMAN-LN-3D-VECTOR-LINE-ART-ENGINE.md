# 104 — `fogleman/ln`: 3D Vector Line Art Engine (Source Screenshot)

**Source screenshot:** single narrow GitHub image clearly reading `fogleman / ln`, repository `ln`, visibility `Public`, branch `master`. No instructions or visual outputs from the project were shown. **Canonical verified source:** https://github.com/fogleman/ln .

## Actual project, independently verified

The README calls `ln` **“The 3D Line Art Engine”**. It is written in **Go** and transforms 3D primitives, polyline textures and meshes into **2D vector paths**. Unlike a regular raster renderer, it can output **SVG**, useful for plotters and graphic art, or rasterize those paths as PNG.

### Technical capabilities reported upstream

- Geometric primitives: sphere, cube, triangle, cylinder, 3D functions.
- Import meshes: OBJ and STL.
- Custom “texturing” defined as surface lines (not ordinary image textures).
- Constructive solid geometry: union, intersection, difference.
- Ray-intersection visibility testing so hidden scene paths don't appear.
- Camera and transformation from 3D lines to 2D image plane; final PNG or SVG export.
- Creator motivation: draw 3D scenes with a physical XY pen plotter.
- MIT license as identified on GitHub; inspect full license and pin version for any distribution.

### Pipeline from first principles

```text
scene objects / curves / surface path definitions
  → fragment paths at a chosen spatial sampling step
  → camera-directed ray visibility / hidden-line rejection
  → project surviving 3D paths into 2D viewport
  → organize 2D line strokes
  → SVG vector output or PNG raster preview
  → optional physical plotter/pen drawing
```

This differs from:
- **ASCII art**, where each pixel is a terminal character.
- **Voxel art**, where 3D volume is made of grid cells/cubes.
- **Remotion/HTML video**, which creates full video frames rather than vector visibility paths.
- **LLM-generated image**, where a model invents pixels; ln computes geometry and occlusion.

## Where it belongs in our project idea library

- Generative isometric technical diagrams, perspective line landscapes, blueprint product visuals.
- Mechanical/architectural sketch art and physical plotter output.
- An alternative original look to overused gradient/glow template pages.
- If animating, re-render a sequence of geometric camera or scene states with a separate frame compositor; **ln is not presented upstream as a full timeline video editor**.

## What to test before adoption

Set up a small 3D scene, inspect camera clipping, hidden surfaces, SVG path fidelity, sharp corners, dense mesh render time, output license/size and whether the Go maintenance/API fits an app. Use a sandboxed fixture; don't call repo functionality “pixel-perfect” merely from a screenshot of GitHub.

**Status:** canonical repository verified via connected GitHub; source not cloned, executed or modified. Source screenshot's partial browser page is preserved as text only. Related [100 — Python ASCII](100-PURE-PYTHON-ASCII-ART-AND-ANIMATION.py), [66 — ICQR](66-ICQR-VOXEL-TREE-SCANNABLE-QR-INTERACTION.md), [106 — Code Films](106-LEMO-OPUSCAR-REMOTION-CODE-FILM-MOTION.md).
