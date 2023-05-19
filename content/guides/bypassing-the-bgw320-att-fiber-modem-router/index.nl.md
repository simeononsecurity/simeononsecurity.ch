---
title: "De BGW-320 omzeilen: Een Azores COTS ONT gebruiken - een stap-voor-stap handleiding"
draft: false
toc: true
date: 2023-04-30
description: "Leer hoe u de BGW-320 kunt omzeilen en een COTS ONT van Azores kunt gebruiken om verbinding te maken met het netwerk van uw ISP met deze gemakkelijk te volgen gids."
tags: ["COTS ONT", "BGW-320", "Azoren", "vezel", "netwerk", "XGS-PON", "Ethernet", "IP passthrough", "maatwerk", "ISP", "hebben ID", "MAC-adres", "apparatuur-ID", "beeldversie", "hardwareversie", "telnet", "CLI-toepassing", "web GUI", "fabrieksconfiguratiemodus", "compatibiliteitsproblemen"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Een tekenfilmtechnicus die een COTS ONT vasthoudt met een vezelkabel op de achtergrond."
coverCaption: ""
---

## Hoe de BGW-320 te omzeilen en een Azoren WAG-D20 te gebruiken

De meeste mensen met glasvezel hebben twee manieren om verbinding te maken met het internet - glasvezel naar een ONT, Ethernet naar een gateway of glasvezel rechtstreeks naar de gateway. In dit artikel bespreken we hoe de BGW-320 te omzeilen en een COTS ONT van Azores te gebruiken.

### Technische aspecten

De[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Apparaat Toegang

Het standaard IP-adres van het apparaat is 192.168.1.1 en het Gateway-adres heeft een fabrieksfout waarbij een openbaar IP-adres wordt gebruikt, d.w.z. het toont 192.162.1.1 in plaats van 192.168.1.1.

Zodra het opstart, moet u op enter drukken om een login prompt te krijgen op de TTL seriële interface (115200 8N1). Dit apparaat heeft een A/B image systeem met een overlay partitie die alle bestanden bevat die je aanpast.
 
### Inloggegevens

-`admin``ADMIN123!@#` - Administrator login voor web GUI
-`Guest``welcome` - Gast inloggen
-`test``default` - Fabriekslogin

### Ethernet-interface

Sluit uw client aan op de 10G-ethernetpoort en configureer hem met een adres in het 192.168.1.x/24-netwerk zoals - 192.168.1.2/255.255.255.0.

Bij het uitvoeren van een poortscan van 1-65535 zult u enkele open poorten zien:

- Poorten`23` &`8009` - Telnet, vereist aanmelding, voert de CLI-toepassing uit.
- Poort`10002` - Onbekende
- Haven`80` - WebUI, slechts twee functies

### De ONT aanpassen

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Nu komt het belangrijke deel, namelijk het veranderen van wat apparaatinformatie om het compatibel te maken met het netwerk van uw ISP.

Pak eerst de volgende informatie van uw ISP Gateway of ONT:

1. **ONT ID**
2. **MAC-adres**
3. **Uitrusting ID**
4. **Image Version**
5. **Hardware versie**

Opmerking: Dit zijn de OMCI-waarden en niet die van de web UI.

Telnet naar uw persoonlijke ONT (telnet 192.168.1.1), login als **.`test` met behulp van de **`default` wachtwoord en voer het commando 'test' uit om in de fabrieksconfiguratiemodus te komen.

Geef de momenteel ingestelde waarden weer met het commando "show":

-`show gpon mac`
-`show sn`
-`show equipment id`

Pas de instellingen aan met de volgende commando's, waarbij u x vervangt door de waarden van uw apparaat:

-`set gpon mac xx:xx:xx:xx:xx:xx`
-`set sn <insert ONT ID here>`

Voor HUMAX:

-`set equipment id “iONT320500G”`
-`config ONU-G_Version "BGW320-500_2.1”`

Voor Nokia:

-`set equipment id “iONT320505G”`
-`config ONU-G_Version "BGW320-505_2.2”`

Opmerking: De laatste twee commando's moeten worden toegepast vanaf telnet ingelogd als de **`test` gebruiker.

### Herstart en geniet van echte IP-doorvoer

Na het aanpassen herstart u de ONT en geniet u van echte IP passthrough.

### Probleemoplossing en verdere stappen
Voor meer informatie over dit onderwerp kunt u de[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusie

Door deze stappen te volgen kan men met succes de BGW-320 omzeilen en COTS ONT van Azores gebruiken om verbinding te maken met het netwerk van hun ISP. Wees echter voorzichtig bij het invoeren van commando's en zorg ervoor dat u de 'x' correct vervangt door uw apparaatwaarden, anders kunt u te maken krijgen met compatibiliteitsproblemen die kunnen leiden tot verbindingsfouten.


