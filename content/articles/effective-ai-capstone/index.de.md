---
title: "KI-Workflow-Capstone: Einen JSON-Bericht erstellen und prüfen"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Erstelle einen neuen JSON-Aufgabenbericht mit Projektkontext, klar begrenztem Agentenauftrag, unabhängigen Tests, Quellenprüfung und Übergabe an eine neue Sitzung."
genre: ["Künstliche Intelligenz", "Softwareentwicklung", "Bildung"]
tags: ["KI-Workflow-Capstone", "Coding-Agent-Projekt", "KI-Aufgabenprüfung", "AGENTS.md", "MCP-Übung", "Agentenübergabe"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Eine abgeschlossene Softwareaufgabe mit Quelldateien, Testergebnissen, Agentenprüfung und Übergabeprotokoll"
coverCaption: ""
---

[Zurück zum Kurs „Praktischer KI-Workflow“](/effective-ai-course-start/)

**Erstelle ein neues Ausgabeformat und belege sein Verhalten.** Zuvor hast du einen Statusfilter ergänzt. Dieses Capstone beginnt mit einem neuen Lab und ergänzt einen JSON-Bericht, den ein anderes Programm einlesen soll. Die neue Anforderung prüft, ob du deinen Workflow auf ein anderes Feature übertragen kannst.

**Lernziel:** Du lieferst einen geprüften JSON-Bericht, einen Beleg für Quellen und Werkzeuge sowie eine Übergabe, mit der eine neue Sitzung das Ergebnis versteht.

## Wichtigste Erkenntnisse

- **Eine separate Anforderung** legt das Capstone-Feature fest.
- **Die Änderung eines Coding-Agenten** bleibt auf benannte Dateien beschränkt.
- **Unabhängige Prüfungen** entscheiden über die Abnahme.
- **Eine Übergabe an eine neue Sitzung** ermöglicht die Rekonstruktion des Ergebnisses.

## Vor dem Start

**Voraussetzungen:** Schließe Lektionen 0 bis 10 ab, einschließlich Arbeitsbereich-Hintergrund, erster Coding-Aufgabe, MCP oder Browser-Alternative, Delegation und begrenzten Schleifen. Lektion 11 ist optional. Plane 90 bis 120 Minuten ein. Der Schwierigkeitsgrad ist mittel.

**Verwende eine frische Entpackung** des [Starter-Labs](/downloads/effective-ai-course-lab.zip). Führe `python3 task_report.py tasks.json` und die beiden Basistests vor jeder Änderung aus. Unter Windows verwende `py -3`, wenn deine Einrichtung den Python-Launcher nutzt. Erstelle wie bei der Kurseinrichtung einen lokalen Git-Baseline-Commit. Der Statusfilter aus Lektion 5 fehlt absichtlich.

**Lies `docs/capstone-requirements.md`, Revision 1.** Gefordert ist `--format text|json`. Die Standardausgabe bleibt `Total tasks: 4`. Die JSON-Ausgabe enthält eine numerische Gesamtzahl und Zählwerte für jeden Status in den Daten. Prüfe eine leere Liste, einen fehlenden Status und ein nicht unterstütztes Format. Verwende `docs/requirements.md` nicht als maßgebliche Quelle für dieses neue Feature.

**Wähle deinen Track.** Der verbundene Track verwendet eine beobachtete Änderung durch einen Coding-Agenten, einen echten schreibgeschützten MCP-Aufruf und einen nativen Worker oder eine separate Worker-Sitzung. Der Lern-Track verwendet einen Chat-Assistenten für einen Codevorschlag, eine Browserquelle statt MCP und separate Chats als simulierte Worker. Kennzeichne nicht verfügbare Werkzeugschritte mit „nicht ausgeführt“. Beide Tracks erfordern lokale Tests und eine Datei-Prüfung. Der Lösungsschlüssel unten enthält vollständige Dateien als Wiederherstellungspfad. Sichere deinen ersten Versuch in Notizen, bevor du den Lösungsschlüssel in eine frische Entpackung kopierst.

## Prüfschritt 1: Projektbrief

**Öffne das synthetische ChatGPT- oder Claude-Workshop-Projekt.** Bitte um einen Erinnerungsentwurf mit zwei Sätzen. Prüfe die Uhrzeit 19 Uhr anhand von `approved-schedule.md`. Der Zeitplan bestimmt die Erinnerung. Die Capstone-Anforderung bestimmt das Programm.

**Beleg:** Halte Projektnamen, Quellrevision, beobachtete Entwurfszeit und jede Korrektur fest. Sende die Nachricht nicht.

## Prüfschritt 2: Arbeitsbereich-Hintergrund

**Öffne das frische Lab.** Erstelle eine kurze `AGENTS.md`, die auf `docs/capstone-requirements.md`, `task_report.py`, die Tests und den beim Setup bestätigten Testbefehl verweist. Wenn du Claude Code nutzt, binde die gemeinsame Datei über `CLAUDE.md` ein. Erstelle einen menschlichen Setup-Commit für diese Leitdateien und bestätige dann, dass `git status --short` keine Ausgabe liefert. Der Coding-Agent darf die Feature-Änderung nicht committen.

**Beleg:** Sichere die Übersicht und den sauberen Stand der Leitdateien. Nenne die JSON-Schlüssel und das Verhalten bei ungültigen Eingaben aus Revision 1. Wenn ein früherer Chat den Statusfilter beschreibt, behandle ihn als Hintergrund zu einer anderen Aufgabe.

## Prüfschritt 3: Externe Quelle

**Verbundener Track:** Verwende den schreibgeschützten [MCP-Server für OpenAI-Dokumentation](https://learn.chatgpt.com/learn/docs-mcp) über einen unterstützten Client. Bitte ein MCP-Tool um die aktuellen `AGENTS.md`-Hinweise. Halte Toolnamen, Quell-URL und einen relevanten Punkt für dein Lab fest. Entferne die Übungsverbindung anschließend.

**Lern-Track:** Öffne die [offizielle Dokumentation zu `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md) in einem Browser. Halte Titel, URL und einen relevanten Punkt fest. Kennzeichne MCP-Ermittlung und -Ausführung als „nicht ausgeführt“.

**Beleg:** Ein konfigurierter Servereintrag beweist keine Ausführung. Der verbundene Track benötigt einen sichtbaren Tool-Aufruf und zurückgegebene Quellinhalte.

## Prüfschritt 4: Eine Prüfung delegieren

**Bitte einen schreibgeschützten Worker**, `docs/capstone-requirements.md`, `task_report.py` und die Basistests zu prüfen. Verlange einen Bericht mit höchstens fünf Zeilen, der fehlende Prüfungen und Dateipfade nennt. Nutze im Lern-Track einen separaten Chat und kennzeichne ihn als simulierten Worker.

**Erwarteter Befund:** Die Starter-Tests prüfen die Gesamtzahl und einen JSON-Wert, der keine Liste ist. Sie prüfen nicht die JSON-Ausgabe, eine leere Liste, einen fehlenden Status oder ein ungültiges Format. Öffne die Testdatei selbst und prüfe den Bericht. Eine kurze unabhängige Prüfung ist hier nützlich, weil sich die Abnahmekriterien von Lektion 5 unterscheiden.

**Beleg:** Sichere den kurzen Bericht und deine einzeilige Integrationsentscheidung. Bewahre das Worker-Transkript außerhalb des Hauptaufgabenprotokolls auf.

## Prüfschritt 5: Änderung anfordern

**Gib einem Coding-Agenten** das folgende Paket. Im Lern-Track schlägt ein Chat-Assistent einen Patch vor, den du anschließend manuell im Lab anwendest.

```text
Ziel: --format text|json nach dem JSON-Pfad ergänzen.
Quelle: docs/capstone-requirements.md, Revision 1.
Erlaubte Änderungen: task_report.py und tests/test_task_report.py.
Beibehalten: Standardausgabe Total tasks: 4 und tasks.json unverändert.
JSON: ein Objekt mit total und by_status-Zählwerten, keine zusätzliche stdout-Ausgabe.
Erforderliche Prüfungen: Standard und explizites Textformat, JSON 4/2/2, leere Liste,
fehlender Status, ungültiges Format und Basistests.
Anhalten bei: Quellenkonflikt, unabhängigem Basistestfehler oder Änderung außerhalb des Umfangs.
Bericht: geänderte Dateien, Befehle, beobachtete Ausgaben, ungelöstes Problem.
Kein Commit, Push, keine Veröffentlichung und keine Nachricht.
```

**Prüfe den Plan** vor der Änderung. Die Schemawahl zählt: `total` ist eine Zahl, nicht die Zeichenfolge `"4"`. `by_status` enthält jeden Status aus der Eingabe, damit der Bericht auch einen späteren Statuswert erfasst. Beschränke die Änderung auf das entpackte Lab.

## Prüfschritt 6: Testen und prüfen

**Führe diese Prüfungen selbst aus.** Unter Windows ersetze `python3` durch `py -3`. Die genaue Schlüsselreihenfolge und Leerzeichen der JSON-Ausgabe sind unerheblich. Parse die Ausgabe als JSON und vergleiche typisierte Werte.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Erwartetes Verhalten:** Die Tests bestehen. Beide Textbefehle geben `Total tasks: 4` aus. Der JSON-Befehl gibt ein einzelnes Objekt mit `total` 4, `by_status.open` 2 und `by_status.done` 2 zurück. Das ungültige Format liefert einen Fehlercode ungleich null. Die Tests decken auch leere Eingaben und eine Aufgabe ohne String-`status` ab. Lies die beobachtete Fehlerausgabe und den Rückgabecode für diese Fälle.

| Kontrollpunkt | Erfolgsbeleg | Wiederherstellung bei Fehler |
|---|---|---|
| **Projektbrief** | Erinnerung nennt 19 Uhr | Zeitplanquelle neu laden |
| **Arbeitsbereich-Übersicht** | Capstone-Anforderung und Testpfade genannt | Leitdateien korrigieren |
| **Externe Quelle** | MCP-Quelle gelesen oder Browser-Alternative gekennzeichnet | Verbindung oder Quell-URL prüfen |
| **Worker-Prüfung** | Fehlende Tests in der Datei bestätigt | Worker-Bericht korrigieren |
| **Dateiumfang** | Nur Programm und Tests | Jede unerwünschte Änderung prüfen |
| **Verhalten** | Text, JSON, leere Eingabe und Fehler geprüft | Eine Ursache diagnostizieren, dann erneut versuchen |
| **Übergabe** | Neue Sitzung rekonstruiert den Stand | Fehlende Quelle oder Ergebnis ergänzen |

**Nutze eine frische Entpackung als sicheren Reset.** Sichere deine Notizen außerhalb des Labs, verwerfe nur die entbehrliche entpackte Kopie und entpacke das ursprüngliche ZIP erneut. Verwende keinen umfassenden Git-Reset in einem Repository mit Arbeit, die du behalten musst.

## Prüfschritt 7: Übergabe an eine neue Sitzung

**Schreibe eine Übergabe mit weniger als 180 Wörtern** außerhalb des Lab-Ordners. Nenne Revision der Capstone-Anforderung, geänderte Dateien, genauen Testbefehl und Ergebnis, Text- und JSON-Ausgaben, Prüfungen ungültiger Eingaben, Nutzungsprotokoll und offene Aktion. Öffne eine neue Sitzung und bitte sie, die JSON-Schlüssel und den Status des Features zu nennen.

**Erwartete Antwort:** Die neue Sitzung nennt `total` und `by_status`, verweist auf Revision 1, meldet nur beobachtete Prüfungen und kennzeichnet jede fehlende Prüfung.

## Lösungsschlüssel und Bewertungsraster

**Eine gültige Implementierung** steht unten. Speichere den ersten Block als `task_report.py` und den zweiten als `tests/test_task_report.py` in einer frischen Lab-Entpackung. Lasse `tasks.json` und beide Anforderungsdateien unverändert. Führe die Prüfungen aus Kontrollpunkt 6 aus. Vergleiche andere Lösungen mit der Anforderung und dem beobachteten Verhalten.

`task_report.py`:

```python
"""Gibt eine Textanzahl oder eine JSON-Zusammenfassung der Workshop-Aufgaben aus."""

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
    parser = argparse.ArgumentParser(description="Workshop-Aufgabenbericht")
    parser.add_argument("path", type=Path, help="Pfad zur JSON-Aufgabenliste")
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
"""Prüfungen für Text- und JSON-Berichte der Workshop-Aufgaben."""

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

**Reset after using the solution key:** sichere deine Notizen außerhalb des Labs, verwirf diese entpackte Kopie und entpacke das ursprüngliche Starter-Lab erneut. Die neue Kopie enthält die beiden Basistests und keine Feature-Implementierung.

**Vergib einen Punkt pro Kontrollpunkt** in der Tabelle oben. Sieben Punkte schließen den verbundenen Track ab, wenn die externe Quelle einen echten MCP-Aufruf und der Worker eine echte Sitzung dokumentieren. Sieben Punkte schließen den Lern-Track ab, wenn die Quelle eine geprüfte Browserseite enthält und Werkzeugschritte ausdrücklich als nicht ausgeführt gekennzeichnet sind. Fehlende Verhaltens-, Quellen- oder Dateiumfangsprüfung blockiert den Abschluss beider Tracks.

## Verständnis prüfen

1. **Welche Anforderung legt dieses Feature fest?** `docs/capstone-requirements.md`, Revision 1. Die frühere Anforderung zum Statusfilter gehört zu Lektion 5.
2. **Was belegt den JSON-Vertrag?** Parse die Befehlsausgabe, vergleiche Zahlenwerte und jeden Statuszähler und prüfe leere und ungültige Eingaben. Eine ausgefeilte Agentenzusammenfassung reicht nicht.

## Fehlerbehebung

- **Die Basistests schlagen vor der Änderung fehl:** Setze das Lab aus dem ZIP zurück und wiederhole das Setup.
- **Der Agent ändert eine andere Datei:** Prüfe den Diff und stelle nur die unerwünschte Lab-Änderung wieder her.
- **Die MCP-Verbindung schlägt fehl:** Verwende die Browserquelle und kennzeichne den Kontrollpunkt als Lern-Track.
- **Der Worker wiederholt einen falschen Wert:** Lies die Capstone-Anforderung erneut und korrigiere den Bericht.
- **Das Wiederholungsbudget ist ausgeschöpft:** Sichere das Fehlerprotokoll und bitte einen menschlichen Prüfer um den nächsten Schritt.

## Nächste Schritte

**Sichere dein fertiges Belegprotokoll.** Für fortgeschrittene Teamveröffentlichung und systemübergreifende Autorität fahre mit dem [Kurs zur Umsetzung von KI-Kollaboration](/ai-collaboration-course-start/) fort.

**Kursnavigation:** [Vorherige Pflichtlektion: Begrenzte Schleifen](/articles/effective-ai-bounded-agent-loops/), [Optional: Spezialisierte Agenten](/articles/effective-ai-specialized-agent-evaluation/), [Kursübersicht](/effective-ai-course-start/).
