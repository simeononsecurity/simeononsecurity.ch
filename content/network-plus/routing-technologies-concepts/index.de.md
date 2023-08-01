---
title: "Netzwerk-Plus-Kurs: Routing-Protokolle, -Konzepte und -Optimierung"
date: 2023-07-07
toc: true
draft: false
description: "Lernen Sie die Welt der Routing-Technologien und -Konzepte kennen, von dynamischen Routing-Protokollen wie RIP, OSPF, EIGRP und BGP bis hin zu Link-State-, Distanzvektor- und Hybrid-Routing-Protokollen sowie der Konfiguration von statischem Routing und Standardrouten."
genre: ["Technologie", "Vernetzung", "Weiterleitung", "Netzwerk-Protokolle", "Netzwerk-Management", "Dynamisches Routing", "Statisches Routing", "Bandbreitenmanagement", "Qualität der Dienstleistung", "Netzwerkgeräte"]
tags: ["Routing-Technologien", "dynamische Routing-Protokolle", "RIP", "OSPF", "EIGRP", "BGP", "Linkstatus", "Abstandsvektor", "hybride Routing-Protokolle", "statisches Routing", "Standard-Routen", "administrative Entfernung", "Außenverlegung", "inneres Routing", "Zeit zu leben", "Bandbreitenmanagement", "Verkehrsgestaltung", "Qualität der Dienstleistung", "Netzwerkgeräte", "Router", "schaltet", "Firewalls", "Lastverteiler", "Zugangspunkte", "Netzoptimierung", "Netzleistung", "Netzwerksicherheit", "Netzarchitektur", "Netzverkehr"]
cover: "/img/cover/An_illustration_of_interconnected_network_devi.png"
coverAlt: "Eine Illustration von miteinander verbundenen Netzwerkgeräten, zwischen denen Daten fließen."
coverCaption: "Navigieren auf dem digitalen Highway: Optimierung des Netzwerk-Routings für Spitzenleistungen"
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

## Einleitung

In der heutigen vernetzten Welt ist ein effizientes Netzwerk-Routing für eine reibungslose Datenübertragung und Kommunikation unerlässlich. Routing-Technologien und -Konzepte spielen eine entscheidende Rolle bei der Lenkung des Netzwerkverkehrs und der Optimierung der Netzwerkleistung. In diesem Artikel werden verschiedene Routing-Protokolle wie RIP, OSPF, EIGRP und BGP sowie Link-State-, Distance-Vector- und Hybrid-Routing-Protokolle vorgestellt. Wir werden uns auch mit der Konfiguration und Verwendung von statischem Routing und Standardrouten befassen. Außerdem werden wir verschiedene Geräte und ihre Platzierung im Netzwerk vergleichen und gegenüberstellen.

{{< youtube id="YRzr56cwgCg" >}}

## Dynamische Routing-Protokolle

Dynamische Routing-Protokolle wurden entwickelt, um den Austausch von Routing-Informationen zwischen Routern zu automatisieren. Sie passen sich an Netzveränderungen an, wie z. B. Topologieänderungen oder Verbindungsausfälle, indem sie die Routing-Tabellen dynamisch aktualisieren. Schauen wir uns einige häufig verwendete dynamische Routing-Protokolle genauer an:

### Routing Internet Protocol (RIP)

Das Routing Internet Protocol (RIP) ist ein Distanzvektor-Routing-Protokoll, das auf der Anzahl der Sprünge zwischen Routern basiert. Es verwendet die Hop-Count-Metrik, um den besten Pfad zu einem Zielnetz zu ermitteln. RIP unterstützt sowohl IPv4 als auch IPv6 und ist für kleine bis mittelgroße Netze geeignet.

### Open Shortest Path First (OSPF)

Open Shortest Path First (OSPF) ist ein Link-State-Routing-Protokoll, das den kürzesten Pfad zu einem Ziel mithilfe des Dijkstra-Algorithmus berechnet. Es berücksichtigt verschiedene Metriken, wie Bandbreite, Verzögerung und Zuverlässigkeit, um die optimale Route zu bestimmen. OSPF wird aufgrund seiner Skalierbarkeit und schnellen Konvergenz häufig in großen Unternehmensnetzen eingesetzt.

### Enhanced Interior Gateway Routing Protocol (EIGRP)

Enhanced Interior Gateway Routing Protocol (EIGRP) ist ein von Cisco entwickeltes hybrides Routing-Protokoll. Es kombiniert die besten Eigenschaften von Distanzvektor- und Link-State-Protokollen. EIGRP verwendet den Diffusing Update Algorithm (DUAL) zur Berechnung von Routen und bietet erweiterte Funktionen wie Ungleichkosten-Lastausgleich und Routenzusammenfassung.

### Border Gateway Protokoll (BGP)

