---
title: "2x RTX 5060 Ti gegen GB10: Lokaler KI-Benchmark mit fünf Modellen und 256K Kontext"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Vergleich von RTX 5060 Ti und GB10 mit fünf Modellen sowie ein Qwen3.8-Flash-Next-Benchmark mit Strata auf demselben Host und bis zu 256K Kontext."
genre: ["Künstliche Intelligenz", "Lokale KI", "GPU-Hardware", "Benchmarks", "Computerhardware"]
tags: ["RTX 5060 Ti", "GB10", "DGX Spark", "Qwen3.8", "Qwen3.8 Flash-Next", "GSQ-RCO", "Qwen4Exp", "Strata", "Qwen3.5", "Qwen3.6", "GPT-OSS", "Nemotron", "lokale LLM", "lokale Inferenz", "Unified Memory", "VRAM", "GPU-Benchmark", "langer Kontext", "PCIe-Overhead", "KI-Hardware", "NVIDIA Blackwell", "LLM-Leistung", "GPU-Speicher"]
cover: "/img/cover/nvidia-rtx-5060-ti-vs-gb10-memory-performance-comparison.webp"
coverAlt: "Eine Illustration zeigt links zwei NVIDIA-RTX-5060-Ti-Grafikkarten und rechts ein NVIDIA-GB10-System, beide mit leuchtenden Farben vor dunklem Hintergrund."
coverCaption: "Die Leistung lokaler Modelle hängt von Speicherarchitektur, Modellauswahl und Kontextlänge ab."
---

**Zwei RTX 5060 Ti mit jeweils 16 GB bieten zusammen 32 GB VRAM.** Ein NVIDIA-GB10-System verfügt über 128 GB kohärenten Unified Memory. Der neue Benchmark mit fünf Modellen zeichnet ein ausgewogeneres Bild als der frühere Test nur mit Qwen.

Bei der Einstellung 256K erzeugt das System mit zwei Karten bei vier von fünf Modellen schneller. Beim Qwen3.8 27B liegt der GB10 deutlich vorn und hält mehr Speicher für Modelle, Kontext und Runtime-Zuweisungen frei. Die beste Wahl hängt vom Modell und der Arbeitslast ab.

Ein separater Lauf auf demselben Host verglich Qwen3.8-Flash-Next IQ2_XS auf Strata mit dichtem Qwen3.8 27B Q4_K_M auf Ollama. Nach dem Aufwärmen lag der Median der Generierung für Flash-Next bei 92.8 Token pro Sekunde mit einem Prompt von 260,446 Token. Das dichte Qwen3.8 erreichte 0.939 Token pro Sekunde mit einem Prompt von 260,444 Token.

Der NVIDIA GB10 nutzt 128 GB kohärenten Unified Memory. NVIDIA nennt für die GB10-Plattform 128 GB LPDDR5x Unified Memory und eine Chip-TDP von 140 W. Jede RTX 5060 Ti verfügt über 16 GB GDDR7, eine 128-Bit-Speicherschnittstelle und eine angegebene Grafikleistung von 180 W. Die [Spezifikationen der NVIDIA RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/) und des [NVIDIA GB10](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) beschreiben den Hardwareunterschied.

**Die beiden Systeme stellen Speicher unterschiedlich bereit.** Zwei Karten bilden zwei getrennte 16-GB-Pools. Der GB10 legt Modell, Kontextdaten, Runtime-Puffer und Betriebssystemzuweisungen in einem gemeinsamen Adressraum ab.

## Der Speichervergleich

| System | Speicher | Speichermodell | Angegebene Leistungsaufnahme |
|---|---:|---|---:|
| **2x RTX 5060 Ti 16 GB** | 32 GB gesamt | Zwei getrennte GPU-Speicherpools | 360 W GPU gesamt |
| **GB10-System** | 128 GB | Kohärenter gemeinsamer Systemspeicher | 140 W GB10-TDP |

Der GB10 gewinnt nicht jeden Durchsatztest, denn LPDDR5x erreicht nicht die Bandbreite diskreter GPUs. Sein Vorteil liegt bei Kapazität und Speicherzuordnung. CPU und GPU teilen sich denselben Adressraum, sodass der Arbeitssatz nicht in zwei getrennte 16-GB-Geräte passen muss.

Das System mit zwei Karten muss das Modell auf beide Karten verteilen und Daten zwischen ihnen verschieben. PCIe-Verkehr erhöht die Latenz und beansprucht Bandbreite. Laut NVIDIA-Spezifikationen unterstützt die RTX 5060 Ti außerdem kein NVLink.

## Der Benchmark mit fünf Modellen

