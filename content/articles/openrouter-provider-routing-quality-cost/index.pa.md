---
title: "OpenRouter ਪ੍ਰੋਵਾਈਡਰ ਰਾਊਟਿੰਗ: ਮਾਡਲ ਗੁਣਵੱਤਾ, ਟੋਕਨ ਸੀਮਾਵਾਂ ਅਤੇ ਅਸਲ ਲਾਗਤਾਂ"
date: 2026-10-05
lastmod: 2026-11-13
toc: true
draft: false
description: "OpenRouter ਦੇ ਅਸੰਗਤ ਜਵਾਬਾਂ ਦੀ ਜਾਂਚ ਕਰੋ, endpoint ਸੀਮਾਵਾਂ ਅਤੇ cache ਲਾਗਤਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ, ਅਤੇ ਗੁਣਵੱਤਾ ਨਿਯੰਤਰਣ ਅਣਜਾਣੇ ਵਿੱਚ ਬੰਦ ਕੀਤੇ ਬਿਨਾਂ ਪ੍ਰੋਵਾਈਡਰ ਰਾਊਟਿੰਗ ਕੌਂਫਿਗਰ ਕਰੋ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਇਨਫ੍ਰਾਸਟਰਕਚਰ", "ਖੁੱਲ੍ਹਾ ਸਰੋਤ"]
tags: ["OpenRouter", "ਪ੍ਰੋਵਾਈਡਰ ਰਾਊਟਿੰਗ", "OpenRouter ਦੇ ਐਂਡਪੌਇੰਟ", "AI ਮਾਡਲ ਗੁਣਵੱਤਾ", "LLM ਇਨਫਰੈਂਸ", "ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ", "FP4", "MXFP4", "BF16", "gpt-oss-120b", "Auto Exacto", "Exacto", "ਟੂਲ ਕਾਲਿੰਗ", "ਕਾਨਟੈਕਸਟ ਵਿੰਡੋ", "ਵੱਧ ਤੋਂ ਵੱਧ ਟੋਕਨ", "ਤਰਕ ਟੋਕਨ", "ਪ੍ਰੌਮਪਟ ਕੈਸ਼ਿੰਗ", "API ਖਰਚੇ", "ਪ੍ਰੋਵਾਈਡਰ ਫਾਲਬੈਕ", "require_parameters", "AI ਏਜੰਟ", "ਇਨਫਰੈਂਸ ਬੈਂਚਮਾਰਕ", "ਐਂਡਪੌਇੰਟ ਟੈਸਟਿੰਗ", "ਖੁੱਲ੍ਹੇ-ਵੇਟ ਮਾਡਲ"]
cover: "/img/cover/openrouter-provider-routing-inference-services.webp"
coverAlt: "AI inference ਸੇਵਾਵਾਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਆਪਸ ਵਿੱਚ ਜੁੜੇ ਨੋਡਾਂ ਦੀ ਅਬਸਟ੍ਰੈਕਟ ਡਿਜ਼ਿਟਲ ਤਸਵੀਰ, ਗੂੜ੍ਹੇ ਪਿਛੋਕੜ ਵਿੱਚ data flow ਦਿਖਾਉਂਦੀਆਂ ਚਮਕਦਾਰ ਲਾਈਨਾਂ ਨਾਲ।"
coverCaption: ""
---

**OpenRouter ਪ੍ਰੋਵਾਈਡਰ ਰਾਊਟਿੰਗ** ਇਹ ਤੈਅ ਕਰਦੀ ਹੈ ਕਿ ਤੁਹਾਡੀ request ਦਾ ਜਵਾਬ ਕਿਹੜੀ inference service ਦੇਵੇਗੀ। ਇੱਕੋ model name ਵਾਲੀਆਂ ਦੋ calls ਵੀ endpoint limits, supported parameters, serving software ਅਤੇ routing preferences ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੀਆਂ ਹਨ। ਜਦੋਂ ਜਵਾਬ ਛੋਟੇ ਹੋ ਜਾਣ ਜਾਂ tool calls fail ਹੋਣ, quantization ਨੂੰ ਦੋਸ਼ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਫਰਕ ਜਾਂਚੋ।

## ਮੁੱਖ ਗੱਲਾਂ

- **Precision labels** numerical format ਦੱਸਦੇ ਹਨ, accuracy score ਨਹੀਂ।
- **Endpoint limits** context, output length ਅਤੇ feature support ਤੈਅ ਕਰਦੇ ਹਨ।
- **Explicit routing** ਨੂੰ provider preference ਦੇ ਨਾਲ fallback policy ਵੀ ਚਾਹੀਦੀ ਹੈ।
- **Auto Exacto** quality signals ਨਾਲ provider selection ਸੁਧਾਰਦਾ ਹੈ। Tools ਤੋਂ ਬਿਨਾਂ requests ਲਈ opt-in route ਵੀ ਹੈ।
- **Effective cost** ਵਿੱਚ output, cache behavior, retries ਅਤੇ ਸਫਲ task completion ਸ਼ਾਮਲ ਹਨ।

