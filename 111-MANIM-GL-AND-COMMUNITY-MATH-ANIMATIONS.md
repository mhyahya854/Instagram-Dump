# 111 — Manim: Mathematical Animation Engine

**Source:** Screenshot 1 in the fourteenth Instagram batch (2026-10-26), headed **“Math Animations?”**, displaying a GitHub README banner “Manim — Mathematical Animation Engine” and its installation warning. Its screenshot shows the original 3Blue1Brown engine rather than a generic Python renderer. The clip and play overlay are not project source code.

## Verified original and fork

- Original: **https://github.com/3b1b/manim** (creator-maintained **ManimGL**, Python package `manimgl`; uses OpenGL).
- Community edition: **https://github.com/ManimCommunity/manim** (separate **Manim Community Edition**, package `manim`), official documentation https://docs.manim.community/.
- README explicitly warns **the two versions have different installation commands, APIs and examples**. Never mix commands between them or assume 3Blue1Brown's old scene scripts run unchanged on CE.

## What it does

Precise code-authored explanatory motion: mathematical functions, graphs, coordinate axes, transformations, probability, calculus, geometric proofs, equations, SVG objects, camera movement and animations that illustrate *relationships rather than merely decorate*. Scenes are scripted and rendered to video (with optional OpenGL-based interactive preview in ManimGL).

## Original screenshots transcribed

- “Math Animations?”
- “Manim”
- “Mathematical Animation Engine”
- “Manim is an engine for precise programmatic animations, designed for creating explanatory math videos.”
- Visible note explains community and original editions.
- “Installation” and warning that **ManimGL instructions must not be used for Manim Community**.

## Project-fit notes

- Good for the user's educational/explainer animations, math diagrams, computer science concept films and offline knowledge demos.
- Not equivalent to **Three.js** (interactive browser 3D), **GSAP** (web timeline/tween), **Remotion** (React video), **ASCII terminal art**, or **Lemo Opuscar** film-direction skills.
- Set exact project package/environment and FFmpeg/LaTeX requirements; write reproducible scene source; test equation typesetting, fonts, aspect ratio, FPS, render time, narration sync and licensing.
- Keep generated scene code and input assets so future rendering needn't depend on a hosted service. Some dependencies/fonts/LaTeX still need external packages to reproduce offline.

## Evidence boundary

Two GitHub repositories verified, but **neither installed or executed**. No original scene recreated and no “Math Animations?” video was supplied for frame matching. Source https://github.com/3b1b/manim and https://docs.manim.community/en/stable/faq/installation.html .
