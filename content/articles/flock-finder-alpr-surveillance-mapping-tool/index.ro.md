---
title: "Flock Finder: Cartografierea camerelor ALPR Flock Safety"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder este un instrument open-source care cartografiază peste 40.000 de camere ALPR Flock Safety la nivel mondial folosind datele WiFi WiGLE și amprenta OUI. Aflați cum funcționează, limitele sale și instrumentele hardware pentru detecție în timp real."
genre: ["Tehnologie pentru Confidențialitate", "Contra-Supraveghere", "Proiecte Open Source", "Drepturi Digitale", "Securitate Rețea", "Instrumente Confidențialitate", "Hardware Hacking", "Cercetare Securitate"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Cititor Numere de Înmatriculare", "Amprentare OUI", "WiGLE", "Supraveghere WiFi", "Contra-Supraveghere", "STS Collective", "FlockYou", "ESP32", "Instrumente Confidențialitate", "NitekryDPaul", "DeFlockJoplin", "Detectare ALPR", "Securitate Open Source", "Cartografiere Supraveghere", "Supraveghere în Masă", "WiFi OUI", "Protecție Confidențialitate", "Adresă MAC", "Mod Promiscuu", "802.11", "Detectare în Timp Real", "Wardriving", "Drepturi Digitale", "Libertăți Civile", "Conștientizare Supraveghere", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "O hartă interactivă care afișează marcatori colorați indicând locațiile camerelor ALPR Flock Safety, cu semnale WiFi abstracte emanând din marcatori pe un fundal întunecat."
coverCaption: "Flock Finder cartografiază peste 40.000 de camere ALPR Flock Safety suspecte folosind datele WiFi WiGLE și amprenta OUI."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Un instrument open-source de conștientizare a supravegherii care cartografiază camerele ALPR Flock Safety folosind date WiFi colectate colaborativ.**

## Ce este Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** este un proiect open-source care cartografiază **camerele ALPR (Cititor Automat de Numere de Înmatriculare) Flock Safety** din Statele Unite și alte 108 țări. Combină **31 de prefixe OUI (Identificator Unic Organizațional) WiFi Flock Safety** cunoscute cu **baza de date WiFi colectivă WiGLE** pentru a identifica și reprezenta pe o hartă interactivă locațiile suspecte ale camerelor.

Proiectul se află la **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, se actualizează automat zilnic prin GitHub Actions, și din iulie 2026 a cartografiat **peste 40.000 de camere suspecte** în 964 de regiuni din întreaga lume.

| Metric | Valoare |
|--------|---------|
| **Camere Cartografiate** | 40.026+ |
| **Prefixe OUI Cunoscute** | 31 |
| **Țări Acoperite** | 109 |
| **Regiuni Acoperite** | 964 |
| **Retenție Date** | 730 zile (2 ani) |
| **Frecvență Actualizare Automată** | Zilnic |

*Acesta este un instrument general de conștientizare, nu un inventar definitiv. Citiți secțiunea privind limitele înainte de a trage concluzii din date.*

Pentru context privind importanța supravegherii ALPR Flock Safety pentru confidențialitate, citiți **[Supravegherea cu camere Flock Safety: Prevalență, Probleme de Confidențialitate și Strategii de Protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Cum Funcționează: Amprenta OUI prin WiGLE

### Perspectiva Fundamentală

Camerele Flock Safety conțin **transceivere WiFi** care se trezesc periodic din repaus pentru a încărca datele capturate ale numerelor de înmatriculare în cloud. În aceste scurte ferestre active, camera transmite cadre WiFi ce conțin **adresa MAC** — iar primii trei octeți ai oricărei adrese MAC identifică producătorul. Acesta este **OUI (Identificatorul Unic Organizațional)**.

Cercetătorul de securitate **@NitekryDPaul** a descoperit **30 de prefixe OUI** asociate în mod constant cu hardware-ul camerelor Flock Safety prin **analiza în mod promiscuu pe 2,4 GHz**. Un al 31-lea prefix (`82:6B:F2`) a fost contribuit de **Michael / DeFlockJoplin** în timpul testelor de teren în Joplin, MO.

Flock Finder ia acele 31 de OUI-uri, interoghează WiGLE pentru orice rețele WiFi înregistrate ce corespund acelor prefixe, și reprezintă rezultatele pe o hartă.

### Cele 31 de Prefixe OUI Flock Safety Cunoscute

| # | Prefix OUI | Sursă | # | Prefix OUI | Sursă |
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

### Tehnica de Detectare addr1

Descoperirea cheie a lui @NitekryDPaul depășește simpla potrivire pe adresa MAC a transmițătorului. Camerele Flock petrec cea mai mare parte a ciclului lor de funcționare **în repaus**. Când un punct de acces din apropiere trimite un cadru adresat *la* o cameră, adresa MAC a camerei apare ca **addr1 (adresa receptorului)** în cadrele 802.11 — chiar dacă camera însăși nu transmite activ.

Combinat cu **detectarea cererilor de sondaj wildcard** (cadre de management 802.11 tip=0, subtip=4, SSID gol), aceasta produce o semnătură de detectare foarte precisă. Testele de teren din Joplin, MO au obținut **11 din 12 camere detectate cu doar 2 fals pozitive**.

> ⚠️ **Important**: Harta Flock Finder bazată pe WiGLE **nu** implementează tehnica addr1. WiGLE este un set de date istorice, colectate pasiv — înregistrează doar transmițătoarele, nu receptoarele. Pentru detectare în timp real care folosește efectiv metoda lui @NitekryDPaul, aveți nevoie de hardware dedicat care funcționează pe teren.

______

## Utilizarea Hărții Live

Harta interactivă este disponibilă la **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Afișează:

- **Marcatori de camere grupate** codificați prin culoare după prefixul OUI
- **Căutare** după oraș, stat sau BSSID
- **Tabel de date OUI** cu numărătoarea camerelor per prefix
- **Panou de statistici** care arată totalul camerelor, regiunilor și marcajul de timp al ultimei actualizări
- **Pagina despre ALPR-uri** cu daune de confidențialitate documentate, context juridic și resurse comunitare

Exporturile de date ale hărții sunt disponibile și direct:

- `data/flock_cameras.geojson` — GeoJSON pentru utilizare în QGIS, Leaflet sau alte instrumente
- `data/flock_cameras.csv` — format compatibil cu foi de calcul
- `data/scan_stats.json` — statistici și numărătoare de scanare

### Limitări Cheie

**Luați harta cu circumspecție.** WiGLE este un set de date colectate colaborativ, actualizat sporadic, nu un flux live.

- **Camerele Flock nu transmit continuu.** Se trezesc scurt pentru a încărca date, deci înregistrările WiGLE depind în întregime de un wardriver care să fie în apropiere exact în momentul potrivit.
- **Datele pot fi vechi de luni sau ani.** Camerele care au fost relocate sau îndepărtate pot apărea în continuare.
- **Potrivirea OUI este euristică.** OUI-urile pot fi partajate, reatribuite sau falsificate. Fiecare rezultat este un dispozitiv Flock *suspectat*, nu confirmat.
- **Acoperirea este neuniformă.** Zonele metropolitane dense au mai multe date WiGLE; zonele rurale au mult mai puține.

*Folosiți harta pentru a dezvolta o conștientizare generală a densității supravegherii în zona dumneavoastră. Pentru detectare în timp real bazată pe teren, consultați opțiunile hardware de mai jos.*

______

## Rularea Flock Finder pe Cont Propriu

### Cerințe Preliminare

- Python 3.8+
- Un cont [WiGLE](https://wigle.net/account) gratuit cu credențiale API

### Configurare

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

### Rularea Scanerului

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

### Vizualizarea Hărții Local

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Actualizări Zilnice Automate prin GitHub Actions

Bifurcați repo-ul și adăugați credențialele WiGLE ca **secrete de repository** (`WIGLE_API_NAME` și `WIGLE_API_TOKEN`). Fluxul de lucru inclus rulează zilnic la 6 AM UTC și comite automat fișierele de date actualizate ori de câte ori sunt găsite camere noi.

______

## Detectare în Timp Real: Hardware FlockYou de la STS Collective

Harta WiGLE vă spune unde camerele *au fost observate*. Pentru detectare în timp real în timp ce conduceți — folosind metoda actuală de potrivire OUI a lui @NitekryDPaul pe traficul WiFi live — aveți nevoie de hardware dedicat.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** produce detectoare portabile bazate pe ESP32 care scanează semnăturile OUI Flock și vă alertează în momentul în care o semnătură corespunzătoare este detectată.

### Gama de Dispozitive FlockYou

| Dispozitiv | Descriere |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Detector Flock compact, de dimensiunea buzunarului. Pre-programat, plug-and-play. Alerte LED la detectare. |
| **FlockYou Pro — LED + Audio** | Adaugă alerte audio alături de indicatoarele LED. Nu ratați nicio cameră în timp ce conduceți. |
| **FlockYou Atom VoiceS3R** | Detector cu voce activată cu alerte audio vorbite pentru operare hands-free, cu ochii pe drum. |

Toate dispozitivele:
- **Pre-programate**, gata de utilizare din cutie
- Scanează traficul WiFi live pentru toate cele 31 de OUI-uri Flock cunoscute
- Compacte și portabile — încap într-un suport de pahare sau buzunar
- Alimentate prin USB-C (adaptor auto, power bank sau laptop)

> 💰 **Reduceri Exclusive**: Folosiți codul **FLOCKFINDER** pentru **20% reducere** la toate dispozitivele FlockYou de la STS Collective — sau folosiți codul **SIMEONONSECURITY** pentru până la 20% reducere la întreaga comandă. [Cumpărați la stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Pentru o analiză tehnică completă a acestor dispozitive și alternative DIY, citiți **[Proiectul Flock-You Detection: Ghid Complet de Hardware și Configurare pentru Contra-Supraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Structura Proiectului

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

## Întrebări Frecvente

### Este legal?

Da. **Flock Finder folosește doar date disponibile public** din baza de date WiGLE, care agregă date de sondaj WiFi contribuite voluntar. Nu sunt implicate hacking, acces neautorizat sau sisteme proprietare. Monitorizarea pasivă WiFi pentru semnături OUI este legală în Statele Unite.

### Este fiecare cameră cartografiată cu certitudine o cameră Flock?

Nu. Potrivirea OUI este o **euristică**. Prefixele OUI pot fi partajate între producători, reatribuite sau falsificate. Fiecare înregistrare din baza de date este un dispozitiv Flock *suspectat* — nu unul confirmat. Citiți [Politica de Date](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) pentru detalii despre cum să solicitați o corecție.

### De ce unele prefixe OUI nu arată camere?

Acoperirea WiGLE este neuniformă. Dacă niciun wardriver nu a scanat o anumită zonă cu acel OUI specific activ, nu vor exista înregistrări. *Absența datelor nu înseamnă absența camerelor.*

### Cât de actuale sunt datele?

Fluxul de lucru GitHub Actions rulează zilnic și extrage cele mai recente rezultate WiGLE. Cu toate acestea, WiGLE poate avea înregistrări de la zile la ani pentru orice locație dată. Verificați fișierul `scan_stats.json` pentru marcajul de timp al celui mai recent scan.

### Pot contribui cu propriile date de wardrive?

Da. Încărcați datele de wardrive la [WiGLE](https://wigle.net) — acestea alimentează automat următoarea scanare zilnică a Flock Finder. Puteți contribui și cu prefixe OUI sau îmbunătățiri de cod prin [Ghidul de Contribuție](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Comunitate și Proiecte Conexe

Flock Finder nu stă singur. Un ecosistem în creștere de instrumente și organizații lucrează pentru a documenta și contracara supravegherea ALPR:

- **[DeFlock.org](https://deflockjoplin.org/)** — Urmărire ALPR, documentare și advocacy conduse de comunitate
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Verificați dacă plăcuța dvs. a fost căutată în sistemul Flock
- **[FlockHopper](https://flockhopper.com/)** — Planificarea rutelor care evită camerele ALPR cunoscute
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Baza de date a EFF despre tehnologia de supraveghere folosită de forțele de ordine
- **[NoALPRs.com](https://noalprs.com/)** — Resurse pentru comunitățile care luptă împotriva instalărilor ALPR
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Firmware open-source și cercetare de teren; a contribuit cu al 31-lea prefix OUI

______

## Credite

- **Cercetare OUI**: @NitekryDPaul — toate cele 30 de prefixe OUI originale și strategia de detectare addr1/mod-promiscuu
- **Teste de teren**: Michael / DeFlockJoplin — al 31-lea prefix OUI (`82:6B:F2`) și rafinarea sondajelor wildcard
- **Sursă de date**: [WiGLE](https://wigle.net) — baza de date colectivă WiFi/rețele celulare
- **Inspirat de**: [DeFlock](https://deflockjoplin.org/) și track-openroaming-passpoint
- **Partener hardware**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — detectoare FlockYou ESP32

______

## Concluzie

**Flock Finder** oferă oricui o imagine rapidă și vizuală a cât de larg au fost instalate camerele ALPR Flock Safety — peste 40.000 de locații estimate în 109 țări, actualizate automat în fiecare zi din datele WiFi colectate colaborativ.

Este un **instrument de transparență**, nu un tracker live. Datele sale sunt istorice, incomplete și probabilistice. Dar face vizibilă scara supravegherii ALPR într-un mod în care rezumatele și rapoartele nu pot.

Pentru protecție genuină în timp real în timp ce vă deplasați prin zone supravegheate, combinați harta cu hardware dedicat. **[Dispozitivele FlockYou de la STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** implementează metoda de detectare a lui @NitekryDPaul direct pe un ESP32 și vă alertează în momentul în care este detectată o semnătură de cameră live — disponibile la **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** cu codul **FLOCKFINDER** sau **SIMEONONSECURITY** pentru până la 20% reducere.

### Articole Conexe

| Articol | Ce acoperă |
|---------|---------------|
| **[Supravegherea cu camere Flock Safety: Confidențialitate și Protecție](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Imaginea completă: statistici de prevalență, probleme de libertăți civile, trusa ACLU, statistici DeFlock, ghid FOIA și strategii de protecție |
| **[Proiectul Flock-You Detection: Ghid Hardware de Contra-Supraveghere](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Ghid tehnic complet pentru detectoarele Flock bazate pe ESP32 — OUI-SPY, M5 Atom Lite, construcție DIY, configurare firmware pas cu pas |
| **[Cum să Programați Dispozitivele Rayhunter: Ghid Complet](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detectați interceptoarele IMSI (simulatoare de site celular) alături de camerele ALPR pentru o conștientizare completă a contra-supravegherii |
| **[Firmware Personalizat DagShell pentru Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Transformați un hotspot mobil într-o platformă de cercetare de securitate — se perechiază bine cu hardware-ul de detectare Flock |
| **[Compararea Dispozitivelor Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparați opțiunile de hardware de detectare în categoriile de amenințări de supraveghere ALPR și celulară |

______

## Referințe

1. [Repositoriu GitHub Flock Finder](https://github.com/simeononsecurity/flock-finder)
2. [Hartă Interactivă Flock Finder](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — Dispozitive FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Cartografiere Rețele Wireless](https://wigle.net)
5. [DeFlock — Conștientizare ALPR Comunitară](https://deflockjoplin.org/)
6. [DeFlockJoplin — Firmware de Detectare Open-Source](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Ești Urmărit](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
