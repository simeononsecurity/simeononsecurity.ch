---
title: "Construiți o cutie de venit pasiv profitabilă cu hardware de putere redusă: un ghid"
draft: false
toc: true
date: 2023-02-07
description: "Aflați cum să configurați un cripto miner cu venituri pasive cu putere redusă folosind un Raspberry Pi sau Intel NUC și să câștigați 10-20 USD pe lună pe cutie cu acest ghid"
tags: ["Construiți o cutie de venit pasiv profitabilă", "Hardware cu putere redusă", "Venit pasiv", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Ghid", "Cerințe hardware", "Instalare OS", "Instalarea software-ului", "Docher", "Actualizări automate ale containerelor Docker", "Ubuntu Server", "Desktop Ubuntu", "Raspbian", "Buget", "USFF", "Micut", "Mini", "Micro PC", "Experiență tehnică", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Turnul de veghe", "Mușcătură", "Actualizări Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "actualizări offline", "depozit local", "cache", "configurarea serverului", "configurarea clientului", "apt-oglindă", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Actualizări de sistem Linux", "actualizări de pachete offline", "actualizări de software offline", "depozitul local de pachete", "memoria cache locală a pachetelor", "actualizări offline Linux", "gestionarea actualizărilor offline", "metode de actualizare offline", "întreținerea sistemului offline", "Actualizări de server Linux", "Actualizări ale clientului Linux", "management software offline", "gestionarea pachetelor offline", "strategii de actualizare", "Actualizări de securitate Linux"]
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
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
O mare varietate de modele disponibile. Simțiți-vă liber să alegeți unul mai nou.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Orice PC USFF/Tiny/Mini/Micro:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Orice Mini PC cu Intel N5100 sau similar
Pentru echivalentul Raspberry Pi cu o putere foarte mică, dar pe platforma x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instalare OS:
Nu vom intra în detaliile tehnice despre cum să instalați un sistem de operare aici. Cu toate acestea, iată câteva resurse excelente pentru a începe
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instalarea software-ului:
Aceasta va fi o secțiune mai lungă. Vom configura docker și apoi prin docker vom configura actualizări automate ale containerelor docker și vom instala mai multe containere docker. De asemenea, presupunem că utilizați serverul ubuntu, totuși comenzile pentru serverul ubuntu, desktopul ubuntu și raspbian ar trebui să fie toate aceleași.

*Pentru această secțiune presupunem o experiență tehnică de bază și că ați instalat deja sistemul de operare și că știți cum să intrați în terminal.*

### Instalarea actualizărilor:
În primul rând, vrem să ne asigurăm că avem sistemul nostru complet actualizat:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Instalarea Docker:
Trebuie să dezinstalăm toate versiunile existente care sunt pre-ambalate cu sistemul de operare și să instalăm ei înșiși cele mai recente din repo-ul Docker.
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

### Instalează Watchtower:
Acest container docker actualizează automat toate containerele dvs. docker la cele mai recente imagini la un interval regulat și curăță imaginile vechi (învechite).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Instalați Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping vă oferă posibilitatea de a fi plătit în Solana pentru furnizarea unui nod pentru ca întreprinderile să ruleze teste de rețea ușoare din rețeaua dvs.
Aceasta înseamnă aproximativ 0,1 cenți pe zi per nod. Nu știu multe, dar are potențial și plățile sunt ușoare.

