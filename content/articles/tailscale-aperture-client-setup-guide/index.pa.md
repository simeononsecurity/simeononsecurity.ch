---
title: "Tailscale Aperture: 2026 ਵਿੱਚ ਇਨਫਰੈਂਸ ਅਤੇ MCP ਲਈ AI ਕਲਾਇੰਟ ਸੰਰਚਿਤ ਕਰੋ"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Tailscale Aperture ਰਾਹੀਂ ਮਾਡਲ ਬੇਨਤੀਆਂ ਅਤੇ MCP ਟੂਲ ਰੂਟ ਕਰੋ। ਕਿਸੇ ਹੋਰ ਡਿਵਾਈਸ ਜਾਂ ਗੇਟਵੇ ਉੱਤੇ Codex, Claude Code, Claude Desktop, OpenCode ਅਤੇ Hermes ਸੈੱਟ ਅੱਪ ਕਰੋ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਡਿਵੈਲਪਰ ਟੂਲ", "ਨੈੱਟਵਰਕਿੰਗ"]
tags: ["Tailscale Aperture", "Aperture ਸੈੱਟਅੱਪ", "AI ਪ੍ਰੌਕਸੀ", "LLM ਗੇਟਵੇ", "MCP ਗੇਟਵੇ", "Codex Aperture", "Claude Code Aperture", "Claude Desktop Aperture", "OpenCode Aperture", "Hermes Agent Aperture", "Codex MCP", "Claude MCP", "OpenCode MCP", "Hermes MCP", "AI ਇਨਫਰੈਂਸ ਪ੍ਰੌਕਸੀ", "Responses API", "Anthropic Messages API", "ਰਿਮੋਟ MCP", "Streamable HTTP", "Tailscale", "ਸਵੈ-ਹੋਸਟ ਕੀਤੀ AI", "ਕੋਡਿੰਗ ਏਜੰਟ", "AI ਕਲਾਇੰਟ ਸੰਰਚਨਾ"]
cover: "/img/cover/tailscale-aperture-agent-setup.webp"
coverAlt: "Aperture ਵੱਖਰੇ ਨੀਲੇ ਇਨਫਰੈਂਸ ਰੂਟ ਅਤੇ ਹਰੇ ਟੂਲ ਰੂਟ ਰਾਹੀਂ ਕਲਾਇੰਟ ਪੈਨਲਾਂ ਨੂੰ ਮਾਡਲ ਅਤੇ MCP ਟੂਲ ਸੇਵਾਵਾਂ ਨਾਲ ਜੋੜਦਾ ਹੈ"
coverCaption: ""
---

## ਜਾਣ-ਪਛਾਣ

Tailscale Aperture ਮਾਡਲ ਇਨਫਰੈਂਸ ਅਤੇ ਮਾਡਲ Context ਪ੍ਰੋਟੋਕੋਲ (MCP) ਟੂਲਾਂ ਲਈ AI ਕਲਾਇੰਟਾਂ ਨੂੰ tailnet ਨਾਲ ਜੁੜਿਆ ਇੱਕ ਗੇਟਵੇ ਦਿੰਦਾ ਹੈ। ਹਰ ਕਲਾਇੰਟ ਨੂੰ ਆਪਣੇ API ਪ੍ਰੋਟੋਕੋਲ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਰੂਟ ਵਰਤਣਾ ਚਾਹੀਦਾ ਹੈ। MCP ਟੂਲ ਵੱਖਰਾ ਐਂਡਪੌਇੰਟ ਵਰਤਦੇ ਹਨ, ਅਤੇ Aperture ਦੀਆਂ ਪਹੁੰਚ ਮਨਜ਼ੂਰੀਆਂ ਤੈਅ ਕਰਦੇ ਹਨ ਕਿ ਹਰ Tailscale ਪਛਾਣ ਕਿਹੜੇ ਮਾਡਲ ਅਤੇ ਕਨੈਕਟਰ ਵਰਤ ਸਕਦੀ ਹੈ।

ਇਹ ਗਾਈਡ macOS, Linux ਅਤੇ Windows ਉੱਤੇ Codex, Claude Code, Claude Desktop, OpenCode ਅਤੇ Hermes ਦੀ ਸੰਰਚਨਾ ਦੱਸਦੀ ਹੈ। ਇਸ ਵਿੱਚ CLI ਅਤੇ ਡੈਸਕਟਾਪ ਸੈਟਿੰਗਾਂ, ਆਪਣੀ ਪਛਾਣ ਲਈ ਉਪਲਬਧ ਮਾਡਲ ID ਲੱਭਣ ਦਾ ਤਰੀਕਾ ਅਤੇ ਹੋਰ ਡਿਵਾਈਸ ਜਾਂ Aperture ਇੰਸਟੈਂਸ ਸੈੱਟ ਕਰਨ ਲਈ ਮੁੜ ਵਰਤਣਯੋਗ ਅਨਾਮ ਪ੍ਰੌਂਪਟ ਸ਼ਾਮਲ ਹੈ।

**ਰੂਟ ਦੀ ਚੋਣ:** ਐਂਡਪੌਇੰਟ ਦੇ ਰਸਤੇ ਗੇਟਵੇ ਅਤੇ ਹਰ API ਪ੍ਰੋਟੋਕੋਲ ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ। `/codex` ਵਰਗਾ Responses ਰੂਟ Anthropic Messages ਜਾਂ MCP ਟ੍ਰੈਫਿਕ ਨਹੀਂ ਸੰਭਾਲਦਾ। ਗੇਟਵੇ ਦਾ hostname ਅਤੇ ਹਰ ਕਲਾਇੰਟ ਦਾ ਇਨਫਰੈਂਸ ਰੂਟ ਪੱਕਾ ਕਰੋ। ਕਲਾਇੰਟ ਸੈਟਿੰਗਾਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ Aperture ਪਹੁੰਚ ਰਾਹੀਂ ਮਾਡਲ ID ਲੱਭੋ।

## ਮੁੱਖ ਗੱਲਾਂ

- **ਮਾਡਲ ਟ੍ਰੈਫਿਕ** ਲਈ ਕਲਾਇੰਟ ਪ੍ਰੋਟੋਕੋਲ ਵਾਲਾ API ਰੂਟ ਚਾਹੀਦਾ ਹੈ।
- **MCP ਟ੍ਰੈਫਿਕ** ਵੱਖਰਾ `/v1/mcp` ਐਂਡਪੌਇੰਟ ਵਰਤਦਾ ਹੈ।
- **ਗੇਟਵੇ ਅਧਿਕਾਰਾਂ** ਨਾਲ ਤੁਹਾਡੀ Tailscale ਪਛਾਣ ਹਰ ਮਾਡਲ ਅਤੇ ਕਨੈਕਟਰ ਵਰਤ ਸਕੇ।
- **ਕਲਾਇੰਟ ਸੰਰਚਨਾ** ਸਿਰਫ਼ ਸੈਟਿੰਗਾਂ ਸੰਭਾਲੇ ਜਾਣ ਦਾ ਸਬੂਤ ਹੈ। ਅਸਲ ਬੇਨਤੀ ਅਤੇ MCP ਟੂਲ ਕਾਲ ਜਾਂਚੋ।

## ਰੂਟ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ

| ਮਕਸਦ | ਕਲਾਇੰਟ ਬੇਨਤੀ | Aperture ਰੂਟ | ਰੂਟ ਦੀ ਸੇਵਾ |
|---|---|---|---|
| Codex ਅਤੇ Responses-ਅਨੁਕੂਲ ਮਾਡਲ | OpenAI Responses API | ਆਮ ਤੌਰ 'ਤੇ `/v1`। `/codex` ਵਰਗਾ custom ਰਸਤਾ deployment ਉੱਤੇ ਨਿਰਭਰ ਹੈ। | ਮਾਡਲ ਇਨਫਰੈਂਸ |
| Claude ਮਾਡਲ ਇਨਫਰੈਂਸ | Anthropic Messages API | ਗੇਟਵੇ ਦਾ ਮੁੱਖ URL। Aperture `/v1/messages` ਸੰਭਾਲਦਾ ਹੈ | Claude-ਅਨੁਕੂਲ ਇਨਫਰੈਂਸ |
| MCP ਟੂਲ | Streamable HTTP MCP | `/v1/mcp` | ਸੰਰਚਿਤ ਕਨੈਕਟਰਾਂ ਦੇ ਟੂਲ ਅਤੇ ਸਰੋਤ |

{{< figure src="aperture-client-routes.webp" alt="Codex ਅਤੇ Hermes Responses ਰੂਟ ਵਰਤਦੇ ਹਨ, Claude Anthropic Messages ਵਰਤਦਾ ਹੈ, ਅਤੇ MCP ਕਲਾਇੰਟ Aperture ਕਨੈਕਟਰਾਂ ਤੱਕ ਪਹੁੰਚਣ ਲਈ ਵੱਖਰਾ /v1/mcp ਰੂਟ ਵਰਤਦੇ ਹਨ" caption="ਮਾਡਲ ਇਨਫਰੈਂਸ ਅਤੇ MCP ਟ੍ਰੈਫਿਕ ਵੱਖਰੇ Aperture endpoints ਵਰਤਦੇ ਹਨ" >}}

