---
title: "HackTheBox - Provocări - Crypto - Decodare"
date: 2020-10-07
draft: false
description: "Aflați cum să decodați cifrurile Fernet și Malboge pentru a rezolva HackTheBox Crypto Challenge și a descoperi steagul ascuns."
tags: ["HackTheBox", "Provocări", "Cripto", "Decodați", "Notează", "Cifrul Fernet", "Cifrul Malboge", "Criptare simetrică", "Securitate cibernetică", "Criptografie", "Testarea de penetrare", "Piton", "Securitate", "Provocare", "CTF", "Steag", "Criptare", "Decriptare", "Baza 64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un hacker de desene animate stă lângă un lacăt mare, cu o mână ținând o cheie cu logo Fernet și cu cealaltă mână ținând o cheie cu logo Malboge, în timp ce un steag este văzut în interiorul lacătului"
coverCaption: ""
---

Obțineți o prezentare detaliată a provocării HackTheBox Crypto Decode. Având în vedere două șiruri de informații, acest articol vă ghidează prin procesul de decodare a unui cifru Fernet și a unui cifru Malboge pentru a dezvălui steagul. Utilizați instrumentele oferite de asecuritysite.com și base64decode.org pentru a obține soluția.

______

## Fișiere furnizate:

În această provocare vi se oferă două șiruri de informații.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
și
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Plimbare prin:

La prima vedere, se pare că acesta este un fel de cheie și un text cifrat.
După ce ai căutat în jur, vei descoperi că este un cifr Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) are un instrument grozav pentru a-l decoda pentru tine.

Textul simplu din informațiile de mai sus vă oferă un șir codificat base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Pentru a decoda acest lucru, vom folosi instrumentul furnizat de la [base64decode.org](https://www.base64decode.org/)

Decodarea vă oferă din nou următoarele:
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
```

