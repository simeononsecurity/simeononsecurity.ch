---
title: "Begrensde AI-agentlussen: controles, nieuwe pogingen en stopregels"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Definieer een AI-doellus met een waarneembare status, controles, limieten voor nieuwe pogingen, stopvoorwaarden en een duidelijke overdracht aan een mens."
genre: ["Kunstmatige intelligentie", "Software-engineering", "Productiviteit"]
tags: ["AI-doellussen", "agent-herhalingslus", "stopregels voor AI-automatisering", "agentbewaking", "AI-overdracht aan mens", "begrensde AI-workflow"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Een kleine agentlus gaat van een wijziging naar een test, een beslissing over opnieuw proberen en een overdracht aan een mens"
coverCaption: ""
---

[Terug naar de praktische cursus AI-workflows](/effective-ai-course-start/)

**Een doellus herhaalt werk totdat een vastgelegd resultaat slaagt voor een controle of een stopregel wordt geactiveerd.** Een nuttige lus leest de huidige status, voert één begrensde actie uit, controleert het resultaat en legt vast wat er gebeurde. Een open opdracht als “blijf het proberen” heeft geen betrouwbare voltooiingsregel.

**Leerdoel:** je voert een begrensde lablus uit met een controle waarvan de mislukking vooraf bekend is, en legt de stopbeslissing vast.

## Belangrijkste punten

- **Doel:** een resultaat dat in waarneembare termen is beschreven.
- **Status:** de huidige bestanden, uitvoer, fouten en bronrevisie.
- **Controle:** een test of beoordeling die bij het doel hoort.
- **Budget voor nieuwe pogingen:** het maximale aantal pogingen voor één fout.
- **Stopregel:** een voorwaarde die beëindiging of een menselijke beslissing vereist.

## Voordat je begint

**Vereisten:** het [takenpakket](/articles/effective-ai-task-packets/), het [verificatierapport](/articles/effective-ai-output-verification/) en de [les over delegeren](/articles/effective-ai-agent-delegation/). Trek 45 minuten uit. De moeilijkheidsgraad is gemiddeld. Gebruik een nieuwe kopie van het synthetische lab, zodat je de eerste mislukte controle vooraf kent.

## Stel het luscontract op

**Voor het verzoek om op status te filteren** stel je het contract vast voordat er een nieuwe poging plaatsvindt:

```text
Doel: --status open|done ondersteunen zonder de standaarduitvoer te wijzigen.
Bron: docs/requirements.md, revisie 1.
Toegestane bestanden: task_report.py en gerichte tests.
Controles: unit-tests, aantallen 4/2/2, ongeldige waarde geeft een exitcode anders dan nul.
Pogingsbudget: hoogstens twee bewerkingen na de eerste poging.
Meteen stoppen: bronconflict, onverwachte bestandswijziging, blootstelling van een geheim,
of een mislukte basiscontrole die niets met dit verzoek te maken heeft.
Overdracht: meld de definitieve diff, opdrachten, uitvoer, pogingen en het onopgeloste probleem.
```

**Het budget is een taakbeleid**, geen standaardinstelling van het product. Twee nieuwe pogingen zijn genoeg om een kleine labtaak te diagnosticeren zonder herhaalde fouten te verbergen. Een productietaak vraagt om een eigen keuze voor risico en beoordeling.

## Gebruik een statustabel

| Stap | Vast te leggen status | Beslissing |
|---|---|---|
| **Lezen** | Bronrevisie en basisresultaat | Stop als de beginsituatie afwijkt |
| **Handelen** | Gewijzigde bestanden en uitgevoerde actie | Wijs wijzigingen buiten de scope af |
| **Controleren** | Exacte test en handmatige uitvoer | Accepteer of diagnoseer |
| **Opnieuw proberen** | Oorzaak van de fout en nieuwe hypothese | Ga alleen binnen het budget verder |
| **Overdragen** | Eindstatus en volgende eigenaar | Stop na slagen of blokkering |

**Leg pogingen vast, niet alleen het laatste bericht.** Een test die slaagt na drie verborgen wijzigingen vertelt niet wat er veranderde. Houd een kort logboek bij van de fout, de aangepaste hypothese en het nieuwe bewijs.

## Doorloop een fout

**Voorbeeld van de eerste poging:** de agent voegt filteren en tests toe. `open` toont 2, maar `--status invalid` toont 0 en eindigt zonder fout. De eis zegt dat een ongeldige waarde een niet-nul exitcode moet opleveren. Markeer de controle als mislukt.

**Diagnose:** bekijk de argumentvalidatie. De agent behandelde een onbekende waarde als een lege overeenkomst in plaats van als een fout. Vraag om een begrensde correctie die toegestane waarden controleert voordat er wordt geteld. Voer de ongeldige casus en alle eerdere controles opnieuw uit.

```text
Poging 1: de ongeldige status gaf succes terug, dus de acceptatie mislukte.
Oorzaak gevonden: toegestane waarden worden niet gevalideerd.
Verzoek voor poging 2: wijs niet-ondersteunde waarden af en behoud de aantallen 4/2/2.
Benodigd bewijs: volledige testrun en exitstatus van de ongeldige opdracht.
```

**Verwacht resultaat bij de tweede poging:** een duidelijke foutmelding en een niet-nul exitcode voor `invalid`, terwijl geldige aantallen gelijk blijven. Als de tweede poging nog steeds mislukt, gebruik dan de laatste poging pas nadat je een nieuwe oorzaak hebt vastgesteld. Dezelfde opdracht herhalen is geen diagnose.

## Behandel onduidelijke resultaten

**Een proces dat zonder resultaat stopt, is niet geslaagd.** Als een tool een time-out krijgt na een mogelijke schrijfactie, controleer je de bestanden en Git-status voordat je de tool opnieuw uitvoert. Meldt een gekoppelde service een onbekende uitkomst, lees dan de actuele status voordat je een externe actie herhaalt. Dubbele verzendingen, publicaties of schrijfacties vormen buiten het lab een echt risico.

**Stop voor menselijke beoordeling** als de eis botst met een andere goedgekeurde bron, een machtiging de actie blokkeert, het budget voor nieuwe pogingen op is of de gevraagde actie een publicatiegrens overschrijdt. De overdracht vermeldt de exacte status en de nog te nemen beslissing.

## Houd lussen en monitors apart

**Een bewerkingslus** draait binnen een begrensde taak en controleert het resultaat na elke actie. **Een geplande monitor** wordt later wakker om een voorwaarde te controleren. Een monitor heeft een eigen frequentie, wijzigingsdrempel, meldingsregel en stopvoorwaarde nodig. Maak van de bewerkingslus in het lab geen terugkerende taak. De volgende les beoordeelt permanente systemen voordat je ze activeert.

## Voer een gecontroleerde lus uit

**Begin met het ongewijzigde lab.** De twee basistests slagen. Maak in de nieuwe extractie `tests/test_loop_contract.py` met de onderstaande controle. Dit bestand beschrijft een gewenste functie die in de starter ontbreekt. Het hoort niet bij de onderhouden starter-ZIP.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Voer `python3 -m unittest discover -s tests -v` uit.** De twee oorspronkelijke tests horen te slagen en de nieuwe contracttest hoort te mislukken omdat de starter geen `--status` ondersteunt. Leg de echte fout vast. Als je Git volgens les 0 hebt geïnitialiseerd, leg dan ook `git status --short` vast. Vergelijk anders de gewijzigde bestanden met een ongewijzigde extractie. Gebruik in Windows `py -3` als je installatie de launcher gebruikt.

**Stel een budget van drie pogingen in:** de eerste wijziging en maximaal twee correcties. Geef je agent het luscontract hierboven en vraag om één begrensde wijziging. Controleer na elke poging de gewijzigde bestanden, voer alle tests opnieuw uit en probeer de standaardopdracht, `open`, `done` en een ongeldige waarde. Leg de oorzaak vast voordat je opnieuw probeert. Stop wanneer een controle slaagt, een ongerelateerde basistest faalt, er een wijziging buiten de scope plaatsvindt of de derde poging mislukt.

**Studieroute:** pas de volledige [oplossing van les 5](/articles/effective-ai-coding-agent-first-task/) toe in deze nieuwe kopie nadat je de rode test hebt vastgelegd. Voer dezelfde controles opnieuw uit en noteer dat de agentwijziging niet is uitgevoerd. Behoud de gecontroleerde contracttest. Verzwak of verwijder de test niet om hem te laten slagen.

| Poging | Status en waarneming | Beslissing |
|---|---|---|
| **Voor de wijziging** | De twee basistests slagen en de nieuwe controle voor `open` mislukt | Ga verder met één begrensde wijziging |
| **Na elke wijziging** | Leg exacte tests, aantallen, exitcode voor ongeldige invoer en gewijzigde bestanden vast | Accepteer, diagnoseer of stop |
| **Bij een opgebruikt budget** | Leg de resterende fout en huidige diff vast | Draag over zonder nieuwe poging |

## Oefen en controleer

**Je resultaat:** de gecontroleerde test die faalt, waargenomen uitvoer voor en na de wijziging, een pogingenlogboek en een definitieve keuze om te accepteren of te stoppen. Als de eerste wijziging slaagt, leg dan één poging vast. Verzin geen tweede fout om het logboek te vullen.

**Voltooiingscontrole:** het contract noemt een bron, bestandsscope, waarneembare controles, een limiet voor nieuwe pogingen, minstens één onmiddellijke stopvoorwaarde en een overdracht. Je logboek bevat de echte rode test, latere resultaten en een geslaagde uitkomst of stop wegens het budget. Een tweede poging noemt een nieuwe oorzaak en verschilt van de eerste.

## Controleer je begrip

1. **Vraag:** wat bewijst de eerste rode contracttest? **Antwoord:** dat de starter het gevraagde statusfilter mist, aangetoond door een test die vóór de wijziging is geschreven.
2. **Vraag:** wanneer moet de lus stoppen terwijl er nog pogingen over zijn? **Antwoord:** bij een wijziging buiten de scope, onduidelijke toestemming of een conflicterende eis.

## Problemen oplossen

- **De lus herhaalt dezelfde fout:** stop en formuleer een nieuwe hypothese voor de oorzaak.
- **Controles worden zwakker:** herstel de oorspronkelijke acceptatiecriteria.
- **Onzekere externe uitkomst:** controleer de actuele status voordat je opnieuw probeert.
- **Budget op:** draag het foutenlogboek over in plaats van de fout te verbergen.

## Volgende stappen

Ga verder met de optionele [Evaluatie van gespecialiseerde agents](/articles/effective-ai-specialized-agent-evaluation/) of ga direct naar het [eindproject voor de AI-workflowcursus](/articles/effective-ai-capstone/). Lees voor meer runtime-opties de [gids voor agentharnassen](/articles/best-ai-agent-harnesses/).

**Cursusnavigatie:** [Vorige: Agentdelegering](/articles/effective-ai-agent-delegation/), [Cursusoverzicht](/effective-ai-course-start/).
