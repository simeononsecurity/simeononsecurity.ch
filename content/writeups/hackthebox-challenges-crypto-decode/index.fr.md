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

 Obtenez une présentation détaillée du défi HackTheBox Crypto Decode. Étant donné deux chaînes d'informations, cet article vous guide à travers le processus de décodage d'un chiffre Fernet et d'un chiffre Malboge pour révéler le drapeau. Utilisez les outils fournis par asecuritysite.com et base64decode.org pour trouver la solution.  ______  ##Fichiers fournis :  Dans ce défi, deux chaînes d'informations vous sont fournies.  et  ## Procédure pas à pas :  À première vue, il semble qu'il s'agisse d'une sorte de clé et d'un texte chiffré. Après avoir cherché, vous découvrirez qu'il s'agit d'un chiffre de Fernet. [Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) un excellent outil pour le décodeur pour vous.  Le texte brut des informations ci-dessus vous donne une chaîne encodée en base64   Pour décodeur cela, nous utiliserons l'outil fourni par [base64decode.org](https://www.base64decode.org/)  Le décodage vous donne à nouveau ce qui suit :  C'était nouveau pour moi. Mais vous découvrirez après quelques recherches approfondies qu'il s'agit d'un chiffrement Malboge. Le décodeur avec [cet](http://malbolge.doleczek.pl/) outil vous donnera le drapeau.  ______  ### Drapeau Ex : 