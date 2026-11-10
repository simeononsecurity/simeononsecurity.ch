---
title: "PowerShell से केवल-पठन Active Directory सूची तैयार करें"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "सीमित PowerShell क्वेरी से Active Directory की संगठनात्मक इकाइयों, उपयोगकर्ताओं और कंप्यूटरों की सूची बनाएँ। निर्देशिका ऑब्जेक्ट बदले बिना जाँच योग्य CSV फ़ाइलें निर्यात करें।"
genre: ["Active Directory", "PowerShell", "सिस्टम प्रशासन"]
tags: ["Active Directory सूची", "PowerShell AD सूची", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "केवल-पठन AD", "AD उपयोगकर्ता निर्यात", "AD कंप्यूटर निर्यात", "AD OU निर्यात", "Export-Csv", "RSAT", "निर्देशिका लेखा-परीक्षा", "AD रिपोर्ट", "OU सूची", "Windows Server", "PowerShell स्क्रिप्ट", "AD मॉड्यूल", "निर्देशिका स्वच्छता"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Active Directory वृक्ष से उपयोगकर्ता, कंप्यूटर और संगठनात्मक इकाई के अभिलेख तीन जाँच फ़ाइलों में जाते हुए।"
coverCaption: "क्वेरी का दायरा सीमित करें, फिर जाँच के लिए आवश्यक फ़ील्ड ही निर्यात करें।"
---
Active Directory की सफ़ाई मौजूदा ऑब्जेक्टों की भरोसेमंद सूची से शुरू होती है। यह **केवल-पठन सूची** चुने हुए दायरे में संगठनात्मक इकाइयों, उपयोगकर्ताओं और कंप्यूटरों का ब्यौरा जुटाती है। यह निर्देशिका ऑब्जेक्ट बदले बिना जाँच के लिए तीन CSV (अल्पविराम से अलग किए गए मान) फ़ाइलें निर्यात करती है। इन फ़ाइलों को फिर भी सुरक्षित रखें, क्योंकि नाम और उपकरणों का ब्यौरा आपके परिवेश के कुछ हिस्से उजागर करता है।

<!--more-->

## मुख्य बातें

- **दायरा चुनें:** पूरे डोमेन तक बढ़ने से पहले एक संगठनात्मक इकाई की क्वेरी करें।
- **पठन आदेश चलाएँ:** `Get-ADOrganizationalUnit`, `Get-ADUser` और `Get-ADComputer` ऑब्जेक्ट प्राप्त करते हैं।
- **फ़ील्ड चुनें:** काम के लिए आवश्यक गुण ही निर्यात करें।
- **नतीजे जाँचें:** रिपोर्ट पर भरोसा करने से पहले गिनती और कुछ नमूना पंक्तियाँ मिलाएँ।

## शुरू करने से पहले

आपको काम करता DNS और डोमेन नियंत्रक तक नेटवर्क पहुँच वाला Windows प्रशासन होस्ट, PowerShell का **ActiveDirectory** मॉड्यूल, चुने हुए ऑब्जेक्ट पढ़ने की स्वीकृति वाला खाता और CSV आउटपुट के लिए सुरक्षित फ़ोल्डर चाहिए। Windows क्लाइंट पर यह मॉड्यूल Remote Server Administration Tools (RSAT) के Active Directory औज़ारों के साथ मिलता है। [Active Directory मॉड्यूल मार्गदर्शिका](/articles/active-directory-module-powershell-installation-usage-guide/) स्थापना बताती है। Microsoft मॉड्यूल का [cmdlet संदर्भ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) और [RSAT स्थापना विकल्प](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools) देता है। यह मार्गदर्शिका Windows PowerShell वाक्य-विन्यास इस्तेमाल करती है और निर्देशिका ऑब्जेक्ट नहीं बदलती।

निर्देशिका की अनुमतियाँ लागू रहती हैं। Microsoft की [विशेषाधिकार प्राप्त खातों की मार्गदर्शिका](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory) बताती है कि पहुँच नियंत्रण सूचियाँ अक्सर प्रमाणित उपयोगकर्ताओं को सामान्य जानकारी पढ़ने देती हैं, लेकिन संवेदनशील फ़ील्ड और बदलाव सीमित करती हैं। पहले स्वीकृत खाते और परीक्षण OU का इस्तेमाल करें। सूची सफल बनाने के लिए Domain Admin अधिकार न बढ़ाएँ।

> **चेतावनी:** CSV फ़ाइलों में खाते और कंप्यूटर के नाम होते हैं। उन्हें स्वीकृत स्थान पर रखें, पहुँच सीमित करें और जाँच के बाद अतिरिक्त प्रतियाँ हटाएँ। कच्चा निर्यात प्रकाशित न करें और उसे सार्वजनिक Issue में न जोड़ें।

## खोज का आधार चुनें

**संगठनात्मक इकाई (OU)** निर्देशिका ऑब्जेक्टों को समूहित करती है। उसका **विशिष्ट नाम (DN)** निर्देशिका वृक्ष में उसका स्थान बताता है। `-SearchBase` पैरामीटर क्वेरी को चुने हुए DN तक सीमित करता है। जानबूझकर दायरा तय न करने पर व्यापक फ़िल्टर आपकी जाँच की ज़रूरत से कहीं अधिक ऑब्जेक्ट लौटा सकता है।

पहले मॉड्यूल लोड करें और मौजूदा डोमेन का DN देखें:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) और उससे मिलने वाली डोमेन जानकारी का दस्तावेज़ देता है। खोज का आधार तय करने से पहले जाँच वाली OU खोजें:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

