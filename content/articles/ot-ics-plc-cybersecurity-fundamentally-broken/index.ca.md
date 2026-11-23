---
title: "Per què la ciberseguretat OT, ICS i PLC continua fallant"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-22
description: "Analitza per què els controls de seguretat OT van endarrerits respecte del disseny heretat, les limitacions operatives i les vies reals d'atac."
tags: ["seguretat OT", "seguretat ICS", "seguretat PLC", "seguretat IoT", "ciberseguretat industrial", "seguretat SCADA", "NIST 800-82", "IEC 62443", "NERC CIP", "tecnologia operacional", "infraestructura crítica", "sensors analògics", "aïllament de xarxa", "sistemes heretats", "opinió sobre ciberseguretat", "sistemes de control industrial", "SCADA", "Stuxnet", "seguretat dels sistemes de control", "seguretat ciberfísica", "seguretat de la cadena de subministrament", "cadena de subministrament OT"]
cover: "/img/cover/ot-ics-plc-cybersecurity-fundamentally-broken.webp"
coverAlt: "Il·lustració que contrasta un PLC antic amb funcions analògiques i un controlador modern amb capacitats de ciberseguretat i interfícies digitals, sobre un fons fosc."
coverCaption: ""
---

He passat prou temps en entorns industrials per dir-ho clarament: **la majoria dels programes de ciberseguretat OT, ICS i PLC són teatre**. Generen documentació de compliment normatiu. No generen seguretat. La bretxa entre totes dues coses és el lloc on rep atacs la infraestructura crítica.

Això no és un atac a les persones que redacten estàndards. **NIST SP 800-82 Rev 3**, **IEC 62443** i **NERC CIP** són documents tècnicament sòlids. El problema no són les directrius. *El problema és a quins sistemes s'apliquen.*

## Els sistemes es van crear per funcionar, no per protegir-se

**Els PLC, els sistemes SCADA, els sistemes de control distribuït (DCS) i el maquinari IoT industrial heretat** es van dissenyar amb un únic propòsit: funcionar de manera fiable durant molt de temps. **La disponibilitat era l'únic objectiu de disseny que valia la pena discutir.** La confidencialitat, la integritat, l'autenticació i el registre d'activitat no eren requisits. Sovint, ni tan sols eren conceptes que es plantegessin quan es van dissenyar aquests sistemes.

NIST SP 800-82 Rev 3 (2023) ho admet amb franquesa. Descriu els entorns OT com a sistemes amb *«requisits singulars de rendiment, fiabilitat i seguretat»*, on *«la seguretat no pot interferir amb el funcionament del sistema»*. Torna-ho a llegir. **El principal document de directrius de seguretat per a la tecnologia operacional reconeix explícitament que la seguretat passa a segon terme.** No és un defecte del document. És una descripció fidel de l'entorn.

No pots aplicar control d'accés basat en rols a un PLC que desconeix els rols d'usuari. No pots actualitzar el microprogramari d'un equip si el fabricant ja no existeix. **Els protocols sèrie heretats, com ara Modbus RTU i Profibus DP, no ofereixen autenticació nativa.** Transmeten ordres i dades a qui les demani. No verifiquen qui fa la petició.

*Les directrius són sòlides. Sovint, els sistemes no les poden aplicar.* No és el mateix problema.

## Hi ha dues categories d'OT completament diferents

**Els PLC heretats dels anys vuitanta fins a principis dels 2000** es van dissenyar per funcionar aïllats i amb accés exclusivament físic. Executen sistemes operatius propietaris. Sovint es gestionen des d'estacions d'enginyeria que també es connecten a xarxes corporatives. Les seves configuracions es desen en formats sense verificació d'integritat. Aquests sistemes constitueixen una part important de la infraestructura desplegada en el tractament de l'aigua, la generació d'energia, la fabricació i el transport.

**Els controladors moderns amb funcions de seguretat són diferents.** Siemens, Schneider, Rockwell, Beckhoff i Phoenix Contact ja distribueixen plataformes amb arrencada segura, microprogramari signat, control d'accés basat en rols, identitat amb suport TPM i comunicacions xifrades. EtherNet/IP CIP Security, PROFINET Security Class i OPC UA amb autenticació són funcions disponibles en el maquinari actual.

No menystinc l'enginyeria moderna de seguretat OT. El progrés és real. **El problema és que la majoria dels sistemes desplegats no són moderns.** Quan es parla de «ciberseguretat OT», sovint es descriu un intent de protegir un controlador programable de fa vint anys amb un marc de ciberseguretat redactat el 2023. Aquesta és la bretxa a què em refereixo.

## Què funciona de debò

