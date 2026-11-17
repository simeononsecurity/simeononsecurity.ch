---
title: "Raspberry Pi 4 ਜਾਂ 5 ਉੱਤੇ ਕਿਹੜੇ AI ਮਾਡਲ ਚੱਲਦੇ ਹਨ?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Raspberry Pi 4 ਅਤੇ 5 ਦੇ ਮਾਪੇ ਨਤੀਜਿਆਂ ਤੋਂ ਮੈਮੋਰੀ, ਗਤੀ ਅਤੇ ਕੰਮ ਮੁਤਾਬਕ ਸਥਾਨਕ ਭਾਸ਼ਾ ਮਾਡਲ ਚੁਣੋ, ਛੋਟੇ LFM2.5 ਤੋਂ 3B ਅਤੇ ਵੱਡੇ ਵਿਕਲਪਾਂ ਤੱਕ।"
genre: ["Raspberry Pi", "ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਸਵੈ-ਹੋਸਟਿੰਗ"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "ਸਥਾਨਕ AI", "ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲ", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "ਮਾਡਲ ਕੁਆੰਟੀਜ਼ੇਸ਼ਨ", "ਐਜ AI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "ਗੂੜ੍ਹੇ ਡੈਸਕ ਉੱਤੇ ਦੋ Raspberry Pi ਕੰਪਿਊਟਰ, ਉੱਪਰ ਨੀਲੇ ਅਤੇ ਅੰਬਰ ਰੰਗ ਦੇ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਚਿੱਤਰ"
coverCaption: "Raspberry Pi ਹਾਰਡਵੇਅਰ ਉੱਤੇ ਚੱਲਦੇ ਸਥਾਨਕ AI ਮਾਡਲਾਂ ਦੀ ਤਸਵੀਰ।"
---

Raspberry Pi ਸਥਾਨਕ ਤੌਰ ਉੱਤੇ ਲਾਭਦਾਇਕ ਭਾਸ਼ਾ ਮਾਡਲ ਚਲਾ ਸਕਦਾ ਹੈ, ਪਰ ਮਾਡਲ ਬੋਰਡ ਦੀ ਮੈਮੋਰੀ ਵਿੱਚ ਆਉਣਾ ਅਤੇ ਤੁਹਾਡੀ ਐਪ ਲਈ ਸਹਿਣਯੋਗ ਸਮੇਂ ਵਿੱਚ ਜਵਾਬ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ। 2 GB ਵਾਲਾ Raspberry Pi 4 ਲਗਭਗ ਇੱਕ ਅਰਬ ਤੋਂ ਘੱਟ ਪੈਰਾਮੀਟਰਾਂ ਵਾਲੇ ਮਾਡਲਾਂ ਲਈ ਵਧੀਆ ਹੈ। 8 GB ਵਾਲਾ Raspberry Pi 5 ਸੰਖੇਪ 1B–3B ਮਾਡਲ ਆਰਾਮ ਨਾਲ ਚਲਾ ਸਕਦਾ ਹੈ ਅਤੇ ਕੁਝ ਵੱਡੇ quantized ਮਾਡਲ ਵੀ ਲੋਡ ਕਰ ਸਕਦਾ ਹੈ, ਪਰ ਵੱਡੇ ਸਮਝੌਤਿਆਂ ਨਾਲ।

ਅਸੀਂ Ollama ਰਾਹੀਂ **2 GB Pi 4B** ਅਤੇ **8 GB Pi 5** ਉੱਤੇ ਇਹ ਮਾਡਲ ਖੁਦ ਮਾਪੇ; ਦੋਹਾਂ ਵਿੱਚ microSD ਸਟੋਰੇਜ ਸੀ। ਟੇਬਲਾਂ ਵਾਲੇ ਦੌੜਾਂ ਵਿੱਚ ਉਹੀ ਪੰਜ ਛੋਟੇ ਸਹਾਇਕ prompts, ਉਹੀ system prompt, ਨਿਸ਼ਚਿਤ seed ਅਤੇ 140-token ਆਉਟਪੁੱਟ ਸੀਮਾ ਵਰਤੀ। ਹਰ ਦੌੜ ਤੋਂ ਪਹਿਲਾਂ ਹੋਰ ਮਾਡਲ unload ਕੀਤੇ ਅਤੇ cold-load ਸਮਾਂ, ਪਹਿਲਾ ਦਿਸਣ ਵਾਲਾ token ਆਉਣ ਦਾ ਸਮਾਂ, ਪੂਰਾ ਜਵਾਬ ਸਮਾਂ, ਆਉਟਪੁੱਟ ਗਤੀ ਅਤੇ ਚੋਟੀ ਦੀ resident memory ਮਾਪੀ। ਇਹ ਛੋਟੇ ਜਵਾਬਾਂ ਵਾਲੇ ਕੰਮ ਦੇ ਇਕ-ਪਾਸੇ ਟੈਸਟ ਸਨ। ਨਤੀਜੇ ਸਰੋਤਾਂ ਦਾ ਅੰਦਾਜ਼ਾ ਹਨ, ਵਿਸ਼ਵਵਿਆਪੀ ਗਤੀ ਜਾਂ ਜਵਾਬ-ਗੁਣਵੱਤਾ ਦਰਜਾਬੰਦੀ ਨਹੀਂ। Pi 5 ਦਾ [Cortex-A76 CPU ਅਤੇ ਉਪਲਬਧ ਮੈਮੋਰੀ ਸੰਰਚਨਾਵਾਂ](https://www.raspberrypi.com/products/raspberry-pi-5/) Pi 4 ਦੇ [Cortex-A72 ਪਲੇਟਫਾਰਮ](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf) ਤੋਂ ਵੀ ਕਾਫ਼ੀ ਵੱਖ ਹਨ।

## ਕਿਹੜੇ ਮਾਡਲ ਕਿਸਮਾਂ ਢੁਕਵੀਆਂ ਹਨ

| ਮਾਡਲ ਦੀ ਕਿਸਮ | ਮਾਪਾਂ ਵਿੱਚੋਂ ਉਦਾਹਰਨਾਂ | ਵਰਤੋਂ |
|---|---|---|
| ਲਗਭਗ 230M–600M ਪੈਰਾਮੀਟਰਾਂ ਵਾਲੇ ਛੋਟੇ ਟੈਕਸਟ ਮਾਡਲ | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | ਛੋਟੇ ਸਥਾਨਕ ਹੁਕਮ, ਸਾਰ ਅਤੇ ਸੀਮਿਤ ਸਵਾਲ-ਜਵਾਬ; 2 GB Pi 4 ਲਈ ਵਧੀਆ ਸ਼ੁਰੂਆਤ |
| ਲਗਭਗ 1B–2B ਸੰਖੇਪ ਟੈਕਸਟ ਮਾਡਲ | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Pi 5 ਜਾਂ ਵਧੇਰੇ ਮੈਮੋਰੀ ਵਾਲੇ Pi 4 ਉੱਤੇ ਨੁਕਤੇਦਾਰ ਹਦਾਇਤਾਂ ਲਈ ਹੋਰ ਥਾਂ, ਪਰ ਸਭ ਤੋਂ ਛੋਟੇ ਮਾਡਲਾਂ ਨਾਲੋਂ ਹੌਲੇ ਜਵਾਬ |
| quantized 3B–4B ਟੈਕਸਟ ਮਾਡਲ | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | 8 GB Pi 5 ਲਈ ਵਧੇਰੇ ਸਮਰੱਥ ਚੋਣਾਂ, ਜੇ ਹਰ ਜਵਾਬ ਲਈ ਕਈ ਸਕਿੰਟ ਉਡੀਕ ਮਨਜ਼ੂਰ ਹੋਵੇ |
| ਵੱਡੇ sparse ਜਾਂ hybrid ਮਾਡਲ | LFM2.5 8B | ਜਾਂਚੇ 8 GB Pi 5 ਉੱਤੇ ਤਕਨੀਕੀ ਤੌਰ ਉੱਤੇ ਚੱਲਦਾ ਹੈ, ਪਰ ਮੈਮੋਰੀ ਬਹੁਤ ਲੈਂਦਾ ਅਤੇ cold load ਹੌਲਾ ਹੈ |

ਇਹ **ਟੈਕਸਟ ਬਣਾਉਣ** ਦੇ ਨਤੀਜੇ ਹਨ। ਇਹ ਚਿੱਤਰ ਬਣਾਉਣ, ਬੋਲੀ ਪਛਾਣ, vision ਜਾਂ training ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਨਹੀਂ ਦੱਸਦੇ। “ਚੱਲਦਾ ਹੈ” ਦਾ ਅਰਥ ਸਿਰਫ਼ ਮਾਡਲ ਫਾਈਲ ਦਾ ਕਾਰਡ ਵਿੱਚ ਆਉਣਾ ਨਹੀਂ; runtime, context cache, ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਅਤੇ ਹੋਰ ਸੇਵਾਵਾਂ ਨੂੰ ਵੀ RAM ਚਾਹੀਦੀ ਹੈ। Quantization ਵਜ਼ਨਾਂ ਦੀ ਫਾਈਲ ਛੋਟੀ ਕਰਦੀ ਹੈ, ਪਰ ਜਵਾਬ ਦੀ ਗੁਣਵੱਤਾ ਘਟਾ ਸਕਦੀ ਹੈ, ਖਾਸ ਕਰਕੇ 1-bit ਵਜ਼ਨਾਂ ਵਰਗੀਆਂ ਅਤਿ ਸੈਟਿੰਗਾਂ ਵਿੱਚ।

### ਅੰਕੜੇ ਕੀ ਮਾਪਦੇ ਹਨ

Benchmark ਨੇ Ollama chat API ਨੂੰ ਤੱਥਾਂ, ਸੁਰੱਖਿਆ-ਤਰੀਕਿਆਂ, ਲੱਭੇ context, ਮੌਸਮ ਅਤੇ ਮਦਦ ਬਾਰੇ ਛੋਟੇ prompts ਭੇਜੇ। ਹਰ ਮਾਡਲ ਨੂੰ ਉਹੀ prompt-set ਅਤੇ seed ਮਿਲੇ। ਸਮਾਂ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ ਮਾਡਲ unload ਕੀਤਾ ਤਾਂ ਜੋ ਅਗਲੀ request ਵਿੱਚ cold load ਸ਼ਾਮਲ ਹੋਵੇ। **ਕੁੱਲ ਸਮਾਂ** ਪੂਰੀ request ਦਾ ਹੈ, ਜਦਕਿ **tokens per second** ਸਿਰਫ਼ ਆਉਟਪੁੱਟ ਬਣਾਉਣ ਦੀ ਗਤੀ ਹੈ। ਪਹਿਲਾ *ਦਿਸਣ ਵਾਲਾ* token ਵੀ ਮਾਪਿਆ, ਜੋ ਮਾਡਲ ਦੇ ਜਵਾਬ ਤੋਂ ਪਹਿਲਾਂ reasoning ਕਰਨ ਉੱਤੇ ਅਹਿਮ ਹੈ।

ਮੈਮੋਰੀ ਲਈ ਹਰ request ਦੌਰਾਨ Pi ਦੀ ਉਪਲਬਧ RAM ਅਤੇ swap ਨਾਲ Ollama ਅਤੇ ਇਸ ਦੀ inference process ਦੀ resident memory ਵੀ ਦਰਜ ਕੀਤੀ। **RSS** ਅੰਕ process ਦੀ resident memory ਹਨ, ਪੂਰੇ host ਦੀ ਲੋੜ ਨਹੀਂ। File-backed pages, operating system, browser ਜਾਂ ਹੋਰ ਸਥਾਨਕ ਸੇਵਾ nominally ਫਿੱਟ ਹੋਣ ਵਾਲੇ ਮਾਡਲ ਵਿੱਚ ਵੀ swap ਕਰਵਾ ਸਕਦੀ ਹੈ। ਟੇਬਲਾਂ ਵਿੱਚ ਪਹਿਲੇ ਪੰਜ-prompt, ਇਕ-ਪਾਸੇ runs ਹਨ। ਬਾਅਦ ਵਿੱਚ news prompt ਅਤੇ reply-rule ਜਾਂਚਾਂ ਸ਼ਾਮਲ ਕੀਤੀਆਂ। ਉਹ ਕੀ ਵੇਖਣਾ ਹੈ ਦੱਸਦੀਆਂ ਹਨ, ਪਰ ਪਹਿਲੇ timing ਨੂੰ ਛੇ-prompt compliance ਨਤੀਜੇ ਨਹੀਂ ਬਣਾਉਂਦੀਆਂ।

ਨਾ tokens per second ਤੇ ਨਾ parameter count ਗੁਣਵੱਤਾ ਸਕੋਰ ਹੈ। ਮਾਡਲ ਤੇਜ਼ੀ ਨਾਲ ਲਿਖ ਕੇ ਵੀ ਮੰਗਿਆ ਸਰੋਤ ਛੱਡ ਸਕਦਾ ਹੈ, ਸ਼ਬਦ-ਹੱਦ ਲੰਘ ਸਕਦਾ ਹੈ ਜਾਂ ਅਧੂਰਾ ਵਾਕ ਦੇ ਸਕਦਾ ਹੈ। ਜਿਹੜੇ prompts ਭੇਜਣੇ ਹਨ ਉਨ੍ਹਾਂ ਨਾਲ ਮਾਡਲਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ ਅਤੇ ਐਪ ਲਈ ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ ਜਵਾਬ ਪੜ੍ਹੋ।

## Raspberry Pi 4: ਸਭ ਤੋਂ ਛੋਟੇ ਮਾਡਲ ਚੁਣੋ

ਜਾਂਚੇ 2 GB Pi 4 ਵਿੱਚ ਵਾਧੂ ਮੈਮੋਰੀ ਘੱਟ ਸੀ। ਸਭ ਤੋਂ ਛੋਟੇ LFM2.5 ਮਾਡਲਾਂ ਨੇ ਪੰਜੇ prompts ਪੂਰੇ ਕੀਤੇ, ਜਿਵੇਂ `qwen2.5:0.5b` ਨੇ ਵੀ। ਛੋਟੇ offline ਜਵਾਬਾਂ ਜਾਂ ਨਿੱਕੇ ਸਥਾਨਕ ਸਹਾਇਕ ਲਈ ਇਹ ਵਾਜਬ ਚੋਣਾਂ ਹਨ।

| ਮਾਡਲ | ਮਾਡਲ ਫਾਈਲ | ਮਾਪੀ ਆਉਟਪੁੱਟ ਗਤੀ | ਔਸਤ ਜਵਾਬ ਸਮਾਂ | ਮੈਮੋਰੀ ਜਾਂ ਨਤੀਜਾ |
|---|---:|---:|---:|---|
| LFM2.5-230M, GGUF import | 0.25 GB | 12.8 tokens/s | 7.2 s | ਚੋਟੀ ਦੀ resident memory 383 MB; 5/5 prompts |
| LFM2.5-350M, GGUF import | 0.38 GB | 8.6 tokens/s | 8.6 s | ਚੋਟੀ ਦੀ resident memory 516 MB; 5/5 prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 tokens/s | 9.7 s | 5/5 prompts; Ollama ਵਿੱਚ ਸਿੱਧਾ ਉਪਲਬਧ |
| MiniCPM5-1B, GGUF import, reasoning ਬੰਦ | 0.69 GB | 5.9 tokens/s | 12.2 s | ਚੋਟੀ ਦੀ resident memory 883 MB; 5/5 prompts |
| MiniCPM5-1B, GGUF import, default reasoning | 0.69 GB | 5.7 tokens/s | 33.3 s | ਪੰਜ ਵਿੱਚੋਂ ਸਿਰਫ਼ ਇੱਕ prompt ਨੇ ਵਰਤਣਯੋਗ ਦਿਸਦਾ ਜਵਾਬ ਦਿੱਤਾ |
| `qwen3:0.6b`, default reasoning | 0.52 GB | 6.4 tokens/s | 40.4 s | ਇੱਕ ਖਾਲੀ ਜਵਾਬ; ਬੋਰਡ reboot ਹੋਇਆ |
| `granite4:350m` | 0.71 GB | 4.6 tokens/s | 15.5 s | 913 MB RSS, swap ਜਾਂ reboot ਨਹੀਂ; ਹੌਲਾ ਪਰ ਸਥਿਰ |
| `gemma3:1b` | 0.82 GB | 4.0 tokens/s | 30.7 s | ਵੱਡਾ swap; ਟੈਸਟ ਦੌਰਾਨ ਬੋਰਡ reboot ਹੋਇਆ |
| `qwen3.5:0.8b` | 1.04 GB | — | — | ਪੂਰਾ ਨਹੀਂ ਹੋਇਆ; ਬੋਰਡ reboot ਹੋਇਆ |

Pi 4 ਦੇ ਨਤੀਜੇ ਸਿਸਟਮ ਦੇ ਬਾਕੀ ਕੰਮਾਂ ਉੱਤੇ ਖਾਸ ਨਿਰਭਰ ਕਰਦੇ ਹਨ। ਵੱਡੇ ਮਾਡਲਾਂ ਦੇ ਟੈਸਟਾਂ ਦੌਰਾਨ board reset ਹੋਇਆ, ਜਿਸ ਵਿੱਚ `qwen3.5:0.8b` ਦਾ ਅਧੂਰਾ run ਵੀ ਸ਼ਾਮਲ ਸੀ। ਇਹ ਸਾਡੇ 2 GB setup ਦਾ ਸਬੂਤ ਹੈ, ਹਰ Pi 4 ਜਾਂ ਹਰ 1B ਮਾਡਲ reboot ਕਰੇਗਾ ਇਹ ਦਾਅਵਾ ਨਹੀਂ। 4 GB ਜਾਂ 8 GB Pi 4 ਵਿੱਚ ਮੈਮੋਰੀ ਵੱਧ ਹੈ, ਪਰ CPU ਟੈਸਟ ਕੀਤੇ Pi 5 ਨਾਲੋਂ inference ਹੌਲੀ ਕਰੇਗਾ। ਇਨ੍ਹਾਂ Pi 4 memory variant ਨੂੰ ਸਿੱਧਾ benchmark ਨਹੀਂ ਕੀਤਾ।

Pi 4 ਦਾ ਇਕ ਸ਼ੁਰੂਆਤੀ run ਅੰਤਿਮ ਮਾਪਾਂ ਨਾਲੋਂ ਕਾਫ਼ੀ ਮਾੜਾ ਲੱਗਾ: RAM-ਅਧਾਰਿਤ `/tmp` ਵਿੱਚ ਲਗਭਗ 625 MB staged GGUF ਫਾਈਲਾਂ ਸਨ, ਸਿਰਫ਼ 500–600 MB ਖਾਲੀ ਰਹੇ ਅਤੇ ਸੈਂਕੜੇ MB swap ਵਿੱਚ ਗਏ। ਫਾਈਲਾਂ ਸਥਾਈ ਸਟੋਰੇਜ ਉੱਤੇ ਲਿਜਾਣ ਮਗਰੋਂ ਛੋਟੇ ਮਾਡਲਾਂ ਦੇ ਨਤੀਜਿਆਂ ਨੇ inference memory ਦੀ ਚੰਗੀ ਤਸਵੀਰ ਦਿੱਤੀ। 2 GB ਬੋਰਡ ਉੱਤੇ *download ਕਿੱਥੇ ਰੱਖਿਆ ਹੈ* ਇਹ ਵੀ benchmark ਵਿਗਾੜ ਸਕਦਾ ਹੈ।

**ਸਿਫ਼ਾਰਸ਼:** ਇਸ 2 GB ਬੋਰਡ ਲਈ default ਵਜੋਂ import ਕੀਤਾ LFM2.5-350M ਚੁਣਦੇ ਹਾਂ। ਇਹ **516 MB RSS** ਉੱਤੇ ਸਥਿਰ ਰਿਹਾ, ਲਗਭਗ **1 GB RAM ਉਪਲਬਧ** ਛੱਡੀ ਅਤੇ Pi 4 ਦੇ reply-rule pass ਵਿੱਚ **5/6** ਪਾਏ। Pi 5 ਦੇ repeated test ਵਿੱਚ ਇਸ ਨੇ ਕਦੇ ਸਰੋਤ ਦਾ ਨਾਮ ਛੱਡਿਆ, ਇਸ ਲਈ attribution ਲੋੜੀਂਦਾ ਹੋਵੇ ਤਾਂ ਐਪ ਵਿੱਚ ਜਾਂਚੋ। Latency ਤੇ memory headroom ਸਭ ਤੋਂ ਅਹਿਮ ਹੋਣ ਤਾਂ LFM2.5-230M ਲਓ: ਇਹ ਤੇਜ਼ ਅਤੇ ਹਲਕਾ ਸੀ, ਪਰ ਇੱਕ medical-context ਜਵਾਬ ਵਿੱਚ “nausea or vomiting” ਨੂੰ “nausea/ventilator use” ਕਰ ਦਿੱਤਾ। ਇਹ content error ਇਸ ਨੂੰ health ਜਾਂ safety ਜਵਾਬਾਂ ਲਈ ਕਮਜ਼ੋਰ default ਬਣਾਉਂਦੀ ਹੈ, ਭਾਵੇਂ repeated mechanical compliance score ਵੱਧ ਹੋਵੇ। [Ollama registry](https://ollama.com/library/qwen2.5/tags) ਤੋਂ ਮਾਡਲ ਚਾਹੀਦਾ ਹੋਵੇ ਤਾਂ `qwen2.5:0.5b` ਲਓ, ਪਰ ਇਸ ਦੀ ਕਮਜ਼ੋਰ instruction compliance ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ। `granite4:350m` ਸਥਿਰ ਰਿਹਾ, ਪਰ ਹੌਲਾ ਸੀ ਅਤੇ ਵਧੇਰੇ ਮੈਮੋਰੀ ਲੈਂਦਾ ਸੀ; MiniCPM5-1B ਤਾਂ ਹੀ ਠੀਕ ਹੈ ਜੇ client reasoning ਬੰਦ ਕਰੇ। ਇਸ ਖਾਸ 2 GB setup ਉੱਤੇ reboot ਆਉਣ ਕਰਕੇ Gemma 3 1B ਅਤੇ Qwen3.5 0.8B ਤੋਂ ਬਚੋ।

## Raspberry Pi 5: ਵਧੇਰੇ ਚੋਣਾਂ, ਗਤੀ ਨਾਲ ਸਮਝੌਤਾ

8 GB Pi 5 ਨੇ speed ਅਤੇ memory benchmark ਦੇ **ਸਾਰੇ 25 ਮਾਡਲ** ਚਲਾਏ। ਛੋਟੇ-ਜਵਾਬ ਵਾਲੇ ਕੰਮ ਲਈ ਨਾ-ਸਿਫ਼ਾਰਸ਼ੀ ਮਾਡਲ ਵੀ ਟੇਬਲ ਵਿੱਚ ਹਨ। † import ਕੀਤੇ GGUF ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। “Think off” speed run ਦੀ setting ਹੈ; ਵੱਖਰੇ compliance pass ਵਿੱਚ ਇਹ setting ਜ਼ਰੂਰੀ ਨਹੀਂ ਵਰਤੀ ਗਈ।

| ਮਾਡਲ | ਫਾਈਲ GB | ਆਉਟਪੁੱਟ tok/s | ਜਵਾਬ s | ਚੋਟੀ RSS MB | ਛੋਟੇ ਜਵਾਬ ਦਾ ਅੰਦਾਜ਼ਾ |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | ਸਭ ਤੋਂ ਘੱਟ latency; repeated compliance 78% |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | ਛੱਡੋ: 1-bit weights ਅਤੇ ਇਕ-ਪਾਸੇ compliance 3/6 |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | ਤੇਜ਼, ਪਰ 18 ਵਿੱਚੋਂ 5 ਵਾਰ source citation ਛੱਡੀ |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | ਆਸਾਨ registry ਵਿਕਲਪ; repeated compliance 61% |
| `qwen3:0.6b`, reasoning ਬੰਦ | 0.52 | 23.0 | 4.3 | 1,069 | ਸ਼ਰਤਾਂ ਨਾਲ: 4/6, reasoning setting ਅਹਿਮ |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | ਪ੍ਰਯੋਗਾਤਮਕ 1-bit ਮਾਡਲ; ਇਕ ਵਾਰ ਦਾ 6/6 ਪੱਕਾ ਨਹੀਂ |
| `minicpm5-1b` †, reasoning ਬੰਦ | 0.69 | 18.4 | 5.1 | 869 | ਸ਼ਰਤਾਂ ਨਾਲ: default reasoning ਨੇ ਖਾਲੀ ਜਵਾਬ ਦਿੱਤੇ |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | ਫਿੱਟ ਹੁੰਦਾ ਹੈ, ਪਰ ਛੋਟੇ LFM2.5 ਨਾਲੋਂ ਹੌਲਾ ਤੇ ਵੱਡਾ |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | ਸਾਡੇ ਕੰਮ ਲਈ ਵਧੀਆ; repeated compliance 89% |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | registry ਵਿਕਲਪ; compliance 5/6 |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | registry ਮਾਡਲਾਂ ਵਿੱਚ ਵਧੀਆ repeated compliance: 83% |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6; Gemma 3 1B ਨੇ ਨਿਯਮ ਵਧੀਆ ਮੰਨੇ |
| `qwen3.5:0.8b`, reasoning ਬੰਦ | 1.04 | 8.8 | 12.2 | 1,592 | default reasoning ਨਾਲ 0/6; reasoning control ਨਾ ਹੋਵੇ ਤਾਂ ਬਚੋ |
| `spark-x2.5-1.7b` †, reasoning ਬੰਦ | 1.11 | 9.7 | 9.4 | 1,542 | default reasoning ਨਾਲ 0/6; reasoning control ਨਾ ਹੋਵੇ ਤਾਂ ਬਚੋ |
| `qwen3:1.7b`, reasoning ਬੰਦ | 1.36 | 8.1 | 12.4 | 1,867 | ਸ਼ਰਤਾਂ ਨਾਲ; ਛੋਟਿਆਂ ਤੋਂ ਵੱਧ ਮੈਮੋਰੀ ਅਤੇ ਦੇਰੀ |
| `minicpm5-2b` †, reasoning ਬੰਦ | 1.56 | 7.7 | 10.9 | 1,787 | ਸ਼ਰਤਾਂ ਨਾਲ; ਇਕ pass ਵਿੱਚ 5/6, ਵਾਧੂ bullets |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | ਅਜ਼ਮਾਉਣ ਲਈ 3B ਚੋਣ; ਇਕ pass ਵਿੱਚ 5/6 |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | interactive ਵਰਤੋਂ ਲਈ ਛੱਡੋ: decode ਹੌਲਾ |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | ਹੋਰ 3B ਚੋਣ; compliance run ਰਿਪੋਰਟ ਨਹੀਂ |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | ਫਿੱਟ, ਪਰ ਛੋਟਿਆਂ ਨਾਲੋਂ ਹੌਲੇ ਜਵਾਬ |
| `qwen3.5:2b`, reasoning ਬੰਦ | 2.74 | 5.0 | 16.1 | 3,627 | ਵੱਧ ਮੈਮੋਰੀ ਤੇ ਦੇਰੀ; compliance run ਰਿਪੋਰਟ ਨਹੀਂ |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | ਤੁਰੰਤ ਜਵਾਬ ਲਈ ਛੱਡੋ; ਪਹਿਲਾ token 14.3 s ਵਿੱਚ |
| `ling-3.0-tiny` †, reasoning ਬੰਦ | 4.82 | 9.9 | 19.4 | 5,071 | ਵੱਡਾ footprint; ਇਕ pass ਵਿੱਚ 5/6, grounding error ਸਮੇਤ |
| `lfm2.5:8b`, reasoning ਬੰਦ | 5.16 | 8.7 | 54.6 | 5,317 | ਬਸ ਫਿੱਟ; cold load 34.4 s ਅਤੇ ਲੰਮੇ ਜਵਾਬ |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | ਛੱਡੋ: Pi ਦੀਆਂ ਹੋਰ ਸੇਵਾਵਾਂ ਨਾਲ swap ਦਬਾਅ |

† Import ਕੀਤਾ GGUF। ਜਵਾਬ ਸਮਾਂ ਅਤੇ memory ਅੰਕ Pi 5 ਦੇ ਪੰਜ-prompt speed run ਤੋਂ ਹਨ; compliance ਅੰਕ ਛੇ-prompt ਦੀਆਂ ਵੱਖਰੀਆਂ ਜਾਂਚਾਂ ਤੋਂ ਹਨ। ਜਿਸ ਮਾਡਲ ਦਾ compliance score ਨਹੀਂ, ਉਸ ਵੱਲੋਂ reply rules ਮੰਨਣ ਦਾ ਸਬੂਤ ਨਹੀਂ।

ਛੋਟੇ LFM2.5 ਮਾਡਲ ਇਸ ਛੋਟੇ-ਜਵਾਬ ਕੰਮ ਲਈ ਸਭ ਤੋਂ ਤੇਜ਼ ਸਨ। 1.2B ਸੰਸਕਰਣ ਟੈਸਟ ਕੀਤੇ Pi 5 ਉੱਤੇ ਵਰਤੋਂਯੋਗ ਵਿਚਕਾਰਲਾ ਰਾਹ ਹੈ। Gemma 3 1B registry-only ਵਿਕਲਪ ਹੈ ਅਤੇ ਬਾਅਦ ਦੇ ਟੈਸਟਾਂ ਵਿੱਚ Qwen2.5 1.5B ਨਾਲੋਂ reply rules ਵਧੇਰੇ ਵਾਰ ਮੰਨੇ। ਵਧੇਰੇ ਸਮਰੱਥਾ ਮੰਗਣ ਵਾਲੇ prompt ਲਈ 3B ਮਾਡਲ ਦੀ ਹੌਲੀ output ਲਾਭਦਾਇਕ ਹੋ ਸਕਦੀ ਹੈ, ਪਰ timing ਨਾਲ ਇਕੱਲੇ ਇਹ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦਾ ਕਿ ਕਿਹੜਾ ਮਾਡਲ ਵਧੀਆ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

Cold-load ਅਤੇ first-token ਦੇਰੀ ਵਰਤੋਂ ਦਾ ਅਨੁਭਵ ਬਦਲਦੀਆਂ ਹਨ। Pi 5 ਉੱਤੇ LFM2.5-230M ਲਗਭਗ **0.21 seconds** ਵਿੱਚ load ਹੋਇਆ ਅਤੇ **0.37 seconds** ਵਿੱਚ ਦਿਸਦਾ token ਦਿੱਤਾ। Qwen2.5 1.5B ਨੂੰ load ਲਈ **2.59 seconds** ਅਤੇ ਪਹਿਲੇ ਦਿਸਦੇ token ਲਈ **3.66 seconds** ਲੱਗੇ; Qwen2.5 3B ਨੂੰ **5.60** ਅਤੇ **7.97 seconds**। ਕਦੇ-ਕਦੇ ਸਵਾਲ ਹੋਵੇ ਤਾਂ generation ਸ਼ੁਰੂ ਹੋਣ ਮਗਰੋਂ ਦੀ output rate ਨਾਲੋਂ ਇਹ ਦੇਰੀਆਂ ਵੱਧ ਮਹੱਤਵ ਰੱਖ ਸਕਦੀਆਂ ਹਨ। ਲਗਾਤਾਰ loaded ਮਾਡਲ ਵਿੱਚ ਦੇਰੀ ਘੱਟ ਮਾਇਨੇ ਰੱਖਦੀ ਹੈ, ਪਰ request ਦੇ ਵਿਚਕਾਰ ਵੀ ਮੈਮੋਰੀ ਵਰਤਦਾ ਹੈ।

ਹੋਰ ਮਾਪੇ candidate ਦਿਖਾਉਂਦੇ ਹਨ ਕਿ parameter count ਇਕੱਲੇ ਨਾਲ ਦਰਜਾਬੰਦੀ ਕਿਉਂ ਨਹੀਂ ਕਰਨੀ। Reasoning ਬੰਦ ਕਰਕੇ `qwen3:0.6b` ਨੇ Pi 5 ਉੱਤੇ **1,069 MB RSS** ਨਾਲ **23.0 tokens/s** ਦਿੱਤੇ; import ਕੀਤੇ MiniCPM5-1B ਨੇ **869 MB RSS** ਨਾਲ **18.4 tokens/s** ਦਿੱਤੇ। ਨਾਮ 350M ਹੋਣ ਦੇ ਬਾਵਜੂਦ `granite4:350m` ਨੂੰ **0.71 GB** download ਚਾਹੀਦਾ ਸੀ ਅਤੇ **12.1 tokens/s** ਬਣੇ। Model packaging ਅਤੇ architecture ਨਾਮ, file size, memory ਅਤੇ speed ਦਾ ਰਿਸ਼ਤਾ ਬਦਲਦੇ ਹਨ।

ਜੇ client ਭਰੋਸੇ ਨਾਲ `think: false` ਭੇਜ ਸਕੇ ਤਾਂ Qwen3 0.6B ਤੇ MiniCPM5-1B ਨੂੰ LFM2.5 ਦੇ ਬਦਲ ਵਜੋਂ ਅਜ਼ਮਾਉਣਾ ਠੀਕ ਹੈ। MiniCPM5-2B, Qwen3 1.7B ਅਤੇ Spark-X2.5 1.7B ਵੀ Pi 5 ਉੱਤੇ ਚਲੇ, ਪਰ ਮੁੱਖ ਚੋਣਾਂ ਨਾਲੋਂ speed ਅਤੇ memory ਵਿੱਚ ਸਾਫ਼ ਲਾਭ ਨਹੀਂ ਸੀ। MiniCPM5-1B ਤੇ Spark-X2.5 ਦੀ compliance test ਵਿੱਚ default reasoning ਸੀ; ਉਨ੍ਹਾਂ ਦੇ ਖਾਲੀ ਜਵਾਬ think-off speed run ਦਾ ਨਤੀਜਾ ਨਹੀਂ ਦੱਸਣੇ। ਉਲਟ, think-off ਵਿੱਚ ਤੇਜ਼ ਸਮਾਂ ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਕਿ flag ਨਾ ਭੇਜਣ ਵਾਲਾ bridge ਵਰਤਣਯੋਗ ਜਵਾਬ ਲਵੇਗਾ।

Raw speed ਨਾਲੋਂ ਸੌਖੀ installation ਅਹਿਮ ਹੋਵੇ ਤਾਂ 8 GB Pi 5 ਉੱਤੇ Gemma 3 1B ਅਤੇ Llama 3.2 1B registry ਚੋਣਾਂ ਹਨ। Gemma 3 1B ਨੇ repeated replies ਵਿੱਚ **15/18** ਵਾਰ ਟੈਸਟ ਕੀਤੇ ਨਿਯਮ ਮੰਨੇ। Llama 3.2 1B ਨੇ ਇਕ pass ਵਿੱਚ **5/6** ਪਾਇਆ, ਇਸ ਲਈ ਇਸ ਦਾ compliance ਅੰਦਾਜ਼ਾ ਘੱਟ ਪੱਕਾ ਹੈ। Timing run ਵਿੱਚ Qwen2.5 1.5B, Gemma 3 1B ਨਾਲੋਂ ਛੇਤੀ load ਅਤੇ ਜਵਾਬ ਦੇ ਸਕਿਆ, ਪਰ ਇਕ compliance test ਵਿੱਚ **4/6** ਹੀ ਪਾਏ। ਆਪਣੇ prompt ਦੀ ਲੋੜ ਅਨੁਸਾਰ ਚੁਣੋ।

ਕਦੇ-ਕਦੇ ਲੰਮੇ ਜਾਂ ਔਖੇ text prompt ਲਈ quantized Qwen2.5 3B ਅਤੇ Llama 3.2 3B ਸਾਡੇ 8 GB Pi 5 ਉੱਤੇ ਦਰਮਿਆਨੀ ਮੈਮੋਰੀ ਵਰਤਣ ਵਾਲੇ 3B candidate ਹਨ। ਅਸੀਂ speed ਅਤੇ memory ਮਾਪੀ; Qwen2.5 3B ਨੇ ਇਕ compliance pass ਵਿੱਚ **5/6** ਪਾਏ। Llama 3.2 3B ਲਈ ਤੁਲਨਾਯੋਗ compliance test ਰਿਪੋਰਟ ਨਹੀਂ ਸੀ। ਵਧੇਰੇ parameter ਉਨ੍ਹਾਂ ਨੂੰ ਉਹਨਾਂ ਕੰਮਾਂ ਉੱਤੇ *ਅਜ਼ਮਾਉਣ* ਦਾ ਕਾਰਨ ਹਨ ਜਿੱਥੇ ਛੋਟੇ ਮਾਡਲ ਘੱਟ ਪੈਂਦੇ ਹਨ, ਇਹ ਸਬੂਤ ਨਹੀਂ ਕਿ ਉਹ ਕੰਮ ਚੰਗੇ ਕਰਦੇ ਹਨ। Granite 4 Micro ਅਤੇ Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny ਅਤੇ Gemma 3n E2B Pi 5 ਵਿੱਚ ਫਿੱਟ ਜਾਂ ਲੋਡ ਹੋਏ, ਪਰ ਛੋਟੇ-ਜਵਾਬ ਐਪ ਲਈ latency, memory headroom ਜਾਂ reliability ਘੱਟ ਆਕਰਸ਼ਕ ਸੀ।

ਦੋ Bonsai ਮਾਡਲ extreme quantization ਦੀ ਕੀਮਤ ਦਿਖਾਉਂਦੇ ਹਨ। 1.7B ਅਤੇ 4B ਨਾਮਾਂ ਦੇ ਮੁਕਾਬਲੇ ਉਨ੍ਹਾਂ ਦੀਆਂ Q1_0 ਫਾਈਲਾਂ ਹੈਰਾਨੀਜਨਕ ਛੋਟੀਆਂ ਸਨ, ਫਿਰ ਵੀ 1.7B ਮਾਡਲ ਨੇ reply-rule check ਵਿੱਚ **3/6** ਹੀ ਪਾਏ। 4B ਮਾਡਲ ਨੇ ਛੇ prompts ਵਾਲਾ ਇਕ pass ਪਾਸ ਕੀਤਾ, ਪਰ ਹਰ ਜਵਾਬ ਲਈ **18.1 seconds** ਲੱਗੇ ਅਤੇ repeated compliance ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ। ਖਾਸ ਕਰਕੇ ਜਿੱਥੇ ਜਵਾਬ-ਗੁਣਵੱਤਾ ਮਹੱਤਵਪੂਰਨ ਹੈ ਉੱਥੇ ਦੋਹਾਂ ਨੂੰ default ਸਿਫ਼ਾਰਸ਼ ਨਹੀਂ, ਪ੍ਰਯੋਗ ਸਮਝੋ।

LFM2.5-8B ਨਤੀਜੇ ਨੂੰ ਸੰਦਰਭ ਚਾਹੀਦਾ ਹੈ: hybrid architecture ਹਰ token ਉੱਤੇ ਘੱਟ active parameter ਵਰਤਦੀ ਹੈ, ਇਸ ਲਈ ਇਸ ਦੀ decode rate ਮਾਪੇ dense 3B ਮਾਡਲਾਂ ਤੋਂ ਉੱਚੀ ਸੀ। ਫਿਰ ਵੀ microSD ਤੋਂ cold load ਲਈ **34.4 seconds** ਲੱਗੇ ਅਤੇ **5.3 GB ਤੋਂ ਵੱਧ resident memory** ਵਰਤੀ। ਇਹ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਕੀ ਫਿੱਟ ਹੁੰਦਾ ਹੈ, ਪਰ ਹੋਰ ਸੇਵਾਵਾਂ ਚਲਾਉਂਦੇ Pi ਲਈ ਸੁਖਾਲਾ default ਨਹੀਂ। ਮਾਪੇ `gemma3n:e2b` ਨੇ ਵੀ ਲਗਭਗ 5.3 GB resident memory ਵਰਤੀ ਅਤੇ test host ਦੀਆਂ ਹੋਰ ਸੇਵਾਵਾਂ ਨਾਲ swap ਕਰਵਾਇਆ।

LFM2.5 8B run ਨੇ ਛੋਟਾ ਜਵਾਬ ਰੱਖਣ ਦੀ ਥਾਂ ਪੂਰੀ **140-token ਹੱਦ** ਲੈ ਲਈ। Gemma 3 4B ਨੂੰ ਪਹਿਲੇ token ਲਈ **14.3 seconds** ਅਤੇ ਪੂਰੇ ਜਵਾਬ ਲਈ **30.3 seconds** ਲੱਗੇ। ਦੋਵੇਂ ਇਸ Pi 5 ਵਿੱਚ load ਹੋ ਸਕਦੇ ਹਨ, ਪਰ ਸਾਡੇ ਟੈਸਟਾਂ ਵਿੱਚ responsive ਛੋਟੇ assistant ਵਰਗੇ ਨਹੀਂ ਸਨ। ਢੁਕਵਾਂ ਛੋਟਾ ਜਵਾਬ ਦੇਣ ਵਾਲਾ ਨਿੱਕਾ ਮਾਡਲ radio ਜਾਂ command interface ਲਈ ਕਾਗਜ਼ ਉੱਤੇ ਤੇਜ਼ decode ਵਾਲੇ ਵੱਡੇ ਮਾਡਲ ਨਾਲੋਂ ਵਧੀਆ ਹੋ ਸਕਦਾ ਹੈ।

## ਮੈਮੋਰੀ, reasoning ਅਤੇ ਮਾਡਲ ਫਾਰਮੈਟ

ਸਾਡੇ ਮਾਪਾਂ ਤੋਂ inference resident memory ਦਾ ਪਹਿਲਾ ਅੰਦਾਜ਼ਾ **model download size × 1.4** ਹੈ। ਇਹ thumb rule ਹੈ: context length, runtime setting, model architecture ਅਤੇ ਹੋਰ process ਲੋੜ ਬਦਲਦੇ ਹਨ। Generation ਦੌਰਾਨ ਉਪਲਬਧ memory ਵੇਖੋ, ਛੋਟੇ host ਉੱਤੇ ਇਕੋ ਮਾਡਲ load ਰੱਖੋ ਅਤੇ OS ਲਈ ਥਾਂ ਛੱਡੋ। 4 GB ਬੋਰਡ ਛੋਟੇ ਜਾਂ compact ਮਾਡਲਾਂ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹੈ, ਪਰ 4 GB ਲਈ ਸਾਡੀਆਂ ਸਿਫ਼ਾਰਸ਼ਾਂ extrapolation ਹਨ, ਸਿੱਧੇ 4 GB ਟੈਸਟ ਨਹੀਂ।

ਉਦਾਹਰਨ ਵਜੋਂ Pi 5 ਉੱਤੇ 0.73 GB LFM2.5-1.2B ਫਾਈਲ ਲਗਭਗ **967 MB RSS** ਨਾਲ ਮਿਲੀ, ਜਦਕਿ 0.99 GB Qwen2.5 1.5B ਫਾਈਲ **1,361 MB RSS** ਤੱਕ ਗਈ। ਇਨ੍ਹਾਂ ਮਾਡਲਾਂ ਲਈ thumb rule ਠੀਕ ਹੈ, ਪਰ ਸਖ਼ਤ ਹੱਦ ਨਹੀਂ। ਜੇ Pi interface, search index, local library ਜਾਂ ਹੋਰ background service ਵੀ ਚਲਾਉਂਦਾ ਹੋਵੇ ਤਾਂ ਮਾਡਲ process ਤੋਂ ਵੱਧ memory ਰੱਖੋ। ਅਸਲੀ request ਵਿੱਚ swap ਵੇਖੋ; ਸਿਰਫ਼ ਲੋਡ ਹੋ ਜਾਣਾ ਪਰ ਲਗਾਤਾਰ swap ਕਰਨਾ ਵਰਤੋਂਯੋਗ fit ਨਹੀਂ।

ਕੁਝ ਮਾਡਲ ਦਿਸਦੇ ਜਵਾਬ ਤੋਂ ਪਹਿਲਾਂ ਅੰਦਰੂਨੀ reasoning block ਬਣਾਉਂਦੇ ਹਨ। ਸਾਡੇ ਟੈਸਟ ਵਿੱਚ 2 GB Pi 4 ਉੱਤੇ `qwen3:0.6b` ਨੂੰ ਦਿਸਦਾ text ਬਣਾਉਣ ਵਿੱਚ ਕਾਫ਼ੀ ਵੱਧ ਸਮਾਂ ਲੱਗਾ। MiniCPM5-1B ਨੇ default reasoning ਉੱਤੇ ਪੰਜ ਵਿੱਚੋਂ ਇਕ ਅਤੇ reasoning ਬੰਦ ਕਰਨ ਉੱਤੇ ਪੰਜੇ prompts ਲਈ ਉਪਯੋਗ ਜਵਾਬ ਦਿੱਤਾ। ਛੋਟੀ ਜਵਾਬ-ਸੀਮਾ ਲਈ compatible Ollama API request ਵਿੱਚ `think: false` ਰੱਖੋ ਜਾਂ default reasoning ਨਾ ਕਰਨ ਵਾਲਾ ਮਾਡਲ ਚੁਣੋ। ਇਹ setting ਸਿਰਫ਼ ਸਮਰਥਿਤ model ਅਤੇ client ਲਈ ਹੈ, ਸਾਰਵਭੌਮ speed switch ਨਹੀਂ।

ਫਰਕ ਇਸ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿ token cap ਵਿੱਚ reasoning ਉੱਤੇ ਲੱਗੇ token ਵੀ ਹੋ ਸਕਦੇ ਹਨ, ਭਾਵੇਂ ਵਰਤੋਂਕਾਰ ਨੂੰ ਜਵਾਬ ਨਾ ਦਿੱਸੇ। Pi 4 ਉੱਤੇ default reasoning ਵਾਲੇ `qwen3:0.6b` ਨੇ request ਪਿੱਛੇ ਔਸਤ **40.4 seconds** ਲਏ; ਇਕ prompt ਵਿੱਚ ਦਿਸਦਾ ਜਵਾਬ ਖਾਲੀ ਸੀ। MiniCPM5-1B ਨੇ default setting ਉੱਤੇ ਔਸਤ **33.3 seconds**, reasoning ਬੰਦ ਹੋਣ ਉੱਤੇ **12.2 seconds** ਲਏ। Pi 5 ਦੌੜਾਂ ਵਿੱਚ ਜਿੱਥੇ ਰਿਕਾਰਡ ਨੇ ਦੱਸਿਆ, Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 ਅਤੇ Spark-X2.5 ਦਾ reasoning ਬੰਦ ਕੀਤਾ। ਹਰ ਮਾਡਲ ਨੂੰ ਉਹੀ reasoning setting ਦੇ ਕੇ ਤੁਲਨਾ ਕਰੋ ਜੋ client ਵਰਤੇਗਾ।

### ਵੇਖੋ ਜਵਾਬ ਵਰਤਣਯੋਗ ਹੈ ਜਾਂ ਨਹੀਂ

ਸਾਡੇ ਛੋਟੇ mesh-assistant ਕੰਮ ਵਿੱਚ response contract ਗਤੀ ਜਿੰਨਾ ਅਹਿਮ ਹੈ: ਵੱਧ ਤੋਂ ਵੱਧ **90 ਸ਼ਬਦ**, **ਤਿੰਨ bullet** ਤੱਕ, plain text, ਪੂਰਾ ਵਾਕ, ਅਤੇ ਦਿੱਤੇ retrieval context ਦੀ source name ਨਾਲ ਵਰਤੋਂ। Bridge ਪਾਠ ਨੂੰ **180-character chunks** ਵਿੱਚ ਵੰਡਦਾ ਹੈ। ਲੰਮਾ ਜਵਾਬ radio airtime ਵਧਾਉਂਦਾ ਹੈ, ਭਾਵੇਂ ਮਾਡਲ ਤੇਜ਼ ਬਣਾਏ।

Benchmark ਦਾ ਬਾਅਦਲਾ ਸੰਸਕਰਣ ਖਾਲੀ ਜਵਾਬ, prompt-ਵਿਸ਼ੇਸ਼ ਸ਼ਬਦ-ਹੱਦ, ਵਾਧੂ bullets, Markdown table ਜਾਂ code fence, ਅਧੂਰਾ ਅੰਤ, ਦਿੱਤੇ context ਦੇ term ਦੀ ਗੈਰਹਾਜ਼ਰੀ ਅਤੇ source name ਦੀ ਗੈਰਹਾਜ਼ਰੀ ਵੇਖਦਾ ਹੈ। ਤੈਨਾਤ assistant ਦੇ system prompt ਅਨੁਸਾਰ ਜਾਂਚਣ ਉੱਤੇ ਛੋਟੇ ਮਾਡਲ ਅਕਸਰ ਇਹ ਨਿਯਮ ਤੋੜਦੇ ਸਨ। ਸਭ ਤੋਂ ਗੰਭੀਰ ਗਲਤੀਆਂ **ਖਾਲੀ ਜਵਾਬ** ਸਨ ਜਦੋਂ reasoning ਨੇ token budget ਖਤਮ ਕੀਤਾ, ਫਿਰ ਉਹ ਜਵਾਬ ਜੋ retrieved context ਨੂੰ ਅਣਡਿੱਠਾ ਕਰਦੇ ਜਾਂ ਸਰੋਤ ਛੱਡਦੇ ਸਨ। ਸ਼ਬਦ-ਹੱਦ ਜਾਂ bullets ਵੱਧ ਹੋਣ ਉੱਤੇ ਵੀ text ਦਿੱਸਿਆ, ਪਰ airtime ਵਿਅਰਥ ਹੋਇਆ। ਇਹ mechanical checks ਹਨ, ਜਵਾਬ ਪੜ੍ਹਨ ਦੀ ਥਾਂ ਨਹੀਂ; ਇਹ ਤੱਥਾਂ ਦੀ ਸਹੀਤਾ ਜਾਂ safety ਸਲਾਹ ਦੀ ਗੁਣਵੱਤਾ ਸਾਬਤ ਨਹੀਂ ਕਰਦੇ।

#### Pi 5 ਦੇ repeated compliance ਨਤੀਜੇ

ਪਹਿਲਾਂ ਹਰ ਮਾਡਲ ਲਈ ਤੈਨਾਤ system prompt ਅਤੇ **220-token cap** ਨਾਲ ਛੇ prompts ਇਕ ਵਾਰ ਚਲਾਏ। ਸੰਭਾਵੀ ਮਾਡਲ ਨੂੰ ਵੱਖਰੇ seed ਨਾਲ ਦੋ ਵਾਰ ਹੋਰ ਪਰਖਿਆ, ਅਰਥਾਤ **ਹਰ ਮਾਡਲ ਲਈ 18 ਜਵਾਬ**। ਇਕ ਵਾਰ ਦੀ ਪੂਰੀ ਸਫਲਤਾ repeated ਸਫਲਤਾ ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ ਸੀ। ਹੇਠਲੇ repeated ਨਤੀਜੇ ਛੋਟੇ mesh ਜਵਾਬਾਂ ਦੀ ਪੱਕੀ ਤੁਲਨਾ ਦਿੰਦੇ ਹਨ:

| ਮਾਡਲ | ਜਵਾਬ ਜਿਨ੍ਹਾਂ ਨੇ ਹਰ ਜਾਂਚਿਆ ਨਿਯਮ ਮੰਨਿਆ | ਮੁੱਖ ਦੇਖੀਆਂ ਗਲਤੀਆਂ |
|---|---:|---|
| Import ਕੀਤਾ LFM2.5-1.2B | 16/18 (89%) | ਦੋ ਅਧੂਰੇ ਜਵਾਬ |
| `gemma3:1b` | 15/18 (83%) | ਤਿੰਨ ਅਧੂਰੇ ਜਵਾਬ |
| Import ਕੀਤਾ LFM2.5-230M | 14/18 (78%) | ਅਧੂਰੇ ਜਵਾਬ ਅਤੇ source name ਗੁੰਮ |
| Import ਕੀਤਾ LFM2.5-350M | 13/18 (72%) | source name ਗੁੰਮ |
| `qwen2.5:0.5b` | 11/18 (61%) | ਵੱਧ bullets ਅਤੇ ਸ਼ਬਦ, source name ਗੁੰਮ |

**2 GB Pi 4** ਉੱਤੇ ਵੱਖਰੇ ਛੇ-prompt compliance pass ਵਿੱਚ LFM2.5-350M ਨੂੰ **5/6**, LFM2.5-230M ਨੂੰ **4/6** ਅਤੇ Qwen2.5-0.5B ਨੂੰ **2/6** ਮਿਲੇ। MiniCPM5-1B default reasoning ਨਾਲ **1/6** ਤੋਂ reasoning ਬੰਦ ਕਰਕੇ **5/6** ਹੋਇਆ। Pi 4 ਦੇ ਇਹ ਸਕੋਰ ਇਕੋ pass ਦੇ ਹਨ; ਇਸ ਲਈ ਆਮ instruction-following ਬਾਰੇ ਗੱਲ ਕਰਦੇ ਹੋਏ repeated Pi 5 ਨਤੀਜੇ ਨੂੰ ਵੱਧ ਤਰਜੀਹ ਦਿੰਦੇ ਹਾਂ, ਅਤੇ Pi 4 run ਨਾਲ ਉਸ ਬੋਰਡ ਦੀ ਸਥਿਰਤਾ ਤੇ ਗਤੀ ਵੇਖਦੇ ਹਾਂ।

ਗਲਤੀਆਂ ਦੇ ਅਸਰ ਵੱਖਰੇ ਹਨ। **ਖਾਲੀ** ਜਵਾਬ ਵਰਤੋਂਕਾਰ ਦੀ ਮਦਦ ਨਹੀਂ ਕਰਦਾ; ਦਿੱਤੀ ਸਮੱਗਰੀ ਨੂੰ ਅਣਡਿੱਠਾ ਕਰਨ ਵਾਲਾ ਜਵਾਬ ਗੁੰਮਰਾਹ ਕਰ ਸਕਦਾ ਹੈ। Source name ਨਾ ਹੋਵੇ ਤਾਂ ਪਾਠਕ attribution ਨਹੀਂ ਜਾਂਚ ਸਕਦਾ। ਵਾਧੂ bullets ਜਾਂ ਸ਼ਬਦ ਮੁੱਖ ਤੌਰ ਉੱਤੇ ਵਾਧੂ 180-character packet ਲੈਂਦੇ ਹਨ। ਅਧੂਰਾ ਵਾਕ truncation ਦਾ ਸੰਕੇਤ ਹੋ ਸਕਦਾ ਹੈ। LFM2.5-230M ਦੀ medical-term ਗਲਤੀ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ mechanical checks ਪਾਸ ਕਰਕੇ ਵੀ ਜਵਾਬ ਗਲਤ ਹੋ ਸਕਦਾ ਹੈ। repeated ਪਰਖੇ ਪੰਜ ਮਾਡਲਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਨੇ ਵੀ ਸਾਰੇ 18 ਜਵਾਬਾਂ ਵਿੱਚ ਹਰ ਨਿਯਮ ਨਹੀਂ ਮੰਨਿਆ। ਸਖ਼ਤ length ਜਾਂ format ਲੋੜ ਵਾਲੀ ਐਪ generation ਮਗਰੋਂ ਵੀ ਇਸਨੂੰ ਲਾਗੂ ਕਰੇ ਅਤੇ high-stakes content ਵੱਖਰੇ ਤੌਰ ਉੱਤੇ ਜਾਂਚੇ।

ਅਸੀਂ retrieved WikiMed context ਨਾਲ ਅਸਲੀ bridge endpoint, Ollama ਦੇ OpenAI-compatible `/v1/chat/completions`, ਦੀ ਵੀ ਜਾਂਚ ਕੀਤੀ। Pi 5 ਉੱਤੇ LFM2.5-1.2B ਨੇ ਦਿੱਤੇ ਛੇ term ਵਰਤ ਕੇ 28-ਸ਼ਬਦਾਂ ਦਾ ਜਵਾਬ ਦਿੱਤਾ; Qwen2.5-0.5B ਨੇ ਸੱਤ term ਨਾਲ 38 ਸ਼ਬਦ ਦਿੱਤੇ। ਦੋਵੇਂ 180-character ਦੇ ਦੋ packet ਵਿੱਚ ਆ ਗਏ। ਇਹ endpoint check ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ ਕਿ import ਕੀਤਾ LFM2.5 bridge ਦੇ request path ਰਾਹੀਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਪਰ ਇਕ ਸਫਲ ਜਵਾਬ reliability ਦੀ ਗਾਰੰਟੀ ਨਹੀਂ।

Ollama ਵਿੱਚ ਕਈ ready-to-pull ਮਾਡਲ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ [Qwen2.5 ਦੇ 0.5B, 1.5B ਅਤੇ 3B ਰੂਪ](https://ollama.com/library/qwen2.5/tags) ਸ਼ਾਮਲ ਹਨ। ਅਸੀਂ ਛੋਟੇ LFM2.5 ਮਾਡਲ [Liquid AI ਦੇ GGUF releases](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) ਤੋਂ Ollama ਵਿੱਚ import ਕੀਤੇ। Download ਤੋਂ ਪਹਿਲਾਂ ਸਹੀ tag ਜਾਂ GGUF file name ਵੇਖੋ; registry ਅਤੇ repository ਬਦਲ ਸਕਦੇ ਹਨ। GGUF download ਸਥਾਈ ਸਟੋਰੇਜ ਵਿੱਚ ਰੱਖੋ; ਸਾਡੇ ਟੈਸਟ ਵਿੱਚ RAM-backed `/tmp` ਨੇ Pi 4 ਦੀ ਘੱਟ ਮੈਮੋਰੀ ਖਾਧੀ।

### Registry tag ਅਤੇ GGUF import

Ollama tag ਪਹਿਲੇ ਟੈਸਟ ਦਾ ਸਭ ਤੋਂ ਛੋਟਾ ਰਾਹ ਹੈ: ਸਹੀ tag pull ਕਰੋ ਤੇ ਚਲਾਓ। ਟੇਬਲਾਂ ਦੇ ਛੋਟੇ LFM2.5 **GGUF imports** ਸਨ, Ollama ਦੀ ਜਨਤਕ library ਵਿੱਚ `lfm2.5-230m`, `lfm2.5-350m` ਜਾਂ `lfm2.5-1.2b` ਨਾਮ ਦੇ tags ਨਹੀਂ। GGUF model-file format ਹੈ; `Q8_0` ਅਤੇ `Q4_K_M` ਵਰਗੇ ਨਾਮ quantization ਚੋਣਾਂ ਦੱਸਦੇ ਹਨ। ਵਰਤੀਆਂ 230M ਅਤੇ 350M LFM2.5 ਫਾਈਲਾਂ Q8_0 ਸਨ, ਜਦਕਿ 1.2B ਫਾਈਲ Q4_K_M ਸੀ। ਇਸ ਲਈ ਹੋਰ quantization ਵਿੱਚ ਉਹੀ parameter count ਹੋਣ ਨਾਲ ਫਾਈਲ ਆਕਾਰ, memory use ਜਾਂ quality ਇੱਕੋ ਨਹੀਂ ਰਹਿੰਦੀ।

ਜਾਂਚੇ 350M variant ਨੂੰ import ਕਰਨ ਲਈ GGUF ਨੂੰ ਸਥਾਈ ਸਟੋਰੇਜ ਦੇ directory ਵਿੱਚ download ਕਰੋ, ਉਸ path ਵਾਲਾ Modelfile ਬਣਾਓ ਅਤੇ Ollama ਨੂੰ model store ਵਿੱਚ copy ਕਰਨ ਦਿਓ:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Import ਨੂੰ download ਕੀਤੀ ਫਾਈਲ ਅਤੇ Ollama ਦੀ store ਕੀਤੀ copy, ਦੋਹਾਂ ਲਈ ਅਸਥਾਈ ਥਾਂ ਚਾਹੀਦੀ ਹੈ। ਲੰਮਾ GGUF transfer ਕਦੇ-ਕਦੇ ਟੁੱਟਣ ਕਰਕੇ resumable download ਵਰਤੀ। Import ਤੋਂ ਪਹਿਲਾਂ download ਦਾ SHA-256 source ਵੱਲੋਂ ਦਿੱਤੇ hash ਨਾਲ ਮਿਲਾਓ; ਅਧੂਰਾ transfer ਮਾਡਲ ਦੀ ਸਮੱਸਿਆ ਜਿਹਾ ਲੱਗ ਸਕਦਾ ਹੈ। ਸਾਡੇ Pi ਉੱਤੇ `/tmp` RAM-backed ਸੀ, ਇਸ ਲਈ ਉੱਥੇ GGUF ਰੱਖਣ ਨਾਲ inference ਲਈ ਮੈਮੋਰੀ ਘਟੀ।

## ਵਰਤੋਂਯੋਗ ਸ਼ੁਰੂਆਤ

| ਹਾਰਡਵੇਅਰ ਅਤੇ ਮਕਸਦ | ਪਹਿਲਾਂ ਅਜ਼ਮਾਉਣ ਵਾਲਾ ਮਾਡਲ | ਕਾਰਨ |
|---|---|---|
| 2 GB Pi 4, default | Import ਕੀਤਾ LFM2.5-350M | 516 MB RSS ਉੱਤੇ ਸਥਿਰ ਅਤੇ ਲਗਭਗ 1 GB ਉਪਲਬਧ; 230M ਦੀ medical-term ਗਲਤੀ ਮਗਰੋਂ ਚੁਣਿਆ |
| 2 GB Pi 4, ਸਭ ਤੋਂ ਘੱਟ latency | Import ਕੀਤਾ LFM2.5-230M | 383 MB RSS ਅਤੇ ਔਸਤ reply 7.2 s; health ਜਾਂ safety ਸਵਾਲਾਂ ਵਿੱਚ content ਧਿਆਨ ਨਾਲ ਜਾਂਚੋ |
| 2 GB Pi 4, registry-only | `qwen2.5:0.5b` | Ollama ਤੋਂ ਸਿੱਧਾ pull ਅਤੇ Pi 4 ਦੇ ਪੰਜ-prompt run ਵਿੱਚ ਸਥਿਰ; Pi 5 ਉੱਤੇ repeated compliance 61% |
| 4 GB Pi 4 ਜਾਂ Pi 5 | Import ਕੀਤਾ LFM2.5-1.2B, ਫਿਰ ਸਥਾਨਕ ਜਾਂਚ | 8 GB Pi 5 ਉੱਤੇ 967 MB RSS ਅਤੇ 89% repeated compliance; 4 GB variant ਸਿੱਧਾ ਨਹੀਂ ਮਾਪਿਆ |
| 8 GB Pi 5, responsive assistant | Import ਕੀਤਾ LFM2.5-1.2B | 15.5 tokens/s, ਪੂਰਾ ਜਵਾਬ 4.7 s ਅਤੇ ਸਭ ਤੋਂ ਉੱਚੀ ਮਾਪੀ repeated compliance |
| 8 GB Pi 5, registry-only setup | `gemma3:1b` | 11.2 tokens/s, 1,262 MB RSS ਅਤੇ 83% repeated compliance |
| 8 GB Pi 5, ਵੱਡਾ text model ਅਜ਼ਮਾਉਣਾ | Quantized Qwen2.5 3B ਜਾਂ Llama 3.2 3B | ਦੋਵੇਂ ਲਗਭਗ 5 tokens/s ਉੱਤੇ ਚਲੇ ਅਤੇ 2.4–2.8 GB RSS ਵਰਤੀ; Qwen2.5 3B ਨੇ ਇਕ compliance pass ਵਿੱਚ 5/6 ਪਾਏ |

ਇਹ ਚੋਣਾਂ ਅਜਿਹੇ Pi ਉੱਤੇ ਛੋਟੇ ਲਾਭਦਾਇਕ ਜਵਾਬ ਪਹਿਲ ਦਿੰਦੀਆਂ ਹਨ ਜੋ ਹੋਰ ਸੇਵਾਵਾਂ ਵੀ ਚਲਾ ਸਕਦਾ ਹੈ। ਇਹ ਸ਼ੁਰੂਆਤੀ ਚੋਣਾਂ ਹਨ, ਹਰ ਕੰਮ ਲਈ ਇਕ ਮਾਡਲ ਵਧੀਆ ਹੋਣ ਦਾ ਦਾਅਵਾ ਨਹੀਂ। Pi 5 ਦੇ single-pass compliance check ਵਿੱਚ default reasoning ਵਾਲੇ `qwen3.5:0.8b` ਅਤੇ Spark-X2.5 ਨੇ compliant ਜਵਾਬ ਨਹੀਂ ਦਿੱਤੇ; MiniCPM5-1B ਨੇ 1/6 ਕੀਤਾ। ਜੇ client reasoning ਬੰਦ ਨਹੀਂ ਕਰ ਸਕਦਾ ਤਾਂ ਇਸ ਛੋਟੇ-ਜਵਾਬ ਕੰਮ ਲਈ ਇਨ੍ਹਾਂ ਤੋਂ ਬਚੋ। ਅੰਤਿਮ ਮਾਡਲ ਨੂੰ ਅਸਲ prompt, context length, concurrency ਅਤੇ ਯੋਜਿਤ response limit ਨਾਲ ਜਾਂਚੋ।

Registry model ਲਈ [Linux ਵਾਸਤੇ Ollama install](https://ollama.com/download/linux) ਕਰਨ ਮਗਰੋਂ ਚਲਾਓ:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

ਆਪਣੇ prompts, ਮਨਚਾਹੀ ਜਵਾਬ ਲੰਬਾਈ ਅਤੇ ਹੋਰ ਚੱਲਦੀਆਂ ਸੇਵਾਵਾਂ ਨਾਲ ਟੈਸਟ ਕਰੋ। ਪੂਰਾ reply ਸਮਾਂ ਅਤੇ memory use ਦਰਜ ਕਰੋ। ਇਹ parameter count ਇਕੱਲੇ ਨਾਲੋਂ ਵਧੀਆ ਦੱਸਦਾ ਹੈ ਕਿ ਮਾਡਲ Pi ਲਈ ਠੀਕ ਹੈ ਜਾਂ ਨਹੀਂ।

ਘੱਟ ਮੈਮੋਰੀ ਵਾਲੇ node ਉੱਤੇ ਟੈਸਟ ਕਰਦੇ ਸਮੇਂ swap ਵੇਖੋ। ਵੱਡਾ ਮਾਡਲ ਬੋਰਡ ਨੂੰ ਬੇਜਵਾਬ ਕਰੇ ਤਾਂ ਛੋਟਾ ਮਾਡਲ ਵਰਤੋ ਅਤੇ Ollama service ਲਈ ਢੁਕਵੀਂ memory limit ਰੱਖੋ, ਤਾਂ ਜੋ ਬੇਹੱਦ ਵੱਡਾ load host ਦੀ ਮੈਮੋਰੀ ਖਤਮ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਫੇਲ੍ਹ ਹੋਵੇ। Service cap ਸੁਰੱਖਿਆ ਹੈ, ਵੱਡਾ ਮਾਡਲ ਫਿੱਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਨਹੀਂ। ਸਾਡੇ Pi 4 reboot ਦਿਖਾਉਂਦੇ ਹਨ ਕਿ tokens per second ਦੇ ਨਾਲ responsiveness ਅਤੇ memory headroom ਵੀ ਚੋਣ ਦੇ ਮਾਪਦੰਡ ਹਨ।

## Benchmark ਨੂੰ deployment ਫੈਸਲੇ ਵਿੱਚ ਬਦਲੋ

ਮਾਡਲ ਨੂੰ ਰੋਜ਼ਾਨਾ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਚਾਰ ਹੱਦਾਂ ਲਿਖੋ: **ਵੱਧ ਤੋਂ ਵੱਧ ਜਵਾਬ ਸਮਾਂ, ਵੱਧ ਤੋਂ ਵੱਧ resident memory, response format ਅਤੇ failure behavior**। ਉਸੇ ਬੋਰਡ ਨਾਲ ਸਾਂਝੀਆਂ ਸੇਵਾਵਾਂ ਚਲਦਿਆਂ ਇਹ ਹੱਦਾਂ ਜਾਂਚੋ। ਇਕੱਲੇ ਪਾਸ ਹੋਣ ਪਰ radio bridge ਜਾਂ dashboard ਨਾਲ swap ਕਰਾਉਣ ਵਾਲਾ ਮਾਡਲ deployment ਲੋੜ ਪੂਰੀ ਨਹੀਂ ਕਰਦਾ।

ਇਕ ਛੋਟਾ fallback ਮਾਡਲ install ਰੱਖੋ। ਮੁੱਖ ਮਾਡਲ memory limit ਪਾਰ ਕਰੇ, ਖਾਲੀ reply ਦੇਵੇ ਜਾਂ response contract ਤੋੜੇ ਤਾਂ ਉਸ ਵੱਲ ਬਦਲੋ। ਹਰ ਤੁਲਨਾ ਵਿੱਚ model tag, quantization, Ollama version, prompt, context length ਅਤੇ seed ਦਰਜ ਕਰੋ ਤਾਂ ਕਿ ਅਗਲਾ model update hardware ਸੁਧਾਰ ਨਾ ਲੱਗੇ।
