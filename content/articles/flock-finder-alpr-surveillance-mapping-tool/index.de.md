---
title: "Flock Finder: Open-Source-Tool zur Kartierung von Flock Safety ALPR-Überwachungskameras"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder ist ein Open-Source-Tool, das über 40.000 Flock Safety ALPR-Kameras weltweit mithilfe von WiGLE-WLAN-Daten und OUI-Fingerprinting kartiert. Erfahren Sie, wie es funktioniert, wo seine Grenzen liegen und welche Hardware-Tools zur Echtzeiterkennung geeignet sind."
genre: ["Datenschutztechnologie", "Gegensurveillance", "Open-Source-Projekte", "Digitale Rechte", "Netzwerksicherheit", "Datenschutz-Tools", "Hardware-Hacking", "Sicherheitsforschung"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "Kennzeichenleser", "OUI-Fingerprinting", "WiGLE", "WLAN-Überwachung", "Gegensurveillance", "STS Collective", "FlockYou", "ESP32", "Datenschutz-Tools", "NitekryDPaul", "DeFlockJoplin", "ALPR-Erkennung", "Open-Source-Sicherheit", "Überwachungskartierung", "Massenüberwachung", "WLAN-OUI", "Datenschutz", "MAC-Adresse", "Promiscuous-Modus", "802.11", "Echtzeiterkennung", "Wardriving", "Digitale Rechte", "Bürgerrechte", "Überwachungsbewusstsein", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "Eine interaktive Karte mit bunten Markierungen, die Standorte von Flock Safety ALPR-Kameras anzeigen, mit abstrakten WLAN-Signalen, die von den Markierungen auf einem dunklen Hintergrund ausgehen."
coverCaption: "Flock Finder kartiert über 40.000 vermutete Flock Safety ALPR-Kameras mithilfe von WiGLE-WLAN-Daten und OUI-Fingerprinting."
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**Ein Open-Source-Tool zur Überwachungsbewusstsein, das Flock Safety ALPR-Kameras mithilfe von crowdgesourcten WLAN-Daten kartiert.**

## Was ist Flock Finder?

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** ist ein Open-Source-Projekt, das **Flock Safety ALPR (Automatic License Plate Reader)-Kameras** in den Vereinigten Staaten und 108 weiteren Ländern kartiert. Es kombiniert **31 bekannte Flock Safety WLAN-OUI (Organizationally Unique Identifier)-Präfixe** mit der **crowdgesourcten WiGLE-WLAN-Datenbank**, um vermutete Kamerastandorte auf einer interaktiven Karte zu identifizieren und darzustellen.

Das Projekt befindet sich unter **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**, aktualisiert sich täglich automatisch über GitHub Actions und hat stand Juli 2026 **über 40.000 vermutete Kameras** in 964 Regionen weltweit kartiert.

| Kennzahl | Wert |
|--------|-------|
| **Kartierte Kameras** | 40.026+ |
| **Bekannte OUI-Präfixe** | 31 |
| **Abgedeckte Länder** | 109 |
| **Abgedeckte Regionen** | 964 |
| **Datenspeicherung** | 730 Tage (2 Jahre) |
| **Automatische Aktualisierungsfrequenz** | Täglich |

*Dies ist ein allgemeines Bewusstseins-Tool, kein definitives Inventar. Lesen Sie den Abschnitt über Einschränkungen, bevor Sie Schlussfolgerungen aus den Daten ziehen.*

______

## Wie es funktioniert: OUI-Fingerprinting über WiGLE

### Die zentrale Erkenntnis

Flock Safety-Kameras enthalten **WLAN-Transceiver**, die periodisch aus dem Schlafzustand erwachen, um aufgenommene Kennzeichendaten in die Cloud hochzuladen. Während dieser kurzen aktiven Fenster sendet die Kamera WLAN-Frames aus, die ihre **MAC-Adresse** enthalten. Die ersten drei Bytes jeder MAC-Adresse identifizieren den Hersteller. Dies ist der **OUI (Organizationally Unique Identifier)**.

Sicherheitsforscher **@NitekryDPaul** entdeckte **30 OUI-Präfixe**, die konsistent mit Flock Safety-Kamera-Hardware durch **Promiscuous-Modus-2,4-GHz-Analyse** assoziiert wurden. Ein 31. Präfix (`82:6B:F2`) wurde von **Michael / DeFlockJoplin** während Feldtests in Joplin, MO beigesteuert.

Flock Finder nimmt diese 31 OUIs, fragt WiGLE nach aufgezeichneten WLAN-Netzwerken ab, die diesen Präfixen entsprechen, und stellt die Ergebnisse auf einer Karte dar.

### Die addr1-Erkennungstechnik

Die wichtigste Entdeckung von @NitekryDPaul geht über das einfache Abgleichen mit der Sender-MAC-Adresse hinaus. Flock-Kameras verbringen den Großteil ihres Betriebszyklus im **Schlafmodus**. Wenn ein nahe gelegener Zugangspunkt einen Frame *an* eine Kamera sendet, erscheint die MAC-Adresse der Kamera als **addr1 (die Empfängeradresse)** in 802.11-Frames, selbst während die Kamera selbst nicht aktiv sendet.

In Kombination mit der **Wildcard-Probe-Request-Erkennung** (802.11-Management-Frames Typ=0, Subtyp=4, leere SSID) ergibt sich eine sehr präzise Erkennungssignatur. Feldtests in Joplin, MO erzielten **11 von 12 erkannten Kameras mit nur 2 Falschwarnungen**.

> ⚠️ **Wichtig**: Die WiGLE-basierte Flock Finder-Karte implementiert **nicht** die addr1-Technik. WiGLE ist ein historischer, passiv gesammelter Datensatz. Er zeichnet nur Sender auf, nicht Empfänger. Für die Echtzeiterkennung, die tatsächlich die Methode von @NitekryDPaul verwendet, benötigen Sie dedizierte Hardware im Einsatz.

______

## Nutzung der Live-Karte

Die interaktive Karte ist live unter **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)** verfügbar. Sie zeigt:

- **Gruppierte Kamera-Markierungen**, farblich nach OUI-Präfix kodiert
- **Suche** nach Stadt, Bundesstaat oder BSSID
- **OUI-Datentabelle** mit Kameraanzahlen pro Präfix
- **Statistikfeld** mit Gesamtkameras, Regionen und letztem Aktualisierungszeitstempel
- **Seite über ALPRs** mit dokumentierten Datenschutzschäden, rechtlichem Kontext und Community-Ressourcen

Die Kartendatenexporte sind ebenfalls direkt verfügbar:

- `data/flock_cameras.geojson` — GeoJSON zur Verwendung in QGIS, Leaflet oder anderen Tools
- `data/flock_cameras.csv` — tabellenfreundliches Format
- `data/scan_stats.json` — Scan-Statistiken und Zählungen

### Wichtige Einschränkungen

**Betrachten Sie die Karte mit Vorsicht.** WiGLE ist ein crowdgesourcter, sporadisch aktualisierter Datensatz, kein Live-Feed.

- **Flock-Kameras senden nicht kontinuierlich.** Sie erwachen kurz zum Hochladen von Daten, sodass WiGLE-Einträge vollständig davon abhängen, dass ein Wardriver genau im richtigen Moment in der Nähe ist.
- **Daten können Monate oder Jahre alt sein.** Kameras, die verschoben oder entfernt wurden, können noch erscheinen.
- **OUI-Abgleich ist eine Heuristik.** OUIs können geteilt, neu zugewiesen oder gefälscht werden. Jedes Ergebnis ist ein *vermutetes* Flock-Gerät, kein bestätigtes.
- **Die Abdeckung ist ungleichmäßig.** Dichte Ballungsgebiete haben mehr WiGLE-Daten; ländliche Gebiete haben weit weniger.

*Verwenden Sie die Karte, um ein allgemeines Bewusstsein für die Überwachungsdichte in Ihrer Umgebung zu entwickeln. Für bodennahe Echtzeiterkennung siehe die Hardware-Optionen unten.*

______

## Flock Finder selbst ausführen

### Voraussetzungen

