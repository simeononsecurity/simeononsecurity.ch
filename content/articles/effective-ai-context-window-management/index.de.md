---
title: "KI-Kontextfenster verwalten: Coding-Agents fokussiert halten"
description: "Steuere den aktiven Kontext einer KI-Aufgabe mit ausgewählten Dateien, kompakten Übergaben und kurzen Worker-Ausgaben. Entscheidungen und Belege bleiben erhalten."
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
genre: ["Künstliche Intelligenz", "Softwareentwicklung"]
tags: ["KI-Kontextfenster verwalten", "Coding-Agent-Kontext", "KI-Übergabe", "Kontextkomprimierung", "Agentenorchestrierung", "Tokenbudget"]
cover: "/img/cover/effective-ai-context-window-management.webp"
coverAlt: "Eine kompakte Übergabenotiz neben ausgewählten Projektdateien und einem deutlich längeren verworfenen Chattranskript"
coverCaption: ""
---

[Zurück zum praktischen KI-Workflow-Kurs](/effective-ai-course-start/)

**Das Kontextfenster enthält den Text und weitere Inhalte, die ein Modell im aktuellen Schritt verarbeitet.** Prompts, Anweisungen, Werkzeugdefinitionen, Dateiausschnitte, Werkzeugausgaben und Gesprächsverlauf belegen Kontext. Diese Lektion zeigt, wie du die nächste Aufgabe fokussierst und eine verlässliche Übergabe hinterlässt.

**Lernziel:** eine kompakte Übergabe erstellen und in einer neuen Sitzung testen.

## Wichtigste Erkenntnisse

- **Tokens** sind Einheiten, mit denen ein Modell Ein- und Ausgaben verarbeitet.
- **Aktiver Kontext** steht in einem Schritt zur Verfügung und unterliegt den Produktgrenzen.
- **Dauerhafte Quellen** liegen außerhalb des Chats in Dateien oder Projektaufzeichnungen.
- **Komprimierung** fasst älteren Kontext zusammen oder entfernt ihn. Dabei kann ein wichtiges Detail verloren gehen.
- **Eine Übergabe** verweist eine neue Sitzung auf aktuelle Quellen und geprüfte Arbeit.

## Vor dem Start

**Voraussetzungen:** dein bearbeitetes Lab aus der [ersten Aufgabe mit einem Coding-Agent](/articles/effective-ai-coding-agent-first-task/), die genehmigte Anforderung und die [Lektion zu Aufgabenpaketen](/articles/effective-ai-task-packets/). Wenn du den Lernpfad genutzt hast, verwende dein manuell bearbeitetes Lab. Plane 35 Minuten ein. Der Schwierigkeitsgrad ist mittel. Lege Kursnotizen außerhalb des entpackten Lab-Ordners ab, damit `git status` nur Codeänderungen zeigt.

## Kontext nach Aufgabe auswählen

**Für die Bearbeitung des Statusfilters** benötigt der Agent `task_report.py`, `docs/requirements.md`, passende Tests und ein kleines Beispiel aus `tasks.json`. Alte Chats, die gesamte Website-Dokumentation und die vollständige Git-Historie sind unnötig. Lies zuerst eine Übersicht und lade danach nur die Dateien, die für die nächste Entscheidung nötig sind.

| Aufgabe | Nützlicher Kontext | Überflüssiger Kontext |
|---|---|---|
| **Verhalten festlegen** | Genehmigte Anforderung und ein Datenbeispiel | Alte Erkundungsgespräche |
| **Programm bearbeiten** | Programm und gezielte Tests | Nicht zugehörige Projektordner |
| **Ergebnis prüfen** | Diff, Testausgabe, Anforderung | Vollständiges Agententranskript |
| **Später fortsetzen** | Übergabenotiz und Quellpfade | Eingefügter mehrstündiger Chat |

**Das ist eine Entscheidung über den Abruf, keine Regel zum Verbergen von Belegen.** Wenn ein Test fehlschlägt, nimm die genaue Ausgabe und die betroffene Datei auf. Entferne irrelevante Protokolle, aber nicht die Details, die zur Diagnose nötig sind.

