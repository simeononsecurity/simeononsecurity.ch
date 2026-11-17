---
title: "ਸਥਾਨਕ ਮਾਡਲਾਂ ਨਾਲ Claude Cowork ਅਤੇ Claude Code: 2026 ਸੈੱਟਅੱਪ ਗਾਈਡ"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Anthropic-ਅਨੁਕੂਲ API ਰਾਹੀਂ Claude Desktop ਅਤੇ Claude Code ਨਾਲ Ollama ਕੌਂਫਿਗਰ ਕਰੋ। 2026 ਦੇ ਮਾਡਲਾਂ ਅਤੇ ਕਲਾਊਡ-ਨਿਰਭਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਬਾਰੇ ਜਾਣੋ।"
genre: ["ਸਥਾਨਕ AI", "AI ਪ੍ਰੋਗਰਾਮਿੰਗ ਟੂਲ", "ਆਪਣੇ ਸਰਵਰ ਤੇ ਚੱਲਦਾ AI", "ਡਿਵੈਲਪਰ ਟੂਲ", "ਨਿੱਜਤਾ", "ਓਪਨ-ਸੋਰਸ ਮਾਡਲ", "ਆਟੋਮੇਸ਼ਨ", "AI ਹਾਰਡਵੇਅਰ"]
tags: ["claude cowork", "claude code", "claude desktop ਸਥਾਨਕ ਮਾਡਲ", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code ਸਥਾਨਕ ਮਾਡਲ", "claude ਆਫਲਾਈਨ ਚਲਾਉਣਾ", "ਸਥਾਨਕ AI ਕੋਡਿੰਗ ਏਜੰਟ", "ollama launch claude", "claude desktop ollama", "ਸਥਾਨਕ llm ਕੋਡਿੰਗ", "ਨਿੱਜੀ AI ਕੋਡਿੰਗ", "ਆਫਲਾਈਨ AI ਕੋਡਿੰਗ", "ਸਥਾਨਕ AI ਏਜੰਟ", "qwen3.8", "glm ਕਲਾਊਡ ਮਾਡਲ", "ਟੂਲ ਕਾਲਿੰਗ ਮਾਡਲ", "claude code ਸੈੱਟਅੱਪ", "ਮੁਫ਼ਤ claude code", "API ਕੁੰਜੀ ਤੋਂ ਬਿਨਾਂ claude", "ਸਥਾਨਕ ਮਾਡਲ ਦੀ context window", "llama.cpp", "ollama cloud", "AI ਕੋਡਿੰਗ ਦੀ ਨਿੱਜਤਾ", "ਨੈੱਟਵਰਕ ਤੋਂ ਵੱਖਰਾ AI", "devops AI ਟੂਲ"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "ਆਧੁਨਿਕ ਕੰਮਕਾਜੀ ਥਾਂ ਤੇ ਕੰਪਿਊਟਰ ਵਿੱਚ ਕੋਡਿੰਗ ਇੰਟਰਫੇਸ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ। ਨਾਲ ਟੈਬਲੈਟ ਅਤੇ ਸਮਾਰਟ ਸਪੀਕਰ ਹਨ, ਪਿੱਛੇ ਰੰਗੀਨ ਰੌਸ਼ਨੀ ਵਾਲਾ ਗੂੜ੍ਹਾ ਨੀਲਾ ਪਿਛੋਕੜ ਹੈ।"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Claude ਦੇ ਏਜੰਟ ਟੂਲ ਹੁਣ ਤੁਹਾਡੇ ਆਪਣੇ ਹਾਰਡਵੇਅਰ ਤੇ ਮੌਜੂਦ ਮਾਡਲਾਂ ਨਾਲ ਚੱਲਦੇ ਹਨ। API ਕੁੰਜੀ, ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਜਾਂ ਡਿਵਾਈਸ ਤੋਂ ਬਾਹਰ ਡਾਟਾ ਭੇਜਣ ਦੀ ਲੋੜ ਨਹੀਂ।** Ollama Anthropic-ਅਨੁਕੂਲ API ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ Claude Code ਅਤੇ Claude Desktop ਕੁਝ ਕਮਾਂਡਾਂ ਰਾਹੀਂ ਜੁੜਦੇ ਹਨ।

*ਕਈ ਗਾਈਡਾਂ ਇੱਕ ਅਹਿਮ ਗੱਲ ਛੱਡ ਦਿੰਦੀਆਂ ਹਨ। ਉਹ Claude Cowork ਬਾਰੇ ਦੱਸਦੀਆਂ ਹਨ, ਫਿਰ ਕਮਾਂਡ-ਲਾਈਨ ਟੂਲ ਕੌਂਫਿਗਰ ਕਰਨ ਦੇ ਕਦਮ ਦਿੰਦੀਆਂ ਹਨ। ਇਹ ਦੋ ਵੱਖਰੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹਨ ਅਤੇ Cowork ਸਿਰਫ਼ ਇੱਕ ਵਿੱਚ ਮਿਲਦਾ ਹੈ।*

ਇਹ ਗਾਈਡ ਦੋਵੇਂ ਰਾਹ ਵੱਖ-ਵੱਖ ਸਮਝਾਉਂਦੀ ਹੈ, ਉਹ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਦੱਸਦੀ ਹੈ ਜੋ ਪ੍ਰਸਿੱਧ ਟਿਊਟੋਰਿਅਲ ਛੱਡ ਦਿੰਦੇ ਹਨ, ਸਤੰਬਰ 2026 ਵਿੱਚ ਹਰ ਰਾਹ ਲਈ ਢੁਕਵੇਂ ਮਾਡਲ ਦਿਖਾਉਂਦੀ ਹੈ ਅਤੇ ਉਹ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੱਸਦੀ ਹੈ ਜੋ ਕਿਸੇ ਵੀ ਸੈੱਟਅੱਪ ਵਿੱਚ ਸਿਰਫ਼ ਕਲਾਊਡ ਤੇ ਰਹਿੰਦੀਆਂ ਹਨ।

**ਗਾਈਡ ਤੋਂ ਬਾਅਦ:** ਤੁਸੀਂ ਲੋੜੀਂਦਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪਛਾਣੋਗੇ, Ollama ਦੇ ਦਸਤਾਵੇਜ਼ੀ ਤਰੀਕੇ ਰਾਹੀਂ ਜੋੜੋਗੇ ਅਤੇ ਇੱਕ ਟੂਲ-ਕਾਲਿੰਗ ਟੈਸਟ ਨਾਲ endpoint ਦੀ ਜਾਂਚ ਕਰੋਗੇ। ਸਥਾਨਕ inference ਮਾਡਲ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਡਿਵਾਈਸ ਤੇ ਤਾਂ ਹੀ ਰੱਖਦਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਸਥਾਨਕ ਮਾਡਲ ਚੁਣਦੇ ਹੋ ਅਤੇ ਕਲਾਊਡ-ਅਧਾਰਿਤ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਤੋਂ ਬਚਦੇ ਹੋ।

## ਛੋਟਾ ਜਵਾਬ

**Ollama ਰਾਹੀਂ Claude ਨਾਲ ਜੁੜਨ ਦੇ ਦੋ ਵੱਖਰੇ ਤਰੀਕੇ ਹਨ। ਗਲਤ ਤਰੀਕਾ ਚੁਣਨਾ ਹੀ ਉਹ ਆਮ ਕਾਰਨ ਹੈ ਜਿਸ ਕਰਕੇ ਗਾਈਡ ਪੂਰੀ ਕਰਨ ਤੇ ਟਰਮੀਨਲ ਤਾਂ ਚੱਲਦਾ ਹੈ ਪਰ Cowork ਨਹੀਂ ਮਿਲਦਾ।**

| ਇੰਟੀਗ੍ਰੇਸ਼ਨ | ਕੀ ਮਿਲਦਾ ਹੈ | ਸੈੱਟਅੱਪ ਦਾ ਰਾਹ | ਪਲੇਟਫਾਰਮ |
|---|---|---|---|
| **Claude Desktop** | Cowork, subagents, ਵੈੱਬ ਖੋਜ, auto mode | Ollama ਐਪ, ਫਿਰ **Apps** ਅਤੇ **Connect Claude** | **ਸਿਰਫ਼ macOS** |
| **Claude Code** | ਟੂਲ ਕਾਲਿੰਗ ਅਤੇ ਫ਼ਾਈਲ ਸੋਧਾਂ ਵਾਲਾ CLI ਕੋਡਿੰਗ ਏਜੰਟ | `ollama launch claude` ਜਾਂ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ | macOS, Linux, Windows |

**Cowork ਚਾਹੀਦਾ ਹੈ ਤਾਂ Claude Desktop ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵਰਤੋ।** ਇਹ Ollama ਐਪ ਵਿੱਚ ਗ੍ਰਾਫ਼ਿਕਲ ਤਰੀਕੇ ਨਾਲ ਸੈੱਟ ਹੁੰਦਾ ਹੈ ਅਤੇ ਸਿਰਫ਼ macOS ਲਈ ਉਪਲਬਧ ਹੈ। Windows ਸਮਰਥਨ ਹਾਲੇ ਆਉਣ ਵਾਲਾ ਦਰਸਾਇਆ ਗਿਆ ਹੈ।

**ਟਰਮੀਨਲ ਵਿੱਚ ਏਜੰਟ ਚਾਹੀਦਾ ਹੈ ਤਾਂ Claude Code ਵਰਤੋ।** ਇੱਕ ਕਮਾਂਡ ਕਾਫ਼ੀ ਹੈ।

*ਦੋਵੇਂ ਮੁਫ਼ਤ ਹਨ। ਖਰਚ ਸਿਰਫ਼ ਹਾਰਡਵੇਅਰ ਅਤੇ ਬਿਜਲੀ ਦਾ ਹੈ।*

## ਦੋ ਇੰਟੀਗ੍ਰੇਸ਼ਨ, ਇੱਕ ਨਹੀਂ

ਉਲਝਣ ਨਾਵਾਂ ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦੀ ਹੈ। **Claude Cowork, Claude Desktop ਦੇ ਅੰਦਰ ਇੱਕ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ**, ਵੱਖਰੀ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ Claude Code ਦਾ ਦੂਜਾ ਨਾਂ ਨਹੀਂ।

Ollama ਦੇ ਦਸਤਾਵੇਜ਼ ਦੋਵੇਂ ਨੂੰ ਵੱਖਰੇ ਪੰਨਿਆਂ ਅਤੇ ਸਿਰਲੇਖਾਂ ਹੇਠ ਰੱਖਦੇ ਹਨ। Claude Desktop **Assistants** ਵਿੱਚ OpenClaw ਅਤੇ Hermes ਦੇ ਨਾਲ ਹੈ। Claude Code **Coding** ਵਿੱਚ OpenCode, Cline ਅਤੇ Codex CLI ਦੇ ਨਾਲ ਹੈ।

ਇਹ ਫ਼ਰਕ ਮਹੱਤਵਪੂਰਨ ਹੈ ਕਿਉਂਕਿ ਦੋਵਾਂ ਦਾ ਸੈੱਟਅੱਪ ਪੂਰੀ ਤਰ੍ਹਾਂ ਵੱਖਰਾ ਹੈ:

- **Claude Desktop** ਨੂੰ Ollama ਐਪ ਦੇ ਇੰਟਰਫੇਸ ਤੋਂ ਕੌਂਫਿਗਰ ਕਰੋ। Shell profile ਬਦਲਣ ਦੀ ਲੋੜ ਨਹੀਂ।
- **Claude Code** ਨੂੰ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲਾਂ ਜਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਕਮਾਂਡ ਨਾਲ ਕੌਂਫਿਗਰ ਕਰੋ।

ਜੇ ਕੋਈ ਗਾਈਡ ਤੁਹਾਨੂੰ `ANTHROPIC_BASE_URL` export ਕਰਨ ਅਤੇ ਫਿਰ `claude` ਚਲਾਉਣ ਲਈ ਕਹਿੰਦੀ ਹੈ, ਤਾਂ ਉਸ ਨੇ ਕਮਾਂਡ-ਲਾਈਨ ਟੂਲ ਕੌਂਫਿਗਰ ਕੀਤਾ ਹੈ। ਜੇ ਤੁਸੀਂ ਉਹਨਾਂ ਕਦਮਾਂ ਤੋਂ ਬਾਅਦ Cowork ਦੀ desktop ਵਰਤੋਂ ਦੀ ਉਮੀਦ ਕੀਤੀ ਸੀ, **ਤਾਂ ਸੈੱਟਅੱਪ ਟੁੱਟਿਆ ਨਹੀਂ ਹੈ। ਤੁਸੀਂ ਕੋਈ ਹੋਰ ਉਤਪਾਦ ਕੌਂਫਿਗਰ ਕੀਤਾ ਹੈ।**

## Claude Desktop ਅਤੇ Cowork ਸੈੱਟਅੱਪ

ਇਹ ਰਾਹ ਟਰਮੀਨਲ ਦੀ ਬਜਾਏ Ollama ਐਪ ਵਿੱਚ ਪੂਰਾ ਹੁੰਦਾ ਹੈ।

### ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ

- macOS ਤੇ **Ollama ਇੰਸਟਾਲ ਹੋਵੇ**। Windows ਸਮਰਥਨ ਆਉਣ ਵਾਲਾ ਦਰਸਾਇਆ ਗਿਆ ਹੈ।
- ਸਥਾਨਕ ਤੌਰ ਤੇ ਚਲਾਉਣ ਲਈ ਪਹਿਲਾਂ **ਇੱਕ ਮਾਡਲ ਡਾਊਨਲੋਡ ਕਰੋ**। ਕਲਾਊਡ ਮਾਡਲ ਲਈ Ollama ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰਕੇ cloud models ਚਾਲੂ ਕਰੋ। ਕੁਝ ਲਈ ਭੁਗਤਾਨ ਵਾਲਾ ਪਲਾਨ ਲੋੜੀਂਦਾ ਹੈ।
- **Claude ਇੰਸਟਾਲ ਹੋਵੇ।** ਨਾ ਹੋਣ ਤੇ Ollama ਸੈੱਟਅੱਪ ਦੌਰਾਨ ਇਸਨੂੰ ਡਾਊਨਲੋਡ ਕਰਨ ਦੀ ਪੇਸ਼ਕਸ਼ ਕਰਦਾ ਹੈ।

### ਕਦਮ

1. Ollama ਖੋਲ੍ਹੋ ਅਤੇ **Apps** ਚੁਣੋ।
2. **Connect Claude** ਚੁਣੋ।
3. ਸੈੱਟਅੱਪ ਦੇ ਨਿਰਦੇਸ਼ ਮੰਨੋ। ਪੁੱਛੇ ਜਾਣ ਤੇ Claude ਇੰਸਟਾਲ ਕਰੋ ਅਤੇ ਕਹਿਣ ਤੇ ਮੁੜ ਚਲਾਓ।

ਇਹ ਪੂਰਾ ਤਰੀਕਾ ਹੈ। ਬਾਅਦ ਵਿੱਚ ਮਾਡਲ ਬਦਲਣ ਲਈ **Ollama Settings** ਖੋਲ੍ਹੋ, **Apps** ਤੇ ਜਾਓ, ਮਾਡਲ ਚੁਣੋ ਅਤੇ **Restart Claude** ਦਬਾਓ।

### ਮਿਲਣ ਵਾਲੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

Ollama ਦੇ ਦਸਤਾਵੇਜ਼ ਇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਵਿੱਚ ਚਾਰ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸਮਰਥਿਤ ਦੱਸਦੇ ਹਨ:

- ਔਖੇ ਕੰਮ ਪੂਰੇ ਕਰਨ ਲਈ **Cowork**
- ਵੱਡੇ ਕੰਮ ਕਈ ਏਜੰਟਾਂ ਵਿੱਚ ਵੰਡਣ ਲਈ **Subagents**
- Ollama ਵੱਲੋਂ ਮੂਲ ਰੂਪ ਵਿੱਚ ਦਿੱਤੀ **Web search**
- **Auto mode**, ਜਿਸ ਵਿੱਚ ਏਜੰਟ ਫ਼ੈਸਲਾ ਕਰਦਾ ਹੈ ਕਿ ਬਦਲਾਅ ਤੋਂ ਪਹਿਲਾਂ ਕਦੋਂ ਪੁੱਛਣਾ ਹੈ

*Cowork ਇਸ ਸੂਚੀ ਵਿੱਚ ਹੈ। ਇਹ ਇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਰਾਹੀਂ ਉਪਲਬਧ ਹੈ, ਕਮਾਂਡ-ਲਾਈਨ ਵਾਲੇ ਰਾਹ ਰਾਹੀਂ ਨਹੀਂ।*

### ਡਿਸਕਨੈਕਟ ਕਰਨਾ

ਡਿਸਕਨੈਕਟ ਕਰਨ ਤੇ Claude ਦੀ ਪਿਛਲੀ ਕੌਂਫਿਗਰੇਸ਼ਨ ਵਾਪਸ ਆਉਂਦੀ ਹੈ, ਇਸ ਲਈ ਇਹ ਬਦਲਾਅ ਨੁਕਸਾਨਦਾਇਕ ਨਹੀਂ।

- ਇੰਟਰਫੇਸ ਵਿੱਚ **Apps** ਖੋਲ੍ਹੋ, Claude ਨੂੰ ਡਿਸਕਨੈਕਟ ਕਰੋ ਅਤੇ ਪੁੱਛਣ ਤੇ ਮੁੜ ਚਲਾਓ।
- ਟਰਮੀਨਲ ਤੋਂ `ollama launch claude-desktop --restore` ਚਲਾਓ।
- **Claude ਜੁੜਿਆ ਹੋਣ ਤੇ Ollama ਬੰਦ ਕਰਨ ਨਾਲ ਵੀ Claude ਦੀ ਆਮ ਕੌਂਫਿਗਰੇਸ਼ਨ ਵਾਪਸ ਆਉਂਦੀ ਹੈ।** ਸਥਾਨਕ ਸੈੱਟਅੱਪ ਰੱਖਣ ਲਈ Ollama ਚਾਲੂ ਛੱਡੋ।

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="ਚਿੱਤਰ ਵਿੱਚ Ollama ਐਪ ਦੇ Apps ਪੈਨਲ ਰਾਹੀਂ Claude Desktop ਨਾਲ ਕਨੈਕਸ਼ਨ, Ollama ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਮਾਡਲ ਚੋਣ ਅਤੇ ਮੂਲ ਕੌਂਫਿਗਰੇਸ਼ਨ ਮੁੜ ਲਿਆਉਣ ਦਾ ਰਾਹ ਦਿਖਾਇਆ ਗਿਆ ਹੈ" >}}

