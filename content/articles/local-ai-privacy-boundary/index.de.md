---
title: "Datenschutz bei lokaler KI: Was auf Ihrem Computer bleibt und was nicht"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Verfolgen Sie Prompts, Modelldateien, Tools, Protokolle, Netzwerkzugriff und Stromkosten, bevor Sie lokale Inferenz oder einen gehosteten KI-Dienst wählen."
genre: ["Lokale KI", "Datenschutz", "Self-Hosted-KI", "Cybersicherheit", "KI-Ökonomie"]
tags: ["local AI privacy", "local inference", "cloud AI", "AI data privacy", "self-hosted AI", "LLM privacy", "GPU ownership cost", "AI electricity cost", "RTX 5070", "Claude Haiku 5.5", "Ollama privacy", "llama.cpp", "AI security", "offline AI", "local language models", "prompt privacy", "AI threat model", "GPU break-even", "AI data boundary", "private AI"]
cover: "/img/cover/local-ai-vs-chatgpt-comparison-illustration.webp"
coverAlt: "Eine lokale KI-Workstation mit sichtbaren Datenpfaden zu einem Cloud-Dienst"
coverCaption: "Darstellung lokaler und gehosteter KI-Datenpfade"
---

**Lokale KI verkleinert Ihre Datengrenze.** Ein Prompt bleibt auf Ihrem Gerät, wenn Modell, Tools, Protokolle und Netzwerkpfad lokal bleiben. Eine lokale GPU macht einen Computer nicht zu einem abgeschotteten System.

Modelllaufzeiten, Tool-Plugins, Browser-Erweiterungen, Fernzugriff, offene APIs und Modelldownloads bestimmen Ihr Risiko. Auch Kosten zählen. Strom kann günstiger als ein gehosteter Tokenpreis sein, während Hardwarebesitz den vollständigen Break-even weit nach hinten verschiebt.

Dieser Leitfaden kartiert zuerst die Datenschutzgrenze. Danach prüft er die Kosten mit aktuellen Anbieterpreisen, einer klaren Leistungsannahme und den gemeldeten Zahlen aus dem bereitgestellten Video.

<!--more-->

Der Kostenvergleich zwischen lokal und gehostet liefert den Kontext für die folgenden Formeln. Übernehmen Sie keine Durchsatzzahlen, ohne dieselbe Modelldatei und Laufzeit auf Ihrer Hardware zu testen.

{{< youtube id="DmkuFpoMYmc" enable="true" title="Is local AI worth it? We did the math vs Claude Haiku 5.5" description="A local-versus-hosted AI cost comparison." >}}

Das Video nennt eine Laufzeit von 2 Minuten 31 Sekunden. Titel und Laufzeit wurden über die Watch-Seite geprüft. Der Hardwaretest wurde nicht wiederholt. Die Geschwindigkeiten bleiben daher Messwerte aus der Quelle.

## Die kurze Antwort

- **Wählen Sie lokale Inferenz für einen kontrollierten Datenpfad.** Halten Sie den Modellserver auf dem Gerät, binden Sie ihn an Loopback und beschränken Sie Toolzugriff.
- **Wählen Sie gehostete Inferenz für gelegentliche Arbeit.** Vermeiden Sie Hardwareausgaben, wenn der Workload klein ist oder Ihr bevorzugtes Modell nicht passt.
- **Behandeln Sie lokale Kosten als zwei Zahlen.** Trennen Sie Strom pro aktiver Stunde von Hardwarebesitz.
- **Behandeln Sie Datenschutz als Systemeigenschaft.** Ein Plugin, das Dateien hochlädt, oder eine API auf allen Interfaces nimmt dem privaten Modell seinen Vorteil.

Lokale Inferenz hilft bei sensiblen Texten, Offline-Betrieb, festen Modellversionen und Zugriff ohne Anbieterquote. Diese Vorteile beweisen keine besseren Antworten. Ein gehostetes Modell passt zu einer Aufgabe besser, arbeitet schneller oder braucht weniger Wartung. Messen Sie den Workload vor dem Hardwarekauf.

## Verfolgen Sie den Datenpfad

| Komponente | Datenschutzfrage | Zu sammelnder Nachweis |
|---|---|---|
| **Lokaler Modellserver** | Bleibt der Prompt auf dem Host? | Prozesskonfiguration, Listenadresse und ausgehender Verkehr |
| **Cloud-Modell** | Welche Texte, Dateien und Toolergebnisse verlassen den Host? | API-Endpunkt, Anbieterbedingungen, Anfrageprotokolle und Kontoeinstellungen |
| **Cloud-Modus in lokaler App** | Läuft das gewählte Modell auf dem Gerät? | Modellkennung, Anbieterbezeichnung und Netzwerkverbindung |
| **Tool-Plugin** | Erhält das Modell Dateien, Shell-Ausgabe oder Browserinhalt? | Toolliste, Berechtigungen und aufgezeichnete Anfragedaten |
| **Modelldownload** | Welcher Code und welche Gewichte gelangen auf den Host? | Quell-Repository, Lizenz, Release-Prüfsumme und Downloadpfad |
| **Lokale Protokolle** | Wo bleiben Prompts und Toolergebnisse bestehen? | Laufzeitprotokolle, Shell-Verlauf, Absturzberichte und Backupumfang |

