---
title: "Ollama vs vLLM vs llama.cpp vs Strata: Choosing a Local Inference Backend in 2026"
date: 2026-10-21
lastmod: 2026-10-21
toc: true
draft: false
description: "Compare Ollama, vLLM, llama.cpp, and Strata as the inference backend behind an OpenAI-compatible broker. Load lifecycle, health checks, multi-GPU, and a decision table for 2026."
genre: ["Local AI", "Self-Hosted AI", "Developer Tools", "AI Infrastructure"]
tags: ["ollama vs vllm", "llama.cpp vs ollama", "vllm vs llama.cpp", "strata inference engine", "local inference backend", "openai compatible backend", "ai broker backend", "self hosted llm", "local llm runtime", "model load lifecycle", "keep_alive ollama", "tensor parallel vllm", "tensor split llama.cpp", "n-gpu-layers", "gguf quantization", "awq gptq fp8", "kv cache quantization", "llama-server health", "non loading health check", "api ps ollama", "backend agnostic broker", "sticky routing", "idle timeout unload", "multi gpu inference", "mixture of experts offload", "qwen3.8", "16gb vram", "local coding agent", "hermes agent", "brokerized agentic workflow"]
cover: "/img/cover/ollama-vllm-llamacpp-strata-backend-comparison-2026.webp"
coverAlt: "An illustration comparing four local inference backends feeding one OpenAI-compatible broker on a dark background."
coverCaption: ""
---

**The backend is the runtime loading your model weights and answering tokens.** In a brokerized setup your agents never talk to it straight. They reach an OpenAI-compatible broker, and the broker forwards each request to one of several backends on a GPU host. This page compares the four backends worth running there in 2026: **Ollama**, **vLLM**, **llama.cpp**, and **Strata**.

**The question answered here is narrow.** Not "which runtime is best" in the abstract, but "which runtime goes behind my broker for a given GPU and workload." Evaluation date is October 21, 2026, against runtime documentation verified on October 20, 2026. Hardware sizing lives in separate guides, linked below. This article stays on the backend layer.

## Key Takeaways

- **Ollama is the only backend the broker never spawns.** It lazy-loads per request and unloads on `keep_alive`, and it is the only one with a true non-loading residency view.
- **vLLM serves the widest OpenAI surface and the highest concurrent throughput**, at the cost of a slow process-start load and tensor-parallel setup.
- **llama.cpp gives the most GGUF flexibility on constrained hardware**, with per-layer GPU offload, fractional splits, and KV-cache quantization.
- **Strata targets a mixture-of-experts model far larger than the GPU**, keeping hot experts on the card and the rest in system RAM.
- **The broker, not the backend, usually owns the process lifecycle** for vLLM, llama.cpp, and Strata, so idle freeing means the broker stops the process.

**Prerequisites:** A GPU host, a working OpenAI-compatible broker in front of it, and familiarity with running one local model. Read the hardware guides first if you have not sized VRAM for your target model.

**Time and difficulty:** Intermediate. Reading and picking a backend takes about fifteen minutes. Installing and tuning the chosen runtime takes longer and depends on model size.

## Where the Backend Sits

This article is part of the series **Hermes Agent plus Local AI: a brokerized agentic workflow**. The layering runs in one direction:

- **Agents** send OpenAI-style chat requests.
- **A private Tailscale edge** carries those requests inside your tailnet. The public-edge pattern is out of scope here.
- **An OpenAI-compatible broker** authenticates, routes by model name, and manages backend processes.
- **Backends** load weights and generate tokens. This article covers the backends.

The broker exposes one endpoint and one model namespace. Behind it, each backend behaves differently when asked to load, unload, report health, split across GPUs, and serve the OpenAI surface. Those differences decide which runtime you pin to which model.

______

## The Four Backends at a Glance

**Pick the backend by model format and lifecycle needs, not by brand loyalty.** Each one is OpenAI-compatible on the broker path, so the agent sees the same API regardless of which runs underneath.

