---
title: "AI-contextvenster beheren: houd codeeragents gefocust"
description: "Beheer de actieve context van een AI-taak met geselecteerde bestanden, compacte overdrachten en korte workeruitvoer, met behoud van besluiten en bewijs."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Kunstmatige intelligentie", "Software-engineering"]
tags: ["AI-contextvenster beheren", "context voor codeeragent", "AI-overdracht", "contextcompressie", "agentorchestratie", "tokenbudget"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Een beknopte overdrachtsnotitie naast geselecteerde projectbestanden en een veel groter weggegooid chattranscript"
coverCaption: ""
---

[Terug naar de Praktische AI-werkwijzecursus](/effective-ai-course-start/)

**Het contextvenster bevat de tekst en andere inhoud die een model tijdens de huidige beurt verwerkt.** Prompts, instructies, tooldefinities, bestandsfragmenten, tooluitvoer en gesprekshistorie nemen ruimte in. Deze les laat zien hoe je de volgende taak gericht houdt en een betrouwbare overdracht achterlaat.

**Leerdoel:** maak een beknopte overdracht en test die in een nieuwe sessie.

## Belangrijkste punten

- **Tokens** zijn de eenheden waarmee een model invoer en uitvoer verwerkt.
- **Actieve context** is materiaal dat tijdens één beurt beschikbaar is, binnen de productlimieten.
- **Duurzame bronnen** staan in bestanden of projectregistraties buiten de chat.
- **Contextcompressie** vat oudere context samen of verwijdert die. Een belangrijk detail kan ontbreken.
- **Een overdracht** verwijst een nieuwe sessie naar actuele bronnen en geverifieerd werk.

## Voor je begint

**Vereisten:** je bewerkte lab uit de [eerste taak met een codeeragent](/articles/effective-ai-coding-agent-first-task/), de goedgekeurde eis en de [les over taakpakketten](/articles/effective-ai-task-packets/). Gebruik je het studietraject, neem dan je handmatig bewerkte lab. Reserveer 35 minuten. De moeilijkheidsgraad is gemiddeld. Bewaar cursusnotities buiten de uitgepakte labmap, zodat `git status` alleen codewijzigingen toont.

## Kies context per taak

**Voor de wijziging van het statusfilter** heeft de agent `task_report.py`, `docs/requirements.md`, relevante tests en een klein voorbeeld uit `tasks.json` nodig. Alle oude chats, de volledige sitedocumentatie en de complete Git-geschiedenis zijn overbodig. Bekijk eerst een overzicht en laad daarna alleen de bestanden die nodig zijn voor de volgende beslissing.

| Taak | Nuttige context | Overbodige context |
|---|---|---|
| **Gedrag bepalen** | Goedgekeurde eis en één gegevensvoorbeeld | Oude verkennende gesprekken |
| **Programma aanpassen** | Programma en gerichte tests | Niet-gerelateerde projectmappen |
| **Resultaat controleren** | Diff, testuitvoer, eis | Volledig agenttranscript |
| **Later hervatten** | Overdrachtsnotitie en bronpaden | Een geplakte chat van meerdere uren |

**Dit is een keuze voor het ophalen van informatie, geen regel om bewijs te verbergen.** Neem bij een mislukte test de exacte uitvoer en het betrokken bestand op. Verwijder irrelevante logs, niet de details die nodig zijn om de fout op te sporen.

**Reken vaste overhead mee voordat je workers toevoegt.** Agentinstructies en beschikbare toolschema’s nemen mogelijk al context in voordat een taakbestand is gelezen. Een tweede worker herhaalt een deel daarvan en levert een rapport op dat de hoofdagent moet beoordelen. Gebruik één agent voor een wijziging aan twee bestanden. Bij een onafhankelijke zoekactie door veel bronnen kan een kort werkerrapport de context van de hoofdsessie verkleinen, ook al stijgt het totale tokengebruik.

## Maak een beknopte overdracht

**Een overdracht is een kort verslag voor de volgende sessie.** Maak onderscheid tussen afgerond en voorgesteld werk. Sla dit voorbeeld buiten het lab op als `course-notes/handoff.md` en vervang de voorbeeldwaarnemingen door je eigen resultaten.

```text
Doel: --status open|done toevoegen aan het cursus taakrapport.
Bron: docs/requirements.md, revisie 1.
Werkruimte: uitgepakte map effective-ai-course-lab.
Huidige stand: de statusfilter staat in task_report.py en de tests.
Gecontroleerd: noteer het waargenomen testresultaat en de handmatige aantallen 4, 2 en 2.
Besluit: tasks.json bleef ongewijzigd.
Openstaand: onafhankelijke controle van diff en bron.
Volgende controle: voer de tests en de ongeldige statuscase opnieuw uit.
Stop als: vereiste of basiswaarde afwijkt van dit verslag.
```

**Het voorbeeld beweert niet dat je dit werk hebt uitgevoerd.** Noteer je waargenomen testresultaten en gewijzigde bestanden. Als de bronversie verandert, werk de overdracht dan bij nadat je de bron opnieuw hebt gelezen.

## Test een nieuwe sessie

**Start in het lab een nieuwe chat of codeersessie.** Plak in een chat de overdracht en het `AGENTS.md`-bestand van het synthetische lab. Noem ook de bestanden die de sessie moet bekijken. Open in een codeeragent de labmap en plak de overdracht met leesrechten voor de genoemde bestanden. Vraag:

```text
Noem met deze overdracht en de huidige repositorybestanden de goedgekeurde statuswaarden, de basisstand en de volgende controle. Bewerk niets.
Meld het conflict als de overdracht afwijkt van een huidige bron.
```

**Verwacht redeneren:** de nieuwe sessie vindt `open` en `done` in `docs/requirements.md`, noemt de beginwaarde 4 en wijst op tests en handmatige controles. Herhaalt de sessie de oude waarde `pending`, lees dan de eis opnieuw en corrigeer de overdracht.

## Houd de orchestrator klein

**Een orchestrator is de hoofdagent die workers coördineert.** Geef elke worker een afgebakende vraag en benoemde invoerbestanden. Vraag om een kort resultaat: bevinding, bewijsbestand, zekerheid en onopgelost punt. Bewaar gedetailleerde logs in een bestand of in de workersessie. Neem alleen mee wat de hoofdagent nodig heeft voor de volgende beslissing.

**Voorbeeld:** vraag een worker met alleen-lezen-toegang om de tests te bekijken en te melden: “ontbrekende case, bestand en regel, voorgestelde controle”. Laat de worker niet alle tests in de hoofdchat plakken. De hoofdagent controleert de bevinding in de repository voor de wijziging. De [les over delegeren](/articles/effective-ai-agent-delegation/) voegt een aparte workeropdracht toe wanneer de omvang die kosten rechtvaardigt.

**Workersessies hebben bij veel producten een eigen context,** maar overerving en isolatie verschillen. Controleer de actuele productregels voordat je aanneemt dat een worker dezelfde instructies, bestanden of tools ziet als de hoofdagent. De gidsen over [Codex-subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) en [Claude Code-subagents](https://code.claude.com/docs/en/sub-agents) beschrijven het gedrag van die producten.

## Gebruik contextcompressie zorgvuldig

**Contextcompressie verkort de actieve geschiedenis.** Codex, Claude Code en OpenCode verschillen in het moment en de manier waarop ze comprimeren. Zie een gecomprimeerde samenvatting als hulpmiddel om verder te gaan, niet als volledig projectdossier. Bewaar eisen en besluiten in bestanden en controleer ze na compressie opnieuw. Bekijk de actuele richtlijnen voor [Beste werkwijzen voor Codex](https://learn.chatgpt.com/docs/learn/best-practices), [Claude Code-opdrachten](https://code.claude.com/docs/en/commands) en [OpenCode 2-compressie](https://opencode.ai/v2/docs/compaction). OpenCode 1 en OpenCode 2 gebruiken verschillende schema’s. Controleer `opencode --version` voordat je instellingen overneemt.

**Verliest de assistent een randvoorwaarde,** stop dan de wijziging, open de bron opnieuw en herhaal het taakpakket. Een nieuwe sessie met een korte, geverifieerde overdracht vraagt vaak minder aandacht dan herhaaldelijk een lange, verwarde chat corrigeren.

## Oefen en controleer

**Je artefact:** een overdracht van minder dan 180 woorden, opgeslagen buiten het lab. Label elke regel als bron, waargenomen resultaat, besluit of openstaande actie. Geef de overdracht aan een nieuwe sessie en noteer of die beide geaccepteerde statuswaarden en de volgende controle noemt.

**Voltooiingscontrole:** de nieuwe sessie noemt `open`, `done`, de beginwaarde 4 en een teststap zonder op de oude chat te steunen. Vul ontbrekende punten aan en test opnieuw in een andere nieuwe sessie.

## Controleer je begrip

1. **Vraag:** wat hoort in een overdracht voor een nieuwe sessie? **Antwoord:** het doel, de gezaghebbende bron, de huidige status, het gecontroleerde resultaat en de volgende actie.

2. **Vraag:** waarom moet een workerrapport kort zijn? **Antwoord:** een beknopt bewijsrapport geeft de orchestrator het benodigde resultaat zonder het workertranscript te herhalen.

## Problemen oplossen

- **Samenvatting mist een besluit:** voeg een korte beslisregel en bronversie toe.
- **Workerantwoord is enorm:** vraag om een beperkte bewijstabel en bestandsverwijzingen.
- **Overdracht is verouderd:** lees de actuele bronbestanden opnieuw voordat je iets wijzigt.
- **Contextdruk blijft bestaan:** splits de taak over kleinere sessies met aparte artefacten.

## Volgende stappen

**Ga verder met [MCP-server instellen](/articles/effective-ai-mcp-server-setup/)**. Je voegt een externe tool met alleen-lezen-toegang toe en beperkt de uitvoer.

**Cursusnavigatie:** [Vorige: Eerste codeertaak](/articles/effective-ai-coding-agent-first-task/), [Cursusoverzicht](/effective-ai-course-start/).
