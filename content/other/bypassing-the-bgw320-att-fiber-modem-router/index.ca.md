---
title: "Oblidació del BGW-320: ús d'un COTS ONT de les Açores: una guia pas a pas"
draft: false
toc: true
date: 2023-04-30
description: "Aprèn a obviar el BGW-320 i a utilitzar un COTS ONT fet per Açores per connectar-te a la xarxa del teu ISP amb aquesta guia fàcil de seguir".
tags: ["COTS ONT","BGW-320","Açores","fibra","xarxa","XGS-PON","Ethernet","Transmissió IP","personalització","ISP","ont ID","Adreça MAC","ID d'equip","versió de la imatge","versió de maquinari","telnet","Aplicació CLI","GUI web","mode de configuració de fàbrica","Problemes de compatibilitat"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Un tècnic de dibuixos animats sostenint un COTS ONT amb un cable de fibra al fons".
coverCaption: ""
---

## Com evitar el BGW-320 i utilitzar un Açores WAG-D20

La majoria de les persones amb fibra tenen dues maneres de connectar-se a Internet: fibra a una ONT, Ethernet a una passarel·la o fibra directament a la passarel·la. En aquest article, ens centrarem en com evitar el BGW-320 i utilitzar un COTS ONT fabricat per Açores.

### Aspectes tècnics

El[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Accés al dispositiu

L'adreça IP predeterminada del dispositiu és 192.168.1.1 i la seva adreça de passarel·la té un error tipogràfic de fàbrica utilitzant una adreça IP pública, és a dir, mostra 192.162.1.1 en lloc de 192.168.1.1.

Un cop arrenqui, heu de prémer Intro per obtenir una sol·licitud d'inici de sessió a la interfície sèrie TTL (115200 8N1). Aquest dispositiu té un sistema d'imatge A/B amb una partició superposada que conté els fitxers que personalitzeu.
 
### Credencials

- `admin`/`ADMIN123!@#` - Inici de sessió de l'administrador per a la GUI web
- `Convidat`/`benvingut` - Inici de sessió de convidat
- `test`/`default` - Inici de sessió de fàbrica

### Interfície Ethernet

Connecteu el vostre client al port Ethernet 10G i configureu-lo amb una adreça a la xarxa 192.168.1.x/24 com - 192.168.1.2/255.255.255.0.

En executar una exploració de ports des de l'1-65535, notareu alguns ports oberts:

- Ports `23` i `8009` - Telnet, requereix inici de sessió, executa l'aplicació CLI.
- Port `10002` - Desconegut
- Port `80` - WebUI, només dues funcions

### Personalització de l'ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Ara ve la part important, és a dir, canviar alguna informació del dispositiu per fer-lo compatible amb la xarxa del vostre ISP.

Primer, agafeu la informació següent del vostre ISP Gateway o ONT:

1. **ID ONT**
2. **Adreça MAC**
3. **ID de l'equip**
4. **Versió de la imatge**
5. **Versió de maquinari**

Nota: aquests són els valors OMCI i no els de la interfície d'usuari web.

Telnet al vostre ONT personal (telnet 192.168.1.1), inicieu sessió com a **`test`** amb la contrasenya **`default`** i executeu l'ordre 'prova' per passar al mode de configuració de fàbrica.

Mostra els valors establerts actualment amb l'ordre "mostrar":

- `mostrar gpon mac`
- `mostrar sn`
- "Mostra l'identificador de l'equip".

Un cop fet, personalitzeu la configuració amb les ordres següents substituint x pels valors del vostre dispositiu:

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insereix l'ID ONT aquí>`

Per a HUMAX:

- `configureu l'identificador de l'equip "iONT320500G"`
- `config ONU-G_Versió "BGW320-500_2.1"`

Per a Nokia:

- `configureu l'identificador de l'equip "iONT320505G"`
- `config ONU-G_Version "BGW320-505_2.2"`

Nota: Les dues últimes ordres s'han d'aplicar des de telnet connectat com a usuari **`test`**.

### Reinicieu i gaudiu de True IP Passthrough

Després de personalitzar-lo, reinicieu l'ONT i gaudiu de la transmissió IP real.

### Resolució de problemes i passos addicionals
Per obtenir més informació sobre aquest tema, consulteu el[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusió

Seguint aquests passos, es pot evitar amb èxit el BGW-320 i utilitzar COTS ONT fet per Açores per connectar-se a la xarxa del seu ISP. Tanmateix, aneu amb compte quan introduïu les ordres i assegureu-vos de substituir correctament "x" pels valors del vostre dispositiu, en cas contrari, podríeu tenir problemes de compatibilitat que poden provocar errors de connexió.


