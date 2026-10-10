---
title: "GitHub Copilot CLI vs. VS Code: Workflow-Vergleich 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Vergleiche den Copilot-Terminalagenten mit seiner VS-Code-Erfahrung, einschließlich Editor-Kontext, visuellen Diffs, Agent-Modus, CLI-Integration und Kontorichtlinien."
genre: ["Entwicklerwerkzeuge", "Künstliche Intelligenz", "Softwareentwicklung"]
tags: ["GitHub Copilot CLI vs VS Code", "Copilot CLI", "GitHub Copilot", "VS Code", "Agent-Modus", "CLI vs GUI", "Editor-Kontext", "Inline-Vorschläge", "visueller Diff", "Copilot-Sitzungen", "Terminalagent", "GitHub-Workflow", "Code-Review", "IDE-Integration", "MCP-Tools", "Agent-Berechtigungen", "AI Credits", "Entwicklerwerkzeuge", "Programmierassistent", "Automatisierung"]
cover: "/img/cover/github-copilot-cli-vs-vscode.webp"
coverAlt: "Terminal-Prompt mit einer Editor-Auswahl und einem visuellen Diff in einem blau-grünen Programmierbereich"
coverCaption: ""
---

**GitHub Copilot CLI und Copilot in VS Code bieten verschiedene Einstiegspunkte für Programmierarbeit.** CLI beginnt mit Shell und Aufgaben-Prompt. VS Code verbindet Editor-Kontext, Vorschläge, Chat und Agent-Workflows. Beide müssen unter derselben Konto- und Repository-Richtlinie bewertet werden.

**Die Wahl schließt die andere Oberfläche nicht aus.** GitHub dokumentiert eine Verbindung zwischen Copilot CLI und VS Code. Eine terminalbasierte Aufgabe profitiert von Editor-Auswahl und visueller Prüfung, wenn du beide ausdrücklich verbindest.

## Wichtigste Erkenntnisse

- **Nutze Copilot CLI für terminalbasierte Aufgaben** und unterstützte programmatische Aufrufe.
- **Nutze Copilot in VS Code für editorzentrierte Arbeit**, einschließlich Inline-Hilfe und Agent-Modus.
- **Verbinde CLI mit VS Code**, wenn Terminal-Prompts Editor-Kontext und Diffs benötigen.
- **Prüfe Konto-, Modell- und Richtlinieneinstellungen**, auch innerhalb derselben Produktfamilie.

**Umfang und Datum:** Offizielle Dokumentation wurde am 10. Oktober 2026 geprüft. Dieser Vergleich behandelt das eigenständige `copilot` CLI und Copilot in VS Code, nicht die alte `gh copilot`-Erweiterung oder einen Cloud-Agenten für ein GitHub-Issue. Voraussetzungen sind ein testbares Repository und erlaubter Copilot-Zugriff. Plane eine Stunde für den Versuch ein.

## Drei Arbeitsweisen

| Workflow | Hauptinteraktion | Geeignete Testaufgabe |
|---|---|---|
| **Eigenständiges CLI** | Terminal-Prompt und Befehlsausgabe | Einen reproduzierten Testfehler erklären und beheben |
| **VS-Code-Integration** | Editor-Auswahl, Chat, Vorschläge und Diffs | Eine ausgewählte Funktion und ihre Tests ändern |
| **CLI mit VS Code verbunden** | Terminalaufgabe mit Editor-Kontext und Review | In der Shell untersuchen und den Patch visuell prüfen |

**Der hybride Ablauf bleibt eine CLI-Sitzung.** Die Ausführung in einem integrierten Terminal macht daraus nicht automatisch eine native Agent-Modus-Unterhaltung des Editors. Prüfe aktive Sitzung und Verbindung, statt dich auf das Fenster mit dem Prompt zu verlassen.

## Was das CLI bietet

```bash
copilot
```

