---
title: "HackTheBox - Défis - Crypto - Décoder"
date: 2020-10-07
draft: false
description: "Apprenez à décoder les chiffrements Fernet et Malboge pour résoudre le HackTheBox Crypto Challenge et découvrir le drapeau caché."
tags: ["HackTheBox", "Défis", "Crypto", "Décoder", "Rédaction", "Chiffre de Fernet", "Chiffre de Malboge", "Chiffrement symétrique", "La cyber-sécurité", "Cryptographie", "Tests de pénétration", "Python", "Sécurité", "Défi", "FCT", "Drapeau", "Chiffrement", "Décryptage", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un hacker de dessin animé debout à côté d'une grande serrure avec une main tenant une clé avec le logo Fernet et l'autre main tenant une clé avec le logo Malboge tandis qu'un drapeau est vu à l'intérieur de la serrure"
coverCaption: ""
---

Obtenez une présentation détaillée du défi HackTheBox Crypto Decode. Étant donné deux chaînes d'informations, cet article vous guide à travers le processus de décodage d'un chiffre Fernet et d'un chiffre Malboge pour révéler le drapeau. Utilisez les outils fournis par asecuritysite.com et base64decode.org pour trouver la solution.

______

## Fichiers fournis :

Dans ce défi, deux chaînes d'informations vous sont fournies.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
et
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Procédure pas à pas:

À première vue, il semble qu'il s'agisse d'une sorte de clé et d'un texte chiffré.
Après avoir cherché, vous découvrirez qu'il s'agit d'un chiffre de Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) a un excellent outil pour le décoder pour vous.

Le texte brut des informations ci-dessus vous donne une chaîne encodée en base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Pour décoder cela, nous utiliserons l'outil fourni par [base64decode.org](https://www.base64decode.org/)

Le décodage vous donne à nouveau ce qui suit :
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

