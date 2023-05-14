---
title: "ChromiumADMX: Chromium ਬ੍ਰਾਊਜ਼ਰ ਲਈ ਸਹੀ ADMX ਟੈਮਪਲੇਟ"
date: 2020-07-25
---


Chromium ਬ੍ਰਾਊਜ਼ਰ ਲਈ ਸਹੀ ADMX ਟੈਮਪਲੇਟ

Chromium, ਇੱਕ ਕੰਪਨੀ ਦੇ ਰੂਪ ਵਿੱਚ, Chromium ਬ੍ਰਾਊਜ਼ਰ ਲਈ ADMX ਟੈਂਪਲੇਟਾਂ ਨੂੰ ਜਾਰੀ ਕਰਨ ਵਿੱਚ ਅਸਫਲ ਰਿਹਾ ਹੈ ਜੋ Google Chrome ਟੈਂਪਲੇਟਸ ਦੇ ਨਾਲ ਹੀ ਸਥਾਪਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।
ਇਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਅਸੀਂ Chromium ਬ੍ਰਾਊਜ਼ਰ ਦੇ ਰਜਿਸਟਰੀ ਮਾਰਗ ਨੂੰ ਦਰਸਾਉਣ ਲਈ Google Chrome ADMX ਟੈਂਪਲੇਟਾਂ ਨੂੰ ਸੋਧਿਆ ਹੈ ਅਤੇ GPO ਵਿੱਚ Google ADMX ਫੋਲਡਰ ਵਿੱਚ ਟੈਂਡਮ ਵਿੱਚ ਰੱਖਿਆ ਹੈ।

**ਇਹ ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਪ੍ਰੀ-ਅਲਫ਼ਾ ਅਵਸਥਾ ਵਿੱਚ ਹਨ। ਉਹਨਾਂ ਦੀ ਵਰਤੋਂ ਸਿਰਫ ਜਾਂਚ ਦੇ ਉਦੇਸ਼ਾਂ ਲਈ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ**

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ

** ਤੋਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## ਨੋਟਸ

Google Chrome ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਨੂੰ ਇਸ ਅਨੁਸਾਰ ਸੋਧਿਆ ਗਿਆ:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**ਨੋਟ:** "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" ਨੂੰ "HKEY_LOCAL_MACHINE\Software\Policies\Chromium" ਨਾਲ ਬਦਲਿਆ ਗਿਆ

**ਨੋਟ:** ਇੱਕੋ ਸਮੇਂ 'ਤੇ SOS'es Chromium ਅਤੇ Brave Browser ADMX ਟੈਂਪਲੇਟਸ ਨੂੰ ਸਥਾਪਿਤ ਨਾ ਕਰੋ।

## ਕਿਵੇਂ ਇੰਸਟਾਲ ਕਰਨਾ ਹੈ

1.) readme.md ਨੂੰ ਛੱਡ ਕੇ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਨੂੰ "C:\Windows\PolicyDefinitions" ਅਤੇ/ਜਾਂ "\\\domain.tld\domain\Policies\PolicyDefinitions" ਵਿੱਚ ਕਾਪੀ ਕਰੋ।

2.) ਲਾਭ?




