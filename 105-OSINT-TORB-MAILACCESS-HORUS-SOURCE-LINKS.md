# 105 — OSINT Comment: TorBot, MailAccess and Horus

**Source:** user's uploaded Instagram screenshot. Left: a reel cover with a stylized sun/eye and the large word **“OSINT”**. Right: a visible public comment that shares three GitHub links. The creator caption mentions OSINT, OPSEC, cybersecurity, ethical hacking and bug bounty; this doesn't establish the tools are safe or authorized for targeting specific people.

## Exact original three links (transcribed)

```text
https://github.com/DedsecInside/TorBot
https://github.com/KatrielMoses/MailAccess
https://github.com/6abd/horus
```

GitHub is case-insensitive for repository owner path; canonical redirect is `DedSecInside/TorBot`.

## Existence-verified repos and actual purposes

| Source link | Canonical GitHub | What project README supports | Important constraints |
|---|---|---|---|
| **TorBot** | https://github.com/DedSecInside/TorBot | Python open-source intelligence tool for Tor/onion site/link crawling, title/description extraction, link-tree output and optional analysis. | Onion content may be inaccurate, unlawful or hazardous depending on source; respect site access, local law and network privacy. Tor access does not grant permission to obtain private records. |
| **MailAccess** | https://github.com/KatrielMoses/MailAccess | Self-hostable email-address OSINT/reputation and exposure investigations with opt-in third-party modules, API integrations and structured exports; read official disclaimer. | Email addresses can identify people. Modules may consult breach datasets and publicly accessible personal information. Only assess self/organization-owned or authorized subjects; don't collect or publish third-party profiles. |
| **Horus** | https://github.com/6abd/horus | Python “all-in-one” investigation-assistance CLI drawing on configurable APIs and modules; some capabilities are marked partial/planned in README. | Not a comprehensive turnkey forensic suite. Includes API configuration and potential third-party service fees; code review and credential security necessary. |

### What the screenshot DOES NOT show

No original demonstration of a particular investigation, subject, scan, exploit, feature test or command; the three links are shared by another commenter, **not verified as the reel creator's official pack**. Treat them as independent repo leads, not a promise of universal investigation capability.

## Legitimate defensive uses

- Audit domains and exposed information your organization owns, with explicit scope and authorization.
- Review **your own** account's publicly discoverable email/digital footprint.
- Study OSINT provenance, uncertainty, public-source verification, ethical intelligence reports, retention and data minimization.
- Evaluate how to design investigator interfaces with evidence provenance and redaction.

## Privacy, safety and trust controls

1. Document authorized targets, collection scope, purpose and retention window **before** any lookup.
2. Do not use these tools to identify, track, profile or expose a private individual without proper authorization.
3. Do not automatically open unknown `.onion` content or run downloaded scripts on a primary device.
4. Avoid uploading sensitive emails/breach contents to unapproved third-party APIs.
5. Strip API keys and secret configs before committing; Horus README specifically warns about API keys in JSON.
6. Use a container/VM and pin dependencies if a future authorized test is requested.
7. Separate a scraped/external claim from independently corroborated evidence; export only necessary summaries.
8. Use defensive reporting and responsible disclosure, not doxxing, credential testing or bypass of service controls.

### Repository verification

All three public repository paths verified with GitHub metadata and README inspection on this pass; **none installed, executed, queried against a person or used for scanning**.

Related [42 — Digital Privacy](42-DIGITAL-FOOTPRINT-DATA-BROKER-REMOVAL.md), [74 — Mobile Security](74-PRIVACYPACK-AND-PLUG-IN-PHONE-MALWARE-DIAGNOSTICS.md), [06 — Security Tools](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md).
