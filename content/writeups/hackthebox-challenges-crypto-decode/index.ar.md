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

 احصل على جولة تفصيلية حول فك تشفير HackTheBox. عملية فك شفرة "فيرنت" وشفرة مالبوج عن العلم. استخدم الأدوات التي توفرها asecuritysite.com و base64decode.org للحصول على الحل.  ______  ## الملفات المقدمة:  تزويد بالسلسلتين.  و  ## المشي من خلال:  يبدو أن هذا نوع من النصوص. بعد البحث حولك ، ... [Asecuritysite.com] (https://asecuritysite.com/encryption/ferdecode) لديه أداة رائعة لفك تشفيره نيابة عنك.  يمنحك النص الطبيعي لسلسلة مصفرة القاعدة 64   لفك هذا ، فريق البداية من [base64decode.org] (https://www.base64decode.org/)  يمنحك فك  كان هذا برنامجان بالنسبة لي. لكن ، بعد بعض البحث ، تشفير مالبوج. سيعطيك فك تشفيرها أداة [this] (http://malbolge.doleczek.pl/) العلم.  ______  ### عن مثال بسيط: 