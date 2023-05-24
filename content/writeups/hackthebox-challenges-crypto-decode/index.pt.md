---
title: "HackTheBox - Desafios - Criptografia - Decodificação"
date: 2020-10-07
draft: false
description: "Aprenda a decodificar as cifras de Fernet e Malboge para resolver o HackTheBox Crypto Challenge e descobrir a bandeira oculta."
tags: ["HackTheBox", "desafios", "Criptografia", "Decodificar", "Escrever", "Cifra Fernet", "Cifra Malboge", "Criptografia Simétrica", "Cíber segurança", "Criptografia", "Teste de penetração", "Pitão", "Segurança", "Desafio", "CTF", "Bandeira", "Criptografia", "Descriptografia", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Um hacker de desenho animado ao lado de uma grande fechadura com uma mão segurando uma chave com o logotipo da Fernet e a outra segurando uma chave com o logotipo da Malboge enquanto uma bandeira é vista dentro da fechadura"
coverCaption: ""
---

Obtenha uma explicação detalhada do desafio HackTheBox Crypto Decode. Dadas duas sequências de informações, este artigo orienta você no processo de decodificação de uma cifra Fernet e uma cifra Malboge para revelar a bandeira. Utilize as ferramentas fornecidas por asecuritysite.com e base64decode.org para obter a solução.

______

## Arquivos Fornecidos:

Neste desafio, você recebe duas sequências de informações.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
e
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Passeio por:

À primeira vista, parece que é algum tipo de chave e algum texto cifrado.
Depois de pesquisar, você descobrirá que é uma cifra Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) tem uma ótima ferramenta para decodificá-lo para você.

O texto simples das informações acima fornece uma string codificada em base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Para decodificar isso, usaremos a ferramenta fornecida em [base64decode.org](https://www.base64decode.org/)

A decodificação novamente fornece o seguinte:
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

