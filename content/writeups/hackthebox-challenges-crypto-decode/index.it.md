---
title: "HackTheBox - Sfide - Crittografia - Decodifica"
date: 2020-10-07
draft: false
description: "Scopri come decodificare i cifrari Fernet e Malboge per risolvere l'HackTheBox Crypto Challenge e scoprire la bandiera nascosta."
tags: ["HackTheBox", "Sfide", "Cripto", "Decodificare", "Scrivilo", "Cifra Fernet", "Malboge cifrario", "Crittografia simmetrica", "Sicurezza informatica", "Crittografia", "Test di penetrazione", "Pitone", "Sicurezza", "Sfida", "CTF", "Bandiera", "Crittografia", "Decrittazione", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un hacker di cartoni animati in piedi accanto a un grande lucchetto con una mano che tiene una chiave con il logo Fernet e l'altra mano che tiene una chiave con il logo Malboge mentre si vede una bandiera all'interno del lucchetto"
coverCaption: ""
---

Ottieni una panoramica dettagliata della sfida HackTheBox Crypto Decode. Date due stringhe di informazioni, questo articolo ti guida attraverso il processo di decodifica di un cifrario Fernet e un cifrario Malboge per rivelare la bandiera. Utilizza gli strumenti forniti da asecuritysite.com e base64decode.org per ottenere la soluzione.

______

## File forniti:

In questa sfida ti vengono fornite due stringhe di informazioni.

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

