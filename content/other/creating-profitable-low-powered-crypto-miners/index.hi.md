---
title: "लो-पावर्ड हार्डवेयर के साथ एक लाभदायक पैसिव इनकम बॉक्स बनाएं: एक गाइड"
draft: false
toc: true
date: 2023-02-07
description: "रास्पबेरी पाई या इंटेल एनयूसी का उपयोग करके कम-शक्ति वाली निष्क्रिय आय क्रिप्टो माइनर स्थापित करना सीखें, और इस गाइड के साथ प्रति बॉक्स $10-$20 प्रति माह कमाएं"
tags: ["एक लाभदायक निष्क्रिय आय बॉक्स बनाएँ", "कम शक्ति वाला हार्डवेयर", "निष्क्रिय आय", "क्रिप्टो माइनर", "रास्पबेरी पाई", "इंटेल एनयूसी", "मार्गदर्शक", "हार्डवेयर आवश्यकताएँ", "ओएस स्थापना", "सॉफ्टवेयर स्थापना", "डाक में काम करनेवाला मज़दूर", "स्वचालित डॉकर कंटेनर अपडेट", "उबंटू सर्वर", "उबंटू डेस्कटॉप", "Raspbian", "बजट", "यूएसएफएफ", "छोटा", "छोटा", "माइक्रो पीसी", "तकनीकी अनुभव", "अर्नऐप", "मिस्ट", "पीर2प्रोफिट", "हनीगैन", "ट्रैफमॉनीटाइज़र", "पहरे की मिनार", "बिटिंग", "लिनक्स अद्यतन", "उबंटू", "डेबियन", "Centos", "आरएचईएल", "ऑफ़लाइन अद्यतन", "स्थानीय भंडार", "कैश", "सर्वर सेटअप", "क्लाइंट सेटअप", "apt-दर्पण", "demirror", "createrepo", "apt-cacher-एनजी", "यम-क्रोन", "लिनक्स सिस्टम अपडेट", "ऑफ़लाइन पैकेज अद्यतन", "ऑफ़लाइन सॉफ़्टवेयर अद्यतन", "स्थानीय पैकेज भंडार", "स्थानीय पैकेज कैश", "ऑफ़लाइन लिनक्स अद्यतन", "ऑफ़लाइन अद्यतनों को संभालना", "ऑफ़लाइन अद्यतन तरीके", "ऑफ़लाइन सिस्टम रखरखाव", "लिनक्स सर्वर अपडेट", "लिनक्स क्लाइंट अपडेट", "ऑफ़लाइन सॉफ्टवेयर प्रबंधन", "ऑफ़लाइन पैकेज प्रबंधन", "अद्यतन रणनीतियों", "लिनक्स सुरक्षा अद्यतन"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "एक हरा, सर्किट बोर्ड एक बॉक्स के आकार का होता है जिसमें इंटरनेट कनेक्टिविटी के प्रतीक होते हैं जैसे कि तार जुड़े होते हैं।"
coverCaption: ""
---

** कम शक्ति वाले हार्डवेयर के साथ एक लाभदायक निष्क्रिय आय बॉक्स बनाएं: एक गाइड**
इन दिनों बहुत से लोग क्रिप्टो माइनिंग और हीलियम माइनर्स जैसे लो पावर माइनर्स में हैं। ये महान और सभी हैं लेकिन वे अब और अधिक नहीं कमाते हैं और वे एक तरह की कमाई पर केंद्रित हैं। आज हम एक कम शक्ति वाला पैसिव इनकम बॉक्स बनाने जा रहे हैं जो $10-$20 प्रति माह प्रति बॉक्स और आवासीय आईपी से कहीं भी कमाता है।

*यदि आपके पास अतिथि नेटवर्क पर इस बॉक्स को स्थापित करने की क्षमता है या इससे भी बेहतर, एक अलग वीएलएएन है, तो ऐसा करें। जबकि यह एक सुरक्षा ब्लॉग है, हम हर किसी की सुरक्षा चिंताओं और जोखिम सहनशीलता को नहीं मान सकते।*

## हार्डवेयर आवश्यकताएँ:
निम्न में से एक आवश्यक है। हमें मूल रूप से किसी भी कुशल और कम शक्ति वाले कंप्यूटर की आवश्यकता होती है जिस पर हम अपना हाथ रख सकते हैं। कोई भी Raspberry PI, Intel NUC, या ऐसा ही करेगा। उन्हें इतना शक्तिशाली होने की जरूरत नहीं है। हालाँकि मैं आपको सलाह दूंगा कि आपके पास कम से कम 32g-64g स्टोरेज, 4g RAM और कम से कम 2 cpu थ्रेड्स हों। इसके लिए हम हार्डवेयर के लिए लगभग $100-$200 के बजट को लक्षित कर रहे हैं, लेकिन यदि यह आपकी आवश्यकताओं के अनुरूप है तो इसे और अधिक करने के लिए स्वतंत्र महसूस करें। हमारा शक्ति लक्ष्य लगभग है। 25w औसत।
### रास्पबेरी पाई:
इन दिनों को पकड़ना मुश्किल है लेकिन वे बहुत कम शक्ति वाले हैं और काफी अनुकूलन योग्य हैं। अपने रास्पबेरी पीआई पर रास्पियन कैसे स्थापित करें, इस बारे में जानकारी के लिए
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### इंटेल न्यूक:
वहाँ मॉडल की विस्तृत विविधता। एक नया चुनने के लिए स्वतंत्र महसूस करें।
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### कोई USFF/छोटा/मिनी/माइक्रो पीसी:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### इंटेल N5100 या समान के साथ कोई भी मिनी पीसी
सुपर लो पावर रास्पबेरी पाई समकक्ष के लिए लेकिन x64 प्लेटफॉर्म पर।
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## ओएस स्थापना:
हम यहां ऑपरेटिंग सिस्टम कैसे स्थापित करें, इसके तकनीकी विवरण में नहीं जाएंगे। हालाँकि यहाँ आपको आरंभ करने के लिए कुछ बेहतरीन संसाधन दिए गए हैं
### रास्पियन:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### उबंटू:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## सॉफ्टवेयर स्थापना:
यह एक लंबा खंड होने जा रहा है। हम डॉकर सेट अप करने जा रहे हैं और फिर डॉकर के माध्यम से हम स्वचालित डॉकर कंटेनर अपडेट सेट अप करेंगे और एकाधिक डॉकर कंटेनर इंस्टॉल करेंगे। हम यह भी मानते हैं कि आप ubuntu सर्वर का उपयोग कर रहे हैं, हालाँकि ubuntu सर्वर, ubuntu डेस्कटॉप और रास्पियन के लिए कमांड समान होने चाहिए।

*इस खंड के लिए हम कुछ बुनियादी तकनीकी अनुभव मानते हैं और यह कि आपने अपना ऑपरेटिंग सिस्टम पहले ही स्थापित कर लिया है और साथ ही यह भी जानते हैं कि टर्मिनल में कैसे जाना है।*

### अपडेट स्थापित कर रहा है:
हम पहले यह सुनिश्चित करना चाहते हैं कि हमारा सिस्टम पूरी तरह से अद्यतित है:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### डॉकटर स्थापित करना:
हमें किसी भी मौजूदा संस्करण को अनइंस्टॉल करने की आवश्यकता है जो ओएस के साथ पैक किया गया है और डॉकर के रेपो से नवीनतम को स्वयं स्थापित करें।
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### गुम्मट स्थापित करें:
यह डॉकटर कंटेनर स्वचालित रूप से आपके सभी डॉकटर कंटेनरों को नियमित अंतराल पर नवीनतम छवियों में अपडेट करता है और पुरानी (बासी) छवियों को साफ करता है।
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### बिटपिंग स्थापित करें:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

बिटपिंग आपको अपने नेटवर्क से हल्के नेटवर्क परीक्षण चलाने के लिए व्यवसायों के लिए एक नोड प्रदान करने के लिए सोलाना में भुगतान करने की क्षमता प्रदान करता है।
यह औसतन लगभग 0.1 सेंट प्रति दिन प्रति नोड है। मैं बहुत कुछ नहीं जानता, लेकिन इसमें क्षमता है और भुगतान आसान है।

#### खाता बनाएं:
पर अकाउंट बनाएं [bitping.com](https://bitping.com)

#### डॉकटर कंटेनर स्थापित करें:
चरण 1. इन आदेशों को पहले चलाएँ क्योंकि यह आपके कंटेनर की स्थापना के माध्यम से चलता है और आपको साइन इन करने के लिए कहता है।
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

अपने बिटिंग खाते से साइन इन करने के बाद कंटेनर से बचने के लिए अपने कीबोर्ड पर CTRL+C दबाएं।

चरण 2. कंटेनर को पृष्ठभूमि में बनाए रखने के लिए इस आदेश को चलाएँ
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### अर्न ऐप इंस्टॉल करें:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

अर्न ऐप आपको अपने इंटरनेट को वीपीएन सेवा के रूप में आश्चर्यजनक रूप से पुरस्कारों के लिए साझा करने देता है। औसतन लगभग $5 माह प्रति नोड प्रति आवासीय IP। पेपैल और अमेज़ॅन उपहार कार्ड के माध्यम से पेआउट प्रदान करता है।

#### अर्न एप अकाउंट बनाएं:
पर अकाउंट बनाएं [earnapp.com](https://earnapp.com/i/GCL9QzB5)
*चेतावनी, एक Google खाते की आवश्यकता है*

#### अपना UUID प्राप्त करने के लिए ऐप का गैर डॉकर संस्करण स्थापित करें:
अपना UUID प्राप्त करने के बाद स्थापना रद्द करना सुनिश्चित करें अन्यथा आप इसे एक ही होस्ट पर और स्वचालित अपडेट के बिना दो बार चलाएंगे
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### डॉकटर कंटेनर स्थापित करें:
अपने टर्मिनल में चिपकाने से पहले स्ट्रिंग को संशोधित करें। आपको अपना अर्न ऐप UUID निर्दिष्ट करना होगा।
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### वीडियो ट्यूटोरियल:
{{< youtube id="tt499o0OjGU" >}}

### हनी गेन स्थापित करें:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

हनी गेन आपको आश्चर्यजनक पुरस्कार के लिए अपने इंटरनेट को वीपीएन सेवा के रूप में साझा करने देता है। औसतन लगभग $5 माह प्रति नोड प्रति आवासीय IP। भुगतान जटिल हो सकता है। इस कंटेनर का उपयोग करने का निर्णय लेने से पहले इसे और पढ़ें

#### हनी गेन अकाउंट बनाएं:
पर अकाउंट बनाएं [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### डॉकटर कंटेनर स्थापित करें:
टर्मिनल में चिपकाने से पहले स्ट्रिंग को स्पष्ट ईमेल, पासवर्ड और डिवाइस नाम से संशोधित करें
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### रास्पबेरी पाई के लिए वैकल्पिक निर्देश
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### वीडियो ट्यूटोरियल:
{{< youtube id="Wd11M0nSy1k" >}}

### PawnsApp इंस्टॉल करें:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Pawns ऐप, यहां सूचीबद्ध अन्य लोगों के समान ही आपको अपना इंटरनेट साझा करने के लिए भुगतान करने की पेशकश करता है। न्यूनतम भुगतान $5 है। औसत भुगतान $0.50 प्रति माह प्रति नोड प्रति IP है।

#### एक PawnsApp अकाउंट बनाएं:
पर अकाउंट बनाएं [https://pawns.app](https://pawns.app/?r=2092882)

#### डॉकटर कंटेनर स्थापित करें:

अपने टर्मिनल पर कॉपी करने से पहले अपने ईमेल, पासवर्ड, डिवाइस का नाम और डिवाइस आईडी के साथ निम्नलिखित को संशोधित करें।
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```


### रिपॉकेट स्थापित करें:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

यहाँ अन्य प्रसाद के समान। न्यूनतम $20 भुगतान। भुगतान जटिल हो सकता है। यह देखने के लिए स्वयं शोध करें कि क्या आप इस सेवा का उपयोग करना चाहते हैं। भुगतान औसतन लगभग $1 प्रति नोड प्रति बॉक्स प्रति माह।

#### एक रिपॉकेट अकाउंट बनाएं:
पर अकाउंट बनाएं [repocket.co](https://link.repocket.co/raqc) और अपने डैशबोर्ड से अपनी एपीआई कुंजी लें।
#### डॉकटर कंटेनर स्थापित करें:
अपने टर्मिनल में चिपकाने से पहले अपने ईमेल और एपीआई कुंजी के साथ निम्न पंक्ति को संशोधित करें।
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### वीडियो ट्यूटोरियल:
{{< youtube id="171gWknfAbY" >}}

### ट्रैफ़ मोनेटाइज़र इंस्टॉल करें:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

EarnApp और HoneyGain के समान, TraffMonetizer आपको अपना इंटरनेट साझा करने के लिए भुगतान करता है। औसतन लगभग $2 प्रति माह प्रति नोड प्रति IP। केवल बीटीसी में भुगतान प्रदान करता है।

#### अपना ट्रैफ मुद्रीकरण खाता बनाएं:
पर अपना एकाउंट बनाएं [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
एक बार जब आप डैशबोर्ड में पहुंच जाते हैं, तो अपने एप्लिकेशन टोकन को नोट कर लें।

#### डॉकटर कंटेनर स्थापित करें:
निम्नलिखित स्ट्रिंग की प्रतिलिपि बनाएँ और अपने टोकन को अपने टर्मिनल में चिपकाने से पहले डैशबोर्ड से मिला हुआ संलग्न करें।

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### मिस्टीरियम स्थापित करें:
[Mysterium](https://www.mysterium.network/) एक विकेन्द्रीकृत वीपीएन और वेबस्क्रैपिंग सेवा है जो एथेरियम और पॉलीगॉन ब्लॉकचेन पर निर्मित है।
प्रति आईपी प्रति नोड कई कारकों के आधार पर भुगतान औसतन कहीं भी $1-$20 प्रति माह होता है। सक्रियण के लिए नोड सेटअप करने के लिए $1.XX खर्च होता है। MYST टोकन में भुगतान।


#### डॉकटर कंटेनर स्थापित करें:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### डॉकर कंटेनर सेटअप करें:
अपने नोड के आईपी पते के साथ "नोडीप" को बदलकर http://"nodeip"/#/dashboard पर जाएं। आप इसे टर्मिनल में "ifconfig" टाइप करके पा सकते हैं।

"स्टार्ट नोड सेटअप" पर क्लिक करें।

ERC20 वॉलेट का पता विगत करें जिसमें आप पुरस्कार प्राप्त करना चाहते हैं और "अगला" पर क्लिक करें। आप अपने मेटामास्क पतों में से एक जैसे मानक एथेरियम पते का उपयोग कर सकते हैं।

एक पासवर्ड टाइप करें जिसका उपयोग आप भविष्य में इस नोड डैशबोर्ड तक पहुँचने के लिए करेंगे। अपने नेटवर्क में नोड का दावा करने के लिए चेकबॉक्स को चेक करें।

"इसे यहां प्राप्त करें" लिंक पर क्लिक करें और अपनी एपीआई कुंजी खोजें। इसे कॉपी करें। वापस जाओ और इसे चिपकाओ। "सहेजें और जारी रखें" पर क्लिक करें।

#### अग्रेषण पोर्ट:
हम यह वर्णन नहीं कर सकते कि प्रत्येक व्यक्ति के विशिष्ट हार्डवेयर के लिए पोर्ट फ़ॉरवर्ड कैसे करें। आगे पोर्ट करने का तरीका जानने के लिए यहां कुछ संसाधन दिए गए हैं।
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### बूट पर डॉकटर कंटेनर को ऑटो रीस्टार्ट करें:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### वैकल्पिक कॉन्फ़िगरेशन:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### मैलवेयर और ट्रैकर्स को ब्लॉक करके सुरक्षा बढ़ाएं।
क्लाउडफ्लेयर मैलवेयर और ट्रैकिंग सुरक्षा डीएनएस के लिए सभी डीएनएस अनुरोधों को बाध्य करें।
साथ ही, DNS/HTTPS अनुरोधों को ब्लॉक करें।
*यदि आपके पास नेटवर्क पर अधिक उन्नत राउटर या फ़ायरवॉल है, तो आप ज्ञात खराब कार्य करने वाले IPs, टोर एक्सेस, टोरेंट, सामान्य रूप से p2p ट्रैफ़िक आदि को ब्लॉक करने के लिए अधिक उन्नत नियम बनाने के लिए स्नॉर्ट/सिक्योरिटा जैसे पैकेज का उपयोग कर सकते हैं। यह अत्यधिक है सुझाया गया लेकिन आवश्यक नहीं।*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
अधिक उन्नत ToR अवरोधन के लिए आप निम्न कार्य कर सकते हैं:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## लाभ?