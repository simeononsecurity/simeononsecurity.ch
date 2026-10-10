---
title: "10 Claude-Code-Plugins, Skills und MCP-Tools: Ein praktischer Leitfaden"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Wähle Claude-Code-Erweiterungen für Planung, Code-Review, Wissensmanagement, Design und Automatisierung. Vergleiche zehn Tools, Abhängigkeiten und praktische Prüfungen."
genre: ["Künstliche Intelligenz", "Entwickler-Tools", "Softwareentwicklung"]
tags: ["Claude-Code-Plugins", "Claude-Code-Skills", "MCP-Tools", "Graphify", "grill-me", "grill-with-docs", "grill-me-codex", "Claudex Loop", "Codex-Plugin", "Code-Review", "claude-obsidian", "Obsidian", "CLAUDE.md", "Karpathy-Richtlinien", "Impeccable", "Higgsfield", "NotebookLM", "notebooklm-py", "n8n MCP", "KI-Entwicklungsworkflow", "Agentenanweisungen", "Wissensgraphen"]
cover: "/img/cover/claude-code-plugins-workflow-management-tools.webp"
coverAlt: "Blaue und violette Tool-Symbole, Ordner und abstrakte Diagrammflächen, verbunden mit einem zentralen geometrischen Knoten auf dunklem Hintergrund"
coverCaption: "Konzeptionelle Darstellung eines Workflows. Die Diagrammformen zeigen keine gemessenen Ergebnisse."
---

**Wähle eine Claude-Code-Erweiterung für einen konkreten Fehler in deinem Workflow.** Unklare Anforderungen brauchen ein Planungsgespräch. Übersehene Fehler brauchen Review und Tests. Wiederholte Recherche braucht nachvollziehbare Quellen. Mehr Tools helfen nur bei klaren Zuständigkeiten.

Dieser Leitfaden vergleicht **zehn Projekte** für diese Aufgaben. Er enthält Einrichtungsbeispiele und eine praktische Bewertungsübung. Die Analyse stützt sich auf aktuelle Projektdokumentation und das bereitgestellte Chase-AI-Video. Die Empfehlungen sind redaktionelle Einschätzungen, keine praktischen Leistungsmessungen und kein Beleg für eine zehnfache Produktivitätssteigerung.

<!--more-->

## Die wichtigsten Punkte

- **Nach dem Ergebnis wählen:** Ein geprüftes Konzept, eine Codekarte und ein erzeugtes Bild brauchen unterschiedliche Tools.
- **Installationsschichten trennen:** Anweisungen, ausführbare Programme, Plugins und Serviceverbindungen haben unterschiedliche Abhängigkeiten.
- **Aktuelle Namen prüfen:** Graphify und grill-me-codex liegen inzwischen an verschiedenen kanonischen Repository-Orten.
- **Über Zustimmung hinaus prüfen:** Wenn zwei Modelle einem Plan zustimmen, beweist das keine korrekte Umsetzung.
- **Angenommene Arbeit messen:** Erfasse Setup, Servicenutzung, Fehlversuche und menschliche Korrekturen.

## Vor dem Start

**Voraussetzungen:** eine funktionierende Claude-Code-Installation, ein wegwerfbares Projekt oder ein temporärer Branch sowie die Erlaubnis für die ausgewählten externen Dienste. CLI-Beispiele setzen ein Terminal und den genannten Paketmanager voraus. Cloud-Integrationen brauchen eigene Konten und Authentifizierung.

**Geschätzte Zeit:** 15 Minuten zum Lesen, danach 30 bis 60 Minuten für einen begrenzten Versuch. **Schwierigkeit:** mittel für CLI-Setup und Serviceintegration. Das Lesen von Instruction-Skills braucht weniger Setup.

**Dokumentation geprüft am 10. Oktober 2026.** Befehle und Zugriffsregeln folgen den verlinkten Quellen. Prüfe deine installierte Version erneut, bevor du einem älteren Tutorial folgst. Dieser Artikel behandelt Erweiterungen aus Claude Code und nennt Host-Unterschiede, wenn sie relevant sind.

