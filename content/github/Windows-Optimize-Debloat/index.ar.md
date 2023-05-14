---
title: "قم بتحسين جهاز الكمبيوتر الذي يعمل بنظام Windows باستخدام Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "قم بتحسين أداء وخصوصية نظام التشغيل Windows الخاص بك باستخدام Windows-Optimize-Debloat ، وهو برنامج نصي شامل يساعد على إزالة bloatware وتحسين إعدادات النظام."
tags: ["Windows-Optimize-Debloat", "تحسين Windows", "النوافذ المنحلة", "تسريع النوافذ", "تحسين أداء Windows", "تعزيز أداء Windows", "تحسين نظام Windows", "مايكروسوفت", "خصوصية", "إزالة Bloatware", "نظام التشغيل Windows 10", "نظام التشغيل Windows 11", "ويندوز ديفندر", "تحديث ويندوز", "كورتونا", "كائنات نهج المجموعة", "القياس عن بعد", "متجر ويندوز", "نظام التشغيل Windows 10 Professional", "نظام التشغيل Windows 10 Home"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

* بالنسبة لأولئك الذين يسعون إلى تقليل عمليات تثبيت Windows 10 و 11. *

** ملاحظة: ** يجب أن يعمل هذا البرنامج النصي مع معظم ، إن لم يكن جميع ، الأنظمة التي لا تحتوي على مشكلة. بينما[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) لا تقم بتشغيل هذا البرنامج النصي إذا كنت لا تفهم ما يفعله.

## مقدمة:
يعد نظاما التشغيل Windows 10 و 11 نظام تشغيل غير آمن وغير آمن.
منظمات مثل[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) وأوصى آخرون بتغييرات التكوين لتحسين نظام التشغيل Windows 10 وإلغاء تعويمه. تتضمن هذه التغييرات حظر التتبع عن بعد وحذف السجلات وإزالة bloatware على سبيل المثال لا الحصر. يهدف هذا البرنامج النصي إلى أتمتة التكوينات الموصى بها من قبل تلك المؤسسات.

## ملحوظات:
- تم تصميم هذا البرنامج النصي للتشغيل في بيئات ** الاستخدام الشخصي ** بشكل أساسي.
- تم تصميم هذا البرنامج النصي بحيث لا تؤدي التحسينات ، على عكس بعض البرامج النصية الأخرى ، إلى تعطيل وظائف Windows الأساسية.
 - تم تقييد ميزات مثل Windows Update و Windows Defender و Windows Store و Cortona ، ولكنها ليست في حالة معطلة مثل معظم البرامج النصية الأخرى لخصوصية Windows 10.
- إذا كنت تبحث عن برنامج نصي مصغر يستهدف البيئات التجارية فقط ، فيرجى الاطلاع على هذا[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## متطلبات:
- [X] Windows 10/11 Enterprise أو Windows 10 Professional أو Windows 10 Home
  - لا يسمح Windows Home بتكوينات GPO.
    - سيستمر البرنامج النصي في العمل ولكن لن يتم تطبيق جميع الإعدادات.
  - لم يتم اختبار إصدارات Windows "N".
  - قم بتشغيل ملف[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) لتحديث أحدث إصدار رئيسي والتحقق منه.

## إصلاح حساب Microsoft أو خدمات Xbox:
هذا لأننا نحظر تسجيل الدخول إلى حسابات Microsoft. اقتران الهوية والقياس عن بُعد من Microsoft أمر مستاء.
ومع ذلك ، إذا كنت لا تزال ترغب في استخدام هذه الخدمات ، فراجع تذاكر الإصدار التالية للحصول على الحل:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## قائمة النصوص والأدوات التي تستخدمها هذه المجموعة:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## تم اعتبار التكوينات الإضافية من:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## كيفية تشغيل البرنامج النصي:
### التثبيت الآلي:
يمكن تشغيل البرنامج النصي من تنزيل GitHub المستخرج مثل هذا:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

