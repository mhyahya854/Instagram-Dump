# 123 — Five Original Image-Editing Prompts (Exact Screenshot Text)

**Source:** five orange screenshot slides (#5–9), four of which display original carousel sequence numbers `04`, `05`, `06` in the corner. These are **prompt templates**, not proof a model can preserve every pixel or identity perfectly. The visible text is transcribed **without silently fixing source typos, repetitions or grammar**. Later operational guidance is separate.

## Source slide 1 — REMOVE ANYTHING

```text
“Remove [OBJECT/PERSON] from this image completely and realistically reconstruct the area behind it.Match the original background, lighting, shadows, textures, reflections, depth, and perspective so the edited area blends naturally. Keep every other part of the image exactly unchanged.”
```

## Source slide 2 — CHANGE THE BACKGROUND

```text
“Replace the current background with [NEW/BACKGROUND] while keeping the main subject unchanged in identity, face, body, clothing, hairstyle, pose, and proportions. Adjust only the the lighting, shadows, and perspective on the subject as needed so it blends naturally into the new environment.”
```

## Source slide 3 — CHANGE THE OUTFIT

```text
“Replace the current outfit with [OUTFIT DESCRIPTION] while keeping the person’s identity completely unchanged. Preserve the face, hairstyle, body shape, pose, hands, skin tone, proportions, expression, and background. Make the new clothing fit naturally on the body.”
```

## Source slide 4 (corner number `05`) — EXPAND THE PHOTO

```text
“Expand this image beyond its current borders to [ASPECT RATIO, eg.16:9 or 4:5] while keeping everything inside the original image completely unchanged. Naturally continue the existing background, environment, floor, walls, sky, scenery, objects, lighting, textures, and patterns into the new areas.”
```

## Source slide 5 (corner number `06`) — COLOUR GRADE

```text
“Apply a professional colour grade to this image while keeping the skin tones natural and the subject unchanged. Balance highlights and shadows, refine contrasts and saturations, and give the whole frame a consistent, cinematic finish.”
```

## Exactness notes

- Screenshot #5 wording says `behind it.Match` **without a space**, recorded as visible.
- Screenshot #6 says `the the lighting`; deliberately retained rather than corrected.
- Screenshot #8 has `eg.16:9` and names background continuation.
- Screenshot #9 writes British `colour` and `saturations`.
- Slide heading `CHANGE THE OUTFIT` has corner `04` visible, and the latter two `05` and `06` — earlier orange cards don't show a legible corner sequence number; don't invent one.
- Image player arrows/translucent play overlay are screenshot UI, not part of the prompt.

## Practical implementation and editing quality

These commands describe goals, not deterministic pixel locks. To actually verify **“every other part unchanged”**, use masks/segmentation, defined inpainting regions, image diffs outside masks, consistent crop and color-space checks. Outpainting requires checking newly synthesized region geometry. Character/face/wardrobe editing on photographs should respect consent and not misrepresent evidence. When the result is used as testimony, news, identity verification or public advertising, disclose material edits as appropriate.

For a user-requested image edit, preserve source file and provenance, iterate visibly on target region, compare output at reference dimensions, flag irreversible or uncertain details, and never claim exact identity fidelity without evidence.

**No new images were generated in this archival task.** These are user-supplied templates stored in text, not instructions to retroactively edit the screenshots.
