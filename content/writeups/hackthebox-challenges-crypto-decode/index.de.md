---
title: "HackTheBox – Herausforderungen – Krypto – Dekodieren"
date: 2020-10-07
draft: false
description: "Erfahren Sie, wie Sie Fernet- und Malboge-Chiffren entschlüsseln, um die HackTheBox Crypto Challenge zu lösen und die verborgene Flagge aufzudecken."
tags: ["HackTheBox", "Herausforderungen", "Krypto", "Dekodieren", "Zuschreibung", "Fernet-Chiffre", "Malboge-Chiffre", "Symmetrische Verschlüsselung", "Internet-Sicherheit", "Kryptographie", "Penetrationstests", "Python", "Sicherheit", "Herausforderung", "CTF", "Flagge", "Verschlüsselung", "Entschlüsselung", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Ein Cartoon-Hacker steht neben einem großen Schloss und hält in einer Hand einen Fernet-Logo-Schlüssel und in der anderen Hand einen Malboge-Logo-Schlüssel, während im Schloss eine Flagge zu sehen ist"
coverCaption: ""
---

Erhalten Sie einen detaillierten Überblick über die HackTheBox Crypto Decode-Herausforderung. Anhand von zwei Informationssträngen führt Sie dieser Artikel durch den Prozess der Dekodierung einer Fernet-Chiffre und einer Malboge-Chiffre, um die Flagge zu enthüllen. Nutzen Sie die von asecuritysite.com und base64decode.org bereitgestellten Tools, um die Lösung zu erreichen.

______

## Bereitgestellte Dateien:

Bei dieser Herausforderung werden Ihnen zwei Informationsstränge zur Verfügung gestellt.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
Und
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Durchgehen:

Auf den ersten Blick scheint es, dass es sich hierbei um eine Art Schlüssel und einen Chiffretext handelt.
Nachdem Sie sich umgesehen haben, werden Sie feststellen, dass es sich um eine Fernet-Verschlüsselung handelt.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) hat ein großartiges Tool, um es für Sie zu entschlüsseln.

Der Klartext aus den obigen Informationen ergibt eine Base64-codierte Zeichenfolge

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Um dies zu entschlüsseln, verwenden wir das von bereitgestellte Tool [base64decode.org](https://www.base64decode.org/)

Durch erneutes Dekodieren erhalten Sie Folgendes:
„
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB{x_xxx_xxxx}
„

