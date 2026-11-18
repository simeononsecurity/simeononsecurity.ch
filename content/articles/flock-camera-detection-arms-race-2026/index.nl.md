---
title: "De Flock-cameradetectierace: wat veranderde er in 2026?"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Bekijk gemelde veranderingen in Flock Safety-detectie, reacties van de gemeenschap en infraroodmethoden om camerasystemen te herkennen."
genre: ["Privacytechnologie", "Tegensurveillance", "Open-sourceprojecten", "Digitale rechten", "Netwerkbeveiliging", "Beveiligingsonderzoek", "Hardwarehacking", "Privacyhulpmiddelen"]
tags: ["Flock Safety", "ALPR", "Flock-You", "OUI-detectie", "Wildcard-probeverzoek", "Promiscue WiFi-modus", "802.11-bewaking", "DeFlockJoplin", "NitekryDPaul", "BLE-detectie", "WiFi 5 GHz", "Lokaal beheerd MAC-adres", "SSID-patroonherkenning", "Hardware voor tegensurveillance", "STS Collective", "colonelpanichacks", "Detectieontwijking", "ESP32", "WiFi-detectie", "Bewustwording van surveillance", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "GitHub-issuebeheer", "Firmware bijwerken", "Bescherming tegen digitale apparaatvingerafdrukken", "MAC-randomisatie", "Fingerprinting van Information Elements", "Kanaalwisselen", "Privacybelangenbehartiging", "Open-sourcebeveiliging", "Massasurveillance", "Detectiefirmware", "Rijdend WiFi-onderzoek", "Cameraverwijdering", "Privacyhardware", "Infrarooddetectie", "IR-verlichting", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Optische detectie", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Stadsbeeld met een Flock-camera aan een lantaarnpaal en een voertuig met een geavanceerd detectieapparaat. Gloeiende signalen tonen draadloze gegevensoverdracht tegen een donkere achtergrond."
coverCaption: "Hoe veranderende hardware van Flock Safety open-source detectietools blijft breken en hoe de gemeenschap de achterstand telkens inhaalt"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Als je Flock-You-detector stil is geworden op een route waar hij eerder telkens camera's vond, beeld je je dat niet in en is je hardware waarschijnlijk niet kapot.** De hardware en firmware van Flock Safety zijn het afgelopen jaar minstens twee keer veranderd. Daardoor werkten detectiemethoden van de gemeenschap niet meer en moesten open-sourceonderzoekers telkens een nieuw kenmerk reverse-engineeren.

*Dit verhaal ontwikkelt zich snel. De detectiemethode en OUI-lijst hieronder komen uit de tak `colonelpanichacks/flock-you` `main` van september 2026. Controleer de [GitHub-repository](https://github.com/colonelpanichacks/flock-you) voordat je je apparaat defect verklaart.*

{{< youtube id="cVf-id71BuQ" >}}

*De video van Valleytech Custom Solutions hierboven toont precies het verschijnsel dat dit artikel beschrijft: een gewone wardrive die plotseling nul detecties oplevert op meerdere firmwareversies, op een route waar eerder betrouwbaar camera's werden gevonden en in een county waar eerder gemarkeerde camera's fysiek waren verdwenen.*

______

## Een wardrive die plotseling niets opleverde

Meldingen beschrijven vaak hetzelfde patroon. Een bestuurder rijdt een bekende route die tientallen keren is afgelegd. De detector gebruikt actuele firmware en heeft dezelfde camera's eerder gevonden. Tijdens één rit blijft alles stil. Geen piep en geen logregel, op alle aangepaste firmwareversies die de gebruiker probeert.

De video hierboven beschrijft dit precies: op een dagelijkse rit naar het postkantoor werd altijd minstens één Flock-camera geregistreerd, maar nu geen enkele. Op een tweede route langs Micro Center stonden vroeger vijf camera's in de meldingen; nu is er één actief en zijn de andere vier fysiek van hun palen verwijderd.

**Er gebeurden twee dingen tegelijk, en die zijn makkelijk met elkaar te verwarren:**

- **Camera's zijn in sommige gebieden fysiek verwijderd of verplaatst.** Daardoor zijn er echt minder apparaten om te vinden.
- **De draadloze signatuur van de camera's is veranderd.** Een camera die nog op zijn paal staat, activeert mogelijk geen detector met verouderde firmware.

Twee GitHub-issues in `colonelpanichacks/flock-you`, maanden uit elkaar geplaatst, beschrijven het tweede probleem. Samen laten ze zien hoe de gemeenschap haar detectiemethode al twee keer moest aanpassen.

______

## Issue #20: het beheeraccesspoint verdween

**[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)** werd in januari 2026 geopend. Een gebruiker testte het apparaat naast een bekende Flock-camera op DeFlock, maar vond niets. In de weken erna meldden meer mensen hetzelfde vanuit Florida, Indiana, Atlanta en het Midwesten, met verschillende hardware en antennes.

Een reactie stelde de belangrijkste vraag: **had Flock iets veranderd waardoor detectie voor iedereen ongeveer tegelijk uitviel?**

Projectonderhouder colonelpanichacks bevestigde dat. **Rond december 2025 schakelde Flock het beheeraccesspoint uit dat camera's uitzonden.** Dat accesspoint vormde de oorspronkelijke basis voor draadloze detectie. Toen het signaal verdween, schakelde de gemeenschap over op Bluetooth Low Energy (BLE). Ook die vervanging werd tegen het voorjaar van 2026 onbetrouwbaar.

| Detectieoppervlak | Toestand |
|---|---|
| **Beheer-WiFi-accesspoint** | Door Flock uitgeschakeld, ongeveer december 2025 |
| **BLE-bakens** | Werkten vanaf voorjaar 2026 niet meer betrouwbaar |
| **Mobiele LTE-uplink** | Nog in gebruik voor clouduploads, maar niet passief detecteerbaar |
| **Wildcard 802.11-probeverzoeken** | Huidige detectiebasis, zie hieronder |

*Aangepaste firmware die oude AP- of BLE-signalen zoekt, zoekt nu naar iets wat de camera's niet meer uitzenden. Daarom kan een eerder werkend apparaat stilvallen terwijl de hardware in orde is.*

## De vervangende methode: wildcard-probes en framefingerprinting

De huidige firmware van `flock-you` gebruikt een speciale 802.11-promiscue modus. De radio zendt niets uit en maakt geen verbinding met een netwerk. Hij luistert alleen en wisselt elke 250 milliseconden tussen WiFi-kanalen 11, 6 en 1 om het schakelen van de camera's bij te houden.

**De firmware meldt nu pas een detectie als al deze voorwaarden kloppen:**

1. Het frame is een 802.11 **Management Probe Request** (type 0, subtype 4).
2. Het **SSID Information Element is aanwezig en heeft lengte 0**, dus het is een wildcard-probe en vraagt niet om een specifiek netwerk.
3. Het zendadres (**addr2**) komt overeen met een bekende Flock-OUI-prefix.
4. De overige Information Elements komen overeen met het fingerprintpatroon dat de gemeenschap van DeFlockJoplin documenteerde, op basis van onderzoek van Pintor en Atzori uit 2022 naar **[fingerprinting van WiFi-probeverzoeken op basis van Information Elements](https://ieeexplore.ieee.org/document/10001618)**.

De firmware noemt deze methode `wifi_wildcard_probe_ie_sig`. Tijdens veldtests vond DeFlockJoplin **11 van 12 bekende camera's met slechts 2 fout-positieven**. Dat is dezelfde veldgeverifieerde basislijn als in de **[hardwaregids](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**. De OUI van camera twaalf is later aan de lijst hieronder toegevoegd.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Tijdlijn van Flock-cameradetectie: van beheer-WiFi-accesspoint via Bluetooth Low Energy-bakens naar wildcard-probeverzoeken en fingerprinting van Information Elements, gevolgd door nieuwe SSID-, 5GHz- en MAC-adresontwijking" >}}

______

## De huidige OUI-lijst

De wildcard-probefingerprint wordt pas geactiveerd als het MAC-adres van de zender overeenkomt met een OUI-prefix die de gemeenschap op echte Flock-hardware heeft bevestigd. Onderzoeker **@NitekryDPaul** onderhoudt de lijst vooral. De **DeFlockJoplin**-gemeenschap voegde de 31e prefix toe nadat die een camera vond die de oorspronkelijke lijst met 30 vermeldingen miste.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Deze lijst ligt niet vast.** In de onderzoeksnotities staan prefixes die na tests zijn afgewaardeerd. Eén bleek van een Sony-mediaspeler te zijn, een andere was een vroege tijdelijke waarde die nooit overeenkwam. Twee vermeldingen hebben een lage betrouwbaarheid. Eén prefix, `82:6b:f2`, blijft bewust staan hoewel het lokaal beheerd is: verwijderen zou een echte, door DeFlockJoplin bevestigde detectie missen.

**Eén prefix heeft nu onafhankelijke bevestiging op echte hardware.** De bestandssysteembeelden van een Flock-eenheid die in september 2026 zijn gepubliceerd, bevatten MAC-adres **`f4:6a:dd:57:46:fb`**. De prefix `f4:6a:dd` staat als nummer 13 op deze lijst. Het was geen laboratoriumapparaat of gekocht proefexemplaar, maar een paalcamera in Wauwatosa, Wisconsin, die verkeer fotografeerde. Dit is tot nu toe de sterkste bevestiging van een prefix.

*Beheer je een eigen firmwarefork? Haal de OUI-lijst dan uit de upstreammap `datasets/` in plaats van een kopie vast te leggen. De lijst verandert met het onderzoek. Een verouderde kopie zorgt er ongemerkt voor dat je camera's mist.*

______

## De detectiesignalen op volgorde

OUI-overeenkomst is de methode waarop de huidige firmware leunt, maar het is de zwakste van vijf beschikbare signalen. De gemeenschap van **[WiFi Mothership](https://wifimothership.com/flock)** rangschikt ze op betrouwbaarheid en gebruikt daarbij firmwareonderzoek van GainSec.

| Betrouwbaarheid | Signaal | Opmerking |
|---|---|---|
| **HOOG** | **BLE-fabrikant-ID `0x09C8`** (XUNTONG) | Sterkste digitale fingerprint. Komt voor op Raven-eenheden en op Falcon of Sparrow met aangesloten batterijmodule |
| **HOOG** | **Raven BLE-service-UUID's `0x3100` tot `0x3500`** | Raven-specifieke GATT-services voor GPS, voeding, netwerk, uploads en fouten. Werkt alleen op Raven-hardware |
| **GEMIDDELD** | **WiFi-SSID-patroon `^Flock-[A-Z0-9]+$`** | Standaardnaam van de provisioninghotspot. Andere SSID's in firmware zijn `FS Ext Battery`, `Penguin` en `Pigvision` |
| **GEMIDDELD** | **Substring in BLE-apparaatnaam** | Namen als `FS Ext Battery` staan in advertentiepakketten; fabrikantgegevens hoeven niet te worden geparseerd |
| **LAAG** | **MAC- en OUI-prefixovereenkomst** | **De meest ruisgevoelige methode.** Prefixes van componentleveranciers zitten in duizenden niet-gerelateerde producten |

*De onderste rij is de methode waarop de huidige firmware het meest steunt. Dat is het kernprobleem van detectie die met OUI's begint.*

### Waarom de OUI-lijst veel ruis bevat

De 31 prefixes hierboven zijn geen 31 Flock-identifiers. WiFi Mothership volgt daarnaast **26 prefixes en classificeert elk prefix op basis van de werkelijke eigenaar**.

| Klasse | Aantal | Eigenaar |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, een IEEE-toewijzing aan het bedrijf zelf |
| **Batterijmodules** | 10 | Silicon Labs-onderdelen in accu-uitbreidingen |
| **Cameramodules** | 11 | Liteon Technology WiFi-cameramodules |
| **Rekeninfrastructuur** | 4 | Raspberry Pi Foundation en Raspberry Pi Trading |

**Vijfentwintig van die 26 prefixes behoren aan componentleveranciers.** Hun onderdelen zitten in enorme aantallen niet-gerelateerde apparaten. Een prefix van een Silicon Labs-accupakket of Liteon-cameramodule komt voor in producten zonder relatie met Flock Safety, en Raspberry Pi-kaarten zijn overal.

**Een overeenkomst is een aanwijzing, geen identificatie.** Daarom is de wildcard-probesignatuur zo belangrijk in de huidige firmware. Een OUI-overeenkomst samen met een probeverzoek met lege SSID verhoogt de betrouwbaarheid op de eigen schaal van het project van een gok naar 62.

*Alleen `B4:1E:52` beantwoordt zelfstandig de vraag «is dit een Flock-apparaat?». Zie de andere 30 prefixes als ondersteunend bewijs.*

### Hoeveel camera's zenden een hotspot uit?

Wardrivinggegevens geven een ondergrens. WiFi Mothership telde **minstens 900 Flock-accesspoints op WiGLE in 2025**. Een Flock-AP betekent hier een apparaat dat de standaardhotspot-SSID `Flock-XXXX` uitzond.

Dit cijfer gaat over apparaten die een provisioninghotspot uitzenden, niet over het totale aantal installaties. Flock zegt tienduizenden apparaten te hebben geplaatst. De meeste camera's zenden niets uit wat een passerende wardriver registreert. **De kaart is een steekproef, en een kleine.**

______




## Issue #43: nieuw SSID-patroon, 5GHz en MAC-antifingerprinting

Drie maanden nadat Issue #20 werd gesloten, kwam een tweede melding binnen. Die beschrijft een mogelijke tegenmaatregel tegen detectie, niet alleen een toevallige firmwarewijziging. **[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, ingediend in mei 2026, gebruikt WiGLE-gegevens van een camera die al op DeFlock was bevestigd. De melding documenteert drie dingen waarop bestaande hulpmiddelen niet waren voorbereid.

### Bevinding 1: een ander SSID-formaat

De gedocumenteerde Flock-hotspot gebruikte altijd het patroon `Flock-XXXXXX`. De camera in deze melding zond **`Flock Camera net.`** uit, een geheel andere naamconventie. Wie in WiGLE zocht op de wildcard `Flock-*`, zoals meerdere onderzoekers deden, kreeg nul resultaten voor deze camera hoewel die actief uitzond.

### Bevinding 2: een bevestigde 5GHz-hotspot

Dezelfde camera zond tegelijk uit op **2,4GHz-kanaal 1** en **5GHz-kanaal 157**, met opeenvolgende MAC-adressen (`...9f:a2:de` en `...9f:a2:df`). Dat wijst op één dualband-WiFi-module die aangrenzende adressen aan elke radio toekent, niet op twee losse apparaten. Onderzoeker nsm_barii had eerder een Flock-probeverzoek op 5GHz-kanaal 149 vastgelegd. Er zijn dus twee gegevenspunten die bevestigen dat 5GHz echt wordt gebruikt.

**Alle detectiemethoden eerder in dit artikel, inclusief de huidige wildcard-probefirmware, luisteren alleen op 2,4GHz.** Een camera die uitsluitend of vooral op 5GHz uitzendt, blijft voor die hardware onzichtbaar, ongeacht hoe nauwkeurig de OUI-lijst is.

### Bevinding 3: lokaal beheerde MAC-adressen op de hotspot

Bij beide vastgelegde MAC-adressen staat de **lokaal beheerde bit aan**. Ze komen dus niet uit Flocks bij IEEE geregistreerde OUI-blok. De standaarddetectie van `flock-you` slaat lokaal beheerde adressen bewust over om MAC-randomisatie van telefoons en laptops te filteren.

**Die filter vermindert fout-positieven, maar filtert ook een Flock-camera uit die een lokaal beheerd MAC-adres op zijn hotspot gebruikt.** De opeenvolgende laatste bytes van de adressen sluiten willekeurige generatie uit en wijzen op gestructureerde adrestoewijzing.

| Bevinding | Wat nog werkt |
|---|---|
| **Nieuw SSID-formaat** (`Flock Camera net.`) | SSID-patroonherkenning werkt als het matchpatroon wordt verbreed |
| **5GHz-gebruik** | Niets in de huidige WiFi-firmware, die alleen 2,4GHz scant |
| **Lokaal beheerd MAC-adres** | SSID-patroonherkenning, omdat die niet van het MAC-adres afhangt |

*SSID-detectie is de enige methode in de tabel die blijft werken, ongeacht de band of MAC-adrestoewijzing. Dat pleit ervoor SSID-patronen te verbreden en niet alleen op OUI-overeenkomsten te vertrouwen.*

______

## Ontwijkt Flock bewust detectie?

Geen van beide GitHub-issues bewijst opzet. De auteur van Issue #43 stelde dit zelf als open vraag: gebeurt dit bij alle Flock-installaties of alleen bij één firmwareversie op één camera?

Bekijk het patroon in beide issues. Een detectiesignaal verdwijnt, de gemeenschap vindt een vervanging en de blinde vlekken daarvan (alleen 2,4GHz scannen, OUI's gebruiken en lokaal beheerde MAC-adressen wegfilteren) komen overeen met eigenschappen die een nieuw SSID-formaat, 5GHz-radio en lokaal beheerd MAC-adres zouden benutten. **Dat kan toeval zijn door een niet-gerelateerde firmwarecyclus. Het kan ook een leverancier zijn die zijn draadloze aanwezigheid verkleint, waardoor detectie door derden onbedoeld of opzettelijk moeilijker wordt.**

*De nuttigste houding is niet om één verklaring te kiezen. Bouw detectie die niet op één aanname steunt. In de geschiedenis van dit project bleken aannames telkens tijdelijk.*

### Visuele bevestiging: ingeschakeld maar zonder uitzending

**[Een derde korte video van Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) toetst de uitleg dat de camera misschien verwijderd was.**

{{< youtube id="sjI8FB0cLk0" >}}

De maker ging 's nachts terug naar dezelfde camera uit de eerste video en zag dat de **IR-leds nog brandden**. De camera stond aan en verlichtte het beeld voor nachtregistratie. Tegelijkertijd registreerde **elke geteste aangepaste firmware nul geldige detecties**. Eén waarschuwing bleek een fout-positief. Er kwam niets van de camera via de draadloze kant binnen.

**Zo kun je de twee verklaringen onderscheiden.** Een verwijderde camera verklaart geen apparaat dat zichtbaar aanstaat en 's nachts verlicht. Een actieve, verlichte camera die stil blijft op alle WiFi-detectiemethoden wijst erop dat de draadloze signatuur verdwenen is.

De maker meldde na gesprekken met andere ontwikkelaars dat dit geen afzonderlijk geval was. **Meerdere mensen zagen ongeveer tegelijk hetzelfde patroon**, wat eerder op een landelijke verandering bij Flock wijst dan op een lokale uitzondering. *Dit is anekdotisch, gebaseerd op informele gesprekken in plaats van een gepubliceerde dataset. Het past wel bij de perioden december 2025 en voorjaar 2026 uit Issue #20 en hoort in een nieuw GitHub-issue.*

______

## Wat dit betekent voor je detectiehardware

Als je apparaat stil is geworden, loop dan deze punten na voordat je aanneemt dat het defect is:

1. **Werk eerst de firmware bij.** Gebruik je iets ouder dan de huidige tak `main`, dan zoek je mogelijk nog naar het uitgeschakelde beheer-AP of onbetrouwbare BLE-bakens. Haal de nieuwste firmware op en flash opnieuw.
2. **Controleer of de camera er nog staat.** Sommige meldingen van nul detecties bleken echte verwijdering of verplaatsing. Vergelijk met **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** of **[DeFlock](https://deflock.org/)** voordat je het apparaat troubleshoott.
3. **Rijd langzaam bij kruisingen.** Door een kanaalverblijftijd van 250 ms kun je het detectievenster missen als je snel langsrijdt. Stop 30 tot 60 seconden. Daarmee vind je meer camera's dan met een snelle rit en grotere antenne.
4. **Meld je waarneming.** Nul detecties naast een visueel bevestigde camera is precies het soort gegeven dat Issue #20 en #43 opleverde. Open een issue in plaats van aan te nemen dat iemand anders het al meldde.
5. **Ken de beperkingen.** Firmware die alleen WiFi en 2,4GHz gebruikt, ziet geen camera op 5GHz of een camera die stil is op de gescande banden. Dat is een echte lacune, geen fout in jouw build.

**Daarom is de hardware niet nutteloos.** De OUI-lijst en wildcard-probefingerprint vinden nog steeds de meeste geplaatste camera's. Zie elke detector, zelfgebouwd of gekocht, als momentopname van een voortdurende wedloop, niet als permanente oplossing.

{{< stscollective-ad "flockyou" >}}

______


## Een parallelle aanpak: de infraroodflits detecteren in plaats van WiFi

Draadloze detectie is niet het enige front. **[Een aparte vervolgvideo](https://www.youtube.com/shorts/mzpr6bslsYA) van Valleytech Custom Solutions beschrijft een heel andere aanpak**: kijk naar de infraroodverlichting van de camera in plaats van naar radiosignalen te luisteren.

{{< youtube id="mzpr6bslsYA" >}}

De meeste ALPR-camera's, ook die van Flock, gebruiken **infrarood om 's nachts leesbare kentekens vast te leggen**. Het IR-licht is onzichtbaar voor mensen, maar een beeldsensor zonder infrarood-cutfilter kan het zien. *Het ontbrekende IR-cutfilter maakt van een gewone cameramodule een Flock-detector.*

### Hoe het prototype eruitziet

De aanpak doorliep meerdere versies voordat er een bruikbare combinatie ontstond:

- **Eerste poging**: speciale IR-fotodiodeontvangers. Technisch bruikbaar, maar te duur voor doe-het-zelfgebruik.
- **Tweede poging**: een **Jetson Nano met een Raspberry Pi-cameramodule**. Dit bewees dat het concept werkte, maar prijs en energieverbruik waren onpraktisch voor een handheld- of voertuigopstelling.
- **Huidige bouw**: een **ESP32-cameramodule zonder IR-cutlens**. De maker testte een **ESP32-CAM** en een **M5Stack S3 Cam**, en koos daarna de **Seeed Studio XIAO ESP32S3 Sense** met een **Seeed XIAO GNSS-module op basis van de Quectel L76K-chip** om detecties van GPS-posities te voorzien. Dit volgt het GPS-wardrivingpatroon van het WiFi-dashboard van `flock-you`.

| Vereiste | Waarom het telt |
|---|---|
| **Geen IR-cutfilter op de cameramodule** | Het filter dat gewone foto's kleurnauwkeurig maakt, blokkeert het licht dat deze methode moet zien |
| **Een camera in plaats van een fotodiode** | Fotodiodeontvangers die het signaal konden isoleren waren te duur voor een praktische doe-het-zelfbouw |
| **GPS-logging** | Koppelt detecties aan een locatie, zoals het Flask-dashboard van de WiFi-firmware |

### Het knipperpatroon van de camera

Het idee werkt alleen als de verlichting in een herhalend patroon knippert. De maker rapporteerde een **zelfgemeten timing van ongeveer 20 milliseconden aan en 80 milliseconden uit, met een periode van 100 milliseconden. Dat is een inschakelduur van 20% bij 10Hz**. Hij benadrukte dat dit niet is geverifieerd en onjuist kan zijn. *Gebruik het getal als beginpunt voor eigen metingen, niet als bevestigde specificatie. Flock heeft het niet gepubliceerd en de maker gaf geen zekerheid.*

### De stand van het project

**Dit is een vroeg prototype voor doe-het-zelfgebruik, geen afgerond product.** De maker omschreef de software als «vibe coded» en nog in ontwikkeling. Een zoemer voor hoorbare meldingen staat gepland maar is nog niet toegevoegd. Er is ook geen kant-en-klaar bord zoals OUI-SPY. De huidige versie vereist dat **een mens visueel bevestigt** of een melding echt een camera is en geen andere IR-lichtbron. Het werkt als screeningshulpmiddel, niet volledig automatisch.

*Dit detectieoppervlak hangt niet af van WiFi, 2,4 of 5GHz, OUI-overeenkomsten of MAC-adresgedrag. De ontwijkingstechnieken uit Issue #43 zijn er dus niet op van toepassing. Het heeft eigen beperkingen: zichtlijn, daglichtinterferentie en een inschakelduur die niet onafhankelijk is bevestigd.*

______

## Wat de gemeenschap eraan doet

De reacties op beide issues volgden hetzelfde patroon dat het project al twee jaar bruikbaar houdt: iemand meldt een lacune, iemand anders draagt de oplossing bij en die komt uit als update in plaats van in een achterstand te blijven liggen.

- **Issue #20** eindigde met een bevestigde oorzaak en herschreven firmware rond wildcard-probes, gebaseerd op veldonderzoek van DeFlockJoplin.
- **Issue #43** staat nog open. Het voorstel voor SSID-patroonherkenning is niet uitgevoerd. *Het patroon `Flock Camera` toevoegen is een kleine, afgebakende bijdrage voor iemand die de matchlogica van de firmware kent.*
- De OUI-dataset heeft versies en datums. Afgewaardeerde en onzekere vermeldingen zijn gedocumenteerd, zodat forkers zien wat veranderde en waarom.

*Dit is het praktische voordeel van open-source detectietools boven een gesloten alternatief. Een gebruiker kan een gesloten detector niet aanpassen zodra die de lacune ontdekt. Dit project is al twee keer aangepast.*

______

## De andere reactie: de hardware weghalen

Draadloze detectie is één reactie op deze camera's. Een parallel initiatief richtte zich op de hardware zelf en leverde in september 2026 het meest gedetailleerde openbare bewijs op over de werking van een Flock-camera.

**Het collectief stegan0gram haalde een camera van een paal, kopieerde de interne opslag en publiceerde de bestandssysteembeelden via Distributed Denial of Secrets.** Het beschreef het werk zo:

> "Waarom ze alleen vernielen als we ze ook kunnen reverse-engineeren en de geheimen kunnen vinden van degenen die ons bespioneren? We hebben hardware uit het veld bevrijd, onschadelijk gemaakt en daarna de camera's en bijbehorende zonne-energieapparatuur reverse-engineered."

*Dat onderscheid telt. Een camera vernielen verwijdert één apparaat. Reverse-engineering levert bewijs op over alle apparaten.*

### Wat de verwijdering opleverde

De dataset bevat een **mediapartitie van 18 GB**, een **Android-systeemimage van 1,5 GB** en een **partitie met inloggegevens van 32 MB**, plus de teruggevonden sleutel voor de versleutelde mediacontainer. Onderzoekers stelden de versies van het besturingssysteem en de kernel vast, plus hardgecodeerde backend-inloggegevens en platte authenticatietokens die de camera opslaat.

Deze bewijsbasis ondersteunt het beveiligingsonderzoek in **[Kwetsbaarheden in Flock Safety-camera's: meer dan 50 fouten gevonden](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**. Dat onderzoek steunde eerder op laboratoriumapparaten en gekochte exemplaren.

### De reactie op verwijdering

Fysieke ingrepen hebben gevolgen en het beeld is gemengd:

- **Meerdere mensen zijn landelijk gearresteerd** wegens vermeende sabotage van Flock-camera's.
- **Sommige gemeenten kondigden aan de camera's niet meer te gebruiken.** Dat is de uitkomst die tegenstanders willen.
- **Eén politieafdeling bouwde een nepbehuizing van een 3D-geprinte Flock-camera** om mogelijke vandalen te lokken en aan te houden.

Noel Pichardo, voormalig politieagent in Pawtucket, Rhode Island, werd criticus van Flock nadat hij het cameragebruik van zijn afdeling aanvocht. Tegen WIRED zei hij dat hij de frustratie begrijpt, maar vreest dat sabotage de politie en overheid bevestigt in hun overtuiging dat deze technologie nodig is. «Hoe langer de overheid het gemor negeert van inwoners die tegen dit soort surveillance zijn, hoe vaker dit zal gebeuren», zei hij.

### Waar detectie past

De ontmanteling verandert het detectieprobleem niet. De camera zendt nog steeds uit, firmware heeft nog steeds de OUI-lijst en probesignatuur nodig en de twee gedocumenteerde uitvalmomenten blijven bestaan.

De gegevensdump bevestigt **de hardware-identiteit**, inclusief één OUI-vermelding die op een echt apparaat is gecontroleerd. **Camera's verdwijnen van een route omdat een gemeenteraad een contract beëindigt, niet omdat een detector stilvalt.** Draadloze hulpmiddelen beantwoorden een persoonlijke vraag over je omgeving. De beleidsdiscussie beantwoordt de grotere vraag, en de dump gaf die discussie het sterkste bewijs tot nu toe.

______

## Conclusie: detectie blijft veranderen

Een stille detector op een route waar eerder camera's werden gevonden, bewijst niet dat je hardware kapot is. Het is bewijs dat de draadloze signatuur waarop de detector vertrouwt opnieuw veranderde, al twee keer in één jaar. Het **beheeraccesspoint, de BLE-bakens en mogelijk nu de aannames van alleen 2,4GHz en alleen OUI's in de firmware** bleken elk maar tijdelijk bruikbaar.

**De oplossing is nooit geweest om draadloze detectie op te geven.** Houd de aannames zichtbaar en gedocumenteerd, zodat je ze kunt aanpassen wanneer een melding zoals Issue #20 of #43 binnenkomt. Dat is het argument voor open-sourcefirmware boven een gesloten alternatief: de gemeenschap kan de lacune dichten zodra die gevonden is, zonder te wachten op de leverancier.

### Belangrijkste punten

- **Twee detectiesignalen zijn al uitgevallen**: het beheer-WiFi-AP (uitgeschakeld rond december 2025) en BLE-bakens (onbetrouwbaar vanaf voorjaar 2026).
- **De huidige methode, wildcard-probes met OUI- en IE-fingerprinting, vond in veldtests 11 van 12 camera's**, maar werkt alleen via WiFi op 2,4GHz.
- **Een openstaande melding beschrijft een nieuw SSID-formaat, een bevestigde 5GHz-hotspot en lokaal beheerde MAC-adressen** die de huidige OUI-methode op alleen 2,4GHz niet vindt.
- **Een aparte aanpak zonder WiFi komt op**: een ESP32-camera zonder IR-cutfilter vindt de infraroodverlichting en is ongevoelig voor de beschreven draadloze ontwijking.
- **Visuele controle bevestigt de draadloze stilte**: een camera stond 's nachts aan en verlichtte de omgeving, maar registreerde nul geldige WiFi-detecties. Voor dat apparaat verklaart verwijdering de stilte niet.
- **Nul detecties bij een bekende camera betekent niet meteen dat je hardware kapot is.** Werk eerst de firmware bij en controleer daarna of de camera er nog staat.
- **Het open-sourceproject brengt oplossingen uit wanneer de gemeenschap lacunes vindt.** Lees GitHub-issues naast de README voor de actuele stand.

### Volgende stappen

1. **Werk de firmware bij** naar de huidige tak `main` voordat je iets anders troubleshoott: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Lees de volledige hardwaregids** als je die nog niet kent: **[Flock-You-detectieproject: hardwaregids voor tegensurveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Vergelijk vermoedelijke blinde zones** met **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** voordat je aanneemt dat je apparaat iets miste.
4. **Lees wat je tegenover je hebt**: **[Flock Safety-camerasurveillance: omvang, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Combineer WiFi-detectie met mobiele detectie** via **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** voor een vollediger beeld. Geen van de methoden in dit artikel detecteert IMSI-catchers.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Koop gebruiksklare FlockYou-apparaten, bespaar 20%
{{< /centerbutton >}}

______

## Gerelateerde artikelen

| Artikel | Onderwerp |
|---------|-----------|
| **[Flock-You-detectieproject: hardwaregids voor tegensurveillance](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Gids voor drie hardwareplatforms, firmware-installatie en detectiemethode |
| **[Flock Finder: breng vermoedelijke Flock-camera's bij jou in kaart](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Vergelijk een vermoedelijke blinde zone met meer dan 40.000 cameravindplaatsen |
| **[Flock-camera's: hulpmiddel voor openbare veiligheid of surveillance zonder bevel?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analyse van wat de database mogelijk maakt en waarom de vraag over huiszoekingsbevelen zwaarder weegt dan detectie |
| **[Flock Safety-camerasurveillance: omvang, privacyzorgen en beschermingsstrategieën](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Inzet, misbruikgevallen en hulpmiddelen voor gemeenschapsorganisatie |
| **[Kwetsbaarheden in Flock Safety-camera's: meer dan 50 fouten gevonden](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Hardware- en softwareonderzoek, los van draadloze detectie |
| **[Rayhunter-apparaten flashen: volledige gids](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | IMSI-catchers en stingrays detecteren, de mobiele tegenhanger van de WiFi-lacune |

______

## Bronnen

1. [Flock-You GitHub-repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub-issue #20 - Flock-camera's worden niet gedetecteerd, andere apparaten wel](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub-issue #43 - 5GHz-signaal? Nieuwe OUI en MAC-adresfiltering](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [OUI-onderzoeksdataset van NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - ALPR-onderzoek door de gemeenschap](https://deflockjoplin.today)
7. [Pintor, L. & Atzori, L. (2022) - Analyse van Wi-Fi-probeverzoeken voor fingerprinting van Information Elements, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED en 404 Media - Hackers drongen een Flock-camera binnen](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Flock-camera's bevatten tientallen kwetsbaarheden en hardgecodeerde inloggegevens](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - bestandssysteembeelden van een Flock-ALPR-camera](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Deze week in beveiliging: Flock-camera's zijn oud; Microsoft-patches en SSH-onderzoek](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Flock Safety-ALPR-detectie en apparaatregister](https://wifimothership.com/flock)
13. [GainSec - firmwareonderzoek en beveiligingsadviezen](https://gainsec.com/)
8. [De zoektocht naar de verborgen probe - gedrag van wildcard-probes met verborgen SSID](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - kaart met ALPR-camera's uit crowdsourcing](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY en detectiehardware](https://colonelpanic.tech)
11. [STS Collective - FlockYou-apparaten](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Er gebeurt iets vreemds met Flock-camera's - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Infrarood-wardriving voor Flock-camera's - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Flock-camera's staan aan maar zenden niets uit - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Automatische kentekenplaatherkenning - Wikipedia (infraroodverlichting bij ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [L76K-GNSS-module voor Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)

