---
title: "डिफेंडर हार्डनिंग स्क्रिप्ट के साथ विंडोज 10 सुरक्षा बढ़ाना"
date: 2020-11-15
toc: true
draft: false
description: "Windows डिफेंडर एंटीवायरस STIG V2R1 की सभी आवश्यकताओं को लागू करते हुए, Windows डिफेंडर एंटीवायरस को कठोर बनाने वाली PowerShell स्क्रिप्ट के साथ Windows 10 सुरक्षा को बढ़ाना सीखें।"
tags: ["विंडोज़ रक्षक", "विंडोज 10", "विंडोज 10 सुरक्षा", "पॉवरशेल स्क्रिप्ट", "हार्डनिंग", "डिफेंडर हार्डनिंग", "सुरक्षा स्वचालन", "अनुपालन", "नियंत्रित फ़ोल्डर पहुँच", "अनाधिकृत प्रवेश निरोधक प्रणाली", "आवेदन नियंत्रण", "हमले की सतह में कमी", "शोषण संरक्षण", "क्लाउड-डिलीवरेड प्रोटेक्शन", "नेटवर्क सुरक्षा", "विंडोज डिफेंडर STIG स्क्रिप्ट", "विंडोज डिफेंडर एसटीआईजी", "विंडोज डिफेंडर एंटीवायरस STIG V2R1", "डब्ल्यूडीएसी", "अस्र"]
---


## यह स्क्रिप्ट क्या करती है?
- क्लाउड-वितरित सुरक्षा को सक्षम करता है
- नियंत्रित फोल्डर एक्सेस को सक्षम करता है
- नेटवर्क सुरक्षा सक्षम करता है
- घुसपैठ रोकथाम प्रणाली को सक्षम करता है
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- में सूचीबद्ध सभी आवश्यकताओं को लागू करता है[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## आवश्यकताएं:
- [x] विंडोज 10 एंटरप्राइज (**पसंदीदा**) या विंडोज 10 प्रोफेशनल
  - विंडोज 10 होम जीपीओ कॉन्फ़िगरेशन या के लिए अनुमति नहीं देता है[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
हालांकि इनमें से अधिकतर कॉन्फ़िगरेशन अभी भी लागू होंगे।
  - Windows 10 "N" संस्करण का परीक्षण नहीं किया गया है।

## आवश्यक फ़ाइलें डाउनलोड करें:

से आवश्यक फाइलों को डाउनलोड करें[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## स्क्रिप्ट कैसे चलाएं:

** इस तरह से निकाले गए GitHub डाउनलोड से स्क्रिप्ट को लॉन्च किया जा सकता है: **
```
.\sos-windowsdefenderhardening.ps1
```
