---
title: "ChatGPT- und Claude-Projekte: Wiederverwendbaren KI-Kontext einrichten"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Richte ChatGPT- und Claude-Projekte mit klaren Anweisungen, aktuellen Referenzdateien und einem einfachen Test für wiederverwendeten Kontext ein."
genre: ["Künstliche Intelligenz", "Produktivität"]
tags: ["ChatGPT-Projekte", "Claude-Projekte", "KI-Projektanweisungen", "KI-Kontext", "ChatGPT-Projekteinrichtung", "Claude-Projektwissen"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Zwei geordnete KI-Projektarbeitsbereiche mit Projektübersicht, Referenzdateien und getrennten Gesprächen"
coverCaption: ""
---

[Zurück zum Kurs Praktischer KI-Workflow](/effective-ai-course-start/)

**Lege ein Projekt an, wenn mehrere Gespräche denselben Zweck haben.** Hinterlege stabile Anweisungen und freigegebene Referenzdateien an einem Ort. Halte jedes Gespräch auf eine Aufgabe ausgerichtet. Diese Lektion nutzt eine erfundene Gemeinschaftswerkstatt zum Üben ohne private Daten.

**Lernziel:** Du erstellst ein Projekt mit zwei kontrollierten Quellen und prüfst deren Fakten in einem neuen Chat.

## Wichtigste Erkenntnisse

- **Projektanweisungen** legen wiederverwendbares Verhalten für zusammengehörige Chats fest.
- **Projektquellen** enthalten Referenzmaterial, das der Assistent berücksichtigen soll.
- **Gesprächsverlauf** dokumentiert einen Austausch und ersetzt keine freigegebene Quelle.
- **Ein Test im neuen Chat** zeigt, ob deine Projekteinstellungen genügend Kontext liefern.

## Vor dem Start

**Voraussetzungen:** ein ChatGPT- oder Claude-Konto sowie das Aufgabenpaket aus [Lektion 1](/articles/effective-ai-workflow-foundations/). Plane 35 Minuten ein. Der Schwierigkeitsgrad ist Anfänger. Verwende während der gesamten Übung erfundene Namen, Daten und Orte.

**Erstelle zwei kleine Dateien** auf deinem Computer. Öffne einen Texteditor, füge jeden folgenden Block in eine eigene Datei ein und speichere sie unter dem angegebenen `.md`-Namen. Markdown-Dateien sind einfacher Text. `workshop-brief.md` nennt Zielgruppe und Stil. `approved-schedule.md` enthält den erfundenen offiziellen Zeitplan.

```text
workshop-brief.md, Version 1
Zielgruppe: Personen, die für einen Einführungsworkshop angemeldet sind.
Stil: kurze Sätze und ein freundlicher, sachlicher Ton.
Erfinde keine Preise, Angaben zur Barrierefreiheit oder Parkmöglichkeiten.
```

```text
approved-schedule.md, Version 1
Quellenmarker: WS-2026-11-12-R1
Veranstaltung: Einführung in digitale Sicherheit
Datum: 2026-11-12
Beginn: 7 p.m.
Ort: Community Room A
```

## ChatGPT einrichten

1. **Öffne „Projects“** in der ChatGPT-Seitenleiste und erstelle ein Projekt namens `Workshop Practice`.
2. **Füge die beiden Dateien** als Projektquellen hinzu.
3. **Öffne die Projekteinstellungen** und füge die folgenden Anweisungen ein.
4. **Prüfe die Speicher- und Freigabeeinstellungen** deines Kontos und Arbeitsbereichs, bevor du echte Inhalte hinzufügst.

```text
Nutze approved-schedule.md für Veranstaltungsangaben.
Nutze workshop-brief.md für Zielgruppe und Stil.
Fehlt eine angefragte Angabe, frage nach der Quelle oder kennzeichne sie als unbekannt.
Erstelle nur Entwürfe. Sende oder veröffentliche sie nicht.
Liste nach jeder überarbeiteten Fassung die sachlichen Änderungen auf.
```

**ChatGPT-Projekte bündeln zusammengehörige Chats, Dateien und Anweisungen.** Projekteinstellungen und verfügbare Funktionen unterscheiden sich je nach Tarif und Arbeitsbereich. Wähle beim Erstellen den Projektspeicher, wenn die Option für einen isolierten Test angeboten wird. Beim Standardspeicher kann ein Chat Informationen außerhalb der hochgeladenen Dateien heranziehen. Die eindeutige Quellenmarkierung unten hilft dir, die Datei zu testen, ohne eine Antwort aus dem Speicher als Dateinachweis zu behandeln. Prüfe mit dem [offiziellen Leitfaden zu ChatGPT-Projekten](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) die aktuellen Speicheroptionen.

## Claude einrichten

1. **Öffne „Projects“** in Claude und erstelle ein Projekt mit demselben Übungsnamen.
2. **Füge die beiden Dateien** zur Projektbasis hinzu.
3. **Lege als Projektanweisungen** dieselben fünf Zeilen fest.
4. **Starte einen neuen Chat im Projekt**, um die Einrichtung zu testen.

**Diese Schritte beschreiben klassische Claude-Projekte.** Anthropic führt eine separate Projects-Beta für ausgewählte Pro- und Max-Nutzer von Claude Code ein. In der Beta besteht ein Projekt aus einem Gespräch mit parallelen Cloud-Threads. Prüfe [Was sind Projekte?](https://support.claude.com/en/articles/9517075-what-are-projects) und orientiere dich an der Oberfläche deines Kontos. Klassische Projektanweisungen gelten für alle Chats, und das Projektwissen stellt gemeinsame Referenzmaterialien bereit. Nutze die hochgeladenen Dateien als kontrollierte Fakten. Das Verhalten des Projektspeichers hängt vom Konto und den Einstellungen ab. Behandle Angaben aus einem anderen Chat daher nicht als freigegebenen Zeitplan. Prüfe die aktuellen Einstellungen im [Claude-Leitfaden zur Projekteinstellung](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

| Projektmodus | Gemeinsames Material zum Prüfen | Test in einem neuen Chat |
|---|---|---|
| **ChatGPT-Projekt** | Hochgeladene Dateien, Anweisungen, ausgewählter Speichermodus | Neuer Projektchat nennt die Zeitplanmarkierung |
| **Klassisches Claude-Projekt** | Projektwissen und Anweisungen für alle Chats | Neuer Projektchat nennt die Zeitplanmarkierung |
| **Claude Projects Beta** | Quellen und Kontext im Projekt und in Cloud-Threads | Neuer Projekt-Thread nennt die Zeitplanmarkierung |

**Ein Projekt bündelt Kontext, bestätigt aber keine Quelle.** Die Markierung zeigt, ob eine benannte Datei den Chat erreicht hat. Vergleiche Datum, Uhrzeit und Raum trotzdem selbst mit der Datei.

## Einen neuen Chat testen

**Öffne ein neues ChatGPT-Projektgespräch oder einen neuen klassischen Claude-Projektchat.** Nutze in der Claude Projects Beta einen neuen Thread im Projekt. Bitte um einen kurzen Veranstaltungshinweis. Lass den Zeitplan aus deinem Prompt weg, damit die Projektquellen die nötigen Angaben liefern.

```text
Verfasse eine 100 Wörter lange E-Mail zum bevorstehenden Workshop.
Nenne für Zeit und Ort die Quelldatei und ihren exakten Quellenmarker.
Liste nach dem Entwurf fehlende Angaben auf.
Sende die Nachricht nicht.
```

| Ergebnis | Bedeutung | Nächster Schritt |
|---|---|---|
| **Uhrzeit, Ort und Markierung stimmen** | Die Datei ist für diesen Chat verfügbar | Prüfe die Fakten selbst anhand der Datei |
| **Eine Tatsache ist erfunden** | Anweisungen oder Quellennutzung sind fehlgeschlagen | Entferne die Angabe und grenze die Anfrage enger ein |
| **Quelle fehlt** | Die Referenz hat diesen Chat nicht erreicht | Prüfe Projektzugehörigkeit und Datei-Upload |
| **Eine alte Revision erscheint** | Im Projekt liegen veraltete Inhalte | Ersetze die Quelle und teste erneut |

**Leite aus einer einzigen richtigen Antwort keine Zuverlässigkeit ab.** Der Projektspeicher kann eine vertraute Uhrzeit liefern, ohne die hochgeladene Datei zu lesen. Verlange die genaue Markierung `WS-2026-11-12-R1` und wiederhole den Test dann mit diesem widersprüchlichen Entwurf:

```text
Überarbeite diese Zeile anhand des genehmigten Projektplans:
„Der Kurs Einführung in digitale Sicherheit beginnt um 6 p.m. in Community Room A.“
Nenne die sachliche Änderung, die Quelldatei und den Quellenmarker. Sende die Nachricht nicht.
```

**Erwartete Antwort:** In der Zeile steht 19 Uhr, und sie nennt `approved-schedule.md` mit der Markierung `WS-2026-11-12-R1`. Notiere jeden beobachteten Fehler. Ein erfolgreicher Lauf braucht keinen erfundenen Fehler.

**Beispiel für ein Testprotokoll:** neuer Chat, erste Anfrage, 19 Uhr, Raum Community Room A, Quelle `approved-schedule.md`, Markierung `WS-2026-11-12-R1`, bestanden. Widerspruchsfrage, 18 Uhr auf 19 Uhr korrigiert, bestanden. Dies ist ein Beispielprotokoll. Ersetze es durch deine eigenen Beobachtungen.

## Das Projekt pflegen

**Halte Projektanweisungen kurz.** Hinterlege dort stabile Regeln. Gib aufgabenspezifische Details in jedem Prompt an. Ersetze veraltete Dateien und kennzeichne ihre Revisionen. Trenne nicht zusammengehörige Arbeit in einem anderen Projekt, damit sich die Quellen nicht widersprechen.

**Prüfe vor der Freigabe eines Projekts** seine Dateien, Chats, Anweisungen und Zugriffsliste. Ein Projekt ist ein Arbeitsbereich, kein Freigabesystem. Auch eine Datei mit dem Namen „approved“ braucht für wichtige Arbeiten einen echten Verantwortlichen und einen Revisionsnachweis.

## Üben und überprüfen

**Dein Ergebnis:** ein Projekt mit zwei synthetischen Quelldateien, fünf Anweisungszeilen und einem kurzen Testprotokoll. Halte die beobachtete Uhrzeit, den Ort, den Quellnamen, die Markierung und jede erfundene Tatsache fest. Lösche das Übungsprojekt nach Abschluss, wenn du es nicht mehr brauchst.

**Erwartete Schlussfolgerung:** Ein neuer Chat nutzt Projektquellen für stabile Fakten, während dein Prompt die aktuelle Ausgabe festlegt. Prüfe das Ergebnis anhand der Datei. Fehlt eine Quelle oder liegt eine falsche Revision vor, kehre zur Projekteinstellung zurück.

## Verständnis überprüfen

1. **Frage:** Garantiert ein neuer Chat in einem ChatGPT-Projekt bei jeder Speichereinstellung eine isolierte Umgebung? **Antwort:** Nein. Prüfe den Projektspeichermodus und teste mit einer eindeutigen Quellenmarkierung.

2. **Frage:** Was solltest du tun, wenn das Projekt einen alten Zeitplan wiederholt? **Antwort:** Prüfe die angehängte Quelle und den Speicherumfang, ersetze dann das veraltete Quellenmaterial.

## Fehlerbehebung

- **Projektsteuerung fehlt:** Prüfe deinen aktuellen Tarif und die Arbeitsbereichseinstellungen im Anbieterleitfaden.
- **Antworten widersprechen sich:** Entferne doppelte oder veraltete Quelldateien und starte einen neuen Chat.
- **Unerwartete Freigabe:** Prüfe die Projektmitglieder und entferne sensible Quellen, bevor du fortfährst.
- **Stilabweichungen wiederholen sich:** Kürze die Anweisungen und gib ein kurzes Beispiel im Aufgabenprompt an.

## Nächste Schritte

**Fahre mit [AGENTS.md: Repository-Kontext](/articles/effective-ai-agents-md-context/) fort.** Die nächste Lektion wechselt vom Chatprojekt zu einem lokalen Code-Repository.

**Kursnavigation:** [Zurück: Grundlagen des Workflows](/articles/effective-ai-workflow-foundations/), [Kursübersicht](/effective-ai-course-start/).
