---
title: "HackTheBox - ਚੁਣੌਤੀ - Crypto - ਕਮਜ਼ੋਰ RSA"
draft: false
description: "ਹੈਕTheBox ਕਮਜ਼ੋਰ RSA ਕ੍ਰਿਪਟੋ ਚੁਣੌਤੀ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਹੱਲ ਕਰਨ ਲਈ ਇੱਕ ਸਵੈਚਲਿਤ RSA ਅਟੈਕ ਟੂਲ, RsaCtfTool ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸਿੱਖੋ।"
tags: ["ਹੈਕ ਬਾਕਸ","ਚੁਣੌਤੀਆਂ","ਕ੍ਰਿਪਟੋ","ਕਮਜ਼ੋਰ RSA","RsaCtfTool","HTB ਕਮਜ਼ੋਰ RSA ਕ੍ਰਿਪਟੋ","ਆਸਾਨ ਚੁਣੌਤੀ","RSA ਸਿਫਰ","flag.enc", "key.pub", "OpenSSL ਪੈਕੇਜ","ਆਟੋਮੇਟਿਡ RSA ਅਟੈਕ ਟੂਲ","ਪਾਈਥਨ ਸਕ੍ਰਿਪਟ","RsaCtfTool","python3","ਜਨਤਕ ਕੁੰਜੀ","ਅਨਸੀਫਰਫਾਈਲ","ਝੰਡੇ ਦੀ ਉਦਾਹਰਨ"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "ਇੱਕ ਕਾਰਟੂਨ ਹੈਕਰ, ਇੱਕ ਕੇਪ ਅਤੇ ਇੱਕ ਮਾਸਕ ਪਹਿਨਿਆ ਹੋਇਆ ਹੈ, ਇੱਕ ਵਾਲਟ ਦੇ ਦਰਵਾਜ਼ੇ ਦੇ ਸਾਹਮਣੇ ਖੜ੍ਹਾ ਹੈ ਜਿਸ 'ਤੇ HTB ਲੋਗੋ ਹੈ ਅਤੇ ਇੱਕ ਟੂਲ (ਜਿਵੇਂ ਕਿ ਇੱਕ ਰੈਂਚ ਜਾਂ ਇੱਕ ਸਕ੍ਰਿਊਡਰਾਈਵਰ) ਇੱਕ ਹਰੇ ਬੈਕਗ੍ਰਾਉਂਡ ਦੇ ਨਾਲ ਸਫਲਤਾ ਦਾ ਪ੍ਰਤੀਕ ਹੈ ਅਤੇ ਭਾਸ਼ਣ ਦੇ ਬੁਲਬੁਲੇ ਵਿੱਚ ਝੰਡਾ ਹੈ। ਉਨ੍ਹਾਂ ਦੇ ਸਿਰ ਦੇ ਉੱਪਰ।"
coverCaption: ""
---
 HTB ਕਮਜ਼ੋਰ RSA ਕ੍ਰਿਪਟੋ ਚੁਣੌਤੀ ਆਸਾਨੀ ਨਾਲ। RSA ਸਾਈਫਰ ਦੇ ਆਧਾਰ 'ਤੇ, ਇਸ ਆਸਾਨ ਚੁਣੌਤੀ ਲਈ RsaCtfTool ਵਰਗੇ ਸਵੈਚਲਿਤ RSA ਅਟੈਕ ਟੂਲ ਦੀ ਵਰਤੋਂ ਦੀ ਲੋੜ ਹੈ। ਇੱਕ ਸਧਾਰਨ ਕਮਾਂਡ ਦੇ ਨਾਲ ਫਲੈਗ ਪ੍ਰਾਪਤ ਕਰੋ ਅਤੇ HackTheBox ਚੁਣੌਤੀਆਂ ਦੇ ਨਾਲ ਆਪਣੇ ਕ੍ਰਿਪਟੋ ਹੁਨਰ ਦਾ ਵਿਸਤਾਰ ਕਰੋ।

______

## ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਫਾਈਲਾਂ:

**ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਫਾਈਲਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ:**
- flag.enc
- key.pub

## ਵਾਕ-ਥਰੂ:

ਪਹਿਲੀ ਨਜ਼ਰ 'ਤੇ, ਤੁਸੀਂ ਸੋਚੋਗੇ ਕਿ ਤੁਸੀਂ ਜਨਤਕ ਕੁੰਜੀ ਨਾਲ ਫਲੈਗ ਨੂੰ ਡੀਕ੍ਰਿਪਟ ਕਰ ਸਕਦੇ ਹੋ।
ਇਸਦੇ ਲਈ, ਅਸੀਂ ਫਲੈਗ ਨੂੰ ਡੀਕ੍ਰਿਪਟ ਕਰਨ ਲਈ OpenSSL ਪੈਕੇਜ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ।
ਇਸ ਵਾਰ ਇਹ ਥੋੜ੍ਹਾ ਵੱਖਰਾ ਹੈ ਅਤੇ ਤੁਸੀਂ ਦੇਖੋਗੇ ਕਿ OpenSSL ਪੈਕੇਜ ਇਸ ਚੁਣੌਤੀ ਲਈ ਕੰਮ ਨਹੀਂ ਕਰੇਗਾ।

ਅਸੀਂ ਇੱਕ ਸਵੈਚਲਿਤ RSA ਅਟੈਕ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ। ਇੱਕ ਆਮ ਪਾਈਥਨ ਸਕ੍ਰਿਪਟ ਹੈ[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
