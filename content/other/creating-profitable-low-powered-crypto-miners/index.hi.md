---
title: "Build a Profitable Passive Income Box with Low-Powered Hardware: A Guide"
draft: false
toc: true
date: 2023-02-07
description: "Learn how to set up a low-powered passive income crypto miner using a Raspberry Pi or Intel NUC, and earn $10-$20 per month per box with this guide"
tags:
  [
    "Build a Profitable Passive Income Box",
    "Low-Powered Hardware",
    "Passive Income",
    "Crypto Miner",
    "Raspberry Pi",
    "Intel NUC",
    "Guide",
    "Hardware Requirements",
    "OS Installation",
    "Software Installation",
    "Docker",
    "Automatic Docker Container Updates",
    "Ubuntu Server",
    "Ubuntu Desktop",
    "Raspbian",
    "Budget",
    "USFF",
    "Tiny",
    "Mini",
    "Micro PC",
    "Technical Experience",
    "EarnApp",
    "MYST",
    "Peer2Profit",
    "HoneyGain",
    "TraffMonitizer",
    "Watchtower",
    "Bitping",
  ]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "a green, circuit board shaped like a box with internet connectivity symbols as wires connected to it."
coverCaption: ""
---

```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

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

```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup
```

```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite
```

```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

```bash
export P2P_EMAIL="your_email_without_quotes";
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest
```

```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

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

```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

