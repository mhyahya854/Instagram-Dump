# Reel Notes 15 — Hermes Agent Ecosystem, Skills, Memory and Control Center

_Captured 2026-10-25. Research reference only; **nothing installed**._

## Five things recommended by reel

| Item | What it means without a link | Canonical or credible source | Risk/limitations |
| --- | --- | --- | --- |
| **Hermes** | The agent runtime: tools, memory/session interface, skills, chat, external connectors and scheduling depending on configuration. | https://github.com/NousResearch/hermes-agent | Powerful runtime needs credential and tool-action boundaries. |
| **GBrain** | Optional persistent memory: facts with sources, corrections, retrieval/synthesis, access/sharing boundaries, optional automation and more complex backends. | https://github.com/garrytan/gbrain | Do not assume private-by-default for all server modes; read access boundaries, remote connections, storage and recurring costs. |
| **Skills Hub** | Hermes feature to browse/load agent skills on demand, rather than always loading every skill into context. Skills are often \`SKILL.md\` instruction bundles. | https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md | External registries contain untrusted instructions and scripts; review before installing. |
| **Agent Reach** | Connector/tool-routing layer for certain web platforms and media. | https://github.com/Panniantong/Agent-Reach | Supports vary by version and site. Auth cookies/browser sessions carry real security and ToS risks. |
| **Open Design** | AI design and production skill suite covering web/mobile designs, dashboards, decks and docs with reusable visual-system references. | https://github.com/nexu-io/open-design | The project's self-reported “31 skills, 129 systems” is version-dependent; need license and output testing. |
| **Hermes Studio** | Separate self-hosted dashboard for conversations, agent crews, usage/costs, terminal, schedules and monitoring. | Likely https://github.com/JPeetz/Hermes-Studio | “Hermes Studio” is ambiguous: https://github.com/rhinorhino/hermes-studio and other repos also use name. Never merge projects by name alone. |

**Note:** The reel calls these “five tools,” but the list comprises **GBrain, Skills Hub, Agent Reach, Open Design, Hermes Studio** *in addition to* Hermes itself.

### GBrain: what memory really involves

Capture facts with provenance (who said what and when), query relevant pages, attach corrections/expiry and control which user/agent can read it. A memory store is not the same as live access to private accounts. Before activation: decide local-only versus server, data retention/deletion, user separation, encryption, backup and whether anything transmits context to external inference providers. Verify fresh-session recall through actual queries rather than pretending remembered data was retrieved.

### Skills Hub: workflow

The runtime enumerates short descriptions; selects one relevant skill; loads the full instructions only when needed; tests applicability; executes tool calls with approval; and logs output. An installed skill is not a tested capability. Users should audit scripts, linked docs, shell commands and downstream downloads.

### Agent Reach: what “internet access” means

Agent Reach **orchestrates multiple platform-specific tools** rather than giving AI universal unrestrained access. Public reads differ from authenticated searches and private accounts. The October 23, 2026 v1.6.0 changed integration and install behavior; some channels (including Instagram) were experimental or not fully tested on release. Cookie/session storage is a sensitive trust boundary.

### Studio operations checklist

- Access control to browser UI/terminal/agent approvals and stored tokens.
- Scheduling visibility, stop/pause functions, job limits and cost alerts.
- Agent action logging and human approval for deployments, permission changes, purchases and data exports.
- Backup of local configuration and persistence and a tested restore.
- Cross-agent sharing and memory namespace boundaries; group chat is not automatic access isolation.

## Version/source notes

- GBrain upstream: https://github.com/garrytan/gbrain
- Optional community Hermes GBrain plugin: https://github.com/kerrz2020/hermes-gbrain ; not official and may install dependencies.
- Hermes hub documentation: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md
- Agent Reach release notes: https://github.com/Panniantong/Agent-Reach/releases
- Open Design candidate: https://github.com/nexu-io/open-design
- Hermes Studio candidate: https://github.com/JPeetz/Hermes-Studio
- **Claims not audited:** “instantly 10x,” exact feature counts, performance guarantees or self-reported safety.
