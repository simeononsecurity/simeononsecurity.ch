---
title: "16GB GPU ਉੱਤੇ ਸਥਾਨਕ AI ਕੋਡਿੰਗ: Strata, OpenCode ਅਤੇ Qwen3.8"
date: 2026-10-06
lastmod: 2026-11-13
toc: true
draft: false
description: "Strata ਅਤੇ OpenCode ਨਾਲ ਸਥਾਨਕ ਕੋਡਿੰਗ ਏਜੰਟ ਚਲਾਓ। RTX 4060 Ti ਦੇ ਦੱਸੇ ਨਤੀਜੇ, RAM ਦੀ ਲੋੜ, prompt ਦੀ ਮੁੜ ਵਰਤੋਂ, reasoning budgets ਅਤੇ ਭੁਗਤਾਨੀ subscription ਬਦਲਣ ਦੀਆਂ ਹੱਦਾਂ ਨੂੰ ਸਮਝੋ।"
genre: ["ਸਥਾਨਕ AI", "ਡਿਵੈਲਪਰ ਟੂਲ", "ਸਵੈ-ਹੋਸਟਡ AI", "AI ਹਾਰਡਵੇਅਰ"]
tags: ["ਸਥਾਨਕ AI ਕੋਡਿੰਗ ਏਜੰਟ", "Strata", "OpenCode", "Qwen3.8 Flash Next", "125B ਮਾਡਲ", "RTX 4060 Ti", "16GB GPU", "64GB RAM", "IQ3_S", "ਮਿਸ਼ਰਤ ਮਾਹਰ", "ਮਾਹਰ cache", "prompt caching", "prefix reuse", "reasoning budget", "ਕੋਡਿੰਗ ਸਹਾਇਕ", "ਸਥਾਨਕ inference", "AI subscriptions", "GPU offload", "Docker", "automated tests", "OpenAI compatible API", "context window", "NVMe SSD", "self hosted AI"]
cover: "/img/cover/local-ai-coding-16gb-gpu-nvidia-rtx-4060-ti.webp"
coverAlt: "ਸਥਾਨਕ AI ਕੋਡਿੰਗ ਵਾਤਾਵਰਣ ਦੀ ਤਸਵੀਰ, ਜਿਸ ਵਿੱਚ NVIDIA RTX 4060 Ti GPU ਹਨੇਰੇ ਪਿਛੋਕੜ ਉੱਤੇ ਚਮਕਦਾਰ data streams ਅਤੇ code snippets ਨਾਲ ਘਿਰਿਆ ਹੋਇਆ ਹੈ।"
coverCaption: ""
---

**16GB GPU ਉੱਤੇ ਸਥਾਨਕ ਕੋਡਿੰਗ ਏਜੰਟ ਸੀਮਿਤ development ਕੰਮਾਂ ਲਈ ਇੱਕ ਵਿਹਾਰਕ ਵਿਕਲਪ ਹੈ।** Strata ਅਤੇ OpenCode ਸਥਾਨਕ inference ਨੂੰ file editing, shell commands ਅਤੇ test execution ਨਾਲ ਜੋੜਦੇ ਹਨ। RTX 4060 Ti ਉੱਤੇ ਦੱਸੇ Qwen3.8-Flash-Next run ਨੇ ਭੁਗਤਾਨੀ inference calls ਤੋਂ ਬਿਨਾਂ application, ਬਾਅਦ ਦੀਆਂ ਤਬਦੀਲੀਆਂ ਅਤੇ racing-game prototype ਪੂਰਾ ਕੀਤਾ।

**Subscription ਬਦਲਣ ਲਈ ਵੱਡਾ test ਲੋੜੀਂਦਾ ਹੈ।** ਪ੍ਰਕਾਸ਼ਿਤ ਨਤੀਜੇ ਇੱਕ machine ਉੱਤੇ ਚੱਲਦੀ setup ਦਿਖਾਉਂਦੇ ਹਨ। ਇਹ ਵੱਖ-ਵੱਖ languages, repositories ਜਾਂ ਔਖੇ debugging ਕੰਮਾਂ ਵਿੱਚ paid coding services ਨਾਲ ਬਰਾਬਰੀ ਸਾਬਤ ਨਹੀਂ ਕਰਦੇ। Hardware ਵਿੱਚ 64GB system RAM ਵੀ ਹੈ, ਜਿਸ ਵਿੱਚ model ਦਾ ਵੱਡਾ ਹਿੱਸਾ ਰਹਿੰਦਾ ਹੈ।

