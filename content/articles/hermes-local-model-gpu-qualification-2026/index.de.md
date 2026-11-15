---
title: "Hermes-Modelltests lokal: Welche GPU- und Modellkombinationen ich wählen würde"
date: 2026-10-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Meine Empfehlungen für Hermes beruhen auf Tests mit langem Kontext, Werkzeugen, Streaming und Vision auf RTX-5060-Ti-, RTX-2000E-Ada-, RTX-3060-Ti- und RTX-3070-Systemen."
genre: ["Künstliche Intelligenz", "Lokale KI", "Computerhardware"]
tags: ["Hermes Agent", "lokale Sprachmodelle", "LLM-Leistungsmessungen", "GPU-Inferenz", "RTX 3060 Ti", "RTX 3070", "RTX 2000E Ada", "RTX 5060 Ti", "Modellqualifizierung", "Werkzeugaufrufe", "langer Kontext", "llama.cpp", "Ollama", "Qwen3.5", "Qwen3.6", "Qwen3.8"]
cover: "/img/cover/hermes-local-model-gpu-benchmarks.webp"
coverAlt: "Illustration einer Grafikkarte mit zwei Lüftern und flacher Karten neben dem Titel Hermes Model Benchmarks auf dunkelblauem Hintergrund"
coverCaption: ""
---

Für Hermes-Aufgaben mit langem Kontext würde ich mit Qwen3.5 35B auf zwei RTX 5060 Ti mit je 16 GB beginnen. Die getestete Route behielt 239.153 Eingabetokens über LiteLLM und bestand getrennte Prüfungen für Werkzeuge, Streaming, Vision, Warteschlange und Abbruch. Qwen3.6 ist meine Ein-Karten-Alternative. Auf RTX-3060-Ti- und RTX-3070-Systemen würde ich mit Qwen3.5 2B oder 4B beginnen.

Diese Auswahl beruht auf Modellen in den Inferenzpfaden des Agenten. Ich prüfte lange Eingaben, Werkzeugrunden, gestreamte Antworten, Bildfragen und das Freigeben des Modells. Auch die Modi und Speichereinstellungen der Routen testete ich, denn ein erfolgreich geladenes Modell sagt wenig über seinen Nutzen bei einer langen Agentenanfrage aus.

Hermes benötigt für Agenten mit Werkzeugen mindestens 64.000 Kontexttokens. Als Schwelle für langen Kontext nutzte ich 65.536 tatsächlich verarbeitete Eingabetokens. Die Zahl der Eingabetokens zählt mehr als die vom Server beworbene Kontextgröße. ([Dokumentation der Hermes-Agent-Provider](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md))

## GPUs in den einzelnen Systemen

Die Systembuchstaben kennzeichnen diese Hardwarekombinationen in den Ergebnissen.

| System | GPUs für diesen Benchmark | Mein Startmodell |
|---|---|---|
| A | 2 × GeForce RTX 5060 Ti, je 16 GB | Qwen3.5 35B auf beiden Karten oder Qwen3.6 auf einer Karte |
| B | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, wenn mehrere Minuten Verarbeitung langer Eingaben zur Aufgabe passen |
| C | 1 × RTX 2000E Ada, 16GB | Gemma 3 4B für den getesteten Pfad mit langen Eingaben; Qwen3.5 0.8B ohne Denkmodus für gezielte Erinnerungsaufgaben |
| D | 1 × RTX 2000E Ada, 16GB | Qwen3.5 9B, Gemma 4 12B-IT oder GPT-OSS 20B für die getesteten Arbeitslasten mit größeren Modellen |
| E | 9 × GeForce RTX 3060 Ti, je 8 GB | Qwen3.5 2B oder 4B |
| F | 8 × GeForce RTX 3060 Ti, je 8 GB | Qwen3.5 2B oder 4B |
| G | 3 × GeForce RTX 3070 | Qwen3.5 2B oder 4B |

Die Zahl installierter Karten bedeutet nicht, dass jede Anfrage alle GPUs nutzte. Die Tests mit Qwen3.5 35B und Flash Next verwendeten beide Karten in System A. Qwen3.6 nutzte eine Karte. Beim erfolgreichen Vision-Wiederholungstest mit Qwen3.5 4B in System E lief eine ausgewählte Karte aus einem Pool von acht, während eine neunte Karte von KI-Aufgaben ausgeschlossen blieb.

Die folgenden Laufzeiten sind Ergebnisse aus dem Zusammenspiel des getesteten Modells, der Laufzeitumgebung und des Systems. Sie vergleichen nutzbare Konfigurationen, isolieren aber nicht die GPU-Architektur als Ursache eines Geschwindigkeitsunterschieds.

## Zwei RTX 5060 Ti machen Qwen3.5 35B zu meiner Wahl für langen Kontext

Qwen3.5 35B erzielte in diesen Tests die größte erhaltene Eingabe. Die direkte Ollama-Folge behielt 248.279 Eingabetokens in einem Laufzeitkontext von 262.144. Eine separate gestreamte Gateway-Anfrage behielt 239.153 Eingabetokens, gab die Startmarkierung zurück und endete nach 31 Ausgabetokens in 148,12 Sekunden regulär.

Das Gateway-Ergebnis ist für Hermes relevant, weil die Anfrage über Broker und LiteLLM lief. Separate Anfragen schlossen eine Werkzeugrunde ab, erkannten ein rotes Bild und lieferten zwei richtige Antworten, als beide zusammen gesendet wurden. Der Broker reihte sie ein. Beim Schließen des Streams gab der Broker die Anfrage frei und entlud das Modell innerhalb von 60,31 Sekunden.

| Qwen3.5-35B-Anfrage | Eingabetokens | Ausgabetokens | Dauer | Ergebnis |
|---|---:|---:|---:|---|
| Direktes Ollama, erste progressive Stufe | 69,429 | 31 | 38.783 s | Exakte Startmarkierung |
| Direktes Ollama, Fortsetzung mit gemeinsamem Präfix | 124,179 | 31 | 28.472 s | Exakte Startmarkierung |
| Direktes Ollama, Fortsetzung mit gemeinsamem Präfix | 182,579 | 31 | 38.974 s | Exakte Startmarkierung |
| Direktes Ollama, Fortsetzung mit gemeinsamem Präfix | 248,279 | 31 | 54.215 s | Exakte Startmarkierung |
| Streaming-Anfrage über den Broker | 69,427 | 29 | 38.872 s | Exakte Startmarkierung |
| Streaming-Anfrage über LiteLLM | 239,153 | 31 | 148.12 s | Exakte Startmarkierung, clean unload |

Die fortlaufenden direkten Anfragen verwendeten ein wachsendes gemeinsames Präfix erneut. Ihre Zeiten beschreiben eine warme Fortsetzung. Die 54,215 Sekunden sind keine unabhängige Kaltmessung für einen neuen 248K-Prompt.

In der größten direkten Stufe meldete das Modell etwa 27,3 Milliarden Bytes Speicherbelegung auf beiden GPUs. Die Speicherspitzen je Karte erreichten 14.964 und 12.386 MiB.

Die Spitzentemperaturen erreichten 62 und 63 °C. Der Lauf verzeichnete weder OOM- noch Xid-Fehler. Im konfigurierten Kontext blieben 13.865 Tokens für eine Fortsetzung. Die kurze Markierungsantwort nutzte 31 davon.

Diese Route würde ich einsetzen, wenn ein großer Arbeitssatz wichtiger ist als die kürzeste erste Antwort. Werkzeug- und Vision-Prüfungen belegen nützliches Agentenverhalten, der Lang-Eingabetest belegt die Erhaltung. Es sind getrennte Arbeitslasten.

