---
title: "Claude Cowork und Claude Code mit lokalen Modellen: Einrichtungsleitfaden 2026"
date: 2026-09-22
lastmod: 2026-11-09
toc: true
draft: false
description: "Richte Ollama mit Claude Desktop und Claude Code über eine Anthropic-kompatible API ein. Erfahre mehr über Modellauswahl und Cloud-Funktionen im Jahr 2026."
genre: ["Lokale KI", "KI-Programmierwerkzeuge", "Selbst gehostete KI", "Entwicklerwerkzeuge", "Datenschutz", "Open-Source-Modelle", "Automatisierung", "KI-Hardware"]
tags: ["claude cowork", "claude code", "lokale claude desktop modelle", "ollama claude code", "anthropic base url", "anthropic_auth_token", "claude code lokales modell", "claude offline ausführen", "lokaler KI-programmieragent", "ollama launch claude", "claude desktop ollama", "lokales llm-programmieren", "privates KI-programmieren", "offline KI-programmieren", "lokaler KI-agent", "qwen3.8", "glm-cloudmodell", "modelle mit toolaufrufen", "claude code einrichten", "kostenloses claude code", "claude ohne API-schlüssel", "kontextfenster lokales modell", "llama.cpp", "ollama cloud", "datenschutz beim KI-programmieren", "air-gapped KI", "devops-KI-werkzeuge"]
cover: "/img/cover/claude-cowork-setup-guide-local-models-2026.webp"
coverAlt: "Ein moderner Arbeitsplatz mit einem Computer, der eine Programmieroberfläche zeigt, dazu ein Tablet und intelligente Lautsprecher vor dunkelblauem Hintergrund mit farbigen Leuchteffekten."
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Die Agentenwerkzeuge von Claude laufen jetzt mit Modellen auf deiner eigenen Hardware, ohne API-Schlüssel, Abonnement oder Daten, die deinen Rechner verlassen.** Ollama stellt eine Anthropic-kompatible API bereit, mit der sich Claude Code und Claude Desktop über wenige Befehle verbinden.

*Viele Anleitungen übersehen ein wichtiges Detail. Sie beschreiben Claude Cowork und geben anschließend Schritte, die das Befehlszeilenwerkzeug einrichten. Das sind zwei unterschiedliche Integrationen, und nur eine davon bietet Cowork.*

Dieser Leitfaden behandelt beide Wege getrennt, erklärt die Umgebungsvariable, die in beliebten Anleitungen fehlt, zeigt passende Modelle für beide Wege im September 2026 und nennt Funktionen, die unabhängig von der Konfiguration nur in der Cloud verfügbar bleiben.

**Nach dem Lesen:** weißt du, welche Integration du brauchst, verbindest sie über den dokumentierten Ollama-Weg und prüfst den Endpunkt mit einem Toolaufruf-Test. Lokale Inferenz hält Modellanfragen nur dann lokal, wenn du ein lokales Modell auswählst und Cloud-Funktionen vermeidest.

## Die kurze Antwort

**Ollama verbindet sich auf zwei verschiedene Arten mit Claude. Die falsche Auswahl ist der häufigste Grund dafür, dass nach einer Anleitung zwar das Terminal funktioniert, Cowork aber fehlt.**

| Integration | Funktionen | Einrichtungsweg | Plattform |
|---|---|---|---|
| **Claude Desktop** | Cowork, Subagenten, Websuche, Automatikmodus | Ollama-App, dann **Apps** und **Connect Claude** | **Nur macOS** |
| **Claude Code** | Der CLI-Programmieragent mit Toolaufrufen und Dateibearbeitung | `ollama launch claude` oder Umgebungsvariablen | macOS, Linux, Windows |

**Wenn du Cowork möchtest, verwende die Claude-Desktop-Integration.** Sie läuft über eine grafische Oberfläche in der Ollama-App und ist nur für macOS verfügbar. Die Windows-Unterstützung wird noch als geplant geführt.

**Wenn du einen Agenten im Terminal willst, verwende Claude Code.** Ein Befehl genügt.

*Beides ist kostenlos. Kosten entstehen nur für Hardware und Strom.*