**Nach der Installation schichtweise prüfen.** Prüfe Dateien, Host-Erkennung, ausführbare Abhängigkeiten, Zugangsdaten und eine repräsentative Aufgabe getrennt. Ein erfolgreicher Installer beweist nicht, dass Browser, MCP-Server, Medientool oder externes Konto funktionieren. Führe den ersten Test mit synthetischen Daten aus und notiere die Upstream-Revision.

## Erweiterungstypen verstehen

| Typ | Rolle | Beispiel |
|---|---|---|
| **Anweisungsdatei** | Setzt dauerhafte Projekterwartungen | CLAUDE.md |
| **Skill** | Liefert ein Verfahren für eine Aufgabe | grill-me |
| **Plugin** | Bündelt registrierte Befehle und Integrationen | Codex-Plugin |
| **CLI** | Führt Befehle im Terminal aus | Graphify |
| **MCP-Server** | Stellt einem Agent-Client aufrufbare Tools bereit | n8n-Integration |

Das **Model Context Protocol (MCP)** verbindet eine Agent-Anwendung mit den von einem Server bereitgestellten Tools und Daten. Eine **Command-Line-Schnittstelle (CLI)** führt ausführbare Befehle aus. Ein Skill zeigt dem Agenten oft die Nutzung einer Schnittstelle, aber sein Vorhandensein beweist keine funktionierende Verbindung.

**Beginne mit der fehlenden Fähigkeit.** Hat dein Agent bereits Repository-Suche, braucht ein neues Suchverfahren einen beobachtbaren Nutzen. Fehlt der Zugriff auf eine Automatisierungsplattform, liefert eine reine Anweisungsdatei keinen authentifizierten Zugriff. Der breitere [Leitfaden zur Agent-Runtime](/articles/best-ai-agent-harnesses/) erklärt die Software rund um Modellaufrufe und Toolausführung.

## Das erste Tool wählen

| Problem | Tool | Erste Abnahmeprüfung |
|---|---|---|
| **Unklare Anforderungen** | grill-me / grill-with-docs | Explizite Entscheidungen und Abnahmekriterien |
| **Wiederholte Abweichung vom Umfang** | Karpathy-inspiriertes CLAUDE.md | Jede Änderung dient der angeforderten Änderung |
| **Riskanter Umsetzungsplan** | Claudex Loop | Review-Ergebnisse mit Belegen behoben |
| **Ungeprüfte Codeänderungen** | OpenAI-Codex-Plugin | Ergebnisse mit Code und Fehlerfällen verknüpft |
| **Unbekanntes Repository** | Graphify | Beziehungen stimmen mit Quelldateien überein |
| **Verstreutes Projektwissen** | claude-obsidian | Aussagen behalten Links zur ursprünglichen Evidenz |
| **Wiederholte Quellensynthese** | notebooklm-py | Antworten zitieren die vorgesehenen Quellen |
| **Verwirrende Oberfläche** | Impeccable | Nutzer schließen die vorgesehene Interaktion ab |
| **Fehlende visuelle Assets** | Higgsfield | Ergebnis passt zum freigegebenen Asset-Briefing |
| **Wiederholbarer Serviceworkflow** | n8n MCP | Testausführung erzeugt das erwartete Ergebnis |

**Empfohlener Start:** Wähle eine Zeile und speichere vor der Installation eine Baseline-Aufgabe. Füge ein zweites Tool nur bei einem separaten, messbaren Beitrag hinzu.

## Arbeit klären

### grill-me und grill-with-docs

