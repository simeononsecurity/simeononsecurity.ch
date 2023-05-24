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
و
```
gAAAAABboRUb0FsuiYBk1tsXRDr6KAzU1xrNSUv7grB-G-dAEeyqj99kUebz466I2VcH5xDa5HEc5KkbgTklQ7tm9JCRPlJtRng1Ns3VEvbrk7B835OINfPnRbc-UIOnnCmW3CgMdMtf5wGLN299AZEzxIvuy71WC5d9xJDchyiORycuzCth95-4nTKphlNQQ2ko3DX72RxWeEjwt3mavnFXqcOCkGxUhJYmFltz_6ND56VGTrXZi_CK5xLODOX4sj1GNwN_CrU3sJ0obTdA2wF5OaDZLbA1GBPfK0PDlC9WxoUf85K0tFXKfqbt3c5YqtqfytNG5gTkbDFM2NjE7BveBf1DP9ca8g==
```

## المشي من خلال:

للوهلة الأولى يبدو أن هذا نوع من المفاتيح وبعض النصوص المشفرة.
بعد البحث حولك ، ستجد أنه من طراز Fernet cypher.
[Asecuritysite.com](https://asecuritysite.com/encryption/ferdecode) لديه أداة رائعة لفك تشفيرها نيابة عنك.

يمنحك النص العادي من المعلومات أعلاه سلسلة مشفرة باستخدام base64

```
RCdgTl45OFs8O3tGMlZVNTRRPythcUw6bVxJNmlYJmYkMEBSeFBfdSldeHFwdW5tM3Fwb2htZmUrTGJnZl9eXSNhYFleV1Z6VFNyUVZVTnJMUVBPTkdrS0QsSEFlKERDPDtfPz5+fTVZOTg3dzUuUjJyMC8oJyZKKikoJyYlfHtBeX53djx6eXhxWTZ0c1VUcG9oLnk=
```

لفك هذا ، سنستخدم الأداة المقدمة من [base64decode.org](https://www.base64decode.org/)

يمنحك فك التشفير مرة أخرى ما يلي:
""
د'`N^98[<;{F2VU54Q?+aqL:m\I6iX&f$0@RxP_u)]xqpunm3qpohmfe+Lbgf_^]#a`
```

This was a new one for me. But you'll find after some careful research that it is a Malboge cipher.
Decoding it with [this](http://malbolge.doleczek.pl/) tool will give you the flag.

______

### Flag Ex:
```
HTB {x_xxx_xxxx}
""