Der aktualisierte Lauf verwendete auf beiden Systemen dieselbe Anfragematrix. Er umfasste fünf Ollama-Modelle mit Kontexteinstellungen von 4K, 16K, 32K, 64K, 128K und 256K. Jede Anfrage erzeugte 128 Token bei Temperatur 0.

Die getesteten Modell-Tags waren:

- **Qwen3.8 27B:** `qwen3.8:27b`
- **GPT-OSS 20B:** `gpt-oss:20b`
- **Qwen3.6 35B-A3B:** `qwen3.6:35b`
- **Qwen3.5 35B-A3B:** `qwen3.5:35b-a3b-q4_K_M`
- **Nemotron 3.5 Lightning 30B-A3B:** `nemotron-3.5-lightning:30b-a3b-q4_K_M`

Das System mit zwei Karten verwendete zwei RTX 5060 Ti mit jeweils 16 GB. Das GB10-System nutzte 128 GB Unified Memory. Die Tests liefen mit Ollama, Version 0.34.2 auf dem System mit zwei Karten und Version 0.40.2 auf dem GB10.

### Generierungsgeschwindigkeit

Die Generierungsgeschwindigkeit misst die Token, die nach der Prompt-Verarbeitung entstehen. Dieser Wert ist bei interaktiven Gesprächen besonders wichtig.

System mit zwei RTX 5060 Ti:

| Kontext | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 91.518 | 162.027 | 117.547 | 156.104 | 55.654 |
| 16K | 87.176 | 161.377 | 112.903 | 140.596 | 51.656 |
| 32K | 82.372 | 157.055 | 106.455 | 144.833 | 47.369 |
| 64K | 74.661 | 135.106 | 95.979 | 125.008 | 38.863 |
| 128K | 62.767 | 130.924 | 79.572 | 115.352 | 26.399 |
| 256K | 67.853 | 106.221 | 58.947 | 67.159 | 1.079 |

GB10:

| Kontext | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 62.199 | 98.648 | 72.405 | 100.906 | 32.985 |
| 16K | 56.764 | 94.366 | 69.782 | 95.448 | 32.939 |
| 32K | 53.257 | 98.175 | 64.055 | 95.025 | 29.772 |
| 64K | 49.201 | 96.132 | 58.428 | 84.528 | 25.625 |
| 128K | 40.637 | 80.238 | 48.108 | 74.579 | 22.294 |
| 256K | 43.688 | 68.043 | 36.649 | 62.115 | 22.371 |

Bei 256K generierte das System mit zwei Karten GPT-OSS, Nemotron, Qwen3.5 und Qwen3.6 schneller. Beim Qwen3.8 lag der GB10 mit deutlichem Abstand vorn: Das Modell fiel auf dem System mit zwei Karten auf 1.079 Token pro Sekunde, während der GB10 22.371 Token pro Sekunde erreichte.

Das Ergebnis für Qwen3.6 liegt nahe beieinander. Das System mit zwei Karten erreichte 67.159 Token pro Sekunde, der GB10 62.115. Daraus folgt nicht, dass Unified Memory immer gewinnt oder zwei diskrete GPUs immer überlegen sind.

### Prompt-Verarbeitungsgeschwindigkeit

Die Prompt-Verarbeitung misst, wie schnell die Runtime den Eingabekontext vor der Generierung einliest. Sie ist bei langen Dokumenten und wiederholtem Laden des Kontexts wichtig.

System mit zwei RTX 5060 Ti:

| Kontext | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 4745.9 | 2409.0 | 2701.7 | 464.3 | 783.9 |
| 16K | 7617.0 | 3031.8 | 4175.3 | 2654.0 | 840.1 |
| 32K | 8099.5 | 3074.2 | 4335.8 | 2623.2 | 811.2 |
| 64K | 6809.5 | 2893.0 | 4129.9 | 2400.4 | 727.8 |
| 128K | 5089.9 | 2362.7 | 3084.0 | 1723.6 | 546.1 |
| 256K | 5838.3 | 1813.2 | 2229.1 | 1011.0 | 251.3 |

GB10:

| Kontext | GPT-OSS 20B | Nemotron 3.5 | Qwen3.5 35B | Qwen3.6 35B | Qwen3.8 27B |
|---:|---:|---:|---:|---:|---:|
| 4K | 3295.5 | 576.0 | 2067.9 | 628.8 | 756.9 |
| 16K | 4675.5 | 3006.7 | 2691.2 | 2556.3 | 812.6 |
| 32K | 4571.4 | 3077.9 | 2691.7 | 2563.9 | 794.1 |
| 64K | 3704.7 | 3066.9 | 2585.3 | 2444.9 | 714.0 |
| 128K | 2857.0 | 2802.9 | 2360.4 | 2229.9 | 655.5 |
| 256K | 3243.4 | 2325.4 | 1938.5 | 1817.6 | 535.1 |

