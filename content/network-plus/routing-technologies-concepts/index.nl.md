---
title: "Netwerk Plus Cursus: Routing protocollen, concepten en optimalisatie"
date: 2023-07-07
toc: true
draft: false
description: "Verken de wereld van routeringstechnologieën en -concepten, van dynamische routeringsprotocollen zoals RIP, OSPF, EIGRP en BGP tot link state, afstandsvector en hybride routeringsprotocollen, evenals de configuratie van statische routering en standaardroutes."
genre: ["Technologie", "Netwerken", "Routing", "Netwerkprotocollen", "Netwerkbeheer", "Dynamisch routeren", "Statisch routeren", "Beheer bandbreedte", "Kwaliteit van service", "Netwerkapparaten"]
tags: ["routeringstechnologieën", "dynamische routeringsprotocollen", "RIP", "OSPF", "EIGRP", "BGP", "verbindingsstatus", "afstandsvector", "hybride routeringsprotocollen", "statische routing", "standaard routes", "administratieve afstand", "buitenrouting", "interne routering", "tijd om te leven", "bandbreedtebeheer", "vormgeving van verkeer", "kwaliteit van dienstverlening", "netwerkapparaten", "routers", "schakelaars", "firewalls", "loadbalancers", "toegangspunten", "netwerkoptimalisatie", "netwerkprestaties", "netwerkbeveiliging", "netwerkarchitectuur", "netwerkverkeer"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Een afbeelding van onderling verbonden netwerkapparaten waartussen gegevens stromen."
coverCaption: "Navigeren op de digitale snelweg: Netwerkroutering optimaliseren voor topprestaties"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Introductie

In de huidige onderling verbonden wereld is efficiënte netwerkroutering essentieel voor een vlotte gegevensoverdracht en communicatie. Routing technologieën en concepten spelen een cruciale rol in het sturen van netwerkverkeer en het optimaliseren van netwerkprestaties. Dit artikel verkent verschillende routeringsprotocollen, zoals RIP, OSPF, EIGRP en BGP, samen met link state, afstandsvector en hybride routeringsprotocollen. We zullen ook ingaan op de configuratie en het gebruik van statische routing en standaardroutes. Daarnaast zullen we verschillende apparaten en hun plaatsing op het netwerk vergelijken en tegen elkaar afzetten.

{{< youtube id="YRzr56cwgCg" >}}

## Dynamische routeprotocollen

Dynamische routeringsprotocollen zijn ontworpen om het uitwisselen van routeringsinformatie tussen routers te automatiseren. Ze passen zich aan aan netwerkveranderingen, zoals wijzigingen in de topologie of verbindingsfouten, door routeringstabellen dynamisch bij te werken. Laten we eens kijken naar enkele veelgebruikte dynamische routeringsprotocollen:

### Routing Internet Protocol (RIP)

Het Routing Internet Protocol (RIP) is een afstandsvectorrouteringsprotocol dat werkt op basis van het aantal hops tussen routers. Het gebruikt de hop count metric om het beste pad naar een bestemmingsnetwerk te bepalen. RIP ondersteunt zowel IPv4 als IPv6 en is geschikt voor kleine tot middelgrote netwerken.

### Open kortste pad eerst (OSPF)

Open Shortest Path First (OSPF) is een link state routeringsprotocol dat het kortste pad naar een bestemming berekent met behulp van het Dijkstra algoritme. Het houdt rekening met verschillende metrieken, zoals bandbreedte, vertraging en betrouwbaarheid, om de optimale route te bepalen. OSPF wordt veel gebruikt in grote bedrijfsnetwerken vanwege de schaalbaarheid en snelle convergentie.

### Verbeterd intern routeringsprotocol (EIGRP)

Enhanced Interior Gateway Routing Protocol (EIGRP) is een hybride routeringsprotocol ontwikkeld door Cisco. Het combineert de beste eigenschappen van zowel afstandsvector- als link state-protocollen. EIGRP gebruikt het Diffusing Update Algorithm (DUAL) om routes te berekenen en biedt geavanceerde functies zoals unequal-cost load balancing en route summarization.

### Grensgatewayprotocol (BGP)

Border Gateway Protocol (BGP) is een extern gatewayprotocol dat wordt gebruikt voor routering tussen autonome systemen (ASen) op het internet. BGP is zeer schaalbaar en laat autonome systemen toe om routeringsinformatie uit te wisselen. Het gebruikt padattributen en beleidsregels om routeringsbeslissingen te nemen op basis van factoren zoals netwerkbeleid, padlengte en AS-pad.

## Link State, afstandvector en hybride routeringsprotocollen

Routing protocollen kunnen gecategoriseerd worden in link state, afstandsvector en hybride op basis van hun werking en de informatie die ze gebruiken om routes te bepalen.

### Link State Routeerprotocollen

Link state routing protocollen, zoals OSPF, onderhouden een gedetailleerde kaart van het hele netwerk door link state informatie uit te wisselen tussen routers. Elke router bouwt een topologische database op, waardoor hij het beste pad naar een bestemmingsnetwerk kan berekenen op basis van verschillende metrieken.

### Afstandvectorrouteringsprotocollen

Afstandvectorrouteringsprotocollen, zoals RIP, gebruiken een eenvoudige metriek (zoals het aantal hops) en wisselen routeringsinformatie uit met naburige routers. Routers adverteren periodiek hun routeringstabellen aan naburige routers, zodat ze een beeld van het netwerk kunnen vormen. Afstandvectorprotocollen hebben een beperkte kennis van het hele netwerk en kunnen gevoelig zijn voor routing loops.

### Hybride routeringsprotocollen

Hybride routeringsprotocollen, zoals EIGRP, combineren de eigenschappen van zowel link state- als afstandsvectorprotocollen. Ze onderhouden een topologietabel zoals link state protocollen, maar gebruiken distance vector algoritmen voor het berekenen van routes. Hybride protocollen bieden de voordelen van snellere convergentie en minder overhead.

## Statische routing en standaard routes

Statisch routeren houdt in dat de routeringstabel op routers handmatig geconfigureerd wordt, waarbij de paden om specifieke netwerken te bereiken gespecificeerd worden. Het wordt typisch gebruikt in scenario's waar de netwerktopologie minimaal of voorspelbaar verandert. Statische routes zijn eenvoudig te configureren en kunnen nuttig zijn voor kleine netwerken of specifieke netwerksegmenten.

Een standaardroute, ook wel gateway of last resort genoemd, wordt gebruikt als er geen expliciete route bestaat voor een bestemmingsnetwerk. Het fungeert als een vangnetroute en wordt geconfigureerd op routers om verkeer naar een standaard gateway te leiden wanneer de router het bestemmingsnetwerk niet kent.

## Administratieve afstand, buitenste vs. binnenste en tijd tot leven

{{< youtube id="HR59xk4umWY" >}}

### Administratieve afstand

Administratieve afstand (AD) is een waarde die aan routeringsprotocollen wordt toegekend om de prioriteit van routes te bepalen als er meerdere protocollen op een router worden uitgevoerd. Lagere administratieve afstandswaarden geven een hogere prioriteit aan voor een bepaald routeringsprotocol. OSPF heeft bijvoorbeeld een lagere AD (110) dan RIP (120), dus krijgen OSPF-routes de voorkeur boven RIP-routes.

### Exterior vs. Interior routing

Externe routeringsprotocollen, zoals BGP, worden gebruikt om routeringsinformatie uit te wisselen tussen autonome systemen (ASen). Ze behandelen routering tussen verschillende organisaties en serviceproviders. Interne routeringsprotocollen, zoals RIP, OSPF en EIGRP, worden daarentegen gebruikt voor routering binnen een autonoom systeem.

### Time to Live (TTL)

Time to Live (TTL) is een veld in IP-pakketten dat het maximum aantal hops specificeert dat een pakket kan afleggen voordat het wordt weggegooid. Het voorkomt dat pakketten oneindig lang in het netwerk blijven circuleren als er een routeringslus of andere problemen zijn. Elke router verlaagt de TTL waarde terwijl het pakket door het netwerk reist.

## Bandbreedtebeheer

Efficiënt bandbreedtebeheer is cruciaal voor het optimaliseren van netwerkprestaties en het verzekeren van een soepele verkeersstroom. Twee belangrijke aspecten van bandbreedtebeheer zijn traffic shaping en quality of service (QoS).

### Vormgeven van verkeer

Traffic shaping is een techniek die gebruikt wordt om de snelheid van gegevensoverdracht op een netwerk te regelen. Het laat netwerkbeheerders toe om de verkeersstroom vorm te geven door bandbreedtelimieten te definiëren en voorrang te geven aan bepaalde types verkeer. Dit helpt netwerkcongestie voorkomen en zorgt ervoor dat kritieke toepassingen voldoende bandbreedte krijgen.

### Quality of Service (QoS)

Quality of Service (QoS) verwijst naar de mogelijkheid van een netwerk om voorrang te geven en middelen toe te wijzen aan verschillende soorten verkeer op basis van hun belang en vereisten. QoS-mechanismen, zoals verkeersprioritering, bandbreedtetoewijzing en congestiebeheer, helpen optimale prestaties te garanderen voor realtime toepassingen zoals spraak en video.

## Vergelijking en plaatsing van apparaten

Verschillende apparaten spelen een specifieke rol in een netwerk en hebben verschillende eigenschappen die ze geschikt maken voor bepaalde taken. Laten we een aantal veelgebruikte netwerkapparaten vergelijken en hun geschikte plaatsing bespreken:

- **Routers**: Routers zijn verantwoordelijk voor het sturen van verkeer tussen verschillende netwerken. Ze werken op de netwerklaag (Laag 3) en gebruiken routeringsprotocollen om het beste pad voor gegevensoverdracht te bepalen.

- Schakelaars**: Switches werken op de datalinklaag (laag 2) en vergemakkelijken de communicatie tussen apparaten binnen een lokaal netwerk (LAN). Ze gebruiken MAC-adressen om gegevenspakketten door te sturen naar de beoogde ontvanger.

- Firewalls**: Firewalls beschermen netwerken tegen ongeautoriseerde toegang en kwaadwillig verkeer. Ze dwingen beveiligingsbeleid af door netwerkverkeer te inspecteren en specifieke verbindingen toe te staan of te blokkeren op basis van vooraf gedefinieerde regels.

- Loadbalancers**: Load balancers verdelen inkomend netwerkverkeer over meerdere servers om het gebruik van bronnen te optimaliseren, prestaties te verbeteren en een hoge beschikbaarheid te garanderen.

- Toegangspunten**: Access points (AP's) bieden draadloze connectiviteit aan apparaten binnen een netwerk. Ze maken draadloze communicatie mogelijk door gegevens te verzenden en te ontvangen tussen draadloze apparaten en het bekabelde netwerk.

De plaatsing van deze apparaten hangt af van de netwerkarchitectuur en de vereisten. **Routers** worden meestal aan de rand van het netwerk geplaatst om verkeer tussen netwerken af te handelen. **Switches** worden binnen LAN's geplaatst om apparaten met elkaar te verbinden en lokale communicatie te vergemakkelijken. **Firewalls** worden tussen netwerken geplaatst om bescherming te bieden tegen bedreigingen van buitenaf. **Load balancers** worden voor webservers geplaatst om het verkeer efficiënt te verdelen. **Toegangspunten** worden strategisch geplaatst om draadloze dekking te bieden in de gewenste gebieden.

______

## Conclusie

Inzicht in **routing technologieën en concepten** is cruciaal voor netwerkbeheerders en IT-professionals. **Dynamische routeringsprotocollen** zoals **RIP, OSPF, EIGRP en BGP** automatiseren het proces van het uitwisselen van routeringsinformatie en passen zich aan netwerkveranderingen aan. **Link state, afstandsvector en hybride routeringsprotocollen** bieden verschillende benaderingen om optimale routes te bepalen. **Statische routering en standaardroutes** bieden handmatige controle over routeringsbeslissingen. **Bandbreedtebeheer** technieken zoals **traffic shaping en QoS** zorgen voor een efficiënt netwerkgebruik. Het op de juiste manier vergelijken en plaatsen van netwerkapparaten verbetert de netwerkprestaties en -beveiliging.

Door routingtechnologieën en -concepten** te beheersen, kunnen netwerkbeheerders **robuuste en efficiënte netwerken** bouwen die voldoen aan de eisen van moderne connectiviteit.

______