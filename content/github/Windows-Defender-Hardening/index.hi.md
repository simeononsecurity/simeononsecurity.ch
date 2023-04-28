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

  ## यह स्क्रिप्ट क्या करती है? - क्लाउड-वितरित सुरक्षा क्षमता है - नियंत्रक फ़ोल्डर ऐक्सेस कर सकता है - नेटवर्क सुरक्षा सक्षम करता है - घुसपैठ रोधी प्रणाली सक्षम है - [Windows डिफ़ेंडर एप नियंत्रण को समर्थ बनाता है](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control ) - [विनमय अटैक सरफेस रिडक्शन रूल्स को सक्षम कर सकता है] - [विनिमय प्लैटफ़ॉर्म की बचत सुरक्षा क्षमता करता है](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell ) - [Windows डिफेंडर सॉफ्टवेयर STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip) में सभी सूचीबद्ध आवश्यकताओं को लागू करता है  ## खुलासा: - [x] विंडोज 10 इंटरप्राइजेज (**पसंदीदा**) या विंडोज 10 प्रोफेशनल   - Windows 10 Home GPO या [ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) की अनुमति नहीं देता है। हालांकि इनमें से अधिकतर विवरण अभी भी लागू होंगे।   - Windows 10 "N" संस्करण का परीक्षण नहीं किया गया है।  ## आवश्यक फ़ाइलें डाउनलोड करें:  [GitHub रिपोजिटरी](https://github.com/simeononsecurity/Windows-Defender-STIG-Script) से आवश्यक फ़ाइलें डाउनलोड करें  ## स्क्रिप्ट कैसे चलाएं:  ** इस तरह से निकाले गए GitHub डाउनलोड से स्क्रिप्ट को शेयर किया जा सकता है: **