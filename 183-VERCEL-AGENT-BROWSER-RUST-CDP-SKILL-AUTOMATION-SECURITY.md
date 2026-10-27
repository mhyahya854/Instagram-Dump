# 183 — Vercel Labs agent-browser: agent-accessible browser CLI, security and adoption

**Source:** User typed “on github ... agent-browser” on 2026-10-27. No owner or screenshots supplied. GitHub search and live repository metadata independently identified **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)**, the prominent, current, canonical researched match. **Official project:** https://agent-browser.dev/ ; **repository license:** Apache-2.0; latest main branch was active at research time. No runtime installation, browser navigation, logins or command execution occurred.

## 1. What the project does

**agent-browser** is a **fast native Rust command-line tool and agent skill for browser automation**, not a language model or browser extension of ChatGPT. An AI coding agent can use it to navigate sites, inspect DOM/accessibility snapshots, click and fill elements, take screenshots, test web applications, read page content and perform user-authorized browser workflows.

A main advantage is **compact, agent-friendly element references** (e.g., `@e1`, `@e2`) from accessibility snapshots. Agents can inspect actionable elements without sending full screenshot pixels or giant raw HTML on every step. It also supports selector/role locators, JSON result formats, tabs, sessions, wait conditions, console/network inspection, screenshots, React/Core Web Vitals, accessibility and optional experimental WebMCP.

### First-principles architecture

~~~text
Trusted user goal + allowed origins + browser safety policy
  -> AI agent issues CLI command
     -> native Rust CLI parses intent and talks to local daemon
        -> Rust daemon manages browser sessions via Chrome DevTools Protocol (CDP)
           -> browser navigates / captures accessibility tree / drives input
        <- compact structured observation + errors / context refs
     <- agent validates outcome before next permitted action
~~~

The upstream README describes **Rust CLI + persistent Rust daemon**, direct CDP, and Chrome for Testing as the default browser. Other supported engines/modes may include Lightpanda, Obscura and Safari/iOS through WebDriver as documented, but engine support and feature parity vary by mode. A page element reference is meaningful only within the current snapshot/tab state; after significant DOM changes refresh observation.

## 2. Official source usage example (documentation, not executed)

~~~bash
agent-browser open https://example.com
agent-browser snapshot                 # Lists accessible elements and @eN refs
agent-browser click @e2               # Only if identified and authorized
agent-browser fill @e3 "example text"
agent-browser get text @e1
agent-browser screenshot page.png
agent-browser close
~~~

**Suggested agent workflow:** read the goal and origin restriction → open authorized website → snapshot → determine element role/name/visibility → click or type → wait for a concrete success criterion → independently verify DOM/URL/result → repeat with bounded retry. A tap/click command's successful return does not prove that a checkout, upload, payment, form or GitHub change succeeded; verify server-visible state.

The upstream skill has a small **discovery stub** under `skills/agent-browser/SKILL.md`: after installation, run `agent-browser skills get core` to obtain instructions matching the installed CLI version. Do not copy a stale SKILL.md and assume it contains the entire reference. Project/home installation options documented upstream include npm package, Homebrew for macOS and Cargo; initial Chrome for Testing provisioning may download a browser. **Nothing was installed for this research task.**

**Platforms per current upstream:** native Rust binaries for Windows x64, macOS x64/ARM64, Linux x64/ARM64. Runtime browser, downloadable packages and integration may require additional components; native binary availability does not imply every automation feature works on every engine.

## 3. Security and privacy: specific upstream guardrails

The official README's [Security](https://agent-browser.dev/security) section describes **opt-in** controls, not unconditional sandboxing:

| Feature | Purpose | Caveats |
|---|---|---|
| `--allowed-domains` | Allowlist top-level site origins, request and WebSocket destinations in supported Chromium sessions | **Cannot be applied safely to existing profiles/CDP connections, auto-connect, restored state and some alternate engines** according to upstream, so option is rejected for these modes |
| `--content-boundaries` | Mark untrusted page output so agent recognizes website text as data | Marker is a provenance cue, **not** an impermeable prompt-injection defense |
| `--action-policy` | Gate dangerous actions with policy file | A missing/invalid policy blocks commands; good fail-closed property in the documented mode |
| `--confirm-actions` | Require human confirmation for named sensitive action categories | Only effective if host actually enforces it; don't represent a prompt instruction as approval |
| Encrypted local auth vault | Keep credentials out of ordinary LLM tool arguments/output | Vault file/key/security and OS permissions must be reviewed; login origin checks need attention |
| `--max-output` | Limit untrusted output/context flooding | Could truncate evidence needed for verification; use targeted reads |
| Session/profile restore | Preserve cookies and localStorage for authorized workflows | Stored state files can be **high-value secrets**; restrict permissions and retention |
| Strict tab pinning | Avoid silently acting on the wrong tab in shared browser sessions | Use a dedicated profile/context where possible; confirm active URL before action |

