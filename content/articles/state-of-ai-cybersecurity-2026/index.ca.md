---
title: "Ciberseguretat de la IA el 2026: desplegar ràpid, protegir més tard"
draft: false
toc: true
date: 2026-06-26
lastmod: 2026-11-23
description: "Avaluació de l'adopció de la IA en ciberseguretat, les mancances operatives, les directrius actuals i els controls pràctics per a les organitzacions el 2026."
tags: ["seguretat de la IA", "ciberseguretat de la IA 2026", "injecció de prompt", "agents d'IA", "seguretat MCP", "cadena de subministrament de la IA", "IA a l'ombra", "red teaming de la IA", "seguretat LLM", "observabilitat de la IA", "IA agentiva", "amenaces de la IA", "atacs amb IA", "seguretat dels models", "governança de la IA", "NIST AI 600-1", "OWASP LLM", "MITRE ATLAS", "resposta a incidents d'IA", "seguretat de la IA empresarial", "identitat de la IA", "enverinament del context", "enverinament d'eines", "autorització de la IA"]
cover: "/img/cover/state-of-ai-cybersecurity-2026.webp"
coverAlt: "Il·lustració de sistemes d'IA interconnectats representats com a nodes lluminosos sobre un fons fosc. Les línies brillants mostren les connexions i les ombres al voltant d'alguns nodes indiquen vulnerabilitats de seguretat."
coverCaption: ""
---

Les organitzacions van desplegar sistemes d'IA durant el 2023, el 2024 i el 2025 a un ritme que les directrius defensives, les eines de seguretat i les pràctiques operatives no van poder seguir. **El resultat el 2026 és una superfície d'atac gran, poc monitorada i connectada a sistemes empresarials reals, mentre les defenses encara s'estan construint.**

Vull explicar amb precisió què em preocupa i per què. No és una advertència genèrica sobre els riscos de la IA. És una descripció de la superfície d'atac real, de les mancances documentades i del que han d'abordar les organitzacions.

## Per què existeix aquesta bretxa

La seguretat del programari tradicional va madurar al llarg d'uns trenta anys. Dècades d'experiència en resposta a incidents, recerca de vulnerabilitats, desenvolupament d'eines i coneixement operatiu guanyat amb esforç van produir els marcs, els productes i les pràctiques sobre els quals es basen els programes de seguretat actuals.

**La IA generativa empresarial va arribar a milions de desplegaments en producció en aproximadament dos anys.**

Les disciplines que fan funcionar la seguretat del programari, com ara el modelatge d'amenaces per a arquitectures específiques, els patrons de desplegament reforçats, els procediments madurs de resposta a incidents i les pràctiques establertes d'auditoria i observabilitat, no van tenir temps de desenvolupar-se abans que les organitzacions comencessin a desplegar IA a gran escala. *Les directrius van arribar després del desplegament. Les eines van arribar després de les directrius. L'expertesa operativa encara està evolucionant.*

No és un retret. Explica per què les mancances són estructurals i no accidentals.

## Les quatre capes de la seguretat de la IA

Gran part de la confusió en les converses sobre seguretat de la IA prové de tractar els documents de governança, les taxonomies d'amenaces, les directrius d'enginyeria i els controls operatius com si fossin el mateix. No ho són.

**La capa 1 és la governança.** NIST AI RMF, ISO/IEC 42001 i EU AI Act operen a nivell organitzatiu i de processos. Descriuen com gestionar els riscos de la IA, estructurar la supervisió i documentar la rendició de comptes. Són marcs de governança, no controls tècnics.

**La capa 2 és la taxonomia d'amenaces.** MITRE ATLAS documenta tàctiques adversàries contra sistemes d'IA. OWASP Top 10 for LLMs i OWASP Agentic AI Top 10 enumeren classes d'atac concretes. Aquests documents posen nom als atacs, però no prescriuen defenses.

**La capa 3 són les directrius d'enginyeria.** Google SAIF, Microsoft AI SDL, OWASP AI Exchange i NIST AI 600-1 proporcionen orientacions per construir i desplegar IA de manera segura. NIST AI 600-1 és molt més específic que l'AI RMF bàsic i tracta la injecció de prompts, l'enverinament de dades i els perills informatius en els desplegaments d'IA generativa.

**La capa 4 són les operacions.** La supervisió, la resposta a incidents, els controls en temps d'execució, el registre, el mínim privilegi, les canonades d'avaluació i la governança de l'accés són pràctiques operatives. Requereixen processos organitzatius, no només documentació.

