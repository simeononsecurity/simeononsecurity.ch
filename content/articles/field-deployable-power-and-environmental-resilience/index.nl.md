---
title: "Stroomvoorziening en omgevingsbestendigheid voor veldsystemen"
date: 2026-08-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Plan stroomvoorziening en omgevingsbescherming voor edge-computing in het veld. Bereken UPS-capaciteit en behandel zonnepanelen, accu's, tijdsynchronisatie, behuizingsklassen, aarding en overspanningsbeveiliging."
genre: ["Edge computing", "IT in het veld", "Stroomsystemen", "Hardware", "Rampenherstel", "Robuuste computers", "Netwerken"]
tags: ["UPS-capaciteit", "stroomvoorziening in het veld", "DC-servervoeding", "servervoeding met zonne-energie", "IP-klasse behuizing", "NEMA-klasse", "overspanningsbeveiliging", "aarding van elektronica", "servervoeding zonder netstroom", "stroomvoorziening voor mobiel datacenter", "berekening accuduur", "12V-servervoeding", "48V-DC-voeding", "IT-voeding met generator", "robuust stroomsysteem", "edge-node-voeding", "stroomvoorziening voor rampenherstel", "verplaatsbare server", "omgevingsbestendigheid", "expeditionaire stroomvoorziening", "LiFePO4-accupakket", "lithiumijzerfosfaat", "USB-PD-voeding", "vergelijking accutechnologie", "Network UPS Tools NUT", "UPS-bewaking via SNMP", "NTP-tijdsynchronisatie", "GPS-gestuurde klok"]
cover: "/img/cover/field-deployable-power-environmental-resilience-solar-ups.webp"
coverAlt: "Illustratie van een robuuste serveropstelling buiten, waar zonnepanelen een accubank opladen, met grafieken voor digitaal stroombeheer op een donkere achtergrond."
coverCaption: ""
ref: ["/articles/field-deployable-edge-compute-hardware-and-enclosure-selection", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/articles/field-it-tidbits-beyond-the-mini-datacenter", "/articles/the-role-of-ecc-memory-in-mitigating-data-corruption"]
---

**Een server voor gebruik in het veld is maar zo betrouwbaar als zijn stroombron.** De beste behuizing en snelste computer helpen niet wanneer de locatie zonder stroom komt te zitten en niets de belasting opvangt. *Stroomplanning is geen extraatje. Dit onderdeel van de installatie faalt waarschijnlijk als eerste.*

Dit is **deel twee van een serie van vier delen** over compacte servers en netwerkapparatuur die snel inzetbaar zijn. [Deel één](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) behandelde behuizingen en rekenkracht. Dit deel gaat over stroomvoorziening en bescherming tegen hitte, stof, water en elektrische storingen. [Deel drie](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) behandelt verbindingen en gegevensbeveiliging. [Deel vier](/articles/field-it-tidbits-beyond-the-mini-datacenter/) vat kleinere aandachtspunten samen.

______

## Een UPS voor gebruik in het veld dimensioneren

Een **UPS (uninterruptible power supply, oftewel noodstroomvoorziening)** overbrugt de tijd tussen een stroomstoring en het uitschakelen van apparatuur of het overnemen door een reservebron. De dimensionering voor gebruik in het veld begint met een eenvoudige berekening.

1. Tel het **vermogen van elk apparaat** in de koffer bij elkaar op, zoals de computer, switch, het accesspoint en de opslag.
2. Vermenigvuldig het totaal met **1,5 tot 1,6** om ruimte te laten voor de inschakelstroom.
3. Deel de opgegeven **capaciteit in wattuur** van de UPS door het totale vermogen van de belasting om de gebruiksduur in uren te schatten.

*De accucapaciteit neemt af door ouderdom en temperatuur. Behandel de opgegeven gebruiksduur daarom als een bestcasescenario, niet als garantie.* Reken op een kortere gebruiksduur in de praktijk, vooral in warme omgevingen waar accu's sneller capaciteit verliezen.

**[Schneider Electric / APC](https://www.apc.com/) publiceert uitgebreide richtlijnen voor UPS-dimensionering en accugedrag.** Hun basisregel geldt ook voor veldinstallaties: sluit de UPS rechtstreeks aan op de wandcontactdoos of generatoruitgang, nooit op een stekkerdoos met overspanningsbeveiliging. Sluit extra benodigde stopcontacten aan op een afzonderlijke PDU achter de UPS.

| Type UPS | Geschikt voor | Afweging |
|---|---|---|
| **Line-interactive UPS** | De meeste veldinstallaties met net- of generatorstroom | Korte omschakeltijd bij stroomuitval, meestal minder dan 10 ms |
| **Online-UPS met dubbele omzetting** | Gevoelige apparatuur op instabiele of vervuilde stroom | Zwaarder en duurder per watt |
| **DC-accupakket met ingebouwde omvormer** | Zeer compacte installaties waar een traditionele UPS niet past | Lager rendement doordat DC naar AC en terug wordt omgezet |

## DC-stroom: sla de omvormer over

Elke omzetting van AC naar DC verspilt energie in de vorm van warmte. **Rechtstreeks gebruik van DC-stroom voor apparatuur, wanneer die apparatuur dit ondersteunt, haalt een omzettingsstap en een mogelijk storingspunt weg.**

- **12V-systemen** passen bij kleine installaties, zoals singleboardcomputers, thin clients en kleine switches. Ze sluiten aan op gangbare accuspanning in voertuigen en boten.
- **48V-systemen** passen bij grotere installaties en komen overeen met de spanningsstandaard van telecomvoedingssystemen. Daardoor is telecomgeschikte DC-apparatuur vaak tweedehands voor weinig geld beschikbaar.
- Veel **netwerkswitches en accesspoints** ondersteunen al PoE of DC-ingang. Controleer het specificatieblad voordat je ervan uitgaat dat een omvormer nodig is.

*Een installatie die rechtstreeks op DC werkt, haalt meer gebruiksduur uit dezelfde accucapaciteit dan een AC-installatie met een omvormer ertussen. De verliezen van de omvormer vallen weg.*

## Hybride stroom met zonnepanelen en generator

Voor inzet die langer duurt dan één accupakket aankan, combineer je een accubank met een laadbron.

- **Draagbare zonnepanelen met laadregelaar** zijn geschikt voor overdag opladen en 's nachts op accu werken, op locaties met betrouwbare zon.
- **Een kleine invertergenerator** laadt snel en is niet afhankelijk van het weer, maar vereist brandstoflogistiek en maakt geluid. Dat is een serieus probleem bij heimelijke inzet of locaties waar weinig geluid gewenst is.
- **Een hybride opstelling**, met zonne-energie als hoofdbron en een generator als reserve, vangt de periode op waarin slecht weer de zonne-energie enkele dagen beperkt.

*Dimensioneer de accubank voor minstens één volledige dag autonomie zonder laadbron.* Een laadplan dat uitgaat van onafgebroken zon of gegarandeerde brandstofaanvoer is niet veerkrachtig.

{{< figure src="field-power-hybrid-solar-battery-generator.webp" alt="Diagram waarin een zonnepaneel en generator een centrale accubank opladen, die een compacte serverkoffer voedt via een DC- en AC-verdeeleenheid" >}}

## Accutechnologie voor veldpakketten

Niet elk accupakket is geschikt voor een koffer die afwisselend wordt geschud, verhit en bevroren. **De accutechnologie is net zo belangrijk als het aantal wattuur op het etiket.**

| Technologie | Geschikt voor | Afweging |
|---|---|---|
| **LiFePO4 (lithiumijzerfosfaat)** | De meeste veldinstallaties, lange levensduur in laadcycli en veiligste faalgedrag | Zwaarder per wattuur dan andere lithiumtechnologieën |
| **Lithium-ion (NMC/NCA)** | Installaties waar gewicht zwaar weegt en elke gram telt | Minder bestand tegen hitte en diepe ontlading, kortere levensduur in laadcycli |
| **Gesloten loodzuur (AGM/gel)** | Budgetinstallaties of als tijdelijke oplossing met materiaal dat al beschikbaar is | Zwaar, minder bruikbare capaciteit en de kortste levensduur in laadcycli van de drie |

**[Battery University's vergelijking van secundaire accutechnologieën](https://www.batteryuniversity.com/article/bu-107-comparison-table-of-secondary-batteries) beschrijft de afwegingen tussen laadcycli en specifieke energie uitgebreider.** *LiFePO4 is hier de uitzondering: het verdraagt hitte, ruwe behandeling en volledige ontlading veel beter dan de andere twee technologieën. Dat past bij wat een veldkoffer moet doorstaan.*

Hitte tast elke accutechnologie aan. **[Battery University's onderzoek naar capaciteitsverlies van lithium-ionaccu's](https://www.batteryuniversity.com/article/bu-808b-what-causes-li-ion-to-die) documenteert capaciteitsverlies in de praktijk dat ruim boven de laboratoriumwaarden van fabrikanten uitkomt zodra hitte en snelle laadcycli een rol spelen.** Daarom raadt deze serie aan om in warme klimaten met minder gebruiksduur te rekenen dan de nominale waarde.

## Apparaten voeden via USB-C PD

Veel thin clients, accesspoints en randapparatuur in compacte installaties accepteren nu stroom via **USB-C met de specificatie [USB Power Delivery (USB PD)](https://www.usb.org/document-library/usb-power-delivery)**. Dit vereenvoudigt de veldset aanzienlijk.

- **Eén USB-PD-powerbank vervangt meerdere apparaatspecifieke adapters**, zodat er minder kabels en adapters in de koffer nodig zijn.
- **Controleer welk vermogen het apparaat in de praktijk onderhandelt**, niet alleen het maximale vermogen van de kabel. Een onvoldoende sterke PD-bron kan een apparaat onder belasting ongemerkt vertragen of niet opladen.
- **Neem een PD-kabel mee die geschikt is voor het hoogste vermogen in de set.** Een goedkope kabel die alleen kan laden en voor 60 watt is gespecificeerd, beperkt een apparaat van 100 watt zonder duidelijke waarschuwing.

*USB-C PD vervangt de UPS en accubankdimensionering hierboven niet. Het is een handige voedingslaag voor kleinere randapparaten, niet de primaire stroomarchitectuur van de koffer.*

## De UPS bewaken in plaats van gissen

**Een UPS die een uur geleden ongemerkt op accu is overgeschakeld, beschermt niets als niemand dit merkt voordat de accu leeg is.** De meeste UPS'en geven hun status door via USB of een netwerkkaart. Een veldinstallatie moet die status uitlezen in plaats van erop te vertrouwen.

- **[Network UPS Tools (NUT)](https://networkupstools.org/) is een opensourceproject dat ruim duizend UPS-modellen ondersteunt** en een gemeenschappelijke set bewakings- en beheertools biedt, ongeacht het leveranciersprotocol.
- **Start automatisch een nette afsluiting van de computer zodra de accu een ingestelde grens bereikt.** Laat de UPS niet leeglopen terwijl een actief bestandssysteem plotseling stroom verliest.
- **Leg trends in accugezondheid en gebruiksduur vast**, niet alleen het huidige laadpercentage. Een accu die langzaam capaciteit verliest, vertoont geen duidelijk symptoom totdat hij uitvalt.

*Een UPS zonder bewaking is een accu met een onbekende vervaldatum.* NUT of de gelijkwaardige tool van de fabrikant één keer aansluiten kost een middag en maakt elke volgende inzet inzichtelijker.

## Tijd synchroniseren zonder internet

**Nauwkeurige tijd is in het veld belangrijker dan in veel installaties wordt onderkend.** Tijd beïnvloedt logcorrelatie, certificaatgeldigheid, versleutelde tunnelverbindingen en alle gedateerde bewijzen die de inzet oplevert.

- **Een lokale NTP-server in de koffer**, gesynchroniseerd met een GPS-ontvanger of een stratum-1-bron wanneer internet beschikbaar is, houdt alle apparaten op dezelfde tijd, ook tijdens verbindingsonderbrekingen.
- **Klokken die door GPS worden gestuurd werken zonder internetverbinding.** Dit is nuttig voor de mesh- en satellietscenario's met noodverbinding die later in deze serie aan bod komen.
- **Een klok die zelfs enkele minuten afwijkt, kan TLS-certificaatvalidatie en VPN-handshakes verstoren.** Een netwerkstoring blijkt dan een tijdsprobleem waar niemand aan dacht.

**De [NTP-versie 4-specificatie, RFC 5905](https://www.ietf.org/rfc/rfc5905.txt), beschrijft het protocol dat de meeste van deze hulpmiddelen gebruiken.** De dynamische ontdekking van servers maakt het mogelijk om met minimale configuratie een kleine NTP-server in de koffer alle andere apparaten te laten bedienen.

## IP- en NEMA-klassen voor de omgeving

Twee classificaties geven aan of een behuizing of apparaat de omgeving aankan waarin je het inzet. **Geen van beide is een synoniem voor 'robuust'. Beide gebruiken specifieke, testbare waarden.**

De **[IP-code (Ingress Protection)](https://en.wikipedia.org/wiki/IP_Code)**, vastgelegd in IEC-norm 60529, gebruikt twee cijfers. Het eerste cijfer geeft bescherming tegen vaste deeltjes zoals stof aan. Het tweede geeft bescherming tegen vloeistoffen zoals water aan.

| IP-klasse | Betekenis |
|---|---|
| **IP54** | Beschermd tegen stof en spatwater uit alle richtingen |
| **IP65** | Stofdicht en beschermd tegen waterstralen onder lage druk |
| **IP67** | Stofdicht en beschermd tegen tijdelijke onderdompeling tot 1 meter |
| **IP68** | Stofdicht en beschermd tegen voortdurende onderdompeling dieper dan 1 meter, volgens de door de fabrikant opgegeven diepte en duur |

Het **[NEMA-classificatiesysteem voor behuizingen](https://en.wikipedia.org/wiki/NEMA_enclosure_types)** is gebruikelijk bij industriële apparatuur in Noord-Amerika en gebruikt typenummers in plaats van cijferparen. **NEMA 3R** is geschikt voor algemeen buitengebruik. **NEMA 4X** voegt waterdichte en corrosiebestendige bescherming toe voor kust- of schoonmaakomgevingen. **NEMA 6P** is bedoeld voor tijdelijke onderdompeling.

*Stem de klasse af op de werkelijke dreiging op de inzetlocatie, niet op het hoogste beschikbare getal.* Een IP68-koffer voor een woestijninzet zonder blootstelling aan water is een onnodige uitgave. Besteed dat geld liever aan koeling of accucapaciteit.

## Temperatuur, trillingen en vocht

Naast stof en water beschadigen drie andere omgevingsfactoren ongemerkt elektronica in het veld.

- **Extreme temperaturen** verkorten de levensduur van accu's en vertragen of stoppen computers. Controleer het temperatuurbereik op het specificatieblad van elk onderdeel, niet alleen van de koffer.
- **Trillingen** maken connectoren los en verzwakken soldeerverbindingen tijdens herhaald vervoer. Rubberen isolatiesteunen tussen de computerlade en de koffer vangen trillingen op voordat ze de hardware bereiken.
- **Vocht en condensatie** ontstaan wanneer een koffer van een koude wagen naar warme, vochtige lucht gaat. Laat de gesloten koffer bij een groot temperatuurverschil enkele minuten acclimatiseren voordat je hem opent. Overweeg een klein droogmiddel in afgesloten koffers.

## Aarding en overspanningsbeveiliging

Stroombronnen in het veld, vooral generatoren, zijn minder stabiel en voorspelbaar dan netstroom. **Bij een overspanning of aardingsfout staat er op een veldlocatie geen elektricien klaar om je apparatuur te beschermen.**

- **Zorg voor een goede aarding** van de koffer en eventuele metalen rackrails voordat je stroom aansluit. Gebruik daarvoor een aardpen of, waar passend, de massa van het voertuig.
- **Gebruik overspanningsbeveiliging die geschikt is voor de stroombron.** Generatoren kunnen pieken veroorzaken die bij stabiele netstroom niet voorkomen.
- **Plaats de UPS tussen de onbewerkte stroombron en de apparatuur.** Doe dit niet andersom, zodat de overspanningsbeveiliging van de UPS de meest vervuilde stroom als eerste opvangt.

*Aarding overslaan om vijf minuten installatietijd te besparen, zet de hele koffer met apparatuur op het spel.*

## Controlelijst voor stroom en omgeving

- [ ] UPS of accubank met 1,5 tot 1,6 keer reservecapaciteit boven het totale vermogen gedimensioneerd
- [ ] Minstens één volledige dag gebruiksduur beschikbaar zonder laadbron
- [ ] IP- of NEMA-klasse van de behuizing afgestemd op de werkelijke dreiging op de locatie
- [ ] Temperatuurbereik van elk onderdeel gecontroleerd, niet alleen dat van de koffer
- [ ] Trillingsisolatie aanwezig bij vervoer over lange afstanden of onverharde wegen
- [ ] Goede aarding aangebracht voordat een generator of andere veldstroom wordt aangesloten

## Volgende stappen

Nu de stroomvoorziening en omgevingsbescherming geregeld zijn, is de volgende vraag hoe de inzet verbinding maakt met de buitenwereld en gegevens veilig houdt. Ga verder naar [deel drie: verbindingen en gegevensbeveiliging voor edge-nodes](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/).

Als je het nog niet hebt gelezen, behandelt [deel één: hardware en behuizingskeuze](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) de keuzes voor computer en koffer die bij dit stroomplan moeten passen. [Deel vier](/articles/field-it-tidbits-beyond-the-mini-datacenter/) behandelt kleinere aandachtspunten naast alles hierboven.
