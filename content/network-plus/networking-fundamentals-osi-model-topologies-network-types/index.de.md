---
title: "Netzwerk-Plus-Kurs: Das OSI-Modell, Topologien und Netzwerktypen verstehen"
date: 2023-07-01
toc: true
draft: false
description: "Erkunden Sie die Bedeutung der Netzwerkgrundlagen, einschließlich des OSI-Modells, der Netzwerktopologien und der verschiedenen Netzwerktypen, für den Aufbau effizienter und zuverlässiger Infrastrukturen."
genre: ["Technologie", "Vernetzung", "IT-Infrastruktur", "Netzarchitektur", "Informatik", "Datenkommunikation", "Informationstechnologie", "Netzwerksicherheit", "Netzwerk-Management", "Internet"]
tags: ["Netzwerk-Grundlagen", "OSI-Modell", "Netzwerktopologien", "Netzwerktypen", "Datenkapselung", "Netzwerkschichten", "Maschentopologie", "Sterntopologie", "Bus-Topologie", "Ringtopologie", "Hybridtopologie", "Peer-to-Peer-Netzwerk", "Client-Server-Netzwerk", "LAN", "MAN", "WAN", "WLAN", "PAN", "CAN", "SAN", "SDWAN", "MPLS", "mGRE", "vSwitch", "vNIC", "NFV", "Hypervisor", "Satellitenverbindungen", "DSL", "Kabelinternet", "Mietleitung", "metro-optisch"]
cover: "/img/cover/A_symbolic_illustration_of_interconnected_nodes.png"
coverAlt: "Eine symbolische Darstellung von miteinander verbundenen Knoten, die ein Netz bilden."
coverCaption: "Entfesseln Sie die Kraft der Netzwerkgrundlagen."
---

#### [Click Here to Return To the Network Plus Course Page](/network-plus-start)

In der vernetzten Welt von heute spielen die Grundlagen der Vernetzung eine entscheidende Rolle. Ob beim Surfen im Internet, beim Versenden von E-Mails oder beim Streaming von Videos - all diese Aktivitäten sind auf eine robuste Netzwerkinfrastruktur angewiesen. In diesem Artikel geben wir einen Überblick über die **Grundlagen der Netzwerktechnik**, beginnend mit dem **OSI-Modell** und **Kapselungskonzepten**. Wir werden auch verschiedene **Netzwerktopologien** und ihre Eigenschaften untersuchen.

## Überblick über das OSI-Modell und Verkapselungskonzepte

Das **OSI (Open Systems Interconnection)-Modell** ist ein konzeptioneller Rahmen, der die Funktionen eines Netzwerks in sieben verschiedenen Schichten definiert. Jede Schicht hat spezifische Verantwortlichkeiten und interagiert mit den darüber und darunter liegenden Schichten. Das Verständnis des OSI-Modells ist wichtig, um zu verstehen, wie Daten über ein Netzwerk übertragen und verarbeitet werden.

### OSI-Modell-Schichten

{{< youtube id="G7aVKgGUe9c" >}}

1. **Schicht 1 - Physikalisch**: Die physikalische Schicht befasst sich mit der eigentlichen Übertragung und dem Empfang von Rohdatenströmen über physikalische Medien wie Kupferleitungen, Glasfaserkabel oder drahtlose Verbindungen.

2. **Schicht 2 - Datenverbindung**: Die Datenverbindungsschicht ist für den Aufbau und die Beendigung von Verbindungen zwischen Netzgeräten zuständig. Sie übernimmt auch die Fehlererkennung und -korrektur, um eine zuverlässige Datenübertragung zu gewährleisten.

3. **Schicht 3 - Netzwerk**: Die Netzwerkschicht erleichtert die Weiterleitung von Datenpaketen von der Quelle zum Ziel über mehrere Netzwerkknoten hinweg. Sie befasst sich mit Problemen im Zusammenhang mit **Netzüberlastung**, **Paketweiterleitung** und **IP-Adressierung**.

