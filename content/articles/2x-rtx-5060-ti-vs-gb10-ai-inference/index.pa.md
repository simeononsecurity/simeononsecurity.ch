---
title: "2x RTX 5060 Ti ਬਨਾਮ GB10: 256K ਸੰਦਰਭ ’ਤੇ ਪੰਜ ਮਾਡਲਾਂ ਦਾ ਸਥਾਨਕ AI ਬੈਂਚਮਾਰਕ"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "ਪੰਜ ਮਾਡਲਾਂ ਦੀ RTX 5060 Ti ਅਤੇ GB10 ਤੁਲਨਾ, ਨਾਲ ਹੀ 256K ਸੰਦਰਭ ਤੱਕ ਇੱਕੋ ਹੋਸਟ ’ਤੇ Qwen3.8 Flash-Next Strata ਬੈਂਚਮਾਰਕ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਸਥਾਨਕ AI", "GPU ਹਾਰਡਵੇਅਰ", "ਬੈਂਚਮਾਰਕਿੰਗ", "ਕੰਪਿਊਟਰ ਹਾਰਡਵੇਅਰ"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "ਸਥਾਨਕ LLM", "ਸਥਾਨਕ ਇਨਫ਼ਰੈਂਸ", "ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ", "VRAM", "GPU ਬੈਂਚਮਾਰਕ", "ਲੰਮਾ ਸੰਦਰਭ", "PCIe ਓਵਰਹੈੱਡ", "AI ਹਾਰਡਵੇਅਰ", "NVIDIA Blackwell", "LLM ਕਾਰਗੁਜ਼ਾਰੀ", "GPU ਮੈਮੋਰੀ"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "ਖੱਬੇ ਪਾਸੇ ਦੋ NVIDIA RTX 5060 Ti ਗ੍ਰਾਫ਼ਿਕਸ ਕਾਰਡ ਅਤੇ ਸੱਜੇ ਪਾਸੇ NVIDIA GB10 ਸਿਸਟਮ ਦੀ ਤਸਵੀਰ, ਦੋਵੇਂ ਗੂੜ੍ਹੇ ਰੰਗ ਦੀ ਪਿੱਠਭੂਮੀ ’ਤੇ ਚਮਕਦਾਰ ਰੰਗਾਂ ਨਾਲ ਦਿਖਾਏ ਗਏ ਹਨ।"
coverCaption: "ਸਥਾਨਕ ਮਾਡਲ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਮੈਮੋਰੀ ਆਰਕੀਟੈਕਚਰ, ਮਾਡਲ ਦੀ ਚੋਣ ਅਤੇ ਸੰਦਰਭ ਦੀ ਲੰਬਾਈ ’ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।"
---

**ਦੋ RTX 5060 Ti 16 GB ਕਾਰਡਾਂ ਵਿੱਚ ਕੁੱਲ 32 GB VRAM ਹੁੰਦੀ ਹੈ।** NVIDIA GB10 ਸਿਸਟਮ ਵਿੱਚ 128 GB ਇਕਸਾਰ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਹੈ। ਪੰਜ ਮਾਡਲਾਂ ਦਾ ਨਵਾਂ ਬੈਂਚਮਾਰਕ ਪਹਿਲਾਂ ਦੇ ਸਿਰਫ਼ Qwen ਟੈਸਟ ਨਾਲੋਂ ਵਧੇਰੇ ਸੰਤੁਲਿਤ ਨਤੀਜਾ ਦਿਖਾਉਂਦਾ ਹੈ।

256K ਸੈਟਿੰਗ ’ਤੇ ਪੰਜ ਵਿੱਚੋਂ ਚਾਰ ਮਾਡਲਾਂ ਲਈ ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ ਦੀ ਜਨਰੇਸ਼ਨ ਗਤੀ ਵੱਧ ਹੈ। Qwen3.8 27B ’ਤੇ GB10 ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ ਅੱਗੇ ਹੈ ਅਤੇ ਮਾਡਲ, ਸੰਦਰਭ ਅਤੇ ਰਨਟਾਈਮ ਅਲਾਟਮੈਂਟ ਲਈ ਹੋਰ ਮੈਮੋਰੀ ਖਾਲੀ ਰੱਖਦਾ ਹੈ। ਠੀਕ ਚੋਣ ਮਾਡਲ ਅਤੇ ਵਰਕਲੋਡ ’ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।

ਇੱਕ ਵੱਖਰੇ ਇੱਕੋ-ਹੋਸਟ ਟੈਸਟ ਨੇ Strata ’ਤੇ Qwen3.8-Flash-Next IQ2_XS ਦੀ ਤੁਲਨਾ Ollama ’ਤੇ dense Qwen3.8 27B Q4_K_M ਨਾਲ ਕੀਤੀ। ਵਾਰਮਅੱਪ ਤੋਂ ਬਾਅਦ Flash-Next ਦੀ ਜਨਰੇਸ਼ਨ ਮੀਡੀਅਨ 92.8 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਸੀ ਅਤੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ 260,446 ਟੋਕਨ ਸਨ। Dense Qwen3.8 ਨੇ 260,444 ਟੋਕਨ ਦੇ ਪ੍ਰਾਂਪਟ ਨਾਲ 0.939 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਹਾਸਲ ਕੀਤੇ।

NVIDIA GB10 ਵਿੱਚ 128 GB ਇਕਸਾਰ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਹੈ। NVIDIA GB10 ਪਲੇਟਫ਼ਾਰਮ ਲਈ 128 GB LPDDR5x ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਅਤੇ 140 W ਚਿੱਪ TDP ਦੱਸਦਾ ਹੈ। RTX 5060 Ti ਵਿੱਚ ਹਰ ਕਾਰਡ ’ਤੇ 16 GB GDDR7, 128-bit ਮੈਮੋਰੀ ਇੰਟਰਫ਼ੇਸ ਅਤੇ 180 W ਕੁੱਲ ਗ੍ਰਾਫ਼ਿਕਸ ਪਾਵਰ ਹੈ। [NVIDIA RTX 5060 Ti ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) ਅਤੇ [NVIDIA GB10 ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) ਹਾਰਡਵੇਅਰ ਦਾ ਫ਼ਰਕ ਦੱਸਦੀਆਂ ਹਨ।

**ਦੋਵੇਂ ਸਿਸਟਮ ਮੈਮੋਰੀ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਦਿੰਦੇ ਹਨ।** ਦੋ ਕਾਰਡ ਦੋ ਵੱਖਰੇ 16 GB ਪੂਲ ਬਣਾਉਂਦੇ ਹਨ। GB10 ਮਾਡਲ, ਸੰਦਰਭ ਡੇਟਾ, ਰਨਟਾਈਮ ਬਫ਼ਰ ਅਤੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੇ ਅਲਾਟਮੈਂਟ ਇੱਕ ਸਾਂਝੇ ਐਡਰੈੱਸ ਸਪੇਸ ਵਿੱਚ ਰੱਖਦਾ ਹੈ।

## ਮੈਮੋਰੀ ਦੀ ਤੁਲਨਾ

| ਸਿਸਟਮ | ਮੈਮੋਰੀ | ਮੈਮੋਰੀ ਮਾਡਲ | ਦਰਜ ਪਾਵਰ ਅੰਕੜਾ |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB ਕੁੱਲ | GPU ਮੈਮੋਰੀ ਦੇ ਦੋ ਵੱਖਰੇ ਪੂਲ | GPU ਲਈ ਕੁੱਲ 360 W |
| **GB10 ਸਿਸਟਮ** | 128 GB | ਇਕਸਾਰ ਯੂਨੀਫ਼ਾਈਡ ਸਿਸਟਮ ਮੈਮੋਰੀ | 140 W GB10 TDP |

GB10 ਹਰ throughput ਟੈਸਟ ਇਸ ਕਰਕੇ ਨਹੀਂ ਜਿੱਤਦਾ ਕਿ LPDDR5x ਮੈਮੋਰੀ ਵੱਖਰੇ GPU ਦੀ ਬੈਂਡਵਿਡਥ ਨਾਲ ਮੇਲ ਖਾਂਦੀ ਹੈ। ਇਸ ਦਾ ਫ਼ਾਇਦਾ ਸਮਰੱਥਾ ਅਤੇ ਡੇਟਾ ਦੀ ਸਥਿਤੀ ਤੋਂ ਆਉਂਦਾ ਹੈ। CPU ਅਤੇ GPU ਇੱਕੋ ਐਡਰੈੱਸ ਸਪੇਸ ਸਾਂਝਾ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਵਰਕਿੰਗ ਸੈੱਟ ਨੂੰ ਦੋ ਵੱਖਰੇ 16 GB ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਫਿੱਟ ਹੋਣ ਦੀ ਲੋੜ ਨਹੀਂ।

