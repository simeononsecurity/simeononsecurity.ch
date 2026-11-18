---
title: "Descobreix el món de la pirateria de maquinari"
date: 2023-07-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Coneix la pirateria de maquinari i les eines i tècniques essencials que utilitzen els intrusos de maquinari."
genre: ["Tecnologia i pirateria informàtica", "Ciberseguretat", "Pirateria de maquinari", "Eines de pirateria", "Electrònica", "Internet de les coses", "Pirateria feta per compte propi", "Enginyeria inversa", "Microcontroladors", "Pirateria sense fil"]
tags: ["intrús de maquinari", "pirateria de maquinari", "maquinari per a intrusos", "eines de pirateria de maquinari", "eines de pirateria", "maquinari per a la pirateria", "depurador JTAG", "analitzador lògic", "Bus Pirate", "ràdio definida per programari", "SDR", "soldador", "microcontroladors", "Arduino", "Raspberry Pi", "ESP8266", "enginyeria inversa", "pirateria sense fil", "electrònica", "ciberseguretat", "pirateria feta per compte propi", "HackRF", "RTL-SDR", "OpenOCD", "J-Link", "Saleae Logic", "Sigrok", "tecnologia", "seguretat"]
cover: "/img/cover/A_symbolic_art_style_depicting_a_hacker_surrou.webp"
coverAlt: "Una imatge simbòlica d’un hacker envoltat de dispositius electrònics, que representa el món de la pirateria de maquinari."
coverCaption: "Obre noves possibilitats: el món de la pirateria de maquinari."
---

## Introducció

