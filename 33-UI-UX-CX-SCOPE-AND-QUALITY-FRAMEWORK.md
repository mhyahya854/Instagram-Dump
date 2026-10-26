# 33 — UI, UX and CX: Scope, Responsibilities and a Practical Quality Model

Captured: 2026-10-25 from Instagram UI/UX/CX spoken list. **This is a conceptual classification, not a command that all projects need every activity.**

## Original distinction, corrected

**UI (User Interface)** = the visible, audible and interactive surface through which a person controls a product. The reel groups colors, typography, spacing, layouts, icons, buttons, visual design, interaction design and motion design here. **UI is not just “looks good”;** focus states, accessible controls and interaction behavior matter.

**UX (User Experience)** = how well people achieve their goals across a product journey, including research, product strategy, information architecture, content strategy, flows, wireframing, prototyping, usability and real-world functional convenience. Good UX is not merely speed or efficiency; it includes trust, comprehension, inclusion, emotional experience and recovery from mistakes.

**CX (Customer Experience)** = the broader relationship with an organization beyond one app: advertising and expectations, brand promises, discovery, sales, purchasing, account onboarding, support, delivery, billing, service recovery, retention and cancellations. “Knowledge,” “product story,” “office,” brand/marketing/sales/customer-service strategy were all spoken; **“office” is unclear**, possibly internal operations, not a formal CX pillar.

## Three related scopes

| Dimension | UI: interface itself | UX: using the product | CX: interacting with the business |
| --- | --- | --- | --- |
| Main question | Can I see, understand and control it? | Can I accomplish the right job safely and efficiently? | Does the organization fulfill its promise across touchpoints? |
| Typical disciplines | Layout, color, type, buttons, labels, animation, component states | User research, accessibility, IA, content, task flows, usability, prototypes | Brand, support, marketing, billing, sales, service reliability and journey mapping |
| Sample defect | “Submit” has no visible focus or loading feedback | Form loses entered fields after validation fails | Sales promised refunds, but support rejects valid requests |
| Success measures | Contrast, target size, recognizability, state feedback | Completion rate, errors, time, perceived ease, retention where useful | Complaint/recovery trends, resolution time, trust, customer outcomes |
| Good handoff | Component specs + states + semantics | User journey + research + acceptance tests | Cross-team ownership + truthful promise + support/escalation plans |

These domains **overlap**: a button is UI, a failed checkout is UX, and the return/refund experience is CX. “UI looks good, UX works well” is a useful mnemonic, **not a rigorous boundary**.

## Practical end-to-end example: booking a consultation

1. **CX acquisition:** advertising accurately describes the service, eligibility, prices and availability.
2. **UI page:** readable typography, clear CTA, logical form layout, keyboard/touch/focus, appropriate feedback.
3. **UX workflow:** user finds a suitable option, enters details once, recovers from errors and receives real confirmation.
4. **CX after purchase:** calendar reminder, accessible rescheduling, clear support and actual fulfillment of booked service.
5. **Cross-cutting:** privacy, security, ethical consent, consistent information and operational reliability.

## What to examine for each project

### UI review
Color roles and contrast; typographic hierarchy and responsive text; meaningful spacing/grouping; component states, icons, hit areas, real imagery, coherent grids, keyboard/touch interactions; motion as feedback rather than decoration.

### UX review
Target users/jobs and contextual constraints; navigation/information architecture; content clarity; first-use and recovery flows; prototype and usability testing; error prevention; accessibility and real-world convenience; durable task completion and truthful status.

### CX review
Promise-to-delivery consistency; service blueprint; customer acquisition and support access; account, purchase, invoicing/cancellation/refunds; trust, privacy and accurate marketing; escalation/recovery and feedback loops.

## Cross-reference to the existing standing rules

- [01 — Design & UX](01-DESIGN-UX.md) is the master anti-pattern and usability reference.
- [02 — Vibe-Coded App Quality](02-VIBE-CODED-APP-QUALITY.md) governs working flows, authentic content and release completeness.
- [12 — Marketing/Pricing/Homepages](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md) is a CX/marketing supplement.
- [18 — Learning UI Critique](18-LEARNING-UI-CRITIQUE-VISUAL-TAXONOMY.md) develops evidence-based criticism.
- [29 — UX Psychology/Ethics](29-UX-PSYCHOLOGY-LAWS-OF-UX-BOOK-AND-ETHICS.md) flags manipulation and mental models.
- [03 — Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md) addresses reliability/security underpinning all three.

**Standing decision:** design-style vocabulary remains reference-only; don't turn this framework into a mandate for fake pricing tiers, giant hero blocks, unnecessary animation, or entire enterprise CX departments in a tiny private app.

## Eleventh batch — missing content versus intentional whitespace

[77 — Portfolio Style and Empty-Space Guide](77-PORTFOLIO-STYLE-SCREENSHOTS-AND-WHITESPACE-RULES.md) distinguishes a meaningful **empty-data state** (must explain next action), accidental layout gaps (repair), and deliberate **negative space** (often leave untouched). This improves UI/UX quality without manufacturing cards, badges, product claims or over-explaining a visual metaphor.
