---
title: „Umgehung des BGW-320: Verwendung eines Azores COTS ONT – Eine Schritt-für-Schritt-Anleitung“
draft: false
toc: true
date: 2023-04-30
description: „Erfahren Sie mit dieser leicht verständlichen Anleitung, wie Sie den BGW-320 umgehen und ein von Azores hergestelltes COTS ONT verwenden, um eine Verbindung zum Netzwerk Ihres ISP herzustellen.“
tags: [„COTS ONT“,„BGW-320“,„Azoren“,"Faser","Netzwerk",„XGS-PON“,„Ethernet“,„IP-Passthrough“,"Anpassung",„ISP“,„Ont-ID“,"MAC-Adresse",„Geräte-ID“,„Bildversion“,"Hardware Version",„Telnet“,„CLI-Anwendung“,„Web-GUI“,„Werkskonfigurationsmodus“,"Kompatibilitätsprobleme"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: „Ein Cartoon-Techniker hält ein COTS ONT mit einem Glasfaserkabel im Hintergrund.“
coverCaption: „“
---

## So umgehen Sie den BGW-320 und verwenden einen Azores WAG-D20

Die meisten Menschen mit Glasfaser haben zwei Möglichkeiten, sich mit dem Internet zu verbinden: Glasfaser zu einem ONT, Ethernet zu einem Gateway oder Glasfaser direkt zum Gateway. In diesem Artikel konzentrieren wir uns darauf, wie man den BGW-320 umgeht und einen von Azores hergestellten COTS ONT verwendet.

### Technische Aspekte

Der[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Gerätezugriff

Die Standard-IP-Adresse des Geräts ist 192.168.1.1 und seine Gateway-Adresse weist werkseitig einen Tippfehler auf, der eine öffentliche IP-Adresse verwendet, d. h. sie zeigt 192.162.1.1 statt 192.168.1.1 an.

Nach dem Booten müssen Sie die Eingabetaste drücken, um eine Anmeldeaufforderung an der seriellen TTL-Schnittstelle (115200 8N1) zu erhalten. Dieses Gerät verfügt über ein A/B-Image-System mit einer Overlay-Partition, die alle von Ihnen angepassten Dateien enthält.
 
### Referenzen

- `admin`/`ADMIN123!@#` – Administratoranmeldung für Web-GUI
- „Gast“/„Willkommen“ – Gastanmeldung
- „test“/„default“ – Werksanmeldung

### Ethernet-Schnittstelle

Verbinden Sie Ihren Client mit dem 10G-Ethernet-Port und konfigurieren Sie ihn mit einer Adresse im Netzwerk 192.168.1.x/24, z. B. 192.168.1.2/255.255.255.0.

Wenn Sie einen Port-Scan von 1-65535 ausführen, werden Sie einige offene Ports bemerken:

- Ports „23“ und „8009“ – Telnet, erfordert Anmeldung, führt die CLI-Anwendung aus.
- Port „10002“ – Unbekannt
- Port „80“ – WebUI, nur zwei Funktionen

### Anpassen des ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Jetzt kommt der wichtige Teil, nämlich das Ändern einiger Geräteinformationen, um es mit dem Netzwerk Ihres ISP kompatibel zu machen.

Besorgen Sie sich zunächst die folgenden Informationen von Ihrem ISP-Gateway oder ONT:

1. **ONT-ID**
2. **MAC-Adresse**
3. **Geräte-ID**
4. **Bildversion**
5. **Hardwareversion**

Hinweis: Dies sind die OMCI-Werte und nicht die aus der Web-Benutzeroberfläche.

Telnet mit Ihrem persönlichen ONT (Telnet 192.168.1.1), melden Sie sich als **`test`** mit dem **`Standard`**-Passwort an und führen Sie den Befehl „test“ aus, um in den Werkskonfigurationsmodus zu wechseln.

Zeigen Sie die aktuell eingestellten Werte mit dem Befehl „show“ an:

- „GPON Mac anzeigen“.
- `sn anzeigen`
- „Geräte-ID anzeigen“.

Wenn Sie fertig sind, passen Sie die Einstellungen mit den folgenden Befehlen an und ersetzen Sie x durch Ihre Gerätewerte:

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <hier ONT-ID einfügen>`

Für HUMAX:

- „Geräte-ID „iONT320500G“ festlegen“.
- `config ONU-G_Version „BGW320-500_2.1“`

Für Nokia:

- „Geräte-ID „iONT320505G“ festlegen“.
- `config ONU-G_Version „BGW320-505_2.2“`

Hinweis: Die letzten beiden Befehle sollten über Telnet angewendet werden, bei dem Sie als **`test`**-Benutzer angemeldet sind.

### Starten Sie neu und genießen Sie echtes IP-Passthrough

Starten Sie nach der Anpassung das ONT neu und genießen Sie echtes IP-Passthrough.

### Fehlerbehebung und zusätzliche Schritte
Weitere Informationen zu diesem Thema finden Sie unter[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Abschluss

Wenn Sie diese Schritte befolgen, können Sie den BGW-320 erfolgreich umgehen und COTS ONT von Azores verwenden, um eine Verbindung zum Netzwerk ihres ISP herzustellen. Seien Sie jedoch bei der Eingabe von Befehlen vorsichtig und stellen Sie sicher, dass Sie „x“ korrekt durch Ihre Gerätewerte ersetzen. Andernfalls kann es zu Kompatibilitätsproblemen kommen, die zu Verbindungsfehlern führen können.


