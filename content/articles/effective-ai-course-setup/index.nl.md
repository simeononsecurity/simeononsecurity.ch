---
title: "De AI-workflowcursus instellen: terminal, Git en oefenlab"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Maak een veilige oefenplek voor AI, leer de terminal- en Git-termen uit de cursus en voer het startlab uit."
genre: ["Kunstmatige intelligentie", "Softwareontwikkeling", "Onderwijs"]
tags: ["AI-cursus instellen", "basiskennis terminal", "basiskennis Git", "vereisten voor codeeragenten", "AI-oefenlab", "AI-cursus voor beginners"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Oefenplek voor beginners met terminal-, Python- en Git-symbolen, een aangevinkte labmap en een herstelarchief"
coverCaption: ""
---

[Terug naar de praktische AI-workflowcursus](/effective-ai-course-start/)

**Maak een veilige oefenplek voordat je een agent gebruikt.** Les 1 en 2 werken in een browser zonder dit lab. Kom vóór les 3 terug als je de volledige cursus wilt volgen. De programmeerlessen gebruiken Git, Python 3.10 of hoger en één codeeragent. In de studieroute vervangen gemarkeerde handmatige taken de niet-beschikbare agentacties.

**Leerdoel:** je voert het startlab uit, bewaart een lokale beginsituatie en legt uit hoe je een wegwerpkopie herstelt.

## Belangrijkste punten

- **Browserroute:** voer de chat-, plannings-, broncontrole- en reviewoefeningen uit in ChatGPT of Claude.
- **Lokale route:** gebruik een terminal en het meegeleverde Python-lab voor programmeeroefeningen.
- **Herstelroute:** pak een nieuwe labkopie uit als een oefening misgaat.
- **Veiligheidsregel:** houd privébestanden, klantgegevens en inloggegevens buiten het lab.

## Kies je route

| Route | Benodigdheden | Oefening |
|---|---|---|
| **Introductie in de browser** | Actuele browser en een ChatGPT- of Claude-account | Les 1 en 2, plus het chattakenpakket uit les 1 |
| **Lokaal oefenen** | Git, Python 3.10 of hoger, terminal en één codeeragent | Bestanden, verschillen, tests en agentwijzigingen |
| **Studiecursus** | Browser, lokale Python 3.10 of hoger en Git | Alle labcontroles; niet-beschikbare agent- en MCP-stappen zijn gemarkeerd als niet uitgevoerd |

**Elk product bepaalt zijn eigen abonnementen en limieten.** Bekijk [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) en [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) voordat je op een functie vertrouwt. De studieroute bewijst geen praktische vaardigheid met een niet-beschikbare codeeragent. Noteer dit verschil in je afrondingsnotities.

**Volg één standaardroute:** gebruik ChatGPT in een browser voor chatopdrachten en daarna één beschikbare codeeragent met het lokale lab. Claude is een gelijkwaardige chatoptie. Voor het programmeerdeel kun je Codex CLI, Claude Code CLI of OpenCode gebruiken. Accounts bij alle aanbieders zijn niet nodig.

**Noteer vijf controles voordat je een codeeragent opent.** Zo houd je een lokale labcontrole gescheiden van een bewering over een account of gehoste werkruimte.

| Controle | Noteer |
|---|---|
| **Werkruimte** | De exacte uitgepakte labmap die de agent leest |
| **Uitvoering** | Lokale computer of gekozen externe werkruimte |
| **Aanbieder** | Account of modelaanbieder voor deze taak |
| **Machtigingen** | Of bestanden schrijven en shellopdrachten uitvoeren mag of goedkeuring vereist |
| **Beginsituatie** | Waargenomen aantal en twee geslaagde tests vóór wijzigingen |

**Houd de oefenmap beperkt.** Een gehoste werkruimte heeft een eigen kopie van het synthetische lab nodig. Een lokale uitvoering bewijst niet dat de externe kopie of account dezelfde bestanden en machtigingen heeft.

## Leer de lokale termen

| Term | Eenvoudige betekenis |
|---|---|
| **Terminal** | App waarin je opdrachten typt |
| **Shell** | Software die die opdrachten interpreteert |
| **CLI** | Opdrachtregelinterface van een programma |
| **Werkmap** | Map die een opdracht standaard gebruikt |
| **Repository** | Project dat Git bijhoudt |
| **Commit** | Opgeslagen Git-momentopname |
| **Branch** | Benoemde reeks Git-wijzigingen |
| **Diff** | Weergave van toegevoegde of verwijderde regels |
| **Controle** | Herhaalbare controle van verwacht gedrag |
| **Exitcode** | Getal dat succes of mislukking van een opdracht meldt |

**Je hebt GitHub niet nodig voor het startlab.** Git werkt op je computer. GitHub is een aparte hostingdienst. Een lokale commit bewaart een momentopname zonder bestanden te versturen.

## Bereid het lab voor

**Download het [startlab van de cursus](/downloads/effective-ai-course-lab.zip)** en pak het uit in een nieuwe map die jij beheert. Open daar een terminal. Gebruik op macOS of Linux Terminal en `cd` om naar de uitgepakte map te gaan. Gebruik op Windows PowerShell of Windows Terminal en `cd`. Op Windows is het Python-commando vaak `py -3` in plaats van `python3`.

**Installeer zo nodig [Python 3.10 of hoger](https://www.python.org/downloads/) en [Git](https://git-scm.com/downloads).** Controleer de geïnstalleerde hulpmiddelen voordat je het lab start. De eerste twee opdrachten tonen versies. `cd` wijzigt de werkmap. `ls` toont bestanden. Vervang het voorbeeldpad door het werkelijke pad van je uitgepakte map.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**Gebruik in Windows PowerShell** `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` en `Get-ChildItem`. De lijst moet `task_report.py`, `tasks.json`, `tests` en `docs` bevatten. Rond de installatie af als een versieopdracht mislukt.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**Vervang in Windows PowerShell** `pwd` door `Get-Location` als je dat liever gebruikt, en `python3` door `py -3` als Python de launcher gebruikt. De eerste opdracht toont het pad. Dat moet eindigen op je uitgepakte labmap. Controleer ook de bestandsnamen. `AGENTS.md.txt` vervangt `AGENTS.md` niet. Schakel in Verkenner bestandsextensies in om de volledige naam te zien.

**Verwachte uitvoer:** het rapport meldt `Total tasks: 4`. De testopdracht toont twee tests en eindigt met `OK`. Een shell geeft bij succes exitcode nul terug. Een ander aantal of een traceback betekent dat je de map en Python-installatie controleert.

**Lees elke opdracht in delen.** In `python3 task_report.py tasks.json` start `python3` Python, is `task_report.py` het programma en noemt `tasks.json` de invoergegevens. Het afgedrukte aantal is uitvoer, geen extra opdracht. Na een fout tonen macOS en Linux de status met `echo $?`. PowerShell geeft de status van het laatste native programma via `$LASTEXITCODE`.

**Trek ongeveer tien minuten uit voor de eerste uitvoering** zodra Python is geïnstalleerd: pak het lab uit, voer het rapport uit en vergelijk het totaal met de vier items in `tasks.json`. Open het JSON-bestand in een teksteditor en tel de items zelf.

## Oefen veilig met Git

**Start Git alleen in de uitgepakte labmap.** Deze opdrachten bewaren een lokale momentopname. `git status` toont gewijzigde bestanden. `git diff` toont gewijzigde regels nadat je een bijgehouden bestand bewerkt.

```bash
git init
git add .
git commit -m "Basislijn van het cursuslab"
git status --short
```

**Verwachte status:** na de commit verschijnen geen bestandsnamen. Vraagt Git om een naam en e-mailadres, stel dan in deze map een identiteit in die alleen voor het lab geldt en voer de commit opnieuw uit. Vervang voorbeeldwaarden door privéwaarden. Plak geen identiteit of inloggegevens in een openbare chat.

```bash
git config --local user.name "Cursist"
git config --local user.email "learner@example.invalid"
git commit -m "Basislijn van het cursuslab"
git status --short
```

**Je hebt geen Git-opdracht nodig om te herstellen.** Bewaar notities buiten het lab, verwijder de uitgepakte oefenkopie en pak de oorspronkelijke ZIP opnieuw uit. Gebruik dit als een leswijziging het programma in een onbekende staat brengt.

## Bescherm je oefenplek

**Gebruik synthetische voorbeelden.** Upload geen privédocumenten naar een cursusproject. Zet geen API-sleutels in prompts, bronbestanden, schermafbeeldingen of commits. De toegang van een codeeragent tot bestanden en opdrachten hangt af van machtigingen en de geopende map. Controleer beide voordat je de agent laat werken.

**Controleer delen voordat je iets uploadt.** Projectleden kunnen toegang hebben tot projectbestanden. Volg voor echt werk het beleid van je organisatie. De cursus gebruikt fictieve gegevens, dus het lab zelf vereist geen speciale toestemming.

## Oefen en controleer

**Jouw resultaat:** noteer de gekozen route, de vijf voorafvelden, het aantal uit het rapport, de testuitkomst en de herstelmethode. Gebruik een verse labkopie om te controleren of je het lab kunt herstellen.

**Verwacht inzicht:** je weet op welke map opdrachten werken, onderscheidt lokale Git van hosting en hebt een herstelmethode voordat een agent bestanden aanpast.

## Controleer je begrip

1. **Vraag:** Rondt een introductie die alleen in de browser plaatsvindt de lokale labroute af? **Antwoord:** Nee. De volledige route vereist een lokale Python- en Git-beginsituatie.

2. **Vraag:** Wat bewaar je voordat je het wegwerplab wijzigt? **Antwoord:** Het geslaagde resultaat van de starttest en een schoon herstelpunt.

## Problemen oplossen

- **Python-opdracht ontbreekt:** installeer Python 3 bij de officiële aanbieder en open de terminal opnieuw.
- **Bestand niet gevonden:** controleer de werkmap en toon de bestanden in de uitgepakte map.
- **Tests starten niet:** gebruik precies de opdracht uit het README-bestand van het uitgepakte lab.
- **Git vraagt om commitidentiteit:** stel Git lokaal in en houd de gekozen waarden uit cursusnotities.

## Volgende stappen

**Ga verder met de [betrouwbare AI-workflow](/articles/effective-ai-workflow-foundations/)**. De eerste oefening gebruikt dezelfde synthetische werkplaats voordat een hulpmiddel echte bestanden krijgt.

**Cursusnavigatie:** [Cursusoverzicht](/effective-ai-course-start/).
