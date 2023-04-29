---
title: "Hardening Your Computer's Security by Disabling SSL and TLS 1.2 and Below"
date: 2023-02-08
toc: true
draft: false
description: "This article discusses the steps to improve data security by disabling older versions of SSL and TLS protocols, which are vulnerable to cyber threats such as POODLE, BEAST, and Heartbleed, in Windows and Linux systems."
tags: ["Hardening computer security", "Disabling SSL and TLS", "Data security", "POODLE", "BEAST", "Heartbleed", "Windows registry editor", "Linux OpenSSL configuration", "Apache", "Nginx"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "A computer with a padlock symbol representing data security"
coverCaption: ""
---
```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# Disable DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1"

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```
 ## परिचय:  कंप्यूटर हमारे दैनिक जीवन का एक महत्वपूर्ण पहलू बन गए हैं और इसके साथ ही डेटा सुरक्षा की आवश्यकता काफी हद तक बढ़ गई है। असुरक्षित डेटा को सुरक्षित करने के लिए उपयोग करने वाले विभिन्न खाते में, एसएसएल (सिक्योर निर्धारण लेआउट) और टीएलएस (ट्रांसक्रिप्शन परत कई) व्यापक रूप से उपयोग किए जाने वाले प्रोटोकॉल हैं। हालाँकि, जैसी-जैसी तकनीक विकसित होती है, इन प्रोटोकॉल के पुराने संस्करण साइबर-हमलों के प्रति संवेदनशील होते जा रहे हैं। इस लेख में, हम डेटा को सुरक्षित रखने के लिए एसएसएल और सभी टीएलएस संस्करण 1.2 और नीचे की ओर काम करने वाले कंप्यूटरों को सख्त करने के चरणों पर चर्चा करेंगे।  ### एसएसएल और टीएलएस 1.2 और उसके नीचे के वर्जन को मैटिक क्यों करें?  SSL और TLS का पुराना संस्करण पूडल (डाउनग्रेड लिगेसी शेयर पर पैडिंग Oracle), BEAST (SSL/TLS के खिलाफ लेयर एक्सप्लॉइट) और हार्टब्लिड जैसे कई सुरक्षा दायित्वों के प्रति संवेदनशील हैं। इन संपत्तियों की संवेदनशील जानकारी का जोखिम हो सकता है, किसी भी पुराने प्रोटोकॉल के उपयोग को वेब करना महत्वपूर्ण हो जाता है।  ### फिक्स में SSL और टी-एलएस 1.2 और अधोसंबद्ध:  लिपिक में, एसएसएल और टीएलएस 1.2 के माध्यम से रजिस्ट्री संपादक के माध्यम से और असंगत करने की प्रक्रिया को प्राप्त किया जा सकता है। यहाँ कार्य को पूरा करने के लिए एक पॉवरशेल स्क्रिप्ट है:   #### लिनक्स में एसएसएल और टीएलएस 1.2 और नीचे अक्षम करना:  लिनक्स में, एसएसएल और टीएलएस 1.2 और नीचे की प्रक्रिया को ओपनएसएसएल कॉन्फ़िगरेशन फ़ाइल को संशोधित करके प्राप्त किया जा सकता है। यहां अनुसरण करने के चरण दिए गए हैं:  1. टर्मिनल खोलें और रूट के रूप में लॉग इन करें। 2. OpenSSL कॉन्फ़िगरेशन फ़ाइल पर नेविगेट करें। आमतौर पर, यह /etc/ssl/openssl.cnf पर स्थित होता है। 3. नैनो या विम जैसे पाठ संपादक का उपयोग करके फ़ाइल खोलें। 4. SSLProtocol निर्देश का पता लगाएँ और इसके मान को -TLSv1.2 पर सेट करें। 5. फाइल को सेव करें और टेक्स्ट एडिटर को बंद करें। 6. परिवर्तनों को प्रभावी करने के लिए उन सेवाओं को पुनः आरंभ करें जो OpenSSL का उपयोग करती हैं, जैसे कि Apache या Nginx।  ## निष्कर्ष:  एसएसएल और सभी टीएलएस संस्करण 1.2 और नीचे को अक्षम करके, आप अपने कंप्यूटर की सुरक्षा को सख्त कर सकते हैं और संभावित साइबर खतरों से संवेदनशील जानकारी की रक्षा कर सकते हैं। यह एक सरल प्रक्रिया है जिसे न्यूनतम प्रयास से पूरा किया जा सकता है, जिससे यह आपके कंप्यूटर की सुरक्षा को बनाए रखने का एक महत्वपूर्ण पहलू बन जाता है। इस लेख में उल्लिखित चरणों को लागू करके, आप अपने डेटा को सुरक्षित रख सकते हैं और साइबर हमलों को रोक सकते हैं, जिससे संवेदनशील जानकारी के उजागर होने का जोखिम कम हो जाता है।  यह ध्यान रखना महत्वपूर्ण है कि एसएसएल और टीएलएस प्रोटोकॉल के इन पुराने संस्करणों को अक्षम करने से आपके कंप्यूटर की सुरक्षा में सुधार हो सकता है, यह कुछ पुराने सिस्टम के साथ संगतता को भी प्रभावित कर सकता है। इसलिए, किए गए परिवर्तनों का पूरी तरह से परीक्षण करना और उन्हें पूरी तरह से लागू करने से पहले यह सुनिश्चित करना आवश्यक है कि आपके सिस्टम पर कोई प्रतिकूल प्रभाव नहीं पड़ रहा है।  अंत में, संवेदनशील जानकारी की सुरक्षा को बनाए रखने और साइबर हमलों को रोकने के लिए एसएसएल और सभी टीएलएस संस्करणों 1.2 और नीचे को अक्षम करके अपने कंप्यूटर को सख्त बनाना एक महत्वपूर्ण कदम है। इस आलेख में उल्लिखित चरण आपके कंप्यूटर को सुरक्षित करने के लिए एक सीधी मार्गदर्शिका प्रदान करते हैं, जिससे व्यक्तियों और संगठनों के लिए आवश्यक सुरक्षा उपायों को लागू करना आसान हो जाता है।