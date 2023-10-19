---
title: "ਵਿੰਡੋਜ਼-ਓਪਟੀਮਾਈਜ਼-ਹਾਰਡਨ-ਡੈਬਲੋਟ ਸਕ੍ਰਿਪਟ ਨਾਲ ਆਪਣੇ ਵਿੰਡੋਜ਼ ਸਿਸਟਮ ਨੂੰ ਅਨੁਕੂਲਿਤ ਅਤੇ ਸਖ਼ਤ ਕਰੋ"
date: 2020-12-29
toc: true
draft: false
description: "ਇਹ ਵਿਆਪਕ ਗਾਈਡ ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ, ਸੁਰੱਖਿਆ, ਅਤੇ ਗੋਪਨੀਯਤਾ ਲਈ ਤੁਹਾਡੇ ਵਿੰਡੋਜ਼ ਸਿਸਟਮ ਨੂੰ ਕਿਵੇਂ ਅਨੁਕੂਲ ਬਣਾਉਣ, ਸਖ਼ਤ ਅਤੇ ਡੀਬਲੋਟ ਕਰਨ ਬਾਰੇ ਕਦਮ-ਦਰ-ਕਦਮ ਨਿਰਦੇਸ਼ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ।"
tags: ["ਵਿੰਡੋਜ਼ ਓਪਟੀਮਾਈਜੇਸ਼ਨ", "ਵਿੰਡੋਜ਼ ਨੂੰ ਸਖਤ ਕਰਨਾ", "ਵਿੰਡੋਜ਼ ਡੀਬਲੋਟਿੰਗ", "ਵਿੰਡੋਜ਼ ਸੁਰੱਖਿਆ", "ਵਿੰਡੋਜ਼ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ", "ਵਿੰਡੋਜ਼ ਗੋਪਨੀਯਤਾ", "ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ", "ਸਮੂਹ ਨੀਤੀ ਆਬਜੈਕਟ", "ਅਡੋਬ ਐਕਰੋਬੈਟ ਰੀਡਰ", "ਫਾਇਰਫਾਕਸ", "ਗੂਗਲ ਕਰੋਮ", "ਇੰਟਰਨੈੱਟ ਐਕਸਪਲੋਰਰ", "Microsoft Chromium Edge", "ਡਾਟ ਨੈੱਟ 4", "ਮਾਈਕ੍ਰੋਸਾਫਟ ਆਫਿਸ", "Onedrive", "Oracle Java JRE 8", "ਵਿੰਡੋਜ਼ ਫਾਇਰਵਾਲ", "ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ", "ਅਪਲੋਕਰ"]
---
 ਜਾਣ-ਪਛਾਣ:

ਵਿੰਡੋਜ਼ 10 ਅਤੇ ਵਿੰਡੋਜ਼ 11 ਬਾਕਸ ਤੋਂ ਬਾਹਰ ਹਮਲਾਵਰ ਅਤੇ ਅਸੁਰੱਖਿਅਤ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਹਨ।
ਵਰਗੀਆਂ ਸੰਸਥਾਵਾਂ[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) ਨੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਨੂੰ ਲੌਕਡਾਊਨ, ਸਖ਼ਤ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਹੈ। ਇਹ ਤਬਦੀਲੀਆਂ ਟੈਲੀਮੈਟਰੀ ਨੂੰ ਰੋਕਣਾ, ਮੈਕਰੋਜ਼ ਨੂੰ ਰੋਕਣਾ, ਬਲੋਟਵੇਅਰ ਨੂੰ ਹਟਾਉਣਾ, ਅਤੇ ਸਿਸਟਮ ਉੱਤੇ ਬਹੁਤ ਸਾਰੇ ਡਿਜੀਟਲ ਅਤੇ ਭੌਤਿਕ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣਾ ਸਮੇਤ ਬਹੁਤ ਸਾਰੀਆਂ ਕਮੀਆਂ ਨੂੰ ਕਵਰ ਕਰਦਾ ਹੈ। ਇਸ ਸਕ੍ਰਿਪਟ ਦਾ ਉਦੇਸ਼ ਉਹਨਾਂ ਸੰਸਥਾਵਾਂ ਦੁਆਰਾ ਸਿਫ਼ਾਰਿਸ਼ ਕੀਤੀਆਂ ਸੰਰਚਨਾਵਾਂ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ ਹੈ।

