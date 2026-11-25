---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Vergelijk Meshtastic, MeshCore en Reticulum op basis van routering, zendtijd, infrastructuur, transport en gebruik zonder internetverbinding."
genre: ["LoRa", "Meshnetwerken", "Communicatie zonder infrastructuur", "Noodcommunicatie", "Amateurradio", "Software met open broncode", "Rampenvoorbereiding", "Draadloze netwerken", "Privacy", "Netwerken"]
tags: ["meshtastic vs meshcore vs reticulum", "Reticulum-netwerk", "meshtastic", "meshcore", "reticulum", "lxmf", "LoRa-meshnetwerk", "communicatie zonder infrastructuur", "rnode", "pakketgeschakelde radio", "transportonafhankelijk netwerken", "meshnetwerken", "noodcommunicatie", "community-meshnetwerk", "LoRa-zendtijd", "beheerste flooding", "hoplimiet", "repeaterknooppunt", "roomserver", "Sideband-app", "nomadnet", "meshchat", "rampencommunicatie", "radio zonder infrastructuur", "meshnetwerkprotocol", "regionaal meshnetwerk", "RF-techniek"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Illustratie die drie meshnetwerksystemen vergelijkt met knooppunten, antennes en verbindingslijnen op een donkere achtergrond met heldere kleuren, als weergave van hun eigen functies."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## Het korte antwoord

**Deze drie projecten lossen niet allemaal hetzelfde probleem op.** Meshtastic en MeshCore zijn LoRa-meshnetwerksystemen met verschillende ideeën over routering. Reticulum heeft een bredere opzet. Het is een transportonafhankelijke netwerklaag die tegelijk werkt via LoRa, pakketgeschakelde radio, wifi, Ethernet, seriële verbindingen en internet.

**De juiste vraag is niet "welke is de beste?"** De vraag is: "welke architectuur past bij het netwerk dat ik wil bouwen?"

*Meshtastic past bij ad-hocnetwerken en mobiele gebruikers.* **MeshCore past bij bewust gebouwde, vaste infrastructuur.** **Reticulum past bij netwerken die verschillende transporten moeten koppelen of anders gescheiden netwerken moeten verbinden.** Wie één regionaal LoRa-mesh bouwt, heeft meestal maar een van de eerste twee nodig.

______

## Bepaal welk netwerk je bouwt

Schrijf op wat het netwerk moet doen voordat je protocollen vergelijkt. Voor de meeste community- en noodcommunicatienetwerken zijn dit bruikbare doelen:

- **Werken zonder licentie**, zodat iedereen zonder amateurradiolicentie kan meedoen
- **Betaalbare hardware** die een community op grote schaal kan inzetten
- **Laag stroomverbruik**, bij voorkeur geschikt voor zonne-energie of batterijen
- **Communicatie over grote afstanden** zonder mobiel netwerk of internet
- **Onafhankelijkheid van infrastructuur**, elektriciteitsnet, internetproviders en telecombedrijven
- **Eenvoudig genoeg voor mensen zonder radio-expertise** om in te stellen en te gebruiken
- **Geschikt voor inzet door een community**, niet alleen in de kelder van één beheerder
- **Groeien tot meer dan een handvol knooppunten** zonder uit elkaar te vallen
- **Bruikbaar bij uitval van infrastructuur**, als zendmasten en internet niet werken
- **Betrouwbare bezorging boven recordafstand**

Houd deze lijst bij de hand. We toetsen de architectuurkeuzes hieronder aan deze doelen.

______

## Meshtastic

**Meshtastic** is de meest volwassen en breedst gebruikte optie. Voor de meeste gebruikers biedt het veel voordelen.

- **Volwassen ecosysteem** met jaren actieve ontwikkeling
- **Grote gebruikersgroep**, een actieve Discord en uitgebreide documentatie
- **Brede hardwareondersteuning** voor boards van LILYGO, Heltec, RAK en Seeed
- **Goede mobiele apps** voor iOS en Android
- **Eenvoudige start**, de eerste installatie duurt minder dan 20 minuten
- **Goede ondersteuning voor draagbare en mobiele gebruikers** die het mesh onvoorspelbaar in- en uitgaan
- **GPS- en telemetriefuncties** met een ontwikkeld ecosysteem eromheen
- **Bestaande netwerken** in de meeste stedelijke gebieden maken instappen makkelijker, omdat je je bij een netwerk aansluit in plaats van er een vanaf nul te bouwen

Lees de **[vergelijkingsgids voor MeshCore en Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)** voor een volledig overzicht van de routering, hardwarecompatibiliteit en installatie van Meshtastic tegenover MeshCore. Dit artikel richt zich op de architectuurvraag die het belangrijkst is voor grotere netwerken: **beheerste flooding en hoplimieten**.

### Beheerste flooding en waarom hops ertoe doen

Bij **[beheerde flooding](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** in Meshtastic annuleert een gewone client een geplande heruitzending als hij hetzelfde pakket eerder hoort langskomen. `ROUTER` en `ROUTER_LATE` kunnen het toch doorsturen. Voor `CLIENT_BASE` geldt die uitzondering voor verkeer van of naar een favoriet.

De hopteller van Meshtastic staat standaard op **3** en kan maximaal op **7** staan. Vanaf firmware 2.7.11 kunnen geschikte infrastructuurknooppunten [de teller behouden](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) na de eerste hop als het vorige relais een favoriete `ROUTER` of `ROUTER_LATE` is. Een echte heruitzending kost nog steeds zendtijd.

Een hogere hoplimiet kan meer relais bereiken, maar laat niet elke ontvanger zenden. **Vaker doorsturen** kan leiden tot:

- **Meer zendtijd** per bericht
- **Meer exemplaren in de ether** als meerdere geschikte relais hetzelfde pakket doorsturen
- **Meer concurrentie** om het gedeelde kanaal
- **Meer kans op botsingen** wanneer meer radio's in hetzelfde tijdvenster uitzenden
- **Hoger batterijverbruik** bij elk knooppunt dat ontvangt en opnieuw uitzendt
- **Minder beschikbare kanaalcapaciteit** voor echte berichten

De capaciteit van LoRa wordt beperkt door zendtijd en regionale limieten voor de duty cycle, niet door het aantal knooppunten. Een netwerk met tien drukke knooppunten die vaak GPS en telemetrie uitzenden, kan een kanaal verzadigen dat vijftig stille sensoren nauwelijks zouden gebruiken. Daarom gaat een dicht mesh met een hoge hoplimiet sneller achteruit dan hetzelfde aantal knooppunten met een lagere limiet en beheerste telemetrie-intervallen.

Sinds Meshtastic 2.6 gebruiken **directe berichten** eerst flooding om een route te ontdekken. Daarna proberen ze de geleerde volgende hop. Bij uitval kunnen ze terugvallen op flooding.

Voor een klein of middelgroot mesh, zoals dat van een wandelvereniging, is dit zelden belangrijk. Voor een **regionaal netwerk dat een stad of meerdere plaatsen moet bestrijken**, wordt dit de centrale ontwerpbeperking.

______

## MeshCore

**Speciale repeaters** vormen de vaste doorstuurlaag van MeshCore. Clientradio’s zijn eindpunten.

### Knooppuntrollen

MeshCore-netwerken zijn opgebouwd rond verschillende rollen, niet rond één vlakke groep gelijkwaardige knooppunten:

- **Companion- of clientknooppunten** bevatten een LoRa-radio die is gekoppeld aan een telefoon of laptop. Ze communiceren via nabijgelegen infrastructuur wanneer die beschikbaar is
- **Repeaters** sturen verkeer door tussen clients en andere infrastructuur en doen het meeste routeringswerk
- **Roomservers** (optioneel) hosten groepsgesprekken en leveren opgeslagen berichten af aan clients wanneer die opnieuw verbinding maken

In MeshCore kan een eerste **direct bericht** via flooding een pad ontdekken. Latere directe berichten kunnen dat pad volgen en afhankelijk van de instellingen terugvallen op flooding. **[Openbare en besloten groepskanalen blijven flooding gebruiken](https://docs.meshcore.io/faq/#5-general)** via geschikte repeaters. Clientradio’s sturen geen pakketten van andere knooppunten door.

### Waarom dit bij vaste infrastructuur past

*Dit is het belangrijkste argument voor MeshCore.* Het floodingmodel van Meshtastic heeft echte voordelen voor ad-hoc- en mobiele netwerken: geen planning, geen infrastructuuronderhoud en soepele omgang met knooppunten die komen en gaan. Het routeringsmodel van MeshCore heeft een voordeel wanneer **gebruikers bewust infrastructuur neerzetten**.

Een netwerk met bekende, hoog geplaatste repeaters geeft je de mogelijkheid om de dekking doelgericht te ontwerpen, in plaats van af te hangen van welke knooppunten elkaar op een bepaalde dag toevallig kunnen bereiken. Dat verschil is belangrijk voor:

- **Permanente knooppunten op daken** met betrouwbare stroomvoorziening
- **Masten** en bestaande communicatie-infrastructuur
- **Repeaters op zonne-energie** bij onbemande locaties
- **Relaylocaties in de bergen of op hoogte**
- **Infrastructuur in gemeenschapsbezit** die door meerdere groepen wordt gedeeld
- **Regionale netwerken** die groter zijn dan één wijk
- **Noodcommunicatie** waarbij voorspelbare dekking zwaarder weegt dan flexibiliteit

Kijk naar de basisprincipes van RF: **betrouwbare verbindingen tussen goed geplaatste infrastructuur zijn belangrijker dan maximale antenneversterking, zendvermogen of theoretisch bereik.** **Beide meshes profiteren van goed geplaatste relais.** Welke knooppunten doorsturen, hangt af van hun rollen en het verkeer.

______

## Het argument voor mobiele knooppunten en wat het kost

Een vaak gehoorde suggestie is: *"Meshtastic is beter voor mobiele knooppunten en MeshCore voor vaste knooppunten, dus gebruik Meshtastic voor gebruikers en MeshCore als backbone."*

Op papier klinkt dit aantrekkelijk. In de praktijk levert het combineren van beide niet vanzelf de voordelen van allebei op, want **Meshtastic en MeshCore gebruiken verschillende routerings- en netwerkarchitecturen en wisselen geen berichten met elkaar uit.** Koppelen betekent een vertaallaag toevoegen tussen twee incompatibele systemen, niet simpelweg de beste onderdelen kiezen.

Na het koppelen beheer je:

- **Twee aparte netwerken**, elk met een eigen topologie en werking
- **Twee routeringsmodellen** die geen status delen
- **Een vertaallaag** die doorlopend ontwikkeling en onderhoud vraagt
- **Meer infrastructuur** om de koppeling te hosten
- **Meer instellingen** verdeeld over twee firmware-ecosystemen
- **Meer faalpunten**, want de koppeling kan onafhankelijk van beide meshes uitvallen
- **Moeilijkere probleemoplossing**, omdat een bezorgprobleem in een van beide netwerken of in de koppeling kan zitten

Stel jezelf eerst een directe vraag: **lost de extra complexiteit een probleem op dat één goed afgesteld meshprotocol niet oplost?** Vaak biedt een goed geconfigureerd MeshCore-netwerk met een paar mobielvriendelijke companionknooppunten, of een Meshtastic-netwerk met enkele goed geplaatste relays en een hogere hoplimiet, het meeste praktische voordeel zonder twee netwerken aan elkaar te lijmen.

______

## Reticulum

Reticulum verdient een eigen categorie in plaats van een plek als "derde LoRa-meshoptie", want het is niet in de eerste plaats een LoRa-meshprotocol. **Het onderscheidende kenmerk is de onafhankelijkheid van het transport.**

Reticulum is een op cryptografie gebaseerde netwerkstack. Het gebruikt geen bronadressen, dus pakketten bevatten geen informatie over waar ze vandaan komen. Elk adres is zelfsoeverein: na generatie is het binnen seconden tot minuten wereldwijd bereikbaar en blijft het dat ook wanneer een apparaat fysiek naar een ander deel van het netwerk verhuist. Alle communicatie is standaard versleuteld met tijdelijke sleutels en forward secrecy. Reticulum verwijdert niet-versleutelde pakketten in plaats van ze af te leveren. Kernelstuurprogramma's zijn niet nodig. Het draait in gebruikersruimte op elk systeem met Python 3, waaronder een Raspberry Pi Zero.

Reticulum ondersteunt onder meer deze interfaces:

- **LoRa**, met RNode-compatibele hardware (een vastgelegd open source-ontwerp voor een LoRa-transceiver dat je zelf bouwt, op gangbare boards flasht of kant-en-klaar koopt)
- **Pakketgeschakelde radio**, via elke TNC in KISS-modus, geschikt voor amateurradio op VHF en UHF
- **Wifi en bekabeld Ethernet**, met automatische peer discovery en zonder router of DHCP-server
- **Seriële verbindingen** voor rechtstreekse verbindingen tussen apparaten
- **TCP en UDP over bestaande IP-netwerken**, waaronder internet
- **Het I2P-netwerk** en aangepaste interfaces voor andere systemen met een Python-bridge

Op Reticulum draaien applicaties zoals **LXMF** (een vertragingsbestendig berichtenprotocol) en eindgebruikersprogramma's zoals **Sideband**, **NomadNet** en communityclients voor **MeshChat**. Die geven Reticulumnetwerken een berichten- en browserlaag die vergelijkbaar is met wat Meshtastic en MeshCore standaard aanbieden.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagram waarop Reticulum een LoRa-mesh, een pakketgeschakeld radionetwerk en een internetverbinding koppelt tot één adresseerbaar, versleuteld netwerk" >}}

### Wanneer Reticulum zinvol is

Reticulum laat zijn waarde goed zien in een heterogene opstelling, bijvoorbeeld:

**LoRa-mesh → Reticulum-knooppunt → IP-verbinding → Reticulum-knooppunt → radionetwerk**

Hier doet Reticulum iets wat Meshtastic en MeshCore niet doen: twee verder losstaande communicatiesystemen verbinden tot één adresseerbaar netwerk. Dit is een concrete vereiste, geen algemene upgrade. Goede toepassingen zijn:

- **Geografisch gescheiden netwerken koppelen** zonder rechtstreeks radioverbinding tussen beide
- **Verschillende fysieke transporten overbruggen**, zoals een LoRa-mesh aan de ene en een pakketgeschakeld radionetwerk aan de andere kant
- **Radio-naar-IP-gateways** die verkeer doorgeven tussen een veldradionetwerk en internet
- **Experimentele en onderzoeksnetwerken**, waar het mengen van transporten belangrijker is dan een eenvoudig ontwerp
- **Netwerken waarvoor één transport niet voldoende is**, zodat verschillende onderdelen aan elkaar moeten worden gekoppeld

### Wanneer Reticulum onnodig veel complexiteit toevoegt

Als iedereen compatibele LoRa-hardware gebruikt en het werkelijke doel **één regionaal LoRa-mesh** is, levert Reticulum weinig voordeel op en heeft het wel echte kosten. Elke extra laag in een netwerkstack betekent meer:

- **Configuratie** die goed moet staan en op alle knooppunten gelijk moet blijven
- **Software** om te installeren, bij te werken en te onderzoeken
- **Hardware** in sommige configuraties, afhankelijk van de manier waarop interfaces worden gekoppeld
- **Probleemoppervlak** wanneer iets niet wordt bezorgd
- **Benodigde kennis**, omdat beheerders een derde netwerkmodel moeten begrijpen

*Gebruik Reticulum wanneer transportonafhankelijkheid een echte vereiste oplost, niet alleen omdat het meer interfacetypen ondersteunt dan het alternatief.* Een probleem met de hoplimiet in één LoRa-mesh is een afstelprobleem voor Meshtastic of MeshCore. Het is geen transportonafhankelijkheidsprobleem, en Reticulum verandert dat niet.

______

## Bouw eerst één gezond mesh voordat je er drie fragmenteert

Als één protocol al aan je vereisten voldoet, **bouw dan één gezond netwerk** in plaats van meerdere kleinere netwerken die via bruggen aan elkaar zijn gekoppeld. Het principe "eerst één mesh" hoort de meeste bovenstaande keuzes te sturen.

Voor een communitynetwerk is **interoperabiliteit voor de mensen die het al gebruiken vaak belangrijker dan architecturale flexibiliteit.** Eén groot, werkend netwerk op één protocol heeft meer praktische waarde dan drie technisch interessante, gefragmenteerde netwerken die maar gedeeltelijk met elkaar praten.

### Bestaande Meshtastic-netwerken zijn belangrijk

**Wijs Meshtastic niet af alleen omdat MeshCore architecturale voordelen heeft voor vaste infrastructuur.** Als een stad al tientallen of honderden Meshtastic-knooppunten heeft, vormen die een echte infrastructuur en een echte community. Migreren kost meer dan een vergelijking van specificaties laat zien:

- **Geïnstalleerde hardware** die opnieuw geflasht of vervangen moet worden
- **Bestaande gebruikers** die het netwerk al kennen
- **Communitykennis** die rond de huidige installatie is opgebouwd
- **Repeaters die al zijn geplaatst**, soms op daken of masten waar toegang moeilijk te krijgen was
- **Configuratie-ervaring** van de mensen die het netwerk beheren
- **Bestaande kanalen** die mensen al volgen
- **Training** voor iedereen die een tweede systeem moet leren

De protocolkeuze is **deels een technisch probleem en deels een vraagstuk over acceptatie door de community.** De architectuur die op papier beter lijkt, wint niet automatisch als een bestaande, actieve community opnieuw moet beginnen.

______

## Het regionale netwerkprobleem

Neem een hypothetische uitrol over meerdere steden:

**Stad A, repeater, repeater, landelijke relay, repeater, Stad B, repeater, Stad C**

**Test langs deze keten groepsberichten en directe berichten afzonderlijk.** MeshCore kan een geleerd pad hergebruiken voor directe berichten, maar gebruikt nog steeds flooding voor groepen. Meshtastic kan op geschikte infrastructuurverbindingen de hopteller behouden. Elke heruitzending kost zendtijd. Geen van beide protocollen garandeert aflevering over het hele traject.

In dit scenario bepalen **hoplimieten, zendtijdbudget, routeringsgedrag en infrastructuurontwerp** of het netwerk van begin tot eind werkt. Op regionale schaal zijn de architectuurverschillen tussen Meshtastic en MeshCore niet langer theoretisch.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagram van een regionale meshnetwerkketen tussen drie steden via repeaters en een landelijke relay, met de toename van zendtijd en hops over de afstand" >}}

______

## RF blijft belangrijker dan het protocol

**Geen enkele slimme routeringssoftware maakt een fysiek onmogelijke RF-route mogelijk.** Controleer eerst de basis voordat je een dekkingsprobleem aan het protocol toeschrijft:

- **Antennehoogte** boven obstakels
- **Zichtlijn** tussen beide kanten van de verbinding
- **Vrije Fresnelzone**, die iets anders is dan zichtlijn met het blote oog
- **Verlies in de voedingskabel** door goedkope of te lange coax
- **Antennekwaliteit** en geschiktheid voor de gebruikte band
- **Ruisvloer** op de ontvangende locatie
- **Terrein** tussen de knooppunten
- **Plaatsing van knooppunten**, inclusief realistische verbeteringen
- **Linkmarge**, het verschil tussen het ontvangen signaal en het minimum dat nodig is om te decoderen

*Een goed geplaatste antenne van 2 dBi op een geschikte mast presteert vaak beter dan een slecht geplaatste antenne met hoge versterking bij een kelderraam.* De protocolkeuze bepaalt hoe het netwerk de verbindingen gebruikt die er zijn. Het maakt geen verbindingen mogelijk die de natuurkunde uitsluit.

### Betrouwbaarheid boven maximaal bereik

**Ontwerp een netwerk niet rond de uiterste afstand die een verbinding soms haalt.** Ontwerp het rond verbindingen die steeds werken.

Voor community- of noodcommunicatie heeft **betrouwbare bezorging over 15 mijl meer praktische waarde dan een verbinding die af en toe 40 mijl haalt en de rest van de tijd uitvalt.** Bouw overlappende dekking met betrouwbare infrastructuur in plaats van recordafstanden na te jagen. Dit geldt voor elk protocol.

______

## Welke kies je?

**Meshtastic is geschikt** als je waarde hecht aan een volwassen ecosysteem, een eenvoudige start, draagbare en mobiele gebruikers en compatibiliteit met een bestaande Meshtastic-community. Voor de meeste mensen die vanaf nul beginnen, is dit de standaardkeuze.

**Vaste repeaters** maken dekking planbaar, maar nemen flooding niet weg. Test beide protocollen met het verwachte groepsverkeer, de radio-instellingen en de geplande relaislocaties.

**Reticulum is geschikt** als het probleem verder gaat dan één LoRa-mesh en verschillende transporten of anders gescheiden netwerken in één adresseerbaar systeem moeten worden verbonden.

Voor een **licentievrij, energiezuinig regionaal communitynetwerk met groot bereik en vooral vaste repeaters** ligt MeshCore voor de hand. **Test groepsverkeer voordat je overstapt.** Vaste repeaters helpen bij de dekking, maar geven groepskanalen geen gerichte routes. *Als er in jouw omgeving al een gezond Meshtastic-netwerk bestaat, moet de meerwaarde groot genoeg zijn om versnippering van die community te rechtvaardigen.* Reticulum komt in beeld wanneer één meshprotocol of fysiek transport niet meer volstaat, niet simpelweg omdat het meer functies heeft.

______

## Bronnen

1. [Meshtastic-algoritme voor meshbroadcasts](https://meshtastic.org/docs/overview/mesh-algo/)
2. [LoRa-configuratie van Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Officiële website van MeshCore](https://meshcore.co.uk/)
4. [Reticulum Network Stack](https://reticulum.network/)
5. [Wat is Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Reticulum-interfaces configureren](https://reticulum.network/manual/interfaces.html)
7. [Vergelijkingsgids voor MeshCore en Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