*La majoria d'organitzacions tenen una cobertura incompleta de les capes 3 i 4. És aquí on es concentra gairebé tot el risc operatiu.*

## Què hi ha en producció

La IA empresarial el 2026 no són només xatbots. Els sistemes en producció inclouen:

- **Sistemes RAG** que recuperen informació de repositoris interns de documents, wikis, bases de dades i registres de clients
- **Agents d'atenció al client** amb accés a dades de comptes i sistemes de gestió de casos
- **Assistents interns de productivitat** integrats amb el correu electrònic, els calendaris, els sistemes de fitxers i les plataformes de comunicació
- **Eines de revisió i generació de codi** amb accés als repositoris de codi font
- **Agents automatitzats** que executen fluxos de treball programats amb credencials per a API internes
- **Processadors de documents, contractes i dades financeres**
- **Models d'IA integrats en la detecció de frau, la selecció de personal i les decisions de control d'accés**

Cada sistema representa una superfície d'atac diferent. Un sistema RAG connectat a la base de coneixement interna és alhora un risc de divulgació d'informació i un objectiu per a la injecció de prompts. **Un agent amb accés al correu electrònic i una credencial persistent és un procés autònom amb influència real sobre sistemes reals.**

*Sovint els equips de seguretat no van participar en la decisió de desplegar aquests sistemes. Descobreixen desplegaments d'IA existents durant una auditoria en lloc d'una revisió del disseny.*

## Ara la IA és a totes dues bandes

**Les mateixes capacitats d'IA disponibles per a l'equip de seguretat també estan a l'abast dels atacants.**

**El desenvolupament assistit per IA** redueix el temps necessari per convertir les divulgacions públiques de vulnerabilitats en proves de concepte funcionals i eines operatives. El pas de llegir una CVE a tenir codi funcional és més ràpid per a qualsevol que faci servir aquestes eines, inclosos els atacants.

**El contingut de pesca generat per IA** produeix correus amb millor gramàtica, un context més convincent i menys errors detectables que molts atacs escrits per persones. Els senyals de format i els patrons lingüístics que els usuaris han après a reconèixer són menys fiables quan el contingut el genera la IA.

**La clonació de veu en campanyes de pesca de veu** suplanta executius i companys en trucades en temps real. La barrera d'entrada per a l'enginyeria social dirigida ha baixat amb la millora de la síntesi de veu i la reducció dels costos d'accés.

**Els vídeos deepfake per al frau de correu empresarial** han passat de ser teòrics a operatius. Des del 2024 s'han documentat fraus financers en diversos sectors que utilitzen vídeos d'executius generats per IA autoritzant transaccions. *La formació de conscienciació es va dissenyar per a un altre model d'amenaça.*

## Injecció d'instruccions i contaminació del contingut de treball

**Entendre la injecció de prompts és el punt de partida per entendre la seguretat dels sistemes d'IA.**

Un model lingüístic segueix les instruccions incloses a la seva finestra de context. Aquesta finestra inclou el prompt del sistema, l'historial de converses, les sortides de les eines i els documents recuperats. **El model no pot distingir de manera fiable les instruccions del desenvolupador de l'aplicació de les instruccions que un atacant ha inserit en el contingut que el model està processant.** Aquest és el nucli de la injecció de prompts segons la definició d'OWASP.

La *injecció directa de prompts* apunta directament a l'entrada del model. L'usuari proporciona text dissenyat per substituir les instruccions del sistema.

La *injecció indirecta de prompts* és més greu en desplegaments empresarials. L'agent RAG recupera un document de la base de coneixement. El document conté instruccions perquè l'agent faci una altra acció. L'eina de resum processa una pàgina web amb directives ocultes. El bot de suport llegeix un adjunt del client amb instruccions. L'agent les processa i hi actua.

**L'enverinament del context** és una categoria més àmplia. Els atacants no necessiten comprometre el model per comprometre el sistema d'IA. Han d'introduir contingut maliciós al context del model. Això inclou documents RAG enverinats, entrades de memòria enverinades, contingut de correu electrònic preparat maliciosament que processa l'agent, PDF adversaris i pàgines web controlades per l'atacant que visita l'agent de navegació. *Això és diferent de l'enverinament del model. El model està bé. El context no.*

