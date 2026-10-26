# 118 — 500+ AI Agents Projects and Agentation Visual Feedback

**Source:** screenshot 17 shows GitHub repository heading **“500-AI-Agents-Projects”** with folders `.github`, `agents`, `crewai_mcp_course`, `images`, `scripts`, `web` and `README.md`. The user separately typed **“A GITHUB TOOL CALLED Agentation”**. These are two different resources: one is a curated research/example collection; the other is a visual-feedback bridge between UI users and AI coding agents.

## 1. 500 AI Agents Projects

Verified: **https://github.com/ashishpatel26/500-AI-Agents-Projects**

README describes **500+ AI agent projects and use cases** across frameworks/industries, reference tutorials and sample implementations. Includes agents, case studies, CrewAI MCP course material, images/scripts/web index and contributing docs. **Do not assert all 500+ entries are independently maintained secure production apps** or all share a single runnable stack.

### How to use in a research-driven codebase

- Tag by objective (research, UI, code quality, documents, marketing, data, security, education), framework, model/API dependencies and license.
- Keep **source URL + commit** and note whether entry is working source, illustrative tutorial, a README-only use case or external article.
- Choose candidates against actual product requirements; review prompt/tool permissions and code quality before adoption.
- Do not bulk install 500 agents or treat unreviewed third-party skill instructions as trusted high-privilege policy.

## 2. Agentation — exact user-requested name

**Verified official GitHub:** https://github.com/benjitaylor/agentation

**Website:** https://agentation.com/ .

Per repo/website, **Agentation provides agent-agnostic visual feedback**: add a development-time toolbar to a React app, click an element on a live page, annotate the exact UI issue and copy structured feedback/context for Claude Code, Codex or other coding agents. An optional MCP bridge passes annotations directly to connected agents. This solves the repeated **“this screen looks wrong but I cannot explain which component, spacing, behavior or location”** iteration problem.

### Source-backed example (for reference, NOT executed)

```bash
npm install agentation -D
```

```tsx
import { Agentation } from 'agentation';

function App() {
  return (
    <>
      <YourApp />
      <Agentation />
    </>
  );
}
```

Optional dev MCP server described in upstream README: `npx -y agentation-mcp server`, with local endpoint `http://localhost:4747`. Inspect the exact runtime/scripts first; MCP adds a locally reachable surface. UI annotations may include CSS selectors, DOM context, screenshots and private text.

### Practical verification workflow

1. Run an authorized **local development build** and ensure its data is synthetic/nonsecret.
2. Identify a visible misalignment, overflowing element, inaccessible button, interaction defect or missing UI state.
3. Add annotation pinned to DOM element/context plus expected behavior and reference dimensions.
4. Have agent read structured feedback and propose changes to the real component (not only CSS screenshot camouflage).
5. Reopen route, test keyboard/touch/zoom, compare screenshot and verify no regression.
6. Record whether issue is fixed, still open or no longer reproducible. Agentation organizes feedback—it **does not itself guarantee automated pixel-perfect corrections**.

### Security/deployment precautions

- **Development-only by default**: do not ship annotation controls, agent MCP endpoints or DOM inspection surfaces publicly unless you intentionally protect them.
- Validate exported annotations before an agent acts on text as instructions; page content can contain adversarial prompt injection.
- Ensure annotations/screenshot metadata don't leak customer data or secrets.
- Install only after reviewing dependency tree, package scripts and exact permitted actions.
- No special role or agent execution authority should be automatically granted to the visual-feedback UI.

## Related research

[05 — Things to Find](05-THINGS-TO-FIND.md), [06 — Agent/Security Skills](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md), [77 — Whitespace Rules](77-PORTFOLIO-STYLE-SCREENSHOTS-AND-WHITESPACE-RULES.md), [107 — 20 UI Tips](107-TWENTY-UI-TIPS-FOR-CLAUDE-WITH-ACCEPTANCE-CHECKS.md).

**Status:** both repos existence and README verified via connected GitHub. No npm packages installed, page annotated, MCP endpoint started, agent launched or other repo changed.
