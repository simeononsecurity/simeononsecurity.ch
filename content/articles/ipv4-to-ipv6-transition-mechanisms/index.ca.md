---
title: "Mecanismes de transició d’IPv4 a IPv6: una guia completa"
date: 2023-02-18
lastmod: 2026-11-12
toc: true
draft: false
description: "Descobreix els diferents mecanismes que s'utilitzen per passar d'IPv4 a IPv6 en aquesta guia completa."
tags: ["IPv4", "IPv6", "xarxes", "mecanismes de transició", "pila dual", "NAT64", "DNS64", "túnel IPv6", "ISATAP", "6to4", "DS-Lite", "MAP-T", "migració IPv6", "protocols de xarxa", "protocol d'internet", "arquitectura de xarxa", "encaminament", "subxarxes", "adreçament"]
cover: "/img/cover/A_cartoon_image_of_a_person_standing_at_a_crossroads.webp"
coverAlt: "Il·lustració d'una persona en una cruïlla amb un senyal que indica les direccions IPv4 i IPv6, com a representació de l'elecció i la transició entre els dos protocols."
coverCaption: ""
---
**Mecanismes de transició d’IPv4 a IPv6**

A mesura que augmenten els dispositius connectats i el trànsit d'internet, al món queden menys adreces IPv4 disponibles. IPv6 es va introduir per resoldre aquest problema i moltes xarxes ja l'han adoptat, però la transició encara continua. Aquest article presenta els diferents mecanismes que es poden fer servir per migrar d'IPv4 a IPv6.

## Introducció

**IPv4** és el format original d'adreça IP i s'utilitza des dels primers dies d'internet. Fa servir adreces de 32 bits i admet fins a 4,3 mil milions d'adreces úniques. Amb la proliferació de dispositius connectats, aquesta quantitat ha resultat insuficient. En canvi, **IPv6** utilitza adreces de 128 bits i pot admetre un nombre gairebé infinit d'adreces úniques. La transició a IPv6 és necessària perquè internet continuï creixent i evolucionant.

## Mecanismes de transició

### Pila dual

El mecanisme més senzill consisteix a executar IPv4 i IPv6 a la mateixa xarxa. S'anomena **pila dual (Dual Stack)**. En una xarxa de pila dual, els dos protocols s'activen als dispositius de xarxa, que es poden comunicar amb qualsevol dels dos. Aquest enfocament permet migrar gradualment a IPv6 i mantenir la connectivitat IPv4.

### Túnel

El **túnel** encapsula paquets IPv6 dins de paquets IPv4 per transportar-los a través d'una xarxa IPv4. Aquest mecanisme connecta segments IPv6 separats per una xarxa IPv4. El paquet IPv6 s'encapsula en un paquet IPv4, i la xarxa IPv4 l'encamina fins a l'altre extrem del túnel. Allà, el paquet IPv6 es desencapsula i es lliura a la destinació.

### Traducció

La **traducció** facilita la comunicació entre xarxes IPv4 i IPv6. N'hi ha dos tipus: Network Address Translation-Protocol Translation (NAT-PT) i Address Family Transition Router (AFTR). **NAT-PT** tradueix paquets IPv6 a paquets IPv4 i a l'inrevés, mentre que **AFTR** proporciona connectivitat IPv6 als amfitrions que només utilitzen IPv4.

### 6rd

**IPv6 Rapid Deployment (6rd)** permet desplegar IPv6 ràpidament en una xarxa IPv4. Amb 6rd, un prefix IPv6 s'encapsula dins d'un paquet IPv4 i s'envia per la xarxa IPv4. A l'altre extrem, el paquet IPv6 es desencapsula i es lliura a la destinació. Aquest mecanisme és útil per als proveïdors de serveis que volen desplegar IPv6 de manera ràpida i eficient.

### DS-Lite

**Dual-Stack Lite (DS-Lite)** proporciona connectivitat IPv6 a xarxes que només utilitzen IPv4. Amb DS-Lite, un paquet IPv6 s'encapsula dins d'un paquet IPv4 i s'envia per la xarxa IPv4. A l'altre extrem, el paquet IPv6 es desencapsula i es lliura a la destinació. Aquest mecanisme permet migrar gradualment a IPv6 sense interrompre la connectivitat IPv4.

### NAT64

**NAT64** proporciona connectivitat IPv6 als amfitrions que només utilitzen IPv4. El paquet IPv6 es tradueix a un paquet IPv4, que es pot enviar per una xarxa IPv4. A l'altre extrem, el paquet IPv4 es torna a traduir a un paquet IPv6 i es lliura a la destinació. Aquest mecanisme és útil per proporcionar connectivitat als amfitrions que no es poden actualitzar per admetre IPv6.

______

La transició a IPv6 és necessària perquè internet continuï creixent i evolucionant. La migració encara està en curs i hi ha diversos mecanismes de transició disponibles