- Python 3.8+
- Ein kostenloses [WiGLE](https://wigle.net/account)-Konto mit API-Zugangsdaten

### Einrichtung

```bash
# Repository klonen
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Abhängigkeiten installieren
pip install -r requirements.txt

# WiGLE-API-Zugangsdaten einrichten
cp .env.example .env
# .env mit Ihrem WiGLE-API-Namen und Token bearbeiten
```

### Scanner ausführen

```bash
# Vollständiger Scan — alle 31 OUI-Präfixe, weltweit
python3 scripts/wigle_query.py

# Einzelner OUI-Test
python3 scripts/wigle_query.py --oui 70:C9:4E

# Nur USA
python3 scripts/wigle_query.py --country US

# Spezifisches Begrenzungsrechteck (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Trockenlauf — Auth überprüfen, keine API-Abfragen
python3 scripts/wigle_query.py --dry-run
```

### Karte lokal anzeigen

```bash
python3 -m http.server 8080 --directory docs/
# http://localhost:8080 im Browser öffnen
```

### Automatische tägliche Updates über GitHub Actions

Forken Sie das Repository und fügen Sie Ihre WiGLE-Zugangsdaten als **Repository-Geheimnisse** hinzu (`WIGLE_API_NAME` und `WIGLE_API_TOKEN`). Der enthaltene Workflow läuft täglich um 6 Uhr UTC und committed automatisch aktualisierte Datendateien, wenn neue Kameras gefunden werden.

______

## Echtzeiterkennung: STS Collective FlockYou Hardware

Die WiGLE-Karte zeigt Ihnen, wo Kameras *beobachtet wurden*. Für Echtzeiterkennung beim Fahren, mit der tatsächlichen OUI-Abgleich-Methode von @NitekryDPaul auf Live-WLAN-Verkehr, benötigen Sie dedizierte Hardware.

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** stellt tragbare ESP32-basierte Detektoren her, die nach Flock OUI-Signaturen suchen und Sie sofort alarm, wenn eine passende Signatur erkannt wird.

### FlockYou-Gerätepalette

| Gerät | Beschreibung |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | Kompakter, taschengroßer Flock-Detektor. Vorgeflasht, Plug-and-Play. LED-Alarm bei Erkennung. |
| **FlockYou Pro — LED + Audio** | Fügt Audioalarme neben LED-Indikatoren hinzu. Keine Kamera beim Fahren verpassen. |
| **FlockYou Atom VoiceS3R** | Sprachfähiger Detektor mit gesprochenen Audioalarmen für freihändigen, augenauf-der-Straße-Betrieb. |

Alle Geräte:
- **Vorgeflasht**, sofort einsatzbereit
- Scannen Live-WLAN-Verkehr auf alle 31 bekannten Flock OUIs
- Kompakt und tragbar — passt in einen Becherhalter oder eine Tasche
- Wird über USB-C betrieben (Autoadapter, Powerbank oder Laptop)

> 💰 **Exklusive Rabatte**: Verwenden Sie Code **FLOCKFINDER** für **20% Rabatt** auf alle STS Collective FlockYou-Geräte — oder verwenden Sie Code **SIMEONONSECURITY** für bis zu 20% Rabatt auf Ihre gesamte Bestellung. [Shop unter stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Projektstruktur

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE-API-Abfrage und Datenpipeline
├── data/
│   ├── flock_ouis.csv         # 31 bekannte Flock Safety OUI-Präfixe
│   ├── flock_cameras.geojson  # Kamerastandorte (GeoJSON)
│   ├── flock_cameras.csv      # Kamerastandorte (CSV)
│   └── scan_stats.json        # Scan-Statistiken
├── docs/
│   └── index.html             # Interaktive Leaflet-Karte
└── .github/workflows/
    └── update-data.yml        # Täglicher Auto-Update-Workflow
```

______

## Häufig gestellte Fragen

### Ist das legal?

Ja. **Flock Finder verwendet nur öffentlich zugängliche Daten** aus der WiGLE-Datenbank, die freiwillig beigesteuerte WLAN-Vermessungsdaten aggregiert. Es ist kein Hacking, kein unbefugter Zugriff und keine proprietären Systeme involviert. Passives WLAN-Monitoring auf OUI-Signaturen ist in den USA legal.

### Ist jede kartierte Kamera definitiv eine Flock-Kamera?

Nein. OUI-Abgleich ist eine **Heuristik**. OUI-Präfixe können von verschiedenen Herstellern geteilt, neu zugewiesen oder gefälscht werden. Jeder Eintrag in der Datenbank ist ein *vermutetes* Flock-Gerät, kein bestätigtes.

### Warum zeigen einige OUI-Präfixe keine Kameras?

WiGLE-Abdeckung ist ungleichmäßig. Wenn kein Wardriver ein bestimmtes Gebiet mit diesem spezifischen OUI aktiv gescannt hat, gibt es keine Einträge. *Fehlen von Daten bedeutet nicht Fehlen von Kameras.*

### Wie aktuell sind die Daten?

Der GitHub Actions-Workflow läuft täglich und zieht die neuesten WiGLE-Ergebnisse. WiGLE selbst kann jedoch Einträge haben, die für einen bestimmten Standort zwischen Tagen und Jahren alt sind. Überprüfen Sie die Datei `scan_stats.json` für den Zeitstempel des letzten Scans.

### Kann ich eigene Wardrive-Daten beitragen?

Ja. Laden Sie Ihre Wardrive-Daten auf [WiGLE](https://wigle.net) hoch. Sie werden automatisch in den nächsten täglichen Scan von Flock Finder eingespeist. Sie können auch OUI-Präfixe oder Code-Verbesserungen über den [Contributing Guide](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md) beitragen.

______

## Community und verwandte Projekte

Flock Finder steht nicht allein. Ein wachsendes Ökosystem von Tools und Organisationen arbeitet daran, ALPR-Überwachung zu dokumentieren und entgegenzuwirken:

- **[DeFlock.org](https://deflockjoplin.org/)** — Community-getriebenes ALPR-Tracking, Dokumentation und Interessenvertretung
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — Überprüfen Sie, ob Ihr Kennzeichen im Flock-System gesucht wurde
- **[FlockHopper](https://flockhopper.com/)** — Routenplanung, die bekannte ALPR-Kameras meidet
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — Die EFF-Datenbank der von Strafverfolgungsbehörden eingesetzten Überwachungstechnologie
- **[NoALPRs.com](https://noalprs.com/)** — Ressourcen für Gemeinschaften, die ALPR-Einsätze bekämpfen
- **[DeFlockJoplin](https://deflockjoplin.org/)** — Open-Source-Firmware und Feldforschung; hat das 31. OUI-Präfix beigesteuert

______

## Danksagungen

- **OUI-Forschung**: @NitekryDPaul — alle 30 originalen OUI-Präfixe und die addr1/Promiscuous-Modus-Erkennungsstrategie
- **Feldtests**: Michael / DeFlockJoplin — 31. OUI-Präfix (`82:6B:F2`) und Präzisierung der Wildcard-Probe
- **Datenquelle**: [WiGLE](https://wigle.net) — crowdgesourcte WLAN/Mobilfunknetz-Datenbank
- **Inspiriert von**: [DeFlock](https://deflockjoplin.org/) und track-openroaming-passpoint
- **Hardware-Partner**: [STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32-Detektoren

______

## Fazit

**Flock Finder** gibt jedem einen schnellen, visuellen Eindruck davon, wie weit Flock Safety ALPR-Kameras verbreitet sind. Über 40.000 geschätzte Standorte in 109 Ländern, täglich automatisch aus crowdgesourcten WLAN-Daten aktualisiert.

Es ist ein **Transparenz-Tool**, kein Live-Tracker. Seine Daten sind historisch, unvollständig und probabilistisch. Aber es macht das Ausmaß der ALPR-Überwachung auf eine Weise sichtbar, die Berichte und Abstracts nicht können.

Für echten Echtzeitschutz beim Durchfahren überwachter Bereiche kombinieren Sie die Karte mit dedizierter Hardware. **[STS Collectives FlockYou-Geräte](https://stscollective.com/discount/SIMEONONSECURITY)** implementieren die Erkennungsmethode von @NitekryDPaul direkt auf einem ESP32 und alarmieren Sie, sobald eine Live-Kamerasignatur erkannt wird — erhältlich unter **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** mit Code **FLOCKFINDER** oder **SIMEONONSECURITY** für bis zu 20% Rabatt.

______

## Referenzen

1. [Flock Finder GitHub-Repository](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finder Interaktive Karte](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYou-Geräte](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — Drahtlosnetzwerk-Kartierung](https://wigle.net)
5. [DeFlock — Community ALPR-Bewusstsein](https://deflockjoplin.org/)
6. [DeFlockJoplin — Open-Source-Erkennungs-Firmware](https://deflockjoplin.org/)
7. [Electronic Frontier Foundation — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — Sie werden verfolgt](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
