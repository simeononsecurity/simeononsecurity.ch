---
title: "KI-Ausgaben, Quellen, Tests und Kosten überprüfen"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Erstelle einen Abnahmenachweis für ein KI-Ergebnis mit Quellenprüfung, Dateiumfang, Testbelegen, Datenschutzprüfung und Nutzungsdaten."
genre: ["Künstliche Intelligenz", "Softwareentwicklung"]
tags: ["KI-Ausgaben überprüfen", "KI-Fakten prüfen", "Prüfung von Programmieragenten", "KI-Testnachweis", "KI-Kosten erfassen", "menschliche Prüfung"]
cover: "/img/cover/effective-ai-output-verification.webp"
coverAlt: "Ein Prüfblatt vergleicht eine KI-Aussage mit einer Quelldatei, einem Code-Diff, einer Testausgabe und der Nutzungsübersicht"
coverCaption: ""
---

[Zurück zum Kurs Praktischer KI-Workflow](/effective-ai-course-start/)

**Akzeptiere ein KI-Ergebnis erst, nachdem du die für die Aufgabe passenden Belege geprüft hast.** Eine ausgefeilte Erklärung, ein konfiguriertes Werkzeug und ein grünes Testbanner beantworten unterschiedliche Fragen. Diese Lektion erstellt einen gemeinsamen Prüfdatensatz für das Workshop-Labor.

**Lernziel:** Du erstellst einen Abnahmenachweis für Quellen, Dateiumfang, Tests, Datenschutz und Nutzung.

## Wichtigste Punkte

- **Quellenprüfung:** Vergleiche eine Tatsachenbehauptung mit einer aktuellen, maßgeblichen Quelle.
- **Umfangsprüfung:** Prüfe, welche Dateien oder Systeme geändert wurden.
- **Verhaltensprüfung:** Führe Tests und passende manuelle Prüffälle aus.
- **Datenschutzprüfung:** Prüfe, welche Inhalte das Werkzeug oder der Anbieter erhalten hat.
- **Nutzungsprüfung:** Erfasse Tokens, Werkzeugaufrufe und den für die Kostenberechnung verwendeten Tarif.

## Vor dem Start

**Voraussetzungen:** das Kurslabor, `docs/requirements.md`, ein lokaler Git-Snapshot und die [MCP-Lektion](/articles/effective-ai-mcp-server-setup/) oder deren Browser-Alternative. Plane 40 Minuten ein. Der Schwierigkeitsgrad ist mittel. Verwende dein bearbeitetes Labor aus der ersten Coding-Agent-Aufgabe. Wenn du die Bearbeitung übersprungen hast, verwende eine frische Extraktion und markiere Funktionsprüfungen als nicht implementiert. Die unveränderte Ausgangsversion besteht weiterhin ihre zwei ursprünglichen Tests.

## Eine Tatsachenbehauptung prüfen

**Behauptung:** „Die zugelassenen Statuswerte sind `open` und `pending`.“ Öffne `docs/requirements.md`, Revision 1. Dort stehen `open` und `done`. Die Behauptung ist falsch. Ein selbstsicherer Ton ändert die Anforderung nicht.

