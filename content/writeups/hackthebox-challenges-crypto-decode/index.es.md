---
title: "HackTheBox - Desafíos - Cripto - Decodificación"
date: 2020-10-07
draft: false
description: "Aprenda a decodificar los cifrados Fernet y Malboge para resolver el desafío criptográfico HackTheBox y descubrir la bandera oculta."
tags: ["HackTheBox", "Desafíos", "Cripto", "Descodificar", "redacción", "Cifrado Fernet", "Cifrado Malboge", "Cifrado simétrico", "La seguridad cibernética", "Criptografía", "Pruebas de penetración", "Pitón", "Seguridad", "Desafío", "CTF", "Bandera", "Cifrado", "Descifrado", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un hacker de dibujos animados parado junto a una gran cerradura con una mano sosteniendo una llave con el logo de Fernet y la otra mano sosteniendo una llave con el logo de Malboge mientras se ve una bandera dentro de la cerradura"
coverCaption: ""
---

Obtenga un recorrido detallado del desafío HackTheBox Crypto Decode. Dadas dos cadenas de información, este artículo lo guía a través del proceso de decodificación de un cifrado Fernet y un cifrado Malboge para revelar la bandera. Utilice las herramientas proporcionadas por asecuritysite.com y base64decode.org para lograr la solución.

______

## Archivos proporcionados:

En este desafío, se le proporcionan dos cadenas de información.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
y
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Caminar a través de:

A primera vista, parece que se trata de una especie de clave y un texto cifrado.
Después de buscar, encontrará que es un cifrado de Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) tiene una gran herramienta para decodificarlo por ti.

El texto sin formato de la información anterior le proporciona una cadena codificada en base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Para decodificar esto, usaremos la herramienta provista por [base64decode.org](https://www.base64decode.org/)

La decodificación nuevamente te da lo siguiente:
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

