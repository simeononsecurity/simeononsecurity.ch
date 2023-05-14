---
title: "Windows-Optimize-Debloat के साथ अपने Windows PC को ऑप्टिमाइज़ करें"
date: 2020-12-29
toc: true
draft: false
description: "विंडोज-ऑप्टिमाइज़-डीब्लोट के साथ अपने विंडोज ऑपरेटिंग सिस्टम के प्रदर्शन और गोपनीयता में सुधार करें, एक व्यापक स्क्रिप्ट जो ब्लोटवेयर को हटाने और सिस्टम सेटिंग्स को अनुकूलित करने में मदद करती है।"
tags: ["विंडोज-ऑप्टिमाइज़-डीब्लोट", "विंडोज ऑप्टिमाइज़ेशन", "विंडोज़ को डिब्लो करना", "विंडोज को तेज करें", "विंडोज प्रदर्शन का अनुकूलन करें", "विंडोज प्रदर्शन बूस्ट", "विंडोज सिस्टम अनुकूलन", "माइक्रोसॉफ्ट", "गोपनीयता", "ब्लोटवेयर हटाना", "विंडोज 10", "विंडोज़ 11", "विंडोज़ रक्षक", "विंडोज़ अपडेट", "कॉर्टोना", "समूह नीति ऑब्जेक्ट", "टेलीमेटरी", "विंडोज स्टोर", "विंडोज 10 प्रोफेशनल", "विंडोज 10 होम"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*उन लोगों के लिए जो अपने विंडोज 10 और 11 इंस्टाल को कम करना चाहते हैं।*

**ध्यान दें:** यह स्क्रिप्ट बिना किसी समस्या के अधिकांश, यदि सभी नहीं, सिस्टम के लिए काम करनी चाहिए। जबकि[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) यदि आप यह नहीं समझते कि यह क्या करता है तो इस स्क्रिप्ट को न चलाएँ।

## परिचय:
विंडोज 10 और 11 बॉक्स से बाहर आक्रामक और असुरक्षित ऑपरेटिंग सिस्टम हैं।
संगठन पसंद करते हैं[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) और अन्य ने विंडोज 10 ऑपरेटिंग सिस्टम को अनुकूलित और डीब्लोट करने के लिए कॉन्फ़िगरेशन परिवर्तनों की सिफारिश की है। इन परिवर्तनों में टेलीमेट्री को ब्लॉक करना, लॉग हटाना और ब्लोटवेयर को हटाना आदि शामिल हैं। इस स्क्रिप्ट का उद्देश्य उन संगठनों द्वारा अनुशंसित कॉन्फ़िगरेशन को स्वचालित करना है।

## टिप्पणियाँ:
- यह स्क्रिप्ट मुख्य रूप से **निजी उपयोग** वातावरण में संचालन के लिए डिज़ाइन की गई है।
- इस स्क्रिप्ट को इस तरह से डिज़ाइन किया गया है कि अनुकूलन, कुछ अन्य स्क्रिप्ट के विपरीत, कोर विंडोज़ की कार्यक्षमता को नहीं तोड़ेगा।
 - विंडोज अपडेट, विंडोज डिफेंडर, विंडोज स्टोर और कॉर्टोना जैसी सुविधाओं को प्रतिबंधित कर दिया गया है, लेकिन अधिकांश अन्य विंडोज 10 गोपनीयता लिपियों की तरह यह निष्क्रिय स्थिति में नहीं हैं।
- यदि आप केवल व्यावसायिक परिवेशों के लिए लक्षित न्यूनतम स्क्रिप्ट चाहते हैं, तो कृपया इसे देखें[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## आवश्यकताएं:
- [एक्स] विंडोज 10/11 एंटरप्राइज, विंडोज 10 प्रोफेशनल या विंडोज 10 होम
  - विंडोज होम जीपीओ कॉन्फ़िगरेशन की अनुमति नहीं देता है।
    - स्क्रिप्ट अभी भी काम करेगी लेकिन सभी सेटिंग्स लागू नहीं होंगी I
  - विंडोज "एन" संस्करण का परीक्षण नहीं किया गया है।
  - चलाएँ[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) नवीनतम प्रमुख रिलीज़ को अपडेट और सत्यापित करने के लिए।

## Microsoft खाता या Xbox सेवाओं को ठीक करना:
ऐसा इसलिए है क्योंकि हम Microsoft खातों में साइन इन करना ब्लॉक कर देते हैं। Microsoft की टेलीमेट्री और आइडेंटिटी एसोसिएशन की आलोचना की जाती है।
हालाँकि, यदि आप अभी भी इन सेवाओं का उपयोग करना चाहते हैं, तो समाधान के लिए निम्न समस्या टिकट देखें:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## इस संग्रह द्वारा उपयोग की जाने वाली स्क्रिप्ट और टूल की सूची:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## अतिरिक्त कॉन्फ़िगरेशन पर विचार किया गया:
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

## स्क्रिप्ट कैसे चलाएं:
### स्वचालित स्थापना:
स्क्रिप्ट को इस तरह निकाले गए GitHub डाउनलोड से लॉन्च किया जा सकता है:
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

