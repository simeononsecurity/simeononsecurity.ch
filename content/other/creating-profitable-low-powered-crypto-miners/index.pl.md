---
title: "Zbuduj dochodową skrzynkę dochodu pasywnego za pomocą sprzętu o małej mocy: Poradnik"
draft: false
toc: true
date: 2023-02-07
description: "Dowiedz się, jak skonfigurować nisko zasilany pasywny dochód crypto miner przy użyciu Raspberry Pi lub Intel NUC, i zarabiać $10-$20 miesięcznie na pudełko z tym przewodnikiem"
tags: ["Zbuduj dochodową skrzynkę dochodu pasywnego", "Sprzęt o małej mocy", "Dochód pasywny", "Crypto Miner", "Raspberry Pi", "Intel NUC", "Przewodnik", "Wymagania sprzętowe", "Instalacja systemu operacyjnego", "Instalacja oprogramowania", "Docker", "Automatyczne aktualizacje kontenerów Docker", "Ubuntu Server", "Pulpit Ubuntu", "Raspbian", "Budżet", "USFF", "Tiny", "Mini", "Micro PC", "Doświadczenie techniczne", "EarnApp", "MYST", "Peer2Profit", "HoneyGain", "TraffMonitizer", "Strażnica", "Bitping"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "zielona, płytka w kształcie pudełka z symbolami łączności internetowej w postaci podłączonych do niej przewodów."
coverCaption: ""
---

**Zbuduj dochodową skrzynkę dochodu pasywnego z niskim sprzętem: A Guide**
Wiele osób w dzisiejszych czasach zajmuje się wydobywaniem kryptowalut i niską mocą górników, takich jak górnicy helu. Są one świetne i wszystkie, ale nie zarabiają już tak dużo i skupiają się na jednym rodzaju zarabiania. Dzisiaj będziemy budować niską zasilaną skrzynkę dochodu pasywnego, która zarabia gdziekolwiek od $10-$20 miesięcznie na skrzynkę i IP mieszkalne.

*Jeśli masz możliwość ustawienia tego pudełka w sieci dla gości lub, nawet lepiej, posegregowane VLAN, zrobić to. Chociaż jest to blog o bezpieczeństwie, nie możemy zakładać, że każdy ma obawy o bezpieczeństwo i tolerancję ryzyka.

## Wymagania sprzętowe:
Wymagany jest jeden z następujących elementów. W zasadzie potrzebujemy po prostu jakiegokolwiek wydajnego i nisko zasilanego komputera, który możemy dostać w swoje ręce. Każdy Raspberry PI, Intel NUC, lub podobny zrobi to. Nie muszą być one aż tak potężne. Jednak polecam mieć co najmniej 32g-64g pamięci, 4g ram, i co najmniej 2 wątki cpu. W tym celu będziemy celować w budżet około $100-$200 na sprzęt, ale nie krępuj się iść wyżej, jeśli odpowiada to twoim potrzebom. Nasz docelowy pobór mocy to średnio ok. 25W.
### Raspberry Pi:
Ciężko dostać się do tych dni, ale są one super niską mocą i są dość konfigurowalne. Aby dowiedzieć się jak zainstalować raspian na Raspberry PI
-[Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
-[GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
-[GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
Szeroki wybór modeli. Zapraszamy do wybrania nowszego.
-[Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
-[Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
-[Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### Każdy USFF/Tiny/Mini/Micro PC:
-[Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
-[Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Dowolny Mini PC z Intel N5100 lub podobny
Dla super low power Raspberry Pi odpowiednik ale na platformie x64.
-[Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
-[TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## Instalacja systemu operacyjnego:
Nie będziemy wchodzić w szczegóły techniczne jak zainstalować system operacyjny tutaj. Jednak tutaj jest kilka świetnych źródeł, abyś mógł zacząć
### Raspbian:
-[Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
-[The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### Ubuntu:
-[Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
-[Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
-[Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## Instalacja oprogramowania:
To będzie dłuższa sekcja. Zamierzamy skonfigurować docker, a następnie poprzez docker ustawimy automatyczne aktualizacje kontenerów docker i zainstalujemy wiele kontenerów docker. Zakładamy również, że używasz ubuntu server, jednak polecenia dla ubuntu server, ubuntu desktop i raspbian powinny być takie same.

*W tej sekcji zakładamy podstawowe doświadczenie techniczne oraz to, że masz już zainstalowany system operacyjny, jak również wiesz jak dostać się do terminala.

### Instalowanie aktualizacji:
Najpierw chcemy się upewnić, że mamy nasz system w pełni aktualny:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### Instalacja Dockera:
Musimy odinstalować wszelkie istniejące wersje, które przychodzą prepakowane z os i samodzielnie zainstalować najnowsze z repo Dockera.
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

### Zainstaluj Watchtower:
Ten kontener docker automatycznie aktualizuje wszystkie twoje kontenery docker do najnowszych obrazów w regularnym odstępie czasu i czyści stare (nieświeże) obrazy.
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

Bitping oferuje możliwość uzyskania wypłaty w Solanie za udostępnienie węzła dla firm w celu przeprowadzenia lekkich testów sieciowych z Twojej sieci.
Wynosi to średnio około 0,1 centa dziennie na węzeł. Nie jest to dużo wiem, ale ma potencjał i wypłaty są łatwe.

#### Załóż konto:
Załóż konto na.[bitping.com](https://bitping.com)

#### Zainstaluj kontener docker:
Krok 1. Uruchom najpierw te polecenia, ponieważ prowadzi Cię przez konfigurację kontenera i prosi o zalogowanie się.
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

Naciśnij CTRL+C na klawiaturze, aby uciec z kontenera po zalogowaniu się na konto bitpingowe.

Krok 2. Uruchom to polecenie, aby wytrwać kontener w tle
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Zainstaluj Earn App:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Earn app pozwala Ci udostępnić swój internet jako usługę VPN za zaskakującą ilość nagród. Averages about $5 month per node per residential IP. Offers payouts via paypal and amazon gift cards.

#### Create an Earn App Account:
Utwórz konto na.[earnapp.com](https://earnapp.com/i/c1dllee)
*Ostrzeżenie, wymaga konta google*

#### Zainstaluj wersję aplikacji bez dockera, aby uzyskać swój UUID:
Pamiętaj, aby odinstalować po uzyskaniu identyfikatora UUID, w przeciwnym razie skończysz uruchamiając go dwukrotnie na tym samym hoście i bez automatycznych aktualizacji.
-[Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### Zainstaluj kontener docker:
Zmodyfikuj ciąg przed wklejeniem do swojego terminala. Musisz określić swój identyfikator UUID aplikacji zarobkowej.
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### Video Tutorial:
{{< youtube id="tt499o0OjGU" >}}

### Zainstaluj Honey Gain:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

Honey Gain pozwala Ci udostępnić swój internet jako usługę VPN za zaskakującą ilość nagród. Averages about $5 month per node per residential IP. Wypłaty mogą być skomplikowane. Read into it further before deciding to use this container

#### Create a Honey Gain Account:
Utwórz konto na stronie[honeygain.com](https://r.honeygain.me/DAVID07A75)

#### Zainstaluj Docker Container:
Zmodyfikuj ciąg znaków z oczywistym e-mailem, hasłem i nazwą urządzenia przed wklejeniem do terminala
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### Alternatywne instrukcje dla Raspberry Pi
-[How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### Video Tutorial:
{{< youtube id="Wd11M0nSy1k" >}}

### Zainstaluj PawnsApp:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Pawns app, ponownie podobne do innych wymienionych tutaj oferują zapłacić za dzielenie się swoim internecie. Minimalna wypłata to 5$, średnia wypłata to 0,50$ miesięcznie za węzeł na IP.

#### Create a PawnsApp Account:
Utwórz konto na.[https://pawns.app](https://pawns.app/?r=2092882)

#### Zainstaluj Docker Container:

Zmodyfikuj poniższe za pomocą swojego e-maila, hasła, nazwy urządzenia i id urządzenia przed skopiowaniem do swojego terminala.
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### Zainstaluj Peer 2 Profit:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://p2pr.me/16538445386293aa3aaec4e)

Podobnie jak EarnApp i HoneyGain, Peer2Profit dzieli się twoim internetem dla celów VPN i Scrapingu. Zarabia około $1 miesięcznie na węzeł na IP.
Oferuje różnorodne wypłaty, w tym przekazy pieniężne, BTC, LTC, MATIC itp.

#### Create a Peer 2 Profit Account:
Załóż konto na.[peer2profit.com](https://p2pr.me/16538445386293aa3aaec4e)

#### Zainstaluj Docker Container:
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
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

Podobne do innych ofert tutaj. Minimalna wypłata 20$. Wypłaty mogą być skomplikowane. Zbadaj sam, aby zobaczyć, czy chcesz korzystać z tej usługi. Wypłaty średnio około $1 na węzeł na pudełko miesięcznie.

#### Utwórz konto Repocket:
Załóż konto na.[repocket.co](https://link.repocket.co/raqc) i złapać swój klucz api z pulpitu nawigacyjnego.
#### Zainstaluj kontener Docker:
Zmodyfikuj następującą linię z twoim e-mailem i kluczem api przed wklejeniem do terminala.
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### Video Tutorial:
{{< youtube id="171gWknfAbY" >}}

### Zainstaluj Traff Monetizer:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

Podobnie jak EarnApp i HoneyGain, TraffMonetizer płaci ci za udostępnianie internetu. Średnio około 2$ miesięcznie za węzeł na IP. Oferuje tylko wypłaty w BTC.

#### Utwórz swoje konto Traff Monetizer:
Utwórz swoje konto na.[https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
Po wejściu do dashboardu zanotuj swój token aplikacji.

#### Zainstaluj kontener Docker:
Skopiuj następujący ciąg i dołącz swój token, który otrzymałeś z pulpitu nawigacyjnego przed wklejeniem do swojego terminala.

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### Install Mystery:
[Mysterium](https://www.mysterium.network/) to zdecentralizowany VPN i usługa webscrapingu zbudowana na blockchainach Etherium i Polygon.
Płatności wynoszą średnio od $1-$20 miesięcznie w zależności od wielu czynników na węzeł na IP. Kosztuje $1.XX, aby ustawić węzeł do aktywacji. Wypłaty w tokenach MYST.


#### Zainstaluj kontener Docker:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### Skonfiguruj kontener Docker:
Przejdź do http://"nodeip"/#/dashboard zastępując "nodeip" adresem IP Twojego węzła. Możesz to znaleźć wpisując "ifconfig" w terminalu.

Kliknij "start node setup".

Wklej adres portfela ERC20, w którym chcesz otrzymywać nagrody i kliknij "next". Możesz użyć standardowego adresu Ethereum, jak jeden z twoich adresów MetaMask.

Wpisz hasło, którego będziesz używać, aby uzyskać dostęp do tego pulpitu nawigacyjnego węzła w przyszłości. Zaznacz pole wyboru, aby zażądać węzła w swojej sieci.

Kliknij link "Pobierz tutaj" i znajdź swój klucz API. Skopiuj go. Wróć i wklej go. Kliknij "Zapisz i kontynuuj".

#### Port Forwarding:
Nie możemy opisać, jak przekierować porty dla każdego konkretnego sprzętu. Oto kilka źródeł, aby dowiedzieć się, jak przekierować porty.
-[PortForward.com](https://portforward.com/)
-[Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### Auto Restart Docker Containers on Boot:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### Konfiguracje opcjonalne:
-[Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
-[Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### Zwiększ bezpieczeństwo, blokując złośliwe oprogramowanie i trackery.
Wymuś wszystkie żądania dns do Cloudflares malware i tracking protection dns.
Ponadto blokuj żądania DNS/HTTPS.
*Jeśli masz bardziej zaawansowany router lub firewall w sieci, możesz nawet użyć pakietów takich jak snort/securita, aby stworzyć bardziej zaawansowane reguły, aby zablokować znane złe działające IP, dostęp do tor, torrenty, ruch p2p w ogóle, itp. Jest to wysoce sugerowane, ale nie wymagane.*
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
W przypadku bardziej zaawansowanego blokowania ToR możesz wykonać następujące czynności:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## Zysk?