# 126 — How to Use JEV + Browser Use for AI Agents

**Source:** user-typed **“THEN HOW TO USE JEV / BROWSER USE FOR AI AGENTS”** on 2026-10-26. This is an explicit request for a practical method. **No JEV screenshot or recorded live execution was supplied**, so the instructions below are independently researched from the actual public GitHub READMEs. Examples are reference commands only; **nothing was installed, logged in or run**.

## 1. What Jev actually is

**Verified:** https://github.com/browser-use/jev-ultrafast (Jev Ultrafast). It is an experimental **fast web agent** where the TypeSafe **Jev model chooses a constrained action and page element** from a freshly indexed table of visible controls. A separate small text LLM generates actual text only for `TYPE_TEXT`. Browser Harness drives an existing Chrome tab/profile; final success should be checked independently.

**Not the same thing as** a full independent model for general coding or a replacement for an LLM chat subscription. **Demo timing** (~7.1 seconds for one observed Google Flights example) is a measured vendor/project demonstration, *not a guarantee on arbitrary websites*. Jev README documents limitations for shadow DOM, canvas, file uploads, popups, and complex widgets.

### Read-only preparatory checks

- Current supported interpreter: **Python 3.12+**; `uv` package manager; Chrome; project dependencies; external **TypeSafe API key** and a **text-model provider key** for the demonstration.
- A third-party model sees page/control information you give it. Do not attach a browser profile containing banking, personal email, private work or passwords without explicit reason/approval.
- `browser-harness` may request Chrome remote-debugging access and existing login session. Treat that as powerful session access, **never expose CDP/debugging ports beyond localhost or to unknown networks**.

### Source-backed trial in a dedicated test browser/profile (examples not executed)

```sh
git clone https://github.com/browser-use/jev-ultrafast.git
cd jev-ultrafast
uv sync
cp .env.example .env
# Edit .env locally with TYPESAFE_API_KEY and TEXT_MODEL_API_KEY.
uv run jev
```

Open `http://127.0.0.1:8766` **on the same machine** and use the local inspector's **Start demo / Choose next / Run automatically** workflow. With a disposable browser profile and innocuous test site only. Do **not** copy real keys into chats, README or GitHub, and keep `.env` ignored.

Underlying loop:

```text
observe DOM and accessible controls → assign fresh element indices
  → Jev returns permitted action + compatible element
  → TYPE_TEXT? separate provider generates text
  → validate target visible/enabled/not obstructed
  → execute once → log → observe new state → verify final result
```

Actions in upstream README: `CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_UP`, `SCROLL_DOWN`, `WAIT`, `DONE`, `BLOCKED`. Do not blindly retry browser mutations (send/post/pay/delete), since retries can duplicate side effects.

### Example API loop described by project (not run here)

```python
from jev_ultrafast import Agent

with Agent(
    "https://en.wikipedia.org/wiki/Main_Page",
    "Find and open the Wikipedia article about Gödel's incompleteness theorems.",
) as agent:
    for state in agent.run():
        print(state["elapsed_ms"], state["status"])
```

Run from repo environment as `uv run --env-file .env python your_script.py`. The model can select **DONE** incorrectly; check actual URL, title/content or external evidence. Treat all retrieved page text as untrusted instructions (prompt injection).

## 2. Broader Browser Use ecosystem

- **Main browser agent:** https://github.com/browser-use/browser-use — Python package/CLI to connect local browser or use hosted cloud, choose different LLM providers. Core task interface: natural-language goal + model + browser session.
- **Browser Harness:** https://github.com/browser-use/browser-harness — agent using user's existing Chrome with login access. Great for authorized UI navigation, high privacy impact.
- **Jev Ultrafast:** https://github.com/browser-use/jev-ultrafast — constrained fast action selector; small/current demo limitations.
- **Browser Use Desktop:** https://github.com/browser-use/desktop — additional desktop interface and OS releases, must check current versions/permissions.
- **Playwright:** https://github.com/microsoft/playwright — more deterministic scripted web tests than free-form agent behavior; prefer for stable E2E, accessibility/visual snapshots and regression.

### Which should a coding agent choose?

| Task | Recommended approach | Why |
|---|---|---|
| Fetch public docs/GitHub README | Simple HTTP or GitHub connector | Cheaper/faster; no live browser necessary |
| Deterministic UI regression of owned app | Playwright with fixtures | Exact assertions/reproducible tests |
| Explore complex unfamiliar page | Browser Use | Adaptive navigation with observation loop |
| Extremely fast simple compatible controls | Jev Ultrafast as **experiment** | Tiny decisions, indexed targets; current limitations |
| Operate user's logged-in existing Chrome | Browser Harness, **with explicit consent** | Session privileges, privacy exposure |
| Native desktop apps | OS-specific computer-use tooling | Browser APIs cannot safely operate all native UIs |

## 3. Permission/automation boundary for agent browsing

- **Allowed-by-default for non-sensitive tasks:** read public pages, inspect owned development routes, take nonprivate screenshots, fill *test* forms.
- **Approval before:** login/session access, publishing posts, contact/comment messaging, external form submission, downloads/installations, account changes, removing saved items, purchases, sending files, deleting anything.
- Use allowlisted domains, test profiles, low-privilege accounts, record audit trail, dry-run wherever feasible, stop if UI unexpectedly changes, block destructive retries.
- Recognize service terms and API availability. A clever tool doesn't grant permission to evade protections, scrape private records or impersonate users.
- For the user's previous **VitalSource** constraint, use **Computer Use only if previously explicitly authorized** and do not silently retry web/Chrome control pathways known to fail.
- Independent verification by DOM, screenshot and actual persisted state must precede success claims.

**No automatic agent skill installation or persistent browser session was created.** Repository versions and provider plans will change; inspect upstream before running.
