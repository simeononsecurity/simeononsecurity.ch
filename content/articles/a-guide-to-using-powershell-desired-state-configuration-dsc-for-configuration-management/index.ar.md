---
title: "PowerShell DSC: دليل للمبتدئين"
date: 2023-04-02
toc: true
draft: false
description: استكشف قوة PowerShell Desired State Configuration (DSC) لأتمتة وإدارة تكوينات النظام من أجل بيئة آمنة ومتوافقة.
tags:
- PowerShell
- DSC
- إدارة التكوين
- الأتمتة
- ويندوز
- إدارة النظام
- أفضل الممارسات
- الامتثال
- الأمان
- البنية التحتية
- DevOps
- تكوين الخادم
- الاختبار
- Git
- التحكم بالمصدر
- لوائح حكومية
- NIST
- CIS
- انحراف التكوين
- الموارد المخصصة
cover: /img/cover/a-guide-to-using-powershell-desired-state-configuration-dsc-for-configuration-management.webp
coverAlt: رسم توضيحي يظهر محطة PowerShell بأسلوب مميز مع رموز مجردة حولها، تمثل إدارة التكوين والأتمتة، على خلفية زرقاء داكنة.
coverCaption: ''
lastmod: 2026-10-08
---

**دليل لاستخدام PowerShell Desired State Configuration (DSC) لإدارة التكوين**

______

## المقدمة

PowerShell Desired State Configuration (**DSC**) هو أداة قوية و**أساسية** لمسؤولي تكنولوجيا المعلومات ومحترفي DevOps، تتيح لهم أتمتة نشر وتكوين أنظمة ويندوز ولينكس. تقدم هذه المقالة دليلاً شاملاً لاستخدام PowerShell DSC لإدارة التكوين، بما في ذلك أفضل الممارسات، اللوائح الحكومية، والمراجع المفيدة.

______

## البدء مع PowerShell Desired State Configuration

### ما هو PowerShell Desired State Configuration؟

PowerShell Desired State Configuration (**DSC**) هو **لغة وصفية** مدمجة في PowerShell تمكن المسؤولين من أتمتة تكوين الأنظمة، التطبيقات، والخدمات. يوفر طريقة **موحدة ومتسقة** لإدارة التكوينات وضمان بقاء الأنظمة في الحالة المرغوبة.

### تثبيت PowerShell DSC

للبدء مع PowerShell DSC، ستحتاج إلى تثبيت **إطار إدارة ويندوز (WMF)**. WMF هو حزمة تشمل PowerShell، DSC، وأدوات إدارة أساسية أخرى. يمكنك تنزيل أحدث إصدار من WMF من [مركز تنزيل مايكروسوفت](https://www.microsoft.com/en-us/download/details.aspx?id=54616).

______

## إنشاء وتطبيق تكوينات DSC

### كتابة تكوينات DSC

تكوين DSC هو **سكريبت PowerShell** يصف الحالة المرغوبة للنظام. يتكون من مورد واحد أو أكثر من **موارد DSC** التي تحدد الإعدادات والخصائص المطلوبة لمكونات النظام. إليك مثال على تكوين DSC بسيط يقوم بتثبيت دور خادم الويب (IIS) على خادم ويندوز:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### تطبيق تكوينات DSC
بعد كتابة تكوين DSC، يمكنك تطبيقه على النظام المستهدف باستخدام الأمر **Start-DscConfiguration**. أولاً، قم بترجمة سكريبت التكوين عن طريق تشغيله في PowerShell:

```powershell
InstallIIS
```

سيولد هذا ملف **MOF** (Managed Object Format) يحتوي على التكوين المترجم. بعد ذلك، طبق التكوين على النظام المستهدف باستخدام الأمر التالي:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## أفضل الممارسات لاستخدام PowerShell DSC

### تقسيم تكويناتك إلى وحدات

أنشئ تكوينات **وحدوية وقابلة لإعادة الاستخدام** بفصل مكونات البنية التحتية المختلفة إلى **موارد DSC فردية**. تتيح لك هذه الطريقة سهولة **الصيانة والتوسع** في تكويناتك مع نمو بيئتك.

### استخدام التحكم بالمصدر

احفظ دائمًا تكوينات DSC والموارد المخصصة في نظام **التحكم بالمصدر** مثل Git. تتيح لك هذه الممارسة تتبع التغييرات، التعاون مع فريقك، والرجوع بسهولة إلى الإصدارات السابقة من تكويناتك عند الحاجة.

### اختبار تكويناتك

**الاختبار** هو جانب حاسم في إدارة التكوين. قبل نشر تكوين DSC، اختبره في بيئة **غير إنتاجية** للتأكد من عمله كما هو متوقع وعدم إحداث أي نتائج غير مقصودة. يمكنك أيضًا استخدام أدوات مثل [Pester](https://github.com/pester/Pester) للاختبار الآلي لتكوينات DSC الخاصة بك.

______

## اللوائح الحكومية والإرشادات

### إرشادات NIST

يوفر المعهد الوطني للمعايير والتقنية (NIST) إرشادات لإدارة تكوين النظام. على وجه الخصوص، يحتوي منشور [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) على قسم (CM-2) حول التكوينات الأساسية، وهو ذو صلة باستخدام DSC. تؤكد الإرشادات على أهمية الحفاظ على مراقبة وضبط التغييرات في تكوينات النظام. يمكن لـ PowerShell DSC مساعدة المؤسسات على الامتثال لهذه الإرشادات من خلال توفير طريقة متسقة وآلية لإدارة تكوينات النظام.

### قانون إدارة أمن المعلومات الفيدرالي (FISMA)

يتطلب قانون إدارة أمن المعلومات الفيدرالي [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) من الوكالات الفيدرالية تنفيذ إطار شامل لضمان فعالية ضوابط أمن المعلومات الخاصة بها. إدارة التكوين هي مكون رئيسي للامتثال لـ FISMA، ويمكن لـ PowerShell DSC أن يلعب دورًا أساسيًا في مساعدة المؤسسات على تلبية هذه المتطلبات.
______

## الخاتمة

PowerShell Desired State Configuration (DSC) هو أداة قوية ومرنة لأتمتة نشر وإدارة تكوينات النظام. باتباع أفضل الممارسات والالتزام باللوائح الحكومية، يمكنك ضمان بقاء أنظمة مؤسستك في الحالة المرغوبة مع الحفاظ على الامتثال. لا تنس الاستفادة من الموارد المقدمة في هذه المقالة لتعزيز فهمك لـ PowerShell DSC وتحسين عمليات إدارة التكوين الخاصة بك.
______

## المراجع

- [التوثيق الرسمي لـ PowerShell Desired State Configuration (DSC)](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - ضوابط الأمان والخصوصية للأنظمة والمعلومات الفيدرالية](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [قانون إدارة أمن المعلومات الفيدرالي (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - إطار اختبار PowerShell](https://github.com/pester/Pester)
- [دليل المبتدئين لاستخدام التشفير لحماية البيانات](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [أفضل الممارسات لتثبيت تصحيحات الأمان على ويندوز](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)
