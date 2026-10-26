# 113 — FreeLLMAPI: Multi-Provider Router and Advertised Free Quotas

**Source:** image 7, a cropped card labelled **“FreeLLMAPI”**. Source claim is kept verbatim here; it is **not verified actual monthly usage available to any particular user**.

## Exact source text visible

> 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. One OpenAI-compatible endpoint.

> Aggregate free tiers from dozens of providers, plus custom OpenAI-compatible chat, embedding, image, and audio endpoints, behind a single `/v1` API. Keys are stored encrypted. A…

Screenshot is cut off after “A…”. Do not invent completion as if transcribed.

## Verified public research

- Canonical primary GitHub candidate: **https://github.com/tashfeenahmed/freellmapi**
- Related publicly accessible upstream/copies include **https://github.com/ou-pingping/FreeLLMAPI**; clones can vary. Screenshot only supplies name/claim and does **not** establish a specific owner.
- Project site: **https://freellmapi.co/** (publisher claims; inspect before providing credentials).
- Technical intent: put multiple **user-supplied provider credentials** behind a server-side **OpenAI-compatible `/v1` endpoint**, routing between providers on rate limits/availability and reporting usage; includes custom compatible local server endpoints.
- README at capture advertises 34 free providers, 474 model families, 635 model/provider endpoints and ~7.4B theoretical aggregated monthly token allowances, plus a paid faster-updated catalog feed. This figure is a **catalog maximum/marketing sum**, not a promised free allowance for an individual account.

## Critical caveats

- **“Free tiers” require your own eligible accounts, keys and limits** at each provider; usage, eligibility and rate limits vary, may prohibit multiplexing or automated account cycling, and can change without notice.
- One endpoint and “keys encrypted” do **not** prove secure deployment; verify key encryption key management, credential leaks, logs, authZ, network binding, rotation, tenant isolation and provider outbound destinations.
- Not necessarily entirely offline: remote providers receive the prompts/data sent to them; local-model-only operation is a different configuration with compute needs.
- Smart routing can change models unexpectedly, altering quality/latency, licensing, context windows, safety behavior and structured output. Pin model when reproducibility matters.
- Commercial access/paid fast catalog is distinct from the free router. No guaranteed token count or subscription value.
- Treat one-click “agent config setup” tools as write access to credentials/local config; inspect scripts and back up before running.

## Appropriate uses

A testing proxy for nonsecret prompts, fallback experimentation and explicit cost/performance comparison across personally authorized API accounts. For sensitive documents/patient/customer data, enforce data routing policy and provider contracts before sending any content.

**Status:** project existence and public README researched; no accounts, API keys, model providers, billing details or remote endpoint connected; no inference run. Related [50 — LLM APIs](50-PROGRAMMING-SYSTEM-DESIGN-GUIDES-FREE-LLM-APIS.md) and [84 — URL Security](84-URL-PROTECTION-VIBE-CODED-APP-SECURITY.md).
