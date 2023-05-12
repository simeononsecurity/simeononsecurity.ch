---
title: "Build a Profitable Passive Income Box with Low-Powered Hardware: A Guide"
draft: false
toc: true
date: 2023-02-07
description: "Learn how to set up a low-powered passive income crypto miner using a Raspberry Pi or Intel NUC, and earn $10-$20 per month per box with this guide"
tags: ["Build a Profitable Passive Income Box", "Low-Powered Hardware", "Passive Income", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guide", "Hardware Requirements", "OS Installation", "Software Installation", "Docker", "Automatic Docker Container Updates", "Ubuntu Server", "Ubuntu Desktop", "Raspbian", "Budget", "USFF", "Tiny", "Mini", "Micro PC", "Technical Experience", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Watchtower", "Bitping"]
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
 **Bauen Sie mit Low-Power-Hardware eine mietbare passive Einkommensbox auf: Ein Leitfaden** Heutzutage interessieren sich viele Menschen für Krypto-Mining und Low-Power-Miner wie Helium-Miner. Diese sind großartig und alle, aber sie verdienen nicht mehr so viel und sie konzentrieren sich auf eine Art des Verdienens. Heute werden wir eine passive Einkommensbox mit elektrischem Stromverbrauch bauen, die zwischen 10 und 20 US-Dollar pro Monat pro Box und Wohn-IP verdient.  *Wenn Sie die Möglichkeit haben, diese Box in einem Gastnetzwerk oder, noch besser, in einem getrennten VLAN aufzurufen, tun Sie dies. Obwohl dies ein Sicherheitsblog ist, können wir nicht die Sicherheitsbedenken und die Risikobereitschaft aller annehmen.*  ## Hardware-Anforderungen: Eines der folgenden ist erforderlich. Wir brauchen im Grunde nur jeden effizienten und stromsparenden Computer, den wir in die Finger bekommen können. Jeder Raspberry PI, Intel NUC oder ähnliches reicht aus. Sie müssen nicht allzu mächtig sein. Ich empfehle jedoch, dass Sie mindestens 32 g bis 64 g Speicher, 4 g RAM und mindestens 2 CPU-Threads haben. Dafür streben wir ein Budget von etwa 100 bis 200 US-Dollar für Hardware an, can aber gerne höher gehen, wenn es Ihren Anforderungen entspricht. Unser Leistungsziel liegt bei ca. 25w Durchschnitt. ### Himbeer-Pi: Heutzutage schwer zu bekommen, aber sie sind sehr stromsparend und lassen sich gut anpassen. Informationen zur Installation von Raspian auf Ihrem Raspberry PI - [Raspberry Pi 4B Modell B Bausatz] (https://amzn.to/3x72kv0) - [GeeekPi Raspberry Pi 4 4 GB Starterkit] (https://amzn.to/3jG2g2k) - [GeeekPi Raspberry Pi 4 8 GB Starterkit] (https://amzn.to/3DQisF6) ### Intel Nuc: Große Auswahl an Modellen da draußen. Fühlen Sie sich frei, ein neueres zu wählen. - [Intel NUC 12 Pro](https://amzn.to/3JTzLc7) - [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8) - [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6) ### Jeder USFF/Tiny/Mini/Micro PC: - [Lenovo ThinkCentre M900 Tiny] (https://www.ebay.com/itm/385116504642) - [Dell OptiPlex 7040 Micro USFF] (https://www.ebay.com/itm/165504038978) ### Jeder Mini-PC mit Intel N5100 oder ähnlichem Für Raspberry Pi-Äquivalente mit extrem niedrigem Stromverbrauch, jedoch auf x64-Plattform. - [Beelink U59 Mini-PC] (https://amzn.to/3YkFhcj) - [TRIGKEY Mini-Computer](https://amzn.to/3XkbXkS)  ## OS-Installation: Auf die technischen Details zur Installation eines Betriebssystems gehen wir hier nicht ein. Hier sind jedoch einige hervorragende Ressourcen, um Ihnen den Einstieg zu erleichtern ### Raspbian: - [Erste Schritte](https://www.raspberrypi.com/documentation/computers/getting-started.html) - [Die neue Methode zum Einrichten von Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns) ###Ubuntu: - [Ubuntu-Desktop installieren] (https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) - [Ubuntu Server - Basisinstallation] (https://ubuntu.com/server/docs/installation) - [Ubuntu Complete Beginner's Guide: Ubuntu herunterladen und installieren](https://www.youtube.com/watch?v=W-RFY4LQ6oE)   ## Software Installation: Das wird ein längerer Abschnitt. Wir Werden Docker einrichten und dann über Docker automatische Docker-Container-Updates einrichten und mehrere Docker-Container installieren. Wir gehen auch davon aus, dass SIE Ubuntu-Server verwenden, die Befehle für Ubuntu-Server, Ubuntu-Desktop und Raspbian sollten jedoch alle gleich sein.  *Für diesen Abschnitt setzen wir einige technische Grundkenntnisse voraus und dass SIE Ihr Betriebssystem bereits installiert haben und wissen, wie Sie in das Terminal gelangen.*  ### Installiere Updates: Wir wollen zunächst sicher sein, dass wir unser System auf dem neuesten Stand haben:  ### Docker installieren: Wir & alle vorhandenen Versionen, die mit dem Betriebssystem vorinstalliert sind, deinstallieren und die neueste Version aus Dockers Repo selbst installieren.  ###Wachturm installieren: Dieser Docker-Container aktualisiert alle Ihre Docker-Container zuverlässig automatisch auf sterben neuesten Bilder und bereinigte alte (veraltete) Bilder.  ### Bitping installieren: [*Bitping ist eine Website-Überwachungs- und Leistungsoptimierungslösung, die Echtzeit-, echte Benutzerüberwachung und sofortiges Feedback zu Ausfallzeiten oder Leistungseinbußen bietet, mit Stresstest- und Benchmarking-Funktionen, dynamischer Umleitung und Neubereitstellung, die von einer verteilten Netzwerkintelligenzschicht und Integration unterstützt wird mit vorhandene Workflows über Webhooks.*](https://bitping.com)  Bitping bietet Ihnen die Möglichkeit, in Solana für die Bereitstellung eines Knotens für Unternehmen ausgezahlt zu werden, um leichte Netzwerktests von Ihrem Netzwerk auszuführen. Das sind durchschnittlich etwa 0,1 Cent pro Tag und Knoten. Ich weiß nicht viel, aber es hat Potenzial und die Auszahlungen sind einfach.  #### Ein Konto erstellen: Erstelle ein Konto auf [bitping.com](https://bitping.com)  #### Installieren Sie den Docker-Container: Schritt 1. Führen Sie zuerst diese Befehle aus, während SIE durch die Einrichtung Ihres Containers geführt werden und Sie aufgefordert werden, sich anzumelden.  Drücken Sie STRG+C auf Ihrer Tastatur, um den Container zu verlassen, nachdem Sie sich mit Ihrem Bitping-Konto angemeldet haben.  Schritt 2. Führen Sie diesen Befehl aus, um den Container im Hintergrund beizubehalten   ### Earn-App installieren: [*Nutze die Zeit, in der deine Geräte ungenutzt bleiben, dafür du für die ungenutzten Ressourcen deines eingestellten bezahlt wirst*](https://earnapp.com/i/c1dllee)  Mit der Earn-App können Sie Ihr Internet als VPN-Dienst für eine überraschende Menge an Prämien freigeben. Im Durchschnitt etwa 5 $ pro Knoten und Wohn-IP im Monat. Bietet Auszahlungen über Paypal und Amazon-Geschenkkarten an.  #### Erstellen Sie ein Earn App-Konto: Erstellen Sie ein Konto unter [earnapp.com](https://earnapp.com/i/c1dllee). *Achtung, erfordert ein Google-Konto*  #### Installieren Sie die Nicht-Docker-Version der App, um Ihre UUID zu erhalten: Stellen Sie sicher, dass Sie deinstallieren, nachdem Sie Ihre UUID erhalten haben, da Sie sonst zweimal auf demselben Host und ohne automatische Updates ausführen - [Anleitung] (https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)  #### Installieren Sie den Docker-Container: Ändern Sie die Zeichenfolge, bevor Sie sie in Ihr Terminal einfügen. Sie müssen Ihre Earn-App-UUID angeben. #### Videoanleitung: {{< youtube id="tt499o0OjGU" >}}  ### Honey Gain installieren: [*Passives Einkommen – Mit Honeygain können Sie mühelos Geld verdienen, indem Sie einfach Ihr Internet teilen. Verdienen Sie jetzt.*](https://r.honeygain.me/DAVID07A75)  Mit Honey Gain können Sie Ihr Internet als VPN-Dienst für überraschend viele Belohnungen freigeben. Im Durchschnitt etwa 5 $ pro Knoten und Wohn-IP im Monat. Auszahlungen können kompliziert sein. Lesen Sie sich weiter ein, bevor Sie sich entscheiden, diesen Behälter zu verwenden  #### Erstellen Sie ein Honey Gain-Konto: Erstellen Sie ein Konto auf [honeygain.com](https://r.honeygain.me/DAVID07A75)  #### Installieren Sie den Docker-Container: Ändern Sie die Zeichenfolge mit der offensichtlichen E-Mail, dem Kennwort und dem Gerätenamen, bevor Sie sie in das Terminal einfügen  #### Alternative Anweisungen für Raspberry Pi - [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)  #### Videoanleitung: {{< youtube id="Wd11M0nSy1k" >}}  ### PawnsApp installieren: [*Verdienen Sie online passives Geld, indem Sie Umfragen ausfüllen und Ihr Internet teilen *](https://pawns.app/?r=sos) Die Pawns-App, die den anderen hier aufgelistet erscheint, bietet eine, SIE für die gemeinsame Nutzung Ihres Internets zu bezahlen. Die Mindestauszahlung beträgt $5. Die durchschnittliche Auszahlung beträgt 0,50 $ pro Monat pro Knoten und IP.  #### Erstellen Sie ein PawnsApp-Konto: Erstellen Sie ein Konto unter [https://pawns.app](https://pawns.app/?r=sos)  #### Installieren Sie den Docker-Container:  Ändern Sie Folgendes mit Ihrer E-Mail-Adresse, Ihrem Passwort, Ihrem Gerätenamen und Ihrer Geräte-ID, bevor Sie sie auf Ihr Terminal kopieren.  ### Installieren Sie Peer 2 Profit: [*TEILEN SIE IHREN TRAFFIC UND PROFITIEREN SIE DAVON!*](https://p2pr.me/16538445386293aa3aaec4e)  Ähnlich wie EarnApp und HoneyGain teilt Peer2Profit Ihr Internet für VPN- und Scraping-Zwecke. Verdienen etwa 1 $ pro Monat pro Knoten und IP. Bietet eine Vielzahl von Auszahlungen, einschließlich Zahlungsanweisungen, BTC, LTC, LTC, MATIC usw.  #### Erstellen Sie ein Peer-2-Gewinnkonto: Erstellen Sie ein Konto auf [peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)  #### Installieren Sie den Docker-Container: #### Videoanleitung: {{< youtube id="J_rSV5N8aQk" >}}   ###Repocket installieren: [*Werden Sie für Ihr ungenutztes Internet bezahlt*](https://link.repocket.co/pyqL)  Ähnlich wie bei anderen Angeboten hier. Mindestauszahlung von $20. Auszahlungen können kompliziert sein. Recherchieren Sie selbst, ob Sie diesen Service nutzen möchten. Die Auszahlungen betragen durchschnittlich etwa 1 $ pro Node pro Box und Monat.  #### Erstellen Sie ein Repocket-Konto: Erstellen Sie ein Konto bei [repocket.co](https://link.repocket.co/pyqL) und holen Sie sich Ihren API-Schlüssel von Ihrem Dashboard. #### Installieren Sie den Docker-Container: Ändern Sie die folgende Zeile mit Ihrer E-Mail und Ihrem API-Schlüssel, bevor Sie sie in Ihr Terminal einfügen. #### Videoanleitung: {{< youtube id="171gWknfAbY" >}}  ### Traffic Monetizer installieren: [*Teilen Sie Ihre Internetverbindung und verdienen Sie online Geld*](https://traffmonetizer.com/?aff=242022)  Ähnlich wie EarnApp und HoneyGain bezahlt TraffMonetizer Sie dafür, Ihr Internet zu teilen. Durchschnittlich etwa 2 $ pro Monat pro Knoten und IP. Bietet nur Auszahlungen in BTC an.  #### Erstellen Sie Ihr Traffic Monetizer-Konto: Erstellen Sie Ihr Konto unter [https://traffmonetizer.com](https://traffmonetizer.com/?aff=242022) Sobald Sie das Dashboard aufgerufen haben, notieren Sie sich Ihr Anwendungstoken.  #### Installieren Sie den Docker-Container: Kopieren Sie die folgende Zeichenfolge und hängen Sie Ihr Token an, das Sie vom Dashboard erhalten haben, bevor Sie es in Ihr Terminal einfügen.   ### Mysterium installieren: [Mysterium](https://www.mysterium.network/) ist ein dezentraler VPN- und Webscraping-Dienst, der auf den Etherium- und Polygon-Blockchains aufbaut. Die Rechnung liegt im Durchschnitt zwischen 1 und 20 US-Dollar pro Monat, abhängig von mehreren Faktoren pro Knoten und IP. Kostet 1,XX $, um einen Knoten für die Aktivierung zu beantragen. Auszahlungen in MYST-Token.   #### Installieren Sie den Docker-Container:  #### Richten Sie den Docker-Container ein: Gehen Sie zu http://"nodeip"/#/dashboard, und ersetzen Sie "nodeip" durch die IP-Adresse Ihres Knotens. Sie finden stirbt, dafür müssen Sie im Terminal "ifconfig" eingeben.  Klicken Sie auf „Knoteneinrichtung starten“.  Geben Sie die Adresse der ERC20-Geldbörse ein, in der Sie Prämien erhalten möchten, und klicken Sie auf „Weiter“. Sie können eine Standard-Ethereum-Adresse wie eine Ihrer MetaMask-Adressen verwenden.  Geben Sie ein Passwort ein, mit dem SIE in Zukunft auf dieses Knoten-Dashboard zugreifen werden. Aktivieren Sie das Kontrollkästchen, um den Knoten in Ihrem Netzwerk zu beanspruchen.  Klicken Sie auf den Link „Get it here“ und finden Sie Ihren API-Schlüssel. Kopien es. Gehen Sie zurück und fügen Sie es ein. Klicken Sie auf „Speichern & Fortfahren“.  #### Hafen-Weiterleitung: Wir können nicht beschreiben, wie die Portweiterleitung für jede spezifische Hardware durchgeführt wird. Hier sind einige Ressourcen, um zu lernen, wie man weiterleitet. - [PortForward.com](https://portforward.com/) - [Mysterium - Portweiterleitung](https://docs.mysterium.network/troubleshooting/port-forwarding)   ### Docker-Container beim Booten automatisch neu starten:  ### Optionale Konfigurationen: - [Automatische Ubuntu-Updates und -Neustarts](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/) - [Blockieren von ToR-Verkehr auf Ubuntu] (https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver) #### Erhöhen Sie die Sicherheit, indem Sie Malware und Tracker blockieren. Erzwingen Sie alle DNS-Anfragen an Cloudflares-Malware und Tracking-Schutz-DNS. Blockieren Sie außerdem DNS/HTTPS-Anfragen. *Wenn SIE einen intensiven Router oder eine Firewall im Netzwerk haben, können SIE sogar Pakete wie snort/securita verwenden, um umfangreichere Regeln zu erstellen, um bekanntermaßen schlecht funktionierende IPs, Tor-Zugriff, Torrents, P2P-Verkehr im Allgemeinen usw. zu blockieren. Dies ist sehr hoch empfohlen, aber nicht erforderlich.* Für eine erweiterte ToR-Blockierung can SIE Folgendes tun:  ## Gewinn?