**Die Skills von Matt Pocock** helfen, eine unklare Idee in Entscheidungen zu verwandeln. Der aktuelle [grill-me-Einstieg](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) ruft den gemeinsamen Grilling-Skill auf. [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) ruft Grilling und Domain Modeling auf. Die [Sammlungsdokumentation](https://github.com/mattpocock/skills) beschreibt gemeinsame Begriffe und Architekturentscheidungen.

**Nutze die Dokumentationsvariante**, wenn Geschäftsbegriffe die Umsetzung beeinflussen. Kläre bei einem beispielhaften CSV-Importer, ob ein vorhandener Kunde dieselbe E-Mail, dieselbe externe ID oder beides bedeutet. Halte die Definition vor dem Schreiben der Duplikaterkennung fest.

**Halte das Gespräch proportional.** Eine nützliche Sitzung löst wichtige Unsicherheit. Sie sollte keine im Repository vorhandenen Antworten wiederholen. Beende sie mit Plan, offenen Fragen und beobachtbaren Abschlussprüfungen.

### Karpathy-inspiriertes CLAUDE.md

**Die von Multica gepflegten Richtlinien** übertragen Karpathys Beobachtungen auf vier Themen: explizite Annahmen, einfache Lösungen, fokussierte Änderungen und überprüfbare Ziele. Das [Repository](https://github.com/multica-ai/andrej-karpathy-skills) ist eine von seinen Beobachtungen inspirierte Community-Implementierung. Es als persönlich von Karpathy gepflegtes Plugin zu bezeichnen, wäre eine falsche Herkunftsangabe.

**Übernimm nützliche Hinweise in die bestehende Projektpolitik.** Bewahre Build-Befehle, Content-Konventionen und Deployment-Grenzen. Eine Ersatzdatei, die diese Details entfernt, erzeugt neue Fehlerquellen.

**Beispiel für eine Projektregel:** Eine Änderung am Importer muss die bestehende Duplikatbehandlung bewahren und jede beabsichtigte Änderung mit einem Fixture erklären. So wird eine allgemeine Vorsicht zu einer für Reviewer verständlichen Prüfung. Anweisungen formulieren Erwartungen. Tests und Laufzeitkontrollen liefern getrennte Belege.

| Planungsartefakt | Zweck |
|---|---|
| **Anforderung** | Benennt das sichtbare Ergebnis |
| **Glossareintrag** | Gibt einem mehrdeutigen Begriff eine Bedeutung |
| **Entscheidungsprotokoll** | Bewahrt den Grund für eine wichtige Wahl |
| **Abnahmeprüfung** | Legt die Bewertung der Fertigstellung fest |

## Pläne und Code prüfen

### grill-me-codex, jetzt Claudex Loop

**Claudex Loop** ist das aktuelle Ziel des ursprünglichen grill-me-codex-Repositories. Die [Dokumentation](https://github.com/chaseai-yt/claudex-loop) beschreibt Repository-Erkundung, Anforderungen, Review durch den anderen Anbieter, Umsetzung und unabhängige Prüfung. Der vollständige Ablauf braucht beide CLIs und Python 3.10 oder neuer.

**Nutze Claudex Loop für folgenreiche Pläne**, deren Annahmen vor der Umsetzung geprüft werden sollen. Der aktuelle Workflow startet mit Claude Code oder Codex. Er zeichnet Befunde und Entscheidungen auf und trennt Review-Erlaubnis von Bau-Erlaubnis. Die ältere Beschreibung mit fünf Runden im Video ersetzt nicht das Budget des installierten Workflows.

**Fordere zu jedem Einwand Belege.** Bei einem CSV-Importer muss ein Review einen konkreten Duplikat- oder Wiederholungsfall und das erwartete Verhalten nennen. Modellübereinstimmung ist ein Review-Ergebnis, kein Beweis. Bewahre offene Befunde am Ende des Review-Budgets auf.

### OpenAI-Codex-Plugin

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

**OpenAIs Codex-Plugin für Claude Code** ergänzt Code-Review und Aufgabenübergabe in Claude Code. Das sind Claude-Code-Befehle, keine Shell-Befehle. Das [offizielle Repository](https://github.com/openai/codex-plugin-cc) dokumentiert Node.js 18.18 oder neuer und authentifizierten Codex-Zugriff über ChatGPT oder einen OpenAI-API-Key.

```text
/codex:review --background
/codex:status
/codex:result
```

**Nutze normales Review** für aktuelle Änderungen oder einen Branch-Vergleich. **`/codex:adversarial-review`** dient einer fokussierten Gegenprüfung. Delegationsbefehle wie **`/codex:rescue`** erledigen eine andere Aufgabe als ein Nur-Lese-Review. Benenne daher die vorgesehene Berechtigung.

**Plane Codex-Nutzung separat.** Das Projekt nennt ChatGPT Free als unterstütztes Konto, doch Nutzungslimits gelten weiter. Die Installation erzeugt keinen unbegrenzten Zugriff.

**Auswahlregel:** Nutze ein begrenztes Plugin-Review für einen vorhandenen Patch. Wähle den größeren Ablauf, wenn Anforderungen und Planrevision einen eigenen dokumentierten Prozess brauchen.

## Nützlichen Kontext bewahren

### Graphify

```bash
uv tool install graphifyy
graphify install --project
graphify extract . --code-only
graphify query "show the authentication flow"
```

**Graphify** bildet Repository-Beziehungen in einen abfragbaren Wissensgraphen ab. Das [kanonische Repository](https://github.com/Graphify-Labs/graphify) liegt jetzt unter Graphify-Labs. Der Paketname lautet **`graphifyy`** mit zwei y am Ende. Das ausführbare Programm heißt weiter **`graphify`**.

**Code-only-Extraktion** nutzt lokale Abstract-Syntax-Tree-Analyse und liest die Code-Struktur. Dokument- und Medieninterpretation nutzt einen separaten modellgestützten Weg. Übertrage die Aussagen zu lokaler Privatsphäre und lokalen Kosten nicht auf jeden Modus.

**Optionale Hooks** bauen den Codegraphen nach Commits und Branchwechseln neu. Nach Pull oder Merge verlangt der dokumentierte Ablauf **`graphify update .`**. Dokumentänderungen brauchen eine eigene Aktualisierung. Der Obsidian-Export bietet eine weitere Sicht auf den Graphen.

**Nutze Graphify für Beziehungsfragen** und prüfe anschließend die relevante Quelle. Ein Graph hilft bei der Dateiauswahl. Seine Struktur beweist kein Laufzeitverhalten und ersetzt keine Tests. Miss mögliche Token-Einsparungen mit deinen Fragen und rechne Aufbau sowie Pflege des Graphen ein.

### claude-obsidian

**claude-obsidian** organisiert Quellen in verknüpften, quellenzitierten Obsidian-Seiten. Das [Repository](https://github.com/AgriciDaniel/claude-obsidian) beschreibt Aufnahme, Abruf, Wissenspflege, Quellenerhalt und Belege für Unterstützung oder Widerspruch. Der Vault bleibt eine Sammlung normaler lokaler Dateien.

**Nutze claude-obsidian für dauerhaftes Projektwissen:** Designentscheidungen, Quelldokumente und Forschungsnotizen, die einzelne Gespräche überdauern sollen. Das nützliche Ergebnis ist ein wartbares Protokoll mit Herkunft, also einer nachvollziehbaren Quelle für jede wichtige Aussage.

**Prüfe den Vault nach der Aufnahme.** Wähle Aussagen und folge den Zitaten zum Originalmaterial. Bewahre widersprüchliche Evidenz, statt sie zu einer sicheren Zusammenfassung zu verschmelzen. Lokaler Speicher beweist keine lokale Inferenz. Prüfe Host- und Modellkonfiguration vor der Weitergabe sensibler Dokumente.

| Kontextsysten | Beste erste Frage |
|---|---|
| **Graphify** | Welche Quellkomponenten sind verbunden? |
| **claude-obsidian** | Welche bewahrte Evidenz stützt diese Entscheidung? |
| **notebooklm-py** | Was sagen die gewählten Forschungsquellen? |

### notebooklm-py

```bash
uv tool install "notebooklm-py[browser]"
notebooklm login
notebooklm auth check --test --json
notebooklm skill install
```

**notebooklm-py** liefert Python-Bibliothek, CLI und Agent-Skill für Googles Notebook-Recherche. Das [Projekt](https://github.com/teng-lin/notebooklm-py) dokumentiert Quellenimport, quellenbasierte Fragen, erzeugte Artefakte und Batch-Downloads. Das Browser-Extra unterstützt den interaktiven Login.

**Diese Integration ist nicht offiziell.** Die Bibliothek nutzt undokumentierte Google-Schnittstellen und bleibt anfällig für Brüche und Ratelimits. Stelle sie nicht als öffentlich unterstützte Google-API dar.

**Nutze notebooklm-py für ein begrenztes Forschungskorpus**, etwa Release Notes und Migrationsanleitungen einer Abhängigkeit. Prüfe Zitate am Quelltext, bevor du Ergebnisse in einen Plan übernimmst. Schütze gespeicherte Authentifizierungsdaten als Kontozugangsmaterial.

**Rechercheauslagerung verlagert den Ausführungsort.** Sie beseitigt weder Orchestrierungstokens, Servicequoten, Reviewaufwand noch Pflichten zum Umgang mit Daten. Behandle Tokenersparnis als Messwert, nicht als automatische Eigenschaft der Installation.

## Assets gestalten und erzeugen

### Impeccable

```text
/impeccable critique settings
/impeccable audit settings
/impeccable polish settings
```

**Impeccable** liefert ein Designvokabular für fokussierte Interface-Arbeit. Die [Dokumentation](https://github.com/pbakaus/impeccable) behandelt Kritik, Layout, Typografie, Barrierefreiheit, Bewegung und visuelle Browser-Iteration. Die Beispiele setzen einen installierten Skill und ein Projekt mit Einstellungsoberfläche voraus.

**Beginne mit einem Interaktionsproblem.** Frage beim Importer, warum Nutzer Validierungsfehler übersehen oder die Duplikatoption missverstehen. Prüfe Änderungen vor einem visuellen Feinschliff. Guter Abstand allein behebt keine unklare Aktion.

**Live-Iteration** hilft beim Vergleich im Browser. Prüfe Tastaturnavigation, Mobil-Layout, Fehlermeldungen und Kontrast. Die Zahl der Befehle ändert sich zwischen Releases. Nutze daher die Liste deiner installierten Version statt die Anzahl aus dem Video.

### Higgsfield

**Higgsfields MCP-Integration** verbindet Agents mit einem Bild- und Videogenerierungsdienst. Die [offizielle Integrationsseite](https://higgsfield.ai/mcp) listet Claude Code und CLI-Verbindungsoptionen. Nutze den aktuellen Ablauf für dein Konto und die gewählte Schnittstelle.

**Wähle Higgsfield, wenn ein Medien-Asset fehlt.** Für eine illustrative Produktseite beschreibe Seitenverhältnis, Komposition, Markenregeln und Platzierung vor der Varianten-Erzeugung. Halte das visuelle Briefing von der Seitenimplementierung getrennt.

**Prüfe zuerst Dienstzugang und Verbrauch.** Ein Integrationseintrag beweist weder Zugriff auf alle Modelle noch unbegrenzte Erzeugung oder ein bestimmtes kommerzielles Nutzungsrecht. Lies Kontobedingungen und gewähltes Modell vor einem Produktionsworkflow.

**Prüfe die fertige Datei** in der vorgesehenen Größe. Kontrolliere sichtbaren Text, unerwünschte Symbole, Zuschnitt und Produktkonsistenz. Erzeugte Terminalbilder und Diagramme sind kein Beleg für einen erfolgreichen Test.

| Design-Lieferobjekt | Abschlussbeleg |
|---|---|
| **Interface-Revision** | Benötigte Aktionen funktionieren in den Zielansichten |
| **Bild-Asset** | Größe, Zuschnitt und Inhalt entsprechen dem Briefing |
| **Video-Asset** | Timing, Bewegung und Export entsprechen dem Briefing |

## Wiederholbare Workflows verbinden

### n8n MCP

**n8ns eingebauter MCP-Server** stellt verbundenen Clients Workflow-Operationen bereit. Die [aktuelle Verbindungsdokumentation](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) behandelt Cloud- und selbstgehostete Instanzen. Workflow-Bau und -Bearbeitung sind ab n8n 2.13.0 dokumentiert. Dieser Artikel meint n8ns eigenen Server, kein unabhängiges Community-Paket mit ähnlichem Namen.

**Nutze den Instanzzugriff** für diese Integration. Der MCP-Server-Trigger-Knoten hat einen anderen Umfang und stellt Tools aus einem Workflow bereit. Vergleiche die [Toolreferenz](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) mit deiner bereitgestellten Version.

**Aktiviere Zugriff bewusst.** Vorhandene Workflows brauchen MCP-Exposition für vollständigen Zugriff. Suchvorschauen haben im Rahmen der bestehenden Nutzerrechte mehr Sichtbarkeit. Workflow-Exposition ist keine eigene Allowlist pro Client, doch Client-Berechtigungen steuern Vorgänge ebenfalls.

**Prüfe den Ausführungsmodus.** **`execute_workflow`** startet laut Dokumentation standardmäßig die veröffentlichte Produktionsversion. Der manuelle Modus startet die aktuelle unveröffentlichte Version. Prüfe Eingaben und Folgeschritte vor dem Start.

**Ein nützlicher erster Versuch:** Klassifiziere synthetische Supportanfragen und schreibe die Ergebnisse in ein Testziel. Prüfe fehlende Felder und Wiederholungen. Selbsthosting braucht weiterhin Rechenleistung, Pflege und eventuell kostenpflichtige Folgedienste.

## Einen kontrollierten Versuch durchführen

**Beispielübung:** Füge einer kleinen Anwendung einen CSV-Importer hinzu. Er zeigt Zeilen vorab an, meldet ungültige E-Mail-Felder und verhindert doppelte Erstellung. Kundendaten und aktive externe Ziele sind nicht nötig.

```yaml
# Evaluation worksheet, not a tool configuration file
task: "add CSV import preview"
inputs:
  - "valid rows"
  - "invalid email field"
  - "repeated customer identifier"
  - "same import submitted twice"
acceptance:
  - "preview creates no records"
  - "invalid rows receive useful messages"
  - "duplicate policy matches the written requirement"
  - "repeat submission creates no extra records"
record:
  - "source revision and selected skill version"
  - "model and service configuration"
  - "elapsed time and billed usage"
  - "failed checks and human corrections"
```

**Lege zuerst die Baseline fest.** Speichere die Ausgangsrevision und lass den Agenten die Aufgabe mit deinem bisherigen Workflow lösen. Führe unabhängige Abnahmeprüfungen aus und bewahre das Ergebnis. Wiederhole es aus derselben Revision mit einer Erweiterung und denselben Anforderungen.

**Passe das Experiment an das vermutete Problem an.** Bei wiederholt falsch verstandener Duplikatbehandlung teste einen Anforderungsskill. Wenn ein vorhandener Validator übersehen wird, teste Repository-Mapping. Wenn Nutzer Fehler übersehen, teste Interface-Kritik. Alle zehn Tools zusammen verhindern eine Zuordnung des Nutzens.

**Erwartete Schlussfolgerung:** Ein erfolgreicher zweiter Versuch ist nützliches Indiz, doch ein Lauf beweist keinen allgemeinen Produktivitätsfaktor. Wiederholte Läufe trennen Toolwert von Modellschwankungen. Vergleiche angenommene Ergebnisse inklusive Reviewaufwand und Fehlversuchen.

| Beobachtung | Interpretation |
|---|---|
| **Schnellere Antwort, fehlgeschlagene Tests** | Kürzere Antwortzeit ohne abgeschlossene Aufgabe |
| **Längerer Lauf, weniger Korrekturen** | Möglicher Nutzen beim gesamten Lieferaufwand |
| **Zwei zustimmende Reviewer** | Zustimmung braucht unabhängige Prüfung |
| **Geringere Agentennutzung, neue Servicekosten** | Kosten wurden zwischen Anbietern verschoben |

**Erstelle ein dauerhaftes Entscheidungsprotokoll.** Benenne Problem, gewähltes Tool, beobachteten Nutzen, offene Frage und Bedingungen für einen weiteren Versuch. Behalte ein Tool, wenn sein Beitrag diese Prüfung besteht. Eine große installierte Sammlung verlangt keinen großen aktiven Workflow.

## Fehlerbehebung

| Symptom | Nächste Prüfung |
|---|---|
| **Skill vorhanden, Befehl scheitert** | Installation des Executables, PATH und benötigte Zusatzdateien |
| **Alte Tutorialnamen liefern keine Befehle** | Installierte Version und kanonische Upstream-Anweisungen |
| **Graph enthält neue Änderungen nicht** | Aktualität des Graphen und separate Dokumentaktualisierung |
| **Reviewer wiederholt gelöste Einwände** | Exakte Planrevision, Beleg und Reviewbudget |
| **Notebook-Authentifizierung scheitert** | Auth-Diagnose, Sitzungsstatus und Upstream-Probleme |
| **n8n-Verbindung bietet erwartete Vorgänge nicht** | Bereitgestellte Version, Exposition und Berechtigungen |
| **Design sieht besser aus, funktioniert aber schlechter** | Ursprüngliche Abnahmekriterien und Interaktionsprüfungen |

**Prüfe Installationsschichten der Reihe nach:** Dateien vorhanden, Host erkannt, Abhängigkeiten bereit, Authentifizierung erfolgreich und repräsentative Aufgabe geprüft. Ein erfolgreicher Installer beweist nur einen Teil dieser Kette.

**Untersuche überschneidende Skills vor einer weiteren Kopie.** Anforderungsinterviews, Planungssuiten, Designtools und Reviewpakete haben manchmal widersprüchliche Defaults. Wähle ein Hauptverfahren und ergänze Tools nur für benannte Beiträge. Bewahre Repository-Regeln und den angeforderten Umfang.

## Videorundgang

{{< youtube id="IShdbDP4Jgg" enable="true" title="The Top 10 Claude Code Plugins to 10x Your Next Project (June '26)" >}}

**Der Rundgang von Chase AI** stellt die zehn hier besprochenen Projekte vor. [Sieh das Originalvideo](https://www.youtube.com/watch?v=IShdbDP4Jgg) für die Demonstrationen. Nutze die verlinkte Projektdokumentation für aktuelle Installation und Verhalten. Der Videotitel ist eine Werbeaussage, kein von diesem Leitfaden gemessenes Ergebnis.

## Nächste Schritte

**Wähle einen wiederkehrenden Fehler und eine Abnahmeprüfung.** Teste die passende Erweiterung in einem wegwerfbaren Projekt und behalte die kleinste Kombination, die das Ergebnis verbessert. Ergänze Wissensmanagement, Medienerzeugung oder Automatisierung nur bei Bedarf.

**Für verwandte Hinweise** lies beim Auswählen des Agents den [CLI-Vergleich von Coding-Agents](/articles/cli-coding-agents-comparison/). Nutze den [KI-Zusammenarbeitskurs](/ai-collaboration-course-start/) für praktische Arbeit an Anforderungen, Evidenz und Review-Verantwortung.

{{< centerbutton href="/ai-collaboration-course-start/" >}}
Den KI-Zusammenarbeitskurs lesen
{{< /centerbutton >}}

## Quellen

- [Graphify: Codegraphen und Installation](https://github.com/Graphify-Labs/graphify)
- [Matt Pocock: Skill-Sammlung](https://github.com/mattpocock/skills)
- [Claudex Loop: aktuelles grill-me-codex-Projekt](https://github.com/chaseai-yt/claudex-loop)
- [OpenAI: Codex-Plugin für Claude Code](https://github.com/openai/codex-plugin-cc)
- [claude-obsidian: quellengebundenes Wissensmanagement](https://github.com/AgriciDaniel/claude-obsidian)
- [Multica: von Karpathy inspirierte Coding-Richtlinien](https://github.com/multica-ai/andrej-karpathy-skills)
- [Impeccable: Designbefehle und Installation](https://github.com/pbakaus/impeccable)
- [Higgsfield: Agent-Integration](https://higgsfield.ai/mcp)
- [notebooklm-py: inoffizielle Bibliothek, CLI und Skill](https://github.com/teng-lin/notebooklm-py)
- [n8n: offizieller MCP-Verbindungsleitfaden](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
