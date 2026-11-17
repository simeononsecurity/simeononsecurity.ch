---
title: "Welche KI-Modelle laufen auf einem Raspberry Pi 4 oder 5?"
date: 2026-09-20
lastmod: 2026-11-07
toc: true
draft: false
description: "Nutze Messwerte vom Raspberry Pi 4 und 5, um lokale Sprachmodelle nach Speicher, Geschwindigkeit und Arbeitslast auszuwählen, von kleinen LFM2.5-Modellen bis zu Optionen ab 3B."
genre: ["Raspberry Pi", "Künstliche Intelligenz", "Self-Hosting"]
tags: ["Raspberry Pi 4", "Raspberry Pi 5", "lokale KI", "kleine Sprachmodelle", "Ollama", "GGUF", "LFM2.5", "Qwen2.5", "Gemma 3", "Modellquantisierung", "Edge-KI"]
cover: "/img/cover/raspberry-pi-4-5-local-ai-models.webp"
coverAlt: "Zwei Raspberry-Pi-Computer auf einem dunklen Schreibtisch mit blauen und bernsteinfarbenen Darstellungen neuronaler Netze darüber"
coverCaption: "Illustration lokaler KI-Modelle auf Raspberry-Pi-Hardware."
---

Ein Raspberry Pi kann ein nützliches Sprachmodell lokal ausführen. Das Modell muss jedoch in den Arbeitsspeicher des Boards passen und eine Antwortzeit erreichen, die deine Anwendung verkraftet. Ein Raspberry Pi 4 mit 2 GB eignet sich am besten für Modelle mit weniger als ungefähr einer Milliarde Parametern. Ein Raspberry Pi 5 mit 8 GB führt kompakte 1B–3B-Modelle komfortabel aus und kann einige größere quantisierte Modelle mit erheblichen Kompromissen laden.

Wir haben diese Modelle selbst mit Ollama auf einem **Pi 4B mit 2 GB** und einem **Pi 5 mit 8 GB** getestet, beide mit microSD-Speicher. Die Messungen in den Tabellen nutzten dieselben fünf kurzen Assistenten-Prompts, denselben System-Prompt, einen festen Seed und eine Ausgabelimitierung auf 140 Token. Vor jedem Test entluden wir andere Modelle. Wir erfassten die Kaltstart-Ladezeit, die Zeit bis zum ersten sichtbaren Token, die gesamte Antwortzeit, die Ausgabegeschwindigkeit und den Spitzenwert des residenten Speichers. Es waren Einzeltests mit einer Arbeitslast für kurze Antworten. Die Ergebnisse sind daher Beispiele zur Dimensionierung, keine allgemeingültigen Ranglisten für Geschwindigkeit oder Antwortqualität. Die [Cortex-A76-CPU und verfügbaren Speicherkonfigurationen des Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) unterscheiden sich zudem deutlich von der [Cortex-A72-Plattform des Pi 4](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf).

## Welche Modelltypen sinnvoll sind

| Modelltyp | Beispiele aus den Messungen | Praktische Verwendung |
|---|---|---|
| Kleine Textmodelle mit etwa 230M–600M Parametern | LFM2.5-230M, LFM2.5-350M, Qwen2.5-0.5B | Kurze lokale Befehle, Zusammenfassungen und eingeschränkte Fragen; bester Einstieg für einen Pi 4 mit 2 GB |
| Kompakte Textmodelle mit etwa 1B–2B | LFM2.5-1.2B, Qwen2.5-1.5B, Gemma 3 1B, MiniCPM5-1B | Mehr Platz für nuancierte Anweisungen auf einem Pi 5 oder Pi 4 mit mehr Speicher, aber langsamer als die kleinsten Modelle |
| Quantisierte Textmodelle mit 3B–4B | Qwen2.5-3B, Llama 3.2 3B, Gemma 3 4B | Leistungsfähigere Kandidaten für einen Pi 5 mit 8 GB, wenn mehrere Sekunden Wartezeit pro Antwort akzeptabel sind |
| Größere sparsame oder hybride Modelle | LFM2.5 8B | Auf dem getesteten Pi 5 mit 8 GB technisch ausführbar, aber mit hohem Speicherbedarf und langer Kaltstart-Ladezeit |

Diese Ergebnisse beziehen sich auf **Textgenerierung**. Sie belegen keine Leistung bei Bilderzeugung, Spracherkennung, Bildverarbeitung oder Training. „Läuft“ bedeutet mehr als nur, dass die Modelldatei auf die Karte passt: Auch Laufzeitumgebung, Kontextcache, Betriebssystem und andere Dienste benötigen RAM. Quantisierung verkleinert die Gewichtedatei, kann aber die Antwortqualität senken, besonders bei extremen Einstellungen wie 1-Bit-Gewichten.

### Was unsere Zahlen messen

