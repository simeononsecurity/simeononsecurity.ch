---
title: "ESP32 WiFi Canary: Passive Erkennung von Bedrohungen auf 2,4 GHz"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "Technische Analyse von ESP32 WiFi Canary, einem passiven 2,4-GHz-Sensor zur Erkennung von Evil Twins, Deauthentifizierung, Sicherheitsabsenkungen und Beacon-Fluten."
genre: ["Netzwerksicherheit", "WiFi-Sicherheit", "IoT-Sicherheit", "Sicherheitsforschung", "Eingebettete Systeme", "Datenschutzwerkzeuge", "ESP32-Projekte", "Hardwaresicherheit", "Drahtlose Sicherheit", "Open-Source-Sicherheit"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "Deauthentifizierungs-Erkennung", "Evil-Twin-Erkennung", "WiFi-Sicherheit", "Passive WiFi-Überwachung", "802.11-Verwaltungsframes", "Netzwerksicherheit", "IoT-Sicherheit", "NeoPixel", "SK6812", "PlatformIO", "C++", "Quelloffene Software", "Sicherheitssensor", "Drahtlose Bedrohungserkennung", "BSSID-Überwachung", "SSID-Überwachung", "Erkennung von Sicherheitsabsenkungen", "Beacon-Flut-Erkennung", "WiFi-Überwachung", "RGB-LED", "Promiscuous-Modus", "Eingebettete Sicherheit", "Reisesicherheit", "Hotel-WiFi-Sicherheit", "WiFi im Café", "Sicherheitsbewusstsein", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "Illustration eines kleinen Geräts ähnlich dem ESP32 WiFi Canary, das an einem USB-Anschluss steckt. Eine RGB-LED leuchtet in verschiedenen Farben und symbolisiert die Fähigkeit zur Bedrohungserkennung."
coverCaption: ""
---

**Ein daumengroßer passiver WiFi-Bedrohungssensor, der niemals zurückspricht**

## Das Problem mit öffentlichem WiFi

Wenn du dich mit Hotel-WiFi, einem Hotspot im Café oder einem Flughafennetz verbindest, vertraust du darauf, dass der Zugangspunkt echt ist. Das Problem: **802.11-Verwaltungsframes**, die Netze ankündigen, Verbindungen verwalten und Clients koordinieren, sind in den meisten Umgebungen *nicht authentifiziert*. Mit einfacher Hardware kann jeder eine SSID klonen, Deauthentifizierungsframes senden oder neben einem legitimen WPA2-Netz einen offenen Köder einrichten.

Der [**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) ist ein passiver Sensor, der dieses Risiko in einem sehr kleinen Format sichtbar macht. Er passt auf den M5Stack Atom Lite, etwa so groß wie ein Zuckerwürfel. Das Gerät wird an USB angeschlossen, lernt die Umgebung und schaltet eine RGB-LED ein, wenn Muster erkannt werden, die zu drahtlosen Bedrohungen passen.

Es verbindet sich mit nichts, erfasst keine Zugangsdaten und sendet keine Frames. Es beobachtet, bewertet und zeigt die Lage durch eine Farbe an.

Dieser Artikel ist eine vollständige technische Referenz zum Projekt: Erkennung, Vertrauensmodell, Bau und Flashen sowie praktische Grenzen.

---

## Was der ESP32 WiFi Canary tut und nicht tut

### Immer nur passiv

WiFi Canary verwendet zwei Funkmodi, aber nie gleichzeitig:

1. **Promiscuous-Modus**: empfängt und prüft 802.11-Verwaltungsframes wie Deauthentifizierung und Disassoziation, ohne sich mit einem Netz zu verbinden.
2. **Scanmodus**: führt aktive WiFi-Scans durch, um nahe Zugangspunkte zu erfassen und mit einer gelernten Basislinie zu vergleichen.

Das Gerät:
- verbindet sich mit keinem Netzwerk;
- erfasst weder Datenframes noch Zugangsdaten;
- sendet keinerlei 802.11-Frames;
- speichert keine Daten dauerhaft im Flash;
- kommuniziert nicht über das Internet.

**Alle gelernten Daten bleiben im RAM und werden beim Neustart gelöscht.** Das ist Absicht: Der Canary ist ein **Sensor**, kein Aufzeichnungsgerät.

### Die LED ist die Schnittstelle

Es gibt weder Display noch App oder Weboberfläche. Die gesamte Ausgabe besteht aus einem **SK6812-RGB-NeoPixel** an GPIO 27 des M5Stack Atom Lite. Die LED zeigt vier Zustände:

| LED-Zustand | Bedeutung |
|---|---|
| 🔵 Blau (langsamer Puls) | Start, Basislinie wird aufgebaut |
| 🟢 Grün (leuchtet stetig) | Normal, keine hochvertrauenswürdigen Probleme |
| 🟡 Gelb (leuchtet stetig) | Vorsicht, verdächtiges Muster erkannt |
| 🔴 Rot (schneller Puls) | Alarm, Bedrohung mit höherer Zuverlässigkeit erkannt |

Der Start dauert etwa **24 Sekunden** (3 Scans mit je 8 Sekunden). Sobald die LED nicht mehr blau leuchtet, steht eine Basislinie bereit und die Überwachung beginnt.

---

## Hardware

### Primäres Ziel: M5Stack Atom Lite

Das Projekt wurde für den M5Stack Atom Lite entwickelt, eine vollständige ESP32-Entwicklungsplattform in einem 24 × 24 mm großen Gehäuse.

| Bauteil | Details |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | Ein SK6812-RGB-NeoPixel (GPIO 27) |
| Taste | GPIO 39, aktiv-low |
| USB | CP2104-UART-Brücke |
| Stromversorgung | USB-C, etwa 80–120 mA beim Scannen |

**Kein Steckbrett, keine externen Bauteile und kein Löten.** An USB-Strom anschließen und starten.

### Generisches ESP32 DevKit für Entwicklung und Tests

Das Projekt enthält eine zweite PlatformIO-Buildumgebung (`esp32dev`) für ein beliebiges Standard-ESP32-Entwicklungsboard. In dieser Konfiguration:

- ersetzt die integrierte LED an GPIO 2 das NeoPixel;
- ist die vollständige serielle Debugausgabe aktiviert;
- läuft die gesamte Erkennungslogik wie beim Atom Lite.

Damit ist das Projekt auch mit einem ESP32 DevKit für 5 $ zugänglich, und die Erkennungslogik lässt sich ohne Zielhardware testen.

---

## Der Basislinien-Lernprozess

### Warum eine Basislinie wichtig ist

Ein Canary, der in einer Stadt bei jedem offenen Netz Alarm schlägt, wäre nutzlos. Der ESP32 WiFi Canary lernt erst seine Umgebung und bewertet danach Bedrohungen. In der ersten Betriebsphase erstellt er eine **Referenztabelle** mit legitimen Zugangspunkten in der Umgebung.

### Drei Scans in 24 Sekunden

Beim Start führt das Gerät drei aufeinanderfolgende WiFi-Scans mit Pausen dazwischen aus. Danach speichert es die erfassten Zugangspunkte - SSID, BSSID, Verschlüsselungstyp und Signalstärke - als Basislinie.

Die serielle Ausgabe in dieser Phase sieht so aus:

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

Wechselt die LED von Blau zu Grün, ist das Gerät voll betriebsbereit.

---

## Erkannte Bedrohungen

WiFi Canary überwacht sechs Bedrohungsmuster. Jedes trägt Punkte zu einem **Vertrauenswert** bei, der den LED-Zustand steuert. *Ein einzelner Indikator gilt nicht als sicherer Beweis*: Das Modell sammelt bestätigende Hinweise, bevor es eskaliert.

### 1. Deauthentifizierungs- und Disassoziationsserien

**802.11-Verwaltungsframe-Untertypen 10 (Disassoziation) und 12 (Deauthentifizierung)** sind verbreitete Werkzeuge bei WiFi-Angriffen. Jedes Gerät kann sie senden. Clients, die sie empfangen, werden vom Zugangspunkt getrennt.

Der Canary zählt diese Frames im **Promiscuous-Modus** pro Quell-MAC-Adresse in einem gleitenden Fenster von **5 Sekunden**.

| Bedingung | Punkte |
|---|---|
| ≥ 8 Frames einer Quelle in 5 s | +2 |
| ≥ 20 Frames einer Quelle in 5 s | +4 |
| ≥ 5 Deauthentifizierungs-Broadcastframes | +1 |

**Die Schwellenwerte sind wichtig**: Ein Client, der zwischen Zugangspunkten wechselt, erzeugt einige legitime Frames. Angriffswerkzeuge senden dagegen dauerhaft Hunderte Frames pro Sekunde gegen ein Ziel. Das 5-Sekunden-Fenster und die Mindestzahl von 8 Frames filtern normales Roaming-Rauschen und erfassen anhaltende Serien von Werkzeugen wie `aireplay-ng`.

### 2. Offener Klon eines bekannten verschlüsselten Netzes (Evil Twin)

**Dies ist die Erkennung mit der höchsten Zuverlässigkeit.** Ein Evil-Twin-Angriff funktioniert oft so:

1. Eine offene Kopie eines bekannten WPA2-SSID ohne Passwort einrichten.
2. Das Signal stärker als das echte Netz senden, damit Clients automatisch verbinden.

Nach dem Lernen der Basislinie erkennt ein neuer Scan eine SSID, die vorher nur WPA/WPA2/WPA3 verwendete, nun aber als **OPEN** erscheint:

| Bedingung | Punkte |
|---|---|
| Gleiche SSID, zuvor verschlüsselt und jetzt offen | +3 |
| BSSID nicht in der Basislinie | +1 |
| Klonsignal ≥ 10 dB stärker als bekannter Zugangspunkt | +1 |

Ein offener Klon des Hotel-WiFi, der 10 dB stärker als der echte Zugangspunkt ist, ist ein Musterbeispiel. *Diese Kombination erreicht in einem Scanzyklus 5 Punkte (Vorsicht).*

**Serielles Beispiel**:

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. Ursprünglicher verschlüsselter Zugangspunkt fehlt, offener Klon vorhanden

Eine fortgeschrittene Variante: Der stärkere Klon zieht Clients an, während der echte Zugangspunkt gleichzeitig durch Deauthentifizierung aus der Luft gedrängt wird.

| Bedingung | Punkte |
|---|---|
| Verschlüsselter Basislinien-Zugangspunkt verschwunden und passendes offenes Netz aufgetaucht | +3 |

Das deckt Fälle ab, in denen der echte Zugangspunkt noch sendet, aber den Signalstärkevergleich verliert oder aktiv gestört wird.

### 4. Sicherheitsabsenkung

Die gleiche SSID wie in der Basislinie wird mit schwächerer Verschlüsselung als zuvor beobachtet.

| Bedingung | Punkte |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| Abfall um mindestens 2 Verschlüsselungsstufen | +3 |

*Offene Absenkungen gehören zur Evil-Twin-Erkennung und erhalten höhere Werte.* Diese Kategorie erfasst teilweise Absenkungen, die bei einem einfachen Vergleich von offen und verschlüsselt übersehen werden könnten.

### 5. Doppelte SSID von einem unerwarteten Anbieter

Gleiche SSID und gleicher Sicherheitstyp wie bei einem Basislinien-Zugangspunkt, aber BSSID mit einer **anderen Anbieter-OUI** (die ersten 3 Bytes der MAC-Adresse).

| Bedingung | Punkte |
|---|---|
| Andere OUI als beim Basislinien-Zugangspunkt mit derselben SSID | +1 |
| Klon ist zusätzlich ≥ 10 dB stärker | +2 |

*Der Wert ist bewusst niedrig.* Unternehmensnetze, Mesh-Systeme und Provider-Zugangspunkte haben oft mehrere legitime BSSIDs mit derselben SSID von verschiedenen Anbietern. Dieses Signal soll sich mit anderen Hinweisen summieren und keinen eigenständigen Alarm auslösen.

### 6. Beacon- oder SSID-Flut

Zählt neue, nicht in der Basislinie vorhandene SSIDs, die in einem **gleitenden 30-Sekunden-Fenster** auftauchen.

| Bedingung | Punkte |
|---|---|
| ≥ 15 neue SSIDs in 30 s | +2 |
| ≥ 30 neue SSIDs in 30 s | +3 |

**Beacon-Flutangriffe** senden Tausende gefälschte SSIDs, um Scantabellen zu verwirren oder legitime Beacon-Signale zu stören. Fünfzehn unbekannte SSIDs in 30 Sekunden sind in den meisten Umgebungen ungewöhnlich.

---

## Das Vertrauenswert-Modell

Alle erkannten Signale fließen in einen ganzzahligen **Bedrohungswert** ein, der den LED-Zustand steuert:

| Wertebereich | LED-Zustand |
|---|---|
| 0–2 | Normal (grün) |
| 3–5 | Vorsicht (gelb) |
| 6+ | Alarm (rot, schneller Puls) |

### Abbau des Werts

Ohne neue Ereignisse **sinkt der Wert alle 60 Sekunden um einen Punkt**. Das ist eine der wichtigsten praktischen Designentscheidungen:

- Eine Deauthentifizierungsserie hebt den Wert auf Vorsicht. Endet der Angriff, sinkt er innerhalb weniger Minuten automatisch auf Normal.
- Ein andauernder Angriff hält den Alarmzustand aufrecht.
- Das Gerät setzt sich ohne Eingriff oder Neustart selbst zurück.

Das bedeutet:
- **Kurze Anomalien** wie Roaming oder vorübergehende Nachbarnetze lösen sich selbst auf.
- **Anhaltende Angriffe** bleiben markiert.
- **Keine Alarmmüdigkeit** durch einzelne Ereignisse, die sich nicht wiederholen.

### Zurücksetzen per Taste

Die Taste an GPIO 39 des Atom Lite führt zwei Aktionen aus:

1. Sie gibt die vollständige aktuelle Zugangspunkttabelle über die serielle Schnittstelle aus, damit sich prüfen lässt, was das Gerät sieht.
2. Sie setzt den Bedrohungswert auf 0 und kehrt sofort zum grünen Zustand zurück, damit der nächste Scan frisch beobachtet werden kann.

---

## Bauen und Flashen

### Voraussetzungen

- **PlatformIO** (CLI oder VS-Code-Erweiterung)
- **M5Stack Atom Lite** (oder ESP32 DevKit für Tests)
- USB-C-Kabel

### Auf M5Stack Atom Lite flashen

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# Bauen und flashen
pio run -e atom-lite --target upload

# Seriellen Monitor bei 115200 Baud öffnen
pio device monitor -b 115200
```

### Auf ein generisches ESP32 DevKit flashen

```bash
pio run -e esp32dev --target upload
```

Der DevKit-Build nutzt GPIO 2 (integrierte LED) und gibt das vollständige serielle Protokoll aus. Er steuert kein NeoPixel an. Die Erkennungslogik ist mit der Atom-Lite-Version identisch.

### Projektstruktur

```
esp32-wifi-canary/
├── main.cpp              # Gesamte Firmwarelogik
├── platformio.ini        # Buildumgebungen (atom-lite, esp32dev)
├── partitions_4mb.csv    # 4-MB-Flash-Partitionstabelle
└── README.md
```

Die gesamte Firmware besteht aus **einer C++-Quelldatei**. Für die Erkennungslogik sind keine externen Bibliotheken nötig, nur das ESP32-Arduino-Framework für WiFi-Scans, Callbacks im Promiscuous-Modus und NeoPixel-Steuerung.

### platformio.ini-Umgebungen

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

Die Umgebung `atom-lite` verwendet die Boarddefinition `m5stick-c` (gleicher ESP32-PICO-D4-Chip, kompatible Pinbelegung für das NeoPixel an GPIO 27).

---

## Referenz zur seriellen Ausgabe

Das Gerät erstellt ausführliche Protokolle mit **115200 Baud**. Alle Zeilen beginnen mit `[canary]` und lassen sich dadurch leicht filtern.

### Startsequenz

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### Erkennungsereignisse

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### Wertübergänge

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

Das serielle Protokoll zeigt genau, was das Gerät wann gesehen hat und warum sich der Wert verändert hat. Es eignet sich auch als **passives Auditprotokoll**, wenn niemand auf die LED schaut.

---

## Erkennungshinweise und praktische Grenzen

Die README beschreibt ungewöhnlich offen, was das Gerät nicht leisten kann. Diese Grenzen verdienen eine genauere Erklärung.

### Mögliche Fehlalarme

**Unternehmens- und Mesh-Netze** verursachen die meisten Fehlalarme. Ein großes Unternehmensnetz, Hotel oder Mesh-System wie Eero oder Google WiFi kann legitimerweise Folgendes zeigen:

- Mehrere BSSIDs derselben SSID mit unterschiedlichen Anbieter-OUIs.
- Abweichende Sicherheitseinstellungen zwischen Frequenzbändern.
- Zugangspunkte, die bei Änderungen des Mesh-Netzes erscheinen und verschwinden.

**Airbnb- und SOHO-Router** mit mehreren SSIDs für verschiedene Bänder können ebenfalls OUI-Abweichungen verursachen, wenn 2,4- und 5-GHz-Funkgeräte aufeinanderfolgende MAC-Blöcke unterschiedlicher Anbieter verwenden.

*Vorübergehende Änderungen von Nachbarnetzen*: Ein verschlüsseltes Netz, das kurz aus dem Scan verschwindet und mit anderen Parametern wiederkommt (Firmwareupdate, Neustart oder Neukonfiguration), kann vorübergehend eine Erkennung auslösen.

Der Vertrauenswert und sein Abbau sollen Fehlalarme *verringern, nicht beseitigen*.

### Mögliche Fehl­erkennungen

Ein **gut ausgeführter Evil-Twin-Angriff**, der:

- Die exakte BSSID des legitimen Zugangspunkts fälscht, sodass die OUI übereinstimmt.
- Den Sicherheitstyp genau nachbildet, einschließlich korrekter WPA2-IE-Konfiguration.
- Mit einer Signalstärke innerhalb von 10 dB des echten Zugangspunkts arbeitet.

*Er sammelt möglicherweise nicht genug Punkte, um Vorsicht auszulösen.* Die für das Trennen der Clients nötige Deauthentifizierung würde Punkte hinzufügen. Ein raffinierter Angreifer, der wenige Deauth-Frames sendet, könnte jedoch unter dem Schwellenwert bleiben.

### Lücke beim Funkwechsel

**Das ESP32-Funkgerät kann nicht gleichzeitig im Promiscuous-Modus sein und aktiv nach Zugangspunkten scannen.** Die Firmware wechselt zwischen diesen Modi. Daher werden **Deauthentifizierungsframes während des ungefähr dreisekündigen Scanfensters nicht erfasst**. Ein Angreifer könnte seine Bursts genau auf dieses Fenster abstimmen, müsste dafür aber den Scanplan kennen.

### Nur 2,4 GHz

Das ESP32-Funkgerät arbeitet mit 2,4 GHz. **Netze mit 5 und 6 GHz werden nicht gescannt oder überwacht.** Evil Twins, die nur auf 5 GHz arbeiten, erkennt dieses Gerät nicht.

### Passive Reichweite

Für die Deauthentifizierungserkennung muss das Gerät die Frames empfangen können. Ein entfernter oder stark gerichteter Angreifer oder ein Angriff auf einen weit entfernten Client erzeugt möglicherweise keine ausreichend starken Frames für die Zähler.

---

## Einsatzszenarien

### Reisen mit sensibler Arbeit

Der Canary ist vor allem für Reisen gedacht. Schließe ihn an den USB-Anschluss eines Laptops, eine Hotelsteckdose oder eine Powerbank an und lasse ihn die Umgebung des Hotels oder Konferenzzentrums lernen. Ein später auftauchender offener Klon der Hotel-SSID, das häufigste Angriffsszenario, löst mindestens Vorsicht aus.

### Cafés und öffentliches WiFi

Offene WiFi-Umgebungen sind ein häufiges Ziel für Evil Twins. Die Basislinie lernt beim Eintreffen den legitimen Café-Zugangspunkt und überwacht anschließend konkurrierende SSIDs.

### Sicherheitsbewusstsein und Schulung

Die serielle Ausgabe liefert ein detailliertes, verständliches Protokoll. In einer Schulung ist es deutlich wirksamer, eine Deauthentifizierungsserie in Echtzeit zu zeigen und den Farbwechsel der LED zu beobachten, als eine Präsentation zu verwenden.

### Passive Laborüberwachung

In einem Heimlabor oder kleinen Büro dient der Canary als dauerhafter Umgebungsmonitor. Die LED zeigt den Status auf einen Blick. Mit der Taste lässt sich bei Bedarf die aktuelle Zugangspunkttabelle ausgeben.

---

## Architekturhinweise

### Warum ein einzelner Wert statt separater Alarme

Das Vertrauensmodell fasst unterschiedliche Signale in einer Zahl zusammen, statt einzelne Alarmkategorien darzustellen. Das ist eine bewusste Entscheidung für die Benutzeroberfläche: Die Ausgabe ist eine LED mit drei Zuständen. Separate Alarme würden Display oder App erfordern. *Das Modell wandelt verrauschte, teilweise korrelierte Signale in einen umsetzbaren Hinweis um.*

### Warum der Wert sinkt

Ohne Abbau müsste ein einzelner Fehlalarm per Tastendruck gelöscht werden. Durch den Abbau alle 60 Sekunden verschwinden kurze Anomalien innerhalb weniger Minuten. **So kann der Canary unbeaufsichtigt laufen**, etwa in einer Tasche, einem Hotelzimmer oder Auto, und nach vorübergehenden Ereignissen zum Normalzustand zurückkehren.

### Warum drei Basislinienscans

Ein einzelner Scan könnte einen Zugangspunkt übersehen, der in dieser Zeit nicht sendete, etwa wegen einer Scanlücke oder eines vorübergehenden Stromausfalls. *Drei Scans über etwa 24 Sekunden zeigen die stabile Umgebung vollständiger, bevor die Überwachung beginnt.*

---

## Mitwirken und Projektstatus

Das Projekt steht unter [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary) unter einer Lizenz für passive Nutzung. Der Code besteht aus einer einzelnen `main.cpp` und lässt sich deshalb leicht lesen, prüfen und erweitern.

Mit PlatformIO und ESP32 lässt sich das Projekt ohne Änderungen sowohl für Atom Lite als auch für ein Standard-DevKit bauen.

---

## Vergleich mit anderen WiFi-Überwachungsansätzen

| Ansatz | Passiv? | Keine Zugangsdaten | Einzelne LED-Ausgabe | Reiseformat |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet (Laptop) | ✅ | ✅ | ❌ (Display nötig) | ❌ (schwer) |
| WiFi Pineapple | ❌ (aktiv) | ❌ | ❌ | Teilweise |
| Drahtloses IDS (Unternehmen) | ✅ | ✅ | ❌ (Infrastruktur nötig) | ❌ |
| Manuelles Scannen (Smartphone-App) | Teilweise | ✅ | ❌ | ✅ |

Der Canary besetzt eine spezielle Nische: **dauerhafte Umgebungsüberwachung ohne Interaktion und ohne Netzwerkverbindung**, in einem Format für Schlüsselbund oder Laptoptasche.

---

## Fazit

Der ESP32 WiFi Canary hat genau eine Aufgabe: die 2,4-GHz-Umgebung beobachten und die Farbe ändern, wenn etwas verdächtig wirkt. Er ist kein vollständiges drahtloses Einbruchserkennungssystem, kein Paketmitschnittgerät und kein forensischer Analysator. Er ist ein Canary, ein passiver Sensor, der bemerkt, wenn die Umgebung gefährlich wird.

Das **Vertrauenswert-Modell**, der **Wertabbau** und die **dreistufige Basislinie** berücksichtigen Fehlalarme, die bei Umgebungssensoren häufig sind. Das Gerät kann unbeaufsichtigt in Hotel oder Konferenzzentrum laufen und relevante Abweichungen signalisieren, während normale Netzwerkschwankungen ruhig bleiben.

Wer ein tragbares Sicherheitskit baut, in Umgebungen mit nicht vertrauenswürdiger WiFi-Infrastruktur arbeitet oder ein nützliches ESP32-Projekt sucht, sollte einen Nachmittag und einen M5Stack Atom Lite für 15 $ einplanen.

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)
