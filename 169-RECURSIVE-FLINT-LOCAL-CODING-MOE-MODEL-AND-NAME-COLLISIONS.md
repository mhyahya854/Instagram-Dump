# 169 — Recursive Flint: local 40B MoE coding model, hardware fit, real uses and namesakes

**Typed source, 2026-10-27:** “an ai model called flint”. No original screenshot or URL was supplied. The strongest context match is **Recursive Flint**, though the bare name remains ambiguous. **Primary:** https://recursive.com/updates/introducing-recursive-flint ; **weights/model card:** https://huggingface.co/RecursiveSI/flint ; **Transformers model architecture:** https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/flint.md ; **third-party runtime integration:** https://vllm-project.github.io/2026/10/21/flint.html . Researched 2026-10-27; weights were **not downloaded, loaded or benchmarked**.

## Source statement versus verified primary claims

Recursive describes Flint as a **39.8B/approximately 40B total-parameter**, **2.5B active-parameter per-token** Mixture-of-Experts language model for local agentic coding. It is not Google's Elephant-Goldfish Model (a skill methodology), nor Microsoft's Flint (a visualization language), nor a product that guarantees 40B weights will fit into 4 GB RAM.

### Architecture and practical implications

- Decoder-only transformer with **49 layers**, using mixed attention: **35 sliding-window** layers see a roughly **513-token window**, while **14 full-attention** layers can attend over wider context. Thus long-context KV memory can be lower than uniform full attention, but it is not zero. vLLM described approximately **28 KiB of KV cache per token** for its documented implementation. Actual allocations depend on precision, context and batching.
- MoE routing uses 256 experts, top-6 sigmoid selection plus shared expert in sparse layers; the first two layers are dense. Active parameters per token reduce math relative to a similarly sized dense model but **all model weights still need storage**.
- A BF16 copy of 39.8B parameters is roughly **79.6 billion bytes of raw weights before runtime overhead**. Quantized NVFP4 / GGUF variants can reduce device memory; GPU/CPU RAM fit depends on runtime, format, cache, batch and memory mapping. SSD streaming alone doesn't guarantee interactive speed.
- Recursive advertises a 512k-token context window but recommends using at most 256k for the best results. Higher context dramatically affects cache and throughput.
- The model accepts and emits text, uses reasoning and tool calls and supports coding tasks: understanding a repository, proposing patches, writing tests, explaining errors and triaging bugs.

**Claimed benchmarks:** the publisher's model card reports Terminal-Bench 2.1 **54.9%**, SWE-bench Pro v2 **89.7%**, SWE-bench Verified **74.2%** under stated evaluation settings; benchmark tasks, harness, pass@1 definition, internet access and sample versions matter. Those are **publisher-reported results**, not independent user benchmarks. The upstream also claims >125 tokens/s on an M4 Pro MacBook and >150 tokens/s on certain NVIDIA 64 GB hardware under short-context conditions. Do not extrapolate to all laptops, workloads, prompts or context lengths.

### Integration and operational research (do not execute merely for archiving)

- Official checkpoint: https://huggingface.co/RecursiveSI/flint (BF16 architecture/tokenizer/config/chat template). Quantized versions are listed separately. Check **exact model license** and each distribution's terms; the publisher describes weights as Apache-2.0.
- The model's release cites **llama.cpp, Ollama, LM Studio, vLLM, SGLang, Unsloth** plus the publisher's \`rec\` engine. Runtime support is version-specific. The Transformers usage examples require suitable GPU resources; do not paste an unconstrained default deployment command into a production service.
- To compare locally, pin model file SHA, tokenizer, quantization format, runtime build/commit, CPU/GPU/NPU, driver, OS, storage, batch and attention settings, and turn off unnecessary cloud telemetry when testing offline privacy claims.
- Record **TTFT**, prompt prefill throughput, decode tokens/s, p50/p95 per task, peak RAM+VRAM, KV size, disk bytes read, energy, correctness/acceptance tests, security, and cost. Compare against a resident small coding model and cloud baseline where permitted.

### Fit and limits

**Good fit:** on-device software engineering, private code review under your own threat model, experiment with agent tool loops and coding tests. **Poor fit:** 4 GB hardware; guaranteed high-quality long-context reasoning; fast on all laptops; safe unsupervised shell execution; visual image generation. A local model is only private if the entire serving and toolchain is configured to avoid unauthorized network egress. Sandbox code and tools; never assume model output is executable instructions.

## Distinct products called Flint — preserve names, don't conflate

| Project | Verified public source | What it is |
|---|---|---|
| **Recursive Flint** | https://recursive.com/updates/introducing-recursive-flint | Actual MoE **language model** for coding; strongest match to user wording |
| **Microsoft Flint** | https://github.com/microsoft/flint-chart | Semantic chart-spec compiler with multiple rendering backends, not an LLM |
| **Flint Agent** | https://github.com/dklymentiev/flint-agent | CLI **coding agent application** using selectable third-party models, not model weights |
| **Flint LLM** | https://flint-llm.github.io/flint/ | CLI serving/deployment workflow for models on laptop/Kubernetes |
| **FLINT late-interaction retriever** | https://github.com/hmk55555/FLINT | Different research retrieval model; not a general-purpose coding LLM |
| **Flint / Foundry Local UI** | https://github.com/joelst/flint | Local model manager/chat desktop app built around Foundry Local |

### Source uncertainty

User gave no screenshot or specific Flint link. **Recursive Flint is a researched likely match, not a confirmed attribution.** Record other candidates until a source distinguishes them. Check [131 — Edge0](131-EDGE0-SSD-STREAMED-MOE-LOCAL-LLM-FACT-CHECK.md), [159 — GGUF](159-LOCAL-IMAGEMAGICK-GGUF-LLM-APPS-PRIVACY.md), [171 — later Edge0 evaluation lead](171-EDGE0-GGUF-LOCAL-INFERENCE-CLAIM-TEST-PROTOCOL.md) only if that later numbered file exists; **do not assume an uncommitted filename exists**. This note is documentation only.
