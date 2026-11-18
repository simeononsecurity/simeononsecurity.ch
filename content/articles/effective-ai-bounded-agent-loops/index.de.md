---
title: "Begrenzte KI-Agentenschleifen: Prüfungen, Wiederholungen und Stoppregeln"
date: 2026-10-10
lastmod: 2026-11-14
toc: true
draft: false
description: "Definieren Sie eine KI-Zielschleife mit beobachtbarem Zustand, Prüfungen, Wiederholungsgrenzen, Stoppbedingungen und klarer Übergabe an einen Menschen."
genre: ["Künstliche Intelligenz", "Softwareentwicklung", "Produktivität"]
tags: ["KI-Zielschleifen", "Agenten-Wiederholungsschleife", "Stoppregeln für KI-Automatisierung", "Agentenüberwachung", "KI-Übergabe an Menschen", "begrenzter KI-Arbeitsablauf"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Eine kleine Agentenschleife führt von einer Bearbeitung über einen Test und eine Wiederholungsentscheidung bis zur Übergabe an einen Menschen"
coverCaption: ""
---

[Zurück zum praktischen KI-Workflow-Kurs](/effective-ai-course-start/)

**Eine Zielschleife wiederholt Arbeit, bis ein festgelegtes Ergebnis die Prüfung besteht oder eine Stoppregel greift.** Eine nützliche Schleife liest den aktuellen Zustand, führt eine begrenzte Aktion aus, prüft das Ergebnis und hält fest, was passiert ist. Eine offene Anweisung wie „Versuche es weiter“ hat keine zuverlässige Abschlussregel.

**Lernziel:** Sie führen eine begrenzte Laborschleife mit einer bekannten fehlgeschlagenen Prüfung aus und protokollieren die Stoppentscheidung.

## Wichtigste Erkenntnisse

- **Ziel:** ein Ergebnis, das anhand beobachtbarer Kriterien beschrieben wird.
- **Zustand:** aktuelle Dateien, Ausgaben, Fehler und Quellrevision.
- **Prüfung:** ein Test oder eine Überprüfung, die zum Ziel gehört.
- **Wiederholungsbudget:** die maximale Anzahl von Versuchen bei einem Fehler.
- **Stoppregel:** eine Bedingung, die ein Ende oder eine menschliche Entscheidung verlangt.

## Bevor Sie beginnen

**Voraussetzungen:** das [Aufgabenpaket](/articles/effective-ai-task-packets/), der [Verifizierungsnachweis](/articles/effective-ai-output-verification/) und die [Lektion zur Delegation](/articles/effective-ai-agent-delegation/). Planen Sie 45 Minuten ein. Der Schwierigkeitsgrad ist mittel. Verwenden Sie eine frische Kopie des synthetischen Labs, damit die erste fehlgeschlagene Prüfung im Voraus bekannt ist.

## Den Schleifenvertrag schreiben

**Für die Anfrage zum Statusfilter** legen Sie den Vertrag vor jedem Wiederholungsversuch fest:

```text
Ziel: --status open|done unterstützen, ohne die Standardausgabe zu ändern.
Quelle: docs/requirements.md, Revision 1.
Erlaubte Dateien: task_report.py und gezielte Tests.
Prüfungen: Unit-Tests, Zählwerte 4/2/2, ungültiger Wert liefert einen Exit-Code ungleich null.
Wiederholungsbudget: höchstens zwei Änderungen nach dem ersten Versuch.
Sofort stoppen: Quellkonflikt, unerwartete Dateiänderung, Offenlegung eines Geheimnisses,
oder ein nicht zu dieser Anfrage gehörender Fehler im Ausgangstest.
Übergabe: endgültigen Diff, Befehle, Ausgaben, Versuche und ungelöstes Problem melden.
```

**Das Budget ist eine Aufgabenregel**, keine Produkteinstellung. Zwei Wiederholungen reichen aus, um eine kleine Laboraufgabe zu untersuchen, ohne wiederholte Fehler zu verbergen. Eine Produktionsaufgabe braucht eine eigene Risiko- und Prüfentscheidung.

## Eine Statustabelle verwenden

| Schritt | Zu erfassender Zustand | Entscheidung |
|---|---|---|
| **Lesen** | Quellrevision und Ausgangsergebnis | Stoppen, wenn der Ausgangszustand abweicht |
| **Handeln** | Geänderte Dateien und ausgeführte Aktion | Änderungen außerhalb des Umfangs ablehnen |
| **Prüfen** | Genau angegebener Test und manuelle Ausgabe | Annehmen oder Ursache untersuchen |
| **Wiederholen** | Fehlerursache und neue Hypothese | Nur innerhalb des Budgets fortfahren |
| **Übergeben** | Endzustand und nächste zuständige Person | Nach Erfolg oder Blockierung stoppen |

**Protokollieren Sie alle Versuche, nicht nur die letzte Meldung.** Ein Test, der nach drei nicht dokumentierten Änderungen besteht, liefert keinen brauchbaren Bericht darüber, was sich geändert hat. Führen Sie ein kurzes Protokoll mit Fehler, überarbeiteter Hypothese und neuen Belegen.

## Einen Fehler durchgehen

**Beispiel für den ersten Versuch:** Der Agent ergänzt Filterung und Tests. `open` gibt 2 aus, aber `--status invalid` gibt 0 aus und endet erfolgreich. Die Anforderung verlangt für einen ungültigen Wert einen Rückgabecode ungleich null. Markieren Sie die Prüfung als fehlgeschlagen.

**Diagnose:** Untersuchen Sie die Argumentvalidierung. Der Agent hat einen unbekannten Wert als leere Trefferliste statt als Fehler behandelt. Fordern Sie eine begrenzte Korrektur an, die zulässige Werte vor dem Zählen prüft. Führen Sie den ungültigen Fall und alle vorherigen Prüfungen erneut aus.

```text
Versuch 1: Der ungültige Status lieferte Erfolg, daher schlug die Abnahme fehl.
Gefundene Ursache: keine Prüfung zulässiger Werte.
Anfrage für Versuch 2: Nicht unterstützte Werte ablehnen und die Zählwerte 4/2/2 beibehalten.
Erforderliche Nachweise: vollständiger Testlauf und Exit-Status des ungültigen Befehls.
```

**Erwartetes Ergebnis des zweiten Versuchs:** eine klare Fehlermeldung und ein Rückgabecode ungleich null für `invalid`, während die gültigen Zählwerte unverändert bleiben. Wenn der zweite Versuch weiterhin fehlschlägt, nutzen Sie den letzten Wiederholungsversuch erst, nachdem Sie eine neue Ursache benannt haben. Dieselbe Anfrage zu wiederholen ist keine Diagnose.

## Mehrdeutige Ergebnisse behandeln

**Ein Prozess, der ohne Ergebnis endet, war nicht erfolgreich.** Läuft ein Werkzeug nach einem möglichen Schreibvorgang in ein Zeitlimit, prüfen Sie Dateien und Git-Status, bevor Sie es erneut ausführen. Meldet ein verbundener Dienst einen unbekannten Ausgang, lesen Sie den aktuellen Zustand aus, bevor Sie eine externe Aktion wiederholen. Doppelte Sendungen, Beiträge oder Schreibvorgänge sind außerhalb des Labs ein reales Risiko.

**Stoppen Sie für eine menschliche Prüfung**, wenn die Anforderung einer anderen freigegebenen Quelle widerspricht, eine Berechtigung die Aktion verhindert, das Wiederholungsbudget aufgebraucht ist oder die angeforderte Aktion eine Veröffentlichungsgrenze überschreitet. Die Übergabe nennt den genauen Zustand und die ausstehende Entscheidung.

## Schleifen und Monitore trennen

**Eine Bearbeitungsschleife** läuft innerhalb einer begrenzten Aufgabe und prüft nach jeder Aktion das Ergebnis. **Ein geplanter Monitor** wird später aktiv, um eine Bedingung zu prüfen. Ein Monitor braucht einen eigenen Takt, eine Änderungsschwelle, eine Benachrichtigungsregel und eine Stoppbedingung. Machen Sie aus der Bearbeitungsschleife des Labs keinen wiederkehrenden Auftrag. Die nächste Lektion bewertet dauerhafte Systeme, bevor sie aktiviert werden.

## Eine kontrollierte Schleife ausführen

**Beginnen Sie mit dem unveränderten Lab.** Die beiden Ausgangstests bestehen. Erstellen Sie in der frischen Extraktion `tests/test_loop_contract.py` mit der folgenden Prüfung. Diese Datei beschreibt eine gewünschte Funktion, die im Starter fehlt. Sie gehört nicht in das gepflegte Starter-ZIP.

```python
"""Eine kontrolliert fehlschlagende Prüfung für die Übung zum Statusfilter."""

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

**Führen Sie `python3 -m unittest discover -s tests -v` aus.** Die zwei ursprünglichen Tests sollten bestehen und der neue Vertragstest sollte fehlschlagen, weil der Starter `--status` nicht unterstützt. Protokollieren Sie den tatsächlichen Fehler. Wenn Sie Git wie in Lektion 0 initialisiert haben, erfassen Sie auch `git status --short`. Vergleichen Sie andernfalls die geänderten Dateien mit einer unveränderten Extraktion. Unter Windows verwenden Sie `py -3`, wenn Ihre Einrichtung den Launcher nutzt.

**Legen Sie ein Budget von drei Versuchen fest:** die erste Bearbeitung und höchstens zwei Korrekturen. Geben Sie Ihrem Agenten den Schleifenvertrag oben und bitten Sie um eine begrenzte Änderung. Prüfen Sie nach jedem Versuch die geänderten Dateien, führen Sie alle Tests erneut aus und probieren Sie die Standardausgabe, `open`, `done` und einen ungültigen Wert. Notieren Sie vor dem nächsten Versuch die Fehlerursache. Stoppen Sie nach Erfolg, bei einem unabhängigen Fehler der Ausgangsbasis, einer Änderung außerhalb des Umfangs oder nach dem dritten fehlgeschlagenen Versuch.

**Lernpfad:** Wenden Sie nach der Aufzeichnung des roten Tests die vollständige [Lösung zu Lektion 5](/articles/effective-ai-coding-agent-first-task/) in dieser frischen Kopie an. Führen Sie dieselben Prüfungen erneut aus und halten Sie fest, dass die Agentenbearbeitung nicht ausgeführt wurde. Behalten Sie den kontrollierten Vertragstest bei. Schwächen oder löschen Sie ihn nicht, um ihn zum Bestehen zu bringen.

| Versuch | Zustand und Beobachtung | Entscheidung |
|---|---|---|
| **Vor der Bearbeitung** | Zwei Ausgangstests bestehen, die neue `open`-Prüfung schlägt fehl | Mit einer begrenzten Änderung fortfahren |
| **Nach jeder Bearbeitung** | Genaue Tests, Zählwerte, Rückgabecode bei ungültigem Wert und geänderte Dateien erfassen | Annehmen, untersuchen oder stoppen |
| **Am Budgetende** | Verbleibenden Fehler und aktuellen Diff erfassen | Ohne weiteren Versuch übergeben |

## Üben und prüfen

**Ihr Artefakt:** der kontrollierte fehlgeschlagene Test, die beobachteten Ausgaben vor und nach der Änderung, ein Versuchsprotokoll und eine abschließende Annahme- oder Stoppentscheidung. Besteht die erste Bearbeitung, protokollieren Sie einen Versuch. Erfinden Sie keinen zweiten Fehler, nur um das Protokoll zu füllen.

**Abschlussprüfung:** Der Vertrag nennt eine Quelle, den Datei-Umfang, beobachtbare Prüfungen, eine Wiederholungsgrenze, mindestens eine sofortige Stoppbedingung und eine Übergabe. Ihr Protokoll enthält den tatsächlichen roten Test, spätere Prüfergebnisse und entweder einen Erfolg oder einen Stopp wegen aufgebrauchten Budgets. Ein zweiter Versuch nennt eine neue Ursache und unterscheidet sich vom ersten.

## Verständnis prüfen

1. **Frage:** Was weist der erste rote Vertragstest nach? **Antwort:** Dem Starter fehlt der angeforderte Statusfilter, wie ein vor der Bearbeitung geschriebener Test zeigt.
2. **Frage:** Wann muss die Schleife trotz verbleibender Wiederholungen stoppen? **Antwort:** Bei einer Änderung außerhalb des Umfangs, einer unklaren Berechtigung oder einer widersprüchlichen Anforderung.

## Fehlerbehebung

- **Die Schleife wiederholt denselben Fehler:** Stoppen Sie und formulieren Sie eine neue Ursachenhypothese.
- **Prüfungen werden schwächer:** Stellen Sie die ursprünglichen Akzeptanzkriterien wieder her.
- **Unsicheres externes Ergebnis:** Prüfen Sie den aktuellen Zustand vor einem weiteren Versuch.
- **Budget aufgebraucht:** Übergeben Sie das Fehlerprotokoll, statt den Fehler zu verbergen.

## Nächste Schritte

Arbeiten Sie mit der optionalen [Bewertung spezialisierter Agenten](/articles/effective-ai-specialized-agent-evaluation/) weiter oder gehen Sie direkt zum [Abschlussprojekt des KI-Workflow-Kurses](/articles/effective-ai-capstone/). Weitere Optionen für Laufzeitumgebungen finden Sie im [Leitfaden zu Agenten-Frameworks](/articles/best-ai-agent-harnesses/).

**Kursnavigation:** [Zurück: Agentendelegation](/articles/effective-ai-agent-delegation/), [Kursübersicht](/effective-ai-course-start/).
