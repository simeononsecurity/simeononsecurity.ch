---
title: „HackTheBox - Provocare - Crypto - RSA slabă”
draft: false
description: „Aflați cum să utilizați un instrument automat de atac RSA, RsaCtfTool, pentru a rezolva cu ușurință provocarea HackTheBox Weak RSA Crypto.”
tags: [„HackTheBox”,„Provocări”,"Crypto",„RSA slab”,„RsaCtfTool”,„HTB Weak RSA Crypto”,„Provocare ușoară”,„Cifrul RSA”,"flag.enc", "key.pub", „Pachetul OpenSSL”,„instrument automat de atac RSA”,"script python",„RsaCtfTool”,"python3",„cheie publică”,"descifrează fișierul",„Exemplu de steag”]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: „Un hacker de desene animate purtând o pelerină și o mască, stând în fața unei uși seifului cu sigla HTB pe ea și ținând în mână o unealtă (cum ar fi o cheie sau o șurubelniță) cu un fundal verde care simbolizează succesul și steagul într-un balon de vorbire deasupra capului lor”.
coverCaption: ""
---
 provocarea HTB Weak RSA Crypto cu ușurință. Bazată pe cifrul RSA, această provocare ușoară necesită utilizarea unui instrument automat de atac RSA, cum ar fi RsaCtfTool. Obțineți steagul cu o comandă simplă și extindeți-vă abilitățile cripto cu provocările HackTheBox.

______

## Fișiere furnizate:

**Vi se oferă următoarele fișiere:**
- steag.enc
- cheie.pub

## Examinare:

La prima vedere, ați crede că puteți decripta steag-ul cu cheia publică.
Pentru asta, am putea folosi pachetul OpenSSL pentru a decripta steag-ul.
De data aceasta este puțin diferit și veți descoperi că pachetul OpenSSL nu va funcționa pentru această provocare.

Vom folosi un instrument automat de atac RSA. Un script python obișnuit este[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
