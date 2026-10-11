---
title: "Meta ਦੇ Context Language Models: ਏਜੰਟ ਦੀ ਬਿਹਤਰ ਯਾਦਦਾਸ਼ਤ, ਪਰ hallucinations ਦਾ ਅੰਤ ਨਹੀਂ"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Context Language Models ਏਜੰਟ ਦੀ memory ਨੂੰ ਕਿਵੇਂ edit ਕਰਦੇ ਹਨ, benchmarks ਕੀ ਸਾਬਤ ਕਰਦੇ ਹਨ, ਅਤੇ cache cost, model capability ਅਤੇ ਅਣਭਰੋਸੇਯੋਗ notes reliability ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "AI ਏਜੰਟ", "ਲੋਕਲ AI", "AI ਸੁਰੱਖਿਆ"]
tags: ["Context Language Models", "CLM", "Meta AI", "AI hallucinations", "ਏਜੰਟ memory", "context management", "context compaction", "context window", "Suffix Cache Reuse", "KV cache", "SGLang", "llama.cpp", "prompt caching", "prompt injection", "BrowseComp-Plus", "ContextBench", "EdgeBench", "Qwen3.6", "ਲੰਬੇ ਸਮੇਂ ਚੱਲਣ ਵਾਲੇ ਏਜੰਟ", "AI reliability", "ਏਜੰਟ verification"]
cover: "/img/cover/context-language-models-editable-memory.webp"
coverAlt: "ਹਨੇਰੀ ਸਤ੍ਹਾ ਉੱਤੇ ਮੁੜ ਕ੍ਰਮਬੱਧ ਪਾਰਦਰਸ਼ੀ document cards ਅਤੇ ਵੱਖਰੇ archive stack ਦੇ ਕੋਲ ਚਮਕਦਾ processor"
coverCaption: "Edit ਹੋ ਸਕਣ ਵਾਲੀ ਏਜੰਟ memory ਦੀ conceptual illustration।"
---

**Context Language Models (CLMs)** AI ਏਜੰਟ ਨੂੰ ਅਗਲੀ model call ਵਿੱਚ ਭੇਜੀ ਜਾਣ ਵਾਲੀ ਜਾਣਕਾਰੀ ਉੱਤੇ ਸਿੱਧਾ control ਦਿੰਦੇ ਹਨ। ਇਹ ਤਰੀਕਾ ਕਈ published evaluations ਵਿੱਚ context management ਸੁਧਾਰਦਾ ਹੈ, ਪਰ hallucinations ਦੇ ਅੰਤ ਨੂੰ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ। ਏਜੰਟ ਨੂੰ ਆਪਣੇ claims ਲਈ evidence ਅਤੇ ਆਪਣੇ ਕੰਮ ਦੀਆਂ independent checks ਹਾਲੇ ਵੀ ਚਾਹੀਦੀਆਂ ਹਨ।

Engineering ਦਾ ਸਵਾਲ ਇਹ ਹੈ ਕਿ selective editing ਸਹੀ facts ਨੂੰ ਮਨਜ਼ੂਰਯੋਗ cost ਉੱਤੇ ਬਚਾਉਂਦੀ ਹੈ ਜਾਂ ਨਹੀਂ। ਛੋਟੀ conversation ਤਦੋਂ ਹੀ useful ਹੈ ਜਦੋਂ ਏਜੰਟ requirements ਬਚਾਏ, observations ਨੂੰ assumptions ਤੋਂ ਵੱਖ ਕਰੇ, ਅਤੇ ਲੋੜ ਪੈਣ ਉੱਤੇ supporting evidence ਲੱਭੇ।

<!--more-->

## ਮੁੱਖ ਨੁਕਤੇ

