---
title: "MCP-Server einrichten: Berechtigungen, Werkzeugtests und sichere Entfernung"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Verbinden Sie einen schreibgeschützten MCP-Dokumentationsserver, prüfen Sie seine Werkzeuge, führen Sie einen echten Lesezugriff aus und entfernen Sie die Verbindung."
genre: ["Künstliche Intelligenz", "Entwicklerwerkzeuge"]
tags: ["MCP-Server einrichten", "Modellkontextprotokoll (MCP)", "MCP-Berechtigungen", "MCP in Codex", "MCP in Claude Code", "MCP in OpenCode"]
cover: "/img/cover/effective-ai-mcp-server-setup.webp"
coverAlt: "Ein KI-Client ist mit einem schreibgeschützten Dokumentationsserver verbunden. Werkzeug und Zugriffsgrenze sind sichtbar."
coverCaption: ""
---

[Zurück zum Kurs Praktischer KI-Workflow](/effective-ai-course-start/)

**Verwenden Sie einen MCP-Server, wenn eine Aufgabe ein wiederverwendbares Werkzeug oder aktuelle Informationen außerhalb des Projekts benötigt.** Das Model Context Protocol, kurz MCP, legt fest, wie Client und Server Informationen über Werkzeuge, Ressourcen und Prompts austauschen. Ein Servereintrag beweist nicht, dass das Werkzeug funktioniert. Diese Lektion prüft eine schreibgeschützte Dokumentationsverbindung.

**Lernziel:** Sie unterscheiden die Konfiguration von einem echten MCP-Lesezugriff und dokumentieren die sichere Entfernung.

## Wichtigste Erkenntnisse

- **MCP-Host:** KI-Anwendung, die Nutzer, Modelle, Berechtigungen und Clients koordiniert.
- **MCP-Client:** Protokollkomponente, die mit einem Server kommuniziert.
- **MCP-Server:** Programm oder Remotedienst, der Werkzeuge, Ressourcen oder Prompts anbietet.
- **Werkzeugerkennung:** Nachweis einer benannten Funktion im Client.
- **Werkzeugausführung:** Nachweis eines echten Aufrufs und der zurückgegebenen Inhalte.
- **Berechtigungsumfang:** Zugriff, den Host, Server, Konto und Nutzer gewähren.

## Vor dem Start

