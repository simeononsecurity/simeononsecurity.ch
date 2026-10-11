---
title: "Lesson 3: Measure and Tune Local AI Inference"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Measure prompt and generation speed, memory use, context cost, and concurrency with repeatable local tests."
genre: ["Artificial Intelligence", "Performance", "Self-Hosted"]
tags: ["local LLM benchmark", "Ollama performance", "llama.cpp benchmark", "tokens per second", "context memory", "GPU offload"]
cover: "/img/cover/local-ai-inference-measure-tune.webp"
coverAlt: "Local AI performance worksheet comparing prompt speed, generation speed, memory, and context"
coverCaption: ""
---

[Return to the Local AI Course](/local-ai-secure-server-course-start/)

**Measure prompt processing and token generation separately.** A single elapsed time hides model loading, prompt evaluation, generation, and queue delay.

## Freeze the Test Conditions

Record:

- **Host state:** Active applications and free RAM or VRAM
- **Runtime:** Version and configuration
- **Model:** Exact identifier or file digest
- **Prompt:** Exact text and actual input token count from runtime output
- **Context:** Configured maximum
- **Output:** Fixed generation limit when supported
- **Temperature and seed:** Fixed when the runtime exposes them
- **Warm state:** Cold first run or already loaded model
- **Concurrency:** Number of simultaneous requests

Use the same conditions for every comparison. A faster result from a shorter prompt does not establish a faster model.

## Run a Beginner Measurement

Ollama's verbose CLI reports timing details:

```bash
MODEL_NAME='replace-with-your-model'
ollama run --verbose "$MODEL_NAME" 'Explain a three-step backup restore test in 120 words or fewer.'
```

Record prompt evaluation count and rate, evaluation count and rate, total duration, and processor placement from:

```bash
ollama ps
```

Run three warm trials. Report each trial and the median. Do not discard a slow run without a recorded cause.

## Test Context Growth

The [Ollama FAQ](https://docs.ollama.com/faq) documents `OLLAMA_CONTEXT_LENGTH` for server defaults and `num_ctx` for API requests. Larger context needs more memory.

Test two context settings on synthetic input. Keep concurrency at one. Record peak memory and whether the model stays fully on the GPU, splits across CPU and GPU, or runs in system memory.

Use modest values which fit your host. A failed larger setting is a useful capacity result.

## Advanced llama.cpp Profile

The official [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) describes the current server flags and API. A representative local command is:

```bash
./build/bin/llama-server \
  -m /path/to/model.gguf \
  -c 4096 \
  --host 127.0.0.1 \
  --port 8080 \
  -ngl auto \
  --np 1
```

Confirm the startup log reports the expected backend and layer placement. `-ngl auto` requests automatic offload. Runtime diagnostics establish what occurred.

Increase one variable at a time:

1. Context size
2. GPU layer placement
3. Parallel slots
4. Batch settings

After each change, repeat the same prompt and memory checks.

## Build the Results Table

| Trial | Context | Parallel requests | Prompt tokens | Prompt tok/s | Generated tokens | Generation tok/s | Peak memory | Placement |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Warm 1** | 4096 | 1 | Observed | Observed | Observed | Observed | Observed | Observed |
| **Warm 2** | 4096 | 1 | Observed | Observed | Observed | Observed | Observed | Observed |
| **Warm 3** | 4096 | 1 | Observed | Observed | Observed | Observed | Observed | Observed |

Label values copied from documentation as examples. Only runtime output belongs in observed columns.

## Choose the Operating Point

Select the smallest context which supports the workload. Reserve enough memory for runtime variation and the operating system. Add concurrency only after one-request behavior passes.

For a shared server, include queue latency and overload behavior. The Ollama FAQ documents queue and parallelism settings and explains how parallel requests increase allocated context.

## Expected Result

Your record contains three comparable warm trials, separate prompt and generation rates, memory placement, and one selected operating point with a stated margin.

## Troubleshooting

- **Rates exceed plausible elapsed time:** Recheck units, token counts, and whether prompt and generation phases were mixed.
- **First run is much slower:** Label model loading and cold-cache effects.
- **Context increase triggers failure:** Return to the last passing value and record the boundary.
- **GPU diagnostics show no offload:** Verify runtime build, driver, backend support, and available VRAM.
- **Parallel tests vary widely:** Check queue delay, thermal limits, competing workloads, and model reloads.

## Verify Completion

Pass when the record gives another person enough detail to repeat your test. The record must include commands, exact prompt, model identity, runtime version, host state, three runs, and the chosen configuration.

Continue with [Lesson 4: Design a Secure Local AI Server](/local-ai-secure-server-course/04-secure-server/).
