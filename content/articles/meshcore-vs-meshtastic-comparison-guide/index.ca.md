---
title: "MeshCore o Meshtastic: comparació"
date: 2026-06-26
lastmod: 2026-11-12
toc: true
draft: false
description: "Compara MeshCore i Meshtastic segons l’encaminament, l’abast, el temps d’emissió, la infraestructura, els dispositius compatibles i l’ús adequat."
genre: ["LoRa", "Xarxes mesh", "Comunicacions fora de xarxa", "Comunicacions d’emergència", "Comunicacions tàctiques", "Radioafició", "Codi obert", "Preparació per a desastres", "Xarxes sense fil", "Privadesa"]
tags: ["meshcore contra meshtastic", "meshtastic", "meshcore", "xarxa mesh lora", "comunicacions fora de xarxa", "comparació meshtastic", "comparació meshcore", "ràdio lora", "xarxes mesh", "comunicacions d’emergència", "mesh tàctica", "ràdio fora de xarxa", "protocol meshtastic", "protocol meshcore", "lora meshtastic", "comunicacions en desastres", "ràdio mesh", "emmagatzematge i reenviament", "flooding lora", "mesh LoRa", "t-beam meshtastic", "heltec lora", "rak wisblock", "missatgeria fora de xarxa", "protocol de xarxa mesh", "meshtastic 2.6", "temps d’emissió lora", "ràdio d’emergència"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Il·lustració de dues xarxes mesh LoRa: Meshtastic a l’esquerra, amb nodes que difonen paquets, i MeshCore a la dreta, amb encaminament estructurat, sobre un fons fosc."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## Resposta breu

Meshtastic i MeshCore funcionen amb el mateix maquinari LoRa econòmic. Tots dos permeten enviar missatges xifrats sense xarxa mòbil ni Internet. **Els dos protocols no són compatibles.**

**La filosofia d’encaminament és diferent.** Meshtastic difon paquets a tots els nodes propers. MeshCore encamina el trànsit per una infraestructura planificada. Aquests enfocaments ofereixen resultats diferents quan la xarxa creix.

*Meshtastic és adequat per a la majoria.* L’aplicació mòbil és polida, la comunitat és gran, la documentació és sòlida i configurar-lo triga menys de 20 minuts. MeshCore s’ajusta millor a desplegaments planificats on l’eficiència del temps d’emissió importa més que l’autoorganització espontània.

**Els fonaments de la radiofreqüència importen més que el microprogramari.** Cap dels dos protocols compensa una antena mal situada.

______

## Què fa cada sistema

### Meshtastic

**Meshtastic** és un projecte de codi obert iniciat el 2020 per Kevin Hester. El microprogramari converteix maquinari LoRa habitual en una xarxa mesh de missatges de text que no depèn d’Internet ni de xarxes mòbils. Les emissions utilitzen flooding controlat: cada node torna a transmetre els paquets fins a un límit de salts configurable. Des de la versió 2.6, **els missatges directes utilitzen encaminament al salt següent** després de descobrir la ruta, en lloc de flooding. Això redueix el temps d’emissió del trànsit punt a punt.

El microprogramari funciona amb maquinari LoRa que molts usuaris ja tenen o compren a baix cost. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock i Seeed SenseCAP Indicator** admeten Meshtastic sense eines especialitzades. Les aplicacions d’iOS i Android es mantenen bé. Els usuaris sense perfil tècnic es connecten en menys de deu minuts. L’ecosistema inclou ponts MQTT, integració amb Home Assistant i connectors ATAK.

### MeshCore

**MeshCore** va guanyar popularitat el 2023 i el 2024. El microprogramari funciona amb bona part del mateix maquinari LoRa, però utilitza una **arquitectura d’encaminament híbrida**. Primer es descobreixen les rutes. Després, el trànsit passa per repetidors fins a la destinació, en comptes de difondre’s a tothom. No és emmagatzematge i reenviament pur en el sentit de les xarxes tolerants als retards.

Els repetidors fan la major part del reenviament. **Els servidors de sala són opcionals.** Guarden missatges de grup perquè els clients els recuperin quan es tornin a connectar. Els clients fan servir una ràdio LoRa complementària i es connecten a través de la infraestructura quan n’hi ha, o es comuniquen directament amb nodes propers quan no hi ha repetidor.

______

## La diferència tècnica principal

### Com funciona l’encaminament de Meshtastic

Les emissions utilitzen **flooding controlat**. Cada node retransmet el paquet fins al límit de salts. Cap node necessita conèixer la topologia. Els nodes nous s’incorporen sense configurar-los i els nodes caiguts s’eviten automàticament. Des de la versió 2.6, **els missatges directes utilitzen encaminament al salt següent** després de descobrir la ruta, cosa que redueix el temps d’emissió punt a punt.

**La restricció real és el temps d’emissió, no el nombre de nodes.** LoRa utilitza bandes ISM compartides amb límits regionals de cicle de treball, normalment de l’1 % a Europa. Una xarxa amb senyals GPS freqüents, telemetria i trànsit actiu al canal satura el temps d’emissió abans d’assolir un límit absolut de nodes. Deu nodes actius que envien telemetria sovint creen més contenció que cinquanta sensors silenciosos. Les xarxes denses amb desenes d’usuaris actius sovint tenen més contenció, però no hi ha un límit fix. El llindar depèn del factor d’eixamplament, el perfil del temps d’emissió, els intervals de telemetria, el terreny i la ubicació dels repetidors.

Meshtastic genera trànsit addicional amb anuncis d’informació dels nodes, telemetria de la bateria, paquets GPS i descoberta dels veïns. Les versions recents del microprogramari han reduït aquest trànsit. *Ajustar aquests paràmetres sovint resol els problemes de rendiment abans que calgui canviar de protocol.*

### Com funciona l’encaminament de MeshCore

MeshCore descobreix rutes, les aprèn i després encamina el trànsit cap a la infraestructura en lloc de retransmetre’l a tothom. **Els repetidors reenvien trànsit entre nodes.** Els servidors de sala poden allotjar converses de grup i guardar missatges per als clients que es reconnectin més tard.

L’ocupació del canal depèn de les converses actives, no del nombre total de nodes. Un desplegament gran amb molts nodes silenciosos no perd rendiment com una xarxa densa de flooding amb molt de trànsit addicional. MeshCore està dissenyat per a desplegaments força més grans, tot i que el rendiment real depèn de la qualitat de la implementació.

Sense repetidor, els clients es comuniquen directament si són dins de l’abast. *L’arquitectura funciona millor amb infraestructura. La infraestructura no és obligatòria.*

______

## Maquinari

Tots dos protocols funcionen amb les mateixes plaques LoRa populars.

| Placa | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Sí | Sí |
| LILYGO T-Echo (nRF52840 + SX1262) | Sí | Sí |
| Heltec WiFi LoRa 32 V3 | Sí | Sí |
| RAK WisBlock 4631 | Sí | Sí |
| Seeed SenseCAP Indicator | Sí | Parcial |
| Station G2 | Sí | Sí |

**Pots instal·lar qualsevol dels dos microprogramaris al mateix dispositiu físic.** Canviar de protocol no requereix maquinari nou. Experimentar només costa temps.

______

## Facilitat de configuració

### Configurar Meshtastic

1. Baixa el microprogramari de meshtastic.org
2. Instal·la’l amb el flasher web de flasher.meshtastic.org, sense controladors
3. Instal·la l’aplicació Meshtastic al telèfon
4. Vincula el dispositiu per Bluetooth
5. Uneix-te a un canal o crea’n un amb un nom i una contrasenya compartits

**Temps total per a un usuari novell: menys de 20 minuts.** El xifratge del canal utilitza claus precompartides AES-256. El canal públic per defecte et connecta de seguida amb qualsevol node Meshtastic dins de l’abast. L’aplicació mostra les posicions GPS en un mapa quan els nodes tenen el GPS activat.

### Configurar MeshCore

1. Instal·la el microprogramari al node d’infraestructura, repetidor o servidor de sala, amb PlatformIO o binaris precompilats
2. Instal·la el microprogramari a la ràdio complementària del client
3. Instal·la l’aplicació MeshCore
4. Configura a l’aplicació l’adreça i les credencials de la infraestructura
5. Connecta la ràdio complementària per Bluetooth

**La configuració requereix més planificació.** Cal entendre els rols dels nodes abans del desplegament. Els servidors de sala són opcionals, però afegeixen persistència dels missatges per als clients desconnectats. *Dos amics que volen comunicar-se de pressa haurien d’utilitzar Meshtastic. Un equip que instal·la una estació base amb un repetidor al terrat hauria d’utilitzar MeshCore.*

______

## El temps d’emissió és la restricció real

Tots dos protocols funcionen amb LoRa. **La capacitat de LoRa depèn del temps d’emissió i del pressupost del cicle de treball, no del nombre de nodes.**

Les variables que determinen el rendiment de la xarxa:

- **Factor d’eixamplament.** Els valors més alts augmenten l’abast, però redueixen la velocitat de dades i la capacitat total.
- **Perfil del temps d’emissió.** Els perfils de llarg abast consumeixen més cicle de treball per missatge.
- **Interval de telemetria.** GPS, bateria i paquets ambientals de Meshtastic afegeixen trànsit continu.
- **Freqüència dels missatges.** Els usuaris actius que envien sovint afecten més que els nodes passius.
- **Ubicació dels repetidors.** Un repetidor ben situat reparteix la càrrega. Un de mal situat augmenta la congestió.
- **Terreny.** Els nodes que no se senten afegeixen trànsit sense crear contenció. Els nodes a l’abast de molts altres alhora sí que la creen.

*Meshtastic redueix la planificació i accepta una mica de sobrecàrrega d’emissió per l’autoorganització. MeshCore exigeix planificació i la recompensa amb una eficiència d’emissió més previsible. Canviar a MeshCore sense millorar la planificació de la xarxa no garanteix un millor rendiment.*

______

## Consideracions normatives

Les comparacions de rendiment varien segons la regió perquè les normes són diferents:

- **915 MHz (EUA):** no hi ha un límit fix de cicle de treball segons FCC Part 15, però s’apliquen límits de potència.
- **868 MHz (UE):** cicle de treball de l’1 % segons ETSI, és a dir, 36 segons d’emissió per hora i canal.
- **433 MHz (UE/Àsia):** moltes regions imposen límits més estrictes, sovint del 10 % en certes subbandes.

**El límit de cicle de treball de l’1 % a Europa és una restricció normativa estricta.** Les xarxes Meshtastic denses a la UE arriben als límits més ràpid que desplegaments equivalents als EUA. L’ús més eficient del temps d’emissió de MeshCore aporta un avantatge proporcionalment més gran a les regions amb límits de cicle de treball.

______

## Privadesa i seguretat

### Meshtastic

Meshtastic xifra el trànsit dels canals privats amb **claus precompartides AES-256**. Tots els missatges d’un canal comparteixen la mateixa clau. Qualsevol persona amb la clau pot llegir tots els missatges, incloses les posicions GPS. **El canal públic per defecte utilitza una clau coneguda que es distribueix amb el microprogramari**, per tant no manté confidencial el trànsit davant de qui utilitzi Meshtastic a prop.

Les posicions GPS d’un canal privat xifrat només són visibles per als nodes amb la clau. Al canal públic, qualsevol persona les veu. *Això importa quan el seguiment té conseqüències operatives.*

Meshtastic 2.6 va millorar l’encaminament dels missatges directes. El trànsit de grup continua utilitzant la clau precompartida del canal. Els missatges directes ofereixen més aïllament, però no tenen xifratge d’extrem a extrem en el sentit del protocol Signal.

### MeshCore

L’encaminament híbrid de MeshCore vol dir que **un oient passiu no pot reconstruir tota la topologia de la xarxa només escoltant-la**. El trànsit es dirigeix a infraestructura específica en lloc de difondre’s a tothom. **Els missatges directes utilitzen xifratge per contacte**, no una clau de canal compartida. Els altres nodes de la mateixa infraestructura no poden desxifrar la teva conversa directa encara que utilitzin el mateix repetidor.

Els nodes d’infraestructura retransmeten trànsit xifrat. En missatges directes amb xifratge per contacte, el repetidor reenvià el text xifrat sense desxifrar-lo. En el trànsit de sala, els servidors de sala veuen el contingut de les sales que allotgen. *La pregunta important és si controles el servidor de sala.*

MeshCore no ofereix xifratge estricte d’extrem a extrem com Signal. **El xifratge per contacte dels missatges directes millora notablement la protecció respecte a una clau de canal compartida.** Els usos operatius d’alt risc haurien d’avaluar els detalls de la implementació.

______

## Consum d’energia

Amb la configuració per defecte, MeshCore genera menys transmissions de ràdio addicionals que Meshtastic. **Menys emissions milloren l’autonomia de la bateria dels nodes clients.** La telemetria, les difusions GPS i el flooding controlat de Meshtastic consumeixen temps d’emissió. Pots reduir aquesta càrrega ajustant els intervals de telemetria i desactivant les difusions GPS als nodes sense GPS. Amb valors per defecte equivalents, **MeshCore transmet menys**.

Un desplegament Meshtastic ben ajustat, amb telemetria mínima, s’acosta a l’autonomia de MeshCore. La configuració per defecte afavoreix MeshCore.

______

## Resiliència de la xarxa

**El flooding controlat de Meshtastic és resistent.** La pèrdua d’un node de retransmissió sovint té poc efecte operatiu perquè els altres nodes redirigeixen el trànsit de manera natural. No cal conèixer per endavant els nodes disponibles. La xarxa es recupera passivament.

**MeshCore depèn més de la ubicació dels repetidors.** Una xarxa MeshCore ben dissenyada, amb bona cobertura de repetidors, té un rendiment previsible. Si es perd l’únic repetidor d’una zona de cobertura, els nodes que en depenen perden la connexió. *MeshCore recompensa la planificació prèvia. Meshtastic tolera millor les fallades dels nodes.*

Meshtastic accepta sobrecàrrega d’emissió a canvi de resiliència. MeshCore accepta dependència de la infraestructura a canvi d’eficiència.

______

## GPS i seguiment de posicions

**L’ecosistema GPS de Meshtastic és més complet.** L’aplicació mòbil inclou una vista de mapa. Els nodes de la comunitat alimenten mapes públics com meshmap.net mitjançant passarel·les MQTT. La telemetria GPS és una funció principal. Compartir la posició per a grups excursionistes, coordinació de recerca i rescat i esdeveniments està ben desenvolupat.

MeshCore no se centra en el seguiment de posicions. *Si la visibilitat GPS és un requisit principal, l’ecosistema de Meshtastic està més desenvolupat i és més madur el 2026.*

______

## Ecosistema i comunitat

Meshtastic té una **comunitat més gran**:

- Discord actiu amb milers de membres
- Subreddit actiu a r/meshtastic
- Documentació extensa a meshtastic.org
- Integracions de tercers amb MQTT, Home Assistant, Node-RED, ATAK i biblioteques Python
- Llançaments regulars de microprogramari
- Moltes guies de maquinari creades per la comunitat

MeshCore creix, però continua sent més petit. *Hi ha menys publicacions en fòrums, tutorials i integracions de tercers. Quan alguna cosa falla, buscaràs respostes al codi font del microprogramari o al Discord del projecte, en lloc de trobar solucions ja documentades.*

Tots dos projectes són de codi obert, però les llicències són diferents. **Meshtastic utilitza una llicència de tipus BSD. MeshCore utilitza GPL.** Algunes organitzacions ho tenen en compte per al desplegament i la distribució.

______

## Quan Meshtastic és la millor opció

**Grups petits i informals.** Un club excursionista que vol missatges fora de xarxa i compartir la posició hauria de fer servir Meshtastic. És fàcil de configurar, el mapa funciona bé i la xarxa s’autoorganitza.

**Desplegaments mòbils.** Els usuaris que travessen terrenys i s’incorporen o marxen de manera imprevisible encaixen amb el flooding autoorganitzat de Meshtastic. No cal planificar la infraestructura per als nodes mòbils.

**Desplegaments per a consumidors.** Les persones sense coneixements tècnics configuren els dispositius pel seu compte. Meshtastic és accessible.

**Desplegament ràpid per a un esdeveniment.** Comunicacions de festivals, coordinació de curses o recerca i rescat instal·lats avui i retirats la setmana vinent. La configuració ràpida i la manca de dependència d’infraestructura fan que Meshtastic sigui pràctic.

**Seguiment GPS.** Si la posició és l’ús principal, Meshtastic és l’opció adequada el 2026.

______

## Quan MeshCore és la millor opció

**Desplegaments amb infraestructura planificada.** Tens un repetidor al terrat o un servidor de sala amb alimentació fiable. L’encaminament híbrid de MeshCore aprofita la infraestructura fixa.

**Xarxes grans amb infraestructura dedicada.** El desplegament prioritza l’eficiència del temps d’emissió i un rendiment previsible a escala per damunt de l’autoorganització espontània.

**Persistència dels missatges amb connectivitat intermitent.** Els servidors de sala guarden els missatges i els lliuren quan els clients es tornen a connectar. **Aquest és un dels avantatges pràctics més concrets de MeshCore respecte a Meshtastic.**

**Separació entre nodes fixos i mòbils.** Alguns nodes han de fer d’infraestructura i d’altres han de ser clients. El model de rols de MeshCore es va crear per a aquesta separació.

**Regions amb restriccions del cicle de treball.** Els desplegaments europeus subjectes al límit ETSI de l’1 % aprofiten més l’ús eficient del temps d’emissió de MeshCore.

**Xifratge per contacte.** Per xifrar missatges directes, el model de MeshCore és molt millor que l’enfocament de Meshtastic basat en clau compartida del canal.

______

## Quan cada sistema falla

### Punts febles de Meshtastic

- **Contenció del temps d’emissió a escala.** Les xarxes denses amb valors per defecte de trànsit elevat, difusions GPS freqüents i canals actius es degraden. Ajusta la configuració abans de canviar de protocol.
- **Sense persistència de missatges sense infraestructura.** Sense passarel·la MQTT, els missatges perduts no es recuperen.
- **Privadesa de posició al canal públic.** Qualsevol oient veu totes les difusions GPS. És acceptable per a un ús informal, però no per a necessitats de seguretat operativa.
- Les versions principals del microprogramari de vegades provoquen problemes de compatibilitat fins que tota la xarxa utilitza una versió corresponent.

### Punts febles de MeshCore

- **Configuració complexa.** Cal entendre els rols d’infraestructura abans d’implementar-lo amb sentit.
- **Comunitat més petita.** La documentació, els tutorials i les integracions de tercers de Meshtastic estan més desenvolupats.
- **Menys varietat de maquinari.** MeshCore admet una llista més reduïda de dispositius.
- **Aplicacions mòbils menys madures.** Funcionen, però no són tan polides com les aplicacions d’iOS i Android de Meshtastic.
- **Dependència de la infraestructura per obtenir un rendiment òptim.** Sense repetidors, els clients es comuniquen directament, però desapareix l’eficiència de l’encaminament. Si el grup no manté infraestructura fixa, l’avantatge arquitectònic no es materialitza.
- **Recuperació de la xarxa.** Perdre un repetidor en una zona talla la connexió dels nodes dependents. El flooding de Meshtastic tolera millor les fallades.
- **Cap interoperabilitat entre protocols.** MeshCore i Meshtastic no intercanvien missatges. El mateix maquinari admet qualsevol microprogramari, però fer servir tots dos vol dir gestionar dues xarxes separades.

______

## La radiofreqüència importa més que el microprogramari

**La qualitat i l’alçada de l’antena, les pèrdues del cable, el terreny i la configuració de ràdio afecten més el rendiment de la xarxa que l’elecció del microprogramari.**

Un node Meshtastic ben situat al cim d’un turó amb una bona antena supera un repetidor MeshCore mal situat dins d’una caixa metàl·lica al soterrani. La comparació assumeix una qualitat física de desplegament semblant.

Abans de canviar de protocol per resoldre un problema de rendiment, comprova:

- Les connexions de l’antena són netes i tenen poques pèrdues.
- Els nodes són tan alts com sigui possible.
- El perfil del temps d’emissió coincideix amb l’abast necessari.
- **Els intervals de telemetria no saturen el canal.**
- El factor d’eixamplament s’ajusta a la densitat dels nodes.

______

## Resum comparatiu

| Factor | Meshtastic | MeshCore |
|---|---|---|
| Model de xarxa | Flooding controlat i DM pel salt següent | Descoberta híbrida de rutes i reenviament dirigit |
| Dificultat de configuració | Fàcil | Mitjana a alta |
| Disseny per escalar | Flexible, es degrada amb la contenció d’emissió | Dissenyat per a xarxes planificades més grans |
| Qualitat de l’aplicació mòbil | Excel·lent | Funcional |
| Mida de la comunitat | Molt gran | En creixement |
| GPS i seguiment de posició | Ecosistema desenvolupat | Poc centrat |
| Persistència dels missatges | No. Necessita una passarel·la MQTT | Sí, amb servidors de sala opcionals |
| Xifratge de missatges directes | PSK del canal | Xifratge per contacte |
| Necessitat d’infraestructura | No cal | Optimitzat per a nodes d’infraestructura |
| Recuperació de la xarxa | Resilient i auto-recuperable | Depèn de la ubicació dels repetidors |
| Suport de maquinari | Ampli | Selecció limitada |
| Adequat per a | Grups mòbils, improvisats i petits | Desplegaments planificats amb infraestructura fixa |

______

## Quin has de triar

**Comença amb Meshtastic.** En una tarda ja podràs transmetre. Trobaràs gent per provar-lo. L’aplicació funciona i la documentació és excel·lent. L’encaminament al salt següent de Meshtastic 2.6 redueix la diferència d’eficiència per al trànsit directe punt a punt.

**Passa a MeshCore quan els valors per defecte de Meshtastic no s’ajustin al desplegament.** Si tens repetidors dedicats, necessites persistència per a usuaris intermitents o construeixes una xarxa gran i planificada on l’eficiència d’emissió importa més que l’autoorganització, l’arquitectura de MeshCore s’ajusta i justifica l’esforç de configuració.

Abans de canviar de protocol, **ajusta el desplegament Meshtastic**. Redueix els intervals de telemetria. Desactiva les difusions GPS als nodes sense GPS. Adapta el perfil del temps d’emissió a la densitat dels nodes. *Moltes xarxes amb problemes de rendiment tenen problemes de configuració, no de protocol.*

Els protocols ocupen punts diferents en l’equilibri entre planificació i espontaneïtat. Meshtastic redueix la planificació i accepta la sobrecàrrega d’emissió de l’autoorganització. MeshCore exigeix planificació i la recompensa amb un rendiment més previsible. **Cap no substituirà l’altre, perquè els usos són diferents.**

*Estàs creant una xarxa que ha de connectar LoRa amb packet radio, Wi-Fi o Internet, en lloc de quedar-se en una sola xarxa mesh LoRa?* Consulta la **[guia comparativa de Meshtastic, MeshCore i Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** per veure on encaixen les xarxes independents del transport i on afegeixen complexitat innecessària.
