---
title: "HackTheBox - Challenges - Crypto - Call"
date: 2020-10-07
draft: false
description: "Learn how to decrypt DTMF tones using prime number cipher to solve the Crypto - Call challenge on HackTheBox."
tags: ["HackTheBox", "Crypto Challenge", "DTMF Tones", "Prime Number Cipher", "Decryption", "Solving Puzzles", "Cryptography", "Audio Conversion", "DialABC", "Decode.fr", "WAV", "MP3", "Frequency", "Mathematical Trait", "Flag", "Audacity", "Sonic Visualizer", "Numbers", "Automated Teller Menus", "Pay Phone"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "A cartoon phone with a green screen and a padlock on it, symbolizing security and encryption, with DTMF tones depicted in the backgroun"
coverCaption: ""
---
```
2331434783711923431767372331117714113
```
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```
```
2331434783711923431767372331117714113
```
```
HTB{xxxxxxxxxxxxxxxxxxx}
```
 قم بحل Crypto - Call Challenge على HackTheBox عن طريق فك تشفير نغمات DTMF في ملف sound.mp3. قم بتحويل الملف إلى .wav واستخدم DialABC للحصول على نص مشفر. افصل بين الأرقام واستخدم تشفير الرقم الأولي على Decode.fr للكشف عن العلم. استعد لوضع مهاراتك في تشفير رقم أولي للاختبار في هذا التحدي المثير على HackTheBox ".  ______  ## الملفات المقدمة:  تم تزويدك بملف واحد: - صوت. mp3  ## المشي من خلال:  عند تشغيل ** sound.mp3 ** ، ستسمع صوتًا مألوفًا. إذا لم تكن ميألوفًا للأصوات التي تسمعها ، فستسمع نغمات ** DTMF ** (نغمة مزدوجة متعددة الترددات). التنزيلات ، التنزيلات ، التنقل.  كل نغمة لها تردد معين. يمكنك الحصول على الوقت المناسب لذلك؟ [DialABC] (http://www.dialabc.com/sound/detect/index.html) أولاً ، سيتعين عليك تحويله إلى.  خذ الملف المحول إلى [DialABC] (http://www.dialabc.com/sound/detect/index.html) وقد ناتج عن ناتج التالي:   لاحظ أنه تستمع إلى الطابع الخاص بي. قد حصل على سلسلة ، وقد حصل على الصورة التالية:  منظمًا على هذا النحو ، قد تكون مرتبكًا وتعتقد أنه قد يكون HEX. إنه ليس كذلك. انتبه للأرقام. ما هي السمة الرياضية التي تشترك فيها كل مجموعة من الأرقام؟ ... كلهم أعداد أولية. وهو ما يجب أن يجلب لك تجربة ** الأقل شهرة ** تشفير الرقم الأولي **.  سنستخدم [Decode.fr] (https://www.dcode.fr/prime-numbers-cipher) لإكمال هذا التحدي. أرسل النص المشفر من قبل أن نفصله وستحصل على العلم.  ______  ### مثال العلم: