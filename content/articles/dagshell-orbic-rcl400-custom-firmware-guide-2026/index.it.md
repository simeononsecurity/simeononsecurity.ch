---
title: "Firmware personalizzato DagShell per Orbic RCL400: guida 2026"
date: 2026-05-28
lastmod: 2026-11-11
toc: true
draft: false
description: "Guida tecnica al firmware DagShell per Orbic RCL400. Descrive installazione, strumenti per la privacy, wardriving e limiti della ricerca."
genre: ["Firmware personalizzato", "Sicurezza mobile", "Strumenti per la privacy", "Sicurezza di rete", "Wardriving", "Penetration testing", "Hacking IoT", "Ricerca sulla sicurezza", "Hacking hardware", "Tecnologie per la privacy"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalizzato", "Hacking degli hotspot", "Strumenti per la privacy", "Correzione TTL", "Spoofing MAC", "Rilevamento di IMSI catcher", "Wardriving", "Tracciamento GPS", "Attacco Evil Twin", "Captive portal", "Sniffer DNS", "Scanner ARP", "Scanner di porte", "Companion Raspberry Pi", "Sicurezza Wi-Fi", "Hotspot mobile", "Monitoraggio di rete", "Penetration testing", "Ricerca sulla sicurezza", "Scansione Bluetooth", "Attacco di deautenticazione", "Scansione Wi-Fi", "Ricerca OUI", "Caricamento su Wigle", "Monitoraggio delle torri cellulari", "Comandi AT", "Gestore firewall", "Blocco degli annunci", "Crittografia TLS", "Integrazione RayHunter", "STS Collective", "Laboratorio di sicurezza mobile", "Analisi di rete", "Firmware per la privacy", "Sicurezza open source", "Cross-compilazione ARM", "Linux embedded", "Toolkit di sicurezza", "Strumenti per hacker", "Red team", "Ricognizione di rete"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Illustrazione di un hotspot mobile Orbic RCL400 con interfaccia verde luminosa, circondato da rappresentazioni astratte di strumenti di sicurezza come grafici e mappe, su uno sfondo blu navy."
coverCaption: ""
---

**Trasforma Orbic RCL400 in un laboratorio mobile di ricerca sulla sicurezza**

## Introduzione: un hotspot per hacker

**DagShell** è un firmware personalizzato open source per l'**hotspot mobile Orbic RCL400**. Trasforma un normale dispositivo cellulare in un **kit portatile per la ricerca sulla sicurezza e la tutela della privacy**. Il ricercatore di sicurezza noto come "dag" ha creato questo firmware con un'interfaccia in stile terminale. Include **strumenti di hacking, funzioni per la privacy e funzionalità di monitoraggio di rete**, in un'estetica hacker verde su sfondo nero.

Questa guida completa illustra:
- **Cos'è DagShell** e quali funzioni offre
- **Le istruzioni di installazione dettagliate**, tramite webflasher e metodo manuale
- **Tutti gli strumenti e le funzionalità**, spiegati nel dettaglio
- **La configurazione del companion Raspberry Pi** per estendere le funzionalità
- **Perché abbinare DagShell a RayHunter** per la sicurezza mobile
- **Casi d'uso reali** per ricercatori di sicurezza e sostenitori della privacy
- **Considerazioni legali ed etiche**

**In breve:** DagShell e RayHunter su Orbic RCL400 formano un **laboratorio mobile completo di sicurezza** per rilevare IMSI catcher, fare wardriving, analizzare reti e proteggere la privacy.

**Dispositivi con firmware preinstallato:** Questo articolo è sponsorizzato da **STS Collective**, che offre hotspot Orbic RCL400 con RayHunter e DagShell già installati e pronti all'uso: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Sconto esclusivo per i lettori:** Risparmia fino al 20% sui prodotti STS Collective, inclusi i dispositivi Orbic RCL400 con firmware preinstallato. Usa il codice **SIMEONONSECURITY** al pagamento oppure [acquista con lo sconto applicato](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Cos'è DagShell?

### Panoramica

**DagShell** è un firmware personalizzato open source che sostituisce l'interfaccia web di serie di Orbic RCL400 con un **kit completo di strumenti di sicurezza**, che include:

- **Interfaccia in stile terminale** con arte ASCII ed estetica hacker
- **Interfaccia web crittografata con TLS 1.2+** e certificato autofirmato
- **Strumenti per la privacy**, tra cui mascheramento TTL, spoofing MAC e blocco degli annunci tramite DNS
- **Monitoraggio di rete**, connessioni attive, tabelle di routing e query DNS
- **Strumenti di hacking**, rilevamento IMSI catcher, scansione di porte e individuazione ARP
- **Funzionalità di attacco**, Evil Twin AP, captive portal per phishing e attacchi di deautenticazione
- **Tracciamento GPS e wardriving** con esportazione CSV compatibile con Wigle
- **Companion Raspberry Pi** per GPS, scansione Bluetooth e ricognizione Wi-Fi
- **Accesso al file system** con gestore file nel browser
- **Funzionalità SMS** tramite comandi AT
- **Persistenza:** DagShell si avvia automaticamente all'accensione

### Specifiche tecniche

**Piattaforma:** hotspot mobile Orbic RCL400\
**Architettura:** ARM Linux (kernel 3.18)\
**Linguaggio:** C/C++ (binario ARM statico)\
**Crittografia:** TLS 1.2+ con certificati autofirmati (PKI a due livelli)\
**Web server:** server HTTPS embedded personalizzato (porta 8443)\
**Interfaccia:** interfaccia terminale basata su browser\
**Licenza:** MIT (open source)\
**GitHub:** [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Design visivo

DagShell ha un'**estetica hacker retrò**:
- **Logo ASCII** su ogni pagina
- **Palette verde su nero**, in stile Matrix
- **Font monospaziato** (Fira Code)
- **Effetti di linee di scansione** e testo luminoso
- **Layout ispirato al terminale**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware personalizzato DagShell in esecuzione su Orbic RCL400. Mostra l'interfaccia terminale verde su nero con arte ASCII e menu degli strumenti di sicurezza." >}}

______

## Panoramica completa delle funzionalità

### 🏠 Pannello di controllo

**Panoramica del sistema:**
- **Tempo di attività**, da quanto è acceso il dispositivo
- **Interfaccia dei comandi AT**, controllo diretto del modem per utenti esperti
- **Stato rapido**, indirizzo IP e stato della connessione

I **comandi AT** permettono il controllo del modem a basso livello:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Strumenti di rete

**Informazioni sulla rete corrente:**
- **Indirizzo IP e interfaccia**
- **Maschera di sottorete, gateway** e indirizzo broadcast
- **Statistiche di rete**, pacchetti inviati e ricevuti

**Visualizzatore della tabella di routing:**
- Visualizza tutte le route di rete
- Informazioni sul gateway predefinito
- Mappatura delle interfacce

**Monitor delle connessioni attive:**
- Elenco in tempo reale di **tutte le connessioni TCP/UDP**
- Indirizzi IP locali e remoti
- Numeri di porta e stati delle connessioni
- Utile per **monitorare le comunicazioni del dispositivo**
+
### 🛡️ Suite di protezione della privacy

#### Correzione TTL

**Scopo:** mascherare il traffico dell'hotspot per evitare il rilevamento da parte dell'operatore

**Come funziona:**
- Modifica a **65** il valore **Time To Live (TTL)** nei pacchetti IP
- Gli operatori rilevano il tethering tramite la diminuzione del TTL: telefono=64, dispositivo collegato=63
- Impostando il TTL a 65, **tutto il traffico appare locale**

**Caso d'uso:** aggirare le restrizioni o la limitazione della velocità del tethering applicate dall'operatore

**Comandi:**
```bash
# Enable TTL fix
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Disable TTL fix  
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Spoofing dell'indirizzo MAC

**Scopo:** randomizzare l'indirizzo MAC del dispositivo per proteggere la privacy

**Come funziona:**
- Modifica l'indirizzo MAC di **wlan0**, l'interfaccia Wi-Fi
- Genera un **indirizzo MAC casuale** o permette di inserirne uno personalizzato
- Rende il dispositivo **difficile da tracciare** tra una sessione e l'altra

**Caso d'uso:** impedire il tracciamento basato sul MAC da parte delle reti a cui ti connetti

**Procedura:**
1. L'interfaccia si disattiva
2. Viene applicato il nuovo indirizzo MAC
3. L'interfaccia si riattiva
4. La connessione viene ristabilita

#### Blocco degli annunci tramite DNS

**Scopo:** bloccare annunci e tracciamento a livello DNS

**Come funziona:**
- Modifica il file `/etc/hosts` aggiungendo una **blocklist**
- I domini elencati puntano a **127.0.0.1** (localhost)
- Blocca gli annunci **per tutti i dispositivi connessi**

**Caso d'uso:** bloccare gli annunci sull'intera rete senza configurare ogni dispositivo

**Origine della blocklist:** domini comuni di annunci e tracciamento, personalizzabili

### 📱 Gestione degli SMS

**Inviare SMS:**
- Invia messaggi al modem tramite **comandi AT**
- Utile per **notifiche remote** o test

**Visualizzare i messaggi:**
- Collegamento alla casella SMS nativa di Orbic
- Permette di leggere gli SMS ricevuti

**Comando AT utilizzato:**
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Strumenti di hacking

#### Rilevatore di IMSI catcher

**Scopo:** monitorare le informazioni sulle torri cellulari per individuare anomalie che indicano dispositivi **IMSI catcher/Stingray**

**Come funziona:**
- Interroga il modem per ottenere i **dati delle torri cellulari**:
  - **Cell ID**, identificativo della torre
  - **LAC**, codice dell'area di localizzazione
  - **MCC/MNC**, codice del paese e della rete mobile
  - **Potenza del segnale** (RSSI)
  - **Generazione di rete** (2G/3G/4G)
- **Registra le variazioni** per rilevare passaggi sospetti tra torri
- **Stabilisce una base di confronto**, registrando le torri normali nell'area

**Indicatori di rilevamento:**
- **Cambio improvviso di torre** quando il dispositivo è fermo
- **Passaggio a 2G** *(gli IMSI catcher spesso forzano il 2G per rimuovere la crittografia)*
- Comparsa di un **Cell ID sconosciuto**
- **Segnale debole** da una torre falsa
- **Riconnessioni frequenti**

**Integrazione con RayHunter:** DagShell offre **monitoraggio delle torri cellulari**, RayHunter offre **rilevamento dedicato degli IMSI catcher** con analisi più sofisticata. Consulta la sezione successiva.

#### Scanner di porte

**Scopo:** cercare porte aperte sugli indirizzi IP di destinazione

**Come funziona:**
- La scansione **TCP SYN** invia pacchetti SYN alle porte di destinazione
- Il **rilevamento del timeout** determina se una porta è aperta, chiusa o filtrata
- Il **supporto degli intervalli** consente di scansionare una porta o un intervallo

**Casi d'uso:**
- **Ricognizione di rete**
- **Individuazione di dispositivi IoT**
- **Audit di sicurezza** delle reti locali
- **Identificazione dei servizi**

**Comando:**
```bash
# Scan ports 1-1000 on target
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Gestore firewall

**Scopo:** bloccare o sbloccare indirizzi IP tramite iptables

**Come funziona:**
- Le regole **iptables** eliminano i pacchetti provenienti da indirizzi IP specificati o diretti a essi
- Le **regole persistenti** sopravvivono ai riavvii, se salvate
- Funzioni di **whitelist e blacklist**

**Casi d'uso:**
- **Bloccare IP malevoli**
- **Impedire accessi non autorizzati**
- **Gestire o filtrare il traffico**
- **Controllo genitori**

**Comandi:**
```bash
# Block IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Unblock IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Strumenti di attacco

**IMPORTANTE AVVERTENZA LEGALE:** Questi strumenti sono destinati **SOLO a test di sicurezza autorizzati**. Usarli contro reti che non possiedi o per cui non hai un'autorizzazione scritta esplicita è **ILLEGALE** nella maggior parte delle giurisdizioni, per esempio ai sensi del Computer Fraud and Abuse Act negli Stati Uniti e del Computer Misuse Act nel Regno Unito. Usali solo su **reti di tua proprietà** o in **laboratori controllati**.

#### Sniffer DNS

**Scopo:** registrare le query DNS dei client connessi

**Come funziona:**
- **Logging iptables** sulla porta 53 (DNS)
- **Non richiede la modalità promiscuous**
- Registra tutte le richieste DNS dei client dell'hotspot
- Rivela **quali siti e servizi** visitano i client

**Casi d'uso** (autorizzati):
- **Analisi del traffico di rete**
- **Controllo dei figli** sulla rete di famiglia
- **Ricerca sulla sicurezza** dei propri dispositivi
- **Analisi del comportamento di malware**

*Questo strumento raccoglie metadati, cioè i domini visitati dai client connessi. Usalo solo su reti di tua proprietà o che amministri.*

#### Scanner ARP

**Scopo:** individuare dispositivi sulla rete locale

**Come funziona:**
- Invia **richieste ARP** a tutti gli IP della sottorete
- I dispositivi rispondono con i propri **indirizzi MAC**
- La **ricerca OUI** identifica il produttore, per esempio Apple o Samsung
- Crea una **mappa dei dispositivi attivi** sulla rete

**Casi d'uso:**
- **Inventario di rete**
- **Rilevamento di dispositivi sconosciuti**
- **Analisi di reti BYOD**
- **Individuazione di dispositivi IoT**

**Esempio di output:**
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Scopo:** visualizzare il percorso di rete verso la destinazione

**Come funziona:**
- Invia pacchetti con **TTL crescente**
- Ogni hop decrementa il TTL e restituisce **ICMP Time Exceeded**
- Mostra i **router e il percorso** verso la destinazione
- Misura il **tempo di andata e ritorno (RTT)** per ogni hop

**Casi d'uso:**
- **Risoluzione dei problemi di rete**
- **Analisi delle route**
- **Diagnosi della latenza**
- **Analisi dei collegamenti tra ISP**

#### Evil Twin AP

**Scopo:** creare un punto di accesso Wi-Fi falso che duplica l'SSID di una rete esistente

**Come funziona:**
- Usa **wlan1**, la seconda interfaccia Wi-Fi, se disponibile tramite il companion Pi
- Duplica **SSID e tipo di crittografia** della rete obiettivo
- **Cattura i client** che tentano di connettersi
- Mostra un **captive portal** per raccogliere credenziali

**Scenario di attacco** (laboratorio):
1. Scansiona le reti Wi-Fi legittime
2. Crea un **AP falso** con lo stesso SSID
3. Usa un **attacco di deautenticazione** per disconnettere i client dall'AP reale
4. I client si riconnettono automaticamente all'**AP falso**
5. Il captive portal raccoglie le credenziali

*Rilevamento: i client vedono **SSID duplicati** se entrambi gli AP sono visibili nello stesso momento.*

#### Captive portal

**Scopo:** modelli di pagine phishing per raccogliere credenziali

**Modelli inclusi:**
- **Pagina di accesso Wi-Fi**, stile generico di un ISP o hotel
- **Pagine di accesso ai social media**, copie di Facebook, Twitter e Instagram
- **Portali di accesso aziendali**
- **Pagine Wi-Fi** di aeroporti e caffetterie

**Come funziona:**
1. L'Evil Twin AP reindirizza **tutto il traffico** al portale
2. Il client visualizza la **pagina di accesso**
3. Il client inserisce le credenziali
4. Le credenziali vengono **salvate in un file**
5. Il client ottiene accesso a Internet o visualizza un errore

**Scopo didattico:** mostra i rischi dell'**ingegneria sociale** e perché gli utenti devono verificare gli URL

### 📍 Localizzatore GPS e wardriving

#### Funzioni GPS

**Fonte GPS:** solo il **companion Raspberry Pi**
- *Orbic RCL400 **non ha GPS integrato**. Senza il companion Pi, non vengono registrati dati di posizione.*
- Il Pi collega un **ricevitore GPS USB** con chipset U-Blox 7
- Il Pi invia le coordinate a Orbic tramite **file di dati condivisi**
- La conversione **ECEF in latitudine/longitudine** avviene automaticamente

**Visualizzazione nella dashboard:**
- **Latitudine e longitudine** in gradi decimali
- **Altitudine** sul livello del mare
- **Stato del fix GPS** e precisione
- **Aggiornamento automatico** ogni 5 secondi
- **Nessuna richiesta di geolocalizzazione del browser**, l'API del browser non viene usata

**Stato GPS condiviso:**
- I dati GPS sono disponibili a **tutti i processi DagShell**
- Il wardriving usa automaticamente il GPS
- Le funzioni non entrano in conflitto

#### Modalità wardriving

**Scopo:** scansionare reti Wi-Fi con coordinate GPS per mapparle

**Come funziona:**
1. Attende un **fix GPS valido**, senza registrare coordinate 0,0
2. Scansiona le reti Wi-Fi ogni **5 secondi** in un ciclo continuo
3. Registra i dati di rete:
   - **SSID**, nome della rete
   - **BSSID**, indirizzo MAC
   - **Tipo di crittografia**, WPA2, WPA3 o aperta
   - **Potenza del segnale**, RSSI in dBm
   - **Numero del canale**
   - **Coordinate GPS**, latitudine e longitudine
   - **Timestamp**
4. Esporta i dati in formato **CSV compatibile con Wigle**

**Integrazione Wigle:**
- **WiGLE** (wigle.net) è un progetto globale di mappatura Wi-Fi
- Il CSV di DagShell è **caricabile direttamente** su WiGLE
- **Caricamento dal browser** nella pagina File, senza strumenti esterni
- Contribuisce al **database pubblico** delle posizioni Wi-Fi

**Casi d'uso:**
- **Mappatura della copertura Wi-Fi**
- **Rilievi di rete** per ISP
- **Analisi della potenza del segnale**
- **Ricerca sulla sicurezza**, reti aperte e crittografia debole
- **Analisi basate sulla posizione**

**Esempio di formato CSV:**
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="La modalità wardriving di DagShell mostra coordinate GPS e reti Wi-Fi scansionate con SSID, BSSID, tipo di crittografia e potenza del segnale salvati in un CSV compatibile con Wigle." >}}

### 🥧 Companion Raspberry Pi

Il **companion Raspberry Pi** amplia le funzionalità di DagShell con **hardware esterno**:

#### Requisiti hardware

**Minimi:**
- **Raspberry Pi 3B+** o successivo. *(Pi Zero non fornisce alimentazione USB sufficiente per le periferiche.)*
- **Ricevitore GPS USB**, consigliato il chipset U-Blox 7
- **Alimentatore**, *il Pi richiede un'alimentazione separata. La porta USB di Orbic non è sufficiente.*

**Opzionali:**
- **Adattatore Wi-Fi**, seconda interfaccia per scansionare mantenendo il collegamento attivo
- **Adattatore Bluetooth**, se il Bluetooth integrato nel Pi è debole

#### Modulo GPS (U-Blox 7)

**Collegamento:** ricevitore GPS USB collegato al Pi\
**Protocollo:** frasi NMEA tramite porta seriale\
**Conversione:** il Pi converte automaticamente ECEF in latitudine/longitudine\
**Condivisione dei dati:** scrive le coordinate GPS in un **file condiviso** su Orbic

**Analisi della frase NMEA:**
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Scansione Bluetooth (BLE)

**Scopo:** individuare i dispositivi Bluetooth vicini

**Come funziona:**
- Cerca **annunci BLE**
- Acquisisce **indirizzi MAC**
- La **ricerca OUI** identifica il produttore
- Registra i risultati in **formato CSV**

**Controllo remoto:**
- Avvia o interrompe la scansione dall'interfaccia web di DagShell
- Non serve accedere al Pi tramite SSH
- Aggiornamenti dello stato in tempo reale

**Casi d'uso:**
- **Tracciamento e conteggio dei dispositivi**
- **Analisi del passaggio di persone**
- **Individuazione di dispositivi Bluetooth**
- **Ricerca sulla sicurezza IoT**

**Output CSV:**
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Scansione Wi-Fi

**Scopo:** il Pi scansiona le reti Wi-Fi e invia i dati a Orbic

**Vantaggio:** interfaccia dedicata alla scansione mentre **Orbic mantiene l'hotspot attivo**

**Come funziona:**
- Il Pi usa un **secondo adattatore Wi-Fi** o il Wi-Fi integrato, se non serve per la connettività
- Scansiona **tutti i canali**: 1–14 a 2,4 GHz e 36–165 a 5 GHz, se supportato
- Invia i risultati a Orbic tramite spazio di archiviazione condiviso
- DagShell li registra nel **CSV del wardriving**

**Coordinamento:**
- Pi e Orbic **sincronizzano gli orari GPS**
- Evita voci duplicate
- Combina **le due fonti di scansione** in un unico registro

#### Attacchi di deautenticazione

**Scopo:** disconnettere client dalle reti Wi-Fi per test di laboratorio

**Come funziona:**
- Invia **frame di deautenticazione 802.11**
- Falsifica l'**indirizzo MAC dell'AP**
- Il client riceve dall'AP un messaggio di disconnessione
- Il client **perde la connessione** e tenta di riconnettersi

**Metodi di controllo:**
- **Deautenticazione singola:** un unico gruppo di frame
- **Deautenticazione continua:** blocca la riconnessione e provoca un DoS
- **Controllo remoto:** avviato dalla pagina di scansione DagShell

**Casi d'uso** (autorizzati):
- **Rimozione di dispositivi non autorizzati** dalla propria rete
- **Penetration test** autorizzati
- **Attacchi Evil Twin** in laboratorio, per forzare i client verso un AP falso

**⚠️ Avvertenza legale:** gli attacchi di deautenticazione sono **illegali contro reti che non possiedi**. Possono violare le norme FCC e comportare accuse ai sensi del CFAA.

#### Servizio di avvio automatico

**Servizio systemd:** il companion Pi si avvia automaticamente all'accensione

**File del servizio** (`/etc/systemd/system/pi-companion.service`):
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

**Comandi:**
```bash
# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

#### Database OUI

**Scopo:** identificare il produttore dal prefisso dell'indirizzo MAC

**Database:** API basata sui prefissi [OUI Master Database](https://standards.ieee.org/products-programs/regauth/)

**Come funziona:**
- Estrae i **primi 3 byte** dell'indirizzo MAC, il prefisso OUI
- Interroga l'API: `api.example.com/oui/A4:83:E7`
- Restituisce il **nome del produttore**

**Esempio:**
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integrazione:** è usato dallo scanner ARP, dallo scanner BLE e dal wardriving Wi-Fi

### 📁 Esplora file

**Scopo:** esplorare e gestire i file sul dispositivo

**Posizione:** directory `/data/`, partizione scrivibile

**Funzionalità:**
- **Esplorare file** e sottodirectory
- **Scaricare** file sul computer
- **Eliminare** file dopo una conferma
- **Visualizzare dimensioni** e timestamp

**File comuni:**
- `wardrive_log.csv`: dati di scansione Wi-Fi
- `bluetooth_scan.csv`: dati dei dispositivi BLE
- `gps_track.gpx`: tracce GPS
- `dns_queries.log`: query DNS acquisite
- `arp_scan.txt`: elenco dei dispositivi di rete

**Caricamento su Wigle:**
- **Caricamento diretto dal browser** nella pagina File
- Accesso con l'account WiGLE
- Carica il CSV senza scaricarlo prima

______

{{< stscollective-ad "rayhunter" >}}
+
## Guida all'installazione

### Prerequisiti

**Hardware:**
- **Hotspot mobile Orbic RCL400**
- **Computer** Windows, macOS o Linux
- **Cavo USB**, se si installa direttamente il firmware

**Software:**
- **Python 3** con i moduli `requests` e `cryptography`
- **Browser web**, Chrome, Firefox, Edge o Safari

**Opzionale:**
- **Raspberry Pi 3B+** o successivo per GPS e funzioni aggiuntive
- **Ricevitore GPS USB** con chipset U-Blox 7

### Metodo 1: webflasher (consigliato)

**Il metodo più semplice**, non richiede la riga di comando.

**Passaggio 1:** visita il webflasher DagShell.
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Passaggio 2:** genera i certificati PKI.
- Fai clic sul pulsante **"Generate Certificates"**
- Il browser genera una **PKI a due livelli**, CA radice e certificato server
- **Scarica i file:** `root.der` e `server.der`

**Passaggio 3:** abilita la shell root su Orbic.
- Connettiti alla rete Wi-Fi Orbic
- Inserisci la **password amministratore** nel modulo web
- Fai clic su **"Enable Shell"**
- La pagina sfrutta l'API Orbic per aprire una **shell root sulla porta 24**

**Passaggio 4:** installa il firmware.
- Fai clic sul pulsante **"Deploy DagShell"**
- Lo script carica:
  - `orbic_app`, il binario principale del firmware
  - `root.der`, il certificato radice
  - `server.der`, il certificato server TLS
  - `dagshell_boot.sh`, lo script di persistenza
- L'installazione dura **2–3 minuti**

**Passaggio 5:** riavvia Orbic.
- Spegni e riaccendi il dispositivo
- DagShell si avvia automaticamente

**Passaggio 6:** accedi a DagShell.
- Apri nel browser `https://192.168.1.1:8443/`
- Accetta l'**avviso di sicurezza**. Il certificato autofirmato è previsto.
- Se richiesto, accedi con le credenziali predefinite

### Metodo 2: installazione manuale

**Per utenti esperti** che desiderano compilare il firmware dal codice sorgente.

#### Passaggio 1: installa le dipendenze

**Windows:**
```powershell
# Install Python 3
# Download from python.org

# Install required modules
pip install requests cryptography

# ARM cross-compiler included in gcc_win/ folder
```

**macOS:**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Install required modules
pip3 install requests cryptography

# ARM toolchain included in gcc_mac/ folder
```

**Linux:**
```bash
# Install Python 3 and pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install required modules
pip3 install requests cryptography

# Install ARM cross-compiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Passaggio 2: clona il repository

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Passaggio 3: compila il firmware

**Windows:**
```powershell
cd orbic_fw_c
python gen_pki.py          # Generate certificates
.\build.ps1                # Compile firmware
```

**macOS/Linux:**
```bash
cd orbic_fw_c
python3 gen_pki.py         # Generate certificates
./build.sh                 # Compile firmware (auto-builds BearSSL)
```

**Output:** `orbic_app`, binario ARM statico, e i file dei certificati DER.

**⚠️ Nota per macOS:** la cartella `gcc_mac/` contiene una toolchain ARM personalizzata creata con **crosstool-ng** e basata sugli header del kernel **Linux 3.2**, per la compatibilità con il kernel 3.18 di Orbic. *I compilatori ARM standard di Homebrew puntano a kernel più recenti e **non funzionano**.*

#### Passaggio 4: abilita la shell root su Orbic

```bash
# Connect to Orbic WiFi
# Replace YOUR_ADMIN_PASSWORD with actual password

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Questo sfrutta l'API web Orbic per aprire una shell root sulla **porta 24**.

#### Passaggio 5: installa il firmware

```bash
python deploy_base64.py
```

Lo script carica e installa:
- `orbic_app` in `/data/orbic_app`
- I certificati in `/data/root.der` e `/data/server.der`
- Lo script di avvio in `/etc/rc.d/dagshell_boot.sh`

**Persistenza:** il firmware si avvia automaticamente dopo il riavvio tramite uno script init.

#### Passaggio 6: riavvia e accedi

```bash
# Reboot Orbic (power cycle or via SSH)
reboot

# After reboot, access DagShell
# Browser: https://192.168.1.1:8443/
```

### Avviso sul certificato di sicurezza

Quando accedi a DagShell, visualizzerai l'avviso **"Not Secure"** o **"Not Trusted"**.

**Browser desktop:**
- Fai clic su **"Advanced"**
- Fai clic su **"Proceed to 192.168.1.1 (unsafe)"**

**Browser mobile:**
- Tocca **"Show Details"**
- Tocca **"visit this website"**

**Perché succede:**
- Il certificato è **autofirmato**, non proviene da una CA attendibile come Let's Encrypt
- Il dispositivo non ha il certificato radice nel suo archivio attendibile
- *È un comportamento **previsto** per un firmware personalizzato, non un segno di compromissione*

**La connessione è sicura?**
- **Sì.** La connessione è crittografata con **TLS 1.2+**.
- I dati non possono essere intercettati.
- *Il certificato non è collegato a una CA pubblica attendibile, ma la crittografia è attiva.*

**Opzionale:** installa `root.der` nell'archivio dei certificati attendibili del dispositivo per eliminare l'avviso.

______

## Configurazione del companion Raspberry Pi

**Opzionale, ma consigliata** per tutte le funzionalità.

### Configurazione hardware

**Passaggio 1:** procurati i componenti.
- **Raspberry Pi 3B+** o successivo (35–55 USD)
- **Ricevitore GPS USB** con chipset U-Blox 7 (15–30 USD)
- **Scheda microSD** da almeno 16 GB per Pi OS (10 USD)
- **Alimentatore** per Pi (10 USD)

**Passaggio 2:** installa Raspberry Pi OS.
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flash "Raspberry Pi OS Lite" to SD card
# Boot Pi and complete setup
```

**Passaggio 3:** collega il ricevitore GPS.
- Collega il GPS USB al Pi
- Verifica il rilevamento: `lsusb`, dovrebbe mostrare il dispositivo GPS
- Verifica la porta seriale: `ls /dev/ttyUSB*` o `/dev/ttyACM*`

### Installazione del software

**Passaggio 1:** clona il repository DagShell sul Pi.

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Passaggio 2:** installa le dipendenze.

```bash
# Update package list
sudo apt-get update

# Install required packages
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Install Python modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Passaggio 3:** configura il demone GPS.

```bash
# Edit gpsd config
sudo nano /etc/default/gpsd

# Set DEVICES line to your GPS serial port
DEVICES="/dev/ttyUSB0"  # Adjust if different

# Restart gpsd
sudo systemctl restart gpsd

# Test GPS
cgps -s  # Should show satellite data after ~30 seconds
```

**Passaggio 4:** configura il companion Pi.

```bash
# Edit configuration file
nano pi_companion/config.py

# Set Orbic IP address
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Set GPS serial port
GPS_DEVICE = "/dev/ttyUSB0"

# Save and exit
```

**Passaggio 5:** installa il servizio systemd.

```bash
# Copy service file
sudo cp pi_companion.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

**Passaggio 6:** verifica la comunicazione.

```bash
# Check logs
journalctl -u pi-companion -f

# Should see GPS coordinates being sent to Orbic
```

### Configurazione di rete

**Opzione A:** connessione Wi-Fi

```bash
# Pi connects to Orbic hotspot
# Edit wpa_supplicant config
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add network
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Restart WiFi
sudo systemctl restart networking
```

**Opzione B:** Ethernet USB (consigliata)

- Collega il Pi a Orbic con un **cavo USB**, dalla porta USB del Pi a quella di Orbic
- Abilita la **modalità USB gadget** sul Pi
- Il Pi opera come **dispositivo Ethernet USB**
- *È più affidabile del Wi-Fi per il trasferimento continuo di dati*
- Il Pi accede a Internet tramite Orbic

**Configurazione USB gadget:**
```bash
# Edit config.txt
sudo nano /boot/config.txt

# Add at end
dtoverlay=dwc2

# Edit cmdline.txt
sudo nano /boot/cmdline.txt

# Add after rootwait
modules-load=dwc2,g_ether

# Reboot
sudo reboot
```

______

## Perché abbinare DagShell a RayHunter?
+
{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Diagramma affiancato che confronta il wardriving Wi-Fi e gli strumenti di attacco di rete di DagShell con il rilevamento delle anomalie dei protocolli cellulari di RayHunter. Entrambi funzionano sullo stesso hotspot Orbic RCL400." >}}

### Funzionalità complementari

**DagShell** e **RayHunter** sono strumenti di sicurezza **complementari** che coprono aspetti diversi della ricerca sulla sicurezza mobile:

| Funzione | DagShell | RayHunter |
|---------|----------|-----------|
| **Rilevamento IMSI catcher** | Monitoraggio di base delle torri cellulari | Analisi avanzata dei modelli |
| **Tracciamento GPS** | Sì, tramite Pi | Sì, tramite modem |
| **Wardriving Wi-Fi** | Sì | No |
| **Scansione Bluetooth** | Sì, tramite Pi | No |
| **Strumenti di rete** | Sì, sniffer DNS, scansione ARP e porte | No |
| **Strumenti di attacco** | Sì, Evil Twin, captive portal e deautenticazione | No |
| **Strumenti per la privacy** | Sì, correzione TTL, spoofing MAC e blocco annunci | Minimi |
| **Database delle torri cellulari** | Di base | Completo |
| **Analisi AI/ML** | No | Sì, rilevamento anomalie |
| **Analisi dei protocolli degli operatori** | Limitata | Approfondita, SS7/Diameter |

### Casi d'uso combinati

#### 1. **Protezione completa dagli IMSI catcher**

**Scenario:** viaggio in un'area sottoposta a sorveglianza intensa

**Contributo di DagShell:**
- **Monitora i cambi di torre cellulare** in tempo reale
- **Registra la posizione GPS** durante passaggi sospetti
- **Salva i dati delle torri** per analisi successive

**Contributo di RayHunter:**
- **Rilevamento delle anomalie** nei protocolli cellulari basato su ML
- **Ispezione dei pacchetti SS7/Diameter** per attacchi sofisticati
- **Database di torri attendibili** come riferimento

**Risultato combinato:** DagShell offre **monitoraggio continuo**, RayHunter offre **analisi approfondita**.

#### 2. **Wardriving con sicurezza**

**Scenario:** mappatura di reti Wi-Fi in un'area urbana

**Contributo di DagShell:**
- **Scansione Wi-Fi** con coordinate GPS
- Strumenti di **analisi di rete**, potenza del segnale e crittografia
- **Esportazione CSV per Wigle** per creare mappe

**Contributo di RayHunter:**
- **Tracciamento delle torri cellulari** durante il wardriving
- **Rilevamento degli IMSI catcher** durante le scansioni Wi-Fi
- **Avvisi in caso di compromissione della sicurezza cellulare**

**Risultato combinato:** wardriving con consapevolezza della **sicurezza cellulare**.

#### 3. **Laboratorio di ricerca sulla sicurezza**

**Scenario:** esercitazione red team o penetration test

**Contributo di DagShell:**
- **Evil Twin AP** per test Wi-Fi
- **Captive portal** per dimostrazioni di ingegneria sociale
- **Attacchi di deautenticazione** per testare la resilienza
- Strumenti di **ricognizione di rete**

**Contributo di RayHunter:**
- **Rileva se sei monitorato** durante i test
- Aumenta la consapevolezza della **sicurezza delle torri cellulari**
- **Limita il rischio di contro-sorveglianza** durante le verifiche

**Risultato combinato:** strumenti offensivi con **consapevolezza difensiva**.

#### 4. **Viaggi all'insegna della privacy**

**Scenario:** giornalista o attivista in un ambiente delicato

**Contributo di DagShell:**
- **Mascheramento TTL** per nascondere il tethering
- **Spoofing MAC** per l'anonimato
- **Blocco degli annunci** per impedire il tracciamento
- **Monitoraggio degli IMSI catcher**

**Contributo di RayHunter:**
- **Rilevamento avanzato degli IMSI catcher**
- Rilevamento di attacchi **a livello di protocollo**
- **Avvisi sulla sicurezza cellulare**

**Risultato combinato:** maggiore privacy con **protezione a più livelli**.

### Installazione congiunta

**Opzione preinstallata** (la più semplice):
- Acquista da **STS Collective**: [Orbic RCL400 con RayHunter e DagShell preinstallati](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Pronto all'uso** appena tolto dalla confezione
- Entrambi i firmware sono **stati testati e verificati**
- **Nessuna difficoltà di installazione**

**Installazione fai da te:**
1. **Installa prima RayHunter**, consulta la guida [Come installare RayHunter sui dispositivi](/articles/how-to-flash-rayhunter-devices-complete-guide/)
2. Poi **installa DagShell**, i due firmware possono coesistere
3. **RayHunter** usa le porte predefinite
4. **DagShell** usa la porta 8443
5. Accedi a entrambi da schede diverse del browser

**Nessun conflitto:**
- RayHunter usa le porte **80/443**
- DagShell usa la porta **8443**
- Non interferiscono tra loro
- Funzionano **contemporaneamente**

Preferisci evitare l'installazione fai da te? L'**[Orbic RCL400 con RayHunter e DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** preinstallati è pronto all'uso. Il codice lettore **SIMEONONSECURITY** offre fino al 20% di sconto presso STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acquista RCL400 preinstallato e risparmia il 20%
{{< /centerbutton >}}

______

## Casi d'uso reali

### Caso d'uso 1: ricercatore di sicurezza

**Profilo:** penetration tester che valuta la sicurezza Wi-Fi

**Strumenti DagShell usati:**
- **Wardriving Wi-Fi** per mappare le reti del cliente
- **Scanner ARP** per individuare dispositivi
- **Scanner di porte** per identificare servizi
- **Evil Twin e captive portal** per testare la resilienza all'ingegneria sociale
- **Esplora file** per estrarre i risultati

**Flusso di lavoro:**
1. Percorri il perimetro della struttura del cliente
2. Usa il wardriving per mappare la copertura Wi-Fi
3. Crea un Evil Twin della rete del cliente, con autorizzazione
4. Monitora i tentativi di connessione dei client
5. Prepara un rapporto con i dati raccolti

**Integrazione RayHunter:** aiuta il ricercatore a verificare di non essere sorvegliato durante la valutazione.

### Caso d'uso 2: sostenitore della privacy

**Profilo:** giornalista in viaggio all'estero

**Strumenti DagShell usati:**
- **Correzione TTL** per aggirare le restrizioni dell'operatore
- **Spoofing MAC** per l'anonimato del dispositivo
- **Rilevatore di IMSI catcher** per controllare i rischi di sorveglianza
- **Sniffer DNS** per verificare che il dispositivo non invii dati
- **Blocco degli annunci** per impedire il tracciamento

**Flusso di lavoro:**
1. Abilita la correzione TTL prima di usare il dispositivo
2. Randomizza l'indirizzo MAC
3. Monitora continuamente il rilevatore di IMSI catcher
4. Usa il blocco degli annunci per tutti i dispositivi collegati
5. Registra attività cellulari sospette

**Integrazione RayHunter:** rileva gli IMSI catcher in modo più avanzato rispetto al monitoraggio di base.

### Caso d'uso 3: amministratore di rete

**Profilo:** amministratore IT responsabile di più sedi

**Strumenti DagShell usati:**
- **Wardriving Wi-Fi** per verificare la copertura
- **Scanner ARP** per inventariare i dispositivi
- **Scanner di porte** per gli audit di sicurezza
- **Monitor delle connessioni attive** per il traffico non autorizzato
- **Gestore firewall** per bloccare indirizzi IP

**Flusso di lavoro:**
1. Verifica la copertura Wi-Fi della struttura con il wardriving
2. Individua i dispositivi di rete con la scansione ARP
3. Scansiona i server per identificare servizi esposti
4. Blocca gli IP malevoli tramite firewall
5. Esporta i rapporti per la documentazione

**Integrazione RayHunter:** monitora la sicurezza cellulare nelle strutture con dispositivi mobili.

### Caso d'uso 4: ricercatore di sicurezza IoT

**Profilo:** ricercatore che analizza la sicurezza dei dispositivi IoT

**Strumenti DagShell usati:**
- **Scanner ARP con ricerca OUI** per identificare i dispositivi IoT
- **Scanner di porte** per trovare servizi aperti
- **Sniffer DNS** per acquisire i modelli di traffico IoT
- **Scanner Bluetooth** tramite Pi per i dispositivi BLE IoT
- **Traceroute** per analizzare la connettività

**Flusso di lavoro:**
1. Installa Orbic e Pi nell'ambiente di test
2. Individua i dispositivi IoT con lo scanner ARP
3. Cerca servizi vulnerabili con lo scanner di porte
4. Scansiona i dispositivi IoT Bluetooth con BLE
5. Analizza il traffico "phone home" con lo sniffer DNS
6. Documenta le vulnerabilità

**Integrazione RayHunter:** rileva la connettività cellulare dei dispositivi IoT e controlla le anomalie.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagramma di quattro casi d'uso reali combinati per DagShell e RayHunter: ricercatore di sicurezza, sostenitore della privacy, amministratore di rete e ricercatore IoT." >}}

______

## Considerazioni legali ed etiche

### Quadro giuridico

**Gli strumenti come DagShell si trovano in una zona grigia legale.**

**Usi legali:**
✅ **Reti proprie**, testa i tuoi dispositivi e le tue reti\
✅ **Test autorizzati**, ottieni un permesso scritto prima di verificare sistemi altrui\
✅ **Formazione**, impara in laboratori isolati\
✅ **Protezione della privacy**, usa correzione TTL e spoofing MAC sul tuo dispositivo\
✅ **Ricerca sulla sicurezza**, segnala le vulnerabilità in modo responsabile\

**Usi illegali:**
❌ **Accesso non autorizzato**, attaccare reti altrui può violare il CFAA\
❌ **Attacchi di deautenticazione** su reti altrui, violazioni FCC e possibili accuse penali\
❌ Attacchi **Evil Twin** contro il pubblico, frode telematica e furto di identità\
❌ **Sniffing DNS** altrui senza consenso\
❌ **Elusione delle protezioni** per commettere frodi\

### Leggi da conoscere

**Stati Uniti:**
- **Computer Fraud and Abuse Act (CFAA)**, accesso non autorizzato a computer e reti
- **Wiretap Act**, intercettazione delle comunicazioni elettroniche
- **Norme FCC**, interferenze radio, inclusi gli attacchi di deautenticazione

**Regno Unito:**
- **Computer Misuse Act 1990**, simile al CFAA
- **Regulation of Investigatory Powers Act (RIPA)**, restrizioni sulle intercettazioni

**Unione Europea:**
- **GDPR**, protezione dei dati, inclusi quelli identificativi raccolti tramite BLE e Wi-Fi
- *Le norme locali e la loro applicazione variano da paese a paese.*

### Linee guida etiche

**DA FARE:**
- ✅ Usa gli strumenti sui **tuoi dispositivi e sulle tue reti**
- ✅ Ottieni un'**autorizzazione scritta** prima di testare sistemi altrui
- ✅ **Segnala responsabilmente** le vulnerabilità trovate
- ✅ Usa gli strumenti per la **formazione** in ambienti controllati
- ✅ Proteggi la **tua privacy**

**DA NON FARE:**
- ❌ Non attaccare reti che non possiedi
- ❌ Non raccogliere credenziali di estranei
- ❌ Non interferire con infrastrutture critiche
- ❌ Non usare gli strumenti in modo malevolo
- ❌ Non distribuire i dati acquisiti

### Dichiarazione sull'uso responsabile

DagShell è uno **strumento di ricerca sulla sicurezza e tutela della privacy**. Le sue funzionalità sono simili a quelle di strumenti professionali per i penetration test come **Kali Linux**, **WiFi Pineapple** e **HackRF**.

**Conta l'intento:** gli stessi strumenti sono usati da **hacker malevoli** e **professionisti della sicurezza**. Le differenze sono:
- **Autorizzazione**, il permesso di eseguire i test
- **Intento**, migliorare la sicurezza o causare danni
- **Divulgazione**, segnalare i risultati o sfruttarli

Usa DagShell **in modo responsabile ed etico**. *Se non sai se un'attività è legale, fermati e consulta un avvocato prima di procedere.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Quadro legale ed etico per la ricerca sulla sicurezza con DagShell: usi autorizzati e non autorizzati e leggi applicabili." >}}

______

## Risoluzione dei problemi
+
### Problemi di installazione

**Problema:** `enable_shell.py` non riesce a connettersi

**Soluzioni:**
- Verifica di essere connesso al **Wi-Fi Orbic**
- Controlla che l'indirizzo IP sia **192.168.1.1**, quello predefinito
- Riprova la password amministratore, distinguendo maiuscole e minuscole
- Verifica che la porta 80 sia accessibile: `telnet 192.168.1.1 80`

**Problema:** il caricamento del firmware non riesce

**Soluzioni:**
- Abilita prima la shell root. `enable_shell.py` deve riuscire.
- Controlla la stabilità della rete. Se possibile, usa una connessione cablata.
- Prova `deploy_net.py` invece di `deploy_base64.py`
- Verifica lo spazio disponibile sulla partizione `/data`: `df -h /data`

**Problema:** l'avviso del certificato non scompare

**Soluzioni:**
- *È **normale** con certificati autofirmati. La connessione resta crittografata.*
- Fai clic su "Advanced" e poi su "Proceed anyway" ogni volta
- **Opzionale:** installa `root.der` nell'archivio attendibile del dispositivo, se hai esperienza

### Problemi durante l'esecuzione

**Problema:** DagShell non si avvia all'accensione

**Soluzioni:**
- Controlla lo script di avvio: `ls -la /etc/rc.d/dagshell_boot.sh`
- Verifica che sia eseguibile: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Controlla i log: `logread | grep dagshell`
- Avvialo manualmente: `/data/orbic_app &`

**Problema:** il GPS non funziona

**Soluzioni:**
- Verifica che il **companion Pi** sia in esecuzione: `systemctl status pi-companion`
- Controlla che il GPS abbia agganciato i satelliti: `cgps -s` sul Pi
- Verifica che il ricevitore GPS sia collegato: `lsusb`
- *Un fix GPS a freddo può richiedere 5–10 minuti. Al primo avvio il fix richiede più tempo all'aperto.*

**Problema:** il wardriving non registra i dati

**Soluzioni:**
- Verifica che il GPS abbia un fix prima di avviare la scansione
- Controlla i permessi di scrittura di `/data`
- Verifica che venga creato il CSV: `ls -la /data/wardrive_log.csv`
- Controlla che l'interfaccia Wi-Fi sia attiva: `ifconfig wlan0`

**Problema:** il companion Pi non comunica con Orbic

**Soluzioni:**
- Verifica la connettività di rete: `ping 192.168.1.1`
- Controlla che il file di configurazione contenga l'IP corretto
- Verifica che la porta 8443 sia aperta: `telnet 192.168.1.1 8443`
- Controlla i log del companion Pi: `journalctl -u pi-companion`

### Problemi di prestazioni

**Problema:** l'interfaccia web è lenta o poco reattiva

**Soluzioni:**
- Svuota la cache del browser
- Disattiva le estensioni del browser. I blocchi degli annunci interferiscono.
- Usa una connessione **cablata** a Orbic invece del Wi-Fi
- Riavvia DagShell: `killall orbic_app && /data/orbic_app &`

**Problema:** le scansioni di wardriving richiedono troppo tempo

**Soluzioni:**
- Aumenta l'intervallo di scansione nelle impostazioni, riducendo la frequenza per migliorare le prestazioni
- Riduci il numero di canali scansionati
- *Un fix GPS debole rallenta le scansioni. Il sistema attende coordinate valide prima di registrare i dati.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Procedura di risoluzione dei problemi DagShell per errori comuni di installazione, GPS e wardriving, con soluzioni passo per passo." >}}

______

## Configurazione avanzata

### Personalizzazione di DagShell

**Modifica del codice sorgente:**
- Modifica i file nella directory `orbic_fw_c/`
- Ricompila con `build.sh` o `build.ps1`
- Installa di nuovo il firmware

**Aggiunta di pagine personalizzate:**
- DagShell incorpora HTML nel codice C++
- Modifica `main.cpp` per aggiungere nuove route
- Ricompila e installa

**Certificato personalizzato:**
- Genera la tua PKI con `gen_pki.py`
- Oppure usa **OpenSSL** per creare i certificati
- Sostituisci `root.der` e `server.der`

### Integrazione con altri strumenti

**Esportazione dei dati in Wireshark:**
```bash
# Capture pcap file
tcpdump -i wlan0 -w /data/capture.pcap

# Download via file browser
# Open in Wireshark on PC
```

**Importazione delle tracce GPS in QGIS:**
```bash
# Export GPX format
python gps_to_gpx.py /data/gps_coords.txt

# Import to QGIS as vector layer
```

**Sincronizzazione con un database esterno:**
```python
# Custom script to upload wardrive data to MySQL
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

### Ottimizzazione delle prestazioni

**Velocizzare la scansione:**
```bash
# Edit wardrive scan interval
# In DagShell web UI, change from 5s to 3s for faster scanning
# Trade-off: Higher CPU usage, potential missed networks
```

**Ottimizzazione della batteria** (se usi un pacco batteria):
```bash
# Reduce screen brightness on Orbic
# Disable unused features (BT, GPS when not needed)
# Use sleep mode between wardrive sessions
```

______

## Confronto con le alternative

### DagShell o WiFi Pineapple

| Funzione | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|-------------------------|----------------|
| **Prezzo** | 60–80 USD più il dispositivo | 99–299 USD |
| **Cellulare** | ✅ 4G LTE integrato | ❌ No, solo Wi-Fi |
| **GPS** | ✅ Tramite companion Pi | ⚠️ Tramite ricevitore USB |
| **Evil Twin** | ✅ Sì | ✅ Sì |
| **Captive portal** | ✅ Sì | ✅ Sì |
| **Deautenticazione** | ✅ Sì, tramite Pi | ✅ Sì |
| **Wardriving** | ✅ Sì | ✅ Sì |
| **Rilevamento IMSI** | ✅ Di base | ❌ No |
| **Portabilità** | ✅ Elevata | ⚠️ Media |
| **Batteria** | ✅ Integrata | ⚠️ Serve una batteria esterna |
| **Curva di apprendimento** | Media | Bassa, interfaccia curata |

**Scelta:** DagShell per la **sicurezza cellulare mobile**, Pineapple per test **specifici del Wi-Fi** con un'interfaccia semplice.

### DagShell o Kali Linux su Pi

| Funzione | DagShell | Kali su Pi |
|---------|----------|-----------|
| **Tempo di configurazione** | 15 minuti | 2–3 ore |
| **LTE cellulare** | ✅ Integrato | ❌ Richiede modem USB |
| **Interfaccia web** | ✅ Sì | ⚠️ Limitata, richiede VNC/SSH |
| **Numero di strumenti** | Circa 15 | Oltre 600 |
| **Specializzazione** | Sicurezza mobile | Penetration testing generale |
| **Portabilità** | ✅ Tascabile | ⚠️ Richiede schermo e alimentazione |
| **Durata della batteria** | 8–10 ore | 2–4 ore |

**Scelta:** DagShell per attività **specifiche per dispositivi mobili**, Kali per un toolkit **completo**.

### DagShell o firmware di serie Orbic

| Funzione | DagShell | Firmware di serie |
|---------|----------|-------------------|
| **Strumenti di sicurezza** | ✅ Estesi | ❌ Nessuno |
| **Funzioni per la privacy** | ✅ Sì | ❌ Minime |
| **Personalizzazione** | ✅ Completa | ❌ Bloccata |
| **Wardriving** | ✅ Sì | ❌ No |
| **GPS** | ✅ Sì, tramite Pi | ❌ No |
| **Open source** | ✅ Sì | ❌ Proprietario |
| **Supporto** | ⚠️ Community | ✅ Ufficiale |
| **Stabilità** | ⚠️ Beta | ✅ Produzione |

**Scelta:** DagShell per i **ricercatori**, firmware di serie per gli **utenti occasionali**.

______

## Conclusione: il laboratorio mobile definitivo

**DagShell** trasforma l'**hotspot Orbic RCL400** in un **potente laboratorio mobile di sicurezza** con:

✅ **Protezione della privacy**, mascheramento TTL, spoofing MAC e blocco degli annunci\
✅ **Monitoraggio di rete**, connessioni, DNS e routing\
✅ **Strumenti di hacking**, rilevamento IMSI, scansione di porte e individuazione ARP\
✅ **Funzionalità di attacco**, Evil Twin, captive portal e deautenticazione\
✅ **Wardriving GPS** con integrazione Wigle\
✅ **Espansione Raspberry Pi**, BLE, Wi-Fi e GPS\
✅ **Portabilità e alimentazione a batteria**\
✅ **Open source e personalizzabile**

### Insieme a RayHunter

**RayHunter e DagShell** costituiscono una **piattaforma mobile completa per la sicurezza**:
- **RayHunter** offre rilevamento avanzato degli IMSI catcher
- **DagShell** offre strumenti offensivi e per la privacy
- Entrambi funzionano **contemporaneamente** sullo stesso dispositivo
- Le loro funzionalità sono **complementari e senza sovrapposizioni**
- Un **unico kit portatile** copre tutte le esigenze di sicurezza mobile

### Inizia oggi

**Opzione 1: dispositivo preinstallato** (la più semplice)
- **STS Collective**: [Orbic RCL400 con RayHunter e DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Arriva **pronto all'uso**
- Nessuna difficoltà di installazione
- Configurato professionalmente

**Opzione 2: installazione fai da te**
- Segui questa guida
- È **gratuita** se possiedi un Orbic RCL400
- Impara il processo di installazione
- Personalizza il sistema secondo le tue esigenze

### Letture correlate

- **[Come installare RayHunter sui dispositivi: guida completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)**, installa prima RayHunter
- **[Confronto dei dispositivi RayHunter: recensione completa](/articles/rayhunter-device-comparison-2026-complete-review/)**, scegli la piattaforma
- **[Progetto Flock-You: guida all'hardware anti-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**, altri strumenti di rilevamento

### Considerazioni finali

DagShell offre una piattaforma **portatile, potente e conveniente** per il lavoro sulla sicurezza mobile a **ricercatori di sicurezza**, **penetration tester**, **sostenitori della privacy** e **amministratori di rete**.

**Dichiarazione di non responsabilità:** usa gli strumenti responsabilmente. Testa solo reti e dispositivi di tua proprietà o per cui hai un'autorizzazione scritta esplicita. Rispetta la legge e l'etica. Buon hacking! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 con firmware DagShell che funge da laboratorio portatile completo per la ricerca sulla sicurezza mobile." >}}

______

## Riferimenti

1. [Repository DagShell su GitHub](https://github.com/dagnazty/DagShell)
2. [Documentazione DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective, dispositivi preinstallati](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE, progetto di mappatura Wi-Fi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentazione ufficiale Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentazione del modulo GPS U-Blox](https://www.u-blox.com/)
8. [Database OUI, standard IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutorial iptables](https://www.netfilter.org/documentation/)
10. [Documentazione OpenSSL](https://www.openssl.org/docs/)
