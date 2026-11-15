---
title: 'Netwerkbasics: switches, routers, firewalls en DMZ''s'
draft: false
toc: true
date: 2023-07-21
lastmod: 2026-11-15
description: Lees hoe switches, routers, gateways, subnetten, firewalls en DMZ's netwerkverkeer verdelen en beveiligingsgrenzen afdwingen.
genre:
- Netwerken
- IT-infrastructuur
- Netwerkbeveiliging
- Netwerkarchitectuur
- Cyberveiligheid
- Datacommunicatie
- Informatietechnologie
- IT-basiskennis
- Netwerkbeheer
- Internetverbinding
tags:
- netwerkbasics
- netwerkschakelaars
- netwerkrouters
- netwerkpoorten
- subnetten
- netwerkfirewalls
- DMZ's
- lokaal netwerk
- LAN
- netwerkverbinding
- internettoegang
- IP-adresbeheer
- netwerksegmentatie
- netwerkbeveiliging
- subnetteren
- firewallbeveiliging
- netwerkprestaties
- netwerkarchitectuur
- datacommunicatie
- netwerkbeheer
- cyberveiligheid
- netwerkinfrastructuur
- IT-basiskennis
- informatietechnologie
- beheer van dataverkeer
- IT-beveiliging
- netwerkontwerp
- IT-naleving
- netwerkprotocollen
- netwerkproblemen oplossen
- netwerkadministratie
cover: /img/cover/A_symbolic_illustration_showing_interconnected.webp
coverAlt: Symbolische illustratie van apparaten die via switches, routers, gateways en firewalls met elkaar verbonden zijn.
coverCaption: Netwerkbasics helpen bij het opbouwen van veilige en betrouwbare netwerken.
---

## Inleiding

In de snel veranderende technologiewereld verbinden netwerken apparaten en maken ze communicatie mogelijk. Basiskennis van netwerken is essentieel voor IT-professionals en voor iedereen die zijn kennis wil uitbreiden. Dit artikel geeft een overzicht van belangrijke netwerkcomponenten, waaronder switches, routers, gateways, subnetten, firewalls en DMZ's. Na het lezen begrijp je deze begrippen en hun belang voor betrouwbare en veilige netwerken.

{{< youtube id="_IOZ8_cPgu8" >}}

## Netwerkschakelaars: betere prestaties voor het lokale netwerk

{{< youtube id="NDVImep5UBI" >}}

Een **switch** is een netwerkapparaat dat op de datalinklaag van het OSI-model werkt. Het verbindt meerdere apparaten binnen een lokaal netwerk (LAN) en stuurt datapakketten tussen die apparaten door. Hubs sturen gegevens naar alle aangesloten apparaten, terwijl switches pakketten alleen naar de bedoelde ontvanger sturen. Dit vermindert botsingen en congestie en verbetert de netwerkprestaties.

Belangrijke functies en voordelen van switches:

- **Doorsturen per poort**: elke switchpoort krijgt een uniek Media Access Control-adres (MAC), zodat pakketten rechtstreeks naar het doelapparaat gaan.
- **Virtuele LAN's (VLAN's)**: VLAN's segmenteren het netwerk en verbeteren de beveiliging door verkeer tussen apparaatgroepen te scheiden.
- **Quality of Service (QoS)**: switches kunnen bepaalde soorten verkeer voorrang geven, zodat tijdgevoelige toepassingen zoals spraak en video voldoende bandbreedte krijgen.

______

## Netwerkrouters: netwerken verbinden en internettoegang mogelijk maken

{{< youtube id="lyIUgr9JOLs" >}}

Switches werken binnen een LAN. **Routers** verbinden meerdere netwerken met elkaar. Ze werken op de netwerklaag van het OSI-model en gebruiken routeringsprotocollen om het beste pad naar de bestemming van datapakketten te kiezen. Naast het koppelen van netwerken geven routers apparaten toegang tot internet.

Belangrijke functies en voordelen van routers:

- **IP-adresbeheer**: routers gebruiken IP-adressen om datapakketten tussen verschillende netwerken te herkennen en door te sturen.
- **Network Address Translation (NAT)**: routers vertalen privé-IP-adressen in een LAN naar openbare IP-adressen voor communicatie met internet.
- **Firewallfuncties**: veel routers hebben basisfuncties van een firewall die het netwerk tegen onbevoegde toegang beschermen.
- **Dynamic Host Configuration Protocol (DHCP)**: routers kunnen als DHCP-server automatisch IP-adressen aan netwerkapparaten toewijzen.

______

## Netwerkpoorten: verschillende soorten netwerken koppelen

{{< youtube id="SXZC6D7TRfM" >}}

Een **gateway** is een apparaat of softwarecomponent die netwerken met verschillende protocollen of architecturen verbindt. Zo kunnen die netwerken met elkaar communiceren. Gateways fungeren als tussenstation en zetten datapakketten om van de ene netwerkindeling naar de andere. Ze verbinden bijvoorbeeld een lokaal netwerk met internet.

Belangrijke functies en voordelen van gateways:

- **Protocolvertaling**: gateways zetten pakketten om, zodat netwerken met verschillende communicatieprotocollen informatie uitwisselen.
- **Netwerkintegratie**: gateways integreren netwerken met verschillende architecturen en vergemakkelijken communicatie.
- **Beveiliging afdwingen**: gateways passen vaak maatregelen toe, zoals pakketfiltering of versleuteling, om gegevensoverdracht tussen netwerken te beveiligen.

______

## Subnetten: netwerken ordenen voor efficiënte communicatie

{{< youtube id="nR5xCmXJE5E" >}}

Een **subnet** is een logische onderverdeling van een IP-netwerk. Een netwerk opsplitsen in kleinere, beter beheersbare subnetwerken kan prestaties en beveiliging verbeteren. Een subnetmasker bepaalt het subnet en het bereik van IP-adressen dat eraan wordt toegewezen.

Voordelen van subnetten:

- **Betere prestaties**: door een groot netwerk in subnetten te verdelen, blijft verkeer lokaal en neemt de totale netwerkcongestie af.
- **Meer beveiliging**: toegangsbeleid kan communicatie tussen subnetten beperken en vormt zo een extra beveiligingslaag.
- **Eenvoudiger beheer**: apparaten in logische groepen indelen maakt IP-adrestoewijzing, routering en probleemoplossing eenvoudiger.

______

## Netwerkfirewalls: netwerken beschermen tegen onbevoegde toegang

{{< youtube id="kDEX1HXybrU" >}}

Een **firewall** is een netwerkbeveiligingsapparaat dat inkomend en uitgaand verkeer controleert en beheert op basis van vooraf ingestelde beveiligingsregels. De firewall vormt een grens tussen interne netwerken en externe netwerken, zoals internet, om onbevoegde toegang en mogelijke bedreigingen te voorkomen.

Belangrijke functies en voordelen van firewalls:

- **Pakketfiltering**: firewalls controleren inkomende en uitgaande pakketten en blokkeren mogelijk schadelijk verkeer volgens vooraf ingestelde regels.
- **Intrusion Prevention System (IPS)**: firewalls met IPS kunnen netwerkaanvallen, zoals malware-infecties en inbraakpogingen, detecteren en voorkomen.
- **Ondersteuning voor Virtual Private Networks (VPN's)**: veel firewalls ondersteunen VPN-technologie voor veilige externe toegang via internet.
- **Applicatiebeheer**: geavanceerde firewalls inspecteren de applicatielaag en geven gedetailleerde controle over specifieke toepassingen en hun netwerkgebruik.

______

## DMZ's: de netwerkbeveiliging verbeteren

{{< youtube id="dqlzQXo1wqo" >}}

Een **gedemilitariseerde zone (DMZ)** is een netwerksegment tussen een intern netwerk en externe netwerken, zoals internet. De DMZ isoleert openbaar toegankelijke diensten, zoals web- of mailservers, van het interne netwerk en voegt zo een beveiligingslaag toe.

Belangrijke voordelen en toepassingen van DMZ's:

- **Betere beveiliging**: door openbare diensten in een DMZ te plaatsen, kunnen aanvallers minder makkelijk het interne netwerk bereiken.
- **Kleiner aanvalsoppervlak**: alleen noodzakelijke diensten worden aan internet blootgesteld, waardoor mogelijke aanvalsroutes afnemen.
- **Naleving van regelgeving**: regels zoals de Payment Card Industry Data Security Standard (PCI DSS) vereisen vaak een DMZ om gevoelige klantgegevens te beschermen.

______

## Probleemoplossing in 2026

Werk van de client naar buiten. Controleer de linkstatus, adresuitgifte, standaardgateway, DNS-naamomzetting, routeringskeuze, firewallbeleid en applicatieservice. Noteer vóór een regelwijziging het bronadres, de bestemming, het protocol, de poort, het tijdstip en de waargenomen fout.

Maak alleen pakketopnamen op netwerken die je bezit of beheert. Plaats beheerinterfaces op een afgeschermd netwerk, segmenteer gast- en IoT-apparaten en controleer het pad dat elke poortdoorschakeling creëert. De [NIST-netwerkbegrippenlijst](https://csrc.nist.gov/glossary) en [CISA-adviezen](https://www.cisa.gov/news-events/cybersecurity-advisories) bieden nuttige informatie over terminologie en actuele risico's.

## Conclusie

Kennis van netwerkcomponenten is belangrijk voor het opbouwen en onderhouden van efficiënte, veilige en betrouwbare netwerken. Dit artikel behandelde de functies en voordelen van switches, routers, gateways, subnetten, firewalls en DMZ's. Met deze kennis kun je netwerken ontwerpen en beheren die voldoen aan de eisen van moderne connectiviteit.

Houd altijd rekening met de specifieke behoeften van je netwerk en raadpleeg relevante documentatie en overheidsregels, zoals de **Federal Information Processing Standards (FIPS)** en richtlijnen van het **National Institute of Standards and Technology (NIST)**, voor best practices en compliance.

## Bronnen

- Federal Information Processing Standards (FIPS): [https://www.nist.gov/itl/fips](https://www.nist.gov/itl/fips)
- National Institute of Standards and Technology (NIST): [https://www.nist.gov/](https://www.nist.gov/)
