---
title: "HackTheBox - التحديات - التشفير - فك الشفرة"
date: 2020-10-07
draft: false
description: "تعرف على كيفية فك شيفرات Fernet و Malboge لحل تحدي تشفير HackTheBox وكشف العلم المخفي."
tags: ["هاكذا بوكس", "التحديات", "تشفير", "فك تشفير", "اكتب", "فيرنيت شيفر", "مالبوج شيفر", "التشفير المتماثل", "الأمن الإلكتروني", "التشفير", "اختبار الاختراق", "بايثون", "حماية", "تحدي", "CTF", "علَم", "التشفير", "فك التشفير", "Base64"]
toc: true
cover: "/img/cover/A_cartoon_hacker_standing_next_to_a_large_lock_with_one_hand.png"
coverAlt: "متسلل كرتوني يقف بجوار قفل كبير بيد واحدة تحمل مفتاح شعار Fernet والأخرى تحمل مفتاح شعار Malboge بينما يظهر العلم داخل القفل"
coverCaption: ""
---

احصل على جولة تفصيلية حول تحدي فك تشفير HackTheBox. بالنظر إلى سلسلتين من المعلومات ، ترشدك هذه المقالة خلال عملية فك تشفير شفرة Fernet وشفرة Malboge للكشف عن العلم. استخدم الأدوات التي يوفرها asecuritysite.com و base64decode.org لتحقيق الحل.

______

## الملفات المقدمة:

في هذا التحدي يتم تزويدك بسلسلتين من المعلومات.

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

