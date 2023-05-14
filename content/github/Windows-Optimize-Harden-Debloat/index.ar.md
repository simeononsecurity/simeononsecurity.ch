---
title: "قم بتحسين وتقوية نظام Windows الخاص بك باستخدام البرنامج النصي Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "يوفر هذا الدليل الشامل إرشادات خطوة بخطوة حول كيفية تحسين نظام Windows وتقويته وإزالته من أجل تحسين الأداء والأمان والخصوصية."
tags: ["تحسين Windows", "تصلب النوافذ", "الويندوز المنفلتة", "أمن Windows", "أداء Windows", "خصوصية Windows", "تحديثات Windows", "كائنات نهج المجموعة", "أدوبي أكروبات ريدر", "ثعلب النار", "جوجل كروم", "متصفح الانترنت", "مايكروسوفت كروم إيدج", "دوت نت 4", "مايكروسوفت أوفيس", "ون درايف", "أوراكل جافا JRE 8", "جدار حماية Windows", "ويندوز ديفندر", "التطبيق خزانة"]
---
 مقدمة:

يعتبر نظاما التشغيل Windows 10 و Windows 11 نظام تشغيل غير آمن وغير آمن.
منظمات مثل[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) تغييرات التكوين الموصى بها لإغلاق نظام التشغيل وتقويته وتأمينه. تغطي هذه التغييرات مجموعة واسعة من وسائل التخفيف بما في ذلك حظر القياس عن بعد ووحدات الماكرو وإزالة bloatware ومنع العديد من الهجمات الرقمية والمادية على النظام. يهدف هذا البرنامج النصي إلى أتمتة التكوينات الموصى بها من قبل تلك المؤسسات.

## ملاحظات وتحذيرات واعتبارات:

**تحذير:**

