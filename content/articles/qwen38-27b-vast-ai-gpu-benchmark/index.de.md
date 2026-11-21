---
title: "Llama 3.1 8B und Qwen3.8 27B: GPU-Benchmarks auf Vast.ai"
date: 2026-10-02
lastmod: 2026-11-20
toc: true
draft: false
description: "Vergleiche gemessene Ollama-Ergebnisse für Llama 3.1 8B und Qwen3.8 27B auf Vast.ai-GPUs, ihre Kosten und Hosting-Optionen."
genre: ["Lokale KI", "GPU-Leistungstests", "Selbst gehostete KI", "Cloud-Infrastruktur", "Künstliche Intelligenz", "KI-Wirtschaft"]
tags: ["Llama 3.1 8B", "llama3.1:8b", "Qwen3.8 27B", "Qwen3.8:27b", "Vast.ai", "GPU-Leistungstest", "Ollama", "H100", "RTX PRO 5000", "RTX 6000 Ada", "RTX PRO 6000 Max-Q", "A100", "CMP 170HX", "lokale LLMs", "langer Kontext", "GPU-Miete", "selbst gehostete KI", "abliterierte Modelle", "ungefilterte Modelle", "API-Guthaben", "KI-Abonnement", "Q4_K_M", "Token pro Sekunde"]
cover: "/img/cover/local-ai-2026-qwen3-8-bonsai-2-27b-models.webp"
coverAlt: "Hightech-Arbeitsplatz mit Grafikkarte und Bildschirmen, die lokale KI-Benchmark-Ergebnisse zeigen"
coverCaption: ""
ref: ["/articles/local-ai-2026-build-your-rig-now", "/articles/ai-models-raspberry-pi-4-5"]
---

**Die H100 SXM war in beiden Ollama-Modelltests die schnellste Karte, bot aber nicht das beste Preis-Leistungs-Verhältnis.** Die RTX PRO 5000 und die RTX 6000 Ada erzielten ein besseres Verhältnis zwischen Geschwindigkeit und Mietkosten. Die CMP 170HX hatte unter den abgeschlossenen Qwen3.8-27B-Läufen den niedrigsten Stundensatz.

*Diese Ergebnisse messen ein Modell, einen Ollama-Wrapper, eine Standardquantisierung und ein Bereitstellungsmuster. Nutze sie zur Dimensionierung dieser Arbeitslast, nicht als allgemeines GPU-Ranking.*

Dieser Artikel vergleicht **Llama 3.1:8b**, einen Ollama-Build mit Q4_K_M und 8,03 Milliarden Parametern, mit **Qwen3.8:27b**, einem Ollama-Build mit Q4_K_M und ungefähr 27,3 Milliarden Parametern. Beide Modelle liefen auf GPU-Instanzen, die über Vast.ai gemietet wurden. Die Tests erfassten den Decode-Durchsatz bei tatsächlichen Prompt-Längen bis zur unterstützten Kontextgrenze.

## Kurzantwort

**Miete für regelmäßige Einzelbenutzer-Arbeit eine RTX PRO 5000 oder RTX 6000 Ada.** Die RTX PRO 5000 bot bei kurzem und mittlerem Kontext den besten Gegenwert. Die RTX 6000 Ada kostete weniger und lag weiterhin deutlich vor den A100-Karten. Miete eine H100 SXM, wenn Antwortgeschwindigkeit wichtiger ist als der Stundensatz oder lange Prompts zur Arbeitslast gehören.

| Ziel | Empfehlung | Begründung |
|---|---|---|
| **Niedrigste Testkosten** | CMP 170HX | 0,420 USD pro Stunde und genügend VRAM für die getesteten Q4_K_M-Modelle |
| **Bester Gegenwert unter 1,25 USD/h** | RTX PRO 5000 oder RTX 6000 Ada | Hohe Decode-Geschwindigkeit ohne H100-Mietkosten |
| **Schnellste Antworten** | H100 SXM | Höchste Decode-Geschwindigkeit in beiden Modelltests |
| **Qwen mit langem Kontext** | H100 SXM oder RTX PRO 6000 Max-Q | Beide schlossen den Qwen-Lauf mit ungefähr 131k Tokens und reichlich VRAM-Reserve ab |
| **Beliebte 8B-Baseline** | Llama 3.1:8b | Praktischer Vergleich für ein 8B-Modell mit 128K-Kontextgrenze |
| **Kleine, wiederkehrende Arbeitslast** | API-Guthaben oder Chat-Abonnement | Keine Leerlaufkosten für die GPU, keine Wartung und kein Bereitstellungsaufwand |
| **Private und häufige Nutzung** | Eigene GPU-Workstation | Bei anhaltender Auslastung lässt sich der Hardwarepreis leichter rechtfertigen |
| **Abliterierte oder ungefilterte Modelle testen** | Erst mieten, erst nach anhaltender Nutzung kaufen | Modellverhalten, Lizenzierung und Betriebsrisiken sollten vor dem Hardwarekauf separat geprüft werden |

