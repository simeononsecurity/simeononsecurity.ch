---
title: "Netwerk Plus Cursus: Het OSI-model, topologieën en netwerktypes begrijpen"
date: 2023-07-01
toc: true
draft: false
description: "Ontdek het belang van netwerkfundamenten, waaronder het OSI-model, netwerktopologieën en verschillende soorten netwerken, voor het bouwen van efficiënte en betrouwbare infrastructuren."
genre: ["Technologie", "Netwerken", "IT-infrastructuur", "Netwerkarchitectuur", "Informatica", "Datacommunicatie", "Informatie Technologie", "Netwerkbeveiliging", "Netwerkbeheer", "Internet"]
tags: ["netwerkbeginselen", "OSI-model", "netwerktopologieën", "netwerktypes", "gegevensinkapseling", "netwerklagen", "netwerktopologie", "stertopologie", "bustopologie", "ringtopologie", "hybride topologie", "peer-to-peer netwerk", "client-server-netwerk", "LAN", "MAN", "WAN", "WLAN", "PAN", "KAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "hypervisor", "satellietverbindingen", "DSL", "kabelinternet", "huurlijn", "metro-optisch"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Een symbolische illustratie van onderling verbonden knooppunten die een netwerk vormen."
coverCaption: "De kracht van netwerkgrondbeginselen ontketenen."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

Netwerkfundamenten spelen een cruciale rol in de onderling verbonden wereld van vandaag. Of je nu op het internet surft, e-mails verstuurt of video's streamt, al deze activiteiten zijn afhankelijk van een robuuste netwerkinfrastructuur. In dit artikel geven we een overzicht van **netwerkbeginselen**, te beginnen met het **OSI-model** en **inkapseling** concepten. We zullen ook verschillende **netwerk topologieën** en hun kenmerken onderzoeken.

## Overzicht van het OSI-model en inkapselingsconcepten

Het **OSI (Open Systems Interconnection) model** is een conceptueel raamwerk dat de functies van een netwerk definieert in zeven verschillende lagen. Elke laag heeft specifieke verantwoordelijkheden en interageert met de lagen erboven en eronder. Inzicht in het OSI-model is essentieel om te begrijpen hoe gegevens over een netwerk worden verzonden en verwerkt.

### OSI Model Lagen

{{< youtube id="G7aVKgGUe9c" >}}

1. **Laag 1 - Fysiek**: De fysieke laag behandelt de feitelijke overdracht en ontvangst van ruwe bitstromen over fysieke media zoals koperdraden, glasvezelkabels of draadloze verbindingen.

2. **Laag 2 - Gegevensverbinding**: De datalinklaag is verantwoordelijk voor het tot stand brengen en beëindigen van verbindingen tussen netwerkapparaten. Deze laag zorgt ook voor foutdetectie en -correctie om een betrouwbare gegevensoverdracht te garanderen.

3. **Laag 3 - Netwerk**: De netwerklaag vergemakkelijkt de routering van gegevenspakketten van de bron naar de bestemming over meerdere netwerkknooppunten. Deze laag behandelt problemen met **netwerkcongestie**, **packetrouting** en **IP-adressering**.

4. **Laag 4 - Transport**: De transportlaag zorgt voor **end-to-end gegevenslevering** en voor betrouwbare communicatie tussen bron en bestemming. Ze beheert **datasegmentatie**, **stroomregeling** en **foutherstel**.

5. **Laag 5 - Sessie**: De sessielaag zet communicatiesessies tussen applicaties op, onderhoudt ze en beëindigt ze. Het beheert **dialoogcontrole** en **synchronisatie** tussen apparaten.

6. **Laag 6 - Presentatie**: De presentatielaag richt zich op de **syntaxis** en **semantiek** van de informatie die wordt uitgewisseld tussen applicaties. Het behandelt **gegevenscodering**, **compressie** en **opmaak** voor de juiste interpretatie.

7. **Laag 7 - Toepassing**: De applicatielaag vertegenwoordigt de eigenlijke netwerktoepassingen en -diensten die door eindgebruikers worden gebruikt. Deze laag biedt diensten zoals **email**, **bestandsoverdracht**, **webbrowsing** en **toegang op afstand**.

### Gegevensinkapseling en -decapsulatie binnen de context van het OSI-model

{{< youtube id="_fPzeQ9PHhA" >}}

Gegevensinkapseling is het proces van het toevoegen van protocol-specifieke headers en trailers aan de payload op elke laag van het OSI-model. Door deze inkapseling kunnen de gegevens door het netwerk reizen en de beoogde bestemming bereiken. Omgekeerd bestaat decapsulatie uit het verwijderen van de toegevoegde headers en trailers op elke laag van het OSI-model om de originele payload eruit te halen.

Binnen de context van het OSI-model dragen de volgende elementen bij aan het inkapselen en inkapselen van gegevens:

- **Ethernet koptekst**: De Ethernet header bevat informatie zoals de MAC-adressen van de bron- en bestemmingsapparaten, het Ethernetprotocoltype en mechanismen voor foutcontrole.

- **Internet Protocol (IP)-header**: De IP-header bevat de IP-adressen van bron en bestemming, pakketidentificatie, time-to-live en andere essentiële parameters voor IP-gebaseerde communicatie.

- TCP (Transmission Control Protocol)/User Datagram Protocol (UDP) Headers**: TCP en UDP headers bevatten poortnummers, volgnummers, controlesommen en andere relevante informatie die nodig is voor communicatie op de transportlaag.

- TCP-vlaggen**: TCP-flags geven specifieke controlefuncties en opties aan tijdens een TCP-sessie. Ze bevatten vlaggen voor het tot stand brengen van verbindingen, het bevestigen van gegevens, het beëindigen van verbindingen en meer.

- **Payload**: De payload zijn de gegevens die worden verzonden, zoals een webpagina, e-mailbericht of mediabestand.

- Maximale transmissie-eenheid (MTU)**: MTU staat voor de maximale grootte van een gegevenspakket dat zonder fragmentatie over een netwerk kan worden verzonden.

## Netwerk topologieën en hun kenmerken onderzoeken

{{< youtube id="zbqrNg4C98U" >}}

Netwerktopologieën definiëren de fysieke of logische rangschikking van netwerkapparaten en de onderlinge verbindingen. Elke topologie heeft zijn eigen sterke en zwakke punten en het kiezen van de juiste topologie hangt af van verschillende factoren zoals schaalbaarheid, fouttolerantie en kosten.

### Mesh-topologie

In een **mesh topologie** is elk apparaat verbonden met elk ander apparaat en vormt zo een volledig onderling verbonden netwerk. Deze redundantie biedt een hoge fouttolerantie maar kan duur en complex zijn om te implementeren. Mesh-topologieën worden vaak gebruikt in kritieke infrastructuur en krachtige computeromgevingen.

### Ster/Hub-en-Spaak Topologie

In een **star topologie** zijn alle apparaten verbonden met een centrale hub of switch. De hub fungeert als centraal verbindingspunt en vergemakkelijkt de communicatie tussen apparaten. Deze topologie is eenvoudig te beheren en biedt gecentraliseerde controle, maar kan een enkelvoudig storingspunt creëren als de hub uitvalt.

### Bus topologie

In een **bustopologie** zijn alle apparaten verbonden met een enkele communicatielijn, een bus genaamd. Gegevens worden sequentieel over de bus verzonden en apparaten ontvangen de gegevens die voor hen bedoeld zijn. Bustopologieën zijn eenvoudig en kosteneffectief, maar kunnen last hebben van netwerkcongestie en hebben een beperkte schaalbaarheid.

### Ringtopologie

In een **ringtopologie** zijn apparaten verbonden in een cirkelvormige keten, waarbij elk apparaat verbinding maakt met het volgende en het laatste apparaat weer verbinding maakt met het eerste. Gegevens circuleren in één richting rond de ring. Ringtopologieën bieden eerlijke toegang en kunnen hoge verkeersbelastingen aan, maar kunnen last hebben van netwerkstoringen als een apparaat uitvalt.

### Hybride topologie

Een **hybride topologie** combineert meerdere topologieën om een flexibeler en schaalbaarder netwerk te vormen. Een combinatie van ster- en ringtopologieën kan bijvoorbeeld redundantie en fouttolerantie bieden met behoud van schaalbaarheid.

## Netwerktypes en -kenmerken

{{< youtube id="6a-roIeJ_a4" >}}

Netwerken omvatten verschillende soorten netwerken, elk voor specifieke behoeften en gebruikssituaties. Hier zijn enkele veelvoorkomende netwerktypes:

### Peer-to-Peer (P2P) netwerk

In een **peer-to-peer (P2P) netwerk** maken apparaten rechtstreeks verbinding met elkaar zonder afhankelijk te zijn van een gecentraliseerde server. P2P-netwerken worden vaak gebruikt voor het delen van bestanden, samenwerkingstoepassingen en gedecentraliseerde systemen.

### Client-server-netwerk

Een **client-server-netwerk** heeft clients die diensten of bronnen aanvragen en servers die deze diensten of bronnen leveren. Client-server netwerken worden veel gebruikt in bedrijfsomgevingen, waar gecentraliseerde controle en middelenbeheer essentieel zijn.

### Lokaal netwerk (LAN)

Een **local area network (LAN)** strekt zich uit over een klein geografisch gebied, zoals een kantoorgebouw of een huis. Het stelt apparaten binnen het netwerk in staat om te communiceren en bronnen te delen. LAN's worden vaak gebruikt voor interne communicatie, het delen van bestanden en printers.

### Metropolitaan netwerk (MAN)

Een **metropolitan area network (MAN)** bestrijkt een groter geografisch gebied dan een LAN maar kleiner dan een WAN. Het verbindt meerdere LAN's binnen een stad of grootstedelijke regio. MAN's worden vaak gebruikt door organisaties die een snelle verbinding nodig hebben tussen hun vestigingen of campussen.

### Wide Area Network (WAN)

Een **wide area network (WAN)** omspant een groot geografisch gebied en verbindt meerdere LAN's of MAN's in verschillende steden, landen of continenten. WAN's maken gebruik van verschillende communicatietechnologieën, zoals huurlijnen, satellieten en optische netwerken, om gegevens over lange afstanden te verzenden.

### Draadloos lokaal netwerk (WLAN)

Een **draadloos lokaal netwerk (WLAN)** biedt draadloze connectiviteit binnen een beperkt gebied, meestal met behulp van Wi-Fi-technologie. WLAN's worden vaak aangetroffen in huizen, kantoren, coffeeshops en openbare ruimten, en stellen gebruikers in staat om hun apparaten zonder fysieke kabels aan te sluiten.

### PAN (Personal Area Network)

Een **personal area network (PAN)** bestrijkt een klein gebied, meestal binnen iemands werkruimte of directe omgeving. Het maakt communicatie mogelijk tussen persoonlijke apparaten, zoals smartphones, tablets en draagbare apparaten.

### Campus Area Network (CAN)

Een **campus area network (CAN)** is een netwerk dat zich uitstrekt over een universiteitscampus of een grote bedrijfscampus. Het biedt connectiviteit met verschillende gebouwen en faciliteiten binnen het campusgebied, wat communicatie en het delen van middelen vergemakkelijkt.

### SAN (Storage Area Network)

Een **storage area network (SAN)** is een gespecialiseerd netwerk dat ontworpen is voor opslagdoeleinden. Het geeft meerdere servers toegang tot gedeelde opslagbronnen, zoals disk arrays of tape libraries, via een snelle verbinding.

### SDWAN (Software-Defined Wide Area Network)

**Software-Defined Wide Area Network (SDWAN)** is een technologie die het beheer en de configuratie van WAN's vereenvoudigt door het netwerkbesturingsvlak te scheiden van de onderliggende hardware. Het biedt gecentraliseerde controle en stelt organisaties in staat om hun WAN-infrastructuur dynamisch te beheren.

### Multiprotocol Label Switching (MPLS)

**Multiprotocol Label Switching (MPLS)** is een routeringstechniek die labels gebruikt om gegevenspakketten efficiënt door een netwerk te sturen. Het biedt krachtige, betrouwbare en veilige communicatie, waardoor het geschikt is voor serviceproviders en ondernemingen.

### Multipoint Generic Routing Encapsulation (mGRE)

**Multipoint Generic Routing Encapsulation (mGRE)** is een techniek die wordt gebruikt om virtuele privénetwerken (VPN's) te maken door gegevenspakketten in te kapselen en ze over een multipuntsnetwerk te verzenden. Het maakt efficiënte communicatie mogelijk tussen meerdere sites of eindpunten.

## Virtuele netwerkconcepten

{{< youtube id="A29g5-Os-u8" >}}

Virtualisatietechnologieën hebben een revolutie teweeggebracht in de manier waarop netwerken worden ontworpen en beheerd. Hier zijn enkele virtuele netwerkconcepten:

### vSwitch

Een **vSwitch**, of virtuele switch, is een op software gebaseerde netwerkswitch die binnen een gevirtualiseerde omgeving werkt, zoals een hypervisor. Het maakt communicatie tussen virtuele machines (VM's) mogelijk en verbindt ze met het fysieke netwerk.

### Virtuele netwerkinterfacekaart (vNIC)

Een **virtuele netwerkinterfacekaart (vNIC)** is een gevirtualiseerde netwerkinterfacekaart die een fysieke netwerkadapter emuleert binnen een virtuele machine. Hiermee kunnen VM's communiceren met de virtuele switch en het fysieke netwerk.

### Network Function Virtualization (NFV)

**Network Function Virtualization (NFV)** is een aanpak waarbij netwerkfuncties, zoals firewalls, routers en loadbalancers, worden gevirtualiseerd door ze op standaardservers uit te voeren in plaats van op speciale hardwareapparaten. Het biedt flexibiliteit, schaalbaarheid en kostenbesparingen in netwerkinfrastructuur.

### Hypervisor

Een **hypervisor** is een softwarelaag die het creëren en beheren van virtuele machines mogelijk maakt. Het biedt hardware-abstractie, waardoor meerdere VM's op één fysieke server kunnen draaien.

## Provider koppelingen

{{< youtube id="M2cJtZXJrpE" >}}

Providerlinks verwijzen naar de verschillende soorten connectiviteitsopties die door serviceproviders worden aangeboden. Hier zijn enkele veel voorkomende providerlinks:

### Satelliet

**Satelliet** links maken gebruik van communicatiesatellieten om gegevens over lange afstanden te versturen. Ze worden vaak gebruikt in afgelegen gebieden waar andere verbindingsmogelijkheden beperkt zijn.

### Digitale abonneelijn (DSL)

**Digital Subscriber Line (DSL)** is een technologie die internettoegang met hoge snelheid biedt via bestaande telefoonlijnen. Het biedt hogere snelheden dan traditionele inbelverbindingen en is wijdverspreid beschikbaar in residentiële en zakelijke omgevingen.

### Kabel

**Kabelinternet** maakt gebruik van dezelfde coaxkabels die voor kabeltelevisie worden gebruikt om snelle internettoegang te bieden. Het is populair in woonwijken en biedt hogere snelheden dan DSL.

### Huurlijn

Een **leaselijn** is een speciale punt-tot-punt-verbinding tussen twee locaties. Het biedt betrouwbare en veilige connectiviteit, waardoor het geschikt is voor bedrijven met hoge bandbreedtevereisten.

### Metro-optisch

**Metro-optische** netwerken gebruiken optische vezeltechnologie om hogesnelheidsconnectiviteit binnen een grootstedelijk gebied te bieden. Ze bieden een hoge bandbreedte en een lage latentie, ideaal voor data-intensieve toepassingen.

______

Tot besluit: inzicht in netwerkfundamenten is cruciaal voor het bouwen en onderhouden van betrouwbare en efficiënte netwerkinfrastructuren. Het **OSI-model** biedt een kader om te begrijpen hoe gegevens over verschillende netwerklagen worden verzonden en verwerkt. Daarnaast helpt kennis van **netwerktopologieën** bij het ontwerpen van netwerken die voldoen aan specifieke eisen voor schaalbaarheid, fouttolerantie en kostenefficiëntie. Door vertrouwd te raken met verschillende **netwerktypes**, **virtuele netwerkconcepten** en **providerlinks** kunnen we weloverwogen beslissingen nemen bij het opzetten en beheren van netwerken.

Referenties:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