नतीजे से सटीक DN की प्रतिलिपि लें। आगे के उदाहरणों में इस दस्तावेज़ी मान को अपनी OU के DN से बदलें:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` दस्तावेज़ का उदाहरण डोमेन है। उसका DN वास्तविक क्वेरी में न डालें। यदि जानबूझकर पूरे डोमेन की सूची चाहिए, तो `$SearchBase` में डोमेन का DN रखें और रिपोर्ट में बड़ा दायरा दर्ज करें। Microsoft का [Get-ADOrganizationalUnit संदर्भ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) `-Filter` और `-SearchBase` बताता है।

## OU, उपयोगकर्ता और कंप्यूटर की सूची बनाएँ

पहले ऑब्जेक्टों की गिनती करें। इससे गलत खोज-आधार या अप्रत्याशित खाली नतीजे का पता जल्दी चलता है:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` खोज-आधार के भीतर सभी मेल खाते ऑब्जेक्ट प्राप्त करता है। Microsoft [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) और [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) को प्राप्ति आदेशों के रूप में दस्तावेज़ करता है। शून्य गिनती सही हो सकती है, लेकिन सूची पूरी मानने से पहले DN, अनुमतियाँ और लक्ष्य डोमेन जाँचें।

अब कंसोल में कुछ पंक्तियाँ देखें। चुने हुए फ़ील्ड सहेजें ताकि पूर्वावलोकन और आगे का CSV निर्यात समान स्तंभ इस्तेमाल करें:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

कंप्यूटरों के लिए अतिरिक्त ऑपरेटिंग सिस्टम गुण तभी माँगें जब जाँच में उसकी ज़रूरत हो:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

`-Properties` पैरामीटर cmdlet के डिफ़ॉल्ट समूह से बाहर के गुण माँगता है। Microsoft इसे [कंप्यूटर cmdlet संदर्भ](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) में समझाता है। ऑपरेटिंग सिस्टम के नाम को निर्देशिका जानकारी मानें, मौजूदा स्थापित संस्करण का प्रमाण नहीं। कंप्यूटर ऑब्जेक्ट पुराना हो सकता है या उसका गुण अभी अद्यतन न हुआ हो।

## जाँच योग्य CSV फ़ाइलें निर्यात करें

पर्याप्त खाली जगह वाला स्वीकृत आउटपुट फ़ोल्डर चुनें। आगे के आदेश **स्थानीय CSV फ़ाइलें** लिखते हैं और निर्देशिका ऑब्जेक्ट नहीं बदलते। इन्हें उसी फ़ोल्डर में चलाएँ। `-NoClobber` मौजूदा फ़ाइल को अधिलेखित होने से रोकता है। हर बार नया फ़ोल्डर या फ़ाइल नाम रखें।

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Microsoft का [Export-Csv संदर्भ](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) `-NoTypeInformation`, `-Encoding` और `-NoClobber` समझाता है। हर CSV को पाठ संपादक या स्वीकृत स्प्रेडशीट में खोलें। शीर्षक पंक्ति, कुछ अभिलेख और अभिलेखों की संख्या पिछली गिनती से मिलाएँ। असफल आदेश या शून्य-बाइट फ़ाइल पूरी रिपोर्ट का प्रमाण नहीं है।

