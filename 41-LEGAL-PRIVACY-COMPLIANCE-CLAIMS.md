# 41 — Legal/Privacy Risks of Launching a Web App (Jurisdiction-Sensitive)

Captured 2026-10-25. This note evaluates a viral “vibe-coded app gets sued with zero sales” claim. **General information, not legal advice.** Actual obligations vary by the countries/states of the business, users, processors, products and dates. Have qualified counsel review regulated, high-volume, subscription and user-upload offerings.

## Spoken headline claims — source-checked with important qualifications

| Reel claim | Accurate reference and limits | Correct practical response |
| --- | --- | --- |
| “Google Fonts loaded remotely, Munich court made site pay €100” | **Real 20 January 2022 decision**, LG München I, 3 O 17493/20: website unnecessarily sent a visitor's dynamic IP to Google to download fonts without applicable legal basis, and court ordered **€100 in that case**. This is neither a blanket ban on Google Fonts nor a universal per-visitor fine. | If subject to relevant EU/German law, evaluate lawful basis and use self-hosted fonts if feasible. Inventory external font requests, privacy notice and data flows. |
| “Session replay records keystrokes; in California that's wiretapping, $5,000 per violation” | California Invasion of Privacy Act section **637.2** provides statutory damages **$5,000 per proven violation or triple actual damages**. Whether a specific replay/chat/pixel implementation violates CIPA is disputed and facts/court rulings differ; *recording keystrokes is not automatically always illegal*. | Audit analytics/session replay SDK, mask sensitive fields, reduce recording, review third-party sharing and lawful notice/consent, and get counsel for California reach. |
| “One launch email without unsubscribe, $53K per email” | FTC CAN-SPAM guidance identifies up to **$53,088 for each separate violating commercial email**; the FTC's September 2026 notice retained 2025 penalty levels. This is a maximum statutory exposure, not an automatic fine for any message. Transactional emails have a different analysis. | Commercial email requires truthful header/subject, valid physical postal address, clear opt-out and prompt honoring of requests. Ensure email marketing permissions and regional privacy requirements. |
| “Renewal terms not next to Subscribe, every subscription is a gift” | California Automatic Renewal Law requires clear, conspicuous **pre-agreement proximity**, express consent, acknowledgement/cancellation instructions and other notices depending on offer/date. The reel's “gift” or automatic voiding conclusion is too broad; remedies depend on facts and applicable law. | Present price/frequency/trial conversion/terms and cancellation visibly before consent; log consent, test easy cancellation and renewal notices. |
| “No six-dollar DMCA agent means no shield for stolen uploads” | US Copyright Office **designated agent registration is $6** per designation/amendment/resubmission. DMCA §512 safe harbor requires more than registration: qualifying service-provider conduct, notice/takedown procedures, repeat-infringer policy and other conditions. Not every simple non-upload website needs the same service-provider arrangement. | If user-uploaded copyrighted content and eligible for safe harbor, consider proper agent registration, published agent details, notices, takedowns, counter-notices and retention/audit process with counsel. |

## Why “zero sales” is not an exemption

Privacy, tracking, breach, consumer protection, email and copyright obligations can arise from operating a website or handling a visitor's data **before** a paying customer exists. Yet the exact US state and EU regulations require geographic/factual analysis; don't copy an American law into every country as a universal global rule.

### Data-flow map to create before enabling tracking

1. Visitor enters page: IP, cookies, fonts, CDNs, analytics scripts and browser fingerprinting.
2. Visitor fills forms: personal data, messages, contact information; determine destination and retention.
3. Visitor signs up: accounts, passwords, login sessions, email service and database policies.
4. Visitor buys: payment processor, subscription terms, receipts, taxes/refunds and webhook handling.
5. Visitor uploads: copyright/privacy/illegal content moderation, access rules and retention/deletion.
6. Visitor requests deletion or unsubscribes: verified identity, scope, jurisdiction and documented process.

### Practical legal review checklist

- [ ] Applicable jurisdiction and user markets recorded.
- [ ] Privacy notice covers actual processing and vendors; consent/cookies considered where applicable.
- [ ] Remote fonts, analytics, pixels, session-replay and advertising scripts inventoried.
- [ ] Sensitive input fields never sent to analytics or replay vendors unnecessarily.
- [ ] Commercial email policy includes opt-out, truthful subject, postal contact and honor deadlines.
- [ ] Recurring pricing, billing frequency, free-trial conversions, consent record and easy cancellation validated.
- [ ] User-upload copyright complaints, DMCA eligibility and designated agent evaluated where applicable.
- [ ] Security and incident reporting, retention/deletion, vendor contracts, minors/health data obligations considered if relevant.
- [ ] Evidence retained for review; do not claim a legal audit was performed by prompts alone.

## Primary legal sources (dates matter)

- **Munich court official:** https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2022-N-612
- **California Penal Code §637.2:** https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=637.2.&lawCode=PEN
- **FTC CAN-SPAM business guidance:** https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- **FTC 2026 penalty notice:** https://www.govinfo.gov/content/pkg/FR-2026-09-15/html/2026-18853.htm
- **California renewal statute:** https://california.public.law/codes/business_and_professions_code_section_17602
- **California AG consumer alert:** https://oag.ca.gov/node/608083
- **US Copyright Office designated-agent FAQs:** https://www.copyright.gov/dmca-directory/faq.html
- **DMCA safe harbor US statute:** https://www.copyright.gov/title17/92chap5.html#512

See [37 — Website Prelaunch](37-WEBSITE-PRELAUNCH-RELEASE-CHECKLIST.md) and [20 — Security Hardening](20-SECURITY-SERVER-HARDENING-OSI-LAYERS.md).
