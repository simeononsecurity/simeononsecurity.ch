---
title: "निम्न शक्ति वाले हार्डवेयर के साथ एक लाभदायक निष्क्रिय आय बॉक्स बनाएँ: एक गाइड"
draft: false
toc: true
date: 2023-02-07
description: "Raspberry Pi या Intel NUC का उपयोग करके एक निम्न-शक्ति निष्क्रिय आय क्रिप्टो माइनर स्थापित करना सीखें, और इस गाइड के साथ $10-$20 प्रति माह प्रति बॉक्स कमाएं"
tags: ["लाभदायक निष्क्रिय आय बॉक्स बनाएँ","कम शक्ति वाले हार्डवेयर","निष्क्रिय आय","क्रिप्टो माइनर","रास्पबेरी पाई","इंटेल एनयूसी","मार्गदर्शक","हार्डवेयर आवश्यकताएँ","ओएस स्थापना","सॉफ्टवेयर स्थापना","डॉकर","स्वचालित डॉकर कंटेनर अद्यतन","उबंटू सर्वर","उबंटू डेस्कटॉप","रास्पियन","बजट","यूएसएफएफ","छोटा","छोटा","माइक्रो पीसी","तकनीकी अनुभव","अर्नएप","मिस्ट","पीयर2प्रोफिट","हनीगैन","ट्रैफ़मॉनीटाइज़र","वॉचटावर","बिटिंग"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "एक हरे रंग का, सर्किट बोर्ड एक बॉक्स के आकार का होता है, जिसमें इंटरनेट कनेक्टिविटी के प्रतीक होते हैं, जैसे तार जुड़े होते हैं।"
coverCaption: ""
---

** कम शक्ति वाले हार्डवेयर के साथ एक लाभदायक निष्क्रिय आय बॉक्स बनाएं: एक गाइड**
इन दिनों बहुत से लोग क्रिप्टो माइनिंग और हीलियम माइनर्स जैसे लो पावर माइनर्स में हैं। ये महान और सभी हैं लेकिन वे अब और अधिक नहीं कमाते हैं और वे एक तरह की कमाई पर केंद्रित हैं। आज हम एक कम शक्ति वाला पैसिव इनकम बॉक्स बनाने जा रहे हैं जो $10-$20 प्रति माह प्रति बॉक्स और आवासीय आईपी से कहीं भी कमाता है।

*यदि आपके पास अतिथि नेटवर्क पर इस बॉक्स को स्थापित करने की क्षमता है या इससे भी बेहतर, एक अलग वीएलएएन है, तो ऐसा करें। जबकि यह एक सुरक्षा ब्लॉग है, हम हर किसी की सुरक्षा चिंताओं और जोखिम सहनशीलता को नहीं मान सकते।*

## हार्डवेयर आवश्यकताएँ:
निम्न में से एक आवश्यक है। हमें मूल रूप से किसी भी कुशल और कम शक्ति वाले कंप्यूटर की आवश्यकता होती है जिस पर हम अपना हाथ रख सकते हैं। कोई भी Raspberry PI, Intel NUC, या ऐसा ही करेगा। उन्हें इतना शक्तिशाली होने की जरूरत नहीं है। हालाँकि मैं आपको सलाह दूंगा कि आपके पास कम से कम 32g-64g स्टोरेज, 4g RAM और कम से कम 2 cpu थ्रेड्स हों। इसके लिए हम हार्डवेयर के लिए लगभग $100-$200 के बजट को लक्षित कर रहे हैं, लेकिन यदि यह आपकी आवश्यकताओं के अनुरूप है तो इसे और अधिक करने के लिए स्वतंत्र महसूस करें। हमारा शक्ति लक्ष्य लगभग है। 25w औसत।
### रास्पबेरी पाई:
इन दिनों को पकड़ना मुश्किल है लेकिन वे बहुत कम शक्ति वाले हैं और काफी अनुकूलन योग्य हैं। अपने रास्पबेरी पीआई पर रास्पियन कैसे स्थापित करें, इस बारे में जानकारी के लिए
-[Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
-[GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
-[GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### इंटेल न्यूक:
वहाँ मॉडल की विस्तृत विविधता। एक नया चुनने के लिए स्वतंत्र महसूस करें।
-[Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
-[Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
-[Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### कोई USFF/छोटा/मिनी/माइक्रो पीसी:
-[Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
-[Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### इंटेल N5100 या समान के साथ कोई भी मिनी पीसी
सुपर लो पावर रास्पबेरी पाई समकक्ष के लिए लेकिन x64 प्लेटफॉर्म पर।
-[Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
-[TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## ओएस स्थापना:
हम यहां ऑपरेटिंग सिस्टम कैसे स्थापित करें, इसके तकनीकी विवरण में नहीं जाएंगे। हालाँकि यहाँ आपको आरंभ करने के लिए कुछ बेहतरीन संसाधन दिए गए हैं
### रास्पियन:
-[Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
-[The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### उबंटू:
-[Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
-[Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
-[Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## सॉफ्टवेयर स्थापना:
यह एक लंबा खंड होने जा रहा है। हम डॉकर सेट अप करने जा रहे हैं और फिर डॉकर के माध्यम से हम स्वचालित डॉकर कंटेनर अपडेट सेट अप करेंगे और एकाधिक डॉकर कंटेनर इंस्टॉल करेंगे। हम यह भी मानते हैं कि आप ubuntu सर्वर का उपयोग कर रहे हैं, हालाँकि ubuntu सर्वर, ubuntu डेस्कटॉप और रास्पियन के लिए कमांड समान होने चाहिए।

*इस खंड के लिए हम कुछ बुनियादी तकनीकी अनुभव मानते हैं और यह कि आपने अपना ऑपरेटिंग सिस्टम पहले ही स्थापित कर लिया है और साथ ही यह भी जानते हैं कि टर्मिनल में कैसे जाना है।*

### अपडेट स्थापित कर रहा है:
हम पहले यह सुनिश्चित करना चाहते हैं कि हमारा सिस्टम पूरी तरह से अद्यतित है:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Installing Docker:
We need to uninstall any existing versions that come prepackaged with the os and install the latest from Docker's repo themselves.
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

### Install Watchtower:
This docker container automatically updates all your docker containers to the latest images on a regular interval and cleans up old (stale) images.
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Install Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping offers you the ability to get paid out in Solana for providing a node for businesses to run lightweight network tests from your network.
This averages about 0.1 Cents per day per node. Not a lot I know, but it has potential and payouts are easy. 

#### Create an account:
Create an account at [bitping.com](https://bitping.com)

#### Install the docker container:
Step 1. Run these commands first as it walks you through setting up your container and asks you to sign in.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Hit CTRL+C on your keyboard to escape the container following signing in with your bitping account.

Step 2. Run this command to persist the container in the background
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Install Earn App:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Earn app lets you share your internet as a VPN service for a surprising amount of rewards. Averages about $5 month per node per residential IP. Offers payouts via paypal and amazon gift cards. 

#### Create an Earn App Account:
Create an account at [earnapp.com](https://earnapp.com/i/c1dllee).
*Warning, requires a google account*

#### Install the non docker version of the app to get your UUID:
Be sure to uninstall after you get your UUID otherwise you'll end up running it twice on the same host and without automatic updates
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Install the docker container:
Modify the string before pasting into your terminal. You need to specify your earn app UUID.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Video Tutorial:
{{< youtube id="tt499o0OjGU" >}}

### Install Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain lets you share your internet as a VPN service for a surprising amount of rewards. Averages about $5 month per node per residential IP. Payouts can be complicated. Read into it further before deciding to use this container

#### Create a Honey Gain Account:
Create an account at [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Install the Docker Container:
Modify the string with the obvious email, password, and device name before pasting into the terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Alternate instructions for Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Video Tutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Install PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=sos)
Pawns app, again similar to the others listed here offer to pay you for sharing your internet. Minimum payout is $5. Average payout is $0.50 per month per node per IP.

#### Create a PawnsApp Account:
Create an account at [https://pawns.app](https://pawns.app/?r=sos)

#### Install the Docker Container:

Modify the following with your email, password, device name, and device id before copying to your terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Install Peer 2 Profit:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://p2pr.me/16538445386293aa3aaec4e)

Similar to EarnApp and HoneyGain, Peer2Profit shares your internet for VPN and Scraping purposes. Earns about $1 a month per node per IP.
Offers a variety of payouts including money orders, BTC, LTC, LTC, MATIC, etc.

#### Create a Peer 2 Profit Account:
Create an account at [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)

#### Install the Docker Container:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### Video Tutorial:
{{< youtube id="J_rSV5N8aQk" >}}


### Install Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/pyqL)

Similar to other offerings here. Minimum $20 Payout. Payouts can be complicated. Research for yourself to see if you want to use this service. Payouts average about $1 per node per box a month.

#### Create a Repocket Account:
Create an account at [repocket.co](https://link.repocket.co/pyqL) and grab your api key from your dashboard.
#### Install the Docker Container:
Modify the following line with your email and api key before pasting into your terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Video Tutorial:
{{< youtube id="171gWknfAbY" >}}

### Install Traff Monetizer:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=242022)

Similar to EarnApp and HoneyGain, TraffMonetizer pays you to share your internet. Averages about $2 a month per node per IP. Only offers payouts in BTC.

#### Create your Traff Monetizer Account:
Create your account at [https://traffmonetizer.com](https://traffmonetizer.com/?aff=242022)
Once you get into the dashboard, make note of your application token.

#### Install the Docker Container:
Copy the following string and append your token that you got from the dashboard before pasting into your terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Install Mysterium:
[Mysterium](https://www.mysterium.network/) is a decentralized VPN and webscraping service built on the Etherium and Polygon blockchains. 
Payments average anywhere from $1-$20 a month depending on multiple factors per node per IP. Costs $1.XX to setup a node for activation. Payouts in MYST token.


#### Install the Docker Container:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Setup the Docker Container:
Go to http://"nodeip"/#/dashboard by replacing "nodeip" with the IP address of your node. You can find this by typing "ifconfig" in the terminal.

Click “start node setup”.

Past the address of the ERC20 wallet you want to receive rewards in and click “next”. You can use a standard Ethereum address like one of your MetaMask addresses.

Type in a password you’ll use to access this node dashboard in the future. DO check the checkbox to claim the node in your network.

Click the “Get it here” link and find your API key. Copy it. Go back and paste it. Click “Save & Continue”.

#### Port Forwarding:
We can not describe how to port forward for everyone's specific hardware. Here are some resources to learn how to port forward.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Auto Restart Docker Containers on Boot:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Optional Configurations:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Increase security by blocking malware and trackers.
Force all dns requests to Cloudflares malware and tracking protection dns.
Also, block DNS/HTTPS requests.
*If you have more advanced of a router or firewall on the network you can even use packages like snort/securita  to create more advanced rules to block known bad acting IPs, tor access, torrents, p2p traffic in general, etc. This is highly suggested but not required.*
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
For more advanced ToR blocking you can do the following:
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