---
title: "HackTheBox - التحديات - التشفير - الاتصال"
date: 2020-10-07
draft: false
description: "تعرف على كيفية فك تشفير نغمات DTMF باستخدام تشفير الأرقام الأولية لحل تحدي Crypto - Call على HackTheBox."
tags: ["هاكذا بوكس", "تحدي التشفير", "نغمات DTMF", "عدد الشفرات الأولية", "فك التشفير", "حل الألغاز", "التشفير", "تحويل الصوت", "DialABC", "فك الشفرة", "WAV", "MP3", "تكرار", "السمة الرياضية", "علَم", "الجرأة", "متخيل سونيك", "أعداد", "قوائم الصراف الآلي", "الهاتف المدفوع"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "هاتف كرتوني بشاشة خضراء وقفل عليه ، يرمز إلى الأمان والتشفير ، مع نغمات DTMF موضحة في الخلفية"
coverCaption: ""
---

قم بحل Crypto - Call Challenge على HackTheBox عن طريق فك تشفير نغمات DTMF في ملف sound.mp3. قم بتحويل الملف إلى .wav واستخدم DialABC للحصول على نص مشفر. افصل بين الأرقام واستخدم تشفير الرقم الأولي على Decode.fr للكشف عن العلم. استعد لوضع مهاراتك في تشفير رقم أولي للاختبار في هذا التحدي المثير على HackTheBox ".

______

## الملفات المقدمة:

تم تزويدك بملف واحد:
- صوت. mp3

## المشي من خلال:

عند تشغيل ** sound.mp3 ** ، ستسمع صوتًا مألوفًا. إذا لم تكن مألوفًا للأصوات التي تسمعها ، فستسمع نغمات ** DTMF ** (نغمة مزدوجة متعددة الترددات). نفس النغمات التي كنت تسمعها أثناء الاتصال على هاتف عمومي أو أثناء التنقل عبر قوائم الصراف الآلي.

كل نغمة لها تردد معين. يمكنك الحصول على الأرقام يدويًا ، ولكن من لديه الوقت لذلك؟[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

خذ الملف المحول إلى[DialABC](http://www.dialabc.com/sound/detect/index.html) وستحصل على الناتج التالي:
```
2331434783711923431767372331117714113
```
 
Take notice that if you listen to the audio file carefully or open it in **Audacity** or **Sonic Visualizer** that, with one exception, the numbers are paired in groups of two.
If you separate out the number you get the following:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organized like this, you might be confused and think that it might be HEX. It isn't.  
Pay close attention to the numbers. What mathematical trait do each grouping of numbers share?....
They are all prime numbers. Which should bring you to try the lesser known **prime number cipher**.

We'll use [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) to complete this challenge.   
Submit the cipher text from before we separated it out and you'll get the flag.
```
2331434783711923431767372331117714113
```

______

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```