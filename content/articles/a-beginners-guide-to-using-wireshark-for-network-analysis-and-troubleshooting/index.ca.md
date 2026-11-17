---
title: "Dominar Wireshark: guia completa d'anàlisi de xarxes per a principiants"
date: 2023-04-07
lastmod: 2026-11-08
toc: true
draft: false
description: "Aprèn a fer servir Wireshark per analitzar xarxes i resoldre problemes amb aquesta guia detallada per a principiants."
tags: ["Wireshark", "anàlisi de xarxes", "resolució de problemes", "guia per a principiants", "monitoratge de xarxes", "captura de paquets", "protocols de xarxa", "TCP IP", "visualització de dades", "seguretat de xarxes", "filtres de captura", "filtres de visualització", "dispositius de xarxa", "Ethernet", "topologia de xarxa", "diagnòstic de xarxes", "administració de xarxes", "rendiment de xarxa", "tutorial de Wireshark", "paquets de dades"]
cover: "/img/cover/a-beginners-guide-to-using-wireshark-for-network-analysis-and-troubleshooting.webp"
coverAlt: "Il·lustració d'una pantalla d'ordinador amb la interfície de Wireshark, una llista de paquets de xarxa, gràfics estadístics de colors i un fons blau marí fosc."
coverCaption: ""
---

**Guia per a principiants sobre l'ús de Wireshark**

## Introducció

**Wireshark** és un analitzador de protocols de xarxa potent i de codi obert. Permet monitorar, capturar i analitzar el trànsit de xarxa. Els administradors de xarxa, els professionals de seguretat i els desenvolupadors l'utilitzen per resoldre problemes, analitzar xarxes i aprendre. En aquest article veurem els fonaments de l'ús de Wireshark per analitzar i diagnosticar xarxes, com ara la instal·lació, la interfície, les funcions essencials i alguns casos d'ús habituals.

______

## Instal·lació i configuració