## ਮੁੱਖ ਗੱਲਾਂ

- **16GB GPU memory ਦੱਸਦਾ ਹੈ**, ਦੱਸੀ configuration ਲਈ ਲੋੜੀਂਦੀ ਕੁੱਲ memory ਨਹੀਂ।
- **Prompt reuse ਮਹੱਤਵਪੂਰਨ ਹੈ**, ਕਿਉਂਕਿ coding agents ਵਾਰ-ਵਾਰ overlap ਕਰਦੀ conversation history ਭੇਜਦੇ ਹਨ।
- **Reasoning ਲਈ budget ਚਾਹੀਦਾ ਹੈ**, ਤਾਂ planning code ਅਤੇ tool calls ਲਈ ਥਾਂ ਛੱਡੇ।
- **Generated tests pass ਹੋਣਾ ਅਧੂਰਾ ਸਬੂਤ ਹੈ**, Docker ਅਤੇ gameplay ਲਈ ਵੱਖਰੀ ਜਾਂਚ ਚਾਹੀਦੀ ਹੈ।
- **Zero API spend ownership costs ਨੂੰ ਨਹੀਂ ਗਿਣਦਾ**, ਜਿਵੇਂ ਬਿਜਲੀ ਅਤੇ maintenance time।

**Prerequisites:** Compatible computer, ਚੁਣੇ model ਲਈ ਕਾਫ਼ੀ free storage, Git, npm ਸਮੇਤ Node.js ਅਤੇ terminal tools ਦੀ ਜਾਣਕਾਰੀ। ਦੱਸੀ IQ3_S setup ਲਈ 64GB RAM ਵਰਤੋ। ਹੋਰ configurations ਲਈ current Strata installer ਵੇਖੋ।

**ਸਮਾਂ ਅਤੇ ਮੁਸ਼ਕਲ:** ਦਰਮਿਆਨਾ। Task completion speed ਮਾਪਣ ਤੋਂ ਪਹਿਲਾਂ ਵੱਡੇ model downloads ਅਤੇ installation ਲਈ ਸਮਾਂ ਰੱਖੋ। ਦੱਸੇ task timings setup ਨੂੰ ਸ਼ਾਮਲ ਨਹੀਂ ਕਰਦੇ।

## ਪਰਖੀ ਗਈ ਸੰਰਚਨਾ

| ਘਟਕ | ਦੱਸੀ configuration |
|---|---|
| **GPU** | NVIDIA RTX 4060 Ti, 16GB VRAM |
| **CPU** | Intel Core i5-11600K |
| **ਸਿਸਟਮ ਮੈਮੋਰੀ** | 64GB RAM |
| **Storage** | NVMe SSD |
| **ਮਾਡਲ** | Qwen3.8-Flash-Next, 125B MoE, IQ3_S |
| **Inference engine** | Strata |
| **Coding agent** | OpenCode |
| **Configured context** | 65,536 tokens |
| **ਕੌਂਫਿਗਰ ਕੀਤੀ ਆਉਟਪੁੱਟ ਸੀਮਾ** | 16,384 tokens |