Bei 256K verarbeitete das System mit zwei Karten die Prompts von GPT-OSS und Qwen3.5 schneller. Der GB10 lag bei Nemotron, Qwen3.6 und Qwen3.8 vorn. Modellarchitektur und Runtime-Verhalten sind ebenso wichtig wie die Speicherschnittstelle.

## Ergänzende Qwen3.8-Flash-Next-Benchmarks

Drei weitere Läufe maßen Qwen3.8-Flash-Next-GGUF-Pakete auf dem System mit zwei RTX 5060 Ti bei Kontexteinstellungen von 4K und 16K. Jede Zeile nennt die genaue Hugging-Face-Modellreferenz und Quantisierung.

| Genaues Modell | Quantisierung | Generierung 4K | Generierung 16K |
|---|---:|---:|---:|
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS) | IQ2_XS | 31.77 tok/s | 28.20 tok/s |
| [`hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S`](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S) | IQ3_S | 24.54 tok/s | 22.60 tok/s |
| [`hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M`](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF/tree/main) | Q4_K_M | 17.91 tok/s | 17.02 tok/s |

Das Paket IQ2_XS erreichte in dieser Gruppe den höchsten Durchsatz: 31.77 Token pro Sekunde bei 4K, gegenüber 24.54 für IQ3_S und 17.91 für Q4_K_M. Bei 16K blieb die Reihenfolge mit 28.20, 22.60 und 17.02 Token pro Sekunde gleich.

Führe dieselben exakten Modellreferenzen mit Ollama aus:

```bash
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ2_XS
ollama run hf.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF:IQ3_S
ollama run hf.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF:Q4_K_M
```

Diese früheren Zusatzwerte stammen von einem System mit zwei GPUs und sind von der obigen abgestimmten Anfragematrix für RTX 5060 Ti und GB10 getrennt. Die Aufzeichnung nennt die exakten Modellreferenzen, Quantisierungen, Kontexteinstellungen und Generierungsgeschwindigkeiten. Es fehlen aufgelöste Manifest-Digests, verarbeitete Prompt-Token, Ausgabelänge, Aufwärmzustand, Geräteaufteilung, CPU, Arbeitsspeicher, Kühlung und Messdatum.

## Strata gegen dichtes Ollama bei 256K

**Ein zweiter Benchmark vom 14. Oktober 2026 verglich zwei Modell- und Runtime-Stacks auf demselben Host mit zwei RTX 5060 Ti.** Die dichte Baseline verwendete [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b), ein Qwen35-Modell mit 27.3 Milliarden Parametern in Q4_K_M. Der Flash-Stack nutzte [Qwen3.8-Flash-Next IQ2_XS](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ2_XS), ein Qwen4Exp-Mixture-of-Experts-Modell in einem nativen, vereinheitlichten Strata-Paket.

Dies ist ein Vergleich ganzer Stacks. Modellarchitektur, Quantisierung, Paketierung, Experten-Routing und Inferenz-Engine änderten sich gemeinsam. Die Flash-Varianten IQ3_S und Q4_K_M waren nicht Teil dieses Durchlaufs.

### Testsystem und Methode

| Komponente | Aufgezeichnete Konfiguration |
|---|---|
| **GPUs** | 2x NVIDIA GeForce RTX 5060 Ti, jeweils 16 GiB, Compute Capability 12.0 |
| **GPU-Verbindung** | PCIe 4.0 x4 pro Karte, PHB-Topologie, kein NVLink |
| **CPU** | AMD Ryzen 9 5900XT, 32 Threads |
| **Host-Speicher** | 62 GiB RAM und 15 GiB Swap |
| **NVIDIA-Treiber** | 595.99.02 |

Der Harness erzeugte synthetische nummerierte Datensätze. Jede Zeile folgte dem Format `Record 00001: alpha beta gamma delta epsilon zeta eta theta iota kappa.` Die Anweisung verlangte zuerst `BENCHMARK_OK`, gefolgt von einer knappen technischen Zusammenfassung bis zum Ausgabelimit. Die sechs Prompts enthielten 180, 720, 1,500, 3,100, 6,200 und 12,400 Datensätze.

Jeder Lauf verwendete Temperatur 0, Seed 42 und eine maximale Ausgabelänge von 128 Token. Für jeden Kontext folgten auf einen Aufwärmlauf fünf gemessene Anfragen. Die Ollama-Tests nutzten `/api/generate`, die Strata-Tests `/v1/chat/completions`. Alle gemessenen Anfragen wurden ohne API-Fehler abgeschlossen.

Die Dekodiersteuerung war nicht angeglichen. Strata setzte `reasoning_effort` ausdrücklich auf `none` und deaktivierte Thinking über sein Chat-Template. Die Anfrage für das dichte Modell an Ollama enthielt kein `think: false`; eine Folgeprüfung fand die dichte Ausgabe in den Feldern für Thinking und Antwort. Der Generierungswert gilt daher nur für diese Dekodiermodi.