## CLI ਤੋਂ Claude Code ਸੈੱਟਅੱਪ

ਲਗਭਗ ਹਰ ਗਾਈਡ ਇਸ ਰਾਹ ਬਾਰੇ ਦੱਸਦੀ ਹੈ। ਟਰਮੀਨਲ ਵਿੱਚ ਕੰਮ ਲਈ ਇਹੀ ਢੁਕਵਾਂ ਹੈ।

### ਇੱਕ-ਕਮਾਂਡ ਤਰੀਕਾ

```bash
ollama launch claude
```

ਇਹ ਕਮਾਂਡ ਲੋੜੀਂਦੇ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਸੈੱਟ ਕਰਦੀ ਹੈ, Claude Code ਨੂੰ ਤੁਹਾਡੇ ਸਥਾਨਕ Ollama instance ਵੱਲ ਭੇਜਦੀ ਹੈ ਅਤੇ ਚਲਾਉਂਦੀ ਹੈ। ਸੂਚੀ ਵਿੱਚੋਂ ਮਾਡਲ ਚੁਣੋ ਅਤੇ Enter ਦਬਾਓ। ਪਹਿਲਾਂ ਹੀ ਮਾਡਲ ਦੱਸਣ ਲਈ ਇਹ flag ਜੋੜੋ:

