---
title: "Automate .NET STIG Compliance with PowerShell Script"
date: 2020-08-20T22:14:22-05:00
draft: false
toc: true
description: "Easily implement the .NET Framework STIG with this PowerShell script, modifying the machine.config file and applying required registry changes for FIPS and other controls."
tags: [".NET STIG Script", ".NET Framework", "STIG Compliance", "Powershell Automation", "FIPS", "Windows Server", "Microsoft", "Administrative Powershell", "Code Access Security Policy Tool", "Machine.config", "DoD Compliance", "Cybersecurity", "Information Assurance", "GitHub Repository", "XML", "Windows 7", "IIS", "Configuration Management", "Security Hardening", "Automation"]
---
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
```
iwr -useb 'https://simeononsecurity.ch/scripts/sosdotnet.ps1'|iex
```

أتمتة .NET Framework STIG  من مفروشات أن تطبيق .NET STIG ليس بالأمر السهل. بالنسبة إلى حلول ، قد تنفيذ التنفيذ الكامل على تنفيذ واحد ساعات. يتوقع أن تكون جاهزًا للمجيء المتوقع.  ## ملحوظة:  لا يمكن لهذا البرنامج يعرض أبدًا على امتثال. صافي ستيج إلى 100 ٪. في الوقت الحالي ، كما هو الحال ، من المتوقع أن يكمل ما يقرب من 75 ٪ من الشيكات ويعود ويكمل عمليات الفحص المطبقة على جميع إصدارات .NET السابقة.  مطلوب تدخل يدوي لأي تطبيق .NET أو موقع IIS.  ##: - [X] Windows 7 أو Windows Server 2008 أو أحدث - [X] الاختبار في بيئتك قبل التشغيل على أنظمة الإنتاج.  ## تطبيق STIGS / SRGs:  - [Microsoft .Net Framework 4 V1R9] (https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)  ## مصادر:  - [إضافة بيانات XML إلى ملف XML آخر موجود] (http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/) - [Caspol.exe (Code Access Security Policy Tool)] (https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool) - [وثائق Microsoft .NET Framework] (https://docs.microsoft.com/en-us/dotnet/framework/) - [PowerShell $ PSScriptRoot] (https://riptutorial.com/powershell/example/27231/-psscriptroot) - [PowerShell: تشغيل الأمر من دليل البرنامج] (https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory) - [Powershell XML importnode من ملف مختلف] (https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)  ## تحميل الملفات المطلوب  يمكنك تنزيل الملفات المطلوبة من [GitHub Repository] (https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)  ## كيفية تشغيل البرنامج  ** يتم تشغيل البرنامج من تنزيل GitHub المستخرج مثل هذا: **  ## كيفية تشغيل البرنامج ### التثبيت اليدوي: في حالة التنزيل يدويًا ، تشغيل النص البرمجي في الدليل الذي يحتوي على جميع الملفات من [GitHub Repository] (https://github.com/simeononsecurity/.NET-STIG-Script) ### التثبيت الآلي: استخدم هذا الخط الواحد للتنزيل تلقائيًا وفك ضغط جميع الملفات الداعمة وأحدث إصدار من البرنامج.