## Qwen3.6 ist die Option mit einer Karte

Qwen3.6-35B-A3B UD-Q4_K_XL behielt 131.000 Eingabetokens auf einer RTX 5060 Ti. Die zweite Karte blieb während des Tests ungenutzt. Das ist eine nützliche Alternative, wenn nicht beide Karten einem Modell zugewiesen werden sollen.

| Qwen3.6-Gatewayanfrage | Eingabetokens | Ausgabetokens | Dauer | Ergebnis |
|---|---:|---:|---:|---|
| Erste lange Anfrage | 66,007 |  | 167.82 s | Startmarkierung erhalten |
| Längere Anfrage | 90,000 | 11 | 159.92 s | Startmarkierung erhalten, zero cached input |
| Längere Anfrage | 119,999 | 11 | 250.61 s | Startmarkierung erhalten, zero cached input |
| Nahe der Laufzeitgrenze | 131,000 | 11 | 287.09 s | Startmarkierung erhalten, zero cached input |

Die Anfrage mit 131.000 Tokens näherte sich dem Laufzeitlimit von 131.072. Für einen Agenten würde ich mehr Platz für die Antwort und folgende Werkzeugnachrichten lassen. Ein Erhaltungstest nahe am Limit belegt die Eingabeverarbeitung, ist aber kein sinnvoller Standardwert für das Eingabebudget.

Die Werkzeugnutzung bestand bei deaktiviertem Denkmodus. Der Standardmodus verbrauchte das Testlimit von 512 Tokens, bevor er das Werkzeug aufrief. Der erfolgreiche Pilot bestand auch Schnell-, Streaming- und Vision-Anfragen. Der erste Kontexttest mit 65.845 Tokens dauerte 139,57 Sekunden.

## Qwen3.8 27B gewinnt den Antwortvergleich mit gleichem 66K-Input

Bei derselben Markierungsaufgabe mit 66.007 Tokens auf System A lieferte Qwen3.8 27B die schnellste Antwort. Diese Route würde ich für Anfragen nahe der getesteten Eingabegröße verfügbar halten, Qwen3.5 35B für den größeren Arbeitssatz.

| Route auf System A | Eingabetokens | Dauer | Ergebnis |
|---|---:|---:|---|
| Qwen3.8 27B | 66,007 | 54.64 s | Startmarkierung erhalten |
| Qwen3.6-35B-A3B UD-Q4_K_XL | 66,007 | 167.82 s | Startmarkierung erhalten |
| Qwen3.8-Flash-Next UD-IQ4_XS | 66,007 | 164.58 s | Startmarkierung erhalten |
| Flash Next IQ4 compatibility alias | 66,007 | 213.25 s | Markierung erhalten |

Qwen3.8 27B benötigte etwa ein Drittel der Laufzeit der vergleichbaren Qwen3.6- und Flash-Next-Anfragen. Das sind Beobachtungen vollständiger Anfragen in den getesteten Laufzeitumgebungen, kein reiner Hardwarevergleich.

Auch schnelle Antworten, Streaming und Werkzeugnutzung bestanden die Tests. Der Modus ohne Denken schloss die gesamte Farbfolge und Werkzeugrunde ab. Der Denkversuch gab innerhalb des Limits von 512 Tokens nur einen Teil der Farbfolge zurück.

Flash Next ist auf diesem System wegen des Speicherdrucks weniger attraktiv als Standard. Der Pilot mit 65.847 Tokens bestand in 201,41 Sekunden bei einem Laufzeitkontext von 98.304. Zwei frühere Profile mit Kontext 131.072 erreichten vor der Bereitschaft ihre Speichergrenzen.

Die spätere Route erreichte ihr cgroup-Limit von 54 GiB. Für unbeaufsichtigte Arbeit würde ich eine Route mit mehr Speicherreserve wählen.

Die Route mit dem Namen `flash-iq2` nutzte das Flash-Next-IQ4-Kompatibilitätsbackend. Der Name bezeichnet kein IQ2-Ergebnis.

## Die RTX 2000E Ada verarbeitet lange Eingaben, doch die Modellwahl verändert die Wartezeit

Gemma 3 4B ist meine bevorzugte getestete Route für lange Eingaben auf System C. Zwei Pfade behielten mehr als 84K Eingabetokens in etwa 88 Sekunden. Auch größere Modelle bestanden nützliche Erhaltungstests, ihre Anfragen dauerten jedoch mehrere Minuten.

| System | Modell und Pfad | Eingabetokens | Dauer | Ergebnis |
|---|---|---:|---:|---|
| B | Qwen3.5 9B, Gateway | 72,265 | 263 s | Beide Markierungen erhalten; spätere Mining-Wiederherstellungsprüfung bestanden |
| C | Gemma 3 4B, Gateway | 84,044 | 88.05 s | Startmarkierung erhalten |
| C | Gemma 3 4B, Aperture | 84,045 | 87.68 s | Startmarkierung erhalten |
| C | Gemma 4 12B-IT, Gateway | 67,254 | 263.07 s | Startmarkierung erhalten |
| C | Gemma 4 12B-IT, Aperture ohne Streaming | 67,255 | 274.24 s | Startmarkierung erhalten |
| C | Gemma 4 12B-IT, Aperture-Streaming | 67,255 | 282.16 s | Startmarkierung erhalten |
| C | Qwen3.5 9B, Gateway | 75,648 | 319.36 s | Startmarkierung erhalten, Modell aus dem Speicher entladen |
| C | GPT-OSS 20B, Gateway | 84,099 | 315.83 s | Startmarkierung erhalten, Modell aus dem Speicher entladen |
| D | Qwen3.5 9B, Aperture | 81,051 | 324.07 s | Erhaltung auf dem installierten Artefakt bestanden |
| D | Gemma 4 12B-IT, Aperture | 72,057 | 300.67 s | Erhaltung auf dem installierten Artefakt bestanden |
| D | GPT-OSS 20B, Aperture | 72,104 | 245.94 s | Erhaltung auf dem installierten Artefakt bestanden |

Streaming beseitigte das lange Prefill-Warten von Gemma 4 auf System C nicht. Der erste gestreamte Inhalt kam nach 277,49 Sekunden und damit später als die vollständige Antwort ohne Streaming nach 274,24 Sekunden. Ein früherer Versuch ohne Streaming lief vor der erfolgreichen Wiederholung in einen Timeout. Diese Route würde ich nur nutzen, wenn mehrere Minuten bis zur ersten Verarbeitung zum Auftrag passen.

Gemma 3 4B zeigt auch, warum die Qualifizierung auf das jeweilige getestete System beschränkt bleiben muss. System D verfehlte die Startmarkierung in zwei 65K-Abrufversuchen, darunter eine Wiederholung bei Temperatur null mit 67.252 Eingabetokens. Die deterministische Anfrage endete nach 62,07 Sekunden regulär bei voller GPU-Belegung.

Eine schnelle Antwort und eine normale API-Antwort machten das Ergebnis nicht richtig. Ich würde die erfolgreiche Route auf System C nutzen und die fehlgeschlagene System-D-Route aus der Hermes-Auswahl nehmen.

## Der Denkmodus entscheidet, ob Qwen3.5 0.8B nützlich ist

Nach dem Deaktivieren des Denkmodus wurde Qwen3.5 0.8B auf System C ein nützlicher Kandidat für eng begrenzte Abrufe. Das kleine Q8_0-Modell behielt über das Gateway 75.649 Eingabetokens in 65,92 Sekunden. Das Ergebnis gilt für das getestete Q8_0-Artefakt und die Route ohne Denkmodus, nicht für die älteren 16K-Konfigurationen in der Tabelle.