> **अपेक्षित नतीजा:** चुने हुए निर्देशिका दायरे के OU, उपयोगकर्ता और कंप्यूटर अभिलेखों वाली तीन CSV फ़ाइलें हैं। पंक्तियों की गिनती और नमूना मान चुने हुए दायरे से मेल खाते हैं।

## ऑब्जेक्ट बदले बिना जाँचें

सूची से ठोस सवालों के जवाब पाएँ: किसी कंप्यूटर की ज़िम्मेदारी किस OU की है? कौन से उपयोगकर्ता खाते निष्क्रिय हैं? किन उपकरण नामों के लिए मालिक तय करना है? निष्कर्ष अलग जाँच टिप्पणी में लिखें। `Enabled` मान से यह तय न करें कि खाता अब भी आवश्यक है या नहीं। केवल निर्यात देखकर किसी ऑब्जेक्ट को न हटाएँ और न निष्क्रिय करें।

नियमित रिपोर्ट में क्वेरी की तारीख, डोमेन, OU का DN, चुने हुए गुण, ऑपरेटर और CSV का स्थान लिखें। दो निर्यातों की तुलना करते समय पुष्टि करें कि दोनों में समान दायरा और फ़ील्ड थे। अन्यथा अंतर निर्देशिका के असली बदलाव के बजाय क्वेरी के कारण हो सकता है।

यह **सूची** है, विशेषाधिकार प्राप्त खातों की जाँच या लॉगिन गतिविधि रिपोर्ट नहीं। Microsoft बताता है कि Active Directory के गुण और अनुमतियाँ ऑब्जेक्ट तथा परिवेश के अनुसार बदलती हैं। ऑपरेटिंग सिस्टम गुण या प्रदर्शित नाम पर कार्रवाई से पहले सिस्टम मालिक से पुष्टि करें। व्यापक सुरक्षा नियंत्रणों के लिए [Active Directory सुरक्षा मार्गदर्शिका](/articles/active-directory-security-best-practices/) देखें।

## समस्या निवारण

- **मॉड्यूल आयात नहीं होता:** पुष्टि करें कि होस्ट पर RSAT के Active Directory औज़ार या Windows Server प्रशासन औज़ार स्थापित हैं। [मॉड्यूल सेटअप मार्गदर्शिका](/articles/active-directory-module-powershell-installation-usage-guide/) देखें।
- **क्वेरी कोई ऑब्जेक्ट नहीं लौटाती:** सटीक DN, मौजूदा डोमेन, OU की सामग्री और पठन अनुमतियाँ जाँचें। दायरा बढ़ाने से पहले किसी छोटी, ज्ञात OU को आज़माएँ।
- **कोई गुण खाली है:** जाँचें कि गुण मौजूद है और आपका खाता उसे पढ़ सकता है। अनुमान से छूटे फ़ील्ड न भरें।
- **निर्यात कहता है कि फ़ाइल पहले से है:** `-NoClobber` ने पुरानी रिपोर्ट सुरक्षित रखी। नया फ़ाइल नाम या फ़ोल्डर चुनकर फिर चलाएँ।
- **गिनती उम्मीद से अलग है:** जाँचें कि उपयोगकर्ता या कंप्यूटर किसी दूसरी OU में तो नहीं, दायरा बदला तो नहीं, या क्वेरी के दौरान निर्देशिका बदली तो नहीं।

## अगले कदम

कच्ची CSV फ़ाइलें तय समीक्षा अवधि तक सुरक्षित स्थान पर रखें। समीक्षक के लिए आवश्यक फ़ील्ड ही साझा करें। ज़िम्मेदार लोग निष्कर्षों की पुष्टि कर दें, तब अपनी सामान्य स्वीकृति और वापसी प्रक्रिया के अनुसार बदलाव योजना बनाएँ। स्वीकृत बदलावों के बाद उसी दायरे की यही सूची फिर चलाकर नतीजे की पुष्टि करें।