La defensa en profunditat redueix aquest risc. Els filtres d'entrada, la validació de sortides, els àmbits limitats de les eines, l'execució aïllada i les aprovacions humanes per a accions importants ajuden. **Cap d'aquestes defenses no tanca la classe d'atac.** OWASP, NIST, Anthropic, OpenAI i Microsoft recomanen enfocaments per capes perquè cap control individual no és suficient.

*Dissenya assumint que la injecció de prompts tindrà èxit en un percentatge de les entrades. Limita'n les conseqüències en consonància.*

## Assistents d'IA, límits de permisos i l'abast dels danys

Operativament, els agents es diferencien dels xatbots en un aspecte crític: **duen a terme accions.**

Un agent connectat al correu electrònic, GitHub, Jira, Slack, Salesforce, AWS i API internes és un procés autònom amb accés als mateixos sistemes que utilitzen els empleats més connectats. **Una injecció de prompts reeixida contra aquest agent no produeix una resposta textual indesitjada. Produeix una acció indesitjada en un sistema real.**

**L'abast de l'impacte d'una intrusió depèn de què pot accedir l'agent.** La majoria de desplegaments actuals d'agents tenen molt més accés del que requereix qualsevol tasca individual. Un agent que ha de llegir un tiquet de Jira no hauria de tenir també accés d'escriptura a la branca principal de GitHub. Un agent que processa sol·licituds de suport no hauria de tenir credencials del sistema de facturació.

**L'autorització de la IA és un problema diferent de l'autorització de l'usuari.** Les aplicacions tradicionals pregunten si un usuari està autoritzat a fer una acció. Les arquitectures d'agents han de preguntar si aquest agent està autoritzat a fer aquesta acció concreta per a aquest usuari concret en aquest moment i segons el context actual. La majoria dels desplegaments actuals d'agents no ho implementen.

**L'enverinament d'eines** és diferent de la injecció de prompts. Una eina maliciosa o compromesa connectada a un agent retorna descripcions o dades dissenyades per alterar-ne el comportament. Els investigadors consideren cada vegada més l'enverinament d'eines una classe d'atac separada de la injecció de prompts, sobretot en integracions basades en MCP.

*Els fluxos d'aprovació humana han de ser l'última barrera per a les accions importants dels agents. Les organitzacions també descobreixen el cansament d'aprovar. Quan els agents demanen sovint aprovació per a accions rutinàries, els usuaris comencen a aprovar automàticament sense revisar la sol·licitud. L'última barrera es converteix en un tràmit.*

## La identitat de la IA és un problema de seguretat empresarial

**Els agents tenen credencials.** Les implementacions d'agents d'IA fan servir tokens OAuth, claus API, credencials de comptes de servei i rols cloud IAM. Són identitats no humanes amb accés real.

Mancances concretes en els desplegaments actuals:

- **Les credencials dels agents sovint són de llarga durada** i no es roten amb una periodicitat comparable a la dels comptes de servei
- **Els àmbits dels tokens dels agents sovint són més amplis** del que requereixen les seves tasques
- El registre d'auditoria de les accions fetes amb identitats d'agent varia molt
- **La filtració de credencials a través dels prompts** és un risc documentat. Si un agent inclou les seves claus API al context o a les sortides, les exposa a qui llegeixi la sortida o recuperi la conversa.
- Els agents que obtenen credencials addicionals mitjançant crides a eines creen **cadenes d'identitat difícils d'auditar**

*Governar les identitats dels agents com els comptes de servei privilegiats requereix una acció deliberada, perquè la majoria d'eines de governança d'identitats no admeten de manera nativa els patrons d'identitat dels agents d'IA.*

## La memòria que perdura entre sessions amplia els riscos d'atac

**Els agents amb memòria persistent presenten una superfície d'atac que no existeix en sistemes sense estat.**

Un atacant que pot injectar contingut a la memòria d'un agent estableix una posició que perdura entre sessions. *L'atac no ha de reeixir en una sola interacció. La influència acumulada a la memòria durant dies o setmanes modela el comportament futur de l'agent.* De vegades s'anomena **atac d'horitzó llarg o d'estat latent del context**.

Hi ha molt poques directrius operatives per a aquest risc concret. Les organitzacions que despleguen agents amb memòria persistent han de:

- Tractar els **magatzems de memòria com a dades d'alt valor** que requereixen controls d'accés
- **Validar el contingut de la memòria** abans que els agents hi actuïn
- Incorporar a l'arquitectura la capacitat d'**auditar i revertir l'estat de la memòria**

