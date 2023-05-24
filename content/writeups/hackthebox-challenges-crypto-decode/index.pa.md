---
title: "ਹੈਕਬੌਕਸ - ਚੁਣੌਤੀਆਂ - ਕ੍ਰਿਪਟੋ - ਡੀਕੋਡ"
date: 2020-10-07
draft: false
description: "ਸਿੱਖੋ ਕਿ ਹੈਕਦਬੌਕਸ ਕ੍ਰਿਪਟੋ ਚੈਲੇਂਜ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਫਰਨੇਟ ਅਤੇ ਮਾਲਬੋਜ ਸਿਫਰਾਂ ਨੂੰ ਕਿਵੇਂ ਡੀਕੋਡ ਕਰਨਾ ਹੈ ਅਤੇ ਲੁਕਵੇਂ ਫਲੈਗ ਨੂੰ ਬੇਪਰਦ ਕਰਨਾ ਹੈ।"
tags: ["HackTheBox", "ਚੁਣੌਤੀਆਂ", "ਕ੍ਰਿਪਟੋ", "ਡੀਕੋਡ ਕਰੋ", "ਲਿਖੋ", "ਫਰਨੇਟ ਸਿਫਰ", "ਮਾਲਬੋਗੇ ਸਿਫਰ", "ਸਮਮਿਤੀ ਐਨਕ੍ਰਿਪਸ਼ਨ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ", "ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ", "ਪਾਈਥਨ", "ਸੁਰੱਖਿਆ", "ਚੁਣੌਤੀ", "ਸੀ.ਟੀ.ਐਫ", "ਝੰਡਾ", "ਐਨਕ੍ਰਿਪਸ਼ਨ", "ਡਿਕ੍ਰਿਪਸ਼ਨ", "ਬੇਸ 64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "ਇੱਕ ਕਾਰਟੂਨ ਹੈਕਰ ਇੱਕ ਵੱਡੇ ਤਾਲੇ ਦੇ ਕੋਲ ਖੜ੍ਹਾ ਹੈ ਜਿਸ ਦੇ ਇੱਕ ਹੱਥ ਵਿੱਚ ਇੱਕ ਫਰਨੇਟ ਲੋਗੋ ਦੀ ਕੁੰਜੀ ਹੈ ਅਤੇ ਦੂਜੇ ਹੱਥ ਵਿੱਚ ਮਲਬੋਜ ਲੋਗੋ ਦੀ ਕੁੰਜੀ ਹੈ ਜਦੋਂ ਕਿ ਤਾਲੇ ਦੇ ਅੰਦਰ ਇੱਕ ਝੰਡਾ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ"
coverCaption: ""
---

HackTheBox ਕ੍ਰਿਪਟੋ ਡੀਕੋਡ ਚੁਣੌਤੀ ਦਾ ਵਿਸਤ੍ਰਿਤ ਵਾਕ-ਥਰੂ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਣਕਾਰੀ ਦੇ ਦੋ ਸਤਰ ਦਿੱਤੇ ਗਏ ਹਨ, ਇਹ ਲੇਖ ਫਲੈਗ ਨੂੰ ਪ੍ਰਗਟ ਕਰਨ ਲਈ ਇੱਕ ਫਰਨੇਟ ਸਾਈਫਰ ਅਤੇ ਇੱਕ ਮਾਲਬੋਜ ਸਾਈਫਰ ਨੂੰ ਡੀਕੋਡ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਤੁਹਾਡੀ ਅਗਵਾਈ ਕਰਦਾ ਹੈ। ਹੱਲ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ asecuritysite.com ਅਤੇ base64decode.org ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਟੂਲਸ ਦੀ ਵਰਤੋਂ ਕਰੋ।

______

## ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਫਾਈਲਾਂ:

ਇਸ ਚੁਣੌਤੀ ਵਿੱਚ ਤੁਹਾਨੂੰ ਜਾਣਕਾਰੀ ਦੀਆਂ ਦੋ ਸਤਰਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
ਅਤੇ
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## ਪੈਦਲ ਚੱਲੋ:

ਪਹਿਲੀ ਨਜ਼ਰ ਵਿੱਚ ਇਹ ਜਾਪਦਾ ਹੈ ਕਿ ਇਹ ਕਿਸੇ ਕਿਸਮ ਦੀ ਕੁੰਜੀ ਅਤੇ ਕੁਝ ਸਿਫਰ ਟੈਕਸਟ ਹੈ।
ਆਲੇ ਦੁਆਲੇ ਖੋਜ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਦੇਖੋਗੇ ਕਿ ਇਹ ਇੱਕ ਫਰਨੇਟ ਸਾਈਫਰ ਹੈ।
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) ਤੁਹਾਡੇ ਲਈ ਇਸਨੂੰ ਡੀਕੋਡ ਕਰਨ ਲਈ ਇੱਕ ਵਧੀਆ ਟੂਲ ਹੈ.

ਉਪਰੋਕਤ ਜਾਣਕਾਰੀ ਤੋਂ ਸਾਦਾ ਟੈਕਸਟ ਤੁਹਾਨੂੰ ਇੱਕ ਬੇਸ 64 ਏਨਕੋਡਡ ਸਤਰ ਦਿੰਦਾ ਹੈ

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

ਇਸ ਨੂੰ ਡੀਕੋਡ ਕਰਨ ਲਈ, ਅਸੀਂ ਪ੍ਰਦਾਨ ਕੀਤੇ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ [base64decode.org](https://www.base64decode.org/)

ਡੀਕੋਡਿੰਗ ਦੁਬਾਰਾ ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖਿਆਂ ਦਿੰਦਾ ਹੈ:
``
ਡੀ'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
``

