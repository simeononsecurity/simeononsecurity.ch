---
title: "Detecció Flock-You: Guia de Configuració de Contra-Vigilància"
date: 2026-05-24
lastmod: 2026-11-19
toc: true
draft: false
description: "Guia tècnica completa del projecte de codi obert Flock-You per detectar càmeres ALPR de Flock Safety amb maquinari basat en ESP32. Inclou instruccions de configuració, detalls del microprogramari i opcions de compra."
genre: ["Maquinari de Seguretat", "Contra-Vigilància", "Tecnologia de Privacitat", "Projectes de Codi Obert", "Desenvolupament ESP32", "Monitoratge WiFi", "Eines de Privacitat", "Drets Digitals", "Hacking de Maquinari", "Seguretat de Xarxa"]
tags: ["Projecte Flock-You", "Detecció ALPR", "ESP32-S3", "Detecció WiFi OUI", "Maquinari de Contra-Vigilància", "Detecció Flock Safety", "Seguretat de Codi Obert", "Maquinari de Privacitat", "M5 Atom Lite", "OUI-SPY", "mesh-detect v2", "WiFi en Mode Promiscu", "Monitoratge 802.11", "Colonel Panic Tech", "STS Collective", "Dispositius de Privacitat", "Detecció de Vigilància", "Escaneig WiFi", "Projecte GitHub", "colonelpanichacks", "Microprogramari ESP32", "Guia de Configuració de Maquinari", "Eines de Privacitat DIY", "Monitoratge de Xarxa", "Base de Dades OUI", "Detecció de Sondes Comodí", "Anàlisi de Trames", "Detecció de Càmeres ALPR", "Tecnologia de Privacitat", "Maquinari de Detecció", "Arduino ESP32", "Platform.io", "Sistemes Encastats", "Detecció RF", "Processament de Senyals", "Enginyeria de Privacitat", "Contra-Tecnologia", "Investigació de Seguretat", "Defensa de la Privacitat", "Maquinari Obert", "Defensa de la Privacitat", "Microprogramari de Detecció", "Detecció Mòbil", "Projectes de Privacitat", "Comparació de Maquinari"]
cover: "/img/cover/flock-you-detection-project-counter-surveillance-hardware-guide-2026.webp"
coverAlt: "Una il·lustració que mostra un dispositiu basat en ESP32 en primer pla, escanejant senyals WiFi. Ones de colors representen diferents intensitats de senyal, sobre un fons fosc."
coverCaption: "Solucions de maquinari de codi obert per detectar càmeres de vigilància ALPR"
canonical: "https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/"
---

**Guia Tècnica Completa per Construir i Utilitzar Dispositius de Detecció Flock-You**

## Introducció: Contra-Vigilància de Codi Obert

El **projecte Flock-You** és una **iniciativa de codi obert impulsada per la comunitat** per detectar i cartografiar la infraestructura de vigilància ALPR de Flock Safety. Allotjat a GitHub com **colonelpanichacks/flock-you**, aquest projecte utilitza maquinari basat en ESP32 assequible per identificar les càmeres Flock mitjançant les seves **signatures de xarxa WiFi**.