**ਲੋੜਾਂ:** JSON requests ਦੀ ਜਾਣਕਾਰੀ ਅਤੇ ਆਪਣੀ application ਦੀ OpenRouter configuration ਤੱਕ ਪਹੁੰਚ। Endpoint inspection public API ਵਰਤਦੀ ਹੈ। Model requests ਭੇਜਣ ਲਈ API key ਅਤੇ usage charges ਲੋੜੀਂਦੇ ਹਨ। ਕਿਸੇ dated example ਨੂੰ ਦੁਬਾਰਾ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ endpoint metadata ਫਿਰ ਜਾਂਚੋ।

**ਸਮਾਂ ਅਤੇ ਮੁਸ਼ਕਲ:** ਪਹਿਲੀ configuration review ਲਈ ਲਗਭਗ 20 ਮਿੰਟ। ਦਰਮਿਆਨਾ ਪੱਧਰ। Providers ਦੀ ਚੰਗੀ ਤੁਲਨਾ ਲਈ representative prompts ਨਾਲ ਹੋਰ testing ਲੋੜੀਂਦੀ ਹੈ।

## ਮਾਡਲ ਦਾ ਨਾਮ ਕੀ ਨਹੀਂ ਦੱਸਦਾ

**Model identifier** ਮੰਗਿਆ ਹੋਇਆ model ਚੁਣਦਾ ਹੈ। Provider inference service ਚਲਾਉਂਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ model implementation, token limits ਅਤੇ tool-call parser ਸ਼ਾਮਲ ਹਨ। Model-level benchmark ਹਰ service ਨੂੰ validate ਨਹੀਂ ਕਰਦਾ ਜੋ ਇਹ weights host ਕਰਦੀ ਹੈ।

| ਐਂਡਪੌਇੰਟ ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ | ਕੀ ਜਾਂਚਣਾ ਹੈ |
|---|---|
| **ਸੰਦਰਭ ਦੀ ਲੰਬਾਈ** | ਪ੍ਰੌਮਪਟ, ਪਿਛਲਾ ਸੰਵਾਦ, ਟੂਲ ਦੇ ਨਤੀਜੇ ਅਤੇ ਨਵਾਂ ਜਵਾਬ ਬਣਾਉਣ ਲਈ ਉਪਲਬਧ ਥਾਂ |
| **ਜਵਾਬ ਦੀ ਵੱਧ ਤੋਂ ਵੱਧ ਲੰਬਾਈ** | ਮੰਗੇ ਕੰਮ ਲਈ ਆਉਟਪੁੱਟ ਦੀ ਮਨਜ਼ੂਰ ਹੱਦ |
| **ਸਮਰਥਿਤ ਪੈਰਾਮੀਟਰ** | ਟੂਲ ਦੀ ਵਰਤੋਂ, ਸੰਰਚਿਤ ਆਉਟਪੁੱਟ, ਨਮੂਨਾ ਚੋਣ ਅਤੇ ਤਰਕ-ਪ੍ਰਕਿਰਿਆ ਦੇ ਨਿਯੰਤਰਣ |
| **ਕੁਆਂਟਾਈਜ਼ੇਸ਼ਨ** | ਮੂਲ ਰਿਲੀਜ਼ ਨਾਲ ਤੁਲਨਾ ਕੀਤਾ ਦਰਜ ਫਾਰਮੈਟ |
| **ਕੀਮਤ** | ਇਨਪੁੱਟ, ਆਉਟਪੁੱਟ, ਕੈਸ਼ ਤੋਂ ਪੜ੍ਹਨਾ ਅਤੇ ਲਾਗੂ ਵਾਧੂ ਖਰਚੇ |
| **ਮਾਡਲ ਸੇਵਾ ਦਾ ਵਿਹਾਰ** | ਜਵਾਬ ਦੀ ਗੁਣਵੱਤਾ, ਪਾਰਸਿੰਗ ਦੀਆਂ ਗਲਤੀਆਂ, ਦੇਰੀ ਅਤੇ ਮੁੜ ਕੋਸ਼ਿਸ਼ਾਂ |

