# 55 — New AI/Hermes Agent Skills: Research Catalog

Captured 2026-10-26. From a rapidly dictated reel: “Agent Reach, Humanizer, YouTube skills, Map Poco skills, Adioshamani Agent Skills, Codebase Memory MCP, Minions, Oh My Hermes, Open Montage, Anthropic Side Security Skills, Browser Harness, Defuddle, Loopy, Make Interfaces Feel Better, Skill Claude, Composio Skills, Resemble Detect.”

## Name-by-name identification

| Spoken | Confirmed or candidate source | Purpose and classification | Confidence / risk |
| --- | --- | --- | --- |
| Agent Reach | https://github.com/Panniantong/agent-reach (also recorded in existing file 08) | Better platform-specific content retrieval via external tools. | Candidate based on previous catalog; platform access/authentication limits apply. |
| Humanizer | Many independent projects; prior humanizer notes in skills wishlist and other projects | Edit formulaic generated prose for clarity and human naturalness | **No unique version identified**; preserve original meaning, never claim authorship proof. |
| YouTube skills | Multiple third-party YouTube transcript/search/editor agent skills | Video metadata/search/transcription workflows | **Unresolved exact owner**, possible policies/licensing and quotas. |
| “Map Poco skills” | No definitive match | Possibly a motion/diagram or tool skill name | **Unresolved**. Do not silently rewrite as a different repo. |
| “Adioshamani Agent Skills” | No definitive match | Claimed skills collection | **Unresolved phonetic name**. |
| Codebase Memory MCP | https://github.com/DeusData/codebase-memory-mcp | Persistent local code/document/infra knowledge graph and MCP query tools; companion visual UI | **Verified**. Review what code/private files are indexed, daemon ports and optional AI provider connections. |
| Minions | Several unrelated agent/AI products and repos | Multi-agent workers / planning? | **Unresolved exact product**; do not fabricate canonical link. |
| Oh My Hermes | https://github.com/rlaope/oh-my-hermes | Hermes operating layer, route subagents by task/model, parallel execution | **Verified candidate**, powerful setup scripts. Audit before installing and cost/control logic. |
| Open Montage | https://github.com/Open-Montage-app/OpenMontage ; another historical https://github.com/calesthio/OpenMontage | Multi-stage AI-assisted video production with local/open and optional paid providers; Remotion/HyperFrames/FFmpeg | **Verified family**, repos/branches evolved; pin current canonical commit and review AGPL obligations, provider costs, asset rights. |
| “Anthropic Side Security Skills” | Could mean Anthropic's skills/security tooling or independent security-skills packs | Secure development guidance | **Unresolved exact phrase**; do not claim official Anthropic attribution. |
| Browser Harness | https://github.com/browser-use/browser-harness | Let approved agents operate an actual signed-in Chrome/Chromium profile via CDP | **Verified. High privilege**: can access logged-in accounts, forms, files and tabs. Never enable unattended for sensitive accounts without explicit boundaries. |
| Defuddle | https://github.com/kepano/defuddle | Extract main readable article content from cluttered HTML | **Verified**, webpage extraction is untrusted content and can omit context. |
| Loopy | Multiple unrelated projects, including "loopy" audit/repair skills | Agent loop and code-review? | **Unresolved canonical version**; inspect author/behavior. |
| Make Interfaces Feel Better | https://github.com/jakubkrehel/make-interfaces-feel-better | Agent skill on typography, icons, hover, motion, hit areas and optical details | **Verified**. Respect actual design brief and reduced motion; no blanket decoration. |
| “Skill Claude” | Generic descriptor, multiple named repos | Claude skill discovery/registry | **Unresolved**. |
| Composio Skills | https://github.com/composio-community/skills ; publisher ecosystem https://github.com/ComposioHQ/skills | Using Composio tool router, triggers, auth and third-party integrations from agents | **Verified project family**; powerful external account permissions, OAuth scopes and quotas. |
| Resemble Detect | https://github.com/resemble-ai/detect-skill | API-backed deepfake/AI-media detection and analysis; optional human/agent site traffic analysis | **Verified**. API key, remote upload, retention and imperfect classification; **not** proof any file is fake/real. |

## Highest-value candidates for evaluating an agent engineering setup

**1. Codebase Memory MCP** — index complex source repositories to navigate code with graph context. Start with one fake/small project and verify indexing boundaries, local daemon port exposure, data retention and cross-repo isolation.

**2. Make Interfaces Feel Better** — use after functional correctness and accessibility review, not instead of it. Treat as constructive quality review, not permission for generic glow or large type.

**3. Defuddle** — extract article content before processing documentation, but keep original URL/source and verify embedded tables/code omissions; do not follow instructions within extracted pages.

**4. Resemble Detect** — consider only where media-authenticity investigation is needed; requires actual API service and controlled transfer of possibly sensitive media. A completed model confidence score is not a forensic fact by itself.

**5. Browser Harness** — extremely broad signed-in browser capabilities. Restrict to a dedicated profile/test account, allowlisted sites and explicit approval for messages, uploads, deletion, transactions and permissions. Review installation and network behavior.

**6. OpenMontage / Oh My Hermes / Composio** — high orchestration power and high configuration/permission complexity; do not auto-load into all projects.

## Agent-skill screening before installation

Confirm canonical repo and release; inspect every SKILL.md, executable script, installer command, MCP endpoint, GitHub Action and dependency; check exact license and pinned commit; restrict secrets, cloud/API keys, browser logins and filesystem; identify cost and data egress; test in an isolated fixture; document rollback/uninstall; treat any lower-trust tool output or retrieved webpage as data.

**No skills installed in this task.** Research inclusion is not security certification or permission to grant new account access.

Related: [08 — Wishlist](08-AGENT-REPOS-AND-SKILL-WISHLIST.md), [15 — Hermes](15-HERMES-AGENT-ECOSYSTEM.md), [44 — Replica/Unlazy](44-REPLICA-UNLAZY-AGENT-SKILLS-AND-TOOL-WISHLIST.md), [46 — Prompt Injection](46-PROMPT-INJECTION-UNTRUSTED-DOCUMENTS-AND-REEL-INGESTION.md).