Das Border Gateway Protocol (BGP) ist ein Protokoll für externe Gateways, das für das Routing zwischen autonomen Systemen (ASes) im Internet verwendet wird. BGP ist hoch skalierbar und ermöglicht es autonomen Systemen, Routing-Informationen auszutauschen. Es verwendet Pfadattribute und Richtlinien, um Routing-Entscheidungen auf der Grundlage von Faktoren wie Netzwerkrichtlinien, Pfadlänge und AS-Pfad zu treffen.

## Link-State-, Distanzvektor- und Hybrid-Routing-Protokolle

Routing-Protokolle können aufgrund ihrer Funktionsweise und der Informationen, die sie zur Bestimmung von Routen verwenden, in Link-State-, Distanzvektor- und Hybrid-Protokolle unterteilt werden.

### Link-State-Routing-Protokolle

Link-State-Routing-Protokolle wie OSPF erstellen eine detaillierte Karte des gesamten Netzwerks, indem sie Link-State-Informationen zwischen Routern austauschen. Jeder Router baut eine topologische Datenbank auf, die es ihm ermöglicht, den besten Pfad zu einem Zielnetz auf der Grundlage verschiedener Metriken zu berechnen.

### Distanzvektor-Routing-Protokolle

Distanzvektor-Routing-Protokolle wie RIP verwenden eine einfache Metrik (z. B. Hop Count) und tauschen Routing-Informationen mit benachbarten Routern aus. Router geben ihre Routing-Tabellen in regelmäßigen Abständen an benachbarte Router weiter, damit diese sich ein Bild vom Netz machen können. Distanzvektorprotokolle haben nur begrenzte Kenntnisse über das gesamte Netz und können für Routing-Schleifen anfällig sein.

### Hybride Routing-Protokolle

Hybride Routing-Protokolle wie EIGRP vereinen die Eigenschaften von Link-State- und Distance-Vector-Protokollen. Sie führen eine Topologietabelle ähnlich wie Link-State-Protokolle, verwenden aber Distanzvektor-Algorithmen für die Berechnung von Routen. Hybridprotokolle bieten die Vorteile einer schnelleren Konvergenz und eines geringeren Overheads.

{{< inarticle-dark >}}

## Statisches Routing und Standard-Routen

Beim statischen Routing wird die Routing-Tabelle auf den Routern manuell konfiguriert, wobei die Pfade zum Erreichen bestimmter Netze festgelegt werden. Es wird typischerweise in Szenarien verwendet, in denen Änderungen der Netzwerktopologie minimal oder vorhersehbar sind. Statische Routen sind einfach zu konfigurieren und können für kleine Netzwerke oder bestimmte Netzwerksegmente nützlich sein.

Eine Standardroute, die auch als Gateway der letzten Instanz bezeichnet wird, wird verwendet, wenn keine explizite Route für ein Zielnetz existiert. Sie fungiert als Auffangroute und wird auf Routern so konfiguriert, dass der Datenverkehr zu einem Standard-Gateway geleitet wird, wenn der Router keine Kenntnis über das Zielnetz hat.

## Administrative Entfernung, Exterior vs. Interior, und Time to Live

{{< youtube id="HR59xk4umWY" >}}

### Administrative Entfernung

Die administrative Distanz (AD) ist ein Wert, der Routing-Protokollen zugewiesen wird, um die Priorität von Routen zu bestimmen, wenn mehrere Protokolle auf einem Router laufen. Niedrigere Werte der administrativen Distanz bedeuten eine höhere Priorität für ein bestimmtes Routing-Protokoll. Zum Beispiel hat OSPF eine niedrigere AD (110) als RIP (120), so dass OSPF-Routen gegenüber RIP-Routen bevorzugt werden.

### Exterior vs. Interior Routing

Externe Routing-Protokolle, wie BGP, werden für den Austausch von Routing-Informationen zwischen autonomen Systemen (AS) verwendet. Sie übernehmen das Routing zwischen verschiedenen Organisationen und Dienstanbietern. Interne Routing-Protokolle wie RIP, OSPF und EIGRP hingegen werden für das Routing innerhalb eines autonomen Systems verwendet.

### Time to Live (TTL)

Time to Live (TTL) ist ein Feld in IP-Paketen, das die maximale Anzahl von Sprüngen angibt, die ein Paket durchlaufen kann, bevor es verworfen wird. Es verhindert, dass Pakete bei einer Routing-Schleife oder anderen Problemen unendlich lange im Netz zirkulieren. Jeder Router verringert den TTL-Wert, wenn das Paket das Netzwerk durchläuft.

## Bandbreitenmanagement

Ein effizientes Bandbreitenmanagement ist entscheidend für die Optimierung der Netzwerkleistung und die Gewährleistung eines reibungslosen Verkehrsflusses. Zwei wichtige Aspekte der Bandbreitenverwaltung sind Traffic Shaping und Quality of Service (QoS).