## Zwei Integrationen, nicht eine

Die Verwirrung beginnt mit den Namen. **Claude Cowork ist eine Funktion in Claude Desktop**, keine eigenständige Anwendung und kein Synonym für Claude Code.

Die Ollama-Dokumentation führt beide auf getrennten Seiten und unter getrennten Überschriften auf. Claude Desktop steht unter **Assistants**, neben OpenClaw und Hermes. Claude Code steht unter **Coding**, neben OpenCode, Cline und Codex CLI.

Das ist wichtig, denn die Einrichtung unterscheidet sich vollständig:

- **Claude Desktop** richtest du in der Ollama-Anwendung ein. Du musst kein Shell-Profil ändern.
- **Claude Code** richtest du über Umgebungsvariablen oder einen einzigen Startbefehl ein.

Eine Anleitung, die dich `ANTHROPIC_BASE_URL` exportieren und dann `claude` ausführen lässt, richtet das Befehlszeilenwerkzeug ein. Hast du nach diesen Schritten die Cowork-Desktopoberfläche erwartet, **ist nichts an deiner Einrichtung kaputt. Du hast ein anderes Produkt eingerichtet.**

## Claude Desktop und Cowork einrichten

Für diesen Weg verwendest du die Ollama-Anwendung statt des Terminals.

### Voraussetzungen

- **Ollama installiert**, unter macOS. Windows-Unterstützung wird als geplant geführt.
- **Ein Modell vorher herunterladen**, wenn du lokal arbeiten willst. Für ein Cloudmodell meldest du dich bei Ollama an und aktivierst Cloudmodelle. Einige benötigen einen kostenpflichtigen Tarif.
- **Claude installiert.** Fehlt die Anwendung, bietet Ollama an, sie während der Einrichtung herunterzuladen.

### Schritte

1. Öffne Ollama und wähle **Apps**.
2. Wähle **Connect Claude**.
3. Folge den Einrichtungshinweisen. Installiere Claude, wenn du dazu aufgefordert wirst, und starte die Anwendung auf Nachfrage neu.

Das war der gesamte Ablauf. Um später das Modell zu ändern, öffne **Ollama Settings**, gehe zu **Apps**, wähle deine Modelle und klicke auf **Restart Claude**.

### Unterstützte Funktionen

Die Ollama-Dokumentation nennt vier Funktionen, die über diese Integration unterstützt werden:

- **Cowork**, für schwierige Aufgaben
- **Subagenten**, um größere Aufgaben auf mehrere Agenten aufzuteilen
- **Websuche**, standardmäßig über Ollama bereitgestellt
- **Automatikmodus**, bei dem der Agent entscheidet, wann er vor Änderungen nachfragt

*Cowork steht in dieser Liste. Über diese Integration ist es verfügbar, über die Befehlszeilenintegration dagegen nicht.*

### Verbindung trennen

Beim Trennen wird Claudes vorherige Konfiguration wiederhergestellt. Die Änderung ist also nicht destruktiv.

- Öffne in der Oberfläche **Apps**, trenne Claude und starte Claude neu, wenn du dazu aufgefordert wirst.
- Führe im Terminal `ollama launch claude-desktop --restore` aus.
- **Wenn du Ollama beendest, während Claude verbunden ist, wird Claudes übliche Konfiguration ebenfalls wiederhergestellt.** Soll die lokale Einrichtung bestehen bleiben, lass Ollama geöffnet.

{{< figure src="claude-desktop-ollama-integration-flow.webp" alt="Diagramm der Ollama-App, die über das Apps-Menü eine Verbindung zu Claude Desktop herstellt, mit Modellauswahl in den Ollama-Einstellungen und einem Weg zurück zur ursprünglichen Konfiguration" >}}

## Claude Code über die CLI einrichten

Dieser Weg wird in fast jeder Anleitung beschrieben und ist für die Arbeit im Terminal der richtige.

### Methode mit einem Befehl

```bash
ollama launch claude
```