| Kontexteinstellung | Prompt-Token, dicht | Prompt-Token, Flash |
|---:|---:|---:|
| **4K** | 3,824 | 3,826 |
| **16K** | 15,164 | 15,166 |
| **32K** | 31,544 | 31,546 |
| **64K** | 65,144 | 65,146 |
| **128K** | 130,244 | 130,246 |
| **256K** | 260,444 | 260,446 |

Beide Modell-Header gaben einen maximalen Kontext von 262,144 Token an. Die gepaarten Prompts unterschieden sich an jedem Prüfpunkt um zwei Token.

### Median der Generierungsgeschwindigkeit nach dem Aufwärmen

Jeder Median umfasst fünf gemessene Anfragen nach einem Aufwärmlauf. Jede gemessene Anfrage des dichten Modells verwendete alle bis auf vier Prompt-Token erneut. Bei Flash waren es alle bis auf sieben. Die Tabelle misst warmen Dekodierdurchsatz mit zwischengespeichertem Präfix, nicht die kalte End-to-End-Latenz.

| Kontext | Flash IQ2_XS auf Strata | Dichtes Q4_K_M auf Ollama | Flash-Vorsprung |
|---:|---:|---:|---:|
| **4K** | 98.4 tok/s | 65.0 tok/s | 1.51x |
| **16K** | 96.8 tok/s | 60.6 tok/s | 1.60x |
| **32K** | 95.3 tok/s | 64.4 tok/s | 1.48x |
| **64K** | 89.6 tok/s | 51.2 tok/s | 1.75x |
| **128K** | 92.9 tok/s | 31.5 tok/s | 2.95x |
| **256K** | 92.8 tok/s | 0.939 tok/s | 98.9x |

Der Flash-Stack blieb von 64K bis 256K bei etwa 90 Token pro Sekunde. Dichtes Qwen3.8 wurde nach 64K deutlich langsamer und erreichte bei 256K 0.939 Token pro Sekunde. Die Flash-Antwort bei 256K endete regulär nach 67 Token. Der dichte Lauf erreichte das Ausgabelimit von 128 Token.

### Prompt-Verarbeitung bei der ersten Anfrage

| Kontext | Erste Flash-Anfrage | Erste Anfrage, dicht |
|---:|---:|---:|
| **4K** | 1,134 tok/s | 832 tok/s |
| **16K** | 2,013 tok/s | 856 tok/s |
| **32K** | 2,386 tok/s | 799 tok/s |
| **64K** | 2,509 tok/s | 690 tok/s |
| **128K** | 2,538 tok/s | 489 tok/s |
| **256K** | 2,399 tok/s | 214 tok/s |

Die erste Anfrage des dichten Modells verarbeitete an jedem Prüfpunkt den vollständigen Prompt. Strata meldete 16,384 wiederverwendete Präfix-Token bei 64K, 49,152 bei 128K und 114,688 bei 256K. Die Flash-Werte von 64K bis 256K sind als Fortsetzungsdurchsatz der ersten Anfrage zu behandeln, nicht als vollständiges Prefill ohne Cache.

Bei 256K verarbeitete Strata die erste Anfrage in 60.8 Sekunden. Ollama benötigte etwa 1,215.4 Sekunden. Durch die Präfix-Wiederverwendung ist an diesem Prüfpunkt kein direkter Vergleich des kalten Prefills möglich.

### Die Runtime-Zuordnung erklärt den Unterschied bei langem Kontext

Ollama 0.34.2 verwendete llama-server 0.4.1-dev mit CUDA-Layer-Offload, dem ChatML-Template und spekulativer MTP-Dekodierung mit einer maximalen Draft-Breite von vier. Batch- und Microbatch-Größen betrugen 1,024 bei 32K und 512 von 64K bis 256K. Bei 32K und 64K blieben alle 66 dichten Layer auf den GPUs. Bei 128K blieben 63 von 66 Layern auf den GPUs; 1,404 MiB wechselten in CPU-gemappten Speicher. Bei 256K blieben 42 von 66 Layern auf den GPUs; 6,002 MiB wechselten in CPU-gemappten Speicher. Die MTP-Akzeptanzrate lag bei 256K bei etwa 69.4 Prozent.

Strata 0.1.44.1 mit CUDA 13.0.3 verteilte seine 48 Layer auf beide GPUs. Die 4K- und 16K-Konfiguration legte Layer 0 bis 23 auf die erste GPU und Layer 24 bis 47 auf die zweite. Dieser Durchlauf nutzte eine automatische VRAM-Reserve von 700 MiB und 16,047 residente Experten-Slots.

