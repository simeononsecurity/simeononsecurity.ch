---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "تعرف على كيفية إنشاء رمز دعوة والانضمام إلى منصة HackTheBox عبر الإنترنت لاختبار مهاراتك وتطويرها في اختبار الاختراق والأمن السيبراني على كل من Windows و Linux."
tags: ["هاكذا بوكس", "دعوة التحدي", "اختبار الاختراق", "الأمن الإلكتروني", "شبابيك", "لينكس", "منصة على الإنترنت", "بريد HTTP", "رقم الدعوة", "تشفير Base64", "بوويرشيل", "لينكس باش", "فك تشفير Base64", "قم بدعوة إنشاء رمز", "برمجة", "تطوير الشبكة", "تكنولوجيا", "أمن تكنولوجيا المعلومات", "تدريب تكنولوجيا المعلومات"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "شاشة كمبيوتر كرتونية تعرض موقع HackTheBox الإلكتروني مع فتح باب قبو بمفتاح ، وكشف عن كأس أو ميدالية ، مع خلفية منظر المدينة في مخطط ألوان شعار HackTheBox (باللونين الأزرق والأبيض)."
coverCaption: ""
---
 إرشادات خطوة بخطوة لإكمال تحدي دعوة HackTheBox على نظامي التشغيل Windows أو Linux. تعرف على كيفية إنشاء رمز دعوة والانضمام إلى النظام الأساسي عبر الإنترنت لاختبار مهاراتك وتطويرها في اختبار الاختراق والأمن السيبراني. تقدم المقالة كلاً من الحلول البسيطة والمتقدمة ، مما يسهل على المستخدمين من جميع المستويات إكمال التحدي والوصول إلى النظام الأساسي.

______

## ما هو هاك ذا بوكس؟

HackTheBox عبارة عن منصة عبر الإنترنت لاختبار مهاراتك وتطويرها في اختبار الاختراق والأمن السيبراني.

## كيف تنضم إلى هاك ذا بوكس؟

لإنشاء حساب على HackTheBox (HTB) ، عليك إكمال تحدي الدعوة ، أو اختراق نفسك. لا تقلق على الرغم من أن هذا ليس صعبًا وستساعدك هذه المقالة على عدم إكمال التحدي.

أولاً ، انتقل إلى [HackTheBox Website](https://hackthebox.eu) وانقر على زر الانضمام.

سيظهر لك مربع يطلب بوضوح رمز دعوة.

يمكنك أن ترى بوضوح مربع نص يطلب منا رمز دعوة.

اضغط إما على *** "F12" *** على لوحة المفاتيح أو *** "Ctrl + Shift + I" *** لفتح أدوات مطور المستعرضات.

في علامة التبويب "العناصر" ، ستجد نصًا برمجيًا **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

بمراجعة جافا سكريبت ووظيفة makeInviteCode ، ستكتشف أنك بحاجة إلى إرسال ** HTTP POST ** إلى ** / api / calling / create ** للحصول على رمز دعوة.

يمكنك القيام بما يلي للحصول على رمز الدعوة المشفر Base64:

### حل:

#### بسيط:
- **شبابيك**: ```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- ** لينكس **: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

والذي سينشئ المحتوى التالي: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

إذا كنت تأخذ رمز الدعوة المشفر إلى [base64decode.org](https://www.base64decode.org/) ستحصل على رمز الدعوة الخاص بك!

#### متقدم (اطبع رمز الدعوة فورًا):
 - **شبابيك**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- ** لينكس **: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - ** ملاحظة **: ستحتاج إلى تثبيت برنامج [jq](https://stedolan.github.io/jq/download/) طَرد.

______

### دعوة رمز مثال:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```


