---
title: "Conceptes bàsics de xarxes: capes OSI i model TCP IP"
draft: false
toc: true
date: 2023-07-22
lastmod: 2026-11-26
description: "Entén les capes OSI i el model TCP IP, estructures essencials de xarxa que faciliten la comunicació i la resolució de problemes."
genre: ["Conceptes bàsics de xarxes", "Capes OSI", "Model TCP IP", "Protocols de xarxa", "Models de comunicació", "Fonaments de xarxa", "Transmissió de dades", "Resolució de problemes de xarxa", "Arquitectura de xarxa", "Conceptes de xarxa"]
tags: ["capes OSI", "model TCP IP", "conceptes bàsics de xarxes", "protocols de xarxa", "models de comunicació", "transmissió de dades", "resolució de problemes de xarxa", "arquitectura de xarxa", "conceptes de xarxa", "fonaments de xarxa", "marcs de xarxa", "explicació dels protocols de xarxa", "estàndards de xarxa", "capa física", "capa d’enllaç de dades", "capa de xarxa", "capa de transport", "capa de sessió", "capa de presentació", "capa d’aplicació", "capes TCP IP", "capa d’interfície de xarxa", "capa d’Internet", "capa de transport", "capa d’aplicació", "protocols de xarxa explicats", "models de xarxa", "fonaments de xarxa explicats", "guia de xarxes", "bones pràctiques de xarxa", "Model de xarxes"]
cover: "/img/cover/An_animated_illustration_showcasing_a_network.webp"
coverAlt: "Il·lustració animada d’una xarxa de nodes interconnectats amb dades que hi circulen, símbol d’una comunicació eficient."
coverCaption: "Entén el potencial de les xarxes per a una comunicació fluida."
slug: "networking-basics-osi-layers-tcp-ip-model"
---
## Conceptes bàsics de xarxes: capes OSI i model TCP IP

### Introducció

En xarxes, és essencial entendre els protocols i models que regulen la comunicació. Dos marcs molt utilitzats són el **model OSI (Open Systems Interconnection)** i el **model TCP IP (Transmission Control Protocol/Internet Protocol)**. Organitzen els conceptes de xarxa i serveixen de base per crear sistemes i resoldre’n els problemes. Aquest article explica clarament les capes OSI i el model TCP IP.

## Les capes OSI

El **model OSI** és un marc conceptual que descriu com interactuen els protocols de xarxa i com permeten la comunicació entre sistemes. Té set capes, cadascuna amb responsabilitats pròpies.

| Capa OSI | Descripció de la capa | Exemples | Protocols | Estàndards |
|----------------|---------------------------------------------------------------|---------------------|------------------------------------------------|---------------------------------------------|
| Capa física | Transmet físicament les dades | Cables, connectors | Ethernet, USB, HDMI | IEEE 802.3, USB 3.0 |
| Capa d’enllaç de dades | Garanteix la transferència fiable entre nodes adjacents | Commutadors, NIC | Ethernet, Wi-Fi (802.11), PPP | IEEE 802.3, IEEE 802.11, RFC 1662 |
| Capa de xarxa | Encaminament de paquets entre xarxes | Encaminadors | IP, ICMP, ARP | IPv4 (RFC 791), IPv6 (RFC 2460), ARP (RFC 826) |
| Capa de transport | Proporciona un lliurament fiable d’extrem a extrem | Passarel·les | TCP, UDP | TCP (RFC 793), UDP (RFC 768) |
| Capa de sessió | Gestiona les sessions de comunicació entre aplicacions | NetBIOS | NetBIOS, SIP | RFC 1001, RFC 1002, RFC 3261 |
| Capa de presentació | Tracta la sintaxi i el significat de la informació | SSL, HTTP | SSL/TLS, HTTP | SSL/TLS (RFC 5246), HTTP (RFC 2616) |
| Capa d’aplicació | Interactua directament amb les aplicacions de l’usuari | Navegadors, clients de correu | HTTP, FTP, SMTP, DNS | HTTP (RFC 2616), FTP (RFC 959), SMTP (RFC 5321), DNS (RFC 1035) |

{{< youtube id="0y6FtKsg6J4" >}}

A continuació, cada capa:

### Capa 1: capa física

La **capa física** és la més baixa del model OSI i tracta la **transmissió física** de dades per la xarxa. Defineix els **components de maquinari**, com ara cables, connectors i interfícies de xarxa, que transmeten **senyals binaris (0 i 1)**. Alguns protocols d’aquesta capa són **Ethernet, USB i HDMI**.

### Capa 2: capa d’enllaç de dades

La **capa d’enllaç de dades** garanteix la **transferència fiable** entre nodes adjacents, com commutadors i targetes d’interfície de xarxa (NIC). Assegura una **transmissió sense errors** i proporciona mecanismes de **control de flux** i **detecció d’errors**. Entre els protocols habituals hi ha **Ethernet, Wi-Fi (802.11) i Point-to-Point Protocol (PPP)**.