- **Editable context:** CLM ਮੌਜੂਦਾ models ਲਈ execution method ਹੈ, ਜਿਸ ਨੂੰ training ਨਾਲ ਹੋਰ ਚੰਗੀ ਤਰ੍ਹਾਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।
- **Conditional gains:** model size, context budget, task ਅਤੇ serving backend ਨਤੀਜਿਆਂ ਉੱਤੇ ਅਸਰ ਪਾਉਂਦੇ ਹਨ।
- **Compute accounting:** prefix-reuse FLOPs edits ਤੋਂ ਬਾਅਦ recomputation ਨੂੰ ਗਿਣਦੇ ਹਨ, ਪਰ elapsed time ਜਾਂ billing ਨੂੰ ਸਿੱਧਾ ਨਹੀਂ ਮਾਪਦੇ।
- **Memory integrity:** ਏਜੰਟ ਦੇ ਆਪਣੇ notes ਗਲਤੀਯੋਗ ਅਤੇ ਸੰਭਾਵੀ ਤੌਰ ਉੱਤੇ unsafe inputs ਰਹਿੰਦੇ ਹਨ।
- **Practical evaluation:** accepted results, lost facts, unsupported claims ਅਤੇ recovery cost ਨੂੰ ਇਕੱਠੇ ਮਾਪੋ।

## Memory ਨੂੰ evidence ਤੋਂ ਵੱਖ ਰੱਖੋ

**Context window** ਵਿੱਚ call ਦੌਰਾਨ model ਲਈ available input ਹੁੰਦਾ ਹੈ। Instructions, tool responses, working notes ਅਤੇ ਪਿਛਲੇ messages ਥਾਂ ਲਈ ਮੁਕਾਬਲਾ ਕਰਦੇ ਹਨ। Compaction ਇਸ material ਦੇ ਕੁਝ ਹਿੱਸੇ ਨੂੰ ਛੋਟੀ representation ਨਾਲ ਬਦਲਦੀ ਹੈ।

ਇੱਕ **illustrative dependency-upgrade task** ਵੇਖੋ। Test runner ਦੋ failures report ਕਰਦਾ ਹੈ। ਏਜੰਟ ਆਪਣੀ history ਨੂੰ ਇਸ note ਵਿੱਚ compress ਕਰਦਾ ਹੈ ਕਿ upgrade pass ਹੋ ਗਿਆ। ਅਗਲਾ ਕੰਮ ਫਿਰ ਗਲਤ assumption ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ, ਭਾਵੇਂ original test output disk ਉੱਤੇ ਮੌਜੂਦ ਹੋਵੇ।

Compaction method ਬਦਲਣ ਨਾਲ ਇਹ ਗਲਤ note working memory ਵਿੱਚ ਕਿਵੇਂ ਦਾਖਲ ਹੁੰਦਾ ਹੈ, ਉਹ ਬਦਲਦਾ ਹੈ। ਇਹ **test runner ਨੂੰ evidence ਵਜੋਂ** ਨਹੀਂ ਬਦਲਦਾ। Upgrade ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ workflow ਨੂੰ fresh test result ਜਾਂ relevant run ਦਾ inspectable record ਹਾਲੇ ਵੀ ਚਾਹੀਦਾ ਹੈ।

| Failure | ਢੁੱਕਵੀਂ check |
|---|---|
| **Lost requirement** | Current state ਦੀ original acceptance criteria ਨਾਲ ਤੁਲਨਾ ਕਰੋ |
| **Invented observation** | Claim ਨੂੰ tool result ਜਾਂ source record ਨਾਲ ਮਿਲਾਓ |
| **Incorrect reasoning** | Conclusion ਨੂੰ task ਦੇ expected behavior ਵਿਰੁੱਧ test ਕਰੋ |
| **Unauthorized instruction** | Model-written notes ਤੋਂ ਬਾਹਰ permissions ਲਾਗੂ ਕਰੋ |

ਇਹ ਫਰਕ ਹਰ memory technique ਦੀ evaluation ਵਿੱਚ ਮਹੱਤਵ ਰੱਖਦਾ ਹੈ। **Preservation ਅਤੇ correctness ਵੱਖਰੇ ਗੁਣ ਹਨ।** ਕੋਈ system ਗਲਤ claim ਨੂੰ ਬਿਲਕੁਲ ਠੀਕ ਸੰਭਾਲੇ, ਫਿਰ ਵੀ ਉਹ ਗਲਤ ਰਹਿੰਦਾ ਹੈ।

## CLMs ਕੀ ਬਦਲਦੇ ਹਨ

