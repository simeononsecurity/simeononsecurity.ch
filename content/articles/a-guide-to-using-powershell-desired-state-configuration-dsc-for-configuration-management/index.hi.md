---
title: "PowerShell DSC: एक प्रारंभिक मार्गदर्शिका"
date: 2023-04-02
toc: true
draft: false
description: PowerShell Desired State Configuration (DSC) की शक्ति का अन्वेषण करें ताकि सिस्टम कॉन्फ़िगरेशन को स्वचालित और प्रबंधित किया जा सके, जिससे एक सुरक्षित और अनुपालन वातावरण सुनिश्चित हो।
tags:
- PowerShell
- DSC
- कॉन्फ़िगरेशन प्रबंधन
- स्वचालन
- Windows
- सिस्टम प्रशासन
- सर्वोत्तम प्रथाएँ
- अनुपालन
- सुरक्षा
- इन्फ्रास्ट्रक्चर
- DevOps
- सर्वर कॉन्फ़िगरेशन
- परीक्षण
- Git
- स्रोत नियंत्रण
- सरकारी नियम
- NIST
- CIS
- कॉन्फ़िगरेशन ड्रिफ्ट
- कस्टम संसाधन
cover: /img/cover/a-guide-to-using-powershell-desired-state-configuration-dsc-for-configuration-management.webp
coverAlt: एक चित्र जिसमें एक स्टाइलिश PowerShell टर्मिनल है, जिसके चारों ओर अमूर्त प्रतीक हैं, जो कॉन्फ़िगरेशन प्रबंधन और स्वचालन का प्रतिनिधित्व करते हैं, गहरे नौसेना रंग की पृष्ठभूमि के खिलाफ।
coverCaption: ''
lastmod: 2026-10-08
---

**कॉन्फ़िगरेशन प्रबंधन के लिए PowerShell Desired State Configuration (DSC) का उपयोग करने के लिए एक मार्गदर्शिका**

______

## परिचय

PowerShell Desired State Configuration (**DSC**) एक शक्तिशाली और **आवश्यक उपकरण** है जो आईटी प्रशासकों और DevOps पेशेवरों को Windows और Linux सिस्टम के तैनाती और कॉन्फ़िगरेशन को स्वचालित करने की अनुमति देता है। यह लेख PowerShell DSC का उपयोग कॉन्फ़िगरेशन प्रबंधन के लिए करने के लिए एक व्यापक मार्गदर्शिका प्रदान करता है, जिसमें सर्वोत्तम प्रथाएँ, सरकारी नियम और उपयोगी संदर्भ शामिल हैं।

______

## PowerShell Desired State Configuration के साथ शुरुआत

### PowerShell Desired State Configuration क्या है?

PowerShell Desired State Configuration (**DSC**) PowerShell में निर्मित एक **घोषणात्मक भाषा** है जो प्रशासकों को सिस्टम, अनुप्रयोगों और सेवाओं के कॉन्फ़िगरेशन को स्वचालित करने में सक्षम बनाती है। यह कॉन्फ़िगरेशन प्रबंधन के लिए एक **मानकीकृत और सुसंगत** तरीका प्रदान करता है और सुनिश्चित करता है कि सिस्टम इच्छित स्थिति में बने रहें।

### PowerShell DSC स्थापित करना

PowerShell DSC के साथ शुरुआत करने के लिए, आपको **Windows Management Framework (WMF)** स्थापित करना होगा। WMF एक पैकेज है जिसमें PowerShell, DSC और अन्य आवश्यक प्रबंधन उपकरण शामिल हैं। आप WMF का नवीनतम संस्करण [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616) से डाउनलोड कर सकते हैं।

______

## DSC कॉन्फ़िगरेशन बनाना और लागू करना

### DSC कॉन्फ़िगरेशन लिखना

DSC कॉन्फ़िगरेशन एक **PowerShell स्क्रिप्ट** है जो सिस्टम की इच्छित स्थिति का वर्णन करती है। यह एक या अधिक **DSC संसाधनों** से मिलकर बनती है जो सिस्टम के घटकों के लिए आवश्यक सेटिंग्स और गुणों को परिभाषित करते हैं। यहाँ एक सरल DSC कॉन्फ़िगरेशन का उदाहरण है जो Windows सर्वर पर वेब सर्वर (IIS) भूमिका स्थापित करता है:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### DSC कॉन्फ़िगरेशन लागू करना
एक बार जब आपने DSC कॉन्फ़िगरेशन लिख लिया, तो आप इसे लक्षित सिस्टम पर **Start-DscConfiguration** cmdlet का उपयोग करके लागू कर सकते हैं। पहले, PowerShell में स्क्रिप्ट चलाकर कॉन्फ़िगरेशन को संकलित करें:

```powershell
InstallIIS
```

