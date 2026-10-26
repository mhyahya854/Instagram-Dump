# 153 — Five Software Licenses: Proprietary, MIT, LGPL, GPL, AGPL

**Original image:** `image(20261026-173027).png`. Source heading **“Freedom is a spectrum.”**, subtitle **“Every license answers one question: how much do you get to change?”**, and inset card **“THE MAP — Five licenses. Five different obligations.”**. The left illustration shows top **MOST FREEDOM**, then vertically **AGPL → GPL → LGPL → MIT → PROPRIETARY**, ending **LEAST FREEDOM**. The screenshot presents a *single ranked axis*, a useful teaching device but **legally misleading if read literally**: freedom and reciprocal obligations are different axes.

| License name as pictured | Engineering reality | Key redistribution condition |
|---|---|---|
| Proprietary | Rights depend on the actual EULA; not necessarily source available | Generally no modification/redistribution unless explicitly granted |
| MIT | Permissive copyright license; allows modification, distribution and commercial use subject to notice and liability disclaimer | Keep required copyright/license notices |
| LGPL | Weak copyleft for libraries; allows some combinations with proprietary apps under conditions | Library modification/source requirements and user ability to modify/relink depending on version/conveyance |
| GPL | Copyleft for covered combined/distributed derivatives | Offer complete corresponding source under compatible GPL terms when distributing covered binary work; obligations depend on GPL version |
| AGPL | Extends GPL-style source obligations to certain modified programs made available over networks | Network interaction with modified AGPL-covered software can require source offer to users |

## Corrections worth preserving

- **AGPL is not categorically “more freedom” than MIT** for downstream proprietary integration. MIT usually imposes fewer reciprocity obligations; AGPL/GPL preserve freedoms for recipients by imposing stronger sharing conditions. Choose which freedom you mean.
- “Hosted SaaS can ignore open-source license” is false for **AGPL** network obligations, and GPL still applies when distribution/conveyance triggers it.
- Libraries, fonts, stock photos, UI components, documentation and video/audio assets can all have **different licenses** from the main GitHub repository.
- If combining open-source components, track package versions, SPDX IDs, notices, modifications, distribution form, dynamic/static linking where applicable, and obligations for source availability.
- “Open source” alone does **not** authorize uploading proprietary customer data to an outside AI provider, stripping credits, reproducing competitor logos, or redistributing original art.

**Useful primary references:** [choosealicense.com](https://choosealicense.com/), [Open Source Initiative license list](https://opensource.org/licenses), [GNU GPL/LGPL/AGPL FAQs](https://www.gnu.org/licenses/gpl-faq.html), exact LICENSE file of each pinned repo.

**Status:** screenshot taxonomy preserved with independent legal qualifications; this is a general technical checklist, not a specific product's legal opinion. No license-compliance audit performed.
