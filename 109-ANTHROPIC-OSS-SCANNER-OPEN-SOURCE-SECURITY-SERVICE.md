# 109 — Anthropic OSS Scanner: Verified GitHub Security Service

**Source:** separately typed direct GitHub URL `https://github.com/anthropics/oss-scanner` (2026-10-26), no screenshot for this specific project. Official repository verified via connected GitHub and official vendor source at https://red.anthropic.com/oss-scanner/ .

## What it actually is

**OSS Scanner** is an **opt-in Anthropic security scanning service for eligible public open-source repositories**. Enrollment occurs by a maintainer-submitted pull request in the public `anthropics/oss-scanner` repository, creating `projects/<name>/` with configuration. Anthropic's scanning infrastructure then builds/tests the project and sends vulnerability reports to the nominated maintainer contact.

It is **not** simply `pip install oss-scanner` / a generic one-command GitHub Action for private repositories, and **not** a replacement for secure design, tests, pentesting or an incident response plan.

## What the published service and README say

- **Eligibility:** targets critical open-source projects meeting service criteria; enroll via PR under `projects/<name>`.
- Required `project.yaml`: public GitHub repository URL and **primary contact email**.
- Build specification: a trusted project Dockerfile (in repo or alongside enrollment), with project dependencies/fixtures.
- Optional `threat_model.md`: business context, assets, input trust boundaries and severity guidance. This is important for catching failures beyond generic scanner rules.
- Scanner setup/build uses internet access, then the analysis runs in an isolated VM **without internet access**.
- Reports arrive by email to maintainer and optional CCs; can use an **OpenPGP public key** to encrypt reports (no CC with encrypted delivery).
- **Critical report caveat:** the opt-in **fast track sends model-generated findings without human review**, directly to the project contact. Anthropic also describes a separately manually reviewed coordinated-disclosure process; they must not be conflated.
- README describes edit/disable/withdraw enrollment via project entry changes.
- Its local preflight `tools/check` runs Docker build code with network, and `--qemu` uses a VM; **do not run arbitrary untrusted project Dockerfiles on a primary computer**.

### Example data model — *educational, not an enrollment performed*

```yaml
repo: https://github.com/OWNER/PUBLIC-REPO
primary_contact: security@example.org
dockerfile: .oss-scanner/Dockerfile
threat_model: .oss-scanner/threat_model.md
```

The address above is a placeholder, **not a real recipient**. Don't publish the user's personal email as `primary_contact` without approval.

## Appropriate use in our repo ecosystem

- Consider for future **eligible, public, actively maintained production code repositories** where the user is an authorized owner and agrees to public enrollment and the vendor's terms.
- **Instagram-Dump and Universal-Rules are primarily documentation/rulebook repositories**, so enrollment need not be appropriate and is **not requested** by the user.
- For local/private projects use existing tests, dependency scanning, static analyzers, secret scans, access-control negative tests and a targeted human-reviewed security assessment. Complementary tools are described in [06 — AI Failure Mitigation](06-AI-FAILURE-MITIGATION-REPOS-AND-SKILLS.md).
- Analyze all reported issues with a reproduce/fix/retest loop and avoid blindly executing “proof of concept” strings sent by third parties.

## Operational risk checklist

1. Confirm repo is public, ownership/maintainer approval, eligibility and commercial/third-party data restrictions.
2. Review enrollment terms and permissions before opening the public PR.
3. Prepare a **safe reproducible Dockerfile** free of production secrets, customer data and privileged service calls.
4. Use a security-role public contact address where appropriate, not a personal mailbox shared inadvertently.
5. Draft threat model with actual authorization matrix, business invariants and deployed attack surface.
6. Accept that AI-generated findings can be inaccurate; reproduce in safe environments and have qualified review.
7. Rotate exposed secrets proactively; scanning a repository doesn't remove history or invalidate compromised tokens.
8. No automatic push/fix/app deployment just because a scanner suggests it.

## Sources

- Official repo: https://github.com/anthropics/oss-scanner
- Official service: https://red.anthropic.com/oss-scanner/
- Official terms: https://red.anthropic.com/oss-scanner/terms

**Status:** project verified and catalogued. **No enrollment PR submitted, no repo shared with scanner, no email supplied, no code scanned or downloaded, no vendor account connected**.