**Berücksichtige den festen Grundaufwand, bevor du weitere Worker hinzufügst.** Agentenanweisungen und verfügbare Werkzeugschemata belegen möglicherweise Kontext, bevor eine Aufgabendatei gelesen wird. Ein zweiter Worker verursacht einen Teil dieses Aufwands erneut und erstellt zusätzlich einen Bericht, den der Hauptagent prüfen muss. Für eine Änderung an zwei Dateien reicht ein Agent. Bei einer unabhängigen Suche in vielen Quellen kann ein kurzer Worker-Bericht den Kontext der Hauptsitzung entlasten, obwohl der Gesamtverbrauch steigt.

## Kompakte Übergabe erstellen

**Eine Übergabe ist ein kurzer Bericht für die nächste Sitzung.** Sie unterscheidet erledigte von vorgeschlagener Arbeit. Speichere dieses Beispiel außerhalb des Labs unter `course-notes/handoff.md` und ersetze die Beispielbeobachtungen durch deine eigenen.

```text
Ziel: --status open|done zum Aufgabenbericht des Kurses hinzufügen.
Quelle: docs/requirements.md, Version 1.
Arbeitsbereich: entpackter Ordner effective-ai-course-lab.
Aktueller Stand: Der Statusfilter ist in task_report.py und den Tests enthalten.
Geprüft: Notiere das beobachtete Testergebnis und die manuellen Zählungen 4, 2 und 2.
Entscheidung: tasks.json blieb unverändert.
Offen: unabhängige Prüfung von Diff und Quelle.
Nächste Prüfung: Tests und den Fall mit ungültigem Status erneut ausführen.
Abbrechen, wenn: Anforderung oder Basiswert vom obigen Protokoll abweichen.
```

**Das Beispiel behauptet nicht, dass du diese Arbeit ausgeführt hast.** Trage deine beobachteten Testergebnisse und geänderten Dateien ein. Ändert sich der Quellstand, aktualisiere die Übergabe nach erneutem Lesen der Quelle.

## Neue Sitzung testen

**Starte im Lab einen neuen Chat oder eine neue Coding-Agent-Sitzung.** Füge in einem Chat die Übergabe und die `AGENTS.md` des synthetischen Labs ein und nenne die zu prüfenden Dateien. Öffne bei einem Coding-Agent den Lab-Ordner, füge die Übergabe ein und erlaube den Lesezugriff auf die genannten Dateien. Frage:

```text
Nenne anhand dieser Übergabe und der aktuellen Repository-Dateien die genehmigten Statuswerte, den Basiswert und die nächste Prüfung. Nichts bearbeiten.
Melde einen Widerspruch, falls die Übergabe einer aktuellen Quelle widerspricht.
```

**Erwartete Schlussfolgerung:** Die neue Sitzung findet `open` und `done` in `docs/requirements.md`, nennt den Ausgangswert 4 und führt Tests sowie manuelle Prüfungen auf. Wiederholt sie den alten Wert `pending`, lies die Anforderung erneut und korrigiere die Übergabe.

## Orchestrator klein halten

**Ein Orchestrator ist der Hauptagent, der Worker koordiniert.** Gib jedem Worker eine eng gefasste Frage und benannte Eingabedateien. Bitte um eine kompakte Antwort: Befund, Belegpfad, Sicherheit und offene Frage. Speichere ausführliche Protokolle in einer Datei oder in der Sitzung des Workers. Übernimm nur die Punkte, die der Hauptagent für die nächste Entscheidung braucht.

**Beispiel:** Bitte einen Worker mit Lesezugriff, die Tests zu prüfen und „fehlender Fall, Datei und Zeile, vorgeschlagene Prüfung“ zu melden. Lass nicht alle Tests in den Hauptchat kopieren. Der Hauptagent prüft den Befund im Repository, bevor er etwas ändert. Die [Lektion zur Delegation](/articles/effective-ai-agent-delegation/) ergänzt eine unabhängige Worker-Aufgabe, wenn der Umfang den Aufwand rechtfertigt.

