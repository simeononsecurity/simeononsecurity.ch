---
title: "Construeix un laboratori domèstic en 10 nivells, de Pi-hole a la IA local"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Construeix un laboratori domèstic en deu etapes pràctiques, des del filtratge DNS de tota la xarxa fins a la IA local, amb maquinari, costos, habilitats i compensacions per a cada nivell."
genre: ["Laboratori domèstic", "Autoallotjament", "IA local", "Xarxes domèstiques"]
tags: ["laboratori domèstic", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "IA local", "consum elèctric"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Un laboratori domèstic creix des d'un Raspberry Pi i un encaminador petits fins a emmagatzematge, servidors, equips de xarxa i una estació de treball d'IA local."
coverCaption: ""
---

Construeix un laboratori domèstic en 10 nivells, de Pi-hole a la IA local
=========================================================================

Un **laboratori domèstic** és un conjunt d'ordinadors i serveis que gestiones per resoldre problemes quotidians i aprendre a operar sistemes reals. Pots bloquejar anuncis, automatitzar llums, desar els continguts multimèdia de la família o provar màquines virtuals. **Comença amb una tasca útil.** Afegeix maquinari quan aparegui una limitació real.

Aquesta guia comença amb un Raspberry Pi petit que executa Pi-hole i arriba fins a un servidor amb models d'IA locals. **Cada nivell afegeix una capacitat i una responsabilitat nova.** Les estimacions de costos fan servir un consum orientatiu i una tarifa elèctrica d'exemple de $0.15 per quilowatt hora. Comprova la tarifa local i mesura els equips abans de comprar-ne més.

## Nivell 1: Bloqueja anuncis a tota la xarxa domèstica

Instal·la [Pi-hole](https://docs.pi-hole.net/) en un Raspberry Pi o un altre ordinador petit amb Linux. Pi-hole funciona com un **forat negre DNS**. Quan un dispositiu demana l'adreça d'un domini inclòs en una llista de bloqueig, Pi-hole no retorna cap destinació útil. El navegador, el telèfon i el televisor intel·ligent fan servir el mateix filtre si l'encaminador o el servidor DHCP dirigeix els clients a Pi-hole.

El **filtratge DNS** també funciona fora dels navegadors web, inclosos alguns anuncis d'aplicacions i televisors connectats. El contingut de les pàgines queda fora del filtre, de manera que passen els anuncis servits des del mateix domini que un lloc web o una aplicació. De vegades, una llista de bloqueig impedeix que es carregui un inici de sessió, un vídeo o un pagament. Revisa el registre de consultes de Pi-hole, permet el domini concret quan calgui i prepara un DNS alternatiu per a les interrupcions.

El consum d'energia és baix. Per a un dispositiu de 8 watts que funciona tot el mes, l'estimació és 8 W × 24 hores × 30 dies ÷ 1.000 × $0.15 = **uns $0.86 al mes**. Mesura tota la font d'alimentació a l'endoll. Un segon ordinador, una unitat USB o un adaptador poc eficient canvien el total.

**Aprendràs:** DNS, DHCP, llistes de bloqueig i manteniment bàsic de Linux.

## Nivell 2: Automatitza localment els dispositius intel·ligents

Afegeix [Home Assistant](https://www.home-assistant.io/), que agrupa els dispositius intel·ligents compatibles i les automatitzacions en un sistema. Programa que els llums s'apaguin a l'hora d'anar a dormir. Encén un ventilador quan un sensor de temperatura supera un valor establert. Envia't una notificació quan un sensor de fuites detecti aigua. **Aquestes petites automatitzacions aporten valor immediat.**

El **control local** manté moltes automatitzacions dins de casa quan falla un servei extern o la connexió a Internet. El comportament depèn del dispositiu. Alguns productes encara necessiten un compte del proveïdor, un servei al núvol o Internet per configurar-se i oferir funcions remotes. Comprova els requisits de la integració abans de comprar maquinari.

**Fes una còpia de seguretat de Home Assistant** i desa'n una còpia fora de l'amfitrió. Documenta les integracions i els passos de recuperació. Una targeta SD o un mini PC avariat no hauria d'esborrar la configuració.

**Aprendràs:** integracions de dispositius, activadors, condicions i recuperació de còpies de seguretat.

## Nivell 3: Executa diversos serveis en un mini PC

Un **mini PC empresarial de segona mà** sovint ofereix memòria ampliable, emmagatzematge substituïble i ports útils a un preu baix. Un mini PC Intel N100 acostuma a consumir menys energia i ocupa poc espai. Intel descriu l'N100 com un processador de quatre nuclis i quatre fils, amb un TDP de 6 watts i suport per a un màxim de 16 GB de memòria. La classificació del processador no equival al consum de tot el sistema a l'endoll. Compara l'ordinador concret, la memòria, l'emmagatzematge, la garantia i els ports de xarxa.

Instal·la Linux i fes servir [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) per executar serveis separats en **contenidors**. Un contenidor empaqueta una aplicació i les seves dependències, però comparteix el nucli del sistema operatiu amfitrió. Per exemple, executa un gestor de contrasenyes com el projecte Vaultwarden, mantingut per la comunitat, i un monitor de disponibilitat com Uptime Kuma. **Tracta el gestor de contrasenyes com un servei sensible:** limita'n l'accés, fes servir una autenticació forta, aplica actualitzacions i conserva una còpia xifrada.

**Els contenidors no substitueixen les actualitzacions ni les còpies de seguretat.** Assigna una ubicació d'emmagatzematge a cada servei i anota els passos de recuperació. Un mini PC petit també té límits. Diverses bases de dades, conversions de contingut multimèdia o aplicacions grans poden esgotar la memòria, l'emmagatzematge o el temps de CPU.

**Aprendràs:** administració de Linux, contenidors, volums, actualitzacions i recuperació de serveis.

## Nivell 4: Crea una biblioteca multimèdia domèstica

[Jellyfin](https://jellyfin.org/docs/) és un servidor multimèdia de codi obert. [Plex](https://support.plex.tv/) ofereix un ecosistema de clients polit i funcions opcionals vinculades a un compte. Tots dos organitzen biblioteques personals i transmeten contingut multimèdia a clients compatibles. **Tria segons els clients**, el model d'accés remot, el suport de maquinari i les funcions que necessites.

**Les necessitats d'emmagatzematge** depenen de la mida i la qualitat de la col·lecció. Comença amb un sol disc només si ja tens un pla de còpia de seguretat separat. Fes servir noms de carpetes i metadades coherents perquè el servidor identifiqui bé pel·lícules i episodis.

La **reproducció directa** envia un fitxer compatible al client sense canviar-ne el flux de vídeo. La **transcodificació** converteix l'àudio o el vídeo quan el client, la connexió, els subtítols o la qualitat requereixen un altre format. La transcodificació carrega més el servidor. Prova els dispositius i la xarxa abans de comprar una GPU o una CPU més potent. **Prescindeix d'un servidor multimèdia dedicat** si tots els clients reprodueixen els fitxers directament i un sol amfitrió és suficient.

**Aprendràs:** formats multimèdia, planificació de l'emmagatzematge, velocitat de xarxa i proves de càrrega.

## Nivell 5: Afegeix redundància d'emmagatzematge i una còpia de seguretat separada

Un NAS amb dos discos i **emmagatzematge en mirall** escriu les dades als dos discos. Si un falla, l'altre conserva una còpia actual mentre substitueixes el disc defectuós i reconstrueixes el mirall. La duplicació protegeix la disponibilitat quan falla un disc. **Un mirall no recupera** un fitxer esborrat, no reverteix el xifratge de ransomware ni protegeix contra un robatori, un incendi o una avaria elèctrica que faci malbé els dos discos.

Conserva una **còpia de seguretat separada** en un altre dispositiu o en una altra ubicació. Inclou documents importants, fotografies, exportacions de configuració i dades dels serveis. Programa les còpies i conserva'n diverses versions perquè els canvis accidentals no sobreescriguin totes les còpies bones.

**Prova una restauració.** Tria uns quants fitxers, restaura'ls en una carpeta separada i obre'ls. Per a un servei, restaura les dades en una instància de prova o documenta els passos i verifica cada fitxer. Una còpia que no has restaurat mai és una suposició, no un pla de recuperació.

**Aprendràs:** sistemes de fitxers, substitució de discos, rotació de còpies i proves de restauració.

## Nivell 6: Aprèn virtualització amb un clúster Proxmox petit

[Proxmox VE](https://pve.proxmox.com/pve-docs/) executa màquines virtuals i contenidors en maquinari de servidor. Diversos mini PC units en un **clúster** comparteixen una vista de gestió i permeten aprendre sobre nodes, emmagatzematge i migració. Un clúster és un grup de servidors configurats per coordinar-se. Els seus membres no fusionen la memòria en un únic conjunt gran. **L'alta disponibilitat requereix** planificació addicional i emmagatzematge compartit o replicat adequat.

Una **instantània** registra l'estat d'una màquina virtual en un moment concret i et permet tornar a un estat anterior després d'un canvi al laboratori. Les instantànies solen dependre de l'emmagatzematge original. No són còpies de seguretat independents. **Copia les dades importants en una destinació de còpia separada** i prova de restaurar-les.

Cada node afegeix consum elèctric, ports de xarxa, cables i actualitzacions. Tres ordinadors petits també volen dir tres sistemes per actualitzar i resoldre problemes. Un sol mini PC amb unes quantes màquines virtuals ensenya moltes de les mateixes bases per menys diners. **Afegeix nodes quan** els experiments necessitin aïllament o vulguis practicar operacions de clúster.

**Aprendràs:** màquines virtuals, conjunts d'emmagatzematge, instantànies, pertinença al clúster i manteniment de nodes.

## Nivell 7: Afegeix accés remot privat i separació de xarxa

[Tailscale](https://tailscale.com/kb/) connecta els teus dispositius aprovats en una xarxa privada i et permet accedir a alguns serveis de casa quan ets fora. **Limita l'accés** als dispositius i serveis que necessita cada persona. Protegeix els comptes amb autenticació multifactor i revisa els dispositius i les claus antics.

Un commutador o encaminador administrable amb suport de **VLAN** separa grups de dispositius. Posa els endolls intel·ligents i altres dispositius de confiança baixa en una xarxa diferent de la dels ordinadors amb fitxers personals. Posa l'emmagatzematge en una xarxa accessible només als sistemes que el necessiten. La segmentació limita quins dispositius es comuniquen. Mantén també les actualitzacions, les contrasenyes fortes i les regles d'accés.

**Evita exposar directament els panells d'administració a Internet públic** si no entens els requisits d'autenticació, actualitzacions i tallafoc del servei. Una eina d'accés privat també requereix controlar bé els comptes i els dispositius.

**Aprendràs:** accés privat, permisos basats en identitat, VLAN, regles de tallafoc i límits de confiança entre dispositius.

## Nivell 8: Afegeix un servidor empresarial

Passa a un servidor més gran quan les mesures demostrin que necessites més nuclis de CPU, memòria, badies de discos, ranures PCIe o capacitat de xarxa. Els servidors empresarials antics sovint costen menys de segona mà, però els ventiladors són sorollosos i el **consum en repòs és d'uns 100 a 160 watts**, segons el model i les peces instal·lades. Considera aquest interval una estimació, no una especificació.

Calcula una estimació anual d'electricitat abans de comprar:

`watts mesurats ÷ 1.000 × 24 × 365 × tarifa elèctrica per kWh`

Amb 120 watts i $0.15 per kWh, l'estimació és de 1.051 kWh a l'any, o uns **$158 anuals**. Mesura el servidor concret en repòs i amb la càrrega habitual. Inclou el consum dels discos, la refrigeració i l'UPS.

Comprova la profunditat del xassís, la compatibilitat dels discos, el soroll, el control dels ventiladors, la font d'alimentació i les targetes d'expansió. Un servidor que supera el pressupost d'espai o energia no és una millora pràctica.

**Aprendràs:** maquinari de servidor, gestió remota, ampliació, refrigeració i estimació dels costos operatius.

## Nivell 9: Mesura l'energia i ajusta la mida del laboratori

Fes servir un **mesurador de consum endollable** per mesurar cada ordinador en repòs i durant l'ús normal. Fes una llista dels consumidors més grans. Revisa els paràmetres d'energia de la BIOS, treu targetes i discos que no facis servir i torna a posar els serveis quotidians en mini PC eficients quan no calgui maquinari empresarial.

Engega el servidor gran només quan una càrrega necessiti la seva capacitat. Si fas servir una programació Wake-on-LAN o un control remot de l'alimentació, documenta els passos de recuperació en cas de fallada de xarxa o corrent. Mantén una **llista de dependències dels serveis** per evitar que un apagat interrompi l'emmagatzematge o la xarxa que necessiten altres sistemes.

Un bastidor ajuda a organitzar els equips i el flux d'aire quan el maquinari per a bastidor justifica l'espai. Un UPS cobreix talls breus i dona temps perquè els sistemes s'apaguin bé. Tots dos afegeixen cost de compra, ocupen espai i consumeixen electricitat. **Mesura'n el consum** i inclou el canvi de bateries al pressupost a llarg termini.

**Aprendràs:** mesura de l'energia, gestió de l'alimentació, mapa de dependències i planificació de capacitat.

## Nivell 10: Executa models d'IA localment

[Ollama](https://docs.ollama.com/) baixa models de llenguatge compatibles i els executa al teu ordinador. La **inferència local** manté les sol·licituds i les respostes al maquinari que controles quan fas servir un model i una aplicació locals. Comprova que tot el procés de programari sigui local. Una aplicació connectada, una funció de telemetria o una opció de model al núvol envia dades fora de la xarxa.

Els requisits de maquinari depenen de la mida del model, la quantització, la longitud del context i la velocitat desitjada. **La memòria del sistema o de la GPU ha de contenir** els pesos del model i el context de treball. Els ordinadors petits executen models petits. Els models grans i els contextos llargs requereixen més memòria i sovint una GPU potent. Mesura l'energia durant la inferència. Un sistema amb GPU sol consumir molta més electricitat que un mini PC en repòs.

Els models locals serveixen per redactar, resumir notes privades i classificar de manera senzilla quan la qualitat cobreix les necessitats. Generen respostes incorrectes, i als models petits sovint els costa raonar de manera complexa o tractar dades actuals. Els models al núvol poden fer-ho millor en algunes tasques concretes. **Compara la qualitat, la privadesa, la latència, el cost i l'energia** abans de triar on executar una càrrega.

**Aprendràs:** memòria de models, quantització, inferència, límits de privadesa i avaluació de càrregues.

## Compara els deu nivells

**Els costos són estimacions, no pressupostos.** Els preus del maquinari varien segons la regió, l'estat i la configuració d'emmagatzematge. Estima l'electricitat amb `watts ÷ 1.000 × hores × dies × tarifa per kWh`. Mesura a l'endoll quan puguis i inclou les hores en repòs, perquè molts servidors domèstics funcionen tot el dia.

### Capacitats i maquinari

| Nivell | Capacitat nova | Maquinari habitual |
|---|---|---|
| **1** | Filtratge DNS de xarxa | Raspberry Pi o host Linux petit |
| **2** | Automatització local de dispositius | Pi o mini PC, dispositius compatibles |
| **3** | Diverses aplicacions autoallotjades | Mini PC empresarial de segona mà o sistema N100 |
| **4** | Transmissió de contingut multimèdia personal | Mini PC i emmagatzematge multimèdia |
| **5** | Tolerància a fallades de disc i recuperació | NAS de dos discos i còpia separada |
| **6** | Laboratori de servidors virtuals | Dos mini PC o més |
| **7** | Accés privat i segmentació | Tailscale, encaminador o commutador administrable |
| **8** | Capacitat i ampliació altes | Servidor empresarial |
| **9** | Menys consum d'energia al laboratori | Mesurador de consum, sistemes ajustats |
| **10** | Inferència local de models | PC amb molta memòria, GPU opcional |

### Habilitats, costos i compensacions

| Nivell | Habilitats apreses | Estimació de costos recurrents | Compensació principal |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Uns $1 al mes a 8 W i $0.15/kWh | Queden alguns anuncis i cal revisar els bloquejos falsos |
| **2** | Integracions, activadors, còpies de seguretat | Electricitat de l'amfitrió i cost dels dispositius | Compatibilitat i feina amb les còpies |
| **3** | Docker, actualitzacions, emmagatzematge | Depèn del consum mesurat del sistema | Límits de CPU, memòria i disc |
| **4** | Formats, organització, transcodificació | Emmagatzematge i electricitat del servidor | La transcodificació de vegades demana més maquinari |
| **5** | Mirall, retenció, restauració | Electricitat del NAS, discos, destinació de còpia | Un mirall no és una còpia de seguretat |
| **6** | Proxmox, VM, clústers | Cada node afegeix consum i manteniment | Més nodes impliquen més manteniment |
| **7** | Regles d'accés, VLAN, tallafoc | Equips de xarxa i cost dels serveis | Les regles errònies exposen serveis |
| **8** | Maquinari, refrigeració, gestió remota | Varia segons el servidor, calcula-ho amb les mesures | Soroll, calor i consum en repòs |
| **9** | Mesura, programació, ajust de mida | Cost únic del mesurador, estalvi variable | Programar afegeix passos operatius |
| **10** | Desplegament i avaluació de models | Energia de càlcul i emmagatzematge | Qualitat i velocitat depenen del maquinari |

## Tria la millora útil següent

**Atura't al nivell que cobreix les necessitats actuals.** Pi-hole i un mini PC poden cobrir els teus serveis. Un NAS és útil quan necessites emmagatzematge compartit i un pla de recuperació provat. Afegeix un clúster o un servidor empresarial quan ho justifiqui una càrrega o un objectiu d'aprenentatge.

Anota **on són les dades de cada servei, com s'actualitza i com es restaura.** Prova les còpies abans d'afegir més equips. Deixa que la següent limitació real guiï la propera compra.

## Referències

- [Documentació de Pi-hole](https://docs.pi-hole.net/)
- [Documentació de Home Assistant](https://www.home-assistant.io/docs/)
- [Especificacions del processador Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: Què és un contenidor?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentació de Jellyfin](https://jellyfin.org/docs/)
- [Suport de Plex](https://support.plex.tv/)
- [Documentació de Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentació de Tailscale](https://tailscale.com/kb/)
- [Documentació d'Ollama](https://docs.ollama.com/)
