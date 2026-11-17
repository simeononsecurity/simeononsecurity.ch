---
title: "Errors habituals en fer servir una VPN i com pots revelar la teva IP pública sense voler"
draft: false
toc: true
date: 2023-05-08
lastmod: 2026-11-09
description: "Protegeix la teva privadesa en línia evitant errors habituals de VPN que poden revelar la teva adreça IP pública sense voler."
tags: ["Errors de VPN", "Fuites d'IP", "Privadesa en línia", "Ciberseguretat", "Seguretat d'Internet", "Xarxa privada virtual", "WebRTC", "Servidor DNS", "Proveïdor de VPN", "Autenticació de dos factors", "Programari de VPN", "Kill switch", "Privadesa de les dades", "Privadesa a Internet", "Ciberamenaces", "Seguretat de les dades", "Seguretat de xarxa", "Seguretat en línia", "Anonimat en línia", "Navegació anònima"]
cover: "/img/cover/A_cartoon_character_standing_on_a_laptop_with_a_magnifying_glass.webp"
coverAlt: "Un personatge de dibuixos animats dret sobre un portàtil busca privadesa en línia amb una lupa."
coverCaption: ""
---

**Errors habituals en fer servir VPN i com pots revelar la teva IP pública sense voler**

Milions de persones d'arreu del món fan servir xarxes privades virtuals (VPN) per protegir la seva privadesa i seguretat en línia. Tot i tenir bones intencions, és fàcil cometre errors que poden provocar **la filtració accidental de la teva IP pública** mentre fas servir una VPN. Aquest article repassa els errors habituals i com evitar-los.

## Què és una VPN?

Una VPN és un servei que crea una connexió segura i privada entre el teu dispositiu i Internet. Envia el trànsit d'Internet a través d'un servidor situat en un lloc diferent del teu. Així sembla que et connectis des de la ubicació del servidor i no des de la teva.

## Errors habituals en fer servir VPN

### No comprovar si hi ha fuites d'IP

Un dels errors més habituals en fer servir una VPN és **no comprovar si hi ha fuites d'IP**. Quan et connectes a una VPN, el trànsit hauria de passar pel servidor VPN i l'adreça IP hauria de quedar oculta. Però si la connexió no està ben configurada o el proveïdor té una vulnerabilitat, la IP es pot filtrar i la VPN deixa de complir el seu propòsit.

