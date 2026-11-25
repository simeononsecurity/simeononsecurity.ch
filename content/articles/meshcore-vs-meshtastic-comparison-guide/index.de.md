---
title: "MeshCore oder Meshtastic: Vergleich"
date: 2026-06-26
lastmod: 2026-11-25
toc: true
draft: false
description: "Vergleich von MeshCore und Meshtastic nach Routing, Reichweite, Sendezeit, Infrastruktur, Geräteunterstützung und geeignetem Einsatz."
genre: ["LoRa", "Mesh-Netzwerke", "Offline-Kommunikation", "Notfallkommunikation", "Taktische Kommunikation", "Amateurfunk", "Quelloffene Software", "Katastrophenvorsorge", "Drahtlosnetzwerke", "Datenschutz"]
tags: ["MeshCore vs. Meshtastic", "Meshtastic", "MeshCore", "LoRa-Mesh-Netzwerk", "Offline-Kommunikation", "Meshtastic-Vergleich", "MeshCore-Vergleich", "LoRa-Funk", "Mesh-Netzwerke", "Notfallkommunikation", "taktisches Mesh", "Offline-Funk", "Meshtastic-Protokoll", "MeshCore-Protokoll", "LoRa Meshtastic", "Katastrophenkommunikation", "Mesh-Funk", "Speichern und Weiterleiten", "LoRa-Flooding", "LoRa-Mesh", "T-Beam Meshtastic", "Heltec LoRa", "RAK WisBlock", "Offline-Nachrichten", "Mesh-Netzwerkprotokoll", "Meshtastic 2.6", "LoRa-Sendezeit", "Notfallfunk"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Illustration zweier LoRa-Mesh-Netzwerke: links Meshtastic mit Flooding zwischen Knoten, rechts MeshCore mit strukturiertem Routing, vor dunklem Hintergrund."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## Die kurze Antwort

Meshtastic und MeshCore laufen auf derselben günstigen LoRa-Hardware. Beide ermöglichen verschlüsselte Nachrichten ohne Mobilfunk oder Internet. **Die Protokolle sind nicht miteinander kompatibel.**

**Beide Protokolle fluten Gruppenverkehr.** Normale Meshtastic-Clients unterdrücken redundante Weitersendungen. Bei MeshCore leiten nur Infrastrukturknoten weiter. Beide können gelernte Routen für Direktnachrichten nutzen.

*Meshtastic eignet sich für die meisten.* Die Mobil-App ist ausgereift, die Community groß, die Dokumentation gut und die Einrichtung dauert weniger als 20 Minuten.

**Grundlagen der Funktechnik sind wichtiger als die Firmware.** Kein Protokoll gleicht eine schlecht platzierte Antenne aus.

______

## Was die Systeme leisten

### Meshtastic

**Meshtastic** ist ein Open-Source-Projekt, das Kevin Hester 2020 startete. Die Firmware macht aus handelsüblicher LoRa-Hardware ein Textnachrichten-Mesh ohne Abhängigkeit von Internet oder Mobilfunk.

Die Firmware läuft auf LoRa-Hardware, die viele Nutzer bereits besitzen oder günstig kaufen. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock und Seeed SenseCAP Indicator** unterstützen Meshtastic ohne Spezialwerkzeuge. Die iOS- und Android-Apps werden gut gepflegt. Nichttechnische Nutzer sind in weniger als zehn Minuten im Netz. Das Ökosystem bietet MQTT-Bridges, Home-Assistant-Integration und ATAK-Erweiterungen.

### MeshCore

**MeshCore** gewann 2023 und 2024 an Bedeutung. Die Firmware läuft auf einem großen Teil derselben LoRa-Hardware, verwendet aber eine **hybride Routing-Architektur**. Das ist kein Store-and-Forward im Sinn verzögerungstoleranter Netzwerke.

Repeater übernehmen den Großteil der Weiterleitung. **Raumserver sind optional.** Sie speichern Gruppennachrichten, damit Clients sie nach einer erneuten Verbindung abrufen. Clients verwenden ein LoRa-Begleitfunkgerät und verbinden sich bei vorhandener Infrastruktur darüber. Ohne Repeater kommunizieren sie direkt mit Knoten in Reichweite.

______

## Der wichtigste technische Unterschied

### Meshtastic-Routing

Beim **[gesteuerten Fluten](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** in Meshtastic bricht ein normaler Client eine geplante Weitersendung ab, wenn er dasselbe Paket zuvor von einem anderen Knoten hört. `ROUTER` und `ROUTER_LATE` können es trotzdem weiterleiten. Bei `CLIENT_BASE` gilt diese Ausnahme für Verkehr zu oder von Favoriten.

Seit Meshtastic 2.6 nutzen **Direktnachrichten** zunächst Fluten zur Pfadsuche und versuchen danach die Weiterleitung über den gelernten nächsten Knoten. Wenn das scheitert, können sie erneut fluten.

**Die eigentliche Grenze ist die Sendezeit, nicht die Knotenzahl.** LoRa nutzt gemeinsam belegte ISM-Bänder mit regionalen Grenzen für den Duty Cycle, in Europa typischerweise 1 %. Ein Netz mit häufigen GPS-Beacons, Telemetrie und aktivem Kanalverkehr erschöpft die Sendezeit, bevor ein absolutes Knotenlimit erreicht ist. Zehn aktive Knoten mit häufiger Telemetrie verursachen mehr Konkurrenz als fünfzig ruhige Sensoren. Dichte Netze mit mehreren Dutzend aktiven Nutzern haben oft mehr Sendezeitkonkurrenz, aber es gibt keine feste Obergrenze. Der Schwellenwert hängt von Spreizfaktor, Sendezeit-Preset, Telemetrieintervallen, Gelände und Repeater-Standorten ab.

Meshtastic erzeugt Zusatzverkehr durch Knoteninformationen, Batterietelemetrie, GPS-Pakete und Nachbarerkennung. Neuere Firmware-Versionen haben diesen Aufwand reduziert. *Eine Anpassung dieser Einstellungen löst Leistungsprobleme oft, bevor ein Protokollwechsel nötig ist.*

### MeshCore-Routing

Bei MeshCore kann eine erste **Direktnachricht** zur Pfadsuche geflutet werden. Spätere Direktnachrichten können diesen Pfad nutzen und je nach Einstellung wieder auf Fluten zurückfallen. **[Öffentliche und private Gruppenkanäle werden weiterhin geflutet](https://docs.meshcore.io/faq/#5-general)**, und zwar über dafür zugelassene Repeater. Endgeräte leiten keine Pakete anderer Knoten weiter.

**Repeater leiten Daten zwischen Knoten weiter.** Raumserver können Gruppengespräche hosten und Nachrichten für später zurückkehrende Clients speichern.

**Die Funkzeit hängt vom Verkehr ab.** Gruppennachrichten können bei beiden Protokollen mehrere Relais erreichen. Ein gelernter Pfad kann Direktnachrichten mit weniger Sendungen zustellen. Relaisstandorte, Funkeinstellungen und Nachrichtenrate bleiben wichtig.

Ohne Repeater kommunizieren Clients direkt, wenn sie in Reichweite sind. *Die Architektur funktioniert mit Infrastruktur am besten. Infrastruktur ist keine zwingende Voraussetzung.*

______

## Hardware

Beide Protokolle laufen auf denselben gängigen LoRa-Platinen.

| Platine | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Ja | Ja |
| LILYGO T-Echo (nRF52840 + SX1262) | Ja | Ja |
| Heltec WiFi LoRa 32 V3 | Ja | Ja |
| RAK WisBlock 4631 | Ja | Ja |
| Seeed SenseCAP Indicator | Ja | Teilweise |
| Station G2 | Ja | Ja |

**Du kannst dasselbe physische Gerät mit beiden Firmware-Varianten flashen.** Ein Protokollwechsel benötigt keine neue Hardware. Das Experiment kostet nur Zeit.

______

## Einrichtungsaufwand

### Meshtastic einrichten

1. Firmware von meshtastic.org herunterladen
2. Über den Web-Flasher unter flasher.meshtastic.org flashen, ohne Treiber
3. Meshtastic-App auf dem Smartphone installieren
4. Per Bluetooth koppeln
5. Einem Kanal mit gemeinsamem Namen und Passwort beitreten oder einen erstellen

**Einrichtung für Erstnutzer: weniger als 20 Minuten.** Die Kanalverschlüsselung nutzt vorab geteilte AES-256-Schlüssel. Der öffentliche Standardkanal verbindet dich sofort mit jedem Meshtastic-Knoten in Reichweite. Bei aktivem GPS zeigt die App die Positionen auf einer Karte.

### MeshCore einrichten

1. Infrastrukturknoten, Repeater oder Raumserver, mit PlatformIO oder vorkompilierten Binärdateien flashen
2. Client-Begleitfunkgerät flashen
3. MeshCore-App installieren
4. Adresse und Zugangsdaten der Infrastruktur in der App eintragen
5. Begleitfunkgerät per Bluetooth verbinden

**Die Einrichtung braucht mehr Planung.** Vor dem Einsatz musst du die Rollen der Knoten verstehen. Raumserver sind optional, speichern aber Nachrichten für offline befindliche Clients. *Zwei Freunde, die schnell kommunizieren wollen, sollten Meshtastic verwenden. Ein Team mit Basisstation und Dach-Repeater sollte MeshCore einsetzen.*

______

## Sendezeit ist die eigentliche Grenze

Beide Protokolle nutzen LoRa. **Die LoRa-Kapazität hängt von Sendezeit und Duty-Cycle-Budget ab, nicht von der Knotenzahl.**

Diese Faktoren bestimmen die Netzleistung:

- **Spreizfaktor.** Höhere Werte vergrößern die Reichweite, senken aber Datenrate und Gesamtkapazität.
- **Sendezeit-Preset.** Presets für große Reichweite verbrauchen mehr Duty Cycle pro Nachricht.
- **Telemetrieintervall.** GPS-, Batterie- und Umweltdaten von Meshtastic erzeugen dauerhaften Zusatzverkehr.
- **Nachrichtenrate.** Häufig sendende Nutzer beeinträchtigen die Leistung stärker als passive Knoten.
- **Repeater-Standort.** Ein gut platzierter Repeater verteilt die Last. Ein schlecht platzierter erhöht die Überlastung.
- **Gelände.** Knoten, die sich nicht hören, erzeugen Verkehr ohne gegenseitige Konkurrenz. Knoten in Reichweite vieler anderer erzeugen Konkurrenz.

**Feste Repeater** machen die Abdeckung planbar, verhindern aber kein Fluten. Teste vor der Wahl beide Protokolle mit der erwarteten Nachrichtenrate, den Funkeinstellungen und der geplanten Relaisanordnung.

______

## Vorschriften

Leistungsvergleiche unterscheiden sich je nach Region, da andere Vorschriften gelten:

- **915 MHz (USA):** Kein festes Duty-Cycle-Limit nach FCC Part 15, aber Leistungsgrenzen gelten.
- **868 MHz (EU):** 1 % Duty Cycle nach ETSI, also 36 Sekunden Sendezeit pro Stunde und Kanal.
- **433 MHz (EU/Asien):** In vielen Regionen gelten strengere Grenzen, oft 10 % auf bestimmten Teilbändern.

**Das Duty-Cycle-Limit von 1 % in Europa ist eine feste gesetzliche Grenze.** Dichte Meshtastic-Netze in der EU erreichen das Limit schneller als vergleichbare US-Netze. Die effizientere Sendezeitnutzung von MeshCore bringt in Regionen mit Duty-Cycle-Limits einen entsprechend größeren Vorteil.

______

## Datenschutz und Sicherheit

### Meshtastic

Meshtastic verschlüsselt Datenverkehr auf privaten Kanälen mit **vorab geteilten AES-256-Schlüsseln**. Alle Nachrichten eines Kanals verwenden denselben Schlüssel. Wer den Kanalschlüssel besitzt, kann alle Nachrichten lesen, auch GPS-Positionen. **Der öffentliche Standardkanal nutzt einen bekannten, mit der Firmware ausgelieferten Schlüssel.** Damit bietet der Datenverkehr keine Vertraulichkeit gegenüber Meshtastic-Nutzern in der Nähe.

GPS-Positionen auf privaten verschlüsselten Kanälen sind nur für Knoten mit dem Schlüssel sichtbar. Auf dem öffentlichen Kanal kann sie jeder sehen. *Das ist wichtig, wenn die Ortung operative Folgen hat.*

Meshtastic 2.6 verbesserte das Routing für Direktnachrichten. Gruppenverkehr nutzt weiterhin den Kanal-PSK. Direktnachrichten bieten mehr Isolation, sind aber nicht Ende-zu-Ende nach dem Vorbild des Signal-Protokolls verschlüsselt.

### MeshCore

**Routing verbirgt keine Funkaktivität.** Gehe nicht davon aus, dass ein gelernter Pfad verschleiert, welche Repeater senden. **Direktnachrichten verwenden eine Verschlüsselung pro Kontakt**, keinen gemeinsamen Kanalschlüssel. Andere Knoten derselben Infrastruktur können dein Direktgespräch auch dann nicht entschlüsseln, wenn sie denselben Repeater verwenden.

Infrastrukturknoten leiten verschlüsselten Verkehr weiter. Bei Direktnachrichten mit Kontaktverschlüsselung leitet der Repeater Chiffretext weiter, ohne ihn zu entschlüsseln. Bei Raumgesprächen sehen Raumserver die Inhalte der Räume, die sie hosten. *Entscheidend ist, ob du den Raumserver kontrollierst.*

MeshCore bietet keine strikte Ende-zu-Ende-Verschlüsselung wie Signal. **Die Kontaktverschlüsselung von Direktnachrichten ist eine deutliche Verbesserung gegenüber einem gemeinsamen Kanal-PSK.** Bei Anwendungen mit hohem Risiko solltest du die Implementierungsdetails prüfen.

______

## Stromverbrauch

**Weniger Sendevorgänge verbessern die Akkulaufzeit der Client-Knoten.** Meshtastics Telemetrie, GPS-Broadcasts und Flooding verbrauchen Sendezeit. Du kannst den Aufwand deutlich senken, indem du Telemetrieintervalle anpasst und GPS-Broadcasts auf Knoten ohne GPS deaktivierst.

**Vergleiche die Akkulaufzeit bei gleicher Last.** Telemetrie, Sendezeit und Knotenrolle sind ebenso wichtig wie das Protokoll.

______

## Netzresilienz

**Meshtastics kontrolliertes Flooding ist ausfallsicher.** Der Verlust eines Relay-Knotens hat oft geringe Folgen, da andere Knoten den Verkehr automatisch umleiten. Du musst verfügbare Knoten nicht im Voraus kennen. Das Mesh heilt sich passiv.

**MeshCore hängt stärker vom Repeater-Standort ab.** Ein gut geplantes MeshCore-Netz mit guter Repeater-Abdeckung bietet vorhersagbare Leistung. Fällt der einzige Repeater in einem Gebiet aus, verlieren davon abhängige Knoten die Verbindung. *MeshCore belohnt frühe Planung. Meshtastic verzeiht Knotenausfälle besser.*

**Gelernte Pfade und Fluten lösen unterschiedliche Probleme.** Ein Ersatzpfad hilft nur, wenn ein anderes geeignetes Relais das Paket hören und weiterleiten kann.

______

## GPS und Standortverfolgung

**Das GPS-Ökosystem von Meshtastic ist stärker.** Die Mobil-App enthält eine Kartenansicht. Community-Knoten speisen öffentliche Tracking-Karten wie meshmap.net über MQTT-Gateways. GPS-Telemetrie ist eine Kernfunktion. Das Teilen von Positionen für Wandergruppen, Such- und Rettungseinsätze und Veranstaltungen ist gut entwickelt.

MeshCore konzentriert sich nicht auf Standortverfolgung. *Wenn GPS-Übersicht eine Kernanforderung ist, ist das Meshtastic-Ökosystem 2026 weiter entwickelt und ausgereifter.*

______

## Ökosystem und Community

Meshtastic hat eine **größere Community**:

- Aktiver Discord mit Tausenden Mitgliedern
- Aktives Subreddit unter r/meshtastic
- Ausführliche Dokumentation auf meshtastic.org
- Integrationen von Drittanbietern für MQTT, Home Assistant, Node-RED, ATAK und Python-Bibliotheken
- Regelmäßige Firmware-Releases
- Viele von der Community erstellte Hardware-Anleitungen

MeshCore wächst, bleibt aber kleiner. *Es gibt weniger Forenbeiträge, Anleitungen und Integrationen von Drittanbietern. Bei Problemen suchst du eher im Firmware-Quellcode oder im Projekt-Discord als nach einer vorhandenen Lösung.*

Beide Projekte sind Open Source, ihre Lizenzen unterscheiden sich. **Meshtastic nutzt eine BSD-artige Lizenz. MeshCore nutzt die GPL.** Für manche Organisationen ist das bei Einsatz und Weitergabe relevant.

______

## Wann Meshtastic gewinnt

**Kleine, informelle Gruppen.** Ein Wanderverein, der Offline-Textnachrichten und Standortfreigabe möchte, sollte Meshtastic verwenden. Die Einrichtung ist einfach, die Karte funktioniert gut und das Netz organisiert sich selbst.

**Mobile Einsätze.** Nutzer, die sich durch Gelände bewegen und unvorhersehbar dazukommen oder weggehen, profitieren vom selbstorganisierenden Flooding. Die Infrastruktur muss bewegliche Knoten nicht vorab einplanen.

**Einsätze für Endnutzer.** Nichttechnische Personen können ihre Geräte selbst einrichten. Meshtastic ist leicht zugänglich.

**Schneller Einsatz für eine Veranstaltung.** Festival-Kommunikation, Rennkoordination oder Such- und Rettungsaufbau, der heute eingerichtet und nächste Woche abgebaut wird. Schnelle Einrichtung und fehlende Infrastrukturabhängigkeit machen Meshtastic praktisch.

**GPS-Ortung.** Wenn die Standortübersicht 2026 der Hauptzweck ist, ist Meshtastic die passende Wahl.

______

## Wann MeshCore gewinnt

**Geplante Infrastruktur.** Du hast einen Repeater auf dem Dach oder einen zuverlässig versorgten Raumserver. MeshCores hybrides Routing nutzt feste Infrastruktur.

**Große Netze mit eigener Infrastruktur.** **Teste Gruppenverkehr vor einem Wechsel.** Feste Repeater verbessern die planbare Abdeckung, geben Gruppenkanälen aber keine gerichteten Pfade.

**Nachrichtenpersistenz bei unterbrochener Verbindung.** Raumserver speichern Nachrichten und liefern sie aus, wenn Clients erneut verbunden sind. **Das ist einer der greifbarsten praktischen Vorteile von MeshCore gegenüber Meshtastic.**

**Trennung zwischen festen und mobilen Knoten.** Manche Knoten sollen Infrastruktur bereitstellen, andere sollen Clients sein. MeshCores Rollenmodell wurde dafür entwickelt.

**Regionen mit Duty-Cycle-Beschränkungen.** Installationen in Europa unter dem ETSI-Limit von 1 % profitieren stärker von MeshCores effizienter Sendezeitnutzung.

**Kontaktverschlüsselung.** Für die Verschlüsselung von Direktnachrichten ist MeshCores Modell deutlich besser als Meshtastics Kanal-PSK-Ansatz.

______

## Wo die Systeme an Grenzen stoßen

### Schwächen von Meshtastic

- **Sendezeitkonkurrenz bei hoher Netzdichte.** Dichte Netze mit sehr kommunikativen Standardeinstellungen, häufigen GPS-Broadcasts und aktiven Kanälen verlieren Leistung. Passe zuerst die Konfiguration an.
- **Keine Nachrichtenpersistenz ohne Infrastruktur.** Ohne MQTT-Gateway bleiben verpasste Nachrichten verpasst.
- **Standortdatenschutz auf dem öffentlichen Kanal.** Jeder Zuhörer sieht alle GPS-Broadcasts. Für informelle Nutzung ist das vertretbar, nicht für operative Sicherheitsanforderungen.
- Größere Firmware-Releases verursachen gelegentlich Kompatibilitätsprobleme, bis das Netz eine passende Version einsetzt.

### Schwächen von MeshCore

- **Komplexe Einrichtung.** Vor einem sinnvollen Einsatz musst du Infrastrukturrollen verstehen.
- **Kleinere Community.** Meshtastics Dokumentation, Anleitungen und Integrationen von Drittanbietern sind weiter entwickelt.
- **Weniger Hardwareauswahl.** MeshCore unterstützt eine kleinere Geräteliste.
- **Weniger ausgereifte Mobil-Apps.** Sie funktionieren, sind aber nicht so ausgefeilt wie Meshtastics iOS- und Android-Apps.
- **Infrastrukturabhängigkeit für optimale Leistung.** Ohne Repeater kommunizieren Clients direkt, aber der Routing-Vorteil entfällt. Ohne feste Infrastruktur kommt der Architekturvorteil nicht zum Tragen.
- **Netzheilung.** Fällt ein Repeater in einem Gebiet aus, verlieren davon abhängige Knoten die Verbindung. Meshtastics Flooding ist toleranter gegenüber Ausfällen.
- **Keine Protokollinteroperabilität.** MeshCore und Meshtastic tauschen keine Nachrichten aus. Dieselbe Hardware kann eine der beiden Firmware-Varianten ausführen, aber bei parallelem Betrieb verwaltest du zwei getrennte Netze.

______

## Funktechnik ist wichtiger als Firmware

**Antennenqualität, Antennenhöhe, Leitungsverluste, Gelände und Funkeinstellungen beeinflussen die Netzleistung stärker als die Firmwarewahl.**

Ein gut platzierter Meshtastic-Knoten auf einem Hügel mit guter Antenne übertrifft einen schlecht platzierten MeshCore-Repeater in einem Metallgehäuse im Keller. Der Protokollvergleich setzt eine ungefähr gleich gute physische Installation voraus.

Prüfe vor einem Protokollwechsel zur Lösung eines Leistungsproblems:

- Antennenanschlüsse sind sauber und verlustarm.
- Knoten stehen so hoch wie praktisch möglich.
- Das Sendezeit-Preset entspricht der benötigten Reichweite.
- **Telemetrieintervalle überlasten den Kanal nicht.**
- Der Spreizfaktor passt zur Knotendichte.

______

## Vergleich auf einen Blick

| Faktor | Meshtastic | MeshCore |
|---|---|---|
| Netzwerkmodell | Gesteuertes Fluten für Kanäle, gelernter nächster Knoten für Direktnachrichten | Fluten für Kanäle, gelernter Repeater-Pfad für Direktnachrichten |
| Einrichtungsaufwand | Einfach | Mittel bis hoch |
| Skalierungsziel | Flexibel, Leistung sinkt bei Sendezeitkonkurrenz | Für größere geplante Netze entwickelt |
| Qualität der Mobil-App | Sehr gut | Funktional |
| Größe der Community | Sehr groß | Wachsend |
| GPS/Standortverfolgung | Starkes, entwickeltes Ökosystem | Geringer Schwerpunkt |
| Nachrichtenpersistenz | Nein, benötigt MQTT-Gateway | Ja, optional über Raumserver |
| Verschlüsselung von Direktnachrichten | Kanal-PSK | Verschlüsselung pro Kontakt |
| Infrastrukturbedarf | Keine nötig | Für Infrastrukturknoten optimiert |
| Netzheilung | Resilient und selbstheilend | Hängt von Repeater-Standorten ab |
| Hardwareunterstützung | Breit | Gezielte Auswahl |
| Am besten für | Mobile, spontane und kleine Gruppen | Geplante Installationen mit fester Infrastruktur |

______

## Die richtige Wahl

**Beginne mit Meshtastic.** Innerhalb eines Nachmittags bist du auf Sendung. Du findest Leute zum Testen. Die App funktioniert und die Dokumentation ist ausgezeichnet. Meshtastic 2.6 schließt mit Next-Hop-Routing für Direktnachrichten die Effizienzlücke bei Punkt-zu-Punkt-Verkehr.

**Ziehe MeshCore in Betracht**, wenn du dedizierte Repeater oder optionale Raumserver brauchst, die Beiträge für später wieder verbundene Teilnehmer speichern.

Stimme vor einem Wechsel **dein Meshtastic-Netz ab**. Reduziere Telemetrieintervalle. Deaktiviere GPS-Broadcasts auf Knoten ohne GPS. Passe das Sendezeit-Preset an die Knotendichte an. *Viele Leistungsprobleme sind Konfigurationsprobleme, keine Protokollprobleme.*

**Beide Meshes profitieren von gut platzierten Relais.** Welche Knoten senden, hängt von ihren Rollen und vom Verkehr ab.

*Möchtest du LoRa mit Packet Radio, WLAN oder dem Internet verbinden, statt bei einem einzelnen LoRa-Mesh zu bleiben?* Lies den **[Vergleich Meshtastic, MeshCore und Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)**. Er zeigt, wo transportunabhängige Netzwerke passen und wo sie unnötige Komplexität hinzufügen.