### Capa 3: capa de xarxa

La **capa de xarxa** **encamina paquets de dades** entre xarxes. Determina el **millor camí** segons les condicions de xarxa i els esquemes d’adreçament. El **protocol d'Internet (IP)** és fonamental en aquesta capa i assigna **adreces IP úniques** per identificar i encaminar els dispositius.

### Capa 4: capa de transport

La **capa de transport** garanteix el **lliurament fiable i eficient d’extrem a extrem** entre aplicacions de dispositius diferents. Estableix **connexions**, **segmenta les dades** en unitats més petites si cal i proporciona **recuperació d’errors** i **control de flux**. Els protocols de transport habituals són **TCP** i **UDP**.

### Capa 5: capa de sessió

La **capa de sessió** gestiona les **sessions de comunicació** entre aplicacions de dispositius diferents. Les estableix, manté i tanca perquè els processos puguin **intercanviar dades**. També s’encarrega de la **sincronització** i el **control del diàleg**. Alguns exemples són **NetBIOS** i **Session Initiation Protocol (SIP)**.

### Capa 6: capa de presentació

La **capa de presentació** tracta la **sintaxi i el significat** de la informació intercanviada entre sistemes. Garanteix que les dades es **formatin**, **codifiquin** i **xifrin** per transmetre-les de manera segura. També s’encarrega de la **compressió**, el **xifratge** i la **conversió de protocols**. En són exemples **Secure Sockets Layer (SSL)** i **Hypertext Transfer Protocol (HTTP)**.

### Capa 7: capa d’aplicació

La **capa d’aplicació**, la més alta del model OSI, interactua directament amb les **aplicacions de l’usuari final**. Proporciona serveis de **comunicació** i **intercanvi de dades**. En són exemples **HTTP**, **FTP**, **SMTP** i **DNS**.

## El model TCP IP

El model OSI és conceptual; el model TCP IP és la suite de protocols que s’utilitza realment a Internet. Té quatre capes que corresponen a algunes capes OSI.

| Capa TCP IP | Descripció de la capa | Exemples | Protocols |
|---------------------|---------------------------------------------------------------|---------------------|-------------------------------------------------|
| Capa d’interfície de xarxa | Gestiona la transmissió física | NIC, cables Ethernet | Ethernet, Wi-Fi (802.11) |
| Capa d’Internet | S’encarrega de l’adreçament, l’encaminament i la fragmentació | Encaminadors | IP, ICMP, ARP |
| Capa de transport | Proporciona comunicació fiable i orientada a la connexió | Passarel·les | TCP, UDP |
| Capa d’aplicació | Interfície entre aplicacions i protocols | Navegadors, clients de correu | HTTP, FTP, SMTP, DNS |

{{< youtube id="OTwp3xtd4dg" >}}

Aquestes són les capes:

### Capa 1: interfície de xarxa

La **capa d’interfície de xarxa** combina les capes **física** i **d’enllaç de dades** del model OSI. Transmet físicament les dades per la xarxa i proporciona protocols per controlar l’enllaç.

### Capa 2: Internet

La **capa d’Internet** equival a la **capa de xarxa** del model OSI. Inclou el protocol IP, que s’encarrega de l’**adreçament**, l’**encaminament** i la **fragmentació** de paquets entre xarxes.

### Capa 3: transport

La **capa de transport** del model TCP IP correspon a la **capa de transport OSI**. Proporciona comunicació **fiable** i **orientada a la connexió** amb **TCP**, o comunicació **lleugera i sense connexió** amb **UDP**.

### Capa 4: aplicació

La **capa d’aplicació del TCP IP** inclou les funcions de les capes OSI **de sessió**, **de presentació** i **d’aplicació**. Fa d’interfície entre les aplicacions i els protocols de xarxa subjacents.

## Conclusió

Entendre les **capes OSI** i el **model TCP IP** és essencial per a qualsevol persona que treballi en xarxes. Aquests models expliquen com funcionen les xarxes i quins protocols faciliten la comunicació. Conèixer la funció de cada capa ajuda els **administradors** i **enginyers de xarxa** a resoldre problemes i dissenyar sistemes robustos.

Referències:
- [Model OSI](https://en.wikipedia.org/wiki/OSI_model)
- [Model TCP IP](https://www.geeksforgeeks.org/tcp-ip-model/)
- [Ethernet](https://www.computernetworkingnotes.com/networking-tutorials/ethernet-standards-and-protocols-explained.html)
- [Wi-Fi](https://www.wi-fi.org/)
- [Adreça IP](https://en.wikipedia.org/wiki IP_address)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [User Datagram Protocol](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)
- [NetBIOS](https://en.wikipedia.org/wiki/NetBIOS)
- [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