| Qwen3.5-0.8B-Anfrage auf System C | Eingabetokens | Ausgabetokens | Dauer | Ergebnis |
|---|---:|---:|---:|---|
| Kurze Diagnose mit standardmäßigem Denken | 9,050 | 3,391 | 66.56 s | Exakte Startmarkierung |
| Denken deaktiviert, angeglichene Diagnose | 9,055 | 21 | 7.65 s | Exakte Startmarkierung, no reasoning text |
| Langer Versuch mit standardmäßigem Denken |  |  | Timeout nach 600 s | Keine abgeschlossene Antwort |
| Denken deaktiviert, natives Ollama | 75,656 | 22 | 69.80 s | Exakte Startmarkierung |
| OpenAI-kompatibler Endpunkt ohne Denken | 75,646 | 12 | 69.09 s | Exakte Startmarkierung |
| Broker mit erzwungenem Modus ohne Denken | 75,647 | 13 | 66.83 s | Exakte Startmarkierung |
| LiteLLM vom System A zum System C | 75,649 | 15 | 65.92 s | Exakte Startmarkierung |

Die vergleichbare Diagnose sank von 66,56 auf 7,65 Sekunden und war damit etwa 8,7-mal schneller. Die erzeugte Ausgabe sank von 3.391 auf 21 Tokens. Für einfache Extraktions- und Routing-Aufgaben würde ich deshalb den Denkmodus ausdrücklich festlegen. Das Standarddenken verbrauchte den größten Teil der Arbeit für unnötige Ausgabe.

Eine kurze OpenAI-kompatible Probe verfehlte die Markierung, bevor die Wiederholung bei Temperatur null bestand. Die erfolgreichen Routen nutzten den Modus ohne Denken und einen natürlichen Abschluss ohne Ausgabelimit. Drei weitere Gateways bestanden kurze Markierungsanfragen in 4,22, 4,37 und 3,85 Sekunden. Diese Prüfungen belegen das Routing; die Anfrage mit 75.649 Tokens belegt die Erhaltung langer Eingaben über das Gateway.

Diese Route würde ich für begrenzte Abrufe und Extraktion ausprobieren. Für offenes Agenten-Denken würde ich ein größeres Modell wählen. Eine synthetische Markierung abzurufen ist enger gefasst als zu planen, zu programmieren oder mehrere Werkzeuge zu koordinieren.

## Die RTX-3060-Ti- und RTX-3070-Systeme eignen sich für Qwen3.5 2B und 4B

Qwen3.5 2B und 4B sind meine praktischen Startmodelle für 8-GB-Karten. Ihre Text-Kontextanfragen auf System E, F und G bestanden mit 65.579 Eingabetokens und dauerten 30,343 bis 93,753 Sekunden. Die getesteten 4B-Routen bestanden auch Werkzeug-, Streaming- und Bildprüfungen.

Der 4B-Vision-Kontext-Wiederholungstest auf System E behielt beide Markierungen und die Reihenfolge der Bildfarben bei 65.637 Eingabetokens in 44,88 Sekunden. Auch Anfragen mit vorwärts und umgekehrt sortierten Farben bestanden. Der Test nutzte eine intakte Karte, nachdem eine andere einen Xid-79-Linkfehler erlitt und das System neu startete.

| System | Qwen3.5-2B-Textkontext | Qwen3.5-4B-Textkontext | Qwen3.5-4B-Visionkontext |
|---|---|---|---|
| E, RTX 3060 Ti pool | 65,579 tokens, 30.343 s | 65,579 tokens, 53.787 s | 65,637 tokens, 44.88 s |
| F, RTX 3060 Ti pool | 65,579 tokens, 61.282 s | 65,579 tokens, 93.753 s | 65,635 tokens, 84.749 s |
| G, RTX 3070 pool | 65,579 tokens, 76.731 s | 65,579 tokens, 90.807 s | 65,635 tokens, 87.496 s |

Jedes dieser Systeme verzeichnete 29 bestandene Prüfungen. Die Zeitspanne zwischen den beiden RTX-3060-Ti-Systemen zeigt außerdem, warum ich ein getestetes Systemprofil auswählen würde, statt Karten anhand dieser Anfragedauern zu sortieren.

Alle sieben Systeme kehrten nach dem Inferenzfenster zum Mining zurück. Die separate Wiederherstellungsprüfung nach dem Stopp auf System B bestand mit neuen akzeptierten Shares. Die fehlerhafte Karte in System E kehrte später nach einem Neustart und einer PCIe-Link-Härtung zum Mining zurück, blieb aber vom KI-Pool ausgeschlossen. Mining am Ende des Zeitfensters wiederherzustellen ist ein anderes Ergebnis als die automatische Rückgabe nach einer einzelnen Inferenzanfrage.

## Ein geladenes Modell ist noch nicht qualifiziert

DeepSeek Coder V2 16B würde ich aus den getesteten 65K-Hermes-Optionen ausschließen. Der Lauf mit f16-Cache behielt 50.477 Eingabetokens, doch der 65K-Zielversuch erreichte die VRAM-Schutzgrenze. Q4- und Q8-Cache-Alternativen luden die Gewichte auf die GPUs und stießen danach an Host-Speichergrenzen oder erreichten bei langen Prompts einen schlechten Durchsatz.

| DeepSeek-Coder-V2-Cacheprofil | Laufzeitkontext | Beobachtetes Ergebnis | Meine Einschätzung |
|---|---:|---|---|
| f16 | 81,920 | Abruf von 50.477 Tokens bestanden, übergroße Anfrage abgewiesen | Nützliches Ergebnis mit kürzerem Kontext |
| f16 | 73,728 | Prefill für 65K-Ziel bei 15.802 MiB GPU-Nutzung gestoppt | Qualifiziert nicht für 65K |
| Q4_0 | 98,304 | Das lange Pre-Fill sank vor dem kontrollierten Stopp auf 96.72 Token/s | Ungeeignet für diese Arbeitslast |
| Q8_0 | 77,824 | Das lange Pre-Fill sank vor dem kontrollierten Stopp auf 120.12 Token/s | Ungeeignet für diese Arbeitslast |
| Q4_0 / Q8_0, größere Profile | 163,840 / 98,304 | Host-Speicherschutz stoppte die Tests | Die Speicherauslegung muss das ganze System berücksichtigen |

Die praktische Lehre: Teste die Anfrage, die du senden willst. GPU-Belegung, eine kurze Antwort und ein großer konfigurierter Kontext belegen keine Erhaltung langer Eingaben bei brauchbarer Latenz.

Granite 4.2 8B und GPT-OSS 20B verbesserten sich nach routenspezifischer Nacharbeit auf System A. Granites Q6_K-Route behielt 66.082 Eingabetokens in 88,636 Sekunden bei null gecachtem Input. GPT-OSS schloss seine Werkzeugrunde nach der Brokerkorrektur ab: 9,854 Sekunden für den Aufruf und 9,849 für die Folgeanfrage. Diese bestandenen Routenprüfungen würde ich von früheren unvollständigen Versuchen trennen.

## Vollständige Benchmark-Ergebnisse

Die Tabelle enthält 295 Prüfungen über 59 Modell-System-Kombinationen. Die Matrix verzeichnet 273 bestandene Prüfungen, einen fehlgeschlagenen Abruf und sieben unvollständige, inkonsistente oder inkompatible Ergebnisse. Vierzehn Prüfungen liegen außerhalb des 65K-Qualifizierungsbereichs. Jede Zeile zeigt das gemessene Ergebnis.

