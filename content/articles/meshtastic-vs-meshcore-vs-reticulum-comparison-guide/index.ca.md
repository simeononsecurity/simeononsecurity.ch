---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Compara Meshtastic, MeshCore i Reticulum segons l'encaminament, el temps d'emissió, la infraestructura, el transport i els usos sense connexió a Internet."
genre: ["LoRa", "Xarxes mesh", "Comunicacions fora de xarxa", "Comunicacions d'emergència", "Radioafició", "Codi obert", "Preparació per a desastres", "Xarxes sense fils", "Privadesa", "Xarxes"]
tags: ["meshtastic vs meshcore vs reticulum", "xarxa reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "xarxa mesh LoRa", "comunicacions fora de xarxa", "rnode", "ràdio per paquets", "xarxes independents del transport", "xarxes mesh", "comunicacions d'emergència", "xarxa mesh comunitària", "temps d'emissió LoRa", "inundació gestionada", "límit de salts", "node repetidor", "servidor de sala", "aplicació sideband", "nomadnet", "meshchat", "comunicacions en desastres", "ràdio fora de xarxa", "protocol de xarxa mesh", "xarxa mesh regional", "enginyeria RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Il·lustració que compara tres sistemes de xarxa mesh amb nodes, antenes i línies de connexió sobre un fons fosc i acolorit."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## Resposta breu

**Aquests tres projectes no resolen el mateix problema.** Meshtastic i MeshCore són sistemes de xarxa mesh LoRa amb filosofies d'encaminament diferents. Reticulum és més ampli: una capa de xarxa independent del transport que funciona alhora sobre LoRa, ràdio per paquets, Wi-Fi, Ethernet, enllaços sèrie i Internet.

**La pregunta adequada no és «quin és el millor?».** És «quina arquitectura s'ajusta a la xarxa que vull construir?»

*Meshtastic s'adapta a l'ús espontani i als usuaris mòbils.* **MeshCore s'adapta a una infraestructura fixa dissenyada expressament.** **Reticulum s'adapta a xarxes que han de connectar transports diferents o unir xarxes separades.** La majoria de qui desplega una sola xarxa LoRa regional només necessita una de les dues primeres opcions.

______

## Defineix la xarxa que vols construir

Abans de comparar protocols, anota què ha de fer la xarxa. Per a la majoria de desplegaments comunitaris i de comunicació d'emergència, aquests objectius són útils:

- **Funcionament sense llicència**, perquè tothom hi participi sense llicència de radioaficionat
- **Maquinari assequible** que una comunitat pugui desplegar a gran escala
- **Consum baix**, idealment sostenible amb energia solar o bateria
- **Comunicació de llarg abast** sense dependència de xarxes mòbils ni d'Internet
- **Independència de la infraestructura**, la xarxa elèctrica, els ISP i les operadores
- **Configuració i ús prou senzills** per a persones sense experiència de ràdio
- **Adequació al desplegament comunitari**, no només al soterrani d'un operador
- **Capacitat de créixer més enllà d'uns quants nodes** sense col·lapsar
- **Utilitat quan falla la infraestructura**, quan les torres mòbils i Internet no funcionen
- **Lliurament fiable per davant d'una distància rècord**

Tingues aquesta llista present. Avaluarem cada compromís arquitectònic segons aquests requisits.

______

## Meshtastic

**Meshtastic** és l'opció més madura i estesa. Resol bé moltes necessitats de l'usuari mitjà.

- **Ecosistema madur**, amb anys de desenvolupament actiu
- **Comunitat d'usuaris gran**, Discord actiu i documentació extensa
- **Àmplia compatibilitat de maquinari** amb plaques LILYGO, Heltec, RAK i Seeed
- **Bones aplicacions mòbils** per a iOS i Android
- **Entrada senzilla**, la configuració inicial dura menys de 20 minuts
- **Bon suport per a usuaris portàtils i itinerants** que entren i surten de la malla de manera imprevisible
- **Funcions GPS i de telemetria**, amb un ecosistema desenvolupat
- **Desplegaments existents** a la majoria d'àrees metropolitanes, de manera que pots unir-te a una xarxa en lloc de començar de zero

Per a una comparació detallada de l'encaminament, la compatibilitat de maquinari i la configuració de Meshtastic amb MeshCore, consulta la **[guia de comparació MeshCore vs Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Aquest article se centra en la qüestió arquitectònica principal dels desplegaments grans: **la inundació gestionada i els límits de salts.**

### Inundació gestionada i importància dels límits de salts

En la **[inundació gestionada](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** de Meshtastic, un client normal cancel·la una retransmissió pendent si abans sent el mateix paquet retransmès. `ROUTER` i `ROUTER_LATE` poden retransmetre igualment. `CLIENT_BASE` fa aquesta excepció per al trànsit cap a un favorit o des d’un favorit.

El comptador de salts de Meshtastic val **3** per defecte i admet fins a **7**. A partir del microprogramari 2.7.11, la infraestructura apta pot [conservar el comptador](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) després del primer salt si el repetidor anterior és un `ROUTER` o `ROUTER_LATE` favorit. Les retransmissions reals continuen ocupant el canal.

Un límit més alt pot arribar a més repetidors, però no obliga tots els receptors a transmetre. **Més reenviaments** poden comportar:

- **Més temps d'emissió** per missatge
- **Més còpies a l’aire** si diversos repetidors aptes reenvien el mateix paquet
- **Més competència** pel canal compartit
- **Més risc de col·lisions** quan més ràdios intenten transmetre alhora
- **Més consum de bateria** a cada node que rep i retransmet
- **Menys capacitat de canal** per al trànsit real de missatges

La capacitat de LoRa està limitada pel temps d'emissió i les restriccions regionals del cicle de treball, no pel nombre de nodes. Una xarxa amb deu nodes molt actius que envien sovint GPS i telemetria pot saturar un canal que cinquanta sensors silenciosos ni tan sols afectarien. Per això una malla densa amb un límit alt de salts es degrada abans que el mateix nombre de nodes distribuït amb menys salts i intervals de telemetria controlats.

Des de Meshtastic 2.6, els **missatges directes** fan servir inundació per descobrir la ruta i després proven el salt següent après. Si falla, poden tornar a la inundació.

En una malla petita o mitjana, com la d'un club d'excursionisme, poques vegades és un problema. En una **xarxa regional que vol cobrir una ciutat o diverses poblacions**, esdevé la principal limitació de disseny.

______

## MeshCore

Els **repetidors dedicats** formen la capa fixa de reenviament de MeshCore. Les ràdios client són els terminals.

### Funcions dels nodes

Els desplegaments MeshCore es basen en funcions diferenciades, no en un conjunt pla de nodes equivalents:

- **Nodes companys o clients**, amb una ràdio LoRa aparellada amb un telèfon o portàtil, que es comuniquen amb la infraestructura propera quan n'hi ha
- **Repetidors**, dedicats a reenviar trànsit entre clients i altra infraestructura, i responsables de gran part de l'encaminament
- **Servidors de sala** opcionals, que conserven converses de grup i lliuren missatges desats als clients quan es tornen a connectar

A MeshCore, un primer **missatge directe** pot inundar la xarxa per descobrir una ruta. Els següents poden seguir-la i tornar a la inundació segons la configuració. **[Els canals de grup públics i privats continuen fent servir inundació](https://docs.meshcore.io/faq/#5-general)** a través de repetidors aptes. Els dispositius client no retransmeten paquets d’altres nodes.

### Per què encaixa amb la infraestructura fixa

*Aquest és l'argument central a favor de MeshCore.* El model d'inundació de Meshtastic té avantatges reals en xarxes espontànies i itinerants: no cal planificar ni mantenir infraestructura i gestiona bé els nodes que apareixen i desapareixen. El model d'encaminament de MeshCore és avantatjós quan **els usuaris despleguen infraestructura deliberadament**.

Una xarxa amb repetidors coneguts i elevats permet dissenyar la cobertura de manera intencionada, en lloc de dependre dels nodes que casualment queden a l'abast els uns dels altres cada dia. Això és important per a:

- **Nodes permanents en teulades** amb alimentació fiable
- **Torres** i infraestructura de comunicacions existent
- **Repetidors solars** en emplaçaments sense personal
- **Punts de retransmissió de muntanya o elevats**
- **Infraestructura comunitària** compartida per diversos grups
- **Xarxes regionals** més grans que un sol barri
- **Comunicacions d'emergència**, on la cobertura previsible pesa més que la flexibilitat

Relaciona-ho amb els principis de RF: **els enllaços fiables entre infraestructures ben situades importen més que maximitzar el guany d'antena, la potència d'emissió o l'abast teòric.** **Totes dues malles es beneficien de repetidors ben situats.** Els nodes que retransmeten depenen del seu paper i del trànsit.

______

## L'argument dels nodes itinerants i per què no és gratuït

Una proposta habitual és: *«Meshtastic és millor per als nodes itinerants, MeshCore per als fixos; fem servir Meshtastic per als usuaris i MeshCore com a xarxa troncal.»*

Sobre el paper sona bé. A la pràctica, barrejar-los no combina automàticament els seus avantatges, perquè **Meshtastic i MeshCore fan servir arquitectures de xarxa i encaminament diferents i no intercanvien missatges.** Connectar-los exigeix una capa de traducció entre dos sistemes incompatibles, no simplement escollir-ne les millors parts.

Després de connectar-los, gestiones:

- **Dues xarxes separades**, cadascuna amb topologia i comportament propis
- **Dos models d'encaminament** que no comparteixen cap estat
- **Una capa de traducció** que exigeix desenvolupament i manteniment continus
- **Més infraestructura** per allotjar el pont
- **Més configuració** en dos ecosistemes de microprogramari en lloc d'un
- **Més punts de fallada**, ja que el pont pot fallar independentment de les dues malles
- **Diagnòstic més difícil**, perquè el lliurament pot fallar en qualsevol xarxa o al pont

Abans d'adoptar aquest disseny, pregunta't: **la complexitat afegida resol un problema que un únic protocol mesh ben ajustat no pot resoldre?** Sovint, un desplegament MeshCore ben configurat amb uns quants nodes companys adaptats al moviment, o un Meshtastic amb uns quants repetidors ben situats i un límit de salts alt, ofereix bona part del benefici sense mantenir dues xarxes enganxades.

______

## Reticulum

Reticulum mereix una categoria pròpia, no una posició com a «tercera opció LoRa mesh», perquè no és principalment un protocol mesh LoRa. **La seva característica clau és la independència del transport.**

Reticulum és una pila de xarxa basada en criptografia. No fa servir adreces d'origen, així que els paquets no indiquen d'on provenen. Cada adreça és sobirana: un cop generada, esdevé accessible globalment en segons o minuts i continua sent-ho encara que es traslladi físicament a una altra part de la xarxa. Totes les comunicacions s'encripten per defecte amb claus efímeres i secret endavant. Reticulum descarta els paquets sense xifrar. No calen controladors del nucli. Funciona en espai d'usuari en qualsevol sistema amb Python 3, inclòs un Raspberry Pi Zero.

Les interfícies que admet Reticulum inclouen:

- **LoRa**, amb maquinari compatible amb RNode, un disseny obert de transceptor LoRa que es pot construir, instal·lar en plaques habituals o comprar preparat
- **Ràdio per paquets**, mitjançant qualsevol TNC en mode KISS, adequat per a ràdioafició VHF i UHF
- **Wi-Fi i Ethernet amb cable**, amb descobriment automàtic de parells, sense encaminador ni servidor DHCP
- **Enllaços sèrie**, per a connexions directes entre dispositius
- **TCP i UDP sobre xarxes IP existents**, inclosa Internet
- **La xarxa I2P** i interfícies personalitzades per a qualsevol altre mitjà amb un pont Python

Sobre Reticulum hi ha aplicacions com **LXMF**, un protocol de missatgeria tolerant a retards, i eines d'usuari com **Sideband**, **NomadNet** i clients comunitaris **MeshChat**, que ofereixen una capa de missatgeria i navegació semblant a la que Meshtastic i MeshCore inclouen de sèrie.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagrama que mostra Reticulum connectant una malla LoRa, una xarxa de ràdio per paquets i un enllaç a Internet en una sola xarxa xifrada i adreçable" >}}

### Quan té sentit Reticulum

El valor de Reticulum es veu clarament en configuracions heterogènies, per exemple:

**Malla LoRa, node Reticulum, enllaç IP, node Reticulum, xarxa de ràdio**

Aquí Reticulum fa una cosa que ni Meshtastic ni MeshCore fan: connecta dos sistemes de comunicació diferents en una única xarxa adreçable. És un requisit real i concret, no una millora genèrica. És útil per a:

- **Connectar xarxes separades geogràficament** sense camí de ràdio directe
- **Enllaçar transports físics diferents**, com ara una malla LoRa en un extrem i ràdio per paquets a l'altre
- **Passarel·les de ràdio a IP** que transmeten trànsit entre una xarxa de camp i Internet
- **Xarxes experimentals i de recerca**, on la flexibilitat per barrejar transports importa més que la simplicitat
- **Xarxes sense un únic transport que cobreixi tot el requisit**, que han d'unir-ne les peces

### Quan Reticulum afegeix complexitat innecessària

Si tothom té maquinari LoRa compatible i l'objectiu real és **una sola malla LoRa regional**, afegir-hi Reticulum aporta poc i té un cost real. Cada capa addicional de xarxa implica més:

- **Configuració** per ajustar i mantenir coherent entre nodes
- **Programari** per instal·lar, actualitzar i diagnosticar
- **Maquinari** en algunes configuracions, segons com s'uneixin les interfícies
- **Superfície de diagnòstic** quan no arriba un missatge
- **Coneixement necessari** perquè els operadors entenguin un tercer model de xarxa

*Fes servir Reticulum quan la independència del transport resolgui una necessitat real, no perquè admeti més tipus d'interfícies.* Un problema de límit de salts en una sola malla LoRa és un problema d'ajust de Meshtastic o MeshCore. No és un problema d'independència del transport, i Reticulum no el converteix en això.

______

## Construeix una malla sana abans de tres xarxes fragmentades

Si un protocol ja compleix els requisits, **construeix una xarxa sana** en lloc de diverses xarxes petites unides amb ponts. Aquest principi de «primer una sola malla» hauria de guiar la majoria de decisions anteriors.

En una xarxa comunitària, **la interoperabilitat entre les persones que ja l'utilitzen sol ser més important que la flexibilitat arquitectònica.** Una xarxa gran i funcional d'un sol protocol té més valor pràctic que tres xarxes tècnicament interessants però fragmentades, que només es comuniquen parcialment.

### Les xarxes Meshtastic existents importen

**No descartis Meshtastic només perquè MeshCore té avantatges arquitectònics per a infraestructura fixa.** Si una ciutat ja té desenes o centenars de nodes Meshtastic, aquesta base instal·lada és infraestructura i comunitat reals. Migrar té un cost que una comparació de fitxes tècniques no reflecteix:

- **Maquinari instal·lat** que cal reflashejar o substituir
- **Usuaris existents** que ja saben fer servir la xarxa
- **Coneixement comunitari** acumulat al voltant del desplegament
- **Repetidors desplegats** en llocs difícils d'aconseguir, com teulades o torres
- **Experiència de configuració** de qui administra la xarxa
- **Canals establerts** que la gent ja supervisa
- **Formació necessària** per a qui aprengui un segon sistema

L'elecció del protocol és **alhora un problema d'enginyeria i d'adopció comunitària.** L'arquitectura millor sobre el paper no guanya automàticament si obliga una comunitat funcional a començar de nou.

______

## El problema de la xarxa regional

Considera aquest desplegament hipotètic entre ciutats:

**Ciutat A, repetidor, repetidor, relé rural, repetidor, Ciutat B, repetidor, Ciutat C**

En aquesta cadena, **prova per separat els missatges de grup i els directes**. MeshCore pot reutilitzar una ruta per als directes, però inunda per als missatges de grup. Meshtastic pot conservar el comptador en enllaços d’infraestructura aptes. Cada retransmissió ocupa el canal. Cap protocol garanteix el lliurament d’extrem a extrem.

En aquest escenari, **els límits de salts, el pressupost d'emissió, l'encaminament i el disseny de la infraestructura deixen de ser teòrics** i determinen si la xarxa funciona d'extrem a extrem. A escala geogràfica, les diferències entre Meshtastic i MeshCore deixen de ser acadèmiques.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagrama d'una xarxa mesh regional que connecta tres ciutats amb repetidors i un relé rural, i mostra com s'acumulen el temps d'emissió i els salts amb la distància" >}}

______

## La RF continua important més que el protocol

**Cap programari d'encaminament crea un camí RF on físicament no n'hi ha.** Abans de culpar el protocol d'un problema de cobertura, comprova els fonaments:

- **Alçada de l'antena** per sobre dels obstacles
- **Línia de visió** entre els dos extrems de l'enllaç
- **Despejament de la zona de Fresnel**, diferent de la línia de visió visual
- **Pèrdues de la línia d'alimentació** per un coaxial barat o massa llarg
- **Qualitat de l'antena** i compatibilitat amb la banda utilitzada
- **Nivell de soroll** al lloc de recepció
- **Terreny** entre nodes
- **Ubicació dels nodes** i marge real de millora
- **Marge de l'enllaç**, diferència entre el senyal rebut i el mínim per descodificar

*Sovint una antena de 2 dBi ben situada en un bon màstil supera una antena de guany alt mal situada en una finestra de soterrani.* El protocol determina com la xarxa gestiona els enllaços disponibles. No crea els que la física no permet.

### Fiabilitat per davant de l'abast màxim

**No dissenyis la xarxa segons la distància màxima que un enllaç assoleix ocasionalment.** Dissenya-la perquè funcioni de manera constant.

En una xarxa comunitària o d'emergència, **un lliurament previsible a 15 milles té més valor pràctic que un enllaç que completa de vegades 40 milles i falla la resta del temps.** Crea cobertura solapada amb infraestructura fiable en lloc de perseguir rècords d'abast. Aquest principi val per a tots els protocols.

______

## Quin cal triar

**Meshtastic és adequat** si valores un ecosistema madur, una adopció senzilla, usuaris portàtils i itinerants, i la compatibilitat amb una comunitat Meshtastic existent. És l'opció inicial per defecte per a la majoria de qui comença de zero.

Els **repetidors fixos** ajuden a planificar la cobertura, no a eliminar la inundació. Abans de triar, prova tots dos protocols amb el volum de missatges de grup, els ajustos de ràdio i la disposició dels repetidors previstos.

**Reticulum és adequat** quan el problema supera una sola malla LoRa i necessites connectar transports diferents o xarxes separades en un sistema adreçable.

Per a una **xarxa comunitària sense llicència, de baix consum i llarg abast, basada principalment en repetidors fixos**, inclina't per MeshCore. **Prova el trànsit de grup abans de canviar.** Una xarxa de repetidors fixos ajuda amb la cobertura, però no dona rutes dirigides als canals de grup. *Si ja hi ha una xarxa Meshtastic sana a la teva zona, substituir-la ha d'aportar prou benefici per justificar la fragmentació de la comunitat.* Reticulum entra en joc quan un protocol mesh o un transport físic no basta, no simplement perquè faci més coses.

______

## Referències

1. [Algorisme de difusió mesh de Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configuració LoRa de Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Lloc oficial de MeshCore](https://meshcore.co.uk/)
4. [Pila de xarxa Reticulum](https://reticulum.network/)
5. [Què és Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Configuració d'interfícies de Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Guia de comparació MeshCore vs Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
