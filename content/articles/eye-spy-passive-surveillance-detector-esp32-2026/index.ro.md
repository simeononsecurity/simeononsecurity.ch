---
title: "Eye Spy: detector pasiv de supraveghere și trackere pentru ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Referință tehnică pentru Eye Spy v1.1, un detector pasiv BLE și WiFi pentru ESP32, care detectează camere, trackere, drone și semnale asociate."
genre: ["Instrumente de confidențialitate", "Contrasupraveghere", "Securitatea IoT", "Sisteme integrate", "Cercetare de securitate", "Securitate WiFi", "Securitate Bluetooth", "Proiecte ESP32", "Securitate hardware", "Securitate cu cod sursă deschisă"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Detectarea supravegherii", "Contrasupraveghere", "Detectare BLE", "Scanare WiFi", "Detectare AirTag", "Detectare ALPR", "Flock Safety", "Detectarea camerelor corporale", "Detectarea dronelor", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Cod cu sursă deschisă", "Confidențialitate", "BLE pasiv", "Mod monitor", "Detectare OUI", "Detectarea trackerelor", "Cameră corporală Axon", "Ray-Ban Meta", "Samsung SmartTag", "Tracker Tile", "Cameră ascunsă", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Ilustrație a unui M5Stack Atom Lite mic, înconjurat de unde colorate de semnal pe un fundal bleumarin închis, care simbolizează detectarea supravegherii prin Bluetooth și WiFi."
coverCaption: ""
---

**Un senzor pasiv de dimensiunea unui deget mare care te anunță când ceva te observă**

## Introducere: peisajul de supraveghere pe care nu-l vezi

Lumea fizică este tot mai echipată cu dispozitive care observă, înregistrează și urmăresc: cititoare de plăcuțe de înmatriculare la intersecții, camere corporale ale forțelor de ordine, camere în locuințe închiriate, trackere comerciale asemănătoare cu AirTag, ascunse în genți sau mașini, și camere de supraveghere la intrările magazinelor. Majoritatea acestor dispozitive comunică fără fir prin **Bluetooth LE** sau **WiFi**. *Cele mai multe astfel de comunicări sunt transmise în spațiu deschis și pot fi detectate de oricine are receptorul potrivit.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) este un instrument pasiv de detectare a supravegherii care exploatează exact acest fapt. Eye Spy rulează pe **M5Stack Atom Lite**, o placă de dezvoltare ESP32-PICO-D4 de mărimea aproximativă a unui cub de zahăr, și monitorizează continuu benzile BLE și WiFi pentru semnăturile electronice ale dispozitivelor de înregistrare, camerelor de supraveghere, sistemelor **ALPR** (cititoare automate de plăcuțe de înmatriculare), dronelor și trackerelor personale. Când detectează un semnal, schimbă culoarea LED-ului RGB.

*Nu se conectează la nimic și nu transmite.* Observă, calculează scoruri și se aprinde.

Acest articol este o referință tehnică completă. Explică ce detectează Eye Spy, cum funcționează modelul de scor de încredere, proiectarea motoarelor de detecție, cum să construiești și să programezi dispozitivul și care sunt limitele sale practice.