Abans d'analitzar una xarxa amb Wireshark, baixa i instal·la el programa a l'ordinador. Wireshark està disponible per a Windows, macOS i Linux. Per baixar-ne la versió més recent, visita el [lloc web oficial de Wireshark](https://www.wireshark.org/#download).

Després d'instal·lar Wireshark, potser hauràs d'instal·lar els controladors necessaris i configurar el sistema per obtenir un rendiment òptim. La [documentació oficial de Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/) inclou instruccions detallades per a sistemes operatius específics.

______

## Interfície de Wireshark

Quan obris Wireshark per primera vegada, veuràs una interfície intuïtiva amb diversos panells, cadascun amb una funció concreta.

- **Llista d'interfícies de captura:** mostra les interfícies de xarxa disponibles a l'ordinador. Per començar a capturar paquets, selecciona una interfície i fes clic a «Inicia».
- **Llista de paquets:** mostra els paquets capturats en ordre cronològic. Aplica filtres per veure els paquets que t'interessen.
- **Detalls del paquet:** mostra informació detallada del paquet seleccionat, incloses la pila de protocols i les capçaleres individuals.
- **Bytes del paquet:** mostra les dades en brut, en hexadecimal i ASCII, del paquet seleccionat.

______

## Captura i filtratge de paquets

Per capturar paquets, selecciona la interfície de xarxa desitjada i fes clic a «Inicia». Wireshark començarà a monitorar el trànsit de xarxa i mostrarà els paquets capturats en temps real.

El **filtratge de paquets** és una funció essencial de Wireshark, perquè permet centrar-se en trànsit concret segons paràmetres com ara les adreces IP, els protocols o els números de port. Escriu els filtres a la barra «Filtre», situada damunt del panell Llista de paquets. Per exemple, fes servir `ip.addr == 192.168.1.1` per filtrar paquets relacionats amb una adreça IP. Consulta la [referència dels filtres de visualització de Wireshark](https://www.wireshark.org/docs/man-pages/wireshark-filter.html) per conèixer els filtres disponibles.

______

## Anàlisi del trànsit de xarxa

Després de capturar i filtrar paquets, pots analitzar el trànsit de xarxa. Wireshark ofereix diverses eines integrades per ajudar-te a interpretar les dades:

- **Estadístiques:** presenta estadístiques de converses, jerarquia de protocols, punts finals i altres elements. Accedeix-hi des del menú «Estadístiques».
- **Gràfics:** ajuden a identificar patrons, tendències i anomalies. Crea gràfics de mètriques com ara el rendiment, el temps d'anada i tornada o l'escalat de finestra des de «Estadístiques», amb «Gràfics d'E/S» o «Gràfics de flux TCP».
- **Informació experta:** mostra possibles problemes del trànsit capturat, com ara retransmissions, paquets duplicats o malformats. Fes clic a «Analitza» a la barra de menús i selecciona «Informació experta».

______

## Resolució de problemes de xarxa

Wireshark és una eina excel·lent per investigar problemes de xarxa, com ara la latència, la pèrdua de paquets o les fallades de connectivitat. Algunes tècniques habituals són:

- **Anàlisi de retransmissions TCP:** un nombre elevat de retransmissions pot indicar congestió de xarxa, pèrdua de paquets o altres problemes. Fes servir el filtre de visualització `tcp.analysis.retransmission` per aïllar les retransmissions i analitzar-ne les característiques.
- **Identificació de connexions lentes:** analitza el temps d'anada i tornada (RTT) entre paquets per determinar si una connexió lenta es deu a la latència de xarxa o a retards de l'aplicació. El gràfic de flux TCP permet visualitzar els valors RTT i detectar possibles colls d'ampolla.
- **Detecció d'accés no autoritzat:** filtra paquets per adreça IP, port o protocol per cercar activitats sospitoses o intents d'accés no autoritzat.

## Pla de captura per a principiants

Comença amb una pregunta i un interval de captura curt. Captura el trànsit a la interfície que transporta el trànsit que analitzes, reprodueix un problema i atura la captura. Desa el fitxer pcapng amb una marca horària. Les captures de paquets sovint inclouen credencials, dades personals, noms d'amfitrió i adreces internes. Emmagatzema-les com a registres sensibles i comparteix-les només amb persones autoritzades.

Fes servir un **filtre de captura** per reduir els paquets que es desen durant la captura. Després, aplica un **filtre de visualització** per ocultar paquets sense eliminar-los del fitxer. Les sintaxis són diferents. La guia de Wireshark documenta tots dos llenguatges de filtre.

| Objectiu | Filtre de visualització | Què cal comprovar |
|---|---|---|
| **Fallada de DNS** | `dns` | Nom consultat, codi de resposta, adreça del servidor i retard de resposta. |
| **Connexió TCP** | `tcp.flags.syn == 1` | SYN, SYN-ACK i ACK final per al punt final previst. |
| **Retransmissions** | `tcp.analysis.retransmission` | Direcció, temps i si la pèrdua es repeteix en un mateix camí. |
| **Un amfitrió** | `ip.addr == 192.168.1.20` | Trànsit cap a l'amfitrió seleccionat o des d'aquest. |
| **Un servei** | `tcp.port == 443` | El port TCP seleccionat, sense donar per fet quina aplicació l'utilitza. |

En un terminal, `tshark -i <interface> -f "host 192.168.1.20" -w incident.pcapng` desa una captura pcapng amb un filtre de captura libpcap. `tshark -r incident.pcapng -Y "dns or tcp.analysis.retransmission"` llegeix el fitxer amb un filtre de visualització. Substitueix la interfície, l'adreça i el nom del fitxer pels valors de la prova autoritzada.

Selecciona un paquet i fes servir **Analitza > Segueix** per inspeccionar un flux de protocol. Wireshark admet fluxos TCP, UDP, TLS, HTTP, HTTP/2, QUIC, WebSocket, SIP i altres. Seguir un flux no desxifra TLS per si sol. La [guia de fluxos de Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html) n'explica l'abast i les limitacions.

Tracta la **Informació experta** com una pista. Cal relacionar una retransmissió, un paquet duplicat o un paquet malformat amb les marques horàries, els punts finals, els comptadors de la interfície i els registres de l'aplicació. La documentació de Wireshark indica que la informació experta és un punt de partida, no una prova d'una fallada.

______

## Compliment de normatives governamentals

Algunes normatives governamentals, com el [**Reglament general de protecció de dades (GDPR)**](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) i la [**Llei de portabilitat i responsabilitat de les assegurances mèdiques (HIPAA)**](https://www.hhs.gov/hipaa/index.html), exigeixen que les organitzacions protegeixin la informació sensible i mantinguin la seguretat de xarxa. Wireshark ajuda a complir aquestes normatives si monitoras el trànsit de xarxa per detectar accessos no autoritzats o filtracions de dades.

La captura i l'anàlisi del trànsit de xarxa també plantegen qüestions legals i ètiques. Abans d'utilitzar Wireshark, assegura't de tenir l'autorització necessària i de seguir les polítiques de l'organització i les lleis locals.

______

## Conclusió

Wireshark és una eina potent i versàtil per analitzar xarxes i resoldre problemes. Si n'entens les funcions i aprens a fer-les servir, pots millorar la seguretat de xarxa de l'organització, optimitzar-ne el rendiment i complir les normatives governamentals.

______

## Referències

1. [Wireshark - Go Deep.](https://www.wireshark.org/)
2. [Guia d'usuari de Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/)
3. [Reglament general de protecció de dades (GDPR)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)
4. [Llei de portabilitat i responsabilitat de les assegurances mèdiques (HIPAA)](https://www.hhs.gov/hipaa/index.html)
5. [Manual de TShark de Wireshark](https://www.wireshark.org/docs/man-pages/tshark.html)
6. [Wireshark: seguir fluxos de protocols](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html)
7. [Informació experta de Wireshark](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvExpert.html)

Recorda practicar i experimentar amb Wireshark per conèixer millor les seves funcions. Com més el facis servir, més hàbil seràs a l'hora d'identificar i resoldre problemes de xarxa
