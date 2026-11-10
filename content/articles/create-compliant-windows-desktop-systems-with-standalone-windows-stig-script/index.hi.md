---
title: "Standalone-Windows-STIG-Script: अनुपालन वाला पीसी बनाएं"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "पैरामीटर और सत्यापन सहित, अनुपालन वाले Windows सिस्टम बनाने के लिए Standalone-Windows-STIG-Script का चरण-दर-चरण मार्गदर्शन।"
tags: ["STIG स्क्रिप्ट", "Windows सुरक्षा", "अनुपालन वाला Windows सिस्टम", "सिस्टम हार्डनिंग", "Windows STIG", "सुरक्षित Windows", "Windows अनुपालन", "मैन्युअल इंस्टॉल", "Windows अपडेट", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Windows Firewall", "जोखिम कम करने के उपाय", "Nessus PID", "VMware Horizon", "वैकल्पिक हार्डनिंग"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "गहरे नेवी रंग की पृष्ठभूमि पर चमकीले रंगों के साथ प्रगति पट्टियाँ और डेटा प्रवाह दिखाने वाले सुरक्षा-अनुपालन इंटरफ़ेस की कंप्यूटर स्क्रीन का चित्र।"
coverCaption: ""
---

Windows सिस्टम का उपयोग व्यवसायों, संगठनों और घरों में व्यापक रूप से होता है। साइबर हमलों की बढ़ती संख्या के साथ, यह सुनिश्चित करना ज़रूरी है कि ये सिस्टम सुरक्षित हों और उद्योग मानकों का पालन करें। Standalone-Windows-STIG-Script इस काम में मददगार है। यह लेख बताता है कि यह स्क्रिप्ट क्या है, कैसे काम करती है और सुरक्षित तथा अनुपालन वाला Windows सिस्टम बनाने के लिए इसका उपयोग कैसे करें।

## Standalone-Windows-STIG-Script क्या है?

**Standalone-Windows-STIG-Script** Simeononsecurity द्वारा विकसित स्क्रिप्ट है, जो Security Technical Implementation Guide (STIG) के अनुसार Windows सिस्टम को सुरक्षित बनाने की प्रक्रिया को स्वचालित करती है। यह ओपन सोर्स है और **GitHub** पर उपलब्ध है।

## यह कैसे काम करती है?

Standalone-Windows-STIG-Script Windows सिस्टम को सुरक्षित करने के लिए STIG में दिए गए दिशानिर्देश लागू करती है। इसे Windows सिस्टम पर चलाने से STIG अनुपालन के लिए ज़रूरी बदलाव होते हैं। इसमें कई सुरक्षा उपाय शामिल हैं, जैसे:

- खाता नीतियाँ
- ऑडिट नीतियाँ
- सुरक्षा विकल्प
- फ़ायरवॉल सेटिंग्स
- सेवा सेटिंग्स

## Standalone-Windows-STIG-Script का उपयोग करने के लाभ:

- **स्वचालन**: स्क्रिप्ट Windows सिस्टम सुरक्षित करने की प्रक्रिया को स्वचालित करती है, जिससे समय बचता है और मानवीय त्रुटि की संभावना घटती है।

- **अनुपालन**: स्क्रिप्ट STIG दिशानिर्देश लागू करती है और Windows सिस्टम को उद्योग मानकों के अनुरूप बनाने में मदद करती है।

- **निश्चिंतता**: Standalone-Windows-STIG-Script का उपयोग करके आप भरोसा रख सकते हैं कि आपका Windows सिस्टम सुरक्षित है और उद्योग मानकों का पालन करता है।

_________________________________________________________________________________________________________________________

## Standalone-Windows-STIG-Script का उपयोग कैसे करें:

1. Standalone-Windows-STIG-Script का उपयोग करना अपेक्षाकृत आसान है। इसके चरण ये हैं:

2. **स्क्रिप्ट डाउनलोड करें**: यह GitHub पर https://github.com/simeononsecurity/Standalone-Windows-STIG-Script पर उपलब्ध है। इसे डाउनलोड करके अपने Windows सिस्टम पर सहेजें।

3. **ऊँचे अधिकारों वाला कमांड प्रॉम्प्ट खोलें**: Windows Start बटन पर दायाँ-क्लिक करें और "Windows PowerShell (Admin)" चुनें।

4. **स्क्रिप्ट चलाएँ**: जहाँ स्क्रिप्ट सहेजी है वहाँ जाएँ और यह कमांड दर्ज करके चलाएँ:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. बदलावों की समीक्षा करें: स्क्रिप्ट पूरी होने के बाद सिस्टम में हुए बदलाव देखें और सुनिश्चित करें कि सब कुछ सही ढंग से कॉन्फ़िगर हुआ है।

## निष्कर्ष:

Standalone-Windows-STIG-Script एक उपयोगी टूल है, जो आपके Windows सिस्टम को सुरक्षित करने और उद्योग मानकों के अनुरूप बनाने में मदद करता है। यह सुरक्षा प्रक्रिया को स्वचालित करता है और STIG दिशानिर्देश लागू करता है। सुरक्षित और अनुपालन वाला Windows सिस्टम बनाने के लिए Standalone-Windows-STIG-Script पर विचार करें।
