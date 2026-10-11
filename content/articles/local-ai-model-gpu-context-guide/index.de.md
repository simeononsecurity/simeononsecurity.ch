---
title: "Welches lokale KI-Modell solltest du ausführen? Ein GPU-, Kontext- und Coding-Leitfaden für Oktober 2026"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Ein praktischer Leitfaden für Oktober 2026 zur Auswahl lokaler KI-Modelle für Coding-Agenten. Vergleiche GPU-Speicher, KV-Cache-Wachstum, Kontextgröße, Quantisierungsqualität, Prompt-Verarbeitung, Reasoning-Einstellungen und Cloud-Mietkosten."
genre: ["Lokale KI", "KI-Hardware", "Selbst gehostete KI", "GPU-Benchmarking", "Entwicklerwerkzeuge", "KI-Ökonomie"]
tags: ["lokale KI-Modelle", "Coding-Agenten", "GPU-Leitfaden", "VRAM", "KV-Cache", "Kontextfenster", "Qwen 27B", "Mixture of Experts", "Quantisierung", "llama.cpp", "Ollama", "spekulative Dekodierung", "Multi-Token-Prognose", "lokales LLM", "GPU-Miete", "KI-Workstation", "Agent-Coding", "Prompt-Verarbeitung", "Inferenzgeschwindigkeit"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Eine Workstation mit lokalen KI-Modellen, GPU-Speichernutzung und Kontextfenstern für Coding-Agenten"
coverCaption: ""
ref: ["/articles/32gb-vram-qwen-27b-hardware-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark", "/articles/local-ai-2026-build-your-rig-now"]
---

**Das beste lokale Coding-Modell ist das Modell, das genug von deinem Projekt im Speicher hält und schnell genug liest, um nützlich zu bleiben.** Die Modellgröße zählt weiterhin. Ein Modell, das erst nach dem Auslagern in den Systemspeicher passt, fühlt sich oft schlechter an als ein kleineres Modell mit stabilem Kontextfenster.

*Wähle Modell und Speicherbudget gemeinsam. Nimm kein Modell aus einer Rangliste und zwinge es auf ungeeignete Hardware.*

Dieser Leitfaden behandelt Coding-Agenten, keine kurzen Autocomplete-Prompts. Ein Agent liest Dateien, Tool-Ausgaben, Compilerfehler und Testergebnisse, bevor er eine Lösung schreibt. Diese Eingaben verbrauchen Kontext und verändern die Hardwareentscheidung.

## Das Video dient als Referenz

Das folgende Video vergleicht lokale Modelle über mehrere GPU-Speicherklassen hinweg. Es ist nützlich für praktische Hinweise zur Modellauswahl und gemeldete Hardwareergebnisse. Dieser Artikel verfolgt einen eigenen Ansatz und ordnet die Entscheidung nach Speicherverhalten, Agent-Kontext, Prompt-Verarbeitung und Gesamtkosten.

{{< youtube id="C9M6iUFtVB4" enable="true" title="I Tested Every Local AI Model So You Don't Have To" description="Praktischer Vergleich lokaler KI-Modelle über mehrere GPU-Speicherklassen hinweg, mit Blick auf Coding-Workloads und Hardwaregrenzen." >}}

## Warum Ranglisten scheitern

Eine Modellrangliste ordnet meist die Parameterzahl einer GPU-Speichergröße zu. Für eine erste Schätzung ist dieser Ansatz nützlich. Sobald ein Coding-Agent ein echtes Repository liest, reicht er nicht mehr.

Die Modellgewichte sind die erste Speicherbelegung. Der **KV-Cache** wächst mit. Er speichert Attention-Schlüssel und -Werte des aktiven Kontexts, damit die Laufzeit nicht nach jedem generierten Token den gesamten Prompt neu berechnen muss.

| Speicherverbraucher | Inhalt | Warum es zählt |
|---|---|---|
| **Modellgewichte** | Quantisierte Parameter | Einmaliger Ladebedarf |
| **KV-Cache** | Notizen aus dem aktiven Kontext | Wächst mit Prompt und Unterhaltung |
| **Laufzeitpuffer** | Temporärer Rechenraum | Hängt von Backend und Batchgröße ab |
| **Agent-Anweisungen** | System-Prompts und Tooldefinitionen | Verbrauchen Kontext vor den Projektdateien |

**Ein passendes Modellfile beweist noch keinen brauchbaren Agenten.** Die Laufzeit braucht Platz für Cache, temporäre Puffer, Tooldefinitionen und die nächste Antwort.

## Der Kontext ist das echte Budget

Coding-Agenten verbrauchen Kontext für mehr als Quelldateien. Dazu gehören Systemanweisungen, Tool-Schemata, Verzeichnislisten, Shell-Ausgaben, Compilermeldungen, Testergebnisse und frühere Gesprächsrunden.

Drei MCP-Verbindungen mit ausführlichen Tooldefinitionen verbrauchen oft mehrere tausend Tokens, bevor der Agent eine Projektdatei öffnet. Ein kleiner Standardkontext lässt wenig Platz für Code. Der Agent antwortet weiterhin, verliert aber den Arbeitsbestand für Reparaturen über mehrere Schritte.

Die [Ollama-Laufzeit-FAQ](https://docs.ollama.com/faq) nennt einen Standardkontext von 4.096 Tokens. `OLLAMA_CONTEXT_LENGTH` ändert den Standardwert. `OLLAMA_NUM_PARALLEL` skaliert den benötigten Speicher mit der Zahl paralleler Anfragen. Notiere beide Werte, bevor du einen lokalen Benchmark mit einem Ergebnis für eine einzelne Anfrage vergleichst.

```bash
OLLAMA_CONTEXT_LENGTH=32768 OLLAMA_NUM_PARALLEL=1 ollama serve
```

Dieses Beispiel setzt für eine aktive Anfrage einen Standardwert von 32K. Es reserviert keine 32K Tokens für Projektdateien. Anweisungen, Tooldefinitionen, Eingabe und Ausgabe teilen sich das Fenster.

### Ein einfacher Kontextdatensatz

Notiere vor dem GPU-Vergleich diese Werte:

- **Projektgröße:** Dateien und ungefähre Quellzeilen in einer normalen Aufgabe.
- **Tool-Overhead:** System-Prompt, MCP-Schemata, Shell-Tools und Editoranweisungen.
- **Fehlerpayload:** Übliche Länge von Compiler- und Testausgaben.
- **Zielkontext:** Der größte Prompt, den du ohne Kürzung behalten willst.
- **Antwortreserve:** Platz für den geplanten Patch und seine Erklärung.

Verwende das Ergebnis als Workload-Spezifikation. Ein Entwickler, der jeweils eine Datei ändert, benötigt anderen Speicher als jemand, der einen Agenten eine API durch ein Monorepo verfolgen lässt.

## Der KV-Cache verändert die Rangfolge

Zwei Modelle mit ähnlicher Parameterzahl haben oft unterschiedliche Kontextkosten. Ein dichtes Modell, bei dem jede Schicht zum wachsenden Cache beiträgt, braucht mehr Speicher als ein Modell mit hybrider Attention-Architektur.

Ein im Referenzmaterial besprochenes 27B-Coding-Modell nutzt wenige Schichten mit vollständiger Attention. Andere Schichten verwenden eine Zusammenfassung fester Größe. Die gemeldeten Kosten für 128K Kontext bleiben für den Cache unter 9GB. Ein ähnlich großes Modell mit vollständig wachsender Attention in jeder Schicht benötigt bei gleicher Kontextlänge laut Bericht mehr als 21GB.

Diese Zahlen gelten für bestimmte Modellarchitekturen und Laufzeiteinstellungen. Nutze sie als Grund, die Architektur zu prüfen, nicht als allgemeine Speicherformel.

| Modellverhalten | Kontexteffekt | Folge für die Hardware |
|---|---|---|
| **Vollständige Attention in jeder Schicht** | Starkes Cache-Wachstum | Mehr Speicher für lange Prompts nötig |
| **Hybride oder gleitende Attention** | Geringeres Cache-Wachstum in einigen Schichten | Mehr Kontextreserve bei gleicher Modellgröße |
| **Mixture of Experts** | Weniger aktive Parameter pro Token | Weniger Rechenarbeit pro Token, aber alle Gewichte müssen gespeichert werden |
| **Erweiterung für langen Kontext** | Größeres Arbeitsfenster | Mehr Cache-Speicher und mehr Prompt-Verarbeitung |

**Lies die Modellarchitektur vor dem Speicherkauf.** Die Parameterzahl allein verbirgt die Kosten einer langen Coding-Sitzung.

## Wähle nach der GPU-Speicherklasse

### Vier bis acht GB

Kleine dichte Modelle bleiben die praktische Wahl. Sie passen auf die Karte, antworten schnell und eignen sich für Autocomplete, kurze Erklärungen und begrenzte Dateiänderungen.

Ein größeres Modell mit CPU-Offload erzeugt zwar Text, doch die Antwortzeit wird oft zum Engpass. Ein Coding-Agent braucht wiederholte Dateizugriffe und Toolaufrufe. Ein Setup mit vier Tokens pro Sekunde macht jede Reparatur zu einer langen Wartezeit, selbst wenn das Modell technisch läuft.

Mixture-of-Experts-Modelle bieten einen weiteren Weg. Ein kleiner aktiver Teil senkt den Rechenaufwand, während der vollständige Gewichtssatz teilweise im Systemspeicher liegt. Dafür braucht das System viel RAM und schnelle Übertragungswege.

| Workload | Empfohlene Richtung |
|---|---|
| **Autocomplete** | Kleines dichtes Modell mit kurzem Prompt |
| **Änderungen an einer Datei** | Kleines Instruct-Modell mit Tool-Unterstützung |
| **Repositoryweiter Agent** | Erst eine größere GPU mieten oder Systemspeicher erhöhen |
| **Privater Code unter NDA** | Lokales Modell nutzen, aber kleineren Umfang oder langsamere Läufe akzeptieren |

**In dieser Klasse kaufst du zuerst Systemspeicher, bevor du ein großes Modell verfolgst.** Ein stabiles kleines Modell ist besser als ein großes Modell, das die meiste Zeit Daten über den Bus verschiebt.

### Zwölf bis sechzehn GB

Diese Klasse ermöglicht ein 27B-Coding-Modell, doch die Quantisierungswahl wird zentral. Ein standardmäßiger 4-Bit-Build mit etwa 17GB passt mit Laufzeit-Overhead nicht auf eine 16GB-Karte.

Ein 3-Bit-Build mit etwa 13GB lässt mehr Platz für Kontext. Eine 12GB-Karte drängt zu einem 2-Bit-Build oder einem kleineren Mixture-of-Experts-Modell. Die Qualität hängt vom konkreten Quantisierer und Kalibrierungsprozess ab. Zwei Uploads mit derselben Bitbreite liefern daher oft unterschiedliche Coding-Ergebnisse.

Prüfe vor dem Download eines quantisierten Modells:

- **Autor des Quantisierers und Versionshinweise**
- **Kalibrierungsdaten und Auswertungsergebnisse**
- **Tokenizer-Kompatibilität**
- **Tests für Tool-Aufrufe**
- **Kontextlänge bei der gewählten Quantisierung**
- **Laufzeitunterstützung in Ollama, llama.cpp oder dem gewählten Frontend**

**„2-bit“ oder „3-bit“ beschreibt die Qualität nicht vollständig.** Packmethode und Kalibrierungsprotokoll zählen.

### Vierundzwanzig bis zweiunddreißig GB

Dieser Bereich ist für ein 27B-Coding-Modell am flexibelsten. Eine 24GB-Karte nimmt oft einen 4-Bit-Build mit brauchbarem Kontext auf, doch ein vollständiges 128K-Fenster kann den verbleibenden Speicher überschreiten. Eine 32GB-Karte lässt der Laufzeit mehr Platz für Cache und temporäre Belegungen.

Dieser Bereich erleichtert auch die Begründung für eigene Hardware. Eine GPU erledigt die Aufgabe ohne die Komplexität eines Zwei-Karten-Splits. Das System verbraucht weniger Strom als ein Multi-GPU-Aufbau, und die Softwareunterstützung lässt sich leichter testen.

| Kapazität | Praktische Position |
|---|---|
| **24GB** | Starkes 4-Bit-Modell mit messbaren Kontextgrenzen |
| **32GB** | 4- oder 6-Bit-27B-Modell mit größerer Kontextreserve |
| **48GB** | Höhere Präzision oder größerer Cache ohne Wechsel des Kernmodells |

**24GB bis 32GB ist der sinnvolle Bereich für eigene Hardware bei regelmäßiger privater Coding-Arbeit.** Er vermeidet schwaches Offload-Verhalten, ohne Rechenzentrumshardware in ein Desktopgehäuse zu zwingen.

### Achtundvierzig GB und mehr

Mehr Speicher bedeutet nicht automatisch ein neues Modell. Dasselbe 27B-Modell läuft auf einer 48GB-Karte eventuell mit 8-Bit-Präzision, größerem Cache und weniger Kompromissen. Der Gewinn liegt in Konsistenz, Kontextplatz und Ausgabequalität, nicht in einer neuen Reasoning-Stufe.

Bei 128GB ändert sich die Entscheidung. Ein deutlich größeres Mixture-of-Experts-Modell wird möglich, aber die Prompt-Verarbeitung wird kritisch. Ein Modell generiert oft schnell, braucht aber lange, um ein großes Repository oder ein frisches Tool-Ergebnis einzulesen.

**Bei großen Modellen misst du Prefill- und Decode-Geschwindigkeit getrennt.** Eine schnelle Antwort nach langsamem Prompt-Lesen fühlt sich im Agent-Workflow weiterhin langsam an.

## Decode-Geschwindigkeit ist nur die halbe Prüfung

**Decode-Geschwindigkeit** misst erzeugte Tokens pro Sekunde. Sie beantwortet: „Wie schnell schreibt das Modell?“ **Prefill-Geschwindigkeit** misst die Prompt-Verarbeitung. Sie beantwortet: „Wie schnell liest das Modell?“

Ein Agent verbringt viel Zeit mit Lesen. Jeder Toolaufruf fügt neuen Text hinzu. Eine lange Quelldatei, ein Stacktrace oder ein Testprotokoll kommt in den Prompt, bevor die nächste Antwort beginnt.

| Metrik | Nutzererlebnis |
|---|---|
| **Decode-Tokens pro Sekunde** | Wie schnell die Antwort nach der Verarbeitung erscheint |
| **Prompt-Tokens pro Sekunde** | Wie lange der Agent vor dem Antwortbeginn wartet |
| **Zeit bis zum ersten Token** | Gemeinsame Verzögerung durch Prompt-Verarbeitung und Einrichtung |
| **Kontexterhalt** | Wie viel Projektzustand während der Aufgabe verfügbar bleibt |

**Benchmarke deine eigenen Promptgrößen.** Ein kurzer synthetischer Prompt verbirgt die Kosten, die bei Repository-Arbeit am wichtigsten sind.

## Zuerst kostenlose Laufzeiteinstellungen

Hardware-Upgrades sind nicht der erste Performance-Schritt. Teste Laufzeiteinstellungen, bevor du eine Kaufseite öffnest.

### Multi-Token-Prognose

Einige Modell- und Backend-Kombinationen unterstützen die Prognose mehrerer zukünftiger Tokens und prüfen sie in einem Durchlauf. Die Funktion erscheint oft als Laufzeitflag oder kompatible Draft-Konfiguration.

Gemeldete Tests aus dem Referenzmaterial zeigen auf einigen High-End-Karten große Gewinne. Die Ergebnisse hängen von Modellfile, Backend, Treiber und Karte ab. Apple-Metal-Pfade behalten die erforderliche Funktion bei der Konvertierung eventuell nicht.

### Reasoning-Stufe

Ein Modell mit maximal aktiviertem Reasoning verbringt vor der Rückgabe mehr Zeit mit interner Arbeit. Mittleres Reasoning bietet für Code-Reparaturen oft das bessere Gleichgewicht, besonders bei klarer Fehlermeldung und engem Dateiziel.

Verwende eine einfache Testmatrix:

1. Führe dieselbe Fehlerbehebungsaufgabe mit niedrigem, mittlerem und hohem Reasoning aus.
2. Zeichne Zeit bis zum ersten Token, Gesamtzeit, Patch-Erfolg und Testergebnis auf.
3. Wiederhole den Test mit einem kurzen Prompt und einem Prompt in Repository-Größe.
4. Behalte die Einstellung mit der besten abgeschlossenen Aufgabe, nicht mit der höchsten Tokenrate.

**Mittleres Reasoning mit einem kompatiblen Multi-Token-Pfad ist ein guter Startpunkt.** Prüfe die Qualität an deinem eigenen Code, bevor du es zum Standard machst.

## Lokale Hardware oder Miet-GPU?

Miet-Compute gewinnt bei gelegentlicher Arbeit. Du zahlst für aktive Sitzungen, statt eine Karte zu kaufen, zu kühlen, zu aktualisieren und ganzjährig zu betreiben.

Eigene Hardware gewinnt bei häufiger, privater oder offline ausgeführter Arbeit. Sie entfernt außerdem Warteschlangen und bietet eine stabile Umgebung für wiederholbare Tests.

| Situation | Bester erster Schritt |
|---|---|
| **Einige Sitzungen pro Monat** | GPU mieten oder eine API nutzen |
| **Tägliches privates Coding** | Unterstütztes 24GB- bis 32GB-System kaufen |
| **Großes Repository mit häufigem Neuladen** | Zuerst mieten und Prefill-Geschwindigkeit messen |
| **Code verlässt das Gebäude nicht** | Das kleinste System kaufen, das das Kontextziel erfüllt |
| **Neues Modell testen** | Vor dem Hardwarekauf mieten |

Berechne den Break-even mit aktiven Stunden, nicht mit Kalenderstunden. Berücksichtige Strom, Speicher, Kühlung, Wartung und den Zeitaufwand für eine funktionierende Laufzeit.

**Eine High-End-GPU für gelegentliche Experimente ist eine Hobbyausgabe.** Ein täglich für private Arbeit verwendetes 24GB- bis 32GB-System hat die stärkere wirtschaftliche Begründung.

## Eine bessere Kaufliste

Nutze diese Reihenfolge beim Vergleich von Modell und GPU:

1. **Definiere die Aufgabe.** Autocomplete, Reparatur einer Datei, Repository-Agent oder Analyse mit langem Kontext.
2. **Miss den Prompt.** Zähle normale Systemanweisungen, Tool-Schemata, Dateien und Testausgaben.
3. **Prüfe das Cache-Verhalten.** Suche Architekturhinweise und Messungen zum Kontextspeicher.
4. **Wähle eine Quantisierung.** Prüfe Qualitätsdaten des konkreten Uploads, nicht nur die Bitzahl.
5. **Teste Prefill und Decode.** Nutze Prompts aus deinem eigenen Repository.
6. **Stimme Reasoning ab.** Vergleiche die Zeit für eine abgeschlossene Aufgabe bei mehreren Reasoning-Stufen.
7. **Teste Datenschutz und Wartung.** Prüfe, wohin Quellcode fließt und wer das Backend betreut.
8. **Vergleiche Mietkosten.** Nutze erwartete aktive Stunden und nimm Strom in die Schätzung eigener Hardware auf.

## Abschließende Empfehlung

**Unter 12GB führst du ein kleineres Modell oder ein Mixture-of-Experts-Modell mit genug Systemspeicher aus.** Zwinge kein dichtes 27B-Modell in ein Setup, das die meiste Zeit auslagert.

**Bei 12GB bis 16GB konzentrierst du dich auf Quantisierungsqualität und ein kontrolliertes Kontextziel.** Ein gut getesteter 2- oder 3-Bit-Build mit Tool-Unterstützung ist nützlicher als ein 4-Bit-File, das nie sauber passt.

**Bei 24GB bis 32GB wird ein 27B-Coding-Modell zur praktischen Standardwahl für tägliche private Arbeit.** Miss Kontextverbrauch und Prompt-Geschwindigkeit, bevor du das vollständige beworbene Fenster voraussetzt.

**Ab 48GB verwendest du den zusätzlichen Speicher zuerst für Präzision, Cache-Platz und stabile Sitzungen, bevor du zu einem größeren Modell wechselst.** Sobald das Modell in den 128GB-Bereich kommt, verdienen Prompt-Lesegeschwindigkeit und Mietökonomie mehr Aufmerksamkeit als die Rohkapazität.

Der Modellname ist nur der Anfang. Die nützliche Frage lautet, wie viel Projektkontext bleibt, nachdem Modell, Laufzeit, Tools und Cache ihren Anteil genommen haben.

## Weiterführende Lektüre

- [32GB VRAM für Qwen 27B: Leitfaden für lokale KI-Hardware](/articles/32gb-vram-qwen-27b-hardware-guide/), mit Hardwarewegen für eine 27B-Workload.
- [Llama 3.1 8B- und Qwen3.8 27B-GPU-Benchmarks auf Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/), gemessene Miet-GPU-Ergebnisse und Grenzen bei langem Kontext.
- [Lokale KI 2026: Ein 27B-Modell schlägt Sonnet 4.6](/articles/local-ai-2026-build-your-rig-now/), Modellqualität, Quantisierung und Wirtschaftlichkeit lokaler Hardware.