**Bei Produktbehauptungen** verwendest du aktuelle offizielle Dokumentation und hältst Seitentitel und Prüfdatum fest. Eine Aussage über ein Menü, einen Tarif, einen Befehl oder ein Kontextlimit veraltet schneller als ein allgemeines Workflow-Prinzip. Die [Codex-Dokumentation](https://learn.chatgpt.com/docs/codex/cli), die [Claude-Code-Dokumentation](https://code.claude.com/docs/en/overview) und die [OpenCode-Dokumentation](https://opencode.ai/docs/) beschreiben ihre aktuellen Oberflächen.

| Behauptung | Quelle | Entscheidung |
|---|---|---|
| **`open` und `pending`** | Laboranforderung, Revision 1 | Ablehnen, `pending` durch `done` ersetzen |
| **Anzahl ohne Filter ist 4** | Ausgangsprogramm und vier JSON-Einträge | Durch Ausführen des Programms prüfen |
| **Ein MCP-Lesezugriff fand statt** | Werkzeugprotokoll der Sitzung | Nur akzeptieren, wenn ein Werkzeugaufruf sichtbar ist |

## Änderung prüfen

**Bei einer Programmieraufgabe** listest du mit Git die geänderten Dateien auf und liest den tatsächlichen Diff. Eine neue, noch nicht verfolgte Datei erscheint im Status, auch wenn sie in einem normalen Diff nicht auftaucht. Prüfe daher beides.

```bash
git status --short
git diff -- task_report.py tests
```

**Erwarteter Umfang:** Nach der Filteraufgabe ändern sich nur `task_report.py` und gezielte Tests. Eine Änderung an `tasks.json`, `docs/requirements.md` oder einer versteckten Konfigurationsdatei braucht eine Erklärung und eine separate Prüfung. Wenn du keine Änderung vorgenommen hast, sind keine Änderungen zu erwarten.

## Verhalten testen

**Führe dieselben Basis- und Funktionsprüfungen** im extrahierten Laborordner aus. Der Abschlussbericht des Agenten soll die dabei beobachteten Ergebnisse nennen.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**In der bearbeiteten Kopie** decken die Tests die neuen Fälle ab, die Zählungen lauten 4, 2 und 2, und der ungültige Wert führt mit einer klaren Fehlermeldung zu einem Fehlerstatus. In einer frischen Starter-Kopie bestehen nur die zwei Basistests und die Gesamtzahl ist 4. Halte diesen Ausgangszustand separat fest.

**Ein fehlgeschlagener Funktionstest muss untersucht werden.** Wenn `open` den Wert 4 ausgibt, prüfe, ob das Filterargument die Zählfunktion erreicht und ob das Programm das Feld `status` der Aufgabe vergleicht. Bezeichne einen fehlgeschlagenen Test nicht als bestanden, nur weil der Agent sagt, die Implementierung sei fertig.

## Datenschutz und Zugriff prüfen

**Erfasse, welche Dateien der Agent erhalten hat.** Das Labor enthält synthetische Daten und keine Geheimnisse. Ein reales Projekt kann Zugangsdaten, Kundendaten oder private Dokumente enthalten. Prüfe Prompts, Protokolle, Screenshots und Diffs auf solche Werte, bevor du eine Ausgabe teilst.

**Ein lokaler Test belegt nur lokales Verhalten.** Er beweist weder die Berechtigungen eines Cloud-Kontos noch den Umfang eines MCP-Servers oder das Verhalten eines bereitgestellten Dienstes. Prüfe jede Grenze in der Umgebung, in der sie relevant ist.

## Nutzung und Kosten erfassen

**Tokens messen die Ein- und Ausgabemenge des Modells.** Produkt-Dashboards unterscheiden sich, verwende daher die Nutzungswerte deines Anbieters. Erfasse Werkzeugaufrufe und Gebühren für Bilder oder gehostete Umgebungen bei Bedarf separat. Prüfe aktuelle Tarife, bevor du eine echte Rechnung berechnest.

**Öffne die Nutzungsansicht des Kontos, das die Aufgabe ausgeführt hat.** Erfasse angezeigte Ein- und Ausgabetokens, Modell, Abrechnungszeitraum und eine etwaige Kategorie für zwischengespeicherte Eingaben. Bei ChatGPT- oder Claude-Abos ist ein Nutzungslimit oder Kontingent nicht mit einer API-Aufgabegebühr gleichzusetzen. Bei einem API- oder Anbieter-basierten OpenCode-Lauf prüfst du Nutzung oder Abrechnung dieses Anbieters und den aktuellen Tarif. Zeigt das Produkt keine Tokens pro Aufgabe, schreibe „nicht verfügbar“ und leite keine Kosten aus der Chatlänge ab.

**Beispielrechnung, keine Anbieterpreise:** 30.000 Eingabetokens zu 1 $ pro Million kosten 0,03 $. 5.000 Ausgabetokens zu 5 $ pro Million kosten 0,025 $. Die kombinierten Modellkosten dieses Beispiels betragen 0,055 $, vor Werkzeug- oder Hostinggebühren.

```text
Eingabekosten = Eingabetokens / 1.000.000 × Eingabetarif
Ausgabekosten = Ausgabetokens / 1.000.000 × Ausgabetarif
Gesamt = Eingabekosten + Ausgabekosten + separate Werkzeuggebühren
```

**Auch ein delegierter Auftrag verbraucht Tokens.** Delegation verlagert ausführliche Ergebnisse aus dem Hauptgespräch, macht die Arbeit aber nicht kostenlos. Vergleiche die Kosten mit dem Nutzen der unabhängigen Prüfung.

**Halte Gebührenkategorien getrennt.** Zwischengespeicherte Eingaben, neue Eingaben, Ausgaben, Werkzeugaufrufe und gehostete Ausführung können unterschiedliche Tarife haben. Dieses Beispiel verwendet nur Tarife für neue Eingaben und Ausgaben. Es sagt nichts über ein Abo oder Werkzeuggebühren aus.

## Einen Abnahmenachweis führen

| Feld | Ausgefülltes Beispiel nach der Bearbeitung |
|---|---|
| **Quelle** | `docs/requirements.md`, Revision 1, gelesen |
| **Geänderte Dateien** | `task_report.py` und `tests/test_task_report.py` in `git status --short` |
| **Tests** | Basis- und neue Filtertests bestanden, beobachtete Anzahl eintragen |
| **Manuelle Ausgabe** | `Total tasks: 4`, `2` und `2` beobachtet, ungültiger Wert abgelehnt |
| **Funktionsstatus** | `--status open` und `--status done` implementiert |
| **Datenschutz** | Nur synthetische Dateien |
| **Nutzung** | Werte deines Anbieters eintragen, falls verfügbar |
| **Entscheidung** | Nur akzeptieren, wenn Quellen-, Diff-, Test- und Datenschutzprüfungen bestehen |

**Dein Ergebnis:** Kopiere diesen Nachweis und fülle ihn nach deinem eigenen Lauf aus. Ersetze „beobachtet“ nur durch eine Ausgabe, die du selbst gesehen hast. Wähle Akzeptieren, wenn alle erforderlichen Prüfungen bestehen, Überarbeiten, wenn die Korrektur klar begrenzt ist, und Stoppen, wenn Quelle, Umfang oder Zugriff unklar sind.

## Verständnis prüfen

1. **Frage:** Belegt eine bestandene Starter-Basis, dass die gewünschte Funktion vorhanden ist? **Antwort:** Nein. Prüfe nach der Bearbeitung das neue Abnahmeverhalten.

2. **Frage:** Was gehört in einen Abnahmenachweis? **Antwort:** Quellenbelege, geänderte Dateien, Verhaltensprüfungen, Zugriffsbereich und beobachtete Nutzung.

## Fehlerbehebung

- **Keine Quelle für eine Behauptung:** Markiere sie als ungeprüft und suche eine maßgebliche Quelle.
- **Tests bestehen, aber die Ausgabe weicht ab:** Ergänze einen manuellen Fall und prüfe die Daten.
- **Nutzungsdaten fehlen:** Notiere „nicht verfügbar“, statt echte Kosten zu schätzen.
- **Der Diff enthält private Daten:** Teile die Ausgabe nicht weiter und entferne die Daten aus dem Übungsnachweis.

## Nächste Schritte

**Weiter geht es mit [Agentendelegation](/articles/effective-ai-agent-delegation/)**. Einzelheiten zu Kosten und Datenschutz findest du unter [Anbieterrouting](/articles/openrouter-provider-routing-quality-cost/) und [Datenschutzgrenze lokaler KI](/articles/local-ai-privacy-boundary/).

**Kursnavigation:** [Zurück: MCP-Einrichtung](/articles/effective-ai-mcp-server-setup/), [Kursübersicht](/effective-ai-course-start/).
