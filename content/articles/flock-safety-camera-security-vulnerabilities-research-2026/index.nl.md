---
title: "Kwetsbaarheden in Flock Safety-camera's: meer dan 50 fouten gevonden"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Onderzoek naar kwetsbaarheden in Flock Safety-camera's behandelt blootgestelde inloggegevens, zwakke beveiliging, fysieke toegang en beperkingen bij meldingen."
genre: ["Beveiligingsonderzoek", "Kwetsbaarheidsanalyse", "Bewakingstechnologie", "Cyberbeveiliging", "Privacy en beveiliging", "IoT-beveiliging", "Fysieke beveiliging", "Netwerkbeveiliging", "Kritieke infrastructuur", "Overheidstechnologie"]
tags: ["Flock Safety-kwetsbaarheden", "ALPR-beveiliging", "Camera hacken", "IoT-beveiligingsfouten", "Hardgecodeerde wachtwoorden", "Kwetsbaarheden in Android Things", "Exploit via fysieke toegang", "Netwerkbeveiliging", "Versleutelingsfouten", "Schendingen van gegevensprivacy", "CVE-meldingen", "Beveiligingsonderzoek", "GainSec-onderzoek", "Onderzoek van Ben Jordan", "Beveiliging van bewakingscamera's", "Fouten in overheidstechnologie", "Kritieke kwetsbaarheden", "Verantwoorde openbaarmaking", "Cyberbeveiligingsanalyse", "Technologie voor wetshandhaving", "Beveiliging van openbare veiligheid", "Draadloos toegangspunt", "Authenticatie omzeilen", "Inloggegevens in leesbare tekst", "RF-lekkage", "Tempest-aanval", "Informatielekkage", "Root-shelltoegang", "Code op afstand uitvoeren", "Beveiligingsaudit", "Kwetsbaarheidsbeoordeling", "Risico voor nationale veiligheid", "Onderzoek door de Senaat", "Beloningsprogramma voor fouten", "Zero-daykwetsbaarheid", "Exploitontwikkeling", "Penetratietesten", "Whitepaper over beveiliging", "Berichtgeving van 404 Media", "Onafhankelijk onderzoek", "Hardwarebeveiliging", "Firmwareanalyse", "Systeemmisbruik"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Een hightech bewakingscamera met felblauwe en groene accenten tegen een donkere achtergrond. Abstracte vormen en lijnen eromheen staan voor digitale beveiligingslekken."
coverCaption: "Kritieke beveiligingsfouten stellen meer dan 80.000 bewakingscamera's bloot aan onbevoegde toegang"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Meer dan 50 kritieke beveiligingskwetsbaarheden stellen het grootste particuliere bewakingsnetwerk van het land bloot**

## Inleiding: een crisis voor de nationale veiligheid

Eind 2024 en gedurende 2025 ontdekten onafhankelijke beveiligingsonderzoekers wat mogelijk **de grootste beveiligingsfout in de geschiedenis van bewakingstechnologie voor wetshandhaving** is. Er zijn **meer dan 50 kritieke kwetsbaarheden** in de camerasystemen van Flock Safety gevonden. Die camera's fotograferen en volgen dagelijks meer dan **150 miljoen voertuigen** bij ruim **80.000 installaties** in het hele land.

Dit artikel analyseert de kwetsbaarheden technisch op basis van:
- **De officiële whitepaper van GainSec**, "Examining the Security Posture of an Anti-Crime Ecosystem" (51 bevindingen, 22 toegewezen CVE's en 8 in behandeling)
- **Het onderzoeksjournalistieke werk** en de praktische beveiligingstests van Ben Jordan
- **De berichtgeving van 404 Media** over openbaar toegankelijke camerabeelden
- **Officiële reacties** van Flock Safety en Amerikaanse senatoren
- **Gepubliceerde meldingen** in de National Vulnerability Database
- **De bestandssysteemdump van september 2026** die Distributed Denial of Secrets publiceerde, met een technische analyse per regel door Micah Lee en een gezamenlijk onderzoek van WIRED en 404 Media

Lees voor context over **waarom deze camera's bestaan** en **de gevolgen voor privacy** ook ons artikel: **[Bewaking met Flock Safety-camera's: verspreiding, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Lees voor informatie over **het opsporen van deze camera's**: **[Flock-You-detectieproject: gids voor hardware tegen surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## De omvang van het probleem

### De schaal van kwetsbare infrastructuur

Per mei 2026:
- **Meer dan 80.000 Flock Safety-camera's** in gebruik in de Verenigde Staten
- **Meer dan 5.000 steden en dorpen** gebruiken Flock-diensten
- **Meer dan 3.500 wetshandhavingsinstanties** hebben toegang tot het systeem
- **Meer dan 22.000 gebruikers bij wetshandhaving** raadplegen databases
- **Miljarden gegevenspunten** staan in doorzoekbare databases

### Tijdlijn van de kwetsbaarheden

- **Eind 2024**: beveiligingsonderzoeker Jon "GainSec" Gaines ontdekt de eerste kwetsbaarheden
- **Februari 2025**: verantwoorde melding aan Flock Safety begint
- **April 2025**: eerste CVE-toewijzingen worden gepubliceerd
- **November 2025**: officiële whitepaper met 51 bevindingen verschijnt
- **December 2025**: Ben Jordan demonstreert kwetsbaarheden op video
- **Januari 2026**: 404 Media ontdekt meer dan 60 openbaar toegankelijke camerafeeds
- **Februari 2026**: Amerikaanse senatoren vragen de FTC om onderzoek
- **Mei 2026**: het meldingsproces loopt door

### Categorieën van kwetsbaarheden

De meer dan 50 kwetsbaarheden vallen in meerdere categorieën:
1. **Authenticatie en autorisatie** (hardgecodeerde wachtwoorden, geen MFA)
2. **Cryptografie en versleuteling** (gegevens niet versleuteld tijdens opslag of overdracht)
3. **Netwerkbeveiliging** (blootgestelde wifi-toegangspunten, inloggegevens in leesbare tekst)
4. **Fysieke beveiliging** (misbruik van knopcombinaties, blootgestelde USB-poorten)
5. **Gegevensprivacy** (onbevoegde gegevensverzameling, lange bewaartermijn)
6. **Systeemontwerp** (verouderde software, ontoereikende toegangscontrole)
7. **Informatielekkage** (blootgestelde API-sleutels, openbare camerafeeds)

______

## De bestandssysteemdump van september 2026

**In september 2026 publiceerde de transparantieorganisatie Distributed Denial of Secrets volledige bestandssysteemafbeeldingen van een Flock-camera die in gebruik was.** Een collectief dat zichzelf **stegan0gram** noemt, schroefde de hardware van de paal, kopieerde de interne opslag en publiceerde de afbeeldingen. **404 Media** en **WIRED** deden gezamenlijk onderzoek. Beveiligingsonderzoeker **Micah Lee** publiceerde een technische analyse van de inhoud.

Alle eerdere bevindingen in dit artikel kwamen van een onderzoeksapparaat of een gekocht exemplaar. Deze dataset komt van een camera die actief door een gemeente werd gebruikt. Daarmee is dit tot nu toe het sterkste gepubliceerde bewijs.

*De camera is niet via het netwerk gehackt. Hij is fysiek weggehaald.*

### Wat de dump bevat

De publicatie bevat drie partitieafbeeldingen. Elke afbeelding vertelt een ander deel van het verhaal.

| Partitie | Grootte | Waarom dit van belang is |
|-----------|------|----------------|
| **system** | 1.5 GB | Android-systeemimage met **19 door Flock gebouwde apps**, waaronder `flock-sambuca`, `flock-collins` en `flock-phone-home` |
| **persist** | 32 MB | Apparaatgegevens in `flock/auth0/auth0_cred`, op een **onversleutelde partitie die een fabrieksreset overleeft** |
| **media** | 18 GB | Logboeken en beelden in een container waarvan de **ontsleutelingssleutel op dezelfde partitie staat** |

### Het probleem met inloggegevens is bevestigd

De dump maakt duidelijk of hardgecodeerde inloggegevens theoretisch zijn of in gebruik zijn. Ze zijn in gebruik.

**Een API-sleutel die toegang geeft tot de backend van Flock staat hardgecodeerd in de toepassingsbinaries.** De waarde staat in een klasse met de naam `CameraSettings` in `com.flocksafety.android.common.lib`. Flock levert de gedeelde bibliotheek mee met alle 19 apps, dus de sleutel zit in elk exemplaar. De app `flock-sambuca` gebruikt de sleutel tijdens het configureren.

**De authenticatiestroom werkt als volgt:**

1. Elke camera vraagt inloggegevens op bij een Flock-server en identificeert zichzelf met het **MAC-adres**.
2. De aanmeldservice **Okta Auth0** van Flock stuurt een kortlevend `FlockAuth0Token` terug.
3. De camera slaat de ontvangen inloggegevens **op als leesbare tekst**.

De Auth0-client-ID en het clientgeheim staan op de **onversleutelde partitie `/persist`**, in een bestand dat een fabrieksreset overleeft. Een aanvaller haalt eerst de persist-partitie op, want niets beschermt die.

[Kritieke kwetsbaarheid 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system) beschrijft het bredere patroon van hardgecodeerde geheimen op het platform.

### De versleutelingssleutel staat bij het slot

Flock zegt dat zijn camera's met **versleuteling op het apparaat** zijn beveiligd. De dump laat zien hoe dat in de praktijk werkt.

De mediapartitie van 18 GB staat inderdaad in een versleutelde container. De ontsleutelingssleutel staat op dezelfde partitie, in een bestandsnaam die eindigt op `.key`. Het collectief stegan0gram haalde de sleutel op, ontgrendelde de container en las de inhoud. **De beelden zijn versleuteld zoals een afgesloten doos afgesloten is wanneer de sleutel met tape op het deksel zit.**

De teruggevonden logboeken tonen ook de positie van de camera zelf. De GPS-coördinaten komen **155 keer** in de logboeken voor, gegroepeerd binnen ongeveer 100 meter. Dat is normale afwijking voor een ontvanger die aan een paal is bevestigd. De coördinaten wijzen naar **Wauwatosa in Wisconsin**, een voorstad van Milwaukee waar de camera aan N Mayfair Road stond. Micah Lee vergeleek de logboeken met Google Street View en stelde het specifieke apparaat vast aan de hand van het serienummer en MAC-adres.

*Versleuteling van opgeslagen gegevens betekent niets wanneer de sleutel naast de versleutelde gegevens ligt.*

### De reactie van Flock

De reactie van Flock herhaalde het standpunt over de eerdere bevindingen van GainSec. Een woordvoerder verklaarde:

> "Flock neemt beveiliging serieus en heeft een openbaar beleid voor het melden van kwetsbaarheden, zodat beveiligingsonderzoekers mogelijke kwetsbaarheden rechtstreeks aan ons melden. Via dat proces hebben we geen melding ontvangen. Op basis van de beperkte informatie die is verstrekt, hebben we onvoldoende details om de beweringen te beoordelen."

Deze reactie strookt moeilijk met de tijdlijn. De kwetsbaarheden in het besturingssysteem van de camera zijn in **2018 en 2021** openbaar gepatcht. De normen voor opslag van inloggegevens en sleutelbeheer zijn al ruim voor de introductie van de camera niet veranderd. **Een decennium aan openbare kwetsbaarheidsgeschiedenis doornemen vereist geen externe melding.**

Flock noemde ook het verwijderen en analyseren van de camera illegaal. Dat klopt volgens de huidige wet. De beveiligingsbevindingen blijven op zichzelf staan, ongeacht hoe de hardware is verkregen.

### Waarom dit zwaarder weegt dan het eerdere onderzoek

De whitepaper van GainSec documenteerde 51 bevindingen op apparaten die legaal waren verkregen. Flock betwistte de ernst en stelde dat fysieke nabijheid nodig was.

Deze dump neemt die voorbehouden weg. De standaardconfiguratie van een productiecamera, zonder aanpassingen door de beheerders, bevat infrastructuurinloggegevens als leesbare tekst, sleutels naast de gegevens die ze beveiligen en een besturingssysteem met acht jaar achterstallige beveiligingsupdates. **Er was geen exploit nodig. Alleen een moersleutel.**

______

## De apparaatvloot

Flock verkoopt een productlijn en niet één camera. De beveiliging verschilt per apparaat. De onderstaande specificaties komen uit de demontage door GainSec en de firmwareanalyse die de detectiegemeenschap bij **[WiFi Mothership](https://wifimothership.com/flock)** heeft samengesteld.

| Apparaat | Functie | Platform | Besturingssysteem |
|--------|------|----------|-----|
| **Falcon** | Camera voor kentekenherkenning op zonne-energie | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Camera voor kentekenherkenning met bekabelde voeding | Zelfde als Falcon | Android 8.1 |
| **Raven** | Detectie van schoten en noodgeluiden | ESP32-WROOM-32D met Syntiant NDP120-B0 DSP | FreeRTOS / ESP-IDF |
| **Bravo** | Edge-AI-rekenkast | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, kernel 5.4.180** |
| **Picard** | Verouderde rekenkast | Uitgefaseerd en vervangen door Bravo | |
| **Condor** | PTZ-camera | Niet volledig gedocumenteerd | |
| **Alpha** | Autonome drone | Door Flock ontworpen, voldoet aan NDAA | Eigen autopilot |
| **Aerodome M350** | Verouderde drone | DJI Matrice M350 / M300 RTK | DJI-firmware |
| **LPR Trailer (ATS-5)** | Mobiel platform voor kentekenherkenning | Chassis van All Traffic Solutions met een Flock-camera | Zelfde als Falcon |
| **Wing** | Softwarebrug voor camera's van derden | Geen, gebruikt bestaande IP-camera's | |

*Het generatieverschil valt meteen op. De rekenkast draait Android 13, terwijl de camera's die ermee communiceren Android 8.1 gebruiken, een besturingssysteem uit 2017.*

**Falcon verdient aandacht.** Dit apparaat voert de kentekenherkenning uit, draait nog steeds Android 8.1 en slaat gegevens op een **onversleutelde eMMC van 32 GB** op. Op diezelfde eMMC stonden de media en logboeken die het collectief stegan0gram terugvond. Sparrow gebruikt hetzelfde platform met bekabelde voeding.

**Bravo vormt het tegenovergestelde geval.** Een moderne rekenkast met Android 13 en AI-inferentie voor camerafeeds laat zien dat het bedrijf actuele software levert wanneer het daarvoor kiest.

## Geverifieerde CVE-identificaties

Vijftien CVE's zijn toegewezen aan de productfamilies Falcon, Sparrow, Raven en Bravo. Elke identificatie hieronder is in september 2026 gecontroleerd aan de hand van het **CVE.org-record**, en niet overgenomen uit een secundaire bron.

### Detectie van schoten en audioapparaten

| CVE | Bevinding | CVSS |
|-----|---------|------|
| **CVE-2025-47818** | Hardgecodeerd wachtwoord voor een verbinding | 2.2 |
| **CVE-2025-47819** | Debuginterface op de chip met onjuiste toegangscontrole | 6.4 |
| **CVE-2025-47820** | Code opgeslagen als leesbare tekst | 2.0 |
| **CVE-2025-47821** | Hardgecodeerd wachtwoord voor een systeem | 2.2 |

Alle vier zijn van invloed op apparaten voor schotdetectie **vóór versie 1.3**.

### Kentekenlezers

| CVE | Bevinding | CVSS |
|-----|---------|------|
| **CVE-2025-47822** | Debuginterface op de chip met onjuiste toegangscontrole | 6.4 |
| **CVE-2025-47823** | Hardgecodeerd wachtwoord voor een systeem | 2.2 |
| **CVE-2025-47824** | Code opgeslagen als leesbare tekst | 2.0 |

Deze drie zijn van invloed op firmware voor kentekenlezers **tot en met versie 2.2**.

### Applicatiefouten in de hele vloot

| CVE | Bevinding | CVSS |
|-----|---------|------|
| **CVE-2025-59403** | De app Collins stelt beheerendpoints bloot op **poort 8080 zonder authenticatie**: `/reboot`, `/logs`, `/crashpack` en `/adb/enable`. Die laatste start ADB via TCP zonder bevestiging voor foutopsporing, waardoor een aanvaller op hetzelfde netwerk een shell krijgt | **9.8 KRITIEK** |
| **CVE-2025-59407** | De app DetectionProcessing bevat een Java-keystore samen met het **hardgecodeerde wachtwoord**. De keystore bevat een privésleutel | **9.8 KRITIEK** |
| **CVE-2025-59405** | De app Peripheral bevat een DataDog-API-sleutel in leesbare tekst | 7.5 |
| **CVE-2025-59409** | Productiefirmware van Falcon en Sparrow wordt geleverd met **wifi-ontwikkelgegevens in leesbare tekst** | 7.5 |
| **CVE-2025-59406** | De app Pisco bevat een Auth0-**clientgeheim** in leesbare tekst | 6.2 |

### Bravo-rekenkast

| CVE | Bevinding | CVSS |
|-----|---------|------|
| **CVE-2025-59402** | Accepteert de standaard Firehose-loader van Thundercomm TurboX 6490, waarmee firmware kan worden geflasht en partities kunnen worden uitgelezen | 5.4 |
| **CVE-2025-59404** | Wordt geleverd met een ontgrendelde bootloader, waardoor Android Verified Boot wordt omzeild | 7.5 |
| **CVE-2025-59408** | Wordt geleverd met uitgeschakelde Secure Boot | 7.3 |

**Vier van deze kwetsbaarheden hebben een netwerk-aanvalsroute met een score van 7,5 of hoger. Daarvoor is dus geen fysieke toegang nodig.** CVE-2025-59403 is de toegewezen identificatie voor het niet-geauthenticeerde API-pad. Dit pad bevat de aanroep `/adb/enable` waarvan [kritieke kwetsbaarheid 1](#critical-vulnerability-1-button-press-wireless-access-point) afhankelijk is om een root-shell te bereiken.

*De CVE-records zijn om een tweede reden belangrijk. Ze bevestigen het probleem met geheimen in leesbare tekst via onafhankelijke registries en niet alleen via onderzoeksrapporten. De beveiligingswaarschuwingspagina van Flock staat bovendien als referentie bij de Raven- en LPR-records.*

______

## Kritieke kwetsbaarheid 1: draadloos toegangspunt via knopdruk {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Ernst**: KRITIEK (CVSS 9.8)

### De exploit

De meest alarmerende kwetsbaarheid geeft **iedereen met fysieke toegang** tot een Flock Safety-camera binnen 60 seconden volledige controle:

**Stap 1**: Druk **drie keer** op de knop aan de achterkant van een Falcon- of Sparrow-camera
**Stap 2**: Het apparaat maakt een open wifi-toegangspunt aan
**Stap 3**: Maak verbinding met het wifinetwerk (hardgecodeerd wachtwoord: beschreven in de whitepaper van GainSec)
**Stap 4**: Stuur een opdracht om ADB (Android Debug Bridge) in te schakelen
**Stap 5**: Maak via ADB verbinding en verkrijg root-shelltoegang

### Technische details

```
Apparaat: Flock Safety Falcon/Sparrow ALPR-camera
Hardware: Android Things 8.0/8.1 (ondersteuning beëindigd in 2021)
Aanvalsroute: reeks fysieke knopdrukken
Authenticatie: hardgecodeerd WiFi-wachtwoord (voor alle apparaten hetzelfde)
Impact: volledige overname van het apparaat, gegevensdiefstal en installatie van malware
```

### Wat dit mogelijk maakt

Na het verkrijgen van shelltoegang kan een aanvaller:
- **Alle opgeslagen beelden ophalen**, waaronder beelden van mensen en niet alleen voertuigen
- **Bewijsmateriaal op het apparaat aanpassen of verwijderen**
- **Blijvende malware installeren** die herstarts overleeft
- **De apparaatidentiteit klonen** om zich voor te doen als het apparaat
- **Videostreams onderscheppen en aanpassen**
- **Het apparaat als botnetclient gebruiken** voor DDoS-aanvallen
- **Wifi-inloggegevens van apparaten in de buurt vastleggen** met honeypot-aanvallen
- **De camera uitschakelen** of een denial-of-service veroorzaken

### Demonstratie

Beveiligingsonderzoeker Ben Jordan demonstreerde deze exploit op YouTube. De video toont:
- Verbinding met het wifi-toegangspunt in **minder dan 30 seconden**
- Root-shelltoegang in **minder dan 60 seconden in totaal**
- Volledige toegang tot het bestandssysteem, opgeslagen beelden en systeemgeheugen
- De mogelijkheid willekeurige Android-apps te installeren

**Citaat uit de demonstratie**:
> "Het wachtwoord voor dat toegangspunt staat [WEGGELAKT] en bestaat volledig uit kleine letters. Bij elke camera die we hebben getest, is dat hetzelfde hardgecodeerde wachtwoord. Daarna stuur je een opdracht om ADB in te schakelen... je hebt waarschijnlijk in minder dan 30 seconden volledige shelltoegang tot het apparaat."

### Reactie van de leverancier

Flock Safety beweerde aanvankelijk dat de kwetsbaarheid alleen van invloed was op **apparaten die niet met de cloud verbonden waren**. Het bedrijf vergeleek ze met **"een iPhone die van een vrachtwagen is gestolen voordat hij verbinding heeft gemaakt"**.

*Die bewering is weerlegd.* Onderzoekers reproduceerden de kwetsbaarheid **op apparaten die met de cloud verbonden waren**, op meerdere cameramodellen met **dezelfde kwetsbaarheid** en op apparaten uit **verschillende bronnen**. Alle apparaten vertoonden de fout.

______

## Kritieke kwetsbaarheid 2: verouderd Android-besturingssysteem

### CVE-2025-47822 tot en met CVE-2025-47824

**Ernst**: GEMIDDELD tot LAAG (CVSS 6.4, 2.2 en 2.0)

### Het probleem

Flock Safety-camera's draaien **Android Things 8.0 of 8.1**. Google:
- **stopte in 2021 met dit product**
- levert **sinds 2021 geen beveiligingsupdates** meer
- kent **meer dan 900 gepubliceerde kwetsbaarheden** voor deze software, stand 2026
- heeft de ondersteuning **meer dan vijf jaar geleden beëindigd**

### Technische analyse

**Besturingssysteem**: Android Things 8.0/8.1  
**Einde van ondersteuning**: januari 2021  
**Bekende kwetsbaarheden**: meer dan 900  
**Beveiligingspatches**: geen sinds het einde van de ondersteuning  
**Getroffen apparaten**: Falcon, Sparrow, Condor en Bravo-rekenkasten

### Wat de dump van september 2026 laat zien

De bestandssysteemafbeeldingen die in september 2026 zijn gepubliceerd, tonen de exacte versies op een camera die actief in gebruik was. Dit is geen testapparaat.

| Onderdeel | Versie op de camera | Toestand |
|-----------|----------------------|--------|
| **Android** | 8.1, build gedateerd op 5 juni 2025 | Beveiligingspatchniveau **2018-06-05** |
| **Linux-kernel** | 3.18.71 | Uitgebracht in 2017; de 3.18-reeks eindigde in mei 2019 bij 3.18.140 |
| **Huidige Android-versie** | Android 17, juni 2026 | Negen grote versies nieuwer |

De camera-build zelf is recent. Het **besturingssysteem eronder is dat niet**. Het patchniveau laat zien dat het apparaat al **acht jaar geen Android-beveiligingsupdates** heeft ontvangen. De kernel loopt zelfs **69 patchreleases achter** op het einde van zijn eigen onderhoudstak, met meer dan negen jaar aan ontbrekende reparaties.

### Twee kwetsbaarheden in deze build

Micah Lee vond twee publiek bekende fouten in onderdelen die met de camera worden geleverd. De patchdatums tonen aan dat de camera ouder is dan beide oplossingen.

| CVE | Onderdeel | Effect | Opgelost |
|-----|-----------|--------|---------|
| **CVE-2021-1905** | Qualcomm Adreno GPU-stuurprogramma | Use-after-free waardoor **elke code op het apparaat, ook een niet-bevoorrechte app, kernelgeheugen kan beschadigen en volledige controle kan krijgen** | mei 2021 |
| **CVE-2018-9568** "WrongZone" | Afhandeling van sockets in de Linux-kernel | Typeverwarring bij IPv6 waarmee een programma **rechten naar root kan verhogen**. Publieke exploitcode bestaat | december 2018 |

Beide fouten waren al jaren gepatcht voordat de firmware voor deze camera werd gebouwd. **Geen van beide vereist fysieke toegang, want software die al op het apparaat draait, kan ze bereiken.** De nabijheidsbeperking waarmee Flock de bevindingen van GainSec relativeerde, geldt hier niet.

### Vergelijking met consumentenapparaten

Ter vergelijking:
- Een fabrikant stopt na ongeveer vijf jaar met updates voor je **smartphone** en **verkoopt het apparaat niet langer**.
- Een **thuisbewakingscamera** met software die vijf jaar oud is, geldt als **kritiek onveilig**.
- Overheidsinstanties eisen **actuele, ondersteunde software** voor gevoelige systemen.

*Toch blijft Flock Safety camera's inzetten en verkopen met software waarvoor de fabrikant geen ondersteuning biedt, die geen beveiligingspatches ontvangt, honderden bekende exploits bevat en gevoelige gegevens van wetshandhaving verwerkt.*

### Waarom dit van belang is

**Verouderde software zonder ondersteuning** op bewakingsapparaten betekent:
- **Elke gepubliceerde kwetsbaarheid in Android 8.x** werkt mogelijk op deze camera's.
- Voor veel kwetsbaarheden is **exploitcode openbaar beschikbaar**.
- Nieuwe problemen krijgen **nooit meer patches**.
- **Naleving van regelgeving** (FISMA, NIST, CMMC) is onmogelijk.

______

## Kritieke kwetsbaarheid 3: geen versleuteling tijdens gebruik

### CVE-2025-47824 en CVE-2025-59407

**Ernst**: HOOG tot KRITIEK (CVSS 2.0 tot 9.8)

### Beweringen van Flock Safety tegenover de werkelijkheid

**De website van Flock Safety stelt**:
> "Gegevens en beeldmateriaal worden gedurende de volledige levenscyclus versleuteld."

**Onafhankelijke onderzoeksbevindingen** (GainSec en Ben Jordan):
> "Tijdens ons onderzoek hebben we niets ontsleuteld of gekraakt. Alles was tijdens gebruik onversleuteld."

*De marketingclaim staat volledig haaks op de technische werkelijkheid.*

### Wat niet versleuteld is

Bij onderzoek naar de apparaten vonden onderzoekers het volgende **onversleuteld**:
1. **Opgeslagen videobeelden en foto's**
2. **Kentekengegevens en metadata**
3. **Wifi-inloggegevens en API-sleutels**
4. **Databasebestanden met detectierecords**
5. **Netwerkverkeer** (zie kwetsbaarheid 6)
6. **Systeemlogboeken met gevoelige informatie**

### Tegenstrijdigheid over gegevensbewaring

**Claim van Flock Safety**: gegevens worden na 7 dagen automatisch verwijderd.  
**Onderzoeksbevindingen**: onderzoekers vonden beelden van **de fabricage van het apparaat** (maanden of jaren oud).

Fragment uit de whitepaper van GainSec:
> "We vonden afbeeldingen die ouder waren dan 7 dagen. Sommige opgeslagen beelden waren gemaakt toen de camera werd geactiveerd in de fabriek waar het apparaat was geproduceerd."

*Dit betekent dat het apparaat de gecommuniceerde privacyregels niet afdwingt.*

### Gevolgen voor privacy

Deze fout in de versleuteling betekent:
- **Diefstal van het apparaat** leidt direct tot een datalek.
- **Onderschepping van netwerkverkeer** stelt gegevens in leesbare tekst bloot.
- **Insiderrisico's** maken het eenvoudig gegevens weg te sluizen.
- **Bescherming door een bevelschrift** geldt mogelijk niet voor onversleutelde gegevens.
- Er ontstaan **overtredingen van meerdere regels** (HIPAA, CCPA enzovoort).

______

## Kritieke kwetsbaarheid 4: hardgecodeerde inloggegevens in het hele systeem {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 en CVE-2025-59409

**Ernst**: KRITIEK (CVSS 9.8, de hoogste ernstscore)

### Soorten hardgecodeerde geheimen

Beveiligingsonderzoekers ontdekten **uitgebreid gebruik van hardgecodeerde inloggegevens**:

#### 1. Wachtwoorden voor wifi-toegangspunten
- **Eén universeel wachtwoord** voor alle Falcon- en Sparrow-camera's
- **Gebruikers en beheerders kunnen het niet wijzigen**
- **Bekend bij onderzoekers** en opgenomen in de whitepaper (met weggelakte passages)
- **Bevestigd door CVE-2025-59409**: productiefirmware van Falcon en Sparrow (build `OPM1.171019.026`) bevat **wifi-ontwikkelgegevens in leesbare tekst**

#### 2. API-sleutels en tokens
- **Hardgecodeerd in firmware** en toepassingscode
- **Geeft toegang tot backends** van verschillende diensten
- **Gevonden door reverse-engineering** van Android-APK's
- **Bevestigd door de dump van september 2026**: een hardgecodeerde backend-API-sleutel staat in `CameraSettings` in `com.flocksafety.android.common.lib`, een gedeelde bibliotheek die met **alle 19 Flock-apps** op het apparaat wordt meegeleverd
- **De Auth0-client-ID en het geheim staan op de onversleutelde partitie `/persist`** in `flock/auth0/auth0_cred`, een locatie die een fabrieksreset overleeft
- **De camera slaat ontvangen inloggegevens als leesbare tekst op** nadat deze zich bij de Okta Auth0-dienst van Flock heeft geauthenticeerd met zijn eigen MAC-adres

#### 3. Database-inloggegevens
- **SQLite-databases** zonder wachtwoordbeveiliging
- **MySQL- en PostgreSQL-inloggegevens** in configuratiebestanden
- **Rechtstreekse databasetoegang** vanuit een lokale shell

#### 4. Cryptografische keystores
- **Bevestigd door CVE-2025-59407**: de app DetectionProcessing levert een Java-keystore samen met het hardgecodeerde wachtwoord. De keystore bevat een **privésleutel**.
- **Ernst**: KRITIEK (CVSS 9.8), want de sleutel wordt samen met het binaire bestand verspreid dat de sleutel juist moet beschermen.

#### 5. Namen van wifi-netwerken
- Een **lijst met voorkeursnetwerken** staat hardgecodeerd in de firmware.
- Hierdoor zijn aanvallen met **valse toegangspunten** mogelijk (zie kwetsbaarheid 6).

#### 6. Inloggegevens voor clouddiensten
- **AWS- en Azure-tokens** zijn in code ingebed.
- **API-sleutels van derden** (ArcGIS, kaartdiensten)
- **OAuth-tokens** worden nooit vervangen.

### Aanvalsscenario: vals netwerk

Met hardgecodeerde wifi-netwerknamen demonstreerden onderzoekers het volgende:

1. Een aanvaller zet een **vals wifi-netwerk** op met dezelfde hardgecodeerde SSID.
2. De camera **maakt automatisch verbinding** en geeft voorrang aan de hardgecodeerde netwerken.
3. De aanvaller onderschept **al het netwerkverkeer** via een man-in-the-middle-aanval.
4. Inloggegevens in leesbare tekst worden uit het verkeer gehaald.
5. De aanvaller krijgt **toegang tot het backendsysteem**.

**Fysieke toegang tot de camera is niet nodig.** Binnen het bereik van wifi zijn is genoeg.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagram met vijf aanvalsroutes via hardgecodeerde inloggegevens in Flock Safety-camera's, waaronder wifiwachtwoorden, API-sleutels, databasegegevens en tokens voor clouddiensten" >}}

______

## Kritieke kwetsbaarheid 5: geen multifactorauthenticatie

### Falen van organisatorisch beleid

**Ernst**: HOOG (organisatorisch)

### De onthulling

**Flock Safety verplicht sommige wetshandhavingsinstanties niet tot 2FA/MFA**. Het gaat om *dezelfde instanties die dagelijks trackinggegevens over 150 miljoen voertuigen raadplegen*.

Een citaat van een beveiligingsonderzoeker:
> "Toen ik dit voor het eerst ontdekte, kon ik het gewoon niet geloven. Het beveiligingsproces dat je doorloopt wanneer je je aanmeldt bij Disney Plus is voor sommige politiediensten al te veel gevraagd, zelfs wanneer ze vertrouwelijke informatie en de locatie van in sommige gevallen vrijwel iedereen raadplegen."

### Waarom dit van belang is

Zonder MFA/2FA geldt:
- **Eén gestolen wachtwoord** geeft toegang tot het hele systeem.
- **Phishingaanvallen** werken bijzonder goed.
- **Credential stuffing** met gegevens uit andere datalekken werkt.
- **Insiderrisico's** zijn eenvoudiger te benutten.
- **Gestolen apparaten** geven direct toegang.

### Vergelijking

Beveiligingseisen voor **minder gevoelige** systemen:
- **Disney+**: 2FA beschikbaar
- **Gmail**: 2FA standaard voor nieuwe accounts
- **Banken**: 2FA wettelijk verplicht
- **Sociale media**: 2FA is gebruikelijk

Beveiligingseisen voor **systemen die dagelijks meer dan 150 miljoen voertuigen volgen**:
- **Flock Safety**: 2FA optioneel (sommige instanties gebruiken het niet)

### Reactie van een Amerikaanse senator

Deze bevinding werd nadrukkelijk genoemd in **de brief van senator Wyden** met het verzoek om een FTC-onderzoek. De brief stelde dat Flock Safety:
> "gevoelige persoonsgegevens van Amerikanen onnodig heeft blootgesteld aan diefstal door hackers en buitenlandse spionnen"

### Eenvoudige oplossing

**USB- en NFC-beveiligingssleutels** kosten **$10-25** en bieden:
- **Phishingbestendige** authenticatie
- Geen **extra apps** of codes nodig
- Voldoen aan de **FIDO2/WebAuthn-standaard**
- Een **eenvoudige gebruikerservaring** (plug in of tik op het apparaat)

*Als dit "te veel gedoe" is voor personeel van wetshandhaving, **hoort dat personeel geen toegang te hebben** tot nationale bewakingssystemen.*

______

## Kritieke kwetsbaarheid 6: netwerkverkeer in leesbare tekst

### Wacht op toewijzing van een identificatie

**Ernst**: HOOG (door onderzoekers geschatte CVSS 7.8)

**Voor deze categorie is geen CVE-identificatie toegewezen.** Het dichtstbijzijnde toegewezen record, CVE-2025-59406, heeft de CWE-319-classificatie voor overdracht in leesbare tekst. Dat record betreft echter een ingebed Auth0-geheim en niet onderschepping tijdens overdracht. De bevindingen in dit onderdeel zijn nog steeds gebaseerd op de hierboven genoemde onderzoeksrapporten.

### De kwetsbaarheid

Wanneer camera's verbinding maken met een netwerk (LTE of wifi), versturen ze gegevens **zonder voldoende versleuteling**:

**Getroffen verkeer**:
- Kentekenfoto's en tekst
- Detectiemetadata
- Systeemlogboeken
- Configuratiegegevens
- Inloggegevens (in sommige gevallen)

### Aanvalsroute 1: vals wifi-netwerk

Onderzoekers demonstreerden het volgende:
1. Verwijder de simkaart uit de camera **of** maak een vals netwerk met de hardgecodeerde SSID.
2. De camera maakt verbinding met het valse wifi-netwerk.
3. Leg verkeer vast met **Wireshark** of een vergelijkbaar pakketanalyseprogramma.
4. Analyseer het met tools als **NetworkMiner** of **Unblo**.
5. Haal **inloggegevens in leesbare tekst** en gevoelige gegevens eruit.

Citaat uit het onderzoek van GainSec:
> "Ik heb een tijdje de pcap-gegevens vastgelegd die door een van deze camera's werden verzonden. Daarna heb ik ze met Wireshark en Unblo geanalyseerd... en inderdaad, er stonden inloggegevens in leesbare tekst in de gegevens."

### Aanvalsroute 2: IMSI-catcher / Stingray

Voor een geavanceerdere aanval is geen fysieke nabijheid nodig:
1. Gebruik een **IMSI-catcher** (een zelfgebouwd Stingray-apparaat) of een SDR voor professioneel gebruik.
2. **Kaap de LTE-verbinding** door je voor te doen als een zendmast.
3. De camera maakt verbinding met een **vals basisstation**.
4. Onderschep **al het verkeer** met een man-in-the-middle-aanval.
5. Haal inloggegevens, beelden en metadata eruit.

**Fysieke toegang is niet nodig.** Dit werkt vanaf **honderden meters afstand**.

### Mogelijkheden voor moderne Tempest-aanvallen

Doordat gegevens in leesbare tekst worden verzonden, zijn ook **Tempest-achtige aanvallen** mogelijk:
- RF-emissies van de camera kunnen worden opgevangen.
- De videostream kan **op afstand worden gereconstrueerd**.
- De techniek lijkt op methoden van de **CIA tijdens de Koude Oorlog**.
- Moderne SDR-apparatuur maakt dit **toegankelijk voor hobbyisten**.

______

## Kritieke kwetsbaarheid 7: openbare camerafeeds blootgesteld

### Ontdekking in januari 2026

**Ernst**: KRITIEK (CVSS 10.0, volledig systeem blootgesteld)

### De ontdekking

In januari 2026 ontdekten Ben Jordan en **404 Media** dat ze met **eenvoudige Google-zoekopdrachten** het volgende konden vinden:
- **Meer dan 60 volledig blootgestelde** beheerinterfaces van Flock Safety-camera's
- **Geen gebruikersnaam of wachtwoord nodig**
- **Livevideostreams** en 30 dagen aan opgeslagen beelden
- Toegang tot **het volledige camerabedieningspaneel**

### Wat toegankelijk was

Via deze blootgestelde interfaces kon iedereen:
- **Livevideofeeds** bekijken
- **Beelden van 30 dagen** terugkijken
- Videobestanden rechtstreeks **downloaden**
- **PTZ-camera's** (draaien, kantelen en zoomen) van Condor-apparaten bedienen
- **Bestandspaden en hashes** van bewijsmateriaal zien
- Bewijsmateriaal met één klik **verwijderen**
- Camera-instellingen **wijzigen**
- Serienummers en locaties van apparaten **bekijken**

### Waargenomen privacyschendingen

Ben Jordan legde vast dat hij het volgende zag:
- **Een gezin dat een baby in een auto zette** op de parkeerplaats van Lowe's
- **Een man die 's ochtends zijn huis verliet** in New York
- **Een vrouw die alleen jogde** op een bospad in Georgia
- **Een stel dat ruzie maakte** op een straatmarkt in Atlanta (AI zoomde automatisch in op gezichten)
- **Een agent en ambulancepersoneel** die een psychische crisis hielpen oplossen in Iowa
- **Kinderen die speelden** op een speelplaats in de San Francisco Bay Area
- **Een man op een schommel** in een leeg park tijdens een privé-moment

Citaat van Ben Jordan:
> "Alleen al hardop zeggen maakt me misselijk. Ik probeer je maar een fractie te laten zien van de informatie die iedereen ter wereld met toegang tot een commerciële zoekmachine de afgelopen 31 dagen over bezoekers van die markt of wandelaars op dat pad kon vinden."

### Mogelijkheden om mensen te volgen

De blootgestelde Condor-PTZ-camera's bieden **AI-gestuurde tracking**:
- Automatisch **inzoomen op mensen**
- **Personen volgen** terwijl ze bewegen
- **Smartphones detecteren en erop scherpstellen** (om schermen te lezen)
- Meerdere doelen tegelijk **volgen**
- Zonder toezicht **continu opnemen**

### Risico op doxing

Ben Jordan toonde hoe eenvoudig blootgestelde beelden naar identiteiten leiden:
> "Binnen twee minuten OSINT met een commerciële gezichtsherkenningsdienst ontdekte ik dat een van hen net de medische opleiding had afgerond en de ander chronische prikkelbaredarmsyndroomklachten heeft. Het stel heeft vorig jaar ook een baby gekregen... Ik weet ook dat ze ruim 45 minuten van hun adres in de buitenwijken hebben gereden."

Koppel gegevens aan:
- **Gezichtsherkenningsdiensten**
- Profielen op **sociale media**
- Databases met **openbare gegevens**
- Informatie uit **datalekken** (zoals Park Mobile)
- **Logboeken van noodoproepen** (veel steden publiceren die)

Resultaat: **volledige de-anonimisering binnen enkele minuten**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Overzichtsdiagram van blootgestelde Flock Safety-PTZ-camera's met automatische AI-tracking die openbare toegang gaf tot livebeelden van mensen in parken, op paden en parkeerplaatsen" >}}

______

## Kritieke kwetsbaarheid 8: onbevoegde gegevensverzameling

### Tegenstrijdigheid met openbare verklaringen

**Ernst**: HOOG (gevolgen voor privacy en wetgeving)

### Beweringen van Flock Safety

**Verklaring op de officiële website**:
> "Flock Safety legt geen gegevens van mensen vast, alleen van voertuigen."

### Onafhankelijke onderzoeksbevindingen

**Wat de camera's werkelijk doen**:
1. **Bewegingsdetectie** activeert de camera **bij alles**, niet alleen bij voertuigen.
2. De **AI zoekt op de afbeelding naar een kenteken**.
3. **Zonder gevonden kenteken** wordt de afbeelding **nog steeds opgeslagen** en niet verwijderd.
4. Een **aparte map** bewaart afbeeldingen zonder kenteken.
5. Beelden van **mensen, voetgangers en fietsers** worden vastgelegd en bewaard.

*De bewering "alleen voertuigen" klopt niet. De camera bewaart beelden van iedereen die ervoor langsloopt.*

### Geverifieerde waarnemingen

Onderzoekers legden vast dat camera's het volgende fotografeerden:
- **Een persoon die voor de camera liep** (afbeelding opgeslagen)
- **Een hand die naar de lens zwaaide** (afbeelding opgeslagen)
- **Een bureau of voorwerp dat bij de camera werd verplaatst** (afbeelding opgeslagen)
- **Fabrieksmedewerkers** in de productielocatie (maandenlang bewaard)

Citaat van GainSec:
> "Toen ik voor de camera liep, activeerde de radarmodule de cameramodule om een foto van mij te maken. Daarna zocht de ingebouwde AI naar een kenteken en vond er geen, maar de camera sloeg de afbeelding toch op in een aparte map."

### Juridische gevolgen

Deze onbevoegde gegevensverzameling kan:
- **Gepubliceerde privacyregels schenden** (misleidende handelspraktijken)
- **Aanbestedingscontracten schenden** (als steden "alleen voertuigen" hadden vastgelegd)
- Overtredingen van **GDPR/CCPA** veroorzaken (EU-burgers, inwoners van Californië)
- **Toestemmingsovereenkomsten ongeldig maken**
- Het bedrijf blootstellen aan rechtszaken wegens **misleidende reclame**

### Uitbreiding van de surveillance

De **Condor-PTZ-camera's** (ingezet in 2025-2026) zijn **uitdrukkelijk ontworpen** om mensen te volgen:
- **AI-gestuurde persoonsdetectie**
- Automatisch **inzoomen op gezichten**
- Mensen **blijven volgen** wanneer ze bewegen
- **Geen mogelijkheid om bezwaar te maken**
- Vaak geplaatst bij **parken, wandelpaden en OV-stations**

*Dit is een enorme uitbreiding van "kentekenlezers" naar surveillance van de gehele bevolking, zonder beleidswijziging, nieuwe contracten of openbare kennisgeving.*

______

## Kritieke kwetsbaarheid 9: blootgestelde USB-poorten voor Rubber Ducky-aanvallen

### Misbruik van fysieke toegang

**Ernst**: HOOG (met fysieke toegang)

### De kwetsbaarheid

**Bravo-rekenkasten** en sommige cameramodellen hebben:
- **Blootgestelde USB-C-poorten** aan de buitenkant
- **Geen fysieke beveiliging** (afdichting van de behuizing)
- **Automatische uitvoering** van USB-apparaten
- **Geen authenticatie** nodig

### Rubber Ducky- of BadUSB-aanval

Een **BadUSB-apparaat** (kost $5-15):
- Verschijnt voor het systeem als **USB-toetsenbord**
- **Voert vooraf geprogrammeerde scripts uit** (payloads)
- **Start automatisch** wanneer het wordt aangesloten
- Vereist **geen interactie van een gebruiker**

### Aanvalsscenario

GainSec demonstreerde het volgende:
1. Benader een geplaatst Flock-apparaat.
2. Sluit een **BadUSB-apparaat** aan op de blootgestelde poort.
3. Het apparaat voert de payload (het script) uit.
4. De payload installeert **blijvende malware**.
5. De aanvaller **loopt weg**.
6. De malware **maakt via LTE/wifi verbinding met de aanvaller**.

**Totale tijd**: minder dan 30 seconden

### Wat payloads kunnen doen

Automatische scripts kunnen:
- Een **draadloos toegangspunt inschakelen** (knopdrukken omzeilen)
- Een **achterdeur installeren** voor toegang op afstand
- Gegevens **naar een externe server sluizen**
- Beelden of bewijsmateriaal **aanpassen**
- De camera **uitschakelen** of een denial-of-service veroorzaken
- Het apparaat aan een **botnet toevoegen** voor DDoS-aanvallen
- Inloggegevens van andere systemen **vastleggen**

### Waarom dit van belang is

Bij **meer dan 80.000 camera's**, vaak op **semi-landelijke locaties** met **beperkt zicht**:
- Is **fysieke toegang** relatief eenvoudig.
- Zijn er **geen bewakers of voortdurend toezicht**.
- Zijn apparaten bevestigd met **eenvoudige slangklemmen**.
- Hangen ze vaak op **2,1 meter hoogte** (bereikbaar met een opstapje).

Citaat van Ben Jordan:
> "Deze camera's zijn geen ondoordringbare forten. Het zijn plastic Android-camera's en rekenkasten, met slangklemmen op 2,1 meter hoogte bevestigd."

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Aanvalsdiagram dat toont hoe een BadUSB-apparaat op de blootgestelde USB-poort van een Flock Safety-camera in minder dan 30 seconden blijvende malware installeert" >}}

______

## Kritieke kwetsbaarheid 10: openbaar blootgestelde API-sleutels

### Ontdekt door een OSINT-onderzoeker

**Ernst**: KRITIEK (CVSS 9.5)

### De ontdekking

In 2025 ontdekte **OSINT-onderzoeker Joshua Michael** het volgende:
- Een **blootgestelde demowebsite van Flock Safety** via Google-dorking
- **5.000 regels broncode** die zichtbaar waren
- Een **actieve API-sleutel** in de code
- Toegang tot **meer dan 50 privé-geolagen**

### Waartoe de API-sleutel toegang gaf

De blootgestelde **ArcGIS-API-sleutel** gaf toegang tot:

**1. Registratiegegevens**
- Namen van klanten
- E-mailadressen
- Aantal camera's per locatie
- Bestandsbijlagen toevoegen

**2. Liveposities van politieauto's** (meerdere diensten)
- Realtime GPS-tracking van politievoertuigen
- Inzet in Aurora, Colorado
- Politiedienst van Carrollton
- **Risico voor de nationale veiligheid**

**3. Persoonsgegevens van agenten**
- Namen en telefoonnummers
- E-mailadressen
- Verwachte patrouillegebieden
- Thuisjurisdicties

**4. Database met hotlistmeldingen** (Dallas, Texas)
- **6.000 records** van gemarkeerde voertuigen
- Kentekens en redenen voor meldingen
- Detectielocaties en tijdstempels
- Camera-ID's die voertuigen hebben vastgelegd
- **Vijf maanden aan verplaatsingstracking**

Citaat van Joshua Michael:
> "Iedereen kon deze kaart via Google vinden en de bewegingspatronen van deze mensen over vijf maanden volgen. Ook bevat de reden-categorie iemand die alleen als 'verdachte' is aangeduid, terwijl veel andere records helemaal geen reden bevatten."

### Aanvalsoppervlak

Blootgestelde API-sleutels maken het volgende mogelijk:
- Specifieke voertuigen **stalken**
- De **veiligheid van agenten** aantasten (woonadressen, patrouillepatronen)
- De **operationele beveiliging** schenden (waar de politie wel of niet is)
- **Getuigen intimideren** (mensen volgen die misdrijven hebben gemeld)
- **Criminele inlichtingen** verzamelen voor georganiseerde misdaad

### Context van het datalek: Flax Typhoon

Enkele weken voordat dit werd ontdekt, had de **door de Chinese staat gesteunde** hackgroep **Flax Typhoon** volgens beveiligingsonderzoekers Alexa Feminina en James Zhang ArcGIS gecompromitteerd.

Citaat van InfoSecurity Magazine:
> "De hackers zouden een legitieme, openbaar toegankelijke ArcGIS-toepassing hebben aangevallen... die werd gebruikt voor herstel na rampen, noodbeheer en andere kritieke functies."

**Dit betekent dat vijandige natiestaten mogelijk toegang hadden tot** politievoertuiglocaties, identiteiten van agenten, locaties van bewakingscamera's en noodhulppatronen.

______

## Aanvullende kwetsbaarheden (samenvatting van meer dan 50)

### Kwetsbaarheden 11-51

De whitepaper van GainSec documenteert **41 aanvullende bevindingen**, waaronder:

**Fouten in het systeemontwerp**:
- Debugmodus ingeschakeld in productiefirmware
- Onveilig opstartproces maakt compromittering van de bootloader mogelijk
- Geen secure element of TPM voor sleutelopslag
- Voorspelbaar mechanisme voor firmware-updates

**Problemen met authenticatie**:
- Sessietokens verlopen nooit
- Geen toegangsbeperkingen op basis van IP-adres
- Inloggegevens gedeeld tussen apparaatvloten
- Geen certificate pinning

**Netwerkbeveiliging**:
- Open poorten met debugdiensten
- Telnet ingeschakeld op sommige apparaten
- FTP-servers met zwakke inloggegevens
- Kwetsbaarheden voor DNS-rebinding

**Privacy en gegevensbewaring**:
- Beelden langer bewaard dan aangegeven
- Metadata wordt nooit verwijderd
- Gegevens voor gezichtsherkenning verzameld
- Locaties gevolgd, ook buiten voertuiggegevens

**Fysieke beveiliging**:
- Behuizingen eenvoudig te demonteren
- Seriële interfaces blootgesteld
- JTAG-debugpoorten toegankelijk
- Geen zegels die manipulatie aantonen

**Cryptografische fouten**:
- Zwakke generatie van willekeurige getallen
- Hardgecodeerde versleutelingssleutels
- MD5 nog gebruikt in hashketen
- Certificaatvalidatie uitgeschakeld

**Informatielekkage**:
- Uitgebreide foutmeldingen onthullen interne gegevens
- Directoryvermelding ingeschakeld op webservers
- Opmerkingen in broncode bevatten inloggegevens
- Configuratieback-ups voor iedereen leesbaar

### CVE-status

Per mei 2026:
- **22 CVE's toegewezen** en gepubliceerd
- **8 CVE's wachten** op toewijzing door MITRE
- **21 bevindingen** niet ingediend voor een CVE (keuze van onderzoeker)
- **Alle bevindingen** staan in de whitepaper van GainSec

Volledige technische details: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Reactie van Flock Safety

### Officiële verklaringen

**Blogbericht van november 2025**:
> "Flock zet zich in voor voortdurende verbetering van de beveiliging... Geen van de kwetsbaarheden in het rapport heeft invloed op het vermogen van onze klanten om hun doelen op het gebied van openbare veiligheid te bereiken."

**Bewering**: voor de kwetsbaarheden is fysieke toegang en "grondige kennis" nodig.

**Tegenbewijs**:
- Voor de blootgestelde camerafeeds was **alleen een Google-zoekopdracht** nodig.
- Voor draadloze exploits was **alleen nabijheid** nodig.
- De API-sleutel was **volledig op afstand** blootgesteld.
- Na openbaarmaking waren de hardgecodeerde wachtwoorden **algemeen bekend**.

### Onderzoeksapparaten afgedaan

Flock beweerde eerst dat onderzoeksapparaten:
> "Niet met de cloud verbonden waren... zoals een iPhone die van een vrachtwagen is gestolen voordat hij ooit verbinding heeft gemaakt."

*Dit is onjuist gebleken.* Onderzoekers testten **apparaten die met de cloud verbonden waren** en kregen dezelfde resultaten. Publiek bereikbare camera's vertoonden **dezelfde kwetsbaarheden**. 404 Media vond **meer dan 60 blootgestelde productiecamera's**.

### Reactie op onderzoekers

GainSec meldde dat pogingen tot verantwoorde openbaarmaking leidden tot:
- **Een bug bounty met geheimhoudingsverklaring** (die openbaarmaking aan banden legde)
- **Geen bevestiging** van oplossingen
- Een **PR-verklaring** voordat de periode van 90 dagen was verstreken
- **Geen erkenning** van de onderzoeker in de PR
- **Verlies van werk** voor de onderzoeker binnen 48 uur na publicatie van de video

Ben Jordan meldde:
- **Politiebezoeken** aan zijn woning
- **Vermoedelijke privédetectives** die zijn huis fotografeerden
- **Intimidatie door buren**
- Dreigementen met een **sommatie** van Flock Safety

Citaat van Ben:
> "Ik zie dit niet als gevolgen of straf voor onderzoek naar beveiligingskwetsbaarheden. Ik zie dit als gevolgen en straf omdat ik dat op ethische en transparante wijze heb gedaan."

### Voortgezette inzet

*Ondanks dit alles* blijft Flock Safety:
- **Kwetsbare apparaten verkopen**
- **Geen firmware-updates leveren** die de hoofdoorzaken aanpakken
- **Android Things 8.x gebruiken** (ondersteuning beëindigd in 2021)
- **MFA niet verplicht stellen** voor wetshandhaving

______

## Wetgevende en beleidsreactie

### Verzoek om onderzoek door de Amerikaanse Senaat

**Februari 2026**: senatoren **Ron Wyden** (Oregon) en **Raja Krishnamoorthi** (Illinois) stuurden de FTC een officiële brief met het verzoek om onderzoek.

**Fragment uit de brief**:
> "Flock heeft gevoelige persoonsgegevens van Amerikanen onnodig blootgesteld aan diefstal door hackers en buitenlandse spionnen."

**Aangehaalde redenen**:
- Risico's voor de nationale veiligheid
- Misleidende privacyclaims
- Onvoldoende beveiligingsmaatregelen
- Geen verplichte MFA

### Acties van gemeenteraden

**Denver, Colorado**:
- De gemeenteraad **stemde tegen** verlenging van het Flock-contract (december 2025).
- De raad noemde Flocks **"gebrek aan eerlijkheid en verantwoordingsplicht"**.
- De burgemeester **blokkeerde het besluit** via een "deal achter gesloten deuren" (januari 2026).
- De publieke verontwaardiging duurt voort.

**Evanston, Illinois**:
- Ontdekte dat **ICE de camera's zonder toestemming gebruikte**.
- Stemde voor het **verwijderen van de camera's**.
- *Flock plaatste de camera's zonder toestemming opnieuw terug.*
- De stad besteedt belastinggeld aan het **afdekken van camera's** en onderneemt juridische stappen.

**Oakland, Californië**:
- Stelde de stemming over een uitbreiding van **$2,25 miljoen** uit.
- Liet een onafhankelijke beveiligingsaudit uitvoeren.
- De audit vond de beweringen van Flock over effectiviteit **misleidend**.

### Verzoeken om openbare documenten

Meerdere steden voeren onderzoek uit op basis van:
- Openbaar beveiligingsonderzoek
- FOIA-verzoeken om Flock-contracten
- Eisen voor onafhankelijke audits
- Druk van belangenbehartigers uit de gemeenschap

______

## Technische analyse: aanvalsscenario's uit de praktijk

### Scenario 1: surveillance door een natiestaat

**Dreigingsactor**: buitenlandse inlichtingendienst

**Doel**: overheidsfunctionarissen volgen

**Methode**:
1. Gebruik een IMSI-catcher om LTE-verkeer van de camera te onderscheppen.
2. Haal inloggegevens in leesbare tekst uit de stroom.
3. Benader de backend met gecompromitteerde API-sleutels (of een eerder blootgestelde ArcGIS-laag).
4. Doorzoek de database op voertuigen die bij overheidsgebouwen horen.
5. Volg verplaatsingen van functionarissen en militair personeel.

**Uitvoeringstijd**: dagen (zodra de infrastructuur klaarstaat)  
**Kans op detectie**: laag (versleutelde C2, lijkt op legitiem verkeer)

### Scenario 2: tegen-surveillance door georganiseerde misdaad

**Dreigingsactor**: drugsorganisatie

**Doel**: politiepatrouillepatronen vaststellen

**Methode**:
1. Koop een BadUSB-apparaat ($15).
2. Rijd naar camera's in het eigen werkgebied.
3. Sluit de BadUSB aan op de blootgestelde USB-poort (30 seconden).
4. De payload schakelt de camera uit of past beelden aan.
5. Alternatief: de payload stuurt trackinggegevens van politievoertuigen naar een externe server.

**Uitvoeringstijd**: 30 seconden per camera  
**Kans op detectie**: laag (lijkt op activiteit van een legitiem apparaat)

### Scenario 3: stalker of huiselijk geweld

**Dreigingsactor**: gewelddadige voormalige partner

**Doel**: bewegingen van het slachtoffer volgen

**Methode**:
1. Verkrijg het kenteken van het slachtoffer (openbare informatie).
2. Zoek met Google naar een blootgestelde interface van een Flock-camera (kwetsbaarheid uit januari 2026).
3. Doorzoek 30 dagen beeldmateriaal op verschijningen van het voertuig.
4. Vergelijk dit met openbare databases (werkadres, woning enzovoort).
5. Stel dagelijkse patronen en tijdstippen vast.

**Uitvoeringstijd**: minuten tot uren  
**Kans op detectie**: nul (er zijn geen authenticatielogboeken)

### Scenario 4: bewijsmateriaal manipuleren

**Dreigingsactor**: verdachte in een strafzaak

**Doel**: bewijsmateriaal vernietigen voordat de zaak voorkomt

**Methode**:
1. Ontdek de cameralocatie via gegevens uit een gerechtelijk bevel.
2. Verkrijg fysieke toegang tot de camera (knopcombinatie).
3. Verkrijg een root-shell.
4. Navigeer naar de map met bewijsmateriaal.
5. Verwijder specifieke foto's/video's of pas tijdstempels aan.

**Uitvoeringstijd**: minder dan 5 minuten  
**Kans op detectie**: laag (tenzij de camera forensisch wordt onderzocht voordat de verdediging toegang krijgt)

### Scenario 5: privacyactivist of journalist

**Dreigingsactor**: voorvechter van transparantie

**Doel**: buitensporige surveillance documenteren

**Methode**:
1. Gebruik detectieapparaten (zie onze [hardwaregids Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)).
2. Breng cameralocaties in de gemeenschap in kaart.
3. Dien FOIA-verzoeken in over beleid voor beeldmateriaal.
4. Demonstreer kwetsbaarheden aan de gemeenteraad.
5. Pleit voor verwijdering of toezicht.

**Uitvoeringstijd**: doorlopend  
**Kans op detectie**: hoog (openbare activiteit)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrix die vijf praktijkaanvallen op Flock Safety-camera's vergelijkt, waaronder surveillance door een natiestaat, tegen-surveillance door georganiseerde misdaad, stalking, manipulatie van bewijsmateriaal en belangenbehartiging voor privacy" >}}

______

## Bescherming tegen deze kwetsbaarheden

### Voor wetshandhavingsinstanties

**Directe acties**:
1. **Verplicht MFA/2FA** voor alle gebruikers (USB-beveiligingssleutels).
2. **Controleer maandelijks toegangslogboeken** op onbevoegde zoekopdrachten.
3. **Beperk gegevensdeling** tot de minimaal benodigde jurisdicties.
4. **Isoleer netwerken**: plaats camera's op afzonderlijke VLAN's.
5. **Beveilig fysiek**: gebruik zegels die manipulatie aantonen en houd toezicht op camera's.
6. Stel een **incidentresponsplan** op voor compromittering.

**Contractuele eisen**:
1. **Regelmatige beveiligingsaudits** door onafhankelijke bedrijven.
2. **Verplichte firmware-updates** binnen 30 dagen na publicatie van een patch.
3. **Melding van CVE's** binnen 24 uur.
4. **Versleutelde opslag van bewijsmateriaal** met sleutels die de klant beheert.
5. **Boetes volgens de SLA** voor beveiligingslekken.
6. **Auditrecht** voor locaties en code van leveranciers.

**Langetermijnstrategie**:
1. **Overgangsplan** weg van besturingssystemen zonder ondersteuning.
2. **Zelfgehoste infrastructuur** (minder afhankelijkheid van de cloud).
3. **Open-sourcealternatieven** beoordelen.
4. **Transparantie richting de gemeenschap** over cameralocaties en beleid.

### Voor Flock Safety (aanbevelingen)

**Kritieke prioriteit** (direct):
1. **Schakel het maken van draadloze toegangspunten via knopdruk uit**.
2. **Verplicht MFA** voor alle gebruikersaccounts, zonder uitzonderingen.
3. **Vervang alle hardgecodeerde inloggegevens** in het hele systeem.
4. **Patch onmiddellijk de blootgestelde openbare interfaces**.
5. **Versleutel gegevens in rust** en beheer sleutels op de juiste manier.

**Hoge prioriteit** (30 dagen):
1. **Migreer naar een ondersteund besturingssysteem** (Android 12+ of Linux).
2. **Start een bug-bountyprogramma zonder geheimhoudingsverklaringen**.
3. **Laat een externe beveiligingsaudit uitvoeren** en publiceer de resultaten.
4. **Versleutel netwerkverkeer end-to-end**.
5. **Verbeter fysieke beveiliging** (verwijder blootgestelde USB-poorten en versterk behuizingen).

**Gemiddelde prioriteit** (90 dagen):
1. **Ontwerp het authenticatiesysteem volledig opnieuw**.
2. **Gebruik Secure Boot** met geverifieerde firmware.
3. **Integreer een hardwarebeveiligingsmodule**.
4. **Haal compliancecertificeringen** (FedRAMP, SOC 2, ISO 27001).
5. **Bied klanten een beveiligingsdashboard** met meldingen van datalekken.

**Lange termijn** (1 jaar):
1. **Maak beveiligingscomponenten opensource** (om vertrouwen op te bouwen).
2. **Voer adversarial testing uit** (red team).
3. **Stel eisen aan functies voor beveiligingstechniek**.
4. **Integreer beveiliging in de SDLC** (DevSecOps).
5. Neem deel aan **industriestandaarden** (OWASP, CIS).

### Voor particulieren

**Beschermingsstrategieën**:
1. **Gebruik detectieapparaten** (zie onze [hardwaregids](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)).
2. **Breng cameralocaties in jouw omgeving in kaart**.
3. **Wissel routes en tijdstippen af** om patroonanalyse te beperken.
4. Pleit bij de **gemeenteraad** voor toezicht en transparantie.
5. Dien waar wettelijk toegestaan **FOIA-verzoeken** in voor jouw gegevens.
6. Steun **privacywetgeving** op staats- en federaal niveau.

**OpSec-maatregelen**:
1. **Vermijd opvallende voertuigen** (kies een gangbaar merk, model en kleur).
2. Gebruik waar dat wettelijk is toegestaan **verschillende voertuigen** voor gevoelige activiteiten.
3. Kies **ander vervoer** (fiets, openbaar vervoer, lopen).
4. Gebruik **privacygerichte kentekenhoezen**, alleen als die in jouw jurisdictie legaal zijn.
5. Gebruik **Faradaytassen** voor telefoons wanneer koppeling van gegevens een risico vormt.

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Geprioriteerde herstelroutekaart met directe beveiligingsoplossingen, oplossingen binnen 30 en 90 dagen en langetermijnmaatregelen voor Flock Safety" >}}

______

## Het onderzoeksteam

### GainSec (Jon "GainSec" Gaines)

**Achtergrond**: professional in offensieve beveiliging, meer dan 10 jaar ervaring

**Bijdrage**:
- Ontdekte **47 van de 51** kwetsbaarheden
- Publiceerde een **officiële whitepaper** met technische details
- Coördineerde **verantwoorde openbaarmaking** met Flock Safety
- Registreerde **30 CVE's** (22 gepubliceerd, 8 in behandeling)
- Maakte een **controlelijst voor verdedigers** voor beveiligingsprofessionals

**Contact**: whitepaper@gainsecmail.com  
**Onderzoek**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)  
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Achtergrond**: journalist, muzikant en technologieonderzoeker

**Bijdrage**:
- **Video's van kwetsbaarheden** gemaakt
- **Openbare demonstraties** voor journalisten (The Guardian, 404 Media)
- Ontdekte via Google **meer dan 60 blootgestelde camerafeeds**
- **Belangenbehartiging en publieke voorlichting**
- **Wetgevende afstemming** met senatoren

**Contact**: via het YouTube-kanaal  
**Werk**: YouTube - Benn Jordan

### Joshua Michael (Next AI)

**Achtergrond**: OSINT-specialist en privacyonderzoeker

**Bijdrage**:
- Ontdekte via Google-dorking **blootgestelde API-sleutels**
- Documenteerde **blootgestelde ArcGIS-lagen**
- Legde de **OSINT-methoden voor trackingonderzoek** vast
- **Combineerde gegevens** met openbare datalekken

**Organisatie**: Next AI - inlichtingenbureau dat alle bronnen gebruikt

### Andere bijdragers

- **404 Media**: onderzoeksjournalistiek en openbaarmaking
- **The Guardian**: internationale berichtgeving
- **Lucy Parsons Labs**: jarenlang belangenwerk en onderzoek naar ALPR
- **Sassy South**: gemeenschapsorganisatie en transparantie
- **DeFlock / Will Freeman**: project om cameralocaties in kaart te brengen
- **Ed Vogel**: juridische en beleidsanalyse

______

## Ethische overwegingen

### Tijdlijn voor verantwoorde openbaarmaking

De beveiligingsgemeenschap volgde de beste praktijken voor **verantwoorde openbaarmaking**:

**Standaardprotocol**:
1. Ontdek de kwetsbaarheid.
2. **Meld deze 90 dagen privé** aan de leverancier.
3. De leverancier ontwikkelt en verspreidt een patch.
4. **Maak de kwetsbaarheid openbaar** na de patch of na 90 dagen (wat het eerst komt).
5. Publiceer een gedetailleerde beschrijving om verdedigers te helpen.

**Wat er werkelijk gebeurde**:
1. GainSec ontdekte kwetsbaarheden (eind 2024).
2. **Nam herhaaldelijk contact op** met Flock Safety (vanaf februari 2025).
3. Flock bood een **bug bounty met geheimhoudingsverklaring** aan.
4. Flock publiceerde vroeg een **PR-verklaring** zonder de onderzoeker te erkennen.
5. Er kwam **geen bevestiging** dat patches waren uitgerold.
6. GainSec maakte de kwetsbaarheden **openbaar** nadat de perioden van 90 dagen waren verstreken.
7. Ben Jordan en 404 Media **controleerden de bevindingen onafhankelijk** op productiesystemen.

### Vergelding tegen onderzoekers

GainSec en Ben Jordan meldden allebei:
- **Verlies van werk** of problemen met hun dienstverband
- **Politiebezoeken** aan privéwoningen
- **Vermoedelijke surveillance** van woningen en eigendommen
- **Intimidatie door buren**
- Dreigementen met een **sommatie**
- **Aanvallen op sociale media** (de CEO van Flock noemde hen "terroristen")

Dit **afschrikkende effect** op beveiligingsonderzoek:
- Ontmoedigt het melden van kwetsbaarheden
- Vertraagt kritieke beveiligingsoplossingen
- Schaadt de openbare veiligheid
- Schendt de ethische normen van de beveiligingsgemeenschap

*De reactie van Flock Safety op onderzoekers die de meldprocedures volgden, schept een gevaarlijk precedent voor de hele beveiligingsonderzoeksgemeenschap.*

Citaat van Ben Jordan:
> "Ik heb niet de luxe om nog maanden aan weer een kwetsbaarheid in Flock Safety te besteden. Zoals je ziet, is deze dringend en eerlijk gezegd ben ik bang dat er al misbruik van wordt gemaakt."

### Het publieke belang

Deze onderzoekers handelden **in het publieke belang** door:
- De protocollen voor **verantwoorde openbaarmaking** te volgen
- De leverancier **vooraf te informeren**
- Gevoelige details die misbruik mogelijk maken **weg te laten**
- **Richtlijnen voor verdediging** te publiceren
- Via de juiste kanalen **beleidswijzigingen te bepleiten**
- Persoonlijk risico te **aanvaarden** om het publiek te informeren

Zonder hun werk:
- zouden **meer dan 80.000 kwetsbare camera's** zonder oplossing blijven
- zouden **meer dan 150 miljoen dagelijkse voertuigscans** onbeschermd blijven
- zouden **miljoenen Amerikanen** onbewust risico lopen
- zou de **nationale veiligheid** in gevaar komen
- zou er **geen wetgevende actie** lopen

______

## Conclusie: de weg vooruit

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Tijdlijndiagram met het meldingsproces van kwetsbaarheden in Flock Safety tussen 2024 en 2026, van ontdekking via verantwoorde openbaarmaking tot de voortdurende blootstelling van niet-gepatchte systemen" >}}

### Huidige stand (mei 2026)

- **Meer dan 50 kritieke kwetsbaarheden** gedocumenteerd en gedeeltelijk openbaar gemaakt
- **Meer dan 80.000 camera's** blijven in gebruik met niet-gepatchte fouten
- De leverancier heeft **geen volledige herstelmaatregelen** getroffen
- **Beperkte wettelijke actie** (om een FTC-onderzoek is gevraagd, maar het is niet gestart)
- **Risico op voortgezet misbruik** met gevolgen voor nationale veiligheid en persoonlijke privacy

### Wat moet er gebeuren

**In de hele sector**:
1. **Verplichte beveiligingsaudits** vóór inzet door overheidsinstanties
2. **Onafhankelijke tests** door gekwalificeerde derde partijen
3. **Openbare publicatie** van auditresultaten
4. **Aansprakelijkheid van leveranciers** voor beveiligingsfouten
5. **Naleving van standaarden** (NIST, ISO enzovoort)

**Specifiek voor Flock Safety**:
1. **Breng direct noodpatches uit** voor kritieke kwetsbaarheden.
2. **Migreer het besturingssysteem** naar een ondersteund platform.
3. **Erken de volledige omvang** publiekelijk.
4. **Vergoed getroffen onderzoekers**.
5. **Publiceer transparantierapporten** over de beveiliging.

**Wetshandhaving**:
1. Neem **beveiligingseisen** op in aanbestedingscontracten.
2. **Controleer ingezette systemen regelmatig**.
3. **Verplicht MFA** voor alle gebruikers.
4. Stel **incidentresponsplannen** op.
5. Wees **transparant tegenover de gemeenschap** over surveillanceprogramma's.

**Wetgevers**:
1. Stel **federale standaarden** vast voor bewakingstechnologie.
2. Verplicht **melding van kwetsbaarheden** aan getroffen partijen.
3. Bescherm **klokkenluiders en beveiligingsonderzoekers**.
4. Bied **burgerrechtelijke verhaalsmogelijkheden** voor privacyschendingen.
5. Stel **toezichtmechanismen** in voor bewakingssystemen.

### Het grotere beeld

Deze casus gaat over **meer dan alleen Flock Safety**. De casus staat symbool voor:
- Een **bewakingssector** die groei boven beveiliging stelt
- **Overheidsaanbestedingen** zonder voldoende technische expertise
- **Beweringen van leveranciers** blijven onbeantwoord en ongecontroleerd
- **Financiële prikkels** die niet aansluiten bij de openbare veiligheid
- **Regelgevingslacunes** bij het toezicht op nieuwe technologie

*Elke stad die een Flock-contract afsluit zonder onafhankelijke beveiligingscontrole aanvaardt deze risico's namens haar inwoners.*

### Oproep tot actie

**Voor beveiligingsprofessionals**:
- Steun initiatieven voor **verantwoorde openbaarmaking**.
- Draag bij aan **opensourcebeveiligingstools**.
- Pleit voor **bescherming van onderzoekers**.

**Voor wetshandhaving**:
- **Eis verantwoording** van leveranciers.
- Verplicht **beveiligingsaudits vóór inzet**.
- Voer **direct MFA in**.
- **Betrek de beveiligingsgemeenschap** voor advies.

**Voor beleidsmakers**:
- Neem wetten aan die **beveiligingsstandaarden verplicht stellen**.
- Financier **onafhankelijke audits** van bewakingstechnologie.
- Bescherm **klokkenluiders en onderzoekers**.
- Richt **toezichthoudende instanties** op met technische expertise.

**Voor het publiek**:
- Informeer jezelf over **surveillance in je gemeenschap**.
- Ga naar **gemeenteraadsvergaderingen** wanneer contracten worden besproken.
- Steun organisaties die **transparantie bevorderen**.
- Neem contact op met **vertegenwoordigers** over je zorgen.
- Gebruik **detectietools** om surveillance in kaart te brengen (zie onze [hardwaregids](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)).

### Gerelateerd lezen

- **[Bewaking met Flock Safety-camera's: verspreiding, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** - Begrijp het landschap van surveillance
- **[Flock-You-detectieproject: gids voor hardware tegen surveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Bouw je eigen detectieapparaat

Wachten tot de sector deze fouten oplost, is geen beschermingsstrategie. **[FlockYou-detectieapparaten](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** van STS Collective werken nu. Met de lezerscode **SIMEONONSECURITY** krijg je tot 20% korting.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Koop FlockYou-detectoren en bespaar 20%
{{< /centerbutton >}}

______

## Bronnen

1. [GainSec-onderzoek naar het ecosysteem tegen criminaliteit - GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [Whitepaper van GainSec - Zenodo DOI: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [Blog van GainSec - informele technische rapporten](https://gainsec.com/)
4. [Officiële reactie van Flock Safety - november 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media - blootgestelde feeds van Flock-camera's](https://www.404media.co/)
6. [YouTube van Ben Jordan - demonstraties van kwetsbaarheden](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [MITRE CVE-database](https://cve.mitre.org/)
9. [Electronic Frontier Foundation - ALPR-surveillance](https://www.eff.org/issues/automated-license-plate-readers)
10. [Brief van senator Wyden aan de FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs - ALPR-onderzoek](https://lucyparsonslabs.com/)
12. [DeFlock-project - camera's in kaart brengen](https://deflockproject.org/)
13. [Distributed Denial of Secrets - bestandssysteemafbeeldingen van Flock ALPR-camera](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee - Flock-camera's zitten vol beveiligingslekken en hardgecodeerde inloggegevens](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED en 404 Media - hackers kregen toegang tot een Flock-camera](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday - deze week in beveiliging: Flock-camera's zijn oud](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD - CVE-2021-1905 Qualcomm Adreno GPU use-after-free](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD - CVE-2018-9568 typeverwarring in Linux-kernelsocket](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership - Flock Safety ALPR-detectie en apparatenreferentie](https://wifimothership.com/flock)
20. [CVE.org - zoekfunctie voor records van het CVE-programma](https://www.cve.org/)
21. [Beveiligingswaarschuwing van Flock Safety - schotdetectie en kentekenlezer](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec - Fly By Device 2: draadloze RCE, camerafeed, DoS en informatielek bij Falcon en Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec - Root from the Coop Device 3: root-shell op de Bravo-rekenkast van Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
