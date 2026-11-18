---
title: "Wettlauf bei der Erkennung von Flock-Kameras: Was sich 2026 geändert hat"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Berichtete Änderungen bei der Erkennung von Flock Safety, die Reaktionen der Community und Infrarotansätze zur Identifizierung von Kamerasystemen."
genre: ["Datenschutztechnologie", "Gegenüberwachung", "Open-Source-Projekte", "Digitale Rechte", "Netzwerksicherheit", "Sicherheitsforschung", "Hardware-Modifikation", "Datenschutzwerkzeuge"]
tags: ["Flock Safety", "ALPR", "Flock-You", "OUI-Erkennung", "Wildcard-Probe-Anfrage", "Promiscuous-Mode-WLAN", "802.11-Überwachung", "DeFlockJoplin", "NitekryDPaul", "BLE-Erkennung", "5-GHz-WLAN", "Lokal verwaltete MAC", "SSID-Mustererkennung", "Hardware zur Gegenüberwachung", "STS Collective", "colonelpanichacks", "Erkennungsumgehung", "ESP32", "WLAN-Erkennung", "Überwachungsbewusstsein", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "GitHub-Problemverfolgung", "Firmware-Aktualisierung", "Schutz vor Geräteerkennung durch digitale Fingerabdrücke", "MAC-Randomisierung", "Fingerprinting von Information Elements", "Kanalwechsel", "Datenschutzaktivismus", "Open-Source-Sicherheit", "Massenüberwachung", "Erkennungsfirmware", "WiFi-Erkennung während der Fahrt", "Entfernung von Kameras", "Datenschutz-Hardware", "Infraroterkennung", "IR-Beleuchtung", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Optische Erkennung", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Stadtszene mit einer Flock-Kamera an einer Straßenlaterne und einem Fahrzeug mit einem modernen Erkennungsgerät. Leuchtende Signale zeigen die drahtlose Datenkommunikation vor dunklem Hintergrund."
coverCaption: "Wie wechselnde Flock-Safety-Hardware Open-Source-Erkennungstools immer wieder ausbremst und wie die Community aufholt"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Wenn dein Flock-You-Detektor auf einer Route verstummt ist, auf der er früher jedes Mal Kameras fand, bildest du dir das nicht ein, und deine Hardware ist wahrscheinlich nicht kaputt.** Die Kamera-Hardware und Firmware von Flock Safety haben sich im vergangenen Jahr mindestens zweimal so geändert, dass die Erkennungsmethoden der Community ausfielen. Open-Source-Forschende mussten jedes Mal eine neue Signatur zurückentwickeln.

*Die Lage verändert sich schnell. Die Erkennungsmethode und die OUI-Liste unten entsprechen dem `main`-Branch von `colonelpanichacks/flock-you` mit Stand September 2026. Prüfe das [GitHub-Repository](https://github.com/colonelpanichacks/flock-you), bevor du dein Gerät für defekt hältst.*

{{< youtube id="cVf-id71BuQ" >}}

*Das Video von Valleytech Custom Solutions zeigt genau das beschriebene Symptom: Eine gewöhnliche Wardriving-Fahrt liefert über mehrere Firmware-Versionen hinweg plötzlich keine Treffer mehr, obwohl Kameras auf derselben Route früher zuverlässig erkannt wurden und einige zuvor gemeldete Kameras im Bezirk physisch entfernt worden waren.*

______

## Eine Wardriving-Fahrt, die plötzlich nichts mehr findet

Die Berichte schildern oft denselben Ablauf. Eine Person fährt eine Strecke, die sie schon Dutzende Male gefahren ist. Der Detektor läuft mit aktueller Firmware und hat dieselben Kameras früher erkannt. Auf einer Fahrt findet er nichts: kein Signalton, kein Protokolleintrag, bei allen getesteten benutzerdefinierten Builds.

Im Video von Valleytech wird ein ähnlicher Fall beschrieben: Auf dem täglichen Weg zum Postamt wurde früher mindestens eine Flock-Kamera erkannt, jetzt keine mehr. Auf einer zweiten Route nahe Micro Center waren früher fünf Kameras aktiv; inzwischen ist nur noch eine aktiv, die anderen vier wurden von den Masten entfernt.

**Im selben Zeitraum passierten zwei Dinge, die leicht zu verwechseln sind:**

- **Einige Kameras werden physisch entfernt oder versetzt**, wodurch es tatsächlich weniger Geräte zu erkennen gibt.
- **Die drahtlose Signatur der Kameras hat sich geändert**, sodass eine noch installierte Kamera bei veralteter Firmware eventuell keinen Alarm auslöst.

Zwei GitHub-Issues im Repository `colonelpanichacks/flock-you`, die Monate auseinanderliegen, dokumentieren das zweite Problem. Zusammen zeigen sie, wie die Community ihre Erkennungsmethode bereits zweimal weiterentwickeln musste.

______

## Issue #20: Der Management-Access-Point verstummte

**[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)** wurde im Januar 2026 eröffnet. Eine Person testete das Gerät neben einer bekannten, auf DeFlock verzeichneten Flock-Kamera, doch es erkannte nichts. In den folgenden Wochen kamen ähnliche Berichte aus Florida, Indiana, Atlanta und dem Mittleren Westen, mit unterschiedlicher Hardware und verschiedenen Antennen.

Ein Kommentator stellte die entscheidende Frage: **Hatte Flock auf seiner Seite etwas geändert, sodass die Erkennung bei allen ungefähr zur gleichen Zeit ausfiel?**

Der Maintainer des Projekts, colonelpanichacks, bestätigte schließlich genau das. **Um Dezember 2025 deaktivierte Flock den Management-Access-Point, über den die Kameras zuvor sendeten.** Dieser AP war die ursprüngliche Grundlage der drahtlosen Erkennung. Als er verschwand, wechselte die Community zu Bluetooth-Low-Energy-Signalen (BLE). Auch dieser Ersatz funktionierte bis zum Frühjahr 2026 nicht mehr zuverlässig.

| Erkennungsfläche | Stand |
|---|---|
| **Management-WLAN-AP** | Von Flock ungefähr im Dezember 2025 deaktiviert |
| **BLE-Beacons** | Seit Frühjahr 2026 nicht mehr zuverlässig |
| **Mobilfunk-Uplink über LTE** | Für Cloud-Uploads weiter in Verwendung, aber passiv nicht erkennbar |
| **Wildcard-802.11-Probe-Requests** | Aktuelle Grundlage der Erkennung (siehe unten) |

*Jede benutzerdefinierte Firmware, die auf den alten AP- oder BLE-Erkennungspfaden beruht, sucht inzwischen nach einem Signal, das die Kameras nicht mehr senden. Darum wird ein zuvor funktionierendes Gerät plötzlich still, obwohl seine Hardware in Ordnung ist.*

______

## Die Ersatzmethode: Wildcard-Probes und Frame-Fingerprinting

Die aktuelle Firmware `flock-you` läuft im dedizierten 802.11-Promiscuous-Modus. Das Funkgerät sendet nicht und verbindet sich mit keinem Netzwerk. Es hört nur zu und wechselt zwischen den WLAN-Kanälen 11, 6 und 1. Jeder Kanal bleibt 250 Millisekunden aktiv, um mit den häufigen Kanalwechseln der Kameras Schritt zu halten.

**Ein Alarm wird nur ausgelöst, wenn alle folgenden Bedingungen erfüllt sind:**

1. Der Frame ist eine 802.11-**Management-Probe-Request** (Typ 0, Subtyp 4).
2. Das **SSID-Information-Element ist vorhanden und hat Länge 0**. Es handelt sich also um eine Wildcard-Probe und nicht um die Suche nach einem bestimmten Netzwerk.
3. Die Senderadresse (**addr2**) stimmt mit einem bekannten Flock-OUI-Präfix überein.
4. Die übrigen Information Elements des Frames entsprechen dem von der DeFlockJoplin-Community dokumentierten Fingerabdruck. Er stützt sich auf Pintor und Atzoris Forschung von 2022 zu **[WiFi-Probe-Request-IE-Fingerprinting](https://ieeexplore.ieee.org/document/10001618)**.

Die Firmware nennt dieses Verfahren `wifi_wildcard_probe_ie_sig`. Feldtests der DeFlockJoplin-Community erfassten **11 von 12 bekannten Kameras bei nur zwei Fehlalarmen** auf ihrer Testroute. Dies ist dieselbe vor Ort bestätigte Vergleichsbasis, die im **[Hardwareleitfaden](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** des Projekts genannt wird. Die zwölfte Kamera nutzte ein OUI, das inzwischen in die Liste unten aufgenommen wurde.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Zeitachse der Flock-Kameraerkennung: vom Management-WLAN-Access-Point über Bluetooth-Low-Energy-Beacons zur aktuellen Wildcard-Probe-Anfrage und zum Information-Element-Fingerprinting. Eine vierte Phase zeigt neue SSIDs, 5 GHz und MAC-Adressumgehung." >}}

______

## Die aktuelle OUI-Liste

Der Wildcard-Probe-Fingerabdruck löst nur aus, wenn die MAC-Adresse des Senders mit einem OUI-Präfix übereinstimmt, das die Community anhand echter Flock-Hardware bestätigt hat. Vor allem der Forscher **@NitekryDPaul** pflegt die Liste. Den 31. Eintrag trug die **DeFlockJoplin**-Community bei, nachdem sie eine Kamera fand, die in der ursprünglichen Liste mit 30 Einträgen fehlte.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Diese Liste ist nicht statisch.** In der zugrunde liegenden Forschung wurden mehrere Präfixe nach Tests herabgestuft. Eines gehörte zu einem Sony-Mediaplayer, ein anderes war ein früher Platzhalter, der nie einen Treffer ergab. Zwei Einträge gelten als wenig zuverlässig. Das Präfix `82:6b:f2` bleibt trotz der lokal verwalteten Adresse enthalten, denn ein Ausschluss hätte einen bestätigten DeFlockJoplin-Treffer stillschweigend entfernt.

**Ein Eintrag wurde unabhängig an einer Kamera im kommunalen Einsatz bestätigt.** Die Flock-Einheit, deren Dateisystemabbilder im September 2026 veröffentlicht wurden, trug die MAC-Adresse **`f4:6a:dd:57:46:fb`**. `f4:6a:dd` steht an Position 13 der Liste. Diese Kamera war kein Laborgerät und keine gekaufte Probe. Sie hing an einem Mast in Wauwatosa, Wisconsin, fotografierte Verkehr und ist damit die stärkste Einzelbestätigung eines Präfixes in der Liste.

*Wenn du einen eigenen Firmware-Fork pflegst, übernimm die OUI-Liste aus dem Upstream-Verzeichnis `datasets/`, statt sie fest zu kopieren. Die Liste ändert sich mit der Forschung; eine veraltete Kopie führt schleichend dazu, dass Kameras übersehen werden.*

## Rangfolge der Erkennungssignale

Der OUI-Abgleich ist die Methode, auf die sich die aktuelle Firmware am stärksten stützt, und zugleich das schwächste der fünf verfügbaren Signale. Die Erkennungsgemeinschaft **[WiFi Mothership](https://wifimothership.com/flock)** ordnet sie nach Zuverlässigkeit und bezieht die Firmware-Forschung von GainSec ein.

| Erkennungsstärke | Signal | Bedeutung |
|---|---|---|
| **HOCH** | **BLE-Herstellerkennung `0x09C8`** (XUNTONG) | Starker Fingerabdruck, der bei Raven sowie Falcon- oder Sparrow-Geräten mit Batteriemodul vorkommt |
| **HOCH** | **Raven-BLE-Dienst-UUIDs von `0x3100` bis `0x3500`** | Raven-GATT-Dienste für GPS, Stromversorgung, Netzwerk, Upload und Fehler; nur Raven-Hardware |
| **MITTEL** | **WiFi-SSID-Muster `^Flock-[A-Z0-9]+$`** | Standard-Hotspotname bei der Einrichtung; weitere Firmware-SSIDs sind `FS Ext Battery`, `Penguin` und `Pigvision` |
| **MITTEL** | **BLE-Namensfragment** | Namen wie `FS Ext Battery` stehen in Werbepaketen, ohne dass Herstellerdaten ausgewertet werden |
| **NIEDRIG** | **MAC-Adresse und OUI-Präfix** | **Rauschstärkste Methode.** Zuliefererpräfixe tauchen in Tausenden nicht zugehörigen Produkten auf |

*Die unterste Zeile ist die Grundlage, auf die sich die aktuelle Firmware am stärksten stützt. Das ist das zentrale Problem einer Erkennung, die zuerst auf OUI-Präfixe setzt.*

### Warum die OUI-Liste so viele Fehlalarme liefert

Die 31 aufgeführten Präfixe sind nicht 31 Flock-Kennungen. WiFi Mothership verfolgt **26 davon gleichzeitig und ordnet sie ihren tatsächlichen Eigentümern zu**.

| Kategorie | Anzahl | Eigentümer |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, IEEE-Zuweisung an das Unternehmen selbst |
| **Batteriemodule** | 10 | Silicon-Labs-Komponenten in erweiterten Batteriepaketen |
| **Kameramodule** | 11 | Liteon-WLAN-Module für Kameras |
| **Recheninfrastruktur** | 4 | Raspberry Pi Foundation und Raspberry Pi Trading |

**Fünfundzwanzig dieser 26 Präfixe gehören zu Zulieferern**, deren Komponenten in großen Mengen auch in nicht zugehöriger Hardware verwendet werden. Ein Silicon-Labs- oder Liteon-Präfix erscheint daher bei Produkten ohne Verbindung zu Flock Safety. Auch Raspberry-Pi-Boards sind weit verbreitet.

**Ein Treffer ist ein Hinweis, keine Identifizierung.** Deshalb ist der Wildcard-Probe-Fingerabdruck wichtig: Zusammen mit einer OUI hebt eine Probe-Anfrage mit leerer SSID die Vertrauensbewertung auf 62 Punkte auf der Projektskala.

*Nur `B4:1E:52` beantwortet allein die Frage «Ist das ein Flock-Gerät?». Die übrigen 30 Präfixe sind unterstützende Hinweise.*

### Wie viele Kameras senden einen Hotspot

Wardriving-Daten liefern eine Untergrenze. WiFi Mothership zählte 2025 auf WiGLE **mindestens 900 Flock-Access-Points**. Ein solcher AP steht für ein Gerät, das die Standard-Hotspot-SSID `Flock-XXXX` sendet.

Die Zahl beschreibt Geräte mit einem Einrichtungshotspot, nicht alle Installationen. Flock spricht von Zehntausenden Kameras. Die meisten senden nichts, was eine vorbeifahrende Person beim Wardriving protokolliert. **Die Karte zeigt eine kleine Stichprobe.**

## Issue #43: neues SSID-Muster, 5 GHz und MAC-Anti-Fingerprinting

Drei Monate nach dem Abschluss von Issue #20 kam ein zweiter Bericht, der eine mögliche Gegenmaßnahme zur Erkennung statt einer beiläufigen Firmwareänderung beschreibt. **[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)** wurde im Mai 2026 eingereicht. Grundlage sind WiGLE-Wardriving-Daten einer Kamera, die bereits auf DeFlock bestätigt worden war. Der Bericht enthält drei Beobachtungen, auf die vorhandene Werkzeuge nicht ausgelegt waren.

### Beobachtung 1: ein anderes SSID-Format

Der dokumentierte Flock-Hotspot verwendete stets das Muster `Flock-XXXXXX`. Die Kamera in diesem Bericht sendete stattdessen **`Flock Camera net.`**. Wer auf WiGLE nach dem Platzhalter `Flock-*` suchte, erhielt für diese aktiv sendende Kamera keine Treffer.

### Beobachtung 2: bestätigter 5-GHz-Hotspot

Die Kamera sendete gleichzeitig auf **2,4 GHz, Kanal 1**, und **5 GHz, Kanal 157**. Die MAC-Adressen waren auf beiden Bändern fortlaufend (`...9f:a2:de` und `...9f:a2:df`). Das spricht für ein einzelnes Dualband-WLAN-Modul mit benachbarten Adressen für beide Funkgeräte. Eine unabhängige Meldung von nsm_barii hatte bereits eine Flock-Probe-Anfrage auf 5 GHz, Kanal 149, protokolliert. Zwei Beobachtungen bestätigen nun den tatsächlichen 5-GHz-Betrieb.

**Alle zuvor beschriebenen Methoden, auch die aktuelle Wildcard-Probe-Firmware, hören nur auf 2,4 GHz.** Eine Kamera, die ausschließlich oder überwiegend auf 5 GHz sendet, bleibt für diese Hardware unsichtbar, unabhängig von der Genauigkeit der OUI-Liste.

### Beobachtung 3: lokal verwaltete MAC-Adressen am Hotspot

Bei beiden aufgezeichneten MAC-Adressen ist das **Bit für lokale Verwaltung gesetzt**. Sie stammen also nicht aus Flocks bei IEEE registriertem OUI-Block. Die Erkennungslogik von `flock-you` überspringt solche Adressen standardmäßig, um MAC-randomisierende Telefone und Laptops herauszufiltern.

**Der Filter soll Fehlalarme reduzieren, schließt aber auch eine Flock-Kamera aus, die lokal verwaltete MAC-Adressen für ihren Hotspot verwendet.** Die fortlaufenden letzten Bytes der beiden erfassten Adressen sprechen gegen eine zufällige Zuweisung und für eine strukturierte Vergabe.

| Beobachtung | Was weiterhin funktioniert |
|---|---|
| **Neues SSID-Format** (`Flock Camera net.`) | SSID-Musterabgleich, wenn das Muster erweitert wird |
| **5-GHz-Betrieb** | Nichts in der aktuellen WLAN-Firmware, die nur 2,4 GHz scannt |
| **Lokal verwaltete MAC-Adresse** | SSID-Musterabgleich, da er nicht von der MAC-Adresse abhängt |

*Der SSID-Abgleich ist die einzige Methode in der Tabelle, die unabhängig vom Band und von der MAC-Zuweisung funktioniert. Das spricht für breitere SSID-Muster statt ausschließlicher OUI-Erkennung.*

______

## Umgeht Flock absichtlich die Erkennung?

Keines der GitHub-Issues beweist eine Absicht. Der Autor von Issue #43 stellte die Frage selbst offen: Ist das bei Flock-Installationen allgemein so oder betrifft es eine einzelne Firmwareversion auf einer Kamera?

Betrachtet man beide Issues zusammen, fällt ein Muster auf. Eine Erkennungsfläche verstummt. Die Community findet Ersatz. Dessen blinde Flecken, also die Beschränkung auf 2,4 GHz, OUI-Abgleich und das Herausfiltern lokal verwalteter MAC-Adressen, passen zu den Eigenschaften, die ein neues SSID-Format, ein 5-GHz-Funkgerät und eine lokal verwaltete MAC-Adresse ausnutzen würden. **Das kann Zufall durch einen unabhängigen Firmwarezyklus sein. Es könnte auch ein Anbieter sein, der seinen drahtlosen Fußabdruck verkleinert und dadurch die Erkennung durch Dritte absichtlich oder unbeabsichtigt erschwert.**

*Am hilfreichsten ist es, keine dieser Erklärungen vorschnell festzulegen. Baue Erkennungssysteme, die nicht von einer einzigen Annahme abhängen. Die zweijährige Geschichte dieses Projekts zeigt, dass keine Annahme dauerhaft galt.*

### Sichtprüfung: eingeschaltet, aber ohne Funkübertragung

**[Ein drittes Kurzvideo von Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) prüft die Erklärung, die Kamera sei vielleicht entfernt worden.**

{{< youtube id="sjI8FB0cLk0" >}}

Der Ersteller kehrte nachts zur Kamera aus dem ersten Video zurück. Ihre **IR-LEDs leuchteten weiterhin**, die Einheit war also eingeschaltet und beleuchtete die Szene für Nachtaufnahmen. Zugleich protokollierten **alle getesteten benutzerdefinierten Firmware-Versionen null gültige Treffer**. Ein Alarm war ein bestätigter Fehlalarm. Von der Kamera war auf der Funkseite nichts zu empfangen.

**Damit lassen sich die beiden Erklärungen trennen.** Eine entfernte Kamera erklärt kein sichtbares Gerät, das nachts eingeschaltet ist und leuchtet. Eine aktive, beleuchtete Kamera, die bei allen WLAN-Methoden stumm bleibt, weist auf eine verschwundene Funksignatur hin, nicht auf fehlende Hardware.

Nach Gesprächen mit anderen Entwicklern berichtete der Ersteller, dass dies kein Einzelfall war. **Mehrere Personen beobachteten ungefähr zur selben Zeit dasselbe Muster.** Das deutet eher auf eine koordinierte landesweite Änderung bei Flock als auf einen lokalen Sonderfall hin. *Diese Aussage ist anekdotisch und beruht auf informellen Gesprächen, nicht auf veröffentlichten Daten. Sie passt zu den Zeiträumen Dezember 2025 und Frühjahr 2026 in Issue #20. Solche Beobachtungen gehören in ein neues GitHub-Issue.*

______

## Was das für deine Erkennungshardware bedeutet

Wenn dein Gerät still geworden ist, prüfe diese Punkte, bevor du von einem Defekt ausgehst:

1. **Aktualisiere zuerst die Firmware.** Bei einer Version vor dem aktuellen `main`-Branch suchst du möglicherweise noch nach dem abgeschalteten Management-AP oder unzuverlässigen BLE-Beacons. Lade die aktuelle Firmware und flashe sie erneut.
2. **Prüfe, ob die Kamera noch vorhanden ist.** Einige Berichte ohne Treffer gingen auf tatsächlich entfernte oder versetzte Hardware zurück. Gleiche mit **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** oder **[DeFlock](https://deflock.org/)** ab, bevor du dein Gerät untersuchst.
3. **Fahre an Kreuzungen langsamer.** Bei 250 ms Verweilzeit pro Kanal kannst du am Erkennungsfenster vorbeifahren, bevor das Funkgerät den passenden Kanal erreicht. Ein Halt von 30 bis 60 Sekunden erfasst mehr Kameras als eine schnelle Vorbeifahrt mit größerer Antenne.
4. **Melde deine Beobachtung.** Null Treffer neben einer visuell bestätigten Kamera ist genau die Art von Messpunkt, aus der Issue #20 und #43 hervorgingen. Eröffne ein Issue, statt anzunehmen, jemand anderes habe es bereits gemeldet.
5. **Beachte die aktuellen Grenzen.** Firmware, die nur WLAN auf 2,4 GHz nutzt, erkennt keine Kamera auf 5 GHz oder eine Kamera, die auf den gescannten Bändern nicht sendet. Das ist derzeit eine echte Lücke und kein Fehler deiner konkreten Version.

**Die Hardware ist deshalb nicht nutzlos.** OUI-Liste und Wildcard-Probe-Fingerabdruck erkennen weiterhin die große Mehrheit der installierten Kameras. Betrachte jeden Detektor als Momentaufnahme eines laufenden Wettlaufs, nicht als dauerhafte Lösung.

{{< stscollective-ad "flockyou" >}}

______

## Ein paralleler Ansatz: den Infrarotblitz statt des WLAN-Signals erkennen

Drahtlose Erkennung ist nicht die einzige Seite dieses Wettlaufs. **[Ein weiteres Video](https://www.youtube.com/shorts/mzpr6bslsYA) von Valleytech Custom Solutions beschreibt einen anderen Ansatz**: Statt einem Funksignal zuzuhören, wird die Infrarotbeleuchtung der Kamera beobachtet.

{{< youtube id="mzpr6bslsYA" >}}

Die meisten ALPR-Kameras, auch die von Flock, verwenden **Infrarotlicht, um nachts lesbare Kennzeichen aufzunehmen**. Für Menschen ist IR-Licht unsichtbar, ein Bildsensor ohne IR-Sperrfilter erkennt es jedoch. *Das fehlende IR-Cut-Filter macht aus einem gewöhnlichen Kameramodul einen Flock-Detektor.*

### So sieht der Prototyp aus

Der im Video beschriebene Ansatz wurde mehrfach überarbeitet:

- **Erster Versuch**: spezielle IR-Fotodiodenempfänger. Technisch brauchbar, aber für ein praktisches DIY-Projekt zu teuer.
- **Zweiter Versuch**: **Jetson Nano mit Raspberry-Pi-Kameramodul**. Damit wurde das Konzept bestätigt, doch Kosten und Stromverbrauch eigneten sich nicht für ein tragbares oder fahrzeugmontiertes Gerät.
- **Aktueller Aufbau**: **ESP32-Kameramodul ohne IR-Cut-Linse**. Der Ersteller testete **ESP32-CAM** und **M5Stack S3 Cam**, bevor er sich für **Seeed Studio XIAO ESP32S3 Sense** entschied. Dazu kommt ein **Seeed-XIAO-GNSS-Modul mit Quectel-L76K-Chip**, das GPS-Koordinaten zu den Treffern speichert, ähnlich wie das GPS-Wardriving-Dashboard von `flock-you`.

| Anforderung | Warum sie zählt |
|---|---|
| **Kameramodul ohne IR-Cut-Filter** | Der Filter für farbtreue normale Fotos blockiert genau das Licht, das diese Methode erkennen muss |
| **Kamera statt Fotodiode** | Fotodiodenempfänger, die das Signal isolieren konnten, waren für einen praktischen DIY-Aufbau zu teuer |
| **GPS-Protokollierung** | Verknüpft Treffer mit einem Ort, wie das Flask-Dashboard der WLAN-Firmware |

### Blinkmuster der Kamera

Der Ansatz setzt voraus, dass die Beleuchtung in einem wiederkehrenden Muster blinkt. Der Ersteller berichtete von einer **selbst gemessenen Zeit von etwa 20 Millisekunden an und 80 Millisekunden aus, also 100 Millisekunden pro Periode, 20 Prozent Tastgrad bei 10 Hz**. Er betonte, dass dieser Wert unbestätigt und möglicherweise falsch sei. *Nutze ihn als Startpunkt für eigene Messungen, nicht als bestätigte Spezifikation. Flock hat den Wert nicht veröffentlicht und der Ersteller beansprucht keine Gewissheit.*

### Projektstatus

**Das ist ein früher DIY-Prototyp, kein fertiges Produkt.** Der Ersteller bezeichnete die Software als «vibe coded» und noch in Arbeit. Ein Summer für akustische Alarme ist geplant, aber noch nicht eingebaut. Eine fertige Platine wie OUI-SPY gibt es nicht. Die aktuelle Version erfordert, dass **ein Mensch visuell bestätigt**, ob ein gemeldeter Treffer tatsächlich eine Kamera und keine andere IR-Lichtquelle ist. Das Gerät dient als Vorauswahl, nicht als vollautomatische Erkennung.

*Diese Erkennungsfläche hängt nicht von WLAN, 2,4 oder 5 GHz, OUI-Abgleich oder MAC-Verhalten ab. Die in Issue #43 beschriebenen Umgehungstechniken gelten daher nicht dafür. Eigene Grenzen bleiben: Sichtlinie, Störungen durch Tageslicht und ein nicht unabhängig bestätigter Tastgrad.*

______

## Was die Community unternimmt

Die Reaktion auf beide Issues folgte demselben Muster, das das Projekt seit zwei Jahren nützlich macht: Jemand meldet eine Lücke, jemand anderes trägt eine Korrektur bei, und sie erscheint als Update statt in einem Rückstand zu landen.

- **Issue #20** endete mit einer bestätigten Ursache und einer Firmware-Neufassung rund um die Wildcard-Probe-Signatur, gestützt auf Feldforschung der DeFlockJoplin-Community.
- **Issue #43** ist zum Zeitpunkt dieses Artikels noch offen. Der Vorschlag, das SSID-Muster zu ergänzen, wurde noch nicht umgesetzt. *`Flock Camera` als zusätzliches Muster aufzunehmen ist ein klar abgegrenzter Beitrag für Personen, die mit der Abgleichlogik der Firmware vertraut sind.*
- Der OUI-Datensatz ist versioniert und datiert. Herabgestufte Einträge und Einträge mit geringer Sicherheit werden dokumentiert, damit Forks nachvollziehen können, was sich geändert hat und warum.

*Das ist der praktische Vorteil quelloffener Erkennungstools gegenüber proprietären Lösungen. Eine Person, die eine Lücke findet, kann einen geschlossenen Detektor nicht selbst korrigieren. Dieses Projekt wurde bereits zweimal angepasst.*

______

## Die andere Reaktion: die Hardware entfernen

Drahtlose Erkennung ist eine Reaktion auf diese Kameras. Eine parallele Initiative nahm die Hardware selbst ins Visier und lieferte im September 2026 die detailliertesten öffentlichen Belege über das Innenleben einer Flock-Kamera.

**Das stegan0gram-Kollektiv entfernte eine Kamera von ihrem Mast, kopierte den internen Speicher und veröffentlichte Dateisystemabbilder über Distributed Denial of Secrets.** Es beschrieb die Arbeit so:

> "Warum sie nur zerstören, wenn wir sie zurückentwickeln und die Geheimnisse derjenigen finden können, die uns ausspionieren? Wir haben Hardware vor Ort befreit, außer Betrieb genommen und anschließend die Kameras und zugehörige Solarausrüstung zurückentwickelt."

*Der Unterschied ist wichtig. Eine zerstörte Kamera entfernt ein Gerät. Reverse Engineering liefert Belege über alle Geräte.*

### Was die Entfernung offenbarte

Der Datensatz enthält eine **18-GB-Medienpartition**, ein **1,5-GB-Android-Systemabbild** und eine **32-MB-Anmeldedatenpartition**, außerdem den wiederhergestellten Schlüssel für den verschlüsselten Mediencontainer. Forschende ermittelten Betriebssystem- und Kernelversionen, fest einprogrammierte Backend-Zugangsdaten und unverschlüsselte Authentifizierungstoken im Kameraspeicher.

Diese Beweisgrundlage ergänzt die Sicherheitsforschung in **[Schwachstellen in Flock-Safety-Kameras: mehr als 50 Fehler gefunden](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**. Diese Forschung stützte sich zuvor auf Laborgeräte und gekaufte Exemplare.

### Reaktionen auf die Entfernung

Physische Eingriffe haben Folgen, und das Bild ist gemischt:

- **Landesweit wurden mehrere Personen wegen mutmaßlicher Beschädigung von Flock-Kameras festgenommen.**
- **Einige Kommunen kündigten an, die Kameras nicht weiter zu nutzen.** Das ist das gewünschte Ergebnis der Kritiker.
- **Eine Polizeidienststelle baute ein falsches Gehäuse einer 3D-gedruckten Flock-Kamera**, um mögliche Täter anzulocken und festzunehmen.

Noel Pichardo, ein ehemaliger Polizist in Pawtucket, Rhode Island, wurde zum Flock-Kritiker, nachdem er die Kameranutzung seiner Dienststelle angefochten hatte. Gegenüber WIRED sagte er, er verstehe die Frustration, fürchte aber, dass Sabotage Polizei und Regierung in ihrer Überzeugung bestärke, diese Technik sei notwendig. «Je länger die Regierung den Beschwerden von Anwohnern widerspricht, die diese Art von Überwachung ablehnen, desto öfter wird das passieren», sagte er.

### Wo Erkennung hineinpasst

Die Demontage ändert das Erkennungsproblem nicht. Die Kamera sendet weiterhin; die Firmware benötigt weiterhin OUI-Liste und Probe-Signatur; die beiden dokumentierten Ausfälle bleiben bestehen.

Der Datendump bestätigt die **Hardware-Identität**, darunter einen OUI-Eintrag, der an einem echten Gerät überprüft wurde. **Kameras verschwinden von einer Route, weil ein Stadtrat einen Vertrag beendet, nicht weil ein Detektor verstummt.** Drahtlose Werkzeuge beantworten eine persönliche Frage zur eigenen Umgebung. Die politische Debatte beantwortet die größere Frage, und der Datendump lieferte dafür bislang die stärksten Belege.

______

## Fazit: Erkennung bleibt ein bewegliches Ziel

Ein stiller Detektor auf einer Route, auf der früher Kameras gefunden wurden, beweist nicht, dass die Hardware defekt ist. Er zeigt, dass sich die drahtlose Signatur erneut verändert hat, bereits zweimal innerhalb eines Jahres. **Der Management-Access-Point, BLE-Beacons und möglicherweise die Annahmen «nur 2,4 GHz» und «nur OUI» in der Firmware** waren jeweils nur vorübergehend zuverlässig.

**Die Lösung war nie, drahtlose Erkennung aufzugeben.** Halte Annahmen sichtbar und dokumentiert, damit du sie anpassen kannst, wenn Issue #20 oder #43 auftaucht. Das ist das Argument für Open-Source-Firmware statt eines geschlossenen Angebots: Die Community kann eine entdeckte Lücke schließen, ohne auf den Anbieter zu warten.

### Wichtigste Punkte

- **Zwei Erkennungssignale sind bereits ausgefallen**: der Management-WLAN-AP, ungefähr seit Dezember 2025 abgeschaltet, und BLE-Beacons, die seit Frühjahr 2026 unzuverlässig sind.
- **Die aktuelle Methode mit Wildcard-Probes, OUI- und IE-Fingerprinting fand bei Feldtests 11 von 12 Kameras**, funktioniert aber nur über WLAN auf 2,4 GHz.
- **Ein offenes Issue beschreibt ein neues SSID-Format, einen bestätigten 5-GHz-Hotspot und lokal verwaltete MAC-Adressen**, die die aktuelle, auf 2,4 GHz beschränkte OUI-Methode nicht erfasst.
- **Ein anderer Ansatz ohne WLAN entsteht**: Eine ESP32-Kamera ohne IR-Cut-Filter erkennt Infrarotlicht und ist von den beschriebenen drahtlosen Umgehungsmethoden unabhängig.
- **Eine Sichtprüfung bestätigt die Funkstille**: Eine Kamera war nachts eingeschaltet und beleuchtete ihre Umgebung, doch WLAN-Methoden meldeten null gültige Treffer. Bei diesem Gerät erklärt eine Entfernung die Stille nicht.
- **Null Treffer bei einer bekannten Kamera bedeuten nicht sofort, dass deine Hardware kaputt ist.** Aktualisiere zuerst die Firmware und prüfe danach, ob die Kamera noch steht.
- **Das Open-Source-Projekt veröffentlicht Korrekturen, sobald die Community Lücken findet.** Prüfe GitHub-Issues neben der README auf den aktuellen Stand.

### Nächste Schritte

1. **Aktualisiere zuerst die Firmware** auf den aktuellen `main`-Branch: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Lies den vollständigen Hardwareleitfaden**, falls du ihn noch nicht kennst: **[Flock-You-Erkennungsprojekt: Hardwareleitfaden zur Gegenüberwachung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Vergleiche mögliche Funklöcher** mit **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)**, bevor du annimmst, dass dein Gerät etwas übersehen hat.
4. **Informiere dich über das System**: **[Flock-Safety-Kameraüberwachung: Verbreitung, Datenschutzbedenken und Schutzstrategien](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Kombiniere WLAN-Erkennung mit Mobilfunkerkennung** über **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)**. Keines der Verfahren in diesem Artikel erkennt IMSI-Catcher.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  FlockYou-Geräte einsatzbereit kaufen, 20 % sparen
{{< /centerbutton >}}

______

## Verwandte Artikel

| Artikel | Inhalt |
|---------|---------------|
| **[Flock-You-Erkennungsprojekt: Hardwareleitfaden zur Gegenüberwachung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Technischer Leitfaden zu drei Hardwareplattformen, Firmware-Einrichtung und Erkennungsmethode |
| **[Flock Finder: vermutete Flock-Kameras in deiner Nähe kartieren](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Abgleich einer möglichen Funklücke mit mehr als 40.000 erfassten Kamerastandorten |
| **[Flock-Kameras: Werkzeug für die öffentliche Sicherheit oder Überwachung ohne Durchsuchungsbeschluss?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Analyse der Flock-Datenbank und warum die Frage nach Durchsuchungsbeschlüssen wichtiger ist als die Erkennung |
| **[Flock-Safety-Kameraüberwachung: Verbreitung, Datenschutzbedenken und Schutzstrategien](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Verbreitung, dokumentierte Missbrauchsfälle und Ressourcen für gemeinschaftliches Engagement |
| **[Schwachstellen in Flock-Safety-Kameras: mehr als 50 Fehler gefunden](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Sicherheitsforschung zu Hardware und Software, getrennt von der Frage der drahtlosen Erkennung |
| **[Rayhunter-Geräte flashen: vollständige Anleitung](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | IMSI-Catcher und Stingrays erkennen, das Mobilfunk-Pendant zur hier beschriebenen WLAN-Lücke |

______

## Quellen

1. [Flock-You-GitHub-Repository - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub-Issue #20 - Flock-Kameras werden nicht erkannt, andere Geräte jedoch schon](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub-Issue #43 - 5-GHz-Signal? Neue OUI / MAC-Adressfilterung](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [NitekryDPaul-OUI-Forschungsdatensatz](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - ALPR-Forschung der Community](https://deflockjoplin.today)
7. [Pintor, L. & Atzori, L. (2022) - Analyse von Wi-Fi-Probe-Anfragen für das Fingerprinting von Information Elements, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED und 404 Media - Hacker drangen in eine Flock-Kamera ein](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - Flock-Kameras weisen zahlreiche Schwachstellen und fest einprogrammierte Zugangsdaten auf](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - Dateisystemabbilder einer Flock-ALPR-Kamera](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - Diese Woche in der Sicherheit: Flock-Kameras sind alt, Microsoft-Patches und SSH-Forschung](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - Flock-Safety-ALPR-Erkennung und Geräteübersicht](https://wifimothership.com/flock)
13. [GainSec - Firmware-Forschung und Sicherheitsmeldungen](https://gainsec.com/)
14. [The Hunt for the Hidden Probe - Verhalten verborgener SSID-Wildcard-Probes](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
15. [DeFlock - Crowdsourcing-Karte für ALPR-Kameras](https://deflock.org/)
16. [Colonel Panic Tech - OUI-SPY und Erkennungshardware](https://colonelpanic.tech)
17. [STS Collective - FlockYou-Geräte](https://stscollective.com/discount/SIMEONONSECURITY)
18. [Mit Flock-Kameras geschieht etwas Seltsames - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
19. [Infrarot-Wardriving für Flock-Kameras - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
20. [Flock-Kameras noch aktiv, aber ohne Funkübertragung - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
21. [Automatische Kennzeichenerkennung - Wikipedia (Infrarotbeleuchtung bei ANPR/ALPR-Systemen)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
22. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
23. [L76K-GNSS-Modul für Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)
