---
title: "SSL और TLS 1.1 तथा उससे पुराने संस्करण बंद करके कंप्यूटर की सुरक्षा मजबूत करें"
date: 2023-02-08
lastmod: 2026-11-14
toc: true
draft: false
description: "TLS 1.2 या नया संस्करण चालू रखते हुए SSL और पुराने TLS संस्करण बंद करें। इसमें Windows Schannel, .NET और Linux सेवाएँ शामिल हैं।"
tags: ['कंप्यूटर सुरक्षा मजबूत करना', 'SSL और TLS बंद करना', 'डेटा सुरक्षा', 'POODLE', 'BEAST', 'Heartbleed', 'Windows रजिस्ट्री संपादक', 'Linux OpenSSL कॉन्फ़िगरेशन', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "डेटा सुरक्षा दर्शाने वाले ताले के चिह्न वाला कंप्यूटर"
coverCaption: ""
---

## परिचय:

कंप्यूटर हमारे रोज़मर्रा के जीवन का अहम हिस्सा बन गए हैं, इसलिए डेटा सुरक्षा की ज़रूरत भी बढ़ी है। डेटा के संचार के दौरान उसकी सुरक्षा के लिए SSL (Secure Socket Layer) और TLS (Transport Layer Security) प्रोटोकॉल व्यापक रूप से उपयोग होते हैं। तकनीक के विकास के साथ इनके पुराने संस्करण साइबर हमलों के प्रति असुरक्षित हो गए हैं। यह लेख बताता है कि TLS 1.2 या TLS 1.3 उपलब्ध रखते हुए SSL और TLS 1.0 तथा 1.1 को कैसे बंद करें।

*TLS 1.2 अप्रचलित प्रोटोकॉल नहीं है। मौजूदा न्यूनतम मान TLS 1.2 या नया है। [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) TLS 1.3 को परिभाषित करता है, जबकि [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) औपचारिक रूप से TLS 1.0 और TLS 1.1 को अप्रचलित घोषित करता है।*

### SSL और TLS 1.1 तथा उससे पुराने संस्करण क्यों बंद करें?

SSL और TLS के पुराने संस्करण POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) और Heartbleed जैसे सुरक्षा खतरों के प्रति असुरक्षित हैं। इन हमलों से संवेदनशील जानकारी उजागर हो सकती है, इसलिए पुराने प्रोटोकॉल बंद करना ज़रूरी है। Heartbleed स्वयं कोई प्रोटोकॉल संस्करण नहीं था, बल्कि इसने OpenSSL के असुरक्षित कार्यान्वयनों को प्रभावित किया था। लाइब्रेरी को पैच करें और उजागर हुए क्रेडेंशियल बदलें।

Microsoft की मौजूदा [Schannel रजिस्ट्री मार्गदर्शिका](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) समर्थित Windows रिलीज़ के प्रोटोकॉल सेटिंग सूचीबद्ध करती है। जहाँ उपलब्ध हों, Microsoft Group Policy या अन्य समर्थित प्रबंधन टूल की सलाह देता है। सीधे रजिस्ट्री में बदलाव तभी करें जब बेहतर नियंत्रण उपलब्ध न हो।

### Windows में SSL और TLS 1.1 तथा उससे पुराने संस्करण बंद करना:

Windows में रजिस्ट्री संपादक से SSL और TLS 1.1 तथा उससे पुराने संस्करण बंद किए जा सकते हैं। नीचे दी गई PowerShell स्क्रिप्ट Schannel की क्लाइंट और सर्वर सेटिंग बदलती है। यह .NET को ऑपरेटिंग सिस्टम के TLS डिफ़ॉल्ट और मज़बूत क्रिप्टोग्राफी का उपयोग करने के लिए भी सेट करती है।

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
# SSL v2 अक्षम करें
Disable-Protocol -Protocol "SSL 2.0"
# SSL v3 अक्षम करें
Disable-Protocol -Protocol "SSL 3.0"
# TLS 1.0 अक्षम करें
Disable-Protocol -Protocol "TLS 1.0"
# DTLS 1.0 अक्षम करें
Disable-Protocol -Protocol "DTLS 1.0"
# TLS 1.1 अक्षम करें
Disable-Protocol -Protocol "TLS 1.1"
# DTLS 1.1 प्रोटोकॉल मौजूद नहीं है। RFC 8996, DTLS 1.0 को अप्रचलित घोषित करता है और DTLS 1.2 को बनाए रखता है।

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

