---
title: "Els millors harnesses d'agents d'IA el 2026: tria segons el flux de treball"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Compara Deep Agents, Claude Agent SDK, OpenAI Agents SDK, Pydantic AI, Pi i LangGraph segons l'execució d'eines, la memòria, la recuperació i l'esforç d'integració."
genre: ["Intel·ligència artificial", "Desenvolupament de programari", "Seguretat de la IA"]
tags: ["harnesses d'agents d'IA", "millors frameworks d'agents", "Deep Agents", "Claude Agent SDK", "OpenAI Agents SDK", "Pydantic AI", "agent de programació Pi", "LangGraph", "runtime d'agents", "crida d'eines", "memòria d'agents", "gestió del context", "execució durable", "permisos d'agents", "seguretat d'agents d'IA", "agents d'IA locals", "avaluació d'agents", "humà en el circuit", "comparació de SDK d'agents", "agents de producció"]
cover: "/img/cover/ai-agent-execution-components.webp"
coverAlt: "Components metàl·lics modulars connectats a un processador central lluminós amb camins turquesa i taronja sobre una superfície de treball fosca"
coverCaption: "Il·lustració conceptual dels components que envolten un model d'IA."
---

**Deep Agents és la meva primera opció per a un agent general amb models configurables i gestió del context integrada.** Claude Agent SDK encaixa bé per incrustar el comportament d'execució de Claude Code. OpenAI Agents SDK i Pydantic AI mereixen una prova per a agents específics d'una aplicació, mentre Pi prioritza un nucli petit i extensible i LangGraph prioritza el control explícit del flux de treball.

**La millor opció depèn del treball que vulguis acceptar.** Un assistent de recerca, un editor de repositoris i un servei que processa sol·licituds de clients necessiten eines i regles de recuperació diferents. Aquestes recomanacions són judicis editorials basats en documentació oficial revisada el **10 d'octubre de 2026**, no resultats d'un benchmark pràctic de rendiment.

<!--more-->

## Idees clau

- **Tria primer l'abstracció:** agent assemblat, SDK d'aplicació o runtime de flux de treball.
- **Comprova els límits d'execució:** l'aprovació d'eines, l'aïllament del sistema de fitxers i la política de xarxa resolen problemes diferents.
- **Prova la recuperació:** l'historial de conversa per si sol no evita accions externes duplicades.
- **Mesura el treball acceptat:** inclou errors, temps de revisió i infraestructura en la comparació de costos.
- **Mantén explícit el model:** canviar el model i el programari de l'agent prova el sistema complet, no només el programari.

## Què proporciona un harness

Un **harness d'agent és el programari que envolta una crida al model.** Prepara el context, exposa eines, executa accions aprovades, retorna resultats i decideix quan continuar o aturar-se. Segons la implementació, també gestiona memòria, delegació, permisos i recuperació.

Un **model** proposa la següent acció. Una **eina** executa una operació. Un **runtime** executa i conserva el flux de treball. Aquestes responsabilitats se solapen en productes empaquetats, però separar-les ajuda a identificar capacitats que falten.

| Component | Pregunta que cal fer |
|---|---|
| **Gestió del context** | Quins requisits sobreviuen a una execució llarga? |
| **Execució d'eines** | Qui valida els arguments i limita l'autoritat? |
| **Emmagatzematge de l'estat** | Què sobreviu al reinici del procés? |
| **Verificació** | Quina evidència estableix que s'ha completat? |

Considera un **agent de suport il·lustratiu** a qui es demana inspeccionar una comanda i preparar una sol·licitud de reemplaçament. Llegir la comanda, proposar el reemplaçament i enviar-lo han de tenir autoritats separades. Una explicació convincent no demostra permís per enviar, i una transcripció desada no demostra si l'enviament ja s'ha fet.

**Abast:** aquesta guia compara opcions de programari i runtime que es poden incrustar. Per a interfícies diàries de desenvolupador, usa la [comparació d'agents de programació CLI](/articles/cli-coding-agents-comparison/) o la [comparació d'agents de programació GUI](/articles/gui-coding-agents-comparison/). Una comparació de SDK no s'ha de convertir en silenci en una classificació d'eines de terminal contra extensions d'editor.

