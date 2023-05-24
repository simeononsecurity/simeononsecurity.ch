---
title: "Ocolirea BGW-320: Utilizarea unui COTS ONT Azore - Un ghid pas cu pas"
draft: false
toc: true
date: 2023-04-30
description: "Aflați cum să ocoliți BGW-320 și să utilizați un COTS ONT realizat de Azore pentru a vă conecta la rețeaua ISP-ului dvs. cu acest ghid ușor de urmat."
tags: ["COTS ONT", "BGW-320", "Azore", "fibră", "reţea", "XGS-PON", "Ethernet", "trecere IP", "personalizare", "ISP", "ont ID", "Adresa mac", "ID echipament", "versiunea imaginii", "versiunea hardware", "telnet", "aplicație CLI", "GUI web", "modul de configurare din fabrică", "probleme de compatibilitate"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un tehnician din desene animate care ține un COTS ONT cu un cablu de fibră în fundal."
coverCaption: ""
---

## Cum să ocoliți BGW-320 și să utilizați un Azores WAG-D20

Majoritatea persoanelor cu fibră au două moduri de a se conecta la internet - fibră la un ONT, Ethernet la un gateway sau fibră direct la gateway. În acest articol, ne vom concentra pe cum să ocolim BGW-320 și să folosim un COTS ONT fabricat de Azore.

### Aspecte tehnice

The [Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Acces la dispozitiv

Adresa IP implicită a dispozitivului este 192.168.1.1, iar adresa sa Gateway are o greșeală de tipar din fabrică folosind o adresă IP publică, adică arată 192.162.1.1 în loc de 192.168.1.1.

Odată ce pornește, trebuie să apăsați enter pentru a obține o solicitare de conectare pe interfața serială TTL (115200 8N1). Acest dispozitiv are un sistem de imagine A/B cu o partiție de suprapunere care conține toate fișierele pe care le personalizați.
 
### Acreditări

- `admin``ADMIN123!@#` - Conectare administrator pentru GUI web
- `Guest``welcome` - Autentificare invitat
- `test``default` - Autentificare în fabrică

### Interfață Ethernet

Conectați-vă clientul la portul Ethernet 10G și configurați-l cu o adresă în rețeaua 192.168.1.x/24, cum ar fi - 192.168.1.2/255.255.255.0.

La rularea unei scanări de porturi de la 1-65535, veți observa câteva porturi deschise:

- Porturi `23` & `8009` - Telnet, necesită autentificare, rulează aplicația CLI.
- Port `10002` - Necunoscut
- Port `80` - WebUI, doar două funcții

### Personalizarea ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Acum vine partea importantă, adică modificarea unor informații despre dispozitiv pentru a-l face compatibil cu rețeaua ISP-ului tău.

Mai întâi, luați următoarele informații de la ISP Gateway sau ONT:

1. **ONT ID**
2. **Adresa MAC**
3. **ID echipament**
4. **Versiunea imaginii**
5. **Versiune hardware**

Notă: Acestea sunt valorile OMCI și nu cele din interfața de utilizare web.

Telnet la ONT-ul dvs. personal (telnet 192.168.1.1), conectați-vă ca **`test` folosind **`default` parola și rulați comanda „test” pentru a trece în modul de configurare din fabrică.

Afișați valorile setate în prezent cu comanda „show”:

- `show gpon mac`
- `show sn`
- `show equipment id`

După ce ați terminat, personalizați setările cu următoarele comenzi, înlocuind x cu valorile dispozitivului dvs.:

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insert ONT ID here>`

Pentru HUMAX:

- `set equipment id “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

Pentru Nokia:

- `set equipment id “iONT320505G”`
- `config ONU-G_Version "BGW320-505_2.2”`

Notă: Ultimele două comenzi ar trebui aplicate de la telnet conectat ca **`test` utilizator.

### Reporniți și bucurați-vă de True IP Passthrough

După personalizare, reporniți ONT-ul și bucurați-vă de trecerea IP adevărată.

### Depanare și pași suplimentari
Pentru mai multe informații despre acest subiect, vă rugăm să consultați [8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Concluzie

Urmând acești pași, puteți ocoli cu succes BGW-320 și puteți utiliza COTS ONT realizat de Azore pentru a vă conecta la rețeaua ISP-ului lor. Cu toate acestea, aveți grijă când introduceți comenzi și asigurați-vă că înlocuiți corect „x” cu valorile dispozitivului dvs., altfel vă puteți confrunta cu probleme de compatibilitate care pot duce la eșecuri de conexiune.


