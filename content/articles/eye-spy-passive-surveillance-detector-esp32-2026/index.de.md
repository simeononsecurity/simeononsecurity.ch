---
title: "Eye Spy: Passive Überwachungs- und Tracker-Erkennung mit ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Technische Referenz zu Eye Spy v1.1, einem passiven ESP32-Detektor für BLE und WiFi, der Kameras, Tracker, Drohnen und verwandte Signale erkennt."
genre: ["Datenschutzwerkzeuge", "Gegenüberwachung", "IoT-Sicherheit", "Eingebettete Systeme", "Sicherheitsforschung", "WiFi-Sicherheit", "Bluetooth-Sicherheit", "ESP32-Projekte", "Hardwaresicherheit", "Open-Source-Sicherheit"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Überwachungserkennung", "Gegenüberwachung", "BLE-Erkennung", "WiFi-Scan", "AirTag-Erkennung", "ALPR-Erkennung", "Flock Safety", "Bodycam-Erkennung", "Drohnen-Erkennung", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Quelloffen", "Datenschutz", "Passives BLE", "Promiscuous-Modus", "OUI-Erkennung", "Tracker-Erkennung", "Axon-Bodycam", "Ray-Ban Meta", "Samsung SmartTag", "Tile-Tracker", "Versteckte Kamera", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Illustration eines kleinen M5Stack Atom Lite mit farbigen Signalwellen vor dunkelblauem Hintergrund als Symbol für die Erkennung von Bluetooth- und WiFi-Überwachung."
coverCaption: ""
---

**Ein passiver Sensor in Daumengröße, der anzeigt, wenn etwas Sie beobachtet**

## Einleitung: Die unsichtbare Überwachungslandschaft

Die physische Welt wird zunehmend mit Geräten ausgestattet, die beobachten, aufzeichnen und verfolgen. Dazu gehören Kennzeichenleser an Straßenecken, Bodycams bei Polizeikräften, Kameras in Mietwohnungen, kommerzielle AirTag-ähnliche Tracker in Taschen oder Autos und Überwachungskameras an Ladeneingängen. Die meisten dieser Geräte kommunizieren drahtlos über **Bluetooth LE** oder **WiFi**. *Die meisten dieser Kommunikationen werden frei ausgestrahlt und lassen sich mit einem geeigneten Empfänger erkennen.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) ist ein Werkzeug zur passiven Überwachungserkennung, das genau diese Tatsache nutzt. Eye Spy läuft auf dem **M5Stack Atom Lite**, einem etwa zuckerwürfelgroßen Entwicklungsboard mit ESP32-PICO-D4, und überwacht fortlaufend die BLE- und WiFi-Frequenzbereiche auf elektronische Signaturen von Aufnahmegeräten, Überwachungskameras, **ALPR**-Systemen (automatic license plate reader), Drohnen und persönlichen Trackern. Sobald das Gerät etwas erkennt, ändert seine RGB-LED die Farbe.

*Es verbindet sich mit nichts und sendet nichts.* Es beobachtet, bewertet und leuchtet auf.

Dieser Artikel ist eine vollständige technische Referenz: Was Eye Spy erkennt, wie das Konfidenzbewertungsmodell funktioniert, wie die Erkennungs-Engines aufgebaut sind, wie Sie das Gerät bauen und flashen und welche praktischen Grenzen es hat.

