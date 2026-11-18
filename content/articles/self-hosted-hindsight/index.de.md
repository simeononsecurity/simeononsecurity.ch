---
title: "Self-hosted Hindsight: Lokales Agentengedächtnis und privates Modell-Routing"
date: 2026-11-08
lastmod: 2026-11-12
toc: true
draft: false
description: "Fallstudie zu selbst gehostetem Hindsight, beobachteten lokalen Qwen-Routen und GPU-Arbeit pro Anfrage ohne gehostetes Modell-Abo auf den geprüften Routen."
genre: ["Lokale KI", "Selbst gehostete KI", "KI-Agenten", "KI-Infrastruktur", "Datenschutz"]
tags: ["Hindsight", "selbst gehostetes Hindsight", "Agentengedächtnis", "lokale KI", "lokales LLM", "Qwen3.5", "LiteLLM", "privates VPN", "Modell-Gateway", "Embeddings", "Reranking", "GPU-Planung", "private Inferenz", "Docker", "Gedächtnisbänke", "Wissensseiten", "lokales Modell-Routing"]
cover: "/img/cover/self-hosted-hindsight-local-model-routing.webp"
coverAlt: "Ein privater Gedächtnisdienst leitet Aufgaben an lokale CPU- und GPU-Modellserver weiter"
coverCaption: "Gedächtnis, Abruf und geprüfte Modellrouten laufen auf eigener Hardware"
---

**Unser Hindsight-Gedächtnisdienst läuft auf Hardware, die wir kontrollieren.** Gedächtnis-Engine, Datenbank, Embedding-Modell und Reranker laufen in einer selbst gehosteten Bereitstellung. Hindsight sendet Generierungsanfragen an ein privates Gateway. Das geprüfte gemeinsame Qwen-Backend und die getestete Seitenaktualisierung nutzen lokale Modellserver, ohne Abo für gehostete Inferenz.

Dies beschreibt eine funktionierende Bereitstellung. **Selbst gehostet bedeutet nicht offline.** Das VPN nutzt einen externen Koordinierungsdienst, und Software-Images sowie Modellgewichte müssen heruntergeladen werden. Die Aussage betrifft die Gedächtnisverarbeitung und Modellinferenz, nicht jede Netzwerkverbindung unserer Geräte oder anderer Agentenwerkzeuge.

<!--more-->

## Kernaussagen

- **Hindsight verwaltet den Gedächtnisablauf.** Ein Docker-Container stellt API, Worker und Steuerungsebene bereit. Ein persistentes Volume speichert die Bankdaten.
- **Kleine Abrufmodelle bleiben lokal.** Embeddings und Reranking laufen innerhalb des Hindsight-Prozesses auf der CPU.
- **Qwen erzeugt Text.** Retain, Reflect und Consolidation fragen den privaten Alias Qwen3.5-4B mit deaktiviertem Reasoning und begrenzter Ausgabe ab. Das geprüfte Backend stellt ihn lokal bereit.
- **Langsame Seitenaktualisierungen erhalten eine GPU.** Ein separater Modellalias leiht für eine Hintergrundanfrage eine Karte aus und gibt sie nach der Anfrage frei.
- **Das Gateway verbirgt den physischen Ausführungsort.** Hindsight wählt einen Modellalias. Private Routingdienste wählen den Server-Endpunkt.

## Grenzen vor der Modellauswahl festlegen

