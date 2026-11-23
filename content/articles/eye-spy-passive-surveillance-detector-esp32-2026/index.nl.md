---
title: "Eye Spy: passieve bewakings- en trackerdetectie met ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Technische referentie voor Eye Spy v1.1, een passieve ESP32-detector voor BLE en WiFi die camera's, trackers, drones en verwante signalen opspoort."
genre: ["Privacyhulpmiddelen", "Tegenbewaking", "IoT-beveiliging", "Ingebedde systemen", "Beveiligingsonderzoek", "WiFi-beveiliging", "Bluetooth-beveiliging", "ESP32-projecten", "Hardwarebeveiliging", "Open-sourcebeveiliging"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Bewakingsdetectie", "Tegenbewaking", "BLE-detectie", "WiFi-scannen", "AirTag-detectie", "ALPR-detectie", "Flock Safety", "Detectie van bodycams", "Dronedetectie", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open source beveiliging", "Privacy", "Passieve BLE", "Monitor-modus", "OUI-detectie", "Trackerdetectie", "Axon-bodycam", "Ray-Ban Meta", "Samsung SmartTag", "Tile-tracker", "Verborgen camera", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Illustratie van een kleine M5Stack Atom Lite met kleurrijke signaalgolven eromheen tegen een diep marineblauwe achtergrond, als voorstelling van detectie van bewaking via Bluetooth en WiFi."
coverCaption: ""
---

**Een passieve sensor ter grootte van een duim die aangeeft wanneer iets meekijkt**

## Inleiding: het bewakingslandschap dat u niet ziet

De fysieke wereld wordt steeds vaker uitgerust met apparaten die meekijken, opnemen en volgen. Denk aan kentekencamera's op straathoeken, bodycams bij de politie, camera's in huurwoningen, commerciële AirTag-achtige trackers in tassen of auto's en bewakingscamera's bij iedere winkelingang. De meeste van deze apparaten communiceren draadloos via **Bluetooth LE** of **WiFi**, en *de meeste van die communicatie wordt openlijk uitgezonden, zodat iedereen met de juiste ontvanger het signaal kan detecteren*.

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) is een hulpmiddel voor passieve detectie van bewaking dat precies dit gegeven benut. Eye Spy draait op de **M5Stack Atom Lite**, een ontwikkelbord met ESP32-PICO-D4 ter grootte van ongeveer een suikerklontje, en bewaakt voortdurend de BLE- en WiFi-frequentiebanden op elektronische kenmerken van opnameapparatuur, bewakingscamera's, **ALPR**-systemen (automatic license plate reader), drones en persoonlijke trackers. Zodra het iets vindt, verandert de RGB-led van kleur.

*Het maakt nergens verbinding mee en zendt niets uit.* Het luistert, kent scores toe en licht op.

Dit artikel is een volledige technische referentie: wat Eye Spy detecteert, hoe het betrouwbaarheidsscoresysteem werkt, hoe de detectie-engines zijn gebouwd, hoe u het apparaat bouwt en programmeert en welke praktische beperkingen het heeft.