ਦੋ-ਕਾਰਡ ਸਿਸਟਮ ਨੂੰ ਡੇਟਾ ਰੱਖਣ ਦੀ ਸਮੱਸਿਆ ਆਉਂਦੀ ਹੈ। ਮਾਡਲ ਦੋਵੇਂ ਕਾਰਡਾਂ ’ਤੇ ਵੰਡਣਾ ਪੈਂਦਾ ਹੈ। ਰਨਟਾਈਮ ਨੂੰ ਉਨ੍ਹਾਂ ਵਿਚਕਾਰ ਡੇਟਾ ਭੇਜਣਾ ਪੈਂਦਾ ਹੈ। PCIe ਟ੍ਰੈਫ਼ਿਕ ਲੇਟੈਂਸੀ ਵਧਾਉਂਦਾ ਅਤੇ ਬੈਂਡਵਿਡਥ ਵਰਤਦਾ ਹੈ। NVIDIA ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਮੁਤਾਬਕ RTX 5060 Ti NVLink ਦਾ ਸਮਰਥਨ ਵੀ ਨਹੀਂ ਕਰਦਾ।

## ਪੰਜ ਮਾਡਲਾਂ ਦਾ ਬੈਂਚਮਾਰਕ

ਅਪਡੇਟ ਕੀਤੇ ਟੈਸਟ ਨੇ ਦੋਵੇਂ ਸਿਸਟਮਾਂ ’ਤੇ ਇੱਕੋ request matrix ਚਲਾਈ। ਇਸ ਵਿੱਚ ਪੰਜ Ollama ਮਾਡਲ 4K, 16K, 32K, 64K, 128K ਅਤੇ 256K ਸੰਦਰਭ ਸੈਟਿੰਗਾਂ ’ਤੇ ਸਨ। ਹਰ request ਨੇ temperature 0 ’ਤੇ 128 ਟੋਕਨ ਬਣਾਏ।

ਟੈਸਟ ਕੀਤੇ ਮਾਡਲ ਟੈਗ ਇਹ ਸਨ:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਵਿੱਚ ਦੋ RTX 5060 Ti 16 GB ਕਾਰਡ ਸਨ। GB10 ਸਿਸਟਮ ਵਿੱਚ 128 GB ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਸੀ। ਟੈਸਟ Ollama ਨਾਲ ਚਲੇ। ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ’ਤੇ ਵਰਜਨ 0.34.2 ਅਤੇ GB10 ’ਤੇ 0.40.2 ਸੀ।

### ਜਨਰੇਸ਼ਨ ਗਤੀ

ਜਨਰੇਸ਼ਨ ਗਤੀ ਦੱਸਦੀ ਹੈ ਕਿ ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸਿੰਗ ਤੋਂ ਬਾਅਦ ਮਾਡਲ ਕਿੰਨੀ ਤੇਜ਼ੀ ਨਾਲ ਟੋਕਨ ਬਣਾਉਂਦਾ ਹੈ। ਇੰਟਰਐਕਟਿਵ ਗੱਲਬਾਤ ਲਈ ਇਹ ਅੰਕੜਾ ਸਭ ਤੋਂ ਅਹਿਮ ਹੁੰਦਾ ਹੈ।

ਦੋ RTX 5060 Ti ਵਾਲਾ ਸਿਸਟਮ:

| ਸੰਦਰਭ | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| ਸੰਦਰਭ | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

256K ’ਤੇ ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ GPT-OSS, Nemotron, Qwen3.5 ਅਤੇ Qwen3.6 ਲਈ ਤੇਜ਼ ਜਨਰੇਸ਼ਨ ਕਰਦਾ ਹੈ। Qwen3.8 ਲਈ GB10 ਤੇਜ਼ ਹੈ। ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ’ਤੇ Qwen3.8 ਦੀ ਗਤੀ 1.079 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਤੱਕ ਡਿੱਗੀ, ਜਦਕਿ GB10 ਨੇ 22.371 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਦਿੱਤੇ।

Qwen3.6 ਦੇ ਨਤੀਜੇ ਨੇੜੇ ਹਨ। ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਨੇ 67.159 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਅਤੇ GB10 ਨੇ 62.115 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਦਿੱਤੇ। ਇਹ ਨਤੀਜੇ ਨਾ ਇਹ ਸਾਬਤ ਕਰਦੇ ਹਨ ਕਿ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਹਮੇਸ਼ਾ ਜਿੱਤਦੀ ਹੈ, ਨਾ ਇਹ ਕਿ ਦੋ discrete GPU ਹਮੇਸ਼ਾ ਜਿੱਤਦੇ ਹਨ।

### ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸਿੰਗ ਗਤੀ

ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸਿੰਗ ਦੱਸਦੀ ਹੈ ਕਿ ਜਨਰੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਰਨਟਾਈਮ ਇਨਪੁੱਟ ਸੰਦਰਭ ਕਿੰਨੀ ਤੇਜ਼ੀ ਨਾਲ ਪੜ੍ਹਦਾ ਹੈ। ਲੰਮੇ ਦਸਤਾਵੇਜ਼ਾਂ ਅਤੇ ਵਾਰ-ਵਾਰ ਸੰਦਰਭ ਮੁੜ ਲੋਡ ਕਰਨ ਲਈ ਇਹ ਮਹੱਤਵਪੂਰਨ ਹੈ।

ਦੋ RTX 5060 Ti ਵਾਲਾ ਸਿਸਟਮ:

| ਸੰਦਰਭ | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| ਸੰਦਰਭ | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

256K ’ਤੇ ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ GPT-OSS ਅਤੇ Qwen3.5 ਦੀ ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸਿੰਗ ਵਿੱਚ ਅੱਗੇ ਸੀ। GB10 Nemotron, Qwen3.6 ਅਤੇ Qwen3.8 ਵਿੱਚ ਅੱਗੇ ਸੀ। ਮੈਮੋਰੀ ਇੰਟਰਫ਼ੇਸ ਜਿੰਨਾ ਹੀ ਮਾਡਲ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਰਨਟਾਈਮ ਵਿਹਾਰ ਵੀ ਮਹੱਤਵ ਰੱਖਦੇ ਹਨ।

## ਵਾਧੂ Qwen3.8 Flash-Next ਬੈਂਚਮਾਰਕ

ਤਿੰਨ ਵਾਧੂ ਰਨਾਂ ਨੇ ਦੋ RTX 5060 Ti ਸਿਸਟਮ ’ਤੇ Qwen3.8 Flash-Next GGUF ਪੈਕੇਜਾਂ ਨੂੰ 4K ਅਤੇ 16K ਸੰਦਰਭ ਸੈਟਿੰਗਾਂ ’ਤੇ ਮਾਪਿਆ। ਹਰ ਕਤਾਰ ਵਿੱਚ ਸਹੀ Hugging Face ਮਾਡਲ ਹਵਾਲਾ ਅਤੇ quantization ਦਿੱਤੀ ਹੈ।

| ਸਹੀ ਮਾਡਲ | Quantization | 4K ਜਨਰੇਸ਼ਨ | 16K ਜਨਰੇਸ਼ਨ |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

ਇਸ ਸਮੂਹ ਵਿੱਚ IQ2_XS ਪੈਕੇਜ ਦੀ throughput ਸਭ ਤੋਂ ਵੱਧ ਸੀ। 4K ’ਤੇ ਇਸ ਦਾ ਨਤੀਜਾ 31.77 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਸੀ, ਜਦਕਿ IQ3_S ਲਈ 24.54 ਅਤੇ Q4_K_M ਲਈ 17.91 ਸੀ। 16K ’ਤੇ ਵੀ ਇਹੀ ਕ੍ਰਮ 28.20, 22.60 ਅਤੇ 17.02 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਰਿਹਾ।