Meine Empfehlungen gelten für bestandene Routen und Arbeitslasten. Eine fehlgeschlagene oder unvollständige Zeile qualifiziert das betreffende Verhalten nicht.

Bestandene Kurzkontext- und Embedding-Tests gelten für ihre jeweiligen Arbeitslasten. Ein bestandener Kontext von 16K oder 32K qualifiziert eine Route nicht für Hermes mit 65.536 Eingabetokens. Modellnamen sind hier Routenbezeichnungen. `flash-iq2` nutzte das IQ4-Kompatibilitätsbackend.

Die Kontextzeile für Qwen3.5 35B auf System A ist die letzte Stufe der gemeinsamen Präfixfolge oben. Werkzeugzeiten mit Pluszeichen zeigen Aufruf und Folge getrennt.

Die Parallelitätszeile nennt die Laufzeiten der beiden eingereihten Anfragen. Die Abbruchzeile zeigt die Freigabezeit nach dem Schließen des Streams durch den Client. Zusätzliche Kontextfolgen und Qwen3.5-0.8B-Routenvergleiche stehen in eigenen Tabellen weiter oben.

### System A

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| bonsai-2-27b | context | Bestanden | 65,621 | 88.746 s |
| bonsai-2-27b | quick | Bestanden | 57 | 6.429 s |
| bonsai-2-27b | stream | Bestanden |  | 9.371 s |
| bonsai-2-27b | tools | Bestanden |  | 10.478 s |
| deepseek-coder-v2:16b | context | Inkompatibel | 50,477 |  |
| deepseek-coder-v2:16b | quick | Bestanden | 77 | 43.239 s |
| flash-iq2 | context | Bestanden | 66,007 | 213.25 s |
| flash-iq2 | quick | Bestanden |  | 56.03 s |
| flash-iq2 | stream | Bestanden |  | 1.35 s |
| flash-iq2 | tools | Bestanden |  | 16.55 s |
| gemma-4-12b-it | context | Bestanden | 65,590 | 51.225 s |
| gemma-4-12b-it | quick | Bestanden | 21 | 5.166 s |
| gemma-4-12b-it | stream | Bestanden |  | 4.653 s |
| gemma-4-12b-it | tools | Bestanden |  | 18.72 s |
| gemma-4-12b-it | vision | Bestanden | 115 | 7.222 s |
| gemma-4-12b-it | vision_context | Bestanden | 65,685 | 56.06 s |
| gemma-4-12b-it | vision_reverse | Bestanden | 115 | 7.467 s |
| gemma-4-e4b-it | context | Bestanden | 65,590 | 21.889 s |
| gemma-4-e4b-it | quick | Bestanden | 21 | 17.919 s |
| gemma-4-e4b-it | stream | Bestanden |  | 4.25 s |
| gemma-4-e4b-it | tools | Bestanden |  | 8.734 s |
| gpt-oss-20b | context | Bestanden | 65,637 | 159.155 s |
| gpt-oss-20b | quick | Bestanden | 73 | 10.548 s |
| gpt-oss-20b | stream | Bestanden |  | 20.594 s |
| gpt-oss-20b | tools | Bestanden |  | 9.854 + 9.849 s |
| granite-4.2-3b | context | Bestanden | 65,589 | 70.968 s |
| granite-4.2-3b | quick | Bestanden | 20 | 4.009 s |
| granite-4.2-3b | stream | Bestanden |  | 5.365 s |
| granite-4.2-3b | tools | Bestanden |  | 6.086 s |
| granite-4.2-8b | context | Bestanden | 66,082 | 88.636 s |
| granite-4.2-8b | quick | Bestanden | 20 | 5.857 s |
| granite-4.2-8b | stream | Bestanden |  | 11.826 s |
| granite-4.2-8b | tools | Bestanden |  | 11.852 s |
| qwen27b | context | Bestanden | 66,007 | 54.64 s |
| qwen27b | quick | Bestanden | 57 | 31.5 s |
| qwen27b | stream | Bestanden |  | 0.92 s |
| qwen27b | tools | Bestanden |  | 4.25 s |
| qwen3-embedding-0.6b | context | Bestanden | 32,767 | 7.736 s |
| qwen3-embedding-0.6b | quick | Bestanden | 14 | 2.125 s |
| qwen3.5-0.8b | context | Bestanden | 16,429 | 10.5 s |
| qwen3.5-0.8b | quick | Bestanden | 17 | 14.316 s |
| qwen3.5-0.8b | stream | Bestanden |  | 2.125 s |
| qwen3.5-0.8b | tools | Bestanden |  | 4.416 s |
| qwen3.5-2b | context | Bestanden | 65,581 | 11.175 s |
| qwen3.5-2b | quick | Bestanden | 17 | 4.519 s |
| qwen3.5-2b | stream | Bestanden |  | 3.736 s |
| qwen3.5-2b | tools | Bestanden |  | 5.046 s |
| qwen3.5-4b | context | Bestanden | 65,579 | 36.451 s |
| qwen3.5-4b | quick | Bestanden | 15 | 19.935 s |
| qwen3.5-4b | stream | Bestanden |  | 17.496 s |
| qwen3.5-4b | tools | Bestanden |  | 7.308 s |
| qwen3.5-4b | vision | Bestanden | 70 | 7.848 s |
| qwen3.5-4b | vision_context | Bestanden | 65,635 | 28.24 s |
| qwen3.5-4b | vision_reverse | Bestanden | 70 | 4.386 s |
| qwen3.5-9b | context | Bestanden | 65,581 | 34.139 s |
| qwen3.5-9b | quick | Bestanden | 17 | 3.88 s |
| qwen3.5-9b | stream | Bestanden |  | 3.378 s |
| qwen3.5-9b | tools | Bestanden |  | 10.204 s |
| qwen3.5-9b | vision | Bestanden | 72 | 4.441 s |
| qwen3.5-9b | vision_context | Bestanden | 65,637 | 33.745 s |
| qwen3.5-9b | vision_reverse | Bestanden | 72 | 3.97 s |
| qwen3.5:35b-a3b-q4_K_M | cancellation | Bestanden |  | 60.31 s |
| qwen3.5:35b-a3b-q4_K_M | concurrency | Bestanden |  | 26.23 / 25.33 s |
| qwen3.5:35b-a3b-q4_K_M | context | Bestanden | 248,279 | 54.215 s |
| qwen3.5:35b-a3b-q4_K_M | gateway | Bestanden | 239,153 | 148.12 s |
| qwen3.5:35b-a3b-q4_K_M | quick | Bestanden | 79 | 10.08 s |
| qwen3.5:35b-a3b-q4_K_M | stream | Bestanden | 69,429 | 38.783 s |
| qwen3.5:35b-a3b-q4_K_M | tools | Bestanden |  | 15.22 + 14.83 s |
| qwen3.5:35b-a3b-q4_K_M | vision | Bestanden |  | 18.39 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | context | Bestanden | 65,845 | 139.57 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | quick | Bestanden | 15 | 3.97 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | stream | Bestanden |  | 0.45 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | tools | Bestanden | 293 | 5.48 s |
| Qwen3.6-35B-A3B UD-Q4_K_XL | vision | Bestanden | 38 | 0.59 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | context | Bestanden | 65,847 | 201.41 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | quick | Bestanden | 17 | 54.62 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | stream | Bestanden |  | 1.2 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | tools | Bestanden |  | 22.18 s |
| Qwen3.8-Flash-Next UD-IQ4_XS | vision | Bestanden |  | 3.86 s |

