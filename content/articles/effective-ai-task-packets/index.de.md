---
title: "KI-Aufgabenpakete: bessere Prompts und Abnahmekriterien"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Formuliere vage KI-Aufträge als Aufgabenpakete mit festgelegtem Ergebnis, Quelle, Dateiumfang, Prüfungen und Abbruchbedingung."
genre: ["Künstliche Intelligenz", "Produktivität", "Softwareentwicklung"]
tags: ["KI-Promptschreiben", "Aufgabenpaket", "Programmieragent-Prompt", "Abnahmekriterien", "KI-Arbeitsablauf", "Anweisungen für KI-Agenten"]
cover: "/img/cover/effective-ai-task-packets.webp"
coverAlt: "Ein vager Auftrag, der in ein kurzes Aufgabenpaket mit Quelle, Umfang, Prüfung und Abbruchbedingung umformuliert wurde"
coverCaption: ""
---

[Zurück zum praktischen KI-Workflow-Kurs](/effective-ai-course-start/)

**Ein guter Prompt beschreibt die Arbeit und wie du sie bewertest.** Mehr Wörter gleichen einen fehlenden Umfang nicht aus. In dieser Lektion wird ein vager Auftrag für das Kurslabor in ein Aufgabenpaket umgewandelt.

**Lernziel:** Du schreibst ein klar begrenztes Aufgabenpaket mit Quelle, Dateiumfang, Prüfungen und Abbruchbedingung.

## Wichtigste Erkenntnisse

- **Ergebnis** benennt das gewünschte Artefakt oder Verhalten.
- **Umfang** benennt erlaubte Dateien und ausgeschlossene Aktionen.
- **Quelle** nennt die genehmigte Anforderung.
- **Abnahmekriterien** machen den Erfolg beobachtbar.
- **Abbruchbedingungen** verhindern Vermutungen und nicht genehmigte Folgearbeiten.

## Vor dem Start

**Voraussetzungen:** das entpackte Labor, seine Datei `docs/requirements.md` und die [Lektion zum Repository-Kontext](/articles/effective-ai-agents-md-context/). Plane 30 Minuten ein. Der Schwierigkeitsgrad ist Anfänger. Diese Übung endet mit einem schriftlichen Paket. Du musst noch keinen Code bearbeiten.

## Zwei Aufträge vergleichen

**Vager Auftrag:** „Verbessere das Aufgaben-Skript.“ Ein Agent könnte die Ausgabe umschreiben, Abhängigkeiten hinzufügen, Beispieldaten bearbeiten oder Tests auslassen. Der Auftrag legt keine dieser Entscheidungen fest.

**Begrenzter Auftrag:** „Füge `task_report.py` anhand von Revision 1 der `docs/requirements.md` einen optionalen Statusfilter hinzu. Behalte die Standardausgabe bei. Ergänze Tests. Ändere keine Beispieldaten. Stoppe vor dem Commit.“ Der Agent entscheidet weiterhin über Implementierungsdetails. Die Aufgabe definiert, woran der Erfolg erkennbar ist.

| Paketbestandteil | Laborbeispiel | Prüfung |
|---|---|---|
| **Ergebnis** | `--status` zum Bericht hinzufügen | Beide erlaubten Werte funktionieren |
| **Quelle** | `docs/requirements.md`, Revision 1 | Der Code entspricht den genehmigten Werten |
| **Umfang** | Nur Programm und Tests | Das Diff enthält keine weiteren Dateien |
| **Vorgaben** | Standardausgabe und Beispieldaten beibehalten | Die Basisausgabe bleibt `Total tasks: 4` |
| **Nachweis** | Testbefehl und manuelle Aufrufe | Ausgaben entsprechen den erwarteten Anzahlen |
| **Stopp** | Weder Commit noch Push | Git-Verlauf und Remote bleiben unverändert |

## Eine wiederverwendbare Vorlage nutzen

**Kopiere diese Vorlage** für eine kleine Programmier- oder Rechercheaufgabe. Entferne irrelevante Felder, statt sie mit vagen Angaben auszufüllen.

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

