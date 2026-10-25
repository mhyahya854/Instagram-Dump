# 19 — Agent Skills, Hooks, Code Reviews and Code-Drawn Animation

Captured: 2026-10-25. Research register; **no skills installed, no commands executed**.

## Spoken reel: Antigravity plugins

| Spoken name | Research result | What to preserve |
|---|---|---|
| Get Shit Done | GSD agent workflow (see https://getshitdone.help/) and ecosystem; Antigravity adapters also exist | Break a large goal into milestones, smaller deliverables and validation gates; this is not proof of speed improvement |
| “RAL flow” | **Unresolved**, possible “Ralph”/“Ralph Flow” agent iteration pattern | An agent repeatedly selects next work/checks code. Set explicit budget, stop condition and authorization; do not assign a fabricated canonical repository |
| CodeRabbit | https://www.coderabbit.ai/ and https://github.com/coderabbitai | AI-assisted pull-request code review; findings require developer verification |

No Antigravity plugin was installed or enabled.

## “Slop Monster” for writing

**Confirmed repository:** https://github.com/ItsssssJack/SlopMonster.

The tool scores AI-like prose patterns, flags overused vocabulary and formulaic structures, and offers a rewrite/check workflow (which may use a second model/CLI). Useful for copy review and clarity, **not** for deceiving readers, proving human authorship or bypassing detectors. Preserve accuracy, citations and actual meaning. It is not the same product as visual anti-slop tools like Impeccable or Hallmark. Review text-handling privacy and inference costs.

## “Apple Design” by Emil Kowalski

**Confirmed canonical source:** https://github.com/emilkowalski/skills ; skill path skills/apple-design/SKILL.md. Site: https://emilkowal.ski/skill.

This skill translates interaction principles into web practices: immediate feedback, dragging/gestures, momentum/spring, spatial continuity, polish and restraint, tactile-feeling motion, and reduced-motion support. Reel's “watched every Apple WWDC” is creator commentary rather than a factual verification of all talks. **Do not default to Apple visual imitation or excessive liquid glass.**

## Design-skill workflow, from the tier-ranking reel

A **D-tier idea** is “change the style” without identifying the problem; often swaps one generic aesthetic for another.
**C-tier** is using a generic frontend design skill, helpful but insufficient.
**B-tier** is showing a real example; useful, but the agent still has to infer exactly what you admire.
**A-tier** is persistent project design context: documented typography, semantic color, spacing, components, examples and explicit anti-patterns. Tier names are the creator's editorial opinion, **not measured rankings**.

A practical configuration:
1. Keep persistent design intent in a human-readable DESIGN.md and scoped AGENTS.md / CLAUDE.md where applicable.
2. Explain both **positive references** and **avoid-by-default** patterns (generic gradient, giant italic serif, decorative stripes, false social proof).
3. Validate output against real viewports, accessibility, actual product requirements and license boundaries.
4. Add Figma MCP when there is an authorized source-of-truth Figma document and supported connector; do not pretend screenshot similarity alone proves parity.
5. Browser automation (e.g. Playwright) can inspect visual rendering and interactions but needs safe scope and assertion-based tests.

## Claude Code hooks: instructions vs reliable automated actions

A **rule** tells an agent what to do; a **hook** triggers a configured handler when a specific event happens. Example events:
- **PostToolUse / Write/Edit:** run a formatter or lint changed files.
- **Stop:** test task completion or send a notification.
- **PreToolUse:** reject dangerous tool calls before execution.
- **SessionStart:** load project context.
- **PermissionRequest:** route approval, not blindly auto-approve privileged commands.

Hooks can perform real shell commands **with the invoking user's permissions**. A malicious hook can delete files or leak secrets. Keep hook scripts reviewable, pin sources, avoid untrusted dynamic input, and test on sandbox data. Do not rely on a hook alone for production access control or irreversible-action confirmation.

Official docs: https://claude.com/resources/articles/how-to-configure-hooks ; https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more .

## Code-drawn video / animation reel

The clip claims Claude Code plus a creator-provided animation skill can research scenes, write procedural drawings, render video frames and compose sound. **The exact skill is unidentified.** A code-rendered animation is possible using SVG/Canvas/WebGL/Blender/Remotion/FFmpeg or programmatic composition, but this is not the same as a guarantee of quality or the original reel's exact workflow.

General concept:
- Storyboard: audience, message, aspect ratio, duration and style references with rights.
- Scene graph: geometric elements, text, transforms, easing/timeline and visual layering.
- Renderer: deterministically produce ordered image/video frames.
- Sound: licensed speech, sound design and music synchronized with scenes.
- QA: inspect legibility, motion sickness/reduced-motion alternatives, frame timing, audio rights and render logs.

Do not infer the model name, exact effort setting, or a skill's capability merely from the Instagram copy; they may change.

## Skill-review checklist (to use before any installation)

- Confirm upstream author and repo, version, dependencies, scripts and any update checks.
- Read all executable instructions and check prompt-injection/secrets-exfiltration risk.
- Restrict file access, network, credentials and browser sessions.
- Define evaluation cases and collect evidence.
- Distinguish **catalog approved** from **installation approved** and **security audited**.

Existing reference: [08-AGENT-REPOS-AND-SKILL-WISHLIST.md](08-AGENT-REPOS-AND-SKILL-WISHLIST.md), [06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md).


## Voice transcript: “UI UX Comma Design” / 136K-star design skill

Possible meaning is **UI/UX Pro Max**, an existing design-intelligence skill documented in [05-THINGS-TO-FIND.md](05-THINGS-TO-FIND.md) and at https://github.com/nextlevelbuilder/ui-ux-pro-max-skill . **The phonetic wording is uncertain**, and the reel's 136K-star count was not independently established as belonging to the exact skill. Do not merge a name or trust a popularity claim without source confirmation.

## “UI UX Comma Design” and the 136K-star claim

The reel refers to a purported design skill “UI UX Comma Design” with 136,000 stars. It **may mean UI/UX Pro Max** (https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), which is independently documented in the repo's existing skill notes. The wording and numerical claim are not conclusively matched to that upstream source. Keep **raw name and uncertainty**.
