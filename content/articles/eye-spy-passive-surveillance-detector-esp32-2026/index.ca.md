---
title: "Eye Spy: detector passiu de vigilància i rastrejadors per a ESP32"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Referència tècnica d’Eye Spy v1.1, un detector passiu de BLE i WiFi amb ESP32 per a càmeres, rastrejadors, drons i senyals relacionats."
genre: ["Eines de privadesa", "Contra-vigilància", "Seguretat IoT", "Sistemes encastats", "Recerca en seguretat", "Seguretat WiFi", "Seguretat Bluetooth", "Projectes ESP32", "Seguretat del maquinari", "Seguretat de codi obert"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "Detecció de vigilància", "Contra-vigilància", "Detecció BLE", "Escaneig WiFi", "Detecció d’AirTag", "Detecció ALPR", "Flock Safety", "Detecció de càmeres corporals", "Detecció de drons", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "Codi obert", "Privadesa", "BLE passiu", "Mode monitor", "Detecció OUI", "Detecció de rastrejadors", "Càmera corporal Axon", "Ray-Ban Meta", "Samsung SmartTag", "Rastreador Tile", "Càmera oculta", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "Il·lustració d’un petit M5Stack Atom Lite envoltat d’ones de senyal de colors sobre un fons blau marí fosc, que representa la detecció de vigilància per Bluetooth i WiFi."
coverCaption: ""
---

**Un sensor passiu de la mida d’un polze que t’avisa quan alguna cosa t’observa**

## Introducció: el panorama de vigilància que no veus

El món físic disposa cada cop de més dispositius que observen, enregistren i segueixen les persones: lectors de matrícules als encreuaments, càmeres corporals dels cossos policials, càmeres en habitatges de lloguer, rastrejadors comercials semblants als AirTag amagats en bosses o cotxes, i càmeres de vigilància a les entrades de les botigues. La majoria d’aquests dispositius es comuniquen sense fil mitjançant **Bluetooth LE** o **WiFi**. *La major part d’aquestes comunicacions s’emet a l’aire i qualsevol persona amb el receptor adequat les pot detectar.*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy) és una eina passiva de detecció de vigilància que aprofita exactament aquest fet. Eye Spy funciona al **M5Stack Atom Lite**, una placa de desenvolupament ESP32-PICO-D4 de la mida aproximada d’un terròs de sucre, i supervisa contínuament les bandes BLE i WiFi per cercar les signatures electròniques de dispositius de gravació, càmeres de vigilància, sistemes **ALPR** (lectors automàtics de matrícules), drons i rastrejadors personals. Quan troba un senyal, canvia el color del seu LED RGB.

*No es connecta a res ni transmet res.* Observa, assigna puntuacions i s’il·lumina.

Aquest article és una referència tècnica completa. Explica què detecta Eye Spy, com funciona el sistema de puntuació de confiança, com estan dissenyats els motors de detecció, com construir i flashejar el dispositiu i quines limitacions pràctiques té.

**T’estimes més no construir-lo?** STS Collective ofereix **[detectors Eye Spy](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)** preconfigurats i llestos per fer servir. El codi per a lectors **SIMEONONSECURITY** ofereix fins a un 20 % de descompte.

{{< stscollective-ad "eyespy" >}}

---

## Indicadors LED: tota la interfície d’usuari

Com l’[ESP32 WiFi Canary: detecció passiva d’amenaces a 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/), tota la sortida d’Eye Spy és un únic NeoPixel RGB SK6812 connectat al GPIO 27 de l’M5Stack Atom Lite. El LED comunica contínuament un dels quatre nivells d’amenaça:

| Color | Significat | Interval de puntuació |
|-------|-------------|---------------------|
| 🔵 Pols blau | Inici / primera exploració | -- |
| 🟢 Verd fix | No s’ha detectat res | 0–2 |
| 🟡 Groc fix | Atenció: podria haver-hi un dispositiu de gravació a prop | 3–5 |
| 🔴 Vermell intermitent | Alerta: s’ha detectat un dispositiu de vigilància o seguiment | 6+ |