4. **Schicht 4 - Transport**: Die Transportschicht gewährleistet die **End-to-End-Datenübertragung** und stellt eine zuverlässige Kommunikation zwischen Quelle und Ziel her. Sie verwaltet **Datensegmentierung**, **Flusskontrolle** und **Fehlerbehebung**.

5. **Schicht 5 - Sitzung**: Die Sitzungsschicht baut Kommunikationssitzungen zwischen Anwendungen auf, unterhält sie und beendet sie. Sie verwaltet die **Dialogsteuerung** und die **Synchronisierung** zwischen Geräten.

6. **Schicht 6 - Präsentation**: Die Präsentationsschicht konzentriert sich auf die **Syntax** und **Semantik** der zwischen den Anwendungen ausgetauschten Informationen. Sie kümmert sich um **Datenverschlüsselung**, **Komprimierung** und **Formatierung** für die richtige Interpretation.

7. **Schicht 7 - Anwendung**: Die Anwendungsschicht stellt die eigentlichen Netzanwendungen und -dienste dar, die von den Endnutzern verwendet werden. Sie bietet Dienste wie **E-Mail**, **Dateitransfer**, **Browsing im Internet** und **Fernzugriff**.

{{< inarticle-dark >}}

### Datenkapselung und -entkapselung im Kontext des OSI-Modells

{{< youtube id="_fPzeQ9PHhA" >}}

Unter Datenkapselung versteht man das Hinzufügen von protokollspezifischen Headern und Trailern zu den Nutzdaten auf jeder Schicht des OSI-Modells. Diese Verkapselung ermöglicht es den Daten, das Netz zu durchqueren und das vorgesehene Ziel zu erreichen. Umgekehrt werden bei der Entkapselung die hinzugefügten Header und Trailer auf jeder Schicht des OSI-Modells entfernt, um die ursprüngliche Nutzlast zu extrahieren.

Im Kontext des OSI-Modells tragen die folgenden Elemente zur Datenkapselung und -entkapselung bei:

- **Ethernet-Header**: Der Ethernet-Header enthält Informationen wie die MAC-Adressen der Quell- und Zielgeräte, den Typ des Ethernet-Protokolls und Fehlerkontrollmechanismen.

- **Internet-Protokoll (IP)-Kopfzeile**: Der IP-Header enthält die Quell- und Ziel-IP-Adressen, die Paketidentifikation, die Time-to-Live und andere wichtige Parameter für die IP-basierte Kommunikation.

- **Transmission Control Protocol (TCP)/User Datagram Protocol (UDP)-Kopfzeilen**: TCP- und UDP-Header enthalten Portnummern, Sequenznummern, Prüfsummen und andere relevante Informationen, die für die Kommunikation auf der Transportschicht erforderlich sind.

- **TCP-Flaggen**: TCP-Flags kennzeichnen spezifische Kontrollfunktionen und Optionen während einer TCP-Sitzung. Dazu gehören Flags für den Aufbau von Verbindungen, die Bestätigung von Daten, das Beenden von Verbindungen und mehr.

- **Nutzlast**: Die Nutzdaten sind die eigentlichen Daten, die übertragen werden, z. B. eine Webseite, eine E-Mail-Nachricht oder eine Mediendatei.

- **Maximale Übertragungseinheit (MTU)**: Die MTU gibt die maximale Größe eines Datenpakets an, das ohne Fragmentierung über ein Netzwerk übertragen werden kann.

{{< inarticle-dark >}}

## Untersuchung von Netztopologien und ihren Merkmalen

{{< youtube id="zbqrNg4C98U" >}}

Netzwerktopologien definieren die physische oder logische Anordnung von Netzgeräten und die Verbindungen zwischen ihnen. Jede Topologie hat ihre eigenen Stärken und Schwächen, und die Wahl der richtigen Topologie hängt von verschiedenen Faktoren wie Skalierbarkeit, Fehlertoleranz und Kosten ab.

### Mesh-Topologie