## Was getestet wurde

**Der Benchmark nutzte Ollama mit dem standardmäßigen Q4_K_M-Modell-Build.** Es kamen keine spezielle Quantisierung, spekulative Dekodierung, eigenen Sampler oder zusätzlichen Bereitstellungs-Stacks zum Einsatz. Ziel war ein einfacher, lokal reproduzierbarer Vergleich der GPU-Instanzen.

Vast.ai beschreibt seinen Dienst als GPU-Cloud-Marktplatz, der Rechenanbieter und Nutzer verbindet. Die Dokumentation nennt On-Demand-, reservierte, unterbrechbare und serverlose Optionen sowie Suchfilter für GPU-Modell, Speicher, Preis und Verfügbarkeit. Die folgenden Stundensätze stammen von den für diese Benchmark-Sitzung ausgewählten Instanzen, nicht aus einer dauerhaft gültigen Vast.ai-Preisliste.

Die gemessene Ausgabe war der **Decode-Durchsatz**, angegeben als erzeugte Tokens pro Sekunde. Der Prefill-Durchsatz steht separat, weil er die Prompt-Verarbeitung und nicht die Geschwindigkeit der Antwortanzeige beschreibt. Ein langer Prompt benötigt oft viel Verarbeitungszeit, auch wenn die Decode-Geschwindigkeit hoch bleibt.

Der Benchmark verwendete zwei gültige Versuche pro Kontext und erfasste den Median des Decode-Ergebnisses. Die abgeschlossenen Prompt-Stufen basierten auf tatsächlichen `prompt_eval_count`-Werten:

- **Ungefähr 16,4k Prompt-Tokens**
- **Ungefähr 32,8k Prompt-Tokens**
- **Ungefähr 65,5k Prompt-Tokens**
- **Ungefähr 131k Prompt-Tokens**

Der angeforderte Lauf mit 256k Tokens wurde nicht abgeschlossen. Die A100-Karten mit 40 GB und mehrere kleinere Karten verarbeiteten den Prompt noch oder erreichten die Ziel-Kontextlänge nicht.

> **Benchmark-Grenze:** Die Werte beschreiben zwei Ollama-Q4_K_M-Arbeitslasten mit einem Bereitstellungsmuster. Sie sagen nichts über Trainingsgeschwindigkeit, Durchsatz für mehrere Nutzer, Bildgenerierung, vLLM-Leistung oder Ergebnisse anderer Modelle aus.

## Llama 3.1 8B erneut getestet

