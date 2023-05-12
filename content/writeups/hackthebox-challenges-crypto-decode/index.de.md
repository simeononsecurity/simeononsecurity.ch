---
title: "HackTheBox - Challenges - Crypto - Decode"
date: 2020-10-07
draft: false
description: "Learn how to decode Fernet and Malboge ciphers to solve the HackTheBox Crypto Challenge and uncover the hidden flag."
tags: ["HackTheBox", "Challenges", "Crypto", "Decode", "Writeup", "Fernet Cipher", "Malboge Cipher", "Symmetric Encryption", "Cybersecurity", "Cryptography", "Penetration Testing", "Python", "Security", "Challenge", "CTF", "Flag", "Encryption", "Decryption", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "A cartoon hacker standing next to a large lock with one hand holding a Fernet logo key and the other hand holding a Malboge logo key while a flag is seen inside the lock"
coverCaption: ""
---
```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```
```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```
```
D'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`Y^WVzTSXQVUNrLQPONGkKD,HAe(DC<;_?>
```
```
HTB{x_xxx_xxxx}
```

 Erhalten Sie eine detaillierte Anleitung zur HackTheBox Crypto Decode Challenge. Anhand von zwei Informationssträngen führt Sie diesen Artikel durch den Prozess der Entschlüsselung einer Fernet-Chiffre und Einer Malboge-Chiffre, um die Flagge zu enthüllen. Verwenden Sie Tools von asecuritysite.com und base64decode.org, um die Lösung zu erreichen.  ______  ## Bereitgestellte Dateien:  In dieser Herausforderung Werden Ihnen zwei Informationsstränge bereitgestellt.  Und  ##Durchgang:  Auf den ersten Blick scheint es sich um eine Art Schlüssel und Chiffretext zu handeln. Nachdem Sie sich umgesehen haben, werden Sie feststellen, dass es sich um eine Fernet-Chiffre handelt. [Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) hat ein großartiges Tool, um es für Sie zu entschlüsseln.  Der Klartext aus den obigen Informationen ergibt eine Base64-codierte Zeichenfolge   Um dies zu decodieren, verwenden wir das von [base64decode.org](https://www.base64decode.org/) bereitgestellte Tool.  Die erneute Dekodierung ergibt Folgendes:  Das war mir neu. Aber SIE Werden nach verstärkter Recherche feststellen, dass es sich um eine Malboge-Chiffre handelt. Wenn Sie es mit [diesem](http://malbolge.doleczek.pl/) Tool entschlüsseln, erhalten Sie die Flagge.  ______  ###Flagge Bsp.: 