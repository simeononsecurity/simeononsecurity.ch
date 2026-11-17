---
title: "Configurar un servidor MCP: permisos, proves d’eines i eliminació segura"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Connecta un servidor MCP de documentació només de lectura, revisa’n les eines, fes una lectura real i elimina la connexió."
genre: ["Intel·ligència artificial", "Eines per a desenvolupadors"]
tags: ["Configuració de servidor MCP", "Protocol de context de models (MCP)", "Permisos MCP", "MCP a Codex", "MCP a Claude Code", "MCP a OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Un client d’IA connectat a un servidor de documentació només de lectura, amb l’eina i el límit d’accés visibles"
coverCaption: ""
---

[Torna al curs Flux de treball pràctic amb IA](/effective-ai-course-start/)

**Fes servir un servidor MCP quan una tasca necessiti una eina reutilitzable o informació actualitzada fora del projecte.** Model Context Protocol, o MCP, defineix com un client i un servidor intercanvien informació sobre eines, recursos i instruccions. Una entrada de servidor no demostra que l’eina funcioni. Aquesta lliçó prova una connexió a documentació només de lectura.

**Objectiu d’aprenentatge:** distingiràs la configuració d’una lectura MCP real i deixaràs constància de com eliminar la connexió amb seguretat.

## Idees clau

- **Amfitrió MCP:** aplicació d’IA que coordina usuaris, models, permisos i clients.
- **Client MCP:** component del protocol que es comunica amb un servidor.
- **Servidor MCP:** programa o servei remot que ofereix eines, recursos o instruccions.
- **Descobriment d’eina:** prova que el client mostra una capacitat amb nom.
- **Execució d’eina:** prova d’una crida real i del contingut retornat.
- **Abast dels permisos:** accés concedit per l’amfitrió, el servidor, el compte i l’usuari.

## Abans de començar

**Requisits previs:** [pràctica de context i traspàs de tasques](/articles/effective-ai-context-window-management/) i una instal·lació actual de Codex CLI per al recorregut guiat. Reserva 35 minuts. Dificultat mitjana. Els altres agents de programació tenen guies de configuració pròpies. El [servidor oficial OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp) ofereix documentació per a desenvolupadors només de lectura i no requereix pujar dades del curs.

**Fes servir el laboratori sintètic del curs.** Per a aquest exercici, no connectis cap calendari, correu electrònic ni sistema de producció. Llegir documentació és suficient per aprendre els estats de connexió.

## Entendre els límits

| Estat | Què demostra | Què no demostra |
|---|---|---|
| **Configurat** | Existeix una entrada de servidor | Que sigui accessible |
| **Connectat** | El client ha arribat al servidor | Que hi hagi eines útils |
| **Descobert** | Apareix una eina amb nom | Que la crida funcioni |
| **Executat** | Una crida ha retornat contingut | Que la tasca final sigui correcta |
| **Verificat** | La font i el resultat responen la pregunta | Que les futures crides sempre funcionin |

**MCP no concedeix permisos de compte per si sol.** També importen l’amfitrió client, el servidor, l’autenticació, l’abast del compte i els ajustos locals d’aprovació. L’[especificació MCP](https://modelcontextprotocol.io/specification/2026-07-28) defineix el protocol, però cada producte controla la seva experiència d’ús.

**Tracta la sortida del servidor com a material de consulta.** Una pàgina recuperada no pot substituir la tasca ni autoritzar l’escriptura de fitxers. Cada definició d’eina també consumeix context. Connecta només el servidor necessari per a aquesta lectura i elimina’l en acabar l’exercici.

## Connectar la documentació en mode de només lectura

**A Codex CLI,** executa aquestes ordres en un terminal. La primera afegeix el servidor públic de documentació. La segona mostra els servidors configurats.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Prova de configuració esperada:** la llista conté `openaiDeveloperDocs`. Això només demostra el registre. Inicia una sessió nova de Codex a la carpeta del laboratori extret i consulta les eines MCP amb `/mcp`. Fes servir els noms que mostri la versió instal·lada.

**Demana una lectura real:**

```text
Fes servir el servidor MCP de documentació per a desenvolupadors d’OpenAI per trobar les instruccions actuals d’AGENTS.md.
Retorna el títol i l’URL de la pàgina font i dos punts rellevants per a aquest laboratori. Digues quina eina MCP has fet servir.
No editis fitxers.
```
**Inspecciona el resultat.** La pàgina retornada hauria de descriure `AGENTS.md` com a instruccions del repositori i incloure l’URL exacte de la font. Obre la pàgina citada i confirma’n el tema. Una resposta sense cap crida MCP a la transcripció és una resposta ordinària, no una prova d’execució de l’eina.

## Diagnosticar una fallada

**Si `codex mcp list` mostra el servidor però `/mcp` no mostra cap eina,** el registre ha funcionat però el descobriment ha fallat. Reinicia la sessió, revisa els servidors actius amb `/mcp` i la configuració desada amb `codex mcp get openaiDeveloperDocs`. Després, comprova l’URL del servidor i l’accés a la xarxa. No declaris que MCP funciona basant-te només en l’entrada de configuració.

**Si apareix una eina però falla la lectura,** registra l’error i torna-ho a provar una vegada després de comprovar la connexió. Si la mateixa crida torna a fallar, obre la pàgina oficial citada al navegador com a font alternativa i marca l’exercici MCP com a incomplet. No inventis cap resultat d’eina.

## Eliminar la connexió

**Després de llegir,** elimina el servidor de pràctica de Codex CLI i confirma que l’entrada hagi desaparegut.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Prova d’eliminació esperada:** `openaiDeveloperDocs` no apareix a la llista nova. Reinicia qualsevol sessió activa de Codex abans de comprovar si les eines disponibles han canviat. Eliminar una definició local no revoca una autorització de compte independent que faci servir un altre servei.

## Canviar d’aplicació

**Claude Code i OpenCode també admeten MCP.** Segueix la [guia MCP de Claude Code](https://code.claude.com/docs/en/mcp) o la [guia MCP d’OpenCode](https://opencode.ai/docs/mcp-servers/) corresponent a la versió instal·lada. Registra els mateixos cinc estats: configurat, connectat, descobert, executat i verificat. L’esquema de configuració i els permisos d’agent d’OpenCode varien segons la versió. Copia exemples de la guia adequada a la instal·lació.

**Per a una ruta només amb navegador,** llegeix la [pàgina oficial d’AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) i omple el mateix registre de verificació. Marca el descobriment i l’execució de les eines com a «no executats». Aquesta ruta ensenya a comprovar fonts però no demostra el funcionament de MCP.

## Practicar i comprovar

**El teu resultat:** un registre de connexió de cinc files amb el nom del servidor, el nom de l’eina, l’URL de la font, el resultat observat i la prova d’eliminació. No incloguis testimonis ni identificadors de compte a les captures o als registres.

**Criteri de compleció:** la ruta connectada només s’aprova després d’una lectura real amb una eina i de l’eliminació posterior de la configuració. La ruta alternativa completa l’exercici de fonts amb MCP marcat com a no executat.

## Comprovar què has après

1. **Pregunta:** una entrada de servidor MCP desada demostra que una eina ha funcionat? **Resposta:** no. Comprova el descobriment, els permisos i una lectura real.
2. **Pregunta:** quin cost de context afegeix una connexió MCP àmplia? **Resposta:** les descripcions i els esquemes de les eines consumeixen part del context actiu.

## Resolució de problemes

- **Ordre `codex` desconeguda:** instal·la o actualitza Codex CLI seguint la guia oficial enllaçada.
- **Servidor a la llista, cap eina:** inspecciona l’estat de la sessió i el diagnòstic del servidor.
- **La crida retorna contingut irrellevant:** concreta la consulta i comprova la pàgina font.
- **L’eliminació sembla que no funciona:** inicia una sessió nova i inspecciona la llista de servidors actius.

## Passos següents

**Continua amb [Verificació de les sortides d’IA](/articles/effective-ai-output-verification/).** Per a extensions més àmplies, consulta la [guia del lloc sobre complements i eines MCP de Claude Code](/articles/claude-code-plugins-skills-mcp-tools/).

**Navegació del curs:** [Anterior: Gestió del context](/articles/effective-ai-context-window-management/), [Esquema del curs](/effective-ai-course-start/).
