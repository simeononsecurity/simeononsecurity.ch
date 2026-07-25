---
title: "Eye Spy: Passiver Überwachungsdetektor für den M5Stack Atom Lite (ESP32)"
date: 2026-06-07
toc: true
draft: false
description: "Eine vollständige technische Referenz für Eye Spy v1.1 - ein Open-Source-passiver BLE- und WiFi-Überwachungsdetektor, der auf dem M5Stack Atom Lite (ESP32-PICO-D4) läuft und nach Bodycams, ALPR-Systemen, AirTags, Drohnen und versteckten Kameras mit einem Konfidenz-Score-Bedrohungsmodell und einer einzigen RGB-LED sucht."
genre: ["Datenschutz-Tools", "Gegenüberwachung", "IoT-Sicherheit", "Eingebettete Systeme", "Sicherheitsforschung", "WiFi-Sicherheit", "Bluetooth-Sicherheit", "ESP32-Projekte", "Hardware-Sicherheit", "Open-Source-Sicherheit"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Überwachungserkennung", "Gegenüberwachung", "BLE-Erkennung", "WiFi-Scanning", "AirTag-Erkennung", "ALPR-Erkennung", "Flock Safety", "Bodycam-Erkennung", "Drohnenerkennung", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open Source", "Datenschutz", "Passives BLE", "Promiscuous-Modus", "OUI-Erkennung", "Tracker-Erkennung", "Axon Body Camera", "Ray-Ban Meta", "Samsung SmartTag", "Tile Tracker", "Versteckte Kamera", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Eine Illustration eines kleinen M5Stack Atom Lite-Geräts mit bunten Signalwellen um es herum, alles vor einem tiefen Marineblau-Hintergrund, der Bluetooth- und WiFi-Überwachungserkennung repräsentiert."
coverCaption: ""
---

**Ein daumengroßer passiver Sensor, der Ihnen sagt, wenn etwas beobachtet**

## Einführung: Die Überwachungslandschaft, die Sie nicht sehen können

Die physische Welt wird zunehmend mit Geräten instrumentiert, die beobachten, aufzeichnen und verfolgen. Kennzeichenleser an Straßenecken, Bodycams bei Strafverfolgungsbehörden, Mietobjekt-Kameras, kommerzielle AirTag-ähnliche Tracker in Taschen oder Autos und kommerzielle Überwachungskameras an jedem Einzelhandelseingang. Die meisten dieser Geräte kommunizieren drahtlos über **Bluetooth LE** oder **WiFi**, und *die meisten dieser Kommunikationen werden offen in die Luft gefunkt, sodass jeder mit dem richtigen Empfänger sie erkennen kann*.

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) ist ein passives Überwachungserkennungswerkzeug, das genau diese Tatsache ausnutzt. Auf dem **M5Stack Atom Lite** ausgeführt, einem ESP32-PICO-D4-Entwicklungsboard etwa in der Größe eines Zuckerwürfels, überwacht Eye Spy kontinuierlich das BLE- und WiFi-Spektrum auf elektronische Signaturen von Aufnahmegeräten, Überwachungskameras, **ALPR**-Systemen (automatische Kennzeichenlesegeräte), Drohnen und persönlichen Trackern. Wenn es etwas findet, ändert seine RGB-LED die Farbe.

*Es verbindet sich mit nichts. Es sendet nicht.* Es beobachtet, bewertet und leuchtet auf.

Dieser Artikel ist eine vollständige technische Referenz: was Eye Spy erkennt, wie das Konfidenz-Score-System funktioniert, die Technik hinter jedem Erkennungsmotor, wie man es erstellt und flasht und was seine praktischen Einschränkungen sind.

---

## LED-Anzeigen: Die gesamte Benutzeroberfläche

Wie der [ESP32 WiFi Canary](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), ist Eye Spys einzige Ausgabe ein einzelner SK6812 RGB NeoPixel auf GPIO 27 des M5Stack Atom Lite. Die LED kommuniziert jederzeit einen vierstufigen Bedrohungszustand:

