---
title: "HackTheBox - Wyzwania - Kryptowaluty - Dekodowanie"
date: 2020-10-07
draft: false
description: "Dowiedz się, jak rozszyfrować szyfry Fernet i Malboge, aby rozwiązać wyzwanie kryptograficzne HackTheBox i odkryć ukrytą flagę."
tags: ["HackTheBox", "Wyzwania", "Kryptowaluty", "Dekodowanie", "Opis", "Fernet Cipher", "Szyfr Malboge", "Szyfrowanie symetryczne", "Cyberbezpieczeństwo", "Kryptografia", "Testy penetracyjne", "Python", "Bezpieczeństwo", "Wyzwanie", "CTF", "Flaga", "Szyfrowanie", "Deszyfrowanie", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Haker z kreskówki stojący obok dużego zamka z jedną ręką trzymającą klucz z logo Fernet i drugą ręką trzymającą klucz z logo Malboge, podczas gdy wewnątrz zamka widać flagę"
coverCaption: ""
---

Poznaj szczegółowy opis wyzwania HackTheBox Crypto Decode. Biorąc pod uwagę dwa ciągi informacji, ten artykuł poprowadzi Cię przez proces dekodowania szyfru Fernet i szyfru Malboge w celu ujawnienia flagi. Aby uzyskać rozwiązanie, należy skorzystać z narzędzi dostarczonych przez asecuritysite.com i base64decode.org.

______

## Dostarczone pliki:

W tym wyzwaniu otrzymasz dwa ciągi informacji.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
oraz
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Walk Through:

Na pierwszy rzut oka wydaje się, że jest to jakiś klucz i tekst zaszyfrowany.
Po przeszukaniu okaże się, że jest to szyfr Fernet.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) ma świetne narzędzie do dekodowania.

Zwykły tekst z powyższych informacji daje ciąg zakodowany w base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Aby to rozszyfrować, użyjemy narzędzia dostarczonego przez [base64decode.org](https://www.base64decode.org/)

Ponowne dekodowanie daje następujące wyniki:
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