**Wilt u er liever zelf geen bouwen?** Voorgeprogrammeerde, gebruiksklare **[Eye Spy-detectieapparaten](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** zijn verkrijgbaar bij STS Collective. Met de code **SIMEONONSECURITY** krijgt u tot 20% korting.

{{< stscollective-ad "eyespy" >}}

---

## Led-indicatoren: de volledige gebruikersinterface

Net als de [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) geeft Eye Spy alle uitvoer weer via één SK6812 RGB NeoPixel op GPIO 27 van de M5Stack Atom Lite. De led toont voortdurend een dreigingsniveau met vier toestanden:

| Kleur | Betekenis | Scorebereik |
|-------|-----------|-------------|
| 🔵 Blauwe puls | Opstarten / eerste scan | -- |
| 🟢 Continu groen | Vrij, niets gedetecteerd | 0–2 |
| 🟡 Continu geel | Let op, mogelijk opnameapparaat in de buurt | 3–5 |
| 🔴 Knipperend rood | Alarm, bewakings- of trackingapparaat gedetecteerd | 6+ |

**Eén detectie met hoge betrouwbaarheid, zoals een Axon-bodycam, Flock Safety-camera, overeenkomstige ALPR-OUI of AirTag, levert genoeg punten op om de led tijdens één detectiecyclus meteen rood te laten worden.** Meerdere detecties met gemiddelde betrouwbaarheid stapelen op tot geel en kunnen samen rood opleveren.

---

## Hardware

### Primair doelapparaat: M5Stack Atom Lite

| Onderdeel | Gegevens |
|-----------|----------|
| Bord | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| Led | SK6812 NeoPixel op GPIO 27 |
| Knop | GPIO 39 (alleen invoer) |
| Flashgeheugen | 4 MB |

De Atom Lite is een compleet zelfstandig platform. **Geen soldeerwerk, breadboard of externe onderdelen nodig.** Sluit hem aan op USB en hij werkt.

### Generieke ESP32 DevKit

Een tweede PlatformIO-bouwomgeving (`esp32dev`) is bedoeld voor elke standaard ESP32 DevKit met een ingebouwde led op GPIO 2. Alle detectielogica werkt hetzelfde. De DevKit-versie is geschikt voor ontwikkeling, het testen van detectielogica en gebruik wanneer de compacte vorm van de Atom Lite niet nodig is.

---

## Het scoresysteem

Eye Spy gebruikt een **betrouwbaarheidsscoremodel** dat signalen van alle detectie-engines samenvoegt tot één geheel getal. De score bepaalt de ledstatus (groen, geel of rood) en wordt automatisch op twee manieren beheerd:

### Scoreverval

Zonder nieuwe detecties daalt de score **iedere 60 seconden met 1 punt**. Loopt u weg van een gedetecteerd apparaat, dan wordt de led binnen enkele minuten weer groen, zonder dat u iets hoeft te doen.

### Afkoelperiode voor nieuwe scores

Voor ieder detectie *type* geldt een **afkoelperiode van 120 seconden** voordat hetzelfde type vanaf dezelfde bron opnieuw punten kan opleveren. *Zo kan één aanhoudend apparaat de score niet onbeperkt opstapelen.* Een Flock Safety-camera die binnen bereik blijft, levert één keer +5 op en kan pas na 120 seconden opnieuw bijdragen.

Deze twee mechanismen betekenen samen:

- **Kortstondige detecties**, zoals een auto met AirTag die voorbijrijdt, verdwijnen vanzelf.
- **Aanhoudende bewaking**, zoals een vaste inzet van bodycams, houdt de led op alarm zolang u binnen bereik blijft.
- **Geen onbeperkt oplopende score** door herhaalde detectie van één apparaat.

---

## Detectie-engines

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagram van Eye Spy's parallelle BLE- en WiFi-detectie-engines die naar AirTags, bodycams, ALPR-systemen en drones zoeken en signalen doorgeven aan het dreigingsmodel met betrouwbaarheidsscores" >}}

Eye Spy doorloopt voortdurend drie verschillende scanfasen:

**Passieve BLE (9 s) → WiFi-scan (~3 s) → promiscuous sniffing (5 s) → herhalen**

BLE wordt uitdrukkelijk gestopt voordat WiFi-bewerkingen beginnen, zodat de gedeelde ESP32-radio niet conflicteert. Aan het begin van iedere cyclus start BLE opnieuw.

---

### Detectie-engine 1: BLE, passief scannen

BLE-scanning gebruikt **NimBLE zonder scanverzoeken uit te zenden**. Het apparaat luistert naar BLE-reclamepakketten zonder een antwoord te sturen. *Daardoor blijft Eye Spy elektronisch onzichtbaar voor de apparatuur waarnaar het zoekt.* Een passieve scanner is voor het doelapparaat niet te detecteren.

Signalen zwakker dan **−90 dBm** worden genegeerd om het aantal fout-positieven in drukke omgevingen te beperken.

#### BLE-detectietabel

| # | Doel | Detectiemethode | Punten |
|---|------|-----------------|-------|
| 1 | **Axon-bodycam** | BLE MAC OUI `00:25:df` (Axon, bodycams, tasers en politieapparatuur) | +5 🔴 |
| 2 | **Ray-Ban Meta-smartbril** | BLE-service-UUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | BLE-apparaatnaam bevat `Flock`, `Penguin`, `Pigvision` of `FS Ext Battery` | +5 🔴 |
| 4 | **Kaartskimmer (HC-03/05/06)** | Exacte overeenkomst met BLE-apparaatnaam, vaak gebruikte Bluetooth-modules in skimmers op betaalterminals | +5 🔴 |
| 5 | **Apple AirTag** | Fabrikantgegevens subtype `0x12`/`0x1E` van `0x004C`, of onbewerkte payload `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drone (OpenDroneID BLE)** | BLE-service-UUID `0xFFFA`, of ruwe AD-service-datapayload met appcode `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | BLE-service-UUID `0xFD5A` | +3 🟡 |
| 8 | **Tile-tracker** | BLE-service-UUID `0xFEED` of `0xFEEC` | +3 🟡 |
| 9 | **MeshCore-node** | BLE-apparaatnaam met prefix `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (tracking in winkels of locaties)** | Fabrikantgegevens `0x004C 0x02 0x15`, gebruikt in winkels, luchthavens en stadions om beweging te volgen | +2 🟡 |
| 11 | **Onbekend, aanhoudend apparaat** | Iedere niet-geclassificeerde BLE-MAC die ≥3× in ≥5 minuten wordt gezien (detectie van verkenner of volger) | +2 🟡 |

#### Diepere bespreking van opvallende BLE-detecties

**Axon-bodycam (+5)**: Axon (voorheen TASER International) maakt de meest gebruikte bodycamsystemen voor wetshandhaving in de Verenigde Staten. De OUI `00:25:df` staat op naam van Axon en komt voor in draagbare apparatuur van het bedrijf. **Eén detectie brengt de score meteen op de alarmdrempel.**

**Ray-Ban Meta-smartbril (+5)**: De samenwerking tussen Ray-Ban en Meta levert slimme consumentenbrillen op die video en foto's kunnen opnemen. De BLE-service-UUID `0xFD5F` is de kenmerkende advertentie die deze apparaten gebruiken. *Dit is een consumentenproduct dat op drukke openbare plekken kan voorkomen.* Een detectie met deze score verdient aandacht, ongeacht de bedoeling van de drager.

**Bluetooth-modules in kaartskimmers (+5)**: HC-03, HC-05 en HC-06 zijn goedkope Bluetooth-seriële modules die regelmatig worden aangetroffen in overlays op betaalterminals en in ATM-skimmers. De detectie vergelijkt de exacte apparaatnaam met bekende standaardnamen van de firmware van deze modules. **Een rood alarm is hier aanleiding om betaalterminals in de buurt meteen fysiek te inspecteren.**

**Apple AirTag (+4)**: AirTags zenden berichten uit met Apples eigen protocol **Nearby Interaction**. De detectie zoekt naar de apparaatspecifieke fabrikantheader (`0x004C` = Apple) en de AirTag-subtypen (`0x12` voor de standaardadvertentie, `0x1E` voor een advertentie van een verloren voorwerp). Patronen in de onbewerkte payload bieden een tweede detectiemogelijkheid.

**OpenDroneID via BLE (+4)**: De standaard **ASTM F3411 Remote ID**, die de FAA ook voor commerciële drones in de VS heeft overgenomen, definieert een uitzendprotocol waarmee drones hun identiteit en positie bekendmaken. Eye Spy zoekt naar GATT-service-UUID `0xFFFA`, de toegewezen Remote ID-service, en naar appcode `0x0D` in AD-service-datapayloads. *Iedere conforme commerciële drone in de buurt activeert deze detectie.*

**Onbekend, aanhoudend apparaat (+2)**: Dit is de engine voor **detectie van volgers**. Eye Spy houdt iedere BLE-MAC bij die niet onder de specifieke detecties hierboven valt. Verschijnt dezelfde niet-geclassificeerde MAC binnen vijf minuten drie keer of vaker, dan levert die punten op. De volgertracker kan maximaal 50 onbekende MAC-adressen tegelijk volgen en verwijdert vermeldingen nadat ze 30 minuten niet zijn gezien. **Zo worden aangepaste of gewijzigde trackers gevonden die geen bekende service-UUID of fabrikantpatroon gebruiken.**

**iBeacon (+2)**: Winkels, luchthavens en stadions gebruiken Apples iBeacon-formaat (`0x4C 0x00 0x02 0x15`) om beweging door fysieke ruimtes te volgen. De detectie herkent het standaardadvertentieformaat, ongeacht de UUID. Ze richt zich op het soort inzet, niet op een specifieke UUID. *Een treffer betekent waarschijnlijk dat u op een locatie bent waar de aanwezigheid van Bluetooth-apparaten actief wordt gevolgd.*

---

### Detectie-engine 2: WiFi-scan, actieve kanaalscan

De WiFi-scanengine gebruikt de standaard AP-scaninterface van de ESP32 om toegangspunten in de buurt op te sommen. Vervolgens vergelijkt de engine hun BSSID's en SSID's met bekende kenmerken van bewakingsapparatuur.

#### Detectietabel voor WiFi-scans

| # | Doel | Detectiemethode | Punten |
|---|------|-----------------|-------|
| 12 | **Flock Safety-camera (OUI)** | BSSID komt overeen met een tabel van 22 Flock Safety-OUI's (`d4:bb:e6`, `3c:61:05`, FS-Ext-Battery-prefixen) | +5 🔴 |
| 13 | **ALPR-/LPR-camera (OUI)** | BSSID komt overeen met Motorola Solutions / Vigilant Solutions OUI `00:0e:58` | +5 🔴 |
| 14 | **SSID met Flock-trefwoord** | SSID bevat `flock`, `flocksafety`, `fs ext`, `penguin` of `pigvision` | +5 🔴 |
| 15 | **SSID met ALPR-trefwoord** | SSID bevat `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` of `automate` | +4 🔴 |
| 16 | **Bewakingscamerafabrikant (OUI)** | BSSID komt overeen met een tabel van 31 camera-OUI's: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix en Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID met camerawoord** | SSID bevat onder meer `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` en `genetec` | +2 🟡 |

#### De Flock Safety-OUI-tabel

De tabel `FLOCK_OUIS` met 22 vermeldingen is de meest gedetailleerde opzoeklijst in het project. De tabel bevat:

- `d4:bb:e6`, een IEEE-geregistreerde Flock Safety-OUI
- `3c:61:05`, een IEEE-geregistreerde Flock Safety-OUI
- 20 andere MAC-prefixen die in het veld zijn waargenomen op Flock FS-Ext-Battery- en Flock-WiFi-cameraapparatuur

Deze 22 vermeldingen vertegenwoordigen MAC-adresbereiken van hardware die is waargenomen op gebruikte Flock Safety-ALPR-camerasystemen. **Detectie via OUI is onafhankelijk van de SSID.** Een Flock-camera met een SSID zonder trefwoord krijgt nog steeds +5 als de OUI van de BSSID overeenkomt.

De OUI's van Flock Safety en Vigilant Solutions staan bewust in aparte tabellen, zodat beide onafhankelijk punten kunnen opleveren tijdens dezelfde scanronde. *Een locatie met beide soorten leveranciers kan tijdens één WiFi-scan +10 punten opleveren.*

#### OUI-tabel voor fabrikanten van bewakingscamera's

De tabel met 31 camera-OUI's omvat grote fabrikanten van IP-camera's waarvan de hardware waarschijnlijk voorkomt in bewakingsinstallaties voor winkels, bedrijven en woningen:

- **Zakelijk en commercieel**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix, Genetec
- **Consumenten en kleine kantoren**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex, Amcrest
- **Infrastructuur**: Ubiquiti UniFi (toegangspunten en camera's delen OUI-bereiken), FLIR

Een overeenkomst levert +3 op, het niveau Let op, zonder bevestiging via een trefwoord. In combinatie met een SSID-trefwoord levert hetzelfde cameranetwerk eerst +5 op voor de OUI en daarna nog +2 voor de SSID. Zo bereikt het in één scanronde het alarmniveau.

---

### Detectie-engine 3: WiFi-monitorstand, passief frames sniffen

De promiscuous-engine zet de ESP32-radio in **monitormodus** en legt ruwe 802.11-beheerframes vast. Zo kan Eye Spy apparaten detecteren die geen SSID uitzenden, met name drones die het protocol **Remote ID** via **WiFi Neighbor Awareness Networking (NaN)** gebruiken.

Tijdens deze fase **wisselt de radio iedere 400 ms van kanaal** binnen `{1, 6, 11, 3, 8, 13}`. Zo wordt de dekking van de NaN-uitzendkanalen van drones zo groot mogelijk.

#### Detectietabel voor promiscuousmodus

| # | Doel | Detectiemethode | Punten |
|---|------|-----------------|-------|
| 18 | **Drone (OpenDroneID WiFi NaN)** | 802.11-beheerframe naar bestemmingsadres `51:6f:9a:01:00:00`, een ASTM F3411 Remote ID-uitzending | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: De ASTM F3411-standaard wijst bestemmingsadres `51:6f:9a:01:00:00` toe aan alle Remote ID-WiFi-NaN-frames. Iedere commercieel gereguleerde drone die via WiFi positie en identiteit uitzendt, verstuurt frames naar dit adres. Eye Spy let op beheerframes die aan dit multicast-MAC-adres zijn gericht. Dat gebeurt passief en betrouwbaar en is *door de dronebestuurder niet te verhelpen zonder Remote ID volledig uit te schakelen, wat zelf een overtreding van de regelgeving zou zijn*.

Deze detectie vult de BLE-OpenDroneID-engine aan (detectie #6). *Een drone kan via BLE, WiFi of beide uitzenden, afhankelijk van de hardware en configuratie.* Eye Spy ondersteunt beide.

---

## Fasering en radiobeheer

```
BLE passive (9 s) → WiFi scan (~3 s) → Promiscuous sniff (5 s) → repeat
```

De ESP32-PICO-D4 heeft één **gedeelde 2,4GHz-radio** voor BLE en WiFi. Eye Spy beheert het gebruik daarvan zorgvuldig:

1. **BLE-fase** (9 seconden): NimBLE actief, passieve scan loopt, er worden geen scanverzoeken uitgezonden
2. **BLE uitschakelen**: de BLE-stack wordt gestopt voordat WiFi wordt gestart
3. **WiFi-scan** (~3 seconden): actieve AP-scan op alle kanalen, met OUI- en SSID-controle
4. **Promiscuous sniffing** (5 seconden): passieve vastlegging van 802.11-frames, met wisseling van kanaal
5. **WiFi uitschakelen**: WiFi stopt en BLE start opnieuw voor de volgende cyclus

Deze expliciete fasering voorkomt radioconflicten. Zo krijgen zowel de BLE- als de WiFi-engine tijdens iedere cyclus ongehinderd toegang tot de radio.

---

## Seriële uitvoer

Alle uitvoer begint met `[eyespy]`, zodat u deze eenvoudig kunt filteren. De seriële monitor werkt op **115200 baud**.

### Opstarten

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Normale cyclus

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Detectiegebeurtenissen

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

Het veld `tracked=N` toont hoeveel verschillende BLE-MAC-adressen op dat moment in de persistentietracker staan. Dit helpt de BLE-apparaatdichtheid in de omgeving te begrijpen.

### Scorevelden

Elke statusregel bevat:
- **score**: de huidige dreigingsscore
- **state**: `CLEAR` / `CAUTION` / `ALERT`
- **phase**: de actieve engine (`BLE` / `WIFI` / `PROMISC`)
- **tracked**: aantal unieke BLE-MAC-adressen in de persistentietabel

---

## Bouwen en flashen

### Vereisten

- **PlatformIO** (CLI of VS Code-extensie)
- **M5Stack Atom Lite** of een ESP32 DevKit
- USB-C-kabel

### Afhankelijkheden

PlatformIO installeert deze automatisch:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** stuurt de SK6812 RGB-led aan. **NimBLE-Arduino** levert de passieve BLE-scanstack. Deze heeft de voorkeur boven de standaard ESP32-BLE-bibliotheek omdat de stack de passieve scanmodus correct ondersteunt, geen scanverzoekpakketten verstuurt en minder geheugen gebruikt.

### Flashen naar M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Bouwen en flashen voor Atom Lite
pio run -e atom-lite -t upload

# Seriële monitor op 115200 baud
pio device monitor -b 115200
```

### Flashen naar een generieke ESP32 DevKit

```bash
pio run -e esp32dev -t upload
```

### Projectstructuur

```
eye-spy/
├── src/
│   └── main.cpp          # Alle firmwarelogica
├── platformio.ini         # Bouwomgevingen (atom-lite, esp32dev)
├── partitions_4mb.csv     # Flash-partitietabel van 4 MB
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

*De omgeving `atom-lite` gebruikt de boarddefinitie `m5stick-c`.* Deze heeft dezelfde ESP32-PICO-D4-chip en een compatibele pinaansluiting voor de GPIO 27 NeoPixel.

---

## Detectienotities en praktische beperkingen

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Illustratie in fotostijl van het Eye Spy-apparaat met M5Stack Atom Lite, ongeveer zo groot als een suikerklontje en tussen twee vingers gehouden om het compacte formaat te laten zien" >}}

### Wat Eye Spy niet kan

**WiFi op 5 GHz**: De ESP32 werkt uitsluitend op **2,4 GHz**. Bewakingscamera's, ALPR-systemen en toegangspunten die alleen de 5GHz-band gebruiken, zijn niet zichtbaar voor de WiFi-scan- of promiscuous-engine. *Veel moderne IP-camera's ondersteunen ook 2,4 GHz, maar installaties die alleen 5 GHz gebruiken worden gemist.*

**Versleutelde BLE**: Enkele hoogwaardige bewakingsproducten versleutelen of verhullen hun BLE-advertenties. Eye Spy detecteert apparaten die herkenbare kenmerken onversleuteld uitzenden, zoals OUI's, service-UUID's en fabrikantgegevens. *Apparaten die hun MAC-adres wisselen, een privacyfunctie die steeds vaker voorkomt in consumententrackers, ontlopen detectie op basis van MAC.* De persistentietracker vindt ze mogelijk alleen wanneer ze minder vaak dan eens per vijf minuten wisselen.

**Bekabelde camera's**: **IP-camera's die via Ethernet zijn aangesloten en geen WiFi-radio gebruiken, zenden geen draadloze signalen uit die Eye Spy kan detecteren.** Verborgen camera's zonder netwerkverbinding die alleen lokaal opnemen, zenden evenmin een RF-signaal uit.

**Beperkt bereik**: Binnen heeft de ESP32-antenne voor sterke signalen een praktisch ontvangstbereik van **20–40 meter**. Voor zwakke of afgeschermde signalen is dat minder. *Apparaten aan de rand van het bereik of achter sterke RF-afscherming kunnen nul punten krijgen of de RSSI-filterdrempel van −90 dBm niet halen.*

### Verwachte fout-positieven

**Consumentencamera's bij buren**: Ring-, Nest-, Wyze-, Arlo- en Reolink-camera's komen veel voor in woonwijken. Hun OUI's staan in de cameratabel met 31 vermeldingen. *Verwacht in woongebieden enkele gele treffers (Let op, +3) van deurbelcamera's van buren.* Technisch gezien zijn dit geen fout-positieven, want *Eye Spy detecteert inderdaad een camera*. De context is van belang.

**iBeacon-installaties in winkels**: Grote winkelketens gebruiken iBeacon-apparatuur in bijna al hun winkels. *Een bezoek aan een winkelcentrum of supermarkt activeert waarschijnlijk de iBeacon-detectie (+2).* Ook hier werkt het apparaat zoals bedoeld. De trackinginfrastructuur van de winkel is er daadwerkelijk.

**Ubiquiti UniFi-infrastructuur**: UniFi-toegangspunten staan in de OUI-tabel voor bewakingscamera's omdat Ubiquiti zowel netwerkapparatuur als beveiligingscamera's maakt met overlappende OUI-bereiken. *Een installatie met UniFi-netwerkapparatuur krijgt +3 bij een OUI-treffer van de WiFi-scanengine.*

**Samsung SmartTag tegenover consumentenapparatuur**: De UUID van de SmartTag (`0xFD5A`) hoort bij een Samsung-geregistreerde service. *Samsung SmartTags zijn consumententrackers met een legitiem persoonlijk gebruik.* Een eigenaar van een Samsung SmartTag in de buurt activeert deze detectie.

### Wat iedere score in de praktijk betekent

| Punten | Waarschijnlijke praktijksituatie |
|-------|----------------------------------|
| 6–10 (🔴) | Geloofwaardige detectie met hoge betrouwbaarheid: Axon-camera binnen ongeveer 30 m, Flock Safety-camera met overeenkomende OUI, bevestigde AirTag-volgdetectie of drone met Remote ID-uitzending |
| 3–5 (🟡) | Meerdere consumententrackers, meerdere camera's van buren, mogelijke Flock-camera of één OpenDroneID-detectie |
| 0–2 (🟢) | Geen belangrijke bewakingskenmerken gedetecteerd; normale signalen van consumentenapparaten blijven onder de drempel |

---

## Vergelijking met verwante projecten

Eye Spy detecteert fysieke bewaking in de omgeving. De [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) richt zich op WiFi-aanvallen op netwerkniveau tegen uw eigen apparaten. *De tools vullen elkaar aan en behandelen verschillende dreigingsmodellen.*

| Mogelijkheid | Eye Spy | ESP32 WiFi Canary |
|-------------|---------|-------------------|
| AirTag- en trackerdetectie | ✅ | ❌ |
| Detectie van ALPR- en Flock-camera's | ✅ | ❌ |
| Detectie van bodycams | ✅ | ❌ |
| Detectie van drones (Remote ID) | ✅ | ❌ |
| Detectie van rogue accesspoints | ❌ | ✅ |
| Detectie van deauth-aanvallen | ❌ | ✅ |
| Detectie van downgrade-aanvallen | ❌ | ✅ |
| Leren van een basislijn | ❌ | ✅ |
| Passieve BLE | ✅ | ❌ |
| Hetzelfde hardwareplatform | ✅ | ✅ |

Beide projecten draaien op dezelfde M5Stack Atom Lite, met dezelfde led-indicatoren en hetzelfde PlatformIO-bouwsysteem. Voor uitgebreide bewustwording van fysieke én netwerkbewaking kunt u beide op verschillende Atom Lite-apparaten flashen en tegelijk meenemen.

Eye Spy vormt ook een aanvulling op het [Flock You-detectieproject](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) voor mensen die zich vooral zorgen maken over bewakingsinfrastructuur met ALPR.

---

## Toepassingen

### Bewustwording van tegenbewaking

Eye Spy is bedoeld voor iedereen die in de directe omgeving wil weten welke bewakingsinfrastructuur aanwezig is. Tijdens een wandeling door een buurt, het passeren van een kruispunt of een openbaar evenement geeft Eye Spy een realtime signaal. Het vat complexe RF-analyse samen in **één ledstatus**.

### Detectie van stalking met AirTags

Stalking met AirTags is een gedocumenteerd probleem. De **volgerdetectie-engine** van Eye Spy, die een onbekende, aanhoudende BLE-MAC detecteert na ≥3 waarnemingen in ≥5 minuten, richt zich op aangepaste of zelfgemaakte trackers die niet overeenkomen met het bekende advertentieformaat van Apple. Samen met de directe AirTag-detectie biedt dit **twee onafhankelijke manieren om een tracker te vinden die u volgt**.

### Inspectie van een huurwoning of hotelkamer

Wanneer u een nieuwe hotelkamer of huurwoning binnengaat terwijl Eye Spy actief is, krijgt u een eerste aanwijzing over onverwachte apparaten die via BLE of WiFi uitzenden. Een SSID met een camerawoord of een bewakings-OUI uit de WiFi-scanengine levert punten op in de categorie Let op. *Dit vervangt geen grondige RF-inspectie*, maar voegt wel passieve omgevingscontrole toe aan een fysieke inspectie.

### ALPR-installaties en privacyonderzoek

Onderzoekers die bewakingsinfrastructuur vastleggen, journalisten in bewaakte omgevingen en privacyvoorvechters die ALPR-installaties in kaart brengen, kunnen Eye Spy gebruiken als draagbare detectieapparatuur voor weinig geld. De seriële uitvoer logt iedere detectie met RSSI. Daardoor is het apparaat geschikt voor eenvoudige gegevensverzameling.

### Reisbeveiliging

Net als de WiFi Canary is Eye Spy ontworpen om mee te nemen. De Atom Lite past in een broekzak of aan een tas. Tijdens reizen via luchthavens, treinstations of openbare evenementen met veel bewaking kan het apparaat voortdurend passief monitoren zonder dat u het hoeft te bedienen.

---

## Architectuurnotities

### Waarom passieve BLE belangrijk is

De keuze voor passief BLE-scannen, zonder scanverzoekpakketten, heeft belangrijke beveiligingsgevolgen. Bij standaard BLE-scanning zendt een scanner een **SCAN_REQ**-pakket uit om aanvullende advertentiegegevens bij iedere zender op te vragen. *Actief BLE-scannen is dus aan beide kanten waarneembaar.* Het gescande apparaat ziet het adres van de scanner in het scanverzoek.

NimBLE in passieve modus luistert alleen naar ongerichte advertentiepakketten (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) en verstuurt nooit een SCAN_REQ. **Het Eye Spy-apparaat zendt tijdens de scanfase helemaal niets via BLE uit.** Een gedetecteerde Axon-bodycam, Flock-camera of AirTag kan de scanner niet zien en er niet op reageren.

### Ontwerp van de persistentietracker

De persistentietracker voor onbekende apparaten houdt een tabel bij met maximaal **50 BLE-MAC-adressen** en tijdstempels voor de eerste en laatste waarneming. De detectie gaat af zodra een MAC-adres drie keer of vaker wordt gezien binnen een periode van minstens vijf minuten.

De limiet van 50 vermeldingen en het verwijdervenster van 30 minuten zijn technische keuzes die detectiegevoeligheid afwegen tegen de RAM-beperkingen van de ESP32. *In een drukke BLE-omgeving, zoals openbaar vervoer, een conferentie of winkelcentrum, kan de tabel snel vol raken met consumentenapparaten.* De RSSI-drempel van −90 dBm beperkt dit door apparaten op grotere afstand te filteren. Zo volgt de tracker vooral apparaten die in de buurt blijven.

### Samenhang tussen scoreverval en afkoelperiode

De **afkoelperiode van 120 seconden** voorkomt dat een apparaat dat voortdurend binnen bereik blijft iedere BLE-cyclus van 9 seconden punten opstapelt. Zonder deze periode zou één Flock-camera iedere 15 seconden +5 toevoegen en binnen enkele minuten honderden punten opleveren.

De **scoredaling van 1 punt per 60 seconden** zorgt ervoor dat de score afneemt nadat een apparaat buiten bereik raakt en de afkoelperiode verloopt zonder nieuwe detectie. *Een enkele detectie van +5 die niet opnieuw wordt geactiveerd, daalt binnen vijf minuten naar nul.* Het apparaat heeft zo een natuurlijke wachttijd tot de toestand weer veilig is, passend bij normale verplaatsingen.

---

## Bijdragen en projectstatus

Eye Spy staat onder de Apache-2.0-licentie op [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Mogelijke uitbreidingen zijn onder meer:

- **Meer OUI-vermeldingen**: breid de Flock Safety- en camera-OUI-tabellen uit wanneer nieuwe hardware-MAC-adressen in het veld worden vastgelegd.
- **Meer BLE-service-UUID's**: nieuwe slimme brillen, camera's en trackers brengen nieuwe UUID's op de markt.
- **Afstellen van de persistentietracker**: de limiet van 50 vermeldingen, de drempel van drie waarnemingen en het venster van vijf minuten zijn instelbare constanten.
- **Seriële datalogging**: het formaat van de seriële uitvoer is bedoeld voor programmatische verwerking. Een externe logger kan detectiegebeurtenissen van meerdere Eye Spy-apparaten samenvoegen.

De firmware staat in één `main.cpp` in de map `src/`, zodat u de code eenvoudig kunt lezen, controleren en aanpassen.

---

## Conclusie

Eye Spy pakt een beperkt maar relevant probleem aan: de fysieke omgeving om u heen krijgt steeds meer bewakingsapparatuur en de meeste apparaten zenden detecteerbare RF-kenmerken uit. **Een M5Stack Atom Lite van $15 met Eye Spy-firmware wordt een scanner die voortdurend de omgeving bewaakt.** Die vertaalt de complexiteit van BLE-pakketanalyse en WiFi-OUI-opzoekingen naar één RGB-led.

Het betrouwbaarheidsscoresysteem weerspiegelt een realistische weging van dreigingen. Een Axon-bodycam in het bereik van de politie levert +5 op en laat de led meteen rood oplichten. Een iBeacon van een winkel levert +2 op en draagt bij aan een breder beeld zonder zelfstandig een vals alarm te veroorzaken. Scoreverval en afkoelperiodes voorkomen dat het apparaat alarm slaat over kortstondige signalen of aanhoudende signalen met een laag risico.

Voor tegenbewaking, reisbeveiliging, detectie van AirTags of simpelweg inzicht in apparaten die in de buurt meekijken, is Eye Spy een praktische, open-source tool die passief werkt en in de uitrusting van beveiligingsprofessionals past.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Shop Eye Spy-detectieapparaten en bespaar 20%
{{< /centerbutton >}}