| Backend | Role behind the broker |
|---|---|
| **Ollama** | Zero broker process management, native lazy load and idle unload, GGUF model store |
| **vLLM** | Maximum concurrent throughput and the widest OpenAI surface on one model |
| **llama.cpp** | GGUF flexibility on constrained or mixed hardware, fine-grained GPU offload |
| **Strata** | A mixture-of-experts model far larger than the GPU, with system RAM offload |

*For most single-user agent setups on one consumer GPU, Ollama or llama.cpp is the starting point. Reach for vLLM when concurrency matters and for Strata when the model is far larger than the card.*

## How the Broker Drives Each Backend

**Load lifecycle is the first real difference.** Ollama manages its own model residency. The other three load one model at process start, so a broker brings them up on the first request and takes them down when idle.

| Backend | Model load and lifecycle |
|---|---|
| **Ollama** | Native lazy load on first request. The broker never spawns it. Unload runs on `keep_alive` |
| **vLLM** | Loads one model at process start. The broker starts the process on first request, stops it when idle |
| **llama.cpp** | Loads one GGUF at process start. The broker starts and stops the `llama-server` process |
| **Strata** | Process-start load. The broker manages the start and stop. Native idle behavior is not documented |

Ollama's lazy load follows the [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md), where `keep_alive` defaults to `5m` and a value of `0` unloads the model at once. The broker drives this natively rather than killing a process. For vLLM, llama.cpp, and Strata, "idle unload" means the broker stops the child process on its idle sweep, freeing the VRAM the process held.

**One caveat on vLLM idle behavior.** vLLM exposes native sleep-mode endpoints to free and reload engine memory without a full restart. A broker stopping the process does not use those endpoints. Scope any "idle frees VRAM" claim for vLLM to the process-stop behavior unless your broker drives sleep mode.

______

## Non-Loading Health Checks

**A health probe should tell you a model is alive without forcing a cold load.** Only Ollama offers a probe decoupled from loading. The broker-managed runtimes are checked for liveness while their process runs, and an unloaded backend reports as not loaded rather than being spawned to answer a ping.

| Backend | Liveness probe without a model load |
|---|---|
| **Ollama** | `GET /api/tags` lists models without loading. Residency shows through `GET /api/ps` |
| **vLLM** | `GET /health` while the process runs. Unloaded shows as not loaded, with no spawn |
| **llama.cpp** | `GET /health` returns 503 during load and 200 when ready. Checked only while running |
| **Strata** | A default health route answers 200 while the broker-owned process runs |

Ollama's `GET /api/ps` is the standout. It reports what is resident in VRAM and RAM right now, a view the other three do not provide without loading.

**Treat llama.cpp `/health` as a readiness gate, not a pure liveness ping.** Its [server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) documents a 503 response reporting "Loading model" during weight load and a 200 response reporting `{"status":"ok"}` once ready. Account for the 503 window when you tune readiness timeouts.

A minimal probe pair looks like this. Both commands are untested and illustrative, and host and port are placeholders per the redaction rule.

```bash
curl http://<backend-host>:<port>/api/tags
```

```bash
curl http://<backend-host>:<port>/health
```

Documented llama.cpp `/health` behavior, from the server README checked on October 20, 2026, not captured output:

```text
Loading:  HTTP 503, body reports "Loading model"
Ready:    HTTP 200, body reports {"status":"ok"}
```

## Multi-GPU Control

**Each backend splits a model across cards with a different knob.** llama.cpp uses fractional splits, vLLM uses an integer parallel degree, Ollama sets placement on the daemon, and Strata keeps the split deployment-specific.

