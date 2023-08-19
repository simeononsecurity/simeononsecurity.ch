---
title: "Creeu una caixa d'ingressos passius rendibles amb maquinari de baixa potència: una guia"
draft: false
toc: true
date: 2023-02-07
description: "Apreneu a configurar un miner criptogràfic d'ingressos passius de baixa potència mitjançant un Raspberry Pi o Intel NUC i guanyeu entre 10 i 20 dòlars al mes per caixa amb aquesta guia"
tags: ["Construeix una caixa d'ingressos passius rendibles", "Maquinari de baixa potència", "Renda passiva", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Guia", "Requisits de maquinari", "Instal·lació del SO", "Instal·lació de programari", "Docker", "Actualitzacions automàtiques de contenidors Docker", "Servidor Ubuntu", "Escriptori Ubuntu", "Raspbian", "Pressupost", "USFF", "Petit", "Mini", "Micro PC", "Experiència tècnica", "EarnApp", "MIST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Torre de vigilància", "Picant", "Actualitzacions de Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "actualitzacions fora de línia", "repositori local", "memòria cau", "configuració del servidor", "configuració del client", "mirall apte", "debmirror", "crearrepo", "apt-cacher-ng", "yum-cron", "Actualitzacions del sistema Linux", "actualitzacions de paquets fora de línia", "actualitzacions de programari fora de línia", "dipòsit local de paquets", "memòria cau de paquets locals", "actualitzacions fora de línia de Linux", "gestionar les actualitzacions fora de línia", "mètodes d'actualització fora de línia", "manteniment del sistema fora de línia", "Actualitzacions del servidor Linux", "Actualitzacions del client Linux", "gestió de programari fora de línia", "gestió de paquets fora de línia", "estratègies d'actualització", "Actualitzacions de seguretat de Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "una placa de circuit verda amb forma de caixa amb símbols de connectivitat a Internet com a cables connectats."
coverCaption: ""
---

**Construeix una caixa d'ingressos passius rendibles amb maquinari de baixa potència: una guia**
Molta gent en aquests dies s'interessa per la mineria criptogràfica i els miners de baixa potència, com ara els miners d'heli. Són genials i tot, però ja no guanyen gaire i es centren en un tipus de guanys. Avui construirem una caixa d'ingressos passius de baixa potència que guanyi entre 10 i 20 dòlars al mes per caixa i IP residencial.

*Si teniu la possibilitat de configurar aquesta caixa en una xarxa de convidats o, encara millor, en una VLAN segregada, feu-ho. Tot i que aquest és un bloc de seguretat, no podem assumir les preocupacions de seguretat i la tolerància al risc de tothom.*

## Requisits de maquinari:
Es requereix un dels següents. Bàsicament només necessitem qualsevol ordinador eficient i de poca potència que puguem tenir a les nostres mans. Qualsevol Raspberry PI, Intel NUC o similar ho farà. No han de ser tan poderosos. Tanmateix, us recomanaré que tingueu almenys 32 g-64 g d'emmagatzematge, 4 g de memòria RAM i almenys 2 fils de CPU. Per a això, apuntarem a un pressupost d'uns 100 a 200 dòlars per al maquinari, però no dubteu a augmentar si s'adapta a les vostres necessitats. El nostre objectiu de potència és aprox. 25w de mitjana.
### Raspberry Pi:
Difícil d'aconseguir aquests dies, però tenen una potència molt baixa i són bastant personalitzables. Per obtenir informació sobre com instal·lar raspian al vostre Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Gran varietat de models que hi ha. No dubteu a triar-ne un de més nou.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Qualsevol PC USFF/Tiny/Mini/Micro:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Qualsevol Mini PC amb Intel N5100 o similar
Per a l'equivalent a Raspberry Pi de potència molt baixa, però a la plataforma x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instal·lació del sistema operatiu:
No entrarem en els detalls tècnics de com instal·lar un sistema operatiu aquí. Tanmateix, aquí teniu alguns recursos fantàstics per començar
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instal·lació de programari:
Aquesta serà una secció més llarga. Configurarem Docker i després mitjançant Docker configurarem actualitzacions automàtiques de contenidors Docker i instal·larem diversos contenidors Docker. També suposem que esteu utilitzant el servidor ubuntu, però les ordres per al servidor ubuntu, l'escriptori ubuntu i el raspbian haurien de ser les mateixes.

*Per a aquesta secció suposem una experiència tècnica bàsica i que ja tens instal·lat el teu sistema operatiu i saps com entrar al terminal.*

### Instal·lació d'actualitzacions:
Primer volem assegurar-nos que tenim el nostre sistema totalment actualitzat:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Instal·lació de Docker:
Hem de desinstal·lar totes les versions existents que vinguin preempaquetades amb el sistema operatiu i instal·lar la darrera versió del repo de Docker.
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

### Instal·leu Watchtower:
Aquest contenidor Docker actualitza automàticament tots els vostres contenidors Docker a les imatges més recents en un interval regular i neteja imatges antigues (antigues).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Instal·leu Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping us ofereix la possibilitat de rebre un pagament a Solana per proporcionar un node perquè les empreses executin proves de xarxa lleugeres des de la vostra xarxa.
Això fa una mitjana d'uns 0,1 cèntims per dia per node. No sé gaire, però té potencial i els pagaments són fàcils.

#### Crear un compte:
Creeu un compte a [bitping.com](https://bitping.com)

#### Instal·leu el contenidor docker:
Pas 1. Executeu aquestes ordres primer mentre us guiarà a través de la configuració del contenidor i us demana que inicieu la sessió.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Premeu CTRL+C al vostre teclat per escapar del contenidor després d'iniciar la sessió amb el vostre compte de bitping.

Pas 2. Executeu aquesta ordre per mantenir el contenidor en segon pla
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Instal·la l'aplicació Earn:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

L'aplicació Earn us permet compartir la vostra Internet com a servei VPN per obtenir una sorprenent quantitat de recompenses. Una mitjana d'uns 5 dòlars al mes per node per IP residencial. Ofereix pagaments mitjançant PayPal i targetes de regal d'Amazon.

#### Creeu un compte d'aplicació Earn:
Creeu un compte a [earnapp.com](https://earnapp.com/i/c1dllee)
*Avís, requereix un compte de Google*

#### Instal·leu la versió no acobladora de l'aplicació per obtenir el vostre UUID:
Assegureu-vos de desinstal·lar-lo després d'obtenir el vostre UUID, en cas contrari, l'acabareu executant dues vegades al mateix amfitrió i sense actualitzacions automàtiques.
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Instal·leu el contenidor docker:
Modifiqueu la cadena abans d'enganxar-la al vostre terminal. Heu d'especificar l'UUID de l'aplicació per guanyar.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Videotutorial:
{{< youtube id="tt499o0OjGU" >}}

### Instal·leu Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain us permet compartir la vostra Internet com a servei VPN per obtenir una sorprenent quantitat de recompenses. Una mitjana d'uns 5 dòlars al mes per node per IP residencial. Els pagaments poden ser complicats. Llegiu-lo més abans de decidir-vos a utilitzar aquest contenidor

#### Creeu un compte de guany de mel:
Creeu un compte a [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Instal·leu el contenidor Docker:
Modifiqueu la cadena amb el correu electrònic, la contrasenya i el nom del dispositiu evidents abans d'enganxar-la al terminal
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Instruccions alternatives per a Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Videotutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Instal·leu PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
L'aplicació Pawns, de nou similar a les altres que es mostren aquí, us ofereix pagar per compartir la vostra Internet. El pagament mínim és de 5 $. El pagament mitjà és de 0,50 dòlars al mes per node per IP.

#### Creeu un compte de PawnsApp:
Creeu un compte a [https://pawns.app](https://pawns.app/?r=2092882)

#### Instal·leu el contenidor Docker:

Modifiqueu el següent amb el vostre correu electrònic, contrasenya, nom del dispositiu i identificador del dispositiu abans de copiar-lo al vostre terminal.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Instal·leu Peer 2 Profit:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://dashboard.peer2profit.app/register-with-referral/16538445386293aa3aaec4e?lang=en)

De manera similar a EarnApp i HoneyGain, Peer2Profit comparteix la vostra Internet amb finalitats VPN i Scraping. Guanya aproximadament 1 $ al mes per node per IP.
Ofereix una varietat de pagaments, com ara ordres postals, BTC, LTC, LTC, MATIC, etc.

#### Creeu un compte de beneficis Peer 2:
Creeu un compte a [peer2profit.com](https://dashboard.peer2profit.app/register-with-referral/16538445386293aa3aaec4e?lang=en)

#### Instal·leu el contenidor Docker:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### Videotutorial:
{{< youtube id="J_rSV5N8aQk" >}}


### Instal·leu Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Similar a altres ofertes aquí. Pagament mínim de 20 $. Els pagaments poden ser complicats. Investigueu vosaltres mateixos per veure si voleu utilitzar aquest servei. Els pagaments tenen una mitjana d'1 $ per node per caixa al mes.

#### Crea un compte de reembossament:
Creeu un compte a [repocket.co](https://link.repocket.co/raqc) i agafeu la vostra clau API del vostre tauler.
#### Instal·leu el contenidor Docker:
Modifiqueu la línia següent amb el vostre correu electrònic i la clau API abans d'enganxar-la al vostre terminal.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Videotutorial:
{{< youtube id="171gWknfAbY" >}}

### Instal·leu el monetitzador de trànsit:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

De manera similar a EarnApp i HoneyGain, TraffMoetizer et paga per compartir la teva Internet. Una mitjana d'uns 2 dòlars al mes per node per IP. Només ofereix pagaments en BTC.

#### Creeu el vostre compte de monetitzador de trànsit:
Creeu el vostre compte a [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Quan entreu al tauler, anoteu el vostre testimoni d'aplicació.

#### Instal·leu el contenidor Docker:
Copieu la cadena següent i afegiu el testimoni que heu obtingut del tauler abans d'enganxar-lo al vostre terminal.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Instal·leu Mysterium:
[Mysterium](https://www.mysterium.network/) és un servei descentralitzat de VPN i webscraping basat en les cadenes de blocs Etherium i Polygon.
Els pagaments tenen una mitjana d'entre 1 i 20 dòlars al mes, depenent de diversos factors per node i IP. Costa 1,XX $ configurar un node per a l'activació. Pagaments en testimoni MYST.


#### Instal·leu el contenidor Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Configura el contenidor Docker:
Aneu a http://"nodeip"/#/dashboard substituint "nodeip" per l'adreça IP del vostre node. Podeu trobar-ho escrivint "ifconfig" al terminal.

Feu clic a "iniciar la configuració del node".

Passeu l'adreça de la cartera ERC20 en què voleu rebre recompenses i feu clic a "següent". Podeu utilitzar una adreça estàndard d'Ethereum com una de les vostres adreces de MetaMask.

Escriviu una contrasenya que utilitzareu per accedir a aquest tauler de nodes en el futur. Marqueu la casella de selecció per reclamar el node de la vostra xarxa.

Feu clic a l'enllaç "Obteniu-ho aquí" i cerqueu la vostra clau API. Copia-ho. Torneu enrere i enganxeu-lo. Feu clic a "Desa i continua".

#### Reenviament de ports:
No podem descriure com es pot reenviar el port per al maquinari específic de cadascú. Aquí teniu alguns recursos per aprendre a portar endavant.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Reinici automàtic dels contenidors Docker a l'arrencada:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configuracions opcionals:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Augmenta la seguretat bloquejant programari maliciós i rastrejadors.
Força totes les sol·licituds dns al programari maliciós de Cloudflares i als dns de protecció de seguiment.
A més, bloquegeu les sol·licituds DNS/HTTPS.
*Si teniu un encaminador o un tallafocs més avançats a la xarxa, fins i tot podeu utilitzar paquets com snort/securita per crear regles més avançades per bloquejar les IP conegudes que actuen malament, l'accés a tor, torrents, trànsit p2p en general, etc. Això és molt important. suggerit però no obligatori.*
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
Per a un bloqueig de ToR més avançat, podeu fer el següent:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Guanys?