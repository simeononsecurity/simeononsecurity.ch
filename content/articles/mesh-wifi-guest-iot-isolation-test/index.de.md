---
title: "Gast- und IoT-Isolierung in einem Mesh-WLAN testen"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Prüfen Sie, ob Gast- und IoT-Netze Ihres Mesh-WLANs den Zugriff auf Ihre Heimgeräte blockieren. Testen Sie jedes Netz mit einem funktionierenden Dienst und halten Sie die Grenzen fest."
genre: ["Heimnetzwerke", "WLAN-Sicherheit", "Smart Homes"]
tags: ["Mesh-WLAN-Gastnetz", "Gastnetz-Isolierungstest", "IoT-Netzwerkisolierung", "Mesh-WLAN-Sicherheit", "Client-Isolierung", "Gast-WLAN-Test", "IoT-SSID", "Access-Point-Modus", "Router-Modus", "LAN-Zugriff", "lokaler Netzwerktest", "Deco-Gastnetz", "Orbi-Gastnetz", "ASUS-Gastnetz", "Google-Nest-Gast-WLAN", "Test-NetConnection", "TCP-Konnektivitätstest", "Smart-Home-Netzwerk", "drahtlose Client-Isolierung", "Heimnetzwerksegmentierung"]
cover: "/img/cover/mesh-wifi-guest-iot-isolation-test.webp"
coverAlt: "Ein zweistöckiges Haus mit zwei Mesh-Routern, Gasttelefonen, IoT-Lampen und Kameras sowie einem Schild, das den Weg zu einem vertrauenswürdigen Laptop und NAS blockiert."
coverCaption: "Testen Sie die Pfade zwischen Gast-, IoT- und Hauptnetz getrennt."
---

Ein eigener WLAN-Name zeigt nicht, welche Geräte miteinander kommunizieren. Ein Mesh-System behandelt möglicherweise das **Gastnetz**, das **IoT-Netz** und die **drahtlose Client-Isolierung** als unterschiedliche Kontrollen. Mit dieser Anleitung testen Sie die Pfade auf Ihren eigenen Geräten, ohne anzunehmen, dass die Bezeichnung des Herstellers Ihre Richtlinie beschreibt.

<!--more-->

## Wichtigste Punkte

- **Prüfen Sie zuerst, ob das Ziel funktioniert:** Greifen Sie aus dem Hauptnetz auf einen bekannten Dienst zu, bevor Sie einen blockierten Pfad testen.
- **Testen Sie jede Grenze:** Gast zu Hauptnetz, IoT zu Hauptnetz und Gast zu Gast beantworten unterschiedliche Fragen.
- **Halten Sie die Konfiguration fest:** Modell, Firmware, Router- oder Access-Point-Modus und der verbundene Mesh-Knoten beeinflussen die Auswertung.
- **Testen Sie nach Änderungen erneut:** Ein eindeutiges Ergebnis gilt nur für die getesteten Geräte, den Dienst, die Adressfamilie und die Konfiguration.

## Vorbereitung

Planen Sie etwa 20 Minuten ein. Sie benötigen einen Laptop, der sich mit Ihrem Haupt-, Gast- und IoT-WLAN verbinden lässt. Außerdem brauchen Sie ein vertrauenswürdiges Gerät im Hauptnetz mit einem **bekanntermaßen offenen TCP-Dienst**, zum Beispiel der Weboberfläche eines NAS. Ein TCP-Dienst ist ein Netzwerkdienst, der an einem nummerierten Port lauscht, etwa Port 443 einer NAS-Webseite. Verwenden Sie einen Dienst, der Ihnen gehört oder den Sie verwalten. Notieren Sie seine lokale Adresse und den Port, aber veröffentlichen Sie beides nicht. Lassen Sie den Dienst während des gesamten Tests laufen.

