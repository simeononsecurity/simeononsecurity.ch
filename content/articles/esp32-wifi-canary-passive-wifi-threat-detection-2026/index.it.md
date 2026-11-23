---
title: "ESP32 WiFi Canary: rilevamento passivo delle minacce a 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Analisi tecnica di ESP32 WiFi Canary, un sensore passivo a 2,4 GHz che rileva evil twin, deautenticazione, downgrade di sicurezza e inondazioni di beacon."
genre: ["Sicurezza di rete", "Sicurezza WiFi", "Sicurezza IoT", "Ricerca sulla sicurezza", "Sistemi embedded", "Strumenti per la privacy", "Progetti ESP32", "Sicurezza hardware", "Sicurezza wireless", "Sicurezza open source"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Rilevamento deautenticazione", "Rilevamento evil twin", "Sicurezza WiFi", "Monitoraggio passivo WiFi", "Frame di gestione 802.11", "Sicurezza di rete", "Sicurezza IoT", "NeoPixel", "SK6812", "PlatformIO", "C++", "Software a codice aperto", "Sensore di sicurezza", "Rilevamento minacce wireless", "Monitoraggio BSSID", "Monitoraggio SSID", "Rilevamento downgrade di sicurezza", "Rilevamento inondazione beacon", "Monitoraggio WiFi", "LED RGB", "Modalità promiscuous", "Sicurezza embedded", "Sicurezza in viaggio", "Sicurezza WiFi in hotel", "WiFi nei bar", "Consapevolezza della sicurezza", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Illustrazione di un piccolo dispositivo simile a ESP32 WiFi Canary collegato a una porta USB. Il LED RGB si illumina in diversi colori per rappresentarne le capacità di rilevamento delle minacce."
coverCaption: ""
---

**Un sensore passivo WiFi, grande come un pollice, che non trasmette mai**

## Il problema del WiFi pubblico

Quando ti colleghi al WiFi di un hotel, a un hotspot di un bar o a una rete aeroportuale, ti fidi che il punto di accesso sia autentico. Il problema è che i **frame di gestione 802.11**, che annunciano le reti, gestiscono le connessioni e coordinano i client, sono *privi di autenticazione nella maggior parte delle implementazioni*. Con hardware modesto chiunque può clonare un SSID, inviare frame di deautenticazione o creare un'esca aperta accanto a una rete WPA2 legittima.

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) è un sensore passivo che rende visibile questo rischio con un ingombro minimo. Si basa su M5Stack Atom Lite, grande all'incirca come una zolletta di zucchero. Si collega a una porta USB, apprende l'ambiente e accende un LED RGB quando rileva schemi compatibili con minacce wireless.

Non si connette a nulla, non acquisisce credenziali e non trasmette frame. Osserva, assegna un punteggio e comunica la situazione con un colore.

Questo articolo è una guida tecnica completa al progetto: rilevamenti, modello di affidabilità, compilazione e flash, oltre ai limiti pratici.

---

## Cosa fa e non fa ESP32 WiFi Canary

### Sempre e solo passivo

WiFi Canary usa due modalità radio, mai contemporaneamente:

1. **Modalità promiscuous**: riceve e ispeziona i frame di gestione 802.11, come quelli di deautenticazione e disassociazione, senza associarsi a una rete.
2. **Modalità scansione**: esegue scansioni WiFi attive per elencare i punti di accesso vicini e confrontarli con una baseline appresa.

Il dispositivo non:
- si associa né si connette a una rete;
- acquisisce frame dati o credenziali;
- trasmette frame 802.11;
- salva dati su memoria flash persistente;
- comunica tramite Internet.

**Tutto ciò che apprende resta in RAM e viene cancellato al riavvio.** È una scelta intenzionale: il canary è un **sensore**, non un dispositivo di acquisizione.

### Il LED è l'interfaccia

Non ci sono display, app o interfaccia web. L'unica uscita del dispositivo è un **NeoPixel RGB SK6812** sul GPIO 27 di M5Stack Atom Lite. Il LED indica quattro stati:

