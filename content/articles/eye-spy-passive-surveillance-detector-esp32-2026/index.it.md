---
title: "Eye Spy: rilevatore passivo di sorveglianza e tracker per ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Riferimento tecnico per Eye Spy v1.1, un rilevatore passivo BLE e WiFi con ESP32 per telecamere, tracker, droni e segnali correlati."
genre: ["Strumenti per la privacy", "Controsorveglianza", "Sicurezza IoT", "Sistemi embedded", "Ricerca sulla sicurezza", "Sicurezza WiFi", "Sicurezza Bluetooth", "Progetti ESP32", "Sicurezza hardware", "Sicurezza open source"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Rilevamento della sorveglianza", "Controsorveglianza", "Rilevamento BLE", "Scansione WiFi", "Rilevamento AirTag", "Rilevamento ALPR", "Flock Safety", "Rilevamento bodycam", "Rilevamento droni", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Software libero", "Riservatezza", "BLE passivo", "Modalità promiscuo", "Rilevamento OUI", "Rilevamento tracker", "Bodycam Axon", "Ray-Ban Meta", "Samsung SmartTag", "Tracker Tile", "Telecamera nascosta", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Illustrazione di un piccolo M5Stack Atom Lite circondato da onde di segnale colorate su sfondo blu navy scuro, a rappresentare il rilevamento della sorveglianza Bluetooth e WiFi."
coverCaption: ""
---

**Un sensore passivo grande quanto un pollice che avvisa quando qualcosa vi osserva**

## Introduzione: il panorama della sorveglianza che non si vede

Il mondo fisico è sempre più dotato di dispositivi che osservano, registrano e tracciano: lettori di targhe agli angoli delle strade, bodycam delle forze dell'ordine, telecamere negli alloggi in affitto, tracker commerciali simili agli AirTag nascosti in borse o auto e telecamere di sorveglianza agli ingressi dei negozi. La maggior parte di questi dispositivi comunica in modalità wireless tramite **Bluetooth LE** o **WiFi**. *La maggior parte di queste comunicazioni viene trasmessa nell'aria aperta ed è rilevabile da chiunque disponga del ricevitore adatto.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) è uno strumento passivo per il rilevamento della sorveglianza che sfrutta proprio questo fatto. Eye Spy funziona sul **M5Stack Atom Lite**, una scheda di sviluppo ESP32-PICO-D4 grande più o meno quanto una zolletta di zucchero, e monitora continuamente le bande BLE e WiFi alla ricerca delle firme elettroniche di dispositivi di registrazione, telecamere di sorveglianza, sistemi **ALPR** (lettori automatici di targhe), droni e tracker personali. Quando trova qualcosa, cambia colore al suo LED RGB.

*Non si connette a nulla e non trasmette.* Osserva, assegna punteggi e si illumina.

Questo articolo è un riferimento tecnico completo: spiega cosa rileva Eye Spy, come funziona il sistema di punteggio di confidenza, come sono progettati i motori di rilevamento, come costruire e programmare il dispositivo e quali sono i suoi limiti pratici.

