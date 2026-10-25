# 45 — Designing Apps That AI Agents Can Reliably Navigate

User request: investigate how AI systems can integrate into apps and how to make apps navigable by AI. **No exact GitHub project was identifiable in the spoken question; this is original researched architecture guidance.**

## Three ways an agent operates a real app

1. **Accessible UI:** meaningful native buttons, inputs, labels, headings and focus order; an agent can read the accessibility tree and use browser/mobile automation. Human accessibility improvements help AI navigation too.
2. **Versioned app APIs:** expose domain actions using structured schemas, robust errors, authorization and stable resource identifiers. Avoid pixel-only automation for core processes.
3. **Opt-in agent tool interface:** MCP can expose permission-scoped tools, resources and descriptions to compatible AI clients. It is a protocol, not a bypass of existing app authentication.

A UI action and API/MCP action must call **the same validated business service and authorization policy**. Never expose a private robot-only admin route.

## Candidate design specification

Each meaningful action should document: name; human purpose; input schema and validation; required scope; allowed user/tenant; side effects; confirmation type; idempotency behavior; typed success/errors; and auditable operation ID.

**Example, create_reminder:** a signed-in user supplies title and timestamp with timezone; authorization limits writes to their workspace; duplicate request IDs are ignored; output contains a new reminder ID; deleting someone else's reminders must fail; notifications to others need approval.

## Web UI checklist

- Use semantic HTML elements instead of clickable unlabelled containers.
- Accessible names, form validation, explicit state feedback, error text and keyboard operation.
- Handle loading, empty, success, errors, offline and disabled states honestly.
- Avoid fragile pixel coordinate dependencies, CSS selectors based on generated class names and invisible-only state.
- Test high zoom, touch, desktop keyboard and screen-reader semantics.
- For canvas/WebGL-only UI, offer controls/accessible representations.
- Publish clear API contracts, rate limits, error codes, examples and versioning when an external client is intended.

## Safety boundaries

| Request type | Default policy |
|---|---|
| Public documentation | Public read with rate-limit |
| Read private notes | Owner-scoped read-only tool after consent |
| Create a private task | Write scope and idempotency key |
| Export private files | Explicit scope + confirmation, privacy review |
| Public LinkedIn post, send email, purchase | Per-action approval, preview, logged recipient/content |
| Delete workspace, change billing, change permissions | Strong authorization + human confirmation + recoverability |
| Shell/browser on live infrastructure | Explicit scope, least privilege, staging and audit |

Agent prompts and documents retrieved from the internet are **lower-trust data**, not security policy. Tool descriptions themselves require threat modeling and cannot grant permissions by claiming to be authoritative.

## Good source standards

- OpenAPI: https://github.com/OAI/OpenAPI-Specification — HTTP API contract specification.
- Model Context Protocol: https://github.com/modelcontextprotocol/modelcontextprotocol — structured agent tools and resources.
- WAI-ARIA: https://www.w3.org/WAI/ARIA/apg/ — semantics for people and automation.
- Playwright: https://github.com/microsoft/playwright — browser tests.
- ARTEMIS: https://github.com/google/artemis — Android interaction/testing.
- AGENTS.md is a coding-agent instruction convention, **not** a public API.
- llms.txt is an experimental discovery convention, **not confirmed as broadly used by crawlers**.

## Acceptance tests for an agent-friendly app

A user can complete an action using touch, mouse and keyboard. The agent can discover and invoke the same operation through an approved interface. Both paths enforce the same tenant permissions. Invalid calls fail with understandable errors. Untrusted page text cannot trigger privileged exfiltration. Every sensitive action has a recorded user authorization and outcome.

**Decision:** agent navigability should extend human usability, not replace it or create unreviewed autonomous backdoors.