| Stato LED | Significato |
|---|---|
| 🔵 Blu (impulso lento) | Avvio, creazione della baseline |
| 🟢 Verde (fisso) | Normale, nessun problema ad alta affidabilità |
| 🟡 Giallo (fisso) | Attenzione, rilevato uno schema sospetto |
| 🔴 Rosso (impulso rapido) | Allarme, rilevata una minaccia più affidabile |

L'avvio richiede circa **24 secondi** (3 scansioni da 8 secondi). Quando il LED lascia il blu, la baseline è pronta e inizia il monitoraggio.

---

## Hardware

### Obiettivo principale: M5Stack Atom Lite

Il progetto è pensato per M5Stack Atom Lite, una piattaforma di sviluppo ESP32 completa in un involucro da 24 × 24 mm.

| Componente | Dettaglio |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Un NeoPixel RGB SK6812 (GPIO 27) |
| Pulsante | GPIO 39, attivo basso |
| USB | Bridge UART CP2104 |
| Alimentazione | USB-C, circa 80–120 mA durante la scansione |

**Niente breadboard, componenti esterni o saldature.** Basta collegarlo all'alimentazione USB.

### ESP32 DevKit generico per sviluppo e test

Il progetto include un secondo ambiente PlatformIO (`esp32dev`) per le schede ESP32 standard. In questa configurazione:

- il LED integrato sul GPIO 2 sostituisce il NeoPixel;
- è abilitato l'output completo di debug seriale;
- la logica di rilevamento funziona come nella build Atom Lite.

Il progetto è accessibile a chiunque abbia un ESP32 DevKit da $5 e permette di testare la logica senza l'hardware obiettivo.

---

## Processo di apprendimento della baseline

### Perché la baseline è importante

Un canary che segnala ogni rete aperta in città sarebbe inutile. ESP32 WiFi Canary impara prima l'ambiente e poi assegna un punteggio alle minacce. La prima fase costruisce una **tabella di riferimento** dei punti di accesso legittimi presenti nell'area.

### Tre scansioni, 24 secondi

All'avvio, il dispositivo esegue tre scansioni WiFi consecutive, separate da una pausa. Al termine, memorizza come baseline i punti di accesso appresi: SSID, BSSID, tipo di crittografia e potenza del segnale.

L'output seriale durante questa fase è simile a:

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Quando il LED passa dal blu al verde, il dispositivo è operativo.

---

## Cosa rileva: categorie di minacce

WiFi Canary monitora sei schemi di minaccia. Ognuno aggiunge punti a un **punteggio di affidabilità** che determina lo stato del LED. *Un singolo indicatore non è considerato una prova certa*: il modello raccoglie segnali concordanti prima di aumentare il livello.

### 1. Raffiche di deautenticazione e disassociazione

I **sottotipi 10 (disassociazione) e 12 (deautenticazione) dei frame di gestione 802.11** sono strumenti comuni negli attacchi WiFi. Qualsiasi dispositivo può inviarli e i client che li ricevono vengono disconnessi dal punto di accesso.

In **modalità promiscuous**, il canary conta questi frame per MAC sorgente in una finestra mobile di **5 secondi**.

| Condizione | Punti aggiunti |
|---|---|
| ≥ 8 frame da una sorgente in 5 s | +2 |
| ≥ 20 frame da una sorgente in 5 s | +4 |
| ≥ 5 frame di deautenticazione broadcast | +1 |

**Le soglie contano**: un client che passa da un punto di accesso a un altro genera alcuni frame legittimi. Gli strumenti di attacco ne generano centinaia al secondo contro un obiettivo. La finestra di 5 secondi e il limite di 8 frame filtrano il rumore del roaming e rilevano raffiche persistenti di strumenti come `aireplay-ng`.

### 2. Clone aperto di una rete crittografata nota (evil twin)

**È il rilevamento con maggiore affidabilità.** Un attacco evil twin spesso:

1. Crea una copia aperta, senza password, di un SSID WPA2 noto.
2. Trasmette con segnale più forte del punto reale per far connettere automaticamente i client.

Dopo l'apprendimento della baseline, una nuova scansione rileva un SSID che prima usava solo WPA/WPA2/WPA3 e ora appare come **OPEN**:

| Condizione | Punti aggiunti |
|---|---|
| Stesso SSID, prima crittografato e ora aperto | +3 |
| BSSID non presente nella baseline | +1 |
| Segnale del clone ≥ 10 dB più forte del punto noto | +1 |

