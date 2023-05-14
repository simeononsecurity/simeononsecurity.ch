---
title: "Construiți o cutie de venit pasiv profitabilă cu hardware de putere redusă: un ghid"
draft: false
toc: true
date: 2023-02-07
description: "Aflați cum să configurați un cripto miner cu venituri pasive cu putere redusă folosind un Raspberry Pi sau Intel NUC și să câștigați 10-20 USD pe lună pe cutie cu acest ghid"
tags: ["Construiți o cutie de venit pasiv profitabilă", "Hardware cu putere redusă", "Venit pasiv", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Ghid", "Cerințe hardware", "Instalare OS", "Instalarea software-ului", "Docher", "Actualizări automate ale containerelor Docker", "Ubuntu Server", "Desktop Ubuntu", "Raspbian", "Buget", "USFF", "Micut", "Mini", "Micro PC", "Experiență tehnică", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Turnul de veghe", "Mușcătură"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "o placă de circuit verde, în formă de cutie, cu simboluri de conectare la internet ca fire conectate la ea."
coverCaption: ""
---

**Construiți o cutie de venit pasiv profitabilă cu hardware de putere redusă: un ghid**
Mulți oameni în aceste zile sunt interesați de mineritul criptografic și de mineri cu putere redusă, cum ar fi minerii de heliu. Acestea sunt grozave și toate, dar nu mai câștigă atât de mult și sunt concentrate pe un singur fel de câștig. Astăzi vom construi o casetă cu venituri pasive cu putere redusă, care câștigă între 10 USD și 20 USD pe lună pe cutie și IP rezidențial.

*Dacă aveți posibilitatea de a configura această casetă într-o rețea de oaspeți sau, chiar mai bine, într-un VLAN segregat, faceți acest lucru. Deși acesta este un blog de securitate, nu ne putem asuma preocupările de securitate și toleranța la risc ale tuturor.*

## Cerințe hardware:
Este necesar unul dintre următoarele. Practic avem nevoie de orice computer eficient și cu putere redusă pe care putem pune mâna. Orice Raspberry PI, Intel NUC sau similar va fi potrivit. Nu trebuie să fie atât de puternici. Cu toate acestea, vă voi recomanda să aveți cel puțin 32g-64g de stocare, 4g de ram și cel puțin 2 fire de procesare. Pentru aceasta, vom viza un buget de aproximativ 100-200 USD pentru hardware, dar nu ezitați să mergeți mai mult dacă se potrivește nevoilor dvs. Ținta noastră de putere este de aprox. 25w medie.
### Raspberry Pi:
Este greu de atins aceste zile, dar au o putere foarte scăzută și sunt destul de personalizabile. Pentru informații despre cum să instalați raspian pe Raspberry PI
-[Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
-[GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
-[GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
O mare varietate de modele disponibile. Simțiți-vă liber să alegeți unul mai nou.
-[Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
-[Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
-[Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Orice PC USFF/Tiny/Mini/Micro:
-[Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
-[Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Orice Mini PC cu Intel N5100 sau similar
Pentru echivalentul Raspberry Pi cu putere foarte scăzută, dar pe platforma x64.
-[Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
-[TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instalare OS:
Nu vom intra în detaliile tehnice despre cum să instalați un sistem de operare aici. Cu toate acestea, iată câteva resurse excelente pentru a începe
### Raspbian:
-[Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
-[The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
-[Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
-[Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
-[Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instalarea software-ului:
Aceasta va fi o secțiune mai lungă. Vom configura docker și apoi prin docker vom configura actualizări automate ale containerelor docker și vom instala mai multe containere docker. De asemenea, presupunem că utilizați serverul ubuntu, totuși comenzile pentru serverul ubuntu, desktopul ubuntu și raspbian ar trebui să fie toate aceleași.

*Pentru această secțiune presupunem o experiență tehnică de bază și că ați instalat deja sistemul de operare și că știți cum să intrați în terminal.*

### Instalarea actualizărilor:
În primul rând, vrem să ne asigurăm că avem sistemul nostru complet actualizat:
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

## Profit?