| Backend | Multi-GPU mechanism |
|---|---|
| **Ollama** | Set on the daemon with `CUDA_VISIBLE_DEVICES` and `OLLAMA_*`, not by the broker |
| **vLLM** | `--tensor-parallel-size` (integer) and `--pipeline-parallel-size`, plus `--gpu-memory-utilization` |
| **llama.cpp** | `--split-mode {layer,row,tensor}` with `--tensor-split` fractions and `--n-gpu-layers` offload |
| **Strata** | Two or three cards of the same make share a model. Exact split flags are deployment-specific |

The practical split is this. vLLM wants whole GPUs and a parallel degree, so two cards means `--tensor-parallel-size 2`. llama.cpp accepts fractions through `--tensor-split` and offloads a chosen number of layers with `--n-gpu-layers`, which suits uneven cards or a card-plus-CPU mix. Strata's public documentation states two or three cards of one make share a model and does not publish a broker-style split flag, so treat its multi-GPU mapping as deployment-specific rather than a confirmed CLI.

______

## OpenAI-Compatible Surface

**All four serve `POST /v1/chat/completions` through the broker**, streaming and non-streaming, with the upstream model pinned to the runtime's model id. Past this shared floor, the surfaces diverge.

| Backend | Endpoints exposed |
|---|---|
| **Ollama** | `/v1/chat/completions` OpenAI-compatible, plus native `/api/*`. Chat and streaming |
| **vLLM** | Widest: `/v1/completions`, `/v1/chat/completions`, `/v1/responses`, `/v1/embeddings`, `/v1/models`, Anthropic `/v1/messages` |
| **llama.cpp** | OpenAI chat, completions, and embeddings, Anthropic `/v1/messages`, a rerank route, and schema-constrained JSON |
| **Strata** | `/v1` OpenAI-compatible, Anthropic `/v1/messages`, and OpenAI Responses `/v1/responses` |

