---
title: "Flock-You Detection: Guida alla Configurazione del Contro-Sorveglianza"
date: 2026-05-24
toc: true
draft: false
description: "Guida tecnica completa al progetto open-source Flock-You per il rilevamento delle telecamere ALPR di Flock Safety tramite hardware basato su ESP32. Include istruzioni di configurazione, dettagli firmware e opzioni di acquisto."
genre: ["Hardware di Sicurezza", "Contro Sorveglianza", "Tecnologia per la Privacy", "Progetti Open Source", "Sviluppo ESP32", "Monitoraggio WiFi", "Strumenti per la Privacy", "Diritti Digitali", "Hardware Hacking", "Sicurezza di Rete"]
tags: ["Flock-You Project", "ALPR Detection", "ESP32-S3", "WiFi OUI Detection", "Counter Surveillance Hardware", "Flock Safety Detection", "Open Source Security", "Privacy Hardware", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "Promiscuous Mode WiFi", "802.11 Monitoring", "Colonel Panic Tech", "STS Collective", "Privacy Devices", "Surveillance Detection", "WiFi Scanning", "GitHub Project", "colonelpanichacks", "ESP32 Firmware", "Hardware Setup Guide", "DIY Privacy Tools", "Network Monitoring", "OUI Database", "Wildcard Probe Detection", "Frame Analysis", "ALPR Camera Detection", "Privacy Technology", "Detection Hardware", "Arduino ESP32", "Platform.io", "Embedded Systems", "RF Detection", "Signal Processing", "Privacy Engineering", "Counter Technology", "Security Research", "Privacy Advocacy", "Open Hardware", "Privacy Defense", "Detection Firmware", "Mobile Detection", "Privacy Projects", "Hardware Comparison"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Un'illustrazione che mostra un dispositivo basato su ESP32 in primo piano che scansiona segnali WiFi. Onde colorate rappresentano diverse intensità di segnale su uno sfondo scuro."
coverCaption: "Soluzioni hardware open-source per il rilevamento delle telecamere di sorveglianza ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guida Tecnica Completa per Costruire e Utilizzare Dispositivi di Rilevamento Flock-You**

## Introduzione: Contro-Sorveglianza Open Source

Il **progetto Flock-You** è un'**iniziativa open-source guidata dalla comunità** per rilevare e mappare l'infrastruttura di sorveglianza ALPR di Flock Safety. Ospitato su GitHub all'indirizzo **colonelpanichacks/flock-you**, questo progetto utilizza hardware economico basato su ESP32 per identificare le telecamere Flock attraverso le loro **firme di rete WiFi**.

Questa guida completa copre tutto, dalla **metodologia tecnica** dietro il rilevamento Flock alle **istruzioni di configurazione passo dopo passo** per tre piattaforme hardware, **installazione del firmware** e **informazioni sull'acquisto da rivenditori autorizzati**. Che tu sia un sostenitore della privacy, un ricercatore di sicurezza o un cittadino preoccupato, questa guida ti consentirà di costruire o acquistare il tuo dispositivo di rilevamento.

Per il contesto su perché questa tecnologia è importante e il panorama più ampio della sorveglianza, leggi il nostro articolo correlato: **[Sorveglianza con Telecamere Flock Safety: Prevalenza, Preoccupazioni per la Privacy e Strategie di Protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Vuoi vedere dove le telecamere Flock sono già state mappate? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** è uno strumento open-source che traccia oltre 40.000 telecamere Flock Safety sospette in tutto il mondo utilizzando i dati WiFi WiGLE e il fingerprinting OUI — aggiornato quotidianamente. Sorgente su **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Comprensione della Metodologia di Rilevamento Flock-You

### La Base Tecnica

Le telecamere Flock Safety contengono **moduli WiFi integrati** per la connettività e la gestione remota. Questi moduli trasmettono firme di rete identificabili rilevabili dai dispositivi che operano in **modalità di monitoraggio WiFi promiscuo**. Il progetto Flock-You sfrutta questa caratteristica attraverso:

#### 1. Rilevamento WiFi OUI (Identificatore Univoco Organizzativo)

Ogni interfaccia di rete ha un **indirizzo MAC** composto da:
- **Primi 3 byte (24 bit)**: OUI, che identifica il produttore
- **Ultimi 3 byte**: Identificatore specifico del dispositivo

I ricercatori **@NitekryDPaul** e la comunità **DeFlockJoplin** hanno scoperto **31 OUI specifici** costantemente presenti nelle distribuzioni di telecamere Flock Safety:

```
Primary Espressif OUIs (ESP32-based modules):
D4:AD:FC - Espressif Inc. (Common ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3 variants)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (ESP32-based)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (ESP32-based)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Additional OUIs identified in Flock deployments:
[... 21 additional manufacturer OUIs ...]
```

Quando un dispositivo di rilevamento scansiona il traffico WiFi in modalità promiscua, **identifica qualsiasi dispositivo che trasmette frame con questi OUI**.

#### 2. Rilevamento Probe Request Wildcard

Le telecamere Flock inviano periodicamente **probe request wildcard** alla ricerca di reti disponibili. Queste hanno caratteristiche distintive:

- **Frame di Gestione 802.11**: Type=0, Subtype=4
- **Elemento Informativo SSID**: Length=0 (vuoto/wildcard)
- **Struttura del frame**: Schema prevedibile nei tempi della probe
- **IE specifici del fornitore**: Indicatori aggiuntivi nel payload del frame

Il firmware di rilevamento analizza questi **schemi di probe request** per aumentare la fiducia nell'identificazione delle telecamere Flock al di là del semplice abbinamento OUI.

#### 3. Monitoraggio WiFi in Modalità Promiscua

Il funzionamento WiFi standard riceve solo i frame indirizzati al tuo dispositivo. La **modalità promiscua** cattura tutti i frame WiFi nel raggio d'azione:

- **Struttura frame 802.11**: Analisi dei campi addr1, addr2, addr3
- **Frame di gestione**: Probe request, beacon frame, richieste di associazione
- **Frame dati**: Rivelano schemi di comportamento della rete
- **Frame di controllo**: ACK, RTS, CTS forniscono informazioni sui tempi

I microcontrollori ESP32 supportano la modalità promiscua attraverso l'**esp_wifi API**, abilitando hardware di rilevamento a basso costo.

#### 4. Analisi della Forza del Segnale

I dispositivi di rilevamento misurano l'**RSSI (Indicatore della Forza del Segnale Ricevuto)** per:
- **Stimare la distanza** dalle telecamere rilevate
- **Triangolare le posizioni** con misurazioni multiple
- **Filtrare i falsi positivi** in base alle caratteristiche di segnale attese
- **Creare mappe di calore** della densità delle telecamere

### Precisione del Rilevamento e Falsi Positivi

La metodologia Flock-You raggiunge un'elevata precisione:

- **Tasso di Veri Positivi**: ~95% per le telecamere Flock confermate nel raggio d'azione
- **Tasso di Falsi Positivi**: ~5-10% a seconda dell'ambiente
- **Raggio di Rilevamento**: 15-90 metri a seconda degli ostacoli e dell'antenna
- **Punteggio di Fiducia**: L'analisi multifattoriale riduce i falsi allarmi

**Fonti Comuni di Falsi Positivi**:
- **Schede di sviluppo ESP32** utilizzate in altri dispositivi IoT
- **Prodotti commerciali basati su ESP32** (smart home, sensori)
- **Altre telecamere di sorveglianza** che utilizzano componenti simili
- **Apparecchiature di test WiFi** utilizzate dai tecnici

**Strategie di Mitigazione**:
- **Rilevamento multi-firma**: Combinazione di OUI + schema probe + verifica fisica
- **Correlazione della posizione**: Riferimento incrociato con posizioni di telecamere note
- **Conferma visiva**: Ispezione fisica dopo il rilevamento elettronico
- **Database della comunità**: Validazione crowdsourced dei rilevamenti

______

## Confronto delle Piattaforme Hardware

Sono disponibili tre piattaforme principali per il rilevamento Flock-You, ciascuna con vantaggi distinti:

### Tabella Panoramica delle Piattaforme

| Caratteristica | DIY ESP32 | M5 Atom Lite (Pre-Flashato) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Produttore** | DIY / Più fornitori | STS Collective | Colonel Panic Tech |
| **Prezzo** | $5-12 | $39,99 | $85 |
| **Processore** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Pronto all'Uso** | No (build DIY) | Sì (pre-flashato) | Sì (multi-modo) |
| **Display** | Opzionale | LED RGB (matrice 5×5) | Nessuno |
| **Batteria** | Opzionale | Esterna consigliata | Nessuna inclusa |
| **GPS** | Opzionale | No | No |
| **Avvisi** | Buzzer + LED | LED RGB (blu=rilevamento) | Buzzer integrato |
| **Registrazione Dati** | Opzionale | No | No |
| **Custodia** | Stampa 3D o nessuna | Modulo plastico compatto | Nessuna (PCB nudo) |
| **Firmware** | Flash manuale | FlockYou precaricato | Multi-modo (4 firmware) |
| **Ideale Per** | Appassionati DIY, apprendimento | Soluzione economica pronta | Rilevamento multiuso |
| **Difficoltà di Configurazione** | Medio-Avanzato | Plug-and-play | Plug-and-play |
| **Peso** | 20-50g (variabile) | 18g (nudo) | ~40g |
| **Dimensioni** | Variabile | 24×24×14mm | Scheda PCB |

### Analisi Dettagliata delle Piattaforme

#### 1. Build DIY ESP32 ($5-12)

**Panoramica**: L'opzione più economica che utilizza schede di sviluppo ESP32 standard con firmware open-source.

**Specifiche Hardware**:
- **Microcontrollore**: ESP32-WROOM-32 o simile (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, modalità promiscua abilitata
- **Memoria**: 520KB SRAM, 4MB+ Flash
- **Display**: Opzionale (LED integrato sufficiente)
- **Alimentazione**: USB o pacco batterie
- **Buzzer**: Modulo buzzer passivo opzionale (KY-006)
- **Indicatori**: LED integrato + buzzer opzionale
- **Espandibilità**: Compatibile con breadboard, facili modifiche

**Firmware**: Fork open-source su **simeononsecurity/flock-you-esp32**:
- Modificato per hardware ESP32 standard (GPIO 25, 2, 17)
- Melodia di avvio di Super Mario Bros. (conferma funzionamento buzzer)
- Due bip crescenti rapidi al nuovo rilevamento
- Bip heartbeat ogni 10 secondi durante il tracciamento attivo
- Supporto dashboard Flask per wardriving GPS
- Esportazione in formato JSON, CSV, KML

**Opzioni di Build**:
- **Solo LED ($5)**: ESP32 nudo + cavo USB, solo feedback visivo
- **Breadboard ($9-11)**: Aggiungi buzzer passivo + breadboard + jumper, avvisi audio
- **Con Custodia ($10-12)**: Aggiungi custodia stampata in 3D con coperchio a scatto

**Vantaggi**:
- ✅ Opzione più economica (risparmio del 85-95% rispetto a OUI-SPY)
- ✅ Completamente open-source e modificabile
- ✅ Utilizza schede ESP32 ampiamente disponibili
- ✅ Educativo, insegna i sistemi embedded
- ✅ Documentazione e guide estese
- ✅ File custodia stampabili in 3D disponibili
- ✅ **Stessa precisione di rilevamento dei dispositivi premium**

**Svantaggi**:
- ❌ Richiede assemblaggio DIY (breadboard senza saldatura o custodia 3D)
- ❌ Flash manuale del firmware necessario
- ❌ Nessuna batteria integrata (alimentazione USB o pacco esterno)
- ❌ Solo feedback audio di base (nessun display)
- ❌ Richiede tempo per reperire i componenti

**Ideale Per**: Maker, studenti, sostenitori della privacy con budget limitato, chiunque voglia imparare come funziona il rilevamento, chi ama i progetti DIY.

**Acquista Componenti**:
- **Amazon**: Cerca "ESP32 DevKit" o "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Sconti all'ingrosso disponibili
- **Adafruit**: Parti di qualità selezionate con tutorial

**Risorse di Configurazione**:
- **Repository GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Guida alla Build**: Assemblaggio senza saldatura in 10-15 minuti
- **File Custodia**: Design parametrico OpenSCAD + file STL

---

#### 2. M5 Atom Lite Pre-Flashato da STS Collective ($39,99)

**Panoramica**: Dispositivo di rilevamento compatto pre-flashato, pronto all'uso fuori dalla scatola.

**Specifiche Hardware**:
- **Microcontrollore**: ESP32-PICO-D4 (dual-core, 240MHz)
- **WiFi**: 802.11 b/g/n, modalità promiscua abilitata
- **Memoria**: 520KB SRAM, 4MB Flash
- **Display**: Matrice LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentazione**: 5V tramite USB-C o connettore Grove
- **Batteria**: Nessuna inclusa (banco di alimentazione USB esterno consigliato)
- **Indicatore**: LED RGB programmabile (blu=rilevamento)
- **Pulsanti**: 1 pulsante programmabile
- **I/O**: Connettore Grove per espansione
- **Dimensioni**: Ultra-compatto 24×24×14mm
- **Custodia**: Modulo plastico resistente

**Firmware**: Port FlockYou personalizzato da STS Collective (proprietario):
- Precaricato e pronto all'uso
- Avviso LED blu al rilevamento di telecamere Flock
- Basato sulla ricerca FlockYou di colonelpanichacks
- Nessuna configurazione o flash richiesta
- Operazione semplice plug-and-play
- Supporto dashboard opzionale

**Vantaggi**:
- ✅ Pre-flashato, nessuna configurazione tecnica richiesta
- ✅ Soluzione economica pronta all'uso
- ✅ Estremamente compatto e portatile
- ✅ Piattaforma hardware collaudata
- ✅ Semplice LED blu = rilevamento
- ✅ Alimentato da USB-C (auto, power bank, laptop)
- ✅ Supporto qualità del fornitore
- ✅ Prezzo regolare $99,99, in saldo $39,99

**Svantaggi**:
- ❌ Nessuna batteria integrata (richiede alimentazione USB)
- ❌ Display limitato (solo LED RGB, nessuno schermo)
- ❌ *Il firmware è proprietario, non open-source per il momento*
- ❌ Nessuna registrazione dati senza connessione al computer
- ❌ Il singolo pulsante limita le funzionalità

**Ideale Per**: Utenti che vogliono rilevamento immediato senza lavoro DIY, priorità alla portabilità, chi è a proprio agio con il semplice feedback LED, acquirenti attenti al budget che vogliono una soluzione già pronta.

**Acquisto**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Sconto Esclusivo**: Risparmia fino al 20% sui prodotti STS Collective — usa il codice **SIMEONONSECURITY** al momento del checkout o [clicca qui per fare acquisti con lo sconto applicato](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY di Colonel Panic Tech ($85)

**Panoramica**: Scheda di rilevamento sorveglianza multi-modo con quattro diverse modalità firmware selezionabili tramite menu WiFi.

**Specifiche Hardware**:
- **Microcontrollore**: ESP32-S3 dual-core Xtensa LX7, 8MB flash
- **WiFi**: 802.11 b/g/n, modalità promiscua abilitata
- **Memoria**: 8MB Flash
- **Display**: Nessuno (PCB nudo con indicatori LED)
- **Batteria**: Nessuna inclusa
- **Ricarica**: USB-C alimentazione e programmazione
- **Storage**: Nessuno (modalità solo rilevamento)
- **Indicatori**: Buzzer PWM integrato con melodie specifiche per modalità
- **Pulsanti**: Pulsante Boot per cambio modalità
- **Antenna**: **Commutabile**, ceramica 2,4GHz integrata OPPURE esterna tramite connettore MMCX
- **Custodia**: Nessuna (PCB nudo con grafica PCB)
- **Caratteristica Unica**: Randomizzazione MAC ad ogni avvio

**Firmware**: OUI-SPY Unified Blue con **4 modalità selezionabili**:
1. **Modalità Detector**: Scanner BLE multi-target con filtro OUI + portale di configurazione web
2. **Modalità Foxhunter**: Tracker di prossimità RSSI a singolo target per il radiogoniometro
3. **Modalità Flock-You**: Rilevamento telecamere Flock Safety e Raven con wardriving GPS, esportazione JSON/CSV/KML
4. **Modalità Sky Spy**: Rilevatore RemoteID droni (OpenDroneID / ASTM F3411) con tracciamento multi-drone

**Selezione Modalità**:
- Menu di avvio WiFi a 192.168.4.1
- Tieni premuto il pulsante BOOT per 2 secondi per tornare al selettore
- Memoria ultima modalità tra i cicli di alimentazione
- Melodie di avvio per modalità (avvisi chiptune retro)
- Operazione solo rilevamento (nulla trasmesso)

**Vantaggi**:
- ✅ Quattro modalità firmware in un unico dispositivo
- ✅ Antenna commutabile (integrata o MMCX esterno)
- ✅ Buzzer integrato con melodie di avvio personalizzate
- ✅ Design PCB di livello professionale
- ✅ Multiuso: ALPR, droni, BLE, radiogoniometro
- ✅ Supporto antenna esterna per portata estesa
- ✅ Dal creatore originale del progetto Flock-You
- ✅ Sviluppo attivo e aggiornamenti

**Svantaggi**:
- ❌ Prezzo più alto per il rilevamento Flock a scopo singolo
- ❌ Nessuna custodia inclusa (PCB nudo)
- ❌ Nessuna batteria integrata
- ❌ Nessun display (solo feedback audio per la maggior parte delle modalità)
- ❌ *Complessità non necessaria per il rilevamento di base*
- ❌ GPS esterno richiesto per le funzioni di wardriving

**Ideale Per**: Rilevamento sorveglianza multiuso, utenti che desiderano rilevamento droni + ALPR + BLE in un unico dispositivo, applicazioni di radiogoniometro, chi valorizza le antenne commutabili e le funzionalità avanzate.

**Acquisto**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)


______

## Istruzioni di Configurazione Passo dopo Passo

### Guida alla Configurazione 1: Build DIY ESP32

**Per istruzioni complete e dettagliate**, visita il repository GitHub: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Panoramica Avvio Rapido

1. **Hardware Necessario**:
   - Scheda ESP32 DevKit ($5-6)
   - Cavo USB (Micro-USB o USB-C a seconda della scheda)
   - Opzionale: Modulo buzzer passivo (KY-006), breadboard, jumper
   - Opzionale: Custodia stampata in 3D

2. **Configurazione Software**:
   ```bash
   # Install PlatformIO
   pip install platformio
   
   # Clone repository
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Flash firmware
   pio run -t upload
   pio device monitor
   ```

3. **Assemblaggio Hardware** (se si utilizza il buzzer):
   - Buzzer positivo → GPIO 25
   - Buzzer negativo → GND
   - Indicatore LED → GPIO 2 (integrato)
   - Alimentazione tramite USB

4. **Conferma Avvio**:
   - Suona la melodia di Super Mario Bros. 1-2 (se il buzzer è collegato)
   - Il LED lampeggia per indicare la scansione
   - Il monitor seriale mostra l'inizializzazione "Flock-You ESP32"

5. **Avvisi di Rilevamento**:
   - **Nuovo rilevamento**: Due bip ascendenti rapidi (2000→2800 Hz)
   - **Heartbeat**: Due bip ogni 10 secondi durante il tracciamento
   - **LED**: Lampeggia ad ogni rilevamento

6. **Wardriving GPS** (opzionale):
   - Collega al computer tramite USB
   - Esegui dashboard Flask: `cd api && python flockyou.py`
   - Apri http://localhost:5000
   - Collega dispositivo GPS o usa la posizione del browser
   - Esporta rilevamenti in JSON/CSV/KML

**Guida completa alla build, file custodia e risoluzione dei problemi**: Consulta il README di GitHub

---

### Guida alla Configurazione 2: M5 Atom Lite Pre-Flashato (STS Collective)

#### Avvio Rapido

1. **Unboxing**:
   - Dispositivo M5 Atom Lite (pre-flashato con firmware FlockYou)
   - Controlla l'elenco del prodotto per l'inclusione del cavo USB-C

2. **Accensione**:
   - Collega a una fonte di alimentazione USB-C (power bank, USB auto, adattatore da parete, computer)
   - Il dispositivo si avvia automaticamente
   - La matrice LED RGB si inizializza

3. **Funzionamento**:
   - **Inattivo/Scansione**: Il LED visualizza lo schema di scansione
   - **Rilevamento**: Il LED diventa **BLU** quando viene rilevata una telecamera Flock
   - **Pulsante**: Premi per eseguire nuovamente la scansione o resettare manualmente

4. **Uso Portatile**:
   - Collega a un power bank USB (5000mAh = ~20 ore)
   - Posiziona nel portabicchieri, nella borsa o in tasca
   - LED visibile attraverso la custodia traslucida

5. **Connessione Dashboard** (opzionale):
   - Collega il dispositivo al computer tramite USB-C
   - Installa il dashboard FlockYou secondo le istruzioni STS Collective
   - Visualizza i rilevamenti in tempo reale nell'interfaccia del browser

**Avvertenza**: *Questo è firmware proprietario. Il re-flash con versioni open-source eliminerà definitivamente il firmware STS.*

---

### Guida alla Configurazione 3: Scheda Multi-Modo OUI-SPY

#### Configurazione Iniziale

1. **Contenuto della Confezione**:
   - Scheda PCB nuda OUI-SPY
   - Cavo USB-C
   - Guida rapida

2. **Prima Accensione**:
   - Collega alimentazione USB-C (computer, adattatore da parete o power bank)
   - Il dispositivo trasmette la rete WiFi: `OUISPY-[ID]`
   - Il buzzer suona la melodia di avvio specifica per la modalità

3. **Selezione Modalità WiFi**:
   - Collega telefono/computer alla rete WiFi OUI-SPY
   - Apri il browser a: `http://192.168.4.1`
   - L'interfaccia web mostra 4 modalità firmware:
     1. **Detector** - Scanner BLE multi-target
     2. **Foxhunter** - Radiogoniometro  
     3. **Flock-You** - Rilevamento telecamere ALPR
     4. **Sky Spy** - Rilevatore RemoteID droni
   - Seleziona la modalità desiderata e clicca "Activate"

4. **Funzionamento Modalità Flock-You**:
   - Il dispositivo si riavvia in modalità Flock-You
   - Il buzzer suona la melodia di avvio Flock-You
   - Inizia la scansione per 31 OUI noti
   - **Avviso di rilevamento**: Il buzzer cinguetta con schema unico
   - L'ultima modalità viene ricordata tra i cicli di alimentazione

5. **Cambio Modalità**:
   - Tieni premuto il pulsante **BOOT** per 2 secondi
   - Il dispositivo torna al selettore modalità WiFi
   - Riconnetti al WiFi e scegli la nuova modalità

#### Avanzato: Antenna Esterna

6. **Commutazione Antenna** (per portata estesa):
   - Per impostazione predefinita: Utilizza l'antenna ceramica integrata
   - Collega l'antenna MMCX al connettore MMCX
   - Il firmware passa automaticamente all'antenna esterna
   - Usa un'antenna direzionale/Yagi per il rilevamento a lungo raggio

#### Montaggio

7. **Installazione su Veicolo/Fissa**:
   - *Nessuna custodia inclusa, il PCB nudo necessita di protezione prima del montaggio*
   - Opzioni:
     - Stampa 3D custodia personalizzata
     - Montaggio con velcro sul cruscotto
     - Usa nastro biadesivo
     - Box progetto DIY
   - Mantieni la porta USB-C accessibile per l'alimentazione

#### Esportazione Dati (Modalità Flock-You)

8. **Wardriving GPS**:
   - Collega modulo GPS esterno (non incluso)
   - Il dispositivo registra i rilevamenti con le coordinate
   - Scarica i file dati tramite l'interfaccia web
   - Formati di esportazione: JSON, CSV, KML

**Nota**: Consulta colonelpanic.tech per aggiornamenti firmware e documentazione specifici per OUI-SPY Unified Blue.

---



______

## Guida all'Acquisto e Informazioni sui Rivenditori

### Rivenditori Autorizzati

#### Colonel Panic Tech (colonelpanic.tech)

**Prodotti Offerti**:
- **OUI-SPY** ($85): Dispositivo di rilevamento Flock pronto all'uso
- **Kit DIY** ($55): Componenti + PCB + guida all'assemblaggio
- **Add-on Modulo GPS** ($18): Modulo GPS-6M compatibile
- **Accessori**: Antenne, custodie, upgrade batterie

**Perché Acquistare da Colonel Panic**:
- ✅ Direttamente dallo sviluppatore dell'hardware OUI-SPY
- ✅ Firmware più recente preinstallato
- ✅ Supporto tecnico incluso
- ✅ Etica open-source (schemi disponibili)
- ✅ Forum della comunità attivo

**Spedizione**:
- Domestica USA: 3-5 giorni lavorativi
- Internazionale: 7-14 giorni lavorativi
- Spedizione gratuita per ordini >$100

**Garanzia**: Garanzia hardware 90 giorni, aggiornamenti firmware a vita

**Sito Web**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Prodotti Offerti**:
- **M5 Atom Lite Pre-Flashato** ($39,99): Dispositivo di rilevamento Flock pronto all'uso
- **Accessori**: Compatibili con varie piattaforme ESP32

**Perché Acquistare da STS Collective**:
- ✅ Dispositivi pre-flashati pronti all'uso
- ✅ Garanzia di qualità e test
- ✅ Prezzi accessibili
- ✅ Assistenza clienti

**Spedizione**:
- Domestica USA: 2-4 giorni lavorativi (Priority Mail)
- Internazionale: 7-21 giorni lavorativi
- Opzioni espresse disponibili

**Garanzia**: Garanzia standard sull'hardware

**Sito Web**: [https://stscollective.com](https://stscollective.com)

> 💰 **Sconto Lettori**: Usa il codice **SIMEONONSECURITY** per fino al 20% di sconto sui prodotti STS Collective — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Altre Fonti per M5 Atom Lite

**Store Ufficiale M5Stack**:
- Sito Web: [shop.m5stack.com](https://shop.m5stack.com)
- Prezzo: $9,95 per Atom Lite nudo
- Accessori: Moduli batteria, sensori Grove, custodie
- Spedizione: Internazionale, 7-14 giorni

**Amazon**: Cerca "M5Stack Atom Lite"
- Prezzo: ~$12-15 (varia per venditore)
- Spedizione Prime disponibile
- Opzioni bundle con accessori

**Adafruit**: [adafruit.com](https://adafruit.com)
- Rivenditore di elettronica selezionata
- Ottime risorse di apprendimento
- Spedizione rapida basata negli USA

**Nota**: *Quando si acquista un M5 Atom Lite nudo, il firmware deve essere installato separatamente seguendo la guida DIY sopra. La versione pre-flashata STS Collective è un prodotto diverso.*

### Riepilogo Confronto Prezzi

| Dispositivo | Prezzo Base | Add-on Opzionali | Investimento Totale | Tempo di Configurazione |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | Custodia 3D, batteria | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39,99 | Power bank $10 | $40-50 | Plug-and-play |
| **OUI-SPY** | $85 | Antenna esterna $20, custodia | $85-115 | Plug-and-play |

______

## Utilizzo del Dispositivo di Rilevamento: Scenari Pratici

### Scenario 1: Mappatura del Tragitto Quotidiano

**Obiettivo**: Documentare le posizioni delle telecamere Flock lungo i tuoi percorsi abituali.

**Configurazione**:
- Usa un dispositivo con capacità GPS (DIY ESP32 con modulo GPS o OUI-SPY con GPS)
- Abilita la registrazione automatica
- Monta nel veicolo o porta in tasca
- Imposta la sensibilità su MEDIO per ridurre i falsi positivi

**Procedura**:
1. Avvia il dispositivo di rilevamento prima di partire
2. Percorri il tuo itinerario normale
3. Il dispositivo avvisa quando vengono rilevate telecamere Flock
4. Le coordinate GPS vengono registrate automaticamente
5. Torna a casa ed esporta i dati
6. Importa GPX/CSV nel software di mappatura
7. Crea una mappa personale delle posizioni delle telecamere

**Vantaggi**:
- Consapevolezza della copertura di sorveglianza sui tuoi percorsi
- Identifica percorsi alternativi privi di telecamere
- Contribuisci ai progetti di mappatura della comunità
- Traccia i cambiamenti di distribuzione nel tempo

### Scenario 2: Valutazione della Sorveglianza del Quartiere

**Obiettivo**: Determinare la copertura delle telecamere Flock nella tua zona residenziale.

**Configurazione**:
- Usa un dispositivo portatile (M5 Atom Lite, DIY ESP32 o OUI-SPY)
- Rilevamento a piedi o in bicicletta
- Monitoraggio stazionario agli incroci principali

**Procedura**:
1. Percorri le strade del quartiere a piedi/bicicletta
2. Fermati ad ogni incrocio per 30-60 secondi
3. Annota i rilevamenti sulla mappa
4. Usa l'intensità del segnale per stimare distanza/direzione
5. Conferma visivamente le posizioni delle telecamere quando possibile
6. Documenta i risultati con foto (dalle aree pubbliche)

**Risultato**:
- Mappa completa dell'infrastruttura di sorveglianza locale
- Prove per l'organizzazione della comunità
- Dati per le richieste di documenti pubblici
- Consapevolezza per le decisioni personali sulla privacy

### Scenario 3: Valutazione della Privacy durante i Viaggi

**Obiettivo**: Comprendere l'esposizione alla sorveglianza durante gli spostamenti.

**Configurazione**:
- Porta un dispositivo compatto (M5 Atom Lite in tasca o DIY ESP32)
- Abilita la registrazione continua
- Rivedi i dati dopo il viaggio

**Casi d'Uso**:
- Appuntamenti medici: Valuta la sorveglianza vicino alle cliniche
- Consulenze legali: Controlla la copertura dell'area dell'ufficio dell'avvocato
- Servizi religiosi: Comprendi il monitoraggio vicino ai luoghi di culto
- Attività politiche: Valuta la sorveglianza agli eventi/proteste
- Situazioni domestiche: Identifica se la residenza è monitorata

### Scenario 4: Advocacy della Comunità

**Obiettivo**: Fornire dati per i dibattiti politici e la sensibilizzazione pubblica.

**Applicazioni**:
- Presenta i risultati alle riunioni del consiglio comunale
- Includi nelle richieste di documenti pubblici
- Condividi con organizzazioni per la difesa della privacy
- Contribuisci ai progetti di ricerca
- Informa le associazioni di quartiere

**Presentazione dei Dati**:
- Crea mappe di calore che mostrano la densità delle telecamere
- Genera rapporti sulle disparità di copertura
- Produci cronologie dell'espansione della distribuzione
- Correla con le statistiche sulla criminalità (o la loro assenza)

______

## Analisi Tecnica Dettagliata: Comprensione del Codice

### Algoritmo di Rilevamento Principale (Semplificato)

Per chi è interessato all'implementazione tecnica, ecco una visione semplificata della logica di rilevamento:

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

### Concetti Tecnici Chiave Spiegati

**Modalità Promiscua**: Invece di ricevere solo i frame indirizzati al tuo dispositivo, ESP32 cattura tutti i frame WiFi nel raggio d'azione. **Questo è essenziale per rilevare i dispositivi vicini che non comunicano con il tuo rilevatore.**

**Struttura Indirizzo MAC**: Ogni frame WiFi contiene più indirizzi MAC:
- `addr1`: Indirizzo del ricevitore
- `addr2`: Indirizzo del trasmettitore (contiene OUI)
- `addr3`: Indirizzo della destinazione/sorgente finale

**RSSI (Indicatore della Forza del Segnale Ricevuto)**: Intensità del segnale in dBm (decibel negativi relativi a 1 milliwatt). Valori tipici:
- -30 dBm: Estremamente forte (molto vicino)
- -50 dBm: Segnale forte
- -70 dBm: Debole ma utilizzabile
- -90 dBm: Molto debole (limite del raggio)

**Probe Request**: I dispositivi WiFi inviano probe request per scoprire le reti disponibili. *Le probe wildcard (SSID vuoto) cercano qualsiasi rete, il che è comune nei dispositivi IoT come le telecamere Flock, rendendole rilevabili in modo affidabile.*

______

## Risoluzione dei Problemi Comuni

### Problema: Nessun Rilevamento Nonostante una Telecamera Nota nelle Vicinanze

**Possibili Cause**:
1. **Telecamera offline/spenta**: Le telecamere Flock sono temporaneamente inattive a volte
2. **Segnale bloccato**: I materiali da costruzione assorbono il WiFi (metallo, cemento)
3. **Fuori portata**: Portata effettiva ~30-90 metri a seconda degli ostacoli
4. **Problema firmware**: Il firmware obsoleto manca delle varianti OUI più recenti

**Soluzioni**:
- Conferma che la telecamera sia visibile e sembri operativa (pannelli solari, luci)
- Avvicinati alla posizione sospetta della telecamera
- Prova orientamenti dell'antenna diversi
- Aggiorna all'ultimo firmware Flock-You
- **Verifica che il dispositivo stia eseguendo la scansione attivamente** (verifica attività LED/display)

### Problema: Troppi Falsi Positivi

**Possibili Cause**:
1. **Alta densità di dispositivi ESP32**: Smart home, dispositivi IoT sono comuni
2. **Sensibilità troppo alta**: Rilevamento di dispositivi distanti/irrilevanti
3. **Altre telecamere di sorveglianza**: Molte usano moduli ESP32

**Soluzioni**:
- Riduci l'impostazione di sensibilità
- Abilita il rilevamento probe wildcard (maggiore fiducia)
- Verifica fisicamente i rilevamenti prima di registrarli
- Usa l'intensità del segnale per filtrare (avvisa solo per segnali forti)
- Aggiorna il database OUI per concentrarti sugli OUI Flock confermati

### Problema: La Batteria si Scarica Rapidamente

**Possibili Cause**:
1. **Scansione continua**: Nessuna gestione del risparmio energetico
2. **Display sempre attivo**: Lo schermo consuma energia significativa
3. **GPS attivo**: I moduli GPS sono energivori
4. **Batteria vecchia**: Le batterie Li-Po si degradano nel tempo

**Soluzioni**:
- Abilita la modalità di scansione passiva (intermittente vs. continua)
- Imposta il timeout del display
- Disabilita il GPS quando la mappatura non è necessaria
- Sostituisci la batteria (OUI-SPY/mesh-detect v2 hanno batterie sostituibili)
- Usa un power bank esterno per sessioni prolungate

### Problema: Il GPS Non Acquisisce il Blocco

**Possibili Cause**:
1. **Uso interno**: Il GPS richiede visibilità del cielo
2. **Antenna non collegata**: mesh-detect v2 necessita dell'antenna esterna collegata
3. **Avvio a freddo**: Il primo blocco GPS richiede 5-15 minuti
4. **Interferenze**: L'elettronica vicina interferisce con il segnale

**Soluzioni**:
- Spostati in una posizione con visibilità del cielo libera
- Assicurati che l'antenna sia correttamente collegata (connettore SMA)
- Attendi il blocco iniziale (i blocchi successivi sono più veloci)
- Allontanati dalle fonti di interferenza RF
- Controlla che il GPS sia abilitato nelle impostazioni

### Problema: I Dati Non si Registrano sulla Scheda SD

**Possibili Cause**:
1. **Scheda SD non formattata**: Deve essere in formato FAT32
2. **Scheda SD piena**: Nessuno spazio rimanente
3. **Scheda non rilevata**: Non completamente inserita
4. **Corruzione del file system**: Scheda danneggiata

**Soluzioni**:
- **Formatta la scheda SD come FAT32** (massimo 32GB per compatibilità)
- Elimina i vecchi log o usa una scheda più grande
- Reinserisci completamente la scheda (dovrebbe fare clic)
- Riformatta la scheda o sostituiscila se danneggiata
- Controlla che il dispositivo riconosca la scheda (il menu mostrerà lo stato SD)

______

## Considerazioni Legali ed Etiche

### Status Legale dei Dispositivi di Rilevamento

**Legalità della Scansione WiFi**:
- ✅ **Legale negli USA**: Il monitoraggio WiFi passivo (solo ricezione) è legale
- ✅ **Nessuna intercettazione**: I dispositivi monitorano solo i frame trasmessi pubblicamente
- ✅ **Nessuna decrittazione**: Non si tenta di decrittare dati o connettersi a reti
- ✅ **Simile agli scanner radio**: Status legale comparabile agli scanner della polizia

**Distinzioni Importanti**:
- ❌ **Illegale**: Jamming/interferenza attiva con il funzionamento delle telecamere
- ❌ **Illegale**: Tentativo di hackerare o accedere ai sistemi delle telecamere
- ❌ **Illegale**: Distruzione o manomissione delle telecamere fisiche
- ⚠️ **Area grigia**: *Alcune giurisdizioni hanno leggi sulla privacy più severe. Verifica le normative locali prima dell'uso.*

**Raccomandazione**: **I dispositivi di rilevamento sono solo per la consapevolezza. Non interferire con il funzionamento delle telecamere.**

### Linee Guida per l'Uso Etico

**Uso Responsabile**:
- ✅ Usa per la consapevolezza personale della sorveglianza
- ✅ Documenta per l'advocacy e le discussioni politiche
- ✅ Condividi i dati aggregati con le organizzazioni per la privacy
- ✅ Contribuisci ai progetti di mappatura della comunità
- ✅ Educa gli altri sull'infrastruttura di sorveglianza

**Evita**:
- ❌ Usare i dati per facilitare attività illegali
- ❌ Molestare i proprietari che hanno installato telecamere
- ❌ Trespassing per confermare le posizioni delle telecamere
- ❌ Azioni di vigilantismo contro l'infrastruttura di sorveglianza

### Considerazioni sulla Privacy

**La Tua Privacy dei Dati**:
- **I dispositivi di rilevamento registrano LA TUA posizione** (tramite GPS)
- Archivia questi dati in modo sicuro
- **Sii consapevole del rischio di citazione in giudizio** se coinvolto in procedimenti legali
- Considera la crittografia per i file di log sensibili
- Comprendi le politiche sulla privacy dei vendor per i dispositivi connessi al cloud

**Rispetto degli Altri**:
- Sii cauto quando usi dispositivi di rilevamento in spazi privati
- Non usarli per tracciare altri individui
- Considera le implicazioni etiche della condivisione dei dati

______

## Comunità e Sviluppo Open Source

### Contribuire al Progetto Flock-You

Il progetto Flock-You prospera grazie ai contributi della comunità:

**Repository GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Modi per Contribuire**:
1. **Scoperta di Nuovi OUI**: Invia OUI di telecamere Flock appena identificati
2. **Miglioramenti del Codice**: Invia pull request per miglioramenti al firmware
3. **Progettazione Hardware**: Condividi progetti di dispositivi di rilevamento personalizzati
4. **Documentazione**: Migliora le guide di configurazione, traduzioni
5. **Test**: Segnala bug, verifica le funzionalità su vari dispositivi
6. **Mappatura**: Contribuisci ai database crowdsourced delle posizioni delle telecamere

### Risorse della Comunità

**Forum e Discussioni**:
- **Reddit**: r/privacy, r/privacytoolsIO, discussioni attive
- **Discord**: Server Colonel Panic Tech, chat in tempo reale
- **GitHub Issues**: Supporto tecnico e richieste di funzionalità

**Articoli di Ricerca**:
- Studi accademici sulla sorveglianza ALPR
- Valutazioni dell'impatto sulla privacy
- Analisi legali della legalità dei dispositivi di rilevamento

**Organizzazioni di Advocacy**:
- **Electronic Frontier Foundation** (EFF): Tracciamento ALPR
- **ACLU**: Sorveglianza e diritti alla privacy
- **Gruppi locali**: DeFlockJoplin e simili iniziative comunitarie

### Roadmap di Sviluppo Futuro

**Funzionalità Pianificate** (dal GitHub del progetto):
- **Machine learning**: Riconoscimento di pattern per una maggiore precisione
- **Sincronizzazione cloud**: Database di rilevamento crowdsourced opzionale
- **App mobile**: Integrazione smartphone per interfacce migliorate
- **Modalità di rilevamento aggiuntive**: Altre tecnologie di sorveglianza
- **Avvisi in tempo reale**: Notifiche push tramite cellular/WiFi

______

## Conclusione: Aiutare la Privacy attraverso la Tecnologia

Il **progetto di rilevamento Flock-You** rappresenta una potente democratizzazione della tecnologia di contro-sorveglianza. Per meno del costo di un abbonamento mensile in streaming, gli individui acquisiscono consapevolezza dell'infrastruttura di sorveglianza che li circonda. Che tu scelga la **build DIY ESP32 ($5-12)**, il **M5 Atom Lite pronto all'uso ($40)** o il **multi-modo OUI-SPY ($85)**, stai investendo nella consapevolezza della privacy e nell'autonomia digitale.

### Punti Principali

✅ **Empowerment open-source**: Lo sviluppo guidato dalla comunità garantisce l'accessibilità
✅ **Tecnologia accessibile**: L'hardware consumer (ESP32) rende il rilevamento accessibile
✅ **Piattaforme multiple**: Opzioni per diversi budget e livelli di competenza tecnica
✅ **Sviluppo attivo**: Aggiornamenti regolari con nuove firme OUI e funzionalità
✅ **Legale ed etico**: Il monitoraggio passivo è conforme alle leggi sulle comunicazioni
✅ **Beneficio comunitario**: Contribuisce alla consapevolezza pubblica e alla discussione politica

### Prossimi Passi

1. **Scopri di più** sul perché il rilevamento è importante: [Sorveglianza con Telecamere Flock Safety: Prevalenza e Preoccupazioni per la Privacy](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Scegli la tua piattaforma**: Decidi quale dispositivo si adatta alle tue esigenze e al tuo budget
3. **Ordina hardware**: Acquista da rivenditori autorizzati
4. **Configura e imposta**: Segui le guide dettagliate in questo articolo
5. **Unisciti alla comunità**: Interagisci con altri utenti, condividi i risultati, contribuisci ai miglioramenti
6. **Agisci**: Usa i tuoi dati per advocacy, consapevolezza e decisioni informate

La proliferazione della sorveglianza ALPR rappresenta un cambiamento significativo nelle dinamiche della privacy. Le tecnologie di contro-sorveglianza come Flock-You offrono una capacità cruciale: **consapevolezza**. Quando comprendiamo l'ambito e la scala della sorveglianza, prendiamo decisioni informate sui nostri movimenti, la nostra advocacy e le nostre aspettative di privacy negli spazi pubblici.

**La tecnologia ha abilitato la sorveglianza pervasiva. La tecnologia aiuta anche chi valorizza la privacy.** Il progetto Flock-You è una testimonianza del potere della collaborazione open-source nella protezione delle libertà civili.

______

## Articoli Correlati

| Articolo | Descrizione |
|---------|-------------|
| **[Sorveglianza con Telecamere Flock Safety: Prevalenza, Preoccupazioni per la Privacy e Strategie di Protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | La guida definitiva alla rete ALPR di Flock Safety, abusi documentati, risorse per l'organizzazione della comunità e cosa puoi fare per proteggerti |
| **[Flock Finder: Mappa Ogni Telecamera Flock Safety Sospetta Vicino a Te](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Come usare lo strumento open-source Flock Finder per visualizzare oltre 40.000 telecamere Flock sospette in tutto il mondo usando dati WiGLE e fingerprinting OUI |
| **[Come Flashare Rayhunter sui Dispositivi di Rilevamento IMSI Catcher](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Guida passo dopo passo per flashare il firmware Rayhunter per rilevare IMSI catcher e stingray — complementa il rilevamento ALPR |
| **[Firmware Personalizzato DagShell per Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Guida completa all'installazione di DagShell su Orbic RCL400 per il monitoraggio avanzato della rete cellulare e il rilevamento IMSI catcher |
| **[Confronto Dispositivi Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Confronto fianco a fianco dei dispositivi supportati da Rayhunter per aiutarti a scegliere l'hardware giusto per il tuo kit di contro-sorveglianza |

______

## Riferimenti

1. [Flock-You GitHub Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Interactive ALPR Camera Map](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - GitHub Repository](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Official Vendor](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Pre-Flashed](https://stscollective.com)
4. [M5Stack Official Documentation](https://docs.m5stack.com/en/core/atom_lite)
5. [Espressif ESP32 Technical Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
6. [WiFi Promiscuous Mode Tutorial](https://esp32developer.com/wifi-promiscuous-mode)
7. [DeFlockJoplin Community Research](https://deflockjoplin.org/)
8. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
9. [Arduino IDE Official Download](https://www.arduino.cc/en/software)
10. [Platform.io Documentation](https://docs.platformio.org/)
11. [OUI Database - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
12. [802.11 Frame Structure Reference](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
