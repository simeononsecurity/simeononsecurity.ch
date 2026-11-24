---
title: "Kali Purple 2023.1: अपडेट और मुख्य विशेषताएँ"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Kali Purple 2023.1 की ऐतिहासिक सुविधाओं, टूल और सुधारों की समीक्षा, सुरक्षा लैब के लिए वर्तमान संदर्भों सहित।"
tags: ["Kali Linux", "Kali Purple", "2023.1", "एथिकल हैकिंग", "पेनेट्रेशन टेस्टिंग", "साइबर सुरक्षा", "टूल", "एक्सप्लॉइट फ्रेमवर्क", "Kali ARM अपडेट", "Kali NetHunter", "Kali दस्तावेज़", "कर्नेल समर्थन", "Bluetooth समर्थन", "LineageOS", "OneUI", "Radxa Zero", "सिंगल-बोर्ड कंप्यूटर", "कर्नेल पैच", "समुदाय का योगदान", "Kali Discord", "Linux अपडेट", "एथिकल हैकिंग वितरण", "नई सुविधाएँ", "सुधार", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "नए टूल और पैकेज", "ARM डिवाइस समर्थन", "Kali दस्तावेज़", "सरकारी नियम"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Kali Linux का त्रि-आयामी ड्रैगन एक ढाल पर बैठा है और उसके चारों ओर साइबर सुरक्षा टूल हैं।"
coverCaption: ""
---

**Kali Purple 2023.1: समीक्षा**

Kali Purple 2023.1, Kali की रक्षात्मक सुरक्षा दिशा का पहला तकनीकी preview था। अब यह Kali की नवीनतम release नहीं है। यह लेख मूल release का रिकॉर्ड रखता है और वर्तमान संदर्भ जोड़ता है, ताकि आप 2023.1 के पैकेज संस्करण को वर्तमान versions न समझें।

## Kali की वर्तमान स्थिति

Kali का आधिकारिक रिलीज़ इतिहास 29 जून 2026 को जारी Kali 2026.2 को 2026 की दूसरी निरंतर अपडेट वाला रिलीज़ बताता है। इसमें Linux कर्नेल 6.19 और Xfce 4.20.7 हैं। [Kali 2026.2 रिलीज़ नोट्स](https://www.kali.org/blog/kali-linux-2026-2-release/) में GNOME 50, KDE Plasma 6.6, `sources.list` से `sources.list.d/kali.source` पर बदलाव और virtual machine boot में परिवर्तन भी बताए गए हैं।

Kali Purple, Kali के भीतर defensive और purple-team दिशा है। 2023.1 की घोषणा ने इसे SOC-in-a-box संदर्भ वास्तुकला, रक्षात्मक उपकरण और NIST Cybersecurity Framework की मेनू श्रेणियाँ वाला तकनीकी पूर्वावलोकन बताया था। ये ऐतिहासिक दायरे के विवरण हैं। वर्तमान packages चुनने के लिए Kali का [मेटापैकेज दस्तावेज़](https://www.kali.org/docs/general-use/metapackages/) देखें और अपने lab के लिए आवश्यक उपकरण समूह ही चुनें।

*हर offensive या रक्षात्मक सुरक्षा अभ्यास अलग-थलग और अधिकृत lab में करें। Kali install करने से आपको उन systems को test करने की अनुमति नहीं मिलती जिनका आप स्वामित्व या प्रबंधन नहीं करते।*

______

## Kali वॉलपेपर और desktop अपडेट

Kali Purple 2023.1 में Kali Sticker नाम का **नया डिफ़ॉल्ट वॉलपेपर** है। इसमें बैंगनी पृष्ठभूमि और Kali से जुड़े कई sticker हैं। यह wallpaper /u/Albert-III- और TJ_Null के काम से प्रेरित है।

नए wallpaper के साथ Kali Purple 2023.1 तीन मुख्य डेस्कटॉप परिवेश भी अपडेट करता है: **Xfce, KDE और GNOME**। इन अपडेट में नई सुविधाएँ, performance सुधार और बग सुधार शामिल हैं।

______

## Xfce 4.18

**Xfce 4.18** में कई उल्लेखनीय सुधार हैं, जैसे:

- UI scaling के लिए बेहतर समर्थन
- Thunar फ़ाइल प्रबंधक अपडेट
- आसान अनुकूलन के लिए panel profiles

______

## KDE Plasma 5.27

**KDE Plasma 5.27** अपडेट में शामिल हैं:

- नई विंडो को टाइलों में व्यवस्थित करना प्रणाली
- अधिक आकर्षक ऐप थीम
- अधिक साफ़ और उपयोगी tools और widgets

______

## GNOME अपडेट

GNOME में Kali Purple 2023.1 usability सुधार लाता है। उदाहरण के लिए, F4 दबाकर फ़ाइल प्रबंधक के वर्तमान folder में terminal जल्दी खोला जा सकता है।

______

## डिफ़ॉल्ट कर्नेल सेटिंग और ज्ञात समस्याएँ

बेहतर usability के लिए Kali Purple 2023.1 कुछ kernel defaults अपडेट करता है।

______

## नए टूल और पैकेज

Kali Purple 2023.1 **पेनेट्रेशन परीक्षण** और **नैतिक हैकिंग** के लिए नई क्षमताएँ जोड़ता है। इनमें ये नए tools और packages शामिल हैं:

- **Rizin 0.3.0**: आधुनिक reverse-engineering framework
- **Ghidra 10.1**: software रिवर्स इंजीनियरिंग के लिए open-source suite
- **Python 3.10**: लोकप्रिय प्रोग्रामिंग भाषा का नवीनतम संस्करण

इन tools और मौजूदा packages के अपडेट ने सुरक्षा पेशेवरों के लिए 2023.1 preview का विस्तार किया। इस भाग के versions 2023.1 release के हैं, Kali 2026.2 में शामिल versions के नहीं।

______

## ARM डिवाइस समर्थन

Kali Purple 2023.1 ARM उपकरणों का समर्थन बढ़ाता है। यह **Radxa Zero** जैसे नए devices के लिए compatibility जोड़ता है और **LG V20** जैसे devices का मौजूदा support बेहतर करता है। इससे छोटे एकल-बोर्ड कंप्यूटर से लेकर शक्तिशाली smartphones तक कई तरह के hardware पर Kali चलाया जा सकता है।

______

## दस्तावेज़ और समुदाय

Kali टीम ने **documentation** में नए guides, tutorials और troubleshooting सुझाव जोड़े, ताकि users Kali Purple 2023.1 का बेहतर उपयोग कर सकें। टीम ने Kali में योगदान देने वाले समुदाय के कई सदस्यों को भी सम्मानित किया, जो open-source सहयोग और Kali समुदाय की ताकत दिखाता है।

______

## सरकारी नियम

यह लेख नैतिक हैकिंग या पेनेट्रेशन परीक्षण से जुड़े किसी खास सरकारी नियम की समीक्षा नहीं करता। फिर भी, कई क्षेत्रों में ये गतिविधियाँ नियंत्रित हैं। सुरक्षा आकलन करते समय उचित अनुमति लें और लागू कानूनों का पालन करें। संबंधित नियमों के लिए देखें:

- [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## निष्कर्ष

**Kali Purple 2023.1** Kali की रक्षात्मक सुरक्षा दिशा का पहला preview था। इसने toolset बढ़ाया, ARM support सुधारा और documentation का विस्तार किया। वर्तमान installation के लिए Kali रिलीज़ नोट्स देखें और अपने lab के लिए सही packages चुनें। लागू नियमों का पालन करें और केवल स्पष्ट अनुमति वाले systems का test करें।

______

## संदर्भ

1. [Kali Linux की आधिकारिक वेबसाइट](https://www.kali.org/)
2. [Kali Linux दस्तावेज़](https://www.kali.org/docs/)
3. [Kali Linux डाउनलोड](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## अतिरिक्त संसाधन

- [Kali Linux के आधिकारिक फ़ोरम](https://forums.kali.org/)
- [Kali Linux ब्लॉग](https://www.kali.org/blog/)
- [Kali Linux प्रशिक्षण और प्रमाणन](https://www.offensive-security.com/)

______

## अपडेट जाँच सूची

- **रिलीज़ इतिहास देखें.** इमेज डाउनलोड करने से पहले Kali का [वर्तमान रिलीज़ इतिहास](https://www.kali.org/releases/) पढ़ें।
- **आधिकारिक इमेज इस्तेमाल करें.** [Get Kali](https://www.kali.org/get-kali/) से इमेज डाउनलोड करें और प्रकाशित checksum सत्यापित करें।
- **rolling इंस्टॉलेशन अपडेट करें.** 2023.1 के repository उदाहरण को बिना जाँचे कॉपी करने के बजाय Kali का [वर्तमान अपडेट दस्तावेज़](https://www.kali.org/docs/general-use/updating-kali/) अपनाएँ।
- **मेटापैकेज सोचकर चुनें.** Standard या Purple लैब को Kali के हर package की ज़रूरत नहीं होती।
- **लैब का दायरा दर्ज करें.** टूल चलाने से पहले अधिकृत systems, परीक्षण अवधि, logging और cleanup तय करें।
