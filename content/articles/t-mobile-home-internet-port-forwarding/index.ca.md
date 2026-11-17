---
title: "Per què el reenviament de ports no funciona amb T-Mobile Home Internet"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Entén els límits del reenviament de ports a T-Mobile 5G Home Internet, el NAT de l'operador i les opcions pràctiques per accedir a un servidor domèstic sense un port públic d'entrada."
genre: ["Networking", "Self-Hosted", "Network Security"]
tags: ["T-Mobile Home Internet", "reenviament de ports T-Mobile", "5G Home Internet", "CGNAT", "NAT de nivell d'operador", "NAT", "accés remot", "servidor domèstic", "homelab", "passarel·la T-Mobile", "mode pont", "IP dinàmica", "IPv4 pública", "doble NAT", "Tailscale", "Cloudflare Tunnel", "Cloudflare Access", "xarxa privada", "connexions entrants", "Internet mòbil"]
cover: "/img/cover/t-mobile-home-internet-port-forwarding.webp"
coverAlt: "Una passarel·la cel·lular domèstica es connecta a una torre llunyana i a una porta de xarxa compartida, al costat d'una connexió de núvol lluminosa."
coverCaption: ""
---

**Les passarel·les per a consumidors de T-Mobile 5G Home Internet** no ofereixen reenviament de ports configurable. Afegir una regla a un segon encaminador no canvia la configuració de la passarel·la de l'operador ni crea una ruta pública d'entrada. T-Mobile tampoc documenta cap opció per al mode pont ni per canviar el tipus de traducció d'adreces de xarxa (NAT). [Configuració de la passarel·la T-Mobile](https://www.t-mobile.com/support/home-internet/connect).

Aquest article tracta **Home Internet per xarxa cel·lular**. Considera la fibra i els productes per a empreses serveis diferents, amb les seves pròpies funcions documentades.

## Idees clau

- **Identifica el límit:** distingeix una funció de la passarel·la de la traducció d'adreces en una xarxa superior.
- **Examina la ruta:** registra a quin dispositiu pertanyen cada adreça i port.
- **Compara alternatives:** ajusta l'accés dels clients i els requisits del protocol al mètode d'allotjament.
- **Documenta la decisió:** prepara un pla de connexió amb una prova i una alternativa.

## Abans de començar

**Públic:** usuaris de T-Mobile Home Internet per xarxa cel·lular que volen accedir a un servei domèstic des de fora. **Requisits previs:** accés al servidor, a la configuració de la xarxa local i a la informació d'estat de la passarel·la subministrada. Una segona connexió a Internet va bé per a la prova remota final.

**Temps estimat:** 15–20 minuts per reunir els requisits i fer les comprovacions locals. Configurar un mètode alternatiu d'accés requereix més temps. **Dificultat:** de principiant a intermèdia. L'objectiu és triar una connexió amb criteri, no afegir una altra regla d'encaminador que ningú farà servir.

## Per què una regla local de port no és suficient

El **reenviament de ports** dirigeix el trànsit entrant que arriba a un encaminador cap a una destinació interna. Perquè un servidor domèstic rebi trànsit d'Internet no sol·licitat, la ruta ha de funcionar a través de cada dispositiu superior rellevant. Una connexió local correcta demostra que el servidor és accessible des de la xarxa de casa, no des de fora.

El **NAT de nivell d'operador (CGNAT)** afegeix traducció d'adreces a la xarxa del proveïdor. Els abonats comparteixen la capacitat pública d'IPv4, mentre que el proveïdor controla la traducció externa. La RFC 6598 reserva **`100.64.0.0/10`** per a l'espai d'adreces compartit que s'utilitza en aquest tipus de desplegament. [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598.html).

**El suport de la passarel·la i el NAT de l'operador són qüestions diferents.** La pàgina d'assistència de T-Mobile estableix la limitació de la passarel·la. El CGNAT explica per què configurar el teu encaminador tampoc és suficient quan la traducció superior és fora del teu control. L'absència d'un menú de reenviament de ports no revela per si sola tot el disseny de la xarxa de l'operador.

**A la pràctica, has de triar un model de connexió.** Fes servir una xarxa overlay per a l'accés privat, un túnel de sortida per a un servei HTTP o un endpoint allotjat si els usuaris externs necessiten accés públic. Prova el mètode triat des d'una altra xarxa. Una petició LAN correcta no demostra que s'hi pugui accedir des d'Internet.

| Canvi | Què canvia | Què continua sense resoldre |
|---|---|---|
| **Regla en un segon encaminador** | Reenviament al teu encaminador | Passarel·la de l'operador i ruta superior |
| **Un altre resolver DNS** | Resolució de noms | Connectivitat d'entrada |
| **Nom de DNS dinàmic** | Un nom que segueix una adreça | Una ruta d'entrada utilitzable |
| **Wi-Fi més ràpid** | Rendiment sense fil local | Accessibilitat des d'Internet |

