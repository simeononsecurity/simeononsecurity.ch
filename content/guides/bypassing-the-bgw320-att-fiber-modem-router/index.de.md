---
title: "Umgehung des BGW-320: Verwendung eines Azores COTS ONT - eine schrittweise Anleitung"
draft: false
toc: true
date: 2023-04-30
description: "In dieser leicht verständlichen Anleitung erfahren Sie, wie Sie den BGW-320 umgehen und einen COTS ONT von Azores verwenden, um sich mit dem Netzwerk Ihres ISP zu verbinden."
tags: ["COTS ONT", "BGW-320", "Azoren", "Faser", "Netzwerk", "XGS-PON", "Ethernet", "IP-Passthrough", "Personalisierung", "ISP", "haben ID", "MAC-Adresse", "Geräte-ID", "Bildversion", "Hardware-Version", "telnet", "CLI-Anwendung", "Web-GUI", "Werkskonfigurationsmodus", "Kompatibilitätsprobleme"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Ein Techniker mit einem COTS ONT in der Hand und einem Glasfaserkabel im Hintergrund."
coverCaption: ""
---

## Umgehung der BGW-320 und Verwendung eines Azores WAG-D20

Die meisten Menschen mit Glasfaser haben zwei Möglichkeiten, sich mit dem Internet zu verbinden - Glasfaser zu einem ONT, Ethernet zu einem Gateway oder Glasfaser direkt zu einem Gateway. In diesem Artikel werden wir uns darauf konzentrieren, wie man den BGW-320 umgeht und einen COTS-ONT von Azores verwendet.

### Technische Aspekte

Die[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Gerätezugriff

Die Standard-IP-Adresse des Geräts lautet 192.168.1.1 und die Gateway-Adresse enthält einen werkseitigen Tippfehler unter Verwendung einer öffentlichen IP-Adresse, d. h. es wird 192.162.1.1 statt 192.168.1.1 angezeigt.

Sobald das Gerät hochgefahren ist, müssen Sie die Eingabetaste drücken, um eine Anmeldeaufforderung an der seriellen TTL-Schnittstelle (115200 8N1) zu erhalten. Dieses Gerät verfügt über ein A/B-Image-System mit einer Overlay-Partition, auf der alle von Ihnen angepassten Dateien gespeichert sind.
 
### Anmeldeinformationen

-`admin``ADMIN123!@#` - Administrator-Anmeldung für Web-GUI
-`Guest``welcome` - Guest login
-`test``default` - Werksanmeldung

### Ethernet-Schnittstelle

Schließen Sie Ihren Client an den 10G-Ethernet-Port an und konfigurieren Sie ihn mit einer Adresse im 192.168.1.x/24-Netzwerk wie - 192.168.1.2/255.255.255.0.

Wenn Sie einen Port-Scan von 1-65535 durchführen, werden Sie einige offene Ports feststellen:

- Ports`23` &`8009` - Telnet, erfordert Anmeldung, führt die CLI-Anwendung aus.
- Anschluss`10002` - Unbekannt
- Hafen`80` - WebUI, nur zwei Funktionen

### Anpassen des ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Jetzt kommt der wichtige Teil, d. h. die Änderung einiger Geräteinformationen, um sie mit dem Netz Ihres Internetanbieters kompatibel zu machen.

Holen Sie sich zunächst die folgenden Informationen von Ihrem ISP-Gateway oder ONT:

1. **ONT-ID**
2. **MAC-Adresse**
3. **Geräte-ID**
4. **Bildversion**
5. **Hardware-Version**

Hinweis: Dies sind die OMCI-Werte und nicht die Werte der Web-UI.

Telnet zu Ihrem persönlichen ONT (telnet 192.168.1.1), Anmeldung als **`test` mit dem **`default` Passwort und führen Sie den Befehl 'test' aus, um in den Werkskonfigurationsmodus zu gelangen.

Zeigen Sie die aktuell eingestellten Werte mit dem Befehl "show" an:

-`show gpon mac`
-`show sn`
-`show equipment id`

Danach können Sie die Einstellungen mit den folgenden Befehlen anpassen, indem Sie x durch die Werte Ihres Geräts ersetzen:

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Für HUMAX:

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Für Nokia:

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Hinweis: Die letzten beiden Befehle sollten von telnet aus ausgeführt werden, wenn Sie als ** angemeldet sind.`test` Benutzer.

### Neustart und genießen Sie echten IP-Passthrough

Nach der Anpassung starten Sie den ONT neu und genießen Sie echten IP-Passthrough.

### Fehlerbehebung und weitere Schritte
Weitere Informationen zu diesem Thema finden Sie in der[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Schlussfolgerung

Wenn man diese Schritte befolgt, kann man den BGW-320 erfolgreich umgehen und den COTS ONT von Azores verwenden, um sich mit dem Netzwerk des ISP zu verbinden. Seien Sie jedoch vorsichtig bei der Eingabe von Befehlen und stellen Sie sicher, dass Sie "x" durch die Werte Ihres Geräts ersetzen, da sonst Kompatibilitätsprobleme auftreten können, die zu Verbindungsfehlern führen können.


