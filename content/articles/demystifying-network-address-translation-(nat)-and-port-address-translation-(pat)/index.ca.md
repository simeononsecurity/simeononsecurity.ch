---
title: "NAT i PAT: guia essencial de comunicació en xarxa"
date: 2024-02-13
lastmod: 2026-11-12
toc: true
draft: false
description: "Entén NAT i PAT per facilitar les comunicacions digitals."
genre: ["Fonaments de xarxes", "Ciberseguretat", "Infraestructura de TI", "Guies tecnològiques", "Gestió de xarxes", "Protocols d'Internet", "Tecnologies de comunicació", "Administració de sistemes", "Enginyeria de xarxes", "Xarxes digitals"]
tags: ["TraduccióAdrecesDeXarxa", "TraduccióAdrecesDePort", "GestióIP", "Ciberseguretat", "ComunicacióDeXarxa", "SolucionsTecnològiques", "ImplementacióIPv6", "NATvsPAT", "ReptesEquilibriDeCàrrega", "XarxesSegures", "XarxesInformàtiques", "TecnologiesEmergentsPAT", "SolucióEsgotamentIP", "TipusNAT", "AvantatgesPAT", "XarxesEficients", "EvolucióProtocolInternet", "OptimitzacióXarxesDigitals", "AdministracióXarxa", "FuturXarxes", "EntendreNATiPAT", "ConfiguracióNAT", "ImplementacióPAT", "SeguretatNAT", "AssignacióIP", "TecnologiaDeXarxa", "IPv4iIPv6", "ReptesNAT", "ResolucióProblemesNAT/PAT", "SolucionsConnectivitatXarxa"]
cover: "/img/cover/demystifying-network-address-translation-(nat)-and-port-address-translation-(pat).webp"
coverAlt: "Il·lustració de la guia essencial de comunicació en xarxa sobre NAT i PAT."
---

Desmitificació de la traducció d'adreces de xarxa (NAT) i la traducció d'adreces de port (PAT)
===============================================================================================

La traducció d'adreces de xarxa (NAT) i la traducció d'adreces de port (PAT) són tecnologies de xarxa essencials per gestionar adreces IP i permetre la comunicació entre dispositius de xarxes diferents. NAT permet que diversos dispositius d'una xarxa local comparteixin una única adreça IP pública, mentre que PAT amplia aquesta funció traduint també els números de port. Aquest article explica què són NAT i PAT, per a què serveixen, quins tipus hi ha i quins avantatges i inconvenients presenten. També descriu PAT, els seus beneficis i el seu funcionament, compara NAT amb PAT i n'explica els casos d'ús. A més, tracta problemes habituals com l'esgotament d'adreces, els riscos de seguretat i l'equilibri de càrrega, juntament amb possibles solucions. Finalment, repassa tendències futures, com ara l'impacte d'IPv6 i les tecnologies emergents en PAT.

### Punts clau

* NAT i PAT gestionen adreces IP i permeten la comunicació entre dispositius de xarxes diferents.
* NAT permet que diversos dispositius d'una xarxa local comparteixin una adreça IP pública.
* PAT amplia NAT traduint també els números de port.
* Els casos d'ús de NAT i PAT depenen dels requisits de la xarxa.
* Entre els reptes habituals hi ha l'esgotament d'adreces, la seguretat i l'equilibri de càrrega.

Introducció a la traducció d'adreces de xarxa (NAT)
---------------------------------------------------

### Definició i objectiu de NAT

{{< figure src="nat-pat-private-public-ip-translation.webp" alt="Diagrama que mostra com la traducció d'adreces de xarxa converteix les adreces IP privades d'una xarxa local en una única adreça IP pública compartida per comunicar-se per Internet" >}}

