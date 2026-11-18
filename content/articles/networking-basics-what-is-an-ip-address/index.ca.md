---
title: "Conceptes bàsics de xarxes: què és una adreça IP i què són IPv4 i IPv6"
draft: false
toc: true
date: 2023-07-22
lastmod: 2026-11-12
description: "Aprèn què és una adreça IP, quines diferències hi ha entre IPv4 i IPv6, per què són importants i per què cal adoptar IPv6."
genre: ["Xarxes", "Adreces IP", "Protocols d'Internet", "IPv4", "IPv6", "Comunicació de xarxa", "Connectivitat a Internet", "Tecnologia", "Infraestructura de xarxa", "Seguretat d'Internet"]
tags: ["adreça IP", "IPv4", "IPv6", "protocol d'Internet", "xarxes", "espai d'adreces", "format d'adreça", "configuració d'adreces", "seguretat", "qualitat del servei", "connectivitat a Internet", "infraestructura de xarxa", "tecnologia", "esgotament d'IPv4", "creixement d'Internet", "regulacions governamentals", "comunicació de xarxa", "seguretat d'Internet", "Internet Assigned Numbers Authority", "requisits federals d'IPv6", "assignació dinàmica", "DHCP", "IPsec", "QoS", "autoconfiguració de xarxa", "compressió d'adreces", "notació d'adreces", "tipus d'adreces IP", "esquema d'adreçament IP"]
cover: "/img/cover/A_cartoon_image_of_two_devices_with_speech_bub.webp"
coverAlt: "Il·lustració de dos dispositius amb bafarades que intercanvien dades, una representació de la comunicació de xarxa"
coverCaption: "Adopta IPv6 per gaudir d'una connectivitat a Internet fluida i del creixement futur."
---

## Conceptes bàsics de xarxes: què és una adreça IP i què són IPv4 i IPv6

### Introducció

En xarxes, les adreces IP identifiquen els dispositius connectats a Internet i permeten que es comuniquin. Cada dispositiu que s'hi connecta, com ara un ordinador, un telèfon intel·ligent o un dispositiu domèstic intel·ligent, rep una adreça IP única. Aquest article explica què és una adreça IP, quina diferència hi ha entre IPv4 i IPv6 i per què aquests conceptes són importants per a particulars i empreses.

## Entendre les adreces IP

### Què és una adreça IP?

Una **adreça IP** (adreça del protocol d'Internet) és una etiqueta numèrica assignada a cada dispositiu que participa en una xarxa informàtica. Té dues funcions principals: identificar l'amfitrió o la interfície de xarxa i indicar-ne la ubicació dins la xarxa. Les adreces IP són essencials perquè els dispositius es comuniquin i intercanviïn dades per Internet.

Les adreces IPv4 se solen escriure com quatre grups de números separats per punts, per exemple, 192.168.0.1. Cada grup va de 0 a 255, cosa que permet uns 4.300 milions de combinacions úniques. Però, a mesura que més dispositius es connecten a Internet, l'espai d'adreces IPv4 s'ha anat limitant i això ha impulsat el desenvolupament d'IPv6.

{{< youtube id="8zEVA-Bxs-0" >}}

### IPv4: l'estàndard antic

{{< youtube id="O48yc2nYBRA" >}}

IPv4, o **protocol d'Internet versió 4**, és la quarta iteració del protocol d'Internet i durant molts anys ha estat l'esquema d'adreçament IP dominant. Les adreces IPv4 tenen 32 bits i s'escriuen en format decimal, com l'exemple anterior: 192.168.0.1.

L'adopció generalitzada d'Internet i el ràpid creixement dels dispositius connectats han esgotat les adreces IPv4 disponibles. Amb uns 4.300 milions de combinacions úniques, el conjunt d'adreces ja no és suficient per cobrir el nombre creixent de dispositius del món.

### IPv6: la nova generació

{{< youtube id="pUrdDelghwA" >}}

Per resoldre les limitacions d'IPv4, es va desenvolupar **IPv6** (protocol d'Internet versió 6). IPv6 fa servir adreces de 128 bits i ofereix un espai d'adreces molt més gran que IPv4. En lloc del format decimal habitual, les adreces IPv6 s'escriuen en hexadecimal i els grups se separen amb dos punts, per exemple, 2001:0db8:85a3:0000:0000:8a2e:0370:7334.

