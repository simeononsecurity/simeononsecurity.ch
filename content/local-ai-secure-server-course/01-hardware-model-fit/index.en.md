---
title: "Lesson 1: Choose Hardware and a Local AI Model"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Match a local model, quantization, context target, license, and runtime to your hardware."
genre: ["Artificial Intelligence", "Hardware", "Self-Hosted"]
tags: ["local LLM hardware", "VRAM model sizing", "GGUF quantization", "local AI model selection", "AI model license"]
cover: "/img/cover/local-ai-hardware-model-fit.webp"
coverAlt: "Hardware inventory matched to model weights, context memory, and workload requirements"
coverCaption: "Lesson cover placeholder. Image generation follows editorial review."
---

[Return to the Local AI Course](/local-ai-secure-server-course/)

**Choose from your workload and memory limit.** A model name alone does not describe license, quantization, context cost, or runtime support.

## Define the Workload

Write one target task before downloading a model:

```text
Task: Summarize a synthetic support note into five bullets.
Input: Up to 2,000 tokens.
Output: Up to 300 tokens.
Users: One.
Latency target: First useful response within 15 seconds.
Data rule: Local synthetic data only.
```

This statement gives you a context target and workload shape. It also prevents a later benchmark from changing the task to favor one model.

## Inventory the Host

Record these values in **`local-ai-course-record.md`**:

| Resource | Record | Why it matters |
|---|---|---|
| **System memory** | Total and available | CPU inference and overflow use RAM |
| **GPU memory** | Total and free | Weight and context placement depend on VRAM |
| **Storage** | Free space and filesystem | Models use several gigabytes each |
| **CPU** | Architecture and instruction support | CPU speed varies by build and instruction set |
| **GPU** | Vendor, model, driver | Runtime support differs across CUDA, ROCm, Metal, Vulkan, and CPU |
| **Network** | Local interfaces and trust zone | Server exposure changes risk |

Leave operating headroom. Do not plan model weights against all available memory. Context state, runtime buffers, parallel requests, and the operating system need space.

## Read the Model Record

For each candidate, record:

1. **Publisher and source repository**
2. **Model card and intended use**
3. **License and use restrictions**
4. **Parameter count and architecture**
5. **Quantization or precision**
6. **File size and digest when available**
7. **Supported context length**
8. **Runtime chat template requirements**

Quantization reduces weight storage at a quality cost which varies by model, task, and format. Treat file size as one part of memory use. Test the chosen build on your workload.

## Estimate Fit

Use this planning formula:

```text
required memory = model weights + context state + runtime buffers + concurrency margin + operating margin
```

Do not claim a universal bytes-per-token value. Context memory depends on architecture, cache format, layer count, runtime, and settings.

**Beginner path:** Select a small model from the Ollama library with a download size comfortably below available memory.

**Advanced path:** Compare two quantizations or two model sizes. Keep prompt, output limit, context, runtime version, and host state fixed.

## Verify Provenance

Save the exact model identifier and runtime inspection output. With Ollama:

```bash
ollama show MODEL_NAME
ollama ls
```

With a downloaded GGUF file:

```bash
shasum -a 256 model.gguf
```

Use `sha256sum` on systems where `shasum` is absent. Compare the digest with a trusted publisher record when one exists. A digest proves file identity against the reference. It does not prove the model is safe or accurate.

## Expected Result

Your record names one model, source, license, format, file size, context target, runtime, and memory margin. The selection ties to the target task rather than a leaderboard rank.

## Troubleshooting

- **VRAM appears lower than the product label:** Check current processes and reserved display memory.
- **The model card lacks a clear license:** Do not use the model for a deployment until ownership and terms are resolved.
- **The runtime rejects the model:** Check format, architecture support, chat template, and runtime version.
- **The model fits at short context but fails later:** Lower context or concurrency and remeasure peak memory.

## Verify Completion

Pass when your record answers these questions:

1. Which exact model artifact will run?
2. Which license governs use?
3. How much memory stays free at the planned context?
4. Which command proves the local artifact identity?
5. Which synthetic prompt measures task quality?

Continue with [Lesson 2: Run Your First Local Model](/local-ai-secure-server-course/02-first-local-model/).