Per comprovar si la VPN filtra la teva IP, pots fer servir un lloc com [**ipleak.net**](https://ipleak.net/). Mostra la teva IP pública i si és diferent de la del servidor VPN al qual et connectes. Si les adreces són diferents, la VPN funciona correctament. Si són iguals, la VPN filtra la teva IP.

### No triar un proveïdor de VPN segur

Un altre error habitual és **no triar un proveïdor de VPN segur**. N'hi ha molts, però no tots són fiables. Alguns poden registrar el trànsit d'Internet o vendre les teves dades a tercers. D'altres poden tenir vulnerabilitats que permetin als atacants accedir a la teva informació.

Tria un proveïdor amb una política estricta de no conservar registres, xifratge robust i un historial acreditat de protecció de la privadesa. Pots consultar ressenyes, com ara les [recomanacions de proveïdors de VPN de simeononsecurity.com](https://simeononsecurity.com/recommendations/vpns/), per prendre una decisió informada.

### Fer servir VPN gratuïtes

Fer servir una VPN gratuïta és un altre error habitual. Tot i que pot semblar una bona opció, sovint té limitacions que poden perjudicar la seguretat i la privadesa. Les VPN gratuïtes poden registrar el trànsit, vendre les dades a tercers o limitar l'amplada de banda i la velocitat.

Si vols fer servir una VPN, és recomanable pagar per un servei fiable. Així redueixes el risc que venguin o registrin les teves dades i pots gaudir d'una connexió ràpida i estable.

### No actualitzar el programari de VPN

No actualitzar el programari de VPN també és un error habitual. Els proveïdors publiquen actualitzacions per corregir vulnerabilitats i millorar el rendiment. Una versió antiga et pot exposar a riscos de seguretat i problemes de rendiment.

Per evitar-ho, actualitza el programari de VPN regularment. La majoria de proveïdors t'avisen quan hi ha una actualització o pots comprovar-ho manualment.

## Com evitar que es filtri la IP pública mentre fas servir una VPN

### Fes servir un kill switch

Un **kill switch** desconnecta automàticament Internet si cau la connexió VPN. Això evita exposar la IP si falla la connexió VPN.

Molts proveïdors de VPN ofereixen aquesta funció. Activa-la si està disponible.

### Desactiva WebRTC

WebRTC és una tecnologia dels navegadors que permet comunicacions en temps real, com ara videoconferències i intercanvi de fitxers. Però també es pot fer servir per revelar la IP real, fins i tot quan tens una VPN activa.

Per desactivar WebRTC al navegador, pots instal·lar una extensió com **WebRTC Control** per a Chrome o **Disable WebRTC** per a Firefox.

### Fes servir un servidor DNS privat

Quan et connectes a un lloc web, el dispositiu envia una sol·licitud a un servidor DNS (sistema de noms de domini) perquè converteixi el nom del domini en una adreça IP. Per defecte, el dispositiu fa servir el servidor DNS del proveïdor de serveis d'Internet (ISP), que pot registrar la teva activitat.

Per evitar-ho, fes servir un servidor DNS privat que no registri l'activitat. Alguns proveïdors de VPN n'ofereixen un, o pots fer servir serveis de tercers com [**Cloudflare DNS**](https://1.1.1.1/) o [**Google DNS**](https://developers.google.com/speed/public-dns).

### [Fes servir l'autenticació de dos factors](https://simeononsecurity.com/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)

L'[**autenticació de dos factors**](https://simeononsecurity.com/articles/what-are-the-diferent-kinds-of-factors-in-mfa/) ajuda a protegir el compte de VPN contra accessos no autoritzats. Cal que proporcionis dues proves d'identitat per accedir-hi, com ara una contrasenya i un codi enviat al telèfon.

Molts proveïdors de VPN ofereixen [autenticació de dos factors](https://simeononsecurity.com/articles/what-are-the-diferent-kinds-of-factors-in-mfa/). Activa-la si està disponible.

### Conclusió

Les VPN són una bona manera de protegir la privadesa i la seguretat en línia, però no són infal·libles. Errors com no comprovar les fuites d'IP, fer servir un proveïdor no segur o una VPN gratuïta, i no actualitzar el programari poden posar en risc la seguretat i la privadesa. Per evitar que es filtri la IP pública, fes servir un kill switch, desactiva WebRTC, utilitza un servidor DNS privat i activa l'autenticació de dos factors.

Investiga sempre i tria un proveïdor de VPN fiable amb un historial acreditat de protecció de la privadesa. Si segueixes aquests consells, podràs gaudir d'una experiència en línia segura i privada.

## Referències

- [Recomanacions de proveïdors de VPN de simeononsecurity.com](https://simeononsecurity.com/recommendations/vpns/)
- [Guia sobre l'autenticació multifactor: tipus i bones pràctiques](https://simeononsecurity.com/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)
- [IPLeak.net](https://ipleak.net/)
- [Extensió WebRTC Control per a Chrome](https://chrome.google.com/webstore/detail/webrtc-control/fjkmabmdepjfammlpliljpnbhleegehm?hl=en)
- [Extensió Disable WebRTC per a Firefox](https://addons.mozilla.org/en-US/firefox/addon/happy-bonobo-disable-webrtc/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)
- [Cloudflare DNS](https://1.1.1.1/)
- [Google DNS](https://developers.google.com/speed/public-dns)