** कम शक्ति वाले घूमने के साथ एक उपयोगी आय बॉक्स बनाएं: एक गाइड** इन दिनों बहुत से लोग क्रिप्टो माइनिंग और एलियम माइनर जैसे लो पावर माइनर्स में हैं। ये सभी महान हैं और अब अधिक कमाई नहीं कर रहे हैं और वे एक तरह से कमाई पर केंद्रित हैं। आज हम एक अपराधी इनकमिंग बॉक्स बना रहे हैं जो $10-$20 प्रति माह प्रति बॉक्स और इनकमिंग आईप से कहीं भी कमाता है। _ यदि आपके पास अतिथि नेटवर्क पर इस बॉक्स को स्थापित करने की क्षमता है या इससे भी बेहतर, एक अलग वीएलएएन, ऐसा करें। जबकि यह एक सुरक्षा ब्लॉग है, हम हर किसी की सुरक्षा की साझेदारी और जोखिम सहनशीलता को नहीं मान सकते।_ #छुट्टी की घोषणा: में से एक आवश्यक है। हमें मूल रूप से किसी भी कुशल और कम शक्ति वाले कंप्यूटर की आवश्यकता होती है जिस पर हम अपना हाथ रख सकते हैं। कोई भी Raspberry PI, Intel NUC, या ऐसा ही होगा। उन्हें इतने शक्तिशाली होने की जरूरत नहीं है। हालांकि मैं आपको सलाह देता हूं कि आपके पास कम से कम 32जी-64जी स्टोरेज, 4जी रैम और कम से कम 2 सीपीयू फोल्डर हो। इसके लिए हम छत के लिए लगभग $100-$200 के बजट को लक्षित कर रहे हैं, लेकिन यदि यह आपकी आवश्यकताओं के अनुरूप है तो इसे और अधिक करने के लिए स्वतंत्र अनुभव करें। हमारा शक्ति लक्ष्य लगभग है। 25w औसत। ### चिपचिपी पाई: इन दिनों पकड़ कठिन होती है, लेकिन वे बहुत कम अधिकार वाले होते हैं और काफी अनुकूल अनुकूलन होते हैं। अपने अटैचमेंट पर रास्पियन कैसे स्थापित करें, इसके बारे में जानकारी के लिए - [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0) - [GeekPi Raspberry Pi 4 4GB स्टेपर किट](https:// amzn.to/3jG2g2k) - [GeekPi Raspberry Pi 4 8GB स्टार्टर किट](https://amzn.to/3DQisF6) ### इंटेल न्यूक: वहाँ मॉडल की विशिष्ट विविधता। एक नई पहचान के लिए स्वतंत्र अनुभव करें। - [इंटेल अनोही 12 प्रो](https://amzn.to/3JTzLc7) - [इंटेल अनोही 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8) - [इंटेल अनोही 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6) ### कोई USFF/छोटा/मिनी/माइक्रो पीसी: - [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642) - [डेल ऑप्टिप्लेक्स 7040 माइक्रो असैस](https://www.ebay.com/itm/165504038978) ### इंटेल N5100 या समान के साथ कोई मिनी पीसी सुपर लो पावर पाएके समकक्ष लेकिन x64 प्लेटफॉर्म पर। - [बी लिंक यू59 मिनी](https://amzn.to/3YkFhcj) - [ट्रिग का मिनी कंप्यूटर](https://amzn.to/3XkbXkS) ## OS की स्थापना: हम यहां ऑपरेटिंग सिस्टम कैसे स्थापित करें, इसके तकनीकी विवरण में नहीं जाएंगे। हालाँकि आज आपने शुरुआत करने के लिए कुछ बेहतरीन संसाधन दिए हैं ### रास्पियन: - [आरंभ करना](https://www.raspberrypi.com/documentation/computers/getting-started.html) - [रास्पबेरी पाए जाने की] नई विधि](https://www.youtube.com/watch?v=jRKgEXiMtns) ### फ़ैसला: - [उबंटू डेस्कटॉप तय करें] (https://ubuntu.com/tutorials/install-ubuntu-desktop#1 -overview) - [उबंटू सर्वर - मूल स्थापना](https://ubuntu.com/server/docs/installation) - [उबंटू पूरी तरह से हो सकता है: अटक कर डाउनलोड करें और कुछ करें] (https://www. . . . . . . . . . youtube.com/watch?v=W-RFY4LQ6oE) ## सॉफ्टवेयर स्थापना: यह एक विस्तृत खंड हो रहा है। हम डॉकर सेट अप करने जा रहे हैं और फिर डॉकर के माध्यम से हम स्वचालित डॉकर कंटेनर अपडेट सेट अप और कई डॉकर क्लोजर रिकॉर्ड करेंगे। मैं यह भी कह रहा हूं कि आप सभी समीक्षकों का उपयोग कर रहे हैं, हालांकि, दोषी रिकॉर्ड्स और रास्पियन के लिए समान अधिकार होना चाहिए। _इस खंड के लिए हम कुछ तकनीकी तकनीकी अनुभव मानते हैं और आपने अपना ऑपरेटिंग सिस्टम पहले ही स्थापित कर लिया है और साथ ही यह भी जानते हैं कि टर्मिनल में कैसे जाना जाता है।_ ### सुधार स्थापित कर रहा है: हम पहले यह सुनिश्चित करना चाहते हैं कि हमारा सिस्टम पूरी तरह से अद्यतित है: ### डॉकटर स्थापित करना: हमें किसी भी मौजूदा संस्करण को चिपकाने की आवश्यकता है जो ओएस के साथ पहले पैक किया गया है और डॉकर के रेपो से संबंधित को स्वयं स्थापित करें । ### गुम्मट स्थापित करें: यह डॉकटर कंटेनर स्वचालित रूप से आपके सभी डॉकटर कंटेनरों को नियमित स्टॉक में अपडेट करता है और पुराने (बासी) एक्सपोजर को स्पष्ट करता है। ### बिटपिंग रिफंड: [_ बिटपिंग एक वेबसाइट की निगरानी और प्रदर्शन समाधान जो वास्तविक समय, वास्तविक उपयोगकर्ता निगरानी और डाउनटाइम या खराब प्रदर्शन पर प्रतिक्रिया प्रदान करता है, तनाव परीक्षण और प्रासंगिकता क्षमता के साथ, नेटवर्क इंटेलीजेंस प्रतिक्रिया द्वारा ऑपरेशन सक्रिय पुन: रूटिंग और पुन: बंद करें: , और बहिष्कृत वेबहुक के माध्यम से मौजूदा प्रवाह के कार्य के साथ।_](https://bitping.com) बिटपिंग आपको अपना नेटवर्क से खुला नेटवर्क लाने की पेशकश के लिए एक निरंतर प्रदान करने के लिए सोलाना में भुगतान करने की क्षमता प्रदान करता है। यह औसत लगभग 0.1 सेंट प्रति दिन प्रति प्रतिक्रिया है। मैं बहुत कुछ नहीं जानता, लेकिन इसकी क्षमता और भुगतान आसान है। #### खाता बनाना: [Bitping.com](https://bitping.com) पर खाता बनाना #### डॉकटर अधिकार स्थापित करें: चरण 1. इन झटकों को पहली धारा क्योंकि यह आपके खाते की स्थापना के माध्यम से चलता है और आपको साइन इन करने के लिए कहता है। अपने बिटिंग लाभ से साइन इन करने के बाद कंटेनर से बचने के लिए आप अपना CTRL+C दबाएं। चरण 2. पहलू में रहने के लिए इस क्रम को चलाया जाता है ### अर्न ऐप इंस्टॉल करें: [_ अपने डिवाइस के चालू रहने के समय का लाभ उठाएं_](https://earnapp.com/i/c1dllee) अर्न ऐप आपको आश्चर्यजनक रूप से दिखने वाली सेवा के रूप में अपना इंटरनेट शेयर करता है। औसत लगभग $5 माह प्रति गैर प्रतिरूप IP। पेआउट के माध्यम से घोषणा और उपहार कार्ड प्रदान करता है। #### अर्न एप अकाउंट अकाउंट: [earnapp.com](https://earnapp.com/i/c1dllee) पर अकाउंट अकाउंट अकाउंट अकाउंट अकाउंट अकाउंट अकाउंट पर अकाउंट बनाएं। *चेतावनी, Google के एक लाभ की आवश्यकता है* #### अपना अधिकार प्राप्त करने के लिए ऐप का गैर-डॉक्टर संस्करण स्थापित करें: अपना यूयू प्राधिकरण प्राप्त करने के बाद स्थापना रद्द करना सुनिश्चित करें अन्यथा आप इसे स्वयं एक होस्ट और सक्रिय करते हैं करते हैं जैसे अपडेट किए बिना दो बार चलेंगे - [दुःख](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions) ####डॉक्टर लगे: अपने में चिपकाने से पहली स्ट्रिंग ठीक हो जाएगी। आपको अपना अर्न ऐप UUID से देखना होगा। #### वीडियो ट्यूटोरियल:  ### रिपॉकेट करें: [* अपने आप को इंटरनेट के लिए भुगतान करें*](https:// लिंक .repocket.co/pyqL) यहां अन्य पेशकशों के समान। न्यूनतम $20 भुगतान। भुगतान जटिल हो सकता है। यह देखने के लिए स्वयं को बनाना चाहते हैं कि आप इस सेवा का क्या उपयोग करना चाहते हैं। भुगतान औसत लगभग $1 प्रति प्रति प्रति बॉक्स प्रति माह। #### एक रेपोकेट खाता बनाएँ: [repocket.co](https://link.repocket.co/pyqL) पर एक ख़ज़ाना बनाएँ और अपने बैग से अपना अत्यावश्यक कुंजी प्राप्त करें। #### डॉकर बनाएं: ठीक है आपके टर्मिनल में चिपकाने से पहले आपके ईमेल और अगले हिस्से के साथ एक नई लाइन। #### वीडियो ट्यूटोरियल:  ### ट्रैफ़ मोनेटाइज़र रिकॉर्ड करें: [*अपना इंटरनेट कनेक्शन शेयर करें और ऑनलाइन पैसे कमाएँ*](https://traffmonetizer.com/? aff= 242022) अर्नऐप्स और हनीगैन के समान, ट्रैफमोनेटाइज़र आपको अपना इंटरनेट साझा करने के लिए भुगतान करता है। औसत लगभग $2 प्रति माह प्रति प्रतिक्रिया प्रति IP। केवल बीटीसी में भुगतान प्रदान करता है। #### अपना ट्रैफ़ मोनेटाइज़र खाता बनाएँ: अपना खाता [https://traffmonetizer.com](https://traffmonetizer.com/?aff=242022) बनाएं, एक बार जब आप अपनी बातों पर पहुंचें, तो अपने एप टोर को नोट कर लें। ### इंस्टाल मिस्टीरियम: [मिस्टीरियम](https://www.mysterium.network/) एक विकेंद्रीकृत बना और वेबस्क्रैपिंग सेवा है जो एथेरियम और पॉलीगॉन ब्लॉकों पर निर्मित है। प्रति लिप प्रति अनुमान कई संभावनाओं पर भुगतान औसत कहीं भी $1-$20 प्रति माह होता है। सक्रियता के लिए समझौता करने के लिए \$1.XX खर्च होता है। MYST टोकन में भुगतान।#### डॉकर धारण करें: #### डॉकर प्रवास करें: अपने टाउन कनेक्शन के साथ "nodeip" को चाहे http://"nodeip"/#/dashboard पर जाएं। आप इसे टर्मिनल में "ifconfig" टाइप करके पा सकते हैं। "कनेक्शन शुरू करें" पर क्लिक करें। ERC20 वॉलेट का पता विगत करें जिसमें आप पुरस्कार प्राप्त करना चाहते हैं और "अगला" पर क्लिक करें। आप अपने मेटामास्क पटों में से एक जैसे मानक एथेरियम का उपयोग कर सकते हैं। एक पासवर्ड टाइप करें जिसका उपयोग करके आप भविष्य में इस विश्वसनीय स्टॉक तक पहुंचेंगे। अपने नेटवर्क में कोई भी दावा करने के लिए चेकबॉक्स को चेक करें। "इसे यहां प्राप्त करें" लिंक पर क्लिक करें और अपनी ग्राहक सूची देखें। इसे कॉपी करें। वापस जाओ और चिपकाओ। "सहेजें और जारी रखें" पर क्लिक करें। #### पोर्ट फ़ॉरवर्डिंग: हम वर्णन नहीं कर सकते कि प्रत्येक विशिष्ट चिह्न के लिए पोर्ट फ़ॉरवर्डिंग कैसे करें। आगे पोर्ट करने का तरीका सीखने के लिए यहां कुछ संसाधन दिए गए हैं।- [पोर्टफॉरवर्ड.कॉम](https://portforward.com/) - [मिस्टरियम - पोर्ट फॉरवर्डिंग](https://docs.mysterium.network/troubleshooting) ) /port-forwarding ) ### बूट पर डॉकटर को ऑटो रीस्टार्ट करें: ### वैकल्पिक रूप: - [स्वप्रारूप उबंटू अपडेट और रीबूट](https://www.cyberciti.biz/faq/set-up- ऑटोमेटिक) -) अनअटेंडेड-अपडेट्स-फॉर-उबंटू-20-04/) - [उबंटू पर टीओआर ट्रैफिक को ब्लॉक करना](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix- or- Fail2ban-on-mailserver) #### धोखेबाज़ और ट्रैकर्स को ब्लॉक करके जोखिम जोखिम बढ़ रहे हैं। क्लॉडफ्लेयर डॉक्यूमेंटेशन और सुरक्षा डीएनएस के लिए सभी डीएनएस कनेक्शन बाउंड करें। इसी के साथ DNS/HTTPS को ब्लॉक करें। _ यदि आपके पास नेटवर्क पर अधिक विस्मयकारी या फ़ायरवॉल है, तो आप ज्ञात खराब कार्य करने वाले IPs, Tor Axex, Torent, सामान्य रूप से P2p आकार आदि को ब्लॉक करने के लिए अधिक उन्नत नियम बनाने के लिए स्नॉर्ट/सिक्योरिटा जैसे पैकेज का उपयोग करें यह भी कर सकते हैं। यह अत्यधिक सलाह दी गई है, लेकिन इसकी आवश्यकता नहीं है।_ अधिक उन्नत टीओआर ब्लॉकिंग के लिए आप कुछ कार्य कर सकते हैं: ## लाभ?