**Una sola detecció d’alta confiança (càmera corporal Axon, càmera Flock Safety, coincidència d’OUI ALPR o AirTag) suma prou punts per posar immediatament el LED en vermell en un sol cicle de detecció.** Diverses deteccions de confiança mitjana s’acumulen fins al groc i es poden combinar per arribar al vermell.

---

## Maquinari

### Objectiu principal: M5Stack Atom Lite

| Peça | Detall |
|-----------|--------|
| Placa | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | NeoPixel SK6812 al GPIO 27 |
| Botó | GPIO 39 (només entrada) |
| Flaix | 4 MB |

L’Atom Lite és una plataforma completa i autònoma. **No cal soldar, fer servir una placa de proves ni afegir components externs.** Connecta’l a l’USB i ja funciona.

### ESP32 DevKit genèric

Un segon entorn de compilació de PlatformIO (`esp32dev`) serveix per a qualsevol ESP32 DevKit estàndard amb un LED integrat al GPIO 2. Tota la lògica de detecció funciona igual. Aquesta compilació és útil per desenvolupar i provar la lògica, o per implementar-la quan no cal el format de l’Atom Lite.

---

## El sistema de puntuació

Eye Spy utilitza un **model de puntuació de confiança** que combina els senyals de tots els motors de detecció en un únic nombre enter. La puntuació determina l’estat del LED (verd, groc o vermell) i queda subjecta a dos mecanismes de gestió automàtica:

### Reducció de la puntuació

Si no hi ha noves deteccions, la puntuació baixa **1 punt cada 60 segons**. Si t’allunyes d’un dispositiu detectat, el LED torna al verd en uns quants minuts sense intervenció teva.

### Temps d’espera per puntuar de nou

Cada *tipus* de detecció té un **temps d’espera de 120 segons** abans que la mateixa font pugui tornar a sumar punts. *Això impedeix que un dispositiu persistent acumuli punts indefinidament.* Una càmera Flock Safety que es manté dins del radi suma +5 una vegada i espera 120 segons abans de tornar-hi a contribuir.

Aquests dos mecanismes junts volen dir que:

- **Les deteccions passatgeres** (per exemple, un cotxe amb un AirTag que passa) es resolen automàticament.
- **La vigilància persistent** (per exemple, càmeres corporals desplegades en un lloc fix) manté el LED en alerta mentre et mantinguis dins del radi.
- **Un dispositiu no provoca una acumulació descontrolada** de punts només perquè es detecta sovint.

---

## Motors de detecció

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Diagrama dels motors BLE i WiFi paral·lels d’Eye Spy: cerquen AirTag, càmeres corporals, sistemes ALPR i drons, i envien els resultats al model d’amenaça amb puntuació de confiança" >}}

Eye Spy alterna contínuament tres fases d’exploració:

**BLE passiu (9 s) → exploració WiFi (~3 s) → captura promíscua (5 s) → repetir**

Eye Spy atura explícitament el BLE abans de qualsevol operació WiFi per respectar la ràdio compartida de l’ESP32. El BLE es reinicia al començament de cada cicle.

---

### Motor 1: BLE, exploració passiva

L’exploració BLE fa servir **NimBLE sense transmetre sol·licituds d’exploració**. El dispositiu escolta paquets d’anunci BLE sense enviar cap resposta. *Això fa que Eye Spy sigui electrònicament invisible per als dispositius que cerca: l’objectiu no pot detectar un escàner passiu.*

Per reduir els falsos positius en entorns densos, s’ignoren els dispositius amb un senyal inferior a **−90 dBm**.

#### Taula de detecció BLE

