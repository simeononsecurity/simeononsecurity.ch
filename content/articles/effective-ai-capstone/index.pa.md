---
title: "AI ਵਰਕਫ਼ਲੋ ਕੈਪਸਟੋਨ: JSON ਰਿਪੋਰਟ ਬਣਾਓ ਅਤੇ ਜਾਂਚੋ"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "ਪ੍ਰੋਜੈਕਟ ਸੰਦਰਭ, ਸੀਮਿਤ ਏਜੰਟ ਬੇਨਤੀ, ਸੁਤੰਤਰ ਟੈਸਟਾਂ, ਸਰੋਤ ਸਮੀਖਿਆ ਅਤੇ ਨਵੇਂ ਸੈਸ਼ਨ ਲਈ ਹਵਾਲੇ ਸਮੇਤ ਨਵੀਂ JSON ਟਾਸਕ ਰਿਪੋਰਟ ਬਣਾਓ।"
genre: ["ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ", "ਸਾਫਟਵੇਅਰ ਇੰਜੀਨੀਅਰਿੰਗ", "ਸਿੱਖਿਆ"]
tags: ["AI ਵਰਕਫ਼ਲੋ ਕੈਪਸਟੋਨ", "ਕੋਡਿੰਗ ਏਜੰਟ ਪ੍ਰੋਜੈਕਟ", "AI ਟਾਸਕ ਜਾਂਚ", "AGENTS.md", "MCP ਅਭਿਆਸ", "ਏਜੰਟ ਹਵਾਲਾ"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "ਸਰੋਤ ਫ਼ਾਈਲਾਂ, ਟੈਸਟ ਨਤੀਜਿਆਂ, ਏਜੰਟ ਸਮੀਖਿਆ ਅਤੇ ਹਵਾਲਾ ਰਿਕਾਰਡ ਵਾਲਾ ਪੂਰਾ ਹੋਇਆ ਵਰਕਸ਼ਾਪ ਸਾਫਟਵੇਅਰ ਕੰਮ"
coverCaption: ""
---

[ਵਿਹਾਰਕ AI ਵਰਕਫ਼ਲੋ ਕੋਰਸ ’ਤੇ ਵਾਪਸ ਜਾਓ](/effective-ai-course-start/)

**ਨਵਾਂ ਆਉਟਪੁੱਟ ਫ਼ਾਰਮੈਟ ਬਣਾਓ ਅਤੇ ਇਸ ਦੇ ਵਿਹਾਰ ਦਾ ਸਬੂਤ ਦਿਓ।** ਪਹਿਲਾਂ ਤੁਸੀਂ ਸਟੇਟਸ ਫ਼ਿਲਟਰ ਜੋੜਿਆ ਸੀ। ਇਹ ਕੈਪਸਟੋਨ ਨਵੀਂ ਲੈਬ ਤੋਂ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਹੋਰ ਪ੍ਰੋਗਰਾਮ ਵੱਲੋਂ ਪੜ੍ਹੀ ਜਾਣ ਵਾਲੀ JSON ਰਿਪੋਰਟ ਜੋੜਦਾ ਹੈ। ਨਵੀਂ ਲੋੜ ਜਾਂਚਦੀ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣਾ ਵਰਕਫ਼ਲੋ ਹੋਰ ਫੀਚਰ ’ਤੇ ਲਾਗੂ ਕਰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

**ਸਿੱਖਣ ਦਾ ਨਤੀਜਾ:** ਤੁਸੀਂ ਜਾਂਚੀ ਹੋਈ JSON ਰਿਪੋਰਟ, ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਾਂ ਦੇ ਸਬੂਤਾਂ ਦਾ ਰਿਕਾਰਡ ਅਤੇ ਨਵੇਂ ਸੈਸ਼ਨ ਨੂੰ ਸਮਝ ਆਉਣ ਵਾਲਾ ਹਵਾਲਾ ਤਿਆਰ ਕਰੋਗੇ।

## ਮੁੱਖ ਗੱਲਾਂ

- **ਵੱਖਰੀ ਲੋੜ** ਕੈਪਸਟੋਨ ਫੀਚਰ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ।
- **ਕੋਡਿੰਗ ਏਜੰਟ ਦੀ ਸੋਧ** ਦੱਸੀਆਂ ਫ਼ਾਈਲਾਂ ਤੱਕ ਸੀਮਿਤ ਰਹਿੰਦੀ ਹੈ।
- **ਸੁਤੰਤਰ ਜਾਂਚਾਂ** ਸਵੀਕਾਰਤਾ ਨਿਰਧਾਰਤ ਕਰਦੀਆਂ ਹਨ।
- **ਨਵੇਂ ਸੈਸ਼ਨ ਲਈ ਹਵਾਲਾ** ਨਤੀਜੇ ਨੂੰ ਦੁਬਾਰਾ ਸਮਝਣ ਦਿੰਦਾ ਹੈ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਪੂਰਵ-ਸ਼ਰਤਾਂ:** ਪਾਠ 0 ਤੋਂ 10 ਪੂਰੇ ਕਰੋ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਰਿਪੋਜ਼ਟਰੀ ਸੰਦਰਭ, ਪਹਿਲਾ ਕੋਡਿੰਗ ਕੰਮ, MCP ਜਾਂ ਬ੍ਰਾਊਜ਼ਰ ਵਿਕਲਪ, ਡੈਲੀਗੇਸ਼ਨ ਅਤੇ ਸੀਮਿਤ ਚੱਕਰ ਸ਼ਾਮਲ ਹਨ। ਪਾਠ 11 ਵਿਕਲਪਿਕ ਹੈ। 90 ਤੋਂ 120 ਮਿੰਟ ਰੱਖੋ। ਔਖਿਆਈ ਦਰਮਿਆਨੀ ਹੈ।

[ਸ਼ੁਰੂਆਤੀ ਲੈਬ](/downloads/effective-ai-course-lab.zip) ਦੀ **ਨਵੀਂ ਨਕਲ ਖੋਲ੍ਹੋ**। ਸੋਧ ਤੋਂ ਪਹਿਲਾਂ `python3 task_report.py tasks.json` ਅਤੇ ਦੋ ਬੇਸਲਾਈਨ ਟੈਸਟ ਚਲਾਓ। Windows ’ਤੇ `py -3` ਵਰਤੋ ਜੇ ਤੁਹਾਡੀ ਸੈਟਅੱਪ ਵਿੱਚ Python launcher ਹੈ। ਕੋਰਸ ਸੈਟਅੱਪ ਵਾਂਗ ਸਥਾਨਕ Git ਬੇਸਲਾਈਨ ਬਣਾਓ। ਪਾਠ 5 ਦਾ ਸਟੇਟਸ ਫ਼ਿਲਟਰ ਜਾਣਬੁੱਝ ਕੇ ਮੌਜੂਦ ਨਹੀਂ।

**`docs/capstone-requirements.md`, revision 1 ਪੜ੍ਹੋ।** ਇਸ ਵਿੱਚ `--format text|json` ਦੀ ਲੋੜ ਹੈ। ਮੂਲ ਟੈਕਸਟ `Total tasks: 4` ਹੀ ਰਹਿੰਦਾ ਹੈ। JSON ਆਉਟਪੁੱਟ ਵਿੱਚ ਅੰਕੀ ਕੁੱਲ ਅਤੇ ਡਾਟਾ ਵਿੱਚ ਹਰ ਸਟੇਟ ਦੀ ਗਿਣਤੀ ਹੁੰਦੀ ਹੈ। ਖਾਲੀ ਸੂਚੀ, ਗੁੰਮ ਸਟੇਟਸ ਅਤੇ ਅਸਮਰਥਿਤ ਫ਼ਾਰਮੈਟ ਜਾਂਚੋ। ਇਸ ਨਵੇਂ ਫੀਚਰ ਲਈ `docs/requirements.md` ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਨਾ ਮੰਨੋ।

**ਆਪਣਾ ਰਾਹ ਚੁਣੋ।** ਜੁੜਿਆ ਰਾਹ ਕੋਡਿੰਗ ਏਜੰਟ ਦੀ ਦੇਖੀ ਗਈ ਸੋਧ, ਅਸਲ read-only MCP ਕਾਲ ਅਤੇ ਮੂਲ worker ਜਾਂ ਵੱਖਰਾ worker ਸੈਸ਼ਨ ਵਰਤਦਾ ਹੈ। ਅਧਿਐਨ ਰਾਹ ਕੋਡ ਸੁਝਾਉਣ ਲਈ chat assistant, MCP ਦੀ ਥਾਂ ਬ੍ਰਾਊਜ਼ਰ ਸਰੋਤ ਅਤੇ ਨਕਲੀ worker ਵਜੋਂ ਵੱਖਰੀਆਂ chats ਵਰਤਦਾ ਹੈ। ਅਣਉਪਲਬਧ ਟੂਲ ਕਦਮਾਂ ਨੂੰ “ਨਹੀਂ ਚਲਾਇਆ” ਲਿਖੋ। ਦੋਵੇਂ ਰਾਹਾਂ ਲਈ ਸਥਾਨਕ ਟੈਸਟ ਅਤੇ ਫ਼ਾਈਲ ਸਮੀਖਿਆ ਲਾਜ਼ਮੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ ਉੱਤਰ-ਕੁੰਜੀ ਵਿੱਚ ਮੁੜ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਪੂਰੀਆਂ ਫ਼ਾਈਲਾਂ ਹਨ। ਕੁੰਜੀ ਨੂੰ ਨਵੀਂ ਨਕਲ ਵਿੱਚ ਪਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੀ ਪਹਿਲੀ ਕੋਸ਼ਿਸ਼ ਨੋਟਾਂ ਵਿੱਚ ਸੰਭਾਲੋ।

## ਜਾਂਚ 1: ਪ੍ਰੋਜੈਕਟ ਸੰਖੇਪ

**ਸਿੰਥੈਟਿਕ ChatGPT ਜਾਂ Claude ਵਰਕਸ਼ਾਪ ਪ੍ਰੋਜੈਕਟ ਖੋਲ੍ਹੋ।** ਦੋ ਵਾਕਾਂ ਦਾ ਯਾਦ-ਦਿਹਾਨੀ ਮਸੌਦਾ ਮੰਗੋ। `approved-schedule.md` ਵਿੱਚ 7 ਵਜੇ ਨਾਲ ਇਸ ਦਾ ਸਮਾਂ ਮਿਲਾਓ। ਸਮਾਂ-ਸੂਚੀ ਯਾਦ-ਦਿਹਾਨੀ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ। ਕੈਪਸਟੋਨ ਲੋੜ ਪ੍ਰੋਗਰਾਮ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ।

**ਸਬੂਤ:** ਪ੍ਰੋਜੈਕਟ ਦਾ ਨਾਮ, ਸਰੋਤ revision, ਮਸੌਦੇ ਵਿੱਚ ਦੇਖਿਆ ਸਮਾਂ ਅਤੇ ਕੋਈ ਸੁਧਾਰ ਦਰਜ ਕਰੋ। ਸੁਨੇਹਾ ਨਾ ਭੇਜੋ।

## ਜਾਂਚ 2: ਰਿਪੋਜ਼ਟਰੀ ਸੰਦਰਭ

**ਨਵੀਂ ਲੈਬ ਖੋਲ੍ਹੋ।** ਛੋਟੀ `AGENTS.md` ਬਣਾਓ ਜੋ `docs/capstone-requirements.md`, `task_report.py`, ਟੈਸਟਾਂ ਅਤੇ ਸੈਟਅੱਪ ਦੌਰਾਨ ਜਾਂਚੇ ਟੈਸਟ ਹੁਕਮ ਵੱਲ ਦੱਸੇ। Claude Code ਵਰਤਦੇ ਹੋ ਤਾਂ ਸਾਂਝੀ ਫ਼ਾਈਲ `CLAUDE.md` ਤੋਂ ਜੋੜੋ। ਇਨ੍ਹਾਂ ਹਦਾਇਤੀ ਫ਼ਾਈਲਾਂ ਲਈ ਮਨੁੱਖੀ setup commit ਕਰੋ, ਫਿਰ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ `git status --short` ਖਾਲੀ ਹੈ। ਕੋਡਿੰਗ ਏਜੰਟ ਫੀਚਰ ਸੋਧ commit ਨਹੀਂ ਕਰੇਗਾ।

**ਸਬੂਤ:** ਨਕਸ਼ਾ ਅਤੇ ਸਾਫ਼ ਹਦਾਇਤਾਂ ਸੰਭਾਲੋ। Revision 1 ਤੋਂ JSON keys ਅਤੇ ਗਲਤ ਇਨਪੁੱਟਾਂ ਦਾ ਵਿਹਾਰ ਲਿਖੋ। ਪਿਛਲੀ chat ਵਿੱਚ ਸਟੇਟਸ ਫ਼ਿਲਟਰ ਦੀ ਗੱਲ ਹੋਈ ਹੋਵੇ ਤਾਂ ਉਸਨੂੰ ਹੋਰ ਕੰਮ ਦਾ ਸੰਦਰਭ ਮੰਨੋ।

## ਜਾਂਚ 3: ਬਾਹਰੀ ਸਰੋਤ

**ਜੁੜਿਆ ਰਾਹ:** ਸਮਰਥਿਤ client ਰਾਹੀਂ [OpenAI Docs MCP ਸਰਵਰ, ਸਿਰਫ਼ ਪੜ੍ਹਨ ਲਈ](https://learn.chatgpt.com/learn/docs-mcp) ਵਰਤੋ। MCP ਟੂਲ ਤੋਂ `AGENTS.md` ਦੀਆਂ ਮੌਜੂਦਾ ਹਦਾਇਤਾਂ ਮੰਗੋ। ਟੂਲ ਦਾ ਨਾਮ, ਸਰੋਤ URL ਅਤੇ ਲੈਬ ਨਾਲ ਜੁੜੀ ਇੱਕ ਗੱਲ ਦਰਜ ਕਰੋ। ਫਿਰ ਅਭਿਆਸ ਵਾਲਾ ਕੁਨੈਕਸ਼ਨ ਹਟਾਓ।

**ਅਧਿਐਨ ਰਾਹ:** ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ [`AGENTS.md` ਦੀ ਅਧਿਕਾਰਤ ਦਸਤਾਵੇਜ਼ੀ](https://learn.chatgpt.com/docs/agent-configuration/agents-md) ਖੋਲ੍ਹੋ। ਸਿਰਲੇਖ, URL ਅਤੇ ਲਾਭਦਾਇਕ ਗੱਲ ਦਰਜ ਕਰੋ। MCP ਖੋਜ ਅਤੇ ਚਲਾਉਣ ਨੂੰ “ਨਹੀਂ ਚਲਾਇਆ” ਲਿਖੋ।

**ਸਬੂਤ:** ਸੰਰਚਿਤ server entry ਉਸ ਦੇ ਚੱਲਣ ਦਾ ਸਬੂਤ ਨਹੀਂ। ਜੁੜੇ ਰਾਹ ਲਈ ਦਿਖਾਈ ਦੇਣ ਵਾਲੀ ਟੂਲ ਕਾਲ ਅਤੇ ਵਾਪਸ ਆਇਆ ਸਰੋਤ ਲੋੜੀਂਦਾ ਹੈ।

## ਜਾਂਚ 4: ਇੱਕ ਸਮੀਖਿਆ ਸੌਂਪੋ

**read-only worker ਨੂੰ** `docs/capstone-requirements.md`, `task_report.py` ਅਤੇ ਬੇਸਲਾਈਨ ਟੈਸਟ ਵੇਖਣ ਲਈ ਕਹੋ। ਗੁੰਮ ਜਾਂਚਾਂ ਅਤੇ ਫ਼ਾਈਲ ਪਾਥਾਂ ਵਾਲੀਆਂ ਵੱਧ ਤੋਂ ਵੱਧ ਪੰਜ ਲਾਈਨਾਂ ਮੰਗੋ। ਅਧਿਐਨ ਰਾਹ ਵਿੱਚ ਵੱਖਰੀ chat ਵਰਤੋ ਅਤੇ ਉਸਨੂੰ ਨਕਲੀ worker ਲਿਖੋ।

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** ਸ਼ੁਰੂਆਤੀ ਟੈਸਟ ਕੁੱਲ ਅਤੇ ਗੈਰ-ਸੂਚੀ JSON ਮੁੱਲ ਜਾਂਚਦੇ ਹਨ। ਉਹ JSON ਆਉਟਪੁੱਟ, ਖਾਲੀ ਸੂਚੀ, ਗੁੰਮ ਸਟੇਟਸ ਜਾਂ ਗਲਤ ਫ਼ਾਰਮੈਟ ਨਹੀਂ ਜਾਂਚਦੇ। ਰਿਪੋਰਟ ਦੀ ਖੁਦ ਟੈਸਟ ਫ਼ਾਈਲ ਖੋਲ੍ਹ ਕੇ ਪੁਸ਼ਟੀ ਕਰੋ। ਛੋਟੀ ਸੁਤੰਤਰ ਸਮੀਖਿਆ ਲਾਭਦਾਇਕ ਹੈ ਕਿਉਂਕਿ ਸਵੀਕਾਰਤਾ ਦੇ ਮਾਪਦੰਡ ਪਾਠ 5 ਤੋਂ ਵੱਖਰੇ ਹਨ।

**ਸਬੂਤ:** ਛੋਟੀ ਰਿਪੋਰਟ ਅਤੇ ਇੱਕ ਵਾਕ ਵਿੱਚ ਆਪਣਾ ਇਕੀਕਰਨ ਫ਼ੈਸਲਾ ਸੰਭਾਲੋ। Worker transcript ਮੁੱਖ ਕੰਮ ਰਿਕਾਰਡ ਤੋਂ ਬਾਹਰ ਰੱਖੋ।

## ਜਾਂਚ 5: ਸੋਧ ਮੰਗੋ

**ਕੋਡਿੰਗ ਏਜੰਟ ਨੂੰ** ਹੇਠਾਂ ਦਿੱਤਾ ਪੈਕੇਟ ਦਿਓ। ਅਧਿਐਨ ਰਾਹ ਵਿੱਚ chat assistant patch ਸੁਝਾਉਂਦਾ ਹੈ, ਜਿਸਨੂੰ ਤੁਸੀਂ ਲੈਬ ਵਿੱਚ ਹੱਥੀਂ ਲਾਗੂ ਕਰਦੇ ਹੋ।

```text
ਉਦੇਸ਼: JSON ਪਾਥ ਤੋਂ ਬਾਅਦ --format text|json ਜੋੜੋ।
ਸਰੋਤ: docs/capstone-requirements.md, revision 1.
ਮਨਜ਼ੂਰ ਸੋਧਾਂ: task_report.py ਅਤੇ tests/test_task_report.py.
ਬਚਾਉਣਾ: ਮੂਲ Total tasks: 4 ਅਤੇ tasks.json ਬਿਨਾਂ ਬਦਲਾਅ।
JSON: total ਅਤੇ by_status ਗਿਣਤੀਆਂ ਵਾਲਾ ਇੱਕ object, stdout ’ਤੇ ਵਾਧੂ ਟੈਕਸਟ ਨਹੀਂ।
ਲਾਜ਼ਮੀ ਜਾਂਚਾਂ: ਮੂਲ ਅਤੇ ਸਪਸ਼ਟ text, JSON 4/2/2, ਖਾਲੀ ਸੂਚੀ,
ਗੁੰਮ ਸਟੇਟਸ, ਗਲਤ ਫ਼ਾਰਮੈਟ ਅਤੇ ਬੇਸਲਾਈਨ ਟੈਸਟ।
ਰੁਕੋ ਜੇ: ਸਰੋਤ ਟਕਰਾਏ, ਬੇਸਲਾਈਨ ਦੀ ਬੇਸਬੰਧ ਨਾਕਾਮੀ ਹੋਵੇ ਜਾਂ ਹੱਦ ਤੋਂ ਬਾਹਰ ਸੋਧ ਹੋਵੇ।
ਰਿਪੋਰਟ: ਬਦਲੀਆਂ ਫ਼ਾਈਲਾਂ, ਹੁਕਮ, ਦੇਖੇ ਨਤੀਜੇ, ਅਣਸੁਲਝੀ ਸਮੱਸਿਆ।
Commit, push, ਪ੍ਰਕਾਸ਼ਨ ਜਾਂ ਸੁਨੇਹਾ ਨਾ ਭੇਜੋ।
```

**ਸੋਧ ਤੋਂ ਪਹਿਲਾਂ ਯੋਜਨਾ ਵੇਖੋ।** Schema ਦੀ ਚੋਣ ਮਹੱਤਵ ਰੱਖਦੀ ਹੈ: `total` ਅੰਕ ਹੈ, `"4"` string ਨਹੀਂ। `by_status` ਵਿੱਚ ਇਨਪੁੱਟ ਦੇ ਹਰ ਸਟੇਟ ਦੀ ਗਿਣਤੀ ਹੈ, ਇਸ ਲਈ ਭਵਿੱਖ ਦਾ ਸਟੇਟ ਵੀ ਆਵੇਗਾ। ਸੋਧ ਖੁੱਲ੍ਹੀ ਲੈਬ ਤੱਕ ਸੀਮਿਤ ਰੱਖੋ।

## ਜਾਂਚ 6: ਟੈਸਟ ਅਤੇ ਸਮੀਖਿਆ

**ਇਹ ਜਾਂਚਾਂ ਖੁਦ ਚਲਾਓ।** Windows ’ਤੇ `python3` ਦੀ ਥਾਂ `py -3` ਵਰਤੋ। JSON keys ਦਾ ਸਹੀ ਕ੍ਰਮ ਅਤੇ ਖਾਲੀ ਥਾਵਾਂ ਅਹਿਮ ਨਹੀਂ। ਆਉਟਪੁੱਟ ਨੂੰ JSON ਵਜੋਂ ਪੜ੍ਹੋ ਅਤੇ ਮੁੱਲਾਂ ਦੀ ਕਿਸਮ ਮਿਲਾਓ।

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**ਉਮੀਦ ਕੀਤਾ ਵਿਹਾਰ:** ਟੈਸਟ ਪਾਸ ਹੁੰਦੇ ਹਨ। ਦੋਵੇਂ text ਹੁਕਮ `Total tasks: 4` ਛਾਪਦੇ ਹਨ। JSON ਹੁਕਮ `total` 4, `by_status.open` 2 ਅਤੇ `by_status.done` 2 ਵਾਲਾ ਇੱਕ object ਵਾਪਸ ਕਰਦਾ ਹੈ। ਗਲਤ ਫ਼ਾਰਮੈਟ ਗੈਰ-ਜ਼ੀਰੋ ਕੋਡ ਨਾਲ ਮੁੱਕਦਾ ਹੈ। ਟੈਸਟ ਖਾਲੀ ਇਨਪੁੱਟ ਅਤੇ string `status` ਤੋਂ ਬਿਨਾਂ ਕੰਮ ਨੂੰ ਵੀ ਜਾਂਚਦੇ ਹਨ। ਇਨ੍ਹਾਂ ਕੇਸਾਂ ਦੀ ਗਲਤੀ ਆਉਟਪੁੱਟ ਅਤੇ exit code ਪੜ੍ਹੋ।

| ਜਾਂਚ | ਸਫ਼ਲਤਾ ਦਾ ਸਬੂਤ | ਨਾਕਾਮੀ ਤੋਂ ਬਹਾਲੀ |
|---|---|---|
| **ਪ੍ਰੋਜੈਕਟ ਸੰਖੇਪ** | ਯਾਦ-ਦਿਹਾਨੀ ਵਿੱਚ 7 ਵਜੇ ਹਨ | ਸਮਾਂ-ਸੂਚੀ ਸਰੋਤ ਤਾਜ਼ਾ ਕਰੋ |
| **ਰਿਪੋਜ਼ਟਰੀ ਨਕਸ਼ਾ** | ਲੋੜ ਅਤੇ ਟੈਸਟ ਪਾਥ ਦੱਸੇ | ਹਦਾਇਤੀ ਫ਼ਾਈਲਾਂ ਠੀਕ ਕਰੋ |
| **ਬਾਹਰੀ ਸਰੋਤ** | MCP ਪੜ੍ਹਿਆ ਜਾਂ ਬ੍ਰਾਊਜ਼ਰ ਵਿਕਲਪ ਦਰਜ ਕੀਤਾ | ਕੁਨੈਕਸ਼ਨ ਜਾਂ URL ਜਾਂਚੋ |
| **Worker ਸਮੀਖਿਆ** | ਗੁੰਮ ਟੈਸਟ ਫ਼ਾਈਲ ਵਿੱਚ ਪੱਕੇ ਕੀਤੇ | Worker ਰਿਪੋਰਟ ਠੀਕ ਕਰੋ |
| **ਫ਼ਾਈਲ ਸੀਮਾ** | ਸਿਰਫ਼ ਪ੍ਰੋਗਰਾਮ ਅਤੇ ਟੈਸਟ | ਹਰ ਗੈਰ-ਚਾਹੀ ਸੋਧ ਵੇਖੋ |
| **ਵਿਹਾਰ** | text, JSON, ਖਾਲੀ ਅਤੇ ਗਲਤ ਇਨਪੁੱਟ ਜਾਂਚੇ | ਕਾਰਨ ਲੱਭ ਕੇ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ |
| **ਹਵਾਲਾ** | ਨਵਾਂ ਸੈਸ਼ਨ ਸਥਿਤੀ ਬਣਾਉਂਦਾ ਹੈ | ਗੁੰਮ ਸਰੋਤ ਜਾਂ ਨਤੀਜਾ ਜੋੜੋ |

**ਸੁਰੱਖਿਅਤ reset ਲਈ ਨਵੀਂ extraction ਵਰਤੋ।** ਨੋਟਾਂ ਲੈਬ ਤੋਂ ਬਾਹਰ ਸੰਭਾਲੋ, ਸਿਰਫ਼ ਅਸਥਾਈ ਨਕਲ ਹਟਾਓ ਅਤੇ ਮੂਲ ZIP ਮੁੜ extract ਕਰੋ। ਜਿਸ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਕੰਮ ਰੱਖਣਾ ਹੈ, ਉਸ ਵਿੱਚ ਵੱਡਾ Git reset ਨਾ ਕਰੋ।

## ਜਾਂਚ 7: ਨਵੇਂ ਸੈਸ਼ਨ ਨੂੰ ਹਵਾਲਾ

ਲੈਬ ਫੋਲਡਰ ਤੋਂ ਬਾਹਰ **180 ਸ਼ਬਦਾਂ ਤੋਂ ਛੋਟਾ ਹਵਾਲਾ ਲਿਖੋ**। ਲੋੜ ਦੀ revision, ਬਦਲੀਆਂ ਫ਼ਾਈਲਾਂ, ਸਹੀ ਟੈਸਟ ਹੁਕਮ ਅਤੇ ਨਤੀਜਾ, text ਅਤੇ JSON ਆਉਟਪੁੱਟ, ਗਲਤ ਇਨਪੁੱਟ ਜਾਂਚਾਂ, ਵਰਤੋਂ ਰਿਕਾਰਡ ਅਤੇ ਬਾਕੀ ਕਦਮ ਦੱਸੋ। ਨਵਾਂ ਸੈਸ਼ਨ ਖੋਲ੍ਹੋ ਅਤੇ JSON keys ਅਤੇ ਫੀਚਰ ਦੀ ਪਾਸ ਸਥਿਤੀ ਪੁੱਛੋ।

**ਉਮੀਦ ਕੀਤਾ ਜਵਾਬ:** ਨਵਾਂ ਸੈਸ਼ਨ `total` ਅਤੇ `by_status` ਦੱਸਦਾ ਹੈ, revision 1 ਦਾ ਹਵਾਲਾ ਦਿੰਦਾ ਹੈ, ਸਿਰਫ਼ ਦੇਖੀਆਂ ਜਾਂਚਾਂ ਦੀ ਰਿਪੋਰਟ ਕਰਦਾ ਹੈ ਅਤੇ ਗੁੰਮ ਜਾਂਚ ਦੱਸਦਾ ਹੈ।

## ਉੱਤਰ-ਕੁੰਜੀ ਅਤੇ ਮਾਪਦੰਡ

**ਇੱਕ ਠੀਕ implementation** ਹੇਠਾਂ ਹੈ। ਪਹਿਲਾ block `task_report.py` ਅਤੇ ਦੂਜਾ `tests/test_task_report.py` ਵਜੋਂ ਲੈਬ ਦੀ ਨਵੀਂ extraction ਵਿੱਚ ਸੰਭਾਲੋ। `tasks.json` ਅਤੇ ਦੋਵੇਂ requirement ਫ਼ਾਈਲਾਂ ਨਾ ਬਦਲੋ। ਜਾਂਚ 6 ਦੇ ਕਦਮ ਚਲਾਓ। ਹੋਰ ਹੱਲ ਨੂੰ ਲੋੜ ਅਤੇ ਦੇਖੇ ਵਿਹਾਰ ਨਾਲ ਮਿਲਾਓ।

`task_report.py`:

```python
"""ਵਰਕਸ਼ਾਪ ਕੰਮਾਂ ਦੀ text ਗਿਣਤੀ ਜਾਂ JSON ਸਾਰ ਛਾਪਦਾ ਹੈ।"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="ਵਰਕਸ਼ਾਪ ਕੰਮਾਂ ਦੀ ਰਿਪੋਰਟ")
    parser.add_argument("path", type=Path, help="JSON ਕੰਮ ਸੂਚੀ ਦਾ ਪਾਥ")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""ਵਰਕਸ਼ਾਪ ਕੰਮਾਂ ਦੀ text ਅਤੇ JSON ਰਿਪੋਰਟ ਜਾਂਚ।"""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**ਕੁੰਜੀ ਵਰਤਣ ਤੋਂ ਬਾਅਦ reset ਕਰੋ:** ਨੋਟਾਂ ਲੈਬ ਤੋਂ ਬਾਹਰ ਸੰਭਾਲੋ, ਇਹ ਨਕਲ ਹਟਾਓ ਅਤੇ ਮੂਲ ਸਟਾਰਟਰ ਲੈਬ ਮੁੜ extract ਕਰੋ। ਨਵੀਂ ਨਕਲ ਵਿੱਚ ਦੋ ਬੇਸਲਾਈਨ ਟੈਸਟ ਹਨ ਅਤੇ ਫੀਚਰ implementation ਨਹੀਂ।

**ਉੱਪਰਲੀ ਸਾਰਣੀ ਦੇ ਹਰ ਜਾਂਚ ਲਈ ਇੱਕ ਅੰਕ ਦਿਓ।** ਜੁੜਿਆ ਰਾਹ ਸੱਤ ਅੰਕਾਂ ’ਤੇ ਪੂਰਾ ਹੈ ਜੇ ਬਾਹਰੀ ਸਰੋਤ ਵਾਲੀ ਕਤਾਰ ਵਿੱਚ ਅਸਲ MCP ਕਾਲ ਅਤੇ worker ਵਾਲੀ ਕਤਾਰ ਵਿੱਚ ਅਸਲ ਸੈਸ਼ਨ ਦਰਜ ਹੈ। ਅਧਿਐਨ ਰਾਹ ਸੱਤ ਅੰਕਾਂ ’ਤੇ ਪੂਰਾ ਹੈ ਜੇ ਸਰੋਤ ਜਾਂਚਿਆ ਬ੍ਰਾਊਜ਼ਰ ਪੰਨਾ ਹੈ ਅਤੇ ਟੂਲ ਕਦਮ ਸਪਸ਼ਟ ਤੌਰ ’ਤੇ ਨਹੀਂ ਚਲਾਏ ਗਏ ਲਿਖੇ ਹਨ। ਵਿਹਾਰ, ਸਰੋਤ ਜਾਂ ਫ਼ਾਈਲ ਸੀਮਾ ਦੀ ਗੁੰਮ ਜਾਂਚ ਦੋਵੇਂ ਰਾਹ ਰੋਕਦੀ ਹੈ।

## ਆਪਣੀ ਸਮਝ ਜਾਂਚੋ

1. **ਇਸ ਫੀਚਰ ਨੂੰ ਕਿਹੜੀ ਲੋੜ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ?** `docs/capstone-requirements.md`, revision 1। ਪੁਰਾਣੀ ਸਟੇਟਸ-ਫ਼ਿਲਟਰ ਲੋੜ ਪਾਠ 5 ਨਾਲ ਸਬੰਧਤ ਹੈ।
2. **JSON ਕਰਾਰ ਦਾ ਸਬੂਤ ਕੀ ਹੈ?** ਹੁਕਮ ਦਾ ਨਤੀਜਾ ਪੜ੍ਹੋ, ਅੰਕੀ ਮੁੱਲ ਅਤੇ ਹਰ ਸਟੇਟਸ ਦੀ ਗਿਣਤੀ ਮਿਲਾਓ ਅਤੇ ਖਾਲੀ ਤੇ ਗਲਤ ਇਨਪੁੱਟ ਜਾਂਚੋ। ਸੁੰਦਰ agent summary ਕਾਫ਼ੀ ਨਹੀਂ।

## ਸਮੱਸਿਆ ਹੱਲ

- **ਸੋਧ ਤੋਂ ਪਹਿਲਾਂ ਬੇਸਲਾਈਨ ਫੇਲ੍ਹ:** ZIP ਤੋਂ ਲੈਬ ਰੀਸੈੱਟ ਕਰੋ ਅਤੇ ਸੈਟਅੱਪ ਦੁਹਰਾਓ।
- **ਏਜੰਟ ਹੋਰ ਫ਼ਾਈਲ ਬਦਲੇ:** diff ਵੇਖੋ ਅਤੇ ਸਿਰਫ਼ ਅਣਚਾਹੀ ਲੈਬ ਸੋਧ ਵਾਪਸ ਕਰੋ।
- **MCP ਕੁਨੈਕਸ਼ਨ ਫੇਲ੍ਹ:** ਬ੍ਰਾਊਜ਼ਰ ਸਰੋਤ ਵਰਤੋ ਅਤੇ ਜਾਂਚ ਨੂੰ ਅਧਿਐਨ ਰਾਹ ਲਿਖੋ।
- **Worker ਗਲਤ ਮੁੱਲ ਦਹੁਰਾਏ:** ਕੈਪਸਟੋਨ ਲੋੜ ਮੁੜ ਪੜ੍ਹੋ ਅਤੇ ਰਿਪੋਰਟ ਠੀਕ ਕਰੋ।
- **ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ਾਂ ਮੁੱਕਣ:** ਗਲਤੀ ਰਿਕਾਰਡ ਸੰਭਾਲੋ ਅਤੇ ਅਗਲੇ ਕਦਮ ਲਈ ਮਨੁੱਖੀ ਸਮੀਖਿਅਕ ਤੋਂ ਪੁੱਛੋ।

## ਅਗਲੇ ਕਦਮ

**ਪੂਰਾ ਸਬੂਤ ਰਿਕਾਰਡ ਸੰਭਾਲੋ।** ਉੱਨਤ ਟੀਮ ਪ੍ਰਕਾਸ਼ਨ ਅਤੇ ਕਈ ਸਿਸਟਮਾਂ ਵਿੱਚ ਅਧਿਕਾਰ ਲਈ [AI ਸਹਿਯੋਗ ਲਾਗੂਕਰਨ ਕੋਰਸ](/ai-collaboration-course-start/) ਜਾਰੀ ਰੱਖੋ।

**ਕੋਰਸ ਨੈਵੀਗੇਸ਼ਨ:** [ਪਿਛਲਾ ਲਾਜ਼ਮੀ ਪਾਠ: ਸੀਮਿਤ ਚੱਕਰ](/articles/effective-ai-bounded-agent-loops/), [ਵਿਕਲਪਿਕ: ਵਿਸ਼ੇਸ਼ ਏਜੰਟ ਮੁਲਾਂਕਣ](/articles/effective-ai-specialized-agent-evaluation/), [ਕੋਰਸ ਰੂਪਰੇਖਾ](/effective-ai-course-start/).
