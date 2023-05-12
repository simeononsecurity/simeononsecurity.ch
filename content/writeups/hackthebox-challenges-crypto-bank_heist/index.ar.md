---
title: "HackTheBox - التحديات - التشفير - سرقة البنوك"
date: 2020-10-07
draft: false
toc: true
description: "Learn how to decode T9/Multitap and Atbash ciphers to solve the Bank Heist challenge on HackTheBox."
tags: ["hackthebox"،"التشفير"،"تشفير T9"،"تشفير متعدد الصفحات"،"شفرات أتباش"،"الأمن الإلكتروني"،"فك تشفير"،"نص مشفر"،"تحدي"،"علَم"،"الأمن الإلكتروني"،"قرصنة"،"يتعلم"،"درس تعليمي"،"فك التشفير"،"حل الاحجية"،"تفكيك الرموز"،"تحدي التشفير" ،"مهارات الأمن السيبراني" ،"تعليم على الانترنت"]
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

## Walk Through:

**Very clearly, this is either a T9 or Multitap cipher.**  
Multitap is the cipher in this instance though. [Decode.fr](https://www.dcode.fr/multitap-abc-cipher) has a tool to decode this.

You'll get this plain text:
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY. YOUR SHARE OF THE HEIST IS IN YOUR HOUSE. THE KEY TO THE LOCK IS BELOW, GO TO PARIS GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```

**What is that junk at the end you might ask? Well it's actually an atbash cipher text.**

```
GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW
```


We'll use [CyberChef](<https://gchq.github.io/CyberChef-#recipe=Atbash_Cipher()&input=R1NWIFhMV1YgR0wgR1NWIEhaVSBPTFhQIApUTElWR1JJVk5WTUdVRk1X>) to decipher one more time. Then you have your flag. Whoot!

______

### Flag Example:

```
HTB{XXXXXXXXXXXXXXXXX}
```