```bash
ollama launch claude --model qwen3.5
```

*Wrapper ਤੁਹਾਡੇ ਲਈ ਵਾਤਾਵਰਣ ਸੰਭਾਲਦਾ ਹੈ। ਅਗਲਾ ਭਾਗ ਵੀ ਪੜ੍ਹੋ, ਕਿਉਂਕਿ ਇਹ ਜਾਣਨਾ ਕਿ ਕੀ ਸੈੱਟ ਹੁੰਦਾ ਹੈ, ਬਾਅਦ ਵਿੱਚ ਸਮੱਸਿਆ ਸੁਲਝਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।*

### ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਹੱਥੀਂ ਸੈੱਟ ਕਰਨਾ

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**ਦੂਜੀ ਲਾਈਨ ਪ੍ਰਸਿੱਧ ਗਾਈਡਾਂ ਵਿੱਚ ਅਕਸਰ ਨਹੀਂ ਹੁੰਦੀ।** `ANTHROPIC_API_KEY` ਨੂੰ ਖਾਲੀ string ਕਰਨ ਨਾਲ ਵਾਤਾਵਰਣ ਵਿੱਚ ਪਹਿਲਾਂ ਮੌਜੂਦ ਅਸਲੀ key ਸਥਾਨਕ ਕਨੈਕਸ਼ਨ ਵਿੱਚ ਰੁਕਾਵਟ ਨਹੀਂ ਪਾਉਂਦੀ। ਜੇ ਪ੍ਰਕਾਸ਼ਿਤ ਗਾਈਡ ਇਹ ਲਾਈਨ ਛੱਡੇ, ਤਾਂ ਪਹਿਲਾਂ key export ਕਰ ਚੁੱਕੇ ਪਾਠਕਾਂ ਨੂੰ ਉਲਝਾਉਣ ਵਾਲੀ ਗ਼ਲਤੀ ਮਿਲੇਗੀ।

