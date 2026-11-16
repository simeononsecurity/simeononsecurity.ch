---
title: "AI-uitvoer, bronnen, tests en kosten controleren"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Maak een acceptatierecord voor een AI-resultaat met broncontroles, bestandsscope, testbewijs, privacycontrole en gebruikskosten."
genre: ["Kunstmatige intelligentie", "Softwareontwikkeling"]
tags: ["AI-uitvoer controleren", "AI-feiten controleren", "beoordeling van codeeragent", "AI-testbewijs", "AI-kosten bijhouden", "menselijke beoordeling"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Een beoordelingsformulier vergelijkt een AI-bewering met een bronbestand, codediff, testuitvoer en gebruikstotaal"
coverCaption: ""
---

[Terug naar de cursus Praktische AI-workflow](/effective-ai-course-start/)

**Accepteer een AI-resultaat pas nadat je het passende bewijs voor de taak hebt gecontroleerd.** Een verzorgde uitleg, een geconfigureerde tool en een groen testbericht beantwoorden verschillende vragen. Deze les maakt één beoordelingsrecord voor het workshoplab.

**Leerdoel:** je maakt een acceptatierecord voor bronnen, bestandsscope, tests, privacy en gebruik.

## Belangrijkste punten

- **Broncontrole:** vergelijk een feitelijke bewering met een actuele, gezaghebbende bron.
- **Scopecontrole:** inspecteer welke bestanden of systemen zijn gewijzigd.
- **Gedragscontrole:** voer tests en relevante handmatige gevallen uit.
- **Privacycontrole:** inspecteer welke gegevens de tool of aanbieder heeft ontvangen.
- **Gebruikscontrole:** noteer tokens, toolaanroepen en het tarief waarmee je de kosten berekent.

## Voor je begint

**Vereisten:** het cursuslab, `docs/requirements.md`, een lokale Git-snapshot en de [MCP-les](/articles/effective-ai-mcp-server-setup/) of de browservariant. Reserveer 40 minuten. De moeilijkheidsgraad is gemiddeld. Gebruik je bewerkte lab uit de eerste taak met een codeeragent. Heb je de bewerking overgeslagen, gebruik dan een verse extractie en markeer functiecontroles als niet geïmplementeerd. De ongewijzigde basisversie slaagt nog steeds voor de twee oorspronkelijke tests.

## Een feitelijke bewering controleren

**Bewering:** “De goedgekeurde statuswaarden zijn `open` en `pending`.” Open `docs/requirements.md`, revisie 1. Daar staan `open` en `done`. De bewering klopt niet. Een zelfverzekerde toon verandert de vereiste niet.

**Gebruik voor productbeweringen** actuele officiële documentatie en noteer de paginatitel en controledatum. Een bewering over een menu, abonnement, opdracht of contextlimiet veroudert sneller dan een algemeen workflowprincipe. De [Codex-documentatie](https://learn.chatgpt.com/docs/codex/cli), [Claude Code-documentatie](https://code.claude.com/docs/en/overview) en [OpenCode-documentatie](https://opencode.ai/docs/) beschrijven hun huidige interfaces.

| Bewering | Bron | Beslissing |
|---|---|---|
| **`open` en `pending`** | Labvereiste, revisie 1 | Afwijzen, vervang `pending` door `done` |
| **Aantal zonder filter is 4** | Basisprogramma en vier JSON-items | Controleer door het programma uit te voeren |
| **Er vond een MCP-leesactie plaats** | Transcript van sessietools | Alleen accepteren als een toolaanroep zichtbaar is |

## De wijziging inspecteren

**Gebruik voor een programmeertaak** Git om gewijzigde bestanden op te sommen en de echte diff te lezen. Een nieuw, niet-gevolgd bestand verschijnt wel in de status maar niet in een gewone diff. Inspecteer daarom beide.

```bash
git status --short
git diff -- task_report.py tests
```

**Verwachte scope:** na de filtertaak veranderen alleen `task_report.py` en gerichte tests. Een wijziging in `tasks.json`, `docs/requirements.md` of een verborgen configuratiebestand vereist uitleg en een aparte beoordeling. Heb je niets bewerkt, dan verwacht je geen wijzigingen.

## Gedrag testen

**Voer dezelfde basis- en functietests uit** in de uitgepakte labmap. Het voltooiingsbericht van de agent hoort de waargenomen resultaten van deze controles te noemen.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**In de bewerkte kopie** dekken tests de nieuwe gevallen, zijn de aantallen 4, 2 en 2, en eindigt de ongeldige waarde met een duidelijke fout en een niet-nul status. In een verse startkopie slagen alleen de twee basistests en is het totaalaantal 4. Noteer die starttoestand apart.

**Een mislukte functietest vereist onderzoek.** Als `open` 4 toont, controleer dan of het filterargument de telfunctie bereikt en of het programma het veld `status` van de taak vergelijkt. Noem een mislukte test niet geslaagd omdat de agent zegt dat de implementatie klaar is.

## Gegevensbescherming en toegang controleren

**Noteer welke bestanden de agent ontving.** Het lab bevat synthetische gegevens en geen geheimen. Een echt project kan inloggegevens, klantgegevens of privédocumenten bevatten. Inspecteer prompts, logs, schermafbeeldingen en diffs op zulke waarden voordat je uitvoer deelt.

**Een lokale test bewijst alleen lokaal gedrag.** Hij bewijst geen rechten van een cloudaccount, de scope van een MCP-server of het gedrag van een uitgerolde dienst. Test elke grens in de omgeving waar die van belang is.

## Gebruik en kosten registreren

**Tokens meten de hoeveelheid modelinvoer en -uitvoer.** Productdashboards verschillen, dus gebruik de gebruikscijfers van je aanbieder. Noteer toolaanroepen en kosten voor afbeeldingen of gehoste omgevingen apart, indien relevant. Controleer actuele tarieven voordat je een echte rekening berekent.

**Open de gebruiksweergave van het account dat de taak uitvoerde.** Noteer getoonde invoer- en uitvoertokens, het model, de factureringsperiode en een categorie voor gecachte invoer. Bij ChatGPT- of Claude-abonnementen is een gebruikslimiet of tegoed niet hetzelfde als een API-bedrag voor een taak. Bekijk voor een API- of provideruitvoering van OpenCode het gebruik of de facturering van die aanbieder en de actuele tarieven. Toont het product geen tokens per taak, noteer dan “niet beschikbaar” en leid geen kosten af uit de chatlengte.

**Rekenvoorbeeld, geen aanbiederstarief:** 30.000 invoertokens tegen $1 per miljoen kosten $0,03. 5.000 uitvoertokens tegen $5 per miljoen kosten $0,025. De modelkosten in dit voorbeeld zijn samen $0,055, vóór tool- of hostingkosten.

```text
invoerkosten = invoertokens / 1.000.000 × invoertarief
uitvoerkosten = uitvoertokens / 1.000.000 × uitvoertarief
totaal = invoerkosten + uitvoerkosten + afzonderlijke toolkosten
```

**Een gedelegeerde taak verbruikt ook tokens.** Delegatie verplaatst gedetailleerde uitvoer uit het hoofdgesprek, maar maakt het werk niet gratis. Vergelijk de kosten met de waarde van de onafhankelijke controle.

**Houd kostencategorieën apart.** Gecachte invoer, nieuwe invoer, uitvoer, toolaanroepen en gehoste uitvoering hebben mogelijk verschillende tarieven. Dit voorbeeld gebruikt alleen de tarieven voor nieuwe invoer en uitvoer. Het zegt niets over een abonnementsrekening of toolkosten.

## Een acceptatierecord bijhouden

| Veld | Ingevuld voorbeeld na de bewerking |
|---|---|
| **Bron** | `docs/requirements.md`, revisie 1, gelezen |
| **Gewijzigde bestanden** | `task_report.py` en `tests/test_task_report.py` in `git status --short` |
| **Tests** | Basis- en nieuwe filtertests geslaagd, noteer het waargenomen aantal |
| **Handmatige uitvoer** | `Total tasks: 4`, `2` en `2` waargenomen, ongeldige waarde afgewezen |
| **Functiestatus** | `--status open` en `--status done` geïmplementeerd |
| **Gegevensbescherming** | Alleen synthetische bestanden |
| **Gebruik** | Noteer de cijfers van je aanbieder, indien beschikbaar |
| **Beslissing** | Accepteer pas als bron-, diff-, test- en privacycontroles slagen |

**Je resultaat:** kopieer dit record en vul het na je eigen uitvoering in. Vervang “waargenomen” alleen door uitvoer die je zelf zag. Kies Accepteren als alle vereiste controles slagen, Herzien als een oplossing beperkt is en Stoppen als bron, scope of toegang onduidelijk is.

## Controleer je begrip

1. **Vraag:** bewijst een geslaagde basiscontrole van de starter dat de gevraagde functie bestaat? **Antwoord:** Nee. Test het nieuwe acceptatiegedrag na de bewerking.

2. **Vraag:** wat hoort in een acceptatierecord? **Antwoord:** bronbewijs, gewijzigde bestanden, gedragscontroles, toegangsscope en waargenomen gebruik.

## Problemen oplossen

- **Geen bron voor een bewering:** markeer deze als niet geverifieerd en zoek een gezaghebbende bron.
- **Tests slagen maar de uitvoer wijkt af:** voeg een handmatig geval toe en inspecteer de gegevens.
- **Gebruiksgegevens ontbreken:** noteer “niet beschikbaar” in plaats van echte kosten te schatten.
- **Diff bevat privégegevens:** stop met het delen van de uitvoer en verwijder die gegevens uit het oefenrecord.

## Volgende stappen

**Ga verder met [Agentdelegatie](/articles/effective-ai-agent-delegation/)**. Lees voor details over kosten en privacy [aanbiederrouting](/articles/openrouter-provider-routing-quality-cost/) en [de privacygrens van lokale AI](/articles/local-ai-privacy-boundary/).

**Cursusnavigatie:** [Vorige: MCP instellen](/articles/effective-ai-mcp-server-setup/), [Cursusoverzicht](/effective-ai-course-start/).
