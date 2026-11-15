---
title: "Conceptes bàsics de xarxes: commutadors, encaminadors, tallafocs i DMZ"
draft: false
toc: true
date: 2023-07-21
lastmod: 2026-11-15
description: "Aprèn com els commutadors, encaminadors, passarel·les, subxarxes, tallafocs i DMZ divideixen el trànsit de xarxa i imposen límits de seguretat."
genre: ["Xarxes", "Infraestructura de TI", "Seguretat de xarxes", "Arquitectura de xarxes", "Ciberseguretat", "Comunicació de dades", "Tecnologies de la informació", "Conceptes bàsics de TI", "Administració de xarxes", "Connectivitat a Internet"]
tags: ["conceptes bàsics de xarxes", "commutadors", "encaminadors", "passarel·les", "subxarxes", "tallafocs", "DMZ", "xarxa d'àrea local", "LAN", "connectivitat de xarxa", "accés a Internet", "gestió d'adreces IP", "segmentació de xarxa", "seguretat de xarxes", "subxarxes IP", "protecció amb tallafocs", "rendiment de xarxa", "arquitectura de xarxes", "comunicació de dades", "administració de xarxes", "ciberseguretat", "infraestructura de xarxa", "conceptes bàsics de TI", "tecnologies de la informació", "gestió del trànsit de dades", "seguretat de TI", "disseny de xarxes", "compliment de TI", "protocols de xarxa", "resolució de problemes de xarxa", "administració de xarxa"]
cover: "/img/cover/A_symbolic_illustration_showing_interconnected.webp"
coverAlt: "Il·lustració simbòlica de dispositius interconnectats amb commutadors, encaminadors, passarel·les i tallafocs."
coverCaption: "Els conceptes bàsics de xarxes ajuden a crear xarxes segures i fiables."
---

## Introducció

En un món tecnològic que canvia ràpidament, les xarxes connecten dispositius i permeten la comunicació. Comprendre els conceptes bàsics de xarxes és essencial tant per als professionals de TI com per a les persones que volen ampliar els seus coneixements. Aquest article ofereix una visió general dels components principals d'una xarxa, com ara els commutadors, els encaminadors, les passarel·les, les subxarxes, els tallafocs i les DMZ. En acabar, entendràs aquests conceptes i la seva importància per crear xarxes segures i fiables.

{{< youtube id="_IOZ8_cPgu8" >}}

## Commutadors: millorar el rendiment de la xarxa d'àrea local

{{< youtube id="NDVImep5UBI" >}}

Un **commutador** és un dispositiu de xarxa que opera a la capa d'enllaç de dades del model OSI. Connecta diversos dispositius dins d'una xarxa d'àrea local (LAN) i encamina paquets de dades entre ells. A diferència dels concentradors, que envien dades a tots els dispositius connectats, els commutadors només lliuren els paquets al destinatari previst. Això redueix les col·lisions i la congestió, i millora el rendiment de la xarxa.

Funcions i avantatges principals dels commutadors:

- **Encaminament per port**: cada port del commutador té una adreça única de control d'accés al medi (MAC), que permet lliurar els paquets directament al dispositiu de destinació.
- **Xarxes LAN virtuals (VLAN)**: permeten segmentar la xarxa i millorar-ne la seguretat aïllant el trànsit entre grups de dispositius diferents.
- **Qualitat de servei (QoS)**: els commutadors poden prioritzar determinats tipus de trànsit perquè les aplicacions sensibles al temps, com la veu o el vídeo, disposin d'amplada de banda suficient.

______

## Encaminadors: connectar xarxes i permetre l'accés a Internet

{{< youtube id="lyIUgr9JOLs" >}}

Els commutadors operen dins d'una LAN, mentre que els **encaminadors** connecten diverses xarxes entre si. Operen a la capa de xarxa del model OSI i utilitzen protocols d'encaminament per triar la millor ruta perquè els paquets arribin a la destinació. A més d'interconnectar xarxes, permeten que els dispositius hi accedeixin a Internet.

Funcions i avantatges principals dels encaminadors:

- **Gestió d'adreces IP**: fan servir adreces IP per identificar i encaminar paquets entre xarxes diferents.
- **Traducció d'adreces de xarxa (NAT)**: converteixen les adreces IP privades d'una LAN en adreces IP públiques quan es comunica amb Internet.
- **Funcions de tallafoc**: molts encaminadors incorporen funcions bàsiques de tallafoc per protegir la xarxa dels accessos no autoritzats.
- **Protocol de configuració dinàmica d'amfitrions (DHCP)**: poden actuar com a servidors DHCP i assignar automàticament adreces IP als dispositius de la xarxa.

______

## Passarel·les: connectar xarxes de tipus diferent

{{< youtube id="SXZC6D7TRfM" >}}

Una **passarel·la** és un dispositiu o component de programari que connecta xarxes amb protocols o arquitectures diferents i permet que es comuniquin. Fa d'intermediària i converteix paquets d'un format de xarxa a un altre. Per exemple, pot connectar una xarxa local amb Internet.

