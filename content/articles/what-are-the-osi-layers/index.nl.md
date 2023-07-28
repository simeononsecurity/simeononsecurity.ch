---
title: "Basiskennis netwerken: OSI-lagen en TCP IP-model begrijpen"
draft: false
toc: true
date: 2023-07-22
description: "Een uitgebreid begrip krijgen van de OSI-lagen en het TCP IP-model, essentiële kaders in netwerken, om effectieve communicatie en probleemoplossing te vergemakkelijken."
genre: ["Basisprincipes netwerken", "OSI-lagen", "TCP IP-model", "Netwerkprotocollen", "Communicatiemodellen", "Basiskennis netwerken", "Gegevensoverdracht", "Problemen met netwerken oplossen", "Netwerkarchitectuur", "Netwerkconcepten"]
tags: ["OSI-lagen", "TCP IP-model", "basisbeginselen netwerken", "netwerkprotocollen", "communicatiemodellen", "gegevensoverdracht", "netwerkproblemen oplossen", "netwerkarchitectuur", "netwerkconcepten", "netwerkbeginselen", "netwerkkaders", "uitleg netwerkprotocollen", "netwerkstandaarden", "fysieke laag", "datalinklaag", "netwerklaag", "transportlaag", "sessielaag", "presentatielaag", "toepassingslaag", "TCP IP-lagen", "netwerkinterfacelaag", "internetlaag", "transportlaag", "toepassingslaag", "netwerkprotocollen uitgelegd", "netwerkmodellen", "netwerkprincipes uitgelegd", "netwerkgids", "netwerkhandleiding", "beste praktijken voor netwerken"]
cover: "/img/cover/An_animated_illustration_showcasing_a_network.png"
coverAlt: "Een geanimeerde illustratie van een netwerk van onderling verbonden knooppunten waartussen gegevens stromen, als symbool voor efficiënte communicatie en netwerken."
---
 Basiskennis netwerken: De OSI-lagen en het TCP IP-model begrijpen

### Inleiding

In de wereld van netwerken is het essentieel om de protocollen en modellen te begrijpen die de communicatie regelen. Twee veelgebruikte raamwerken zijn het **OSI (Open Systems Interconnection) model** en het **TCP IP (Transmission Control Protocol/Internet Protocol) model**. Deze modellen bieden een gestructureerde benadering van netwerken en dienen als basis voor het bouwen en oplossen van problemen met netwerksystemen. Dit artikel is bedoeld om de OSI-lagen en het TCP IP-model op een duidelijke en beknopte manier uit te leggen.

## De OSI-lagen

Het **OSI model** is een conceptueel raamwerk dat beschrijft hoe netwerkprotocollen op elkaar inwerken en communicatie tussen verschillende systemen mogelijk maken. Het bestaat uit zeven lagen, elk met zijn eigen unieke verantwoordelijkheden.


| OSI Laag Beschrijving Voorbeelden Protocollen Normen.
|----------------|---------------------------------------------------------------|---------------------|------------------------------------------------|---------------------------------------------|
| Fysieke laag | Heeft te maken met de fysieke overdracht van gegevens | Kabels, connectoren | Ethernet, USB, HDMI | IEEE 802.3, USB 3.0 |
| Data Link Layer | Zorgt voor betrouwbare gegevensoverdracht tussen aangrenzende knooppunten | Schakelaars, NIC's | Ethernet, Wi-Fi (802.11), PPP | IEEE 802.3, IEEE 802.11, RFC 1662 | Netwerklaag | Routeert gegevens tussen aangrenzende knooppunten.
| Netwerklaag: routeert gegevenspakketten over verschillende netwerken: routers: IP, ICMP, ARP: IPv4 (RFC 791), IPv6 (RFC 2460), ARP (RFC 826).
| Transportlaag: Biedt betrouwbare gegevenslevering van begin tot eind. Gateways: TCP, UDP: TCP (RFC 793), UDP (RFC 768).
| Sessielaag: beheert communicatiesessies tussen toepassingen NetBIOS, SIP, RFC 1001, RFC 1002, RFC 3261.
| Presentatie Laag: houdt zich bezig met syntaxis en semantiek van informatie-uitwisseling; SSL, HTTP; SSL/TLS, HTTP; SSL/TLS (RFC 5246), HTTP (RFC 2616).
| Toepassingenlaag: directe interactie met toepassingen voor eindgebruikers: webbrowsers, e-mailclients: HTTP, FTP, SMTP, DNS: HTTP (RFC 2616), FTP (RFC 959), SMTP (RFC 5321), DNS (RFC 1035).

{{< youtube id="0y6FtKsg6J4" >}}

Laten we elke laag in detail bekijken:

### Laag 1: Fysieke laag

De **fysieke laag** is de onderste laag van het OSI-model en heeft te maken met de **fysieke overdracht** van gegevens via een netwerk. Het definieert de **hardwarecomponenten**, zoals kabels, connectoren en netwerkinterfaces, die **binaire signalen (0's en 1's)** verzenden. Voorbeelden van protocollen op deze laag zijn **Ethernet, USB en HDMI**.

### Laag 2: Datalinklaag

