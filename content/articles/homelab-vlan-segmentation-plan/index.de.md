---
title: "VLAN-Segmentierung im Homelab planen und testen"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Erstelle einen VLAN-Plan für vertrauenswürdige Geräte, Server, IoT und Gäste. Erfasse erlaubten Datenverkehr, konfiguriere das Netzwerk schrittweise und prüfe die Isolation."
genre: ["Homelab", "Netzwerksicherheit", "Netzwerke"]
tags: ["Homelab-VLAN", "VLAN-Segmentierung", "IoT-Netzwerk", "Gastnetzwerk", "Homelab-Firewall", "Inter-VLAN-Routing", "802.1Q", "Netzwerkisolation", "VLAN-Test", "pfSense-VLAN", "Access-Port", "Trunk-Port", "Firewallregeln", "Homelab-Sicherheit", "Netzwerkplan", "Subnetz", "DHCP", "DNS", "Managed Switch", "WLAN-SSID"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Ein Homelab-Router und -Switch trennen Laptops, Server, IoT-Geräte und Gäste in geschützte Netzwerkzonen."
coverCaption: "Plane VLAN-Grenzen und teste anschließend jeden erlaubten und blockierten Pfad."
---

Ein Homelab verbindet Laptops, Server, Kameras und Gastgeräte oft mit demselben Netzwerk. **VLAN-Segmentierung** verteilt diese Gruppen auf getrennte Netzwerke. Ein Router, eine Firewall oder ein Layer-3-Switch leitet den Datenverkehr zwischen ihnen weiter. Firewallregeln oder Zugriffskontrolllisten auf dem Switch steuern diese gerouteten Verbindungen. Diese Anleitung hilft dir, den Plan zu erstellen, jeweils eine Änderung vorzunehmen und das Ergebnis zu prüfen.

## Wichtigste Erkenntnisse

- **Nach Vertrauen gruppieren:** Lege Verwaltungsgeräte, Server, IoT-Geräte und Gäste in getrennte Netzwerke, wenn sie unterschiedliche Zugriffsanforderungen haben.
- **Erlaubte Pfade festhalten:** Notiere für jede Verbindung zwischen Netzwerken Quelle, Ziel, Dienst und Grund.
- **Beide Ebenen konfigurieren:** Switch- und Access-Point-Einstellungen ordnen Geräte VLANs zu. Firewallregeln oder Zugriffskontrolllisten auf dem Switch steuern gerouteten Datenverkehr.
- **Beide Ergebnisse testen:** Prüfe aus jedem relevanten Netzwerk eine erlaubte und eine abgelehnte Verbindung.

## Vor dem Start

Du brauchst einen Router oder eine Firewall mit VLAN-Schnittstellen oder einen Layer-3-Switch, der VLAN-Routing und Zugriffskontrolllisten unterstützt. Ein Managed Switch transportiert die kabelgebundenen VLANs. Wenn du WLAN-Clients trennst, brauchst du außerdem einen Access Point mit WLAN-Netzwerken, die VLANs zugeordnet sind. Lass während der Konfigurationsänderung ein Gerät im aktuellen Verwaltungsnetzwerk. Sichere zuerst die Einstellungen des Routers, Switches und Access Points. Die folgenden Schritte verwenden einen **Beispielplan**. Passe Adressen und Ports an deine Geräte an.

Eine **VLAN-Schnittstelle** verbindet das Gateway mit einem VLAN. Das Gateway kann ein Router, eine Firewall oder ein Layer-3-Switch sein. Ein **DHCP-Bereich** ist der Adressbereich, den ein DHCP-Dienst den Geräten dort anbietet. Ein **DHCP-Relay** leitet Adressanfragen aus einem VLAN an einen DHCP-Server in einem anderen Netzwerk weiter. Verwende ein Relay, wenn das Gateway für dieses VLAN keine Adressen vergibt und der DHCP-Server an anderer Stelle steht. Junipers [Anleitung zum DHCP-Relay](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) beschreibt diesen Weg. Eine WLAN-**SSID** ist der Netzwerkname, mit dem sich Clients verbinden. Falls deine Geräte keinen Managed Switch oder VLAN-fähigen Access Point haben, beginne mit dem integrierten Gastnetzwerk und prüfe dessen Isolation, bevor du Geräte kaufst oder austauschst.

Wenn du zuerst die Grundbegriffe brauchst, lies [Subnetze und VLANs](/articles/networking-basics-what-are-subnets-and-vlans/). Der [Leitfaden zur Netzwerksegmentierung](/articles/how-to-perform-network-segmentation-for-improved-security/) auf dieser Website behandelt das umfassendere Sicherheitskonzept. CISA beschreibt getrennte Heimnetzwerke für Gäste und Internet-of-Things-Geräte in der [Federal-Mobile-Workplace-Security-Anleitung](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Warnung:** Eine VLAN-Änderung am Port deiner Verwaltungsverbindung kann dich aussperren. Sorge für physischen Zugriff und einen bekannten Wiederherstellungsweg, bis jedes Netzwerk seine Tests besteht.

Exportiere vor dem Umstecken eines Kabels die Konfiguration jedes Geräts. Notiere außerdem die aktuelle Verwaltungs-IP-Adresse, den Switch-Port, die VLAN-Einstellung und die Administratoranmeldung. Lass einen bewährten Verwaltungsport und einen Laptop im ursprünglichen Netzwerk. Falls eine Änderung den Zugriff unterbricht, verbinde den Laptop wieder mit diesem Port, stelle die gespeicherte Einstellung oder Konfiguration wieder her und prüfe, ob das alte Gateway antwortet, bevor du es erneut versuchst. Wenn der Switch keinen erreichbaren Verwaltungsweg hat, nutze die dokumentierte Konsole oder das lokale Wiederherstellungsverfahren. Setze Geräte erst zurück, wenn du weißt, welche Daten beim Zurücksetzen gelöscht werden.

## Geräte und Datenflüsse erfassen

Liste jedes Gerät mit aktueller Adresse, Besitzer und benötigten Diensten auf. Lege für jeden Zugriff auf ein anderes Netzwerk einen Grund fest. Ein Laptop könnte beispielsweise einen Server verwalten, während eine Kamera nur einen Rekorder und einen DNS-Server erreichen muss. Ein Gasttelefon braucht Internetzugriff, aber keinen Zugriff auf Server.

| Gerätegruppe | Beispiele | Erforderlicher Zugriff |
|---|---|---|
| **Verwaltung** | Admin-Laptop, Verwaltungsoberflächen von Switch und Access Point | Router-, Switch-, Access-Point- und Serververwaltung |
| **Server** | Hypervisor, NAS, Sicherungsziel | Updates, DNS, genehmigter Anwendungsverkehr |
| **IoT** | Kameras, Smart-Plugs, Mediengeräte | DNS, Zeitdienst, bestimmter Controller oder Rekorder |
| **Gäste** | Telefone und Laptops von Besuchern | Internet, DNS, keine privaten Subnetze |

Halte Ausnahmen fest, bevor du Regeln hinzufügst. Lokale Erkennungsfunktionen wie Casting verwenden oft Multicast-Verkehr, der eine geroutete Grenze standardmäßig nicht überquert. Öffne nicht den gesamten Verkehr zwischen VLANs, um ein einzelnes Erkennungsproblem zu beheben. Ermittle das Protokoll und füge die kleinste unterstützte Ausnahme hinzu.

## VLANs und Adressen zuweisen

Weise jeder Gruppe eine VLAN-ID und ein eigenes IP-Subnetz zu. Dieser **Beispielplan** verwendet für Dokumentationen reservierte Adressen und setzt voraus, dass der Router DHCP und DNS bereitstellt. Übernimm die Tabelle nicht in ein aktives Netzwerk, ohne zuvor Adresskonflikte zu prüfen.

| Netzwerk | VLAN-ID | Subnetz | Beispielgateway |
|---|---:|---|---|
| **Verwaltung** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Server** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Gäste** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Diese reservierten Dokumentationsbereiche veranschaulichen nur den Aufbau gemäß [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Verwende für dein tatsächliches Lab private Adressen aus [RFC 1918](https://www.rfc-editor.org/info/rfc1918) mit einem nicht überlappenden Subnetz pro VLAN. Notiere jedes reale Gateway, jeden DHCP-Pool, jede DNS-Adresse und jede Gerätezuordnung in deinem Plan.

**Access-Ports** transportieren das Netzwerk eines einzelnen Geräts ohne VLAN-Tag. **Trunk-Ports** transportieren ausgewählte getaggte VLANs zwischen Router, Switch und Access Point. Stimme VLAN-ID und native beziehungsweise untagged-Einstellung an beiden Enden ab. Netgates [VLAN-Switch-Anleitung](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) erklärt getaggte Trunk-Ports, ungetaggte Access-Ports und Port-VLAN-IDs. Verwende VLAN 1 möglichst nicht standardmäßig für die Verwaltung, wenn deine Hardware ein separates VLAN unterstützt, wie Netgate in den [VLAN-Sicherheitshinweisen](https://docs.netgate.com/pfsense/en/latest/vlan/security.html) beschreibt.

**Native** oder **untagged** Datenübertragung auf einem Trunk trägt kein VLAN-Tag. Beide Enden müssen sie demselben VLAN zuordnen, sonst kann ein Gerät im falschen Netzwerk landen. Erlaube nur VLANs, die der Link benötigt. Deaktiviere ungenutzte Switch-Ports oder weise sie einem eingeschränkten Netzwerk zu. Netgate rät außerdem davon ab, ein VLAN als vollständige Sicherheitsgrenze zu behandeln, wenn ein Angreifer einen Switch-Port kontrolliert. Schütze physische Ports und Gerätezugangsdaten ebenso wie den gerouteten Verkehr.

## Verkehrsmatrix erstellen

Ein VLAN trennt zunächst nur Broadcast-Domänen. **Inter-VLAN-Routing** auf dem Router oder Layer-3-Switch benötigt weiterhin Zugriffsregeln. Lege fest, welches Gerät den Verkehr zwischen VLANs routet. Wenn ein Layer-3-Switch lokal routet, erreicht der Verkehr zwischen seinen VLANs die Router-Firewall möglicherweise nie. Wende gleichwertige Zugriffskontrolllisten auf dem Switch an oder route über die Firewall. Teste anschließend am tatsächlichen Kontrollpunkt. Prüfe die Richtung der Switch-ACL und ob sie Verbindungszustände verfolgt. Viele Switch-ACLs gleichen Pakete in jeder Richtung getrennt ab, sodass eine erlaubte Verbindung eine eng gefasste Regel für Rückverkehr braucht. Cisco beschreibt in der [ACL-Anleitung](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) die Schnittstellenrichtung und die geordnete Paketprüfung. Halte anhand der Geräteliste fest, welche Verbindungen erlaubt sein sollen. Die folgenden Einträge sind Beispiele, keine allgemeingültige Regelmenge.

| Quelle | Ziel | Dienst | Entscheidung |
|---|---|---|---|
| **Verwaltung** | Server-Verwaltungsoberfläche | TCP 443 | Für genehmigte Verwaltungsgeräte zulassen |
| **Verwaltung** | Verwaltungsoberflächen von Router, Switch und Access Point | Dokumentierte Verwaltungsports | Für genehmigte Verwaltungsgeräte zulassen |
| **IoT** | Kamera-Rekorder | Dokumentierter Rekorder-Port | Nur bei Bedarf zulassen |
| **IoT** | Genehmigter DNS- und Zeitdienst | DNS und NTP | Nur zu den ausgewählten Diensten zulassen |
| **IoT** | Verwaltungs-Subnetz | Beliebig | Verweigern |
| **Gäste** | Private Subnetze | Beliebig | Verweigern |
| **Gäste** | DNS und Internet | DNS, Webverkehr | Über genehmigten Resolver und Gateway zulassen |

Nimm auch die Dienste des Routers selbst in den Plan auf. Eine Regel, die den IoT-Zugriff auf andere VLANs blockiert, lässt möglicherweise weiterhin die Verwaltungsoberfläche des Routers erreichbar. Beschränke Verwaltungsdienste auf das Verwaltungsnetzwerk. Beginne nur mit den benötigten Zulassungsregeln und einer standardmäßigen Verweigerung für anderen gerouteten Verkehr. Prüfe vorhandene weit gefasste Zulassungsregeln, bevor du annimmst, dass die Standardeinstellung alles verweigert. Netgates [Firewall-Best-Practices](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) weisen darauf hin, dass ein Standard-pfSense-LAN eine Zulassungsregel hat. Wenn du pfSense verwendest, erklärt die [Regelmethodik](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html), dass Schnittstellenregeln eingehenden Verkehr filtern und zugelassene Verbindungen einen Zustand für Rückverkehr anlegen.

Die Beispieltabelle deckt IPv4 ab. Wenn dein Netzwerk IPv6 verwendet, weise jedem VLAN ein IPv6-Präfix und eine Richtlinie zu, prüfe Router Advertisements und teste ebenfalls erlaubte und verweigerte IPv6-Pfade. Eine IPv4-Sperre beweist keine IPv6-Isolation. Wenn du IPv6 nicht routen willst, prüfe die IPv6-Einstellungen des Routers und die Client-Adressen, statt anzunehmen, dass IPv6 fehlt. Netgate dokumentiert [IPv6-Firewallverhalten](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) und [Router Advertisements](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Ein Netzwerk nach dem anderen konfigurieren

1. Wähle das Gateway für das VLAN. Wenn Router oder Firewall routen, erstelle dort eine VLAN-Schnittstelle und weise ihr die Gateway-Adresse zu. Wenn ein Layer-3-Switch routet, erstelle die VLAN-Schnittstelle auf diesem Switch. Richte einen DHCP-Bereich am Gateway oder ein DHCP-Relay zu deinem vorhandenen DHCP-Server ein. Prüfe, ob ein genehmigter DNS-Resolver erreichbar ist. Netgates [VLAN-Konfigurationsanleitung](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) führt die Schnittstellen- und Dienstschritte für ein pfSense-Gateway auf.
2. Wenn der Router das VLAN-Gateway ist, füge das VLAN dem Router-Switch-Trunk hinzu. Wenn der Layer-3-Switch das Gateway ist, verwalte dessen Gateway-Adresse für das VLAN auf dem Switch und route über ein separates Transitnetz oder einen gerouteten Uplink zum Router oder zur Firewall. Lege am Switch eine Standardroute zum Upstream-Router fest. Lege am Router für jedes Switch-eigene VLAN eine Rückroute über den Switch an. Prüfe Firewallrichtlinie und ausgehendes NAT des Routers für diese Subnetze, wenn sie Internetzugang benötigen. Richte nicht dieselbe Gateway-Adresse oder denselben DHCP-Bereich auf beiden Geräten ein. Füge das VLAN dem relevanten Switch-Access-Point-Trunk hinzu, wenn WLAN-Clients das Netzwerk benötigen. Cisco zeigt in der [Inter-VLAN-Routing-Anleitung](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) Switch-eigene VLAN-Gateways. Netgate dokumentiert [Rückrouten](https://docs.netgate.com/pfsense/en/latest/routing/static.html) und [ausgehendes NAT](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) für Netzwerke hinter einem internen Router.
3. Weise dem VLAN einen Test-Access-Port oder eine WLAN-SSID zu. Verbinde ein unkritisches Testgerät mit diesem Port oder dieser SSID.
4. Füge die geplanten Firewallregeln oder Switch-ACLs auf dem Gerät hinzu, das das VLAN routet. Prüfe, dass anderer gerouteter Verkehr verweigert wird. Wenn der Switch keine Zustände verfolgt, prüfe ACL-Richtung und Rückverkehr. Teste den Zugriff auf jedes Gateway, jede Verwaltungsoberfläche, jedes lokale Subnetz und gegebenenfalls IPv6. Erlaube nur die Pfade aus deiner Verkehrsmatrix. Beschränke die Verwaltung auf das Verwaltungsnetzwerk. Prüfe die Regelreihenfolge und entferne oder verenge vorhandene weit gefasste Zulassungsregeln erst, wenn der Verwaltungs-Testpfad funktioniert.
5. Prüfe, ob das Testgerät eine Adresse, ein Gateway und einen DNS-Server aus dem vorgesehenen Subnetz erhält. Führe anschließend die unten aufgeführten Verbindungstests aus, bevor du weitere Geräte verschiebst.

Verschiebe das letzte Verwaltungsgerät erst, wenn sein Ersatzpfad funktioniert. Sichere die funktionierende Konfiguration, nachdem jedes Netzwerk die Tests bestanden hat. Wenn DHCP, DNS oder Verwaltungszugriff ausfällt, verbinde das Testgerät wieder mit dem ursprünglichen Port oder der ursprünglichen SSID. Stelle die letzte Switch- oder Routeränderung aus der gespeicherten Konfiguration wieder her und teste das ursprüngliche Netzwerk erneut, bevor du fortfährst.

## Isolation und Zugriff testen

Verwende einen Dienst, den du kontrollierst und von dem du weißt, dass er am Ziel lauscht. Ersetze auf einem Windows-Testgerät die Beispieladresse und den Port durch einen echten Server und führe Folgendes aus:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Das Feld **`TcpTestSucceeded`** zeigt an, ob eine TCP-Verbindung zustande kam. Microsofts [Referenz zu Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) dokumentiert die Parameter `-ComputerName` und `-Port`. Eine fehlgeschlagene Verbindung beweist allein nicht, dass eine Firewallregel gegriffen hat. Der Dienst ist möglicherweise ausgefallen oder die Host-Firewall blockiert den Verkehr. Prüfe den Zieldienst und das Netzwerk-Firewallprotokoll, bevor du Schlussfolgerungen ziehst.

Teste von einem Gerät aus, das tatsächlich mit jedem Quell-VLAN verbunden ist. Notiere vor jedem Test Quelladresse, Gateway und DNS-Server. Prüfe eine erlaubte Verbindung zum vorgesehenen Dienst, eine verweigerte Verbindung zu einem internen Dienst außerhalb der Matrix, eine DNS-Abfrage über den vorgesehenen Resolver und gegebenenfalls den Internetzugang. Prüfe bei einem Switch-eigenen VLAN die Standardroute des Switches, die Rückroute des Routers und den Rückweg vom Ziel, falls eine erlaubte Verbindung fehlschlägt. Wiederhole erlaubte und verweigerte Tests mit IPv6-Adressen, wenn IPv6 aktiv ist. Unter pfSense zeigt **Status > System Logs > Firewall** protokollierte Zulassungen oder Blockierungen. Netgates [Firewall-Protokollanleitung](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) beschreibt diese Ansicht. Vergleiche Quelle, Ziel, Port und Regel im Protokoll mit deinem Test. Wenn der Test unerwartet erfolgreich ist, prüfe weit gefasste Zulassungsregeln und vorhandene Zustandseinträge. Starte nach einer Regeländerung eine neue Verbindung, da eine bestehende Verbindung über ihren vorhandenen Zustand weiter funktionieren kann.

Führe zur DNS-Prüfung unter Windows `nslookup example.com` aus und vergleiche den angezeigten Server mit dem vorgesehenen Resolver. Teste anschließend eine Abfrage von einem Gast- oder IoT-Client, für den DNS beschränkt ist. Eine erfolgreiche Abfrage beweist allein nicht, dass der Client den gewählten Resolver verwendet hat. Prüfe daher den angezeigten Server und ein Firewall- oder Resolver-Protokoll. Teste den direkten Zugriff eines IoT- oder Gastgeräts auf die Verwaltungsadresse des Routers als gesonderten verweigerten Fall.

Geräte im **selben VLAN** tauschen möglicherweise Daten aus, ohne die Router-Firewall zu passieren. Teste die lokale Client-Isolation separat, falls dein Access Point sie anbietet, und verwende Host-Firewalls auf Servern. Inter-VLAN-Firewalltests belegen keine Isolation innerhalb desselben VLANs.

> **Erwartetes Ergebnis:** Jedes Gerät erhält eine Adresse aus seinem geplanten Subnetz. Erlaubte Dienste funktionieren. Verweigerte Versuche stimmen mit einer Firewallblockierung oder einer dokumentierten gleichwertigen Kontrolle überein.

## Fehlerbehebung

- **Keine Adresse:** Prüfe das VLAN des Access-Ports oder der SSID, Trunk-Tags, den DHCP-Bereich und die Gateway-Schnittstelle.
- **Adresse funktioniert, DNS nicht:** Prüfe die Resolver-Adresse, die Dienstbindung am Router und die Firewallregel für DNS-Verkehr.
- **Ein Gerät erreicht unerwartet ein anderes VLAN:** Prüfe Routerregeln, weit gefasste Zulassungsregeln und ob beide Geräte noch dasselbe ungetaggte Netzwerk nutzen.
- **Kein Firewallprotokoll für gerouteten Verkehr:** Prüfe, ob ein Layer-3-Switch oder ein anderes Gateway die Verbindung geroutet hat, bevor sie die Firewall erreichte.
- **Ein Switch-eigenes VLAN erreicht lokale Netzwerke, aber nicht das Internet:** Prüfe die Standardroute des Switches, Rückrouten am Router, Firewallrichtlinie und ausgehendes NAT für das VLAN-Subnetz.
- **IPv4 wird blockiert, die Verbindung funktioniert trotzdem:** Prüfe IPv6-Adressen, Router Advertisements, IPv6-Regeln und vorhandene Zustandseinträge.
- **Ein verweigerter Test läuft ohne Firewallprotokoll in einen Timeout:** Bestätige, dass der Zieldienst lauscht. Prüfe anschließend Routing und Protokollierungseinstellungen. Netgates [Firewall-Fehlerbehebungsanleitung](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) beschreibt Prüfungen von Protokollen und Zuständen.
- **Casting oder Erkennung funktioniert nicht mehr:** Ermittle das Erkennungsprotokoll und den Controller-Pfad, bevor du eine eng begrenzte Ausnahme hinzufügst.

## Nächste Schritte

Bewahre die Geräteliste und Verkehrsmatrix zusammen mit deinem Netzwerkdiagramm auf. Prüfe die Regeln, wenn du einen Server oder ein IoT-Gerät hinzufügst. Wiederhole nach jeder relevanten Netzwerkänderung einen erlaubten und einen verweigerten Verbindungstest. Zu den umfassenderen Gestaltungsprinzipien kehrst du über [Netzwerksegmentierung](/articles/how-to-perform-network-segmentation-for-improved-security/) zurück.