Der Befehl setzt die erforderlichen Umgebungsvariablen, verweist Claude Code auf deine lokale Ollama-Instanz und startet das Programm. Wähle ein Modell aus der Liste und drücke Enter. Um das Modell vorher festzulegen, ergänze die Option:

```bash
ollama launch claude --model qwen3.5
```

*Der Wrapper richtet die Umgebung ein. Lies trotzdem den nächsten Abschnitt, denn mit diesem Wissen kannst du Fehler später leichter beheben.*

### Umgebungsvariablen manuell setzen

```bash
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://localhost:11434

claude --model qwen3.5
```

**Die zweite Zeile fehlt in beliebten Anleitungen.** Wenn du `ANTHROPIC_API_KEY` auf eine leere Zeichenfolge setzt, verhinderst du, dass ein bereits in deiner Umgebung vorhandener echter Schlüssel die lokale Verbindung stört. Lässt eine veröffentlichte Anleitung diese Zeile aus, erhalten Leser mit einem bereits exportierten Schlüssel eine verwirrende Fehlermeldung.

Um das Shell-Profil nicht zu ändern, übergib alle Werte direkt im Befehl:

```bash
ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_API_KEY="" claude --model kimi-k2.7-code:cloud
```

Zwei Details aus der offiziellen Dokumentation:

- **`ANTHROPIC_AUTH_TOKEN` enthält die Bearer-Authentifizierung.** Deshalb steht im lokalen Modus der wörtliche Wert `ollama` darin.
- **Claudes eigene Einstellungsdateien haben Vorrang vor Shell-Variablen.** Wenn die Verbindung nach dem Export neuer Werte seltsam reagiert, prüfe diese Einstellungen und führe danach in Claude Code `/status` aus. Dort siehst du den verwendeten Endpunkt.

### Direkt mit Ollama Cloud verbinden

Für diesen Weg musst du Ollama nicht installieren. Setze einen API-Schlüssel und verweise Claude Code auf den gehosteten Ollama-Endpunkt:

```bash
ANTHROPIC_BASE_URL=https://ollama.com \
ANTHROPIC_AUTH_TOKEN="$OLLAMA_API_KEY" \
ANTHROPIC_API_KEY="" \
claude --model glm-5.3-flash
```

**Dieser Weg hat eine Einschränkung.** Laut Ollama-Dokumentation werden gehostete Websuche und erweiterte Werkzeugsteuerung nicht vollständig unterstützt. Einfacher Chat, Dateibearbeitung und Toolaufrufe funktionieren mit kompatiblen Modellen.

## Modellauswahl für September 2026

Das Modellangebot hat sich 2026 stark verändert. Empfehlungen aus dem Frühjahr solltest du erneut prüfen.

| Modell | Typ | Kontext | Grund für die Auswahl |
|---|---|---|---|
| **Qwen3.8 27B** | Lokal, 18 GB | 256K | Derzeit bestes lokales Allroundmodell mit Bildverarbeitung, Toolaufrufen und einstellbarem Denkmodus |
| **Qwen3 Coder Next** | Lokal, MoE 80B gesamt / 3B aktiv | 256K | Für ständig laufende Programmieragenten entwickelt, schneller Modus ohne Denkprozess |
| **Qwen3.6 35B A3B** | Lokal, MoE 35B / 3B aktiv | 262K | Apache 2.0 und effizient bei wenig Speicher |
| **kimi-k2.7-code:cloud** | Cloud | Groß | Cloudmodell für Programmieraufgaben ohne lokale Hardwareanforderungen |
| **glm-5.3-flash** | Cloud | Groß | Das Modell, das die Ollama-Dokumentation zuerst nennt |

**Beginne mit Qwen3.8 27B, wenn du genug Speicher hast.** Das Modell läuft lokal mit einem Kontextfenster von 256K, nativer Bildverarbeitung, Toolaufrufen und einem Denkmodus, den du pro Anfrage umschalten kannst. Auf einer Karte mit mindestens 24 GB eignet es sich gut für den Alltag.

**Beginne mit einem Cloudmodell, wenn du diesen Speicher nicht hast.** Claude Code mit einem gehosteten Modell zu verbinden, kostet beim Ausprobieren nichts und macht die Hardwarefrage überflüssig. Dafür verlässt dein Code den Rechner.