| # | Objectiu | Mètode de detecció | Punts |
|---|--------|-----------------|-------|
| 1 | **Càmera corporal Axon** | OUI de la MAC BLE `00:25:df` (càmeres corporals, dispositius Taser i equips policials d’Axon) | +5 🔴 |
| 2 | **Ulleres intel·ligents Ray-Ban Meta** | UUID del servei BLE `0xFD5F` | +5 🔴 |
| 3 | **BLE de Flock Safety** | El nom BLE conté `Flock`, `Penguin`, `Pigvision` o `FS Ext Battery` | +5 🔴 |
| 4 | **Skimmer de targetes (HC-03/05/06)** | Coincidència exacta del nom BLE: mòduls Bluetooth habituals en cobertes de terminals de pagament | +5 🔴 |
| 5 | **Apple AirTag** | Dades del fabricant `0x004C`, subtipus `0x12`/`0x1E`, o càrrega útil `1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **Dron (OpenDroneID BLE)** | UUID del servei BLE `0xFFFA` o càrrega útil de dades del servei AD amb el codi d’aplicació `0x0D` | +4 🔴 |
| 7 | **Samsung SmartTag** | UUID del servei BLE `0xFD5A` | +3 🟡 |
| 8 | **Rastreador Tile** | UUID del servei BLE `0xFEED` o `0xFEEC` | +3 🟡 |
| 9 | **Node MeshCore** | Prefix del nom del dispositiu BLE `MeshCore-` | +2 🟡 |
| 10 | **iBeacon (seguiment en comerços i recintes)** | Dades del fabricant `0x004C 0x02 0x15`; es fa servir en botigues, aeroports i estadis per seguir els moviments | +2 🟡 |
| 11 | **Dispositiu persistent desconegut** | MAC BLE no classificada detectada com a mínim 3 cops en 5 minuts o més (detecció d’exploradors o perseguidors) | +2 🟡 |

#### Detalls de deteccions BLE destacades

**Càmera corporal Axon (+5)**: Axon (abans TASER International) fabrica alguns dels sistemes de càmera corporal més estesos entre les forces de l’ordre dels Estats Units. L’OUI `00:25:df` està registrat a Axon i apareix als seus dispositius portàtils. **Una detecció arriba immediatament al llindar d’alerta.**

**Ulleres intel·ligents Ray-Ban Meta (+5)**: La col·laboració Ray-Ban Meta produeix ulleres intel·ligents de consum que poden gravar vídeo i fer fotos. L’UUID del servei BLE `0xFD5F` és l’anunci característic d’aquests dispositius. *Són productes de consum i poden aparèixer en espais públics concorreguts.* Val la pena parar atenció a una detecció d’aquest nivell, sigui quina sigui la intenció de qui les porta.

**Mòduls Bluetooth de skimmers de targetes (+5)**: HC-03, HC-05 i HC-06 són mòduls Bluetooth sèrie econòmics que sovint es troben en dispositius superposats als terminals de pagament i en equips per clonar caixers automàtics. La detecció compara el nom exacte del dispositiu amb els noms predeterminats coneguts del microprogramari d’aquests mòduls. **Una alerta vermella justifica inspeccionar físicament els terminals de pagament propers.**

**Apple AirTag (+4)**: Els AirTag anuncien la seva presència amb el protocol propietari d’Apple **Nearby Interaction**. La detecció cerca la capçalera de dades específica del fabricant (`0x004C` = Apple) i els subtipus específics de l’AirTag (`0x12` per a l’anunci estàndard, `0x1E` per a l’anunci d’objecte perdut). Els patrons de la càrrega útil en brut proporcionen una ruta de detecció redundant.

**OpenDroneID BLE (+4)**: La norma **ASTM F3411 Remote ID**, també adoptada per la FAA per als drons comercials dels Estats Units, defineix un protocol de difusió perquè els drons anunciïn la seva identitat i posició. Eye Spy cerca l’UUID de servei GATT `0xFFFA` (el servei Remote ID designat) i el codi d’aplicació `0x0D` a la càrrega útil de dades de servei AD. *Un dron comercial proper que compleixi la norma activarà aquesta detecció.*

**Dispositiu persistent desconegut (+2)**: Aquest és el motor de **detecció de seguiment**. Fa un seguiment de qualsevol MAC BLE que no classifiquin les deteccions específiques anteriors. S’hi assignen punts si la mateixa MAC no classificada apareix tres cops o més durant almenys cinc minuts. El rastrejador de persistència pot observar fins a 50 MAC desconegudes alhora i suprimeix els registres després de 30 minuts sense senyal. **Això ajuda a detectar rastrejadors personalitzats o modificats que no coincideixen amb cap UUID de servei o patró de fabricant conegut.**

**iBeacon (+2)**: Els comerços, aeroports i estadis utilitzen el format iBeacon d’Apple (`0x4C 0x00 0x02 0x15`) per seguir els moviments dels dispositius en espais físics. La detecció s’activa amb el format d’anunci estàndard, independentment de l’UUID: s’adreça al tipus d’instal·lació, no a un UUID concret. *Una detecció aquí vol dir que probablement ets en un lloc que segueix activament la presència de dispositius Bluetooth.*

---

### Motor 2: exploració WiFi, cerca activa de canals

El motor d’exploració WiFi fa servir la interfície estàndard de cerca de punts d’accés de l’ESP32 per enumerar els punts d’accés propers i comparar-ne els BSSID i SSID amb les empremtes conegudes de dispositius de vigilància.

#### Taula de detecció WiFi

| # | Objectiu | Mètode de detecció | Punts |
|---|--------|-----------------|-------|
| 12 | **Càmera Flock Safety (OUI)** | El BSSID coincideix amb la taula Flock Safety de 22 OUI (`d4:bb:e6`, `3c:61:05` i prefixos FS-Ext-Battery) | +5 🔴 |
| 13 | **Càmera ALPR / LPR (OUI)** | El BSSID coincideix amb l’OUI `00:0e:58` de Motorola Solutions / Vigilant Solutions | +5 🔴 |
| 14 | **SSID amb paraules clau de Flock** | L’SSID conté `flock`, `flocksafety`, `fs ext`, `penguin` o `pigvision` | +5 🔴 |
| 15 | **SSID amb paraules clau d’ALPR** | L’SSID conté `alpr`, `lpr`, `vigilant`, `plateread`, `licenseplat`, `motorola` o `automate` | +4 🔴 |
| 16 | **Fabricant de càmeres de vigilància (OUI)** | El BSSID coincideix amb una taula de 31 OUI de càmeres: Hikvision, Dahua, Axis, Ring, Nest, Arlo, Wyze, Reolink, FLIR, Amcrest, Vivotek, Hanwha, Mobotix o Ubiquiti UniFi | +3 🟡 |
| 17 | **SSID amb paraules clau de càmeres** | L’SSID conté, entre d’altres, `cam`, `ipcam`, `cctv`, `nvr`, `dvr`, `doorbell`, `surv`, `blink`, `lorex`, `protect` o `genetec` | +2 🟡 |

#### Taula OUI de Flock Safety

La taula `FLOCK_OUIS`, amb 22 entrades, és la cerca més detallada del projecte. Inclou:

- `d4:bb:e6`: OUI de Flock Safety registrat per l’IEEE.
- `3c:61:05`: OUI de Flock Safety registrat per l’IEEE.
- 20 prefixos MAC addicionals observats al camp en bateries Flock FS-Ext-Battery i càmeres WiFi de Flock.

Aquestes 22 entrades representen rangs de MAC de maquinari observats en sistemes de càmeres ALPR de Flock Safety desplegats. **La detecció per OUI és independent de l’SSID**: una càmera Flock amb un SSID que no contingui paraules clau encara suma +5 si coincideix l’OUI del BSSID.

Els OUI de Flock Safety i Vigilant Solutions són en taules separades perquè puguin sumar punts de manera independent dins del mateix cicle d’exploració. *Un lloc amb aparells dels dos fabricants podria acumular +10 en una única passada de WiFi.*

#### Taula OUI de fabricants de càmeres de vigilància

La taula de 31 càmeres de vigilància cobreix els principals fabricants de càmeres IP que podrien aparèixer en instal·lacions comercials, residencials i de botigues:

- **Empreses i ús comercial**: Hikvision, Dahua, Axis, Vivotek, Hanwha (Samsung Techwin), Mobotix i Genetec.
- **Consum i oficines petites**: Ring, Nest, Arlo, Wyze, Reolink, Blink, Lorex i Amcrest.
- **Infraestructura**: Ubiquiti UniFi (els punts d’accés i les càmeres comparteixen rangs OUI) i FLIR.

Una coincidència suma +3, el nivell d’atenció, encara que no hi hagi confirmació per paraula clau. Si també coincideix un SSID amb paraula clau, la mateixa xarxa de càmeres suma +3 per l’OUI i +2 més per l’SSID, i arriba a l’alerta en un cicle d’exploració.

---

### Motor 3: WiFi promiscu, captura passiva de trames

El motor promiscu posa la ràdio ESP32 en **mode monitor** i captura trames de gestió 802.11 sense processar. Això permet detectar dispositius que no anuncien un SSID, concretament drons que fan servir el protocol **Remote ID** per **WiFi Neighbor Awareness Networking (NaN)**.

Durant la fase promíscua, la ràdio **salta entre els canals** `{1, 6, 11, 3, 8, 13}` cada 400 ms per ampliar la cobertura dels canals de difusió de trames NaN dels drons.

#### Taula de detecció promíscua

| # | Objectiu | Mètode de detecció | Punts |
|---|--------|-----------------|-------|
| 18 | **Dron (OpenDroneID WiFi NaN)** | Trama de gestió 802.11 destinada a `51:6f:9a:01:00:00`: difusió Remote ID segons ASTM F3411 | +4 🔴 |

**OpenDroneID WiFi NaN (+4)**: La norma ASTM F3411 defineix l’adreça multicast `51:6f:9a:01:00:00` per a totes les trames Remote ID de WiFi NaN. Els drons comercials regulats que transmeten la posició i la identitat per WiFi envien trames a aquesta adreça. Eye Spy observa passivament i de manera fiable les trames de gestió adreçades a aquesta MAC multicast. *L’operador del dron hauria de desactivar completament Remote ID per evitar-ho, cosa que infringiria les normes aplicables.*

Aquesta detecció complementa el motor OpenDroneID BLE (detecció núm. 6). *Un dron pot anunciar-se per BLE, WiFi o tots dos, segons el maquinari i la configuració.* Eye Spy cobreix ambdues opcions.

---

## Calendari de fases i gestió de la ràdio

```
BLE passiu (9 s) → exploració WiFi (~3 s) → captura promíscua (5 s) → repetir
```

L’ESP32-PICO-D4 té **una sola ràdio compartida de 2,4 GHz** per gestionar BLE i WiFi. Eye Spy la gestiona amb cura:

1. **Fase BLE** (9 segons): pila NimBLE activa, escaneig passiu en marxa i cap sol·licitud d’exploració transmesa.
2. **Aturada del BLE**: la pila BLE s’atura explícitament abans de fer servir WiFi.
3. **Exploració WiFi** (~3 segons): cerca activa de punts d’accés a tots els canals i coincidència d’OUI i SSID.
4. **Captura promíscua** (5 segons): captura passiva de trames 802.11 amb salts de canal.
5. **Aturada del WiFi**: s’atura el WiFi i es reinicia el BLE per al cicle següent.

Aquesta gestió explícita de les fases evita conflictes de ràdio i dona als motors BLE i WiFi accés ordenat a la ràdio en cada cicle.

---

## Sortida sèrie

Totes les línies comencen amb `[eyespy]` per facilitar-ne el filtratge. El monitor sèrie funciona a **115200 bauds**.

### Inici

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### Cicle normal

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### Esdeveniments de detecció

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

El camp `tracked=N` mostra quantes MAC BLE úniques hi ha en aquell moment al rastrejador de persistència. Ajuda a entendre la densitat de l’entorn BLE.

### Camps de puntuació

Cada línia d’estat inclou:

- **score**: puntuació d’amenaça actual.
- **state**: `CLEAR` / `CAUTION` / `ALERT`.
- **phase**: motor actiu (`BLE` / `WIFI` / `PROMISC`).
- **tracked**: nombre de MAC BLE úniques a la taula de persistència.

---

## Compilació i flaixat

### Requisits

- **PlatformIO** (CLI o extensió de VS Code).
- **M5Stack Atom Lite** o qualsevol ESP32 DevKit.
- Cable USB-C.

### Dependències

PlatformIO les instal·la automàticament:

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel** controla el LED RGB SK6812. **NimBLE-Arduino** proporciona la pila d’escaneig BLE passiu. Es prefereix a la biblioteca BLE predeterminada de l’ESP32 perquè admet correctament el mode passiu, evita enviar paquets de sol·licitud d’exploració i consumeix menys memòria.

### Flaixar l’M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# Compilar i flaixar per a l’Atom Lite
pio run -e atom-lite -t upload

# Obrir el monitor sèrie a 115200 bauds
pio device monitor -b 115200
```

