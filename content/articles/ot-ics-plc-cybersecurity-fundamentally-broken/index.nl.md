---
title: "Waarom OT-, ICS- en PLC-cyberbeveiliging nog steeds tekortschiet"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Lees waarom OT-beveiliging achterblijft door verouderde ontwerpen, operationele beperkingen en reële aanvalsroutes."
tags: ["OT-beveiliging", "ICS-beveiliging", "PLC-beveiliging", "IoT-beveiliging", "industriële cyberbeveiliging", "SCADA-beveiliging", "NIST 800-82", "IEC 62443", "NERC CIP", "operationele technologie", "kritieke infrastructuur", "analoge sensoren", "netwerkisolatie", "verouderde systemen", "mening over cyberbeveiliging", "industriële controlesystemen", "SCADA", "Stuxnet", "beveiliging van controlesystemen", "cyberfysieke beveiliging", "beveiliging van de toeleveringsketen", "OT-toeleveringsketen"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Illustratie met links een oude PLC met analoge functies en rechts een moderne controller met cyberbeveiliging en digitale interfaces, tegen een donkere achtergrond."
coverCaption: ""
---

Ik heb lang genoeg in industriële omgevingen gewerkt om dit helder te zeggen: **de meeste programma's voor OT-, ICS- en PLC-cyberbeveiliging zijn theater**. Ze leveren documentatie voor naleving. Ze leveren geen beveiliging. Kritieke infrastructuur wordt getroffen in de kloof tussen die twee.

Dit is geen aanval op de mensen die normen opstellen. **NIST SP 800-82 Rev 3**, **IEC 62443** en **NERC CIP** zijn technisch degelijke documenten. De richtlijnen zijn niet het probleem. *Het probleem is op welke systemen ze worden toegepast.*

## Systemen zijn gemaakt om te werken, niet om beveiligd te worden

**PLC's, SCADA-systemen, gedistribueerde besturingssystemen (DCS) en verouderde industriële IoT-apparatuur** zijn ontworpen met één doel: lange tijd betrouwbaar werken. **Beschikbaarheid was het enige ontwerpdoel dat bespreking waard was.** Vertrouwelijkheid, integriteit, authenticatie en logboekregistratie waren geen vereisten. Vaak waren het niet eens begrippen waaraan ontwerpers dachten.

NIST SP 800-82 Rev 3 (2023) is daar eerlijk over. Het beschrijft OT-omgevingen met *"unieke eisen voor prestaties, betrouwbaarheid en veiligheid"*, waarin *"beveiliging de systeemwerking niet mag hinderen"*. Lees dat opnieuw. **Het belangrijkste beveiligingsdocument voor operationele technologie erkent expliciet dat beveiliging op de tweede plaats komt.** Dat is geen fout in het document. Het beschrijft de omgeving nauwkeurig.

Je kunt geen rolgebaseerde toegangscontrole toepassen op een PLC die geen gebruikersrollen kent. Je kunt firmware niet bijwerken op apparatuur waarvan de fabrikant niet meer bestaat. **Verouderde seriële protocollen, waaronder Modbus RTU en Profibus DP, hebben geen ingebouwde authenticatie.** Ze sturen opdrachten en gegevens naar iedereen die erom vraagt. Ze controleren niet wie er vraagt.

*De richtlijnen zijn goed. De systemen kunnen er vaak niet aan voldoen.* Dat zijn verschillende problemen.

## Er zijn twee heel verschillende soorten OT-systemen

**Verouderde PLC's uit de jaren tachtig tot begin jaren 2000** zijn ontworpen voor geïsoleerde, uitsluitend fysieke bediening. Ze draaien op eigen besturingssystemen. Vaak worden ze beheerd vanaf engineeringwerkstations die ook het bedrijfsnetwerk raken. Hun configuraties staan in formaten zonder integriteitscontrole. Deze systemen vormen een aanzienlijk deel van de infrastructuur voor waterzuivering, energieopwekking, productie en vervoer.

**Moderne controllers met beveiligingsfuncties zijn anders.** Siemens, Schneider, Rockwell, Beckhoff en Phoenix Contact leveren nu platforms met veilig opstarten, ondertekende firmware, rolgebaseerde toegangscontrole, TPM-ondersteunde identiteit en versleutelde communicatie. EtherNet/IP CIP Security, PROFINET Security Class en OPC UA met authenticatie zijn functies op actuele hardware.

Ik doe moderne OT-beveiligingstechniek niet af als onbelangrijk. De vooruitgang is echt. **Het probleem is dat de meeste geïnstalleerde systemen niet modern zijn.** Wanneer mensen over "OT-cyberbeveiliging" praten, beschrijven ze meestal een poging om een twintig jaar oude programmeerbare controller te beschermen met een cyberbeveiligingskader uit 2023. Dat is de kloof die ik bedoel.

## Wat echt werkt

**Fysieke beveiliging en netwerkisolatie zijn de betrouwbaarste maatregelen voor verouderde OT-omgevingen.** Alle grote beveiligingskaders voor ICS zeggen hetzelfde. IEC 62443 deelt OT-omgevingen op in beveiligingszones met vastgelegde verbindingen. Zo moet laterale beweging door gecontroleerde grenzen lopen in plaats van over een vlak netwerk.

Netwerkisolatie verkleint het netwerkgebonden aanvalsoppervlak aanzienlijk, maar verwijdert niet elk risico. Verwijderbare media, toegang door insiders, onderhoudslaptops, tijdelijke engineeringverbindingen en compromittering van de toeleveringsketen zijn bekende toegangsroutes naar systemen zonder netwerkblootstelling. **Stuxnet**, dat via geïnfecteerde USB-sticks een geïsoleerde Iraanse centrifuge-installatie bereikte, is het klassieke voorbeeld. *Netwerkisolatie is noodzakelijk. Ze is niet voldoende.*

**Menselijk toezicht op fysieke procesparameters** blijft een van de betrouwbaarste detectiemethoden. Een getrainde operator die druk, temperatuur en stroming in realtime volgt, merkt zaken op die geen inbraakdetectiesysteem ziet. Een IDS kan niet controleren of de digitale waarde overeenkomt met de fysieke werkelijkheid.

Maatregelen die risico in de juiste situaties verlagen:

- **Datadiodes** laten telemetrie naar buiten gaan zonder inkomende verbindingen toe te staan
- **Applicatiewhitelisting** op HMI-werkstations beperkt wat wordt uitgevoerd op computers met toegang tot besturingssystemen
- **Passieve platformen voor anomaliedetectie** van Claroty, Dragos en Nozomi analyseren verkeer zonder communicatie op het besturingsvlak aan te raken
- **Netwerksegmentatie** tussen OT-zones vertraagt laterale beweging zonder volledige fysieke isolatie te eisen
- **Zero-trustprincipes**, genoemd in NIST SP 800-82 Rev 3, voegen sessiegebonden verificatie toe aan sommige moderne OT-architecturen

*Geen van deze maatregelen lost de onderliggende ontwerpbeperkingen op. Ze verlagen het risico aan de randen van systemen die nooit hiervoor zijn ontworpen.*

## Analoge signalen kunnen niet worden geauthenticeerd

**Stroomlussen van 4-20 mA, signalen van 0-10 V, thermokoppeluitgangen en RTD-metingen worden als veranderende elektrische signalen verzonden.** Het fysieke signaal heeft geen methode om de echtheid te controleren. Wie het juiste signaal op de draad zet, wordt geloofd.

Stuxnet maakte dit concreet. De aanval manipuleerde PLC-logica op Siemens S7-controllers en speelde tegelijk eerder opgenomen normale procesgegevens af op bedieningsinterfaces. **Operators zagen normale waarden op hun scherm terwijl de centrifuges boven hun bedrijfsgrenzen werden gedreven.** De misleiding hield lang genoeg stand om fysieke schade te veroorzaken die op apparatuuruitval leek, niet op een aanval.

Elektromagnetische storing door voedingskabels, frequentieregelaars, bliksem en slechte aarding verstoort analoge metingen tijdens normaal bedrijf. IEC 61000 bestaat om die reden. Industriële installaties gebruiken afgeschermde bekabeling, goede aarding, filters en fysieke scheiding om dit te beperken.

Moderne slimme veldapparaten zetten analoge metingen intern om naar digitaal voordat ze die via HART-IP, WirelessHART, EtherNet/IP CIP Security of OPC UA verzenden. Moderne hardware ondersteunt geauthenticeerde digitale communicatie op apparaatniveau. **De analoge 4-20mA-draad tussen een verouderde zender en een verouderde PLC-ingang biedt geen authenticatie en zal dat nooit doen.** Een aanzienlijk deel van de geïnstalleerde instrumentatie gebruikt die draad nog steeds.

## Sensorvalidatie is een veiligheidsmaatregel, geen cyberbeveiligingsmaatregel

Procesveiligheidssystemen gebruiken **redundante sensorkeuze**. Een 2-uit-3-opstelling waarin twee sensoren 230 PSI aangeven en één 14 PSI, markeert de uitschieter. Dit biedt beperkte weerstand tegen manipulatie van één sensor. *Het is een procesveiligheidsmaatregel, geen cyberbeveiligingsmaatregel.*

Standaard-PLC's valideren hun analoge ingangen niet cryptografisch. Een signaalgenerator op de lus is niet te onderscheiden van een legitieme zender. De PLC leest de stroom en reageert erop.

**Veiligheidsbesturingssystemen moesten de onafhankelijke laatste verdedigingslinie zijn.** In 2017 richtte **TRITON** (ook bekend als **TRISIS**) zich op Schneider Electric Triconex SIS-eenheden met als doel die laag uit te schakelen. De aanvallers bereikten het veiligheidssysteem via het netwerk van engineeringwerkstations. *De onafhankelijkheid van die laag hing af van netwerksegmentatie die niet was gehandhaafd.*

IEC 62443-3-3, IEC 62443-4-2 en de afstemming op functionele veiligheid volgens IEC 61511 verwerken deze les. Jarenlang behandelden afzonderlijke groepen procesveiligheid en cyberbeveiliging als aparte vakgebieden. **TRITON bewees in de praktijk wat onafhankelijke analyses al theoretisch hadden aangetoond:** wie het veiligheidssysteem uitschakelt voordat de gevaarlijke toestand ontstaat, verwijdert de laatste maatregel die fysieke gevolgen voorkomt.

## De toeleveringsketen is een aanvalspad dat je waarschijnlijk mist

**De meeste OT-beveiligingsprogramma's richten zich op de netwerkarchitectuur. Veel recente OT-inbraken gebruikten toegangspunten die netwerkarchitectuur niet tegenhoudt.**

Risico's in de OT-toeleveringsketen zijn onder meer:

- **Firmware-integriteit vóór installatie**, vooral als apparatuur de fabriek of distributeur verlaat met niet-geverifieerde firmware
- **Sessies voor externe toegang van leveranciers**, die blijvende blootstelling vormen op locaties die afhankelijk zijn van ondersteuning door de fabrikant
- **Engineeringwerkstations** die zowel met het bedrijfsnetwerk als het OT-netwerk zijn verbonden, vaak uit operationeel gemak
- Het ontbreken van **software bill of materials (SBOM's)** bij de meeste verouderde OT-implementaties, waardoor softwarecomponenten vrijwel niet te volgen zijn
- **Onderhoudscontractors** die laptops en USB-sticks meenemen naar operationeel geïsoleerde omgevingen
- **Ondersteuning voor ondertekende firmware-updates**, die de meeste oudere platforms missen

NIST SP 800-82 Rev 3 besteedt specifieke onderdelen aan leveranciersafhankelijkheden en toegang door derden. *Als je netwerk intern geïsoleerd is, maar je apparatuurleverancier een permanent portaal voor externe toegang tot je engineeringnetwerk beheert, heb je geen geïsoleerd netwerk. Je hebt een opening met een deur die iemand anders beheert.*

## Oude systemen beveiligen kost meer dan nodig zou moeten zijn

Elk PLC-programma is op maat geschreven voor een specifiek proces. De logica voor een drukstootregelsysteem in een raffinaderij verschilt volledig van die voor een chloorproces in een waterzuiveringsinstallatie of een turbineregelaar. Dat is geen keuze. Fysieke processen zijn verschillend.

**Het beveiligen van verouderde OT-systemen kost vaak meer dan verwacht** door eisen voor technische validatie, noodzakelijke uitvaltijd, beperkingen in leveranciersondersteuning, documentatiehiaten en testcycli die langer duren dan begroot. Zonder ondersteuning van de leverancier kunnen de kosten voor beveiliging soms even hoog worden als vervanging of hoger.

**Naleving van NERC CIP voor cyberactiva van het grootschalige elektriciteitssysteem kost afzonderlijke nutsbedrijven jaarlijks miljoenen dollars.** Een enquête van de American Public Power Association uit 2019 documenteerde uiteenlopende nalevingskosten en een onevenredige last voor kleinere nutsbedrijven. Veel waterbedrijven en kleinere nutsbedrijven vallen buiten NERC CIP en hebben geen vergelijkbare nalevingsplicht.

## De systemen moeten worden vervangen

**Oude OT-systemen vervangen is het juiste antwoord.** Bij grote locaties betekent dit tientallen miljoenen dollars, lange overgangsperiodes en het risico om complexe operationele kennis tijdens de migratie verkeerd vast te leggen. Dat zijn reële kosten en risico's.

Industrieadviezen van CISA en ICS-CERT bevelen aan compenserende maatregelen toe te passen terwijl de vervanging wordt voorbereid. Dat is een rationele reactie op de beperkingen. *Kort gezegd erkennen ze dat volledige beveiliging op oude apparatuur niet haalbaar is. Pas passende maatregelen toe en plan de uiteindelijke vervanging.*

**In de praktijk blijven veel van deze systemen nog tientallen jaren in gebruik.** Dat is een financierings- en beleidsprobleem. De technische gemeenschap heeft duidelijk gemaakt wat moet gebeuren. De operationele budgetten en vervangingsplanningen zijn niet meegegroeid.

## Netwerkverbindingen maken OT-systemen vaak kwetsbaarder

Veel organisaties hebben externe toegang en monitoring toegevoegd aan OT-omgevingen die oorspronkelijk geïsoleerd waren. Het operationele argument is eenvoudig: zicht op afstand versnelt de reactie en leveranciers bieden sneller ondersteuning via een externe verbinding. **Het beveiligingsgevolg is dat systemen zonder externe aanvalsoppervlakte er nu wel een hebben.**

Het **incident bij de waterzuiveringsinstallatie in Oldsmar in 2021** vond plaats via een externe TeamViewer-verbinding. De aanvaller wijzigde de dosering van natriumhydroxide via een legitiem hulpmiddel voor externe toegang dat voor het gemak was toegevoegd. Het **incident bij Colonial Pipeline in 2021** begon met een inbraak in een IT-netwerk. De beheerder legde de OT-pijpleiding uit voorzorg stil omdat niet kon worden vastgesteld of het OT-netwerk onaangetast was. *De aanval drong niet rechtstreeks het OT-netwerk binnen. De onzekerheid over een mogelijke inbraak veroorzaakte de stillegging.*

Netwerkverbindingen toevoegen aan oude OT-systemen voor operationeel gemak, zonder de verbinding volgens passende normen te ontwerpen, **levert in veel gevallen meer risico op dan voordeel**. Het Purdue-model blijft nuttig als referentiearchitectuur, maar NIST beschouwt het niet langer als voldoende op zichzelf. Moderne IIoT, cloudverbindingen, externe bediening en hybride architecturen vragen om zorgvuldiger ontwerp dan alleen zonering.

## Voldoen aan geschreven normen is geen beveiliging

NIST SP 800-82 Rev 3, IEC 62443 en NERC CIP beschrijven passende maatregelen voor deze systemen. Ik wijs ze niet af. Ik benadruk wat ze expliciet zeggen: **niet elk OT-systeem kan elke maatregel uitvoeren.** De kaders gebruiken beveiligingsniveaus en compenserende maatregelen, juist omdat de systemen vaak niet aan alle eisen kunnen voldoen.

Het verschil tussen wat normen beschrijven en wat een bepaalde oude installatie kan bereiken, is geen documentatiefout. De systemen ondersteunen die maatregelen niet. De richtlijnen erkennen dat. **Een geslaagde nalevingsaudit voor verouderde OT betekent niet dat de omgeving veilig is.** Het betekent dat je de aanwezige compenserende maatregelen hebt gedocumenteerd en een auditor ze heeft geaccepteerd.

Het risicobeheerkader van NIST stelt expliciet dat na toepassing van maatregelen restrisico overblijft. Risico accepteren is een van de vier uitkomsten van het kader, naast risico overdragen, beperken en vermijden. *Erkenning van restrisico is opgenomen in de officiële richtlijnen.* **Wie zegt dat naleving je OT-omgeving veilig maakt, beweert iets wat de aangehaalde kaders niet ondersteunen.**

## Wat je met oude OT moet doen

Als je oude OT-omgevingen beheert:

- **Beschouw netwerkisolatie als je belangrijkste maatregel** en controleer alles wat de OT-grens passeert
- **Geef engineeringwerkstations een eigen beveiligingsplan.** Ze raken beide omgevingen en zijn vaak het toegangspunt
- **Beheer en registreer alle verwijderbare media** in OT-zones
- **Controleer externe toegang door leveranciers** en sluit sessies die niet actief worden gebruikt
- Implementeer redundante sensormonitoring als het procesontwerp dat toelaat
- **Maak een vervangingsplan met echte kostenramingen**, ook als vervanging nog jaren duurt
- **Beschouw het afronden van een nalevingsaudit niet langer als een beveiligingsmijlpaal**

Als je nieuwe OT-systemen aanschaft:

- **Neem beveiligingseisen op in de inkoopspecificatie** voordat leveranciers reageren
- Kies platforms met gedocumenteerde ondersteuning voor geauthenticeerde communicatie, ondertekende firmware-updates en rolgebaseerde toegangscontrole
- **Ontwerp IT/OT-grenzen als expliciete verbindingen volgens IEC 62443**, niet als vaag beleid om "ze gescheiden te houden"
- **Eis SBOM's voor OT-softwarecomponenten** als contractuele oplevering

De industrie heeft het probleem goed gedocumenteerd. De normen zijn technisch juist. *Systemen in het veld kunnen vaak niet voldoen aan wat de normen voorschrijven.* Open erkenning daarvan is het begin van verantwoord beheer van het resterende risico.

## Bronnen

- NIST SP 800-82 Rev 3: gids voor beveiliging van operationele technologie (OT) (2023)
- IEC 62443: reeks normen voor beveiliging van industriële automatiserings- en besturingssystemen
- IEC 62443-3-3: systeemeisen voor beveiliging en beveiligingsniveaus
- IEC 62443-4-2: technische beveiligingseisen voor IACS-componenten
- IEC 61511: functionele veiligheid voor instrumentele veiligheidssystemen
- NERC CIP: normen voor bescherming van kritieke infrastructuur van het grootschalige elektriciteitssysteem
- IEC 61000: normen voor elektromagnetische compatibiliteit
- Waarschuwingen en aanbevolen werkwijzen van CISA ICS-CERT
- MITRE ATT&CK-framework voor ICS
- Technische analyse van Stuxnet, Langner Communications, 2011
- Technische analyse van TRITON/TRISIS, Dragos, 2017
- Beoordeling van het Oldsmar-waterincident, CISA, 2021
- Onderzoek naar NERC CIP-nalevingskosten van de American Public Power Association, 2019
