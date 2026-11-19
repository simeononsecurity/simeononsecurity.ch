---
title: 'Home Assistant Core 2026.11 ਤੋਂ 2026.10.4 ਵੱਲ ਰੋਲਬੈਕ: HTTP ਸਟੋਰੇਜ ਵਰਜਨ 3 ਦੀ ਮੁਰੰਮਤ'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Yellow ਉੱਤੇ Home Assistant Core 2026.11 ਦੇ 2026.10.4 ਵੱਲ ਮੁੜਨ ਮਗਰੋਂ HTTP ਸਟੋਰੇਜ ਵਰਜਨ 3 ਦੀ ਗਲਤੀ ਠੀਕ ਕਰੋ। ਇਸ ਵਿੱਚ
  ਸੁਰੱਖਿਅਤ ਕਮਾਂਡਾਂ ਅਤੇ ਜਾਂਚੇ ਹੋਏ ਨਤੀਜੇ ਹਨ।
genre:
- ਘਰੇਲੂ ਆਟੋਮੇਸ਼ਨ
- ਸਮੱਸਿਆ ਹੱਲ
tags:
- Home Assistant Yellow
- Home Assistant OS
- Core 2026.11 ਵੱਲੋਂ ਰੋਲਬੈਕ
- Core 2026.10.4
- HTTP ਸਟੋਰੇਜ ਵਰਜਨ 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: ਪੀਲੇ ਕੰਪਿਊਟਰ ਬੋਰਡ, ਟੁੱਟੇ ਕਨਫ਼ਿਗਰੇਸ਼ਨ ਲਿੰਕ ਅਤੇ ਮੁੜ ਚੱਲੇ ਵੈੱਬ ਡੈਸ਼ਬੋਰਡ ਦਾ ਚਿੱਤਰ
coverCaption: ''
---

Home Assistant Core 2026.11 ਦਾ ਅੱਪਡੇਟ ਅਸਫਲ ਹੋਇਆ ਅਤੇ ਮੇਰੇ Yellow CM4 ਨੂੰ 2026.10.4 ਉੱਤੇ ਵਾਪਸ ਲੈ ਆਇਆ। Yellow ਨੈੱਟਵਰਕ ਉੱਤੇ ਪਹੁੰਚਯੋਗ ਸੀ, ਪਰ ਡੈਸ਼ਬੋਰਡ ਦਿਖਾਉਣਾ ਬੰਦ ਕਰ ਗਿਆ। ਰੋਲਬੈਕ ਮਗਰੋਂ HTTP ਸੈਟਿੰਗਾਂ ਵਾਲੀ ਫ਼ਾਈਲ ਸਟੋਰੇਜ ਵਰਜਨ 3.1 ਵਿੱਚ ਰਹਿ ਗਈ, ਜਦਕਿ Core 2026.10.4 ਵਰਜਨ 2.2 ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਮੈਂ ਫ਼ਾਈਲ ਸੰਭਾਲੀ, ਸਖ਼ਤ ਜਾਂਚਾਂ ਨਾਲ ਉਸਦੀ ਨਕਲ ਬਦਲੀ, HTTP ਪਹੁੰਚ ਮੁੜ ਚਾਲੂ ਕੀਤੀ ਅਤੇ ਫਿਰ Core ਨੂੰ 2026.11.1 ਉੱਤੇ ਅੱਪਡੇਟ ਕੀਤਾ।

<!--more-->

## ਮੁੱਖ ਗੱਲਾਂ

- **ਅੰਤਰ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।** Core ਲੌਗ ਦੀ ਗਲਤੀ ਨੂੰ ਇੰਸਟਾਲ ਕੀਤੇ ਰਿਲੀਜ਼ ਅਤੇ HTTP ਸਟੋਰੇਜ ਵਰਜਨ ਨਾਲ ਮਿਲਾਓ।
- **ਫ਼ਾਈਲ ਸੰਭਾਲੋ।** ਰਿਕਵਰੀ ਤੋਂ ਪਹਿਲਾਂ ਬਿਨਾਂ ਤਬਦੀਲੀ ਵਾਲੀ ਨਕਲ ਅਤੇ ਡਿਵਾਈਸ ਤੋਂ ਬਾਹਰ ਬੈਕਅੱਪ ਰੱਖੋ।
- **ਨਤੀਜਾ ਜਾਂਚੋ।** Core ਦੀ ਹਾਲਤ, ਸੰਭਾਲਿਆ ਲਿਸਨਰ ਪੋਰਟ, ਡੈਸ਼ਬੋਰਡ ਅਤੇ ਇੰਸਟਾਲ ਕੀਤਾ ਵਰਜਨ ਵੇਖੋ।

