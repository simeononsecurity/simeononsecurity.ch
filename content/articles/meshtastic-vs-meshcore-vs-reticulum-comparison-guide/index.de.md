---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Vergleiche Meshtastic, MeshCore und Reticulum nach Routing, Sendezeit, Infrastruktur, Transport und Einsatz ohne Internetverbindung."
genre: ["LoRa", "Mesh-Netzwerke", "Kommunikation ohne Infrastruktur", "Notfallkommunikation", "Amateurfunk", "Quelloffene Software", "Katastrophenvorsorge", "Drahtlosnetzwerke", "Datenschutz", "Netzwerke"]
tags: ["meshtastic vs meshcore vs reticulum", "Reticulum-Netzwerk", "meshtastic", "meshcore", "reticulum", "lxmf", "LoRa-Mesh-Netz", "Kommunikation ohne Infrastruktur", "rnode", "Paketfunk", "transportunabhängige Vernetzung", "Mesh-Netzwerke", "Notfallkommunikation", "gemeinschaftliches Mesh-Netzwerk", "LoRa-Sendezeit", "kontrolliertes Flooding", "Hop-Limit", "Repeater-Knoten", "Room-Server", "Sideband-App", "nomadnet", "meshchat", "Katastrophenkommunikation", "Funk ohne Infrastruktur", "Mesh-Netzwerkprotokoll", "regionales Mesh-Netz", "HF-Technik"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Illustration zum Vergleich dreier Mesh-Netzwerksysteme mit Knoten, Antennen und Verbindungslinien vor dunklem Hintergrund und in leuchtenden Farben."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## Die kurze Antwort

**Diese drei Projekte lösen nicht alle dasselbe Problem.** Meshtastic und MeshCore sind LoRa-Mesh-Netzwerksysteme mit unterschiedlichen Routing-Konzepten. Reticulum ist breiter angelegt. Es ist eine transportunabhängige Netzwerkschicht, die gleichzeitig über LoRa, Paketfunk, WLAN, Ethernet, serielle Verbindungen und das Internet läuft.

**Die richtige Frage lautet nicht „Welches ist das beste?“** Sie lautet: „Welche Architektur passt zu dem Netzwerk, das ich aufbauen will?“

*Meshtastic passt zu Ad-hoc-Netzen und mobilen Nutzern.* **MeshCore passt zu gezielt aufgebauter, fester Infrastruktur.** **Reticulum passt zu Netzwerken, die verschiedene Transportwege verbinden oder sonst getrennte Netze zusammenschalten müssen.** Wer ein regionales LoRa-Mesh aufbaut, braucht meist nur eine der ersten beiden Optionen.

______

## Definiere das Netzwerk, das du aufbaust

Notiere vor dem Protokollvergleich, was das Netzwerk leisten muss. Für die meisten Community- und Notfallkommunikationsnetze eignet sich dieses Ziel:

- **Lizenzfreier Betrieb**, damit alle ohne Amateurfunklizenz teilnehmen können
- **Günstige Hardware**, die eine Community in größerem Maßstab einsetzen kann
- **Niedriger Stromverbrauch**, idealerweise mit Solar- oder Batterieversorgung
- **Kommunikation über große Entfernungen** ohne Mobilfunk- oder Internetverbindung
- **Unabhängigkeit von Infrastruktur**, Stromnetz, Internetanbietern und Mobilfunkbetreibern
- **Einfach genug für Menschen ohne Funkkenntnisse** einzurichten und zu nutzen
- **Für den Einsatz in einer Community geeignet**, nicht nur im Keller eines einzelnen Betreibers
- **Skalierbar über eine Handvoll Knoten hinaus**, ohne zusammenzubrechen
- **Nützlich bei Infrastrukturausfällen**, wenn Mobilfunkmasten und Internet ausfallen
- **Zuverlässige Zustellung statt Rekordreichweite**

Behalte diese Liste im weiteren Verlauf im Blick. Wir bewerten jeden Architekturkompromiss anhand dieser Anforderungen.

______

## Meshtastic

**Meshtastic** ist die ausgereifteste und am weitesten verbreitete Option. Für die meisten Nutzer macht es vieles richtig.

- **Ausgereiftes Ökosystem** mit jahrelanger aktiver Entwicklung
- **Große Community**, aktiver Discord-Server und umfangreiche Dokumentation
- **Breite Hardware-Unterstützung** für Boards von LILYGO, Heltec, RAK und Seeed
- **Gute mobile Apps** für iOS und Android
- **Leichter Einstieg**, die Ersteinrichtung dauert weniger als 20 Minuten
- **Gute Unterstützung für tragbare Geräte und mobile Nutzer**, die dem Mesh unvorhersehbar beitreten und es wieder verlassen
- **GPS- und Telemetriefunktionen** mit einem ausgereiften Ökosystem
- **Bestehende Installationen** in den meisten Ballungsräumen erleichtern den Einstieg, weil du einem Netzwerk beitrittst, statt bei null zu beginnen

Einen vollständigen Vergleich von Meshtastics Routing, Hardwarekompatibilität und Einrichtung mit MeshCore findest du im **[Vergleichsleitfaden zu MeshCore und Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Dieser Artikel behandelt die wichtigste Architekturfrage für größere Installationen: **kontrolliertes Flooding und Hop-Limits**.

### Kontrolliertes Flooding und die Bedeutung der Hops

Beim **[gesteuerten Fluten](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** in Meshtastic bricht ein normaler Client eine geplante Weitersendung ab, wenn er dasselbe Paket zuvor von einem anderen Knoten hört. `ROUTER` und `ROUTER_LATE` können es trotzdem weiterleiten. Bei `CLIENT_BASE` gilt diese Ausnahme für Verkehr zu oder von Favoriten.

Der Hop-Zähler von Meshtastic startet standardmäßig bei **3** und erlaubt maximal **7**. Ab Firmware 2.7.11 können geeignete Infrastrukturknoten [den Zähler unverändert lassen](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/), wenn es nicht der erste Hop ist und zuvor ein favorisiertes Gerät vom Typ `ROUTER` oder `ROUTER_LATE` weitergeleitet hat. Jede tatsächliche Sendung belegt Funkzeit.

Ein höheres Hop-Limit kann weitere Relais erreichen, zwingt aber nicht jeden Empfänger zum Senden. **Mehr Weiterleitungen** können Folgendes bedeuten:

- **Mehr Sendezeit** pro Nachricht
- **Mehr Kopien in der Luft**, wenn mehrere geeignete Relais dasselbe Paket weiterleiten
- **Mehr Konkurrenz** um den gemeinsam genutzten Kanal
- **Höheres Kollisionsrisiko**, wenn mehr Funkgeräte im selben Zeitfenster senden
- **Höheren Batterieverbrauch** an jedem empfangenden und weiterleitenden Knoten
- **Weniger verfügbare Kanalkapazität** für tatsächliche Nachrichten

Die LoRa-Kapazität wird durch Sendezeit und regionale Duty-Cycle-Grenzen bestimmt, nicht durch die Anzahl der Knoten. Ein Netzwerk mit zehn aktiven Knoten, die häufig GPS- und Telemetriedaten senden, kann einen Kanal auslasten, den fünfzig unauffällige Sensoren kaum beanspruchen würden. Deshalb baut ein dichtes Mesh mit hohem Hop-Limit schneller ab als dieselbe Anzahl Knoten mit niedrigerem Hop-Limit und kontrollierten Telemetrieintervallen.

Seit Meshtastic 2.6 nutzen **Direktnachrichten** zunächst Fluten zur Pfadsuche und versuchen danach die Weiterleitung über den gelernten nächsten Knoten. Wenn das scheitert, können sie erneut fluten.

Bei einem kleinen oder mittelgroßen Mesh, etwa für einen Wanderverein, spielt dies selten eine Rolle. Bei einem **regionalen Netzwerk, das eine Stadt oder mehrere Orte abdecken soll**, wird es zur zentralen Designgrenze.

______

## MeshCore

**Dedizierte Repeater** bilden die feste Weiterleitungsebene von MeshCore. Client-Funkgeräte sind Endpunkte.

### Knotenrollen

MeshCore-Installationen basieren auf klar getrennten Rollen und nicht auf einer flachen Gruppe gleichwertiger Knoten:

- **Begleit- oder Client-Knoten** enthalten ein LoRa-Funkgerät, das mit einem Telefon oder Laptop gekoppelt ist. Wenn Infrastruktur in der Nähe verfügbar ist, kommunizieren sie über diese
- **Repeater** leiten gezielt den Verkehr zwischen Clients und anderen Infrastrukturkomponenten weiter. Sie übernehmen den Großteil der eigentlichen Routing-Arbeit
- **Room-Server** (optional) hosten Gruppengespräche und liefern gespeicherte Nachrichten an Clients aus, wenn diese sich wieder verbinden

Bei MeshCore kann eine erste **Direktnachricht** zur Pfadsuche geflutet werden. Spätere Direktnachrichten können diesen Pfad nutzen und je nach Einstellung wieder auf Fluten zurückfallen. **[Öffentliche und private Gruppenkanäle werden weiterhin geflutet](https://docs.meshcore.io/faq/#5-general)**, und zwar über dafür zugelassene Repeater. Endgeräte leiten keine Pakete anderer Knoten weiter.

### Warum sich dies für feste Infrastruktur eignet

*Das ist das zentrale Argument für MeshCore.* Meshtastics Flooding-Modell hat echte Vorteile für Ad-hoc- und mobile Netzwerke: keine Planung, keine zu wartende Infrastruktur und eine gute Anpassung an wechselnde Knoten. MeshCores Routing-Modell ist im Vorteil, wenn **Nutzer gezielt Infrastruktur aufbauen**.

Ein Netzwerk mit bekannten, erhöhten Repeatern ermöglicht eine gezielte Planung der Abdeckung. Sie hängt nicht davon ab, welche Knoten sich an einem bestimmten Tag zufällig erreichen. Das ist wichtig für:

- **Dauerhaft installierte Dachknoten** mit zuverlässiger Stromversorgung
- **Türme** und bestehende Kommunikationsinfrastruktur
- **Solar-Repeater** an unbesetzten Standorten
- **Relaisstandorte in Bergen oder auf Anhöhen**
- **Community-eigene Infrastruktur**, die mehrere Gruppen gemeinsam nutzen
- **Regionale Netzwerke**, die mehr als ein einzelnes Viertel abdecken
- **Notfallkommunikation**, bei der berechenbare Abdeckung wichtiger ist als Flexibilität

Beziehe dies auf die Grundlagen der HF-Technik: **Zuverlässige Verbindungen zwischen gut platzierten Infrastrukturelementen sind wichtiger als maximale Antennenverstärkung, Sendeleistung oder theoretische Reichweite.** **Beide Meshes profitieren von gut platzierten Relais.** Welche Knoten senden, hängt von ihren Rollen und vom Verkehr ab.

______

## Das Argument für mobile Knoten und seine Kosten

Ein häufiger Vorschlag lautet: *„Meshtastic ist besser für mobile Knoten, MeshCore für feste. Also nutzen wir Meshtastic für die Nutzer und MeshCore als Backbone.“*

Auf dem Papier klingt das verlockend. In der Praxis vereint eine Mischung nicht automatisch die Vorteile beider Systeme, denn **Meshtastic und MeshCore verwenden unterschiedliche Routing- und Netzwerkarchitekturen und tauschen keine Nachrichten miteinander aus.** Eine Verbindung erfordert eine Übersetzungsschicht zwischen inkompatiblen Systemen. Sie kombiniert nicht einfach die jeweils besten Eigenschaften.

Mit einer solchen Verbindung betreibst du:

- **Zwei getrennte Netzwerke**, jeweils mit eigener Topologie und eigenem Verhalten
- **Zwei Routing-Modelle**, die keinen Zustand miteinander teilen
- **Eine Übersetzungsschicht**, die Entwicklung und laufende Wartung erfordert
- **Zusätzliche Infrastruktur**, auf der die Bridge läuft
- **Mehr Konfiguration** über zwei Firmware-Ökosysteme statt eines
- **Mehr Fehlerquellen**, da die Bridge unabhängig von den Mesh-Netzen ausfallen kann
- **Aufwendigere Fehlersuche**, weil ein Zustellungsfehler in einem der Netze oder in der Verbindung dazwischen liegen kann

Stelle vor dieser Entscheidung eine direkte Frage: **Löst die zusätzliche Komplexität ein Problem, das ein einzelnes, gut abgestimmtes Mesh-Protokoll nicht lösen kann?** Oft bietet eine korrekt eingerichtete MeshCore-Installation mit einigen mobilfreundlichen Begleitknoten oder eine Meshtastic-Installation mit wenigen gut platzierten Relais und einem höheren Hop-Limit den praktischen Nutzen, ohne zwei verbundene Netze zu betreiben.

______

## Reticulum

Reticulum verdient eine eigene Kategorie und keinen Platz als „dritte LoRa-Mesh-Option“, denn es ist nicht in erster Linie ein LoRa-Mesh-Protokoll. **Sein entscheidendes Merkmal ist die Transportunabhängigkeit.**

Reticulum ist ein kryptografischer Netzwerk-Stack. Er verwendet keine Quelladressen, daher enthalten Pakete keine Information über ihren Ursprung. Jede Adresse ist selbstbestimmt: Nach ihrer Erstellung ist sie innerhalb von Sekunden bis Minuten weltweit erreichbar. Sie bleibt es auch dann, wenn sich das Gerät physisch an einen anderen Ort des Netzwerks bewegt. Die gesamte Kommunikation ist standardmäßig mit kurzlebigen Schlüsseln und Forward Secrecy verschlüsselt. Reticulum verwirft unverschlüsselte Pakete, statt sie zuzustellen. Dafür sind keine Kernel-Treiber nötig. Es läuft im User-Space auf jedem System mit Python 3, einschließlich eines Raspberry Pi Zero.

Reticulum unterstützt folgende Schnittstellen:

- **LoRa** mit RNode-kompatibler Hardware (ein festgelegtes, offenes LoRa-Transceiver-Design, das sich bauen, auf gängige Boards flashen oder fertig kaufen lässt)
- **Paketfunk** über jedes TNC im KISS-Modus, passend für den VHF- und UHF-Amateurfunk
- **WLAN und kabelgebundenes Ethernet** mit automatischer Peer-Erkennung ohne Router oder DHCP-Server
- **Serielle Verbindungen** für direkte Geräteverbindungen
- **TCP und UDP über vorhandene IP-Netze**, einschließlich des Internets
- **Das I2P-Netzwerk** sowie benutzerdefinierte Schnittstellen für andere Systeme mit einer Python-Bridge

Auf Reticulum bauen Anwendungen wie **LXMF** (ein verzögerungstolerantes Nachrichtenprotokoll) und Endnutzerwerkzeuge wie **Sideband**, **NomadNet** und Community-Clients für **MeshChat** auf. Sie bieten Reticulum-Netzen eine Nachrichten- und Browsing-Schicht, die mit den ab Werk enthaltenen Funktionen von Meshtastic und MeshCore vergleichbar ist.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagramm, in dem Reticulum ein LoRa-Mesh, ein Paketfunknetz und eine Internetverbindung zu einem adressierbaren, verschlüsselten Netzwerk verbindet" >}}

### Wann Reticulum sinnvoll ist

Der Nutzen von Reticulum zeigt sich in einer heterogenen Konfiguration, zum Beispiel:

**LoRa-Mesh → Reticulum-Knoten → IP-Verbindung → Reticulum-Knoten → Funknetz**

Hier übernimmt Reticulum eine Aufgabe, die weder Meshtastic noch MeshCore erfüllt: Es verbindet zwei unterschiedliche Kommunikationssysteme zu einem adressierbaren Netzwerk. Das ist eine echte, konkrete Anforderung und keine allgemeine Verbesserung. Geeignet ist Reticulum etwa für:

- **Geografisch getrennte Netzwerke**, zwischen denen keine direkte Funkverbindung besteht
- **Unterschiedliche physische Übertragungswege**, etwa ein LoRa-Mesh am einen und ein Paketfunknetz am anderen Ende
- **Funk-IP-Gateways**, die Verkehr zwischen einem Funknetz im Feld und dem Internet weiterleiten
- **Experimentelle und wissenschaftliche Netzwerke**, bei denen die Mischung verschiedener Übertragungswege wichtiger ist als ein einfacher Aufbau
- **Netzwerke, bei denen kein einzelner Transportweg alle Anforderungen erfüllt** und mehrere Teile verbunden werden müssen

### Wann Reticulum unnötige Komplexität erzeugt

Wenn alle Beteiligten kompatible LoRa-Hardware verwenden und das tatsächliche Ziel **ein einziges regionales LoRa-Mesh** ist, bringt Reticulum wenig Nutzen und verursacht echten Aufwand. Jede zusätzliche Schicht im Netzwerk-Stack bedeutet mehr:

- **Konfiguration**, die auf allen Knoten korrekt und einheitlich sein muss
- **Software**, die installiert, aktualisiert und analysiert werden muss
- **Hardware** in manchen Konfigurationen, abhängig davon, wie Schnittstellen verbunden werden
- **Fehlersuche**, wenn etwas nicht zugestellt wird
- **Erforderliches Wissen**, weil Betreiber ein drittes Netzwerkmodell verstehen müssen

*Nutze Reticulum, wenn Transportunabhängigkeit eine echte Anforderung erfüllt, nicht nur weil mehr Schnittstellentypen unterstützt werden als bei der Alternative.* Ein Hop-Limit-Problem in einem LoRa-Mesh ist ein Tuning-Problem für Meshtastic oder MeshCore. Es ist kein Problem der Transportunabhängigkeit, und Reticulum macht es nicht dazu.

______

## Baue erst ein gesundes Mesh auf, bevor du drei fragmentierte Netze baust

Wenn ein Protokoll deine Anforderungen erfüllt, **baue ein gesundes Netzwerk** statt mehrerer kleiner Netze, die über Bridges verbunden sind. Das Prinzip „erst ein Mesh“ sollte die meisten bisherigen Entscheidungen leiten.

In einem Community-Netzwerk ist **die Interoperabilität der bestehenden Nutzer oft wichtiger als architektonische Flexibilität.** Ein großes, funktionierendes Netzwerk mit einem Protokoll ist praktischer als drei technisch interessante, aber fragmentierte Netze, die nur teilweise miteinander kommunizieren.

### Bestehende Meshtastic-Netze sind wichtig

**Verwirf Meshtastic nicht allein deshalb, weil MeshCore Architekturvorteile für feste Infrastruktur bietet.** Wenn es in einer Stadt bereits Dutzende oder Hunderte Meshtastic-Knoten gibt, ist dieser Bestand echte Infrastruktur und eine echte Community. Eine Migration kostet mehr, als ein Vergleich der technischen Daten erkennen lässt:

- **Installierte Hardware**, die neu geflasht oder ersetzt werden muss
- **Bestehende Nutzer**, die das Netzwerk bereits bedienen können
- **Community-Wissen**, das durch den bisherigen Betrieb entstanden ist
- **Bereits aufgestellte und platzierte Repeater**, manchmal an schwer zugänglichen Dächern oder Türmen
- **Konfigurationserfahrung** der Personen, die das Netzwerk betreiben
- **Etablierte Kanäle**, die Nutzer bereits beobachten
- **Schulungsbedarf** für alle, die ein zweites System lernen müssen

Die Protokollwahl ist **teils eine technische Frage und teils eine Frage der Akzeptanz durch die Community.** Die bessere Architektur auf dem Papier gewinnt nicht automatisch, wenn eine bestehende, aktive Community von vorn beginnen müsste.

______

## Die Herausforderung regionaler Netze

Stell dir einen hypothetischen Einsatz über mehrere Städte vor:

**Stadt A, Repeater, Repeater, ländliches Relais, Repeater, Stadt B, Repeater, Stadt C**

**Teste in dieser Kette Gruppen- und Direktnachrichten getrennt.** MeshCore kann gelernte Pfade für Direktnachrichten wiederverwenden, flutet aber Gruppennachrichten. Meshtastic kann auf geeigneten Infrastrukturverbindungen den Hop-Zähler unverändert lassen. Jede echte Weitersendung kostet Funkzeit. Keines der Protokolle garantiert die Zustellung über die ganze Strecke.

In diesem Szenario bestimmen **Hop-Limits, Sendezeitbudget, Routing-Verhalten und Infrastrukturplanung**, ob die Verbindung von Ende zu Ende funktioniert. Bei geografischer Ausdehnung sind die Architekturunterschiede zwischen Meshtastic und MeshCore nicht länger akademisch.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagramm einer regionalen Mesh-Netzwerkkette zwischen drei Städten mit Repeatern und einem ländlichen Relais, das die Zunahme von Sendezeit und Hop-Zahl über die Entfernung zeigt" >}}

______

## HF ist wichtiger als das Protokoll

**Keine ausgeklügelte Routing-Software schafft eine Funkverbindung, wo physisch keine vorhanden ist.** Prüfe zuerst die Grundlagen, bevor du ein Protokoll für ein Abdeckungsproblem verantwortlich machst:

- **Antennenhöhe** über Hindernissen
- **Sichtverbindung** zwischen den beiden Endpunkten einer Verbindung
- **Fresnelzonenfreiheit**, die nicht mit optischer Sichtverbindung gleichzusetzen ist
- **Kabelverluste** durch billiges oder zu langes Koaxialkabel
- **Antennenqualität** und ihre Eignung für das verwendete Band
- **Rauschpegel** am Empfangsstandort
- **Gelände** zwischen den Knoten
- **Knotenstandorte** und die realistischen Möglichkeiten, sie zu verbessern
- **Link-Marge**, der Abstand zwischen dem empfangenen Signal und dem Mindestpegel für die Dekodierung

*Eine gut platzierte 2-dBi-Antenne auf einem passenden Mast übertrifft oft eine schlecht positionierte Hochgewinnantenne am Kellerfenster.* Das Protokoll bestimmt, wie das Netzwerk vorhandene Verbindungen nutzt. Es schafft keine Funkverbindung, wenn die Physik sie nicht zulässt.

### Zuverlässigkeit statt maximaler Reichweite

**Entwirf das Netzwerk nicht anhand der größten Reichweite, die eine Verbindung gelegentlich erreicht.** Plane mit Verbindungen, die zuverlässig funktionieren.

Für ein Community- oder Notfallkommunikationsnetz hat **eine zuverlässige Zustellung über 15 Meilen mehr praktischen Wert als eine Verbindung über 40 Meilen, die gelegentlich klappt und sonst ausfällt.** Baue mit zuverlässiger Infrastruktur eine überlappende Abdeckung auf, statt Rekordverbindungen zu verfolgen. Dieses Prinzip gilt unabhängig vom verwendeten Protokoll.

______

## Welches System passt?

**Meshtastic ist sinnvoll**, wenn dir ein ausgereiftes Ökosystem, einfacher Einstieg, mobile Nutzer und Kompatibilität mit einer bestehenden Meshtastic-Community wichtig sind. Für die meisten, die bei null beginnen, ist es die richtige Standardwahl.

**Feste Repeater** machen die Abdeckung planbar, verhindern aber kein Fluten. Teste vor der Wahl beide Protokolle mit der erwarteten Nachrichtenrate, den Funkeinstellungen und der geplanten Relaisanordnung.

**Reticulum ist sinnvoll**, wenn die Aufgabe über ein einzelnes LoRa-Mesh hinausgeht und verschiedene Transportwege oder getrennte Netze zu einem adressierbaren System verbunden werden müssen.

Für ein **lizenzfreies, stromsparendes, weitreichendes Community-Infrastrukturnetz, das hauptsächlich auf festen Repeatern beruht**, ist MeshCore die bessere Wahl. **Teste Gruppenverkehr vor einem Wechsel.** Feste Repeater verbessern die planbare Abdeckung, geben Gruppenkanälen aber keine gerichteten Pfade. *Gibt es in deiner Region bereits ein gesundes Meshtastic-Netz, muss der Nutzen groß genug sein, um die Fragmentierung der bestehenden Community zu rechtfertigen.* Reticulum kommt ins Spiel, wenn ein Mesh-Protokoll oder physischer Transportweg die Anforderungen nicht mehr erfüllt, nicht nur weil Reticulum mehr Funktionen bietet.

______

## Quellen

1. [Meshtastic-Mesh-Broadcast-Algorithmus](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Meshtastic-LoRa-Konfiguration (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Offizielle MeshCore-Website](https://meshcore.co.uk/)
4. [Reticulum Network Stack](https://reticulum.network/)
5. [Was ist Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Reticulum-Schnittstellen konfigurieren](https://reticulum.network/manual/interfaces.html)
7. [Vergleichsleitfaden zu MeshCore und Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)
