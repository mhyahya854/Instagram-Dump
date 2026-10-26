# 72 — Ten Self-Hosted Alternatives from the User's Screenshots

**Source:** ten uploaded beige-background tool cards dated 2026-10-26. All **ten exact public GitHub repo identities independently verified**. Preserve screenshot claims about “replaces” and prices **as speaker claims**, not current financial comparisons or guaranteed feature parity.

## All ten, in exact screenshot order

| # | Screenshot tool | Verified GitHub repository | What it actually does | Screenshot's comparison (unverified price/feature equivalence) |
| ---: | --- | --- | --- | --- |
| 1 | **Paperless-ngx** | https://github.com/paperless-ngx/paperless-ngx | Self-hosted document management: ingest scans/PDFs/mail, OCR, full-text indexing, tags, correspondents and workflows | “Adobe Scan + Evernote — $15/mo” |
| 2 | **Karakeep** | https://github.com/karakeep-app/karakeep | Self-hosted bookmarking/archiving for links, articles, screenshots/media with searchable content and optional AI tagging | “Raindrop Pro + Pocket — $15/mo” |
| 3 | **Vaultwarden** | https://github.com/dani-garcia/vaultwarden | Unofficial lightweight Bitwarden-compatible server, implemented in Rust, intended for self-hosting password vault sync | “1Password Family — $10/mo” |
| 4 | **Anytype** | https://github.com/anyproto/anytype-ts | Official desktop client for local-first knowledge graphs, notes, objects and workspaces; its wider ecosystem contains other components | “Notion Plus + Roam — $20/mo” |
| 5 | **AdGuard Home** | https://github.com/AdguardTeam/AdGuardHome | Local/network DNS-level ad and tracker filtering, device coverage, query log and custom allow/block rules | “NextDNS Premium — $20/mo” |
| 6 | **Syncthing** | https://github.com/syncthing/syncthing | Continuous, peer-to-peer encrypted file synchronization between trusted devices | “Dropbox 2TB — $15/mo” |
| 7 | **Home Assistant** | https://github.com/home-assistant/core | Open-source home automation integrations, local control, schedules, automations and device dashboards | “SmartThings Pro + Alexa Plus — $25/mo” |
| 8 | **Audiobookshelf** | https://github.com/advplyr/audiobookshelf | Self-hosted audiobook and podcast library, streaming, progress, supported client apps | “Audible + premium podcast apps — $30/mo” |
| 9 | **Stirling-PDF** | https://github.com/Stirling-Tools/Stirling-PDF | Self-hosted PDF manipulation for merge/split/convert/compress/forms/OCR and more, edition-dependent | “Adobe Acrobat Pro — $20/mo” |
| 10 | **Bitwarden Send** | https://github.com/bitwarden/server | Encrypted sharing of files/text through Send inside the Bitwarden ecosystem; the linked repo is the **broader Bitwarden backend**, not a standalone “Send-only” repo | “WeTransfer Pro + Dropbox Transfer — $20/mo” |

## High-impact corrections to the carousel

**1. “Every receipt automatically scans itself” — Paperless-ngx.** A scanner, watched folder or upload/mail ingestion path must be configured first. OCR accuracy varies by language and scan quality. Sensitive tax/medical/company files need per-user access controls, encrypted backups and secure hosting.

**2. “AI automatically tags everything” — Karakeep.** AI tagging depends on the configured models/providers and accessible page/media content. It may incur costs or process private excerpts through external APIs. Saved links aren't guaranteed to be complete permanent backups of the original pages.

**3. “Nobody but you can access passwords” — Vaultwarden.** The Bitwarden-compatible client encrypts vault items, but encryption and self-hosting aren't absolute protection from weak master passwords, stolen/unlocked clients, server compromise, malicious updates, insecure sharing, backup exposure or admin operational mistakes. A personal vault needs recovery procedures and patching. Because this is an **unofficial Bitwarden-compatible server**, compatibility/security updates should be monitored.

**4. “Local fully encrypted and nobody else can read notes” — Anytype.** Local-first and encrypted sync require actual product setup, identity, sharing and device trust. The listed **anytype-ts is a client project**, not all components of a deployable private notes backend.

**5. “Every device is ad-free forever” — AdGuard Home.** DNS filtering can block known ad/tracker domains on configured devices but does **not** reliably remove first-party ads embedded within the same domain (including many streaming/video ads), native in-app placements or every new tracking endpoint. Some apps may break; devices using separate DNS/DoH or mobile data may bypass the filter.

**6. “Syncthing replaces Dropbox and provides no-cloud backup.”** Syncthing is **synchronization, not backup**. Deletes, overwrites, corrupt files and ransomware changes can propagate. Configure file versioning and **separate independent backups**. Data can transfer via optional relays/discovery infrastructure, even though content transport is encrypted. Mobile platform support differs.

**7. “Every smart device works together, no fees ever” — Home Assistant.** Check the device-specific integration and hardware radios; some products rely on vendor cloud APIs/subscriptions. Self-hosting needs maintenance, availability and backup. Use secure remote access and protect locks/cameras from unauthorized automations.

**8. “Buy audiobook once, no DRM, yours for life” — Audiobookshelf.** The server does **not** grant new audiobook rights, remove DRM from unrelated services, or bypass distribution licenses. Add only media you are authorized to manage and stream.

**9. “Does absolutely everything Adobe does for free” — Stirling-PDF.** Feature parity and prices depend on edition/version. **True redaction** requires destructively removing hidden content (not black overlays) and verification by extracting/searching text and inspecting metadata. OCR doesn't guarantee perfect text or signatures.

**10. “The expiring link means no one else can access it” — Bitwarden Send.** Send access may require a key/password depending on settings; expiration/deletion can stop **future** access, but recipients may already have downloaded or screenshotted content. Link forwarding, traffic/logs and endpoint compromise remain concerns.

### Cost comparison rule

The screenshot's ten claimed subscription “replacements” **cannot be totaled as guaranteed savings**. Managed hosting, storage, domain, electricity, time, data backup, paid APIs, optional mobile apps and commercial editions may cost money. Feature sets, limits and legal licensing aren't identical.

### Offline and self-hosting evaluation checklist

- Repository and license identified, dependencies/binaries reviewed.
- Single-user vs multi-user needs, OS/device support, mobile/iOS access, authentication and authorization.
- Data import/export and migration from existing provider proven on sample data.
- Privacy and data location of local models, telemetry, cloud integrations, backups.
- Signed images/tags, patch plan, TLS and secret management, tested restores.
- Real features tested before cancelling paid providers; no reliance on carousel marketing.
- For protected documents/passwords, threat model the self-hosted server and off-site backups.

**Status:** names and repositories verified, not installed/operated, screenshot is the source of price/“replaces” marketing, not proof of feature parity. See [26 — OSS Alternatives](26-OPEN-SOURCE-ALTERNATIVES-AND-LOCAL-TOOLS.md), [03 — Architecture](03-PRODUCTION-SYSTEM-ARCHITECTURE.md), [42 — Privacy](42-DIGITAL-FOOTPRINT-DATA-BROKER-REMOVAL.md).