**Preferite non costruirne uno?** STS Collective offre **[rilevatori Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** già programmati e pronti all'uso. Il codice lettore **SIMEONONSECURITY** offre fino al 20% di sconto.

{{< stscollective-ad "eyespy" >}}

---

## Indicatori LED: l'intera interfaccia utente

Come l'[ESP32 WiFi Canary: rilevamento passivo delle minacce a 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), l'intera uscita di Eye Spy consiste in un solo NeoPixel RGB SK6812 collegato al GPIO 27 dell'M5Stack Atom Lite. Il LED comunica costantemente uno dei quattro livelli di minaccia:

| Colore | Significato | Intervallo dei punteggi |
|-------|-------------|---------------------|
| 🔵 Impulso blu | Avvio / prima scansione | -- |
| 🟢 Verde fisso | Nessun dispositivo rilevato | 0–2 |
| 🟡 Giallo fisso | Attenzione: possibile dispositivo di registrazione nelle vicinanze | 3–5 |
| 🔴 Rosso lampeggiante | Allerta: rilevato un dispositivo di sorveglianza o tracciamento | 6+ |

**Una singola rilevazione ad alta confidenza (bodycam Axon, telecamera Flock Safety, corrispondenza OUI ALPR o AirTag) assegna abbastanza punti da portare immediatamente il LED al rosso in un solo ciclo di rilevamento.** Più rilevazioni di confidenza media si sommano fino al giallo e possono combinarsi per raggiungere il rosso.

---

## Hardware

### Dispositivo principale: M5Stack Atom Lite

| Componente | Dettaglio |
|-----------|--------|
| Scheda | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 su GPIO 27 |
| Pulsante | GPIO 39 (solo ingresso) |
| Flash | 4 MB |

L'Atom Lite è una piattaforma autonoma completa. **Non servono saldature, breadboard o componenti esterni.** Basta collegarlo all'USB.

### ESP32 DevKit generico

Un secondo ambiente di compilazione PlatformIO (`esp32dev`) è compatibile con qualsiasi ESP32 DevKit standard che abbia un LED integrato sul GPIO 2. Tutta la logica di rilevamento funziona nello stesso modo. Questa compilazione è utile per sviluppare e testare la logica oppure per distribuire il progetto quando non è necessario il formato dell'Atom Lite.

---

## Il sistema di punteggio

Eye Spy usa un **modello a punteggio di confidenza** che riunisce in un unico intero i segnali di tutti i motori di rilevamento. Il punteggio determina lo stato del LED (verde, giallo o rosso) ed è gestito da due meccanismi automatici:

### Riduzione del punteggio

Senza nuove rilevazioni, il punteggio scende di **1 punto ogni 60 secondi**. Se vi allontanate da un dispositivo rilevato, il LED torna verde in pochi minuti senza interventi da parte vostra.

### Intervallo prima di assegnare nuovamente punti

Ogni *tipo* di rilevamento ha un **intervallo di 120 secondi** prima di poter aggiungere altri punti dalla stessa sorgente. *In questo modo un dispositivo persistente non accumula punti all'infinito.* Una telecamera Flock Safety che resta nel raggio d'azione assegna +5 una volta, poi attende 120 secondi prima di contribuire di nuovo.

Insieme, questi meccanismi significano che:

- **Le rilevazioni temporanee** (per esempio, un'auto con un AirTag che passa) si risolvono automaticamente.
- **La sorveglianza persistente** (per esempio, un dispiegamento fisso di bodycam) mantiene il LED in allerta finché restate nel raggio d'azione.
- **Un solo dispositivo non fa accumulare punti senza controllo** a ogni rilevamento ripetuto.

---

## Motori di rilevamento

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagramma dei motori BLE e WiFi paralleli di Eye Spy, che cercano AirTag, bodycam, sistemi ALPR e droni e inviano i risultati al modello di minaccia basato sul punteggio di confidenza" >}}

Eye Spy alterna continuamente tre fasi di scansione:

**BLE passivo (9 s) → scansione WiFi (~3 s) → acquisizione in modalità promiscua (5 s) → ripetere**

Eye Spy arresta esplicitamente il BLE prima di qualsiasi operazione WiFi per rispettare la condivisione della radio ESP32. Il BLE riparte all'inizio di ogni ciclo.

---

### Motore 1: BLE, scansione passiva

La scansione BLE usa **NimBLE senza trasmettere richieste di scansione**. Il dispositivo ascolta i pacchetti pubblicitari BLE senza inviare risposte. *Così Eye Spy è elettronicamente invisibile ai dispositivi che cerca: un ricevitore passivo non viene rilevato dal bersaglio.*

Per ridurre i falsi positivi in ambienti affollati, vengono ignorati i dispositivi con segnale inferiore a **−90 dBm**.

#### Tabella di rilevamento BLE

| # | Obiettivo | Metodo di rilevamento | Punteggio |
|---|--------|-----------------|-------|
| 1 | **Bodycam Axon** | OUI MAC BLE `00:25:df` (Axon: bodycam, dispositivi Taser e apparecchiature delle forze dell'ordine) | +5 🔴 |
| 2 | **Occhiali smart Ray-Ban Meta** | UUID del servizio BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE Flock Safety** | Nome del dispositivo BLE contenente `Flock`, `Penguin`, `Pigvision` o `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer per carte (HC-03/05/06)** | Nome BLE esatto: moduli Bluetooth comuni negli skimmer dei terminali di pagamento | +5 🔴 |
| 5 | **Apple AirTag** | Dati del produttore `0x004C`, sottotipo `0x12`/`0x1E`, oppure payload `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | UUID del servizio BLE `0xFFFA` o payload dati del servizio AD con codice applicazione `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID del servizio BLE `0xFD5A` | +3 🟡 |
| 8 | **Tracker Tile** | UUID del servizio BLE `0xFEED` o `0xFEEC` | +3 🟡 |
| 9 | **Nodo MeshCore** | Prefisso del nome BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (tracciamento in negozi o luoghi)** | Dati del produttore `0x004C 0x02 0x15`, usati in negozi, aeroporti e stadi per tracciare gli spostamenti | +2 🟡 |
| 11 | **Dispositivo persistente sconosciuto** | MAC BLE non classificato rilevato almeno 3 volte in 5 minuti (rilevamento di ricognizione o tracciamento) | +2 🟡 |

#### Rilevamenti BLE importanti nel dettaglio

**Bodycam Axon (+5)**: Axon (in precedenza TASER International) produce alcuni dei sistemi bodycam più diffusi tra le forze dell'ordine negli Stati Uniti. L'OUI `00:25:df` è registrato ad Axon e compare nei suoi dispositivi indossabili. **Una sola rilevazione raggiunge subito la soglia di allerta.**

**Occhiali smart Ray-Ban Meta (+5)**: La collaborazione Ray-Ban Meta produce occhiali smart per i consumatori in grado di registrare video e scattare fotografie. Lo UUID del servizio BLE `0xFD5F` è l'annuncio caratteristico di questi dispositivi. *Sono prodotti di consumo e si possono incontrare in luoghi pubblici affollati.* Vale la pena prestare attenzione a una rilevazione con questo punteggio, indipendentemente dall'intento di chi li indossa.

**Moduli Bluetooth per skimmer (+5)**: HC-03, HC-05 e HC-06 sono moduli Bluetooth seriali economici che si trovano spesso nelle sovrapposizioni dei terminali di pagamento e negli skimmer per bancomat. Il rilevamento confronta il nome esatto del dispositivo con i nomi predefiniti del firmware dei moduli. **Un'allerta rossa giustifica un'ispezione fisica dei terminali di pagamento vicini.**

**Apple AirTag (+4)**: Gli AirTag trasmettono annunci tramite il protocollo proprietario Apple **Nearby Interaction**. Il rilevamento cerca l'intestazione dei dati specifica del produttore (`0x004C` = Apple) insieme ai sottotipi AirTag (`0x12` per l'annuncio standard e `0x1E` per quello di oggetto smarrito). I pattern del payload grezzo aggiungono una seconda modalità di rilevamento.

**OpenDroneID BLE (+4)**: Lo standard **ASTM F3411 Remote ID**, adottato anche dalla FAA per i droni commerciali negli Stati Uniti, definisce un protocollo di trasmissione con cui i droni annunciano identità e posizione. Eye Spy cerca l'UUID del servizio GATT `0xFFFA` (il servizio Remote ID designato) e il codice applicazione `0x0D` nel payload dei dati di servizio AD. *Un drone commerciale conforme in prossimità attiva questa rilevazione.*

**Dispositivo persistente sconosciuto (+2)**: È il motore di **rilevamento dei follower**. Registra ogni MAC BLE non classificato dalle rilevazioni specifiche precedenti. La MAC riceve un punteggio se compare almeno tre volte nell'arco di almeno cinque minuti. Il tracker di persistenza gestisce fino a 50 MAC sconosciute contemporaneamente ed elimina le voci dopo 30 minuti senza rilevamenti. **Così si individuano tracker personalizzati o modificati che non corrispondono a UUID di servizio o pattern di produttori noti.**

**iBeacon (+2)**: Negozi, aeroporti e stadi usano il formato iBeacon Apple (`0x4C 0x00 0x02 0x15`) per seguire il movimento dei dispositivi negli spazi fisici. La rilevazione si attiva con il formato pubblicitario standard, indipendentemente dallo UUID: identifica il tipo di installazione, non un UUID specifico. *Una rilevazione indica che probabilmente vi trovate in un luogo che traccia attivamente la presenza dei dispositivi Bluetooth.*

---

### Motore 2: scansione WiFi, ricerca attiva dei canali

Il motore di scansione WiFi usa l'interfaccia standard dell'ESP32 per cercare punti di accesso, elencare quelli nelle vicinanze e confrontare BSSID e SSID con le impronte note dei dispositivi di sorveglianza.

#### Tabella di rilevamento WiFi

| # | Obiettivo | Metodo di rilevamento | Punteggio |
|---|--------|-----------------|-------|
| 12 | **Telecamera Flock Safety (OUI)** | BSSID corrispondente alla tabella Flock Safety di 22 OUI (`d4:bb:e6`, `3c:61:05` e prefissi FS-Ext-Battery) | +5 🔴 |
| 13 | **Telecamera ALPR / LPR (OUI)** | BSSID corrispondente all'OUI `00:0e:58` di Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID con parole chiave Flock** | SSID contiene: `flock`, `flocksafety`, `fs ext`, `penguin` o `pigvision` | +5 🔴 |
| 15 | **SSID con parole chiave ALPR** | SSID contiene: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` o `automate` | +4 🔴 |
| 16 | **Produttore di telecamere di sorveglianza (OUI)** | BSSID corrispondente a una tabella di 31 OUI di telecamere: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix o Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID con parole chiave delle telecamere** | SSID contiene, tra le altre: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` o `genetec` | +2 🟡 |

#### Tabella OUI Flock Safety

La tabella `FLOCK_OUIS` con 22 voci è la ricerca più dettagliata del progetto. Comprende:

- `d4:bb:e6`: OUI Flock Safety registrato IEEE.
- `3c:61:05`: OUI Flock Safety registrato IEEE.
- Altri 20 prefissi MAC osservati sul campo negli hardware Flock FS-Ext-Battery e nelle telecamere WiFi Flock.

Queste 22 voci rappresentano intervalli di MAC hardware osservati nei sistemi di telecamere ALPR Flock Safety installati. **Il rilevamento tramite OUI è indipendente dallo SSID**: una telecamera Flock con uno SSID senza parole chiave assegna comunque +5 se corrisponde il suo OUI BSSID.

Gli OUI Flock Safety e Vigilant Solutions sono in tabelle separate, così entrambi possono assegnare punti indipendentemente nello stesso ciclo di scansione. *Un luogo con dispositivi di entrambi i produttori potrebbe accumulare +10 in un'unica scansione WiFi.*

#### Tabella OUI dei produttori di telecamere di sorveglianza

La tabella delle 31 telecamere di sorveglianza copre i principali produttori di telecamere IP presenti negli impianti commerciali, residenziali e nei negozi:

- **Imprese e attività commerciali**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix e Genetec.
- **Consumo e piccoli uffici**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex e Amcrest.
- **Infrastruttura**: Ubiquiti UniFi (punti di accesso e telecamere condividono intervalli OUI) e FLIR.

Una corrispondenza assegna +3, nel livello di attenzione, senza confermare parole chiave. Se corrisponde anche uno SSID con parole chiave, la stessa rete di telecamere riceve +3 dall'OUI e altri +2 dallo SSID, raggiungendo il livello di allerta in un singolo ciclo di scansione.

---

### Motore 3: WiFi promiscuo, acquisizione passiva dei frame

Il motore di scansione promiscuo porta la radio ESP32 in **modalità monitor** e acquisisce frame di gestione 802.11 grezzi. In questo modo rileva dispositivi che non annunciano uno SSID, in particolare i droni che usano il protocollo **Remote ID** tramite **WiFi Neighbor Awareness Networking (NaN)**.

Durante questa fase la radio **salta tra i canali** `{1, 6, 11, 3, 8, 13}` ogni 400 ms per ampliare la copertura dei canali di trasmissione dei frame NaN dei droni.

#### Tabella di rilevamento promiscuo

| # | Obiettivo | Metodo di rilevamento | Punteggio |
|---|--------|-----------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | Frame di gestione 802.11 diretto a `51:6f:9a:01:00:00`: trasmissione Remote ID ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: Lo standard ASTM F3411 definisce l'indirizzo multicast `51:6f:9a:01:00:00` per tutti i frame Remote ID WiFi NaN. I droni commerciali regolamentati che trasmettono posizione e identità tramite WiFi inviano frame a questo indirizzo. Eye Spy cerca frame di gestione destinati a questo MAC multicast: il rilevamento è passivo e affidabile. *Per evitarlo, l'operatore del drone dovrebbe disattivare Remote ID, violando le norme applicabili.*

Questo rilevamento integra il motore OpenDroneID BLE (rilevamento n. 6). *Un drone può annunciare la propria presenza tramite BLE, WiFi o entrambi, a seconda dell'hardware e della configurazione.* Eye Spy copre tutte e due le modalità.

---

## Programma delle fasi e gestione della radio

```
BLE passivo (9 s) → scansione WiFi (~3 s) → acquisizione in modalità promiscua (5 s) → ripetere
```

L'ESP32-PICO-D4 ha **una sola radio condivisa a 2,4 GHz** che gestisce sia BLE sia WiFi. Eye Spy la gestisce così:

1. **Fase BLE** (9 secondi): stack NimBLE attivo, scansione passiva in corso, nessuna richiesta di scansione trasmessa.
2. **Arresto BLE**: lo stack BLE viene arrestato esplicitamente prima di usare WiFi.
3. **Scansione WiFi** (~3 secondi): scansione attiva dei punti di accesso su tutti i canali, con confronto di OUI e SSID.
4. **Acquisizione promiscuo** (5 secondi): cattura passiva dei frame 802.11 con salto di canale.
5. **Arresto WiFi**: WiFi viene arrestato e il BLE riparte per il ciclo successivo.

La gestione esplicita delle fasi evita conflitti radio e garantisce a entrambi i motori, BLE e WiFi, un accesso ordinato alla radio a ogni ciclo.

---

## Output seriale

Tutte le righe iniziano con `[eyespy]` per agevolarne il filtraggio. Il monitor seriale funziona a **115200 baud**.

### Avvio

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Ciclo normale

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Eventi di rilevamento

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

Il campo `tracked=N` indica quante MAC BLE uniche si trovano attualmente nel tracker di persistenza. Aiuta a capire la densità dell'ambiente BLE.

### Campi del punteggio

Ogni riga di stato include:

- **score**: punteggio di minaccia attuale.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: motore attivo (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: numero di MAC BLE uniche nella tabella di persistenza.

---

## Compilazione e flashing

### Requisiti

- **PlatformIO** (CLI o estensione di VS Code).
- **M5Stack Atom Lite** o qualsiasi ESP32 DevKit.
- Cavo USB-C.

### Dipendenze

PlatformIO le installa automaticamente:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** controlla il LED RGB SK6812. **NimBLE-Arduino** fornisce lo stack di scansione BLE passiva. È preferito alla libreria BLE ESP32 predefinita perché supporta correttamente la modalità passiva, evita di inviare richieste di scansione e usa meno memoria.

### Flashing su M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Compila e carica su Atom Lite
pio run -e atom-lite -t upload

# Avvia il monitor seriale a 115200 baud
pio device monitor -b 115200
```

### Flashing su ESP32 DevKit generico

```bash
pio run -e esp32dev -t upload
```

### Struttura del progetto

```
eye-spy/
├── src/
│   └── main.cpp          # Tutta la logica del firmware
├── platformio.ini         # Ambienti di compilazione (atom-lite, esp32dev)
├── partitions_4mb.csv     # Tabella delle partizioni flash da 4 MB
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

*L'ambiente `atom-lite` usa la definizione della scheda `m5stick-c`, che ha lo stesso chip ESP32-PICO-D4 e una mappatura dei pin compatibile con il NeoPixel su GPIO 27.*

---

## Note sul rilevamento e limiti pratici

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Illustrazione in stile fotografico di Eye Spy sul M5Stack Atom Lite, grande più o meno quanto una zolletta di zucchero, tenuto tra due dita per mostrare le dimensioni compatte" >}}

### Cosa non può fare Eye Spy

**WiFi a 5 GHz**: l'ESP32 è un dispositivo **solo a 2,4 GHz**. Le telecamere di sorveglianza, i sistemi ALPR e i punti di accesso che funzionano esclusivamente sulle bande a 5 GHz non sono visibili ai motori di scansione WiFi o promiscuo. *Molte telecamere IP moderne supportano anche 2,4 GHz, pur essendo compatibili con i 5 GHz. Tuttavia, i dispositivi esclusivamente a 5 GHz non vengono rilevati.*

**BLE cifrato**: alcuni prodotti di sorveglianza di fascia alta cifrano o offuscano gli annunci BLE. Eye Spy rileva i dispositivi che trasmettono in chiaro firme identificabili come OUI, UUID del servizio e dati del produttore. *I dispositivi che cambiano indirizzo MAC, funzione di privacy sempre più comune nei tracker di consumo, evitano il rilevamento basato sulla MAC.* Il tracker di persistenza potrebbe rilevarli solo se il cambio avviene meno frequentemente di ogni cinque minuti.

**Telecamere cablate**: **Le telecamere IP collegate via Ethernet e prive di radio WiFi non emettono segnali wireless che Eye Spy possa rilevare.** Le telecamere nascoste senza connessione di rete che registrano solo in locale non producono a loro volta una firma RF.

**Limiti della portata**: In ambienti interni, l'antenna ESP32 riceve segnali forti a una distanza pratica di **20–40 metri**, meno per segnali deboli o schermati. *I dispositivi al limite della portata o dietro schermature RF rilevanti potrebbero non assegnare punti o non superare la soglia RSSI di −90 dBm.*

### Falsi positivi prevedibili

**Telecamere di consumo nelle case vicine**: Ring, Nest, Wyze, Arlo e Reolink sono diffuse nei quartieri residenziali e i loro OUI compaiono nella tabella delle 31 telecamere. *In zone residenziali sono prevedibili alcune rilevazioni gialle di attenzione (+3) dovute alle videocamere dei campanelli dei vicini.* Non sono falsi positivi in senso tecnico, perché il dispositivo rileva *davvero* una telecamera. Il contesto resta importante.

**Installazioni iBeacon nei negozi**: i grandi rivenditori installano infrastrutture iBeacon praticamente in ogni negozio. *Una visita a un centro commerciale o a un supermercato probabilmente attiverà la rilevazione iBeacon (+2).* Il dispositivo funziona come previsto: l'infrastruttura di tracciamento commerciale è davvero presente.

**Infrastruttura Ubiquiti UniFi**: i punti di accesso UniFi compaiono nella tabella OUI delle telecamere perché Ubiquiti produce sia apparati di rete sia telecamere di sicurezza con intervalli OUI sovrapposti. *Una rete che usa apparecchiature UniFi assegna +3 alle corrispondenze OUI del motore WiFi.*

**Samsung SmartTag e dispositivi di consumo**: lo UUID SmartTag (`0xFD5A`) è un servizio registrato da Samsung. *Gli SmartTag sono tracker di consumo con usi personali legittimi.* La presenza di uno SmartTag nelle vicinanze attiva la rilevazione.

### Significato pratico dei livelli di punteggio

| Punteggio | Situazione probabile nel mondo reale |
|-------|-----------------------------|
| 6–10 (🔴) | Rilevazione credibile ad alta confidenza: bodycam Axon entro circa 30 m, telecamera Flock Safety con OUI corrispondente, pattern confermato di AirTag che segue o drone che trasmette Remote ID |
| 3–5 (🟡) | Più tracker di consumo, telecamere dei vicini che si sommano, possibile telecamera Flock o una singola rilevazione OpenDroneID |
| 0–2 (🟢) | Nessuna firma di sorveglianza significativa rilevata; sono presenti normali comunicazioni di dispositivi di consumo ma restano sotto soglia |

---

## Confronto con progetti correlati

Eye Spy si occupa della sorveglianza fisica nell'ambiente; [ESP32 WiFi Canary: rilevamento passivo delle minacce a 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) rileva attacchi WiFi di livello rete contro i vostri dispositivi. *Sono strumenti complementari che affrontano modelli di minaccia diversi.*

| Funzionalità | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Rilevamento AirTag e tracker | ✅ | ❌ |
| Rilevamento telecamere ALPR / Flock | ✅ | ❌ |
| Rilevamento bodycam | ✅ | ❌ |
| Rilevamento droni (Remote ID) | ✅ | ❌ |
| Rilevamento access point evil twin | ❌ | ✅ |
| Rilevamento attacchi di deautenticazione | ❌ | ✅ |
| Rilevamento downgrade della sicurezza | ❌ | ✅ |
| Apprendimento di una baseline | ❌ | ✅ |
| BLE passivo | ✅ | ❌ |
| Stessa piattaforma hardware | ✅ | ✅ |

Entrambi i progetti funzionano sullo stesso hardware M5Stack Atom Lite, con gli stessi indicatori LED e lo stesso sistema di compilazione PlatformIO. Per monitorare la sorveglianza fisica e quella di rete, potete installare i due progetti su unità Atom Lite separate e portarle con voi.

Eye Spy integra anche il [progetto di rilevamento Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) per chi si interessa in particolare alle infrastrutture di sorveglianza ALPR.

---

## Casi d'uso

### Consapevolezza della sorveglianza nelle vicinanze

Il pubblico principale di Eye Spy comprende chi vuole conoscere le infrastrutture di sorveglianza nelle immediate vicinanze. Camminando in un quartiere, passando in auto accanto a un incrocio o partecipando a un evento pubblico, Eye Spy traduce la complessa analisi RF in **un unico stato del LED in tempo reale**.

### Rilevamento dello stalking con AirTag

Lo stalking basato su AirTag è un problema documentato. Il **motore di rilevamento dei follower** di Eye Spy (una MAC BLE sconosciuta e persistente vista almeno 3 volte nell'arco di almeno 5 minuti) è pensato per tracker personalizzati o modificati che non corrispondono al formato noto degli annunci Apple. Insieme al rilevamento diretto degli AirTag, offre **due modalità indipendenti per individuare un tracker che vi segue**.

### Ispezione di alloggi in affitto e camere d'albergo

Entrare in una nuova camera d'albergo o in un alloggio in affitto con Eye Spy attivo offre una prima indicazione di dispositivi BLE e WiFi inattesi. Una corrispondenza di SSID con parole chiave di telecamere oppure un OUI di sorveglianza nella scansione WiFi aggiunge punti di attenzione. *Non sostituisce un'indagine RF completa*, ma aggiunge un livello passivo di controllo ambientale all'ispezione fisica.

### Installazioni ALPR e ricerca sulla privacy

Chi ricerca le infrastrutture di sorveglianza, i giornalisti che operano in ambienti sorvegliati e i sostenitori della privacy possono usare Eye Spy come dispositivo di rilevamento portatile e poco costoso. L'output seriale registra ogni rilevazione con il valore RSSI, quindi può fungere da semplice strumento di raccolta dati.

### Sicurezza in viaggio

Come WiFi Canary, Eye Spy è progettato per essere portatile. L'Atom Lite entra in una tasca o si aggancia a una borsa. Durante viaggi in aeroporti, stazioni ferroviarie o eventi pubblici con una sorveglianza nota, offre un monitoraggio passivo continuo senza richiedere interazioni.

---

## Note sull'architettura

### Perché il BLE passivo è importante

La scelta della scansione BLE passiva, senza pacchetti di richiesta, ha conseguenze importanti per la sicurezza. Nella scansione BLE standard, lo scanner trasmette un pacchetto **SCAN_REQ** per chiedere dati pubblicitari aggiuntivi a ogni dispositivo che pubblicizza. *La scansione BLE attiva è quindi osservabile da entrambi i dispositivi*: quello sottoposto a scansione vede l'indirizzo dello scanner nella richiesta.

La modalità passiva NimBLE ascolta solo gli annunci non diretti (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) e non trasmette mai uno SCAN_REQ. **Eye Spy non trasmette nulla tramite BLE durante la scansione.** Una bodycam Axon, un dispositivo Flock o un AirTag rilevato non può osservare né reagire alla presenza dello scanner.

### Progettazione del tracker di persistenza

Il tracker dei dispositivi sconosciuti mantiene una tabella di massimo **50 indirizzi MAC BLE** con gli orari della prima e dell'ultima rilevazione. La rilevazione si attiva quando una MAC appare almeno tre volte in una finestra di almeno cinque minuti.

Il limite di 50 voci e la rimozione dopo 30 minuti sono scelte progettuali che bilanciano la sensibilità del rilevamento con i limiti di RAM dell'ESP32. *In un ambiente BLE denso (trasporti pubblici, conferenze, centri commerciali) la tabella potrebbe riempirsi rapidamente di dispositivi di consumo.* La soglia RSSI di −90 dBm filtra quelli lontani e concentra il tracker sulle sorgenti vicine e persistenti.

### Interazione tra riduzione del punteggio e intervallo di attesa

L'**intervallo di 120 secondi** impedisce a un dispositivo che resta sempre nel raggio d'azione di accumulare punti a ogni ciclo BLE di nove secondi. Senza l'intervallo, una singola telecamera Flock aggiungerebbe +5 ogni 15 secondi e raggiungerebbe centinaia di punti in pochi minuti.

La **riduzione di 1 punto ogni 60 secondi** abbassa il punteggio quando un dispositivo esce dal raggio e l'intervallo scade senza nuove rilevazioni. *Una rilevazione singola da +5 che non si ripete scende a zero in cinque minuti.* Così il dispositivo torna naturalmente a uno stato di tranquillità adatto a normali spostamenti.

---

## Contributi e stato del progetto

Eye Spy è disponibile con licenza Apache-2.0 su [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Tra le possibili estensioni:

- **Aggiungere voci OUI**: estendere le tabelle OUI di Flock Safety e delle telecamere quando sul campo vengono documentate nuove MAC hardware.
- **Aggiungere UUID di servizio BLE**: nuovi occhiali smart, telecamere e tracker introducono altri UUID.
- **Regolare il tracker di persistenza**: il limite di 50 voci, la soglia di 3 rilevazioni e la finestra di 5 minuti sono costanti modificabili.
- **Registrare dati seriali**: il formato dell'output seriale è progettato per l'analisi automatizzata. Un registratore esterno può raccogliere gli eventi da più unità Eye Spy.

Il firmware si trova in un unico file `main.cpp` nella directory `src/`, quindi è facile leggerlo, verificarlo e modificarlo.

---

## Conclusione

Eye Spy affronta un problema circoscritto ma importante: l'ambiente fisico intorno a voi è sempre più dotato di sistemi di sorveglianza e la maggior parte trasmette firme RF rilevabili. **Un M5Stack Atom Lite da 15 dollari con il firmware Eye Spy diventa uno scanner ambientale continuo** che traduce la complessità dell'analisi dei pacchetti BLE e delle ricerche OUI WiFi in un unico LED RGB.

Il modello a punteggio di confidenza assegna pesi realistici alle minacce: una bodycam Axon vicino a un dispiegamento delle forze dell'ordine ottiene +5 e accende subito il LED rosso; un iBeacon commerciale ottiene +2 e contribuisce alla consapevolezza senza attivare da solo un falso allarme. La riduzione del punteggio e gli intervalli impediscono al dispositivo di segnalare eccessivamente segnali temporanei o persistenti di basso livello.

Per le attività di controsorveglianza, la sicurezza in viaggio, il rilevamento degli AirTag o semplicemente per sapere se qualcosa nelle vicinanze vi osserva, Eye Spy è uno strumento pratico, open source e passivo che merita un posto nel kit di ogni professionista della sicurezza.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Acquista i rilevatori Eye Spy e risparmia il 20%
{{< /centerbutton >}}
