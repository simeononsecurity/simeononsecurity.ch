---
title: "PowerShell स्क्रिप्टिंग"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "PowerShell स्क्रिप्टिंग की बुनियादी बातें सीखें और कमांडलेट, लूप, फ़ंक्शन आदि पर इस शुरुआती चरण-दर-चरण मार्गदर्शिका से काम स्वचालित करें।"
genre: ["प्रौद्योगिकी", "प्रोग्रामिंग", "स्वचालन", "Windows", "स्क्रिप्टिंग", "आईटी", "प्रशासनिक कार्य", "कंप्यूटर प्रबंधन", "सॉफ़्टवेयर विकास", "कोडिंग"]
tags: ["PowerShell स्क्रिप्टिंग", "PowerShell स्वचालन", "Windows स्क्रिप्टिंग", "PowerShell कमांडलेट", "PowerShell मॉड्यूल", "PowerShell लूप", "PowerShell सशर्त कथन", "PowerShell फ़ंक्शन", "PowerShell की अच्छी प्रथाएँ", "PowerShell डिबगिंग", "PowerShell परीक्षण", "PowerShell चर", "PowerShell ISE", "PowerShell Remoting", "Microsoft तकनीकें", "आईटी स्वचालन", "कंप्यूटर प्रबंधन", "शुरुआती लोगों के लिए कोडिंग", "प्रशासनिक कार्य", "PowerShell स्क्रिप्ट के विचार", "स्वचालित बैकअप", "फ़ाइल प्रबंधन", "सिस्टम जानकारी", "उपयोगकर्ता प्रबंधन", "सॉफ़्टवेयर स्थापना", "नेटवर्क कॉन्फ़िगरेशन", "सुरक्षा स्वचालन", "कार्य शेड्यूलिंग", "रजिस्ट्री में बदलाव", "दूरस्थ प्रशासन"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "स्क्रिप्ट पकड़े एक कार्टून पात्र के सामने PowerShell प्रॉम्प्ट वाला कंप्यूटर है, जो शुरुआती लोगों के लिए PowerShell स्क्रिप्टिंग की सरलता दिखाता है"
coverCaption: ""
---
**शुरुआती लोगों के लिए PowerShell स्क्रिप्टिंग**

PowerShell, Microsoft द्वारा विकसित कमांड-लाइन शेल और स्क्रिप्टिंग भाषा है। इसमें Windows ऑपरेटिंग सिस्टम और अन्य Microsoft तकनीकों के अलग-अलग पहलुओं को प्रबंधित और स्वचालित करने के लिए कई कमांड और सुविधाएँ हैं। इस लेख में हम PowerShell स्क्रिप्टिंग की बुनियादी बातें बताएँगे और शुरुआत करने के लिए चरण-दर-चरण मार्गदर्शन देंगे।

## PowerShell का परिचय

**PowerShell** एक कमांड-लाइन शेल है, जिससे उपयोगकर्ता Windows ऑपरेटिंग सिस्टम और अन्य Microsoft तकनीकों को स्वचालित और प्रबंधित कर सकते हैं। इसमें फ़ाइलों और डायरेक्टरी का प्रबंधन, नेटवर्क कॉन्फ़िगरेशन और सिस्टम प्रबंधन जैसे प्रशासनिक काम करने के लिए कमांड और सुविधाओं का व्यापक संग्रह है। PowerShell एक स्क्रिप्टिंग भाषा भी देता है, जिससे जटिल स्क्रिप्ट बनाई जा सकती हैं और बार-बार होने वाले काम स्वचालित किए जा सकते हैं।

## PowerShell के साथ शुरुआत

### PowerShell इंस्टॉल करना

Windows के अधिकांश संस्करणों में PowerShell पहले से इंस्टॉल होता है। अगर आप Windows का पुराना संस्करण चला रहे हैं या PowerShell का नया संस्करण चाहते हैं, तो इसे Microsoft वेबसाइट से डाउनलोड करें। PowerShell डाउनलोड और इंस्टॉल करने के लिए ये चरण अपनाएँ:

1. [Microsoft PowerShell वेबसाइट](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) खोलें और इंस्टॉल करने के लिए PowerShell संस्करण चुनें।
2. इंस्टॉलेशन फ़ाइल डाउनलोड करके चलाएँ।
3. इंस्टॉलेशन पूरा करने के लिए स्क्रीन पर दिए निर्देशों का पालन करें।

### PowerShell शुरू करना

PowerShell इंस्टॉल करने के बाद इसे शुरू करने के लिए ये चरण अपनाएँ:

1. Start मेनू खोलें और खोज बार में "PowerShell" लिखें।
2. खोज परिणामों में "Windows PowerShell" चुनें।
3. PowerShell एक नई विंडो में खुलेगा।

### Visual Studio Code में PowerShell स्क्रिप्टिंग

बेहतर स्क्रिप्टिंग अनुभव के लिए आप लोकप्रिय एकीकृत विकास परिवेश (IDE) Visual Studio Code (VS Code) इस्तेमाल कर सकते हैं। VS Code में सिंटैक्स हाइलाइटिंग, कोड पूरा करने के सुझाव, डिबगिंग और एकीकृत टर्मिनल की सुविधा है, इसलिए यह PowerShell स्क्रिप्टिंग के लिए अच्छा विकल्प है। VS Code में शुरू करने के लिए:

1. [आधिकारिक वेबसाइट](https://code.visualstudio.com/) से Visual Studio Code इंस्टॉल करें।
2. VS Code के Extensions बाज़ार से Microsoft का "PowerShell" एक्सटेंशन इंस्टॉल करें।
3. VS Code में PowerShell स्क्रिप्ट फ़ाइल (.ps1) खोलें और स्क्रिप्ट लिखना शुरू करें।

### सिस्टम प्रशासन के लिए PowerShell

PowerShell सिस्टम प्रशासन के कामों के लिए एक बहुउपयोगी टूल है। सरल एक-पंक्ति कमांड से लेकर जटिल स्वचालन कार्यप्रवाह तक, यह उन कामों को आसान बनाता है जिनमें अन्यथा हाथ से दखल देना पड़ता। यह Windows, Linux और macOS पर एक समान स्क्रिप्टिंग मंच देता है, जिससे प्रशासक अलग-अलग परिवेशों को एक जैसी टूलकिट से प्रबंधित कर सकते हैं।

### Command Prompt से Windows PowerShell पर जाना

अगर आप Command Prompt से परिचित हैं और Windows PowerShell पर जाना चाहते हैं, तो सीखना सहज हो सकता है। Windows PowerShell स्क्रिप्टिंग Command Prompt की अवधारणाओं पर आधारित है और अधिक उन्नत सुविधाएँ देती है। अपने मौजूदा ज्ञान से शुरुआत करें और PowerShell की अतिरिक्त सुविधाओं तथा कमांडलेट को धीरे-धीरे जानें।

### PowerShell की बुनियादी बातें

PowerShell ऑपरेटिंग सिस्टम के साथ काम करने के लिए कमांड-लाइन इंटरफ़ेस देता है। इसके कमांड को कमांडलेट कहते हैं और वे मॉड्यूल में व्यवस्थित होते हैं। उपलब्ध मॉड्यूल देखने के लिए Get-Module कमांड चलाएँ:

```powershell
Get-Module
```

किसी मॉड्यूल में उपलब्ध कमांडलेट देखने के लिए Get-Command चलाएँ:
```powershell
Get-Command -Module <module name>
```

किसी कमांडलेट की मदद देखने के लिए Get-Help चलाएँ:
```powershell
Get-Help <कमांडलेट name>
```

PowerShell alias भी देता है, जो कमांडलेट के छोटे नाम हैं। उपलब्ध alias देखने के लिए Get-Alias चलाएँ:
```powershell
Get-Alias
```

## स्क्रिप्ट फ़ाइलें और निष्पादन नीति

PowerShell स्क्रिप्ट फ़ाइलों का एक्सटेंशन .ps1 होता है। स्क्रिप्ट चलाने से पहले आपको निष्पादन नीति सेट करनी पड़ सकती है। यह तय करती है कि स्क्रिप्ट चल सकती हैं या नहीं और किस प्रकार की स्क्रिप्ट की अनुमति है। नीति सेट करने के लिए Set-ExecutionPolicy कमांडलेट इस्तेमाल करें। उदाहरण के लिए, स्क्रिप्ट चलाने की अनुमति देने के लिए:

```powershell
Set-ExecutionPolicy RemoteSigned
```

या (केवल परीक्षण के लिए)

```powershell
Set-ExecutionPolicy Undefined
```

### PowerShell स्क्रिप्टिंग

PowerShell स्क्रिप्टिंग से कई प्रशासनिक काम स्वचालित किए जा सकते हैं। इसमें चर, लूप, सशर्त कथन और फ़ंक्शन समर्थित हैं, इसलिए यह स्वचालन का उपयोगी टूल है।

#### चर

PowerShell स्क्रिप्ट में डेटा रखने के लिए चर इस्तेमाल होते हैं। PowerShell में चर के नाम डॉलर चिह्न ($) से शुरू होते हैं। चर को मान देने के लिए यह सिंटैक्स इस्तेमाल करें:
```powershell
$variable_name = value
```
उदाहरण:
```powershell
$name = "John"
```
#### लूप

लूप कोड के किसी हिस्से को तय संख्या में दोहराते हैं। PowerShell में ये लूप उपलब्ध हैं:

- **For लूप**: कोड के हिस्से को तय संख्या में दोहराता है।
- **While लूप**: शर्त सही रहने तक कोड के हिस्से को दोहराता है।
- **Do-While लूप**: कोड को कम से कम एक बार चलाता है और फिर शर्त सही रहने तक दोहराता है।
- **ForEach लूप**: संग्रह के प्रत्येक आइटम के लिए कोड के हिस्से को दोहराता है।

उदाहरण के लिए, नीचे का कोड For लूप से 1 से 5 तक की संख्याएँ दिखाता है:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### सशर्त कथन

सशर्त कथन

सशर्त कथन किसी शर्त के सही होने पर कोड का एक हिस्सा चलाते हैं। PowerShell में ये प्रकार हैं:

- **If कथन**: शर्त सही होने पर कोड का एक हिस्सा चलाता है।
- **If-Else कथन**: शर्त सही होने पर एक हिस्सा और गलत होने पर दूसरा हिस्सा चलाता है।
- **Switch कथन**: किसी मान की तुलना संभावित मिलानों के समूह से करता है और पहला मेल मिलने पर उससे जुड़ा हिस्सा चलाता है।

उदाहरण के लिए, नीचे का कोड जाँचता है कि कोई संख्या 5 से बड़ी है या नहीं:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "संख्या 5 से बड़ी है"
}
```
#### फ़ंक्शन

फ़ंक्शन दोबारा इस्तेमाल किए जा सकने वाले कोड के हिस्से हैं, जो कोई खास काम करते हैं। फ़ंक्शन इनपुट पैरामीटर लेते हैं और आउटपुट मान लौटाते हैं। PowerShell में ये प्रकार हैं:

- **स्क्रिप्ट ब्लॉक**: कोड का ऐसा हिस्सा जिसे चलाया जा सकता है।
- **उन्नत फ़ंक्शन**: ऐसा फ़ंक्शन जिसमें मेटाडेटा और पैरामीटर सत्यापन शामिल हो।

उदाहरण के लिए, नीचे का कोड दो संख्याएँ जोड़ने वाला फ़ंक्शन परिभाषित करता है:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "परिणाम $result है"
```
### PowerShell ISE

PowerShell ISE (एकीकृत स्क्रिप्टिंग परिवेश) PowerShell स्क्रिप्टिंग के लिए एक ग्राफ़िकल इंटरफ़ेस है। इसमें समृद्ध टेक्स्ट संपादक, डिबगिंग टूल और अन्य सुविधाएँ हैं, जो स्क्रिप्ट लिखना और जाँचना आसान बनाती हैं। इसे खोलने के लिए:

1. Start मेनू खोलें और खोज बार में "PowerShell ISE" लिखें।
2. खोज परिणामों में "Windows PowerShell ISE" चुनें।
3. PowerShell ISE एक नई विंडो में खुलेगा।

### PowerShell Remoting

PowerShell Remoting से उपयोगकर्ता दूरस्थ कंप्यूटर पर PowerShell कमांड और स्क्रिप्ट चला सकते हैं। स्थानीय और दूरस्थ, दोनों कंप्यूटरों पर WinRM सेवा चलनी चाहिए। इसे चालू करने के लिए:

1. प्रशासक अधिकारों वाला PowerShell प्रॉम्प्ट खोलें।
2. PowerShell Remoting चालू करने के लिए यह कमांड चलाएँ:
```powershell
   Enable-PSRemoting -Force
```
3. दूरस्थ कंप्यूटर को TrustedHosts सूची में जोड़ने के लिए यह कमांड चलाएँ:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. WinRM सेवा फिर से शुरू करें।
```powershell
Restart-Service WinRM
```

दूरस्थ कंप्यूटर पर PowerShell कमांड चलाने के लिए Invoke-Command कमांडलेट इस्तेमाल करें:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell मॉड्यूल

PowerShell मॉड्यूल कमांडलेट, फ़ंक्शन और स्क्रिप्ट का संग्रह हैं, जिन्हें खास कामों के लिए बनाया जाता है। इन्हें PowerShell Gallery से इंस्टॉल और प्रबंधित किया जा सकता है। यह PowerShell मॉड्यूल का केंद्रीय भंडार है।

PowerShell Gallery से मॉड्यूल इंस्टॉल करने के लिए:
```powershell
Install-Module <module name>
```

इंस्टॉल किए गए मॉड्यूल देखने के लिए Get-InstalledModule चलाएँ:
```powershell
Get-InstalledModule
```

### PowerShell स्क्रिप्टिंग की अच्छी प्रथाएँ

**PowerShell स्क्रिप्ट** लिखते समय अच्छी प्रथाओं का पालन करें, ताकि वे **सुरक्षित**, **भरोसेमंद** और **आसानी से रखरखाव योग्य** हों। इन बातों पर ध्यान दें:

- **चर के वर्णनात्मक नाम रखें**: ऐसे नाम चुनें जो उनका उद्देश्य स्पष्ट करें।
- **टिप्पणियाँ लिखें**: कोड का उद्देश्य बताएँ।
- **त्रुटियों को संभालें**: त्रुटियों और अपवादों का उचित ढंग से निपटारा करें। PowerShell का `Try...Catch...Finally` ढाँचा अपवाद पकड़ने और उचित कदम उठाने देता है। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **स्क्रिप्ट अच्छी तरह जाँचें**: पुष्टि करें कि वे अपेक्षा के अनुसार चलती हैं। इकाई परीक्षण लिखने और चलाने के लिए PowerShell परीक्षण ढाँचा **Pester** इस्तेमाल किया जा सकता है। [Pester दस्तावेज़](https://pester.dev/)
- **फ़ंक्शन और मॉड्यूल इस्तेमाल करें**: कोड व्यवस्थित करें और उसका पुनः उपयोग बेहतर बनाएँ। फ़ंक्शन कोड को छोटे हिस्सों में बाँटते हैं और मॉड्यूल कोड को पैकेज करके साझा करने देते हैं। [फ़ंक्शन के बारे में](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [मॉड्यूल के बारे में](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **मानों को कोड में स्थिर न करें**: पैरामीटर या चर इस्तेमाल करें, ताकि स्क्रिप्ट अधिक लचीली और दोबारा इस्तेमाल योग्य हो। `param` कीवर्ड से स्क्रिप्ट को पैरामीटर दें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **विस्तृत आउटपुट इस्तेमाल करें**: स्क्रिप्ट की प्रगति की अतिरिक्त जानकारी दें। `Write-Verbose` कमांडलेट से विस्तृत संदेश दिखाए जा सकते हैं। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### PowerShell स्क्रिप्टिंग की अच्छी प्रथाओं का विस्तार

#### त्रुटियों को संभालें

त्रुटि प्रबंधन PowerShell स्क्रिप्टिंग का अहम हिस्सा है, क्योंकि इससे स्क्रिप्ट त्रुटियों और अपवादों का उचित ढंग से निपटारा करती है। PowerShell में कई तरीके हैं, जैसे Try-Catch कथन, Trap कथन और ErrorAction पैरामीटर। Try-Catch अपवादों को पकड़ता और संभालता है, Trap त्रुटियों को पकड़ता और संभालता है, और ErrorAction तय करता है कि स्क्रिप्ट त्रुटियों पर कैसी प्रतिक्रिया दे।

त्रुटि को संभालने के लिए Try-Catch का उदाहरण:
```powershell
try {
    # ऐसा कोड जिसमें त्रुटि आ सकती है
}
catch {
    Write-Error "त्रुटि हुई: $_"
}
```

#### स्क्रिप्ट अच्छी तरह जाँचें

PowerShell स्क्रिप्ट का परीक्षण करना ज़रूरी है, ताकि यह पुष्टि हो कि वे अपेक्षा के अनुसार चलती हैं। Pester जैसे टूल और परीक्षण ढाँचे परीक्षण लिखने और चलाने देते हैं। वे कोड की समस्याएँ खोजने और अलग करने तथा आवश्यकताओं के पूरा होने की पुष्टि करने में मदद करते हैं।

PowerShell स्क्रिप्ट जाँचने के लिए Pester का उदाहरण:
```powershell
Describe "मेरी PowerShell स्क्रिप्ट" {
    It "अपेक्षित काम करती है" {
        # ऐसा कोड जिसे अपेक्षित परिणाम लौटाना चाहिए
        $result = Do-Something
        $result | Should -Be "अपेक्षित परिणाम"
    }
}
```

#### फ़ंक्शन और मॉड्यूल इस्तेमाल करें

फ़ंक्शन और मॉड्यूल कोड व्यवस्थित करने और पुनः उपयोग बेहतर बनाने के लिए ज़रूरी हैं। फ़ंक्शन कोड को दोबारा इस्तेमाल होने वाले हिस्सों में रखते हैं, जबकि मॉड्यूल कोड को पैकेज करके दूसरों के साथ साझा करने देते हैं। इससे स्क्रिप्ट अधिक मॉड्यूलर, कुशल और रखरखाव योग्य बनती हैं।

PowerShell फ़ंक्शन का उदाहरण:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "$count प्रक्रियाएँ चल रही हैं।"
```

#### मानों को कोड में स्थिर न करें

PowerShell स्क्रिप्ट में मानों को स्थिर करने से लचीलापन कम होता है और रखरखाव कठिन होता है। इसके बजाय पैरामीटर या चर इस्तेमाल करें, ताकि उपयोगकर्ता रनटाइम पर मान दे सकें। इससे स्क्रिप्ट का पुनः उपयोग और बदलती परिस्थितियों के अनुसार ढलना आसान होता है।

PowerShell पैरामीटर का उदाहरण:
```powershell
param (
    [string]$name
)

Write-Host "नमस्ते, $name!"
```

#### विस्तृत आउटपुट इस्तेमाल करें

विस्तृत आउटपुट स्क्रिप्ट की प्रगति की जानकारी देता है और डिबगिंग तथा समस्या-समाधान में सहायक होता है। Write-Verbose कमांडलेट कंसोल पर अतिरिक्त जानकारी दिखाता है, जिससे स्क्रिप्ट को समझना और डिबग करना आसान होता है।

PowerShell में विस्तृत आउटपुट का उदाहरण:
```powershell
function Get-ProcessCount {
    Write-Verbose "प्रक्रियाएँ प्राप्त की जा रही हैं..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "$count प्रक्रियाएँ चल रही हैं।"
```

### शुरुआती लोगों के लिए PowerShell स्क्रिप्ट के दस विचार

अगर आप PowerShell स्क्रिप्टिंग सीखना शुरू कर रहे हैं, तो ये दस विचार आज़माएँ:

- **स्वचालित बैकअप**: महत्वपूर्ण फ़ाइलों और डायरेक्टरी का बाहरी हार्ड ड्राइव या क्लाउड स्टोरेज में बैकअप लेने वाली स्क्रिप्ट बनाएँ। फ़ाइलें कॉपी करने के लिए `Copy-Item` और बैकअप को पृष्ठभूमि में चलाने के लिए `Start-Job` कमांडलेट इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **फ़ाइल प्रबंधन**: फ़ाइलों और डायरेक्टरी को प्रकार, आकार या अन्य मानदंडों के आधार पर अलग-अलग फ़ोल्डर में रखने वाली स्क्रिप्ट बनाएँ। फ़ाइलें पाने के लिए `Get-ChildItem` और उन्हें मनचाही जगह ले जाने के लिए `Move-Item` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **सिस्टम जानकारी**: CPU और मेमोरी उपयोग, डिस्क स्थान और नेटवर्क सेटिंग जैसी जानकारी पाकर उसे आसानी से पढ़े जाने वाले रूप में दिखाने वाली स्क्रिप्ट बनाएँ। जानकारी पाने के लिए `Get-WmiObject` और उसे व्यवस्थित करने के लिए `Format-Table` या `Out-GridView` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **उपयोगकर्ता प्रबंधन**: Windows में उपयोगकर्ता और समूह जोड़ने, बदलने या हटाने के काम को स्वचालित करने वाली स्क्रिप्ट बनाएँ। उपयोगकर्ता प्रबंधन के लिए `New-LocalUser`, `Set-LocalUser` और `Remove-LocalUser`; समूहों के लिए `New-LocalGroup`, `Add-LocalGroupMember` और `Remove-LocalGroup` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **सॉफ़्टवेयर स्थापना**: एक साथ कई कंप्यूटरों पर सॉफ़्टवेयर इंस्टॉल और कॉन्फ़िगर करने वाली स्क्रिप्ट बनाएँ। दूरस्थ कंप्यूटर पर इंस्टॉलेशन कमांड चलाने के लिए `Invoke-Command` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **नेटवर्क कॉन्फ़िगरेशन**: IP पता, सबनेट मास्क और डिफ़ॉल्ट गेटवे जैसी नेटवर्क सेटिंग स्वचालित करने वाली स्क्रिप्ट बनाएँ। इन सेटिंग के लिए `Set-NetIPAddress`, `Set-NetIPInterface` और `Set-DnsClientServerAddress` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **सुरक्षा**: सुरक्षा सेटिंग का ऑडिट और निगरानी करने तथा बदलाव मिलने पर उपयोगकर्ता को सूचित करने वाली स्क्रिप्ट बनाएँ। ऑडिट नीतियाँ पाने के लिए `Get-AuditPolicy` और ईमेल सूचना भेजने के लिए `Send-MailMessage` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **कार्य शेड्यूलिंग**: बैकअप, अपडेट और सिस्टम स्कैन जैसे नियमित काम तय करके स्वचालित करने वाली स्क्रिप्ट बनाएँ। तय किए गए काम बनाने के लिए `Register-ScheduledTask` और उन्हें चलाने के लिए `Start-ScheduledTask` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **रजिस्ट्री में बदलाव**: खास कुंजियों या मानों के लिए रजिस्ट्री मान देखने या बदलने वाली स्क्रिप्ट बनाएँ। रजिस्ट्री के साथ काम करने के लिए `Get-ItemProperty` और `Set-ItemProperty` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **दूरस्थ प्रशासन**: Windows कंप्यूटरों का दूरस्थ प्रशासन चालू करने और दूरस्थ मशीनों पर कमांड तथा स्क्रिप्ट चलाने वाली स्क्रिप्ट बनाएँ। दूरस्थ कंप्यूटर पर कमांड चलाने के लिए `Enter-PSSession` या `Invoke-Command` इस्तेमाल करें। [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft दस्तावेज़](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

इन विचारों से व्यावहारिक अनुभव लें और PowerShell स्क्रिप्टिंग का ज्ञान बढ़ाएँ।

## निष्कर्ष

PowerShell Windows ऑपरेटिंग सिस्टम और अन्य Microsoft तकनीकों को प्रबंधित तथा स्वचालित करने का शक्तिशाली टूल है। इस लेख में हमने शुरुआती लोगों के लिए स्क्रिप्टिंग की बुनियादी बातें देखीं, जिनमें इंस्टॉल और शुरू करना, कमांडलेट, चर, लूप, सशर्त कथन और फ़ंक्शन इस्तेमाल करना, साथ ही PowerShell ISE, PowerShell Remoting और मॉड्यूल शामिल हैं। अच्छी प्रथाओं से स्क्रिप्ट सुरक्षित, भरोसेमंद और रखरखाव योग्य बनती हैं। अभ्यास के साथ आप PowerShell में दक्ष होकर कई प्रशासनिक काम आसानी से स्वचालित कर सकते हैं।