**La seguretat física i l'aïllament de xarxa són els controls més fiables per als entorns OT heretats.** Tots els principals marcs de seguretat ICS diuen el mateix. IEC 62443 organitza els entorns OT en zones de seguretat amb conductes definits. La intenció és obligar el moviment lateral a travessar límits controlats, en comptes de circular per una xarxa plana.

L'aïllament de xarxa redueix de manera notable la superfície d'atac basada en xarxa. No elimina tots els riscos. Els dispositius extraïbles, l'accés intern, els portàtils de manteniment, les connexions temporals d'enginyeria i els compromisos de la cadena de subministrament són vies d'entrada documentades a sistemes sense exposició de xarxa. **Stuxnet**, que va arribar a instal·lacions iranianes de centrifugadores aïllades de la xarxa mitjançant USB infectats, n'és l'exemple clàssic. *L'aïllament de xarxa és necessari. No és suficient.*

**La supervisió humana dels paràmetres del procés físic** continua sent un dels mecanismes de detecció més fiables. Un operador format que observa la pressió, la temperatura i el cabal en temps real detectarà coses que cap sistema de detecció d'intrusions veurà, perquè l'IDS no pot verificar si el valor digital coincideix amb la realitat física.

Controls que redueixen el risc en els contextos adequats:

- **Els díodes de dades** permeten que la telemetria surti sense admetre connexions entrants
- **Les llistes d'aplicacions permeses** a les estacions HMI restringeixen què s'executa als equips que accedeixen als sistemes de control
- **Les plataformes passives de detecció d'anomalies** de Claroty, Dragos i Nozomi analitzen el trànsit sense tocar les comunicacions del pla de control
- **La segmentació de xarxa** entre zones OT alenteix el moviment lateral sense exigir un aïllament físic complet
- **Els principis de confiança zero**, esmentats a NIST SP 800-82 Rev 3, afegeixen requisits de verificació per sessió a algunes arquitectures OT modernes

*Cap d'aquests controls resol les limitacions de disseny de fons. Redueixen el risc als marges de sistemes que mai no es van crear per a això.*

## Els senyals analògics no es poden autenticar

**Els bucles de corrent de 4-20 mA, els senyals de 0-10 V, les sortides de termoparell i les lectures RTD es transmeten com a senyals elèctrics variables.** El senyal físic no disposa de cap mecanisme per verificar-ne l'autenticitat. Qui posa el senyal correcte al cable és considerat legítim.

Stuxnet ho va fer evident. L'atac va manipular la lògica del PLC que s'executava als controladors Siemens S7 i, alhora, va reproduir a les interfícies dels operadors dades normals del procés que s'havien enregistrat prèviament. **Els operadors veien pantalles amb lectures normals mentre les centrifugadores superaven els límits operatius.** L'engany va durar prou per causar danys físics que semblaven una fallada de l'equip, no pas un atac.

Les interferències electromagnètiques dels cables d'alimentació, els variadors de freqüència, els llamps i una presa de terra deficient corrompen les mesures analògiques durant el funcionament normal. IEC 61000 existeix per aquest motiu. Les instal·lacions industrials fan servir cablejat apantallat, una presa de terra correcta, filtres i separació física per controlar-ho.

Els dispositius de camp intel·ligents moderns converteixen internament les mesures analògiques a format digital abans de transmetre-les per HART-IP, WirelessHART, EtherNet/IP CIP Security o OPC UA. El maquinari modern permet comunicacions digitals autenticades al nivell del dispositiu. **El cable analògic de 4-20 mA que connecta un transmissor heretat a una entrada d'un PLC heretat no té autenticació i mai no en tindrà.** Una part important de la instrumentació desplegada encara fa servir aquest cable.

## Validar sensors és un control de seguretat funcional, no de ciberseguretat

Els sistemes de seguretat de processos fan **votació redundant de sensors**. Una configuració de 2 de 3, amb dos sensors que llegeixen 230 PSI i un que llegeix 14 PSI, assenyala el valor atípic. Això ofereix una resiliència limitada davant la manipulació d'un sol sensor. *És un control d'enginyeria de seguretat funcional, no un control de ciberseguretat.*

Els PLC estàndard no validen criptogràficament les entrades analògiques. Un generador de senyal connectat al bucle no es pot distingir d'un transmissor legítim. El PLC llegeix el corrent i hi actua.

**Els sistemes instrumentats de seguretat havien de ser l'última línia de defensa independent.** El 2017, **TRITON** (també conegut com a **TRISIS**) va atacar unitats SIS Triconex de Schneider Electric amb l'objectiu concret de desactivar aquesta capa. Els atacants van arribar al sistema de seguretat mitjançant la xarxa de les estacions d'enginyeria. *La independència de la capa depenia d'una separació de xarxa que no s'havia mantingut.*