**Der aktuelle eigenständige Befehl startet den Terminalagenten.** Der [Copilot-CLI-Überblick](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-cli) von GitHub beschreibt interaktive und programmatische Nutzung sowie Planung und Werkzeugberechtigungen. Bewerte ihn dort, wo Terminalausgabe den Hauptnachweis liefert.

**Eine gute erste Aufgabe hat einen konkreten Fehler.** Übergib den fehlschlagenden Befehl, erwartetes Verhalten und eine Einschränkung gegen fremde Refactorings. Fordere die Reproduktion vor Dateiänderungen. Prüfe, ob die Erklärung zur beobachteten Testausgabe passt.

**Automatisierung braucht klare Grenzen.** Nutze die aktuellen [CLI-Anleitungen](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli) für Aufruf und Steuerung. Definiere erlaubte Werkzeuge, Zeitlimits und Ausgabehandling vor unbeaufsichtigten Jobs. Verwandle keine interaktive Berechtigungspolitik in eine pauschale Pipeline-Freigabe.

**Sandboxing verändert den Versuchsrahmen.** GitHub dokumentiert lokale Sandbox-Grenzen für Dateisystem, Netzwerk und System sowie Cloud-Sandboxes für isolierte Ausführung. Ein Trusted-Directory-Prompt und ein Freigabe-Flag ersetzen diese Grenzen nicht. Prüfe Sandbox, Netzwerkzugriff und Schreibbereich zuerst mit einer harmlosen Fixture.

## Was VS Code ergänzt

**Copilots IDE-Erfahrung umfasst Vorschläge, Chat und Agent-Aufgaben.** Die [IDE-Übersicht](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-in-ides) trennt diese Funktionen. Inline-Hilfe passt zu Arbeit, bei der du der primäre Editor bleibst. Agent-Modus passt zu einem begrenzten Ergebnis über mehrere Dateien.

**Agent-Modus bearbeitet Dateien und führt Befehle iterativ aus.** Der [Agent-Modus-Leitfaden](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-agent-mode?tool=vscode) beschreibt Agent-Auswahl, Änderungsprüfung und MCP-Erweiterungen. Verfügbarkeit und Befehlsfreigaben hängen zusätzlich von Konfiguration und Administration ab.

**Bewerte Kontextübertragung bewusst.** Wähle eine Funktion und bitte um eine Erklärung ihrer Fehlerbehandlung. Bitte danach um eine kleine Änderung mit unabhängigem Test. Notiere, ob Nachbardateien nötig waren oder eine Agent-Annahme korrigiert werden musste.

{{< figure src="copilot-terminal-editor-bridge.webp" alt="Terminal-Prompt mit einer Editor-Auswahl und einem nebeneinander angezeigten Code-Diff in einem Repository-Arbeitsbereich" caption="Eine verbundene CLI-Sitzung verbindet Terminaleingabe mit Editor-Review" >}}

## Die beiden Oberflächen verbinden

```text
/ide
```

**Nutze `/ide` in einer interaktiven Copilot-CLI-Sitzung**, um die VS-Code-Verbindung zu prüfen oder zu ändern. Der [Verbindungsleitfaden](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/connecting-vs-code) beschreibt Trusted-Workspace-Abgleich, geteilte Editor-Auswahl und vorgeschlagene Dateiänderungen als Diffs.

**Automatische Verbindung hängt vom Workspace-Abgleich ab.** Ein lokales CLI verbindet sich nicht mit einem entfernten Codespace, nur weil der Repository-Name passt. Starte CLI in der passenden Umgebung. Eine breite Änderungsfreigabe umgeht außerdem die Diff-Genehmigung. Prüfe Berechtigungen, wenn erwartete Prompts verschwinden.

**CLI-Protokolle erscheinen in der Sessions-Ansicht von VS Code**, mit Fortsetzung über Resume in Terminal. Das erhält den Terminal-Workflow. Es macht die Unterhaltung nicht automatisch zu einer austauschbaren nativen Editor-Agent-Sitzung.

