---
title: "HackTheBox - Reptes - Crypto - Descodificació"
date: 2020-10-07
draft: false
description: "Apreneu a descodificar els xifratges de Fernet i Malboge per resoldre el HackTheBox Crypto Challenge i descobrir la bandera oculta."
tags: ["HackTheBox", "Desafiaments", "Cripto", "Descodificar", "Escriure", "Xifrat de Fernet", "Xifrat de Malboge", "Xifratge simètric", "Seguretat cibernètica", "Criptografia", "Prova de penetració", "Python", "Seguretat", "Desafiament", "CTF", "Bandera", "Xifratge", "Desxifrat", "Base 64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Un pirata informàtic de dibuixos animats al costat d'un pany gran amb una mà sostenint una clau amb el logotip de Fernet i l'altra mà sostenint una clau amb el logotip de Malboge mentre es veu una bandera dins del pany"
coverCaption: ""
---

Obteniu una descripció detallada del repte HackTheBox Crypto Decode. Tenint en compte dues cadenes d'informació, aquest article us guiarà pel procés de descodificació d'un xifrat de Fernet i un xifrat de Malboge per revelar la bandera. Utilitzeu les eines proporcionades per asecuritysite.com i base64decode.org per aconseguir la solució.

______

## Fitxers proporcionats:

En aquest repte se't proporcionen dues cadenes d'informació.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
i
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Passejada:

A primera vista sembla que es tracta d'una mena de clau i d'algun text xifrat.
Després de cercar, trobareu que és un xifrat de Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) té una gran eina per desxifrar-lo.

El text sense format de la informació anterior us proporciona una cadena codificada en base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Per descodificar-ho, utilitzarem l'eina proporcionada des de [base64decode.org](https://www.base64decode.org/)

La descodificació de nou us proporciona el següent:
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