| Farbe | Bedeutung | Bewertungsbereich |
|-------|-----------|-------------------|
| 🔵 Blau pulsierend | Start / erster Scan | -- |
| 🟢 Grün solide | Klar - nichts erkannt | 0–2 |
| 🟡 Gelb solide | Vorsicht - mögliches Aufnahmegerät in der Nähe | 3–5 |
| 🔴 Rot blinkend | Alarm - definitives Überwachungs-/Tracking-Gerät erkannt | 6+ |

**Eine einzige hochkonfidente Erkennung (Axon Bodycam, Flock Safety Kamera, ALPR OUI-Treffer, AirTag) erzielt genug Punkte, um die LED in einem einzigen Erkennungszyklus sofort auf Rot zu setzen.** Mehrere mittelkonfidente Erkennungen akkumulieren sich auf Gelb und können sich zu Rot kombinieren.

---

## Hardware

### Primärziel: M5Stack Atom Lite

| Komponente | Detail |
|-----------|--------|
| Board | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | SK6812 NeoPixel auf GPIO 27 |
| Taste | GPIO 39 (nur Eingang) |
| Flash | 4 MB |

Der Atom Lite ist eine vollständige eigenständige Plattform. **Kein Löten, kein Breadboard, keine externen Komponenten.** Stecken Sie ihn in USB und er läuft.

### Generisches ESP32 DevKit

Eine zweite PlatformIO-Build-Umgebung (`esp32dev`) zielt auf jedes Standard-ESP32 DevKit mit einer eingebauten LED auf GPIO 2. Die gesamte Erkennungslogik läuft identisch. Der DevKit-Build ist nützlich für Entwicklung, Testen der Erkennungslogik und Einsatz, wenn der Atom Lite-Formfaktor nicht erforderlich ist.

---

## Das Bewertungssystem

Eye Spy verwendet ein **Konfidenz-Score-Modell**, das Signale aller Erkennungsmotore zu einer einzigen ganzen Zahl aggregiert. Der Score treibt den LED-Zustand (grün / gelb / rot) und unterliegt zwei automatischen Verwaltungsmechanismen:

### Score-Zerfall

Der Score sinkt **−1 Punkt alle 60 Sekunden** ohne neue Erkennungen. Wenn Sie sich von einem erkannten Gerät entfernen, kehrt die LED innerhalb weniger Minuten ohne Benutzereingriff zu Grün zurück.

### Re-Score-Abkühlung

Jeder Erkennungs-*Typ* hat eine **120-Sekunden-Abkühlung**, bevor er erneut Punkte aus derselben Quelle hinzufügen kann. *Dies verhindert, dass ein einzelnes persistentes Gerät den Score unendlich aufstapelt* - eine Flock Safety-Kamera, die in Reichweite bleibt, fügt einmal +5 hinzu und wartet dann 120 Sekunden, bevor sie erneut beitragen kann.

Diese beiden Mechanismen zusammen bedeuten:

- **Transiente Erkennungen** (ein Auto mit einem AirTag, das vorbeifährt) lösen sich automatisch auf
- **Persistente Überwachung** (ein festes Bodycam-Deployment) hält die LED auf Alarm, solange Sie in Reichweite bleiben
- **Kein unkontrollierter Scoring** von einem wiederholt gesehenen Gerät

---

## Erkennungsmotore

Eye Spy betreibt drei separate Scan-Phasen in kontinuierlicher Rotation:

**BLE passiv (9 s) → WiFi-Scan (~3 s) → Promiscuous Sniff (5 s) → Wiederholung**

BLE wird vor WiFi-Operationen explizit gestoppt, um das gemeinsam genutzte ESP32-Radio zu respektieren. Es startet zu Beginn jedes neuen Zyklus sauber neu.

---

### Motor 1: BLE - Passives Scanning

BLE-Scanning wird mit **NimBLE ohne gesendete Scan-Anfragen** implementiert. Das Gerät hört auf BLE-Werbepakete, ohne eine Antwort zu senden. *Dies macht Eye Spy für die gescannte Ausrüstung elektronisch unsichtbar* - ein passiver Scanner kann nicht vom Ziel erkannt werden.

Geräte schwächer als **−90 dBm** werden ignoriert, um Fehlalarme in dichten Umgebungen zu reduzieren.

#### BLE-Erkennungstabelle

