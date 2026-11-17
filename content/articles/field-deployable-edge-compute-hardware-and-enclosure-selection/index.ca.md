---
title: "Computació a la perifèria per al camp: selecció d’equipament i carcassa"
date: 2026-08-25
lastmod: 2026-11-13
toc: true
draft: false
description: "Guia del maquinari edge per a desplegaments al camp i de la selecció de carcasses, amb càlcul, bastidors, refrigeració, emmagatzematge, gestió, cablejat i compatibilitat elèctrica."
genre: ["Computació a la perifèria", "Informàtica de camp", "Equipament", "Laboratori domèstic", "Informàtica resistent", "Xarxes", "Recuperació de desastres", "Informàtica per a petites empreses"]
tags: ["servidor transportable de camp", "edge computing", "mini centre de dades", "carcassa resistent", "centre de dades portàtil", "servidor en maleta Pelican", "servidor thin client", "HP t740", "bastidor o safata", "grau IP", "carcassa NEMA", "mini PC sense ventilador", "gestió de cables", "kit de TI de camp", "servidor compacte muntat", "maquinari de recuperació de desastres", "TI transportable", "TI expedicionària", "maquinari de node edge", "bastidor amb amortidors", "emmagatzematge NVMe SSD de camp", "servidor RAID de camp", "resistència dels SSD a les vibracions", "redundància d'emmagatzematge edge", "gestió remota IPMI", "gestió fora de banda BMC", "PiKVM IP-KVM", "tipus d'endolls internacionals", "font amb entrada universal"]
cover: "/img/cover/field-deployable-edge-compute-hardware-enclosure-selection.webp"
coverAlt: "Una maleta de transport resistent oberta mostra equips de servidor i xarxa ordenats, amb un fons que suggereix un lloc de desplegament remot."
coverCaption: ""
ref: ["/articles/field-deployable-power-and-environmental-resilience", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/articles/field-it-tidbits-beyond-the-mini-datacenter", "/guides/budget-friendly-10g-pfsense-build-hp-t740", "/articles/understanding-raid_-types-and-their-uses-in-data-storage"]
---

**L'edge computing desplegable al camp agrupa les funcions d'un bastidor en una caixa que pots transportar.** És útil en tasques de resposta a desastres, llocs d'enquesta remots, esdeveniments temporals, vaixells, centres de comandament mòbils o un laboratori domèstic que vols moure. *La disciplina bàsica és sempre la mateixa: tria primer maquinari preparat per suportar el transport i la calor, i després prioritza el rendiment.*

Aquesta és **la primera part d'una sèrie de quatre** sobre servidors compactes i equips de xarxa de desplegament ràpid. Aquesta part tracta la caixa, el càlcul, la distribució, el cablejat i la refrigeració. [La segona part](/articles/field-deployable-power-and-environmental-resilience/) tracta l'alimentació i la resiliència ambiental. [La tercera part](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) tracta els enllaços ascendents i la seguretat de les dades. [La quarta part](/articles/field-it-tidbits-beyond-the-mini-datacenter/) recull els consells breus de la resta de la sèrie.

______

## Què vol dir «desplegable al camp»

Un sistema de camp ha de suportar tres condicions que un servidor de bastidor en una sala climatitzada no troba: **transport repetit, una font d'alimentació desconeguda i absència de recanvis al lloc.**

- **Transport** vol dir vibracions, cops i caigudes, no un enviament acurat.
- **Rapidesa de desplegament** vol dir passar de la caixa a estar operatiu en minuts, no en hores.
- **Autosuficiència** vol dir portar la teva pròpia alimentació, refrigeració i xarxa, perquè sovint el lloc no en té.

*Cada opció d'aquesta sèrie es valora segons aquestes tres limitacions. Una peça no és adequada si és més barata, més ràpida o més capaç però falla en qualsevol d'elles.*

## Tria la carcassa

La carcassa no és una peça que s'afegeix al final. És la primera decisió, ja que limita tota la resta: quant equip hi cap, com suporta el viatge i amb quina rapidesa es pot configurar.

| Tipus de carcassa | Més adient per a | Compromís |
|---|---|---|
| **Maleta de transport resistent (Pelican, SKB, Seahorse)** | Viatges freqüents, equipatge facturat, manipulació brusca | Més pesada i cara que un bastidor senzill |
| **Bastidor amb amortiment de xocs** | Equips que continuen muntats al bastidor entre desplegaments | Ocupa més espai que una caixa amb escuma retallada a mida |
| **Caixa de transport amb rodes** | Desplaçaments locals freqüents, esdeveniments i desplegaments AV | Poca protecció contra l'aigua i la pols |
| **Carcassa mural resistent a la intempèrie (NEMA/IP)** | Llocs remots fixos a l'aire lliure sense vigilància | No està dissenyada per aixecar-la i transportar-la sovint |

**[Pelican](https://www.pelicancase.com/) i marques similars de maletes rígides** fabriquen caixes per a equips que es llancen al remolc d'un camió o es facturen com a equipatge. Busca una carcassa amb **marc de bastidor o rails amortidors** integrats en comptes d'escuma solta. L'escuma es degrada i l'equip es mou amb els anys d'ús.

*Una caixa de transport AV no és igual que una maleta resistent per a electrònica.* Les caixes AV protegeixen dels cops en un recinte controlat. Les carcasses resistents afegeixen juntes i vàlvules d'equilibri de pressió per als canvis d'altitud i el clima. Tria la resistent si el kit surt de carreteres pavimentades.

## Safata de servidor o ordinadors compactes independents

Dues filosofies dominen les configuracions edge compactes. Tria la correcta d'entrada per evitar refer el muntatge més tard.

- La **distribució amb safata de bastidor** munta servidors estàndard curts d'1U o 2U sobre rails amortidors dins la caixa. És fàcil d'ampliar si hi afegeixes capacitat de càlcul i es manté amb eines normals de bastidor.
- La **distribució amb mini PC independents** retalla l'escuma d'una maleta per allotjar diversos ordinadors petits sense ventilador o thin clients connectats entre si. Redueix pes i volum per a una càrrega coneguda i fixa, però no s'amplia bé.

*Tria la safata si la missió creixerà. Tria el clúster de mini PC si la missió és petita i fixa.* Barrejar les dues opcions dins la mateixa maleta sol deixar una organització deficient.

{{< figure src="rack-sled-vs-mini-pc-case-layout.webp" alt="Diagrama comparatiu: a l'esquerra, una maleta amb safata de bastidor amortida; a la dreta, una maleta amb escuma retallada per a diversos mini PC petits sense ventilador" >}}

## Maquinari de càlcul adequat per a la tasca

El maquinari per a configuracions edge compactes no és el mateix que un servidor de bastidor de col·locació. **El volum, el consum elèctric i la calor generada importen més que el nombre brut de nuclis.**

- Un **thin client** reutilitzat com a tallafoc o host d'hipervisor lleuger, com el [HP t740](https://amzn.to/3Td6xJE) de la nostra [guia econòmica de muntatge pfSense 10G](/guides/budget-friendly-10g-pfsense-build-hp-t740/), consumeix 50 watts o menys i ocupa aproximadament un litre.
- Un **aparell tallafoc mini PC sense ventilador**, com el [Protectli Vault](https://www.protectli.com/), renuncia a l'ampliació a canvi d'una carcassa tancada resistent a la pols i sense peces mòbils que es puguin espatllar.
- Un **servidor de format petit** (Dell OptiPlex Micro, Lenovo ThinkCentre Tiny o similar) ofereix més marge per a RAM i emmagatzematge que un thin client i continua cabent en una maleta de transport.
- Un **clúster d'ordinadors d'una sola placa** (Raspberry Pi 4/5 o similar) redueix pes i consum per a càrregues sense dependència d'x86.

*Els dissenys sense ventilador són més fiables en aquest context, perquè un ventilador giratori sol ser la primera peça que falla després de sacsejar-se durant dues-centes milles dins un camió.* Cada peça mòbil que elimines evita una fallada que no pots reparar al camp.

## Equips de xarxa dins la mateixa maleta

Els equips de xarxa viatgen a la mateixa maleta i reben els mateixos cops. Aplica als commutadors i punts d'accés els mateixos criteris: sense ventilador i baix consum.

- Un **commutador gestionable compacte** amb PoE alimenta punts d'accés i càmeres des d'un únic enllaç ascendent i redueix els carregadors dins la maleta.
- Un **punt d'accés reforçat o per a exteriors** suporta millor els canvis de temperatura que el Wi-Fi de consum dissenyat per a una sala d'estar.
- Un **tallafoc de maquinari**, com la configuració t740 anterior o un [Firewalla](https://amzn.to/3DG4WmU), estableix una frontera de polítiques entre la xarxa de camp i l'enllaç ascendent utilitzat. Aquí és més important que a casa perquè sovint no és de confiança.

## Gestió de cables per empaquetar-los sovint

Els cables d'una maleta de camp fallen de manera diferent dels d'una sala de servidors. A cada desplegament s'enrotllen, es desenrotllen, s'aixafen i s'empaqueten sota altres equips.

- **Fes servir cables etiquetats i amb codi de colors** per a cada connexió, perquè després del tercer viatge no recordaràs quin port anava a on.
- **Enrotlla els cables amb corretges de velcro, no amb brides**, per tornar-los a col·locar igual cada vegada sense tallar i substituir les brides.
- **Deixa llaços de cable dins la maleta**, sense tensar-los. La flexió repetida carregarà la funda del cable en comptes del connector.
- **Utilitza connectors amb pestell sempre que la norma ho permeti**, com ara protectors RJ45 amb bloqueig o alimentació amb terminals de cargol. Les vibracions afluixen els endolls normals amb el temps.

*Una maleta amb cables ordenats es configura en minuts. Una maleta amb cables embolicats exigeix una sessió de diagnòstic abans que comenci la missió.*

## Refrigeració dins una maleta tancada o mig tancada

Una caixa de transport tancada reté la calor. **Un flux d'aire adequat per a una prestatgeria de bastidor oberta pot sobreescalfar el mateix maquinari quan la tapa de la caixa és tancada.**

| Mètode de refrigeració | Quan s'ha d'utilitzar |
|---|---|
| **Dissipador passiu i càlcul sense ventilador** | Configuracions de baixa potència (thin clients, SBC) amb calor inferior al límit de dissipació passiva de la carcassa |
| **Ventiladors d'entrada i sortida muntats a la caixa** | Configuracions de més potència quan la refrigeració passiva no arriba i la caixa té reixetes tancables |
| **Safata de bastidor ventilada amb laterals oberts** | Llocs on la caixa queda oberta mentre funciona i la pols no és un problema important |
| **Maleta tancada amb circuit intern i reixetes filtrades** | Entorns polsosos o sorrencs que exigeixen filtrar l'aire abans que arribi als equips |

*Prova la maleta completament plena a la temperatura ambient màxima prevista abans d'anar a una instal·lació real.* Una configuració fresca sobre una taula d'oficina amb aire condicionat pot reduir el rendiment o apagar-se a 38 °C dins una maleta tancada sota el sol directe.

## Emmagatzematge per a càlcul de camp

L'emmagatzematge suporta els mateixos cops que la resta de l'equip, però també conté les dades necessàries per a la missió. Mereix una decisió pròpia.

| Tipus d'emmagatzematge | Més adient per a | Compromís |
|---|---|---|
| **SSD NVMe** | La majoria de configuracions de camp, millor resistència als cops i a les vibracions | Més car per terabyte que un disc giratori |
| **SSD SATA** | Configuracions econòmiques que necessiten fiabilitat d'estat sòlid | Més lent que NVMe, però molt més robust que un disc dur |
| **Disc dur giratori** | Emmagatzematge massiu quan la maleta queda fixa un cop desplegada | Els capçals de lectura i escriptura fallen amb vibracions, la pitjor opció per al transport |
| **SSD industrial o d'alta resistència d'escriptura** | Registres o bases de dades amb escriptures contínues | Més car per gigabyte que els SSD de consum |

*Un disc dur giratori no té lloc dins una maleta que es carrega, es condueix o s'envia.* L'emmagatzematge d'estat sòlid no té peces mòbils que fallin amb un cop. És l'opció habitual per a tot el que surt d'una sala de bastidors.

**Duplica els discs en mirall si la missió no tolera perdre dades per la fallada d'un sol disc.** Un mirall senzill de dos discs sobreviu a una fallada sense maquinari especial. La nostra [guia dels tipus RAID i els seus usos](/articles/understanding-raid_-types-and-their-uses-in-data-storage/) explica els compromisos entre mirall, striping i paritat amb més detall del que necessita habitualment un muntatge de camp. Per a una comparació més àmplia de tipus de disc i còpies al núvol, consulta també [solucions d'emmagatzematge: HDD, SSD i núvol](/articles/data-storage-solutions_-understanding-hdds,-ssds,-and-cloud-options/).

*La redundància dins la maleta no és una còpia de seguretat.* Un parell en mirall protegeix contra la fallada d'un disc. No serveix si tota la maleta es perd, es roba o es destrueix. Combina la redundància local amb les còpies fora del lloc descrites més endavant en aquesta sèrie.

## Gestió remota i accés fora de banda

**Tornar a un lloc de camp perquè un ordinador sense pantalla necessita un teclat contradiu l'objectiu d'un disseny de desplegament ràpid.** Prepara l'accés a la consola del maquinari encara que el sistema operatiu no arrenqui.

- **IPMI o un controlador de gestió de placa base (BMC)**, integrat en moltes plaques de servidor, ofereix control d'alimentació, redirecció de consola i dades dels sensors per xarxa, independentment del sistema operatiu amfitrió.
- **[PiKVM](https://www.pikvm.org/) i dispositius IP-KVM de codi obert similars** afegeixen accés fora de banda a equips sense BMC integrat, com un thin client o mini PC. Capturen la sortida HDMI i emulen un teclat i un ratolí USB.
- **Posa la gestió fora de banda en un segment de xarxa aïllat propi**, mai a la mateixa VLAN que el trànsit de producció. Un BMC amb contrasenya predeterminada és una via d'atac coneguda cap a maquinari protegit altrament.

*L'accés fora de banda marca la diferència entre una reparació remota de cinc minuts i una tornada al lloc el mateix dia.* Ometre'l estalvia una mica en maquinari, però el primer reinici forçat des de diversos estats de distància costa molt més.

## Compatibilitat internacional de l'alimentació i els connectors

Una configuració provada i empaquetada en un país no sempre es connecta bé en un altre. **Les diferències de tensió, freqüència i forma de l'endoll poden deixar inutilitzable una maleta en arribar.**

| Regió | Tensió nominal | Tipus d'endoll habituals |
|---|---|---|
| Amèrica del Nord | 120V, 60Hz | Tipus A/B (NEMA) |
| La majoria d'Europa | 220 a 240V, 50Hz | Tipus C/E/F (Europlug, Schuko) |
| Regne Unit i Irlanda | 220 a 240V, 50Hz | Tipus G |
| Austràlia i Nova Zelanda | 220 a 240V, 50Hz | Tipus I |

**La referència de [Wikipedia sobre endolls i preses de corrent altern](https://en.wikipedia.org/wiki/AC_power_plugs_and_sockets) cataloga tots els estàndards regionals** i convé consultar-la abans d'un desplegament internacional.

- **Tria fonts d'alimentació amb entrada universal (100 a 240V, 50/60Hz)** quan sigui possible, així només canvia l'adaptador d'endoll entre regions.
- **Porta un petit joc d'adaptadors adequats per a la destinació** i prova'ls amb els adaptadors de corrent reals del kit abans de sortir, perquè no tots encaixen físicament amb tots els transformadors.
- **No donis per fet que un transformador reductor no cal.** Un dispositiu només per a 120V pot patir danys permanents en un circuit de 230V si només hi poses un adaptador d'endoll.

*Comprova la compatibilitat de tensió de cada dispositiu de la maleta, no només de l'ordinador principal.* Un SAI d'entrada universal no resol el problema d'un accessori només per a 120V.

## Llista de control dels components

Abans de tancar la maleta per al primer desplegament, comprova cada punt:

- [ ] La carcassa correspon al mètode real de transport (equipatge facturat, caixa del camió, motxilla)
- [ ] El maquinari de càlcul no té ventiladors o disposa de ventiladors filtrats reparables
- [ ] Els equips de xarxa corresponen a la classe de potència i robustesa del maquinari de càlcul
- [ ] Tots els cables estan etiquetats, diferenciats per color i subjectats amb fixacions reutilitzables
- [ ] La refrigeració s'ha provat a la temperatura ambient màxima amb la maleta tancada
- [ ] La maleta conté cables de recanvi i una peça petita (SFP, cable de connexió, alimentador)

## Passos següents

El maquinari i les carcasses resolen només la meitat del problema. L'altra meitat és mantenir-lo alimentat i en funcionament un cop surt de la maleta. Continua amb [la segona part: alimentació i resiliència ambiental](/articles/field-deployable-power-and-environmental-resilience/) per dimensionar els SAI, veure opcions d'alimentació CC i revisar els graus ambientals IP/NEMA.

Per a la connectivitat i la seguretat de la mateixa configuració, consulta [la tercera part: connectivitat i seguretat de dades per a nodes edge](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/). Per als detalls petits que és fàcil oblidar, llegeix [la quarta part: consells breus de TI de camp](/articles/field-it-tidbits-beyond-the-mini-datacenter/).

Si vols un punt de partida concret i econòmic per a les capes de càlcul i tallafoc, la nostra [guia econòmica de muntatge pfSense 10G amb HP t740](/guides/budget-friendly-10g-pfsense-build-hp-t740/) presenta un exemple real.
