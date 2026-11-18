---
title: "Delegació d’agents d’IA: assignar treballadors i revisar resultats"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Decidiu quan ajuda un segon agent d’IA, assigneu una tasca delimitada a cada treballador, eviteu conflictes d’edició i integreu les proves a la sessió principal."
genre: ["Intel·ligència artificial", "Enginyeria del programari"]
tags: ["delegació d’agents d’IA", "subagents", "agents treballadors", "context de l’orquestrador", "arbres de treball d’IA", "tasques d’IA en paral·lel"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Un agent principal assigna tasques independents de recerca i revisió de proves abans d’unir informes breus d’evidències"
coverCaption: ""
---

[Torna al curs pràctic de flux de treball amb IA](/effective-ai-course-start/)

**Delega quan una pregunta independent justifica una sessió separada.** Un agent treballador inspecciona fonts, revisa proves o prepara un canvi delimitat dins del seu context. L’agent principal comprova i integra el resultat. Aquesta lliçó compara documentació mentre la sessió principal conserva la tasca petita del laboratori.

**Objectiu d’aprenentatge:** assignaràs una revisió independent a un treballador i verificaràs el seu informe breu d’evidències.

## Idees clau

- **Orquestrador:** agent principal que coordina la tasca i la revisió final.
- **Treballador:** agent separat amb un únic resultat delimitat.
- **Treball independent:** subtasca la resposta de la qual no depèn d’un resultat inacabat d’un altre treballador.
- **Propietat:** fitxer o pregunta concret assignat a un sol treballador.
- **Integració:** comparació que fa l’agent principal del resultat amb les fonts actuals.

## Abans de començar

**Prerequisits:** els teus registres de [traspàs de context](/articles/effective-ai-context-window-management/) i [verificació de sortida](/articles/effective-ai-output-verification/). Reserva 40 minuts. Dificultat intermèdia. La ruta connectada requereix un producte amb suport per a treballadors. La ruta d’estudi utilitza un xat separat i integració manual.

**Comença amb una còpia neta per a aquesta lliçó.** Desa fora del laboratori el diff del filtre editat i el registre de proves. Extreu el ZIP original en una carpeta temporal nova. Executa l’ordre d’inici i les dues proves de referència. Repeteix la base de Git de la lliçó de configuració del curs i recrea les instruccions breus `AGENTS.md` i l’opcional `CLAUDE.md` de la lliçó sobre el context del repositori. Fes tu mateix el commit d’aquests fitxers i confirma que `git status --short` no mostra canvis. Conserva la còpia del filtre editat com a referència, però fes l’exercici del treballador amb l’iniciador net.

## Decideix si cal delegar

**Utilitza un agent** per a una edició seqüencial petita. Delegar té costos de configuració, tokens i revisió. Utilitza un treballador quan una pregunta de només lectura sigui independent i la seva resposta ompliria el xat principal amb molts fitxers o pàgines de fonts.

| Tasca del laboratori | Delegar? | Motiu |
|---|---|---|
| **Afegir un filtre de dos valors** | Normalment no | Un fitxer petit i proves focalitzades |
| **Trobar casos absents en dues proves base** | Normalment no | La sessió principal llegeix més ràpid un fitxer curt |
| **Comparar la documentació actual de tres productes** | Sí, només lectura | La lectura de fonts queda al context del treballador |
| **Editar dues vegades la mateixa funció** | No | Les edicions simultànies creen conflictes |

**El treballador ha de rebre menys context que l’orquestrador,** no una còpia de tota la conversa. Dona-li l’objectiu, el camí de la font, els límits de la tasca i el format de resposta. Conserva un informe breu d’evidències a la sessió principal. Inspecciona tu mateix els fitxers citats abans d’actuar.

## Executa un treballador de només lectura

**Mantén petita la tasca principal.** A la sessió principal, llegeix l’`AGENTS.md` local i anota quin fitxer conté l’ordre de prova. Assigna la pregunta de recerca separada següent a un treballador. No necessita tot el laboratori ni el xat anterior.

**Ruta connectada:** a Codex, Claude Code o un altre client que admeti treballadors, obre el laboratori com a projecte i demana a l’agent principal que delegui la petició de només lectura següent a un treballador. Comprova al registre d’eines que un treballador real ha començat i ha retornat l’informe. Si el producte no exposa cap treballador, utilitza una sessió separada i identifica-la com una sessió de treballador separada. Les guies actuals de [subagents de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [subagents de Claude Code](https://code.claude.com/docs/en/sub-agents) i [agents d’OpenCode](https://opencode.ai/docs/agents/) descriuen els controls disponibles.

**Ruta d’estudi:** obre un xat nou per a la mateixa petició. Dona-li els tres enllaços oficials o fragments de les fonts. Etiqueta’l com a treballador simulat. Un segon xat és un context separat, no prova que s’hagi executat un subagent natiu.

```text
Utilitza la documentació oficial actual de Codex AGENTS.md, Claude Code memory i OpenCode rules.
Compara com carrega cada producte els fitxers d’instruccions del repositori.
No editis fitxers.
Retorna com a màxim tres files: producte, fitxer d’instruccions, URL de la font
 i un comportament de càrrega. Indica la incertesa. No enganxis pàgines senceres.
```

**Conjunt de fonts:** [instruccions de projecte de Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [memòria de Claude Code](https://code.claude.com/docs/en/memory) i [regles d’OpenCode](https://opencode.ai/docs/rules/). L’informe esperat cita `AGENTS.md` per a Codex i OpenCode. Les versions actuals de Claude Code també carreguen `AGENTS.md` directament quan cap `CLAUDE.md` o `CLAUDE.local.md` no té prioritat. Aquest laboratori utilitza un fitxer `CLAUDE.md` amb una importació `@AGENTS.md`, que també funciona amb sessions anteriors o configurades d’una altra manera. Comprova les pàgines actuals i la versió activa abans de presentar aquest exemple com un resultat observat d’un treballador.

## Integra els resultats

**Obre tu mateix les pàgines de fonts citades.** Si el treballador afirma que Claude Code sempre necessita importar `CLAUDE.md`, comprova la guia de memòria i corregeix l’informe. Compara’l amb els fitxers d’instruccions locals. Escriu una nota breu d’integració:

```text
Acceptat: Codex i OpenCode utilitzen AGENTS.md com a instruccions del projecte.
Les versions actuals de Claude Code poden carregar AGENTS.md directament. Aquest laboratori
utilitza CLAUDE.md amb una importació @AGENTS.md per mantenir un mapa compartit estable.
Proves: anota les tres URL oficials actuals i la data de revisió.
Decisió: conserva un mapa compartit breu i una importació de Claude.
```

**Aquesta nota és el resultat útil del treballador.** L’orquestrador necessita resultats verificats i camins de les fonts, no la transcripció de recerca. Delegar consumeix més tokens en total, així que mantén més petita la conversa principal només quan la sessió separada estalviï atenció.

## Assigna la propietat de les edicions

**Si els treballadors editen fitxers,** divideix la propietat per fitxer o utilitza arbres de treball separats per a tasques de repositori que se superposin. Un arbre de treball és una altra còpia del mateix repositori Git, amb fitxers de treball propis. Ajuda a separar edicions simultànies. L’agent principal revisa i transfereix els canvis amb un merge, cherry-pick o pedaç explícit, i després torna a executar les proves a l’arbre integrat.

| Treballador | Tasca assignada | Resultat |
|---|---|---|
| **Implementació** | `task_report.py` | Diff i ordre de prova |
| **Autor de proves** | `tests/test_task_report.py` | Casos de prova i resultat observat |
| **Orquestrador** | Requisits i integració final | Diff combinat i criteris d’acceptació |

**El laboratori petit no necessita edicions en paral·lel.** Aquesta taula ensenya un patró de propietat per a feines més grans. Les proves d’un arbre no validen una implementació que encara és aïllada en un altre. Si dos treballadors necessiten la mateixa funció, treballa en sèrie o demana a un que revisi sense editar. Els arbres separats eviten col·lisions de fitxers, però no resolen requisits contradictoris.

## Comprova el comportament del producte

**Els subagents varien segons l’amfitrió.** Codex, Claude Code i OpenCode tenen maneres diferents d’heretar context, permetre eines i lliurar resultats. Llegeix la guia de [subagents de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), de [subagents de Claude Code](https://code.claude.com/docs/en/sub-agents) i d’[agents d’OpenCode](https://opencode.ai/docs/agents/) per al producte instal·lat. No donis per fet que un treballador comparteix tota la conversa principal ni que té un arbre de treball aïllat.

## Practica i comprova

**Resultat:** un informe breu d’un treballador de documentació i una nota d’integració. A la ruta d’estudi, utilitza un xat nou i identifica’l com a treballador simulat. No afirmis que s’ha executat un subagent natiu en aquesta ruta.

**Comprovació final:** l’informe cita tres fonts oficials, es limita a la seva pregunta i respecta el límit de llargada. La nota d’integració comprova les fonts i identifica els fitxers d’instruccions del laboratori.

## Comprova la comprensió

1. **Pregunta:** Quan ajuda més un treballador que un únic agent? **Resposta:** Quan s’encarrega d’una pregunta o resultat independent i lliura un informe d’evidències útil.

2. **Pregunta:** Què ha de passar després que dos treballadors toquin fitxers coincidents? **Resposta:** Integra els canvis, inspecciona el diff combinat i torna a executar les comprovacions.

## Resolució de problemes

- **El treballador retorna una transcripció llarga:** demana una taula d’evidències més curta amb referències als fitxers.
- **Els treballadors discrepen:** torna a llegir el fitxer autoritatiu abans d’escollir una resposta.
- **Dues edicions se superposen:** atura una edició i estableix la propietat dels fitxers o separa els arbres de treball.
- **L’accés a eines del treballador és diferent:** inspecciona els seus permisos en lloc de suposar que coincideixen amb els del pare.

## Passos següents

**Continua amb [bucles d’objectius delimitats](/articles/effective-ai-bounded-agent-loops/).** Per a la governança d’equip més enllà d’aquest laboratori, utilitza el [curs d’implementació de col·laboració amb IA](/ai-collaboration-course-start/).

**Navegació del curs:** [Anterior: verificació de sortida](/articles/effective-ai-output-verification/), [Esquema del curs](/effective-ai-course-start/).
