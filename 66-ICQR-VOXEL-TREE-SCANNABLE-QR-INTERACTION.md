# 66 — ICQR Magic Tree: A Voxel Tree Built From a Scannable QR Code

**Captured:** 2026-10-26. **Input source:** user-uploaded screenshot (text only; no original video or code). **Original public experience:** https://tree.icqr.com/ (**confirmed**). Research references are below. This note is a standalone engineering/design case study for the offline-first Instagram-Dump archive, **not** an actual recreation or copied original source.

## 1. What the supplied screenshot actually says

> “ICQR turns any link into a voxel tree. The ground it grows on is the actual QR code: tap the tree and it folds back into a scannable QR.”

The screenshot explicitly lists:

- **Three seasons:** spring, summer, autumn.
- **User picks the leaf color.**
- **Ambient sound.**
- **Export in one click.**

The screenshot **does not** identify a specific export file format, technology stack, creator, GitHub repository, software license, device support, screenshot of the running app, source-code availability, or proof that every generated QR scans. Do not fill those details from the image alone.

## 2. Independent research: the real ICQR site

- **Original live app:** https://tree.icqr.com/ — page title “ICQR Magic Tree — 3D QR Code Generator.” The site is an interactive browser experience rather than a GitHub repository identified in this research.
- Contemporary third-party explanations describe **procedurally generated branching trees** on a QR-derived plot, three seasons, palette variants, ambient sound, transition to a flat code, and client-side generation.
- An independent gallery describes the original as hand-written **WebGPU/WGSL** with an **L-system** branching model. **This is secondary-source technical reporting, not original published source-code verification; keep it qualified.**
- No publicly licensed **first-party ICQR source-code repository** was verified in this research. A community project referencing ICQR as inspiration does **not** become its official source.

**References:** https://tree.icqr.com/ ; https://www.designtoolmark.com/resources/detail/tree-icqr ; https://itscai.com/icqr-magic-tree/ .

## 3. The actual design idea

**What makes this interaction novel is not merely “a tree next to a QR image.”** The **QR matrix is the scene's structural ground**, and changing perspective or morphing foliage returns the user to a reliable, machine-readable code. The tree is the initial visual invitation; the scan state is the real utilitarian artifact.

### UX states

1. **URL entry** — user supplies a destination; validate supported URL protocols and size/capacity.
2. **Choose look** — pick spring, summer or autumn; choose leaf/palette color.
3. **Tree state** — QR plot becomes the scene floor/terrain; the tree grows above it, with optional ambience.
4. **Reveal QR** — a clear “Reveal QR” control *or* interaction with the tree moves to a top-down, unobstructed code.
5. **Scan state** — the code has high contrast, preserved quiet zone, stable finder/alignment/timing patterns and no obscuring foliage.
6. **Export/share** — user saves a usable artifact or copyable link. **Original screenshot promises one-click export but does not specify PNG, SVG, MP4, video or other format.**
7. **Return/edit** — user can go back to tree view, change look, or replace URL without losing accessible scan/export functionality.

**Important:** A decorative isometric view may **not** be reliably scannable; a **dedicated flat scanning view** is essential. A camera scan is not the same as visually recognizing a QR pattern.

## 4. Engineering reconstruction from first principles (new interpretation, not ICQR source)

```text
input URL
  ├─ URL validation & normalization
  ├─ QR encoder → matrix of light/dark modules
  │    ├─ data + error correction
  │    ├─ finder/alignment/timing patterns
  │    └─ four-module quiet zone
  └─ stable seed (URL + generator version)
       └─ procedural branches / leaf positions / season colors
            └─ GPU-instanced tiles, voxels, foliage and camera
                 ├─ isometric animated tree view
                 └─ QR reveal t ∈ [0,1]
                      ├─ flatten/remove obstructions
                      ├─ align to exact QR module coordinates
                      ├─ switch to overhead orthographic view
                      └─ increase reliable light/dark contrast

scan renderer → reproduce the original encoded matrix exactly
export renderer → use canonical QR matrix (not an arbitrary 3D screenshot)
```

### Invariants that must stay true

- **Encoded information:** the same URL generates the same QR code and scanning returns the expected URL, not a visually similar address.
- **Finder/timing/alignment regions:** do not overwrite machine-readable QR functional patterns.
- **Quiet zone:** maintain a margin of at least **four modules** around the code in the finished scan/export view.
- **Contrast:** palette colors in the **tree state** are free; scan-state modules must become reliably light/dark enough for mobile camera binarization. Pretty pastel foliage isn't automatically QR-safe.
- **Geometry:** keep each QR module in its correct grid cell; avoid seams, height variations and shadow/gradient crossings in the final flat view.
- **Occlusion:** branches, text, dock and grass must not cover code/quiet zone when revealed.
- **Determinism:** optional hash-based stable seed makes the same URL/style re-create the same tree, independent of display resolution.
- **Export:** produce a crisp canonical code independent of WebGPU lighting; do not export a perspective view and call it scannable.
- **Fallback:** on unsupported GPU/browsers or reduced-motion settings, offer a static QR without losing functionality.