La traducció d'adreces de xarxa (NAT) és una tecnologia fonamental que converteix adreces IP privades en adreces IP públiques i a l'inrevés. El seu objectiu és permetre la [comunicació entre dispositius de xarxes diferents](https://www.blamethe.network/posts/demystifying-vasi/) que utilitzen esquemes d'adreçament incompatibles. NAT permet que diversos dispositius d'una xarxa privada comparteixin una adreça IP pública, cosa que conserva el conjunt limitat d'adreces públiques disponibles. També ofereix un cert grau de seguretat perquè amaga les adreces IP internes a les xarxes externes.

### Tipus de NAT

Els tipus de traducció d'adreces de xarxa (NAT) són importants per a la [seguretat i la connectivitat de xarxa](https://youtube.com/watch?v=QBqPzHEDzvo&pp=ygUOI2tva2FudGxpcG9wdGk%3D). Conèixer-los ajuda els professionals de la ciberseguretat a gestionar i protegir la infraestructura de xarxa. Aquests són alguns tipus habituals de NAT:

### Avantatges i inconvenients de NAT

Els professionals de la ciberseguretat han d'entendre els avantatges i els inconvenients de NAT per prendre decisions informades sobre la seguretat de xarxa. NAT ofereix diversos beneficis:

* **Estalvi d'adreces IP**: diversos dispositius poden compartir una adreça IP pública, cosa que ajuda a conservar les adreces IPv4, que són limitades.
* **Privacitat i seguretat**: en amagar les adreces IP internes dels dispositius darrere d'una adreça IP pública, NAT afegeix una capa de privacitat i seguretat i dificulta que els atacants apuntin directament a cada dispositiu.
* **Gestió de xarxa simplificada**: NAT redueix la necessitat d'adreces IP públiques i facilita la configuració d'adreces IP privades.

Tot i això, NAT també té limitacions i inconvenients:

* **Connectivitat entre iguals limitada**: NAT pot dificultar la connectivitat entre iguals, perquè establir connexions directes entre dispositius pot requerir configuració addicional o tècniques com Universal Plug and Play (UPnP).
* **Impacte en alguns protocols de xarxa**: protocols com IPsec i FTP poden tenir problemes amb NAT a causa de la traducció d'adreces IP i ports.
* **Més complexitat per als administradors de xarxa**: implementar i gestionar NAT afegeix complexitat, especialment en xarxes grans.

Els professionals de la ciberseguretat han de valorar amb cura aquests avantatges i inconvenients quan implementen NAT a la seva infraestructura de xarxa.

Comprendre la traducció d'adreces de port (PAT)
------------------------------------------------

{{< figure src="advantages-and-disadvantages-of-nat.webp" alt="Mapa il·lustrat amb rutes sinuoses i indicadors de localització que connecten servidors, monitors i un núvol, amb una figura desconcertada entre els camins per mostrar l'encaminament d'adreces NAT." >}}

### Visió general de PAT

La traducció d'adreces de port (PAT) és un component important de NAT que permet que diversos dispositius d'una xarxa privada comparteixin una única adreça IP pública. PAT opera a la capa de transport del model OSI i s'utilitza sovint quan hi ha escassetat d'adreces IP públiques.

PAT assigna números de port únics a cada sessió de comunicació entre una adreça IP privada i una de pública. Així, l'encaminador pot saber a quin dispositiu pertanyen els paquets entrants i retornar les respostes al dispositiu correcte.

Punts clau sobre PAT:

* PAT conserva adreces IP públiques multiplexant diverses adreces IP privades en una única adreça IP pública.
* Utilitza números de port per distingir les diferents sessions de comunicació.
* PAT es pot implementar amb assignació estàtica o dinàmica de ports.
* PAT aporta un cert grau de seguretat en amagar les adreces IP privades dels dispositius darrere de l'adreça IP pública.

En resum, PAT és un mecanisme essencial de NAT que permet aprofitar eficientment les adreces IP públiques i facilita la comunicació entre els dispositius d'una xarxa privada i Internet.

### Com funciona PAT

[La traducció d'adreces de port (PAT)](https://youtube.com/watch?v=l5wuJFoeVDQ&pp=ygULI3VubmF0XzQ2NDY%3D) és una tècnica de NAT que associa diverses adreces IP privades amb una sola adreça IP pública. Permet que diversos dispositius d'una xarxa privada comparteixin aquesta adreça i ajuda a conservar adreces IPv4. PAT assigna números de port únics als dispositius de la xarxa privada perquè l'encaminador pugui identificar a quin dispositiu pertany un paquet concret. Quan arriba un paquet d'Internet, l'encaminador el reenvia al dispositiu adequat segons el número de port.

### Beneficis de PAT

[La traducció d'adreces de port (PAT)](https://provost.ucsd.edu/12all/lt.php?c=249&m=234&nl=17&s=bad97c655476f96a390a72c05a742011&lid=3379&l=-http--62018811nov98.%D0%B0%D0%BB%D1%8C%D0%B4%D0%BE%D0%B3%D0%B0.%D1%80%D1%84) ofereix diversos beneficis per a la comunicació de xarxa.

Comparació entre NAT i PAT
--------------------------

{{< figure src="benefits-of-pat.webp" alt="Imatge dividida que contrasta una esfera de xarxa lluminosa i ordenada, amb nodes connectats a l'esquerra, amb un conjunt caòtic de quadrats de colors a la dreta." >}}

### Diferències entre NAT i PAT

NAT i PAT són dues tècniques de xarxes informàtiques que permeten traduir adreces IP. NAT tradueix les adreces IP a la capa de xarxa, mentre que PAT opera a la capa de transport. Aquesta diferència fonamental provoca distincions en les funcions i els casos d'ús.

**Diferències principals entre NAT i PAT:**

1. **Abast de la traducció**: NAT tradueix adreces IP en una relació d'un a un, PAT tradueix adreces IP i números de port en una relació de molts a un.
2. **Estalvi d'adreces**: NAT conserva adreces IP reutilitzant-les per a diverses adreces IP privades, mentre que PAT conserva adreces IP i números de port.
3. **Multiplexació de ports**: PAT assigna números de port diferents a diverses adreces IP privades i les associa amb una sola adreça IP pública.
4. **Seguiment de connexions**: NAT no conserva informació de connexió, PAT sí que la conserva per encaminar correctament els paquets entrants.

**Casos d'ús de NAT:**

* Proporcionar accés a Internet a diversos dispositius d'una xarxa privada.
* Permetre la comunicació entre xarxes privades i públiques.
* Aplicar mesures de seguretat de xarxa amagant les adreces IP internes.

**Casos d'ús de PAT:**

* Facilitar l'accés a Internet de diversos dispositius d'una xarxa privada amb una sola adreça IP pública.
* Distribuir el trànsit entre diversos servidors.
* Habilitar el reenviament de ports per a serveis concrets.

Aquestes diferències i aquests usos mostren per què és important entendre la distinció entre NAT i PAT quan es dissenyen i gestionen arquitectures de xarxa.

### Casos d'ús de NAT

NAT té diversos usos en ciberseguretat. Un ús important és protegir els recursos de la xarxa interna contra l'accés no autoritzat. En traduir les adreces IP privades en públiques, [NAT actua com una barrera](https://www.thesamba.com/vw/bin/banner_click.php?redirect=1093825nov22.%D0%BC%D0%BE%D0%B6%D0%B0%D0%B9%D1%81%D0%BA-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B5%D0%BC%D0%BE%D0%BD%D1%82-%D1%86%D0%B5%D0%BD%D1%82%D1%80.%D1%80%D1%84) entre la xarxa interna i l'externa, i impedeix la comunicació directa i possibles atacs. Un altre ús és conservar adreces IP públiques. Com que augmenta el nombre de dispositius connectats a Internet, la disponibilitat d'adreces públiques és limitada. NAT permet que diversos dispositius comparteixin una adreça IP pública i redueix la demanda. També es pot utilitzar per equilibrar la càrrega: distribueix el trànsit entrant entre diversos servidors interns, cosa que ajuda a optimitzar els recursos i millorar el rendiment de la xarxa.

### Casos d'ús de PAT

És important que els professionals de la ciberseguretat coneguin els usos de PAT. S'utilitza sovint quan diversos dispositius d'una xarxa privada necessiten accedir a Internet mitjançant una sola adreça IP pública. Alguns usos principals són:

1. **Conservar adreces IP**: PAT associa diverses adreces IP privades amb una adreça IP pública. És especialment útil quan n'hi ha poques de públiques.
2. **Millorar la seguretat**: PAT amaga les adreces IP privades dels dispositius de la xarxa interna. Això ajuda a protegir-los d'atacs i dificulta que actors maliciosos apuntin a dispositius concrets.
3. **Simplificar la gestió de xarxa**: PAT redueix la necessitat de configuracions complexes i permet gestionar fàcilment l'accés a Internet de diversos dispositius mitjançant una sola adreça IP pública.
4. **Permetre l'equilibri de càrrega**: PAT pot distribuir el trànsit entrant entre diversos dispositius interns, equilibrar la càrrega i garantir un ús eficient dels recursos.

Aquests casos fan de PAT una eina valuosa de NAT, útil per conservar adreces IP, millorar la seguretat i la gestió de xarxa i equilibrar la càrrega.

Reptes i solucions habituals de NAT i PAT
-----------------------------------------

{{< figure src="use-cases-for-pat.webp" alt="Dos homes de dibuixos animats, desconcertats, munten peces de trencaclosques taronges en un camp al costat d'una pila de commutadors de xarxa, uns globus de pensament comparen dispositius NAT i PAT." >}}

### Esgotament d'adreces

L'esgotament d'adreces és un repte important per a NAT i PAT. La demanda d'adreces IP creix ràpidament, mentre que el conjunt d'adreces IPv4 disponibles s'esgota. Això es deu principalment al nombre limitat d'adreces IPv4 i a l'augment de dispositius connectats a Internet.

S'han implementat diverses solucions:

* **IPv6**: adoptar IPv6 proporciona un espai d'adreces molt més gran i gairebé il·limitat. IPv6 utilitza adreces de 128 bits en lloc dels 32 bits d'IPv4, fet que amplia molt el conjunt disponible.
* **Traducció d'adreces de xarxa amb IPv6 (NAT64)**: NAT64 permet que els dispositius només IPv6 es comuniquin amb dispositius només IPv4 traduint paquets IPv6 a IPv4 i a l'inrevés. Això facilita la coexistència de xarxes IPv4 i IPv6 i ajuda a reduir l'esgotament d'adreces.

Aquestes solucions són prometedores, però la seva adopció i implementació generalitzades encara presenten reptes. Les organitzacions han de planificar i executar acuradament la transició a IPv6 per garantir la compatibilitat i la seguretat.

En resum, l'esgotament d'adreces és un problema urgent per a NAT i PAT. Adoptar IPv6 i implementar NAT64 són passos clau per afrontar-lo i garantir el creixement i l'estabilitat continuats d'Internet.

### Qüestions de seguretat

La seguretat és una preocupació important en NAT i PAT. Els professionals de la ciberseguretat han d'entendre les vulnerabilitats i els riscos potencials associats a aquestes tecnologies. Un risc principal és l'accés no autoritzat als recursos interns de la xarxa. **Marcus Dods**, un [investigador de ciberseguretat reconegut](https://www.thesamba.com/vw/bin/banner_click.php?redirect=a1xe8bnr43.%D0%B2%D0%B0%D1%88-%D1%81%D0%B0%D0%BD%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA-%D0%B4%D0%B7%D1%80.%D1%80%D1%84), ha destacat la importància d'implementar mesures de seguretat sòlides per impedir l'accés no autoritzat.

### Equilibri de càrrega

L'equilibri de càrrega és un aspecte important de la [traducció d'adreces de xarxa](https://labs.iximiuz.com/tutorials/container-networking-from-scratch) (NAT) i de la traducció d'adreces de port (PAT). Distribueix el trànsit de xarxa de manera eficient entre diversos servidors o dispositius. Això ajuda a optimitzar els recursos, millorar el rendiment i augmentar la fiabilitat de la infraestructura de xarxa.

Tendències futures de NAT i PAT
------------------------------

{{< figure src="load-balancing.webp" alt="Escena isomètrica de monitors, portàtils, servidors i encaminadors Wi-Fi connectats amb línies roses que distribueixen el trànsit entre dispositius i mostren l'equilibri de connexions." >}}

### IPv6 i NAT

A mesura que el món passa a IPv6, el paper de NAT és encara més important per gestionar la [disponibilitat limitada d'adreces IP](https://www.blackhillsinfosec.com/unpacking-the-packet/). IPv6, la següent generació del Protocol d'Internet, ofereix un espai d'adreces molt més gran que IPv4. Tot i això, la seva adopció ha estat relativament lenta i moltes organitzacions encara depenen d'IPv4. NAT ajuda a connectar xarxes IPv4 i IPv6 perquè els dispositius que utilitzen IPv6 es puguin comunicar amb els que utilitzen IPv4.

### Tecnologies emergents en PAT

És important que els professionals de la ciberseguretat estiguin al dia de les tecnologies emergents en PAT. Aquests avenços ajuden a millorar la seguretat i el rendiment de la xarxa. Dues tecnologies destacades són **IPv6** i les **xarxes definides per programari (SDN)**.

**IPv6** és la següent generació de l'esquema d'adreçament del Protocol d'Internet (IP). Proporciona un espai d'adreces molt més gran que IPv4, necessari per al nombre creixent de dispositius connectats a Internet. Amb IPv6, PAT es pot implementar de manera més eficient, amb més escalabilitat i una gestió de xarxa millorada.

Les **xarxes definides per programari (SDN)** són una altra tecnologia emergent que complementa PAT. SDN separa el pla de control del pla de dades i permet gestionar i programar la xarxa de manera centralitzada. Aquesta tecnologia simplifica el desplegament i la configuració de PAT, i en facilita l'adaptació a requisits de xarxa canviants.

En resum, IPv6 i SDN estan transformant el camp de PAT. Ofereixen més escalabilitat, una gestió de xarxa millor i flexibilitat per afrontar els reptes dels entorns de xarxa moderns.

En el món canviant de les xarxes, NAT (Network Address Translation) i PAT (Port Address Translation) són essencials per garantir una comunicació eficient entre dispositius. A mesura que avança la tecnologia, convé seguir les tendències futures per optimitzar el rendiment i la seguretat de la xarxa. Les guies de SimeonOnSecurity ofereixen informació detallada i tutorials pràctics sobre control de versions, administració de sistemes, ciberseguretat, [gestió de xarxes](https://simeononsecurity.com/guides/) i desenvolupament de programari. Volem ajudar-te a adquirir coneixements i millorar les teves habilitats. Visita el nostre lloc web per consultar les guies i mantenir-te al dia en un entorn tecnològic que canvia ràpidament.

Conclusió
---------

La traducció d'adreces de xarxa (NAT) i la traducció d'adreces de port (PAT) tenen un paper essencial en les xarxes modernes. NAT permet que diversos dispositius comparteixin una adreça IP pública i aprofitin millor les adreces IPv4 limitades. També afegeix una capa de seguretat perquè amaga les adreces IP internes a les xarxes externes. Tanmateix, NAT presenta reptes com l'esgotament d'adreces i possibles problemes de seguretat. PAT, una variant de NAT, afegeix una capa de traducció que utilitza números de port per distingir diversos dispositius interns. Això aporta més escalabilitat i flexibilitat a les configuracions de xarxa. S'espera que **IPv6** resolgui el problema de l'esgotament d'adreces i redueixi la necessitat de NAT, mentre que les tecnologies emergents en PAT busquen millorar encara més el rendiment i la seguretat de la xarxa. A mesura que les xarxes evolucionin, els administradors i professionals del sector hauran d'entendre NAT i PAT. _Desmitificació de la traducció d'adreces de xarxa (NAT) i la traducció d'adreces de port (PAT)_ ofereix una visió completa d'aquests conceptes importants i ajuda a entendre la complexitat de les xarxes modernes.

Preguntes freqüents
-------------------

### Què és la traducció d'adreces de xarxa (NAT)?

La traducció d'adreces de xarxa (NAT) és una tècnica de xarxes informàtiques que modifica la informació d'adreçament de xarxa a la capçalera IP dels paquets mentre travessen un dispositiu que encamina el trànsit.

### Quin és l'objectiu de NAT?

NAT permet reutilitzar adreces IP, ja que el nombre d'adreces IPv4 disponibles és limitat. Així, diversos dispositius d'una xarxa privada poden compartir una sola adreça IP pública.

### Quins tipus de NAT hi ha?

Hi ha tres tipus principals: NAT estàtica, NAT dinàmica i traducció d'adreces de port (PAT). NAT estàtica associa una adreça IP privada amb una de pública. NAT dinàmica associa diverses adreces IP privades amb un conjunt d'adreces públiques. PAT associa diverses adreces IP privades amb una sola adreça pública mitjançant números de port diferents.

### Quins són els avantatges de NAT?

NAT permet conservar adreces IP públiques, millora la seguretat de xarxa amagant adreces IP internes i permet la coexistència de xarxes IPv4 i IPv6.

### Quins són els inconvenients de NAT?

Els inconvenients inclouen una possible reducció del rendiment pel procés de traducció, limitacions en la comunicació entre iguals i dificultats per allotjar serveis que necessiten connexions entrants directes.

### Què és la traducció d'adreces de port (PAT)?

La traducció d'adreces de port (PAT), també coneguda com a Network Address Port Translation (NAPT), és una variant de NAT que permet que diversos dispositius d'una xarxa privada comparteixin una sola adreça IP pública mitjançant números de port diferents per distingir-ne el trànsit.