### Flaixar un ESP32 DevKit genèric

```bash
pio run -e esp32dev -t upload
```

### Estructura del projecte

```
eye-spy/
├── src/
│   └── main.cpp          # Tota la lògica del microprogramari
├── platformio.ini         # Entorns de compilació (atom-lite, esp32dev)
├── partitions_4mb.csv     # Taula de particions de flaix de 4 MB
└── README.md
```

### platformio.ini

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

*L’entorn `atom-lite` fa servir la definició de placa `m5stick-c`, amb el mateix xip ESP32-PICO-D4 i un mapa de pins compatible amb el NeoPixel del GPIO 27.*

---

## Notes sobre la detecció i limitacions pràctiques

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="Il·lustració d’estil fotogràfic de l’Eye Spy a l’M5Stack Atom Lite, aproximadament de la mida d’un terròs de sucre, subjectat entre dos dits per mostrar-ne la mida compacta" >}}

### Què no pot fer Eye Spy

**WiFi de 5 GHz**: L’ESP32 és un dispositiu **només de 2,4 GHz**. Les càmeres de vigilància, els sistemes ALPR i els punts d’accés que funcionen exclusivament a 5 GHz no seran visibles per als motors d’exploració WiFi o de captura promíscua. *Moltes càmeres IP modernes també funcionen a 2,4 GHz encara que admetin 5 GHz. Els desplegaments que només utilitzen 5 GHz no es detectaran.*

