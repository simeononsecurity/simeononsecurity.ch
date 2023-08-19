---
title: "Bauen Sie mit stromsparender Hardware eine profitable passive Einnahmequelle auf: Ein Leitfaden"
draft: false
toc: true
date: 2023-02-07
description: "Erfahren Sie in dieser Anleitung, wie Sie mit einem Raspberry Pi oder Intel NUC einen Krypto-Miner mit geringem Stromverbrauch und passivem Einkommen einrichten und 10 bis 20 US-Dollar pro Monat und Box verdienen"
tags: ["Bauen Sie eine profitable passive Einkommensbox auf", "Hardware mit geringem Stromverbrauch", "Passives Einkommen", "Krypto-Miner", "Raspberry Pi", "Intel NUC", "Führung", "Hardware-Anforderungen", "Betriebssysteminstallation", "Software Installation", "Docker", "Automatische Docker-Container-Updates", "Ubuntu-Server", "Ubuntu-Desktop", "Raspbian", "Budget", "USFF", "Winzig", "Mini", "Mikro-PC", "Technische Erfahrung", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TrafficMonitizer", "Wachturm", "Beißen", "Linux-Updates", "Ubuntu", "Debian", "CentOS", "RHEL", "Offline-Updates", "lokales Repository", "Zwischenspeicher", "Server-Setup", "Client-Setup", "passender Spiegel", "debmirror", "createrepo", "apt-cacher-ng", "lecker-cron", "Linux-Systemaktualisierungen", "Offline-Paketaktualisierungen", "Offline-Software-Updates", "lokales Paket-Repository", "lokaler Paketcache", "Offline-Linux-Updates", "Umgang mit Offline-Updates", "Offline-Update-Methoden", "Offline-Systemwartung", "Linux-Server-Updates", "Linux-Client-Updates", "Offline-Softwareverwaltung", "Offline-Paketverwaltung", "Update-Strategien", "Linux-Sicherheitsupdates"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "Eine grüne, kastenförmige Leiterplatte mit Symbolen für die Internetverbindung in Form von daran angeschlossenen Drähten."
coverCaption: ""
---

**Bauen Sie mit stromsparender Hardware eine profitable passive Einnahmequelle auf: Ein Leitfaden**
Viele Menschen beschäftigen sich heutzutage mit Krypto-Mining und Minern mit geringer Leistung wie Helium-Minern. Diese sind großartig und so, aber sie verdienen nicht mehr so viel und konzentrieren sich auf eine Art des Verdienens. Heute werden wir eine passive Einkommensbox mit geringem Stromverbrauch bauen, die zwischen 10 und 20 US-Dollar pro Monat pro Box und IP für Privathaushalte einbringt.

*Wenn Sie die Möglichkeit haben, diese Box in einem Gastnetzwerk oder, noch besser, in einem getrennten VLAN einzurichten, tun Sie dies. Obwohl dies ein Sicherheitsblog ist, können wir nicht davon ausgehen, dass alle Sicherheitsbedenken und Risikotoleranz haben.*

## Hardware-Anforderungen:
Eine der folgenden Voraussetzungen ist erforderlich. Wir brauchen im Grunde einfach jeden effizienten Computer mit geringem Stromverbrauch, den wir in die Finger bekommen können. Jeder Raspberry PI, Intel NUC oder ähnliches reicht aus. Sie müssen nicht allzu mächtig sein. Ich empfehle jedoch, dass Sie über mindestens 32 bis 64 g Speicher, 4 g RAM und mindestens 2 CPU-Threads verfügen. Hierfür streben wir ein Hardware-Budget von etwa 100 bis 200 US-Dollar an, können aber auch gerne höher aussteigen, wenn es Ihren Anforderungen entspricht. Unser Leistungsziel liegt bei ca. Durchschnittlich 25 W.
### Raspberry Pi:
Heutzutage ist es schwierig, sie zu bekommen, aber sie haben einen extrem geringen Stromverbrauch und sind ziemlich anpassbar. Informationen zur Installation von Raspian auf Ihrem Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Es gibt eine große Auswahl an Modellen. Sie können sich gerne für ein neueres Modell entscheiden.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Jeder USFF/Tiny/Mini/Micro-PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Jeder Mini-PC mit Intel N5100 oder ähnlichem
Für Raspberry Pi-Äquivalent mit extrem geringem Stromverbrauch, jedoch auf einer x64-Plattform.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Betriebssysteminstallation:
Auf die technischen Details zur Installation eines Betriebssystems gehen wir hier nicht ein. Hier finden Sie jedoch einige großartige Ressourcen, die Ihnen den Einstieg erleichtern
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Software Installation:
Das wird ein längerer Abschnitt. Wir werden Docker einrichten und dann über Docker automatische Docker-Container-Updates einrichten und mehrere Docker-Container installieren. Wir gehen auch davon aus, dass Sie einen Ubuntu-Server verwenden. Die Befehle für Ubuntu-Server, Ubuntu-Desktop und Raspbian sollten jedoch alle gleich sein.

*Für diesen Abschnitt setzen wir voraus, dass Sie über grundlegende technische Erfahrungen verfügen und Ihr Betriebssystem bereits installiert haben sowie wissen, wie Sie in das Terminal gelangen.*

### Installiere Updates:
Wir möchten zunächst sicherstellen, dass unser System vollständig auf dem neuesten Stand ist:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Docker installieren:
Wir müssen alle vorhandenen Versionen deinstallieren, die mit dem Betriebssystem vorinstalliert sind, und die neueste Version aus dem Docker-Repo selbst installieren.
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

### Watchtower installieren:
Dieser Docker-Container aktualisiert automatisch alle Ihre Docker-Container in regelmäßigen Abständen auf die neuesten Images und bereinigt alte (veraltete) Images.
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Bitping installieren:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping bietet Ihnen die Möglichkeit, in Solana eine Vergütung für die Bereitstellung eines Knotens für Unternehmen zu erhalten, mit dem diese leichtgewichtige Netzwerktests in Ihrem Netzwerk durchführen können.
Dies entspricht durchschnittlich etwa 0,1 Cent pro Tag und Knoten. Ich weiß nicht viel, aber es hat Potenzial und die Auszahlung ist einfach.

#### Ein Konto erstellen:
Erstellen Sie ein Konto unter [bitping.com](https://bitping.com)

#### Installieren Sie den Docker-Container:
Schritt 1: Führen Sie zuerst diese Befehle aus, während Sie durch die Einrichtung Ihres Containers geführt werden und Sie aufgefordert werden, sich anzumelden.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Drücken Sie STRG+C auf Ihrer Tastatur, um den Container zu verlassen, nachdem Sie sich mit Ihrem Bitping-Konto angemeldet haben.

Schritt 2: Führen Sie diesen Befehl aus, um den Container im Hintergrund beizubehalten
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Earn App installieren:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Mit der Earn-App können Sie Ihr Internet als VPN-Dienst teilen und überraschend viele Belohnungen erhalten. Durchschnittlich etwa 5 US-Dollar pro Monat pro Knoten und privater IP. Bietet Auszahlungen per Paypal- und Amazon-Geschenkkarten.

#### Erstellen Sie ein Earn-App-Konto:
Erstellen Sie ein Konto unter [earnapp.com](https://earnapp.com/i/c1dllee)
*Achtung, erfordert ein Google-Konto*

#### Installieren Sie die Nicht-Docker-Version der App, um Ihre UUID zu erhalten:
Stellen Sie sicher, dass Sie die Installation deinstallieren, nachdem Sie Ihre UUID erhalten haben. Andernfalls führen Sie das Programm am Ende zweimal auf demselben Host und ohne automatische Updates aus
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Installieren Sie den Docker-Container:
Ändern Sie die Zeichenfolge, bevor Sie sie in Ihr Terminal einfügen. Sie müssen die UUID Ihrer Earn-App angeben.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Videoanleitung:
{{< youtube id="tt499o0OjGU" >}}

### Honey Gain installieren:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Mit Honey Gain können Sie Ihr Internet als VPN-Dienst für überraschend viele Belohnungen teilen. Durchschnittlich etwa 5 US-Dollar pro Monat pro Knoten und privater IP. Auszahlungen können kompliziert sein. Lesen Sie es weiter, bevor Sie sich für die Verwendung dieses Behälters entscheiden

#### Erstellen Sie ein Honey Gain-Konto:
Erstellen Sie ein Konto unter [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Installieren Sie den Docker-Container:
Ändern Sie die Zeichenfolge mit der offensichtlichen E-Mail-Adresse, dem Passwort und dem Gerätenamen, bevor Sie sie in das Terminal einfügen
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Alternative Anleitung für Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Videoanleitung:
{{< youtube id="Wd11M0nSy1k" >}}

### PawnsApp installieren:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Die Pawns-App ähnelt wiederum den anderen hier aufgeführten und bietet Ihnen eine Bezahlung für die gemeinsame Nutzung Ihres Internets an. Die Mindestauszahlung beträgt 5 $. Die durchschnittliche Auszahlung beträgt 0,50 $ pro Monat, pro Knoten und pro IP.

#### Erstellen Sie ein PawnsApp-Konto:
Erstellen Sie ein Konto unter [https://pawns.app](https://pawns.app/?r=2092882)

#### Installieren Sie den Docker-Container:

Ändern Sie Folgendes mit Ihrer E-Mail-Adresse, Ihrem Passwort, Ihrem Gerätenamen und Ihrer Geräte-ID, bevor Sie es auf Ihr Terminal kopieren.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Installieren Sie Peer 2 Profit:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://p2pr.me/16538445386293aa3aaec4e)

Ähnlich wie EarnApp und HoneyGain teilt Peer2Profit Ihr Internet für VPN- und Scraping-Zwecke. Verdient etwa 1 US-Dollar pro Monat pro Knoten und IP.
Bietet eine Vielzahl von Auszahlungen, einschließlich Zahlungsanweisungen, BTC, LTC, LTC, MATIC usw.

#### Erstellen Sie ein Peer-2-Gewinnkonto:
Erstellen Sie ein Konto unter [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)

#### Installieren Sie den Docker-Container:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### Videoanleitung:
{{< youtube id="J_rSV5N8aQk" >}}


### RePocket installieren:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Ähnlich wie bei anderen Angeboten hier. Mindestauszahlung von 20 $. Auszahlungen können kompliziert sein. Recherchieren Sie selbst, ob Sie diesen Service nutzen möchten. Die Auszahlungen betragen durchschnittlich etwa 1 US-Dollar pro Knoten und Box pro Monat.

#### Erstellen Sie ein Repocket-Konto:
Erstellen Sie ein Konto unter [repocket.co](https://link.repocket.co/raqc) und holen Sie sich Ihren API-Schlüssel von Ihrem Dashboard.
#### Installieren Sie den Docker-Container:
Ändern Sie die folgende Zeile mit Ihrer E-Mail-Adresse und Ihrem API-Schlüssel, bevor Sie sie in Ihr Terminal einfügen.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Videoanleitung:
{{< youtube id="171gWknfAbY" >}}

### Traffic Monetizer installieren:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Ähnlich wie EarnApp und HoneyGain bezahlt Sie TraffMonetizer dafür, dass Sie Ihr Internet teilen. Durchschnittlich etwa 2 US-Dollar pro Monat pro Knoten und IP. Bietet nur Auszahlungen in BTC an.

#### Erstellen Sie Ihr Traff Monetizer-Konto:
Erstellen Sie Ihr Konto unter [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Notieren Sie sich im Dashboard Ihren Anwendungstoken.

#### Installieren Sie den Docker-Container:
Kopieren Sie die folgende Zeichenfolge und hängen Sie Ihr Token an, das Sie vom Dashboard erhalten haben, bevor Sie es in Ihr Terminal einfügen.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Mysterium installieren:
[Mysterium](https://www.mysterium.network/) ist ein dezentraler VPN- und Webscraping-Dienst, der auf den Blockchains Etherium und Polygon basiert.
Die durchschnittlichen Zahlungen liegen zwischen 1 und 20 US-Dollar pro Monat, abhängig von mehreren Faktoren pro Knoten und IP. Die Einrichtung eines Knotens für die Aktivierung kostet 1,XX $. Auszahlungen im MYST-Token.


#### Installieren Sie den Docker-Container:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Richten Sie den Docker-Container ein:
Gehen Sie zu http://"nodeip"/#/dashboard, indem Sie „nodeip“ durch die IP-Adresse Ihres Knotens ersetzen. Diese finden Sie, indem Sie im Terminal „ifconfig“ eingeben.

Klicken Sie auf „Knoteneinrichtung starten“.

Geben Sie die Adresse des ERC20-Wallets ein, in dem Sie Prämien erhalten möchten, und klicken Sie auf „Weiter“. Sie können eine Standard-Ethereum-Adresse wie eine Ihrer MetaMask-Adressen verwenden.

Geben Sie ein Passwort ein, mit dem Sie in Zukunft auf dieses Knoten-Dashboard zugreifen. Aktivieren Sie das Kontrollkästchen, um den Knoten in Ihrem Netzwerk zu beanspruchen.

Klicken Sie auf den Link „Hier herunterladen“ und suchen Sie Ihren API-Schlüssel. Kopiere es. Gehen Sie zurück und fügen Sie es ein. Klicken Sie auf „Speichern und fortfahren“.

#### Port-Weiterleitung:
Wir können nicht beschreiben, wie die Portweiterleitung für jede spezifische Hardware durchgeführt wird. Hier finden Sie einige Ressourcen zum Erlernen der Portweiterleitung.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Docker-Container beim Booten automatisch neu starten:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Optionale Konfigurationen:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Erhöhen Sie die Sicherheit, indem Sie Malware und Tracker blockieren.
Erzwingen Sie alle DNS-Anfragen an Cloudflares-Malware und Tracking-Schutz-DNS.
Blockieren Sie außerdem DNS/HTTPS-Anfragen.
*Wenn Sie über einen fortgeschritteneren Router oder eine Firewall im Netzwerk verfügen, können Sie sogar Pakete wie snort/securita verwenden, um erweiterte Regeln zu erstellen, um bekanntermaßen schädliche IPs, Tor-Zugriff, Torrents, P2P-Verkehr im Allgemeinen usw. zu blockieren. Das ist sehr hilfreich empfohlen, aber nicht erforderlich.*
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
Für eine erweiterte ToR-Blockierung können Sie Folgendes tun:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Gewinn?