**Für das Labor** sieht das ausgefüllte Paket so aus:

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

**Unter Windows** verwende in Paketbefehlen `py -3`, wenn deine Umgebung den Python-Launcher nutzt.

**Das Paket schreibt nicht jede Codezeile vor.** Der Agent darf eine kleine Umsetzung wählen, während das Ergebnis überprüfbar bleibt.

## Beispiele sorgfältig ergänzen

**Ein genaues Beispiel beseitigt Unklarheit.** Die Beispiele `open` und `done` geben die Ausgabe für die bereitgestellte Datei mit vier Aufgaben vor. Sie legen keine allgemeine Regel für jede Datei fest. Bei einer anderen Datei hängen die Anzahlen von deren Datensätzen ab.

**Erwartetes von Beobachtetem trennen.** Vor der Programmausführung ist `Total tasks: 2` das erwartete Ergebnis für jeden Status. Danach ist die Terminalausgabe eine Beobachtung. Weichen die Werte ab, prüfe Daten und Implementierung, bevor du Erfolg meldest.

## Eine Abbruchbedingung festlegen

**Angenommen, die Anforderungsdatei fehlt.** Das Paket nennt sie als genehmigte Quelle. Halte an und frage nach der Anforderung, statt erlaubte Werte aus einem alten Chat oder einem Beispiel-Ticket abzuleiten.

**Angenommen, die Basistests schlagen vor der Bearbeitung fehl.** Halte den Fehler fest und frage, ob zuerst der Ausgangszustand korrigiert werden soll. Ein späterer erfolgreicher Lauf zeigt nicht, ob der Filter oder der Ausgangszustand die Änderung verursacht hat.

**Angenommen, der Agent möchte einen Commit erstellen.** Das Paket schließt Commits aus. Bitte ihn, nach Diff und Tests anzuhalten. Du entscheidest, ob ein späterer Commit in den Projektablauf passt.

## Das Paket prüfen

**Vergib je Antwort einen Punkt:** Ist das Ergebnis konkret? Ist die maßgebliche Quelle genannt? Ist der Dateiumfang klar? Sind mindestens zwei beobachtbare Prüfungen aufgeführt? Gibt es eine Abbruchbedingung? Weniger als fünf Punkte bedeutet, dass du das Paket vor der Delegation überarbeiten solltest.

**Dein Ergebnis:** Speichere dein endgültiges Aufgabenpaket und eine einzeilige Erklärung zu einer Abbruchbedingung. Gib es einem Programmieragenten in der nächsten praktischen Lektion oder beantworte die erwarteten Ergebnisse manuell auf der Lernroute.

## Verständnis prüfen

1. **Frage:** Was macht ein Aufgabenpaket überprüfbar? **Antwort:** Eine Quelle, erlaubte Dateien, beobachtbare Prüfungen und eine Abbruchbedingung.
2. **Frage:** Was soll ein Agent tun, wenn der Quelle ein erforderliches Detail fehlt? **Antwort:** Anhalten und das fehlende Detail melden, statt es zu erfinden.

## Fehlerbehebung

- **Der Agent ändert zu viel:** Nenne im Paket Dateien und ausgeschlossene Aktionen.
- **Der Agent stellt viele Fragen:** Liefere die fehlende Quelle oder ein konkretes Beispiel.
- **Der Agent meldet zu früh Erfolg:** Verlange beobachtete Befehlsausgaben und prüfe die Dateien.
- **Das Paket wird zu lang:** Ersetze kopierte Quelltexte durch Pfad und Revision.

## Nächste Schritte

**Weiter geht es mit [Deiner ersten Aufgabe mit einem Programmieragenten](/articles/effective-ai-coding-agent-first-task/)**. Nutze das Paket als Leitfaden für eine kleine Änderung im Labor.

**Kursnavigation:** [Zurück: Repository-Kontext](/articles/effective-ai-agents-md-context/), [Kursübersicht](/effective-ai-course-start/).