**Ein lokales Modell entfernt einen Anbieter aus dem Promptpfad.** Den restlichen Pfad müssen Sie trotzdem prüfen.

## Lokal bedeutet nicht automatisch privat

[Ollamas Datenschutzrichtlinie](https://ollama.com/privacy) sagt, Ollama sehe bei lokalem Modellbetrieb keine Prompts oder Daten. Die Richtlinie trennt lokalen Betrieb von Cloud-Modellen. Ein Cloud-Modell schafft eine Dienstgrenze, auch wenn dieselbe Anwendung beide Modi startet.

[Die Serverdokumentation von llama.cpp](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) zeigt `127.0.0.1:8080` als Standard. Docker-Beispiele zeigen auch `--host 0.0.0.0`, womit der Dienst auf allen Interfaces erreichbar wird. Eine breitere Bind-Adresse verändert die Zugriffsgrenze.

Prüfen Sie die Listenadresse vor sensiblen Texten:

```bash
lsof -nP -iTCP -sTCP:LISTEN | rg 'ollama|llama|8080|11434'
```

`127.0.0.1` oder `localhost` begrenzen den Zugriff im Normalfall auf denselben Host. Eine LAN-Adresse oder `0.0.0.0` braucht Firewallregel und Authentifizierungsplan. Testen Sie beides, bevor Sie einen Modellendpunkt im Netzwerk öffnen.

Prüfen Sie auch den Modellnamen. Ollamas Cloud-Dokumentation beschreibt Cloud-Modelle als separaten Dienstpfad. Eine lokale Oberfläche beweist keine lokale Ausführung.

Ollamas [FAQ](https://docs.ollama.com/faq) dokumentiert einen lokalen Modus. Setzen Sie vor dem Neustart `disable_ollama_cloud` in `~/.ollama/server.json` oder `OLLAMA_NO_CLOUD=1`. Das entfernt Ollama-Cloudmodelle und Websuche aus der gewählten Laufzeit. Andere Anwendungen, Browsertools, Plugins und Netzwerkzugriff des Hosts werden nicht begrenzt.

```json
{
  "disable_ollama_cloud": true
}
```

Prüfen Sie die Einstellung nach dem Neustart. Eine lokale Laufzeit verengt einen Pfad. Sie macht den Host nicht privat.

## Berechnen Sie gehostete Kosten

Tokenpreise trennen Eingabe und Ausgabe. [Anthropic nennt für Claude Haiku 5.5 $0.10 pro Million Eingabetoken und $0.50 pro Million Ausgabetoken bis 100.000 Token](https://www.anthropic.com/claude/haiku). Darüber gelten die höheren angegebenen Preise.

[OpenAIs Tokenleitfaden](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens) erklärt, warum Wortzahl und Tokenzahl nicht gleich sind. Er trennt Eingabe, Ausgabe, gecachte Eingabe und Reasoning-Token. Verwenden Sie Anbieter-Nutzungsfelder statt einer Wortschätzung.

Für einen einfachen Vergleich verwenden Sie eine Million erzeugte und eine Million Eingabetoken als getrennte Workloads. Ein Coding-Agent sendet oft wiederholten Kontext und erzeugt eine kleinere Antwort. Eine gemeinsame Tokenzahl verdeckt daher den Kostenmix.

## Berechnen Sie lokale Leistung

[NVIDIAs RTX-5070-Ankündigung](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/) nannte $549 als Einstiegspreis. Die [RTX-5070-Familienseite](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/) nennt 12 GB Speicher und 250 W Gesamtgrafikleistung für das Founders-Edition-Referenzdesign. Während der Prüfung zeigte die Produktseite die Karte als nicht verfügbar.

Die GPU-Leistung ist nicht die Gesamtleistung des Systems. Nutzen Sie ein Wattmeter an der Steckdose. Das Beispiel nimmt **400 W Gesamtverbrauch** an, einschließlich GPU, Prozessor, Speicher, Laufwerken, Lüftern und Netzteilverlusten. Dies ist eine Rechenannahme, kein Messwert.

Die [Prognose der U.S. Energy Information Administration](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os) verwendete für 2026 einen durchschnittlichen Haushaltsstrompreis von 18,2 Cent pro Kilowattstunde. Ihr Tarif verändert das Ergebnis.

```text
local cost per 1M output tokens =
(whole_system_watts / 1,000)
× (1,000,000 / output_tokens_per_second / 3,600)
× electricity_price_per_kWh
```

Bei 400 W und $0.182 pro Kilowattstunde kostet das System $0.0728 pro aktiver Stunde.

| Ausgabegeschwindigkeit | Zeit für 1M Token | Stromkosten für 1M Token |
|---:|---:|---:|
| **20 Token pro Sekunde** | 13 Stunden 53 Minuten | **$1.01** |
| **50 Token pro Sekunde** | 5 Stunden 33 Minuten | **$0.40** |
| **94 Token pro Sekunde** | 2 Stunden 57 Minuten | **$0.22** |

Bei 50 Ausgabetoken pro Sekunde kostet lokale Leistung weniger als Haiku 5.5 mit $0.50. Bei 20 Token pro Sekunde kostet sie mehr. Der Schwellenwert liegt unter diesen Annahmen bei etwa 40 Token pro Sekunde.

Die Eingaberechnung nutzt dieselbe Formel. Bei 2.650 Eingabetoken pro Sekunde dauern eine Million etwa 6 Minuten 17 Sekunden und kosten etwa $0.008 Strom. Bei 1.000 Token pro Sekunde kosten sie etwa $0.020.

Das bereitgestellte Transkript nennt für das RTX-5070-Beispiel 94 Ausgabe- und 2.650 Eingabetoken pro Sekunde. Die Rechnung stimmt unter der 400-W-Annahme damit überein. Es fehlen unabhängiges Laborprotokoll, Modelldatei-Hash, Laufzeit-Build, Prompt und Wattmeterwert. Behandeln Sie diese Geschwindigkeiten als Referenz, nicht als Kaufgarantie.

## Hardwareänderungen und Break-even

Stromeinsparungen zahlen Hardware nicht allein zurück. Vergleichen Sie den vollständigen Kauf mit der Differenz aus gehosteten Ausgabekosten und lokalen variablen Kosten.

```text
$0.50 hosted output price - $0.40 local power = $0.10 saved per 1M tokens
$549 GPU price / $0.10 = about 5.5 billion output tokens
```

Bei 94 Ausgabetoken pro Sekunde steigt die gerundete Ersparnis auf etwa $0.28 pro Million. Für eine $549-GPU brauchen Sie etwa 2 Milliarden Ausgabetoken. Beide Zahlen schließen Speicher, Speicherlaufwerke, Mainboard, Netzteil, Kühlung, Wartung und Wiederverkaufswert aus.

Der Einführungspreis ist kein allgemeines Angebot. NVIDIAs Seite zeigte den offiziellen Preis ohne Bestand. Ein Händlerpreis von $819 braucht eine eigene Prüfung. Verwenden Sie Ihre Rechnung und gemessene Steckdosenleistung.

**Vorhandene Hardware ändert die Entscheidung.** Wenn Workstation, Speicher und GPU passen, ist die Hardware für die nächste Aufgabe bereits bezahlt. Vergleichen Sie Leistung, Zeit, Qualität, Datenschutz und Wartung. Beim Kauf eines vollständigen Systems vergleichen Sie das ganze System mit gehosteter Nutzung.

Für Modellpassung lesen Sie den [Leitfaden zu lokalen KI-Modellen und GPU-Kontext](/articles/local-ai-model-gpu-context-guide/) und den [Leitfaden zu 16 GB VRAM](/articles/is-16gb-vram-enough-local-llm/). Für ein lokales Coding-Agent-Setup lesen Sie den [Strata-und-OpenCode-Leitfaden](/articles/strata-opencode-local-coding-agent-16gb/).

## Was lokaler Datenschutz gibt

- **Kürzerer Datenpfad:** Bei lokaler Inferenz muss der Prompt keinen Modellanbieter erreichen.
- **Offline-Betrieb:** Heruntergeladenes Modell und lokale Laufzeit brauchen für Textgenerierung keine aktive Anbieter-Verbindung.
- **Versionskontrolle:** Sie wählen Modell- und Laufzeitversion statt einer automatischen Anbieteränderung.
- **Nutzungskontrolle:** Nach Hardware- und Stromkosten vermeidet lokale Inferenz einen Cloud-Zähler pro Anfrage.
- **Netzwerkrichtlinien:** Firewall und Hostkontrollen bestimmen, wer den Modellendpunkt erreicht.

Das zählt besonders für Quellcode, Kundendaten, unveröffentlichte Entwürfe, private Notizen und getrennte Umgebungen. Lokale Inferenz braucht weiterhin Festplattenverschlüsselung, Hostupdates, getrennte Konten und beschränkte Tools.

## Was lokaler Datenschutz nicht gibt

- **Keine Qualitätsgarantie:** Kleinere oder quantisierte Modelle müssen gegen Ihre echten Abnahmekriterien getestet werden.
- **Keine Lieferkettengarantie:** Modelldateien, Laufzeiten, Plugins und Containerbilder brauchen vertrauenswürdige Quellen und Integritätsprüfungen.
- **Keinen sauberen Host:** Malware, Browsererweiterungen, Backups, Absturzberichte und Fernverwaltung sehen weiterhin Hostdaten.
- **Keinen sicheren Netzwerkendpunkt:** Ein Server auf allen Interfaces schafft einen neuen Dienst, den Sie schützen müssen.
- **Kein kostenloses System:** Strom, Speicher, Kühlung, Verschleiß und Wartung kosten Geld.

Der [Strata-Leitfaden für lokale Coding-Agents](/articles/strata-opencode-local-coding-agent-16gb/) zeigt, warum Systemspeicher, Kontext, Toolzugriff und Laufzeiteinstellungen in die Bewertung gehören. GPU-Speicher allein definiert Datenschutz- oder Leistungsgrenze nicht.

## Wählen Sie die richtige Grenze

| Situation | Erste Wahl | Grund |
|---|---|---|
| **Sensible Dokumente und vorhandener kompatibler PC** | Lokale Inferenz | Prompts im kontrollierten Host halten und neue Hardwareausgaben vermeiden |
| **Gelegentliche allgemeine Entwürfe** | Gehostete API oder Chatdienst | Kleinen Workload bezahlen und Wartung vermeiden |
| **Spitzenmodell oder spezielles Cloudtool** | Gehosteter Dienst | Modell oder Tool ist lokal nicht verfügbar |
| **Großes wiederkehrendes Volumen mit geprüftem lokalen Modell** | Lokal oder hybrid | Strom, Qualität, Supportzeit und Anbieterpreis vergleichen |
| **Gemischte Workloads** | Hybrides Routing | Sensible Aufgaben lokal halten und genehmigte allgemeine Aufgaben hosten |

**Hybrides Routing braucht eine ausdrückliche Klassifizierungsregel.** Markieren Sie Daten als nur lokal, für gehostete Verarbeitung genehmigt oder bis zur Prüfung verboten. Erzwingen Sie die Regel nicht über Modellnamen oder App-Symbole.

## Prüfen Sie vor dem Vertrauen

1. **Benennen Sie den Modellpfad.** Notieren Sie Modellkennung, Laufzeit, Version und Downloadquelle.
2. **Prüfen Sie die Bind-Adresse.** Der Server soll Loopback nutzen, außer ein breiterer Pfad ist dokumentiert.
3. **Listen Sie jedes Tool.** Prüfen Sie Datei-, Shell-, Browser-, Netzwerk- und Pluginzugriff.
4. **Prüfen Sie Persistenz.** Suchen Sie Promptprotokolle, Toolausgabe, Absturzberichte, Backups und gemeinsame Modellordner.
5. **Testen Sie das Netzwerk.** Beobachten Sie Verbindungen bei einem sensiblen Test mit repräsentativem Prompt.
6. **Messen Sie das System.** Notieren Sie Steckdosenleistung, Ausgabe, Eingabe, Kontextlänge und Wiederholungen.
7. **Testen Sie angenommene Arbeit.** Vergleichen Sie erledigte Aufgaben und Prüfaufwand, nicht nur Token pro Sekunde.

Der [Leitfaden lokale KI gegen ChatGPT](/articles/local-ai-vs-chatgpt-how-close-are-we/) behandelt Unterschiede bei Modellfähigkeiten. Nutzen Sie diese Datenschutz-Checkliste zusammen mit dem Qualitätstest.

## Quellen

- [Video, Is local AI worth it? We did the math vs Claude Haiku 5.5](https://www.youtube.com/watch?v=DmkuFpoMYmc)
- [NVIDIA Blackwell GeForce RTX 50 Series launch announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/677c9a9c3d6332e22e6c8571/)
- [NVIDIA GeForce RTX 5070 family specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/)
- [NVIDIA GeForce RTX 5070 product page](https://marketplace.nvidia.com/en-us/consumer/graphics-cards/geforce-rtx-5070/)
- [U.S. Energy Information Administration, October 2026 Short-Term Energy Outlook](https://www.eia.gov/outlooks/steo/pdf/steo_text.pdf?os=os)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude/haiku)
- [Anthropic Claude Platform pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI, Understanding and counting tokens](https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens)
- [Ollama privacy policy](https://ollama.com/privacy)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/tree/master/tools/server)
