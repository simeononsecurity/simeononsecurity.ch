---
title: "Delegation von KI-Agenten: Aufgaben verteilen und Ergebnisse prüfen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Erfahre, wann ein zweiter KI-Agent hilft, wie du begrenzte Aufgaben vergibst, Bearbeitungskonflikte vermeidest und Belege in der Hauptsitzung zusammenführst."
genre: ["Künstliche Intelligenz", "Softwareentwicklung"]
tags: ["Delegation von KI-Agenten", "Subagenten", "Arbeitsagenten", "Orchestrator-Kontext", "KI-Worktrees", "Parallele KI-Aufgaben"]
cover: "/img/cover/effective-ai-agent-delegation.webp"
coverAlt: "Ein Hauptagent verteilt getrennte Recherche- und Prüftätigkeiten, bevor er kurze Belegberichte zusammenführt."
coverCaption: ""
---

[Zurück zum Kurs Praktische KI-Workflows](/effective-ai-course-start/)

**Delegiere eine unabhängige Frage, wenn genug Arbeit anfällt, um eine separate Sitzung zu rechtfertigen.** Ein Arbeitsagent prüft Quellen, untersucht Tests oder entwirft eine klar begrenzte Änderung in seinem eigenen Kontext. Der Hauptagent prüft und integriert das Ergebnis. In dieser Lektion dient ein Dokumentationsvergleich als Beispiel, während die Hauptsitzung die kleine Laboraufgabe fortsetzt.

**Lernziel:** Du weist einem unabhängigen Arbeitsagenten eine Prüfung zu und verifizierst anschließend seinen kurzen Belegbericht.

## Wichtigste Punkte

- **Orchestrator:** der Hauptagent, der Aufgabe und Abschlussprüfung koordiniert.
- **Arbeitsagent:** ein separater Agent mit einem klar begrenzten Ergebnis.
- **Unabhängige Arbeit:** eine Teilaufgabe, deren Antwort nicht von einem unfertigen Ergebnis eines anderen Agenten abhängt.
- **Zuständigkeit:** eine Datei oder Frage, die genau einem Arbeitsagenten zugewiesen ist.
- **Integration:** der Vergleich des Agentenergebnisses mit den aktuellen Quellen durch den Hauptagenten.

## Vor dem Start

**Voraussetzungen:** deine [Kontextübergabe](/articles/effective-ai-context-window-management/) und [Ergebnisprüfung](/articles/effective-ai-output-verification/). Plane 40 Minuten ein. Der Schwierigkeitsgrad ist mittel. Für die vernetzte Variante brauchst du ein Produkt mit Unterstützung für Arbeitsagenten. Die Lernvariante nutzt einen separaten Chat und eine manuelle Integration.

**Starte mit einem unveränderten Projekt.** Sichere den bearbeiteten Filter-Diff und den Testbericht außerhalb des Labors. Entpacke die ursprüngliche ZIP-Datei in einen neuen temporären Ordner. Führe den Startbefehl und die beiden Basistests aus. Wiederhole die Git-Baseline aus der Kurseinrichtung und erstelle die kurze `AGENTS.md`- sowie die optionale `CLAUDE.md`-Anleitung aus der Lektion zum Repository-Kontext neu. Committe diese Anleitungsdateien selbst und prüfe, ob `git status --short` keine Änderungen meldet. Bewahre die bearbeitete Filterkopie als Referenz auf, führe die Agentenübung aber mit dem unveränderten Starter aus.

## Wann sich Delegation lohnt

**Nutze einen Agenten** für eine kleine, aufeinanderfolgende Änderung. Delegation kostet Einrichtung, Tokens und Prüfaufwand. Setze einen Arbeitsagenten ein, wenn eine schreibgeschützte Frage unabhängig ist und sonst viele Dateien oder Quellseiten in der Hauptsitzung landen würden.

| Laboraufgabe | Delegieren? | Grund |
|---|---|---|
| **Einen Filter mit zwei Werten ergänzen** | Meistens nicht | Eine kleine Datei und gezielte Tests |
| **Fehlende Fälle in zwei Basistests finden** | Meistens nicht | Der Hauptagent liest eine kurze Datei schneller |
| **Drei aktuelle Produktdokumentationen vergleichen** | Ja, schreibgeschützt | Die Quellen bleiben im Kontext des Arbeitsagenten |
| **Dieselbe Funktion zweimal bearbeiten** | Nein | Gleichzeitige Änderungen verursachen Konflikte |

