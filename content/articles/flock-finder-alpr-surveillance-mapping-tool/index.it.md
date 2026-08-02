---
title: "Flock Finder: Mappa delle telecamere ALPR di Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder è uno strumento open source che mappa oltre 40.000 telecamere Flock Safety ALPR in tutto il mondo utilizzando i dati WiFi di WiGLE e il fingerprinting OUI. Scopri come funziona, i suoi limiti e gli strumenti hardware per il rilevamento in tempo reale."
genre: ["Tecnologia della privacy", "Contro-sorveglianza", "Progetti open source", "Diritti digitali", "Sicurezza delle reti", "Strumenti per la privacy", "Hardware hacking", "Ricerca sulla sicurezza"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Lettore di targhe", "Fingerprinting OUI", "WiGLE", "Sorveglianza WiFi", "Contro-sorveglianza", "STS Collective", "FlockYou", "ESP32", "Strumenti per la privacy", "NitekryDPaul", "DeFlockJoplin", "Rilevamento ALPR", "Sicurezza open source", "Mappatura della sorveglianza", "Sorveglianza di massa", "WiFi OUI", "Protezione della privacy", "Indirizzo MAC", "Modalità promiscua", "802.11", "Rilevamento in tempo reale", "Wardriving", "Diritti digitali", "Libertà civili", "Consapevolezza della sorveglianza", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Una mappa interattiva che mostra indicatori colorati che indicano le posizioni delle telecamere Flock Safety ALPR, con segnali WiFi astratti che emanano dagli indicatori su uno sfondo scuro."
coverCaption: "Flock Finder mappa oltre 40.000 presunte telecamere Flock Safety ALPR utilizzando i dati WiFi di WiGLE e il fingerprinting OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Uno strumento open source per la consapevolezza della sorveglianza che mappa le telecamere Flock Safety ALPR utilizzando dati WiFi raccolti dalla comunità.**

## Cos'è Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** è un progetto open source che mappa le **telecamere Flock Safety ALPR (Lettore Automatico di Targhe)** negli Stati Uniti e in altri 108 paesi. Combina **31 prefissi OUI (Identificatore Unico Organizzativo) WiFi di Flock Safety noti** con il **database WiFi crowd-sourced WiGLE** per identificare e tracciare le posizioni presunte delle telecamere su una mappa interattiva.

Il progetto si trova su **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, si aggiorna automaticamente ogni giorno tramite GitHub Actions e, a luglio 2026, ha mappato **oltre 40.000 telecamere presunte** in 964 regioni in tutto il mondo.

| Metrica | Valore |
|--------|-------|
| **Telecamere mappate** | 40.026+ |
| **Prefissi OUI noti** | 31 |
| **Paesi coperti** | 109 |
| **Regioni coperte** | 964 |
| **Conservazione dei dati** | 730 giorni (2 anni) |
| **Frequenza di aggiornamento automatico** | Quotidianamente |

*Questo è uno strumento di consapevolezza generale, non un inventario definitivo. Leggi la sezione sulle limitazioni prima di trarre conclusioni dai dati.*

Per informazioni sul perché la sorveglianza ALPR di Flock Safety è importante per la privacy, leggi **[Sorveglianza tramite telecamere Flock Safety: prevalenza, preoccupazioni sulla privacy e strategie di protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Come funziona: Fingerprinting OUI tramite WiGLE

### Il concetto centrale

Le telecamere Flock Safety contengono **ricetrasmettitori WiFi** che si svegliano periodicamente dal sonno per caricare i dati delle targhe catturate sul cloud. Durante queste brevi finestre attive, la telecamera trasmette frame WiFi che contengono il suo **indirizzo MAC** — e i primi tre byte di ogni indirizzo MAC identificano il produttore. Questo è l'**OUI (Identificatore Unico Organizzativo)**.

Il ricercatore di sicurezza **@NitekryDPaul** ha scoperto **30 prefissi OUI** costantemente associati all'hardware delle telecamere Flock Safety attraverso **l'analisi 2,4 GHz in modalità promiscua**. Un 31° prefisso (`82:6B:F2`) è stato contribuito da **Michael / DeFlockJoplin** durante i test sul campo a Joplin, MO.

Flock Finder prende questi 31 OUI, interroga WiGLE per qualsiasi rete WiFi registrata che corrisponda a questi prefissi e traccia i risultati su una mappa.

### I 31 prefissi OUI noti di Flock Safety

| # | Prefisso OUI | Fonte | # | Prefisso OUI | Fonte |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### La tecnica di rilevamento addr1

La scoperta chiave di @NitekryDPaul va oltre la semplice corrispondenza sull'indirizzo MAC del trasmettitore. Le telecamere Flock trascorrono la maggior parte del loro ciclo di lavoro **in standby**. Quando un punto di accesso vicino invia un frame indirizzato *a* una telecamera, il MAC della telecamera appare come **addr1 (l'indirizzo del ricevitore)** nei frame 802.11 — anche quando la telecamera stessa non sta trasmettendo attivamente.

Combinato con il **rilevamento di richieste probe wildcard** (frame di gestione 802.11 tipo=0, sottotipo=4, SSID vuoto), questo produce una firma di rilevamento molto precisa. I test sul campo a Joplin, MO hanno raggiunto **11 telecamere su 12 rilevate con solo 2 falsi positivi**.

> ⚠️ **Importante**: La mappa Flock Finder basata su WiGLE **non** implementa la tecnica addr1. WiGLE è un set di dati storici, raccolti passivamente — registra solo i trasmettitori, non i ricevitori. Per il rilevamento in tempo reale che utilizza effettivamente il metodo di @NitekryDPaul, hai bisogno di hardware dedicato sul campo.

______

## Utilizzo della mappa in tempo reale

La mappa interattiva è disponibile su **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Mostra:

- **Indicatori di telecamere raggruppati** codificati per colore per prefisso OUI
- **Ricerca** per città, stato o BSSID
- **Tabella dati OUI** con conteggi di telecamere per prefisso
- **Pannello statistiche** che mostra le telecamere totali, le regioni e l'ultimo timestamp di aggiornamento
- **Pagina sugli ALPR** con danni alla privacy documentati, contesto legale e risorse della comunità

Le esportazioni dei dati della mappa sono disponibili anche direttamente:

- `data/flock_cameras.geojson` — GeoJSON per l'uso in QGIS, Leaflet o altri strumenti
- `data/flock_cameras.csv` — formato compatibile con i fogli di calcolo
- `data/scan_stats.json` — statistiche e conteggi di scansione

### Limitazioni principali

**Prendi la mappa con cautela.** WiGLE è un set di dati crowd-sourced, aggiornato sporadicamente, non un feed in diretta.

- **Le telecamere Flock non trasmettono continuamente.** Si svegliano brevemente per caricare i dati, quindi i record WiGLE dipendono interamente da un wardriver nelle vicinanze esattamente nel momento giusto.
- **I dati potrebbero avere mesi o anni.** Le telecamere che sono state spostate o rimosse potrebbero ancora apparire.
- **La corrispondenza OUI è un'euristica.** Gli OUI possono essere condivisi, riassegnati o falsificati. Ogni risultato è un dispositivo Flock *presunto*, non confermato.
- **La copertura è disomogenea.** Le aree metropolitane dense hanno più dati WiGLE; le aree rurali ne hanno molto meno.

*Usa la mappa per sviluppare una consapevolezza generale della densità di sorveglianza nella tua area. Per il rilevamento in tempo reale con dati reali sul campo, consulta le opzioni hardware di seguito.*

______

## Eseguire Flock Finder da soli

### Prerequisiti

- Python 3.8+
- Un account gratuito di [WiGLE](https://wigle.net/account) con credenziali API

### Configurazione

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### Esecuzione dello scanner

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### Visualizzazione della mappa in locale

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Aggiornamenti automatici giornalieri tramite GitHub Actions

Esegui il fork del repository e aggiungi le tue credenziali WiGLE come **segreti del repository** (`WIGLE_API_NAME` e `WIGLE_API_TOKEN`). Il workflow incluso viene eseguito alle 6:00 UTC ogni giorno e salva automaticamente i file di dati aggiornati ogni volta che vengono trovate nuove telecamere.

______

## Rilevamento in tempo reale: Hardware STS Collective FlockYou

La mappa WiGLE ti dice dove le telecamere *sono state osservate*. Per il rilevamento in tempo reale mentre guidi — utilizzando il vero metodo di corrispondenza OUI di @NitekryDPaul sul traffico WiFi in diretta — hai bisogno di hardware dedicato.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** produce rilevatori portatili basati su ESP32 che scansionano le firme OUI di Flock e ti avvisano nel momento in cui viene rilevata una firma corrispondente.

### Gamma di dispositivi FlockYou

| Dispositivo | Descrizione |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Rilevatore Flock compatto, tascabile. Pre-flashato, plug-and-play. Avvisi LED al rilevamento. |
| **FlockYou Pro — LED + Audio** | Aggiunge avvisi audio accanto agli indicatori LED. Non perdere mai una telecamera mentre guidi. |
| **FlockYou Atom VoiceS3R** | Rilevatore vocale con avvisi audio parlati per un'operazione a mani libere con gli occhi sulla strada. |

Tutti i dispositivi:
- **Pre-flashati**, pronti all'uso direttamente dalla scatola
- Scansionano il traffico WiFi in diretta per tutti i 31 OUI Flock noti
- Compatti e portatili — si adattano a un portabicchieri o a una tasca
- Alimentati tramite USB-C (adattatore per auto, power bank o laptop)

> 💰 **Sconti esclusivi**: Usa il codice **FLOCKFINDER** per il **20% di sconto** su tutti i dispositivi STS Collective FlockYou — o usa il codice **SIMEONONSECURITY** per uno sconto fino al 20% sull'intero ordine. [Acquista su stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Per un'analisi tecnica completa di questi dispositivi e alternative DIY, leggi la **[Guida completa all'hardware e alla configurazione del Progetto di Rilevamento Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Struttura del progetto

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## Domande frequenti

### È legale?

Sì. **Flock Finder utilizza solo dati disponibili pubblicamente** dal database WiGLE, che aggrega dati di survey WiFi contribuiti volontariamente. Non sono coinvolti hacking, accesso non autorizzato o sistemi proprietari. Il monitoraggio passivo WiFi per le firme OUI è legale negli Stati Uniti.

### Ogni telecamera mappata è definitivamente una telecamera Flock?

No. La corrispondenza OUI è un'**euristica**. I prefissi OUI possono essere condivisi tra produttori, riassegnati o falsificati. Ogni record nel database è un dispositivo Flock *presunto* — non confermato. Leggi la [Politica sui dati](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) per dettagli su come richiedere una correzione.

### Perché alcuni prefissi OUI non mostrano telecamere?

La copertura WiGLE è disomogenea. Se nessun wardriver ha scansionato una determinata area con quello specifico OUI attivo, non ci saranno record. *L'assenza di dati non significa l'assenza di telecamere.*

### Quanto sono aggiornati i dati?

Il workflow GitHub Actions viene eseguito quotidianamente e recupera gli ultimi risultati WiGLE. Tuttavia, WiGLE stesso può avere record che vanno da giorni ad anni per qualsiasi posizione specifica. Controlla il file `scan_stats.json` per il timestamp della scansione più recente.

### Posso contribuire con i miei dati di wardrive?

Sì. Carica i tuoi dati di wardrive su [WiGLE](https://wigle.net) — vengono automaticamente inseriti nella prossima scansione giornaliera di Flock Finder. Puoi anche contribuire con prefissi OUI o miglioramenti al codice tramite la [Guida alla contribuzione](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunità e progetti correlati

Flock Finder non agisce da solo. Un ecosistema crescente di strumenti e organizzazioni lavora per documentare e contrastare la sorveglianza ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Tracciamento ALPR, documentazione e difesa guidati dalla comunità
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Controlla se la tua targa è stata cercata nel sistema Flock
- **[FlockHopper](https://flockhopper.com/)** — Pianificazione del percorso che evita le telecamere ALPR note
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Database dell'EFF sulle tecnologie di sorveglianza utilizzate dalle forze dell'ordine
- **[NoALPRs.com](https://noalprs.com/)** — Risorse per le comunità che combattono i deployment ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware open source e ricerca sul campo; ha contribuito il 31° prefisso OUI

______

## Crediti

- **Ricerca OUI**: @NitekryDPaul — tutti i 30 prefissi OUI originali e la strategia di rilevamento addr1/modalità promiscua
- **Test sul campo**: Michael / DeFlockJoplin — 31° prefisso OUI (`82:6B:F2`) e perfezionamento delle probe wildcard
- **Fonte dati**: [WiGLE](https://wigle.net) — database WiFi/rete cellulare crowd-sourced
- **Ispirato da**: [DeFlock](https://deflockjoplin.org/) e track-openroaming-passpoint
- **Partner hardware**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — rilevatori FlockYou ESP32

______

## Conclusione

**Flock Finder** dà a chiunque un'idea rapida e visiva di quanto ampiamente siano state distribuite le telecamere Flock Safety ALPR — oltre 40.000 posizioni stimate in 109 paesi, aggiornate automaticamente ogni giorno dai dati WiFi crowd-sourced.

È uno **strumento di trasparenza**, non un tracker in diretta. I suoi dati sono storici, incompleti e probabilistici. Ma rende visibile la portata della sorveglianza ALPR in un modo che i riassunti e i rapporti non possono.

Per una protezione genuina in tempo reale mentre ti muovi nelle aree sorvegliate, abbina la mappa con hardware dedicato. **[I dispositivi FlockYou di STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementano il metodo di rilevamento di @NitekryDPaul direttamente su un ESP32 e ti avvisano nel momento in cui viene rilevata una firma di telecamera in diretta — disponibili su **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** con il codice **FLOCKFINDER** o **SIMEONONSECURITY** per uno sconto fino al 20%.

### Articoli correlati

| Articolo | Cosa tratta |
|---------|---------------|
| **[Sorveglianza tramite telecamere Flock Safety: Privacy e protezione](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Il quadro completo: statistiche sulla prevalenza, questioni di libertà civili, toolkit ACLU, statistiche DeFlock, guida FOIA e strategie di protezione |
| **[Progetto di Rilevamento Flock-You: Guida all'hardware di contro-sorveglianza](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guida tecnica completa ai rilevatori Flock basati su ESP32 — OUI-SPY, M5 Atom Lite, build DIY, configurazione firmware passo dopo passo |
| **[Come flashare i dispositivi Rayhunter: Guida completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Rilevare i catcher IMSI (simulatori di stazioni cellulari) accanto alle telecamere ALPR per una piena consapevolezza della contro-sorveglianza |
| **[Firmware personalizzato DagShell per Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Trasformare un hotspot mobile in una piattaforma di ricerca sulla sicurezza — si abbina bene con l'hardware di rilevamento Flock |
| **[Confronto dei dispositivi Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Confrontare le opzioni di hardware per il rilevamento tra le categorie di minacce ALPR e di sorveglianza cellulare |

______

## Riferimenti

1. [Repository GitHub di Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Mappa interattiva di Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Dispositivi FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Mappatura delle reti wireless](https://wigle.net)
5. [DeFlock — Consapevolezza ALPR della comunità](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware di rilevamento open source](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Stai sendo tracciato](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
