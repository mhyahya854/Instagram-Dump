# 62 — Immersive Web Design: GSAP, Taste, 21st MCP and shadcn MCP

**Captured 2026-10-26.** A reel claims four “Claude skills” can create immersive websites. In reality these are **different categories**: animation instruction, design review skill, component marketplace connector, and open registry connector. None guarantees distinct designs or quality.

## Original voice transcription (normalized)

> “Now you can make this kind of immersive website using four Claude skills. First, **GSAP Animation Skill** for smooth kinetic text and animated components. Second, **Test skill** for anti-slop frontend framework guidelines so AI generates distinctive design. Third, **Twenty First Dev MCP connector**, a large collection of components. Fourth, **Shatsian UI MCP connector**, for more minimal, clean UI.”

Likely speech corrections: **“Test” → “Taste”** (probable, not proven) and **“Shatsian UI” → “shadcn/ui”** (strong). **GSAP animation skill** does not point to a unique creator. “Unique every time” is promotional; a component registry can encourage homogeneous designs if overused.

## Verified official resources versus community skills

| Tool | Primary source | Purpose | Critical limits |
|---|---|---|---|
| **GSAP engine** | https://gsap.com/ ; https://github.com/greensock/GSAP | High-performance timelines, ScrollTrigger, stagger, kinetic type and coordinated motion | The engine isn't itself a “Claude skill.” Version/license/performance and reduced-motion behavior matter. |
| **GSAP animation skills** | Multiple third-party candidates incl. https://github.com/kxwxn/gsap-animation-helper-skill and https://github.com/xerxes-on/gsap-animation-skill | Teach agents appropriate GSAP APIs and effects | **Exact reel skill unresolved**; inspect SKILL.md/scripts before use. |
| **Taste** | https://github.com/Leonxlnx/taste-skill | Design direction and avoidance of generic visual templates | **Probable transcription match**, not proven from original reel. May conflict with specific brand rules. |
| **21st MCP / CLI** | https://21st.dev/mcp ; https://21st.dev/ | Search component marketplace, use code/components, create variants | Current catalog advertises 12,000+ components; free tier has per-day code retrieval limits; API/login needed for some features; inserted code needs audit. |
| **shadcn/ui MCP** | https://ui.shadcn.com/docs/mcp | Search and install components from shadcn-compatible public/private registries | **Exact official docs verified**. Registry items can write source/dependencies; permits much more than a “clean look.” |

**Do not blindly install** the 21st CLI, add registries, or run a third-party skill from this research note.

### Recipe for original, accessible immersive design

1. Define product task, content hierarchy, and art direction before adding motion.
2. Maintain a persistent DESIGN.md and exact typography/color/spacing decisions; don't copy the design of another company.
3. Choose one or two motion roles: reveal state, spatial continuity, task feedback or narrative emphasis.
4. Use GSAP where its timeline/controller is technically justified; simpler CSS transitions can suffice.
5. Consider **one reviewed registry component at a time**, inspect all copied files/dependencies and adapt tokens.
6. Check reduced-motion preference, keyboard and touch functionality, content without JS where applicable, and unblocked primary action.
7. Run actual mobile browser/Lighthouse and automated integration tests, then watch a visual recording for bad pacing.
8. Declare success only with tested working product, not a cinematic landing screenshot.

## An example movement spec

**Hero:** title and real value proposition visible without an obligatory lengthy intro. Subtle stagger only if it reinforces reading order. Primary CTA never hidden behind scroll gating. **Feature preview:** one interactive real feature demonstration with explicit fallback when motion disabled. **Focus:** users can tab all controls and skip decorative effects.

## Why this doesn't require “immersion” everywhere

A banking/medical form, study portal or private journal often benefits more from responsive feedback and information clarity than elaborate kinetic words, parallax or horizontal scrolling. Motion is **optional** under earlier design rules. Test against page load, motion sensitivity and real conversion outcomes before retaining an effect.

Primary documentation:
- https://gsap.com/docs/v3/
- https://21st.dev/mcp
- https://ui.shadcn.com/docs/mcp
- https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html

Related: [19 — Agent Skills](19-AGENT-SKILLS-HOOKS-AND-CODE-ANIMATION.md), [22 — Motion/Trust](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md), [48 — Design](48-AI-DESIGN-VIDEO-SEO-MARKETING-REFERENCES.md).