### System B

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Bestanden | 65,590 | 299.163 s |
| gemma-4-12b-it | quick | Bestanden | 21 | 15.261 s |
| gemma-4-12b-it | stream | Bestanden |  | 148.792 s |
| gemma-4-12b-it | tools | Bestanden |  | 34.124 s |
| gemma-4-12b-it | vision | Bestanden | 120 | 61.455 s |
| gemma-4-12b-it | vision_context | Bestanden | 65,690 | 295.581 s |
| gemma-4-12b-it | vision_reverse | Bestanden | 120 | 32.511 s |
| gemma3-4b | context | Bestanden | 65,584 | 67.382 s |
| gemma3-4b | quick | Bestanden | 15 | 6.329 s |
| gemma3-4b | stream | Bestanden |  | 24.138 s |
| gemma3-4b | vision | Bestanden | 306 | 7.018 s |
| gemma3-4b | vision_context | Bestanden | 65,876 | 70.912 s |
| gemma3-4b | vision_reverse | Bestanden | 306 | 5.762 s |
| gpt-oss-20b | context | Bestanden | 65,637 | 206.767 s |
| gpt-oss-20b | quick | Bestanden | 72 | 16.583 s |
| gpt-oss-20b | stream | Bestanden |  | 32.075 s |
| gpt-oss-20b | tools | Bestanden |  | 28.102 s |
| nomic-embed-text | context | Unvollständig | 2,048 |  |
| nomic-embed-text | quick | Bestanden |  | 7.117 s |
| qwen3-14b | context | Unvollständig |  | 1800.09 s |
| qwen3-14b | quick | Bestanden | 15 | 37.199 s |
| qwen3-14b | stream | Bestanden |  | 35.471 s |
| qwen3-14b | tools | Bestanden |  | 87.554 s |
| qwen3-8b | context | Außerhalb 65K-Bereich, ausgeschlossen |  |  |
| qwen3-8b | quick | Außerhalb 65K-Bereich, bestanden | 15 | 21.059 s |
| qwen3-8b | stream | Außerhalb 65K-Bereich, ausgeschlossen |  |  |
| qwen3-8b | tools | Außerhalb 65K-Bereich, ausgeschlossen |  |  |
| qwen3.5-9b | context | Bestanden | 65,579 | 282.796 s |
| qwen3.5-9b | litellm_long_route | Bestanden | 72,265 | 263 s |
| qwen3.5-9b | post_external_stop_mining | Bestanden |  |  |
| qwen3.5-9b | quick | Bestanden | 15 | 25.881 s |
| qwen3.5-9b | stream | Bestanden |  | 143.44 s |
| qwen3.5-9b | tools | Bestanden |  | 31.812 s |
| qwen3.5-9b | vision | Bestanden | 75 | 32.015 s |
| qwen3.5-9b | vision_context | Bestanden | 65,640 | 396.288 s |
| qwen3.5-9b | vision_reverse | Bestanden | 75 | 28.626 s |

### System C

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-12b-it | aperture_context | Bestanden | 67,255 | 274.24 s |
| gemma-4-12b-it | aperture_short | Bestanden | 35 | 39.32 s |
| gemma-4-12b-it | aperture_stream_context | Bestanden | 67,255 | 282.16 s |
| gemma-4-12b-it | context | Bestanden | 65,670 | 313.661 s |
| gemma-4-12b-it | gateway_context | Bestanden | 67,254 | 263.07 s |
| gemma-4-12b-it | gateway_short | Bestanden | 27 | 20.98 s |
| gemma-4-12b-it | quick | Bestanden | 21 | 16.447 s |
| gemma-4-12b-it | stream | Bestanden |  | 15.175 s |
| gemma-4-12b-it | tools | Bestanden |  | 37.821 s |
| gemma-4-12b-it | vision | Bestanden | 120 | 58.52 s |
| gemma-4-12b-it | vision_context | Bestanden | 65,690 | 308.759 s |
| gemma-4-12b-it | vision_reverse | Bestanden | 120 | 31.25 s |
| gemma3-4b | aperture_context | Bestanden | 84,045 | 87.68 s |
| gemma3-4b | aperture_after_system_d_route_change | Bestanden | 24 | 5.42 s |
| gemma3-4b | aperture_short | Bestanden | 22 | 5.45 s |
| gemma3-4b | aperture_stream | Bestanden |  | 3.72 s |
| gemma3-4b | context | Bestanden | 65,664 | 67.543 s |
| gemma3-4b | gateway_context | Bestanden | 84,044 | 88.05 s |
| gemma3-4b | gateway_short_via_system_a | Bestanden |  | 3.16 s |
| gemma3-4b | gateway_short_via_system_e | Bestanden |  |  |
| gemma3-4b | gateway_short_via_system_f | Bestanden |  | 4.15 s |
| gemma3-4b | gateway_short_via_system_g | Bestanden |  | 6.06 s |
| gemma3-4b | quick | Bestanden | 15 | 5.163 s |
| gemma3-4b | stream | Bestanden |  | 24.691 s |
| gemma3-4b | vision | Bestanden | 306 | 7.318 s |
| gemma3-4b | vision_context | Bestanden | 65,876 | 72.476 s |
| gemma3-4b | vision_reverse | Bestanden | 306 | 5.831 s |
| gpt-oss-20b | context | Bestanden | 65,716 | 216.594 s |
| gpt-oss-20b | gateway_context | Bestanden | 84,099 | 315.83 s |
| gpt-oss-20b | gateway_short | Inkonsistent |  |  |
| gpt-oss-20b | quick | Bestanden | 72 | 21.603 s |
| gpt-oss-20b | stream | Bestanden |  | 31.957 s |
| gpt-oss-20b | tools | Bestanden |  | 26.096 s |
| nomic-embed-text | context | Außerhalb 65K-Bereich, unvollständig | 2,048 |  |
| nomic-embed-text | quick | Außerhalb 65K-Bereich, bestanden |  | 4.178 s |
| qwen3-14b | context | Außerhalb 65K-Bereich, unvollständig |  | 1800.06 s |
| qwen3-14b | quick | Außerhalb 65K-Bereich, bestanden | 15 | 35.809 s |
| qwen3-14b | stream | Außerhalb 65K-Bereich, bestanden |  | 35.43 s |
| qwen3-14b | tools | Außerhalb 65K-Bereich, bestanden |  | 87.723 s |
| qwen3-8b | context | Außerhalb 65K-Bereich, ausgeschlossen |  |  |
| qwen3-8b | quick | Außerhalb 65K-Bereich, bestanden | 15 | 21.293 s |
| qwen3-8b | stream | Außerhalb 65K-Bereich, unvollständig |  | 900.01 s |
| qwen3-8b | tools | Außerhalb 65K-Bereich, ausgeschlossen |  |  |
| qwen3.5-9b | context | Bestanden | 65,662 | 287.984 s |
| qwen3.5-9b | gateway_context | Bestanden | 75,648 | 319.36 s |
| qwen3.5-9b | gateway_short | Bestanden | 21 | 72.14 s |
| qwen3.5-9b | quick | Bestanden | 15 | 24.635 s |
| qwen3.5-9b | stream | Bestanden |  | 143.157 s |
| qwen3.5-9b | tools | Bestanden |  | 30.395 s |
| qwen3.5-9b | vision | Bestanden | 75 | 27.756 s |
| qwen3.5-9b | vision_context | Bestanden | 65,640 | 398.797 s |
| qwen3.5-9b | vision_reverse | Bestanden | 75 | 28.645 s |

