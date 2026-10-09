---
title: "Com descarregar un ISO net de Windows i instal·lar des de zero"
date: 2023-02-20
toc: true
draft: false
description: Aprèn a descarregar un fitxer ISO net de Windows i instal·lar Windows des de zero amb aquesta guia pas a pas.
tags:
- Windows 10
- Windows 11
- Fitxer ISO
- Instal·lació neta
- Eina de creació de mitjans
- USB d'arrencada
- Mitjà d'instal·lació
- BIOS
- Firmware UEFI
- Instal·lació personalitzada
- Clau de producte
- Sistema de 64 bits
- Sistema de 32 bits
- Rufus
- ImgBurn
- CDBurnerXP
- HashCalc
- Utilitat de comprovació de sumes MD5 i SHA
- Tipus de sistema
cover: /img/cover/A_cartoon_image_of_a_person_holding_a_USB_stick.webp
coverAlt: Una imatge de dibuixos animats d'una persona que sosté una memòria USB amb un logotip de Windows i una marca de verificació, davant d'una pantalla d'ordinador amb un logotip de Windows.
coverCaption: ''
lastmod: 2026-10-08
---

**Com descarregar un ISO net de Windows 10 o 11 i instal·lar Windows des de zero**

Si planeges instal·lar Windows en un ordinador nou o vols fer una instal·lació neta per eliminar qualsevol problema que estiguis experimentant, descarregar un fitxer ISO net de Windows és un primer pas essencial. En aquest article, cobrirem els passos per descarregar un ISO net de Windows 10 o 11 i t'orientarem durant el procés d'instal·lació.

## Part 1: Descarregar un fitxer ISO net de Windows

### Pas 1: Comprova el tipus de sistema

El primer pas per descarregar un ISO net de Windows és comprovar el tipus de sistema. Necessites saber si tens un sistema de 32 bits o de 64 bits, ja que això determinarà quin fitxer ISO descarregar.

Per comprovar el tipus de sistema a Windows 10, segueix aquests passos:

1. Obre el menú Inici i fes clic a "Configuració."
2. Fes clic a "Sistema."
3. Fes clic a "Quant a."
4. A sota de "Especificacions del dispositiu", comprova l'entrada "Tipus de sistema".

Si tens un sistema de 32 bits, hauràs de descarregar la versió de Windows de 32 bits. Si tens un sistema de 64 bits, pots descarregar la versió de 32 bits o de 64 bits, però recomanem la versió de 64 bits per a un millor rendiment.

### Pas 2: Descarrega l'Eina de creació de mitjans

Per descarregar un ISO net de Windows, utilitzarem l'Eina de creació de mitjans de Microsoft. La pots descarregar directament des del lloc web de Microsoft seguint aquests passos:

