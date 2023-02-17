---
title: "HackTheBox - Challenge - Crypto - Weak RSA"
draft: false
description: "Learn how to use an automated RSA attack tool, RsaCtfTool, to easily solve the HackTheBox Weak RSA Crypto challenge."
tags: ["HackTheBox", "Challenges", "Crypto", "Weak RSA", "RsaCtfTool", "HTB Weak RSA Crypto", "Easy challenge", "RSA cipher", "flag.enc", "key.pub", "OpenSSL package", "automated RSA attack tool", "python script", "RsaCtfTool", "python3", "public key", "uncipherfile", "Flag Example"]
toc: true
cover: "A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "A cartoon hacker wearing a cape and a mask, standing in front of a vault door with the HTB logo on it and holding a tool (such as a wrench or a screwdriver) with a green background symbolizing success and the "flag" in a speech bubble above their head."
coverCaption: ""
useRelativeCover: true
---

# HackTheBox - Challenge - Crypto - Weak RSA

Solve the HTB Weak RSA Crypto challenge with ease. Based on the RSA cipher, this easy challenge requires the use of an automated RSA attack tool like the RsaCtfTool. Get the flag with a simple command and expand your crypto skills with HackTheBox challenges.

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
