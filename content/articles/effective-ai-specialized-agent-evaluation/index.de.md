---
title: "OpenClaw und Hermes Agent: ein praxisnaher Vergleich"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Bewerte spezialisierte und dauerhaft aktive KI-Agenten mit einer Zugriffsübersicht, Prüfung von Auslösern, Datenflussprotokoll und Pilotentscheidung."
genre: ["Künstliche Intelligenz", "Softwareentwicklung", "Produktivität"]
tags: ["spezialisierte KI-Agenten", "OpenClaw", "Hermes Agent", "Worker-Agenten", "Bewertung von KI-Agenten", "dauerhaft aktive KI-Agenten"]
cover: "/img/cover/effective-ai-specialized-agent-evaluation.webp"
coverAlt: "Arbeitsblatt mit den Werkzeugen, dem gespeicherten Speicher, den Auslösern, Protokollen und der Prüfentscheidung eines Agenten"
coverCaption: ""
---

[Zurück zum Kurs „Praktische KI-Workflows“](/effective-ai-course-start/)

**Wähle einen spezialisierten Agenten anhand der Aufgabe und seiner Zugriffsanforderungen.** Ein Worker, der eine einzelne Datei prüft, unterscheidet sich von einem dauerhaft aktiven System, das Nachrichten empfängt, Erinnerungen speichert und geplante Aktionen ausführt. Diese optionale Lektion verwendet OpenClaw und Hermes Agent als Beispiele und stellt anschließend ein Bewertungsarbeitsblatt für die Zeit vor der Installation bereit.

**Lernziel:** Du vergleichst Zugriffsrechte und Auslöser eines Agenten und hältst anschließend eine Entscheidung über einen begrenzten Pilotversuch fest.

## Wichtigste Erkenntnisse

- **Rollenbezogener Worker:** ein eng begrenzter Agent, der eine Frage oder ein Artefakt bearbeitet.
- **Dauerhaft aktiver Agent:** ein Dienst oder eine Sitzung, der bzw. die Zustand speichert oder auf spätere Auslöser reagiert.
- **Auslöser:** ein Ereignis, eine Nachricht oder ein Zeitplan, der die Arbeit startet.
- **Zugriffsübersicht:** Liste der Werkzeuge, Konten, Dateien und Schreibrechte, die der Agent erhält.
- **Pilotentscheidung:** ablehnen, einen begrenzten Test durchführen oder einen genau festgelegten Einsatz genehmigen.

## Vor dem Start

**Voraussetzungen:** [Delegation](/articles/effective-ai-agent-delegation/), [Zielschleifen](/articles/effective-ai-bounded-agent-loops/) und ein fiktiver Anwendungsfall. Plane 35 Minuten ein. Der Schwierigkeitsgrad ist mittel. Für diese Lektion musst du keinen dauerhaft aktiven Agenten installieren.

**Anwendungsfall:** Eine Werkstattkoordination möchte, dass ein Assistent einen Zeitplan liest und einen Erinnerungsentwurf vorbereitet. Die Anfrage erlaubt nicht, die Erinnerung zu versenden. Deine Bewertung muss diese Grenze bewahren.

## Rollen vergleichen

| Ansatz | Typische Aufgabe | Erste Frage |
|---|---|---|
| **Ein Chat** | Eine Erinnerung entwerfen | Liegt der Zeitplan vor? |
| **Nur-Lese-Worker** | Zeitplanangaben unabhängig prüfen | Welche Quelle soll er lesen? |
| **Programmieragent** | Ein lokales Berichtsprogramm aktualisieren | Welche Dateien und Tests gelten? |
| **Dauerhafte Plattform** | Im Laufe der Zeit auf Nachrichten oder Zeitpläne reagieren | Welche Auslöser, Werkzeuge und gespeicherten Zustände gibt es? |

