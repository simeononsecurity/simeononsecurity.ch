---
title: "ESP32 WiFi Canary: Passive 2,4-GHz-Bedrohungserkennung mit RGB-LED-Alarmen"
date: 2026-06-06
toc: true
draft: false
description: "Eine detaillierte Analyse des ESP32 WiFi Canary-Projekts - ein kompakter, passiver 2,4-GHz-Bewusstseinssensor für den M5Stack Atom Lite, der still nach Evil-Twin-APs, Deauthentifizierungsangriffen, Sicherheits-Downgrades und Beacon-Floods sucht und ein Konfidenz-Bewertungs-Bedrohungsmodell sowie eine einzige RGB-LED verwendet."
genre: ["Netzwerksicherheit", "WiFi-Sicherheit", "IoT-Sicherheit", "Sicherheitsforschung", "Eingebettete Systeme", "Datenschutz-Tools", "ESP32-Projekte", "Hardware-Sicherheit", "Drahtlose Sicherheit", "Open-Source-Sicherheit"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Deauth-Erkennung", "Evil-Twin-Erkennung", "WiFi-Sicherheit", "Passives WiFi-Monitoring", "802.11-Management-Frames", "Netzwerksicherheit", "IoT-Sicherheit", "NeoPixel", "SK6812", "PlatformIO", "C++", "Open Source", "Sicherheitssensor", "Drahtlose Bedrohungserkennung", "BSSID-Monitoring", "SSID-Monitoring", "Sicherheits-Downgrade-Erkennung", "Beacon-Flood-Erkennung", "WiFi-Monitoring", "RGB-LED", "Promiscuous-Modus", "Eingebettete Sicherheit", "Reisesicherheit", "Hotel-WiFi-Sicherheit", "Coffeeshop-WiFi", "Sicherheitsbewusstsein", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Eine Illustration eines kleinen Geräts ähnlich dem ESP32 WiFi Canary, das in einen USB-Port eingesteckt ist, mit einer RGB-LED, die in verschiedenen Farben leuchtet, vor einem dunklen Hintergrund und seine Bedrohungserkennungsfähigkeiten symbolisiert."
coverCaption: ""
---

**Ein daumengroßer passiver WiFi-Bedrohungssensor, der nie antwortet**

## Einführung: Das Problem mit öffentlichem WiFi

Jedes Mal, wenn Sie sich mit Hotel-WiFi, einem Café-Hotspot oder einem Flughafen-Netzwerk verbinden, vertrauen Sie darauf, dass der Access Point vor Ihnen der echte ist. Das Problem ist, dass **802.11-Management-Frames** - genau die Frames, die Netzwerke ankündigen, Verbindungen verwalten und Clients koordinieren - *in den meisten Deployments vollständig unauthentifiziert sind*. Jeder mit bescheidener Hardware kann eine SSID klonen, Deauthentifizierungs-Frames an Clients senden oder einen offenes Köder neben ein legitimes WPA2-Netzwerk setzen.

Der [**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) ist ein passiver Bewusstseinssensor, der diese Realität mit dem kleinstmöglichen Fußabdruck adressiert. Er passt auf den M5Stack Atom Lite, einem Gerät etwa in der Größe eines Zuckerwürfels, steckt in jeden USB-Port, lernt die Umgebung kennen und leuchtet eine RGB-LED auf, wenn es Muster erkennt, die mit drahtlosen Bedrohungen konsistent sind.

Er verbindet sich mit nichts. Er erfasst keine Anmeldedaten. Er sendet keinen einzigen Frame. Er beobachtet, bewertet und sagt Ihnen, welche Farbe die Situation hat.

Dieser Artikel ist eine vollständige technische Referenz für das Projekt: was es erkennt, wie das Konfidenzmodell funktioniert, wie man es erstellt und flasht und was seine praktischen Einschränkungen sind.

---

## Was der ESP32 WiFi Canary tut (und nicht tut)

### Nur passiv, immer

Der WiFi Canary betreibt zwei Radio-Modi, nie gleichzeitig:

1. **Promiscuous-Modus** - empfängt und überprüft 802.11-Management-Frames (Deauth, Disassoc) ohne sich mit einem Netzwerk zu assoziieren
2. **Scan-Modus** - führt aktive WiFi-Scans durch, um nahegelegene Access Points aufzulisten und mit einer gelernten Baseline zu vergleichen

Das Gerät:
- Assoziiert sich nicht mit und verbindet sich nicht mit einem Netzwerk
- Erfasst keine Daten-Frames oder Anmeldedaten
- Sendet keine 802.11-Frames jeglicher Art
- Speichert nichts im persistenten Flash
- Kommuniziert nicht über das Internet

**Alles Gelernte wird im RAM gehalten und beim Neustart zurückgesetzt.** Dieses Design ist beabsichtigt: Der Canary ist ein **Sensor**, kein Erfassungsgerät.

### Die LED ist die Schnittstelle

Es gibt kein Display, keine App, keine Web-UI. Die einzige Ausgabe des Geräts ist ein einzelner **SK6812 RGB NeoPixel** auf GPIO 27 des M5Stack Atom Lite. Die LED spricht eine vierstufige Sprache:

| LED-Zustand | Bedeutung |
|-------------|-----------|
| 🔵 Blau (langsam pulsierend) | Start - Baseline-Referenz aufbauen |
| 🟢 Grün (solide) | Normal - keine hochkonfidenten Probleme |
| 🟡 Gelb (solide) | Vorsicht - verdächtiges Muster erkannt |
| 🔴 Rot (schnell pulsierend) | Alarm - höherkonfidente Bedrohung erkannt |

Der Start dauert ungefähr **24 Sekunden** (3 Scans × 8 Sekunden jeweils). Sobald das Gerät aus dem Blau heraus transitiert, hat es eine funktionierende Baseline und beginnt die aktive Überwachung.

---

## Hardware

### Primärziel: M5Stack Atom Lite

Das Projekt ist um den M5Stack Atom Lite konzipiert, eine vollständige ESP32-Entwicklungsplattform in einem 24 × 24 mm Gehäuse.

| Komponente | Detail |
|-----------|--------|
| MCU | ESP32-PICO-D4 |
| LED | Einzelner SK6812 RGB NeoPixel (GPIO 27) |
| Taste | GPIO 39, aktiv-niedrig |
| USB | CP2104 UART-Bridge |
| Strom | USB-C, ~80–120 mA beim Scannen |

**Kein Breadboard, keine externen Komponenten, kein Löten.** Stecken Sie es in USB-Strom und es läuft.

---

## Der Baseline-Lernprozess

### Warum eine Baseline wichtig ist

Ein Canary, der bei jedem offenen Netzwerk in einer Stadt auslöst, wäre nutzlos. Der ESP32 WiFi Canary löst das, indem er seine Umgebung lernt, bevor er mit der Bewertung von Bedrohungen beginnt.

### Drei Scans, 24 Sekunden

Beim Start führt das Gerät drei aufeinanderfolgende WiFi-Scans durch. Nach Abschluss aller drei wird der gelernte Satz von APs, SSID, BSSID, Verschlüsselungstyp, Signalstärke, als Baseline gespeichert.

---

## Was es erkennt: Bedrohungskategorien

Der WiFi Canary überwacht fünf verschiedene Bedrohungsmuster. Jedes trägt Punkte zu einem **Konfidenz-Score** bei, der den LED-Zustand steuert.

### 1. Deauthentifizierungs-/Disassoziierungs-Bursts

**802.11-Management-Frame-Subtypen 10 (Disassoc) und 12 (Deauth)** sind die Arbeitstiere von WiFi-Angriffen. Jedes Gerät kann diese Frames senden, und jeder Client, der sie empfängt, trennt sich von seinem AP.

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| ≥ 8 Frames von einer Quelle in 5 s | +2 |
| ≥ 20 Frames von einer Quelle in 5 s | +4 |
| ≥ 5 Broadcast-Deauth-Frames | +1 |

### 2. Offener Klon eines bekannten verschlüsselten Netzwerks (Evil Twin)

**Die höchstkonfidente Erkennung.** Ein Evil-Twin-Angriff funktioniert oft, indem eine offene (passwortlose) Kopie einer bekannten WPA2 SSID aufgestellt wird.

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| Gleiche SSID, war verschlüsselt, jetzt offen | +3 |
| BSSID nicht in Baseline gesehen | +1 |
| Klon-Signal ≥ 10 dB stärker als bekannter AP | +1 |

### 3. Originaler verschlüsselter AP fehlt + Offener Klon vorhanden

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| Baseline-verschlüsselter AP weg + passendes offenes Netzwerk erschienen | +3 |

### 4. Sicherheits-Downgrade

Gleiche SSID wie ein Baseline-Eintrag, aber mit schwächerer Verschlüsselung als aufgezeichnet.

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Abfall von 2+ Verschlüsselungsrängen | +3 |

### 5. Doppelte SSID von unerwartetem Hersteller

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| Anderer OUI als Baseline-AP derselben SSID | +1 |
| Klon ist auch ≥ 10 dB stärker | +2 |

### 6. Beacon-/SSID-Flood

| Bedingung | Hinzugefügte Punkte |
|-----------|---------------------|
| ≥ 15 neue SSIDs in 30 s | +2 |
| ≥ 30 neue SSIDs in 30 s | +3 |

---

## Das Konfidenz-Bewertungsmodell

Alle erkannten Signale fließen in einen einzigen ganzzahligen **Bedrohungs-Score** ein.

| Score-Bereich | LED-Zustand |
|---------------|-------------|
| 0–2 | Normal (grün) |
| 3–5 | Vorsicht (gelb) |
| 6+ | Alarm (rot, schnell pulsierende) |

### Score-Zerfall

Der Score **zerfällt um 1 Punkt alle 60 Sekunden** ohne neue Auslöseereignisse. Das bedeutet:

- Ein einzelner Deauth-Burst schiebt den Score auf Vorsicht und zerfällt dann automatisch nach einigen Minuten zurück auf Normal, wenn der Angriff aufhört
- Ein anhaltender Angriff hält den Alarm-Zustand unbegrenzt

---

## Erstellen und Flashen

### Anforderungen

- **PlatformIO** (CLI oder VS Code-Erweiterung)
- **M5Stack Atom Lite** (oder beliebiges ESP32 DevKit zum Testen)
- USB-C-Kabel

### Flash auf M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Build und Flash
pio run -e atom-lite --target upload

# Seriellen Monitor bei 115200 Baud öffnen
pio device monitor -b 115200
```

### Flash auf Generisches ESP32 DevKit

```bash
pio run -e esp32dev --target upload
```

---

## Erkennungshinweise und praktische Einschränkungen

### Was Fehlalarme verursachen kann

**Enterprise- und Mesh-Netzwerke** sind die größte Quelle von Fehlalarmen. Ein großes Enterprise-Deployment, ein Hotel mit vielen APs oder ein Mesh-System kann legitim zeigen:
- Mehrere BSSIDs für dieselbe SSID mit verschiedenen Hersteller-OUIs
- Sicherheitskonfigurationsunterschiede zwischen Bändern
- APs, die erscheinen und verschwinden, wenn das Mesh sich anpasst

### Was Fehlerkennungen verursachen kann

**Ein gut gemachter Evil-Twin-Angriff**, der die genaue BSSID des legitimen AP fälscht, den Sicherheitstyp genau anpasst und bei einer Signalstärke innerhalb von 10 dB des echten AP arbeitet, *könnte nicht genug Score ansammeln, um den Vorsicht-Schwellenwert zu überschreiten*.

---

## Einsatzszenarien

### Reisen mit sensibler Arbeit

Der Canary ist primär für Reisen konzipiert. Stecken Sie ihn in den USB-Port eines Laptops, eine Hotel-USB-Steckdose oder eine tragbare Powerbank und lassen Sie ihn die Hotel- oder Kongresszentrum-Umgebung lernen.

### Cafés und öffentliches WiFi

Offene WiFi-Umgebungen sind die häufigste Angriffsfläche für Evil-Twin-Setups.

### Sicherheitsbewusstsein und Bildung

Die serielle Ausgabe des Geräts bietet ein detailliertes, von Menschen lesbares Protokoll.

### Passives Labor-Monitoring

In einem Home-Lab oder kleinen Büro kann der Canary als persistenter Ambient-Monitor dienen.

---

## Fazit

Der ESP32 WiFi Canary ist ein eng definiertes Werkzeug, das eine Sache tut: die 2,4-GHz-Umgebung um Sie herum beobachten und die Farbe wechseln, wenn etwas falsch erscheint. Er ist ein Kanarienvogel - ein passiver Sensor, dessen Aufgabe es ist zu bemerken, wenn das Bergwerk gefährlich wird.

Das **Konfidenz-Bewertungsmodell**, der **Score-Zerfall** und der **dreiphasige Baseline-Ansatz** spiegeln sorgfältiges Nachdenken über das Fehlalarm-Problem wider. Das Ergebnis ist ein Gerät, das unbeaufsichtigt in einem Hotelzimmer oder Kongresszentrum laufen und zuverlässig signalisieren kann, wenn etwas bedeutsam Ungewöhnliches geschieht.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