**BLE xifrat**: Alguns productes de vigilància de gamma alta xifren o ofusquen els seus anuncis BLE. Eye Spy detecta dispositius que emeten en text clar signatures identificables com ara OUI, UUID de servei i dades del fabricant. *Els dispositius que roten les adreces MAC, una funció de privadesa cada cop més habitual en els rastrejadors de consum, esquiven la detecció basada en MAC.* El rastrejador de persistència pot detectar-los només si roten amb una freqüència inferior a un canvi cada cinc minuts.

**Càmeres amb cable**: **Les càmeres IP connectades per Ethernet i que no fan servir una ràdio WiFi no emeten senyals sense fil que Eye Spy pugui detectar.** Les càmeres ocultes sense connexió de xarxa que només enregistren localment tampoc no generen cap signatura RF.

**Límits d’abast**: A l’interior, l’abast pràctic de recepció de senyals forts de l’antena ESP32 és de **20 a 40 metres**; els senyals febles o obstaculitzats arriben menys lluny. *Els dispositius al límit de l’abast o darrere d’un blindatge RF important poden no sumar punts o quedar per sota del llindar RSSI de −90 dBm.*

### Falsos positius previsibles

**Càmeres de consum a les cases veïnes**: Les càmeres Ring, Nest, Wyze, Arlo i Reolink són habituals als barris residencials i els seus OUI apareixen a la taula de 31 càmeres. *En zones residencials, és normal veure algunes alertes grogues d’atenció (+3) per les càmeres de timbre dels veïns.* No són falsos positius en sentit tècnic: el dispositiu *sí que detecta una càmera*. El context és important.

