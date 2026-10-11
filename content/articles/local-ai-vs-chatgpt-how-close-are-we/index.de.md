---
title: "Lokale KI vs. ChatGPT: Wie nah sind wir wirklich?"
date: 2026-10-06
lastmod: 2026-10-10
toc: true
draft: false
description: "Vergleiche lokale KI mit ChatGPT und Claude anhand von Benchmarkwerten, Speicherschätzungen, Bereitstellungsgeschwindigkeit und Agentenprüfung. Mit Szenarien für RTX 5090, DGX Spark und Mac Studio."
genre: ["Lokale KI", "Künstliche Intelligenz", "KI-Hardware", "Entwicklerwerkzeuge"]
tags: ["lokale KI vs ChatGPT", "lokale KI vs Claude", "lokales LLM", "KI-Agenten", "offene Gewichte", "Qwen3.8 27B", "GLM-5.3", "GPT-6 Astra", "Claude Opus 5.5", "RTX 5090", "DGX Spark", "Mac Studio", "Quantisierung", "KV-Cache", "gemeinsamer Speicher", "VRAM", "Artificial Analysis", "Agentenprüfung", "lokale Inferenz", "hybride KI", "Coding-Agenten", "KI-Benchmarks"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Eine Desktop-Workstation ist über einen leuchtenden Pfad mit einer abstrakten Wolke aus Netzwerkpunkten vor dunklem Hintergrund verbunden"
coverCaption: "Konzeptionelle Darstellung lokaler und gehosteter KI."
---

**Lokale KI** eignet sich für begrenzte Aufgaben mit klaren Prüfungen. Um die Arbeit von ChatGPT oder Claude zu ersetzen, müssen Modellfähigkeit, nutzbarer Speicher und ein Agent zur Prüfung der Ausgabe zusammenpassen.

Ein passendes Modell braucht geeignete Werkzeuge und genügend Geschwindigkeit für wiederholte Versuche. Dieser Artikel trennt Benchmarkwerte, Speicherschätzungen und Nachweise abgeschlossener Aufgaben.

<!--more-->

## Die wichtigsten Punkte

- **Fähigkeit:** Referenzwerte gelten für bestimmte Prüfbedingungen, nicht für deinen quantisierten lokalen Build.
- **Speicher:** Plane Gewichte, Kontext-Cache und Laufzeitreserve gemeinsam.
- **Geschwindigkeit:** Das Wiederholen eines Agentengesprächs misst die Bereitstellung, nicht die Richtigkeit.
- **Prüfung:** Ein Agent braucht Prüfungen, die zum gewünschten Ergebnis passen.
- **Auswahl:** Vergleiche wiederholte Aufgaben, Reparaturzeit und Gesamtkosten vor dem Hardwarekauf.

## Werte im Kontext lesen

Der **Artificial Analysis Intelligence Index** fasst mehrere Tests zu einem Referenzwert zusammen. Die [Modellrangliste](https://artificialanalysis.ai/leaderboards/models) und lokale Hardwareergebnisse zeigen die am 6. Oktober 2026 geprüften Einträge.

| Modell und Einstellung | Indexwert | Einsatz in diesem Vergleich |
|---|---|---|
| **Qwen3.8 27B, xhigh** | 34 | Herunterladbare Gewichte |
| **GLM-5.3, max** | 45 | Herunterladbare Gewichte |
| **GPT-6 Astra, max** | 53 | Gehosteter Dienst |
| **Claude Opus 5.5, max mit Fallback** | 58 | Gehosteter Dienst |

**Indexpunkte** sind keine Prozente für Intelligenz oder Aufgabenerfolg. Ein Abstand von 13 Punkten zwischen GLM und Claude beweist keinen Unterschied von 13 Prozent bei deinen Programmierergebnissen. Auch die Denk-Einstellung beeinflusst den Vergleich.

Die [veröffentlichte Bewertungsmethode](https://artificialanalysis.ai/methodology/intelligence-benchmarking) beschreibt den Testaufbau. Einige Tests enthalten Werkzeuge und Agenteninfrastruktur. Übertrage den Wert nicht direkt auf eine komprimierte lokale Kopie in einer anderen Anwendung.

**ChatGPT und Claude sind Produkte**, diese Tabelle vergleicht ausgewählte Grundmodelle. Abonnement, Modell, Werkzeuge und Aufgabenkontext schaffen weitere Unterschiede. Teste zuerst eine wiederholte Aufgabe mit der vollständigen Einrichtung.

## Den gesamten Speicherbedarf planen

Die **Speicherplanung** beginnt mit drei Anteilen. Modellgewichte speichern gelernte Parameter. Der Key-Value-Cache, kurz **KV-Cache**, hält Aufmerksamkeitsdaten für die Inferenz. Laufzeitpuffer und Software verbrauchen den Rest.

```text
Benötigter Speicher = residente Gewichte + Kontext-Cache + Laufzeitreserve
Verfügbarer Speicher = physische Kapazität - Reserve für Betriebssystem und Anwendungen
```

**Quantisierung** senkt die Speicherpräzision der Gewichte. Niedrigere Präzision senkt den Bedarf, die Qualität hängt vom Modell und vom quantisierten Build ab. Cache-Präzision ist eine eigene Einstellung. Eine Q4-Datei beweist keinen Vier-Bit-Cache.

Bei 27 Milliarden Parametern benötigen 16 Bit ungefähr 50,3 GiB, 8 Bit ungefähr 25,1 GiB und 4 Bit ungefähr 12,6 GiB. **Veröffentlichte Dateigrößen** enthalten auch Metadaten, Packing und gemischte Präzision. Plane mit den tatsächlichen Dateien.

Die [Qwen3.8-27B-Modellkarte](https://huggingface.co/Qwen/Qwen3.8-27B) und die [GLM-5.3-Modellkarte](https://huggingface.co/zai-org/GLM-5.3) beschreiben unterschiedliche Architekturen. Ein **Mixture-of-Experts-Modell** aktiviert pro Token nur einen Teil seiner Parameter. Die übrigen Gewichte müssen trotzdem gespeichert werden. Offloading ändert Platzierung und Latenz, entfernt die Gewichte aber nicht.

## Mit veröffentlichten Dateien beginnen

Die **Downloadgröße** ist ein konkreterer Startpunkt als die Parameterzahl. Die veröffentlichten Qwen- und GLM-Builds von Unsloth zeigen die Wirkung der Quantisierung.

| Quantisierter Build | Veröffentlichte Größe, dezimale GB | Ungefähre GiB |
|---|---|---|
| **Qwen3.8 27B Q4_0** | 16.1 | 15.0 |
| **Qwen3.8 27B Q8_0** | 29.0 | 27.0 |
| **GLM-5.3 UD-Q4_K_XL** | 467 | 434.9 |
| **GLM-5.3 UD-IQ2_M** | 239 | 222.6 |

**Dateiquellen:** [Qwen Q4_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q4_0.gguf), [Qwen Q8_0](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-Q8_0.gguf), [GLM UD-Q4_K_XL-Segmente](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-Q4_K_XL) und [GLM UD-IQ2_M-Segmente](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main/UD-IQ2_M). Gerundete Werte vom 6. Oktober 2026. GiB teilt dezimale Bytes durch 2³⁰.

Dies sind **Gewichtsdateigrößen**, keine Messungen des gesamten residenten Speichers. Laden, Caches, temporäre Puffer und weitere Modellteile beeinflussen den Prozess. Vergleiche 29 GB nicht ohne Umrechnung mit einer 30-GiB-Zuweisung.

## Kontext verändert den Bedarf

Der **Qwen-Aufmerksamkeitscache** dient als Rechenbeispiel. Die [veröffentlichte Konfiguration](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/config.json) nennt 64 Schichten, vollständige Aufmerksamkeit in jeder vierten Schicht, vier Key-Value-Köpfe und eine Kopfdimension von 256.

```text
Vollständige KV-Bytes pro Token:
16 Schichten × 4 KV-Köpfe × 256 Dimensionen × 2 (K und V) × 2 Bytes
= 65.536 Bytes

8.192 Tokens  = 0,5 GiB
32.768 Tokens = 2,0 GiB
```

Diese **berechnete Cache-Komponente** setzt 16-Bit-Schlüssel und -Werte für eine Sequenz voraus. Linearer Zustand, Laufzeitpuffer, Allocator-Overhead und optionale Vision- oder spekulative Dekodierung fehlen. Dafür bleibt weiterhin Speicher nötig.

Für ein **beispielhaftes Planungsbudget** addiere 3–5 GiB für diese Reserven zu den gerundeten Gewichten. Ersetze die Annahme durch Messungen deiner Laufzeit.

| Build und Kontext | Berechnete Planungsspanne |
|---|---|
| **Qwen Q4_0, 8K** | 18.5–20.5 GiB |
| **Qwen Q8_0, 8K** | 30.5–32.5 GiB |
| **Qwen Q8_0, 32K** | 32.0–34.0 GiB |

Eine **nutzbare Zuweisung von 30 GiB** lässt beim Q4-Beispiel viel Kontextreserve. Die Q8-Szenarien überschreiten sie unter diesen Annahmen. Ein kurzer erfolgreicher Prompt beweist daher keine Kapazität für eine lange Codingsitzung.

**Gleichzeitige Anfragen** erhöhen den Bedarf. Ollama dokumentiert das Wachstum des Kontextspeichers bei parallelen Anfragen und separate Einstellungen für die Cache-Präzision. Q8 benötigt ungefähr die Hälfte des F16-Cache-Speichers, Q4 ungefähr ein Viertel. Die Qualitätsabweichung hängt vom Modell ab. Siehe die [Ollama-Laufzeit-FAQ](https://docs.ollama.com/faq).

## Hardware an die Zuweisung anpassen

Eine **RTX 5090** bietet 32 GB dedizierten Grafikspeicher. Ein DGX Spark mit 128 GB nutzt gemeinsamen Speicher. Artificial Analysis dokumentiert beide Konfigurationen. Mehr Kapazität erlaubt größere Zuweisungen, beweist aber keine Bereitstellungsgeschwindigkeit.

| Hardwareszenario | Praktische Folge |
|---|---|
| **RTX 5090, 32 GB** | Qwen Q4 lässt mehr Kontextreserve als Q8 |
| **DGX Spark, 128 GB** | Platz für beide Qwen-Builds, aber mit Laufzeitreserve |
| **Mac Studio, 256 GB** | Größere Gewichte sind Kandidaten, abhängig von Laufzeit und Zuweisung |

**GLM UD-Q4_K_XL** überschreitet alle drei Kapazitäten schon vor dem Cache. Auch der IQ2-Gewichtssatz mit etwa 222,6 GiB übersteigt ein 128-GB-System. Auf einem 256-GB-Mac hängt die Nutzbarkeit von GPU-Zuweisung und Restreserve ab. [Apples Spezifikationen](https://www.apple.com/mac-studio/specs/) garantieren keine Inferenzzuweisung.

Ein **hypothetisches nutzbares Budget von 240 GiB** lässt nach den IQ2-Gewichten etwa 17,4 GiB. Bei 192 GiB scheitert die Gewichtszuweisung allein. Keine der Zahlen beweist Betriebssystemreserve, komprimierten Cache, brauchbaren Durchsatz oder akzeptable IQ2-Qualität. Verlange vor dem Kauf eine nachgewiesene Laufzeitkonfiguration.

## Geschwindigkeit ist ein eigenes Ergebnis

Der **lokale Inferenzbenchmark von Artificial Analysis** wiederholt eine aufgezeichnete Last von 168 Modellrunden. Die [Laptop- und Workstation-Ergebnisse](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/) nennen folgende Zeiten für getestete Qwen3.8-27B-Konfigurationen.

| System | Zeit der Servicereproduktion |
|---|---|
| **DGX Spark, 128 GB** | 24,2 Minuten |
| **RTX 5090** | 4,9 Minuten |
| **Mac Studio, 256 GB** | In diesem Vergleich kein Ergebnis |

Das RTX-Ergebnis benötigt ungefähr ein Fünftel der Spark-Zeit. **Die Servingskonfiguration zählt**, daher ist dies kein allgemeines Hardwareverhältnis. Die getesteten Builds unterscheiden sich zudem von den GGUF-Planungsbeispielen.

Die **Reproduktionszeit** zählt Toolausführung nicht und erzwingt aufgezeichnete Antwortlängen. Sie bewertet nicht, ob die Antworten die ursprüngliche Aufgabe lösen. Ein MacBook-Messwert beweist auch keine Mac-Studio-Leistung.

## Dem Agenten Feedback geben

Ein **Agenten-Ausführungssystem** liefert Werkzeuge, Kontext, Aktionsschleife und Prüfung. Ein Modell schreibt oder wählt darin Aktionen. Für einen CSV-Export gehören Projektdateien lesen, Code ändern, Tests ausführen und Fehler empfangen zu den nützlichen Fähigkeiten.

Betrachte eine **beispielhafte Exportaufgabe**, kein gemessenes Experiment. Der Agent schreibt einen Download, nutzt aber das falsche Datumsformat. Eine Sichtprüfung verfehlt den Fehler. Ein Test öffnet die exportierte Datei und vergleicht die Daten mit dem geforderten Format. Der Agent erhält den Fehler, ändert den Formatierer und wiederholt die Prüfung.

| Fehlende Komponente | Wahrscheinlicher Fehler |
|---|---|
| **Relevanter Kontext** | Bearbeitet eine falsche Datei |
| **Ausführungswerkzeuge** | Beschreibt eine Lösung ohne sie anzuwenden |
| **Prüfschritt** | Stoppt nach plausibel wirkendem Code |
| **Fehlerfeedback** | Wiederholt einen fehlgeschlagenen Ansatz |

**LangChain berichtet** eine Änderung von 52,8 % auf 66,5 % bei Terminal Bench 2.0 mit festgehaltenem GPT-5.2-Codex. Der [Agentenbericht](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) beschreibt Prüfanweisungen, Umgebungskontext, Erkennung wiederholter Änderungen und Anpassungen des Denkbudgets.

Dies ist **anbieterberichtete Evidenz**, kein Beleg dafür, dass ein kleines lokales Modell ein Frontier-Modell erreicht. Die engere Folgerung lautet: Die Modellauswahl allein erklärt Agentenergebnisse nicht. LangChain berichtet auch schlechtere Ergebnisse bei dauerhaft maximalem Denken wegen Zeitüberschreitungen.

## Prüfungen an die Aufgabe anpassen

Eine **bestandene Prüfung** belegt nur ihren Abdeckungsbereich. Ein CSV-Test für Spaltennamen prüft weder Datumsformat, Anführungszeichen, Unicode noch Zugriffskontrolle. Definiere das gewünschte Ergebnis vor der Auswahl der Prüfung.

| Aufgabe | Nützlicher Abschlussnachweis |
|---|---|
| **Codeänderung** | Relevante Tests und Prüfung des resultierenden Verhaltens |
| **Rechercheantwort** | Quellen für einzelne Behauptungen |
| **Buchung oder Rückerstattung** | Korrekte gespeicherte Daten und passende Richtlinie |
| **Dokumentexport** | Geparste Ausgabe mit den verlangten Feldern und Formaten |

Die **τ-bench-Studie** bewertet Agenten, die mit Werkzeugen, Benutzern und Fachregeln arbeiten. Das [Forschungspapier](https://arxiv.org/abs/2406.12045) vergleicht den finalen Datenbankzustand mit dem erwarteten Ergebnis. Flüssiger Bestätigungstext reicht daher bei Transaktionen nicht aus.

## Lokal bedeutet nicht offline

**Lokale Inferenz** bestimmt den Ausführungsort des Modells. Die umgebende Anwendung bestimmt weiterhin, wohin Dokumente, Suchabfragen, Traces und Toolergebnisse gehen. Ein lokales Coding-Modell mit externer Suche oder Cloud-Werkzeugen ist ein vernetztes System.

Ollama erklärt, dass es bei lokaler Ausführung keine Prompts oder Antworten empfängt, und beschreibt das Abschalten der Cloud-Funktionen. Das ist eine **laufzeitspezifische Aussage**, keine Datenschutzgarantie für jeden verbundenen Agenten. Prüfe Endpunkt und Integrationen in der [Laufzeitdokumentation](https://docs.ollama.com/faq).

| Datenpfad | Was zu prüfen ist |
|---|---|
| **Inferenz-Endpunkt** | Lokaler Prozess, entfernter Server oder automatischer Fallback |
| **Suche und Abruf** | Extern gesendete Abfragen und Dokumentausschnitte |
| **Werkzeugverbindungen** | Dateien und Datensätze je Dienst |
| **Logs und Traces** | Speicherort, Aufbewahrung und Zugriff |

Ein **hybrider Ablauf** braucht eine klare Übergaberegel. Halte private Dokumentextraktion lokal und sende nur genehmigte Summen zur gehosteten Analyse. Prüfe die exakten ausgehenden Daten. Auch eine Zusammenfassung bleibt sensibel, wenn sie Namen, Kundendaten oder vertrauliche Ergebnisse enthält.

## Vor dem Kauf testen

**Wähle eine wiederholte Aufgabe** mit klarer Abschlussbedingung. Vergleiche die lokale Einrichtung mit deinem gehosteten Produkt samt Werkzeugen. Nutze dieselben Eingaben und Akzeptanzkriterien und wiederhole die Aufgabe mit mehreren Beispielen.

1. **Konfiguration erfassen:** Modell-Datei, Quantisierung, Backend-Version, Kontextlimit und Denk-Einstellung.
2. **Erfolg definieren:** erwartetes Artefakt, gefordertes Verhalten und verbotene Nebenwirkungen.
3. **Abschluss messen:** Zeit, bestandene Prüfungen, Fehlversuche und manuelle Reparaturen.
4. **Besitzkosten einbeziehen:** Hardware, Strom, API-Gebühren, Wartung und eigene Zeit.
5. **Fehler klassifizieren:** Denken, Speicher, Latenz, fehlender Kontext oder fehlende Prüfung.

**Lokale Inferenz** passt, wenn Qualität und Latenz deine Anforderungen erfüllen. Ein gehostetes Modell bleibt sinnvoll, wenn zusätzliche Fähigkeiten Fehler oder Prüfaufwand senken. Ein hybrider Ablauf verteilt Aufgaben nach einer klaren Datenfreigabe.

## Kosten pro akzeptiertem Ergebnis zählen

**Menschliche Reparaturzeit** verändert die Wirtschaftlichkeit. Eine schnelle lokale Antwort mit zehn Minuten Korrektur kostet mehr Arbeitszeit als eine langsame Antwort, die die Prüfung besteht. Zähle akzeptierte Ergebnisse neben den Inferenzkosten.

```text
Kosten pro akzeptierter Aufgabe =
(Hardwarezuweisung + Strom + Dienstgebühren + Wartung + Prüfzeit)
÷ akzeptierte Aufgaben
```

**Beispielhafte Prüfkosten:** Bei angenommenen 30 Dollar pro Stunde kosten acht Korrekturminuten 4 Dollar pro Aufgabe. Einhundert solcher Aufgaben verbrauchen 400 Dollar Prüfzeit. Dies sind Rechenbeispiele, keine gemessenen lokalen Fehlerraten.

**Vergleiche gleiche Ergebnisse.** Rechne abgelehnte Versuche in Zeit und Kosten ein. Verteile bei eigener Hardware den Kaufpreis auf eine realistische Nutzungsdauer und Aufgabenmenge. Bei einem gehosteten Dienst zählen Abonnement oder API-Kosten und die verbleibende Prüfzeit.

Für Hardwaredetails lies den [Leitfaden zu lokalen Modellen, GPUs und Kontext](/articles/local-ai-model-gpu-context-guide/). Für Kapazität und Preise lies den [DGX-Spark-Speichervergleich](/articles/dgx-spark-64gb-memory-crisis-2027/). Wähle anhand deiner Ergebnisse die kleinste passende Einrichtung.

## Referenzvideo

{{< youtube id="siZ3f_06k8M" enable="true" title="Lokale KI vs. ChatGPT: Wie nah sind wir wirklich?" description="Lokale und gehostete KI-Modelle, Speicherbedarf, Bereitstellungsleistung und Agentenprüfung." >}}

## Referenzen

- **AI Mechanics:** [Lokale KI vs. ChatGPT: Wie nah sind wir wirklich?](https://www.youtube.com/watch?v=siZ3f_06k8M).
- **Artificial Analysis:** [Modellergebnisse](https://artificialanalysis.ai/leaderboards/models), [Bewertungsmethode](https://artificialanalysis.ai/methodology/intelligence-benchmarking) und [lokale Inferenz](https://artificialanalysis.ai/hardware-inference-stack/laptops-workstations/).
- **Modellhersteller:** [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) und [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3).
- **Unsloth:** [Qwen-GGUF-Builds](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) und [GLM-GGUF-Builds](https://huggingface.co/unsloth/GLM-5.3-GGUF/tree/main).
- **Ollama:** [Dokumentation zu Laufzeit, Speicher und Datenschutz](https://docs.ollama.com/faq).
- **LangChain:** [Ergebnisse zur Agentenentwicklung](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering).
- **τ-bench:** [Forschung zu Tool-Agenten-Nutzer-Bewertung](https://arxiv.org/abs/2406.12045).
