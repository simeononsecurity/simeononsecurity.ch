---
title: "HackTheBox - Challenge - Crypto - Weak RSA"
draft: false
description: "Solve the HTB Weak RSA Crypto, an easy challenge based on the RSA cipher."
tags: ['HackTheBox', 'Challenges', 'Crypto', 'Weak RSA', 'RsaCtfTool']
toc: true
---

# HackTheBox - Challenge - Crypto - Weak RSA

The HTB "Weak RSA" Crypto is an easy challenge based on the RSA cipher.

## Provided Files:

**You are provided with the following files:**
- flag.enc
- key.pub

## Walk-through:

At first glance, you'd think you can decrypt the flag with the public key.   
For that, we might use the OpenSSL package to decrypt the flag.
This time it's a bit different and you'll find that the OpenSSL package won't work for this challenge. 

We'll use an automated RSA attack tool. A common python script is the [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
