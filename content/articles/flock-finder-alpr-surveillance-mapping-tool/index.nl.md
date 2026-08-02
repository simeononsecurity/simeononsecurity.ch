---
title: "Flock Finder: Kaart van Flock Safety ALPR-camera's"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder is een open-source tool die wereldwijd meer dan 40.000 Flock Safety ALPR-camera's in kaart brengt met behulp van WiGLE WiFi-gegevens en OUI-vingerafdrukken. Leer hoe het werkt, de beperkingen en de hardwaretools voor realtime detectie."
genre: ["Privacytechnologie", "Tegenbewaking", "Open-sourceprojecten", "Digitale rechten", "Netwerkbeveiliging", "Privacy-tools", "Hardware-hacking", "Beveiligingsonderzoek"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Kentekenplatenlezer", "OUI-vingerafdruk", "WiGLE", "WiFi-bewaking", "Tegenbewaking", "STS Collective", "FlockYou", "ESP32", "Privacy-tools", "NitekryDPaul", "DeFlockJoplin", "ALPR-detectie", "Open-source beveiliging", "Bewakingskartering", "Massabewaking", "WiFi OUI", "Privacybescherming", "MAC-adres", "Promiscuous modus", "802.11", "Realtime detectie", "Wardriving", "Digitale rechten", "Burgerrechten", "Bewakingsbewustzijn", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Een interactieve kaart met kleurrijke markeringen die de locaties van Flock Safety ALPR-camera's aangeven, met abstracte WiFi-signalen die vanuit de markeringen uitstralen op een donkere achtergrond."
coverCaption: "Flock Finder brengt meer dan 40.000 vermoedelijke Flock Safety ALPR-camera's in kaart met behulp van WiGLE WiFi-gegevens en OUI-vingerafdrukken."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Een open-source bewakingsbewustzijnstool die Flock Safety ALPR-camera's in kaart brengt met behulp van crowdsourced WiFi-gegevens.**

## Wat is Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** is een open-source project dat **Flock Safety ALPR (Automatische Kentekenplaatlezer)-camera's** in kaart brengt in de Verenigde Staten en 108 andere landen. Het combineert **31 bekende Flock Safety WiFi OUI (Organisatorisch Unieke Identifier)-prefixen** met de **WiGLE crowdsourced WiFi-database** om vermoedelijke cameralocaties te identificeren en op een interactieve kaart te plotten.

Het project bevindt zich op **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, wordt dagelijks automatisch bijgewerkt via GitHub Actions en heeft vanaf juli 2026 **meer dan 40.000 vermoedelijke camera's** in kaart gebracht in 964 regio's wereldwijd.

| Statistiek | Waarde |
|--------|-------|
| **Camera's in kaart gebracht** | 40.026+ |
| **Bekende OUI-prefixen** | 31 |
| **Landen gedekt** | 109 |
| **Regio's gedekt** | 964 |
| **Gegevensbewaring** | 730 dagen (2 jaar) |
| **Automatische updatefrequentie** | Dagelijks |

*Dit is een algemeen bewustzijnstool, geen definitieve inventarisatie. Lees de sectie over beperkingen voordat u conclusies trekt uit de gegevens.*

Voor achtergrond over waarom Flock Safety ALPR-bewaking belangrijk is voor privacy, lees **[Flock Safety-camerabewaking: prevalentie, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## Hoe het werkt: OUI-vingerafdrukken via WiGLE

### Het kernidee

Flock Safety-camera's bevatten **WiFi-transceivers** die periodiek wakker worden uit de slaap om vastgelegde kentekenplatengegevens naar de cloud te uploaden. Tijdens deze korte actieve vensters zendt de camera WiFi-frames uit die het **MAC-adres** bevatten — en de eerste drie bytes van elk MAC-adres identificeren de fabrikant. Dit is de **OUI (Organisatorisch Unieke Identifier)**.

Beveiligingsonderzoeker **@NitekryDPaul** ontdekte **30 OUI-prefixen** die consistent geassocieerd worden met Flock Safety-camerahardware via **promiscuous-mode 2,4 GHz-analyse**. Een 31e prefix (`82:6B:F2`) werd bijgedragen door **Michael / DeFlockJoplin** tijdens veldtesten in Joplin, MO.

Flock Finder neemt die 31 OUI's, vraagt WiGLE om geregistreerde WiFi-netwerken die overeenkomen met die prefixen, en plot de resultaten op een kaart.

### De 31 bekende Flock Safety OUI-prefixen

| # | OUI-prefix | Bron | # | OUI-prefix | Bron |
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

### De addr1-detectietechniek

@NitekryDPaul's belangrijkste ontdekking gaat verder dan eenvoudig overeenkomen op het MAC-adres van de zender. Flock-camera's brengen het grootste deel van hun dutycycle **slapend** door. Wanneer een nabijgelegen toegangspunt een frame stuurt *aan* een camera, verschijnt het MAC van de camera als **addr1 (het ontvangeradres)** in 802.11-frames — zelfs terwijl de camera zelf niet actief zendt.

Gecombineerd met **wildcard probe request-detectie** (802.11-beheerframes type=0, subtype=4, leeg SSID), levert dit een zeer nauwkeurige detectiehandtekening op. Veldtesten in Joplin, MO bereikten **11 van de 12 camera's gedetecteerd met slechts 2 valse positieven**.

> ⚠️ **Belangrijk**: De WiGLE-gebaseerde Flock Finder-kaart implementeert de addr1-techniek **niet**. WiGLE is een historische, passief verzamelde dataset — het registreert alleen zenders, geen ontvangers. Voor realtime detectie met de werkelijke methode van @NitekryDPaul, hebt u speciale hardware nodig die in het veld werkt.

______

## De live kaart gebruiken

De interactieve kaart is live op **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)**. Het toont:

- **Geclusterde cameramarkeringen** kleurgecodeerd per OUI-prefix
- **Zoeken** op stad, staat of BSSID
- **OUI-gegevenstabel** met cameraantallen per prefix
- **Statistiekenpaneel** met totale camera's, regio's en tijdstempel van laatste update
- **Pagina over ALPR's** met gedocumenteerde privacyschade, juridische context en gemeenschapsbronnen

De kaartdataexports zijn ook direct beschikbaar:

- `data/flock_cameras.geojson` — GeoJSON voor gebruik in QGIS, Leaflet of andere tools
- `data/flock_cameras.csv` — spreadsheetvriendelijk formaat
- `data/scan_stats.json` — scanstatistieken en -aantallen

### Belangrijkste beperkingen

**Neem de kaart met een korrel zout.** WiGLE is een crowdsourced, sporadisch bijgewerkte dataset, geen live feed.

- **Flock-camera's zenden niet continu.** Ze worden kort wakker om gegevens te uploaden, dus WiGLE-records zijn volledig afhankelijk van een wardriver die precies op het juiste moment in de buurt is.
- **Gegevens kunnen maanden of jaren oud zijn.** Camera's die zijn verplaatst of verwijderd, kunnen nog steeds verschijnen.
- **OUI-matching is een heuristiek.** OUI's kunnen worden gedeeld, opnieuw toegewezen of vervalst. Elk resultaat is een *vermoedelijk* Flock-apparaat, geen bevestigd.
- **Dekking is ongelijkmatig.** Dichte stedelijke gebieden hebben meer WiGLE-gegevens; landelijke gebieden hebben veel minder.

*Gebruik de kaart om een algemeen bewustzijn te ontwikkelen van de bewakingsdichtheid in uw omgeving. Voor realtime detectie met grondwaarheid, zie de hardwareopties hieronder.*

______

## Flock Finder zelf uitvoeren

### Vereisten

- Python 3.8+
- Een gratis [WiGLE](https://wigle.net/account)-account met API-inloggegevens

### Installatie

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

### De scanner uitvoeren

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

### De kaart lokaal bekijken

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Geautomatiseerde dagelijkse updates via GitHub Actions

Fork de repository en voeg uw WiGLE-inloggegevens toe als **repository-secrets** (`WIGLE_API_NAME` en `WIGLE_API_TOKEN`). De meegeleverde workflow wordt dagelijks om 6:00 uur UTC uitgevoerd en commit automatisch bijgewerkte gegevensbestanden wanneer nieuwe camera's worden gevonden.

______

## Realtime detectie: STS Collective FlockYou-hardware

De WiGLE-kaart vertelt u waar camera's *zijn waargenomen*. Voor realtime detectie terwijl u rijdt — met de werkelijke OUI-overeenkomstmethode van @NitekryDPaul op live WiFi-verkeer — heeft u speciale hardware nodig.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** maakt draagbare ESP32-gebaseerde detectoren die scannen op Flock OUI-handtekeningen en u waarschuwen op het moment dat een overeenkomende handtekening wordt gedetecteerd.

### FlockYou-apparaatlijn

| Apparaat | Beschrijving |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Compacte, zakformaat Flock-detector. Voorgeflasht, plug-and-play. LED-waarschuwingen bij detectie. |
| **FlockYou Pro — LED + Audio** | Voegt audiosignalen toe naast LED-indicatoren. Mis nooit een camera tijdens het rijden. |
| **FlockYou Atom VoiceS3R** | Stemgestuurde detector met gesproken audiowaarschuwingen voor handsfree bediening met ogen op de weg. |

Alle apparaten:
- **Voorgeflasht**, klaar voor gebruik uit de doos
- Scannen live WiFi-verkeer op alle 31 bekende Flock OUI's
- Compact en draagbaar — past in een bekerhouder of zak
- Gevoed via USB-C (autoadapter, powerbank of laptop)

> 💰 **Exclusieve kortingen**: Gebruik code **FLOCKFINDER** voor **20% korting** op alle STS Collective FlockYou-apparaten — of gebruik code **SIMEONONSECURITY** voor tot 20% korting op uw hele bestelling. [Winkel bij stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Voor een volledig technische analyse van deze apparaten en DIY-alternatieven, lees de **[Flock-You Detectieproject: Complete handleiding voor tegenbewakingshardware en configuratie](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Projectstructuur

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

## Veelgestelde vragen

### Is dit legaal?

Ja. **Flock Finder gebruikt alleen openbaar beschikbare gegevens** uit de WiGLE-database, die vrijwillig bijgedragen WiFi-surveygegevens aggregeert. Er is geen hacking, ongeautoriseerde toegang of eigendomssystemen betrokken. Passieve WiFi-monitoring voor OUI-handtekeningen is legaal in de Verenigde Staten.

### Is elke in kaart gebrachte camera zeker een Flock-camera?

Nee. OUI-matching is een **heuristiek**. OUI-prefixen kunnen worden gedeeld tussen fabrikanten, opnieuw worden toegewezen of worden vervalst. Elk record in de database is een *vermoedelijk* Flock-apparaat — geen bevestigd. Lees het [Gegevensbeleid](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) voor details over hoe u een correctie kunt aanvragen.

### Waarom tonen sommige OUI-prefixen geen camera's?

WiGLE-dekking is ongelijkmatig. Als geen wardriver een bepaald gebied heeft gescand met die specifieke actieve OUI, zijn er geen records. *Afwezigheid van gegevens betekent niet afwezigheid van camera's.*

### Hoe actueel zijn de gegevens?

De GitHub Actions-workflow wordt dagelijks uitgevoerd en haalt de nieuwste WiGLE-resultaten op. WiGLE zelf kan echter records bevatten die variëren van dagen tot jaren oud voor elke locatie. Controleer het `scan_stats.json`-bestand voor de tijdstempel van de meest recente scan.

### Kan ik mijn eigen wardrive-gegevens bijdragen?

Ja. Upload uw wardrive-gegevens naar [WiGLE](https://wigle.net) — het vloeit automatisch door naar de volgende dagelijkse scan van Flock Finder. U kunt ook OUI-prefixen of codeverbeteringen bijdragen via de [Bijdragegids](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md).

______

## Community en gerelateerde projecten

Flock Finder staat niet alleen. Een groeiend ecosysteem van tools en organisaties werkt aan het documenteren en bestrijden van ALPR-bewaking:

- **[DeFlock.org](https://deflockjoplin.org/)** — Gemeenschapsgedreven ALPR-tracking, documentatie en belangenbehartiging
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Controleer of uw kenteken is gezocht in het systeem van Flock
- **[FlockHopper](https://flockhopper.com/)** — Routeplanning die bekende ALPR-camera's vermijdt
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — EFF's database van bewakingstechnologie gebruikt door wetshandhaving
- **[NoALPRs.com](https://noalprs.com/)** — Bronnen voor gemeenschappen die strijden tegen ALPR-implementaties
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Open-source firmware en veldonderzoek; heeft het 31e OUI-prefix bijgedragen

______

## Credits

- **OUI-onderzoek**: @NitekryDPaul — alle 30 originele OUI-prefixen en de addr1/promiscuous-mode detectiestrategie
- **Veldtesten**: Michael / DeFlockJoplin — 31e OUI-prefix (`82:6B:F2`) en wildcard probe-aanscherping
- **Gegevensbron**: [WiGLE](https://wigle.net) — crowdsourced WiFi/mobiel netwerkdatabase
- **Geïnspireerd door**: [DeFlock](https://deflockjoplin.org/) en track-openroaming-passpoint
- **Hardwarepartner**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32-detectoren

______

## Conclusie

**Flock Finder** geeft iedereen een snel, visueel beeld van hoe breed Flock Safety ALPR-camera's zijn uitgerold — meer dan 40.000 geschatte locaties in 109 landen, dagelijks automatisch bijgewerkt vanuit crowdsourced WiFi-gegevens.

Het is een **transparantietool**, geen live tracker. De gegevens zijn historisch, onvolledig en probabilistisch. Maar het maakt de schaal van ALPR-bewaking zichtbaar op een manier die samenvattingen en rapporten niet kunnen.

Voor echte realtime bescherming terwijl u door bewakte gebieden beweegt, combineer de kaart met speciale hardware. **[STS Collective's FlockYou-apparaten](https://stscollective.com/discount/SIMEONONSECURITY)** implementeren de detectiemethode van @NitekryDPaul direct op een ESP32 en waarschuwen u op het moment dat een live camerahandtekening wordt gedetecteerd — beschikbaar op **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** met code **FLOCKFINDER** of **SIMEONONSECURITY** voor tot 20% korting.

### Gerelateerde artikelen

| Artikel | Wat het behandelt |
|---------|---------------|
| **[Flock Safety-camerabewaking: privacy en bescherming](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Het volledige beeld: prevalentiestatistieken, burgerrechtenkwesties, ACLU-toolkit, DeFlock-statistieken, FOIA-gids en beschermingsstrategieën |
| **[Flock-You Detectieproject: Handleiding voor tegenbewakingshardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Volledige technische handleiding voor ESP32-gebaseerde Flock-detectoren — OUI-SPY, M5 Atom Lite, DIY-bouw, stapsgewijze firmware-installatie |
| **[Hoe Rayhunter-apparaten te flashen: Volledige handleiding](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | IMSI-catchers (celsite-simulatoren) detecteren naast ALPR-camera's voor volledig tegenbewakingsbewustzijn |
| **[DagShell aangepaste firmware voor Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Een mobiele hotspot omzetten in een beveiligingsonderzoeksplatform — past goed bij Flock-detectiehardware |
| **[Rayhunter-apparaatvergelijking 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Detectiehardwareopties vergelijken over ALPR- en cellulaire bewakingsdreigingscategorieën |

______

## Referenties

1. [Flock Finder GitHub-repository](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finder interactieve kaart](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYou-apparaten](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Draadloze netwerkkaartering](https://wigle.net)
5. [DeFlock — Gemeenschaps-ALPR-bewustzijn](https://deflockjoplin.org/)
6. [DeFlockJoplin — Open-source detectiefirmware](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — U wordt gevolgd](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
