---
title: "Enhancing Windows 10 Security with Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Learn how to enhance Windows 10 security with a PowerShell script that hardens Windows Defender Antivirus, implementing all the requirements of the Windows Defender Antivirus STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Windows 10 Security", "PowerShell Script", "Hardening", "Defender Hardening", "Security Automation", "Compliance", "Controlled Folder Access", "Intrusion Prevention System", "Application Control", "Attack Surface Reduction", "Exploit Protections", "Cloud-Delivered Protections", "Network Protections", "Windows Defender STIG Script", "Windows Defender STIG", "Windows Defender Antivirus STIG V2R1", "WDAC", "ASR"]
---
```
.\sos-windowsdefenderhardening.ps1
```

  ## يفعل ماذا هذا البرنامج؟ - تمكين الحماية عبر السحابة - تمكن من التحكم في الوصول إلى المجلد - حماية تمكن الشبكة - حظر التطفل - [تمكين سياسات التحكم في تطبيق Windows Defender] (https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control) - [تمكين قواعد تقليل سطح هجوم Windows Defender] (https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) - [تفعيل حماية استغلال Windows Defender) (https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection؟view=o365-worldwide#powershell) - جميع البيانات المشتركة في [Windows Defender Antivirus STIG V2R1] (https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)  ##: - [x] Windows 10 Enterprise (** المفضل **) أو Windows 10 Professional   - لا يسمح لـ Windows 10 Home بتكوينات GPO أو [ASR] (https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction). أن معظم هذه التكوينات ستظل سارية.   - لم يتم اختبار إصدارات Windows 10 "N".  ## تنزيل الملفات المطلوبة:  تنزيل الملفات المطلوبة من [مستودع جيثب] (https://github.com/simeononsecurity/Windows-Defender-STIG-Script)  ## كيفية تشغيل البرنامج:  ** يتم تنفيذ البرنامج من تنزيل GitHub المستخرج على النحو التالي: **