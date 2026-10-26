# 131 — Edge0: Large MoE Models Using SSD-Streamed Expert Weights

**Source:** screenshot 1 of sixteenth Instagram batch (2026-10-26), from `notmy.bug`; a Reel caption in Hindi/Hinglish describes running **35 billion parameter AI on 4GB RAM** via `Edge0`. Claims shown: no large GPU/cloud fees, SSD-streamed weights instead of full RAM load, offline AI agents, privacy, fast SSD, “FREE”. A separate comment jokingly says “1 token per decade”; that is not a real benchmark.

## Directly transcribed concepts

- “4GB RAM mein 35 Billion parameter AI model? 🤯 Yes, it's possible! | Day 22”
- Creator claims the **Edge0 framework** streams model weights from SSD rather than loading full weights into RAM; even low-end laptops/Macs might run local models without GPU or paid cloud calls.
- The pictured Edge0 site shows **“Unlimited Access To Advanced AI”**, **“Designed For Low-Power, Low-Memory Devices”**, **“Private By Design”** and small active memory.
- These are social/vendor claims, not benchmark results conducted in this archive.

## Verified official research

- Code: https://github.com/Edge0-AI/Edge0
- Research site: https://edge0.ai/research/edge0
- Model: https://huggingface.co/Edge0/Edge0-35b-a3b-preview
- Official README says Edge0 uses **sparse mixture-of-experts (MoE)** with **SSD expert offload**, **trained prerouter to prefetch expert weights**, **4-bit frozen base + Recover-LoRA** for quality recovery.
- As of repo announcements Sept. 30, 2026, runtime directories for **macOS, iOS, Android and Windows** are open-source, but platform readiness, release builds and unified API differ. Mac Python/MLX version is a separate backend from Windows C++/Vulkan.
- Stated tier **35B-A3B**: about **23 GB on disk** at 4-bit, and about **2.9 GiB peak MLX allocator** under short-context reported conditions. The allocator value **excludes** entire operating system, runtime, extra mapped pages and KV/cache overhead; it is **not proof an ordinary 4GB Windows machine will run the model responsively**. SSD access patterns and GPU/CPU performance limit speed.
- Lighter 8B-A1B tier: about 4.2 GB weights, around 1.0 GiB MLX allocator in described tests, with similar total-RAM caveat.

## How to evaluate on a personal Windows computer safely

1. **Research-only initially:** check hardware CPU/GPU, VRAM, RAM, free SSD capacity, SSD speed/endurance, operating system/build and model/software licenses.
2. Check `windows/README.md` and tagged releases, actual Vulkan driver requirements, 35B vs 8B support and compatibility with existing graphics problems.
3. Budget space for 23GB checkpoint **plus** any downloads, adapters, copies, caches and rollback headroom; memory and speed may remain unacceptable.
4. If **a separate explicit installation/testing task** is later authorized: use isolated directory, signed/verified artifacts, hash checks, synthetic public prompts, no admin privileges if avoidable, and measured peak **process RSS/working set**, GPU memory, disk reads, token/sec and first-token latency.
5. Avoid conflating “small resident active expert set” with *all 35B weights present in RAM*. Record temperatures, I/O pressure, failure/recovery, battery and model quality on actual prompts.
6. **No install or inference while prioritizing a laptop graphics/Windows corruption investigation.** Do not alter drivers, Windows/BIOS settings or BitLocker for this research.

## Useful concepts beyond this repo

Hierarchical weight storage (SSD ↔ RAM ↔ accelerator), sparse experts, learned predictive routing, asynchronous prefetch, memory/mmap semantics, distillation after aggressive quantization, multi-platform runtime splits and careful benchmarking.

**Status:** canonical repo and research page verified; no model downloaded, drivers changed, system scanned, API key used, benchmark performed or universal rules modified.
