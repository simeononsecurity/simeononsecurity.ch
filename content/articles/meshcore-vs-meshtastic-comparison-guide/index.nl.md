---
title: "MeshCore versus Meshtastic"
date: 2026-06-26
lastmod: 2026-11-25
toc: true
draft: false
description: "Vergelijk MeshCore en Meshtastic op basis van routering, bereik, zendtijd, infrastructuur, apparaatondersteuning en geschikte toepassingen."
genre: ["LoRa", "Meshnetwerken", "Offlinecommunicatie", "Noodcommunicatie", "Tactische communicatie", "Amateurradio", "Software met open broncode", "Rampenvoorbereiding", "Draadloze netwerken", "Privacy"]
tags: ["meshcore versus meshtastic", "meshtastic", "meshcore", "lora-meshnetwerk", "offlinecommunicatie", "meshtastic-vergelijking", "meshcore-vergelijking", "lora-radio", "meshnetwerken", "noodcommunicatie", "tactisch meshnetwerk", "offline radio", "meshtastic-protocol", "meshcore-protocol", "lora meshtastic", "rampencommunicatie", "mesh-radio", "opslaan en doorsturen", "lora-flooding", "LoRa-mesh", "t-beam meshtastic", "heltec lora", "rak wisblock", "offlineberichten", "meshnetwerkprotocol", "meshtastic 2.6", "lora-zendtijd", "noodradio"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Illustratie van twee LoRa-meshnetwerken: Meshtastic links met knooppunten die pakketten verspreiden en MeshCore rechts met gestructureerde routering, tegen een donkere achtergrond."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## Het korte antwoord

Meshtastic en MeshCore werken allebei op dezelfde goedkope LoRa-hardware. Beide laten je versleutelde berichten versturen zonder mobiel netwerk of internet. **De protocollen zijn niet onderling compatibel.**

**Beide protocollen gebruiken flooding voor groepsverkeer.** Gewone Meshtastic-clients onderdrukken overbodige heruitzendingen. Bij MeshCore stuurt alleen de infrastructuur door. Beide kunnen geleerde routes gebruiken voor directe berichten.

*Meshtastic is geschikt voor de meeste mensen.* De mobiele app is verzorgd, de community is groot, de documentatie is goed en de configuratie duurt minder dan 20 minuten.

**De basis van radiofrequenties is belangrijker dan firmware.** Geen van beide protocollen compenseert een slecht geplaatste antenne.

______

## Wat elk systeem doet

### Meshtastic

**Meshtastic** is een opensourceproject dat Kevin Hester in 2020 startte. De firmware maakt van gewone LoRa-hardware een meshnetwerk voor tekstberichten, zonder afhankelijkheid van internet of mobiele netwerken.

De firmware werkt op LoRa-hardware die veel gebruikers al bezitten of goedkoop kopen. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock en Seeed SenseCAP Indicator** ondersteunen Meshtastic zonder speciale hulpmiddelen. De iOS- en Android-apps worden goed onderhouden. Niet-technische gebruikers zijn binnen tien minuten online. Het ecosysteem bevat MQTT-bridges, Home Assistant-integratie en ATAK-plug-ins.

### MeshCore

**MeshCore** won aan populariteit in 2023 en 2024. De firmware werkt op veel van dezelfde LoRa-hardware, maar gebruikt een **hybride routeringsarchitectuur**. Dit is geen puur store-and-forward in de betekenis van vertragingsbestendige netwerken.

Repeaters verzorgen het grootste deel van het doorsturen. **Roomservers zijn optioneel.** Ze bewaren groepsberichten zodat clients ze bij een nieuwe verbinding ophalen. Clients gebruiken een begeleidende LoRa-radio en verbinden via infrastructuur wanneer die beschikbaar is, of communiceren rechtstreeks met nabije knooppunten zonder repeater.

______

## Het belangrijkste technische verschil

### Hoe Meshtastic routeert

Bij **[beheerde flooding](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** in Meshtastic annuleert een gewone client een geplande heruitzending als hij hetzelfde pakket eerder hoort langskomen. `ROUTER` en `ROUTER_LATE` kunnen het toch doorsturen. Voor `CLIENT_BASE` geldt die uitzondering voor verkeer van of naar een favoriet.

Sinds Meshtastic 2.6 gebruiken **directe berichten** eerst flooding om een route te ontdekken. Daarna proberen ze de geleerde volgende hop. Bij uitval kunnen ze terugvallen op flooding.

**De werkelijke beperking is zendtijd, niet het aantal knooppunten.** LoRa gebruikt gedeelde ISM-banden met regionale dutycyclelimieten, meestal 1% in Europa. Een netwerk met frequente GPS-bakens, telemetrie en actief kanaalverkeer raakt verzadigd voordat een absoluut maximum aan knooppunten wordt bereikt. Tien actieve knooppunten die vaak telemetrie verzenden veroorzaken meer botsingen dan vijftig stille sensoren. Dichte netwerken met enkele tientallen actieve gebruikers zien vaak meer zendtijdconcurrentie, maar er bestaat geen vaste bovengrens. De grens hangt af van de spreading factor, zendtijdpreset, telemetrie-intervallen, terrein en plaatsing van repeaters.

Meshtastic voegt verkeer toe met aankondigingen van knooppuntinformatie, batterijtelemetrie, GPS-pakketten en buurtdetectie. Recente firmwareversies hebben dit verminderd. *Het aanpassen van die instellingen lost prestatieproblemen vaak op voordat een protocolwissel nodig is.*

### Hoe MeshCore routeert

In MeshCore kan een eerste **direct bericht** via flooding een pad ontdekken. Latere directe berichten kunnen dat pad volgen en afhankelijk van de instellingen terugvallen op flooding. **[Openbare en besloten groepskanalen blijven flooding gebruiken](https://docs.meshcore.io/faq/#5-general)** via geschikte repeaters. Clientradio’s sturen geen pakketten van andere knooppunten door.

**Repeaters sturen verkeer tussen knooppunten door.** Roomservers kunnen groepsgesprekken hosten en berichten bewaren voor clients die later opnieuw verbinding maken.

**Zendtijd hangt af van het verkeer.** Groepsberichten kunnen bij beide protocollen meerdere relais bereiken. Een geleerd pad kan het aantal uitzendingen voor directe berichten verminderen. Relaislocaties, radio-instellingen en het aantal berichten blijven van belang.

Zonder repeater communiceren clients rechtstreeks wanneer ze binnen bereik zijn. *De architectuur presteert het best met infrastructuur. Infrastructuur is geen harde vereiste.*

______

## Hardware

Beide protocollen werken op dezelfde populaire LoRa-borden.

| Bord | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Ja | Ja |
| LILYGO T-Echo (nRF52840 + SX1262) | Ja | Ja |
| Heltec WiFi LoRa 32 V3 | Ja | Ja |
| RAK WisBlock 4631 | Ja | Ja |
| Seeed SenseCAP Indicator | Ja | Gedeeltelijk |
| Station G2 | Ja | Ja |

**Je flasht hetzelfde fysieke apparaat met een van beide firmwareversies.** Wisselen van protocol vereist geen nieuwe hardware. Experimenteren kost alleen tijd.

______

## Gemak van installatie

### Meshtastic instellen

1. Download firmware van meshtastic.org
2. Flash via de webflasher op flasher.meshtastic.org, zonder stuurprogramma's
3. Installeer de Meshtastic-app op je telefoon
4. Koppel via Bluetooth
5. Word lid van een kanaal of maak er een met een gedeelde naam en wachtwoord

**Totale tijd voor een eerste gebruiker: minder dan 20 minuten.** Kanaalversleuteling gebruikt vooraf gedeelde AES-256-sleutels. Het openbare standaardkanaal verbindt je meteen met elk Meshtastic-knooppunt binnen bereik. De app toont GPS-posities op een kaart wanneer knooppunten GPS hebben ingeschakeld.

### MeshCore instellen

1. Flash het infrastructuurknooppunt, repeater of roomserver met PlatformIO of vooraf gebouwde binaries
2. Flash de begeleidende clientradio
3. Installeer de MeshCore-app
4. Stel in de app het adres en de aanmeldgegevens van de infrastructuur in
5. Verbind de begeleidende radio via Bluetooth

**De installatie vraagt meer planning.** Je moet de rollen van knooppunten begrijpen voor de implementatie. Roomservers zijn optioneel, maar bewaren berichten voor offline clients. *Twee vrienden die snel willen communiceren kiezen Meshtastic. Een team dat een basisstation met repeater op het dak plaatst, kiest MeshCore.*

______

## Zendtijd is de echte beperking

Beide protocollen werken via LoRa. **LoRa-capaciteit komt voort uit zendtijd en dutycyclebudget, niet uit het aantal knooppunten.**

Deze factoren bepalen de netwerkprestaties:

- **Spreading factor.** Hogere waarden vergroten het bereik, maar vertragen de datasnelheid en verlagen de totale capaciteit.
- **Zendtijdpreset.** Presets voor groot bereik gebruiken meer dutycycle per bericht.
- **Telemetrie-interval.** GPS-, batterij- en omgevingspakketten van Meshtastic voegen continu verkeer toe.
- **Berichtfrequentie.** Actieve gebruikers die vaak verzenden beïnvloeden prestaties meer dan passieve knooppunten.
- **Plaatsing van repeaters.** Een goed geplaatste repeater verdeelt de belasting. Een slecht geplaatste repeater verhoogt de drukte.
- **Terrein.** Knooppunten die elkaar niet horen, voegen verkeer toe zonder concurrentie te veroorzaken. Knooppunten binnen bereik van veel andere knooppunten tegelijk veroorzaken wel concurrentie.

**Vaste repeaters** maken dekking planbaar, maar nemen flooding niet weg. Test beide protocollen met het verwachte groepsverkeer, de radio-instellingen en de geplande relaislocaties.

______

## Regelgeving

Prestatievergelijkingen verschillen per regio door andere regels:

- **915 MHz (VS):** geen vaste dutycyclelimiet onder FCC Part 15, maar er gelden vermogenslimieten.
- **868 MHz (EU):** 1% dutycycle onder ETSI, dus 36 seconden zendtijd per uur per kanaal.
- **433 MHz (EU/Azië):** veel regio's hanteren strengere limieten, vaak 10% op bepaalde deelbanden.

**De dutycyclebeperking van 1% in Europa is een harde wettelijke grens.** Dichte Meshtastic-netwerken in de EU bereiken de limieten sneller dan vergelijkbare netwerken in de VS. Het efficiëntere zendtijdgebruik van MeshCore levert naar verhouding meer voordeel op in regio's met dutycyclelimieten.

______

## Privacy en beveiliging

### Meshtastic

Meshtastic versleutelt verkeer van privékanalen met **vooraf gedeelde AES-256-sleutels**. Alle berichten op een kanaal delen dezelfde sleutel. Iedereen met de kanaalsleutel kan alle berichten lezen, ook GPS-posities. **Het openbare standaardkanaal gebruikt een bekende sleutel die met de firmware wordt verspreid**, dus het openbare verkeer biedt geen vertrouwelijkheid tegenover mensen met Meshtastic in de buurt.

GPS-posities op een versleuteld privékanaal zijn alleen zichtbaar voor knooppunten met de sleutel. Op het openbare kanaal ziet iedereen de posities. *Dit is van belang wanneer tracking operationele gevolgen heeft.*

Meshtastic 2.6 verbeterde de routering van directe berichten. Groepsverkeer gebruikt nog steeds de kanaal-PSK. Directe berichten geven meer isolatie, maar zijn niet end-to-end versleuteld in de betekenis van het Signal Protocol.

### MeshCore

**Routering verbergt geen radioactiviteit.** Ga er niet van uit dat een geleerd pad verbergt welke repeaters zenden. **Directe berichten gebruiken versleuteling per contact**, niet een gedeelde kanaalsleutel. Andere knooppunten op dezelfde infrastructuur kunnen je directe gesprek niet ontsleutelen, ook niet bij gebruik van dezelfde repeater.

Infrastructuurknooppunten sturen versleuteld verkeer door. Bij directe berichten met versleuteling per contact stuurt de repeater ciphertext door zonder die te ontsleutelen. Bij roomverkeer zien roomservers de inhoud van de rooms die ze hosten. *De relevante vraag is of jij de roomserver beheert.*

MeshCore biedt geen strikte end-to-endversleuteling zoals het Signal Protocol. **Versleuteling per contact voor directe berichten verbetert de bescherming aanzienlijk ten opzichte van een gedeelde kanaal-PSK.** Beoordeel de implementatiedetails zorgvuldig voor toepassingen met hoge risico's.

______

## Stroomverbruik

**Minder zenden verbetert de batterijduur van clientknooppunten.** Meshtastic-telemetrie, GPS-uitzendingen en beheerst flooding gebruiken elk zendtijd. Je vermindert de extra belasting sterk door telemetrie-intervallen aan te passen en GPS-uitzendingen op knooppunten zonder GPS uit te schakelen.

**Vergelijk de accuduur bij dezelfde belasting.** Telemetrie, zendtijd en de rol van het knooppunt tellen ook mee.

______

## Netwerkbestendigheid

**Meshtastic-flooding is bestand tegen storingen.** Het verlies van een relayknooppunt heeft vaak weinig operationeel effect, omdat andere knooppunten verkeer vanzelf omleiden. Je hoeft niet vooraf te weten welke knooppunten beschikbaar zijn. Het mesh herstelt zichzelf passief.

**MeshCore leunt meer op de plaatsing van repeaters.** Een goed ontworpen MeshCore-netwerk met voldoende repeaterdekking presteert voorspelbaar. Bij verlies van de enige repeater in een dekkingsgebied verliezen knooppunten die ervan afhankelijk zijn de verbinding. *MeshCore beloont planning vooraf. Meshtastic is toleranter bij uitval van knooppunten.*

**Geleerde paden en flooding lossen verschillende problemen op.** Een alternatief pad helpt alleen als een ander geschikt relais het pakket kan horen en doorsturen.

______

## GPS en positiebepaling

**Meshtastic heeft een sterker GPS-ecosysteem.** De mobiele app bevat een kaartweergave. Knooppunten van de community sturen via MQTT-gateways gegevens naar openbare kaarten zoals meshmap.net. GPS-telemetrie is een kernfunctie. Posities delen voor wandelgroepen, zoek- en reddingscoördinatie en evenementen is goed ontwikkeld.

MeshCore richt zich niet op positiebepaling. *Als GPS-overzicht een primaire eis is, is het ecosysteem van Meshtastic in 2026 verder ontwikkeld en volwassener.*

______

## Ecosysteem en community

Meshtastic heeft een **grotere community**:

- Actieve Discord met duizenden leden
- Actieve subreddit op r/meshtastic
- Uitgebreide documentatie op meshtastic.org
- Integraties van derden voor MQTT, Home Assistant, Node-RED, ATAK en Python-bibliotheken
- Regelmatige firmwareversies
- Veel hardwarehandleidingen van de community

MeshCore groeit, maar blijft kleiner. *Er zijn minder forumberichten, handleidingen en integraties van derden. Als iets stukgaat, zoek je antwoorden in de firmwarebroncode of de Discord van het project in plaats van bestaande oplossingen te vinden.*

Beide projecten zijn open source, maar de licenties verschillen. **Meshtastic gebruikt een BSD-achtige licentie. MeshCore gebruikt GPL.** Sommige organisaties houden daar bij implementatie en distributie rekening mee.

______

## Wanneer Meshtastic wint

**Kleine informele groepen.** Een wandelclub die offline berichten en het delen van posities wil, kiest Meshtastic. De configuratie is eenvoudig, de kaart werkt goed en het netwerk organiseert zichzelf.

**Mobiele toepassingen.** Gebruikers die door terrein bewegen en onvoorspelbaar komen en gaan, passen bij de zelforganiserende flooding van Meshtastic. Er hoeft geen vooraf geplande infrastructuur te zijn voor mobiele knooppunten.

**Toepassingen voor consumenten.** Niet-technische mensen stellen hun eigen apparaat in zonder hulp. De instap bij Meshtastic is laag.

**Snelle inzet voor een evenement.** Festivalcommunicatie, wedstrijdcoördinatie of zoek- en reddingswerk dat vandaag start en volgende week weer stopt. De snelle configuratie en het ontbreken van verplichte infrastructuur maken Meshtastic praktisch.

**GPS-tracking.** Voor positiebepaling als primair gebruik is Meshtastic in 2026 de juiste keuze.

______

## Wanneer MeshCore wint

**Geplande infrastructuur.** Je hebt een repeater op het dak of een roomserver met betrouwbare stroom. MeshCores hybride routering benut vaste infrastructuur.

**Grote netwerken met eigen infrastructuur.** **Test groepsverkeer voordat je overstapt.** Vaste repeaters helpen bij de dekking, maar geven groepskanalen geen gerichte routes.

**Berichten bewaren bij onderbroken verbindingen.** Roomservers slaan berichten op en bezorgen die wanneer clients opnieuw verbinding maken. **Dit is een van de concreetste praktische voordelen van MeshCore ten opzichte van Meshtastic.**

**Scheiding tussen vaste en mobiele knooppunten.** Sommige knooppunten moeten infrastructuur leveren en andere moeten clients zijn. Het rollenmodel van MeshCore is hiervoor ontworpen.

**Regio's met dutycyclebeperkingen.** Europese implementaties onder de ETSI-limiet van 1% profiteren meer van MeshCores efficiënte zendtijdgebruik.

**Versleuteling per contact.** Voor versleuteling van directe berichten is het model van MeshCore betekenisvol beter dan de kanaal-PSK-aanpak van Meshtastic.

______

## Waar elk systeem tekortschiet

### Zwakke punten van Meshtastic

- **Zendtijdconcurrentie op schaal.** Dichte netwerken met drukke standaardinstellingen, frequente GPS-uitzendingen en actieve kanalen gaan achteruit. Pas de configuratie aan voordat je van protocol wisselt.
- **Geen berichtbewaring zonder infrastructuur.** Zonder MQTT-gateway blijven gemiste berichten gemist.
- **Privacy van posities op het openbare kanaal.** Iedereen die meeluistert ziet alle GPS-uitzendingen. Dit past bij informeel gebruik, niet bij eisen voor operationele veiligheid.
- Grote firmwareversies veroorzaken soms compatibiliteitsproblemen totdat het netwerk naar een passende versie is bijgewerkt.

### Zwakke punten van MeshCore

- **Complexe installatie.** Je moet infrastructuurrollen begrijpen voordat je het zinvol inzet.
- **Kleinere community.** De documentatie, handleidingen en integraties van derden van Meshtastic zijn verder ontwikkeld.
- **Minder hardwarekeuze.** MeshCore richt zich op een kleinere lijst ondersteunde apparaten.
- **Minder volwassen mobiele apps.** Ze werken, maar zijn minder gepolijst dan de apps van Meshtastic voor iOS en Android.
- **Afhankelijkheid van infrastructuur voor optimale prestaties.** Zonder repeaters communiceren clients rechtstreeks, maar verdwijnt de routeringsefficiëntie. Zonder vaste infrastructuur wordt het architectuurvoordeel niet benut.
- **Netwerkherstel.** Bij verlies van een repeater in een gebied verliezen afhankelijke knooppunten de verbinding. Meshtastic-flooding verdraagt uitval beter.
- **Geen protocolinteroperabiliteit.** MeshCore en Meshtastic wisselen geen berichten uit. Dezelfde hardware ondersteunt een van beide firmwareversies, maar bij gebruik van beide beheer je twee aparte netwerken.

______

## Radiofrequentie is belangrijker dan firmware

**Antennekwaliteit, antennehoogte, kabelverlies, terrein en radio-instellingen beïnvloeden de netwerkprestaties sterker dan de firmwarekeuze.**

Een goed geplaatst Meshtastic-knooppunt op een heuvel met een goede antenne presteert beter dan een slecht geplaatste MeshCore-repeater in een metalen behuizing in een kelder. De vergelijking gaat uit van ongeveer dezelfde fysieke installatiekwaliteit.

Controleer het volgende voordat je van protocol wisselt om een prestatieprobleem op te lossen:

- Antenneverbindingen zijn schoon en hebben weinig verlies.
- Knooppunten staan zo hoog als praktisch haalbaar.
- De zendtijdpreset past bij het gewenste bereik.
- **Telemetrie-intervallen verzadigen het kanaal niet.**
- De spreading factor past bij de knooppuntdichtheid.

______

## Overzicht naast elkaar

| Factor | Meshtastic | MeshCore |
|---|---|---|
| Netwerkmodel | Beheerde flooding voor kanalen, geleerde volgende hop voor directe berichten | Flooding voor kanalen, geleerd repeaterpad voor directe berichten |
| Installatiemoeilijkheid | Eenvoudig | Gemiddeld tot moeilijk |
| Ontwerp voor schaal | Flexibel, prestaties dalen door zendtijdconcurrentie | Ontworpen voor grotere geplande netwerken |
| Kwaliteit mobiele app | Uitstekend | Functioneel |
| Communitygrootte | Zeer groot | Groeit |
| GPS/positiebepaling | Sterk, ecosysteem is ontwikkeld | Beperkte focus |
| Berichten bewaren | Nee. MQTT-gateway vereist | Ja, optionele roomservers |
| Versleuteling directe berichten | Kanaal-PSK | Versleuteling per contact |
| Infrastructuur nodig | Niet vereist | Geoptimaliseerd voor infrastructuurknooppunten |
| Netwerkherstel | Bestendig en zelfherstellend | Afhankelijk van repeaterplaatsing |
| Hardwareondersteuning | Breed | Gerichte selectie |
| Geschikt voor | Mobiele, ad-hoc- en kleine groepen | Geplande implementaties met vaste infrastructuur |

______

## Welke kies je?

**Begin met Meshtastic.** Binnen een middag ben je in de lucht. Je vindt mensen om mee te testen. De app werkt en de documentatie is uitstekend. Meshtastic 2.6 verkleint met next-hop-routering voor directe berichten het efficiëntieverschil voor punt-tot-puntverkeer.

**Overweeg MeshCore** als je aparte repeaters of optionele ruimteservers nodig hebt die berichten bewaren voor terugkerende gebruikers.

Pas vóór een protocolwissel **je Meshtastic-installatie aan**. Verlaag telemetrie-intervallen. Schakel GPS-uitzendingen uit op knooppunten zonder GPS. Stem de zendtijdpreset af op de knooppuntdichtheid. *Veel netwerken met prestatieproblemen hebben configuratieproblemen, geen protocolproblemen.*

**Beide meshes profiteren van goed geplaatste relais.** Welke knooppunten doorsturen, hangt af van hun rollen en het verkeer.

*Bouw je een netwerk dat LoRa moet verbinden met packet radio, wifi of internet in plaats van één LoRa-mesh?* Bekijk de **[vergelijkingsgids voor Meshtastic, MeshCore en Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** voor de rol van transportonafhankelijke netwerken en de situaties waarin ze onnodige complexiteit toevoegen.
