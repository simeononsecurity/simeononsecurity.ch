---
title: "ਹੈਕਬੌਕਸ - ਚੁਣੌਤੀਆਂ - ਕ੍ਰਿਪਟੋ - ਡੀਕੋਡ"
date: 2020-10-07
draft: false
description: "ਹੈਕਬੌਕਸ ਕ੍ਰਿਪਟੋ ਚੈਲੇਂਜ ਨੂੰ ਹੱਲ ਕਰਨ ਅਤੇ ਲੁਕਵੇਂ ਫਲੈਗ ਨੂੰ ਬੇਪਰਦ ਕਰਨ ਲਈ ਫਰਨੇਟ ਅਤੇ ਮਾਲਬੋਜ ਸਿਫਰਾਂ ਨੂੰ ਡੀਕੋਡ ਕਰਨਾ ਸਿੱਖੋ।"
tags: ["ਹੈਕ ਬਾਕਸ","ਚੁਣੌਤੀਆਂ","ਕ੍ਰਿਪਟੋ","ਡੀਕੋਡ","ਲਿਖੋ","ਫਰਨੇਟ ਸਿਫਰ","ਮਾਲਬੋਗੇ ਸਿਫਰ","ਸਿਮਟ੍ਰਿਕ ਐਨਕ੍ਰਿਪਸ਼ਨ","ਸਾਈਬਰ ਸੁਰੱਖਿਆ","ਕ੍ਰਿਪਟੋਗ੍ਰਾਫੀ","ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ","ਪਾਈਥਨ","ਸੁਰੱਖਿਆ","ਚੁਣੌਤੀ","CTF","ਝੰਡਾ","ਇਨਕ੍ਰਿਪਸ਼ਨ","ਡਿਕ੍ਰਿਪਸ਼ਨ","ਬੇਸ 64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "ਇੱਕ ਕਾਰਟੂਨ ਹੈਕਰ ਇੱਕ ਵੱਡੇ ਤਾਲੇ ਦੇ ਕੋਲ ਖੜ੍ਹਾ ਹੈ ਜਿਸ ਦੇ ਇੱਕ ਹੱਥ ਵਿੱਚ ਇੱਕ ਫਰਨੇਟ ਲੋਗੋ ਦੀ ਕੁੰਜੀ ਹੈ ਅਤੇ ਦੂਜੇ ਹੱਥ ਵਿੱਚ ਇੱਕ ਮਾਲਬੋਜ ਲੋਗੋ ਦੀ ਕੁੰਜੀ ਹੈ ਜਦੋਂ ਕਿ ਤਾਲੇ ਦੇ ਅੰਦਰ ਇੱਕ ਝੰਡਾ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ"
coverCaption: ""
---

HackTheBox ਕ੍ਰਿਪਟੋ ਡੀਕੋਡ ਚੁਣੌਤੀ ਦਾ ਵਿਸਤ੍ਰਿਤ ਵਾਕ-ਥਰੂ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਣਕਾਰੀ ਦੇ ਦੋ ਸਤਰ ਦਿੱਤੇ ਗਏ, ਇਹ ਲੇਖ ਫਲੈਗ ਨੂੰ ਪ੍ਰਗਟ ਕਰਨ ਲਈ ਇੱਕ ਫਰਨੇਟ ਸਾਈਫਰ ਅਤੇ ਇੱਕ ਮਾਲਬੋਜ ਸਾਈਫਰ ਨੂੰ ਡੀਕੋਡ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਤੁਹਾਡੀ ਅਗਵਾਈ ਕਰਦਾ ਹੈ। ਹੱਲ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ asecuritysite.com ਅਤੇ base64decode.org ਦੁਆਰਾ ਪ੍ਰਦਾਨ ਕੀਤੇ ਟੂਲਸ ਦੀ ਵਰਤੋਂ ਕਰੋ।

______

## ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਫਾਈਲਾਂ:

ਇਸ ਚੁਣੌਤੀ ਵਿੱਚ ਤੁਹਾਨੂੰ ਜਾਣਕਾਰੀ ਦੀਆਂ ਦੋ ਸਤਰਾਂ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
and
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Walk Through:

At first glance it appears this is some sort of key and some cipher text.
After searching around, you'll find that it is a Fernet cypher.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) has a great tool to decode it for you.

The plain text from the above information gives you a base64 encoded string

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

To decode this, we'll use the tool provided from [base64decode.org](https://www.base64decode.org/)

Decoding again gives you the following:
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`Y^WVzTSXQVUNrLQPONGkKD,HAe(DC<;_?>
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