Der Benchmark schickte kurze Faktenfragen, Prompts zur Verfahrenssicherheit, Fragen mit abgerufenem Kontext, eine Wetterfrage und eine Hilfsanfrage an Ollamas Chat-API. Jedes Modell erhielt denselben Prompt-Satz und Seed. Vor der Zeitmessung entluden wir das Modell, damit der nächste Aufruf einen Kaltstart enthielt. Die angegebene **Echtzeit** umfasst die gesamte Anfrage; **Token pro Sekunde** beschreibt nur die Ausgabeerzeugung. Wir erfassten auch das erste *sichtbare* Token, da ein Modell Zeit mit Schlussfolgern verbringen kann, bevor es antwortet.

Für den Speicher erfassten wir während jeder Anfrage den verfügbaren RAM und Swap des Pi sowie den residenten Speicher von Ollama und des Inferenzprozesses. Die **RSS**-Werte beziehen sich auf den residenten Prozessspeicher, nicht auf den gesamten Speicherbedarf des Hosts. Dateiseiten, Betriebssystem, Browser oder ein anderer lokaler Dienst können trotzdem zu Swap führen, auch wenn das Modell nominell hineinpasst. Die Tabellen verwenden die ursprünglichen Einzelläufe mit fünf Prompts. Später erweiterten wir den Testaufbau um einen Nachrichtenprompt und Prüfungen der Antwortregeln. Diese Prüfungen zeigen, worauf es ankommt, machen aus den früheren Zeitmessungen aber keine Ergebnisse für sechs Compliance-Prompts.

Token pro Sekunde und Parameterzahl sind keine Qualitätswerte. Ein Modell kann schnell Text ausgeben und trotzdem eine angeforderte Quelle weglassen, das Wortlimit überschreiten oder einen Satz unvollendet lassen. Wir würden Modelle mit den Prompts vergleichen, die wir tatsächlich einsetzen wollen, und die Antworten prüfen, bevor wir eines für eine Anwendung auswählen.

## Raspberry Pi 4: möglichst kleine Modelle wählen

Der getestete Pi 4 mit 2 GB hatte nur wenig Speicherreserve. Die kleinsten LFM2.5-Modelle erledigten alle fünf Prompts, ebenso `qwen2.5:0.5b`. Sie eignen sich für kurze Offline-Antworten oder einen kleinen lokalen Assistenten.

| Modell | Modelldatei | Gemessene Ausgabegeschwindigkeit | Durchschnittliche Antwortzeit | Beobachteter Speicher oder Ergebnis |
|---|---:|---:|---:|---|
| LFM2.5-230M, importiertes GGUF | 0.25 GB | 12.8 Token/s | 7.2 s | Spitzen-RSS 383 MB; 5/5 Prompts |
| LFM2.5-350M, importiertes GGUF | 0.38 GB | 8.6 Token/s | 8.6 s | Spitzen-RSS 516 MB; 5/5 Prompts |
| `qwen2.5:0.5b` | 0.40 GB | 8.0 Token/s | 9.7 s | 5/5 Prompts; direkt in Ollama verfügbar |
| MiniCPM5-1B, importiertes GGUF, Schlussfolgern aus | 0.69 GB | 5.9 Token/s | 12.2 s | Spitzen-RSS 883 MB; 5/5 Prompts |
| MiniCPM5-1B, importiertes GGUF, Schlussfolgern standardmäßig | 0.69 GB | 5.7 Token/s | 33.3 s | Nur 1/5 Prompts lieferte eine brauchbare sichtbare Antwort |
| `qwen3:0.6b`, Schlussfolgern standardmäßig | 0.52 GB | 6.4 Token/s | 40.4 s | Eine leere Antwort; das Board startete neu |
| `granite4:350m` | 0.71 GB | 4.6 Token/s | 15.5 s | 913 MB RSS, kein Swap oder Neustart; langsam, aber stabil |
| `gemma3:1b` | 0.82 GB | 4.0 Token/s | 30.7 s | Starker Swap-Einsatz; Board startete während des Tests neu |
| `qwen3.5:0.8b` | 1.04 GB | — | — | Test nicht abgeschlossen; Board startete neu |

Die Pi-4-Ergebnisse reagieren besonders empfindlich auf die übrige Systemlast. Bei Tests mit größeren Modellen beobachteten wir Neustarts, darunter einen nicht abgeschlossenen Lauf mit `qwen3.5:0.8b`. Das ist ein Ergebnis für unsere 2-GB-Konfiguration und keine Behauptung, jeder Pi 4 oder jedes 1B-Modell würde neu starten. Ein Pi 4 mit 4 GB oder 8 GB hat mehr Speicher, aber seine CPU macht die Inferenz weiterhin langsamer als auf dem getesteten Pi 5. Diese Pi-4-Speichervarianten haben wir nicht direkt getestet.