Ollama ਵਿੱਚ ਉਹੀ ਸਹੀ ਮਾਡਲ ਹਵਾਲੇ ਚਲਾਓ:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

ਇਹ ਪਹਿਲਾਂ ਦੇ ਵਾਧੂ ਨਤੀਜੇ ਦੋਹਰੇ-GPU ਸਿਸਟਮ ਦੇ ਹਨ। ਇਹ ਉੱਪਰ ਦਿੱਤੀ ਮਿਲਦੀ RTX 5060 Ti ਅਤੇ GB10 request matrix ਤੋਂ ਵੱਖਰੇ ਹਨ। ਰਿਕਾਰਡ ਵਿੱਚ ਸਹੀ ਮਾਡਲ ਹਵਾਲੇ, quantization, ਮੰਗੀਆਂ ਸੰਦਰਭ ਸੈਟਿੰਗਾਂ ਅਤੇ ਜਨਰੇਸ਼ਨ ਗਤੀ ਦਰਜ ਹਨ। ਇਸ ਵਿੱਚ resolved manifest digest, ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਪ੍ਰਾਂਪਟ ਟੋਕਨ, ਆਉਟਪੁੱਟ ਲੰਬਾਈ, warm state, ਡਿਵਾਈਸ split, CPU, ਸਿਸਟਮ RAM, ਕੂਲਿੰਗ ਸੈੱਟਅੱਪ ਜਾਂ ਮਾਪ ਦੀ ਤਾਰੀਖ ਨਹੀਂ ਹੈ।

## 256K ’ਤੇ Strata ਬਨਾਮ dense Ollama

**14 ਅਕਤੂਬਰ 2026 ਦੇ ਦੂਜੇ ਬੈਂਚਮਾਰਕ ਨੇ ਇੱਕੋ ਦੋਹਰੇ RTX 5060 Ti ਹੋਸਟ ’ਤੇ ਦੋ ਮਾਡਲ ਅਤੇ ਰਨਟਾਈਮ ਸਟੈਕਾਂ ਦੀ ਤੁਲਨਾ ਕੀਤੀ।** Dense baseline ਵਿੱਚ Ollama ’ਤੇ [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b) ਸੀ, ਜੋ Q4_K_M ਵਿੱਚ 27.3 ਅਰਬ ਪੈਰਾਮੀਟਰਾਂ ਵਾਲਾ Qwen35 ਮਾਡਲ ਹੈ। Flash ਸਟੈਕ ਵਿੱਚ Strata unified native pack ਵਾਲਾ [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), Qwen4Exp mixture-of-experts ਮਾਡਲ, ਸੀ।

ਇਹ ਸਟੈਕ-ਪੱਧਰ ਦੀ ਤੁਲਨਾ ਹੈ। ਮਾਡਲ ਆਰਕੀਟੈਕਚਰ, quantization, ਪੈਕੇਜਿੰਗ, expert routing ਅਤੇ inference engine ਇਕੱਠੇ ਬਦਲੇ। IQ3_S ਅਤੇ Q4_K_M Flash ਰੂਪ ਇਸ ਟੈਸਟ ਵਿੱਚ ਸ਼ਾਮਲ ਨਹੀਂ ਸਨ।

### ਟੈਸਟ ਸਿਸਟਮ ਅਤੇ ਤਰੀਕਾ

| ਹਿੱਸਾ | ਦਰਜ ਕੀਤੀ ਸੰਰਚਨਾ |
|---|---|
| **GPU** | 2x NVIDIA GeForce RTX 5060 Ti, ਹਰ ਇੱਕ 16 GiB, compute capability 12.0 |
| **GPU ਲਿੰਕ** | ਹਰ ਕਾਰਡ ਲਈ PCIe 4.0 x4, PHB topology, NVLink ਨਹੀਂ |
| **CPU** | AMD Ryzen 9 5900XT, 32 threads |
| **ਹੋਸਟ ਮੈਮੋਰੀ** | 62 GiB RAM ਅਤੇ 15 GiB swap |
| **NVIDIA ਡਰਾਈਵਰ** | 595.99.02 |

Harness ਨੇ ਨੰਬਰ ਵਾਲੇ synthetic records ਬਣਾਏ। ਹਰ ਕਤਾਰ ਦਾ ਰੂਪ `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` ਸੀ। ਹਦਾਇਤ ਵਿੱਚ ਪਹਿਲਾਂ `BENCHMARK_OK`, ਫਿਰ output limit ਤੱਕ ਛੋਟਾ ਤਕਨੀਕੀ ਸੰਖੇਪ ਮੰਗਿਆ ਗਿਆ। ਛੇ ਪ੍ਰਾਂਪਟਾਂ ਵਿੱਚ 180, 720, 1,500, 3,100, 6,200 ਅਤੇ 12,400 records ਸਨ।

ਹਰ ਰਨ ਵਿੱਚ temperature 0, seed 42 ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ 128 output tokens ਸਨ। ਹਰ ਸੰਦਰਭ ਲਈ ਪੰਜ ਮਾਪੀਆਂ requests ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ warmup ਹੋਇਆ। Ollama ਟੈਸਟਾਂ ਨੇ `/api/generate` ਅਤੇ Strata ਟੈਸਟਾਂ ਨੇ `/v1/chat/completions` ਵਰਤਿਆ। ਸਾਰੀਆਂ ਮਾਪੀਆਂ requests API errors ਤੋਂ ਬਿਨਾਂ ਪੂਰੀਆਂ ਹੋਈਆਂ।

Decode controls ਇੱਕੋ ਜਿਹੇ ਨਹੀਂ ਸਨ। Strata ਨੇ `reasoning_effort` ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ `none` ਰੱਖਿਆ ਅਤੇ ਆਪਣੇ chat template ਰਾਹੀਂ thinking ਬੰਦ ਕੀਤੀ। Dense Ollama request ਨੇ `think: false` ਨਹੀਂ ਭੇਜਿਆ। ਬਾਅਦ ਦੀ ਜਾਂਚ ਵਿੱਚ dense output thinking ਅਤੇ response fields ਵਿੱਚ ਦਿਖਿਆ। ਜਨਰੇਸ਼ਨ ਨਤੀਜੇ ਨੂੰ ਇਨ੍ਹਾਂ decode modes ਤੱਕ ਹੀ ਸੀਮਿਤ ਮੰਨੋ।

| ਸੰਦਰਭ ਸੈਟਿੰਗ | Dense ਪ੍ਰਾਂਪਟ ਟੋਕਨ | Flash ਪ੍ਰਾਂਪਟ ਟੋਕਨ |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

ਦੋਵੇਂ model headers ਵਿੱਚ ਵੱਧ ਤੋਂ ਵੱਧ 262,144-token ਸੰਦਰਭ ਸੀ। ਹਰ checkpoint ’ਤੇ ਜੋੜੇ ਪ੍ਰਾਂਪਟਾਂ ਵਿੱਚ ਦੋ ਟੋਕਨ ਦਾ ਫ਼ਰਕ ਸੀ।

### Warmup ਤੋਂ ਬਾਅਦ ਜਨਰੇਸ਼ਨ ਗਤੀ ਦੀ ਮੀਡੀਅਨ

ਹਰ ਮੀਡੀਅਨ ਵਿੱਚ ਇੱਕ warmup ਤੋਂ ਬਾਅਦ ਪੰਜ ਮਾਪੀਆਂ requests ਹਨ। ਹਰ dense request ਨੇ ਪਿਛਲੇ ਪ੍ਰਾਂਪਟ ਦੇ ਚਾਰ ਟੋਕਨਾਂ ਤੋਂ ਇਲਾਵਾ ਬਾਕੀ ਸਾਰੇ ਟੋਕਨ ਮੁੜ ਵਰਤੇ। ਹਰ Flash request ਨੇ ਸੱਤ ਟੋਕਨਾਂ ਤੋਂ ਇਲਾਵਾ ਬਾਕੀ ਮੁੜ ਵਰਤੇ। ਇਹ ਟੇਬਲ warm, prefix-cached decode throughput ਮਾਪਦੀ ਹੈ। ਇਹ cold end-to-end latency ਨਹੀਂ ਮਾਪਦੀ।