| # | Ziel | Erkennungsmethode | Score |
|---|------|------------------|-------|
| 1 | **Axon Bodycam** | BLE MAC OUI `00:25:df` (Axon - Bodycams, Taser, LE-Ausrüstung) | +5 🔴 |
| 2 | **Ray-Ban Meta Smart Glasses** | BLE-Dienst-UUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | BLE-Gerätename enthält `Flock`, `Penguin`, `Pigvision` oder `FS Ext Battery` | +5 🔴 |
| 4 | **Kartenscanner (HC-03/05/06)** | BLE-Gerätename exakte Übereinstimmung - in Zahlungsterminal-Skimmern gefundene Bluetooth-Module | +5 🔴 |
| 5 | **Apple AirTag** | Herstellerdaten `0x004C` Subtyp `0x12`/`0x1E`, oder rohe Nutzlast `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drohne (OpenDroneID BLE)** | BLE-Dienst-UUID `0xFFFA`, oder rohe AD-Dienstdaten-Nutzlast mit App-Code `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | BLE-Dienst-UUID `0xFD5A` | +3 🟡 |
| 8 | **Tile Tracker** | BLE-Dienst-UUID `0xFEED` oder `0xFEEC` | +3 🟡 |
| 9 | **MeshCore-Knoten** | BLE-Gerätename-Präfix `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (Einzelhandels-/Veranstaltungsort-Tracking)** | Herstellerdaten `0x004C 0x02 0x15` - in Geschäften, Flughäfen und Stadien eingesetzt | +2 🟡 |
| 11 | **Unbekanntes persistentes Gerät** | Jede unklassifizierte BLE-MAC, die ≥3× über ≥5 Minuten gesehen wurde (Followererkennung) | +2 🟡 |

---

### Motor 2: WiFi-Scan - Aktiver Kanal-Scan

Der WiFi-Scan-Motor verwendet die Standard-AP-Scanning-Schnittstelle des ESP32, um nahegelegene Access Points aufzulisten und ihre BSSIDs und SSIDs gegen bekannte Überwachungsgerät-Fingerabdrücke zu vergleichen.

#### WiFi-Scan-Erkennungstabelle

| # | Ziel | Erkennungsmethode | Score |
|---|------|------------------|-------|
| 12 | **Flock Safety Kamera (OUI)** | BSSID stimmt mit 22-Eintrags-Flock Safety OUI-Tabelle überein | +5 🔴 |
| 13 | **ALPR / LPR Kamera (OUI)** | BSSID stimmt mit Motorola Solutions / Vigilant Solutions OUI `00:0e:58` überein | +5 🔴 |
| 14 | **Flock-Schlüsselwort-SSID** | SSID enthält: `flock`, `flocksafety`, `fs ext`, `penguin`, `pigvision` | +5 🔴 |
| 15 | **ALPR-Schlüsselwort-SSID** | SSID enthält: `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola`, `automate` | +4 🔴 |
| 16 | **Überwachungskamera-Hersteller (OUI)** | BSSID stimmt mit 31-Eintrags-Kamera-OUI-Tabelle überein - Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix, Ubiquiti UniFi | +3 🟡 |
| 17 | **Kamera-Schlüsselwort-SSID** | SSID enthält: `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect`, `genetec` und mehr | +2 🟡 |

---

### Motor 3: WiFi Promiscuous - Passives Frame-Sniffing

Der Promiscuous-Motor versetzt das ESP32-Radio in den **Monitor-Modus** und erfasst rohe 802.11-Management-Frames. Dies ermöglicht die Erkennung von Geräten, die keine SSID bewerben, insbesondere Drohnen, die das **Remote ID**-Protokoll über **WiFi Neighbor Awareness Networking (NaN)** verwenden.

#### Promiscuous-Erkennungstabelle

| # | Ziel | Erkennungsmethode | Score |
|---|------|------------------|-------|
| 18 | **Drohne (OpenDroneID WiFi NaN)** | 802.11-Management-Frame an Ziel `51:6f:9a:01:00:00` - ASTM F3411 Remote ID Broadcast | +4 🔴 |

---

## Phasenplan und Radio-Management

```
BLE passiv (9 s) → WiFi-Scan (~3 s) → Promiscuous Sniff (5 s) → Wiederholung
```

Der ESP32-PICO-D4 hat ein **einziges gemeinsam genutztes 2,4-GHz-Radio**, das sowohl BLE als auch WiFi handhabt. Eye Spy verwaltet dies sorgfältig.

---

## Build und Flash

### Anforderungen

- **PlatformIO** (CLI oder VS Code-Erweiterung)
- **M5Stack Atom Lite** oder beliebiges ESP32 DevKit
- USB-C-Kabel

### Flash auf M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Build und Flash für Atom Lite
pio run -e atom-lite -t upload

# Serieller Monitor bei 115200 Baud
pio device monitor -b 115200
```