## ਨੋਟਸ, ਚੇਤਾਵਨੀਆਂ ਅਤੇ ਵਿਚਾਰ:

**ਚੇਤਾਵਨੀ:**

ਇਹ ਸਕ੍ਰਿਪਟ ਜ਼ਿਆਦਾਤਰ, ਜੇਕਰ ਸਾਰੇ ਨਹੀਂ, ਬਿਨਾਂ ਸਮੱਸਿਆ ਵਾਲੇ ਸਿਸਟਮਾਂ ਲਈ ਕੰਮ ਕਰੇਗੀ। ਜਦਕਿ[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- ਇਹ ਸਕ੍ਰਿਪਟ ਮੁੱਖ ਤੌਰ 'ਤੇ **ਨਿੱਜੀ ਵਰਤੋਂ** ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਕੰਮ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਕੁਝ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਕੌਂਫਿਗਰੇਸ਼ਨ ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਇਹ ਸਕ੍ਰਿਪਟ ਇੱਕ ਸਿਸਟਮ ਨੂੰ 100% ਅਨੁਪਾਲਨ ਵਿੱਚ ਲਿਆਉਣ ਲਈ ਤਿਆਰ ਨਹੀਂ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਦੀ ਬਜਾਏ ਇਸਨੂੰ ਜ਼ਿਆਦਾਤਰ ਪੂਰਾ ਕਰਨ ਲਈ ਇੱਕ ਸਟੈਪਿੰਗ ਸਟੋਨ ਵਜੋਂ ਵਰਤਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੇ ਸਭ ਨਹੀਂ, ਤਾਂ ਸੰਰਚਨਾ ਤਬਦੀਲੀਆਂ ਜੋ ਕਿ ਬ੍ਰਾਂਡਿੰਗ ਅਤੇ ਬੈਨਰਾਂ ਵਰਗੇ ਪੁਰਾਣੇ ਮੁੱਦਿਆਂ ਨੂੰ ਛੱਡਣ ਵੇਲੇ ਸਕ੍ਰਿਪਟ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ ਜਿੱਥੇ ਉਹਨਾਂ ਨੂੰ ਸਖਤ ਨਿੱਜੀ ਵਰਤੋਂ ਵਾਲੇ ਮਾਹੌਲ ਵਿੱਚ ਵੀ ਲਾਗੂ ਨਹੀਂ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।
- ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਡਿਜ਼ਾਇਨ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਕੁਝ ਹੋਰ ਸਕ੍ਰਿਪਟਾਂ ਦੇ ਉਲਟ ਓਪਟੀਮਾਈਜੇਸ਼ਨ, ਕੋਰ ਵਿੰਡੋਜ਼ ਕਾਰਜਕੁਸ਼ਲਤਾ ਨੂੰ ਨਹੀਂ ਤੋੜਨਗੀਆਂ।
- ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ, ਵਿੰਡੋਜ਼ ਡਿਫੈਂਡਰ, ਵਿੰਡੋਜ਼ ਸਟੋਰ, ਅਤੇ ਕੋਰਟੋਨਾ ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ ਪ੍ਰਤਿਬੰਧਿਤ ਕਰ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਪਰ ਜ਼ਿਆਦਾਤਰ ਹੋਰ ਵਿੰਡੋਜ਼ 10 ਗੋਪਨੀਯਤਾ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਨ ਵਾਲੀ ਸਥਿਤੀ ਵਿੱਚ ਨਹੀਂ ਹਨ।
- ਜੇਕਰ ਤੁਸੀਂ ਸਿਰਫ਼ ਵਪਾਰਕ ਵਾਤਾਵਰਣਾਂ ਨੂੰ ਨਿਸ਼ਾਨਾ ਬਣਾਉਣ ਵਾਲੀ ਇੱਕ ਛੋਟੀ ਜਿਹੀ ਸਕ੍ਰਿਪਟ ਦੀ ਭਾਲ ਕਰਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਦੇਖੋ[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਨਾ ਚਲਾਓ ਜੇਕਰ ਤੁਸੀਂ ਇਹ ਨਹੀਂ ਸਮਝਦੇ ਕਿ ਇਹ ਕੀ ਕਰਦੀ ਹੈ। ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਸ ਦੀ ਸਮੀਖਿਆ ਅਤੇ ਜਾਂਚ ਕਰਨਾ ਤੁਹਾਡੀ ਜ਼ਿੰਮੇਵਾਰੀ ਹੈ।**

**ਉਦਾਹਰਣ ਲਈ, ਜੇਕਰ ਤੁਸੀਂ ਰੋਕਥਾਮ ਵਾਲੇ ਕਦਮ ਚੁੱਕੇ ਬਿਨਾਂ ਇਸਨੂੰ ਚਲਾਉਂਦੇ ਹੋ ਤਾਂ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਗੱਲਾਂ ਟੁੱਟ ਜਾਣਗੀਆਂ:**

- "ਪ੍ਰਸ਼ਾਸਕ" ਨਾਮਕ ਡਿਫੌਲਟ ਪ੍ਰਸ਼ਾਸਕ ਖਾਤੇ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਅਯੋਗ ਹੈ ਅਤੇ DoD STIG ਪ੍ਰਤੀ ਨਾਮ ਬਦਲਿਆ ਗਿਆ ਹੈ

  - ਬਣਾਏ ਗਏ ਡਿਫੌਲਟ ਖਾਤੇ 'ਤੇ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦਾ ਪਰ ਇਹ ਡਿਫੌਲਟ ਐਡਮਿਨਿਸਟ੍ਰੇਟਰ ਖਾਤੇ ਦੀ ਵਰਤੋਂ ਕਰਨ 'ਤੇ ਲਾਗੂ ਹੁੰਦਾ ਹੈ ਜੋ ਅਕਸਰ ਐਂਟਰਪ੍ਰਾਈਜ਼, IOT, ਅਤੇ ਵਿੰਡੋਜ਼ ਸਰਵਰ ਸੰਸਕਰਣਾਂ 'ਤੇ ਪਾਇਆ ਜਾਂਦਾ ਹੈ।

  - ਕੰਪਿਊਟਰ ਮੈਨੇਜਮੈਂਟ ਦੇ ਤਹਿਤ ਇੱਕ ਨਵਾਂ ਖਾਤਾ ਬਣਾਓ ਅਤੇ ਜੇਕਰ ਤੁਸੀਂ ਚਾਹੋ ਤਾਂ ਇਸਨੂੰ ਪ੍ਰਸ਼ਾਸਕ ਵਜੋਂ ਸੈਟ ਕਰੋ। ਫਿਰ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਸ ਬਾਰੇ ਕੰਮ ਕਰਨ ਲਈ ਪਹਿਲੀ ਵਾਰ ਨਵੇਂ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸਾਈਨ ਇਨ ਕਰਨ ਤੋਂ ਬਾਅਦ ਪਿਛਲੇ ਉਪਭੋਗਤਾ ਫੋਲਡਰ ਦੀਆਂ ਸਮੱਗਰੀਆਂ ਨੂੰ ਨਵੇਂ ਵਿੱਚ ਕਾਪੀ ਕਰੋ।

- ਮਾਈਕ੍ਰੋਸਾਫਟ ਖਾਤੇ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਾਈਨ ਇਨ ਕਰਨਾ DoD STIG ਪ੍ਰਤੀ ਅਸਮਰੱਥ ਹੈ।

  - ਸੁਰੱਖਿਅਤ ਅਤੇ ਨਿੱਜੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਸਮੇਂ, Microsoft ਖਾਤੇ ਰਾਹੀਂ ਆਪਣੇ ਸਥਾਨਕ ਖਾਤੇ ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰਨ ਦੀ ਸਲਾਹ ਨਹੀਂ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਇਸ ਰੈਪੋ ਦੁਆਰਾ ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ।

  - ਕੰਪਿਊਟਰ ਮੈਨੇਜਮੈਂਟ ਦੇ ਤਹਿਤ ਇੱਕ ਨਵਾਂ ਖਾਤਾ ਬਣਾਓ ਅਤੇ ਜੇਕਰ ਤੁਸੀਂ ਚਾਹੋ ਤਾਂ ਇਸਨੂੰ ਪ੍ਰਸ਼ਾਸਕ ਵਜੋਂ ਸੈਟ ਕਰੋ। ਫਿਰ ਸਕ੍ਰਿਪਟ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਸ ਬਾਰੇ ਕੰਮ ਕਰਨ ਲਈ ਪਹਿਲੀ ਵਾਰ ਨਵੇਂ ਉਪਭੋਗਤਾ ਦੁਆਰਾ ਸਾਈਨ ਇਨ ਕਰਨ ਤੋਂ ਬਾਅਦ ਪਿਛਲੇ ਉਪਭੋਗਤਾ ਫੋਲਡਰ ਦੀਆਂ ਸਮੱਗਰੀਆਂ ਨੂੰ ਨਵੇਂ ਵਿੱਚ ਕਾਪੀ ਕਰੋ।

- ਖਾਤਾ ਪਿੰਨ ਪ੍ਰਤੀ DoD STIG ਅਯੋਗ ਹਨ

  - ਪਿੰਨ ਅਸੁਰੱਖਿਅਤ ਹੁੰਦੇ ਹਨ ਜਦੋਂ ਸਿਰਫ਼ ਪਾਸਵਰਡ ਦੀ ਥਾਂ 'ਤੇ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਘੰਟਿਆਂ ਜਾਂ ਸੰਭਾਵਤ ਤੌਰ 'ਤੇ ਸਕਿੰਟਾਂ ਜਾਂ ਮਿੰਟਾਂ ਵਿੱਚ ਆਸਾਨੀ ਨਾਲ ਬਾਈਪਾਸ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ

  - ਖਾਤੇ ਤੋਂ ਪਿੰਨ ਨੂੰ ਹਟਾਓ ਅਤੇ/ਜਾਂ ਸਕ੍ਰਿਪਟ ਚਲਾਉਣ ਤੋਂ ਬਾਅਦ ਪਾਸਵਰਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਾਈਨ ਇਨ ਕਰੋ।

- ਬਿਟਲਾਕਰ ਡਿਫੌਲਟ ਬਦਲੇ ਗਏ ਹਨ ਅਤੇ DoD STIG ਦੇ ਕਾਰਨ ਸਖ਼ਤ ਹੋ ਗਏ ਹਨ।

  - ਬਿਟਲਾਕਰ ਨੂੰ ਕਿਵੇਂ ਲਾਗੂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜਦੋਂ ਇਹ ਤਬਦੀਲੀਆਂ ਹੁੰਦੀਆਂ ਹਨ ਅਤੇ ਜੇਕਰ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਬਿਟਲਾਕਰ ਸਮਰਥਿਤ ਕੀਤਾ ਹੋਇਆ ਹੈ ਤਾਂ ਇਹ ਬਿਟਲਾਕਰ ਲਾਗੂਕਰਨ ਨੂੰ ਤੋੜ ਦੇਵੇਗਾ।

  - ਬਿਟਲੌਕਰ ਨੂੰ ਅਸਮਰੱਥ ਬਣਾਓ, ਸਕ੍ਰਿਪਟ ਚਲਾਓ, ਫਿਰ ਇਸ ਮੁੱਦੇ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਬਿਟਲੌਕਰ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰੋ।

## ਲੋੜਾਂ:

- [x] ਵਿੰਡੋਜ਼ 10/11 ਐਂਟਰਪ੍ਰਾਈਜ਼ (**ਪਸੰਦੀਦਾ**) ਜਾਂ ਪੇਸ਼ੇਵਰ
  - Windows 10/11 ਹੋਮ ਐਡੀਸ਼ਨ GPO ਸੰਰਚਨਾ ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ ਹਨ ਅਤੇ ਟੈਸਟ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
  - ਵਿੰਡੋ "ਐਨ" ਐਡੀਸ਼ਨ ਦੀ ਜਾਂਚ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ।
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) ਇੱਕ ਬਹੁਤ ਹੀ ਸੁਰੱਖਿਅਤ Windows 10 ਡਿਵਾਈਸ ਲਈ
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - ਚਲਾਓ[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) ਨਵੀਨਤਮ ਮੁੱਖ ਰੀਲੀਜ਼ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਅਤੇ ਤਸਦੀਕ ਕਰਨ ਲਈ।
- [x] ਇਸ ਸਕ੍ਰਿਪਟ ਨੂੰ ਲਾਗੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਬਿਟਲੌਕਰ ਨੂੰ ਮੁਅੱਤਲ ਜਾਂ ਬੰਦ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸਨੂੰ ਰੀਬੂਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਦੁਬਾਰਾ ਚਾਲੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।
  - ਇਸ ਸਕ੍ਰਿਪਟ ਦੇ ਫਾਲੋ-ਅਪ ਰਨ ਬਿਟਲਾਕਰ ਨੂੰ ਅਯੋਗ ਕੀਤੇ ਬਿਨਾਂ ਚਲਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।
- [x] ਹਾਰਡਵੇਅਰ ਲੋੜਾਂ
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## ਸਿਫਾਰਸ਼ੀ ਪੜ੍ਹਨ ਸਮੱਗਰੀ:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## ਜੋੜ, ਧਿਆਨ ਦੇਣ ਯੋਗ ਤਬਦੀਲੀਆਂ, ਅਤੇ ਬੱਗ ਫਿਕਸ:

**ਇਹ ਸਕ੍ਰਿਪਟ ਤੁਹਾਡੇ ਸਿਸਟਮ 'ਤੇ ਸੈਟਿੰਗਾਂ ਨੂੰ ਜੋੜਦੀ, ਹਟਾਉਂਦੀ ਅਤੇ ਬਦਲਦੀ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸਕ੍ਰਿਪਟ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।**

### ਬ੍ਰਾਊਜ਼ਰ:

- ਬ੍ਰਾਊਜ਼ਰਾਂ ਵਿੱਚ ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਵਿੱਚ ਸਹਾਇਤਾ ਲਈ ਵਾਧੂ ਐਕਸਟੈਂਸ਼ਨਾਂ ਸਥਾਪਤ ਕੀਤੀਆਂ ਜਾਣਗੀਆਂ।
  - ਵੇਖੋ[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) ਵਾਧੂ ਜਾਣਕਾਰੀ ਲਈ।
- ਬ੍ਰਾਊਜ਼ਰਾਂ ਲਈ ਲਾਗੂ ਕੀਤੇ ਗਏ DoD STIGs ਦੇ ਕਾਰਨ, ਐਕਸਟੈਂਸ਼ਨ ਪ੍ਰਬੰਧਨ ਅਤੇ ਹੋਰ ਐਂਟਰਪ੍ਰਾਈਜ਼ ਸੈਟਿੰਗਾਂ ਸੈੱਟ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ। ਇਹਨਾਂ ਵਿਕਲਪਾਂ ਨੂੰ ਕਿਵੇਂ ਵੇਖਣਾ ਹੈ ਇਸ ਬਾਰੇ ਹਦਾਇਤਾਂ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ GPO ਨਿਰਦੇਸ਼ਾਂ ਨੂੰ ਦੇਖਣ ਦੀ ਲੋੜ ਪਵੇਗੀ।

### ਪਾਵਰਸ਼ੇਲ ਮੋਡੀਊਲ:

- PowerShell ਨੂੰ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਆਟੋਮੈਟਿਕ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) ਮੋਡੀਊਲ ਤੁਹਾਡੇ ਸਿਸਟਮ ਵਿੱਚ ਜੋੜਿਆ ਜਾਵੇਗਾ।

