---
title: "تعزيز أمان Windows 10 باستخدام برنامج Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "تعرف على كيفية تحسين أمان Windows 10 باستخدام برنامج PowerShell النصي الذي يقوي برنامج Windows Defender Antivirus ، وينفذ جميع متطلبات برنامج الحماية من الفيروسات لـ Windows Defender STIG V2R1."
tags: ["ويندوز ديفندر", "نظام التشغيل Windows 10", "أمان Windows 10", "برنامج PowerShell النصي", "تصلب", "تصلب المدافع", "أتمتة الأمن", "امتثال", "التحكم في الوصول إلى المجلد", "نظام منع الاختراق", "التحكم في التطبيق", "هجوم الحد من السطح", "استغلال الحماية", "الحماية المقدمة عبر السحابة", "حماية الشبكة", "برنامج Windows Defender STIG", "برنامج Windows Defender STIG", "برنامج مكافحة الفيروسات لـ Windows Defender STIG V2R1", "WDAC", "ASR"]
---


## ماذا يفعل هذا البرنامج النصي؟
- تمكين الحماية المقدمة عبر السحابة
- تمكن من التحكم في الوصول إلى المجلد
- تمكن حماية الشبكة
- تمكن نظام منع التطفل
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- تنفذ جميع المتطلبات المدرجة في[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## متطلبات:
- [x] Windows 10 Enterprise (** المفضل **) أو Windows 10 Professional
  - لا يسمح Windows 10 Home بتكوينات GPO أو[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
على الرغم من أن معظم هذه التكوينات ستظل سارية.
  - لم يتم اختبار إصدارات Windows 10 "N".

## تنزيل الملفات المطلوبة:

قم بتنزيل الملفات المطلوبة من ملف[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## كيفية تشغيل البرنامج النصي:

** قد يتم تشغيل البرنامج النصي من تنزيل GitHub المستخرج على النحو التالي: **
```
.\sos-windowsdefenderhardening.ps1
```