## La llista curta pràctica

| Requisit inicial | Primera opció a avaluar | Responsabilitat principal que conserves |
|---|---|---|
| **Agent general** | Deep Agents | Configurar backend, permisos i model |
| **Claude Code dins d'una aplicació** | Claude Agent SDK | Operar i aïllar el procés d'execució |
| **Flux d'eines d'una aplicació** | OpenAI Agents SDK | Definir eines, aprovacions i acceptació |
| **Aplicació Python tipada** | Pydantic AI i el seu paquet Harness | Seleccionar capacitats i espai de treball |
| **Nucli de programació mínim incrustable** | Pi SDK | Assemblar extensions i política d'execució |
| **Flux durable explícit** | LangGraph | Dissenyar l'estat del graf i la recuperació |

**Són punts de partida diferents.** Deep Agents ja usa LangGraph, així que triar-lo no és necessàriament una decisió excloent. Pydantic AI també separa el seu framework bàsic d'agents de les capacitats de harness assemblades. Compara la quantitat de codi d'aplicació que has de mantenir, en lloc de tractar cada fila com una biblioteca intercanviable.

**Comença per la capa més petita que superi la prova d'acceptació.** Usa un framework d'aplicació tipat per a crides d'eines limitades, un agent assemblat per a treball obert amb fitxers o recerca, i un graf explícit quan la recuperació i les transicions necessitin estats amb nom. Afegeix memòria, accés a shell o subagents només després que una prova mostri per què falla la capa més simple.

## Deep Agents: capacitats assemblades