### Traffic Shaping

Traffic Shaping ist eine Technik zur Steuerung der Datenübertragungsrate in einem Netzwerk. Sie ermöglicht es Netzwerkadministratoren, den Datenverkehr zu steuern, indem sie Bandbreitenbeschränkungen festlegen und bestimmten Arten von Datenverkehr Vorrang einräumen. Auf diese Weise wird eine Überlastung des Netzes verhindert und sichergestellt, dass kritische Anwendungen ausreichend Bandbreite erhalten.

### Quality of Service (QoS)

Quality of Service (QoS) bezieht sich auf die Fähigkeit eines Netzwerks, Prioritäten zu setzen und Ressourcen für verschiedene Arten von Datenverkehr auf der Grundlage ihrer Bedeutung und Anforderungen zuzuweisen. QoS-Mechanismen wie Verkehrspriorisierung, Bandbreitenzuweisung und Staumanagement tragen dazu bei, eine optimale Leistung für Echtzeitanwendungen wie Sprache und Video zu gewährleisten.

{{< inarticle-dark >}}

## Gerätevergleich und Platzierung

Verschiedene Geräte spielen in einem Netzwerk bestimmte Rollen und haben unterschiedliche Eigenschaften, die sie für bestimmte Aufgaben geeignet machen. Im Folgenden werden wir einige gängige Netzwerkgeräte vergleichen und ihre geeignete Platzierung diskutieren:

- **Router**: Router sind für die Weiterleitung des Datenverkehrs zwischen verschiedenen Netzwerken zuständig. Sie arbeiten auf der Netzwerkschicht (Layer 3) und verwenden Routing-Protokolle, um den besten Pfad für die Datenübertragung zu ermitteln.

- **Switches**: Switches arbeiten auf der Datenübertragungsschicht (Schicht 2) und erleichtern die Kommunikation zwischen Geräten innerhalb eines lokalen Netzwerks (LAN). Sie verwenden MAC-Adressen, um Datenpakete an den vorgesehenen Empfänger weiterzuleiten.

- **Firewalls**: Firewalls schützen Netzwerke vor unbefugtem Zugriff und bösartigem Datenverkehr. Sie setzen Sicherheitsrichtlinien durch, indem sie den Netzwerkverkehr untersuchen und bestimmte Verbindungen auf der Grundlage vordefinierter Regeln zulassen oder blockieren.

- **Lastverteiler**: Load Balancer verteilen den eingehenden Netzwerkverkehr auf mehrere Server, um die Ressourcenauslastung zu optimieren, die Leistung zu verbessern und eine hohe Verfügbarkeit zu gewährleisten.

- **Zugangspunkte**: Access Points (APs) stellen drahtlose Verbindungen zu Geräten innerhalb eines Netzwerks her. Sie ermöglichen die drahtlose Kommunikation, indem sie Daten zwischen drahtlosen Geräten und dem kabelgebundenen Netzwerk übertragen und empfangen.

Die Platzierung dieser Geräte hängt von der Netzwerkarchitektur und den Anforderungen ab. **Router** werden in der Regel am Netzrand platziert, um den Datenverkehr zwischen Netzen abzuwickeln. **Switches** werden innerhalb von LANs eingesetzt, um Geräte zu verbinden und die lokale Kommunikation zu erleichtern. **Firewalls** werden zwischen den Netzen aufgestellt, um sie vor externen Bedrohungen zu schützen. **Lastverteiler** werden vor Webservern platziert, um den Datenverkehr effizient zu verteilen. **Access Points** werden strategisch platziert, um in den gewünschten Bereichen eine drahtlose Abdeckung zu gewährleisten.

______

## Schlussfolgerung

Das Verständnis von **Routing-Technologien und -Konzepten** ist für Netzwerkadministratoren und IT-Experten von entscheidender Bedeutung. **Dynamische Routing-Protokolle** wie **RIP, OSPF, EIGRP und BGP** automatisieren den Prozess des Austauschs von Routing-Informationen und passen sich an Netzwerkänderungen an. **Link-State-, Distanzvektor- und hybride Routing-Protokolle** bieten verschiedene Ansätze zur Ermittlung optimaler Routen. **Statisches Routing und Standardrouten** bieten manuelle Kontrolle über Routingentscheidungen. Techniken zur **Bandbreitenverwaltung** wie **Traffic Shaping und QoS** sorgen für eine effiziente Netzauslastung. Der Vergleich und die richtige Platzierung von Netzwerkgeräten verbessert die Netzwerkleistung und -sicherheit.

Durch die Beherrschung von **Routing-Technologien und -Konzepten** können Netzwerkadministratoren **robuste und effiziente Netzwerke** aufbauen, die den Anforderungen der modernen Konnektivität gerecht werden.

______