---
title: "Wir kartierten 146.526 „Flock-Kameras“. 50.278 waren ClickShare-Systeme"
date: 2026-09-21
lastmod: 2026-11-14
toc: true
draft: false
description: "Ein Audit von Flock Finder zeigt ClickShare und weitere Fehlalarme, erläutert die Belege und dokumentiert die Änderungen."
genre: ["Sicherheitsforschung", "Datenschutztechnologie", "Open-Source-Projekte", "Datenjournalismus", "Gegenüberwachung"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "OUI-Fingerprinting", "WiGLE", "Fehlalarme", "Datenqualität", "Barco ClickShare", "MAC-Adresse", "IEEE-OUI", "Fingerprinting von Informationselementen", "ESP32", "Flock-You", "NitekryDPaul", "DeFlockJoplin", "Open-Source-Rechenschaft", "Überwachungskartierung", "WiFi", "Probe Request", "MAC-Randomisierung"]
cover: "/img/cover/flock-finder-oui-false-positive-audit-2026.webp"
coverAlt: "Eine dunkle Stadtkarte voller roter Markierungen, die sich als Büro-WiFi-Geräte herausstellen, während wenige grüne Markierungen stärkere Erkennungen darstellen"
coverCaption: "Ein Audit von 146.526 Flock-Finder-Datensätzen zeigte, wie eine nützliche Feldbeobachtung zu einer übertrieben sicheren Kartenbehauptung wurde."
canonical: "https://simeononsecurity.com/articles/flock-finder-oui-false-positive-audit-2026/"
---

**Wir setzten 146.526 Punkte auf eine Karte von Überwachungskameras. Mindestens 50.278 davon waren Barco-ClickShare-Präsentationssysteme. Konferenzraumtechnik machte mehr als ein Drittel dessen aus, was unsere Überschrift „Kartierte Kameras“ nannte.**

Das war unser Projekt, unsere Datenpipeline und unser Fehler. Flock Finder fragte WiGLE täglich nach MAC-Adresspräfixen ab, die auf Flock-Safety-Kameras beobachtet worden waren, veröffentlichte Ergebnisse mit voller Koordinatengenauigkeit und stellte sie als gleichartige Markierungen dar. In den Metadaten stand zwar `suspected`, und die Dokumentation erwähnte Fehlalarme. Karte und Überschrift vermittelten dennoch Gewissheit.

**Ergebnis für Leser:** Prüfe das Audit nach, trenne Beobachtung von Zuordnung und zeige die Sicherheit direkt an Kartenmarkierung und Überschrift. Ein Präfixtreffer ist ein Ansatz für weitere Prüfung, kein Kamerabeweis.

Als wir endlich ein Häufigkeitshistogramm der SSID-Spalte erstellten, erklärte der Datensatz den Fehler binnen Minuten. ClickShare war nur die größte Kategorie. Weitere 6.099 Datensätze nannten sich `SMARTGATE_*`, 3.801 begannen mit dem allgemeinen WiFi-Direct-Präfix `DIRECT-`, 314 trugen exakt den Namen `AndroidAP`, 138 lauteten `Audi HUD`, 133 `MAX-PRINTER`, und 30 enthielten die Urteilszeichenfolge eines anderen Detektors. Insgesamt **entsprachen 60.793 Zeilen oder 41,5 % den bekannten Namensregeln für andere Geräte des ursprünglichen Audits.**

Flock Finder veröffentlicht inzwischen Evidenzklassen je Datensatz, schließt bekannte Fremdgeräte standardmäßig aus Karte und Überschrift aus, stellt Filter bereit, markiert Datensätze außerhalb des Hauptmarkts und trennt hochsichere Präfixe von Präfixen von Auftragsfertigern. Dieser Artikel beschreibt den Fehler, die Belege und die verbleibenden Grenzen.

______

## So funktioniert die Community-Erkennung von ALPR

Community-Entwicklungen für Flock-Detektoren kombinieren meist drei Arten drahtloser Belege:

1. **WiFi-MAC/OUI-Präfixe.** Die ersten Bytes einer global verwalteten MAC-Adresse können die Organisation identifizieren, der der Adressblock zugeteilt wurde.
2. **WiFi-Verhalten.** Eine SSID, eine Wildcard-Probe-Request, die Empfängeradresse, das Kanalverhalten oder eine Folge von 802.11-Informationselementen kann die Geräteklasse eingrenzen.
3. **Bluetooth-Belege.** Hersteller-IDs und Service-UUIDs können Funkmodule eines Produkts oder einer Firmwaregeneration identifizieren.

