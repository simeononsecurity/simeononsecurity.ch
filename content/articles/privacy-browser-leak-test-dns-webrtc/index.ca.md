---
title: "Comprova les fuites de DNS i WebRTC del navegador amb una VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprova l'IP pública, el servidor DNS i les adreces WebRTC del navegador abans i després de connectar una VPN. Interpreta els resultats i investiga els problemes d'encaminament."
genre: ["Privadesa", "Navegadors", "Xarxes"]
tags: ["prova de fuita DNS", "prova de fuita WebRTC", "prova de fuita VPN", "prova de privadesa del navegador", "fuita d'adreça IP", "DNS sobre HTTPS", "DNS segur", "DNS del Firefox", "DNS segur del Chrome", "candidats WebRTC", "túnel dividit VPN", "fuita IPv6", "prova de servidor DNS", "privadesa del navegador", "privadesa de xarxa", "resolució de problemes VPN", "servidor DNS", "candidats ICE", "adreça IP privada", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Finestra del navegador amb tres panells per a IP pública, DNS i connexions entre parells, amb un túnel sòlid i una ruta alternativa de punts cap a servidors remots."
coverCaption: "Compara cada ruta de xarxa abans i després de connectar la VPN."
---

La icona de connexió d'una xarxa privada virtual (VPN) no demostra que totes les sol·licituds del navegador segueixin la mateixa ruta. Comprova per separat la teva **IP pública**, el **servidor del Sistema de noms de domini (DNS)** i les **adreces WebRTC**. Cada resultat respon una pregunta diferent. Aquesta guia presenta una comprovació repetible i una manera d'investigar resultats inesperats.

<!--more-->

## Idees clau

- **Compara dos estats:** Registra les mateixes proves abans i després de connectar la VPN.
- **Llegeix cada resultat per separat:** Un canvi d'IP pública no indica on han anat les consultes DNS.
- **Revisa els candidats WebRTC:** Busca una adreça pública fora de la ruta prevista. Una adreça privada té un significat diferent.
- **Canvia una opció cada vegada:** Torna a provar després de cada canvi de VPN, navegador o DNS.

## Abans de començar

Fes servir el navegador i la connexió de xarxa que vols protegir. Decideix si la VPN ha de cobrir tot el dispositiu o només algunes aplicacions. Si la VPN fa servir un túnel dividit, anota si el navegador de prova passa pel túnel. Tingues a mà la política DNS del client VPN per comparar-la.

El **túnel dividit** envia algunes aplicacions per la VPN i deixa que les altres facin servir la xarxa habitual.

Aquest procediment fa servir les pàgines [IP de BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) i [WebRTC](https://browserleaks.com/webrtc). El servei veu l'adreça de connexió quan el visites. Segons la descripció de la prova, la prova DNS demana al navegador que resolgui 50 noms aleatoris. No facis proves externes en una xarxa administrada o restringida sense autorització. No introdueixis credencials, noms d'amfitrió interns ni registres privats de navegació en un lloc de proves.

> **Avís:** No publiquis les adreces IP exactes en captures de pantalla públiques ni publicacions de suport. Anota si les adreces coincideixen amb la ruta esperada del proveïdor d'Internet o de la VPN. Comparteix els valors reals només per un canal de suport aprovat.

## Què mostra cada prova

| Comprovació | Què cal comparar | Què no demostra el resultat |
|---|---|---|
| **IP pública** | Adreça que veu un lloc web normal | Quin servidor ha gestionat el DNS |
| **Servidor DNS** | Servidors observats en noves cerques de noms | On envia el DNS cada aplicació |
| **WebRTC** | Candidats de connexió locals i públics | Quin candidat farà servir una trucada posterior |

La pàgina d'IP pública indica l'adreça de la sol·licitud web. La pàgina DNS inicia cerques noves i mostra els servidors que les gestionen. WebRTC, abreviatura de Web Real-Time Communication, permet que les aplicacions del navegador estableixin connexions entre parells. La pàgina WebRTC comprova les adreces exposades durant aquestes connexions. Un **candidat ICE** és una possible adreça de xarxa per a una connexió entre parells. Una **sortida VPN** és l'adreça pública que fa servir el trànsit en sortir de la VPN. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) explica per què els candidats de connexió WebRTC de vegades inclouen adreces diferents de la que veu una sol·licitud web normal, sobretot amb túnels dividits o proxies.

Un servidor DNS del proveïdor VPN, un altre servidor triat dins la VPN o un servidor xifrat triat al navegador mostren noms diferents a la prova. El nom del servidor, per si sol, no identifica una fuita. Compara'l amb la política que volies fer servir.

## Registra una referència inicial

Desconnecta la VPN només si la situació permet una referència sense túnel. Obre les tres pàgines de prova en un perfil normal del navegador. Executa la prova DNS i espera'n el resultat. Registra aquestes dades sense publicar les adreces exactes:

| Camp | Nota inicial |
|---|---|
| **Navegador i versió** | Nom, versió i extensions de privadesa rellevants |
| **Xarxa** | Wi-Fi de casa, punt d'accés mòbil o una altra xarxa aprovada |
| **IPv4 i IPv6 públiques** | Si cada adreça pertany a la connexió habitual |
| **Resultat DNS** | Noms o operadors dels servidors mostrats |
| **Resultat WebRTC** | Candidats públics, privats o `.local` mostrats |

Si no pots desconnectar la VPN, comença amb la ruta VPN prevista i marca la referència sense túnel com a no disponible. No dedueixis l'adreça habitual del proveïdor a partir d'una etiqueta d'ubicació o d'un mapa. Les bases de dades d'ubicació de vegades no coincideixen amb l'operador real de la xarxa.

## Repeteix la prova amb la VPN connectada

Connecta la VPN i confirma que el client indica que el túnel funciona. Torna a carregar cada pàgina de prova al **mateix perfil del navegador**. Executa la prova DNS una altra vegada per generar cerques noves. Registra també els resultats IPv4 i IPv6 quan el servei els mostri.

Compara els resultats en aquest ordre:

1. **IP pública:** La sol·licitud web hauria de mostrar una adreça coherent amb la sortida VPN o la ruta configurada expressament. Si el navegador hauria de passar pel túnel i apareix l'adreça habitual del proveïdor, hi ha un problema d'encaminament.
2. **DNS:** Compara cada servidor indicat amb la configuració DNS de la VPN i del navegador. Investiga si apareix un servidor del proveïdor d'Internet fora del túnel previst. Si has triat expressament un servidor extern al navegador, que aparegui pel nom és normal.
3. **WebRTC:** Compara el candidat WebRTC públic amb la sortida VPN i la IP pública de referència. Si tot el trànsit del navegador hauria de passar per la VPN, que la IP pública habitual aparegui només a WebRTC és un senyal que cal investigar.
4. **Adreces privades:** Una adreça dels [rangs privats RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) o un candidat `.local` és diferent d'una IP pública del proveïdor. Anota l'entrada local i decideix si el lloc l'hauria de conèixer.

L'[estàndard de tractament d'IP de WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descriu com una aplicació obté altres adreces públiques o privades mitjançant la detecció de candidats ICE. El disseny dels [candidats d'amfitrió mDNS de Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) substitueix algunes adreces privades per noms `.local`. Un resultat WebRTC buit és **inconcloent** si JavaScript, l'API o el servidor de proves no han funcionat. Un resultat buit no demostra una protecció completa.

> **Resultat esperat:** La sol·licitud web normal del navegador i els candidats WebRTC públics segueixen la ruta triada. Els resultats DNS coincideixen amb la política DNS de la VPN o del navegador que has registrat.

## Investiga una diferència DNS

Primer comprova si el navegador tria el seu propi servidor DNS. La configuració de [DNS sobre HTTPS del Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) mostra l'estat actiu i el nivell de protecció. La protecció predeterminada torna al servidor del sistema en algunes condicions i respecta els senyals de xarxa. Els nivells Millorada i Personalitzada fan servir un proveïdor triat amb opcions de reserva. El nivell Màxima avisa quan falla la resolució segura. L'estat i la llista d'excepcions importen més que un simple commutador.

La [guia DNS segur del Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) descriu el mode automàtic i un proveïdor personalitzat. El mode automàtic torna a una consulta sense xifrar si falla la resolució segura. Un proveïdor personalitzat no fa servir per defecte el mode sense xifrar. Els dispositius administrats i els controls parentals restringeixen aquesta opció. Consulta la interfície actual del navegador abans de canviar una política administrada.

Si el servidor del navegador no és la causa, compara la configuració DNS del client VPN, la llista d'aplicacions del túnel dividit, el servidor del sistema operatiu i la ruta IPv6. Canvia un element i repeteix la prova DNS. La prova DNS del navegador mesura el camí de consulta d'aquell navegador. No indica com resol noms una altra aplicació. Si la xarxa fa servir [filtratge DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), prova un domini que bloquegis expressament i un altre que permetis. No consideris que l'absència d'un anunci demostra la ruta del servidor DNS.

## Investiga una diferència WebRTC

Comprova si el navegador queda fora del túnel VPN o fa servir un proxy fora de la ruta prevista. Corregeix la ruta i torna a provar. No desactivis IPv6 ni WebRTC com a primera resposta a un únic resultat ambigu. L'[estàndard WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descriu l'equilibri entre exposar l'adreça i mantenir el rendiment de les trucades directes. Restringir candidats o forçar un proxy afecta les videotrucades i altres connexions entre parells.

Si el navegador o la VPN ofereixen un control documentat per tractar les IP de WebRTC, llegeix-ne la descripció actual i tria una política coherent amb l'ús que fas de les trucades. Torna a comprovar el candidat públic. Una adreça local, per si sola, no demostra que la IP pública del proveïdor hagi sortit de la VPN. Una IP pública del proveïdor exposada, comparada amb una adreça HTTP VPN diferent, és un senyal més clar.

## Conserva un registre de les proves

| Camp | Resultat que cal anotar |
|---|---|
| **Data i navegador** | Versió, perfil, extensions i xarxa |
| **Ruta prevista** | VPN per a tot el dispositiu, túnel dividit o proxy del navegador |
| **Abans i després** | Operador de la IP pública, operador DNS i candidat WebRTC públic |
| **Diferència** | Quin resultat no coincidia amb la política prevista |
| **Un canvi** | Opció canviada i motiu |
| **Nova prova** | Resultat nou i incertesa pendent |

Torna a fer la comprovació després de canviar la configuració del navegador, la VPN o la xarxa. Un resultat net només cobreix el navegador, el perfil, la xarxa i el moment provats. No demostra anonimat ni cobreix totes les aplicacions. Si encara tries navegador, consulta la [comparació de navegadors privats](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) per veure'n les funcions i després fes aquesta prova a la teva configuració.

## Passos següents

Repeteix la prova després de canvis al navegador, la VPN o la xarxa. Consulta la [comparació de navegadors privats](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) per triar un navegador.