In einer **Mesh-Topologie** ist jedes Gerät mit jedem anderen Gerät verbunden und bildet ein vollständig zusammenhängendes Netz. Diese Redundanz bietet eine hohe Fehlertoleranz, kann aber kostspielig und komplex in der Implementierung sein. Mesh-Topologien werden häufig in kritischen Infrastrukturen und Hochleistungscomputerumgebungen eingesetzt.

### Stern/Hub-und-Speichen-Topologie

Bei einer **Sterntopologie** sind alle Geräte an einen zentralen Hub oder Switch angeschlossen. Der Hub fungiert als zentraler Verbindungspunkt und erleichtert die Kommunikation zwischen den Geräten. Diese Topologie ist einfach zu verwalten und bietet eine zentrale Steuerung, kann aber bei einem Ausfall des Hubs zu einem Single Point of Failure führen.

### Bus-Topologie

In einer **Bustopologie** sind alle Geräte an eine einzige Kommunikationsleitung, den Bus, angeschlossen. Die Daten werden sequentiell über den Bus übertragen, und die Geräte empfangen die für sie bestimmten Daten. Bustopologien sind einfach und kostengünstig, können aber zu Netzwerküberlastungen führen und sind nur begrenzt skalierbar.

### Ring-Topologie

In einer **Ringtopologie** sind die Geräte in einer kreisförmigen Kette verbunden, wobei jedes Gerät mit dem nächsten und das letzte Gerät wieder mit dem ersten verbunden ist. Die Daten zirkulieren in einer Richtung durch den Ring. Ringtopologien bieten einen fairen Zugang und können hohe Verkehrslasten bewältigen, können aber durch den Ausfall eines Geräts zu Netzwerkunterbrechungen führen.

### Hybride Topologie

Eine **Hybridtopologie** kombiniert mehrere Topologien, um ein flexibleres und skalierbares Netz zu bilden. Beispielsweise kann eine Kombination aus Stern- und Ringtopologien Redundanz und Fehlertoleranz bieten und gleichzeitig die Skalierbarkeit erhalten.

## Netzwerktypen und -merkmale

{{< youtube id="6a-roIeJ_a4" >}}

Die Vernetzung umfasst verschiedene Netzwerktypen, die jeweils auf bestimmte Bedürfnisse und Anwendungsfälle zugeschnitten sind. Hier sind einige gängige Netzwerktypen:

### Peer-to-Peer (P2P) Netzwerk

In einem **Peer-to-Peer (P2P)-Netzwerk** verbinden sich Geräte direkt miteinander, ohne auf einen zentralen Server angewiesen zu sein. P2P-Netzwerke werden häufig für die gemeinsame Nutzung von Dateien, kollaborative Anwendungen und dezentrale Systeme verwendet.

### Client-Server-Netzwerk

Ein **Client-Server-Netzwerk** umfasst Clients, die Dienste oder Ressourcen anfordern, und Server, die diese Dienste oder Ressourcen bereitstellen. Client-Server-Netze sind in Unternehmensumgebungen weit verbreitet, in denen eine zentrale Steuerung und Ressourcenverwaltung unerlässlich sind.

### Lokales Netzwerk (LAN)

Ein **Local Area Network (LAN)** erstreckt sich über ein kleines geografisches Gebiet, wie z. B. ein Bürogebäude oder ein Haus. Es ermöglicht den Geräten innerhalb des Netzes zu kommunizieren und Ressourcen gemeinsam zu nutzen. LANs werden in der Regel für die interne Kommunikation, die gemeinsame Nutzung von Dateien und Druckern verwendet.

### Metropolitan Area Network (MAN)

Ein **Metropolitan Area Network (MAN)** deckt ein größeres geografisches Gebiet als ein LAN, aber ein kleineres als ein WAN ab. Es verbindet mehrere LANs innerhalb einer Stadt oder Großstadtregion. MANs werden häufig von Unternehmen genutzt, die eine Hochgeschwindigkeitsverbindung zwischen ihren Niederlassungen oder Standorten benötigen.

