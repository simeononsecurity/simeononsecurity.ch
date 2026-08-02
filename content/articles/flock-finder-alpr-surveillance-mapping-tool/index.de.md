---
title: "Flock Finder: Karte der Flock Safety ALPR-Kameras"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder ist ein Open-Source-Tool, das weltweit über 40.000 Flock Safety ALPR-Kameras mithilfe von WiGLE-WiFi-Daten und OUI-Fingerprinting kartiert. Erfahren Sie, wie es funktioniert, welche Einschränkungen es gibt und welche Hardware-Tools zur Echtzeiterkennung verfügbar sind."
genre: ["Datenschutztechnologie", "Gegenüberwachung", "Open-Source-Projekte", "Digitale Rechte", "Netzwerksicherheit", "Datenschutz-Tools", "Hardware-Hacking", "Sicherheitsforschung"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Kennzeichenleser", "OUI-Fingerprinting", "WiGLE", "WiFi-Überwachung", "Gegenüberwachung", "STS Collective", "FlockYou", "ESP32", "Datenschutz-Tools", "NitekryDPaul", "DeFlockJoplin", "ALPR-Erkennung", "Open-Source-Sicherheit", "Überwachungskartierung", "Massenüberwachung", "WiFi OUI", "Datenschutz", "MAC-Adresse", "Promiskuitiver Modus", "802.11", "Echtzeiterkennung", "Wardriving", "Digitale Rechte", "Bürgerrechte", "Überwachungsbewusstsein", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Eine interaktive Karte mit farbigen Markierungen, die die Standorte von Flock Safety ALPR-Kameras anzeigen, mit abstrakten WLAN-Signalen, die von den Markierungen auf einem dunklen Hintergrund ausgehen."
coverCaption: "Flock Finder kartiert über 40.000 mutmaßliche Flock Safety ALPR-Kameras mithilfe von WiGLE-WiFi-Daten und OUI-Fingerprinting."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Ein Open-Source-Tool zur Überwachungssensibilisierung, das Flock Safety ALPR-Kameras mithilfe von per Crowdsourcing gesammelten WiFi-Daten kartiert.**

## Was ist Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** ist ein Open-Source-Projekt, das **Flock Safety ALPR (Automatischer Kennzeichenleser)-Kameras** in den Vereinigten Staaten und 108 weiteren Ländern kartiert. Es kombiniert **31 bekannte Flock Safety WiFi-OUI (Organisatorisch Eindeutige Kennung)-Präfixe** mit der **per Crowdsourcing erstellten WiGLE-WiFi-Datenbank**, um mutmaßliche Kamerastandorte zu identifizieren und auf einer interaktiven Karte darzustellen.

Das Projekt befindet sich unter **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, wird täglich automatisch über GitHub Actions aktualisiert und hat bis Juli 2026 **über 40.000 mutmaßliche Kameras** in 964 Regionen weltweit kartiert.

| Metrik | Wert |
|--------|-------|
| **Kartierte Kameras** | 40.026+ |
| **Bekannte OUI-Präfixe** | 31 |
| **Abgedeckte Länder** | 109 |
| **Abgedeckte Regionen** | 964 |
| **Datenaufbewahrung** | 730 Tage (2 Jahre) |
| **Automatische Aktualisierungsfrequenz** | Täglich |

*Dies ist ein allgemeines Sensibilisierungstool, kein definitives Inventar. Lesen Sie den Abschnitt zu den Einschränkungen, bevor Sie Schlussfolgerungen aus den Daten ziehen.*

Für Hintergrundinformationen darüber, warum Flock Safety ALPR-Überwachung für den Datenschutz wichtig ist, lesen Sie **[Flock Safety-Kameraüberwachung: Verbreitung, Datenschutzbedenken und Schutzstrategien](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

______

## So funktioniert es: OUI-Fingerprinting über WiGLE

### Der Kerngedanke

Flock Safety-Kameras enthalten **WLAN-Transceiver**, die periodisch aus dem Schlaf erwachen, um erfasste Kennzeichendaten in die Cloud hochzuladen. Während dieser kurzen aktiven Fenster sendet die Kamera WLAN-Frames aus, die ihre **MAC-Adresse** enthalten — und die ersten drei Bytes jeder MAC-Adresse identifizieren den Hersteller. Dies ist der **OUI (Organizationally Unique Identifier)**.

Sicherheitsforscher **@NitekryDPaul** entdeckte **30 OUI-Präfixe**, die durchgehend mit der Hardware von Flock Safety-Kameras durch **Promiscuous-Mode-2,4-GHz-Analyse** assoziiert werden. Ein 31. Präfix (`82:6B:F2`) wurde von **Michael / DeFlockJoplin** während Feldtests in Joplin, MO beigetragen.

Flock Finder nimmt diese 31 OUIs, fragt WiGLE nach aufgezeichneten WLAN-Netzwerken, die mit diesen Präfixen übereinstimmen, und stellt die Ergebnisse auf einer Karte dar.

### Die 31 bekannten Flock Safety OUI-Präfixe

| # | OUI-Präfix | Quelle | # | OUI-Präfix | Quelle |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### Die addr1-Erkennungstechnik

@NitekryDPauls Schlüsselentdeckung geht über das einfache Abgleichen der Sender-MAC-Adresse hinaus. Flock-Kameras verbringen den Großteil ihres Arbeitszyklus im **Schlaf**. Wenn ein nahegelegener Access Point einen Frame sendet, der *an* eine Kamera adressiert ist, erscheint die MAC der Kamera als **addr1 (die Empfängeradresse)** in 802.11-Frames — auch wenn die Kamera selbst nicht aktiv sendet.

In Kombination mit der **Wildcard-Probe-Request-Erkennung** (802.11-Management-Frames Typ=0, Subtyp=4, leere SSID) ergibt dies eine sehr präzise Erkennungssignatur. Feldtests in Joplin, MO erzielten **11 von 12 erkannten Kameras bei nur 2 Fehlalarmen**.

> ⚠️ **Wichtig**: Die WiGLE-basierte Flock Finder-Karte implementiert die addr1-Technik **nicht**. WiGLE ist ein historischer, passiv gesammelter Datensatz — er zeichnet nur Sender auf, keine Empfänger. Für die Echtzeiterkennung, die tatsächlich @NitekryDPauls Methode verwendet, benötigen Sie dedizierte Hardware im Einsatz.

______

## Die Live-Karte verwenden

Die interaktive Karte ist live unter **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)** verfügbar. Sie zeigt:

- **Geclusterte Kamera-Markierungen** farblich nach OUI-Präfix codiert
- **Suche** nach Stadt, Bundesland oder BSSID
- **OUI-Datentabelle** mit Kameraanzahlen pro Präfix
- **Statistik-Panel** mit der Gesamtzahl der Kameras, Regionen und dem letzten Aktualisierungszeitstempel
- **Seite über ALPRs** mit dokumentierten Datenschutzverletzungen, rechtlichem Kontext und Community-Ressourcen

Die Kartenexporte sind auch direkt verfügbar:

- `data/flock_cameras.geojson` — GeoJSON für die Verwendung in QGIS, Leaflet oder anderen Tools
- `data/flock_cameras.csv` — tabellenfreundliches Format
- `data/scan_stats.json` — Scan-Statistiken und Zählungen

### Wichtige Einschränkungen

**Betrachten Sie die Karte mit Vorsicht.** WiGLE ist ein per Crowdsourcing erstellter, sporadisch aktualisierter Datensatz, kein Live-Feed.

- **Flock-Kameras senden nicht kontinuierlich.** Sie wachen kurz auf, um Daten hochzuladen, daher hängen WiGLE-Einträge völlig davon ab, dass genau im richtigen Moment ein Wardriver in der Nähe ist.
- **Daten können Monate oder Jahre alt sein.** Kameras, die verlagert oder entfernt wurden, können noch erscheinen.
- **OUI-Abgleich ist eine Heuristik.** OUIs können geteilt, neu zugewiesen oder gefälscht werden. Jedes Ergebnis ist ein *mutmaßliches* Flock-Gerät, kein bestätigtes.
- **Die Abdeckung ist ungleichmäßig.** Dichte Ballungsräume haben mehr WiGLE-Daten; ländliche Gebiete haben weit weniger.

*Nutzen Sie die Karte, um ein allgemeines Bewusstsein für die Überwachungsdichte in Ihrer Region zu entwickeln. Für bodennahe, Echtzeiterkennung sehen Sie die Hardware-Optionen unten.*

______

## Flock Finder selbst ausführen

### Voraussetzungen

- Python 3.8+
- Ein kostenloses [WiGLE](https://wigle.net/account)-Konto mit API-Anmeldedaten

### Einrichtung

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### Den Scanner ausführen

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### Karte lokal anzeigen

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### Automatische tägliche Updates über GitHub Actions

Forken Sie das Repository und fügen Sie Ihre WiGLE-Anmeldedaten als **Repository-Secrets** (`WIGLE_API_NAME` und `WIGLE_API_TOKEN`) hinzu. Der enthaltene Workflow läuft täglich um 6 Uhr UTC und committet automatisch aktualisierte Datendateien, wenn neue Kameras gefunden werden.

______

## Echtzeiterkennung: STS Collective FlockYou-Hardware

Die WiGLE-Karte zeigt Ihnen, wo Kameras *beobachtet wurden*. Für die Echtzeiterkennung beim Fahren — unter Verwendung von @NitekryDPauls tatsächlicher OUI-Abgleichmethode auf Live-WLAN-Traffic — benötigen Sie dedizierte Hardware.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** stellt tragbare ESP32-basierte Detektoren her, die nach Flock-OUI-Signaturen suchen und Sie sofort alarmieren, wenn eine übereinstimmende Signatur erkannt wird.

### FlockYou-Gerätelinie

| Gerät | Beschreibung |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Kompakter, taschengroßer Flock-Detektor. Vorgeflasht, Plug-and-Play. LED-Alarme bei Erkennung. |
| **FlockYou Pro — LED + Audio** | Fügt Audioalarme neben LED-Indikatoren hinzu. Verpassen Sie nie eine Kamera beim Fahren. |
| **FlockYou Atom VoiceS3R** | Sprachfähiger Detektor mit gesprochenen Audioalarmen für freihändigen Betrieb mit Blick auf die Straße. |

Alle Geräte:
- **Vorgeflasht**, einsatzbereit aus der Box
- Scannen Live-WLAN-Traffic nach allen 31 bekannten Flock-OUIs
- Kompakt und tragbar — passt in einen Getränkehalter oder eine Tasche
- Wird über USB-C gespeist (Autoadapter, Powerbank oder Laptop)

> 💰 **Exklusive Rabatte**: Verwenden Sie den Code **FLOCKFINDER** für **20% Rabatt** auf alle STS Collective FlockYou-Geräte — oder verwenden Sie den Code **SIMEONONSECURITY** für bis zu 20% Rabatt auf Ihre gesamte Bestellung. [Kaufen Sie bei stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

Für eine vollständige technische Analyse dieser Geräte und DIY-Alternativen lesen Sie den **[Flock-You Erkennungsprojekt: Vollständiger Leitfaden für Gegenüberwachungs-Hardware und Einrichtung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**.

______

## Projektstruktur

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## Häufig gestellte Fragen

### Ist das legal?

Ja. **Flock Finder verwendet ausschließlich öffentlich verfügbare Daten** aus der WiGLE-Datenbank, die freiwillig beigetragene WLAN-Umfragedaten aggregiert. Es sind kein Hacking, kein unbefugter Zugriff und keine proprietären Systeme beteiligt. Passives WLAN-Monitoring auf OUI-Signaturen ist in den Vereinigten Staaten legal.

### Ist jede kartierte Kamera definitiv eine Flock-Kamera?

Nein. OUI-Abgleich ist eine **Heuristik**. OUI-Präfixe können von Herstellern geteilt, neu zugewiesen oder gefälscht werden. Jeder Eintrag in der Datenbank ist ein *mutmaßliches* Flock-Gerät — kein bestätigtes. Lesen Sie die [Datenschutzrichtlinie](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md) für Details, wie Sie eine Korrektur beantragen können.

### Warum zeigen einige OUI-Präfixe keine Kameras?

Die WiGLE-Abdeckung ist ungleichmäßig. Wenn kein Wardriver ein bestimmtes Gebiet mit diesem spezifischen aktiven OUI gescannt hat, gibt es keine Einträge. *Das Fehlen von Daten bedeutet nicht das Fehlen von Kameras.*

### Wie aktuell sind die Daten?

Der GitHub Actions-Workflow läuft täglich und ruft die neuesten WiGLE-Ergebnisse ab. WiGLE selbst kann jedoch Einträge haben, die für einen bestimmten Standort von Tagen bis Jahren alt sind. Überprüfen Sie die `scan_stats.json`-Datei für den Zeitstempel des letzten Scans.

### Kann ich meine eigenen Wardrive-Daten beitragen?

Ja. Laden Sie Ihre Wardrive-Daten bei [WiGLE](https://wigle.net) hoch — sie fließen automatisch in Flock Finders nächsten täglichen Scan ein. Sie können auch OUI-Präfixe oder Code-Verbesserungen über den [Beitragsleitfaden](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md) beitragen.

______

## Community und verwandte Projekte

Flock Finder steht nicht allein. Ein wachsendes Ökosystem von Tools und Organisationen arbeitet daran, ALPR-Überwachung zu dokumentieren und entgegenzuwirken:

- **[DeFlock.org](https://deflockjoplin.org/)** — Community-gesteuerte ALPR-Verfolgung, Dokumentation und Interessenvertretung
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Überprüfen Sie, ob Ihr Kennzeichen im Flock-System gesucht wurde
- **[FlockHopper](https://flockhopper.com/)** — Routenplanung, die bekannte ALPR-Kameras vermeidet
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — EFFs Datenbank der von Strafverfolgungsbehörden eingesetzten Überwachungstechnologie
- **[NoALPRs.com](https://noalprs.com/)** — Ressourcen für Gemeinschaften, die gegen ALPR-Einsätze kämpfen
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Open-Source-Firmware und Feldforschung; hat das 31. OUI-Präfix beigetragen

______

## Danksagungen

- **OUI-Forschung**: @NitekryDPaul — alle 30 ursprünglichen OUI-Präfixe und die addr1/Promiscuous-Mode-Erkennungsstrategie
- **Feldtests**: Michael / DeFlockJoplin — 31. OUI-Präfix (`82:6B:F2`) und Wildcard-Probe-Verschärfung
- **Datenquelle**: [WiGLE](https://wigle.net) — per Crowdsourcing erstellte WiFi/Mobilfunknetz-Datenbank
- **Inspiriert von**: [DeFlock](https://deflockjoplin.org/) und track-openroaming-passpoint
- **Hardware-Partner**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32-Detektoren

______

## Fazit

**Flock Finder** gibt jedem einen schnellen, visuellen Eindruck davon, wie weit Flock Safety ALPR-Kameras eingesetzt werden — über 40.000 geschätzte Standorte in 109 Ländern, täglich automatisch aus per Crowdsourcing gesammelten WLAN-Daten aktualisiert.

Es ist ein **Transparenz-Tool**, kein Live-Tracker. Seine Daten sind historisch, unvollständig und probabilistisch. Aber es macht das Ausmaß der ALPR-Überwachung auf eine Weise sichtbar, die Zusammenfassungen und Berichte nicht können.

Für echten Echtzeitschutz, während Sie sich durch überwachte Gebiete bewegen, kombinieren Sie die Karte mit dedizierter Hardware. **[STS Collectives FlockYou-Geräte](https://stscollective.com/discount/SIMEONONSECURITY)** implementieren @NitekryDPauls Erkennungsmethode direkt auf einem ESP32 und alarmieren Sie sofort, wenn eine Live-Kamerasignatur erkannt wird — erhältlich unter **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** mit dem Code **FLOCKFINDER** oder **SIMEONONSECURITY** für bis zu 20% Rabatt.

### Verwandte Artikel

| Artikel | Was er abdeckt |
|---------|---------------|
| **[Flock Safety-Kameraüberwachung: Datenschutz und Schutz](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Das vollständige Bild: Verbreitungsstatistiken, Bürgerrechtsfragen, ACLU-Toolkit, DeFlock-Statistiken, FOIA-Leitfaden und Schutzstrategien |
| **[Flock-You Erkennungsprojekt: Leitfaden für Gegenüberwachungs-Hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Vollständiger technischer Leitfaden für ESP32-basierte Flock-Detektoren — OUI-SPY, M5 Atom Lite, DIY-Build, schrittweise Firmware-Einrichtung |
| **[Rayhunter-Geräte flashen: Vollständiger Leitfaden](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | IMSI-Catcher (Mobilfunkstations-Simulatoren) neben ALPR-Kameras erkennen für vollständiges Gegenüberwachungsbewusstsein |
| **[DagShell Custom-Firmware für Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Einen mobilen Hotspot in eine Sicherheitsforschungsplattform verwandeln — passt gut zu Flock-Erkennungs-Hardware |
| **[Rayhunter-Gerätevergleich 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Erkennungs-Hardware-Optionen über ALPR- und Mobilfunk-Überwachungsbedrohungskategorien vergleichen |

______

## Referenzen

1. [Flock Finder GitHub-Repository](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finder Interaktive Karte](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYou-Geräte](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Kartierung drahtloser Netzwerke](https://wigle.net)
5. [DeFlock — Community-ALPR-Bewusstsein](https://deflockjoplin.org/)
6. [DeFlockJoplin — Open-Source-Erkennungs-Firmware](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Sie werden verfolgt](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