**Tria Deep Agents primer per a un agent que treballi amb fitxers, eines i converses llargues.** La seva [visió general oficial](https://docs.langchain.com/oss/python/deepagents/overview) documenta backends de sistema de fitxers, descàrrega de context, resum, subagents i aprovació humana. Es basa en LangChain i el runtime LangGraph, amb integracions per a diversos proveïdors de models.

**La configuració encara determina el comportament.** La documentació actual indica que la planificació de tasques és opt-in a partir de la versió 0.7. No assumeixis que un tutorial d'una versió anterior descriu els valors actuals. Registra la versió del paquet i el middleware activat en l'avaluació.

**Inspecciona amb cura l'abast dels permisos.** Les regles documentades del sistema de fitxers cobreixen les eines de fitxers integrades, no ordres shell arbitràries a través de backends sandbox. Denegar una eina de fitxers no és suficient si un altre camí d'execució arriba al mateix fitxer. Prova conjuntament el backend i el límit de shell.

**La meva recomanació:** posa'l a la llista curta per a un servei d'anàlisi de documents o repositoris quan vulguis capacitats assemblades i elecció de proveïdor. Prefereix un punt de partida més petit quan la tasca sigui dues crides API limitades i una resposta validada. Les eines addicionals aporten més comportament per avaluar.

## Claude: execució incrustada

**Tria Claude Agent SDK quan vulguis l'agent de Claude Code dins de la teva aplicació.** Anthropic descriu una biblioteca Python i TypeScript que usa el mateix bucle d'execució, eines i gestió del context que Claude Code. L'SDK executa el binari de Claude Code en un procés que tu operes. És diferent del client API bàsic d'Anthropic i dels Managed Agents allotjats. [Visió general de l'Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview).

**L'atractiu és reutilitzar un sistema d'execució existent.** Les operacions de fitxers, ordres, hooks, permisos, sessions i subagents arriben com a capacitats documentades. La teva integració aporta el límit de l'aplicació i les comprovacions d'acceptació específiques de la tasca.

**L'allotjament continua sent una decisió d'enginyeria.** La [guia de desplegament d'Anthropic](https://code.claude.com/docs/en/agent-sdk/secure-deployment) tracta controls del sistema de fitxers, restriccions de xarxa i aïllament. Configura'ls al voltant del procés en lloc de tractar un diàleg de permisos com un límit del sistema operatiu.

**La meva recomanació:** avalua'l per a automatització de documents o codi centrada en Claude amb força treball de fitxers i ordres. Tria una alternativa flexible amb el proveïdor si comparar models locals i diversos proveïdors allotjats és un requisit central del producte.

| Opció assemblada | Èmfasi de la integració |
|---|---|
| **Deep Agents** | Selecció de model, middleware i configuració del backend |
| **Claude Agent SDK** | Execució de Claude Code dins d'un procés d'aplicació |

## OpenAI: fluxos d'eines d'aplicació

**Tria OpenAI Agents SDK per a una aplicació organitzada al voltant de funcions, tasques delegades i sortides explícites.** La seva [visió general](https://openai.github.io/openai-agents-python/) documenta el bucle de l'agent, handoffs, guardrails, tracing i capacitats de sandbox-agent. L'SDK és una interfície per a constructors, diferent de l'aplicació de desenvolupador Codex.

**L'aprovació és un comportament configurable.** La [guia human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/) descriu execucions interrompudes i estat serialitzat per reprendre després d'una decisió. Per a eines locals de shell i patch, l'aprovació és opt-in. Afegir només un callback d'aprovació no activa el requisit d'aprovació.

**El suport de models va més enllà d'OpenAI.** La [documentació de proveïdors](https://openai.github.io/openai-agents-python/models/) descriu punts d'integració i adaptadors per a proveïdors externs. Valida sortides estructurades, crides d'eines i suport de transport per al teu endpoint, sense assumir paritat de funcions.

**La meva recomanació:** posa'l a la llista curta per a un servei on les accions útils ja existeixin com a funcions d'aplicació ben definides. Per exemple, recupera una comanda, calcula l'elegibilitat amb codi normal i prepara una sol·licitud estructurada. Mantén l'autorització i les comprovacions d'elegibilitat a l'aplicació encara que el model triï l'eina següent.

## Pydantic AI: aplicacions tipades

**Tria Pydantic AI quan els tipus Python i les sortides validades siguin centrals a la teva aplicació.** La seva [documentació principal](https://pydantic.dev/docs/ai/overview/) cobreix eines tipades, injecció de dependències, sortides estructurades i integracions d'execució durable. La validació estableix l'estructura requerida de la sortida. No estableix la veritat de cada camp.

**El paquet Harness separat afegeix capacitats assemblades.** La seva [documentació](https://pydantic.dev/docs/ai/harness/) inclou les piles Coder i Researcher, accés al sistema de fitxers i shell, memòria i integracions d'espai de treball. Un espai de treball local i un sandbox aïllat són opcions d'execució diferents. Les capacitats de harness pertinents requereixen un espai de treball en lloc de seleccionar-ne un en silenci.

**La meva recomanació:** posa el framework bàsic a la llista curta per a un servei Python que retorni registres tipats. Afegeix capacitats de harness quan la tasca també necessiti explorar l'espai de treball o fer recerca oberta. Això evita que un servei d'extracció limitat hereti accés a shell sense una necessitat concreta.

Per a un **agent il·lustratiu de revisió de factures**, la validació de l'esquema comprova si un total és numèric i si una moneda pertany a un conjunt permès. La lògica separada de l'aplicació compara el total amb les línies i verifica l'evidència d'origen. Totes dues comprovacions pertanyen a la prova.

| Aspecte de l'aplicació | Prova d'acceptació |
|---|---|
| **Sortida estructurada** | Valida camps i comprova el seu significat de manera independent |
| **Pausa d'aprovació** | Persisteix l'acció pendent exacta i la decisió |
| **Canvi de proveïdor** | Repeteix les proves de compatibilitat de crides i sortides |

## Pi: nucli petit extensible

**Tria l'SDK de Pi quan vulguis control directe sobre una implementació compacta d'un agent de programació.** La [documentació del projecte](https://github.com/earendil-works/pi/tree/main/packages/coding-agent) descriu la integració SDK i RPC al costat de la interfície interactiva. El conjunt d'eines per defecte inclou lectura, escriptura, edició i execució shell, amb extensions per a comportament addicional.

**El minimalisme trasllada feina a l'integrador.** Pi omet deliberadament finestres de permisos integrades i orquestració de subagents. La seva documentació dirigeix els usuaris cap a contenidors o extensions personalitzades per als fluxos de confirmació. Avalua aquí l'SDK incrustat, no la seva interfície de terminal contra l'editor gràfic d'un altre proveïdor.

**La meva recomanació:** posa Pi a la llista curta per a un servei de programació a mida si estàs disposat a fer-te càrrec de les restriccions d'execució, la revisió d'extensions i la política de recuperació. El seu nucli petit facilita entendre i canviar el comportament. És un punt de partida menys adequat quan el requisit principal és un sistema d'aprovació i orquestració ja assemblat.

## LangGraph: control explícit del flux de treball

**Tria LangGraph quan el flux de treball necessiti estat i transicions explícits.** La seva [documentació de persistència](https://docs.langchain.com/oss/python/langgraph/persistence) distingeix checkpoints limitats al fil de stores entre fils. Un checkpointer persistent permet la recuperació després de reinicis del procés. Un checkpointer en memòria no ho fa.

**LangGraph és una base de runtime.** Tu defineixes el flux de treball i decideixes on pertany el comportament guiat pel model. Deep Agents ja usa aquesta base, així que baixar a LangGraph té sentit quan necessites més control directe sobre els camins d'execució.

**La meva recomanació:** posa'l a la llista curta per a un procés amb etapes amb nom, pauses de revisió i regles de recuperació diferents. Un flux d'entrada de documents podria extreure camps, validar-los, demanar revisió i publicar un registre aprovat. Les transicions fixes són útils quan el model ha de triar el contingut però no inventar el procés de negoci.

| Etapa del flux | Evidència de finalització |
|---|---|
| **Extreure** | Registre candidat vinculat a la font |
| **Validar** | Comprovacions deterministes i excepcions |
| **Revisar** | Decisió adjunta al candidat concret |
| **Publicar** | Rebut extern registrat contra l'operació |

**Els efectes externs necessiten el seu propi disseny de recuperació.** Desar l'estat del graf no fa atòmica una transacció d'un servei remot amb el checkpoint. Usa un identificador d'operació i concilia el resultat extern abans de repetir un enviament.

## Prova les peces que falten

**Una llista de funcions només és un punt de partida.** Executa cada candidat davant errors que s'assemblin a la teva càrrega de treball. Usa un espai de treball descartable i prova els serveis amb registres sintètics.

| Prova | Evidència que cal conservar |
|---|---|
| **Enviament interromput** | Un efecte extern després de la recuperació |
| **Conversa llarga** | Els requisits originals encara es compleixen |
| **Acció rebutjada** | Cap efecte a través d'una eina alternativa |
| **Instrucció no fiable en un document** | El text del document no obté autoritat |
| **Arguments d'eina mal formats** | Rebuig abans de mutar l'aplicació |
| **Esgotament del pressupost** | Aturada limitada amb treball parcial inspeccionable |

**Defineix la repetició explícitament.** Per a un servei de sol·licituds de reemplaçament, atura el worker després que el servei de prova accepti una sol·licitud però abans de desar la finalització local. En reiniciar, el flux ha de cercar l'identificador d'operació en lloc d'enviar de nou a cegues. És una prova proposada, no un resultat observat dels productes llistats.

**Comprova l'evidència després de la compactació.** Posa un requisit important al principi de la tasca i després aporta material realista suficient per activar l'estratègia de context configurada. Demana a l'agent l'artefacte final i les referències de fonts. La nostra [anàlisi de CLM i memòria d'agents](/articles/context-language-models-agent-memory-hallucinations/) explica per què conservar notes i conservar evidència exacta són qüestions diferents.

**Revisa les destinacions de la telemetria.** Les traces d'eines i els stores de memòria sovint contenen dades de tasques. Registra quins sistemes les reben i quant de temps estan disponibles. La inferència amb un model local no implica registre, recuperació o execució només locals.

## Compara el cost per tasca acceptada

**Usa dues línies d'avaluació.** Una comparació controlada manté constants el model, les eines, el conjunt de tasques i els pressupostos quan hi ha suport. Una comparació de desplegament usa la configuració prevista de cada candidat. La primera aïlla alguns efectes del programari. La segona respon quin muntatge complet serveix millor la teva feina.

**No forcis configuracions no compatibles en la línia controlada.** Si dos candidats no comparteixen model o interfície d'eines, presenta la comparació com una avaluació del sistema. Conserva en el registre l'esforç de configuració i la direcció humana.

```yaml
# Illustrative trial record, not a framework configuration file
candidate: "package and pinned version"
model: "provider and exact model identifier"
workspace: "isolated test environment"
task_set: "frozen fixtures and acceptance checks"
limits:
  elapsed_minutes: 15
  model_calls: 30
  tool_calls: 60
record:
  - accepted_result
  - unsupported_claims
  - duplicate_external_actions
  - inference_cost
  - infrastructure_cost
  - human_review_minutes
  - recovery_outcome
```

**Executa diverses proves per tasca.** Mantén els intents fallits al denominador i informa dels recomptes bruts juntament amb els percentatges. Una prova petita mostra patrons d'error, no una classificació estable de la indústria.

**Càlcul de costos il·lustratiu:** suposa que la configuració A gasta 12 dòlars en deu intents i produeix vuit resultats acceptats. El cost d'inferència per tasca acceptada és d'1,50 dòlars. La configuració B gasta 8 dòlars però produeix quatre resultats acceptats, així que el cost corresponent és de 2,00 dòlars. Cap xifra inclou revisió humana o infraestructura. Formen part d'un total registrat separat.

**Defineix els errors desqualificadors abans de provar.** Un enviament no autoritzat o una filtració de dades entre usuaris no ha de desaparèixer dins d'una puntuació mitjana de qualitat. Després d'imposar aquests requisits, compara correcció, recuperació, esforç de revisió i cost.

## Pren una decisió limitada

**Comença amb dos candidats i un flux real.** Per a un agent assemblat i flexible amb el proveïdor, compara Deep Agents amb una alternativa més estreta adequada a la teva aplicació. Per al comportament de Claude Code dins d'un servei, prova Claude Agent SDK. Per a aplicacions tipades, compara Pydantic AI amb OpenAI Agents SDK. Tria Pi quan el comportament personalitzat justifiqui més integració, i LangGraph quan el control explícit del flux sigui la prioritat.

**Requisits previs de la prova:** accés aprovat al model, fixtures sintètiques, espai de treball aïllat quan calgui i criteris d'acceptació escrits. Reserva la primera tarda per a la configuració i proves bàsiques d'errors, després recull execucions repetides abans de decidir en producció. La dificultat és intermèdia o avançada segons les accions externes i els requisits de recuperació.

**Selecciona el sistema més petit que compleixi els requisits.** Conserva les fixtures, versions dels paquets i registres d'errors de la prova. Repeteix-los quan canviïs el model, l'estratègia de context, les eines o el backend d'execució. Aquests canvis modifiquen el sistema avaluat.

## Referències

- [LangChain: visió general de Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview)
- [Anthropic: visió general de Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)
- [Anthropic: desplegament segur](https://code.claude.com/docs/en/agent-sdk/secure-deployment)
- [OpenAI: Agents SDK](https://openai.github.io/openai-agents-python/)
- [OpenAI: execució human-in-the-loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [OpenAI: integració de models i proveïdors](https://openai.github.io/openai-agents-python/models/)
- [Pydantic: visió general del framework d'IA](https://pydantic.dev/docs/ai/overview/)
- [Pydantic: AI Harness](https://pydantic.dev/docs/ai/harness/)
- [Earendil: SDK d'agent de programació Pi i modes d'integració](https://github.com/earendil-works/pi/tree/main/packages/coding-agent)
- [LangChain: persistència de LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence)