Shell profile ਬਦਲੇ ਬਿਨਾਂ ਸਭ ਕੁਝ ਕਮਾਂਡ ਵਿੱਚ ਦੇਣ ਲਈ:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

ਸਰਕਾਰੀ ਦਸਤਾਵੇਜ਼ਾਂ ਦੀਆਂ ਦੋ ਗੱਲਾਂ:

- **`ANTHROPIC_AUTH_TOKEN` bearer authentication ਰੱਖਦਾ ਹੈ**, ਇਸ ਲਈ ਸਥਾਨਕ ਮੋਡ ਵਿੱਚ ਇਸ ਦਾ ਅਸਲ ਮੁੱਲ `ollama` ਹੈ।
- **Claude ਦੀਆਂ ਆਪਣੀਆਂ settings ਫ਼ਾਈਲਾਂ shell ਵੇਰੀਏਬਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।** ਨਵੇਂ ਮੁੱਲ export ਕਰਨ ਤੋਂ ਬਾਅਦ ਕਨੈਕਸ਼ਨ ਅਜੀਬ ਚਲੇ ਤਾਂ settings ਵੇਖੋ ਅਤੇ ਵਰਤੇ ਜਾ ਰਹੇ endpoint ਨੂੰ ਵੇਖਣ ਲਈ Claude Code ਵਿੱਚ `/status` ਚਲਾਓ।

### ਸਿੱਧਾ Ollama Cloud ਨਾਲ ਜੁੜਨਾ

ਇਸ ਰਾਹ ਲਈ Ollama ਇੰਸਟਾਲ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ। API key ਸੈੱਟ ਕਰੋ ਅਤੇ Claude Code ਨੂੰ Ollama ਦੇ hosted endpoint ਵੱਲ ਭੇਜੋ:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**ਇਸ ਰਾਹ ਦੀ ਇੱਕ ਸੀਮਾ ਹੈ।** Ollama ਦੇ ਦਸਤਾਵੇਜ਼ ਮੁਤਾਬਕ hosted web search ਅਤੇ ਉੱਨਤ tool control ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਮਰਥਿਤ ਨਹੀਂ। ਅਨੁਕੂਲ ਮਾਡਲਾਂ ਨਾਲ ਆਮ chat, ਫ਼ਾਈਲ ਸੋਧ ਅਤੇ tool calling ਕੰਮ ਕਰਦੇ ਹਨ।

## ਸਤੰਬਰ 2026 ਲਈ ਮਾਡਲ ਚੋਣ

2026 ਵਿੱਚ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ ਕਾਫ਼ੀ ਬਦਲੀ। ਬਸੰਤ ਵਿੱਚ ਲਿਖੀ ਸਲਾਹ ਮੁੜ ਜਾਂਚਣੀ ਚਾਹੀਦੀ ਹੈ।

| ਮਾਡਲ | ਕਿਸਮ | ਕਨਟੈਕਸਟ | ਕਿਉਂ ਚੁਣੋ |
|---|---|---|---|
| **Qwen3.8 27B** | ਸਥਾਨਕ, 18 GB | 256K | ਦ੍ਰਿਸ਼ਟੀ, tool calling ਅਤੇ thinking control ਵਾਲਾ ਮੌਜੂਦਾ ਵਧੀਆ ਸਥਾਨਕ ਆਮ-ਮਕਸਦ ਮਾਡਲ |
| **Qwen3 Coder Next** | ਸਥਾਨਕ, ਕੁੱਲ MoE 80B / ਸਰਗਰਮ 3B | 256K | ਹਮੇਸ਼ਾਂ ਚੱਲਣ ਵਾਲੇ ਕੋਡਿੰਗ ਏਜੰਟਾਂ ਲਈ ਬਣਿਆ, ਤੇਜ਼ੀ ਲਈ non-thinking mode |
| **Qwen3.6 35B A3B** | ਸਥਾਨਕ, MoE 35B / ਸਰਗਰਮ 3B | 262K | Apache 2.0 ਅਤੇ ਘੱਟ ਮੈਮਰੀ ਵਿੱਚ ਕੁਸ਼ਲ |
| **kimi-k2.7-code:cloud** | ਕਲਾਊਡ | ਵੱਡਾ | ਸਥਾਨਕ ਹਾਰਡਵੇਅਰ ਤੋਂ ਬਿਨਾਂ ਕੋਡਿੰਗ ਲਈ ਕਲਾਊਡ ਮਾਡਲ |
| **glm-5.3-flash** | ਕਲਾਊਡ | ਵੱਡਾ | Ollama ਦੇ ਆਪਣੇ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਪਹਿਲਾਂ ਸੁਝਾਇਆ ਮਾਡਲ |