**NetworkCoder ਦੀ published configuration ਅਤੇ results** ਇਹ ਅੰਕੜੇ ਦਿੰਦੇ ਹਨ। [ਟੈਸਟ ਰਿਪੋਜ਼ਟਰੀ](https://github.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU) 46.84GiB expert weights ਨੂੰ 28 seconds ਵਿੱਚ load ਕਰਨ ਦੀ report ਕਰਦੀ ਹੈ। 4,431 experts ਨੇ GPU memory ਦੀ 8.45GiB ਵਰਤੀ। ਇਹ measurements tested run ਨੂੰ ਦੱਸਦੇ ਹਨ, ਕਿਸੇ ਹੋਰ engine version ਉੱਤੇ guaranteed allocation ਨੂੰ ਨਹੀਂ।

**ਮੌਜੂਦਾ ਅਨੁਕੂਲਤਾ ਇਸ ਟੈਸਟ ਨਾਲੋਂ ਵੱਡੀ ਹੈ।** 6 ਅਕਤੂਬਰ 2026 ਨੂੰ ਵੇਖੇ [Strata ਪ੍ਰੋਜੈਕਟ](https://github.com/Niko1221/Strata) ਵਿੱਚ ਘੱਟੋ-ਘੱਟ 12GB VRAM ਵਾਲੇ ਚੁਣੇ NVIDIA ਅਤੇ AMD ਕਾਰਡਾਂ ਅਤੇ 32GB RAM ਸਿਸਟਮਾਂ ਲਈ ਛੋਟੇ ਮਾਡਲ ਦਰਜ ਹਨ। ਇਹ ਵਿਕਲਪ 16GB GPU, 64GB RAM ਅਤੇ IQ3_S ਵਾਲੇ ਟੈਸਟ ਨੂੰ ਦੁਹਰਾਉਂਦੇ ਨਹੀਂ। Hardware ਖਰੀਦਣ ਤੋਂ ਪਹਿਲਾਂ ਸਹੀ GPU, model variant ਅਤੇ runtime support ਜਾਂਚੋ।

## Model ਕਿੱਥੇ ਰਹਿੰਦਾ ਹੈ

**Mixture of experts**, ਜਾਂ MoE, ਹਰ token ਲਈ model ਦੀਆਂ expert networks ਦਾ ਇੱਕ subset activate ਕਰਦਾ ਹੈ। ਇਸ ਨਾਲ ਹਰ step ਉੱਤੇ ਹਰ parameter ਵਰਤਣ ਦੇ ਮੁਕਾਬਲੇ active computation ਘੱਟ ਹੁੰਦੀ ਹੈ। ਬਾਕੀ weights ਨੂੰ storage ਅਤੇ computation ਤੱਕ ਰਸਤਾ ਫਿਰ ਵੀ ਚਾਹੀਦਾ ਹੈ।

**Strata ਦੀ hybrid execution** ਅਕਸਰ ਵਰਤੇ ਜਾਣ ਵਾਲੇ experts ਨੂੰ GPU ਉੱਤੇ ਰੱਖਦੀ ਹੈ ਅਤੇ expert collection ਨੂੰ system RAM ਵਿੱਚ ਰੱਖਦੀ ਹੈ। CPU uncached experts ਨੂੰ ਉੱਥੇ compute ਕਰਦਾ ਹੈ ਅਤੇ GPU cached experts ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। Storage model files ਅਤੇ lookup data ਲਈ ਵੀ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। System ਪੂਰੇ 125B model ਨੂੰ 16GB VRAM ਵਿੱਚ ਨਹੀਂ ਸਮਾਉਂਦਾ।

**GPU memory ਕਈ ਕੰਮਾਂ ਵਿੱਚ ਵੰਡੀ ਜਾਂਦੀ ਹੈ।** Runtime allocation, attention state ਅਤੇ expert cache ਸੀਮਿਤ ਸਰੋਤ ਸਾਂਝੇ ਕਰਦੇ ਹਨ। Context ਲਈ ਵੱਧ memory ਦੇਣ ਨਾਲ expert cache ਦੀ ਬਚੀ ਸਮਰੱਥਾ ਘਟਦੀ ਹੈ। Strata ਦੇ ਮੌਜੂਦਾ versions KV-cache streaming ਦਾ ਵੀ ਸਮਰਥਨ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ data placement ਪੁਰਾਣੀ configuration ਤੋਂ ਵੱਖਰੀ ਹੈ। ਆਪਣੇ engine version ਲਈ [ਤਕਨੀਕੀ ਦਸਤਾਵੇਜ਼](https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md) ਵੇਖੋ।

{{< figure src="local-agent-gpu-ram-expert-cache.webp" alt="ਸਥਾਨਕ workstation ਵੱਲੋਂ model execution ਨੂੰ graphics card, system memory ਅਤੇ solid-state storage ਵਿੱਚ ਵੰਡਣ ਦੀ ਤਸਵੀਰ" caption="GPU inference system ਦਾ ਇੱਕ ਹਿੱਸਾ ਹੈ, CPU execution, system RAM ਅਤੇ storage ਦੇ ਨਾਲ" >}}

## ਪ੍ਰੌਂਪਟ ਦੀ ਮੁੜ ਵਰਤੋਂ ਗਤੀ ਬਦਲਦੀ ਹੈ

**Coding agent ਇੱਕ loop ਚਲਾਉਂਦਾ ਹੈ:** task ਪੜ੍ਹਦਾ ਹੈ, tool action ਮੰਗਦਾ ਹੈ, result ਲੈਂਦਾ ਹੈ ਅਤੇ ਅਗਲਾ action ਚੁਣਦਾ ਹੈ। File contents, errors ਅਤੇ test output conversation ਵਿੱਚ ਇਕੱਠੇ ਹੁੰਦੇ ਹਨ। Agents context ਨੂੰ compact ਜਾਂ select ਵੀ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਹਰ implementation ਬਿਨਾਂ ਬਦਲੀ ਪੂਰੀ history ਹਮੇਸ਼ਾ ਦੁਬਾਰਾ ਨਹੀਂ ਭੇਜਦੀ।

**Prefill** generation ਤੋਂ ਪਹਿਲਾਂ input tokens process ਕਰਦਾ ਹੈ। **Decode** response ਬਣਾਉਂਦਾ ਹੈ। Fast decode ਪਰ slow repeated prefill ਵਾਲਾ system ਵੀ tool calls ਦੇ ਵਿਚਕਾਰ ਉਡੀਕ ਕਰਵਾਉਂਦਾ ਹੈ।

**ਦੱਸੇ 44K-token timing ਵਿੱਚ prefix reuse ਵਰਤੀ ਗਈ।** Strata ਨੇ ਪਹਿਲਾਂ process ਕੀਤੀ conversation content ਮੁੜ ਵਰਤੀ ਅਤੇ ਵਧਦਾ prompt ਲਗਭਗ ਇੱਕ ਤੋਂ ਤਿੰਨ seconds ਵਿੱਚ ਤਿਆਰ ਸੀ। ਇਹ continuing agent session ਲਈ ਲਾਭਦਾਇਕ evidence ਹੈ। ਇਹ 44,000 ਪੂਰੀ ਤਰ੍ਹਾਂ ਨਵੇਂ tokens ਨੂੰ scratch ਤੋਂ ਇੱਕ second ਵਿੱਚ process ਕਰਨ ਦਾ ਸਬੂਤ ਨਹੀਂ।

| Measurement | ਕੀ record ਕਰਨਾ ਹੈ |
|---|---|
| **Cold prompt** | Reusable prefix state ਤੋਂ ਬਿਨਾਂ ਨਵੀਂ content ਦਾ ਸਮਾਂ |
| **Warm continuation** | Existing context ਵਿੱਚ tool result ਜੋੜਨ ਤੋਂ ਬਾਅਦ ਦਾ ਸਮਾਂ |
| **Generation speed** | Response ਦੌਰਾਨ tokens per second |
| **ਕੰਮ ਦੀ ਮਿਆਦ** | Planning, generation, tools, tests ਅਤੇ retries ਇਕੱਠੇ |

**ਦੋ caches ਵੱਖਰੇ ਕੰਮ ਕਰਦੇ ਹਨ।** Expert cache ਅਕਸਰ ਵਰਤੇ weights ਨੂੰ GPU computation ਦੇ ਨੇੜੇ ਰੱਖਦਾ ਹੈ। Prefix reuse ਪੁਰਾਣੇ input ਉੱਤੇ ਕੰਮ ਦੁਹਰਾਉਣ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ। High expert-cache hit rate prompt-cache hit ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

## Tasks ਨੇ ਕੀ ਦਿਖਾਇਆ

| Task | ਦੱਸਿਆ ਸਮਾਂ | ਦੱਸਿਆ ਨਤੀਜਾ |
|---|---|---|
| **Build task manager** | 3m 38s | Express API, interface, 5/5 tests |
| **ਸੰਪਾਦਨ ਠੀਕ ਕਰੋ ਅਤੇ ਮਿਤੀਆਂ ਜੋੜੋ** | 4m 58s | Changes complete, 6/6 tests |
| **ਨਿਰਯਾਤ, ਆਯਾਤ ਅਤੇ ਪੈਕੇਜਿੰਗ ਜੋੜੋ** | 3m 48s | 7/7 tests, Docker build unverified |
| **Racing game, first attempt** | 6m 35s | Reasoning ਦੌਰਾਨ output ਖਤਮ, code ਨਹੀਂ |
| **Racing game, budgeted retry** | 4m 51s | Game generated, JavaScript syntax checked |

**[ਪ੍ਰਕਾਸ਼ਿਤ ਨਤੀਜਿਆਂ ਦੀ ਫਾਈਲ](https://raw.githubusercontent.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU/main/results.csv)** ਪਹਿਲੇ task ਲਈ 48–52, ਦੂਜੇ ਲਈ 40–43 ਅਤੇ ਤੀਜੇ ਲਈ 37–44 tokens per second ਦੀ ਗਤੀ ਦਰਜ ਕਰਦੀ ਹੈ। “Up to 52” ਇਨ੍ਹਾਂ ਮਾਪਾਂ ਵਿੱਚ ਸਭ ਤੋਂ ਉੱਚੀ ਗਤੀ ਹੈ, ਹਰ task ਦੀ ਲਗਾਤਾਰ ਰਹਿਣ ਵਾਲੀ ਦਰ ਨਹੀਂ।

**ਪਹਿਲੇ ਤਿੰਨ tasks ਇੱਕ application ਨੂੰ ਵਧਾਉਂਦੇ ਹਨ।** 5/5, 6/6 ਅਤੇ 7/7 counts successive test suites ਦੱਸਦੇ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਜੋੜਨਾ 18 independent capabilities ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ। ਉਸੇ agent ਵੱਲੋਂ ਲਿਖੇ tests ਨੂੰ coverage ਅਤੇ meaningful assertions ਲਈ review ਚਾਹੀਦਾ ਹੈ।

**Environmental recovery ਕੰਮ ਦਾ ਹਿੱਸਾ ਸੀ।** Agent ਨੇ inappropriate shell command ਤੋਂ recover ਕੀਤਾ ਅਤੇ testing ਦੌਰਾਨ stale application server ਪਛਾਣਿਆ। ਇਹ ਲਾਭਦਾਇਕ behaviours ਹਨ, ਪਰ existing process terminate ਕਰਨ ਲਈ shared development environment ਵਿੱਚ ਸੋਚੇ-ਸਮਝੇ permissions ਚਾਹੀਦੇ ਹਨ।

**Docker unverified ਰਿਹਾ।** Agent ਨੇ Dockerfile ਲਿਖਿਆ, ਪਰ build ਲਈ running Docker engine ਨਹੀਂ ਸੀ। Container ਤੋਂ ਬਾਹਰ application tests pass ਹੋਣ ਨਾਲ working image ਸਾਬਤ ਨਹੀਂ ਹੁੰਦੀ। Game retry ਨੇ syntax check ਕੀਤੀ ਅਤੇ browser ਖੋਲ੍ਹਿਆ, ਪਰ agent ਕੋਲ gameplay ਦੀ direct visual confirmation ਨਹੀਂ ਸੀ।

## Output ਲਈ ਥਾਂ ਰੱਖੋ

```json
{
  "reasoning_budget_tokens": 8000
}
```

**ਇਹ setting ਮੌਜੂਦਾ `strata-iq3_s.json` configuration ਵਿੱਚ merge ਕਰੋ**, ਬਾਕੀ fields ਬਚਾ ਕੇ, ਫਿਰ ਚੁਣੇ Strata model ਨੂੰ restart ਕਰੋ। ਇਹ Strata setting ਹੈ, replacement OpenCode configuration file ਨਹੀਂ। Startup output ਵਿੱਚ active budget verify ਕਰੋ।

**Strata ਇੱਕ hard reasoning budget document ਕਰਦਾ ਹੈ**, ਜੋ thinking phase ਖਤਮ ਕਰਕੇ answer ਵੱਲ ਜਾਂਦਾ ਹੈ। Request-level value configured default ਨੂੰ override ਕਰਦੀ ਹੈ। ਇਹ setting low ਜਾਂ high ਵਰਗੀ general reasoning-effort instruction ਤੋਂ ਵੱਖਰੀ ਹੈ।

**ਪਹਿਲੀ game attempt ਨੇ planning ਦੌਰਾਨ ਆਪਣਾ 16,384-token allowance ਖਰਚ ਕਰ ਦਿੱਤਾ।** Retry ਨੇ 8,000-token thinking budget ਲਗਾਇਆ ਅਤੇ code ਦਿੱਤਾ। ਇਹ workload ਲਈ bounded reasoning phase ਵਰਤਣ ਦੀ ਹਮਾਇਤ ਕਰਦਾ ਹੈ। ਇਹ ਹਰ task ਲਈ 8,000 ਨੂੰ best setting ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

**ਬਾਕੀ output allowance maximum ਹੈ, guarantee ਕੀਤੀ reservation ਨਹੀਂ।** ਜੇ 16,384 total limit ਹੇਠ 8,000-token cap ਪੂਰਾ ਵਰਤਿਆ ਜਾਂਦਾ, ਤਾਂ ਹੋਰ overhead ਤੋਂ ਪਹਿਲਾਂ ਲਗਭਗ 8,384 tokens ਬਚਦੇ। Result log retry ਉੱਤੇ 11,054 written tokens ਦੱਸਦਾ ਹੈ, ਪਰ reasoning ਅਤੇ code ਦੀ complete ਵੰਡ ਨਹੀਂ ਦਿੰਦਾ। ਇਸ ਨੂੰ ਉਸੇ limit ਵਿੱਚ 8,000 reasoning tokens plus 11,054 code tokens ਨਾ ਸਮਝੋ।

**Narrow edits ਲਈ ਛੋਟਾ budget ਵਰਤੋ**, ਫਿਰ ਵਧੇਰੇ analysis ਵਾਲੇ tasks ਲਈ ਵੱਡੇ budgets test ਕਰੋ। Complete file output, finish status ਅਤੇ test results ਵੇਖੋ। ਵੱਧ planning time ਤਦ ਹੀ ਲਾਭਦਾਇਕ ਹੈ ਜਦੋਂ delivered change ਸੁਧਰੇ।

## Strata ਅਤੇ OpenCode ਜੋੜੋ

```bash
git clone https://github.com/Niko1221/Strata.git
cd Strata
./setup.sh
```

**ਇਹ Linux setup entry point ਹੈ।** Current installation instructions review ਕਰੋ ਅਤੇ documented Windows path ਲਈ **`START-HERE.bat`** ਵਰਤੋ। Reported configuration ਦੇ ਨੇੜੇ ਜਾਣ ਲਈ original Qwen3.8-Flash-Next IQ3_S variant ਅਤੇ 65,536-token context ਚੁਣੋ। Benchmark notes ਵਿੱਚ engine version ਅਤੇ selected model files save ਕਰੋ।

```bash
npm install -g opencode-ai
```

**OpenCode ਇੰਸਟਾਲ ਕਰੋ** ਅਤੇ ਇਸ ਦੀਆਂ [ਅਧਿਕਾਰਿਕ ਹਦਾਇਤਾਂ](https://opencode.ai/docs/) ਮੰਨੋ। ਦੂਜੇ terminal ਵਿੱਚ **`STRATA_BASE_URL`** ਨੂੰ Strata ਵੱਲੋਂ ਦਿੱਤੇ local API ਪਤੇ ਤੇ ਸੈੱਟ ਕਰੋ ਅਤੇ ਅੰਤ ਵਿੱਚ **`/v1`** ਜੋੜੋ। ਇਸ ਸੈੱਟਅੱਪ ਵਿੱਚ inference ਨੂੰ local machine ਤੱਕ ਸੀਮਿਤ ਰੱਖੋ।

```json
{
  "provider": {
    "strata": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Strata local",
      "options": {
        "baseURL": "{env:STRATA_BASE_URL}",
        "apiKey": "local"
      },
      "models": {
        "qwen3.8-flash-next-iq3_s": {
          "name": "Qwen3.8-Flash-Next IQ3_S",
          "limit": { "context": 65536, "output": 16384 }
        }
      }
    }
  },
  "model": "strata/qwen3.8-flash-next-iq3_s"
}
```

**ਮੌਜੂਦਾ settings ਬਚਾਉਂਦੇ ਹੋਏ provider block ਨੂੰ `~/.config/opencode/opencode.json` ਵਿੱਚ ਜੋੜੋ।** [ਪ੍ਰਕਾਸ਼ਿਤ ਉਦਾਹਰਨ ਸੰਰਚਨਾ](https://raw.githubusercontent.com/network-tocoder/Free-Local-AI-Coding-Agent-125B-on-16GB-GPU/main/config/opencode.json) environment variable ਤੋਂ local endpoint ਦਾ ਪਤਾ ਲੈਂਦੀ ਹੈ। OpenCode [ਕਸਟਮ provider](https://opencode.ai/docs/providers/) ਅਤੇ [ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਬਦਲਣ](https://opencode.ai/docs/config/) ਬਾਰੇ ਦਸਤਾਵੇਜ਼ ਦਿੰਦਾ ਹੈ।

**`local` placeholder credential ਹੈ**, example unauthenticated local setup ਦੇ ਅਨੁਸਾਰ। ਇਹ server secure ਨਹੀਂ ਕਰਦਾ। ਜੇ Strata instance authentication enable ਕਰਦੀ ਹੈ, ਤਾਂ configured credential ਨੂੰ ਉਚਿਤ local secret mechanism ਰਾਹੀਂ ਦਿਓ।

**`opencode` ਨੂੰ disposable project copy ਵਿੱਚ start ਕਰੋ** ਅਤੇ configured model ਚੁਣੋ। Code ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ selected provider verify ਕਰੋ। Client-side context declaration server ਦੇ configured context ਨੂੰ ਨਹੀਂ ਵਧਾਉਂਦੀ, ਅਤੇ 65,536-token window input ਲਈ 65,536 tokens ਨਹੀਂ ਛੱਡਦੀ ਜਦੋਂ output ਲਈ ਵੀ ਥਾਂ ਚਾਹੀਦੀ ਹੈ।

## Local inference ਅਤੇ permissions

```json
{
  "permission": {
    "edit": "ask",
    "bash": "ask"
  }
}
```

**Agent ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ OpenCode configuration ਵਿੱਚ ਸ਼ੁਰੂਆਤੀ permissions ਜੋੜੋ।** [ਅਨੁਮਤੀਆਂ ਬਾਰੇ ਦਸਤਾਵੇਜ਼](https://opencode.ai/docs/permissions/) ਉਪਲਬਧ controls ਸਮਝਾਉਂਦੇ ਹਨ। Inference ਜਿੱਥੇ ਵੀ ਚੱਲੇ, file ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਅਤੇ shell commands ਤੁਹਾਡੀ machine ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ।

**Local inference ਹਰ tool ਨੂੰ local ਨਹੀਂ ਬਣਾਉਂਦੀ।** Package downloads, web tools, external integrations ਅਤੇ optional sharing ਵਿੱਚ network services ਸ਼ਾਮਲ ਰਹਿੰਦੀਆਂ ਹਨ। Private repositories ਸੰਭਾਲਣ ਤੋਂ ਪਹਿਲਾਂ enabled tools review ਕਰੋ। “Model locally runs” ਦਾ ਦਾਅਵਾ “ਕੁਝ ਵੀ computer ਤੋਂ ਬਾਹਰ ਨਹੀਂ ਜਾਂਦਾ” ਨਾਲੋਂ ਛੋਟਾ ਹੈ।

## ਪਹਿਲੀ run ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਦਾ ਹੱਲ

| Symptom | ਪਹਿਲਾਂ ਕੀ check ਕਰਨਾ ਹੈ |
|---|---|
| **Provider unavailable** | Strata ਚੱਲ ਰਹੀ ਹੈ ਅਤੇ environment variable OpenCode process ਤੱਕ ਪਹੁੰਚਦੀ ਹੈ |
| **Model selection ਵਿੱਚ missing** | Provider ID ਅਤੇ model ID saved configuration ਨਾਲ match ਕਰਦੇ ਹਨ |
| **Context-limit error** | Prompt length plus requested output server ਦੀ active window ਵਿੱਚ fit ਹੁੰਦਾ ਹੈ |
| **Planning without code** | Reasoning budget, total output limit ਅਤੇ finish status |
| **Slow continuation** | Prefix reuse, memory pressure, expert-cache behaviour ਅਤੇ competing processes |
| **Docker command fails** | Working engine ਉਪਲਬਧ ਹੈ, ਕੇਵਲ command-line client ਨਹੀਂ |

**ਇੱਕ ਵਾਰ ਵਿੱਚ ਇੱਕ setting ਬਦਲੋ** ਅਤੇ saved starting state ਤੋਂ ਉਹੀ task ਦੁਹਰਾਓ। ਇਸ ਨਾਲ configuration improvement ਨੂੰ ਵੱਖਰੇ prompt ਜਾਂ ਆਸਾਨ test ਤੋਂ ਵੱਖ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਕੀ ਇਹ subscription ਬਦਲਦਾ ਹੈ?

| Local setup test ਕਰਨ ਦੀ ਸਥਿਤੀ | ਹੋਰ option ਉਪਲਬਧ ਰੱਖੋ |
|---|---|
| **Existing compatible hardware** | ਕੇਵਲ untested workload ਲਈ hardware ਖਰੀਦਣਾ |
| **Bounded application changes** | ਵੱਡੀਆਂ ਅਣਜਾਣ repositories ਅਤੇ ਔਖੀਆਂ migrations |
| **Repeatable acceptance tests** | Correctness check ਕਰਨ ਦੇ reliable ਤਰੀਕੇ ਤੋਂ ਬਿਨਾਂ tasks |
| **Runtime maintenance ਲਈ ਸਮਾਂ** | Minimal setup ਅਤੇ support overhead ਵਾਲਾ ਕੰਮ |

**Zero API spend ਮਹੱਤਵਪੂਰਨ ਹੈ**, ਖਾਸ ਕਰਕੇ ਜਦੋਂ hardware ਪਹਿਲਾਂ ਉਪਲਬਧ ਹੋਵੇ। ਇਸ ਵਿੱਚ electricity, hardware depreciation, storage ਅਤੇ environment maintain ਕਰਨ ਦਾ time ਸ਼ਾਮਲ ਨਹੀਂ। Displayed zero-cost field ਇਹ expenses ਵੀ meter ਨਹੀਂ ਕਰਦੀ।

**Subscription comparison ਲਈ matched tasks ਚਾਹੀਦੇ ਹਨ।** ਦੋਵੇਂ systems ਵਿੱਚ ਉਹੀ starting repository, instructions ਅਤੇ acceptance checks ਚਲਾਓ। Elapsed time ਨਾਲ retries ਅਤੇ human corrections ਵੀ record ਕਰੋ। Full workflow evaluate ਕਰਦੇ ਸਮੇਂ failed first game attempt ਸ਼ਾਮਲ ਕਰੋ, ਕੇਵਲ successful retry ਨਹੀਂ।

**Useful local agent ਨੂੰ universal superiority ਦੀ ਲੋੜ ਨਹੀਂ।** ਜੇ ਇਹ routine edits ਭਰੋਸੇ ਨਾਲ ਕਰਦਾ ਹੈ ਅਤੇ ਔਖੇ tasks ਦਾ ਛੋਟਾ set ਕਿਸੇ ਹੋਰ tool ਨੂੰ ਛੱਡਦਾ ਹੈ, ਤਾਂ ਇਹ ਪਹਿਲਾਂ ਹੀ ਤੁਹਾਡੀ paid services ਦੀ ਲੋੜ ਬਦਲਦਾ ਹੈ। ਆਪਣੇ projects ਵਿੱਚ accepted work ਦੇ ਆਧਾਰ ਉੱਤੇ ਫੈਸਲਾ ਕਰੋ।

## ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਅਗਲੇ ਕਦਮ

{{< youtube id="QBPbvMaHkJc" enable="true" title="Strata, OpenCode ਅਤੇ 16GB GPU ਨਾਲ ਸਥਾਨਕ coding agent test" >}}

**ਹੋਰ ਵੇਖੋ:** [125B local coding agent ਦਾ ਪ੍ਰਦਰਸ਼ਨ](https://www.youtube.com/watch?v=QBPbvMaHkJc)। ਉੱਪਰਲੇ ਮਾਪ ਪ੍ਰਕਾਸ਼ਿਤ ਟੈਸਟ ਤੋਂ ਹਨ। ਇਹ ਇਸ ਲੇਖ ਲਈ ਕੀਤਾ ਸੁਤੰਤਰ benchmark ਨਹੀਂ ਹੈ।

1. **ਇੱਕ ਛੋਟਾ task ਦੁਹਰਾਓ** fixed acceptance criteria ਅਤੇ saved starting revision ਨਾਲ।
2. **Cold ਅਤੇ warm turns ਮਾਪੋ**, prefix reuse ਨੂੰ cold prefill speed ਨਾ ਸਮਝੋ।
3. **Packaging ਨੂੰ ਵੱਖਰੇ ਤੌਰ ਉੱਤੇ verify ਕਰੋ** successful image build, startup ਅਤੇ container-level checks ਨਾਲ।
4. **Generated tests inspect ਕਰੋ** ਅਤੇ ਉਹ cases ਜੋ implementation ਨੇ anticipate ਨਹੀਂ ਕੀਤੇ, ਜੋੜੋ।
5. **Completed work compare ਕਰੋ** subscription ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ current coding tool ਨਾਲ।

**Hardware ਦੀ ਯੋਜਨਾ ਲਈ**, [ਸਥਾਨਕ AI model ਅਤੇ GPU ਸੰਦਰਭ ਗਾਈਡ](/articles/local-ai-model-gpu-context-guide/) ਪੜ੍ਹੋ। Hosted model ਦੇ ਵਿਹਾਰ ਅਤੇ ਲਾਗਤਾਂ ਲਈ [OpenRouter provider routing ਗਾਈਡ](/articles/openrouter-provider-routing-quality-cost/) ਵੇਖੋ।
