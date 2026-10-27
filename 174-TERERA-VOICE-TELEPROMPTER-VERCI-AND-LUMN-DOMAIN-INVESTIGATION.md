# 174 — Terera and two unresolved .xyz app leads

**Original typed inputs, 2026-10-27:** “there is an app called terera”; “apps called verci.xyz, trylumn.xyz”. **Source class:** user-typed names/URLs, not screenshots. Keep spelling exactly. **Research:** official website discovery, product details and independent site fetch attempts; no download, purchase, login, installer execution or network inspection of downloaded binaries.

## Terera — voice-following teleprompter

**Official site:** https://terera.app/ ; **downloads:** https://terera.app/download . The vendor identifies itself as **Terkon Pty Ltd (Australia)** and distributes a **paid desktop app**. **It is not presently verified as open-source**; do not invent a GitHub repository or assert permission to clone it.

### What it does

A transparent floating teleprompter/reader above existing applications follows an English-speaking presenter's **actual spoken words** instead of scrolling at a rigid fixed speed. It can pause while the user thinks, hold position on an off-script digression, and resume when the script picks up again. Multiple fixed reading positions or a moving placement can help the speaker look toward different people/cameras without sweeping eyes across a long line.

**Uses:** Zoom/Teams/Meet calls, recorded explainer or course video, public talks, presentations, interviews and rehearsing scripts. Word documents (\`.docx\`), rich text, emphasis and formatting can be imported. Song lyrics can be followed by manually timed scroll instead; voice-follow mode is tuned for spoken words, not singing.

### Technical architecture and privacy representations

According to its **own** official site, Terera downloads a speech-recognition model of about **190 MB** during first setup and then performs speech recognition **locally** on Windows/Mac. Scripts, audio and rehearsal feedback are said to remain on device. Internet connections are still needed for the initial model download, trial activation and periodic license checks. This is **vendor-described**, not verified by independent packet capture or software audit. A local speech recognizer may mis-hear accents, overlapping voices, noise, or speakers from a laptop microphone, so evaluate a real microphone/setup during trial.

The overlay is designed to keep clicks passing through to underlying apps; screen-share hiding depends on the conferencing app's capture behavior. Always inspect the preview **before** sharing sensitive notes. The product does not track eyes or use gaze detection according to its published description.

### System and pricing (vendor snapshot, 2026-10-27)

| Property | Vendor-stated terms |
|---|---|
| Windows | Windows 10 / 11 |
| macOS | macOS 15.5+, Apple Silicon or Intel |
| Speech | English; microphone; audio matching, not speaker diarization |
| Trial | 14 days; vendor says no payment card or account |
| Personal license | **USD 89 one time** (vendor site), three personal devices, 12 months of updates, installed version usable afterwards |
| Refund | Vendor states 30 days; verify detailed terms at purchase |
| Network | First-time model download, trial and licensing checks |

**Do not assert price/terms never change**, and do not call all features verified simply because an interactive website demo exists. Check vendor installer signature, OS entitlements, local file permissions, telemetry policy, update channel and accessibility before recommending production adoption.

### Comparable alternatives by function, not endorsement

Teleprompter.com, BigVU, Speakflow, Onwords or a basic PDF/PowerPoint presenter view may meet simpler scrolling needs. Differentiate **true speech-following pause/off-script resume** from constant-scroll and AI subtitle generation. For an internal replacement design, a desktop always-on-top/transparent overlay + local STT + fuzzy script alignment + pause/detour state machine + secure license/update flow is a feasible architecture, **not** a claim to reproduce Terera's proprietary implementation. Prioritize consent and on-device/offline operation.

## \`verci.xyz\` — exact spelling preserved; identity unverified

**Input URL (not independently verified as a product):** https://verci.xyz/ . Exact-domain browser fetch on 2026-10-27 returned a cache/fetch failure, and targeted public searches did not establish an authoritative publisher, product purpose, pricing, privacy policy or code repository. **Do not create invented feature descriptions, screenshot transcriptions, “official GitHub” paths or positive security guarantees.** The domain may be inactive, new, inaccessible, privately indexed or a typo. Status: **UNRESOLVED; no access or purchase**.

**Next evidence required:** functioning homepage or original screenshot, source creator, app store/profile link, repo owner, changelog, privacy/licensing details and preferably reproducible test on a disposable environment. Until then treat it as a direct typed research lead only.

## \`trylumn.xyz\` — exact spelling preserved; identity unverified

**Input URL:** https://trylumn.xyz/ . Direct website fetch in research returned a cache/fetch failure; a third-party domain assessment offered warnings about young/low-traffic hosting but **cannot conclusively establish fraud or the product's actual purpose**. No official product documentation, codebase, capabilities, billing or legal identity was independently recovered. Status: **UNRESOLVED / UNVERIFIED SITE**. Never instruct installation, authentication, credit card entry or sharing private materials without better proof.

**Audit method for both domains:** validate DNS and HTTPS independently in a sandbox, compare archive snapshots, inspect publisher contact/legal identity, signed software/notarization, payment merchant, privacy/retention/permissions and versioned source where available. Third-party reputation scores are cues, not fact checks or proof of illegitimacy.

**Related:** [26 — local/private tools](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md), [74 — malware diagnostics](74-PRIVACYPACK-AND-PLUG-IN-PHONE-MALWARE-DIAGNOSTICS.md), [172 — agent products](172-MULTICA-LANGWATCH-ORCA-CODING-AND-AGENT-ORCHESTRATION.md). Documentation-only; the target repo alone was modified.
