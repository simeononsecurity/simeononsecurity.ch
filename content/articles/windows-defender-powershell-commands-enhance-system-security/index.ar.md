---
title: "أوامر Windows Defender PowerShell لأمن النظام"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "تعرّف إلى أوامر Windows Defender PowerShell واستخدم التحكم عبر سطر الأوامر لتحسين أمن نظامك."
genre: ["Windows Defender", "أوامر PowerShell", "أمن النظام", "التحكم عبر سطر الأوامر", "مكافحة الفيروسات", "أنظمة تشغيل Windows", "الحماية من البرمجيات الخبيثة", "إعدادات الأمان المتقدمة", "أتمتة عمليات الأمان", "Windows PowerShell"]
tags: ["التقنية", "الأمن السيبراني", "أنظمة التشغيل", "Windows", "أدوات سطر الأوامر", "أمن النظام", "PowerShell", "مكافحة الفيروسات", "الحماية من البرمجيات الخبيثة", "البرمجة النصية"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "رسم متحرك لدرع يحمي نظام حاسوب من تهديدات سيبرانية مختلفة."
coverCaption: "عزّز أمن نظامك باستخدام أوامر Windows Defender PowerShell."
---

## المقدمة

طورت Microsoft برنامج Windows Defender، وهو حل مدمج لمكافحة الفيروسات وحماية أنظمة تشغيل Windows. ويوفر **واجهة سهلة الاستخدام** لإدارة إعدادات الأمان بفاعلية. أما المستخدمون المتقدمون الذين يفضلون التحكم عبر سطر الأوامر، فيستطيعون استخدام مجموعة أوامر PowerShell الخاصة به. يشرح هذا المقال **أوامر Windows Defender PowerShell** وكيفية استخدامها لتحسين أمن النظام والتحكم في بيئة Windows.

## إمكانات أوامر Windows Defender PowerShell

تتيح أوامر Windows Defender PowerShell تنفيذ **عمليات أمان متقدمة** من واجهة سطر الأوامر. وتشمل وظائف متعددة، من فحص البرمجيات الخبيثة إلى ضبط إعدادات الأمان المتقدمة. باستخدام PowerShell، تستطيع أتمتة عمليات الأمان وإنشاء نصوص مخصصة ودمج Windows Defender في سير العمل الحالي.

## بدء استخدام Windows Defender PowerShell

لاستخدام أوامر Windows Defender PowerShell، افتح جلسة PowerShell **بصلاحيات المسؤول**. اتبع الخطوات التالية:

1. اضغط `Win + X` واختر **Windows PowerShell (Admin)** (كمسؤول) من القائمة.
2. عند ظهور الطلب، انقر **Yes** (نعم) للسماح للتطبيق بإجراء تغييرات على جهازك.

بعد فتح جلسة PowerShell، ابدأ باستخدام أوامر Windows Defender PowerShell.

## أوامر Windows Defender PowerShell الشائعة

### 1. **Get-MpComputerStatus**: التحقق من حالة Windows Defender

يعرض الأمر `Get-MpComputerStatus` نظرة عامة على حالة Windows Defender الحالية في نظامك، ومنها إصدار محرك مكافحة الفيروسات ووقت آخر فحص وحالة الحماية في الوقت الفعلي. شغّل الأمر لتقييم الحالة العامة للبرنامج والتأكد من عمله كما ينبغي.

للتحقق من حالة Windows Defender، افتح **جلسة PowerShell بصلاحيات المسؤول** وشغّل الأمر التالي:

```powershell
Get-MpComputerStatus
```

يعرض هذا الأمر معلومات مثل:

- **AntivirusEngineVersion**: رقم إصدار محرك مكافحة الفيروسات الذي يستخدمه Windows Defender.
- **LastFullScanTime**: تاريخ ووقت آخر فحص كامل أجراه Windows Defender.
- **LastQuickScanTime**: تاريخ ووقت آخر فحص سريع أجراه Windows Defender.
- **RealTimeProtectionEnabled**: يبيّن ما إذا كانت الحماية في الوقت الفعلي مفعّلة أو معطّلة.

تساعدك مراقبة الحالة بانتظام باستخدام `Get-MpComputerStatus` على معرفة مستوى حماية نظامك من **التهديدات المحتملة**.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

يتيح لك الأمر `Update-MpSignature` تحديث **تواقيع مكافحة الفيروسات** التي يستخدمها Windows Defender يدويًا. تتضمن التواقيع معلومات أساسية عن البرمجيات الخبيثة المعروفة، وتساعد Windows Defender على اكتشاف التهديدات ومنعها. يضمن تشغيل الأمر حصول نظامك على أحدث التواقيع لمواجهة التهديدات الناشئة.

لتحديث تواقيع Windows Defender يدويًا، افتح جلسة PowerShell بصلاحيات المسؤول وشغّل الأمر التالي:

```powershell
Update-MpSignature
```

يبدأ هذا الأمر عملية التحديث، ويتصل Windows Defender بخوادم Microsoft لتنزيل أحدث تواقيع مكافحة الفيروسات. بعد اكتمال التحديث، تتوفر لدى Windows Defender أحدث معلومات البرمجيات الخبيثة المعروفة، مما يعزز قدرته على تحديد التهديدات وإزالتها.

يُعد تحديث تواقيع Windows Defender ضروريًا للحفاظ على مستوى الحماية مع تغير البرمجيات الخبيثة والتهديدات السيبرانية. حدّث التواقيع بانتظام باستخدام `Update-MpSignature` كي يتمكن Windows Defender من حماية نظامك بفاعلية.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

يساعدك الأمر `Set-MpPreference` على تخصيص إعدادات متعددة في **Windows Defender** لتوافق متطلبات الأمان لديك. ويتيح ضبط خيارات مثل **الحماية في الوقت الفعلي** و **الحماية المستندة إلى السحابة** وإعدادات **نظام فحص الشبكة**.

على سبيل المثال، تستطيع تفعيل الحماية في الوقت الفعلي أو تعطيلها باستخدام `Set-MpPreference`. تراقب هذه الحماية النظام بحثًا عن الأنشطة الضارة وتستجيب للتهديدات فورًا. لتفعيلها، شغّل الأمر التالي:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

يمكنك أيضًا ضبط الحماية المستندة إلى السحابة. تستخدم هذه الحماية **موارد السحابة** لتحسين اكتشاف التهديدات وتسريع الاستجابة لها. لتفعيلها، شغّل الأمر التالي:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

كذلك يتيح الأمر `Set-MpPreference` تخصيص إعدادات نظام فحص الشبكة. يحلل هذا النظام حركة مرور الشبكة للبحث عن أنشطة مشبوهة وتهديدات محتملة. لضبط إعداداته، شغّل الأمر التالي:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

اضبط هذه الخيارات باستخدام `Set-MpPreference` لمواءمة **Windows Defender** مع احتياجاتك الأمنية وحماية نظامك من البرمجيات الخبيثة والأنشطة الضارة الأخرى.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

يبدأ الأمر `Start-MpScan` فحوص البرمجيات الخبيثة على نظامك، ويساعدك على اكتشاف الملفات الضارة وإزالتها استباقيًا. ويدعم أنواعًا مختلفة من الفحوص، منها **الفحص السريع** و **الفحص الكامل** و **الفحص المخصص** لمسارات محددة.

لبدء **فحص سريع** باستخدام `Start-MpScan`، شغّل أمر PowerShell التالي:

```powershell
Start-MpScan -ScanType QuickScan
```

يركز الفحص السريع على مناطق النظام المهمة التي تظهر فيها البرمجيات الخبيثة عادةً، ويوفر تقييمًا سريعًا للتهديدات المحتملة.

لفحص جميع الملفات والمجلدات على النظام، ابدأ **فحصًا كاملًا** باستخدام `Start-MpScan`. شغّل الأمر التالي:

```powershell
Start-MpScan -ScanType FullScan
```

يوفر الفحص الكامل تغطية شاملة للبرمجيات الخبيثة، لكنه قد يستغرق وقتًا أطول من الفحص السريع.

إضافة إلى أنواع الفحص المحددة مسبقًا، يتيح لك `Start-MpScan` إجراء فحص مخصص لمسارات أو ملفات بعينها. على سبيل المثال، لفحص مجلد محدد، شغّل الأمر التالي:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

يبدأ هذا الأمر فحصًا مخصصًا للمجلد المحدد، لتوجيه البحث عن البرمجيات الخبيثة إلى مناطق معينة من النظام.

استخدم إمكانات الأمر `Start-MpScan` لجدولة الفحوص وأتمتة عمليات الأمان وضمان الكشف المنتظم عن البرمجيات الخبيثة والتعامل معها.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

يوفر الأمر `Get-MpThreatCatalog` معلومات مفصلة عن التهديدات المعروفة وخصائصها. ويعرض فهرسًا شاملًا للتهديدات يتضمن مستوى خطورتها وأسماء الملفات المرتبطة بها والإجراءات الموصى بها للتخفيف منها.

لاسترداد معلومات عن تهديدات محددة باستخدام `Get-MpThreatCatalog`، اتبع الخطوات التالية:

1. افتح جلسة PowerShell بصلاحيات المسؤول.
2. شغّل الأمر التالي:

```powershell
   Get-MpThreatCatalog
```

يعرض الأمر قائمة بالتهديدات المعروفة والتفاصيل المرتبطة بكل منها.

يتضمن ناتج الأمر `Get-MpThreatCatalog` معلومات مهمة مثل:

- **ThreatID**: معرّف فريد للتهديد.
- **Severity**: يحدد مستوى خطورة التهديد، من Low (منخفض) إلى Severe (شديد).
- **Name**: اسم التهديد أو وصفه.
- **Path**: مسار الملف المرتبط بالتهديد.
- **RecommendedAction**: إرشادات الإجراء الموصى به للتخفيف من التهديد.

استخدم المعلومات الناتجة من `Get-MpThreatCatalog` لفهم التهديدات المحتملة واتخاذ قرارات مدروسة بشأن الإجراءات المناسبة للتعامل معها. سواء أكان الإجراء عزل تهديد محدد أو إزالته أو مراقبته، يساعدك الفهرس المفصل على الاستجابة للحوادث الأمنية بفاعلية.

لمعرفة المزيد عن استخدام `Get-MpThreatCatalog` وتفسير نتائجه، راجع وثائق Microsoft الرسمية.

ابقَ متيقظًا وشغّل الأمر `Get-MpThreatCatalog` بانتظام لمتابعة التهديدات المتغيرة وتعزيز أمن نظامك.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

يساعدك الأمر `Add-MpPreference` على إضافة استثناءات إلى Windows Defender وتخصيص سلوكه أثناء الفحص والحماية في الوقت الفعلي. تحدد الاستثناءات ملفات أو مجلدات أو عمليات تتجاهلها عمليات الفحص والحماية الفورية.

لإضافة استثناء باستخدام `Add-MpPreference`، حدّد مسار الملف أو المجلد أو اسم العملية المطلوب استثناؤها. يضيف المثال التالي استثناءً لمجلد:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

يتجاوز Windows Defender فحص المجلد المحدد، مما يقلل التنبيهات غير الضرورية والمقاطعات المحتملة لسير عملك.

تفيد الاستثناءات في حالات مثل استبعاد تطبيقات موثوقة أو بيئات تطوير أو ملفات معينة قد تؤدي إلى نتائج إيجابية كاذبة. استخدم `Add-MpPreference` لضبط Windows Defender وفق احتياجات الأمان لديك وتحسين أدائه.

احمِ نظامك مع تقليل النتائج الإيجابية الكاذبة ومقاطعات الفحص غير الضرورية باستخدام إمكانات الاستثناء في `Add-MpPreference`.

## فحوص أوامر Defender في 2026

شغّل أوامر Defender من جلسة بصلاحيات مرتفعة فقط عندما تتطلب المهمة ذلك. راجع تعليمات الوحدة الحالية لإصدار Windows المستهدف قبل استخدام أي وسيط. سجّل الإعدادات الحالية، وغيّر إعدادًا واحدًا في كل مرة، وتحقق من النتيجة وسجّل أمر التراجع.

تشمل خطوات المراجعة المفيدة فحص حالة الحماية وعمر التواقيع والاستثناءات والتفضيلات وسجل الفحوص والاكتشافات الأخيرة. اجعل الاستثناءات محدودة ووثّق المسؤول عنها وتاريخ انتهائها. راجع [وثائق وحدة Microsoft Defender PowerShell](https://learn.microsoft.com/en-us/powershell/module/defender/) و[وثائق Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) للاطلاع على الأوامر وسلوكها الحالي.

## الخلاصة

تقدم أوامر Windows Defender PowerShell مجموعة **متينة من الأدوات** لإدارة أمن نظام Windows وتعزيزه. وباستخدامها تستطيع *أتمتة عمليات الأمان* و *ضبط الإعدادات المتقدمة* ودمج Windows Defender في سير عملك. سواء أكنت مسؤول نظام أم مستخدمًا متقدمًا، فإن استخدام هذه الأوامر يعزز الوضع الأمني لنظامك.

تذكّر أن استخدام أوامر PowerShell يتطلب الحذر وفهم أثرها قبل التنفيذ. اجمع معرفتك بأوامر Windows Defender PowerShell واتخذ خطوات استباقية لحماية نظامك من التهديدات المتغيرة.

## المراجع

1. Microsoft Docs - [أوامر Windows Defender في Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [مقدمة إلى Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