**OpenClaw** ist eine Open-Source-Agentenplattform mit Gateway, Messaging-Kanälen, Werkzeugen, Speicher, MCP-Verbindungen und Unteragenten. Die [Übersicht](https://docs.openclaw.ai/start/why-openclaw), der [Leitfaden zu MCP-Verbindungen](https://docs.openclaw.ai/tools/mcp) und der [Leitfaden zu Unteragenten](https://docs.openclaw.ai/tools/subagents) beschreiben diese Komponenten. Prüfe vor einem Pilotversuch die aktiven Kanal-, Werkzeug- und Sandbox-Einstellungen.

**Hermes Agent** ist die Agentenanwendung von Nous Research. Die Hermes-Modellfamilie ist davon getrennt. Die [Dokumentation](https://hermes-agent.nousresearch.com/docs/), der [Leitfaden zur Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) und der [Konfigurationsleitfaden](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/) behandeln CLI, Messaging, Werkzeuge, Speicher und delegierte Aufgaben. Der [Speicherleitfaden](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/) beschreibt lokale Speicher und Schreibfreigaben. Für `memory.write_approval` und `skills.write_approval` ist der dokumentierte Standardwert `false`. Aktiviere die Freigabe oder deaktiviere den betreffenden Speicher für einen Pilotversuch, bei dem Schreibvorgänge geprüft werden müssen. Verlasse dich auf keine der beiden Kontrollen, ohne die laufende Konfiguration zu prüfen.

| Prüfpunkt | OpenClaw | Hermes Agent |
|---|---|---|
| **Einstieg** | Gateway und verbundene Kanäle | CLI oder konfigurierte Messaging-Oberfläche |
| **Delegierte Arbeit** | Unteragenten mit plattformspezifischen Sitzungs- und Werkzeugregeln | Delegierte Aufgaben mit plattformspezifischen Werkzeugregeln |
| **Dauerhafter Zustand** | Aktivierten Speicher und Sitzungsdaten prüfen | Speicher- und Profileinstellungen sowie Schreibvorgänge von Skills prüfen |
| **Wiederkehrende Arbeit** | Konfigurierte Auslöser und Zeitpläne prüfen | [Cron-Aufträge](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/) und Gateway-Zustand prüfen |
| **Erster Pilotversuch** | Eine manuelle Anfrage über einen ausgewählten Kanal | Eine manuelle Anfrage per CLI oder Messaging |

Diese Tabelle nennt Prüfpunkte, keine gleichwertigen Sicherheitsstandards. Notiere installierte Version und aktive Konfiguration, bevor du echte Daten oder Konten freigibst.

**Namen legen kein gemeinsames Berechtigungsmodell fest.** Ein „Unteragent“ kann in einem Produkt andere Dateien, Werkzeuge und den Gesprächsverlauf erhalten als ein Worker in einem anderen. Prüfe die Dokumentation der installierten Version und die aktiven Einstellungen, statt Annahmen zwischen Werkzeugen zu übertragen.

## Zugriffsarbeitsblatt ausfüllen

**Lege für jede Fähigkeit eine Zeile an**, bevor du ein System installierst oder verbindest. Trage, falls ein Produkt verfügbar ist, die tatsächlichen Einstellungen ein. Verwende „unbekannt“, statt zu raten.

| Frage | Antwort für den Werkstatt-Pilot |
|---|---|
| **Aufgabe** | Eine Erinnerung aus einem synthetischen Zeitplan entwerfen |
| **Eingabe** | Eine freigegebene Zeitplandatei |
| **Dateien** | Zeitplandatei lesen, kein Schreibzugriff |
| **Externe Werkzeuge** | Beim ersten Pilot keine |
| **Kontozugriff** | Kein E-Mail- oder Kalenderkonto |
| **Auslöser** | Nur manuelle Anfrage |
| **Speicher- und Skill-Schreibzugriffe** | Aktive Einstellungen notieren und Speicher deaktivieren oder Schreibfreigabe für den Pilot verlangen |
| **Protokolle** | Speicherort, Aufbewahrungsregel, Prompt, Quellrevision und Entwurf notieren |
| **Prüfung** | Mensch prüft Datum, Uhrzeit, Ort und Empfängerliste |
| **Rücknahme** | Entwurf verwerfen und Pilot deaktivieren |

**Der Datenfluss gehört zum Arbeitsblatt.** Notiere, wo Eingaben deinen Computer verlassen, welcher Anbieter sie verarbeitet und wo Gesprächsverläufe oder Erinnerungen gespeichert bleiben. Wenn sich ein Werkzeug mit E-Mail verbindet, halte fest, ob es liest, Entwürfe erstellt oder sendet. Das sind unterschiedliche Berechtigungsbereiche.

## Pilotentscheidung treffen

**Ablehnen:** Der Agent benötigt weitreichende Schreibrechte für ein Postfach, obwohl er nur einen Entwurf erstellen soll, oder Auslöser und Protokolle sind unbekannt. Du musst nichts installieren, um eine ungeeignete Lösung abzulehnen.

**Pilot:** Beschränke die Eingabe auf den synthetischen Zeitplan, verwende einen manuellen Auslöser, deaktiviere das Senden und prüfe einen Entwurf. Erwartetes Ergebnis: eine korrekte Uhrzeit von 19 Uhr und keine versendete Nachricht. Notiere deine eigene Beobachtung, wenn du den Pilot ausführst.

**Genau festgelegten Einsatz genehmigen:** Erst nachdem der Pilot seine Prüfungen besteht und die verantwortliche Person den konkreten Zugriff, Auslöser, Aufbewahrungszeitraum und Prüfablauf akzeptiert. Eine Genehmigung zum Entwerfen erlaubt weder das Senden noch spätere Automatisierung.

## Fehler untersuchen

**Angenommen, ein Erinnerungsentwurf nennt 18 Uhr.** Prüfe, ob der Agent den aktuellen Zeitplan gelesen hat oder ob gespeicherte Erinnerungen beziehungsweise eine alte Nachricht die veraltete Uhrzeit lieferten. Ersetze die veraltete Eingabe, wiederhole einen manuellen Pilotversuch und lasse das Senden deaktiviert. Ein korrekter zweiter Entwurf löscht den ersten Fehler nicht aus dem Protokoll.

**Angenommen, in den Einstellungen erscheint eine MCP-Verbindung, aber kein Werkzeug ist erreichbar.** Kehre zu den [MCP-Verbindungszuständen](/articles/effective-ai-mcp-server-setup/) zurück. Ein gespeicherter Servereintrag beweist keinen erfolgreichen Lesezugriff.

## Übung und Prüfung

**Dein Ergebnis:** ein ausgefülltes Zugriffsarbeitsblatt und eine Entscheidung: Ablehnen, Pilot oder genau festgelegten Einsatz genehmigen. Nenne einen Auslöser, eine Berechtigungsgrenze, eine Frage zum Datenfluss und eine Möglichkeit, den Agenten zu stoppen.

**Abschlussprüfung:** Eine andere Person sollte erkennen, welche Aktion der Agent ausführt, was er liest und speichert, wann er läuft, wer das Ergebnis prüft und wie er deaktiviert wird. Wenn eine Antwort unbekannt ist, wähle Ablehnen oder einen enger begrenzten Pilot.

## Verständnis prüfen

1. **Frage:** Braucht eine Aufgabe, die nur einen Erinnerungsentwurf erstellt, die Berechtigung, E-Mails zu senden? **Antwort:** Nein. Senden bleibt außerhalb des Pilotumfangs.
2. **Frage:** Welche Hermes-Einstellungen musst du vor einem Pilot mit kontrollierten Schreibvorgängen prüfen? **Antwort:** Prüfe aktive Schreiboptionen für Speicher und Skills, einschließlich der Freigabekontrollen.

## Nächste Schritte

**Fahre mit dem [KI-Workflow-Abschlussprojekt](/articles/effective-ai-capstone/) fort.** Für einen breiteren Laufzeitvergleich nutze den [Leitfaden zu Agenten-Laufzeitumgebungen](/articles/best-ai-agent-harnesses/).

**Kursnavigation:** [Zurück: Begrenzte Schleifen](/articles/effective-ai-bounded-agent-loops/), [Kursübersicht](/effective-ai-course-start/).
