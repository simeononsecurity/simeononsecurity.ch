---
title: "إنشاء جرد للقراءة فقط في Active Directory باستخدام PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "احصر الوحدات التنظيمية والمستخدمين وأجهزة الكمبيوتر في Active Directory باستخدام استعلامات PowerShell محددة النطاق. صدّر ملفات CSV قابلة للمراجعة من دون تغيير كائنات الدليل."
genre: ["Active Directory", "PowerShell", "إدارة الأنظمة"]
tags: ["جرد Active Directory", "جرد AD باستخدام PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD للقراءة فقط", "تصدير مستخدمي AD", "تصدير أجهزة AD", "تصدير وحدات OU", "Export-Csv", "RSAT", "تدقيق الدليل", "تقارير AD", "جرد OU", "Windows Server", "برنامج PowerShell نصي", "وحدة AD", "نظافة الدليل"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "شجرة Active Directory تتدفق منها سجلات المستخدمين وأجهزة الكمبيوتر والوحدات التنظيمية إلى ثلاثة ملفات للمراجعة."
coverCaption: "حدّد نطاق الاستعلام، ثم صدّر الحقول اللازمة للمراجعة فقط."
---
يبدأ تنظيف Active Directory بقائمة موثوقة للكائنات الموجودة. يجمع هذا **الجرد المخصص للقراءة فقط** الوحدات التنظيمية والمستخدمين وأجهزة الكمبيوتر ضمن نطاق تختاره. ويصدّر ثلاثة ملفات CSV (قيم مفصولة بفواصل) للمراجعة من دون تغيير كائنات الدليل. احمِ هذه الملفات أيضًا، لأن الأسماء وتفاصيل الأجهزة تكشف جزءًا من بيئتك.

<!--more-->

## أهم النقاط

- **اختر نطاقًا:** استعلم عن وحدة تنظيمية واحدة قبل توسيع البحث ليشمل المجال كله.
- **استخدم أوامر القراءة:** تسترجع `Get-ADOrganizationalUnit` و`Get-ADUser` و`Get-ADComputer` الكائنات.
- **اختر الحقول:** صدّر الخصائص اللازمة للمهمة فقط.
- **تحقق من النتائج:** قارن العدد وبعض الصفوف النموذجية قبل الاعتماد على التقرير.

## قبل البدء

تحتاج إلى مضيف إدارة يعمل بنظام Windows مع DNS سليم واتصال شبكي بوحدة تحكم المجال، ووحدة PowerShell النمطية **ActiveDirectory**، وحساب مصرح له بقراءة الكائنات المحددة، ومجلد محمي لملفات CSV. في عميل Windows، تأتي الوحدة مع أدوات Active Directory ضمن Remote Server Administration Tools (RSAT). يشرح [دليل وحدة Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) التثبيت. توفر Microsoft [مرجع أوامر الوحدة](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) و[خيارات تثبيت RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). يستخدم هذا الدليل صياغة Windows PowerShell ولا يغيّر كائنات الدليل.

تظل أذونات الدليل سارية. توضح Microsoft في [إرشادات الحسابات ذات الامتيازات](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) أن قوائم التحكم بالوصول تسمح غالبًا للمستخدمين المصادق عليهم بقراءة المعلومات العامة، مع تقييد الحقول الحساسة والتغييرات. ابدأ بحساب معتمد ووحدة OU اختبارية. لا ترفع الامتيازات إلى Domain Admin كي ينجح الجرد.

> **تحذير:** تحتوي ملفات CSV على أسماء الحسابات وأجهزة الكمبيوتر. احفظها في موقع معتمد، وقيّد الوصول إليها، واحذف النسخ الإضافية بعد المراجعة. لا تنشر تصديرًا خامًا ولا ترفقه بمسألة عامة.

## اختيار قاعدة البحث

تجمع **الوحدة التنظيمية (OU)** كائنات الدليل. ويحدد **الاسم المميز (DN)** موضعها في شجرة الدليل. يقيّد المعامل `-SearchBase` الاستعلام بالاسم المميز المحدد. ومن دون نطاق مقصود، قد يعيد عامل تصفية واسع كائنات أكثر بكثير مما تحتاج إلى مراجعته.

حمّل الوحدة أولًا واعرض الاسم المميز للمجال الحالي:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

توثق Microsoft الأمر [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) ومعلومات المجال التي يعيدها. حدّد وحدة OU التي تريد مراجعتها قبل ضبط قاعدة البحث:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

انسخ الاسم المميز الدقيق من النتيجة. واستبدل قيمة التوثيق هذه في الأمثلة التالية بالاسم المميز لوحدة OU لديك:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` مجال مخصص للتوثيق. لا تنسخ اسمه المميز إلى استعلام فعلي. إذا كنت تحتاج عمدًا إلى جرد المجال كله، فعيّن الاسم المميز للمجال إلى `$SearchBase` وسجّل هذا النطاق الأوسع في التقرير. يشرح [مرجع Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) من Microsoft المعاملين `-Filter` و`-SearchBase`.

## جرد الوحدات والمستخدمين والأجهزة

ابدأ بعدّ الكائنات. يساعدك ذلك على اكتشاف قاعدة بحث خاطئة أو نتيجة فارغة غير متوقعة بسرعة:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

تعني `-Filter *` استرجاع جميع الكائنات المطابقة ضمن قاعدة البحث. توثق Microsoft [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) و[Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) كأمرين للاسترجاع. قد يكون العدد صفرًا نتيجة صحيحة، لكن تحقق من الاسم المميز والأذونات والمجال المستهدف قبل اعتبار الجرد كاملًا.

اعرض الآن بعض الصفوف في وحدة التحكم. احفظ الحقول المحددة كي يستخدم العرض الأولي وتصدير CSV اللاحق الأعمدة نفسها:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

اطلب خاصية نظام التشغيل الإضافية لأجهزة الكمبيوتر عند الحاجة إليها للمراجعة فقط:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

يطلب المعامل `-Properties` خصائص خارج المجموعة الافتراضية للأمر. توضح Microsoft ذلك في [مرجع أمر أجهزة الكمبيوتر](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). تعامل مع أسماء أنظمة التشغيل بوصفها بيانات دليل، لا دليلًا على الإصدار المثبت حاليًا. فقد يكون كائن الكمبيوتر قديمًا أو لم تُحدّث خاصيته بعد.

## تصدير ملفات CSV قابلة للمراجعة

اختر مجلد إخراج معتمدًا تتوفر فيه مساحة كافية. تكتب الأوامر التالية **ملفات CSV محلية** ولا تغيّر كائنات الدليل. شغّلها من هذا المجلد. يمنع `-NoClobber` استبدال ملف موجود. استخدم مجلدًا أو اسم ملف جديدًا في كل مرة.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

يشرح [مرجع Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) من Microsoft المعاملات `-NoTypeInformation` و`-Encoding` و`-NoClobber`. افتح كل ملف CSV في محرر نصوص أو أداة جداول معتمدة. تحقق من العنوان وبعض الصفوف وعدد السجلات مقارنة بالعدد السابق. لا يثبت فشل الأمر أو إنشاء ملف حجمه صفر اكتمال التقرير.

> **النتيجة المتوقعة:** لديك ثلاثة ملفات CSV تضم سجلات الوحدات والمستخدمين وأجهزة الكمبيوتر ضمن نطاق الدليل المحدد. يتطابق عدد الصفوف والقيم النموذجية مع النطاق المختار.

## المراجعة دون تغيير الكائنات

استخدم الجرد للإجابة عن أسئلة محددة: ما الوحدة المسؤولة عن جهاز كمبيوتر؟ ما حسابات المستخدمين المعطلة؟ ما أسماء الأجهزة التي تحتاج إلى مسؤول؟ سجّل النتائج في ملاحظة مراجعة منفصلة. لا تعتبر قيمة `Enabled` دليلًا على استمرار الحاجة إلى الحساب. ولا تحذف كائنًا أو تعطّله استنادًا إلى تصدير وحده.

في التقارير المتكررة، سجّل تاريخ الاستعلام والمجال والاسم المميز لوحدة OU والخصائص المختارة والمشغّل وموقع ملف CSV. عند مقارنة تصديرين، تحقق من استخدام النطاق والحقول نفسيهما. وإلا فقد ينتج الاختلاف من الاستعلام بدلًا من تغيير فعلي في الدليل.

هذا **جرد** وليس تدقيقًا للحسابات ذات الامتيازات ولا تقريرًا لنشاط تسجيل الدخول. تشير Microsoft إلى أن خصائص Active Directory وأذوناته تختلف حسب الكائن والبيئة. تحقق من خاصية نظام التشغيل أو الاسم المعروض لدى مسؤول النظام قبل التصرف بناءً عليهما. يتناول [دليل أمان Active Directory](/articles/active-directory-security-best-practices/) ضوابط أمان أوسع.

## استكشاف الأخطاء وإصلاحها

- **تعذر استيراد الوحدة:** تحقق من تثبيت أدوات Active Directory من RSAT أو أدوات إدارة Windows Server على المضيف. اتبع [دليل إعداد الوحدة](/articles/active-directory-module-powershell-installation-usage-guide/).
- **لا يعيد الاستعلام كائنات:** تحقق من الاسم المميز الدقيق والمجال الحالي ومحتوى وحدة OU وأذونات القراءة. جرّب وحدة OU صغيرة معروفة قبل توسيع النطاق.
- **خاصية فارغة:** تحقق من وجود السمة ومن قدرة حسابك على قراءتها. لا تملأ الحقول الناقصة بالتخمين.
- **يذكر التصدير أن الملف موجود:** حمى `-NoClobber` التقرير السابق. اختر اسم ملف أو مجلدًا جديدًا وأعد تشغيل الأمر.
- **العدد لا يطابق التوقعات:** تحقق مما إذا كان المستخدمون أو الأجهزة في وحدة OU أخرى، أو تغير النطاق، أو تغير الدليل أثناء الاستعلام.

## الخطوات التالية

احتفظ بملفات CSV الخام في موقع محمي طوال فترة المراجعة المتفق عليها. شارك الحقول التي يحتاج إليها المراجع فقط. بعد تأكيد المسؤولين للنتائج، خطط للتغييرات وفق إجراءات الاعتماد والتراجع المعتادة. وبعد التغييرات المعتمدة، أعد الجرد نفسه بالنطاق نفسه لتأكيد النتيجة.