يجب أن يعمل هذا البرنامج النصي مع معظم ، إن لم يكن كل ، الأنظمة التي لا تحتوي على مشكلة. بينما[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- تم تصميم هذا البرنامج النصي للتشغيل في بيئات ** الاستخدام الشخصي ** بشكل أساسي. مع أخذ ذلك في الاعتبار ، لا يتم تنفيذ بعض إعدادات تكوين المؤسسة. هذا البرنامج النصي غير مصمم لتحقيق الامتثال بنسبة 100٪ في النظام. بدلاً من ذلك ، يجب استخدامه كنقطة انطلاق لإكمال معظم ، إن لم يكن كل ، تغييرات التكوين التي يمكن كتابتها أثناء تخطي المشكلات السابقة مثل العلامات التجارية واللافتات حيث لا ينبغي تنفيذها حتى في بيئة الاستخدام الشخصي القوية.
- تم تصميم هذا البرنامج النصي بحيث لا تؤدي التحسينات ، على عكس بعض البرامج النصية الأخرى ، إلى تعطيل وظائف Windows الأساسية.
- تم تقييد ميزات مثل Windows Update و Windows Defender و Windows Store و Cortona ، ولكنها ليست في حالة خلل وظيفي مثل معظم البرامج النصية الأخرى لخصوصية Windows 10.
- إذا كنت تبحث عن نص مصغر يستهدف البيئات التجارية فقط ، فيرجى الاطلاع على هذا[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


** لا تقم بتشغيل هذا البرنامج النصي إذا كنت لا تفهم ما يفعله. تقع على عاتقك مسؤولية مراجعة واختبار النص قبل تشغيله. **

** على سبيل المثال ، سوف ينكسر ما يلي إذا قمت بتشغيل هذا دون اتخاذ خطوات وقائية: **

- تم تعطيل استخدام حساب المسؤول الافتراضي المسمى "Administrator" وإعادة تسميته وفقًا لـ DoD STIG

  - لا ينطبق على الحساب الافتراضي الذي تم إنشاؤه ولكنه ينطبق على استخدام حساب المسؤول الافتراضي الموجود غالبًا في إصدارات Enterprise و IOT و Windows Server

  - قم بإنشاء حساب جديد تحت إدارة الكمبيوتر وقم بتعيينه كمسؤول إذا كنت ترغب في ذلك. ثم انسخ محتويات مجلد المستخدمين السابقين إلى المجلد الجديد بعد تسجيل الدخول إلى المستخدم الجديد لأول مرة للتغلب على هذا قبل تشغيل البرنامج النصي.

- تم تعطيل تسجيل الدخول باستخدام حساب Microsoft وفقًا لـ DoD STIG.

  - عند محاولة أن تكون آمنًا وخاصًا ، لا يُنصح بتسجيل الدخول إلى حسابك المحلي عبر حساب Microsoft. يتم فرض هذا من خلال هذا الريبو.

  - قم بإنشاء حساب جديد تحت إدارة الكمبيوتر وقم بتعيينه كمسؤول إذا كنت ترغب في ذلك. ثم انسخ محتويات مجلد المستخدمين السابقين إلى المجلد الجديد بعد تسجيل الدخول إلى المستخدم الجديد لأول مرة للتغلب على هذا قبل تشغيل البرنامج النصي.

- يتم تعطيل أرقام التعريف الشخصية للحساب وفقًا لـ DoD STIG

  - تكون أرقام التعريف الشخصية غير آمنة عند استخدامها فقط بدلاً من كلمة المرور ويمكن تجاوزها بسهولة في غضون ساعات أو ربما حتى ثوانٍ أو دقائق

  - قم بإزالة رقم التعريف الشخصي من الحساب و / أو تسجيل الدخول باستخدام كلمة المرور بعد تشغيل البرنامج النصي.

- يتم تغيير الإعدادات الافتراضية لـ Bitlocker وتقويتها بسبب DoD STIG.

  - نظرًا لكيفية تنفيذ bitlocker ، عند حدوث هذه التغييرات وإذا كان لديك بالفعل تمكين bitlocker ، فسيؤدي ذلك إلى تعطيل تنفيذ bitlocker.

  - قم بتعطيل bitlocker ، قم بتشغيل البرنامج النصي ، ثم أعد تمكين bitlocker لحل هذه المشكلة.

## متطلبات:

- [x] Windows 10/11 Enterprise (** المفضل **) أو Professional
  - لا تدعم إصدارات Windows 10/11 Home تكوينات GPO ولا يتم اختبارها.
  - لا يتم اختبار إصدارات النافذة "N".
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) لجهاز Windows 10 آمن للغاية
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - قم بتشغيل ملف[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) لتحديث أحدث إصدار رئيسي والتحقق منه.
- [x] يجب تعليق Bitlocker أو إيقاف تشغيله قبل تنفيذ هذا البرنامج النصي ، ويمكن تمكينه مرة أخرى بعد إعادة التشغيل.
  - يمكن تشغيل عمليات المتابعة لهذا البرنامج النصي دون تعطيل bitlocker.
- [x] متطلبات الأجهزة
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## مواد القراءة الموصى بها:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## الإضافات والتغييرات الملحوظة وإصلاح الأخطاء:

** يضيف هذا البرنامج النصي إعدادات نظامك ويزيلها ويغيرها. يرجى مراجعة البرنامج النصي قبل تشغيله. **

### المتصفحات:

- سيكون لدى المستعرضات امتدادات إضافية مثبتة للمساعدة في الخصوصية والأمان.
  - يرى[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) للحصول على معلومات إضافية.
- بسبب DoD STIGs المطبقة للمتصفحات ، تم تعيين إدارة الامتدادات وإعدادات المؤسسة الأخرى. للحصول على إرشادات حول كيفية رؤية هذه الخيارات ، ستحتاج إلى إلقاء نظرة على تعليمات GPO أدناه.

### وحدات باورشيل:

- للمساعدة في أتمتة تحديثات Windows على PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) ستتم إضافة وحدة إلى نظامك.

### إصلاح حساب Microsoft أو المتجر أو خدمات Xbox:

هذا لأننا نحظر تسجيل الدخول إلى حسابات Microsoft. اقتران الهوية والقياس عن بُعد من Microsoft أمر مستاء.
ومع ذلك ، إذا كنت لا تزال ترغب في استخدام هذه الخدمات ، فراجع تذاكر الإصدار التالية للحصول على الحل:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### تحرير السياسات في نهج المجموعة المحلية بعد الحقيقة:

إذا كنت بحاجة إلى تعديل أو تغيير أحد الإعدادات ، فمن المرجح أن تكون قابلة للتكوين عبر GPO:

- استيراد تعريفات سياسة ADMX من هذا[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) إلى _C: \ windows \ PolicyDefinitions_ على النظام الذي تحاول تعديله.

- افتح "gpedit.msc" على النظام الذي تحاول تعديله.

## قائمة النصوص والأدوات التي تستخدمها هذه المجموعة:

### الطرف الأول:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### طرف ثالث:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## تطبيق STIGS / SRGs:

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## تم اعتبار التكوينات الإضافية من:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## كيفية تشغيل البرنامج النصي:
### واجهة المستخدم الرسومية - التثبيت الموجه:

قم بتنزيل أحدث إصدار[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)اختر الخيارات التي تريدها واضغط على تنفيذ. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="مثال على التثبيت الإرشادي المستند إلى واجهة المستخدم الرسومية لـ Windows-Optimize-Harden-Debloat"> ### التثبيت التلقائي: استخدم هذا المكون من سطر واحد للتنزيل تلقائيًا وفك ضغط جميع الملفات الداعمة وتشغيل أحدث إصدار من البرنامج النصي.```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
