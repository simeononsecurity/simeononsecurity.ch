---
title: "Firmware personalizat DagShell pentru Orbic RCL400: Ghidul din 2026"
date: 2026-05-28
lastmod: 2026-11-11
toc: true
draft: false
description: "Ghid tehnic pentru firmware-ul DagShell pe Orbic RCL400, cu instalare, instrumente de confidențialitate, wardriving și limitele cercetării."
genre: ["Firmware personalizat", "Securitate mobilă", "Instrumente de confidențialitate", "Securitatea rețelei", "Wardriving", "Testare de penetrare", "Hacking IoT", "Cercetare în securitate", "Hacking hardware", "Tehnologie de confidențialitate"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalizat", "Hacking hotspot", "Instrumente de confidențialitate", "Corecție TTL", "MAC spoofing", "Detectarea IMSI catcher", "Wardriving", "Urmărire GPS", "Atac Evil Twin", "Portal captiv", "Sniffer DNS", "Scaner ARP", "Scaner de porturi", "Companion Raspberry Pi", "Securitate WiFi", "Hotspot mobil", "Monitorizarea rețelei", "Testare de penetrare", "Cercetare în securitate", "Scanare Bluetooth", "Atac de deautentificare", "Scanare WiFi", "Căutare OUI", "Încărcare Wigle", "Monitorizarea turnurilor celulare", "Comenzi AT", "Manager firewall", "Blocare reclame", "Criptare TLS", "Integrare RayHunter", "STS Collective", "Laborator de securitate mobilă", "Analiza rețelei", "Firmware pentru confidențialitate", "Securitate open-source", "Compilare încrucișată ARM", "Linux încorporat", "Set de instrumente de securitate", "Instrumente de hacking", "Red Team", "Recunoașterea rețelei"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Ilustrație cu un hotspot mobil Orbic RCL400 cu interfață verde luminoasă, înconjurat de reprezentări abstracte ale unor instrumente de securitate, precum grafice și hărți, pe fundal bleumarin închis."
coverCaption: ""
---

**Transformă Orbic RCL400 într-un laborator mobil de cercetare în securitate**

## Introducere: un hotspot pentru hackeri

**DagShell** este un firmware personalizat open-source pentru **hotspotul mobil Orbic RCL400**, care transformă un dispozitiv celular obișnuit într-un **set portabil de instrumente pentru cercetare în securitate și confidențialitate**. Creat de cercetătorul în securitate „dag”, firmware-ul cu aspect de terminal oferă **instrumente de hacking, funcții de confidențialitate și monitorizarea rețelei**, într-o interfață elegantă, verde pe negru, cu estetică de hacker.

Acest ghid cuprinzător prezintă:
- Ce este DagShell și toate funcțiile sale
- Instrucțiuni de instalare pas cu pas, prin webflasher sau manual
- Detalii despre toate instrumentele și capacitățile
- Configurarea companionului Raspberry Pi pentru funcții extinse
- De ce să asociezi DagShell cu RayHunter pentru securitate mobilă
- Cazuri reale de utilizare pentru cercetători și susținătorii confidențialității
- Considerații legale și etice

**Pe scurt**: DagShell și RayHunter pe Orbic RCL400 formează un **laborator mobil complet de securitate** pentru detectarea dispozitivelor IMSI catcher, wardriving, analiza rețelei și protejarea confidențialității.

**Dispozitive pre-flash disponibile**: Acest articol este sponsorizat de **STS Collective**, care oferă hotspoturi Orbic RCL400 cu **RayHunter și DagShell** instalate și gata de utilizare: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Reducere exclusivă pentru cititori**: Economisește până la 20% la produsele STS Collective, inclusiv la dispozitivele Orbic RCL400 pre-flash. Folosește codul **SIMEONONSECURITY** la checkout sau [cumpără cu reducerea aplicată](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Ce este DagShell?

### Prezentare generală

**DagShell** este un firmware personalizat open-source care înlocuiește interfața web standard a Orbic RCL400 cu un **set complet de instrumente de securitate**, care include:

- Interfață în stil terminal, cu artă ASCII și estetică de hacker
- Interfață web criptată **TLS 1.2+**, cu certificat autosemnat
- Instrumente de confidențialitate: mascarea TTL, MAC spoofing și blocarea reclamelor prin DNS
- Monitorizarea rețelei: conexiuni active, tabele de rutare și interogări DNS
- Instrumente de hacking: detectarea IMSI catcher, scanarea porturilor și descoperirea ARP
- Capacități de atac: Evil Twin AP, phishing prin portal captiv și atacuri de deautentificare
- Urmărire GPS și wardriving, cu export CSV compatibil Wigle
- Companion Raspberry Pi pentru GPS, scanare Bluetooth și recunoaștere WiFi
- Acces la sistemul de fișiere printr-un manager în browser
- Funcții SMS prin comenzi AT
- Persistență: pornește automat la boot

### Specificații tehnice

**Platformă**: hotspot mobil Orbic RCL400
**Arhitectură**: ARM Linux (kernel 3.18)
**Limbaj**: C/C++ (binar ARM static)
**Criptare**: TLS 1.2+ cu certificate autosemnate (PKI pe două niveluri)
**Server web**: server HTTPS încorporat, personalizat (portul 8443)
**Interfață**: UI de terminal în browser
**Licență**: MIT (open-source)
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Design vizual

DagShell are o **estetică retro de hacker**:
- Logo ASCII pe fiecare pagină
- Culori verde pe negru, în stil Matrix
- Font monospațiat (Fira Code)
- Efecte de scanare și text luminos
- Aspect inspirat de terminal

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware DagShell care rulează pe Orbic RCL400, cu interfață de terminal verde pe negru, artă ASCII și meniu cu instrumente de securitate" >}}

______

## Prezentare completă a funcțiilor

### 🏠 Panou principal

**Prezentarea sistemului**:
- **Afișarea timpului de funcționare** - De cât timp rulează dispozitivul
- **Interfață pentru comenzi AT** - Control direct al modemului pentru utilizatorii avansați
- **Stare rapidă** - Adresa IP și starea conexiunii

**Comenzile AT** permit controlul modemului la nivel inferior:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Instrumente de rețea

**Informații despre rețeaua curentă**:
- Detalii despre adresa IP și interfață
- Mască de subrețea, gateway și adresă broadcast
- Statistici de rețea, cu pachete trimise și primite

**Vizualizatorul tabelei de rutare**:
- Afișează toate rutele de rețea
- Informații despre gateway-ul implicit
- Asocierea interfețelor

**Monitorul conexiunilor active**:
- Listă în timp real cu toate conexiunile TCP/UDP
- Adrese IP locale și la distanță
- Numerele porturilor și starea conexiunilor
- Util pentru a monitoriza cu cine comunică dispozitivul

### 🔒 Set de protecție a confidențialității

#### Corecție TTL

**Scop**: Ascunde traficul hotspotului de detectarea operatorului

**Cum funcționează**:
- Modifică valoarea **Time To Live (TTL)** din pachetele IP la **65**
- Operatorii detectează tethering-ul prin scăderea TTL-ului (telefon=64, dispozitiv tethered=63)
- Valoarea TTL 65 face ca tot traficul să pară local

**Utilizare**: Ocolește restricțiile sau limitarea vitezei impuse de operator pentru tethering

**Comenzi**:
```bash
# Enable TTL fix
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Disable TTL fix  
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Falsificarea adresei MAC

**Scop**: Randomizează adresa MAC a dispozitivului pentru confidențialitate

**Cum funcționează**:
- Schimbă adresa MAC a interfeței WiFi **wlan0**
- Generează o adresă MAC aleatorie sau permite introducerea uneia personalizate
- Face dispozitivul mai greu de urmărit între sesiuni

**Utilizare**: Împiedică rețelele la care te conectezi să urmărească adresa MAC

**Proces**:
1. Interfața se dezactivează
2. Se aplică noua adresă MAC
3. Interfața se activează din nou
4. Conexiunea se restabilește

#### Blocarea reclamelor prin DNS

**Scop**: Blochează reclamele și urmărirea la nivel DNS

**Cum funcționează**:
- Modifică fișierul `/etc/hosts` cu o listă de blocare
- Domeniile din listă se rezolvă la **127.0.0.1** (localhost)
- Blochează reclamele pentru toate dispozitivele conectate

**Utilizare**: Blochează reclamele în toată rețeaua fără configurarea fiecărui dispozitiv

**Sursa listei de blocare**: Domenii obișnuite de reclame și urmărire, lista poate fi personalizată

### 📱 Gestionarea SMS-urilor

**Trimite SMS-uri**:
- Trimite mesaje text modemului prin comenzi AT
- Util pentru notificări la distanță sau testare

**Vezi mesajele**:
- Link către căsuța de mesaje originală Orbic
- Citește mesajele SMS primite

**Comandă AT utilizată**:
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Instrumente de hacking

#### Detector IMSI catcher

**Scop**: Monitorizează informațiile despre antenele celulare pentru anomalii care pot indica dispozitive **IMSI catcher/Stingray**

**Cum funcționează**:
- Solicită modemului date despre antene: Cell ID (identificatorul antenei), LAC (Location Area Code), MCC/MNC (Mobile Country/Network Code), puterea semnalului (RSSI) și generația rețelei (2G/3G/4G)
- Înregistrează schimbările pentru a detecta comutări suspecte între antene
- Stabilește un reper cu antenele obișnuite din zonă

**Indicatori de detectare**:
- Schimbarea bruscă a antenei celulare când dispozitivul stă pe loc
- Trecerea la 2G *(IMSI catcher-ele forțează adesea 2G pentru a elimina criptarea)*
- Apariția unui Cell ID necunoscut
- Semnal slab de la o antenă falsă
- Reconectări frecvente

**Combinarea cu RayHunter**: DagShell monitorizează antenele celulare, iar RayHunter oferă detectarea dedicată a dispozitivelor IMSI catcher prin analize mai sofisticate (vezi secțiunea de mai jos).

#### Scaner de porturi

**Scop**: Scanează adrese IP țintă pentru porturi deschise

**Cum funcționează**:
- Scanarea TCP SYN trimite pachete SYN către porturile țintă
- Detectarea expirării timpului stabilește dacă portul este deschis, închis sau filtrat
- Poate scana un port sau intervale de porturi

**Utilizări**:
- Recunoașterea rețelei
- Descoperirea dispozitivelor IoT
- Auditarea securității rețelelor locale
- Identificarea serviciilor

**Comandă**:
```bash
# Scan ports 1-1000 on target
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Manager de firewall

**Scop**: Blochează sau deblochează adrese IP folosind iptables

**Cum funcționează**:
- Regulile iptables elimină pachetele către sau de la IP-urile specificate
- Regulile salvate persistă după repornire
- Funcționalitate de listă permisă și listă blocată

**Utilizări**:
- Blocarea adreselor IP malițioase
- Prevenirea accesului neautorizat
- Modelarea sau filtrarea traficului
- Control parental

**Comenzi**:
```bash
# Block IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Unblock IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Instrumente de atac

**AVERTISMENT LEGAL IMPORTANT**: Aceste instrumente sunt destinate **NUMAI testării de securitate autorizate**. Utilizarea lor împotriva unor rețele care nu îți aparțin sau pentru care nu ai permisiune scrisă este **ILEGALĂ** în majoritatea jurisdicțiilor. Folosește-le doar în rețele proprii sau în medii de laborator controlate.

#### Sniffer DNS

**Scop**: Înregistrează interogările DNS ale clienților conectați

**Cum funcționează**:
- Înregistrează prin iptables traficul de pe portul 53 (DNS)
- Nu necesită modul promiscuu
- Înregistrează toate cererile DNS ale clienților hotspotului
- Arată site-urile și serviciile accesate de clienți

**Utilizări** (cu autorizare):
- Analiza traficului de rețea
- Monitorizarea propriei familii
- Cercetarea securității pe propriile dispozitive
- Analiza comportamentului malware-ului

*Această funcție colectează metadate, precum domeniile vizitate de clienții conectați. Folosește-o doar în rețele pe care le deții sau le administrezi.*

#### Scaner ARP

**Scop**: Descoperă dispozitive din rețeaua locală

**Cum funcționează**:
- Trimite cereri ARP către toate adresele IP din subrețea
- Dispozitivele răspund cu adresele MAC
- Căutarea OUI identifică producătorul, precum Apple sau Samsung
- Creează o hartă de rețea cu dispozitivele active

**Utilizări**:
- Inventarierea rețelei
- Detectarea dispozitivelor necunoscute
- Analiza rețelelor BYOD
- Descoperirea dispozitivelor IoT

**Exemplu de rezultat**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Scop**: Vizualizează traseul rețelei către destinație

**Cum funcționează**:
- Trimite pachete cu valori TTL în creștere
- Fiecare salt reduce TTL și returnează **ICMP Time Exceeded**
- Dezvăluie routerele și traseul până la destinație
- Măsoară **Round-Trip Time (RTT)** pentru fiecare salt

**Utilizări**:
- Depanarea rețelei
- Analiza rutelor
- Diagnosticarea latenței
- Investigarea peering-ului ISP

#### Evil Twin AP

**Scop**: Creează un punct de acces WiFi fals care clonează SSID-uri existente

**Cum funcționează**:
- Folosește **wlan1**, a doua interfață WiFi disponibilă prin companionul Pi
- Clonează SSID-ul și tipul de criptare ale rețelei țintă
- Capturează clienții care încearcă să se conecteze
- Afișează un portal captiv pentru colectarea acreditărilor

**Scenariu de atac** (mediu de laborator):
1. Scanează rețelele WiFi legitime
2. Creează un AP fals cu același SSID
3. Folosește un atac de deautentificare pentru a deconecta clienții de la AP-ul real
4. Clienții se reconectează automat la AP-ul fals
5. Portalul captiv colectează acreditările

*Detectare: Clienții văd SSID-uri duplicate dacă ambele AP-uri sunt vizibile în același timp.*

#### Portal captiv

**Scop**: Oferă șabloane de pagini de phishing pentru colectarea acreditărilor

**Șabloane incluse**:
- Pagină de autentificare WiFi în stil generic ISP/hotel
- Pagini de autentificare care imită Facebook, Twitter și Instagram
- Portaluri de autentificare corporativă
- Pagini WiFi pentru aeroporturi și cafenele

**Cum funcționează**:
1. AP-ul Evil Twin redirecționează tot traficul către portal
2. Clientul vede pagina de autentificare
3. Clientul introduce acreditările
4. Acreditările sunt înregistrate într-un fișier
5. Clientul primește acces la internet sau vede o eroare

**Scop educațional**: Demonstrează riscurile ingineriei sociale și de ce utilizatorii trebuie să verifice URL-urile

### 📍 Tracker GPS și wardriving

#### Funcționalitatea GPS

**Sursa GPS**: Numai companionul Raspberry Pi
- *Orbic RCL400 **nu are GPS încorporat**. Fără companionul Pi, nu există date de localizare.*
- Pi conectează un dongle GPS USB cu chipset U-Blox 7
- Pi trimite coordonatele către Orbic prin fișiere de date partajate
- Conversia ECEF în latitudine/longitudine se face automat

**Afișare în panou**:
- Latitudine și longitudine în grade zecimale
- Altitudine deasupra nivelului mării
- Starea fixării GPS și precizia
- Actualizare automată la fiecare 5 secunde
- Nu apar solicitări de localizare din browser, deoarece nu se folosește API-ul browserului

**Stare GPS partajată**:
- Datele GPS sunt disponibile tuturor proceselor DagShell
- Wardriving folosește automat GPS-ul
- Funcțiile nu intră în conflict

#### Modul wardriving

**Scop**: Scanează rețele WiFi cu coordonate GPS pentru cartografiere

**Cum funcționează**:
1. Așteaptă o fixare GPS validă, astfel încât să nu fie înregistrate coordonate 0,0
2. Scanează rețele WiFi la fiecare 5 secunde, într-o buclă continuă
3. Înregistrează SSID-ul, BSSID-ul, tipul de criptare (WPA2, WPA3, deschisă), puterea semnalului (RSSI în dBm), numărul canalului, coordonatele GPS și marcajul temporal
4. Exportă datele în format CSV compatibil Wigle

**Integrare Wigle**:
- WiGLE (wigle.net) este un proiect global de cartografiere WiFi
- Fișierul CSV DagShell poate fi încărcat direct pe WiGLE
- Încărcarea se face din browser, pe pagina Files, fără instrumente externe
- Contribuie la baza de date publică a locațiilor WiFi

**Utilizări**:
- Cartografierea acoperirii WiFi
- Analizarea rețelelor pentru ISP-uri
- Analiza puterii semnalului
- Cercetare de securitate pentru rețele deschise și criptare slabă
- Analize bazate pe locație

**Exemplu de format CSV**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Modul wardriving DagShell afișează coordonatele GPS și rețelele WiFi scanate, cu SSID, BSSID, tipul de criptare și puterea semnalului înregistrate într-un CSV compatibil Wigle" >}}

### 🥧 Raspberry Pi Companion

Companionul **Raspberry Pi** extinde capacitățile DagShell prin **hardware extern**:

#### Cerințe hardware

**Minim**:
- **Raspberry Pi 3B+** sau mai nou *(Pi Zero nu furnizează suficientă energie USB pentru periferice)*
- **Adaptor GPS USB** (se recomandă chipsetul U-Blox 7)
- **Sursă de alimentare** *(Pi necesită alimentare separată. Portul USB Orbic nu furnizează suficientă energie.)*

**Opțional**:
- **Adaptor WiFi** (a doua interfață pentru scanare, păstrând conexiunea activă)
- **Adaptor Bluetooth** (dacă Bluetooth-ul integrat al Pi este slab)

#### Modul GPS (U-Blox 7)

**Conexiune**: adaptorul GPS USB se conectează la Pi\
**Protocol**: propoziții NMEA prin port serial\
**Conversie**: Pi convertește automat coordonatele ECEF în latitudine și longitudine\
**Partajarea datelor**: coordonatele GPS sunt scrise într-un **fișier partajat** de pe Orbic

**Analizarea propozițiilor**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Scanare Bluetooth (BLE)

**Scop**: descoperirea dispozitivelor Bluetooth din apropiere

**Cum funcționează**:
- Scanează **anunțurile BLE**
- Captează **adrese MAC**
- Folosește **căutarea OUI** pentru identificarea producătorului
- Înregistrează datele în **format CSV**

**Control de la distanță**:
- Pornirea și oprirea scanării din interfața web DagShell
- Nu este nevoie de conexiune SSH la Pi
- Afișează starea în timp real

**Exemple de utilizare**:
- **Urmărirea și numărarea dispozitivelor**
- **Analiza fluxului de persoane**
- **Descoperirea dispozitivelor Bluetooth**
- **Cercetarea securității IoT**

**Ieșire CSV**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Scanare WiFi

**Scop**: Pi scanează rețele WiFi și trimite datele către Orbic

**Avantaj**: o interfață dedicată scanării, în timp ce **Orbic menține hotspotul activ**

**Cum funcționează**:
- Pi folosește **un al doilea adaptor WiFi** sau adaptorul WiFi integrat, dacă nu este necesar pentru conectivitate
- Scanează **toate canalele** (1-14 la 2,4 GHz și 36-165 la 5 GHz, dacă există suport)
- Trimite rezultatele către Orbic prin spațiul de stocare partajat
- DagShell înregistrează datele în **CSV-ul wardriving**

**Sincronizare**:
- Pi și Orbic se **sincronizează** folosind marcajele temporale GPS
- Previne înregistrările duplicate
- Combină **ambele surse de scanare** într-un singur jurnal

#### Atacuri de deautentificare

**Scop**: deconectarea clienților de la rețele WiFi (pentru testare în laborator)

**Cum funcționează**:
- Trimite **cadre de deautentificare 802.11**
- Falsifică **adresa MAC a punctului de acces**
- Clientul primește de la punctul de acces un mesaj de deconectare
- Clientul **întrerupe conexiunea** și încearcă să se reconecteze

**Metode de control**:
- **Deautentificare unică**: un singur rafal de cadre
- **Deautentificare continuă**: blochează reconectarea (DoS)
- **Control de la distanță**: declanșare din pagina de scanare DagShell

**Exemple de utilizare** (cu autorizare):
- **Eliminarea dispozitivelor neautorizate** din propria rețea
- **Testare de penetrare** cu permisiune
- Atacuri **Evil Twin** în laborator (forțarea clienților să se conecteze la un punct de acces fals)

**⚠️ Avertisment legal**: atacurile de deautentificare sunt **ilegale împotriva rețelelor pe care nu le dețineți**. Pot atrage sancțiuni FCC și acuzații în baza CFAA.

#### Serviciu cu pornire automată

**Serviciu systemd**: companionul Pi pornește automat la boot

**Fișierul serviciului** (`/etc/systemd/system/pi-companion.service`):
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

**Comenzi**:
```bash
# Enable auto-start
sudo systemctl enable pi-companion

# Start service
sudo systemctl start pi-companion

# Check status
sudo systemctl status pi-companion
```

#### Baza de date OUI

**Scop**: identificarea producătorului după adresa MAC

**Bază de date**: API bazat pe prefixul [OUI Master Database](https://standards.ieee.org/products-programs/regauth/)

**Cum funcționează**:
- Extrage **primii 3 octeți** ai adresei MAC (prefixul OUI)
- Interoghează API-ul: `api.example.com/oui/A4:83:E7`
- Returnează **numele producătorului**

**Exemplu**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integrare**: folosit de scanerul ARP, scanerul BLE și funcția de wardriving WiFi

### 📁 Explorator de fișiere

**Scop**: răsfoirea și gestionarea fișierelor de pe dispozitiv

**Locație**: directorul `/data/` (partiție cu drepturi de scriere)

**Capacități**:
- **Răsfoirea fișierelor** și a subdirectoarelor
- **Descărcarea** fișierelor pe computer
- **Ștergerea** fișierelor (cu confirmare)
- **Afișarea dimensiunii fișierelor** și a marcajelor temporale

**Fișiere uzuale**:
- `wardrive_log.csv` - date de scanare WiFi
- `bluetooth_scan.csv` - date despre dispozitivele BLE
- `gps_track.gpx` - trasee GPS
- `dns_queries.log` - solicitări DNS capturate
- `arp_scan.txt` - lista dispozitivelor din rețea

**Încărcare în Wigle**:
- **Încărcare directă din browser** de pe pagina Files
- Autentificare cu un cont WiGLE
- Încarcă fișierul CSV fără a-l descărca mai întâi

______

{{< stscollective-ad "rayhunter" >}}

## Ghid de instalare

### Condiții preliminare

**Echipamente**:
- **Orbic RCL400** hotspot mobil
- **Computer** (Windows, macOS sau Linux)
- **Cablu USB** (dacă firmware-ul se instalează direct)

**Programe**:
- **Python 3** cu modulele `requests` și `cryptography`
- **Browser web** (Chrome, Firefox, Edge, Safari)

**Opțional**:
- **Raspberry Pi 3B+** sau mai nou (pentru GPS și funcții suplimentare)
- **Adaptor GPS USB** (chipset U-Blox 7)

### Metoda 1: Web flasher (recomandată)

**Cea mai simplă metodă**, fără linie de comandă

**Pasul 1**: accesați DagShell Webflasher
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Pasul 2**: generați certificatele PKI
- Apăsați butonul **„Generate Certificates”**
- Browserul generează un **PKI cu două niveluri** (CA rădăcină și certificat de server)
- **Descărcați fișierele**: `root.der` și `server.der`

**Pasul 3**: activați shell-ul root pe Orbic
- Conectați-vă la rețeaua WiFi Orbic
- Introduceți **parola de administrator** în formularul web
- Apăsați **„Enable Shell”**
- Pagina web exploatează API-ul Orbic pentru a deschide un **shell root pe portul 24**

**Pasul 4**: implementați firmware-ul
- Apăsați butonul **„Deploy DagShell”**
- Scriptul încarcă:
  - `orbic_app` (binarul principal al firmware-ului)
  - `root.der` (certificatul rădăcină)
  - `server.der` (certificatul TLS al serverului)
  - `dagshell_boot.sh` (scriptul de persistență)
- Instalarea durează **2-3 minute**

**Pasul 5**: reporniți Orbic
- Opriți și porniți dispozitivul
- DagShell pornește automat la boot

**Pasul 6**: accesați DagShell
- Deschideți browserul la `https://192.168.1.1:8443/`
- Acceptați **avertismentul de securitate** (certificatul este autosemnat, lucru așteptat)
- Autentificați-vă cu datele implicite, dacă vi se solicită

### Metoda 2: Instalare manuală

Pentru **utilizatorii avansați** care doresc să compileze din sursă

#### Pasul 1: Instalați dependențele

**Windows**:
```powershell
# Install Python 3
# Download from python.org

# Install required modules
pip install requests cryptography

# ARM cross-compiler included in gcc_win/ folder
```

**macOS**:
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Install required modules
pip3 install requests cryptography

# ARM toolchain included in gcc_mac/ folder
```

**Linux**:
```bash
# Install Python 3 and pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Install required modules
pip3 install requests cryptography

# Install ARM cross-compiler
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Pasul 2: Clonați depozitul

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Pasul 3: Compilați firmware-ul

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # Generate certificates
.\build.ps1                # Compile firmware
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # Generate certificates
./build.sh                 # Compile firmware (auto-builds BearSSL)
```

**Rezultat**: `orbic_app` (binar ARM static) și fișierele de certificat DER

**⚠️ Notă pentru macOS**: directorul `gcc_mac/` include un lanț de instrumente ARM personalizat, construit cu **crosstool-ng** și destinat antetelor **Linux kernel 3.2**, pentru compatibilitate cu kernelul Orbic 3.18. *Compilatoarele ARM standard din Homebrew vizează nuclee mai noi și **nu vor funcționa**.*

#### Pasul 4: Activați shell-ul root pe Orbic

```bash
# Connect to Orbic WiFi
# Replace YOUR_ADMIN_PASSWORD with actual password

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Aceasta exploatează API-ul web Orbic pentru a deschide un shell root pe **portul 24**.

#### Pasul 5: Implementați firmware-ul

```bash
python deploy_base64.py
```

Acest pas încarcă și instalează:
- `orbic_app` în `/data/orbic_app`
- Certificatele în `/data/root.der` și `/data/server.der`
- Scriptul de boot în `/etc/rc.d/dagshell_boot.sh`

**Persistență**: firmware-ul pornește automat la repornire prin scriptul init

#### Pasul 6: Reporniți și accesați DagShell

```bash
# Reboot Orbic (power cycle or via SSH)
reboot

# After reboot, access DagShell
# Browser: https://192.168.1.1:8443/
```

### Avertisment privind certificatul de securitate

La accesarea DagShell, veți vedea un avertisment **„Not Secure” sau „Not Trusted”**:

**Browsere desktop**:
- Apăsați **„Advanced”**
- Apăsați **„Proceed to 192.168.1.1 (unsafe)”**

**Browsere mobile**:
- Apăsați **„Show Details”**
- Apăsați **„visit this website”**

**De ce apare**:
- Certificatul este **autosemnat** (nu provine de la o CA de încredere precum Let’s Encrypt)
- Dispozitivul nu are certificatul rădăcină în depozitul de certificate de încredere
- *Acesta este un comportament **așteptat** pentru firmware personalizat, nu un indiciu de compromitere*

**Este conexiunea securizată?**:
- **Da**. Conexiunea este criptată cu **TLS 1.2+**
- Datele nu pot fi interceptate
- *Certificatul nu are un lanț de încredere către o CA publică, dar criptarea este reală*

**Opțional**: instalați `root.der` în depozitul de certificate de încredere al dispozitivului pentru a elimina avertismentul

______

## Configurarea companionului Raspberry Pi

Opțional, dar **recomandat insistent** pentru funcționalitate completă

### Configurarea hardware-ului

**Pasul 1**: procurați componentele
- **Raspberry Pi 3B+** sau mai nou ($35-55)
- **Adaptor GPS USB** cu chipset U-Blox 7 ($15-30)
- **Card MicroSD** de minimum 16 GB pentru Pi OS ($10)
- **Sursă de alimentare** pentru Pi ($10)

**Pasul 2**: instalați Raspberry Pi OS
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flash "Raspberry Pi OS Lite" to SD card
# Boot Pi and complete setup
```

**Pasul 3**: conectați adaptorul GPS
- Conectați GPS-ul USB la Pi
- Verificați detectarea cu `lsusb` (ar trebui să apară dispozitivul GPS)
- Verificați portul serial cu `ls /dev/ttyUSB*` sau `ls /dev/ttyACM*`

### Instalarea software-ului

**Pasul 1**: clonați depozitul DagShell pe Pi

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Pasul 2**: Instalați dependențele

```bash
# Update package list
sudo apt-get update

# Install required packages
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Install Python modules
pip3 install pyserial gps3 bluetooth pybluez
```

**Pasul 3**: Configurați serviciul GPS

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

**Pasul 4**: Configurați modulul însoțitor pentru Pi

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

**Pasul 5**: Instalați serviciul systemd

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

**Pasul 6**: Verificați comunicarea

```bash
# Check logs
journalctl -u pi-companion -f

# Should see GPS coordinates being sent to Orbic
```

### Configurarea rețelei

**Option A**: WiFi Connection

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

**Opțiunea B**: Ethernet USB (recomandat)

- Conectați Pi la Orbic prin **cablu USB** (portul USB al Pi la portul USB Orbic)
- Activați **modul USB gadget** pe Pi
- Pi funcționează ca **dispozitiv Ethernet USB**
- *Este mai fiabil decât WiFi pentru transfer continuu de date*
- Pi accesează internetul prin Orbic

**Configurarea USB Gadget**:
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

## De ce să combinați DagShell cu RayHunter?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Diagramă comparativă între wardriving-ul WiFi și instrumentele de atac de rețea DagShell și detectarea anomaliilor de protocol celular RayHunter, ambele rulând pe același hotspot Orbic RCL400" >}}

### Capacități complementare

**DagShell** și **RayHunter** sunt instrumente de securitate **complementare**, care acoperă aspecte diferite ale cercetării în securitate mobilă:

| Funcție | DagShell | RayHunter |
|---------|----------|-----------|
| **Detectarea captatoarelor IMSI** | Monitorizare de bază a turnurilor celulare | Analiză avansată a tiparelor |
| **Urmărire GPS** | Da (prin Pi) | Da (prin modem) |
| **Wardriving WiFi** | Da | Nu |
| **Scanare Bluetooth** | Da (prin Pi) | Nu |
| **Instrumente de rețea** | Da (sniffer DNS, scanare ARP și scanare porturi) | Nu |
| **Instrumente de atac** | Da (Evil Twin, portal captiv, deautentificare) | Nu |
| **Instrumente de confidențialitate** | Da (remediere TTL, falsificare MAC, AdBlock) | Minime |
| **Bază de date a turnurilor celulare** | De bază | Cuprinzătoare |
| **Analiză AI/ML** | Nu | Da (detectarea anomaliilor) |
| **Analiza protocoalelor operatorilor** | Limitată | Aprofundată (SS7/Diameter) |

### Exemple de utilizare complementară

#### 1. Protecție completă împotriva detectoarelor IMSI

**Scenariu**: călătorie într-o zonă cu supraveghere intensă

**Contribuția DagShell**:
- **Monitorizează schimbările turnurilor celulare** în timp real
- **Urmărește poziția GPS** în timpul schimbărilor suspecte
- **Înregistrează datele turnurilor** pentru analiză ulterioară

**Contribuția RayHunter**:
- **Detectarea anomaliilor bazată pe ML** în protocoalele celulare
- **Inspectarea pachetelor SS7/Diameter** pentru atacuri sofisticate
- **Bază de date cu turnuri cunoscute ca sigure** pentru comparație

**Rezultatul combinației**: DagShell oferă **monitorizare continuă**, iar RayHunter oferă **analiză aprofundată**

#### 2. Wardriving în condiții de siguranță

**Scenariu**: cartografierea rețelelor WiFi într-o zonă urbană

**Contribuția DagShell**:
- **Scanare WiFi** cu coordonate GPS
- Instrumente de **analiză a rețelei** (puterea semnalului, criptarea)
- **Export CSV Wigle** pentru cartografiere

**Contribuția RayHunter**:
- **Urmărirea turnurilor celulare** în timpul wardriving-ului
- **Detectarea captatoarelor IMSI** în timp ce scanați rețele WiFi
- **Avertizare** dacă securitatea celulară este compromisă

**Rezultatul combinației**: wardriving în siguranță, cu **vizibilitate asupra securității celulare**

#### 3. Laborator de cercetare în securitate

**Scenariu**: echipă red team sau testare de penetrare

**Contribuția DagShell**:
- **Punct de acces Evil Twin** pentru testarea WiFi
- **Portal captiv** pentru demonstrații de inginerie socială
- **Atacuri de deautentificare** pentru testarea rezilienței
- Instrumente de **recunoaștere a rețelei**

**Contribuția RayHunter**:
- **Detectează dacă sunteți monitorizat** în timpul testării
- Oferă vizibilitate asupra **securității turnurilor celulare**
- Ajută la prevenirea **supravegherii contrare** în timpul testelor

**Rezultatul combinației**: instrumente ofensive cu **vizibilitate defensivă**

#### 4. Călătorii axate pe confidențialitate

**Scenariu**: jurnalist sau activist într-un mediu sensibil

**Contribuția DagShell**:
- **Mascare TTL** pentru ascunderea tethering-ului
- **Falsificare MAC** pentru anonimizarea dispozitivului
- **AdBlock** pentru prevenirea urmăririi
- **Monitorizarea captatoarelor IMSI**

**Contribuția RayHunter**:
- **Detectare avansată a captatoarelor IMSI**
- Detectarea atacurilor **la nivel de protocol**
- Alerte privind **securitatea celulară**

**Rezultatul combinației**: confidențialitate sporită prin **protecție pe mai multe niveluri**

### Instalarea împreună

**Opțiune preinstalată** (cea mai simplă):
- Cumpărați de la **STS Collective**: [Orbic RCL400 cu RayHunter și DagShell preinstalate](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Gata de utilizare** imediat
- Ambele versiuni de firmware sunt **testate și verificate**
- Fără grija instalării

**Instalare DIY**:
1. **Instalați mai întâi RayHunter** (consultați ghidul nostru [Cum să instalați RayHunter: ghid complet](/articles/how-to-flash-rayhunter-devices-complete-guide/))
2. **Apoi instalați DagShell** (cele două pot funcționa împreună)
3. **RayHunter** folosește porturile implicite
4. **DagShell** folosește portul 8443
5. Accesați-le din file diferite ale browserului

**Nu există conflicte**:
- RayHunter folosește porturile **80/443**
- DagShell folosește portul **8443**
- Nu interferează unul cu celălalt
- Funcționează **simultan**

Doriți să evitați instalarea DIY? [Orbic RCL400 cu RayHunter și DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot) preinstalate este gata de utilizare. Codul pentru cititori **SIMEONONSECURITY** oferă o reducere de până la 20% la STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpărați RCL400 cu firmware preinstalat și economisiți 20%
{{< /centerbutton >}}

______

## Exemple practice de utilizare

### Exemplul 1: Cercetător în securitate

**Profil**: tester de penetrare care evaluează securitatea WiFi

**Instrumente DagShell folosite**:
- **Wardriving WiFi** pentru cartografierea rețelelor clientului
- **Scaner ARP** pentru descoperirea dispozitivelor
- **Scaner de porturi** pentru identificarea serviciilor
- **Evil Twin / portal captiv** pentru testarea rezistenței la inginerie socială
- **Explorator de fișiere** pentru extragerea rezultatelor

**Flux de lucru**:
1. Deplasați-vă în jurul perimetrului facilității clientului
2. Folosiți wardriving pentru a cartografia acoperirea WiFi
3. Creați un punct de acces Evil Twin al rețelei clientului, cu permisiune
4. Monitorizați încercările de conectare ale clienților
5. Generați un raport cu datele colectate

**Integrare RayHunter**: ajută cercetătorul să detecteze supravegherea în timpul evaluării

### Exemplul 2: Susținător al confidențialității

**Profil**: jurnalist care călătorește în străinătate

**Instrumente DagShell folosite**:
- **Remediere TTL** pentru ocolirea restricțiilor operatorului
- **Falsificare MAC** pentru anonimizarea dispozitivului
- **Detector de captatoare IMSI** pentru vizibilitate asupra supravegherii
- **Sniffer DNS** pentru verificarea scurgerilor de date ale dispozitivului
- **AdBlock** pentru prevenirea urmăririi

**Flux de lucru**:
1. Activați remedierea TTL înainte de utilizarea dispozitivului
2. Randomizați adresa MAC
3. Monitorizați continuu detectorul de captatoare IMSI
4. Folosiți AdBlock pentru toate dispozitivele conectate
5. Înregistrați activitățile celulare suspecte

**Integrare RayHunter**: detectarea avansată a captatoarelor IMSI depășește monitorizarea de bază

### Exemplul 3: Administrator de rețea

**Profil**: administrator IT care gestionează mai multe facilități

**Instrumente DagShell folosite**:
- **Wardriving WiFi** pentru verificarea acoperirii
- **Scaner ARP** pentru inventarierea dispozitivelor
- **Scaner de porturi** pentru audituri de securitate
- Monitorizarea **conexiunilor active** pentru identificarea traficului neautorizat
- **Manager firewall** pentru blocarea adreselor IP

**Flux de lucru**:
1. Folosiți wardriving pentru a valida acoperirea WiFi a facilității
2. Scanați prin ARP pentru a găsi toate dispozitivele din rețea
3. Scanați porturile serverelor pentru a găsi servicii expuse
4. Blocați prin firewall adresele IP rău intenționate
5. Exportați rapoarte pentru documentare

**Integrare RayHunter**: monitorizarea securității celulare în facilitățile cu dispozitive mobile

### Exemplul 4: Cercetător în securitatea IoT

**Profil**: cercetător care analizează securitatea dispozitivelor IoT

**Instrumente DagShell folosite**:
- **Scaner ARP** cu căutare OUI pentru identificarea dispozitivelor IoT
- **Scaner de porturi** pentru găsirea serviciilor deschise
- **Sniffer DNS** pentru capturarea tiparelor de trafic IoT
- **Scaner Bluetooth** (Pi) pentru dispozitive IoT BLE
- **Traceroute** pentru analiza conectivității

**Flux de lucru**:
1. Implementați Orbic și Pi în mediul de testare
2. Scanați prin ARP pentru a descoperi dispozitive IoT
3. Scanați porturile pentru servicii vulnerabile
4. Scanați BLE pentru dispozitive Bluetooth IoT
5. Analizați prin DNS comportamentul de comunicare cu serverele externe
6. Documentați vulnerabilitățile

**Integrare RayHunter**: detectează conectivitatea celulară a dispozitivelor IoT și monitorizează anomaliile

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagramă cu patru exemple de utilizare combinată a DagShell și RayHunter: cercetător în securitate, susținător al confidențialității, administrator de rețea și cercetător IoT" >}}

______

## Considerații legale și etice

### Cadru legal

**Instrumente precum DagShell se află într-o zonă juridică gri**:

**Utilizări legale**:
✅ **Propriile rețele**: testați propriile dispozitive și rețele
✅ **Testare autorizată**: teste de penetrare cu permisiune scrisă
✅ **Scopuri educaționale**: învățare în laboratoare izolate
✅ **Protecția confidențialității**: remediere TTL și falsificare MAC pe propriul dispozitiv
✅ **Cercetare în securitate**: cercetare de vulnerabilități și divulgare responsabilă

**Utilizări ilegale**:
❌ **Acces neautorizat**: atacarea rețelelor care nu vă aparțin (încălcarea CFAA)
❌ **Atacuri de deautentificare** asupra altor rețele (încălcarea regulilor FCC și posibilă infracțiune gravă)
❌ Atacuri **Evil Twin** împotriva publicului (fraudă prin comunicații, furt de identitate)
❌ **Sniffing DNS** al altor persoane fără consimțământ (interceptare ilegală)
❌ Ocolirea măsurilor de securitate pentru comiterea unei fraude

### Legi de care trebuie să țineți cont

**Statele Unite**:
- **Computer Fraud and Abuse Act (CFAA)**: acces neautorizat la computere sau rețele
- **Wiretap Act**: interceptarea comunicațiilor electronice
- **Reglementările FCC**: interferențe cu frecvențele radio (atacuri de deautentificare)

**Regatul Unit**:
- **Computer Misuse Act 1990**: lege similară cu CFAA
- **Regulation of Investigatory Powers Act (RIPA)**: restricții privind interceptarea

**Uniunea Europeană**:
- **GDPR**: protecția datelor (scanarea BLE/WiFi care identifică persoane)
- *Reglementările locale și aplicarea lor diferă semnificativ de la o țară la alta*

### Ghiduri etice

**Faceți**:
- ✅ Folosiți instrumentele pe **propriile dispozitive** și rețele
- ✅ Obțineți **permisiune scrisă** înainte de testarea sistemelor altora
- ✅ Practicați **divulgarea responsabilă** dacă găsiți vulnerabilități
- ✅ Folosiți instrumentele în **medii educaționale controlate**
- ✅ Protejați-vă propria **confidențialitate**

**Nu faceți**:
- ❌ Nu atacați rețele care nu vă aparțin
- ❌ Nu colectați date de autentificare de la persoane necunoscute
- ❌ Nu interferați cu infrastructura critică
- ❌ Nu folosiți instrumentele în scopuri rău intenționate
- ❌ Nu distribuiți datele capturate

### Declarație privind utilizarea responsabilă

DagShell este un **instrument pentru cercetare în securitate și protecția confidențialității**. Capacitățile sale seamănă cu cele ale unor instrumente profesionale de testare a penetrării, precum **Kali Linux**, **WiFi Pineapple** sau **HackRF**.

**Intenția contează**: aceleași instrumente folosite de **atacatori** sunt folosite și de **profesioniștii în securitate**. Diferența ține de:
- **Autorizare** (permisiunea de a testa)
- **Intenție** (îmbunătățirea securității sau provocarea de daune)
- **Divulgare** (raportarea constatărilor sau exploatarea lor)

Folosiți DagShell **responsabil** și **etic**. *Dacă nu știți dacă o acțiune este legală, opriți-vă și consultați un avocat înainte de a continua.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Cadru legal și etic pentru cercetarea de securitate cu DagShell, cu utilizări autorizate și neautorizate și legile relevante" >}}


______

## Depanare

### Probleme de instalare

**Problemă**: `enable_shell.py` nu reușește să se conecteze

**Soluții**:
- Verificați conexiunea la **WiFi Orbic**
- Confirmați că adresa IP este **192.168.1.1** (implicită)
- Încercați din nou parola de administrator, ținând cont de majuscule
- Verificați accesibilitatea portului 80: `telnet 192.168.1.1 80`

**Problemă**: încărcarea firmware-ului eșuează

**Soluții**:
- Asigurați-vă că shell-ul root a fost activat (`enable_shell.py` a reușit)
- Verificați stabilitatea rețelei (folosiți o conexiune prin cablu, dacă este posibil)
- Încercați `deploy_net.py` în loc de `deploy_base64.py`
- Verificați spațiul disponibil pe partiția `/data`: `df -h /data`

**Problemă**: avertismentul certificatului nu dispare

**Soluții**:
- *Este **normal** pentru certificatele autosemnate, conexiunea rămâne criptată*
- Apăsați „Advanced”, apoi „Proceed anyway” de fiecare dată
- **Opțional**: instalați `root.der` în depozitul de certificate de încredere al dispozitivului (avansat)

### Probleme în timpul funcționării

**Problemă**: DagShell nu pornește la boot

**Soluții**:
- Verificați scriptul de boot: `ls -la /etc/rc.d/dagshell_boot.sh`
- Verificați dacă este executabil: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Consultați jurnalele: `logread | grep dagshell`
- Porniți manual: `/data/orbic_app &`

**Problemă**: GPS-ul nu funcționează

**Soluții**:
- Verificați dacă **companionul Pi** rulează: `systemctl status pi-companion`
- Verificați dacă GPS-ul are semnal de la sateliți: `cgps -s` (pe Pi)
- Verificați dacă adaptorul GPS este conectat: `lsusb`
- *Așteptați 5-10 minute pentru localizarea GPS la pornirea la rece. La prima pornire, localizarea durează mai mult în exterior.*

**Problemă**: wardriving-ul nu înregistrează date

**Soluții**:
- Verificați dacă GPS-ul are localizare înainte de pornire
- Verificați permisiunile de scriere pentru `/data`
- Confirmați crearea fișierului CSV: `ls -la /data/wardrive_log.csv`
- Verificați dacă interfața WiFi este activă: `ifconfig wlan0`

**Problemă**: companionul Pi nu comunică cu Orbic

**Soluții**:
- Verificați conectivitatea: `ping 192.168.1.1`
- Verificați dacă fișierul de configurare conține adresa IP corectă
- Confirmați că portul 8443 este deschis: `telnet 192.168.1.1 8443`
- Consultați jurnalele companionului Pi: `journalctl -u pi-companion`

### Probleme de performanță

**Problemă**: interfața web este lentă sau nu răspunde prompt

**Soluții**:
- Ștergeți memoria cache a browserului
- Dezactivați extensiile browserului (blocatoarele de reclame pot interfera)
- Folosiți o conexiune **prin cablu** la Orbic în loc de WiFi
- Reporniți DagShell: `killall orbic_app && /data/orbic_app &`

**Problemă**: scanările wardriving durează prea mult

**Soluții**:
- Măriți intervalul de scanare din setări, cu frecvență redusă pentru performanță mai bună
- Reduceți numărul de canale scanate
- *Un semnal GPS slab încetinește scanarea. Sistemul așteaptă coordonate valide înainte de înregistrare.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Flux de depanare DagShell cu probleme uzuale de instalare, GPS și wardriving și soluțiile lor pas cu pas" >}}


______

## Configurare avansată

### Personalizarea DagShell

**Modificarea codului sursă**:
- Editați fișierele din directorul `orbic_fw_c/`
- Recompilați cu `build.sh` sau `build.ps1`
- Implementați din nou firmware-ul

**Adăugarea paginilor personalizate**:
- DagShell folosește HTML încorporat în cod C++
- Editați `main.cpp` pentru a adăuga rute noi
- Recompilați și implementați

**Certificat personalizat**:
- Generați propriul PKI cu `gen_pki.py`
- Sau folosiți **OpenSSL** pentru a crea certificate
- Înlocuiți `root.der` și `server.der`

### Integrarea cu alte instrumente

**Exportarea datelor în Wireshark**:
```bash
# Capture pcap file
tcpdump -i wlan0 -w /data/capture.pcap

# Download via file browser
# Open in Wireshark on PC
```

**Importarea traseelor GPS în QGIS**:
```bash
# Export GPX format
python gps_to_gpx.py /data/gps_coords.txt

# Import to QGIS as vector layer
```

**Sincronizarea cu o bază de date externă**:
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

### Optimizarea performanței

**Optimizarea vitezei de scanare**:
```bash
# Edit wardrive scan interval
# In DagShell web UI, change from 5s to 3s for faster scanning
# Trade-off: Higher CPU usage, potential missed networks
```

**Optimizarea bateriei** (dacă folosiți un acumulator extern):
```bash
# Reduce screen brightness on Orbic
# Disable unused features (BT, GPS when not needed)
# Use sleep mode between wardrive sessions
```

______

## Comparație cu alternativele

### DagShell comparativ cu WiFi Pineapple

| Funcție | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Preț** | $60-80 + dispozitiv | $99-299 |
| **Conectivitate celulară** | ✅ LTE 4G integrat | ❌ Nu (doar WiFi) |
| **GPS** | ✅ Prin companionul Pi | ⚠️ Prin adaptor USB |
| **Evil Twin** | ✅ Da | ✅ Da |
| **Portal captiv** | ✅ Da | ✅ Da |
| **Deautentificare** | ✅ Da (prin Pi) | ✅ Da |
| **Wardriving** | ✅ Da | ✅ Da |
| **Detectare IMSI** | ✅ De bază | ❌ Nu |
| **Portabilitate** | ✅ Foarte portabil | ⚠️ Moderată |
| **Baterie** | ✅ Integrată | ⚠️ Necesită baterie externă |
| **Curba de învățare** | Moderată | Redusă (interfață finisată) |

**Recomandare**: DagShell pentru **securitate celulară mobilă**, Pineapple pentru testare **WiFi** cu o interfață simplă

### DagShell comparativ cu Kali Linux pe Pi

| Funcție | DagShell | Kali pe Pi |
|---------|----------|-----------|
| **Timp de configurare** | 15 minute | 2-3 ore |
| **LTE celular** | ✅ Integrat | ❌ Necesită modem USB |
| **Interfață web** | ✅ Da | ⚠️ Limitată (necesită VNC/SSH) |
| **Număr de instrumente** | ~15 | 600+ |
| **Specializare** | Securitate mobilă | Testare generală de penetrare |
| **Portabilitate** | ✅ Încape în buzunar | ⚠️ Necesită ecran și alimentare |
| **Autonomie** | 8-10 ore | 2-4 ore |

**Recomandare**: DagShell pentru sarcini **specifice dispozitivelor mobile**, Kali pentru un set de instrumente **cuprinzător**

### DagShell comparativ cu firmware-ul original Orbic

| Funcție | DagShell | Firmware original |
|---------|----------|----------------|
| **Instrumente de securitate** | ✅ Numeroase | ❌ Niciunul |
| **Funcții de confidențialitate** | ✅ Da | ❌ Minime |
| **Personalizare** | ✅ Complet personalizabil | ❌ Blocat |
| **Wardriving** | ✅ Da | ❌ Nu |
| **GPS** | ✅ Da (prin Pi) | ❌ Nu |
| **Open source** | ✅ Da | ❌ Proprietar |
| **Asistență** | ⚠️ Comunitate | ✅ Oficială |
| **Stabilitate** | ⚠️ Beta | ✅ Producție |

**Recomandare**: DagShell pentru **cercetători**, firmware-ul original pentru **utilizatori ocazionali**

______

## Concluzie: laboratorul mobil complet

**DagShell** transformă hotspotul **Orbic RCL400** într-un **laborator mobil de securitate** cu:

✅ **Protecția confidențialității** (mascare TTL, falsificare MAC, AdBlock)
✅ **Monitorizarea rețelei** (conexiuni, DNS, rutare)
✅ **Instrumente de securitate** (detectare IMSI, scanare porturi, descoperire ARP)
✅ **Capacități de atac** (Evil Twin, portal captiv, deautentificare)
✅ **Wardriving GPS** cu integrare Wigle
✅ **Extindere cu Raspberry Pi** (BLE, WiFi, GPS)
✅ **Portabil și alimentat de baterie**
✅ **Open source și personalizabil**

### Utilizare împreună cu RayHunter

**RayHunter + DagShell** = **platformă completă de securitate mobilă**:
- **RayHunter** oferă detectare avansată a captatoarelor IMSI
- **DagShell** oferă instrumente ofensive și de protecție a confidențialității
- Ambele rulează **simultan** pe același dispozitiv
- **Capacități complementare**, fără suprapuneri
- **Un singur pachet portabil** pentru toate nevoile de securitate mobilă

### Începeți astăzi

**Opțiunea 1: Firmware preinstalat** (cea mai simplă)
- **STS Collective**: [Orbic RCL400 cu RayHunter și DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Ajunge **gata de utilizare**
- Fără grija instalării
- Configurat profesional

**Opțiunea 2: Instalare DIY**
- Urmați acest ghid
- **Gratuită** dacă dețineți un Orbic RCL400
- Învățați procesul de instalare
- Personalizați după nevoi

### Lecturi conexe

- **[Cum să instalați RayHunter: ghid complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** - Instalați RayHunter mai întâi
- **[Comparație între dispozitivele RayHunter: recenzie completă](/articles/rayhunter-device-comparison-2026-complete-review/)** - Alegeți platforma
- **[Proiectul Flock-You: ghid hardware de contrasupraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Alte instrumente de detectare

### Gânduri finale

Fie că sunteți **cercetător în securitate**, **tester de penetrare**, **susținător al confidențialității** sau **administrator de rețea**, DagShell oferă o platformă **portabilă și accesibilă** pentru activități de securitate mobilă.

**Declinare de responsabilitate**: folosiți instrumentele responsabil. Testați numai rețele și dispozitive pe care le dețineți sau pentru care aveți permisiune scrisă. Respectați legea și regulile etice. 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 cu firmware DagShell, folosit ca laborator portabil complet pentru cercetare în securitate mobilă" >}}


______

## Referințe

1. [Depozitul GitHub DagShell](https://github.com/dagnazty/DagShell)
2. [Documentația DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective - dispozitive cu firmware preinstalat](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - proiect de cartografiere WiFi](https://wigle.net/)
5. [Computer Fraud and Abuse Act (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentația oficială Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentația modulului GPS U-Blox](https://www.u-blox.com/)
8. [Baza de date OUI - standarde IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutorial iptables](https://www.netfilter.org/documentation/)
10. [Documentația OpenSSL](https://www.openssl.org/docs/)