**Viele Produkte geben Worker-Sitzungen eigenen Kontext,** aber Vererbung und Isolation unterscheiden sich. Prüfe die aktuellen Produktregeln, bevor du annimmst, dass ein Worker dieselben Anweisungen, Dateien oder Werkzeuge sieht wie der Hauptagent. Die Anleitungen für [Codex-Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) und [Claude-Code-Subagents](https://code.claude.com/docs/en/sub-agents) beschreiben das jeweilige Verhalten.

## Komprimierung mit Bedacht nutzen

**Komprimierung verkürzt den aktiven Verlauf.** Codex, Claude Code und OpenCode unterscheiden sich darin, wann und wie sie komprimieren. Behandle eine komprimierte Zusammenfassung als Hilfe zum Fortsetzen, nicht als vollständige Projektaufzeichnung. Speichere Anforderungen und Entscheidungen in Dateien und prüfe sie nach der Komprimierung erneut. Lies die aktuellen Hinweise zu [Bewährte Vorgehensweisen für Codex](https://learn.chatgpt.com/docs/learn/best-practices), [Claude-Code-Befehlen](https://code.claude.com/docs/en/commands) und [OpenCode-2-Komprimierung](https://opencode.ai/v2/docs/compaction). OpenCode 1 und OpenCode 2 nutzen unterschiedliche Komprimierungsschemata. Prüfe `opencode --version`, bevor du Einstellungen übernimmst.

**Verliert der Assistent eine Einschränkung,** stoppe die Bearbeitung, öffne die Quelle erneut und formuliere das Aufgabenpaket neu. Eine neue Sitzung mit einer kurzen geprüften Übergabe erfordert oft weniger Aufmerksamkeit als wiederholte Korrekturen in einem verwirrten Langzeit-Chat.

## Üben und prüfen

**Dein Arbeitsergebnis:** eine Übergabe mit weniger als 180 Wörtern außerhalb des Labs. Kennzeichne jede Zeile als Quelle, beobachtetes Ergebnis, Entscheidung oder offene Aufgabe. Gib die Übergabe einer neuen Sitzung und notiere, ob sie beide zulässigen Statuswerte und die nächste Prüfung nennt.

**Abschlussprüfung:** Die neue Sitzung nennt `open`, `done`, den Ausgangswert 4 und einen Testschritt, ohne sich auf den alten Chat zu stützen. Ergänze fehlende Punkte und teste erneut in einer weiteren neuen Sitzung.

## Verständnis überprüfen

1. **Frage:** Was gehört in eine Übergabe für eine neue Sitzung? **Antwort:** Ziel, maßgebliche Quelle, aktueller Stand, geprüftes Ergebnis und nächster Schritt.

2. **Frage:** Warum sollte ein Worker-Bericht kurz sein? **Antwort:** Ein knapper Bericht mit Belegen liefert dem Orchestrator das Ergebnis, ohne das Worker-Transkript zu wiederholen.

## Fehlerbehebung

- **Zusammenfassung lässt eine Entscheidung aus:** Ergänze eine kurze Entscheidungszeile mit Quellrevision.
- **Worker-Antwort ist zu lang:** Bitte um eine begrenzte Belegtabelle und Dateiverweise.
- **Übergabe ist veraltet:** Lies aktuelle Quelldateien vor der nächsten Bearbeitung erneut.
- **Kontextdruck bleibt bestehen:** Teile die Aufgabe in kleinere Sitzungen mit getrennten Ergebnissen.

## Nächste Schritte

**Fahre mit der [MCP-Server-Einrichtung](/articles/effective-ai-mcp-server-setup/) fort.** Du fügst ein externes Nur-Lese-Werkzeug hinzu und begrenzt seine Ausgabe.

**Kursnavigation:** [Zurück: Erste Coding-Aufgabe](/articles/effective-ai-coding-agent-first-task/), [Kursübersicht](/effective-ai-course-start/).
