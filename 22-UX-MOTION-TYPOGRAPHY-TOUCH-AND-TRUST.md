# 22 — New UI/UX Reels: Typography, Loading, Touch Targets, Motion and Conversion Ethics

Captured 2026-10-25. Visual design **references and rules to consider**, not a mandate to add every effect.

## 1. Generic AI design clichés — the newer “Claude look”

The reels criticize an old cliché (purple/blue gradients, glowing buttons and colored stripes on cards) and a newer cliché: **oversized italic serif editorial headlines paired with dark black/cream “old money” styling, often claiming elegance without underlying product substance**.

**Avoid automatically copying this pattern**. Large serif type or cream backgrounds can be appropriate when the actual brand calls for them. The problem is repeating a fashionable formula without a clear role, audience, content, performance or functionality.

Aesthetic quality depends on hierarchy, clarity, coherence, responsiveness, real imagery and real interaction behavior. An agent skill or copied screenshot does not guarantee taste.

## 2. Social-media typography scale reel

Spoken heuristic: “24 pixels minimum body, subhead 1.5×, heading 3×, title 6×, fine print 0.75× body.”

For a *social media graphic* using a 24-pixel base, the numerical example would be:
- Body **24 px**
- Subheading **36 px**
- Heading **72 px**
- Title **144 px**
- Fine print **18 px**

**Not a universal UI type scale**. Social-media graphic dimensions, screen density, contrast, export resolution and reading distance matter. A 144px title can overflow phone layouts, and a web body does not universally need 24 CSS px. For web, consider responsive sizing with readable line length, spacing, platform text scaling, browser zoom and WCAG reflow instead of hard-coded reel ratios.

## 3. Pre-launch functional website checklist

| Category | Check |
| --- | --- |
| Responsive layout | No unintended horizontal overflow; mobile viewport, long text, font zoom and touch targets work. |
| Navigation | Mobile menu, internal links, footer links, unused navigation, logo-home link and custom 404 are correct. |
| SEO/public metadata | Real page titles and descriptions, favicon, canonical/share metadata when relevant. |
| Contact | Email and phone are tappable with proper schemes; verify destination. |
| Content | No placeholder text, generic fake reviews, fake counters or stale copyright year. |
| Performance | Compress/responsively serve images without losing useful quality; avoid cumulative layout shifts. |
| Functionality | Buttons work and link to real actions; forms show actual server-confirmed success or meaningful errors. |
| Accessibility | Contrast, keyboard/focus, semantics, text resizing, labels and reduced-motion preferences. |
| Release | Test a production build and deployed pages, not only local preview. |

## 4. Tiny icon with large invisible hit box

The visible icon and **interactive hit target** can be different sizes. A 20–24px icon can sit inside an invisible 44–48-unit button surface, giving a comfortable finger target and preserving visual density.

**Grounded guidance:** Android recommends a **48 × 48 dp** target; WCAG 2.2 AA 2.5.8 generally requires **24 × 24 CSS px with exceptions**; many mobile-platform conventions aim around 44 points or more. CSS pixels, points and density-independent pixels are not interchangeable physical units. Avoid overlapping targets or stealing taps from nearby controls.

A smaller target can be problematic even if Fitts's Law is satisfied on desktop; test actual fingers, assistive technology and zoom.
Sources: https://support.google.com/accessibility/android/answer/7101858 ; https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum .

## 5. Loading perception and “airport baggage claim”

The story says a perceived wait may feel shorter when part of the time is occupied with a purposeful action instead of standing still. The precise “1983 airport” history and ratio are **not verified** here.

The reel's bookshelf-scanning app fakes four equal loading stages when the first three are instant and the fourth is slow. That may manipulate perceived progress, but **avoid falsely implying equal task completion or inventing stages**. Better:
- Fast acknowledgement immediately after upload/scan.
- Real stages, indeterminate spinner when unknown, or honest estimated progress with clear language.
- Explain meaningful work and elapsed/retry behavior; offer cancel/background action if appropriate.
- Do not show 75% complete when no measurable work has been accomplished.
- Preserve user trust more than optimizing subjective wait through deception.

## 6. “Linking Orbs” animation library

Reel claims dotted animated orb states, MIT license, reduced-motion support and zero performance slowdown. **Canonical repository not confirmed.** Preserve as research lead only; do not invent a GitHub link or accept performance/license claims without checking the actual files. Separate “example motion vocabulary” from “default interface design”.

The earlier rulebook already says **avoid radial orbs, gratuitous motion and skeletons by default**; this resource is **optional inspiration** only.

## 7. Five “$100M company visual rules” (clip incomplete)

- **Isolation / Von Restorff:** limited use of accent increases salience when everything else is visually calm; using brand color only on one button is an overstatement and may undermine broader brand needs.
- **“Pattern interrupt” paywalls:** abrupt theme reversal can demand attention, but deliberately startling users at payment creates manipulation and trust risk. Prefer clear, fair pricing disclosures and predictable checkout.
- **“Ban pure black/pure white”:** claim of inevitable OLED eye strain is overgeneralized; accessible contrast and user comfort are context-dependent. Off-black/off-white are **options**, not requirements.
- The reel announces **five patterns** but the supplied transcript cuts off after part of number three. **Do not invent patterns four and five**.

## 8. Why custom design context beats “make it prettier”

Use durable typography, spacing, semantic colors, component rules, content examples, interaction/animation principles, screenshots **with notes about which aspects to borrow**, and the established anti-cliché list. A prompt without a design specification leaves the agent to choose generic statistical defaults. Validate actual rendering through browser screenshots, visual review and accessibility tests.

## 9. References and boundaries

- [01 — Design UX](01-DESIGN-UX.md): avoid-by-default and employ lists.
- [07 — UX Principles](07-45-UX-LAWS-ENGLISH.md): aesthetic–usability, Fitts, Von Restorff, peak-end.
- [13 — UI interaction/icon vocabulary](13-DESIGN-INTERACTIONS-ICON-STYLES.md).
- [17 — Design websites](17-DESIGN-WEBSITES-AND-COMPONENT-LIBRARIES.md).
- [19 — Design skills and hooks](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md).