| ਸੰਦਰਭ | Strata ’ਤੇ Flash IQ2_XS | Ollama ’ਤੇ Dense Q4_K_M | Flash ਦੀ ਬੜ੍ਹਤ |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

64K ਤੋਂ 256K ਤੱਕ Flash ਸਟੈਕ ਲਗਭਗ 90 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ’ਤੇ ਰਿਹਾ। Dense Qwen3.8 ਦੀ ਗਤੀ 64K ਤੋਂ ਬਾਅਦ ਤੇਜ਼ੀ ਨਾਲ ਘਟੀ ਅਤੇ 256K ’ਤੇ 0.939 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਤੱਕ ਪਹੁੰਚੀ। 256K Flash ਜਵਾਬ 67 ਟੋਕਨਾਂ ਤੋਂ ਬਾਅਦ ਆਮ ਤਰ੍ਹਾਂ ਮੁਕਿਆ। Dense ਰਨ 128-token output limit ਤੱਕ ਪਹੁੰਚਿਆ।

### ਪਹਿਲੀ request ਦੀ ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸਿੰਗ

| ਸੰਦਰਭ | Flash ਪਹਿਲੀ request | Dense ਪਹਿਲੀ request |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

Dense ਦੀ ਪਹਿਲੀ request ਨੇ ਹਰ checkpoint ’ਤੇ ਪੂਰਾ ਪ੍ਰਾਂਪਟ ਪ੍ਰੋਸੈਸ ਕੀਤਾ। Strata ਨੇ 64K ’ਤੇ 16,384, 128K ’ਤੇ 49,152 ਅਤੇ 256K ’ਤੇ 114,688 prefix tokens ਮੁੜ ਵਰਤੇ। ਇਸ ਲਈ 64K ਤੋਂ 256K ਤੱਕ Flash ਦਰਾਂ ਨੂੰ ਪਹਿਲੀ request ਦੀ continuation throughput ਮੰਨੋ, ਪੂਰੀ ਤਰ੍ਹਾਂ uncached prefill ਨਹੀਂ।

256K ’ਤੇ Strata ਨੇ ਪਹਿਲੀ request 60.8 ਸਕਿੰਟ ਵਿੱਚ ਪ੍ਰੋਸੈਸ ਕੀਤੀ। Ollama ਨੂੰ ਲਗਭਗ 1,215.4 ਸਕਿੰਟ ਲੱਗੇ। Prefix reuse ਕਰਕੇ ਇਸ checkpoint ’ਤੇ cold prefill ਦੀ ਸਿੱਧੀ ਤੁਲਨਾ ਨਹੀਂ ਹੁੰਦੀ।

### ਰਨਟਾਈਮ ਦੀ ਸਥਿਤੀ ਲੰਮੇ-ਸੰਦਰਭ ਦਾ ਫ਼ਰਕ ਸਮਝਾਉਂਦੀ ਹੈ

Ollama 0.34.2 ਨੇ CUDA layer offload, ChatML template ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਚਾਰ draft ਵਾਲੀ MTP speculative decoding ਨਾਲ llama-server 0.4.1-dev ਵਰਤਿਆ। Batch ਅਤੇ microbatch ਆਕਾਰ 32K ’ਤੇ 1,024 ਅਤੇ 64K ਤੋਂ 256K ਤੱਕ 512 ਸਨ। 32K ਅਤੇ 64K ’ਤੇ ਸਾਰੀਆਂ 66 dense layers GPU ’ਤੇ ਰਹੀਆਂ। 128K ’ਤੇ 66 ਵਿੱਚੋਂ 63 layers GPU ’ਤੇ ਰਹੀਆਂ ਅਤੇ 1,404 MiB CPU-mapped ਮੈਮੋਰੀ ਵਿੱਚ ਗਈ। 256K ’ਤੇ 66 ਵਿੱਚੋਂ 42 layers GPU ’ਤੇ ਰਹੀਆਂ ਅਤੇ 6,002 MiB CPU-mapped ਮੈਮੋਰੀ ਵਿੱਚ ਗਈ। 256K MTP acceptance rate ਲਗਭਗ 69.4 ਫ਼ੀਸਦੀ ਸੀ।

Strata 0.1.44.1 ਨੇ CUDA 13.0.3 ਨਾਲ ਆਪਣੀਆਂ 48 layers ਦੋਵੇਂ GPUਆਂ ’ਤੇ ਵੰਡੀਆਂ। 4K ਅਤੇ 16K ਸੰਰਚਨਾ ਵਿੱਚ layers 0 ਤੋਂ 23 ਪਹਿਲੇ GPU ’ਤੇ ਅਤੇ 24 ਤੋਂ 47 ਦੂਜੇ ’ਤੇ ਸਨ। ਇਸ ਟੈਸਟ ਨੇ automatic 700 MiB VRAM reserve ਅਤੇ 16,047 resident expert slots ਵਰਤੇ।

32K ਤੋਂ 256K ਸੰਰਚਨਾ ਵਿੱਚ layers 0 ਤੋਂ 24 ਪਹਿਲੇ GPU ’ਤੇ ਅਤੇ 25 ਤੋਂ 47 ਦੂਜੇ ’ਤੇ ਸਨ। ਇਸ ਟੈਸਟ ਨੇ automatic prefill, 0.5 speculative minimum probability, INT8 KV storage, ਹਰ QSA layer ਲਈ 32,768 resident KV cells, 832 MiB VRAM reserve, 15,318 slots ਅਤੇ 21,024 MiB ਵਾਲਾ expert cache, ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਚਾਰ draft ਵਾਲੀ MTP speculative decoding ਵਰਤੀ।

Strata native ਅਤੇ PLE blob digest `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da` ਸੀ। ਰਨ expert profile ਅਤੇ MTP draft pack ’ਤੇ ਵੀ ਨਿਰਭਰ ਸੀ, ਜਿਨ੍ਹਾਂ ਦੇ immutable digest ਜਾਰੀ ਨਹੀਂ ਕੀਤੇ ਗਏ।

Strata ਰਨ ਨੇ default route-tail skip mode ਵਰਤਿਆ। ਇਹ ਸੈਟਿੰਗ ਮਾਡਲ output ਨੂੰ ਥੋੜ੍ਹਾ ਬਦਲਦੀ ਹੈ ਅਤੇ ਨਤੀਜੇ ਨੂੰ ਦਰਜ runtime configuration ਤੱਕ ਸੀਮਿਤ ਕਰਦੀ ਹੈ। Flash ਜਵਾਬਾਂ ਵਿੱਚ `BENCHMARK_OK` markers ਸਨ। Dense requests ਵਿੱਚ API errors ਨਹੀਂ ਸਨ, ਪਰ ਮੁੱਖ harness ਨੇ marker ਦਰਜ ਨਹੀਂ ਕੀਤਾ। Raw rows ਵਿੱਚ zero response characters ਸਨ। ਬਾਅਦ ਦੀ ਜਾਂਚ ਨੇ response ਅਤੇ thinking fields ਵਿੱਚ output ਲੱਭਿਆ ਅਤੇ response ਵਿੱਚ `BENCHMARK_OK` ਦੀ ਪੁਸ਼ਟੀ ਕੀਤੀ।

4K ਅਤੇ 16K ਸੰਰਚਨਾ ਨੇ ਇੱਕ request ਵਿੱਚ 409 MiB ਖਾਲੀ ਪਾਇਆ ਅਤੇ 832 MiB reserve ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ। ਲੰਮੇ-ਸੰਦਰਭ ਸੰਰਚਨਾ ਨੇ ਇੱਕ request ਵਿੱਚ 481 MiB ਖਾਲੀ ਪਾਇਆ ਅਤੇ 896 MiB reserve ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ। ਦੋਵੇਂ ਮੁੱਲ engine ਦੀ 512 MiB driver-paging ਹੱਦ ਤੋਂ ਹੇਠਾਂ ਸਨ। ਕੋਈ request ਅਸਫ਼ਲ ਨਹੀਂ ਹੋਈ, ਪਰ ਘੱਟ ਮੈਮੋਰੀ repeatability ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ।