### Microsoft ਖਾਤੇ, ਸਟੋਰ, ਜਾਂ Xbox ਸੇਵਾਵਾਂ ਨੂੰ ਠੀਕ ਕਰਨਾ:

ਇਹ ਇਸ ਲਈ ਹੈ ਕਿਉਂਕਿ ਅਸੀਂ ਮਾਈਕ੍ਰੋਸੌਫਟ ਖਾਤਿਆਂ ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰਨ ਨੂੰ ਬਲੌਕ ਕਰਦੇ ਹਾਂ। ਮਾਈਕ੍ਰੋਸਾੱਫਟ ਦੀ ਟੈਲੀਮੈਟਰੀ ਅਤੇ ਪਛਾਣ ਐਸੋਸੀਏਸ਼ਨ ਨੂੰ ਭੜਕਾਇਆ ਗਿਆ ਹੈ।
ਹਾਲਾਂਕਿ, ਜੇਕਰ ਤੁਸੀਂ ਅਜੇ ਵੀ ਇਹਨਾਂ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਰੈਜ਼ੋਲਿਊਸ਼ਨ ਲਈ ਨਿਮਨਲਿਖਤ ਮੁੱਦੇ ਦੀਆਂ ਟਿਕਟਾਂ ਵੇਖੋ:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### ਤੱਥਾਂ ਤੋਂ ਬਾਅਦ ਸਥਾਨਕ ਸਮੂਹ ਨੀਤੀ ਵਿੱਚ ਨੀਤੀਆਂ ਨੂੰ ਸੰਪਾਦਿਤ ਕਰਨਾ:

