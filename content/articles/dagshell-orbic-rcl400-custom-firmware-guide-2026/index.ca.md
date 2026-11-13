---
title: "Firmware personalitzat DagShell per a Orbic RCL400: guia de 2026"
date: 2026-05-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Guia tècnica del firmware DagShell per a Orbic RCL400. Explica la instal·lació, les eines de privacitat, el wardriving i els límits de la recerca."
genre: ["Firmware personalitzat", "Seguretat mòbil", "Eines de privacitat", "Seguretat de xarxa", "Wardriving", "Proves de penetració", "Seguretat IoT", "Recerca de seguretat", "Seguretat de maquinari", "Tecnologia de privacitat"]
tags: ["DagShell", "Orbic RCL400", "Firmware personalitzat", "Hacking de hotspots", "Eines de privacitat", "Correcció TTL", "Suplantació MAC", "Detecció d’IMSI catchers", "Wardriving", "Seguiment GPS", "Atac Evil Twin", "Portal captiu", "Sniffer DNS", "Escàner ARP", "Escàner de ports", "Complement Raspberry Pi", "Seguretat WiFi", "Hotspot mòbil", "Monitoratge de xarxa", "Proves de penetració", "Recerca de seguretat", "Escaneig Bluetooth", "Atac de desautenticació", "Escaneig WiFi", "Cerca OUI", "Pujada a Wigle", "Monitoratge de torres cel·lulars", "Comandes AT", "Gestor de tallafoc", "Bloqueig d’anuncis", "Xifratge TLS", "Integració amb RayHunter", "STS Collective", "Laboratori de seguretat mòbil", "Anàlisi de xarxa", "Firmware de privacitat", "Seguretat de codi obert", "Compilació creuada ARM", "Linux encastat", "Kit d’eines de seguretat", "Eines de hacking", "Equip vermell", "Reconeixement de xarxa"]
canonical: "https://simeononsecurity.com/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/"
cover: "/img/cover/dagshell-orbic-rcl400-custom-firmware-guide-2026.webp"
coverAlt: "Il·lustració d’un hotspot Orbic RCL400 amb una interfície verda lluminosa, envoltat de representacions abstractes d’eines de seguretat, com gràfics i mapes, sobre un fons blau marí fosc."
coverCaption: ""
---

**Converteix l’Orbic RCL400 en un laboratori mòbil de recerca de seguretat**

## Introducció: un hotspot per a hackers

**DagShell** és un firmware personalitzat de codi obert per a l’**hotspot mòbil Orbic RCL400**. Transforma un dispositiu cel·lular corrent en un **kit portàtil de recerca de seguretat i privacitat**. Creat pel investigador de seguretat «dag», aquest firmware d’estil terminal ofereix **eines de hacking, funcions de privacitat i capacitats de monitoratge de xarxa** amb una interfície verda sobre negre d’estètica hacker.

Aquesta guia explica:
- **Què és DagShell** i quines funcions inclou
- La **instal·lació pas a pas**, amb el webflasher i els mètodes manuals
- Les **eines i capacitats** disponibles
- La configuració d’un **Raspberry Pi complementari** per ampliar les funcions
- **Per què combinar DagShell amb RayHunter** per a la seguretat mòbil
- **Casos d’ús reals** per a investigadors de seguretat i defensors de la privacitat
- Les **consideracions legals i ètiques**

**En resum**: DagShell i RayHunter en un Orbic RCL400 formen un **laboratori mòbil de seguretat** per detectar IMSI catchers, fer wardriving, analitzar xarxes i protegir la privacitat.

**Dispositius preparats**: aquest article està patrocinat per **STS Collective**, que ofereix hotspots Orbic RCL400 preparats amb **RayHunter i DagShell** instal·lats: [stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)

