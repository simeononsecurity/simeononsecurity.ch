---
title: "SenseCAP M1 Raspberry Pi Shield: pinout i reutilització amb LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Entén la shield SenseCAP M1, compara mapes GPIO contradictoris, inspecciona l’ATECC608 i planifica una passarel·la LoRaWAN amb una versió moderna de Raspberry Pi OS."
genre: ["Raspberry Pi", "IoT", "Seguretat del maquinari"]
tags: ["SenseCAP M1", "Shield SenseCAP M1", "Pinout SenseCAP M1", "Shield Raspberry Pi", "Raspberry Pi HAT", "Passarel·la LoRaWAN", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Reutilització d'un hotspot Helium", "Concentrador LoRa", "SPI GPIO", "GPIO17", "LED GPIO22", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "Diagnòstic I2C", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "Enginyeria inversa del maquinari"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "Shield SenseCAP M1 amb un mòdul Seeed WM1302, connector Raspberry Pi, cable d'antena, presa USB-C i connector de ventilador"
coverCaption: "Fotografia de la placa: Clockwork Bird, 2023. La font i l'atribució són al final de l'article."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**La shield SenseCAP M1 és útil com a maquinari de passarel·la LoRaWAN, però el seu cablejat exigeix més comprovacions que un tutorial genèric de Raspberry Pi HAT.** Aquesta guia amplia [la investigació de Clockwork Bird de 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) amb documentació del fabricant, una revisió d'un controlador upstream i recomanacions GPIO actuals. Identificaràs el maquinari, separaràs els fets confirmats de les dades incompletes del pinout i crearàs un registre de posada en servei reproduïble.

> **Abast:** Aquesta és una guia de maquinari basada en documentació. Les ordres i els mapes de la placa no s'han provat en un M1 físic per a aquest article.

## Punts principals

- **Identifica les dues plaques:** el suport M1 i el concentrador extraïble tenen models i revisions propis.
- **Revisa els scripts de reinici:** els valors per defecte de CoreCell entren en conflicte amb senyals del pinout M1 publicat.
- **Comprova les interfícies del sistema:** els fitxers de dispositiu SPI, la numeració GPIO i les versions de les eines GPIO responen preguntes diferents.
- **Preserva el provisionament de l'element segur:** llegir informació del dispositiu no és el mateix que configurar-lo o generar claus.
- **Valida el recorregut complet:** detectar un concentrador no demostra que s'entreguin les dades del sensor.

## Abans de començar

**Dificultat: intermèdia.** Reserva aproximadament d'una a dues hores per inventariar, preparar el sistema i revisar la documentació. La verificació elèctrica, l'adaptació del controlador i el desplegament del servidor de xarxa requereixen més feina, especialment si desconeixes la revisió de la placa.

| Element | Finalitat |
|---|---|
| **Shield M1 i concentrador** | Llegeix la revisió del suport i l'etiqueta completa del mòdul |
| **Raspberry Pi 4** | Comença amb l'amfitrió utilitzat en el disseny M1 original |
| **Targeta microSD de recanvi** | Prepara un altre sistema sense perdre la instal·lació original |
| **Font d'alimentació i antena adequades** | Ajusta-les al conjunt i a la banda RF del mòdul |
| **SSH o consola local** | Registra els diagnòstics i edita la configuració |
| **Sensor i servidor LoRaWAN** | Verifica el lliurament real a l'aplicació després d'iniciar el maquinari |
| **Multímetre i experiència amb maquinari** | Resol les connexions no documentades abans d'accionar-les |

Fotografia les dues cares del conjunt desconnectat abans de treure cap peça. Anota l'orientació dels connectors, els cargols, els separadors i el recorregut de l'antena. Mantén disponibles la targeta i la configuració originals fins que la instal·lació nova superi les proves d'acceptació.

## Identifica les tres capes

**El M1 complet, el suport shield i el concentrador són components diferents.** Seeed descriu el hotspot muntat com un Raspberry Pi 4 amb un concentrador WM1302/SX1302 o WM1303/SX1303. Un anunci titulat «SenseCAP M1 shield» no indica quin d'aquests components acompanya el suport. [Visió general del M1 de Seeed Studio](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

El **suport** connecta l'alimentació i els senyals perifèrics entre el Pi i el mòdul. El **concentrador** gestiona la recepció i la transmissió de ràdio. Un **reenviador de paquets** a l'amfitrió intercanvia amb un servidor els paquets de ràdio rebuts i els enllaços descendents programats. [Visió general del SX1302 HAL de Semtech](https://github.com/Lora-net/sx1302_hal)

Per exemple, un sensor de temperatura de prestatgeria envia un enllaç ascendent per ràdio. El concentrador el rep, l'amfitrió el reenvia i els serveis de xarxa i aplicació el processen. Que Linux s'iniciï només demostra la part de l'amfitrió d'aquesta cadena.

La fotografia de Clockwork Bird mostra un suport M1 v1.1 amb un mòdul etiquetat explícitament `WM1302-SPI-EU868`. Fes-la servir per localitzar les etiquetes del teu maquinari. Els números de sèrie identifiquen l'equip fotografiat, no la configuració d'una altra passarel·la.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Suport M1 verd amb un mòdul WM1302 SPI EU868 etiquetat, al costat d'USB-C, un botó, el connector del ventilador i el cable de l'antena" caption="Maquinari M1 v1.1 fotografiat per Clockwork Bird, també utilitzat a la portada d'aquest article" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Connexions d'alimentació i ràdio

**Tracta el connector USB-C del M1 com una entrada d'alimentació.** El fabricant especifica 5 V CC, 3 A per a tota la passarel·la i identifica USB-C com la interfície d'alimentació. Anomenar-lo port de càrrega suggereix una bateria absent d'aquestes especificacions. [Especificacions del SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

El diagrama de blocs del fabricant separa la font de 5 V del rail regulat de 3,3 V del mòdul. Aquesta diferència és important en el diagnòstic: el Pi pot funcionar mentre el concentrador no rep alimentació. No injectis 5 V en un pin de senyal ni pressuposis que les dues entrades d'alimentació estan aïllades entre si.

**Les variants SPI i USB del mòdul requereixen connexions diferents amb l'amfitrió.** La documentació WM1302 de Seeed descriu accés SPI directe per al model SPI i un pont USB STM32L4 per al model USB. La forma mini-PCIe descriu el format del mòdul, mentre que les interfícies elèctriques documentades són SPI o USB. Encaixar en una presa de portàtil no demostra compatibilitat. [Documentació WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

Abans d'alimentar el conjunt, instal·la el mòdul amb l'alimentació desconnectada i connecta una antena adequada. Ajusta el maquinari RF, l'antena i el pla regional previst. Canviar el nom d'un fitxer de configuració no modifica els components RF, i la presa d'alimentació M1 no demostra compatibilitat amb una variant USB del concentrador.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Diagrama de blocs que connecta el Raspberry Pi 4 amb la shield M1 mitjançant alimentació, SPI, GPIO i I2C" caption="Diagrama del fabricant SenseCAP reproduït a l'article original de Clockwork Bird, que mostra el disseny WM1302" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Llegeix atentament el pinout

**Anota per separat els números GPIO BCM i els pins físics del connector.** Per exemple, BCM GPIO17 correspon al pin físic 11 del connector Pi. El connector de vora del mòdul afegeix un tercer sistema de numeració, de manera que el seu número de pin de reinici no és un número GPIO de Raspberry Pi.

La taula següent transcriu les connexions de la imatge anotada de Clockwork Bird. És una **referència comunitària**, no un esquema complet del fabricant ni una mesura de totes les revisions M1. El dibuix també utilitza etiquetes `SX1262`, mentre que el script genèric de reinici Semtech fa servir noms `SX1261`.

| Senyal del dibuix | BCM / pin físic | Interpretació |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Bus de gestió compartit |
| **Reinici SX1302** | GPIO17 / 11 | Candidat a reinici del concentrador |
| **LED d'usuari** | GPIO22 / 15 | Anotació M1 |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | Senyals de dades SPI |
| **Rellotge SPI** | GPIO11 / 23 | Senyal de rellotge SPI |
| **Selecció SX1302** | GPIO8 / 24 | SPI0 CE0 |
| **Reinici SX1262** | GPIO5 / 29 | Candidat a reinici de la ràdio auxiliar |
| **Selecció SX1262** | GPIO6 / 31 | GPIO6, diferent de SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Sortida d'estat de la ràdio auxiliar |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Senyals auxiliars que cal verificar abans d'utilitzar |

Les anotacions GPS/UART ratllades no demostren que el M1 tingui GPS. No afegeixis configuració GPS si el teu maquinari no en té. El diagrama publicat tampoc no resol el botó d'usuari ni el control del ventilador. [Investigació del pinout de Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Dibuix anotat del connector Raspberry Pi amb el LED M1, el reinici del concentrador, els senyals SPI i les connexions GPS ratllades" caption="Referència anotada per la comunitat amb cobertura incompleta de revisions, no és un esquema M1 complet" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Resol els conflictes dels scripts de reinici

**Un script de reinici selecciona sortides elèctriques, no només preferències de programari.** El `reset_lgw.sh` upstream de Semtech s'adreça al disseny de referència CoreCell. Els valors per defecte inclouen GPIO23 per al reinici del concentrador, GPIO18 per habilitar l'alimentació, GPIO22 per al reinici auxiliar i GPIO13 per al reinici de l'AD5338R. [Codi font del script de reinici Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Les instruccions antigues de configuració de Seeed canvien les dues assignacions de reinici a GPIO17 i GPIO5, però conserven les altres entrades del disseny de referència. Compara els valors amb la imatge M1 anotada abans de seguir l'exemple. [Instruccions de configuració WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc)

| Assignació | Evidència contradictòria | Decisió necessària |
|---|---|---|
| **GPIO22 com a reinici auxiliar** | La imatge M1 l'identifica com a LED d'usuari | Elimina aquesta suposició abans d'activar el LED |
| **GPIO18 com a activació d'alimentació** | La imatge M1 l'identifica com a BUSY auxiliar | Verifica la xarxa i la direcció abans d'accionar-lo |
| **GPIO13 com a reinici del DAC** | L'script genèric anomena un altre disseny de referència | Determina si el circuit existeix |
| **Dispositiu SPI auxiliar** | La imatge M1 selecciona GPIO6 en lloc de CE1 | Confirma l'encaminament de selecció i el suport del controlador |

**Inferència:** si GPIO18 està connectat a una sortida de ràdio auxiliar tal com es dibuixa, configurar el costat Pi com a sortida crea risc de contenció elèctrica. La discrepància exigeix verificació, però no demostra que hi hagi danys ni que tots els M1 tinguin el mateix cablejat.

Desconnecta totes les fonts d'alimentació i traça les connexions accessibles entre el connector i el mòdul. Anota la revisió de la placa i els dos extrems. La continuïtat demostra connexió, mentre que la documentació del component n'estableix la direcció del senyal i els límits elèctrics.

Fes servir el diagrama del mòdul de sota per no confondre els pins del connector de vora amb els del Pi. Les etiquetes de ràdio auxiliar descriuen la referència publicada del mòdul, no demostren el mateix silici ni les mateixes funcions en totes les revisions. [Pinout del mòdul WM1302 de Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Diagrama de Seeed amb les dues cares del connector de vora WM1302 i els senyals d'alimentació, SPI, I2C i ràdio auxiliar" caption="La numeració del connector de vora del mòdul és diferent de la numeració del connector Raspberry Pi" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Prepara Raspberry Pi OS

Registra l'entorn de l'amfitrió a la instal·lació de recanvi:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

La versió del sistema, el kernel i el model Pi constitueixen el punt de partida reproduïble. Anota'ls abans de comparar resultats amb un tutorial antic.

Instal·la eines d'inspecció i compilació:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

A **Interface Options**, activa SPI i I2C i reinicia. SPI serveix per al recorregut del concentrador, mentre que I2C serveix per als dispositius de gestió descrits més endavant. No importis canvis de port sèrie GPS sense relació d'un tutorial d'un altre HAT.

Inspecciona les interfícies exposades:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Aquestes ordres mostren nodes de dispositiu, adaptadors, controladors GPIO, línies i la versió de l'eina GPIO instal·lada. **`i2cdetect -l` enumera adaptadors sense escanejar adreces.** El fitxer `/dev/spidev0.0` demostra que hi ha una interfície SPI exposada, no que es comuniqui amb un concentrador funcional. [Manual i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [Recomanacions GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Tingues en compte les versions GPIO

**No copiïs números GPIO globals d'una altra màquina.** Els scripts antics escriuen a través de `/sys/class/gpio`, una interfície que la documentació del kernel considera obsoleta. Les integracions noves a l'espai d'usuari han d'utilitzar la interfície GPIO character device amb el controlador i el desplaçament de línia correctes. [Documentació Linux GPIO](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Consulta també `gpioset --help` abans d'adaptar un script. La sintaxi i el comportament dels processos són diferents entre les versions 1 i 2. L'eina actual manté per defecte les línies sol·licitades, però el contracte portable no garanteix l'estat després que el procés acabi. [Documentació gpioset de libgpiod](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi documenta un comportament de persistència de sortides al seu kernel i opcions per canviar-lo. Registra la configuració real del kernel en lloc de suposar que tots els Linux es comporten igual. Una numeració nova o una eina GPIO més recent no corregeix un mapa elèctric incorrecte. [Guia d'ús GPIO de Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## Prova el LED d'usuari

Després de comprovar que GPIO22 pertany al LED i d'eliminar els usos GPIO en conflicte, edita la configuració d'arrencada:

```bash
sudoedit /boot/firmware/config.txt
```

Les versions modernes de Raspberry Pi OS munten la configuració d'arrencada a **`/boot/firmware/config.txt`**. Les imatges antigues fan servir `/boot/config.txt`, el camí de l'article de 2023. Fes una còpia de seguretat del fitxer actiu abans d'editar-lo. [Documentació config.txt de Raspberry Pi](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Afegeix l'overlay LED en una secció aplicable al teu Pi, com ara `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

El paràmetre **`gpio`** utilitza numeració BCM. **`label`** assigna un nom al dispositiu LED Linux, i **`trigger=heartbeat`** tria el trigger heartbeat del kernel. Clockwork Bird indica aquesta assignació per al M1, i la referència d'overlays de Raspberry Pi documenta aquests paràmetres. [Observació original del LED](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Referència de l'overlay gpio-led](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Després de reiniciar, inspecciona el LED registrat:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

El resultat esperat és una entrada LED `lorawan` amb `heartbeat` seleccionat entre claudàtors. El parpelleig demostra que funciona el recorregut GPIO/controlador. No indica registre LoRaWAN, recepció de ràdio ni estat Helium.

## Investiga els dispositius I2C

**Una adreça I2C és una pista, no la identitat d'un dispositiu.** Clockwork Bird va observar respostes a `0x60` i `0x39`, i després va llegir informació ATECC608 amb la biblioteca criptogràfica. La identificació del sensor de temperatura continuava sent provisional a l'article original.

Comença amb la llista d'adaptadors de la secció anterior. Les exploracions àmplies de `i2cdetect` envien transaccions de prova, no observen passivament el trànsit; el manual upstream adverteix que poden provocar interrupcions. Evita escanejar de rutina una passarel·la en funcionament o dispositius connectats desconeguts. [Comportament de prova d'i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Observació | Conclusió fonamentada | Pregunta no resolta |
|---|---|---|
| **Resposta a `0x60`** | Alguna cosa ha reconegut la prova | És l'element segur esperat? |
| **Resposta a `0x39`** | Alguna cosa ha reconegut la prova | Quin component i revisió han respost? |
| **`UU` a l'escaneig** | Un controlador ocupa l'adreça i s'ha omès la prova | Quin controlador la té? |
| **Sense resposta** | La prova no ha rebut confirmació | Alimentació, bus, propietari o protocol? |

### Aprofundeix en la pista del sensor de temperatura

**STTS751 és un candidat per a `0x39` amb suport documental.** La capçalera del controlador de temperatura de Semtech associa explícitament `0x39` amb `STTS751-0DP3F`. Això reforça la hipòtesi original, però no identifica tots els components instal·lats a aquesta adreça. [Capçalera del controlador STTS751 de Semtech](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Després d'identificar un component compatible i comprovar que cap altre procés l'ocupa, llegeix els registres d'identificació:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Aquí, **`1`** selecciona el bus verificat, **`0x39`** el dispositiu i **`b`** demana una lectura SMBus byte-data. Per a l'STTS751-0, l'ID de producte documentat a `0xFD` és `0x00`, i l'ID del fabricant a `0xFE` és `0x53`. Aquestes transaccions seleccionen adreces de registre, però no escriuen valors de configuració. [Full tècnic STTS751, mapa i registres d'identificació](https://www.st.com/resource/en/datasheet/stts751.pdf)

Compara les lectures amb el marcatge del xip i la documentació. Una parella coincident reforça la identificació; si hi ha un error, comprova el bus i el propietari abans de canviar la configuració. El sensor mesura la temperatura local, diferent de la del processador Pi.

## Inspecciona l'element segur

**L'ATECC608 és un component d'autenticació independent.** Tracta la configuració, el número de sèrie, la clau pública i el material de clau protegit com a conceptes separats. Llegir una clau pública no revela la clau privada corresponent.

La **CryptoAuthLib** de Microchip proporciona la interfície del dispositiu. El repositori **cryptoauthtools** conté exemples basats en la biblioteca. Prepara la biblioteca nativa i les bindings Python per al sistema objectiu seguint les instruccions dels projectes abans d'executar un exemple. Instal·lar un paquet Python sense relació o copiar un únic script no demostra que el backend I2C funcioni. [CryptoAuthLib de Microchip](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools de Microchip](https://github.com/MicrochipTech/cryptoauthtools)

Des d'un directori `cryptoauthtools/python/examples` preparat, executa l'ordre d'inspecció de l'article original:

```bash
sudo python3 info.py -i i2c
```

L'argument **`-i i2c`** selecciona la interfície. En un entorn virtual, utilitza explícitament el seu intèrpret Python i comprova que localitzi la biblioteca nativa corresponent. En moltes instal·lacions, `sudo python3` selecciona l'intèrpret del sistema, cosa que explica alguns errors d'importació de mòduls.

El `info.py` revisat llegeix dades de revisió, el número de sèrie, la configuració i l'estat dels bloquejos. Si la zona de dades està bloquejada, intenta recuperar la clau pública de l'slot 0. No executa la seqüència de provisionament de l'exemple. Un error aïllat en la lectura d'aquesta clau no demostra que el dispositiu estigui espatllat. [Codi font info.py de Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Sortida o operació | Significat |
|---|---|
| **Configuració bloquejada** | Hi ha restriccions de configuració actives |
| **Zona de dades bloquejada** | Interpreta l'accés segons les polítiques configurades dels slots |
| **Clau pública mostrada** | S'han recuperat dades públiques, no s'ha exportat una clau privada |
| **Execució de `config.py`** | Exemple de provisionament amb escriptura de configuració, bloqueig i generació de claus |

**No executis `config.py` per corregir un error d'inspecció.** El codi inclou escriptures de configuració, ordres per bloquejar zones i generació de claus. La ruta de generació predeterminada també és important en dispositius ja configurats. [Codi font config.py de Microchip](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Els perfils de provisionament documentats per Microchip mostren per què bloquejar la zona de dades no implica que tots els slots tinguin els mateixos permisos. Aquests perfils no estableixen la configuració exacta del M1. Conserva la configuració existent i consulta la documentació del component corresponent abans de planificar la reutilització de claus. [Polítiques Microchip de memòria i accés als slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Investiga les incògnites del ventilador i el botó

**Una presa de ventilador de tres pins no n'estableix la tensió, la polaritat ni el mètode de control.** Fotografia la numeració i llegeix l'etiqueta del ventilador. Confirma les connexions d'alimentació i control abans de connectar-ne un de recanvi o triar un overlay GPIO.

La investigació original tampoc identifica el GPIO del botó. Busca un controlador o una configuració associats a la revisió de la placa i verifica la connectivitat sense alimentació. No configuris totes les GPIO aparentment lliures com a sortides per trobar el botó.

| Perifèric | Evidència que cal recollir | Criteri d'acceptació |
|---|---|---|
| **Alimentació del ventilador** | Potència nominal, terra i alimentació del connector | La font mesurada coincideix amb les especificacions del ventilador |
| **Control del ventilador** | Controlador/configuració o circuit de control traçat | Comportament definit a l'inici i amb temperatura elevada |
| **Botó d'usuari** | Cablejat dels contactes, mapa GPIO, polaritat d'entrada | Una sola pulsació intencionada genera l'esdeveniment esperat |

Una instal·lació nova del sistema no reprodueix automàticament la política de refrigeració del dispositiu original. A la primera prova prolongada, observa alhora el ventilador i les temperatures. Mantén el flux d'aire de la carcassa i atura la prova si el conjunt perd la refrigeració necessària.

## Tria una pila de passarel·la

**Separa el suport de la placa del protocol del servidor.** Un servidor LoRaWAN compatible no corregeix una rutina de reinici incorrecta ni un calibratge RF inadequat. Tria primer programari compatible amb el concentrador, el cablejat del suport, el sistema i la configuració regional.

| Opció de programari | Funció útil | Comprovació abans del desplegament |
|---|---|---|
| **Semtech SX1302 HAL** | Arrencada a nivell de codi font i eines de diagnòstic | Rutina de reinici de placa i configuració del mòdul |
| **LoRa Basics Station** | Connexió autenticada entre passarel·la i servidor | Integració funcional de la placa i credencials del servidor |
| **ChirpStack Concentratord** | Servei dedicat al concentrador | Model compatible, calibratge i mapa GPIO |

ChirpStack llista el model SPI **`seeed_wm1302`**. Això demostra compatibilitat amb el mòdul, no l'existència d'una imatge M1 completa ni el suport de totes les revisions M1. No tractis les instruccions d'instal·lació de SenseCAP M2 com a instruccions de firmware M1. [Compatibilitat de maquinari ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Objectiu d'instal·lació Seeed ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Per a The Things Stack, la documentació recomana **LoRa Basics Station** en lloc del reenviador UDP Semtech antic. Station ofereix TLS i autenticació amb token, a més de funcions de configuració centralitzada. Els exemples UDP ajuden a entendre el reenviament de paquets, però la configuració de l'adreça del servidor no aporta aquestes proteccions. [Recomanacions UDP de The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentació LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Prepara les eines upstream

Compila al Pi objectiu en un directori de treball nou:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Desa l'identificador del commit amb la sortida de compilació. Una compilació correcta demostra compatibilitat amb el compilador, però la ràdio també necessita una implementació de reinici verificada i una configuració correcta. La documentació Semtech explica la funció del HAL i les eines auxiliars. [Documentació de compilació i eines SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Revisa el fitxer de reinici abans d'executar eines d'accés al maquinari:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

No copiïs aquest fitxer sense canvis al directori d'execució. Semtech documenta l'ús automàtic del script de reinici pels seus programes d'accés al maquinari, incloses les eines d'identificació. La revisió ha d'incloure cada pin assignat, direcció del senyal, API GPIO i estat d'inici i aturada.

Després de verificar la placa, segueix les instruccions de la pila triada per llegir l'EUI del concentrador i registrar la passarel·la. Conserva el calibratge del mòdul i la configuració RF en afegir els paràmetres del servidor. A la configuració UDP Semtech, `gateway_ID` representa l'EUI; el Gateway ID de la consola The Things Stack és l'identificador llegible emprat en el registre. [Configuració de passarel·la The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Demostra el lliurament del sensor

**Fes servir proves per etapes per trobar la primera capa que falla.** Que una passarel·la aparegui en línia demostra una connexió amb el servidor. La prova d'acceptació també necessita un sensor conegut, un pla de freqüència coincident i una càrrega útil d'aplicació descodificada.

La seqüència següent és un pla de prova proposat, no resultats mesurats en un M1:

| Punt de control | Evidència que cal desar | Significat |
|---|---|---|
| **Amfitrió preparat** | Sistema, kernel, alimentació i inventari d'interfícies | Preparació Linux completada |
| **El concentrador respon** | EUI i registre d'inicialització correcta | La comunicació amfitrió-concentrador funciona |
| **Recepció de ràdio** | Paquet de sensor esperat i metadades de recepció | Funciona el recorregut de recepció configurat |
| **El servidor accepta** | Esdeveniment de passarel·la associat al sensor | Funcionen el reenviament i l'encaminament del servidor |
| **Descodificació de l'aplicació** | Mesura i marca de temps esperades | Funciona el recorregut de l'aplicació |
| **Recuperació després de reiniciar** | Les mateixes comprovacions després de reiniciar | La configuració d'inici és reproduïble |

Per a un sensor **OTAA**, confirma també l'intercanvi d'activació i l'enllaç ascendent posterior. OTAA vol dir activació over-the-air, el procediment d'unió que estableix una sessió. Rebre una petició d'unió no demostra que la unió o el recorregut descendent hagin funcionat. [Documentació d'activació The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnòstic pràctic:** la passarel·la es connecta al servidor i comunica l'EUI, però el sensor no apareix. Prioritza la configuració de transmissió del sensor, els canals de recepció seleccionats, el recorregut de l'antena i els registres de ràdio. Reprogramar l'ATECC608 no resoldria la falta d'evidència en aquest cas.

**Segon diagnòstic:** el paquet del sensor apareix localment, però no arriba a l'aplicació. Correlaciona l'hora del paquet amb els esdeveniments de la passarel·la i del servidor; després revisa l'encaminament, el registre del dispositiu i la descodificació. Un paquet RF al registre no és prou evidència per culpar el descodificador abans que el servidor accepti l'esdeveniment.

## Resol problemes segons el símptoma

| Símptoma | Comprova primer | Acció següent |
|---|---|---|
| **No hi ha fitxer de dispositiu SPI** | Configuració d'arrencada activa i opcions d'interfície | Activa la interfície prevista i reinicia |
| **Hi ha SPI, però falla la ràdio** | Alimentació, encaix, seqüència de reinici i selecció de xip | Verifica el recorregut elèctric abans de canviar el servidor |
| **Error d'exportació GPIO** | Supòsits sysfs antics i kernel instal·lat | Utilitza una implementació revisada per a l'API GPIO |
| **GPIO ja en ús** | Consumidor que mostra `gpioinfo` | Resol la propietat abans de tornar-ho a provar |
| **El LED falla després de configurar-lo** | Aplicació de l'overlay i conflictes GPIO22 | Inspecciona els dispositius LED registrats i el script de reinici |
| **Falta un dispositiu I2C** | Número de bus, alimentació i propietari actual | Investiga sense repetir exploracions àmplies |
| **Error en importar la biblioteca criptogràfica** | Intèrpret, bindings i ruta de la biblioteca nativa | Corregeix l'entorn de programari |
| **Falla la lectura de la clau pública** | Política del slot i lectures anteriors correctes | Revisa la configuració sense fer provisionament |
| **El ventilador no gira** | Alimentació verificada i control de refrigeració | Restableix la refrigeració abans de proves llargues |
| **Arriben uplinks, falla la unió** | Recorregut descendent i ajustos regionals/del dispositiu | Traça la resposta d'unió i les finestres de recepció |

Tracta cada correcció com un experiment únic. Desa la configuració anterior, canvia una variable, repeteix la mateixa comprovació i registra si apareix l'evidència esperada.

## Crea el registre del maquinari

Fes servir aquesta plantilla per convertir la investigació en un traspàs reproduïble:

```text
Revisió del suport i fotografies:
Model del concentrador, interfície i banda RF:
Model de l'amfitrió / sistema / kernel / versió de l'eina GPIO:
Font / antena / disposició de refrigeració:
Mapa de pins verificat i evidències:
Xarxes no resoltes i funcions excloses:
Repositori del programari i commit:
Implementació de reinici i propietari GPIO:
EUI de la passarel·la / servidor / pla de freqüències:
Activació del sensor i evidència d'uplink descodificat:
Resultat de recuperació després de reiniciar:
Ubicació de la targeta original i procediment de rollback:
```

**Exercici de decisió:** tens un suport nu econòmic sense etiqueta de mòdul i un conjunt més car amb etiquetes llegibles i funcionament documentat. Decideix què s'ajusta al projecte després d'afegir al comparatiu el Pi, el concentrador, l'antena, la font i el temps de verificació. La millor opció depèn del cost total i de les proves que exigeix el servei previst, no només del preu del suport.

**Raonament esperat:** un projecte d'aprenentatge tolera cablejat no resolt si tens instruments de mesura i temps. Una passarel·la per a sensors operatius necessita inici reproduïble, refrigeració, suport de programari i lliurament demostrat. Anota quina condició no resolta aturaria el desplegament.

## Passos següents

Comença completant el registre del maquinari i resolent les discrepàncies del script de reinici. Després, posa en marxa un sensor conegut i desa proves fins a la descodificació de l'aplicació abans d'afegir més dispositius.

**Registre d'acceptació:** desa la revisió de la placa, l'etiqueta del mòdul, la banda de ràdio, la mesura de la font, el dispositiu SPI actiu, els noms de les línies GPIO, la seqüència de reinici, el registre del concentrador, la connexió al servidor i un uplink descodificat. Marca cada valor com a observat, documentat o encara suposat. No tractis l'inici d'un procés com a prova del rendiment RF o del lliurament a l'aplicació.

Si el teu objectiu és la missatgeria mesh, compara primer els rols dels protocols a la nostra [guia Meshtastic, MeshCore i Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Compartir tecnologia de ràdio LoRa no demostra compatibilitat del firmware. Per desplegar missatgeria, consulta la [documentació del maquinari compatible amb MeshtasticD](https://meshtastic.org/docs/meshtasticd/) en lloc de tractar aquest procediment LoRaWAN com una conversió a Meshtastic.

## Fonts i crèdits de les imatges

Recerca verificada el 12 de setembre de 2026. Els enllaços sense data a documentació i repositoris fan referència a les versions revisades per a aquest article. Les figures locals conserven les etiquetes i l'atribució originals.

| Editor | Font i data |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Fotografia de la placa, connector anotat i diagrama de blocs del fabricant reproduït |
| **Seeed Studio / SenseCAP** | [Visió general i especificacions M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/), sense data. Atribució del diagrama original |
| **Seeed Studio** | [Documentació WM1302 i pinout del mòdul](https://github.com/seeed-lora/WM1302-doc), repositori |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), incloses les fonts enllaçades del script de reinici i del controlador de temperatura |
| **Raspberry Pi** | [Configuració d'arrencada](https://www.raspberrypi.com/documentation/computers/config_txt.html), [guia d'ús GPIO](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) i [referència d'overlays](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Interfície GPIO sysfs obsoleta](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) i [manual gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), aquest darrer d'agost de 2026 |
| **i2c-tools** | [Manual i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), font v4.3 |
| **STMicroelectronics** | [Full tècnic STTS751](https://www.st.com/resource/en/datasheet/stts751.pdf), revisió 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) i [documentació de polítiques d'accés als slots](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Suport de maquinari Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) i [objectiu d'instal·lació Seeed](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [Reenviador UDP](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) i [activació de dispositius](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [Documentació MeshtasticD](https://meshtastic.org/docs/meshtasticd/), sense data |
