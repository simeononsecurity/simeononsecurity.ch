---
title: "Windows Defender के साथ Windows को मजबूत करने के लिए पूर्ण मार्गदर्शिका..."
date: 2020-12-16
toc: true
draft: false
description: स्क्रिप्ट और टूल्स के साथ अपने Windows ऑपरेटिंग सिस्टम को मजबूत करने के लिए Windows Defender Application Control WDAC का उपयोग कैसे करें, जानें।
tags:
- Windows Defender Application Control WDAC हार्डनिंग
- PowerShell
- PowerShell स्क्रिप्ट
- स्वचालन
- अनुपालन
- ब्लू-टीम
- Windows Defender STIG स्क्रिप्ट
- Windows Defender हार्डनिंग
- Windows Defender STIG
- Defender STIG
- Windows Defender Exploit Protection WDEP
- Windows Defender Attack Surface Reduction ASR
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- CI पॉलिसी रीफ्रेश करें
- Microsoft अनुशंसित ब्लॉक नियम
- Microsoft अनुशंसित ड्राइवर ब्लॉक नियम
- XML नीतियां
- BIN नीतियां
- ग्रुप पॉलिसी
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: एक भविष्यवादी सर्वर रूम का चित्रण जिसमें चमकती स्क्रीन पर Windows Defender Application Control से संबंधित XML और BIN फ़ाइल संरचनाएं दिखाई दे रही हैं। गहरा पृष्ठभूमि जीवंत रंगों को बढ़ाता है।
coverCaption: ''
lastmod: 2026-10-08
---

**Windows Defender Application Control WDAC के साथ Windows को मजबूत करें**

## नोट्स:
- Windows Server 2016/2019 या संस्करण 1903 से पहले के किसी भी संस्करण में एक समय में केवल एक ही पुरानी नीति का समर्थन होता है।
- Windows Server Core संस्करण [WDAC](https://simeononsecurity.com/til/2022-05-18/) का समर्थन करता है लेकिन कुछ ऐसे घटक जो AppLocker पर निर्भर हैं, काम नहीं करेंगे
- कृपया लागू करने या परीक्षण करने से पहले [अनुशंसित पठन](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) पढ़ें।

## इस संग्रह में उपयोग की गई स्क्रिप्ट और टूल्स की सूची:

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - CI पॉलिसी रीफ्रेश करें](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## अतिरिक्त कॉन्फ़िगरेशन विचार किए गए:

- [Microsoft - अनुशंसित ब्लॉक नियम](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - अनुशंसित ड्राइवर ब्लॉक नियम](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## व्याख्या:

### XML बनाम BIN:

- सरल शब्दों में, **"XML"** नीतियां स्थानीय मशीन पर लागू करने के लिए होती हैं और **"BIN"** फ़ाइलें उन्हें [ग्रुप पॉलिसी](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) या [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) के साथ लागू करने के लिए होती हैं। जबकि आप स्थानीय परिनियोजन में XML, BIN, या CIP नीतियों का उपयोग कर सकते हैं, सामान्यतः जहां संभव हो XML का उपयोग करना चाहिए, खासकर ऑडिटिंग या समस्या निवारण के दौरान।

### नीति विवरण:

- **डिफ़ॉल्ट नीतियां:**
  - "डिफ़ॉल्ट" नीतियां केवल WDAC-Toolkit में उपलब्ध डिफ़ॉल्ट सुविधाओं का उपयोग करती हैं।
- **अनुशंसित नीतियां:**
  - "अनुशंसित" नीतियां डिफ़ॉल्ट सुविधाओं के साथ-साथ Microsoft के अनुशंसित [ब्लॉक्स](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) और [ड्राइवर ब्लॉक](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) नियमों का उपयोग करती हैं।
- **ऑडिट नीतियां:**
  - "ऑडिट" नीतियां केवल नियमों के अपवादों को लॉग करती हैं। यह आपके वातावरण में परीक्षण के लिए है ताकि आप अपनी आवश्यकताओं के अनुसार नीतियों को संशोधित कर सकें।
- **प्रवर्तन नीतियां:**
  - "प्रवर्तन" नीतियां नियमों के किसी भी अपवाद की अनुमति नहीं देतीं, अनुप्रयोग, ड्राइवर, dll आदि को ब्लॉक कर दिया जाएगा यदि वे अनुपालन नहीं करते।

### उपलब्ध नीतियां:

- **XML:**
  - **केवल ऑडिट:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **प्रवर्तन:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **केवल ऑडिट:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **प्रवर्तन:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **केवल ऑडिट:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **प्रवर्तन:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

स्क्रिप्ट में निम्न पंक्ति को स्थानीय रूप से अपनी इच्छित नीति का उपयोग करने के लिए अपडेट करें:

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

वैकल्पिक रूप से, आप WDAC नीतियों को लागू करने के लिए [ग्रुप पॉलिसी](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) या [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) का उपयोग कर सकते हैं।

## ऑडिटिंग:

आप इवेंट व्यूअर में WDAC इवेंट लॉग देख सकते हैं:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## अनुशंसित पठन:

- [Argonsys - Windows 10 एप्लिकेशन नियंत्रण नीति तैनात करना](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Windows Defender Application Control नीतियों का ऑडिट करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - संदर्भ कंप्यूटर का उपयोग करके फिक्स्ड-वर्कलोड डिवाइस के लिए WDAC नीति बनाएं](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - ग्रुप पॉलिसी का उपयोग करके Windows Defender Application Control नीतियां तैनात करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Microsoft Intune का उपयोग करके Windows Defender Application Control नीतियां तैनात करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - स्क्रिप्ट का उपयोग करके WDAC नीतियां तैनात करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Windows Defender Application Control नीतियों को लागू करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - WDAC डिनाय नीतियां बनाने पर मार्गदर्शन](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - कई Windows Defender Application Control नीतियों का उपयोग करें](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## स्क्रिप्ट कैसे चलाएं:

### मैनुअल इंस्टॉल:

यदि मैनुअल रूप से डाउनलोड किया गया है, तो स्क्रिप्ट को प्रशासनिक पॉवरशेल से लॉन्च करना होगा जिसमें सभी फ़ाइलें [GitHub रिपॉजिटरी](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip) से हों।

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
