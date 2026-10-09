---
title: "الدليل الكامل لتقوية ويندوز باستخدام Windows Defender..."
date: 2020-12-16
toc: true
draft: false
description: تعلم كيفية استخدام Windows Defender Application Control WDAC لتقوية نظام تشغيل ويندوز الخاص بك باستخدام السكربتات والأدوات.
tags:
- تقوية Windows Defender Application Control WDAC
- PowerShell
- سكريبت PowerShell
- الأتمتة
- الامتثال
- فريق الدفاع الأزرق
- سكريبت Windows Defender STIG
- تقوية Windows Defender
- Windows Defender STIG
- Defender STIG
- حماية استغلال Windows Defender WDEP
- تقليل سطح الهجوم Windows Defender ASR
- Windows Server 2016 2019
- Windows Server Core
- مجموعة أدوات Microsoft WDAC
- تحديث سياسة CI
- قواعد الحظر الموصى بها من Microsoft
- قواعد حظر برامج التشغيل الموصى بها من Microsoft
- سياسات XML
- سياسات BIN
- سياسة المجموعة
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: رسم توضيحي لغرفة خوادم مستقبلية مع شاشات متوهجة تعرض هياكل ملفات XML و BIN المتعلقة بـ Windows Defender Application Control. الخلفية الداكنة تعزز الألوان الزاهية.
coverCaption: ''
lastmod: 2026-10-08
---

**تقوية ويندوز باستخدام Windows Defender Application Control WDAC**

## ملاحظات:
- يدعم Windows Server 2016/2019 أو أي إصدار قبل 1903 سياسة تراثية واحدة فقط في كل مرة.
- إصدار Windows Server Core يدعم [WDAC](https://simeononsecurity.com/til/2022-05-18/) لكن بعض المكونات التي تعتمد على AppLocker لن تعمل
- يرجى قراءة [القراءة الموصى بها](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) قبل التنفيذ أو حتى الاختبار.

## قائمة السكربتات والأدوات التي يستخدمها هذا التجميع:

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - تحديث سياسة CI](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## تم النظر في تكوينات إضافية من:

- [Microsoft - قواعد الحظر الموصى بها](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - قواعد حظر برامج التشغيل الموصى بها](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## شرح:

### XML مقابل BIN:

- ببساطة، السياسات **"XML"** مخصصة للتطبيق محليًا على الجهاز وملفات **"BIN"** مخصصة لفرضها عبر [سياسة المجموعة](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) أو [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune). بينما يمكنك استخدام سياسات XML أو BIN أو CIP في نشر محلي، من الأفضل عمومًا الالتزام بـ XML حيثما أمكن وخاصة أثناء التدقيق أو استكشاف الأخطاء وإصلاحها.

### وصف السياسات:

- **السياسات الافتراضية:**
  - تستخدم سياسات "الافتراضية" فقط الميزات الافتراضية المتاحة في WDAC-Toolkit.
- **السياسات الموصى بها:**
  - تستخدم سياسات "الموصى بها" الميزات الافتراضية بالإضافة إلى قواعد [الحظر](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) وقواعد حظر برامج التشغيل [الموصى بها](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) من Microsoft.
- **سياسات التدقيق:**
  - تسجل سياسات "التدقيق" فقط الاستثناءات من القواعد. هذا للاختبار في بيئتك، بحيث يمكنك تعديل السياسات بحرية لتناسب احتياجات بيئتك.
- **السياسات المفروضة:**
  - لا تسمح سياسات "المفروضة" بأي استثناءات للقواعد، سيتم حظر التطبيقات وبرامج التشغيل وملفات dll، إلخ إذا لم تمتثل.

### السياسات المتاحة:

- **XML:**
  - **تدقيق فقط:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **مفروضة:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **تدقيق فقط:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **مفروضة:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **تدقيق فقط:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **مفروضة:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

قم بتحديث السطر التالي في السكربت لاستخدام السياسة التي ترغب بها محليًا:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

بدلاً من ذلك، يمكنك استخدام [سياسة المجموعة](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) أو [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) لفرض سياسات WDAC.

## التدقيق:

يمكنك عرض سجلات أحداث WDAC في عارض الأحداث تحت:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## القراءة الموصى بها:

- [Argonsys - نشر سياسة التحكم في تطبيقات Windows 10](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - تدقيق سياسات Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - إنشاء سياسة WDAC لأجهزة العمل الثابتة باستخدام جهاز مرجعي](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - نشر سياسات Windows Defender Application Control باستخدام سياسة المجموعة](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - نشر سياسات Windows Defender Application Control باستخدام Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - نشر سياسات WDAC باستخدام سكربت](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - فرض سياسات Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - إرشادات إنشاء سياسات رفض WDAC](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - استخدام سياسات متعددة لـ Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## كيفية تشغيل السكربت:

### التثبيت اليدوي:

إذا تم التنزيل يدويًا، يجب تشغيل السكربت من PowerShell بصلاحيات المسؤول في الدليل الذي يحتوي على جميع الملفات من [مستودع GitHub](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