**ਮੈਮਰੀ ਕਾਫ਼ੀ ਹੋਵੇ ਤਾਂ Qwen3.8 27B ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** ਇਹ 256K ਕਨਟੈਕਸਟ ਵਿੰਡੋ, native vision, tool calling ਅਤੇ ਹਰ ਬੇਨਤੀ ਲਈ ਬਦਲੀ ਜਾ ਸਕਣ ਵਾਲੀ thinking ਨਾਲ ਸਥਾਨਕ ਤੌਰ ਤੇ ਚੱਲਦਾ ਹੈ। 24 GB ਜਾਂ ਵੱਧ ਵਾਲੇ ਕਾਰਡ ਤੇ ਰੋਜ਼ਾਨਾ ਕੰਮ ਲਈ ਇਹ ਸੁਵਿਧਾਜਨਕ ਹੈ।

**ਮੈਮਰੀ ਨਾ ਹੋਵੇ ਤਾਂ ਕਲਾਊਡ ਮਾਡਲ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** Claude Code ਨੂੰ hosted ਮਾਡਲ ਨਾਲ ਅਜ਼ਮਾਉਣ ਦੀ ਕੋਈ ਲਾਗਤ ਨਹੀਂ ਅਤੇ ਹਾਰਡਵੇਅਰ ਦੀ ਚਿੰਤਾ ਨਹੀਂ ਰਹਿੰਦੀ, ਪਰ ਤੁਹਾਡਾ ਕੋਡ ਡਿਵਾਈਸ ਤੋਂ ਬਾਹਰ ਜਾਂਦਾ ਹੈ।

### Ternary ਮਾਡਲਾਂ ਬਾਰੇ ਚੇਤਾਵਨੀ

ਸਾਡੀ **[ਸਥਾਨਕ AI ਗਾਈਡ](/articles/local-ai-2026-build-your-rig-now/)** ਦੱਸਦੀ ਹੈ ਕਿ ternary Bonsai 2 27B, **5.53 GiB** ਵਿੱਚ ਪੂਰਾ 27B ਮਾਡਲ ਚਲਾਉਂਦਾ ਹੈ। ਇੱਥੇ ਵੀ ਇਸ ਨੂੰ ਵਰਤਣ ਦਾ ਮਨ ਕਰ ਸਕਦਾ ਹੈ।

**ਇਹ ਇਸ workflow ਵਿੱਚ ਨਹੀਂ ਚੱਲੇਗਾ।** Ternary kernels Prism ML ਦੇ llama.cpp fork ਵਿੱਚ ਹਨ ਅਤੇ stock Ollama ਉਹ ਫ਼ਾਈਲਾਂ ਲੋਡ ਨਹੀਂ ਕਰ ਸਕਦਾ। `ollama launch claude --model Ternary-Bonsai-2-27B` ਵਰਗੀ ਕਮਾਂਡ inference ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਹੀ ਫੇਲ੍ਹ ਹੁੰਦੀ ਹੈ। Claude Code ਲਈ standard Qwen3.8 27B package ਵਰਤੋ ਅਤੇ ternary packages ਨੂੰ ਅਨੁਕੂਲ runtime ਲਈ ਰੱਖੋ।

*ਇੱਥੇ ਸਹੂਲਤ ਅਤੇ ਵੱਧ ਤੋਂ ਵੱਧ ਕੁਸ਼ਲਤਾ ਲਈ ਵੱਖਰੇ ਚੋਣਾਂ ਹਨ। ਇਕੱਠੇ ਟੂਲ standard GGUF ਚਾਹੁੰਦੇ ਹਨ।*

## ਮਾਡਲ ਨੂੰ ਦੋਸ਼ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਕਨਟੈਕਸਟ 64K ਕਰੋ

ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਕੰਮ ਲਈ Ollama ਦਸਤਾਵੇਜ਼ ਇੱਕ ਸਿੱਧਾ ਨਿਰਦੇਸ਼ ਦਿੰਦੇ ਹਨ: ਮਾਡਲ ਚੁਣੋ ਅਤੇ **ਕਨਟੈਕਸਟ ਵਿੰਡੋ 64K ਜਾਂ ਵੱਧ ਰੱਖੋ**। ਵੱਡੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ ਲਈ ਇਸਨੂੰ ਹੋਰ ਵਧਾਓ।

Claude Code ਫ਼ਾਈਲਾਂ ਦਾ ਪਾਠ, diff ਅਤੇ ਕਮਾਂਡ ਦੀ output ਕਨਟੈਕਸਟ ਵਿੰਡੋ ਵਿੱਚ ਰੱਖਦਾ ਹੈ। ਛੋਟੀ default value ਹੋਵੇ ਤਾਂ ਕੰਮ ਮੁੱਕਣ ਤੋਂ ਪਹਿਲਾਂ ਥਾਂ ਖ਼ਤਮ ਹੋ ਜਾਂਦੀ ਹੈ। ਸਮੱਸਿਆ reasoning ਦੀ ਲੱਗਦੀ ਹੈ, ਪਰ ਕਾਰਨ ਸੈਟਿੰਗ ਹੁੰਦੀ ਹੈ।

| ਕਨਟੈਕਸਟ | ਕੀ ਸੰਭਾਲਦਾ ਹੈ |
|---|---|
| 32K ਤੋਂ ਘੱਟ | ਇੱਕ ਫ਼ਾਈਲ ਵਿੱਚ ਸੋਧਾਂ ਅਤੇ ਛੋਟੇ ਸਵਾਲ |
| **64K** | ਦਰਮਿਆਨੀ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਕਈ ਫ਼ਾਈਲਾਂ ਦਾ ਕੰਮ |
| 128K | ਵੱਡੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ ਅਤੇ ਲੰਮੀ ਕਮਾਂਡ output |
| 256K | Qwen3.8 27B ਦੀ ਪੂਰੀ ਵਿੰਡੋ |

*ਜੇ Claude Code ਕੰਮ ਦੇ ਵਿਚਕਾਰ ਲੜੀ ਭੁੱਲ ਜਾਵੇ, ਤਾਂ ਮਾਡਲ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਕਨਟੈਕਸਟ ਸੈਟਿੰਗ ਵੇਖੋ।*

## ਇੱਕ ਕਮਾਂਡ ਨਾਲ tool calling ਜਾਂਚੋ

Tool calling ਹੀ ਏਜੰਟ ਅਤੇ text generator ਵਿਚਕਾਰ ਫ਼ਰਕ ਹੈ। ਇਹ ਮੰਨਣ ਦੀ ਬਜਾਏ ਜਾਂਚੋ।

Claude Code ਚੱਲਣ ਤੇ ਇਸਨੂੰ ਕਹੋ:

```text
Read the current directory and list all files
```