**Der Arbeitsagent braucht weniger Kontext als der Orchestrator,** keine Kopie des gesamten Gesprächs. Gib ihm Ziel, Quellpfad, Aufgabenbereich und gewünschtes Rückgabeformat. Halte den Belegbericht in der Hauptsitzung kurz. Prüfe zitierte Dateien selbst, bevor du handelst.

## Einen schreibgeschützten Agenten einsetzen

**Halte die Hauptaufgabe klein.** Lies in der Hauptsitzung die lokale `AGENTS.md` und notiere, welche Datei den Testbefehl enthält. Weise einem Arbeitsagenten die folgende unabhängige Recherchefrage zu. Für diese Aufgabe braucht er weder das gesamte Labor noch den bisherigen Chat.

**Verbundene Variante:** Öffne das Labor in Codex, Claude Code oder einem anderen Produkt mit Arbeitsagenten-Unterstützung. Bitte den Hauptagenten, die folgende schreibgeschützte Aufgabe an einen Agenten zu delegieren. Prüfe im Werkzeugprotokoll, dass der Agent wirklich gestartet ist und einen Bericht geliefert hat. Bietet das Produkt keine Agentenfunktion, verwende eine separate Sitzung und kennzeichne sie als separaten Arbeitsagenten. Die Anleitungen für [Codex-Subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude-Code-Subagenten](https://code.claude.com/docs/en/sub-agents) und [OpenCode-Agenten](https://opencode.ai/docs/agents/) beschreiben die aktuellen Steuerelemente.

**Lernvariante:** Öffne einen neuen Chat für dieselbe Aufgabe. Gib ihm die drei offiziellen Links oder Quellenauszüge. Kennzeichne ihn als simulierten Arbeitsagenten. Ein zweiter Chat hat einen separaten Kontext, belegt aber keine native Subagent-Ausführung.

```text
Nutze die aktuellen offiziellen Dokumentationen zu Codex AGENTS.md, Claude Code Memory und OpenCode Rules.
Vergleiche, wie jedes Produkt Projektanweisungsdateien lädt.
Bearbeite keine Dateien.
Gib höchstens drei Zeilen zurück: Produkt, Anweisungsdatei, Quell-URL
und ein Verhalten beim Laden. Kennzeichne Unsicherheit. Füge keine vollständigen Seiten ein.
```

**Quellen:** [Codex-Projektanweisungen](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude-Code-Speicheranleitung](https://code.claude.com/docs/en/memory) und [OpenCode-Regeln](https://opencode.ai/docs/rules/). Ein erwarteter Bericht nennt für Codex und OpenCode `AGENTS.md`. Aktuelle Claude-Code-Versionen laden `AGENTS.md` ebenfalls direkt, wenn keine `CLAUDE.md` oder `CLAUDE.local.md` Vorrang hat. Dieses Labor verwendet eine `CLAUDE.md`-Datei mit einem `@AGENTS.md`-Import. Das unterstützt auch ältere oder anders konfigurierte Sitzungen. Prüfe die aktuellen Seiten und Versionen, bevor du dieses Beispiel als beobachtetes Agentenergebnis darstellst.

## Ergebnisse integrieren

**Öffne die zitierten Quellseiten selbst.** Behauptet der Arbeitsagent etwa, Claude Code brauche immer einen `CLAUDE.md`-Import, prüfe die Memory-Anleitung und korrigiere den Bericht. Vergleiche den Bericht mit deinen lokalen Anleitungsdateien. Schreibe eine kurze Integrationsnotiz:

```text
Übernommen: Codex und OpenCode verwenden AGENTS.md als Projektanleitung.
Aktuelle Claude-Code-Versionen können AGENTS.md direkt laden. Dieses Labor
verwendet CLAUDE.md mit einem @AGENTS.md-Import für eine stabile gemeinsame Karte.
Belege: Notiere die drei aktuellen offiziellen Seiten und das Prüfdatum.
Entscheidung: Behalte eine kurze gemeinsame Karte und eine Claude-Importdatei.
```

**Diese Notiz ist das nützliche Arbeitsergebnis.** Der Orchestrator braucht geprüfte Erkenntnisse und Quellpfade, nicht das Rechercheprotokoll. Delegation verbraucht insgesamt mehr Tokens. Halte den Hauptchat nur dann kleiner, wenn die separate Arbeit Aufmerksamkeit spart.

## Zuständigkeit für Änderungen festlegen

**Wenn Arbeitsagenten Dateien bearbeiten,** teile die Zuständigkeit nach Dateien auf oder verwende getrennte Worktrees für überlappende Aufgaben. Ein Worktree ist ein weiterer Checkout desselben Git-Repositories mit eigenen Arbeitsdateien. So bleiben gleichzeitige Änderungen getrennt. Der Hauptagent prüft und übernimmt das Ergebnis anschließend über einen expliziten Merge, Cherry-pick oder Patch und führt die Tests im integrierten Checkout erneut aus.

| Agent | Zuständigkeit | Rückgabe |
|---|---|---|
| **Implementierung** | `task_report.py` | Diff und Testbefehl |
| **Testautor** | `tests/test_task_report.py` | Testfälle und beobachtetes Ergebnis |
| **Orchestrator** | Anforderung und Abschlussintegration | Zusammengeführter Diff und Abnahmenotiz |

**Das kleine Labor braucht keine parallelen Änderungen.** Die Tabelle zeigt ein Zuständigkeitsmuster für größere Aufgaben. Tests in einem Worktree validieren keine Implementierung, die in einem anderen Worktree isoliert liegt. Verändert ein zweiter Agent dieselbe Funktion, arbeite nacheinander oder lasse einen Agenten nur prüfen. Getrennte Worktrees verhindern Dateikollisionen, lösen aber keine widersprüchlichen Anforderungen.

## Produktverhalten prüfen

**Subagenten unterscheiden sich je nach Host.** Codex, Claude Code und OpenCode haben unterschiedliche Kontextvererbung, Werkzeugrechte und Ergebniszustellung. Lies die Anleitungen für [Codex-Subagenten](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude-Code-Subagenten](https://code.claude.com/docs/en/sub-agents) und [OpenCode-Agenten](https://opencode.ai/docs/agents/) für dein installiertes Produkt. Nimm nicht an, dass ein Arbeitsagent den gesamten Kontext des Hauptagenten oder einen isolierten Worktree erhält.

## Übung und Prüfung

**Dein Ergebnis:** ein kurzer Bericht des Dokumentationsagenten und eine Integrationsnotiz. Verwende in der Lernvariante einen neuen Chat und kennzeichne ihn als simulierten Arbeitsagenten. Behaupte auf diesem Weg keine native Subagent-Ausführung.

**Abschlussprüfung:** Der Bericht nennt drei offizielle Quellen, bleibt bei der Frage und hält das Längenlimit ein. Deine Integrationsnotiz prüft die Quellen und nennt die Anleitungsdateien des Labors.

## Verständnis prüfen

1. **Frage:** Wann hilft ein Arbeitsagent mehr als ein einzelner Agent? **Antwort:** Wenn er eine unabhängige Frage oder ein eigenes Ergebnis mit einem brauchbaren Belegbericht bearbeitet.

2. **Frage:** Was muss nach Änderungen an überlappenden Dateien geschehen? **Antwort:** Änderungen integrieren, den gemeinsamen Diff prüfen und die Kontrollen erneut ausführen.

## Fehlerbehebung

- **Der Arbeitsagent liefert ein langes Protokoll:** Bitte um eine kürzere Tabelle mit Belegen und Dateiverweisen.
- **Arbeitsagenten widersprechen sich:** Lies die maßgebliche Datei erneut, bevor du dich entscheidest.
- **Zwei Änderungen überlappen:** Stoppe eine Bearbeitung und weise Zuständigkeiten oder getrennte Worktrees zu.
- **Der Zugriff auf Werkzeuge unterscheidet sich:** Prüfe die Rechte des Arbeitsagenten, statt Elternrechte anzunehmen.

## Nächste Schritte

**Fahre mit [Begrenzten Zielschleifen](/articles/effective-ai-bounded-agent-loops/)** fort. Für Teamregeln über dieses kleine Labor hinaus gibt es den [Kurs zur Umsetzung von KI-Zusammenarbeit](/ai-collaboration-course-start/).

**Kursnavigation:** [Zurück: Ergebnisprüfung](/articles/effective-ai-output-verification/), [Kursübersicht](/effective-ai-course-start/).
