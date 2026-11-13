---
title: "AI-taakpakketten: betere prompts en acceptatiecriteria"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Zet vage AI-verzoeken om in taakpakketten met een vast resultaat, bron, bestandsbereik, controles en stopvoorwaarde."
genre: ["Kunstmatige intelligentie", "Productiviteit", "Software-engineering"]
tags: ["AI-prompts schrijven", "taakpakket", "prompt voor programmeeragent", "acceptatiecriteria", "AI-werkproces", "instructies voor AI-agenten"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Een vaag verzoek herschreven als een kort taakpakket met bron, bereik, controle en stopvoorwaarde"
coverCaption: ""
---

[Terug naar de cursus Praktische AI-werkprocessen](/effective-ai-course-start/)

**Een goede prompt beschrijft het werk en hoe je het resultaat beoordeelt.** Meer woorden lossen een ontbrekend bereik niet op. Deze les zet een vaag verzoek om in een taakpakket voor het cursuslab.

**Leerdoel:** je schrijft een afgebakend taakpakket met bron, bestandsbereik, controles en stopvoorwaarde.

## Belangrijkste punten

- **Resultaat** benoemt het gewenste artefact of gedrag.
- **Bereik** benoemt toegestane bestanden en uitgesloten acties.
- **Bron** wijst de goedgekeurde eis aan.
- **Acceptatiecriteria** maken succes waarneembaar.
- **Stopvoorwaarden** voorkomen giswerk en niet-goedgekeurd vervolgwerk.

## Voordat je begint

**Vereisten:** het uitgepakte lab, het bestand `docs/requirements.md` en de [les over repositorycontext](/articles/effective-ai-agents-md-context/). Reserveer 30 minuten. Het niveau is beginner. De oefening eindigt met een geschreven pakket. Je hoeft nog geen code aan te passen.

## Vergelijk twee verzoeken

**Vaag verzoek:** “Verbeter het taakscript.” Een agent kan de uitvoer herschrijven, afhankelijkheden toevoegen, voorbeeldgegevens aanpassen of tests overslaan. Het verzoek bepaalt geen van die keuzes.

**Afgebakend verzoek:** “Voeg een optioneel statusfilter toe aan `task_report.py` op basis van revisie 1 van `docs/requirements.md`. Behoud de standaarduitvoer. Voeg tests toe. Wijzig geen voorbeeldgegevens. Stop vóór de commit.” De agent kiest nog steeds de implementatiedetails, terwijl de taak bepaalt wanneer het werk slaagt.

| Onderdeel van pakket | Labvoorbeeld | Controle |
|---|---|---|
| **Resultaat** | Voeg `--status` toe aan het rapport | Beide toegestane waarden werken |
| **Bron** | `docs/requirements.md`, revisie 1 | Code volgt de goedgekeurde waarden |
| **Bereik** | Alleen programma en tests | Diff bevat geen andere bestanden |
| **Beperkingen** | Behoud standaarduitvoer en voorbeeldgegevens | Basisuitvoer blijft `Total tasks: 4` |
| **Bewijs** | Testopdracht en handmatige uitvoeringen | Uitvoer komt overeen met verwachte aantallen |
| **Stop** | Geen commit of push | Git-geschiedenis en remote blijven onaangeroerd |

## Gebruik een herbruikbaar sjabloon

**Kopieer dit sjabloon** voor een kleine programmeer- of onderzoekstaak. Verwijder irrelevante velden in plaats van ze met vage tekst te vullen.

```text
Outcome:
Authoritative source and revision:
Relevant files or records:
Allowed changes:
Excluded changes and actions:
Examples of desired behavior:
Completion checks:
Stop or ask when:
Report back with:
```

**Voor het lab** ziet het ingevulde pakket er zo uit:

```text
Outcome: Add an optional --status filter to task_report.py.
Source: docs/requirements.md, revision 1.
Relevant files: task_report.py, tasks.json, tests/.
Allowed changes: task_report.py and focused tests.
Excluded: tasks.json, new dependencies, commits, pushes.
Examples: no filter prints Total tasks: 4. Open and done each print 2.
Checks: run unit tests and four manual commands: no filter, open, done, and invalid.
The invalid value must exit nonzero with a clear error.
Stop or ask: source conflict, missing file, unrelated failing baseline.
Report: changed files, commands, observed outputs, unresolved issues.
```

**Op Windows** gebruik je `py -3` in pakketopdrachten wanneer je omgeving de Python-launcher gebruikt.

**Het pakket schrijft niet elke coderegel voor.** De agent kiest een kleine implementatie, terwijl het resultaat toetsbaar blijft.

## Voeg voorbeelden zorgvuldig toe

**Een nauwkeurig voorbeeld vermindert dubbelzinnigheid.** De voorbeelden `open` en `done` geven de uitvoer aan voor het aangeleverde bestand met vier taken. Ze vormen geen algemene regel voor elk bestand. Bij een ander bestand hangen de aantallen af van de records.

**Scheid verwacht van waargenomen.** Vóór het programma draait, is `Total tasks: 2` het verwachte resultaat voor elke status. Na de uitvoering is de terminaluitvoer een waarneming. Verschillen de waarden, onderzoek dan de gegevens en implementatie voordat je succes meldt.

## Oefen een stopvoorwaarde

**Stel dat het eisenbestand ontbreekt.** Het pakket noemt dit als goedgekeurde bron. Stop en vraag om de eis in plaats van toegestane waarden af te leiden uit een oude chat of voorbeeldissue.

**Stel dat de basistests vóór bewerking falen.** Leg de fout vast en vraag of je eerst de beginsituatie moet herstellen. Een latere geslaagde run maakt niet duidelijk of de filtertaak of de uitgangssituatie het verschil veroorzaakte.

**Stel dat de agent wil committen.** Het pakket sluit commits uit. Vraag de agent te stoppen na de diff en tests. Jij bepaalt of een latere commit bij de projectworkflow past.

## Controleer het pakket

**Geef één punt per antwoord:** is het resultaat concreet? Is de leidende bron genoemd? Is het bestandsbereik duidelijk? Zijn ten minste twee waarneembare controles vermeld? Is er een stopvoorwaarde? Minder dan vijf punten betekent dat je het pakket vóór delegatie herzien moet.

**Jouw resultaat:** bewaar het definitieve taakpakket en een uitleg van één regel over een stopvoorwaarde. Geef het aan een programmeeragent in de volgende praktijkles of beantwoord de verwachte resultaten handmatig op de studieroute.

## Controleer je begrip

1. **Vraag:** Wat maakt een taakpakket controleerbaar? **Antwoord:** Een bron, toegestane bestanden, waarneembare controles en een stopvoorwaarde.
2. **Vraag:** Wat moet een agent doen wanneer de bron een vereist detail mist? **Antwoord:** Stoppen en het ontbrekende detail melden in plaats van het te verzinnen.

## Problemen oplossen

- **De agent verandert te veel:** noem bestanden en uitgesloten acties in het pakket.
- **De agent stelt veel vragen:** geef de ontbrekende bron of een concreet voorbeeld.
- **De agent claimt te vroeg succes:** vraag om waargenomen opdrachtuitvoer en inspecteer de bestanden.
- **Het pakket wordt te lang:** vervang gekopieerde broninhoud door een pad en revisie.

## Volgende stappen

**Ga verder met [Je eerste taak met een programmeeragent](/articles/effective-ai-coding-agent-first-task/)**. Gebruik het pakket voor een kleine labwijziging.

**Cursusnavigatie:** [Vorige: Repositorycontext](/articles/effective-ai-agents-md-context/), [Cursusoverzicht](/effective-ai-course-start/).