### Warnung vor ternären Modellen

In unserem **[Leitfaden für lokale KI](/articles/local-ai-2026-build-your-rig-now/)** steht, dass das ternäre Bonsai 2 27B ein vollständiges 27B-Modell mit **5,53 GiB** ausführt. Das klingt auch hier verlockend.

**Mit diesem Ablauf funktioniert es nicht.** Die ternären Kernel befinden sich im llama.cpp-Fork von Prism ML, und das normale Ollama kann diese Dateien nicht laden. Ein Befehl wie `ollama launch claude --model Ternary-Bonsai-2-27B` schlägt fehl, bevor die Inferenz beginnt. Verwende für Claude Code das normale Qwen3.8-27B-Paket und reserviere ternäre Pakete für eine Laufzeitumgebung, die sie unterstützt.

*Komfort und maximale Effizienz führen hier zu unterschiedlichen Entscheidungen. Die integrierten Werkzeuge benötigen ein normales GGUF.*

## Stelle den Kontext auf 64K ein, bevor du dem Modell die Schuld gibst

Die Ollama-Dokumentation enthält einen direkten Hinweis zur Arbeit in Repositories: Wähle ein Modell und **stelle das Kontextfenster auf mindestens 64K ein**. Für größere Repositories solltest du den Wert weiter erhöhen.

Claude Code lädt Dateiinhalte, Unterschiede und Befehlsausgaben in das Kontextfenster. Bei einem kleinen Standardwert reicht der Platz mitten in einer Aufgabe nicht mehr. Das sieht nach einem Denkproblem aus, liegt aber an der Einstellung.

| Kontext | Geeignet für |
|---|---|
| Unter 32K | Einzelne Dateien bearbeiten und kurze Fragen |
| **64K** | Arbeit mit mehreren Dateien in einem kleineren Repository |
| 128K | Größere Repositories und lange Befehlsausgaben |
| 256K | Das gesamte Fenster von Qwen3.8 27B |

*Wenn Claude Code mitten in einer Aufgabe den Zusammenhang verliert, prüfe die Kontexteinstellung, bevor du das Modell wechselst.*

## Toolaufrufe mit einem Befehl prüfen

Toolaufrufe unterscheiden einen Agenten von einem Textgenerator. Prüfe, ob sie tatsächlich funktionieren.

Frage Claude Code nach dem Start:

```text
Read the current directory and list all files
```

**Wenn echte Dateien aufgelistet werden, funktionieren die Toolaufrufe.** Antwortet das Modell, es würde das Verzeichnis lesen, und beschreibt, was dort wohl liegt, ist die Funktion nicht verbunden. Du sprichst mit einem Chatmodell, das einen Programmierprompt erhalten hat, nicht mit einem Agenten. Weitere Prompts beheben das nicht.

Gehe die möglichen Ursachen in dieser Reihenfolge durch:

1. **Wechsle zu einem Modell mit bestätigter Toolunterstützung.** Nicht jedes Modell unterstützt sie, und die Parameterzahl verrät den Unterschied nicht.
2. **Prüfe, ob die Umgebung auf Ollama verweist.** Führe `ollama --version` aus und prüfe, ob `ANTHROPIC_BASE_URL` auf deinen lokalen Endpunkt verweist.
3. **Führe `/status` in Claude Code aus.** Eine Basis-URL oder ein Zugangsschlüssel in Claudes Einstellungsdateien hat Vorrang vor den gerade exportierten Shell-Variablen.

## Was nur in der Cloud verfügbar ist

Kenne diese Grenze, bevor du einen Ablauf rund um lokale Inferenz einrichtest.

| Funktion | Lokale Modelle | Cloud |
|---|---|---|
| Chat und Dateibearbeitung | Ja | Ja |
| Toolaufrufe | Modellabhängig | Ja |
| Subagenten | Ja | Ja |
| Websuche | Über Ollama bereitgestellt | Ja |
| **Cowork** | Über die Claude-Desktop-Integration | Ja |
| Automatikmodus | Über die Claude-Desktop-Integration | Ja |
| Geplante Prompts | Über `/loop` in Claude Code | Ja |

