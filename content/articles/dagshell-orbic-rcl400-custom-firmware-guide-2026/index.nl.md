---
title: "DagShell custom firmware voor Orbic RCL400: gids voor 2026"
date: 2026-05-28
lastmod: 2026-11-15
toc: true
draft: false
description: "Technische gids voor DagShell-firmware op de Orbic RCL400, met installatie, privacytools, wardriving en onderzoeksbeperkingen."
genre: ["Custom firmware", "Mobiele beveiliging", "Privacytools", "Netwerkbeveiliging", "Wardriving", "Penetratietests", "IoT-hacking", "Beveiligingsonderzoek", "Hardwarehacking", "Privacytechnologie"]
tags: ["DagShell", "Orbic RCL400", "Custom firmware", "Hotspot-hacking", "Privacytools", "TTL-fix", "MAC-spoofing", "IMSI-catcherdetectie", "Wardriving", "GPS-tracking", "Evil Twin-aanval", "Captive portal", "DNS-sniffer", "ARP-scanner", "Poortscanner", "Raspberry Pi Companion", "WiFi-beveiliging", "Mobiele hotspot", "Netwerkbewaking", "Penetratietests", "Beveiligingsonderzoek", "Bluetooth-scannen", "Deauth-aanval", "WiFi-scannen", "OUI-opzoeken", "Wigle-upload", "Celltowerbewaking", "AT-commando's", "Firewallbeheer", "AdBlock", "TLS-versleuteling", "RayHunter-integratie", "STS Collective", "Mobiel beveiligingslab", "Netwerkanalyse", "Privacyfirmware", "Open source-beveiliging", "ARM-crosscompilatie", "Embedded Linux", "Beveiligingstoolkit", "Hackertools", "Red team", "Netwerkverkenning"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Illustratie van een mobiele Orbic RCL400-hotspot met een groen oplichtende interface, omringd door abstracte beveiligingstools zoals grafieken en kaarten tegen een donker marineblauw vlak."
coverCaption: ""
---

**Maak van uw Orbic RCL400 een mobiel laboratorium voor beveiligingsonderzoek**

## Inleiding: een hotspot voor hackers

**DagShell** is openbronfirmware voor de **mobiele hotspot Orbic RCL400**. De firmware verandert een gewone mobiele hotspot in een **draagbare toolkit voor beveiligingsonderzoek en privacy**. Deze firmware met terminalstijl is gemaakt door beveiligingsonderzoeker "dag". De strakke interface met groene tekst op zwart biedt **hacktools, privacyfuncties en netwerkbewaking** in een hackerachtige stijl.

Deze uitgebreide gids behandelt:
- **Wat DagShell is** en welke functies beschikbaar zijn
- Installatie-instructies **stap voor stap**, via een webflasher en handmatig
- Een gedetailleerde uitleg van **alle tools en mogelijkheden**
- De installatie van een **Raspberry Pi Companion** voor extra functies
- **Waarom u DagShell met RayHunter combineert** voor mobiele beveiliging
- **Praktijkvoorbeelden** voor beveiligingsonderzoekers en privacyvoorvechters
- **Juridische en ethische aandachtspunten**

**Kort gezegd**: DagShell + RayHunter op een Orbic RCL400 = een **compleet mobiel beveiligingslab** voor IMSI-catcherdetectie, wardriving, netwerkanalyse en privacybescherming.

**Vooraf geflashte apparaten beschikbaar**: Dit artikel wordt gesponsord door **STS Collective**, dat Orbic RCL400-hotspots aanbiedt met **RayHunter en DagShell** vooraf geïnstalleerd en klaar voor gebruik: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Exclusieve lezerskorting**: Bespaar tot 20% op producten van STS Collective, waaronder vooraf geflashte Orbic RCL400-apparaten. Gebruik code **SIMEONONSECURITY** bij het afrekenen of [bestel met de korting al toegepast](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Wat is DagShell?

### Overzicht

**DagShell** is openbronfirmware die de standaard webinterface van de Orbic RCL400 vervangt door een **uitgebreide beveiligingstoolkit** met:

- **Terminalinterface** met ASCII-art en een hackeruitstraling
- Een **met TLS 1.2+ versleutelde** webinterface (zelfondertekend certificaat)
- **Privacytools** (TTL-maskering, MAC-spoofing en DNS-gebaseerde advertentieblokkering)
- **Netwerkbewaking** (actieve verbindingen, routeringstabellen en DNS-query's)
- **Hacktools** (IMSI-catcherdetectie, poortscans en ARP-detectie)
- **Aanvalsmogelijkheden** (Evil Twin AP, phishing via captive portal en deauth-aanvallen)
- **GPS-tracking en wardriving** met CSV-export die compatibel is met WiGLE
- **Raspberry Pi Companion** voor GPS, Bluetooth-scans en WiFi-verkenning
- **Toegang tot het bestandssysteem** via een bestandsbeheerder in de browser
- **SMS-functies** via AT-commando's
- **Persistentie**: start automatisch op bij het opstarten

### Technische specificaties

**Platform**: mobiele Orbic RCL400-hotspot\
**Architectuur**: ARM Linux (kernel 3.18)\
**Taal**: C/C++ (statische ARM-binary)\
**Versleuteling**: TLS 1.2+ met zelfondertekende certificaten (PKI met twee niveaus)\
**Webserver**: aangepaste ingebouwde HTTPS-server (poort 8443)\
**Interface**: terminalinterface in een browser\
**Licentie**: MIT (openbron)\
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Visueel ontwerp

DagShell heeft een **retro-uitstraling voor hackers**:
- **ASCII-artlogo** op elke pagina
- **Groen-zwart kleurenschema** (Matrix-stijl)
- **Monospace-lettertype** (Fira Code)
- **Scanlijneffecten** en oplichtende tekst
- **Lay-out geïnspireerd op terminals**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="DagShell-firmware op de Orbic RCL400, met een groen-zwarte terminalinterface, ASCII-art en een menu met beveiligingstools" >}}

______

## Volledig overzicht van functies

### 🏠 Overzicht

**Systeemoverzicht**:
- **Uptimeweergave**: hoe lang het apparaat actief is
- **AT-commando-interface**: directe modemaansturing voor gevorderde gebruikers
- **Snelle status**: IP-adres en verbindingsstatus

**AT-commando's** bieden modemaansturing op laag niveau:
```
Voorbeelden van AT-commando's:
AT+CSQ       - Signaalkwaliteit
AT+COPS?     - Huidige netwerkprovider
AT+CREG?     - Registratiestatus op het netwerk
AT+CIMI      - IMSI ophalen (abonnee-identiteit)
AT+CGSN      - IMEI ophalen (apparaatidentificatie)
```

### 🌐 Netwerktools

**Informatie over het huidige netwerk**:
- Gegevens over het **IP-adres en de interface**
- **Subnetmasker, gateway** en broadcastadres
- **Netwerkstatistieken** (verzonden en ontvangen pakketten)

**Routeringstabel bekijken**:
- Alle netwerkroutes bekijken
- Informatie over de standaardgateway
- Interfaces in kaart brengen

**Actieve verbindingen bewaken**:
- Realtime lijst van **alle TCP/UDP-verbindingen**
- Lokale en externe IP-adressen
- Poortnummers en verbindingsstatussen
- Handig om te **zien waarmee het apparaat communiceert**

### 🔒 Privacybescherming

#### TTL-fix

**Doel**: Hotspotverkeer maskeren zodat de provider het niet herkent.

**Werking**:
- Past de **Time To Live (TTL)** in IP-pakketten aan naar **65**.
- Providers herkennen tethering aan TTL-verlagingen (telefoon = 64, apparaat via tethering = 63).
- Met TTL 65 lijkt **al het verkeer lokaal**.

**Gebruik**: Tetheringbeperkingen of snelheidsbeperkingen van de provider omzeilen.

**Commando's**:
```bash
# Schakel TTL-correctie in
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Schakel TTL-correctie uit
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### MAC-adres vervalsen

**Doel**: Het MAC-adres van het apparaat willekeurig wijzigen voor meer privacy.

**Werking**:
- Wijzigt het MAC-adres van **wlan0** (WiFi-interface).
- Genereert een **willekeurig MAC-adres** of accepteert een eigen waarde.
- Maakt het apparaat tussen sessies **moeilijker te volgen**.

**Gebruik**: MAC-gebaseerde tracking voorkomen op netwerken waarmee u verbinding maakt.

**Proces**:
1. De interface wordt uitgeschakeld.
2. Het nieuwe MAC-adres wordt toegepast.
3. De interface wordt weer ingeschakeld.
4. De verbinding wordt hersteld.

#### DNS-gebaseerde advertentieblokkering

**Doel**: Advertenties en trackers op DNS-niveau blokkeren.

**Werking**:
- Wijzigt `/etc/hosts` met een **blokkeerlijst**.
- Domeinen op de lijst verwijzen naar **127.0.0.1** (localhost).
- Blokkeert advertenties **voor alle aangesloten apparaten**.

**Gebruik**: Advertenties in het hele netwerk blokkeren zonder elk apparaat apart in te stellen.

**Bron van de blokkeerlijst**: Veelgebruikte advertentie- en trackingdomeinen (aanpasbaar).

### 📱 SMS beheren

**SMS versturen**:
- Verstuurt tekstberichten naar de modem via **AT-commando's**.
- Handig voor **meldingen op afstand** of tests.

**Berichten bekijken**:
- Link naar het standaardpostvak van Orbic.
- Ontvangen sms-berichten lezen.

**Gebruikt AT-commando**:
```
AT+CMGS="PHONE_NUMBER"
Berichttekst hier^Z
```

### 🔧 Hacktools

#### IMSI-catcherdetector

**Doel**: Informatie over zendmasten bewaken op afwijkingen die wijzen op **IMSI-catcher- of Stingray-apparaten**.

**Werking**:
- Vraagt modemgegevens over **zendmasten** op:
  - **Cell ID** (identificatie van de zendmast)
  - **LAC** (Location Area Code)
  - **MCC/MNC** (landcode en mobiel netwerkcode)
  - **Signaalsterkte** (RSSI)
  - **Netwerkgeneratie** (2G/3G/4G)
- **Registreert wijzigingen** om verdachte wisselingen van zendmast te vinden.
- **Houdt een basislijn bij** met normale zendmasten in de omgeving.

**Aanwijzingen voor detectie**:
- **Plotselinge wisseling van zendmast** terwijl u stilstaat
- **Terugval naar 2G** *(IMSI-catchers dwingen vaak 2G af om versleuteling uit te schakelen)*
- Een **onbekende Cell ID** verschijnt
- **Zwak signaal** van een valse zendmast
- **Regelmatige verbroken en herstelde verbindingen**

**Samenwerking met RayHunter**: DagShell biedt **bewaking van zendmasten**. RayHunter biedt **gerichte IMSI-catcherdetectie** met geavanceerdere analyse (zie de sectie verderop).

#### Poortscanner

**Doel**: Doel-IP-adressen op open poorten scannen.

**Werking**:
- **TCP SYN-scan**: verstuurt SYN-pakketten naar doelpoorten.
- **Timeoutdetectie**: bepaalt of poorten open, gesloten of gefilterd zijn.
- **Bereikondersteuning**: scant één poort of een reeks poorten.

**Gebruik**:
- **Netwerkverkenning**
- **IoT-apparaten opsporen**
- **Beveiligingscontrole** van lokale netwerken
- **Services identificeren**

**Commando**:
```bash
# Scan poorten 1–1000 op het doel
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Firewallbeheer

**Doel**: IP-adressen blokkeren of deblokkeren met iptables.

**Werking**:
- **iptables-regels** laten pakketten van of naar opgegeven IP-adressen vallen.
- **Permanente regels** blijven na een herstart actief als ze zijn opgeslagen.
- Functies voor **toegestane en geblokkeerde adressen**.

**Gebruik**:
- **Kwaadaardige IP-adressen blokkeren**
- **Onbevoegde toegang voorkomen**
- **Verkeer vormgeven of filteren**
- **Ouderlijk toezicht**

**Commando's**:
```bash
# Blokkeer het IP-adres
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Deblokkeer het IP-adres
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Aanvalstools

**BELANGRIJKE JURIDISCHE DISCLAIMER**: Deze tools zijn **ALLEEN bedoeld voor geautoriseerde beveiligingstests**. Gebruik tegen netwerken die niet van u zijn of waarvoor u geen expliciete schriftelijke toestemming hebt, is in de meeste rechtsgebieden **ILLEGAAL** (onder andere onder de Computer Fraud and Abuse Act in de VS en de Computer Misuse Act in het VK). Gebruik de tools alleen op **uw eigen netwerken** of in **gecontroleerde labomgevingen**.

#### DNS-sniffer

**Doel**: DNS-query's van aangesloten clients registreren.

**Werking**:
- **iptables-logging** op poort 53 (DNS)
- **Promiscue modus is NIET vereist**
- Registreert alle DNS-verzoeken van hotspotclients
- Toont **welke websites en services** clients bezoeken

**Gebruik** (met toestemming):
- **Netwerkverkeer analyseren**
- **Ouderlijk toezicht** (eigen gezin)
- **Beveiligingsonderzoek** op eigen apparaten
- **Gedrag van malware analyseren**

*Deze functie verzamelt metadata (bezochte domeinen) van aangesloten clients. Gebruik haar alleen op netwerken die u bezit of beheert.*

#### ARP-scanner

**Doel**: Apparaten op het lokale netwerk vinden.

**Werking**:
- Verstuurt **ARP-verzoeken** naar alle IP-adressen in het subnet.
- Apparaten antwoorden met hun **MAC-adres**.
- De **OUI-opzoekfunctie** identificeert de fabrikant (Apple, Samsung en andere).
- Maakt een **netwerkkaart** van actieve apparaten.

**Gebruik**:
- **Netwerkinventarisatie**
- **Onbekende apparaten opsporen**
- **BYOD-netwerken analyseren**
- **IoT-apparaten ontdekken**

**Voorbeeld van uitvoer**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Doel**: Het netwerkpad naar een bestemming zichtbaar maken.

**Werking**:
- Verstuurt pakketten met een **oplopend TTL**.
- Elke hop verlaagt de TTL en stuurt **ICMP Time Exceeded** terug.
- Toont de **routers en route** naar de bestemming.
- Meet de **Round-Trip Time (RTT)** per hop.

**Gebruik**:
- **Netwerkproblemen oplossen**
- **Routes analyseren**
- **Latentie onderzoeken**
- **Peering van providers onderzoeken**

#### Evil Twin AP

**Doel**: Een vals WiFi-toegangspunt maken dat bestaande SSID's kopieert.

**Werking**:
- Gebruikt **wlan1** (tweede WiFi-interface, indien beschikbaar via de Pi Companion).
- Kopieert de **SSID en versleuteling** van het doelnetwerk.
- **Vangt clients op** die verbinding proberen te maken.
- Toont een **captive portal** om inloggegevens te verzamelen.

**Aanvalsscenario** (labomgeving):
1. Scan op legitieme WiFi-netwerken.
2. Maak een **vals AP** met dezelfde SSID.
3. Gebruik een **deauth-aanval** om clients van het echte AP te verbreken.
4. Clients maken automatisch opnieuw verbinding met het **valse AP**.
5. De captive portal verzamelt de inloggegevens.

*Detectie: clients zien **dubbele SSID's** als beide AP's tegelijk zichtbaar zijn.*

#### Captive portal

**Doel**: Phishingpaginamodellen aanbieden om inloggegevens te verzamelen.

**Inbegrepen modellen**:
- **WiFi-inlogpagina** (algemene stijl van een provider of hotel)
- **Inlogpagina's voor sociale media** (namaak van Facebook, Twitter en Instagram)
- **Zakelijke inlogportalen**
- WiFi-inlogpagina's voor **luchthavens en cafés**

**Werking**:
1. Het Evil Twin AP stuurt **al het verkeer** door naar de portal.
2. De client ziet een **inlogpagina**.
3. De client voert inloggegevens in.
4. De inloggegevens worden **in een bestand opgeslagen**.
5. De client krijgt internettoegang of ziet een foutmelding.

**Educatief doel**: De **risico's van social engineering** laten zien en uitleggen waarom gebruikers URL's moeten controleren.

### 📍 GPS-tracker en wardriving

#### GPS-functie

**GPS-bron**: Alleen de **Raspberry Pi Companion**.
- *De Orbic RCL400 heeft **geen ingebouwde GPS**. Zonder de Pi Companion zijn er geen locatiegegevens.*
- De Pi maakt verbinding met een **USB-GPS-dongle** (U-Blox 7-chipset).
- De Pi stuurt coördinaten via **gedeelde gegevensbestanden** naar de Orbic.
- De omzetting van **ECEF naar breedte- en lengtegraad** gebeurt automatisch.

**Weergave op het dashboard**:
- **Breedte- en lengtegraad** in decimale graden
- **Hoogte** boven zeeniveau
- **GPS-fixstatus** (nauwkeurigheid)
- **Automatisch vernieuwen** elke 5 seconden
- **Geen locatieverzoeken van de browser** (gebruikt de browser-API niet)

**Gedeelde GPS-status**:
- GPS-gegevens zijn beschikbaar voor **alle DagShell-processen**.
- Wardriving gebruikt GPS automatisch.
- Er zijn geen conflicten tussen functies.

#### Wardrivingmodus

**Doel**: WiFi-netwerken met GPS-coördinaten scannen om ze in kaart te brengen.

**Werking**:
1. Wacht op een **geldige GPS-fix** (coördinaten 0,0 worden niet geregistreerd).
2. Scant WiFi-netwerken elke **5 seconden** in een doorlopende lus.
3. Registreert netwerkgegevens:
   - **SSID** (netwerknaam)
   - **BSSID** (MAC-adres)
   - **Versleutelingstype** (WPA2, WPA3 of open)
   - **Signaalsterkte** (RSSI in dBm)
   - **Kanaalnummer**
   - **GPS-coördinaten** (breedte- en lengtegraad)
   - **Tijdstempel**
4. Exporteert naar **CSV-formaat dat compatibel is met WiGLE**.

**WiGLE-integratie**:
- **WiGLE** (wigle.net) is een wereldwijd project om WiFi-netwerken in kaart te brengen.
- De DagShell-CSV kan **rechtstreeks naar WiGLE worden geüpload**.
- Uploaden kan vanuit de browser via de pagina Files, zonder externe tools.
- De gegevens dragen bij aan de **openbare database** met WiFi-locaties.

**Gebruik**:
- **WiFi-dekking in kaart brengen**
- **Netwerkonderzoek** voor internetproviders
- **Signaalsterkte analyseren**
- **Beveiligingsonderzoek** (open netwerken en zwakke versleuteling)
- **Locatiegebonden analyse**

**Voorbeeld van CSV-formaat**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Wardrivingmodus van DagShell met GPS-coördinaten en gescande WiFi-netwerken, inclusief SSID, BSSID, versleutelingstype en signaalsterkte, opgeslagen als CSV dat compatibel is met WiGLE" >}}

### 🥧 Raspberry Pi Companion

De **Raspberry Pi Companion** breidt DagShell uit met **externe hardware**:

#### Hardwarevereisten

**Minimaal**:
- **Raspberry Pi 3B+** of nieuwer *(een Pi Zero levert niet genoeg USB-vermogen voor randapparatuur)*
- **USB-GPS-dongle** (U-Blox 7-chipset aanbevolen)
- **Voeding** *(de Pi heeft een aparte voeding nodig. De USB-poort van de Orbic levert niet genoeg stroom.)*

**Optioneel**:
- **WiFi-adapter** (tweede interface om te scannen terwijl de verbinding actief blijft)
- **Bluetooth-dongle** (als de interne Bluetooth van de Pi zwak is)

#### GPS-module (U-Blox 7)

**Aansluiting**: USB-GPS-dongle op de Pi\
**Protocol**: NMEA-zinnen via serieel\
**Omzetting**: De Pi zet ECEF automatisch om naar breedte- en lengtegraad\
**Gegevens delen**: Schrijft GPS-coördinaten naar een **gedeeld bestand** op de Orbic

**Zinnen parseren**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Tijd  Breedtegraad  Lengtegraad  Status  Satellieten  Hoogte
```

#### Bluetooth-scannen (BLE)

**Doel**: Bluetooth-apparaten in de buurt opsporen.

**Werking**:
- Scant op **BLE-advertenties**.
- Legt **MAC-adressen** vast.
- Gebruikt **OUI-opzoeking** om de fabrikant vast te stellen.
- Registreert de gegevens in **CSV-formaat**.

**Bediening op afstand**:
- Start of stop het scannen vanuit de DagShell-webinterface.
- SSH-toegang tot de Pi is niet nodig.
- Status wordt in realtime bijgewerkt.

**Gebruik**:
- **Apparaten volgen en tellen**
- **Voetgangersstromen analyseren**
- **Bluetooth-apparaten opsporen**
- **IoT-beveiligingsonderzoek**

**CSV-uitvoer**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### WiFi-scannen

**Doel**: De Pi scant WiFi-netwerken en stuurt de gegevens naar de Orbic.

**Voordeel**: Een eigen interface scant terwijl de **Orbic als hotspot actief blijft**.

**Werking**:
- De Pi gebruikt een **tweede WiFi-adapter** of ingebouwde WiFi als die niet voor de verbinding nodig is.
- Scant **alle kanalen** (1-14 op 2,4 GHz en 36-165 op 5 GHz, indien ondersteund).
- Stuurt resultaten via gedeelde opslag naar de Orbic.
- DagShell registreert ze in een **wardriver-CSV**.

**Afstemming**:
- Pi en Orbic **synchroniseren** via de GPS-tijdstempel.
- Dit voorkomt dubbele vermeldingen.
- Beide scanbronnen worden gecombineerd in één logboek.

#### Deauth-aanvallen

**Doel**: Clients loskoppelen van WiFi-netwerken voor labtests.

**Werking**:
- Verstuurt **802.11-deauthenticatieframes**.
- Vervalst het **MAC-adres van het AP**.
- De client ontvangt een melding van het AP dat de verbinding wordt verbroken.
- De client **verliest de verbinding** en probeert opnieuw verbinding te maken.

**Bedieningsmethoden**:
- **Eenmalige deauth**: één korte reeks frames.
- **Doorlopende deauth**: voorkomt opnieuw verbinden (DoS).
- **Bediening op afstand**: starten vanuit de scanpagina van DagShell.

**Gebruik** (met toestemming):
- **Onbekende apparaten verwijderen** uit uw eigen netwerk
- **Penetratietests** met toestemming
- **Evil Twin-aanvallen** in een lab (clients naar het valse AP dwingen)

**⚠️ Juridische waarschuwing**: Deauth-aanvallen zijn **illegaal tegen netwerken die niet van u zijn**. Ze kunnen de FCC-regels overtreden en tot vervolging onder de CFAA leiden.

#### Automatische startservice

**systemd-service**: De Pi Companion start automatisch op.

**Servicebestand** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Commando's**:
```bash
# Schakel automatisch starten in
sudo systemctl enable pi-companion

# Start de service
sudo systemctl start pi-companion

# Controleer de status
sudo systemctl status pi-companion
```

#### OUI-database

**Doel**: De fabrikant opzoeken die bij een MAC-adres hoort.

**Database**: Prefixgebaseerde API van de [OUI Master Database](https://standards.ieee.org/products-programs/regauth/).

**Werking**:
- Haalt de **eerste drie bytes** van het MAC-adres op (OUI-prefix).
- Vraagt de API op: `api.example.com/oui/A4:83:E7`.
- Geeft de **fabrikantnaam** terug.

**Voorbeeld**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integratie**: Gebruikt door de ARP-scanner, BLE-scanner en WiFi-wardriving.

### 📁 Bestandsbeheerder

**Doel**: Bestanden op het apparaat bekijken en beheren.

**Locatie**: Map `/data/` (schrijfbare partitie).

**Mogelijkheden**:
- **Bestanden** en submappen bekijken
- Bestanden naar uw computer **downloaden**
- Bestanden **verwijderen** (na bevestiging)
- Bestandsgrootte en tijdstempels **bekijken**

**Veelgebruikte bestanden**:
- `wardrive_log.csv`: WiFi-scangegevens
- `bluetooth_scan.csv`: BLE-apparaatgegevens
- `gps_track.gpx`: GPS-tracks
- `dns_queries.log`: vastgelegde DNS-query's
- `arp_scan.txt`: lijst met netwerkapparaten

**Upload naar WiGLE**:
- Rechtstreeks uploaden via de browser op de pagina Files
- Aanmelden met een WiGLE-account
- CSV uploaden zonder het eerst te downloaden

______

{{< stscollective-ad "rayhunter" >}}

## Installatiegids

### Vereisten

**Hardware**:
- **Mobiele hotspot Orbic RCL400**
- **Computer** (Windows, macOS of Linux)
- **USB-kabel** (voor het rechtstreeks flashen van firmware)

**Software**:
- **Python 3** met de modules `requests` en `cryptography`
- **Webbrowser** (Chrome, Firefox, Edge of Safari)

**Optioneel**:
- **Raspberry Pi 3B+** of nieuwer (voor GPS en extra functies)
- **USB-GPS-dongle** (U-Blox 7-chipset)

### Methode 1: Webflasher (aanbevolen)

**De eenvoudigste methode**. U hebt geen opdrachtregel nodig.

**Stap 1**: Open de DagShell-webflasher.
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Stap 2**: Genereer PKI-certificaten.
- Klik op **"Generate Certificates"**.
- De browser maakt een **PKI met twee niveaus** (root-CA en servercertificaat).
- **Download de bestanden**: `root.der` en `server.der`.

**Stap 3**: Schakel de root-shell in op de Orbic.
- Maak verbinding met het WiFi-netwerk van de Orbic.
- Voer het **beheerderswachtwoord** in het webformulier in.
- Klik op **"Enable Shell"**.
- De webpagina misbruikt de Orbic-API om een **root-shell op poort 24** te openen.

**Stap 4**: Installeer de firmware.
- Klik op **"Deploy DagShell"**.
- Het script uploadt:
  - `orbic_app` (hoofdbinary van de firmware)
  - `root.der` (rootcertificaat)
  - `server.der` (TLS-servercertificaat)
  - `dagshell_boot.sh` (persistentiescript)
- De installatie duurt **2 tot 3 minuten**.

**Stap 5**: Herstart de Orbic.
- Schakel het apparaat uit en weer in.
- DagShell start automatisch bij het opstarten.

**Stap 6**: Open DagShell.
- Open in de browser `https://192.168.1.1:8443/`.
- Accepteer de **beveiligingswaarschuwing** (een zelfondertekend certificaat is verwacht).
- Meld u aan met de standaardgegevens als daarom wordt gevraagd.

### Methode 2: Handmatige installatie

Voor **gevorderde gebruikers** die de firmware vanuit de broncode willen bouwen.

#### Stap 1: Afhankelijkheden installeren

**Windows**:
```powershell
# Installeer Python 3
# Download van python.org

# Installeer de vereiste modules
pip install requests cryptography

# ARM-crosscompiler staat in de map gcc_win
```

**macOS**:
```bash
# Installeer Homebrew als dit nog niet is geïnstalleerd
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installeer Python 3
brew install python3

# Installeer de vereiste modules
pip3 install requests cryptography

# ARM-toolchain staat in de map gcc_mac
```

**Linux**:
```bash
# Installeer Python 3 en pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Installeer de vereiste modules
pip3 install requests cryptography

# Installeer de ARM-crosscompiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Stap 2: Repository klonen

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Stap 3: Firmware bouwen

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # Genereer certificaten
.\build.ps1                # Compileer de firmware
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # Genereer certificaten
./build.sh                 # Compileer de firmware, BearSSL wordt automatisch meegebouwd
```

**Uitvoer**: `orbic_app` (statische ARM-binary) en DER-certificaatbestanden.

**⚠️ Opmerking voor macOS**: De map `gcc_mac/` bevat een aangepaste ARM-toolchain die met **crosstool-ng** is gebouwd voor **Linux-kernel 3.2**-headers. Dat zorgt voor compatibiliteit met kernel 3.18 van de Orbic. *Standaard ARM-compilers van Homebrew zijn bedoeld voor nieuwere kernels en **werken niet**.*

#### Stap 4: Root-shell inschakelen op de Orbic

```bash
# Maak verbinding met de Orbic-WiFi
# Vervang YOUR_ADMIN_PASSWORD door het echte wachtwoord

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Dit misbruikt de Orbic-web-API om een root-shell op **poort 24** te openen.

#### Stap 5: Firmware installeren

```bash
python deploy_base64.py
```

Dit uploadt en installeert:
- `orbic_app` naar `/data/orbic_app`
- Certificaten naar `/data/root.der` en `/data/server.der`
- Opstartscripts naar `/etc/rc.d/dagshell_boot.sh`

**Persistentie**: De firmware start na een herstart automatisch via een init-script.

#### Stap 6: Herstarten en openen

```bash
# Herstart de Orbic (haal de stroom eraf of gebruik SSH)
reboot

# Open DagShell na het opnieuw opstarten
# Open in je browser: https://192.168.1.1:8443/
```

### Waarschuwing voor het beveiligingscertificaat

Bij het openen van DagShell ziet u de waarschuwing **"Not Secure" of "Not Trusted"**:

**Desktopbrowsers**:
- Klik op **"Advanced"**.
- Klik op **"Proceed to 192.168.1.1 (unsafe)"**.

**Mobiele browsers**:
- Tik op **"Show Details"**.
- Tik op **"visit this website"**.

**Waarom dit gebeurt**:
- Het certificaat is **zelfondertekend** en komt niet van een vertrouwde CA zoals Let's Encrypt.
- Het rootcertificaat staat niet in de certificaatopslag van uw apparaat.
- *Dit is **verwacht gedrag** bij custom firmware en wijst niet op een compromis.*

**Is de verbinding echt veilig?**:
- **Ja**. De verbinding **is versleuteld met TLS 1.2+**.
- Gegevens kunnen niet worden onderschept.
- *Het certificaat is alleen niet via een certificaatketen aan een openbare CA gekoppeld. De versleuteling is echt.*

**Optioneel**: Installeer `root.der` in de certificaatopslag van uw apparaat om de waarschuwing te verwijderen.

______

## Raspberry Pi Companion instellen

**Optioneel, maar sterk aanbevolen** voor alle functies.

### Hardware instellen

**Stap 1**: Verzamel de onderdelen.
- **Raspberry Pi 3B+** of nieuwer ($35-55)
- **USB-GPS-dongle** met U-Blox 7-chipset ($15-30)
- **MicroSD-kaart** van 16 GB of meer voor Pi OS ($10)
- **Voeding** voor de Pi ($10)

**Stap 2**: Installeer Raspberry Pi OS.
```bash
# Haal Raspberry Pi Imager op
# https://www.raspberrypi.org/software/

# Flash Raspberry Pi OS Lite naar de SD-kaart
# Start de Pi en voltooi de configuratie
```

**Stap 3**: Sluit de GPS-dongle aan.
- Sluit de USB-GPS aan op de Pi.
- Controleer de detectie met `lsusb` (de GPS hoort te verschijnen).
- Controleer de seriële poort: `ls /dev/ttyUSB*` of `/dev/ttyACM*`.

### Software installeren

**Stap 1**: Kloon de DagShell-repository op de Pi.

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Stap 2**: Installeer afhankelijkheden.

```bash
# Werk de pakketlijst bij
sudo apt-get update

# Installeer de vereiste pakketten
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Installeer Python-modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Stap 3**: Stel de GPS-daemon in.

```bash
# Bewerk de gpsd-configuratie
sudo nano /etc/default/gpsd

# Stel de DEVICES-regel in op de GPS-seriële poort
DEVICES="/dev/ttyUSB0"  # Pas zo nodig aan

# Herstart gpsd
sudo systemctl restart gpsd

# Test de GPS
cgps -s  # Satellietgegevens zouden na ongeveer 30 seconden moeten verschijnen
```

**Stap 4**: Stel de Pi Companion in.

```bash
# Bewerk het configuratiebestand
nano pi_companion/config.py

# Stel het Orbic-IP-adres in
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Stel de GPS-seriële poort in
GPS_DEVICE = "/dev/ttyUSB0"

# Opslaan en afsluiten
```

**Stap 5**: Installeer de systemd-service.

```bash
# Kopieer het servicebestand
sudo cp pi_companion.service /etc/systemd/system/

# Laad systemd opnieuw
sudo systemctl daemon-reload

# Schakel automatisch starten in
sudo systemctl enable pi-companion

# Start de service
sudo systemctl start pi-companion

# Controleer de status
sudo systemctl status pi-companion
```

**Stap 6**: Controleer de communicatie.

```bash
# Controleer de logs
journalctl -u pi-companion -f

# GPS-coördinaten zouden naar de Orbic moeten worden verzonden
```

### Netwerk instellen

**Optie A**: WiFi-verbinding

```bash
# De Pi maakt verbinding met de Orbic-hotspot
# Bewerk de wpa_supplicant-configuratie
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Voeg een netwerk toe
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Herstart de WiFi
sudo systemctl restart networking
```

**Optie B**: USB-Ethernet (aanbevolen)

- Sluit de Pi met een **USB-kabel** aan op de Orbic (USB-poort van de Pi naar die van de Orbic).
- Schakel de **USB-gadgetmodus** in op de Pi.
- De Pi werkt als **USB-Ethernetapparaat**.
- *Betrouwbaarder dan WiFi voor doorlopende gegevensoverdracht.*
- De Pi krijgt via de Orbic toegang tot internet.

**USB-gadgetconfiguratie**:
```bash
# Bewerk config.txt
sudo nano /boot/config.txt

# Voeg achteraan toe
dtoverlay=dwc2

# Bewerk cmdline.txt
sudo nano /boot/cmdline.txt

# Voeg toe na rootwait
modules-load=dwc2,g_ether

# Start opnieuw op
sudo reboot
```

______

## Waarom DagShell en RayHunter combineren?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Schema dat de WiFi-wardriving- en netwerkaanvalstools van DagShell vergelijkt met de detectie van afwijkingen in mobiele protocollen door RayHunter. Beide draaien op dezelfde Orbic RCL400-hotspot." >}}

### Aanvullende mogelijkheden

**DagShell** en **RayHunter** zijn **sterk complementaire** beveiligingstools die verschillende onderdelen van mobiel beveiligingsonderzoek afdekken:

| Functie | DagShell | RayHunter |
|---------|----------|-----------|
| **IMSI-catchers detecteren** | Basisbewaking van zendmasten | Geavanceerde patroonanalyse |
| **GPS-tracking** | Ja (via Pi) | Ja (via modem) |
| **WiFi-wardriving** | Ja | Nee |
| **Bluetooth-scans** | Ja (via Pi) | Nee |
| **Netwerktools** | Ja (DNS-sniffer, ARP-scan, poortscan) | Nee |
| **Aanvalstools** | Ja (Evil Twin, captive portal, deauth) | Nee |
| **Privacytools** | Ja (TTL-fix, MAC-spoofing, AdBlock) | Beperkt |
| **Database met zendmasten** | Basis | Uitgebreid |
| **AI/ML-analyse** | Nee | Ja (afwijkingen detecteren) |
| **Analyse van providerprotocollen** | Beperkt | Diepgaand (SS7/Diameter) |

### Gecombineerde gebruiksscenario's

#### 1. **Volledige bescherming tegen IMSI-catchers**

**Scenario**: Reizen in een gebied met veel toezicht.

**Bijdrage van DagShell**:
- **Bewaakt wijzigingen in zendmasten** in realtime.
- **Registreert de GPS-locatie** tijdens verdachte wisselingen.
- **Slaat zendmastgegevens op** voor latere analyse.

**Bijdrage van RayHunter**:
- **Detecteert afwijkingen** in mobiele protocollen met machine learning.
- **Inspecteert SS7/Diameter-pakketten** op geavanceerde aanvallen.
- Vergelijkt met een **database van bekende betrouwbare zendmasten**.

**Gecombineerd resultaat**: DagShell biedt **doorlopende bewaking**, RayHunter biedt **diepgaande analyse**.

#### 2. **Wardriving met beveiligingsbewustzijn**

**Scenario**: WiFi-netwerken in een stedelijk gebied in kaart brengen.

**Bijdrage van DagShell**:
- **WiFi-scans** met GPS-coördinaten.
- Tools voor **netwerkanalyse** (signaalsterkte en versleuteling).
- **WiGLE-CSV-export** voor het in kaart brengen.

**Bijdrage van RayHunter**:
- **Volgt zendmasten** tijdens wardriving.
- **Detecteert IMSI-catchers** terwijl u WiFi scant.
- **Waarschuwt als de mobiele beveiliging is aangetast**.

**Gecombineerd resultaat**: Wardriving met **aandacht voor mobiele beveiliging**.

#### 3. **Laboratorium voor beveiligingsonderzoek**

**Scenario**: Red team of penetratietests.

**Bijdrage van DagShell**:
- **Evil Twin AP** om WiFi te testen.
- **Captive portal** voor demonstraties van social engineering.
- **Deauth-aanvallen** om weerbaarheid te testen.
- Tools voor **netwerkverkenning**.

**Bijdrage van RayHunter**:
- **Detecteert of u tijdens tests wordt gevolgd**.
- Biedt inzicht in de **beveiliging van mobiele netwerken**.
- Helpt **tegenbewaking tijdens tests** voorkomen.

**Gecombineerd resultaat**: Aanvalstools met **defensief bewustzijn**.

#### 4. **Reizen met privacy als uitgangspunt**

**Scenario**: Journalist of activist in een gevoelige omgeving.

**Bijdrage van DagShell**:
- **TTL-maskering** om tethering te verbergen.
- **MAC-spoofing** voor meer anonimiteit.
- **AdBlock** om tracking tegen te gaan.
- **Bewaking op IMSI-catchers**.

**Bijdrage van RayHunter**:
- **Geavanceerde IMSI-catcherdetectie**.
- **Aanvallen op protocolniveau detecteren**.
- **Beveiligingsmeldingen over mobiele netwerken**.

**Gecombineerd resultaat**: Maximale privacy met **meerlaagse bescherming**.

### Samen installeren

**Vooraf geflashte optie** (eenvoudigst):
- Koop bij **STS Collective**: [Vooraf geflashte Orbic RCL400 met RayHunter en DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot).
- **Direct klaar voor gebruik**.
- Beide firmwareversies zijn **getest en gecontroleerd**.
- **Geen installatiewerk**.

**Zelf installeren**:
1. **Flash eerst RayHunter** (zie onze [complete gids voor het flashen van RayHunter-apparaten](/articles/how-to-flash-rayhunter-devices-complete-guide/)).
2. **Flash daarna DagShell**. Beide kunnen naast elkaar bestaan.
3. **RayHunter** gebruikt de standaardpoorten.
4. **DagShell** gebruikt poort 8443.
5. Open beide in een apart browsertabblad.

**Geen conflicten**:
- RayHunter gebruikt poort **80/443**.
- DagShell gebruikt poort **8443**.
- Ze hinderen elkaar niet.
- Ze draaien **tegelijkertijd**.

Geen zin in de doe-het-zelfroute? De vooraf geflashte **[Orbic RCL400 met RayHunter en DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** van STS Collective is direct klaar voor gebruik. Met lezerscode **SIMEONONSECURITY** krijgt u tot 20% korting bij STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Koop de vooraf geflashte RCL400 en bespaar 20%
{{< /centerbutton >}}

______

## Praktijkvoorbeelden

### Gebruiksscenario 1: Beveiligingsonderzoeker

**Profiel**: Een penetratietester voert een beveiligingsbeoordeling van WiFi uit.

**Gebruikte DagShell-tools**:
- **WiFi-wardriving** om netwerken van klanten in kaart te brengen
- **ARP-scanner** om apparaten te ontdekken
- **Poortscanner** om services te identificeren
- **Evil Twin/captive portal** om de weerbaarheid tegen social engineering te testen
- **Bestandsbeheerder** om resultaten op te halen

**Werkwijze**:
1. Rijd langs de rand van het terrein van de klant.
2. Breng met wardriving de WiFi-dekking in kaart.
3. Maak met toestemming een Evil Twin van het netwerk van de klant.
4. Bewaak verbindingspogingen van clients.
5. Maak een rapport met de verzamelde gegevens.

**RayHunter-integratie**: Helpt vaststellen of de onderzoeker tijdens de beoordeling zelf wordt gevolgd.

### Gebruiksscenario 2: Privacyvoorvechter

**Profiel**: Een journalist reist internationaal.

**Gebruikte DagShell-tools**:
- **TTL-fix** om providerbeperkingen te omzeilen
- **MAC-spoofing** om het apparaat anoniem te maken
- **IMSI-catcherdetector** om mogelijke bewaking op te merken
- **DNS-sniffer** om te controleren of apparaten geen gegevens lekken
- **AdBlock** om tracking te voorkomen

**Werkwijze**:
1. Schakel de TTL-fix in voordat u het apparaat gebruikt.
2. Maak het MAC-adres willekeurig.
3. Laat de IMSI-catcherdetector doorlopend bewaken.
4. Gebruik AdBlock op alle aangesloten apparaten.
5. Registreer verdachte mobiele activiteit.

**RayHunter-integratie**: Detecteert IMSI-catchers geavanceerder dan basisbewaking.

### Gebruiksscenario 3: Netwerkbeheerder

**Profiel**: Een IT-beheerder beheert meerdere locaties.

**Gebruikte DagShell-tools**:
- **WiFi-wardriving** om dekking te controleren
- **ARP-scanner** voor een apparaatinventaris
- **Poortscanner** voor beveiligingscontroles
- **Bewaking van actieve verbindingen** voor ongeautoriseerd verkeer
- **Firewallbeheer** om IP-adressen te blokkeren

**Werkwijze**:
1. Controleer met wardriving de WiFi-dekking op de locatie.
2. Ontdek alle netwerkapparaten met een ARP-scan.
3. Scan servers op poorten en blootgestelde services.
4. Blokkeer kwaadaardige IP-adressen via de firewall.
5. Exporteer rapporten voor documentatie.

**RayHunter-integratie**: Bewaakt mobiele beveiliging op locaties met mobiele apparaten.

### Gebruiksscenario 4: IoT-beveiligingsonderzoeker

**Profiel**: Een onderzoeker analyseert de beveiliging van IoT-apparaten.

**Gebruikte DagShell-tools**:
- **ARP-scanner** met OUI-opzoeking om IoT-apparaten te identificeren
- **Poortscanner** om open services te vinden
- **DNS-sniffer** om IoT-verkeerspatronen vast te leggen
- **Bluetooth-scanner** (Pi) voor BLE-IoT-apparaten
- **Traceroute** voor connectiviteitsanalyse

**Werkwijze**:
1. Plaats de Orbic en Pi in een testomgeving.
2. Ontdek IoT-apparaten met de ARP-scanner.
3. Scan op kwetsbare services.
4. Scan op Bluetooth-IoT-apparaten met BLE.
5. Analyseer DNS om te zien of apparaten verbinding maken met externe servers.
6. Documenteer kwetsbaarheden.

**RayHunter-integratie**: Helpt detecteren of IoT-apparaten mobiele connectiviteit hebben en bewaakt afwijkingen.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Schema met vier praktijktoepassingen van DagShell en RayHunter: beveiligingsonderzoeker, privacyvoorvechter, netwerkbeheerder en IoT-onderzoeker" >}}

______

## Juridische en ethische aandachtspunten

### Juridisch kader

**Tools zoals DagShell vallen in juridische grijze gebieden**:

**Wettige toepassingen**:
✅ **Uw eigen netwerken**: Test uw eigen apparaten en netwerken.
✅ **Tests met toestemming**: Voer penetratietests uit met schriftelijke toestemming.
✅ **Educatief gebruik**: Leer in geïsoleerde labomgevingen.
✅ **Privacybescherming**: Gebruik TTL-fix en MAC-spoofing op uw eigen apparaat.
✅ **Beveiligingsonderzoek**: Onderzoek kwetsbaarheden en meld ze op verantwoorde wijze.

**Onwettige toepassingen**:
❌ **Onbevoegde toegang**: Netwerken aanvallen die niet van u zijn (overtreding van de CFAA).
❌ **Deauth-aanvallen** op andere netwerken (overtreding van FCC-regels en mogelijk een misdrijf).
❌ **Evil Twin-aanvallen** tegen het publiek (elektronische fraude en identiteitsdiefstal).
❌ **DNS-verkeer van anderen sniffen** zonder toestemming (aftappen).
❌ **Beveiliging omzeilen** om fraude te plegen.

### Wetten om rekening mee te houden

**Verenigde Staten**:
- **Computer Fraud and Abuse Act (CFAA)**: Onbevoegde toegang tot computers of netwerken.
- **Wiretap Act**: Elektronische communicatie onderscheppen.
- **FCC-regelgeving**: Radiofrequentie-interferentie (deauth-aanvallen).

**Verenigd Koninkrijk**:
- **Computer Misuse Act 1990**: Vergelijkbaar met de CFAA.
- **Regulation of Investigatory Powers Act (RIPA)**: Beperkingen op onderschepping.

**Europese Unie**:
- **AVG (GDPR)**: Gegevensbescherming (Bluetooth- en WiFi-scans van identificeerbare gegevens).
- *Lokale regels verschillen per land en worden niet overal hetzelfde gehandhaafd.*

### Ethische richtlijnen

**WEL DOEN**:
- ✅ Gebruik de tools op **uw eigen apparaten** en netwerken.
- ✅ Vraag **schriftelijke toestemming** voordat u systemen van anderen test.
- ✅ Doe aan **verantwoorde openbaarmaking** als u kwetsbaarheden vindt.
- ✅ Gebruik de tools **educatief** in een gecontroleerde omgeving.
- ✅ Bescherm **uw eigen privacy**.

**NIET DOEN**:
- ❌ Val netwerken aan die niet van u zijn.
- ❌ Verzamel inloggegevens van vreemden.
- ❌ Verstoor kritieke infrastructuur.
- ❌ Gebruik de tools kwaadwillig.
- ❌ Verspreid verzamelde gegevens.

### Verklaring voor verantwoord gebruik

DagShell is een **tool voor beveiligingsonderzoek en privacy**. De mogelijkheden zijn vergelijkbaar met professionele penetratietesttools zoals **Kali Linux**, **WiFi Pineapple** en **HackRF**.

**De bedoeling is bepalend**: Zowel **kwaadwillende hackers** als **beveiligingsprofessionals** gebruiken dezelfde tools. Het verschil zit in:
- **Toestemming** (toestemming om te testen)
- **Bedoeling** (beveiliging verbeteren of schade veroorzaken)
- **Melding** (bevindingen melden of misbruiken)

Gebruik DagShell **verantwoordelijk** en **ethisch**. *Als u niet weet of iets wettelijk is toegestaan, stop dan en raadpleeg een advocaat voordat u verdergaat.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Juridisch en ethisch kader voor beveiligingsonderzoek met DagShell, met toegestane en ongeoorloofde toepassingen en relevante wetten" >}}

______

## Problemen oplossen

### Installatieproblemen

**Probleem**: `enable_shell.py` kan geen verbinding maken.

**Oplossingen**:
- Controleer of u met **WiFi van de Orbic** bent verbonden.
- Controleer of het IP-adres **192.168.1.1** is (standaard).
- Probeer het beheerderswachtwoord opnieuw. Het is hoofdlettergevoelig.
- Controleer of poort 80 bereikbaar is: `telnet 192.168.1.1 80`.

**Probleem**: Het uploaden van de firmware mislukt.

**Oplossingen**:
- Schakel eerst de root-shell in en controleer of `enable_shell.py` is gelukt.
- Controleer de netwerkverbinding. Gebruik zo mogelijk een bekabelde verbinding.
- Probeer `deploy_net.py` in plaats van `deploy_base64.py`.
- Controleer of de partitie `/data` ruimte heeft: `df -h /data`.

**Probleem**: De certificaatwaarschuwing blijft verschijnen.

**Oplossingen**:
- *Dit is **normaal** bij zelfondertekende certificaten. De verbinding blijft versleuteld.*
- Klik telkens op "Advanced" en vervolgens op "Proceed anyway".
- **Optioneel**: Installeer `root.der` in de certificaatopslag van het apparaat (geavanceerd).

### Problemen tijdens uitvoering

**Probleem**: DagShell start niet op bij het opstarten.

**Oplossingen**:
- Controleer het opstartscript: `ls -la /etc/rc.d/dagshell_boot.sh`.
- Controleer of het uitvoerbaar is: `chmod +x /etc/rc.d/dagshell_boot.sh`.
- Bekijk de logs: `logread | grep dagshell`.
- Start het handmatig: `/data/orbic_app &`.

**Probleem**: GPS werkt niet.

**Oplossingen**:
- Controleer of de **Pi Companion** actief is: `systemctl status pi-companion`.
- Controleer of GPS satellieten ontvangt: `cgps -s` (op de Pi).
- Controleer of de GPS-dongle is aangesloten: `lsusb`.
- *Wacht 5 tot 10 minuten op een koude GPS-fix. Bij de eerste start duurt een GPS-fix buiten langer.*

**Probleem**: Wardriving legt geen gegevens vast.

**Oplossingen**:
- Controleer vóór het starten of GPS een fix heeft.
- Controleer de schrijfrechten van `/data`.
- Controleer of het CSV-bestand wordt aangemaakt: `ls -la /data/wardrive_log.csv`.
- Controleer of de WiFi-interface actief is: `ifconfig wlan0`.

**Probleem**: De Pi Companion communiceert niet met de Orbic.

**Oplossingen**:
- Controleer de netwerkverbinding: `ping 192.168.1.1`.
- Controleer of het configuratiebestand het juiste IP-adres bevat.
- Controleer of poort 8443 open is: `telnet 192.168.1.1 8443`.
- Bekijk de logs van de Pi Companion: `journalctl -u pi-companion`.

### Prestatieproblemen

**Probleem**: De webinterface reageert traag.

**Oplossingen**:
- Wis de browsercache.
- Schakel browserextensies uit (advertentieblokkers kunnen storen).
- Gebruik een **bekabelde** verbinding met de Orbic in plaats van WiFi.
- Herstart DagShell: `killall orbic_app && /data/orbic_app &`.

**Probleem**: Wardriving-scans duren te lang.

**Oplossingen**:
- Verhoog het scaninterval in de instellingen (minder scans in ruil voor betere prestaties).
- Scan minder kanalen.
- *Een zwakke GPS-fix vertraagt scans. Het systeem wacht op geldige coördinaten voordat het gegevens vastlegt.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Probleemoplossingsschema van DagShell met veelvoorkomende installatie-, GPS- en wardrivingproblemen en stapsgewijze oplossingen" >}}

______

## Geavanceerde configuratie

### DagShell aanpassen

**Broncode wijzigen**:
- Bewerk bestanden in de map `orbic_fw_c/`.
- Bouw opnieuw met `build.sh` of `build.ps1`.
- Installeer de firmware opnieuw.

**Aangepaste pagina's toevoegen**:
- DagShell bevat HTML in de C++-code.
- Bewerk `main.cpp` om routes toe te voegen.
- Compileer en installeer opnieuw.

**Aangepast certificaat**:
- Genereer een eigen PKI met `gen_pki.py`.
- Of gebruik **OpenSSL** om certificaten te maken.
- Vervang `root.der` en `server.der`.

### Integratie met andere tools

**Gegevens exporteren naar Wireshark**:
```bash
# Leg het pcap-bestand vast
tcpdump -i wlan0 -w /data/capture.pcap

# Download via de bestandsbrowser
# Open in Wireshark op de pc
```

**GPS-tracks in QGIS importeren**:
```bash
# Exporteer als GPX
python gps_to_gpx.py /data/gps_coords.txt

# Importeer in QGIS als vectorlaag
```

**Synchroniseren met een externe database**:
```python
# Aangepast script om wardrive-gegevens naar MySQL te uploaden
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Prestaties afstellen

**Scansnelheid optimaliseren**:
```bash
# Bewerk het wardrive-scaninterval
# Wijzig in de DagShell-webinterface 5 s naar 3 s voor sneller scannen
# Dit verhoogt het CPU-gebruik en kan netwerken missen
```

**Batterij optimaliseren** (bij gebruik van een accupack):
```bash
# Verlaag de helderheid van het Orbic-scherm
# Schakel ongebruikte functies uit (BT en GPS wanneer die niet nodig zijn)
# Gebruik de slaapstand tussen wardrive-sessies
```

______

## Vergelijking met alternatieven

### DagShell versus WiFi Pineapple

| Functie | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Prijs** | $60-80 + apparaat | $99-299 |
| **Mobiel netwerk** | ✅ 4G LTE ingebouwd | ❌ Nee (alleen WiFi) |
| **GPS** | ✅ Via Pi Companion | ⚠️ Via USB-dongle |
| **Evil Twin** | ✅ Ja | ✅ Ja |
| **Captive portal** | ✅ Ja | ✅ Ja |
| **Deauth** | ✅ Ja (via Pi) | ✅ Ja |
| **Wardriving** | ✅ Ja | ✅ Ja |
| **IMSI-detectie** | ✅ Basis | ❌ Nee |
| **Draagbaarheid** | ✅ Zeer draagbaar | ⚠️ Gemiddeld |
| **Batterij** | ✅ Ingebouwd | ⚠️ Extern nodig |
| **Leercurve** | Gemiddeld | Laag (afgewerkte interface) |

**Winnaar**: DagShell voor **mobiele netwerkbeveiliging** en Pineapple voor **WiFi-specifieke** tests met een eenvoudige interface.

### DagShell versus Kali Linux op Pi

| Functie | DagShell | Kali op Pi |
|---------|----------|-----------|
| **Installatietijd** | 15 minuten | 2-3 uur |
| **Mobiel LTE** | ✅ Ingebouwd | ❌ USB-modem vereist |
| **Webinterface** | ✅ Ja | ⚠️ Beperkt (VNC/SSH vereist) |
| **Aantal tools** | Ongeveer 15 | Meer dan 600 |
| **Specialisatie** | Mobiele beveiliging | Algemene pentests |
| **Draagbaarheid** | ✅ Past in een zak | ⚠️ Scherm en voeding vereist |
| **Batterijduur** | 8-10 uur | 2-4 uur |

**Winnaar**: DagShell voor **mobiele taken** en Kali voor een **uitgebreide toolkit**.

### DagShell versus standaardfirmware van Orbic

| Functie | DagShell | Standaardfirmware |
|---------|----------|-------------------|
| **Beveiligingstools** | ✅ Uitgebreid | ❌ Geen |
| **Privacyfuncties** | ✅ Ja | ❌ Beperkt |
| **Aanpasbaarheid** | ✅ Volledig aanpasbaar | ❌ Vergrendeld |
| **Wardriving** | ✅ Ja | ❌ Nee |
| **GPS** | ✅ Ja (via Pi) | ❌ Nee |
| **Open source** | ✅ Ja | ❌ Eigendom van fabrikant |
| **Ondersteuning** | ⚠️ Community | ✅ Officieel |
| **Stabiliteit** | ⚠️ Beta | ✅ Productie |

**Winnaar**: DagShell voor **onderzoekers** en standaardfirmware voor **gewone gebruikers**.

______

## Conclusie: het ultieme mobiele lab

**DagShell** verandert de eenvoudige **Orbic RCL400-hotspot** in een **krachtig mobiel beveiligingslab** met:

✅ **Privacybescherming** (TTL-maskering, MAC-spoofing, AdBlock)\
✅ **Netwerkbewaking** (verbindingen, DNS, routering)\
✅ **Hacktools** (IMSI-detectie, poortscans, ARP-detectie)\
✅ **Aanvalsmogelijkheden** (Evil Twin, captive portal, deauth)\
✅ **GPS-wardriving** met WiGLE-integratie\
✅ **Uitbreiding met Raspberry Pi** (BLE, WiFi, GPS)\
✅ **Draagbaar en werkt op batterij**\
✅ **Open source en aanpasbaar**

### In combinatie met RayHunter

**RayHunter + DagShell** = een **compleet mobiel beveiligingsplatform**:
- **RayHunter** biedt geavanceerde IMSI-catcherdetectie.
- **DagShell** biedt aanvalstools en privacyfuncties.
- Beide draaien **tegelijkertijd** op hetzelfde apparaat.
- De **mogelijkheden vullen elkaar aan** en overlappen niet.
- Eén **draagbaar pakket** voor alle behoeften rond mobiele beveiliging.

### Vandaag beginnen

**Optie 1: Vooraf geflasht** (eenvoudigst)
- **STS Collective**: [Orbic RCL400 met RayHunter en DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot).
- Wordt **klaar voor gebruik** geleverd.
- Geen ingewikkelde installatie.
- Professioneel geconfigureerd.

**Optie 2: Zelf installeren**
- Volg deze gids.
- **Gratis** als u al een Orbic RCL400 hebt.
- Leer het installatieproces.
- Pas het systeem aan uw behoeften aan.

### Gerelateerde artikelen

- **[RayHunter-apparaten flashen: complete gids](/articles/how-to-flash-rayhunter-devices-complete-guide/)**: Installeer RayHunter eerst.
- **[RayHunter-apparaten vergelijken: complete beoordeling](/articles/rayhunter-device-comparison-2026-complete-review/)**: Kies uw platform.
- **[Flock-You-detectieproject: gids voor hardware tegen surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**: Bekijk meer detectietools.

### Laatste gedachten

Of u nu **beveiligingsonderzoeker**, **penetratietester**, **privacyvoorvechter** of **netwerkbeheerder** bent, DagShell biedt een **draagbaar, krachtig en betaalbaar** platform voor mobiel beveiligingswerk.

**Disclaimer**: Gebruik de tools verantwoord. Test alleen netwerken en apparaten die van u zijn of waarvoor u expliciet schriftelijke toestemming hebt. Houd het legaal en ethisch. Veel succes met hacken! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Orbic RCL400-hotspot met DagShell-firmware als compleet draagbaar laboratorium voor mobiel beveiligingsonderzoek" >}}

______

## Bronnen

1. [DagShell-repository op GitHub](https://github.com/dagnazty/DagShell)
2. [DagShell-documentatie](https://dagnazty.github.io/DagShell/)
3. [STS Collective: vooraf geflashte apparaten](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE: WiFi-mappingproject](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Officiële Raspberry Pi-documentatie](https://www.raspberrypi.org/documentation/)
7. [Documentatie over U-Blox-GPS-modules](https://www.u-blox.com/)
8. [OUI-database: IEEE-standaarden](https://standards.ieee.org/products-programs/regauth/)
9. [iptables-handleiding](https://www.netfilter.org/documentation/)
10. [OpenSSL-documentatie](https://www.openssl.org/docs/)
