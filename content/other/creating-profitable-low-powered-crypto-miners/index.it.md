---
title: "Costruisci una redditizia scatola del reddito passivo con hardware a bassa potenza: una guida"
draft: false
toc: true
date: 2023-02-07
description: "Scopri come impostare un crypto miner a reddito passivo a bassa potenza utilizzando un Raspberry Pi o Intel NUC e guadagna $ 10- $ 20 al mese per scatola con questa guida"
tags: ["Costruisci una redditizia casella di reddito passivo", "Hardware a bassa potenza", "Reddito passivo", "Minatore di criptovalute", "Lampone Pi", "Intel NUC", "Guida", "Requisiti hardware", "Installazione del sistema operativo", "Installazione software", "Docker", "Aggiornamenti automatici del contenitore Docker", "Server Ubuntu", "Desktop Ubuntu", "Raspbian", "Bilancio", "USFF", "Minuscolo", "Mini", "MicroPC", "Esperienza tecnica", "GuadagnaApp", "MIST", "Peer2Profit", "HoneyGain", "Monitor di traffico", "Torre di guardia", "Mordere", "Aggiornamenti Linux", "Ubuntu", "Debian", "CentOS", "REL", "aggiornamenti offline", "deposito locale", "cache", "configurazione del server", "configurazione del cliente", "apt-specchio", "debmirror", "createrepo", "apt-cacher-ng", "yum-cron", "Aggiornamenti del sistema Linux", "aggiornamenti dei pacchetti offline", "aggiornamenti software offline", "repository di pacchetti locale", "cache dei pacchetti locale", "aggiornamenti Linux offline", "gestire gli aggiornamenti offline", "metodi di aggiornamento offline", "manutenzione del sistema offline", "Aggiornamenti del server Linux", "Aggiornamenti del client Linux", "gestione del software offline", "gestione dei pacchetti offline", "aggiornare le strategie", "Aggiornamenti di sicurezza Linux"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "un circuito stampato verde a forma di scatola con simboli di connettività Internet come fili collegati ad esso."
coverCaption: ""
---

**Costruisci un reddito passivo redditizio con hardware a bassa potenza: una guida**
Molte persone in questi giorni sono interessate al mining di criptovalute e ai minatori a bassa potenza come i minatori di elio. Questi sono fantastici e tutti, ma non guadagnano più molto e sono concentrati su un tipo di guadagno. Oggi costruiremo una scatola di reddito passivo a bassa potenza che guadagna ovunque da $ 10 a $ 20 al mese per scatola e IP residenziale.

*Se hai la possibilità di configurare questa casella su una rete ospite o, ancora meglio, su una VLAN segregata, fallo. Anche se questo è un blog sulla sicurezza, non possiamo dare per scontato i problemi di sicurezza e la tolleranza al rischio di tutti.*

## Requisiti hardware:
È richiesto uno dei seguenti. Fondamentalmente abbiamo solo bisogno di qualsiasi computer efficiente e di bassa potenza su cui possiamo mettere le mani. Va bene qualsiasi Raspberry PI, Intel NUC o simili. Non devono essere così potenti. Tuttavia ti consiglierò di avere almeno 32g-64g di spazio di archiviazione, 4g di ram e almeno 2 thread della cpu. Per questo punteremo a un budget di circa $ 100- $ 200 per l'hardware, ma sentiti libero di aumentare se soddisfa le tue esigenze. Il nostro obiettivo di potenza è di ca. 25w di media.
### Lampone Pi:
Difficile da ottenere in questi giorni, ma sono a bassissima potenza e sono abbastanza personalizzabili. Per informazioni su come installare raspian sul tuo Raspberry PI
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Nuc Intel:
Ampia varietà di modelli là fuori. Sentiti libero di sceglierne uno nuovo.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Qualsiasi USFF/Piccolo/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Qualsiasi Mini PC con Intel N5100 o simili
Per Raspberry Pi a bassissima potenza equivalente ma su piattaforma x64.
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Installazione del sistema operativo:
Non entreremo nei dettagli tecnici di come installare un sistema operativo qui. Tuttavia, ecco alcune ottime risorse per iniziare
### Raspbian:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
###Ubuntu:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Installazione software:
Questa sarà una sezione più lunga. Stiamo per configurare la finestra mobile e quindi tramite la finestra mobile imposteremo gli aggiornamenti automatici del contenitore della finestra mobile e installeremo più contenitori della finestra mobile. Supponiamo inoltre che tu stia utilizzando Ubuntu Server, tuttavia i comandi per Ubuntu Server, Ubuntu Desktop e Raspbian dovrebbero essere tutti uguali.

*Per questa sezione presumiamo una certa esperienza tecnica di base e che tu abbia già installato il tuo sistema operativo e sappia come accedere al terminale.*

### Installazione degli aggiornamenti:
Per prima cosa vogliamo essere sicuri di avere il nostro sistema completamente aggiornato:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Installazione di Docker:
Abbiamo bisogno di disinstallare tutte le versioni esistenti preconfezionate con il sistema operativo e installare le ultime dal repository di Docker.
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

### Installa Watchtower:
Questo contenitore docker aggiorna automaticamente tutti i contenitori docker alle immagini più recenti a intervalli regolari e ripulisce le immagini vecchie (obsolete).
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### Installa Bitping:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

Bitping ti offre la possibilità di essere pagato in Solana per fornire un nodo alle aziende per eseguire test di rete leggeri dalla tua rete.
Questa media è di circa 0,1 centesimi al giorno per nodo. Non molto lo so, ma ha un potenziale e le vincite sono facili.

#### Creare un account:
Crea un account su [bitping.com](https://bitping.com)

#### Installa il contenitore docker:
Passo 1. Esegui prima questi comandi mentre ti guida attraverso la configurazione del tuo contenitore e ti chiede di accedere.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Premi CTRL + C sulla tastiera per uscire dal contenitore dopo aver effettuato l'accesso con il tuo account bitping.

Passaggio 2. Eseguire questo comando per mantenere il contenitore in background
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Installa Guadagna App:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Guadagna app ti consente di condividere Internet come servizio VPN per una quantità sorprendente di premi. In media circa $ 5 al mese per nodo per IP residenziale. Offre pagamenti tramite paypal e buoni regalo Amazon.

#### Crea un account per l'app Guadagna:
Crea un account su [earnapp.com](https://earnapp.com/i/c1dllee)
*Attenzione, richiede un account Google*

#### Installa la versione non docker dell'app per ottenere il tuo UUID:
Assicurati di disinstallare dopo aver ottenuto il tuo UUID altrimenti finirai per eseguirlo due volte sullo stesso host e senza aggiornamenti automatici
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Installa il contenitore docker:
Modifica la stringa prima di incollarla nel tuo terminale. Devi specificare l'UUID dell'app di guadagno.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Tutorial video:
{{< youtube id="tt499o0OjGU" >}}

### Installa Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain ti consente di condividere Internet come servizio VPN per una quantità sorprendente di premi. In media circa $ 5 al mese per nodo per IP residenziale. I pagamenti possono essere complicati. Leggere ulteriormente prima di decidere di utilizzare questo contenitore

#### Crea un account Honey Gain:
Crea un account su [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Installa il contenitore Docker:
Modifica la stringa con l'ovvia e-mail, password e nome del dispositivo prima di incollarla nel terminale
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Istruzioni alternative per Raspberry Pi
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Tutorial video:
{{< youtube id="Wd11M0nSy1k" >}}

### Installa PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
L'app Pawns, sempre simile alle altre elencate qui, ti offre di pagarti per condividere la tua connessione Internet. La vincita minima è di $ 5. Il pagamento medio è di $ 0,50 al mese per nodo per IP.

#### Crea un account PawnsApp:
Crea un account su [https://pawns.app](https://pawns.app/?r=2092882)

#### Installa il contenitore Docker:

Modifica quanto segue con la tua e-mail, password, nome del dispositivo e ID del dispositivo prima di copiarli sul tuo terminale.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Installa profitto peer 2:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

Simile a EarnApp e HoneyGain, Peer2Profit condivide Internet per scopi VPN e Scraping. Guadagna circa $ 1 al mese per nodo per IP.
Offre una varietà di pagamenti inclusi vaglia postali, BTC, LTC, LTC, MATIC, ecc.

#### Crea un conto di profitto Peer 2:
Crea un account su [peer2profit.com](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

#### Installa il contenitore Docker:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### Tutorial video:
{{< youtube id="J_rSV5N8aQk" >}}


### Installa Repocket:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Simile ad altre offerte qui. Pagamento minimo di $ 20. I pagamenti possono essere complicati. Cerca tu stesso per vedere se desideri utilizzare questo servizio. I pagamenti sono in media di circa $ 1 per nodo per scatola al mese.

#### Crea un account Repocket:
Crea un account su [repocket.co](https://link.repocket.co/raqc) e prendi la tua chiave API dalla tua dashboard.
#### Installa il contenitore Docker:
Modifica la seguente riga con la tua e-mail e la chiave API prima di incollarla nel tuo terminale.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Tutorial video:
{{< youtube id="171gWknfAbY" >}}

### Installa Traff Monetizer:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Simile a EarnApp e HoneyGain, TraffMonetizer ti paga per condividere la tua connessione Internet. In media circa $ 2 al mese per nodo per IP. Offre solo pagamenti in BTC.

#### Crea il tuo account Monetizzatore di traffico:
Crea il tuo account su [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Una volta entrato nella dashboard, prendi nota del token dell'applicazione.

#### Installa il contenitore Docker:
Copia la seguente stringa e aggiungi il tuo token che hai ottenuto dalla dashboard prima di incollarlo nel tuo terminale.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Installa Mysterium:
[Mysterium](https://www.mysterium.network/) è una VPN decentralizzata e un servizio di webscraping basato sulle blockchain Etherium e Polygon.
I pagamenti vanno in media da $ 1 a $ 20 al mese a seconda di più fattori per nodo per IP. Costa $ 1,XX per impostare un nodo per l'attivazione. Pagamenti in token MYST.


#### Installa il contenitore Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Imposta il contenitore Docker:
Vai su http://"nodeip"/#/dashboard sostituendo "nodeip" con l'indirizzo IP del tuo nodo. Puoi trovarlo digitando "ifconfig" nel terminale.

Fare clic su "Avvia configurazione nodo".

Oltre l'indirizzo del portafoglio ERC20 in cui desideri ricevere i premi e fai clic su "Avanti". Puoi utilizzare un indirizzo Ethereum standard come uno dei tuoi indirizzi MetaMask.

Digita una password che utilizzerai per accedere a questo dashboard del nodo in futuro. SELEZIONA la casella di controllo per rivendicare il nodo nella tua rete.

Fai clic sul link "Prendilo qui" e trova la tua chiave API. Copialo. Torna indietro e incollalo. Fare clic su "Salva e continua".

#### Port forwarding:
Non possiamo descrivere come eseguire il port forwarding per l'hardware specifico di tutti. Ecco alcune risorse per imparare a eseguire il port forwarding.
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Riavvio automatico dei contenitori Docker all'avvio:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Configurazioni opzionali:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Aumenta la sicurezza bloccando malware e tracker.
Forza tutte le richieste dns al malware Cloudflares e al dns di protezione del tracciamento.
Inoltre, blocca le richieste DNS/HTTPS.
*Se disponi di un router o firewall più avanzato sulla rete, puoi persino utilizzare pacchetti come snort/securita per creare regole più avanzate per bloccare IP noti che agiscono male, accesso a tor, torrent, traffico p2p in generale, ecc. consigliato ma non obbligatorio.*
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
Per un blocco dei ToR più avanzato puoi procedere come segue:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Profitto?