La tecnologia és cada vegada més complexa i els dispositius connectats són més habituals. Per això, la pirateria informàtica també s’ha estès del programari al maquinari. La pirateria de maquinari consisteix a manipular o modificar dispositius electrònics per obtenir accés no autoritzat, extreure informació o controlar-ne les funcions. En aquest article explorarem el [maquinari per a intrusos](https://simeononsecurity.com/recommendations/hacker_hardware/) i les eines essencials que fan servir els [intrusos de maquinari](https://simeononsecurity.com/recommendations/hacker_hardware/).

## L’auge de la pirateria de maquinari

En els darrers anys, la pirateria de maquinari ha rebut molta atenció perquè cada vegada hi ha més dispositius connectats i exposats a bretxes de seguretat. Aquesta pràctica manipula components electrònics com ara plaques de circuits, microcontroladors, sensors i actuadors per explotar vulnerabilitats i obtenir accés no autoritzat als sistemes.

Les vulnerabilitats de programari es poden corregir amb relativa facilitat, però les de maquinari sovint són més difícils de solucionar. La pirateria de maquinari permet manipular físicament els dispositius per extreure informació sensible, injectar codi maliciós o controlar-ne el funcionament. Això crea riscos importants per a les persones, les organitzacions i fins i tot les infraestructures crítiques.

## Eines essencials per a la pirateria de maquinari

### 1. Depurador JTAG

Un depurador JTAG (Joint Test Action Group) és una eina física que permet accedir als circuits digitals dels dispositius electrònics i manipular-los. Proporciona una interfície estandarditzada per provar i depurar circuits integrats, cosa que la converteix en una eina potent per a la pirateria de maquinari. Es pot utilitzar per eludir mesures de seguretat, extreure firmware o modificar el comportament del dispositiu.

{{< youtube id="_FSM_10JXsM" >}}

Alguns depuradors JTAG populars són:

- [OpenOCD](https://github.com/sysprogs/openocd)
- [J-Link](https://www.segger.com/products/debug-probes/j-link/)

### 2. Analitzador lògic

Un analitzador lògic captura i analitza senyals digitals en sistemes electrònics. Permet observar i entendre el comportament dels circuits digitals d’un dispositiu, identificar vulnerabilitats i fer enginyeria inversa del maquinari. L’anàlisi dels senyals pot ajudar a extreure claus de xifratge, identificar protocols de comunicació i trobar portes del darrere al sistema.

{{< youtube id="u1DYs2I-_lU" >}}

Alguns analitzadors lògics populars entre els intrusos de maquinari són:

- [Saleae Logic](https://www.saleae.com/)
- [Sigrok](https://sigrok.org/)

### 3. Bus Pirate

Bus Pirate és una eina versàtil que permet connectar-se a diversos busos de comunicació electrònica, com ara I2C, SPI i UART. Fa de pont entre l’ordinador i el dispositiu objectiu, de manera que es poden llegir i escriure dades directament al bus de comunicació. És útil per interceptar comunicacions, injectar dades o explorar l’interior del dispositiu.

{{< youtube id="lP8vMvBu3Bg" >}}

El lloc web oficial de Bus Pirate és [aquí](http://dangerousprototypes.com/docs/Bus_Pirate).

### 4. Ràdio definida per programari (SDR)

Una ràdio definida per programari (SDR) és un sistema de comunicació per ràdio les funcions del qual es defineixen amb programari, en comptes de dependre de components de maquinari tradicionals. Els intrusos poden utilitzar SDR per interceptar, analitzar i manipular comunicacions sense fil. Són especialment útils per provar dispositius controlats per ràdio, sistemes de claus sense fil i altres protocols sense fil.

{{< youtube id="nB6XQSEFwVA" >}}

Algunes eines SDR populars per a la pirateria de maquinari són:

- [HackRF](https://amzn.to/40aBO1F)
- [RTL-SDR](https://amzn.to/3Mh9HrP)

### 5. Soldador i accessoris

Soldar és una habilitat essencial per als intrusos de maquinari, perquè permet modificar o reparar circuits electrònics. Un soldador escalfa i fon l’estany per crear connexions elèctriques entre components. Per als projectes de pirateria de maquinari també calen accessoris com ara [fil d’estany](https://amzn.to/46FrAZu), [flux](https://amzn.to/3FucA4H) i [eines per dessoldar](https://amzn.to/3Sejnau).

{{< youtube id="R2sPDQeGlj8" >}}

Recomanem aquests dos soldadors:
- [Estació de soldadura digital Merece](https://amzn.to/46zZVct)
- [Soldador intel·ligent portàtil PINECIL](https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/)

### 6. Microcontroladors i plaques de desenvolupament

Els microcontroladors són dispositius petits i programables que permeten crear eines pròpies de pirateria de maquinari o modificar dispositius existents. Ofereixen una plataforma flexible per experimentar amb diverses tècniques. Alguns microcontroladors i plaques de desenvolupament populars entre els intrusos de maquinari són [Arduino](https://amzn.to/476dh03), [Raspberry Pi](https://amzn.to/3Fw1Ann), [ESP8266](https://amzn.to/3s86pAn) i [ESP32](https://amzn.to/3Ftyxkz).

{{< youtube id="RmD7UgKvUnY" >}}

## Conclusió

La pirateria de maquinari planteja reptes de seguretat importants en el món connectat actual. A mesura que avança la tecnologia, convé conèixer les eines i tècniques que utilitzen els intrusos per comprometre el maquinari. Aquest article ha presentat eines essencials com ara depuradors JTAG, analitzadors lògics, Bus Pirate, SDR, equips de soldadura i microcontroladors. Entendre aquestes eines ajuda les persones i les organitzacions a protegir millor els seus sistemes i reduir els riscos potencials.

## Referències

- [OpenOCD - depurador de circuits integrats](https://github.com/sysprogs/openocd)
- [SEGGER - J-Link](https://www.segger.com/products/debug-probes/j-link/)
- [Saleae Logic](https://www.saleae.com/)
- [Sigrok](https://sigrok.org/)
- [Bus Pirate](http://dangerousprototypes.com/docs/Bus_Pirate)
- [Great Scott Gadgets - HackRF](https://greatscottgadgets.com/hackrf/)
- [RTL-SDR](https://www.rtl-sdr.com/)