Amb l'adopció d'IPv6, el nombre d'adreces IP úniques disponibles és pràcticament il·limitat, cosa que permet que continuï creixent el nombre de dispositius connectats a Internet. IPv6 també aporta altres avantatges, com ara més seguretat, millor suport per a xarxes mòbils i una autoconfiguració de xarxa millorada.

### Diferències clau entre IPv4 i IPv6

{{< youtube id="ThdO9beHhpA" >}}

#### Espai d'adreces

La diferència més important entre IPv4 i IPv6 és l'espai d'adreces. IPv4 ofereix uns 4.300 milions d'adreces úniques, mentre que IPv6 en proporciona uns 340 undecilions (3,4×10^38). Aquest espai enorme permet que Internet s'ampliï i connecti un nombre cada cop més gran de dispositius.

#### Format d'adreça

Una altra diferència és el format de les adreces. IPv4 fa servir quatre grups de números en format decimal, mentre que IPv6 fa servir vuit grups en format hexadecimal. A més, les adreces IPv6 poden contenir zeros consecutius, que es poden comprimir amb la notació "::". Aquesta compressió simplifica la representació de les adreces IPv6 i en redueix la llargada.

#### Configuració d'adreces

Les adreces IPv4 se solen assignar manualment o mitjançant mètodes d'assignació dinàmica com el Protocol de configuració dinàmica d'amfitrió (DHCP). En canvi, les adreces IPv6 sovint es configuren automàticament amb una combinació d'autoconfiguració d'adreces sense estat i DHCPv6 (Protocol de configuració dinàmica d'amfitrió versió 6).

#### Seguretat i qualitat del servei

IPv6 incorpora millores de seguretat i qualitat del servei respecte d'IPv4. Inclou funcions com la integració d'IPsec (seguretat del protocol d'Internet), que proporciona xifratge i autenticació d'extrem a extrem per a les comunicacions de xarxa. IPv6 també admet mecanismes de qualitat del servei (QoS), que permeten prioritzar determinats tipus de trànsit de xarxa.

### La importància d'adoptar IPv6

La [transició d'IPv4 a IPv6](https://simeononsecurity.com/articles/ipv4-to-ipv6-transition-mechanisms/) és essencial per al creixement futur i la sostenibilitat d'Internet. A mesura que augmenta el nombre de dispositius connectats, l'esgotament de les adreces IPv4 esdevé un problema imminent. Amb IPv6, particulars i empreses poden mantenir la connectivitat dels seus dispositius i aprofitar les capacitats millorades del protocol nou.

Els governs i els organismes reguladors d'arreu del món també reconeixen la importància d'adoptar IPv6 i han introduït iniciatives i regulacions per facilitar la transició. Per exemple, el govern dels Estats Units va emetre el 2020 una directiva que exigeix a les agències federals habilitar IPv6 als llocs web i serveis accessibles al públic.

## Conclusió

Les adreces IP són essencials perquè els dispositius es comuniquin i intercanviïn dades per Internet. IPv4 i IPv6 són dues versions diferents del protocol d'Internet. IPv4 és l'estàndard antic, mentre que IPv6 és la solució més nova i escalable. La transició a IPv6 és vital per mantenir el creixement d'Internet i connectar un nombre cada cop més gran de dispositius. Si entens els fonaments de l'adreçament IP i les diferències entre IPv4 i IPv6, podràs prendre decisions informades sobre la infraestructura de xarxa i la connectivitat futura.

## Referències

- [RFC 791 - Protocol d'Internet](https://tools.ietf.org/html/rfc791)
- [RFC 2460 - Especificació del protocol d'Internet versió 6 (IPv6)](https://tools.ietf.org/html/rfc2460)
- [Internet Assigned Numbers Authority (IANA) - Espai d'adreces IPv6](https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml)