**98.9x ਅੰਕੜੇ ਨੂੰ ਪੂਰੇ long-context stack ਦਾ ਨਤੀਜਾ ਮੰਨੋ, ਸਿਰਫ਼ engine ਦੀ 98.9x ਬੜ੍ਹਤ ਦਾ ਸਬੂਤ ਨਹੀਂ।** ਟੈਸਟ ਨੇ ਹੋਸਟ ਨੂੰ ਇਕਸਾਰ ਰੱਖਿਆ। ਇਸ ਨੇ ਮਾਡਲ, quantization ਜਾਂ runtime ਨੂੰ ਵੱਖਰੇ ਤੌਰ ’ਤੇ ਨਹੀਂ ਪਰਖਿਆ।

## ਅਸਲ ਪ੍ਰਾਂਪਟ ਲੰਬਾਈ ਮਹੱਤਵਪੂਰਨ ਹੈ

ਮੰਗਿਆ ਸੰਦਰਭ ਅਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਇੱਕੋ ਨਹੀਂ ਹੁੰਦੇ। 256K ਸੈਟਿੰਗ ’ਤੇ Qwen3.5, Qwen3.6, Nemotron ਅਤੇ Qwen3.8 ਨੇ ਦੋਵੇਂ ਸਿਸਟਮਾਂ ’ਤੇ ਲਗਭਗ 171,359 ਤੋਂ 171,365 ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਪ੍ਰੋਸੈਸ ਕੀਤੇ।

GPT-OSS ਨੇ 256K ਸੈਟਿੰਗ ’ਤੇ ਦੋਵੇਂ ਸਿਸਟਮਾਂ ’ਤੇ 65,538 ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਪ੍ਰੋਸੈਸ ਕੀਤੇ। ਇਸ ਦੀ 256K ਕਤਾਰ ਬਾਕੀ ਮਾਡਲਾਂ ਵਰਗੀ ਇਨਪੁੱਟ ਲੰਬਾਈ ਨਹੀਂ ਦਿਖਾਉਂਦੀ।

256K Qwen3.8 ਨਤੀਜਾ ਸਭ ਤੋਂ ਸਪਸ਼ਟ ਫ਼ਰਕ ਹੈ। ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਨੇ 251.3 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ’ਤੇ 171,359 ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਅਤੇ 1.079 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ’ਤੇ ਜਨਰੇਸ਼ਨ ਕੀਤੀ। GB10 ਨੇ ਉਨੇ ਹੀ ਪ੍ਰਾਂਪਟ ਟੋਕਨ 535.1 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ’ਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਅਤੇ 22.371 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ’ਤੇ ਜਨਰੇਸ਼ਨ ਕੀਤੀ।

**ਸੰਦਰਭ ਸੈਟਿੰਗ ਮੰਗੀ ਹੱਦ ਦੱਸਦੀ ਹੈ।** ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਦੱਸਦੀ ਹੈ ਕਿ runtime ਨੇ ਕਿੰਨਾ ਵਰਕਲੋਡ ਪੂਰਾ ਕੀਤਾ।

## ਕੁੱਲ VRAM ਅਜੇ ਵੀ ਕਿਉਂ ਮਹੱਤਵ ਰੱਖਦੀ ਹੈ

### 1. ਮਾਡਲ ਨੂੰ ਇੱਕ 32 GB ਕਾਰਡ ਨਹੀਂ ਦਿਸਦਾ

ਦੋ GPU ਆਪਣੀ ਮੈਮੋਰੀ ਨੂੰ ਇੱਕ local address space ਵਿੱਚ ਨਹੀਂ ਜੋੜਦੇ। Model-parallel runtime layers ਜਾਂ tensors ਨੂੰ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਵੰਡਦਾ ਹੈ। ਹਰ ਡਿਵਾਈਸ ਨੂੰ ਆਪਣੇ ਨਿਰਧਾਰਤ weights, temporary buffers ਅਤੇ ਸੰਦਰਭ ਸਥਿਤੀ ਦੇ ਹਿੱਸੇ ਲਈ ਥਾਂ ਚਾਹੀਦੀ ਹੈ।

ਵਰਤਣਯੋਗ ਸਮਰੱਥਾ ਸਧਾਰਨ ਜੋੜ ਨਾਲੋਂ ਘੱਟ ਹੁੰਦੀ ਹੈ। ਸਹੀ overhead ਮਾਡਲ format, quantization, inference backend, tensor split ਅਤੇ ਸੰਦਰਭ ਦੀ ਲੰਬਾਈ ’ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।

### 2. ਜਨਰੇਸ਼ਨ ਦੌਰਾਨ ਸੰਦਰਭ ਮੈਮੋਰੀ ਵਧਦੀ ਹੈ

ਮਾਡਲ weights ਮੈਮੋਰੀ ਬਜਟ ਦਾ ਸਿਰਫ਼ ਇੱਕ ਹਿੱਸਾ ਹਨ। Key-value cache, ਜਾਂ KV cache, ਪਹਿਲਾਂ ਦੇ ਟੋਕਨਾਂ ਦਾ attention ਡੇਟਾ ਰੱਖਦਾ ਹੈ। ਲੰਮੇ ਸੰਦਰਭ ਲਈ ਹੋਰ cache ਮੈਮੋਰੀ ਚਾਹੀਦੀ ਹੈ। 4K ਟੈਸਟ 128K ਜਾਂ 256K deployment ਦਾ ਅੰਦਾਜ਼ਾ ਨਹੀਂ ਦਿੰਦਾ।

ਨਵੇਂ ਨਤੀਜੇ ਹਰ ਮਾਡਲ ਲਈ ਵੱਖਰੀ ਸੀਮਾ ਦਿਖਾਉਂਦੇ ਹਨ। 256K ’ਤੇ ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ’ਤੇ Qwen3.8 ਦੀ ਜਨਰੇਸ਼ਨ ਬੁਰੀ ਤਰ੍ਹਾਂ ਡਿੱਗਦੀ ਹੈ। ਹੋਰ ਚਾਰ ਮਾਡਲ ਦੋਵੇਂ ਸਿਸਟਮਾਂ ’ਤੇ ਵਰਤਣਯੋਗ ਜਨਰੇਸ਼ਨ ਗਤੀ ਰੱਖਦੇ ਹਨ। ਸਮਰੱਥਾ ਇਸ ਲਈ ਅਹਿਮ ਹੈ ਕਿ ਇਸ ਨਾਲ ਪਤਾ ਲੱਗਦਾ ਹੈ ਕਿਹੜੇ ਮਾਡਲ ਅਤੇ ਸੰਦਰਭ runtime allocations ਲਈ ਥਾਂ ਛੱਡ ਕੇ ਫਿੱਟ ਹੁੰਦੇ ਹਨ।

### 3. PCIe ਟ੍ਰਾਂਸਫ਼ਰ ਵਾਧੂ ਲਾਗਤ ਜੋੜਦੇ ਹਨ

ਜਦੋਂ runtime GPUਆਂ ਵਿਚਕਾਰ activations ਜਾਂ tensors ਭੇਜਦਾ ਹੈ, ਤਾਂ ਟ੍ਰਾਂਸਫ਼ਰ host interconnect ਰਾਹੀਂ ਲੰਘਦਾ ਹੈ। ਇਸ ਨਾਲ synchronization points ਬਣਦੇ ਅਤੇ ਹਰ ਕਦਮ ’ਤੇ latency ਜੁੜਦੀ ਹੈ। ਅਸਰ tensor placement, ਮਾਡਲ architecture, quantization ਅਤੇ ਸੰਦਰਭ ਦੀ ਲੰਬਾਈ ’ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।

ਇਸ ਦਾ ਮਤਲਬ ਨਹੀਂ ਕਿ ਦੋਹਰਾ-GPU ਸਿਸਟਮ ਬੇਕਾਰ ਹੈ। Runtime configuration ਅਤੇ ਮਾਡਲ ਨਤੀਜਾ ਤੈਅ ਕਰਦੇ ਹਨ। ਸਿਰਫ਼ 4K prompt processing ਦੱਸਣ ਵਾਲਾ ਬੈਂਚਮਾਰਕ ਇਹ ਲਾਗਤ ਨਹੀਂ ਦਿਖਾਉਂਦਾ।

### 4. ਪਾਵਰ ਕੁਸ਼ਲਤਾ ਸਿਸਟਮ-ਪੱਧਰ ਦਾ ਫ਼ਾਇਦਾ ਹੈ

