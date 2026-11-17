---
title: "SenseCAP M1 Raspberry Pi Shield: पिनआउट और LoRaWAN में पुनः उपयोग"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "SenseCAP M1 शील्ड को समझें, परस्पर विरोधी GPIO मैप की तुलना करें, ATECC608 की जाँच करें और आधुनिक Raspberry Pi OS से LoRaWAN गेटवे की योजना बनाएँ।"
genre: ["Raspberry Pi", "IoT", "हार्डवेयर सुरक्षा"]
tags: ["SenseCAP M1", "SenseCAP M1 शील्ड", "SenseCAP M1 पिनआउट", "Raspberry Pi शील्ड", "Raspberry Pi HAT", "LoRaWAN गेटवे", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium हॉटस्पॉट पुनः उपयोग", "LoRa concentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C डायग्नोस्टिक्स", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "हार्डवेयर रिवर्स इंजीनियरिंग"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Seeed WM1302 मॉड्यूल, Raspberry Pi हेडर, एंटीना केबल, USB-C सॉकेट और पंखे के कनेक्टर वाला SenseCAP M1 शील्ड"
coverCaption: "बोर्ड की तस्वीर: Clockwork Bird, 2023। स्रोत और श्रेय लेख के अंत में हैं।"
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**SenseCAP M1 शील्ड LoRaWAN गेटवे हार्डवेयर के रूप में उपयोगी है, लेकिन इसकी वायरिंग के लिए सामान्य Raspberry Pi HAT ट्यूटोरियल से अधिक जाँच की जरूरत है।** यह गाइड [Clockwork Bird की 2023 की पड़ताल](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) में निर्माता के दस्तावेज़, upstream ड्राइवर की समीक्षा और मौजूदा GPIO मार्गदर्शन जोड़ती है। आप हार्डवेयर पहचानेंगे, पक्के तथ्यों और अधूरे पिनआउट प्रमाण को अलग करेंगे और दोहराई जा सकने वाली शुरुआत का रिकॉर्ड बनाएँगे।

> **दायरा:** यह दस्तावेज़ों पर आधारित हार्डवेयर गाइड है। इस लेख के लिए कमांड और बोर्ड मैप किसी असली M1 पर नहीं जाँचे गए।

## मुख्य बातें

- **दोनों बोर्ड पहचानें:** M1 कैरियर और हटाया जा सकने वाला concentrator अलग मॉडल और संशोधन रखते हैं।
- **रीसेट स्क्रिप्ट जाँचें:** CoreCell के डिफ़ॉल्ट प्रकाशित M1 पिनआउट के कुछ सिग्नलों से टकराते हैं।
- **OS इंटरफ़ेस देखें:** SPI डिवाइस फ़ाइलें, GPIO नंबरिंग और GPIO टूल के संस्करण अलग सवालों के जवाब देते हैं।
- **सिक्योर एलिमेंट का प्रावधान सुरक्षित रखें:** डिवाइस की जानकारी पढ़ना, उसे कॉन्फ़िगर करने या कुंजी बनाने से अलग है।
- **पूरा मार्ग साबित करें:** concentrator का पता लगना सेंसर डेटा की डिलीवरी साबित नहीं करता।

## शुरू करने से पहले

**कठिनाई: मध्यम।** सूची बनाने, OS तैयार करने और दस्तावेज़ जाँचने के लिए लगभग एक से दो घंटे रखें। विद्युत जाँच, ड्राइवर अनुकूलन और नेटवर्क सर्वर लगाने में अतिरिक्त समय लगेगा, खासकर जब बोर्ड संशोधन अज्ञात हो।

| वस्तु | उद्देश्य |
|---|---|
| **M1 शील्ड और concentrator** | कैरियर संशोधन और मॉड्यूल का पूरा लेबल पढ़ें |
| **Raspberry Pi 4** | मूल M1 डिज़ाइन में इस्तेमाल होस्ट से शुरू करें |
| **अतिरिक्त microSD कार्ड** | मूल इंस्टॉलेशन बचाकर अलग OS तैयार करें |
| **सही बिजली आपूर्ति और एंटीना** | असेंबली और मॉड्यूल के RF बैंड से मेल करें |
| **SSH या स्थानीय कंसोल** | डायग्नोस्टिक्स दर्ज करें और कॉन्फ़िगरेशन संपादित करें |
| **LoRaWAN सेंसर और सर्वर** | हार्डवेयर शुरू करने के बाद ऐप तक वास्तविक डिलीवरी जाँचें |
| **मीटर और हार्डवेयर अनुभव** | अज्ञात कनेक्शन चलाने से पहले स्पष्ट करें |

कुछ भी हटाने से पहले बिना बिजली के असेंबली के दोनों ओर की तस्वीर लें। कनेक्टर की दिशा, स्क्रू, स्पेसर और एंटीना का मार्ग लिखें। वैकल्पिक इंस्टॉलेशन के स्वीकृति परीक्षण पास होने तक मूल कार्ड और कॉन्फ़िगरेशन उपलब्ध रखें।

## तीन परतें पहचानें

**पूरा M1, कैरियर शील्ड और concentrator अलग-अलग हिस्से हैं।** Seeed के दस्तावेज़ पूरे hotspot को Raspberry Pi 4 और WM1302/SX1302 या WM1303/SX1303 concentrator के रूप में बताते हैं। “SenseCAP M1 shield” नाम की सूची से यह साबित नहीं होता कि कैरियर के साथ इनमें से कौन सा हिस्सा आता है। [Seeed Studio का M1 परिचय](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**कैरियर** Pi और मॉड्यूल के बीच बिजली और पेरिफ़रल सिग्नल जोड़ता है। **Concentrator** रेडियो प्राप्ति और प्रसारण संभालता है। होस्ट पर चलने वाला **पैकेट फ़ॉरवर्डर** सर्वर के साथ प्राप्त रेडियो पैकेट और निर्धारित downlink का आदान-प्रदान करता है। [Semtech का SX1302 HAL परिचय](https://github.com/Lora-net/sx1302_hal)

उदाहरण के लिए, शेल्फ़ का तापमान सेंसर रेडियो से uplink भेजता है। Concentrator उसे प्राप्त करता है, होस्ट आगे भेजता है, फिर नेटवर्क और ऐप्लिकेशन सेवाएँ उसे संसाधित करती हैं। Linux का शुरू होना इस शृंखला का केवल होस्ट वाला हिस्सा साबित करता है।

Clockwork Bird की तस्वीर में M1 v1.1 कैरियर पर `WM1302-SPI-EU868` लेबल वाला मॉड्यूल दिखता है। अपने उपकरण पर लेबल ढूँढ़ने के लिए तस्वीर देखें। सीरियल नंबर तस्वीर वाले उपकरण की पहचान करते हैं, किसी अन्य गेटवे के कॉन्फ़िगरेशन की नहीं।

{{< figure src="m1-carrier-wm1302-board.webp" alt="हरे M1 कैरियर पर लेबल वाला WM1302 SPI EU868 मॉड्यूल, USB-C, बटन, पंखे का सॉकेट और एंटीना केबल के साथ" caption="Clockwork Bird की खींची M1 v1.1 तस्वीर, लेख के कवर में भी उपयोग हुई" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## बिजली और रेडियो कनेक्शन

**M1 के USB-C कनेक्टर को बिजली का इनपुट मानें।** निर्माता पूरे गेटवे के लिए DC 5 V, 3 A बताता है और USB-C को बिजली आपूर्ति इंटरफ़ेस कहता है। इसे चार्जिंग पोर्ट कहने से ऐसी बैटरी का संकेत मिलता है जिसका विनिर्देश में उल्लेख नहीं है। [SenseCAP M1 विनिर्देश](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

निर्माता का ब्लॉक डायग्राम 5 V सप्लाई को मॉड्यूल की विनियमित 3.3 V रेल से अलग दिखाता है। समस्या जाँचते समय यह अंतर अहम है: Pi चल सकता है, जबकि concentrator को बिजली न मिले। सिग्नल पिन में 5 V न दें और यह न मानें कि बिजली के दोनों इनपुट एक-दूसरे से अलग हैं।

**SPI और USB मॉड्यूल प्रकारों के लिए होस्ट कनेक्शन अलग हैं।** Seeed के WM1302 दस्तावेज़ SPI मॉडल के लिए सीधा SPI और USB मॉडल के लिए STM32L4 USB ब्रिज बताते हैं। mini-PCIe आकार मॉड्यूल का रूप बताता है, जबकि दस्तावेज़ित विद्युत इंटरफ़ेस SPI या USB हैं। लैपटॉप सॉकेट में आकार मिलना संगतता का पर्याप्त प्रमाण नहीं है। [Seeed के WM1302 दस्तावेज़](https://github.com/seeed-lora/WM1302-doc)

असेंबली को बिजली देने से पहले मॉड्यूल लगाएँ और उपयुक्त एंटीना जोड़ें, बिजली बंद रखें। RF हार्डवेयर, एंटीना और क्षेत्रीय योजना का मेल करें। कॉन्फ़िगरेशन फ़ाइल का नाम बदलने से RF पुर्जे नहीं बदलते, और M1 बिजली सॉकेट USB concentrator प्रकार का समर्थन साबित नहीं करता।

{{< figure src="m1-power-spi-system-diagram.webp" alt="बिजली, SPI, GPIO और I2C बस से Raspberry Pi 4 को M1 शील्ड से जोड़ने वाला ब्लॉक डायग्राम" caption="Clockwork Bird के मूल लेख में पुनः प्रकाशित SenseCAP निर्माता डायग्राम, WM1302 डिज़ाइन दिखाता है" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## पिनआउट ध्यान से पढ़ें

**BCM GPIO नंबर और भौतिक हेडर पिन को अलग-अलग कॉलम में लिखें।** उदाहरण के लिए, BCM GPIO17 Pi हेडर के भौतिक पिन 11 पर है। मॉड्यूल का edge connector तीसरी नंबरिंग प्रणाली जोड़ता है, इसलिए उसका reset pin नंबर Raspberry Pi GPIO नंबर नहीं है।

नीचे दी गई तालिका Clockwork Bird की चिह्नित हेडर छवि के कनेक्शन लिखती है। यह **समुदाय संदर्भ** है, निर्माता का पूरा स्कीमैटिक या हर M1 संशोधन का माप नहीं। चित्र में `SX1262` लेबल हैं, जबकि Semtech की सामान्य reset स्क्रिप्ट `SX1261` नाम उपयोग करती है।

| चित्र का सिग्नल | BCM / भौतिक पिन | अर्थ |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | साझा प्रबंधन बस |
| **SX1302 reset** | GPIO17 / 11 | concentrator reset का उम्मीदवार |
| **उपयोगकर्ता LED** | GPIO22 / 15 | M1 चिह्न |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | SPI डेटा सिग्नल |
| **SPI clock** | GPIO11 / 23 | SPI clock सिग्नल |
| **SX1302 chip select** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262 reset** | GPIO5 / 29 | सहायक रेडियो reset का उम्मीदवार |
| **SX1262 chip select** | GPIO6 / 31 | GPIO6, SPI0 CE1 से अलग |
| **SX1262 BUSY** | GPIO18 / 12 | सहायक रेडियो स्थिति आउटपुट |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | उपयोग से पहले जाँचने वाले सहायक सिग्नल |

काटे गए GPS/UART चिह्न M1 में GPS होने का प्रमाण नहीं हैं। अपने हार्डवेयर में GPS न हो तो उससे जुड़े सेटअप न जोड़ें। प्रकाशित चित्र उपयोगकर्ता बटन और पंखे के नियंत्रण को भी स्पष्ट नहीं करता। [Clockwork Bird की pinout पड़ताल](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="चिह्नित Raspberry Pi हेडर चित्र, M1 LED, concentrator reset, SPI सिग्नल और काटे गए GPS कनेक्शन दिखाता है" caption="संशोधन कवरेज अधूरा रखने वाला समुदाय-चिह्नित संदर्भ, पूरा M1 स्कीमैटिक नहीं" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Reset स्क्रिप्ट के टकराव सुलझाएँ

**Reset स्क्रिप्ट विद्युत आउटपुट चुनती है, सिर्फ सॉफ़्टवेयर प्राथमिकता नहीं।** Semtech की upstream `reset_lgw.sh` CoreCell reference design के लिए है। इसमें concentrator reset पर GPIO23, power enable पर GPIO18, सहायक reset पर GPIO22 और AD5338R reset पर GPIO13 शामिल हैं। [Semtech reset स्क्रिप्ट स्रोत](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Seeed के पुराने सेटअप निर्देश दो reset असाइनमेंट GPIO17 और GPIO5 करते हैं, लेकिन reference design की अन्य प्रविष्टियाँ रखते हैं। उदाहरण अपनाने से पहले उन मानों को चिह्नित M1 चित्र से मिलाएँ। [Seeed WM1302 सेटअप निर्देश](https://github.com/seeed-lora/WM1302-doc)

| असाइनमेंट | विरोधी प्रमाण | आवश्यक निर्णय |
|---|---|---|
| **GPIO22 सहायक reset के रूप में** | M1 चित्र इसे उपयोगकर्ता LED बताता है | LED चालू करने से पहले यह धारणा हटाएँ |
| **GPIO18 power enable के रूप में** | M1 चित्र इसे सहायक BUSY बताता है | चलाने से पहले net और दिशा जाँचें |
| **GPIO13 DAC reset के रूप में** | सामान्य स्क्रिप्ट दूसरे reference design का नाम देती है | तय करें कि सर्किट मौजूद है या नहीं |
| **सहायक SPI डिवाइस** | M1 चित्र CE1 के बदले GPIO6 चुनता है | chip-select रूटिंग और ड्राइवर समर्थन की पुष्टि करें |

**अनुमान:** यदि चित्र के अनुसार GPIO18 सहायक रेडियो आउटपुट से जुड़ा है, तो Pi की ओर उसे आउटपुट बनाना विद्युत संघर्ष का जोखिम पैदा करता है। यह अंतर जाँच की जरूरत बताता है, नुकसान या सभी M1 की एक जैसी वायरिंग साबित नहीं करता।

सारी बिजली काटकर हेडर और मॉड्यूल कनेक्टर के बीच दिखने वाले कनेक्शन खोजें। बोर्ड संशोधन और दोनों छोर दर्ज करें। निरंतरता जाँच कनेक्शन साबित करती है; सिग्नल की दिशा और विद्युत सीमा के लिए पुर्जे के दस्तावेज़ देखें।

मॉड्यूल का नीचे दिया चित्र उपयोग करके edge connector के पिन और Pi हेडर पिन में भ्रम न करें। सहायक रेडियो के लेबल प्रकाशित मॉड्यूल संदर्भ बताते हैं, हर संशोधन में समान चिप या सुविधा साबित नहीं करते। [Seeed WM1302 मॉड्यूल pinout](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="WM1302 मॉड्यूल edge connector के दोनों ओर बिजली, SPI, I2C और सहायक रेडियो सिग्नल दिखाता Seeed चित्र" caption="मॉड्यूल edge connector की नंबरिंग Raspberry Pi हेडर से अलग है" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Raspberry Pi OS तैयार करें

अतिरिक्त इंस्टॉलेशन पर होस्ट वातावरण दर्ज करें:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

OS रिलीज़, kernel और Pi मॉडल दोहराने योग्य आधार हैं। पुराने ट्यूटोरियल से तुलना से पहले इन्हें दर्ज करें।

निरीक्षण और build टूल इंस्टॉल करें:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

**Interface Options** में SPI और I2C चालू करके reboot करें। SPI concentrator मार्ग के लिए है; I2C आगे बताए प्रबंधन डिवाइसों के लिए। किसी दूसरे HAT ट्यूटोरियल से असंबंधित GPS serial-port बदलाव न लें।

खुले इंटरफ़ेस देखें:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

ये कमांड डिवाइस नोड, एडैप्टर, GPIO कंट्रोलर, लाइन और इंस्टॉल GPIO टूल संस्करण दिखाते हैं। **`i2cdetect -l` पता स्कैन किए बिना एडैप्टर सूची देता है।** `/dev/spidev0.0` फ़ाइल SPI इंटरफ़ेस खुला होने का प्रमाण है, चालू concentrator से संचार का नहीं। [i2c-tools मैनुअल](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Raspberry Pi GPIO मार्गदर्शन](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### GPIO संस्करणों का ध्यान रखें

**दूसरी मशीन के global GPIO नंबर न कॉपी करें।** पुराने स्क्रिप्ट `/sys/class/gpio` में लिखते हैं, जिसे kernel दस्तावेज़ अप्रचलित कहते हैं। नए user-space इंटीग्रेशन सही कंट्रोलर और line offset के साथ GPIO character-device इंटरफ़ेस उपयोग करें। [Linux GPIO दस्तावेज़](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

स्क्रिप्ट बदलने से पहले `gpioset --help` भी देखें। संस्करण 1 और 2 में syntax व process व्यवहार अलग हैं। मौजूदा टूल माँगी गई लाइनें डिफ़ॉल्ट रूप से थामता है, पर portable अनुबंध process समाप्त होने के बाद स्थिति की गारंटी नहीं देता। [libgpiod gpioset दस्तावेज़](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi अपने kernel में आउटपुट बने रहने के व्यवहार और उसे बदलने के विकल्प दर्ज करता है। हर Linux प्रणाली के एक जैसा चलने का अनुमान न लगाएँ, असली kernel कॉन्फ़िगरेशन लिखें। नई numbering या GPIO टूल गलत विद्युत मैपिंग ठीक नहीं करता। [Raspberry Pi GPIO उपयोग गाइड](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## उपयोगकर्ता LED जाँचें

GPIO22 LED से जुड़ा है और विरोधी GPIO उपयोगकर्ता हटाए गए हैं, यह पक्का करने के बाद boot config संपादित करें:

```bash
sudoedit /boot/firmware/config.txt
```

नए Raspberry Pi OS में boot कॉन्फ़िगरेशन **`/boot/firmware/config.txt`** पर है। पुराने इमेज `/boot/config.txt` उपयोग करते हैं, जो 2023 लेख का पथ है। संपादन से पहले सक्रिय फ़ाइल का बैकअप लें। [Raspberry Pi config.txt दस्तावेज़](https://www.raspberrypi.com/documentation/computers/config_txt.html)

अपने Pi पर लागू सेक्शन, जैसे `[all]`, में LED overlay जोड़ें:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

**`gpio`** पैरामीटर BCM नंबरिंग लेता है। **`label`** Linux LED डिवाइस का नाम है; **`trigger=heartbeat`** kernel heartbeat trigger चुनता है। Clockwork Bird M1 के लिए यह असाइनमेंट बताता है और Raspberry Pi overlay संदर्भ इन पैरामीटर को दर्ज करता है। [मूल LED अवलोकन](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [gpio-led overlay संदर्भ](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Reboot के बाद पंजीकृत LED देखें:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

अपेक्षित नतीजा `lorawan` LED एंट्री है जिसमें `heartbeat` चौकोर कोष्ठक में चुना हो। LED का चमकना GPIO/ड्राइवर मार्ग दिखाता है। इससे LoRaWAN पंजीकरण, रेडियो प्राप्ति या Helium स्थिति नहीं पता चलती।

## I2C डिवाइस जाँचें

**I2C पता संकेत है, डिवाइस पहचान नहीं।** Clockwork Bird ने `0x60` और `0x39` पर प्रतिक्रिया देखी, फिर क्रिप्टो लाइब्रेरी से ATECC608 जानकारी पढ़ी। मूल लेख में तापमान सेंसर की पहचान अस्थायी थी।

पिछले सेक्शन की एडैप्टर सूची से शुरू करें। व्यापक `i2cdetect` स्कैन निष्क्रिय निरीक्षण नहीं, probe लेनदेन भेजते हैं। upstream मैनुअल व्यवधान की चेतावनी देता है। चल रहे गेटवे या अज्ञात जुड़े डिवाइस को नियमित रूप से स्कैन न करें। [i2c-tools probe व्यवहार](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| अवलोकन | समर्थित निष्कर्ष | अनसुलझा प्रश्न |
|---|---|---|
| **`0x60` पर प्रतिक्रिया** | किसी डिवाइस ने probe स्वीकारा | क्या यह अपेक्षित सिक्योर एलिमेंट है? |
| **`0x39` पर प्रतिक्रिया** | किसी डिवाइस ने probe स्वीकारा | किस घटक और संशोधन ने जवाब दिया? |
| **स्कैन में `UU`** | ड्राइवर पता इस्तेमाल करता है, इसलिए probe छोड़ा गया | किस ड्राइवर के पास यह है? |
| **कोई प्रतिक्रिया नहीं** | probe को पुष्टि नहीं मिली | बिजली, बस, मालिकाना हक या डिवाइस प्रोटोकॉल? |

### तापमान सेंसर की संभावना मजबूत करें

**STTS751, `0x39` का स्रोत-समर्थित उम्मीदवार है।** Semtech तापमान ड्राइवर हेडर स्पष्ट रूप से `0x39` को `STTS751-0DP3F` से जोड़ता है। इससे मूल परिकल्पना मजबूत होती है, पर इस पते पर मौजूद सभी बोर्डों की पहचान नहीं होती। [Semtech STTS751 ड्राइवर हेडर](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

संगत घटक पहचानने और कोई अन्य प्रक्रिया उसका उपयोग नहीं कर रही यह सुनिश्चित करने के बाद पहचान रजिस्टर पढ़ें:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

यहाँ **`1`** सत्यापित bus चुनता है, **`0x39`** डिवाइस और **`b`** SMBus byte-data रीड। STTS751-0 के लिए दस्तावेज़ित product ID `0xFD` पर `0x00` और manufacturer ID `0xFE` पर `0x53` है। ये लेनदेन रजिस्टर पते चुनते हैं, कॉन्फ़िगरेशन नहीं लिखते। [STTS751 डेटाशीट, रजिस्टर मैप और पहचान रजिस्टर](https://www.st.com/resource/en/datasheet/stts751.pdf)

रीडिंग को चिप मार्किंग और दस्तावेज़ से मिलाएँ। दोनों मान मेल खाएँ तो पहचान का प्रमाण बढ़ता है; त्रुटि पर हार्डवेयर बदलने से पहले bus और उसके उपयोगकर्ता जाँचें। सेंसर स्थानीय तापमान मापता है, Pi CPU का तापमान नहीं।

## सिक्योर एलिमेंट देखें

**ATECC608 अलग authentication घटक है।** इसकी कॉन्फ़िगरेशन, सीरियल नंबर, public key और सुरक्षित key सामग्री अलग अवधारणाएँ हैं। Public key पढ़ने से संबंधित private key नहीं खुलती।

Microchip की **CryptoAuthLib** डिवाइस इंटरफ़ेस देती है। **cryptoauthtools** रिपॉज़िटरी में इस लाइब्रेरी पर आधारित उदाहरण हैं। उदाहरण चलाने से पहले परियोजना निर्देशों के अनुसार लक्ष्य प्रणाली में native library और Python bindings तैयार करें। असंबंधित Python पैकेज लगाना या एक स्क्रिप्ट कॉपी करना I2C backend चालू होने का प्रमाण नहीं है। [Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

तैयार `cryptoauthtools/python/examples` डायरेक्टरी से मूल लेख का जाँच कमांड चलाएँ:

```bash
sudo python3 info.py -i i2c
```

**`-i i2c`** तर्क इंटरफ़ेस चुनता है। Virtual environment में उसका स्पष्ट Python इंटरप्रेटर चलाएँ और सुनिश्चित करें कि वही native library पा रहा है। कई इंस्टॉलेशन में `sudo python3` system interpreter चुनता है, जिससे module import विफल होता है।

समीक्षित `info.py` संशोधन जानकारी, सीरियल नंबर, कॉन्फ़िगरेशन और lock स्थिति पढ़ता है। Data zone locked हो तो slot 0 की public key पाने की कोशिश करता है। यह उदाहरण की provisioning प्रक्रिया नहीं चलाता। केवल slot-0 public-key पढ़ने में विफलता डिवाइस खराब होने का प्रमाण नहीं है। [Microchip info.py स्रोत](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| आउटपुट या काम | अर्थ |
|---|---|
| **Configuration locked** | कॉन्फ़िगरेशन पर रोक लागू है |
| **Data zone locked** | configured slot policy के अनुसार पहुँच समझें |
| **Public key दिखाई** | public जानकारी मिली, private key export नहीं हुई |
| **`config.py` चलाना** | configuration, lock और key generation वाला provisioning उदाहरण |

**जाँच त्रुटि सुधारने के लिए `config.py` न चलाएँ।** इसके स्रोत में configuration लिखना, zone lock करना और key generation कॉल शामिल हैं। पहले से configured डिवाइस पर डिफ़ॉल्ट key-generation मार्ग भी मायने रखता है। [Microchip config.py स्रोत](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Microchip की provisioning profiles बताती हैं कि data zone lock होने का अर्थ हर slot की समान पहुँच नहीं है। वे M1 की सटीक configuration नहीं बतातीं। मौजूदा configuration रखें और key reuse की योजना से पहले संबंधित पार्ट दस्तावेज़ देखें। [Microchip memory और slot access नीति](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## पंखे और बटन के अज्ञात हिस्से जाँचें

**तीन-पिन फैन सॉकेट उसके वोल्टेज, polarity या नियंत्रण विधि की पुष्टि नहीं करता।** पिन नंबर की तस्वीर लें और फैन लेबल पढ़ें। बदलने वाला फैन लगाने या GPIO overlay चुनने से पहले बिजली व नियंत्रण कनेक्शन तय करें।

मूल पड़ताल बटन GPIO भी नहीं बताती। अपने बोर्ड संशोधन से जुड़ा ड्राइवर या कॉन्फ़िगरेशन खोजें, फिर बिजली हटाकर कनेक्टिविटी जाँचें। बटन खोजने के लिए सभी खाली दिखते GPIO output न बनाएँ।

| पेरिफ़रल | जुटाने का प्रमाण | स्वीकृति शर्त |
|---|---|---|
| **फैन बिजली** | फैन रेटिंग, कनेक्टर का ground और supply | मापी supply फैन विनिर्देश से मेल खाती है |
| **फैन नियंत्रण** | ड्राइवर/config या trace किया नियंत्रण सर्किट | शुरुआत और अधिक तापमान पर व्यवहार तय है |
| **उपयोगकर्ता बटन** | contact wiring, GPIO map, input polarity | जानबूझकर एक बार दबाने पर अपेक्षित event आता है |

नई OS स्थापना मूल उपकरण की cooling नीति अपने आप वापस नहीं लाती। पहले लंबे परीक्षण में फैन और तापमान साथ देखें। केस का airflow बनाए रखें और जरूरी cooling न मिले तो परीक्षण रोकें।

## गेटवे स्टैक चुनें

**बोर्ड समर्थन और सर्वर प्रोटोकॉल अलग रखें।** अनुकूल LoRaWAN सर्वर गलत reset routine या RF calibration ठीक नहीं करता। पहले ऐसा सॉफ़्टवेयर चुनें जो concentrator, carrier wiring, OS और क्षेत्रीय configuration का समर्थन करे।

| सॉफ़्टवेयर मार्ग | उपयोग | तैनाती से पहले जाँच |
|---|---|---|
| **Semtech SX1302 HAL** | स्रोत स्तर पर शुरुआत और diagnostic टूल | बोर्ड reset routine और मॉड्यूल config |
| **LoRa Basics Station** | सर्वर से प्रमाणित गेटवे कनेक्शन | कार्यशील बोर्ड integration और सर्वर credentials |
| **ChirpStack Concentratord** | अलग concentrator सेवा | समर्थित मॉडल, calibration और GPIO map |

ChirpStack SPI **`seeed_wm1302`** मॉडल सूचीबद्ध करता है। यह मॉड्यूल समर्थन का प्रमाण है, पूरी M1 इमेज या हर M1 संशोधन के समर्थन का वादा नहीं। अलग SenseCAP M2 स्थापना निर्देश M1 firmware निर्देश नहीं हैं। [ChirpStack हार्डवेयर समर्थन](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [ChirpStack Seeed इंस्टॉल लक्ष्य](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

The Things Stack दस्तावेज़ पुराने Semtech UDP forwarder के बजाय **LoRa Basics Station** सुझाते हैं। Station TLS और token authentication के साथ केंद्रीकृत configuration देता है। UDP उदाहरण पैकेट forwarding समझने में उपयोगी हैं, पर server address सेटिंग से वे सुरक्षा नहीं मिलती। [The Things Stack UDP मार्गदर्शन](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station दस्तावेज़](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Upstream टूल तैयार करें

लक्ष्य Pi पर नई working directory में build करें:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Build output के साथ commit पहचान सहेजें। सफल build compiler संगतता बताता है, पर रेडियो के लिए सत्यापित reset implementation और सही config भी चाहिए। Semtech दस्तावेज़ HAL और सहायक प्रोग्राम की भूमिका बताते हैं। [SX1302 HAL build और टूल दस्तावेज़](https://github.com/Lora-net/sx1302_hal)

हार्डवेयर एक्सेस टूल चलाने से पहले reset फ़ाइल देखें:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

यह फ़ाइल बिना बदलाव runtime directory में कॉपी न करें। Semtech के हार्डवेयर एक्सेस प्रोग्राम, पहचान टूल सहित, reset script अपने आप इस्तेमाल कर सकते हैं। समीक्षा में हर assigned pin, signal direction, GPIO API और startup/shutdown स्थिति शामिल हो।

बोर्ड सत्यापन के बाद चुने हुए स्टैक के निर्देशों से concentrator EUI पढ़ें और गेटवे पंजीकृत करें। सर्वर configuration जोड़ते समय मॉड्यूल calibration और RF settings रखें। Semtech UDP में `gateway_ID` EUI है; The Things Stack console का Gateway ID पंजीकरण के लिए मानव-पठनीय पहचान है। [The Things Stack गेटवे config](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## सेंसर डिलीवरी साबित करें

**पहली विफल परत खोजने के लिए चरणबद्ध प्रमाण लें।** गेटवे का online दिखना सर्वर कनेक्शन साबित करता है। स्वीकृति परीक्षण में जाना-पहचाना सेंसर, मेल खाता frequency plan और decoded application payload भी चाहिए।

यह क्रम प्रस्तावित परीक्षण योजना है, M1 पर मापे परिणाम नहीं:

| जाँच बिंदु | सहेजने का प्रमाण | अर्थ |
|---|---|---|
| **होस्ट तैयार** | OS, kernel, power और interface सूची | Linux तैयारी पूरी |
| **Concentrator जवाब देता है** | EUI और सफल initialization log | होस्ट-concentrator संचार काम करता है |
| **रेडियो प्राप्त करता है** | अपेक्षित sensor packet और reception metadata | configured receive path काम करता है |
| **सर्वर स्वीकारता है** | सेंसर से जुड़ी gateway घटना | forwarding और server routing काम करते हैं |
| **ऐप्लिकेशन decode** | अपेक्षित माप और timestamp | application path काम करता है |
| **reboot रिकवरी** | restart के बाद वही जाँच | startup config दोहराई जा सकती है |

**OTAA** सेंसर के लिए activation exchange और अगला uplink भी जाँचें। OTAA का अर्थ over-the-air activation है, session स्थापित करने की join प्रक्रिया। Join अनुरोध मिलना सफल join या downlink मार्ग साबित नहीं करता। [The Things Stack activation दस्तावेज़](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**निदान उदाहरण:** गेटवे सर्वर से जुड़ता है और EUI बताता है, पर सेंसर नहीं दिखता। सेंसर transmission config, चुने receive channels, antenna path और radio logs पहले देखें। इस स्थिति में ATECC608 को फिर प्रोग्राम करने से गायब प्रमाण नहीं मिलेगा।

**दूसरा निदान:** सेंसर पैकेट स्थानीय रूप से दिखता है पर ऐप तक नहीं पहुँचता। पैकेट समय को gateway और server घटनाओं से मिलाएँ, फिर routing, device registration और decoding देखें। Server के घटना स्वीकारने से पहले log में RF packet होना payload decoder को दोष देने के लिए पर्याप्त नहीं।

## लक्षण के अनुसार समस्या समाधान

| लक्षण | पहले जाँचें | अगला कदम |
|---|---|---|
| **SPI डिवाइस फ़ाइल नहीं** | सक्रिय boot config और interface सेटिंग | अपेक्षित इंटरफ़ेस सक्षम कर reboot |
| **SPI है, रेडियो विफल** | बिजली, बैठना, reset क्रम और chip select | server बदलाव से पहले विद्युत मार्ग जाँचें |
| **GPIO export त्रुटि** | पुराने sysfs अनुमान और स्थापित kernel | GPIO API के लिए समीक्षा किया implementation लें |
| **GPIO पहले से उपयोग में** | `gpioinfo` में consumer | फिर प्रयास से पहले मालिकाना हल करें |
| **सेटअप के बाद LED विफल** | overlay लागू होना और GPIO22 टकराव | पंजीकृत LED डिवाइस व reset script देखें |
| **I2C डिवाइस गायब** | bus संख्या, power और मौजूदा उपयोग | बार-बार व्यापक स्कैन किए बिना जाँचें |
| **क्रिप्टो लाइब्रेरी import विफल** | interpreter, bindings, native library path | software environment ठीक करें |
| **Public-key पढ़ना विफल** | slot policy और पहले सफल reads | provisioning किए बिना config देखें |
| **फैन नहीं चलता** | सत्यापित supply और cooling नियंत्रण | लंबे परीक्षण से पहले cooling बहाल करें |
| **Uplink आते हैं, join विफल** | downlink path और क्षेत्रीय/device settings | join उत्तर और receive windows का पता लगाएँ |

हर सुधार को एक प्रयोग मानें। पुराना config सहेजें, एक बार में एक variable बदलें, वही जाँच दोहराएँ और अपेक्षित प्रमाण मिला या नहीं दर्ज करें।

## हार्डवेयर रिकॉर्ड बनाएँ

जाँच को दोहराए जा सकने वाले handover में बदलने के लिए यह टेम्पलेट लें:

```text
कैरियर संशोधन और तस्वीरें:
Concentrator मॉडल, इंटरफ़ेस और RF बैंड:
होस्ट मॉडल / OS / kernel / GPIO टूल संस्करण:
बिजली / एंटीना / cooling व्यवस्था:
सत्यापित pin map और प्रमाण:
अनसुलझे net और हटाई गई सुविधाएँ:
सॉफ़्टवेयर repository और commit:
Reset कार्यान्वयन और GPIO मालिकाना:
Gateway EUI / सर्वर / frequency plan:
सेंसर activation और decoded uplink प्रमाण:
Reboot recovery परिणाम:
मूल कार्ड का स्थान और rollback प्रक्रिया:
```

**निर्णय अभ्यास:** आपके पास बिना मॉड्यूल लेबल का सस्ता bare carrier और पढ़ने योग्य लेबल व दस्तावेज़ित संचालन वाला महँगा असेंबली है। बाकी Pi, concentrator, antenna, supply और verification समय जोड़कर अपने प्रोजेक्ट के लिए एक चुनें। सही विकल्प कुल लागत और आपकी सेवा के प्रमाण पर निर्भर है, सिर्फ carrier की लिखी कीमत पर नहीं।

**अपेक्षित विचार:** सीखने का प्रोजेक्ट अनसुलझी wiring सह सकता है, यदि आपके पास मापने के औज़ार और समय हों। चालू सेंसर के लिए गेटवे को दोहराने योग्य startup, cooling, software support और साबित delivery चाहिए। कौन सी अनसुलझी शर्त deployment रोकेगी, लिखें।

## अगले कदम

पहले हार्डवेयर रिकॉर्ड पूरा करें और reset script की विसंगतियाँ सुलझाएँ। फिर एक जाना-पहचाना सेंसर चालू करके application decoding तक प्रमाण रखें, उसके बाद और डिवाइस जोड़ें।

**स्वीकृति रिकॉर्ड:** बोर्ड संशोधन, मॉड्यूल लेबल, रेडियो बैंड, बिजली माप, सक्रिय SPI डिवाइस, GPIO line नाम, reset क्रम, concentrator log, server connection और एक decoded uplink सहेजें। हर मान को observed, documented या अभी अनुमान के रूप में चिह्नित करें। किसी process के शुरू होने को RF प्रदर्शन या application delivery का प्रमाण न मानें।

यदि आपका लक्ष्य mesh messaging है, तो पहले हमारी [Meshtastic, MeshCore और Reticulum तुलना गाइड](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/) में protocol भूमिकाएँ देखें। LoRa रेडियो तकनीक साझा करने से firmware संगतता साबित नहीं होती। Messaging deployment के लिए [MeshtasticD समर्थित हार्डवेयर दस्तावेज़](https://meshtastic.org/docs/meshtasticd/) देखें, इस LoRaWAN प्रक्रिया को Meshtastic रूपांतरण न समझें।

## स्रोत और चित्र श्रेय

शोध जाँच: 12 सितंबर 2026। बिना तारीख के दस्तावेज़ और repository लिंक इस लेख के लिए जाँचे गए संस्करण हैं। स्थानीय चित्र मूल लेबल और श्रेय रखते हैं।

| प्रकाशक | स्रोत और तारीख |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03। बोर्ड तस्वीर, चिह्नित हेडर और पुनः प्रकाशित निर्माता ब्लॉक डायग्राम |
| **Seeed Studio / SenseCAP** | [M1 परिचय व विनिर्देश](https://www.sensecapmx.com/docs/sensecap-m1/overview/), तारीख नहीं। मूल ब्लॉक डायग्राम का श्रेय |
| **Seeed Studio** | [WM1302 दस्तावेज़ और मॉड्यूल पिनआउट](https://github.com/seeed-lora/WM1302-doc), repository |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), लिंक किए reset script व temperature driver स्रोत सहित |
| **Raspberry Pi** | [Boot config](https://www.raspberrypi.com/documentation/computers/config_txt.html), [GPIO उपयोग गाइड](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) और [overlay संदर्भ](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [अप्रचलित GPIO sysfs इंटरफ़ेस](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) और [gpioset मैनुअल](https://libgpiod.readthedocs.io/en/master/gpioset.html), बाद वाला अगस्त 2026 का |
| **i2c-tools** | [i2cdetect मैनुअल](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), v4.3 स्रोत |
| **STMicroelectronics** | [STTS751 डेटाशीट](https://www.st.com/resource/en/datasheet/stts751.pdf), संशोधन 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools), और [slot-access नीति दस्तावेज़](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Concentratord हार्डवेयर समर्थन](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) और [Seeed इंस्टॉल लक्ष्य](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDP forwarder](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) और [device activation](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticD दस्तावेज़](https://meshtastic.org/docs/meshtasticd/), तारीख नहीं |
