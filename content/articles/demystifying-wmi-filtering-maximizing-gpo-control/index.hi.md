---
title: "WMI फ़िल्टरिंग को समझना"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "जानें कि WMI फ़िल्टरिंग से Group Policy Object (GPO) को सही कंप्यूटरों पर कैसे लागू करें। इसमें व्यावहारिक उदाहरण और बेहतर तरीके शामिल हैं।"
genre: ["Windows प्रबंधन", "Group Policy", "सिस्टम प्रशासन", "नेटवर्क प्रबंधन", "IT अवसंरचना", "नीति प्रबंधन", "IT शासन", "IT स्वचालन", "Active Directory", "सुरक्षा अनुपालन"]
tags: ["WMI फ़िल्टरिंग", "GPO", "Group Policy Objects", "WMI फ़िल्टर", "नीति लक्ष्यीकरण", "WMI क्वेरी", "Windows Management Instrumentation", "GPO नियंत्रण", "Group Policy Management Console", "WMI Query Language", "नीति लागू करना", "WQL", "नीति को सटीक बनाना", "नीति प्रबंधन", "सिस्टम संसाधन", "नीति लक्ष्यीकरण के उदाहरण", "सिस्टम प्रशासन", "नेटवर्क प्रबंधन", "IT अवसंरचना प्रबंधन", "IT स्वचालन", "Active Directory प्रबंधन", "सुरक्षा अनुपालन", "नीति नियंत्रण तकनीकें", "नीति प्रबंधन के बेहतर तरीके", "नीति फ़िल्टरिंग", "GPO नियंत्रण रणनीतियाँ", "GPO सुरक्षा", "WMI फ़िल्टरिंग के लाभ", "WMI फ़िल्टरिंग लागू करना", "WMI फ़िल्टरिंग के बेहतर तरीके"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "फ़िल्टर आइकन पर केंद्रित आवर्धक लेंस का चित्र, जो WMI फ़िल्टरिंग से GPO लक्ष्यीकरण दर्शाता है।"
coverCaption: "GPO नीतियों को सही लक्ष्यों पर लागू करने के लिए WMI फ़िल्टरिंग का उपयोग करें।"
---

## परिचय

Group Policy Object (GPO) में [**WMI फ़िल्टरिंग**](https://simeononsecurity.com/github/wmi-filters/) यह तय करती है कि WMI (Windows Management Instrumentation) क्वेरी के परिणामों के आधार पर नीति किन कंप्यूटरों या उपयोगकर्ताओं पर लागू होगी। इससे प्रशासक नीति का लक्ष्यीकरण सटीक कर सकते हैं और केवल इच्छित सिस्टम पर नीति लागू कर सकते हैं। इस लेख में हम WMI फ़िल्टरिंग, GPO में इसके काम करने के तरीके, [WMI फ़िल्टर](https://simeononsecurity.com/github/wmi-filters/) बनाने और उनके व्यावहारिक उदाहरणों को देखेंगे।

## [WMI फ़िल्टरिंग क्या है?](https://simeononsecurity.com/github/wmi-filters/)

[**WMI फ़िल्टरिंग**](https://simeononsecurity.com/github/wmi-filters/) का अर्थ WMI क्वेरी के परिणामों के आधार पर GPO पर फ़िल्टर लागू करना है। WMI, Windows ऑपरेटिंग सिस्टम में मौजूद प्रबंधन अवसंरचना है। इससे प्रशासक प्रबंधन डेटा प्राप्त कर सकते हैं और प्रोग्राम के माध्यम से सिस्टम संसाधनों के साथ काम कर सकते हैं। WMI फ़िल्टरिंग के ज़रिए GPO को क्वेरी के विशिष्ट मानदंडों के अनुसार गतिशील रूप से लक्षित किया जा सकता है।

WMI फ़िल्टर, WMI Query Language (WQL) में लिखे जाते हैं, जो SQL (Structured Query Language) का एक उपसमुच्चय है। फ़िल्टर आमतौर पर WMI namespace में उपलब्ध properties और values पर आधारित होते हैं। प्रशासक conditions, logical operators और namespaces को मिलाकर ऐसी WMI queries बना सकते हैं जो चुने हुए कंप्यूटरों या उपयोगकर्ताओं से मेल खाती हैं।

## GPO में WMI फ़िल्टरिंग कैसे काम करती है?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="फ्लोचार्ट में GPO से जुड़ा WMI फ़िल्टर WQL क्वेरी को True या False के रूप में जाँचता है और तय करता है कि नीति लक्ष्य कंप्यूटर पर लागू होगी या नहीं" >}}

Group Policy में **WMI फ़िल्टरिंग**, **WMI queries** के परिणामों के आधार पर GPO को चुनिंदा कंप्यूटरों पर लागू करती है। किसी **WMI फ़िल्टर** को GPO से जोड़ने पर फ़िल्टर का परिणाम **True** या **False** तय करता है कि GPO लागू होगी या नहीं।

WMI फ़िल्टर, **WMI Query Language (WQL)** का उपयोग करते हैं। WQL, SQL (Structured Query Language) का उपसमुच्चय है और **WMI namespace** में उपलब्ध **properties** तथा **values** के आधार पर जटिल queries बनाने देता है। इससे खास कंप्यूटरों या उपयोगकर्ताओं को लक्ष्य बनाया जा सकता है।

उदाहरण के लिए, कोई संगठन किसी GPO को केवल Windows 10 चलाने वाले कंप्यूटरों पर लागू करना चाहे। इसके लिए **Win32_OperatingSystem** class की **OperatingSystem** property जाँचने वाला WMI फ़िल्टर बनाया जा सकता है। क्वेरी इस तरह हो सकती है:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

यह क्वेरी जाँचती है कि ऑपरेटिंग सिस्टम का version "10." से शुरू होता है या नहीं, जो Windows 10 दर्शाता है। यदि परिणाम **True** है, तो GPO लक्ष्य कंप्यूटर पर लागू होगी। अन्यथा वह लागू नहीं होगी।

WMI फ़िल्टरिंग में **AND**, **OR** और **NOT** जैसे conditions तथा logical operators भी इस्तेमाल किए जा सकते हैं। कई properties और values को मिलाकर GPO लागू करने पर अधिक सूक्ष्म नियंत्रण मिलता है।

अलग-अलग **WMI namespaces** से WMI classes और properties के विशेष समूहों तक पहुँचा जा सकता है। इससे hardware configuration, installed software, network settings और अन्य मानदंडों के आधार पर GPO लक्ष्यीकरण संभव होता है।

फ़िल्टर और WMI queries बनाने के बारे में अधिक जानकारी के लिए Microsoft का [Group Policy के लिए WMI Filtering](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo) दस्तावेज़ देखें।

WMI फ़िल्टरिंग से प्रशासक बदलती परिस्थितियों के अनुसार कंप्यूटरों या उपयोगकर्ताओं पर GPO लागू कर सकते हैं और IT वातावरण का प्रबंधन बेहतर कर सकते हैं।

## GPO के लिए WMI फ़िल्टर बनाना

GPO के लिए WMI फ़िल्टर बनाने हेतु ये चरण अपनाएँ:

1. Domain से जुड़े Windows कंप्यूटर पर **Group Policy Management Console** (GPMC) खोलें।

2. Domain को expand करें और **WMI Filters** node पर जाएँ।

3. **WMI Filters** पर right-click करके **New** चुनें।

4. फ़िल्टर को उपयोगी नाम दें और **Query** field में WMI query लिखें। WQL syntax का उपयोग करें।

5. WMI फ़िल्टर सहेजने के लिए **OK** पर क्लिक करें।

फ़िल्टर बनने के बाद उसे एक या अधिक GPO से जोड़ा जा सकता है। WMI फ़िल्टर को GPO से जोड़ने के लिए:

1. इच्छित GPO पर right-click करके **Properties** चुनें।

2. GPO Properties विंडो में **WMI Filtering** tab खोलें।

3. सूची में से इच्छित WMI फ़िल्टर चुनें।

4. बदलाव सहेजने के लिए **OK** पर क्लिक करें।

GPO से WMI फ़िल्टर जोड़कर WMI query के परिणामों के अनुसार नीति लागू होने वाले सिस्टम चुने जा सकते हैं।

## एक GPO के लिए कितने WMI फ़िल्टर बनाए जा सकते हैं?

सटीक नीति लक्ष्यीकरण के लिए प्रशासक एक GPO में **कई WMI फ़िल्टर** बना सकते हैं। एक GPO से जुड़े फ़िल्टरों की कोई निश्चित अधिकतम सीमा नहीं है, इसलिए जटिल संयोजन संभव हैं।

फिर भी, फ़िल्टरों की संख्या का GPO processing time पर प्रभाव पड़ सकता है। फ़िल्टर बढ़ने पर GPO का मूल्यांकन और लागू करना भी अधिक समय ले सकता है। कुशल नीति लागू करने के लिए फ़िल्टरों की संख्या उचित रखें।

मान लें कि कोई संगठन ऐसी GPO लागू करना चाहता है जो केवल Windows 10 और एक खास software वाले कंप्यूटरों पर चले। वह दो WMI फ़िल्टर बना सकता है: एक **operating system** के लिए और दूसरा **software installation** के लिए। दोनों को मिलाने से इच्छित कंप्यूटर चुने जा सकते हैं।

विशिष्ट लक्ष्यीकरण की आवश्यकता और processing time के बीच संतुलन रखें। फ़िल्टरों की संख्या तय करने से पहले वातावरण की जटिलता, कंप्यूटरों या उपयोगकर्ताओं की संख्या और performance पर संभावित प्रभाव जाँचें।

कई WMI फ़िल्टरों की सुविधा GPO लक्ष्यीकरण को बेहतर बनाती है और IT वातावरण के कुशल processing तथा प्रबंधन में मदद करती है।

## GPO में WMI फ़िल्टरिंग के व्यावहारिक उदाहरण

GPO में WMI फ़िल्टरिंग से नीति को खास लक्ष्यों पर लागू किया जा सकता है। उदाहरण:

1. **विशिष्ट operating system चुनना**: GPO केवल **Windows 10** कंप्यूटरों पर लागू करने के लिए ऐसा फ़िल्टर बनाएँ जो operating system version जाँचे, जैसे `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`। इससे Windows 10 कंप्यूटर चुने जाते हैं।

2. **Desktop और laptop के लिए अलग नीतियाँ**: यदि दोनों प्रकार के उपकरणों के लिए अलग नीतियाँ हैं, तो दो WMI फ़िल्टर बनाएँ। एक hardware attributes के आधार पर desktop पहचान सकता है, जैसे `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, और दूसरा laptop पहचान सकता है। फिर हर प्रकार पर उपयुक्त नीतियाँ लागू करें।

3. **Disk space के आधार पर नीति लागू करना**: कम disk space वाले कंप्यूटर पर संसाधन-गहन नीतियाँ रोकने के लिए उपलब्ध जगह जाँचने वाला फ़िल्टर बनाएँ। उदाहरण के लिए `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` वाली query 10 GB से कम खाली स्थान वाले कंप्यूटरों को बाहर रखती है।

ये उदाहरण GPO में **WMI फ़िल्टरिंग** की लचीलापन दिखाते हैं। प्रशासक विशिष्ट मानदंडों के अनुसार नीतियों को लक्षित कर सकते हैं।

## निष्कर्ष

WMI फ़िल्टरिंग Group Policy Objects की एक उपयोगी सुविधा है। यह WMI query परिणामों के आधार पर प्रशासकों को नीतियाँ चुनिंदा कंप्यूटरों या उपयोगकर्ताओं पर लागू करने देती है। इससे नीति प्रबंधन अधिक कुशल और नियंत्रित होता है। इस लेख में हमने WMI फ़िल्टरिंग, GPO में इसके काम करने के तरीके, फ़िल्टर बनाने और व्यावहारिक उदाहरणों को देखा।

GPO प्रबंधन में WMI फ़िल्टरिंग शामिल करने से नीतियों का लक्ष्यीकरण अधिक सटीक होता है और वे केवल इच्छित सिस्टम पर लागू होती हैं।

## संदर्भ

- [Microsoft Docs: GPO के लिए WMI फ़िल्टर बनाएँ](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Group Policy Management Console](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