GB10 ਹੋਰ ਮੈਮੋਰੀ ਸਮਰੱਥਾ ਦਿੰਦਾ ਹੋਇਆ ਘੱਟ ਦਰਜ chip ਜਾਂ GPU ਪਾਵਰ ਵਰਤਦਾ ਹੈ। ਦੋ RTX 5060 Ti ਕਾਰਡ ਬਾਕੀ ਸਿਸਟਮ ਤੋਂ ਪਹਿਲਾਂ 360 W ਕੁੱਲ GPU ਪਾਵਰ ਲੈਂਦੇ ਹਨ। NVIDIA GB10 ਲਈ 140 W TDP ਦੱਸਦਾ ਹੈ।

**ਕਈ ਮਾਡਲਾਂ ’ਤੇ peak throughput ਦੇ ਬਦਲੇ GB10 ਵੱਧ ਸਮਰੱਥਾ, ਸਾਂਝਾ working set ਅਤੇ ਘੱਟ ਦਰਜ GPU ਪਾਵਰ ਦਿੰਦਾ ਹੈ।** ਇਸ ਟੈਸਟ ਵਿੱਚ ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ ਕਈ ਨਵੇਂ MoE ਮਾਡਲਾਂ ’ਤੇ ਵੱਧ throughput ਦਿੰਦਾ ਹੈ।

## 5060ti-x2 ਸਿਸਟਮ ਦੀ ਕੀਮਤ ਬਹੁਤ ਘੱਟ ਹੈ

ਦੋ RTX 5060 Ti 16 GB ਵਾਲਾ ਪੂਰਾ workstation 10 ਅਕਤੂਬਰ 2026 ਨੂੰ **$3,479** ’ਤੇ ਸੂਚੀਬੱਧ ਸੀ। ਸੰਰਚਨਾ ਵਿੱਚ Intel Ultra 7 265K, Z890 motherboard, 32 GB DDR5, 1 TB storage, 1,000 W power supply ਅਤੇ ਦੋਵੇਂ GPU ਸ਼ਾਮਲ ਸਨ। [ਪੂਰੇ dual-GPU workstation ਦੀ ਸੂਚੀ ਵੇਖੋ](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)।

NVIDIA ਦਾ US marketplace 128 GB DGX Spark ਨੂੰ **$6,950** ’ਤੇ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ। ਸੂਚੀ ਵਿੱਚ 128 GB ਇਕਸਾਰ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਅਤੇ 4 TB NVMe storage ਹੈ, ਪਰ ਸਿਸਟਮ out of stock ਦਿਖਦਾ ਹੈ। [NVIDIA ਦੀ ਮੌਜੂਦਾ DGX Spark ਸੂਚੀ ਵੇਖੋ](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)।

AMD Ryzen AI Halo Developer Platform ਇੱਕ ਹੋਰ ਤੁਲਨਾ ਦਿੰਦਾ ਹੈ। Micro Center ’ਤੇ ਇਹ Strix Halo ਸਿਸਟਮ 128 GB LPDDR5x ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਅਤੇ 2 TB storage ਸਮੇਤ **$3,999.99** ’ਤੇ ਸੂਚੀਬੱਧ ਹੈ। Strix Halo ਅਕਸਰ GB10 ਵਰਗੀ ਸਥਾਨਕ-AI ਸ਼੍ਰੇਣੀ ਵਿੱਚ ਆਉਂਦਾ ਹੈ, ਹਾਲਾਂਕਿ ਸੁਤੰਤਰ ਟੈਸਟ throughput ਅਤੇ software maturity ਵਿੱਚ GB10 ਨੂੰ ਅਕਸਰ ਅੱਗੇ ਦਿਖਾਉਂਦੇ ਹਨ। [Micro Center ਦੀ ਮੌਜੂਦਾ Linux ਸੂਚੀ ਵੇਖੋ](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) ਅਤੇ [Strix Halo ਬਨਾਮ GB10 ਸਮੀਖਿਆ ਪੜ੍ਹੋ](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)।

| ਪੂਰਾ ਸਿਸਟਮ | 10 ਅਕਤੂਬਰ 2026 ਨੂੰ ਸੂਚੀਬੱਧ ਕੀਮਤ | ਕੀਮਤ ਦਾ ਫ਼ਰਕ |
|---|---:|---:|
| **5060ti-x2 workstation** | $3,479 | ਆਧਾਰ |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 ਵੱਧ |
| **128 GB GB10 DGX Spark** | $6,950 | $3,471 ਵੱਧ |

GB10 ਵੱਡਾ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਪੂਲ ਅਤੇ ਘੱਟ ਦਰਜ GPU ਪਾਵਰ ਦਿੰਦਾ ਹੈ। AMD ਸਿਸਟਮ ਲਗਭਗ $4,000 ’ਤੇ ਉਹੀ 128 GB ਮੈਮੋਰੀ ਸ਼੍ਰੇਣੀ ਦਿੰਦਾ ਹੈ। tax ਅਤੇ shipping ਤੋਂ ਪਹਿਲਾਂ 5060ti-x2 workstation ਦੀ ਕੀਮਤ ਸੂਚੀਬੱਧ GB10 ਕੀਮਤ ਦਾ ਲਗਭਗ **50%** ਹੈ।

ਇਹ ਵੱਖਰੇ ਵਿਕਰੇਤਿਆਂ ਦੀਆਂ ਸੂਚੀਬੱਧ ਕੀਮਤਾਂ ਹਨ, controlled retail basket ਨਹੀਂ। ਤੁਲਨਾ ਵਿੱਚ 5060ti-x2 ਸਿਸਟਮ ਕੋਲ ਘੱਟ system memory ਅਤੇ storage ਵੀ ਹੈ। ਮੌਜੂਦਾ RTX 5060 Ti 16 GB ਕਾਰਡਾਂ ਦੀਆਂ ਸੂਚੀਬੱਧ ਕੀਮਤਾਂ **ਹਰ ਇੱਕ $789 ਤੋਂ $830** ਦੇ ਨੇੜੇ ਹਨ, ਜੋ $429 launch MSRP ਤੋਂ ਕਾਫ਼ੀ ਵੱਧ ਹੈ। GPU ਕੀਮਤਾਂ ਦੇ ਮੌਜੂਦਾ ਵਾਧੇ ਦੌਰਾਨ ਵੀ ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਦੀ ਕੀਮਤ ਦਾ ਫ਼ਾਇਦਾ ਕਾਇਮ ਹੈ। [RTX 5060 Ti ਦੀਆਂ ਮੌਜੂਦਾ ਕੀਮਤਾਂ ਵੇਖੋ](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)。

## ਸਥਾਨਕ AI ਵਰਕਲੋਡਾਂ ਲਈ ਇਸ ਦਾ ਕੀ ਮਤਲਬ ਹੈ

ਦੋ 16 GB ਕਾਰਡਾਂ ਵਾਲਾ ਸੈੱਟਅੱਪ ਲੰਮੇ ਸੰਦਰਭਾਂ ’ਤੇ ਕਈ quantized 27B ਤੋਂ 35B ਮਾਡਲ ਚਲਾਉਂਦਾ ਹੈ। ਬੈਂਚਮਾਰਕ ਹਰ ਮਾਡਲ ਲਈ ਇੱਕੋ ਜੇਤੂ ਨਹੀਂ ਦਿਖਾਉਂਦਾ।

ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ ਚੁਣੋ ਜੇ ਤੁਹਾਨੂੰ ਚਾਹੀਦਾ ਹੈ:

- **ਇਸ ਟੈਸਟ ਵਿੱਚ GPT-OSS, Nemotron, Qwen3.5 ਅਤੇ Qwen3.6 ਲਈ ਵੱਧ ਜਨਰੇਸ਼ਨ ਗਤੀ।**
- **ਪੰਜ ਮਾਡਲਾਂ ’ਤੇ ਛੋਟੇ ਸੰਦਰਭ ਲਈ ਵੱਧ throughput।**
- **ਸੂਚੀਬੱਧ GB10 ਸਿਸਟਮ ਨਾਲੋਂ ਘੱਟ ਖਰੀਦ ਕੀਮਤ।**
- **NVIDIA discrete-GPU software compatibility ਅਤੇ ਹੋਰ ਮਾਡਲ ਅਜ਼ਮਾਉਣ ਦੀ ਗੁੰਜਾਇਸ਼।**