| Vor der Verbindung | Prüfen |
|---|---|
| **Workspace** | Der gewünschte Ordner ist offen und vertrauenswürdig |
| **Ausführungsort** | CLI und Editor-Integration zeigen auf dieselbe Umgebung |
| **Auswahl** | Markierter Code passt zur aktuellen Anfrage |
| **Berechtigungen** | Prüfung vorgeschlagener Änderungen bleibt bei Bedarf aktiv |
| **Sitzung** | Die beabsichtigte Unterhaltung wird fortgesetzt |

## Modelle, Abrechnung und Richtlinien

**Nutze für beide Oberflächen dasselbe ausgewählte Modell, wenn verfügbar.** Bei unterschiedlichen Optionen muss der Unterschied dokumentiert werden. Modell, Kontextauswahl oder Werkzeugset verändern den Versuch über den Vergleich von Grafik- und Terminaloberfläche hinaus.

**Prüfe die aktuelle Nutzungsabrechnung in deinem Konto.** GitHub-Agent-Dokumentation nennt AI Credits. Übertrage alte Premium-Request-Schätzungen nicht auf ein aktuelles Konto, ohne das Abrechnungsmodell zu prüfen. Ein CLI-Prompt und eine Editor-Aufgabe sind nicht automatisch gleichwertige Arbeitseinheiten.

**Organisationszugriff ist Voraussetzung.** Fehlt eine Funktion, prüfe die Richtlinie vor einer Neuinstallation der Erweiterung. Erfasse genehmigte Werkzeuge und Integrationen für beide Oberflächen. Ein Provider-Login erteilt nicht automatisch Zugriff auf jedes Repository oder jeden externen Dienst.

## Einen Paarversuch durchführen

**Bereite zwei Kopien derselben Ausgangsrevision vor.** Verwende gleiche Anweisungen und Akzeptanztests. Führe den ersten Versuch im eigenständigen CLI und den zweiten im VS-Code-Agent-Modus aus. Führe einen dritten Versuch mit verbundenem CLI nur aus, wenn die gemischte Interaktion zu deinem Alltag passt.

| Messung | Grund für die Aufzeichnung |
|---|---|
| **Bereitgestellter Kontext** | Zeigt versteckten manuellen Einrichtungsaufwand |
| **Korrektheit** | Trennt plausiblen Code von verifiziertem Fix |
| **Freigabeschritte** | Zeigt Aufsichtsaufwand unter gleicher Richtlinie |
| **Reviewzeit** | Misst Aufwand zum Verstehen des gesamten Patches |
| **Manuelle Reparaturen** | Erfasst Restarbeit nach dem Agenten |
| **Nutzung** | Verbindet Kosten mit akzeptierten Ergebnissen |

**Lass Wiederherstellung im Test.** Lehne einen vorgeschlagenen Ansatz ab und erkläre warum. Beobachte, ob der nächste Versuch brauchbare Arbeit erhält und die Korrektur respektiert. Das zeigt mehr über tägliche Nutzung als eine einzige ununterbrochene Demo.

## Fehlerbehebung und nächste Schritte

**Wenn CLI das falsche Editorfenster verbindet**, prüfe `/ide` und wähle den gewünschten Workspace. Wenn visuelle Freigabe fehlt, prüfe breite Änderungsberechtigungen. Wenn Agent-Modus fehlt, prüfe Erweiterungsstatus und Organisationsrichtlinie.

**Wähle das eigenständige CLI**, wenn Shell-Kontext und wiederholbarer Aufgabenaufruf dominieren. **Wähle VS Code**, wenn Auswahlkontext, Inline-Arbeit und grafische Prüfung dominieren. **Nutze das verbundene CLI**, wenn Terminaleingabe und Editorprüfung gut zusammenspielen.

**Für Vergleiche zwischen Anbietern** lies den [CLI-Hauptvergleich](/articles/cli-coding-agents-comparison/) oder den [GUI-Hauptvergleich](/articles/gui-coding-agents-comparison/). Trenne diese Bewertungen von diesem Interface-Versuch innerhalb derselben Produktfamilie.
