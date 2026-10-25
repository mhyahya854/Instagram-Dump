# 46 — Prompt-Injection Detector Research and Safe Reel-to-Knowledge Pipeline

Captured 2026-10-25. Source describes a “Trojan horse detector” checking uploaded documents using three agents: one finds invisible text, another finds instructions addressed to Claude, and a third highlights suspect lines red. **Exact GitHub source not present; efficacy is unverified.** No detector prevents every injection.

## What a document prompt injection is

Text in a PDF, HTML page, README, skill file, form input or social caption may falsely order the assistant to ignore instructions, reveal secrets, invoke tools or post data externally. The **retrieved document is untrusted data**, not a system/developer/user authority. Visible and extracted text can differ because of hidden layers, style, zero-width characters, overlays or links.

## Defense-in-depth workflow

1. Receive and classify a document without executing embedded commands.
2. Inspect visible rendering, underlying text and links where possible, noting source lines/pages.
3. Flag authority spoofing, credential requests, tool instructions, hidden/encoded text, exfiltration destinations and requests to bypass approvals.
4. Review suspicious spans in context; a security training document can innocently quote malicious strings.
5. Separate extraction from tool execution. Never allow source material to self-upgrade permissions.
6. Test against adversarial local fixtures. Include false positives and false negatives.
7. Report inspected / suspicious / inconclusive / not inspected, never “100% protected.”

**Three independent agent judges are not a guarantee:** identical model biases, missing hidden content and hallucinations can invalidate consensus.

### Useful tools, not a verified match for the described “Trojan horse detector”

NVIDIA SkillSpector https://github.com/NVIDIA/SkillSpector ; Promptfoo https://github.com/promptfoo/promptfoo ; Trail of Bits Skills https://github.com/trailofbits/skills ; OWASP LLM Prompt Injection guidance https://genai.owasp.org/llmrisk/llm01-prompt-injection/ .

## The “saved 800 reels but never revisited them” workflow

**Goal:** preserve learnable content from legally accessible reels as a private local corpus, not secretly collect creator accounts or impersonate users. Original creator's full paid/DM guide was **not supplied**.

- Save source metadata and rights: creator, original URL, date, caption, content license, retrieved timestamp.
- Extract audio and transcribe with language-aware speech-to-text; Hindi/English code-switching needs review.
- Capture important scene changes/frames and align frame times with speech; sampling **every** frame is often wasteful.
- Keep verbatim transcript separate from normalized translation, phonetic corrections and outside research.
- Tag claims, links, demos, instructions, risks, permissions, software version and unresolved terms.
- Group by categories (Design/UX; skills/tools; security; backend architecture; video; education; privacy; marketing).
- Preserve each source in its own file with status and source ID; maintain a topic index.
- Extract concrete testable procedures, examples and limitations so the text remains useful if web pages disappear.
- Check all expected fragments are assigned; never invent a missing portion or a download-only prompt.
- Keep a dated correction log and verify that no sensitive contacts, home addresses or personal data were committed to a public repo.

### Example source record (conceptual)

Source ID: B6-01; speaker name unknown; media URL missing; language English/Hindi; text completeness partial; topic prompt injection; statement “three agents scan documents”; status not independently verified; outside research separate; installation none.

### Boundaries

Respect source terms and copyright; use only authorized media and approved data retention. A link or screenshot alone does not grant redistribution rights. Don't feed private documents to third-party AI scanners without informed approval.

See [16 — Source Register](16-INSTAGRAM-REELS-SOURCE-REGISTER.md) and [45 — Agent-Navigable Apps](45-AGENT-NAVIGABLE-APP-ARCHITECTURE.md).