यह एक **MOF** फ़ाइल (Managed Object Format) बनाएगा जिसमें संकलित कॉन्फ़िगरेशन होगा। इसके बाद, निम्नलिखित कमांड का उपयोग करके कॉन्फ़िगरेशन को लक्षित सिस्टम पर लागू करें:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## PowerShell DSC के लिए सर्वोत्तम प्रथाएँ

### अपनी कॉन्फ़िगरेशन को मॉड्यूलर बनाएं

अपने इन्फ्रास्ट्रक्चर के विभिन्न घटकों को **व्यक्तिगत DSC संसाधनों** में विभाजित करके **मॉड्यूलर और पुन: प्रयोज्य** कॉन्फ़िगरेशन बनाएं। यह दृष्टिकोण आपको अपने पर्यावरण के बढ़ने के साथ अपनी कॉन्फ़िगरेशन को आसानी से **रखरखाव और स्केल** करने की अनुमति देता है।

### स्रोत नियंत्रण का उपयोग करें

हमेशा अपनी DSC कॉन्फ़िगरेशन और कस्टम संसाधनों को Git जैसे **स्रोत नियंत्रण प्रणाली** में संग्रहित करें। यह अभ्यास आपको परिवर्तनों को ट्रैक करने, अपनी टीम के साथ सहयोग करने और आवश्यक होने पर अपनी कॉन्फ़िगरेशन के पिछले संस्करणों पर आसानी से वापस जाने में सक्षम बनाता है।

### अपनी कॉन्फ़िगरेशन का परीक्षण करें

**परीक्षण** कॉन्फ़िगरेशन प्रबंधन का एक महत्वपूर्ण पहलू है। DSC कॉन्फ़िगरेशन को तैनात करने से पहले, इसे एक **गैर-उत्पादन पर्यावरण** में परीक्षण करें ताकि यह सुनिश्चित हो सके कि यह अपेक्षित रूप से काम करता है और कोई अनपेक्षित परिणाम नहीं लाता। आप अपने DSC कॉन्फ़िगरेशन के स्वचालित परीक्षण के लिए [Pester](https://github.com/pester/Pester) जैसे उपकरण भी उपयोग कर सकते हैं।

______

## सरकारी नियम और दिशानिर्देश

### NIST दिशानिर्देश

National Institute of Standards and Technology (NIST) सिस्टम कॉन्फ़िगरेशन प्रबंधन के लिए दिशानिर्देश प्रदान करता है। विशेष रूप से, [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) प्रकाशन में Baseline Configurations पर एक अनुभाग (CM-2) है, जो DSC के उपयोग से संबंधित है। दिशानिर्देश सिस्टम कॉन्फ़िगरेशन में परिवर्तनों को बनाए रखने, निगरानी करने और नियंत्रित करने के महत्व पर जोर देते हैं। PowerShell DSC संगठनों को इन दिशानिर्देशों का पालन करने में मदद कर सकता है क्योंकि यह सिस्टम कॉन्फ़िगरेशन को प्रबंधित करने का एक सुसंगत और स्वचालित तरीका प्रदान करता है।

### Federal Information Security Management Act (FISMA)

Federal Information Security Management Act [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) संघीय एजेंसियों को उनके सूचना सुरक्षा नियंत्रणों की प्रभावशीलता सुनिश्चित करने के लिए एक व्यापक ढांचा लागू करने की आवश्यकता करता है। कॉन्फ़िगरेशन प्रबंधन FISMA अनुपालन का एक प्रमुख घटक है, और PowerShell DSC संगठनों को इन आवश्यकताओं को पूरा करने में महत्वपूर्ण भूमिका निभा सकता है।
______

## निष्कर्ष

PowerShell Desired State Configuration (DSC) सिस्टम कॉन्फ़िगरेशन की तैनाती और प्रबंधन को स्वचालित करने के लिए एक शक्तिशाली और लचीला उपकरण है। सर्वोत्तम प्रथाओं का पालन करके और सरकारी नियमों का पालन करते हुए, आप सुनिश्चित कर सकते हैं कि आपकी संगठन की प्रणालियाँ इच्छित स्थिति में बनी रहें और अनुपालन बनाए रखें। इस लेख में प्रदान किए गए संसाधनों का उपयोग करना न भूलें ताकि आप PowerShell DSC की समझ बढ़ा सकें और अपने कॉन्फ़िगरेशन प्रबंधन प्रक्रियाओं में सुधार कर सकें।
______

## संदर्भ

- [PowerShell Desired State Configuration (DSC) आधिकारिक दस्तावेज़](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - संघीय सूचना प्रणालियों और संगठनों के लिए सुरक्षा और गोपनीयता नियंत्रण](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell परीक्षण फ्रेमवर्क](https://github.com/pester/Pester)
- [डेटा सुरक्षा के लिए एन्क्रिप्शन का उपयोग करने के लिए शुरुआती मार्गदर्शिका](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Windows पर सुरक्षा पैच स्थापित करने के लिए सर्वोत्तम प्रथाएँ](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)
