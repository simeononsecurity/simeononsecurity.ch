---
title: "Voer je eerste repositorytaak uit met een codeeragent"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Kies een interface voor een codeeragent, open een voorbeeldrepository, beoordeel een voorgestelde wijziging en voer controles uit voordat je de wijziging behoudt."
genre: ["Kunstmatige intelligentie", "Softwareontwikkeling"]
tags: ["Codex CLI-handleiding", "Codex-app", "Claude Code CLI", "OpenCode-handleiding", "workflow voor codeeragenten", "AI-programmeertools"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Een coderepository met aparte terminal- en desktopweergaven van de agent naast een beoordeeld bestandsverschil"
coverCaption: ""
---

[Terug naar de cursus Praktische AI-workflow](/effective-ai-course-start/)

**Een codeeragent leest bestanden, stelt wijzigingen voor en voert tools uit in een werkruimte.** In deze les voer je een kleine repositorytaak uit. Kies Codex in de ChatGPT-desktopapp of CLI, Claude Code CLI of OpenCode TUI. Beoordeel daarna een wijziging voordat je die accepteert.

**Leerdoel:** voer één afgebakende wijziging uit of pas die handmatig toe en controleer het verschil en het gedrag.

## Belangrijkste punten

- **Codex in de ChatGPT-desktopapp** biedt een visuele werkruimte voor taken en beoordeling.
- **Codex CLI** start een Codex-sessie vanuit je terminal.
- **Claude Code CLI** voert Claude's programmeerworkflow uit vanuit je terminal.
- **OpenCode TUI** biedt een terminalworkflow met instelbare providers en machtigingen.
- **Een verschil en een testresultaat** wegen zwaarder dan een voltooiingsbericht van de assistent.

## Voordat je begint

**Vereisten:** voltooi de [cursusinstellingen](/articles/effective-ai-course-setup/), inclusief de nulmeting en de lokale Git-snapshot. Voltooi [repositorycontext](/articles/effective-ai-agents-md-context/) en [taakpakketten](/articles/effective-ai-task-packets/) vóór deze les. Gebruik een codeeragent waarvoor je toegang hebt. Trek 45 minuten uit. Het niveau loopt van beginner tot gemiddeld.

**Gebruik het [cursusstartlab](/downloads/effective-ai-course-lab.zip)** in een wegwerpmap. Het archief bevat een klein takenrapportprogramma, voorbeeldgegevens en tests. Gebruik geen productierepository voor je eerste wijziging. Voeg een `--status`-filter toe en behoud de bestaande totaaltelling.

## Studieroute zonder codeeragent

**Vraag een chatassistent dezelfde wijziging voor te stellen** als er geen codeeragent beschikbaar is. Plak alleen `docs/requirements.md`, `task_report.py` en het gerichte testbestand uit het synthetische lab. Vraag om een uniforme diff en een korte uitleg. Een uniforme diff toont oude regels met `-` en nieuwe regels met `+`. Open het genoemde bestand in een teksteditor, vervang de oude regels door het voorstel en sla het op. Voer daarna alle opdrachten onder Resultaat beoordelen uit. Laat `tasks.json` ongewijzigd. Noteer dat je de stap met de codeeragent hebt overgeslagen. De eindopdracht bevat een aparte JSON-functie. Vergelijk je filteroplossing dus met de eis en controles uit les 5.

## Kies een interface

**Kies eerst een beoordelingsomgeving.** Codex in de ChatGPT-desktopapp past bij visueel projectwerk en diffbeoordeling. Een terminalinterface past bij werk in de uitgepakte labmap. Vergelijk de terminalopties met elkaar:

| Terminaltool | Account- of providercontrole | Startopdracht |
|---|---|---|
| **Codex CLI** | Bevestig je Codex-aanmelding en lokale machtigingen | `codex` |
| **Claude Code CLI** | Bevestig je Claude Code-toegang en lokale machtigingen | `claude` |
| **OpenCode TUI** | Stel een ondersteunde modelprovider en machtigingen in | `opencode` |

**Installeer de tool en meld je aan met de actuele officiële handleiding.** Lees [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [ChatGPT-desktopapp](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) of [OpenCode](https://opencode.ai/docs/). Opdrachten, ondersteunde platforms en accountvereisten veranderen. Deze les gebruikt stabiele startnamen en één gedeelde beoordelingsprocedure.

**Lees voor een uitgebreidere productkeuze** de vergelijking van [CLI-codeeragenten](/articles/cli-coding-agents-comparison/) of [codeeragenten met grafische interface](/articles/gui-coding-agents-comparison/) op de site. De handleidingen voor [Codex CLI en desktop](/articles/codex-cli-vs-desktop/), [Claude Code CLI en desktop](/articles/claude-code-cli-vs-desktop/) en [OpenCode CLI en desktop](/articles/opencode-cli-vs-desktop/) vergelijken de interfaces van elk product.

**Begin in de labmap.** Elke interface vereist een expliciete keuze van de werkruimte:

1. **Codex desktop:** open de ChatGPT-desktopapp, selecteer het uitgepakte lab als lokaal project en start daar een lokale taak. Controleer het mappad en goedkeuringsverzoeken voordat de agent iets wijzigt. Een gehoste taak gebruikt een aparte werkkopie.
2. **Codex CLI:** voer `cd /path/to/effective-ai-course-lab` uit en daarna `codex`. Controleer de getoonde werkmap en goedkeuringsmodus.
3. **Claude Code CLI:** voer dezelfde opdracht `cd` uit en daarna `claude`. Controleer de projectmap en toolmachtigingen.
4. **OpenCode TUI:** voer dezelfde opdracht `cd` uit en daarna `opencode`. Controleer de gekozen provider, het project en de machtigingen.

**ChatGPT-chat en Claude Projects beheren gesprekken en gedeelde referentiebestanden.** Codex en Claude Code werken in een codewerkruimte met tools voor bestanden en opdrachten. OpenCode biedt ook desktop- en IDE-omgevingen, maar deze les gebruikt de terminalinterface. Provider, account en lokale of gehoste uitvoering verschillen. Noteer daarom de gekozen omgeving in plaats van alle sessies als dezelfde uitvoering te behandelen.

**Controleer vijf punten voordat je het lab opent:** ondersteund besturingssysteem, verificatie, kosten van provider of account, machtigingen voor bestanden en opdrachten, en lokale uitvoering of uitvoering op een externe host. Noteer je keuze. Ga er niet van uit dat een desktopapp en een terminaltool dezelfde werkruimte gebruiken.

## Bekijk het startproject

**Open de schone labmap opnieuw** uit de les over repositorycontext. Deze kopie bevat je vastgelegde `AGENTS.md` en de optionele instructies in `CLAUDE.md`. Bekijk de bestanden voordat je de agent om een wijziging vraagt. Voer de nulmetingtests vanuit deze map uit.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Verwachte nulmeting:** het rapport toont `Total tasks: 4`. De testuitvoer noemt twee tests en eindigt met `OK`. Stop en bekijk de uitgepakte bestanden als een test faalt. Laat de agent geen defecte beginsituatie herstellen.

**Gebruik de lokale Git-snapshots** uit de cursusinstellingen en de les over repositorycontext. `AGENTS.md` en het optionele `CLAUDE.md` moeten al zijn vastgelegd. Voer vóór de functieaanpassing `git status --short` uit en verwacht geen bestanden. De agent mag evenmin een commit maken. Het archief bevat geen Git-geschiedenis. Het `.gitignore`-bestand sluit Python-bytecode uit die tijdens testuitvoeringen wordt gegenereerd. Heb je een nieuwe kopie uitgepakt, herhaal dan de cursusinstellingen en de contextles in die map. Leg de instructiebestanden vast vóór de functieaanpassing. Initialiseer en commit eerst het startproject:

```bash
git init
git add .
git commit -m "Basis voor cursuslab"
```

**Voeg daarna `AGENTS.md` en het optionele `CLAUDE.md` toe** met de goedgekeurde bron en testopdracht uit de contextles. Commit die bestanden, controleer of `git status --short` schoon is en begin dan met de functieaanpassing. Voer deze opdrachten uit in je uitgepakte oefenmap, niet in de hoofdmap van een andere repository.

## Geef een afgebakende opdracht

**Open de labmap** in je gekozen codeeragent. Stuur dit taakpakket:

```text
Voeg een optioneel --status-argument toe aan task_report.py.
Toegestane waarden: open en done.
Laat de huidige uitvoer van de totaaltelling ongewijzigd als het argument ontbreekt.
Tel alleen overeenkomende taken en toon Total tasks: N als het argument aanwezig is.
Voeg tests toe voor beide waarden, een ongeldige waarde en de ongewijzigde standaarduitvoer.
Wijzig tasks.json en niet-gerelateerde bestanden niet.
Voer de tests uit en meld de exacte opdracht en het resultaat.
Stop na de code en tests. Maak geen commit en voer geen push uit.
```

**Op Windows** vervang je `python3` door de tijdens de installatie gecontroleerde opdracht `py -3`, ook in de opgeslagen repository-instructies en het taakpakket.

**Vraag eerst om een kort plan** als je de code niet kent. Geef de agent alleen toestemming om de wegwerpmap van het lab te wijzigen. Machtigingsinstellingen verschillen per tool. Controleer de actuele instellingen voordat je shellopdrachten of bestandsschrijfrechten toestaat.

## Beoordeel het resultaat

**Lees de diff.** Controleer of de uitvoer zonder filter gelijk blijft, de filter maar twee waarden accepteert en de tests de fout en ongewijzigde standaarduitvoer behandelen. Geslaagde tests bevestigen de wijziging alleen als ze het gevraagde gedrag controleren.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Verwachte resultaten:** de eerste drie rapportopdrachten tonen aantallen 4, 2 en 2. De ongeldige waarde toont een duidelijke fout en eindigt met een niet-nulstatus. De precieze fouttekst hangt van de implementatie af. Voer op macOS of Linux direct na de ongeldige opdracht `echo $?` uit om de afsluitcode te zien. Controleer in PowerShell `$LASTEXITCODE`.

| Bewijs | Wat je controleert |
|---|---|
| **Bestandenlijst** | Alleen het programma en de tests zijn gewijzigd |
| **Diff** | De filterlogica voldoet aan de opdracht |
| **Testuitvoer** | De nieuwe gevallen zijn uitgevoerd en geslaagd |
| **Handmatige uitvoering** | De aantallen voor standaard, `open` en `done` kloppen met `tasks.json` |

**Voert de agent geen tests uit,** voer de opdracht dan zelf uit. Valt de wijziging buiten het taakpakket, vraag om een afgebakende correctie. Is de toestand onduidelijk, verwijder dan de uitgepakte oefenkopie en pak de originele ZIP opnieuw uit.

## Antwoorden voor de studieroute

**Gebruik deze volledige bestanden als je handmatige patch mislukt.** Begin met een nieuw uitgepakt lab, sla het eerste blok op als `task_report.py` en het tweede als `tests/test_task_report.py`. Voer daarna de opdrachten onder Resultaat beoordelen uit. Laat `tasks.json` en `docs/requirements.md` ongewijzigd. Noteer de oorspronkelijke fout voordat je de bestanden kopieert.

`task_report.py`:

```python
"""Toont het aantal taken in een JSON-bestand."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Telt alle taken of taken met een toegestane status."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Workshoptaakjes tellen")
    parser.add_argument("path", type=Path, help="pad naar de JSON-takenlijst")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Tests voor het takenrapport van de workshop."""

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


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Bewaar een aangepaste kopie met geslaagde filtertests** voor de lessen over context en resultaatcontrole. Heb je dit volledige voorbeeld als herstel gebruikt, bewaar dan de nieuwe kopie met geslaagde filtertests voor die lessen. Bewaar de diff en het testverslag buiten het lab. Herstel het startproject vóór de delegatieles of verwijder een mislukte poging om schoon opnieuw te beginnen.

## Oefen en controleer

**Je resultaat:** een labdiff en een beoordelingsnotitie van vier regels over de bestandsomvang, het standaardgedrag, het filtergedrag en ongeldige invoer. Noteer de toolnaam en versie privé, zodat je een versiespecifiek probleem kunt reproduceren.

**Verwachte redenering:** je koos een passende interface, gaf een afgebakende opdracht, bekeek de echte wijziging en voerde een controle uit die onafhankelijk was van het agentverslag.

## Controleer je begrip

1. **Vraag:** Wat bewijst dat de statusfilterwijziging werkt? **Antwoord:** Een afgebakende diff, geslaagde tests en waargenomen resultaten voor standaard, open, done en ongeldige invoer.
2. **Vraag:** Geldt de melding van de agent dat deze tests heeft uitgevoerd als jouw testresultaat? **Antwoord:** Nee. Voer de opdracht uit of bekijk de testuitvoer.

## Problemen oplossen

- **Opdracht ontbreekt:** voltooi de installatie met de gekoppelde leveranciershandleiding en open de terminal opnieuw.
- **Geen bestandstoegang:** open de uitgepakte labmap en controleer de machtigingen van de werkruimte.
- **Onverwachte bestanden gewijzigd:** stop en controleer `git status --short` voordat je een nieuwe opdracht geeft.
- **Tests slagen maar gedrag klopt niet:** voeg een handmatig geval of test voor de ontbrekende eis toe.

## Volgende stappen

**Ga verder met [Contextvensters en overdrachten](/articles/effective-ai-context-window-management/)**. Je bewaart een nuttig verslag voor een nieuwe sessie.

**Cursusnavigatie:** [Vorige: Taakpakketten](/articles/effective-ai-task-packets/), [Cursusoverzicht](/effective-ai-course-start/).