Notieren Sie Mesh-Modell, Firmwareversion, Betriebsmodus und Einstellungen für Gastzugriff, IoT-Zugriff, freigegebene Geräte und Client-Isolierung. Prüfen Sie nach jedem WLAN-Wechsel den WLAN-Namen des Laptops. Wenn Ihre übliche Richtlinie die Änderung erlaubt, trennen Sie VPN oder Proxy für diesen lokalen Pfadtest und aktivieren Sie die Verbindung anschließend wieder. Ein VPN ändert den getesteten Pfad.

> **Warnung:** Testen Sie nur eigene Geräte oder Geräte, die Sie verwalten dürfen. Die Anmeldeseite des Routers ist kein guter Ersatz für einen Host im Hauptnetz, da für den Zugriff auf das Gateway andere Regeln gelten.

Ein **lokales Netzwerk (LAN)** ist Ihr privates Heimnetz. **IoT**, das Internet der Dinge, umfasst Geräte wie Kameras, Lautsprecher und intelligente Steckdosen. Die **Client-Isolierung** blockiert direkten Datenverkehr zwischen Geräten in einem WLAN.

## Grenze festlegen

Legen Sie vor einer Einstellungsänderung das gewünschte Ergebnis fest. Internetzugriff und lokaler Zugriff sind getrennte Ergebnisse.

| Pfad | Zu beantwortende Frage | Beispiel für ein erwartetes Ergebnis |
|---|---|---|
| **Gast zum Haupt-LAN** | Ist ein Computer oder NAS erreichbar? | Blockiert, außer eine Ausnahme wurde eingerichtet |
| **IoT zum Haupt-LAN** | Sind private Geräte erreichbar? | Abhängig vom Produkt und Ihrer Richtlinie |
| **Gast zu Gast** | Ist ein Gastgerät vom anderen erreichbar? | Abhängig von der Client-Isolierung |
| **Gast zu freigegebenem Gerät** | Funktioniert ein freigegebener Drucker oder Bildschirm? | Nur erlaubt, wenn beabsichtigt |
| **Gast zum Internet** | Ist eine gewöhnliche öffentliche Website erreichbar? | Erlaubt, wenn Ihre Gastregel Internetzugriff vorsieht |

