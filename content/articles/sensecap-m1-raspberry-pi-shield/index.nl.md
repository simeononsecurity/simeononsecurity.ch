---
title: "SenseCAP M1 Raspberry Pi Shield: pinout en hergebruik voor LoRaWAN"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "Bekijk de SenseCAP M1-shield, vergelijk tegenstrijdige GPIO-schema's, inspecteer de ATECC608 en plan met modern Raspberry Pi OS een LoRaWAN-gateway."
genre: ["Raspberry Pi", "IoT", "Hardwarebeveiliging"]
tags: ["SenseCAP M1", "SenseCAP M1 shield", "SenseCAP M1 pinout", "Raspberry Pi shield", "Raspberry Pi HAT", "LoRaWAN gateway", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium hotspot reuse", "LoRa concentrator", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C diagnostics", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "hardware reverse engineering"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "SenseCAP M1-shield met een Seeed WM1302-module, Raspberry Pi-header, antennekabel, USB-C-aansluiting en ventilatoraansluiting"
coverCaption: "Foto van de printplaat: Clockwork Bird, 2023. Bron en naamsvermelding staan hieronder."
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**De SenseCAP M1-shield is bruikbare LoRaWAN-gatewayhardware, maar de bedrading verdient meer aandacht dan in een algemene Raspberry Pi HAT-handleiding.** Deze gids bouwt voort op het [onderzoek van Clockwork Bird uit 2023](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/) en voegt fabrikantdocumentatie, inspectie van upstreamdrivers en actuele GPIO-richtlijnen toe. Je brengt de hardware in kaart, scheidt vastgestelde feiten van onvolledige pinoutinformatie en maakt een herhaalbaar opstartverslag.

> **Reikwijdte:** Dit is een hardwaregids op basis van documentatie. De opdrachten en pinindelingen zijn voor dit artikel niet getest op een fysieke M1.

## Belangrijkste punten

- **Identificeer beide printplaten:** de M1-drager en de verwijderbare concentrator hebben aparte model- en revisiegegevens.
- **Controleer resetscripts:** de standaardwaarden voor CoreCell botsen met signalen in de gepubliceerde M1-pinout.
- **Controleer de OS-interfaces:** SPI-apparaatbestanden, GPIO-nummering en versies van GPIO-tools beantwoorden verschillende vragen.
- **Behoud de beveiligingschipconfiguratie:** apparaatinfo lezen is iets anders dan sleutels configureren of genereren.
- **Bewijs het volledige pad:** een gevonden concentrator bewijst geen succesvolle sensorgegevensoverdracht.

## Voordat je begint

**Moeilijkheidsgraad: gemiddeld.** Reken ongeveer één tot twee uur voor inventarisatie, OS-voorbereiding en documentatiecontroles. Elektrische verificatie, driveraanpassingen en uitrol van de netwerkserver kosten extra tijd, vooral bij een onbekende printplaatrevisie.

| Onderdeel | Doel |
|---|---|
| **M1-shield en concentrator** | Noteer de revisie van de drager en het volledige etiket van de module |
| **Raspberry Pi 4** | Begin met de host uit het oorspronkelijke M1-ontwerp |
| **Reserve-microSD-kaart** | Bereid een afzonderlijk OS voor en bewaar de oorspronkelijke installatie |
| **Passende voeding en antenne** | Stem deze af op de assemblage en de RF-band van de module |
| **SSH of lokale console** | Leg diagnostiek vast en pas configuratie aan |
| **LoRaWAN-sensor en server** | Verifieer na het opstarten van de hardware de daadwerkelijke aflevering van gegevens |
| **Multimeter en hardware-ervaring** | Los ongedocumenteerde verbindingen op voordat je ze aanstuurt |

Fotografeer beide zijden van de spanningsloze assemblage voordat je iets verwijdert. Noteer de richting van connectoren, schroeven, afstandhouders en antenne. Bewaar de oorspronkelijke kaart en configuratie totdat de vervangende installatie je acceptatiecontroles doorstaat.

## Identificeer de drie lagen

**De volledige M1, de dragershield en de concentrator zijn verschillende onderdelen.** Seeed beschrijft de complete hotspot als een Raspberry Pi 4 met een WM1302/SX1302- of WM1303/SX1303-concentrator. Een vermelding met de titel "SenseCAP M1-shield" bewijst niet welke module bij de drager zit. [Overzicht van Seeed Studio voor de M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

De **drager** verbindt voeding en randapparatuursignalen tussen de Pi en module. De **concentrator** verzorgt radio-ontvangst en -verzending. Een **pakketforwarder** draait op de host en wisselt ontvangen radiopakketten en geplande downlinks uit met een server. [Overzicht van Semtechs SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Een temperatuursensor op een plank stuurt bijvoorbeeld een uplink via radio. De concentrator ontvangt die, de host stuurt hem door en de netwerk- en applicatieservices verwerken hem. Een succesvolle Linux-start bewijst alleen dat het hostdeel werkt.

De foto van Clockwork Bird toont een M1 v1.1-drager met een module waarop `WM1302-SPI-EU868` staat. Gebruik de foto om de labels op je eigen hardware te vinden. De serienummers identificeren de gefotografeerde apparatuur, niet de configuratiewaarden van een andere gateway.

{{< figure src="m1-carrier-wm1302-board.webp" alt="Groene M1-drager met gelabelde WM1302 SPI EU868-module naast USB-C, knop, ventilatoraansluiting en antennekabel" caption="M1 v1.1-hardware gefotografeerd door Clockwork Bird, ook gebruikt als omslag voor dit artikel" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Voeding en radioverbindingen

**Behandel de USB-C-aansluiting van de M1 als voedingsingang.** De fabrikant vermeldt 5 V gelijkspanning en 3 A voor de complete gateway en noemt USB-C de voedingsinterface. De term laadpoort suggereert een batterijfunctie die niet in die specificaties staat. [Specificaties van de SenseCAP M1](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

Het blokschema van de leverancier scheidt de 5V-voeding van de gereguleerde 3,3V-rail van de module. Dit verschil is belangrijk bij probleemoplossing: een werkende Pi en een spanningsloze concentrator zijn afzonderlijke mogelijkheden. Zet geen 5 V op een signaalpin en neem niet aan dat twee voedingangen van elkaar geïsoleerd zijn.

**SPI- en USB-modulevarianten vereisen verschillende hostverbindingen.** De WM1302-documentatie van Seeed beschrijft directe SPI-toegang voor het SPI-model en een STM32L4-USB-brug voor het USB-model. De mini-PCIe-vorm beschrijft de fysieke vormfactor. De gedocumenteerde elektrische interfaces zijn SPI of USB. Een passende aansluiting in een laptop bewijst geen compatibiliteit. [WM1302-documentatie van Seeed](https://github.com/seeed-lora/WM1302-doc)

Schakel de voeding uit voordat je de module plaatst en sluit een passende antenne aan. Stem radiohardware, antenne en het beoogde netwerkplan op elkaar af. Een andere configuratiebestandsnaam vervangt de RF-onderdelen van de module niet. De voedingsaansluiting van de M1 bewijst ook geen ondersteuning voor een USB-concentratorvariant.

{{< figure src="m1-power-spi-system-diagram.webp" alt="Blokschema met Raspberry Pi 4 verbonden met de M1-shield via voeding, SPI, GPIO en I2C" caption="Fabrikantschema van SenseCAP uit het oorspronkelijke artikel van Clockwork Bird, met het WM1302-ontwerp" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## Lees de pinout zorgvuldig

**Noteer BCM-GPIO-nummers en fysieke pinnummers in afzonderlijke kolommen.** BCM GPIO17 zit bijvoorbeeld op fysieke pin 11 van de Pi-header. De randconnector van de module gebruikt een derde nummering. Het resetpinnummer daarvan is geen GPIO-nummer van de Raspberry Pi.

De tabel schrijft de verbindingen over uit de geannoteerde headerafbeelding van Clockwork Bird. Dit is een **gemeenschapsreferentie**, geen volledig schema van de fabrikant of meting van elke M1-revisie. De tekening noemt ook `SX1262`, terwijl het algemene resetscript van Semtech namen voor `SX1261` gebruikt.

| Signaal in de tekening | BCM / fysieke pin | Betekenis |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3, GPIO3 / 5 | Gedeelde beheerbus |
| **SX1302-reset** | GPIO17 / 11 | Kandidaat voor reset van de concentrator |
| **Gebruikers-led** | GPIO22 / 15 | M1-aanduiding |
| **SPI MOSI / MISO** | GPIO10 / 19, GPIO9 / 21 | SPI-datasignalen |
| **SPI-klok** | GPIO11 / 23 | SPI-kloksignaal |
| **SX1302-chipselect** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262-reset** | GPIO5 / 29 | Kandidaat voor reset van de extra radio |
| **SX1262-chipselect** | GPIO6 / 31 | GPIO6, anders dan SPI0 CE1 |
| **SX1262 BUSY** | GPIO18 / 12 | Statusuitgang van de extra radio |
| **SX1262 IO1 / IO2** | GPIO23 / 16, GPIO24 / 18 | Extra signalen, verifieer vóór gebruik |

De doorgestreepte GPS/UART-aanduidingen bewijzen niet dat een M1 GPS bevat. Laat GPS-configuratie weg tenzij je hardware die functie biedt. Het gepubliceerde diagram geeft ook geen uitsluitsel over de gebruikersknop en ventilatorregeling. [Pinoutonderzoek van Clockwork Bird](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="Geannoteerde Raspberry Pi-headertekening met M1-led, concentratorreset, SPI-signalen en doorgestreepte GPS-verbindingen" caption="Gemeenschapsreferentie zonder bevestiging voor alle printplaatrevisies, geen volledig M1-schema" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## Tegenstrijdigheden in resetscripts oplossen

**Een resetscript kiest elektrische uitgangen, niet alleen softwarevoorkeuren.** Semtechs upstreambestand `reset_lgw.sh` is bedoeld voor het CoreCell-referentieontwerp. De standaardwaarden gebruiken GPIO23 voor reset van de concentrator, GPIO18 voor inschakeling van de voeding, GPIO22 voor een extra reset en GPIO13 voor een AD5338R-reset. [Broncode van het Semtech-resetscript](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

De oudere installatie-instructies van Seeed wijzigen de twee resettoewijzingen naar GPIO17 en GPIO5, maar laten andere waarden uit het referentieontwerp staan. Vergelijk die waarden met de geannoteerde M1-afbeelding voordat je het voorbeeld volgt. [WM1302-installatie-instructies van Seeed](https://github.com/seeed-lora/WM1302-doc)

| Toewijzing | Tegenstrijdige aanwijzing | Vereiste beslissing |
|---|---|---|
| **GPIO22 als extra reset** | M1-afbeelding noemt deze pin de gebruikers-led | Verwijder deze aanname voordat je de led inschakelt |
| **GPIO18 als voedingenable** | M1-afbeelding noemt deze pin de extra BUSY-uitgang | Controleer verbinding en richting voordat je de pin aanstuurt |
| **GPIO13 als DAC-reset** | Algemeen script noemt een ander referentieontwerp | Stel vast of het circuit aanwezig is |
| **Extra SPI-apparaat** | M1-afbeelding kiest GPIO6 in plaats van CE1 | Controleer chipselectverbinding en driverondersteuning |

**Afleiding:** als GPIO18 volgens de tekening verbonden is met een uitgang van een extra radio, veroorzaakt configuratie als uitgang op de Pi kans op elektrische conflicten. Het verschil vraagt om verificatie, maar bewijst geen schade en ook geen universele M1-bedrading.

Schakel alle voeding uit en volg toegankelijke verbindingen tussen header en moduleconnector. Noteer de printplaatrevisie en beide eindpunten. Een continuïteitsmeting toont een verbinding aan. De componentdocumentatie bepaalt de signaalrichting en elektrische grenzen.

Gebruik het onderstaande moduleschema van de fabrikant om pinnummers van de randconnector niet te verwarren met Pi-headerpinnen. De aanduidingen voor de extra radio beschrijven de gepubliceerde module-referentie. Ze bewijzen niet dat elke revisie dezelfde chip of functies heeft. [WM1302-pinout van Seeed](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Seeed-tekening met beide zijden van de WM1302-randconnector en voeding, SPI, I2C en radiosignalen" caption="De nummering van de moduleconnector wijkt af van de Raspberry Pi-header" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## Raspberry Pi OS voorbereiden

Leg de hostomgeving op je reserve-installatie vast:

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

De OS-versie, kernel en Pi-model vormen het startpunt voor reproduceerbaarheid. Noteer deze gegevens voordat je resultaten met een oudere handleiding vergelijkt.

Installeer inspectie- en bouwtools:

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

Schakel in **Interface Options** SPI en I2C in en start daarna opnieuw op. SPI ondersteunt de concentratorverbinding. I2C ondersteunt de hieronder besproken beheeronderdelen. Neem geen niet-gerelateerde GPS-aanpassingen van andere HAT-handleidingen over.

Controleer de beschikbare interfaces:

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

Deze opdrachten tonen apparaatbestanden, adapters, GPIO-controllers, lijninformatie en de versie van de geïnstalleerde GPIO-tool. **`i2cdetect -l` vermeldt adapters zonder apparaatadressen te scannen.** Een bestand zoals `/dev/spidev0.0` bewijst dat een SPI-interface beschikbaar is, niet dat een werkende concentrator communiceert. [Handleiding van i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), [GPIO-richtlijnen van Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### Houd rekening met GPIO-versies

**Kopieer geen globale GPIO-nummers van een andere machine.** Oude scripts schrijven via `/sys/class/gpio`, een interface die de kernel als verouderd documenteert. Nieuwe gebruikersprogramma's horen de GPIO-character-device-interface te gebruiken met de juiste controller en lijnoffset. [Linux GPIO-documentatie](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

Bekijk ook `gpioset --help` voordat je een script aanpast. Versie 1 en versie 2 verschillen in syntaxis en procesgedrag. De huidige tool houdt aangevraagde lijnen standaard vast. De overdraagbare interface garandeert hun toestand niet nadat het proces stopt. [Documentatie van libgpiod gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi documenteert gedrag waarbij uitgangen in de kernel actief blijven en geeft opties om dat te wijzigen. Noteer de feitelijke kernelconfiguratie in plaats van aan te nemen dat elk Linux-systeem hetzelfde werkt. Andere nummering of een nieuwere GPIO-tool lost een verkeerde elektrische indeling niet op. [GPIO-gebruiksgids van Raspberry Pi](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## De gebruikers-led testen

Controleer eerst dat GPIO22 met de led verbonden is en verwijder conflicterende gebruikers van die GPIO. Pas daarna de opstartconfiguratie aan:

```bash
sudoedit /boot/firmware/config.txt
```

Moderne Raspberry Pi OS-versies koppelen de opstartconfiguratie aan **`/boot/firmware/config.txt`**. Oudere images gebruiken `/boot/config.txt`, het pad uit het artikel van 2023. Maak een back-up van het actieve bestand voordat je het wijzigt. [Documentatie van Raspberry Pi config.txt](https://www.raspberrypi.com/documentation/computers/config_txt.html)

Voeg de led-overlay toe onder een toepasselijk gedeelte voor je Pi, zoals `[all]`:

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

De parameter **`gpio`** gebruikt BCM-nummering. **`label`** geeft het Linux-ledapparaat een naam en **`trigger=heartbeat`** kiest de kernel-heartbeattrigger. Clockwork Bird meldt deze toewijzing voor de M1 en de overlayreferentie van Raspberry Pi documenteert de parameters. [Oorspronkelijke ledwaarneming](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), [Referentie voor de gpio-led-overlay](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

Controleer na de herstart de geregistreerde led:

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

Het verwachte resultaat is een `lorawan`-ledvermelding met `heartbeat` tussen vierkante haken. Een knipperende led toont deze GPIO-/driverroute aan. Ze rapporteert geen succesvolle LoRaWAN-registratie, radio-ontvangst of Helium-status.

## I2C-apparaten onderzoeken

**Een I2C-adres is een aanwijzing, geen apparaatidentiteit.** Clockwork Bird zag antwoorden op `0x60` en `0x39` en las daarna ATECC608-informatie via de cryptobibliotheek. De identificatie van de temperatuursensor bleef in het oorspronkelijke artikel onzeker.

Begin met de adapterlijst uit het vorige onderdeel. Brede `i2cdetect`-scans sturen testtransacties in plaats van passief verkeer te observeren. De upstreamhandleiding waarschuwt voor verstoring. Scan een draaiende gateway of onbekende aangesloten apparaten niet routinematig. [Probeergedrag van i2c-tools](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| Waarneming | Onderbouwde conclusie | Open vraag |
|---|---|---|
| **Antwoord op `0x60`** | Iets bevestigde de testaanvraag | Is dit het verwachte beveiligingselement? |
| **Antwoord op `0x39`** | Iets bevestigde de testaanvraag | Welk onderdeel en welke revisie antwoordden? |
| **`UU` in een scan** | Een driver bezit het adres, daarom is scannen overgeslagen | Welke driver bezit het? |
| **Geen antwoord** | De testaanvraag kreeg geen bevestiging | Voeding, bus, eigenaarschap of apparaatprotocol? |

### Sterkere aanwijzing voor de temperatuursensor

**STTS751 is op basis van de bronnen een kandidaat voor `0x39`.** De header van Semtechs temperatuursensordriver koppelt `0x39` expliciet aan `STTS751-0DP3F`. Dit versterkt de oorspronkelijke hypothese, maar identificeert niet elk printplaatonderdeel op dit adres. [Header van de Semtech STTS751-driver](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

Nadat je een compatibel onderdeel hebt vastgesteld en zeker weet dat geen ander proces het gebruikt, lees je met deze opdrachten de identificatieregisters:

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

Hier selecteert **`1`** de geverifieerde bus, **`0x39`** het apparaat en vraagt **`b`** een SMBus-bytegegevenslezing aan. Bij een STTS751-0 is de gedocumenteerde product-ID op `0xFD` `0x00` en de fabrikants-ID op `0xFE` `0x53`. Deze transacties selecteren registeradressen, maar schrijven geen configuratiewaarden. [STTS751-datasheet, registerkaart en identificatieregisters](https://www.st.com/resource/en/datasheet/stts751.pdf)

Vergelijk de waarden met de chipmarkering en documentatie. Een overeenkomend paar ondersteunt de identificatie. Bij een fout controleer je eerst bus en eigenaarschap voordat je de hardwareconfiguratie wijzigt. De sensor meet zijn lokale temperatuur, iets anders dan de CPU-temperatuur van de Pi.

## Het beveiligingselement inspecteren

**De ATECC608 is een afzonderlijk onderdeel voor authenticatie.** Behandel de configuratie, het serienummer, de openbare sleutel en beschermde sleutelgegevens als verschillende concepten. Een leesbare openbare sleutel onthult de bijbehorende privésleutel niet.

Microchips **CryptoAuthLib** biedt de apparaatinterface. De repository **cryptoauthtools** bevat voorbeelden die de bibliotheek gebruiken. Bereid volgens de instructies van die projecten de native bibliotheek en Python-bindingen voor je doelsysteem voor voordat je een voorbeeld uitvoert. Een niet-gerelateerd Python-pakket installeren of één script kopiëren levert nog geen werkende I2C-backend op. [Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

Voer vanuit een voorbereide map `cryptoauthtools/python/examples` de inspectieopdracht uit het oorspronkelijke artikel uit:

```bash
sudo python3 info.py -i i2c
```

Het argument **`-i i2c`** selecteert de interface. Gebruik in een virtuele omgeving de expliciete Python-interpreter daarvan en controleer of deze de bijbehorende native bibliotheek vindt. `sudo python3` kiest bij veel installaties de systeeminterpreter, wat enkele importfouten verklaart.

De geïnspecteerde `info.py` leest revisiegegevens, serienummer, configuratie en vergrendelingsstatus. Bij een vergrendelde gegevenszone probeert het script de openbare sleutel uit slot 0 op te halen. Het voert de provisioningreeks uit het voorbeeld niet uit. Een mislukte uitlezing van de openbare sleutel uit slot 0 bewijst op zichzelf geen defect apparaat. [Broncode van Microchips info.py](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| Uitvoer of bewerking | Betekenis |
|---|---|
| **Configuratie vergrendeld** | Configuratiebeperkingen gelden |
| **Gegevenszone vergrendeld** | Interpreteer toegang aan de hand van de ingestelde slotbeleidsregels |
| **Openbare sleutel getoond** | Openbare informatie is opgehaald, geen export van een privésleutel |
| **`config.py` uitvoeren** | Provisioningvoorbeeld met configuratie-, vergrendelings- en sleutelbewerkingen |

**Voer `config.py` niet uit om een inspectiefout te herstellen.** De bron bevat configuratieschrijfbewerkingen, oproepen om zones te vergrendelen en sleutelgeneratie. De standaardroute voor sleutelgeneratie is ook van belang op een reeds geconfigureerd apparaat. [Broncode van Microchips config.py](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

De provisioningprofielen van Microchip laten zien waarom een vergrendelde gegevenszone niet betekent dat elk slot dezelfde toegangsrechten heeft. Die profielen bewijzen niet wat de exacte M1-configuratie is. Behoud de bestaande apparaatconfiguratie en raadpleeg de documentatie van het juiste onderdeel voordat je hergebruik van sleutels plant. [Geheugen- en slottoegangsbeleid van Microchip](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## Onzekerheden over ventilator en knop behandelen

**Een ventilatoraansluiting met drie pinnen zegt niets over spanning, polariteit of regeling.** Fotografeer de pinnummering en lees het label van de ventilator. Stel voeding en besturingssignalen vast voordat je een vervanging aansluit of een GPIO-overlay kiest.

Ook is de GPIO van de knop in het oorspronkelijke onderzoek onbekend. Zoek een driver of configuratie die bij je printplaatrevisie hoort en controleer daarna de verbinding met uitgeschakelde voeding. Wijs niet elke ogenschijnlijk ongebruikte GPIO als uitgang toe om de knop te vinden.

| Randapparaat | Te verzamelen bewijs | Acceptatievoorwaarde |
|---|---|---|
| **Ventilatorvoeding** | Nominale waarde van de ventilator, massa en voeding op de connector | Gemeten voeding komt overeen met de specificatie van de ventilator |
| **Ventilatorregeling** | Driver/configuratie of getraceerd regelcircuit | Gedrag bij opstarten en hoge temperatuur is vastgelegd |
| **Gebruikersknop** | Bedrading van contacten, GPIO-toewijzing, ingangspolariteit | Eén bewuste druk veroorzaakt het verwachte evenement |

Een nieuwe OS-installatie herstelt niet automatisch het koelbeleid van het oorspronkelijke apparaat. Houd tijdens de eerste langdurige test de ventilatorwerking en temperaturen samen in de gaten. Behoud de luchtstroom in de behuizing en stop de test als de assemblage onvoldoende koelt.

## Kies een gatewaystack

**Scheid ondersteuning voor de printplaat van het serverprotocol.** Een compatibele LoRaWAN-server herstelt geen verkeerde resetprocedure of RF-kalibratie. Kies eerst software die de concentrator, bedrading van de drager, het OS en de regionale configuratie ondersteunt.

| Softwarepad | Geschikte rol | Controle voor uitrol |
|---|---|---|
| **Semtech SX1302 HAL** | Opstarten op bronniveau en diagnostische tools | Resetprocedure van de printplaat en moduleconfiguratie |
| **LoRa Basics Station** | Geauthenticeerde gatewayverbinding met een server | Werkende printplaatintegratie en servergegevens |
| **ChirpStack Concentratord** | Afzonderlijke concentratordienst | Ondersteund model, kalibratie en GPIO-indeling |

ChirpStack vermeldt het SPI-model **`seeed_wm1302`**. Dit is bewijs voor moduleondersteuning, geen garantie voor een complete M1-image of ondersteuning van elke M1-revisie. Behandel de aparte installatie-instructies voor SenseCAP M2 niet als M1-firmware-instructies. [Hardwareondersteuning van ChirpStack](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html), [Seeed-installatiedoel van ChirpStack](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

Voor The Things Stack beveelt de documentatie **LoRa Basics Station** aan boven de oudere Semtech UDP-forwarder. Station biedt TLS en tokenauthenticatie plus centrale configuratiefuncties. UDP-voorbeelden zijn nuttig om pakketforwarding te begrijpen, maar hun serveradresinstellingen bieden die bescherming niet. [UDP-richtlijnen van The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [Documentatie van LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### Upstreamtools voorbereiden

Bouw op de doel-Pi in een nieuwe werkmap:

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

Bewaar de commit-ID bij je bouwuitvoer. Een geslaagde build toont compilercompatibiliteit, maar de radio vereist nog steeds een geverifieerde resetimplementatie en juiste configuratie. De documentatie van Semtech beschrijft de functie van de HAL en hulpprogramma's. [Bouw- en tooldocumentatie van de SX1302 HAL](https://github.com/Lora-net/sx1302_hal)

Controleer het resetbestand voordat je tools voor hardwaretoegang uitvoert:

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

Kopieer dit bestand niet ongewijzigd naar de runtime-map. Semtech documenteert automatisch gebruik van het resetscript door programma's voor hardwaretoegang, waaronder identificatietools. Controleer iedere toegewezen pin, signaalrichting, GPIO-API en toestand bij starten en afsluiten.

Volg na verificatie van de printplaat de instructies van de gekozen stack om de concentrator-EUI te lezen en de gateway te registreren. Behoud de kalibratie en RF-instellingen van de module wanneer je de serverconfiguratie toevoegt. In Semtech UDP-configuratie staat `gateway_ID` voor de EUI. De Gateway ID in de console van The Things Stack is de leesbare registratie-ID. [Gatewayconfiguratie van The Things Stack](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## Sensorgegevensoverdracht bewijzen

**Gebruik opeenvolgend bewijs om de eerste falende laag te vinden.** Een gateway met de status online heeft verbinding met een server. Je acceptatietest vereist ook een bekende sensor, een passend frequentieplan en een gedecodeerde payload van de toepassing.

De volgende volgorde is een voorgesteld testplan, geen gemeten M1-resultaat:

| Controlepunt | Bewijs om op te slaan | Betekenis |
|---|---|---|
| **Host gereed** | OS, kernel, voeding en interface-inventaris | Linux-voorbereiding is afgerond |
| **Concentrator reageert** | EUI en geslaagd initialisatielog | Communicatie tussen host en concentrator werkt |
| **Radio ontvangt** | Verwacht sensorpakket en ontvangstmetadata | Het ingestelde ontvangstpad werkt |
| **Server accepteert** | Gatewaygebeurtenis gekoppeld aan de sensor | Doorsturen en serverroutering werken |
| **Toepassing decodeert** | Verwachte meting en tijdstempel | Het toepassingspad werkt |
| **Herstel na herstart** | Dezelfde controles na herstart | De opstartconfiguratie is herhaalbaar |

Controleer bij een **OTAA**-sensor ook de activeringsuitwisseling en daaropvolgende uplink. OTAA betekent activering via de ether, de aanmeldprocedure die een sessie opzet. Een ontvangen aanmeldverzoek bewijst geen geslaagde aanmelding of downlinkpad. [Activeringsdocumentatie van The Things Stack](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**Diagnosevoorbeeld:** de gateway verbindt met de server en meldt zijn EUI, maar je sensor verschijnt niet. Controleer eerst de zendconfiguratie van de sensor, gekozen ontvangstkanalen, antennepad en radiologs. De ATECC608 opnieuw programmeren verhelpt in dit scenario het ontbrekende bewijs niet.

**Tweede diagnose:** een sensorpakket verschijnt lokaal, maar bereikt de toepassing niet. Vergelijk de pakkettijd met gateway- en servergebeurtenissen en controleer daarna routering, apparaatregistratie en decodering. Een RF-pakket in een log is onvoldoende reden om de decoder van de payload de schuld te geven zolang de server het evenement niet heeft geaccepteerd.

## Problemen per symptoom oplossen

| Symptoom | Controleer eerst | Volgende actie |
|---|---|---|
| **Geen SPI-apparaatbestand** | Actieve opstartconfiguratie en interface-instellingen | Schakel de bedoelde interface in en start opnieuw op |
| **SPI bestaat, radio werkt niet** | Voeding, plaatsing, resetreeks en chipselect | Verifieer het elektrische pad voordat je serverinstellingen wijzigt |
| **GPIO-exportfout** | Aannames over oude sysfs en geïnstalleerde kernel | Gebruik een gecontroleerde implementatie voor de GPIO-API |
| **GPIO al in gebruik** | Gebruiker die `gpioinfo` toont | Los eigenaarschap op voordat je opnieuw probeert |
| **Led werkt niet na installatie** | Toepassing van overlay en conflicten op GPIO22 | Controleer geregistreerde ledapparaten en resetscript |
| **I2C-apparaat ontbreekt** | Busnummer, voeding en bestaand eigenaarschap | Onderzoek dit zonder herhaalde brede scans |
| **Import van cryptobibliotheek mislukt** | Interpreter, bindingen en pad naar native bibliotheek | Herstel de softwareomgeving |
| **Uitlezen openbare sleutel mislukt** | Slotbeleid en eerdere succesvolle uitlezingen | Controleer de configuratie zonder provisioning |
| **Ventilator draait niet** | Geverifieerde voeding en koelregeling | Herstel de koeling voor langdurige tests |
| **Uplinks komen aan, aanmelding mislukt** | Downlinkpad en regionale/apparaatinstellingen | Volg het aanmeldantwoord en de ontvangstvensters |

Behandel iedere correctie als één experiment. Bewaar de vorige configuratie, wijzig één variabele, herhaal dezelfde controle en noteer of het verwachte bewijs verscheen.

## Maak een hardwareverslag

Gebruik deze sjabloon voor een reproduceerbare overdracht:

```text
Carrier revision and photographs:
Concentrator model, interface and RF band:
Host model / OS / kernel / GPIO tool version:
Supply / antenna / cooling arrangement:
Verified pin mapping and evidence:
Unresolved nets and excluded features:
Software repository and commit:
Reset implementation and GPIO ownership:
Gateway EUI / server / frequency plan:
Sensor activation and decoded uplink evidence:
Reboot recovery result:
Original-card location and rollback procedure:
```

**Beslisoefening:** je kunt een goedkope losse drager zonder modulelabel kopen of een duurdere assemblage met leesbare labels en gedocumenteerde werking. Bepaal welke bij je project past nadat je de ontbrekende Pi, concentrator, antenne, voeding en verificatietijd aan de vergelijking hebt toegevoegd. De betere keuze volgt uit de totale kosten en het vereiste bewijs voor de beoogde dienst, niet alleen uit de geadverteerde prijs van de drager.

**Verwachte redenering:** een leerproject kan onopgeloste bedrading verdragen als je meetapparatuur en tijd hebt. Een gateway voor operationele sensoren vereist herhaalbare starts, koeling, softwareondersteuning en aangetoonde gegevensoverdracht. Noteer welke onopgeloste voorwaarde je uitrol zou stoppen.

## Volgende stappen

Begin met het hardwareverslag en los de verschillen tussen resetscripts op. Start daarna één bekende sensor op en bewaar bewijs tot en met decodering in de toepassing voordat je meer apparaten toevoegt.

**Acceptatieverslag:** bewaar de printplaatrevisie, het modulelabel, de radioband, voedingsmeting, actieve SPI-interface, GPIO-lijnnamen, resetreeks, concentratorlog, serververbinding en één gedecodeerde uplink. Markeer elke waarde als waargenomen, gedocumenteerd of nog aangenomen. Een gestart proces bewijst geen RF-prestaties of gegevensoverdracht naar de toepassing.

Als je meshberichten wilt versturen, vergelijk dan eerst de protocolrollen in onze [gids voor Meshtastic, MeshCore en Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/). Gebruik van dezelfde LoRa-radiotechniek bewijst geen firmwarecompatibiliteit. Raadpleeg voor een berichtentoepassing de [hardwaredocumentatie van MeshtasticD](https://meshtastic.org/docs/meshtasticd/) en behandel deze LoRaWAN-procedure niet als een conversie naar Meshtastic.

## Bronnen en beeldcredits

Onderzoek gecontroleerd op 12 september 2026. Ongedateerde documentatie- en repositorylinks verwijzen naar de versies die voor dit artikel zijn bekeken. Lokale afbeeldingen behouden hun oorspronkelijke labels en toegeschreven herkomst.

| Uitgever | Bron en datum |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/), 2023-05-03. Foto van de printplaat, geannoteerde header en gereproduceerd blokschema van de fabrikant |
| **Seeed Studio / SenseCAP** | [M1-overzicht en specificaties](https://www.sensecapmx.com/docs/sensecap-m1/overview/), ongedateerd. Oorspronkelijke toeschrijving van het blokschema |
| **Seeed Studio** | [WM1302-documentatie en modulepinout](https://github.com/seeed-lora/WM1302-doc), repository |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal), inclusief gekoppelde broncode voor resetscript en temperatuursensordriver |
| **Raspberry Pi** | [Opstartconfiguratie](https://www.raspberrypi.com/documentation/computers/config_txt.html), [GPIO-gebruiksgids](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices) en [overlayreferentie](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [Verouderde GPIO-sysfs-interface](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html) en [handleiding voor gpioset](https://libgpiod.readthedocs.io/en/master/gpioset.html), die laatste gedateerd augustus 2026 |
| **i2c-tools** | [Handleiding voor i2cdetect](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8), broncode v4.3 |
| **STMicroelectronics** | [STTS751-datasheet](https://www.st.com/resource/en/datasheet/stts751.pdf), revisie 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib), [cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools) en [documentatie over slottoegangsbeleid](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Hardwareondersteuning voor Concentratord](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html) en [Seeed-installatiedoel](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDP-forwarder](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/), [LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) en [apparaatactivering](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticD-documentatie](https://meshtastic.org/docs/meshtasticd/), ongedateerd |
