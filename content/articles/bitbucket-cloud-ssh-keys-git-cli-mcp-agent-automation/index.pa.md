---
title: "Bitbucket Cloud SSH ਕੁੰਜੀਆਂ: AI ਏਜੰਟਾਂ ਲਈ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੀ Git ਪਹੁੰਚ"
date: 2026-10-11
lastmod: 2026-11-13
toc: true
draft: false
description: "ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੇ AI ਏਜੰਟ ਵਰਕਫਲੋ ਲਈ Bitbucket Cloud SSH ਕੁੰਜੀਆਂ, Git CLI ਪਹੁੰਚ, REST API ਟੋਕਨ, 1Password ਅਤੇ MCP ਟੂਲ ਸੈੱਟ ਕਰੋ।"
genre: ["ਕਲਾਉਡ ਸੁਰੱਖਿਆ", "ਡਿਵੈਲਪਰ ਟੂਲ", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ"]
tags: ["Bitbucket Cloud", "Bitbucket SSH ਕੁੰਜੀਆਂ", "ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ ਕੁੰਜੀਆਂ", "ਪ੍ਰੋਜੈਕਟ ਪਹੁੰਚ ਕੁੰਜੀਆਂ", "ਵਰਕਸਪੇਸ ਪਹੁੰਚ ਕੁੰਜੀਆਂ", "Git CLI", "Bitbucket CLI", "1Password CLI", "1Password SSH Agent", "MCP", "Model Context Protocol", "REST API", "API ਟੋਕਨ ਸਕੋਪ", "ਏਜੰਟ ਅਧਿਕਾਰ", "ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ ਆਟੋਮੇਸ਼ਨ", "SSH ਹੋਸਟ ਕੁੰਜੀਆਂ"]
cover: "/img/cover/bitbucket-cloud-ssh-keys-git-cli-mcp-agent-automation.webp"
coverAlt: "ਟਰਮੀਨਲ ਵਰਕਫਲੋ Bitbucket Cloud Git ਪਹੁੰਚ, ਸੀਮਿਤ-ਸਕੋਪ SSH ਕੁੰਜੀਆਂ, 1Password, REST API ਪੜ੍ਹਨ ਅਤੇ MCP ਟੂਲ ਜੋੜਦਾ ਹੈ"
coverCaption: ""
---

**ਸੀਮਿਤ ਏਜੰਟ ਵਰਕਫਲੋ ਰਿਪੋਜ਼ਟਰੀ ਪੜ੍ਹਨ, API ਪੜ੍ਹਨ, ਰਾਜ਼ਾਂ ਦੀ ਸੰਭਾਲ ਅਤੇ ਦੂਰਲੇ ਲਿਖਣ ਨੂੰ ਵੱਖ ਕਰਦਾ ਹੈ।** ਸਰੋਤ ਤੱਕ ਪਹੁੰਚ ਲਈ Secure Shell (SSH) ਉੱਤੇ Git ਵਰਤੋ, ਆਟੋਮੈਟਿਕ checkout ਲਈ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੀ Bitbucket ਪਹੁੰਚ ਕੁੰਜੀ, ਮੈਟਾਡਾਟਾ ਲਈ REST API ਅਤੇ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਟੂਲਾਂ ਲਈ Model Context Protocol (MCP) ਸਰਵਰ ਵਰਤੋ। ਨਿੱਜੀ ਕੁੰਜੀਆਂ ਅਤੇ API ਟੋਕਨ 1Password ਵਿੱਚ ਰੱਖੋ। ਲਿਖਣ ਤੋਂ ਪਹਿਲਾਂ ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਲਵੋ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਮੂਲ ਰੂਪ ਵਿੱਚ ਸਿਰਫ਼ ਪੜ੍ਹਨ:** ਏਜੰਟ checkout ਲਈ ਰਿਪੋਜ਼ਟਰੀ ਜਾਂ ਪ੍ਰੋਜੈਕਟ ਪਹੁੰਚ ਕੁੰਜੀ ਵਰਤੋ। ਦੋਵਾਂ ਵਿੱਚੋਂ ਕੋਈ ਵੀ push ਪਹੁੰਚ ਨਹੀਂ ਦਿੰਦੀ।
- **ਨਿੱਜੀ ਪਛਾਣ:** ਵਰਤੋਂਕਾਰ ਖਾਤੇ ਨਾਲ ਜੁੜੇ ਇੰਟਰਐਕਟਿਵ ਕੰਮ ਲਈ ਨਿੱਜੀ SSH ਕੁੰਜੀ ਵਰਤੋ।
- **ਰਾਜ਼ਾਂ ਦੀ ਹਿਫ਼ਾਜ਼ਤ:** 1Password SSH Agent ਵਰਤੋ ਤਾਂ ਜੋ Git ਨਿੱਜੀ ਕੁੰਜੀ ਪੜ੍ਹੇ ਬਿਨਾਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਦਸਤਖ਼ਤ ਕਰ ਸਕੇ।
- **CLI ਦਾ ਮਤਲਬ:** `git`, `curl` ਅਤੇ ਛੋਟੇ ਜਾਂਚੇ ਹੋਏ API wrapper ਨੂੰ ਵਰਤੋਂਯੋਗ Bitbucket ਕਮਾਂਡ ਲਾਈਨ ਮੰਨੋ।
- **MCP ਸੀਮਾ:** ਘੱਟ-ਦਾਇਰੇ ਵਾਲੇ ਪੜ੍ਹਨ ਟੂਲ ਦਿਓ। ਲਿਖਣ ਵਾਲੇ ਟੂਲ ਬੰਦ ਰੱਖੋ ਜਾਂ ਵੱਖਰੀ ਮਨਜ਼ੂਰੀ ਪ੍ਰਕਿਰਿਆ ਪਿੱਛੇ ਰੱਖੋ।
- **ਲਿਖਣ ਦੀ ਮਨਜ਼ੂਰੀ:** ਏਜੰਟ ਨੂੰ ਜਾਂਚ, ਤੁਲਨਾ ਅਤੇ ਤਬਦੀਲੀ ਤਿਆਰ ਕਰਨ ਦਿਓ। push, pull request, merge ਜਾਂ ਸੈਟਿੰਗ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਮਨੁੱਖ ਤੋਂ ਮਨਜ਼ੂਰੀ ਲਵੋ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

**ਲੋੜੀਂਦੀਆਂ ਚੀਜ਼ਾਂ:** Bitbucket Cloud ਪਹੁੰਚ, Git, OpenSSH ਕਲਾਇੰਟ, 1Password 8, 1Password CLI, ਸਾਈਨ ਇਨ ਕੀਤਾ CLI ਜਾਂ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਸੇਵਾ ਖਾਤਾ ਅਤੇ ਸਰਵਰ ਮਨਜ਼ੂਰੀ ਕੰਟਰੋਲ ਵਾਲਾ MCP ਹੋਸਟ। 45 ਮਿੰਟ ਰੱਖੋ। ਔਖਾਈ ਦਰਮਿਆਨੀ ਹੈ।

ਪਹਿਲੀ ਵਾਰ ਲਈ ਟੈਸਟ ਰਿਪੋਜ਼ਟਰੀ ਵਰਤੋ। ਉਦਾਹਰਣਾਂ ਦੇ ਸਾਰੇ placeholder ਬਦਲੋ। ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਕਮਾਂਡਾਂ ਬਿਨਾਂ ਜਾਂਚੇ ਉਦਾਹਰਣ ਹਨ। ਇਹ ਕਿਸੇ ਸਰਗਰਮ Bitbucket ਖਾਤੇ ਜਾਂ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਨਹੀਂ ਦਰਸਾਉਂਦੀਆਂ।

**ਵਰਜਨ:** ਇਹ ਲੇਖ ਡਿਜ਼ਾਈਨ ਬਾਰੇ ਸਲਾਹ ਹੈ, ਵਰਜਨ ਨਾਲ ਬੱਝੀ ਰਨਬੁੱਕ ਨਹੀਂ। ਜਾਂਚ ਤੋਂ ਪਹਿਲਾਂ ਸਥਾਪਿਤ Git, OpenSSH, 1Password CLI, Teamwork Graph CLI, MCP ਹੋਸਟ ਅਤੇ MCP ਸਰਵਰ ਦੇ ਵਰਜਨ ਪੁਸ਼ਟੀ ਕਰੋ। `ssh-add -l` ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਮੌਜੂਦਾ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਲਈ 1Password SSH Agent ਸੈੱਟ ਕਰੋ।

**ਪਛਾਣ-ਜਾਣਕਾਰੀ shell, ਲੌਗ, URL, Git ਰਿਮੋਟ ਜਾਂ ਸਰੋਤ ਫਾਈਲਾਂ ਵਿੱਚ ਨਾ ਰੱਖੋ।** `<workspace>`, `<repository>`, `<api-token>` ਅਤੇ `<socket-path>` ਵਰਗੇ placeholder ਵਰਤੋ। ਟਰਮੀਨਲ ਰਿਕਾਰਡ ਵਿੱਚ ਅਸਲੀ ਨਿੱਜੀ ਕੁੰਜੀ ਨਾ ਪੇਸਟ ਕਰੋ।

## ਪਹੁੰਚ ਦੀ ਹੱਦ ਚੁਣੋ

Bitbucket Cloud ਰਿਪੋਜ਼ਟਰੀ, ਪ੍ਰੋਜੈਕਟ ਅਤੇ ਵਰਕਸਪੇਸ ਪੱਧਰ ਉੱਤੇ ਪਹੁੰਚ ਕੁੰਜੀਆਂ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ। ਕਾਪੀ ਹੋਈ ਕੁੰਜੀ ਦਾ ਅਸਰ ਉਸਦਾ ਦਾਇਰਾ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ। [ਪਹੁੰਚ ਕੁੰਜੀਆਂ ਦੀ ਅਧਿਕਾਰਤ ਤੁਲਨਾ](https://support.atlassian.com/bitbucket-cloud/kb/difference-between-repository-project-and-workspace-access-keys/) ਇਜਾਜ਼ਤਾਂ ਦਾ ਫ਼ਰਕ ਸਿੱਧਾ ਦੱਸਦੀ ਹੈ।

| ਪਹੁੰਚ ਦਾ ਰਸਤਾ | ਦਾਇਰਾ | ਲਿਖਣ ਦੀ ਸਮਰੱਥਾ | ਢੁੱਕਵੀਂ ਵਰਤੋਂ |
|---|---|---:|---|
| **ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ ਕੁੰਜੀ** | ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ | ਨਹੀਂ | ਏਜੰਟ ਲਈ ਮੂਲ checkout |
| **ਪ੍ਰੋਜੈਕਟ ਪਹੁੰਚ ਕੁੰਜੀ** | ਇੱਕ ਪ੍ਰੋਜੈਕਟ ਦੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ | ਨਹੀਂ | ਛੋਟੇ ਰਿਪੋਜ਼ਟਰੀ ਸਮੂਹ ਉੱਤੇ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੇ ਕੰਮ |
| **ਵਰਕਸਪੇਸ ਪਹੁੰਚ ਕੁੰਜੀ** | ਇੱਕ ਵਰਕਸਪੇਸ ਦੀਆਂ ਰਿਪੋਜ਼ਟਰੀਆਂ | ਹਾਂ | ਵੱਖਰੀ ਲਿਖਣ ਯੋਜਨਾ ਵਾਲਾ ਨਿਯੰਤਰਿਤ ਸੇਵਾ ਆਟੋਮੇਸ਼ਨ |
| **ਨਿੱਜੀ SSH ਕੁੰਜੀ** | ਇੱਕ ਵਰਤੋਂਕਾਰ ਨੂੰ ਮਨਜ਼ੂਰ ਰਿਪੋਜ਼ਟਰੀਆਂ | ਵਰਤੋਂਕਾਰ ਖਾਤੇ ਅਨੁਸਾਰ | ਇੰਟਰਐਕਟਿਵ ਪ੍ਰਸ਼ਾਸਨ |
| **API ਟੋਕਨ** | ਵਰਤੋਂਕਾਰ-ਅਧਾਰਿਤ API ਸਕੋਪ ਅਤੇ ਖਾਤਾ ਪਹੁੰਚ | ਸਕੋਪਾਂ ਉੱਤੇ ਨਿਰਭਰ | REST API ਪੜ੍ਹਨ ਜਾਂ ਥੋੜ੍ਹੇ ਸਮੇਂ ਦਾ ਲਿਖਣ ਕੰਮ |

**ਸਭ ਤੋਂ ਛੋਟੀ ਲਾਭਦਾਇਕ ਹੱਦ ਤੋਂ ਸ਼ੁਰੂ ਕਰੋ।** ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਕਾਫ਼ੀ ਹੋਵੇ ਤਾਂ ਰਿਪੋਜ਼ਟਰੀ ਕੁੰਜੀ ਚੁਣੋ। ਕਈ ਰਿਪੋਜ਼ਟਰੀਆਂ ਇੱਕ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਹੋਣ ਅਤੇ ਸਿਰਫ਼ ਪੜ੍ਹਨਾ ਕਾਫ਼ੀ ਹੋਵੇ ਤਾਂ ਪ੍ਰੋਜੈਕਟ ਕੁੰਜੀ ਚੁਣੋ। ਵਰਕਸਪੇਸ ਕੁੰਜੀ ਨੂੰ ਲਿਖਣ ਵਾਲੀ ਪਛਾਣ ਮੰਨੋ, ਸੁਵਿਧਾਜਨਕ ਮੂਲ ਚੋਣ ਨਹੀਂ।

Bitbucket ਸੈਟਿੰਗਾਂ ਦੇ ਢੁੱਕਵੇਂ ਰਸਤੇ ਰਾਹੀਂ ਸਭ ਤੋਂ ਘੱਟ ਅਧਿਕਾਰ ਵਾਲੀ ਕੁੰਜੀ ਬਣਾਓ ਅਤੇ ਦਰਜ ਕਰੋ:

1. ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਲਈ Repository settings, Access keys ਅਤੇ Add key ਖੋਲ੍ਹੋ। ਜਨਤਕ ਕੁੰਜੀ ਪੇਸਟ ਕਰੋ ਅਤੇ ਕੁੰਜੀ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਲਈ ਰੱਖੋ।
2. ਕਈ ਰਿਪੋਜ਼ਟਰੀਆਂ ਨੂੰ ਪ੍ਰੋਜੈਕਟ-ਸੀਮਿਤ ਪੜ੍ਹਨ ਪਛਾਣ ਚਾਹੀਦੀ ਹੋਵੇ ਤਾਂ Project settings, Access keys ਅਤੇ Add key ਖੋਲ੍ਹੋ।
3. ਵਰਕਸਪੇਸ ਪਹੁੰਚ ਕੁੰਜੀ ਸਿਰਫ਼ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਲਿਖਣ ਡਿਜ਼ਾਈਨ ਵਾਲੇ ਸਾਂਝੇ ਵਰਕਸਪੇਸ ਵਿੱਚ ਵਰਤੋ। ਨਿੱਜੀ ਵਰਕਸਪੇਸ ਵਿੱਚ ਇਹੋ ਜਿਹਾ ਵਰਕਸਪੇਸ-ਪੱਧਰੀ ਰਸਤਾ ਨਹੀਂ ਹੁੰਦਾ।
4. ਕੁੰਜੀ ਦਾ ਲੇਬਲ, ਦਾਇਰਾ, ਜਨਤਕ ਕੁੰਜੀ ਦਾ fingerprint, ਮਾਲਕ ਅਤੇ ਬਦਲਣ ਦੀ ਮਿਤੀ ਦਰਜ ਕਰੋ। ਨਿੱਜੀ ਕੁੰਜੀ 1Password ਵਿੱਚ ਰੱਖੋ।

ਦਰਜ ਕਰਨ ਤੋਂ ਬਾਅਦ ਇੱਕ ਸਟੀਕ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ ਕਨੈਕਸ਼ਨ ਟੈਸਟ ਚਲਾਓ:

```bash
git ls-remote git@bitbucket.org:<workspace>/<repository>.git HEAD
```

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** `HEAD` ਲਈ ਇੱਕ commit reference। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। ਸਫਲ ਨਤੀਜਾ ਸਾਬਤ ਕਰਦਾ ਹੈ ਕਿ ਇੱਕ ਮਨਜ਼ੂਰ SSH ਪਛਾਣ ਦਿੱਤੀ ਰਿਪੋਜ਼ਟਰੀ ਤੱਕ ਪਹੁੰਚੀ। ਇਹ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ ਕਿ ਦਰਜ ਕੀਤੀ ਕੁੰਜੀ ਚੁਣੀ ਗਈ ਜਾਂ ਲਿਖਣ ਪਹੁੰਚ ਹੈ। ਹਰ ਰਿਪੋਜ਼ਟਰੀ ਲਈ ਇੱਕ ਕੁੰਜੀ ਵਾਲੀ ਸੈਟਿੰਗ ਤੋਂ ਬਾਅਦ ਟੈਸਟ ਮੁੜ ਚਲਾਓ।

ਨਿੱਜੀ ਕੁੰਜੀ ਦੀ ਹਿਫ਼ਾਜ਼ਤ ਅਤੇ 1Password SSH Agent ਦੀ ਮਨਜ਼ੂਰੀ ਲਈ [1Password CLI ਅਤੇ SSH Agent: AI ਏਜੰਟਾਂ ਲਈ ਸੁਰੱਖਿਅਤ SSH ਕੁੰਜੀਆਂ](/articles/1password-cli-ssh-keys-mcp-agent-administration/) ਵੇਖੋ।

## “Bitbucket CLI” ਨੂੰ ਠੀਕ ਤਰ੍ਹਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ

**Bitbucket CLI** ਸ਼ਬਦ ਅਕਸਰ ਤਿੰਨ ਵੱਖਰੇ ਇੰਟਰਫੇਸਾਂ ਨੂੰ ਮਿਲਾ ਦਿੰਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਨੂੰ ਵੱਖ ਰੱਖੋ।

- **Git CLI:** `git clone` ਅਤੇ `git fetch` SSH ਜਾਂ HTTPS ਰਾਹੀਂ ਰਿਪੋਜ਼ਟਰੀ ਡਾਟਾ ਲਿਜਾਂਦੇ ਹਨ। `git diff` ਸਥਾਨਕ ਫਾਈਲਾਂ ਜਾਂ revisions ਦੀ ਤੁਲਨਾ ਕਰਦਾ ਹੈ।
- **REST ਕਲਾਇੰਟ:** `curl` ਜਾਂ ਜਾਂਚਿਆ wrapper Bitbucket Cloud Representational State Transfer (REST) API ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ। API ਡਾਟਾ ਜਾਂ ਕਾਰਵਾਈ ਮੰਗਣ ਲਈ ਪ੍ਰੋਗਰਾਮੀ ਇੰਟਰਫੇਸ ਹੈ। [Bitbucket Cloud REST API ਹਵਾਲਾ](https://developer.atlassian.com/cloud/bitbucket/rest/) ਰਿਪੋਜ਼ਟਰੀ, ਸਰੋਤ, branch, pull request, pipeline ਅਤੇ status ਸਰੋਤ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ।
- **Atlassian CLI:** `acli` Atlassian ਦੀ ਅਧਿਕਾਰਤ ਕਮਾਂਡ ਲਾਈਨ ਹੈ। ਇਸਦੀ [ਜਾਣ-ਪਛਾਣ](https://developer.atlassian.com/cloud/acli/guides/introduction/) ਉਤਪਾਦ ਦੱਸਦੀ ਹੈ, ਜਦਕਿ ਇਸਦਾ [ਕਮਾਂਡ ਹਵਾਲਾ](https://developer.atlassian.com/cloud/acli/reference/commands/) `admin`, `jira`, `feedback` ਅਤੇ `rovodev` ਪਾਸੇ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ। ਹਵਾਲਾ Bitbucket Cloud ਕਮਾਂਡਾਂ ਨਹੀਂ ਦੱਸਦਾ।

**Atlassian ਦਾ ਅਧਿਕਾਰਤ `acli` ਕਮਾਂਡ ਹਵਾਲਾ Bitbucket Cloud ਕਮਾਂਡਾਂ ਨਹੀਂ ਦੱਸਦਾ।** `acli bitbucket clone` ਵਰਗੀ ਕਮਾਂਡ ਨਾ ਘੜੋ। Git ਕਾਰਵਾਈਆਂ ਲਈ Git ਅਤੇ Bitbucket Cloud ਡਾਟੇ ਲਈ REST API ਵਰਤੋ।

### ਵਿਕਲਪਕ Teamwork Graph CLI

**Atlassian Teamwork Graph CLI, ਜਾਂ `twg`, ਵੀ ਪ੍ਰਕਾਸ਼ਿਤ ਕਰਦਾ ਹੈ।** ਇਸਦੀ [ਜਾਣ-ਪਛਾਣ](https://developer.atlassian.com/cloud/twg-cli/) ਅਤੇ [ਕਮਾਂਡ ਕੈਟਾਲੌਗ](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/commands/commands-catalog/) Bitbucket ਕਮਾਂਡ ਪਰਿਵਾਰ ਦਰਜ ਕਰਦੇ ਹਨ। ਸੈੱਟਅੱਪ ਕਮਾਂਡ ਹੈ:

```bash
twg setup
```

ਸੈੱਟਅੱਪ ਕਮਾਂਡ ਸਥਾਨਕ ਪ੍ਰਮਾਣੀਕਰਨ ਹਾਲਤ ਬਦਲਦੀ ਹੈ। ਵਿਕਲਪਕ Bitbucket ਟੋਕਨ ਸੈਟਿੰਗ ਲਈ ਸਥਾਪਿਤ ਵਰਜਨ ਦੇ prompts ਮੰਨੋ। CLI ਦਾ Bitbucket ਟੋਕਨ ਰਸਤਾ Atlassian OAuth ਤੋਂ ਵੱਖਰਾ ਹੈ। ਸਹੀ ਕਮਾਂਡ syntax ਸਥਾਪਿਤ ਵਰਜਨ ਅਤੇ ਮੌਜੂਦਾ ਕੈਟਾਲੌਗ ਨਾਲ ਮਿਲਾਓ। ਬਦਲਾਅ ਕਰਨ ਵਾਲੀਆਂ ਕਮਾਂਡਾਂ ਲਈ ਵੱਖਰਾ profile, ਸੀਮਿਤ ਟੋਕਨ, ਜਾਂਚੇ ਹੋਏ ਸਥਾਪਿਤ ਹੁਨਰ ਅਤੇ ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਵਰਤੋ।

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ, ਬਿਨਾਂ ਜਾਂਚਿਆ:** ਅਲੱਗ profile ਨੂੰ Bitbucket ਪ੍ਰਮਾਣੀਕਰਨ ਸੈਟਿੰਗ ਮਿਲਦੀ ਹੈ। ਸੈੱਟਅੱਪ ਤੋਂ ਪਹਿਲਾਂ profile ਦੀ ਪੁਰਾਣੀ ਹਾਲਤ ਲਿਖੋ। rollback ਵੇਲੇ ਸਥਾਪਿਤ ਵਰਜਨ ਦੀ ਦਰਜ logout ਜਾਂ configuration ਹਟਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨਾਲ ਸੁਰੱਖਿਅਤ credential ਹਟਾਓ।

ਜੇ ਤੀਜੀ ਧਿਰ ਦਾ ਪ੍ਰੋਜੈਕਟ ਆਪਣੇ ਆਪ ਨੂੰ Bitbucket CLI ਕਹੇ, ਤਾਂ ਇਸਦਾ ਸਰੋਤ, release ਪ੍ਰਕਿਰਿਆ, checksums, update ਰਸਤਾ, ਪ੍ਰਮਾਣੀਕਰਨ ਤਰੀਕਾ, ਮੰਗੇ ਸਕੋਪ, ਨੈੱਟਵਰਕ ਮੰਜ਼ਿਲਾਂ, ਲੌਗ ਸੰਭਾਲ ਅਤੇ ਲਿਖਣ ਕਮਾਂਡਾਂ ਜਾਂਚੋ। ਜਾਣਿਆ-ਪਛਾਣਿਆ binary ਨਾਮ vendor support ਜਾਂ ਸੁਰੱਖਿਅਤ ਅਧਿਕਾਰ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

## SSH ਕੁੰਜੀਆਂ 1Password ਦੇ ਨਿਯੰਤਰਣ ਹੇਠ ਰੱਖੋ

[1Password SSH Agent](https://www.1password.dev/ssh/agent) 1Password ਵਿੱਚ ਸੰਭਾਲੀਆਂ SSH ਕੁੰਜੀਆਂ Git ਅਤੇ SSH ਕਲਾਇੰਟਾਂ ਨੂੰ ਦਿੰਦਾ ਹੈ। ਕਲਾਇੰਟ ਮਨਜ਼ੂਰਸ਼ੁਦਾ ਦਸਤਖ਼ਤ ਦੀ ਬੇਨਤੀ ਕਰਦਾ ਹੈ। ਨਿੱਜੀ ਕੁੰਜੀ 1Password ਐਪ ਦੇ ਅੰਦਰ ਰਹਿੰਦੀ ਹੈ ਅਤੇ ਮਨਜ਼ੂਰ ਕਲਾਇੰਟ ਦੇ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ 1Password ਸਹਿਮਤੀ ਮੰਗਦਾ ਹੈ।

[1Password CLI ਹਵਾਲਾ](https://www.1password.dev/cli/reference) ਦਾ ਕੰਮ ਵੱਖਰਾ ਹੈ। item, API ਟੋਕਨ, ਸੇਵਾ ਖਾਤਿਆਂ ਅਤੇ ਆਟੋਮੇਸ਼ਨ ਸੈੱਟਅੱਪ ਤੱਕ ਨਿਯੰਤਰਿਤ ਪਹੁੰਚ ਲਈ `op` ਵਰਤੋ। SSH signing ਲਈ SSH Agent ਵਰਤੋ। ਏਜੰਟ ਦਾ ਕੰਮ ਆਸਾਨ ਕਰਨ ਲਈ ਨਿੱਜੀ ਕੁੰਜੀ ਅਸਥਾਈ ਫਾਈਲ ਵਿੱਚ export ਨਾ ਕਰੋ।

ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੀਆਂ ਕਮਾਂਡਾਂ ਨਾਲ ਸਥਾਨਕ CLI ਅਤੇ agent ਦੀ ਹਾਲਤ ਜਾਂਚੋ:

```bash
op --version
ssh-add -l
```

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** 1Password CLI ਦਾ ਵਰਜਨ ਅਤੇ ਸਰਗਰਮ agent ਤੋਂ ਇੱਕ ਜਾਂ ਵੱਧ ਜਨਤਕ-ਕੁੰਜੀ fingerprints। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। `ssh-add -l` ਦਾ ਖਾਲੀ ਨਤੀਜਾ ਦੱਸਦਾ ਹੈ ਕਿ ਚੁਣੇ agent socket ਰਾਹੀਂ ਕੋਈ ਕੁੰਜੀ ਉਪਲਬਧ ਨਹੀਂ।

ਨਵੀਂ ਕੁੰਜੀ ਲਈ 1Password ਵਿੱਚ Ed25519 SSH Key item ਬਣਾਓ ਜਾਂ ਭਰੋਸੇਯੋਗ ਸਥਾਨਕ ਪ੍ਰਕਿਰਿਆ ਨਾਲ ਬਣੀ ਕੁੰਜੀ import ਕਰੋ। ਵਰਤੋਂ, ਦਾਇਰੇ ਅਤੇ ਬਦਲਣ ਦੀ ਮਿਤੀ ਅਨੁਸਾਰ ਲੇਬਲ ਰੱਖੋ। Bitbucket Cloud ਵਿੱਚ ਸਿਰਫ਼ ਜਨਤਕ ਕੁੰਜੀ ਜੋੜੋ। [Linux ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ-ਕੁੰਜੀ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/set-up-repository-access-keys-on-linux/) ਰਿਪੋਜ਼ਟਰੀ ਸੈਟਿੰਗ ਦਾ ਰਸਤਾ ਅਤੇ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਦੀ ਹੱਦ ਦੱਸਦੀ ਹੈ।

## ਪਹਿਲਾਂ Bitbucket host key ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ

SSH ਵਰਤੋਂਕਾਰ ਪ੍ਰਮਾਣੀਕਰਨ ਸਰਵਰ ਦੀ ਪਛਾਣ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ। ਪ੍ਰਮਾਣੀਕਰਨ ਬੇਨਤੀ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ ਕਲਾਇੰਟ ਨੂੰ Bitbucket Cloud host key ਦੀ ਪੁਸ਼ਟੀ ਕਰਨੀ ਪੈਂਦੀ ਹੈ। Atlassian ਦੀ [SSH ਅਤੇ ਦੋ-ਕਦਮੀ ਪੁਸ਼ਟੀ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/configure-ssh-and-two-step-verification/) ਜਨਤਕ host keys ਸੂਚੀਬੱਧ ਕਰਦੀ ਹੈ ਅਤੇ known-host entries ਲੈਣ ਦਾ ਅਧਿਕਾਰਤ endpoint ਦਿਖਾਉਂਦੀ ਹੈ।

ਤੁਲਨਾ ਲਈ ਜਨਤਕ host-key ਡਾਟਾ ਲਵੋ:

```bash
curl --fail --silent --show-error https://bitbucket.org/site/ssh
```

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** `bitbucket.org` ਲਈ OpenSSH `known_hosts` ਲਾਈਨਾਂ। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। `~/.ssh/known_hosts` ਵਿੱਚ ਲਾਈਨ ਪਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਵਾਪਸ ਮਿਲੀ ਕੁੰਜੀ ਜਾਂ fingerprint ਦੀ ਸੁਤੰਤਰ ਭਰੋਸੇਯੋਗ ਕਾਪੀ ਨਾਲ ਤੁਲਨਾ ਕਰੋ।

ਮਨਜ਼ੂਰ entry ਹੋਣ ਤੋਂ ਬਾਅਦ ਸਖ਼ਤ host checking ਵਰਤੋ:

```sshconfig
Host bitbucket.org
    StrictHostKeyChecking yes
    UserKnownHostsFile ~/.ssh/known_hosts
```

**ਏਜੰਟ ਚੱਲਣ ਦੌਰਾਨ ਬਦਲੀ host key ਕਬੂਲ ਨਾ ਕਰੋ।** ਚਲਾਉਣਾ ਰੋਕੋ, Bitbucket Cloud ਦਾ ਮੌਜੂਦਾ host-key ਰਿਕਾਰਡ ਜਾਂਚੋ ਅਤੇ ਸਥਾਨਕ `known_hosts` entry ਵੇਖੋ। ਆਟੋਮੈਟਿਕ ਮਨਜ਼ੂਰੀ ਕੁੰਜੀ-ਅਧਾਰਿਤ ਸੁਰੱਖਿਆ ਹੱਦ ਹਟਾ ਦਿੰਦੀ ਹੈ।

## ਹਰ ਰਿਪੋਜ਼ਟਰੀ ਲਈ ਇੱਕ ਕੁੰਜੀ ਚੁਣੋ

ਇੱਕ ਡਿਵਾਈਸ ਉੱਤੇ ਅਕਸਰ ਕਈ Bitbucket ਕੁੰਜੀਆਂ ਹੁੰਦੀਆਂ ਹਨ। ਵੱਡਾ SSH agent ਇੱਕ connection ਵਿੱਚ ਕਈ ਪਛਾਣਾਂ ਦਿੰਦਾ ਹੈ। ਘੱਟ authentication-attempt ਹੱਦ ਵਾਲਾ ਸਰਵਰ ਜਾਂ ਨੀਤੀ ਪਹਿਲੀਆਂ ਕੁੰਜੀਆਂ ਫੇਲ੍ਹ ਹੋਣ ਤੋਂ ਬਾਅਦ ਸਹੀ ਕੁੰਜੀ ਵੀ ਰੱਦ ਕਰ ਸਕਦੀ ਹੈ।

Atlassian ਦੀ [ਕਈ ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ ਕੁੰਜੀਆਂ ਬਾਰੇ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) ਰਿਪੋਜ਼ਟਰੀ Git configuration ਫਾਈਲ ਵਿੱਚ `core.sshCommand` ਅਤੇ ਗਲੋਬਲ Git configuration ਵਿੱਚ `includeIf` ਵਰਤਦੀ ਹੈ। ਹਰ ਰਿਪੋਜ਼ਟਰੀ ਲਈ ਇੱਕ ਕੁੰਜੀ ਵਾਸਤੇ ਇਹੋ ਤਰੀਕਾ ਵਰਤੋ।

ਫਾਈਲ-ਅਧਾਰਿਤ ਪੋਰਟੇਬਲ ਉਦਾਹਰਣ:

```ini
# ਇੱਕ ਸਥਾਨਕ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਅੰਦਰ .gitconfig
[core]
    sshCommand = ssh -o IdentitiesOnly=yes -i ~/.ssh/<repository-automation-key>
```

```ini
# ~/.gitconfig
[includeIf "gitdir:~/src/<repository>/"]
    path = ~/src/<repository>/.gitconfig
```

ਉੱਪਰਲਾ block ਸਮਰਪਿਤ ਆਟੋਮੇਸ਼ਨ ਪਛਾਣ ਲਈ ਫਾਈਲ-ਅਧਾਰਿਤ ਨਿੱਜੀ-ਕੁੰਜੀ ਛੋਟ ਹੈ। ਇਹ 1Password SSH Agent ਸੈੱਟ ਨਹੀਂ ਕਰਦਾ। 1Password SSH Agent ਲਈ [1Password setup guide](https://www.1password.dev/ssh/get-started) ਤੋਂ ਪਲੇਟਫਾਰਮ-ਵਿਸ਼ੇਸ਼ `IdentityAgent` ਜਾਂ `SSH_AUTH_SOCK` ਮੁੱਲ ਸੈੱਟ ਕਰੋ। ਕੁਝ OpenSSH configurations `.pub` ਫਾਈਲ ਨੂੰ agent identity selector ਵਜੋਂ ਵਰਤਦੀਆਂ ਹਨ। ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਪਲੇਟਫਾਰਮ ਸਹਾਇਤਾ ਪੁਸ਼ਟੀ ਕਰੋ। ਫਾਈਲ-ਅਧਾਰਿਤ ਸੈਟਅੱਪ ਨੂੰ ਮਿਲਦੀ ਨਿੱਜੀ-ਕੁੰਜੀ ਦਾ ਰਸਤਾ ਚਾਹੀਦਾ ਹੈ। ਨਿੱਜੀ ਕੁੰਜੀ ਦੀ ਸਮੱਗਰੀ ਮੰਗਣ ਵਾਲੀ ਕਮਾਂਡ ਨੂੰ `.pub` ਫਾਈਲ ਨਾ ਦਿਓ ਅਤੇ ਨਿੱਜੀ ਨਿੱਜੀ ਕੁੰਜੀ export ਨਾ ਕਰੋ।

ਜਦੋਂ ਸਥਾਨਕ clone ਨੂੰ ਇੱਕ ਖਾਸ ਕੁੰਜੀ ਚਾਹੀਦੀ ਹੋਵੇ ਤਾਂ ਸਪਸ਼ਟ repository configuration ਵਰਤੋ। ਇੱਕੋ ਪਹੁੰਚ ਹੱਦ ਵਾਲੇ ਕਈ clone ਇੱਕ directory ਵਿੱਚ ਹੋਣ ਤਾਂ `includeIf` ਵਰਤੋ। [ਕਈ ਕੁੰਜੀਆਂ ਦੀ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/managing-multiple-repository-access-keys-on-one-device/) Bitbucket workflow ਦੀਆਂ ਦੋਵੇਂ ਸੈਟਿੰਗਾਂ ਦਿਖਾਉਂਦੀ ਹੈ।

SSH ਰਾਹੀਂ Git clone ਕਰੋ:

```bash
git clone git@bitbucket.org:<workspace>/<repository>.git <local-directory>
```

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** Git `<local-directory>` ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ `bitbucket.org` ਰਾਹੀਂ ਰਿਪੋਜ਼ਟਰੀ ਲੈਂਦਾ ਹੈ। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ ਕੁੰਜੀ ਸਿਰਫ਼ clone ਅਤੇ pull ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦੀ ਹੈ।

## ਸੀਮਿਤ REST ਪੜ੍ਹਨ ਲਈ API ਟੋਕਨ ਵਰਤੋ

Git ਆਵਾਜਾਈ ਲਈ SSH ਵਰਤੋ। ਮੈਟਾਡਾਟਾ ਜਾਂ Git ਆਵਾਜਾਈ ਤੋਂ ਬਾਹਰ ਦੇ ਕੰਮਾਂ ਲਈ REST API ਵਰਤੋ। [API ਟੋਕਨ ਅਧਿਕਾਰ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/) Read, Write, Admin ਅਤੇ Delete ਵਰਗੇ repository scopes ਦੱਸਦੀ ਹੈ। Repository Read ਦਾ ਮੁੱਲ `read:repository:bitbucket` ਹੈ ਅਤੇ ਇਸ ਵਿੱਚ pull request ਪਹੁੰਚ ਨਹੀਂ।

ਪੜ੍ਹਨ ਆਟੋਮੇਸ਼ਨ ਲਈ Bitbucket repository ਜਾਂ project access token ਨੂੰ ਤਰਜੀਹ ਦਿਓ, ਜੇ ਨਿਸ਼ਾਨਾ ਲੋੜੀਂਦੇ endpoint ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਵਰਤੋਂਕਾਰ-ਅਧਾਰਿਤ API ਟੋਕਨ ਖਾਤੇ ਦੀ ਵੱਡੀ ਪਹੁੰਚ ਰੱਖਦਾ ਹੈ। workspace access token ਸਿਰਫ਼ ਉਦੋਂ ਵਰਤੋ ਜਦੋਂ ਕੰਮ ਦਾ ਰਿਕਾਰਡ ਵੱਡੀ ਹੱਦ ਦੱਸੇ। ਕਿਸਮ ਚੁਣਨ ਤੋਂ ਪਹਿਲਾਂ [Bitbucket access-token ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/) ਵੇਖੋ।

ਏਜੰਟ ਦੇ ਪੜ੍ਹਨ ਰਸਤੇ ਲਈ `read:repository:bitbucket` ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ। `read:pullrequest:bitbucket` ਸਿਰਫ਼ ਉਦੋਂ ਜੋੜੋ ਜਦੋਂ ਏਜੰਟ ਨੂੰ pull request ਡਾਟਾ ਚਾਹੀਦਾ ਹੋਵੇ। workspace ਜਾਂ pipeline scopes ਸਿਰਫ਼ ਉਦੋਂ ਜੋੜੋ ਜਦੋਂ ਕੰਮ ਦਾ ਰਿਕਾਰਡ endpoint ਅਤੇ ਨਤੀਜਾ ਦੱਸੇ। Write ਅਤੇ admin scopes ਲਈ ਵੱਖਰੀ ਮਨਜ਼ੂਰੀ ਲੋੜੀਂਦੀ ਹੈ।

ਹਰ API ਟੋਕਨ ਇੱਕ ਮਕਸਦ ਲਈ ਬਣਾਓ, ਮਿਆਦ-ਪੂਰੀ ਤਾਰੀਖ ਰੱਖੋ, rotation ਰਿਕਾਰਡ ਵਿੱਚ ਦਰਜ ਕਰੋ ਅਤੇ ਮਿਆਦ ਤੋਂ ਪਹਿਲਾਂ ਟੋਕਨ ਬਦਲੋ। Atlassian ਦੀ [API ਟੋਕਨ ਬਣਾਉਣ ਗਾਈਡ](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) ਨਾਮ, ਮਿਆਦ, app ਚੋਣ ਅਤੇ scopes ਮੰਗਦੀ ਹੈ। ਬਣਨ ਤੋਂ ਬਾਅਦ ਟੋਕਨ ਇੱਕ ਵਾਰ ਦਿਖਦਾ ਹੈ।

ਮੁੱਲ 1Password ਜਾਂ ਪ੍ਰਬੰਧਿਤ runtime secret ਵਿੱਚ ਰੱਖੋ। ਇਸਨੂੰ remote URL ਵਿੱਚ ਨਾ ਰੱਖੋ। bearer token environment variable ਰਾਹੀਂ ਸਿਰਫ਼ ਉਸ process ਨੂੰ ਦਿਓ ਜਿਸਨੂੰ ਇੱਕ ਪੜ੍ਹਨ ਦੀ ਲੋੜ ਹੈ:

```bash
op run --env-file=/path/to/agent.env -- \
sh -c 'curl --fail --silent --show-error \
  --request GET \
  --url "https://api.bitbucket.org/2.0/repositories/<workspace>/<repository>" \
  --header "Authorization: Bearer ${BITBUCKET_API_TOKEN}" \
  --header "Accept: application/json"'
```

`/path/to/agent.env` ਨੂੰ ਰਿਪੋਜ਼ਟਰੀ ਤੋਂ ਬਾਹਰ ਰੱਖੋ। ਫਾਈਲ ਵਿੱਚ `BITBUCKET_API_TOKEN=op://synthetic-vault/synthetic-api-token/credential` ਵਰਗਾ ਹਵਾਲਾ ਰੱਖੋ। `op run` ਹਵਾਲਾ ਹੱਲ ਕਰਦਾ ਹੈ ਅਤੇ subprocess ਚੱਲਣ ਤੱਕ curl child process ਨੂੰ ਮੁੱਲ ਦਿੰਦਾ ਹੈ। ਇਹ child process ਨੂੰ environment variable ਦਾ ਮੁੱਲ ਪੜ੍ਹਨ ਜਾਂ ਲੌਗ ਕਰਨ ਤੋਂ ਨਹੀਂ ਰੋਕਦਾ। placeholder ਨੂੰ ਅਸਲੀ ਟੋਕਨ ਨਾਲ ਨਾ ਬਦਲੋ।

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** ਚੁਣੀ ਰਿਪੋਜ਼ਟਰੀ ਦਾ JSON metadata। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। placeholder committed ਫਾਈਲ ਜਾਂ ਲੌਗ ਵਿੱਚ ਅਸਲੀ ਟੋਕਨ ਨਾ ਬਣੇ।

ਲੰਮੇ ਆਟੋਮੇਸ਼ਨ ਲਈ ਸਮਰਥਿਤ CLI ਜਾਂ service-account ਤਰੀਕੇ ਰਾਹੀਂ 1Password ਨੂੰ process environment ਵਿੱਚ secret ਦੇਣ ਦਿਓ। ਟੋਕਨ ਦੀ ਮਿਆਦ ਕੰਮ ਲਈ ਢੁੱਕਵੀਂ ਰੱਖੋ। ਕੰਮ ਜਲਦੀ ਮੁੱਕੇ ਜਾਂ host ਦਾ ਮਾਲਕ ਬਦਲੇ ਤਾਂ ਟੋਕਨ ਰੱਦ ਕਰੋ।

## MCP ਨੂੰ ਛੋਟੀ ਪੜ੍ਹਨ-ਸਤਹ ਦਿਓ

ਨਵੇਂ ਸਰਵਰ ਦੀ ਸਮੀਖਿਆ ਕਰਦੇ ਸਮੇਂ [ਮੌਜੂਦਾ MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) ਅਤੇ ਇਸਦੇ [authorization ਨਿਯਮ](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) ਵਰਤੋ। HTTP ਸਰਵਰਾਂ ਨੂੰ token audience ਦੀ ਜਾਂਚ ਅਤੇ 401 ਤੇ 403 ਜਵਾਬਾਂ ਦਾ ਸਪਸ਼ਟ ਪ੍ਰਬੰਧ ਚਾਹੀਦਾ ਹੈ।

MCP host ਵਰਤੋਂਕਾਰ ਦੀ ਸਹਿਮਤੀ ਲੈਂਦਾ ਹੈ। client ਇੱਕ ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਰੱਖਦਾ ਹੈ। ਸਰਵਰ tools, resources ਜਾਂ prompts ਦਿੰਦਾ ਹੈ। ਸਰੋਤ, transport, account ਅਤੇ permissions ਦੀ ਸਮੀਖਿਆ ਹੋਣ ਤੱਕ ਹਰ ਸਰਵਰ ਨੂੰ ਅਣਭਰੋਸੇਯੋਗ ਕੋਡ ਮੰਨੋ।

ਅਗਲੇ ਪੈਰੇ ਦਾ 2025-06-18 specification URL ਇਤਿਹਾਸਕ ਵਰਜਨ ਹੈ। ਨਵੀਆਂ ਸਮੀਖਿਆਵਾਂ ਲਈ ਮੌਜੂਦਾ 2026-07-28 specification ਵਰਤੋ।

[MCP specification](https://modelcontextprotocol.io/specification/2025-06-18) MCP host, client ਅਤੇ server ਵਿਚਕਾਰ ਸੰਚਾਰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ। ਸਰਵਰ protocol ਰਾਹੀਂ tools, resources ਜਾਂ prompts ਦਿੰਦਾ ਹੈ। MCP ਸੰਪਰਕ ਦਾ ਫਾਰਮੈਟ ਮਿਆਰੀ ਕਰਦਾ ਹੈ। host, server implementation, account, token scope ਅਤੇ ਮਨਜ਼ੂਰੀ ਨੀਤੀ ਤੈਅ ਕਰਦੇ ਹਨ ਕਿ call ਕਿੱਥੇ ਪਹੁੰਚਦੀ ਹੈ।

Git ਅਤੇ Bitbucket Cloud REST API ਦੇ ਉੱਪਰ ਸੀਮਿਤ adapter ਵਜੋਂ MCP ਸਰਵਰ ਵਰਤੋ।

adapter ਨੂੰ token passthrough, server-side request forgery (SSRF) ਅਤੇ confused-deputy ਵਿਹਾਰ ਤੋਂ ਸੁਰੱਖਿਅਤ ਕਰੋ। SSRF ਵਿੱਚ ਸਰਵਰ ਬੇਇਰਾਦਾ ਟਿਕਾਣਿਆਂ ਨੂੰ ਬੇਨਤੀਆਂ ਭੇਜਦਾ ਹੈ। confused-deputy ਵਿਹਾਰ ਉਦੋਂ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਸਰਵਰ ਕਾਲ ਕਰਨ ਵਾਲੇ ਦੀ ਥਾਂ ਵੱਧ ਅਧਿਕਾਰ ਵਰਤਦਾ ਹੈ। ਖਤਰਨਾਕ ਸਥਾਨਕ ਸਰਵਰਾਂ, ਅਸੁਰੱਖਿਅਤ OAuth redirects ਅਤੇ ਬਹੁਤ ਵੱਡੇ ਸਰੋਤ-ਡਾਟਾ ਜਵਾਬਾਂ ਤੋਂ ਵੀ ਸੁਰੱਖਿਆ ਕਰੋ। ਮਨਜ਼ੂਰ Bitbucket origins ਅਤੇ repository identifiers ਨਿਸ਼ਚਿਤ ਕਰੋ। ਸਥਾਨਕ ਸਰਵਰ ਵੱਖਰੇ operating-system user ਹੇਠ sandbox ਵਿੱਚ ਚਲਾਓ। ਟੂਲ ਨਤੀਜਿਆਂ ਅਤੇ ਲੌਗਾਂ ਵਿੱਚ ਰਾਜ਼ ਲੁਕਾਓ।

ਇਹ ਭਾਗ ਡਿਜ਼ਾਈਨ ਦੱਸਦਾ ਹੈ, ਜਾਂਚਿਆ MCP configuration ਨਹੀਂ। ਕੋਈ client, server, transport, version ਜਾਂ fixture ਨਿਸ਼ਚਿਤ ਨਹੀਂ। production ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਏਜੰਟ ਜੋੜਨ ਤੋਂ ਪਹਿਲਾਂ ਵੱਖਰੇ test profile ਵਿੱਚ ਇੱਕ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ ਸਰਵਰ ਜਾਂਚੋ।

ਪੜ੍ਹਨ ਵਾਲੇ ਟੂਲਾਂ ਦੀਆਂ ਮਿਸਾਲਾਂ:

| ਟੂਲ | ਸੀਮਿਤ ਨਤੀਜਾ |
|---|---|
| **`get_repository_metadata`** | ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਦਾ metadata ਦਿੰਦਾ ਹੈ |
| **`read_source_file`** | ਇੱਕ revision ਉੱਤੇ ਇੱਕ path ਪੜ੍ਹਦਾ ਹੈ |
| **`list_branches`** | ਇੱਕ ਰਿਪੋਜ਼ਟਰੀ ਦੀਆਂ ਸ਼ਾਖਾਂ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ |
| **`get_pull_request`** | token ਵਿੱਚ pull request read scope ਹੋਵੇ ਤਾਂ ਇੱਕ pull request ਦਿੰਦਾ ਹੈ |
| **`get_build_status`** | ਇੱਕ commit ਦੀ status ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ |

ਇਹ ਨਾਮ ਡਿਜ਼ਾਈਨ ਦੱਸਦੇ ਹਨ। ਇਹ Atlassian ਕਮਾਂਡਾਂ ਦੇ ਨਾਮ ਨਹੀਂ। ਸਰਵਰ ਨੂੰ ਮਨਮਾਨੇ URL, shell ਕਮਾਂਡਾਂ, raw ਟੋਕਨ, ਨਿੱਜੀ-ਕੁੰਜੀ export ਬੇਨਤੀਆਂ ਜਾਂ ਬਿਨਾਂ ਸੀਮਾ repository identifiers ਲੈਣ ਤੋਂ ਰੋਕੋ।

ਚਾਰ ਪੱਧਰਾਂ ਉੱਤੇ permissions ਤੈਅ ਕਰੋ:

1. **Bitbucket Cloud:** Git ਲਈ repository ਜਾਂ project read key ਅਤੇ REST ਪੜ੍ਹਨ ਲਈ ਘੱਟੋ-ਘੱਟ API token scopes।
2. **1Password:** ਕੰਮ ਲਈ ਇੱਕ vault ਜਾਂ service account, ਨਿੱਜੀ-ਕੁੰਜੀ export ਰਸਤੇ ਤੋਂ ਬਿਨਾਂ।
3. **MCP ਸਰਵਰ:** ਪੜ੍ਹਨ ਵਾਲੇ ਟੂਲਾਂ ਦੀ allowlist, ਨਿਸ਼ਚਿਤ Bitbucket Cloud endpoints, input validation, timeout ਹੱਦਾਂ ਅਤੇ ਰਾਜ਼ ਹਟਾਏ ਲੌਗ।
4. **MCP host:** ਸਰਵਰ ਅਤੇ ਹਰ ਲਿਖਣ-ਯੋਗ ਕਾਰਵਾਈ ਲਈ ਵਰਤੋਂਕਾਰ ਦੀ ਮਨਜ਼ੂਰੀ, ਅਤੇ ਮੂਲ profile ਵਿੱਚ ਲਿਖਣ ਵਾਲੇ ਟੂਲ ਬੰਦ।

*MCP ਟੂਲ ਸੂਚੀ ਇਹ ਸਾਬਤ ਕਰਦੀ ਹੈ ਕਿ ਟੂਲ ਲੱਭੇ ਗਏ। ਇਹ authorization, ਸਹੀ scope, ਸੁਰੱਖਿਅਤ input handling ਜਾਂ ਸਹੀ ਨਤੀਜਾ ਸਾਬਤ ਨਹੀਂ ਕਰਦੀ।*

## ਏਜੰਟ ਵਰਕਫਲੋ ਦੇ ਪੜਾਅ ਰੱਖੋ

ਵਰਕਫਲੋ ਸਪਸ਼ਟ ਰੱਖੋ। ਹਰ ਪੜਾਅ ਅਗਲੇ ਲਈ ਸਬੂਤ ਦਿੰਦਾ ਹੈ।

| ਪੜਾਅ | ਏਜੰਟ ਦੀ ਕਾਰਵਾਈ | ਇਜਾਜ਼ਤ | ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ |
|---|---|---|---|
| **ਤਿਆਰੀ** | configuration, host-key ਰਿਕਾਰਡ, ਕੁੰਜੀ ਲੇਬਲ, token scope ਅਤੇ ਮਿਆਦ ਪੜ੍ਹੋ | ਸਥਾਨਕ ਪੜ੍ਹਨ | ਸੈੱਟਅੱਪ ਰਿਕਾਰਡ ਮਨਜ਼ੂਰ ਕਰੋ |
| **ਜਾਂਚ** | SSH ਉੱਤੇ Git ਨਾਲ clone ਜਾਂ fetch ਅਤੇ REST metadata ਪੁੱਛੋ | ਰਿਪੋਜ਼ਟਰੀ ਤੇ API ਪੜ੍ਹਨ | ਸੈੱਟਅੱਪ ਤੋਂ ਬਾਅਦ ਕੋਈ ਨਹੀਂ |
| **ਵਿਸ਼ਲੇਸ਼ਣ** | ਮਨਜ਼ੂਰ ਟੂਲਾਂ ਰਾਹੀਂ ਫਾਈਲਾਂ, ਸ਼ਾਖਾਂ, pull requests ਅਤੇ build status ਪੜ੍ਹੋ | ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੇ MCP ਟੂਲ | ਸੀਮਿਤ ਪੜ੍ਹਨ ਲਈ ਕੋਈ ਨਹੀਂ |
| **ਤਬਦੀਲੀ ਤਿਆਰ ਕਰੋ** | ਸਥਾਨਕ workspace ਵਿੱਚ patch, branch ਯੋਜਨਾ ਜਾਂ pull request draft ਬਣਾਓ | ਸਿਰਫ਼ ਸਥਾਨਕ ਲਿਖਣ | diff ਅਤੇ ਨਿਸ਼ਾਨਾ ਵੇਖੋ |
| **ਲਿਖਣ ਦੀ ਮਨਜ਼ੂਰੀ** | ਸਹੀ remote ਕਾਰਵਾਈ, scope ਅਤੇ ਵਾਪਸੀ ਰਸਤਾ ਦਿਖਾਓ | ਹਾਲੇ remote write ਨਹੀਂ | ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ |
| **ਲਿਖਣ ਦੀ ਕਾਰਵਾਈ** | branch push ਕਰੋ, pull request ਬਣਾਓ ਜਾਂ write endpoint ਕਾਲ ਕਰੋ | ਥੋੜ੍ਹੇ ਸਮੇਂ ਦੀ write identity | ਹਰ ਕਾਰਵਾਈ ਪੱਕੀ ਕਰੋ |
| **ਪੁਸ਼ਟੀ** | ਬਣਿਆ commit, pull request ਜਾਂ status ਪੜ੍ਹੋ | ਮੁੜ ਸਿਰਫ਼ ਪੜ੍ਹਨ | ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ ਪੱਕਾ ਕਰੋ |

ਮੂਲ ਏਜੰਟ profile ਨੂੰ **ਵਿਸ਼ਲੇਸ਼ਣ** ਜਾਂ **ਤਬਦੀਲੀ ਤਿਆਰ ਕਰੋ** ਤੋਂ ਬਾਅਦ ਰੁਕਣਾ ਚਾਹੀਦਾ ਹੈ। ਵੱਖਰੇ write profile ਵਿੱਚ ਹੋਰ token ਜਾਂ key, ਛੋਟੀ ਮਿਆਦ, ਨਿਸ਼ਚਿਤ ਨਿਸ਼ਾਨਾ ਅਤੇ ਮਨਜ਼ੂਰੀ prompt ਹੋਵੇ। ਰਿਪੋਜ਼ਟਰੀ ਪਹੁੰਚ ਕੁੰਜੀ ਲਿਖਣ ਵਾਲਾ ਪੜਾਅ ਨਹੀਂ ਕਰ ਸਕਦੀ, ਜਿਸ ਨਾਲ ਲਾਭਦਾਇਕ ਤਕਨੀਕੀ ਹੱਦ ਬਣਦੀ ਹੈ।

## ਵਾਪਸੀ ਅਤੇ ਹਟਾਉਣਾ

ਪਹਿਲਾਂ ਪਹੁੰਚ ਹਟਾਓ, ਫਿਰ ਸਥਾਨਕ configuration ਸਾਫ਼ ਕਰੋ:

1. ਸੰਬੰਧਿਤ Bitbucket ਸੈਟਿੰਗ ਪੰਨੇ ਤੋਂ repository, project ਜਾਂ workspace ਪਹੁੰਚ ਕੁੰਜੀ ਹਟਾਓ।
2. ਸੰਬੰਧਿਤ Bitbucket ਸੁਰੱਖਿਆ ਪੰਨੇ ਵਿੱਚ repository, project, workspace ਜਾਂ user API token ਰੱਦ ਕਰੋ।
3. ਸਥਾਪਿਤ CLI ਵਰਜਨ ਲਈ ਦਰਜ [ਪ੍ਰਮਾਣੀਕਰਨ ਪ੍ਰਕਿਰਿਆ](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/getting-started/how-authentication-works/) ਰਾਹੀਂ ਸੁਰੱਖਿਅਤ Teamwork Graph credential ਹਟਾਓ। ਪੁਰਾਣੀ credential ਸਿਰਫ਼ ਮਨਜ਼ੂਰ secret manager ਵਿੱਚ ਰੱਖੋ। ਪੱਕਾ ਕਰੋ ਕਿ ਵੱਖਰਾ profile ਹੁਣ ਟੈਸਟ credential ਨਹੀਂ ਦਿਖਾਉਂਦਾ।
4. ਟੈਸਟ ਖਤਮ ਹੋਣ ਉੱਤੇ repository `.gitconfig` ਫਾਈਲ ਅਤੇ ਇਸਦੀ `includeIf` entry ਹਟਾਓ। ਗੈਰ-ਸੰਬੰਧਿਤ Git configuration ਨਾ ਬਦਲੋ।
5. ਟੈਸਟ ਲਈ ਜੋੜੀ ਸਿਰਫ਼ ਤਸਦੀਕਸ਼ੁਦਾ Bitbucket host-key ਲਾਈਨ ਹਟਾਓ। ਹੋਰ ਮਨਜ਼ੂਰ host keys ਰੱਖੋ।
6. ਬਾਹਰੀ `agent.env` ਫਾਈਲ ਅਤੇ ਅਸਥਾਈ ਨਤੀਜੇ ਹਟਾਓ। host configuration ਤੋਂ MCP server entry ਹਟਾ ਕੇ host ਮੁੜ ਚਲਾਓ।

ਹਰ ਹਟਾਉਣ ਦੀ ਕਾਰਵਾਈ, ਕਰਨ ਵਾਲੇ ਵਿਅਕਤੀ ਅਤੇ ਸਮੇਂ ਦਾ ਰਿਕਾਰਡ ਰੱਖੋ। ਕੋਈ ਮੁੱਲ ਅਣਉਮੀਦ ਲੌਗ, ਪ੍ਰਕਿਰਿਆ ਰਿਕਾਰਡ ਜਾਂ transcript ਵਿੱਚ ਆ ਜਾਵੇ ਤਾਂ key ਜਾਂ token ਬਦਲੋ।

## ਸਥਾਨਕ ਹਵਾਲੇ ਅੱਪਡੇਟ ਕਰਨ ਵਾਲਾ ਦੂਰਲਾ-ਪੜ੍ਹਨ ਚੱਕਰ

ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਵਾਰ-ਵਾਰ ਜਾਂਚ ਲਈ ਛੋਟਾ ਚੱਕਰ ਵਰਤੋ:

```bash
LOCAL_REPO="<local-directory>"
git -C "$LOCAL_REPO" fetch --no-tags
git -C "$LOCAL_REPO" status --short --branch
git -C "$LOCAL_REPO" log -1 --format='%H %ad %s' --date=iso-strict
```

`HEAD` ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਮੌਜੂਦਾ checkout reference ਹੈ। ਸਫਲ ਨਤੀਜਾ ਸਾਬਤ ਕਰਦਾ ਹੈ ਕਿ ਮਨਜ਼ੂਰ SSH ਪਛਾਣ ਨਿਰਧਾਰਤ ਰਿਪੋਜ਼ਟਰੀ ਤੱਕ ਪਹੁੰਚੀ। ਇਹ ਨਹੀਂ ਦੱਸਦਾ ਕਿ ਕਿਹੜੀ ਕੁੰਜੀ ਚੁਣੀ ਗਈ ਜਾਂ push ਪਹੁੰਚ ਹੈ।

**ਉਮੀਦ ਕੀਤਾ ਨਤੀਜਾ:** fetch ਨਤੀਜਾ, branch status ਅਤੇ ਇੱਕ commit ਲਾਈਨ। ਬਿਨਾਂ ਜਾਂਚਿਆ ਉਦਾਹਰਣ। `fetch` remote ਉੱਤੇ ਨਹੀਂ ਲਿਖਦਾ, ਪਰ ਸਥਾਨਕ references ਅਤੇ `FETCH_HEAD` ਅੱਪਡੇਟ ਕਰਦਾ ਹੈ। ਇਹ ਚੱਕਰ push ਨਹੀਂ ਕਰਦਾ ਜਾਂ branch ਨਹੀਂ ਬਦਲਦਾ।

MCP ਸਰਵਰ ਨੂੰ ਨਾਮ ਵਾਲੀਆਂ ਕਾਰਵਾਈਆਂ ਰਾਹੀਂ ਇਹੋ ਪੜ੍ਹਨ ਸੀਮਾ ਦੇਣੀ ਚਾਹੀਦੀ ਹੈ। ਸਥਾਨਕ shell wrapper ਜਾਂ MCP tool ਨੂੰ ਬੇਨਤੀ ਭੇਜਣ ਤੋਂ ਪਹਿਲਾਂ write verb ਰੱਦ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ। ਟੂਲ ਦਾ ਨਾਮ, repository placeholder, revision, ਨਤੀਜੇ ਦੀ ਕਿਸਮ ਅਤੇ ਸਮਾਂ ਲੌਗ ਕਰੋ। ਜਦ ਤੱਕ ਕੰਮ ਲਈ ਇੱਕ ਫਾਈਲ ਖਾਸ ਤੌਰ ਉੱਤੇ ਲੋੜੀਂਦੀ ਨਾ ਹੋਵੇ, token, cookie, ਨਿੱਜੀ paths ਅਤੇ ਫਾਈਲ ਸਮੱਗਰੀ ਲੁਕਾਓ।

## ਸਮੱਸਿਆ ਹੱਲ

### `Permission denied (publickey)`

ਸਰਗਰਮ agent socket, ਚੁਣੀ ਜਨਤਕ ਕੁੰਜੀ, repository access-key entry ਅਤੇ `IdentitiesOnly` ਜਾਂਚੋ। repository key ਨਿਸ਼ਾਨੇ ਵਾਲੀ repository ਜਾਂ project ਵਿੱਚ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। ਨਿੱਜੀ key ਲਈ account permission ਚਾਹੀਦੀ ਹੈ। workspace access key ਦੀ write ਹੱਦ ਵੱਖਰੀ ਹੈ।

### ਗਲਤ repository key ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ

`core.sshCommand` ਨਾਲ ਹਰ repository ਲਈ ਇੱਕ key ਵਰਤੋ ਜਾਂ `includeIf` ਨਾਲ ਨਿਯੰਤਰਿਤ directory ਵਿੱਚ clones ਇਕੱਠੇ ਰੱਖੋ। `ssh-add -l` ਨਾਲ agent keys ਵੇਖੋ। ਕਈ 1Password keys ਹੋਣ ਤਾਂ ਸਪਸ਼ਟ identity selector ਜਾਂ 1Password SSH bookmark ਵਰਤੋ। [1Password Agent ਗਾਈਡ](https://www.1password.dev/ssh/agent) key ਗਿਣਤੀ ਅਤੇ bookmark ਸੰਬੰਧੀ ਗੱਲਾਂ ਦੱਸਦੀ ਹੈ।

### SSH ਬਦਲੀ host key ਦੱਸਦਾ ਹੈ

ਏਜੰਟ ਰੋਕੋ। ਪਹਿਲੀ ਕਾਰਵਾਈ ਵਜੋਂ `known_hosts` ਨਾ ਮਿਟਾਓ। ਸੁਤੰਤਰ ਮਾਧਿਅਮ ਰਾਹੀਂ ਮੌਜੂਦਾ Bitbucket Cloud host-key record ਦੀ ਸਥਾਨਕ entry ਨਾਲ ਤੁਲਨਾ ਕਰੋ। ਤੁਲਨਾ ਸਹੀ ਹੋਣ ਉੱਤੇ ਹੀ entry ਹਟਾਓ ਜਾਂ ਬਦਲੋ।

### API `401` ਜਾਂ `403` ਦਿੰਦੀ ਹੈ

token ਦੀ ਮਿਆਦ, ਕਿਸਮ, endpoint scope ਅਤੇ account ਜਾਂ workspace ਸੀਮਾ ਜਾਂਚੋ। repository read scope ਵਿੱਚ pull requests ਨਹੀਂ। write endpoint ਲਈ write scope ਅਤੇ ਮਨਜ਼ੂਰ write profile ਚਾਹੀਦਾ ਹੈ। ਫੇਲ੍ਹ ਹੋਏ endpoint ਦੀ ਪਛਾਣ ਤੋਂ ਪਹਿਲਾਂ scopes ਨਾ ਵਧਾਓ।

### API repository ਡਾਟਾ ਦਿੰਦੀ ਹੈ ਪਰ pull requests ਨਹੀਂ

ਨਵੇਂ ਜਾਂ ਬਦਲੇ token ਵਿੱਚ ਸਭ ਤੋਂ ਛੋਟਾ pull request read scope ਜੋੜੋ। ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲੇ MCP ਸਰਵਰ ਲਈ ਵਿਸ਼ਾਲ user token ਮੁੜ ਨਾ ਵਰਤੋ।

### MCP ਸਰਵਰ ਟੂਲ ਦਿਖਾਉਂਦਾ ਹੈ ਪਰ ਕਾਲ ਫੇਲ੍ਹ ਹੁੰਦੀ ਹੈ

server registration, connection, tool discovery, execution ਅਤੇ ਨਤੀਜਾ ਪੁਸ਼ਟੀ ਨੂੰ ਵੱਖ ਕਰੋ। token ਦਿਖਾਏ ਬਿਨਾਂ server log ਵੇਖੋ। endpoint ਅਤੇ input shape ਜਾਂਚੋ। ਕਨੈਕਟੀਵਿਟੀ ਜਾਂਚਣ ਤੋਂ ਬਾਅਦ ਇੱਕ ਵਾਰ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਦੂਜੀ ਕਾਲ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਕਾਰਵਾਈ ਅਧੂਰੀ ਦਰਜ ਕਰੋ।

### ਤੀਜੀ ਧਿਰ ਦਾ Bitbucket CLI ਵੱਡੀ ਪਹੁੰਚ ਮੰਗਦਾ ਹੈ

ਇੰਸਟਾਲੇਸ਼ਨ ਰੋਕੋ। ਮੰਗੀ ਪਹੁੰਚ ਦੀ ਕੰਮ ਦੇ ਰਿਕਾਰਡ ਨਾਲ ਤੁਲਨਾ ਕਰੋ। ਸਰੋਤ, release signatures ਜਾਂ checksums, ਨੈੱਟਵਰਕ ਮੰਜ਼ਿਲਾਂ, ਰਾਜ਼ਾਂ ਦੀ ਸਟੋਰੇਜ ਅਤੇ ਲਿਖਣ ਵਿਹਾਰ ਜਾਂਚੋ। Atlassian CLI ਦਾ ਅਧਿਕਾਰਤ ਕਮਾਂਡ ਹਵਾਲਾ ਤੀਜੀ ਧਿਰ ਦੇ Bitbucket binary ਦੀ ਹਮਾਇਤ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ।

## ਅਗਲੇ ਕਦਮ

ਰਿਪੋਜ਼ਟਰੀ ਜਾਂ ਪ੍ਰੋਜੈਕਟ ਦਾਇਰਾ, ਕੁੰਜੀ ਲੇਬਲ, host-key ਪੁਸ਼ਟੀ ਮਿਤੀ, API scopes, token ਮਿਆਦ, 1Password ਮਾਲਕ, MCP tool allowlist, ਲੌਗ ਨੀਤੀ ਅਤੇ ਲਿਖਣ ਦੀ ਮਨਜ਼ੂਰੀ ਦੇਣ ਵਾਲੇ ਵਿਅਕਤੀ ਸਮੇਤ ਛੋਟਾ ਪਹੁੰਚ ਰਿਕਾਰਡ ਬਣਾਓ।

transcript ਵਿੱਚ placeholders ਰੱਖ ਕੇ ਇੱਕ ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ clone, ਇੱਕ REST metadata ਪੜ੍ਹਨ ਅਤੇ ਇੱਕ MCP tool ਪੜ੍ਹਨ ਚਲਾਓ। ਨਤੀਜਿਆਂ ਦੀ ਤੁਲਨਾ ਕਰੋ। ਰਿਕਾਰਡ ਅਤੇ logs ਦੀ ਜਾਂਚ ਹੋਣ ਤੱਕ ਏਜੰਟ profile ਸਿਰਫ਼ ਪੜ੍ਹਨ ਵਾਲਾ ਰੱਖੋ।

ਲਿਖਣ ਦਾ ਕੰਮ ਆਵੇ ਤਾਂ ਪਹਿਲਾਂ ਸਥਾਨਕ diff ਤਿਆਰ ਕਰੋ। ਨਿਸ਼ਾਨਾ branch, ਬਦਲੇ paths, ਮੰਗਿਆ API method, token scope ਅਤੇ ਵਾਪਸੀ ਕਦਮ ਦੱਸੋ। ਸਹੀ ਕਾਰਵਾਈ ਲਈ ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ ਤੋਂ ਬਾਅਦ ਹੀ ਵੱਖਰੀ ਥੋੜ੍ਹੇ ਸਮੇਂ ਵਾਲੀ ਲਿਖਣ ਪਛਾਣ ਵਰਤੋ।