ਜੇਕਰ ਤੁਹਾਨੂੰ ਕਿਸੇ ਸੈਟਿੰਗ ਨੂੰ ਸੋਧਣ ਜਾਂ ਬਦਲਣ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ ਉਹ GPO ਰਾਹੀਂ ਸੰਰਚਨਾਯੋਗ ਹਨ:

- ਇਸ ਤੋਂ ADMX ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਨੂੰ ਆਯਾਤ ਕਰੋ[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) ਸਿਸਟਮ ਵਿੱਚ _C:\windows\PolicyDefinitions_ ਜਿਸ ਨੂੰ ਤੁਸੀਂ ਸੋਧਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹੋ।

- ਜਿਸ ਸਿਸਟਮ ਨੂੰ ਤੁਸੀਂ ਸੋਧਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਰਹੇ ਹੋ ਉਸ 'ਤੇ 'gpedit.msc' ਖੋਲ੍ਹੋ।

## ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਸਾਧਨਾਂ ਦੀ ਇੱਕ ਸੂਚੀ ਜੋ ਇਹ ਸੰਗ੍ਰਹਿ ਵਰਤਦਾ ਹੈ:

### ਪਹਿਲੀ ਧਿਰ:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### ਤੀਸਰਾ ਪੱਖ:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRGs ਲਾਗੂ:

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## ਇਸ ਤੋਂ ਵਧੀਕ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਵਿਚਾਰ ਕੀਤਾ ਗਿਆ ਸੀ:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## ਸਕ੍ਰਿਪਟ ਨੂੰ ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ:
### GUI - ਨਿਰਦੇਸ਼ਿਤ ਸਥਾਪਨਾ:

ਨਵੀਨਤਮ ਰੀਲੀਜ਼ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)ਉਹ ਵਿਕਲਪ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਅਤੇ ਐਗਜ਼ੀਕਿਊਟ ਦਬਾਓ। <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="ਵਿੰਡੋਜ਼-ਓਪਟੀਮਾਈਜ਼-ਹਾਰਡਨ-ਡੀਬਲੋਟ ਜੀਯੂਆਈ ਅਧਾਰਤ ਗਾਈਡਡ ਸਥਾਪਨਾ ਦੀ ਉਦਾਹਰਨ"> ### ਆਟੋਮੇਟਿਡ ਇੰਸਟੌਲ: ਆਟੋਮੈਟਿਕ ਡਾਊਨਲੋਡ ਕਰਨ, ਸਾਰੀਆਂ ਸਹਾਇਕ ਫਾਈਲਾਂ ਨੂੰ ਅਨਜ਼ਿਪ ਕਰਨ ਅਤੇ ਸਕ੍ਰਿਪਟ ਦੇ ਨਵੀਨਤਮ ਸੰਸਕਰਣ ਨੂੰ ਚਲਾਉਣ ਲਈ ਇਸ ਵਨ-ਲਾਈਨਰ ਦੀ ਵਰਤੋਂ ਕਰੋ।```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