**Desplegaments comercials d’iBeacon**: Els grans distribuïdors instal·len infraestructura iBeacon pràcticament a totes les botigues. *Una visita a un centre comercial o supermercat probablement activarà la detecció d’iBeacon (+2).* El dispositiu funciona com s’espera: la infraestructura de seguiment comercial hi és.

**Infraestructura Ubiquiti UniFi**: Els punts d’accés UniFi apareixen a la taula OUI de càmeres perquè Ubiquiti fabrica equips de xarxa i càmeres de seguretat amb rangs OUI que se solapen. *Una instal·lació amb equips UniFi pot sumar +3 per coincidències OUI del motor d’exploració WiFi.*

**Samsung SmartTag i dispositius de consum**: L’UUID SmartTag (`0xFD5A`) és un servei registrat per Samsung. *Els SmartTag són rastrejadors de consum amb usos personals legítims.* La presència d’un SmartTag a prop activarà aquesta detecció.

### Què significa cada nivell de puntuació a la pràctica

| Puntuació | Situació probable al món real |
|-------|-----------------------------|
| 6–10 (🔴) | Detecció creïble d’alta confiança: càmera Axon a uns 30 m, càmera Flock Safety amb OUI coincident, patró confirmat d’un AirTag que et segueix o dron que emet Remote ID |
| 3–5 (🟡) | Diversos rastrejadors de consum, càmeres veïnes que acumulen punts, possible càmera Flock o una detecció OpenDroneID aïllada |
| 0–2 (🟢) | No s’han detectat signatures importants de vigilància; hi ha comunicacions normals de dispositius de consum però per sota del llindar |

