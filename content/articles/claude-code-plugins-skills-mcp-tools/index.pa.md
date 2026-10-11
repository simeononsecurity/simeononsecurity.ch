---
title: "Claude Code ਲਈ 10 ਪਲੱਗਇਨ, ਸਕਿਲਾਂ ਅਤੇ MCP ਟੂਲ: ਇੱਕ ਵਿਹਾਰਕ ਗਾਈਡ"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "ਪਲਾਨਿੰਗ, ਕੋਡ ਰਿਵਿਊ, ਗਿਆਨ ਪ੍ਰਬੰਧਨ, ਡਿਜ਼ਾਈਨ ਅਤੇ ਆਟੋਮੇਸ਼ਨ ਲਈ Claude Code ਐਕਸਟੈਂਸ਼ਨ ਚੁਣੋ। ਦਸ ਟੂਲਾਂ, ਨਿਰਭਰਤਾਵਾਂ ਅਤੇ ਵਿਹਾਰਕ ਜਾਂਚਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਡਿਵੈਲਪਰ ਟੂਲ", "ਸਾਫਟਵੇਅਰ ਵਿਕਾਸ"]
tags: ["Claude Code ਪਲੱਗਇਨ", "Claude Code ਸਕਿਲਾਂ", "MCP ਟੂਲ", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "Codex ਪਲੱਗਇਨ", "ਕੋਡ ਰਿਵਿਊ", "claude-obsidian", "Obsidian", "CLAUDE.md", "Karpathy ਗਾਈਡਲਾਈਨ", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "AI ਵਿਕਾਸ ਵਰਕਫਲੋ", "ਏਜੰਟ ਹਦਾਇਤਾਂ", "ਗਿਆਨ ਗ੍ਰਾਫ"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "ਨੀਲੇ ਅਤੇ ਜਾਮਨੀ ਟੂਲ ਆਇਕਨ, ਫੋਲਡਰ ਅਤੇ ਅਭਾਸੀ ਚਾਰਟ ਪੈਨਲ, ਜੋ ਗੂੜ੍ਹੇ ਪਿਛੋਕੜ ਉੱਤੇ ਕੇਂਦਰੀ ਜਿਆਮਿਤੀ ਹੱਬ ਨਾਲ ਜੁੜੇ ਹਨ"
coverCaption: "ਵਰਕਫਲੋ ਦੀ ਧਾਰਣਾਤਮਕ ਤਸਵੀਰ। ਚਾਰਟ ਆਕਾਰ ਮਾਪੇ ਹੋਏ ਨਤੀਜੇ ਨਹੀਂ ਦਿਖਾਉਂਦੇ।"
---

**ਆਪਣੇ ਵਰਕਫਲੋ ਦੀ ਕਿਸੇ ਖਾਸ ਸਮੱਸਿਆ ਲਈ Claude Code ਐਕਸਟੈਂਸ਼ਨ ਚੁਣੋ।** ਅਸਪਸ਼ਟ ਲੋੜਾਂ ਲਈ ਪਲਾਨਿੰਗ ਗੱਲਬਾਤ ਚਾਹੀਦੀ ਹੈ। ਛੁੱਟੇ ਹੋਏ ਦੋਸ਼ਾਂ ਲਈ ਰਿਵਿਊ ਅਤੇ ਟੈਸਟ ਚਾਹੀਦੇ ਹਨ। ਵਾਰ-ਵਾਰ ਕੀਤੀ ਖੋਜ ਲਈ ਪਤਾ ਲੱਗਣ ਵਾਲੇ ਸਰੋਤ ਚਾਹੀਦੇ ਹਨ। ਹੋਰ ਟੂਲ ਇੰਸਟਾਲ ਕਰਨ ਦਾ ਲਾਭ ਤਦੋਂ ਹੀ ਹੈ ਜਦੋਂ ਉਨ੍ਹਾਂ ਦੀਆਂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਸਪਸ਼ਟ ਹੋਣ।

ਇਹ ਗਾਈਡ ਇਨ੍ਹਾਂ ਕੰਮਾਂ ਲਈ **ਦਸ ਪ੍ਰੋਜੈਕਟਾਂ** ਦੀ ਤੁਲਨਾ ਕਰਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਸੈਟਅਪ ਉਦਾਹਰਨਾਂ ਅਤੇ ਪੂਰੀ ਮੁਲਾਂਕਣ ਕਸਰਤ ਹੈ। ਵਿਸ਼ਲੇਸ਼ਣ ਮੌਜੂਦਾ ਪ੍ਰੋਜੈਕਟ ਦਸਤਾਵੇਜ਼ਾਂ ਅਤੇ ਦਿੱਤੀ Chase AI ਵੀਡੀਓ ਉੱਤੇ ਆਧਾਰਿਤ ਹੈ। ਸਿਫਾਰਸ਼ਾਂ ਸੰਪਾਦਕੀ ਫੈਸਲੇ ਹਨ। ਇਹ ਹੱਥੋਂ ਕੀਤੇ ਪ੍ਰਦਰਸ਼ਨ ਮਾਪ ਜਾਂ ਉਤਪਾਦਕਤਾ ਵਿੱਚ ਦਸ ਗੁਣਾ ਵਾਧੇ ਦਾ ਸਬੂਤ ਨਹੀਂ ਹਨ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਨਤੀਜੇ ਅਨੁਸਾਰ ਚੁਣੋ:** ਰਿਵਿਊ ਕੀਤਾ ਪਲਾਨ, ਕੋਡ ਮੈਪ ਅਤੇ ਬਣਾਈ ਤਸਵੀਰ ਲਈ ਵੱਖਰੇ ਟੂਲ ਚਾਹੀਦੇ ਹਨ।
- **ਇੰਸਟਾਲੇਸ਼ਨ ਦੀਆਂ ਪਰਤਾਂ ਵੱਖ ਰੱਖੋ:** ਹਦਾਇਤਾਂ, ਚੱਲਣ ਵਾਲੇ ਪ੍ਰੋਗਰਾਮ, ਪਲੱਗਇਨ ਅਤੇ ਸਰਵਿਸ ਕਨੈਕਸ਼ਨਾਂ ਦੀਆਂ ਨਿਰਭਰਤਾਵਾਂ ਵੱਖ ਹੁੰਦੀਆਂ ਹਨ।
- **ਮੌਜੂਦਾ ਨਾਮ ਜਾਂਚੋ:** Graphify ਅਤੇ grill-me-codex ਦੇ ਹੁਣ ਵੱਖਰੇ ਕੈਨੋਨਿਕਲ ਰਿਪੋਜ਼ਟਰੀ ਪਤੇ ਹਨ।
- **ਸਹਿਮਤੀ ਤੋਂ ਅੱਗੇ ਜਾਂਚੋ:** ਦੋ ਮਾਡਲਾਂ ਵੱਲੋਂ ਪਲਾਨ ਸਵੀਕਾਰ ਕਰਨ ਨਾਲ ਸਹੀ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਸਾਬਤ ਨਹੀਂ ਹੁੰਦੀ।
- **ਸਵੀਕਾਰਿਆ ਕੰਮ ਮਾਪੋ:** ਸੈਟਅਪ, ਸਰਵਿਸ ਵਰਤੋਂ, ਅਸਫਲ ਕੋਸ਼ਿਸ਼ਾਂ ਅਤੇ ਮਨੁੱਖੀ ਸੁਧਾਰ ਸ਼ਾਮਲ ਕਰੋ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਲੋੜਾਂ:** ਚੱਲਦੀ Claude Code ਇੰਸਟਾਲੇਸ਼ਨ, ਟੈਸਟ ਲਈ ਵੱਖਰਾ ਪ੍ਰੋਜੈਕਟ ਜਾਂ ਬ੍ਰਾਂਚ ਅਤੇ ਚੁਣੀਆਂ ਬਾਹਰੀ ਸਰਵਿਸਾਂ ਵਰਤਣ ਦੀ ਇਜਾਜ਼ਤ। CLI ਉਦਾਹਰਨਾਂ ਟਰਮੀਨਲ ਅਤੇ ਦੱਸੇ ਪੈਕੇਜ ਮੈਨੇਜਰ ਨੂੰ ਮੰਨਦੀਆਂ ਹਨ। ਕਲਾਉਡ ਇੰਟੀਗ੍ਰੇਸ਼ਨਾਂ ਲਈ ਆਪਣੇ ਖਾਤੇ ਅਤੇ ਪ੍ਰਮਾਣਿਕਤਾ ਚਾਹੀਦੀ ਹੈ।

**ਅੰਦਾਜ਼ਾ ਸਮਾਂ:** ਪੜ੍ਹਨ ਲਈ 15 ਮਿੰਟ, ਫਿਰ ਇੱਕ ਸੀਮਿਤ ਟ੍ਰਾਇਲ ਲਈ 30 ਤੋਂ 60 ਮਿੰਟ। **ਮੁਸ਼ਕਲ:** CLI ਸੈਟਅਪ ਅਤੇ ਸਰਵਿਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ ਦਰਮਿਆਨੀ। ਹਦਾਇਤੀ ਸਕਿਲਾਂ ਪੜ੍ਹਨ ਲਈ ਘੱਟ ਸੈਟਅਪ ਚਾਹੀਦਾ ਹੈ।

**ਦਸਤਾਵੇਜ਼ 10 ਅਕਤੂਬਰ 2026 ਨੂੰ ਜਾਂਚੇ ਗਏ।** ਕਮਾਂਡਾਂ ਅਤੇ ਪਹੁੰਚ ਨਿਯਮ ਦਿੱਤੇ ਸਰੋਤਾਂ ਨਾਲ ਮਿਲਦੇ ਹਨ। ਪੁਰਾਣਾ ਟਿਊਟੋਰਿਅਲ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੀ ਇੰਸਟਾਲ ਕੀਤੀ ਵਰਜਨ ਜਾਂਚੋ। ਇਹ ਲੇਖ Claude Code ਤੋਂ ਵਰਤੀਆਂ ਐਕਸਟੈਂਸ਼ਨਾਂ ਉੱਤੇ ਧਿਆਨ ਦਿੰਦਾ ਹੈ ਅਤੇ ਜਿੱਥੇ ਲੋੜ ਹੈ ਉੱਥੇ ਹੋਸਟ ਦੇ ਫਰਕ ਦੱਸਦਾ ਹੈ।

**ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਬਾਅਦ ਪਰਤਾਂ ਵਿੱਚ ਜਾਂਚ ਕਰੋ।** ਫਾਈਲਾਂ, ਹੋਸਟ ਡਿਸਕਵਰੀ, ਐਗਜ਼ਿਕਿਊਟੇਬਲ ਨਿਰਭਰਤਾਵਾਂ, ਕਰੈਡੈਂਸ਼ਲ ਅਤੇ ਇੱਕ ਪ੍ਰਤੀਨਿਧੀ ਕੰਮ ਵੱਖ-ਵੱਖ ਜਾਂਚੋ। ਸਫਲ ਇੰਸਟਾਲਰ ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਕਿ ਬ੍ਰਾਊਜ਼ਰ, MCP ਸਰਵਰ, ਮੀਡੀਆ ਟੂਲ ਜਾਂ ਬਾਹਰੀ ਖਾਤਾ ਚੱਲਦਾ ਹੈ। ਪਹਿਲਾ ਟੈਸਟ ਸਿੰਥੈਟਿਕ ਡਾਟਾ ਉੱਤੇ ਕਰੋ ਅਤੇ ਸਰੋਤ ਰਿਵਿਜ਼ਨ ਲਿਖੋ।

## ਐਕਸਟੈਂਸ਼ਨ ਦੀ ਕਿਸਮ ਜਾਣੋ

| ਕਿਸਮ | ਭੂਮਿਕਾ | ਉਦਾਹਰਨ |
|---|---|---|
| **ਹਦਾਇਤ ਫਾਈਲ** | ਪ੍ਰੋਜੈਕਟ ਦੀਆਂ ਸਥਾਈ ਉਮੀਦਾਂ ਤੈਅ ਕਰਦੀ ਹੈ | CLAUDE.md |
| **Skill** | ਚੁਣੇ ਕੰਮ ਲਈ ਤਰੀਕਾ ਦਿੰਦੀ ਹੈ | grill-me |
| **Plugin** | ਰਜਿਸਟਰ ਕੀਤੀਆਂ ਕਮਾਂਡਾਂ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪੈਕੇਜ ਕਰਦਾ ਹੈ | Codex plugin |
| **CLI** | ਟਰਮੀਨਲ ਤੋਂ ਕਮਾਂਡਾਂ ਚਲਾਉਂਦਾ ਹੈ | Graphify |
| **MCP ਸਰਵਰ** | ਏਜੰਟ ਕਲਾਇੰਟ ਨੂੰ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਣ ਵਾਲੇ ਟੂਲ ਦਿੰਦਾ ਹੈ | n8n instance integration |

**Model Context Protocol (MCP)** ਏਜੰਟ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਸਰਵਰ ਵੱਲੋਂ ਦਿੱਤੇ ਟੂਲਾਂ ਅਤੇ ਡਾਟੇ ਨਾਲ ਜੋੜਦਾ ਹੈ। ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ, ਜਾਂ **CLI**, ਚੱਲਣ ਵਾਲੀਆਂ ਕਮਾਂਡਾਂ ਚਲਾਉਂਦਾ ਹੈ। ਸਕਿਲ ਅਕਸਰ ਏਜੰਟ ਨੂੰ ਇਨ੍ਹਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇੰਟਰਫੇਸ ਦੀ ਵਰਤੋਂ ਸਿਖਾਉਂਦੀ ਹੈ। ਸਕਿਲ ਦੀ ਮੌਜੂਦਗੀ ਕੰਮ ਕਰਦੇ ਕਨੈਕਸ਼ਨ ਦਾ ਸਬੂਤ ਨਹੀਂ ਹੈ।

**ਗੁੰਮ ਸਮਰੱਥਾ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** ਜੇ ਏਜੰਟ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਰਿਪੋਜ਼ਟਰੀ ਖੋਜ ਹੈ, ਤਾਂ ਨਵੀਂ ਖੋਜ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਦਿਖਣ ਵਾਲਾ ਲਾਭ ਦੇਣਾ ਪਵੇਗਾ। ਜੇ ਏਜੰਟ ਕੋਲ ਆਟੋਮੇਸ਼ਨ ਪਲੇਟਫਾਰਮ ਦੀ ਪਹੁੰਚ ਨਹੀਂ ਹੈ, ਤਾਂ ਸਿਰਫ਼ ਹਦਾਇਤ ਫਾਈਲ ਪ੍ਰਮਾਣਿਤ ਪਹੁੰਚ ਨਹੀਂ ਦੇਵੇਗੀ। ਵੱਡਾ [ਏਜੰਟ ਰਨਟਾਈਮ ਗਾਈਡ](/articles/best-ai-agent-harnesses/) ਮਾਡਲ ਕਾਲਾਂ ਅਤੇ ਟੂਲ ਚਲਾਉਣ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਦੇ ਸਾਫਟਵੇਅਰ ਨੂੰ ਸਮਝਾਉਂਦਾ ਹੈ।

## ਪਹਿਲਾ ਟੂਲ ਚੁਣੋ

| ਸਮੱਸਿਆ | ਟੂਲ | ਪਹਿਲੀ ਸਵੀਕ੍ਰਿਤੀ ਜਾਂਚ |
|---|---|---|
| **ਅਸਪਸ਼ਟ ਲੋੜਾਂ** | grill-me / grill-with-docs | ਸਪਸ਼ਟ ਫੈਸਲੇ ਅਤੇ ਸਵੀਕ੍ਰਿਤੀ ਮਾਪਦੰਡ |
| **ਵਾਰ-ਵਾਰ ਸਕੋਪ ਦਾ ਭਟਕਣਾ** | Karpathy ਤੋਂ ਪ੍ਰੇਰਿਤ CLAUDE.md | ਹਰ ਸੋਧ ਮੰਗੀ ਤਬਦੀਲੀ ਲਈ ਹੋਵੇ |
| **ਖਤਰਨਾਕ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਪਲਾਨ** | Claudex Loop | ਰਿਵਿਊ ਨਤੀਜੇ ਸਬੂਤ ਨਾਲ ਹੱਲ |
| **ਬਿਨਾਂ ਰਿਵਿਊ ਕੋਡ ਤਬਦੀਲੀਆਂ** | OpenAI Codex plugin | ਨਤੀਜੇ ਕੋਡ ਅਤੇ ਅਸਫਲਤਾ ਕੇਸ ਨਾਲ ਜੁੜੇ |
| **ਅਣਜਾਣ ਰਿਪੋਜ਼ਟਰੀ** | Graphify | ਰਿਸ਼ਤੇ ਸਰੋਤ ਫਾਈਲਾਂ ਨਾਲ ਮਿਲਣ |
| **ਖਿਲਰਿਆ ਪ੍ਰੋਜੈਕਟ ਗਿਆਨ** | claude-obsidian | ਦਾਅਵਿਆਂ ਨਾਲ ਮੂਲ ਸਬੂਤ ਦੀਆਂ ਲਿੰਕਾਂ ਰਹਿਣ |
| **ਵਾਰ-ਵਾਰ ਸਰੋਤ ਸੰਖੇਪ** | notebooklm-py | ਜਵਾਬ ਮਕਸਦ ਵਾਲੇ ਸਰੋਤ ਦੱਸਣ |
| **ਉਲਝਣ ਵਾਲਾ ਇੰਟਰਫੇਸ** | Impeccable | ਵਰਤੋਂਕਾਰ ਮਕਸਦ ਵਾਲੀ ਇੰਟਰੈਕਸ਼ਨ ਪੂਰੀ ਕਰਨ |
| **ਗੁੰਮ ਵਿਜ਼ੁਅਲ ਸਰੋਤ** | Higgsfield | ਨਤੀਜਾ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਐਸੈਟ ਬ੍ਰੀਫ ਨਾਲ ਮਿਲੇ |
| **ਦੁਹਰਾਉਣ ਯੋਗ ਸਰਵਿਸ ਵਰਕਫਲੋ** | n8n MCP | ਟੈਸਟ ਚਲਾਉਣ ਨਾਲ ਉਮੀਦਿਆ ਨਤੀਜਾ ਮਿਲੇ |

**ਸਿਫਾਰਸ਼ੀ ਸ਼ੁਰੂਆਤ:** ਇੱਕ ਕਤਾਰ ਚੁਣੋ ਅਤੇ ਇੰਸਟਾਲੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਬੇਸਲਾਈਨ ਕੰਮ ਸੰਭਾਲੋ। ਦੂਜਾ ਟੂਲ ਤਦੋਂ ਹੀ ਜੋੜੋ ਜਦੋਂ ਉਹ ਵੱਖਰਾ ਅਤੇ ਮਾਪਿਆ ਜਾ ਸਕਣ ਵਾਲਾ ਯੋਗਦਾਨ ਦੇਵੇ।

## ਕੰਮ ਸਪਸ਼ਟ ਕਰੋ

### grill-me ਅਤੇ grill-with-docs

**Matt Pocock ਦੀਆਂ ਸਕਿਲਾਂ** ਅਧੂਰੇ ਵਿਚਾਰ ਨੂੰ ਫੈਸਲਿਆਂ ਵਿੱਚ ਬਦਲਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ। ਮੌਜੂਦਾ [grill-me ਐਂਟਰੀ](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) ਸਾਂਝੀ grilling skill ਚਲਾਉਂਦੀ ਹੈ। [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) grilling ਅਤੇ ਡੋਮੇਨ ਮਾਡਲਿੰਗ ਚਲਾਉਂਦੀ ਹੈ। [ਕਲੈਕਸ਼ਨ ਦਸਤਾਵੇਜ਼](https://github.com/mattpocock/skills) ਇੰਟਰਵਿਊ ਨਾਲ ਸਾਂਝੀ ਸ਼ਬਦਾਵਲੀ ਅਤੇ ਆਰਕੀਟੈਕਚਰ ਫੈਸਲਾ ਰਿਕਾਰਡ ਸਮਝਾਉਂਦਾ ਹੈ।

**ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਵਾਲਾ ਰੂਪ ਵਰਤੋ** ਜਦੋਂ ਕਾਰੋਬਾਰੀ ਸ਼ਬਦ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਉੱਤੇ ਅਸਰ ਪਾਉਣ। ਉਦਾਹਰਨ CSV ਇੰਪੋਰਟਰ ਲਈ ਤੈਅ ਕਰੋ ਕਿ ਮੌਜੂਦਾ ਗਾਹਕ ਦਾ ਮਤਲਬ ਉਹੀ ਈਮੇਲ, ਉਹੀ ਬਾਹਰੀ ਪਛਾਣਕਰਤਾ ਜਾਂ ਦੋਵੇਂ ਹਨ। ਡੁਪਲੀਕੇਟ ਖੋਜ ਲਿਖਣ ਤੋਂ ਪਹਿਲਾਂ ਪਰਿਭਾਸ਼ਾ ਲਿਖੋ।

**ਇੰਟਰਵਿਊ ਨੂੰ ਹੱਦ ਵਿੱਚ ਰੱਖੋ।** ਚੰਗਾ ਸੈਸ਼ਨ ਮਹੱਤਵਪੂਰਨ ਅਸਪਸ਼ਟਤਾ ਦੂਰ ਕਰਦਾ ਹੈ। ਇੰਟਰਵਿਊ ਨੂੰ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਪਹਿਲਾਂ ਮੌਜੂਦ ਜਵਾਬ ਦੁਬਾਰਾ ਨਹੀਂ ਮੰਗਣੇ ਚਾਹੀਦੇ। ਅੰਤ ਵਿੱਚ ਪਲਾਨ, ਬਾਕੀ ਸਵਾਲ ਅਤੇ ਦਿਖਣ ਵਾਲੀਆਂ ਪੂਰਨਤਾ ਜਾਂਚਾਂ ਹੋਣ।

### Karpathy ਤੋਂ ਪ੍ਰੇਰਿਤ CLAUDE.md

**Multica ਵੱਲੋਂ ਸੰਭਾਲੀਆਂ ਗਾਈਡਲਾਈਨਾਂ** Karpathy ਦੇ ਅਧਿਐਨਾਂ ਨੂੰ ਚਾਰ ਵਿਸ਼ਿਆਂ ਵਿੱਚ ਬਦਲਦੀਆਂ ਹਨ: ਸਪਸ਼ਟ ਧਾਰਨਾਵਾਂ, ਸਧਾਰਨ ਹੱਲ, ਕੇਂਦਰਿਤ ਤਬਦੀਲੀਆਂ ਅਤੇ ਜਾਂਚੇ ਜਾ ਸਕਣ ਵਾਲੇ ਟੀਚੇ। [ਰਿਪੋਜ਼ਟਰੀ](https://github.com/multica-ai/andrej-karpathy-skills) ਉਸ ਦੀਆਂ ਗੱਲਾਂ ਤੋਂ ਪ੍ਰੇਰਿਤ ਕਮਿਊਨਿਟੀ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਹੈ। ਇਸਨੂੰ Karpathy ਵੱਲੋਂ ਨਿੱਜੀ ਤੌਰ ਉੱਤੇ ਸੰਭਾਲਿਆ ਪਲੱਗਇਨ ਕਹਿਣਾ ਗਲਤ ਹੋਵੇਗਾ।

**ਲਾਭਦਾਇਕ ਹਦਾਇਤਾਂ ਨੂੰ ਮੌਜੂਦਾ ਪ੍ਰੋਜੈਕਟ ਨੀਤੀ ਵਿੱਚ ਮਿਲਾਓ।** ਬਿਲਡ ਕਮਾਂਡਾਂ, ਸਮੱਗਰੀ ਨਿਯਮ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਪਾਬੰਦੀਆਂ ਬਚਾਓ। ਇਨ੍ਹਾਂ ਵੇਰਵਿਆਂ ਨੂੰ ਹਟਾਉਣ ਵਾਲੀ ਬਦਲਵੀਂ ਹਦਾਇਤ ਫਾਈਲ ਨਵੀਆਂ ਗਲਤੀਆਂ ਪੈਦਾ ਕਰਦੀ ਹੈ।

**ਉਦਾਹਰਨ ਪ੍ਰੋਜੈਕਟ ਨਿਯਮ:** ਇੰਪੋਰਟਰ ਤਬਦੀਲੀ ਨੂੰ ਮੌਜੂਦਾ ਡੁਪਲੀਕੇਟ ਪ੍ਰਬੰਧਨ ਬਚਾਉਣਾ ਅਤੇ fixture ਨਾਲ ਹਰ ਜਾਣ-ਬੁੱਝ ਕੇ ਕੀਤੀ ਤਬਦੀਲੀ ਸਮਝਾਉਣਾ ਲਾਜ਼ਮੀ ਕਰੋ। ਹਦਾਇਤਾਂ ਉਮੀਦਾਂ ਦੱਸਦੀਆਂ ਹਨ। ਟੈਸਟ ਅਤੇ ਰਨਟਾਈਮ ਕੰਟਰੋਲ ਵੱਖਰੇ ਸਬੂਤ ਦਿੰਦੇ ਹਨ।

| ਪਲਾਨਿੰਗ ਆਰਟੀਫੈਕਟ | ਮਕਸਦ |
|---|---|
| **ਲੋੜ** | ਵਰਤੋਂਕਾਰ ਨੂੰ ਦਿਖਣ ਵਾਲਾ ਨਤੀਜਾ ਦੱਸਦੀ ਹੈ |
| **ਸ਼ਬਦਾਵਲੀ ਐਂਟਰੀ** | ਉਲਝੇ ਸ਼ਬਦ ਨੂੰ ਇੱਕ ਮਤਲਬ ਦਿੰਦੀ ਹੈ |
| **ਫੈਸਲਾ ਰਿਕਾਰਡ** | ਮਹੱਤਵਪੂਰਨ ਚੋਣ ਦਾ ਕਾਰਨ ਸੰਭਾਲਦਾ ਹੈ |
| **ਸਵੀਕ੍ਰਿਤੀ ਜਾਂਚ** | ਪੂਰਨਤਾ ਨੂੰ ਮਾਪਣ ਦਾ ਢੰਗ ਦਿੰਦੀ ਹੈ |

## ਪਲਾਨ ਅਤੇ ਕੋਡ ਰਿਵਿਊ ਕਰੋ

### grill-me-codex, ਹੁਣ Claudex Loop

**Claudex Loop** ਅਸਲ grill-me-codex ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਮੌਜੂਦਾ ਟਿਕਾਣਾ ਹੈ। ਇਸਦੀ [ਡੌਕੂਮੈਂਟੇਸ਼ਨ](https://github.com/chaseai-yt/claudex-loop) ਰਿਪੋਜ਼ਟਰੀ ਜਾਂਚ, ਲੋੜਾਂ, ਦੂਜੇ ਪ੍ਰੋਵਾਈਡਰ ਵੱਲੋਂ ਰਿਵਿਊ, ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਅਤੇ ਸੁਤੰਤਰ ਜਾਂਚ ਦੱਸਦੀ ਹੈ। ਪੂਰੇ ਲੂਪ ਲਈ ਦੋਵੇਂ CLI ਅਤੇ Python 3.10 ਜਾਂ ਨਵਾਂ ਚਾਹੀਦਾ ਹੈ।

**ਮਹੱਤਵਪੂਰਨ ਪਲਾਨਾਂ ਲਈ Claudex Loop ਵਰਤੋ** ਜਿਨ੍ਹਾਂ ਦੀਆਂ ਧਾਰਨਾਵਾਂ ਨੂੰ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਤੋਂ ਪਹਿਲਾਂ ਚੁਣੌਤੀ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ। ਮੌਜੂਦਾ ਵਰਕਫਲੋ Claude Code ਜਾਂ Codex ਤੋਂ ਸ਼ੁਰੂ ਹੋ ਸਕਦਾ ਹੈ। ਇਹ ਨਤੀਜੇ ਅਤੇ ਫੈਸਲੇ ਲਿਖਦਾ ਹੈ ਅਤੇ ਰਿਵਿਊ ਦੀ ਇਜਾਜ਼ਤ ਨੂੰ ਬਿਲਡ ਦੀ ਇਜਾਜ਼ਤ ਤੋਂ ਵੱਖ ਕਰਦਾ ਹੈ। ਵੀਡੀਓ ਦਾ ਪੁਰਾਣਾ ਪੰਜ ਰਾਊਂਡ ਵਰਣਨ ਮੌਜੂਦਾ ਰਾਊਂਡ ਬਜਟ ਦਾ ਬਦਲ ਨਹੀਂ ਹੈ।

**ਹਰ ਇਤਰਾਜ਼ ਲਈ ਸਬੂਤ ਮੰਗੋ।** CSV ਇੰਪੋਰਟਰ ਲਈ ਰਿਵਿਊ ਨੂੰ ਡੁਪਲੀਕੇਟ ਜਾਂ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਦਾ ਠੋਸ ਕੇਸ ਅਤੇ ਉਮੀਦਿਆ ਵਿਹਾਰ ਦੱਸਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਾਡਲਾਂ ਦੀ ਸਹਿਮਤੀ ਰਿਵਿਊ ਦਾ ਨਤੀਜਾ ਹੈ, ਸਬੂਤ ਨਹੀਂ। ਬਜਟ ਮੁੱਕਣ ਉੱਤੇ ਬਾਕੀ ਨਤੀਜੇ ਸੰਭਾਲੋ।

### OpenAI Codex ਪਲੱਗਇਨ

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**Claude Code ਲਈ OpenAI ਦਾ Codex ਪਲੱਗਇਨ** Claude Code ਵਿੱਚ ਕੋਡ ਰਿਵਿਊ ਅਤੇ ਕੰਮ ਸੌਂਪਣਾ ਜੋੜਦਾ ਹੈ। ਇਹ Claude Code ਕਮਾਂਡਾਂ ਹਨ, ਸ਼ੈੱਲ ਕਮਾਂਡਾਂ ਨਹੀਂ। [ਅਧਿਕਾਰਤ ਰਿਪੋਜ਼ਟਰੀ](https://github.com/openai/codex-plugin-cc) Node.js 18.18 ਜਾਂ ਨਵਾਂ ਅਤੇ ChatGPT ਜਾਂ OpenAI API ਕੁੰਜੀ ਰਾਹੀਂ ਪ੍ਰਮਾਣਿਤ Codex ਪਹੁੰਚ ਦੱਸਦੀ ਹੈ।

```text
/codex:review --background
/codex:status
/codex:result
```

**ਮੌਜੂਦਾ ਤਬਦੀਲੀਆਂ ਜਾਂ ਬ੍ਰਾਂਚ ਤੁਲਨਾ ਲਈ ਆਮ ਰਿਵਿਊ ਵਰਤੋ।** ਕੇਂਦਰਿਤ ਚੁਣੌਤੀ ਲਈ **`/codex:adversarial-review`** ਵਰਤੋ। **`/codex:rescue`** ਵਰਗੀਆਂ ਡੈਲੀਗੇਸ਼ਨ ਕਮਾਂਡਾਂ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੇ ਰਿਵਿਊ ਤੋਂ ਵੱਖਰਾ ਕੰਮ ਕਰਦੀਆਂ ਹਨ। ਮਕਸਦ ਅਤੇ ਅਧਿਕਾਰ ਸਪਸ਼ਟ ਕਰੋ।

**Codex ਵਰਤੋਂ ਲਈ ਵੱਖਰਾ ਬਜਟ ਰੱਖੋ।** ਪ੍ਰੋਜੈਕਟ ChatGPT Free ਨੂੰ ਸਮਰਥਿਤ ਖਾਤਿਆਂ ਵਿੱਚ ਰੱਖਦਾ ਹੈ, ਪਰ ਵਰਤੋਂ ਸੀਮਾਵਾਂ ਲਾਗੂ ਰਹਿੰਦੀਆਂ ਹਨ। ਪਲੱਗਇਨ ਇੰਸਟਾਲ ਕਰਨ ਨਾਲ ਅਸੀਮਿਤ ਪਹੁੰਚ ਨਹੀਂ ਮਿਲਦੀ।

**ਚੋਣ ਨਿਯਮ:** ਮੌਜੂਦਾ ਪੈਚ ਲਈ ਸੀਮਿਤ ਪਲੱਗਇਨ ਰਿਵਿਊ ਵਰਤੋ। ਜਦੋਂ ਲੋੜਾਂ ਅਤੇ ਪਲਾਨ ਸੋਧ ਲਈ ਆਪਣੀ ਦਰਜ ਪ੍ਰਕਿਰਿਆ ਚਾਹੀਦੀ ਹੋਵੇ ਤਾਂ ਵੱਡਾ ਲੂਪ ਚੁਣੋ।

## ਲਾਭਦਾਇਕ ਸੰਦਰਭ ਬਚਾਓ

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਰਿਸ਼ਤਿਆਂ ਨੂੰ ਪੁੱਛਗਿੱਛ ਯੋਗ ਗਿਆਨ ਗ੍ਰਾਫ ਵਿੱਚ ਮੈਪ ਕਰਦਾ ਹੈ। ਇਸਦੀ [ਕੈਨੋਨਿਕਲ ਰਿਪੋਜ਼ਟਰੀ](https://github.com/Graphify-Labs/graphify) ਹੁਣ Graphify-Labs ਵਿੱਚ ਹੈ। ਪੈਕੇਜ ਨਾਮ **`graphifyy`** ਹੈ, ਜਿਸ ਵਿੱਚ ਅੰਤ ਉੱਤੇ ਦੋ y ਹਨ। ਐਗਜ਼ਿਕਿਊਟੇਬਲ **`graphify`** ਹੀ ਰਹਿੰਦਾ ਹੈ।

**ਸਿਰਫ਼ ਕੋਡ ਐਕਸਟਰੈਕਸ਼ਨ** ਸਥਾਨਕ abstract syntax tree ਪਾਰਸਿੰਗ ਵਰਤਦੀ ਹੈ। ਦਸਤਾਵੇਜ਼ ਅਤੇ ਮੀਡੀਆ ਦੀ ਵਿਆਖਿਆ ਵੱਖਰੇ ਮਾਡਲ-ਆਧਾਰਿਤ ਰਸਤੇ ਨਾਲ ਹੁੰਦੀ ਹੈ। code-only ਮੋਡ ਦੀ ਪਰਾਈਵੇਸੀ ਜਾਂ ਖਰਚ ਦੀ ਗੱਲ ਹਰ ਮੋਡ ਉੱਤੇ ਲਾਗੂ ਨਾ ਕਰੋ।

**ਵਿਕਲਪਿਕ hooks** commit ਅਤੇ ਬ੍ਰਾਂਚ ਬਦਲਣ ਤੋਂ ਬਾਅਦ ਕੋਡ ਗ੍ਰਾਫ ਮੁੜ ਬਣਾਉਂਦੇ ਹਨ। pull ਜਾਂ merge ਤੋਂ ਬਾਅਦ ਦਸਤਾਵੇਜ਼ੀ ਵਰਕਫਲੋ **`graphify update .`** ਮੰਗਦਾ ਹੈ। ਦਸਤਾਵੇਜ਼ ਤਬਦੀਲੀਆਂ ਲਈ ਵੱਖਰੀ ਤਾਜ਼ਗੀ ਚਾਹੀਦੀ ਹੈ। Obsidian export ਗ੍ਰਾਫ ਦਾ ਹੋਰ ਦ੍ਰਿਸ਼ ਦਿੰਦਾ ਹੈ।

**ਰਿਸ਼ਤਿਆਂ ਵਾਲੇ ਸਵਾਲਾਂ ਲਈ Graphify ਵਰਤੋ,** ਫਿਰ ਸੰਬੰਧਿਤ ਸਰੋਤ ਜਾਂਚੋ। ਗ੍ਰਾਫ ਫਾਈਲਾਂ ਚੁਣਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਗ੍ਰਾਫ ਢਾਂਚਾ ਰਨਟਾਈਮ ਵਿਹਾਰ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਅਤੇ ਟੈਸਟਾਂ ਦੀ ਥਾਂ ਨਹੀਂ ਲੈਂਦਾ। ਗ੍ਰਾਫ ਬਣਾਉਣ ਅਤੇ ਸੰਭਾਲਣ ਸਮੇਤ ਆਪਣੇ ਸਵਾਲਾਂ ਉੱਤੇ ਟੋਕਨ ਬਚਤ ਮਾਪੋ।

### claude-obsidian

**claude-obsidian** ਸਰੋਤ ਸਮੱਗਰੀ ਨੂੰ ਲਿੰਕ ਕੀਤੀਆਂ ਅਤੇ ਸਰੋਤ-ਹਵਾਲੇ ਵਾਲੀਆਂ Obsidian ਪੰਨਿਆਂ ਵਿੱਚ ਰੱਖਦਾ ਹੈ। ਇਸਦੀ [ਰਿਪੋਜ਼ਟਰੀ](https://github.com/AgriciDaniel/claude-obsidian) ingestion, retrieval, ਗਿਆਨ ਸੰਭਾਲ, ਸਰੋਤ ਬਚਾਅ ਅਤੇ ਸਹਿਮਤੀ ਜਾਂ ਵਿਰੋਧ ਦੇ ਰਿਕਾਰਡ ਦੱਸਦੀ ਹੈ। Vault ਆਮ ਸਥਾਨਕ ਫਾਈਲਾਂ ਹੀ ਰਹਿੰਦਾ ਹੈ।

**ਲੰਬੇ ਸਮੇਂ ਦੇ ਪ੍ਰੋਜੈਕਟ ਗਿਆਨ ਲਈ claude-obsidian ਵਰਤੋ:** ਡਿਜ਼ਾਈਨ ਫੈਸਲੇ, ਸਰੋਤ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਖੋਜ ਨੋਟ, ਜੋ ਇੱਕ ਗੱਲਬਾਤ ਤੋਂ ਬਾਅਦ ਵੀ ਰਹਿਣ। ਲਾਭਦਾਇਕ ਨਤੀਜਾ provenance ਵਾਲਾ ਸੰਭਾਲਣ ਯੋਗ ਰਿਕਾਰਡ ਹੈ, ਮਤਲਬ ਹਰ ਮਹੱਤਵਪੂਰਨ ਦਾਅਵੇ ਦਾ ਪਤਾ ਲੱਗਣ ਵਾਲਾ ਸਰੋਤ।

**Ingestion ਤੋਂ ਬਾਅਦ Vault ਰਿਵਿਊ ਕਰੋ।** ਕੁਝ ਦਾਅਵੇ ਚੁਣੋ ਅਤੇ ਹਵਾਲਿਆਂ ਰਾਹੀਂ ਮੂਲ ਸਰੋਤ ਤੱਕ ਜਾਓ। ਟਕਰਾਓਂਦੇ ਸਬੂਤ ਬਚਾਓ। ਸਥਾਨਕ ਸਟੋਰੇਜ ਸਥਾਨਕ inference ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ। ਸੰਵੇਦਨਸ਼ੀਲ ਦਸਤਾਵੇਜ਼ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਹੋਸਟ ਅਤੇ ਮਾਡਲ ਸੰਰਚਨਾ ਜਾਂਚੋ।

| ਸੰਦਰਭ ਸਿਸਟਮ | ਸਭ ਤੋਂ ਵਧੀਆ ਪਹਿਲਾ ਸਵਾਲ |
|---|---|
| **Graphify** | ਕਿਹੜੇ ਸਰੋਤ ਕੰਪੋਨੈਂਟ ਜੁੜੇ ਹਨ? |
| **claude-obsidian** | ਕਿਹੜਾ ਸੰਭਾਲਿਆ ਸਬੂਤ ਇਸ ਫੈਸਲੇ ਨੂੰ ਸਹਾਰਾ ਦਿੰਦਾ ਹੈ? |
| **notebooklm-py** | ਚੁਣੇ ਸਰੋਤ ਕੀ ਕਹਿੰਦੇ ਹਨ? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** Google ਦੀ notebook research service ਲਈ Python ਲਾਇਬ੍ਰੇਰੀ, CLI ਅਤੇ ਏਜੰਟ ਸਕਿਲ ਦਿੰਦਾ ਹੈ। [ਪ੍ਰੋਜੈਕਟ](https://github.com/teng-lin/notebooklm-py) ਸਰੋਤ ਆਯਾਤ, grounded ਸਵਾਲ, ਬਣੇ ਆਰਟੀਫੈਕਟ ਅਤੇ batch ਡਾਊਨਲੋਡ ਦੱਸਦਾ ਹੈ। browser extra ਇੰਟਰਐਕਟਿਵ ਲੌਗਇਨ ਲਈ ਹੈ।

**ਇਹ ਗੈਰ-ਅਧਿਕਾਰਤ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹੈ।** ਲਾਇਬ੍ਰੇਰੀ Google ਦੇ ਗੈਰ-ਦਸਤਾਵੇਜ਼ੀ ਇੰਟਰਫੇਸ ਵਰਤਦੀ ਹੈ ਅਤੇ ਟੁੱਟਣ ਜਾਂ ਰੇਟ ਸੀਮਾਵਾਂ ਦਾ ਸਾਹਮਣਾ ਕਰ ਸਕਦੀ ਹੈ। ਇਸਨੂੰ Google ਵੱਲੋਂ ਸਮਰਥਿਤ ਜਨਤਕ API ਨਾ ਕਹੋ।

**ਸੀਮਿਤ ਖੋਜ ਕੋਰਪਸ ਲਈ notebooklm-py ਵਰਤੋ,** ਜਿਵੇਂ ਇੱਕ dependency ਦੀ ਰਿਲੀਜ਼ ਨੋਟ ਅਤੇ migration guide। ਪਲਾਨ ਵਿੱਚ ਨਤੀਜੇ ਜੋੜਣ ਤੋਂ ਪਹਿਲਾਂ ਹਵਾਲੇ ਸਰੋਤ ਪਾਠ ਨਾਲ ਮਿਲਾਓ। ਸੰਭਾਲੀ authentication state ਨੂੰ ਖਾਤਾ ਪਹੁੰਚ ਸਮੱਗਰੀ ਵਾਂਗ ਸੁਰੱਖਿਅਤ ਰੱਖੋ।

**ਖੋਜ ਬਾਹਰ ਭੇਜਣ ਨਾਲ ਕੰਮ ਚੱਲਣ ਦਾ ਸਥਾਨ ਬਦਲਦਾ ਹੈ।** ਇਹ orchestration ਟੋਕਨ, ਸਰਵਿਸ ਕੋਟਾ, ਰਿਵਿਊ ਮਿਹਨਤ ਜਾਂ ਡਾਟਾ ਸੰਭਾਲ ਜ਼ਿੰਮੇਵਾਰੀ ਖਤਮ ਨਹੀਂ ਕਰਦਾ। ਟੋਕਨ ਬਚਤ ਨੂੰ ਮਾਪੋ, ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਆਟੋਮੈਟਿਕ ਵਿਸ਼ੇਸ਼ਤਾ ਨਾ ਮੰਨੋ।

## ਐਸੈਟ ਡਿਜ਼ਾਈਨ ਅਤੇ ਜਨਰੇਟ ਕਰੋ

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** ਕੇਂਦਰਿਤ ਇੰਟਰਫੇਸ ਕੰਮ ਲਈ ਡਿਜ਼ਾਈਨ ਸ਼ਬਦਾਵਲੀ ਦਿੰਦਾ ਹੈ। [ਡੌਕੂਮੈਂਟੇਸ਼ਨ](https://github.com/pbakaus/impeccable) critique, layout, typography, accessibility, motion ਅਤੇ browser iteration ਦੱਸਦੀ ਹੈ। ਉਦਾਹਰਨਾਂ ਇੰਸਟਾਲ ਸਕਿਲ ਅਤੇ settings ਵਾਲਾ ਪ੍ਰੋਜੈਕਟ ਮੰਨਦੀਆਂ ਹਨ।

**ਇੰਟਰੈਕਸ਼ਨ ਸਮੱਸਿਆ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** ਇੰਪੋਰਟਰ ਲਈ ਪੁੱਛੋ ਕਿ ਵਰਤੋਂਕਾਰ validation ਗਲਤੀਆਂ ਕਿਉਂ ਛੱਡਦੇ ਹਨ ਜਾਂ ਡੁਪਲੀਕੇਟ ਨੀਤੀ ਗਲਤ ਕਿਉਂ ਸਮਝਦੇ ਹਨ। ਵਿਜ਼ੁਅਲ polish ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਰਿਵਿਊ ਕਰੋ। ਚੰਗੀ spacing ਅਸਪਸ਼ਟ action ਠੀਕ ਨਹੀਂ ਕਰਦੀ।

**ਲਾਈਵ iteration** ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਵਿਕਲਪਾਂ ਦੀ ਤੁਲਨਾ ਕਰਨ ਦਿੰਦੀ ਹੈ। keyboard navigation, mobile layout, error messages ਅਤੇ contrast ਜਾਂਚੋ। ਕਮਾਂਡ ਗਿਣਤੀ ਵਰਜਨਾਂ ਨਾਲ ਬਦਲਦੀ ਹੈ, ਇਸ ਲਈ ਇੰਸਟਾਲ ਵਰਜਨ ਦੀ ਸੂਚੀ ਵਰਤੋ।

### Higgsfield

**Higgsfield ਦੀ MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ** ਏਜੰਟਾਂ ਨੂੰ image ਅਤੇ video generation service ਨਾਲ ਜੋੜਦੀ ਹੈ। [ਅਧਿਕਾਰਤ ਪੰਨਾ](https://higgsfield.ai/mcp) Claude Code ਅਤੇ CLI ਕਨੈਕਸ਼ਨ ਵਿਕਲਪ ਦਿੰਦਾ ਹੈ। ਆਪਣੇ ਖਾਤੇ ਅਤੇ ਇੰਟਰਫੇਸ ਲਈ ਮੌਜੂਦਾ ਸੈਟਅਪ ਵਰਤੋ।

**ਜਦੋਂ ਗੁੰਮ ਨਤੀਜਾ ਮੀਡੀਆ ਹੋਵੇ ਤਾਂ Higgsfield ਚੁਣੋ।** ਉਤਪਾਦ ਪੰਨੇ ਲਈ ratio, composition, brand limits ਅਤੇ placement ਪਹਿਲਾਂ ਤੈਅ ਕਰੋ। ਵਿਜ਼ੁਅਲ ਬ੍ਰੀਫ ਨੂੰ ਪੰਨਾ ਬਣਾਉਣ ਦੇ ਕੰਮ ਤੋਂ ਵੱਖ ਰੱਖੋ।

**ਪਹਿਲਾਂ ਸਰਵਿਸ ਪਹੁੰਚ ਅਤੇ ਖਪਤ ਜਾਂਚੋ।** ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਸੂਚੀ ਹਰ ਮਾਡਲ, ਅਸੀਮਿਤ generation ਜਾਂ ਖਾਸ commercial right ਦੀ ਪਹੁੰਚ ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ। ਉਤਪਾਦਨ ਵਰਕਫਲੋ ਤੋਂ ਪਹਿਲਾਂ ਖਾਤਾ ਸ਼ਰਤਾਂ ਅਤੇ ਮਾਡਲ ਜਾਂਚੋ।

**ਅੰਤਿਮ ਫਾਈਲ ਨੂੰ** ਉਸਦੇ display size ਵਿੱਚ ਰਿਵਿਊ ਕਰੋ। ਦਿਖਣ ਵਾਲਾ ਪਾਠ, ਅਣਚਾਹੇ ਨਿਸ਼ਾਨ, crop ਅਤੇ ਉਤਪਾਦ ਨਾਲ ਮਿਲਾਪ ਜਾਂਚੋ। ਬਣੇ terminal screen ਅਤੇ diagram ਸਫਲ ਟੈਸਟ ਦਾ ਸਬੂਤ ਨਹੀਂ ਹਨ।

| ਡਿਜ਼ਾਈਨ ਡਿਲਿਵਰੇਬਲ | ਪੂਰਨਤਾ ਦਾ ਸਬੂਤ |
|---|---|
| **ਇੰਟਰਫੇਸ ਸੋਧ** | ਲੋੜੀਂਦੇ ਕੰਮ ਟੀਚੇ ਵਾਲੇ viewports ਵਿੱਚ ਚੱਲਣ |
| **ਚਿੱਤਰ ਐਸੈਟ** | dimensions, crop ਅਤੇ content ਬ੍ਰੀਫ ਨਾਲ ਮਿਲਣ |
| **ਵੀਡੀਓ ਐਸੈਟ** | timing, motion ਅਤੇ final export ਬ੍ਰੀਫ ਨਾਲ ਮਿਲਣ |

## ਦੁਹਰਾਉਣ ਯੋਗ ਵਰਕਫਲੋ ਜੋੜੋ

### n8n MCP

**n8n ਦਾ built-in MCP server** ਜੁੜੇ clients ਨੂੰ ਵਰਕਫਲੋ operations ਦਿੰਦਾ ਹੈ। [ਮੌਜੂਦਾ connection documentation](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) Cloud ਅਤੇ self-hosted instances ਨੂੰ ਕਵਰ ਕਰਦੀ ਹੈ। ਵਰਕਫਲੋ ਬਣਾਉਣ ਅਤੇ ਸੋਧਣ ਦੀ ਡੌਕੂਮੈਂਟੇਸ਼ਨ n8n 2.13.0 ਤੋਂ ਹੈ। ਇਹ n8n ਦੇ ਆਪਣੇ server ਬਾਰੇ ਹੈ, ਸਮਾਨ ਨਾਮ ਵਾਲੇ community package ਬਾਰੇ ਨਹੀਂ।

**ਇਸ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ instance-level access ਵਰਤੋ।** MCP Server Trigger node ਦਾ scope ਵੱਖਰਾ ਹੈ ਅਤੇ ਇੱਕ workflow ਦੇ tools ਦਿੰਦਾ ਹੈ। [Tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) ਨੂੰ ਆਪਣੀ deployed version ਨਾਲ ਮਿਲਾਓ।

**ਪਹੁੰਚ ਸੋਚ-ਸਮਝ ਕੇ ਚਾਲੂ ਕਰੋ।** Existing workflows ਨੂੰ full access ਲਈ MCP exposure ਚਾਹੀਦਾ ਹੈ। Search previews ਵਰਤੋਂਕਾਰ ਦੀਆਂ ਮੌਜੂਦਾ permissions ਵਿੱਚ ਵੱਧ visibility ਰੱਖਦੇ ਹਨ। Workflow exposure ਵੱਖਰੀ client allowlist ਨਹੀਂ ਹੈ, ਹਾਲਾਂਕਿ client permissions operations ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦੀਆਂ ਹਨ।

**Execution mode ਜਾਂਚੋ।** Documented default **`execute_workflow`** published production version ਚਲਾਉਂਦਾ ਹੈ। Manual mode current unpublished version ਚਲਾਉਂਦਾ ਹੈ। ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ inputs ਅਤੇ downstream actions ਜਾਂਚੋ।

**ਪਹਿਲਾ ਵਧੀਆ ਟੈਸਟ:** synthetic support requests ਨੂੰ classify ਕਰੋ ਅਤੇ ਨਤੀਜੇ test destination ਵਿੱਚ ਲਿਖੋ। missing fields ਅਤੇ retries ਜਾਂਚੋ। Self-hosting ਲਈ compute, maintenance ਅਤੇ paid downstream services ਦੀ ਲੋੜ ਰਹਿੰਦੀ ਹੈ।

## ਨਿਯੰਤਰਿਤ ਟ੍ਰਾਇਲ ਚਲਾਓ

**ਉਦਾਹਰਨ ਕਸਰਤ:** ਛੋਟੀ application ਵਿੱਚ CSV importer ਜੋੜੋ। ਇਹ rows ਦਾ preview ਦਿੰਦਾ ਹੈ, invalid email fields ਦੱਸਦਾ ਹੈ ਅਤੇ duplicate creation ਰੋਕਦਾ ਹੈ। ਇਸ ਕਸਰਤ ਲਈ customer records ਜਾਂ live external destinations ਨਹੀਂ ਚਾਹੀਦੇ।

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**ਪਹਿਲਾਂ baseline ਬਣਾਓ।** ਸ਼ੁਰੂਆਤੀ revision ਸੰਭਾਲੋ ਅਤੇ ਏਜੰਟ ਨੂੰ ਮੌਜੂਦਾ ਵਰਕਫਲੋ ਨਾਲ ਕੰਮ ਪੂਰਾ ਕਰਨ ਲਈ ਕਹੋ। ਸੁਤੰਤਰ acceptance checks ਚਲਾਓ ਅਤੇ ਨਤੀਜਾ ਰੱਖੋ। ਉਸੇ revision ਤੋਂ ਇੱਕ extension ਅਤੇ ਉਹੀ requirements ਨਾਲ ਦੁਹਰਾਓ।

**Experiment ਨੂੰ ਸ਼ੱਕੀ ਸਮੱਸਿਆ ਨਾਲ ਮਿਲਾਓ।** ਜੇ duplicate handling ਵਾਰ-ਵਾਰ ਗਲਤ ਸਮਝੀ ਜਾਂਦੀ ਹੈ, requirements skill ਟ੍ਰਾਇਲ ਕਰੋ। ਜੇ agent ਮੌਜੂਦਾ validator ਛੱਡਦਾ ਹੈ, repository mapping ਟ੍ਰਾਇਲ ਕਰੋ। ਜੇ users errors ਨਹੀਂ ਵੇਖਦੇ, interface critique ਟ੍ਰਾਇਲ ਕਰੋ। ਸਾਰੇ ਦਸ tools ਇਕੱਠੇ ਲੋਡ ਕਰਨ ਨਾਲ ਸੁਧਾਰ ਦਾ ਕਾਰਨ ਨਹੀਂ ਪਤਾ ਲੱਗਦਾ।

**ਉਮੀਦਿਆ reasoning:** ਦੂਜੀ ਸਫਲ ਕੋਸ਼ਿਸ਼ ਲਾਭਦਾਇਕ ਸਬੂਤ ਹੈ, ਪਰ ਇੱਕ run ਆਮ productivity multiplier ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ। ਵਾਰ-ਵਾਰ runs tool value ਨੂੰ model variation ਤੋਂ ਵੱਖ ਕਰਦੀਆਂ ਹਨ। accepted results, review effort ਅਤੇ failed attempts ਸਮੇਤ, ਤੁਲਨਾ ਕਰੋ।

| ਨਿਰੀਖਣ | ਅਰਥ |
|---|---|
| **ਤੇਜ਼ ਜਵਾਬ, ਅਸਫਲ ਟੈਸਟ** | task completion ਬਿਨਾਂ ਘੱਟ response time |
| **ਲੰਬਾ run, ਘੱਟ corrections** | ਕੁੱਲ delivery effort ਵਿੱਚ ਸੰਭਾਵੀ ਲਾਭ |
| **ਦੋ reviewers ਸਹਿਮਤ** | ਸੁਤੰਤਰ verification ਦੀ ਲੋੜ ਵਾਲੀ ਸਹਿਮਤੀ |
| **ਘੱਟ agent usage, ਨਵੇਂ service charges** | ਖਰਚ providers ਵਿਚਕਾਰ ਤਬਦੀਲ |

**ਫੈਸਲਾ ਰਿਕਾਰਡ ਸੰਭਾਲੋ।** ਸਮੱਸਿਆ, ਚੁਣਿਆ tool, ਵੇਖਿਆ ਲਾਭ, ਬਾਕੀ issue ਅਤੇ ਅਗਲੇ trial ਦੀਆਂ ਸ਼ਰਤਾਂ ਲਿਖੋ। ਜਦੋਂ ਯੋਗਦਾਨ ਇਹ ਜਾਂਚ ਪਾਰ ਕਰੇ ਤਾਂ tool ਰੱਖੋ। ਵੱਡੀ installed collection ਲਈ ਵੱਡਾ active workflow ਲਾਜ਼ਮੀ ਨਹੀਂ।

## ਸਮੱਸਿਆ ਹੱਲ

| ਲੱਛਣ | ਅਗਲੀ ਜਾਂਚ |
|---|---|
| **Skill ਮੌਜੂਦ ਪਰ command fail** | executable install, PATH ਅਤੇ sidecar files |
| **ਪੁਰਾਣੇ tutorial ਵਿੱਚ command names ਨਹੀਂ** | installed version ਅਤੇ canonical instructions |
| **Graph ਵਿੱਚ ਨਵੀਆਂ ਤਬਦੀਲੀਆਂ ਨਹੀਂ** | graph freshness ਅਤੇ document refresh |
| **Reviewer ਹੱਲ ਹੋਏ ਇਤਰਾਜ਼ ਦੁਹਰਾਉਂਦਾ ਹੈ** | exact plan revision, evidence ਅਤੇ review budget |
| **Notebook authentication fail** | auth diagnostic, session validity ਅਤੇ upstream issues |
| **n8n connection ਵਿੱਚ operations ਨਹੀਂ** | deployed version, exposure settings ਅਤੇ permissions |
| **Design ਵਧੀਆ ਪਰ ਕੰਮ ਮਾੜਾ** | original acceptance criteria ਅਤੇ interaction checks |

**Installation layers ਇਸ ਕ੍ਰਮ ਵਿੱਚ ਜਾਂਚੋ:** files present, host discovery, dependencies ready, authentication working ਅਤੇ representative task verified। ਸਫਲ installer ਸਿਰਫ਼ chain ਦਾ ਇੱਕ ਹਿੱਸਾ ਸਾਬਤ ਕਰਦਾ ਹੈ।

**ਹੋਰ copy ਜੋੜਣ ਤੋਂ ਪਹਿਲਾਂ overlapping skills ਜਾਂਚੋ।** Requirements interviews, planning suites, design tools ਅਤੇ review packages ਕਈ ਵਾਰ ਵੱਖਰੇ defaults ਰੱਖਦੇ ਹਨ। ਕੰਮ ਲਈ ਇੱਕ primary procedure ਚੁਣੋ ਅਤੇ named contributions ਵਾਲੇ supporting tools ਜੋੜੋ। repository policy ਅਤੇ ਮੰਗਿਆ scope ਬਚਾਓ।

## ਵੀਡੀਓ walkthrough

{{< youtube id="IShdbDP4Jgg" enable="true" title="ਅਗਲੇ ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਤੇਜ਼ ਕਰਨ ਲਈ 10 ਵਧੀਆ Claude Code ਪਲੱਗਇਨ, ਜੂਨ 2026" >}}

**Chase AI walkthrough** ਇੱਥੇ ਚਰਚਿਤ ਦਸ ਪ੍ਰੋਜੈਕਟ ਪੇਸ਼ ਕਰਦੀ ਹੈ। demonstrations ਲਈ [ਮੂਲ ਵੀਡੀਓ](https://www.youtube.com/watch?v=IShdbDP4Jgg) ਵੇਖੋ। ਮੌਜੂਦਾ installation ਅਤੇ behavior ਲਈ linked project documentation ਵਰਤੋ। ਵੀਡੀਓ ਦਾ title promotional claim ਹੈ, ਇਸ ਗਾਈਡ ਵੱਲੋਂ ਮਾਪਿਆ ਨਤੀਜਾ ਨਹੀਂ।

## ਅਗਲੇ ਕਦਮ

**ਇੱਕ ਦੁਹਰਾਉਂਦੀ ਸਮੱਸਿਆ ਅਤੇ ਇੱਕ acceptance test ਚੁਣੋ।** disposable project ਉੱਤੇ matching extension ਟ੍ਰਾਇਲ ਕਰੋ, ਫਿਰ ਨਤੀਜਾ ਸੁਧਾਰਨ ਵਾਲਾ ਸਭ ਤੋਂ ਛੋਟਾ combination ਰੱਖੋ। knowledge management, media generation ਜਾਂ automation ਤਦੋਂ ਹੀ ਜੋੜੋ ਜਦੋਂ ਕੰਮ ਨੂੰ ਉਹ outputs ਚਾਹੀਦੇ ਹੋਣ।

**ਸੰਬੰਧਿਤ ਮਾਰਗਦਰਸ਼ਨ ਲਈ**, agent ਚੁਣਦੇ ਸਮੇਂ [CLI coding-agent comparison](/articles/cli-coding-agents-comparison/) ਪੜ੍ਹੋ। requirements, evidence ਅਤੇ review responsibilities ਲਈ [AI collaboration course](/ai-collaboration-course-start/) ਵਰਤੋ।

{{< centerbutton href="/ai-collaboration-course-start/" >}}
AI Collaboration Course ਪੜ੍ਹੋ
{{< /centerbutton >}}

## ਹਵਾਲੇ

- [Graphify: code graphs ਅਤੇ installation](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: skill collection](https://github.com/mattpocock/skills)
- [Claudex Loop: current grill-me-codex project](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: Claude Code ਲਈ Codex plugin](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: source-linked knowledge management](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: Karpathy-inspired coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: design commands ਅਤੇ installation](https://github.com/pbakaus/impeccable)
- [Higgsfield: agent integration](https://higgsfield.ai/mcp)
- [notebooklm-py: unofficial library, CLI ਅਤੇ skill](https://github.com/teng-lin/notebooklm-py)
- [n8n: official MCP connection guide](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
