---
title: "ESP32 WiFi Canary: passieve detectie van 2,4GHz-bedreigingen"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Een technische bespreking van ESP32 WiFi Canary, een passieve 2,4GHz-sensor die evil twins, deauthenticatie, beveiligingsverlagingen en beacon-overstromingen detecteert."
genre: ["Netwerkbeveiliging", "WiFi-beveiliging", "IoT-beveiliging", "Beveiligingsonderzoek", "Ingebedde systemen", "Privacytools", "ESP32-projecten", "Hardwarebeveiliging", "Draadloze beveiliging", "Open-sourcebeveiliging"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Deauthenticatiedetectie", "Evil-twindetectie", "WiFi-beveiliging", "Passieve WiFi-bewaking", "802.11-beheerframes", "Netwerkbeveiliging", "IoT-beveiliging", "NeoPixel", "SK6812", "PlatformIO", "C++", "Openbronsoftware", "Beveiligingssensor", "Draadloze dreigingsdetectie", "BSSID-bewaking", "SSID-bewaking", "Detectie van beveiligingsverlaging", "Beacon-overstromingsdetectie", "WiFi-bewaking", "RGB-led", "Promiscuous-modus", "Ingebedde beveiliging", "Reisbeveiliging", "Hotel-WiFi-beveiliging", "WiFi in cafés", "Beveiligingsbewustzijn", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Een illustratie van een klein apparaat dat lijkt op de ESP32 WiFi Canary, aangesloten op een USB-poort. Een RGB-led licht in verschillende kleuren op en staat voor de mogelijkheden voor dreigingsdetectie."
coverCaption: ""
---

**Een piepkleine passieve WiFi-dreigingssensor die nooit terugzendt**

## Het probleem met openbare WiFi

Wanneer je verbinding maakt met hotel-WiFi, een hotspot in een café of een netwerk op een luchthaven, vertrouw je erop dat het toegangspunt echt is. Maar **802.11-beheerframes** - de frames die netwerken aankondigen, verbindingen beheren en clients coördineren - zijn in de meeste implementaties *helemaal niet geauthenticeerd*. Met eenvoudige apparatuur kan iemand een SSID klonen, clients met deauthenticatieframes loskoppelen of naast een echt WPA2-netwerk een open loknetwerk opzetten.

De [**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) is een passieve sensor die dit risico zichtbaar maakt. Het apparaat past op de M5Stack Atom Lite, ongeveer zo groot als een suikerklontje. Het sluit aan op USB, leert de omgeving kennen en laat een RGB-led oplichten wanneer het patronen ziet die bij draadloze aanvallen passen.

Het apparaat maakt nergens verbinding mee, verzamelt geen inloggegevens en verzendt geen frames. Het observeert, scoort en toont met kleur wat er aan de hand is.

Dit artikel is een technische referentie voor het project: de detecties, het betrouwbaarheidsmodel, het bouwen en flashen, en de praktische beperkingen.

---

## Wat de ESP32 WiFi Canary wel en niet doet

### Altijd alleen passief

De WiFi Canary gebruikt twee radiomodi, nooit tegelijk:

1. **Promiscuous-modus** - ontvangt en controleert 802.11-beheerframes, zoals deauthenticatie en disassociatie, zonder verbinding met een netwerk.
2. **Scanmodus** - voert actieve WiFi-scans uit om toegangspunten te vinden en met een aangeleerde basislijn te vergelijken.

Het apparaat:
- maakt geen verbinding met een netwerk;
- verzamelt geen gegevensframes of inloggegevens;
- verzendt geen 802.11-frames;
- bewaart niets op permanente flashopslag;
- communiceert niet via internet.

**Alle aangeleerde gegevens staan in RAM en verdwijnen na een herstart.** Dat is bewust: de canary is een **sensor**, geen opnameapparaat.

### De led is de interface

Er is geen scherm, app of webinterface. De volledige uitvoer is één **SK6812 RGB NeoPixel** op GPIO 27 van de M5Stack Atom Lite. De led toont vier toestanden:

| Ledtoestand | Betekenis |
|---|---|
| 🔵 Blauw (langzame puls) | Opstarten, basislijn opbouwen |
| 🟢 Groen (continu) | Normaal, geen problemen met hoge betrouwbaarheid |
| 🟡 Geel (continu) | Waarschuwing, verdacht patroon gevonden |
| 🔴 Rood (snelle puls) | Alarm, dreiging met hogere betrouwbaarheid gevonden |

Opstarten duurt ongeveer **24 seconden** (3 scans van elk 8 seconden). Zodra blauw verdwijnt, is er een basislijn en begint de bewaking.

---

## Hardware

### Primair doel: M5Stack Atom Lite

Het project is ontworpen voor de M5Stack Atom Lite, een compleet ESP32-ontwikkelplatform in een behuizing van 24 × 24 mm.

| Onderdeel | Detail |
|---|---|
| MCU | ESP32-PICO-D4 |
| Led | Eén SK6812 RGB NeoPixel (GPIO 27) |
| Knop | GPIO 39, actief laag |
| USB | CP2104-UART-brug |
| Voeding | USB-C, circa 80–120 mA tijdens scannen |

**Geen breadboard, extra onderdelen of soldeerwerk nodig.** Sluit het apparaat aan op USB-voeding en het start.

### Generieke ESP32 DevKit voor ontwikkeling en tests

Het project bevat een tweede PlatformIO-buildomgeving (`esp32dev`) voor standaard ESP32-ontwikkelborden. In deze configuratie:

- vervangt de ingebouwde led op GPIO 2 de NeoPixel;
- staat volledige seriële debuguitvoer aan;
- werkt alle detectielogica hetzelfde als op de Atom Lite.

Zo kan iedereen met een ESP32 DevKit van circa $5 het project gebruiken en de detectielogica testen zonder de doelhardware.

---

## De basislijn aanleren

### Waarom een basislijn nodig is

Een canary die in een stad bij elk open netwerk afgaat, is nutteloos. De ESP32 WiFi Canary leert eerst de omgeving en gaat daarna pas dreigingen scoren. In de eerste fase bouwt het een **referentietabel** op met toegangspunten die legitiem in de buurt aanwezig zijn.

### Drie scans in 24 seconden

Bij het opstarten voert het apparaat drie WiFi-scans achter elkaar uit, met een pauze ertussen. Daarna wordt de verzameling toegangspunten - SSID, BSSID, versleutelingstype en signaalsterkte - als basislijn opgeslagen.

De seriële uitvoer ziet er zo uit:

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

Zodra de led van blauw naar groen gaat, werkt het apparaat volledig.

---

## Wat het detecteert: dreigingscategorieën

De WiFi Canary bewaakt zes soorten dreigingspatronen. Elk patroon draagt punten bij aan een **betrouwbaarheidsscore** die de ledtoestand bepaalt. *Eén indicator is nooit op zichzelf doorslaggevend*: het model verzamelt bevestigend bewijs voordat het opschaalt.

### 1. Reeksen deauthenticatie en disassociatie

**802.11-beheerframes met subtype 10 (disassociatie) en 12 (deauthenticatie)** worden vaak gebruikt bij WiFi-aanvallen. Elk apparaat kan ze verzenden. Clients die ze ontvangen, worden losgekoppeld van hun toegangspunt.

De canary telt deze frames in **promiscuous-modus** per bron-MAC-adres binnen een voortschrijdend venster van **5 seconden**.

| Voorwaarde | Punten |
|---|---|
| ≥ 8 frames van één bron binnen 5 s | +2 |
| ≥ 20 frames van één bron binnen 5 s | +4 |
| ≥ 5 broadcast-deauthframes | +1 |

**Drempels zijn van belang**: een client die tussen toegangspunten wisselt, genereert enkele legitieme frames. Aanvalstools produceren iets heel anders: honderden frames per seconde tegen een doelwit. Het venster van 5 seconden en de ondergrens van 8 frames filteren normale roamingruis en vangen langdurige bursts van tools als `aireplay-ng` op.

### 2. Open kloon van een bekend versleuteld netwerk (evil twin)

**Dit is de detectie met de hoogste betrouwbaarheid.** Een evil-twin-aanval werkt vaak zo:

1. Een open kopie zonder wachtwoord van een bekende WPA2-SSID opzetten.
2. Het signaal sterker maken dan dat van het echte toegangspunt zodat clients automatisch verbinden.

Na het leren van de basislijn detecteert een nieuwe scan een SSID die eerder alleen WPA/WPA2/WPA3 gebruikte, maar nu als **OPEN** verschijnt:

| Voorwaarde | Punten |
|---|---|
| Dezelfde SSID, eerder versleuteld en nu open | +3 |
| BSSID ontbrak in de basislijn | +1 |
| Kloonsignaal ≥ 10 dB sterker dan bekend toegangspunt | +1 |

Een open kloon van de hotel-WiFi-SSID die ook 10 dB sterker is dan het echte toegangspunt is een schoolvoorbeeld. *Deze combinatie brengt de score in één scancyclus op 5 (Waarschuwing).*

**Serieel voorbeeld**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Het oorspronkelijke versleutelde toegangspunt ontbreekt, open kloon aanwezig

Een geavanceerdere variant: de sterkere kloon laat clients er de voorkeur aan geven, terwijl het echte toegangspunt tegelijk met deauthenticatie van de lucht wordt verdreven.

| Voorwaarde | Punten |
|---|---|
| Versleuteld toegangspunt uit basislijn verdwenen en overeenkomend open netwerk verschenen | +3 |

Dit dekt situaties waarin het echte toegangspunt nog uitzendt, maar de signaalsterktewedstrijd verliest, of actief wordt verstoord.

### 4. Beveiligingsverlaging

Dezelfde SSID als in een basislijnvermelding wordt gezien, maar met zwakkere versleuteling.

| Voorwaarde | Punten |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Daling van 2 of meer versleutelingsniveaus | +3 |

*Open verlagingen vallen onder de evil-twin-detectie met hogere scores.* Deze categorie richt zich op gedeeltelijke verlagingen die bij een eenvoudige vergelijking van open met versleuteld over het hoofd kunnen worden gezien.

### 5. Dubbele SSID van een onverwachte leverancier

Dezelfde SSID en hetzelfde beveiligingstype als bij een toegangspunt in de basislijn, maar met een BSSID van een **andere leverancier-OUI** (de eerste 3 bytes van het MAC-adres).

| Voorwaarde | Punten |
|---|---|
| Andere OUI dan het toegangspunt uit de basislijn met dezelfde SSID | +1 |
| Kloon ook ≥ 10 dB sterker | +2 |

*Deze score is bewust laag.* Bedrijfsnetwerken, mesh-systemen en door providers uitgerolde toegangspunten hebben vaak legitiem meerdere BSSID's met dezelfde SSID en verschillende leveranciers. Dit signaal moet samen met ander bewijs worden meegewogen, niet zelfstandig alarm slaan.

### 6. Beacon- of SSID-overstroming

Het apparaat telt nieuwe SSID's die niet in de basislijn staan en binnen een **voortschrijdend venster van 30 seconden** verschijnen.

| Voorwaarde | Punten |
|---|---|
| ≥ 15 nieuwe SSID's in 30 s | +2 |
| ≥ 30 nieuwe SSID's in 30 s | +3 |

**Beacon-overstromingsaanvallen** zenden duizenden nep-SSID's uit om scantabellen te verwarren of legitieme beacons te verstoren. Vijftien onbekende SSID's in 30 seconden is in de meeste omgevingen ongebruikelijk.

---

## Het betrouwbaarheidsscoremodel

Alle gedetecteerde signalen tellen op tot één geheel getal: de **dreigingsscore**. Die bepaalt de ledtoestand:

| Scorebereik | Ledtoestand |
|---|---|
| 0–2 | Normaal (groen) |
| 3–5 | Waarschuwing (geel) |
| 6+ | Alarm (rood, snelle puls) |

### Scoreverval

De score **daalt elke 60 seconden met 1 punt** als er geen nieuwe gebeurtenissen zijn. Dit is een van de belangrijkste praktische ontwerpkeuzes:

- Eén deauthenticatieburst brengt de score naar Waarschuwing. Als de aanval stopt, daalt de score in enkele minuten vanzelf naar Normaal.
- Een voortdurende aanval houdt de alarmtoestand vast.
- Het apparaat herstelt vanzelf zonder tussenkomst of herstart.

Dit betekent:

- **Korte afwijkingen** zoals roaming en tijdelijke buurtnetwerken verdwijnen vanzelf.
- **Aanhoudende aanvallen** blijven gemarkeerd.
- **Alarmmoeheid** door eenmalige gebeurtenissen die niet terugkeren blijft uit.

### Knop voor reset

Met de knop op GPIO 39 van de Atom Lite kun je twee dingen doen:

1. De volledige huidige tabel met toegangspunten naar de seriële uitvoer sturen. Zo kun je controleren wat het apparaat ziet.
2. De dreigingsscore op 0 zetten. De led gaat meteen terug naar groen en je kunt de volgende scancyclus opnieuw bekijken.

---

## Bouwen en flashen

### Benodigdheden

- **PlatformIO** (CLI of VS Code-extensie)
- **M5Stack Atom Lite** (of ESP32 DevKit voor tests)
- USB-C-kabel

### Flashen naar M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Bouwen en flashen
pio run -e atom-lite --target upload

# Open de seriële monitor op 115200 baud
pio device monitor -b 115200
```

### Flashen naar een generieke ESP32 DevKit

```bash
pio run -e esp32dev --target upload
```

De DevKit-build gebruikt GPIO 2 (ingebouwde led) en toont het volledige seriële log. De NeoPixel wordt niet aangestuurd. Alle detectielogica is identiek aan die van de Atom Lite.

### Projectstructuur

```
esp32-wifi-canary/
├── main.cpp              # Alle firmwarelogica
├── platformio.ini        # Buildomgevingen (atom-lite, esp32dev)
├── partitions_4mb.csv    # 4MB-flashpartitietabel
└── README.md
```

De volledige firmware staat in **één C++-bronbestand**. De detectielogica gebruikt geen externe bibliotheken, alleen het ESP32 Arduino-framework voor WiFi-scans, callbacks in promiscuous-modus en NeoPixel-besturing.

### Omgevingen in platformio.ini

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

De omgeving `atom-lite` gebruikt de borddefinitie `m5stick-c` (dezelfde ESP32-PICO-D4-chip, met een compatibele pinindeling voor de NeoPixel op GPIO 27).

---

## Referentie voor seriële uitvoer

Het apparaat geeft uitgebreide logs op **115200 baud**. Alle logregels beginnen met `[canary]`, zodat je ze eenvoudig kunt filteren.

### Opstartvolgorde

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

### Detectiegebeurtenissen

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Scoreovergangen

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Het seriële log maakt zichtbaar wat het apparaat zag, wanneer het dat zag en waarom de score veranderde. Het vormt ook een **passief auditlog**, zelfs wanneer je niet naar de led kijkt.

---

## Detectieaantekeningen en praktische beperkingen

De README is opvallend eerlijk over wat dit apparaat niet kan. Die beperkingen verdienen uitleg.

### Mogelijke foutpositieven

**Bedrijfs- en meshnetwerken** veroorzaken de meeste foutpositieven. Een groot bedrijfsnetwerk, hotel of mesh-systeem zoals Eero of Google WiFi kan legitiem het volgende vertonen:

- Meerdere BSSID's voor dezelfde SSID met verschillende vendor-OUI's.
- Verschillen in beveiligingsinstellingen tussen frequentiebanden.
- Toegangspunten die verschijnen en verdwijnen wanneer het mesh-netwerk zich aanpast.

**Airbnb- en SOHO-routers** met aparte SSID's voor verschillende banden kunnen ook verschillen in vendor-OUI veroorzaken als de 2,4GHz- en 5GHz-radio's opeenvolgende MAC-adresblokken gebruiken.

*Tijdelijke buurtnetwerken*: een versleuteld netwerk dat kort uit scans verdwijnt en met andere parameters terugkeert (na een firmware-update, herstart of herconfiguratie) kan kortstondig detectie activeren.

De score en het verval zijn bedoeld om foutpositieven *te verminderen, niet weg te nemen*.

### Mogelijke foutnegatieven

**Een goed uitgevoerde evil-twin-aanval** die:

- De exacte BSSID van het echte toegangspunt nabootst, zodat de OUI overeenkomt.
- Exact hetzelfde beveiligingstype gebruikt, met een correcte WPA2-IE-configuratie.
- Een signaalsterkte binnen 10 dB van het echte toegangspunt heeft.

*Verzamelt mogelijk niet genoeg punten om de Waarschuwingsdrempel te bereiken.* Het onderdeel voor deauthenticatie levert punten op, maar een geraffineerde aanvaller die weinig frames verstuurt, kan onder de drempel blijven.

### Gat bij het wisselen van radiomodus

**De ESP32-radio kan niet tegelijk in promiscuous-modus staan en actief naar toegangspunten scannen.** De firmware wisselt tussen deze modi. Daardoor worden **deauthenticatieframes tijdens het scanvenster van ongeveer 3 seconden niet vastgelegd**. Een aanvaller die zijn bursts precies op die vensters afstemt, kan detectie ontwijken, al moet die daarvoor het scanschema kennen.

### Alleen 2,4 GHz

De ESP32-radio werkt op 2,4 GHz. **Netwerken op 5 en 6 GHz worden niet gescand of bewaakt.** Dit apparaat detecteert dus geen evil twins die uitsluitend op 5 GHz actief zijn.

### Passief bereik

Deauthenticatiedetectie vereist dat het apparaat de frames kan ontvangen. Een aanvaller op afstand, met een zeer gerichte antenne, of gericht op een client ver van de canary kan frames uitzenden die te zwak zijn om de tellers te activeren.

---

## Gebruikssituaties

### Reizen met gevoelig werk

De canary is vooral ontworpen voor reizen. Sluit hem aan op een laptop, USB-aansluiting in een hotelkamer of draagbare batterij en laat hem de omgeving van het hotel of conferentiecentrum leren. Een open kloon van de hotel-SSID, het meest voorkomende aanvalsscenario, veroorzaakt vervolgens minstens een Waarschuwing.

### Cafés en openbare WiFi

Open WiFi is een veelvoorkomend doelwit voor evil twins. Dankzij de basislijn leert de canary bij aankomst het legitieme toegangspunt en bewaakt het daarna concurrerende SSID's.

### Beveiligingsbewustzijn en onderwijs

De seriële uitvoer toont in begrijpelijke taal wat het apparaat ziet. Voor beveiligingstraining is een deauthenticatieburst in realtime tonen en de led zien verkleuren veel effectiever dan een presentatie.

### Passieve labbewaking

In een thuislab of klein kantoor werkt de canary als continue omgevingssensor. De led toont de status in één oogopslag. Met de knop kun je op verzoek de huidige toegangspunten bekijken.

---

## Architectuuraantekeningen

### Waarom één score in plaats van aparte alarmen

Het model combineert verschillende signalen in één score in plaats van aparte alarmcategorieën te tonen. Dat is een bewuste keuze voor de gebruikersinterface: één led heeft drie toestanden. Losse alarmen zouden een scherm of app vereisen. *De score zet ruisrijke, deels samenhangende signalen om in één bruikbare indicator.*

### Waarom de score vervalt

Zonder verval vereist één foutpositief handmatig ingrijpen met de knop. Met verval na 60 seconden verdwijnen korte afwijkingen binnen enkele minuten. **De canary kan daardoor onbeheerd werken** in een tas, hotelkamer of auto en na tijdelijke gebeurtenissen terugkeren naar de basislijn.

### Waarom drie basisscans

Eén scan kan een toegangspunt missen dat op dat moment niet uitzendt, bijvoorbeeld door een scanpauze of tijdelijke stroomuitval. *Drie scans in ongeveer 24 seconden geven een vollediger beeld van de stabiele omgeving voordat de bewaking begint.*

---

## Bijdragen en projectstatus

Het project staat op [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) onder een licentie voor passief gebruik. De code bestaat uit één `main.cpp`, waardoor lezen, controleren en uitbreiden eenvoudig is.

Wie met PlatformIO en ESP32 werkt, kan het project zonder aanpassingen bouwen voor zowel de Atom Lite als een standaard DevKit.

---

## Vergelijking met andere WiFi-bewakingsmethoden

| Methode | Passief? | Geen inloggegevens | Eén led als uitvoer | Reisformaat |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (laptop) | ✅ | ✅ | ❌ (scherm nodig) | ❌ (zwaar) |
| WiFi Pineapple | ❌ (actief) | ❌ | ❌ | Gedeeltelijk |
| Draadloos IDS (bedrijf) | ✅ | ✅ | ❌ (infrastructuur nodig) | ❌ |
| Handmatig scannen (telefoon-app) | Gedeeltelijk | ✅ | ❌ | ✅ |

De canary heeft een specifieke functie: **altijd-aan omgevingsbewaking zonder interactie of netwerkverbinding**, in een formaat dat aan een sleutelhanger kan of in een laptoptas past.

---

## Conclusie

De ESP32 WiFi Canary doet één ding: de 2,4GHz-omgeving bewaken en van kleur veranderen wanneer iets verdacht lijkt. Het is geen volledig draadloos inbraakdetectiesysteem, pakketopnameapparaat of forensische analyzer. Het is een canary: een passieve sensor die opmerkt wanneer de omgeving gevaarlijk wordt.

Het **betrouwbaarheidsscoremodel**, **scoreverval** en de **basislijn in drie fasen** zijn gericht op het probleem van foutpositieven bij omgevingssensoren. Het apparaat kan onbeheerd in een hotelkamer of conferentiecentrum werken en betekenisvolle afwijkingen signaleren, terwijl het stil blijft tijdens normale netwerkveranderingen.

Voor wie een draagbare beveiligingsset bouwt, met onbetrouwbare WiFi-infrastructuur werkt of een nuttig ESP32-project zoekt, is de WiFi Canary een middag en een M5Stack Atom Lite van $15 waard.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
