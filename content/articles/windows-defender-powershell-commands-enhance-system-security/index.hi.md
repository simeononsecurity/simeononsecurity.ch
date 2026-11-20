---
title: "सिस्टम सुरक्षा के लिए Windows Defender PowerShell कमांड"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Windows Defender PowerShell कमांड जानें और कमांड-लाइन नियंत्रण से अपने सिस्टम की सुरक्षा बढ़ाएँ।"
genre: ["Windows Defender", "PowerShell कमांड", "सिस्टम सुरक्षा", "कमांड-लाइन नियंत्रण", "एंटीवायरस", "Windows ऑपरेटिंग सिस्टम", "मैलवेयर सुरक्षा", "उन्नत सुरक्षा सेटिंग", "सुरक्षा संचालन स्वचालन", "Windows PowerShell"]
tags: ["तकनीक", "साइबर सुरक्षा", "ऑपरेटिंग सिस्टम", "Windows", "कमांड-लाइन टूल", "सिस्टम सुरक्षा", "PowerShell", "एंटीवायरस", "मैलवेयर सुरक्षा", "स्क्रिप्टिंग"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "कई साइबर खतरों से कंप्यूटर सिस्टम की रक्षा करती ढाल का एनिमेटेड चित्र।"
coverCaption: "Windows Defender PowerShell कमांड से अपने सिस्टम की सुरक्षा बढ़ाएँ।"
---

## परिचय

Microsoft द्वारा विकसित Windows Defender, Windows ऑपरेटिंग सिस्टम के लिए **एकीकृत एंटीवायरस और सुरक्षा समाधान** है। इसका इंटरफ़ेस सुरक्षा सेटिंग प्रबंधित करना आसान बनाता है। कमांड लाइन से नियंत्रण पसंद करने वाले उन्नत उपयोगकर्ता PowerShell कमांड का उपयोग कर सकते हैं। यह लेख **Windows Defender PowerShell कमांड** और Windows वातावरण की सुरक्षा व नियंत्रण बेहतर करने में उनके उपयोग की जानकारी देता है।

## Windows Defender PowerShell कमांड की क्षमता

ये कमांड कमांड-लाइन इंटरफ़ेस से **उन्नत सुरक्षा संचालन** चलाने देते हैं। इनमें मैलवेयर स्कैन करने से लेकर उन्नत सुरक्षा सेटिंग कॉन्फ़िगर करने तक के काम शामिल हैं। PowerShell से आप सुरक्षा संचालन स्वचालित कर सकते हैं, कस्टम स्क्रिप्ट बना सकते हैं और Windows Defender को मौजूदा कार्यप्रवाह में जोड़ सकते हैं।

## Windows Defender PowerShell शुरू करना

इन कमांड तक पहुँचने के लिए **व्यवस्थापक अधिकारों वाला PowerShell सत्र** खोलें:

1. `Win + X` दबाएँ और मेनू से **Windows PowerShell (Admin)** (व्यवस्थापक के रूप में) चुनें।
2. संकेत मिलने पर ऐप को डिवाइस में बदलाव की अनुमति देने के लिए **Yes** (हाँ) चुनें।

PowerShell सत्र खुलने के बाद Windows Defender PowerShell कमांड चलाएँ।

## आम Windows Defender PowerShell कमांड

### 1. **Get-MpComputerStatus**: Windows Defender की स्थिति जाँचें

`Get-MpComputerStatus` सिस्टम में Windows Defender की मौजूदा स्थिति दिखाता है। इसमें एंटीवायरस इंजन संस्करण, आखिरी स्कैन का समय और रीयल-टाइम सुरक्षा की स्थिति शामिल है। इसे चलाकर Windows Defender की स्थिति जल्दी जाँचें।

व्यवस्थापक अधिकार वाले PowerShell सत्र में यह कमांड चलाएँ:

```powershell
Get-MpComputerStatus
```

यह कमांड ऐसी जानकारी दिखाता है:

- **AntivirusEngineVersion**: Windows Defender द्वारा उपयोग किए जाने वाले **एंटीवायरस इंजन का संस्करण**।
- **LastFullScanTime**: आखिरी **पूर्ण स्कैन** की तारीख और समय।
- **LastQuickScanTime**: आखिरी त्वरित स्कैन की तारीख और समय।
- **RealTimeProtectionEnabled**: रीयल-टाइम सुरक्षा चालू है या बंद, यह बताता है।

`Get-MpComputerStatus` से नियमित निगरानी करने पर संभावित खतरों के विरुद्ध सिस्टम की सुरक्षा स्थिति पता रहती है।

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

`Update-MpSignature` Windows Defender के एंटीवायरस सिग्नेचर को मैन्युअल रूप से अपडेट करता है। सिग्नेचर में ज्ञात मैलवेयर की अहम जानकारी होती है, जिससे Windows Defender खतरों का पता लगाकर उन्हें रोकता है। इसे चलाने से सिस्टम को नए सिग्नेचर मिलते हैं और उभरते खतरों से सुरक्षा बेहतर होती है।

व्यवस्थापक अधिकार वाले PowerShell सत्र में यह कमांड चलाएँ:

```powershell
Update-MpSignature
```

यह अपडेट शुरू करता है। Windows Defender, Microsoft सर्वर से जुड़कर **नवीनतम एंटीवायरस सिग्नेचर** डाउनलोड करता है। अपडेट पूरा होने पर Windows Defender के पास ज्ञात मैलवेयर की नई जानकारी होती है, जिससे वह खतरों की पहचान और उन्हें हटाने में मदद करता है।

बदलते मैलवेयर और साइबर खतरों से सुरक्षा के लिए सिग्नेचर अपडेट रखें। `Update-MpSignature` नियमित रूप से चलाएँ ताकि Windows Defender आपके सिस्टम की प्रभावी रक्षा करे।

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

`Set-MpPreference` से **Windows Defender** की सेटिंग अपनी सुरक्षा आवश्यकताओं के अनुसार बदलें। इसमें **रीयल-टाइम सुरक्षा**, **क्लाउड-आधारित सुरक्षा** और **नेटवर्क निरीक्षण सिस्टम** की सेटिंग शामिल हैं।

उदाहरण के लिए, `Set-MpPreference` से रीयल-टाइम सुरक्षा चालू या बंद करें। यह सिस्टम में हानिकारक गतिविधियाँ देखती है और खतरों पर तुरंत प्रतिक्रिया देती है। इसे चालू करने के लिए:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

क्लाउड-आधारित सुरक्षा भी सेट की जा सकती है। यह खतरे पहचानने और नए खतरों पर तेज़ी से प्रतिक्रिया देने के लिए **क्लाउड संसाधनों** का उपयोग करती है। इसे चालू करने के लिए:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

`Set-MpPreference` नेटवर्क निरीक्षण सिस्टम की सेटिंग भी बदलता है। यह संदिग्ध गतिविधियों और संभावित खतरों के लिए नेटवर्क ट्रैफ़िक का विश्लेषण करता है। सेटिंग बदलने के लिए:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

`Set-MpPreference` से इन विकल्पों को अपनी सुरक्षा आवश्यकताओं के अनुरूप करें और **Windows Defender** से मैलवेयर व अन्य हानिकारक गतिविधियों से सिस्टम की रक्षा करें।

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

`Start-MpScan` सिस्टम पर मैलवेयर स्कैन शुरू करता है ताकि आप हानिकारक फ़ाइलों का पता लगाकर उन्हें हटा सकें। इससे **त्वरित**, **पूर्ण** और चुने हुए पथों के **कस्टम स्कैन** किए जा सकते हैं।

`Start-MpScan` से **त्वरित स्कैन** करने के लिए यह PowerShell कमांड चलाएँ:

```powershell
Start-MpScan -ScanType QuickScan
```

त्वरित स्कैन सिस्टम के उन अहम हिस्सों की जाँच करता है जहाँ अक्सर मैलवेयर मिलता है और संभावित खतरों का शीघ्र आकलन करता है।

सभी फ़ाइलों और निर्देशिकाओं की जाँच के लिए `Start-MpScan` से **पूर्ण स्कैन** चलाएँ:

```powershell
Start-MpScan -ScanType FullScan
```

पूर्ण स्कैन मैलवेयर की व्यापक जाँच करता है, लेकिन त्वरित स्कैन से अधिक समय ले सकता है।

पहले से तय प्रकारों के अलावा, `Start-MpScan` से चुने हुए पथ या फ़ाइल स्कैन करें। किसी खास डायरेक्टरी को स्कैन करने के लिए:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

यह कमांड चुनी गई डायरेक्टरी में कस्टम स्कैन शुरू करता है और सिस्टम के खास हिस्से में मैलवेयर ढूँढता है।

`Start-MpScan` से स्कैन तय समय पर चलाएँ, सुरक्षा प्रक्रियाएँ स्वचालित करें और मैलवेयर का नियमित पता लगाकर उसका समाधान करें।

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

`Get-MpThreatCatalog` ज्ञात खतरों और उनकी विशेषताओं की विस्तृत जानकारी देता है। इसकी सूची में खतरे की गंभीरता, संबंधित फ़ाइल नाम और जोखिम कम करने के सुझाए गए कदम शामिल हैं।

`Get-MpThreatCatalog` से किसी खास खतरे की जानकारी पाने के लिए:

1. व्यवस्थापक अधिकार वाला PowerShell सत्र खोलें।
2. यह कमांड चलाएँ:

```powershell
   Get-MpThreatCatalog
```

कमांड ज्ञात खतरों और उनके विवरण की सूची दिखाता है।

`Get-MpThreatCatalog` के आउटपुट में ऐसी अहम जानकारी होती है:

- **ThreatID**: खतरे का विशिष्ट पहचानकर्ता।
- **Severity**: खतरे की गंभीरता, Low (कम) से Severe (गंभीर) तक।
- **Name**: खतरे का नाम या विवरण।
- **Path**: खतरे से जुड़ी फ़ाइल का पथ।
- **RecommendedAction**: खतरा कम करने के सुझाए गए कदम।

`Get-MpThreatCatalog` की जानकारी संभावित खतरों को समझने और उचित कार्रवाई चुनने में मदद करती है। किसी खास खतरे को अलग करना, हटाना या निगरानी में रखना हो, विस्तृत सूची सुरक्षा घटनाओं का प्रभावी जवाब देने में सहायक है।

`Get-MpThreatCatalog` का उपयोग और परिणाम समझने के लिए Microsoft के आधिकारिक दस्तावेज़ देखें।

सतर्क रहें और बदलते खतरों की जानकारी व सिस्टम की सुरक्षा बेहतर करने के लिए `Get-MpThreatCatalog` नियमित रूप से चलाएँ।

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

`Add-MpPreference` Windows Defender में अपवाद जोड़ता है और स्कैन तथा रीयल-टाइम सुरक्षा का व्यवहार तय करने देता है। अपवाद से आप उन फ़ाइलों, फ़ोल्डरों या प्रक्रियाओं को चुनते हैं जिन्हें सुरक्षा स्कैन या रीयल-टाइम सुरक्षा के दौरान अनदेखा किया जाएगा।

`Add-MpPreference` से अपवाद जोड़ने के लिए फ़ाइल, फ़ोल्डर या प्रक्रिया का पथ अथवा नाम दें। यह उदाहरण फ़ोल्डर को अपवाद बनाता है:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

इससे Windows Defender चुने गए फ़ोल्डर को स्कैन नहीं करता और अनावश्यक चेतावनियाँ तथा काम में रुकावट घटती हैं।

विश्वसनीय ऐप, विकास वातावरण या गलत पहचान कराने वाली खास फ़ाइलों को छोड़ने के लिए अपवाद उपयोगी हो सकते हैं। `Add-MpPreference` से Windows Defender को अपनी सुरक्षा आवश्यकताओं के अनुरूप करें।

`Add-MpPreference` के अपवाद विकल्पों से सिस्टम की रक्षा करें और गलत पहचान तथा अनावश्यक स्कैन रुकावट घटाएँ।

## 2026 Defender कमांड जाँच

Defender कमांड केवल तभी उन्नत अधिकार वाले सत्र से चलाएँ जब काम में ऐसे अधिकार आवश्यक हों। कोई पैरामीटर उपयोग करने से पहले लक्ष्य Windows संस्करण के लिए मॉड्यूल की मौजूदा मदद देखें। वर्तमान कॉन्फ़िगरेशन दर्ज करें, एक बार में एक सेटिंग बदलें, परिणाम की पुष्टि करें और वापसी कमांड लिखें।

उपयोगी जाँच में सुरक्षा स्थिति, सिग्नेचर की आयु, अपवाद, प्राथमिकताएँ, स्कैन इतिहास और हाल की पहचान शामिल हैं। अपवाद सीमित रखें और उनके जिम्मेदार व्यक्ति व समाप्ति तारीख दर्ज करें। मौजूदा cmdlet और व्यवहार के लिए [Microsoft Defender PowerShell मॉड्यूल के दस्तावेज़](https://learn.microsoft.com/en-us/powershell/module/defender/) और [Microsoft Defender Antivirus दस्तावेज़](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) देखें।

## निष्कर्ष

Windows Defender PowerShell कमांड Windows सिस्टम की सुरक्षा प्रबंधित और बेहतर करने के लिए **उपयोगी टूल का समूह** देते हैं। उनसे *सुरक्षा संचालन स्वचालित*, *उन्नत सेटिंग कॉन्फ़िगर* और Windows Defender को कार्यप्रवाह में शामिल किया जा सकता है। सिस्टम प्रशासक हों या उन्नत उपयोगकर्ता, ये कमांड आपके सिस्टम की सुरक्षा स्थिति मजबूत करते हैं।

PowerShell कमांड चलाने से पहले सावधानी बरतें और उनका प्रभाव समझें। Windows Defender PowerShell कमांड के अपने ज्ञान से बदलते खतरों के विरुद्ध सिस्टम की सक्रिय रक्षा करें।

## संदर्भ

1. Microsoft Docs - [Windows PowerShell में Windows Defender Cmdlet](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Windows PowerShell का परिचय](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
