---
title: "برمجة PowerShell النصية"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "تعرّف إلى أساسيات البرمجة النصية باستخدام PowerShell وأتمتة المهام عبر دليل عملي للمبتدئين يتناول أوامر cmdlet والحلقات والدوال وغير ذلك."
genre: ["التقنية", "البرمجة", "الأتمتة", "Windows", "البرمجة النصية", "تقنية المعلومات", "المهام الإدارية", "إدارة الحاسوب", "تطوير البرمجيات", "الترميز"]
tags: ["برمجة PowerShell النصية", "أتمتة PowerShell", "برمجة Windows النصية", "أوامر PowerShell cmdlet", "وحدات PowerShell", "حلقات PowerShell", "عبارات PowerShell الشرطية", "دوال PowerShell", "أفضل ممارسات PowerShell", "تصحيح أخطاء PowerShell", "اختبار PowerShell", "متغيرات PowerShell", "PowerShell ISE", "PowerShell Remoting", "تقنيات Microsoft", "أتمتة تقنية المعلومات", "إدارة الحاسوب", "البرمجة للمبتدئين", "المهام الإدارية", "أفكار لبرامج PowerShell النصية", "النسخ الاحتياطي الآلي", "إدارة الملفات", "معلومات النظام", "إدارة المستخدمين", "تثبيت البرامج", "تهيئة الشبكة", "أتمتة الأمان", "جدولة المهام", "التعامل مع السجل", "الإدارة عن بُعد"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "شخصية كرتونية تحمل برنامجًا نصيًا وتقف أمام حاسوب يعرض موجه PowerShell، في إشارة إلى سهولة تعلم البرمجة النصية به للمبتدئين"
coverCaption: ""
---
**تعلم برمجة PowerShell النصية للمبتدئين**

PowerShell هو صدفة لسطر الأوامر ولغة برمجة نصية طورتها Microsoft. يضم مجموعة واسعة من الأوامر والميزات لإدارة جوانب مختلفة من نظام Windows وتقنيات Microsoft الأخرى وأتمتتها. نستعرض في هذا المقال أساسيات البرمجة النصية باستخدام PowerShell، ونقدم دليلًا خطوة بخطوة للبدء.

## مقدمة إلى PowerShell

**PowerShell** صدفة لسطر الأوامر تتيح للمستخدمين أتمتة نظام Windows وتقنيات Microsoft الأخرى وإدارتها. توفر مجموعة شاملة من الأوامر والميزات لتنفيذ مهام إدارية متنوعة، مثل إدارة الملفات والمجلدات وتهيئة الشبكة وإدارة النظام. كما تدعم لغة برمجة نصية تتيح إنشاء برامج معقدة وأتمتة المهام المتكررة.

## البدء باستخدام PowerShell

### تثبيت PowerShell

يأتي PowerShell مثبتًا مسبقًا في معظم إصدارات نظام Windows. إذا كنت تستخدم إصدارًا أقدم من Windows أو تحتاج إلى إصدار أحدث من PowerShell، فنزّله من موقع Microsoft. اتبع الخطوات التالية لتنزيل PowerShell وتثبيته:

1. انتقل إلى [موقع Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) واختر إصدار PowerShell الذي تريد تثبيته.
2. نزّل ملف التثبيت وشغّله.
3. اتبع التعليمات التي تظهر على الشاشة لإكمال عملية التثبيت.

### تشغيل PowerShell

بعد تثبيت PowerShell، شغّله بهذه الخطوات:

1. افتح قائمة Start واكتب "PowerShell" في شريط البحث.
2. اختر "Windows PowerShell" من نتائج البحث.
3. ستفتح PowerShell في نافذة جديدة.

### البرمجة النصية باستخدام PowerShell في Visual Studio Code

للحصول على تجربة برمجة نصية أفضل، يمكنك استخدام Visual Studio Code (VS Code)، وهي بيئة تطوير متكاملة (IDE) شائعة. يوفر VS Code تمييز الصياغة وإكمال التعليمات البرمجية وتصحيح الأخطاء ودعمًا لطرفية مدمجة، ما يجعله خيارًا مناسبًا لبرمجة PowerShell النصية. للبدء باستخدام PowerShell في VS Code، اتبع الخطوات التالية:

1. ثبّت Visual Studio Code من [الموقع الرسمي](https://code.visualstudio.com/).
2. ثبّت إضافة "PowerShell" من Microsoft عبر سوق الإضافات داخل VS Code.
3. افتح ملف برنامج PowerShell النصي بامتداد (.ps1) في VS Code، وابدأ البرمجة.

### PowerShell لإدارة الأنظمة

PowerShell أداة متعددة الاستخدامات لمهام إدارة الأنظمة. فهو يسهّل تنفيذ المهام التي تتطلب تدخلًا يدويًا، بدءًا من أمر واحد قصير وصولًا إلى تدفقات عمل الأتمتة المعقدة. كما يوفر منصة برمجة نصية موحدة لأنظمة Windows وLinux وmacOS، ويمنح المسؤولين مجموعة أدوات متسقة لإدارة بيئات مختلفة.

### الانتقال من Command Prompt إلى Windows PowerShell

إذا كنت معتادًا على Command Prompt وتريد الانتقال إلى Windows PowerShell، فالتعلم سلس. تعتمد برمجة Windows PowerShell النصية على مفاهيم Command Prompt، لكنها تضيف إمكانات أكثر تقدمًا. يمكنك الاستفادة سريعًا من معرفتك الحالية ثم استكشاف الميزات الإضافية وأوامر cmdlet التي يوفرها PowerShell تدريجيًا.

### أساسيات PowerShell

يوفر PowerShell واجهة لسطر الأوامر تتيح للمستخدمين التفاعل مع نظام التشغيل. تسمى أوامره cmdlet، وهي منظمة ضمن وحدات. لعرض قائمة الوحدات المتاحة، استخدم الأمر Get-Module:

```powershell
Get-Module
```

لعرض أوامر cmdlet المتاحة في وحدة، استخدم الأمر Get-Command:
```powershell
Get-Command -Module <module name>
```

للحصول على تعليمات حول أمر cmdlet، استخدم الأمر Get-Help:
```powershell
Get-Help <cmdlet name>
```

يدعم PowerShell أيضًا الأسماء المستعارة، وهي أسماء أقصر لأوامر cmdlet. لعرض قائمة الأسماء المستعارة المتاحة، استخدم الأمر Get-Alias:
```powershell
Get-Alias
```

## ملفات البرامج النصية وسياسة التنفيذ

تستخدم ملفات PowerShell النصية الامتداد .ps1. قبل تشغيل البرامج النصية، قد تحتاج إلى ضبط سياسة التنفيذ، التي تحدد ما إذا كان مسموحًا بتشغيل البرامج النصية وأنواعها المسموح بها. لضبط السياسة، استخدم أمر cmdlet المسمى Set-ExecutionPolicy. على سبيل المثال، للسماح بتشغيل البرامج النصية، استخدم:

```powershell
Set-ExecutionPolicy RemoteSigned
```

أو (لأغراض الاختبار فقط)

```powershell
Set-ExecutionPolicy Undefined
```

### البرمجة النصية باستخدام PowerShell

تتيح البرمجة النصية باستخدام PowerShell أتمتة مهام إدارية متنوعة. وهي تدعم المتغيرات والحلقات والعبارات الشرطية والدوال، ما يجعلها أداة قوية للأتمتة.

#### المتغيرات

تُستخدم المتغيرات لتخزين البيانات في برامج PowerShell النصية. تبدأ أسماء المتغيرات في PowerShell بعلامة الدولار ($). لإسناد قيمة إلى متغير، استخدم الصيغة التالية:
```powershell
$variable_name = value
```
على سبيل المثال:
```powershell
$name = "John"
```
#### الحلقات

تكرر الحلقات كتلة من التعليمات البرمجية عددًا محددًا من المرات. يدعم PowerShell أنواع الحلقات التالية:

- **حلقة For**: تكرر كتلة تعليمات برمجية عددًا محددًا من المرات.
- **حلقة While**: تكرر كتلة تعليمات برمجية ما دام الشرط صحيحًا.
- **حلقة Do-While**: تنفذ كتلة تعليمات برمجية مرة واحدة على الأقل، ثم تكررها ما دام الشرط صحيحًا.
- **حلقة ForEach**: تكرر كتلة تعليمات برمجية لكل عنصر في مجموعة.

على سبيل المثال، يستخدم الكود التالي حلقة For لطباعة الأرقام من 1 إلى 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### العبارات الشرطية

العبارات الشرطية

تُستخدم العبارات الشرطية لتنفيذ كتلة من التعليمات البرمجية إذا تحقق شرط معين. يدعم PowerShell الأنواع التالية من العبارات الشرطية:

- **عبارة If**: تنفذ كتلة تعليمات برمجية إذا تحقق الشرط.
- **عبارة If-Else**: تنفذ إحدى الكتلتين وفقًا لتحقق الشرط أو عدم تحققه.
- **عبارة Switch**: تقارن قيمة بمجموعة من القيم المحتملة وتنفذ الكتلة الخاصة بأول تطابق.

على سبيل المثال، يستخدم الكود التالي عبارة If للتحقق مما إذا كان الرقم أكبر من 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "الرقم أكبر من 5"
}
```
#### الدوال

الدوال كتل تعليمات برمجية قابلة لإعادة الاستخدام وتنفذ مهمة محددة. تستقبل الدوال معلمات إدخال وتعيد قيمًا ناتجة. يدعم PowerShell الأنواع التالية من الدوال:

- **كتلة البرامج النصية**: كتلة تعليمات برمجية يمكن تنفيذها.
- **دالة متقدمة**: دالة تتضمن بيانات وصفية والتحقق من صحة المعلمات.

على سبيل المثال، تعرف الشيفرة التالية دالة تجمع رقمين:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "النتيجة هي $result"
```
### PowerShell ISE

PowerShell ISE (بيئة البرمجة النصية المتكاملة) واجهة رسومية لبرمجة PowerShell النصية. يوفر PowerShell ISE محرر نصوص غنيًا وأدوات لتصحيح الأخطاء وميزات أخرى تسهّل كتابة برامج PowerShell النصية واختبارها. لفتح PowerShell ISE، اتبع الخطوات التالية:

1. افتح قائمة Start واكتب "PowerShell ISE" في شريط البحث.
2. اختر "Windows PowerShell ISE" من نتائج البحث.
3. ستفتح PowerShell ISE في نافذة جديدة.

### PowerShell Remoting

تتيح ميزة PowerShell Remoting تشغيل أوامر PowerShell وبرامجه النصية على حواسيب بعيدة. وتتطلب تشغيل خدمة WinRM على الحاسوب المحلي والحاسوب البعيد. لتمكين PowerShell Remoting، اتبع الخطوات التالية:

1. افتح موجه PowerShell بصلاحيات المسؤول.
2. شغّل الأمر التالي لتمكين PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. شغّل الأمر التالي لإضافة الحاسوب البعيد إلى قائمة TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. أعد تشغيل خدمة WinRM.
```powershell
Restart-Service WinRM
```

لتشغيل أمر PowerShell على حاسوب بعيد، استخدم أمر cmdlet المسمى Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### وحدات PowerShell

وحدات PowerShell مجموعات من أوامر cmdlet والدوال والبرامج النصية المصممة لمهام محددة. يمكن تثبيت هذه الوحدات وإدارتها باستخدام PowerShell Gallery، وهو مستودع مركزي لوحدات PowerShell.

لتثبيت وحدة من PowerShell Gallery، استخدم الأمر التالي:
```powershell
Install-Module <module name>
```

لعرض وحدات PowerShell المثبتة، استخدم الأمر Get-InstalledModule:
```powershell
Get-InstalledModule
```

### أفضل الممارسات لبرمجة PowerShell النصية

عند كتابة **برامج PowerShell النصية**، اتبع أفضل الممارسات كي تكون البرامج **آمنة** و**موثوقة** و**سهلة الصيانة**. إليك بعض الممارسات التي يجدر اتباعها:

- **استخدم أسماء متغيرات وصفية**: اختر أسماء توضح الغرض من المتغير.
- **استخدم التعليقات**: اشرح الغرض من التعليمات البرمجية بالتعليقات.
- **تعامل مع الأخطاء**: عالج الأخطاء والاستثناءات بطريقة مناسبة. يتيح تركيب `Try...Catch...Finally` في PowerShell معالجة الاستثناءات واتخاذ الإجراء الملائم. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **اختبر البرامج النصية بدقة**: تأكد من عملها كما هو متوقع. يمكنك استخدام **Pester**، وهو إطار اختبار لـ PowerShell، لكتابة اختبارات الوحدة وتشغيلها. [وثائق Pester](https://pester.dev/)
- **استخدم الدوال والوحدات**: نظّم التعليمات البرمجية وحسّن إعادة استخدامها. تتيح لك الدوال تقسيم الشيفرة إلى أجزاء صغيرة يمكن إدارتها، وتوفر الوحدات طريقة لتجميع الشيفرة وتوزيعها. [معلومات عن الدوال](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1)، [معلومات عن الوحدات](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **تجنب تثبيت القيم في الشيفرة**: استخدم المعلمات أو المتغيرات بدلًا من القيم الثابتة. يجعل ذلك البرامج النصية أكثر مرونة وقابلية لإعادة الاستخدام. مرّر المعلمات إلى البرنامج النصي باستخدام الكلمة المفتاحية `param`. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **استخدم المخرجات التفصيلية**: اعرض معلومات إضافية عن تقدم البرنامج النصي. استخدم أمر cmdlet المسمى `Write-Verbose` لإظهار رسائل تفصيلية أثناء التنفيذ. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### شرح أفضل الممارسات لبرمجة PowerShell النصية

#### معالجة الأخطاء

معالجة الأخطاء جانب أساسي في البرمجة النصية باستخدام PowerShell، لأنها تضمن تعامل البرنامج مع الأخطاء والاستثناءات بطريقة مناسبة. يوفر PowerShell عدة وسائل لمعالجة الأخطاء، منها عبارة Try-Catch وعبارة Trap ومعلمة ErrorAction. تُستخدم عبارة Try-Catch لالتقاط الاستثناءات ومعالجتها، بينما تُستخدم عبارة Trap لالتقاط الأخطاء ومعالجتها. وتتحكم معلمة ErrorAction في طريقة تعامل البرنامج النصي مع الأخطاء.

إليك مثالًا على استخدام عبارة Try-Catch لمعالجة خطأ:
```powershell
try {
    # كود قد يسبب خطأ
}
catch {
    Write-Error "حدث خطأ: $_"
}
```

#### اختبر البرامج النصية بدقة

اختبار برامج PowerShell النصية ضروري للتأكد من أنها تعمل كما هو متوقع. يوفر PowerShell أدوات وأطر اختبار متعددة، مثل Pester، تتيح كتابة الاختبارات وتشغيلها. تساعد هذه الأدوات على تحديد المشكلات وعزلها في التعليمات البرمجية، والتأكد من تلبية البرنامج النصي للمتطلبات المطلوبة.

إليك مثالًا على استخدام Pester لاختبار برنامج PowerShell نصي:
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # كود يفترض أن يعيد النتيجة المتوقعة
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### استخدم الدوال والوحدات

الدوال والوحدات أساسية لتنظيم التعليمات البرمجية وتحسين إمكانية إعادة استخدامها في PowerShell. تتيح الدوال تجميع الشيفرة في كتل قابلة لإعادة الاستخدام، بينما تتيح الوحدات تجميع الشيفرة ومشاركتها مع الآخرين. يساعد استخدام الدوال والوحدات على جعل البرامج النصية أكثر نمطية وكفاءة وأسهل صيانة.

إليك مثالًا على استخدام دالة في PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "هناك $count عملية قيد التشغيل."
```

#### تجنب تثبيت القيم في الشيفرة

يقلل تثبيت القيم في برنامج PowerShell النصي من مرونته ويصعّب صيانته. بدلًا من ذلك، استخدم المعلمات أو المتغيرات كي يتمكن المستخدمون من تمرير القيم وقت التشغيل. وهكذا يصبح البرنامج النصي أكثر قابلية لإعادة الاستخدام والتكيف مع الظروف المتغيرة.

إليك مثالًا على استخدام معلمة في PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "مرحبًا، $name!"
```

#### استخدم المخرجات التفصيلية

توفر المخرجات التفصيلية معلومات إضافية عن تقدم البرنامج النصي، وقد تفيد في تصحيح الأخطاء واستكشاف المشكلات. يتيح أمر cmdlet المسمى Write-Verbose إخراج معلومات تفصيلية إلى وحدة التحكم. يجعل هذا برامج PowerShell النصية أكثر إفادة وأسهل في تصحيح الأخطاء.

إليك مثالًا على استخدام المخرجات التفصيلية في PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "هناك $count عملية قيد التشغيل."
```

### عشر أفكار لبرامج PowerShell النصية للمبتدئين

إذا كنت مبتدئًا في البرمجة النصية باستخدام PowerShell، فإليك عشر أفكار تساعدك على البدء:

- **النسخ الاحتياطي الآلي**: أنشئ برنامجًا نصيًا لأتمتة نسخ الملفات والمجلدات المهمة احتياطيًا إلى قرص صلب خارجي أو خدمة تخزين سحابي. استخدم أمر cmdlet المسمى `Copy-Item` لنسخ الملفات و`Start-Job` لتشغيل عملية النسخ الاحتياطي في الخلفية. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **إدارة الملفات**: أنشئ برنامجًا نصيًا لتنظيم الملفات والمجلدات ونقلها إلى مجلدات مختلفة وفقًا لنوع الملف أو حجمه أو معايير أخرى. استخدم `Get-ChildItem` لاسترداد الملفات و`Move-Item` لنقلها إلى الموقع المطلوب. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **معلومات النظام**: أنشئ برنامجًا نصيًا يسترجع معلومات النظام، مثل استخدام وحدة المعالجة المركزية والذاكرة والمساحة على القرص وإعدادات الشبكة، ثم يعرضها بتنسيق سهل القراءة. استخدم `Get-WmiObject` لجمع معلومات النظام، ونسّقها باستخدام `Format-Table` أو `Out-GridView`. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **إدارة المستخدمين**: أنشئ برنامجًا نصيًا لأتمتة إضافة المستخدمين والمجموعات أو تعديلهم أو حذفهم في Windows. استخدم `New-LocalUser` و`Set-LocalUser` و`Remove-LocalUser` لإدارة المستخدمين، واستخدم `New-LocalGroup` و`Add-LocalGroupMember` و`Remove-LocalGroup` لإدارة المجموعات. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **تثبيت البرامج**: أنشئ برنامجًا نصيًا يثبّت البرامج ويهيئها على عدة حواسيب دفعة واحدة، لتوفير الوقت والجهد. استخدم `Invoke-Command` لتنفيذ أوامر التثبيت على الحواسيب البعيدة. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **تهيئة الشبكة**: أنشئ برنامجًا نصيًا لأتمتة ضبط إعدادات الشبكة، مثل عنوان IP وقناع الشبكة الفرعية والبوابة الافتراضية. استخدم `Set-NetIPAddress` و`Set-NetIPInterface` و`Set-DnsClientServerAddress` لضبط هذه الإعدادات. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **الأمان**: أنشئ برنامجًا نصيًا يراجع إعدادات الأمان ويراقبها، وينبه المستخدم عند اكتشاف تغييرات. استخدم `Get-AuditPolicy` لاسترداد سياسات التدقيق، و`Send-MailMessage` لإرسال إشعارات بالبريد الإلكتروني. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **جدولة المهام**: أنشئ برنامجًا نصيًا لجدولة المهام المتكررة وأتمتتها، مثل النسخ الاحتياطي والتحديثات وفحوص النظام. استخدم `Register-ScheduledTask` لإنشاء المهام المجدولة و`Start-ScheduledTask` لتشغيلها. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **التعامل مع السجل**: أنشئ برنامجًا نصيًا لتعديل قيم السجل أو استردادها لمفاتيح أو قيم محددة. استخدم `Get-ItemProperty` و`Set-ItemProperty` للتعامل مع السجل. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **الإدارة عن بُعد**: أنشئ برنامجًا نصيًا لتمكين الإدارة عن بُعد لحواسيب Windows، بما يتيح للمستخدمين تنفيذ الأوامر والبرامج النصية على أجهزة بعيدة. استخدم أمر cmdlet المسمى `Enter-PSSession` أو `Invoke-Command` لتشغيل الأوامر على الحواسيب البعيدة. [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1)، [وثائق Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

ابدأ باستكشاف هذه الأفكار لاكتساب خبرة عملية وتوسيع معرفتك ببرمجة PowerShell النصية.

## الخلاصة

PowerShell أداة قوية لإدارة نظام Windows وتقنيات Microsoft الأخرى وأتمتتها. تناولنا في هذا المقال أساسيات البرمجة النصية للمبتدئين، بما فيها التثبيت والتشغيل واستخدام أوامر cmdlet والمتغيرات والحلقات والعبارات الشرطية والدوال، إلى جانب PowerShell ISE وPowerShell Remoting ووحدات PowerShell. تساعد أفضل الممارسات على جعل البرامج النصية آمنة وموثوقة وسهلة الصيانة. ومع التدريب، ستتمكن من إتقان PowerShell وأتمتة مهام إدارية متنوعة بسهولة.
