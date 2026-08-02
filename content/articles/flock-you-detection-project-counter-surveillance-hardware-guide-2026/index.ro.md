---
title: "Detectarea Flock-You: Ghid de Configurare pentru Contra-Supraveghere"
date: 2026-05-24
toc: true
draft: false
description: "Ghid tehnic complet al proiectului open-source Flock-You pentru detectarea camerelor ALPR Flock Safety folosind hardware bazat pe ESP32. Include instrucțiuni de configurare, detalii despre firmware și opțiuni de achiziție."
genre: ["Hardware de Securitate", "Contra-Supraveghere", "Tehnologie pentru Confidențialitate", "Proiecte Open Source", "Dezvoltare ESP32", "Monitorizare WiFi", "Instrumente de Confidențialitate", "Drepturi Digitale", "Hacking Hardware", "Securitate Rețele"]
tags: ["Proiect Flock-You", "Detectare ALPR", "ESP32-S3", "Detectare WiFi OUI", "Hardware Contra-Supraveghere", "Detectare Flock Safety", "Securitate Open Source", "Hardware pentru Confidențialitate", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Mod Promiscuu WiFi", "Monitorizare 802.11", "Colonel Panic Tech", "STS Collective", "Dispozitive de Confidențialitate", "Detectare Supraveghere", "Scanare WiFi", "Proiect GitHub", "colonelpanichacks", "Firmware ESP32", "Ghid Configurare Hardware", "Instrumente DIY de Confidențialitate", "Monitorizare Rețea", "Bază de Date OUI", "Detectare Sonde Wildcard", "Analiză Frame-uri", "Detectare Camere ALPR", "Tehnologie de Confidențialitate", "Hardware de Detectare", "Arduino ESP32", "Platform.io", "Sisteme Integrate", "Detectare RF", "Procesare Semnale", "Inginerie de Confidențialitate", "Contra-Tehnologie", "Cercetare Securitate", "Advocacy Confidențialitate", "Hardware Open", "Apărare Confidențialitate", "Firmware de Detectare", "Detectare Mobilă", "Proiecte de Confidențialitate", "Comparație Hardware"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "O ilustrație care prezintă un dispozitiv bazat pe ESP32 în prim-plan, scanând semnale WiFi. Unde colorate reprezintă diferite intensități de semnal, pe un fundal întunecat."
coverCaption: "Soluții hardware open-source pentru detectarea camerelor de supraveghere ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Ghid Tehnic Complet pentru Construirea și Utilizarea Dispozitivelor de Detectare Flock-You**

## Introducere: Contra-Supraveghere Open Source

**Proiectul Flock-You** este o **inițiativă open-source, condusă de comunitate** pentru detectarea și cartografierea infrastructurii de supraveghere ALPR a Flock Safety. Găzduit pe GitHub la **colonelpanichacks/flock-you**, acest proiect utilizează hardware accesibil bazat pe ESP32 pentru a identifica camerele Flock prin **semnăturile lor de rețea WiFi**.

Acest ghid cuprinzător acoperă totul, de la **metodologia tehnică** din spatele detectării Flock până la **instrucțiunile pas cu pas** pentru trei platforme hardware, **instalarea firmware-ului** și **informații despre achiziție de la furnizori autorizați**. Fie că ești un avocat al confidențialității, un cercetător de securitate sau un cetățean preocupat, acest ghid te va ajuta să construiești sau să achiziționezi propriul dispozitiv de detectare.

Pentru context despre de ce contează această tehnologie și despre peisajul mai larg al supravegherii, citește articolul nostru companion: **[Supravegherea prin camere Flock Safety: Prevalență, Probleme de Confidențialitate și Strategii de Protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Vrei să vezi unde au fost deja cartografiate camerele Flock? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** este un instrument open-source care trasează 40.000+ camere Flock Safety suspectate în toată lumea folosind date WiGLE WiFi și amprentare OUI — actualizat zilnic. Sursa pe **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Înțelegerea Metodologiei de Detectare Flock-You

### Fundamentul Tehnic

Camerele Flock Safety conțin **module WiFi integrate** pentru conectivitate și gestionare la distanță. Aceste module transmit semnături de rețea identificabile detectabile de dispozitive care operează în **modul de monitorizare WiFi promiscuu**. Proiectul Flock-You exploatează această caracteristică prin:

#### 1. Detectarea WiFi OUI (Identificator Unic Organizațional)

Fiecare interfață de rețea are o **adresă MAC** compusă din:
- **Primii 3 octeți (24 de biți)**: OUI, care identifică producătorul
- **Ultimii 3 octeți**: Identificator specific dispozitivului

Cercetătorii **@NitekryDPaul** și comunitatea **DeFlockJoplin** au descoperit **31 de OUI-uri specifice** prezente în mod consistent în implementările camerelor Flock Safety:

```
OUI-uri principale Espressif (module bazate pe ESP32):
D4:AD:FC - Espressif Inc. (ESP32-S3 comun)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (variante ESP32-S3)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (bazat pe ESP32)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (bazat pe ESP32)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

OUI-uri suplimentare identificate în implementările Flock:
[... 21 OUI-uri suplimentare ale producătorilor ...]
```

Când un dispozitiv de detectare scanează traficul WiFi în modul promiscuu, **identifică orice dispozitiv care transmite frame-uri cu aceste OUI-uri**.

#### 2. Detectarea Solicitărilor Probe Wildcard

Camerele Flock trimit periodic **solicitări probe wildcard** în căutarea rețelelor disponibile. Acestea au caracteristici distinctive:

- **Frame de management 802.11**: Tip=0, Subtip=4
- **Element informațional SSID**: Lungime=0 (gol/wildcard)
- **Structura frame-ului**: Model previzibil în temporizarea sondelor
- **IE-uri specifice producătorului**: Indicatori suplimentari în payload-ul frame-ului

Firmware-ul de detectare analizează aceste **modele de solicitare probe** pentru a crește încrederea în identificarea camerei Flock dincolo de simpla potrivire OUI.

#### 3. Monitorizarea WiFi în Modul Promiscuu

Operarea standard WiFi primește doar frame-uri adresate dispozitivului tău. **Modul promiscuu** captează toate frame-urile WiFi din rază:

- **Structura frame-ului 802.11**: Analizarea câmpurilor addr1, addr2, addr3
- **Frame-uri de management**: Solicitări probe, frame-uri beacon, solicitări de asociere
- **Frame-uri de date**: Dezvăluie modelele de comportament ale rețelei
- **Frame-uri de control**: ACK-uri, RTS-uri, CTS-uri oferă informații de temporizare

Microcontrolerele ESP32 suportă modul promiscuu prin **esp_wifi API**, permițând hardware de detectare la cost redus.

#### 4. Analiza Intensității Semnalului

Dispozitivele de detectare măsoară **RSSI (Indicatorul de Intensitate al Semnalului Recepționat)** pentru a:
- **Estima distanța** față de camerele detectate
- **Triangula locațiile** cu mai multe măsurători
- **Filtra rezultatele fals pozitive** pe baza caracteristicilor așteptate ale semnalului
- **Crea hărți termice** ale densității camerelor

### Acuratețea Detectării și Rezultatele Fals Pozitive

Metodologia Flock-You atinge o precizie ridicată:

- **Rata de Adevărat Pozitiv**: ~95% pentru camerele Flock confirmate în rază
- **Rata de Fals Pozitiv**: ~5-10% în funcție de mediu
- **Raza de Detectare**: 15-90 de metri în funcție de obstacole și antenă
- **Scorare a Încrederii**: Analiza multi-factor reduce alarmele false

**Surse Comune de Fals Pozitiv**:
- **Plăci de dezvoltare ESP32** utilizate în alte dispozitive IoT
- **Produse comerciale bazate pe ESP32** (casă inteligentă, senzori)
- **Alte camere de supraveghere** care folosesc componente similare
- **Echipamente de testare WiFi** operate de tehnicieni

**Strategii de Atenuare**:
- **Detectare multi-semnătură**: Combinarea OUI + model probe + verificare fizică
- **Corelarea locației**: Referire încrucișată cu locații cunoscute ale camerelor
- **Confirmarea vizuală**: Inspecție fizică după detectarea electronică
- **Baza de date comunitară**: Validare crowdsourced a detectărilor

______

## Compararea Platformelor Hardware

Trei platforme principale sunt disponibile pentru detectarea Flock-You, fiecare cu avantaje distincte:

### Tabel de Prezentare Generală a Platformelor

| Caracteristică | DIY ESP32 | M5 Atom Lite (Pre-Flashat) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Producător** | DIY / Mai mulți furnizori | STS Collective | Colonel Panic Tech |
| **Preț** | $5-12 | $39.99 | $85 |
| **Procesor** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Gata de Utilizare** | Nu (construcție DIY) | Da (pre-flashat) | Da (multi-mod) |
| **Afișaj** | Opțional | LED RGB (matrice 5×5) | Niciunul |
| **Baterie** | Opțional | Externă recomandată | Neinclus |
| **GPS** | Opțional | Nu | Nu |
| **Alerte** | Buzzer + LED | LED RGB (albastru=detectare) | Buzzer integrat |
| **Înregistrare Date** | Opțional | Nu | Nu |
| **Carcasă** | Imprimare 3D sau niciunul | Modul plastic compact | Niciunul (PCB gol) |
| **Firmware** | Flashare manuală | FlockYou pre-încărcat | Multi-mod (4 firmware-uri) |
| **Cel mai bun pentru** | Entuziaști DIY, învățare | Buget gata de utilizare | Detectare multi-scop |
| **Dificultate de Configurare** | Moderat-Avansat | Plug-and-play | Plug-and-play |
| **Greutate** | 20-50g (variază) | 18g (gol) | ~40g |
| **Dimensiuni** | Variabil | 24×24×14mm | Placă PCB |

### Analiza Detaliată a Platformelor

#### 1. Construcție DIY ESP32 ($5-12)

**Prezentare generală**: Cea mai accesibilă opțiune folosind plăci de dezvoltare standard ESP32 cu firmware open-source.

**Specificații Hardware**:
- **Microcontroler**: ESP32-WROOM-32 sau similar (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, capabil de mod promiscuu
- **Memorie**: 520KB SRAM, 4MB+ Flash
- **Afișaj**: Opțional (LED-ul de pe placă este suficient)
- **Alimentare**: Alimentat prin USB sau baterie externă
- **Buzzer**: Modul buzzer pasiv opțional (KY-006)
- **Indicatoare**: LED de pe placă + buzzer opțional
- **Extensibilitate**: Compatibil breadboard, modificări ușoare

**Firmware**: Fork open-source la **simeononsecurity/flock-you-esp32**:
- Modificat pentru hardware standard ESP32 (GPIO 25, 2, 17)
- Melodie de pornire din Super Mario Bros. (confirmă funcționarea buzzerului)
- Două bip-uri ascendente rapide la detectare nouă
- Bip-uri heartbeat la fiecare 10 secunde când urmărirea este activă
- Suport dashboard Flask pentru wardriving GPS
- Export în formate JSON, CSV, KML

**Opțiuni de Construcție**:
- **Numai LED ($5)**: ESP32 gol + cablu USB, feedback vizual doar
- **Breadboard ($9-11)**: Adaugă buzzer pasiv + breadboard + jumpere, alerte audio
- **Inclus în carcasă ($10-12)**: Adaugă carcasă imprimată 3D cu capac cu prindere

**Avantaje**:
- ✅ Cea mai ieftină opțiune (economii de 85-95% față de OUI-SPY)
- ✅ Complet open-source și modificabil
- ✅ Folosește plăci ESP32 disponibile pe scară largă
- ✅ Educativ, predă sisteme integrate
- ✅ Documentație și ghiduri extinse
- ✅ Fișiere de carcasă imprimabilă 3D disponibile
- ✅ **Aceeași precizie de detectare ca dispozitivele premium**

**Dezavantaje**:
- ❌ Necesită asamblare DIY (breadboard fără lipire sau carcasă 3D)
- ❌ Necesită flasharea manuală a firmware-ului
- ❌ Nicio baterie integrată (alimentare USB sau pachet extern)
- ❌ Feedback audio de bază numai (fără afișaj)
- ❌ Necesită timp pentru procurarea componentelor

**Cel mai bun pentru**: Makers, studenți, avocați ai confidențialității cu buget limitat, oricine dorește să înțeleagă cum funcționează detectarea, cei care se bucură de proiecte DIY.

**Achiziționare Componente**:
- **Amazon**: Caută "ESP32 DevKit" sau "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Reduceri disponibile pentru cumpărare în vrac
- **Adafruit**: Piese de calitate alese cu tutoriale

**Resurse de Configurare**:
- **Repo GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Ghid de Construcție**: Asamblare fără lipire în 10-15 minute
- **Fișiere Carcasă**: Design parametric OpenSCAD + fișiere STL

---

#### 2. M5 Atom Lite Pre-Flashat de STS Collective ($39.99)

**Prezentare generală**: Dispozitiv de detectare compact pre-flashat, gata de utilizare imediat din cutie.

**Specificații Hardware**:
- **Microcontroler**: ESP32-PICO-D4 (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, capabil de mod promiscuu
- **Memorie**: 520KB SRAM, 4MB Flash
- **Afișaj**: Matrice LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentare**: 5V prin USB-C sau conector Grove
- **Baterie**: Neinclus (se recomandă baterie externă USB)
- **Indicator**: LED RGB programabil (albastru=detectare)
- **Butoane**: 1 buton programabil
- **I/O**: Conector Grove pentru expansiune
- **Dimensiune**: Ultra-compact 24×24×14mm
- **Carcasă**: Modul plastic durabil

**Firmware**: Port FlockYou personalizat de STS Collective (proprietar):
- Pre-încărcat și gata de utilizare
- Alertă LED albastru la detectarea camerei Flock
- Bazat pe cercetarea FlockYou a colonelpanichacks
- Nu necesită configurare sau flashare
- Operare simplă plug-and-play
- Suport opțional pentru dashboard

**Avantaje**:
- ✅ Pre-flashat, nu necesită configurare tehnică
- ✅ Soluție accesibilă gata de utilizare
- ✅ Extrem de compact și portabil
- ✅ Platformă hardware dovedită
- ✅ LED albastru simplu = detectare
- ✅ Alimentat prin USB-C (mașină, baterie externă, laptop)
- ✅ Suport calificat de la furnizor
- ✅ Preț normal $99.99, la reducere $39.99

**Dezavantaje**:
- ❌ Nicio baterie integrată (necesită alimentare USB)
- ❌ Afișaj limitat (numai LED RGB, fără ecran)
- ❌ *Firmware-ul este proprietar, deocamdată nu este open-source*
- ❌ Nicio înregistrare de date fără conexiune la computer
- ❌ Un singur buton limitează funcționalitatea

**Cel mai bun pentru**: Utilizatori care doresc detectare instantanee fără muncă DIY, prioritate portabilitate, cei mulțumiți cu feedback simplu prin LED, cumpărători conștienți de buget care doresc o soluție gata făcută.

**Achiziție**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Reducere Exclusivă**: Economisești până la 20% pe produsele STS Collective — folosește codul **SIMEONONSECURITY** la finalizarea comenzii sau [apasă aici pentru a cumpăra cu reducerea aplicată](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY de Colonel Panic Tech ($85)

**Prezentare generală**: Placă de detectare a supravegherii multi-mod cu patru moduri diferite de firmware selectabile prin meniu WiFi.

**Specificații Hardware**:
- **Microcontroler**: ESP32-S3 dual-core Xtensa LX7, 8MB flash
- **WiFi**: 802.11 b/g/n, capabil de mod promiscuu
- **Memorie**: 8MB Flash
- **Afișaj**: Niciunul (PCB gol cu indicatoare LED)
- **Baterie**: Neinclus
- **Încărcare**: Alimentare și programare USB-C
- **Stocare**: Niciunul (moduri numai detectare)
- **Indicatoare**: Buzzer PWM integrat cu melodii specifice modului
- **Butoane**: Buton Boot pentru comutarea modurilor
- **Antenă**: **Comutabilă**, ceramică 2.4GHz de pe placă SAU externă prin conector MMCX
- **Carcasă**: Niciunul (PCB gol cu artă PCB)
- **Caracteristică Unică**: Randomizare MAC la fiecare pornire

**Firmware**: OUI-SPY Unified Blue cu **4 moduri selectabile**:
1. **Modul Detector**: Scanner BLE multi-țintă cu filtrare OUI + portal de configurare web
2. **Modul Foxhunter**: Tracker de proximitate RSSI cu o singură țintă pentru radiogoniometrie
3. **Modul Flock-You**: Detectarea camerelor Flock Safety & Raven cu wardriving GPS, export JSON/CSV/KML
4. **Modul Sky Spy**: Detector de RemoteID pentru drone (OpenDroneID / ASTM F3411) cu urmărire multi-dronă

**Selectarea Modului**:
- Meniu de pornire WiFi la 192.168.4.1
- Ține butonul BOOT apăsat 2 secunde pentru a reveni la selector
- Memoria ultimului mod peste ciclurile de alimentare
- Melodii de pornire per mod (alerte chiptune retro)
- Operare numai detectare (nimic transmis)

**Avantaje**:
- ✅ Patru moduri firmware într-un singur dispozitiv
- ✅ Antenă comutabilă (de pe placă sau MMCX extern)
- ✅ Buzzer integrat cu melodii de pornire personalizate
- ✅ Design PCB de calitate profesională
- ✅ Multi-scop: ALPR, drone, BLE, radiogoniometrie RF
- ✅ Suport pentru antena externă pentru rază extinsă
- ✅ De la creatorul original al proiectului Flock-You
- ✅ Dezvoltare activă și actualizări

**Dezavantaje**:
- ❌ Cel mai mare preț pentru detectarea Flock cu un singur scop
- ❌ Nicio carcasă inclusă (PCB gol)
- ❌ Nicio baterie integrată
- ❌ Niciun afișaj (feedback numai audio pentru majoritatea modurilor)
- ❌ *Complexitate inutilă pentru detectarea de bază*
- ❌ GPS extern necesar pentru funcțiile de wardriving

**Cel mai bun pentru**: Detectare supraveghere multi-scop, utilizatori care doresc detectare drone + ALPR + BLE într-un singur dispozitiv, aplicații de radiogoniometrie RF, cei care apreciază antene comutabile și caracteristici avansate.

**Achiziție**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)


______

## Instrucțiuni de Configurare Pas cu Pas

### Ghid de Configurare 1: Construcție DIY ESP32

**Pentru instrucțiuni detaliate complete**, vizitați repository-ul GitHub: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Prezentare Generală Rapid Start

1. **Hardware Necesar**:
   - Placă ESP32 DevKit ($5-6)
   - Cablu USB (Micro-USB sau USB-C în funcție de placă)
   - Opțional: Modul buzzer pasiv (KY-006), breadboard, jumpere
   - Opțional: Carcasă imprimată 3D

2. **Configurare Software**:
   ```bash
   # Instalează PlatformIO
   pip install platformio
   
   # Clonează repository-ul
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Flashează firmware-ul
   pio run -t upload
   pio device monitor
   ```

3. **Asamblare Hardware** (dacă se folosește buzzer):
   - Pozitiv buzzer → GPIO 25
   - Negativ buzzer → GND
   - Indicator LED → GPIO 2 (pe placă)
   - Alimentare prin USB

4. **Confirmare Pornire**:
   - Melodia 1-2 din Super Mario Bros. se redă (dacă este conectat buzzerul)
   - LED-ul clipește pentru a indica scanarea
   - Monitorul serial afișează inițializarea "Flock-You ESP32"

5. **Alerte de Detectare**:
   - **Detectare nouă**: Două bip-uri ascendente rapide (2000→2800 Hz)
   - **Heartbeat**: Două bip-uri la fiecare 10 secunde în timp ce urmărirea este activă
   - **LED**: Clipește la fiecare detectare

6. **Wardriving GPS** (opțional):
   - Conectează la computer prin USB
   - Rulează dashboardul Flask: `cd api && python flockyou.py`
   - Deschide http://localhost:5000
   - Conectează dispozitivul GPS sau folosește locația browserului
   - Exportă detectările în JSON/CSV/KML

**Ghid complet de construcție, fișiere de carcasă și depanare**: Vezi README-ul GitHub

---

### Ghid de Configurare 2: M5 Atom Lite Pre-Flashat (STS Collective)

#### Rapid Start

1. **Despachetare**:
   - Dispozitiv M5 Atom Lite (pre-flashat cu firmware FlockYou)
   - Verificați listarea produsului pentru includerea cablului USB-C

2. **Pornire**:
   - Conectați la sursa de alimentare USB-C (baterie externă, USB mașină, adaptor de perete, computer)
   - Dispozitivul pornește automat
   - Matricea LED RGB se inițializează

3. **Operare**:
   - **Inactiv/Scanare**: LED-ul afișează modelul de scanare
   - **Detectare**: LED-ul devine **ALBASTRU** când este detectată camera Flock
   - **Buton**: Apasă pentru a rescana manual sau reseta

4. **Utilizare Portabilă**:
   - Conectați la baterie externă USB (5000mAh = ~20 ore)
   - Plasați în suportul de pahare, geantă sau buzunar
   - LED-ul vizibil prin carcasa translucidă

5. **Conexiune Dashboard** (opțional):
   - Conectați dispozitivul la computer prin USB-C
   - Instalați dashboardul FlockYou conform instrucțiunilor STS Collective
   - Vizualizați detectările live în interfața browserului

**Avertisment**: *Acesta este firmware proprietar. Reflasharea cu versiuni open-source va șterge permanent firmware-ul STS.*

---

### Ghid de Configurare 3: Placa Multi-Mod OUI-SPY

#### Configurare Inițială

1. **Conținut Pachet**:
   - Placa PCB goală OUI-SPY
   - Cablu USB-C
   - Ghid de pornire rapidă

2. **Prima Pornire**:
   - Conectați alimentare USB-C (computer, adaptor de perete sau baterie externă)
   - Dispozitivul transmite rețeaua WiFi: `OUISPY-[ID]`
   - Buzzerul redă melodia de pornire specifică modului

3. **Selectarea Modului WiFi**:
   - Conectați telefonul/computerul la rețeaua WiFi OUI-SPY
   - Deschideți browserul la: `http://192.168.4.1`
   - Interfața web afișează 4 moduri firmware:
     1. **Detector** - Scanner BLE multi-țintă
     2. **Foxhunter** - Radiogoniometrie RF
     3. **Flock-You** - Detectare camere ALPR
     4. **Sky Spy** - Detector RemoteID drone
   - Selectați modul dorit și faceți clic pe "Activate"

4. **Operare în Modul Flock-You**:
   - Dispozitivul repornește în modul Flock-You
   - Buzzerul redă melodia de pornire Flock-You
   - Începe scanarea pentru 31 OUI-uri cunoscute
   - **Alertă detectare**: Buzzerul emite cu model unic
   - Ultimul mod reținut peste ciclurile de alimentare

5. **Comutarea Modurilor**:
   - Ține butonul **BOOT** apăsat 2 secunde
   - Dispozitivul revine la selectorul de mod WiFi
   - Reconectați la WiFi și alegeți noul mod

#### Avansat: Antenă Externă

6. **Comutare Antenă** (pentru rază extinsă):
   - Implicit: Folosește antena ceramică de pe placă
   - Conectați antena MMCX la conectorul MMCX
   - Firmware-ul comută automat la antena externă
   - Utilizați antena direcțională/Yagi pentru detectare pe distanță lungă

#### Montare

7. **Instalare în Vehicul/Fixă**:
   - *Nicio carcasă inclusă, PCB-ul gol necesită protecție înainte de montare*
   - Opțiuni:
     - Imprimați 3D o carcasă personalizată
     - Montare cu Velcro pe bord
     - Folosiți bandă dublă față
     - Cutie DIY de proiect
   - Mențineți portul USB-C accesibil pentru alimentare

#### Export Date (Modul Flock-You)

8. **Wardriving GPS**:
   - Conectați modulul GPS extern (neinclus)
   - Dispozitivul înregistrează detectările cu coordonate
   - Descărcați fișierele de date prin interfața web
   - Formate de export: JSON, CSV, KML

**Notă**: Verificați colonelpanic.tech pentru actualizările firmware și documentația specifică OUI-SPY Unified Blue.

---



______

## Ghid de Achiziție și Informații despre Furnizori

### Furnizori Autorizați

#### Colonel Panic Tech (colonelpanic.tech)

**Produse Oferite**:
- **OUI-SPY** ($85): Dispozitiv de detectare Flock gata de utilizare
- **Kituri DIY** ($55): Componente + PCB + ghid de asamblare
- **Add-on Modul GPS** ($18): Modul GPS-6M compatibil
- **Accesorii**: Antene, carcase, actualizări baterie

**De ce să cumperi de la Colonel Panic**:
- ✅ Direct de la dezvoltatorul hardware-ului OUI-SPY
- ✅ Cel mai recent firmware pre-instalat
- ✅ Suport tehnic inclus
- ✅ Ethos open-source (scheme disponibile)
- ✅ Forum comunitar activ

**Livrare**:
- SUA Intern: 3-5 zile lucrătoare
- Internațional: 7-14 zile lucrătoare
- Livrare gratuită la comenzi >$100

**Garanție**: Garanție hardware 90 de zile, actualizări firmware pe viață

**Website**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Produse Oferite**:
- **M5 Atom Lite Pre-Flashat** ($39.99): Dispozitiv de detectare Flock gata de utilizare
- **Accesorii**: Compatible cu diverse platforme ESP32

**De ce să cumperi de la STS Collective**:
- ✅ Dispozitive pre-flashate gata de utilizare
- ✅ Asigurarea calității și testare
- ✅ Prețuri accesibile
- ✅ Suport pentru clienți

**Livrare**:
- SUA Intern: 2-4 zile lucrătoare (Priority Mail)
- Internațional: 7-21 zile lucrătoare
- Opțiuni express disponibile

**Garanție**: Garanție standard pe hardware

**Website**: [https://stscollective.com](https://stscollective.com)

> 💰 **Reducere pentru Cititori**: Folosiți codul **SIMEONONSECURITY** pentru până la 20% reducere la produsele STS Collective — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Alte Surse pentru M5 Atom Lite

**Magazinul Oficial M5Stack**:
- Website: [shop.m5stack.com](https://shop.m5stack.com)
- Preț: $9.95 pentru Atom Lite gol
- Accesorii: Module baterie, senzori Grove, carcase
- Livrare: Internațional, 7-14 zile

**Amazon**: Caută "M5Stack Atom Lite"
- Preț: ~$12-15 (variază în funcție de vânzător)
- Livrare Prime disponibilă
- Opțiuni bundle cu accesorii

**Adafruit**: [adafruit.com](https://adafruit.com)
- Retailer de electronică selecționat
- Resurse de învățare excelente
- Livrare rapidă din SUA

**Notă**: *La achiziționarea unui M5 Atom Lite gol, firmware-ul trebuie instalat separat urmând ghidul DIY de mai sus. Versiunea STS Collective pre-flashat este un produs diferit.*

### Rezumat Comparație Prețuri

| Dispozitiv | Preț de Bază | Add-on-uri Opționale | Investiție Totală | Timp de Configurare |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | Carcasă 3D, baterie | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39.99 | Baterie externă $10 | $40-50 | Plug-and-play |
| **OUI-SPY** | $85 | Antenă externă $20, carcasă | $85-115 | Plug-and-play |

______

## Utilizarea Dispozitivului de Detectare: Scenarii Practice

### Scenariul 1: Cartografierea Navetei Zilnice

**Obiectiv**: Documentarea locațiilor camerelor Flock de-a lungul rutelor obișnuite.

**Configurare**:
- Folosiți dispozitiv cu capacitate GPS (DIY ESP32 cu modul GPS sau OUI-SPY cu GPS)
- Activați înregistrarea automată
- Montați în vehicul sau purtați în buzunar
- Setați sensibilitatea la MEDIU pentru a reduce falsele pozitive

**Procedură**:
1. Porniți dispozitivul de detectare înainte de plecare
2. Conduceți pe ruta obișnuită
3. Dispozitivul alertează când sunt detectate camerele Flock
4. Coordonatele GPS sunt înregistrate automat
5. Reveniți acasă și exportați datele
6. Importați GPX/CSV în software de cartografiere
7. Creați o hartă personală a locațiilor camerelor

**Beneficii**:
- Conștientizarea acoperirii de supraveghere pe rutele tale
- Identificarea rutelor alternative fără camere
- Contribuția la proiectele de cartografiere comunitară
- Urmărirea schimbărilor de implementare în timp

### Scenariul 2: Evaluarea Supravegherii din Cartier

**Obiectiv**: Determinarea acoperirii camerelor Flock în zona rezidențială.

**Configurare**:
- Folosiți dispozitiv portabil (M5 Atom Lite, DIY ESP32 sau OUI-SPY)
- Sondaj pe jos sau cu bicicleta
- Monitorizare staționară la intersecții cheie

**Procedură**:
1. Mergeți pe jos/cu bicicleta prin străzile cartierului
2. Opriți la fiecare intersecție timp de 30-60 de secunde
3. Notați detectările pe hartă
4. Folosiți intensitatea semnalului pentru a estima distanța/direcția
5. Confirmați vizual locațiile camerelor când este posibil
6. Documentați descoperirile cu fotografii (din zone publice)

**Rezultat**:
- Hartă completă a infrastructurii locale de supraveghere
- Dovezi pentru organizare comunitară
- Date pentru solicitări de documente publice
- Conștientizare pentru decizii personale de confidențialitate

### Scenariul 3: Evaluarea Confidențialității în Călătorii

**Obiectiv**: Înțelegerea expunerii la supraveghere în timpul călătoriilor.

**Configurare**:
- Luați dispozitiv compact (M5 Atom Lite în buzunar sau DIY ESP32)
- Activați înregistrarea continuă
- Analizați datele după excursie

**Cazuri de Utilizare**:
- Programări medicale: Evaluați supravegherea în apropierea clinicilor
- Consultații juridice: Verificați acoperirea zonei din apropierea biroului avocatului
- Servicii religioase: Înțelegeți monitorizarea în apropierea locașurilor de cult
- Activități politice: Evaluați supravegherea la evenimente/proteste
- Situații domestice: Identificați dacă reședința este monitorizată

### Scenariul 4: Advocacy Comunitar

**Obiectiv**: Furnizarea de date pentru dezbateri de politici și conștientizare publică.

**Aplicații**:
- Prezentați descoperirile la ședințele consiliului municipal
- Includeți în solicitările de documente publice
- Împărtășiți cu organizații de advocacy pentru confidențialitate
- Contribuiți la proiecte de cercetare
- Informați asociațiile de cartier

**Prezentarea Datelor**:
- Creați hărți termice care arată densitatea camerelor
- Generați rapoarte privind disparitățile de acoperire
- Produceți cronologii ale expansiunii implementării
- Corelați cu statistici criminalistice (sau lipsa acestora)

______

## Analiză Tehnică Detaliată: Înțelegerea Codului

### Algoritmul Principal de Detectare (Simplificat)

Pentru cei interesați de implementarea tehnică, iată o vedere simplificată a logicii de detectare:

```cpp
// Flock-You Detection Core (Conceptual - not full code)

// OUI Database (31 known Flock-associated OUIs)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Espressif ESP32-S3 variant
    // ... 28 more OUIs ...
};

// Promiscuous mode callback
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;
    
    // Extract MAC address from frame
    uint8_t *mac = pkt->payload + 10; // addr2 field position
    
    // Check against OUI database
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI match found
            int rssi = pkt->rx_ctrl.rssi;
            
            // Check signal strength threshold
            if (rssi > RSSI_THRESHOLD) {
                // Analyze frame for additional signatures
                if (is_wildcard_probe_request(pkt)) {
                    // High confidence detection
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // OUI match only
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard probe detection
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Management frame, subtype probe request
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;
    
    // Check for empty SSID IE (wildcard)
    // Position depends on frame structure
    uint8_t *ie = &pkt->payload[24]; // Start of IEs
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard probe
    }
    return false;
}
```

### Concepte Tehnice Cheie Explicate

**Modul Promiscuu**: În loc să primească numai frame-urile adresate dispozitivului tău, ESP32 captează toate frame-urile WiFi din rază. **Acest lucru este esențial pentru detectarea dispozitivelor din apropiere care nu comunică cu detectorul tău.**

**Structura Adresei MAC**: Fiecare frame WiFi conține mai multe adrese MAC:
- `addr1`: Adresa receptorului
- `addr2`: Adresa transmițătorului (conține OUI)
- `addr3`: Adresa destinației finale/sursei

**RSSI (Indicatorul de Intensitate al Semnalului Recepționat)**: Intensitatea semnalului în dBm (decibeli negativi față de 1 miliwatt). Valori tipice:
- -30 dBm: Extrem de puternic (foarte aproape)
- -50 dBm: Semnal puternic
- -70 dBm: Slab dar utilizabil
- -90 dBm: Foarte slab (la limita razei)

**Solicitări Probe**: Dispozitivele WiFi trimit solicitări probe pentru a descoperi rețelele disponibile. *Probele wildcard (SSID gol) caută orice rețea, ceea ce este comun în dispozitivele IoT precum camerele Flock, făcându-le detectabile în mod fiabil.*

______

## Depanarea Problemelor Comune

### Problema: Nicio Detectare Deși Camera Este Cunoscută în Apropiere

**Cauze Posibile**:
1. **Camera offline/oprită**: Camerele Flock sunt temporar inactive uneori
2. **Semnal blocat**: Materialele de construcție absorb WiFi (metal, beton)
3. **În afara razei**: Raza efectivă ~30-90 de metri în funcție de obstacole
4. **Problemă de firmware**: Firmware-ul depășit ratează variantele OUI mai noi

**Soluții**:
- Confirmați că camera este vizibilă și pare funcțională (panouri solare, lumini)
- Apropiați-vă de locația suspectată a camerei
- Încercați orientări diferite ale antenei
- Actualizați la cel mai recent firmware Flock-You
- **Verificați că dispozitivul scanează activ** (verificați activitatea LED/afișaj)

### Problema: Falsuri Pozitive Excesive

**Cauze Posibile**:
1. **Densitate ridicată de dispozitive ESP32**: Dispozitivele casă inteligentă, IoT sunt comune
2. **Sensibilitate prea ridicată**: Detectarea dispozitivelor îndepărtate/irelevante
3. **Alte camere de supraveghere**: Multe folosesc module ESP32

**Soluții**:
- Reduceți setarea de sensibilitate
- Activați detectarea sondei wildcard (mai multă încredere)
- Verificați fizic detectările înainte de înregistrare
- Folosiți intensitatea semnalului pentru filtrare (alertați numai la semnale puternice)
- Actualizați baza de date OUI pentru a vă concentra pe OUI-urile Flock confirmate

### Problema: Bateria se Descarcă Rapid

**Cauze Posibile**:
1. **Scanare continuă**: Nicio gestionare sleep/alimentare
2. **Afișaj mereu pornit**: Ecranul consumă putere semnificativă
3. **GPS activ**: Modulele GPS sunt mari consumatoare de energie
4. **Baterie veche**: Bateriile Li-Po se degradează în timp

**Soluții**:
- Activați modul de scanare pasivă (intermitentă față de continuă)
- Setați timeout-ul afișajului
- Dezactivați GPS-ul când cartografierea nu este necesară
- Înlocuiți bateria (OUI-SPY/mesh-detect v2 au baterii înlocuibile)
- Folosiți baterie externă pentru sesiuni extinse

### Problema: GPS Nu Obține Blocare

**Cauze Posibile**:
1. **Utilizare în interior**: GPS-ul necesită vizibilitate la cer
2. **Antena neconectată**: mesh-detect v2 necesită conectarea antenei externe
3. **Pornire la rece**: Prima blocare GPS durează 5-15 minute
4. **Interferențe**: Electronicele din apropiere interferează cu semnalul

**Soluții**:
- Mutați la o poziție cu vedere liberă la cer
- Asigurați că antena este conectată corect (conector SMA)
- Așteptați blocarea inițială (blocările ulterioare sunt mai rapide)
- Îndepărtați-vă de sursele de interferență RF
- Verificați că GPS-ul este activat în setări

### Problema: Datele Nu Se Înregistrează pe Cardul SD

**Cauze Posibile**:
1. **Card SD neformatat**: Trebuie să fie în format FAT32
2. **Card SD plin**: Nu mai rămâne spațiu
3. **Card nedetectat**: Nu este introdus complet
4. **Corupție sistem de fișiere**: Card deteriorat

**Soluții**:
- **Formatați cardul SD ca FAT32** (maximum 32GB pentru compatibilitate)
- Ștergeți jurnalele vechi sau folosiți un card mai mare
- Reintroduceți complet cardul (ar trebui să facă click)
- Reformatați cardul sau înlocuiți-l dacă este deteriorat
- Verificați că dispozitivul recunoaște cardul (meniul va afișa starea SD)

______

## Considerații Legale și Etice

### Statutul Legal al Dispozitivelor de Detectare

**Legalitatea Scanării WiFi**:
- ✅ **Legal în SUA**: Monitorizarea pasivă WiFi (numai recepție) este legală
- ✅ **Nicio interceptare**: Dispozitivele monitorizează numai frame-urile difuzate public
- ✅ **Nicio decriptare**: Nu se încearcă decriptarea datelor sau conectarea la rețele
- ✅ **Similar cu scanerele radio**: Statut legal comparabil cu scanerele de poliție

**Distincții Importante**:
- ❌ **Ilegal**: Bruiajul activ/interferența cu funcționarea camerei
- ❌ **Ilegal**: Tentativa de a hackui sau accesa sistemele camerei
- ❌ **Ilegal**: Distrugerea sau alterarea fizică a camerelor
- ⚠️ **Zonă gri**: *Unele jurisdicții au legi mai stricte privind confidențialitatea. Verificați reglementările locale înainte de utilizare.*

**Recomandare**: **Dispozitivele de detectare sunt doar pentru conștientizare. Nu interferați cu funcționarea camerei.**

### Ghid de Utilizare Etică

**Utilizare Responsabilă**:
- ✅ Folosiți pentru conștientizarea personală a supravegherii
- ✅ Documentați pentru advocacy și discuții de politici
- ✅ Împărtășiți date agregate cu organizații de confidențialitate
- ✅ Contribuiți la proiectele de cartografiere comunitară
- ✅ Educați-i pe alții despre infrastructura de supraveghere

**Evitați**:
- ❌ Folosirea datelor pentru a facilita activități ilegale
- ❌ Hărțuirea proprietarilor de proprietăți care au instalat camere
- ❌ Intruziunea pentru confirmarea locațiilor camerelor
- ❌ Acțiuni de tip vigilant împotriva infrastructurii de supraveghere

### Considerații de Confidențialitate

**Confidențialitatea Datelor Tale**:
- **Dispozitivele de detectare înregistrează LOCAȚIA TA** (prin GPS)
- Stocați aceste date în siguranță
- **Fiți conștienți de riscul de citație** dacă sunteți implicați în proceduri legale
- Luați în considerare criptarea pentru fișierele de jurnal sensibile
- Înțelegeți politicile de confidențialitate ale furnizorilor pentru dispozitivele conectate la cloud

**Respectarea Celorlalți**:
- Fiți atenți când folosiți dispozitivele de detectare în spații private
- Nu le folosiți pentru a urmări alți indivizi
- Luați în considerare implicațiile etice ale partajării datelor

______

## Comunitate și Dezvoltare Open Source

### Contribuția la Proiectul Flock-You

Proiectul Flock-You prosperă prin contribuțiile comunității:

**Repository GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Modalități de Contribuție**:
1. **Descoperire OUI Nouă**: Trimiteți OUI-uri nou identificate ale camerelor Flock
2. **Îmbunătățiri de Cod**: Trimiteți pull request-uri pentru îmbunătățiri de firmware
3. **Proiecte Hardware**: Distribuiți proiecte personalizate de dispozitive de detectare
4. **Documentație**: Îmbunătățiți ghidurile de configurare, traducerile
5. **Testare**: Raportați erori, verificați funcționalitatea pe dispozitive
6. **Cartografiere**: Contribuiți la bazele de date crowdsourced de locații ale camerelor

### Resurse Comunitare

**Forumuri și Discuții**:
- **Reddit**: r/privacy, r/privacytoolsIO, discuții active
- **Discord**: Serverul Colonel Panic Tech, chat în timp real
- **GitHub Issues**: Suport tehnic și solicitări de funcționalități

**Lucrări de Cercetare**:
- Studii academice despre supravegherea ALPR
- Evaluări ale impactului asupra confidențialității
- Analize juridice ale legalității dispozitivelor de detectare

**Organizații de Advocacy**:
- **Electronic Frontier Foundation** (EFF): Urmărire ALPR
- **ACLU**: Supraveghere și drepturi de confidențialitate
- **Grupuri locale**: DeFlockJoplin și inițiative comunitare similare

### Foaia de Parcurs pentru Dezvoltare Viitoare

**Funcționalități Planificate** (din GitHub-ul proiectului):
- **Învățare automată**: Recunoașterea modelelor pentru precizie mai mare
- **Sincronizare cloud**: Bază de date opțională de detectare crowdsourced
- **Aplicații mobile**: Integrare smartphone pentru interfețe îmbunătățite
- **Moduri de detectare suplimentare**: Alte tehnologii de supraveghere
- **Alerte în timp real**: Notificări push prin celulare/WiFi

______

## Concluzie: Ajutând Confidențialitatea Prin Tehnologie

**Proiectul de detectare Flock-You** reprezintă o democratizare puternică a tehnologiei de contra-supraveghere. Pentru mai puțin decât costul unui abonament lunar de streaming, indivizii obțin conștientizare cu privire la infrastructura de supraveghere din jurul lor. Fie că alegeți **construcția DIY ESP32 ($5-12)**, **M5 Atom Lite gata de utilizare ($40)** sau **OUI-SPY multi-mod ($85)**, investiți în conștientizarea confidențialității și autonomia digitală.

### Puncte Principale

✅ **Autonomizare open-source**: Dezvoltarea condusă de comunitate asigură accesibilitatea
✅ **Tehnologie accesibilă**: Hardware-ul de consum (ESP32) face detectarea accesibilă
✅ **Platforme multiple**: Opțiuni pentru diferite bugete și niveluri de competență tehnică
✅ **Dezvoltare activă**: Actualizări regulate cu noi semnături OUI și funcționalități
✅ **Legal și etic**: Monitorizarea pasivă respectă legile comunicațiilor
✅ **Beneficiu comunitar**: Contribuie la conștientizarea publică și discuțiile de politici

### Pașii Următori

1. **Aflați mai multe** despre de ce contează detectarea: [Supravegherea prin camere Flock Safety: Prevalență și Probleme de Confidențialitate](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Alegeți platforma**: Decideți ce dispozitiv se potrivește nevoilor și bugetului vostru
3. **Comandați hardware**: Achiziționați de la furnizori autorizați
4. **Configurați și configurați**: Urmați ghidurile detaliate din acest articol
5. **Alăturați-vă comunității**: Angajați-vă cu alți utilizatori, împărtășiți descoperiri, contribuiți cu îmbunătățiri
6. **Acționați**: Folosiți datele pentru advocacy, conștientizare și decizii informate

Proliferarea supravegherii ALPR reprezintă o schimbare semnificativă în dinamica confidențialității. Tehnologiile de contra-supraveghere precum Flock-You oferă o capacitate crucială: **conștientizare**. Când înțelegem domeniul și scala supravegherii, luăm decizii informate cu privire la mișcările noastre, advocacy-ul nostru și așteptările noastre de confidențialitate în spațiile publice.

**Tehnologia a permis supravegherea pervasivă. Tehnologia îi ajută și pe cei care valorizează confidențialitatea.** Proiectul Flock-You este un testament al puterii colaborării open-source în protejarea libertăților civile.

______

## Articole Conexe

| Articol | Descriere |
|---------|-------------|
| **[Supravegherea prin camere Flock Safety: Prevalență, Probleme de Confidențialitate și Strategii de Protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Ghidul definitiv pentru rețeaua ALPR a Flock Safety, abuzuri documentate, resurse de organizare comunitară și ce puteți face pentru a vă proteja |
| **[Flock Finder: Cartografiați Fiecare Cameră Flock Safety Suspectată din Apropierea Dvs.](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Cum să folosiți instrumentul open-source Flock Finder pentru a vizualiza 40.000+ camere Flock suspectate în toată lumea folosind date WiGLE și amprentare OUI |
| **[Cum să Flashezi Rayhunter pe Dispozitive de Detectare IMSI Catcher](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Ghid pas cu pas pentru flasharea firmware-ului Rayhunter pentru detectarea IMSI catcher-elor și stingray-urilor — completează detectarea ALPR |
| **[Firmware Personalizat DagShell pentru Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Ghid complet pentru instalarea DagShell pe Orbic RCL400 pentru monitorizarea avansată a rețelei celulare și detectarea IMSI catcher |
| **[Compararea Dispozitivelor Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparație side-by-side a dispozitivelor suportate de Rayhunter pentru a vă ajuta să alegeți hardware-ul potrivit pentru setul de instrumente de contra-supraveghere |

______

## Referințe

1. [Repository GitHub Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Hartă Interactivă Camere ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - Repository GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Furnizor Oficial](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Pre-Flashat](https://stscollective.com)
4. [Documentație Oficială M5Stack](https://docs.m5stack.com/en/core/atom_lite)
5. [Documentație Tehnică Espressif ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
6. [Tutorial Mod Promiscuu WiFi](https://esp32developer.com/wifi-promiscuous-mode)
7. [Cercetare Comunitate DeFlockJoplin](https://deflockjoplin.org/)
8. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
9. [Descărcare Oficială Arduino IDE](https://www.arduino.cc/en/software)
10. [Documentație Platform.io](https://docs.platformio.org/)
11. [Baza de Date OUI - Standarde IEEE](https://standards.ieee.org/products-programs/regauth/)
12. [Referință Structură Frame 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