Diese Zeilen sind getrennte Tests. TP-Links [Deco-Anleitung zur Geräteisolierung](https://www.tp-link.com/us/support/faq/3968/) besagt, dass isolierte Geräte weiterhin Internetzugriff und Kommunikation mit anderen isolierten Geräten haben, während der Zugriff auf Geräte im Hauptnetz blockiert wird. ASUS beschreibt in der [Anleitung zur AP-Isolierung](https://www.asus.com/us/support/faq/1044821/) eine Funk-Peer-Kontrolle und weist darauf hin, dass ein Pfad über einen vorgeschalteten kabelgebundenen Router außerhalb dieser Kontrolle liegt. **Ein blockierter Pfad beweist nicht, dass auch alle anderen Grenzen greifen.**

## Mesh-Einstellungen prüfen

Suchen Sie die Funktion, die die zu testende Grenze kontrolliert. Menünamen und Verfügbarkeit unterscheiden sich je nach Modell und Firmware.

| Mesh-Einstellung | Zu prüfen |
|---|---|
| **TP-Link-Deco-Gastnetz** | Im [Routermodus wird das Gastnetz vom Hauptnetz isoliert](https://www.tp-link.com/us/support/faq/1460/). Prüfen Sie im Access-Point-Modus **Allow Local Access**. |
| **ASUS-Gastprofil** | [Access Intranet](https://www.asus.com/uk/support/faq/1009857/) steuert bei unterstützten Profilen den Zugriff auf das Hauptnetz. |
| **Google-Nest-Gast-WLAN** | Prüfen Sie die Liste [freigegebener Geräte](https://support.google.com/googlehome/answer/6327302?hl=en), bevor Sie davon ausgehen, dass ein Drucker oder Bildschirm verborgen bleibt. |
| **IoT-Netz oder Geräteisolierung** | Prüfen Sie, ob das Produkt eine eigene Isolierungskontrolle bietet. Ein IoT-WLAN-Name legt die Zugriffsregel nicht fest. |

Bei Deco setzt die [Geräteisolierung](https://www.tp-link.com/us/support/faq/3968/) Unterstützung durch Haupt- und Satelliteneinheiten voraus. Notieren Sie, welcher Knoten den Testlaptop versorgt. Fehlt eine Funktion, prüfen Sie die Dokumentation für das genaue Modell und die Firmware, statt anzunehmen, dass die App-Ansicht eines anderen Besitzers zu Ihrer passt.

## Positivkontrolle einrichten

Verbinden Sie den Windows-Testlaptop mit dem **Haupt-WLAN**. Prüfen Sie, ob der gewählte Dienst auf diesem Laptop funktioniert. Geben Sie in PowerShell nach Aufforderung die Adresse des Hosts im Hauptnetz und dessen bekannten offenen Port ein:

```powershell
$targetAddress = Read-Host "Main-network test host address"
$targetPort = [int](Read-Host "Known open TCP port")
Test-NetConnection -ComputerName $targetAddress -Port $targetPort
```

Microsoft beschreibt in der [Dokumentation zu Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) `-ComputerName` und `-Port` als Test für einen bestimmten Host und TCP-Dienst. Notieren Sie `TcpTestSucceeded`. Stellen Sie hier zuerst `True` fest, bevor Sie ein späteres `False` auswerten. Schlägt der Test im Hauptnetz fehl, liegt das Problem möglicherweise beim Dienst, der Adresse, der Host-Firewall oder der Laptop-Konfiguration. Beheben Sie zuerst den Test im Hauptnetz.

Wenn Sie ein Telefon oder ein anderes Betriebssystem verwenden, öffnen Sie denselben bekannten Dienst im Browser oder in der App. Verwenden Sie beim Wechsel des WLANs weiterhin genau denselben Dienst und dieselbe Zieladresse. Eine Geräteliste zur Erkennung liefert schwächere Belege, weil Erkennungsverkehr und direkter TCP-Zugriff unterschiedliche Pfade nutzen.

## Gast- und IoT-Zugriff testen

Verbinden Sie denselben Laptop mit dem **Gast-WLAN**. Prüfen Sie den WLAN-Namen. Rufen Sie eine öffentliche Website auf, wenn Ihre Gastregel Internetzugriff vorsieht. Führen Sie denselben Befehl `Test-NetConnection` erneut aus, ohne `$targetAddress` oder `$targetPort` zu ändern. Notieren Sie das Ergebnis.

Wechseln Sie zurück ins Hauptnetz und prüfen Sie, ob der Dienst weiterhin `True` liefert. Schlägt der Test im Hauptnetz nun fehl, ist das Gast-Ergebnis nicht aussagekräftig. Verbinden Sie den Laptop anschließend mit dem **IoT-WLAN**, sofern Ihr System einen Laptop zulässt, und wiederholen Sie den Test. Nehmen Sie nicht an, dass das IoT-Ergebnis dem Gast-Ergebnis entspricht. Ein erfolgreicher Zugriff von IoT auf das Hauptnetz bedeutet, dass der gewählte lokale TCP-Dienst in dieser Konfiguration aus dem IoT-Netz erreichbar war.

Wenn Gäste voneinander isoliert sein sollen, verwenden Sie zwei eigene Geräte im Gastnetz. Testen Sie von einem Gerät einen bekannten Dienst auf dem anderen. Halten Sie dies getrennt vom Zugriff der Gäste auf das Hauptnetz fest. Soll ein freigegebener Drucker oder Bildschirm funktionieren, testen Sie auch diese vorgesehene Ausnahme. Die Cloud-Steuerung eines Smart-Home-Geräts belegt keinen direkten lokalen Pfad.

Wiederholen Sie den Test Gast zu Hauptnetz in der Nähe jedes Mesh-Knotens. Prüfen Sie in der App, welcher Knoten den Laptop versorgt, falls die App diese Angabe zeigt. **IPv6** ist die neuere Internetprotokoll-Adressfamilie mit 128-Bit-Adressen. Unterstützt der Host im Hauptnetz IPv6 und ist die Positivkontrolle über IPv6 erfolgreich, wiederholen Sie denselben Test mit dieser Adressfamilie über Gast- und IoT-WLAN. Ein Test nur mit IPv4 deckt keinen IPv6-Pfad ab.

## Abweichungen auswerten

| Beobachtung | Nächste Prüfung |
|---|---|
| **Hauptnetz und Gastnetz schlagen fehl** | Prüfen Sie Zieldienst, Adresse, Port und Host-Firewall. Eine Isolierung ist nicht nachgewiesen. |
| **Hauptnetz und Gastnetz sind erfolgreich** | Prüfen Sie lokale Gastzugriffe, Ausnahmen für freigegebene Geräte sowie Router- und Access-Point-Modus. |
| **Hauptnetz erfolgreich, Gastnetz schlägt fehl** | Halten Sie die Belege für dieses Ziel und diesen TCP-Pfad fest. Testen Sie weitere Pfade, die Ihre Richtlinie verlangt. |
| **Gastnetz blockiert, IoT erfolgreich** | Prüfen Sie, ob das IoT-Netz nur ein Kompatibilitätsnetz ohne passende Isolierungsregel ist. |
| **Gast zu Hauptnetz blockiert, Gast zu Gast erfolgreich** | Prüfen Sie die drahtlose Client-Isolierung gesondert. |

Ein fehlgeschlagener **Ping** beantwortet die TCP-Frage nicht. Eine Host-Firewall kann Ping blockieren und den gewählten Dienst trotzdem zulassen. Auch ein fehlgeschlagener TCP-Test ist eng begrenzt: Er sagt nichts über andere Ports, Geräte, IPv6 oder Ausnahmen für freigegebene Geräte aus. Nutzen Sie Abweichungen als Anlass, die konfigurierte Regel zu prüfen und einen kontrollierten Test zu wiederholen.

## Ergebnis korrigieren und festhalten

Ändern Sie jeweils nur eine Kontrolle. Prüfen Sie bei einem Deco im Access-Point-Modus **Allow Local Access**. Prüfen Sie bei einem ASUS-Gastprofil **Access Intranet**. Entfernen Sie bei Google Nest Wifi einen unbeabsichtigten Eintrag aus **Shared devices**. Wenn Sie lokale Smart-Home-Steuerung benötigen, legen Sie vor einer Ausnahme fest, welches Gerät auf welchen Dienst zugreifen muss. Ein **VLAN** ist ein logisches Netzwerk, das über gemeinsam genutzte Hardware übertragen wird. Der [VLAN-Segmentierungsplan](/articles/homelab-vlan-segmentation-plan/) der Website beschreibt ein verwaltetes Netzwerk, wenn einem Mesh-System für Privathaushalte die erforderliche Zugriffsregel fehlt.

Notieren Sie Mesh-Modell, Firmware, Betriebsmodus, Knoten, WLAN-Name, Quellgerät, Zieldienst, Adressfamilie, erwartetes und tatsächliches Ergebnis sowie die einzelne Änderung. Veröffentlichen Sie keine privaten Adressen oder Netzwerkkennwörter. Wiederholen Sie dieselben Tests nach Firmware-Updates, Knotenwechseln oder einem Wechsel zwischen Router- und Access-Point-Modus.

Wenn Sie noch Geräte auswählen, vergleichen Sie die Funktionen im [Kaufratgeber für Mesh-WLAN](/articles/best-wifi-mesh-system-for-consumers/). Prüfen Sie danach das installierte Netzwerk mit diesem Verfahren. **Ein Label oder Schalter in einer App ist eine Behauptung. Eine Positivkontrolle und ein erneuter Test unter gleichen Bedingungen liefern Belege für den Pfad, der Sie interessiert.**

## Nächste Schritte

Wiederholen Sie die Isolationstests nach Firmware-, Knoten- oder Betriebsmodusänderungen. Nutzen Sie den [VLAN-Segmentierungsplan](/articles/homelab-vlan-segmentation-plan/), wenn die Mesh-Kontrollen die erforderliche Grenze nicht erfüllen.