## La cadena de subministrament de models no es tracta com la de programari

**Les organitzacions que descarreguen models preentrenats de repositoris públics accepten artefactes d'IA executables de fonts externes. L'escrutini d'aquestes descàrregues no sol estar al nivell que aquestes mateixes organitzacions apliquen als paquets npm, PyPI o Maven.**

Riscos concrets als repositoris de models:

- **Els fitxers de models PyTorch en format pickle** executen codi Python arbitrari en carregar-se. Això s'ha explotat en atacs documentats a la cadena de subministrament. **SafeTensors** és el format dissenyat específicament per resoldre aquest problema. Prefereix-lo quan estigui disponible.
- Carregadors de models maliciosos que instal·len dependències o executen codi de configuració amb el model
- Models entrenats amb **conjunts de dades enverinats** que produeixen sortides subtilment incorrectes en contextos concrets
- Models amb **portes del darrere incrustades** que s'activen en certes condicions
- **Suplantació del nom del repositori** per distribuir models maliciosos amb noms familiars

*Poques organitzacions mantenen una llista de materials de programari que cobreixi els seus sistemes d'IA.* La majoria no poden dir quin model base va originar un sistema de producció, quina versió de les dades d'entrenament es va utilitzar per a l'ajustament o si els pesos desplegats coincideixen amb els últims que es van avaluar. Aquesta traçabilitat és un requisit previ per a una seguretat significativa de la cadena de subministrament. Avui no és habitual.

## La IA a l'ombra crea fluxos de dades sense control

**Els comptes personals d'IA per a consumidors són el lloc on les dades es mouen sense controls.**

ChatGPT Enterprise, Claude Enterprise i Microsoft Copilot per a M365 inclouen proteccions contractuals per a les dades dels clients. **Els comptes personals de ChatGPT, Claude, Gemini i serveis de consum similars no ofereixen aquestes garanties per defecte.**

Els empleats que utilitzen comptes personals per processar documents de feina transfereixen estratègies legals, registres de clients, codi font, projeccions financeres, decisions de personal i comunicacions internes per canals que l'organització no controla. *Els equips de seguretat sovint no tenen informació precisa sobre el volum d'aquesta activitat ni sobre les categories de dades implicades.*

Els controls DLP no detecten les dades que passen pel navegador cap a un servei d'IA per a consumidors. Les polítiques de retenció de dades no s'apliquen a l'historial de converses d'una plataforma de tercers. **Les obligacions reguladores sota GDPR, HIPAA, SOX i les normes sectorials no canvien pel fet que les dades hagin sortit accidentalment o a través d'una pestanya del navegador.**

*Descobrir l'abast real abans de crear controls és el primer pas necessari. Gairebé segur que la teva estimació del problema és massa baixa.*

## Els sistemes d'IA filtren dades de maneres que les aplicacions tradicionals no ho fan

**La recuperació excessiva de RAG** retorna documents a usuaris que no hi haurien de tenir accés. Un empleat fa una pregunta. El component de recuperació retorna un document d'un segment restringit de la base de coneixement. La resposta inclou informació d'aquest document. *La fallada del control d'accés s'ha produït a la capa de recuperació, no a la capa d'aplicació.* Molts desplegaments RAG es van crear sense aplicar permisos a nivell de document que coincideixin amb els del sistema d'origen.

**La filtració del prompt del sistema** revela les instruccions operatives incorporades al producte d'IA. Tracta els prompts del sistema com a confidencials. La filtració de credencials a través dels prompts, quan les credencials de l'agent apareixen al context o a les sortides del model, sol ser més greu que l'exposició del prompt del sistema per si sola.

**Els errors d'aïllament de la IA multiempresa** es produeixen quan models ajustats amb dades de diversos clients mostren la informació d'un client en el context d'un altre. És una categoria de risc documentada per als productes SaaS d'IA multiempresa.

**La memorització del model** fa que els models reprodueixin literalment contingut de les dades d'entrenament. El risc no desapareix, sobretot en models ajustats amb conjunts de dades privades petits o deduplicats de manera insuficient. Les organitzacions que ajusten models amb dades internes sensibles han d'avaluar aquest risc segons l'enfocament i les dades concretes que utilitzen.

## Les organitzacions no tenen visibilitat en el moment de la inferència