IEC 62443-3-3, IEC 62443-4-2 i la coordinació amb la seguretat funcional segons IEC 61511 reflecteixen aquesta lliçó. Durant anys, equips diferents van tractar la seguretat de processos i la ciberseguretat com a disciplines separades. **TRITON va demostrar a la pràctica allò que les anàlisis independents defensaven en teoria:** un atacant que neutralitza el sistema de seguretat abans d'activar la condició perillosa elimina l'últim control que evita conseqüències físiques.

## La cadena de subministrament és una via que probablement ignores

**La majoria dels programes de seguretat OT se centren en l'arquitectura de xarxa. Molts compromisos OT recents han fet servir punts d'entrada que l'arquitectura de xarxa no pot aturar.**

Els riscos de la cadena de subministrament OT inclouen:

- **La integritat del microprogramari abans de la instal·lació**, sobretot si el maquinari arriba de fàbrica o del distribuïdor amb microprogramari no verificat
- **Les sessions d'accés remot dels proveïdors**, que continuen sent exposicions persistents als centres que depenen del suport dels fabricants
- **Les estacions d'enginyeria** connectades tant a la xarxa corporativa com a l'OT, sovint per comoditat operativa
- L'absència de **llistes de materials de programari (SBOM)** en la majoria de desplegaments OT heretats, que fa gairebé impossible rastrejar els components de programari
- **Els contractistes de manteniment** que porten portàtils i dispositius USB a entorns operatius aïllats
- **El suport per a actualitzacions de microprogramari signades**, absent a la majoria de plataformes antigues

NIST SP 800-82 Rev 3 dedica apartats específics a les dependències dels proveïdors i a l'accés de tercers. *Si l'aïllament de xarxa està intacte internament, però el proveïdor de l'equip manté un portal d'accés remot persistent a la xarxa d'enginyeria, no tens una xarxa aïllada. Tens una bretxa amb una porta que controla una altra persona.*

## Endurir els sistemes heretats costa més del que hauria

Cada programa de PLC s'escriu a mida per a un procés específic. La lògica que controla el sistema de prevenció de sobrepressió d'una refineria és completament diferent de la d'una seqüència de cloració d'una planta de tractament d'aigua o d'un regulador de turbina. No és una elecció. Els processos físics són diferents.

**Endurir els sistemes OT heretats sovint costa més del previst** pels requisits de validació d'enginyeria, el temps d'inactivitat necessari, les limitacions de suport del proveïdor, les mancances de documentació i els cicles de prova que superen les estimacions inicials. En alguns casos de maquinari sense suport del proveïdor, el cost d'enduriment s'apropa al cost de substitució del sistema o el supera.

**El compliment de NERC CIP per als actius cibernètics del sistema elèctric a gran escala costa milions de dòlars anuals a cada empresa de serveis públics.** Una enquesta de 2019 de l'American Public Power Association va documentar una gran variació dels costos, amb una càrrega desproporcionada per a les empreses petites. Molts sistemes d'aigua i empreses petites queden fora dels requisits de NERC CIP i no tenen obligacions comparables.

## Cal substituir els sistemes

**Substituir els sistemes OT heretats és la resposta correcta.** En instal·lacions grans, això significa desenes de milions de dòlars, períodes de transició llargs i el risc de codificar erròniament coneixement operatiu complex durant la migració. Són costos i riscos reals.

Les directrius industrials de CISA i ICS-CERT recomanen aplicar controls compensatoris mentre avança el pla de substitució. És una resposta racional a les limitacions. *Dit clarament, reconeix que els equips heretats no permeten assolir una seguretat completa. Aplica els controls possibles i planifica la substitució futura.*

**La realitat és que molts d'aquests sistemes continuaran en servei durant dècades.** És un problema de finançament i de polítiques. La comunitat tècnica ha explicat què cal fer. Els pressupostos operatius i els calendaris de substitució no han anat al mateix ritme.

## Afegir connectivitat de xarxa als sistemes OT sovint empitjora les coses

Moltes organitzacions han afegit funcions d'accés remot i supervisió als entorns OT que abans estaven aïllats. L'argument operatiu és senzill: la visibilitat remota redueix el temps de resposta i el suport dels proveïdors és més ràpid amb connexions remotes. **La conseqüència de seguretat és que els sistemes aïllats, sense superfície d'atac remota, ara en tenen una.**