**ਜੇ ਇਹ ਅਸਲ ਫ਼ਾਈਲਾਂ ਦਿਖਾਏ, ਤਾਂ tool calling ਕੰਮ ਕਰ ਰਹੀ ਹੈ।** ਜੇ ਇਹ ਕਹੇ ਕਿ ਇਹ directory ਪੜ੍ਹੇਗਾ ਅਤੇ ਦੱਸੇ ਕਿ ਕੀ ਮਿਲਣ ਦੀ ਉਮੀਦ ਹੈ, ਤਾਂ ਵਿਸ਼ੇਸ਼ਤਾ ਜੁੜੀ ਨਹੀਂ। ਤੁਸੀਂ ਕੋਡਿੰਗ prompt ਲੱਗੇ chat ਮਾਡਲ ਨਾਲ ਗੱਲ ਕਰ ਰਹੇ ਹੋ, ਏਜੰਟ ਨਾਲ ਨਹੀਂ। ਹੋਰ prompt ਦੇਣ ਨਾਲ ਇਹ ਠੀਕ ਨਹੀਂ ਹੋਵੇਗਾ।

ਇਸ ਕ੍ਰਮ ਵਿੱਚ ਕਾਰਨ ਵੇਖੋ:

1. **ਪੱਕੇ tool support ਵਾਲੇ ਮਾਡਲ ਤੇ ਜਾਓ।** ਹਰ ਮਾਡਲ ਇਹ ਨਹੀਂ ਕਰਦਾ ਅਤੇ parameter count ਤੋਂ ਇਹ ਗੱਲ ਨਹੀਂ ਪਤਾ ਲੱਗਦੀ।
2. **ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਵਾਤਾਵਰਣ Ollama ਵੱਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ।** `ollama --version` ਚਲਾਓ ਅਤੇ ਵੇਖੋ ਕਿ `ANTHROPIC_BASE_URL` ਸਥਾਨਕ endpoint ਤੇ ਹੈ।
3. **Claude Code ਵਿੱਚ `/status` ਚਲਾਓ।** Claude ਦੀ settings ਫ਼ਾਈਲ ਵਿੱਚ base URL ਜਾਂ credential ਹੁਣੇ export ਕੀਤੇ shell ਵੇਰੀਏਬਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਲਾਗੂ ਹੁੰਦੇ ਹਨ।

## ਕਿਹੜੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸਿਰਫ਼ ਕਲਾਊਡ ਤੇ ਰਹਿੰਦੀਆਂ ਹਨ

ਸਥਾਨਕ inference ਦੇ ਆਲੇ-ਦੁਆਲੇ workflow ਬਣਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਹੱਦ ਜਾਣੋ।

| ਵਿਸ਼ੇਸ਼ਤਾ | ਸਥਾਨਕ ਮਾਡਲਾਂ ਨਾਲ | ਕਲਾਊਡ |
|---|---|---|
| Chat ਅਤੇ ਫ਼ਾਈਲ ਸੋਧ | ਹਾਂ | ਹਾਂ |
| Tool calling | ਮਾਡਲ ਤੇ ਨਿਰਭਰ | ਹਾਂ |
| Subagents | ਹਾਂ | ਹਾਂ |
| ਵੈੱਬ ਖੋਜ | Ollama ਰਾਹੀਂ | ਹਾਂ |
| **Cowork** | Claude Desktop ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਰਾਹੀਂ | ਹਾਂ |
| Auto mode | Claude Desktop ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਰਾਹੀਂ | ਹਾਂ |
| ਨਿਰਧਾਰਤ prompts | Claude Code ਵਿੱਚ `/loop` ਰਾਹੀਂ | ਹਾਂ |

ਸਥਾਨਕ ਪਾਸੇ ਤਿੰਨ ਗੱਲਾਂ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ:

- **ਕਈ ਫ਼ਾਈਲਾਂ ਉੱਤੇ reasoning, ਗਤੀ ਨਾਲੋਂ ਪਹਿਲਾਂ ਕਮਜ਼ੋਰ ਹੁੰਦੀ ਹੈ।** ਸਥਾਨਕ ਮਾਡਲ ਇੱਕ ਫ਼ਾਈਲ ਚੰਗੀ, ਤਿੰਨ ਠੀਕ-ਠਾਕ ਅਤੇ ਪੂਰੀ ਰਿਪੋਜ਼ਟਰੀ ਕਮਜ਼ੋਰ ਸੰਭਾਲਦਾ ਹੈ। ਕੰਮ ਦਾ ਆਕਾਰ ਉਸ ਮੁਤਾਬਕ ਰੱਖੋ।
- **ਕੁਝ ਕਲਾਊਡ ਮਾਡਲਾਂ ਲਈ Ollama ਦਾ ਭੁਗਤਾਨ ਵਾਲਾ ਪਲਾਨ ਚਾਹੀਦਾ ਹੈ।** ਸਾਈਨ ਇਨ ਕਰਕੇ ਉਹਨਾਂ ਨੂੰ ਚਾਲੂ ਵੀ ਕਰਨਾ ਪੈਂਦਾ ਹੈ।
- **ਸਿੱਧੇ ਕਲਾਊਡ ਵਾਲੇ ਰਾਹ ਵਿੱਚ ਕੁਝ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸੀਮਿਤ ਹਨ।** ਸਥਾਨਕ ਇੰਸਟਾਲ ਛੱਡਣ ਤੇ hosted web search ਅਤੇ ਉੱਨਤ tool control ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਮਰਥਿਤ ਨਹੀਂ।

*ਸਥਾਨਕ inference ਸੀਮਿਤ ਅਤੇ ਜਾਂਚਯੋਗ ਕੰਮ ਲਈ ਵਧੀਆ ਹੈ, ਵੱਡੇ ਅਤੇ ਅਸਪਸ਼ਟ ਕੰਮ ਲਈ ਘੱਟ ਢੁਕਵਾਂ। ਇਸ ਹੱਦ ਮੁਤਾਬਕ ਯੋਜਨਾ ਬਣਾਓ।*

## ਆਟੋਮੇਸ਼ਨ

ਦੋ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਇੰਟਰੈਕਟਿਵ ਵਰਤੋਂ ਤੋਂ ਅੱਗੇ ਜਾਣ ਦਿੰਦੀਆਂ ਹਨ।

### Scripts ਅਤੇ CI ਲਈ headless runs