> 💰 **Descompte exclusiu per als lectors**: estalvia fins a un 20 % en productes de STS Collective, inclosos els Orbic RCL400 preparats. Fes servir el codi **SIMEONONSECURITY** en pagar o [compra amb el descompte aplicat](https://stscollective.com/discount/SIMEONONSECURITY).

______

## Què és DagShell?

### Descripció general

**DagShell** és un firmware personalitzat de codi obert que substitueix la interfície web original de l’Orbic RCL400 per un **kit complet d’eines de seguretat**, que inclou:

- **Interfície d’estil terminal** amb art ASCII i estètica hacker
- **Interfície web xifrada amb TLS 1.2 o superior** (certificat autosignat)
- **Eines de protecció de la privacitat** (ocultació del TTL, suplantació de MAC i bloqueig d’anuncis per DNS)
- **Monitoratge de xarxa** (connexions actives, taules d’encaminament i consultes DNS)
- **Eines de hacking** (detecció d’IMSI catchers, escaneig de ports i descobriment ARP)
- **Capacitats d’atac** (punt d’accés Evil Twin, phishing amb portal captiu i atacs de desautenticació)
- **Seguiment GPS i wardriving** amb exportació CSV compatible amb Wigle
- **Raspberry Pi complementari** per al GPS, l’escaneig Bluetooth i el reconeixement WiFi
- **Accés al sistema de fitxers** amb gestor de fitxers al navegador
- **Funcions SMS** mitjançant comandes AT
- **Persistència**: s’inicia automàticament en arrencar

### Especificacions tècniques

**Plataforma**: hotspot mòbil Orbic RCL400\
**Arquitectura**: ARM Linux (kernel 3.18)\
**Llenguatge**: C/C++ (binari ARM estàtic)\
**Xifratge**: TLS 1.2 o superior amb certificats autosignats (PKI de dos nivells)\
**Servidor web**: servidor HTTPS incrustat personalitzat (port 8443)\
**Interfície**: interfície terminal al navegador\
**Llicència**: MIT (codi obert)\
**GitHub**: [github.com/dagnazty/DagShell](https://github.com/dagnazty/DagShell)

### Disseny visual

DagShell té una **estètica hacker retro**:
- **Logotip ASCII** a cada pàgina
- **Colors verd sobre negre** (estil Matrix)
- **Tipus de lletra monoespaiada** (Fira Code)
- **Efectes de línies d’escaneig** i text lluminós
- **Disseny inspirat en un terminal**

{{< figure src="dagshell-orbic-rcl400-hacker-terminal-interface-feature-overview.webp" alt="Firmware DagShell en un Orbic RCL400. La interfície terminal verda sobre negre mostra art ASCII i un menú d’eines de seguretat" >}}

______

## Desglossament complet de les funcions

### 🏠 Tauler

**Resum del sistema**:
- **Temps d’activitat**: quant de temps fa que funciona el dispositiu
- **Interfície de comandes AT**: control directe del mòdem per a usuaris avançats
- **Estat ràpid**: adreça IP i estat de connexió

Les **comandes AT** permeten controlar el mòdem a baix nivell:
```
Example AT Commands:
AT+CSQ       - Signal quality
AT+COPS?     - Current network operator  
AT+CREG?     - Network registration status
AT+CIMI      - Get IMSI (subscriber identity)
AT+CGSN      - Get IMEI (device identifier)
```

### 🌐 Eines de xarxa

**Informació de la xarxa actual**:
- Detalls de l’**adreça IP i la interfície**
- **Màscara de subxarxa, passarel·la** i adreça de difusió
- **Estadístiques de xarxa** (paquets enviats i rebuts)

**Visor de la taula d’encaminament**:
- Mostra totes les rutes de xarxa
- Informació de la passarel·la predeterminada
- Correspondència d’interfícies

**Monitor de connexions actives**:
- Llista en temps real de **totes les connexions TCP/UDP**
- Adreces IP locals i remotes
- Números de port i estats de connexió
- Útil per **monitorar les comunicacions del dispositiu**

### 🔒 Conjunt de protecció de la privacitat

#### Correcció del TTL

**Objectiu**: amagar el trànsit del hotspot perquè l’operador no el detecti

**Com funciona**:
- Modifica a **65** el valor **Time To Live (TTL)** dels paquets IP
- Els operadors detecten el tethering per la reducció del TTL (telèfon = 64, dispositiu connectat = 63)
- Amb el TTL a 65, **tot el trànsit sembla local**

**Cas d’ús**: evitar les restriccions o limitacions de velocitat de tethering de l’operador

**Comandes**:
```bash
# Activa la correcció TTL
iptables -t mangle -A POSTROUTING -j TTL --ttl-set 65

# Desactiva la correcció TTL
iptables -t mangle -D POSTROUTING -j TTL --ttl-set 65
```

#### Suplantació de l’adreça MAC

**Objectiu**: aleatoritzar l’adreça MAC del dispositiu per protegir la privacitat

**Com funciona**:
- Canvia l’adreça MAC de **wlan0** (interfície WiFi)
- Genera una **adreça MAC aleatòria** o permet introduir-ne una de personalitzada
- Fa que sigui **més difícil rastrejar el dispositiu** entre sessions

**Cas d’ús**: evitar el seguiment per MAC a les xarxes a les quals et connectes

**Procés**:
1. La interfície es desactiva
2. S’aplica una adreça MAC nova
3. La interfície es torna a activar
4. Es restableix la connexió

#### Bloqueig d’anuncis per DNS

**Objectiu**: bloquejar anuncis i rastrejadors a nivell de DNS

**Com funciona**:
- Modifica el fitxer `/etc/hosts` amb una **llista de bloqueig**
- Els dominis de la llista es resolen a **127.0.0.1** (localhost)
- Bloqueja anuncis **a tots els dispositius connectats**

**Cas d’ús**: bloquejar anuncis a tota la xarxa sense configurar cada dispositiu

**Origen de la llista**: dominis habituals d’anuncis i seguiment (personalitzable)

### 📱 Gestió d'SMS

**Enviar SMS**:
- Envia missatges de text al mòdem mitjançant **comandes AT**
- Útil per a **notificacions remotes** o proves

**Veure missatges**:
- Enllaç a la bústia d’entrada nativa d’Orbic
- Permet llegir els SMS rebuts

**Comanda AT utilitzada**:
```
AT+CMGS="PHONE_NUMBER"
Message text here^Z
```

### 🔧 Eines de hacking

#### Detector d’IMSI catchers

**Objectiu**: monitorar la informació de les torres cel·lulars i detectar anomalies que indiquin dispositius **IMSI catcher o Stingray**

**Com funciona**:
- Consulta al mòdem les **dades de la torre cel·lular**:
  - **Cell ID** (identificador de la torre)
  - **LAC** (codi d’àrea d’ubicació)
  - **MCC/MNC** (codi de país mòbil i codi de xarxa mòbil)
  - **Potència del senyal** (RSSI)
  - **Generació de xarxa** (2G/3G/4G)
- **Registra els canvis** per detectar canvis sospitosos de torre
- **Seguiment de referència**: estableix quines torres són habituals a la zona

**Indicadors de detecció**:
- **Canvi sobtat de torre cel·lular** mentre el dispositiu està aturat
- **Descens a 2G** *(els IMSI catchers sovint forcen 2G per eliminar el xifratge)*
- Aparició d’un **Cell ID desconegut**
- **Senyal feble** d’una torre falsa
- **Reconnexions freqüents**

**Complementarietat amb RayHunter**: DagShell ofereix **monitoratge de torres cel·lulars**. RayHunter ofereix **detecció dedicada d’IMSI catchers** amb una anàlisi més avançada (consulta la secció següent).

#### Escàner de ports

**Objectiu**: escanejar adreces IP objectiu per trobar-hi ports oberts

**Com funciona**:
- **Escaneig TCP SYN**: envia paquets SYN als ports objectiu
- **Detecció per temps d’espera**: determina si els ports són oberts, tancats o filtrats
- **Suport de rangs**: escaneja un port o un rang de ports

**Casos d’ús**:
- **Reconeixement de xarxa**
- **Descobriment de dispositius IoT**
- **Auditoria de seguretat** de xarxes locals
- **Identificació de serveis**

**Comanda**:
```bash
# Escaneja els ports 1–1000 de l'objectiu
nc -zv -w 2 TARGET_IP 1-1000 2>&1
```

#### Gestor de tallafoc

**Objectiu**: bloquejar o desbloquejar adreces IP amb iptables

**Com funciona**:
- Usa **regles iptables** per descartar paquets d’una IP especificada o adreçats a aquesta
- Les **regles persistents** sobreviuen als reinicis si es desen
- Funcions de **llista d’autorització i llista de bloqueig**

**Casos d’ús**:
- **Bloquejar IP malicioses**
- **Impedir accessos no autoritzats**
- **Regular o filtrar el trànsit**
- **Control parental**

**Comandes**:
```bash
# Bloqueja l'IP
iptables -I INPUT -s IP_ADDRESS -j DROP
iptables -I OUTPUT -d IP_ADDRESS -j DROP

# Desbloqueja l'IP
iptables -D INPUT -s IP_ADDRESS -j DROP
iptables -D OUTPUT -d IP_ADDRESS -j DROP
```

### ⚔️ Eines d’atac

**AVÍS LEGAL IMPORTANT**: aquestes eines són només per a **proves de seguretat autoritzades**. Fer-les servir contra xarxes que no són teves o sense permís explícit per escrit és **il·legal** en moltes jurisdiccions (Computer Fraud and Abuse Act als EUA, Computer Misuse Act al Regne Unit, etc.). Fes-les servir només a **les teves pròpies xarxes** o en **entorns de laboratori controlats**.

#### Sniffer DNS

**Objectiu**: registrar les consultes DNS dels clients connectats

**Com funciona**:
- **Registre d’iptables** al port 53 (DNS)
- **No requereix mode promiscu**
- Registra totes les peticions DNS dels clients del hotspot
- Revela **quins llocs web i serveis** consulten els clients

**Casos d’ús autoritzats**:
- **Anàlisi del trànsit de xarxa**
- **Supervisió parental** (de la pròpia família)
- **Recerca de seguretat** en dispositius propis
- **Anàlisi del comportament de malware**

*Això captura metadades (dominis visitats) dels clients connectats. Fes-ho servir només en xarxes pròpies o que administris.*

#### Escàner ARP

**Objectiu**: descobrir dispositius a la xarxa local

**Com funciona**:
- Envia **peticions ARP** a totes les IP de la subxarxa
- Els dispositius responen amb les seves **adreces MAC**
- La **cerca OUI** identifica el fabricant (Apple, Samsung, etc.)
- Crea un **mapa de xarxa** dels dispositius actius

**Casos d’ús**:
- **Inventari de xarxa**
- **Detecció de dispositius desconeguts**
- **Anàlisi de xarxes BYOD**
- **Descobriment de dispositius IoT**

**Exemple de sortida**:
```
IP: 192.168.1.50
MAC: A4:83:E7:XX:XX:XX
Vendor: Apple, Inc.

IP: 192.168.1.75
MAC: 2C:54:91:XX:XX:XX
Vendor: Samsung Electronics
```

#### Traceroute

**Objectiu**: visualitzar la ruta de xarxa fins a una destinació

**Com funciona**:
- Envia paquets amb **TTL creixent**
- Cada salt redueix el TTL i retorna **ICMP Time Exceeded**
- Revela els **encaminadors i la ruta** fins a la destinació
- Mesura el **temps d’anada i tornada (RTT)** de cada salt

**Casos d’ús**:
- **Resolució de problemes de xarxa**
- **Anàlisi de rutes**
- **Diagnòstic de latència**
- **Investigació del peering de l’ISP**

#### Punt d’accés Evil Twin

**Objectiu**: crear un punt d’accés WiFi fals que cloni SSID existents

**Com funciona**:
- Fa servir **wlan1** (segona interfície WiFi, si el Pi complementari la proporciona)
- Clona el **SSID i el tipus de xifratge** de la xarxa objectiu
- **Captura els clients** que intenten connectar-s’hi
- Mostra un **portal captiu** per obtenir credencials

**Escenari d’atac** (entorn de laboratori):
1. Cerca xarxes WiFi legítimes
2. Crea un **AP fals** amb el mateix SSID
3. Fes servir un **atac de desautenticació** per desconnectar els clients de l’AP real
4. Els clients es tornen a connectar automàticament a l’**AP fals**
5. El portal captiu captura les credencials

*Detecció: els clients veuen **SSID duplicats** si tots dos AP són visibles alhora.*

#### Portal captiu

**Objectiu**: plantilles de pàgines de phishing per obtenir credencials

**Plantilles incloses**:
- **Pàgina d’inici de sessió WiFi** (estil genèric d’ISP o hotel)
- **Inicis de sessió de xarxes socials** (imitacions de Facebook, Twitter i Instagram)
- Portals d’**inici de sessió corporatiu**
- Accés WiFi d’**aeroports i cafeteries**

**Com funciona**:
1. L’AP Evil Twin redirigeix **tot el trànsit** al portal
2. El client veu una **pàgina d’inici de sessió**
3. El client introdueix les credencials
4. Les credencials es **desen en un fitxer**
5. Es concedeix accés a Internet o es mostra un error

**Finalitat educativa**: mostra els **riscos de l’enginyeria social** i per què els usuaris han de verificar les URL

### 📍 Seguidor GPS i wardriving

#### Funcions GPS

**Font GPS**: només el **Raspberry Pi complementari**
- *L’Orbic RCL400 **no té GPS integrat**. Sense el Pi complementari no hi ha dades d’ubicació.*
- El Pi connecta un **dongle GPS USB** (es recomana el chipset U-Blox 7)
- El Pi envia coordenades a l’Orbic mitjançant **fitxers de dades compartits**
- La conversió d’**ECEF a latitud/longitud** es fa automàticament

**Pantalla del tauler**:
- **Latitud/longitud** en graus decimals
- **Altitud** sobre el nivell del mar
- **Estat de fix GPS** (precisió)
- **Actualització automàtica** cada 5 segons
- **No apareixen sol·licituds de geolocalització del navegador** (no fa servir l’API del navegador)

**Estat GPS compartit**:
- Les dades GPS estan disponibles per a **tots els processos DagShell**
- El wardriving fa servir GPS automàticament
- Les funcions no entren en conflicte

#### Mode wardriving

**Objectiu**: escanejar xarxes WiFi amb coordenades GPS per cartografiar-les

**Com funciona**:
1. Espera un **fix GPS vàlid** (no registra coordenades 0,0)
2. Escaneja xarxes WiFi cada **5 segons**, en un bucle continu
3. Registra les dades de xarxa:
   - **SSID** (nom de xarxa)
   - **BSSID** (adreça MAC)
   - **Tipus de xifratge** (WPA2, WPA3 o obert)
   - **Potència del senyal** (RSSI en dBm)
   - **Número de canal**
   - **Coordenades GPS** (latitud/longitud)
   - **Marca de temps**
4. Exporta les dades en format **CSV compatible amb Wigle**

**Integració amb Wigle**:
- **WiGLE** (wigle.net) és un projecte global de cartografia WiFi
- El CSV de DagShell es pot **pujar directament** a WiGLE
- **Pujada des del navegador** a la pàgina Files, sense eines externes
- Contribueix a una **base de dades pública** d’ubicacions WiFi

**Casos d’ús**:
- **Cartografia de cobertura WiFi**
- **Reconeixement de xarxes** per a ISP
- **Anàlisi de la potència del senyal**
- **Recerca de seguretat** (xarxes obertes i xifratge feble)
- **Analítica basada en la ubicació**

**Exemple de format CSV**:
```csv
MAC,SSID,AuthMode,FirstSeen,Channel,RSSI,Latitude,Longitude,AltitudeMeters
A1:B2:C3:D4:E5:F6,HomeNetwork,WPA2,2026-05-28 10:30:15,6,-45,40.7128,-74.0060,10
```

{{< figure src="dagshell-wardriving-gps-wifi-network-mapping-wigle-csv-export.webp" alt="Mode de wardriving DagShell amb coordenades GPS i xarxes WiFi escanejades. El CSV compatible amb Wigle registra SSID, BSSID, xifratge i potència del senyal" >}}

### 🥧 Raspberry Pi complementari

El **Raspberry Pi complementari** amplia les capacitats de DagShell amb **maquinari extern**.

#### Requisits de maquinari

**Mínims**:
- **Raspberry Pi 3B+** o més recent *(el Pi Zero no proporciona prou alimentació USB als perifèrics)*
- **Dongle GPS USB** (es recomana el chipset U-Blox 7)
- **Font d’alimentació** *(el Pi necessita una font independent, el port USB de l’Orbic no en proporciona prou)*

**Opcional**:
- **Adaptador WiFi** (segona interfície per escanejar mentre es manté l’enllaç)
- **Dongle Bluetooth** (si el Bluetooth integrat al Pi és feble)

#### Mòdul GPS (U-Blox 7)

**Connexió**: dongle GPS USB al Pi\
**Protocol**: frases NMEA pel port sèrie\
**Conversió**: el Pi converteix ECEF a latitud/longitud automàticament\
**Compartició de dades**: escriu les coordenades GPS en un **fitxer compartit** de l’Orbic

**Anàlisi de frases**:
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
       |       |          |           |  |  |   |
       Time    Latitude   Longitude   Fix Sats  Altitude
```

#### Escaneig Bluetooth (BLE)

**Objectiu**: descobrir dispositius Bluetooth propers

**Com funciona**:
- Escaneja **anuncis BLE**
- Captura **adreces MAC**
- Cerca l’**OUI** per identificar el fabricant
- Registra les dades en **format CSV**

**Control remot**:
- Inicia o atura l’escaneig des de la interfície web de DagShell
- No cal connectar-se al Pi per SSH
- Mostra l’estat en temps real

**Casos d’ús**:
- **Seguiment i recompte de dispositius**
- **Anàlisi del trànsit de vianants**
- **Descobriment de dispositius Bluetooth**
- **Recerca de seguretat IoT**

**Sortida CSV**:
```csv
Timestamp,MAC,RSSI,Name,Manufacturer
2026-05-28 10:30:15,AA:BB:CC:DD:EE:FF,-65,Fitbit Charge,Fitbit Inc.
```

#### Escaneig WiFi

**Objectiu**: el Pi escaneja xarxes WiFi i envia les dades a l’Orbic

**Avantatge**: una interfície dedicada permet escanejar mentre **l’Orbic manté el hotspot**

**Com funciona**:
- El Pi fa servir un **segon adaptador WiFi** o el WiFi integrat, si no el necessita per connectar-se
- Escaneja **tots els canals** (1-14 a 2,4 GHz i 36-165 a 5 GHz si són compatibles)
- Envia els resultats a l’Orbic mitjançant l’emmagatzematge compartit
- DagShell els registra al **CSV de wardriving**

**Coordinació**:
- El Pi i l’Orbic se **sincronitzen** amb l’hora GPS
- Evita les entrades duplicades
- Combina **les dues fonts d’escaneig** en un sol registre

#### Atacs de desautenticació

**Objectiu**: desconnectar clients de xarxes WiFi (per a proves de laboratori)

**Com funciona**:
- Envia **trames de desautenticació 802.11**
- Suplanta l’**adreça MAC de l’AP**
- El client rep una ordre de desconnexió de l’AP
- El client **perd la connexió** i intenta tornar-s’hi a connectar

**Mètodes de control**:
- **Desautenticació puntual**: ràfega única de trames
- **Desautenticació contínua**: impedeix la reconnexió (DoS)
- **Control remot**: s’activa des de la pàgina d’escaneig de DagShell

**Casos d’ús autoritzats**:
- **Retirar un dispositiu intrús** de la pròpia xarxa
- **Proves de penetració** amb permís
- **Atacs Evil Twin** al laboratori (forçar els clients a connectar-se a un AP fals)

**⚠️ Avís legal**: els atacs de desautenticació són **il·legals contra xarxes que no són teves**. Poden infringir les normes de la FCC i comportar càrrecs segons la CFAA.

#### Servei d’inici automàtic

**Servei systemd**: el Pi complementari s’inicia automàticament en arrencar

**Fitxer de servei** (`/etc/systemd/system/pi-companion.service`):
```ini
[Unit]
Description=DagShell Pi Companion
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/dagshell/pi_companion.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

**Comandes**:
```bash
# Activa l'inici automàtic
sudo systemctl enable pi-companion

# Inicia el servei
sudo systemctl start pi-companion

# Comprova l'estat
sudo systemctl status pi-companion
```

#### Base de dades OUI

**Objectiu**: consultar el proveïdor o fabricant associat a una adreça MAC

**Base de dades**: API basada en prefixos de la [base de dades mestra OUI](https://standards.ieee.org/products-programs/regauth/)

**Com funciona**:
- Extreu els **3 primers bytes** de l’adreça MAC (prefix OUI)
- Consulta l’API: `api.example.com/oui/A4:83:E7`
- Retorna el **nom del fabricant**

**Exemple**:
```
MAC: A4:83:E7:12:34:56
OUI: A4:83:E7
Vendor: Apple, Inc.
```

**Integració**: ho fan servir l’escàner ARP, l’escàner BLE i el wardriving WiFi

### 📁 Explorador de fitxers

**Objectiu**: navegar pels fitxers del dispositiu i gestionar-los

**Ubicació**: directori `/data/` (partició amb permisos d’escriptura)

**Funcions**:
- **Navegar pels fitxers** i subdirectoris
- **Descarregar** fitxers a l’ordinador
- **Eliminar** fitxers (amb confirmació)
- **Veure la mida** i les marques de temps

**Fitxers habituals**:
- `wardrive_log.csv`: dades d’escaneig WiFi
- `bluetooth_scan.csv`: dades de dispositius BLE
- `gps_track.gpx`: rutes GPS
- `dns_queries.log`: consultes DNS capturades
- `arp_scan.txt`: llista de dispositius de xarxa

**Pujada a Wigle**:
- **Pujada directa des del navegador** a la pàgina Files
- Autenticació amb el compte WiGLE
- Puja el CSV sense descarregar-lo abans

______

{{< stscollective-ad "rayhunter" >}}

## Guia d’instal·lació

### Requisits previs

**Maquinari**:
- **Hotspot mòbil Orbic RCL400**
- **Ordinador** (Windows, macOS o Linux)
- **Cable USB** (si flasheges el firmware directament)

**Programari**:
- **Python 3** amb els mòduls `requests` i `cryptography`
- **Navegador web** (Chrome, Firefox, Edge o Safari)

**Opcional**:
- **Raspberry Pi 3B+** o més recent (per al GPS i funcions avançades)
- **Dongle GPS USB** (chipset U-Blox 7)

### Mètode 1: Webflasher (recomanat)

**Mètode més fàcil**: no cal fer servir la línia d’ordres

**Pas 1**: obre DagShell Webflasher
- URL: [dagnazty.github.io/DagShell/orbic.html](https://dagnazty.github.io/DagShell/orbic.html)

**Pas 2**: genera els certificats PKI
- Fes clic al botó **"Generate Certificates"**
- El navegador genera una **PKI de dos nivells** (CA arrel i certificat del servidor)
- **Descarrega els fitxers**: `root.der` i `server.der`

**Pas 3**: activa el shell root a l’Orbic
- Connecta’t a la xarxa WiFi de l’Orbic
- Introdueix la **contrasenya d’administrador** al formulari web
- Fes clic a **"Enable Shell"**
- La pàgina web explota l’API de l’Orbic per obrir un **shell root al port 24**

**Pas 4**: desplega el firmware
- Fes clic al botó **"Deploy DagShell"**
- L’script puja:
  - `orbic_app` (binari principal del firmware)
  - `root.der` (certificat arrel)
  - `server.der` (certificat TLS del servidor)
  - `dagshell_boot.sh` (script de persistència)
- La instal·lació triga **2-3 minuts**

**Pas 5**: reinicia l’Orbic
- Apaga i torna a encendre el dispositiu
- DagShell s’inicia automàticament en arrencar

**Pas 6**: accedeix a DagShell
- Obre el navegador a: `https://192.168.1.1:8443/`
- Accepta l’**avís de seguretat** (el certificat autosignat és normal)
- Inicia la sessió amb les credencials per defecte, si es demanen

### Mètode 2: instal·lació manual

Per a **usuaris avançats** que volen compilar des del codi font.

#### Pas 1: instal·la les dependències

**Windows**:
```powershell
# Instal·la Python 3
# Baixa-ho de python.org

# Instal·la els mòduls necessaris
pip install requests cryptography

# El compilador creuat ARM és a la carpeta gcc_win
```

**macOS**:
```bash
# Instal·la Homebrew si encara no hi és
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instal·la Python 3
brew install python3

# Instal·la els mòduls necessaris
pip3 install requests cryptography

# La cadena d'eines ARM és a la carpeta gcc_mac
```

**Linux**:
```bash
# Instal·la Python 3 i pip
sudo apt-get update
sudo apt-get install python3 python3-pip

# Instal·la els mòduls necessaris
pip3 install requests cryptography

# Instal·la el compilador creuat ARM
sudo apt-get install gcc-arm-linux-gnueabihf
```

#### Pas 2: clona el repositori

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell
```

#### Pas 3: compila el firmware

**Windows**:
```powershell
cd orbic_fw_c
python gen_pki.py          # Genera els certificats
.\build.ps1                # Compila el microprogramari
```

**macOS/Linux**:
```bash
cd orbic_fw_c
python3 gen_pki.py         # Genera els certificats
./build.sh                 # Compila el microprogramari, BearSSL es compila automàticament
```

**Resultat**: `orbic_app` (binari ARM estàtic) i fitxers de certificat DER

**⚠️ Nota per a macOS**: la carpeta `gcc_mac/` conté una cadena d’eines ARM personalitzada, compilada amb **crosstool-ng** per utilitzar les capçaleres de **Linux kernel 3.2**, compatibles amb el kernel 3.18 de l’Orbic. *Els compiladors ARM estàndard de Homebrew apunten a kernels més nous i **no funcionaran**.*

#### Pas 4: activa el shell root a l’Orbic

```bash
# Connecta't a la WiFi de l'Orbic
# Substitueix YOUR_ADMIN_PASSWORD per la contrasenya real

python enable_shell.py YOUR_ADMIN_PASSWORD
```

Aquesta ordre explota l’API web de l’Orbic per obrir un shell root al **port 24**.

#### Pas 5: desplega el firmware

```bash
python deploy_base64.py
```

Puja i instal·la:
- `orbic_app` a `/data/orbic_app`
- Els certificats a `/data/root.der` i `/data/server.der`
- L’script d’arrencada a `/etc/rc.d/dagshell_boot.sh`

**Persistència**: l’script init inicia automàticament el firmware en reiniciar.

#### Pas 6: reinicia i accedeix

```bash
# Reinicia l'Orbic (talla l'alimentació o usa SSH)
reboot

# Després de reiniciar, accedeix a DagShell
# Navegador: https://192.168.1.1:8443/
```

### Avís del certificat de seguretat

En accedir a DagShell, veuràs l’avís **"Not Secure"** o **"Not Trusted"**:

**Navegadors d’escriptori**:
- Fes clic a **"Advanced"**
- Fes clic a **"Proceed to 192.168.1.1 (unsafe)"**

**Navegadors mòbils**:
- Toca **"Show Details"**
- Toca **"visit this website"**

**Per què passa**:
- El certificat és **autosignat** (no prové d’una CA de confiança com Let's Encrypt)
- El dispositiu no té el certificat arrel al seu magatzem de confiança
- *És un comportament **esperat** en firmware personalitzat, no un senyal de compromís.*

**La connexió és segura?**:
- **Sí**. La connexió està xifrada amb **TLS 1.2 o superior**
- Les dades no es poden interceptar
- *El certificat no forma una cadena de confiança fins a una CA pública, però el xifratge és real.*

**Opcional**: instal·la `root.der` al magatzem de confiança del dispositiu per eliminar l’avís.

______

## Configuració del Raspberry Pi complementari

**Opcional, però molt recomanada** per disposar de totes les funcions.

### Configuració del maquinari

**Pas 1**: aconsegueix els components
- **Raspberry Pi 3B+** o més recent (35-55 $)
- **Dongle GPS USB** amb chipset U-Blox 7 (15-30 $)
- **Targeta microSD** de 16 GB o més per a Raspberry Pi OS (10 $)
- **Font d’alimentació** per al Pi (10 $)

**Pas 2**: instal·la Raspberry Pi OS
```bash
# Baixa Raspberry Pi Imager
# https://www.raspberrypi.org/software/

# Flasheja Raspberry Pi OS Lite a la targeta SD
# Arrenca la Pi i completa la configuració
```

**Pas 3**: connecta el dongle GPS
- Endolla el GPS USB al Pi
- Comprova si es detecta: `lsusb` (hauria d’aparèixer el dispositiu GPS)
- Verifica el port sèrie: `ls /dev/ttyUSB*` o `ls /dev/ttyACM*`

### Instal·lació del programari

**Pas 1**: clona el repositori DagShell al Pi

```bash
git clone https://github.com/dagnazty/DagShell.git
cd DagShell/pi_companion
```

**Pas 2**: instal·la les dependències

```bash
# Actualitza la llista de paquets
sudo apt-get update

# Instal·la els paquets necessaris
sudo apt-get install python3-serial python3-requests gpsd gpsd-clients

# Instal·la els mòduls de Python
pip3 install pyserial gps3 bluetooth pybluez
```

**Pas 3**: configura el dimoni GPS

```bash
# Edita la configuració de gpsd
sudo nano /etc/default/gpsd

# Configura la línia DEVICES amb el port sèrie del GPS
DEVICES="/dev/ttyUSB0"  # Ajusta-ho si cal

# Reinicia gpsd
sudo systemctl restart gpsd

# Prova el GPS
cgps -s  # Les dades dels satèl·lits haurien d'aparèixer al cap d'uns 30 segons
```

**Pas 4**: configura el Pi complementari

```bash
# Edita el fitxer de configuració
nano pi_companion/config.py

# Configura l'adreça IP de l'Orbic
ORBIC_IP = "192.168.1.1"
ORBIC_PORT = "8443"

# Configura el port sèrie del GPS
GPS_DEVICE = "/dev/ttyUSB0"

# Desa i surt
```

**Pas 5**: instal·la el servei systemd

```bash
# Copia el fitxer del servei
sudo cp pi_companion.service /etc/systemd/system/

# Torna a carregar systemd
sudo systemctl daemon-reload

# Activa l'inici automàtic
sudo systemctl enable pi-companion

# Inicia el servei
sudo systemctl start pi-companion

# Comprova l'estat
sudo systemctl status pi-companion
```

**Pas 6**: verifica la comunicació

```bash
# Comprova els registres
journalctl -u pi-companion -f

# Hauries de veure com s'envien les coordenades GPS a l'Orbic
```

### Configuració de xarxa

**Opció A**: connexió WiFi

```bash
# La Pi es connecta al punt d'accés de l'Orbic
# Edita la configuració de wpa_supplicant
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Afegeix una xarxa
network={
    ssid="Orbic_SSID"
    psk="PASSWORD"
}

# Reinicia la WiFi
sudo systemctl restart networking
```

**Opció B**: Ethernet per USB (recomanat)

- Connecta el Pi a l’Orbic amb un **cable USB** (del port USB del Pi al de l’Orbic)
- Activa el **mode USB gadget** al Pi
- El Pi actua com a **dispositiu Ethernet USB**
- *És més fiable que el WiFi per transferir dades contínuament.*
- El Pi accedeix a Internet a través de l’Orbic

**Configuració USB gadget**:
```bash
# Edita config.txt
sudo nano /boot/config.txt

# Afegeix al final
dtoverlay=dwc2

# Edita cmdline.txt
sudo nano /boot/cmdline.txt

# Afegeix després de rootwait
modules-load=dwc2,g_ether

# Reinicia
sudo reboot
```

______

## Per què combinar DagShell amb RayHunter?

{{< figure src="dagshell-rayhunter-complementary-capabilities.webp" alt="Diagrama comparatiu de les eines de wardriving WiFi i atac de xarxa de DagShell amb la detecció d’anomalies dels protocols cel·lulars de RayHunter. Tots dos funcionen al mateix hotspot Orbic RCL400" >}}

### Capacitats complementàries

**DagShell** i **RayHunter** són eines de seguretat **complementàries** que cobreixen aspectes diferents de la recerca de seguretat mòbil:

| Funció | DagShell | RayHunter |
|---------|----------|-----------|
| **Detecció d’IMSI catchers** | Monitoratge bàsic de torres cel·lulars | Anàlisi avançada de patrons |
| **Seguiment GPS** | Sí (mitjançant el Pi) | Sí (mitjançant el mòdem) |
| **Wardriving WiFi** | Sí | No |
| **Escaneig Bluetooth** | Sí (mitjançant el Pi) | No |
| **Eines de xarxa** | Sí (sniffer DNS, escàner ARP i de ports) | No |
| **Eines d’atac** | Sí (Evil Twin, portal captiu i desautenticació) | No |
| **Eines de privacitat** | Sí (correcció TTL, suplantació MAC i AdBlock) | Mínimes |
| **Base de dades de torres cel·lulars** | Bàsica | Completa |
| **Anàlisi d’IA/ML** | No | Sí (detecció d’anomalies) |
| **Anàlisi de protocols de l’operador** | Limitada | Profunda (SS7/Diameter) |

### Casos d’ús combinats

#### 1. **Defensa completa contra IMSI catchers**

**Escenari**: viatge en una zona amb molta vigilància

**Aportació de DagShell**:
- **Monitoratge en temps real dels canvis de torre cel·lular**
- **Seguiment de la ubicació GPS** durant canvis sospitosos
- **Registre de les dades de les torres** per analitzar-les més tard

**Aportació de RayHunter**:
- **Detecció d’anomalies basada en aprenentatge automàtic** als protocols cel·lulars
- **Inspecció de paquets SS7/Diameter** per detectar atacs sofisticats
- Comparació amb una **base de dades de torres conegudes com a fiables**

**Resultat conjunt**: DagShell ofereix **monitoratge continu** i RayHunter, **anàlisi profunda**.

#### 2. **Wardriving amb seguretat cel·lular**

**Escenari**: cartografiar les xarxes WiFi d’una zona urbana

**Aportació de DagShell**:
- **Escaneig WiFi** amb coordenades GPS
- Eines d’**anàlisi de xarxa** (potència del senyal i xifratge)
- Exportació CSV de **Wigle** per cartografiar

**Aportació de RayHunter**:
- **Seguiment de torres cel·lulars** durant el recorregut
- **Detecció d’IMSI catchers** mentre s’escaneja WiFi
- **Avís si la seguretat cel·lular està compromesa**

**Resultat conjunt**: wardriving amb **coneixement de la seguretat cel·lular**.

#### 3. **Laboratori de recerca de seguretat**

**Escenari**: equip vermell o proves de penetració

**Aportació de DagShell**:
- **Punt d’accés Evil Twin** per provar WiFi
- **Portal captiu** per a demostracions d’enginyeria social
- **Atacs de desautenticació** per provar la resiliència
- Eines de **reconeixement de xarxa**

**Aportació de RayHunter**:
- **Detecta si et vigilen** durant les proves
- Aporta informació sobre la **seguretat de les torres cel·lulars**
- Ajuda a prevenir la **contravigilància** durant les proves

**Resultat conjunt**: eines ofensives amb **consciència defensiva**.

#### 4. **Viatges centrats en la privacitat**

**Escenari**: periodista o activista en un entorn sensible

**Aportació de DagShell**:
- **Ocultació del TTL** per amagar el tethering
- **Suplantació de MAC** per preservar l’anonimat
- **AdBlock** per impedir el seguiment
- **Monitoratge d’IMSI catchers**

**Aportació de RayHunter**:
- **Detecció avançada d’IMSI catchers**
- **Detecció d’atacs a nivell de protocol**
- **Alertes de seguretat cel·lular**

**Resultat conjunt**: més privacitat amb **protecció multicapa**.

### Instal·lació conjunta

**Opció preparada** (la més fàcil):
- Compra a **STS Collective**: [Orbic RCL400 preparat amb RayHunter i DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- **Llest per fer servir** en sortir de la capsa
- Tots dos firmwares estan **provats i verificats**
- **Sense complicacions d’instal·lació**

**Instal·lació pròpia**:
1. **Flasheja primer RayHunter** (consulta la [guia completa per flashejar dispositius RayHunter](/articles/how-to-flash-rayhunter-devices-complete-guide/))
2. **Flasheja DagShell després** (poden coexistir)
3. **RayHunter** fa servir els ports per defecte
4. **DagShell** fa servir el port 8443
5. Accedeix a cadascun en una pestanya diferent del navegador

**Sense conflictes**:
- RayHunter fa servir els ports **80/443**
- DagShell fa servir el port **8443**
- No interfereixen entre si
- Funcionen **alhora**

Prefereixes no fer la instal·lació manual? L’**[Orbic RCL400 amb RayHunter i DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)** preparat ve llest per fer servir. El codi de lector **SIMEONONSECURITY** descompta fins a un 20 % a STS Collective.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra un RCL400 preparat i estalvia un 20 %
{{< /centerbutton >}}

______

## Casos d’ús reals

### Cas d’ús 1: investigador de seguretat

**Perfil**: provador d’intrusions que avalua la seguretat WiFi

**Eines DagShell utilitzades**:
- **Wardriving WiFi** per cartografiar les xarxes del client
- **Escàner ARP** per descobrir dispositius
- **Escàner de ports** per identificar serveis
- **Evil Twin i portal captiu** per provar la resistència a l’enginyeria social
- **Explorador de fitxers** per extreure resultats

**Flux de treball**:
1. Recórrer el perímetre de les instal·lacions del client
2. Fer wardriving per cartografiar la cobertura WiFi
3. Crear un Evil Twin de la xarxa del client, amb permís
4. Monitorar els intents de connexió dels clients
5. Generar un informe amb les dades recollides

**Integració amb RayHunter**: ajuda a comprovar que no vigilin l’investigador durant l’avaluació.

### Cas d’ús 2: defensor de la privacitat

**Perfil**: periodista que viatja a l’estranger

**Eines DagShell utilitzades**:
- **Correcció TTL** per evitar les restriccions de l’operador
- **Suplantació de MAC** per preservar l’anonimat del dispositiu
- **Detector d’IMSI catchers** per detectar vigilància
- **Sniffer DNS** per comprovar que cap dispositiu filtri dades
- **AdBlock** per impedir el seguiment

**Flux de treball**:
1. Activar la correcció TTL abans de fer servir el dispositiu
2. Aleatoritzar l’adreça MAC
3. Mantenir actiu el detector d’IMSI catchers
4. Fer servir AdBlock a tots els dispositius connectats
5. Registrar activitats cel·lulars sospitoses

**Integració amb RayHunter**: detecció avançada d’IMSI catchers, més enllà del monitoratge bàsic.

### Cas d’ús 3: administrador de xarxa

**Perfil**: administrador de TI que gestiona diversos centres

**Eines DagShell utilitzades**:
- **Wardriving WiFi** per verificar la cobertura
- **Escàner ARP** per inventariar dispositius
- **Escàner de ports** per a auditories de seguretat
- **Monitor de connexions actives** per detectar trànsit no autoritzat
- **Gestor de tallafoc** per bloquejar IP

**Flux de treball**:
1. Recórrer el centre per validar la cobertura WiFi
2. Fer un escaneig ARP per descobrir tots els dispositius de xarxa
3. Escanejar els servidors per trobar serveis exposats
4. Bloquejar IP malicioses amb el tallafoc
5. Exportar informes per documentar la feina

**Integració amb RayHunter**: monitoratge de la seguretat cel·lular en centres amb dispositius mòbils.

### Cas d’ús 4: investigador de seguretat IoT

**Perfil**: investigador que analitza la seguretat dels dispositius IoT

**Eines DagShell utilitzades**:
- **Escàner ARP** amb cerca OUI per identificar dispositius IoT
- **Escàner de ports** per trobar serveis oberts
- **Sniffer DNS** per capturar patrons de trànsit IoT
- **Escàner Bluetooth** (Pi) per a dispositius IoT BLE
- **Traceroute** per analitzar la connectivitat

**Flux de treball**:
1. Desplegar Orbic i Pi en un entorn de proves
2. Fer un escaneig ARP per descobrir dispositius IoT
3. Buscar serveis vulnerables amb l’escàner de ports
4. Escanejar BLE per trobar dispositius IoT Bluetooth
5. Analitzar consultes DNS per entendre les connexions dels dispositius cap a fora
6. Documentar vulnerabilitats

**Integració amb RayHunter**: detecta si els dispositius IoT tenen connectivitat cel·lular i en monitoritza les anomalies.

{{< figure src="dagshell-rayhunter-combined-mobile-security-research-use-cases.webp" alt="Diagrama de quatre casos d’ús reals de DagShell i RayHunter: investigador de seguretat, defensor de la privacitat, administrador de xarxa i investigador IoT" >}}

______

## Consideracions legals i ètiques

### Marc legal

**Eines com DagShell es troben en zones grises legals**:

**Usos legals**:
✅ **Xarxes pròpies**: prova els teus dispositius i xarxes\
✅ **Proves autoritzades**: proves de penetració amb permís escrit\
✅ **Finalitats educatives**: aprenentatge en laboratoris aïllats\
✅ **Protecció de la privacitat**: correcció TTL i suplantació MAC al teu dispositiu\
✅ **Recerca de seguretat**: recerca de vulnerabilitats amb divulgació responsable

**Usos il·legals**:
❌ **Accés no autoritzat**: atacar xarxes que no són teves (infracció de la CFAA)\
❌ **Atacs de desautenticació** contra altres xarxes (infracció de la FCC i possibles càrrecs penals)\
❌ Atacs **Evil Twin** contra el públic (frau electrònic i robatori d’identitat)\
❌ **Sniffing DNS** d’altres persones sense consentiment (intercepció de comunicacions)\
❌ **Eludir la seguretat** per cometre frau

### Lleis que convé conèixer

**Estats Units**:
- **Computer Fraud and Abuse Act (CFAA)**: accés no autoritzat a ordinadors i xarxes
- **Wiretap Act**: interceptació de comunicacions electròniques
- **Normativa de la FCC**: interferències de radiofreqüència (atacs de desautenticació)

**Regne Unit**:
- **Computer Misuse Act 1990**: similar a la CFAA
- **Regulation of Investigatory Powers Act (RIPA)**: restriccions d’interceptació

**Unió Europea**:
- **RGPD**: protecció de dades (escaneig Bluetooth/WiFi de dades identificables)
- *La normativa local varia per país i també en varia l’aplicació.*

### Pautes ètiques

**Fes-ho**:
- ✅ Fes servir les eines als **teus dispositius i xarxes**
- ✅ Obtingues **permís escrit** abans de provar sistemes d’altres persones
- ✅ Practica la **divulgació responsable** si trobes vulnerabilitats
- ✅ Limita l’**ús educatiu** als entorns controlats
- ✅ Protegeix **la teva privacitat**

**No ho facis**:
- ❌ No ataquis xarxes que no són teves
- ❌ No recullis credencials de desconeguts
- ❌ No interfereixis amb infraestructures crítiques
- ❌ No facis servir les eines amb finalitats malicioses
- ❌ No distribueixis dades capturades

### Declaració d’ús responsable

DagShell és una **eina de recerca de seguretat i privacitat**. Les seves capacitats són semblants a les d’eines professionals de proves de penetració com **Kali Linux**, **WiFi Pineapple** o **HackRF**.

**La intenció importa**: tant els **hackers maliciosos** com els **professionals de seguretat** fan servir eines semblants. La diferència és:
- **Autorització** (permís per fer proves)
- **Intenció** (millorar la seguretat o causar danys)
- **Divulgació** (informar dels resultats o explotar-los)

Fes servir DagShell de manera **responsable** i **ètica**. *Si no saps si una acció és legal, atura’t i consulta un advocat abans de continuar.*

{{< figure src="dagshell-legal-ethical-security-research-responsible-use.webp" alt="Marc legal i ètic per a la recerca de seguretat amb DagShell, amb usos autoritzats i no autoritzats i les lleis pertinents" >}}

______

## Resolució de problemes

### Problemes d’instal·lació

**Problema**: `enable_shell.py` no es pot connectar

**Solucions**:
- Verifica que estiguis connectat al **WiFi de l’Orbic**
- Comprova que l’adreça IP sigui **192.168.1.1** (predeterminada)
- Torna a provar la contrasenya d’administrador (distingeix majúscules i minúscules)
- Comprova si el port 80 és accessible: `telnet 192.168.1.1 80`

**Problema**: falla la pujada del firmware

**Solucions**:
- Assegura’t d’haver activat primer el shell root (`enable_shell.py` ha d’haver funcionat)
- Comprova l’estabilitat de la xarxa (fes servir una connexió per cable si és possible)
- Prova `deploy_net.py` en lloc de `deploy_base64.py`
- Verifica que la partició `/data` tingui espai: `df -h /data`

**Problema**: l’avís del certificat no desapareix

**Solucions**:
- *És **normal** amb certificats autosignats: la connexió continua xifrada.*
- Fes clic a «Advanced» i després a «Proceed anyway» cada vegada
- **Opcional**: instal·la `root.der` al magatzem de confiança del dispositiu (opció avançada)

### Problemes d’execució

**Problema**: DagShell no s’inicia en arrencar

**Solucions**:
- Comprova l’script d’arrencada: `ls -la /etc/rc.d/dagshell_boot.sh`
- Verifica que sigui executable: `chmod +x /etc/rc.d/dagshell_boot.sh`
- Consulta els registres: `logread | grep dagshell`
- Inicia’l manualment: `/data/orbic_app &`

**Problema**: el GPS no funciona

**Solucions**:
- Verifica que el **Pi complementari** estigui en execució: `systemctl status pi-companion`
- Comprova si el GPS té senyal de satèl·lit: `cgps -s` (al Pi)
- Assegura’t que el dongle GPS estigui connectat: `lsusb`
- *Espera entre 5 i 10 minuts per obtenir el primer fix GPS. La primera adquisició pot trigar més a l’exterior.*

**Problema**: el wardriving no registra dades

**Solucions**:
- Espera que el GPS tingui fix abans de començar
- Comprova que `/data` tingui permisos d’escriptura
- Verifica que es creï el CSV: `ls -la /data/wardrive_log.csv`
- Comprova que la interfície WiFi estigui activa: `ifconfig wlan0`

**Problema**: el Pi complementari no es comunica amb l’Orbic

**Solucions**:
- Verifica la connectivitat de xarxa: `ping 192.168.1.1`
- Comprova que el fitxer de configuració tingui l’adreça IP correcta
- Assegura’t que el port 8443 estigui obert: `telnet 192.168.1.1 8443`
- Consulta els registres del Pi complementari: `journalctl -u pi-companion`

### Problemes de rendiment

**Problema**: la interfície web és lenta o va a batzegades

**Solucions**:
- Esborra la memòria cau del navegador
- Desactiva les extensions del navegador (els bloquejadors d’anuncis poden interferir)
- Connecta l’Orbic **per cable** en lloc de WiFi
- Reinicia DagShell: `killall orbic_app && /data/orbic_app &`

**Problema**: els escaneigs de wardriving triguen massa

**Solucions**:
- Augmenta l’interval d’escaneig als paràmetres (redueix la freqüència per millorar el rendiment)
- Redueix el nombre de canals escanejats
- *Un fix GPS feble alenteix els escaneigs: el sistema espera coordenades vàlides abans de registrar-les.*

{{< figure src="dagshell-troubleshooting-installation-gps-wardriving-common-issues.webp" alt="Flux de resolució de problemes DagShell amb errors habituals d’instal·lació, GPS i wardriving i les seves solucions pas a pas" >}}

______

## Configuració avançada

### Personalitzar DagShell

**Modificar el codi font**:
- Edita els fitxers del directori `orbic_fw_c/`
- Torna a compilar amb `build.sh` o `build.ps1`
- Torna a desplegar el firmware

**Afegir pàgines personalitzades**:
- DagShell incrusta HTML al codi C++
- Edita `main.cpp` per afegir rutes
- Torna a compilar i desplegar

**Certificat personalitzat**:
- Genera la teva PKI amb `gen_pki.py`
- O fes servir **OpenSSL** per crear certificats
- Substitueix `root.der` i `server.der`

### Integració amb altres eines

**Exportar dades a Wireshark**:
```bash
# Captura el fitxer pcap
tcpdump -i wlan0 -w /data/capture.pcap

# Baixa-ho amb el navegador de fitxers
# Obre-ho a Wireshark al PC
```

**Importar traces GPS a QGIS**:
```bash
# Exporta-ho en format GPX
python gps_to_gpx.py /data/gps_coords.txt

# Importa-ho a QGIS com a capa vectorial
```

**Sincronitzar amb una base de dades externa**:
```python
# Script personalitzat per pujar dades de wardrive a MySQL
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="your_server",
    user="username",
    password="password",
    database="wardriving"
)

with open('/data/wardrive_log.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO networks (ssid, bssid, lat, lon) VALUES (%s, %s, %s, %s)",
                      (row['SSID'], row['MAC'], row['Latitude'], row['Longitude']))
conn.commit()
```

### Ajust de rendiment

**Optimitzar la velocitat d’escaneig**:
```bash
# Edita l'interval d'escaneig wardrive
# A la interfície web de DagShell, canvia de 5s a 3s per escanejar més ràpid
# A canvi, augmenta l'ús de CPU i es poden perdre xarxes
```

**Optimitzar la bateria** (si fas servir una bateria externa):
```bash
# Redueix la brillantor de la pantalla de l'Orbic
# Desactiva les funcions que no facis servir (BT i GPS quan no calguin)
# Fes servir el mode de repòs entre sessions de wardrive
```

______

## Comparació amb alternatives

### DagShell o WiFi Pineapple

| Funció | DagShell (Orbic RCL400) | WiFi Pineapple |
|---------|------------------------|----------------|
| **Preu** | $60-80 + dispositiu | $99-299 |
| **Connexió mòbil** | ✅ 4G LTE integrat | ❌ No (només WiFi) |
| **GPS** | ✅ Mitjançant el Pi complementari | ⚠️ Mitjançant dongle USB |
| **Evil Twin** | ✅ Sí | ✅ Sí |
| **Portal captiu** | ✅ Sí | ✅ Sí |
| **Desautenticació** | ✅ Sí (mitjançant Pi) | ✅ Sí |
| **Wardriving** | ✅ Sí | ✅ Sí |
| **Detecció d’IMSI** | ✅ Bàsica | ❌ No |
| **Portabilitat** | ✅ Molt portàtil | ⚠️ Moderada |
| **Bateria** | ✅ Integrada | ⚠️ Cal una bateria externa |
| **Corba d’aprenentatge** | Moderada | Baixa (interfície polida) |

**Guanyador**: DagShell per a la **seguretat mòbil amb connexió cel·lular**. Pineapple per a proves **centrades en WiFi** amb una interfície senzilla.

### DagShell o Kali Linux en un Pi

| Funció | DagShell | Kali en un Pi |
|---------|----------|-----------|
| **Temps de configuració** | 15 minuts | 2-3 hores |
| **LTE mòbil** | ✅ Integrat | ❌ Requereix un mòdem USB |
| **Interfície web** | ✅ Sí | ⚠️ Limitada (requereix VNC/SSH) |
| **Nombre d’eines** | ~15 | 600+ |
| **Especialització** | Seguretat mòbil | Proves de penetració generals |
| **Portabilitat** | ✅ Mida de butxaca | ⚠️ Requereix pantalla i alimentació |
| **Autonomia de bateria** | 8-10 hores | 2-4 hores |

**Guanyador**: DagShell per a tasques **específiques de mobilitat**. Kali per a un conjunt d’eines **més complet**.

### DagShell o firmware original de l’Orbic

| Funció | DagShell | Firmware original |
|---------|----------|----------------|
| **Eines de seguretat** | ✅ Àmplies | ❌ Cap |
| **Funcions de privacitat** | ✅ Sí | ❌ Mínimes |
| **Personalització** | ✅ Totalment personalitzable | ❌ Bloquejat |
| **Wardriving** | ✅ Sí | ❌ No |
| **GPS** | ✅ Sí (mitjançant Pi) | ❌ No |
| **Codi obert** | ✅ Sí | ❌ Propietari |
| **Assistència** | ⚠️ De la comunitat | ✅ Oficial |
| **Estabilitat** | ⚠️ Beta | ✅ Producció |

**Guanyador**: DagShell per a **investigadors**. El firmware original per a **usuaris ocasionals**.

______

## Conclusió: un laboratori mòbil complet

**DagShell** converteix el **hotspot Orbic RCL400** en un **laboratori mòbil de seguretat** que combina:

✅ **Protecció de la privacitat** (emmascarament TTL, suplantació MAC, AdBlock)
✅ **Monitoratge de xarxa** (connexions, DNS, encaminament)
✅ **Eines de hacking** (detecció d’IMSI, escaneig de ports, detecció ARP)
✅ **Capacitats d’atac** (Evil Twin, portal captiu, desautenticació)
✅ **Wardriving amb GPS** i integració amb Wigle
✅ **Ampliació amb Raspberry Pi** (BLE, WiFi, GPS)
✅ **Portàtil i alimentat per bateria**
✅ **De codi obert i personalitzable**

### En combinació amb RayHunter

**RayHunter + DagShell** = **Plataforma completa de seguretat mòbil**:
- **RayHunter** aporta detecció avançada d’IMSI catchers
- **DagShell** aporta eines ofensives i de privacitat
- Tots dos funcionen **alhora** al mateix dispositiu
- Capacitats **complementàries**, sense solapament
- **Un únic paquet portàtil** per a totes les necessitats de seguretat mòbil

### Comença avui

**Opció 1: Preparat i flashejat** (més fàcil)
- **STS Collective**: [Orbic RCL400 amb RayHunter + DagShell](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
- Arriba **preparat per fer servir**
- Sense complicacions d’instal·lació
- Configurat per professionals

**Opció 2: Instal·lació pròpia**
- Segueix aquesta guia
- **Gratuïta** si ja tens un Orbic RCL400
- Aprèn el procés d’instal·lació
- Personalitza’l segons les teves necessitats

### Lectures relacionades

- **[Com flashejar dispositius RayHunter: guia completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** - Instal·la RayHunter primer
- **[Comparació de dispositius RayHunter: anàlisi completa](/articles/rayhunter-device-comparison-2026-complete-review/)** - Tria la plataforma
- **[Projecte Flock-You: guia de maquinari contra la vigilància](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** - Més eines de detecció

### Reflexions finals

Tant si ets **investigador de seguretat**, **pentester**, **defensor de la privacitat** o **administrador de xarxes**, DagShell ofereix una plataforma **portàtil, capaç i assequible** per treballar en seguretat mòbil.

**Avís legal**: Fes-ne un ús responsable. Prova només xarxes i dispositius de la teva propietat o per als quals tinguis permís explícit per escrit. Respecta la llei i l’ètica, i bona pràctica de hacking! 🚀

{{< figure src="dagshell-orbic-rcl400-mobile-security-lab-conclusion-overview.webp" alt="Hotspot Orbic RCL400 amb firmware DagShell que funciona com a laboratori portàtil complet de recerca en seguretat mòbil" >}}


______

## Referències

1. [Repositori GitHub de DagShell](https://github.com/dagnazty/DagShell)
2. [Documentació de DagShell](https://dagnazty.github.io/DagShell/)
3. [STS Collective - Dispositius preflashejats](https://stscollective.com/products/orbic-rcl400-rayhunter-dagshell-hotspot)
4. [WiGLE - Projecte de cartografia WiFi](https://wigle.net/)
5. [Llei contra el frau i l’abús informàtic (CFAA)](https://www.law.cornell.edu/uscode/text/18/1030)
6. [Documentació oficial de Raspberry Pi](https://www.raspberrypi.org/documentation/)
7. [Documentació del mòdul GPS U-Blox](https://www.u-blox.com/)
8. [Base de dades OUI - Estàndards IEEE](https://standards.ieee.org/products-programs/regauth/)
9. [Tutorial d’iptables](https://www.netfilter.org/documentation/)
10. [Documentació d’OpenSSL](https://www.openssl.org/docs/)