L'**adreçament dinàmic** vol dir que una adreça canvia amb el temps. És diferent de compartir una adreça mitjançant NAT. T-Mobile documenta l'adreçament dinàmic i aquesta pàgina d'assistència no descriu cap opció de consumidor per canviar Home Internet a una adreça estàtica. [Límits de connexió de T-Mobile](https://www.t-mobile.com/support/home-internet/connect).

## Segueix qui controla les adreces

En un **exemple de NAT de l'operador**, la ruta travessa diversos límits independents:

```text
Client remot -> traducció de l'operador -> passarel·la domèstica -> encaminador opcional -> servidor
                    controlada per l'operador   dispositius i ajustos locals
```

**Una adreça visible per a un lloc web** descriu la connexió que hi ha arribat. No estableix un mapatge d'entrada cap al teu servidor. Els requisits CGN descriuen els mapatges mitjançant la identitat de l'abonat, l'adreça externa, el port i l'hora. [RFC 6888](https://www.rfc-editor.org/rfc/rfc6888.html).

**Registra la interfície:** diferencia l'adreça local del servidor, l'adreça WAN del segon encaminador, l'adreça que informa la passarel·la cel·lular i l'observació d'un servei extern. Aquí, **WAN** significa el costat superior d'un encaminador. Una adreça sense l'etiqueta de la interfície és una prova diagnòstica feble.

Considera aquesta **observació il·lustrativa**, amb adreces reservades per a la documentació al costat públic:

| Punt d'observació | Exemple | Interpretació |
|---|---|---|
| **LAN del servidor** | `192.168.50.10` | Destinació local |
| **WAN del segon encaminador** | `192.168.12.20` | Hi ha una altra xarxa privada a dalt |
| **Comprovació externa d'IPv4** | `203.0.113.25` | Adreça visible des de fora |

**Conclusió fonamentada:** el segon encaminador és darrere d'una altra xarxa privada. **Conclusió no fonamentada:** el valor WAN demostra la configuració exacta de traducció de l'operador. Inspecciona la passarel·la cel·lular per separat si la pàgina d'estat mostra l'adreça pertinent.

**Pista del rang d'adreces:** una adreça del costat del proveïdor dins de `100.64.0.0/10` forma part de l'espai compartit. Registra quina interfície l'indica. Si una eina de xarxa privada també assigna adreces d'aquest rang, una captura sense etiquetes és ambigua. La [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598.html) defineix el rang.

## Comprova el servei local

Per a un **tauler HTTP**, executa aquesta petició des d'un altre dispositiu Linux o macOS de la xarxa domèstica. Substitueix l'adreça i el port d'exemple pels del teu servidor:

```bash
curl --connect-timeout 5 --max-time 10 --output /dev/null --write-out '%{http_code}\n' http://192.168.50.10:8080/
```

**`--connect-timeout`** limita el temps per establir la connexió. **`--max-time`** limita tota la petició. **`--output`** descarta el cos de la resposta i **`--write-out`** mostra l'estat HTTP. Aquestes opcions es documenten al [manual de curl](https://curl.se/docs/manpage.html).

**Interpreta el resultat:** una resposta HTTP, inclosa una resposta d'autenticació, indica que un endpoint HTTP ha contestat per aquesta ruta. Confirma'n la identitat al navegador. Un temps d'espera no indica quina capa ha fallat. Després revisa l'adreça d'escolta, el port i el tallafoc de l'amfitrió.

*Aquesta comprovació és per a HTTP. Un joc que utilitza UDP requereix una prova adequada al protocol.*

## Tria una alternativa adequada al servei

**L'accés privat** i **l'allotjament públic** tenen requisits diferents. Primer decideix qui s'ha de connectar i si accepta instal·lar un client.

**TCP** transporta un flux ordenat dins d'una connexió. **UDP** transporta datagrames individuals. L'allotjament ha de ser compatible amb el transport de l'aplicació, encara que dos serveis facin servir el mateix número de port.

| Necessitat | Opció per avaluar | Restricció principal |
|---|---|---|
| **El teu portàtil ha d'accedir al servidor domèstic** | Xarxa privada Tailscale | Registrar els dispositius i configurar les regles d'accés |
| **Tauler privat al navegador** | Cloudflare Tunnel amb Access | Configurar el nom d'amfitrió i la política d'identitat |
| **Lloc web per a visitants públics** | Allotjament públic o túnel adequat | Revisar el protocol, la capacitat i els requisits del servei |
| **Servidor de joc per a clients habituals** | Allotjament amb suport documentat per a ports entrants | Complir els requisits TCP/UDP del joc |

**Tailscale** prova d'establir una connexió directa i admet trànsit retransmès quan falla la comunicació directa. Això evita haver de reenviar manualment un port domèstic, tot i que la ruta resultant afecta el rendiment. Llegeix la [visió general de connexions de Tailscale](https://tailscale.com/docs/reference/connection-types) i la nostra [explicació dels relés](/articles/why-tailscale-uses-a-relay/).

**Cloudflare Tunnel** estableix una connexió de sortida des del servidor. Per a un tauler privat, combina'l amb una política Access. Publicar un nom d'amfitrió sense la política no afegeix cap comprovació d'identitat. Consulta la [connectivitat de Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) i [Tunnel i Access](/articles/cloudflare-tunnel-vs-access/).

**Una subscripció VPN per si sola** no defineix una solució per allotjar connexions entrants. Abans de comprar cap servei, comprova els protocols compatibles, els ports exposats, les opcions d'autenticació i les restriccions. Si es tracta d'un servidor de joc, pregunta concretament quins ports UDP requereix.

## I IPv6?

**L'adreçament IPv6 i el permís per al trànsit entrant** són requisits separats. IPv6 redueix la dependència de la traducció d'adreces IPv4, mentre que el filtratge amb estat de la passarel·la continua controlant les connexions entrants. La RFC 6092 descriu el filtratge IPv6 residencial, inclòs el tractament del trànsit no sol·licitat. No documenta els ajustos de la teva passarel·la T-Mobile. [Recomanacions de seguretat per a IPv6 residencial](https://www.rfc-editor.org/rfc/rfc6092.html).

**Avalua tota la ruta:** el client remot necessita connectivitat IPv6, el servidor necessita una adreça adequada i un procés d'escolta, i la xarxa ha de permetre el trànsit. Una petició web IPv6 correcta demostra una ruta de sortida. No prova que un client d'Internet arribi al teu servidor.

| Prova | Què estableix |
|---|---|
| **Adreça IPv6 al servidor** | S'ha assignat una adreça a una interfície |
| **Petició IPv6 de sortida correcta** | Aquest client ha arribat a un servei extern |
| **Resposta d'una aplicació remota** | La ruta d'entrada provada funciona |

**Regla de decisió:** tria allotjament IPv6 només després de confirmar tota la ruta d'entrada i la compatibilitat dels clients. No tractis l'assignació d'una adreça com a substitut d'una prova remota de l'aplicació.

## Comprova l'aplicació abans de canviar la xarxa

Segueix aquests **passos de diagnòstic** per separar les avaries locals dels límits d'accés remot:

1. **Connexió local:** confirma que un altre dispositiu de casa arriba a l'adreça local i al port previst del servidor.
2. **Configuració del servei:** confirma que l'aplicació escolta a la interfície esperada i que el tallafoc de l'amfitrió permet el client previst.
3. **Públic:** decideix si l'accés ha de ser privat o públic.
4. **Prova remota:** prova el túnel o la xarxa privada triats des d'una altra connexió a Internet.
5. **Rendiment:** mesura la càrrega de treball real quan ja hi ha connectivitat.

**Una prova local fallida** s'ha d'investigar abans de triar un servei d'accés remot. El reenviament de ports no arregla una aplicació que escolta a la interfície equivocada.

## Tria una opció d'allotjament

**Escenari:** vols consultar el tauler de casa mentre viatges i dos amics volen entrar a un servidor de joc. El tauler utilitza HTTP. El joc necessita UDP i els amics volen fer servir els clients habituals del joc sense instal·lar un altre client de xarxa.

**Separa els requisits.** Un tauler de navegador amb una llista petita d'identitats és adequat per a una publicació web autenticada. El joc necessita una ruta pública compatible amb el transport i els clients necessaris. Resoldre el primer requisit no demostra que el segon també es pugui satisfer.

| Requisit | Tria raonada |
|---|---|
| **Tauler privat al navegador** | Avalua Tunnel amb Access |
| **Accés personal amb dispositius registrats** | Avalua una xarxa overlay privada |
| **Clients públics de joc UDP** | Avalua allotjament amb accessibilitat UDP documentada |

**Pregunta de comprovació:** el DNS dinàmic fa que el joc sigui accessible per una ruta d'entrada que no està disponible? No. Actualitzar un nom d'amfitrió no crea el mapatge ni el procés d'escolta necessaris. Rebutja les propostes que només canvien el nom i no expliquen la ruta.

**Anota el compromís:** traslladar el joc a un allotjament extern afegeix despeses recurrents i administració. Demanar als amics que s'uneixin a una xarxa privada els canvia els requisits de configuració. Tria després de decidir quin límit es pot negociar.

## Crea un pla de connexió

Crea un **pla per a un servei** amb aquests camps:

```text
Aplicació i ports TCP/UDP necessaris:
Persones o dispositius que necessiten accés:
És acceptable instal·lar un client:
Resultat de la prova del servei local:
Ruta d'entrada disponible:
Mètode d'accés triat:
Mètode d'autenticació:
Prova remota i criteri d'èxit:
Alternativa si la prova falla:
```

**Criteri de finalització:** cada pas del client remot a l'aplicació té un responsable i un mecanisme compatible. Per a un túnel domèstic, inclou el connector. Per a l'allotjament extern, inclou el tallafoc de l'amfitrió i el procés d'escolta públic. Mantén visibles els supòsits no verificats fins que els confirmis.

## Passos següents

Per a un tauler al navegador, comença amb la [guia de configuració de Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) i afegeix Access. Per obtenir una visió general del servei, llegeix la [presentació de T-Mobile Home Internet](/other/t-mobile-home-internet-benefits-connectivity-features/).