OUI-Abgleich wurde verbreitet, weil er günstig und passiv ist. Ein preiswerter ESP32 kann nahe 802.11-Frames untersuchen, ohne sich mit einem Netzwerk zu verbinden. Eine historische Datenbank wie [WiGLE](https://wigle.net/) erlaubt außerdem die Suche in früheren Beobachtungen ohne eigene Scanner.

Die Methode entstand in einer Community-Linie: Kartierung und lokale Arbeit von [DeFlock](https://deflock.org/), [colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you), Forks und Begleitprojekte wie unser [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32) und schließlich [Flock Finder](https://github.com/simeononsecurity/flock-finder), das die Präfixliste weltweit auf WiGLE-Daten anwandte.

Die ursprüngliche Feldarbeit verdient klare Anerkennung. [@NitekryDPaul](https://github.com/NitekryDPaul) beobachtete 30 Präfixe an echter Flock-Ausrüstung durch Forschung im Promiscuous Mode. [DeFlockJoplin](https://github.com/DeflockJoplin/flock-you) steuerte bei Feldtests ein weiteres bei. Diese Beobachtungen waren legitim. Unser Folgefehler war, **„an einer Flock-Kamera beobachtet“ so zu behandeln, als bedeute es „nur bei Flock-Kameras vorhanden“.**

______

## Der strukturelle Fehler: Eine OUI beschreibt die Lieferkette

IEEE beschreibt eine OUI als 24-Bit-Kennung, die einem Anbieter, Hersteller oder einer anderen Organisation zugeteilt wird. Zusammen mit weiteren 24 Bits, die der Empfänger auswählt, bildet sie eine MAC-Adresse. Die [IEEE Registration Authority](https://standards.ieee.org/products-programs/regauth/) veröffentlicht das Register.

Das zeigt, wer einen Adressblock erhalten hat. Es zeigt nicht zwingend die Marke eines fertigen Produkts. Auftragsfertiger bauen Funkmodule für viele Kunden. Ein Chipanbieter kann deshalb in Kameras, Projektoren, Druckern, Fahrzeugen und Bastlerplatinen auftauchen.

Die Registerzuweisungen hinter unserer Liste machten das Risiko sichtbar:

| Registrant | Präfixe in der geprüften Liste |
|---|---|
| Liteon Technology | `74:4C:A1`, `F4:6A:DD`, `9C:2F:9D`, `C0:35:32`, `E4:AA:EA`, `14:5A:FC` und weitere |
| Universal Global Scientific Industrial (USI) | `E0:4F:43`, `08:3A:88` |
| Espressif | `A4:CF:12`, `3C:71:BF` |
| Silicon Laboratories | `58:8E:81`, `90:35:EA`, `EC:1B:BD` |
| Flock Safety | `B4:1E:52` |

Die Espressif-Einträge hätten uns warnen müssen. Zwei Präfixe in einer vermeintlichen Kameraliste gehörten dem Hersteller einer der weltweit häufigsten eingebetteten WiFi-Plattformen, einschließlich des Chips, den viele Community-Detektoren verwenden.

`B4:1E:52` ist anders, da es direkt auf Flock Safety registriert ist. Das Präfix wurde beim geprüften Commit zur Liste mit 38 Präfixen hinzugefügt, **aber noch nicht abgefragt**: `scan_stats.json` meldete 31 abgefragte Präfixe. Gleiches galt für sechs neu hinzugefügte Batteriepack-Präfixe. Der Snapshot belegt daher nicht, wie häufig oder selten Flocks eigenes Präfix ist. Wir machen aus „nicht abgefragt“ keine „null Treffer“.

Das aktuelle Repository enthält nach Ergänzung von `E0:0A:F6` zum Abgleich mit der Detektor-Firmware 39 Präfixe. Die gespeicherte Scan-Zusammenfassung enthält weiterhin Daten für 31 Präfixe. Die neuen Einträge warten also noch auf eine vollständige Neuberechnung und sind keine nachgewiesenen Null-Treffer.

______

## Der Datensatz prüfte sich selbst

Alle historischen Audit-Zahlen unten wurden aus `data/flock_cameras.csv` im Flock-Finder-Commit [`5551829`](https://github.com/simeononsecurity/flock-finder/tree/5551829) mit `csv` und `collections.Counter` aus Pythons Standardbibliothek neu erzeugt. Ein neuer Fahrtest war nicht nötig. Namen, Geografie und Präfixzusammensetzung widersprachen der Überschrift bereits. Angaben zur korrigierten Implementierung stammen aus der im aktuellen Repository gespeicherten Zusammenfassung `scan_stats.json`.

### Geografie war ein frühes Warnsignal

Von 146.526 Zeilen lagen 75.818 in den Vereinigten Staaten, 70.674 außerhalb und bei 34 fehlte das Land. Deutschland führte mit 13.491 Datensätzen, gefolgt von Kanada mit 6.251, Frankreich mit 5.839, Großbritannien mit 4.836, den Niederlanden mit 4.636 und der Schweiz mit 4.515.

{{< figure src="flock-finder-us-non-us-split.webp" alt="Gestapelter Balken mit 75.818 US-Datensätzen, 70.674 Datensätzen außerhalb der USA und 34 Datensätzen ohne Länderwert" caption="Das Länderhistogramm ergibt 146.492, weil 34 Zeilen ein Null-Land enthalten." >}}

Geografie ist ein Prüfsignal, kein Beweis. Flock beschreibt sein Netz als „landesweit“ und sagt, es verbinde Kunden in [49 US-Bundesstaaten](https://www.flocksafety.com/flock-ecosystem). Internationale Expansion kann die Marktgrenze ebenfalls verändern. Wir markieren Datensätze außerhalb des Markts deshalb zur Prüfung, statt sie zu löschen oder alle Nicht-US-Datensätze für falsch zu erklären.

Die vorsichtige Schlussfolgerung reicht aus: Fast die Hälfte der Datensätze lag außerhalb des primären US-Markts des Projekts. Ein weltweiter OUI-Treffer war ohne weiteres Signal daher nicht gleich plausibel.

### Über 60.000 Geräte nannten sich selbst

| SSID-Familie im ursprünglichen Audit | Datensätze | Anteil | Aussage des Namens |
|---|---:|---:|---|
| Enthält `ClickShare` | 50.278 | 34,3 % | Kabellose Barco-Präsentationstechnik |
| `SMARTGATE_*` | 6.099 | 4,2 % | Gerätefamilie für Gateways oder OBD-Systeme |
| `DIRECT-*` | 3.801 | 2,6 % | WiFi-Direct-Geräte wie Drucker, Fernseher und Adapter |
| Exakter Name `AndroidAP` | 314 | 0,2 % | Android-Hotspots |
| Exakter Name `Audi HUD` | 138 | 0,1 % | Audi-Infotainment- oder Head-up-Display-WiFi |
| Exakter Name `MAX-PRINTER` | 133 | 0,1 % | Bürodrucker |
| `Flock ALPR [...]` | 30 | <0,1 % | Urteil eines anderen Detektors als SSID |
| **Kombiniert, ursprüngliches Audit** | **60.793** | **41,5 %** | Als andere Hardware oder Detektorausgabe erkennbar |

Barcos Support-Dokumentation nennt für eine ClickShare-Basiseinheit den Standardnetzwerknamen [`ClickShare-<serial base number>`](https://www.barco.com/en/support/knowledge-base/2675-how-to-connect-to-your-clickshare-base-unit-wifi). Das bestätigt die Produktfamilie aus erster Hand, ohne Rückschlüsse aus Geografie oder Anbieterregister.

Der Produktionsklassifikator hat diese exakten Namensprüfungen inzwischen durch reguläre Ausdrücke ohne Beachtung der Groß-/Kleinschreibung ersetzt. Er berücksichtigt ClickShare, SmartGate, WiFi Direct, AndroidAP, Audi HUD, MAX-PRINTER und Detektorausgaben. Bei denselben 146.526 Zeilen findet er 629 AndroidAP-, 139 Audi-HUD- und 134 MAX-PRINTER-Varianten. Das aktuelle Repository meldet daher **61.110 `identified_other`-Datensätze**, etwas mehr als die 60.793 des ursprünglichen Audits.

### Das bestätigende Signal lag bei nur 2,4 %

Nur **3.502 Zeilen** trugen eine echte Flock-Muster-SSID. Weitere 24.964 hatten keine SSID. Die übrigen Datensätze bezeichneten entweder andere Hardware oder beruhten auf einer OUI mit nicht klassifiziertem Namen.

Die 3.502 bestätigten Zeilen enthielten 161 echte SSID-Varianten: 3.342 Fälle des einfachen Namens `Flock`, 157 einmalige Bereitstellungsnamen `Flock-XXXXXX` oder `FLOCK-XXXXXX` und drei weitere Namen mit `flock`. Eine frühere README-Zahl von 166 Varianten enthielt fünf verschiedene Detektor-Anmerkungen `Flock ALPR [...]`. Sie belegen den Detektor, nicht die Kamera.

{{< figure src="flock-finder-evidence-class-breakdown.webp" alt="100-Prozent-Balken mit 146.526 Datensätzen: 3.502 per SSID bestätigt, 57.267 benannt und nicht klassifiziert, 24.964 nur verborgene OUI, 60.763 als andere identifiziert und 30 Detektor-Rückkopplungen" caption="Die alte Überschrift fasste fünf wesentlich unterschiedliche Evidenzklassen in einer Zahl zusammen." >}}

### Die Qualität der Präfixe unterschied sich stark

Die Fehlalarmrate war nicht einheitlich. Einige Präfixe behielten ein nützliches Flock-Signal. Andere bestanden überwiegend aus benannten Büro- oder Verbrauchergeräten.

{{< figure src="flock-finder-per-oui-composition.webp" alt="Horizontale gestapelte Balken für 31 OUI-Präfixe: Flock-SSIDs grün, bekannte fremde SSIDs rot, verborgene SSIDs hellgrau und nicht klassifizierte Datensätze dunkelgrau" caption="Die größten Präfixe enthielten oft die meisten bekannten Fremdgeräte. Zahlen aus dem Audit-Snapshot mit 146.526 Zeilen." >}}

Betrachte zwei Präfixe, die die alte Karte gleich bezeichnete:

- `70:C9:4E` hatte 495 Zeilen: 133 Namen mit Flock-Muster und 29 bekannte Fremdnamen.
- `74:4C:A1` hatte 11.872 Zeilen: 211 Namen mit Flock-Muster und 8.385 bekannte Fremdnamen.

{{< figure src="flock-finder-prefix-signal-contrast.webp" alt="Vergleich: Präfix 70 C9 4E mit 26,9 Prozent Flock-SSIDs und 5,9 Prozent bekannten Fremden gegenüber 74 4C A1 mit 1,8 Prozent Flock-SSIDs und 70,6 Prozent bekannten Fremden" caption="Ein einheitliches Label verdeckte gegensätzliche Signal-Rausch-Verhältnisse." >}}

Dasselbe Muster zeigte sich bei den größten Gruppen: `F4:6A:DD` hatte 8.422 bekannte Fremdnamen gegenüber 327 Flock-Namen, `D0:39:57` hatte 8.270 gegenüber 473, und `E0:4F:43` enthielt 6.238 bekannte Fremdnamen gegenüber 66 Flock-Namen. Die Präfixmenge war kein Qualitätsbeleg.

______

## Die Rückkopplungsschleife in 30 Zeilen

Dreißig Datensätze aus Texas hatten SSIDs, die eindeutig die Ausgabe eines anderen Detektors waren:

| Als SSID gespeichertes Detektorlabel | Von diesem Tool angegebene Sicherheit | Datensätze |
|---|---:|---:|
| `Flock ALPR [wifi_receiver_oui;low]` | niedrig | 20 |
| `Flock ALPR [wifi_oui_wildcard_probe;medium]` | mittel | 4 |
| `Flock ALPR [wifi_bssid_oui;low]` | niedrig | 3 |
| `Flock ALPR [flock_receiver_oui;low]` | niedrig | 2 |
| `Flock ALPR [wifi_hidden_ssid_oui;low]` | niedrig | 1 |

Das erzeugende Tool stufte 26 der 30 Fälle als wenig sicher ein. Ein WiGLE-Upload speicherte das Urteil des Tools anschließend im SSID-Feld. Unsere Pipeline fand das Wort `Flock` und hätte dieses Label als unabhängige Bestätigung behandeln können.

Dreißig Zeilen sind statistisch wenig. Der Mechanismus ist bedeutsam: Tools mit gemeinsamer Crowdsourcing-Datenbank können die Ausgaben voneinander übernehmen und so eine Vermutung mit geringer Sicherheit in scheinbare Bestätigung verwandeln. Die Korrektur schließt das gesamte Muster `Flock ALPR [` aus, bevor nach der bestätigenden Teilzeichenfolge `flock` gesucht wird.

______

## Was wir falsch gemacht haben

Die README-Überschrift lautete **„Kartierte Kameras | 146.526“**. Die Karte veröffentlichte Koordinaten mit voller Genauigkeit und zeichnete jedes Ergebnis als dieselbe Art Markierung. Sie wurde nach einem GitHub-Actions-Zeitplan aktualisiert, wodurch eine schwache Heuristik wie ein gepflegtes Inventar wirkte.

Wir hatten Einschränkungen genannt. Jedes Merkmal trug `match_confidence: "suspected"`. Die README erwähnte ClickShare als mögliches weiteres Gerät, und das Projekt führte einen separaten Kandidatenpfad für SSID-Funde. Diese Hinweise bestimmten jedoch weder die Zahl noch die Markierung oder die Standardansicht, die Leser tatsächlich sahen.

Im Text relativierten wir, in der Überschrift bezifferten wir. Die Karte stellte die Behauptung auf.

Am vermeidbarsten war, dass unsere [flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)-Firmware bereits hochsichere Kennungen von Kennungen für Auftragsfertiger trennte und schwache Belege unterhalb der Alarmschwelle bewertete. Das Konzept existierte in derselben Organisation, aber die Kartenpipeline übernahm es nicht.

Wir fanden das Ausmaß des Fehlers mit einem Histogramm unserer eigenen SSID-Spalte. Das dauerte Minuten. Jeden Tag hatten wir 146.526 Belegzeilen gegen unsere Darstellung veröffentlicht.

______

## Was wir geändert haben

Die Korrektur steckt im Datenmodell und in der Oberfläche von Flock Finder:

- **Evidenz je Datensatz:** `ssid_confirmed`, `oui_high`, `oui_mfr` oder `identified_other`.
- **OUI-Stufen:** Präfixe sind in im Feld beobachtete hohe Sicherheit und gemeinsam genutzte Auftragsfertiger-Stufen getrennt.
- **Ausschluss bekannter Fremdgeräte:** ClickShare, SmartGate, WiFi Direct, Android-Hotspots, Audi HUD, MAX-PRINTER und Detektor-SSID-Ausgaben sind standardmäßig von Karte und Überschrift ausgeschlossen.
- **Sichtbare Unsicherheit:** Markierungsfarben, Pop-ups, Zahlen und Filter zeigen die Evidenzklasse.
- **Marktkennzeichnung:** Datensätze außerhalb des primären US-Markts erhalten `out_of_market: true` und bleiben zur Prüfung verfügbar.
- **Aufgeschlüsselte Überschrift:** 3.502 per SSID bestätigt, 73.691 verdächtige OUI-Treffer hoher Stufe, 8.223 verdächtige OUI-Treffer von Auftragsfertigern und 61.110 als andere identifiziert.

Die korrigierte, handlungsrelevante Zahl lautet **85.416**. Darin sind weiterhin 81.914 unbestätigte OUI-Treffer enthalten. Es ist eine nachvollziehbare Abrechnung dessen, was die aktuellen Regeln erfüllt, kein verifiziertes Kamerainventar.

`identified_other` ist ebenfalls ein operativer Klassifikator, kein Orakel. Für die Standard-SSID von ClickShare gibt es starke Primärdokumentation. Ein breites Muster wie `DIRECT-` beschreibt dagegen eine WiFi-Direct-Namenskonvention vieler Produktklassen. Die veröffentlichte Trefferregel und das Feld `blocked_reason` erlauben Forschern, diese Ausschlüsse zu prüfen und bei besseren Belegen anzupassen.

### Langfristig hilft Firmware-Fingerprinting

OUI-Stufen begrenzen den Schaden, machen ein gemeinsam genutztes Herstellerpräfix aber nicht produktspezifisch. Besser ist die geordnete Struktur der Informationselemente in 802.11-Probe-Requests. Frühere Arbeit dokumentiert diese TLV-Signatur:

```text
2,12,127,221:506f9a16030103,45,191,221:0050f208000000
```

Diese Folge beschreibt das Verhalten eines bestimmten Firmware-Stacks statt den Besitzer eines MAC-Blocks. Probe-Request-Fingerprinting ist eine etablierte Methode zur Geräteerkennung. [Veröffentlichte Forschung zu 802.11-MAC-Layer-Fingerprinting](https://doi.org/10.1155/2017/6235484) zeigt, dass Informationselemente von Probe-Requests Geräte auch dann identifizieren können, wenn MAC-Adressen rotieren. Die Methode passt außerdem zum konkreten Fehler aus [flock-you Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43): `Flock Camera net.` erscheint auf aufeinanderfolgenden lokal verwalteten MAC-Adressen im 2,4- und 5-GHz-Band.

Die Signatur braucht weiterhin unabhängige Feldvalidierung über Geräte und Firmwareversionen hinweg. Fehlerhafte Mitschnitte müssen defensiv verarbeitet werden. Dennoch ist dies die richtige Richtung. MAC-Randomisierung macht reinen OUI-Abgleich zu einer absehbaren Sackgasse.

______

## Warum das über ein Repository hinaus wichtig ist

Menschen nutzen Überwachungskarten, um Fahrten, Parkplätze, Meldungen, Forschung und Organisation zu planen. Ein falscher Marker lenkt Aufmerksamkeit um. Zehntausende falsche Marker können danebenliegende korrekte Beobachtungen unglaubwürdig machen.

Hinzu kommt eine Glaubwürdigkeitsasymmetrie. Ein Anbieter oder Kritiker braucht einen nachweislich falschen ClickShare-Marker, um den gesamten Datensatz anzuzweifeln. Wir lieferten 50.278. Journalisten und Interessenverbände können eine klare Überschrift schneller wiederholen, als eine spätere Korrektur sie einholt.

Open-Source-Transparenz verdient Vertrauen durch prüfbare Methoden und sichtbare Unsicherheit. Die Rohdaten halfen, unseren Fehler aufzudecken. Der Zugriff auf Rohdaten entschuldigte jedoch keine Oberfläche, die zu viel behauptete. Die Korrektur gehört überall dorthin, wo Leser die Aussage sehen: in Felder, Filter, Markierungen, Legende und Überschrift.

### Ein Aufruf an alle Flock- und ALPR-Karten

Andere Flock- und ALPR-Kartenprojekte sollten ihre Datensätze ebenfalls prüfen. Dies ist eine Einladung zum Methodenvergleich, kein Vorwurf, dass jede Karte unseren Fehler übernommen hat.

[WiGLE](https://www.wigle.net/stats/) ist der breiteste öffentlich zugängliche, weltweit durchsuchbare WiFi-Beobachtungsdatensatz, den wir kennen. Genau diese Reichweite machte Flock Finder attraktiv: Eine API konnte eine im Feld erforschte Signaturliste in eine Weltkarte verwandeln. Sie machte den Fehler auch messbar groß. Eine globale Datenbank liefert jedes fremde Produkt im Adressraum eines gemeinsamen Funkzulieferers, nicht nur das Produkt, das die Suche auslöste.

Andere Karten verwenden andere Belege. Einige stützen sich auf Fotos und Beobachtungen von Freiwilligen. Andere importieren Überwachungs-Tags von OpenStreetMap, öffentliche Unterlagen, Anbieterangaben oder Daten eines anderen Community-Projekts. Ihre Summen sind nicht direkt mit unseren WiGLE-Ergebnissen vergleichbar. Unsere Quote von 2,4 % SSID-Bestätigungen darf nicht auf feldverifizierte Daten übertragen werden. Das gemeinsame Risiko: Die Klassifizierung eines Projekts fließt in Quelldaten eines anderen ein und erscheint anschließend als unabhängige Bestätigung.

Jede öffentliche Karte sollte ein kurzes Audit beantworten können:

1. **Was bedeutet eine Markierung?** Ein fotografiertes Gerät, ein Behördeneintrag, ein OUI-Treffer, eine Nutzermeldung oder ein Import aus einer anderen Karte?
2. **Wie viele Datensätze haben direkte Produktbelege?** Veröffentliche Zahlen nach Evidenzklasse statt einer aggregierten Kamerazahl.
3. **Welche Quellen sind unabhängig?** Verfolge die Herkunft von Importen, damit dieselbe Beobachtung nicht als mehrere Bestätigungen zählt.
4. **Was widerspricht der Klassifizierung?** Erstelle Häufigkeitstabellen für SSIDs, Anbieter, Länder, Beitragenden-Labels und weitere kategoriale Felder.
5. **Wie werden Unsicherheit und Streitfälle angezeigt?** Zeige Sicherheit und Korrekturstatus in Markierungen, Filtern, Exporten und Überschriften.
6. **Kann ein anderer Forscher die Zahl reproduzieren?** Veröffentliche Abfrage, Quell-Snapshot, Klassifizierungsregeln und Datum.

Dieses Audit macht das Flock-Problem nicht kleiner. Ein ALPR-Kameranetz kann weiterhin Wege aufzeichnen, Suchen über Zuständigkeitsgrenzen hinweg ermöglichen und Menschen betreffen, die der Erfassung nie zugestimmt haben. Präzise Zahlen machen diese Kritik schwerer abzuweisen. Wenn wir Überwachungssysteme kritisieren, müssen unsere Karten Beobachtetes, Abgeleitetes und Bestätigtes unterscheiden.

Wir machten einen gut informierten Fehler. Die Präfixe stammten aus legitimer Feldforschung, die Pipeline war reproduzierbar und die Hinweise waren echt. Die Schlussfolgerung ging trotzdem über die Belege hinaus. Gute Absichten und gute Eingabedaten heben die Pflicht nicht auf, die Ergebnisse eines Systems im großen Maßstab zu prüfen.

______

## Das Audit nachstellen

Wechsle zum Commit `5551829` und führe Folgendes im Repository-Stamm aus. Es verwendet nur Pythons Standardbibliothek und gibt Gesamtzahl, Geografie, häufige SSIDs und ausgewählte benannte Gerätefamilien aus.

```bash
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder
git checkout 5551829

python3 - <<'PY'
import csv
from collections import Counter

with open("data/flock_cameras.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

ssids = Counter((row["ssid"] or "").strip() for row in rows)
countries = Counter((row["country"] or "").strip() for row in rows)

families = {
    "clickshare": lambda s: "clickshare" in s.lower(),
    "smartgate": lambda s: s.lower().startswith("smartgate_"),
    "direct": lambda s: s.lower().startswith("direct-"),
    "androidap": lambda s: s.lower().startswith("androidap"),
    "detector_output": lambda s: s.lower().startswith("flock alpr ["),
}

print("Zeilen", len(rows))
print("USA", countries["US"])
print("außerhalb der USA", sum(countries.values()) - countries["US"] - countries[""])
print("Land fehlt", countries[""])
print("häufigste SSIDs", ssids.most_common(20))
for name, matches in families.items():
    print(name, sum(matches(ssid) for ssid in ssids.elements()))
PY
```

Für die exakte historische Eingabe verwende die CSV aus diesem Commit, nicht einen aktuellen generierten Datensatz. Das Projekt nimmt die große CSV, GeoJSON-Datei und OUI-Dateien seit dem Audit nicht mehr in Git auf, weil jeder Scan Hunderte Megabyte neu schrieb und das Repository stark wachsen ließ. Aktuelle generierte Daten werden aus der laufenden [`data-latest`-Version](https://github.com/simeononsecurity/flock-finder/releases/tag/data-latest) wiederhergestellt und dort veröffentlicht. Die kleine Zusammenfassung `scan_stats.json` bleibt in Git. Eine fehlende generierte Datei im aktuellen Branch bedeutet daher weder, dass historische Belege gelöscht wurden, noch dass ihre Anzahl null ist.

______

## Die Lehre

**Eine Heuristik, die in Metadaten als „vermutet“ markiert, auf der Karte aber als sicherer Marker dargestellt wird, ist eine Behauptung.** Die Kennzeichnung gehört ins Datenmodell und in die Visualisierung, nicht nur in die Dokumentation.

