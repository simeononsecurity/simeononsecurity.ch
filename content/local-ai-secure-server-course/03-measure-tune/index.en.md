---
title: "Lesson 3: Measure and Tune Local AI Inference"
date: 2026-10-10
lastmod: 2026-10-11
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

The [Ollama context documentation](https://docs.ollama.com/context-length) explains how context length changes memory use. The [generate API](https://docs.ollama.com/api/generate) accepts **`num_ctx`** in the request options.

Test two context settings on synthetic input. Keep concurrency at one. Record peak memory and whether the model stays fully on the GPU, splits across CPU and GPU, or runs in system memory.

Use modest values which fit your host. A failed larger setting is a useful capacity result.

### Run Two Exact Contexts

Use the same `MODEL_NAME` value selected in Lesson 1. Replace the placeholder before starting both trials:

```bash
MODEL_NAME="replace-with-your-model"
test "$MODEL_NAME" != "replace-with-your-model" || { echo "Set MODEL_NAME first"; exit 1; }
```

Run the **2,048-token context** trial:

```bash
curl --fail --silent --show-error http://127.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d @- <<JSON | tee context-2048.json
{
    "model": "$MODEL_NAME",
    "prompt": "Explain a three-step backup restore test in 120 words or fewer.",
    "stream": false,
    "think": false,
    "keep_alive": "10m",
    "options": {
      "num_ctx": 2048,
      "num_predict": 120,
      "temperature": 0,
      "seed": 42
    }
}
JSON
ollama ps
```

Run the **4,096-token context** trial with the same model and prompt:

```bash
curl --fail --silent --show-error http://127.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d @- <<JSON | tee context-4096.json
{
    "model": "$MODEL_NAME",
    "prompt": "Explain a three-step backup restore test in 120 words or fewer.",
    "stream": false,
    "think": false,
    "keep_alive": "10m",
    "options": {
      "num_ctx": 4096,
      "num_predict": 120,
      "temperature": 0,
      "seed": 42
    }
}
JSON
ollama ps
```

> **Expected Result:** Each JSON file ends with **`"done":true`** and includes timing and token counts. The **`CONTEXT`** column from **`ollama ps`** reports the allocated context. The 4,096-token trial usually uses at least as much memory as the 2,048-token trial. Record the observed values instead of assuming a fixed increase.

### Sample Peak RAM

Run this sampler in a second terminal on **Linux, macOS, or the course WSL 2 distribution**. Start the sampler before each API trial. Press **Ctrl+C** after the response finishes.

```bash
: > ollama-rss-kib.log
while true; do
  ps -axo rss=,comm= |
    awk '$2 ~ /ollama/ { sum += $1 } END { print sum + 0 }' \
    >> ollama-rss-kib.log
  sleep 1
done
```

Print the highest sampled resident-set size:

```bash
awk 'BEGIN { max = 0 } $1 > max { max = $1 } END { printf "Peak sampled Ollama RSS: %.2f GiB\n", max / 1048576 }' ollama-rss-kib.log
```

This value is a **one-second sampled peak**, not an exact allocator total. On WSL, run both Ollama and the sampler inside the same distribution. Use **`free -h`** to record total memory, available memory, and swap for the Linux or WSL environment.

On macOS with Apple silicon, CPU and GPU work share system memory. Record the sampled Ollama RSS and check [**Memory Pressure** and **Swap Used** in Activity Monitor](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac). Do not report a separate VRAM value when the host has no dedicated VRAM pool.

### Sample NVIDIA VRAM

On a Linux or WSL host with an NVIDIA GPU, use the [NVIDIA System Management Interface](https://docs.nvidia.com/deploy/nvidia-smi/index.html). Start this command before each trial. Press **Ctrl+C** after the response finishes.

```bash
: > gpu-memory-mib.log
nvidia-smi \
  --query-gpu=memory.used \
  --format=csv,noheader,nounits \
  --loop=1 | tee gpu-memory-mib.log
```

Print the highest sampled device-memory use:

```bash
awk 'BEGIN { max = 0 } $1 > max { max = $1 } END { printf "Peak sampled GPU memory: %d MiB\n", max }' gpu-memory-mib.log
```

Record the idle baseline before loading the model. Other GPU processes also contribute to **`memory.used`**. Use **`ollama ps`** to record whether Ollama reports CPU, GPU, or split placement.

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
- **The API returns connection refused:** Start Ollama in the same Linux, macOS, or WSL environment, then retry the loopback URL.
- **The response rejects `think`:** Update Ollama or remove only the **`"think": false`** line. Keep every other test setting fixed and record the change.
- **`ollama ps` shows the wrong context:** Wait for the request to finish, run **`ollama ps`** again, and confirm the model identifier matches the request.
- **The RAM log contains zeros:** Run **`pgrep -af ollama`**. Start the Ollama service if no matching process appears.
- **`nvidia-smi` is missing in WSL:** Confirm [WSL GPU support](https://learn.microsoft.com/windows/wsl/tutorials/gpu-compute) and the Windows NVIDIA driver. Keep the RAM result and mark VRAM as unverified until **`nvidia-smi`** works inside the distribution.
- **Context increase triggers failure:** Return to the last passing value and record the boundary.
- **GPU diagnostics show no offload:** Verify runtime build, driver, backend support, and available VRAM.
- **Parallel tests vary widely:** Check queue delay, thermal limits, competing workloads, and model reloads.

## Verify Completion

Pass when the record gives another person enough detail to repeat your test. The record must include commands, exact prompt, model identity, runtime version, host state, three runs, and the chosen configuration.

Continue with [Lesson 4: Design a Secure Local AI Server](/local-ai-secure-server-course/04-secure-server/).