Drei Einschränkungen gelten für die lokale Nutzung:

- **Das Denken über mehrere Dateien verschlechtert sich früher als die Geschwindigkeit.** Ein lokales Modell bearbeitet eine Datei gut, drei Dateien akzeptabel und ein ganzes Repository schlecht. Plane die Aufgabengröße entsprechend.
- **Einige Cloudmodelle benötigen einen kostenpflichtigen Ollama-Tarif.** Außerdem musst du angemeldet sein und sie aktiviert haben.
- **Der direkte Cloudweg hat Funktionsgrenzen.** Ohne lokale Installation werden gehostete Websuche und erweiterte Werkzeugsteuerung nicht vollständig unterstützt.

*Lokale Inferenz eignet sich gut für klar abgegrenzte, überprüfbare Aufgaben und weniger für große, unklare Vorhaben. Richte deine Planung an dieser Grenze aus.*

## Automatisieren

Zwei Funktionen machen mehr aus der Einrichtung als nur eine interaktive Nutzung.

### Headless-Ausführung für Skripte und CI

Die Option `--yes` überspringt interaktive Auswahlen und lädt das Modell bei Bedarf herunter. Sie benötigt `--model`. Alles nach `--` geht direkt an Claude Code:

```bash
ollama launch claude --model gemma4:cloud --yes -- -p "how does this repository work?"
```

**Achte auf das Berechtigungsmodell.** Claude Code fragt vor den meisten Aktionen nach. Eine Headless-Ausführung braucht daher eingerichtete Berechtigungsregeln oder eine isolierte Umgebung. Richte einen unbeaufsichtigten Agenten nicht auf ein Repository, das dir wichtig ist.

### Geplante Prompts mit `/loop`

In einer Claude-Code-Sitzung führt `/loop` einen Prompt oder Slash-Befehl in einem festgelegten Intervall aus:

```text
/loop 30m Check my open PRs and summarize their status
/loop 1h Research the latest AI news and summarize key developments
/loop 15m Check for new GitHub issues and triage by priority
```

*Das läuft, solange die Sitzung geöffnet ist. Es ist kein Hintergrunddienst und endet mit der Sitzung.*

## Fehlerbehebung

| Symptom | Wahrscheinliche Ursache | Lösung |
|---|---|---|
| **Verbindung verweigert** | Ollama läuft nicht | Führe `ollama serve` aus und prüfe mit `curl http://localhost:11434/api/tags` |
| **Das Modell beschreibt Aktionen, statt sie auszuführen** | Das ausgewählte Modell unterstützt keine Toolaufrufe | Wechsle zu einem Modell mit bestätigter Toolunterstützung |
| **Ein echter API-Schlüssel wird statt des lokalen Endpunkts verwendet** | `ANTHROPIC_API_KEY` ist noch exportiert | Setze ihn wie oben gezeigt auf eine leere Zeichenfolge |
| **Cowork fehlt nach der Einrichtung** | Die Claude-Code-CLI wurde statt Claude Desktop konfiguriert | Verwende für Cowork den Ollama-Ablauf unter **Apps** |
| **Die Generierung ist langsam** | Der Kontext ist zu groß oder ein dichtes Modell wurde gewählt, obwohl ein sparsames reicht | Senke den Kontext und probiere danach ein Mixture-of-Experts-Modell |
| **Exportierte Variablen haben keine Wirkung** | Claudes Einstellungsdateien haben Vorrang vor Shell-Variablen | Prüfe die Einstellungsdateien und führe anschließend `/status` aus |
| **Hintergrundanfragen scheitern** | Claude Code verwendet für interne Aufgaben ein kleines Modell | Setze die Überschreibung für kleine Modelle auf dasselbe lokale Modell |

*Zwei dieser sieben Probleme haben dieselbe Ursache. Die meisten Einrichtungsfehler entstehen durch einen falschen Endpunkt oder ein Modell ohne Toolaufrufe.*

## Wichtigste Punkte