Els programes de seguretat tradicionals tenen una cobertura extensa dels registres de la infraestructura. **La majoria de desplegaments d'IA no tenen una cobertura equivalent dels seus components d'IA.**

Per supervisar un model lingüístic o un agent desplegat cal una telemetria diferent de la d'un servidor d'aplicacions. Les organitzacions han de recopilar:

- **Contingut dels prompts i de les sortides** en un format adequat per revisar polítiques i detectar anomalies
- **Registres de crides a eines** dels agents, amb noms d'eines, arguments i respostes
- **Registres de recuperació** dels sistemes RAG, amb consultes, documents retornats i decisions de control d'accés
- **Senyals de classificació** dels intents de jailbreak i d'injecció
- **Supervisió de la consistència de les sortides** per detectar canvis de comportament entre versions del model
- **Patrons de latència** que poden indicar intents d'omplir el context

*Moltes organitzacions que van desplegar IA el 2023 i el 2024 tenen codis d'estat HTTP i mètriques de latència. Sovint no tenen la telemetria necessària per detectar o investigar un incident de seguretat d'IA. Descobrir-ho després de l'incident és massa tard.*

## La resposta a incidents d'IA necessita procediments propis

**Els procediments de resposta a incidents actuals cobreixen endpoints, xarxes, aplicacions i identitat. No cobreixen escenaris específics de la IA.**

Preguntes que haurà d'afrontar l'equip d'IR i que els procediments actuals no resolen:

- Com determinar si un model es va enverinar durant una execució d'ajustament
- Com delimitar l'abast d'una injecció indirecta reeixida contra un agent amb accés d'escriptura a diversos sistemes
- Com avaluar si les dades d'entrenament o d'ajustament es van exfiltrar en un compromís de la cadena de subministrament
- Com establir una **línia base de comportament** del model per comparar-la amb el comportament posterior a l'incident
- Com respondre quan una actualització del model d'un proveïdor extern introdueix un comportament que sembla intencionat i no accidental
- Com determinar si **la memòria de l'agent s'ha manipulat amb el temps**

*Aquests escenaris requereixen preparació abans que es produeixin. Cal tenir telemetria abans de l'incident. Cal documentar les línies base de comportament abans de necessitar comparar-les.*

## Les canonades d'avaluació es converteixen en pràctica habitual d'enginyeria

La seguretat de la IA depèn cada vegada més de **l'avaluació estructurada abans del desplegament**, i no només de la supervisió posterior.

L'avaluació de seguretat abans del desplegament inclou:

- **Proves d'injecció de prompts** amb conjunts de dades establerts i el cas d'ús concret
- **Comparatives de jailbreak** amb col·leccions publicades de prompts adversaris
- **Avaluació de la robustesa adversària** dels models que prenen decisions amb conseqüències importants
- **Proves de regressió** entre versions de models per identificar canvis de comportament
- **Avaluació de polítiques** respecte als requisits documentats d'ús acceptable
- **Exercicis de red teaming** duts a terme per persones que intenten superar defenses concretes

NIST, CISA, Anthropic, OpenAI, Microsoft i Google ho esperen cada vegada més per als desplegaments d'alt risc. *Construir canonades d'avaluació mínimes abans de desplegaments amb conseqüències importants és més assolible del que creuen moltes organitzacions.* OWASP AI Exchange i els marcs d'avaluació publicats pels principals proveïdors d'IA són bons punts de partida.

## És probable que l'inventari d'actius d'IA sigui incomplet

La gestió d'actius tradicional cobreix servidors, endpoints, aplicacions i dispositius de xarxa. **Els sistemes d'IA introdueixen categories d'actius que la majoria d'inventaris encara no controlen.**

Un inventari de sistemes d'IA ha d'incloure:

- Cada **model desplegat**, inclosos els models base, les variants ajustades i els models d'embedding
- Tots els **prompts i les instruccions del sistema** actius en producció
- Cada **agent** que s'executa a l'entorn i les eines a què té accés
- Tots els **índexs RAG**, incloses les fonts de dades i els controls d'accés aplicats durant la recuperació
- Totes les **bases de dades vectorials** i el seu contingut
- Cada **servidor MCP o marc d'integració equivalent** connectat a qualsevol agent
- Els **serveis externs d'IA** que criden les aplicacions i les dades enviades a cadascun

*No pots governar allò que no has inventariat. El 2026, la majoria d'organitzacions que treballen en seguretat de la IA descobreixen actius que no sabien que existien.*