**ਇਸੇ ਹਾਲਤ ਦਾ ਹੱਲ:** [HTTP ਫ਼ਾਈਲ ਸੰਭਾਲੋ](#preserve-recovery-options), [ਵਰਜਨ 2.2 ਦੀ ਉਮੀਦਵਾਰ ਫ਼ਾਈਲ ਬਣਾਕੇ ਜਾਂਚੋ](#apply-the-tested-fix-for-version-31), [Core ਰੋਕਣ ਮਗਰੋਂ ਇਸਨੂੰ ਇੰਸਟਾਲ ਕਰੋ](#apply-the-tested-fix-for-version-31) ਅਤੇ [ਅੱਪਡੇਟ ਦਾ ਨਤੀਜਾ ਜਾਂਚੋ](#verify-the-update-outcome)। ਰੂਪਾਂਤਰਨ ਅਸਲ ਫ਼ੀਲਡਾਂ ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ ਅਤੇ ਅੰਤਰ ਹੋਣ ਉੱਤੇ ਰੁਕ ਜਾਂਦਾ ਹੈ। ਇਸਨੂੰ ਅਣਜਾਂਚੀ HTTP ਫ਼ਾਈਲ ਉੱਤੇ ਨਾ ਵਰਤੋ।

## ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

ਤੁਹਾਨੂੰ Yellow CM4 ਤੱਕ ਭੌਤਿਕ ਪਹੁੰਚ, USB-C ਡਾਟਾ ਕੇਬਲ, ਚੱਲਦਾ ਸੀਰੀਅਲ ਕੰਸੋਲ ਅਤੇ ਵਰਤਣਯੋਗ ਬੈਕਅੱਪ ਜਾਂ ਸੰਭਾਲੀ ਕਨਫ਼ਿਗਰੇਸ਼ਨ ਚਾਹੀਦੀ ਹੈ। ਹੱਥੀਂ ਕੀਤੇ ਜਾਣ ਵਾਲੇ ਤਰੀਕੇ ਲਈ ਹੋਸਟ ਸ਼ੈੱਲ ਤੱਕ ਪਹੁੰਚ ਅਤੇ JSON ਦੀ ਧਿਆਨ ਨਾਲ ਜਾਂਚ ਲੋੜੀਂਦੀ ਹੈ। ਨਿਦਾਨ ਅਤੇ ਮੁਰੰਮਤ ਲਈ ਘੱਟੋ-ਘੱਟ 30 ਮਿੰਟ ਰੱਖੋ। ਵੱਡੀਆਂ ਇੰਸਟਾਲੇਸ਼ਨਾਂ ਵਿੱਚ Core ਚਾਲੂ ਹੋਣ ਅਤੇ ਬੈਕਅੱਪ ਬਹਾਲ ਕਰਨ ਲਈ ਹੋਰ ਸਮਾਂ ਲੱਗਦਾ ਹੈ।

## ਖ਼ਰਾਬੀ ਪਛਾਣੋ

Core ਲੌਗ ਵਿੱਚ ਫ਼ੈਸਲਾਕੁਨ ਗਲਤੀ ਇਹ ਸੀ:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

ਪੁਰਾਣਾ Core ਰਿਲੀਜ਼ `http` ਲੋਡ ਨਹੀਂ ਕਰ ਸਕਿਆ। HTTP ਉੱਤੇ ਨਿਰਭਰ ਫਰੰਟਐਂਡ ਅਤੇ ਹੋਰ ਹਿੱਸੇ ਵੀ ਫੇਲ੍ਹ ਹੋ ਗਏ। ਰਾਊਟਰ ਲੀਜ਼ ਮਿਲਣਾ ਅਤੇ Observer ਪੰਨੇ ਦਾ ਸਿਹਤਮੰਦ ਹੋਣਾ ਡੈਸ਼ਬੋਰਡ ਤੱਕ ਪਹੁੰਚ ਸਾਬਤ ਨਹੀਂ ਕਰਦਾ। [Home Assistant Core ਦੀ ਸਮੱਸਿਆ #190583](https://github.com/home-assistant/core/issues/190583) ਕਈ ਇੰਸਟਾਲੇਸ਼ਨਾਂ, Yellow ਸਮੇਤ, ਵਿੱਚ ਇਸੇ ਰੋਲਬੈਕ ਖ਼ਰਾਬੀ ਦਾ ਵੇਰਵਾ ਦਿੰਦਾ ਹੈ। [ਇਸ ਇਸ਼ੂ ਉੱਤੇ ਮੇਰੀ ਟਿੱਪਣੀ](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) ਇਸ Yellow ਉੱਤੇ ਜਾਂਚੀ ਰਿਕਵਰੀ ਅਤੇ Core ਦੀ ਆਖ਼ਰੀ ਹਾਲਤ ਦਰਜ ਕਰਦੀ ਹੈ।

**ਵੈੱਬ ਬੰਦ ਹੋਣ ਦਾ ਕਾਰਨ:** Core 2026.11 ਨੇ `.storage/http` ਨੂੰ 3.1 ਫਾਰਮੈਟ ਵਿੱਚ ਲਿਖਿਆ। ਰੋਲਬੈਕ ਨੇ Core 2026.10.4 ਵਾਪਸ ਲਿਆਇਆ, ਪਰ ਅਨੁਕੂਲ HTTP ਫ਼ਾਈਲ ਨਹੀਂ। Core 2026.10.4 ਸਟੋਰੇਜ ਵਰਜਨ 3 ਰੱਦ ਕਰਦਾ ਹੈ। ਇਸ Yellow ਦੀ ਸੰਭਾਲੀ `intermediate_v6` ਪ੍ਰੋਫ਼ਾਈਲ ਵੀ ਪੁਰਾਣੇ ਸਕੀਮਾ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦੀ। ਪਹਿਲਾ ਅੱਪਡੇਟ ਕਿਉਂ ਫੇਲ੍ਹ ਹੋਇਆ ਅਤੇ ਰੋਲਬੈਕ ਕਿਉਂ ਸ਼ੁਰੂ ਹੋਇਆ, ਇਹ ਪਤਾ ਨਹੀਂ। 2026-11-15 ਤੱਕ ਜੁੜਿਆ ਇਸ਼ੂ ਖੁੱਲ੍ਹਾ ਸੀ ਅਤੇ ਚਰਚਾ ਵਿੱਚ ਸੰਭਾਲਕਾਂ ਵੱਲੋਂ ਪੁਸ਼ਟੀ ਕੀਤਾ ਹੱਲ ਨਹੀਂ ਸੀ।

ਫ਼ਾਈਲਾਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਇੰਸਟਾਲ ਕੀਤਾ Core ਰਿਲੀਜ਼ ਅਤੇ HTTP ਸਟੋਰ ਜਾਂਚੋ:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

ਹੇਠਾਂ ਦਿੱਤਾ ਨਤੀਜਾ ਇਸੇ ਹਾਲਤ ਦਾ ਹੈ। ਸਮਾਂ-ਮੁਹਰਾਂ ਅਤੇ ਨਿੱਜੀ ਵੇਰਵੇ ਹਟਾਏ ਗਏ ਹਨ:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

ਹੇਠਲੀਆਂ ਰਿਕਵਰੀ ਕਮਾਂਡਾਂ Supervisor ਵਿੱਚ ਸੰਭਾਲੇ ਲਿਸਨਰ ਪੋਰਟ ਦੀ HTTP ਫ਼ਾਈਲ ਨਾਲ ਤੁਲਨਾ ਕਰਦੀਆਂ ਹਨ, ਪਰ ਦੋਵਾਂ ਵਿੱਚੋਂ ਕੋਈ ਮੁੱਲ ਨਹੀਂ ਦਿਖਾਉਂਦੀਆਂ। ਅੰਤਰ ਹੋਵੇ ਤਾਂ ਫ਼ਾਈਲਾਂ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ Core ਦਾ ਅਸਲ ਲਿਸਨਰ ਪੋਰਟ ਜਾਂਚੋ।

| ਸੰਕੇਤ | ਅਰਥ |
| --- | --- |
| Core ਸਟੋਰੇਜ ਵਰਜਨ 2 ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ, ਫ਼ਾਈਲ ਵਰਜਨ 3 ਦੱਸਦੀ ਹੈ | ਪੁਰਾਣਾ ਰਿਲੀਜ਼ ਸੰਭਾਲੀਆਂ HTTP ਸੈਟਿੰਗਾਂ ਲੋਡ ਨਹੀਂ ਕਰ ਸਕਦਾ |
| HTTP ਫ਼ਾਈਲ ਅਤੇ Supervisor ਸੂਚੀ ਵੱਖਰੇ ਲਿਸਨਰ ਪੋਰਟ ਦਿਖਾਉਂਦੀਆਂ ਹਨ | ਕਾਰਨ ਨਿਰਧਾਰਤ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ Core ਦਾ ਅਸਲ ਲਿਸਨਰ ਪੋਰਟ ਜਾਂਚੋ |
| ਮੁੱਖ ਪੰਨਾ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਪਰ Core ਦੀ ਹਾਲਤ ਹਾਲੇ STARTING ਹੈ | ਫਰੰਟਐਂਡ ਦਾ ਜਵਾਬ ਇਕੱਲਾ ਸਟਾਰਟਅੱਪ ਪੂਰਾ ਹੋਣ ਦਾ ਸਬੂਤ ਨਹੀਂ |

## ਰਿਕਵਰੀ ਦੇ ਵਿਕਲਪ ਸੰਭਾਲੋ {#preserve-recovery-options}

ਅਗਲੇ ਅੱਪਡੇਟ ਤੋਂ ਪਹਿਲਾਂ Yellow ਤੋਂ ਬਾਹਰ ਵਰਤਣਯੋਗ ਬੈਕਅੱਪ ਰੱਖੋ। [Home Assistant ਦੀ ਬੈਕਅੱਪ ਗਾਈਡ](https://www.home-assistant.io/common-tasks/general/backups/) ਕਲਾਉਡ ਅਤੇ ਡਿਵਾਈਸ ਤੋਂ ਬਾਹਰ ਵਾਲੀਆਂ ਥਾਵਾਂ ਬਾਰੇ ਦੱਸਦੀ ਹੈ। ਇਨਕ੍ਰਿਪਟ ਕੀਤੇ ਬੈਕਅੱਪ ਲਈ ਉਸਦੀ ਰਿਕਵਰੀ ਕੁੰਜੀ ਲੋੜੀਂਦੀ ਹੈ। ਸਟੋਰੇਜ ਦੇ ਇਸ ਅੰਤਰ ਦੀ ਜਾਂਚ ਕਰਦਿਆਂ NVMe ਡਾਟਾ ਡਿਸਕ ਨਾ ਮਿਟਾਓ।

ਸੋਧਣ ਤੋਂ ਪਹਿਲਾਂ HTTP ਫ਼ਾਈਲ ਦੀ ਨਕਲ ਕਰੋ:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

ਕਮਾਂਡ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਰੁਕੋ। ਉਸੇ ਨਾਂ ਵਾਲੀ ਪੁਰਾਣੀ ਰਿਕਵਰੀ ਨਕਲ ਅਣਬਦਲੀ ਰਹਿਣ ਦਿਓ। ਨਵਾਂ ਨਾਂ ਚੁਣੋ ਅਤੇ ਅੱਗੇ ਵਧਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਂਚ ਮੁੜ ਕਰੋ।

ਡੈਸ਼ਬੋਰਡ ਉਪਲਬਧ ਨਾ ਹੋਵੇ ਤਾਂ Yellow ਦਾ ਸੀਰੀਅਲ ਕੰਸੋਲ ਵਰਤੋ। [Linux ਅਤੇ macOS ਲਈ Nabu Casa ਗਾਈਡ](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) USB-C ਜੋੜ ਅਤੇ JP1 UART ਦੀ ਥਾਂ ਦਿਖਾਉਂਦੀ ਹੈ। ਆਪਣੇ ਹਾਰਡਵੇਅਰ ਲਈ CM4 ਦੀਆਂ ਹਦਾਇਤਾਂ ਮੰਨੋ।

## ਵਰਜਨ 3.1 ਲਈ ਜਾਂਚਿਆ ਹੱਲ ਲਾਗੂ ਕਰੋ {#apply-the-tested-fix-for-version-31}

ਤਰਜੀਹੀ ਤਰੀਕਾ ਅੱਪਡੇਟ ਤੋਂ ਪਹਿਲਾਂ ਵਾਲੀ ਅਨੁਕੂਲ HTTP ਫ਼ਾਈਲ ਵਰਤਣਾ ਹੈ। ਪੂਰੀ ਬਹਾਲੀ ਢੁਕਵੀਂ ਹੋਵੇ ਤਾਂ Home Assistant ਦੀ ਦਰਜ ਕੀਤੀ ਪ੍ਰਕਿਰਿਆ ਨਾਲ ਬੈਕਅੱਪ ਵਾਪਸ ਲਿਆਓ। ਇੱਕ ਫ਼ਾਈਲ ਕੱਢਦੇ ਹੋ ਤਾਂ ਚੱਲਦੀ ਫ਼ਾਈਲ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਉਸਦਾ ਸਟੋਰੇਜ ਵਰਜਨ ਅਤੇ ਸੰਭਾਲਿਆ ਲਿਸਨਰ ਪੋਰਟ ਪੱਕਾ ਕਰੋ। ਅਨੁਕੂਲ HTTP ਫ਼ਾਈਲ ਨਾ ਹੋਣ ਉੱਤੇ ਇਸ Yellow ਲਈ ਹੇਠਲੀਆਂ ਕਮਾਂਡਾਂ ਸਿੱਧਾ ਜਾਂਚਿਆ ਹੱਲ ਸਨ।

[ਇਸ਼ੂ ਦਾ ਮੁੱਢਲਾ ਵਿਕਲਪੀ ਹੱਲ](https://github.com/home-assistant/core/issues/190583) `.storage/http` ਨੂੰ ਪਾਸੇ ਕਰਦਾ ਹੈ ਅਤੇ ਪੁਰਾਣੇ Core ਨੂੰ ਨਵੀਂ ਫ਼ਾਈਲ ਬਣਾਉਣ ਦਿੰਦਾ ਹੈ। ਬਾਅਦ ਦੀ [Yellow ਰਿਪੋਰਟ](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) ਮੁੜ ਬਣੀ ਫ਼ਾਈਲ ਵਿੱਚ ਵੱਖਰਾ ਲਿਸਨਰ ਪੋਰਟ ਦਿਖਾਉਂਦੀ ਹੈ। ਵੈੱਬ ਇੰਟਰਫੇਸ ਠੀਕ ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ ਨਵੀਂ ਫ਼ਾਈਲ ਅਤੇ `ha core info` ਜਾਂਚੋ।

ਮੇਰੀ ਇੰਸਟਾਲੇਸ਼ਨ ਵਿੱਚ `http:` YAML ਬਲਾਕ, ਲੰਬਿਤ HTTP ਕਨਫ਼ਿਗਰੇਸ਼ਨ, ਜਾਂ ਸਥਿਰ ਸੈਟਿੰਗਾਂ ਵਿੱਚ TLS ਸਰਟੀਫਿਕੇਟ ਜਾਂ ਕੁੰਜੀ ਨਹੀਂ ਸੀ। ਸੰਭਾਲੀ ਪ੍ਰੋਫ਼ਾਈਲ `intermediate_v6` ਸੀ। ਇਸ ਸੀਮਿਤ ਹਾਲਤ ਵਿੱਚ ਮੈਂ ਵੱਖਰਾ ਵਰਜਨ 2.2 ਉਮੀਦਵਾਰ ਬਣਾਇਆ ਅਤੇ ਮੌਜੂਦਾ ਲਿਸਨਰ ਪੋਰਟ ਰੱਖਿਆ:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

ਚੱਲਦੀ ਫ਼ਾਈਲ ਬਦਲਣ ਤੋਂ ਪਹਿਲਾਂ ਉਪਰਲੀਆਂ ਸਾਰੀਆਂ ਕਮਾਂਡਾਂ ਸਫਲ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ। `jq` ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ ਉਮੀਦਵਾਰ ਮਿਟਾ ਕੇ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਉਸਦੀ ਜਾਂਚ ਕਰੋ। [Core 2026.10.4 ਦਾ HTTP ਸਰੋਤ](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) ਸਟੋਰੇਜ ਵਰਜਨ 2.2 ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਅਤੇ `intermediate` ਪ੍ਰੋਫ਼ਾਈਲ ਸਵੀਕਾਰਦਾ ਹੈ। [Core 2026.11.1 ਦਾ ਸਰੋਤ](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) ਵਰਜਨ 3.1 ਅਤੇ ਵਰਜਨ ਵਾਲੇ ਪ੍ਰੋਫ਼ਾਈਲ ਨਾਂ ਵਰਤਦਾ ਹੈ। ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਮੈਂ ਉਮੀਦਵਾਰ ਨੂੰ ਇੰਸਟਾਲ ਕੀਤੇ ਪੁਰਾਣੇ Core ਦੇ `HTTP_STORAGE_SCHEMA` ਨਾਲ ਵੀ ਜਾਂਚਿਆ।

ਕੰਟੇਨਰ ਚੱਲਦਾ ਹੋਵੇ ਤਾਂ ਇੰਸਟਾਲ ਕੀਤੇ ਪੁਰਾਣੇ Core ਦੀ ਸਕੀਮਾ ਜਾਂਚ ਚਲਾਓ:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

ਸਕੀਮਾ ਉਮੀਦਵਾਰ ਰੱਦ ਕਰੇ ਤਾਂ ਰੁਕੋ। ਇਹ ਕਦਮ ਹਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਜਾਂ HTTP ਸਟੋਰ ਦੇ ਅਣਜਾਂਚੇ ਰੂਪ ਦੀ ਪੁਸ਼ਟੀ ਨਹੀਂ ਕਰਦਾ।

ਇਸ ਉਮੀਦਵਾਰ ਲਈ ਸਕੀਮਾ ਜਾਂਚ ਨੇ `Schema accepted` ਛਾਪਿਆ। ਹੋਰ ਕੋਈ ਨਤੀਜਾ ਆਵੇ ਤਾਂ ਇਹ ਰਿਕਵਰੀ ਤਰੀਕਾ ਰੋਕੋ।

ਇਹ ਹੱਥੀਂ ਕੀਤਾ ਰੂਪਾਂਤਰਨ ਦੱਸੇ ਫ਼ੀਲਡਾਂ ਲਈ ਜਾਂਚਿਆ ਗਿਆ ਸੀ। TLS ਸੈਟਿੰਗਾਂ, ਭਰੋਸੇਯੋਗ ਪ੍ਰੌਕਸੀ ਜਾਂ ਲੰਬਿਤ ਕਨਫ਼ਿਗਰੇਸ਼ਨ ਵਾਲੀ ਫ਼ਾਈਲ ਦੀ ਵੱਖਰੀ ਜਾਂਚ ਲੋੜੀਂਦੀ ਹੈ। ਸਿਰਫ਼ ਉੱਪਰਲਾ ਵਰਜਨ ਨੰਬਰ ਬਦਲਣ ਨਾਲ ਅਜਿਹੀ ਪ੍ਰੋਫ਼ਾਈਲ ਬਚਦੀ ਹੈ ਜਿਸਨੂੰ ਪੁਰਾਣਾ Core ਸਵੀਕਾਰ ਨਹੀਂ ਕਰਦਾ।

ਮੇਰੇ ਕੇਸ ਵਿੱਚ Supervisor ਕੋਲ Core ਦਾ ਸਰਗਰਮ ਕੰਮ ਸੀ ਅਤੇ ਉਸਨੇ `ha core stop` ਰੱਦ ਕਰ ਦਿੱਤਾ। ਮੈਂ ਹੋਸਟ ਕੰਸੋਲ ਤੋਂ Core ਕੰਟੇਨਰ ਰੋਕਿਆ, ਜਾਂਚਿਆ ਉਮੀਦਵਾਰ ਇੰਸਟਾਲ ਕੀਤਾ ਅਤੇ ਫਿਰ ਚਾਲੂ ਕੀਤਾ:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

ਰੋਕਣ ਮਗਰੋਂ ਕੋਈ ਕਮਾਂਡ ਫੇਲ੍ਹ ਹੋਵੇ ਤਾਂ `docker start homeassistant` ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸਰਗਰਮ HTTP ਫ਼ਾਈਲ ਜਾਂਚੋ। ਫ਼ਾਈਲ ਬਦਲੀ ਹੋਵੇ ਤਾਂ ਉਸਦੀ ਨਵੀਂ ਸਮੱਗਰੀ ਤੋਂ ਉਮੀਦਵਾਰ ਮੁੜ ਬਣਾਓ। ਇਸ ਕਦਮ ਮਗਰੋਂ HTTP ਪੰਨਾ ਵਾਪਸ ਆ ਗਿਆ। HTTP ਜਵਾਬ ਇਕੱਲਾ Core ਦਾ ਸਟਾਰਟਅੱਪ ਪੂਰਾ ਹੋਣ ਦਾ ਸਬੂਤ ਨਹੀਂ ਸੀ, ਇਸ ਲਈ ਸਿਸਟਮ ਨੂੰ ਬਹਾਲ ਮੰਨਣ ਤੋਂ ਪਹਿਲਾਂ ਮੈਂ Supervisor ਦੀ ਹਾਲਤ ਜਾਂਚੀ।

ਇਸ Yellow ਉੱਤੇ `docker inspect -f '{{.State.Status}}' homeassistant` ਨੇ ਫਿਰ `running` ਦਿਖਾਇਆ। ਅਗਲਾ ਅੱਪਡੇਟ ਮੰਗਣ ਤੋਂ ਪਹਿਲਾਂ `ha core info` ਅਤੇ ਡੈਸ਼ਬੋਰਡ ਜਾਂਚੋ।

## ਅੱਪਡੇਟ ਦਾ ਨਤੀਜਾ ਜਾਂਚੋ {#verify-the-update-outcome}

HTTP ਪਹੁੰਚ ਵਾਪਸ ਆਉਣ ਮਗਰੋਂ ਮੈਂ Core ਨੂੰ 2026.11.1 ਉੱਤੇ ਅੱਪਡੇਟ ਕੀਤਾ। ਉਹ ਰਿਲੀਜ਼ ਮੰਗਣ ਲਈ:

```bash
ha core update --version 2026.11.1
```

ਲੰਮੇ ਸਟਾਰਟਅੱਪ ਮਗਰੋਂ ਕਮਾਂਡ ਨੇ ਅਸਫਲਤਾ ਦੱਸੀ। ਫਿਰ Supervisor ਨੇ Core ਨੂੰ RUNNING ਵਜੋਂ ਲੌਗ ਕੀਤਾ ਅਤੇ `Successfully started Home Assistant 2026.11.1` ਦਿਖਾਇਆ। ਹਾਲਤ ਵੇਖਣ ਉੱਤੇ ਇੰਸਟਾਲ ਕੀਤਾ ਰਿਲੀਜ਼ ਮੌਜੂਦਾ ਸੀ, HTTP ਫ਼ਾਈਲ ਮੁੜ ਵਰਜਨ 3.1 ਵਿੱਚ ਤਬਦੀਲ ਹੋ ਗਈ ਸੀ ਅਤੇ ਨਿਗਰਾਨੀ ਦੌਰਾਨ ਕੰਟੇਨਰ ਮੁੜ ਚਾਲੂ ਨਹੀਂ ਹੋਇਆ। ਲੌਗਇਨ ਕੀਤਾ ਡੈਸ਼ਬੋਰਡ ਖੁੱਲ੍ਹਿਆ। **ਅੱਪਡੇਟ ਕਮਾਂਡ ਅਸਫਲਤਾ ਦੱਸੇ, ਫਿਰ ਵੀ ਨਤੀਜੇ ਦੀ ਹਾਲਤ ਜਾਂਚੋ।**

ਲੰਮੇ ਅੱਪਡੇਟ ਮਗਰੋਂ ਆਪਣੇ ਸਿਸਟਮ ਵਿੱਚ ਰਿਲੀਜ਼, Supervisor ਦੀ ਸਿਹਤ ਅਤੇ ਕੰਟੇਨਰ ਦੀ ਹਾਲਤ ਜਾਂਚੋ:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

ਇਸ ਕੇਸ ਵਿੱਚ ਪਹਿਲੀ ਅਤੇ ਤੀਜੀ ਕਮਾਂਡ ਨੇ ਇਹ ਨਿੱਜੀ ਜਾਣਕਾਰੀ ਹਟਾਏ ਨਤੀਜੇ ਦਿੱਤੇ:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

ਫਿਰ ਆਪਣੇ ਆਮ ਸਥਾਨਕ ਪਤੇ ਰਾਹੀਂ ਡੈਸ਼ਬੋਰਡ ਖੋਲ੍ਹੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਲਾਈਵ ਹਾਲਤਾਂ ਲੋਡ ਹੁੰਦੀਆਂ ਹਨ। ਸੰਭਾਲੀ HTTP ਫ਼ਾਈਲ ਉਦੋਂ ਤੱਕ ਰੱਖੋ ਜਦੋਂ ਤੱਕ ਅਗਲਾ ਬੈਕਅੱਪ ਪੂਰਾ ਅਤੇ ਆਮ ਕੰਮਕਾਜ ਦੀ ਪੁਸ਼ਟੀ ਨਾ ਹੋ ਜਾਵੇ।

ਮੇਰੇ Yellow ਦੇ ਸਬੂਤਾਂ ਨਾਲ ਪਹਿਲੇ ਅੱਪਡੇਟ ਦੀ ਅਸਫਲਤਾ ਦਾ ਕਾਰਨ ਸਥਾਪਤ ਨਹੀਂ ਹੋਇਆ। ਬਾਅਦਲੇ ਕੰਮ ਦੀ ਅਸਫਲਤਾ ਵਾਲੇ ਸੁਨੇਹੇ ਨੇ ਵੀ ਕਾਰਨ ਨਹੀਂ ਦੱਸਿਆ। ਇੰਸਟਾਲ ਰਿਲੀਜ਼ ਅਤੇ ਚੱਲਦਾ ਡੈਸ਼ਬੋਰਡ, ਸਿਰਫ਼ CLI ਸੁਨੇਹੇ ਨਾਲੋਂ ਨਤੀਜੇ ਦੀ ਹਾਲਤ ਦਾ ਮਜ਼ਬੂਤ ਸਬੂਤ ਹਨ, ਪਰ ਕੋਈ ਵੀ ਇਹ ਨਹੀਂ ਸਮਝਾਉਂਦਾ ਕਿ Supervisor ਨੇ ਕੰਮ ਨੂੰ ਅਸਫਲ ਕਿਉਂ ਦੱਸਿਆ।

## ਅਗਲੇ ਕਦਮ

HTTP ਸਟੋਰੇਜ ਗਲਤੀ ਰਹੇ ਤਾਂ ਸੰਭਾਲੀ ਫ਼ਾਈਲ ਜਾਂਚੋ ਅਤੇ ਅਨੁਕੂਲ ਬੈਕਅੱਪ ਬਹਾਲ ਕਰੋ ਜਾਂ Core ਦਾ ਅਜਿਹਾ ਰਿਲੀਜ਼ ਚਲਾਓ ਜੋ ਉਸ ਸਟੋਰੇਜ ਵਰਜਨ ਨੂੰ ਪੜ੍ਹ ਸਕੇ। ਪੁਰਾਣੇ Core ਹੇਠ ਸੰਭਾਲੀ ਵਰਜਨ 3 ਫ਼ਾਈਲ ਵਾਪਸ ਰੱਖਣ ਨਾਲ ਖ਼ਰਾਬੀ ਦੁਹਰਾਏਗੀ। Core RUNNING ਤੱਕ ਪਹੁੰਚੇ ਪਰ ਕੁਝ ਡਿਵਾਈਸ ਉਪਲਬਧ ਨਾ ਹੋਣ ਤਾਂ ਉਹਨਾਂ ਇੰਟੀਗ੍ਰੇਸ਼ਨਾਂ ਦੀ ਵੱਖਰੇ ਤੌਰ ਤੇ ਜਾਂਚ ਕਰੋ। ਅਗਲਾ ਬੈਕਅੱਪ ਪੂਰਾ ਹੋਣ ਅਤੇ ਡੈਸ਼ਬੋਰਡ ਜਵਾਬ ਦਿੰਦਾ ਰਹਿਣ ਤੱਕ ਰਿਕਵਰੀ ਕਾਪੀ ਅਤੇ ਕਲਾਉਡ ਬੈਕਅੱਪ ਸੰਭਾਲੋ।