**Voraussetzungen:** [Übung zu Kontext und Übergaben](/articles/effective-ai-context-window-management/) und eine aktuelle Codex-CLI-Installation für den geführten Ablauf. Planen Sie 35 Minuten ein. Schwierigkeitsgrad: mittel. Andere Coding-Agenten haben eigene Einrichtungsanleitungen. Der [offizielle OpenAI Docs MCP-Server](https://learn.chatgpt.com/learn/docs-mcp) bietet schreibgeschützte Entwicklerdokumentation und benötigt keinen Upload von Kursdaten.

**Verwenden Sie das synthetische Kurslabor.** Verbinden Sie für diese Übung keinen Kalender, keine E-Mail und kein Produktivsystem. Ein Dokumentationsabruf reicht aus, um die Verbindungszustände kennenzulernen.

## Die Grenze verstehen

| Zustand | Was er belegt | Was er nicht belegt |
|---|---|---|
| **Konfiguriert** | Ein Servereintrag ist vorhanden | Erreichbarkeit |
| **Verbunden** | Der Client hat den Server erreicht | Dass nützliche Werkzeuge vorhanden sind |
| **Entdeckt** | Ein benanntes Werkzeug wird angezeigt | Dass sein Aufruf gelingt |
| **Ausgeführt** | Ein Aufruf hat Inhalte zurückgegeben | Dass die endgültige Aufgabe korrekt ist |
| **Geprüft** | Quelle und Ausgabe beantworten die Frage | Dass künftige Aufrufe immer funktionieren |

**MCP gewährt selbst keine Kontoberechtigung.** Client-Host, Server, Authentifizierung, Kontoumfang und lokale Freigabeeinstellungen sind ebenfalls entscheidend. Die [MCP-Spezifikation](https://modelcontextprotocol.io/specification/2026-07-28) definiert das Protokoll. Jedes Produkt bestimmt seine eigene Bedienung.

**Behandeln Sie Serverausgaben als Quellenmaterial.** Eine abgerufene Seite kann Ihre Aufgabe nicht überschreiben und keine Dateischreibberechtigung erteilen. Jede Werkzeugdefinition beansprucht außerdem Kontext. Verbinden Sie nur den für diesen Lesezugriff nötigen Server und entfernen Sie ihn anschließend.

## Dokumentation schreibgeschützt anbinden

**Führen Sie in Codex CLI** diese Befehle in einem Terminal aus. Der erste fügt den öffentlichen Dokumentationsserver hinzu. Der zweite zeigt konfigurierte Server an.

```bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

**Erwarteter Konfigurationsnachweis:** Die Liste enthält `openaiDeveloperDocs`. Das belegt nur die Registrierung. Starten Sie eine neue Codex-Sitzung im entpackten Laborordner und prüfen Sie die MCP-Werkzeugliste mit `/mcp`. Verwenden Sie die Werkzeugnamen, die Ihre installierte Version anzeigt.

**Fordern Sie einen echten Lesezugriff an:**

```text
Verwende den MCP-Server für OpenAI-Entwicklerdokumentation, um die aktuellen AGENTS.md-Hinweise zu finden.
Gib den Titel der Quellseite, ihre URL und zwei relevante Punkte für dieses Labor zurück. Nenne das verwendete MCP-Werkzeug.
Ändere keine Dateien.
```
**Prüfen Sie das Ergebnis.** Die zurückgegebene Seite sollte `AGENTS.md` als Repository-Anleitung beschreiben und die genaue Quell-URL enthalten. Öffnen Sie die zitierte Seite selbst und bestätigen Sie ihr Thema. Eine Antwort ohne MCP-Aufruf im Protokoll ist eine normale Antwort, kein Ausführungsnachweis.

## Einen Fehler diagnostizieren

**Wenn `codex mcp list` den Server zeigt, aber `/mcp` keine Werkzeuge aufführt,** war die Registrierung erfolgreich, die Erkennung jedoch nicht. Starten Sie die Sitzung neu, prüfen Sie aktive Server mit `/mcp` und die gespeicherte Konfiguration mit `codex mcp get openaiDeveloperDocs`. Kontrollieren Sie danach Server-URL und Netzwerkzugriff. Behaupten Sie nicht, der MCP-Aufbau sei allein durch den Konfigurationseintrag gelungen.

**Wenn ein Werkzeug erscheint, der Lesezugriff aber fehlschlägt,** notieren Sie den Fehler und wiederholen Sie den Aufruf einmal nach einer Verbindungsprüfung. Scheitert derselbe Aufruf erneut, verwenden Sie die zitierte offizielle Seite im Browser als Ersatzquelle und markieren Sie die MCP-Übung als unvollständig. Erfinden Sie kein Werkzeugergebnis.

## Verbindung entfernen

**Entfernen Sie nach dem Lesezugriff** den Übungsserver aus Codex CLI und prüfen Sie, ob der Eintrag verschwunden ist.

```bash
codex mcp remove openaiDeveloperDocs
codex mcp list
```

**Erwarteter Entfernungsnachweis:** `openaiDeveloperDocs` fehlt in der neuen Liste. Starten Sie eine aktive Codex-Sitzung neu, bevor Sie prüfen, ob sich ihre verfügbaren Werkzeuge geändert haben. Das Entfernen einer lokalen Definition widerruft keine separate Kontofreigabe, die ein anderer Dienst verwendet.

## Eine andere Anwendung nutzen

**Claude Code und OpenCode unterstützen MCP ebenfalls.** Folgen Sie der [MCP-Anleitung für Claude Code](https://code.claude.com/docs/en/mcp) oder der [OpenCode-MCP-Anleitung](https://opencode.ai/docs/mcp-servers/) für Ihre installierte Version. Dokumentieren Sie dieselben fünf Zustände: konfiguriert, verbunden, entdeckt, ausgeführt und geprüft. OpenCode-Konfigurationsschema und Agent-Berechtigungen unterscheiden sich je nach Version. Übernehmen Sie Beispiele aus der zu Ihrer Installation passenden Anleitung.

**Für einen reinen Browserweg** lesen Sie die [offizielle AGENTS.md-Seite](https://learn.chatgpt.com/docs/agent-configuration/agents-md) und füllen dasselbe Prüfprotokoll aus. Kennzeichnen Sie Werkzeugerkennung und -ausführung mit „nicht ausgeführt“. Dieser Weg vermittelt Quellenprüfung, belegt aber keinen MCP-Betrieb.

## Üben und prüfen

**Ihr Ergebnis:** ein fünfzeiliger Verbindungsnachweis mit Servername, Werkzeugname, Quell-URL, beobachtetem Ergebnis und Entfernungsnachweis. Screenshots und Protokolle dürfen keine Tokens oder Kontokennungen enthalten.

**Abschlussprüfung:** Der verbundene Ablauf ist erst erfolgreich, wenn ein echter Werkzeugaufruf Inhalte gelesen hat und die Konfiguration später entfernt wurde. Der Ersatzweg besteht die Quellenprüfung mit MCP als nicht ausgeführt.

## Verständnis prüfen

1. **Frage:** Beweist ein gespeicherter MCP-Servereintrag, dass ein Werkzeug funktioniert hat? **Antwort:** Nein. Prüfen Sie Erkennung, Berechtigung und einen echten Lesezugriff.
2. **Frage:** Welche zusätzlichen Kontextkosten entstehen durch eine umfangreiche MCP-Verbindung? **Antwort:** Werkzeugbeschreibungen und Schemas beanspruchen einen Teil des aktiven Kontexts.

## Fehlerbehebung

- **Unbekannter Befehl `codex`:** Installieren oder aktualisieren Sie Codex CLI über die verlinkte offizielle Anleitung.
- **Server gelistet, kein Werkzeug:** Prüfen Sie Sitzungsstatus und Serverdiagnose.
- **Werkzeugaufruf liefert unpassende Inhalte:** Präzisieren Sie die Anfrage und prüfen Sie die Quellseite.
- **Entfernung scheint wirkungslos:** Starten Sie eine neue Sitzung und prüfen Sie die aktive Serverliste.

## Nächste Schritte

**Fahren Sie mit [KI-Ausgaben prüfen](/articles/effective-ai-output-verification/) fort.** Weitere Erweiterungen beschreibt der [Leitfaden der Website zu Claude-Code-Plugins und MCP-Werkzeugen](/articles/claude-code-plugins-skills-mcp-tools/).

**Kursnavigation:** [Zurück: Kontextverwaltung](/articles/effective-ai-context-window-management/), [Kursübersicht](/effective-ai-course-start/).