## En quin punt es troba realment la defensa

Les eines, els marcs i les pràctiques de defensa de la seguretat de la IA es desenvolupen activament i de manera significativa. El camp és incipient, però millora.

**NIST AI 600-1** amplia l'AI RMF bàsic per a la IA generativa amb molta més especificitat operativa. Les organitzacions que mantenen programes de compliment de la IA haurien de llegir AI 600-1 i no només el marc bàsic.

**MITRE ATLAS** proporciona documentació de tàctiques, tècniques i procediments adversaris per a sistemes d'IA en format ATT&CK. El modelatge d'amenaces amb ATLAS abans del desplegament produeix requisits de seguretat més precisos que treballar només amb marcs de governança.

**OWASP LLM Top 10** i **OWASP Agentic AI Top 10** ofereixen les directrius públiques més específiques des del punt de vista operatiu. Totes dues són més útils per als professionals que la majoria de currículums formals.

El **red teaming de la IA** abans del desplegament és cada vegada més esperat per NIST, CISA i els grans proveïdors d'IA en desplegaments d'alt risc. Existeix un mercat extern de proves d'equips vermells d'IA i està creixent per a les organitzacions sense capacitat interna.

Els productes de seguretat específics per a IA que cobreixen la supervisió, els guardrails, l'autorització i l'aplicació de polítiques en temps d'execució es troben en les primeres fases comercials. *Aquesta categoria és real i val la pena avaluar-la. Com que el mercat és incipient, les afirmacions de màrqueting sovint superen les capacitats demostrades. Avalua els productes segons la teva arquitectura concreta i no segons els escenaris descrits pel proveïdor.*

## Què has de fer

**Inventaria el que tens desplegat.** Sap què s'executa, a quines dades accedeix, quines credencials té, quines eines crida i quines accions fa. És el requisit previ de tota la resta.

**Tracta els agents d'IA com a comptes privilegiats.** Aplica el mínim privilegi. Limita les credencials a l'accés mínim necessari per a cada tasca. Audita els accessos de cada agent i elimina els que no calen.

**Implementa observabilitat específica per a IA abans del desplegament**, no després d'un incident. El registre de prompts i sortides, de crides a eines i de recuperacions és la telemetria mínima per a l'anàlisi de seguretat.

**Avalua l'exposició a la IA a l'ombra.** Descobreix quins serveis d'IA utilitzen els empleats per a tasques de feina. Determina quines categories de dades passen per comptes personals. Basa les polítiques i els controls en els resultats reals.

**Aplica controls d'accés a nivell de document als sistemes RAG.** Si la capa de recuperació no aplica les regles d'accés dels sistemes d'origen, corregeix-ho abans que mostri un document restringit a un usuari no autoritzat.

**Audita la cadena de subministrament dels models.** Documenta tots els models base en ús. Prefereix SafeTensors als formats pickle. Aplica als artefactes de models un control de cadena de subministrament comparable al de les dependències de programari.

**Governança les identitats dels agents.** Gestiona els tokens OAuth i les claus API dels agents amb el mateix cicle de vida, revisió d'àmbits i pràctiques de rotació que apliques als comptes de servei privilegiats.

**Construeix ara procediments de resposta a incidents específics per a IA.** Defineix abans d'un incident com investigar els escenaris d'IA, quines proves necessites i quines opcions de resposta tens.

**Avalua la IA abans de desplegar-la en contextos d'alt impacte.** Comença amb els marcs públics disponibles si no tens eines internes.

*No tractis el compliment de la governança com una postura de seguretat. Els marcs de governança descriuen processos i gestió de riscos. No descriuen sistemes tècnicament defensius. Calen totes dues coses.*

## Referències

- NIST AI Risk Management Framework (AI RMF 1.0), 2023
- NIST AI 600-1: Generative AI Profile, 2024
- OWASP Top 10 for Large Language Model Applications, 2025
- OWASP Agentic AI Top 10
- OWASP AI Exchange
- MITRE ATLAS: Adversarial Threat Landscape for AI Systems
- Google Secure AI Framework (SAIF)
- Microsoft AI Security SDL
- CISA Guidance on AI Cybersecurity, 2024
- ISO/IEC 42001:2023 Artificial Intelligence Management Systems
- EU AI Act, Regulation (EU) 2024/1689
- SafeTensors format documentation, Hugging Face
