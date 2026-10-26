# 127 — GitHub Skills for AI Agents + Graft: Disambiguation and Tool Governance

**Source:** explicit typed leads **“GITHUB SKILLS FOR AI AGENTS / GRAFT”** from the fifteenth Instagram batch. No screenshot contains a Graft logo or specific URL. Therefore the following are **researched possibilities, not an assertive resolution** of which Graft the user saw.

## 1. What an AI agent skill is

An **agent skill** is usually a directory with `SKILL.md` plus optional referenced instructions/scripts/templates. It tells an LLM **when** to use a workflow, how to inspect required inputs, and how to produce/verify results. It is **not equivalent to an installed software package** or a sandboxed guarantee. Skills may invoke shell scripts or request powerful tool permissions. Source/ownership and scope matter more than popularity.

### Verified directories and projects for discovery

| Reference | GitHub | Reason to examine |
|---|---|---|
| Agent Skills open format | https://github.com/agentskills/agentskills | Standard/community specification and examples |
| Anthropic skills | https://github.com/anthropics/skills | Working examples and project skill structures |
| Vercel agent skills | https://github.com/vercel-labs/agent-skills | UI/web engineering guidance and examples |
| Addy Osmani skills | https://github.com/addyosmani/agent-skills | Frontend engineering, perf/design practices |
| Matt Pocock skills | https://github.com/mattpocock/skills | Planning/typescript and workflow ideas |
| Trail of Bits skills | https://github.com/trailofbits/skills | Security research/review practices; still inspect before running |
| superpowers | https://github.com/obra/superpowers | Planning, execution and systematic verification |
| Existing archive | [06 — 68 Repositories](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md) | Verified prior set grouped by AI-generated code failure category |
| This batch | [124 — GSD/Ralph](124-COST-CONSCIOUS-STACK-GSD-ROO-RALPH-CODERABBIT-LINKEDIN.md) | Planning/review loops, not mandatory installs |

### Selecting/installing responsibly

1. Decide actual task and platform (Claude Code, Codex, Cursor, project-local and Windows/macOS/Linux constraints).
2. Identify official owner and commit SHA, inspect `SKILL.md`, README, nested scripts, lockfiles, network calls and license.
3. Score supply-chain/agent privilege risks; never auto-run curl|sh, privileged terminal commands or remote scripts from a reel.
4. Prefer **project-local**, explicitly scoped skill over global installations, with permission boundaries.
5. Run dry-run/unit-test in disposable repo with fake secrets, verify output and record incompatible versions.
6. Keep a manifest of chosen skills **and rejected alternatives**, with rationale and rollback. Catalog “approved to research” ≠ “approved to execute.”
7. Use user-goal/acceptance contract and avoid infinite self-improving loops or unverified automatic production updates.

## 2. “Graft” is ambiguous: three independently identified technologies

### Candidate A — Graft for agent operations over legacy systems

- https://github.com/graft-org/graft
- Public README markets **“Make the software that runs your business usable by AI agents”**.
- Proposed workflow: observe legacy UI → map workflow/capabilities → compile stable tool contract → enforce policy and verify results → react to UI drift.
- README describes **private beta/waitlist**. A public repo may describe vision/interface without granting access to a ready-to-run product. Do not infer complete availability.
- Use when legacy ERP/desktop/enterprise UIs have no API and require guarded, verified agent workflows.

### Candidate B — Graft self-extending tools over MCP

- https://docs.getgraft.ai/graft/get-started/what-is-graft
- The official site describes a **dynamic MCP tool creation system**: agent requests something missing, Graft writes a narrowly scoped tool, tests the tool and makes it callable; states credentials are isolated from model/tool-generated code.
- This has a **larger threat model** than a static skill: code generation, real-service testing and tool permissions. Before using, demand exact safeguards for sandboxing, auth, allowed network targets, mutation prevention, tool review/signature, audit and time-to-live.
- The screenshot/typed word alone does **not** establish this candidate as intended.

### Candidate C — Graft codebase-memory skill

- https://github.com/AEndrix03/Graft
- Public documentation describes knowledge notes linked to source files and lifecycle operations (bootstrap project, recall relevant context, supersede contradicted facts, save evidence-backed conclusions). Different scope than operating ERP tools or generating MCP capabilities.
- A useful model for long-lived coding agents where stale notes/decisions need revision; must treat inferred memories as fallible and never grant retrieved text top-level instruction authority.

### Additional name collision

- https://graft.page/docs/agent-surface documents a Graft content/CMS agent interface, distinct from the three above.
- All are possible research matches. **Original user merely says “GRAFT.”** Preserve unresolved until an actual URL or source image identifies one.

## 3. Proposed offline-resilient skills manifest (not installed)

```yaml
name: example-skill
source_repo: https://github.com/owner/repo
commit: <pin commit>
purpose: "what concrete error or workflow this fixes"
scope: project-local
platforms: [codex, claude-code]
requires: [read-only filesystem, test browser]
forbidden: [production deletes, payments, secrets export, unattended publishing]
tests: ["test fixture: expected behavior", "negative case"]
license: "checked at pinned revision"
state: research-only
```

For a future internet-outage scenario, **URL lists alone are not offline capability**. Include rights-cleared source snapshots, lockfiles/runtime binaries, test fixtures, platform-specific dependencies and full local documentation **only where permitted**. But this archive stage intentionally saves textual research separately; source mirroring or skill installation requires separate authorization and license review.

**Status:** candidates researched, terms disambiguated, no downloads, installs, AI-generated tools, API calls, live account modifications or Universal-Rules writes performed.
