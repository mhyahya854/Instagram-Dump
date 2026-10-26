# 132 — “Per Visitor, Per Session, Per Email”: Legal-Risk Reel Claim Ledger

**Source:** screenshot 2 from sixteenth Instagram batch. The text below is **not legal advice**, and the reel's penalties are not automatic. Applicable law depends on jurisdiction, audience, service behavior, intent, collection, injuries, remedies, and current agency inflation adjustments.

## Screenshot: exact extracted six bullet claims

> Not a percent of revenue. Per visitor. Per session. Per email.
>
> 🎂 no age question on signup → $53,000 per kid (COPPA)
>
> 🔤 Google Fonts loaded from Google → €100 per visitor (Munich court, 2022)
>
> 🔵 session replay on by default → $5,000 per session (California wiretapping)
>
> ✉️ launch email with no unsubscribe / no address → $53,000 per email (CAN-SPAM)
>
> 💳 Stripe subscription with no renewal terms next to the button → every renewal is a gift you refund (California ARL)
>
> 🖼️ never registered the $6 DMCA agent → $150,000 per stolen image

**All six are source assertions, not automatic legal conclusions.**

## Verified context, correction and safer design outcome

| Claim | What sources actually support | Practical design/code check |
|---|---|---|
| COPPA $53k “per kid” for no age question | FTC says *up to* $53,088 per **rule violation** in cited guidance, assessed contextually. **Not every app is legally required to ask age**; COPPA applicability turns on child-directed service or actual knowledge of collecting data from under-13 children, operator role and other factors. | Assess audience and data collection; if COPPA applies implement appropriate age screening/notice/parental consent/data minimization; test child flow and consent records |
| Remote Google Fonts “€100 per visitor” | **Jan. 20, 2022 Munich judgment (3 O 17493/20)** awarded **€100 to that plaintiff** for IP transmission through dynamically loaded Google Fonts. A **March 30, 2023 Munich case (4 O 13063/22)** rejected another plaintiff's demand. **Neither creates a uniform €100 charge every visitor.** | Self-host fonts or choose provider/configuration consistent with GDPR/consent policy; verify actual network requests and data transfer |
| Session replay “$5k per session” | California Penal Code **§637.2** specifies **$5,000 per violation or three times actual damages**, for a *legally established violation* of relevant privacy laws. Whether replay/tag scripts violate CIPA is fact- and court-dependent. Not every session equals an illegal interception. | Document replay vendors and data flow, obtain consent where required, redact fields/credentials, disable sensitive-event capture; obtain jurisdiction-aware review |
| CAN-SPAM “$53k per email” | FTC guidance gives **up to $53,088 per separate unlawful commercial email**; requirements include truthful headers/subjects, postal address, working opt-out, timely honoring opt-outs, and limits on deceptive claims. Not all launch emails or transactional messages are the same legally. | Classify marketing vs transactional, provide sender postal address and unsubscribe, suppression list, email send logs and test opt-out |
| California ARL renewals automatically “gifts” | California Automatic Renewal Law imposes clear renewal terms, affirmative consent, simple cancellation and applicable notice obligations; the screenshot's universal “every renewal is a gift” remedy is **oversimplified** and subject to statutory terms and litigation. | Make price, frequency, renewal, cancellation, consent and confirmation clear; verify receipts, subscription portal and cancellation |
| $6 DMCA agent missing ⇒ $150k per image | US Copyright Office says **$6** to designate a DMCA agent, an element for applicable **§512(c) safe harbor** eligibility. **$150,000** is an upper statutory-damages figure for **willful infringement per work**, not an automatic fine for not registering. Other safe-harbor conditions also apply. | If hosting user uploads, assess safe-harbor applicability, designate agent if appropriate, implement notices/takedowns/repeat-infringer policy; use licensed content |

## Official or primary references

- FTC COPPA FAQ: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions
- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- Munich Jan 2022 decision: https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2022-N-612
- Munich March 2023 decision: https://www.gesetze-bayern.de/Content/Document/Y-300-Z-BECKRS-B-2023-N-6354
- California Penal Code §637.2: https://codes.findlaw.com/ca/penal-code/pen-sect-637-2/
- California Attorney General ARL alert: https://www.oag.ca.gov/news/press-releases/attorney-general-bonta-issues-consumer-alert-california%E2%80%99s-automatic-renewal-law
- Copyright Office DMCA directory FAQ: https://www.copyright.gov/dmca-directory/faq.html
- US Code 17 USC 504 statutory damages: https://www.law.cornell.edu/uscode/text/17/504

## Pre-launch audit questions

Where do users live? Are children targeted? Which browser tags transmit IP/session data? Are marketing emails opt-out compliant? Is subscription renewal consent truly explicit? Does the app host user-generated copyright material? Does a privacy notice accurately describe real data collection? Are security/privacy controls tested in the **deployed** build?

These six concerns should be checked **by jurisdiction and app behavior**, not hardwired as blanket legal penalties in a coding agent’s universal instructions.

**Status:** original screenshot archived, legal sources linked and misleading generalizations flagged; no legal representation, regulator consultation, vendor audit, website code changed or formal certification performed.
