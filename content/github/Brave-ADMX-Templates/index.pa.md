---
title: "BraveADMX - ਸੰਸ਼ੋਧਿਤ ADMX ਟੈਂਪਲੇਟਸ ਨਾਲ ਬਹਾਦਰ ਬ੍ਰਾਊਜ਼ਰ ਨੀਤੀਆਂ ਦਾ ਨਿਯੰਤਰਣ ਲਓ"
date: 2020-07-25
---


ਬ੍ਰੇਵ, ਇੱਕ ਕੰਪਨੀ ਦੇ ਰੂਪ ਵਿੱਚ, ਸਿਰਫ਼ ਸਮਰਥਿਤ ਵਿਕਲਪ ਵਜੋਂ ਸ਼ੁੱਧ ਰਜਿਸਟਰੀਆਂ ਨੂੰ ਅੱਗੇ ਵਧਾਉਣ ਵਾਲੇ ਬਹਾਦਰ ਬ੍ਰਾਊਜ਼ਰ ਸਾਈਟਿੰਗ ਲਈ ADMX ਟੈਂਪਲੇਟਾਂ ਨੂੰ ਜਾਰੀ ਕਰਨ ਵਿੱਚ ਅਸਫਲ ਰਿਹਾ ਹੈ।
ਜਿਵੇਂ ਕਿ ਬ੍ਰੇਵ ਬ੍ਰਾਊਜ਼ਰ ਕ੍ਰੋਮੀਅਮ ਤੋਂ ਬਣਿਆ ਹੋਇਆ ਹੈ, ਇਸ ਨੂੰ ਕ੍ਰੋਮੀਅਮ ਅਤੇ ਗੂਗਲ ਕਰੋਮ ADMX ਟੈਂਪਲੇਟਸ ਦੀਆਂ ਸਭ ਤੋਂ ਵੱਧ, ਜੇ ਸਾਰੀਆਂ ਨਹੀਂ, ਤਾਂ ਇੱਕੋ ਜਿਹੀਆਂ ਨੀਤੀਆਂ ਦਾ ਸਮਰਥਨ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।
ਇਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਅਸੀਂ ਬ੍ਰੇਵ ਬ੍ਰਾਊਜ਼ਰ ਦੇ ਰਜਿਸਟਰੀ ਮਾਰਗ ਨੂੰ ਦਰਸਾਉਣ ਲਈ Google Chrome ADMX ਟੈਂਪਲੇਟਸ ਨੂੰ ਸੰਸ਼ੋਧਿਤ ਕੀਤਾ ਹੈ। ਕੁਝ ਸ਼ੁਰੂਆਤੀ ਸਮੱਸਿਆ-ਨਿਪਟਾਰਾ ਅਤੇ ਟੈਸਟਿੰਗ ਤੋਂ ਬਾਅਦ, ਟੈਂਪਲੇਟਸ ਕੰਮ ਕਰਦੇ ਜਾਪਦੇ ਹਨ।

**ਇਹ ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਪ੍ਰੀ-ਅਲਫ਼ਾ ਅਵਸਥਾ ਵਿੱਚ ਹਨ। ਉਹਨਾਂ ਦੀ ਵਰਤੋਂ ਸਿਰਫ ਜਾਂਚ ਦੇ ਉਦੇਸ਼ਾਂ ਲਈ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ**

## ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਨੂੰ ਡਾਉਨਲੋਡ ਕਰੋ।

** ਤੋਂ ਲੋੜੀਂਦੀਆਂ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## ਨੋਟਸ

Google Chrome ਨੀਤੀ ਪਰਿਭਾਸ਼ਾਵਾਂ ਨੂੰ ਇਸ ਅਨੁਸਾਰ ਸੋਧਿਆ ਗਿਆ:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**ਨੋਟ:** "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" ਨੂੰ "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave" ਨਾਲ ਬਦਲਿਆ ਗਿਆ

**ਨੋਟ:** ਇੱਕੋ ਸਮੇਂ 'ਤੇ SOS'es Chromium ਅਤੇ Brave Browser ADMX ਟੈਂਪਲੇਟਸ ਨੂੰ ਸਥਾਪਿਤ ਨਾ ਕਰੋ।

## ਕਿਵੇਂ ਇੰਸਟਾਲ ਕਰਨਾ ਹੈ

1.) readme.md ਨੂੰ ਛੱਡ ਕੇ ਸਾਰੀਆਂ ਫਾਈਲਾਂ ਨੂੰ "C:\Windows\PolicyDefinitions" ਅਤੇ/ਜਾਂ "\\\domain.tld\domain\Policies\PolicyDefinitions" ਵਿੱਚ ਕਾਪੀ ਕਰੋ।

2.) ਲਾਭ?