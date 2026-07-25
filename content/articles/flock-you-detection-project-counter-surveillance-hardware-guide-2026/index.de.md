---
title: "Flock-You Erkennungsprojekt: Vollständiger Gegensurveillance-Hardware- und Einrichtungsleitfaden 2026"
date: 2026-05-24
lastmod: 2026-05-24
toc: true
draft: false
description: "Umfassender technischer Leitfaden zum Open-Source-Projekt Flock-You zur Erkennung von Flock Safety ALPR-Kameras mit ESP32-basierter Hardware. Enthält Einrichtungsanweisungen, Firmware-Details und Einkaufsinformationen."
genre: ["Sicherheits-Hardware", "Gegensurveillance", "Datenschutztechnologie", "Open-Source-Projekte", "ESP32-Entwicklung", "WLAN-Monitoring", "Datenschutz-Tools", "Digitale Rechte", "Hardware-Hacking", "Netzwerksicherheit"]
tags: ["Flock-You Projekt", "ALPR-Erkennung", "ESP32-S3", "WLAN-OUI-Erkennung", "Gegensurveillance-Hardware", "Flock Safety Erkennung", "Open-Source-Sicherheit", "Datenschutz-Hardware", "M5 Atom Lite", "OUI-SPY", "Promiscuous Mode WLAN", "802.11 Monitoring", "Colonel Panic Tech", "STS Collective", "Datenschutz-Geräte", "Surveillance-Erkennung", "WLAN-Scanning", "GitHub Projekt", "ESP32 Firmware", "Hardware-Einrichtungsleitfaden", "DIY Datenschutz-Tools", "OUI-Datenbank", "ALPR-Kamera-Erkennung"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Eine Illustration, die ein ESP32-basiertes Gerät im Vordergrund zeigt, das WLAN-Signale scannt. Bunte Wellen repräsentieren verschiedene Signalstärken vor einem dunklen Hintergrund."
coverCaption: "Open-Source-Hardware-Lösungen zur Erkennung von ALPR-Überwachungskameras"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Vollständiger technischer Leitfaden zum Aufbau und Einsatz von Flock-You-Erkennungsgeräten**

## Einführung: Open-Source-Gegensurveillance

Das **Flock-You-Projekt** ist eine **quelloffene, community-getriebene Initiative** zur Erkennung und Kartierung der ALPR-Überwachungsinfrastruktur von Flock Safety. Auf GitHub gehostet unter **colonelpanichacks/flock-you**, nutzt dieses Projekt erschwingliche ESP32-basierte Hardware, um Flock-Kameras durch ihre **WLAN-Netzwerksignaturen** zu identifizieren.

Dieser umfassende Leitfaden behandelt alles von der **technischen Methodik** hinter der Flock-Erkennung bis hin zu **schrittweisen Einrichtungsanweisungen** für drei Hardware-Plattformen, **Firmware-Installation** und **Kaufinformationen von autorisierten Anbietern**. Ob Sie ein Datenschutzadvokat, Sicherheitsforscher oder besorgter Bürger sind - dieser Leitfaden ermöglicht Ihnen den Aufbau oder Kauf Ihres eigenen Erkennungsgeräts.

Für den Kontext, warum diese Technologie wichtig ist, lesen Sie unseren Begleitartikel: **[Flock Safety Kamera-Überwachung: Verbreitung, Datenschutzbedenken und Schutzstrategien](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Möchten Sie sehen, wo Flock-Kameras bereits kartiert wurden? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** ist ein Open-Source-Tool, das 40.000+ vermutete Flock Safety-Kameras weltweit mithilfe von WiGLE-WLAN-Daten und OUI-Fingerprinting darstellt - täglich aktualisiert. Quellcode auf **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

______

## Die Flock-You-Erkennungsmethodik verstehen

### Das technische Fundament

Flock Safety-Kameras enthalten **eingebettete WLAN-Module** für Konnektivität und Fernverwaltung. Diese Module senden identifizierbare Netzwerksignaturen aus, die von Geräten im **WLAN-Promiscuous-Monitoring-Modus** erkannt werden können. Das Flock-You-Projekt nutzt diese Eigenschaft durch:

#### 1. WLAN-OUI (Organisationally Unique Identifier) Erkennung

Jede Netzwerkschnittstelle hat eine **MAC-Adresse** bestehend aus:
- **Ersten 3 Bytes (24 Bit)**: OUI, der den Hersteller identifiziert
- **Letzten 3 Bytes**: Gerätespezifischer Bezeichner

Forscher **@NitekryDPaul** und die **DeFlockJoplin**-Community haben **31 spezifische OUIs** entdeckt, die konsistent in Flock Safety-Kamera-Bereitstellungen vorhanden sind:

```
Primäre Espressif OUIs (ESP32-basierte Module):
D4:AD:FC - Espressif Inc. (Häufig ESP32-S3)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (ESP32-S3 Varianten)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (ESP32-basiert)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (ESP32-basiert)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

Weitere in Flock-Bereitstellungen identifizierte OUIs:
[... 21 weitere Hersteller-OUIs ...]
```

Wenn ein Erkennungsgerät den WLAN-Verkehr im Promiscuous-Modus scannt, **identifiziert es jedes Gerät, das Frames mit diesen OUIs sendet**.

#### 2. Wildcard-Probe-Request-Erkennung

Flock-Kameras senden regelmäßig **Wildcard-Probe-Requests** zur Suche nach verfügbaren Netzwerken. Diese haben charakteristische Merkmale:

- **802.11 Management Frame**: Typ=0, Subtyp=4
- **SSID Information Element**: Länge=0 (leer/Wildcard)
- **Frame-Struktur**: Vorhersehbares Muster im Probe-Timing
- **Herstellerspezifische IEs**: Zusätzliche Indikatoren im Frame-Payload

Erkennungs-Firmware analysiert diese **Probe-Request-Muster**, um die Sicherheit bei der Identifizierung von Flock-Kameras über einfaches OUI-Matching hinaus zu erhöhen.

#### 3. Promiscuous Mode WLAN-Monitoring

Der Standard-WLAN-Betrieb empfängt nur an Ihr Gerät adressierte Frames. Der **Promiscuous Mode** erfasst alle WLAN-Frames in Reichweite:

- **802.11 Frame-Struktur**: Analyse der addr1, addr2, addr3-Felder
- **Management Frames**: Probe Requests, Beacon Frames, Association Requests
- **Data Frames**: Zeigen Netzwerkverhaltens-Muster
- **Control Frames**: ACKs, RTSs, CTSs liefern Timing-Informationen

ESP32-Mikrocontroller unterstützen den Promiscuous Mode über die **esp_wifi API**, was kostengünstige Erkennungs-Hardware ermöglicht.

#### 4. Signalstärkenanalyse

Erkennungsgeräte messen **RSSI (Received Signal Strength Indicator)** um:
- **Abstand** zu erkannten Kameras zu schätzen
- **Positionen zu triangulieren** mit mehreren Messungen
- **Falschmeldungen zu filtern** basierend auf erwarteten Signaleigenschaften
- **Wärmekarten** der Kameradichte zu erstellen

### Erkennungsgenauigkeit und Falschmeldungen

Die Flock-You-Methodik erreicht hohe Genauigkeit:

- **True Positive Rate**: ~95% für bestätigte Flock-Kameras in Reichweite
- **False Positive Rate**: ~5-10% je nach Umgebung
- **Erkennungsreichweite**: 15-90 Meter je nach Hindernissen und Antenne

**Häufige Falschmeldungsquellen**:
- **ESP32-Entwicklungsplatinen** in anderen IoT-Geräten
- **Kommerzielle ESP32-basierte Produkte** (Smart Home, Sensoren)
- **Andere Überwachungskameras** mit ähnlichen Komponenten
- **WLAN-Testausrüstung** von Technikern

______

## Hardware-Plattformvergleich

Drei primäre Plattformen sind für die Flock-You-Erkennung verfügbar, jede mit unterschiedlichen Vorteilen:

### Plattformübersichts-Tabelle

| Funktion | DIY ESP32 | M5 Atom Lite (vorgeflasht) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Hersteller** | DIY / Mehrere Anbieter | STS Collective | Colonel Panic Tech |
| **Preis** | $5-12 | $39,99 | $85 |
| **Prozessor** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Sofort einsatzbereit** | Nein (DIY) | Ja (vorgeflasht) | Ja (Multi-Modus) |
| **Anzeige** | Optional | RGB-LED (5×5-Matrix) | Keine |
| **Akku** | Optional | Extern empfohlen | Keiner enthalten |
| **GPS** | Optional | Nein | Nein |
| **Alarme** | Summer + LED | RGB-LED (blau=Erkennung) | Integrierter Summer |
| **Datenprotokollierung** | Optional | Nein | Nein |
| **Gehäuse** | 3D-Druck oder keines | Kompaktes Plastikmodul | Keines (nackte Platine) |
| **Firmware** | Manuell flashen | Vorgeladen FlockYou | Multi-Modus (4 Firmwares) |
| **Am besten für** | DIY-Enthusiasten, Lernen | Budget-fertig | Multi-Zweck-Erkennung |
| **Einrichtungsschwierigkeit** | Mittel-Erweitert | Plug-and-Play | Plug-and-Play |

### Detaillierte Plattformanalyse

#### 1. DIY ESP32 Build ($5-12)

**Überblick**: Günstigste Option mit Standard-ESP32-Entwicklungsplatinen und Open-Source-Firmware.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-WROOM-32 oder ähnlich (Dual-Core, 240MHz)
- **WLAN**: 802.11 b/g/n, Promiscuous-Mode-fähig
- **Speicher**: 520KB SRAM, 4MB+ Flash
- **Anzeige**: Optional (onboard LED ausreichend)
- **Stromversorgung**: USB-betrieben oder Akku-Pack
- **Summer**: Optionales passives Summer-Modul (KY-006)
- **Erweiterbarkeit**: Breadboard-freundlich, einfache Modifikationen

**Firmware**: Open-Source-Fork bei **simeononsecurity/flock-you-esp32**:
- Modifiziert für Standard-ESP32-Hardware (GPIO 25, 2, 17)
- Super Mario Bros. Starttune (bestätigt Summer-Funktion)
- Zwei schnelle aufsteigende Piepstöne bei neuer Erkennung
- 10-Sekunden-Heartbeat-Piepstöne bei aktiver Verfolgung
- Flask-Dashboard-Unterstützung für GPS-Wardriving
- Export nach JSON, CSV, KML-Formaten

**Build-Optionen**:
- **Nur LED ($5)**: Nackte ESP32 + USB-Kabel, visuelle Rückmeldung
- **Breadboard ($9-11)**: Passiver Summer + Breadboard + Jumper, Audio-Alarme
- **Gehäuse ($10-12)**: 3D-gedrucktes Gehäuse mit Schnappsitz-Deckel

**Vorteile**:
- ✅ Günstigste Option (85-95% Kostenersparnis vs. OUI-SPY)
- ✅ Vollständig quelloffen und modifizierbar
- ✅ Verwendet weit verbreitete ESP32-Platinen
- ✅ Lehrreich, vermittelt eingebettete Systeme
- ✅ Umfangreiche Dokumentation und Anleitungen
- ✅ 3D-druckbare Gehäusedateien verfügbar
- ✅ **Gleiche Erkennungsgenauigkeit wie Premiumgeräte**

**Nachteile**:
- ❌ Erfordert DIY-Montage
- ❌ Manuelles Flashen der Firmware erforderlich
- ❌ Kein integrierter Akku (USB-Strom oder externer Pack)
- ❌ Nur grundlegendes Audio-Feedback (keine Anzeige)

**Am besten für**: Maker, Studenten, budgetbewusste Datenschutzadvokaten, alle, die lernen möchten, wie Erkennung funktioniert.

---

#### 2. M5 Atom Lite Vorgeflasht von STS Collective ($39,99)

**Überblick**: Vorgeflashtes kompaktes Erkennungsgerät, sofort einsatzbereit.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-PICO-D4 (Dual-Core, 240MHz)
- **WLAN**: 802.11 b/g/n, Promiscuous-fähig
- **Speicher**: 520KB SRAM, 4MB Flash
- **Anzeige**: 5×5 RGB-LED-Matrix (WS2812C NeoPixel)
- **Stromversorgung**: 5V via USB-C oder Grove-Anschluss
- **Akku**: Keiner enthalten (externer USB-Powerbank empfohlen)
- **Indikator**: Programmierbares RGB-LED (blau=Erkennung)
- **Tasten**: 1 programmierbare Taste
- **Größe**: Ultra-kompakt 24×24×14mm
- **Gehäuse**: Langlebiges Plastikmodul

**Firmware**: Benutzerdefinierter FlockYou-Port von STS Collective (proprietär):
- Vorgeladen und sofort einsatzbereit
- Blaue LED-Warnung bei Flock-Kamera-Erkennung
- Basiert auf colonelpanichacks FlockYou-Forschung
- Keine Einrichtung oder Flash erforderlich
- Einfacher Plug-and-Play-Betrieb

**Vorteile**:
- ✅ Vorgeflasht, keine technische Einrichtung erforderlich
- ✅ Erschwingliche Sofort-Lösung
- ✅ Extrem kompakt und portabel
- ✅ Bewährte Hardware-Plattform
- ✅ Einfaches blau LED = Erkennung
- ✅ USB-C-betrieben (Auto, Powerbank, Laptop)
- ✅ Qualitäts-Anbieter-Support

**Nachteile**:
- ❌ Kein integrierter Akku (benötigt USB-Strom)
- ❌ Begrenzte Anzeige (nur RGB-LED)
- ❌ *Firmware ist proprietär, derzeit nicht Open-Source*
- ❌ Keine Datenprotokollierung ohne Computerverbindung

**Am besten für**: Benutzer, die sofortige Erkennung ohne DIY-Arbeit wünschen, mit Priorität auf Portabilität.

**Kauf**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Exklusiver Rabatt**: Sparen Sie bis zu 20% auf STS Collective-Produkte - verwenden Sie den Code **SIMEONONSECURITY** beim Checkout oder [hier klicken, um mit angewendetem Rabatt zu kaufen](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### 3. OUI-SPY von Colonel Panic Tech ($85)

**Überblick**: Multi-Modus-Überwachungserkennungsplatine mit vier verschiedenen Firmware-Modi, wählbar über WLAN-Menü.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-S3 Dual-Core Xtensa LX7, 8MB Flash
- **WLAN**: 802.11 b/g/n, Promiscuous-Mode-fähig
- **Speicher**: 8MB Flash
- **Anzeige**: Keine (nackte Platine mit LED-Indikatoren)
- **Akku**: Keiner enthalten
- **Laden**: USB-C Strom & Programmierung
- **Indikatoren**: Integrierter PWM-Summer mit modusspezifischen Tunes
- **Tasten**: Boot-Taste zum Moduswechsel
- **Antenne**: **Umschaltbar**, onboard 2,4GHz-Keramik ODER extern via MMCX
- **Einzigartiges Feature**: MAC-Randomisierung bei jedem Start

**Firmware**: OUI-SPY Unified Blue mit **4 wählbaren Modi**:
1. **Detector-Modus**: Multi-Ziel-BLE-Scanner mit OUI-Filterung + Web-Konfigurationsportal
2. **Foxhunter-Modus**: Einzelziel-RSSI-Proximitätstracker für Radio-Peilung
3. **Flock-You-Modus**: Flock Safety & Raven-Kamera-Erkennung mit GPS-Wardriving, JSON/CSV/KML-Export
4. **Sky Spy-Modus**: Drohnen-RemoteID (OpenDroneID / ASTM F3411) Detektor mit Multi-Drohnen-Tracking

**Modi-Auswahl**:
- WLAN-Startmenü unter 192.168.4.1
- BOOT-Taste 2 Sekunden halten zum Zurückkehren zum Selektor
- Moduserinnerung über Neustarts
- Starttunes pro Modus (Retro-Chiptune-Alarme)

**Vorteile**:
- ✅ Vier Firmware-Modi in einem Gerät
- ✅ Umschaltbare Antenne (onboard oder externe MMCX)
- ✅ Integrierter Summer mit benutzerdefinierten Starttunes
- ✅ Professionelles PCB-Design
- ✅ Multi-Zweck: ALPR, Drohnen, BLE, RF-Peilung
- ✅ Unterstützung für externe Antenne für erweiterte Reichweite
- ✅ Vom ursprünglichen Flock-You-Projektersteller
- ✅ Aktive Entwicklung und Updates

**Nachteile**:
- ❌ Höchster Preis für einfache Flock-Erkennung
- ❌ Kein Gehäuse (nackte Platine)
- ❌ Kein eingebauter Akku
- ❌ Keine Anzeige (nur Audio-Feedback für die meisten Modi)

**Am besten für**: Multi-Zweck-Überwachungserkennung, Benutzer die Drohnen + ALPR + BLE-Erkennung in einem Gerät wollen.

**Kauf**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

## Schrittweise Einrichtungsanweisungen

### Einrichtungsanleitung 1: DIY ESP32 Build

**Für vollständige detaillierte Anweisungen** besuchen Sie das GitHub-Repository: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Schnellstart-Überblick

1. **Benötigte Hardware**:
   - ESP32 DevKit-Platine ($5-6)
   - USB-Kabel (Micro-USB oder USB-C je nach Platine)
   - Optional: Passives Summer-Modul (KY-006), Breadboard, Jumper
   - Optional: 3D-gedrucktes Gehäuse

2. **Software-Einrichtung**:
   ```bash
   # PlatformIO installieren
   pip install platformio
   
   # Repository klonen
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32
   
   # Firmware flashen
   pio run -t upload
   pio device monitor
   ```

3. **Hardware-Montage** (bei Verwendung von Summer):
   - Summer positiv → GPIO 25
   - Summer negativ → GND
   - LED-Indikator → GPIO 2 (onboard)
   - Stromversorgung via USB

4. **Startbestätigung**:
   - Super Mario Bros. 1-2 Tune spielt (wenn Summer verbunden)
   - LED blinkt zum Anzeigen des Scannens
   - Serieller Monitor zeigt "Flock-You ESP32" Initialisierung

5. **Erkennungsalarme**:
   - **Neue Erkennung**: Zwei schnelle aufsteigende Piepstöne (2000→2800 Hz)
   - **Heartbeat**: Zwei Piepstöne alle 10 Sekunden während Verfolgung
   - **LED**: Blinkt bei jeder Erkennung

6. **GPS-Wardriving** (optional):
   - Via USB mit Computer verbinden
   - Flask-Dashboard starten: `cd api && python flockyou.py`
   - http://localhost:5000 öffnen
   - GPS-Gerät anschließen oder Browser-Standort nutzen
   - Erkennungen nach JSON/CSV/KML exportieren

---

### Einrichtungsanleitung 2: M5 Atom Lite Vorgeflasht (STS Collective)

#### Schnellstart

1. **Auspacken**:
   - M5 Atom Lite Gerät (vorgeflasht mit FlockYou-Firmware)
   - USB-C-Kabel prüfen (in Produktliste nachsehen)

2. **Einschalten**:
   - An USB-C-Stromquelle anschließen (Powerbank, Auto-USB, Netzteil, Computer)
   - Gerät startet automatisch
   - RGB-LED-Matrix initialisiert

3. **Betrieb**:
   - **Leerlauf/Scannen**: LED zeigt Scan-Muster
   - **Erkennung**: LED wird **BLAU** wenn Flock-Kamera erkannt
   - **Taste**: Drücken zum manuellen Neuscannen

4. **Portabler Einsatz**:
   - An USB-Akku-Pack anschließen (5000mAh = ~20 Stunden)
   - In Cupholder, Tasche oder Rucksack legen
   - LED durch halbtransparentes Gehäuse sichtbar

**Warnung**: *Dies ist proprietäre Firmware. Ein Neuflashen mit Open-Source-Versionen löscht die STS-Firmware dauerhaft.*

---

### Einrichtungsanleitung 3: OUI-SPY Multi-Modus-Platine

#### Ersteinrichtung

1. **Paketinhalt**:
   - OUI-SPY nackte PCB-Platine
   - USB-C-Kabel
   - Kurzanleitung

2. **Erster Start**:
   - USB-C-Strom verbinden (Computer, Netzteil oder Powerbank)
   - Gerät sendet WLAN-Netzwerk: `OUISPY-[ID]`
   - Summer spielt modusspezifischen Starttune

3. **WLAN-Modusauswahl**:
   - Telefon/Computer mit OUI-SPY WLAN verbinden
   - Browser öffnen unter: `http://192.168.4.1`
   - Web-Interface zeigt 4 Firmware-Modi:
     1. **Detector** - Multi-Ziel-BLE-Scanner
     2. **Foxhunter** - RF-Peilung
     3. **Flock-You** - ALPR-Kamera-Erkennung
     4. **Sky Spy** - Drohnen-RemoteID-Detektor
   - Gewünschten Modus auswählen und "Activate" klicken

4. **Flock-You-Modus-Betrieb**:
   - Gerät startet im Flock-You-Modus neu
   - Summer spielt Flock-You-Starttune
   - Beginnt 31 bekannte OUIs zu scannen
   - **Erkennungsalarm**: Summer piept mit einzigartigem Muster

5. **Modi wechseln**:
   - **BOOT-Taste** 2 Sekunden gedrückt halten
   - Gerät kehrt zum WLAN-Moduswähler zurück

#### Erweitert: Externe Antenne

6. **Antennenwechsel** (für erweiterte Reichweite):
   - Standard: Onboard-Keramikantenne
   - MMCX-Antenne an MMCX-Anschluss anstecken
   - Firmware wechselt automatisch zur externen Antenne
   - Direktionale/Yagi-Antenne für Langstrecken-Erkennung verwenden

#### Montage

7. **Fahrzeug-/Festinstallation**:
   - *Kein Gehäuse enthalten, nackte Platine braucht Schutz vor Montage*
   - Optionen:
     - 3D-gedrucktes Gehäuse drucken
     - Klett-Montage am Armaturenbrett
     - Doppelseitiges Klebeband
     - DIY-Projektbox
   - USB-C-Port für Stromversorgung zugänglich halten

#### Datenexport (Flock-You-Modus)

8. **GPS-Wardriving**:
   - Externes GPS-Modul anschließen (nicht enthalten)
   - Gerät protokolliert Erkennungen mit Koordinaten
   - Datendateien über Web-Interface herunterladen
   - Exportformate: JSON, CSV, KML

______

## Kaufleitfaden und Anbieterinformationen

### Autorisierte Anbieter

#### Colonel Panic Tech (colonelpanic.tech)

**Angebotene Produkte**:
- **OUI-SPY** ($85): Einsatzfertiges Flock-Erkennungsgerät
- **DIY-Kits** ($55): Komponenten + PCB + Montageanleitung
- **GPS-Modul-Addon** ($18): Kompatibles GPS-6M-Modul
- **Zubehör**: Antennen, Gehäuse, Akku-Upgrades

**Warum bei Colonel Panic kaufen**:
- ✅ Direkt vom Entwickler der OUI-SPY-Hardware
- ✅ Neueste Firmware vorinstalliert
- ✅ Technischer Support enthalten
- ✅ Open-Source-Ethos (Schaltpläne verfügbar)
- ✅ Aktives Community-Forum

**Versand**:
- USA Inland: 3-5 Werktage
- International: 7-14 Werktage
- Kostenloser Versand bei Bestellungen über $100

**Garantie**: 90 Tage Hardware-Garantie, lebenslange Firmware-Updates

**Website**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Angebotene Produkte**:
- **M5 Atom Lite Vorgeflasht** ($39,99): Sofort einsatzbereites Flock-Erkennungsgerät
- **Zubehör**: Kompatibel mit verschiedenen ESP32-Plattformen

**Warum bei STS Collective kaufen**:
- ✅ Vorgeflashte, sofort einsatzbereite Geräte
- ✅ Qualitätssicherung und Tests
- ✅ Erschwingliche Preise
- ✅ Kundensupport

**Website**: [https://stscollective.com](https://stscollective.com)

> 💰 **Leserrabatt**: Code **SIMEONONSECURITY** für bis zu 20% Rabatt auf STS Collective-Produkte verwenden - [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Ihr Erkennungsgerät verwenden: Praktische Szenarien

### Szenario 1: Tägliche Pendelkartierung

**Ziel**: Flock-Kamera-Standorte auf Ihren regulären Routen dokumentieren.

**Einrichtung**:
- Gerät mit GPS-Fähigkeit verwenden (DIY ESP32 mit GPS-Modul oder OUI-SPY mit GPS)
- Automatische Protokollierung aktivieren
- Im Fahrzeug montieren oder in der Tasche tragen

**Verfahren**:
1. Erkennungsgerät vor Abfahrt starten
2. Normale Route fahren
3. Gerät alarmiert bei erkannten Flock-Kameras
4. GPS-Koordinaten automatisch protokolliert
5. Nach Hause zurückkehren und Daten exportieren
6. GPX/CSV in Kartierungs-Software importieren
7. Persönliche Kamera-Standortkarte erstellen

### Szenario 2: Nachbarschafts-Überwachungsbewertung

**Ziel**: Flock-Kamera-Abdeckung in Ihrem Wohngebiet bestimmen.

**Verfahren**:
1. Durch Nachbarschaftsstraßen gehen/fahren
2. An jeder Kreuzung 30-60 Sekunden anhalten
3. Erkennungen auf der Karte notieren
4. Signalstärke verwenden, um Entfernung/Richtung zu schätzen
5. Kamera-Standorte nach Möglichkeit visuell bestätigen
6. Befunde mit Fotos dokumentieren (von öffentlichen Bereichen)

### Szenario 3: Reise-Datenschutzbewertung

**Ziel**: Überwachungsexposition beim Reisen verstehen.

**Verwendungsfälle**:
- Arzttermine: Überwachung nahe Kliniken bewerten
- Rechtsberatungen: Kanzleibereich prüfen
- Religiöse Dienste: Monitoring nahe Gotteshäusern verstehen
- Politische Aktivitäten: Überwachung bei Veranstaltungen/Protesten bewerten

### Szenario 4: Community-Advocacy

**Ziel**: Daten für politische Debatten und öffentliches Bewusstsein bereitstellen.

**Anwendungen**:
- Befunde bei Stadtratssitzungen präsentieren
- In Informationsfreiheitsanträge einbeziehen
- Mit Datenschutzorganisationen teilen
- Zu Forschungsprojekten beitragen

______

## Rechtliche und ethische Überlegungen

### Rechtlicher Status von Erkennungsgeräten

**WLAN-Scanning-Legalität**:
- ✅ **Legal in den USA**: Passives WLAN-Monitoring (nur-Empfang) ist legal
- ✅ **Kein Abfangen**: Geräte überwachen nur öffentlich gesendete Frames
- ✅ **Keine Entschlüsselung**: Kein Versuch, Daten zu entschlüsseln oder Netzwerke zu verbinden
- ✅ **Ähnlich wie Radio-Scanner**: Vergleichbarer rechtlicher Status wie Polizei-Scanner

**Wichtige Unterscheidungen**:
- ❌ **Illegal**: Aktives Stören/Eingreifen in den Kamerabetrieb
- ❌ **Illegal**: Versuch, Kamerasysteme zu hacken oder darauf zuzugreifen
- ❌ **Illegal**: Physische Kameras zerstören oder manipulieren
- ⚠️ **Graubereich**: *Einige Jurisdiktionen haben strengere Datenschutzgesetze. Lokale Vorschriften vor Gebrauch prüfen.*

**Empfehlung**: **Erkennungsgeräte dienen nur zur Sensibilisierung. Betrieb der Kamera nicht stören.**

______

## Fazit: Datenschutz durch Technologie

Das **Flock-You-Erkennungsprojekt** repräsentiert eine mächtige Demokratisierung der Gegensurveillance-Technologie. Für weniger als die Kosten eines monatlichen Streaming-Abonnements erhalten Einzelpersonen Bewusstsein über die sie umgebende Überwachungsinfrastruktur. Ob Sie sich für den **DIY ESP32 Build ($5-12)**, das **sofort einsatzbereite M5 Atom Lite ($40)** oder den **Multi-Modus-OUI-SPY ($85)** entscheiden - Sie investieren in Datenschutzbewusstsein und digitale Autonomie.

### Wichtigste Punkte

✅ **Open-Source-Ermächtigung**: Community-getriebene Entwicklung gewährleistet Zugänglichkeit
✅ **Erschwingliche Technologie**: Verbraucher-Hardware (ESP32) macht Erkennung zugänglich
✅ **Mehrere Plattformen**: Optionen für verschiedene Budgets und technische Kenntnisse
✅ **Aktive Entwicklung**: Regelmäßige Updates mit neuen OUI-Signaturen und Funktionen
✅ **Legal und ethisch**: Passives Monitoring entspricht dem Kommunikationsrecht
✅ **Community-Nutzen**: Trägt zu öffentlichem Bewusstsein und Politikdiskussion bei

______

## Referenzen

1. [Flock-You GitHub Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - Interaktive ALPR-Kamera-Karte](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - GitHub Repository](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - Offizieller Anbieter](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite Vorgeflasht](https://stscollective.com)
6. [M5Stack Offizielle Dokumentation](https://docs.m5stack.com/en/core/atom_lite)
7. [Espressif ESP32 Technische Dokumentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
8. [WLAN Promiscuous Mode Tutorial](https://esp32developer.com/wifi-promiscuous-mode)
9. [DeFlockJoplin Community-Forschung](https://deflockjoplin.org/)
10. [Electronic Frontier Foundation - ALPR](https://www.eff.org/issues/automated-license-plate-readers)
11. [Arduino IDE Offizieller Download](https://www.arduino.cc/en/software)
12. [Platform.io Dokumentation](https://docs.platformio.org/)
13. [OUI-Datenbank - IEEE Standards](https://standards.ieee.org/products-programs/regauth/)