**Flock-You només detecta càmeres Flock Safety per Wi-Fi.** No detecta simuladors de cel·les telefòniques com Stingray ni rastrejadors personals que es mouen amb tu. Per a això, consulta **[Com flashejar dispositius Rayhunter: guia completa](/articles/how-to-flash-rayhunter-devices-complete-guide/)** per detectar captadors IMSI i **[Eye Spy: detector passiu de vigilància per a M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** per detectar AirTags i seguidors. Els tres funcionen amb la mateixa família de maquinari ESP32 econòmic.

Aquesta guia completa cobreix des de la **metodologia tècnica** darrere de la detecció Flock fins a **instruccions de configuració pas a pas** per a tres plataformes de maquinari, la **instal·lació del microprogramari** i **informació de compra de proveïdors autoritzats**. Tant si ets un defensor de la privacitat, un investigador de seguretat o un ciutadà preocupat, aquesta guia et permetrà construir o comprar el teu propi dispositiu de detecció.


*El maquinari de Flock Safety s'ha desplegat gairebé del tot als Estats Units, amb una presència menor al Canadà. Fora d'Amèrica del Nord, la llista d'OUI i les signatures de probes següents no coincidiran amb cap dispositiu proper. El maquinari continua sent útil per a la recerca, però no trobarà una infraestructura que no hi sigui.*

Per obtenir context sobre per què aquesta tecnologia és important i el panorama de vigilància més ampli, llegeix el nostre article complementari: **[Vigilància amb càmeres Flock Safety: Privadesa i Protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**.

Vols veure on ja s'han cartografiat les càmeres Flock? **[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** és una eina de codi obert que traça més de 40.000 càmeres Flock Safety sospitoses a tot el món utilitzant dades WiFi de WiGLE i empremtes digitals OUI, actualitzada diàriament. Codi font a **[GitHub](https://github.com/simeononsecurity/flock-finder)**.

### D’un cop d’ull: tres plataformes

*Les especificacions completes, els avantatges i els inconvenients de cada plataforma són més avall. Ves a les [instruccions de configuració](#instruccions-de-configuració-pas-a-pas) si ja saps quina vols.*


| Plataforma | Preu | Configuració | Ideal per a |
|---|---|---|---|
| **DIY ESP32** | 5–12 $ | Placa de proves sense soldar, 10–15 min | Muntatges econòmics i aprendre com funciona la detecció |
| **M5 Atom Lite** (preconfigurat) | 49,99 $ | Connecta’l i comença, sense configuració | Ús immediat sense muntatge propi |
| **OUI-SPY** | 85 $ | Flasheja’l una vegada i tria el mode al menú Wi-Fi | Detecció multimode (ALPR, drons i BLE) |

______

## Comprendre la Metodologia de Detecció de Flock-You

### La Base Tècnica

Les càmeres Flock Safety contenen **mòduls WiFi encastats** per a la connectivitat i la gestió remota. Aquests mòduls emeten signatures de xarxa identificables detectables per dispositius que operen en **mode de monitoratge WiFi promiscu**. El projecte Flock-You aprofita aquesta característica mitjançant:

#### 1. Detecció d'OUI WiFi (Identificador Únic Organitzatiu)

Cada interfície de xarxa té una **adreça MAC** que consta de:
- **Primers 3 bytes (24 bits)**: OUI, que identifica el fabricant
- **Últims 3 bytes**: Identificador específic del dispositiu

Els investigadors **@NitekryDPaul** i la comunitat **DeFlockJoplin** van descobrir **31 OUIs específics** consistentment presents en desplegaments de càmeres Flock Safety:

```
OUIs principals d’Espressif (mòduls basats en ESP32):
D4:AD:FC - Espressif Inc. (ESP32-S3 habitual)
AC:67:B2 - Espressif Inc. (ESP32-WROOM)
84:F3:EB - Espressif Inc. (variants de l’ESP32-S3)
B4:E6:2D - Espressif Inc. (ESP32-C3)
CC:DB:A7 - Espressif Inc. (basat en ESP32)
24:0A:C4 - Espressif Inc. (ESP32-SOLO)
30:AE:A4 - Espressif Inc. (ESP32-WROVER)
94:B9:7E - Espressif Inc. (basat en ESP32)
A4:CF:12 - Espressif Inc. (ESP32-S2)
C0:49:EF - Espressif Inc. (ESP32-C6)

OUIs addicionals identificats en desplegaments de Flock:
[... 21 OUIs addicionals de fabricants ...]
```

Quan un dispositiu de detecció escaneja el trànsit WiFi en mode promiscu, **identifica qualsevol dispositiu que emeti trames amb aquests OUIs**.

#### 2. Detecció de Sol·licituds de Sonda Comodí

Les càmeres Flock envien periòdicament **sol·licituds de sonda comodí** per cercar xarxes disponibles. Aquestes tenen característiques distintives:

- **Trama de Gestió 802.11**: Type=0, Subtype=4
- **Element d'Informació SSID**: Length=0 (buit/comodí)
- **Estructura de la trama**: Patró previsible en el temporitzat de les sondes
- **IEs específics del proveïdor**: Indicadors addicionals a la càrrega útil de la trama

El microprogramari de detecció analitza aquests **patrons de sol·licituds de sonda** per augmentar la confiança en la identificació de càmeres Flock més enllà de la simple concordança d'OUI.

#### 3. Monitoratge WiFi en Mode Promiscu

L'operació WiFi estàndard només rep trames adreçades al teu dispositiu. El **mode promiscu** captura totes les trames WiFi a l'abast:

- **Estructura de trama 802.11**: Anàlisi dels camps addr1, addr2, addr3
- **Trames de gestió**: Sol·licituds de sonda, trames de balisa, sol·licituds d'associació
- **Trames de dades**: Revelen patrons de comportament de la xarxa
- **Trames de control**: ACKs, RTSs, CTSs proporcionen informació de temporitzat

Els microcontroladors ESP32 admeten el mode promiscu a través de la **API esp_wifi**, habilitant maquinari de detecció de baix cost.

#### 4. Anàlisi de la Intensitat del Senyal

Els dispositius de detecció mesuren el **RSSI (Indicador de la Intensitat del Senyal Rebut)** per:
- **Estimar la distància** a les càmeres detectades
- **Triangular ubicacions** amb múltiples mesures
- **Filtrar falsos positius** basant-se en les característiques esperades del senyal
- **Crear mapes de calor** de la densitat de càmeres

### Precisió de Detecció i Falsos Positius

La metodologia Flock-You aconsegueix una alta precisió:

- **Taxa de Veritables Positius**: ~95% per a càmeres Flock confirmades a l'abast
- **Taxa de Falsos Positius**: ~5-10% depenent de l'entorn
- **Abast de Detecció**: 50-300 peus depenent dels obstacles i l'antena
- **Puntuació de Confiança**: L'anàlisi multifactorial redueix les falses alarmes

**Fonts Comunes de Falsos Positius**:
- **Plaques de desenvolupament ESP32** usades en altres dispositius IoT
- **Productes comercials basats en ESP32** (llar intel·ligent, sensors)
- **Altres càmeres de vigilància** que utilitzen components similars
- **Equips de prova WiFi** operats per tècnics

**Estratègies de Mitigació**:
- **Detecció de múltiples signatures**: Combinant OUI + patró de sonda + verificació física
- **Correlació d'ubicació**: Creuant amb ubicacions de càmeres conegudes
- **Confirmació visual**: Inspecció física després de la detecció electrònica
- **Base de dades comunitària**: Validació per multituds de les deteccions

______

{{< figure src="flockyou-oui-detection-methodology-overview.webp" alt="Diagrama de detecció Flock-You: l’ESP32 en mode Wi-Fi promiscu compara MAC amb OUI coneguts, comprova probes comodí i puntua RSSI" >}}

{{< stscollective-ad "flockyou" >}}

## Comparació de Plataformes de Maquinari

Tres plataformes principals estan disponibles per a la detecció Flock-You, cadascuna amb avantatges distintius:
*Les tres plataformes utilitzen el mateix mètode de detecció subjacent: escaneig passiu en mode promiscu WiFi per trobar OUI coneguts de càmeres Flock i signatures de sol·licituds de sonda comodí. Cap no detecta Bluetooth. El microprogramari Flock-You va deixar de donar suport a la detecció BLE la primavera de 2026, després que deixés de funcionar de manera fiable; per tant, totes les plataformes d'aquí només utilitzen WiFi.*

### Taula de Visió General de Plataformes

| Característica | DIY ESP32 | M5 Atom Lite (Pre-Flashejat) | OUI-SPY |
|---------|-----------|---------------------------|---------|
| **Fabricant** | DIY / Múltiples proveïdors | STS Collective | Colonel Panic Tech |
| **Preu** | $5-12 | $39.99 | $85 |
| **Processador** | ESP32-WROOM | ESP32-PICO | ESP32-S3 |
| **Llest per Usar** | No (construcció DIY) | Sí (pre-flashejat) | Sí (multi-mode) |
| **Pantalla** | Opcional | LED RGB (matriu 5×5) | Cap |
| **Bateria** | Opcional | Externa recomanada | No inclosa |
| **GPS** | Opcional | No | No |
| **Alertes** | Brunzidor + LED | LED RGB (blau=detecta) | Brunzidor integrat |
| **Registre de Dades** | Opcional | No | No |
| **Carcassa** | Impressió 3D o cap | Mòdul de plàstic compacte | Cap (PCB nu) |
| **Microprogramari** | Flash manual | FlockYou pre-carregat | Multi-mode (4 microprogramaris) |
| **Millor Per** | Entusiastes DIY, aprenentatge | Econòmic llest per usar | Detecció multipropòsit |
| **Dificultat de Configuració** | Moderada-Avançada | Connectors i llest | Connectors i llest |
| **Pes** | 20-50g (varia) | 18g (nu) | ~40g |
| **Dimensions** | Varia | 24×24×14mm | Placa PCB |

### Anàlisi Detallada de Plataformes

#### 1. Construcció DIY ESP32 ($5-12)

**Visió General**: Opció més assequible amb plaques de desenvolupament ESP32 estàndard i microprogramari de codi obert.

**Especificacions de Maquinari**:
- **Microcontrolador**: ESP32-WROOM-32 o similar (doble nucli, 240MHz)
- **WiFi**: 802.11 b/g/n, capaç de mode promiscu
- **Memòria**: 520KB SRAM, 4MB+ Flash
- **Pantalla**: Opcional (LED incorporat suficient)
- **Alimentació**: Alimentat per USB o bateria externa
- **Brunzidor**: Mòdul de brunzidor passiu opcional (KY-006)
- **Indicadors**: LED incorporat + brunzidor opcional
- **Expansibilitat**: Compatible amb protoboard, modificacions fàcils

**Microprogramari**: Fork de codi obert a **simeononsecurity/flock-you-esp32**:
- Modificat per a maquinari ESP32 estàndard (GPIO 25, 2, 17)
- Melodia d'inici de Super Mario Bros. (confirma que el brunzidor funciona)
- Dos pitidos ascendents ràpids en nova detecció
- Pitidos de pols cada 10 segons mentre el seguiment és actiu
- Suport de tauler de control Flask per al recorreguts de reconeixement de xarxes Wi-Fi amb GPS
- Exportació als formats JSON, CSV, KML

**Opcions de Construcció**:
- **Només LED ($5)**: ESP32 nu + cable USB, només retroalimentació visual
- **Protoboard ($9-11)**: Afegir brunzidor passiu + protoboard + cables, alertes d'àudio
- **Tancat ($10-12)**: Afegir caixa impresa en 3D amb tapa d'encaix

**Avantatges**:
- ✅ Opció més barata (85-95% d'estalvi de cost vs OUI-SPY)
- ✅ Completament de codi obert i modificable
- ✅ Utilitza plaques ESP32 àmpliament disponibles
- ✅ Educatiu, ensenya sistemes encastats
- ✅ Documentació i guies extenses
- ✅ Fitxers de caixa imprimibles en 3D disponibles
- ✅ **Mateixa precisió de detecció que els dispositius premium**

**Desavantatges**:
- ❌ Requereix muntatge DIY (protoboard sense soldadura o caixa 3D)
- ❌ Cal fer flash del microprogramari manualment
- ❌ Sense bateria integrada (alimentació USB o pack extern)
- ❌ Només retroalimentació d'àudio bàsica (sense pantalla)
- ❌ Porta temps obtenir els components

**Millor Per**: Makers, estudiants, defensors de la privacitat amb pressupost limitat, qualsevol que vulgui aprendre com funciona la detecció, els qui gaudeixen dels projectes DIY.

**Comprar Components**:
- **Amazon**: Cerca "ESP32 DevKit" o "ESP32 Breadboard Kit"
- **AliExpress/eBay**: Descomptes per volum disponibles
- **Adafruit**: Peces de qualitat seleccionades amb tutorials

**Recursos de Configuració**:
- **Repositori GitHub**: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)
- **Guia de Construcció**: Muntatge sense soldadura en 10-15 minuts
- **Fitxers de Caixa**: Disseny paramètric OpenSCAD + fitxers STL

---

{{< figure src="flockyou-diy-esp32-solderless-breadboard-build.webp" alt="Muntatge Flock-You amb ESP32 en placa sense soldar, DevKit, brunzidor passiu i fils als GPIO 25, 2 i 17" >}}

#### 2. M5 Atom Lite Pre-Flashejat per STS Collective ($39.99)

**Visió General**: Dispositiu de detecció compacte pre-flashejat, llest per usar directament de la caixa.

**Especificacions de Maquinari**:
- **Microcontrolador**: ESP32-PICO-D4 (doble nucli, 240MHz)
- **WiFi**: 802.11 b/g/n, capaç de mode promiscu
- **Memòria**: 520KB SRAM, 4MB Flash
- **Pantalla**: Matriu LED RGB 5×5 (WS2812C NeoPixel)
- **Alimentació**: 5V via USB-C o connector Grove
- **Bateria**: No inclosa (es recomana bateria USB externa)
- **Indicador**: LED RGB programable (blau=detecció)
- **Botons**: 1 botó programable
- **E/S**: Connector Grove per a expansió
- **Mida**: Ultrecompacte 24×24×14mm
- **Carcassa**: Mòdul de plàstic resistent

**Microprogramari**: Port personalitzat de FlockYou per STS Collective (propietari):
- Pre-carregat i llest per usar
- Alerta LED blau en detecció de càmera Flock
- Basat en la investigació FlockYou de colonelpanichacks
- No cal configuració ni flash
- Funcionament senzill de connectors i llest
- Suport opcional de tauler de control

**Avantatges**:
- ✅ Pre-flashejat, no cal configuració tècnica
- ✅ Solució econòmica llesta per usar
- ✅ Extremadament compacte i portàtil
- ✅ Plataforma de maquinari provada
- ✅ Senzill LED blau = detecció
- ✅ Alimentat per USB-C (cotxe, bateria externa, portàtil)
- ✅ Suport de proveïdor de qualitat
- ✅ Preu normal $99.99, en oferta $39.99

**Desavantatges**:
- ❌ Sense bateria integrada (necessita alimentació USB)
- ❌ Pantalla limitada (només LED RGB, sense pantalla)
- ❌ *El microprogramari és propietari, no és de codi obert de moment*
- ❌ Sense registre de dades sense connexió a l'ordinador
- ❌ Un botó limita la funcionalitat

**Millor Per**: Usuaris que volen detecció instantània sense treball DIY, prioritat de portabilitat, els qui es senten còmodes amb retroalimentació LED senzilla, compradors amb pressupost limitat que volen una solució ja feta.

**Comprar**: [stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)

> 💰 **Descompte Exclusiu**: Estalvia fins a un 20% en productes STS Collective — utilitza el codi **SIMEONONSECURITY** a la caixa o [fes clic aquí per comprar amb el descompte aplicat](https://stscollective.com/discount/SIMEONONSECURITY).

---

{{< figure src="flockyou-m5-atom-lite-pocket-size-comparison.webp" alt="M5 Atom Lite preconfigurat entre dos dits, que mostra la mida petita i el LED RGB blau de detecció" >}}

#### 3. OUI-SPY per Colonel Panic Tech ($85)

**Visió General**: Placa de detecció de vigilància multi-mode amb quatre modes de microprogramari diferents seleccionables via menú WiFi.

**Especificacions de Maquinari**:
- **Microcontrolador**: ESP32-S3 doble nucli Xtensa LX7, 8MB flash
- **WiFi**: 802.11 b/g/n, capaç de mode promiscu
- **Memòria**: 8MB Flash
- **Pantalla**: Cap (PCB nu amb indicadors LED)
- **Bateria**: No inclosa
- **Càrrega**: Alimentació i programació USB-C
- **Emmagatzematge**: Cap (modes només de detecció)
- **Indicadors**: Brunzidor PWM integrat amb melodies específiques per mode
- **Botons**: Botó d'arrencada per canviar de mode
- **Antena**: **Commutable**, ceràmica 2.4GHz incorporada O externa via connector MMCX
- **Carcassa**: Cap (PCB nu amb art en PCB)
- **Característica Única**: Aleatorització de MAC a cada arrencada

**Microprogramari**: OUI-SPY Unified Blue amb **4 modes seleccionables**:
1. **Mode Detector**: Escàner BLE de múltiples objectius amb filtratge OUI + portal de configuració web
2. **Mode Foxhunter**: Seguidor de proximitat RSSI d'objectiu únic per a la cerca de direcció de ràdio
3. **Mode Flock-You**: Detecció de càmeres Flock Safety i Raven amb recorreguts de reconeixement de xarxes Wi-Fi amb GPS, exportació JSON/CSV/KML
4. **Mode Sky Spy**: Detector RemoteID de drons (OpenDroneID / ASTM F3411) amb seguiment de múltiples drons

**Selecció de Mode**:
- Menú d'arrencada WiFi a 192.168.4.1
- Mantén el botó BOOT 2 segons per tornar al selector
- Memòria de l'últim mode entre cicles d'alimentació
- Melodies d'arrencada per mode (alertes de chiptune retro)
- Funcionament de només detecció (res no es transmet)

**Avantatges**:
- ✅ Quatre modes de microprogramari en un dispositiu
- ✅ Antena commutable (incorporada o MMCX externa)
- ✅ Brunzidor integrat amb melodies d'arrencada personalitzades
- ✅ Disseny PCB de qualitat professional
- ✅ Multipropòsit: ALPR, drons, BLE, cerca de direcció RF
- ✅ Del creador original del projecte Flock-You
- ✅ Desenvolupament actiu i actualitzacions

**Desavantatges**:
- ❌ Preu més alt per a la detecció Flock de propòsit únic
- ❌ Sense carcassa inclosa (PCB nu)
- ❌ Sense bateria incorporada
- ❌ Sense pantalla (retroalimentació únicament d'àudio per a la majoria de modes)
- ❌ *Complexitat innecessària per a la detecció bàsica*
- ❌ Cal GPS extern per a les funcions de recorreguts de reconeixement de xarxes Wi-Fi

**Millor Per**: Detecció de vigilància multipropòsit, usuaris que volen detecció de drons + ALPR + BLE en un sol dispositiu, aplicacions de cerca de direcció RF, els qui valoren les antenes commutables i les funcions avançades.

**Comprar**: [colonelpanic.tech](https://colonelpanic.tech/products/oui-spy)

______

{{< figure src="flockyou-oui-spy-multimode-board-pcb.webp" alt="Placa nua OUI-SPY ESP32-S3 amb antena, brunzidor i botó d’arrencada; una pantalla mostra el menú Wi-Fi de quatre modes" >}}

## Instruccions de Configuració Pas a Pas

### Guia de Configuració 1: Construcció DIY ESP32

**Per a instruccions detallades completes**, visita el repositori GitHub: [github.com/simeononsecurity/flock-you-esp32](https://github.com/simeononsecurity/flock-you-esp32)

#### Visió General d'Inici Ràpid

1. **Maquinari Necessari**:
   - Placa ESP32 DevKit ($5-6)
   - Cable USB (Micro-USB o USB-C depenent de la placa)
   - Opcional: Mòdul de brunzidor passiu (KY-006), protoboard, cables
   - Opcional: Caixa impresa en 3D

2. **Configuració del Programari**:
   ```bash
   # Instal·la PlatformIO
   pip install platformio

   # Clona el repositori
   git clone https://github.com/simeononsecurity/flock-you-esp32.git
   cd flock-you-esp32

   # Flasheja el microprogramari
   pio run -t upload
   pio device monitor
   ```

3. **Muntatge del Maquinari** (si s'usa brunzidor):
   - Brunzidor positiu → GPIO 25
   - Brunzidor negatiu → GND
   - Indicador LED → GPIO 2 (incorporat)
   - Alimentació via USB

4. **Confirmació d'Inici**:
   - La melodia 1-2 de Super Mario Bros. sona (si el brunzidor està connectat)
   - El LED parpelleja per indicar l'escaneig
   - El monitor sèrie mostra la inicialització "Flock-You ESP32"

5. **Alertes de Detecció**:
   - **Nova detecció**: Dos pitidos ascendents ràpids (2000→2800 Hz)
   - **Pols**: Dos pitidos cada 10 segons mentre es fa seguiment
   - **LED**: Parpelleja en cada detecció

6. **Recorreguts de reconeixement de xarxes Wi-Fi amb GPS** (opcional):
   - Connecta a l'ordinador via USB
   - Executa el tauler de control Flask: `cd api && python flockyou.py`
   - Obre http://localhost:5000
   - Connecta dispositiu GPS o utilitza la ubicació del navegador
   - Exporta deteccions a JSON/CSV/KML

**Guia de construcció completa, fitxers de caixa i resolució de problemes**: Consulta el README de GitHub

---

### Guia de Configuració 2: M5 Atom Lite Pre-Flashejat (STS Collective)

#### Inici Ràpid

1. **Desembalatge**:
   - Dispositiu M5 Atom Lite (pre-flashejat amb microprogramari FlockYou)
   - Comprova la llista del producte per a la inclusió del cable USB-C

2. **Engegar**:
   - Connecta a la font d'alimentació USB-C (bateria externa, USB de cotxe, adaptador de paret, ordinador)
   - El dispositiu arrenca automàticament
   - La matriu LED RGB s'inicialitza

3. **Funcionament**:
   - **Inactiu/Escanejant**: El LED mostra el patró d'escaneig
   - **Detecció**: El LED es torna **BLAU** quan es detecta una càmera Flock
   - **Botó**: Prem per tornar a escanejar manualment o reiniciar

4. **Ús Portàtil**:
   - Connecta a la bateria USB externa (5000mAh = ~20 hores)
   - Col·loca al portavasos, bossa o butxaca
   - LED visible a través de la carcassa translúcida

5. **Connexió al Tauler de Control** (opcional):
   - Connecta el dispositiu a l'ordinador via USB-C
   - Instal·la el tauler de control FlockYou seguint les instruccions de STS Collective
   - Visualitza les deteccions en directe a la interfície del navegador

**Avís**: *Aquest és un microprogramari propietari. Tornar a flashejar amb versions de codi obert eliminarà el microprogramari STS de forma permanent.*

---

### Guia de Configuració 3: Placa Multi-Mode OUI-SPY

#### Configuració Inicial

1. **Contingut del Paquet**:
   - Placa PCB nua OUI-SPY
   - Cable USB-C
   - Guia d'inici ràpid

2. **Primer Engegament**:
   - Connecta l'alimentació USB-C (ordinador, adaptador de paret o bateria externa)
   - El dispositiu emet la xarxa WiFi: `OUISPY-[ID]`
   - El brunzidor reprodueix la melodia d'arrencada específica del mode

3. **Selecció de Mode WiFi**:
   - Connecta el telèfon/ordinador a la xarxa WiFi d'OUI-SPY
   - Obre el navegador a: `http://192.168.4.1`
   - La interfície web mostra 4 modes de microprogramari:
     1. **Detector** - Escàner BLE de múltiples objectius
     2. **Foxhunter** - Cerca de direcció RF
     3. **Flock-You** - Detecció de càmeres ALPR
     4. **Sky Spy** - Detector RemoteID de drons
   - Selecciona el mode desitjat i fes clic a "Activate"

4. **Funcionament del Mode Flock-You**:
   - El dispositiu reinicia en mode Flock-You
   - El brunzidor reprodueix la melodia d'inici de Flock-You
   - Comença a escanejar els 31 OUIs coneguts
   - **Alerta de detecció**: El brunzidor fa un pipit amb un patró únic
   - L'últim mode es recorda entre cicles d'alimentació

5. **Canviar de Mode**:
   - Mantén el **botó BOOT** durant 2 segons
   - El dispositiu torna al selector de mode WiFi
   - Torna a connectar-te al WiFi i tria un nou mode

#### Avançat: Antena Externa

6. **Commutació d'Antena** (per a major abast):
   - Per defecte: Utilitza l'antena ceràmica incorporada
   - Connecta l'antena MMCX al connector MMCX
   - El microprogramari commuta automàticament a l'antena externa

#### Muntatge

7. **Instal·lació en Vehicle/Fixa**:
   - *No s'inclou carcassa, cal protegir el PCB nu abans de muntar-lo*
   - Opcions:
     - Impressió 3D de carcassa personalitzada
     - Muntatge amb velcro al tauler de control
     - Utilitza cinta de doble cara
     - Caixa de projecte DIY
   - Mantén el port USB-C accessible per a l'alimentació

#### Exportació de Dades (Mode Flock-You)

8. **Recorreguts de reconeixement de xarxes Wi-Fi amb GPS**:
   - Connecta un mòdul GPS extern (no inclòs)
   - El dispositiu registra les deteccions amb coordenades
   - Descarrega fitxers de dades via la interfície web
   - Formats d'exportació: JSON, CSV, KML

**Nota**: Consulta colonelpanic.tech per a actualitzacions de microprogramari i documentació específica per a OUI-SPY Unified Blue.

---

______

## Guia de Compra i Informació de Proveïdors

### Proveïdors Autoritzats

#### Colonel Panic Tech (colonelpanic.tech)

**Productes Oferits**:
- **OUI-SPY** ($85): Dispositiu de detecció Flock llest per usar
- **Kits DIY** ($55): Components + PCB + guia de muntatge
- **Mòdul GPS Addicional** ($18): Mòdul GPS-6M compatible
- **Accessoris**: Antenes, caixes, actualitzacions de bateria

**Per Què Comprar a Colonel Panic**:
- ✅ Directament del desenvolupador del maquinari OUI-SPY
- ✅ Últim microprogramari pre-instal·lat
- ✅ Suport tècnic inclòs
- ✅ Filosofia de codi obert (esquemes disponibles)
- ✅ Fòrum comunitari actiu

**Enviament**:
- EE.UU. Domèstic: 3-5 dies laborables
- Internacional: 7-14 dies laborables
- Enviament gratuït en comandes >$100

**Garantia**: Garantia de maquinari de 90 dies, actualitzacions de microprogramari de per vida

**Web**: [https://colonelpanic.tech](https://colonelpanic.tech)

---

#### STS Collective (stscollective.com)

**Productes Oferits**:
- **M5 Atom Lite Pre-Flashejat** ($39.99): Dispositiu de detecció Flock llest per usar
- **Accessoris**: Compatible amb diverses plataformes ESP32

**Per Què Comprar a STS Collective**:
- ✅ Dispositius pre-flashejats llestos per usar
- ✅ Assegurament de qualitat i proves
- ✅ Preus assequibles
- ✅ Suport al client

**Enviament**:
- EE.UU. Domèstic: 2-4 dies laborables (Correu Prioritari)
- Internacional: 7-21 dies laborables
- Opcions ràpides disponibles

**Garantia**: Garantia estàndard en maquinari

**Web**: [https://stscollective.com](https://stscollective.com)

> 💰 **Descompte per a Lectors**: Utilitza el codi **SIMEONONSECURITY** per a un 20% de descompte en productes STS Collective — [stscollective.com/discount/SIMEONONSECURITY](https://stscollective.com/discount/SIMEONONSECURITY).

---

#### Altres Fonts per al M5 Atom Lite

**Botiga Oficial M5Stack**:
- Web: [shop.m5stack.com](https://shop.m5stack.com)
- Preu: $9.95 per al Atom Lite nu
- Accessoris: Mòduls de bateria, sensors Grove, caixes
- Enviament: Internacional, 7-14 dies

**Amazon**: Cerca "M5Stack Atom Lite"
- Preu: ~$12-15 (varia per venedor)
- Enviament Prime disponible
- Opcions de paquets amb accessoris

**Adafruit**: [adafruit.com](https://adafruit.com)
- Minorista d'electrònica seleccionada
- Excel·lents recursos d'aprenentatge
- Enviament ràpid des dels EE.UU.

**Nota**: *En comprar un M5 Atom Lite nu, el microprogramari s'ha d'instal·lar per separat seguint la guia DIY anterior. La versió pre-flashejada de STS Collective és un producte diferent.*

### Resum de Comparació de Preus

| Dispositiu | Preu Base | Complements Opcionals | Inversió Total | Temps de Configuració |
|--------|------------|------------------|------------------|------------|
| **DIY ESP32** | $5-12 | Caixa 3D, bateria | $5-20 | 15-30 min |
| **M5 Atom Lite** | $39.99 | Bateria externa $10 | $40-50 | Connectors i llest |
| **OUI-SPY** | $85 | Antena externa $20, carcassa | $85-115 | Connectors i llest |

______

## Ús del Teu Dispositiu de Detecció: Escenaris Pràctics

### Escenari 1: Cartografia del Trajecte Diari

**Objectiu**: Documentar les ubicacions de les càmeres Flock al llarg dels teus trajectes habituals.

**Configuració**:
- Utilitza el dispositiu amb capacitat GPS (DIY ESP32 amb mòdul GPS o OUI-SPY amb GPS)
- Activa el registre automàtic
- Munta al vehicle o porta a la butxaca
- Estableix la sensibilitat a MITJANA per reduir els falsos positius

**Procediment**:
1. Inicia el dispositiu de detecció abans de sortir
2. Fes el teu recorregut habitual
3. El dispositiu alerta quan detecta càmeres Flock
4. Les coordenades GPS es registren automàticament
5. Torna a casa i exporta les dades
6. Importa GPX/CSV al programari de cartografia
7. Crea un mapa personal de la ubicació de les càmeres

**Beneficis**:
- Consciència de la cobertura de vigilància als teus trajectes
- Identifica rutes alternatives sense càmeres
- Contribueix a projectes de cartografia comunitaris
- Segueix els canvis de desplegament al llarg del temps

### Escenari 2: Avaluació de la Vigilància del Barri

**Objectiu**: Determinar la cobertura de les càmeres Flock a la teva àrea residencial.

**Configuració**:
- Utilitza el dispositiu portàtil (M5 Atom Lite, DIY ESP32 o OUI-SPY)
- Enquesta caminant o en bicicleta
- Monitoratge estacionari en interseccions clau

**Procediment**:
1. Camina/pedala pels carrers del barri
2. Para't a cada intersecció durant 30-60 segons
3. Anota les deteccions al mapa
4. Utilitza la intensitat del senyal per estimar distància/direcció
5. Confirma visualment les ubicacions de les càmeres quan sigui possible
6. Documenta les troballes amb fotos (des d'àrees públiques)

**Resultat**:
- Mapa complet de la infraestructura de vigilància local
- Evidència per a l'organització comunitària
- Dades per a sol·licituds de registres públics
- Consciència per a les decisions personals de privacitat

*La velocitat a peu importa més del que la majoria espera. El microprogramari salta de canal WiFi aproximadament cada 250 ms per seguir el ritme amb què la càmera també canvia de canal. Si camines o vas amb bicicleta de pressa, pots passar la finestra de detecció d’una càmera abans que coincideixi un canvi de canal. Si les deteccions durant un recorregut a peu són irregulars, redueix la velocitat a les cruïlles abans de provar una antena de més guany. Una antena estàndard amb una espera de 30 a 60 segons a cada parada detecta moltes més càmeres que una antena d’alt guany mentre passes de pressa.*


### Escenari 3: Avaluació de Privacitat en Viatges

**Objectiu**: Comprendre l'exposició a la vigilància en viatjar.

**Configuració**:
- Porta el dispositiu compacte (M5 Atom Lite a la butxaca o DIY ESP32)
- Activa el registre continu
- Revisa les dades després del viatge

**Casos d'Ús**:
- Cites mèdiques: Avalua la vigilància prop de les clíniques
- Consultes legals: Comprova la cobertura de l'àrea d'oficines d'advocats
- Serveis religiosos: Entén el monitoratge prop dels llocs de culte
- Activitats polítiques: Avalua la vigilància en esdeveniments/manifestacions
- Situacions domèstiques: Identifica si la residència és monitorada

### Escenari 4: Defensa Comunitària

**Objectiu**: Proporcionar dades per als debats de polítiques i la consciència pública.

**Aplicacions**:
- Presenta les troballes en reunions del consell municipal
- Inclou en sol·licituds de registres públics
- Comparteix amb organitzacions de defensa de la privacitat
- Contribueix a projectes de recerca
- Informa les associacions de veïns

**Presentació de Dades**:
- Crea mapes de calor que mostren la densitat de càmeres
- Genera informes sobre les disparitats de cobertura
- Produeix cronologies de l'expansió del desplegament
- Correlaciona amb estadístiques delictives (o la manca d'elles)

______

{{< figure src="flockyou-detection-device-driving-scenario.webp" alt="Un conductor mira el detector FlockYou al portagots, que avisa d’una càmera Flock propera" >}}

## Anàlisi Tècnica Detallada: Comprendre el Codi

### Algorisme de Detecció Bàsic (Simplificat)

Per als interessats en la implementació tècnica, aquí hi ha una visió simplificada de la lògica de detecció:

```cpp
// Nucli de detecció de Flock-You (conceptual, no és el codi complet)

// Base de dades OUI (31 OUI associats amb Flock)
const uint8_t FLOCK_OUI_LIST[][3] = {
    {0xD4, 0xAD, 0xFC}, // Espressif ESP32-S3
    {0xAC, 0x67, 0xB2}, // Espressif ESP32-WROOM
    {0x84, 0xF3, 0xEB}, // Variant Espressif ESP32-S3
    // ... 28 OUI més ...
};

// Funció de retorn del mode promiscu
void wifi_sniffer_callback(void* buf, wifi_promiscuous_pkt_type_t type) {
    wifi_promiscuous_pkt_t *pkt = (wifi_promiscuous_pkt_t*)buf;

    // Extreu l’adreça MAC del paquet
    uint8_t *mac = pkt->payload + 10; // Posició del camp addr2

    // Comprova la base de dades OUI
    for (int i = 0; i < NUM_OUIS; i++) {
        if (memcmp(mac, FLOCK_OUI_LIST[i], 3) == 0) {
            // S’ha trobat una coincidència OUI
            int rssi = pkt->rx_ctrl.rssi;

            // Comprova el llindar de potència del senyal
            if (rssi > RSSI_THRESHOLD) {
                // Analitza el paquet per trobar signatures addicionals
                if (is_wildcard_probe_request(pkt)) {
                    // Detecció d’alta confiança
                    trigger_alert(mac, rssi, HIGH_CONFIDENCE);
                } else {
                    // Només coincidència OUI
                    trigger_alert(mac, rssi, MEDIUM_CONFIDENCE);
                }
            }
        }
    }
}

// Detecció de sol·licitud de difusió
bool is_wildcard_probe_request(wifi_promiscuous_pkt_t *pkt) {
    // Trama de gestió, subtipus de sol·licitud de prova
    if ((pkt->payload[0] & 0x0F) != 0x04) return false;

    // Comprova si l’IE SSID és buit (difusió)
    // La posició depèn de l’estructura de la trama
    uint8_t *ie = &pkt->payload[24]; // Inici dels IE
    if (ie[0] == 0x00 && ie[1] == 0x00) {
        return true; // Sol·licitud de difusió
    }
    return false;
}
```

### Conceptes Tècnics Clau Explicats

**Mode Promiscu**: En lloc de rebre només les trames adreçades al teu dispositiu, l'ESP32 captura totes les trames WiFi a l'abast. **Això és essencial per detectar dispositius propers que no es comuniquen amb el teu detector.**

**Estructura d'Adreça MAC**: Cada trama WiFi conté múltiples adreces MAC:
- `addr1`: Adreça del receptor
- `addr2`: Adreça del transmissor (conté l'OUI)
- `addr3`: Adreça de la destinació/origen final

**RSSI (Indicador de la Intensitat del Senyal Rebut)**: Intensitat del senyal en dBm (decibels negatius relatius a 1 mil·liwatt). Valors típics:
- -30 dBm: Extremadament fort (molt prop)
- -50 dBm: Senyal fort
- -70 dBm: Feble però usable
- -90 dBm: Molt feble (límit de l'abast)

**Sol·licituds de Sonda**: Els dispositius WiFi envien sol·licituds de sonda per descobrir xarxes disponibles. *Les sondes comodí (SSID buit) cerquen qualsevol xarxa, cosa habitual en dispositius IoT com les càmeres Flock, fent-les detectables de forma fiable.*

______

## Resolució de Problemes Comuns
{{< figure src="flockyou-troubleshooting-firmware-flash-flowchart.webp" alt="Fluxograma per resoldre problemes de càrrega del firmware i detecció, de l’alimentació als falsos positius d’OUI" >}}

### Problema: Sense Deteccions Malgrat Tenir una Càmera Propera Coneguda

**Possibles Causes**:
1. **Càmera fora de línia/apagada**: Les càmeres Flock estan temporalment inactives de vegades
2. **Senyal bloquejat**: Els materials de construcció absorbeixen el WiFi (metall, formigó)
3. **Fora de l'abast**: L'abast efectiu és ~100-300 peus depenent dels obstacles
4. **Moure’s massa de pressa**: els canvis de canal afavoreixen caminar a poc a poc o aturar-se del tot, no caminar de pressa ni circular amb vehicle
5. **Problema de microprogramari**: El microprogramari obsolet no detecta variants d'OUI més noves

**Solucions**:
- Confirma que la càmera és visible i sembla operativa (panells solars, llums)
- Apropa't a la ubicació sospitosa de la càmera
- Prova diferents orientacions de l'antena
- Actualitza al darrer microprogramari Flock-You
- **Comprova que el dispositiu estigui escanejant activament** (verifica l'activitat del LED/pantalla)

### Problema: Massa Falsos Positius

**Possibles Causes**:
1. **Alta densitat de dispositius ESP32**: La llar intel·ligent, els dispositius IoT són habituals
2. **Sensibilitat massa alta**: Detecta dispositius llunyans/irrellevants
3. **Altres càmeres de vigilància**: Moltes utilitzen mòduls ESP32

**Solucions**:
- Redueix la configuració de sensibilitat
- Activa la detecció de sondes comodí (major confiança)
- Verifica físicament les deteccions abans de registrar-les
- Utilitza la intensitat del senyal per filtrar (alerta només en senyals forts)
- Actualitza la base de dades OUI per centrar-se en els OUIs Flock confirmats

### Problema: La Bateria S'Esgota Ràpidament

**Possibles Causes**:
1. **Escaneig continu**: Sense gestió de son/alimentació
2. **Pantalla sempre encesa**: La pantalla consumeix energia significativa
3. **GPS actiu**: Els mòduls GPS consumeixen molta energia
4. **Bateria antiga**: Les bateries Li-Po es degraden amb el temps

**Solucions**:
- Activa el mode d'escaneig passiu (intermitent vs. continu)
- Estableix el temps d'espera de la pantalla
- Desactiva el GPS quan no cal cartografiar
- Substitueix la bateria (OUI-SPY/mesh-detect v2 tenen bateries substituïbles)
- Utilitza una bateria externa per a sessions llargues

### Problema: El GPS No Adquireix Senyal

**Possibles Causes**:
1. **Ús en interiors**: El GPS requereix visibilitat del cel
2. **Antena no connectada**: El mesh-detect v2 necessita l'antena externa connectada
3. **Arrencada en fred**: El primer bloqueig GPS tarda 5-15 minuts
4. **Interferències**: L'electrònica propera interfereix amb el senyal

**Solucions**:
- Mou-te a una posició amb visió clara del cel
- Assegura't que l'antena estigui correctament connectada (connector SMA)
- Espera el bloqueig inicial (els posteriors són més ràpids)
- Allunya't de les fonts d'interferència RF
- Comprova que el GPS estigui activat a la configuració

### Problema: Les Dades No Es Registren a la Targeta SD

**Possibles Causes**:
1. **Targeta SD no formatada**: Ha d'estar en format FAT32
2. **Targeta SD plena**: Sense espai restant
3. **Targeta no detectada**: No introduïda completament
4. **Corrupció del sistema de fitxers**: Targeta danyada

**Solucions**:
- **Formata la targeta SD com a FAT32** (32GB màxim per compatibilitat)
- Elimina registres antics o utilitza una targeta més gran
- Reintrodueix la targeta completament (ha de fer clic)
- Torna a formatar la targeta o substitueix-la si està danyada
- Comprova que el dispositiu reconeix la targeta (el menú mostrarà l'estat de la SD)

______

## Consideracions Legals i Ètiques

### Estatus Legal dels Dispositius de Detecció

**Legalitat de l'Escaneig WiFi**:
- ✅ **Legal als EE.UU.**: El monitoratge WiFi passiu (només recepció) és legal
- ✅ **Sense interceptació**: Els dispositius només monitoren trames emeses públicament
- ✅ **Sense desxifrat**: No intenta desxifrar dades ni connectar-se a xarxes
- ✅ **Similar als escàners de ràdio**: Estatus legal comparable als escàners de policia

**Distincions Importants**:
- ❌ **Il·legal**: Interferència activa/bloqueig del funcionament de la càmera
- ❌ **Il·legal**: Intent de piratejar o accedir als sistemes de càmeres
- ❌ **Il·legal**: Destruir o manipular càmeres físiques
- ⚠️ **Zona grisa**: *Algunes jurisdiccions tenen lleis de privacitat més estrictes. Verifica les normatives locals abans d'usar-lo.*

**Recomanació**: **Els dispositius de detecció són per a la consciència únicament. No interfereixis amb el funcionament de les càmeres.**

### Directrius d'Ús Ètic

**Ús Responsable**:
- ✅ Utilitza per a la consciència personal de la vigilància
- ✅ Documenta per a la defensa i els debats de polítiques
- ✅ Comparteix dades agregades amb organitzacions de privacitat
- ✅ Contribueix als projectes de cartografia comunitaris
- ✅ Educa els altres sobre la infraestructura de vigilància

**Evita**:
- ❌ Usar les dades per facilitar activitats il·legals
- ❌ Assetjar els propietaris que han instal·lat càmeres
- ❌ Envair propietats per confirmar les ubicacions de les càmeres
- ❌ Accions de vigilantisme contra la infraestructura de vigilància

### Consideracions de Privacitat

**La Teva Privacitat de Dades**:
- **Els dispositius de detecció registren LA TEVA ubicació** (via GPS)
- Emmagatzema aquestes dades de forma segura
- **Tingues en compte el risc de citació judicial** si estàs involucrat en procediments legals
- Considera el xifratge per a fitxers de registre sensibles
- Entén les polítiques de privacitat dels proveïdors per als dispositius connectats al núvol

**Respectar els Altres**:
- Sigues conscient quan utilitis dispositius de detecció en espais privats
- No l'utilitis per rastrejar altres persones
- Considera les implicacions ètiques de la compartició de dades

______

## Comunitat i Desenvolupament de Codi Obert

### Contribuir al Projecte Flock-You

El projecte Flock-You prospera gràcies a les contribucions de la comunitat:

**Repositori GitHub**: [github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)

**Maneres de Contribuir**:
1. **Descobriment de Nous OUIs**: Envia OUIs de càmeres Flock recentment identificats
2. **Millores de Codi**: Envia sol·licituds de fusió per a millores del microprogramari
3. **Dissenys de Maquinari**: Comparteix dissenys de dispositius de detecció personalitzats
4. **Documentació**: Millora les guies de configuració, les traduccions
5. **Proves**: Informa d'errors, verifica la funcionalitat entre dispositius
6. **Cartografia**: Contribueix a les bases de dades d'ubicació de càmeres de multituds

### Recursos de la Comunitat

**Fòrums i Debat**:
- **Reddit**: r/privacy, r/privacytoolsIO, debats actius
- **Discord**: Servidor Colonel Panic Tech, xat en temps real
- **GitHub Issues**: Suport tècnic i sol·licituds de funcions

**Articles d'Investigació**:
- Estudis acadèmics sobre la vigilància ALPR
- Avaluacions d'impacte en la privacitat
- Anàlisis legals de la legalitat dels dispositius de detecció

**Organitzacions de Defensa**:
- **Electronic Frontier Foundation** (EFF): Seguiment ALPR
- **ACLU**: Vigilància i drets de privacitat
- **Grups locals**: DeFlockJoplin i iniciatives comunitàries similars

### Full de Ruta de Desenvolupament Futur

**Funcions Planificades** (des del GitHub del projecte):
- **Aprenentatge automàtic**: Reconeixement de patrons per a major precisió
- **Sincronització al núvol**: Base de dades de detecció de multituds opcional
- **Aplicacions mòbils**: Integració de telèfon intel·ligent per a interfícies millorades
- **Modes de detecció addicionals**: Altres tecnologies de vigilància
- **Alertes en temps real**: Notificacions push via mòbil/WiFi

______

## Conclusió: Ajudant la Privacitat Mitjançant la Tecnologia

El **projecte de detecció Flock-You** representa una poderosa democratització de la tecnologia de contra-vigilància. Per menys del cost d'una subscripció mensual de streaming, les persones obtenen consciència de la infraestructura de vigilància que les envolta. Tant si tries la **construcció DIY ESP32 ($5-12)**, el **M5 Atom Lite llest per usar ($40)** o el **multi-mode OUI-SPY ($85)**, estàs invertint en consciència de la privacitat i autonomia digital.


*Recorda què cobreix aquest maquinari i què no: detecta càmeres Flock per WiFi. No detecta Stingray ni rastrejadors personals que es moguin amb tu. Si necessites una cobertura més àmplia, combina’l amb Rayhunter i Eye Spy, enllaçats més avall.*

### Punts Principals

- **Codi obert i modificable gratuïtament**: el desenvolupament comunitari manté actualitzades la llista OUI i el microprogramari
- **Maquinari assequible**: un ESP32 nu costa 5–12 $; cada nivell superior afegeix comoditat, no capacitats de detecció
- **Només monitoratge passiu**: el dispositiu rep trames Wi-Fi difoses públicament i no transmet res
- **Actualitzacions periòdiques**: s’incorporen noves signatures OUI i recerca de probes comodí quan canvia el maquinari de Flock
- **Verificat sobre el terreny**: la comunitat DeFlockJoplin va detectar 11 de 12 càmeres conegudes en una prova real amb cotxe

### Pròxims Passos

1. **Llegeix el context**: [Vigilància amb càmeres Flock Safety: Privadesa i Protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)
2. **Tria la plataforma**: adapta el muntatge DIY ESP32, M5 Atom Lite o OUI-SPY al pressupost i als coneixements
3. **Demana el maquinari**: compra’l a un proveïdor autoritzat de la llista anterior
4. **Instal·la i configura**: segueix la guia de la plataforma triada
5. **Uneix-te a la comunitat**: comparteix resultats i contribueix amb deteccions al projecte
6. **Cobreix els límits del dispositiu**: combina’l amb [Com flashejar dispositius Rayhunter: guia completa](/articles/how-to-flash-rayhunter-devices-complete-guide/) per detectar captadors IMSI i amb [Eye Spy: detector passiu de vigilància per a M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/) per detectar AirTags i altres rastrejadors

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compra dispositius FlockYou llestos per usar i estalvia un 20%
{{< /centerbutton >}}

La proliferació de la vigilància ALPR representa un canvi significatiu en la dinàmica de la privacitat. Les tecnologies de contra-vigilància com Flock-You ofereixen una capacitat crucial: **consciència**. Quan entenem l'abast i l'escala de la vigilància, prenem decisions informades sobre els nostres moviments, la nostra defensa i les nostres expectatives de privacitat als espais públics.

______

## Articles Relacionats

| Article | Descripció |
|---------|-------------|
| **[Vigilància amb càmeres Flock Safety: Privadesa i Protecció](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | La guia definitiva sobre la xarxa ALPR de Flock Safety, abusos documentats, recursos d'organització comunitària i el que pots fer per protegir-te |
| **[Flock Finder: Mapa de càmeres ALPR de Flock Safety](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Com utilitzar l'eina de codi obert Flock Finder per visualitzar més de 40.000 càmeres Flock sospitoses a tot el món usant dades WiGLE i empremtes digitals OUI |
| **[Eye Spy: detector passiu de vigilància per a M5Stack Atom Lite](/articles/eye-spy-passive-surveillance-detector-esp32-2026/)** | Detector BLE i Wi-Fi que cobreix allò que Flock-You no detecta: AirTags, rastrejadors Tile, càmeres corporals i drons, amb la mateixa família de maquinari. |
| **[Com instal·lar el microprogramari Rayhunter en dispositius de detecció d’interceptors IMSI](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Guia pas a pas per fer flash del microprogramari Rayhunter per detectar interceptors IMSI i stingrays, complementa la detecció ALPR |
| **[Firmware personalitzat DagShell per a Orbic RCL400: guia de 2026](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | Guia completa per instal·lar DagShell a l'Orbic RCL400 per al monitoratge avançat de xarxes mòbils i la detecció d'interceptors IMSI |
| **[Comparació de Dispositius Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Comparació costat a costat de dispositius compatibles amb Rayhunter per ajudar-te a triar el maquinari adequat per al teu kit d'eines de contra-vigilància |

Busques una eina que neutralitzi els rastrejadors en lloc de limitar-se a detectar-los? [Simulacra](https://github.com/Em3ritus/simulacra) és un projecte de codi obert independent i sense afiliació que escampa dispositius BLE i Wi-Fi d’esquer per ocultar el senyal del teu dispositiu real. Resol un problema diferent del dels dispositius d’aquesta guia i pot ser útil si la detecció passiva no basta per al teu model d’amenaces.

______

## Referències

1. [Repositori GitHub de Flock-You - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [Flock Finder - mapa interactiu de càmeres ALPR](https://simeononsecurity.github.io/flock-finder/)
3. [Flock Finder - repositori GitHub](https://github.com/simeononsecurity/flock-finder)
4. [Colonel Panic Tech - lloc web oficial del proveïdor](https://colonelpanic.tech)
5. [STS Collective - M5 Atom Lite amb firmware preinstal·lat](https://stscollective.com)
6. [Documentació oficial de M5Stack Atom Lite](https://docs.m5stack.com/en/core/ATOM%20Lite)
7. [Documentació de l’API WiFi d’ESP32 d’Espressif](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html)
8. [Referència de sol·licituds i respostes Probe 802.11](https://mrncciew.com/2014/10/27/cwap-802-11-probe-requestresponse/)
9. [DeFlock Joplin - recerca comunitària sobre ALPR](https://deflockjoplin.today)
10. [DeFlock - mapa i dades ALPR col·laboratius](https://deflock.me/)
11. [Electronic Frontier Foundation - què és l’ALPR?](https://www.eff.org/pages/what-alpr)
12. [Descàrrega oficial de l’Arduino IDE](https://www.arduino.cc/en/software)
13. [Documentació de Platform.io](https://docs.platformio.org/)
14. [IEEE Registration Authority - bloc gran d’adreces MAC (OUI)](https://standards.ieee.org/products-programs/regauth/oui/)
15. [Referència de l’estructura de trames Beacon 802.11](https://mrncciew.com/2014/10/08/802-11-mgmt-beacon-frame/)