#### Creați un cont:
Creează un cont la [bitping.com](https://bitping.com)

#### Instalați containerul docker:
Pasul 1. Rulați mai întâi aceste comenzi, în timp ce vă ghidează prin configurarea containerului și vă solicită să vă conectați.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Apăsați CTRL+C de pe tastatură pentru a scăpa din container după conectarea cu contul de bitping.

Pasul 2. Rulați această comandă pentru a persista containerul în fundal
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Instalați aplicația Earn:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

Aplicația Earn vă permite să vă împărtășiți internetul ca serviciu VPN pentru o sumă surprinzătoare de recompense. În medie, aproximativ 5 USD pe nod per IP rezidențial. Oferă plăți prin carduri cadou paypal și Amazon.

#### Creați un cont Earn App:
Creează un cont la [earnapp.com](https://earnapp.com/i/GCL9QzB5)
*Atenție, necesită un cont Google*

#### Instalați versiunea non docker a aplicației pentru a obține UUID-ul dvs.:
Asigurați-vă că dezinstalați după ce obțineți UUID-ul, altfel îl veți rula de două ori pe aceeași gazdă și fără actualizări automate
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Instalați containerul docker:
Modificați șirul înainte de a lipi în terminal. Trebuie să specificați UUID-ul aplicației dvs. de câștig.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Tutorial video:
{{< youtube id="tt499o0OjGU" >}}

### Instalați Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/HONEY9149D)

Honey Gain vă permite să vă împărtășiți internetul ca serviciu VPN pentru o sumă surprinzătoare de recompense. În medie, aproximativ 5 USD pe nod per IP rezidențial. Plățile pot fi complicate. Citiți mai departe înainte de a vă decide să utilizați acest recipient

#### Creați un cont Honey Gain:
Creează un cont la [honeygain.com](https://r.honeygain.me/HONEY9149D)

#### Instalați containerul Docker:
Modificați șirul cu e-mailul evident, parola și numele dispozitivului înainte de a lipi în terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Instrucțiuni alternative pentru Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Tutorial video:
{{< youtube id="Wd11M0nSy1k" >}}

### Instalați PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=sos)
Aplicația Pawns, din nou similară cu celelalte enumerate aici, vă oferă să vă plătească pentru partajarea internetului. Plata minimă este de 5 USD. Plata medie este de 0,50 USD pe lună per nod per IP.

#### Creați un cont PawnsApp:
Creează un cont la [https://pawns.app](https://pawns.app/?r=sos)

#### Instalați containerul Docker:

Modificați următoarele cu e-mailul, parola, numele dispozitivului și ID-ul dispozitivului înainte de a copia pe terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Instalați Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Similar cu alte oferte de aici. Plată minimă de 20 USD. Plățile pot fi complicate. Cercetați singuri pentru a vedea dacă doriți să utilizați acest serviciu. Plățile sunt în medie de aproximativ 1 USD pe nod pe cutie pe lună.

#### Creați un cont de rebuzunare:
Creează un cont la [repocket.co](https://link.repocket.co/raqc) și luați-vă cheia API din tabloul de bord.
#### Instalați containerul Docker:
Modificați următoarea linie cu e-mailul și cheia API înainte de a lipi în terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Tutorial video:
{{< youtube id="171gWknfAbY" >}}

### Instalați generatorul de bani pentru trafic:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Similar cu EarnApp și HoneyGain, TraffMoetizer vă plătește pentru a vă partaja internetul. În medie, aproximativ 2 USD pe lună per nod per IP. Oferă doar plăți în BTC.

#### Creați contul dvs. de generare de bani pentru trafic:
Creează-ți contul la [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Odată ce intri în tabloul de bord, notează indicativul aplicației.

#### Instalați containerul Docker:
Copiați următorul șir și adăugați simbolul pe care l-ați primit din tabloul de bord înainte de a lipi în terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli_v2 start accept --token
```

### Instalați Mysterium:
[Mysterium](https://www.mysterium.network/) este un serviciu VPN descentralizat și webscraping construit pe blockchain-urile Etherium și Polygon.
Plățile sunt în medie între 1 USD și 20 USD pe lună, în funcție de mai mulți factori per nod per IP. Costă 1,XX USD pentru a configura un nod pentru activare. Plăți în token MYST.


#### Instalați containerul Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Configurați containerul Docker:
Accesați http://"nodeip"/#/dashboard prin înlocuirea „nodeip” cu adresa IP a nodului dvs. Puteți găsi acest lucru tastând „ifconfig” în terminal.

Faceți clic pe „porniți configurarea nodului”.

Trecuți adresa portofelului ERC20 în care doriți să primiți recompense și faceți clic pe „următorul”. Puteți utiliza o adresă standard Ethereum ca una dintre adresele dvs. MetaMask.

Introduceți o parolă pe care o veți folosi pentru a accesa acest tablou de bord nod în viitor. Bifați caseta de selectare pentru a revendica nodul din rețeaua dvs.

Faceți clic pe linkul „Obțineți aici” și găsiți-vă cheia API. Copiați-l. Întoarceți-vă și lipiți-l. Faceți clic pe „Salvați și continuați”.

#### Port forwarding:
Nu putem descrie cum să port forward pentru hardware-ul specific al fiecăruia. Iată câteva resurse pentru a învăța cum să port forward.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Repornire automată a containerelor Docker la pornire:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configurații opționale:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Creșteți securitatea prin blocarea programelor malware și a dispozitivelor de urmărire.
Forțați toate solicitările dns la malware Cloudflares și dns de protecție de urmărire.
De asemenea, blocați cererile DNS/HTTPS.
*Dacă aveți un router sau un firewall mai avansat în rețea, puteți chiar să utilizați pachete precum snort/securita pentru a crea reguli mai avansate pentru a bloca IP-uri cunoscute care acționează prost, accesul tor, torrente, traficul p2p în general, etc. sugerat, dar nu obligatoriu.*
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
Pentru o blocare mai avansată a ToR, puteți face următoarele:
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