L'**incident de 2021 de la planta de tractament d'aigua d'Oldsmar** es va produir mitjançant una connexió d'accés remot de TeamViewer. L'atacant va canviar la dosificació d'hidròxid de sodi amb una eina d'accés remot legítima afegida per comoditat. L'**incident de Colonial Pipeline de 2021** va començar amb el compromís d'una xarxa TI. L'operador va aturar preventivament les operacions OT del conducte perquè no podia confirmar que la xarxa OT no s'hagués vist afectada. *L'atac no va vulnerar directament la xarxa OT. La incertesa sobre una possible vulneració va causar l'aturada.*

Afegir connectivitat a sistemes OT heretats per obtenir beneficis operatius, sense dissenyar-la segons estàndards adequats, **en molts casos genera més risc del que justifica el benefici**. El model Purdue encara és útil com a arquitectura de referència, però NIST ja no el considera suficient per si sol. L'IIoT modern, la connectivitat al núvol, les operacions remotes i les arquitectures híbrides requereixen un disseny més deliberat que la segmentació en zones per si sola.

## Complir estàndards escrits no és seguretat

NIST SP 800-82 Rev 3, IEC 62443 i NERC CIP descriuen els controls adequats per a aquests sistemes. No els descarto. Assenyalo el que diuen explícitament: **no tots els sistemes OT poden aplicar tots els controls.** Els marcs fan servir nivells de seguretat escalonats i disposicions per a controls compensatoris precisament perquè els sistemes sovint no poden complir tots els requisits.

La bretxa entre el que descriuen els estàndards i el que pot assolir una instal·lació heretada concreta no és un error de documentació. Els sistemes no admeten els controls. Les directrius ho reconeixen. **Superar una auditoria de compliment en OT heretada no significa que l'entorn sigui segur.** Significa que has documentat els controls compensatoris existents i que un auditor els ha acceptat.

El marc de gestió de riscos de NIST és explícit: després d'aplicar els controls encara queda risc residual. L'acceptació del risc és un dels quatre resultats del marc, juntament amb la transferència, la reducció i l'evitació del risc. *El reconeixement del risc residual forma part de les directrius oficials.* **Si algú et diu que complir els requisits normatius fa segur el teu entorn OT, afirma una cosa que els marcs que cita no sostenen.**

## Què has de fer amb l'OT heretada

Si gestiones entorns OT heretats:

- **Tracta l'aïllament de xarxa com el control principal** i audita tot el que travessa el límit OT
- **Dona un pla d'enduriment propi a les estacions d'enginyeria.** Connecten tots dos entorns i sovint són el punt d'entrada
- **Controla i registra tots els dispositius extraïbles** a les zones OT
- **Audita l'accés remot dels proveïdors** i tanca totes les sessions que no s'utilitzin
- Implementa supervisió redundant dels sensors quan el disseny del procés ho permeti
- **Prepara un calendari de substitució amb estimacions de cost reals**, encara que faltin anys per a la substitució
- **Deixa de tractar la finalització d'auditories de compliment com una fita de seguretat**

Si compres sistemes OT nous:

- **Inclou requisits de seguretat a les especificacions de compra** abans que responguin els proveïdors
- Tria plataformes amb suport documentat per a comunicacions autenticades, actualitzacions de microprogramari signades i control d'accés basat en rols
- **Dissenya els límits TI/OT com a conductes explícits segons IEC 62443**, no com una política vaga de «manteniu-los separats»
- **Exigeix SBOM dels components de programari OT** com a lliurable contractual

El sector ha documentat bé el problema. Els estàndards són tècnicament precisos. *Sovint, els sistemes desplegats no poden rebre allò que prescriuen els estàndards.* Reconèixer-ho obertament és el punt de partida per decidir com gestionar el risc que queda.

## Referències

- NIST SP 800-82 Rev 3: guia de seguretat de la tecnologia operacional (OT) (2023)
- IEC 62443: sèrie de seguretat per a sistemes d'automatització i control industrial
- IEC 62443-3-3: requisits de seguretat dels sistemes i nivells de seguretat
- IEC 62443-4-2: requisits tècnics de seguretat per als components IACS
- IEC 61511: seguretat funcional dels sistemes instrumentats de seguretat
- NERC CIP: estàndards de protecció d'infraestructures crítiques per al sistema elèctric de gran escala
- IEC 61000: estàndards de compatibilitat electromagnètica
- Avisos i bones pràctiques de CISA ICS-CERT
- Marc MITRE ATT&CK per a ICS
- Anàlisi tècnica de Stuxnet, Langner Communications, 2011
- Anàlisi tècnica de TRITON/TRISIS, Dragos, 2017
- Revisió de l'incident de la planta de tractament d'aigua d'Oldsmar, CISA, 2021
- Enquesta de costos de compliment NERC CIP de l'American Public Power Association, 2019
