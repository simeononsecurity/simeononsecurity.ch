---
title: "استخدم ChatGPT في الطرفية: Bash وPowerShell وPython"
date: 2023-02-07
lastmod: 2026-11-13
toc: true
draft: false
description: "تعرّف على استخدام نموذج ChatGPT من OpenAI عبر واجهة سطر الأوامر (CLI) لإنشاء النصوص والإجابة عن الأسئلة بسهولة."
tags: ["ChatGPT", "OpenAI", "واجهة سطر الأوامر", "CLI", "توليد النص", "الإجابة عن الأسئلة", "مجموعة أدوات المطور", "مدير الحزم pip", "Python 3.5", "PowerShell", "Bash"]
cover: "/img/cover/A_developer_sitting_at_their_computer_typing.webp"
coverAlt: "مطوّر يجلس أمام حاسوبه ويكتب على لوحة المفاتيح، مع ظهور واجهة ChatGPT CLI في الطرفية."
coverCaption: ""
---
يُعدّ **ChatGPT**، الذي طورته OpenAI، **نموذجًا لغويًا متقدمًا** قادرًا على إنشاء نصوص شبيهة بالنصوص البشرية. ويوفر ChatGPT CLI (واجهة سطر الأوامر) للمطورين طريقة مريحة للتفاعل مع النموذج عبر سطر الأوامر. باستخدام ChatGPT CLI، يستطيع المطورون إنشاء النصوص وإكمالها والإجابة عن الأسئلة بالاستفادة من إمكانات النموذج.

لا يتطلب تثبيت ChatGPT CLI سوى وجود Python 3.5 أو إصدار أحدث على جهاز المطور. ويمكن استخدام مدير الحزم pip لتثبيت ChatGPT CLI بتنفيذ الأمر التالي:

**Linux:**
```bash

pip install chatgpt requests readline

```

**Windows PowerShell**
```powershell

pip install chatgpt requests pyreadline3

```

بعد التثبيت، يستطيع المطورون استخدام ChatGPT CLI لإنشاء النصوص أو الإجابة عن الأسئلة. على سبيل المثال، لإنشاء نص استنادًا إلى مطالبة، استخدم الأمر التالي:

```bash
chatgpt generate --prompt "ما الغاية من الوجود؟"
```

وللإجابة عن سؤال:

```bash
chatgpt answer --question "ما عاصمة فرنسا؟"
```

يمكن أيضًا استخدام ChatGPT CLI في نصوص برمجية بسيطة:

**Linux:**
```bash
prompt="ما معنى الحياة؟"
answer=$(chatgpt generate --prompt "$prompt")
echo "$answer"
```

**Windows PowerShell:**
```powershell
$prompt = "ما معنى الحياة؟"
$answer = chatgpt generate --prompt $prompt
Write-Host $answer
```

ينشئ هذا النص البرمجي محتوى استنادًا إلى المطالبة، ثم يعرض النص الناتج في وحدة التحكم.

إضافةً إلى إنشاء النصوص والإجابة عن الأسئلة، يوفر ChatGPT CLI خيارات أخرى، مثل تحديد طول النص الناتج، وضبط درجة حرارة المخرجات، واختيار عدد الإجابات المطلوب إنشاؤها.

يُعدّ **ChatGPT CLI إضافة مفيدة إلى مجموعة أدوات المطور**، إذ يوفر طريقة بسيطة ومباشرة للتفاعل مع نموذج ChatGPT. سواء كنت تنشئ نصًا لروبوت محادثة، أو تكمل نصًا في محرر، أو تجيب عن أسئلة في نظام للأسئلة والأجوبة، يمكن لـ ChatGPT CLI مساعدتك على إنجاز ذلك بسهولة.
