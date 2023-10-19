---
title: "Windows-Optimize-Harden-Debloat Script के साथ अपने Windows सिस्टम को ऑप्टिमाइज़ और हार्डन करें"
date: 2020-12-29
toc: true
draft: false
description: "यह व्यापक मार्गदर्शिका बेहतर प्रदर्शन, सुरक्षा और गोपनीयता के लिए आपके विंडोज सिस्टम को अनुकूलित, सख्त और डीब्लोट करने के बारे में चरण-दर-चरण निर्देश प्रदान करती है।"
tags: ["विंडोज अनुकूलन", "विंडोज सख्त", "विंडोज डिब्लोटिंग", "विंडोज सुरक्षा", "विंडोज प्रदर्शन", "विंडोज़ गोपनीयता", "विंडोज अपडेट", "समूह नीति ऑब्जेक्ट", "एडोब एक्रोबेट रीडर", "फ़ायरफ़ॉक्स", "गूगल क्रोम", "इंटरनेट एक्सप्लोरर", "माइक्रोसॉफ्ट क्रोमियम एज", "डॉट नेट 4", "माइक्रोसॉफ्ट ऑफिस", "एक अभियान", "ओरेकल जावा जेआरई 8", "विंडोज फ़ायरवॉल", "विंडोज़ रक्षक", "ऐपलॉकर"]
---
 परिचय:

विंडोज 10 और विंडोज 11 बॉक्स से बाहर आक्रामक और असुरक्षित ऑपरेटिंग सिस्टम हैं।
संगठन पसंद करते हैं[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) लॉकडाउन, कठोर और ऑपरेटिंग सिस्टम को सुरक्षित करने के लिए कॉन्फ़िगरेशन परिवर्तनों की सिफारिश की है। इन परिवर्तनों में टेलीमेट्री, मैक्रोज़ को अवरुद्ध करने, ब्लोटवेयर को हटाने और सिस्टम पर कई डिजिटल और भौतिक हमलों को रोकने सहित शमन की एक विस्तृत श्रृंखला शामिल है। इस स्क्रिप्ट का उद्देश्य उन संगठनों द्वारा अनुशंसित कॉन्फ़िगरेशन को स्वचालित करना है।

## नोट्स, चेतावनियां और विचार:

**चेतावनी:**

