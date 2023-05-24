---
title: "HackTheBox - التحديات - التشفير - سرقة البنوك"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["هاكتبوكس", "التشفير", "T9 الشفرات", "الشفرات المتعددة", "شفرات أطباش", "الأمن الإلكتروني", "فك تشفير", "نص مشفر", "تحدي", "علَم", "الأمن الإلكتروني", "القرصنة", "يتعلم", "درس تعليمي", "فك التشفير", "حل الاحجية", "تفكيك الرموز", "تحدي التشفير", "مهارات الأمن السيبراني", "تعليم على الانترنت"]
cover: "/img/cover/A_cartoon_vault_door_being_unlocked_with_a_key_revealing.png"
coverAlt: "يتم فتح باب قبو كرتوني بمفتاح يكشف عن صندوق كنز ، كل ذلك على خلفية منظر المدينة الباريسي عند غروب الشمس."
coverCaption: ""
---

دليل شامل لحل تحدي Crypto "سرقة البنك" على HackTheBox. يتضمن التحدي فك تشفير نص T9 أو Multitap باستخدام Decode.fr ونص تشفير atbash باستخدام CyberChef للكشف عن العلم. يجب أن تقرأ للمتخصصين الطموحين في مجال الأمن السيبراني وأي شخص يتطلع إلى تعزيز مهاراتهم في التشفير.

## الملفات المقدمة:

بالنسبة لهذا التحدي ، تم تزويدك بنص التشفير التالي:

```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.

47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```

______

## المشي من خلال:

** من الواضح جدًا أن هذا إما T9 أو Multitap. **
الضغط المتعدد هو التشفير في هذه الحالة بالرغم من ذلك. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) لديه أداة لفك هذا.

ستحصل على هذا النص العادي:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

** ما هي تلك الخردة في النهاية قد تسأل؟ حسنًا ، إنه في الواقع نص تشفير أتباش. **

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


سنستخدم [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) لفك الشفرة مرة أخرى. ثم لديك علمك. ووه!

______

### مثال العلم:

```
HTB{XXXXXXXXXXXXXXXXX}
```
