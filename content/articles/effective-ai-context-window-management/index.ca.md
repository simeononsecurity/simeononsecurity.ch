---
title: "Gestió de la finestra de context de la IA: mantén centrats els agents de programació"
description: "Controla el context actiu d’una tasca d’IA amb fitxers seleccionats, traspassos breus i sortides petites dels treballadors, tot preservant decisions i evidències."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Intel·ligència artificial", "Enginyeria del programari"]
tags: ["gestió del context d’IA", "context d’agent de programació", "traspàs d’IA", "compactació del context", "orquestració d’agents", "pressupost de tokens"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Una nota breu de traspàs al costat de fitxers seleccionats del projecte i una transcripció de xat molt més extensa descartada"
coverCaption: ""
---

[Torna al Curs pràctic de fluxos de treball amb IA](/effective-ai-course-start/)

**La finestra de context és el text i la resta de material que un model processa durant el torn actual.** Les instruccions, les definicions d’eines, els fragments de fitxers, les sortides de les eines i l’historial del xat consumeixen espai. Aquesta lliçó t’ajuda a centrar la tasca següent i a deixar un traspàs fiable.

**Objectiu d’aprenentatge:** preparar un traspàs breu i provar-lo en una sessió nova.

## Idees clau

- **Tokens:** unitats que el model fa servir per processar l’entrada i la sortida.
- **Context actiu:** material disponible durant un torn, dins dels límits del producte.
- **Fonts persistents:** fitxers o registres del projecte fora del xat.
- **Compactació:** resumeix o retalla el context antic i pot ometre detalls necessaris.
- **Traspàs:** indica a una sessió nova les fonts actuals i la feina verificada.

## Abans de començar

**Requisits previs:** el laboratori editat de la [primera tasca amb un agent de programació](/articles/effective-ai-coding-agent-first-task/), el seu requisit aprovat i la [lliçó sobre paquets de tasques](/articles/effective-ai-task-packets/). Si has seguit la ruta d’estudi, fes servir el laboratori que has editat manualment. Reserva 35 minuts. La dificultat és intermèdia. Desa les notes del curs fora de la carpeta del laboratori extret perquè `git status` només mostri canvis de codi.

## Tria el context segons la tasca

**Per editar el filtre d’estat,** l’agent necessita `task_report.py`, `docs/requirements.md`, les proves pertinents i una mostra petita de `tasks.json`. No necessita tots els xats antics, tota la documentació del lloc ni tot l’historial de Git. Consulta primer un mapa i després carrega només els fitxers necessaris per prendre la decisió següent.

| Tasca | Context útil | Context sobrer |
|---|---|---|
| **Definir el comportament** | Requisit aprovat i una mostra de dades | Converses exploratòries antigues |
| **Editar el programa** | Programa i proves focalitzades | Directoris de projectes no relacionats |
| **Revisar el resultat** | Diferències, sortida de proves i requisit | Transcripció completa de l’agent |
| **Reprendre més tard** | Nota de traspàs i rutes de les fonts | Un xat de diverses hores enganxat sencer |

**Això és una decisió de recuperació, no una regla per amagar proves.** Si falla una prova, inclou la sortida exacta i el fitxer implicat. Elimina registres irrellevants, no els detalls necessaris per diagnosticar l’error.

**Compta la despesa fixa abans d’afegir treballadors.** Les instruccions de l’agent i els esquemes d’eines disponibles poden ocupar context abans de llegir cap fitxer de tasca. Un segon treballador repeteix part d’aquesta despesa i afegeix un informe que l’agent principal ha de revisar. Per editar dos fitxers, fes servir un agent. Per cercar de manera independent en moltes fonts, un informe breu pot reduir el context de la sessió principal encara que augmenti el consum total de tokens.

## Prepara un traspàs breu

**Un traspàs és un registre curt per a la sessió següent.** Ha de distingir la feina acabada de la proposada. Desa aquest exemple com a `course-notes/handoff.md`, fora del laboratori, i substitueix les observacions d’exemple per les teves.

```text
Objectiu: afegir --status open|done a l’informe de tasques del curs.
Font: docs/requirements.md, revisió 1.
Espai de treball: carpeta effective-ai-course-lab extreta.
Estat actual: el filtre d’estat és a task_report.py i a les proves.
Verificat: anota el resultat observat de les proves i els recomptes manuals 4, 2 i 2.
Decisió: tasks.json no s’ha modificat.
Pendent: revisió independent del diff i de la font.
Comprovació següent: torna a executar les proves i el cas d’estat no vàlid.
Atura’t si: el requisit o la línia de base difereixen d’aquest registre.
```

**L’exemple no afirma que hagis fet aquesta feina.** Anota els resultats observats de les proves i els fitxers modificats. Si canvia la revisió de la font, actualitza el traspàs després de tornar-la a llegir.

## Prova una sessió nova

**Inicia un xat o una sessió nova d’agent de programació** al laboratori. En un xat, enganxa el traspàs i l’`AGENTS.md` del laboratori sintètic, i indica els fitxers que ha d’inspeccionar. En un agent de programació, obre la carpeta del laboratori i enganxa el traspàs amb accés de lectura als fitxers indicats. Demana:

```text
Amb aquest traspàs i els fitxers actuals del repositori, indica els valors d’estat aprovats, el recompte de base i la comprovació següent. No editis.
Si el traspàs contradiu una font actual, informa’n.
```

**Raonament esperat:** la sessió nova troba `open` i `done` a `docs/requirements.md`, identifica el recompte inicial de 4 i indica les proves i les comprovacions manuals. Si repeteix el valor antic `pending`, torna a llegir el requisit i corregeix el traspàs.

## Mantén petit l’orquestrador

**Un orquestrador és l’agent principal que coordina treballadors.** Assigna a cada treballador una pregunta acotada i fitxers d’entrada concrets. Demana una resposta breu: troballa, ruta de l’evidència, confiança i qüestió pendent. Desa els registres detallats en un fitxer o a la sessió del treballador. Retorna només el que l’agent principal necessita per decidir el pas següent.

**Exemple:** demana a un treballador de només lectura que revisi les proves i respongui «cas absent, fitxer i línia, comprovació suggerida». No li demanis que enganxi totes les proves al xat principal. L’agent principal verifica la troballa al repositori abans d’editar. La [lliçó sobre delegació](/articles/effective-ai-agent-delegation/) afegeix una tasca independent quan l’abast justifica el cost.

**Les sessions dels treballadors tenen el seu propi context en molts productes,** però la herència i l’aïllament varien. Consulta les regles actuals del producte abans de suposar que un treballador veu les mateixes instruccions, fitxers o eines que l’agent principal. Les guies de [subagents de Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents) i [subagents de Claude Code](https://code.claude.com/docs/en/sub-agents) descriuen el comportament de cada producte.

## Fes servir la compactació amb cura

**La compactació escurça l’historial actiu.** Codex, Claude Code i OpenCode difereixen en quan i com compacten. Tracta un resum compactat com una ajuda per continuar, no com un registre complet del projecte. Desa els requisits i les decisions en fitxers i torna’ls a comprovar després de compactar. Consulta les guies actuals sobre [bones pràctiques de Codex](https://learn.chatgpt.com/docs/learn/best-practices), [ordres de Claude Code](https://code.claude.com/docs/en/commands) i [compactació d’OpenCode 2](https://opencode.ai/v2/docs/compaction). OpenCode 1 i OpenCode 2 fan servir esquemes diferents. Comprova `opencode --version` abans de copiar la configuració.

**Si l’assistent perd una restricció,** atura l’edició, torna a obrir la font i repeteix el paquet de tasques. Sovint una sessió nova amb un traspàs breu i verificat requereix menys atenció que corregir repetidament un xat llarg confús.

## Practica i comprova

**El teu artefacte:** un traspàs de menys de 180 paraules, desat fora del laboratori. Marca cada línia com a font, resultat observat, decisió o acció pendent. Dona’l a una sessió nova i anota si identifica els dos valors d’estat acceptats i la comprovació següent.

**Comprovació final:** la sessió nova indica `open`, `done`, el recompte inicial de 4 i un pas de prova sense dependre del xat antic. Corregeix qualsevol omissió i torna-ho a provar amb una altra sessió nova.

## Comprova què has après

1. **Pregunta:** què ha d’incloure un traspàs per a una sessió nova? **Resposta:** l’objectiu, la font autoritzada, l’estat actual, el resultat comprovat i l’acció següent.

2. **Pregunta:** per què convé que l’informe del treballador sigui breu? **Resposta:** un informe concís amb evidències dona a l’orquestrador el resultat necessari sense repetir tota la transcripció.

## Resolució de problemes

- **El resum omet una decisió:** afegeix una línia breu amb la decisió i la revisió de la font.
- **La resposta del treballador és enorme:** demana una taula d’evidències limitada i referències als fitxers.
- **El traspàs és antic:** torna a llegir les fonts actuals abans d’editar.
- **Continua faltant context:** divideix la tasca en sessions més petites amb artefactes separats.

## Passos següents

**Continua amb [Configuració del servidor MCP](/articles/effective-ai-mcp-server-setup/)**. Afegiràs una eina externa de només lectura i limitaràs l’abast de la seva sortida.

**Navegació del curs:** [Anterior: Primera tasca de programació](/articles/effective-ai-coding-agent-first-task/), [Índex del curs](/effective-ai-course-start/).