1. Ves a la [pàgina de descàrrega de Windows 10 de Microsoft](https://www.microsoft.com/en-us/software-download/windows10).
2. Desplaça't fins a la secció "Crear mitjà d'instal·lació de Windows 10" i fes clic a "Descarrega l'eina ara."
3. Desa el fitxer al teu ordinador.

Si vols descarregar Windows 11, el procés és similar. Pots descarregar l'Eina de creació de mitjans des de la [pàgina de descàrrega de Windows 11 de Microsoft](https://www.microsoft.com/en-us/software-download/windows11) i seguir els mateixos passos.

### Pas 3: Executa l'Eina de creació de mitjans

Un cop hagis descarregat l'Eina de creació de mitjans, executa-la al teu ordinador. Se't preguntarà si vols actualitzar el teu PC actual o crear un mitjà d'instal·lació. Tria l'opció "Crear mitjà d'instal·lació" i fes clic a "Següent."

### Pas 4: Tria l'idioma, l'edició i l'arquitectura

El següent pas és triar l'idioma, l'edició i l'arquitectura. Pots deixar l'opció d'idioma configurada al teu idioma actual o triar un altre idioma si ho prefereixes.

Per a l'edició, tria la versió de Windows que vols instal·lar. Se't donarà l'opció entre Windows 10 Home i Windows 10 Pro, o Windows 11 Home i Windows 11 Pro.

Per a l'arquitectura, selecciona el tipus de sistema que vas determinar al Pas 1. Si tens un sistema de 64 bits, recomanem seleccionar la versió de 64 bits per a un millor rendiment.

### Pas 5: Tria el tipus de mitjà

El següent pas és triar el tipus de mitjà. Pots crear una unitat USB d'arrencada o descarregar un fitxer ISO.

Si tries crear una unitat USB d'arrencada, necessitaràs una unitat USB amb almenys 8 GB d'espai. L'Eina de creació de mitjans formatarà automàticament la unitat i copiarà els fitxers necessaris.

Si tries descarregar un fitxer ISO, l'Eina de creació de mitjans descarregarà el fitxer i el desarà al teu ordinador. Després podràs utilitzar una eina de tercers per crear una unitat USB d'arrencada o gravar l'ISO en un DVD.

### Pas 6: Descarrega el fitxer ISO

Si vas triar descarregar un fitxer ISO, l'Eina de creació de mitjans començarà a descarregar-lo. Això pot trigar una estona, depenent de la velocitat de la teva connexió a internet.

Un cop finalitzada la descàrrega, l'eina verificarà el fitxer per assegurar-se que és un ISO net.

### Pas 7: Verifica el fitxer ISO

Verificar el fitxer ISO és un pas essencial per assegurar que el fitxer que has descarregat és net i no ha estat modificat. Per verificar el fitxer, pots utilitzar una eina com [HashCalc](https://www.slavasoft.com/hashcalc/) o [Utilitat de comprovació de sumes MD5 i SHA](https://raylin.wordpress.com/downloads/md5-sha-1-checksum-utility/).

Un cop hagis descarregat i instal·lat l'eina de verificació, obre-la i selecciona el fitxer ISO que vas descarregar. L'eina calcularà el valor hash del fitxer i el compararà amb el valor hash proporcionat per Microsoft a la pàgina de descàrrega de Windows. Si els valors hash coincideixen, el fitxer ISO és net i es pot utilitzar per instal·lar Windows.

## Part 2: Instal·lar Windows des d'un ISO net

Un cop tinguis un fitxer ISO net de Windows, pots utilitzar-lo per instal·lar Windows al teu ordinador. Aquí tens els passos a seguir:

### Pas 1: Crea el mitjà d'instal·lació

Abans de poder instal·lar Windows des del fitxer ISO, necessites crear un mitjà d'instal·lació. Pots fer-ho utilitzant una unitat USB d'arrencada o un DVD.

Per crear una unitat USB d'arrencada, pots utilitzar una eina com [Rufus](https://rufus.ie/) o [Eina de descàrrega USB/DVD de Windows](https://www.microsoft.com/en-us/download/windows-usb-dvd-download-tool). Simplement connecta la unitat USB, obre l'eina i segueix les instruccions per crear la unitat d'arrencada.

Si prefereixes utilitzar un DVD, pots utilitzar una eina com [ImgBurn](https://www.imgburn.com/) o [CDBurnerXP](https://cdburnerxp.se/en/home). Insereix el DVD, obre l'eina i segueix les instruccions per gravar el fitxer ISO al DVD.

### Pas 2: Arrenca des del mitjà d'instal·lació

Un cop hagis creat el mitjà d'instal·lació, necessites arrencar l'ordinador des d'aquest mitjà. Per fer-ho, pot ser necessari canviar l'ordre d'arrencada al BIOS o firmware UEFI del teu ordinador.

Per entrar al BIOS o firmware UEFI, reinicia l'ordinador i prem la tecla que apareix a la pantalla. Normalment és F2, F10 o Supr. Un cop dins del BIOS o firmware UEFI, busca el menú "Arrencada" i canvia l'ordre d'arrencada perquè el teu mitjà d'instal·lació estigui al principi de la llista.

### Pas 3: Instal·la Windows

Un cop l'ordinador hagi arrencat des del mitjà d'instal·lació, veuràs la pantalla de configuració de Windows. Segueix les instruccions per instal·lar Windows al teu ordinador.

Se't demanarà que seleccionis l'idioma, la zona horària i la distribució del teclat. Després se't demanarà que introdueixis la clau de producte. Si no tens clau de producte, pots triar l'opció "No tinc clau de producte" i continuar amb la instal·lació. Podràs activar Windows més endavant un cop instal·lat.

A continuació, se't demanarà que seleccionis el tipus d'instal·lació. Tria l'opció "Personalitzada" per fer una instal·lació neta.

A continuació se't demanarà que seleccionis la partició on vols instal·lar Windows. Si estàs instal·lant Windows en un ordinador nou o en un ordinador amb un disc dur buit, veuràs espai no assignat. Selecciona l'espai no assignat i fes clic a "Següent" per crear una nova partició i instal·lar Windows.

Un cop finalitzada la instal·lació, Windows es reiniciarà i se't demanarà que configuris el teu compte d'usuari.

## Conclusió

Descarregar una ISO neta de Windows i instal·lar Windows des de zero pot semblar complicat, però és un procés senzill que qualsevol pot fer. Seguint els passos d'aquesta guia, pots assegurar-te que tens un Windows net