Ein früher Lauf auf dem Pi 4 sah deutlich schlechter aus als die späteren Messungen: Rund 625 MB zwischengespeicherte GGUF-Dateien lagen in einem RAM-basierten `/tmp`, sodass nur etwa 500–600 MB frei blieben und Hunderte Megabyte in den Swap verschoben wurden. Nachdem wir die Dateien auf dauerhaften Speicher verschoben hatten, ergaben die kleinen Modelle oben ein aussagekräftigeres Bild des Inferenzspeichers. Auf einem 2-GB-Board kann sogar der *Speicherort eines Downloads* einen Benchmark verfälschen.

**Empfehlung:** Das importierte LFM2.5-350M ist unsere Standardwahl für dieses 2-GB-Board. Es blieb bei **516 MB RSS** stabil, ließ etwa **1 GB RAM verfügbar** und bestand **5/6** Antwortregelprüfungen im Pi-4-Compliance-Lauf. Bei wiederholten Pi-5-Tests ließ es jedoch Quellennamen aus. Anwendungen, die eine Quellenangabe benötigen, sollten das prüfen. Wähle LFM2.5-230M, wenn Latenz und Speicherreserve am wichtigsten sind: Das Modell war schneller und kleiner, verfälschte aber in einer Antwort mit medizinischem Kontext „Übelkeit oder Erbrechen“ zu „Übelkeit/Beatmung“. Dieser inhaltliche Fehler macht es trotz des höheren wiederholten Werts bei mechanischen Prüfungen zu einer schwächeren Standardwahl für Gesundheits- oder Sicherheitsantworten. Wähle `qwen2.5:0.5b`, wenn du ein Modell aus der [Ollama-Registry](https://ollama.com/library/qwen2.5/tags) brauchst, und berücksichtige seine schwächere Befolgung von Anweisungen. `granite4:350m` blieb stabil, war aber langsamer und speicherintensiver; MiniCPM5-1B eignet sich nur, wenn der Client das Schlussfolgern deaktiviert. Vermeide Gemma 3 1B und Qwen3.5 0.8B auf dieser konkreten 2-GB-Konfiguration, da unsere Läufe Neustarts auslösten.

## Raspberry Pi 5: mehr Auswahl, aber langsamer

Der Pi 5 mit 8 GB bewältigte alle **25 Modelle** in unserem Geschwindigkeits- und Speichertest. Die Tabelle enthält jeden Lauf, auch Modelle, die wir für diese Kurzantwort-Arbeitslast nicht empfehlen. Ein Kreuz † kennzeichnet importiertes GGUF. „Think off“ bezeichnet die Einstellung des Geschwindigkeitstests; der separate Compliance-Test nutzte sie nicht zwingend.

| Modell | Dateigröße GB | Ausgabetoken/s | Antwort s | Spitzen-RSS MB | Einschätzung für kurze Antworten |
|---|---:|---:|---:|---:|---|
| `lfm2.5-230m` † | 0.25 | 45.0 | 1.8 | 446 | Niedrigste Latenz; 78 % wiederholte Compliance |
| `bonsai-1.7b` †, Q1_0 | 0.25 | 15.3 | 8.2 | 871 | Nicht verwenden: 1-Bit-Gewichte und 3/6 Compliance im Einzellauf |
| `lfm2.5-350m` † | 0.38 | 30.0 | 2.1 | 581 | Schnell, ließ aber bei 5/18 Wiederholungen die Quelle aus |
| `qwen2.5:0.5b` | 0.40 | 28.4 | 3.6 | 675 | Einfach aus der Registry; 61 % wiederholte Compliance |
| `qwen3:0.6b`, Schlussfolgern aus | 0.52 | 23.0 | 4.3 | 1,069 | Bedingt geeignet: 4/6 Compliance, Einstellung ist wichtig |
| `bonsai-4b` †, Q1_0 | 0.57 | 6.8 | 18.1 | 1,343 | Experimentelles 1-Bit-Modell; 6/6 im Einzellauf nicht bestätigt |
| `minicpm5-1b` †, Schlussfolgern aus | 0.69 | 18.4 | 5.1 | 869 | Bedingt geeignet: Standardmodus gab leere Antworten |
| `granite4:350m` | 0.71 | 12.1 | 6.6 | 892 | Passt, aber langsamer und größer als kleine LFM2.5-Modelle |
| `lfm2.5-1.2b` † | 0.73 | 15.5 | 4.7 | 967 | Insgesamt am besten für unsere Arbeitslast; 89 % wiederholte Compliance |
| `llama3.2:1b-instruct-q4_K_M` | 0.81 | 13.0 | 7.5 | 1,244 | Registry-Alternative; 5/6 im Compliance-Test |
| `gemma3:1b` | 0.82 | 11.2 | 10.9 | 1,262 | Beste wiederholte Compliance der Registry-Modelle: 83 % |
| `qwen2.5:1.5b-instruct-q4_K_M` | 0.99 | 10.3 | 9.4 | 1,361 | 4/6 Compliance; Gemma 3 1B befolgte Regeln besser |
| `qwen3.5:0.8b`, Schlussfolgern aus | 1.04 | 8.8 | 12.2 | 1,592 | 0/6 im Standardmodus; ohne Kontrolle über das Schlussfolgern meiden |
| `spark-x2.5-1.7b` †, Schlussfolgern aus | 1.11 | 9.7 | 9.4 | 1,542 | 0/6 im Standardmodus; ohne Kontrolle über das Schlussfolgern meiden |
| `qwen3:1.7b`, Schlussfolgern aus | 1.36 | 8.1 | 12.4 | 1,867 | Bedingt geeignet; mehr Speicher und Verzögerung als kleinere Modelle |
| `minicpm5-2b` †, Schlussfolgern aus | 1.56 | 7.7 | 10.9 | 1,787 | Bedingt geeignet; 5/6 im Einzellauf, zusätzliche Aufzählungspunkte |
| `qwen2.5:3b-instruct-q4_K_M` | 1.93 | 5.2 | 14.7 | 2,366 | 3B-Modell zum Ausprobieren; 5/6 im Einzellauf |
| `granite4:micro-h` | 1.94 | 3.9 | 23.7 | 2,486 | Für interaktive Nutzung meiden: langsame Decodierung |
| `llama3.2:3b-instruct-q4_K_M` | 2.02 | 5.5 | 18.6 | 2,831 | 3B-Alternative; kein Compliance-Test berichtet |
| `granite4:micro` | 2.10 | 5.3 | 17.9 | 2,679 | Passt, aber Antworten sind langsamer als bei kleineren Alternativen |
| `qwen3.5:2b`, Schlussfolgern aus | 2.74 | 5.0 | 16.1 | 3,627 | Hoher Speicherbedarf und Verzögerung; kein Compliance-Test berichtet |
| `gemma3:4b` | 3.34 | 3.9 | 30.3 | 4,267 | Für schnelle Antworten meiden; 14.3 s bis zum ersten Token |
| `ling-3.0-tiny` †, Schlussfolgern aus | 4.82 | 9.9 | 19.4 | 5,071 | Großer Speicherbedarf; 5/6 im Einzellauf mit Grounding-Fehler |
| `lfm2.5:8b`, Schlussfolgern aus | 5.16 | 8.7 | 54.6 | 5,317 | Passt knapp; 34.4 s Kaltstart und zu lange Antworten |
| `gemma3n:e2b` | 5.62 | 6.1 | 25.9 | 5,261 | Nicht verwenden: Swap-Druck parallel zu anderen Pi-Diensten |

† Importiertes GGUF. Antwortzeiten und Speicherwerte stammen aus dem Geschwindigkeitstest mit fünf Prompts auf dem Pi 5; Compliance-Werte stammen aus separaten Tests mit sechs Prompts. Ohne Compliance-Wert wurde nicht nachgewiesen, dass das Modell die Antwortregeln befolgt.

Die kleinen LFM2.5-Modelle waren für diese Kurzantwort-Arbeitslast am schnellsten. Die 1.2B-Version ist ein praktischer Mittelweg auf dem getesteten Pi 5. Gemma 3 1B ist eine Registry-Alternative, die in unseren späteren Tests die Antwortregeln besser befolgte als Qwen2.5 1.5B. Ein 3B-Modell kann sich bei Prompts lohnen, die mehr Kapazität erfordern, doch die Zeiten allein zeigen nicht, welches Modell die besten Antworten gibt.

Kaltstart- und Ersttoken-Verzögerungen verändern das Nutzungserlebnis. LFM2.5-230M lud auf dem Pi 5 in etwa **0.21 Sekunden** und zeigte nach **0.37 Sekunden** ein Token. Qwen2.5 1.5B benötigte **2.59 Sekunden** zum Laden und **3.66 Sekunden** bis zum ersten sichtbaren Token; bei Qwen2.5 3B waren es **5.60** und **7.97 Sekunden**. Bei einer gelegentlichen Frage können diese Verzögerungen wichtiger sein als die Ausgaberate nach Generierungsbeginn. Bei einem dauerhaft geladenen Modell fallen sie weniger ins Gewicht, dafür belegt das Modell zwischen Anfragen Speicher.

Weitere gemessene Kandidaten zeigen, warum wir nicht nur nach Parameterzahl ordnen. Mit deaktiviertem Schlussfolgern erreichte `qwen3:0.6b` auf dem Pi 5 **23.0 Token/s** bei **1,069 MB RSS**; das importierte MiniCPM5-1B erreichte **18.4 Token/s** bei **869 MB RSS**. `granite4:350m` erforderte einen **0.71-GB**-Download und erzeugte **12.1 Token/s**, trotz der Bezeichnung 350M. Modellverpackung und Architektur verändern den Zusammenhang zwischen Name, Dateigröße, Speicher und Geschwindigkeit.

Wenn dein Client zuverlässig `think: false` senden kann, sind Qwen3 0.6B und MiniCPM5-1B sinnvolle Experimente als Alternativen zu LFM2.5. MiniCPM5-2B, Qwen3 1.7B und Spark-X2.5 1.7B liefen ebenfalls auf dem Pi 5, boten aber keinen klaren Geschwindigkeits- und Speichervorteil gegenüber unseren Hauptempfehlungen. Im Compliance-Test liefen MiniCPM5-1B und Spark-X2.5 mit standardmäßigem Schlussfolgern; ihre leeren Antworten dürfen nicht als Ergebnis der Think-off-Geschwindigkeitsläufe dargestellt werden. Umgekehrt beweist ein schneller Think-off-Lauf nicht, dass eine Bridge ohne diese Einstellung eine brauchbare Antwort erhält.

Wenn eine einfache Installation wichtiger ist als Rohgeschwindigkeit, sind Gemma 3 1B und Llama 3.2 1B plausible Registry-Modelle auf dem Pi 5 mit 8 GB. Gemma 3 1B befolgte die getesteten Antwortregeln in **15/18** wiederholten Antworten. Llama 3.2 1B bestand in einem Einzellauf **5/6**, daher ist die Schätzung weniger sicher. Qwen2.5 1.5B lud und antwortete in unserem Zeittest schneller als Gemma 3 1B, bestand im einzelnen Compliance-Lauf aber nur **4/6** Antwortregelprüfungen. Entscheide anhand der Anforderungen deiner Prompts.

Für gelegentlich längere oder schwierigere Textprompts sind quantisierte Qwen2.5 3B und Llama 3.2 3B die 3B-Kandidaten mit moderatem Speicherbedarf auf unserem Pi 5 mit 8 GB. Wir haben Geschwindigkeit und Speicher gemessen; Qwen2.5 3B bestand in einem Compliance-Einzellauf **5/6**. Für Llama 3.2 3B wurde kein vergleichbarer Compliance-Lauf berichtet. Mehr Parameter sind ein Grund, diese Modelle für Aufgaben zu *testen*, an denen kleinere Modelle scheitern, aber kein Beweis, dass sie diese Aufgaben besser lösen. Granite 4 Micro und Micro-H, Qwen3.5 2B, Gemma 3 4B, Ling-3.0-tiny und Gemma 3n E2B passten oder luden in unseren Pi-5-Tests, boten für diese Kurzantwort-Anwendung jedoch weniger attraktive Latenz, Speicherspielraum oder Zuverlässigkeit.

Die beiden Bonsai-Modelle zeigen den Preis extremer Quantisierung. Ihre Q1_0-Dateien waren für Namen mit 1.7B und 4B Parametern auffallend klein, doch das 1.7B-Modell bestand nur **3/6** Antwortregelprüfungen. Das 4B-Modell bestand einen einzelnen Sechs-Prompt-Test, benötigte aber **18.1 Sekunden** pro Antwort und wurde nicht wiederholt auf Compliance geprüft. Wir betrachten beide als Experimente statt als Standardempfehlungen, besonders wenn Antwortqualität wichtig ist.

Das LFM2.5-8B-Ergebnis braucht Kontext: Die hybride Architektur nutzt pro Token weniger aktive Parameter, sodass die Decodiergeschwindigkeit über den gemessenen dichten 3B-Modellen lag. Das Kaltladen von microSD dauerte trotzdem **34.4 Sekunden**, bei über **5.3 GB residentem Speicher**. Das zeigt, was hineinpasst, ist aber keine bequeme Standardwahl für einen Pi mit weiteren Diensten. Auch das gemessene `gemma3n:e2b` nutzte etwa 5.3 GB residenten Speicher und verursachte parallel zu den übrigen Diensten des Testhosts Swap.

Der LFM2.5-8B-Lauf erreichte außerdem das volle Limit von **140 Token**, statt die Antwort kurz zu halten. Der Gemma-3-4B-Lauf brauchte **14.3 Sekunden** bis zum ersten Token und **30.3 Sekunden** für die gesamte Antwort. Beide Modelle lassen sich auf diesem Pi 5 laden, verhielten sich in unseren Tests aber nicht wie ein reaktionsschneller kleiner Assistent. Ein winziges Modell mit einer passenden kurzen Antwort kann einer Funk- oder Befehlsoberfläche besser dienen als ein größeres Modell mit auf dem Papier schnellerer Decodierung.

## Speicher, Schlussfolgern und Modellformat

Eine erste Schätzung aus unseren Messungen lautet **Downloadgröße des Modells × 1.4** für residenten Inferenzspeicher. Das ist nur eine Faustregel: Kontextlänge, Runtime-Einstellungen, Modellarchitektur und andere Prozesse können den Bedarf ändern. Prüfe während der Generierung den verfügbaren Speicher, lade auf einem kleinen Host jeweils nur ein Modell und lasse Platz für das Betriebssystem. Ein Board mit 4 GB kann sinnvoll mit kleinen oder kompakten Modellen starten, doch unsere Empfehlungen für 4 GB sind Extrapolationen und keine direkten Tests an 4-GB-Varianten.

So entsprach etwa eine 0.73-GB-Datei für LFM2.5-1.2B auf dem Pi 5 ungefähr **967 MB RSS**, während die 0.99-GB-Datei für Qwen2.5 1.5B **1,361 MB RSS** erreichte. Für diese Modelle ist die Faustregel brauchbar, aber kein fester Grenzwert. Plane mehr ein als den gemessenen Modellspeicher, wenn der Pi auch eine Oberfläche, einen Suchindex, eine lokale Bibliothek oder einen Hintergrunddienst ausführt. Beobachte Swap bei einer echten Anfrage; ein Modell, das zwar lädt, aber ständig swappt, passt praktisch nicht.

Einige Modelle erzeugen einen internen Denkblock, bevor die sichtbare Antwort erscheint. In unseren Tests dauerte es bei `qwen3:0.6b` auf dem Pi 4 mit 2 GB deutlich länger, bis Text sichtbar wurde. MiniCPM5-1B lieferte mit der standardmäßigen Denk-Einstellung nur eine von fünf brauchbaren Antworten, mit deaktiviertem Denken dagegen fünf von fünf. Für ein kurzes Antwortlimit kannst du in einer kompatiblen Ollama-API-Anfrage `think: false` setzen oder ein Modell wählen, das standardmäßig nicht schlussfolgert. Diese Einstellung gilt für unterstützte Modelle und Clients und ist kein universeller Geschwindigkeitsschalter.

Das ist wichtig, weil ein Tokenlimit auch Tokens für das Schlussfolgern umfassen kann, obwohl der Nutzer keine Antwort sieht. Auf dem Pi 4 benötigte `qwen3:0.6b` mit standardmäßigem Schlussfolgern durchschnittlich **40.4 Sekunden pro Anfrage**; ein Prompt ergab eine leere sichtbare Antwort. MiniCPM5-1B benötigte standardmäßig durchschnittlich **33.3 Sekunden**, mit deaktiviertem Schlussfolgern **12.2 Sekunden**. Bei den Pi-5-Läufen schalteten wir für Qwen3, Qwen3.5, MiniCPM5, Ling-3.0 und Spark-X2.5 das Schlussfolgern dort aus, wo es in unseren Aufzeichnungen angegeben ist. Vergleiche jedes Modell mit genau der Einstellung, die dein Client später verwendet.

### Prüfen, ob die Antwort brauchbar ist

Für unsere Kurzantwort-Arbeitslast eines Mesh-Assistenten ist der Antwortvertrag ebenso wichtig wie die Geschwindigkeit: höchstens **90 Wörter**, maximal **drei Aufzählungspunkte**, Klartext, ein vollständiger Satz und Verwendung des bereitgestellten Abrufkontexts mit Quellenangabe. Die Bridge teilt den Text in **180-Zeichen-Blöcke**. Eine lange Antwort belegt mehr Funkzeit, auch wenn das Modell sie schnell erzeugt.

Die spätere Benchmark-Version prüft leere Antworten, ein promptabhängiges Wortlimit, zu viele Aufzählungspunkte, Markdown-Tabellen oder Codeblöcke, einen unvollendeten Schluss, fehlende Begriffe aus dem bereitgestellten Kontext und einen fehlenden Quellennamen. Bei der Bewertung nach dem System-Prompt des eingesetzten Assistenten verstießen kleine Modelle regelmäßig gegen diese Regeln. Die schwerwiegendsten Fehler waren **leere Antworten**, wenn das Schlussfolgern das Tokenbudget verbrauchte, gefolgt von Antworten, die den abgerufenen Kontext ignorierten oder die Quelle ausließen. Zu viele Wörter oder Aufzählungspunkte lieferten noch sichtbaren Text, verbrauchten aber Funkzeit. Das sind mechanische Prüfungen und kein Ersatz für das Lesen der Antwort: Sie belegen weder sachliche Richtigkeit noch die Qualität von Sicherheitshinweisen.

#### Wiederholte Compliance-Ergebnisse auf dem Pi 5

Zuerst ließen wir je Modell sechs Prompts einmal mit einem Limit von **220 Token** und dem eingesetzten System-Prompt laufen. Vielversprechende Modelle testeten wir noch zweimal mit einem anderen Seed, also **18 Antworten pro Modell**. Ein perfekter Einzellauf garantierte keine perfekten Wiederholungen. Die folgenden wiederholten Ergebnisse bieten einen belastbareren Vergleich für die getesteten kurzen Mesh-Antworten:

| Modell | Antworten, die alle geprüften Regeln einhielten | Hauptsächliche beobachtete Fehler |
|---|---:|---|
| Importiertes LFM2.5-1.2B | 16/18 (89%) | Zwei unvollständige Antworten |
| `gemma3:1b` | 15/18 (83%) | Drei unvollständige Antworten |
| Importiertes LFM2.5-230M | 14/18 (78%) | Unvollständige Antworten und fehlende Quellennamen |
| Importiertes LFM2.5-350M | 13/18 (72%) | Fehlende Quellennamen |
| `qwen2.5:0.5b` | 11/18 (61%) | Zu viele Aufzählungspunkte und Wörter, fehlende Quellennamen |

Beim **Pi 4 mit 2 GB** ergab der separate Sechs-Prompt-Compliance-Test **5/6** für LFM2.5-350M, **4/6** für LFM2.5-230M und **2/6** für Qwen2.5-0.5B. MiniCPM5-1B verbesserte sich von **1/6** mit standardmäßigem Schlussfolgern auf **5/6** mit deaktiviertem Schlussfolgern. Diese Pi-4-Werte stammen aus Einzelläufen. Bei Aussagen zur allgemeinen Anweisungsbefolgung gewichten wir daher die wiederholten Pi-5-Ergebnisse stärker und nutzen die Pi-4-Läufe zur Bewertung von Stabilität und Geschwindigkeit auf diesem Board.

Die Fehler haben unterschiedliche Folgen. Eine **leere** Antwort hilft dem Nutzer nicht; eine Antwort, die bereitgestelltes Material ignoriert, kann irreführen. Ein fehlender Quellennamen verhindert, dass Leser die Herkunft prüfen. Zusätzliche Aufzählungspunkte oder Wörter verbrauchen vor allem weitere 180-Zeichen-Pakete. Ein unvollständiger Satz kann auf Abschneiden hinweisen. Der Fehler von LFM2.5-230M mit einem medizinischen Begriff zeigt, dass eine Antwort mechanische Prüfungen bestehen und trotzdem falsch sein kann. Keines der fünf wiederholt getesteten Modelle befolgte alle Regeln in allen 18 Antworten. Eine Anwendung mit strengen Längen- oder Formatvorgaben sollte diese nach der Generierung zusätzlich durchsetzen und risikoreiche Inhalte getrennt prüfen.

Wir überprüften auch den tatsächlichen Bridge-Endpunkt, Ollamas OpenAI-kompatibles `/v1/chat/completions`, mit abgerufenem WikiMed-Kontext. Auf dem Pi 5 lieferte LFM2.5-1.2B eine 28 Wörter lange Antwort mit sechs bereitgestellten Begriffen; Qwen2.5-0.5B lieferte 38 Wörter mit sieben Begriffen. Beide passten in zwei 180-Zeichen-Pakete. Diese Endpunktprüfung bestätigt, dass das importierte LFM2.5-Modell über den Anfragepfad der Bridge funktioniert. Eine einzelne erfolgreiche Antwort garantiert aber keine Zuverlässigkeit.

Ollama veröffentlicht viele sofort abrufbare Modelle, darunter [Qwen2.5-Varianten mit 0.5B, 1.5B und 3B](https://ollama.com/library/qwen2.5/tags). Wir importierten die kleinen LFM2.5-Modelle aus den [GGUF-Releases von Liquid AI](https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/tree/main) in Ollama. Prüfe vor dem Download das genaue Tag oder den GGUF-Dateinamen: Registries und Repositories können sich ändern. Speichere GGUF-Downloads dauerhaft; in unseren Tests belegte `/tmp` im RAM knappen Pi-4-Speicher.

### Registry-Tags und GGUF-Imports

Ein Ollama-Tag ist der kürzeste Weg zum ersten Test: Lade das genaue Tag und starte es. Die kleinen LFM2.5-Modelle in unseren Tabellen waren **GGUF-Imports**, keine Tags namens `lfm2.5-230m`, `lfm2.5-350m` oder `lfm2.5-1.2b` in der öffentlichen Ollama-Bibliothek. GGUF ist ein Modelldateiformat; Bezeichnungen wie `Q8_0` und `Q4_K_M` markieren Quantisierungsoptionen. Die verwendeten LFM2.5-Dateien mit 230M und 350M waren Q8_0, die 1.2B-Datei war Q4_K_M. Die gleiche Parameterzahl in einer anderen Quantisierung muss daher nicht dieselbe Dateigröße, denselben Speicherbedarf oder dieselbe Qualität haben.

Für den Import der getesteten 350M-Variante lade die GGUF-Datei in ein Verzeichnis auf dauerhaftem Speicher, erstelle eine Modelfile mit dem Dateipfad und lass Ollama sie in seinen Modellspeicher kopieren:

```bash
mkdir -p "$HOME/gguf"
cd "$HOME/gguf"
curl -fL -C - --retry 5 --retry-all-errors -O \
  https://huggingface.co/LiquidAI/LFM2.5-350M-GGUF/resolve/main/LFM2.5-350M-Q8_0.gguf
printf 'FROM %s/LFM2.5-350M-Q8_0.gguf\n' "$PWD" > Modelfile-lfm2.5-350m
ollama create lfm2.5-350m -f Modelfile-lfm2.5-350m
ollama run lfm2.5-350m
```

Der Import braucht vorübergehend Platz für die heruntergeladene Datei und die Kopie im Ollama-Speicher. Wir nutzten fortsetzbare Downloads, weil lange GGUF-Übertragungen gelegentlich abbrachen. Vergleiche vor dem Import den SHA-256-Wert des Downloads mit dem vom Anbieter veröffentlichten Hash; eine unvollständige Übertragung kann sonst wie ein Modellfehler aussehen. Auf unserem Pi war `/tmp` RAM-basiert, daher verringerte ein dort gespeichertes GGUF den für Inferenz verfügbaren Speicher.

## Ein sinnvoller Einstieg

| Hardware und Ziel | Erstes Modell zum Testen | Grund |
|---|---|---|
| Pi 4 mit 2 GB, Standardwahl | Importiertes LFM2.5-350M | Stabil bei 516 MB RSS und etwa 1 GB freiem RAM; nach medizinischem Fehler des 230M gewählt |
| Pi 4 mit 2 GB, geringste Latenz | Importiertes LFM2.5-230M | 383 MB RSS und 7.2 s mittlere Antwortzeit; Inhalt genau prüfen, besonders bei Gesundheits- und Sicherheitsfragen |
| Pi 4 mit 2 GB, nur Registry-Modelle | `qwen2.5:0.5b` | Direkt aus Ollama abrufbar und im Pi-4-Einzeltest mit fünf Prompts stabil; 61 % wiederholte Compliance auf dem Pi 5 |
| Pi 4 mit 4 GB oder Pi 5 | Importiertes LFM2.5-1.2B, dann lokal testen | 967 MB RSS und 89 % wiederholte Compliance auf unserem Pi 5 mit 8 GB; 4-GB-Varianten wurden nicht direkt getestet |
| Pi 5 mit 8 GB, reaktionsschneller Assistent | Importiertes LFM2.5-1.2B | 15.5 Token/s, 4.7 s Antwortzeit und höchste wiederholte Compliance unserer Messungen |
| Pi 5 mit 8 GB, nur Registry-Setup | `gemma3:1b` | 11.2 Token/s, 1,262 MB RSS und 83 % wiederholte Compliance |
| Pi 5 mit 8 GB, größeres Textmodell ausprobieren | Quantisiertes Qwen2.5 3B oder Llama 3.2 3B | Beide liefen mit etwa 5 Token/s und nutzten 2.4–2.8 GB RSS; Qwen2.5 3B bestand 5/6 in einem Compliance-Einzellauf |

Diese Optionen bevorzugen kurze, nützliche Antworten auf einem Pi, der möglicherweise weitere Dienste ausführt. Es sind Startpunkte, keine Behauptung, ein Modell sei für jede Aufgabe am besten. Im Pi-5-Einzeltest erzeugten `qwen3.5:0.8b` und Spark-X2.5 mit standardmäßigem Schlussfolgern keine konformen Antworten; MiniCPM5-1B erreichte 1/6. Wenn dein Client das Schlussfolgern nicht deaktivieren kann, solltest du sie für diese Kurzantwort-Arbeitslast meiden. Teste das endgültige Modell mit dem geplanten Prompt, Kontext, der Parallelität und Antwortbegrenzung.

Für das Registry-Modell führe nach der [Ollama-Installation für Linux](https://ollama.com/download/linux) Folgendes aus:

```bash
ollama pull qwen2.5:0.5b
ollama run qwen2.5:0.5b
```

Teste mit eigenen Prompts, gewünschter Antwortlänge und den anderen laufenden Diensten. Notiere sowohl die gesamte Antwortzeit als auch den Speicherbedarf. Das sagt mehr über die Eignung für deinen Pi aus als die Parameterzahl allein.

Behalte auf einem speicherbegrenzten Knoten den Swap während der Tests im Blick. Wenn ein größeres Modell das Board unresponsiv macht, verwende ein kleineres Modell und setze ein passendes Speicherlimit für den Ollama-Dienst, damit ein übergroßer Ladevorgang abbricht, bevor dem Host der Speicher ausgeht. Ein Dienstlimit ist eine Schutzmaßnahme, kein Weg, ein zu großes Modell passend zu machen. Die Neustarts des Pi 4 in unseren Tests zeigen, warum Reaktionsfähigkeit und Speicherreserve zusätzlich zu Token pro Sekunde zählen.

## Den Benchmark in eine Bereitstellungsentscheidung umsetzen

Bevor du ein Modell täglich einsetzt, halte vier Grenzen fest: **maximale Antwortzeit, maximaler residenter Speicher, Antwortformat und Fehlerverhalten**. Teste sie zusammen mit den Diensten, die sich das Board teilen. Ein Modell, das allein besteht, aber neben Funk-Bridge oder Dashboard Swap verursacht, erfüllt die Bereitstellungsanforderung nicht.

Lass ein kleines Fallback-Modell installiert. Wechsle zu ihm, wenn das Hauptmodell das Speicherlimit überschreitet, eine leere Antwort liefert oder den Antwortvertrag verletzt. Notiere bei jedem Vergleich Modell-Tag, Quantisierung, Ollama-Version, Prompt, Kontextlänge und Seed, damit eine spätere Modellaktualisierung nicht wie eine Hardwareverbesserung wirkt.