### Wide Area Network (WAN)

Ein **Weitverkehrsnetz (WAN)** erstreckt sich über ein großes geografisches Gebiet und verbindet mehrere LANs oder MANs über verschiedene Städte, Länder oder Kontinente hinweg. WANs stützen sich auf verschiedene Kommunikationstechnologien, wie Mietleitungen, Satelliten und optische Netze, um Daten über große Entfernungen zu übertragen.

### Drahtloses lokales Netzwerk (WLAN)

Ein **Wireless Local Area Network (WLAN)** bietet eine drahtlose Verbindung innerhalb eines begrenzten Bereichs, in der Regel mit Wi-Fi-Technologie. WLANs sind häufig in Wohnungen, Büros, Cafés und öffentlichen Räumen zu finden und ermöglichen es den Nutzern, ihre Geräte ohne physische Kabel anzuschließen.

### Personal Area Network (PAN)

Ein **Personal Area Network (PAN)** deckt einen kleinen Bereich ab, in der Regel innerhalb des Arbeitsplatzes oder der unmittelbaren Umgebung einer Person. Es ermöglicht die Kommunikation zwischen persönlichen Geräten, wie Smartphones, Tablets und tragbaren Geräten.

### Campus Area Network (CAN)

Ein **Campus Area Network (CAN)** ist ein Netzwerk, das sich über einen Universitätscampus oder einen großen Unternehmenscampus erstreckt. Es bietet Konnektivität zu verschiedenen Gebäuden und Einrichtungen innerhalb des Campusgeländes und erleichtert die Kommunikation und die gemeinsame Nutzung von Ressourcen.

### Storage Area Network (SAN)

Ein **Storage Area Network (SAN)** ist ein spezielles Netzwerk für Speicherzwecke. Es ermöglicht mehreren Servern den Zugriff auf gemeinsam genutzte Speicherressourcen, wie z. B. Festplatten-Arrays oder Bandbibliotheken, über eine Hochgeschwindigkeitsverbindung.

### Software-Defined Wide Area Network (SDWAN)

**Software-Defined Wide Area Network (SDWAN)** ist eine Technologie, die die Verwaltung und Konfiguration von WANs vereinfacht, indem sie die Steuerungsebene des Netzwerks von der zugrunde liegenden Hardware trennt. Sie bietet eine zentrale Steuerung und ermöglicht es Unternehmen, ihre WAN-Infrastruktur dynamisch zu verwalten.

### Multiprotocol Label Switching (MPLS)

**Multiprotocol Label Switching (MPLS)** ist eine Routing-Technik, die Etiketten verwendet, um Datenpakete effizient über ein Netzwerk weiterzuleiten. Es bietet eine leistungsstarke, zuverlässige und sichere Kommunikation und eignet sich daher für Dienstanbieter und Unternehmen.

### Multipoint Generic Routing Encapsulation (mGRE)

**Multipoint Generic Routing Encapsulation (mGRE)** ist eine Technik zur Schaffung virtueller privater Netze (VPNs), bei der Datenpakete eingekapselt und über ein Mehrpunktnetz gesendet werden. Sie ermöglicht eine effiziente Kommunikation zwischen mehreren Standorten oder Endpunkten.

{{< inarticle-dark >}}

## Virtuelle Netzwerkkonzepte

{{< youtube id="A29g5-Os-u8" >}}

Virtualisierungstechnologien haben die Art und Weise, wie Netzwerke entworfen und verwaltet werden, revolutioniert. Hier sind einige Konzepte für virtuelle Netzwerke:

### vSwitch

Ein **vSwitch** oder virtueller Switch ist ein softwarebasierter Netzwerk-Switch, der in einer virtualisierten Umgebung, z. B. einem Hypervisor, arbeitet. Er ermöglicht die Kommunikation zwischen virtuellen Maschinen (VMs) und verbindet sie mit dem physischen Netzwerk.

### Virtuelle Netzwerkschnittstellenkarte (vNIC)