**Llama 3.1:8b bietet eine nützliche praktische Baseline für denselben GPU-Pool.** Ollama führt das Modell mit ungefähr 120 Millionen Downloads auf. Damit eignet es sich als zweite Benchmark-Referenz nach Popularität. Auf der [offiziellen Ollama-Modellseite](https://ollama.com/library/llama3.1:8b) sind ein 4,9-GB-Q4_K_M-Build, 8,03 Milliarden Parameter und ein 128K-Kontextfenster angegeben.

Der erneute Test verwendete einen modellspezifischen Benchmark-Runner und stimmte den Prompt-Generator auf den Ollama-Tokenizer ab. Die folgenden Beschriftungen verwenden tatsächliche Prompt-Zahlen statt der angeforderten Kontexteinstellungen:

- **Ungefähr 32.676 tatsächliche Prompt-Tokens** für das 32k-Ziel
- **Ungefähr 65.342 tatsächliche Prompt-Tokens** für das 64k-Ziel
- **Ungefähr 130.671 tatsächliche Prompt-Tokens** für das 128k-Ziel

Die Stufe mit 256k wird für Llama 3.1 8B ausdrücklich nicht unterstützt, weil die angegebene Kontextgrenze des Modells 128K beträgt. Der Runner ergänzte Wiederholungsversuche und Statuszeilen. Eine Zeitüberschreitung bleibt dadurch in der Tabelle sichtbar, statt aus ihr zu verschwinden.

### Ergebnisse für Llama 3.1 8B

| GPU | ~32k Decode-Tokens/s | ~64k Decode-Tokens/s | ~128k Decode-Tokens/s |
|---|---:|---:|---:|
| **H100 SXM** | **163.5** | **124.0** | **82.4** |
| **H100 SXM** | **158.6** | **121.2** | **80.6** |
| **RTX PRO 5000** | 110.1 | 79.8 | 49.9 |
| **CMP 170HX 64GB** | 91.9 | 71.0 | 50.1 |
| **RTX 6000 Ada** | 88.3 | 53.9 | 29.3 |
| **RTX PRO 6000 Max-Q** | 66.7 | 53.0 | 40.3 |
| **RTX PRO 6000 S** | 60.3 | 42.5 | 33.9 |
| **A100 SXM4 40GB** | 2.0 | 40.6 | 38.5 |
| **A100 PCIe 40GB** | 1.2 | 20.3 | 20.3 |
| **2x RTX 5060 Ti** | 1.3 | 26.8 | Zeitüberschreitung |

Die beiden H100-Zeilen stammen von separaten, gültigen Instanzen derselben GPU-Klasse. Beide lagen deutlich vor den anderen Karten. Bei 32k waren ihre Ergebnisse 44 % bis 48 % schneller als die RTX PRO 5000. Bei 128k betrug der Vorsprung ungefähr 61 % bis 65 %.

Die Ergebnisse der A100- und RTX-5060-Ti-Karten bei 32k sind für diese Arbeitslast keine vergleichbaren GPU-Ausführungen, weil sie zu niedrig ausfallen. Der Host mit RTX 5060 Ti lief außerdem beim zweiten Versuch mit 128k in eine Zeitüberschreitung. Behandle den Host als ungeeignet für gültige GPU-Durchsatzvergleiche und nicht als echtes Ranking-Ergebnis.

| Kontextziel | Ergebnis |
|---|---|
| **32k** | Auf allen 10 Hosts abgeschlossen |
| **64k** | Auf allen 10 Hosts abgeschlossen |
| **128k** | Auf 9 Hosts abgeschlossen. Der Host mit 2x RTX 5060 Ti lief beim zweiten Versuch in einen Timeout |
| **256k** | Auf allen Hosts nicht unterstützt, da Llama 3.1 8B bis zu 128K Kontext unterstützt |

## Die beiden Modelle vergleichen

**Das kleinere Llama-Modell war auf jeder vergleichbaren GPU schneller, doch Modellgröße und Qualität sind nicht dasselbe.** Llama 3.1 8B eignet sich als beliebte Baseline mit geringerem Speicherbedarf. Qwen3.8 27B benötigt mehr Speicher und bietet ein anderes Fähigkeitsprofil. Die Zahlen sollten deshalb die Hardwareauswahl leiten, aber kein Modell allgemein zum besseren erklären.

| Anwendungsfall | Geeignete Benchmark-Referenz | Warum |
|---|---|---|
| **Schneller 8B-Assistent** | Llama 3.1:8b | Höhere Decode-Geschwindigkeit und geringerer Speicherbedarf des Modells |
| **Dimensionierung eines lokalen 27B-Modells** | Qwen3.8:27b | Repräsentativer für eine größere Arbeitslast auf einer einzelnen GPU |
| **128K-Kontextgrenze** | Llama 3.1:8b | Das Modell hat eine angegebene Grenze von 128K, daher ist 256k kein gültiges Ziel |
| **VRAM-Reserve testen** | Qwen3.8:27b | Das größere Modell macht Speicher- und Langkontextgrenzen früher sichtbar |
| **Anbieterübergreifende Baseline** | Llama 3.1:8b | Popularität und Modellgröße machen das Ergebnis leichter reproduzierbar |

Der frühere Qwen-Test korrigierte außerdem die tatsächlichen Prompt-Zahlen auf ungefähr **32.770**, **65.538** und **131.074** Tokens für die unterstützten Kontextstufen. Beim Vergleich von Qwen-Läufen ersetzen diese korrigierten Beschriftungen die angeforderten `num_ctx`-Werte.

## Ungefähr 16k Tokens

**Die H100 SXM führte den Lauf mit kurzem Kontext mit 134,4 Decode-Tokens pro Sekunde an.** Die RTX PRO 5000 folgte mit 113,9 Tokens pro Sekunde bei weniger als der Hälfte des Stundensatzes.

| Rang | GPU | VRAM | Decode-Tokens/s | Prompt-Verarbeitung Tokens/s | Mietpreis |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **134.4** | 89,974 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **113.9** | 68,726 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **89.1** | 95,856 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **84.1** | 72,235 | $1.507/hr |
| 5 | **A100 SXM4** | 40 GB | **60.6** | 53,048 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **51.5** | 51,122 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **49.3** | 52,773 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | **38.4** | 38,886 | $0.565/hr |

Bei dieser Prompt-Länge erreichte die RTX PRO 5000 ungefähr 84,7 % des H100-Decode-Durchsatzes bei 37,3 % des Stundensatzes. Die RTX 6000 Ada erreichte ungefähr 66,3 % der H100-Geschwindigkeit bei 30,2 % des Stundensatzes.

## Ungefähr 32,8k Tokens

**Das Ranking blieb beim Lauf mit mittlerem Kontext stabil.** Die H100 SXM erreichte 120,0 Tokens pro Sekunde, die RTX PRO 5000 105,0 und die RTX 6000 Ada 75,7.

| Rang | GPU | VRAM | Decode-Tokens/s | Prompt-Verarbeitung Tokens/s | Mietpreis |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **120.0** | 139,748 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **105.0** | 103,707 | $1.005/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **75.7** | 141,678 | $0.813/hr |
| 4 | **RTX PRO 6000 Max-Q** | 95.6 GB | **66.9** | 120,537 | $1.507/hr |
| 5 | **RTX PRO 6000 S** | 95.6 GB | **65.9** | 109,280 | $1.756/hr |
| 6 | **A100 SXM4** | 40 GB | **51.1** | 81,929 | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | **46.2** | 77,984 | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | **36.1** | 73,377 | $0.565/hr |

Die RTX PRO 5000 blieb in dieser Gruppe die attraktivste Mietoption. Sie war nur 12,5 % langsamer als die H100, kostete aber 62,7 % weniger pro Stunde.

## Ungefähr 65,5k Tokens

**Längere Prompts zeigten einen größeren Abstand zwischen Karten mit viel Speicher und Karten mit geringerer Reserve.** Die H100 blieb mit 112,0 Tokens pro Sekunde an erster Stelle. Die RTX PRO 6000 Max-Q überholte die RTX 6000 Ada beim Decode-Durchsatz.

| Rang | GPU | VRAM | Decode-Tokens/s | Prompt-Verarbeitung Tokens/s | Mietpreis |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **112.0** | 195,252 | $2.693/hr |
| 2 | **RTX PRO 5000** | 47.8 GB | **96.9** | 148,897 | $1.005/hr |
| 3 | **RTX PRO 6000 Max-Q** | 95.6 GB | **75.7** | 156,443 | $1.507/hr |
| 4 | **RTX 6000 Ada** | 48 GB | **70.8** | 208,400 | $0.813/hr |
| 5 | **A100 SXM4** | 40 GB | **49.3** | 147,699 | $0.680/hr |
| 6 | **CMP 170HX** | 64 GB | **45.9** | 118,657 | $0.420/hr |
| 7 | **RTX PRO 6000 S** | 95.6 GB | **37.0** | 124,927 | $1.756/hr |
| 8 | **A100 PCIe** | 40 GB | n. v. | n. v. | $0.565/hr |

Die RTX PRO 5000 bot weiterhin die beste Balance in der abgeschlossenen Tabelle. Die RTX 6000 Ada war langsamer als die RTX PRO 5000, aber ihr niedrigerer Mietpreis machte sie für Budgets attraktiv, bei denen Verfügbarkeit wichtiger ist als Spitzenleistung.

## Ungefähr 131k Tokens

**Bei dieser Kontextlänge überschritt nur die H100 100 Decode-Tokens pro Sekunde.** Die RTX PRO 6000 Max-Q schloss den Lauf mit 73,4 Tokens pro Sekunde ab. Es folgte die RTX 6000 Ada mit 61,7.

| Rang | GPU | VRAM | Decode-Tokens/s | Prompt-Verarbeitung Tokens/s | Mietpreis |
|---:|---|---:|---:|---:|---:|
| 1 | **H100 SXM** | 79.6 GB | **108.2** | 242,093 | $2.693/hr |
| 2 | **RTX PRO 6000 Max-Q** | 95.6 GB | **73.4** | 197,208 | $1.507/hr |
| 3 | **RTX 6000 Ada** | 48 GB | **61.7** | 278,283 | $0.813/hr |
| 4 | **RTX PRO 6000 S** | 95.6 GB | **39.4** | 124,653 | $1.756/hr |
| 5 | **RTX PRO 5000** | 47.8 GB | n. v. | n. v. | $1.005/hr |
| 6 | **A100 SXM4** | 40 GB | n. v. | n. v. | $0.680/hr |
| 7 | **CMP 170HX** | 64 GB | n. v. | n. v. | $0.420/hr |
| 8 | **A100 PCIe** | 40 GB | n. v. | n. v. | $0.565/hr |

Die RTX PRO 6000 Max-Q war bei langen Prompts die praktische Alternative zur H100. Sie erreichte 67,8 % der H100-Decode-Geschwindigkeit bei 56,0 % des Stundensatzes. Die RTX 6000 Ada kostete weniger, doch ihre 48 GB VRAM lassen weniger Spielraum für lange Prompts, größere Batches oder eine andere Modellkonfiguration.

## Gesamter Dekodiervergleich

| GPU | ~16k | ~32,8k | ~65,5k | ~131k |
|---|---:|---:|---:|---:|
| **H100 SXM** | **134.4** | **120.0** | **112.0** | **108.2** |
| **RTX PRO 5000** | 113.9 | 105.0 | 96.9 | n. v. |
| **RTX 6000 Ada** | 89.1 | 75.7 | 70.8 | 61.7 |
| **RTX PRO 6000 Max-Q** | 84.1 | 66.9 | 75.7 | 73.4 |
| **RTX PRO 6000 S** | 49.3 | 65.9 | 37.0 | 39.4 |
| **A100 SXM4** | 60.6 | 51.1 | 49.3 | n. v. |
| **CMP 170HX** | 51.5 | 46.2 | 45.9 | n. v. |
| **A100 PCIe** | 38.4 | 36.1 | n. v. | n. v. |

**Die H100 lag bei jeder abgeschlossenen Kontextlänge vorn.** Ihr Vorsprung vor der RTX PRO 5000 schrumpfte von 20,5 Tokens pro Sekunde bei ungefähr 16k Tokens auf 12,0 bei ungefähr 32,8k Tokens. Welches Gerät den besten Gegenwert bietet, hängt davon ab, ob du die schnellste erste Antwort oder die niedrigsten Kosten für eine lange Sitzung brauchst.

## Kosten pro Million generierte Tokens

**Der Stundensatz allein zeigt nicht den nützlichen Vergleich.** Wenn man ihn durch den Decode-Durchsatz teilt, ergibt sich eine grobe Mietkostenschätzung für eine Million erzeugte Tokens. Prompt-Verarbeitung, Leerlaufzeit, Speicherplatz, Datenübertragung, Steuern, Rabatte und fehlgeschlagene oder unterbrochene Läufe sind darin nicht enthalten.

| GPU | Preis für kurzen Kontext | Ungefähre Kosten pro 1 Mio. Decode-Tokens |
|---|---:|---:|
| **CMP 170HX** | $0.420/hr | $2.27 |
| **RTX PRO 5000** | $1.005/hr | $2.45 |
| **RTX 6000 Ada** | $0.813/hr | $2.53 |
| **A100 SXM4** | $0.680/hr | $3.12 |
| **A100 PCIe** | $0.565/hr | $4.09 |
| **RTX PRO 6000 Max-Q** | $1.507/hr | $4.98 |
| **H100 SXM** | $2.693/hr | $5.57 |
| **RTX PRO 6000 S** | $1.756/hr | $9.89 |

**Die CMP 170HX gewann diesen eng gefassten Rechenvergleich.** Die RTX PRO 5000 und die RTX 6000 Ada lagen knapp dahinter und boten beide mehr Durchsatz als die CMP 170HX. Bei interaktiver Nutzung ist die zusätzliche Wartezeit oft wichtiger als die niedrigsten Tokenkosten.

## Mieten, Guthaben kaufen, abonnieren oder Hardware kaufen?

**Die passende Option hängt von Auslastung und Kontrollbedarf ab.** Eine GPU-Miete erzeugt variable Rechenkosten. API-Guthaben führt zu variablen Modellkosten. Ein Chat-Abonnement ist eine feste Zugangsgebühr mit Nutzungslimits. Eigene Hardware ist eine Investition mit zusätzlichen Kosten für Strom, Kühlung, Wartung und Wertverlust.

| Monatsbudget und Arbeitslast | Empfohlener Weg | Warum | Wichtigster Kompromiss |
|---|---|---|---|
| **Unter $10** | API-Guthaben kaufen oder ein kostenloses lokales Modell nutzen | Beweist den Arbeitsablauf ohne Leerlaufkosten für eine GPU | Weniger Kontrolle über Modellhosting und Ratenbegrenzungen |
| **$10 bis $30** | API-Guthaben für gelegentliche Aufgaben oder ein Chat-Abonnement für tägliche interaktive Nutzung | Ein Abonnement passt zu menschlichem Chat, Guthaben zu Skripten und gemessenen Aufrufen | Keine der Optionen bietet standardmäßig einen privaten 27B-Endpunkt |
| **$30 bis $100** | Eine RTX 6000 Ada oder RTX PRO 5000 nur während aktiver Sitzungen mieten | Das Budget deckt kurze Rechercheläufe ab und vermeidet Eigentumskosten | Die Instanz braucht weiterhin Einrichtung, Speicher, Überwachung und konsequentes Abschalten |
| **$100 bis $250** | Für geplante Arbeit eine schnelle Karte mieten oder ein eigenes Workstation-Konzept testen | Bei anhaltender monatlicher Nutzung wird die Auslastung sichtbar | Mietverfügbarkeit und Stundensätze ändern sich |
| **$250 bis $600** | Einen Monat RTX-PRO-5000-Miete mit einer gebrauchten oder neuen lokalen GPU vergleichen | Hier fällt die Entscheidung bei häufiger privater Inferenz | Hardware verursacht Strom-, Wärme-, Support- und Wiederverkaufsrisiken |
| **Über $600** | Hardware nur bei hoher Auslastung kaufen oder eine H100-Miete für Lastspitzen reservieren | Eine Mischstrategie vermeidet den Besitz einer Spitzenkarte für gelegentlichen Bedarf | Kapital bleibt in einer Konfiguration gebunden |

Diese Bereiche sind Entscheidungshilfen, keine Anbieterangebote. Die Benchmark-Raten zeigen den wichtigsten Break-even-Punkt: Eine H100 für $2.693 pro Stunde kostet bei durchgehendem Betrieb ungefähr $64.63 pro Tag und ungefähr $1,941.00 für 30 Tage, noch ohne Speicher oder weitere Gebühren. Eine RTX PRO 5000 für $1.005 pro Stunde kostet ungefähr $24.12 pro Tag und $723.60 für 30 Tage Dauerbetrieb. Eine GPU, die nur während aktiver Sitzungen gemietet wird, hat andere Gesamtkosten als eine GPU, die den ganzen Monat läuft.

### Wann API-Guthaben sinnvoll ist

**API-Guthaben eignet sich bei unregelmäßiger Nutzung, Automatisierung und Aufgaben ohne ein bestimmtes lokales Modell.** Es erspart GPU-Bereitstellung, Modelldownloads, Treiberprobleme und Leerlaufzeit. Außerdem kannst du mehrere gehostete Modelle vergleichen, bevor du Hardware anschaffst.

API-Preise unterscheiden sich je nach Modell und Anbieter. Der Modellkatalog von OpenRouter dient dem Vergleich von Kontextgrößen, Anbietern und Tokenpreisen. Prüfe die aktuellen Angaben des Anbieters, bevor du eine API-Rechnung mit diesem Benchmark vergleichst. Eine lokale GPU erzeugt Tokens ohne Gebühr pro Token durch einen Anbieter, doch der Mietstundensatz läuft weiter, solange die Instanz wartet.

### Wann ein Abonnement sinnvoll ist

**Ein Abonnement passt zu Personen, die täglich einen gehosteten Assistenten nutzen.** Die aktuellen Einzelabonnements von Claude unterscheiden zum Beispiel zwischen kostenlosem Zugang, Pro und Max mit verschiedenen Nutzungslimits und Funktionen. Ein Abonnement ist nicht dasselbe wie API-Zugang. Es bietet oft eine ausgefeilte Oberfläche und gebündelte Werkzeuge, während API-Guthaben programmatische Kontrolle ermöglicht.

Wähle ein Abonnement, wenn du überwiegend interaktiv schreibst, recherchierst, programmierst oder Dateien prüfst. Wähle API-Guthaben, wenn ein Skript, eine Anwendung oder ein Agent einen nutzungsabhängigen Endpunkt braucht.

### Wann Vast.ai sinnvoll ist

**Vast.ai eignet sich, wenn du ein offenes Modell, private Laufzeitkontrolle oder einen kurzen Schub hohen Durchsatzes brauchst.** Du wählst die GPU aus, startest eine Instanz, führst Ollama aus, testest ein Modell und schaltest die Instanz danach ab. Das passt gut zu Qwen3.8 27B, abliterten Varianten und anderen Modelldateien, die nicht auf ein übliches Consumer-Notebook passen.

Dafür fällt Betriebsaufwand an. Prüfe, ob das Modell tatsächlich die GPU nutzt, überwache den VRAM, sichere den erreichbaren Dienst, bewahre benötigte Modelldateien auf und stoppe die Instanz nach dem Lauf. Ein niedriger Stundensatz verhindert keine vergessene Instanz.

### Wann sich der Kauf einer GPU lohnt

**Eigene Hardware lohnt sich bei anhaltender Nutzung, stabilen Modellanforderungen und Bedarf an lokaler Kontrolle.** Der Kauf beseitigt das Verfügbarkeitsrisiko bei der Miete und schafft eine dauerhafte Umgebung. Außerdem lassen sich private Daten lokal verarbeiten, ohne Prompts an einen gehosteten Anbieter zu senden.

Der Kaufpreis ist nur ein Teil der Kosten. Rechne Hostsystem, Netzteil, Speicher, Kühlung, Strom, Ausfallrisiko und den Wert deiner Einrichtungszeit hinzu. Eine hochwertige Karte steht auch dann ungenutzt herum, wenn API-Guthaben oder ein Abonnement günstiger wären.

In den Referenzangaben von NVIDIA zur RTX 4090 stehen 24 GB Speicher, eine Gesamtgrafikleistung von 450 W und eine empfohlene Mindestleistung des Systems von 850 W. Das ist ein nützlicher Bezugspunkt für lokale Inferenz, doch die 24 GB liegen unter der Kapazität der hier getesteten Q4_K_M-Konfigurationen mit 27B-Modellen. Prüfe den tatsächlichen Speicherbedarf des Modells, statt allein aus der Parameterzahl abzuleiten, dass es auf eine Karte passt.

## Abliterierte und ungefilterte Modelle

**Abliterierte und ungefilterte Modellvarianten verändern die Kaufentscheidung.** Ihr Reiz liegt oft in weniger Ablehnungsverhalten oder weniger eingebauten Einschränkungen. Zu den Kosten zählen schwächeres Sicherheitsverhalten, unklare Herkunft, inkonsistente Prompt-Formate, höherer Prüfaufwand sowie mögliche Lizenz- oder Nutzungsbeschränkungen.

Miete diese Modelle, bevor du sie kaufst. Ein eintägiger Test mit einer RTX PRO 5000 kostet beim angegebenen Satz ungefähr $24.12 vor weiteren Gebühren. Damit lassen sich Modellpassung, GPU-Nutzung, Antwortqualität und Betriebsrisiken prüfen.

**Stelle ein ungefiltertes Modell nicht direkt ins öffentliche Internet.** Schalte Authentifizierung, Ratenbegrenzungen, Protokollierung und Netzwerkisolierung davor. Sende keine persönlichen, vertraulichen oder regulierten Daten an eine Modellquelle, die du nicht geprüft hast.

Wenn das Modell zum täglichen Werkzeug wird, vergleiche die monatliche Miete mit den Gesamtkosten einer eigenen Workstation. Bei gelegentlicher Nutzung lässt sich die Miete einfacher beenden und ersetzen.

## Einschränkungen des Benchmarks

**Fehlende Ergebnisse gehören zum Ergebnis.** Ein Wert `n. v.` bedeutet, dass der Lauf keine gültige Messung ergab. Er bedeutet nicht, dass die GPU entsprechend dem Wert einer anderen Karte langsam ist.

- **Die zweite H100-Instanz lieferte keinen gültigen Benchmark-Satz**, weil der Modelldownload zu spät abgeschlossen wurde.
- **Die Instanz mit 2x RTX 5060 Ti wurde ausgeschlossen**, weil Ollama das Modell auf der CPU statt auf den GPUs ausführte.
- **Der Qwen3.8-27B-Prompt mit 256k Tokens wurde nicht abgeschlossen.** Die höchste gültige Stufe lag bei ungefähr 131k tatsächlichen Prompt-Tokens. Llama 3.1 8B weist 256k als nicht unterstützt aus, da die Kontextgrenze bei 128K liegt.
- **Der angeforderte `num_ctx`-Wert diente nicht als Ranking-Beschriftung.** Die endgültigen Tabellen verwenden tatsächliche `prompt_eval_count`-Werte.
- **Für jeden Kontext wurden zwei gültige Versuche mit dem Median des Decode-Ergebnisses zusammengefasst.** Das reduziert den Einfluss eines langsamen Laufs, ersetzt aber keine größere Testreihe.
- **Der Wrapper war bewusst einfach gehalten.** Eine optimierte vLLM- oder llama.cpp-Bereitstellung führt zu einem anderen Ranking.

## Abschließende Empfehlung

**Beginne mit einer Miete für die RTX 6000 Ada oder RTX PRO 5000.** Die RTX 6000 Ada ist die Budgetwahl, wenn ihr Stundensatz von $0.813 verfügbar ist. Die RTX PRO 5000 bietet unterhalb des H100-Preises mehr Geschwindigkeit. Nutze die H100 SXM für lange Prompts, anspruchsvolle interaktive Latenz oder kurze Benchmark-Zeiträume, in denen Zeit wichtiger ist als Mietkosten. Bei einem 8B-Modell lohnt sich ein Test der CMP 170HX, wenn der niedrigere Stundensatz wichtiger ist als Spitzenleistung.

**Kaufe keine GPU nach einem einzigen erfolgreichen Test.** Miete einen Monat lang für echte Arbeitslasten, protokolliere aktive Stunden, Prompt-Längen, Gleichzeitigkeit und Modelländerungen und vergleiche dann die Mietsumme mit den vollständigen Eigentumskosten. Kaufe Hardware, wenn die Arbeitslast häufig genug ist, um die Karte auszulasten, und stabil genug, um den Verlust an Flexibilität zu rechtfertigen.

Für gelegentliche Arbeit sind API-Guthaben oder ein Chat-Abonnement einfacher. Für private lokale Inferenz, Experimente mit offenen Modellen oder Tests abliterierter Modelle bietet Vast.ai einen Weg mit geringerer Bindung als der sofortige Kauf einer Workstation. Nutze Llama 3.1 8B als Baseline mit geringerem Speicherbedarf und Qwen3.8 27B, wenn das größere Modell tatsächlich das Bereitstellungsziel ist.

## Nächste Schritte

Wiederhole den Vergleich mit deinen eigenen Prompt-Längen und einer Schätzung der aktiven Stunden. Prüfe die GPU-Nutzung, notiere Modellrevision und Laufzeitversion, stoppe die Instanz nach jedem Lauf und vergleiche vor dem Kauf die monatliche Miete mit den vollständigen Eigentumskosten.

## Quellen

1. [Vast.ai-GPU-Cloud-Marktplatz](https://vast.ai/)
2. [Vast.ai-Dokumentation: Marktplatz, Instanzen, Preise und Mietarten](https://docs.vast.ai/)
3. [Ollama-Qwen3-Modellbibliothek](https://ollama.com/library/qwen3)
4. [Ollama-Modellseite für Llama 3.1 8B](https://ollama.com/library/llama3.1:8b)
5. [OpenRouter-Modellkatalog und Preisvergleich](https://openrouter.ai/models)
6. [Claude-Preise und Einzelabonnements](https://www.anthropic.com/pricing)
7. [NVIDIA-Spezifikationen zur GeForce RTX 4090](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/)
8. [Lokale KI 2026: Qwen3.8 27B und Hardware für selbst gehostete Modelle](/articles/local-ai-2026-build-your-rig-now/)
9. [Ollama-Modelltests auf Raspberry-Pi-Hardware](/articles/ai-models-raspberry-pi-4-5/)