`--yes` flag ਇੰਟਰੈਕਟਿਵ ਚੋਣਾਂ ਛੱਡਦਾ ਹੈ ਅਤੇ ਲੋੜ ਪਏ ਤਾਂ ਮਾਡਲ ਖਿੱਚਦਾ ਹੈ। ਇਸ ਲਈ `--model` ਲੋੜੀਂਦਾ ਹੈ ਅਤੇ `--` ਤੋਂ ਬਾਅਦ ਦਾ ਸਭ ਕੁਝ Claude Code ਨੂੰ ਸਿੱਧਾ ਮਿਲਦਾ ਹੈ:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Permission model ਦਾ ਧਿਆਨ ਰੱਖੋ।** Claude Code ਜ਼ਿਆਦਾਤਰ ਕੰਮਾਂ ਤੋਂ ਪਹਿਲਾਂ ਪੁੱਛਦਾ ਹੈ, ਇਸ ਲਈ headless run ਲਈ ਪਹਿਲਾਂ ਕੌਂਫਿਗਰ ਕੀਤੇ permission rules ਜਾਂ ਇਕੱਲਾ ਵਾਤਾਵਰਣ ਚਾਹੀਦਾ ਹੈ। ਬਿਨਾਂ ਨਿਗਰਾਨੀ ਵਾਲਾ ਏਜੰਟ ਅਹਿਮ ਰਿਪੋਜ਼ਟਰੀ ਵੱਲ ਨਾ ਭੇਜੋ।

### `/loop` ਨਾਲ ਨਿਰਧਾਰਤ prompts

Claude Code session ਵਿੱਚ `/loop` ਨਿਰਧਾਰਤ ਸਮੇਂ ਤੇ prompt ਜਾਂ slash command ਚਲਾਉਂਦਾ ਹੈ:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Session ਖੁੱਲ੍ਹੀ ਹੋਣ ਤੱਕ ਇਹ ਚਲਦਾ ਹੈ। ਇਹ background daemon ਨਹੀਂ, ਇਸ ਲਈ session ਮੁੱਕਣ ਤੇ ਰੁਕ ਜਾਂਦਾ ਹੈ।*

## ਸਮੱਸਿਆ ਹੱਲ ਕਰਨਾ

| ਲੱਛਣ | ਸੰਭਾਵੀ ਕਾਰਨ | ਹੱਲ |
|---|---|---|
| **ਕਨੈਕਸ਼ਨ ਇਨਕਾਰ ਹੋਇਆ** | Ollama ਨਹੀਂ ਚੱਲ ਰਿਹਾ | `ollama serve` ਚਲਾਓ ਅਤੇ `curl http://localhost:11434/api/tags` ਨਾਲ ਜਾਂਚੋ |
| **ਕੰਮ ਕਰਨ ਦੀ ਬਜਾਏ ਉਸਦਾ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ** | ਚੁਣਿਆ ਮਾਡਲ tool calling ਨਹੀਂ ਕਰਦਾ | ਪੱਕੇ tool support ਵਾਲੇ ਮਾਡਲ ਤੇ ਜਾਓ |
| **ਸਥਾਨਕ endpoint ਦੀ ਥਾਂ ਅਸਲੀ API key ਵਰਤੀ ਜਾਂਦੀ ਹੈ** | `ANTHROPIC_API_KEY` ਹਾਲੇ export ਹੈ | ਇਸਨੂੰ ਉੱਪਰ ਵਾਂਗ ਖਾਲੀ string ਕਰੋ |
| **ਸੈੱਟਅੱਪ ਤੋਂ ਬਾਅਦ Cowork ਗਾਇਬ ਹੈ** | Claude Desktop ਦੀ ਥਾਂ Claude Code CLI ਸੈੱਟ ਹੋਇਆ | Cowork ਲਈ Ollama ਦਾ **Apps** ਰਾਹ ਵਰਤੋ |
| **Generation ਹੌਲੀ ਹੈ** | ਕਨਟੈਕਸਟ ਬਹੁਤ ਵੱਡਾ ਜਾਂ sparse ਮਾਡਲ ਦੀ ਥਾਂ dense ਮਾਡਲ ਚੁਣਿਆ | ਕਨਟੈਕਸਟ ਘਟਾਓ, ਫਿਰ mixture-of-experts ਮਾਡਲ ਅਜ਼ਮਾਓ |
| **Export ਕੀਤੇ ਵੇਰੀਏਬਲ ਅਸਰ ਨਹੀਂ ਕਰਦੇ** | Claude ਦੀਆਂ settings ਫ਼ਾਈਲਾਂ shell ਵੇਰੀਏਬਲਾਂ ਤੋਂ ਪਹਿਲਾਂ ਹਨ | settings ਫ਼ਾਈਲਾਂ ਵੇਖੋ, ਫਿਰ `/status` ਚਲਾਓ |
| **Background ਬੇਨਤੀਆਂ ਫੇਲ੍ਹ ਹੁੰਦੀਆਂ ਹਨ** | Claude Code ਅੰਦਰੂਨੀ ਕੰਮ ਲਈ ਛੋਟਾ ਮਾਡਲ ਚੁਣਦਾ ਹੈ | ਛੋਟੇ ਮਾਡਲ ਦਾ override ਉਸੇ ਸਥਾਨਕ ਮਾਡਲ ਤੇ ਰੱਖੋ |

*ਇਹਨਾਂ ਸੱਤ ਵਿੱਚੋਂ ਦੋ ਸਮੱਸਿਆਵਾਂ ਦਾ ਕਾਰਨ ਇੱਕੋ ਹੈ। ਜ਼ਿਆਦਾਤਰ ਸੈੱਟਅੱਪ ਗ਼ਲਤੀਆਂ ਗ਼ਲਤ endpoint ਜਾਂ tool calling ਨਾ ਕਰਨ ਵਾਲੇ ਮਾਡਲ ਕਰਕੇ ਹੁੰਦੀਆਂ ਹਨ।*

## ਮੁੱਖ ਗੱਲਾਂ