**One vLLM detail affects routing.** vLLM ignores the OpenAI `user` field, as noted in the [vLLM online serving reference](https://docs.vllm.ai/en/latest/serving/online_serving/). If you rely on sticky session routing, drive it with the broker's own session header rather than the `user` value, since vLLM will not honor `user`.

**llama.cpp adds schema-constrained output.** Its server supports GBNF grammar constraints, so you force valid JSON structure at the backend. Note the native `/completion` route is not OpenAI-compatible. Use `/v1/completions` for OpenAI clients.

## Quantization and Weights Format

**Model format decides which backend you even consider.** Three of the four live in the GGUF world. vLLM is the exception.

| Backend | Quantization and weights format |
|---|---|
| **Ollama** | GGUF model store, quant chosen by `model:tag` such as `q4_0` or `q8_0` |
| **vLLM** | Hugging Face format weights, FP16 and BF16 plus AWQ, GPTQ, and FP8, version-dependent |
| **llama.cpp** | GGUF, F16 and quantized, with selectable KV-cache quant through `--cache-type-k` and `--cache-type-v` |
| **Strata** | GGUF, built on llama.cpp and ggml, shipping IQ3_S, Q2_0, and IQ2_XS variants |

*vLLM quantization support is version-dependent. Pin any AWQ, GPTQ, or FP8 claim to your installed vLLM version rather than assuming a fixed matrix.*

## VRAM Reality Before You Commit

**Weight-file size is a floor, not a budget.** A GGUF file size in decimal GB tells you the weights, not the running memory. Add the KV cache, which grows with context length, plus runtime buffers.

For a sense of scale on a 27B-class model, published GGUF file tables show a Qwen3.8 27B Q4_K_M weight at **17.44 GB** and an ISTA-DASLab GSQ-RCO IQ3_S weight at **11.8 GB**. A 16 GiB card holds about 17.18 billion bytes, so the Q4_K_M weights leave no room before the KV cache, while IQ3_S does. These are weight sizes only, and they do not include runtime memory.

Do not re-derive full budgets here. The hardware guides already do the arithmetic:

- [Is 16GB of VRAM Enough for a Local LLM?](/articles/is-16gb-vram-enough-local-llm/) for the 16 GiB case.
- [Local AI Model, GPU, and Context Guide](/articles/local-ai-model-gpu-context-guide/) for matching model size to card and context.
- [Local AI Secure Server Course](/local-ai-secure-server-course-start/) for the end-to-end build.

## Strata and the Oversized Model Case

**Strata exists for one job: run a model far larger than the GPU.** The [Strata project](https://github.com/Niko1221/Strata) runs Qwen3.8-Flash-Next, a 125-billion-parameter mixture-of-experts model, on a gaming PC by keeping frequently used experts on the card and the full expert set in system RAM. The project is MIT-licensed and built on llama.cpp and ggml.

A published third-party run illustrates the memory split. On an RTX 4060 Ti with 16GB VRAM and 64GB RAM, the reported configuration loaded 46.84 GiB of expert weights and kept 4,431 experts resident at 8.45 GiB of GPU memory, using IQ3_S at 65,536 context. Those figures describe one reported run on a mixture-of-experts model. Do not generalize them to a dense 7B or 27B model. The [Strata and OpenCode local coding article](/articles/strata-opencode-local-coding-agent-16gb/) covers this configuration in full.

**Treat Strata's lifecycle specifics as broker-managed.** Its public documentation describes the app on localhost and the OpenAI, Anthropic, and Responses surfaces, but it does not publish a broker-style health path, an idle-shutdown mechanism, or exact multi-GPU flags. Let the broker own the start and stop, and verify any native idle or split behavior against your installed version.

______

## Which Backend Behind Your Broker

**Match the backend to the model format, the GPU, and the concurrency you expect.** The rules below map directly to the differences above.

- **Choose Ollama when you want zero broker process management and native idle unload.** It is the only backend the broker does not spawn. It lazy-loads per request, unloads on `keep_alive`, and gives a true non-loading residency view through `/api/ps`.
- **Choose vLLM when you need concurrent throughput and the widest OpenAI surface on one model.** Expect a slow first request while it loads at startup, size readiness timeouts generously, and drive sticky routing with the broker session header since vLLM ignores `user`.
- **Choose llama.cpp when you want GGUF flexibility on constrained or mixed hardware.** Per-layer offload, fractional GPU splits, KV-cache quantization, GBNF-constrained JSON, and both OpenAI and Anthropic surfaces. Remember the 503 window on `/health` during load.
- **Choose Strata when the goal is a mixture-of-experts model far larger than the GPU.** It keeps hot experts on the card and the rest in RAM. Let the broker manage the process and treat idle, health, and split details as deployment-specific.

| If you want | Start with |
|---|---|
| **No process babysitting and native unload** | Ollama |
| **High concurrency and the widest API surface** | vLLM |
| **Fine-grained offload on a small or mixed GPU** | llama.cpp |
| **A 100B-plus MoE model on one consumer card** | Strata |

## Put Any of Them Behind a Pool

**When one public model name needs capacity or failover, group several backends into a broker pool.** Sticky routing keeps a conversation warm on one pool member for KV locality, and failover retries another member on error before the first byte of a stream. Failover never silently switches to a different model. A vanished member is marked failed by the non-loading health check rather than spawned to answer.

This is where the broker earns its place. The agent keeps one endpoint and one model name while the backend layer scales, drains, and recovers underneath.

## Next Steps

- Read [One Endpoint for Every Model: Building an OpenAI-Compatible AI Broker](/articles/openai-compatible-ai-broker-one-endpoint-2026/) for the layer routing to these backends.
- Read [Auto-Routing Local and Cloud AI in One Mix](/articles/ai-auto-router-local-cloud-mix-2026/) for mixing local backends with hosted models.
- Read the series master, [Hermes Agent plus Local AI: A Brokerized Agentic Workflow](/articles/hermes-agent-local-ai-brokerized-workflow-2026/), for the full stack.
- Size your hardware with the [Local AI Model, GPU, and Context Guide](/articles/local-ai-model-gpu-context-guide/) before committing to a model.