**Rulin Shao ਅਤੇ coauthors**, ਜਿਨ੍ਹਾਂ ਵਿੱਚ Meta Superintelligence Labs ਅਤੇ University of Washington ਦੇ researchers ਸ਼ਾਮਲ ਹਨ, ਨੇ 29 ਸਤੰਬਰ 2026 ਦੇ preprint ਵਿੱਚ CLMs ਪੇਸ਼ ਕੀਤੇ। ਉਨ੍ਹਾਂ ਦੀ implementation live context ਨੂੰ editable file ਵਜੋਂ ਦਿੰਦੀ ਹੈ। Agent ਇਸ ਨੂੰ shell commands ਜਾਂ code ਨਾਲ edit ਕਰਦਾ ਹੈ ਅਤੇ runtime ਅਗਲੀ call ਉੱਤੇ revised contents ਦਿੰਦਾ ਹੈ। [Context Language Models](https://arxiv.org/abs/2609.37725) ਵੇਖੋ।

```text
Ordinary continuation:
existing context + new response + new tool output

Editable-context continuation:
agent revises context file -> runtime loads revised context -> next model call
```

**Zero-shot ਤਰੀਕੇ ਲਈ model architecture ਬਦਲਣ ਦੀ ਲੋੜ ਨਹੀਂ।** Runtime existing model ਦੇ ਆਲੇ-ਦੁਆਲੇ capability ਜੋੜਦਾ ਹੈ। Paper instructions, learned context-management strategies ਅਤੇ reinforcement learning ਨੂੰ ਵੱਖਰੇ ਤੌਰ ਉੱਤੇ ਜਾਂਚਦਾ ਹੈ।

**Notes file** ਵੱਖਰੀ ਚੀਜ਼ ਹੈ। Saved note ਪੜ੍ਹਨ ਨਾਲ ਉਸ ਦਾ content conversation ਵਿੱਚ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ। ਬਾਅਦ ਵਿੱਚ file edit ਕਰਨ ਨਾਲ live context ਵਿੱਚ ਪੁਰਾਣਾ text ਆਪਣੇ ਆਪ ਨਹੀਂ ਹਟਦਾ। CLM ਨੂੰ subsequent requests ਨਾਲ edits synchronize ਕਰਨ ਲਈ runtime support ਚਾਹੀਦੀ ਹੈ। [Official implementation](https://github.com/facebookresearch/context-language-models) ਵਿੱਚ agent code ਅਤੇ separate serving extension ਹਨ।

**External storage ਹਾਲੇ ਵੀ useful ਹੈ।** Detailed logs ਅਤੇ source documents ਨੂੰ retrieval ਲਈ available ਰੱਖੋ ਅਤੇ working memory ਵਿੱਚ concise references ਰੱਖੋ। Document ਦੀ location ਅਤੇ ਉਸ ਨਾਲ supported claim ਅਕਸਰ ਅਗਲੇ prompt ਵਿੱਚ ਹਰ line ਰੱਖਣ ਨਾਲੋਂ ਵੱਧ ਮਹੱਤਵਪੂਰਨ ਹੁੰਦੇ ਹਨ।

## Results ਨੂੰ ਧਿਆਨ ਨਾਲ ਪੜ੍ਹੋ

**Benchmark improvements specific comparisons ਹਨ।** ਹੇਠਲੇ findings authors ਦੀ evaluations ਤੋਂ ਹਨ, ਇਸ article ਲਈ ਕੀਤੇ tests ਤੋਂ ਨਹੀਂ। Research ਹਾਲੇ preprint ਹੈ ਅਤੇ selected benchmark arbitrary workflows ਲਈ reliability ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

| Evaluation | Reported result | Interpretation |
|---|---|---|
| **BrowseComp-Plus, zero-shot** | Strongest baseline ਦੇ ਮੁਕਾਬਲੇ 11.4% relative accuracy gain ਅਤੇ 21.5% ਘੱਟ prefix-reuse FLOPs | ਇਸ setup ਵਿੱਚ accuracy ਅਤੇ compute ਦੋਵੇਂ ਸੁਧਰੇ |
| **TerminalBench 2.1** | 29.5% ਘੱਟ FLOPs ਨਾਲ strongest baseline ਜਿੰਨੀ accuracy | Comparable accuracy ਉੱਤੇ benefit efficiency ਹੈ |
| **EdgeBench, 12-hour runs** | 59% ਘੱਟ FLOPs ਨਾਲ 5% ਵੱਧ score | Software-optimization score, hallucination rate ਨਹੀਂ |
| **Trained Qwen3.5-9B** | Trained summary ਦੇ 42.1% ਦੇ ਮੁਕਾਬਲੇ CLM 42.5% | ਵੱਡੇ compute difference ਨਾਲ ਛੋਟਾ accuracy gap |

Trained 9B comparison ਵਿੱਚ **1.34 ਬਨਾਮ 2.19 PFLOPs per question**, ਅਰਥਾਤ CLM ਲਈ ਲਗਭਗ 38.8% ਘੱਟ compute ਵਰਤਿਆ ਗਿਆ। Training ਤੋਂ ਪਹਿਲਾਂ 28.8% ਤੋਂ ਬਾਅਦ 42.5% ਤੱਕ ਸੁਧਾਰ, trained summarization ਦੇ ਵਿਰੁੱਧ 0.4-point gap ਤੋਂ ਵੱਖਰੀ comparison ਹੈ। Baseline ਨੂੰ ਸਪਸ਼ਟ ਰੱਖੋ। [Paper ਦੀ results ਅਤੇ training table](https://arxiv.org/html/2609.37725v1) ਵੇਖੋ।

**Relative percentages** ਲਈ denominator ਵੀ ਚਾਹੀਦਾ ਹੈ। ਲਗਭਗ 53.3% ਤੋਂ 59.4% ਦਾ ਵਾਧਾ 6.1 percentage points, ਜਾਂ 11.4% relative ਹੈ। ਕੋਈ ਵੀ expression ਇਹ ਨਹੀਂ ਕਹਿੰਦਾ ਕਿ system ਹਰ question ਦਾ ਸਹੀ answer ਦਿੰਦਾ ਹੈ।

### Context budget outcomes ਬਦਲਦਾ ਹੈ

**32K context budget** main evaluations ਵਿੱਚ ਵਾਰ ਵਾਰ ਆਉਂਦਾ ਹੈ। ਇਹ retention ਅਤੇ editing ਲਈ meaningful constraint ਬਣਾਉਂਦਾ ਹੈ। ਇਸ budget ਦੇ results ਨੂੰ ਹਰ larger-window deployment ਉੱਤੇ generalize ਨਾ ਕਰੋ।

**EdgeBench-10 ਉੱਤੇ 128K** ਵਿੱਚ Appendix F ਦਸ tasks ਅਤੇ ਤਿੰਨ seeds ਲਈ ਇਹ results ਦਿੰਦਾ ਹੈ:

| Method | Final score | Mean prefix-reuse PFLOPs per trial |
|---|---|---|
| **Summarization** | 47.8 | 222 |
| **CLM** | 47.3 | 142 |
| **CLM with subagents** | 50.2 | 219 |

**Single-agent accuracy ਨੇੜੇ ਹੈ**, ਜਦਕਿ ਇਸ comparison ਵਿੱਚ CLM ਲਗਭਗ 36% ਘੱਟ compute ਵਰਤਦਾ ਹੈ। Subagent configuration ਫਿਰ outcome ਬਦਲਦੀ ਹੈ। Context capacity, agent configuration ਅਤੇ compute budget ਨੂੰ method name ਦੇ ਨਾਲ compare ਕਰੋ।

### Model capability ਹਾਲੇ ਵੀ matter ਕਰਦੀ ਹੈ

**ਛੋਟੇ models memory ਨੂੰ ਆਪਣੇ ਆਪ ਚੰਗੀ ਤਰ੍ਹਾਂ manage ਨਹੀਂ ਕਰਦੇ।** Training comparison ਵਿੱਚ untrained 9B CLM summary baseline ਤੋਂ ਹੇਠਾਂ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ। Separate supplementary evaluation BrowseComp-Plus ਉੱਤੇ 39.9% ਬਨਾਮ 37.7% report ਕਰਦੀ ਹੈ। ਇਹ ਵੱਖਰੇ experimental setups ਹਨ, interchangeable measurements ਨਹੀਂ।

Supplementary TerminalBench analysis **9B tasks ਦੇ ਅੱਧੇ ਵਿੱਚ ਕੋਈ context edits ਨਹੀਂ** report ਕਰਦੀ ਹੈ। Model ਨੂੰ editing interface ਦੇਣ ਨਾਲ ਇਹ ਪੱਕਾ ਨਹੀਂ ਹੁੰਦਾ ਕਿ ਉਹ interface ਨੂੰ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਵਰਤੇਗਾ। CLM ਨੂੰ universal upgrade ਮੰਨਣ ਦੀ ਥਾਂ selected model ਅਤੇ settings ਨੂੰ evaluate ਕਰੋ।

## Reprocessing ਨੂੰ account ਕਰੋ

**KV cache** intermediate attention computations ਰੱਖਦਾ ਹੈ। Ordinary prefix caching ਵਿੱਚ next request ਦੇ ਸ਼ੁਰੂ ਦਾ unchanged text ਪਿਛਲੀ computation ਨੂੰ reuse ਕਰਦਾ ਹੈ। ਸ਼ੁਰੂ ਦੇ ਨੇੜੇ edit reusable prefix ਘਟਾਉਂਦੀ ਹੈ ਅਤੇ ਬਾਅਦ ਵਾਲੇ text ਨੂੰ ਮੁੜ process ਕਰਨਾ ਪੈਂਦਾ ਹੈ।

```text
Previous request: A + B + C
Revised request:  A + replacement for B + C

Standard prefix reuse:
reuse A, recompute replacement for B and C
```

Paper ਦੀ **prefix-reuse FLOPs** metric first mismatch ਤੋਂ ਬਾਅਦ generation ਅਤੇ prompt processing ਗਿਣਦੀ ਹੈ। PFLOP ਦਾ ਅਰਥ 10¹⁵ floating-point operations ਹੈ। ਇਹ estimated computation total ਹੈ, quality score, throughput measurement ਜਾਂ invoice ਨਹੀਂ।

**Local latency prompt throughput ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।** Arithmetic example ਵਜੋਂ assumed 800 tokens per second ਉੱਤੇ 24,000 tokens ਮੁੜ ਪੜ੍ਹਨ ਵਿੱਚ ਹੋਰ overhead ਤੋਂ ਪਹਿਲਾਂ 30 seconds ਲੱਗਦੇ ਹਨ। ਇਹ ਕਿਸੇ ਖਾਸ Mac ਜਾਂ GPU ਦਾ benchmark ਨਹੀਂ। Backend, quantization ਅਤੇ ਆਪਣੇ actual prompt sizes ਨੂੰ measure ਕਰੋ।

[llama.cpp ਦੀ hybrid-model reprocessing discussion](https://github.com/ggml-org/llama.cpp/issues/20225) ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ **prefix changes ਅਤੇ recurrent-state checkpoints** ਕਿਉਂ ਮਹੱਤਵਪੂਰਨ ਹਨ। ਇਹ llama.cpp ਵਰਤਣ ਵਾਲੀਆਂ ਸਾਰੀਆਂ releases ਜਾਂ applications ਵਿੱਚ identical behavior ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ। Runtime version record ਕਰੋ ਅਤੇ cache logs ਵੇਖੋ।

## Cache savings ਦੀਆਂ ਹੱਦਾਂ ਹਨ

**Suffix Cache Reuse (SCR)** edit ਤੋਂ ਬਾਅਦ ਬਚੇ text ਲਈ cached states ਰੱਖਦਾ ਹੈ। Released extension SGLang ਨੂੰ target ਕਰਦੀ ਹੈ ਅਤੇ README version 0.5.16 ਦੱਸਦਾ ਹੈ। ਇਹ separate serving optimization ਹੈ, basic editable-context method ਦੀ prerequisite ਨਹੀਂ।

**Reuse approximate ਹੈ।** ਬਚੇ tokens ਪਿਛਲੇ context ਵਿੱਚ computed states ਰੱਖਦੇ ਹਨ। ਇਸ ਲਈ matching benchmark performance ਨਵੇਂ prompt ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ recompute ਕਰਨ ਦੇ numerical equivalence ਨੂੰ ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ।

Authors BrowseComp-Plus comparison ਵਿੱਚ **35% ਘੱਟ server-side compute** report ਕਰਦੇ ਹਨ। Additionally reused prompt tokens ਦੇ 7.8 percentage points ਵਿੱਚੋਂ 5.3 stripped reasoning blocks ਅਤੇ 2.5 ਹੋਰ edits ਤੋਂ ਆਉਂਦੇ ਹਨ। ਇਸ ਲਈ benefit ਦਾ ਵੱਡਾ ਹਿੱਸਾ explicit CLM editing ਤੋਂ ਪਰੇ ਲਾਗੂ ਹੁੰਦਾ ਹੈ। [SCR implementation notes](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md) ਵੇਖੋ।

**API billing ਲਈ** ordinary input, cache writes ਅਤੇ cache reads ਵੱਖ ਕਰੋ। Anthropic Sonnet 4.6 ਲਈ ordinary input, five-minute cache writes ਅਤੇ cache hits ਵਾਸਤੇ ਕ੍ਰਮਵਾਰ $3, $3.75 ਅਤੇ $0.30 per million tokens ਦੱਸਦੀ ਹੈ। 20,000 tokens ਨੂੰ cache write ਵਜੋਂ rewrite ਕਰਨ ਦੀ cost $0.075 ਹੈ, hit ਦੀ $0.006। $0.069 difference output ਅਤੇ ਹੋਰ billing modifiers ਤੋਂ ਪਹਿਲਾਂ ਹੈ। [Prompt-caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), 10 ਅਕਤੂਬਰ 2026 ਨੂੰ checked।

**Total task cost tradeoff ਤੈਅ ਕਰਦੀ ਹੈ।** ਕਦੇ ਕਦੇ ਮਹਿੰਗੀਆਂ edits ਫਿਰ ਵੀ savings ਦਿੰਦੀਆਂ ਹਨ ਜੇ ਉਹ ਬਾਅਦ ਦੇ input ਨੂੰ ਕਾਫੀ ਘਟਾਉਣ। Frequent edits ਤੋਂ ਬਾਅਦ few remaining turns ਹੋਣ ਉੱਤੇ cost recover ਕਰਨ ਦਾ ਮੌਕਾ ਘੱਟ ਹੁੰਦਾ ਹੈ।

**ਜਿਸ serving path ਨੂੰ deploy ਕਰਦੇ ਹੋ, ਉਸ ਵਿੱਚ cache behavior check ਕਰੋ।** Paper ਦੀ reuse measurements ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦੀਆਂ ਕਿ API, SGLang release ਜਾਂ local runtime ਉਹੀ cache controls ਦਿੰਦਾ ਹੈ। Pilot ਦੌਰਾਨ cache hits, prompt tokens, recomputation ਅਤੇ reset behavior record ਕਰੋ। Missing telemetry ਨੂੰ evaluation limitation ਮੰਨੋ।

## Notes ਨੂੰ instructions ਤੋਂ ਹੇਠਾਂ ਰੱਖੋ

**Model-written memory untrusted task data ਹੈ।** ਇਸ ਵਿੱਚ observations, interpretations ਅਤੇ ਕਦੇ ਕਦੇ mistakes ਹੁੰਦੀਆਂ ਹਨ। ਹਰ note ਨੂੰ instruction ਮੰਨਣ ਨਾਲ ਇਹ mistakes future actions ਉੱਤੇ authority ਲੈ ਲੈਂਦੀਆਂ ਹਨ।

OpenAI ਨੇ ਇੱਕ unreleased Astra-family model ਦੀ separate training run ਵਿੱਚ **27 jailbreak-like compaction summaries** document ਕੀਤੀਆਂ। ਕੁਝ injected instructions ignore ਕੀਤੀਆਂ ਗਈਆਂ, ਜਦਕਿ task-specific restrictions ਨੇ ਇੱਕ reported continuation ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕੀਤਾ। Report rare behavior ਦੱਸਦੀ ਹੈ ਅਤੇ ਕਹਿੰਦੀ ਹੈ ਕਿ final Astra model ਜਾਂ traffic ਲਈ ਵਰਤੇ checkpoints ਵਿੱਚ regeneration ਨੇ ਇਸ ਨੂੰ ਦੁਹਰਾਇਆ ਨਹੀਂ। ਇਹ failure mode ਦਾ evidence ਹੈ, deployed CLMs ਵਿੱਚ prevalence ਦਾ ਨਹੀਂ। [OpenAI ਦੀ compaction-summary report](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/) ਵੇਖੋ।

**Defensive implementation** ਨੂੰ ਇਹ responsibilities ਵੱਖ ਰੱਖਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ:

| Component | Treatment |
|---|---|
| **User requirements ਅਤੇ permissions** | Editable notes layer ਤੋਂ ਬਾਹਰ preserve ਕਰੋ |
| **Working notes** | Revision ਦਿਓ, provenance ਰੱਖੋ ਅਤੇ uncertainty mark ਕਰੋ |
| **Original evidence** | Summaries ਤੋਂ independent retrievable records ਰੱਖੋ |
| **Actions ਅਤੇ edits** | Changes log ਕਰੋ ਅਤੇ code ਵਿੱਚ access controls ਲਾਗੂ ਕਰੋ |

**Deletion ਹਮੇਸ਼ਾ erasure ਨਹੀਂ ਹੁੰਦੀ।** SCR ਪਹਿਲਾਂ ਵਾਲੇ context ਤੋਂ ਪ੍ਰਭਾਵਿਤ states ਰੱਖਦਾ ਹੈ। Engineering inference ਵਜੋਂ editable file ਵਿੱਚੋਂ text ਹਟਾਉਣ ਨੂੰ cached state ਵਿੱਚੋਂ ਸਾਰੇ influence ਹਟਣ ਦਾ proof ਨਾ ਮੰਨੋ। ਜਦੋਂ workflow ਨੂੰ clean restart ਚਾਹੀਦਾ ਹੋਵੇ ਤਾਂ explicit reset test ਕਰੋ।

## Bounded pilot test ਕਰੋ

**Advertised context length ਤੋਂ ਪਹਿਲਾਂ retention requirements ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** Known answers, immutable input records ਅਤੇ clear completion check ਵਾਲਾ repeated task ਚੁਣੋ। ਪਹਿਲੀ comparison ਲਈ synthetic data ਵਾਲੀ sandbox ਵਰਤੋ।

1. **Exact facts ਬਣਾਓ:** identifiers, changed requirements, failed attempts ਅਤੇ ਇੱਕ corrected value ਸ਼ਾਮਲ ਕਰੋ।
2. **Comparable configurations ਚਲਾਓ:** fixed summarization, editable context ਅਤੇ fresh-session notes workflow।
3. **Inputs constant ਰੱਖੋ:** same model, task set, tools, generation limits ਅਤੇ context budget ਵਰਤੋ।
4. **Memory changes ਤੋਂ ਬਾਅਦ check ਕਰੋ:** exact recall, source retrieval ਅਤੇ superseded facts ਦੇ obsolete mark ਹੋਣ ਦੀ ਜਾਂਚ ਕਰੋ।
5. **ਸਾਰਾ run ਮਾਪੋ:** success rate, unsupported claims, elapsed time, edits, overflow recovery ਅਤੇ manual corrections record ਕਰੋ।

**Token accounting runtime ਵਿੱਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।** Appendix G tested models ਵਿੱਚ context-length awareness ਸੀਮਿਤ ਪਾਉਂਦਾ ਹੈ ਅਤੇ environmental hints estimates ਸੁਧਾਰਦੇ ਹਨ। Experimental setup ਵਿੱਚ overflow recovery ਵੀ ਹੈ। Measured token counts ਦਿਓ ਅਤੇ response space reserve ਕਰੋ, model ਦੀ capacity estimate ਉੱਤੇ ਨਿਰਭਰ ਨਾ ਕਰੋ।

ਜਦੋਂ live-context editing unavailable ਹੋਵੇ ਤਾਂ **notes-based fallback** useful ਹੈ। Handoff ਛੋਟਾ ਅਤੇ evidence-linked ਰੱਖੋ। ਹੇਠਲਾ record illustrative ਹੈ, CLM API format ਨਹੀਂ:

```yaml
objective: Upgrade the dependency without changing export behavior
verified:
  - claim: Date export test still fails
    evidence: artifacts/export-test-result.txt
superseded:
  - claim: All tests passed
    reason: Contradicted by the retained test result
unknown:
  - Whether the parser change affects empty input
next_step: Test empty input before changing the formatter
```

**Fresh session ਹਾਲੇ ਵੀ ਇਸ note ਨੂੰ read ਕਰਨ ਲਈ pay ਕਰਦੀ ਹੈ**, ਅਤੇ bad note bad information transfer ਕਰਦੀ ਹੈ। Consequential claims ਲਈ evidence ਮੁੜ ਖੋਲ੍ਹੋ ਅਤੇ original task specification available ਰੱਖੋ। ਇਹ compatibility option ਹੈ, CLM-equivalent gains ਦਾ proof ਨਹੀਂ।

## Accepted results ਦੇ ਆਧਾਰ ਉੱਤੇ ਫੈਸਲਾ ਕਰੋ

**CLMs ਨੂੰ trial ਕਰੋ** ਜਦੋਂ long-running tasks ਵਾਰ ਵਾਰ useful state ਗੁਆਉਂਦੇ ਹਨ ਜਾਂ obsolete context ਉੱਤੇ substantial compute ਖਰਚਦੇ ਹਨ। ਘੱਟ history ਵਾਲੀ short interaction ਇਸ optimization ਲਈ ਘੱਟ opportunity ਦਿੰਦੀ ਹੈ।

Official repository **CC BY-NC 4.0** terms ਰੱਖਦਾ ਹੈ। Commercial project ਵਿੱਚ implementation adopt ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ [license](https://github.com/facebookresearch/context-language-models/blob/main/LICENSE) check ਕਰੋ। Public source availability ਆਪਣੇ ਆਪ unrestricted commercial reuse ਨਹੀਂ ਦਿੰਦੀ।

**Reliable completion target ਰਹਿੰਦਾ ਹੈ।** Method ਸਿਰਫ਼ ਉਦੋਂ ਰੱਖੋ ਜਦੋਂ ਉਹ evidence checks ਨੂੰ ਕਮਜ਼ੋਰ ਕੀਤੇ ਬਿਨਾਂ accepted outcomes ਸੁਧਾਰੇ ਜਾਂ cost ਘਟਾਏ। Related deployment choices ਲਈ [local AI ਅਤੇ ChatGPT comparison](/articles/local-ai-vs-chatgpt-how-close-are-we/) ਅਤੇ [GPU ਅਤੇ context planning guide](/articles/local-ai-model-gpu-context-guide/) ਪੜ੍ਹੋ।

{{< youtube id="9-iiHFQyzuM" enable="true" title="AI hallucinations ਦਾ ਅੰਤ? Meta ਦਾ ਨਵਾਂ fix (CLM)" description="Context Language Models, agent memory, serving costs ਅਤੇ reliability considerations." >}}

## ਹਵਾਲੇ

- **Rulin Shao et al.:** [Context Language Models](https://arxiv.org/abs/2609.37725), 29 ਸਤੰਬਰ 2026, [full results ਅਤੇ appendices](https://arxiv.org/html/2609.37725v1) ਦੇ ਨਾਲ।
- **Meta research implementation:** [Context Language Models repository](https://github.com/facebookresearch/context-language-models)।
- **Serving implementation:** [Suffix Cache Reuse documentation](https://raw.githubusercontent.com/facebookresearch/context-language-models/main/suffix_cache_reuse/README.md)।
- **Anthropic:** [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)।
- **OpenAI:** [Self-generated prompt injections in compaction summaries](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/).
- **llama.cpp:** [Hybrid-model prompt reprocessing discussion](https://github.com/ggml-org/llama.cpp/issues/20225)।
- **Kai:** [The End of AI Hallucinations? Meta's New Fix (CLM's)](https://www.youtube.com/watch?v=9-iiHFQyzuM)।