#### Linux में SSL और TLS 1.1 तथा उससे पुराने संस्करण बंद करना:

Linux में पुराने प्रोटोकॉल बंद करने का तरीका एप्लिकेशन और लाइब्रेरी पर निर्भर करता है। `/etc/ssl/openssl.cnf` बदलने से हर डेमॉन या बंडल की गई TLS लाइब्रेरी की सेटिंग नहीं बदलती। ये कदम अपनाएँ:

1. टर्मिनल खोलें और root के रूप में लॉग इन करें।
2. OpenSSL कॉन्फ़िगरेशन फ़ाइल पर जाएँ। यह आम तौर पर /etc/ssl/openssl.cnf में होती है।
3. फ़ाइल को nano या vim जैसे टेक्स्ट एडिटर में खोलें।
4. सेवा का प्रोटोकॉल निर्देश ढूँढें और न्यूनतम संस्करण TLS 1.2 रखें। पुराना `-TLSv1.2` विकल्प TLS 1.2 को बंद करता था, इसलिए इसे आधुनिक न्यूनतम मान के रूप में उपयोग न करें।
5. फ़ाइल सहेजें और टेक्स्ट एडिटर बंद करें।
6. बदलाव लागू करने के लिए OpenSSL उपयोग करने वाली सेवाएँ, जैसे Apache या Nginx, पुनः आरंभ करें।

## निष्कर्ष:

SSL और TLS 1.1 तथा उससे पुराने संस्करण बंद करने से आधुनिक TLS क्लाइंट के साथ संगतता बनाए रखते हुए कंप्यूटर की सुरक्षा मजबूत होती है। सही सेटिंग उस सेवा में होती है जो TLS कनेक्शन पर बातचीत करती है। हर एप्लिकेशन की जाँच करें, यह न मानें कि एक OpenSSL फ़ाइल हर डेमॉन नियंत्रित करती है।

इन पुराने संस्करणों को बंद करने से कुछ पुराने सिस्टम के साथ संगतता प्रभावित हो सकती है। बदलाव पूरी तरह लागू करने से पहले उनका अच्छी तरह परीक्षण करें और सुनिश्चित करें कि सिस्टम पर प्रतिकूल प्रभाव न पड़े।

संवेदनशील जानकारी सुरक्षित रखने और हमलों का जोखिम घटाने के लिए इस लेख के कदम अपनाएँ। पहले पहचानें कि हर सेवा कौन-सा प्रोटोकॉल बातचीत में उपयोग करती है, फिर अस्थायी अपवाद दर्ज करें।

## मौजूदा सत्यापन सूची

- **बातचीत में चुने गए प्रोटोकॉल की पुष्टि करें।** TLS स्कैनर या स्वीकृत आंतरिक परीक्षण से कनेक्शन के दोनों सिरों पर क्लाइंट और सर्वर जाँचें।
- **TLS 1.2 चालू रखें।** कुछ पुराने एप्लिकेशन को अभी भी इसकी ज़रूरत है, जबकि TLS 1.3 का समर्थन ऑपरेटिंग सिस्टम और लाइब्रेरी पर निर्भर करता है।
- **DTLS की अलग से समीक्षा करें।** RFC 8996 DTLS 1.0 को अप्रचलित घोषित करता है। यह DTLS 1.1 प्रोटोकॉल परिभाषित नहीं करता।
- **प्रभावित सेवाएँ पुनः आरंभ करें।** नई नीति लागू करने के लिए Schannel और एप्लिकेशन सेटिंग में अक्सर सेवा या सिस्टम को पुनः आरंभ करना पड़ता है।
- **अपवाद दर्ज करें।** ऐसे हर पुराने एंडपॉइंट को दर्ज करें जिसे अस्थायी संगतता सेटिंग चाहिए और उसे हटाने की तारीख तय करें।
