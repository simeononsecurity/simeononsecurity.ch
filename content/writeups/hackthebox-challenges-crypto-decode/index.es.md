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

 Obtenga un recorrido detallado del desafío HackTheBox Crypto Decode. Dadas dos cadenas de información, este artículo lo guía a través del proceso de decodificación de un cifrado Fernet y un cifrado Malboge para revelar la bandera. Utilice las herramientas proporcionadas por asecuritysite.com y base64decode.org para lograr la solución.  ______  ##Archivos provistos:  En este desafío, se le proporcionan dos cadenas de información.  y  ## Caminar a través de:  A primera vista, parece que se trata de una especie de clave y un texto grabado. Después de buscar, encontrará que es un cifrado de Fernet. [Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) tiene una gran herramienta para decodificarlo por usted.  El texto sin formato de la información anterior le proporciona una cadena codificada en base64   Para decodificar esto, usaremos la herramienta proporcionada por [base64decode.org](https://www.base64decode.org/)  La decodificación nuevamente te da lo siguiente:  Este era nuevo para mí. Pero encontrará después de una investigación cuidadosa que es un cifrado de Malboge. Descifrarlo con [esta] (http://malbolge.doleczek.pl/) herramienta le dar la bandera.  ______  ### Bandera Ej.: 