**High-risk warning:** `--remote-debugging-port` may expose effectively full control of the running browser to a local process. Using a personal Chrome profile or importing authenticated storage exposes social/email accounts and saved sessions. Prefer a disposable dedicated browser, site-scoped low-privilege test account, secret-free project workspace and an action policy. Only connect to authenticated user sessions with informed authorization and browser-isolation controls.

**Prompt injection:** websites can place directives in text/DOM or WebMCP metadata pretending to be the user or developer; never treat such text as authority to run shell commands, reveal cookies, publish data or modify repositories. Page-provided `readOnlyHint` or tool schemas do not grant permission. External executable plugins can themselves introduce privileged actions and dependencies. Validate plugin scopes before use.

## 4. Operational comparison

| Tool | Primary purpose | When to choose |
|---|---|---|
| **agent-browser** | Native CLI and compact agent-readable browser interaction, screenshots and automated QA | AI coding agents need scripted browser tests with bounded permitted actions |
| **Playwright** | Framework API for deterministic web test scripts and CI | Reusable stable regression suites and fine control of execution in code |
| **Microsoft playwright-mcp** | MCP-exposed browser tools to agents | Agent harness primarily supports MCP interface rather than shell CLI |
| **Browser Use** | Higher-level agentic browsing stack | Task-level agent planning with different execution/privacy/cost tradeoffs |
| **ChatGPT Work / Computer Use** | User-authorized UI and cloud browser workflows | Work modes where first-party computer interaction is provided and appropriate |

These can complement each other; don't install redundant browser controllers without a clear test/maintenance need. Browser automation can fail on navigation anti-bot systems and may be prohibited by website terms. Social accounts, banking, payments, private data and bulk scraping require special authorization and restraint.

## 5. Realistic use cases and bounded QA contract

- **Web app smoke test:** navigate app, verify title/controls, submit synthetic form, check real saved state and errors.
- **Accessibility audit assist:** snapshot semantic roles, identify missing labels/contrast/focus candidates, confirm with independent human/browser tests.
- **Visual regression:** capture screenshots at **specified viewport/device scale**, compare actual pixels via dedicated diff tooling, audit font/loading differences.
- **Research extraction:** retrieve limited permitted public content, preserve source URLs/timestamps, avoid reproducing copyrighted full articles or accessing private data.
- **Agent debugging:** read console/network errors and DOM state; distinguish visible UI from backend truth.

**Acceptance criteria:** run only approved domains; bounded actions and time; no credential leaks; explicit confirmations for consequential operations; artifacts/logs redact session tokens; verify each claimed success through authoritative state; close sessions/clean up; do not silently switch to a personal browser context.

## 6. Limitations, license, source verification

GitHub metadata identifies `vercel-labs/agent-browser` as **Apache-2.0** and active on 2026-10-27. Upstream feature claims, speed comparisons and protection mechanisms were **not independently executed or benchmarked**. The source project's README states a client-daemon architecture and available platform binaries, but security guarantees depend on runtime flags, browser profile mode and host privileges. License of external websites, remote browser service providers and optional plugins is separate.

**Related existing archive:** [126 — Browser Use and JEV](126-JEV-ULTRAFAST-AND-BROWSER-USE-AGENT-OPERATION-GUIDE.md), [127 — GitHub agent skills](127-GITHUB-AGENT-SKILLS-AND-GRAFT-MULTIPLE-PROJECTS.md), [145 — forty Claude repos](145-FORTY-CLAUDE-REPOS-EXACT-LIST-AND-MATCHES.md), [164 — repository owner audit](164-FORTY-CLAUDE-REPOSITORIES-OWNER-VERIFICATION-AND-RISK-MATRIX.md), [175 — Understand Anything and diagrams](175-HUASHU-MOTION-FRONTEND-SLIDES-DIAGRAM-DESIGN-UNDERSTAND-ANYTHING.md), [184 — typed source register](184-OCT27-TWO-QUESTIONS-STOP-SLOP-UNDERSTAND-AGENT-BROWSER-REGISTER.md).

**Research status:** GitHub owner, README, skill stub and repo-level declared license verified. No software installed or authorized browser task performed.