- **Claude Desktop ਅਤੇ Claude Code ਵੱਖਰੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹਨ।** Cowork, Claude Desktop ਵਿੱਚ ਹੈ ਅਤੇ macOS ਤੇ Ollama ਦੇ **Apps** ਪੈਨਲ ਤੋਂ ਸੈੱਟ ਹੁੰਦਾ ਹੈ। CLI ਰਾਹ Cowork ਨਹੀਂ ਦਿੰਦਾ।
- **ਇੱਕ ਕਮਾਂਡ CLI ਰਾਹ ਸ਼ੁਰੂ ਕਰਦੀ ਹੈ:** `ollama launch claude`। ਹੱਥੀਂ ਸੈੱਟ ਕਰਨ ਲਈ ਤਿੰਨ ਵੇਰੀਏਬਲ ਚਾਹੀਦੇ ਹਨ ਅਤੇ **ਕਈ ਗਾਈਡਾਂ `ANTHROPIC_API_KEY=""` ਛੱਡ ਦਿੰਦੀਆਂ ਹਨ**।
- **ਸਥਾਨਕ ਇੰਸਟਾਲ ਲਾਜ਼ਮੀ ਨਹੀਂ।** API key ਨਾਲ Claude Code ਨੂੰ `https://ollama.com` ਵੱਲ ਭੇਜੋ।
- **ਮਾਡਲ ਨੂੰ ਪਰਖਣ ਤੋਂ ਪਹਿਲਾਂ ਕਨਟੈਕਸਟ ਘੱਟੋ-ਘੱਟ 64K ਕਰੋ।** ਛੋਟੀ ਵਿੰਡੋ reasoning ਦੀ ਨਾਕਾਮੀ ਵਰਗੀ ਲੱਗ ਸਕਦੀ ਹੈ।
- **ਇੱਕ ਬੇਨਤੀ ਨਾਲ tool calling ਜਾਂਚੋ।** ਜੇ ਮਾਡਲ ਦੱਸਦਾ ਹੈ ਕਿ ਕੀ ਕਰਦਾ, ਤਾਂ ਤੁਹਾਡੇ ਕੋਲ text generator ਹੈ, ਏਜੰਟ ਨਹੀਂ।
- **Ternary Bonsai packages ਇੱਥੇ ਨਹੀਂ ਚੱਲਦੇ।** ਇਹਨਾਂ ਨੂੰ Prism ML ਦਾ llama.cpp fork ਚਾਹੀਦਾ ਹੈ, ਜਿਸਨੂੰ stock Ollama ਲੋਡ ਨਹੀਂ ਕਰ ਸਕਦਾ।
- **ਡਿਸਕਨੈਕਟ ਕਰਨਾ ਸੁਰੱਖਿਅਤ ਹੈ।** Ollama ਬੰਦ ਕਰਨ ਨਾਲ Claude ਦੀ ਪਿਛਲੀ setting ਵਾਪਸ ਆਉਂਦੀ ਹੈ। ਟਰਮੀਨਲ ਤੋਂ `ollama launch claude-desktop --restore` ਵੀ ਚਲਾ ਸਕਦੇ ਹੋ।

## ਅਗਲੇ ਕਦਮ

1. Claude ਸੈੱਟ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ **Ollama ਇੰਸਟਾਲ ਕਰੋ ਅਤੇ ਪੱਕੇ tool support ਵਾਲਾ ਮਾਡਲ ਲਵੋ**: **[Ollama ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library)**
2. ਮੌਜੂਦਾ flags ਅਤੇ ਮਾਡਲਾਂ ਲਈ **Ollama ਦਾ Claude Code ਪੰਨਾ ਪੜ੍ਹੋ**: **[Claude Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ](https://docs.ollama.com/integrations/claude-code)**
3. Cowork ਚਾਹੀਦਾ ਹੋਵੇ ਤਾਂ **Claude Desktop ਵਾਲਾ ਪੰਨਾ ਵਰਤੋ**: **[Claude Desktop ਇੰਟੀਗ੍ਰੇਸ਼ਨ](https://docs.ollama.com/integrations/claude-desktop)**
4. ਖਰੀਦ ਤੋਂ ਪਹਿਲਾਂ **ਸਥਾਨਕ inference ਗਾਈਡ ਦੀਆਂ memory categories ਨਾਲ ਹਾਰਡਵੇਅਰ ਤੈਅ ਕਰੋ**: **[2026 ਵਿੱਚ ਸਥਾਨਕ AI: 27B ਮਾਡਲ Sonnet 4.6 ਤੋਂ ਅੱਗੇ](/articles/local-ai-2026-build-your-rig-now/)**
5. ਘੱਟ-ਬਿਜਲੀ ਵਾਲੀ ਮਸ਼ੀਨ ਤੇ ਹਮੇਸ਼ਾਂ ਚੱਲਣ ਵਾਲਾ ਏਜੰਟ ਚਾਹੀਦਾ ਹੋਵੇ ਤਾਂ **ਛੋਟੇ ਹਾਰਡਵੇਅਰ ਦੀ ਸਮਰੱਥਾ ਵੇਖੋ**: **[Raspberry Pi 4 ਜਾਂ 5 ਤੇ ਕਿਹੜੇ AI ਮਾਡਲ ਚੱਲਦੇ ਹਨ?](/articles/ai-models-raspberry-pi-4-5/)**

## ਸੰਬੰਧਿਤ ਲੇਖ

| ਲੇਖ | ਕੀ ਦੱਸਦਾ ਹੈ |
|---|---|
| **[2026 ਵਿੱਚ ਸਥਾਨਕ AI: 27B ਮਾਡਲ Sonnet 4.6 ਤੋਂ ਅੱਗੇ](/articles/local-ai-2026-build-your-rig-now/)** | ਸਥਾਨਕ inference ਦਾ benchmark, ternary quantization ਅਤੇ ਹਾਰਡਵੇਅਰ ਚੋਣ |
| **[Raspberry Pi 4 ਜਾਂ 5 ਤੇ ਕਿਹੜੇ AI ਮਾਡਲ ਚੱਲਦੇ ਹਨ?](/articles/ai-models-raspberry-pi-4-5/)** | ਹਮੇਸ਼ਾਂ ਚਾਲੂ ਛੋਟੇ ਸਹਾਇਕ ਲਈ ਸਥਾਨਕ inference |
| **[Meshtastic ਲਈ ਨਿੱਜਤਾ-ਸੁਰੱਖਿਅਤ AI ਸਹਾਇਕ ਬਣਾਉਣਾ](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | ਆਫ-ਗ੍ਰਿਡ ਰੇਡੀਓ ਚਲਾਉਣ ਵਾਲਾ ਸਥਾਨਕ ਮਾਡਲ, ਨਿੱਜਤਾ ਮੁੱਖ ਮਕਸਦ |
| **[AI ਵਿਕਾਸ ਲਈ ਵਧੀਆ VS Code extensions](/articles/best-visual-studio-code-extensions-for-ai/)** | ਸਥਾਨਕ ਕੋਡਿੰਗ ਏਜੰਟ ਨਾਲ ਵਰਤਣ ਲਈ editor ਟੂਲ |

## ਹਵਾਲੇ

1. [Claude Code ਇੰਟੀਗ੍ਰੇਸ਼ਨ - Ollama ਦਸਤਾਵੇਜ਼](https://docs.ollama.com/integrations/claude-code)
2. [Claude Desktop ਇੰਟੀਗ੍ਰੇਸ਼ਨ - Ollama ਦਸਤਾਵੇਜ਼](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library)
4. [Qwen3.8 - Ollama ਮਾਡਲ ਲਾਇਬ੍ਰੇਰੀ](https://ollama.com/library/qwen3.8)
5. [ਸਥਾਨਕ ਮਾਡਲਾਂ ਨਾਲ Claude Cowork - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism ML llama.cpp fork - ternary kernels](https://github.com/PrismML-Eng/llama.cpp)
