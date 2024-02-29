---
title: "Bouw een winstgevende passief inkomen box met weinig krachtige hardware: Een gids"
draft: false
toc: true
date: 2023-02-07
description: "Leer hoe je een passief inkomen crypto miner met een Raspberry Pi of Intel NUC opzet, en verdien $10-$20 per maand per box met deze gids."
tags: ["Bouw een winstgevende passief inkomen box", "Hardware met laag vermogen", "Passief inkomen", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guide", "Hardwarevereisten", "OS Installatie", "Software-installatie", "Docker", "Automatische Docker Container Updates", "Ubuntu-server", "Ubuntu Desktop", "Raspbian", "Begroting", "USFF", "Kleine", "Mini", "Micro PC", "Technische ervaring", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Watchtower", "Bitping"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "een groene, printplaat in de vorm van een doos met daarop internetconnectiviteitssymbolen als draden."
coverCaption: ""
---

**Bouw een winstgevende passief inkomen box met laag vermogen hardware: Een gids**
Veel mensen zijn tegenwoordig bezig met cryptomijnbouw en miners met een laag vermogen, zoals helium miners. Die zijn geweldig en zo, maar ze verdienen niet zo veel meer en ze zijn gericht op één soort verdienen. Vandaag gaan we een laag aangedreven passief inkomen box bouwen die overal van $10-$20 per maand per box en residentiële IP verdient.

*Als je de mogelijkheid hebt om deze box op te zetten op een gastnetwerk of, nog beter, een gescheiden VLAN, doe dat dan. Hoewel dit een beveiligingsblog is, kunnen we niet uitgaan van ieders beveiligingszorgen en risicotolerantie.*

## Hardware vereisten:
Een van de volgende is vereist. We hebben eigenlijk elke efficiënte computer met laag vermogen nodig die we te pakken kunnen krijgen. Elke Raspberry PI, Intel NUC, of soortgelijke is goed genoeg. Ze hoeven niet zo krachtig te zijn. Ik raad je wel aan om minstens 32g-64g opslagruimte te hebben, 4g ram en minstens 2 cpu threads. Hiervoor mikken we op een budget van ongeveer $100-$200 voor hardware, maar ga gerust hoger als dat past bij je behoeften. Ons doel is een gemiddeld vermogen van ongeveer 25w.
### Raspberry Pi:
Moeilijk te krijgen tegenwoordig, maar ze zijn super laag vermogen en zijn vrij aanpasbaar. Voor info over hoe raspian te installeren op uw Raspberry PI
-[Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
-[GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
-[GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Er zijn veel verschillende modellen. Voel je vrij om een nieuwere te kiezen.
-[Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
-[Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
-[Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Elke USFF/Tiny/Mini/Micro PC:
-[Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
-[Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Elke minipc met Intel N5100 of gelijkwaardig.
Voor super laag vermogen Raspberry Pi equivalent maar op x64 platform.
-[Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
-[TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## OS Installatie:
We gaan hier niet in op de technische details van de installatie van een besturingssysteem. Maar hier zijn enkele goede bronnen om u op weg te helpen
### Raspbian:
-[Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
-[The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
-[Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
-[Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
-[Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Software Installatie:
Dit wordt een langere sectie. We gaan docker opzetten en dan via docker automatische docker container updates instellen en meerdere docker containers installeren. We gaan er ook van uit dat je ubuntu server gebruikt, maar de commando's voor ubuntu server, ubuntu desktop en raspbian zouden allemaal hetzelfde moeten zijn.

*Voor dit gedeelte gaan we uit van enige technische basiservaring en dat je je besturingssysteem al hebt geïnstalleerd en weet hoe je in de terminal moet komen.*

### Updates installeren:
We willen er eerst zeker van zijn dat ons systeem volledig up-to-date is:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Docker installeren:
We moeten alle bestaande versies die met het os worden meegeleverd verwijderen en de nieuwste van Docker's repo zelf installeren.
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

### Installeer Watchtower:
Deze docker container update automatisch al je docker containers naar de nieuwste images op een regelmatig interval en ruimt oude (stale) images op.
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Installeer Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping biedt u de mogelijkheid om uitbetaald te worden in Solana voor het ter beschikking stellen van een node voor bedrijven om lichtgewicht netwerktests uit te voeren vanuit uw netwerk.
Dit is gemiddeld ongeveer 0,1 cent per dag per node. Niet veel weet ik, maar het heeft potentieel en uitbetalingen zijn gemakkelijk.

#### Maak een account aan:
Maak een account aan op[bitping.com](https://bitping.com)

#### Installeer de docker container:
Stap 1. Voer eerst deze commando's uit terwijl het u door het opzetten van uw container leidt en u vraagt om in te loggen.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Druk op CTRL+C op uw toetsenbord om de container te verlaten na het aanmelden met uw Bitping-account.

Stap 2. Voer deze opdracht uit om de container op de achtergrond te behouden
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Earn App installeren:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/GCL9QzB5)

Verdien app laat je je internet delen als VPN service voor een verrassend bedrag aan beloningen. Gemiddeld ongeveer $5 maand per node per residentieel IP. Biedt uitbetalingen aan via paypal en amazon gift cards.

#### Maak een Earn App account aan:
Maak een account aan bij[earnapp.com](https://earnapp.com/i/GCL9QzB5)
*Waarschuwing, vereist een google account*

#### Installeer de niet docker versie van de app om je UUID te krijgen:
Zorg ervoor dat je de installatie ongedaan maakt nadat je je UUID hebt gekregen, anders draai je het twee keer op dezelfde host en zonder automatische updates.
-[Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Installeer de docker container:
Wijzig de string voordat je hem in je terminal plakt. U moet uw earn app UUID opgeven.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Video Tutorial:
{{< youtube id="tt499o0OjGU" >}}

### Installeer Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/HONEY9149D)

Honey Gain laat u uw internet delen als VPN-dienst voor een verrassend bedrag aan beloningen. Gemiddeld ongeveer $5 per maand per node per residentieel IP. Uitbetalingen kunnen ingewikkeld zijn. Lees u verder in voordat u besluit deze container te gebruiken

#### Maak een Honey Gain Account aan:
Maak een account aan bij[honeygain.com](https://r.honeygain.me/HONEY9149D)

#### Installeer de Docker Container:
Wijzig de string met de voor de hand liggende e-mail, wachtwoord en apparaatnaam voordat u deze in de terminal plakt
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Alternatieve instructies voor Raspberry Pi
-[How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Video Tutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Installeer PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=sos)
Pawns app, opnieuw vergelijkbaar met de anderen hier vermeld, biedt u aan te betalen voor het delen van uw internet. Minimum uitbetaling is $5. Gemiddelde uitbetaling is $0.50 per maand per node per IP.

#### Maak een PawnsApp account aan:
Maak een account aan op[https://pawns.app](https://pawns.app/?r=sos)

#### Installeer de Docker Container:

Wijzig het volgende met uw e-mail, wachtwoord, apparaatnaam en apparaat-id voordat u het naar uw terminal kopieert.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Installeer Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Vergelijkbaar met andere aanbiedingen hier. Minimum $20 uitbetaling. Uitbetalingen kunnen ingewikkeld zijn. Onderzoek zelf of je deze dienst wilt gebruiken. Uitbetalingen gemiddeld ongeveer $1 per node per doos per maand.

#### Maak een Repocket Account aan:
Maak een account aan bij[repocket.co](https://link.repocket.co/raqc) en pak je api-sleutel van je dashboard.
#### Installeer de Docker Container:
Wijzig de volgende regel met uw e-mail en api-sleutel voordat u deze in uw terminal plakt.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Video Tutorial:
{{< youtube id="171gWknfAbY" >}}

### Installeer Traff Monetizer:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Vergelijkbaar met EarnApp en HoneyGain, TraffMonetizer betaalt u om uw internet te delen. Gemiddeld ongeveer $2 per maand per node per IP. Biedt alleen uitbetalingen in BTC.

#### Maak uw Traff Monetizer account aan:
Maak uw account aan op[https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Zodra u in het dashboard bent, noteert u uw aanvraag-token.

#### Installeer de Docker Container:
Kopieer de volgende string en voeg uw token toe dat u van het dashboard hebt gekregen voordat u het in uw terminal plakt.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli_v2 start accept --token
```

### Installeer Mysterie:
[Mysterium](https://www.mysterium.network/) is een gedecentraliseerde VPN en webscraping dienst gebouwd op de Etherium en Polygon blockchains.
Betalingen gaan gemiddeld van $1-$20 per maand, afhankelijk van meerdere factoren per node per IP. Kosten $1.XX om een node te activeren. Uitbetalingen in MYST token.


#### Installeer de Docker Container:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Stel de Docker-container in:
Ga naar http://"nodeip"/#/dashboard door "nodeip" te vervangen door het IP-adres van uw node. U kunt dit vinden door "ifconfig" in de terminal te typen.

Klik op "start node setup".

Geef het adres op van de ERC20 wallet waarin je beloningen wilt ontvangen en klik op "next". Je kunt een standaard Ethereum adres gebruiken zoals een van je MetaMask adressen.

Typ een wachtwoord in dat je zult gebruiken om in de toekomst toegang te krijgen tot dit node dashboard. Vink het vakje aan om het knooppunt in je netwerk te claimen.

Klik op de "Get it here" link en zoek je API sleutel. Kopieer hem. Ga terug en plak hem. Klik op "Opslaan en doorgaan".

#### Port Forwarding:
We kunnen niet voor ieders specifieke hardware beschrijven hoe je poort doorstuurt. Hier zijn enkele bronnen om te leren hoe port forwarding werkt.
-[PortForward.com](https://portforward.com/)
-[Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Docker Containers automatisch herstarten bij het opstarten:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Optionele configuraties:
-[Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
-[Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Verhoog de veiligheid door malware en trackers te blokkeren.
Forceer alle dns-verzoeken naar Cloudflares dns ter bescherming tegen malware en tracking.
Blokkeer ook DNS/HTTPS verzoeken.
*Als u een meer geavanceerde router of firewall op het netwerk hebt, kunt u zelfs pakketten zoals snort/securita gebruiken om meer geavanceerde regels te maken om bekende slecht handelende IP's, tor-toegang, torrents, p2p-verkeer in het algemeen, enz. te blokkeren. Dit wordt ten zeerste aanbevolen, maar is niet verplicht.*
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
Voor meer geavanceerde ToR-blokkering kunt u het volgende doen:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Winst?