**Sie möchten selbst kein Gerät bauen?** Vorprogrammierte, einsatzbereite **[Eye Spy-Detektoren](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** sind bei STS Collective erhältlich. Mit dem Lesercode **SIMEONONSECURITY** erhalten Sie bis zu 20 % Rabatt.

{{< stscollective-ad "eyespy" >}}

---

## LED-Anzeigen: die gesamte Benutzeroberfläche

Wie beim [ESP32 WiFi Canary (passiver WiFi-Bedrohungsdetektor)](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) besteht die gesamte Ausgabe von Eye Spy aus einem einzelnen SK6812-RGB-NeoPixel an GPIO 27 des M5Stack Atom Lite. Die LED zeigt jederzeit eine von vier Bedrohungsstufen an:

| Farbe | Bedeutung | Punktebereich |
|-------|-----------|---------------|
| 🔵 Blaues Pulsieren | Start / erster Scan | -- |
| 🟢 Dauerhaft grün | Keine Erkennung | 0–2 |
| 🟡 Dauerhaft gelb | Vorsicht, möglicherweise ein Aufnahmegerät in der Nähe | 3–5 |
| 🔴 Rot blinkend | Alarm, Überwachungs- oder Trackinggerät erkannt | 6+ |

**Eine einzelne Erkennung mit hoher Konfidenz, etwa eine Axon-Bodycam, Flock-Safety-Kamera, ALPR-OUI-Übereinstimmung oder ein AirTag, liefert genug Punkte, damit die LED bereits in einem Erkennungszyklus rot leuchtet.** Mehrere Erkennungen mittlerer Konfidenz führen zu Gelb und können zusammen Rot auslösen.

---

## Hardware

### Primäres Zielgerät: M5Stack Atom Lite

| Komponente | Details |
|------------|---------|
| Board | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | SK6812 NeoPixel an GPIO 27 |
| Taste | GPIO 39 (nur Eingang) |
| Flashspeicher | 4 MB |

Der Atom Lite ist eine vollständig eigenständige Plattform. **Kein Löten, kein Breadboard und keine externen Komponenten erforderlich.** Schließen Sie ihn per USB an, dann läuft er.

### Generisches ESP32 DevKit

Eine zweite PlatformIO-Buildumgebung (`esp32dev`) richtet sich an jedes standardmäßige ESP32 DevKit mit einer integrierten LED an GPIO 2. Die Erkennungslogik arbeitet identisch. Das DevKit eignet sich für Entwicklung, Tests der Erkennungslogik und Installationen, bei denen die kompakte Form des Atom Lite nicht nötig ist.

---

## Das Bewertungssystem

Eye Spy verwendet ein **Konfidenzbewertungsmodell**, das Signale aller Erkennungs-Engines zu einer einzelnen Ganzzahl zusammenfasst. Die Punktzahl steuert den LED-Status (grün, gelb oder rot) und wird automatisch auf zwei Arten verwaltet:

### Punkteverfall

Ohne neue Erkennungen sinkt die Punktzahl **alle 60 Sekunden um 1 Punkt**. Entfernen Sie sich von einem erkannten Gerät, kehrt die LED innerhalb weniger Minuten ohne Eingriff auf Grün zurück.

### Abkühlzeit bis zur erneuten Bewertung

Jeder Erkennungs*typ* hat eine **Abkühlzeit von 120 Sekunden**, bevor dieselbe Quelle erneut Punkte für diesen Typ hinzufügen kann. *So kann ein einzelnes dauerhaft vorhandenes Gerät die Punktzahl nicht unbegrenzt erhöhen.* Eine Flock-Safety-Kamera, die in Reichweite bleibt, erhält einmal +5 und kann erst nach 120 Sekunden erneut beitragen.

Zusammen bedeuten diese beiden Mechanismen:

- **Kurzzeitige Erkennungen**, etwa ein vorbeifahrendes Auto mit AirTag, erledigen sich automatisch.
- **Dauerhafte Überwachung**, etwa stationär eingesetzte Bodycams, hält die LED auf Alarm, solange Sie in Reichweite bleiben.
- **Keine endlose Punktesteigerung** durch wiederholte Erkennung desselben Geräts.

---

## Erkennungs-Engines

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagramm der parallelen BLE- und WiFi-Erkennungs-Engines von Eye Spy, die nach AirTags, Bodycams, ALPR-Systemen und Drohnen suchen und Signale in das Bedrohungsmodell mit Konfidenzbewertung einspeisen" >}}

Eye Spy durchläuft fortlaufend drei unterschiedliche Scanphasen:

**Passives BLE (9 s) → WiFi-Scan (~3 s) → Promiscuous-Mitschnitt (5 s) → Wiederholung**

BLE wird ausdrücklich beendet, bevor WiFi-Aktivitäten starten, damit die gemeinsam genutzte ESP32-Funkverbindung nicht gestört wird. Zu Beginn jedes neuen Zyklus startet BLE erneut.

---

### Engine 1: passives BLE-Scannen

BLE-Scans werden mit **NimBLE ausgeführt, ohne Scan-Anfragen zu senden**. Das Gerät empfängt BLE-Werbepakete, ohne darauf zu antworten. *Damit bleibt Eye Spy für die Geräte, nach denen es sucht, elektronisch unsichtbar.* Ein passiver Scanner lässt sich vom Zielgerät nicht erkennen.

Signale schwächer als **−90 dBm** werden ignoriert, um Fehlalarme in dicht belegten Umgebungen zu reduzieren.

#### BLE-Erkennungstabelle

| # | Ziel | Erkennungsmethode | Punkte |
|---|------|-------------------|--------|
| 1 | **Axon-Bodycam** | BLE-MAC-OUI `00:25:df` (Axon, Bodycams, Taser und Polizeiausrüstung) | +5 🔴 |
| 2 | **Ray-Ban-Meta-Smartbrille** | BLE-Service-UUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE** | BLE-Gerätename enthält `Flock`, `Penguin`, `Pigvision` oder `FS Ext Battery` | +5 🔴 |
| 4 | **Kartenskimmer (HC-03/05/06)** | Exakte BLE-Gerätenamen, häufig verwendete Bluetooth-Module in Skimmern an Zahlungsterminals | +5 🔴 |
| 5 | **Apple AirTag** | Herstellerdaten-Subtyp `0x12`/`0x1E` von `0x004C` oder Rohdaten-Payload `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Drohne (OpenDroneID BLE)** | BLE-Service-UUID `0xFFFA` oder rohe AD-Service-Daten-Payload mit App-Code `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | BLE-Service-UUID `0xFD5A` | +3 🟡 |
| 8 | **Tile-Tracker** | BLE-Service-UUID `0xFEED` oder `0xFEEC` | +3 🟡 |
| 9 | **MeshCore-Knoten** | BLE-Gerätename mit Präfix `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (Tracking im Einzelhandel oder an Veranstaltungsorten)** | Herstellerdaten `0x004C 0x02 0x15`, eingesetzt in Geschäften, Flughäfen und Stadien zur Bewegungsverfolgung | +2 🟡 |
| 11 | **Unbekanntes dauerhaftes Gerät** | Nicht klassifizierte BLE-MAC, die innerhalb von mindestens fünf Minuten mindestens dreimal erscheint (Erkennung von Erkundungs- oder Verfolgergeräten) | +2 🟡 |

#### Ausgewählte BLE-Erkennungen im Detail

**Axon-Bodycam (+5)**: Axon (früher TASER International) stellt die in den USA am weitesten verbreiteten Bodycamsysteme für Strafverfolgungsbehörden her. Die OUI `00:25:df` ist Axon zugewiesen und kommt in tragbarer Hardware des Unternehmens vor. **Eine einzelne Erkennung erreicht sofort die Alarmschwelle.**

**Ray-Ban-Meta-Smartbrille (+5)**: Die Zusammenarbeit von Ray-Ban und Meta bringt intelligente Verbraucherbrillen hervor, die Videos und Fotos aufnehmen können. Die BLE-Service-UUID `0xFD5F` ist die charakteristische Anzeige dieser Geräte. *Es handelt sich um ein Verbraucherprodukt, das auch an belebten öffentlichen Orten auftauchen kann.* Jede Erkennung auf dieser Punktestufe verdient Aufmerksamkeit, unabhängig von der Absicht der tragenden Person.

**Bluetooth-Module in Kartenskimmern (+5)**: HC-03, HC-05 und HC-06 sind günstige Bluetooth-Seriellmodule, die häufig in Aufsätzen an Zahlungsterminals und in Geldautomaten-Skimmern vorkommen. Die Erkennung vergleicht den exakten Gerätenamen mit bekannten Standardnamen der Modulfirmware. **Ein roter Alarm sollte eine sofortige physische Prüfung der Zahlungsterminals in der Nähe auslösen.**

**Apple AirTag (+4)**: AirTags verwenden Apples proprietäres **Nearby Interaction**-Protokoll. Die Erkennung prüft den herstellerspezifischen Datenheader (`0x004C` = Apple) und AirTag-spezifische Subtypen (`0x12` für die normale Anzeige, `0x1E` für die Anzeige eines verlorenen Gegenstands). Rohdatenmuster bieten eine zusätzliche Erkennungsabdeckung.

**OpenDroneID über BLE (+4)**: Der Standard **ASTM F3411 Remote ID**, den die FAA auch für kommerzielle Drohnen in den USA übernommen hat, definiert ein Sendeprotokoll, über das Drohnen Identität und Position bekanntgeben. Eye Spy sucht nach der GATT-Service-UUID `0xFFFA` (dem vorgesehenen Remote-ID-Dienst) und dem Anwendungscode `0x0D` in AD-Service-Daten-Payloads. *Jede regelkonforme kommerzielle Drohne in der Nähe löst diese Erkennung aus.*

**Unbekanntes dauerhaftes Gerät (+2)**: Dies ist die Engine zur **Verfolgererkennung**. Eye Spy verfolgt jede BLE-MAC, die nicht von den obigen spezifischen Erkennungen klassifiziert wird. Erscheint dieselbe unbekannte MAC innerhalb von mindestens fünf Minuten mindestens drei Mal, gibt es Punkte. Der Persistenz-Tracker beobachtet bis zu 50 unbekannte MAC-Adressen gleichzeitig. Einträge werden nach 30 Minuten ohne erneute Erkennung gelöscht. **So werden angepasste oder modifizierte Tracker erkannt, die keiner bekannten Service-UUID und keinem Hersteller-Muster entsprechen.**

**iBeacon (+2)**: Einzelhändler, Flughäfen und Stadien verwenden Apples iBeacon-Format (`0x4C 0x00 0x02 0x15`), um Bewegungen durch physische Räume zu verfolgen. Die Erkennung reagiert auf das Standard-Werbeformat, unabhängig von der UUID. Sie richtet sich nach dem Einsatzzweck, nicht nach einer bestimmten UUID. *Ein Treffer deutet darauf hin, dass Sie sich wahrscheinlich an einem Ort befinden, an dem die Anwesenheit von Bluetooth-Geräten aktiv erfasst wird.*

---

### Engine 2: WiFi-Scan, aktiver Kanalscan

Die WiFi-Scan-Engine verwendet die standardmäßige AP-Scan-Schnittstelle des ESP32, um nahegelegene Zugangspunkte aufzulisten und ihre BSSIDs und SSIDs mit bekannten Fingerabdrücken von Überwachungsgeräten abzugleichen.

#### WiFi-Erkennungstabelle

| # | Ziel | Erkennungsmethode | Punkte |
|---|------|-------------------|--------|
| 12 | **Flock-Safety-Kamera (OUI)** | BSSID stimmt mit einer Tabelle aus 22 Flock-Safety-OUI-Einträgen überein (`d4:bb:e6`, `3c:61:05`, Präfixe für FS-Ext-Battery) | +5 🔴 |
| 13 | **ALPR-/LPR-Kamera (OUI)** | BSSID stimmt mit der Motorola-Solutions-/Vigilant-Solutions-OUI `00:0e:58` überein | +5 🔴 |
| 14 | **SSID mit Flock-Schlüsselwort** | SSID enthält `flock`, `flocksafety`, `fs ext`, `penguin` oder `pigvision` | +5 🔴 |
| 15 | **SSID mit ALPR-Schlüsselwort** | SSID enthält `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` oder `automate` | +4 🔴 |
| 16 | **Überwachungskamera-Hersteller (OUI)** | BSSID stimmt mit einer Tabelle aus 31 Kamera-OUI-Einträgen überein: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix und Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID mit Kameraschlüsselwort** | SSID enthält unter anderem `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` und `genetec` | +2 🟡 |

#### Die Flock-Safety-OUI-Tabelle

Die Tabelle `FLOCK_OUIS` mit 22 Einträgen ist die detaillierteste Nachschlagetabelle des Projekts. Sie enthält:

- `d4:bb:e6` – bei IEEE registrierte Flock-Safety-OUI
- `3c:61:05` – bei IEEE registrierte Flock-Safety-OUI
- 20 weitere MAC-Präfixe, die an eingesetzter Flock-FS-Ext-Battery- und Flock-WiFi-Kamerahardware beobachtet wurden

Diese 22 Einträge stehen für MAC-Adressbereiche von Hardware, die an eingesetzten Flock-Safety-ALPR-Kamerasystemen beobachtet wurde. **Die OUI-Erkennung ist unabhängig von der SSID.** Eine Flock-Kamera ohne SSID-Schlüsselwort erhält weiterhin +5 Punkte, wenn die OUI ihrer BSSID übereinstimmt.

Die OUIs von Flock Safety und Vigilant Solutions stehen bewusst in getrennten Tabellen, damit beide im selben Scanzyklus unabhängig Punkte liefern können. *An einem Standort mit beiden Herstellertypen können während eines WiFi-Scans insgesamt +10 Punkte entstehen.*

#### OUI-Tabelle für Überwachungskamera-Hersteller

Die Tabelle mit 31 Kamera-OUI-Einträgen deckt wichtige IP-Kamerahersteller ab, deren Geräte wahrscheinlich in Überwachungsinstallationen im Einzelhandel, in Unternehmen und Wohngebäuden vorkommen:

- **Unternehmen und Gewerbe**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix, Genetec
- **Verbraucher und kleine Büros**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex, Amcrest
- **Infrastruktur**: Ubiquiti UniFi (Zugangspunkte und Kameras teilen sich OUI-Bereiche), FLIR

Eine Übereinstimmung liefert +3 Punkte im Vorsichtsbereich, auch ohne Bestätigung durch ein Schlüsselwort. Zusammen mit einem SSID-Schlüsselwort erhält dasselbe Kameranetz zunächst +5 Punkte allein für die OUI und weitere +2 für die SSID. Damit erreicht es innerhalb eines Scanzyklus die Alarmstufe.

---

### Engine 3: WiFi-Promiscuousmodus, passiver Frame-Mitschnitt

Die Promiscuous-Engine schaltet das ESP32-Funkmodul in den **Monitormodus** und erfasst rohe 802.11-Managementframes. Dadurch lassen sich Geräte erkennen, die keine SSID bekanntgeben, insbesondere Drohnen mit dem **Remote-ID**-Protokoll über **WiFi Neighbor Awareness Networking (NaN)**.

Während dieser Phase **wechselt das Funkmodul alle 400 ms zwischen den Kanälen** `{1, 6, 11, 3, 8, 13}`, um möglichst viele der NaN-Sendekanäle von Drohnen abzudecken.

#### Erkennungstabelle für den Promiscuousmodus

| # | Ziel | Erkennungsmethode | Punkte |
|---|------|-------------------|--------|
| 18 | **Drohne (OpenDroneID WiFi NaN)** | 802.11-Managementframe an die Zieladresse `51:6f:9a:01:00:00`, eine ASTM-F3411-Remote-ID-Aussendung | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: Der ASTM-F3411-Standard definiert die Multicast-Zieladresse `51:6f:9a:01:00:00` für alle Remote-ID-WiFi-NaN-Frames. Jede kommerziell regulierte Drohne, die Position und Identität per WiFi aussendet, sendet Frames an diese Adresse. Eye Spy beobachtet Managementframes, die an diese Multicast-MAC gerichtet sind. Das ist passiv und zuverlässig und *lässt sich durch die Drohnensteuerung nicht umgehen, ohne Remote ID vollständig abzuschalten, was selbst einen Regelverstoß darstellen würde*.

Diese Erkennung ergänzt die BLE-OpenDroneID-Engine (Erkennung #6). *Eine Drohne kann abhängig von Hardware und Konfiguration über BLE, WiFi oder beides senden.* Eye Spy deckt beide Varianten ab.

---

## Phasenplan und Funkverwaltung

```
Passives BLE (9 s) → WiFi-Scan (~3 s) → Promiscuous-Mitschnitt (5 s) → Wiederholen
```

Der ESP32-PICO-D4 besitzt ein **einzelnes gemeinsam genutztes 2,4-GHz-Funkmodul**, das BLE und WiFi verarbeitet. Eye Spy verwaltet den Wechsel sorgfältig:

1. **BLE-Phase** (9 Sekunden): NimBLE-Stack aktiv, passiver Scan läuft, keine Scan-Anfragen werden gesendet
2. **BLE-Stopp**: Der BLE-Stack wird angehalten, bevor WiFi verwendet wird
3. **WiFi-Scan** (~3 Sekunden): Aktiver AP-Scan auf allen Kanälen mit OUI- und SSID-Abgleich
4. **Promiscuous-Mitschnitt** (5 Sekunden): Passive Erfassung von 802.11-Frames mit Kanalwechsel
5. **WiFi-Stopp**: WiFi wird beendet und BLE für den nächsten Zyklus neu gestartet

Diese klare Phasenverwaltung verhindert Funkkonflikte und sorgt dafür, dass beide Engines in jedem Zyklus ungehindert auf das Funkmodul zugreifen können.

---

## Serielle Ausgabe

Alle Ausgaben beginnen mit `[eyespy]` und lassen sich so leicht filtern. Der serielle Monitor arbeitet mit **115200 Baud**.

### Start

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Normaler Zyklus

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Erkennungsereignisse

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

Das Feld `tracked=N` zeigt, wie viele unterschiedliche BLE-MAC-Adressen derzeit im Persistenz-Tracker stehen. So lässt sich die Dichte der BLE-Geräte in der Umgebung besser einschätzen.

### Punktfelder

Jede Statuszeile enthält:
- **score** – aktuelle Bedrohungspunktzahl
- **state** – `CLEAR` / `CAUTION` / `ALERT`
- **phase** – derzeit aktive Engine (`BLE` / `WIFI` / `PROMISC`)
- **tracked** – Anzahl eindeutiger BLE-MAC-Adressen in der Persistenztabelle

---

## Bauen und Flashen

### Voraussetzungen

- **PlatformIO** (CLI oder VS-Code-Erweiterung)
- **M5Stack Atom Lite** oder ein ESP32 DevKit
- USB-C-Kabel

### Abhängigkeiten

PlatformIO installiert diese automatisch:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** steuert die SK6812-RGB-LED an. **NimBLE-Arduino** stellt den passiven BLE-Scan-Stack bereit. Er ist der Standardbibliothek für ESP32-BLE vorzuziehen, weil er den passiven Scanmodus zuverlässig unterstützt, keine Scan-Anfragepakete sendet und weniger Speicher belegt.

### Auf den M5Stack Atom Lite flashen

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Für Atom Lite bauen und flashen
pio run -e atom-lite -t upload

# Seriellen Monitor mit 115200 Baud starten
pio device monitor -b 115200
```

### Auf ein generisches ESP32 DevKit flashen

```bash
pio run -e esp32dev -t upload
```

### Projektstruktur

```
eye-spy/
├── src/
│   └── main.cpp          # Gesamte Firmwarelogik
├── platformio.ini         # Buildumgebungen (atom-lite, esp32dev)
├── partitions_4mb.csv     # Flash-Partitionstabelle mit 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*Die Umgebung `atom-lite` verwendet die Boarddefinition `m5stick-c`.* Sie nutzt denselben ESP32-PICO-D4-Chip mit einer passenden GPIO-Belegung für das GPIO-27-NeoPixel.

---

## Hinweise zur Erkennung und praktische Grenzen

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Fotorealistische Illustration des Eye-Spy-Geräts mit M5Stack Atom Lite, ungefähr so groß wie ein Zuckerwürfel und zwischen zwei Fingern gehalten, um das kompakte Format zu zeigen" >}}

### Was Eye Spy nicht kann

**5-GHz-WiFi**: Der ESP32 unterstützt ausschließlich **2,4 GHz**. Überwachungskameras, ALPR-Systeme und Zugangspunkte, die nur das 5-GHz-Band verwenden, sind für die WiFi-Scan- und Promiscuous-Engines nicht sichtbar. *Viele moderne IP-Kameras unterstützen auch 2,4 GHz. Installationen ausschließlich mit 5 GHz werden jedoch übersehen.*

**Verschlüsseltes BLE**: Einige hochwertige Überwachungsprodukte verschlüsseln oder verschleiern ihre BLE-Anzeigen. Eye Spy erkennt Geräte, die identifizierbare Merkmale wie OUIs, Service-UUIDs und Herstellerdaten im Klartext aussenden. *Geräte mit rotierenden MAC-Adressen, einer bei Verbrauchertrackern zunehmend verbreiteten Datenschutzfunktion, umgehen die MAC-basierte Erkennung.* Der Persistenz-Tracker findet sie möglicherweise nur, wenn die Adressen seltener als alle fünf Minuten wechseln.

**Verkabelte Kameras**: **IP-Kameras, die über Ethernet verbunden sind und kein WiFi-Funkmodul verwenden, senden keine drahtlosen Signale aus, die Eye Spy erkennen könnte.** Versteckte Kameras ohne Netzwerkverbindung, die ausschließlich lokal aufzeichnen, senden ebenfalls keine RF-Signatur aus.

**Begrenzte Reichweite**: Im Innenbereich hat die ESP32-Antenne bei starken Signalen eine praktische Empfangsreichweite von **20–40 Metern**. Bei schwachen oder abgeschirmten Signalen ist sie geringer. *Geräte am Rand der Reichweite oder hinter starker RF-Abschirmung erhalten möglicherweise null Punkte oder unterschreiten den RSSI-Grenzwert von −90 dBm.*

### Erwartbare Fehlalarme

**Verbraucherkameras in Nachbarhäusern**: Ring-, Nest-, Wyze-, Arlo- und Reolink-Kameras sind in Wohngebieten weit verbreitet. Ihre OUIs stehen in der Kamera-OUI-Tabelle mit 31 Einträgen. *Rechnen Sie in Wohngebieten mit einigen gelben Treffern (Vorsicht, +3) von Türklingelkameras der Nachbarn.* Technisch sind dies keine Fehlalarme, denn *das Gerät erkennt tatsächlich eine Kamera*. Der Kontext ist entscheidend.

**iBeacon-Installationen im Einzelhandel**: Große Händler setzen iBeacon-Infrastruktur in fast allen Filialen ein. *Ein Besuch im Einkaufszentrum oder Lebensmittelgeschäft löst wahrscheinlich die iBeacon-Erkennung (+2) aus.* Auch dann erledigt das Gerät seine Aufgabe. Die Tracking-Infrastruktur im Einzelhandel ist tatsächlich vorhanden.

**Ubiquiti-UniFi-Infrastruktur**: UniFi-Zugangspunkte erscheinen in der OUI-Tabelle für Überwachungskameras, weil Ubiquiti sowohl Netzwerk- als auch Sicherheitskameraprodukte mit überlappenden OUI-Bereichen herstellt. *Eine Installation mit UniFi-Netzwerkgeräten erhält durch OUI-Treffer der WiFi-Scan-Engine +3 Punkte.*

**Samsung SmartTag und Verbrauchergeräte**: Die SmartTag-UUID (`0xFD5A`) gehört zu einem bei Samsung registrierten Dienst. *Samsung SmartTags sind Verbrauchertracker für legitime persönliche Zwecke.* Ein SmartTag-Besitzer in der Nähe löst diese Erkennung aus.

### Was die einzelnen Punktestufen praktisch bedeuten

| Punkte | Wahrscheinliche Situation in der Realität |
|--------|-------------------------------------------|
| 6–10 (🔴) | Glaubwürdige Erkennung mit hoher Konfidenz: Axon-Kamera innerhalb von etwa 30 m, Flock-Safety-Kamera mit passender OUI, bestätigtes AirTag-Folgemuster oder Drohne mit Remote-ID-Aussendung |
| 3–5 (🟡) | Mehrere Verbrauchertracker, Kameras von Nachbarn, möglicherweise eine Flock-Kamera oder eine einzelne OpenDroneID-Erkennung |
| 0–2 (🟢) | Keine wichtigen Überwachungssignaturen erkannt; normale Signale von Verbrauchergeräten bleiben unter dem Schwellenwert |

---

## Vergleich mit ähnlichen Projekten

Eye Spy richtet sich gegen physische Überwachung in der Umgebung. Der [ESP32 WiFi Canary (passiver WiFi-Bedrohungsdetektor)](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) erkennt WiFi-Angriffe auf Netzwerkebene gegen Ihre eigenen Geräte. *Die Werkzeuge ergänzen einander und behandeln unterschiedliche Bedrohungsmodelle.*

| Fähigkeit | Eye Spy | ESP32 WiFi Canary |
|-----------|---------|-------------------|
| AirTag- und Tracker-Erkennung | ✅ | ❌ |
| Erkennung von ALPR- und Flock-Kameras | ✅ | ❌ |
| Bodycam-Erkennung | ✅ | ❌ |
| Drohnenerkennung (Remote ID) | ✅ | ❌ |
| Erkennung von Evil-Twin-Zugangspunkten | ❌ | ✅ |
| Erkennung von Deauth-Angriffen | ❌ | ✅ |
| Erkennung von Sicherheits-Downgrades | ❌ | ✅ |
| Lernen einer Basislinie | ❌ | ✅ |
| Passives BLE | ✅ | ❌ |
| Dieselbe Hardwareplattform | ✅ | ✅ |

Beide Projekte laufen auf derselben M5Stack-Atom-Lite-Hardware, verwenden dieselben LED-Anzeigen und dasselbe PlatformIO-Buildsystem. Für ein umfassendes Set zur Erkennung physischer und netzwerkbasierter Überwachung können Sie beide auf verschiedene Atom-Lite-Geräte flashen und gleichzeitig mitführen.

Eye Spy ergänzt außerdem das [Flock-You-Erkennungsprojekt](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) für Nutzer, die sich gezielt mit ALPR-Überwachungsinfrastruktur befassen.

---

## Anwendungsfälle

### Bewusstsein für Gegenüberwachung

Eye Spy richtet sich vor allem an Menschen, die Überwachungsinfrastruktur in ihrer unmittelbaren Umgebung wahrnehmen möchten. Beim Spaziergang durch ein Viertel, beim Vorbeifahren an einer Kreuzung oder beim Besuch einer öffentlichen Veranstaltung liefert Eye Spy ein Echtzeitsignal. Es fasst komplexe RF-Analysen in **einem einzigen LED-Status** zusammen.

### Erkennung von AirTag-Stalking

Stalking mit AirTags ist ein dokumentiertes Problem. Die **Verfolgererkennung** von Eye Spy erkennt unbekannte, dauerhafte BLE-MAC-Adressen nach mindestens drei Erkennungen innerhalb von fünf Minuten. Sie richtet sich insbesondere gegen angepasste oder selbstgebaute Tracker, die nicht Apples bekanntem Werbeformat entsprechen. Zusammen mit der direkten AirTag-Erkennung bietet dies **zwei unabhängige Wege, einen Tracker zu erkennen, der Ihnen folgt**.

### Prüfung von Mietwohnungen und Hotelzimmern

Wenn Sie ein neues Hotelzimmer oder eine Mietwohnung mit laufendem Eye Spy betreten, erhalten Sie einen ersten Hinweis auf unerwartete Geräte, die über BLE oder WiFi senden. Eine SSID mit Kameraschlüsselwort oder eine Überwachungs-OUI aus der WiFi-Scan-Engine erhöht die Punktzahl auf Vorsicht. *Das ersetzt keine gründliche RF-Prüfung*, ergänzt aber jede physische Inspektion um eine passive Überwachung der Umgebung.

### ALPR-Installationen und Datenschutzforschung

Forschende, die Überwachungsinfrastruktur dokumentieren, Journalisten in überwachten Umgebungen und Datenschutzaktivisten, die ALPR-Installationen kartieren, können Eye Spy als kostengünstige tragbare Erkennungshardware nutzen. Die serielle Ausgabe protokolliert jede Erkennung mit RSSI und eignet sich damit als einfaches Datenerfassungsgerät.

### Reisesicherheit

Wie der WiFi Canary ist Eye Spy für unterwegs konzipiert. Der Atom Lite passt in jede Tasche oder lässt sich an einer Tasche befestigen. Auf Reisen über Flughäfen, Bahnhöfe oder öffentliche Veranstaltungen mit hoher Überwachungsdichte bietet er kontinuierliche passive Überwachung, ohne dass eine Interaktion nötig ist.

---

## Architekturhinweise

### Warum passives BLE wichtig ist

Passives BLE-Scannen ohne Scan-Anfragepakete hat wichtige Sicherheitsfolgen. Bei einem standardmäßigen BLE-Scan sendet der Scanner ein **SCAN_REQ**-Paket, um bei jedem Sender zusätzliche Werbedaten anzufordern. *Aktives BLE-Scannen ist somit für beide Seiten sichtbar.* Das gescannte Gerät sieht die Scanneradresse in der Scan-Anfrage.

Der passive Modus von NimBLE empfängt nur ungerichtete Werbepakete (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) und sendet niemals ein SCAN_REQ. **Das Eye-Spy-Gerät sendet während der Scanphase keinerlei BLE-Signale.** Eine erkannte Axon-Bodycam, ein Flock-Gerät oder ein AirTag kann den Scanner weder erkennen noch auf seine Anwesenheit reagieren.

### Aufbau des Persistenz-Trackers

Der Persistenz-Tracker für unbekannte Geräte verwaltet eine Tabelle mit bis zu **50 BLE-MAC-Adressen** sowie Zeitstempeln für die erste und letzte Erkennung. Eine Erkennung wird ausgelöst, wenn dieselbe MAC innerhalb eines Zeitraums von mindestens fünf Minuten mindestens dreimal erscheint.

Die Grenze von 50 Einträgen und das Löschfenster von 30 Minuten sind technische Entscheidungen, die Erkennungsempfindlichkeit und RAM-Beschränkungen des ESP32 abwägen. *In einer BLE-dichten Umgebung wie öffentlichen Verkehrsmitteln, einer Konferenz oder einem Einkaufszentrum kann sich die Tabelle schnell mit Verbrauchergeräten füllen.* Der RSSI-Grenzwert von −90 dBm filtert weiter entfernte Geräte heraus und richtet den Fokus auf dauerhafte Signale in der Nähe.

### Zusammenspiel von Punkteverfall und Abkühlzeit

Die **Abkühlzeit von 120 Sekunden** verhindert, dass ein dauerhaft in Reichweite befindliches Gerät in jedem neun Sekunden langen BLE-Zyklus weitere Punkte sammelt. Ohne diese Abkühlzeit würde eine einzelne Flock-Kamera alle 15 Sekunden +5 Punkte hinzufügen und innerhalb weniger Minuten Hunderte erreichen.

Der **Punkteverfall von 1 Punkt je 60 Sekunden** lässt die Punktzahl sinken, sobald ein Gerät außer Reichweite ist und die Abkühlzeit ohne neue Erkennung abläuft. *Eine einzelne Erkennung mit +5 Punkten, die nicht erneut ausgelöst wird, sinkt innerhalb von fünf Minuten auf null.* Das Gerät erreicht so auf natürliche Weise wieder Entwarnung, passend zu realistischen Bewegungsszenarien.

---

## Mitwirken und Projektstatus

Eye Spy ist unter der Apache-2.0-Lizenz auf [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy) verfügbar.

Mögliche Erweiterungen:

- **Weitere OUI-Einträge**: Die Flock-Safety- und Kamera-OUI-Tabellen lassen sich ergänzen, wenn neue Hardware-MAC-Adressen im Feld dokumentiert werden.
- **Weitere BLE-Service-UUIDs**: Neue Smartbrillen, Kameras und Tracker bringen zusätzliche UUIDs mit.
- **Anpassung des Persistenz-Trackers**: Die Grenze von 50 Einträgen, die Schwelle von drei Erkennungen und das Fünf-Minuten-Fenster sind veränderbare Konstanten.
- **Serielle Datenprotokollierung**: Das serielle Ausgabeformat ist für die programmatische Auswertung ausgelegt. Ein externer Logger könnte Erkennungsereignisse mehrerer Eye-Spy-Geräte zusammenfassen.

Die Firmware befindet sich in einer einzelnen `main.cpp` im Verzeichnis `src/`, sodass sie sich einfach lesen, prüfen und ändern lässt.

---

## Fazit

Eye Spy behandelt ein eng umrissenes, aber wichtiges Problem: Die physische Umgebung um Sie herum wird zunehmend mit Überwachungstechnik ausgestattet, und ein Großteil davon sendet erkennbare RF-Signaturen aus. **Ein M5Stack Atom Lite für 15 US-Dollar mit der Eye-Spy-Firmware wird zu einem ständig aktiven Umgebungsscanner.** Er reduziert die Komplexität der BLE-Paketanalyse und WiFi-OUI-Suche auf eine einzelne RGB-LED.

Das Konfidenzbewertungsmodell bildet realistische Bedrohungsstufen ab: Eine Axon-Bodycam in Polizeinähe erhält +5 Punkte und lässt die LED sofort rot leuchten. Ein iBeacon im Einzelhandel erhält +2 Punkte und erweitert das Lagebild, ohne allein einen Fehlalarm auszulösen. Punkteverfall und Abkühlzeiten verhindern, dass das Gerät wegen kurzzeitiger oder dauerhaft schwacher Signale unnötig Alarm schlägt.

Für Gegenüberwachung, Reisesicherheit, AirTag-Erkennung oder einfach das Wissen, ob etwas in der Nähe beobachtet, ist Eye Spy ein praktisches, quelloffenes und passiv arbeitendes Werkzeug für die Ausrüstung von Sicherheitsfachleuten.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Eye-Spy-Detektoren kaufen und 20 % sparen
{{< /centerbutton >}}
