---
title: "HackTheBox - Испытания - Крипто - Расшифровка"
date: 2020-10-07
draft: false
description: "Узнайте, как расшифровать шифры Фернета и Мальбоге, чтобы решить задачу HackTheBox Crypto Challenge и раскрыть скрытый флаг."
tags: ["ХакБокс", "Проблемы", "Крипто", "Расшифровать", "Записать", "Шифр Фернета", "Шифр Мальбога", "Симметричное шифрование", "Информационная безопасность", "Криптография", "Проверка на проницаемость", "питон", "Безопасность", "Испытание", "CTF", "Флаг", "Шифрование", "Расшифровка", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "Мультяшный хакер стоит рядом с большим замком, одной рукой он держит ключ с логотипом Fernet, а другой рукой держит ключ с логотипом Malboge, в то время как внутри замка виден флаг"
coverCaption: ""
---

Получите подробное пошаговое руководство по испытанию HackTheBox Crypto Decode. Учитывая две строки информации, эта статья проведет вас через процесс декодирования шифра Фернета и шифра Мальбоге для раскрытия флага. Используйте инструменты, предоставляемые asecuritysite.com и base64decode.org, для достижения решения.

______

## Предоставленные файлы:

В этом задании вам предоставляется две строки информации.

```
993gmULBNujjrZCDev3W8kAVaLkXiyHhCL3500188bA=
```
и
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## Прохождение:

На первый взгляд кажется, что это какой-то ключ и какой-то зашифрованный текст.
После поиска вы обнаружите, что это шифр Фернета.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) имеет отличный инструмент, чтобы расшифровать его для вас.

Простой текст из приведенной выше информации дает вам строку в кодировке base64.

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

Чтобы расшифровать это, мы будем использовать инструмент, предоставленный из [base64decode.org](https://www.base64decode.org/)

Декодирование снова дает вам следующее:
```
Д'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
ХТБ{х_ххх_хххх}
```

