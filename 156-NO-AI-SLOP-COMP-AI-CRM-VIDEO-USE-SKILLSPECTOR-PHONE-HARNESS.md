# 156 — Four Product/Skill Chips + Phone Harness

**Original images:** `image(20261026-181252).png` contains four visible black pill labels **“no-ai-slop”**, **“comp-ai crm”**, **“video-use”**, **“SkillSpector”**. `image(20261026-181340).png` shows only bold text **“5. PHONE HARNESS”**. They have no direct URL in the screenshots. Research matches below are grounded GitHub repository candidates, **not guaranteed original links**.

| Exact image label | Verified matching repo | Scope and caution |
|---|---|---|
| no-ai-slop | [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) | Writing improvement rules, not a universal UI anti-slop scanner; avoid false AI-detector confidence |
| comp-ai crm | [trycompai/crm](https://github.com/trycompai/crm) | Open-source agent-oriented CRM; permissions, tenant isolation and real integration security required |
| video-use | [browser-use/video-use](https://github.com/browser-use/video-use) | Prompt-driven video editing using local scripts/FFmpeg; check asset licenses, install scripts and machine resource use |
| SkillSpector | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Agent skill supply-chain scanner; catches static patterns and optionally LLM semantic risks but never proves “safe” |
| PHONE HARNESS | [ShawnPana/phone-harness](https://github.com/ShawnPana/phone-harness) | Works with iOS mirroring or Android ADB workflows and cloud device adapters; **identity remains a research match until source URL supplied** |

## Phone Harness: concrete mechanism from upstream

- iOS: screenshot of **iPhone Mirroring** window, Apple Vision OCR for visible text, simulated taps/swipes/typing.
- Android: ADB screenshots and input, accessibility/UI text tree; requires user-provided device connection and authorization.
- Cloud devices: adapters for remote Android/iOS environments.
- Constraints documented by repo: no native multitouch, real-device unlock/camera/Face ID and DRM limits; icon-only targets often need model vision. **User must connect device.**
- Strong security boundary: phone screenshots reveal notifications, private messages and account content; never grant an unattended agent unrestricted device access or let it install apps/change permissions/pay without approval.

## SkillSpector review in practical use

The NVIDIA project advertises **71 patterns across 17 categories**, SARIF/JSON/Markdown output, and static+optional LLM analysis. Scan untrusted `SKILL.md` packages and scripts **before** granting permissions. A clean scanner result is insufficient by itself; manually inspect tool execution, network URLs, file access, symlinks, downloads, supply-chain version and license. Avoid automatically installing the scanner itself from random scripts.

## What these are NOT

- “No AI Slop” **writing** and UI design anti-slop are different domains; keep [01 UX](01-DESIGN-UX.md) and [02 app quality](02-VIBE-CODED-APP-QUALITY.md) separately.
- “Comp AI CRM” is an app, not necessarily a system prompt or agent skill.
- “video-use” is an editing workflow, not guaranteed fully offline for every possible provider.
- “Phone Harness” isn't blanket permission to control users' phones.

**No tool installed or executed; no phones, accounts, browsers, media or private data accessed.**