### System D

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-12b-it | context | Bestanden | 65,590 | 275.395 s |
| gemma-4-12b-it | exact_digest_aperture_65k | Bestanden | 72,057 | 300.67 s |
| gemma-4-12b-it | exact_digest_broker_short | Bestanden | 34 | 30.74 s |
| gemma-4-12b-it | quick | Bestanden | 21 | 15.05 s |
| gemma-4-12b-it | stream | Bestanden |  | 14.722 s |
| gemma-4-12b-it | tools | Bestanden |  | 33.869 s |
| gemma-4-12b-it | vision | Bestanden | 120 | 56.315 s |
| gemma-4-12b-it | vision_context | Bestanden | 65,690 | 282.174 s |
| gemma-4-12b-it | vision_reverse | Bestanden | 120 | 29.978 s |
| gemma3-4b | context | Bestanden | 65,584 | 63.564 s |
| gemma3-4b | exact_digest_65k_recall | Fehlgeschlagen | 67,252 | 62.07 s |
| gemma3-4b | quick | Bestanden | 15 | 5.151 s |
| gemma3-4b | stream | Bestanden |  | 22.552 s |
| gemma3-4b | vision | Bestanden | 306 | 8.276 s |
| gemma3-4b | vision_context | Bestanden | 65,876 | 67.575 s |
| gemma3-4b | vision_reverse | Bestanden | 306 | 5.651 s |
| gpt-oss-20b | context | Bestanden | 65,637 | 189.07 s |
| gpt-oss-20b | exact_digest_aperture_65k | Bestanden | 72,104 | 245.94 s |
| gpt-oss-20b | exact_digest_broker_short | Bestanden | 84 | 15.96 s |
| gpt-oss-20b | quick | Bestanden | 72 | 15.431 s |
| gpt-oss-20b | stream | Bestanden |  | 31.052 s |
| gpt-oss-20b | tools | Bestanden |  | 23.65 s |
| nomic-embed-text | context | Unvollständig | 2,048 |  |
| nomic-embed-text | quick | Bestanden |  | 2.798 s |
| qwen3-14b | context | Unvollständig | 40,939 | 872.209 s |
| qwen3-14b | quick | Bestanden | 15 | 36.021 s |
| qwen3-14b | stream | Bestanden |  | 33.491 s |
| qwen3-14b | tools | Bestanden |  | 82.471 s |
| qwen3-8b | context | Unvollständig |  | 1800.07 s |
| qwen3-8b | quick | Bestanden | 15 | 19.283 s |
| qwen3-8b | stream | Bestanden |  | 19.401 s |
| qwen3-8b | tools | Bestanden |  | 65.054 s |
| qwen3.5-9b | context | Bestanden | 65,579 | 258.048 s |
| qwen3.5-9b | exact_digest_aperture_65k | Bestanden | 81,051 | 324.07 s |
| qwen3.5-9b | exact_digest_broker_short | Bestanden | 29 | 94.48 s |
| qwen3.5-9b | quick | Bestanden | 15 | 27.16 s |
| qwen3.5-9b | stream | Bestanden |  | 28.62 s |
| qwen3.5-9b | tools | Bestanden |  | 28.129 s |
| qwen3.5-9b | vision | Bestanden | 75 | 25.047 s |
| qwen3.5-9b | vision_context | Bestanden | 65,640 | 369.477 s |
| qwen3.5-9b | vision_reverse | Bestanden | 75 | 27.602 s |

### System E

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Bestanden | 65,590 | 49.086 s |
| gemma-4-e4b-it | quick | Bestanden | 21 | 23.911 s |
| gemma-4-e4b-it | stream | Bestanden |  | 28.136 s |
| gemma-4-e4b-it | tools | Bestanden |  | 56.756 s |
| granite-4.0-h-tiny | context | Bestanden | 65,566 |  |
| granite-4.0-h-tiny | quick | Bestanden | 35 | 10.408 s |
| granite-4.0-h-tiny | stream | Bestanden |  | 27.798 s |
| granite-4.0-h-tiny | tools | Bestanden |  | 43.304 s |
| granite-4.2-3b | context | Bestanden | 65,589 | 1014.03 s |
| granite-4.2-3b | quick | Bestanden | 20 | 14.569 s |
| granite-4.2-3b | stream | Bestanden |  | 6.948 s |
| granite-4.2-3b | tools | Bestanden |  | 56.376 s |
| qwen3-embedding-0.6b | context | Bestanden | 32,767 | 20.387 s |
| qwen3-embedding-0.6b | quick | Bestanden | 14 | 9.592 s |
| qwen3.5-0.8b | context | Bestanden | 16,429 | 9.128 s |
| qwen3.5-0.8b | quick | Bestanden | 17 | 452.417 s |
| qwen3.5-0.8b | stream | Bestanden |  | 11.163 s |
| qwen3.5-0.8b | tools | Bestanden |  | 39.214 s |
| qwen3.5-2b | context | Bestanden | 65,579 | 30.343 s |
| qwen3.5-2b | quick | Bestanden | 15 | 12.509 s |
| qwen3.5-2b | stream | Bestanden |  | 26.165 s |
| qwen3.5-2b | tools | Bestanden |  | 42.056 s |
| qwen3.5-4b | context | Bestanden | 65,579 | 53.787 s |
| qwen3.5-4b | quick | Bestanden | 15 | 26.736 s |
| qwen3.5-4b | stream | Bestanden |  | 26.02 s |
| qwen3.5-4b | tools | Bestanden |  | 57.293 s |
| qwen3.5-4b | vision | Bestanden | 72 | 10.09 s |
| qwen3.5-4b | vision_context | Bestanden | 65,637 | 44.88 s |
| qwen3.5-4b | vision_reverse | Bestanden | 72 | 9.96 s |

### System F

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Bestanden | 65,590 | 98.443 s |
| gemma-4-e4b-it | quick | Bestanden | 21 | 27.51 s |
| gemma-4-e4b-it | stream | Bestanden |  | 28.042 s |
| gemma-4-e4b-it | tools | Bestanden |  | 73.891 s |
| granite-4.0-h-tiny | context | Bestanden | 65,599 | 19.692 s |
| granite-4.0-h-tiny | quick | Bestanden | 35 | 43.818 s |
| granite-4.0-h-tiny | stream | Bestanden |  | 27.296 s |
| granite-4.0-h-tiny | tools | Bestanden |  | 75.377 s |
| granite-4.2-3b | context | Bestanden | 65,589 | 145.179 s |
| granite-4.2-3b | quick | Bestanden | 20 | 15.703 s |
| granite-4.2-3b | stream | Bestanden |  | 35.482 s |
| granite-4.2-3b | tools | Bestanden |  | 52.539 s |
| qwen3-embedding-0.6b | context | Bestanden | 32,767 | 20.656 s |
| qwen3-embedding-0.6b | quick | Bestanden | 14 | 8.122 s |
| qwen3.5-0.8b | context | Bestanden | 16,429 | 13.326 s |
| qwen3.5-0.8b | quick | Bestanden | 17 | 445.22 s |
| qwen3.5-0.8b | stream | Bestanden |  | 13.266 s |
| qwen3.5-0.8b | tools | Bestanden |  | 40.825 s |
| qwen3.5-2b | context | Bestanden | 65,579 | 61.282 s |
| qwen3.5-2b | quick | Bestanden | 15 | 16.738 s |
| qwen3.5-2b | stream | Bestanden |  | 25.29 s |
| qwen3.5-2b | tools | Bestanden |  | 47.444 s |
| qwen3.5-4b | context | Bestanden | 65,579 | 93.753 s |
| qwen3.5-4b | quick | Bestanden | 15 | 33.039 s |
| qwen3.5-4b | stream | Bestanden |  | 25.658 s |
| qwen3.5-4b | tools | Bestanden |  | 71.731 s |
| qwen3.5-4b | vision | Bestanden | 70 | 43.053 s |
| qwen3.5-4b | vision_context | Bestanden | 65,635 | 84.749 s |
| qwen3.5-4b | vision_reverse | Bestanden | 70 | 27.518 s |