**ਪ੍ਰਦਾਤਾ root:** Aperture ਕਲਾਇੰਟ ਬੇਨਤੀ ਦੇ ਰਸਤੇ ਪ੍ਰਦਾਤਾ ਦੇ ਮੁੱਖ URL ਨਾਲ ਜੋੜਦਾ ਹੈ। ਪ੍ਰਦਾਤਾ ਦਾ `baseurl` ਉਸਦੇ API ਮੁੱਖ ਪਤਾ ਉੱਤੇ ਰੱਖੋ। ਜੇ ਆਉਣ ਵਾਲੇ ਰਸਤੇ ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ `/v1` ਹੈ ਤਾਂ ਅੱਪਸਟ੍ਰੀਮ ਮੁੱਖ URL ਵਿੱਚ `/v1` ਨਾ ਜੋੜੋ। URL ਬਣਤਰ, ਮਾਡਲ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਅਤੇ grants ਲਈ [Aperture ਸੰਰਚਨਾ reference](https://tailscale.com/docs/aperture/configuration) ਵੇਖੋ।

## ਗੇਟਵੇ ਤਿਆਰ ਕਰੋ

**ਸੰਪਾਦਨ ਤੋਂ ਪਹਿਲਾਂ,** Aperture ਪ੍ਰਸ਼ਾਸਕ ਤੋਂ ਇਹ ਮੁੱਲ ਲਵੋ:

- **ਗੇਟਵੇ hostname:** tailnet ਨਾਲ ਜੁੜੇ ਬਹੁਤੇ ਕਲਾਇੰਟਾਂ ਲਈ `http://` ਵਰਤੋ। Claude Desktop ਇਨਫਰੈਂਸ ਲਈ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫਿਕੇਟ ਨਾਲ `https://` ਲੋੜੀਂਦਾ ਹੈ।
- **ਇਨਫਰੈਂਸ ਰੂਟ:** OpenAI Responses ਅਤੇ Anthropic Messages ਵੱਖਰੇ ਬੇਨਤੀ ਫਾਰਮੈਟ ਵਰਤਦੇ ਹਨ।
- **ਮਾਡਲ ID:** ਹੇਠਲੇ ਐਂਡਪੌਇੰਟ ਰਾਹੀਂ ਆਪਣੀ Tailscale ਪਛਾਣ ਲਈ ਉਪਲਬਧ ਮਾਡਲ ਲੱਭੋ। ਉਸ ਪਛਾਣ ਲਈ ਵਾਪਸ ਆਏ ਸਹੀ ID ਵਰਤੋ।
- **ਪ੍ਰਮਾਣੀਕਰਨ:** ਜਾਂਚੋ ਕਿ ਕਲਾਇੰਟ ਅਸਥਾਈ ਮੁੱਲ API ਕੁੰਜੀ ਭੇਜਦਾ ਹੈ ਜਾਂ ਯੂਜ਼ਰ ਕ੍ਰੈਡੈਂਸ਼ਲ।
- **MCP ਐਂਡਪੌਇੰਟ:** tailnet ਕਲਾਇੰਟਾਂ ਲਈ ਆਮ ਤੌਰ 'ਤੇ `http://<APERTURE_HOST>/v1/mcp`। Claude Desktop ਇਨਫਰੈਂਸ ਲਈ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫਿਕੇਟ ਵਾਲਾ HTTPS ਚਾਹੀਦਾ ਹੈ।
- **ਪਹੁੰਚ grants:** ਆਪਣੀ Tailscale ਪਛਾਣ ਲਈ ਮਾਡਲ ਅਤੇ ਕਨੈਕਟਰ ਅਧਿਕਾਰ ਜਾਂਚੋ।

**ਨੈੱਟਵਰਕ ਪਹੁੰਚ:** ਕਲਾਇੰਟ ਡਿਵਾਈਸ tailnet ਰਾਹੀਂ ਗੇਟਵੇ ਤੱਕ ਪਹੁੰਚੇ। ਸਿਰਫ਼ hostname ਹੋਣ ਨਾਲ ਮਾਡਲ ਜਾਂ ਟੂਲ ਪਹੁੰਚ ਨਹੀਂ ਮਿਲਦੀ। ਮਾਡਲ ਜਾਂ ਕਨੈਕਟਰ ਲਈ ਮੇਲ ਖਾਂਦਾ ਗ੍ਰਾਂਟ ਪਹੁੰਚ ਨਾ ਦੇਵੇ ਤਾਂ Aperture ਇਨਕਾਰ ਕਰਦਾ ਹੈ।

### ਆਪਣੇ ਯੂਜ਼ਰ ਲਈ ਉਪਲਬਧ ਮਾਡਲ ਲੱਭੋ

**ਉਸੇ tailnet ਨਾਲ ਜੁੜੇ ਡਿਵਾਈਸ ਤੋਂ ਮਾਡਲ ਸੂਚੀ ਪੁੱਛੋ।** Aperture ਡਿਵਾਈਸ ਦੀ Tailscale ਪਛਾਣ ਵਰਤਦਾ ਹੈ ਅਤੇ ਉਸ ਯੂਜ਼ਰ ਨੂੰ ਦਿੱਤੇ ਮਾਡਲ ਵਾਪਸ ਕਰਦਾ ਹੈ। [ਮਾਡਲ ਗ੍ਰਾਂਟ ਗਾਈਡ](https://tailscale.com/docs/aperture/how-to/grant-model-access) ਵੇਖੋ:

```sh
# macOS ਜਾਂ Linux
curl -fsS http://<APERTURE_HOST>/v1/models
```

```powershell
# Windows PowerShell ਵਿੱਚ ਪੁਰਾਣਾ curl alias ਟਾਲਣ ਲਈ curl.exe ਵਰਤੋ
curl.exe -fsS http://<APERTURE_HOST>/v1/models
```

**ਨਤੀਜਾ ਪੜ੍ਹੋ:** ਵਾਪਸ ਆਏ ਹਰ `id` ਨੂੰ ਮਾਡਲ ID ਵਜੋਂ ਵਰਤੋ। Aperture ਪ੍ਰਦਾਤਾ ਪਛਾਣਨ ਲਈ `metadata.provider.id` ਵੇਖੋ। ਕਲਾਇੰਟ ਦੇ API ਫਾਰਮੈਟ ਨੂੰ ਸਹਾਰਾ ਦੇਣ ਵਾਲਾ ਮਾਡਲ ਚੁਣੋ। ਮਿਸਾਲ ਲਈ Claude Desktop ਨੂੰ Anthropic Messages ਮਾਡਲ ਚਾਹੀਦਾ ਹੈ। Aperture ਦੀ [ਮਾਡਲ ਡਾਇਰੈਕਟਰੀ](https://tailscale.com/docs/aperture/reference/chat) ਸਾਈਨ-ਇਨ ਯੂਜ਼ਰ ਲਈ ਉਪਲਬਧ ID ਵੀ ਦਿਖਾਉਂਦੀ ਹੈ।

**ਮਾਡਲ ਨਾ ਮਿਲਣ:** ਜੇ ਉਮੀਦ ਕੀਤਾ ਮਾਡਲ ਨਹੀਂ ਦਿਖਦਾ ਤਾਂ Aperture ਪ੍ਰਸ਼ਾਸਕ ਨੂੰ ਪ੍ਰਦਾਤਾ ਸੰਰਚਨਾ ਅਤੇ ਤੁਹਾਡਾ ਮਾਡਲ ਗ੍ਰਾਂਟ ਜਾਂਚਣ ਲਈ ਕਹੋ। ਇਸ ਐਂਡਪੌਇੰਟ ਰਾਹੀਂ ਯੂਜ਼ਰ ਆਪਣੇ ਆਪ ਨੂੰ ਪਹੁੰਚ ਨਹੀਂ ਦੇ ਸਕਦੇ।

**URL ਸਕੀਮ:** Tailscale ਇੱਕੋ tailnet ਦੇ ਬਹੁਤੇ ਕਲਾਇੰਟਾਂ ਲਈ `http://` ਦੀ ਸਲਾਹ ਦਿੰਦਾ ਹੈ। WireGuard ਇਹ ਟ੍ਰੈਫਿਕ encrypt ਕਰਦਾ ਹੈ। Claude Desktop ਨੂੰ `https://` ਅਤੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਵੱਲੋਂ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫਿਕੇਟ ਚਾਹੀਦਾ ਹੈ। ਹਰੇਕ ਕਲਾਇੰਟ ਲਈ ਹੇਠਾਂ ਦਿੱਤੀ ਸਕੀਮ ਵਰਤੋ।

### ਇਨਫਰੈਂਸ ਪ੍ਰਦਾਤਾ ਜੋੜੋ

**OpenAI Responses:** ਅੱਪਸਟ੍ਰੀਮ ਪ੍ਰਦਾਤਾ ਨੂੰ Aperture ਵਿੱਚ ਜੋੜੋ ਅਤੇ ਕਲਾਇੰਟ ਵਾਲਾ API ਫਾਰਮੈਟ ਚਾਲੂ ਕਰੋ। OpenAI ਪ੍ਰਦਾਤਾ ਲਈ ਇਹ ਹਿੱਸਾ ਜੋੜੋ:

```json
{
  "providers": {
    "openai": {
      "baseurl": "https://api.openai.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "models": ["<MODEL_ID>"],
      "compatibility": {
        "openai_chat": true,
        "openai_responses": true
      }
    }
  }
}
```

**Anthropic Messages:** Anthropic API ਮੁੱਖ ਪਤਾ, `x-api-key` authorization ਫਾਰਮੈਟ ਅਤੇ `anthropic_messages` ਅਨੁਕੂਲਤਾ ਵਰਤੋ। ਮਾਡਲ ID ਪ੍ਰਦਾਤਾ ਦੀ `models` ਸੂਚੀ ਵਿੱਚ ਵੀ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਇਹ ਹਿੱਸਾ ਜੋੜੋ:

```json
{
  "providers": {
    "anthropic": {
      "baseurl": "https://api.anthropic.com",
      "apikey": "<UPSTREAM_PROVIDER_KEY>",
      "authorization": "x-api-key",
      "models": ["<CLAUDE_MODEL_ID>"],
      "compatibility": {
        "anthropic_messages": true
      }
    }
  }
}
```

**ਸੰਰਚਨਾ ਬਦਲਾਅ:** ਹਰ ਅਸਥਾਈ ਮੁੱਲ ਨੂੰ ਅੱਪਸਟ੍ਰੀਮ ਮੁੱਲ ਨਾਲ ਬਦਲੋ। ਹਿੱਸਿਆਂ ਨੂੰ ਮੌਜੂਦਾ Aperture ਸੰਰਚਨਾ ਵਿੱਚ ਜੋੜੋ ਅਤੇ ਬਾਕੀ ਫ਼ਾਈਲ ਕਾਇਮ ਰੱਖੋ। ਪ੍ਰਦਾਤਾ ਜਿਨ੍ਹਾਂ API ਨੂੰ ਸਹਾਰਾ ਦਿੰਦਾ ਹੈ ਉਨ੍ਹਾਂ ਲਈ ਅਨੁਕੂਲਤਾ flag ਚਾਲੂ ਕਰੋ।

**ਪਹੁੰਚ grants:** Aperture ਹਰ ਮਾਡਲ ਅਤੇ ਕਨੈਕਟਰ ਲਈ ਯੂਜ਼ਰ ਪਹੁੰਚ ਕੰਟਰੋਲ ਕਰਦਾ ਹੈ। ਹਰੇਕ ਲੋੜੀਂਦੇ Tailscale ਯੂਜ਼ਰ ਨੂੰ ਸਿਰਫ਼ ਲੋੜੀਂਦੇ ਅਧਿਕਾਰ ਦਿਓ। ਇਹ ਮਿਸਾਲ ਇੱਕ ਯੂਜ਼ਰ ਨੂੰ ਇੱਕ ਪ੍ਰਦਾਤਾ ਮਾਡਲ ਅਤੇ ਇੱਕ ਕਨੈਕਟਰ ਦਿੰਦੀ ਹੈ:

```json
{
  "grants": [
    {
      "src": ["<TAILSCALE_USER>"],
      "app": {
        "tailscale.com/cap/aperture": [
          {"role": "user", "models": "openai/<MODEL_ID>"},
          {"connectors": ["teamtools/**"]}
        ]
      }
    }
  ]
}
```

**ਮਾਡਲ ਗ੍ਰਾਂਟ:** ਗ੍ਰਾਂਟ pattern ਵਿੱਚ ਪ੍ਰਦਾਤਾ ID ਅਤੇ ਮਾਡਲ ID ਵਰਤੋ। [ਕਨੈਕਟਰ ਸੈੱਟਅੱਪ guide](https://tailscale.com/docs/aperture/connectors/get-started) ਮੌਜੂਦਾ `connectors.servers` ਸੰਰਚਨਾ ਦਿਖਾਉਂਦੀ ਹੈ। ਪੁਰਾਣੀ top-level `mcp.servers` ਸੰਰਚਨਾ deprecated ਹੈ।

### MCP ਕਨੈਕਟਰ ਜੋੜੋ

**MCP ਕਨੈਕਟਰ:** Aperture ਅੱਪਸਟ੍ਰੀਮ MCP ਸਰਵਰਾਂ ਨਾਲ ਜੁੜਦਾ ਹੈ ਅਤੇ `/v1/mcp` ਉੱਤੇ ਟੂਲ ਦਿੰਦਾ ਹੈ:

```json
{
  "connectors": {
    "servers": {
      "teamtools": {
        "protocol": "mcp",
        "url": "<UPSTREAM_MCP_ENDPOINT>"
      }
    }
  }
}
```

**ਕਨੈਕਟਰ URL:** ਅੱਪਸਟ੍ਰੀਮ ਸਰਵਰ ਦਾ ਪੂਰਾ MCP ਐਂਡਪੌਇੰਟ ਵਰਤੋ। ਫਿਰ ਆਪਣੇ Tailscale ਯੂਜ਼ਰ ਨੂੰ `teamtools/**` ਜਾਂ ਹੋਰ ਸੀਮਿਤ ਟੂਲ pattern ਦੀ ਪਹੁੰਚ ਦਿਓ। [MCP ਪ੍ਰੌਕਸੀ reference](https://tailscale.com/docs/aperture/mcp-server) ਇਕੱਲੇ ਕਲਾਇੰਟ ਐਂਡਪੌਇੰਟ ਅਤੇ ਕਨੈਕਟਰ ਦੇ ਵਿਹਾਰ ਦੀ ਵਿਆਖਿਆ ਕਰਦੀ ਹੈ।

## Codex CLI ਅਤੇ ਡੈਸਕਟਾਪ

**ਸਾਂਝੀਆਂ ਸੈਟਿੰਗਾਂ:** Codex CLI ਅਤੇ ਡੈਸਕਟਾਪ ਐਪ ਇੱਕੋ ਸੰਰਚਨਾ ਵਰਤਦੇ ਹਨ। macOS ਅਤੇ Linux ਉੱਤੇ `~/.codex/config.toml` ਸੋਧੋ। Windows ਉੱਤੇ `%USERPROFILE%\.codex\config.toml` ਸੋਧੋ (ਹੋਮ ਡਾਇਰੈਕਟਰੀ ਫੈਲਾਉਣ ਵਾਲੇ shell ਵਿੱਚ `~/.codex/config.toml` ਵੀ ਚੱਲਦਾ ਹੈ)। [Codex ਐਪ ਜਾਣ-ਪਛਾਣ](https://openai.com/index/introducing-the-codex-app/) ਮੁਤਾਬਕ ਡੈਸਕਟਾਪ ਐਪ Codex CLI ਸੰਰਚਨਾ ਲੈਂਦੀ ਹੈ। Codex ਯੂਜ਼ਰ ਸੈਟਿੰਗਾਂ `~/.codex/config.toml` ਵਿੱਚ ਹਨ। [ਸੰਰਚਨਾ basics](https://learn.chatgpt.com/docs/config-file/config-basic) user-level ਪ੍ਰਦਾਤਾ ਅਤੇ MCP field ਸਮਝਾਉਂਦੀ ਹੈ। ਇਸ ਫ਼ਾਈਲ ਵਿੱਚ ਪ੍ਰਦਾਤਾ ਜੋੜੋ, ਐਪ ਮੁੜ ਚਾਲੂ ਕਰੋ ਅਤੇ UI ਵਿੱਚ ਪ੍ਰਦਾਤਾ ਤੇ ਮਾਡਲ ਦਿਖਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।

```toml
model = "<MODEL_ID>"
model_provider = "aperture"

[model_providers.aperture]
name = "Aperture Proxy"
base_url = "http://<APERTURE_HOST>/v1"
wire_api = "responses"
requires_openai_auth = true
supports_websockets = false
```

**ਵਿਕਲਪੀ field:** ਇਹ ਦੋ ਮੁੱਲ ਇੱਕ Codex ਪ੍ਰਦਾਤਾ ਸੈੱਟਅੱਪ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ। ਸਿਰਫ਼ ਤਦ ਰੱਖੋ ਜਦੋਂ ਗੇਟਵੇ ਅਤੇ Codex ਸੰਰਚਨਾ ਨੂੰ ਲੋੜ ਹੋਵੇ। Tailscale ਦੀ ਮੌਜੂਦਾ [Codex Aperture ਗਾਈਡ](https://tailscale.com/docs/aperture/how-to/use-codex) ਇਹਨਾਂ ਨੂੰ ਛੱਡਦੀ ਹੈ, `wire_api = "responses"` ਵਰਤਦੀ ਹੈ ਅਤੇ ਕਹਿੰਦੀ ਹੈ ਕਿ Aperture ਅੱਪਸਟ੍ਰੀਮ credentials ਜੋੜਦਾ ਹੈ। ਗੇਟਵੇ ਪ੍ਰਸ਼ਾਸਕ ਵੱਲੋਂ ਦਿੱਤਾ ਸਹੀ Responses URL ਵਰਤੋ। `/codex` deployment-ਖਾਸ ਰੂਟ ਹੈ। Tailscale ਦਾ ਦਰਜ ਡਿਫਾਲਟ `/v1` ਹੈ।

**MCP ਸੰਰਚਨਾ:** ਉਸੇ user ਸੰਰਚਨਾ ਵਿੱਚ ਸਰਵਰ ਜੋੜੋ:

```toml
[mcp_servers.aperture]
url = "http://<APERTURE_HOST>/v1/mcp"
enabled = true
```

**Codex ਜਾਂਚੋ:** `codex mcp list` ਚਲਾਓ, ਨਵਾਂ session ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ `/mcp` ਵੇਖੋ। ਸਰਵਰ ਸੂਚੀ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਸਾਬਤ ਕਰਦੀ ਹੈ। ਸੂਚੀ ਵਿੱਚ ਟੂਲ ਅਤੇ ਸਫਲ call ਉਸਦੀ ਖੋਜ ਅਤੇ ਚਲਾਉਣਾ ਸਾਬਤ ਕਰਦੇ ਹਨ। [Codex ਸੰਰਚਨਾ reference](https://learn.chatgpt.com/docs/config-file/config-reference) user-level ਪ੍ਰਦਾਤਾ ਅਤੇ MCP ਸੈਟਿੰਗਾਂ ਦੱਸਦੀ ਹੈ।

## Claude Code CLI

**ਪ੍ਰੋਟੋਕੋਲ:** Claude Code Anthropic Messages ਵਰਤਦਾ ਹੈ। Claude Code ਦੀ global ਸੈਟਿੰਗਾਂ file ਨੂੰ Anthropic-ਅਨੁਕੂਲ Aperture ਗੇਟਵੇ ਵੱਲ ਕਰੋ। macOS ਅਤੇ Linux ਉੱਤੇ `~/.claude/settings.json`, Windows ਉੱਤੇ `%USERPROFILE%\.claude\settings.json` ਵਰਤੋ। PowerShell ਵਿੱਚ `$HOME\.claude\settings.json` ਵਰਤੋ। ਰੂਟ ਨੂੰ `/v1/messages` ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ। Codex Responses ਵੱਖਰਾ ਪ੍ਰੋਟੋਕੋਲ ਅਤੇ ਰੂਟ ਵਰਤਦਾ ਹੈ। WireGuard ਕਨੈਕਸ਼ਨ encrypt ਕਰਦਾ ਹੈ, ਇਸ ਲਈ Tailscale tailnet ਉੱਤੇ Claude Code ਲਈ HTTP ਦੀ ਸਲਾਹ ਦਿੰਦਾ ਹੈ।

```json
{
  "apiKeyHelper": "echo '-'",
  "env": {
    "ANTHROPIC_BASE_URL": "http://<APERTURE_HOST>"
  }
}
```

**ਕਲਾਇੰਟ ਪ੍ਰਮਾਣੀਕਰਨ:** Aperture ਕਲਾਇੰਟ ਗਾਈਡ `apiKeyHelper` ਵਿੱਚ ਅਸਥਾਈ ਮੁੱਲ ਵਰਤਦੀ ਹੈ ਕਿਉਂਕਿ Aperture ਅੱਪਸਟ੍ਰੀਮ ਕ੍ਰੈਡੈਂਸ਼ਲ ਜੋੜਦਾ ਹੈ। Claude ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਸਿੱਧਾ ਅੱਗੇ ਭੇਜਣਾ ਲਈ Aperture ਦੇ Anthropic ਪ੍ਰਦਾਤਾ ਨੂੰ ਯੂਜ਼ਰ ਦਾ Claude ਕ੍ਰੈਡੈਂਸ਼ਲ ਅੱਗੇ ਭੇਜਣਾ ਪਵੇਗਾ। ਉਸ ਹਾਲਤ ਵਿੱਚ `ANTHROPIC_API_KEY` ਅਤੇ `ANTHROPIC_AUTH_TOKEN` ਸੈੱਟ ਨਾ ਕਰੋ। ਇਹ ਵੇਰੀਏਬਲ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦੀ ਥਾਂ ਲੈਂਦੇ ਹਨ। ਆਪਣੇ Claude ਕੋਡ ਵਰਜਨ ਲਈ [Claude Code Aperture ਹਦਾਇਤਾਂ](https://tailscale.com/docs/aperture/how-to/use-claude-code) ਅਤੇ ਪ੍ਰਮਾਣੀਕਰਨ ਵਿਕਲਪਾਂ ਲਈ [Anthropic ਗੇਟਵੇ guide](https://code.claude.com/docs/en/llm-gateway-connect) ਵਰਤੋ।

**HTTP ਰਾਹੀਂ MCP:** ਇਹ commands ਨਾਲ ਐਂਡਪੌਇੰਟ ਜੋੜੋ:

```sh
claude mcp add --transport http --scope user aperture http://<APERTURE_HOST>/v1/mcp
claude mcp list
```

**Claude Code ਜਾਂਚੋ:** session ਸ਼ੁਰੂ ਕਰਕੇ `/mcp` ਚਲਾਓ। Anthropic [MCP ਦਸਤਾਵੇਜ਼](https://code.claude.com/docs/en/mcp) ਵਿੱਚ ਦੂਰਲੇ MCP ਸਰਵਰਾਂ ਲਈ HTTP ਦੀ ਸਲਾਹ ਦਿੰਦਾ ਹੈ।

## Claude Desktop GUI

**ਵੱਖਰੀਆਂ ਸੈਟਿੰਗਾਂ:** Claude Desktop ਵਿੱਚ third-party ਇਨਫਰੈਂਸ ਸਕ੍ਰੀਨ ਹੈ। ਇਹ ਸੈਟਿੰਗ Claude Desktop ਦੀਆਂ ਮਾਡਲ ਬੇਨਤੀਆਂ Aperture ਰਾਹੀਂ ਭੇਜਦੀ ਹੈ। MCP ਸੰਰਚਨਾ ਵੱਖਰਾ ਕਦਮ ਹੈ।

1. macOS ਜਾਂ Windows ਵਾਲੇ Claude Desktop ਵਿੱਚ **Help > Troubleshooting > Enable Developer Mode** (ਮਦਦ > ਸਮੱਸਿਆ-ਨਿਵਾਰਣ > ਡਿਵੈਲਪਰ ਮੋਡ ਚਾਲੂ ਕਰੋ) ਚੁਣੋ। Linux ਬੀਟਾ ਵਿੱਚ ਇਹ menu ਹੋਵੇ ਤਾਂ ਵਰਤੋ। ਪੁੱਛਣ 'ਤੇ ਐਪ ਮੁੜ ਚਾਲੂ ਕਰੋ। Menu ਨਾ ਹੋਵੇ ਤਾਂ Claude Desktop update ਕਰੋ ਅਤੇ ਆਪਣੇ platform ਦੇ ਰੀਲੀਜ਼ note ਵੇਖੋ।
2. **Developer > Configure Third-Party Inference** (ਡਿਵੈਲਪਰ > ਤੀਜੀ-ਧਿਰ ਇਨਫਰੈਂਸ ਸੰਰਚਿਤ ਕਰੋ) ਚੁਣੋ।
3. **Connection type** (ਕਨੈਕਸ਼ਨ ਦੀ ਕਿਸਮ) ਨੂੰ **Gateway** (ਗੇਟਵੇ) ਅਤੇ **Credential kind** (ਪ੍ਰਮਾਣੀਕਰਨ ਜਾਣਕਾਰੀ ਦੀ ਕਿਸਮ) ਨੂੰ **Static API key** (ਸਥਿਰ API ਕੁੰਜੀ) ਬਣਾਓ।
4. **Gateway base URL** (ਗੇਟਵੇ ਦਾ ਮੂਲ URL) ਵਿੱਚ `https://<APERTURE_HOST>` ਦਾਖ਼ਲ ਕਰੋ। ਭਰੋਸੇਯੋਗ TLS ਸਰਟੀਫਿਕੇਟ ਵਾਲਾ ਪੂਰਾ hostname ਵਰਤੋ।
5. ਗੇਟਵੇ ਕੁੰਜੀ ਵਜੋਂ `aperture` ਵਰਗਾ ਖਾਲੀ ਨਾ ਹੋਣ ਵਾਲਾ ਅਸਥਾਈ ਮੁੱਲ ਲਿਖੋ। Aperture ਇਸਨੂੰ ਅਣਡਿੱਠਾ ਕਰਕੇ tailnet ਰਾਹੀਂ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਦਾ ਹੈ।
6. Custom ਇਨਫਰੈਂਸ header ਖਾਲੀ ਛੱਡੋ।
7. ਆਪਣੀ Tailscale ਪਛਾਣ ਲਈ `GET /v1/models` ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੇ ਸਹੀ ID ਨਾਲ ਇੱਕ ਚਾਲੂ ਮਾਡਲ ਜੋੜੋ। Anthropic Messages ਮਾਡਲ ਚੁਣੋ। ID, ਦਿਖਾਇਆ name ਅਤੇ ਵਿਕਲਪੀ tier ਉਪਨਾਮ ਹੱਥੀਂ ਦਾਖ਼ਲ ਕਰੋ। Claude Desktop ਇਸ ਸਕ੍ਰੀਨ ਵਿੱਚ ਮਾਡਲ ਨਹੀਂ ਲੱਭਦਾ।
8. **Save Changes** (ਤਬਦੀਲੀਆਂ ਸੰਭਾਲੋ), ਫਿਰ **Apply Changes** (ਤਬਦੀਲੀਆਂ ਲਾਗੂ ਕਰੋ) ਚੁਣੋ। Claude Desktop ਬੰਦ ਕਰਕੇ ਮੁੜ ਖੋਲ੍ਹੋ।

**ਪ੍ਰੋਟੋਕੋਲ ਜਾਂਚ:** [Aperture Claude ਡੈਸਕਟਾਪ ਗਾਈਡ](https://tailscale.com/docs/aperture/how-to/use-claude-desktop) ਕਹਿੰਦੀ ਹੈ ਕਿ Claude Desktop `/v1/messages` ਉੱਤੇ Anthropic Messages ਵਰਤਦਾ ਹੈ। Codex ਰੂਟ `/codex` ਨਾ ਦਾਖ਼ਲ ਕਰੋ ਅਤੇ OpenAI-ਅਨੁਕੂਲ ਕਨੈਕਸ਼ਨ type ਨਾ ਚੁਣੋ।

### Claude Desktop ਨੂੰ MCP ਨਾਲ ਜੋੜੋ

**ਨਿੱਜੀ MCP ਪਹੁੰਚ:** Claude Desktop ਵਾਲੇ ਕੰਪਿਊਟਰ ਉੱਤੇ ਸਥਾਨਕ stdio ਪੁਲ ਚਲਾਓ। Claude Desktop ਦੀ ਸਥਾਨਕ MCP ਸੰਰਚਨਾ ਵਿੱਚ ਇਹ ਜੋੜੋ:

```json
{
  "mcpServers": {
    "aperture": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "http://<APERTURE_HOST>/v1/mcp"]
    }
  }
}
```

**Bridge ਦਾ ਕੰਮ:** ਸਥਾਨਕ process ਕੰਪਿਊਟਰ ਦੇ Tailscale ਕਨੈਕਸ਼ਨ ਰਾਹੀਂ Aperture ਤੱਕ ਜਾਂਦਾ ਹੈ। OS-ਵਿਸ਼ੇਸ਼ ਸੰਰਚਨਾ ਰਸਤਾ ਵਰਤੋ: macOS, `~/Library/Application Support/Claude/claude_desktop_config.json`; Windows, `%APPDATA%\Claude\claude_desktop_config.json`; Linux ਬੀਟਾ ਵਿੱਚ **ਸੈਟਿੰਗਾਂ > Developer > Edit ਸੰਰਚਨਾ** ਖੋਲ੍ਹੋ ਅਤੇ Claude Desktop ਵੱਲੋਂ ਖੋਲ੍ਹਿਆ ਰਸਤਾ ਵਰਤੋ। Linux ਰਸਤਾ package ਉੱਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ। Claude Desktop ਮੁੜ ਸ਼ੁਰੂ ਕਰੋ, ਕਨੈਕਟਰ ਸੂਚੀ ਵੇਖੋ ਅਤੇ ਸੁਰੱਖਿਅਤ ਟੂਲ call ਕਰੋ। [`mcp-remote` project](https://github.com/punkpeye/mcp-remote) ਸਥਾਨਕ ਤੋਂ ਦੂਰਲਾ ਪੁਲ ਦੱਸਦਾ ਹੈ।

**ਦੂਰਲੇ ਕਨੈਕਟਰ:** Anthropic ਦੇ ਸੈਟਿੰਗਾਂ > Connectors ਲਈ Anthropic service ਤੋਂ ਪਹੁੰਚਯੋਗ ਦੂਰਲਾ ਸਰਵਰ ਚਾਹੀਦਾ ਹੈ। ਸਿਰਫ਼ tailnet ਵਿੱਚ ਵਰਤਿਆ hostname ਤੁਹਾਡੇ ਡਿਵਾਈਸਾਂ ਲਈ ਨਿੱਜੀ ਹੈ, ਇਸ ਲਈ ਨਿੱਜੀ ਐਂਡਪੌਇੰਟ ਲਈ ਸਥਾਨਕ bridge ਵਰਤੋ। ਜੇ ਜਨਤਕ MCP ਸੇਵਾ ਖੋਲ੍ਹੋ ਤਾਂ cloud ਕਨੈਕਟਰ ਜੋੜਨ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰਮਾਣੀਕਰਨ ਅਤੇ permissions ਲਗਾਓ। Anthropic ਦੀ [ਦੂਰਲਾ MCP ਕਨੈਕਟਰ guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) ਵੇਖੋ।

## OpenCode CLI ਅਤੇ ਡੈਸਕਟਾਪ

**ਸਾਂਝੀਆਂ ਸੈਟਿੰਗਾਂ:** OpenCode CLI ਅਤੇ ਡੈਸਕਟਾਪ ਇੱਕੋ OpenCode ਸੰਰਚਨਾ ਪੜ੍ਹਦੇ ਹਨ। ਮੌਜੂਦਾ OpenCode V2 ਦਸਤਾਵੇਜ਼ custom ਪ੍ਰਦਾਤਾ ਲਈ `providers` map ਅਤੇ MCP ਸਰਵਰਾਂ ਲਈ `mcp.servers` ਵਰਤਦਾ ਹੈ। ਇਹ ਮਿਸਾਲ `/v1` ਉੱਤੇ OpenAI-ਅਨੁਕੂਲ chat ਐਂਡਪੌਇੰਟ ਵਰਤਦੀ ਹੈ। ਇਸ ਮਾਡਲ ਰੂਟ ਤੋਂ ਪਹਿਲਾਂ Aperture ਪ੍ਰਦਾਤਾ ਵਿੱਚ OpenAI Chat Completions ਦੀ ਸਹਾਇਤਾ ਜਾਂਚੋ।

**Global ਸੰਰਚਨਾ:** macOS ਅਤੇ Linux ਉੱਤੇ `~/.config/opencode/opencode.json` ਸੋਧੋ। Windows ਉੱਤੇ `%USERPROFILE%\.config\opencode\opencode.json` ਵਰਤੋ। OpenAI-ਅਨੁਕੂਲ ਪ੍ਰਦਾਤਾ ਜੋੜ ਕੇ `<MODEL_ID>` ਨੂੰ ਸਹੀ Aperture ਮਾਡਲ ID ਨਾਲ ਬਦਲੋ। Comment ਲਈ OpenCode ਇਸੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `opencode.jsonc` ਵੀ ਲੈਂਦਾ ਹੈ। [ਸੰਰਚਨਾ reference](https://opencode.ai/docs/config/) global ਅਤੇ project setting ਦੀ ਤਰਜੀਹ ਸਮਝਾਉਂਦੀ ਹੈ।

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "aperture/<MODEL_ID>",
  "providers": {
    "aperture": {
      "env": ["APERTURE_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": {
        "baseURL": "http://<APERTURE_HOST>/v1"
      },
      "models": {
        "<MODEL_ID>": { "modelID": "<MODEL_ID>" }
      }
    }
  },
  "mcp": {
    "servers": {
      "aperture": {
        "type": "remote",
        "url": "http://<APERTURE_HOST>/v1/mcp",
        "oauth": false
      }
    }
  }
}
```

**ਕਲਾਇੰਟ ਪ੍ਰਮਾਣੀਕਰਨ:** `oauth: false` OpenCode ਦਾ ਡਿਫਾਲਟ OAuth ਪ੍ਰਵਾਹ ਛੱਡਦਾ ਹੈ। Aperture Tailscale ਰਾਹੀਂ caller ਪਛਾਣਦਾ ਹੈ। OpenCode ਨੂੰ ਪ੍ਰਦਾਤਾ ਪ੍ਰਮਾਣੀਕਰਨ ਐਂਟਰੀ ਵੀ ਲੋੜੀਂਦੀ ਹੈ, ਇਸ ਲਈ ਸਥਾਨਕ ਵਾਤਾਵਰਣ ਵਿੱਚ `APERTURE_API_KEY=-` ਰੱਖੋ। ਡੈਸਕਟਾਪ ਐਪ ਨੂੰ ਵੀ ਵੇਰੀਏਬਲ ਮਿਲਣਾ ਚਾਹੀਦਾ ਹੈ। Shell ਵਾਤਾਵਰਣ ਨਾ ਮਿਲੇ ਤਾਂ ਐਪ ਵਿੱਚ `/connect` ਚਲਾ ਕੇ Aperture ਲਈ `-` ਦਾਖ਼ਲ ਕਰੋ। ਅੱਪਸਟ੍ਰੀਮ ਪ੍ਰਦਾਤਾ ਕੁੰਜੀ ਇਸ file ਵਿੱਚ ਨਾ ਰੱਖੋ। OpenCode ਦੀ [ਪ੍ਰਦਾਤਾ guide](https://opencode.ai/docs/providers/) ਅਤੇ [MCP ਗਾਈਡ](https://opencode.ai/docs/mcp-servers/) ਮੌਜੂਦਾ ਫਾਰਮੈਟ ਦੱਸਦੀਆਂ ਹਨ। ਸਰਵਰ ਜਾਂਚਣ ਲਈ `opencode mcp list` ਚਲਾਓ ਅਤੇ app ਵਿੱਚ `/mcps` ਨਾਲ ਹਾਲਤ ਵੇਖੋ।

## Hermes CLI ਅਤੇ ਡੈਸਕਟਾਪ

**ਸਾਂਝੀਆਂ ਸੈਟਿੰਗਾਂ:** Hermes Agent macOS ਅਤੇ Linux ਉੱਤੇ ਨਾਮਿਤ ਪ੍ਰਦਾਤਾ ਅਤੇ MCP ਸਰਵਰ `~/.hermes/config.yaml` ਵਿੱਚ ਰੱਖਦਾ ਹੈ। Windows ਦੀ native install `%LOCALAPPDATA%\hermes\config.yaml` ਵਰਤਦੀ ਹੈ। ਸਰਗਰਮ file ਪਤਾ ਕਰਨ ਲਈ `hermes config path` ਚਲਾਓ। `HERMES_HOME` ਡਿਫਾਲਟ ਥਾਂ ਬਦਲ ਸਕਦਾ ਹੈ। ਸਥਾਨਕ Hermes Desktop CLI ਵਾਲਾ Hermes ਹੋਮ ਅਤੇ ਪ੍ਰੋਫ਼ਾਈਲ ਵਰਤਦਾ ਹੈ। Desktop ਦੂਰਲੇ Hermes ਗੇਟਵੇ ਨਾਲ ਜੁੜਦਾ ਹੋਵੇ ਤਾਂ Hermes ਵਾਲੀ ਮਸ਼ੀਨ ਉੱਤੇ Aperture configure ਕਰੋ ਅਤੇ ਸਰਵਰ ਦਾ tailnet ਤੱਕ ਪਹੁੰਚਣਾ ਜਾਂਚੋ। [Hermes ਡੈਸਕਟਾਪ ਗਾਈਡ](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) ਵੇਖੋ।

**Responses ਪ੍ਰਦਾਤਾ:** ਨਾਮਿਤ ਪ੍ਰਦਾਤਾ ਜੋੜੋ। `api` ਮੁੱਲ ਤੁਹਾਡੇ Aperture ਇੰਸਟੈਂਸ ਦੇ Responses ਐਂਡਪੌਇੰਟ ਨਾਲ ਮੇਲ ਖਾਣਾ ਚਾਹੀਦਾ ਹੈ:

```yaml
providers:
  aperture:
    api: "http://<APERTURE_HOST>/v1"
    transport: codex_responses
    default_model: "<MODEL_ID>"
    # Aperture ਨੂੰ client key ਦੀ ਲੋੜ ਹੋਵੇ ਤਾਂ ਹੀ key_env ਜੋੜੋ।
    # key_env: APERTURE_API_KEY

model:
  provider: "custom:aperture"
  default: "<MODEL_ID>"
```

**ਪ੍ਰੋਟੋਕੋਲ ਦੀ ਚੋਣ:** OpenAI Chat Completions ਲਈ `transport: chat_completions` ਸੈੱਟ ਕਰੋ। Anthropic Messages ਲਈ `transport: anthropic_messages` ਚੁਣ ਕੇ Anthropic Messages ਗੇਟਵੇ URL ਵਰਤੋ। ਮੌਜੂਦਾ [ਪ੍ਰਦਾਤਾ guide](https://hermes-agent.nousresearch.com/docs/integrations/providers) Hermes ਨਾਮਿਤ ਪ੍ਰਦਾਤਾ ਦੇ `api`, `transport` ਅਤੇ `default_model` field ਦੱਸਦੀ ਹੈ।

**MCP ਸੰਰਚਨਾ:** ਉਸੇ YAML ਫ਼ਾਈਲ ਵਿੱਚ Aperture MCP ਜੋੜੋ:

```yaml
mcp_servers:
  aperture:
    url: "http://<APERTURE_HOST>/v1/mcp"
    enabled: true
```

**Hermes ਜਾਂਚੋ:** `hermes mcp` ਚਲਾਓ ਅਤੇ ਇੰਟਰਐਕਟਿਵ ਸਰਵਰ ਚੋਣ-ਸੂਚੀ ਵਿੱਚ ਹਰ ਕਨੈਕਸ਼ਨ ਵੇਖੋ। ਸਥਾਨਕ Desktop ਉਹੀ ਸੰਰਚਨਾ ਪ੍ਰੋਫ਼ਾਈਲ ਵਰਤਦਾ ਹੈ। Hermes ਦੀ [ਦੂਰਲੀ HTTP MCP ਸਰਵਰ ਗਾਈਡ](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) ਅਤੇ [MCP ਸੰਰਚਨਾ reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference) ਵੇਖੋ।

## ਦੋਵੇਂ ਰਸਤੇ ਜਾਂਚੋ

**ਮਾਡਲ ਇਨਫਰੈਂਸ ਅਤੇ MCP ਦੀਆਂ ਵੱਖਰੀਆਂ ਜਾਂਚਾਂ ਕਰੋ:**

1. Tailscale ਕਨੈਕਸ਼ਨ ਅਤੇ ਗੇਟਵੇ ਤੱਕ ਪਹੁੰਚ ਪੱਕੀ ਕਰੋ। Claude Desktop ਲਈ ਭਰੋਸੇਯੋਗ TLS ਸਰਟੀਫਿਕੇਟ ਵੀ ਜਾਂਚੋ।
2. ਹਰ configured ਕਲਾਇੰਟ ਤੋਂ ਛੋਟਾ ਪ੍ਰੌਂਪਟ ਭੇਜੋ। Aperture session ਸੂਚੀ ਵਿੱਚ ਮੇਲ ਖਾਂਦੀ ਬੇਨਤੀ ਵੇਖੋ।
3. ਪੱਕਾ ਕਰੋ ਕਿ ਚੁਣਿਆ ਮਾਡਲ ID ਤੁਹਾਡੀ Tailscale ਪਛਾਣ ਨੂੰ ਮਿਲੇ ਮਾਡਲ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।
4. ਹਰ ਕਲਾਇੰਟ ਦੀ MCP ਹਾਲਤ ਸਕ੍ਰੀਨ ਜਾਂ ਸੂਚੀ ਕਮਾਂਡ ਖੋਲ੍ਹੋ। ਜਾਂਚੋ ਕਿ Aperture ਸਰਵਰ ਜੁੜਿਆ ਹੈ ਅਤੇ ਲੋੜੀਂਦੇ ਟੂਲ ਦਿੰਦਾ ਹੈ।
5. ਇੱਕ ਸਿਰਫ਼-ਪੜ੍ਹਨ ਟੂਲ ਚਲਾਓ। ਵਾਪਸ ਆਏ content ਨੂੰ ਅੱਪਸਟ੍ਰੀਮ source ਨਾਲ ਮਿਲਾਓ।
6. ਮਾਡਲ ਜਾਂ ਟੂਲ ਕਾਲ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ Aperture ਲੌਗ ਵੇਖੋ। ਸੰਭਾਲੀ ਸੰਰਚਨਾ ਸਫਲ ਬੇਨਤੀ ਦਾ ਸਬੂਤ ਨਹੀਂ।

| ਲੱਛਣ | ਜਾਂਚ |
|---|---|
| ਮਾਡਲ ਬੇਨਤੀ 404 ਜਾਂ 405 ਦਿੰਦੀ ਹੈ | ਜਾਂਚੋ ਕਿ ਕਲਾਇੰਟ ਐਂਡਪੌਇੰਟ ਸਹੀ ਰੂਟ ਅਤੇ ਪ੍ਰੋਟੋਕੋਲ ਵਰਤਦਾ ਹੈ। Anthropic Messages ਜਾਂ MCP ਲਈ `/codex` ਨਾ ਵਰਤੋ। |
| ਮਾਡਲ ਉਪਲਬਧ ਨਹੀਂ | ਨਿਸ਼ਾਨੇ ਵਾਲੇ Tailscale ਯੂਜ਼ਰ ਵਜੋਂ `/v1/models` ਪੁੱਛੋ। ਸਹੀ ID ਅਤੇ API ਫਾਰਮੈਟ ਦੀ ਮਿਲਾਣ ਜਾਂਚੋ। ਗੁੰਮ ਪ੍ਰਦਾਤਾ ਜਾਂ ਗ੍ਰਾਂਟ ਲਈ ਪ੍ਰਸ਼ਾਸਕ ਨੂੰ ਕਹੋ। |
| ਬੇਨਤੀ ਅਣਅਧਿਕਾਰਤ ਹੈ | ਜਾਂਚੋ ਕਿ ਕਲਾਇੰਟ ਨੂੰ ਅਸਥਾਈ ਮੁੱਲ, ਬੇਅਰਰ ਟੋਕਨ ਜਾਂ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਸਿੱਧਾ ਅੱਗੇ ਭੇਜਣਾ ਚਾਹੀਦਾ ਹੈ। ਅੱਪਸਟ੍ਰੀਮ ਪ੍ਰਦਾਤਾ ਕੁੰਜੀ ਜਨਤਕ ਪ੍ਰੋਜੈਕਟ ਫ਼ਾਈਲ ਵਿੱਚ ਨਾ ਕਾਪੀ ਕਰੋ। |
| MCP ਸਰਵਰ ਸੂਚੀ ਵਿੱਚ ਹੈ ਪਰ ਟੂਲ ਨਹੀਂ ਦਿਖਦੇ | `/v1/mcp`, ਕਨੈਕਟਰ ਸਿਹਤ, ਕਨੈਕਟਰ ਗ੍ਰਾਂਟ ਅਤੇ ਕਲਾਇੰਟ ਤੋਂ Aperture ਤੱਕ ਨੈੱਟਵਰਕ ਰਸਤਾ ਜਾਂਚੋ। |
| Claude Desktop ਨਿੱਜੀ MCP URL ਨਾਲ ਨਹੀਂ ਜੁੜਦਾ | `mcp-remote` ਵਰਗਾ ਸਥਾਨਕ bridge ਚਲਾਓ ਜਾਂ ਢੁੱਕਵੇਂ ਪ੍ਰਮਾਣੀਕਰਨ ਵਾਲਾ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਜਨਤਕ ਕਨੈਕਟਰ ਵਰਤੋ। |

## ਹੋਰ ਡਿਵਾਈਸ ਉੱਤੇ ਸੈੱਟਅੱਪ ਦੁਹਰਾਓ

**ਨਵਾਂ ਡਿਵਾਈਸ:** ਉਹੀ ਕਲਾਇੰਟ install ਕਰੋ ਅਤੇ ਪਹਿਲਾਂ ਡਿਵਾਈਸ ਨੂੰ tailnet ਨਾਲ ਜੋੜੋ। ਨਵੇਂ ਡਿਵਾਈਸ ਤੋਂ `/v1/models` ਪੁੱਛ ਕੇ ਉਸਦੀ Tailscale ਪਛਾਣ ਨੂੰ ਮਿਲੇ ਮਾਡਲ ਲੱਭੋ। ਸੰਰਚਨਾ ਦਾ ਢਾਂਚਾ ਲਓ ਪਰ ਕ੍ਰੈਡੈਂਸ਼ਲ ਸਥਾਨਕ ਰੱਖੋ। `<APERTURE_HOST>`, `<MODEL_ID>` ਅਤੇ `<UPSTREAM_MCP_ENDPOINT>` ਨੂੰ ਮੰਜ਼ਿਲ Aperture ਇੰਸਟੈਂਸ ਦੇ ਮੁੱਲਾਂ ਨਾਲ ਬਦਲੋ। ਹਰ API ਪ੍ਰੋਟੋਕੋਲ ਲਈ ਵੱਖਰਾ ਐਂਡਪੌਇੰਟ ਰੱਖੋ ਅਤੇ ਟੂਲ ਟ੍ਰੈਫਿਕ ਲਈ `/v1/mcp` ਸੈੱਟ ਕਰੋ। ਅੰਤ ਵਿੱਚ ਇੱਕ ਮਾਡਲ ਬੇਨਤੀ ਅਤੇ ਇੱਕ MCP ਟੂਲ call ਜਾਂਚੋ।

**ਕਈ ਗੇਟਵੇ:** ਹਰ Aperture ਇੰਸਟੈਂਸ ਲਈ ਵੱਖਰੀ ਸੰਰਚਨਾ ਵਰਤੋ। ਡਿਵਾਈਸ ਨੂੰ Codex ਅਤੇ Hermes ਲਈ Responses ਐਂਡਪੌਇੰਟ, Claude ਲਈ Anthropic Messages ਐਂਡਪੌਇੰਟ ਅਤੇ ਟੂਲਾਂ ਲਈ MCP ਇਕੱਠਾ ਐਂਡਪੌਇੰਟ ਚਾਹੀਦਾ ਹੈ। API ਕ੍ਰੈਡੈਂਸ਼ਲ ਕਲਾਇੰਟ ਦੇ ਸਥਾਨਕ ਗੁਪਤ store ਜਾਂ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਵਿੱਚ ਸੰਭਾਲੋ। API ਕੁੰਜੀ ਨੂੰ ਸਾਂਝੀ `config.toml`, `opencode.json`, `config.yaml` ਜਾਂ ਜਨਤਕ repository ਵਿੱਚ ਨਾ ਕਾਪੀ ਕਰੋ।

## ਮੁੜ ਵਰਤਣਯੋਗ Aperture ਸੈੱਟਅੱਪ ਪ੍ਰੌਂਪਟ

**ਇਹ ਅਨਾਮ ਪ੍ਰੌਂਪਟ** ਆਪਣੇ ਕੋਡਿੰਗ ਸਹਾਇਕ ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਅਸਥਾਈ ਮੁੱਲ ਨੂੰ ਗੇਟਵੇ ਵੇਰਵਿਆਂ ਨਾਲ ਬਦਲੋ। ਮਾਡਲ ID ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ assistant ਨੂੰ ਤੁਹਾਡੀ Tailscale ਪਛਾਣ ਵਜੋਂ Aperture ਪੁੱਛਣਾ ਚਾਹੀਦਾ ਹੈ।

```text
ਇਸ ਡਿਵਾਈਸ ਉੱਤੇ ਮੇਰਾ ਮੌਜੂਦਾ Tailscale Aperture ਗੇਟਵੇ ਅਤੇ ਇੰਸਟਾਲ AI ਕਲਾਇੰਟ ਸੰਰਚਿਤ ਕਰੋ।

ਦਾਇਰੇ ਵਾਲੇ ਕਲਾਇੰਟ: Codex CLI ਅਤੇ desktop, Claude Code, Claude Desktop, OpenCode CLI ਅਤੇ desktop, Hermes CLI ਅਤੇ desktop।

ਪਹਿਲਾਂ ਪਛਾਣੋ ਕਿ ਡਿਵਾਈਸ macOS, Linux ਜਾਂ Windows ਚਲਾ ਰਿਹਾ ਹੈ, ਸਰਗਰਮ shell (ਜਿਵੇਂ zsh, bash ਜਾਂ PowerShell) ਲੱਭੋ ਅਤੇ ਪੂਰੇ ਕੰਮ ਦੌਰਾਨ ਉਸ platform ਦੇ ਰਸਤਾ ਅਤੇ ਕਮਾਂਡ ਸਿੰਟੈਕਸ ਵਰਤੋ। ਮੌਜੂਦਾ ਗੇਟਵੇ, Tailscale ਕਨੈਕਸ਼ਨ, ਕਲਾਇੰਟ version ਅਤੇ ਮੌਜੂਦਾ ਕਲਾਇੰਟ ਸੈਟਿੰਗਾਂ ਪਹਿਲਾਂ ਜਾਂਚੋ। ਮੌਜੂਦਾ official ਦਸਤਾਵੇਜ਼ ਪੜ੍ਹੋ। ਬੇਸਬੰਧ ਸੰਰਚਨਾ ਕਾਇਮ ਰੱਖੋ ਅਤੇ ਹਰ file edit ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ backup ਲਵੋ। Hostname, ਮਾਡਲ ID, API ਰੂਟ ਜਾਂ ਕ੍ਰੈਡੈਂਸ਼ਲ ਦਾ ਅਨੁਮਾਨ ਨਾ ਲਗਾਓ। ਅੱਪਸਟ੍ਰੀਮ ਪ੍ਰਦਾਤਾ ਕੁੰਜੀ Aperture ਵਿੱਚ ਰੱਖੋ, ਕਲਾਇੰਟ file ਜਾਂ ਇਸ repository ਵਿੱਚ ਨਹੀਂ।

ਇਸ Tailscale ਨਾਲ ਜੁੜੇ ਡਿਵਾਈਸ ਤੋਂ ਉਪਲਬਧ ਮਾਡਲ ਲੱਭੋ:
1. ਮੇਰੇ ਕਲਾਇੰਟ ਦੀ Tailscale ਪਛਾਣ ਵਜੋਂ `http://<APERTURE_HOST>/v1/models` ਪੁੱਛੋ। ਗੇਟਵੇ ਵੱਖਰਾ ਮਾਡਲ-ਸੂਚੀ URL ਦਸਤਾਵੇਜ਼ ਕਰਦਾ ਹੋਵੇ ਤਾਂ ਉਹ ਵਰਤੋ।
2. ਹਰ ਮਾਡਲ ਦਾ `id` ਅਤੇ `metadata.provider.id` ਪੜ੍ਹੋ। ਇਹ ਸੂਚੀ ਮੇਰੀ ਪਛਾਣ ਨੂੰ ਦਿੱਤੇ ਮਾਡਲ ਦਿਖਾਉਂਦੀ ਹੈ। ਪ੍ਰਸ਼ਾਸਕ ਦੀ ਸੂਚੀ ਇਸ ਨਾਲ ਨਾ ਬਦਲੋ ਅਤੇ ID ਨਾ ਬਣਾਓ।
3. ਹਰ ਕਲਾਇੰਟ ਲਈ ਮਾਡਲ ਦੀ API ਅਨੁਕੂਲਤਾ ਮਿਲਾਓ। Codex OpenAI Responses ਵਰਤਦਾ ਹੈ। Claude ਕਲਾਇੰਟ Anthropic Messages ਵਰਤਦੇ ਹਨ। OpenCode ਅਤੇ Hermes ਲਈ ਅਨੁਕੂਲ ਪ੍ਰਦਾਤਾ ਅਤੇ transport configure ਕਰੋ।
4. ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ ਕਲਾਇੰਟ ਦਾ ਮੌਜੂਦਾ ਡਿਫਾਲਟ ਮਾਡਲ ਕਾਇਮ ਰੱਖੋ। ਡਿਫਾਲਟ ਲੋੜੀਂਦਾ ਹੋਵੇ ਤੇ ਮੇਰੀ ਪਸੰਦ ਨਾ ਹੋਵੇ ਤਾਂ ਅਨੁਕੂਲ ਮਾਡਲ ਦਿਖਾ ਕੇ ਮੇਰੀ ਚੋਣ ਪੁੱਛੋ। Claude Desktop ਵਿੱਚ ਸਹੀ ਮਾਡਲ ID ਹੱਥੀਂ ਦਰਜ ਕਰਨੀ ਹੁੰਦੀ ਹੈ।
5. ਐਂਡਪੌਇੰਟ ਢੁੱਕਵਾਂ ਮਾਡਲ ਨਾ ਦੇਵੇ ਤਾਂ ਪ੍ਰਦਾਤਾ ਅਤੇ ਗ੍ਰਾਂਟ setting ਸਿਰਫ਼ ਮੇਰੇ ਕੋਲ ਪ੍ਰਸ਼ਾਸਕ ਪਹੁੰਚ ਹੋਣ 'ਤੇ ਜਾਂਚੋ। ਨਹੀਂ ਤਾਂ ਪ੍ਰਸ਼ਾਸਕ ਨੂੰ ਦੱਸੋ ਕਿ ਕਿਹੜਾ ਮਾਡਲ ਪਹੁੰਚ ਦੇਣਾ ਲੋੜੀਂਦਾ ਹੈ। ਆਪਣੇ ਆਪ ਨੂੰ ਪਹੁੰਚ ਨਾ ਦਿਓ।

Aperture ਤੈਨਾਤੀ ਅਤੇ ਸੰਰਚਨਾ ਦਾ ਸਰੋਤ ਲੱਭੋ। File ਰਸਤਾ ਦਾ ਅਨੁਮਾਨ ਨਾ ਲਗਾਓ ਅਤੇ ਪੂਰੀ ਸੰਰਚਨਾ ਨਾ ਬਦਲੋ। OpenAI Responses ਲਈ `openai_responses`, Anthropic ਕਲਾਇੰਟਾਂ ਲਈ `anthropic_messages` ਚਾਹੀਦਾ ਹੈ। MCP ਕਨੈਕਟਰ ਮੌਜੂਦਾ `connectors.servers` ਸੰਰਚਨਾ ਵਿੱਚ ਹਨ ਅਤੇ ਕਲਾਇੰਟ `/v1/mcp` ਰਾਹੀਂ ਜੁੜਦੇ ਹਨ।

ਸਾਂਝਾ ਗੇਟਵੇ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਪ੍ਰਦਾਤਾ, ਕਨੈਕਟਰ ਅਤੇ ਗ੍ਰਾਂਟ ਦਾ ਸਭ ਤੋਂ ਛੋਟਾ diff ਤਿਆਰ ਕਰੋ। ਇਸਨੂੰ ਸਿਰਫ਼ ਉਦੋਂ ਲਾਗੂ ਕਰੋ ਜਦੋਂ ਮੈਂ ਪ੍ਰਸ਼ਾਸਕ ਹੋਵਾਂ ਅਤੇ ਇਹ ਬੇਨਤੀ ਗੇਟਵੇ ਬਦਲਣ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੀ ਹੋਵੇ। ਨਹੀਂ ਤਾਂ instance ਮਾਲਕ ਨੂੰ ਸਹੀ ਤਜਵੀਜ਼ ਦਿਓ। ਮਾਲਕ ਦੀ ਸਪਸ਼ਟ ਇਜਾਜ਼ਤ ਤੋਂ ਬਿਨਾਂ ਗ੍ਰਾਂਟ ਨਾ ਬਣਾਓ ਅਤੇ ਨਾ ਵਧਾਓ। ਗੇਟਵੇ ਦੀਆਂ ਮੌਜੂਦਾ ਸਾਰੀਆਂ ਸੈਟਿੰਗਾਂ ਕਾਇਮ ਰੱਖੋ।

ਹਰ ਇੰਸਟਾਲ ਕਲਾਇੰਟ ਨੂੰ ਮੌਜੂਦਾ official ਫਾਰਮੈਟ ਅਤੇ OS-ਵਿਸ਼ੇਸ਼ ਟਿਕਾਣੇ ਉੱਤੇ configure ਕਰੋ:
- Codex CLI ਅਤੇ desktop macOS/Linux ਉੱਤੇ `~/.codex/config.toml` ਅਤੇ Windows ਉੱਤੇ `%USERPROFILE%\.codex\config.toml` ਸਾਂਝੇ ਕਰਦੇ ਹਨ। Aperture ਪ੍ਰਦਾਤਾ, ਅਨੁਕੂਲ ਮਾਡਲ, `wire_api = "responses"` ਅਤੇ `mcp_servers` ਵਿੱਚ MCP ਸੈੱਟ ਕਰੋ।
- Claude Code `ANTHROPIC_BASE_URL` ਅਤੇ HTTP ਦੂਰਲਾ MCP ਵਰਤਦਾ ਹੈ। macOS/Linux ਉੱਤੇ `~/.claude/settings.json`, Windows ਉੱਤੇ `%USERPROFILE%\.claude\settings.json` ਵਰਤੋ।
- Claude Desktop ਵਿੱਚ Developer Mode, Configure Third-Party Inference (ਤੀਜੀ-ਧਿਰ ਇਨਫਰੈਂਸ ਸੰਰਚਿਤ ਕਰੋ), ਗੇਟਵੇ, Static API ਕੁੰਜੀ, ਭਰੋਸੇਯੋਗ ਸਰਟੀਫਿਕੇਟ ਵਾਲਾ HTTPS URL ਅਤੇ ਮੇਰੇ user ਲਈ ਲੱਭੀ ਮਾਡਲ ID ਵਰਤੋ। ਨਿੱਜੀ tailnet ਉੱਤੇ MCP ਲਈ ਸਥਾਨਕ `mcp-remote` bridge ਵਰਤੋ। MCP ਸੰਰਚਨਾ ਲਈ ਸੈਟਿੰਗਾਂ > Developer > Edit ਸੰਰਚਨਾ ਵੇਖੋ; ਨਾ ਹੋਵੇ ਤਾਂ ਪਛਾਣੇ OS ਦਾ ਦਸਤਾਵੇਜ਼ੀ ਰਸਤਾ ਵਰਤੋ।
- OpenCode ਮੌਜੂਦਾ V2 `providers` schema ਅਤੇ `mcp.servers` ਵਰਤਦਾ ਹੈ। Global ਸੰਰਚਨਾ macOS/Linux ਉੱਤੇ `~/.config/opencode/opencode.json`, Windows ਉੱਤੇ `%USERPROFILE%\.config\opencode\opencode.json` ਹੈ। Aperture MCP ਲਈ `oauth: false` ਰੱਖੋ। ਲੋੜ ਪਏ ਤਾਂ ਸਥਾਨਕ ਅਸਥਾਈ ਮੁੱਲ API ਕੁੰਜੀ ਵਰਤੋ।
- Hermes ਨਾਮਿਤ ਪ੍ਰਦਾਤਾ, ਮਾਡਲ API ਨਾਲ ਮੇਲ ਖਾਂਦਾ transport ਅਤੇ `mcp_servers` ਵਰਤਦਾ ਹੈ। macOS/Linux ਉੱਤੇ `~/.hermes/config.yaml` ਵਰਤੋ। Windows ਉੱਤੇ `hermes config path` ਜਾਂਚੋ, ਆਮ ਤੌਰ 'ਤੇ `%LOCALAPPDATA%\hermes\config.yaml`। ਵੇਖੋ ਕਿ Hermes Desktop ਸਥਾਨਕ Hermes ਪ੍ਰੋਫ਼ਾਈਲ ਸਾਂਝਾ ਕਰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।

ਕਲਾਇੰਟ ਸਮਰਥਨ ਕਰੇ ਤਾਂ tailnet ਟ੍ਰੈਫਿਕ ਲਈ HTTP ਵਰਤੋ। Claude Desktop ਇਨਫਰੈਂਸ ਨੂੰ ਭਰੋਸੇਯੋਗ ਸਰਟੀਫਿਕੇਟ ਵਾਲਾ HTTPS ਚਾਹੀਦਾ ਹੈ। ਗੇਟਵੇ ਹੋਰ ਰੂਟ ਨਾ ਦੱਸੇ ਤਾਂ `/v1` ਵਰਤੋ।

ਸੰਰਚਿਤ ਕਲਾਇੰਟ ਮੁੜ ਚਾਲੂ ਕਰੋ। Aperture ਵਿੱਚ ਹਰ ਕਲਾਇੰਟ ਲਈ ਇੱਕ ਮਾਡਲ ਬੇਨਤੀ ਅਤੇ ਇੱਕ ਸੁਰੱਖਿਅਤ ਸਿਰਫ਼-ਪੜ੍ਹਨ MCP ਟੂਲ call ਜਾਂਚੋ। ਮੇਰੀ ਪਛਾਣ ਲਈ ਮਿਲੇ ਮਾਡਲ, ਬਦਲੇ ਕਲਾਇੰਟ ਅਤੇ ਫ਼ਾਈਲਾਂ, ਜਾਂਚ ਨਤੀਜੇ ਅਤੇ ਬਾਕੀ ਪ੍ਰਸ਼ਾਸਕੀ ਕੰਮ ਦੱਸੋ। Software install ਨਾ ਕਰੋ, ਗੇਟਵੇ ਜਨਤਕ ਨਾ ਕਰੋ, commit ਜਾਂ publish ਨਾ ਕਰੋ।
```

## ਨਤੀਜਾ

Aperture ਸੈੱਟਅੱਪ ਲਈ ਤਿੰਨ ਚੀਜ਼ਾਂ ਲੋੜੀਂਦੀਆਂ ਹਨ: ਪਹੁੰਚਯੋਗ ਗੇਟਵੇ, ਕਲਾਇੰਟ ਪ੍ਰੋਟੋਕੋਲ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਮਾਡਲ ਰੂਟ ਅਤੇ ਲੋੜੀਂਦੇ ਮਾਡਲਾਂ ਤੇ MCP ਕਨੈਕਟਰਾਂ ਲਈ ਗ੍ਰਾਂਟ। ਇਹ ਸੰਰਚਨਾ pattern macOS, Linux ਅਤੇ Windows ਉੱਤੇ ਕੰਮ ਕਰਦੇ ਹਨ, ਪਰ ਹਰ ਕਲਾਇੰਟ ਆਪਣੇ OS-ਖਾਸ ਟਿਕਾਣੇ ਵਿੱਚ ਸੈਟਿੰਗਾਂ ਰੱਖਦਾ ਹੈ।

ਮਾਡਲ ID ਉਸ Tailscale ਪਛਾਣ ਵਜੋਂ ਲੱਭੋ ਜੋ ਉਹਨਾਂ ਨੂੰ ਵਰਤੇਗੀ। ਮਾਡਲ ਇਨਫਰੈਂਸ ਅਤੇ `/v1/mcp` ਵੱਖਰੇ configure ਕਰੋ, ਫਿਰ ਅਸਲ ਬੇਨਤੀ ਅਤੇ ਸਿਰਫ਼-ਪੜ੍ਹਨ ਟੂਲ ਕਾਲ ਜਾਂਚੋ। ਹੋਰ ਡਿਵਾਈਸ ਜਾਂ Aperture ਇੰਸਟੈਂਸ ਉੱਤੇ ਜਾਂਦੇ ਸਮੇਂ ਇਸ ਗਾਈਡ ਦਾ ਢਾਂਚਾ ਵਰਤੋ, ਉਸ instance ਦੇ ਰੂਟ ਅਤੇ ਗ੍ਰਾਂਟ ਪੱਕੇ ਕਰੋ ਅਤੇ credentials ਸਥਾਨਕ ਗੁਪਤ store ਵਿੱਚ ਰੱਖੋ।

## ਅਗਲੇ ਕਦਮ

**MCP ਅਭਿਆਸ:** ਸੇਵ ਕੀਤੇ ਸਰਵਰ ਅਤੇ ਜਾਂਚੀ ਟੂਲ ਕਾਲ ਦਾ ਫ਼ਰਕ ਜਾਣਨ ਲਈ [MCP ਸਰਵਰ ਸੈੱਟਅੱਪ: Permissions, ਟੂਲ Tests, ਅਤੇ ਸੁਰੱਖਿਅਤ Removal](/articles/effective-ai-mcp-server-setup/) ਪੜ੍ਹੋ। ਵੱਡੇ ਸਵੈ-ਹੋਸਟ ਕੀਤੀ ਬਣਤਰ ਲਈ [ਹਾਈਬ੍ਰਿਡ AI ਏਜੰਟ ਬੇੜਾ: Tailscale, LiteLLM ਅਤੇ Hermes](/articles/hybrid-agentic-ai-fleet-tailscale-litellm-hermes/) ਵੇਖੋ।
