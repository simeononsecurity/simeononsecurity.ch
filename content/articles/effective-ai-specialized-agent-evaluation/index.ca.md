---
title: "OpenClaw i Hermes Agent: una avaluació pràctica"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Avalua agents d’IA especialitzats i persistents amb un inventari d’accessos, una revisió dels activadors, un registre del flux de dades i una decisió sobre la prova pilot."
genre: ["Intel·ligència artificial", "Enginyeria de programari", "Productivitat"]
tags: ["agents d’IA especialitzats", "OpenClaw", "Hermes Agent", "agents de treball", "avaluació d’agents d’IA", "agents d’IA persistents"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Full de treball amb les eines, la memòria desada, els activadors, els registres i la decisió de revisió d’un agent"
coverCaption: ""
---

[Torna al curs pràctic sobre fluxos de treball amb IA](/effective-ai-course-start/)

**Tria un agent especialitzat segons la tasca i els accessos que necessita.** Un agent de treball que revisa un fitxer és diferent d’un sistema persistent que rep missatges, desa memòria i executa accions programades. Aquesta lliçó opcional utilitza OpenClaw i Hermes Agent com a exemples i després ofereix un full d’avaluació previ a la instal·lació.

**Objectiu d’aprenentatge:** compararàs els accessos i activadors dels agents i registraràs una decisió per a una prova pilot limitada.

## Idees clau

- **Agent de treball amb un rol concret:** agent assignat a una pregunta o un artefacte.
- **Agent persistent:** servei o sessió que manté l’estat o respon a activadors posteriors.
- **Activador:** esdeveniment, missatge o programació que inicia la feina.
- **Inventari d’accessos:** llista d’eines, comptes, fitxers i permisos d’escriptura que rep l’agent.
- **Decisió pilot:** rebutjar, fer una prova limitada o aprovar un ús definit.

## Abans de començar

**Prerequisits:** [delegació](/articles/effective-ai-agent-delegation/), [bucles d’agent delimitats](/articles/effective-ai-bounded-agent-loops/) i un cas d’ús fictici. Reserva 35 minuts. El nivell és intermedi. Aquesta lliçó no requereix instal·lar un agent persistent.

**Cas d’ús:** una persona que coordina un taller vol que un assistent llegeixi un horari i prepari un esborrany de recordatori. La petició no autoritza a enviar-lo. La teva avaluació ha de mantenir aquest límit.

## Contrasta els rols

| Enfocament | Tipus de tasca habitual | Primera pregunta |
|---|---|---|
| **Un xat** | Redactar un recordatori | L’horari està disponible? |
| **Agent de només lectura** | Verificar les dades de l’horari de manera independent | Quina font ha de llegir? |
| **Agent de programació** | Actualitzar un programa local d’informes | Quins fitxers i proves s’hi apliquen? |
| **Plataforma persistent** | Respondre a missatges o horaris al llarg del temps | Quins activadors, eines i estats desats hi ha? |

**OpenClaw** és una plataforma d’agents de codi obert amb passarel·la, canals de missatgeria, eines, memòria, connexions MCP i subagents. L’[introducció](https://docs.openclaw.ai/start/why-openclaw), la [guia de connexió MCP](https://docs.openclaw.ai/tools/mcp) i la [guia de subagents](https://docs.openclaw.ai/tools/subagents) descriuen aquests components. Abans d’un pilot, revisa els paràmetres actius dels canals, les eines i l’entorn aïllat.

**Hermes Agent** és l’aplicació d’agents de Nous Research. La família de models Hermes és una altra cosa. La [documentació](https://hermes-agent.nousresearch.com/docs/), la [guia de delegació](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) i la [guia de configuració](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) cobreixen CLI, missatgeria, eines, memòria i tasques delegades. La [guia de memòria](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) descriu els magatzems locals i l’aprovació d’escriptures. El valor predeterminat documentat de `memory.write_approval` i `skills.write_approval` és `false`. Activa l’aprovació o desactiva el magatzem pertinent per a un pilot que requereixi revisar les escriptures. Comprova la configuració activa abans de confiar en qualsevol dels controls.

| Punt d’avaluació | OpenClaw | Hermes Agent |
|---|---|---|
| **Punt d’entrada** | Passarel·la i canals connectats | CLI o interfície de missatgeria configurada |
| **Feina delegada** | Subagents amb normes de sessió i d’eines pròpies de la plataforma | Tasques delegades amb normes d’eines pròpies de la plataforma |
| **Estat persistent** | Revisa la memòria activada i l’emmagatzematge de sessions | Revisa la memòria, els perfils i les escriptures de les habilitats |
| **Feina recurrent** | Revisa els activadors i les programacions configurats | Revisa les [tasques cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) i l’estat de la passarel·la |
| **Primer pilot** | Una petició manual per un canal seleccionat | Una petició manual per CLI o missatgeria |

La taula enumera punts de revisió, no pas valors de seguretat equivalents. Anota la versió instal·lada i la configuració activa abans de donar accés a dades o comptes reals.

**Els noms no defineixen un model de permisos comú.** Un «subagent» d’un producte pot rebre fitxers, eines i historial diferents dels d’un agent de treball d’un altre producte. Consulta la documentació de la versió instal·lada i els paràmetres actius, sense traslladar supòsits d’una eina a l’altra.

## Omple un full d’accessos

**Afegeix una fila per cada capacitat** abans d’instal·lar o connectar un sistema. Si tens el producte disponible, fes servir els paràmetres reals. Escriu «desconegut» en lloc d’endevinar.

| Pregunta | Resposta per al pilot del taller |
|---|---|
| **Tasca** | Redactar un recordatori a partir d’un horari sintètic |
| **Entrada** | Un fitxer d’horari aprovat |
| **Fitxers** | Llegir el fitxer d’horari, sense permís d’escriptura |
| **Eines externes** | Cap per al primer pilot |
| **Accés als comptes** | Cap compte de correu ni de calendari |
| **Activador** | Només una petició manual |
| **Escriptures de memòria i habilitats** | Anota els paràmetres actius, desactiva els magatzems o exigeix aprovació d’escriptura durant el pilot |
| **Registres** | Anota la ruta d’emmagatzematge, la regla de retenció, la instrucció, la revisió de la font i l’esborrany |
| **Revisió** | Una persona comprova la data, l’hora, el lloc i la llista de destinataris |
| **Reversió** | Descarta l’esborrany i desactiva el pilot |

**El flux de dades forma part del full.** Indica on surten les dades del teu ordinador, quin proveïdor les processa i on persisteixen les transcripcions o la memòria. Si una eina es connecta al correu, documenta si llegeix, redacta o envia. Són permisos diferents.

## Decideix si fas la prova

**Rebutja:** l’agent necessita permisos amplis d’escriptura a la bústia per a una tasca que només demana un esborrany, o bé els activadors i els registres són desconeguts. No cal instal·lar res per rebutjar una opció inadequada.

**Prova:** limita l’entrada a l’horari sintètic, utilitza un activador manual, desactiva l’enviament i revisa un esborrany. El resultat esperat és una hora correcta, les 19.00, i cap missatge enviat. Si fas el pilot, anota la teva observació.

**Aprova un ús definit:** només després que el pilot superi les comprovacions i la persona responsable accepti els accessos, l’activador, la retenció i els passos de revisió exactes. Aprovar la redacció no aprova l’enviament ni l’automatització posterior.

## Diagnostica un error

**Suposa que l’esborrany del recordatori indica les 18.00.** Comprova si l’agent ha llegit l’horari actual o si una memòria desada o un missatge antic li ha proporcionat l’hora obsoleta. Substitueix l’entrada obsoleta, repeteix un pilot manual i mantén l’enviament desactivat. Un segon esborrany correcte no esborra el primer error del registre.

**Suposa que hi ha una connexió MCP als paràmetres, però no es pot accedir a cap eina.** Torna als [estats de connexió MCP](/articles/effective-ai-mcp-server-setup/). Una entrada de servidor desada no demostra que la lectura hagi funcionat.

## Practica i comprova

**El teu resultat:** un full d’accessos complet i una decisió: Rebutja, Prova o Aprova un ús definit. Indica un activador, un límit de permisos, una pregunta sobre el flux de dades i una manera d’aturar l’agent.

**Comprovació final:** una altra persona ha de saber quina acció fa l’agent, què llegeix i desa, quan s’executa, qui revisa el resultat i com desactivar-lo. Si no saps alguna resposta, tria Rebutja o una prova més limitada.

## Comprova què has entès

1. **Pregunta:** una tasca que només redacta un recordatori necessita permís per enviar correu? **Resposta:** No. L’enviament queda fora de l’abast del pilot.
2. **Pregunta:** quins paràmetres d’Hermes cal revisar abans d’un pilot amb escriptures controlades? **Resposta:** Comprova els paràmetres actius d’escriptura de memòria i habilitats, inclosos els controls d’aprovació.

## Passos següents

**Continua amb el [projecte final del flux de treball amb IA](/articles/effective-ai-capstone/)**. Per comparar més entorns d’execució, consulta la [guia d’entorns d’agents](/articles/best-ai-agent-harnesses/).

**Navegació del curs:** [Anterior: Bucles delimitats](/articles/effective-ai-bounded-agent-loops/), [Esquema del curs](/effective-ai-course-start/).
