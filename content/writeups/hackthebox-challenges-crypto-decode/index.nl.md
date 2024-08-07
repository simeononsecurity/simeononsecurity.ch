---
title: "HackTheBox - Uitdagingen - Crypto - Decode"
date: 2020-10-07
draft: false
description: "Leer hoe je Fernet- en Malboge-sleutels kunt decoderen om de HackTheBox Crypto Challenge op te lossen en de verborgen vlag te ontdekken."
tags: ["HackTheBox", "Uitdagingen", "Crypto", "Decodeer", "Writeup", "Fernet Cipher", "Malboge Cipher", "Symmetrische encryptie", "Cyberbeveiliging", "Cryptografie", "Penetratie testen", "Python", "Beveiliging", "Uitdaging", "CTF", "Vlag", "Encryptie", "Ontcijfering", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Een cartoon hacker staat naast een groot slot met een hand die een Fernet logo sleutel vasthoudt en de andere hand die een Malboge logo sleutel vasthoudt terwijl een vlag in het slot te zien is"
coverCaption: ""
---

Een gedetailleerde uitleg over de HackTheBox Crypto Decode-uitdaging. Gegeven twee reeksen informatie leidt dit artikel u door het proces van het decoderen van een Fernet-code en een Malboge-code om de vlag te onthullen. Gebruik de tools van asecuritysite.com en base64decode.org om de oplossing te bereiken.

______

## Geleverde bestanden:

In deze uitdaging krijg je twee reeksen informatie.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
en
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Loop door:

Op het eerste gezicht lijkt dit een soort sleutel en wat cijfertekst.
Na wat zoeken kom je erachter dat het een Fernet cypher is.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) heeft een geweldig hulpmiddel om het voor je te decoderen.

De platte tekst van de bovenstaande informatie geeft je een base64 gecodeerde string

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Om dit te decoderen, gebruiken we het hulpmiddel van [base64decode.org](https://www.base64decode.org/)

Opnieuw decoderen geeft je het volgende:
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

