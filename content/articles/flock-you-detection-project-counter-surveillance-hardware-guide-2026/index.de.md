---
title: "Flock-You-Erkennung: Leitfaden zur Einrichtung von Hardware zur Überwachungsabwehr"
date: 2026-05-24
lastmod: 2026-11-19
toc: true
draft: false
description: "Umfassender technischer Leitfaden zum Open-Source-Projekt Flock-You zur Erkennung von Flock Safety ALPR-Kameras mit ESP32-basierter Hardware. Enthält Einrichtungsanweisungen, Firmware-Details und Einkaufsinformationen."
genre: ["Sicherheits-Hardware", "Gegenüberwachung", "Datenschutztechnologie", "Open-Source-Projekte", "ESP32-Entwicklung", "WLAN-Überwachung", "Datenschutzwerkzeuge", "Digitale Rechte", "Hardware-Hacking", "Netzwerksicherheit"]
tags: ["Flock-You-Projekt", "ALPR-Erkennung", "ESP32-S3", "WLAN-OUI-Erkennung", "Hardware zur Gegenüberwachung", "Flock-Safety-Erkennung", "Open-Source-Sicherheit", "Datenschutz-Hardware", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "WLAN im Promiscuous-Modus", "802.11-Überwachung", "Colonel Panic Tech", "STS Collective", "Datenschutzgeräte", "Überwachungserkennung", "WLAN-Scanning", "GitHub-Projekt", "colonelpanichacks", "ESP32-Firmware", "Hardware-Einrichtungsanleitung", "DIY-Datenschutzwerkzeuge", "Netzwerküberwachung", "OUI-Datenbank", "Erkennung von Wildcard-Probes", "Frame-Analyse", "ALPR-Kameraerkennung", "Datenschutztechnologie", "Erkennungshardware", "Arduino ESP32", "Platform.io", "Eingebettete Systeme", "HF-Erkennung", "Signalverarbeitung", "Datenschutztechnik", "Gegenüberwachungstechnologie", "Sicherheitsforschung", "Datenschutzvertretung", "Offene Hardware", "Datenschutzschutz", "Erkennungsfirmware", "Mobile Erkennung", "Datenschutzprojekte", "Hardwarevergleich"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Eine Illustration, die ein ESP32-basiertes Gerät im Vordergrund zeigt, das WLAN-Signale scannt. Bunte Wellen repräsentieren verschiedene Signalstärken vor einem dunklen Hintergrund."
coverCaption: "Open-Source-Hardware-Lösungen zur Erkennung von ALPR-Überwachungskameras"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Vollständiger technischer Leitfaden zum Aufbau und Einsatz von Flock-You-Erkennungsgeräten**

## Einführung: Open-Source-Gegensurveillance

Das **Flock-You-Projekt** ist eine **quelloffene, community-getriebene Initiative** zur Erkennung und Kartierung der ALPR-Überwachungsinfrastruktur von Flock Safety. Auf GitHub gehostet unter **colonelpanichacks/flock-you**, nutzt dieses Projekt erschwingliche ESP32-basierte Hardware, um Flock-Kameras durch ihre **WLAN-Netzwerksignaturen** zu identifizieren.

**Flock-You erkennt ausschließlich Flock-Safety-Kameras über WLAN.** Es erkennt weder Mobilfunkzellen-Simulatoren im Stingray-Stil noch persönliche Tracker, die sich mit dir bewegen. Dafür gibt es **[Rayhunter-Geräte flashen: vollständige Anleitung](/articles/how-to-flash-rayhunter-devices-complete-guide/)** zur Erkennung von IMSI-Catchern und **[Eye Spy: Passiver ESP32-Detektor für Überwachung und Tracker](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** zur Erkennung von AirTags und anderen Trackern. Alle drei laufen auf derselben günstigen ESP32-Hardwarefamilie.

Dieser umfassende Leitfaden behandelt alles von der **technischen Methodik** hinter der Flock-Erkennung bis hin zu **schrittweisen Einrichtungsanweisungen** für drei Hardware-Plattformen, **Firmware-Installation** und **Kaufinformationen von autorisierten Anbietern**. Ob Sie ein Datenschutzadvokat, Sicherheitsforscher oder besorgter Bürger sind - dieser Leitfaden ermöglicht Ihnen den Aufbau oder Kauf Ihres eigenen Erkennungsgeräts.


*Flock-Safety-Hardware ist fast ausschließlich in den Vereinigten Staaten im Einsatz, mit einer kleineren Verbreitung in Kanada. Außerhalb Nordamerikas passen die folgende OUI-Liste und die Probe-Signaturen zu keinem Gerät in der Nähe. Die Hardware bleibt für Forschungszwecke nützlich, findet aber keine Infrastruktur, die dort nicht vorhanden ist.*

Für den Kontext, warum diese Technologie wichtig ist, lesen Sie unseren Begleitartikel: **[Flock Safety Kamera-Überwachung: Verbreitung, Datenschutzbedenken und Schutzstrategien](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Möchten Sie sehen, wo Flock-Kameras bereits kartiert wurden? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** ist ein Open-Source-Tool, das 40.000+ vermutete Flock Safety-Kameras weltweit mithilfe von WiGLE-WLAN-Daten und OUI-Fingerprinting darstellt - täglich aktualisiert. Quellcode auf **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

### Auf einen Blick: drei Plattformen

*Vollständige technische Daten sowie Vor- und Nachteile der Plattformen findest du weiter unten. Springe zur [Einrichtungsanleitung](#schrittweise-einrichtungsanweisungen), wenn du dich bereits entschieden hast.*


| Plattform | Preis | Einrichtung | Geeignet für |
|---|---|---|---|
| **DIY ESP32** | 5–12 $ | Steckbrett ohne Löten, 10–15 Min. | Günstige Eigenbauten und zum Lernen der Erkennung |
| **M5 Atom Lite** (vorinstalliert) | 49,99 $ | Einstecken und loslegen, keine Einrichtung | Sofortiger Einsatz ohne Bastelaufwand |
| **OUI-SPY** | 85 $ | Einmal flashen, Modus im WLAN-Menü auswählen | Erkennung mehrerer Ziele (ALPR, Drohnen, BLE) |

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

#### 3. WLAN-Überwachung im Mithörmodus

Der Standard-WLAN-Betrieb empfängt nur an Ihr Gerät adressierte Frames. Der **Mithörmodus** erfasst alle WLAN-Frames in Reichweite:

- **802.11 Frame-Struktur**: Analyse der addr1, addr2, addr3-Felder
- **Verwaltungsframes**: Sondierungsanfragen, Beacon-Frames, Assoziierungsanfragen
- **Data Frames**: Zeigen Netzwerkverhaltens-Muster
- **Control Frames**: ACKs, RTSs, CTSs liefern Timing-Informationen

ESP32-Mikrocontroller unterstützen den Mithörmodus über die **esp_wifi API**, was kostengünstige Erkennungs-Hardware ermöglicht.

#### 4. Signalstärkenanalyse

Erkennungsgeräte messen **RSSI (Indikator für die empfangene Signalstärke)** um:
- **Abstand** zu erkannten Kameras zu schätzen
- **Positionen zu triangulieren** mit mehreren Messungen
- **Falschmeldungen zu filtern** basierend auf erwarteten Signaleigenschaften
- **Wärmekarten** der Kameradichte zu erstellen

### Erkennungsgenauigkeit und Falschmeldungen

Die Genauigkeit hängt stark von der Umgebung ab. Ein dokumentierter Feldtest liefert einen konkreten Ausgangswert: Die Community **DeFlockJoplin** erkannte bei einer Testfahrt **11 von 12 bekannten Flock-Kameras und nur 2 Falschmeldungen** entlang der Strecke.

- **Im Feld geprüfter Ausgangswert**: 11 von 12 bestätigten Kameras erkannt, 2 Falschmeldungen (Testfahrt von DeFlockJoplin)
- **Erkennungsreichweite**: 50–300 Fuß, abhängig von Hindernissen und Antenne
- **Konfidenzbewertung**: Eine Mehrfaktoranalyse aus OUI-Abgleich, Wildcard-Probe-Signatur und RSSI-Schwelle verringert Fehlalarme
- **Deine Ergebnisse können abweichen**: Funkumgebung, Antenne und Firmware-Version beeinflussen die Genauigkeit im Einsatz

**Häufige Ursachen für Falschmeldungen**:
- **ESP32-Entwicklungsplatinen** in anderen IoT-Geräten
- **Kommerzielle ESP32-Produkte** wie Smart-Home-Geräte und Sensoren
- **Andere Überwachungskameras** mit ähnlichen Komponenten
- **WLAN-Testgeräte**, die Techniker einsetzen

**Maßnahmen gegen Falschmeldungen**:
- **Mehrere Signale kombinieren**: OUI, Probe-Muster und physische Überprüfung zusammen auswerten
- **Standorte abgleichen**: Ergebnisse mit bekannten Kamerastandorten vergleichen
- **Visuell bestätigen**: Nach einer elektronischen Erkennung den Standort aus sicherer und öffentlicher Position prüfen
- **Community-Datenbank nutzen**: Erkennungen gemeinschaftlich überprüfen

{{< figure src="flockyou-oui-detection-methodology-overview.webp" alt="Flock-You-Erkennungsdiagramm: ESP32 im WLAN-Promiscuous-Modus vergleicht MACs mit bekannten Flock-OUIs, prüft Wildcard-Probes und bewertet RSSI" >}}

{{< stscollective-ad "flockyou" >}}

## Hardware-Plattformvergleich

Drei primäre Plattformen sind für die Flock-You-Erkennung verfügbar, jede mit unterschiedlichen Vorteilen:
*Alle drei Plattformen verwenden dieselbe grundlegende Erkennungsmethode: passives Scannen im WiFi-Promiscuous-Modus nach bekannten OUIs von Flock-Kameras und Wildcard-Probe-Signaturen. Keine der Plattformen erkennt Bluetooth. Die Flock-You-Firmware stellte die BLE-Erkennung im Frühjahr 2026 ein, nachdem sie nicht mehr zuverlässig funktionierte. Deshalb nutzen alle hier aufgeführten Plattformen ausschließlich WiFi.*

### Plattformübersichts-Tabelle

| Funktion | DIY ESP32 | M5 Atom Lite (vorgeflasht) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Hersteller** | DIY / Mehrere Anbieter | STS Collective | Colonel Panic Tech |
| **Preis** | $5-12 | $49.99 | $85 |
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
| **Einrichtungsschwierigkeit** | Mittel-Erweitert | Keine Einrichtung erforderlich | Keine Einrichtung erforderlich |
| **Gewicht** | 20–50 g (je nach Modell) | 18 g (ohne Zubehör) | ca. 40 g |
| **Abmessungen** | Variieren | 24 × 24 × 14 mm | Platine |

### Detaillierte Plattformanalyse

#### 1. DIY-Aufbau mit ESP32 ($5-12)

**Überblick**: Günstigste Option mit Standard-ESP32-Entwicklungsplatinen und Open-Source-Firmware.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-WROOM-32 oder ähnlich (mit zwei Kernen, 240 MHz)
- **WLAN**: 802.11 b/g/n, Promiscuous-Mode-fähig
- **Speicher**: 520KB SRAM, 4MB+ Flash
- **Anzeige**: Optional (onboard LED ausreichend)
- **Stromversorgung**: USB-betrieben oder Akku-Pack
- **Summer**: Optionales passives Summer-Modul (KY-006)
- **Erweiterbarkeit**: Breadboard-freundlich, einfache Modifikationen
- **Anzeigen**: Integrierte LED und optionaler Summer

**Firmware**: Open-Source-Fork **simeononsecurity/flock-you-esp32**:
- Modifiziert für Standard-ESP32-Hardware (GPIO 25, 2, 17)
- Super Mario Bros. Starttune (bestätigt Summer-Funktion)
- Zwei schnelle aufsteigende Piepstöne bei neuer Erkennung
- 10-Sekunden-Heartbeat-Piepstöne bei aktiver Verfolgung
- Flask-Dashboard-Unterstützung für GPS-gestützte WLAN-Erkundungsfahrten
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

**Komponenten kaufen**:
- **Amazon**: Suche nach „ESP32 DevKit“ oder „ESP32 Breadboard Kit“
- **AliExpress/eBay**: Mengenrabatte sind verfügbar
- **Adafruit**: ausgewählte Bauteile mit Anleitungen

**Einrichtungsressourcen**:
- **GitHub-Repository**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Bauanleitung**: lötfreier Aufbau in 10–15 Minuten
- **Gehäusedateien**: parametrisches OpenSCAD-Design und STL-Dateien

- ❌ Die Beschaffung der Komponenten braucht Zeit

**Am besten für**: Maker, Studenten, budgetbewusste Datenschutzadvokaten, alle, die lernen möchten, wie Erkennung funktioniert.

---

{{< figure src="flockyou-diy-esp32-solderless-breadboard-build.webp" alt="Lötfreier ESP32-Flock-You-Aufbau mit DevKit, passivem Summer und Kabeln an GPIO 25, 2 und 17" >}}

#### 2. M5 Atom Lite Vorgeflasht von STS Collective ($49.99)

**Überblick**: Vorgeflashtes kompaktes Erkennungsgerät, sofort einsatzbereit.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-PICO-D4 (mit zwei Kernen, 240 MHz)
- **WLAN**: 802.11 b/g/n, Promiscuous-fähig
- **Speicher**: 520KB SRAM, 4MB Flash
- **Anzeige**: 5×5 RGB-LED-Matrix (WS2812C NeoPixel)
- **Stromversorgung**: 5V via USB-C oder Grove-Anschluss
- **Akku**: Keiner enthalten (externer USB-Powerbank empfohlen)
- **Indikator**: Programmierbares RGB-LED (blau=Erkennung)
- **Tasten**: 1 programmierbare Taste
- **E/A**: Grove-Anschluss zur Erweiterung
- **Größe**: Ultra-kompakt 24×24×14mm
- **Gehäuse**: Langlebiges Plastikmodul

**Firmware**: Benutzerdefinierter FlockYou-Port von STS Collective (proprietär):
- Vorgeladen und sofort einsatzbereit
- Blaue LED-Warnung bei Flock-Kamera-Erkennung
- Basiert auf colonelpanichacks FlockYou-Forschung
- Keine Einrichtung oder Flash erforderlich
- Einfache Bedienung ohne aufwendige Konfiguration
- Optionale Dashboard-Unterstützung

**Vorteile**:
- ✅ Vorgeflasht, keine technische Einrichtung erforderlich
- ✅ Erschwingliche Sofort-Lösung
- ✅ Extrem kompakt und portabel
- ✅ Bewährte Hardware-Plattform
- ✅ Einfaches blau LED = Erkennung
- ✅ USB-C-betrieben (Auto, Powerbank, Laptop)
- ✅ Qualitäts-Anbieter-Support
- ✅ Regulär $99.99, aktuell für $49.99 im Angebot

**Nachteile**:
- ❌ Kein integrierter Akku (benötigt USB-Strom)
- ❌ Begrenzte Anzeige (nur RGB-LED)
- ❌ *Firmware ist proprietär, derzeit nicht Open-Source*
- ❌ Keine Datenprotokollierung ohne Computerverbindung
- ❌ Eine einzelne Taste schränkt die Bedienung ein

**Am besten für**: Benutzer, die sofortige Erkennung ohne DIY-Arbeit wünschen, mit Priorität auf Portabilität.

**Kauf**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Exklusiver Rabatt**: Sparen Sie bis zu 20% auf STS Collective-Produkte - verwenden Sie den Code **SIMEONONSECURITY** beim Checkout oder [hier klicken, um mit angewendetem Rabatt zu kaufen](https://stscollective.com/discount/SIMEONONSECURITY).

---

{{< figure src="flockyou-m5-atom-lite-pocket-size-comparison.webp" alt="Vorgeflashtes M5 Atom Lite zwischen zwei Fingern, mit blauer RGB-LED als Erkennungssignal" >}}

#### 3. OUI-SPY von Colonel Panic Tech ($85)

**Überblick**: Multi-Modus-Überwachungsplatine mit vier Firmware-Modi, die über ein WLAN-Menü ausgewählt werden.

**Hardware-Spezifikationen**:
- **Mikrocontroller**: ESP32-S3 mit zwei Xtensa-LX7-Kernen, 8 MB Flash
- **WLAN**: 802.11 b/g/n, unterstützt den Promiscuous-Modus
- **Speicher**: 8 MB Flash
- **Anzeige**: keine, offene Platine mit LED-Anzeigen
- **Akku**: nicht enthalten
- **Laden**: USB-C für Stromversorgung und Programmierung
- **Speicher**: keiner (Modi dienen nur der Erkennung)
- **Anzeigen**: integrierter PWM-Summer mit modusspezifischen Tönen
- **Tasten**: BOOT-Taste zum Wechseln des Modus
- **Antenne**: integrierte 2,4-GHz-Aufklebeantenne, ab Werk; für mehr Reichweite austauschbar
- **Gehäuse**: keines, offene Platine mit Leiterplattenmotiv
- **Besonderheit**: MAC-Adresse wird bei jedem Start randomisiert

**Firmware**: OUI-SPY Unified Blue mit **4 wählbaren Modi**:
1. **Detector-Modus**: Multi-Ziel-BLE-Scanner mit OUI-Filterung + Web-Konfigurationsportal
2. **Foxhunter-Modus**: Einzelziel-RSSI-Proximitätstracker für Radio-Peilung
3. **Flock-You-Modus**: Flock Safety & Raven-Kamera-Erkennung mit GPS-gestützte WLAN-Erkundungsfahrten, JSON/CSV/KML-Export
4. **Sky Spy-Modus**: Drohnen-RemoteID (OpenDroneID / ASTM F3411) Detektor mit Multi-Drohnen-Tracking

**Modi-Auswahl**:
- WLAN-Startmenü unter `192.168.4.1`
- BOOT-Taste zwei Sekunden halten, um zum Auswahlmenü zurückzukehren
- Der zuletzt verwendete Modus bleibt nach dem Ausschalten gespeichert
- Jeder Modus hat eigene Starttöne und Retro-Chiptune-Alarme
- Reiner Erkennungsbetrieb, das Gerät sendet nichts
**Vorteile**:
- ✅ Vier Firmware-Modi in einem Gerät
- ✅ Umschaltbare Antenne (onboard oder externe MMCX)
- ✅ Integrierter Summer mit benutzerdefinierten Starttunes
- ✅ Professionelles PCB-Design
- ✅ Multi-Zweck: ALPR, Drohnen, BLE, RF-Peilung
- ✅ Vom ursprünglichen Flock-You-Projektersteller
- ✅ Aktive Entwicklung und Updates

**Nachteile**:
- ❌ Höchster Preis für einfache Flock-Erkennung
- ❌ Kein Gehäuse (nackte Platine)
- ❌ Kein eingebauter Akku
- ❌ Keine Anzeige (bei den meisten Modi nur Audio-Feedback)
- ❌ Für einfache Erkennung unnötig komplex
- ❌ Für GPS-gestützte WLAN-Erkundungsfahrten ist ein externes GPS-Modul erforderlich

**Am besten für**: Multi-Zweck-Überwachungserkennung, Benutzer die Drohnen + ALPR + BLE-Erkennung in einem Gerät wollen.

**Kauf**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

{{< figure src="flockyou-oui-spy-multimode-board-pcb.webp" alt="Unbestückte OUI-SPY-ESP32-S3-Platine mit Antenne, Summer und Boot-Taste; ein Bildschirm zeigt das WLAN-Menü mit vier Modi" >}}

## Schrittweise Einrichtungsanweisungen

### Einrichtungsanleitung 1: DIY-Aufbau mit ESP32

**Eine ausführliche Anleitung** findest du im [GitHub-Repository](https://github.com/simeononsecurity/flock-you-esp32).

#### Schnellstart

1. **Benötigte Hardware**:
   - ESP32-DevKit-Platine ($5–6)
   - USB-Kabel (Micro-USB oder USB-C, je nach Platine)
   - Optional: passives Summer-Modul (KY-006), Breadboard und Jumper-Kabel
   - Optional: 3D-gedrucktes Gehäuse

2. **Software einrichten**:
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

3. **Hardware zusammenbauen** (bei Verwendung eines Summers):
   - Summer-Pluspol → GPIO 25
   - Summer-Minuspol → GND
   - LED-Anzeige → GPIO 2 (integriert)
   - Stromversorgung über USB

4. **Start bestätigen**:
   - Die Melodie aus Super Mario Bros. 1-2 ertönt, wenn ein Summer angeschlossen ist
   - Die LED blinkt während des Scannens
   - Der serielle Monitor zeigt die Initialisierung von „Flock-You ESP32“

5. **Erkennungsalarme**:
   - **Neue Erkennung**: zwei schnell ansteigende Töne (2000 → 2800 Hz)
   - **Heartbeat**: während der Ortung alle 10 Sekunden zwei Töne
   - **LED**: blinkt bei jeder Erkennung

6. **GPS-gestützte WLAN-Erkundungsfahrten** (optional):
   - Verbinde das Gerät per USB mit einem Computer
   - Starte das Flask-Dashboard mit `cd api && python flockyou.py`
   - Öffne `http://localhost:5000`
   - Verbinde ein GPS-Gerät oder verwende den Standort des Browsers
   - Exportiere Erkennungen in JSON-, CSV- oder KML-Formate

**Ausführliche Bauanleitung, Gehäusedateien und Fehlerbehebung**: Lies die README-Datei auf GitHub.

---

### Einrichtungsanleitung 2: Vorgeflashtes M5 Atom Lite (STS Collective)

#### Schnellstart

1. **Lieferumfang prüfen**:
   - M5 Atom Lite mit vorinstallierter FlockYou-Firmware
   - Prüfe im Produktangebot, ob ein USB-C-Kabel enthalten ist

2. **Einschalten**:
   - Verbinde das Gerät mit einer USB-C-Stromquelle, etwa einer Powerbank, einem Auto-USB-Anschluss, Netzteil oder Computer
   - Das Gerät startet automatisch
   - Die RGB-LED-Matrix wird initialisiert

3. **Bedienung**:
   - **Ruhezustand/Scan**: Die LED zeigt ein Scanmuster
   - **Erkennung**: Die LED leuchtet **BLAU**, wenn eine Flock-Kamera erkannt wird
   - **Taste**: Drücke sie, um erneut zu scannen oder das Gerät zurückzusetzen

4. **Mobiler Einsatz**:
   - Verbinde eine USB-Powerbank (5000 mAh reichen für etwa 20 Stunden)
   - Lege das Gerät in den Becherhalter, eine Tasche oder eine Jackentasche
   - Die LED bleibt durch das durchscheinende Gehäuse sichtbar

5. **Dashboard verbinden** (optional):
   - Verbinde das Gerät per USB-C mit einem Computer
   - Installiere das FlockYou-Dashboard nach den Anweisungen von STS Collective
   - Sieh dir Live-Erkennungen in der Browseroberfläche an

**Warnung**: *Diese Firmware ist proprietär. Beim erneuten Flashen einer Open-Source-Version wird die STS-Firmware dauerhaft gelöscht.*

---

### Einrichtungsanleitung 3: OUI-SPY-Multimodus-Platine

#### Ersteinrichtung

1. **Lieferumfang**:
   - OUI-SPY-Platine ohne Gehäuse
   - USB-C-Kabel
   - Kurzanleitung

2. **Erstes Einschalten**:
   - Verbinde die USB-C-Stromversorgung mit einem Computer, Netzteil oder einer Powerbank
   - Das Gerät sendet das WLAN-Netz `OUISPY-[ID]`
   - Der Summer spielt einen modusspezifischen Startton

3. **WLAN-Modus auswählen**:
   - Verbinde dein Smartphone oder deinen Computer mit dem OUI-SPY-WLAN
   - Öffne im Browser `http://192.168.4.1`
   - Die Weboberfläche zeigt vier Firmware-Modi:
     1. **Detector**: BLE-Scanner für mehrere Ziele
     2. **Foxhunter**: Funkpeilung
     3. **Flock-You**: Erkennung von ALPR-Kameras
     4. **Sky Spy**: Erkennung von Drohnen über Remote ID
   - Wähle den gewünschten Modus und klicke auf „Activate“

4. **Flock-You-Modus verwenden**:
   - Das Gerät startet im Flock-You-Modus neu
   - Der Summer spielt den Flock-You-Startton
   - Das Gerät sucht nach 31 bekannten OUI-Präfixen
   - **Erkennungsalarm**: Der Summer gibt ein eindeutiges Muster aus
   - Der zuletzt verwendete Modus bleibt nach einem Neustart gespeichert

5. **Modus wechseln**:
   - Halte die **BOOT-Taste** zwei Sekunden lang gedrückt
   - Das Gerät wechselt zurück zur WLAN-Modusauswahl
   - Verbinde dich erneut mit dem WLAN und wähle einen anderen Modus

#### Erweiterte Nutzung: Antenne wechseln

6. **Antenne wechseln** (für größere Reichweite):
   - Standardmäßig wird die aufgeklebte interne Antenne verwendet
   - Für eine größere Reichweite lassen sich Antennen mit höherem Gewinn anlöten
   - Das ist eine Hardwareänderung und keine Softwareoption. Prüfe vor dem Kauf einer Ersatzantenne die aktuelle Anschlussangabe auf colonelpanic.tech

#### Montage

7. **Einbau im Fahrzeug oder an einem festen Standort**:
   - *Ein Gehäuse ist nicht enthalten. Schütze die offene Platine vor der Montage.*
   - Mögliche Lösungen:
     - Ein individuelles Gehäuse im 3D-Druck herstellen
     - Mit Klettband am Armaturenbrett befestigen
     - Doppelseitiges Klebeband verwenden
     - Ein Projektgehäuse verwenden
   - Der USB-C-Anschluss für die Stromversorgung muss zugänglich bleiben

#### Daten exportieren (Flock-You-Modus)

8. **GPS-gestützte WLAN-Erkundungsfahrten**:
   - Verbinde ein externes GPS-Modul, das nicht enthalten ist
   - Das Gerät protokolliert Erkennungen mit Koordinaten
   - Lade Datendateien über die Weboberfläche herunter
   - Exportiere sie als JSON, CSV oder KML

**Hinweis**: Firmware-Updates und OUI-SPY-Unified-Blue-Dokumentation findest du auf colonelpanic.tech.

______

## Kaufleitfaden und Anbieterinformationen

### Autorisierte Anbieter

#### Colonel Panic Tech (colonelpanic.tech)

**Angebotene Produkte**:
- **OUI-SPY** ($85): sofort einsatzbereites Gerät zur Flock-Erkennung
- **DIY-Kits** ($55): Komponenten, Platine und Montageanleitung
- **GPS-Modul als Zusatz** ($18): kompatibles GPS-6M-Modul
- **Zubehör**: Antennen, Gehäuse und Akku-Upgrades

**Warum bei Colonel Panic kaufen**:
- ✅ Direkt vom Entwickler der OUI-SPY-Hardware
- ✅ Neueste Firmware vorinstalliert
- ✅ Technischer Support enthalten
- ✅ Open-Source-Ansatz mit verfügbaren Schaltplänen
- ✅ Aktives Community-Forum

**Versand**:
- Inland der USA: 3–5 Werktage
- International: 7–14 Werktage
- Kostenloser Versand bei Bestellungen über $100

**Garantie**: 90 Tage auf die Hardware, lebenslange Firmware-Updates

**Website**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Angebotene Produkte**:
- **Vorgeflashtes M5 Atom Lite** ($49.99): sofort einsatzbereites Gerät zur Flock-Erkennung
- **Zubehör**: mit verschiedenen ESP32-Plattformen kompatibel

**Warum bei STS Collective kaufen**:
- ✅ Vorgeflashte, sofort einsatzbereite Geräte
- ✅ Qualitätssicherung und Tests
- ✅ Erschwingliche Preise
- ✅ Kundensupport

**Versand**:
- Inland der USA: 2–4 Werktage mit Priority Mail
- International: 7–21 Werktage
- Expressversand verfügbar

**Garantie**: Standardgarantie auf die Hardware

**Website**: [https://stscollective.com](https://stscollective.com)

> 💰 **Leserrabatt**: Verwende den Code **SIMEONONSECURITY** für bis zu 20 % Rabatt auf Produkte von STS Collective. [Hier mit angewendetem Rabatt einkaufen](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Weitere Bezugsquellen für den M5 Atom Lite

**Offizieller M5Stack-Shop**:
- Website: [shop.m5stack.com](https://shop.m5stack.com)
- Preis: $9.95 für ein unbefülltes Atom Lite
- Zubehör: Akkumodule, Grove-Sensoren und Gehäuse
- Versand: international, 7–14 Tage

**Amazon**: Suche nach „M5Stack Atom Lite“
- Preis: etwa $12–15, je nach Anbieter
- Prime-Versand verfügbar
- Bundles mit Zubehör erhältlich

**Adafruit**: [adafruit.com](https://adafruit.com)
- Elektronikhändler mit ausgewähltem Sortiment
- Gute Lernmaterialien
- Schneller Versand innerhalb der USA

**Hinweis**: *Bei einem unbefüllten M5 Atom Lite muss die Firmware gemäß der DIY-Anleitung oben separat installiert werden. Das vorgeflashte Modell von STS Collective ist ein anderes Produkt.*

### Preisübersicht

| Gerät | Grundpreis | Optionales Zubehör | Gesamtpreis | Einrichtungszeit |
|--------|------------|--------------------|-------------|------------------|
| **DIY ESP32** | $5–12 | 3D-Gehäuse, Akku | $5–20 | 15–30 Min. |
| **M5 Atom Lite** | $49.99 | Akkupack $10 | $50–60 | Sofort einsatzbereit |
| **OUI-SPY** | $85 | Externe Antenne $20, Gehäuse | $85–115 | Sofort einsatzbereit |

______

## Ihr Erkennungsgerät verwenden: Praktische Szenarien

{{< figure src="flockyou-detection-device-driving-scenario.webp" alt="Fahrer blickt auf einen FlockYou-Detektor im Getränkehalter, dessen LED vor einer nahegelegenen Flock-Safety-Kamera warnt" >}}

### Szenario 1: Tägliche Pendelstrecken kartieren

**Ziel**: Flock-Kamerastandorte entlang deiner regelmäßigen Routen dokumentieren.

**Einrichtung**:
- Verwende ein GPS-fähiges Gerät, etwa einen DIY-ESP32 mit GPS-Modul oder einen OUI-SPY mit GPS
- Aktiviere die automatische Protokollierung
- Befestige das Gerät im Fahrzeug oder trage es in der Tasche
- Stelle die Empfindlichkeit auf MITTEL, um Falschmeldungen zu verringern

**Ablauf**:
1. Starte das Erkennungsgerät vor der Abfahrt
2. Fahre deine übliche Route
3. Das Gerät meldet erkannte Flock-Kameras
4. GPS-Koordinaten werden automatisch protokolliert
5. Kehre nach Hause zurück und exportiere die Daten
6. Importiere GPX- oder CSV-Daten in eine Kartierungssoftware
7. Erstelle eine persönliche Karte der Kamerastandorte

**Vorteile**:
- Du erkennst die Überwachungsabdeckung auf deinen Routen
- Du findest alternative Routen ohne Kameras
- Du trägst zu gemeinschaftlichen Kartierungsprojekten bei
- Du verfolgst Änderungen beim Ausbau im Zeitverlauf

### Szenario 2: Überwachung in der Nachbarschaft erfassen

**Ziel**: Die Abdeckung durch Flock-Kameras in deinem Wohngebiet bestimmen.

**Einrichtung**:
- Verwende ein tragbares Gerät (M5 Atom Lite, DIY-ESP32 oder OUI-SPY)
- Erkunde das Gebiet zu Fuß oder mit dem Fahrrad
- Überwache wichtige Kreuzungen im Stand

**Ablauf**:
1. Gehe oder fahre mit dem Fahrrad durch die Straßen des Viertels
2. Halte an jeder Kreuzung 30 bis 60 Sekunden an
3. Vermerke Erkennungen auf einer Karte
4. Nutze die Signalstärke, um Entfernung und Richtung abzuschätzen
5. Bestätige Kamerastandorte, wenn möglich, durch Sichtprüfung
6. Dokumentiere Beobachtungen mit Fotos aus öffentlichen Bereichen

**Ergebnis**:
- Eine vollständige Karte der lokalen Überwachungsinfrastruktur
- Belege für gemeinschaftliche Interessenvertretung
- Daten für Anträge auf öffentliche Unterlagen
- Informationen für persönliche Datenschutzentscheidungen

*Die Gehgeschwindigkeit spielt eine größere Rolle, als viele erwarten. Die Firmware wechselt etwa alle 250 ms den WLAN-Kanal, um mit den Kanalwechseln der Kamera Schritt zu halten. Wenn du zu Fuß oder mit dem Fahrrad schnell unterwegs bist, fährst du möglicherweise am Erkennungsfenster vorbei, bevor ein Kanalwechsel passt. Bei unregelmäßigen Ergebnissen halte an Kreuzungen länger an, statt sofort eine Antenne mit höherem Gewinn zu kaufen. Eine Standardantenne mit 30 bis 60 Sekunden Wartezeit an jedem Halt erkennt mehr Kameras als eine Antenne mit hohem Gewinn, wenn du zügig vorbeigehst.*

### Szenario 3: Datenschutz auf Reisen prüfen

**Ziel**: Die Überwachung auf Reisen einschätzen.

**Einrichtung**:
- Nimm ein kompaktes Gerät mit, etwa ein M5 Atom Lite in der Tasche oder einen DIY-ESP32
- Aktiviere die fortlaufende Protokollierung
- Prüfe die Daten nach der Reise

**Anwendungsfälle**:
- Arzttermine: Prüfe die Überwachung in der Nähe von Kliniken
- Rechtsberatung: Prüfe die Abdeckung rund um Kanzleien
- Religiöse Veranstaltungen: Informiere dich über Überwachung in der Nähe von Gotteshäusern
- Politische Aktivitäten: Bewerte die Überwachung bei Veranstaltungen und Protesten
- Häusliche Situationen: Stelle fest, ob eine Wohnung überwacht wird

### Szenario 4: Für die Gemeinschaft eintreten

**Ziel**: Daten für politische Debatten und öffentliche Aufklärung bereitstellen.

**Anwendungen**:
- Stelle Beobachtungen bei Stadtratssitzungen vor
- Füge sie Anträgen auf öffentliche Unterlagen bei
- Teile sie mit Datenschutzorganisationen
- Trage zu Forschungsprojekten bei
- Informiere Nachbarschaftsvereine

**Daten präsentieren**:
- Erstelle Wärmekarten zur Kameradichte
- Verfasse Berichte zu Unterschieden in der Abdeckung
- Erstelle Zeitachsen zur Ausweitung der Installationen
- Vergleiche die Standorte mit Kriminalitätsstatistiken oder deren Fehlen

______


## So funktioniert der Erkennungscode wirklich

### Vereinfachter Erkennungsalgorithmus

Für alle, die sich für die technische Umsetzung interessieren, zeigt das folgende vereinfachte Schema die Erkennungslogik:

```cpp
// Flock-You-Erkennungskern (konzeptionell, kein vollständiger Code)

// OUI-Datenbank (31 bekannte, Flock zugeordnete OUI)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // ESP32-S3-Variante von Espressif
    // ... 28 weitere OUI ...
};

// Callback für den Promiscuous-Modus
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;

    // MAC-Adresse aus dem Frame auslesen
    uint8_t *mac = pkt->payload + 10; // Position des addr2-Felds

    // Mit der OUI-Datenbank abgleichen
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // OUI-Treffer gefunden
            int rssi = pkt->rx_ctrl.rssi;

            // Schwellenwert der Signalstärke prüfen
            if (rssi > RSSI_THRESHOLD) {
                // Frame auf weitere Merkmale untersuchen
                if (is_wildcard_probe_request(pkt)) {
                    // Erkennung mit hoher Zuverlässigkeit
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // Nur OUI-Treffer
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Wildcard-Probe erkennen
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Verwaltungsframe, Untertyp Probe-Anfrage
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;

    // Auf leeres SSID-IE (Wildcard) prüfen
    // Position hängt von der Frame-Struktur ab
    uint8_t *ie = &pkt->payload[24]; // Beginn der Informationselemente
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Wildcard-Probe
    }
    return false;
}
```

### Wichtige technische Konzepte erklärt

**Promiscuous-Modus**: Statt nur Frames zu empfangen, die an das eigene Gerät adressiert sind, erfasst der ESP32 alle WLAN-Frames in Reichweite. **So lassen sich Geräte in der Nähe erkennen, die nicht mit dem Detektor kommunizieren.**

**MAC-Adressstruktur**: Jeder WLAN-Frame enthält mehrere MAC-Adressen:
- `addr1`: Empfängeradresse
- `addr2`: Senderadresse (enthält die OUI)
- `addr3`: Adresse des endgültigen Ziels oder der Quelle

**RSSI (Anzeige der empfangenen Signalstärke)**: Signalstärke in dBm, also negativen Dezibel relativ zu einem Milliwatt. Typische Werte:
- -30 dBm: extrem stark (sehr nahe)
- -50 dBm: starkes Signal
- -70 dBm: schwach, aber nutzbar
- -90 dBm: sehr schwach (Rand der Reichweite)

**Probe-Anfragen**: WLAN-Geräte senden Probe-Anfragen, um verfügbare Netzwerke zu finden. *Wildcard-Probes mit leerer SSID suchen nach jedem Netzwerk. Das ist bei IoT-Geräten wie Flock-Kameras üblich und macht sie zuverlässig erkennbar.*

______

## Häufige Probleme beheben

{{< figure src="flockyou-troubleshooting-firmware-flash-flowchart.webp" alt="Flussdiagramm zur Fehlersuche bei Firmware-Installation und Erkennung mit FlockYou, von Stromversorgungsproblemen bis zu falschen OUI-Treffern" >}}

### Problem: Keine Erkennungen trotz bekannter Kamera in der Nähe

**Mögliche Ursachen**:
1. **Kamera offline oder ausgeschaltet**: Flock-Kameras sind zeitweise nicht aktiv.
2. **Signal blockiert**: Baumaterialien wie Metall und Beton dämpfen WLAN.
3. **Außerhalb der Reichweite**: Die wirksame Reichweite beträgt je nach Hindernissen etwa 100 bis 300 Fuß.
4. **Zu schnell unterwegs**: Wegen des Kanalwechsels funktioniert langsames Gehen oder Anhalten besser als zügiges Gehen oder Autofahren.
5. **Firmwareproblem**: Veraltete Firmware erkennt neuere OUI-Varianten nicht.

**Lösungen**:
- Prüfe, ob die Kamera sichtbar und offenbar in Betrieb ist, etwa anhand von Solarmodulen oder Leuchten.
- Gehe näher an den vermuteten Kamerastandort heran oder halte dort 30 bis 60 Sekunden an, statt vorbeizulaufen.
- Probiere andere Antennenausrichtungen.
- Aktualisiere die Flock-You-Firmware.
- **Prüfe, ob das Gerät aktiv scannt**, indem du die LED- oder Display-Aktivität kontrollierst.

### Problem: Zu viele Fehlalarme

**Mögliche Ursachen**:
1. **Viele ESP32-Geräte in der Nähe**: Smart-Home- und IoT-Geräte sind weit verbreitet.
2. **Empfindlichkeit zu hoch**: Das Gerät erkennt weit entfernte oder irrelevante Geräte.
3. **Andere Überwachungskameras**: Viele verwenden ESP32-Module.

**Lösungen**:
- Verringere die Empfindlichkeit.
- Aktiviere die Erkennung von Wildcard-Probes, um zuverlässigere Treffer zu erhalten.
- Prüfe erkannte Geräte vor dem Protokollieren vor Ort.
- Filtere anhand der Signalstärke und melde nur starke Signale.
- Aktualisiere die OUI-Datenbank und konzentriere dich auf bestätigte Flock-OUI.

### Problem: Akku entlädt sich schnell

**Mögliche Ursachen**:
1. **Dauerhaftes Scannen**: Es gibt keinen Ruhe- oder Energiesparmodus.
2. **Display ständig eingeschaltet**: Der Bildschirm verbraucht viel Strom.
3. **GPS aktiv**: GPS-Module benötigen viel Energie.
4. **Alter Akku**: LiPo-Akkus verlieren mit der Zeit an Kapazität.

**Lösungen**:
- Aktiviere den passiven Scanmodus mit Unterbrechungen statt Dauerscan.
- Stelle eine Abschaltzeit für das Display ein.
- Deaktiviere GPS, wenn du keine Kartierung brauchst.
- Ersetze den Akku. Bei OUI-SPY und mesh-detect v2 lassen sich die Akkus austauschen.
- Verwende für längere Einsätze einen externen Akku.

### Problem: GPS erhält keinen Positionsfix

**Mögliche Ursachen**:
1. **Nutzung in Innenräumen**: GPS benötigt freie Sicht zum Himmel.
2. **Antenne nicht angeschlossen**: mesh-detect v2 benötigt eine angeschlossene externe Antenne.
3. **Kaltstart**: Der erste GPS-Fix dauert 5 bis 15 Minuten.
4. **Störungen**: Elektronik in der Nähe kann das Signal beeinträchtigen.

**Lösungen**:
- Begib dich an einen Ort mit freier Sicht zum Himmel.
- Prüfe, ob die Antenne am SMA-Anschluss richtig sitzt.
- Warte auf den ersten Fix. Weitere Fixes erfolgen schneller.
- Entferne dich von Quellen für Funkstörungen.
- Prüfe in den Einstellungen, ob GPS aktiviert ist.

### Problem: Daten werden nicht auf der SD-Karte gespeichert

**Mögliche Ursachen**:
1. **SD-Karte nicht formatiert**: Sie muss für die Kompatibilität FAT32 verwenden.
2. **SD-Karte voll**: Es ist kein Speicherplatz mehr frei.
3. **Karte nicht erkannt**: Sie sitzt nicht vollständig im Steckplatz.
4. **Dateisystem beschädigt**: Die Karte ist defekt.

**Lösungen**:
- **Formatiere die SD-Karte mit FAT32**. Zur Kompatibilität sind höchstens 32 GB vorgesehen.
- Lösche alte Protokolle oder verwende eine größere Karte.
- Setze die Karte vollständig ein, bis sie einrastet.
- Formatiere sie neu oder ersetze sie, wenn sie beschädigt ist.
- Prüfe, ob das Gerät die Karte erkennt. Das Menü zeigt den SD-Status an.

______

## Rechtliche und ethische Überlegungen

### Rechtlicher Status von Erkennungsgeräten

**Rechtmäßigkeit des WLAN-Scannens**:
- ✅ **In den USA legal**: passives WLAN-Monitoring im Empfangsmodus ist legal
- ✅ **Keine Abhörung**: Die Geräte überwachen nur öffentlich ausgesendete Frames
- ✅ **Keine Entschlüsselung**: Es werden weder Daten entschlüsselt noch Verbindungen zu Netzwerken hergestellt
- ✅ **Ähnlich wie Funkscanner**: vergleichbarer Rechtsstatus wie bei Polizeifunk-Scannern

**Wichtige Abgrenzungen**:
- ❌ **Illegal**: aktives Stören des Kamerabetriebs
- ❌ **Illegal**: Versuch, Kamerasysteme zu hacken oder darauf zuzugreifen
- ❌ **Illegal**: physische Kameras zu zerstören oder zu manipulieren
- ⚠️ **Rechtlich unklar**: *Einige Rechtsordnungen haben strengere Datenschutzgesetze. Prüfe vor dem Einsatz die örtlichen Vorschriften.*

**Empfehlung**: **Erkennungsgeräte dienen nur der Information. Greife nicht in den Kamerabetrieb ein.**

### Ethische Nutzungsregeln

**Verantwortungsvolle Nutzung**:
- ✅ Nutze die Geräte, um dich über Überwachung in deiner Umgebung zu informieren
- ✅ Dokumentiere Beobachtungen für Interessenvertretung und politische Gespräche
- ✅ Teile aggregierte Daten mit Datenschutzorganisationen
- ✅ Unterstütze gemeinschaftliche Kartierungsprojekte
- ✅ Informiere andere über Überwachungsinfrastruktur

**Vermeide**:
- ❌ Daten zur Unterstützung illegaler Aktivitäten zu verwenden
- ❌ Grundstückseigentümer wegen installierter Kameras zu belästigen
- ❌ Grundstücke zu betreten, um Kamerastandorte zu bestätigen
- ❌ Selbstjustiz gegen Überwachungsinfrastruktur

### Datenschutz

**Deine Daten**:
- **Erkennungsgeräte speichern DEINEN Standort** (über GPS)
- Speichere diese Daten sicher
- **Beachte das Risiko einer Vorladung**, wenn du an einem Gerichtsverfahren beteiligt bist
- Verschlüssele sensible Protokolldateien
- Lies die Datenschutzrichtlinien von Anbietern vernetzter Geräte

**Respektiere andere**:
- Achte auf deine Umgebung, wenn du Erkennungsgeräte an privaten Orten einsetzt
- Verfolge keine anderen Personen
- Bedenke die ethischen Folgen des Teilens von Daten

______

## Community und Open-Source-Entwicklung

### Zum Flock-You-Projekt beitragen

Das Flock-You-Projekt lebt von Beiträgen aus der Community:

**GitHub-Repository**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**So kannst du beitragen**:
1. **Neue OUI finden**: Melde neu identifizierte OUI von Flock-Kameras.
2. **Code verbessern**: Reiche Pull Requests mit Verbesserungen an der Firmware ein.
3. **Hardware entwerfen**: Teile eigene Entwürfe für Erkennungsgeräte.
4. **Dokumentation**: Verbessere Einrichtungsanleitungen und Übersetzungen.
5. **Testen**: Melde Fehler und prüfe Funktionen auf verschiedenen Geräten.
6. **Kartieren**: Trage zu gemeinschaftlich gepflegten Datenbanken mit Kamerastandorten bei.

### Ressourcen der Community

**Foren und Diskussionen**:
- **Reddit**: r/privacy, r/privacytoolsIO und aktive Diskussionen
- **Discord**: Colonel Panic Tech-Server mit Chat in Echtzeit
- **GitHub Issues**: Technischer Support und Funktionswünsche

**Forschungsarbeiten**:
- Akademische Studien zur ALPR-Überwachung
- Folgenabschätzungen zum Datenschutz
- Rechtliche Analysen zur Zulässigkeit von Erkennungsgeräten

**Organisationen für Interessenvertretung**:
- **Electronic Frontier Foundation** (EFF): ALPR-Verfolgung
- **ACLU**: Überwachung und Datenschutzrechte
- **Lokale Gruppen**: DeFlockJoplin und ähnliche Community-Initiativen

### Entwicklungsplan

**Geplante Funktionen** (laut GitHub-Projekt):
- **Maschinelles Lernen**: Mustererkennung für höhere Genauigkeit
- **Cloud-Synchronisierung**: Optionale, gemeinsam gepflegte Erkennungsdatenbank
- **Mobile Apps**: Smartphone-Anbindung mit erweiterten Oberflächen
- **Weitere Erkennungsmodi**: Andere Überwachungstechnologien
- **Echtzeitwarnungen**: Push-Mitteilungen über Mobilfunk oder WLAN

______

## Fazit: Datenschutz durch Open-Source-Hardware

Das **Flock-You-Erkennungsprojekt** macht Gegenspionage-Hardware für jedes Budget zugänglich. Ob du dich für den **DIY-Aufbau mit ESP32 ($5–12)**, das **einsatzbereite M5 Atom Lite ($49.99)** oder das **Multi-Modus-Gerät OUI-SPY ($85)** entscheidest: Mit jeder Option wird aus der Flock-Kameraerkennung ein Gerät, das du an einem Nachmittag bauen kannst.

*Beachte, was diese Hardware abdeckt und was nicht: Sie erkennt Flock-Kameras über WLAN. Sie erkennt weder Stingrays noch persönliche Tracker, die dir folgen. Ergänze sie bei Bedarf mit Rayhunter und Eye Spy, deren Links unten stehen.*

### Wichtigste Erkenntnisse

- **Open Source und frei anpassbar**: Die Community hält die OUI-Liste und Firmware aktuell
- **Erschwingliche Hardware**: Ein einfacher ESP32 kostet $5–12. Höhere Preisklassen bringen mehr Komfort, aber keine zusätzlichen Erkennungsfunktionen
- **Nur passives Monitoring**: Das Gerät empfängt öffentlich ausgesendete WLAN-Frames und sendet selbst nichts
- **Regelmäßige Aktualisierungen**: Neue OUI-Signaturen und Erkenntnisse zu Wildcard-Probes fließen bei Änderungen an Flocks Hardware in die Firmware ein
- **Im Feld überprüft**: Die Community DeFlockJoplin erkannte bei einer echten Fahrt 11 von 12 bekannten Kameras

### Nächste Schritte

1. **Hintergrund lesen**: [Flock-Sicherheitskameras: Verbreitung und Datenschutzprobleme](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Plattform auswählen**: Stimme DIY-Aufbau, M5 Atom Lite oder OUI-SPY auf dein Budget und deine Kenntnisse ab
3. **Hardware bestellen**: Kaufe bei einem oben aufgeführten autorisierten Anbieter
4. **Firmware flashen und einrichten**: Folge der Anleitung für deine Plattform
5. **Community beitreten**: Teile Beobachtungen und trage Erkennungen zum Projekt bei
6. **Erkennungslücken schließen**: Ergänze [Rayhunter zur Erkennung von IMSI-Catchern](/articles/how-to-flash-rayhunter-devices-complete-guide/) zur Erkennung von IMSI-Catchern und [Eye Spy für AirTags und andere Tracker](/articles/eye-spy-passive-surveillance-detector-esp32-2026/) für AirTags und andere Tracker

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  FlockYou-Geräte kaufen und 20 % sparen
{{< /centerbutton >}}

ALPR-Überwachung breitet sich aus. Wissen über Kamerastandorte hilft dir, Fahrten zu planen, Nachbarschaften zu dokumentieren und dich gegen lokale Installationen einzusetzen.

______

## Verwandte Artikel

| Artikel | Beschreibung |
|---------|--------------|
| **[Flock Safety Kameraüberwachung: Verbreitung, Datenschutzprobleme und Schutzmaßnahmen](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Der umfassende Leitfaden zum ALPR-Netz von Flock Safety, dokumentiertem Missbrauch, Ressourcen für lokale Organisation und Schutzmaßnahmen |
| **[Flock Finder: Verdächtige Flock-Safety-Kameras in deiner Nähe finden](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | So nutzt du Flock Finder, um mit WiGLE-Daten und OUI-Fingerprinting weltweit mehr als 40.000 mutmaßliche Flock-Kameras auf einer Karte zu sehen |
| **[Eye Spy: Passiver ESP32-Detektor für Überwachung und Tracker](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** | BLE- und WLAN-Detektor für das, was Flock-You nicht abdeckt: AirTags, Tile-Tracker, Körperkameras und Drohnen auf derselben Gerätefamilie |
| **[Rayhunter auf Geräten zur IMSI-Catcher-Erkennung installieren](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Schritt-für-Schritt-Anleitung zum Flashen der Rayhunter-Firmware zur Erkennung von IMSI-Catchern und Stingrays auf einem umgenutzten Mobilfunk-Hotspot statt einem ESP32 |
| **[DagShell-Custom-Firmware für den Orbic RCL400](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Vollständige Anleitung zur Installation von DagShell auf dem Orbic RCL400 für erweiterte Mobilfunknetzüberwachung und IMSI-Catcher-Erkennung |
| **[Rayhunter-Gerätevergleich 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Vergleich der von Rayhunter unterstützten Geräte, damit du passende Hardware für dein Werkzeugset zur Gegenüberwachung findest |

*Suchst du ein Werkzeug, das Trackern aktiv entgegenwirkt, statt sie nur zu erkennen? [Simulacra](https://github.com/Em3ritus/simulacra) ist ein unabhängiges Open-Source-Projekt, das die Umgebung mit BLE- und WLAN-Täuschgeräten füllt, um das Signal deines tatsächlichen Geräts zu überdecken. Es löst ein anderes Problem als die Geräte in diesem Leitfaden und kann sinnvoll sein, wenn passive Erkennung für dein Bedrohungsmodell nicht genügt.*

______

## Referenzen

1. [Flock-You-GitHub-Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - interaktive Karte von ALPR-Kameras](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - GitHub-Repository](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - offizielle Anbieterseite](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite mit vorinstallierter Firmware](https://stscollective.com)
6. [Offizielle M5Stack-Dokumentation für Atom Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
7. [Espressif-Dokumentation zur ESP32-WiFi-API](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)
8. [Referenz zu 802.11-Probe-Anfrage und -Antwort](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)
9. [DeFlock Joplin - ALPR-Recherche der Community](https://deflockjoplin.today)
10. [DeFlock - gemeinschaftlich erstellte ALPR-Karte und Daten](https://deflock.me/)
11. [Electronic Frontier Foundation - Was ist ALPR?](https://www.eff.org/pages/what-alpr)
12. [Offizieller Download der Arduino IDE](https://www.arduino.cc/en/software)
13. [Platform.io-Dokumentation](https://docs.platformio.org/)
14. [IEEE Registration Authority - großer MAC-Adressblock (OUI)](https://standards.ieee.org/products-programs/regauth/oui/)
15. [Referenz zur Struktur von 802.11-Beacon-Frames](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
