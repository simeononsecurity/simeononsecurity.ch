---
title: "So wählen Sie ein ungefiltertes lokales KI-Modell aus"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: false
description: "Vergleichen Sie lokale Modellvarianten nach vollständigen Antworten, erhaltenen Fähigkeiten, Kontextnutzung, Quantisierung und passendem VRAM-Bedarf."
genre: ["Lokale KI", "Selbst gehostete KI", "KI-Sicherheit", "GPU-Komponenten"]
tags: ["ungefilterte lokale KI", "Abliterierung", "lokales LLM", "VRAM", "Kontextlänge", "Quantisierung", "Ollama", "Qwen3.8", "Gemma 4"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Lokaler KI-Arbeitsplatz mit Grafikkarte und Monitoren, die Modell- und Inferenzvisualisierungen zeigen"
coverCaption: ""
ref: ["/articles/local-ai-model-gpu-context-guide", "/articles/qwen38-27b-vast-ai-gpu-benchmark"]
---

**Modellauswahl:** Bewerten Sie jede Variante danach, welche nützlichen Antworten sie abschließt, wie viel Qualität sie erhält und wie viel Speicher Ihr Arbeitsablauf benötigt. Eine geringe Zahl an Ablehnungen oder eine beliebte Modellkarte belegen diese Ergebnisse nicht.

Für die Bezeichnung **ungefiltert** gibt es keine standardisierte Leistungsskala. Modellanbieter verwenden sie für unterschiedliche Gewichtsänderungen, Fine-Tunes und Chatvorlagen. Vergleichen Sie jeden Kandidaten mit dem Originalmodell und testen Sie die Aufgaben, die Sie ausführen möchten.

{{< youtube id="j-VqPVjztJE" enable="true" title="Ich habe alle ungefilterten lokalen KI-Modelle getestet (8 GB bis 32 GB VRAM)" description="Vergleich lokaler Modellvarianten, abgeschlossener Antworten, Kontexteinstellungen und GPU-Speicherklassen." >}}

## Was die Bezeichnung aussagt

Ein **abliteriertes Modell** hat Änderungen an seinen Gewichten erhalten, die bestimmte Ablehnungen verändern. Der Artikel von 2024 zur Ablehnungsrichtung zeigte eine Methode für 13 offene Chatmodelle. Neuere Werkzeuge bieten weitere Ansätze. Heretic 2 dokumentiert beispielsweise sowohl Ablation mit beliebigem Rang als auch gerichtete Ablation. Die Bezeichnung auf einer Modellkarte verrät nicht, welches Verhalten sich geändert hat oder was die Änderung beeinflusste.

Halten Sie beim Modellvergleich vier Eigenschaften auseinander:

| Eigenschaft | Was Sie prüfen sollten |
|---|---|
| **Ablehnungsverhalten** | Welche Anfragen führen zu einer Ablehnung, einer Teilantwort oder einer vollständigen Antwort? |
| **Erhalt der Fähigkeiten** | Wie schneiden Aufgaben zu Fakten, Schlussfolgerungen, Programmierung und Formatierung im Vergleich zum Originalmodell ab? |
| **Vollständigkeit der Antwort** | Wie oft endet die Generierung vor dem Token- oder Zeitlimit? |
| **Eignung für die Laufzeitumgebung** | Läuft genau diese quantisierte Datei mit genügend Speicher für den benötigten Kontext? |

Auch ein bearbeitetes Modell bleibt probabilistisch. **Prüfen Sie die Qualität getrennt:** Genauigkeit, Zuverlässigkeit und sichere Nutzung. Für Aufgaben, bei denen Schutzmaßnahmen wichtig sind, sollten Sie ein regulär ausgerichtetes Modell verfügbar halten.

## Warum die Zahl der Ablehnungen eine schwache Rangliste ergibt

**Ein Ablehnungswert** misst ein Ergebnis anhand eines Anfragensatzes. Über faktische Genauigkeit, Antwortlänge oder eine abschließende Antwort vor Ablauf des Generierungsbudgets sagt er wenig aus.

**Sapwells Qwen3.8-27B-Vergleich vom September 2026** testete das Basismodell und acht Varianten mit derselben Bereitstellung. Die 13 Aufgaben maßen Wissen, Mathematik, Programmierung und Wahrhaftigkeit. Ein separater HarmBench-Satz umfasste 400 schädliche Anfragen. Ein LLM-Bewerter prüfte die vollständigen Antworten. Die Ergebnisse gelten für eine Modellfamilie, eine GPU und ein bestimmtes Evaluierungsdesign.

| Qwen3.8-27B-Variante in der Studie | Ausdrückliche Ablehnungen von 400 | Antworten mit unvollständigem Denken |
|---|---:|---:|
| **Basismodell** | 381 | 0 % |
| **OrcaRouter** | 2 | 38 % |
| **Trohrbaugh** | 122 | 15 % |

Die hohe Zahl an Ablehnungen des Basismodells ging mit weniger unvollständigen Ausgaben einher. Die geringe Zahl bei OrcaRouter ging mit einem höheren Anteil unvollständiger Antworten einher. Trohrbaugh behielt mehr Ablehnungen bei und lieferte weniger unvollständige Antworten. **Richten Sie Ihre Wahl an Ihrer Aufgabe und den akzeptablen Abwägungen aus.**

**Eine Studie mit 23 Gemma-4-E4B-Varianten** fand bei der meistgeladenen Variante erhebliche Verluste bei einigen Fähigkeitsmessungen. Eine kleinere Änderung blieb in ihrem Test nahe am Basismodell. Popularität und Downloadzahlen beschreiben die Verbreitung, nicht die Qualität.

Fassen Sie diese Messwerte nicht zu einem Gesamtscore zusammen. **Trennen Sie die Messgrößen:** Ablehnung, Abschluss, Korrektheit und Latenz. Notieren Sie außerdem Anfragensatz, Modellrevision, Chatvorlage, Laufzeitumgebung, Kontext und Ausgabelimit. Jede Änderung an diesen Einstellungen verändert die Aussage des Vergleichs.

## Leere Antworten untersuchen, bevor Sie das Modell ersetzen

**Schlussfolgerungstoken** zählen zum Ausgabelimit, bevor sichtbarer Text erscheint. Läuft das Limit beim internen Denken ab, geben manche Laufzeitumgebungen eine leere oder abgeschnittene Antwort zurück. Das unterscheidet sich von einer Ablehnung oder einer abgeschlossenen, aber falschen Antwort.

**Sapwells Qwen3.6-27B-Benchmark** zeigte, wie sich das auf die Gesamtwerte auswirkt. Die Rohwerte bei Mathematik schwankten stark, weil einige Durchläufe nie eine endgültige Antwort erreichten. Bei den abgeschlossenen Antworten lagen die gemessenen Genauigkeitswerte viel näher beieinander. Der Benchmark trennte die Antwortfähigkeit vom Aufbrauchen des Denkbudgets.

**Prüfen Sie bei einer leeren Antwort den Stoppgrund und die Protokolle der Laufzeitumgebung.** Notieren Sie Eingabelänge, Kontextzuweisung, Ausgabetokenlimit, Laufzeit und ob das Modell eine Markierung für die endgültige Antwort erzeugte. Wiederholen Sie die Anfrage dann mit einem höheren Ausgabelimit, sofern die Ausrüstung noch Speicher frei hat.

| Ergebnis | Wahrscheinliche zu untersuchende Kategorie |
|---|---|
| **Ablehnungstext** | Das Modell lehnte die Anfrage ab. |
| **Leere Ausgabe am Tokenlimit** | Das Generierungsbudget war aufgebraucht, bevor eine endgültige Antwort entstand. |
| **Abgeschnittene Ausgabe** | Das Generierungslimit stoppte eine unvollständige Antwort. |
| **Laufzeitfehler** | Server, Modelldatei oder Speicherzuweisung schlugen fehl. |
| **Abgeschlossene, aber falsche Antwort** | Das Modell gab Text zurück, bestand aber die Korrektheitsprüfung nicht. |

**Leere Ausgabe:** Ermitteln Sie erst das Laufzeitergebnis, bevor Sie jeden Fall als Modellfehler einstufen. Ein größeres Kontextfenster behebt nicht automatisch ein niedriges Ausgabelimit, eine fehlerhafte Vorlage oder eine Zeitüberschreitung der Anwendung.

## VRAM für Gewichte und Kontext einplanen

Die Modelldatei ist nur ein Speicherverbraucher. Die Laufzeitumgebung benötigt auch Platz für den **KV-Cache**, der den Aufmerksamkeitszustand der aktiven Eingabe und Antwort speichert, sowie für Rechenpuffer und weitere geladene Prozesse. Ein längerer Kontext erhöht den Speicherbedarf.

**Die aktuelle Ollama-Dokumentation** nennt Standardkontextfenster von 4K bei weniger als 24 GiB VRAM, 32K zwischen 24 und 48 GiB sowie 256K ab 48 GiB. Diese Vorgaben beschreiben das Laufzeitverhalten. Prüfen Sie den zugewiesenen Kontext und die Prozessorplatzierung mit `ollama ps`.

**Linux-Beispiel:** Dieser Befehl legt für neue Ollama-Serversitzungen einen Standardwert von 16K fest:

```bash
OLLAMA_CONTEXT_LENGTH=16384 ollama serve
```

**Prüfen Sie den zugewiesenen Kontext** anhand üblicher Eingabe- und Antwortgrößen mit dem geladenen Modell:

```bash
ollama ps
```

Die Spalten `CONTEXT` und `PROCESSOR` zeigen die Zuweisung und ob das Modell auf der GPU oder teilweise außerhalb des GPU-Speichers läuft. **Kontextzuweisung:** Ein angezeigtes Limit garantiert nicht, dass das gesamte Fenster in den VRAM passt.

### Ausgangspunkte nach GPU-Speicher

**Erste Kandidaten:** Diese Modellfamilien kamen in Variantenvergleichen von 2026 vor. Die Dateigrößen stammen aus bestimmten quantisierten Repositories. Prüfen Sie die genaue Datei, die Laufzeitunterstützung und den gemessenen Speicherverbrauch, bevor Sie einen Kandidaten als passend einstufen.

| GPU-Speicher | Erster Kandidat | Wichtigste Einschränkung |
|---|---|---|
| **8 GB** | Gemma 4 E4B, etwa die Variante `coder3101` | Hält die Gewichtsdatei klein. Lassen Sie Speicher für Kontext und Laufzeitpuffer frei. |
| **12 GB** | Gemma 4 12B, etwa die 7,4-GB-GGUF-Q4-Datei von `TrevorJS` | Bietet mehr Modellkapazität, aber weniger Platz für langen Kontext als eine kleinere Variante. |
| **16 GB** | Ein kleineres Modell oder eine Q3-Datei von Qwen3.8-27B | Das Qwen-Repository nennt für Q3_K_S 13,72 GB. Der Anbieter stuft diese Datei als niedrigwertig ein. Der Spielraum für Kontext bleibt begrenzt. |
| **24 GB** | Qwen3.8-27B Q4_K_S oder Q4_K_M | Das aktuelle Repository nennt Dateien mit 16,71 GB und 17,77 GB. Lassen Sie Platz für Cache und Puffer. |
| **32 GB** | Qwen3.8-27B Q6_K | Das aktuelle Repository nennt eine Datei mit 23,46 GB. Eine größere Datei lässt weniger Speicher für Kontext als eine kleinere Quantisierung. |

*Verwenden Sie diese Optionen als Ausgangspunkt. Repositories und Versionen ändern sich. Die Dateigröße allein sagt weder den Laufzeitspeicherbedarf noch die Antwortqualität voraus.*

GGUF-Quantisierungsbezeichnungen fassen eine Kodierungsentscheidung zusammen. **Unterschiede zwischen Repositories:** Dateien mit derselben nominellen Bitbreite müssen nicht gleichwertige Qualität haben. Ein Qwen-Repository stuft Q3_K_S als niedrigwertig und Q4_K_M als Standardwahl ein. Prüfen Sie vor dem Herunterladen Dateigröße, Modellkarte, Eingabeformat und Testergebnisse.

**Für Cache-Größe und lokale GPU-Eignung** lesen Sie den [Leitfaden zu lokalen Modellen, GPU und Kontext](/articles/local-ai-model-gpu-context-guide/). Dort stehen Programmieraufgaben im Mittelpunkt. Diese Seite behandelt geändertes Ablehnungsverhalten und Evaluierung.

## Chatvorlage und Modellquelle prüfen

Eine **Chatvorlage** verpackt Nachrichten in die Token und Anweisungen, die das Modell erwartet. Ein Modellpaket enthält manchmal eine angepasste Vorlage oder Systemanweisung. Das beeinflusst das gemessene Verhalten, auch wenn die zugrunde liegenden Gewichte unverändert bleiben.

**Einfluss der Vorlage:** Sapwell fand eine Qwen3.8-Variante, deren Paket eine Persönlichkeitsvorgabe enthielt, die das Modell anwies, niemals abzulehnen oder zu warnen. Die geringe Zahl an Ablehnungen hing von dieser Vorlage ab. Der Vergleich vereinheitlichte die Vorlagen, damit der Test die Unterschiede zwischen den Gewichten hervorhob. Diese Kontrolle belegt nicht, dass die bereitgestellte Vorlage schädlich oder unbrauchbar ist.

**Vor der Installation:** Prüfen Sie Anbieter, Basismodell, Lizenz, Konvertierungsverfahren, Quantisierer, Vorlage und Versionsverlauf. Vergleichen Sie das Modell mit dem Original unter derselben Vorlage und Laufzeitumgebung. Fehlen Methode oder Testaufbau auf der Modellkarte, kennzeichnen Sie die Herkunft als unbekannt.

## Eine kleine Evaluierung für Ihre Aufgaben durchführen

**Erstellen Sie einen wiederholbaren Anfragensatz** aus üblichen Aufgaben, die Ihnen gehören oder die Sie testen dürfen. Nehmen Sie die geplante Arbeit des Modells, Sachfragen mit bekannten Antworten und Formatierungsaufträge mit eindeutigen Bestehenskriterien auf. Ergänzen Sie sichere Grenzfälle, damit das Ablehnungsverhalten bei der Entscheidung berücksichtigt wird.

**Halten Sie die Testeinstellungen** für Originalmodell und Variante konstant. Ändern Sie Systemanweisung, Vorlage, Quantisierung, Laufzeitversion, Kontext, Ausgabelimit und Sampling-Einstellungen nicht. Speichern Sie Modellrevision oder Dateihash mit den Ergebnissen.

Erfassen Sie jedes Ergebnis getrennt:

- **Abschluss:** endgültige Antwort, Ablehnung, leere Ausgabe, Abbruch oder Laufzeitfehler.
- **Korrektheit:** bestanden oder nicht bestanden nach einer erwarteten Antwort oder Bewertungsrichtlinie.
- **Nützlichkeit:** ob die Antwort die Aufgabenanforderungen erfüllt.
- **Latenz:** Zeit bis zum ersten Token und gesamte Generierungszeit.
- **Speicher:** zugewiesener Kontext, GPU-Platzierung und maximaler VRAM-Verbrauch.
- **Sicherheitsverhalten:** angemessene Ablehnung oder Fortsetzung bei jedem Grenzfall.

Wiederholen Sie den Satz nach einer einzelnen Änderung. Wird die Antwort nach Erhöhung des Ausgabelimits abgeschlossen, lag der erste Fehler am Budget. Bleiben die Antworten unvollständig, prüfen Sie Modellvorlage, Denkmodus, Laufzeit und Modellrevision. **Behalten Sie die Variante nur, wenn sie Ihre Zielaufgabe verbessert, ohne unvertretbare Verluste bei Genauigkeit oder Sicherheit.**

## Einsatz begrenzen

**Datenschutz:** Lokale Inferenz hängt von Ihrem gesamten Stack ab. Prüfen Sie Oberfläche, Protokolle, Erweiterungen, Telemetrie und Netzwerkwege. Behandeln Sie nicht vertrauenswürdige Gewichte und angepasste Vorlagen wie Code und Konfigurationen Dritter.

**Öffentlicher Zugriff:** Stellen Sie den Modellendpunkt niemals direkt ins öffentliche Internet. Isolieren Sie den Werkzeugzugriff und verwenden Sie bearbeitete Varianten nur für autorisierte Aufgaben. Legen Sie den Endpunkt für Fernzugriff hinter ein privates Gateway mit Authentifizierung, Anfragelimits und Netzwerkisolierung. Der ursprüngliche Artikel zur Ablehnungsrichtung beschreibt die Sicherheitsfolgen von Änderungen, die Ablehnungen entfernen.

## Fazit

**Entscheidungsregel:** Wählen Sie das Modell mit den stärksten überprüften Ergebnissen für Ihren eigenen Aufgabensatz. Verwenden Sie Ablehnungszahlen als eine Messgröße und prüfen Sie anschließend Antwortabschluss, Korrektheit, Vorlagenverhalten und VRAM-Reserve. Beginnen Sie mit einer Datei, die zu Ihrer GPU passt, wählen Sie den Kontext passend zu Ihren Aufgaben und vergleichen Sie unter identischen Einstellungen mit dem Originalmodell.

**Für die GPU-Auslegung** vergleichen Sie diese Ergebnisse mit dem [Qwen-27B-GPU-Mietbenchmark](/articles/qwen38-27b-vast-ai-gpu-benchmark/). Mieten oder leihen Sie Ausrüstung, bevor Sie sie kaufen, wenn Modelldatei oder Kontextziel noch unklar sind.

## Quellen

- [Qwen3.8-27B-Abliterationsbenchmark](https://nathan.sapwell.net/posts/qwen38-27b-abliteration/), Nathan Sapwell, 6. September 2026.
- [Qwen3.6-27B-Abliterationsbenchmark](https://nathan.sapwell.net/posts/qwen36-27b-abliteration/), Nathan Sapwell, 2026-05-17.
- [Benchmark zu Gemma-4-E4B-Varianten](https://nathan.sapwell.net/posts/gemma4-e4b-abliteration/), Nathan Sapwell, 1. August 2026.
- [Benchmark zu Gemma-4-12B-Varianten](https://nathan.sapwell.net/posts/gemma4-12b-abliteration/), Nathan Sapwell, 28. August 2026.
- [Ablehnung in Sprachmodellen wird durch eine einzelne Richtung vermittelt](https://arxiv.org/abs/2406.11717), Arditi et al., 2024.
- [Dokumentation des Heretic-Projekts](https://github.com/p-e-w/heretic/).
- [Offizielle Qwen3.8-27B-Modellkarte](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Ollama-Dokumentation zur Kontextlänge](https://docs.ollama.com/context-length).
- [Gemma-4-E4B-Modellkarte für `coder3101`](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic).
- [Gemma-4-12B-GGUF-Dateien von TrevorJS](https://huggingface.co/TrevorJS/gemma-4-12B-it-uncensored-GGUF).
- [OrcaRouter-Qwen3.8-27B-GGUF-Dateien](https://huggingface.co/bartowski/orcarouter_Qwen3.8-27B-Uncensored-GGUF).
- [GGUF-Format und Quantisierungstypen](https://huggingface.co/docs/hub/en/gguf), Hugging-Face-Dokumentation.
- [Videoquelle: Ich habe alle ungefilterten lokalen KI-Modelle getestet (8 GB bis 32 GB VRAM)](https://www.youtube.com/watch?v=j-VqPVjztJE).
