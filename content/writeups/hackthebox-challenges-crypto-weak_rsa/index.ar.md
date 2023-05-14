---
title: "HackTheBox - التحدي - التشفير - ضعف RSA"
draft: false
description: "تعرف على كيفية استخدام أداة هجوم RSA آلية ، RsaCtfTool ، لحل تحدي HackTheBox Weak RSA Crypto بسهولة."
tags: ["هاكذا بوكس", "التحديات", "تشفير", "ضعف RSA", "RsaCtfTool", "تشفير HTB ضعيف RSA", "تحدي سهل", "تشفير RSA", "flag.enc", "key.pub", "حزمة OpenSSL", "أداة هجوم آلية RSA", "نص بيثون", "RsaCtfTool", "بيثون 3", "المفتاح العمومي", "فك الشفرة", "مثال العلم"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "متسلل رسوم متحركة يرتدي عباءة وقناعًا ، ويقف أمام باب قبو عليه شعار HTB ويحمل أداة (مثل مفتاح ربط أو مفك براغي) بخلفية خضراء ترمز إلى النجاح والعلم في فقاعة كلام أعلاه رأسهم."
coverCaption: ""
---
 تحدي HTB Weak RSA Crypto بكل سهولة. بناءً على تشفير RSA ، يتطلب هذا التحدي السهل استخدام أداة هجوم RSA آلية مثل RsaCtfTool. احصل على العلم بأمر بسيط وقم بتوسيع مهاراتك في التشفير مع تحديات HackTheBox.

______

## الملفات المقدمة:

** تم تزويدك بالملفات التالية: **
- علم. en
- مفتاح

## جولة تفصيلية:

للوهلة الأولى ، تعتقد أنه يمكنك فك تشفير العلم باستخدام المفتاح العام.
لذلك ، قد نستخدم حزمة OpenSSL لفك تشفير العلم.
هذه المرة مختلفة قليلاً وستجد أن حزمة OpenSSL لن تعمل مع هذا التحدي.

سنستخدم أداة هجوم آلية RSA. أحد نصوص Python الشائعة هو[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```