### System G

| Modell-Routenname | Prüfung | Ergebnis | Eingabetokens | Anfragezeit |
|---|---|---|---:|---:|
| gemma-4-e4b-it | context | Bestanden | 65,590 | 92.696 s |
| gemma-4-e4b-it | quick | Bestanden | 21 | 38.329 s |
| gemma-4-e4b-it | stream | Bestanden |  | 43.549 s |
| gemma-4-e4b-it | tools | Bestanden |  | 66.616 s |
| granite-4.0-h-tiny | context | Bestanden | 65,599 | 69.777 s |
| granite-4.0-h-tiny | quick | Bestanden | 35 | 33.17 s |
| granite-4.0-h-tiny | stream | Bestanden |  | 31.751 s |
| granite-4.0-h-tiny | tools | Bestanden |  | 63.338 s |
| granite-4.2-3b | context | Bestanden | 65,589 | 100.849 s |
| granite-4.2-3b | quick | Bestanden | 20 | 23.355 s |
| granite-4.2-3b | stream | Bestanden |  | 28.75 s |
| granite-4.2-3b | tools | Bestanden |  | 44.226 s |
| qwen3-embedding-0.6b | context | Bestanden | 32,767 | 23.055 s |
| qwen3-embedding-0.6b | quick | Bestanden | 14 | 8.924 s |
| qwen3.5-0.8b | context | Bestanden | 16,429 | 16.74 s |
| qwen3.5-0.8b | quick | Bestanden | 17 | 504.813 s |
| qwen3.5-0.8b | stream | Bestanden |  | 15.095 s |
| qwen3.5-0.8b | tools | Bestanden |  | 36.672 s |
| qwen3.5-2b | context | Bestanden | 65,579 | 76.731 s |
| qwen3.5-2b | quick | Bestanden | 15 | 20.949 s |
| qwen3.5-2b | stream | Bestanden |  | 25.194 s |
| qwen3.5-2b | tools | Bestanden |  | 37.552 s |
| qwen3.5-4b | context | Bestanden | 65,579 | 90.807 s |
| qwen3.5-4b | quick | Bestanden | 15 | 41.84 s |
| qwen3.5-4b | stream | Bestanden |  | 40.812 s |
| qwen3.5-4b | tools | Bestanden |  | 54.999 s |
| qwen3.5-4b | vision | Bestanden | 70 | 29.619 s |
| qwen3.5-4b | vision_context | Bestanden | 65,635 | 87.496 s |
| qwen3.5-4b | vision_reverse | Bestanden | 70 | 26.283 s |

## So habe ich die Hermes-Eignung getestet

Ich setzte eine synthetische Markierung nahe an den Anfang eines langen Prompts und fragte sie nach dem Fülltext ab. Die Antwort musste den erwarteten Wert enthalten. Der Server bestimmte mit seiner Zahl an Eingabetokens die Anfragengröße. Ein Modell, das nach einer großen Eingabe normal antwortete, scheiterte trotzdem bei einer falschen Startmarkierung.

Die Qwen3.5-35B-Folge nutzte nummerierte Fülldatensätze, Temperatur 0 und wachsende Längen von 3.800, 6.800, 10.000 und 13.600 Datensätzen. Diese Stufen lieferten 69.429, 124.179, 182.579 und 248.279 Prompttokens. Das Modell blieb zwischen den Stufen geladen, sodass es das Präfix wiederverwenden konnte. Die separaten Qwen3.6-Grenztests meldeten null gecachte Tokens.

Der lange 0.8B-Prompt wiederholte `river stone lantern orchard circuit velvet compass marble` 8.400-mal zwischen einem Antwortschlüssel am Anfang und der abschließenden Abruffrage. Der native Lauf nutzte `think:false`, `num_ctx:131072`, `stream:false` und `keep_alive:0`. Die OpenAI-kompatible Route nutzte `reasoning_effort:"none"`. Der Broker erzwang den Modus ohne Denken.

### Werkzeug-, Vision- und Freigabeprüfungen

Werkzeugtests prüften die Anfrage und die Antwort nach Rückgabe des Werkzeugergebnisses. Ein einfacher Test nutzte `add_numbers(7, 11)` und erwartete 18. Der Qwen3.5-35B-Test nutzte `lookup_square` und erwartete 49. GPT-OSS fragte einen Bestand ab und musste das Ergebnis einbeziehen.

Visionprüfungen nutzten Fragen zu roten und blauen Bildern, umgekehrte Bildreihenfolge und lange Prompts mit Bildfarben sowie Start- und Endmarkierungen. Der Qwen3.5-35B-Test nutzte ein rotes PNG mit 256 × 256 Pixeln. Vor dem erfolgreichen Lauf musste der Broker die Bildinhaltskonvertierung korrigieren. Der lange 4B-Vision-Test auf System E erforderte beide Markierungen und die richtige Farbreihenfolge.

Während der langen Läufe prüfte ich GPU-Speicher, Modellbelegung, Temperaturen, Host-Speicherdruck, OOM-Ereignisse und GPU-Fehler. Die Qwen3.5-35B-Schutzprüfung kontrollierte auch die Freigabe nach einem kontrollierten Abbruch. Spätere Client-Abbruch- und Warteschlangenprüfungen testeten den Brokerpfad. Zwei eingereihte Anfragen belegen die Verarbeitung unter der getesteten Last, nicht zwei unabhängige gleichzeitige GPU-Backends.

### Leistungsergebnisse lesen

Anfragezeiten enthalten das Prefill der langen Eingabe und die Antwort. Sie sind keine generierten Tokens pro Sekunde. Beim Streaming zählt die Verzögerung bis zum ersten Inhalt; gecachte Präfixfolgen brauchen eine eigene Einordnung.

Die erfolgreichen Nachtests größerer Modelle auf System A und C nutzten eigene Inferenzfenster mit inaktivem Mining. Die Modelle wurden nach den Anfragen entladen. Das Mining wurde am Ende des Fensters auf allen sieben Systemen wiederhergestellt. Diese Ergebnisse beschreiben den Modelldienst während eines Inferenzfensters, nicht gleichzeitiges Mining und Inferieren.

## In den Tests genutzte Backendprofile

Wähle das Profil für die Arbeitslast, die du nachstellen willst. Quantisierung, Laufzeitkontext, Cachetyp, Denkmodus und GPU-Platzierung beeinflussen das Ergebnis.

