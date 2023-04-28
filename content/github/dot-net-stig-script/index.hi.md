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

.NET Framework STIG को चालू कर देगा  .NET STIG को लागू करना निश्चित रूप से लाइव नहीं है। कई व्यवस्थापकों के लिए एकल सिस्टम पर पूरी तरह से लागू होने में समय लग सकता है। यह स्क्रिप्ट के अनुसार वेबसीलेटर को लागू करता है और FIPS और अन्य नियंत्रणों को लागू करने के लिए फ़ाइल. कॉन्फ़िगर फ़ाइल को अनुप्राणित करता है।  ## सुचना:  यह स्क्रिप्ट 100% अनुपालन के लिए .NET स्टिग को कभी प्राप्त नहीं कर सकता है और कभी भी प्राप्त नहीं कर सकता है। अभी, जैसा कि है, यह लगभग 75% चेक को पूरा करने के लिए जमा है और सभी पिछले .NET संस्करण पर लागू चेक को पूरा करता है।  किसी को भी .NET ऐप या IIS साइट के लिए लिंकिंग इंटरेक्शन की आवश्यकता है।  ## खुलासा: - [एक्स] विंडोज 7, विंडोज सर्वर 2008 या नया - [X] प्रसारण पर चलने से पहले अपने वातावरण में परीक्षण।  ## आख्यान/सरजी लागू करें:  - [माइक्रोसॉफ्ट .नेट फ्रेमवर्क 4 वी1आर9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)  ##स्रोत:  - [एक XML डेटा से दूसरा मौजूदा XML फ़ाइल में जोड़ें](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/) - [Caspol.exe (संशोधित एक समान अनुबंध नीति)] (https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool) - [माइक्रोसॉफ्ट .NET फ्रेमवर्क दस्तावेज़ीकरण](https://docs.microsoft.com/en-us/dotnet/framework/) - [पॉवरशेल $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot) - [पवेशेल: स्क्रिप्ट की डायरेक्टरी से कमांड चलाएँ] (https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory) - [विशेष फ़ाइल से पॉवरशेल इंपोर्टनोड]  ## आवश्यक फ़ाइल डाउनलोड करें  आप [GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/) से आवश्यक फ़ाइलें डाउनलोड कर सकते हैं।  ## स्क्रिप्ट कैसे चलाएं  ** स्क्रिप्ट को इस तरह घोषित किया गया GitHub डाउनलोड से लॉन्च किया जा सकता है: **  ## स्क्रिप्ट कैसे चलाएं ### मैनुअल रिकॉर्ड करें: यदि कोई फ़ोल्डर से डाउनलोड किया गया है, तो स्क्रिप्ट को [GitHub Repository](https://github.com/simeonsecurity/.NET-STIG-Script) की सभी दस्तावेज़ निर्देशिकाओं में एक जार शेल से लॉन्च किया जाना चाहिए। ### स्थापित करें: स्वचालित रूप से डाउनलोड करने, सभी सहायक फ़ाइलों को अनज़िप करने और स्क्रिप्ट के नवीनतम संस्करण को चलाने के लिए इस वन-लाइनर का उपयोग करें।