GB10 ਚੁਣੋ ਜੇ ਤੁਹਾਨੂੰ ਚਾਹੀਦਾ ਹੈ:

- **256K ’ਤੇ Qwen3.8 27B**, ਜਿੱਥੇ GB10 ਜਨਰੇਸ਼ਨ ਵਿੱਚ 20 ਗੁਣਾ ਤੋਂ ਵੱਧ ਤੇਜ਼ ਹੈ।
- **ਇੱਕ 128 GB ਮੈਮੋਰੀ ਪੂਲ**, ਜਿਸ ਵਿੱਚ model weights, KV cache ਅਤੇ runtime buffers ਲਈ ਵੱਧ ਥਾਂ ਹੋਵੇ।
- **ਦੋ discrete ਕਾਰਡਾਂ ਨਾਲੋਂ ਘੱਟ ਦਰਜ GPU ਜਾਂ chip ਪਾਵਰ।**
- **ਦੋਹਰੇ-ਕਾਰਡ ਸੈੱਟਅੱਪ ’ਤੇ ਦਬਾਅ ਪਾਉਣ ਵਾਲੇ ਮਾਡਲਾਂ ਲਈ ਘੱਟ multi-device placement ਰੁਕਾਵਟਾਂ।**

ਇਹ [ਕੀ ਗੰਭੀਰ ਸਥਾਨਕ LLM ਕੰਮ ਲਈ 16GB VRAM ਕਾਫ਼ੀ ਹੈ?](/articles/is-16gb-vram-enough-local-llm/) ਦੀ sizing ਸਲਾਹ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ, ਜੋ weights, ਸੰਦਰਭ ਅਤੇ runtime allocations ਨੂੰ ਇੱਕ ਬਜਟ ਮੰਨਦੀ ਹੈ। [Qwen 27B ਲਈ 32GB VRAM ਗਾਈਡ](/articles/32gb-vram-qwen-27b-hardware-guide/) ਦੋਹਰੇ-ਕਾਰਡ ਸੈੱਟਅੱਪ ਲਈ ਇਹੀ ਨਤੀਜਾ ਦਿੰਦੀ ਹੈ। ਕੁੱਲ ਸਮਰੱਥਾ ਵਰਤਣਯੋਗ headroom ਦੇ ਬਰਾਬਰ ਨਹੀਂ।

ਲੰਮੇ ਸੰਦਰਭ ਵਾਲਾ ਹਾਰਡਵੇਅਰ ਖਰੀਦਣ ਤੋਂ ਪਹਿਲਾਂ ਚਾਰ ਸਵਾਲ ਪੁੱਛੋ:

- **ਕੀ ਚੁਣੀ quantization runtime buffers ਸਮੇਤ ਫਿੱਟ ਹੁੰਦੀ ਹੈ?** ਸਿਰਫ਼ model weights ਨਾਲ ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਤੈਅ ਨਹੀਂ ਹੁੰਦੀ।
- **ਕੀ ਸੰਦਰਭ ਬਹੁਤ ਵੱਧ KV-cache ਦਬਾਅ ਤੋਂ ਬਿਨਾਂ ਫਿੱਟ ਹੁੰਦਾ ਹੈ?** ਲੰਮੇ ਪ੍ਰਾਂਪਟ ਨਤੀਜਾ ਬਦਲਦੇ ਹਨ।
- **ਕੀ runtime ਕੁਸ਼ਲ device split ਵਰਤਦਾ ਹੈ?** PCIe ਟ੍ਰਾਂਸਫ਼ਰ ਅਤੇ tensor placement ਹਰ ਬਣੇ ਟੋਕਨ ’ਤੇ ਅਸਰ ਕਰਦੇ ਹਨ।
- **ਕੀ ਸਿਸਟਮ ਨਿਸ਼ਾਨਾ ਸੰਦਰਭ ਪੂਰਾ ਕਰਦਾ ਹੈ?** ਤੇਜ਼ 4K ਨਤੀਜਾ ਅਸਫ਼ਲ 256K ਵਰਕਲੋਡ ਦੀ ਭਰਪਾਈ ਨਹੀਂ ਕਰਦਾ।

**ਨਵਾਂ ਬੈਂਚਮਾਰਕ ਇਹਨਾਂ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਮਾਡਲ ਮੁਤਾਬਕ ਦਿੰਦਾ ਹੈ।** 256K ’ਤੇ Qwen3.8 ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ GB10 ਦੇ ਹੱਕ ਵਿੱਚ ਹੈ। ਇਸ ਖ਼ਾਸ ਸੈੱਟਅੱਪ ਵਿੱਚ ਹੋਰ ਚਾਰ ਮਾਡਲ ਜਨਰੇਸ਼ਨ ਗਤੀ ਲਈ ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਦੇ ਹੱਕ ਵਿੱਚ ਹਨ। ਵੱਧ throughput ਨਾ ਮਿਲਣ ’ਤੇ ਵੀ ਵੱਡਾ ਯੂਨੀਫ਼ਾਈਡ ਮੈਮੋਰੀ ਪੂਲ ਹੋਰ ਸਮਰੱਥਾ ਦਿੰਦਾ ਹੈ।

ਇਸੇ ਦੋਹਰੇ-GPU ਹਾਰਡਵੇਅਰ ਨੇ Strata ’ਤੇ Flash-Next IQ2_XS ਨਾਲ 256K ’ਤੇ ਵਾਰਮਅੱਪ ਤੋਂ ਬਾਅਦ 92.8 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਦੀ ਮੀਡੀਅਨ ਵੀ ਦਰਜ ਕੀਤੀ। ਇਹ ਵੱਖਰਾ ਨਤੀਜਾ dense Qwen3.8 ਅਤੇ GB10 ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਹੀਂ ਬਦਲਦਾ। Flash-Next ਦਾ mixture-of-experts architecture, quantization, package, runtime ਅਤੇ decode mode ਵੱਖਰੇ ਹਨ। ਇਸ ਡੇਟਾਸੈੱਟ ਵਿੱਚ GB10 ’ਤੇ Flash-Next ਦਾ ਮਿਲਦਾ ਨਤੀਜਾ ਨਹੀਂ ਹੈ।

## ਫ਼ੈਸਲਾ

**256K ’ਤੇ ਟੈਸਟ ਕੀਤੇ ਪੰਜ ਵਿੱਚੋਂ ਚਾਰ ਮਾਡਲਾਂ ਲਈ ਦੋਹਰਾ RTX 5060 Ti ਸਿਸਟਮ ਤੇਜ਼ ਹੈ।** ਇਸ ਦੀ ਕੀਮਤ ਸੂਚੀਬੱਧ GB10 ਸਿਸਟਮ ਦੀ ਲਗਭਗ ਅੱਧੀ ਹੈ। 256K ’ਤੇ Qwen3.8 27B, ਹੋਰ headroom ਅਤੇ ਇੱਕ ਸਾਂਝੇ ਮੈਮੋਰੀ ਪੂਲ ਵਾਲੇ ਵਰਕਲੋਡਾਂ ਲਈ GB10 ਬਿਹਤਰ ਚੋਣ ਹੈ।

ਪਹਿਲੇ Qwen-ਮਾਤਰ ਨਤੀਜੇ ਨੇ GB10 ਦੀ ਸੌਖੀ ਜਿੱਤ ਦਾ ਸੰਕੇਤ ਦਿੱਤਾ ਸੀ। ਨਵਾਂ ਪੰਜ-ਮਾਡਲ ਟੈਸਟ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਉਹ ਨਤੀਜਾ ਬਹੁਤ ਵਿਆਪਕ ਸੀ। ਮਾਡਲ architecture, runtime version, tensor placement ਅਤੇ ਸੰਦਰਭ ਵਿਹਾਰ ਨਤੀਜੇ ਬਦਲਦੇ ਹਨ।