**Hindsight ist die Gedächtnis-Engine, kein Modellserver.** Das vollständige Docker-Image enthält lokale Embedding- und Reranking-Modelle, aber die Sprachgenerierung benötigt einen Endpunkt. Der [Hindsight-Installationsleitfaden](https://hindsight.vectorize.io/developer/installation) erklärt diese Trennung und zeigt lokale llama.cpp-, Ollama- und vLLM-Server als Alternativen zu gehosteten Anbietern.

**Die Gedächtnis-API bleibt im privaten Netzwerk.** Die Websteuerung läuft auf einer lokalen Schnittstelle. Ein persistentes Volume speichert die eingebettete Datenbank, damit eine Neuerstellung des Containers die Bänke nicht löscht. Authentifizierung schützt die API, und getrennte Bänke ordnen den Projektkontext.

**Das Generierungs-Gateway bietet stabile Modellnamen.** Hindsight sendet OpenAI-kompatible Anfragen über das private Gateway und das VPN. Das Gateway leitet Anfragen an lokale Server-Endpunkte weiter. Die geprüfte Qwen-Route erreicht eine LiteLLM-Bereitstellung, die einem lokalen CPU-Server zugeordnet ist. Die [LiteLLM-Routerdokumentation](https://docs.litellm.ai/docs/routing) erklärt dieses Alias-Muster. Ein anderer OpenAI-kompatibler Router kann dieselbe Aufgabe übernehmen.

{{< figure src="hindsight-private-request-path.webp" alt="Diagramm mit Agenten, einem privaten Hindsight-Dienst, lokalen Abrufmodellen, einem privaten Gateway und lokalen Qwen-Servern" caption="Das Diagramm zeigt keine Hostnamen, Adressen, Zugriffsschlüssel oder Bezeichnungen physischer Rechner" >}}

[Das vollständige Diagramm des Anfragepfads öffnen](hindsight-private-request-path.webp).

**Es gibt weiterhin eine interne API.** Hindsight ruft ein privates Gateway im OpenAI-kompatiblen Format auf. Die geprüften Modellrouten führen Inferenz lokal aus. Wir haben nicht jede Ausweichregel des Gateways geprüft. Prüfe die Gateway-Richtlinie, bevor du lokale Verarbeitung als Garantie für jede Anfrage behandelst.

## Jede Gedächtnisaufgabe der passenden Rechenleistung zuweisen

Die Hindsight-Operationen erledigen unterschiedliche Aufgaben. **Retain** extrahiert Fakten aus neuem Material. **Recall** findet relevante Erinnerungen. **Reflect** sucht und formuliert eine zusammengefasste Antwort. **Consolidation** führt verwandte Fakten zusammen. Die **Aktualisierung von Wissensseiten** erstellt eine aktuelle Zusammenfassung aus der Bank.

| Operation | Modellplatzierung | Grund |
| --- | --- | --- |
| **Retain** | Qwen3.5-4B über das private Gateway | Lokale strukturierte Extraktion mit begrenztem Ausgabebudget |
| **Recall** | Lokale Embeddings und Reranking auf CPU | Die Suche braucht keinen Aufruf der Generierungs-API |
| **Reflect** | Qwen3.5-4B über das private Gateway | Die Synthese braucht nach dem Abruf eine Generierung |
| **Consolidation** | Qwen3.5-4B über das private Gateway | Kleine Stapel begrenzen lange strukturierte Antworten |
| **Wissensseiten-Aktualisierung** | Dedizierte lokale Qwen-GPU-Route | Große Hintergrundsynthese überschritt das Zeitlimit der CPU-Route |

*Lass kleine Abrufaufgaben auf der CPU und reserviere GPU-Inferenz für gemessene, lang laufende Arbeit.*

Der Hindsight-Container lädt **BAAI/bge-small-en-v1.5** für Embeddings und **hindsight-ai/hs-rerank-1** für Reranking. Startprotokolle bestätigen, dass beide lokal auf CPU laufen. Die [Hindsight-Modellreferenz](https://hindsight.vectorize.io/developer/models) dokumentiert lokale Modelloptionen und den optionalen Pfad für das Entscheidungsmodell.

Wir behielten das vorhandene Embedding-Modell bei, weil ein Wechsel des Embedding-Raums einen Neuaufbau gespeicherter Vektoren erfordert. Der Reranker läuft bereits lokal. Ein gehosteter Rerankingdienst würde daher eine neue Datengrenze schaffen, ohne das beobachtete Generierungs-Timeout zu beheben. Ein lokaler **hs-decide-1-flash**-Test lieferte eine korrekte Reflect-Antwort, endete aber nahe am Zeitlimit des Tests. Die synthetischen Consolidation-Daten prüften den Entscheidungspfad nicht. Deshalb fehlt das Entscheidungsmodell im Produktiv-Routing.

## Langsame Hintergrundarbeit mit einer GPU ausführen

**Der normale Modellname und der Name für die Aktualisierung unterscheiden sich.** Retain, Reflect und Consolidation nutzen den gemeinsamen Qwen-Alias. Die Hintergrundaktualisierung verwendet einen knotenspezifischen GPU-Alias mit höchstens einem gleichzeitigen Sprachmodellaufruf. So bleibt eine lange Wartungsaufgabe auf jeweils eine GPU begrenzt.

**Eine anfragebezogene Reservierung begrenzt die GPU-Nutzung.** Der GPU-Pool startet bei einer Anfrage einen Modell-Worker. Der Controller reserviert eine Karte, bedient die Anfrage, stoppt den Worker und gibt die Reservierung frei. Das Diagramm lässt den physischen Hostbestand aus.

{{< figure src="hindsight-gpu-lease-cycle.webp" alt="Diagramm mit einer für die Hintergrundaktualisierung reservierten GPU, die nach Abschluss der Anfrage freigegeben wird" caption="Eine anfragebezogene Zuweisung reserviert eine GPU für die Seitenaktualisierung" >}}

[Das vollständige Diagramm des GPU-Zuweisungszyklus öffnen](hindsight-gpu-lease-cycle.webp).

Diese Trennung entstand nach einem gemessenen Fehler. **Eine CPU-basierte Seitenaktualisierung erreichte ein Zeitlimit von einer Stunde.** Nachdem wir Hintergrundaktualisierungen zum lokalen GPU-Pool geleitet hatten, wurden fünf zuvor fehlgeschlagene Seiten in einem Wiederherstellungslauf in etwa zwei bis sechs Minuten abgeschlossen. Diese Werte beschreiben jene Seiten und Einstellungen. Sie sind kein allgemeiner Qwen-Durchsatztest.

## Standardwerte und Zeitlimits korrigieren

**Die früheren Hindsight-Ausgabegrenzen passten nicht zu unserem lokalen Router.** Der Router akzeptiert höchstens 8.192 Ausgabetoken und verwendet 256 Token, wenn eine Anfrage keine Grenze angibt. Eine frühere Retain-Grenze von 64.000 Token löste HTTP 400 aus. Consolidation-Stapel mit acht Fakten endeten wegen der Ausgabelänge, und Reflect brauchte eine explizite Grenze, um den 256-Token-Fallback des Routers zu vermeiden.

**Wir legten die Grenzen für jede Aufgabe fest.** Qwen-Reasoning ist für diese Gedächtnisoperationen ausgeschaltet. Hindsight erlaubt jetzt insgesamt vier gleichzeitige LLM-Aufrufe, darunter höchstens einen für die Hintergrundaktualisierung. Das globale LLM-Zeitlimit beträgt 1.800 Sekunden mit einem Modellwiederholungsversuch.

| Arbeitslast | Ausgabe- oder Stapelgrenze | Grenzen für Aufruf und Operation |
| --- | --- | --- |
| **Retain** | 8.192 Ausgabetoken | Allgemeines Aufruflimit: 1.800 Sekunden |
| **Reflect** | 4.096 Ausgabetoken | 900 Sekunden pro Aufruf, 3.600 Sekunden pro Operation |
| **Consolidation** | 4.096 Ausgabetoken, vier Fakten pro Aufruf | 900 Sekunden pro Aufruf, 14.400 Sekunden pro Operation |
| **Seitenaktualisierung** | Ein gleichzeitiger Modellaufruf | 900 Sekunden pro Aufruf, dedizierte GPU-Route |

*Diese Werte beschreiben unsere Bereitstellung im November 2026 und ihren lokalen Router.*

**Aufruf-Timeout und Operationszeitlimit begrenzen verschiedene Phasen.** Einige gültige Qwen-Aufrufe überschritten das frühere Aufruflimit von 300 Sekunden. Die längeren Operationszeitlimits erlauben Arbeit mit mehreren Aufrufen, während die 900 Sekunden pro Aufruf weiterhin jeden Versuch begrenzen.

Im Wiederherstellungslauf beendeten mehrere Retain-Aufgaben **1.042 bis 2.076 Ausgabetoken**. Zwei Consolidation-Läufe schlossen **41 von 41** und **30 von 30** Elementen ab. Ein späteres Zeitlimit bei einer Seitenaktualisierung führte zur separaten GPU-Route. Diese Ergebnisse belegen keine langfristige Zuverlässigkeit.

## Was dieses Design kostet

**Keine Rechnung für ein gehostetes Modell bedeutet nicht keine Kosten.** Die Bereitstellung nutzt eigene Hardware, Strom, Speicher, Wartungszeit und GPU-Zeit für Seitenaktualisierungen. Jede Platzierungsentscheidung tauscht Kapazität gegen Latenz oder einfacheren Betrieb.

| Wahl | Vorteil | Nachteil |
| --- | --- | --- |
| **Generierung zuerst auf CPU** | Hält die GPU verfügbar | Eine getestete Seitenaktualisierung erreichte ihr Stundenlimit |
| **GPU-Seitenaktualisierung** | Fünf Seiten wurden in einem Lauf in etwa zwei bis sechs Minuten abgeschlossen | Verbraucht GPU-Kapazität und hängt von der dedizierten Route ab |
| **Eingebettete Datenbank** | Hält die Bereitstellung kompakt | Verengt den Fehlerbereich und erfordert getestete Sicherungen |

*Nutze eine GPU-Route, wenn die gemessene CPU-Latenz dein Wartungsfenster überschreitet.*

Der [Hindsight-Installationsleitfaden](https://hindsight.vectorize.io/developer/installation) empfiehlt getrenntes PostgreSQL für größere Produktivumgebungen. **Unsere eingebettete Datenbank braucht einen getesteten Sicherungs- und Wiederherstellungspfad**, wenn die Bank wächst.

**Private Inferenz ist eine Eigenschaft des Pfads.** Prüfe den ausgewählten Hindsight-Anbieter, die Modellzuordnung des Gateways, Ausweichregeln, den lokalen Modellprozess, die Protokollaufbewahrung und ausgehenden Netzwerkverkehr. Hindsight-Trace-IDs helfen, Anfragen zuzuordnen, und Docker rotiert Containerprotokolle. Keine der beiden Maßnahmen beweist, dass eine nachgelagerte Anfrage lokal blieb. Ein Gateway-Audit liefert den fehlenden Nachweis Ende zu Ende.

## Empfehlung

**Beginne mit lokalen Abrufmodellen und expliziten Generierungsgrenzen.** Betreibe Hindsight sowie Embedding- und Reranking-Modelle auf eigener Hardware. Leite Generierung über ein privates OpenAI-kompatibles Gateway und ein VPN. Miss jede Operation, bevor du CPU- oder GPU-Kapazität zuweist. Reserviere die GPU-Route für Hintergrundaufgaben, deren CPU-Latenz dein Wartungsfenster überschreitet.

*Prüfe alle Gateway-Ausweichregeln und teste die Wiederherstellung der Bank, bevor du die Bereitstellung als privat und ausfallsicher behandelst.* Der [Leitfaden zu lokalen KI-Datenschutzgrenzen](/articles/local-ai-privacy-boundary/) bietet eine erste Checkliste.

## Fazit

**Diese Bereitstellung hält Hindsight-Gedächtnis und geprüfte Inferenzpfade auf eigener Hardware, ohne Abo für ein gehostetes Modell.** CPU-Abruf, begrenzte Qwen-Aufrufe und eine GPU-Route mit einem Aufruf für die Aktualisierung bedienen unterschiedliche Arbeitslasten. Die Wiederherstellungsläufe schlossen Retain, Consolidation und Seitenaktualisierungen unter diesen Einstellungen ab. Als Nächstes müssen alle Gateway-Ausweichregeln geprüft, Sicherungen getestet und die Zuverlässigkeit länger beobachtet werden.