**Baseline routing** healthy candidates ਵਿੱਚ ਘੱਟ ਕੀਮਤਾਂ ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੀ ਹੈ। OpenRouter inverse-square price weighting document ਕਰਦਾ ਹੈ। ਇਸਦੇ simplified example ਵਿੱਚ $1 candidate ਨੂੰ $3 candidate ਨਾਲੋਂ ਨੌਂ ਗੁਣਾ selection weight ਮਿਲਦਾ ਹੈ। ਇਹ relative weights ਹਨ, ਅਗਲੀ request ਦੀ guarantee ਨਹੀਂ। Explicit ordering, sorting, caching ਅਤੇ quality routing ਵੀ selection ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ। [ਪ੍ਰੋਵਾਈਡਰ ਰਾਊਟਿੰਗ ਦਸਤਾਵੇਜ਼](https://openrouter.ai/docs/guides/routing/provider-selection) ਵੇਖੋ।

**Price weighting** ਤੁਹਾਡੇ workload ਦਾ ਸਭ ਤੋਂ ਸਸਤਾ bill ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ। Documented example input/output mixture ਦੀ universal definition ਨਹੀਂ ਦਿੰਦਾ। Provider ਦੀ selection probability ਸਿਰਫ input price ਤੋਂ ਨਾ ਕੱਢੋ।

## ਸੰਦਰਭ ਵਿੱਚ ਅੰਕਾਂ ਦੀ ਸਟੀਕਤਾ ਸਮਝੋ

**Quantization** numerical values ਨੂੰ reduced representation ਵਿੱਚ store ਕਰਦੀ ਹੈ। ਇਸਦਾ ਪ੍ਰਭਾਵ model, method ਅਤੇ inference implementation ਉੱਤੇ ਨਿਰਭਰ ਹੁੰਦਾ ਹੈ। Lower precision testing ਦੀ ਮੰਗ ਕਰਦੀ ਹੈ, ਪਰ label ਇਕੱਲਾ ਇਹ ਨਹੀਂ ਦਿਖਾਉਂਦਾ ਕਿ provider ਨੇ original weights ਬਦਲੇ ਹਨ।

**GPT-OSS ਇੱਕ ਸਾਫ਼ ਉਦਾਹਰਨ ਹੈ।** OpenAI ਦੀ [gpt-oss-120b ਰਿਲੀਜ਼ ਦਸਤਾਵੇਜ਼](https://huggingface.co/openai/gpt-oss-120b/raw/main/README.md) ਦੱਸਦੀ ਹੈ ਕਿ mixture-of-experts weights MXFP4 ਵਰਤਦੇ ਹਨ ਅਤੇ evaluations ਨੇ ਉਹੀ quantization ਵਰਤੀ। ਇਨ੍ਹਾਂ weights ਲਈ four-bit label published release ਨਾਲ ਮਿਲਦਾ ਹੈ। ਇਹ provider ਦੀ ਵਾਧੂ downgrade ਦਾ ਸਬੂਤ ਨਹੀਂ।

**Upcasting** stored values ਨੂੰ wider representation ਵਿੱਚ ਬਦਲਦਾ ਹੈ। ਪਹਿਲਾਂ ਹੀ quantized checkpoint ਨੂੰ BF16 ਵਿੱਚ ਬਦਲਣ ਨਾਲ quantization ਵਿੱਚ ਗੁਆਚੀ ਜਾਣਕਾਰੀ ਵਾਪਸ ਨਹੀਂ ਆਉਂਦੀ। Higher-precision checkpoint ਨੂੰ four bits ਵਿੱਚ ਬਦਲਣਾ ਵੱਖਰਾ ਬਦਲਾਅ ਹੈ, ਜਿਸਦੀ evaluation ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।

| ਨਿਰੀਖਣ | ਸਮਰਥਿਤ ਨਤੀਜਾ |
|---|---|
| **ਮੂਲ MXFP4 ਚੈਕਪੌਇੰਟ** | ਚਾਰ-ਬਿੱਟ ਮਾਹਿਰ ਵਜ਼ਨ ਮੂਲ ਰਿਲੀਜ਼ ਦਾ ਹਿੱਸਾ ਹਨ |
| **BF16 ਐਂਡਪੌਇੰਟ ਲੇਬਲ** | ਵਧੇਰੇ ਚੌੜਾ ਦਰਜ ਫਾਰਮੈਟ, ਪਰ ਵਧੀਆ ਜਵਾਬਾਂ ਦਾ ਸਬੂਤ ਨਹੀਂ |
| **ਅਣਜਾਣ ਅੰਕਾਤਮਕ ਸਟੀਕਤਾ** | ਮੈਟਾਡੇਟਾ ਦੀ ਕਮੀ, ਪਰ ਲੁਕਵੇਂ ਗੁਣਵੱਤਾ-ਘਾਟ ਦਾ ਸਬੂਤ ਨਹੀਂ |
| **ਇੱਕੋ ਜਿਹੇ ਸਟੀਕਤਾ ਲੇਬਲ** | ਸਮਾਨ ਮਾਡਲ-ਸੇਵਾ ਵਿਹਾਰ ਦਾ ਸਬੂਤ ਦੇਣ ਲਈ ਕਾਫ਼ੀ ਨਹੀਂ |

**Matching labels quantization differences ਨੂੰ ਵੀ rule out ਨਹੀਂ ਕਰਦੇ।** ਉਹ ਇਹ ਵੇਰਵੇ ਛੱਡ ਦਿੰਦੇ ਹਨ ਕਿ ਕਿਹੜੇ tensors quantized ਸਨ, calibration choices ਕੀ ਸਨ ਅਤੇ execution kernels ਕਿਹੜੇ ਸਨ। Bit depth ਨੂੰ quality ranking ਸਮਝਣ ਦੀ ਥਾਂ ਪੂਰੇ endpoint ਦੀ testing ਕਰੋ।

## ਟੋਕਨਾਂ ਦੀ ਸੀਮਾ ਜਾਂਚੋ

```bash
curl --fail --silent --show-error \
  'https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints' \
  | jq '.data.endpoints[] | {
      name,
      provider_name,
      context_length,
      max_completion_tokens,
      supported_parameters,
      quantization,
      pricing
    }'
```

**Endpoints API** ਇੱਕ model ਲਈ provider-level metadata ਦਿੰਦੀ ਹੈ। ਇਹ command **`curl`** ਅਤੇ **`jq`** ਮੰਗਦੀ ਹੈ। Service ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ [gpt-oss-120b endpoint ਦਾ ਮੌਜੂਦਾ ਜਵਾਬ](https://openrouter.ai/api/v1/models/openai/gpt-oss-120b/endpoints) inspect ਕਰੋ। Missing ਜਾਂ null fields ਨੂੰ unknown ਮੰਨੋ, unlimited ਨਹੀਂ। Results compare ਕਰਦੇ ਸਮੇਂ dated local snapshot save ਕਰੋ।

**5 October 2026 ਦੀ check** ਨੇ gpt-oss-120b ਲਈ ਇਹ advertised limits ਵਾਪਸ ਕੀਤੀਆਂ। ਇਹ metadata values ਹਨ, measured completion lengths ਨਹੀਂ। Providers ਸਮੇਂ ਨਾਲ ਇਹਨਾਂ ਨੂੰ ਬਦਲਦੇ ਹਨ।

| ਪ੍ਰੋਵਾਈਡਰ | ਸੰਦਰਭ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ | ਜਵਾਬ ਲਈ ਵੱਧ ਤੋਂ ਵੱਧ ਟੋਕਨ |
|---|---:|---:|
| **DigitalOcean** | 128,000 | 4,096 |
| **Novita** | 131,072 | 32,768 |
| **Together** | 131,072 | 117,964 |

**Context length ਅਤੇ output length ਵੱਖਰੀਆਂ limits ਹਨ।** Long-context model ਨੂੰ ਵੀ answer ਲਈ ਥਾਂ ਚਾਹੀਦੀ ਹੈ। Conversation history, system instructions ਅਤੇ tool definitions user document ਨਾਲ ਥਾਂ ਸਾਂਝੀ ਕਰਦੇ ਹਨ।

**Reasoning tokens** supported reasoning models ਵਿੱਚ generation budget ਵਰਤਦੇ ਹਨ। ਛੋਟਾ allowance incomplete reasoning, ਘੱਟ visible output ਜਾਂ final answer ਤੋਂ ਪਹਿਲਾਂ termination ਕਰ ਸਕਦਾ ਹੈ। Usage ਅਤੇ finish reason inspect ਕਰੋ। ਹਰ short answer ਨੂੰ weaker weights ਨਾਲ ਨਾ ਜੋੜੋ। OpenRouter ਇਸ budget ਨੂੰ [reasoning-token ਦਸਤਾਵੇਜ਼](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens) ਵਿੱਚ ਸਮਝਾਉਂਦਾ ਹੈ।

**Explicit `max_tokens`** router ਨੂੰ requested output length ਦਿੰਦਾ ਹੈ, ਜਿਸਦੀ provider support ਨਾਲ ਤੁਲਨਾ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। Measured task needs ਅਤੇ available context ਤੋਂ value ਚੁਣੋ। ਬਹੁਤ ਵੱਡੀ value eligibility ਘਟਾਉਂਦੀ ਹੈ ਅਤੇ ਲੰਬੇ ਜਾਂ ਚੰਗੇ answer ਦੀ guarantee ਨਹੀਂ ਦਿੰਦੀ।

{{< figure src="context-reasoning-output-token-budget.webp" alt="Illustration of a divided token pool flowing through a model into an output stream" caption="Conceptual token allocation, with reasoning and visible output sharing the completion allowance on supported providers" >}}

## ਲੋੜੀਂਦੇ ਪੈਰਾਮੀਟਰ ਲਾਜ਼ਮੀ ਕਰੋ

```json
{
  "model": "openai/gpt-oss-120b",
  "messages": [
    {"role": "user", "content": "Explain the failure modes of a retry loop."}
  ],
  "max_tokens": 8192,
  "provider": {
    "require_parameters": true
  }
}
```

**`require_parameters`** ਦੀ default value false ਹੈ। Default routing ਵਿੱਚ unsupported parameters endpoint ਨੂੰ ਹਮੇਸ਼ਾ exclude ਨਹੀਂ ਕਰਦੇ। OpenRouter unknown parameters ignore ਕਰਨ ਵਾਲੇ providers document ਕਰਦਾ ਹੈ। ਇਸ field ਨੂੰ true ਕਰਨ ਨਾਲ declared support ਅਨੁਸਾਰ routing filter ਹੁੰਦੀ ਹੈ।

**Support metadata behavior guarantee ਨਹੀਂ ਹੈ।** Seed support ਦੱਸਣ ਵਾਲੇ endpoint ਨੂੰ reproducibility testing ਦੀ ਫਿਰ ਵੀ ਲੋੜ ਹੈ। Tool-capable endpoint ਨੂੰ schema validation ਅਤੇ application-level tests ਦੀ ਲੋੜ ਹੈ। Filter known incompatibilities ਨੂੰ candidate set ਵਿੱਚ ਆਉਣ ਤੋਂ ਰੋਕਦਾ ਹੈ।

## ਪ੍ਰੋਵਾਈਡਰਾਂ ਨੂੰ ਸੋਚ-ਸਮਝ ਕੇ ਨਿਰਧਾਰਤ ਕਰੋ

```json
{
  "model": "openai/gpt-oss-120b",
  "messages": [
    {"role": "user", "content": "Summarize the supplied incident report."}
  ],
  "max_tokens": 8192,
  "provider": {
    "order": ["REPLACE_WITH_VERIFIED_PROVIDER_SLUG"],
    "allow_fallbacks": false,
    "require_parameters": true
  }
}
```

**Placeholder ਨੂੰ ਬਦਲੋ** model ਦੀ provider listing ਤੋਂ copy ਕੀਤੇ provider slug ਨਾਲ। ਆਪਣੀ real request ਵਿੱਚ report ਭੇਜੋ। ਇਹ template configuration review ਲਈ ਹੈ। Placeholder ਬਦਲੇ ਬਿਨਾਂ ਇਹ runnable request ਨਹੀਂ।

**`order`** preference ਤੈਅ ਕਰਦਾ ਹੈ। ਇਕੱਲਾ ਵਰਤਿਆਂ ਹੋਰ providers ਲਈ fallback enabled ਰਹਿੰਦਾ ਹੈ। **`allow_fallbacks: false`** ਨਾਲ routing listed providers ਤੱਕ ਸੀਮਤ ਹੁੰਦੀ ਹੈ। ਜਦੋਂ ਕੋਈ provider request satisfy ਨਾ ਕਰੇ ਜਾਂ available ਨਾ ਰਹੇ, request fail ਹੋਣ ਦੀ ਉਮੀਦ ਰੱਖੋ।

**Endpoint variants ਵੱਲ ਧਿਆਨ ਦਿਓ।** Base provider slug documented matching rules ਅਨੁਸਾਰ ਕਈ variants ਨਾਲ match ਕਰਦਾ ਹੈ। ਖਾਸ service configuration test ਕਰਦੇ ਸਮੇਂ specific variant slug ਵਰਤੋ। ਹਰ response ਵਿੱਚ reported provider ਫਿਰ ਜਾਂਚੋ।

**`quantizations`** named formats ਦੀ allowlist ਹੈ, numerical minimum ਨਹੀਂ। **`"fp8"`** ਵਾਲਾ array matching FP8 endpoints ਚੁਣਦਾ ਹੈ। ਇਹ BF16 ਜਾਂ ਵੱਧ bits ਵਾਲੇ ਸਾਰੇ formats ਨੂੰ ਆਪਣੇ ਆਪ ਸ਼ਾਮਲ ਨਹੀਂ ਕਰਦਾ। ਪਹਿਲਾਂ original checkpoint compare ਕਰੋ, ਫਿਰ evaluation support ਕਰੇ ਤਾਂ filter ਲਗਾਓ।

## ਗੁਣਵੱਤਾ-ਆਧਾਰਿਤ ਰਾਊਟਿੰਗ ਚਾਲੂ ਰੱਖੋ

```json
{
  "model": "openai/gpt-oss-120b:exacto",
  "messages": [
    {"role": "user", "content": "Compare the two supplied incident reports."}
  ],
  "max_tokens": 8192,
  "provider": {
    "require_parameters": true
  }
}
```

**Auto Exacto** throughput, tool-call telemetry ਅਤੇ benchmarks ਵਰਤ ਕੇ ਘੱਟ performance ਵਾਲੇ providers ਨੂੰ ਹੇਠਾਂ ਕਰਦਾ ਹੈ। OpenRouter ਦੀ [ਮਾਰਚ 2026 ਦੀ ਘੋਸ਼ਣਾ](https://openrouter.ai/blog/announcements/auto-exacto/) GLM-5 tool-call errors ਵਿੱਚ 88% ਕਮੀ ਦੱਸਦੀ ਹੈ, ਲਗਭਗ 8% ਤੋਂ 1% ਤੱਕ। ਇਹ gpt-oss-120b ਲਈ 5.6% ਤੋਂ 3.5% ਦੀ ਤਬਦੀਲੀ ਵੀ ਦੱਸਦੀ ਹੈ।

**ਇਹ provider ਵੱਲੋਂ report ਕੀਤੇ ਨਤੀਜੇ ਹਨ**, ਤੁਹਾਡੀ application ਲਈ promise ਨਹੀਂ। Tool-call validity JSON, names ਅਤੇ schemas ਮਾਪਦੀ ਹੈ। Syntactically valid call ਨੂੰ ਵੀ user task ਲਈ ਸਹੀ arguments ਅਤੇ action ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

**Tools ਵਾਲੀਆਂ requests** ਨੂੰ model ਦੀ provider coverage ਕਾਫ਼ੀ ਹੋਣ ਉੱਤੇ default ਤੌਰ ਤੇ Auto Exacto ਮਿਲਦਾ ਹੈ। ਹੋਰ requests ਲਈ **`:exacto`** quality routing opt in ਕਰਦਾ ਹੈ। Current documentation summarization ਅਤੇ chat ਦੇ ਨਾਲ tool use ਲਈ ਵੀ quality routing support ਕਰਦੀ ਹੈ।

**`sort: "price"`**, **`:floor`** suffix ਅਤੇ account-level default price sort Auto Exacto opt out ਕਰਦੇ ਹਨ। Application settings ਅਤੇ account preferences ਇਕੱਠੇ check ਕਰੋ। Routing controls ਜੋੜਨ ਤੋਂ ਪਹਿਲਾਂ [Auto Exacto ਦਸਤਾਵੇਜ਼](https://openrouter.ai/docs/guides/routing/auto-exacto) ਪੜ੍ਹੋ।

## ਕੰਮ ਦੇ ਭਾਰ ਦੀ ਲਾਗਤ ਕੱਢੋ

**Input price ਇਕੱਲੀ** ਅਧੂਰੀ comparison ਹੈ। ਹੇਠਾਂ dollars per million tokens ਵਿੱਚ illustrative rates ਹਨ। ਇਹ arithmetic ਦਿਖਾਉਂਦੀਆਂ ਹਨ, current provider quotes ਨਹੀਂ।

| ਉਦਾਹਰਨ ਵਾਲਾ ਐਂਡਪੌਇੰਟ | ਇਨਪੁੱਟ ਦੀ ਕੀਮਤ | ਆਉਟਪੁੱਟ ਦੀ ਕੀਮਤ |
|---|---:|---:|
| **A** | $0.03 | $16.00 |
| **B** | $0.42 | $1.32 |

```text
ਕੰਮ ਦਾ ਭਾਰ: 6 ਮਿਲੀਅਨ ਇਨਪੁੱਟ ਟੋਕਨ + 1 ਮਿਲੀਅਨ ਆਉਟਪੁੱਟ ਟੋਕਨ

A = 6 × $0.03 + 1 × $16.00 = $16.18
B = 6 × $0.42 + 1 × $1.32  =  $3.84

ਸੰਯੁਕਤ ਇਨਪੁੱਟ ਅਤੇ ਆਉਟਪੁੱਟ ਦੇ ਹਰ ਮਿਲੀਅਨ ਟੋਕਨਾਂ ਲਈ:
A = $16.18 / 7 = $2.31
B =  $3.84 / 7 = $0.55
```

**ਇਸ mixture ਲਈ Endpoint A ਲਗਭਗ 4.2 ਗੁਣਾ ਮਹਿੰਗਾ ਹੈ**, ਭਾਵੇਂ input price ਘੱਟ ਹੈ। A ਦਾ 533-to-1 output/input ratio ਦੋ rates ਵਿਚਕਾਰ ratio ਹੈ, user ਦੇ total cost ਦਾ multiplier ਨਹੀਂ। ਵੱਖਰੀ input/output proportion comparison ਬਦਲ ਦਿੰਦੀ ਹੈ।

**API pricing units comparison tables ਤੋਂ ਵੱਖਰੀਆਂ ਹਨ।** Endpoint API token prices per token ਦਿੰਦੀ ਹੈ। ਉੱਪਰਲੀਆਂ rates ਨਾਲ compare ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ million ਨਾਲ ਗੁਣਾ ਕਰੋ।

**Prompt caching** ਇੱਕ ਹੋਰ variable ਲਿਆਉਂਦੀ ਹੈ। Cached reads, cache writes ਅਤੇ uncached input ਨੂੰ provider billing rules ਅਨੁਸਾਰ ਵੱਖਰਾ account ਕਰੋ। Repeated text cache hit ਦੀ guarantee ਨਹੀਂ। [ਪ੍ਰੌਮਪਟ ਕੈਸ਼ਿੰਗ ਦਸਤਾਵੇਜ਼](https://openrouter.ai/docs/guides/best-practices/prompt-caching) ਵਿੱਚ reported cached-token counts ਅਤੇ costs ਵੇਖੋ।

**Routing cache continuity ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰਦੀ ਹੈ।** OpenRouter caching ਲਈ sticky routing document ਕਰਦਾ ਹੈ, ਜਦਕਿ manual provider order ਨੂੰ priority ਮਿਲਦੀ ਹੈ। Auto Exacto providers ਨੂੰ reorder ਕਰਦਾ ਹੈ ਅਤੇ ਕਈ ਵਾਰ warm cache ਤੋੜਦਾ ਹੈ। Policy ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ observed cache savings ਨੂੰ quality ਅਤੇ retry costs ਨਾਲ compare ਕਰੋ।

**Cost per accepted result** application ਦੀ useful metric ਹੈ। Total spend, retries ਅਤੇ failed attempts ਸਮੇਤ, acceptance criteria ਪੂਰੇ ਕਰਨ ਵਾਲੇ results ਨਾਲ divide ਕਰੋ। Applicable non-token charges ਵੱਖਰੇ ਸ਼ਾਮਲ ਕਰੋ। Low token rate repeatedly unsuccessful tasks ਦੀ ਭਰਪਾਈ ਨਹੀਂ ਕਰਦੀ।

## ਅਸੰਗਤ ਜਵਾਬ ਦੀ ਜਾਂਚ ਕਰੋ

| ਲੱਛਣ | ਪਹਿਲਾਂ ਕੀ ਜਾਂਚਣਾ ਹੈ |
|---|---|
| **ਛੋਟਾ ਜਾਂ ਅਧੂਰਾ ਜਵਾਬ** | ਮੁਕੰਮਲ ਹੋਣ ਦਾ ਕਾਰਨ, ਆਉਟਪੁੱਟ ਦੀ ਹੱਦ, ਤਰਕ ਲਈ ਟੋਕਨਾਂ ਦੀ ਵਰਤੋਂ |
| **ਦਸਤਾਵੇਜ਼ ਦੇ ਵੇਰਵੇ ਗੁੰਮ** | ਭੇਜੀ ਸਮੱਗਰੀ, ਐਂਡਪੌਇੰਟ ਦੀ ਸੰਦਰਭ ਹੱਦ, ਕਲਾਇੰਟ ਵਿੱਚ ਕੱਟੇ ਹਿੱਸੇ |
| **ਗਲਤ-ਬਣਤਰ ਵਾਲੀ ਟੂਲ ਕਾਲ** | ਘੋਸ਼ਿਤ ਸਮਰਥਨ, ਟੂਲ ਦੀ ਸਕੀਮਾ, ਪਾਰਸਿੰਗ ਦਾ ਵਿਹਾਰ |
| **ਨਮੂਨਾ ਚੋਣ ਦੇ ਵਿਹਾਰ ਵਿੱਚ ਫ਼ਰਕ** | ਮੰਗੇ ਪੈਰਾਮੀਟਰ ਅਤੇ ਘੋਸ਼ਿਤ ਸਮਰਥਨ |
| **ਅਣਉਮੀਦ ਖਰਚ** | ਆਉਟਪੁੱਟ ਦੀ ਮਾਤਰਾ, ਕੈਸ਼ ਤੋਂ ਪੜ੍ਹਨਾ, ਮੁੜ ਕੋਸ਼ਿਸ਼ਾਂ, ਪ੍ਰੋਵਾਈਡਰ ਵਿੱਚ ਬਦਲਾਅ |
| **ਕੋਈ ਯੋਗ ਪ੍ਰੋਵਾਈਡਰ ਨਹੀਂ** | ਟਕਰਾਉਂਦੀਆਂ ਹੱਦਾਂ, ਮਨਜ਼ੂਰ-ਸੂਚੀਆਂ ਅਤੇ ਵਿਕਲਪੀ ਪ੍ਰੋਵਾਈਡਰ ਦੀਆਂ ਪਾਬੰਦੀਆਂ |

**Response ਨਾਲ ਮਿਲਿਆ generation ID ਸੰਭਾਲੋ।** OpenRouter ਦੀ [ਜਨਰੇਸ਼ਨ ਮੈਟਾਡੇਟਾ API](https://openrouter.ai/docs/api/api-reference/generations/get-request-&-usage-metadata-for-a-generation) provider identity, usage, cost ਅਤੇ finish information ਦਿੰਦੀ ਹੈ। Session ID related work group ਕਰਦੀ ਹੈ, ਪਰ single request lookup ਲਈ generation ID ਦੀ ਥਾਂ ਨਹੀਂ ਲੈਂਦੀ।

**Generation ID ਦੇ ਨਾਲ request save ਕਰੋ।** Model, provider preferences, requested parameters, timestamp ਅਤੇ response usage ਰੱਖੋ। Routing, prices ਜਾਂ endpoint metadata ਬਦਲਣ ਉੱਤੇ ਬਾਅਦ ਦੀ quality ਜਾਂ cost comparison reproducible ਰਹੇਗੀ।

**Matching conditions ਹੇਠ endpoints compare ਕਰੋ।** ਇੱਕੋ prompt, tools, reasoning settings ਅਤੇ token budget ਵਰਤੋ। ਕਈ representative tasks ਉੱਤੇ repeat ਕਰੋ। Incomplete responses, invalid tool calls ਅਤੇ wrong answers ਨੂੰ ਇੱਕ unexplained quality score ਵਿੱਚ ਨਾ ਮਿਲਾਓ।

**Benchmark uncertainty ਮਹੱਤਵ ਰੱਖਦੀ ਹੈ।** Epoch AI ਦੀ [ਬੈਂਚਮਾਰਕ ਵਿਸ਼ਲੇਸ਼ਣ](https://epoch.ai/gradient-updates/why-benchmarking-is-hard) implementations, sampling ਅਤੇ agent scaffolds ਤੋਂ variation ਦੱਸਦੀ ਹੈ। ਇੱਕ disappointing answer persistent provider defect ਜਾਂ ਉਸਦੀ cause ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

## ਐਂਡਪੌਇੰਟ ਰਾਊਟਿੰਗ ਬਾਰੇ ਕਦਮ-ਦਰ-ਕਦਮ ਜਾਣਕਾਰੀ

{{< youtube id="ZsnFX5mEJ4s" enable="true" title="OpenRouter endpoint routing, precision, and pricing" >}}

**ਹੋਰ ਵੇਖੋ:** [OpenRouter endpoint ਦੀ ਗੁਣਵੱਤਾ ਅਤੇ routing ਬਾਰੇ ਚਰਚਾ](https://www.youtube.com/watch?v=ZsnFX5mEJ4s)। Specific prices, limits ਜਾਂ provider comparisons ਲਾਗੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ endpoint listings ਫਿਰ check ਕਰੋ।

## ਅਗਲੇ ਕਦਮ

1. **ਇੱਕ model ਦੇ endpoints inspect ਕਰੋ** ਅਤੇ ਆਪਣੇ workload ਲਈ relevant limits record ਕਰੋ।
2. **Routing policy ਚੁਣੋ** ਜਿਸ ਵਿੱਚ explicit parameter requirements ਅਤੇ fallback behavior ਹੋਵੇ।
3. **Representative tasks test ਕਰੋ** candidate endpoints ਅਤੇ quality routing ਦੇ ਖ਼ਿਲਾਫ਼।
4. **Accepted-result cost record ਕਰੋ** latency, cache usage ਅਤੇ failure categories ਦੇ ਨਾਲ।
5. **Changes ਤੋਂ ਬਾਅਦ ਫਿਰ check ਕਰੋ** model versions, serving behavior ਜਾਂ provider prices ਵਿੱਚ।

ਵਿਆਪਕ AI fundamentals ਲਈ [AI ਦੇ ਬੁਨਿਆਦੀ ਸੰਕਲਪ](/secai-plus/basic-ai-concepts/) ਪੜ੍ਹੋ। Agent permissions ਅਤੇ validation controls ਲਈ [AI ਸਿਸਟਮਾਂ ਦੀ ਸੁਰੱਖਿਆ](/secai-plus/securing-ai-systems/) ਪੜ੍ਹੋ।
