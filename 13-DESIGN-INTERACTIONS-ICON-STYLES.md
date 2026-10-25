# Reel Notes 13 — Practical UI Patterns, Anti-Slop Design and Icon Style Vocabulary

_Captured 2026-10-25. Existing avoid-by-default design rules remain in force._

## A. Visual hierarchy: one hero, supporting information quiet

Reel idea: Make one important interface element visually dominant, support it with two medium elements and keep lesser details quiet using size and contrast. **Interpret “one big, two medium” as an illustrative hierarchy, not a mandatory three-element layout**.

Example: task dashboard showing the next urgent task prominently; due date and owner clearly nearby; metadata less prominent but still readable. Hierarchy is created through relative size, spatial grouping, semantics and contrast, not by replacing information with huge decorative headings.

**Avoid:** every component demanding equal attention; large generic hero text; hidden key details; insufficient accessible contrast.

## B. “60–30–10” color proportion rule

An informal composition heuristic: roughly **60% base/background**, **30% supporting surfaces/content**, and **10% accents**. It may help restrain a visually chaotic palette, but actual distributions vary across screens, dark mode, brand needs, accessibility and density. **It does not require purple, beige, pastels or any particular palette.**

Assign color **jobs** (semantic status, interaction state, hierarchy), not just decoration. Ensure contrast under different backgrounds. Not every page should artificially contain three colors.

## C. Invisible submenu hover triangle (pointer intent)

Problem: a user moves a pointer diagonally from a top-level menu item toward an adjacent submenu, crossing another parent item. Naïve hover handlers immediately switch to the wrong submenu.

Design strategy: while a submenu is open, estimate a triangular/safe corridor from the pointer's recent position toward the near corners/edges of the open submenu. When movement is headed *toward the open submenu*, delay switching the parent row briefly; switch promptly when pointer clearly leaves corridor. This is a pointer-intent heuristic, not a security boundary.

Important implementation requirements:
- Use recent pointer positions, direction, geometry and a bounded grace delay; avoid sticky menus that refuse to close.
- Keyboard: arrows, Enter/Space, Escape, tab focus order; visible focus.
- Touch/mobile: tap-to-open or explicit disclosure, because hover is absent.
- Test zoom, responsive menu orientation, right-to-left interfaces and reduced-motion preferences.
- Accessibility often favors simpler click-activated menus rather than complex flyouts.

## D. Confirmation dialog design (better than empty “Are you sure?”)

Reel critique: centering all copy in a modal creates multiple alignment anchors; vague “Are you sure?” does not state consequence. Better:
- Title states **specific irreversible action**: “Delete this project?” or “Remove member access?”
- Short left-aligned body explains what changes and what cannot be recovered; keep one alignment anchor.
- Action label uses precise verb: “Delete project,” “Remove access” instead of generic “OK.”
- Provide a clearly visible cancel/escape option and appropriate default focus; prevent accidental destructive confirmation.
- Include confirmation when consequence justifies friction, not for every ordinary action.
- Use undo when genuinely possible; do not imply undo for irrecoverable changes.
- Accessible dialog labeling, focus trap/return, keyboard/assistive technology and mobile viewport tests.

### Example (copy only)

**Remove access for this member?**  
They will no longer be able to sign in or access private team resources. Existing sessions will be revoked according to the account policy.  
Actions: **Cancel** | **Remove access**.

## E. Anti-generic AI design transcript — normalize with caution

The repeated anti-pattern clip includes: ornamental stripes on rounded cards; borders on every block; color/italic text used merely as accent; all-caps labels above every heading; badges and status dots with no meaning; monospace labels and inputs everywhere; numbers written out or overly fussy typography (**transcription unclear**); noun-heavy long headlines; emoji/icon placeholders instead of real banners, logos and images; overstuffed screens; visual metaphors overexplained in labels; text-only fake demos; blanket glass cards; identical radii/shadows; illegibly light gray on white; purposeless motion; heavy hero/appearance animations; formulaic purple gradients and neon-dark grids; unverifiable proof.

These are **avoid by default unless explicitly requested**, not a ban on every card, border, icon, animation, gradient, shadow or mono font in every context. Full master rule: [01-DESIGN-UX.md](01-DESIGN-UX.md).

“Make it look less AI-generated” does **not** justify copying another brand's assets without permission. Design references should inform hierarchy, typography, spacing and interaction while maintaining legitimate licensing and original content.