Eine **virtuelle Netzwerkschnittstellenkarte (vNIC)** ist eine virtualisierte Netzwerkschnittstellenkarte, die einen physischen Netzwerkadapter innerhalb einer virtuellen Maschine emuliert. Sie ermöglicht VMs die Kommunikation mit dem virtuellen Switch und dem physischen Netzwerk.

### Netzwerkfunktionsvirtualisierung (NFV)

**Netzwerkfunktionsvirtualisierung (NFV)** ist ein Ansatz, bei dem Netzwerkfunktionen wie Firewalls, Router und Load Balancer virtualisiert werden, indem sie auf Standardservern statt auf dedizierten Hardwaregeräten ausgeführt werden. Er bietet Flexibilität, Skalierbarkeit und Kosteneinsparungen in der Netzwerkinfrastruktur.

### Hypervisor

Ein **Hypervisor** ist eine Softwareschicht, die die Erstellung und Verwaltung von virtuellen Maschinen ermöglicht. Er bietet eine Abstraktion der Hardware, so dass mehrere virtuelle Maschinen auf einem einzigen physischen Server laufen können.

## Anbieter-Links

{{< youtube id="M2cJtZXJrpE" >}}

Provider-Links beziehen sich auf die verschiedenen Arten von Konnektivitätsoptionen, die von Dienstanbietern angeboten werden. Hier sind einige gängige Anbieterlinks:

### Satellit

**Satellitenverbindungen** nutzen Kommunikationssatelliten, um Daten über große Entfernungen zu übertragen. Sie werden häufig in abgelegenen Gebieten eingesetzt, in denen andere Verbindungsmöglichkeiten begrenzt sind.

### Digital Subscriber Line (DSL)

**Digital Subscriber Line (DSL)** ist eine Technologie, die einen Hochgeschwindigkeits-Internetzugang über bestehende Telefonleitungen ermöglicht. Sie bietet schnellere Geschwindigkeiten als herkömmliche Wählverbindungen und ist sowohl im privaten als auch im geschäftlichen Umfeld weit verbreitet.

### Kabel

Das **Kabel**-Internet nutzt die gleichen Koaxialkabel, die auch für das Kabelfernsehen verwendet werden, um einen Hochgeschwindigkeits-Internetzugang zu ermöglichen. Es ist in Wohngebieten beliebt und bietet im Vergleich zu DSL höhere Geschwindigkeiten.

### Mietleitung

Eine **Mietleitung** ist eine dedizierte Punkt-zu-Punkt-Verbindung zwischen zwei Standorten. Sie bietet eine zuverlässige und sichere Verbindung und eignet sich daher für Unternehmen mit hohen Bandbreitenanforderungen.

### Metro-Optisch

**Metro-optische** Netze nutzen die Glasfasertechnologie, um Hochgeschwindigkeitsverbindungen innerhalb eines Ballungsgebiets bereitzustellen. Sie bieten eine hohe Bandbreite und niedrige Latenzzeiten, ideal für datenintensive Anwendungen.

______

Zusammenfassend lässt sich sagen, dass das Verständnis der Netzwerkgrundlagen entscheidend für den Aufbau und die Wartung zuverlässiger und effizienter Netzwerkinfrastrukturen ist. Das **OSI-Modell** bietet einen Rahmen, um zu verstehen, wie Daten über verschiedene Netzwerkschichten übertragen und verarbeitet werden. Darüber hinaus hilft das Wissen über **Netztopologien** beim Entwurf von Netzwerken, die bestimmte Anforderungen an Skalierbarkeit, Fehlertoleranz und Kosteneffizienz erfüllen. Indem wir uns mit verschiedenen **Netzwerktypen**, **virtuellen Netzkonzepten** und **Provider-Links** vertraut machen, können wir bei der Einrichtung und Verwaltung von Netzen fundierte Entscheidungen treffen.

Referenzen:
- [OSI Model - Cisco](https://learningnetwork.cisco.com/s/article/osi-model-reference-chart)
- [How Does the Internet Work? - Stanford University](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