### Flash auf generisches ESP32 DevKit

```bash
pio run -e esp32dev -t upload
```

---

## Erkennungshinweise und praktische Einschränkungen

### Was Eye Spy nicht kann

**5 GHz WiFi**: Der ESP32 ist ein **reines 2,4-GHz-Gerät**. Jede Überwachungskamera, jedes ALPR-System oder jeder Access Point, der ausschließlich auf 5-GHz-Bändern arbeitet, ist für den WiFi-Scan oder den Promiscuous-Motor nicht sichtbar.

**Verschlüsseltes BLE**: Mehrere hochwertige Überwachungsprodukte verschlüsseln oder verschleiern ihre BLE-Werbungen. Eye Spy erkennt Geräte, die identifizierbare Signaturen in Klartext senden.

**Kabelgebundene Kameras**: **IP-Kameras, die über Ethernet verbunden sind und kein WiFi-Radio betreiben, erzeugen keine drahtlosen Emissionen, die Eye Spy erkennen kann.**

**Reichweitenbeschränkungen**: Die ESP32-Antenne hat eine praktische Innenreichweite von **20–40 Metern** für starke Signale.

### Zu erwartende Fehlalarme

**Verbraucherkameras bei Nachbarn**: Ring, Nest, Wyze, Arlo und Reolink-Kameras sind in Wohngebieten allgegenwärtig. In wohnlichen Umgebungen erwarten Sie einige gelbe (Vorsicht, +3) Treffer von Türklingelkameras der Nachbarn.

**Einzelhandels-iBeacon-Deployments**: Große Einzelhändler setzen iBeacon-Infrastruktur in praktisch jedem Geschäft ein. Jeder Erkennungsausflug in ein Einkaufszentrum oder Lebensmittelgeschäft wird wahrscheinlich die iBeacon-Erkennung (+2) auslösen.

---

## Einsatzszenarien

### Gegenüberwachungs-Bewusstsein

Das primäre Publikum für Eye Spy ist jeder, der das Umgebungsbewusstsein für Überwachungsinfrastruktur in seiner unmittelbaren Umgebung möchte.

### AirTag-Stalking-Erkennung

AirTag-basiertes Stalking ist ein dokumentiertes Problem. Eye Spys **Follower-Erkennungsmotor** (unbekannte persistente BLE-MAC ≥3× über ≥5 Minuten gesehen) adressiert speziell modifizierte oder benutzerdefinierte Tracker.

### Mietobjekt / Hotelzimmer-Inspektion

Das Betreten eines neuen Hotelzimmers oder Mietobjekts mit laufendem Eye Spy gibt einen ersten Hinweis auf unerwartete BLE- und WiFi-sendende Geräte.

### Reisesicherheit

Wie der WiFi Canary ist Eye Spy für den Reise-Formfaktor konzipiert. Der Atom Lite passt in jede Tasche oder ist an einer Tasche befestigt.

---

## Fazit

Eye Spy adressiert ein enges, aber bedeutsames Problem: die physische Überwachungsumgebung um Sie herum wird zunehmend instrumentiert, und der Großteil dieser Instrumentierung sendet erkennbare RF-Signaturen. **Ein 15-Dollar M5Stack Atom Lite, der die Eye Spy-Firmware ausführt, wird zu einem kontinuierlichen Ambient-Scanner**, der die Komplexität der BLE-Paketanalyse und WiFi-OUI-Lookups in eine einzige RGB-LED verwandelt.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)
