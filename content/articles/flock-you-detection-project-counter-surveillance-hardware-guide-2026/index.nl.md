---
title: "Flock-You Detectie: Handleiding voor Contra-Surveillance"
date: 2026-05-24
lastmod: 2026-11-19
toc: true
draft: false
description: "Uitgebreide technische handleiding voor het open-source Flock-You project voor het detecteren van Flock Safety ALPR-camera's met ESP32-hardware. Inclusief installatie-instructies, firmware-details en aankoopinformatie."
genre: ["Beveiligingshardware", "Contra-surveillance", "Privacytechnologie", "open-sourceprojecten", "ESP32 Ontwikkeling", "wifi-bewaking", "Privacytools", "Digitale Rechten", "hardwarehacking", "Netwerkbeveiliging"]
tags: ["Flock-You-project", "ALPR Detectie", "ESP32-S3", "WiFi OUI Detectie", "hardware voor contra-surveillance", "Flock Safety Detectie", "open-sourcebeveiliging", "privacyhardware", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "wifi-meeluistermodus", "802.11-bewaking", "Colonel Panic Tech", "STS Collective", "Privacyapparaten", "detectie van bewaking", "WiFi-scannen", "GitHub-project", "colonelpanichacks", "ESP32-firmware", "hardware-installatiehandleiding", "DIY-privacyhulpmiddelen", "netwerkbewaking", "OUI-database", "detectie van jokerprobes", "frameanalyse", "ALPR-cameradetectie", "Privacytechnologie", "detectiehardware", "Arduino ESP32", "Platform.io", "ingebedde systemen", "RF-detectie", "Signaalverwerking", "privacy-engineering", "Contra-technologie", "Beveiligingsonderzoek", "privacybehartiging", "open hardware", "privacybescherming", "detectiefirmware", "mobiele detectie", "privacyprojecten", "hardwarevergelijking"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Een illustratie van een ESP32-apparaat op de voorgrond dat WiFi-signalen scant. Kleurrijke golven vertegenwoordigen verschillende signaalsterktes tegen een donkere achtergrond."
coverCaption: "Open-source hardwareoplossingen voor het detecteren van ALPR-bewakingscamera's"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Volledige Technische Handleiding voor het Bouwen en Gebruiken van Flock-You Detectieapparaten**

## Inleiding: Open Source Contra-Surveillance

Het **Flock-You project** is een **open-source, door de gemeenschap gedreven initiatief** om de ALPR-bewakingsinfrastructuur van Flock Safety te detecteren en in kaart te brengen. Gehost op GitHub als **colonelpanichacks/flock-you**, gebruikt dit project betaalbare ESP32-hardware om Flock-camera's te identificeren via hun **WiFi-netwerksignaturen**.

**Flock-You detecteert alleen Flock Safety-camera’s via WiFi.** Het detecteert geen mobiele-zendersimulators zoals Stingray en geen persoonlijke trackers die met je meebewegen. Gebruik daarvoor **[Rayhunter-apparaten flashen: complete handleiding](/articles/how-to-flash-rayhunter-devices-complete-guide/)** om IMSI-catchers te detecteren en **[Eye Spy: passieve surveillancedetector voor de M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** voor AirTags en volgers. Alle drie werken op dezelfde betaalbare ESP32-hardwarefamilie.

Deze uitgebreide handleiding behandelt alles, van de **technische methodologie** achter Flock-detectie tot **stapsgewijze installatie-instructies** voor drie hardwareplatforms, **firmware-installatie** en **aankoopinformatie van erkende leveranciers**. Of u nu een privacyadvocaat, beveiligingsonderzoeker of bezorgde burger bent, deze handleiding stelt u in staat uw eigen detectieapparaat te bouwen of aan te schaffen.


*Flock Safety-hardware staat vrijwel volledig in de Verenigde Staten, met een kleinere aanwezigheid in Canada. Buiten Noord-Amerika komen de OUI-lijst en probe-signaturen hieronder niet overeen met apparaten in de buurt. De hardware blijft nuttig voor onderzoek, maar vindt geen infrastructuur die daar niet aanwezig is.*

Voor context over waarom deze technologie belangrijk is en het bredere surveillancelandschap, lees ons aanvullende artikel: **[Flock Safety Camera Bewaking: Prevalentie, Privacyzorgen en Beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Wilt u zien waar Flock-camera's al in kaart zijn gebracht? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** is een open-source tool die 40.000+ vermoedelijke Flock Safety-camera's wereldwijd plot op basis van WiGLE WiFi-data en OUI-fingerprinting — dagelijks bijgewerkt. Broncode op **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

### In één oogopslag: drie platforms

*Volledige specificaties, plus- en minpunten van elk platform staan hieronder. Ga naar de [installatie-instructies](#stapsgewijze-installatie-instructies) als je al weet welk platform je kiest.*


| Platform | Prijs | Installatie | Geschikt voor |
|---|---|---|---|
| **DIY ESP32** | $5–12 | Soldeerloos breadboard, 10–15 min | Budgetbouw en leren hoe detectie werkt |
| **M5 Atom Lite** (vooraf geflasht) | $49,99 | Aansluiten en starten, geen installatie | Direct gebruik zonder doe-het-zelfwerk |
| **OUI-SPY** | $85 | Eenmalig flashen, modus kiezen in het Wi-Fi-menu | Detectie in meerdere modi (ALPR, drones, BLE) |

______

## De Flock-You Detectiemethodologie Begrijpen

### De Technische Basis

Flock Safety-camera's bevatten **ingebouwde WiFi-modules** voor connectiviteit en beheer op afstand. Deze modules zenden identificeerbare netwerksignaturen uit die detecteerbaar zijn door apparaten die in de **promiscuous WiFi-monitoringmodus** werken. Het Flock-You project maakt gebruik van dit kenmerk via:

#### 1. WiFi OUI (Organizationally Unique Identifier) Detectie

Elke netwerkinterface heeft een **MAC-adres** dat bestaat uit:
- **Eerste 3 bytes (24 bits)**: OUI, die de fabrikant identificeert
- **Laatste 3 bytes**: Apparaatspecifieke identificatie

Onderzoekers **@NitekryDPaul** en de **DeFlockJoplin**-gemeenschap ontdekten **31 specifieke OUI's** die consequent aanwezig zijn bij Flock Safety-camera-implementaties:

```
Belangrijkste Espressif-OUI’s (ESP32-gebaseerde modules):
D4:AD:FC - Espressif Inc. (gangbare ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3-varianten)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (op basis van ESP32)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (op basis van ESP32)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Aanvullende OUI’s die in Flock-installaties zijn geïdentificeerd:
[... nog 21 OUI’s van fabrikanten ...]
```

Wanneer een detectieapparaat WiFi-verkeer in meeluistermodus scant, **identificeert het elk apparaat dat frames met deze OUI's uitzendt**.

#### 2. Detectie van generieke sondeeraanvragen

Flock-camera's sturen periodiek **generieke sondeeraanvragen** om beschikbare netwerken te zoeken. Deze hebben onderscheidende kenmerken:

- **802.11-beheerframe**: Type=0, Subtype=4
- **SSID Information Element**: Length=0 (leeg/joker, wildcard)
- **Framestructuur**: Voorspelbaar patroon in probe-timing
- **Vendor-specifieke IE's**: Aanvullende indicatoren in de frame-payload

Detectiefirmware analyseert deze **patronen van sondeeraanvragen** om de betrouwbaarheid van Flock-camera-identificatie te vergroten, verder dan eenvoudige OUI-matching.

#### 3. Promiscuous Modus WiFi-Monitoring

Standaard WiFi-werking ontvangt alleen frames die naar uw apparaat zijn geadresseerd. **Promiscuous modus** legt alle WiFi-frames in het bereik vast:

- **802.11 framestructuur**: Analyse van addr1, addr2, addr3 velden
- **Beheerframes**: sondeeraanvragen, bakenframes (beacon frames) en associatieverzoeken
- **Data frames**: Onthullen netwerksgedragspatronen
- **Controle frames**: ACK's, RTS's, CTS's bieden tijdinformatie

ESP32-microcontrollers ondersteunen meeluistermodus via de **esp_wifi API**, waardoor goedkope detectiehardware mogelijk is.

#### 4. Signaalsterkte-analyse

Detectieapparaten meten **RSSI (indicator voor de ontvangen signaalsterkte)** om:
- **Afstand te schatten** tot gedetecteerde camera's
- **Locaties te trianguleren** met meerdere metingen
- **Valse positieven te filteren** op basis van verwachte signaalkenmerken
- **Warmtekaarten te maken** van cameradichtheid

### Detectienauwkeurigheid en Valse Positieven

De Flock-You-methodologie bereikt hoge nauwkeurigheid:

- **Echt Positief Percentage**: ~95% voor bevestigde Flock-camera's binnen bereik
- **Vals Positief Percentage**: ~5-10% afhankelijk van de omgeving
- **Detectiebereik**: 15-90 meter afhankelijk van obstakels en antenne
- **Betrouwbaarheidsscore**: Meerfactorenanalyse vermindert valse alarmen

**Veelvoorkomende Bronnen van Valse Positieven**:
- **ESP32-ontwikkelborden** gebruikt in andere IoT-apparaten
- **Commerciële ESP32-producten** (slimme woning, sensoren)
- **Andere bewakingscamera's** die vergelijkbare componenten gebruiken
- **WiFi-testapparatuur** bediend door technici

**Mitigatiemaatregelen**:
- **Multi-handtekeningdetectie**: Combinatie van OUI + probe-patroon + fysieke verificatie
- **Locatiecorrelatie**: Kruisverwijzing met bekende cameralocaties
- **Visuele bevestiging**: Fysieke inspectie na elektronische detectie
- **Gemeenschapsdatabase**: Door de gemeenschap gevalideerde detecties

______

{{< figure src="flockyou-oui-detection-methodology-overview.webp" alt="Flock-You-detectiediagram: ESP32 in Wi-Fi-promiscue modus vergelijkt MAC-adressen met bekende Flock-OUIs, controleert wildcard-probes en beoordeelt RSSI" >}}

{{< stscollective-ad "flockyou" >}}

## Vergelijking van Hardwareplatforms

Drie primaire platforms zijn beschikbaar voor Flock-You-detectie, elk met afzonderlijke voordelen:
*Alle drie de platforms gebruiken dezelfde onderliggende detectiemethode: passief scannen in de WiFi-promiscuousmodus naar bekende OUI's van Flock-camera's en wildcardsignaturen van probeverzoeken. Geen ervan detecteert Bluetooth. De Flock-You-firmware liet BLE-detectie in het voorjaar van 2026 vallen nadat die niet meer betrouwbaar werkte. Daarom gebruiken alle platforms hier uitsluitend WiFi.*

### Overzichtstabel van Platforms

| Functie | DIY ESP32 | M5 Atom Lite (Vooraf geflasht) | OUI-SPY |
|---------|-----------|-------------------------------|---------|
| **Fabrikant** | DIY / Meerdere leveranciers | STS Collective | Colonel Panic Tech |
| **Prijs** | $5-12 | $39,99 | $85 |
| **Processor** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Gebruiksklaar** | Nee (DIY bouw) | Ja (vooraf geflasht) | Ja (multi-modus) |
| **Scherm** | Optioneel | RGB LED (5×5 matrix) | Geen |
| **Batterij** | Optioneel | Externe aanbevolen | Niet inbegrepen |
| **GPS** | Optioneel | Nee | Nee |
| **Meldingen** | Buzzer + LED | RGB LED (blauw=detectie) | Geïntegreerde buzzer |
| **Gegevensopslag** | Optioneel | Nee | Nee |
| **Behuizing** | 3D-print of geen | Compact plastic module | Geen (kale PCB) |
| **Firmware** | Handmatig flashen | Vooraf geladen FlockYou | Multi-modus (4 firmware's) |
| **Beste voor** | DIY-enthousiastelingen, leren | Betaalbaar en gebruiksklaar | Multi-doel detectie |
| **Installatiemoeilijkheid** | Gemiddeld-Gevorderd | Geen installatie nodig | Geen installatie nodig |
| **Gewicht** | 20-50g (variabel) | 18g (kaal) | ~40g |
| **Afmetingen** | Variabel | 24×24×14mm | PCB-bord |

### Gedetailleerde Platformanalyse

#### 1. DIY ESP32 Bouw ($5-12)

**Overzicht**: Meest betaalbare optie met standaard ESP32-ontwikkelborden en open-source firmware.

**Hardwarespecificaties**:
- **Microcontroller**: ESP32-WROOM-32 of vergelijkbaar (met twee kernen, 240 MHz)
- **WiFi**: 802.11 b/g/n, meeluistermodus mogelijk
- **Geheugen**: 520KB SRAM, 4MB+ Flash
- **Scherm**: Optioneel (ingebouwde LED voldoende)
- **Voeding**: USB-gevoed of batterijpack
- **Buzzer**: Optionele passieve buzzermodule (KY-006)
- **Indicatoren**: Ingebouwde LED + optionele buzzer
- **Uitbreidbaarheid**: Breadboard-vriendelijk, eenvoudige aanpassingen

**Firmware**: Open-source fork op **simeononsecurity/flock-you-esp32**:
- Aangepast voor standaard ESP32-hardware (GPIO 25, 2, 17)
- Super Mario Bros. opstartmelodie (bevestigt dat buzzer werkt)
- Twee snelle oplopende piepjes bij nieuwe detectie
- Hartslag-piepjes van 10 seconden bij actief volgen
- Flask-dashboard ondersteuning voor GPS-wifinetwerkverkenning onderweg
- Export naar JSON, CSV, KML-formaten

**Bouwopties**:
- **Alleen LED ($5)**: Kale ESP32 + USB-kabel, alleen visuele feedback
- **Breadboard ($9-11)**: Voeg passieve buzzer + breadboard + jumpers toe, audio-meldingen
- **Ingesloten ($10-12)**: Voeg 3D-geprinte behuizing toe met klikdeksel

**Voordelen**:
- ✅ Goedkoopste optie (85-95% kostenbesparend t.o.v. OUI-SPY)
- ✅ Volledig open-source en aanpasbaar
- ✅ Gebruikt veelverkrijgbare ESP32-borden
- ✅ Educatief, leert embedded systemen
- ✅ Uitgebreide documentatie en handleidingen
- ✅ 3D-printbare behuizingsbestanden beschikbaar
- ✅ **Dezelfde detectienauwkeurigheid als premium-apparaten**

**Nadelen**:
- ❌ Vereist DIY-assemblage (soldeerloze breadboard of 3D-behuizing)
- ❌ Handmatig flashen van firmware nodig
- ❌ Geen geïntegreerde batterij (USB-voeding of extern pack)
- ❌ Alleen basale audio-feedback (geen scherm)
- ❌ Kost tijd om componenten te bemachtigen

**Beste voor**: Makers, studenten, privacyadvocaten met een budget, iedereen die wil leren hoe detectie werkt, degenen die van DIY-projecten houden.

**Componenten Kopen**:
- **Amazon**: Zoek naar "ESP32 DevKit" of "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Bulkkortingen beschikbaar
- **Adafruit**: Gecureerde kwaliteitsonderdelen met tutorials

**Installatiebronnen**:
- **GitHub Repo**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Bouwhandleiding**: Soldeerloze assemblage in 10-15 minuten
- **Behuizingsbestanden**: OpenSCAD parametrisch ontwerp + STL-bestanden

---

{{< figure src="flockyou-diy-esp32-solderless-breadboard-build.webp" alt="Soldeerloze Flock-You-opstelling met ESP32 op breadboard, DevKit, passieve zoemer en draden naar GPIO 25, 2 en 17" >}}

#### 2. M5 Atom Lite Vooraf Geflasht door STS Collective ($39,99)

**Overzicht**: Vooraf geflasht compact detectieapparaat, direct bruikbaar uit de doos.

**Hardwarespecificaties**:
- **Microcontroller**: ESP32-PICO-D4 (met twee kernen, 240 MHz)
- **WiFi**: 802.11 b/g/n, meeluistermodus mogelijk
- **Geheugen**: 520KB SRAM, 4MB Flash
- **Scherm**: 5×5 RGB LED-matrix (WS2812C NeoPixel)
- **Voeding**: 5V via USB-C of Grove-connector
- **Batterij**: Niet inbegrepen (externe USB-powerbank aanbevolen)
- **Indicator**: Programmeerbare RGB LED (blauw=detectie)
- **Knoppen**: 1 programmeerbare knop
- **I/O**: Grove-connector voor uitbreiding
- **Afmeting**: Ultra-compact 24×24×14mm
- **Behuizing**: Duurzame plastic module

**Firmware**: Aangepaste FlockYou-port door STS Collective (eigendomsrecht):
- Vooraf geladen en klaar voor gebruik
- Blauwe LED-melding bij detectie van Flock-camera
- Gebaseerd op colonelpanichacks FlockYou-onderzoek
- Geen installatie of flashen vereist
- Eenvoudige bediening zonder ingewikkelde installatie
- Optionele dashboard-ondersteuning

**Voordelen**:
- ✅ Vooraf geflasht, geen technische installatie vereist
- ✅ Betaalbare kant-en-klare oplossing
- ✅ Extreem compact en draagbaar
- ✅ Bewezen hardwareplatform
- ✅ Eenvoudige blauwe LED = detectie
- ✅ USB-C gevoed (auto, powerbank, laptop)
- ✅ Kwaliteitsondersteuning van leverancier
- ✅ Reguliere prijs $99,99, in aanbieding $39,99

**Nadelen**:
- ❌ Geen geïntegreerde batterij (heeft USB-voeding nodig)
- ❌ Beperkt scherm (alleen RGB LED, geen display)
- ❌ *Firmware is eigendomsrechtelijk, momenteel niet open-source*
- ❌ Geen gegevensopslag zonder computerverbinding
- ❌ Enkele knop beperkt functionaliteit

**Beste voor**: Gebruikers die directe detectie willen zonder DIY-werk, prioriteit aan draagbaarheid, degenen die tevreden zijn met eenvoudige LED-feedback, budget-bewuste kopers die een kant-en-klare oplossing willen.

**Aankoop**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Exclusieve Korting**: Bespaar tot 20% op STS Collective-producten — gebruik code **SIMEONONSECURITY** bij het afrekenen of [klik hier om te winkelen met de korting toegepast](https://stscollective.com/discount/SIMEONONSECURITY).

---

{{< figure src="flockyou-m5-atom-lite-pocket-size-comparison.webp" alt="Vooraf geflashte M5 Atom Lite tussen twee vingers, met compact formaat en blauwe RGB-detectie-led" >}}

#### 3. OUI-SPY door Colonel Panic Tech ($85)

**Overzicht**: Multi-modus bewakingsdetectiebord met vier verschillende firmwaremodi selecteerbaar via een WiFi-menu.

**Hardwarespecificaties**:
- **Microcontroller**: ESP32-S3 met twee Xtensa-LX7-kernen, 8 MB flash
- **WiFi**: 802.11 b/g/n, meeluistermodus mogelijk
- **Geheugen**: 8MB Flash
- **Scherm**: Geen (kale PCB met LED-indicatoren)
- **Batterij**: Niet inbegrepen
- **Opladen**: USB-C voeding & programmering
- **Opslag**: Geen (alleen detectiemodi)
- **Indicatoren**: Geïntegreerde PWM-buzzer met modusspecifieke melodieën
- **Knoppen**: Bootknop voor modusomschakeling
- **Antenne**: **Schakelbaar**, ingebouwde 2,4GHz keramisch OF extern via MMCX-connector
- **Behuizing**: Geen (kale PCB met PCB-kunst)
- **Uniek Kenmerk**: MAC-randomisatie bij elke opstart

**Firmware**: OUI-SPY Unified Blue met **4 selecteerbare modi**:
1. **Detectormodus**: Multi-doel BLE-scanner met OUI-filtering + webconfiguratiepaneel
2. **Foxhunter-modus**: Enkeldoel RSSI-nabijheidstracker voor radio-richtingvinding
3. **Flock-You-modus**: Flock Safety & Raven-cameradetectie met GPS-wifinetwerkverkenning onderweg, JSON/CSV/KML-export
4. **Sky Spy-modus**: Drone RemoteID (OpenDroneID / ASTM F3411) detector met multi-drone tracking

**Modusselectie**:
- WiFi-opstartmenu op 192.168.4.1
- Houd BOOT-knop 2 seconden vast om terug te keren naar selector
- Onthoud laatste modus over stroominschakelingen
- Modusspecifieke opstartmelodie (retro chiptune-meldingen)
- Alleen detectiebediening (niets verzonden)

**Voordelen**:
- ✅ Vier firmwaremodi in één apparaat
- ✅ Schakelbare antenne (ingebouwd of extern MMCX)
- ✅ Geïntegreerde buzzer met aangepaste opstartmelodieën
- ✅ PCB-ontwerp van professionele kwaliteit
- ✅ Multi-doel: ALPR, drones, BLE, RF-richtingvinding
- ✅ Van de oorspronkelijke Flock-You-projectmaker
- ✅ Actieve ontwikkeling en updates

**Nadelen**:
- ❌ Hoogste prijs voor enkeldoel Flock-detectie
- ❌ Geen behuizing inbegrepen (kale PCB)
- ❌ Geen ingebouwde batterij
- ❌ Geen scherm (alleen audio-feedback voor de meeste modi)
- ❌ *Complexiteit onnodig voor basisdetectie*
- ❌ Externe GPS vereist voor wifinetwerkverkenning onderweg

**Beste voor**: Multi-doel bewakingsdetectie, gebruikers die drone + ALPR + BLE-detectie in één apparaat willen, RF-richtingvinding toepassingen, degenen die schakelbare antennes en geavanceerde functies waarderen.

**Aankoop**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

{{< figure src="flockyou-oui-spy-multimode-board-pcb.webp" alt="Kale OUI-SPY ESP32-S3-printplaat met antenne, zoemer en bootknop; scherm toont Wi-Fi-menu met vier modi" >}}

## Stapsgewijze Installatie-instructies

### Installatiehandleiding 1: DIY ESP32 Bouw

**Voor volledige gedetailleerde instructies**, bezoek de GitHub-repository: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Snel Start Overzicht

1. **Vereiste Hardware**:
   - ESP32 DevKit-bord ($5-6)
   - USB-kabel (Micro-USB of USB-C afhankelijk van bord)
   - Optioneel: Passieve buzzermodule (KY-006), breadboard, jumpers
   - Optioneel: 3D-geprinte behuizing

2. **Software Installatie**:
   ```bash
   # PlatformIO installeren
   pip install platformio

   # Repository klonen
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32

   # Firmware flashen
   pio run -t upload
   pio device monitor
   ```

3. **Hardware Assemblage** (bij gebruik van buzzer):
   - Buzzer positief → GPIO 25
   - Buzzer negatief → GND
   - LED-indicator → GPIO 2 (ingebouwd)
   - Voeding via USB

4. **Opstartbevestiging**:
   - Super Mario Bros. 1-2-melodie speelt af (als buzzer aangesloten)
   - LED knippert om scanning aan te geven
   - Seriële monitor toont "Flock-You ESP32"-initialisatie

5. **Detectiemeldingen**:
   - **Nieuwe detectie**: Twee snelle oplopende piepjes (2000→2800 Hz)
   - **Hartslag**: Twee piepjes elke 10 seconden tijdens volgen
   - **LED**: Knippert bij elke detectie

6. **GPS-wifinetwerkverkenning onderweg** (optioneel):
   - Verbind met computer via USB
   - Start Flask-dashboard: `cd api && python flockyou.py`
   - Open http://localhost:5000
   - Verbind GPS-apparaat of gebruik browserlocatie
   - Exporteer detecties naar JSON/CSV/KML

**Volledige bouwhandleiding, behuizingsbestanden en probleemoplossing**: Zie de GitHub README

---

### Installatiehandleiding 2: M5 Atom Lite Vooraf Geflasht (STS Collective)

#### Snel Start

1. **Uitpakken**:
   - M5 Atom Lite-apparaat (vooraf geflasht met FlockYou-firmware)
   - Controleer productlijst voor inclusie van USB-C-kabel

2. **Inschakelen**:
   - Verbind met USB-C-voedingsbron (powerbank, auto-USB, wandadapter, computer)
   - Apparaat start automatisch op
   - RGB LED-matrix initialiseert

3. **Bediening**:
   - **Inactief/Scannen**: LED toont scanpatroon
   - **Detectie**: LED wordt **BLAUW** wanneer Flock-camera gedetecteerd
   - **Knop**: Druk om handmatig opnieuw te scannen of te resetten

4. **Draagbaar Gebruik**:
   - Verbind met USB-batterijpack (5000mAh = ~20 uur)
   - Plaats in bekerhouder, tas of zak
   - LED zichtbaar door doorschijnende behuizing

5. **Dashboard Verbinding** (optioneel):
   - Verbind apparaat met computer via USB-C
   - Installeer FlockYou-dashboard per STS Collective-instructies
   - Bekijk live detecties in browserinterface

**Waarschuwing**: *Dit is propriëtaire firmware. Opnieuw flashen met open-source versies verwijdert de STS-firmware permanent.*

---

### Installatiehandleiding 3: OUI-SPY Multi-Modus Bord

#### Initiële Installatie

1. **Pakketinhoud**:
   - OUI-SPY kale PCB-bord
   - USB-C-kabel
   - Snelstarthandleiding

2. **Eerste Inschakeling**:
   - Verbind USB-C-voeding (computer, wandadapter of powerbank)
   - Apparaat zendt WiFi-netwerk uit: `OUISPY-[ID]`
   - Buzzer speelt modusspecifieke opstartmelodie

3. **WiFi Modusselectie**:
   - Verbind telefoon/computer met OUI-SPY WiFi-netwerk
   - Open browser naar: `http://192.168.4.1`
   - Webinterface toont 4 firmwaremodi:
     1. **Detector** - Multi-doel BLE-scanner
     2. **Foxhunter** - RF-richtingvinding
     3. **Flock-You** - ALPR-cameradetectie
     4. **Sky Spy** - Drone RemoteID-detector
   - Selecteer gewenste modus en klik op "Activeren"

4. **Flock-You Modus Bediening**:
   - Apparaat herstart in Flock-You-modus
   - Buzzer speelt Flock-You opstartmelodie
   - Begint met scannen op 31 bekende OUI's
   - **Detectiemelding**: Buzzer piept met uniek patroon
   - Laatste modus onthouden over stroominschakelingen

5. **Modi Wisselen**:
   - Houd **BOOT-knop** 2 seconden vast
   - Apparaat keert terug naar WiFi-modusselector
   - Herverbind met WiFi en kies nieuwe modus

#### Geavanceerd: Externe Antenne

6. **Antenne Omschakelen** (voor uitgebreid bereik):
   - Standaard: Gebruikt ingebouwde keramische antenne
   - Verbind MMCX-antenne met MMCX-connector
   - Firmware schakelt automatisch over naar externe antenne

#### Montage

7. **Voertuig/Vaste Installatie**:
   - *Geen behuizing inbegrepen, kale PCB heeft bescherming nodig voor montage*
   - Opties:
     - 3D-print aangepaste behuizing
     - Klittenband-montage op dashboard
     - Gebruik dubbelzijdig tape
     - DIY-projectdoos
   - Houd USB-C-poort toegankelijk voor voeding

#### Gegevens Export (Flock-You Modus)

8. **GPS-wifinetwerkverkenning onderweg**:
   - Verbind externe GPS-module (niet inbegrepen)
   - Apparaat logt detecties met coördinaten
   - Download gegevensbestanden via webinterface
   - Exportformaten: JSON, CSV, KML

**Opmerking**: Controleer colonelpanic.tech voor firmware-updates en documentatie specifiek voor OUI-SPY Unified Blue.

---

______

## Aankoophandleiding en Leveranciersinformatie

### Erkende Leveranciers

#### Colonel Panic Tech (colonelpanic.tech)

**Aangeboden Producten**:
- **OUI-SPY** ($85): Gebruiksklaar Flock-detectieapparaat
- **DIY Kits** ($55): Componenten + PCB + assemblagehandleiding
- **GPS Module Add-on** ($18): Compatibele GPS-6M module
- **Accessoires**: Antennes, behuizingen, batterij-upgrades

**Waarom Kopen bij Colonel Panic**:
- ✅ Direct van de ontwikkelaar van OUI-SPY hardware
- ✅ Nieuwste firmware vooraf geïnstalleerd
- ✅ Technische ondersteuning inbegrepen
- ✅ Open-source ethos (schema's beschikbaar)
- ✅ Actief communityforum

**Verzending**:
- Binnenlands VS: 3-5 werkdagen
- Internationaal: 7-14 werkdagen
- Gratis verzending bij bestellingen >$100

**Garantie**: 90 dagen hardwaregarantie, levenslange firmware-updates

**Website**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Aangeboden Producten**:
- **M5 Atom Lite Vooraf Geflasht** ($39,99): Gebruiksklaar Flock-detectieapparaat
- **Accessoires**: Compatibel met diverse ESP32-platforms

**Waarom Kopen bij STS Collective**:
- ✅ Vooraf geflashte gebruiksklare apparaten
- ✅ Kwaliteitsborging en testen
- ✅ Betaalbare prijzen
- ✅ Klantenondersteuning

**Verzending**:
- Binnenlands VS: 2-4 werkdagen (Priority Mail)
- Internationaal: 7-21 werkdagen
- Spoedopties beschikbaar

**Garantie**: Standaardgarantie op hardware

**Website**: [https://stscollective.com](https://stscollective.com)

> 💰 **Lezerkorting**: Gebruik code **SIMEONONSECURITY** voor tot 20% korting op STS Collective-producten — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Andere Bronnen voor M5 Atom Lite

**Officiële M5Stack Winkel**:
- Website: [shop.m5stack.com](https://shop.m5stack.com)
- Prijs: $9,95 voor kale Atom Lite
- Accessoires: Batterijmodules, Grove-sensoren, behuizingen
- Verzending: Internationaal, 7-14 dagen

**Amazon**: Zoek naar "M5Stack Atom Lite"
- Prijs: ~$12-15 (varieert per verkoper)
- Prime-verzending beschikbaar
- Bundelopties met accessoires

**Adafruit**: [adafruit.com](https://adafruit.com)
- Gecureerde elektronikaverkoper
- Uitstekende leerresources
- Snelle verzending vanuit de VS

**Opmerking**: *Bij aankoop van een kale M5 Atom Lite moet firmware apart worden geïnstalleerd volgens de bovenstaande DIY-handleiding. De vooraf geflashte STS Collective-versie is een ander product.*

### Prijsvergelijking Samenvatting

| Apparaat | Basisprijs | Optionele Add-ons | Totale Investering | Installatietijd |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | 3D-behuizing, batterij | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39,99 | Batterijpack $10 | $40-50 | Direct klaar voor gebruik |
| **OUI-SPY** | $85 | Externe antenne $20, behuizing | $85-115 | Direct klaar voor gebruik |

______

## Uw Detectieapparaat Gebruiken: Praktische Scenario's

### Scenario 1: Dagelijkse Woon-werkverkeer Mapping

**Doel**: Flock-cameralocaties documenteren langs uw vaste routes.

**Installatie**:
- Gebruik apparaat met GPS-mogelijkheid (DIY ESP32 met GPS-module of OUI-SPY met GPS)
- Schakel automatische logging in
- Monteer in voertuig of draag in zak
- Stel gevoeligheid in op GEMIDDELD om valse positieven te verminderen

**Procedure**:
1. Start detectieapparaat voor vertrek
2. Rijd uw normale route
3. Apparaat waarschuwt wanneer Flock-camera's gedetecteerd worden
4. GPS-coördinaten automatisch gelogd
5. Keer thuis terug en exporteer data
6. Importeer GPX/CSV in kaartsoftware
7. Maak persoonlijke cameralocatiekaart

**Voordelen**:
- Bewustzijn van bewakingsdekking op uw routes
- Identificeer cameravrije alternatieve routes
- Bijdragen aan communautaire karteringsprojecten
- Bijhouden van implementatiewijzigingen in de tijd

### Scenario 2: Buurt Bewakingsbeoordeling

**Doel**: Flock-cameradekking in uw woonwijk bepalen.

**Installatie**:
- Gebruik draagbaar apparaat (M5 Atom Lite, DIY ESP32 of OUI-SPY)
- Loop- of fietssurvey
- Stationaire monitoring op belangrijke kruispunten

**Procedure**:
1. Loop/fiets door buurtstraten
2. Stop bij elk kruispunt voor 30-60 seconden
3. Noteer detecties op kaart
4. Gebruik signaalsterkte om afstand/richting te schatten
5. Bevestig cameralocaties visueel waar mogelijk
6. Documenteer bevindingen met foto's (vanuit openbare gebieden)

**Uitkomst**:
- Volledige kaart van lokale bewakingsinfrastructuur
- Bewijs voor gemeenschapsorganisatie
- Data voor verzoeken om openbare documenten
- Bewustzijn voor persoonlijke privacybeslissingen

*De loopsnelheid is belangrijker dan veel mensen verwachten. De firmware wisselt ongeveer elke 250 ms van WiFi-kanaal om bij te blijven met hoe vaak de camera zelf van kanaal wisselt. Als je snel loopt of fietst, ben je mogelijk voorbij het detectievenster voordat een kanaalwissel samenvalt. Krijg je tijdens een lopende meting wisselende resultaten, vertraag dan bij kruispunten in plaats van meteen een antenne met meer versterking te proberen. Een standaardantenne met 30 tot 60 seconden wachttijd per stop vindt veel meer camera’s dan een antenne met hoge versterking terwijl je er stevig langs loopt.*


### Scenario 3: Reisprivacy Beoordeling

**Doel**: Bewakingsblootstelling begrijpen bij reizen.

**Installatie**:
- Neem compact apparaat mee (M5 Atom Lite in zak of DIY ESP32)
- Schakel continue logging in
- Bekijk data na de reis

**Gebruiksscenario's**:
- Medische afspraken: Beoordeel bewaking nabij klinieken
- Juridische consultaties: Controleer dekking in het kantoorgebied van de advocaat
- Religieuze diensten: Begrijp monitoring nabij gebedshuizen
- Politieke activiteiten: Evalueer bewaking bij evenementen/protesten
- Huishoudelijke situaties: Identificeer of de woning gemonitord wordt

### Scenario 4: Gemeenschapsadvocacy

**Doel**: Data bieden voor beleidsdebattten en publiek bewustzijn.

**Toepassingen**:
- Bevindingen presenteren op gemeenteraadsvergaderingen
- Opnemen in verzoeken om openbare documenten
- Delen met privacyadvocacy-organisaties
- Bijdragen aan onderzoeksprojecten
- Buurtverenigingen informeren

**Datapresentatie**:
- Warmtekaarten maken die cameradichtheid tonen
- Rapporten genereren over dekkingsverschillen
- Tijdlijnen maken van implementatieuitbreiding
- Correleren met misdaadstatistieken (of het ontbreken ervan)

______

{{< figure src="flockyou-detection-device-driving-scenario.webp" alt="Bestuurder kijkt naar FlockYou-detector in bekerhouder; led waarschuwt voor camera dichtbij" >}}

## Technische gedetailleerde uiteenzetting: De Code Begrijpen

### Kern Detectie-algoritme (Vereenvoudigd)

Voor degenen die geïnteresseerd zijn in de technische implementatie, hier is een vereenvoudigd overzicht van de detectielogica:

```cpp
// Kern van Flock-You-detectie (conceptueel, geen volledige code)

// OUI-database (31 met Flock geassocieerde OUI’s)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Espressif ESP32-S3-variant
    // ... nog 28 OUI’s ...
};

// Callback voor meeluistermodus
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;

    // MAC-adres uit frame halen
    uint8_t *mac = pkt->payload + 10; // Positie van het addr2-veld

    // Controleren in de OUI-database
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI-overeenkomst gevonden
            int rssi = pkt->rx_ctrl.rssi;

            // Drempel voor signaalsterkte controleren
            if (rssi > RSSI_THRESHOLD) {
                // Frame analyseren op extra kenmerken
                if (is_wildcard_probe_request(pkt)) {
                    // Detectie met hoge betrouwbaarheid
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // Alleen OUI-overeenkomst
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard-probe detecteren
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Beheerframe, subtype probe request
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;

    // Controleren op lege SSID IE (wildcard)
    // Positie hangt af van de frame-indeling
    uint8_t *ie = &pkt->payload[24]; // Begin van de IE’s
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard-probe
    }
    return false;
}
```

### Belangrijkste Technische Concepten Uitgelegd

**Promiscuous Modus**: In plaats van alleen frames te ontvangen die naar uw apparaat zijn geadresseerd, legt ESP32 alle WiFi-frames in het bereik vast. **Dit is essentieel voor het detecteren van nabijgelegen apparaten die niet met uw detector communiceren.**

**MAC-adresstructuur**: Elk WiFi-frame bevat meerdere MAC-adressen:
- `addr1`: Ontvangstadres
- `addr2`: Zendadres (bevat OUI)
- `addr3`: Adres van eindbestemming/bron

**RSSI (indicator voor de ontvangen signaalsterkte)**: Signaalsterkte in dBm (negatieve decibels relatief aan 1 milliwatt). Typische waarden:
- -30 dBm: Extreem sterk (zeer dichtbij)
- -50 dBm: Sterk signaal
- -70 dBm: Zwak maar bruikbaar
- -90 dBm: Zeer zwak (rand van bereik)

**Sondeeraanvragen**: WiFi-apparaten sturen sondeeraanvragen om beschikbare netwerken te ontdekken. *Jokerprobes met een lege SSID zoeken naar elk netwerk. IoT-apparaten zoals Flock-camera's gebruiken dit vaak, waardoor ze betrouwbaar detecteerbaar zijn.*

______

## Problemen Oplossen
{{< figure src="flockyou-troubleshooting-firmware-flash-flowchart.webp" alt="Stroomschema voor problemen met flashen en detecteren, van stroomproblemen tot foutieve OUI-treffers" >}}

### Probleem: Geen Detecties Ondanks Bekende Camera in de Buurt

**Mogelijke Oorzaken**:
1. **Camera offline/uitgeschakeld**: Flock-camera's zijn soms tijdelijk inactief
2. **Signaal geblokkeerd**: Bouwmaterialen absorberen WiFi (metaal, beton)
3. **Buiten bereik**: Effectief bereik ~30-90 meter afhankelijk van obstakels
4. **Te snel bewegen**: door het wisselen van kanalen werkt langzaam lopen of volledig stilstaan beter dan stevig doorlopen of rijden
5. **Firmwareprobleem**: Verouderde firmware mist nieuwere OUI-varianten

**Oplossingen**:
- Bevestig dat camera zichtbaar is en operationeel lijkt (zonnepanelen, lampjes)
- Beweeg dichter naar vermoede cameralocatie
- Probeer verschillende antenneoriëntaties
- Update naar nieuwste Flock-You firmware
- **Controleer of apparaat actief scant** (controleer LED/display-activiteit)

### Probleem: Overmatige Valse Positieven

**Mogelijke Oorzaken**:
1. **Hoge dichtheid van ESP32-apparaten**: Slimme woning, IoT-apparaten zijn gebruikelijk
2. **Gevoeligheid te hoog**: Detectie van verre/irrelevante apparaten
3. **Andere bewakingscamera's**: Veel gebruiken ESP32-modules

**Oplossingen**:
- Verlaag gevoeligheidsinstelling
- Schakel detectie van generieke sondeeraanvragen in (hogere betrouwbaarheid)
- Verificeer detecties fysiek voor logging
- Gebruik signaalsterkte om te filteren (alleen waarschuwen bij sterke signalen)
- Update OUI-database om te focussen op bevestigde Flock OUI's

### Probleem: Batterij Loopt Snel Leeg

**Mogelijke Oorzaken**:
1. **Continu scannen**: Geen slaap/energiebeheer
2. **Scherm altijd aan**: Scherm verbruikt aanzienlijk vermogen
3. **GPS actief**: GPS-modules zijn energiehongering
4. **Oude batterij**: Li-Po batterijen nemen af in de loop der tijd

**Oplossingen**:
- Schakel passieve scanmodus in (intermitterend vs. continu)
- Stel schermtime-out in
- Schakel GPS uit wanneer mapping niet nodig is
- Vervang batterij (OUI-SPY/mesh-detect v2 hebben vervangbare batterijen)
- Gebruik extern batterijpack voor uitgebreide sessies

### Probleem: GPS Krijgt Geen Vergrendeling

**Mogelijke Oorzaken**:
1. **Binnengebruik**: GPS vereist zichtbaarheid van de lucht
2. **Antenne niet aangesloten**: mesh-detect v2 heeft externe antenne nodig
3. **Koude start**: Eerste GPS-vergrendeling duurt 5-15 minuten
4. **Storing**: Nabijgelegen elektronica stoort het signaal

**Oplossingen**:
- Ga naar een positie met vrij zicht op de lucht
- Zorg ervoor dat antenne goed is aangesloten (SMA-connector)
- Wacht op initiële vergrendeling (volgende vergrendelingen sneller)
- Ga weg van RF-storingsbronnen
- Controleer of GPS is ingeschakeld in instellingen

### Probleem: Gegevens Worden Niet Gelogd naar SD-kaart

**Mogelijke Oorzaken**:
1. **SD-kaart niet geformatteerd**: Moet FAT32-formaat zijn
2. **SD-kaart vol**: Geen ruimte meer
3. **Kaart niet gedetecteerd**: Niet volledig ingevoerd
4. **Bestandssysteemcorruptie**: Kaart beschadigd

**Oplossingen**:
- **Formatteer SD-kaart als FAT32** (32GB maximaal voor compatibiliteit)
- Verwijder oude logs of gebruik grotere kaart
- Voer kaart volledig in (moet klikken)
- Herformatteer kaart of vervang als beschadigd
- Controleer of apparaat kaart herkent (menu toont SD-status)

______

## Juridische en Ethische Overwegingen

### Juridische Status van Detectieapparaten

**Legaliteit van WiFi-Scanning**:
- ✅ **Legaal in de VS**: Passieve WiFi-monitoring (alleen ontvangen) is legaal
- ✅ **Geen interceptie**: Apparaten monitoren alleen openbaar uitgezonden frames
- ✅ **Geen decodering**: Geen poging om data te decoderen of verbinding te maken met netwerken
- ✅ **Vergelijkbaar met radioscanners**: Vergelijkbare juridische status als politiescanners

**Belangrijke Onderscheidingen**:
- ❌ **Illegaal**: Actieve jamming/storing van camerawerking
- ❌ **Illegaal**: Proberen camera-systemen te hacken of toegang te krijgen
- ❌ **Illegaal**: Vernietigen of manipuleren van fysieke camera's
- ⚠️ **Grijs gebied**: *Sommige rechtsgebieden hebben strengere privacywetten. Controleer lokale regelgeving voor gebruik.*

**Aanbeveling**: **Detectieapparaten zijn alleen voor bewustzijn. Niet ingrijpen in camerawerking.**

### Richtlijnen voor Ethisch Gebruik

**Verantwoord Gebruik**:
- ✅ Gebruik voor persoonlijk bewustzijn van bewaking
- ✅ Documenteer voor advocacy en beleidsdiscussies
- ✅ Deel geaggregeerde data met privacyorganisaties
- ✅ Bijdragen aan communautaire karteringsprojecten
- ✅ Informeer anderen over bewakingsinfrastructuur

**Vermijden**:
- ❌ Data gebruiken om illegale activiteiten te faciliteren
- ❌ Eigenaren lastigvallen die camera's hebben geïnstalleerd
- ❌ Terrein betreden om cameralocaties te bevestigen
- ❌ Vigilante-acties tegen bewakingsinfrastructuur

### Privacyoverwegingen

**Uw Gegevensprivacy**:
- **Detectieapparaten loggen UW locatie** (via GPS)
- Sla deze data veilig op
- **Wees bewust van dagvaardingsrisico** bij betrokkenheid bij juridische procedures
- Overweeg encryptie voor gevoelige logbestanden
- Begrijp privacybeleid van leveranciers voor cloud-verbonden apparaten

**Anderen Respecteren**:
- Wees bedachtzaam bij gebruik van detectieapparaten in privéruimten
- Gebruik niet om andere personen te volgen
- Overweeg ethische implicaties van het delen van data

______

## Gemeenschap en Open Source Ontwikkeling

### Bijdragen aan het Flock-You Project

Het Flock-You project gedijt op gemeenschapsbijdragen:

**GitHub Repository**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Manieren om bij te dragen**:
1. **Nieuwe OUI Ontdekking**: Dien nieuw geïdentificeerde Flock-camera OUI's in
2. **Codeverbeteringen**: Dien pull requests in voor firmware-verbeteringen
3. **Hardware Ontwerpen**: Deel aangepaste detectieapparaat-ontwerpen
4. **Documentatie**: Verbeter installatiehandleidingen, vertalingen
5. **Testen**: Rapporteer bugs, verifieer functionaliteit op apparaten
6. **Kartering**: Bijdragen aan door de gemeenschap samengestelde cameralocatiedatabases

### Gemeenschapsbronnen

**Forums en Discussie**:
- **Reddit**: r/privacy, r/privacytoolsIO, actieve discussies
- **Discord**: Colonel Panic Tech server, realtime chat
- **GitHub Issues**: Technische ondersteuning en functieverzoeken

**Onderzoekspapers**:
- Academische studies over ALPR-bewaking
- Privacy-impactbeoordelingen
- Juridische analyses van legaliteit van detectieapparaten

**Advocacy Organisaties**:
- **Electronic Frontier Foundation** (EFF): ALPR-tracking
- **ACLU**: Bewaking en privacyrechten
- **Lokale groepen**: DeFlockJoplin en soortgelijke gemeenschapsinitiatieven

### Toekomstige Ontwikkeling Roadmap

**Geplande Functies** (van project GitHub):
- **Machine learning**: Patroonherkenning voor hogere nauwkeurigheid
- **Cloud synchronisatie**: Optionele door de gemeenschap samengestelde detectiedatabase
- **Mobiele apps**: Smartphone-integratie voor verbeterde interfaces
- **Aanvullende detectiemodi**: Andere bewakingstechnologieën
- **Realtime meldingen**: Pushmeldingen via mobiel/WiFi

______

## Conclusie: Privacy Ondersteunen via Technologie

Het **Flock-You detectieproject** vertegenwoordigt een krachtige democratisering van contra-surveillancetechnologie. Voor minder dan de kosten van een maandelijks streamingabonnement krijgen individuen inzicht in de bewakingsinfrastructuur om hen heen. Of u nu kiest voor de **DIY ESP32-bouw ($5-12)**, de **gebruiksklare M5 Atom Lite ($40)** of de **multi-modus OUI-SPY ($85)**, u investeert in privacybewustzijn en digitale autonomie.


*Houd rekening met wat deze hardware wel en niet detecteert: Flock-camera’s via WiFi. Stingrays en persoonlijke trackers die met je meebewegen detecteert hij niet. Combineer hem met Rayhunter en Eye Spy hieronder als je een bredere dekking nodig hebt.*

### Kernpunten

- **Open source en gratis aanpasbaar**: ontwikkeling door de gemeenschap houdt de OUI-lijst en firmware actueel
- **Betaalbare hardware**: een losse ESP32 kost $5–12; hogere niveaus voegen gemak toe, geen nieuwe detectiemogelijkheden
- **Alleen passieve bewaking**: het apparaat ontvangt openbaar uitgezonden Wi-Fi-frames en zendt niets uit
- **Regelmatig bijgewerkt**: nieuwe OUI-signaturen en onderzoek naar wildcard-probes worden toegevoegd wanneer Flock-hardware verandert
- **In het veld getest**: de DeFlockJoplin-gemeenschap detecteerde 11 van 12 bekende camera’s tijdens een echte testrit

### Volgende Stappen

1. **Lees de achtergrond**: [Flock Safety Camera Bewaking: Prevalentie, Privacyzorgen en Beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Kies je platform**: stem DIY ESP32, M5 Atom Lite of OUI-SPY af op budget en vaardigheden
3. **Bestel hardware**: koop bij een hierboven genoemde erkende verkoper
4. **Flash en configureer**: volg de installatiehandleiding voor je gekozen platform
5. **Doe mee met de gemeenschap**: deel bevindingen en draag detecties bij aan het project
6. **Vul de beperkingen aan**: gebruik [Rayhunter-apparaten flashen: complete handleiding](/articles/how-to-flash-rayhunter-devices-complete-guide/) voor IMSI-catchers en [Eye Spy: passieve surveillancedetector voor de M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/) voor AirTags en andere trackers

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Koop kant-en-klare FlockYou-apparaten en bespaar 20%
{{< /centerbutton >}}

De proliferatie van ALPR-bewaking vertegenwoordigt een significante verschuiving in privacydynamica. Contra-surveillancetechnologieën zoals Flock-You bieden een cruciale mogelijkheid: **bewustzijn**. Wanneer we de omvang en schaal van bewaking begrijpen, nemen we geïnformeerde beslissingen over onze bewegingen, onze advocacy en onze verwachtingen van privacy in openbare ruimten.

______

## Gerelateerde Artikelen

| Artikel | Beschrijving |
|---------|-------------|
| **[Flock Safety Camera Bewaking: Prevalentie, Privacyzorgen en Beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | De definitieve gids voor het ALPR-netwerk van Flock Safety, gedocumenteerde misbruiken, bronnen voor gemeenschapsorganisatie en wat u kunt doen om uzelf te beschermen |
| **[Flock Finder: Breng Elke Vermoedelijke Flock Safety Camera bij U in Kaart](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Hoe de open-source Flock Finder-tool te gebruiken om 40.000+ vermoedelijke Flock-camera's wereldwijd te visualiseren met WiGLE-data en OUI-fingerprinting |
| **[Eye Spy: passieve surveillancedetector voor de M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** | BLE- en WiFi-detector voor AirTags, Tile-trackers, bodycams en drones, als aanvulling op Flock-You binnen dezelfde hardwarefamilie. |
| **[Rayhunter-apparaten flashen: complete handleiding](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Stapsgewijze handleiding voor het flashen van Rayhunter-firmware om IMSI-catchers en Stingrays te detecteren, als aanvulling op ALPR-detectie |
| **[DagShell Aangepaste Firmware voor de Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Volledige handleiding voor het installeren van DagShell op de Orbic RCL400 voor geavanceerde mobiele netwerkmonitoring en detectie van IMSI-afluisterapparatuur |
| **[Rayhunter Apparaatvergelijking 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Zij-aan-zij vergelijking van apparaten ondersteund door Rayhunter om u te helpen de juiste hardware te kiezen voor uw contra-surveillance toolkit |

Zoek je een hulpmiddel dat trackers actief verstoort in plaats van ze alleen te detecteren? [Simulacra](https://github.com/Em3ritus/simulacra) is een onafhankelijk open-sourceproject zonder banden met deze gids. Het verspreidt lokapparaten voor BLE en WiFi om het signaal van je echte apparaat te verbergen. Het lost een ander probleem op dan de apparaten in deze gids en is nuttig als passieve detectie niet volstaat voor je dreigingsmodel.

______

## Referenties

1. [Flock-You GitHub-repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - interactieve kaart met ALPR-camera’s](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - GitHub-repository](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - officiële leverancierssite](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite met vooraf geïnstalleerde firmware](https://stscollective.com)
6. [Officiële documentatie voor M5Stack Atom Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
7. [Espressif-documentatie voor de ESP32 WiFi-API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)
8. [Naslag voor 802.11-probeaanvragen en -antwoorden](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)
9. [DeFlock Joplin - gemeenschappelijk ALPR-onderzoek](https://deflockjoplin.today)
10. [DeFlock - gezamenlijke ALPR-kaart en gegevens](https://deflock.me/)
11. [Electronic Frontier Foundation - wat is ALPR?](https://www.eff.org/pages/what-alpr)
12. [Officiële download van Arduino IDE](https://www.arduino.cc/en/software)
13. [Platform.io-documentatie](https://docs.platformio.org/)
14. [IEEE Registration Authority - groot MAC-adresblok (OUI)](https://standards.ieee.org/products-programs/regauth/oui/)
15. [Naslag voor de structuur van 802.11-beaconframes](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