Funcions i avantatges principals de les passarel·les:

- **Traducció de protocols**: converteixen paquets perquè les xarxes amb protocols de comunicació diferents puguin intercanviar informació.
- **Integració de xarxes**: integren xarxes amb arquitectures diferents i faciliten la comunicació.
- **Aplicació de mesures de seguretat**: sovint implementen filtratge de paquets o xifratge per protegir la transmissió entre xarxes.

______

## Subxarxes: organitzar les xarxes per comunicar-se amb eficàcia

{{< youtube id="nR5xCmXJE5E" >}}

Una **subxarxa** és una subdivisió lògica d'una xarxa IP. Dividir una xarxa en subxarxes més petites i fàcils de gestionar pot millorar-ne el rendiment i la seguretat. La màscara de subxarxa defineix cada subxarxa i determina l'interval d'adreces IP que s'hi assigna.

Avantatges d'utilitzar subxarxes:

- **Millor rendiment**: dividir una xarxa gran en subxarxes localitza el trànsit i redueix la congestió general.
- **Més seguretat**: les polítiques de control d'accés poden limitar la comunicació entre subxarxes i afegir una capa de protecció.
- **Administració més senzilla**: agrupar dispositius de manera lògica facilita l'assignació d'adreces IP, l'encaminament i la resolució de problemes.

______

## Tallafocs: protegir les xarxes dels accessos no autoritzats

{{< youtube id="kDEX1HXybrU" >}}

Un **tallafoc** és un dispositiu de seguretat de xarxa que supervisa i controla el trànsit entrant i sortint segons unes regles de seguretat predefinides. Fa de barrera entre les xarxes internes i les externes, com Internet, per impedir accessos no autoritzats i amenaces potencials.

Funcions i avantatges principals dels tallafocs:

- **Filtratge de paquets**: inspeccionen els paquets entrants i sortints i filtren el trànsit potencialment maliciós segons les regles definides.
- **Sistema de prevenció d'intrusions (IPS)**: els tallafocs amb IPS poden detectar i evitar atacs de xarxa, incloses infeccions de programari maliciós i intents d'intrusió.
- **Compatibilitat amb xarxes privades virtuals (VPN)**: molts tallafocs admeten VPN per oferir accés remot segur a través d'Internet.
- **Control d'aplicacions**: els tallafocs avançats inspeccionen la capa d'aplicació i permeten controlar amb detall aplicacions concretes i el seu ús de la xarxa.

______

## DMZ: reforçar la seguretat de la xarxa

{{< youtube id="dqlzQXo1wqo" >}}

Una **zona desmilitaritzada (DMZ)** és un segment de xarxa entre una xarxa interna i xarxes externes com Internet. Aïlla de la xarxa interna els serveis accessibles públicament, com ara servidors web o de correu electrònic, i afegeix una capa de seguretat.

Avantatges i usos principals de les DMZ:

- **Més seguretat**: allotjar serveis públics en una DMZ redueix el risc que un atacant arribi a la xarxa interna.
- **Menys superfície d'atac**: només s'exposen a Internet els serveis necessaris, fet que redueix les possibles vies d'atac.
- **Compliment normatiu**: normes com el Payment Card Industry Data Security Standard (PCI DSS) sovint exigeixen una DMZ per protegir dades confidencials dels clients.

______

## Seqüència de resolució de problemes de 2026

Investiga des del client cap enfora. Comprova l'estat de l'enllaç, l'assignació de l'adreça, la passarel·la predeterminada, la resolució DNS, la selecció de ruta, la política del tallafoc i el servei de l'aplicació. Abans de canviar una regla, anota l'adreça d'origen, la destinació, el protocol, el port, l'hora i l'error observat.

Captura paquets només en xarxes que posseeixis o administris. Mantén les interfícies de gestió en una xarxa restringida, segmenta els dispositius de convidats i IoT i revisa la ruta creada per cada reenviament de port. El [glossari de xarxes del NIST](https://csrc.nist.gov/glossary) i els [avisos de la CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) ofereixen referències útils sobre terminologia i riscos actuals.

## Conclusió

Comprendre els components bàsics de les xarxes és essencial per crear i mantenir xarxes eficients, segures i fiables. Aquest article ha explicat les funcions i els avantatges dels commutadors, encaminadors, passarel·les, subxarxes, tallafocs i DMZ. Amb aquests coneixements podràs dissenyar i administrar xarxes que satisfacin les necessitats de connectivitat actuals.

Tingues sempre en compte els requisits específics de la teva xarxa i consulta la documentació i les normatives governamentals pertinents, com ara els estàndards **Federal Information Processing Standards (FIPS)** i les directrius del **National Institute of Standards and Technology (NIST)**, per aplicar bones pràctiques i complir els requisits.

## Referències

- Federal Information Processing Standards (FIPS): [https://www.nist.gov/itl/fips](https://www.nist.gov/itl/fips)
- National Institute of Standards and Technology (NIST): [https://www.nist.gov/](https://www.nist.gov/)