| System und Modell | Getestetes Backendprofil |
|---|---|
| A, Qwen3.5 35B-A3B Q4_K_M | Ollama 0.34.2, f16-KV-Cache, beide 16-GB-RTX-5060-Ti-Karten, 64 GiB Host-RAM und Laufzeitkontext 262.144 für die große Progression. Native Anfragen nutzten `think:false`, Temperatur 0, Streaming und fünf Minuten Keep-alive zwischen Stufen. Gateway-Anfragen liefen über Broker und LiteLLM. Kein Ausgabelimit. |
| A, Qwen3.8 27B | llama.cpp bei Bedarf über Broker und LiteLLM, Laufzeitkontext 262.144, ein Inferenzslot, Q4-K/V-Cache und beide RTX 5060 Ti. Die Anfrage mit 66.007 Token hatte kein Ausgabelimit. |
| A, Qwen3.6-35B-A3B UD-Q4_K_XL | Strata 0.1.48, Kontext 131.072, INT8-KV-Cache, eine ausgewählte GPU, Prozessgruppen-Speicherlimit 55 GiB, Laufzeitlimit 30 Minuten, verzögertes Laden und Entladen nach 60 Sekunden Leerlauf. Lange Pilotantwort: 217 Ausgabetoken. Gateway-Antwort nahe dem Limit: 11 Ausgabetoken, kein Ausgabelimit. |
| A, Qwen3.8-Flash-Next UD-IQ4_XS | Strata 0.1.48, Kontext 98.304, Q4-KV-Cache, 8 GiB residenter Experten-Cache und beide RTX 5060 Ti. Speicherlimit des Piloten 52 GiB, spätere Route 54 GiB. Lange Pilotantwort: 10 Ausgabetoken. Frühere größere Kontext-/Cache-Kombinationen stoppten an Speicherlimits. |
| A, Granite 4.2 8B | Q6_K-GGUF-Gewichte, geteilter llama.cpp-Arbeitsprozess, Kontext 131.072, Q4_0-K/V-Cache und `--n-predict -1`. Die lange Anfrage nutzte Temperatur 0 und gestreamte Nutzungsdaten, ohne Ausgabelimit. |
| A, DeepSeek Coder V2 16B | Q4_0-GGUF-Gewichte, Ollama 0.34.2, zwei RTX 5060 Ti, 64 GiB Host-RAM. Getrennte f16-, Q4_0- und Q8_0-Cache-Tests verwendeten die in der Vergleichstabelle gezeigten Laufzeitkontexte. Kein Ausgabelimit. |
| B, C, D, geprüfter Ollama-Dienst | Ollama 0.34.2, Kontext 131.072, Parallelität 1, ein geladenes Modell, Warteschlangengröße 128, Keep-alive 0, Flash Attention und Q4_0-KV-Cache. |
| B, Qwen3.5 9B Gateway-Test | LiteLLM-Routen-Timeout 1.800 Sekunden, keine Wiederholungen, keine Kontext- oder Ausgabetoken-Grenze. Beide Markierungen blieben bei 72.265 Eingabetoken erhalten. Die separate Prüfung der Mining-Wiederherstellung wurde bestanden. |
| C, Qwen3.5 0.8B | Q8_0-Gewichte auf einer RTX 2000E Ada mit 30-W-Leistungsprofil. Laufzeitkontext 131.072. Natives `think:false`, OpenAI-kompatibles `reasoning_effort:"none"`, kein Ausgabelimit. Der Broker-Alias fixierte den Laufzeitkontext und erzwang den Modus ohne Denken. |
| C, Gemma 4 12B-IT | Ollama-Profil mit einer GPU, Laufzeitkontext 131.072 und gestreamte sowie nicht gestreamte Aperture-Anfragen ohne Ausgabelimit. Der direkte Aperture-Lauf erreichte im konfigurierten 30-W-Profil 75 C und 30,64 W und entlud das Modell danach. |
| D, Qwen3.5 9B, Gemma 4 12B-IT, GPT-OSS 20B | Exakte installierte Artefakte, über Aperture getestet, Laufzeitkontext 131.072, vollständige Belegung einer GPU und natürliche Fertigstellung ohne Ausgabelimit. |
| E, F, G, llama.cpp-Chatprozesse | Build 11669, 99 GPU-Layer, Parallelität 1, Flash Attention, Q4_0-K/V-Cache und `--n-predict -1`. Der Laufzeitkontext variierte je nach Modellfamilie. |

Die aufgezeichneten Dienstprofile beschreiben jeweils ihre eigene Laufzeitkonfiguration. Das separat getestete Qwen3.5-35B-Profil mit f16-Cache auf System A übernimmt nicht die Q4_0-Cache-Einstellungen der kleineren Ollama-Systeme.

### Modellfingerabdrücke der neuen Tests mit erhaltener Eingabe

Diese Modellkennungen unterscheiden die getesteten Artefakte von anderen Downloads oder Aliasen mit ähnlichen Namen.

| Artefakt | Quantisierung | Erfasster Digest oder Datei-SHA-256 |
|---|---|---|
| Qwen3.5 35B-A3B Ollama tag | Q4_K_M | `72aac7c28be8ff9b81c2a270eb489c88e6d822a76ec0cb7bf34d965768848567` |
| Qwen3.5 0.8B base Ollama tag | Q8_0 | `de63045f29755d4721c09d54c9b45c2dadb644f4fd7d604d4cac90d96049971c` |
| Granite 4.2 8B GGUF file | Q6_K | `5ad3d67f6fe09a448031029bead7f6a088697ca2787c0c5640bf964c59df1a21` |

Ollama-Manifest-Digests und SHA-256-Werte der Gewichtedateien kennzeichnen unterschiedliche Objekte. Ordne die Kennung dem Artefakttyp in der Tabelle zu.

## Was ich mit Hermes einsetzen würde

Qwen3.5 35B würde ich zur Hauptroute für hohen Kontext auf dem System mit zwei RTX 5060 Ti machen. Die Gateway-Erhaltung von 239.153 Tokens, separate bestandene Werkzeug- und Visionprüfungen sowie die bestätigte Freigabe sind aussagekräftiger als ein beworbenes großes Kontextfenster. Qwen3.8 27B würde ich für die schnellere Antwort bei 66K behalten, Qwen3.6 für Fälle, in denen eine Karte wichtig ist.

Auf RTX-2000E-Ada-Systemen würde ich für die getestete Lang-Eingabe-Antwortlast die bestätigte Gemma-3-4B-Route auf System C wählen. Die Qwen3.5-0.8B-Route ohne Denken würde ich für eng begrenzte Abrufe und Extraktion testen. Größere Gemma-, Qwen- und GPT-OSS-Routen eignen sich, wenn eine erste Antwort nach vier bis fünf Minuten akzeptabel ist. Die fehlgeschlagene Gemma-3-Route auf System D würde ich ausschließen.

Für 8-GB-Karten RTX 3060 Ti und RTX 3070 würde ich mit Qwen3.5 2B oder 4B beginnen. Die 65K-Textergebnisse und 4B-Bildprüfungen stützen eine brauchbare Startkonfiguration, ohne für jede Anfrage die beiden 16-GB-Karten zu nutzen. Flash Nexts Speicherdruck und DeepSeek Coder V2s unvollständiges 65K-Verhalten machen sie auf den getesteten Profilen zu schwächeren Standardoptionen.

Die Tests stützen diese Modell- und Systemauswahl für bestimmte Abläufe. Erhaltene Eingaben, ein korrekter Werkzeugzyklus, Bilderkennung und sauberes Freigeben beantworten unterschiedliche Teile der Hermes-Eignung. Ein zuverlässiger Aufbau braucht die Verhaltensweisen des Agenten und genug Kontext für Antwort und Werkzeugverkehr.

## Quellen und weiterführende Lektüre

- [Hermes-Agent-Providerkonfiguration und Kontextanforderungen](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md)
- [Technische Daten der NVIDIA GeForce RTX 3060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/)
- [Technische Daten der NVIDIA GeForce RTX 5060 Ti](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/)
- [Überblick über Hermes Agent](/hermes-local-ai-broker-course/01-hermes-agent-overview/)
- [Ein lokales Modellbackend auswählen](/hermes-local-ai-broker-course/02-choose-a-backend/)