De **Data Link Layer** is verantwoordelijk voor de **betrouwbare** overdracht van gegevens tussen aangrenzende netwerkknooppunten, zoals switches en netwerkinterfacekaarten (NIC's). Deze laag zorgt voor **foutloze overdracht** en biedt mechanismen voor **flow control** en **foutdetectie**. Veelgebruikte protocollen op deze laag zijn **Ethernet, Wi-Fi (802.11) en Point-to-Point Protocol (PPP)**.

### Laag 3: Netwerklaag

De **netwerklaag** is verantwoordelijk voor **het doorsturen van gegevenspakketten** over verschillende netwerken. Ze bepaalt het **optimale pad** voor gegevensoverdracht op basis van netwerkvoorwaarden en adresseringsschema's. Het **Internet Protocol (IP)** is een fundamenteel protocol op deze laag en kent **unieke IP-adressen** toe aan apparaten voor identificatie- en routeringsdoeleinden.

### Laag 4: Transportlaag

De **Transportlaag** zorgt voor **betrouwbare en efficiënte gegevenslevering van begin tot eind** tussen toepassingen die op verschillende apparaten draaien. Deze laag brengt **verbindingen** tot stand, **segmenteert gegevens** in kleinere eenheden (indien nodig) en biedt mechanismen voor **foutherstel** en **stroomregeling**. Het **Transmission Control Protocol (TCP)** en **User Datagram Protocol (UDP)** zijn veelgebruikte transportprotocollen.

### Laag 5: Sessielaag

De **Sessielaag** beheert de **communicatiesessies** tussen applicaties die op verschillende apparaten draaien. Het creëert, onderhoudt en beëindigt deze sessies, waardoor **gegevens kunnen worden uitgewisseld** tussen processen. Deze laag is verantwoordelijk voor **synchronisatie** en **dialoogcontrole**. Voorbeelden van protocollen op deze laag zijn **NetBIOS** en **Session Initiation Protocol (SIP)**.

### Laag 6: Presentatie Laag

De **presentatielaag** houdt zich bezig met de **syntax en semantiek** van de informatie die tussen systemen wordt uitgewisseld. Deze laag zorgt ervoor dat gegevens correct **opgemaakt**, **gecodeerd** en **versleuteld** worden voor een veilige overdracht. Deze laag is verantwoordelijk voor **gegevenscompressie**, **encryptie** en **protocolconversie**. Voorbeelden van protocollen op deze laag zijn **Secure Sockets Layer (SSL)** en **Hypertext Transfer Protocol (HTTP)**.

### Laag 7: Toepassingslaag

De **Applicatielaag** is de bovenste laag van het OSI-model en staat in direct contact met **eindgebruikertoepassingen**. Het biedt diensten die **communicatie met de gebruiker** en **gegevensuitwisseling**** mogelijk maken. Voorbeelden van protocollen op deze laag zijn **HTTP**, **FTP**, **SMTP** en **DNS**.

## Het TCP IP-model

Terwijl het OSI-model een conceptueel kader biedt, is het TCP IP-model de eigenlijke protocolsuite die op het internet wordt gebruikt. Het bestaat uit vier lagen, die overeenkomen met bepaalde lagen van het OSI-model.


| TCP IP Laag | Laagbeschrijving | Voorbeelden | Protocollen |
|---------------------|---------------------------------------------------------------|---------------------|-------------------------------------------------|
| Netwerkinterfacelaag Behandelt de fysieke overdracht van gegevens via NIC's, Ethernetkabels, Ethernet, Wi-Fi (802.11).
| Internetlaag: Verantwoordelijk voor adressering, routering en fragmentering van gegevens: Routers: IP, ICMP, ARP.
| Transportlaag: zorgt voor betrouwbare en verbindingsgerichte communicatie. Gateways: TCP, UDP.
| Toepassingenlaag: vertegenwoordigt de interface tussen toepassingen en protocollen: webbrowsers, e-mailclients: HTTP, FTP, SMTP, DNS.

{{< youtube id="OTwp3xtd4dg" >}}

Laten we deze lagen eens verkennen:

### Laag 1: Netwerkinterfacelaag

De **Netwerkinterfacelaag** komt overeen met de combinatie van de **Physical** en **Data Link** lagen in het OSI-model. Deze laag zorgt voor de fysieke overdracht van gegevens via het netwerk en biedt protocollen voor datalinkbesturing.

### Laag 2: Internetlaag

De **Internetlaag** is gelijkwaardig aan de **Netwerklaag** in het OSI-model. Deze laag omvat het IP-protocol, dat verantwoordelijk is voor **adressering**, **routering** en **fragmentering** van gegevenspakketten voor verzending over netwerken.

### Laag 3: Transportlaag

De **Transportlaag** in het TCP IP-model komt overeen met de **Transportlaag** in het OSI-model. Het biedt **betrouwbare** en **verbindingsgerichte** communicatie met behulp van het **TCP** protocol of **lichte, verbindingsloze** communicatie met behulp van het **UDP** protocol.

### Laag 4: Toepassingslaag

De **Applicatielaag** in het TCP IP-model omvat de functionaliteit van de lagen **Sessie**, **Presentatie** en **Toepassing** in het OSI-model. Het vertegenwoordigt de interface tussen toepassingen en de onderliggende netwerkprotocollen.

## Conclusie

Het begrijpen van de **OSI lagen** en het **TCP IP model** is cruciaal voor iedereen die betrokken is bij netwerken. Deze modellen bieden een kader om te begrijpen hoe netwerken werken en welke protocollen communicatie mogelijk maken. Door de functies van elke laag te begrijpen, kunnen **netwerkbeheerders** en **ingenieurs** problemen effectief oplossen en robuuste netwerksystemen ontwerpen.


Referenties:
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [TCP IP model](https://www.geeksforgeeks.org/tcp-ip-model/)
- [Ethernet](https://www.computernetworkingnotes.com/networking-tutorials/ethernet-standards-and-protocols-explained.html)
- [Wi-Fi](https://www.wi-fi.org/)
- [IP address](https://en.wikipedia.org/wiki IP_address)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [User Datagram Protocol](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)
- [NetBIOS](https://en.wikipedia.org/wiki/NetBIOS)
- [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
