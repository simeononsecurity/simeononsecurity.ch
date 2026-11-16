---
title: "AI-workflowcapstone: een JSON-rapport bouwen en controleren"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Bouw een nieuw JSON-taakrapport met projectcontext, een afgebakende agentopdracht, onafhankelijke tests, broncontrole en een overdracht voor een nieuwe sessie."
genre: ["Kunstmatige intelligentie", "Softwareontwikkeling", "Onderwijs"]
tags: ["AI-workflowcapstone", "codeeragentproject", "AI-taakverificatie", "AGENTS.md", "MCP-oefening", "agentoverdracht"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Afgeronde softwaretaak uit de workshop met bronbestanden, testresultaten, agentcontrole en overdrachtsnotitie"
coverCaption: ""
---

[Terug naar de cursus Praktische AI-workflow](/effective-ai-course-start/)

**Bouw een nieuw uitvoerformaat en bewijs hoe het werkt.** Eerder voegde je een statusfilter toe. Deze capstone begint met een nieuw lab en voegt een JSON-rapport toe dat een ander programma kan lezen. De nieuwe eis toetst of je je workflow naar een andere functie overdraagt.

**Leerdoel:** je levert een gecontroleerd JSON-rapport, een registratie van bewijs uit bronnen en tools, en een overdracht die een nieuwe sessie begrijpt.

## Belangrijkste punten

- **Een aparte eis** bepaalt de capstonefunctie.
- **Een wijziging door een codeeragent** blijft binnen de genoemde bestanden.
- **Onafhankelijke controles** bepalen de acceptatie.
- **Een overdracht aan een nieuwe sessie** maakt het resultaat reconstrueerbaar.

## Voordat je begint

**Vereisten:** voltooi lessen 0 tot en met 10, waaronder repositorycontext, de eerste codeertaak, MCP of de browseralternatief, delegatie en begrensde rondes. Les 11 is optioneel. Reken op 90 tot 120 minuten. Moeilijkheidsgraad: gemiddeld.

**Gebruik een nieuwe uitpakmap** van het [startlab](/downloads/effective-ai-course-lab.zip). Voer `python3 task_report.py tasks.json` en de twee basistests uit voordat je iets wijzigt. Gebruik op Windows `py -3` als je Python Launcher gebruikt. Maak een lokale Git-basisversie zoals bij de cursusinstelling. Het statusfilter uit les 5 ontbreekt bewust.

**Lees `docs/capstone-requirements.md`, revisie 1.** Dit bestand vereist `--format text|json`. De standaardtekst blijft `Total tasks: 4`. JSON-uitvoer bevat een numeriek totaal en aantallen voor iedere status in de gegevens. Test een lege lijst, een ontbrekende status en een niet-ondersteund formaat. Gebruik `docs/requirements.md` niet als gezaghebbende bron voor deze nieuwe functie.

**Kies je route.** De verbonden route gebruikt een waargenomen wijziging door een codeeragent, een echte alleen-lezen MCP-aanroep en een native worker of aparte workersessie. De studieroute gebruikt een chatassistent om code voor te stellen, een browserbron in plaats van MCP en aparte chats als nagebootste workers. Markeer niet-beschikbare toolstappen als ‘niet uitgevoerd’. Beide routes vereisen lokale tests en bestandscontrole. De antwoordsleutel hieronder bevat volledige bestanden als hersteloptie. Bewaar je eerste poging in notities voordat je de antwoordsleutel naar een nieuwe uitpakmap kopieert.

## Controlepunt 1: Projectbrief

**Open het synthetische ChatGPT- of Claude-workshopproject.** Vraag om een herinneringsconcept van twee zinnen. Controleer de tijd van 19.00 uur aan de hand van `approved-schedule.md`. De planning bepaalt de herinnering. De capstone-eis bepaalt het programma.

**Bewijs:** noteer de projectnaam, bronrevisie, waargenomen tijd in het concept en eventuele correctie. Verstuur het bericht niet.

## Controlepunt 2: Repositorycontext

**Open het nieuwe lab.** Maak een kort `AGENTS.md` met verwijzingen naar `docs/capstone-requirements.md`, `task_report.py`, de tests en het tijdens de setup bewezen testcommando. Gebruik je Claude Code, importeer dan het gedeelde bestand vanuit `CLAUDE.md`. Maak een menselijke setupcommit voor deze instructiebestanden en controleer daarna dat `git status --short` leeg is. De codeeragent mag de functiewijziging niet committen.

**Bewijs:** bewaar de kaart en een schone kopie van de instructies. Noteer de JSON-sleutels en het gedrag bij ongeldige invoer uit revisie 1. Behandel een eerdere chat over het statusfilter als achtergrond voor een andere taak.

## Controlepunt 3: Externe bron

**Verbonden route:** gebruik de alleen-lezen [MCP-server voor OpenAI-documentatie](https://learn.chatgpt.com/learn/docs-mcp) via een ondersteunde client. Vraag een MCP-tool naar de actuele richtlijnen voor `AGENTS.md`. Noteer de toolnaam, bron-URL en een relevant punt voor je lab. Verwijder daarna de oefenverbinding.

**Studieroute:** open de [officiële documentatie voor `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md) in een browser. Noteer titel, URL en een relevant punt. Markeer MCP-ontdekking en -uitvoering als ‘niet uitgevoerd’.

**Bewijs:** een geconfigureerde serververmelding bewijst niet dat de server is gebruikt. De verbonden route vereist een zichtbare toolaanroep en geretourneerde broninhoud.

## Controlepunt 4: Eén beoordeling delegeren

**Vraag een alleen-lezen worker** om `docs/capstone-requirements.md`, `task_report.py` en de basistests te bekijken. Vraag om een rapport van maximaal vijf regels met ontbrekende controles en bestandspaden. Gebruik bij de studieroute een aparte chat en markeer die als nagebootste worker.

**Verwachte bevinding:** de starttests controleren het totaal en een JSON-waarde die geen lijst is. Ze controleren niet de JSON-uitvoer, een lege lijst, een ontbrekende status of een ongeldig formaat. Open zelf het testbestand om het rapport te controleren. Een korte onafhankelijke beoordeling is nuttig, omdat de acceptatiecriteria afwijken van les 5.

**Bewijs:** bewaar het korte rapport en je integratiebesluit in één zin. Bewaar het workertranscript buiten het hoofdtaaklogboek.

## Controlepunt 5: De wijziging aanvragen

**Geef een codeeragent** het volgende pakket. Bij de studieroute stelt een chatassistent een patch voor, die je handmatig in het lab toepast.

```text
Doel: voeg --format text|json toe na het JSON-pad.
Bron: docs/capstone-requirements.md, revisie 1.
Toegestane wijzigingen: task_report.py en tests/test_task_report.py.
Behouden: standaarduitvoer Total tasks: 4 en tasks.json ongewijzigd.
JSON: één object met total en by_status-aantallen, geen extra tekst naar stdout.
Vereiste controles: standaard en expliciete tekst, JSON 4/2/2, lege lijst,
ontbrekende status, ongeldig formaat en basistests.
Stoppen bij: bronconflict, ongerelateerde basistestfout of wijziging buiten bereik.
Rapport: gewijzigde bestanden, opdrachten, waargenomen uitvoer, onopgelost probleem.
Niet committen, pushen, publiceren of een bericht versturen.
```

**Controleer het plan** voordat de agent iets wijzigt. De schemakeuze telt: `total` is een getal, niet de tekenreeks `"4"`. `by_status` bevat iedere status uit de invoer, ook een toekomstige status. Houd de wijziging binnen het uitgepakte lab.

## Controlepunt 6: Testen en beoordelen

**Voer deze controles zelf uit.** Vervang op Windows `python3` door `py -3`. De exacte JSON-sleutelvolgorde en witruimte doen er niet toe. Parseer de uitvoer als JSON en vergelijk de getypeerde waarden.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Verwacht gedrag:** de tests slagen. Beide tekstcommando’s tonen `Total tasks: 4`. Het JSON-commando retourneert één object met `total` 4, `by_status.open` 2 en `by_status.done` 2. Een ongeldig formaat eindigt met een niet-nulstatuscode. De tests behandelen ook een lege invoer en een taak zonder tekstuele `status`. Lees de waargenomen foutuitvoer en exitcode voor deze gevallen.

| Controlepunt | Bewijs van slagen | Herstel bij mislukking |
|---|---|---|
| **Projectbrief** | Herinnering noemt 19.00 uur | Ververs de planningsbron |
| **Repositorykaart** | Capstone-eis en testpaden genoemd | Herstel de instructiebestanden |
| **Externe bron** | MCP-bron gelezen of browseralternatief vermeld | Controleer verbinding of URL |
| **Workerbeoordeling** | Ontbrekende tests in het bestand bevestigd | Herstel het worker-rapport |
| **Bestandsbereik** | Alleen programma en tests | Controleer iedere ongewenste wijziging |
| **Gedrag** | Tekst, JSON, lege invoer en fouten gecontroleerd | Stel één oorzaak vast en probeer opnieuw |
| **Overdracht** | Nieuwe sessie reconstrueert de status | Voeg ontbrekende bron of resultaat toe |

**Gebruik een nieuwe uitpakmap als veilige reset.** Bewaar je notities buiten het lab, verwijder alleen de wegwerpkopie en pak de oorspronkelijke ZIP opnieuw uit. Gebruik geen brede Git-reset in een repository met werk dat je wilt behouden.

## Controlepunt 7: Overdracht naar een nieuwe sessie

**Schrijf buiten de labmap een overdracht van minder dan 180 woorden.** Vermeld de revisie van de capstone-eis, gewijzigde bestanden, exact testcommando en resultaat, tekst- en JSON-uitvoer, controles voor ongeldige invoer, gebruikslog en openstaande actie. Open een nieuwe sessie en vraag welke JSON-sleutels gelden en of de functie is geslaagd.

**Verwacht antwoord:** de nieuwe sessie noemt `total` en `by_status`, verwijst naar revisie 1, meldt alleen waargenomen controles en wijst op iedere ontbrekende controle.

## Antwoordsleutel en beoordelingsrubriek

**Een geldige implementatie** staat hieronder. Sla het eerste blok op als `task_report.py` en het tweede als `tests/test_task_report.py` in een nieuwe uitpakmap van het lab. Laat `tasks.json` en beide eisbestanden ongewijzigd. Voer de controles van controlepunt 6 uit. Vergelijk een andere oplossing met de eis en het waargenomen gedrag.

`task_report.py`:

```python
"""Drukt een tekstrapport of JSON-overzicht van workshoptaken af."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Workshoptaakrapport")
    parser.add_argument("path", type=Path, help="pad naar de JSON-takenlijst")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Controles voor tekst- en JSON-rapporten van workshoptaken."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Herstel na gebruik van de antwoordsleutel:** bewaar je notities buiten het lab, verwijder deze uitpakmap en pak het oorspronkelijke startlab opnieuw uit. De nieuwe kopie bevat de twee basistests en geen implementatie van de functie.

**Geef één punt voor elk controlepunt** in de tabel hierboven. Zeven punten voltooien de verbonden route als de externe bronregel een echte MCP-aanroep bevat en de workerregel een echte sessie vastlegt. Zeven punten voltooien de studieroute als de bron een gecontroleerde browserpagina is en toolstappen expliciet als ‘niet uitgevoerd’ zijn gemarkeerd. Een ontbrekende controle van gedrag, bron of bestandsbereik blokkeert beide routes.

## Controleer je begrip

1. **Welke eis bepaalt deze functie?** `docs/capstone-requirements.md`, revisie 1. De eerdere statusfilter-eis hoort bij les 5.
2. **Wat bewijst het JSON-contract?** Parseer de opdrachtuitvoer, vergelijk numerieke waarden en de aantallen van iedere status, en controleer lege en ongeldige invoer. Een gepolijste agentsamenvatting is onvoldoende.

## Problemen oplossen

- **De basistest faalt vóór de wijziging:** herstel het lab vanuit de ZIP en voer de setup opnieuw uit.
- **De agent wijzigt een ander bestand:** controleer de diff en herstel alleen de ongewenste labwijziging.
- **De MCP-verbinding faalt:** gebruik de browserbron en markeer het controlepunt als studieroute.
- **De worker herhaalt een verkeerde waarde:** lees de capstone-eis opnieuw en corrigeer het rapport.
- **Het aantal pogingen is op:** bewaar het foutenlog en vraag een menselijke reviewer om de volgende stap.

## Volgende stappen

**Bewaar je voltooide bewijsregistratie.** Ga voor geavanceerde teampublicatie en autoriteit tussen systemen verder met de [cursus Implementatie van AI-samenwerking](/ai-collaboration-course-start/).

**Cursusnavigatie:** [Vorige verplichte les: begrensde rondes](/articles/effective-ai-bounded-agent-loops/), [Optioneel: evaluatie van gespecialiseerde agents](/articles/effective-ai-specialized-agent-evaluation/), [Cursusoverzicht](/effective-ai-course-start/).