Un clone aperto del WiFi dell'hotel, con segnale 10 dB più forte del punto reale, è un caso da manuale. *Questa combinazione porta il punteggio a 5 (Attenzione) in un solo ciclo di scansione.*

**Esempio seriale**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Punto di accesso crittografato originale assente e clone aperto presente

Variante avanzata: il clone più potente induce i client a preferirlo e il punto di accesso reale viene contemporaneamente espulso dall'etere tramite deautenticazione.

| Condizione | Punti aggiunti |
|---|---|
| Punto crittografato della baseline scomparso e rete aperta corrispondente apparsa | +3 |

Questo copre i casi in cui il punto reale continua a trasmettere ma perde la competizione di potenza del segnale, oppure viene interrotto attivamente.

### 4. Downgrade di sicurezza

Lo stesso SSID presente nella baseline viene osservato con crittografia più debole di quella registrata.

| Condizione | Punti aggiunti |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Calo di almeno 2 livelli di crittografia | +3 |

*I downgrade a rete aperta sono gestiti dal rilevamento evil twin con punteggi più alti.* Questa categoria copre i downgrade parziali che potrebbero sfuggire a un semplice confronto tra aperto e crittografato.

### 5. SSID duplicato da un fornitore inatteso

Stesso SSID e stesso tipo di sicurezza di un punto di accesso della baseline, ma con un BSSID che usa un **OUI del fornitore diverso** (i primi 3 byte dell'indirizzo MAC).

| Condizione | Punti aggiunti |
|---|---|
| OUI diverso dal punto della baseline con lo stesso SSID | +1 |
| Clone anche ≥ 10 dB più potente | +2 |

*Il punteggio è volutamente basso.* Reti aziendali, sistemi mesh e punti di accesso degli ISP possono avere legittimamente più BSSID per lo stesso SSID, con fornitori diversi. Questo segnale deve sommarsi ad altri elementi e non attivare da solo un allarme.

### 6. Inondazione di beacon o SSID

Conta i nuovi SSID assenti dalla baseline che compaiono in una **finestra mobile di 30 secondi**.

| Condizione | Punti aggiunti |
|---|---|
| ≥ 15 nuovi SSID in 30 s | +2 |
| ≥ 30 nuovi SSID in 30 s | +3 |

Gli **attacchi di inondazione dei beacon** trasmettono migliaia di SSID falsi per confondere le tabelle di scansione o impedire i beacon legittimi. Quindici nuovi SSID sconosciuti in 30 secondi sono insoliti nella maggior parte degli ambienti.

---

## Modello del punteggio di affidabilità

Tutti i segnali rilevati confluiscono in un **punteggio di minaccia** intero che controlla lo stato del LED:

| Intervallo | Stato LED |
|---|---|
| 0–2 | Normale (verde) |
| 3–5 | Attenzione (giallo) |
| 6+ | Allarme (rosso, impulso rapido) |

### Decadimento del punteggio

In assenza di nuovi eventi, il punteggio **scende di 1 punto ogni 60 secondi**. È una delle scelte di progettazione più importanti:

- Una raffica di deautenticazione porta il punteggio ad Attenzione; se l'attacco si interrompe, torna automaticamente a Normale in pochi minuti.
- Un attacco persistente mantiene lo stato di Allarme.
- Il dispositivo si ripristina da solo senza intervento o riavvio.

Questo significa che:
- **Le anomalie brevi** (roaming o variazioni temporanee delle reti vicine) si risolvono da sole.
- **Gli attacchi persistenti** restano segnalati.
- **Niente affaticamento da allarmi** per singoli eventi che non si ripetono.

### Reset con il pulsante

Il pulsante GPIO 39 di Atom Lite esegue due azioni:

1. Invia la tabella AP corrente completa all'output seriale, utile per verificare cosa vede il dispositivo.
2. Azzera il punteggio di minaccia e riporta subito il LED al verde per osservare il ciclo successivo senza storico.

---

## Compilazione e flash

### Requisiti

- **PlatformIO** (CLI o estensione VS Code)
- **M5Stack Atom Lite** (oppure ESP32 DevKit per test)
- Cavo USB-C

### Flash su M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Compilazione e flash
pio run -e atom-lite --target upload

# Apri il monitor seriale a 115200 baud
pio device monitor -b 115200
```

### Flash su ESP32 DevKit generico

```bash
pio run -e esp32dev --target upload
```

La build DevKit usa GPIO 2 (LED integrato) e mostra il log seriale completo. Non pilota il NeoPixel. La logica di rilevamento è identica a quella di Atom Lite.

### Struttura del progetto

```
esp32-wifi-canary/
├── main.cpp              # Tutta la logica del firmware
├── platformio.ini        # Ambienti di build (atom-lite, esp32dev)
├── partitions_4mb.csv    # Tabella delle partizioni flash da 4 MB
└── README.md
```

L'intero firmware è in **un singolo file sorgente C++**. La logica di rilevamento non richiede librerie esterne, solo il framework ESP32 Arduino per scansione WiFi, callback promiscuous e controllo NeoPixel.

### Ambienti platformio.ini

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

L'ambiente `atom-lite` usa la definizione board `m5stick-c` (stesso chip ESP32-PICO-D4 e mappatura pin compatibile con il NeoPixel su GPIO 27).

---

## Riferimento dell'output seriale

Il dispositivo produce log dettagliati a **115200 baud**. Tutte le righe iniziano con `[canary]` per semplificare i filtri.

### Sequenza di avvio

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Eventi di rilevamento

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Transizioni del punteggio

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Il log seriale mostra cosa ha visto il dispositivo, quando e perché è cambiato il punteggio. Funziona anche come **registro di controllo passivo** senza dover guardare il LED.

---

## Note di rilevamento e limiti pratici

Il README è insolitamente chiaro su ciò che il dispositivo non può fare. Ecco i limiti nel dettaglio.

### Possibili falsi positivi

**Reti aziendali e mesh** sono la principale fonte di falsi positivi. Una grande rete aziendale, un hotel o un sistema mesh come Eero o Google WiFi può legittimamente mostrare:

- Più BSSID per lo stesso SSID con OUI di fornitori diversi.
- Differenze di configurazione di sicurezza tra bande.
- Punti di accesso che compaiono e scompaiono quando la mesh si adatta.

**Router Airbnb e SOHO** con SSID diversi per banda possono anch'essi mostrare OUI diversi se le radio a 2,4 e 5 GHz usano blocchi MAC consecutivi di fornitori differenti.

*Variazioni transitorie delle reti vicine*: una rete crittografata che scompare temporaneamente dalla scansione e riappare con parametri diversi (aggiornamento firmware, riavvio o riconfigurazione) può attivare per poco tempo il rilevamento.

Il punteggio e il decadimento servono a *ridurre, non eliminare*, i falsi positivi.

### Possibili falsi negativi

Un **attacco evil twin ben realizzato** che:

- Falsifica il BSSID esatto del punto legittimo, così l'OUI coincide.
- Usa esattamente lo stesso tipo di sicurezza e una configurazione IE WPA2 corretta.
- Trasmette con potenza entro 10 dB dal punto reale.

*Potrebbe non accumulare abbastanza punti per raggiungere Attenzione.* La componente di deautenticazione necessaria per espellere i client aggiungerebbe punti, ma un attaccante sofisticato che limita i frame potrebbe restare sotto soglia.

### Intervallo durante il cambio radio

**La radio ESP32 non può essere in modalità promiscuous e scansionare attivamente i punti di accesso allo stesso tempo.** Il firmware alterna le modalità. Di conseguenza, **i frame di deautenticazione che arrivano nella finestra di scansione di circa 3 secondi non vengono acquisiti**. Un attaccante potrebbe sincronizzare le raffiche con queste finestre, ma dovrebbe conoscere la pianificazione delle scansioni.

### Solo 2,4 GHz

La radio ESP32 opera a 2,4 GHz. **Le reti a 5 e 6 GHz non vengono scansionate né monitorate.** Il dispositivo non rileva evil twin attivi solo a 5 GHz.

### Portata passiva

Il rilevamento richiede che il dispositivo riceva i frame di deautenticazione. Un attaccante lontano, con antenna molto direzionale, o che prende di mira un client lontano dal canary, potrebbe trasmettere segnali troppo deboli per attivare i contatori.

---

## Casi d'uso

### Viaggi con lavoro sensibile

Il canary è pensato soprattutto per i viaggi. Collegalo all'USB di un portatile, a una presa USB in hotel o a una batteria portatile e lascia che apprenda l'ambiente dell'hotel o del centro congressi. La successiva comparsa di un clone aperto dell'SSID dell'hotel, lo scenario più comune, attiva almeno lo stato Attenzione.

### Bar e WiFi pubblico

Gli ambienti WiFi aperti sono un bersaglio comune per gli evil twin. La baseline apprende il punto legittimo all'arrivo e poi controlla eventuali SSID concorrenti.

### Consapevolezza e formazione sulla sicurezza

L'output seriale offre un log leggibile e dettagliato. In una formazione, mostrare in tempo reale una raffica di deautenticazione e il cambio di colore del LED è molto più efficace di una presentazione.

### Monitoraggio passivo di laboratorio

In un home lab o in un piccolo ufficio, il canary può funzionare come monitor ambientale continuo. Il LED mostra lo stato a colpo d'occhio e il pulsante fornisce la tabella delle reti attuali su richiesta.

---

## Note sull'architettura

### Perché un singolo punteggio invece di allarmi separati

Il modello somma segnali diversi in un solo numero, anziché mostrare categorie separate. È una scelta deliberata dell'interfaccia: il dispositivo usa un LED con tre stati. Allarmi distinti richiederebbero display o app. *Il punteggio trasforma segnali rumorosi e parzialmente correlati in un singolo indicatore utile.*

### Perché il punteggio decade

Senza decadimento, un singolo falso positivo richiederebbe un intervento manuale con il pulsante. Con il calo ogni 60 secondi, le anomalie brevi scompaiono in pochi minuti. **Il canary può quindi funzionare senza supervisione** in una borsa, in una camera d'hotel o in auto, tornando alla baseline dopo eventi temporanei.

### Perché tre scansioni iniziali

Una singola scansione potrebbe non vedere un punto di accesso che in quel momento non trasmetteva, per una pausa o un'interruzione temporanea. *Tre scansioni in circa 24 secondi descrivono meglio l'ambiente stabile prima di avviare il monitoraggio.*

---

## Contributi e stato del progetto

Il progetto è disponibile su [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) con una licenza per uso passivo. Il codice è in un unico `main.cpp`, facile da leggere, controllare ed estendere.

Chi usa PlatformIO ed ESP32 può compilare il progetto senza modifiche sia per Atom Lite sia per un DevKit standard.

---

## Confronto con altri approcci al monitoraggio WiFi

| Approccio | Passivo? | Senza credenziali | Un solo LED | Formato da viaggio |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (portatile) | ✅ | ✅ | ❌ (richiede display) | ❌ (ingombrante) |
| WiFi Pineapple | ❌ (attivo) | ❌ | ❌ | Parziale |
| IDS wireless (aziendale) | ✅ | ✅ | ❌ (richiede infrastruttura) | ❌ |
| Scansione manuale (app telefono) | Parziale | ✅ | ❌ | ✅ |

Il canary occupa una nicchia precisa: **monitoraggio ambientale continuo, senza interazione e senza rete**, in un formato che sta su un portachiavi o nella borsa del portatile.

---

## Conclusione

ESP32 WiFi Canary fa una cosa: osserva l'ambiente a 2,4 GHz e cambia colore quando nota qualcosa di sospetto. Non è un sistema completo di rilevamento intrusioni wireless, uno strumento di cattura pacchetti o un analizzatore forense. È un canary, un sensore passivo che segnala quando l'ambiente diventa pericoloso.

Il **modello del punteggio di affidabilità**, il **decadimento del punteggio** e la **baseline in tre fasi** affrontano il problema dei falsi positivi dei sensori ambientali. Il dispositivo può funzionare senza supervisione in hotel o centri congressi e segnalare anomalie significative senza reagire al normale ricambio delle reti.

Per chi prepara un kit di sicurezza portatile, lavora in ambienti con infrastrutture WiFi non affidabili o cerca un progetto ESP32 utile, WiFi Canary vale un pomeriggio e un M5Stack Atom Lite da $15.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
