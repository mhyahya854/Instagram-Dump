# 179 — Tracebase: digital-footprint discovery, account cleanup and privacy evaluation

**Date:** 2026-10-27. **Original user input:** usetracebase.com (typed URL; NOT a screenshot). **Publisher site:** https://usetracebase.com/ ; **manual guides:** https://usetracebase.com/learn .

**Source basis:** Retrieved the vendor's public homepage/FAQ and guides. These are vendor claims, not tested backend guarantees. No personal email, username, password or payment data was submitted. No scans, deletions, signups or purchases performed. A canonical public open-source repository for the service was not verified.

## What is Tracebase?

Tracebase offers digital-footprint discovery: identify candidate forgotten website accounts through email addresses and usernames, cross-reference known breach records, and supply platform-specific account-removal guides.

The exact public homepage headline is **“Find the accounts you forgot about.”** Its FAQ claims checks across **600+ platforms** using **public APIs, registration endpoints and profile pages**, with email verified using a one-time code before a scan. It says passwords are not needed or stored, and account/data deletion can be requested through Settings. This is an advertised service, not independent proof that all 600+ adapters work correctly.

The sample dashboard on the homepage features mock account counts and risk scores, including 47 accounts, 6 breaches, and a score of 78 High risk. These numbers are **illustrative and not an observed scan result**. Do not present them as verified accuracy or exposure data.

## How it could work — engineering interpretation, NOT vendor source code

~~~text
User-provided email and/or usernames
  → email possession/authorization confirmation
  → normalize and scope checks with responsible rate limits
  → authorized public-profile/account/breach lookup adapters
  → map results to dated source evidence and confidence levels
  → deduplicate and distinguish users with the same handle
  → user reviews and verifies ownership manually
  → display first-party account deletion and security steps
  → account-data deletion, optional consented monitoring
~~~

**Critical technical distinction:** a public profile that shares a username is *not proof of ownership*; a breach mention does not prove an account is still active; a password-reset endpoint may intentionally obscure account existence to prevent enumeration; and data-source coverage is partial. The backend implementation, false-positive rate, false-negative rate and exact platform list are **unverified** here.

## Useful self-audit cases

| Scenario | Potential value | Independent confirmation needed |
|---|---|---|
| Forgotten accounts | A list of sites to inspect | Your own login history, inbox receipts or password manager |
| Breach exposure | Prioritize real credential compromise | Check breach provider methodology, rotate reused passwords via official website |
| Public handles | Find your publicly visible profiles | Distinguish namesakes or impersonators |
| Cleanup | Link to deletion/opt-out steps | Confirm site URL is genuine, cancel subscription, export data first |
| Monitoring | New-record alerts if a plan offers them | Verify opt-in, timing, accuracy, cancellation and retention |

## Privacy and security risks

- Email and username combinations are **sensitive identifiers**. Linked-profile/breach results can expose social, employment or other information even without storing passwords.
- Email one-time-code verification does not itself prove safe retention, encryption, deletion or good employee/subprocessor access controls.
- Never provide a digital-footprint site a **social-media password**, reusable OTP, recovery key, session cookie, social-account access token or device unlock information.
- Avoid unauthorized account enumeration of other people. Scan only your own identifiers or authorized organizational domains under clearly defined permissions.
- Account removal can have irreversible consequences, including losing GitHub repositories, subscriptions, purchases, authentication options or professional accounts; export and transfer ownership first.
- Risk ratings may be proprietary proxies with unknown weighting. Base decisions on concrete, documented exposure.
- Verify terms and a real privacy policy before submitting identifying data. **Full first-party legal and data-retention terms were not independently retrieved in this review**; don't claim they do not exist.
- A public website does not imply open-source software, offline operation, local-only processing, independent pentesting or production readiness.

## Price and geographic coverage

The public homepage contains a **pricing** section and describes subscription cancellation from billing, but reliable current checkout prices and exact per-plan scan limits did **not** appear in retrieved public text. A third-party listing has pricing claims, but without current primary-source verification those amounts are not adopted here. Before purchase verify introductory-vs-renewal prices, currency, geographic restrictions, scans per month, monitoring billing, refund terms and deletion rights.

## Free-first workflow (without uploading your identifiers to another service)

1. Search the email inbox **you own** for verification, welcome, subscription and password-reset receipts.
2. Search your **own** password-manager vault and passkey/connected-app listings.
3. Check known breaches with the official https://haveibeenpwned.com/ site, mindful that its source coverage is incomplete too.
4. Review Google/Microsoft/Apple first-party connected-app authorizations.
5. Evaluate public accounts you own; keep records or export data before irreversible deletion.
6. Use first-party account settings for closure and official Google Results About You tools: https://support.google.com/websearch/answer/12719076 .
7. For broker listings, apply official opt-outs and relevant data-rights requests. Tracebase's manual guide collection is here: https://usetracebase.com/learn .

## Relation to other tools

- **Have I Been Pwned:** focuses on breach-data exposure, not inventorying every account.
- **Google Results about you:** eligible removal from Google Search does not necessarily remove the origin website.
- **Password managers:** authoritative for *saved* accounts, not every account ever created.
- **Tracebase:** vendor claims additional broad account discovery and removal references; not independent proof of complete identity mapping.

**Cross-reference:** [42 — self-directed digital-footprint cleanup](42-DIGITAL-FOOTPRINT-DATA-BROKER-REMOVAL.md), [74 — privacy and security](74-PRIVACYPACK-AND-PLUG-IN-PHONE-MALWARE-DIAGNOSTICS.md), [181 — exact typed-source register](181-OCT27-TRACEBASE-CLAUDE-SEO-SOURCE-REGISTER.md).

**Source/fact distinction:** official domain, public FAQ, 600+ *claim*, OTP, guides, no-password *claim* are documented. Actual service implementation, independent coverage, retention guarantees, legal policy, exact price, full platform list, back-end source code and individual scan outcomes remain unknown. No account or system was modified.