**Preferi să nu construiești unul?** STS Collective oferă **[detectoare Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** preprogramate și gata de utilizare. Codul pentru cititori **SIMEONONSECURITY** oferă până la 20% reducere.

{{< stscollective-ad "eyespy" >}}

---

## Indicatori LED: întreaga interfață de utilizare

La fel ca [ESP32 WiFi Canary: detectarea pasivă a amenințărilor pe 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), Eye Spy folosește un singur NeoPixel RGB SK6812, conectat la GPIO 27 al M5Stack Atom Lite, pentru toată ieșirea. LED-ul comunică permanent unul dintre cele patru niveluri de amenințare:

| Culoare | Semnificație | Intervalul scorului |
|-------|-------------|---------------------|
| 🔵 Puls albastru | Pornire / prima scanare | -- |
| 🟢 Verde continuu | Nu s-a detectat nimic | 0–2 |
| 🟡 Galben continuu | Atenție: este posibil să existe un dispozitiv de înregistrare în apropiere | 3–5 |
| 🔴 Roșu intermitent | Alertă: a fost detectat un dispozitiv de supraveghere sau urmărire | 6+ |

**O singură detectare cu încredere ridicată (cameră corporală Axon, cameră Flock Safety, potrivire OUI ALPR sau AirTag) adaugă suficiente puncte pentru a aprinde imediat LED-ul roșu într-un singur ciclu de detecție.** Mai multe detectări cu încredere medie se acumulează până la galben și se pot combina pentru a ajunge la roșu.

---

## Hardware

### Ținta principală: M5Stack Atom Lite

| Componentă | Detaliu |
|-----------|--------|
| Placă | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 pe GPIO 27 |
| Buton | GPIO 39 (doar intrare) |
| Flash | 4 MB |

Atom Lite este o platformă completă și autonomă. **Nu sunt necesare lipire, breadboard sau componente externe.** Conectează-l la USB și pornește.

### ESP32 DevKit generic

Un al doilea mediu de compilare PlatformIO (`esp32dev`) vizează orice placă ESP32 DevKit standard cu un LED integrat pe GPIO 2. Toată logica de detecție funcționează identic. Această versiune este utilă pentru dezvoltare și testarea logicii de detecție sau pentru implementare când nu este necesar formatul Atom Lite.

---

## Sistemul de scor

Eye Spy folosește un **model de scor al încrederii** care reunește semnalele tuturor motoarelor de detecție într-un singur număr întreg. Scorul controlează starea LED-ului (verde, galben sau roșu) și este gestionat prin două mecanisme automate:

### Reducerea scorului

În absența unor detectări noi, scorul scade **cu 1 punct la fiecare 60 de secunde**. Dacă te îndepărtezi de dispozitivul detectat, LED-ul revine la verde în câteva minute, fără intervenție.

### Pauza până la recalcularea scorului

Fiecare *tip* de detecție are o **pauză de 120 de secunde** înainte ca aceeași sursă să poată adăuga din nou puncte. *Astfel, un singur dispozitiv persistent nu poate acumula puncte la nesfârșit.* O cameră Flock Safety aflată în raza de acțiune adaugă +5 o dată, apoi așteaptă 120 de secunde înainte să contribuie din nou.

Împreună, aceste mecanisme înseamnă că:

- **Detectările trecătoare** (de exemplu, o mașină cu AirTag care trece) se rezolvă automat.
- **Supravegherea persistentă** (de exemplu, camere corporale instalate într-o locație fixă) menține LED-ul în alertă cât timp rămâi în raza de acțiune.
- **Un singur dispozitiv nu provoacă acumularea necontrolată a scorului** prin detectări repetate.

---

## Motoare de detecție

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagramă a motoarelor BLE și WiFi paralele din Eye Spy, care caută AirTaguri, camere corporale, sisteme ALPR și drone și trimit rezultatele către modelul de amenințare bazat pe scorul de încredere" >}}

Eye Spy alternează continuu între trei faze de scanare:

**BLE pasiv (9 s) → scanare WiFi (~3 s) → captură promiscuă (5 s) → repetare**

Eye Spy oprește explicit BLE înaintea oricărei operațiuni WiFi pentru a respecta utilizarea comună a radioului ESP32. BLE repornește la începutul fiecărui ciclu.

---

### Motorul 1: BLE, scanare pasivă

Scanarea BLE folosește **NimBLE fără transmiterea solicitărilor de scanare**. Dispozitivul ascultă pachetele de publicitate BLE fără să răspundă. *Astfel, Eye Spy este invizibil electronic pentru echipamentele pe care le caută: ținta nu poate detecta un scanner pasiv.*

Dispozitivele cu semnal sub **−90 dBm** sunt ignorate pentru a reduce rezultatele fals pozitive în medii aglomerate.

#### Tabel de detectare BLE

| # | Țintă | Metodă de detecție | Scor |
|---|--------|-----------------|-------|
| 1 | **Cameră corporală Axon** | OUI MAC BLE `00:25:df` (camere corporale, dispozitive Taser și echipamente de ordine publică Axon) | +5 🔴 |
| 2 | **Ochelari inteligenți Ray-Ban Meta** | UUID al serviciului BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE Flock Safety** | Numele dispozitivului BLE conține `Flock`, `Penguin`, `Pigvision` sau `FS Ext Battery` | +5 🔴 |
| 4 | **Dispozitiv de clonare a cardurilor (HC-03/05/06)** | Nume BLE exact: module Bluetooth întâlnite în suprapuneri de terminale de plată | +5 🔴 |
| 5 | **Apple AirTag** | Datele producătorului `0x004C`, subtipul `0x12`/`0x1E` sau payload brut `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Dronă (OpenDroneID BLE)** | UUID al serviciului BLE `0xFFFA` sau payload de date al serviciului AD cu codul aplicației `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID al serviciului BLE `0xFD5A` | +3 🟡 |
| 8 | **Tracker Tile** | UUID al serviciului BLE `0xFEED` sau `0xFEEC` | +3 🟡 |
| 9 | **Nod MeshCore** | Prefixul numelui dispozitivului BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (urmărire în magazine și spații publice)** | Datele producătorului `0x004C 0x02 0x15`, folosite în magazine, aeroporturi și stadioane pentru urmărirea mișcărilor | +2 🟡 |
| 11 | **Dispozitiv persistent necunoscut** | MAC BLE neclasificat, detectat de cel puțin 3 ori în cel puțin 5 minute (detectarea dispozitivelor de recunoaștere sau urmărire) | +2 🟡 |

#### Detalii despre detectări BLE importante

**Cameră corporală Axon (+5)**: Axon (fostă TASER International) produce unele dintre cele mai răspândite sisteme de camere corporale pentru forțele de ordine din Statele Unite. OUI-ul `00:25:df` este înregistrat pe numele Axon și apare în echipamentele sale purtabile. **O singură detectare atinge imediat pragul de alertă.**

**Ochelari inteligenți Ray-Ban Meta (+5)**: Colaborarea Ray-Ban Meta produce ochelari inteligenți pentru consumatori, capabili să înregistreze video și să facă fotografii. UUID-ul serviciului BLE `0xFD5F` este anunțul caracteristic al acestor dispozitive. *Sunt produse de consum și pot apărea în spații publice aglomerate.* Merită atenție orice detectare la acest nivel, indiferent de intenția persoanei care îi poartă.

**Module Bluetooth în dispozitivele de clonare a cardurilor (+5)**: HC-03, HC-05 și HC-06 sunt module Bluetooth seriale ieftine, găsite frecvent în suprapuneri pentru terminale de plată și echipamente de clonare a bancomatelor. Detectarea compară numele exact al dispozitivului cu numele implicite cunoscute din firmware-ul acestor module. **O alertă roșie justifică inspectarea fizică imediată a terminalelor de plată din apropiere.**

**Apple AirTag (+4)**: AirTagurile transmit anunțuri folosind protocolul proprietar Apple **Nearby Interaction**. Detectarea caută antetul datelor specific producătorului (`0x004C` = Apple) și subtipurile specifice AirTag (`0x12` pentru anunțul standard, `0x1E` pentru anunțul unui obiect pierdut). Tiparele payloadului brut oferă o cale suplimentară de detectare.

**OpenDroneID BLE (+4)**: Standardul **ASTM F3411 Remote ID**, adoptat și de FAA pentru drone comerciale în SUA, definește un protocol de difuzare prin care dronele își anunță identitatea și poziția. Eye Spy caută UUID-ul serviciului GATT `0xFFFA` (serviciul Remote ID desemnat) și codul aplicației `0x0D` în payloadul datelor serviciului AD. *O dronă comercială apropiată, conformă standardului, va declanșa această detectare.*

**Dispozitiv persistent necunoscut (+2)**: Acesta este motorul de **detectare a urmăritorilor**. Înregistrează orice MAC BLE care nu este clasificată de detectările specifice de mai sus. Punctele se acordă dacă aceeași MAC neclasificată apare de cel puțin trei ori într-un interval de cel puțin cinci minute. Trackerul de persistență monitorizează până la 50 de MAC-uri necunoscute simultan și șterge intrările după 30 de minute fără semnal. **Astfel pot fi detectate trackere personalizate sau modificate, care nu corespund niciunui UUID de serviciu sau tipar de producător cunoscut.**

**iBeacon (+2)**: Magazinele, aeroporturile și stadioanele folosesc formatul Apple iBeacon (`0x4C 0x00 0x02 0x15`) pentru urmărirea mișcării dispozitivelor în spații fizice. Detectarea se declanșează la formatul standard de anunț, indiferent de UUID; vizează tipul de implementare, nu un UUID anume. *O detectare aici înseamnă că probabil te afli într-o locație care urmărește activ prezența dispozitivelor Bluetooth.*

---

### Motorul 2: scanare WiFi, căutare activă pe canale

Motorul de scanare WiFi folosește interfața standard ESP32 pentru scanarea punctelor de acces, enumeră punctele apropiate și compară BSSID-urile și SSID-urile acestora cu amprentele cunoscute ale dispozitivelor de supraveghere.

#### Tabel de detectare WiFi

| # | Țintă | Metodă de detecție | Scor |
|---|--------|-----------------|-------|
| 12 | **Cameră Flock Safety (OUI)** | BSSID corespunde tabelului Flock Safety cu 22 de OUI-uri (`d4:bb:e6`, `3c:61:05` și prefixe FS-Ext-Battery) | +5 🔴 |
| 13 | **Cameră ALPR / LPR (OUI)** | BSSID corespunde OUI-ului `00:0e:58` pentru Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID cu termeni Flock** | SSID conține `flock`, `flocksafety`, `fs ext`, `penguin` sau `pigvision` | +5 🔴 |
| 15 | **SSID cu termeni ALPR** | SSID conține `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` sau `automate` | +4 🔴 |
| 16 | **Producător de camere de supraveghere (OUI)** | BSSID corespunde unui tabel cu 31 de OUI-uri de camere: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix sau Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID cu termeni pentru camere** | SSID conține, printre altele, `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` sau `genetec` | +2 🟡 |

#### Tabelul OUI Flock Safety

Tabelul `FLOCK_OUIS` cu 22 de intrări este cea mai detaliată căutare din proiect. Acoperă:

- `d4:bb:e6`: OUI Flock Safety înregistrat la IEEE.
- `3c:61:05`: OUI Flock Safety înregistrat la IEEE.
- Alte 20 de prefixe MAC observate în teren pe baterii Flock FS-Ext-Battery și camere WiFi Flock.

Aceste 22 de intrări reprezintă intervale de MAC hardware observate pe sisteme de camere ALPR Flock Safety instalate. **Detectarea prin OUI este independentă de SSID**: o cameră Flock cu un SSID fără termeni de recunoaștere primește tot +5 dacă OUI-ul BSSID se potrivește.

OUI-urile Flock Safety și Vigilant Solutions se află în tabele separate, astfel încât ambele pot contribui independent în același ciclu de scanare. *O locație cu dispozitive de la ambii furnizori poate acumula +10 într-o singură scanare WiFi.*

#### Tabelul OUI pentru producătorii de camere de supraveghere

Tabelul cu 31 de camere acoperă principalii producători de camere IP ale căror dispozitive pot apărea în magazine, spații comerciale și locuințe:

- **Companii și spații comerciale**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix și Genetec.
- **Consumatori și birouri mici**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex și Amcrest.
- **Infrastructură**: Ubiquiti UniFi (punctele de acces și camerele împart intervale OUI) și FLIR.

O potrivire acordă +3 puncte, în nivelul de atenție, fără confirmarea unui termen. Dacă se potrivește și un SSID cu un termen de recunoaștere, aceeași rețea de camere primește +3 pentru OUI și încă +2 pentru SSID, ajungând la nivelul de alertă într-un singur ciclu de scanare.

---

### Motorul 3: WiFi promiscuu, captură pasivă de cadre

Motorul promiscuu trece radioul ESP32 în **mod monitor** și capturează cadre de management 802.11 brute. Astfel poate detecta dispozitive care nu anunță un SSID, în special drone care folosesc protocolul **Remote ID** prin **WiFi Neighbor Awareness Networking (NaN)**.

În timpul fazei promiscuue, radioul **schimbă canalele** `{1, 6, 11, 3, 8, 13}` la fiecare 400 ms pentru a extinde acoperirea canalelor de difuzare a cadrelor NaN ale dronelor.

#### Tabel de detectare promiscuă

| # | Țintă | Metodă de detecție | Scor |
|---|--------|-----------------|-------|
| 18 | **Dronă (OpenDroneID WiFi NaN)** | Cadru de management 802.11 către destinația `51:6f:9a:01:00:00`: difuzare Remote ID ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: Standardul ASTM F3411 definește adresa multicast `51:6f:9a:01:00:00` pentru toate cadrele Remote ID WiFi NaN. Dronele comerciale reglementate care transmit poziția și identitatea prin WiFi trimit cadre către această adresă. Eye Spy ascultă cadre de management adresate acestei MAC multicast: detectarea este pasivă și fiabilă. *Operatorul dronei ar trebui să dezactiveze complet Remote ID pentru a evita detectarea, încălcând astfel reglementările aplicabile.*

Această detectare completează motorul OpenDroneID BLE (detectarea nr. 6). *O dronă se poate anunța prin BLE, WiFi sau ambele, în funcție de hardware și configurație.* Eye Spy le acoperă pe amândouă.

---

## Programarea fazelor și gestionarea radioului

```
BLE pasiv (9 s) → scanare WiFi (~3 s) → captură promiscuă (5 s) → repetare
```

ESP32-PICO-D4 are **un singur radio partajat de 2,4 GHz** pentru BLE și WiFi. Eye Spy îl gestionează cu atenție:

1. **Faza BLE** (9 secunde): stiva NimBLE este activă și rulează scanarea pasivă, fără solicitări de scanare transmise.
2. **Oprirea BLE**: stiva BLE este oprită explicit înainte de utilizarea WiFi.
3. **Scanarea WiFi** (~3 secunde): scanare activă a punctelor de acces pe toate canalele, cu potrivire OUI și SSID.
4. **Captura promiscuă** (5 secunde): captură pasivă de cadre 802.11 cu schimbarea canalelor.
5. **Oprirea WiFi**: WiFi este oprit, iar BLE repornește pentru ciclul următor.

Gestionarea explicită a fazelor previne conflictele radio și oferă motoarelor BLE și WiFi acces organizat la radio în fiecare ciclu.

---

## Ieșire serială

Toate liniile au prefixul `[eyespy]` pentru a putea fi filtrate ușor. Monitorul serial rulează la **115200 baud**.

### Pornire

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Ciclu normal

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Evenimente de detecție

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

Câmpul `tracked=N` arată câte MAC-uri BLE unice se află în prezent în trackerul de persistență. Ajută la înțelegerea densității mediului BLE.

### Câmpurile scorului

Fiecare linie de stare include:

- **score**: scorul curent al amenințării.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: motorul activ (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: numărul MAC-urilor BLE unice din tabelul de persistență.

---

## Compilare și încărcare

### Cerințe

- **PlatformIO** (CLI sau extensie VS Code).
- **M5Stack Atom Lite** sau orice ESP32 DevKit.
- Cablu USB-C.

### Dependențe

PlatformIO le instalează automat:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** controlează LED-ul RGB SK6812. **NimBLE-Arduino** oferă stiva de scanare BLE pasivă. Este preferată bibliotecii BLE ESP32 implicite deoarece acceptă corect modul pasiv, evită transmiterea solicitărilor de scanare și folosește mai puțină memorie.

### Încărcare pe M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Compilează și încarcă pentru Atom Lite
pio run -e atom-lite -t upload

# Deschide monitorul serial la 115200 baud
pio device monitor -b 115200
```

### Încărcare pe un ESP32 DevKit generic

```bash
pio run -e esp32dev -t upload
```

### Structura proiectului

```
eye-spy/
├── src/
│   └── main.cpp          # Toată logica firmware-ului
├── platformio.ini         # Medii de compilare (atom-lite, esp32dev)
├── partitions_4mb.csv     # Tabel de partiții flash de 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*Mediul `atom-lite` folosește definiția de placă `m5stick-c`, cu același cip ESP32-PICO-D4 și o mapare compatibilă a pinilor pentru NeoPixel pe GPIO 27.*

---

## Note despre detectare și limitări practice

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Ilustrație în stil fotografic a Eye Spy pe M5Stack Atom Lite, de mărimea aproximativă a unui cub de zahăr, ținut între două degete pentru a arăta dimensiunea compactă" >}}

### Ce nu poate face Eye Spy

**WiFi de 5 GHz**: ESP32 este un dispozitiv **numai de 2,4 GHz**. Camerele de supraveghere, sistemele ALPR și punctele de acces care funcționează exclusiv la 5 GHz nu vor fi vizibile pentru motoarele de scanare WiFi sau captură promiscuă. *Multe camere IP moderne acceptă și 2,4 GHz, chiar dacă sunt compatibile și cu 5 GHz. Dispozitivele exclusiv 5 GHz nu vor fi detectate.*

**BLE criptat**: Unele produse avansate de supraveghere criptează sau obfuschează anunțurile BLE. Eye Spy detectează dispozitivele care transmit în clar semnături identificabile, precum OUI, UUID-uri de servicii și date ale producătorului. *Dispozitivele care schimbă adrese MAC, o funcție de confidențialitate tot mai frecventă la trackerele de consum, evită detectarea bazată pe MAC.* Trackerul de persistență le poate detecta doar dacă schimbă adresa la intervale mai mari de cinci minute.

**Camere cablate**: **Camerele IP conectate prin Ethernet și fără radio WiFi nu emit semnale wireless pe care Eye Spy să le poată detecta.** Nici camerele ascunse fără conexiune la rețea, care înregistrează doar local, nu produc o semnătură RF.

**Limite de rază**: În interior, raza practică de recepție a semnalelor puternice cu antena ESP32 este de **20–40 de metri**, mai mică pentru semnale slabe sau obstrucționate. *Dispozitivele aflate la limita razei sau în spatele unei ecranări RF importante pot să nu primească puncte ori pot fi sub pragul RSSI de −90 dBm.*

### Rezultate fals pozitive de așteptat

**Camere de consum în locuințele vecinilor**: Camerele Ring, Nest, Wyze, Arlo și Reolink sunt răspândite în cartierele rezidențiale, iar OUI-urile lor apar în tabelul celor 31 de camere. *În zone rezidențiale, așteaptă-te la câteva avertizări galbene (+3) de la camerele de sonerie ale vecinilor.* Nu sunt rezultate fals pozitive în sens tehnic, deoarece dispozitivul detectează *într-adevăr* o cameră. Contextul contează.

**Implementări iBeacon în magazine**: Marile lanțuri de magazine instalează infrastructură iBeacon în aproape fiecare locație. *O vizită la un mall sau supermarket va declanșa probabil detectarea iBeacon (+2).* Dispozitivul funcționează corect: infrastructura comercială de urmărire există.

**Infrastructura Ubiquiti UniFi**: Punctele de acces UniFi apar în tabelul OUI al camerelor deoarece Ubiquiti fabrică atât echipamente de rețea, cât și camere de securitate cu intervale OUI suprapuse. *O rețea cu echipamente UniFi poate primi +3 pentru potrivirile OUI din motorul de scanare WiFi.*

**Samsung SmartTag și dispozitive de consum**: UUID-ul SmartTag (`0xFD5A`) este un serviciu înregistrat de Samsung. *SmartTagurile sunt trackere de consum cu utilizări personale legitime.* Prezența unui SmartTag în apropiere declanșează detectarea.

### Semnificația practică a fiecărui nivel de scor

| Scor | Situație probabilă în lumea reală |
|-------|-----------------------------|
| 6–10 (🔴) | Detectare credibilă cu încredere ridicată: cameră Axon la aproximativ 30 m, cameră Flock Safety cu OUI potrivit, tipar confirmat de urmărire AirTag sau dronă care transmite Remote ID |
| 3–5 (🟡) | Mai multe trackere de consum, puncte cumulate de la camerele vecinilor, posibilă cameră Flock sau o singură detectare OpenDroneID |
| 0–2 (🟢) | Nu au fost detectate semnături importante de supraveghere; există comunicări obișnuite ale dispozitivelor de consum, dar scorul este sub prag |

---

## Comparație cu proiecte similare

Eye Spy vizează supravegherea fizică din mediul înconjurător; [ESP32 WiFi Canary: detectarea pasivă a amenințărilor pe 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) detectează atacurile WiFi de rețea împotriva propriilor dispozitive. *Sunt instrumente complementare pentru modele de amenințare diferite.*

| Capacitate | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Detectarea AirTag și a trackerelor | ✅ | ❌ |
| Detectarea camerelor ALPR / Flock | ✅ | ❌ |
| Detectarea camerelor corporale | ✅ | ❌ |
| Detectarea dronelor (Remote ID) | ✅ | ❌ |
| Detectarea punctelor de acces evil twin | ❌ | ✅ |
| Detectarea atacurilor de deautentificare | ❌ | ✅ |
| Detectarea retrogradării securității | ❌ | ✅ |
| Învățarea unei linii de bază | ❌ | ✅ |
| BLE pasiv | ✅ | ❌ |
| Aceeași platformă hardware | ✅ | ✅ |

Ambele proiecte rulează pe același hardware M5Stack Atom Lite, folosesc aceiași indicatori LED și același sistem de compilare PlatformIO. Pentru monitorizarea supravegherii fizice și a celei de rețea, poți încărca fiecare proiect pe o unitate Atom Lite diferită și le poți purta pe amândouă.

Eye Spy completează și [proiectul de detectare Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) pentru utilizatorii preocupați în special de infrastructura de supraveghere ALPR.

---

## Cazuri de utilizare

### Conștientizarea supravegherii din apropiere

Publicul principal al Eye Spy este format din persoanele care vor să cunoască infrastructura de supraveghere din jurul lor. În timpul unei plimbări prin cartier, al trecerii cu mașina pe lângă o intersecție sau al participării la un eveniment public, Eye Spy transformă analiza RF complexă într-o **singură stare LED în timp real**.

### Detectarea hărțuirii cu AirTag

Urmărirea unei persoane cu AirTag este o problemă documentată. **Motorul de detectare a urmăritorilor** din Eye Spy (o MAC BLE necunoscută și persistentă, observată de cel puțin 3 ori în minimum 5 minute) vizează trackerele personalizate sau modificate care nu corespund formatului cunoscut de anunț Apple. Împreună cu detectarea directă a AirTag, oferă **două metode independente pentru a identifica un tracker care te urmărește**.

### Inspectarea unei locuințe închiriate sau a unei camere de hotel

Dacă intri într-o cameră de hotel sau într-o locuință nouă cu Eye Spy pornit, obții o primă indicație despre dispozitive BLE și WiFi neașteptate. O potrivire SSID cu termeni pentru camere sau un OUI de supraveghere în scanarea WiFi adaugă puncte de atenție. *Nu înlocuiește o scanare RF adecvată*, dar adaugă un nivel pasiv de verificare ambientală la inspecția fizică.

### Implementări ALPR și cercetarea confidențialității

Cercetătorii care documentează infrastructura de supraveghere, jurnaliștii care lucrează în medii monitorizate și susținătorii confidențialității pot folosi Eye Spy ca dispozitiv portabil și accesibil. Ieșirea serială înregistrează fiecare detecție cu RSSI, fiind potrivită pentru colectarea simplă de date.

### Securitate în călătorii

La fel ca WiFi Canary, Eye Spy este conceput pentru călătorii. Atom Lite încape în orice buzunar sau se poate atașa la o geantă. În aeroporturi, gări sau evenimente publice cu supraveghere densă, oferă monitorizare pasivă continuă fără să necesite interacțiune.

---

## Note despre arhitectură

### De ce contează BLE pasiv

Alegerea scanării BLE pasive, fără pachete de solicitare a scanării, are consecințe importante pentru securitate. Într-o scanare BLE standard, scannerul transmite un pachet **SCAN_REQ** pentru a solicita date publicitare suplimentare de la fiecare emițător. *Astfel, scanarea BLE activă este observabilă de ambele dispozitive*: dispozitivul scanat vede adresa scannerului în solicitare.

Modul pasiv NimBLE ascultă numai anunțurile nedirecționate (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) și nu transmite niciodată SCAN_REQ. **Eye Spy nu transmite nimic prin BLE în timpul fazei de scanare.** O cameră corporală Axon, un dispozitiv Flock sau un AirTag detectat nu poate observa și nici nu poate reacționa la prezența scannerului.

### Proiectarea trackerului de persistență

Trackerul dispozitivelor necunoscute menține un tabel cu până la **50 de adrese MAC BLE**, împreună cu momentele primei și ultimei detectări. Detectarea pornește când o MAC apare de cel puțin trei ori într-o perioadă de minimum cinci minute.

Limita de 50 de intrări și ștergerea după 30 de minute sunt decizii de proiectare care echilibrează sensibilitatea detectării cu limitele RAM ale ESP32. *În medii BLE dense (transport, conferințe, malluri), tabelul se poate umple rapid cu dispozitive de consum.* Pragul RSSI de −90 dBm filtrează dispozitivele îndepărtate și păstrează atenția trackerului pe sursele persistente din apropiere.

### Interacțiunea dintre reducerea scorului și pauză

**Pauza de 120 de secunde înainte de recalculare** împiedică un dispozitiv aflat permanent în rază să acumuleze puncte la fiecare ciclu BLE de nouă secunde. Fără pauză, o singură cameră Flock ar adăuga +5 la fiecare 15 secunde și ar ajunge la sute de puncte în câteva minute.

**Reducerea scorului cu 1 punct la fiecare 60 de secunde** îl face să scadă după ce un dispozitiv iese din rază și pauza expiră fără o nouă declanșare. *O detectare unică de +5 care nu se repetă scade la zero în cinci minute.* Astfel, dispozitivul revine firesc la o stare normală în scenarii obișnuite de deplasare.

---

## Contribuții și starea proiectului

Eye Spy este disponibil sub licența Apache-2.0 la [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Posibile direcții de extindere:

- **Adăugarea intrărilor OUI**: extinderea tabelelor OUI Flock Safety și ale camerelor pe măsură ce sunt documentate noi MAC-uri de hardware.
- **Adăugarea UUID-urilor de servicii BLE**: noile ochelari inteligenți, camere sau trackere aduc UUID-uri noi.
- **Ajustarea trackerului de persistență**: limita de 50 de intrări, pragul de 3 observări și intervalul de 5 minute sunt constante modificabile.
- **Înregistrarea datelor seriale**: formatul ieșirii seriale este conceput pentru analiză programatică. Un recorder extern poate agrega evenimentele de la mai multe unități Eye Spy.

Firmware-ul se află într-un singur fișier `main.cpp` din directorul `src/`, ceea ce îl face ușor de citit, auditat și modificat.

---

## Concluzie

Eye Spy abordează o problemă restrânsă, dar importantă: mediul fizic din jurul tău este tot mai echipat pentru supraveghere, iar majoritatea dispozitivelor emit semnături RF detectabile. **Un M5Stack Atom Lite de 15 USD cu firmware-ul Eye Spy devine un scanner ambiental continuu**, care transformă complexitatea analizei pachetelor BLE și a căutărilor OUI WiFi într-un singur LED RGB.

Modelul de scor al încrederii reflectă o ponderare realistă a amenințărilor: o cameră corporală Axon din apropierea unei operațiuni a forțelor de ordine primește +5 și aprinde imediat LED-ul roșu; un iBeacon comercial primește +2 și contribuie la conștientizarea mediului fără să declanșeze singur o alarmă falsă. Reducerea scorului și pauzele împiedică dispozitivul să reacționeze excesiv la semnale trecătoare sau persistente de nivel redus.

Pentru activități de contrasupraveghere, securitate în călătorii, detectarea AirTag sau pur și simplu pentru a afla dacă ceva din apropiere te observă, Eye Spy este un instrument practic, pasiv și open-source, care merită un loc în trusa oricărui specialist în securitate.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Cumpără detectoare Eye Spy și economisește 20%
{{< /centerbutton >}}