**Why QR error correction doesn't solve everything:** level H can recover on the order of **30% codeword damage** under ideal decoding assumptions; it does **not** mean 30% arbitrary pixel coverage, missing finder patterns or destroyed contrast is safe. Measure actual decode success.

### Motion direction

- Growth should signal the mapping between URL → tree rather than distract from obtaining the code.
- Reveal animation should make the transformation understandable: foliage/geometry resolves into or moves clear of modules; camera rotates/zooms overhead; code stabilizes.
- Use short intentional easing and deterministic end states. A quick reveal is usually preferable to a forced lengthy theatrical animation.
- **Reduced-motion:** skip or shorten camera/leaf movement and show flat QR instantly when user requests.
- **Sound:** three season-specific generated/recorded ambience options, muted by default or gated behind explicit user interaction to satisfy browser autoplay and accessibility. Sound never required to find or scan QR.
- **Color picker:** affects foliage/season look independently of the high-contrast scanning representation.

## 5. Four related open-source GitHub projects (NOT the original)

| Independent repository | Stack and approach | Distinguishing engineering evidence | License/status |
|---|---|---|---|
| **Slifronic/magic-tree** — https://github.com/Slifronic/magic-tree | React 19 + Three.js + TypeScript/Vite; ground is instanced QR tiles. Every leaf maps to a destination dark module and morphs as camera turns overhead. | Details **six leaves per dark module**, same-height 3×2 leaf target layout, H error correction, four-module quiet zone, URL-hash seeded growth; **reports** 64/64 local settled-view jsQR decodes across tested styles, not universal proof. | README states MIT; independent work explicitly credits ICQR idea and says no original code/art/branding used. |
| **lavine888/QR-Worlds** — https://github.com/lavine888/QR-Worlds | React Three Fiber, Three.js, TypeScript. **QR-native voxel columns:** the matrix itself is an instanced cube terrain; switch from isometric sculptural perspective to orthographic scan. | Uses qrcode-generator and ZXing browser decoding; explicit crisp PNG/SVG QR export and QR validation; local-only in README. | README states MIT; independent implementation. |
| **JULESlois/3D-QR** — https://github.com/JULESlois/3D-QR | Three.js generative 3D QR scene; treats **scan polarity** and **structural zone** as independent cell properties. | Proposed invariant: orthographic QR projection matches the original matrix. Light cells can contain light-toned geometry; final projection must still preserve readable polarity. | Public repo; inspect actual license and implementation before reuse. |
| **AlbertAZ1992/every-qrcode** — https://github.com/AlbertAZ1992/every-qrcode | React/Web Component plus low-level TypeScript + WebGPU/WGSL tree/terrain renderer with lazy loading. | Deterministic versioned visual identity, canonical matrix scan state and **static SVG fallback** on unsupported WebGPU; npm packages. | README states MIT; separate project; check package release and dependencies. |

### Why keep all four?

They demonstrate **four distinct reconstruction strategies**: (1) foliage-to-modules morph, (2) QR-native block landscape, (3) orthographic projection constraints, and (4) reusable WebGPU component plus safe fallback. Do **not** misrepresent these as forks of ICQR or as evidence the original site published its source.

### Similarity/recreation boundary

For a new app, borrow **the general interaction mechanism** (animated QR-encoded visual metaphor → correct scannable view) and build original branded art. Don't copy ICQR's proprietary code, entire interface, original animation frames, music, trademark/branding or published asset files without permission. Public source repos have their **own** license terms.

## 6. Test plan — functionality and visual quality, not promotional “100%”

| Test | Acceptance / actual evidence needed |
|---|---|
| Short and long links | URL validation and QR capacity handling are correct; errors explain limits |
| URL equivalence | Scan output decodes to the exact intended normalized URL |
| Seasons/color | All three seasons and multiple leaf swatches return the **same payload**, independent of appearance |
| Scanner reliability | Decodes using at least one software decoder and real iOS/Android cameras at realistic screen sizes and lighting; count success rates for each set |
| Finder/quiet zone | Compare rendered module matrix and structural margins against encoder |
| Interactive reveal | Click/tap/keyboard activate; no missed states, no displaced UI covering QR |
| Responsive/accessible | Small mobile, landscape, high zoom, keyboard, screen reader; no inaccessible canvas-only functionality |
| Motion/audio | Respect prefers-reduced-motion, stop/restart, mute, autoplay restrictions; no aggressive sound |
| Performance | Measure GPU CPU/frame rate, memory, page weight and battery on modest mobile devices |
| Export | Verify exported file or share link exists, is readable, and embeds the **right target**; don't infer export format from screenshot |
| Offline/privacy | Verify whether any URL or media leaves device with browser network inspection; do **not** assume local-only based solely on social claims |
| Browser fallback | If WebGPU fails, a static high-contrast QR still works |

## 7. Archive status

- **Source screenshot:** text transcribed and classified, but original screenshot bytes are **not committed**.
- **Original ICQR site:** found, public UI accessible as a link.
- **Original first-party code:** not verified/open-source.
- **Independent GitHub implementations:** four public repositories identified/confirmed, not installed or executed.
- **Actual QR/device scans:** **not performed**; cited results are upstream self-reports.
- **Future scope:** design inspiration, creative coding, QR correctness, Three.js/WebGPU/procedural graphics, accessibility and export QA.