---

## Comparació amb projectes relacionats

Eye Spy s’adreça a la vigilància física de l’entorn; l’[ESP32 WiFi Canary: detecció passiva d’amenaces a 2,4 GHz](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/) detecta atacs WiFi de xarxa contra els teus dispositius. *Són eines complementàries per a models d’amenaça diferents.*

| Capacitat | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| Detecció d’AirTag i rastrejadors | ✅ | ❌ |
| Detecció de càmeres ALPR / Flock | ✅ | ❌ |
| Detecció de càmeres corporals | ✅ | ❌ |
| Detecció de drons (Remote ID) | ✅ | ❌ |
| Detecció de punts d’accés evil twin | ❌ | ✅ |
| Detecció d’atacs de desautenticació | ❌ | ✅ |
| Detecció de rebaixa de seguretat | ❌ | ✅ |
| Aprenentatge de línia de base | ❌ | ✅ |
| BLE passiu | ✅ | ❌ |
| Mateixa plataforma de maquinari | ✅ | ✅ |

Tots dos projectes funcionen amb el mateix maquinari M5Stack Atom Lite, fan servir els mateixos indicadors LED i el mateix sistema de compilació PlatformIO. Per tenir una visió de la vigilància física i de xarxa, pots flashejar cada projecte en un Atom Lite diferent i dur-los tots dos.

Eye Spy també complementa el [projecte de detecció Flock You](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/) per a qui es preocupa específicament per la infraestructura de vigilància ALPR.

---

## Casos d’ús

### Consciència de la vigilància propera

El públic principal d’Eye Spy és qualsevol persona que vulgui conèixer la infraestructura de vigilància que té a prop. Quan camines per un barri, passes amb cotxe per una intersecció o assisteixes a un acte públic, Eye Spy redueix l’anàlisi RF complexa a **un únic estat LED en temps real**.

### Detecció d’assetjament amb AirTag

L’assetjament amb AirTag és un problema documentat. El **motor de detecció de seguiment** d’Eye Spy (una MAC BLE desconeguda i persistent que es veu com a mínim 3 cops durant almenys 5 minuts) s’adreça a rastrejadors modificats o personalitzats que no coincideixen amb el format d’anunci conegut d’Apple. Juntament amb la detecció directa d’AirTag, ofereix **dues vies independents per detectar un rastrejador que et segueix**.

### Inspecció d’un habitatge de lloguer o d’una habitació d’hotel

Entrar en una habitació d’hotel o un habitatge de lloguer nou amb Eye Spy funcionant ofereix un primer indici de dispositius BLE i WiFi inesperats. Una coincidència d’SSID amb paraules clau de càmera o un OUI de vigilància a l’exploració WiFi suma punts d’atenció. *Això no substitueix un escombratge RF adequat*, però afegeix una capa ambiental passiva a la inspecció física.

### Desplegaments ALPR i recerca sobre privadesa

Els investigadors que documenten infraestructura de vigilància, els periodistes que treballen en entorns vigilats i els defensors de la privadesa poden fer servir Eye Spy com a equip de detecció portàtil i econòmic. La sortida sèrie registra cada detecció amb RSSI i és adequada per recopilar dades senzilles.

### Seguretat durant els viatges

Com el WiFi Canary, Eye Spy està pensat per viatjar. L’Atom Lite cap a qualsevol butxaca o es pot fixar a una bossa. Quan viatges per aeroports, estacions de tren o actes públics amb una vigilància densa coneguda, ofereix un monitoratge passiu continu sense que calgui interactuar-hi.

---

## Notes d’arquitectura

### Per què és important el BLE passiu