ਜੇ ਤੁਸੀਂ GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 ਜਾਂ Qwen3.6 ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਇਸ ਬੈਂਚਮਾਰਕ ਵਿੱਚ ਦੋਹਰੇ-ਕਾਰਡ ਸਿਸਟਮ ਦੀ ਜਨਰੇਸ਼ਨ ਗਤੀ ਵੱਧ ਸੀ। ਜੇ ਤੁਸੀਂ 256K ’ਤੇ Qwen3.8 27B ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ GB10 ਨੇ ਵਰਤਣਯੋਗ ਗਤੀ ਦਿੱਤੀ ਜਦਕਿ ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ ਲਗਭਗ ਰੁਕ ਗਿਆ।

**ਮੈਮੋਰੀ ਸਮਰੱਥਾ ਅਤੇ throughput ਖਰੀਦ ਦੇ ਵੱਖਰੇ ਮਾਪਦੰਡ ਹਨ।** GB10 ਵਿੱਚ ਕੁੱਲ ਮੈਮੋਰੀ ਚਾਰ ਗੁਣਾ ਹੈ ਅਤੇ ਸਾਂਝਾ working set ਸੌਖਾ ਹੈ। ਦੋਹਰਾ-ਕਾਰਡ ਸਿਸਟਮ ਜ਼ਿਆਦਾਤਰ ਟੈਸਟ ਮਾਡਲਾਂ ’ਤੇ ਵੱਧ ਦਰਜ throughput ਅਤੇ ਕਾਫ਼ੀ ਘੱਟ ਸੂਚੀਬੱਧ ਸਿਸਟਮ ਕੀਮਤ ਦਿੰਦਾ ਹੈ।

Strata ਨਤੀਜਾ ਇੱਕ ਹੋਰ ਸਿੱਖਿਆ ਦਿੰਦਾ ਹੈ। ਉਸੇ ਦੋਹਰੇ-GPU ਹੋਸਟ ’ਤੇ runtime placement, ਮਾਡਲ architecture ਅਤੇ decode mode ਨੇ 256K ਨਤੀਜਾ ਬਦਲਿਆ। Flash-Next IQ2_XS ਨੇ ਵਾਰਮਅੱਪ ਤੋਂ ਬਾਅਦ ਲਗਭਗ 93 ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਦੀ ਮੀਡੀਅਨ ਰੱਖੀ, ਜਦਕਿ dense Qwen3.8 ਨੇ 24 layers offload ਕੀਤੀਆਂ ਅਤੇ ਇੱਕ ਟੋਕਨ ਪ੍ਰਤੀ ਸਕਿੰਟ ਤੋਂ ਹੇਠਾਂ ਡਿੱਗਿਆ।

## ਬੈਂਚਮਾਰਕ ਦੀਆਂ ਹੱਦਾਂ

ਬੈਂਚਮਾਰਕ ਵਿੱਚ ਮਾਡਲ ਟੈਗ, ਮੰਗੇ ਸੰਦਰਭ, ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨ, prompt-processing ਗਤੀ, ਜਨਰੇਸ਼ਨ ਗਤੀ, Ollama ਵਰਜਨ ਅਤੇ 128-token ਜਨਰੇਸ਼ਨ ਟਾਰਗੇਟ ਦਰਜ ਹਨ। ਇਸ ਵਿੱਚ resolved manifest digests, CPU power, wall power, fan speed ਜਾਂ ਕੂਲਿੰਗ ਸੈੱਟਅੱਪ ਦਰਜ ਨਹੀਂ ਹਨ।

256K GPT-OSS ਕਤਾਰਾਂ ਨੇ ਦੋਵੇਂ ਸਿਸਟਮਾਂ ’ਤੇ 65,538 ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਪ੍ਰੋਸੈਸ ਕੀਤੇ। ਹੋਰ 256K ਕਤਾਰਾਂ ਨੇ ਲਗਭਗ 171K ਅਸਲ ਪ੍ਰਾਂਪਟ ਟੋਕਨ ਪ੍ਰੋਸੈਸ ਕੀਤੇ। ਇਹ ਅੰਕੜੇ ਵੇਖੇ ਗਏ ਸਿਸਟਮਾਂ ਦੀ ਤੁਲਨਾ ਹਨ, ਹਰ RTX 5060 Ti ਜੋੜੇ ਅਤੇ ਹਰ GB10 implementation ਦੀ ਸਰਵ-ਵਿਆਪੀ ranking ਨਹੀਂ।

Strata ਬਨਾਮ dense ਰਨ ਵਿੱਚ ਸਹੀ ਪ੍ਰਾਂਪਟ ਗਿਣਤੀ, ਹਰ ਸੰਦਰਭ ’ਤੇ ਪੰਜ ਮਾਪੀਆਂ requests, runtime versions, device placement, cache settings ਅਤੇ request status ਦਰਜ ਹਨ। ਤੁਲਨਾ ਵਿੱਚ ਮਾਡਲ architecture, quantization, packaging, runtime ਅਤੇ decode mode ਇਕੱਠੇ ਬਦਲੇ। 32K ਤੋਂ ਉੱਪਰ Strata ਨੇ prompt prefixes ਮੁੜ ਵਰਤੇ। ਦੋਵੇਂ stacks ’ਤੇ ਮਾਪੀਆਂ ਜਨਰੇਸ਼ਨ requests ਨੇ ਲਗਭਗ ਸਾਰਾ ਪ੍ਰਾਂਪਟ ਮੁੜ ਵਰਤਿਆ।

ਇਸ ਲੇਖ ਤੋਂ ਸਹੀ ਦੁਹਰਾਈ ਸੰਭਵ ਨਹੀਂ। Benchmark harness, Strata pack layout, expert profile ਅਤੇ MTP draft pack ਦੇ immutable digests ਉਪਲਬਧ ਨਹੀਂ ਹਨ। ਘੱਟ VRAM ਚੇਤਾਵਨੀ ਵੀ ਮੁੜ ਚਲਾਉਣ ਦੇ ਨਤੀਜਿਆਂ ਵਿੱਚ ਜੋਖ਼ਮ ਵਧਾਉਂਦੀ ਹੈ। ਟੈਸਟ ਨੇ ਹੋਸਟ ਨੂੰ ਇਕਸਾਰ ਰੱਖਿਆ, inference engine ਨੂੰ ਨਹੀਂ।

ਉੱਪਰ ਦਿੱਤੀਆਂ ਹਾਰਡਵੇਅਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ NVIDIA ਤੋਂ ਹਨ। ਕਾਰਗੁਜ਼ਾਰੀ ਅੰਕੜੇ ਇਸ ਲੇਖ ਦੇ ਨਿਯੰਤਰਿਤ ਬੈਂਚਮਾਰਕ ਰਨ ਤੋਂ ਹਨ।

## ਹਵਾਲੇ

- [Ollama Qwen3.8 ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library/qwen3.8)
- [ISTA-DASLab Qwen3.8 Flash-Next GSQ-RCO GGUF ਮਾਡਲ](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [orcarouter Qwen3.8 Flash-Next Uncensored GGUF ਮਾਡਲ](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Ollama Qwen3.5 ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library/qwen3.5)
- [Ollama Qwen3.6 ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library/qwen3.6)
- [Ollama Nemotron 3.5 Lightning ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library/nemotron-3.5-lightning)
- [Ollama GPT-OSS ਮਾਡਲ ਟੈਗ](https://ollama.com/library/gpt-oss/tags)
- [ਕੀ ਗੰਭੀਰ ਸਥਾਨਕ LLM ਕੰਮ ਲਈ 16GB VRAM ਕਾਫ਼ੀ ਹੈ?](/articles/is-16gb-vram-enough-local-llm/)
- [Qwen 27B ਲਈ 32GB VRAM](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [ਸਥਾਨਕ AI GPU ਸੰਦਰਭ ਗਾਈਡ](/articles/local-ai-model-gpu-context-guide/)
- [Vast.ai ’ਤੇ Qwen3.8 27B GPU ਬੈਂਚਮਾਰਕ](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [ਦੋ RTX 5060 Ti 16 GB ਵਾਲੇ workstation ਦੀ ਸੂਚੀ](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [NVIDIA DGX Spark US marketplace ਸੂਚੀ](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [AMD Ryzen AI Halo 128 GB Linux ਸੂਚੀ](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Tom's Hardware Strix Halo ਬਨਾਮ GB10 ਸਮੀਖਿਆ](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [RTX 5060 Ti ਦੀਆਂ ਮੌਜੂਦਾ ਕੀਮਤਾਂ](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