Die Konfiguration von 32K bis 256K legte Layer 0 bis 24 auf die erste GPU und Layer 25 bis 47 auf die zweite. Sie nutzte automatisches Prefill, eine minimale spekulative Wahrscheinlichkeit von 0.5, INT8-KV-Speicher, 32,768 residente KV-Zellen pro QSA-Layer, eine VRAM-Reserve von 832 MiB, einen Expert-Cache mit 15,318 Slots und 21,024 MiB sowie spekulative MTP-Dekodierung mit einer maximalen Draft-Breite von vier.

Der Digest des nativen Strata- und PLE-Blobs lautete `sha256:1473e0664c2017095f9164b6d617d7a71893452c1180c83002c4f28fc8c2b0da`. Der Lauf benötigte außerdem ein Expertenprofil und ein MTP-Draft-Paket ohne veröffentlichte unveränderliche Digests.

Der Strata-Lauf nutzte den standardmäßigen Route-Tail-Skip-Modus. Diese Einstellung verändert die Modellausgabe leicht und bindet das Ergebnis an die aufgezeichnete Runtime-Konfiguration. Flash-Antworten enthielten den Marker `BENCHMARK_OK`. Die dichten Anfragen meldeten keine API-Fehler, doch der primäre Harness erfasste den Marker nicht. In den Rohdaten standen null Antwortzeichen. Eine Folgeprüfung fand Ausgaben in den Feldern für Antwort und Thinking und bestätigte `BENCHMARK_OK` in der Antwort.

Die 4K- und 16K-Konfiguration protokollierte eine Anfrage mit 409 MiB freiem Speicher und empfahl eine Reserve von 832 MiB. Die Langkonfiguration protokollierte eine Anfrage mit 481 MiB freiem Speicher und empfahl 896 MiB Reserve. Beide Werte lagen unter der Paging-Schwelle des Treibers von 512 MiB. Keine Anfrage schlug fehl, doch dieser geringe Speicherstand beeinträchtigt die Wiederholbarkeit.

**Der Wert 98.9x ist als Langkontext-Ergebnis des gesamten Stacks zu verstehen, nicht als Beleg für einen 98.9-fachen Vorteil der Engine allein.** Der Test isoliert den Host, nicht aber Modell, Quantisierung oder Runtime.

## Die tatsächliche Prompt-Länge zählt

Die angeforderte Kontexteinstellung entspricht nicht der Zahl der verarbeiteten Prompt-Token. Bei 256K verarbeiteten Qwen3.5, Qwen3.6, Nemotron und Qwen3.8 auf beiden Systemen etwa 171,359 bis 171,365 tatsächliche Prompt-Token.

GPT-OSS verarbeitete bei der Einstellung 256K auf beiden Systemen 65,538 tatsächliche Prompt-Token. Seine 256K-Zeile steht daher nicht für dieselbe Eingabelänge wie bei den anderen Modellen.

Das Qwen3.8-Ergebnis bei 256K zeigt den größten Unterschied. Das System mit zwei Karten verarbeitete 171,359 Prompt-Token mit 251.3 Token pro Sekunde und generierte mit 1.079 Token pro Sekunde. Der GB10 verarbeitete dieselbe Zahl Prompt-Token mit 535.1 Token pro Sekunde und generierte mit 22.371 Token pro Sekunde.

**Die Kontexteinstellung belegt das angeforderte Limit.** Die tatsächliche Zahl der Prompt-Token zeigt die von der Runtime abgeschlossene Arbeitslast.

## Warum die gesamte VRAM-Kapazität weiterhin wichtig ist

### 1. Das Modell sieht keine einzelne 32-GB-Karte

Zwei GPUs fassen ihren Speicher nicht zu einem lokalen Adressraum zusammen. Eine model-parallel Runtime verteilt Layer oder Tensoren auf die Geräte. Jedes Gerät benötigt weiterhin Platz für seine Gewichte, temporäre Puffer und einen Teil des Kontextzustands.

Die nutzbare Kapazität liegt unter der einfachen Summe. Der genaue Overhead hängt von Modellformat, Quantisierung, Inferenz-Backend, Tensoraufteilung und Kontextlänge ab.

### 2. Der Speicherbedarf für den Kontext wächst während der Generierung

Die Modellgewichte sind nur ein Teil des Speicherbedarfs. Der Key-Value-Cache (KV-Cache) speichert Attention-Daten vorheriger Token. Längere Kontexte benötigen mehr Cache-Speicher. Ein 4K-Test sagt nichts Verlässliches über einen Einsatz mit 128K oder 256K aus.

