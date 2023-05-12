---
title: "HackTheBox - Desafíos - Cripto - Decodificación"
date: 2020-10-07
draft: false
description: "Aprenda a decodificar los cifrados Fernet y Malboge para resolver el Crypto Challenge HackTheBox y descubrir la bandera oculta".
tags: ["Hackear la caja","Desafíos","Cripto","Descodificar","Escribir","Cifrado Fernet","Cifrado Malboge","Cifrado simétrico","La seguridad cibernética","Criptografía","Pruebas de penetración","Pitón","Seguridad","Desafío","CTF","Bandera","Cifrado","Descifrado","Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un hacker de dibujos animados parado junto a una gran cerradura con una mano sosteniendo una llave con el logotipo de Fernet y la otra mano sosteniendo una llave con el logotipo de Malboge mientras se ve una bandera dentro de la cerradura"
coverCaption: ""
---

Obtenga un recorrido detallado del desafío HackTheBox Crypto Decode. Dadas dos cadenas de información, este artículo lo guía a través del proceso de decodificación de un cifrado Fernet y un cifrado Malboge para revelar la bandera. Utilice las herramientas proporcionadas por asecuritysite.com y base64decode.org para lograr la solución.

______

## Archivos proporcionados:

En este desafío, se le proporcionan dos cadenas de información.

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