यह स्क्रिप्ट अधिकांश के लिए काम करनी चाहिए, यदि सभी के लिए नहीं, तो बिना किसी समस्या के सिस्टम। जबकि[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- यह स्क्रिप्ट मुख्य रूप से **निजी उपयोग** वातावरण में संचालन के लिए डिज़ाइन की गई है। इसे ध्यान में रखते हुए, कुछ एंटरप्राइज़ कॉन्फ़िगरेशन सेटिंग्स लागू नहीं की जाती हैं। यह स्क्रिप्ट किसी सिस्टम को 100% अनुपालन में लाने के लिए डिज़ाइन नहीं की गई है। इसके बजाय इसे अधिकांश को पूरा करने के लिए एक कदम के पत्थर के रूप में इस्तेमाल किया जाना चाहिए, यदि सभी नहीं, तो कॉन्फ़िगरेशन परिवर्तन जो ब्रांडिंग और बैनर जैसे पिछले मुद्दों को छोड़ते हुए स्क्रिप्ट किए जा सकते हैं, जहां उन्हें कठोर व्यक्तिगत उपयोग के वातावरण में भी लागू नहीं किया जाना चाहिए।
- इस स्क्रिप्ट को इस तरह से डिज़ाइन किया गया है कि अनुकूलन, कुछ अन्य स्क्रिप्ट के विपरीत, कोर विंडोज़ की कार्यक्षमता को नहीं तोड़ेगा।
- विंडोज अपडेट, विंडोज डिफेंडर, विंडोज स्टोर, और कॉर्टोना जैसी सुविधाओं को प्रतिबंधित कर दिया गया है, लेकिन अधिकांश अन्य विंडोज 10 गोपनीयता लिपियों की तरह एक निष्क्रिय अवस्था में नहीं हैं।
- यदि आप केवल व्यावसायिक परिवेशों के लिए लक्षित न्यूनतम स्क्रिप्ट चाहते हैं, तो कृपया इसे देखें[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


** यदि आप यह नहीं समझते हैं कि यह क्या करता है तो इस स्क्रिप्ट को न चलाएं। स्क्रिप्ट को चलाने से पहले उसकी समीक्षा करना और उसका परीक्षण करना आपकी ज़िम्मेदारी है।**

**उदाहरण के लिए, यदि आप निवारक कदम उठाए बिना इसे चलाते हैं तो निम्नलिखित टूट जाएगा:**

- "प्रशासक" नाम के डिफ़ॉल्ट व्यवस्थापक खाते का उपयोग करना अक्षम है और प्रति DoD STIG का नाम बदल दिया गया है

  - बनाए गए डिफ़ॉल्ट खाते पर लागू नहीं होता है, लेकिन अक्सर एंटरप्राइज़, आईओटी और विंडोज सर्वर संस्करणों पर पाए जाने वाले डिफ़ॉल्ट व्यवस्थापक खाते का उपयोग करने पर लागू होता है

  - कंप्यूटर प्रबंधन के तहत एक नया खाता बनाएं और यदि आप चाहें तो इसे व्यवस्थापक के रूप में सेट करें। फिर स्क्रिप्ट चलाने से पहले इस पर काम करने के लिए पहली बार नए उपयोगकर्ता में साइन इन करने के बाद पिछले उपयोगकर्ता फ़ोल्डर की सामग्री को नए फ़ोल्डर में कॉपी करें।

- प्रत्येक DoD STIG के अनुसार Microsoft खाते का उपयोग करके साइन इन करना अक्षम है।

  - सुरक्षित और निजी रहने का प्रयास करते समय, किसी Microsoft खाते के माध्यम से अपने स्थानीय खाते में साइन इन करने की सलाह नहीं दी जाती है। यह इस रेपो द्वारा लागू किया गया है।

  - कंप्यूटर प्रबंधन के तहत एक नया खाता बनाएं और यदि आप चाहें तो इसे व्यवस्थापक के रूप में सेट करें। फिर स्क्रिप्ट चलाने से पहले इस पर काम करने के लिए पहली बार नए उपयोगकर्ता में साइन इन करने के बाद पिछले उपयोगकर्ता फ़ोल्डर की सामग्री को नए फ़ोल्डर में कॉपी करें।

- डीओडी एसटीआईजी के अनुसार खाता पिन अक्षम हैं

  - जब पासवर्ड के स्थान पर पूरी तरह से उपयोग किया जाता है तो पिन असुरक्षित होते हैं और कुछ घंटों या संभावित रूप से सेकंड या मिनट में आसानी से बायपास हो सकते हैं

  - स्क्रिप्ट चलाने के बाद खाते से पिन निकालें और/या पासवर्ड का उपयोग करके साइन इन करें।

- DoD STIG के कारण बिटलॉकर डिफॉल्ट्स बदल गए हैं और सख्त हो गए हैं।

  - बिटलॉकर कैसे कार्यान्वित किया जाता है, जब यह परिवर्तन होता है और यदि आपके पास पहले से बिटलॉकर सक्षम है तो यह बिटलॉकर कार्यान्वयन को तोड़ देगा।

  - बिटलॉकर को अक्षम करें, स्क्रिप्ट चलाएँ, फिर इस समस्या को हल करने के लिए बिटलॉकर को पुनः सक्षम करें।

## आवश्यकताएं:

- [x] विंडोज 10/11 एंटरप्राइज (**पसंदीदा**) या प्रोफेशनल
  - विंडोज 10/11 होम संस्करण जीपीओ कॉन्फ़िगरेशन का समर्थन नहीं करते हैं और उनका परीक्षण नहीं किया जाता है।
  - विंडो "एन" संस्करण का परीक्षण नहीं किया गया है।
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) अत्यधिक सुरक्षित विंडोज 10 डिवाइस के लिए
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - चलाएँ[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) नवीनतम प्रमुख रिलीज़ को अपडेट और सत्यापित करने के लिए।
- [x] इस स्क्रिप्ट को लागू करने से पहले बिटलॉकर को निलंबित या बंद कर दिया जाना चाहिए, इसे रीबूट करने के बाद फिर से सक्षम किया जा सकता है।
  - इस स्क्रिप्ट के अनुवर्ती रन बिटलॉकर को अक्षम किए बिना चलाए जा सकते हैं।
- [x] हार्डवेयर आवश्यकताएँ
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## अनुशंसित पठन सामग्री:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## जोड़, उल्लेखनीय परिवर्तन और बग फिक्स:

** यह स्क्रिप्ट आपके सिस्टम पर सेटिंग जोड़ती, हटाती और बदलती है। कृपया स्क्रिप्ट चलाने से पहले उसकी समीक्षा करें।**

### ब्राउज़र्स:

- गोपनीयता और सुरक्षा में सहायता के लिए ब्राउज़रों के पास अतिरिक्त एक्सटेंशन स्थापित होंगे।
  - देखना[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) अतिरिक्त जानकारी के लिए।
- ब्राउज़रों के लिए लागू किए गए DoD STIGs के कारण, विस्तार प्रबंधन और अन्य एंटरप्राइज़ सेटिंग्स सेट हैं। इन विकल्पों को कैसे देखें, इस बारे में निर्देशों के लिए, आपको नीचे दिए गए GPO निर्देशों को देखना होगा।

### पावरशेल मॉड्यूल:

- Windows को स्वचालित करने में सहायता के लिए PowerShell को अपडेट करता है[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) मॉड्यूल आपके सिस्टम में जोड़ा जाएगा।

### Microsoft खाता, स्टोर, या Xbox सेवाओं को ठीक करना:

ऐसा इसलिए है क्योंकि हम Microsoft खातों में साइन इन करना ब्लॉक कर देते हैं। Microsoft की टेलीमेट्री और आइडेंटिटी एसोसिएशन की आलोचना की जाती है।
हालाँकि, यदि आप अभी भी इन सेवाओं का उपयोग करना चाहते हैं, तो समाधान के लिए निम्न समस्या टिकट देखें:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### तथ्य के बाद स्थानीय समूह नीति में नीतियों का संपादन:

यदि आपको किसी सेटिंग को संशोधित करने या बदलने की आवश्यकता है, तो सबसे अधिक संभावना है कि वे GPO के माध्यम से कॉन्फ़िगर किए जा सकते हैं:

- इसमें से एडीएमएक्स नीति परिभाषाएं आयात करें[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) _C:\windows\PolicyDefinitions_ में उस सिस्टम पर जिसे आप संशोधित करने का प्रयास कर रहे हैं।

- जिस सिस्टम को आप संशोधित करने का प्रयास कर रहे हैं, उस पर `gpedit.msc` खोलें।

## इस संग्रह द्वारा उपयोग की जाने वाली स्क्रिप्ट और टूल की सूची:

### पहला पक्ष:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### तृतीय पक्ष:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## एसटीआईजीएस/एसआरजी लागू:

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

## अतिरिक्त कॉन्फ़िगरेशन पर विचार किया गया:

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

## स्क्रिप्ट कैसे चलाएं:
### जीयूआई - निर्देशित स्थापना:

नवीनतम रिलीज डाउनलोड करें[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)अपने इच्छित विकल्प चुनें और निष्पादित करें। <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Windows-Optimize-Harden-Debloat GUI आधारित निर्देशित इंस्टाल का उदाहरण"> ### स्वचालित स्थापना: स्वचालित रूप से डाउनलोड करने, सभी सहायक फ़ाइलों को अनज़िप करने और स्क्रिप्ट के नवीनतम संस्करण को चलाने के लिए इस एक-लाइनर का उपयोग करें।```powershell
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