Die neuen Ergebnisse zeigen je nach Modell unterschiedliche Grenzen. Qwen3.8 bricht bei 256K auf dem System mit zwei Karten bei der Generierung stark ein. Die anderen vier Modelle halten auf beiden Systemen eine nutzbare Generierungsgeschwindigkeit. Die Speicherkapazität bleibt wichtig, weil sie bestimmt, welche Modell- und Kontextkombinationen samt Runtime-Zuweisungen passen.

### 3. PCIe-Transfers verursachen Zusatzkosten

Wenn die Runtime Aktivierungen oder Tensoren zwischen GPUs verschiebt, läuft der Transfer über die Host-Verbindung. Dadurch entstehen Synchronisationspunkte und zusätzliche Latenz pro Schritt. Der Nachteil hängt von Tensorplatzierung, Modellarchitektur, Quantisierung und Kontextlänge ab.

Damit wird ein System mit zwei GPUs nicht nutzlos. Das Ergebnis hängt vielmehr von Runtime-Konfiguration und Modell ab. Ein Benchmark, der nur die Prompt-Verarbeitung bei 4K nennt, lässt diese Kosten außen vor.

### 4. Energieeffizienz bleibt ein Systemvorteil

Der GB10 bietet mehr Speicherkapazität bei geringerer angegebener Chip- oder GPU-Leistung. Zwei RTX 5060 Ti kommen zusammen auf 360 W GPU-Leistung, ohne den Rest des Systems. NVIDIA gibt für den GB10 eine TDP von 140 W an.

**Der GB10 tauscht bei mehreren Modellen Spitzendurchsatz gegen Kapazität, einen gemeinsamen Arbeitssatz und geringere angegebene GPU-Leistung.** Das System mit zwei Karten erreicht bei mehreren neueren MoE-Modellen einen höheren gemessenen Durchsatz.

## Das 5060ti-x2-System ist deutlich günstiger

Eine komplette Workstation mit zwei RTX 5060 Ti mit jeweils 16 GB wurde am 10. Oktober 2026 für **$3,479** angeboten. Die Konfiguration umfasst Intel Ultra 7 265K, Z890-Mainboard, 32 GB DDR5, 1 TB Speicher, ein 1,000-W-Netzteil und beide GPUs. [Angebot der kompletten Workstation mit zwei GPUs ansehen](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white).

Der US-Marktplatz von NVIDIA listet den DGX Spark mit 128 GB für **$6,950**. Das Angebot umfasst 128 GB kohärenten Unified Memory und 4 TB NVMe-Speicher, kennzeichnet das System aber als nicht vorrätig. [Aktuelles DGX-Spark-Angebot von NVIDIA prüfen](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/).

Die AMD Ryzen AI Halo Developer Platform bildet einen weiteren Vergleichspunkt. Dieses Strix-Halo-System kostet bei Micro Center **$3,999.99** und bietet 128 GB LPDDR5x Unified Memory sowie 2 TB Speicher. Strix Halo gehört oft zur selben praktischen Klasse lokaler KI-Systeme wie GB10, auch wenn unabhängige Tests bei Durchsatz und Software-Reife häufig den GB10 vorn sehen. [Aktuelles Linux-Angebot bei Micro Center prüfen](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false) und [den Vergleich Strix Halo gegen GB10 lesen](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4).

| Komplettes System | Angebotspreis vom 10. Oktober 2026 | Preisunterschied |
|---|---:|---:|
| **5060ti-x2-Workstation** | $3,479 | Ausgangswert |
| **AMD Ryzen AI Halo, Strix Halo** | $3,999.99 | $520.99 mehr |
| **128 GB GB10 DGX Spark** | $6,950 | $3,471 mehr |

Der GB10 bietet einen größeren Unified-Memory-Pool und eine geringere angegebene GPU-Leistung. Das AMD-System bietet dieselbe Speicherklasse von 128 GB für etwa $4,000. Die 5060ti-x2-Workstation kostet vor Steuern und Versand weiterhin nur ungefähr **50 % des Angebotspreises des GB10**.

Dies sind Angebotspreise verschiedener Händler, kein kontrollierter Warenkorb. Das 5060ti-x2-System verfügt außerdem über weniger Arbeitsspeicher und Speicherplatz. Aktuelle Angebote für RTX 5060 Ti mit 16 GB liegen bei **$789 bis $830 pro Karte** und damit deutlich über der unverbindlichen Preisempfehlung von $429 zum Marktstart. Der Preisvorteil des Systems mit zwei Karten bleibt während des aktuellen GPU-Preisanstiegs bestehen. [Aktuelle RTX-5060-Ti-Preise prüfen](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/).

## Bedeutung für lokale KI-Arbeitslasten

Eine Konfiguration mit zwei 16-GB-Karten führt mehrere quantisierte Modelle mit 27B bis 35B Parametern bei langen Kontexteinstellungen aus. Der Benchmark zeigt keinen allgemeinen Sieger für alle Modelle.

