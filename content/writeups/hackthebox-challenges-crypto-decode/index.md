---
title: "HackTheBox - Challenges - Crypto - Decode"
date: 2020-10-07T16:57:03-05:00
draft: false
description: "Get a detailed walk-through of the HackTheBox Crypto Decode challenge. Given two strings of information, this article guides you through the process of decoding a Fernet cypher and a Malboge cipher to reveal the flag. Utilize tools provided by asecuritysite.com and base64decode.org to achieve the solution."
tags: [HackTheBox", "Challenges", "Crypto", "Decode", "Writeup", "Fernet Cipher", "Base64 Decode", "Malboge Cipher", "Flag"]
toc: true
---

# HackTheBox - Challenges - Crypto - Decode

Get a detailed walk-through of the HackTheBox Crypto Decode challenge. Given two strings of information, this article guides you through the process of decoding a Fernet cypher and a Malboge cipher to reveal the flag. Utilize tools provided by asecuritysite.com and base64decode.org to achieve the solution.

## Provided Files:

In this challenge you are provided two strings of information.

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

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

