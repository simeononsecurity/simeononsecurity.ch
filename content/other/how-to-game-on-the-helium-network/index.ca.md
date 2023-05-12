---
title: "Gaming the Helium Network: Explotació de vulnerabilitats amb MiddleMan i Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Aprèn a jugar a la xarxa Helium explotant vulnerabilitats amb MiddleMan i Chirp Stack Packet Multiplexer, així com els riscos i les conseqüències de fer-ho".
tags: ["Xarxa d'heli","Prova de cobertura","MiddleMan","Multiplexador de paquets Chirp Stack","joc","explotar vulnerabilitats","Xarxa LoRaWAN","criptomoneda","cadena de blocs","xarxa descentralitzada","punts calents","falsificació","enganyar","activitat il·legal","penals","integritat de la xarxa","recompenses","actors maliciosos","seguretat de la xarxa","amfitrions legítims"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Una representació dibuixada d'un grup d'individus que exploten un globus d'heli amb una imatge d'una passarel·la LoRaWAN® i un MiddleMan o un multiplexador de paquets Chirp Stack al fons".
coverCaption: ""
---

**Exempció de responsabilitat**
És important tenir en compte que jugar a la xarxa Helium és una activitat il·legal i poc ètica que està fortament desaprovada per la comunitat Helium i la comunitat de criptomoneda i blockchain més àmplia. Jugar a la xarxa soscava la integritat de la xarxa i perjudica els amfitrions legítims que proporcionen una cobertura valuosa a la xarxa.

A més, tot i que l'ús de MiddleMan i Chirp Stack Packet Multiplexer per explotar vulnerabilitats a la xarxa Helium pot ser un motiu de preocupació, és important tenir en compte que Helium només pot solucionar aquests problemes mitjançant la introducció de passarel·les segures. Això requeriria la substitució de tots els punts d'accés a la xarxa, que és una empresa important i pot ser que no sigui factible. Com a resultat, la comunitat Helium ha de mantenir-se vigilant i proactiva per abordar els reptes que plantegen els jocs a la xarxa.

També val la pena assenyalar que l'equip d'Helium és conscient del problema des de fa temps i ha pres mesures per solucionar-lo, però calen més accions per resoldre el problema. La comunitat demana que es prenguin mesures reals per abordar aquestes vulnerabilitats i garantir que la xarxa pugui continuar escalant i creixent d'una manera segura i fiable.

En escriure aquest article, esperem conscienciar sobre el problema dels jocs a la xarxa Helium i l'ús de MiddleMan i Chirp Stack Packet Multiplexer per explotar les vulnerabilitats del sistema. Creiem que fent llum sobre aquest problema i aportant-hi més publicitat, la comunitat Helium i la comunitat de blockchain i criptomoneda més àmplia poden unir-se per abordar el problema i treballar cap a una xarxa més segura i fiable.

A més, destacant aquest problema, esperem animar l'equip d'Helium a prendre mesures més decisives per abordar les vulnerabilitats de la xarxa i a implementar mesures de seguretat més sòlides per prevenir els jocs en el futur. Creiem que és important que l'equip d'Helium sigui transparent sobre els seus esforços per abordar aquest problema i es comuniqui amb la comunitat sobre el seu progrés per solucionar aquestes vulnerabilitats.

Finalment, fent més publicitat a aquest tema, esperem fomentar una major conscienciació i educació sobre els riscos i les conseqüències dels jocs a la xarxa Helium. És important que els usuaris entenguin la importància del comportament ètic a la xarxa i el dany potencial que pot causar els jocs. Treballant junts per abordar aquests problemes, podem ajudar a garantir el creixement i l'èxit continus de la xarxa Helium.

En resum, jugar a la xarxa Helium no està aprovat per la comunitat ni per nosaltres, i animem els usuaris a actuar de manera ètica i legal quan participin a la xarxa. Tot i que hi ha vulnerabilitats a la xarxa que es poden explotar, és important mantenir-se vigilant i proactiu per abordar aquests problemes i treballar per aconseguir una xarxa més segura i fiable per a tots els usuaris.

# Com jugar a la xarxa d'heli amb MiddleMan i el multiplexador de paquets Chirp Stack
La xarxa Helium és una xarxa LoRaWAN® descentralitzada que compensa els que allotgen punts d'accés físics recompensant-los amb fitxes Helium o $HNT. Aquest sistema es coneix com a prova de cobertura (PoC). A mesura que la xarxa ha anat creixent i ha augmentat la consciència d'aquest projecte, hi ha hagut un nombre cada cop més gran de tramposos que estan explotant el protocol i els mecanismes de recompensa. En aquest article, parlarem de com jugar a la xarxa Helium mitjançant MiddleMan i Chirp Stack Packet Multiplexer.

## Comprendre el problema dels jocs de xarxa d'heli
La xarxa Helium es basa en la prova de cobertura per garantir que els punts d'accés ofereixen cobertura allà on es necessita. Tanmateix, aquest sistema és vulnerable als jocs, la falsificació, la pirateria i altres tipus de mal comportament que poden danyar la xarxa. El problema dels jocs a la xarxa Helium està costant als amfitrions legítims milers de $ HNT al mes. Helium, Inc, juntament amb DeWi, han pres mesures agressives a principis de 2022 per ajudar a eliminar aquest problema.

## Maquinari necessari
-[Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
-[Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
-[Raspberry Pi](https://amzn.to/3KjFCYp)
-[Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Ús de MiddleMan per jugar a la xarxa Helium
Una manera de jugar a la xarxa Helium és utilitzar MiddleMan. MiddleMan és una eina de programari que es pot utilitzar per crear un punt d'accés fals que sembla que ofereix cobertura en una ubicació específica. Mitjançant l'ús de MiddleMan, un usuari pot crear un punt d'accés fals que rebrà recompenses per oferir cobertura en una àrea concreta, tot i que el punt d'accés no es troba físicament en aquesta àrea.

Per utilitzar MiddleMan, un usuari ha d'instal·lar el programari i crear un punt d'accés fals. Aleshores, l'usuari pot configurar el punt d'accés per informar de la seva ubicació a la xarxa Helium mitjançant una eina de falsificació de GPS. La xarxa Helium creurà que el punt d'accés fals proporciona cobertura a la ubicació especificada i recompensarà l'usuari amb $HNT.

Hauríeu de configurar la vostra passarel·la lorawan per apuntar a aquest programari i manipular els valors perquè tots els PoC rebuts es considerin vàlids. L'ús del reenviador semtech és un dels diferents estàndards de la comunitat LoraWAN. Arreglar el problema de manipulació requeriria reinventar la roda i implementar el seu propi protocol des de zero. Coses com les sumes de control i el xifratge evitarien que això succeís. Però també dificultaria que els venedors amb diferents maquinari creïn punts d'accés. Per no parlar de que és un cas d'ús compatible per tenir un miner d'heli i diverses passarel·les Lora per millorar la cobertura. Tot i que això és més un problema a nivell empresarial.

 -[helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Ús del multiplexador de paquets Chirp Stack per jugar a la xarxa d'heli
Una altra manera de jugar a la xarxa Helium és utilitzant Chirp Stack Packet Multiplexer. Chirp Stack Packet Multiplexer és una eina que es pot utilitzar per crear un punt d'accés virtual que pot rebre paquets de diversos punts d'accés físics. Mitjançant l'ús del multiplexador de paquets Chirp Stack, un usuari pot crear un punt d'accés virtual que rep paquets de punts d'accés físics en diverses ubicacions, cosa que augmentarà les recompenses obtingudes.

Per utilitzar Chirp Stack Packet Multiplexer, un usuari ha d'instal·lar el programari i configurar-lo per rebre paquets de punts d'accés físics o passarel·les Lorawan en diverses ubicacions. L'hotspot rebrà els paquets i informarà de la seva ubicació a la xarxa Helium, que recompensarà l'usuari amb $HNT.

Això permet l'entrada de diversos reenviadors i diverses passarel·les de sortida. Hi ha casos d'ús legítims per a aquest programari a la comunitat LoraWAN, però utilitzar-lo en heli és una zona grisa en el millor dels casos. Depèn de com l'utilitzis i també de quina sigui la teva intenció.

La configuració d'aquest requereix alguns fitxers de configuració. Però es pot fer en 5 minuts o menys.
-[chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Riscos i conseqüències dels jocs a la xarxa Helium
Jugar a la xarxa Helium és una activitat arriscada i il·legal que pot tenir greus conseqüències. Helium, Inc, juntament amb DeWi, està treballant activament per detectar i prevenir els jocs a la xarxa, i els usuaris que siguin atrapats jugant a la xarxa seran penalitzats.

Les penalitzacions per jugar a la xarxa Helium poden incloure la pèrdua de l'accés a la xarxa, la prohibició permanent dels punts d'accés a la xarxa i la pèrdua de qualsevol $ HNT que s'hagi guanyat amb el joc. A més, jugar a la xarxa Helium soscava la integritat de la xarxa i perjudica els amfitrions legítims que proporcionen una cobertura valuosa a la xarxa.

## Conclusió
Tot i que la xarxa Helium ofereix oportunitats als amfitrions legítims de punts d'accés per obtenir recompenses mitjançant la prova de cobertura, també presenta un objectiu atractiu per als actors maliciosos que busquen jugar amb el sistema. L'ús de MiddleMan i Chirp Stack Packet Multiplexer, tot i que no està aprovat per Helium Inc. ni per la comunitat en general, és un exemple de com alguns actors dolents estan explotant les vulnerabilitats de la xarxa per obtenir beneficis a costa d'altres.

És important que la comunitat Helium continuï treballant junts per identificar i abordar els jocs a la xarxa, ja que amenacen la integritat del sistema i soscaven els esforços dels amfitrions legítims. Això pot incloure esforços per desenvolupar i implementar mesures de detecció i prevenció més sofisticades, així com augmentar la conscienciació i l'educació sobre els riscos i les conseqüències dels jocs a la xarxa.

En última instància, l'èxit de la xarxa Helium depèn de la voluntat de les seves parts interessades de treballar junts per construir un sistema segur, fiable i fiable que proporcioni valor real als seus usuaris. Si es manté vigilant i proactiu a l'hora d'abordar els reptes que plantegen els jocs, la comunitat pot ajudar a garantir que la xarxa Helium continuï creixent i evolucionant en una direcció positiva.