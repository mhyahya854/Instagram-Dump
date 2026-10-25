# 02 — Vibe-Coded App Quality Rules

> Applies to the completeness, authenticity, functionality, and release quality of AI-assisted or “vibe-coded” sites and apps. Visual patterns belong primarily in [Design & UX](01-DESIGN-UX.md); technical controls belong primarily in [Production & System Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).

## Authenticity: avoid vs. employ

| Avoid | Employ / verify |
| --- | --- |
| Fake reviews, testimonials, or awards | Use genuine, attributable claims and testimonials if presented. |
| Fake metrics or customer counters | Show only real, supportable statistics. |
| AI stock photos / AI-slop imagery passed off as authentic | Use appropriate genuine imagery; label synthetic imagery where relevant. |
| Text-only pretend demos and nonworking buttons | Real working demos and verified critical product actions. |
| Fake product interfaces and false form success | Show honest states linked to actual functionality. |
| Generic visual clichés standing in for product substance | Apply the Design & UX anti-patterns document. |

## Before launching a public site

| Avoid | Require / verify when applicable |
| --- | --- |
| Launch without a custom domain | Connect and verify the intended custom domain. |
| Launch without a favicon | Add and verify a working favicon. |
| Leave a “Made with AI” tag unintentionally | Remove the badge if permitted by the builder/platform terms and project policy. |
| No privacy policy | Publish an accurate, applicable privacy policy. |
| No terms and conditions | Publish appropriate terms and conditions. |
| Missing required cookie/privacy disclosures | Evaluate cookies/consent and actual data practices under applicable law. |
| No verification of the published site | Walk through deployed pages, mobile layout, and critical flows. |
| Misleading analytics and success indicators | Confirm real measurement and backend-backed success/failure states. |

## Product-functionality and measurement checklist

| Consider / add | Acceptance criterion |
| --- | --- |
| UTM tracking | Preserve useful campaign attribution with appropriate privacy handling. |
| Analytics installed and verified | Confirm actual events and privacy choices rather than assuming tags work. |
| Error tracking | Make failures observable without leaking personal or secret data. |
| Onboarding flow | When product complexity warrants onboarding; minimize friction. |
| Form success/error states | Only display success after confirmed completion; show actionable errors. |
| Actual product demos | Demonstrate real product capability rather than decorative placeholders. |
| Mobile layout and cross-browser behavior | Functional experience on applicable devices. |
| Custom 404 and recovery paths | Keep users from reaching dead ends. |
| Privacy / terms / cookie controls | Provide accurate explanations and necessary choices. |

## Vibe-coded app failure areas to inspect

- Client-only validation presented as adequate security (server-side validation must be handled in engineering).
- Demo buttons, signup, login, search, forms, and payments that look functional but fail in the deployed app.
- Authentication/authorization mistakes, exposed secrets, unsafe dependencies, CORS misconfiguration, and missing abuse controls; see [production security](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).
- Missing loading, empty, success, failure, and confirmation feedback (designed under UX rules, validated as product functionality here).
- Production mismatch: a locally working screen that fails because of domain settings, missing environment variables, database connectivity, or build differences; see [production checks](03-PRODUCTION-SYSTEM-ARCHITECTURE.md).

## Interpretation

- **Not every website needs** accounts, payments, site search, analytics, banners, a contact bubble, or onboarding.
- **No fake proof**: do not create reviews, customer counts, claims, or results without real evidence.
- **Don't launch a facade**: prioritize real working application behavior over decorative UI.
- **Keep this file distinct** from security/system architecture and visual style guidance.

## Additional product-completeness lessons (October 25 reels)

See [12 — Product Marketing, Pricing & Homepages](12-PRODUCT-MARKETING-PRICING-HOMEPAGES.md): clearly communicate product and target audience, offer a real first-use result, keep onboarding proportionate, and prefer genuine evidence and usable CTAs over fake social proof or decorative splash screens. These are **considerations**, not a demand to hide important pricing/features or automate spam submissions.

See [11 — Data Pipeline Quality](11-DATA-PIPELINE-QUALITY.md): a successful background job does not imply valid data; enforce checks before publishing dashboards. See [14 — Agent Project Handoff](14-AGENT-PROJECT-HANDOFF-AND-WORKFLOWS.md) for goals, boundaries and acceptance tests.

## Second reel batch: product-completeness check

[22 — UX Motion, Touch and Trust](22-UX-MOTION-TYPOGRAPHY-TOUCH-AND-TRUST.md) extends the checks to mobile overflow, accessible controls, links, titles/metadata, functioning forms and authentic loading/progress. [20 — Security Hardening](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md) adds server/API safety. Do not mistake a beautiful screen or an AI security prompt for a verified product.

## Third reel batch: product completion, automation and media

[28 — Workflow Templates and Page Completeness](28-AUTOMATION-TEMPLATES-AGENT-REVIEWS-AND-SAFETY.md) describes n8n templates, why third-party JSON needs review, missing 404/blog/other scoped pages and actual checks before marking delivery “complete.” [25 — Programmatic Media](25-STICKMAN-PROGRAMMATIC-VIDEO-WORKFLOWS.md) covers honest production proof rather than one-prompt promises. [26 — Local/OSS Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md) distinguishes open application code from commercial model or hosted costs.

## Fourth reel batch: UX/CX end-to-end quality

[33 — UI, UX & CX](33-UI-UX-CX-SCOPE-AND-QUALITY-FRAMEWORK.md) connects working product tasks to marketing promises, purchasing/support, and service reliability. Check meaningful user success across interfaces and customer touchpoints, not only “looks good.”