Wähle das System mit zwei Karten, wenn dir Folgendes wichtig ist:

- **Höhere Generierungsgeschwindigkeit bei GPT-OSS, Nemotron, Qwen3.5 und Qwen3.6** in diesem Test.
- **Höherer Durchsatz bei kurzen Kontexten** für die fünf Modelle.
- **Geringere Anschaffungskosten** als beim angebotenen GB10-System.
- **Softwarekompatibilität mit diskreten NVIDIA-GPUs** und künftige Modelltests.

Wähle den GB10, wenn dir Folgendes wichtig ist:

- **Qwen3.8 27B bei 256K**, wo der GB10 mehr als 20-mal schneller generiert.
- **Ein einzelner 128-GB-Speicherpool** mit mehr Platz für Modellgewichte, KV-Cache und Runtime-Puffer.
- **Geringere angegebene GPU- oder Chip-Leistung** als bei zwei separaten Karten.
- **Weniger Einschränkungen bei der Verteilung auf mehrere Geräte** für Modelle, die das System mit zwei Karten stark beanspruchen.

Das entspricht den Dimensionierungshinweisen in [Reichen 16 GB VRAM für anspruchsvolle lokale LLMs?](/articles/is-16gb-vram-enough-local-llm/), die Gewichte, Kontext und Runtime-Zuweisungen als gemeinsames Budget behandeln. Auch der [Leitfaden zu 32 GB VRAM für Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/) kommt bei Systemen mit zwei Karten zum selben Schluss. Die Gesamtkapazität entspricht nicht dem nutzbaren Spielraum.

Stelle dir vor dem Hardwarekauf für einen Einsatz mit langem Kontext vier Fragen:

- **Passt die gewünschte Quantisierung zusammen mit den Runtime-Puffern?** Die Modellgewichte allein bestimmen den Speicherbedarf nicht.
- **Passt der Kontext ohne starken Druck auf den KV-Cache?** Lange Prompts verändern das Ergebnis.
- **Teilt die Runtime die Arbeit effizient auf die Geräte auf?** PCIe-Transfers und Tensorplatzierung beeinflussen jedes erzeugte Token.
- **Bewältigt das System den Zielkontext vollständig?** Ein schnelles 4K-Ergebnis gleicht eine fehlgeschlagene 256K-Arbeitslast nicht aus.

**Der neue Benchmark beantwortet diese Fragen für jedes Modell.** Bei 256K spricht das Ergebnis klar für den GB10 bei Qwen3.8. Die anderen vier Modelle erzeugen in dieser konkreten Konfiguration auf dem System mit zwei Karten schneller. Der größere Unified-Memory-Pool bietet weiterhin mehr Kapazitätsreserve, selbst wenn er nicht den höchsten gemessenen Durchsatz erreicht.

Dieselbe Dual-GPU-Hardware erreichte bei 256K mit Flash-Next IQ2_XS auf Strata nach dem Aufwärmen außerdem einen Median von 92.8 Token pro Sekunde. Dieses separate Ergebnis widerlegt nicht den Befund für dichtes Qwen3.8 auf dem GB10. Flash-Next verwendet eine andere Mixture-of-Experts-Architektur, Quantisierung, Paketierung, Runtime und Dekodiermethode. In diesem Datensatz gibt es keinen entsprechenden Flash-Next-Wert für den GB10.

## Fazit

**Das System mit zwei RTX 5060 Ti generiert bei 256K für vier der fünf getesteten Modelle schneller.** Es kostet außerdem etwa halb so viel wie das angebotene GB10-System. Für Qwen3.8 27B bei 256K, mehr Speicherspielraum und Arbeitslasten, die von einem kohärenten Speicherpool profitieren, bleibt der GB10 die bessere Wahl.

Der frühere Test nur mit Qwen legte einen klaren Sieg des GB10 nahe. Der aktualisierte Lauf mit fünf Modellen zeigt, warum diese Schlussfolgerung zu allgemein war. Modellarchitektur, Runtime-Version, Tensorplatzierung und Kontextverhalten beeinflussen das Ergebnis.

Wenn du GPT-OSS, Nemotron 3.5 Lightning, Qwen3.5 oder Qwen3.6 ausführst, erzielte das System mit zwei Karten in diesem Benchmark eine höhere Generierungsgeschwindigkeit. Bei Qwen3.8 27B und 256K lieferte der GB10 eine nutzbare Geschwindigkeit, während das System mit zwei Karten beinahe zum Stillstand kam.

**Speicherkapazität und Durchsatz sind getrennte Kaufkriterien.** Der GB10 bietet die vierfache Gesamtspeichermenge und einen einfacheren gemeinsamen Arbeitssatz. Das System mit zwei Karten erzielt bei den meisten getesteten Modellen einen höheren beobachteten Durchsatz und kostet laut Angebot deutlich weniger.