- **Claude Desktop und Claude Code sind getrennte Integrationen.** Cowork gehört zu Claude Desktop und wird unter macOS im Ollama-Menü **Apps** eingerichtet. Der CLI-Weg bietet kein Cowork.
- **Ein Befehl startet den CLI-Weg:** `ollama launch claude`. Für die manuelle Einrichtung brauchst du drei Variablen, und **viele Anleitungen lassen `ANTHROPIC_API_KEY=""` aus**.
- **Eine lokale Installation ist nicht erforderlich.** Verweise Claude Code mit einem API-Schlüssel auf `https://ollama.com`.
- **Stelle den Kontext auf mindestens 64K ein, bevor du ein Modell bewertest.** Ein kleines Fenster wirkt wie ein Denkfehler.
- **Prüfe Toolaufrufe mit einer Anfrage.** Beschreibt das Modell nur, was es tun würde, verwendest du einen Textgenerator statt eines Agenten.
- **Ternäre Bonsai-Pakete funktionieren hier nicht.** Sie benötigen den llama.cpp-Fork von Prism ML, den normales Ollama nicht laden kann.
- **Trennen ist sicher.** Beim Beenden von Ollama wird Claudes vorherige Konfiguration wiederhergestellt. Im Terminal kannst du auch `ollama launch claude-desktop --restore` ausführen.

## Nächste Schritte

1. **Installiere Ollama und lade ein Modell mit bestätigter Toolunterstützung herunter**, bevor du Claude einrichtest: **[Ollama-Modellbibliothek](https://ollama.com/library)**
2. **Lies Ollamas Seite zu Claude Code**, um aktuelle Optionen und Modelle zu sehen: **[Claude-Code-Integration](https://docs.ollama.com/integrations/claude-code)**
3. **Wenn du Cowork brauchst, nutze die Seite für Claude Desktop:** **[Claude-Desktop-Integration](https://docs.ollama.com/integrations/claude-desktop)**
4. **Lege die Hardware vor dem Kauf fest**, anhand der Speicherkategorien in unserem Leitfaden für lokale Inferenz: **[Lokale KI 2026: Ein 27B-Modell übertrifft Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)**
5. **Prüfe die Möglichkeiten kleinerer Hardware**, wenn du einen ständig verfügbaren Agenten auf einem sparsamen Gerät willst: **[Welche KI-Modelle laufen auf einem Raspberry Pi 4 oder 5?](/articles/ai-models-raspberry-pi-4-5/)**

## Verwandte Artikel

| Artikel | Inhalt |
|---|---|
| **[Lokale KI 2026: Ein 27B-Modell übertrifft Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/)** | Benchmark zur lokalen Inferenz, ternäre Quantisierung und Hardwareauswahl |
| **[Welche KI-Modelle laufen auf einem Raspberry Pi 4 oder 5?](/articles/ai-models-raspberry-pi-4-5/)** | Lokale Inferenz für einen kleinen, ständig verfügbaren Assistenten |
| **[Einen datenschutzfreundlichen KI-Assistenten für Meshtastic bauen](/articles/building-a-privacy-preserving-meshtastic-ai-assistant/)** | Ein lokales Modell für Funk ohne Internetverbindung, bei dem Datenschutz im Mittelpunkt steht |
| **[Beste VS-Code-Erweiterungen für KI-Entwicklung](/articles/best-visual-studio-code-extensions-for-ai/)** | Editierwerkzeuge für einen lokalen Programmieragenten |

## Quellen

1. [Claude-Code-Integration - Ollama-Dokumentation](https://docs.ollama.com/integrations/claude-code)
2. [Claude-Desktop-Integration - Ollama-Dokumentation](https://docs.ollama.com/integrations/claude-desktop)
3. [Ollama-Modellbibliothek](https://ollama.com/library)
4. [Qwen3.8 - Ollama-Modellbibliothek](https://ollama.com/library/qwen3.8)
5. [Claude Cowork mit lokalen Modellen - PromptSpace](https://www.promptspace.in/blog/how-to-use-claude-cowork-with-local-models-2026-guide)
6. [Prism-ML-Fork von llama.cpp - ternäre Kernel](https://github.com/PrismML-Eng/llama.cpp)