## F. Icon taxonomy / visual vocabulary (reference only)

The reel rapidly dictates icon styles and some distorted names. Classify by independent dimensions; styles can overlap.

| Dimension | Types or spoken examples | Meaning |
| --- | --- | --- |
| Basic drawing | **Outline**, stroke/monoline, **filled**, glyph, solid, two-tone | Whether contour or filled shape dominates |
| Geometry | Sharp, rounded, squircle-like, angular, minimal | Corner and contour treatment |
| Line character | Thin monoline, heavier stroke, variable stroke | Width and rhythm of icon lines |
| Material family | Material Symbols **Outlined**, **Rounded**, **Sharp**; older Material **Filled** and **Two Tone** | Specific Google Material visual variants, not generic synonyms for all icons |
| Platform/system | System icon set, adaptive/dynamic/variable icons | Visual behavior can change with state, size, weight, platform settings |
| Surface | Flat, glossy, textured, soft UI/neumorphic | Surface rendering; avoid decorative skeuomorphism by default |
| Dimensional | 2D, isometric, “classic 3D,” realistic 3D | Degree of perspective and physical shading |
| Color/light | Monochrome, color-filled, colorful glyphs, neon, blur/glow, highlighted | Purposeful palette/light treatment |
| Pixel | Pixel art icons, low-resolution grid-aligned glyphs | Deliberate retro digital language |
| Motion | Animated icons, variable/adaptive icons | May communicate loading, state or transition; reduced-motion option |
| Meaning | Real-world metaphor (skeuomorphic), abstract symbol, pictogram | Familiar object analogy versus abstract mark |
| Experimental | AI-generated, generative, hybrid media | Not inherently more accessible or authentic |

**Uncertain wording from the reel to preserve (not assert as named families):** “relay system icons,” “zero style,” “skew,” “fixed,” “access symbols,” “outline assets symbols,” “pilot icons,” “multiple icons,” “3D and icons,” “classic 100% 3D.”

**Icon design evaluation:** recognizable meaning without nearby paragraphs, accessible text label for non-decorative icons, consistent sizes, hit areas, semantic colors, focus/touch, correct license, light/dark use, and actual images/logos for people and businesses rather than emoji placeholders.

## G. Reusable pattern testing checklist

- [ ] One dominant action/idea is obvious without giant generic headings.
- [ ] Text and icons pass contrast and assistive technology checks.
- [ ] Any submenu works with pointer, keyboard and touch.
- [ ] Confirmation dialogs describe actual consequences and clear verbs.
- [ ] No “thanks” screen unless real server-side action succeeded.
- [ ] No fake numbers, avatars, logos or testimonials.
- [ ] Hover and animations indicate behavior, not unrelated motion.
- [ ] Icon aesthetic is chosen for the brief, not sprinkled uniformly on all screens.
- [ ] Avoid decorative purple gradients, repetitive card triples or faux glass by default.

## References

- Existing design rules: [01-DESIGN-UX.md](01-DESIGN-UX.md)
- Design style library: [04-DESIGN-STYLE-LIBRARY.md](04-DESIGN-STYLE-LIBRARY.md)
- WAI ARIA Authoring Practices (menu/navigation/dialog): https://www.w3.org/WAI/ARIA/apg/
- Material Symbols: https://fonts.google.com/icons
- Fitts’s Law and familiar interface conventions: [07-45-UX-LAWS-ENGLISH.md](07-45-UX-LAWS-ENGLISH.md)


## Additional UX interaction reference

[22 — UX Motion, Typography, Touch & Trust](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md) expands the icon taxonomy with touch target sizing, meaningful loading, unverified “Linking Orbs,” social-media type sizing versus web UI and manipulative paywalls. [18 — UI Critique & Visual Taxonomy](18-LEARNING-UI-CRITIQUE-VISUAL-TAXONOMY.md) separates the mechanism of a visual idea from an aesthetic.

## UX extension: touch and motion

[22 — Motion, Typography, Touch and Trust](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md) adds platform-specific touch target sizing, honest progress, a social-graphic type-scale example and manipulative paywall cautions. [18 — Visual Taxonomy](18-LEARNING-UI-CRITIQUE-VISUAL-TAXONOMY.md) covers meaning-making mechanisms rather than visual styles.