Das Strata-Ergebnis zeigt einen zweiten Punkt. Runtime-Zuordnung, Modellarchitektur und Dekodiermodus veränderten das 256K-Ergebnis auf demselben Host mit zwei Karten. Flash-Next IQ2_XS hielt nach dem Aufwärmen einen Median nahe 93 Token pro Sekunde, während dichtes Qwen3.8 24 Layer auslagerte und auf unter ein Token pro Sekunde fiel.

## Grenzen des Benchmarks

Der Benchmark erfasst Modell-Tags, angeforderte Kontexte, tatsächliche Prompt-Token, Prompt-Verarbeitungs- und Generierungsgeschwindigkeit, Ollama-Versionen und das Generierungsziel von 128 Token. Nicht erfasst werden aufgelöste Manifest-Digests, CPU-Leistung, Leistungsaufnahme an der Steckdose, Lüfterdrehzahl oder Kühlkonfiguration.

Die GPT-OSS-Zeilen für 256K verarbeiteten auf beiden Systemen 65,538 tatsächliche Prompt-Token. Die übrigen 256K-Zeilen verarbeiteten etwa 171K tatsächliche Prompt-Token. Die Werte sind als beobachteter Systemvergleich zu verstehen, nicht als allgemeine Rangliste aller RTX-5060-Ti-Paare und GB10-Implementierungen.

Der Vergleich von Strata und dem dichten Modell erfasst genaue Prompt-Zahlen, fünf gemessene Anfragen pro Kontext, Runtime-Versionen, Geräteplatzierung, Cache-Einstellungen und Anfragestatus. Zugleich ändern sich Modellarchitektur, Quantisierung, Paketierung, Runtime und Dekodiermodus. Strata verwendete oberhalb von 32K außerdem Prompt-Präfixe wieder. Die gemessenen Generierungsanfragen beider Stacks verwendeten fast den gesamten Prompt erneut.

Eine exakte Reproduktion anhand dieses Artikels ist nicht möglich. Benchmark-Harness, Strata-Paketlayout, Expertenprofil und MTP-Draft-Paket wurden nicht mit unveränderlichen Digests veröffentlicht. Die Warnung zu niedrigem VRAM erhöht zudem das Risiko von Abweichungen zwischen Läufen. Der Test isoliert den Host, nicht die Inferenz-Engine.

Die obigen Hardwarespezifikationen stammen von NVIDIA. Die Leistungswerte stammen aus dem kontrollierten Benchmark-Lauf für diesen Artikel.

## Quellen

- [Ollama-Modellbibliothek Qwen3.8](https://ollama.com/library/qwen3.8)
- [ISTA-DASLab-Qwen3.8-Flash-Next-GSQ-RCO-GGUF-Modelle](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)
- [orcarouter-Qwen3.8-Flash-Next-Uncensored-GGUF-Modelle](https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF)
- [Ollama-Modellbibliothek Qwen3.5](https://ollama.com/library/qwen3.5)
- [Ollama-Modellbibliothek Qwen3.6](https://ollama.com/library/qwen3.6)
- [Ollama-Modellbibliothek Nemotron 3.5 Lightning](https://ollama.com/library/nemotron-3.5-lightning)
- [Ollama-GPT-OSS-Modell-Tags](https://ollama.com/library/gpt-oss/tags)
- [Reichen 16 GB VRAM für anspruchsvolle lokale LLMs?](/articles/is-16gb-vram-enough-local-llm/)
- [32 GB VRAM für Qwen 27B](/articles/32gb-vram-qwen-27b-hardware-guide/)
- [Leitfaden zu Kontexten lokaler KI-Modelle und GPUs](/articles/local-ai-model-gpu-context-guide/)
- [GPU-Benchmarks für Qwen3.8 27B auf Vast.ai](/articles/qwen38-27b-vast-ai-gpu-benchmark/)
- [Angebot einer kompletten Workstation mit zwei RTX 5060 Ti und 16 GB](https://greenbeastgaming.com/products/dual-gpu-rtx-5060-ti-16gb-intel-focus-g-white)
- [NVIDIA-DGX-Spark-Angebot im US-Marktplatz](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/)
- [Linux-Angebot für AMD Ryzen AI Halo mit 128 GB](https://www.microcenter.com/product/711961/amd-ryzen-ai-halo-developer-platform?osfs=false)
- [Tom's-Hardware-Test: Strix Halo gegen GB10](https://www.tomshardware.com/pc-components/gpus/embargo-mon-july-6-8am-pt-1100-edt-amd-ryzen-ai-halo-review/4)
- [Aktuelle RTX-5060-Ti-Preise](https://www.pcgamer.com/hardware/graphics-cards/graphics-card-price-watch-deals/)