L’elecció de l’exploració BLE passiva, sense paquets de sol·licitud, té conseqüències importants per a la seguretat. En una exploració BLE estàndard, l’escàner transmet un paquet **SCAN_REQ** per demanar dades d’anunci addicionals a cada emissor. *Això fa que tant l’escàner com el dispositiu explorat puguin observar una exploració BLE activa*: el dispositiu explorat veu l’adreça de l’escàner dins la sol·licitud.

El mode passiu de NimBLE només escolta anuncis no dirigits (ADV_IND, ADV_NONCONN_IND, ADV_SCAN_IND) i no transmet mai un SCAN_REQ. **Eye Spy no transmet res per BLE durant la fase d’exploració.** Una càmera corporal Axon, un dispositiu Flock o un AirTag detectat no pot observar ni reaccionar a la presència de l’escàner.

### Disseny del rastrejador de persistència

El rastrejador de persistència de dispositius desconeguts manté una taula de fins a **50 adreces MAC BLE** amb les hores de la primera i l’última detecció. La detecció s’activa quan una MAC apareix com a mínim tres cops en un període de cinc minuts o més.

El límit de 50 entrades i la supressió al cap de 30 minuts són decisions d’enginyeria que equilibren la sensibilitat amb les limitacions de RAM de l’ESP32. *En un entorn BLE dens (transport públic, conferències o centres comercials), la taula es pot omplir ràpidament amb dispositius de consum.* El llindar RSSI de −90 dBm filtra els dispositius llunyans i concentra el seguiment en fonts properes i persistents.

### Interacció entre la reducció de puntuació i l’espera

L’**espera de 120 segons per tornar a puntuar** impedeix que un dispositiu que es manté sempre dins del radi acumuli punts a cada cicle BLE de nou segons. Sense aquesta espera, una sola càmera Flock sumaria +5 cada 15 segons i arribaria a centenars de punts en pocs minuts.

La **reducció d’1 punt cada 60 segons** fa baixar la puntuació després que el dispositiu surti del radi i l’espera s’acabi sense cap nova detecció. *Una detecció única de +5 que no es repeteix baixa a zero en cinc minuts.* Així, el dispositiu torna de manera natural a un estat de tranquil·litat adequat per als desplaçaments habituals.

---

## Contribucions i estat del projecte

Eye Spy està disponible amb la llicència Apache-2.0 a [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy).

Algunes possibilitats d’ampliació:

- **Afegir entrades OUI**: ampliar les taules OUI de Flock Safety i de càmeres quan es documentin noves MAC de maquinari.
- **Afegir UUID de servei BLE**: les noves ulleres intel·ligents, càmeres i rastrejadors incorporen UUID nous.
- **Ajustar el rastrejador de persistència**: el límit de 50 entrades, el llindar de 3 observacions i la finestra de 5 minuts són constants ajustables.
- **Registrar dades sèrie**: el format de sortida sèrie està pensat per a l’anàlisi programàtica. Un registrador extern podria agregar els esdeveniments de diverses unitats Eye Spy.

El microprogramari és en un únic fitxer `main.cpp` del directori `src/`, de manera que és fàcil llegir-lo, auditar-lo i modificar-lo.

---

## Conclusió

Eye Spy aborda un problema concret però important: l’entorn físic que t’envolta és cada vegada més equipat amb sistemes de vigilància, i la majoria emet signatures RF detectables. **Un M5Stack Atom Lite de 15 dòlars amb el microprogramari Eye Spy es converteix en un escàner ambiental continu** que transforma la complexitat de l’anàlisi de paquets BLE i de les cerques d’OUI WiFi en un únic LED RGB.

El model de puntuació de confiança reflecteix una ponderació realista de les amenaces: una càmera corporal Axon a prop d’una operació policial suma +5 i encén immediatament el LED vermell; un iBeacon comercial suma +2 i contribueix a la consciència de l’entorn sense activar una alarma falsa per si sol. La reducció de puntuació i els temps d’espera impedeixen que el dispositiu reaccioni excessivament a senyals passatgers o persistents de baix nivell.

Per a tasques de contra-vigilància, seguretat durant els viatges, detecció d’AirTag o simplement per saber si alguna cosa propera t’observa, Eye Spy és una eina pràctica, passiva i de codi obert que es mereix un lloc a l’equip de qualsevol professional de la seguretat.

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra detectors Eye Spy i estalvia un 20 %
{{< /centerbutton >}}
