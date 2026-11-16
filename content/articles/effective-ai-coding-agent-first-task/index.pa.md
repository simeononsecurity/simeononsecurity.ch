---
title: "ਕੋਡਿੰਗ ਏਜੰਟ ਨਾਲ ਆਪਣਾ ਪਹਿਲਾ ਰਿਪੋਜ਼ਟਰੀ ਕੰਮ ਕਰੋ"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "ਕੋਡਿੰਗ ਏਜੰਟ ਦਾ ਇੰਟਰਫੇਸ ਚੁਣੋ, ਨਮੂਨਾ ਰਿਪੋਜ਼ਟਰੀ ਖੋਲ੍ਹੋ, ਸੁਝਾਈ ਤਬਦੀਲੀ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਉਸਨੂੰ ਰੱਖਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚਾਂ ਚਲਾਓ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਸਾਫਟਵੇਅਰ ਇੰਜੀਨੀਅਰਿੰਗ"]
tags: ["Codex CLI ਟਿਊਟੋਰਿਅਲ", "Codex ਐਪ", "Claude Code CLI", "OpenCode ਟਿਊਟੋਰਿਅਲ", "ਕੋਡਿੰਗ ਏਜੰਟ ਵਰਕਫ਼ਲੋ", "AI ਕੋਡਿੰਗ ਟੂਲ"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "ਕੋਡ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਟਰਮੀਨਲ ਅਤੇ ਡੈਸਕਟਾਪ ਏਜੰਟ ਦੇ ਵੱਖਰੇ ਦ੍ਰਿਸ਼, ਨਾਲ ਸਮੀਖਿਆ ਕੀਤਾ ਫ਼ਾਈਲ ਡਿਫ਼"
coverCaption: ""
---

[ਵਿਹਾਰਕ AI ਵਰਕਫ਼ਲੋ ਕੋਰਸ ਵੱਲ ਵਾਪਸ ਜਾਓ](/effective-ai-course-start/)

**ਕੋਡਿੰਗ ਏਜੰਟ ਵਰਕਸਪੇਸ ਵਿੱਚ ਫ਼ਾਈਲਾਂ ਪੜ੍ਹਦਾ, ਤਬਦੀਲੀਆਂ ਸੁਝਾਉਂਦਾ ਅਤੇ ਟੂਲ ਚਲਾਉਂਦਾ ਹੈ।** ਇਸ ਪਾਠ ਵਿੱਚ ਤੁਸੀਂ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਇੱਕ ਛੋਟਾ ਕੰਮ ਕਰੋਗੇ। ChatGPT ਡੈਸਕਟਾਪ ਐਪ ਜਾਂ CLI ਵਿੱਚ Codex, Claude Code CLI ਜਾਂ OpenCode TUI ਚੁਣੋ। ਫਿਰ ਤਬਦੀਲੀ ਸਵੀਕਾਰ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਉਸਦੀ ਸਮੀਖਿਆ ਕਰੋ।

**ਸਿੱਖਣ ਦਾ ਨਤੀਜਾ:** ਤੁਸੀਂ ਸੀਮਿਤ ਤਬਦੀਲੀ ਚਲਾਓਗੇ ਜਾਂ ਖੁਦ ਲਾਗੂ ਕਰੋਗੇ, ਫਿਰ ਉਸਦਾ ਡਿਫ਼ ਅਤੇ ਵਰਤਾਅ ਜਾਂਚੋਗੇ।

## ਮੁੱਖ ਗੱਲਾਂ

- **ChatGPT ਡੈਸਕਟਾਪ ਐਪ ਵਿੱਚ Codex** ਕੰਮ ਅਤੇ ਸਮੀਖਿਆ ਲਈ ਦ੍ਰਿਸ਼ਮਾਨ ਵਰਕਸਪੇਸ ਦਿੰਦਾ ਹੈ।
- **Codex CLI** ਟਰਮੀਨਲ ਤੋਂ Codex ਸੈਸ਼ਨ ਚਲਾਉਂਦਾ ਹੈ।
- **Claude Code CLI** ਟਰਮੀਨਲ ਤੋਂ Claude ਦਾ ਕੋਡਿੰਗ ਵਰਕਫ਼ਲੋ ਚਲਾਉਂਦਾ ਹੈ।
- **OpenCode TUI** ਸੰਰਚਿਤ ਕੀਤੇ ਜਾ ਸਕਣ ਵਾਲੇ ਪ੍ਰਦਾਤਾਵਾਂ ਅਤੇ ਇਜਾਜ਼ਤਾਂ ਨਾਲ ਟਰਮੀਨਲ ਵਰਕਫ਼ਲੋ ਦਿੰਦਾ ਹੈ।
- **ਡਿਫ਼ ਅਤੇ ਟੈਸਟ ਨਤੀਜਾ** ਸਹਾਇਕ ਦੇ ਕੰਮ ਮੁਕੰਮਲ ਹੋਣ ਵਾਲੇ ਸੁਨੇਹੇ ਨਾਲੋਂ ਵਧੇਰੇ ਅਹਿਮ ਹਨ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਪਹਿਲਾਂ ਦੀ ਤਿਆਰੀ:** [ਕੋਰਸ ਸੈੱਟਅੱਪ](/articles/effective-ai-course-setup/) ਪੂਰਾ ਕਰੋ, ਜਿਸ ਵਿੱਚ ਬੇਸਲਾਈਨ ਰਨ ਅਤੇ ਸਥਾਨਕ Git ਸਨੈਪਸ਼ਾਟ ਸ਼ਾਮਲ ਹਨ। ਇਸ ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ [ਰਿਪੋਜ਼ਟਰੀ ਸੰਦਰਭ](/articles/effective-ai-agents-md-context/) ਅਤੇ [ਟਾਸਕ ਪੈਕਟ](/articles/effective-ai-task-packets/) ਪੂਰੇ ਕਰੋ। ਉਹ ਕੋਡਿੰਗ ਏਜੰਟ ਵਰਤੋ ਜਿਸ ਤੱਕ ਪਹੁੰਚਣ ਦੀ ਤੁਹਾਨੂੰ ਇਜਾਜ਼ਤ ਹੈ। 45 ਮਿੰਟ ਰੱਖੋ। ਔਖਾਈ ਸ਼ੁਰੂਆਤੀ ਤੋਂ ਦਰਮਿਆਨੀ ਹੈ।

**[ਕੋਰਸ ਸਟਾਰਟਰ ਲੈਬ](/downloads/effective-ai-course-lab.zip)** ਨੂੰ ਅਸਥਾਈ ਫੋਲਡਰ ਵਿੱਚ ਵਰਤੋ। ਆਰਕਾਈਵ ਵਿੱਚ ਛੋਟਾ ਟਾਸਕ ਰਿਪੋਰਟ ਪ੍ਰੋਗਰਾਮ, ਨਮੂਨਾ ਡਾਟਾ ਅਤੇ ਟੈਸਟ ਹਨ। ਪਹਿਲੀ ਸੋਧ ਲਈ ਉਤਪਾਦਨ ਰਿਪੋਜ਼ਟਰੀ ਨਾ ਵਰਤੋ। ਮੌਜੂਦਾ ਕੁੱਲ ਗਿਣਤੀ ਕਾਇਮ ਰੱਖਦਿਆਂ `--status` ਫ਼ਿਲਟਰ ਜੋੜੋ।

## ਕੋਡਿੰਗ ਏਜੰਟ ਤੋਂ ਬਿਨਾਂ ਅਧਿਐਨ ਰਸਤਾ

**ਜੇ ਕੋਡਿੰਗ ਏਜੰਟ ਉਪਲਬਧ ਨਾ ਹੋਵੇ ਤਾਂ ਚੈਟ ਸਹਾਇਕ ਤੋਂ ਉਹੀ ਤਬਦੀਲੀ ਸੁਝਾਉਣ ਲਈ ਕਹੋ।** ਸਿੰਥੈਟਿਕ ਲੈਬ ਵਿੱਚੋਂ ਸਿਰਫ਼ `docs/requirements.md`, `task_report.py` ਅਤੇ ਸੰਬੰਧਿਤ ਟੈਸਟ ਫ਼ਾਈਲ ਪੇਸਟ ਕਰੋ। ਯੂਨੀਫ਼ਾਇਡ ਡਿਫ਼ ਅਤੇ ਛੋਟੀ ਵਿਆਖਿਆ ਮੰਗੋ। ਯੂਨੀਫ਼ਾਇਡ ਡਿਫ਼ ਵਿੱਚ ਪੁਰਾਣੀਆਂ ਲਾਈਨਾਂ ਅੱਗੇ `-` ਅਤੇ ਨਵੀਆਂ ਅੱਗੇ `+` ਹੁੰਦਾ ਹੈ। ਦੱਸੀ ਫ਼ਾਈਲ ਟੈਕਸਟ ਐਡੀਟਰ ਵਿੱਚ ਖੋਲ੍ਹੋ, ਪੁਰਾਣੀਆਂ ਲਾਈਨਾਂ ਨੂੰ ਸੁਝਾਏ ਬਦਲ ਨਾਲ ਬਦਲੋ ਅਤੇ ਸੇਵ ਕਰੋ। ਫਿਰ ਨਤੀਜੇ ਦੀ ਸਮੀਖਿਆ ਵਾਲੇ ਸਾਰੇ ਕਮਾਂਡ ਚਲਾਓ। `tasks.json` ਨਾ ਬਦਲੋ। ਦਰਜ ਕਰੋ ਕਿ ਏਜੰਟ ਵਾਲਾ ਕਦਮ ਨਹੀਂ ਚਲਾਇਆ। ਅੰਤਿਮ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਵੱਖਰੀ JSON ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ, ਇਸ ਲਈ ਆਪਣੇ ਫ਼ਿਲਟਰ ਹੱਲ ਦੀ ਤੁਲਨਾ ਪਾਠ 5 ਦੀ ਲੋੜ ਅਤੇ ਜਾਂਚਾਂ ਨਾਲ ਕਰੋ।

## ਇੰਟਰਫੇਸ ਚੁਣੋ

**ਪਹਿਲਾਂ ਸਮੀਖਿਆ ਦੀ ਜਗ੍ਹਾ ਚੁਣੋ।** ChatGPT ਡੈਸਕਟਾਪ ਐਪ ਵਿੱਚ Codex ਦ੍ਰਿਸ਼ਮਾਨ ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਡਿਫ਼ ਸਮੀਖਿਆ ਲਈ ਢੁੱਕਵਾਂ ਹੈ। ਖੋਲ੍ਹੀ ਲੈਬ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕੰਮ ਲਈ ਟਰਮੀਨਲ ਇੰਟਰਫੇਸ ਵਰਤੋ। ਟਰਮੀਨਲ ਚੋਣਾਂ ਦੀ ਆਪਸ ਵਿੱਚ ਤੁਲਨਾ ਕਰੋ:

| ਟਰਮੀਨਲ ਟੂਲ | ਖਾਤਾ ਜਾਂ ਪ੍ਰਦਾਤਾ ਜਾਂਚ | ਸ਼ੁਰੂ ਕਰਨ ਦਾ ਕਮਾਂਡ |
|---|---|---|
| **Codex CLI** | Codex ਸਾਈਨ-ਇਨ ਅਤੇ ਸਥਾਨਕ ਇਜਾਜ਼ਤਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ | `codex` |
| **Claude Code CLI** | Claude Code ਪਹੁੰਚ ਅਤੇ ਸਥਾਨਕ ਇਜਾਜ਼ਤਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ | `claude` |
| **OpenCode TUI** | ਸਮਰਥਿਤ ਮਾਡਲ ਪ੍ਰਦਾਤਾ ਅਤੇ ਇਜਾਜ਼ਤਾਂ ਸੰਰਚਿਤ ਕਰੋ | `opencode` |

**ਚੁਣੇ ਟੂਲ ਦੀ ਮੌਜੂਦਾ ਸਰਕਾਰੀ ਗਾਈਡ ਨਾਲ ਇੰਸਟਾਲ ਅਤੇ ਸਾਈਨ ਇਨ ਕਰੋ।** [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [ChatGPT ਡੈਸਕਟਾਪ ਐਪ](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) ਜਾਂ [OpenCode](https://opencode.ai/docs/) ਪੜ੍ਹੋ। ਕਮਾਂਡ, ਸਮਰਥਿਤ ਪਲੇਟਫ਼ਾਰਮ ਅਤੇ ਖਾਤਾ ਲੋੜਾਂ ਬਦਲਦੀਆਂ ਹਨ। ਇਹ ਪਾਠ ਸਿਰਫ਼ ਸਥਿਰ ਸ਼ੁਰੂਆਤੀ ਨਾਂ ਅਤੇ ਸਾਂਝੀ ਸਮੀਖਿਆ ਪ੍ਰਕਿਰਿਆ ਵਰਤਦਾ ਹੈ।

**ਉਤਪਾਦ ਦੀ ਹੋਰ ਡੂੰਘੀ ਚੋਣ ਲਈ,** ਸਾਈਟ ਦੀ [CLI ਕੋਡਿੰਗ ਏਜੰਟ ਤੁਲਨਾ](/articles/cli-coding-agents-comparison/) ਜਾਂ [ਗ੍ਰਾਫ਼ਿਕਲ ਇੰਟਰਫੇਸ ਏਜੰਟ ਤੁਲਨਾ](/articles/gui-coding-agents-comparison/) ਪੜ੍ਹੋ। [Codex CLI ਅਤੇ ਡੈਸਕਟਾਪ](/articles/codex-cli-vs-desktop/), [Claude Code CLI ਅਤੇ ਡੈਸਕਟਾਪ](/articles/claude-code-cli-vs-desktop/) ਅਤੇ [OpenCode CLI ਅਤੇ ਡੈਸਕਟਾਪ](/articles/opencode-cli-vs-desktop/) ਦੀਆਂ ਗਾਈਡਾਂ ਹਰ ਉਤਪਾਦ ਦੇ ਇੰਟਰਫੇਸ ਦੀ ਤੁਲਨਾ ਕਰਦੀਆਂ ਹਨ।

**ਲੈਬ ਫੋਲਡਰ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** ਹਰ ਇੰਟਰਫੇਸ ਲਈ ਵਰਕਸਪੇਸ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਚੁਣੋ:

1. **Codex ਡੈਸਕਟਾਪ:** ChatGPT ਡੈਸਕਟਾਪ ਐਪ ਖੋਲ੍ਹੋ, ਖੋਲ੍ਹੀ ਲੈਬ ਨੂੰ ਸਥਾਨਕ ਪ੍ਰੋਜੈਕਟ ਵਜੋਂ ਚੁਣੋ ਅਤੇ ਉਸੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਸਥਾਨਕ ਕੰਮ ਸ਼ੁਰੂ ਕਰੋ। ਸੋਧ ਤੋਂ ਪਹਿਲਾਂ ਫੋਲਡਰ ਪਾਥ ਅਤੇ ਮਨਜ਼ੂਰੀ ਸੁਨੇਹੇ ਜਾਂਚੋ। ਹੋਸਟ ਕੀਤਾ ਕੰਮ ਵੱਖਰੀ ਵਰਕਸਪੇਸ ਕਾਪੀ ਵਰਤਦਾ ਹੈ।
2. **Codex CLI:** `cd /path/to/effective-ai-course-lab` ਚਲਾਓ, ਫਿਰ `codex` ਚਲਾਓ। ਦਿਖਾਈ ਫੋਲਡਰ ਅਤੇ ਮਨਜ਼ੂਰੀ ਮੋਡ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
3. **Claude Code CLI:** ਉਹੀ `cd` ਕਮਾਂਡ ਚਲਾਓ, ਫਿਰ `claude` ਚਲਾਓ। ਪ੍ਰੋਜੈਕਟ ਫੋਲਡਰ ਅਤੇ ਟੂਲ ਇਜਾਜ਼ਤਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
4. **OpenCode TUI:** ਉਹੀ `cd` ਕਮਾਂਡ ਚਲਾਓ, ਫਿਰ `opencode` ਚਲਾਓ। ਚੁਣੇ ਪ੍ਰਦਾਤਾ, ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਇਜਾਜ਼ਤ ਸੈਟਿੰਗਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।

**ChatGPT chat ਅਤੇ Claude Projects ਗੱਲਬਾਤਾਂ ਅਤੇ ਸਾਂਝੀਆਂ ਹਵਾਲਾ ਫ਼ਾਈਲਾਂ ਸੰਭਾਲਦੇ ਹਨ।** Codex ਅਤੇ Claude Code ਫ਼ਾਈਲਾਂ ਅਤੇ ਕਮਾਂਡਾਂ ਦੇ ਟੂਲਾਂ ਵਾਲੇ ਕੋਡ ਵਰਕਸਪੇਸ ਵਿੱਚ ਕੰਮ ਕਰਦੇ ਹਨ। OpenCode ਡੈਸਕਟਾਪ ਅਤੇ IDE ਰੂਪ ਵੀ ਦਿੰਦਾ ਹੈ, ਪਰ ਇਹ ਪਾਠ ਟਰਮੀਨਲ ਵਰਤਦਾ ਹੈ। ਪ੍ਰਦਾਤਾ, ਖਾਤਾ ਅਤੇ ਸਥਾਨਕ ਜਾਂ ਹੋਸਟ ਕੀਤੀ ਕਾਰਵਾਈ ਵੱਖਰੀ ਹੁੰਦੀ ਹੈ। ਚੁਣਿਆ ਇੰਟਰਫੇਸ ਦਰਜ ਕਰੋ, ਹਰ ਸੈਸ਼ਨ ਨੂੰ ਇਕੋ ਰਨ ਨਾ ਮੰਨੋ।

**ਲੈਬ ਖੋਲ੍ਹਣ ਤੋਂ ਪਹਿਲਾਂ ਪੰਜ ਗੱਲਾਂ ਜਾਂਚੋ:** ਸਮਰਥਿਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ, ਪ੍ਰਮਾਣੀਕਰਨ, ਪ੍ਰਦਾਤੇ ਜਾਂ ਖਾਤੇ ਦੀ ਲਾਗਤ, ਫ਼ਾਈਲ ਅਤੇ ਕਮਾਂਡ ਇਜਾਜ਼ਤਾਂ, ਅਤੇ ਕੀ ਕੰਮ ਸਥਾਨਕ ਹੈ ਜਾਂ ਰਿਮੋਟ ਹੋਸਟ 'ਤੇ। ਆਪਣੀ ਚੋਣ ਦਰਜ ਕਰੋ। ਇਹ ਨਾ ਮੰਨੋ ਕਿ ਡੈਸਕਟਾਪ ਐਪ ਅਤੇ ਟਰਮੀਨਲ ਟੂਲ ਇੱਕੋ ਵਰਕਸਪੇਸ ਵਰਤਦੇ ਹਨ।

## ਸਟਾਰਟਰ ਦੀ ਜਾਂਚ ਕਰੋ

**ਰਿਪੋਜ਼ਟਰੀ ਸੰਦਰਭ ਪਾਠ ਵਾਲਾ ਸਾਫ਼ ਲੈਬ ਫੋਲਡਰ ਮੁੜ ਖੋਲ੍ਹੋ।** ਇਸ ਕਾਪੀ ਵਿੱਚ ਤੁਹਾਡਾ ਕਮਿਟ ਕੀਤਾ `AGENTS.md` ਅਤੇ ਵਿਕਲਪੀ `CLAUDE.md` ਹਦਾਇਤਾਂ ਹਨ। ਏਜੰਟ ਤੋਂ ਸੋਧ ਮੰਗਣ ਤੋਂ ਪਹਿਲਾਂ ਫ਼ਾਈਲਾਂ ਵੇਖੋ। ਇਸ ਫੋਲਡਰ ਤੋਂ ਬੇਸਲਾਈਨ ਟੈਸਟ ਚਲਾਓ।

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**ਉਮੀਦ ਕੀਤੀ ਬੇਸਲਾਈਨ:** ਰਿਪੋਰਟ `Total tasks: 4` ਦਿਖਾਉਂਦੀ ਹੈ। ਟੈਸਟ ਰਨ ਦੋ ਟੈਸਟਾਂ ਦੇ ਨਾਂ ਦਿੰਦਾ ਹੈ ਅਤੇ `OK` ਨਾਲ ਖ਼ਤਮ ਹੁੰਦਾ ਹੈ। ਕੋਈ ਟੈਸਟ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਰੁਕੋ ਅਤੇ ਖੋਲ੍ਹੀਆਂ ਫ਼ਾਈਲਾਂ ਜਾਂਚੋ। ਖ਼ਰਾਬ ਸ਼ੁਰੂਆਤੀ ਹਾਲਤ ਠੀਕ ਕਰਨ ਦਾ ਸਿਹਰਾ ਏਜੰਟ ਨੂੰ ਨਾ ਦਿਓ।

**ਕੋਰਸ ਸੈੱਟਅੱਪ ਅਤੇ ਰਿਪੋਜ਼ਟਰੀ ਸੰਦਰਭ ਪਾਠ ਦੇ ਸਥਾਨਕ Git ਸਨੈਪਸ਼ਾਟ ਵਰਤੋ।** `AGENTS.md` ਅਤੇ ਵਿਕਲਪੀ `CLAUDE.md` ਪਹਿਲਾਂ ਹੀ ਕਮਿਟ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ। ਵਿਸ਼ੇਸ਼ਤਾ ਸੋਧਣ ਤੋਂ ਪਹਿਲਾਂ `git status --short` ਚਲਾਓ ਅਤੇ ਖਾਲੀ ਨਤੀਜੇ ਦੀ ਉਮੀਦ ਕਰੋ। ਏਜੰਟ ਵੀ ਕਮਿਟ ਨਾ ਕਰੇ। ਆਰਕਾਈਵ ਵਿੱਚ Git ਇਤਿਹਾਸ ਨਹੀਂ ਹੈ। ਇਸ ਦੀ `.gitignore` ਫ਼ਾਈਲ ਟੈਸਟ ਰਨਾਂ ਨਾਲ ਬਣਨ ਵਾਲਾ Python ਬਾਈਟਕੋਡ ਬਾਹਰ ਰੱਖਦੀ ਹੈ। ਨਵੀਂ ਕਾਪੀ ਖੋਲ੍ਹੀ ਹੋਵੇ ਤਾਂ ਉਸ ਫੋਲਡਰ ਵਿੱਚ ਸੈੱਟਅੱਪ ਅਤੇ ਸੰਦਰਭ ਪਾਠ ਦੁਹਰਾਓ। ਵਿਸ਼ੇਸ਼ਤਾ ਤੋਂ ਪਹਿਲਾਂ ਹਦਾਇਤੀ ਫ਼ਾਈਲਾਂ ਕਮਿਟ ਕਰੋ। ਪਹਿਲਾਂ ਸਟਾਰਟਰ ਸ਼ੁਰੂ ਅਤੇ ਕਮਿਟ ਕਰੋ:

```bash
git init
git add .
git commit -m "ਕੋਰਸ ਲੈਬ ਬੁਨਿਆਦ"
```

**ਫਿਰ `AGENTS.md` ਅਤੇ ਵਿਕਲਪੀ `CLAUDE.md` ਸ਼ਾਮਲ ਕਰੋ**, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਸੰਦਰਭ ਪਾਠ ਦਾ ਮਨਜ਼ੂਰ ਸਰੋਤ ਅਤੇ ਟੈਸਟ ਕਮਾਂਡ ਹੋਵੇ। ਇਹ ਫ਼ਾਈਲਾਂ ਕਮਿਟ ਕਰੋ, ਜਾਂਚੋ ਕਿ `git status --short` ਸਾਫ਼ ਹੈ, ਫਿਰ ਵਿਸ਼ੇਸ਼ਤਾ ਸੋਧੋ। ਇਹ ਕਮਾਂਡਾਂ ਖੋਲ੍ਹੇ ਅਭਿਆਸ ਫੋਲਡਰ ਵਿੱਚ ਚਲਾਓ, ਕਿਸੇ ਹੋਰ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਜੜ੍ਹ ਵਿੱਚ ਨਹੀਂ।

## ਸੀਮਿਤ ਬੇਨਤੀ ਦਿਓ

**ਚੁਣੇ ਕੋਡਿੰਗ ਏਜੰਟ ਵਿੱਚ ਲੈਬ ਫੋਲਡਰ ਖੋਲ੍ਹੋ।** ਇਹ ਟਾਸਕ ਪੈਕਟ ਭੇਜੋ:

```text
task_report.py ਵਿੱਚ ਵਿਕਲਪੀ --status ਦਲੀਲ ਜੋੜੋ।
ਮੰਨੀਆਂ ਕਦਰਾਂ: open ਅਤੇ done।
ਇਹ ਨਾ ਹੋਵੇ ਤਾਂ ਮੌਜੂਦਾ ਕੁੱਲ ਗਿਣਤੀ ਆਉਟਪੁੱਟ ਨਾ ਬਦਲੋ।
ਇਹ ਹੋਵੇ ਤਾਂ ਸਿਰਫ਼ ਮੇਲ ਖਾਂਦੇ ਕੰਮ ਗਿਣੋ ਅਤੇ Total tasks: N ਛਾਪੋ।
ਦੋਹਾਂ ਕਦਰਾਂ, ਇੱਕ ਗਲਤ ਕਦਰ ਅਤੇ ਨਾ ਬਦਲੀ ਡਿਫ਼ਾਲਟ ਆਉਟਪੁੱਟ ਲਈ ਟੈਸਟ ਜੋੜੋ।
tasks.json ਜਾਂ ਬੇਸਬੰਧ ਫ਼ਾਈਲਾਂ ਨਾ ਬਦਲੋ।
ਟੈਸਟ ਚਲਾਓ ਅਤੇ ਸਹੀ ਕਮਾਂਡ ਤੇ ਨਤੀਜਾ ਦੱਸੋ।
ਕੋਡ ਅਤੇ ਟੈਸਟਾਂ ਤੋਂ ਬਾਅਦ ਰੁਕੋ। ਕਮਿਟ ਜਾਂ ਪੁਸ਼ ਨਾ ਕਰੋ।
```

**Windows ਉੱਤੇ,** `python3` ਦੀ ਥਾਂ ਸੈੱਟਅੱਪ ਦੌਰਾਨ ਜਾਂਚਿਆ `py -3` ਵਰਤੋ, ਸੁਰੱਖਿਅਤ ਰਿਪੋਜ਼ਟਰੀ ਹਦਾਇਤਾਂ ਅਤੇ ਟਾਸਕ ਪੈਕਟ ਵਿੱਚ ਵੀ।

**ਕੋਡ ਜਾਣੂ ਨਾ ਹੋਵੇ ਤਾਂ ਸੋਧ ਤੋਂ ਪਹਿਲਾਂ ਛੋਟੀ ਯੋਜਨਾ ਮੰਗੋ।** ਏਜੰਟ ਨੂੰ ਸਿਰਫ਼ ਅਸਥਾਈ ਲੈਬ ਫੋਲਡਰ ਸੋਧਣ ਦਿਓ। ਟੂਲਾਂ ਵਿੱਚ ਇਜਾਜ਼ਤ ਨਿਯੰਤਰਣ ਵੱਖਰੇ ਹਨ, ਇਸ ਲਈ ਸ਼ੈੱਲ ਕਮਾਂਡ ਜਾਂ ਫ਼ਾਈਲ ਲਿਖਣ ਦੀ ਇਜਾਜ਼ਤ ਤੋਂ ਪਹਿਲਾਂ ਮੌਜੂਦਾ ਸੈਟਿੰਗਾਂ ਜਾਂਚੋ।

## ਨਤੀਜੇ ਦੀ ਸਮੀਖਿਆ ਕਰੋ

**ਡਿਫ਼ ਪੜ੍ਹੋ।** ਜਾਂਚੋ ਕਿ ਬਿਨਾਂ ਫ਼ਿਲਟਰ ਆਉਟਪੁੱਟ ਨਾ ਬਦਲੇ, ਫ਼ਿਲਟਰ ਸਿਰਫ਼ ਦੋ ਮੁੱਲ ਸਵੀਕਾਰੇ ਅਤੇ ਟੈਸਟ ਗਲਤ ਮੁੱਲ ਤੇ ਨਾ ਬਦਲੇ ਡਿਫ਼ਾਲਟ ਆਉਟਪੁੱਟ ਨੂੰ ਕਵਰ ਕਰਨ। ਟੈਸਟ ਤਦ ਹੀ ਤਬਦੀਲੀ ਦਾ ਸਬੂਤ ਹਨ ਜੇ ਉਹ ਮੰਗਿਆ ਵਰਤਾਅ ਜਾਂਚਦੇ ਹਨ।

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**ਉਮੀਦ ਕੀਤੇ ਨਤੀਜੇ:** ਪਹਿਲੀਆਂ ਤਿੰਨ ਰਿਪੋਰਟ ਕਮਾਂਡਾਂ 4, 2 ਅਤੇ 2 ਦਿਖਾਉਂਦੀਆਂ ਹਨ। ਗਲਤ ਮੁੱਲ ਸਪਸ਼ਟ ਗਲਤੀ ਦਿਖਾਉਂਦਾ ਹੈ ਅਤੇ ਪ੍ਰਕਿਰਿਆ ਸਿਫ਼ਰ ਤੋਂ ਵੱਖਰੇ ਸਟੇਟਸ ਨਾਲ ਮੁੱਕਦੀ ਹੈ। ਗਲਤੀ ਦਾ ਅਸਲ ਪਾਠ ਲਾਗੂਕਰਨ ਉੱਤੇ ਨਿਰਭਰ ਹੈ। macOS ਜਾਂ Linux ਉੱਤੇ ਗਲਤ ਕਮਾਂਡ ਤੋਂ ਤੁਰੰਤ ਬਾਅਦ `echo $?` ਚਲਾਓ। PowerShell ਵਿੱਚ `$LASTEXITCODE` ਵੇਖੋ।

| ਸਬੂਤ | ਕੀ ਜਾਂਚਣਾ ਹੈ |
|---|---|
| **ਫ਼ਾਈਲ ਸੂਚੀ** | ਸਿਰਫ਼ ਪ੍ਰੋਗਰਾਮ ਅਤੇ ਟੈਸਟ ਬਦਲੇ |
| **ਡਿਫ਼** | ਫ਼ਿਲਟਰ ਤਰਕ ਬੇਨਤੀ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ |
| **ਟੈਸਟ ਆਉਟਪੁੱਟ** | ਨਵੇਂ ਕੇਸ ਚਲੇ ਅਤੇ ਪਾਸ ਹੋਏ |
| **ਹੱਥੀਂ ਰਨ** | ਡਿਫ਼ਾਲਟ, `open` ਅਤੇ `done` ਗਿਣਤੀਆਂ `tasks.json` ਨਾਲ ਮੇਲ ਖਾਂਦੀਆਂ ਹਨ |

**ਜੇ ਏਜੰਟ ਟੈਸਟ ਚਲਾਏ ਬਿਨਾਂ ਨਤੀਜਾ ਦੱਸੇ,** ਕਮਾਂਡ ਖੁਦ ਚਲਾਓ। ਸੋਧ ਟਾਸਕ ਪੈਕਟ ਤੋਂ ਬਾਹਰ ਜਾਵੇ ਤਾਂ ਸੀਮਿਤ ਸੁਧਾਰ ਮੰਗੋ। ਹਾਲਤ ਸਪਸ਼ਟ ਨਾ ਹੋਵੇ ਤਾਂ ਖੋਲ੍ਹੀ ਅਭਿਆਸ ਕਾਪੀ ਮਿਟਾ ਕੇ ਅਸਲ ZIP ਮੁੜ ਖੋਲ੍ਹੋ।

## ਅਧਿਐਨ ਮਾਰਗ ਦੇ ਜਵਾਬ

**ਹੱਥੀਂ ਪੈਚ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਇਹ ਪੂਰੀਆਂ ਫ਼ਾਈਲਾਂ ਵਰਤੋ।** ਨਵੀਂ ਖੋਲ੍ਹੀ ਲੈਬ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ, ਪਹਿਲਾ ਬਲਾਕ `task_report.py` ਅਤੇ ਦੂਜਾ `tests/test_task_report.py` ਵਜੋਂ ਸੇਵ ਕਰੋ, ਫਿਰ ਨਤੀਜੇ ਦੀ ਸਮੀਖਿਆ ਵਾਲੇ ਕਮਾਂਡ ਚਲਾਓ। `tasks.json` ਅਤੇ `docs/requirements.md` ਨਾ ਬਦਲੋ। ਫ਼ਾਈਲਾਂ ਨਕਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਪਹਿਲੀ ਗੜਬੜ ਦਰਜ ਕਰੋ।

`task_report.py`:

```python
"""JSON ਫ਼ਾਈਲ ਵਿੱਚ ਕੰਮਾਂ ਦੀ ਗਿਣਤੀ ਦਿਖਾਓ।"""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """ਸਾਰੇ ਕੰਮ ਜਾਂ ਮਨਜ਼ੂਰ ਹਾਲਤ ਵਾਲੇ ਕੰਮ ਗਿਣੋ।"""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="ਵਰਕਸ਼ਾਪ ਦੇ ਕੰਮ ਗਿਣੋ")
    parser.add_argument("path", type=Path, help="JSON ਕੰਮ ਸੂਚੀ ਦਾ ਰਸਤਾ")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""ਵਰਕਸ਼ਾਪ ਕੰਮ ਰਿਪੋਰਟ ਦੇ ਟੈਸਟ।"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**ਸੰਦਰਭ ਅਤੇ ਨਤੀਜਾ-ਜਾਂਚ ਪਾਠਾਂ ਲਈ ਫ਼ਿਲਟਰ ਟੈਸਟ ਪਾਸ ਕਰਨ ਵਾਲੀ ਸੋਧੀ ਕਾਪੀ ਰੱਖੋ।** ਜੇ ਇਸ ਜਵਾਬ ਨਾਲ ਕੰਮ ਠੀਕ ਕੀਤਾ, ਅਗਲੇ ਪਾਠਾਂ ਲਈ ਨਵੀਂ ਕਾਪੀ ਅਤੇ ਪਾਸ ਟੈਸਟ ਸੰਭਾਲੋ। ਡਿਫ਼ ਅਤੇ ਟੈਸਟ ਰਿਕਾਰਡ ਲੈਬ ਤੋਂ ਬਾਹਰ ਰੱਖੋ। ਸੌਂਪਣ ਵਾਲੇ ਪਾਠ ਤੋਂ ਪਹਿਲਾਂ ਸਟਾਰਟਰ ਮੁੜ ਬਹਾਲ ਕਰੋ ਜਾਂ ਅਸਫਲ ਕੋਸ਼ਿਸ਼ ਮਿਟਾ ਕੇ ਸਾਫ਼ ਸ਼ੁਰੂ ਕਰੋ।

## ਅਭਿਆਸ ਅਤੇ ਜਾਂਚ

**ਤੁਹਾਡਾ ਨਤੀਜਾ:** ਲੈਬ ਡਿਫ਼ ਅਤੇ ਚਾਰ-ਲਾਈਨਾਂ ਦਾ ਸਮੀਖਿਆ ਰਿਕਾਰਡ: ਫ਼ਾਈਲ ਦਾਇਰਾ, ਡਿਫ਼ਾਲਟ ਵਰਤਾਅ, ਫ਼ਿਲਟਰ ਵਰਤਾਅ ਅਤੇ ਗਲਤ ਇਨਪੁੱਟ। ਵਰਜਨ-ਖਾਸ ਸਮੱਸਿਆ ਦੁਹਰਾਉਣ ਲਈ ਟੂਲ ਦਾ ਨਾਂ ਅਤੇ ਵਰਜਨ ਨਿੱਜੀ ਨੋਟ ਵਿੱਚ ਲਿਖੋ।

**ਉਮੀਦ ਕੀਤਾ ਤਰਕ:** ਤੁਸੀਂ ਆਪਣੇ ਕੰਮ ਦੇ ਢੰਗ ਅਨੁਸਾਰ ਇੰਟਰਫੇਸ ਚੁਣਿਆ, ਸੀਮਿਤ ਕੰਮ ਦਿੱਤਾ, ਅਸਲ ਸੋਧ ਵੇਖੀ ਅਤੇ ਏਜੰਟ ਦੀ ਰਿਪੋਰਟ ਤੋਂ ਵੱਖਰੀ ਜਾਂਚ ਚਲਾਈ।

## ਆਪਣੀ ਸਮਝ ਜਾਂਚੋ

1. **ਸਵਾਲ:** ਕੀ ਸਾਬਤ ਕਰਦਾ ਹੈ ਕਿ ਸਟੇਟ ਫ਼ਿਲਟਰ ਕੰਮ ਕਰਦਾ ਹੈ? **ਜਵਾਬ:** ਸੀਮਿਤ ਡਿਫ਼, ਪਾਸ ਟੈਸਟ ਅਤੇ ਡਿਫ਼ਾਲਟ, open, done ਤੇ ਗਲਤ ਮੁੱਲ ਦੇ ਵੇਖੇ ਨਤੀਜੇ।
2. **ਸਵਾਲ:** ਏਜੰਟ ਦਾ ਇਹ ਕਹਿਣਾ ਕਿ ਉਸਨੇ ਟੈਸਟ ਚਲਾਏ, ਕੀ ਤੁਹਾਡਾ ਟੈਸਟ ਨਤੀਜਾ ਹੈ? **ਜਵਾਬ:** ਨਹੀਂ। ਕਮਾਂਡ ਚਲਾਓ ਜਾਂ ਟੈਸਟ ਆਉਟਪੁੱਟ ਵੇਖੋ।

## ਸਮੱਸਿਆ ਹੱਲ

- **ਕਮਾਂਡ ਨਹੀਂ ਮਿਲਦੀ:** ਲਿੰਕ ਕੀਤੀ ਵਿਕਰੇਤਾ ਗਾਈਡ ਨਾਲ ਇੰਸਟਾਲੇਸ਼ਨ ਪੂਰੀ ਕਰੋ, ਫਿਰ ਟਰਮੀਨਲ ਮੁੜ ਖੋਲ੍ਹੋ।
- **ਫ਼ਾਈਲ ਪਹੁੰਚ ਨਹੀਂ:** ਖੋਲ੍ਹੀ ਲੈਬ ਡਾਇਰੈਕਟਰੀ ਖੋਲ੍ਹੋ ਅਤੇ ਵਰਕਸਪੇਸ ਇਜਾਜ਼ਤਾਂ ਜਾਂਚੋ।
- **ਅਣਉਮੀਦ ਫ਼ਾਈਲਾਂ ਬਦਲੀਆਂ:** ਅਗਲੀ ਬੇਨਤੀ ਤੋਂ ਪਹਿਲਾਂ ਰੁਕੋ ਅਤੇ `git status --short` ਵੇਖੋ।
- **ਟੈਸਟ ਪਾਸ, ਵਰਤਾਅ ਗਲਤ:** ਹੱਥੀਂ ਜਾਂਚ ਜਾਂ ਛੁੱਟੀ ਲੋੜ ਲਈ ਟੈਸਟ ਜੋੜੋ।

## ਅਗਲੇ ਕਦਮ

**[ਸੰਦਰਭ ਵਿੰਡੋ ਅਤੇ ਕੰਮ ਸੌਂਪਣਾ](/articles/effective-ai-context-window-management/)** ਨਾਲ ਜਾਰੀ ਰੱਖੋ। ਤੁਸੀਂ ਨਵੇਂ ਸੈਸ਼ਨ ਲਈ ਲਾਭਦਾਇਕ ਰਿਕਾਰਡ ਰੱਖੋਗੇ।

**ਕੋਰਸ ਨੈਵੀਗੇਸ਼ਨ:** [ਪਿਛਲਾ: ਟਾਸਕ ਪੈਕਟ](/articles/effective-ai-task-packets/), [ਕੋਰਸ ਰੂਪਰੇਖਾ](/effective-ai-course-start/).
