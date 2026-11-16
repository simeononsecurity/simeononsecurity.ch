---
title: "Führe deine erste Repository-Aufgabe mit einem Programmieragent aus"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Wähle eine Programmieragent-Oberfläche, öffne ein Beispiel-Repository, prüfe einen Änderungsvorschlag und führe Prüfungen aus, bevor du die Bearbeitung übernimmst."
genre: ["Künstliche Intelligenz", "Softwareentwicklung"]
tags: ["Codex-CLI-Anleitung", "Codex-App", "Claude Code CLI", "OpenCode-Anleitung", "Programmieragent-Arbeitsablauf", "KI-Programmierwerkzeuge"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Ein Code-Repository mit getrennten Terminal- und Desktop-Agentansichten neben einer geprüften Dateidifferenz"
coverCaption: ""
---

[Zurück zum Kurs Praktischer KI-Arbeitsablauf](/effective-ai-course-start/)

**Ein Programmieragent liest Dateien, schlägt Änderungen vor und führt Werkzeuge in einem Arbeitsbereich aus.** In dieser Lektion bearbeitest du eine kleine Repository-Aufgabe. Wähle Codex in der ChatGPT-Desktop-App oder CLI, Claude Code CLI oder OpenCode TUI. Prüfe anschließend eine Änderung, bevor du sie übernimmst.

**Lernziel:** Du führst eine klar abgegrenzte Änderung aus oder wendest sie manuell an und prüfst die Differenz und das Verhalten.

## Wichtigste Erkenntnisse

- **Codex in der ChatGPT-Desktop-App** bietet einen visuellen Arbeitsbereich für Aufgaben und Prüfungen.
- **Codex CLI** startet eine Codex-Sitzung in deinem Terminal.
- **Claude Code CLI** führt den Programmierablauf von Claude im Terminal aus.
- **OpenCode TUI** bietet einen Terminal-Arbeitsablauf mit konfigurierbaren Anbietern und Berechtigungen.
- **Eine Differenz und ein Testergebnis** zählen mehr als eine Abschlussmeldung des Assistenten.

## Vor dem Start

**Voraussetzungen:** Schließe die [Kurseinrichtung](/articles/effective-ai-course-setup/) ab, einschließlich des ersten Durchlaufs und der lokalen Git-Aufnahme. Bearbeite vor dieser Lektion [Repository-Kontext](/articles/effective-ai-agents-md-context/) und [Aufgabenpakete](/articles/effective-ai-task-packets/). Verwende einen Programmieragent, auf den du zugreifen darfst. Plane 45 Minuten ein. Der Schwierigkeitsgrad reicht von Anfänger bis Mittelstufe.

**Verwende das [Kurs-Startlabor](/downloads/effective-ai-course-lab.zip)** in einem entbehrlichen Ordner. Das Archiv enthält ein kleines Aufgabenberichtsprogramm, Beispieldaten und Tests. Verwende für deine erste Änderung kein Produktions-Repository. Deine Aufgabe ist, einen `--status`-Filter hinzuzufügen und die vorhandene Gesamtzahl beizubehalten.

## Lernweg ohne Programmieragent

**Lass einen Chat-Assistenten dieselbe Änderung vorschlagen**, falls kein Programmieragent verfügbar ist. Füge nur `docs/requirements.md`, `task_report.py` und die gezielte Testdatei aus dem synthetischen Labor ein. Bitte um eine vereinheitlichte Differenz und eine kurze Erklärung. Eine vereinheitlichte Differenz markiert alte Zeilen mit `-` und neue Zeilen mit `+`. Öffne die genannte Datei in einem Texteditor, ersetze die alten Zeilen durch den Vorschlag und speichere sie. Führe anschließend alle Befehle unter Ergebnis prüfen aus. Lass `tasks.json` unverändert. Notiere, dass du den Programmieragent-Schritt nicht ausgeführt hast. Das Abschlussprojekt enthält eine separate JSON-Funktion. Vergleiche deine Filterlösung daher mit der Anforderung und den Prüfungen aus Lektion 5.

## Wähle eine Oberfläche

**Wähle zuerst eine Prüfoberfläche.** Codex in der ChatGPT-Desktop-App passt zu einem visuellen Projekt und zur Prüfung von Differenzen. Eine Terminaloberfläche eignet sich für die Arbeit im entpackten Laborordner. Vergleiche Terminaloptionen untereinander:

| Terminalwerkzeug | Konto- oder Anbieterprüfung | Startbefehl |
|---|---|---|
| **Codex CLI** | Bestätige die Codex-Anmeldung und lokale Berechtigungen | `codex` |
| **Claude Code CLI** | Bestätige den Claude-Code-Zugriff und lokale Berechtigungen | `claude` |
| **OpenCode TUI** | Richte einen unterstützten Modellanbieter und Berechtigungen ein | `opencode` |

**Installiere und melde dich mit der aktuellen offiziellen Anleitung** für dein Werkzeug an. Lies [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [ChatGPT-Desktop-App](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) oder [OpenCode](https://opencode.ai/docs/). Befehle, unterstützte Plattformen und Kontoanforderungen ändern sich. Diese Lektion verwendet nur die stabilen Startnamen und ein gemeinsames Prüfverfahren.

**Für eine ausführlichere Produktauswahl** lies den Vergleich der [Programmieragenten für die CLI](/articles/cli-coding-agents-comparison/) oder der [Programmieragenten mit grafischer Oberfläche](/articles/gui-coding-agents-comparison/) auf der Website. Die Anleitungen zu [Codex CLI und Desktop](/articles/codex-cli-vs-desktop/), [Claude Code CLI und Desktop](/articles/claude-code-cli-vs-desktop/) sowie [OpenCode CLI und Desktop](/articles/opencode-cli-vs-desktop/) vergleichen die Oberflächen der jeweiligen Produkte.

**Starte im Laborordner.** Bei jeder Oberfläche musst du einen Arbeitsbereich ausdrücklich auswählen:

1. **Codex Desktop:** Öffne die ChatGPT-Desktop-App, wähle das entpackte Labor als lokales Projekt aus und starte dort eine lokale Aufgabe. Prüfe vor einer Änderung den Ordnerpfad und die Genehmigungsabfragen. Eine gehostete Aufgabe verwendet eine separate Arbeitsbereichskopie.
2. **Codex CLI:** Führe `cd /path/to/effective-ai-course-lab` und dann `codex` aus. Bestätige den angezeigten Arbeitsordner und den Genehmigungsmodus.
3. **Claude Code CLI:** Führe denselben `cd`-Befehl und dann `claude` aus. Bestätige den Projektordner und die Werkzeugberechtigungen.
4. **OpenCode TUI:** Führe denselben `cd`-Befehl und dann `opencode` aus. Bestätige den gewählten Anbieter, das Projekt und die Berechtigungseinstellungen.

**ChatGPT-Chat und Claude Projects verwalten Unterhaltungen und gemeinsame Referenzdateien.** Codex und Claude Code arbeiten in einem Code-Arbeitsbereich mit Datei- und Befehlswerkzeugen. OpenCode bietet auch Desktop- und IDE-Oberflächen, aber diese Lektion nutzt die Terminaloberfläche. Anbieter, Konto und lokale oder gehostete Ausführung unterscheiden sich. Notiere daher die gewählte Oberfläche, statt alle Sitzungen als denselben Durchlauf zu behandeln.

**Prüfe vor dem Öffnen des Labors fünf Punkte:** unterstütztes Betriebssystem, Authentifizierung, Kosten für Anbieter oder Konto, Datei- und Befehlsberechtigungen sowie lokale Ausführung oder Ausführung auf einem entfernten Host. Notiere deine Auswahl. Gehe nicht davon aus, dass eine Desktop-App und ein Terminalwerkzeug denselben Arbeitsbereich verwenden.

## Prüfe das Startprojekt

**Öffne den sauberen Laborordner aus der Lektion zum Repository-Kontext erneut.** Diese Kopie enthält dein committetes `AGENTS.md` und die optionale Anleitung `CLAUDE.md`. Prüfe die Dateien, bevor du den Agenten um eine Änderung bittest. Führe die Ausgangstests in diesem Ordner aus.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Erwarteter Ausgangszustand:** Der Bericht zeigt `Total tasks: 4`. Der Testlauf nennt zwei Tests und endet mit `OK`. Falls ein Test fehlschlägt, halte an und prüfe die entpackten Dateien. Schreibe dem Agenten keine Reparatur für einen fehlerhaften Ausgangszustand zu.

**Verwende die lokalen Git-Aufnahmen** aus der Kurseinrichtung und der Lektion zum Repository-Kontext. `AGENTS.md` und das optionale `CLAUDE.md` sollten bereits committet sein. Führe vor der Funktionsänderung `git status --short` aus und erwarte keine Dateien. Auch der Agent darf keinen Commit erstellen. Das Archiv enthält keine Git-Historie. Die Datei `.gitignore` schließt Python-Bytecode aus, der bei den Testläufen erzeugt wird. Wenn du eine neue Kopie entpackt hast, wiederhole die Kurseinrichtung und die Lektion zum Repository-Kontext in diesem Ordner. Commite die Anleitungsdateien vor der Funktionsänderung. Initialisiere und commite zuerst das Startprojekt:

```bash
git init
git add .
git commit -m "Kurslabor-Grundlage"
```

**Füge danach `AGENTS.md` und das optionale `CLAUDE.md` hinzu**, einschließlich der in der Lektion zum Repository-Kontext bestätigten Quelle und des Testbefehls. Commite diese Dateien, prüfe mit `git status --short` einen sauberen Status und beginne dann mit der Funktionsänderung. Führe diese Befehle im entpackten Übungsordner aus, nicht im Stammverzeichnis eines anderen Repositorys.

## Gib einen klar abgegrenzten Auftrag

**Öffne den Laborordner** in deinem gewählten Programmieragent. Sende dieses Aufgabenpaket:

```text
Füge task_report.py ein optionales --status-Argument hinzu.
Zulässige Werte: open und done.
Ohne Argument muss die bisherige Ausgabe der Gesamtzahl unverändert bleiben.
Mit Argument dürfen nur passende Aufgaben gezählt und Total tasks: N ausgegeben werden.
Füge Tests für beide Werte, einen ungültigen Wert und die unveränderte Standardausgabe hinzu.
Ändere weder tasks.json noch andere, nicht zugehörige Dateien.
Führe die Tests aus und melde den genauen Befehl und das Ergebnis.
Beende die Arbeit nach Code und Tests. Erstelle keinen Commit und pushe nichts.
```

**Unter Windows** ersetzt du `python3` durch den während der Einrichtung geprüften Befehl `py -3`, auch in den gespeicherten Repository-Anweisungen und im Aufgabenpaket.

**Bitte vor der Bearbeitung um einen kurzen Plan**, wenn du den Code noch nicht kennst. Erlaube dem Agenten, nur den entbehrlichen Laborordner zu bearbeiten. Berechtigungskontrollen unterscheiden sich je nach Werkzeug. Prüfe daher die aktuellen Einstellungen, bevor du Shell-Befehle oder Dateischreibzugriff erlaubst.

## Prüfe das Ergebnis

**Lies die Differenz.** Prüfe, ob die ungefilterte Ausgabe gleich bleibt, der Filter nur zwei Werte annimmt und die Tests den Fehlerfall sowie die unveränderte Standardausgabe abdecken. Ein erfolgreicher Testlauf belegt die Änderung nur, wenn der Test das gewünschte Verhalten prüft.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Erwartete Ergebnisse:** Die ersten drei Berichtsaufrufe zeigen 4, 2 und 2. Der ungültige Wert zeigt eine klare Fehlermeldung und endet mit einem Status ungleich null. Der genaue Wortlaut hängt von der Implementierung ab. Führe unter macOS oder Linux direkt nach dem ungültigen Befehl `echo $?` aus, um den Rückgabewert zu lesen. Prüfe in PowerShell `$LASTEXITCODE`.

| Nachweis | Zu prüfen |
|---|---|
| **Dateiliste** | Nur Programm und Tests ändern sich |
| **Differenz** | Die Filterlogik erfüllt den Auftrag |
| **Testausgabe** | Die neuen Fälle liefen erfolgreich |
| **Manueller Lauf** | Die Zählwerte für Standard, `open` und `done` stimmen mit `tasks.json` überein |

**Wenn der Agent ein Ergebnis ohne Testlauf meldet,** führe den Befehl selbst aus. Wenn die Änderung über das Aufgabenpaket hinausgeht, bitte um eine begrenzte Korrektur. Ist der Zustand unklar, lösche die entpackte Übungskopie und entpacke die Original-ZIP erneut.

## Antworten zum Lernweg

**Verwende diese vollständigen Dateien, falls dein manueller Patch fehlschlägt.** Beginne mit einem frisch entpackten Labor, speichere den ersten Block als `task_report.py` und den zweiten als `tests/test_task_report.py`. Führe danach die Befehle unter Ergebnis prüfen aus. Lass `tasks.json` und `docs/requirements.md` unverändert. Notiere den ursprünglichen Fehler, bevor du die Dateien kopierst.

`task_report.py`:

```python
"""Gibt die Anzahl der Aufgaben aus einer JSON-Datei aus."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Zählt alle Aufgaben oder Aufgaben mit einem zulässigen Status."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Aufgaben des Workshops zählen")
    parser.add_argument("path", type=Path, help="Pfad zur JSON-Aufgabenliste")
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
"""Tests für den Aufgabenbericht des Workshops."""

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

**Bewahre eine bearbeitete Kopie mit erfolgreichen Filtertests** für die Kontext- und Ergebnisprüfungslektionen auf. Wenn du mit dieser Antwortvorlage einen Fehler behoben hast, verwende für diese Lektionen die neue Kopie mit erfolgreichen Filtertests. Bewahre die Differenz und das Testprotokoll außerhalb des Labors auf. Setze das Startprojekt vor der Delegationslektion zurück oder verwirf einen fehlgeschlagenen Versuch, wenn du sauber neu beginnen musst.

## Übe und prüfe

**Dein Ergebnis:** eine Labordifferenz und ein vierzeiliger Prüfvermerk zu Dateiumfang, Standardverhalten, Filterverhalten und ungültiger Eingabe. Notiere Werkzeugname und Version in deinen privaten Aufzeichnungen, um ein versionsspezifisches Problem zu reproduzieren.

**Erwartete Überlegung:** Du hast eine passende Oberfläche gewählt, eine klar begrenzte Aufgabe gestellt, die tatsächliche Änderung geprüft und unabhängig von der Zusammenfassung des Agenten eine Prüfung ausgeführt.

## Prüfe dein Verständnis

1. **Frage:** Was belegt, dass die Statusfilter-Änderung funktioniert? **Antwort:** Eine begrenzte Differenz, erfolgreiche Tests und beobachtete Ergebnisse für Standardausgabe, open, done und den ungültigen Fall.
2. **Frage:** Zählt die Aussage des Programmieragent, er habe Tests ausgeführt, als dein Testergebnis? **Antwort:** Nein. Führe den Befehl aus oder prüfe die Testausgabe.

## Fehlerbehebung

- **Befehl fehlt:** Schließe die Installation anhand der verlinkten Anbieteranleitung ab und öffne das Terminal erneut.
- **Kein Dateizugriff:** Öffne den entpackten Laborordner und prüfe die Berechtigungen des Arbeitsbereichs.
- **Unerwartete Dateien geändert:** Halte an und prüfe `git status --short`, bevor du einen weiteren Auftrag sendest.
- **Tests erfolgreich, Verhalten falsch:** Füge einen manuellen Fall oder einen Test für die fehlende Anforderung hinzu.

## Nächste Schritte

**Fahre mit [Kontextfenstern und Übergaben](/articles/effective-ai-context-window-management/) fort.** Du hältst einen hilfreichen Datensatz für eine neue Sitzung fest.

**Kursnavigation:** [Vorherige Lektion: Aufgabenpakete](/articles/effective-ai-task-packets/), [Kursübersicht](/effective-ai-course-start/).
