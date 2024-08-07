---
title: "حماية Windows من عمليات التنفيذ التخمينية لهجمات القناة الجانبية"
date: 2020-06-18
toc: true
draft: false
description: "تعرف على كيفية حماية نظام Windows الخاص بك من هجمات القناة الجانبية للتنفيذ التخميني باستخدام البرنامج النصي للتخفيف وتحديثات البرامج الثابتة من Microsoft"
tags: ["برنامج Windows Specter Meltdown Mitigation Script", "الهجمات التخمينية للقناة الجانبية", "مايكروسوفت", "شركة انتل", "AMD", "عبر", "ذراع", "ذكري المظهر", "كروم", "iOS", "macOS", "فرع الهدف حقن", "الحدود تحقق من تجاوز", "تحميل ذاكرة التخزين المؤقت للبيانات المارقة", "تجاوز المتجر التخميني", "أخذ عينات البيانات المعمارية الدقيقة", "CVEs", "تحديثات البرامج الثابتة", "مستودع جيثب", "بوويرشيل"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
** نص برمجي بسيط لتنفيذ الحماية ضد ثغرات القناة الجانبية للتنفيذ التخميني في أنظمة Windows. **

تدرك Microsoft وجود فئة جديدة من الثغرات الأمنية تم الكشف عنها علنًا والتي تسمى "هجمات القناة الجانبية للتنفيذ التخميني" والتي تؤثر على العديد من المعالجات الحديثة بما في ذلك Intel و AMD و VIA و ARM.

** ملاحظة: ** تؤثر هذه المشكلة أيضًا على أنظمة التشغيل الأخرى ، مثل Android و Chrome و iOS و macOS. لذلك ، ننصح العملاء بالتماس التوجيه من هؤلاء البائعين.

لقد أصدرنا العديد من التحديثات للمساعدة في التخفيف من هذه الثغرات الأمنية. لقد اتخذنا أيضًا إجراءات لتأمين خدماتنا السحابية. راجع الأقسام التالية لمزيد من التفاصيل.

لم نتلق أي معلومات حتى الآن للإشارة إلى استخدام هذه الثغرات الأمنية لمهاجمة العملاء. نحن نعمل بشكل وثيق مع شركاء الصناعة بما في ذلك صانعي الرقائق ومصنعي المعدات الأصلية للأجهزة وبائعي التطبيقات لحماية العملاء. للحصول على جميع وسائل الحماية المتاحة ، يلزم وجود تحديثات البرامج الثابتة (الرمز الصغير) والبرامج. يتضمن ذلك الرمز الصغير من الشركات المصنعة للجهاز ، وفي بعض الحالات ، تحديثات برامج مكافحة الفيروسات.

** تتناول هذه المقالة نقاط الضعف التالية: **
- CVE-2017-5715 - "إدخال هدف الفرع"
- CVE-2017-5753 - "تجاوز فحص الحدود"
- CVE-2017-5754 - "تحميل مخبأ للبيانات المخادعة"
- CVE-2018-3639 - "تجاوز المتجر التخميني"
- CVE-2018-11091 - "الذاكرة غير القابلة للتخزين لأخذ عينات البيانات المعمارية الدقيقة (MDSUM)"
- CVE-2018-12126 - "أخذ عينات بيانات المخزن المؤقت للمباني المعمارية الدقيقة (MSBDS)"
- CVE-2018-12127 - "أخذ عينات بيانات المخزن المؤقت للتعبئة المعمارية الدقيقة (MFBDS)"
- CVE-2018-12130 - "أخذ عينات بيانات منفذ التحميل المعماري الدقيق (MLPDS)"

** تم التحديث في 6 أغسطس 2019 ** في 6 أغسطس 2019 ، أصدرت إنتل تفاصيل حول ثغرة أمنية في الكشف عن معلومات نواة Windows. هذه الثغرة الأمنية هي أحد أشكال الثغرة الأمنية لقناة التنفيذ التخميني في Specter Variant 1 وقد تم تعيينها CVE-2019-1125.

** تم التحديث في 12 نوفمبر 2019 ** في 12 نوفمبر 2019 ، نشرت إنتل استشارة تقنية حول ثغرة عدم حصانة المعاملات غير المتزامنة التي تم إحباطها من Intel® (Intel® TSX) والتي تم تعيينها CVE-2019-11135. أصدرت Microsoft تحديثات للمساعدة في التخفيف من هذه الثغرة الأمنية وتم تمكين حماية نظام التشغيل افتراضيًا لإصدارات Windows Client OS.

## الإجراءات الموصى بها
يجب على العملاء اتخاذ الإجراءات التالية للمساعدة في الحماية من الثغرات الأمنية:

- تطبيق جميع تحديثات نظام التشغيل Windows المتاحة ، بما في ذلك تحديثات أمان Windows الشهرية.
- تطبيق تحديث البرنامج الثابت القابل للتطبيق (الرمز الصغير) الذي توفره الشركة المصنعة للجهاز.
- قم بتقييم المخاطر على بيئتك بناءً على المعلومات المتوفرة في إرشادات أمان Microsoft: ADV180002 و ADV180012 و ADV190013 والمعلومات الواردة في مقالة قاعدة المعارف هذه.
- اتخذ الإجراء المطلوب باستخدام الإرشادات ومعلومات مفتاح التسجيل المتوفرة في مقالة قاعدة المعارف هذه.

## تنزيل الملفات المطلوبة:

قم بتنزيل الملفات المطلوبة من ملف[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## كيفية تشغيل البرنامج النصي:

** قد يتم تشغيل البرنامج النصي من تنزيل GitHub المستخرج على النحو التالي: **
```
.\sos-spectre-meltdown-mitigations.ps1
```
