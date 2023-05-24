---
title: "Actualització del firmware fora de línia per a Ubiquiti Unifi UDM Pro i UDM SE mitjançant SSH de línia d'ordres"
draft: false
toc: true
date: 2023-05-28
description: "Obteniu informació sobre com actualitzar el microprogramari d'Ubiquiti Unifi UDM Pro i UDM SE fora de línia mitjançant SSH de línia d'ordres per obtenir un rendiment i una seguretat òptims."
tags: ["Actualització del firmware Ubiquiti", "UDM Pro", "UDM SE", "actualització de firmware fora de línia", "línia d'ordres SSH", "gestió de la xarxa", "seguretat de la xarxa", "actualització del firmware", "Connexió SSH", "fitxer de firmware", "Controlador de xarxa UniFi", "reparació d'errors", "millores de rendiment", "pedaços de seguretat", "treball en xarxa", "dispositius de xarxa", "tecnologia", "gestió informàtica", "procés d'actualització del firmware", "optimització de la xarxa", "Actualització del firmware d'Ubiquiti Networks", "Actualització del firmware UDM Pro", "Actualització del firmware UDM SE", "procés d'actualització del firmware fora de línia", "Actualització del firmware SSH", "gestió de dispositius de xarxa", "actualitzacions de seguretat de la xarxa", "estratègies d'actualització del firmware", "gestió de firmware fora de línia", "optimització del rendiment de la xarxa", "gestió de pedaços de seguretat", "actualitzacions tecnològiques de xarxes"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Una il·lustració acolorida que representa un ordinador connectat a un encaminador mitjançant SSH que simbolitza el procés d'actualització del microprogramari fora de línia per als dispositius Ubiquiti Unifi UDM Pro i UDM SE."
coverCaption: ""
---

**Actualitzeu Ubiquiti Unifi UDM Pro i UDM SE fora de línia mitjançant SSH**

En el món de les xarxes, **Ubiquiti Networks** ha guanyat el reconeixement per les seves solucions innovadores. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** i **Unifi Dream Machine SE (UDM SE)** són dos productes populars que ofereixen funcions de gestió de xarxa completes. L'actualització del firmware d'aquests dispositius és crucial per garantir un rendiment i una seguretat òptims. En aquest article, explorarem com actualitzar el microprogramari de l'UDM Pro i l'UDM SE **fora de línia** mitjançant SSH de línia d'ordres.

______

## Per què actualitzar el firmware?

Les actualitzacions de microprogramari són essencials per a qualsevol dispositiu de xarxa, ja que sovint contenen correccions d'errors, millores de rendiment i pedaços de seguretat. Actualitzar regularment el microprogramari del vostre UDM Pro i UDM SE és crucial per garantir que la vostra xarxa es mantingui segura i funcioni sense problemes.

______

## Actualització del firmware fora de línia

L'actualització del microprogramari de l'UDM Pro i l'UDM SE es pot fer a través del **UniFi Dashboard**. Tanmateix, en alguns escenaris, és possible que una connexió a Internet no estigui disponible o no sigui desitjable. En aquests casos, una actualització fora de línia mitjançant SSH de línia d'ordres proporciona una solució alternativa.

______

## Preparant-se per a l'actualització fora de línia

Abans de continuar amb l'actualització fora de línia, assegureu-vos que teniu els requisits previs següents:

1. Un ordinador o dispositiu amb un client SSH instal·lat.
2. El fitxer de microprogramari més recent per al vostre UDM Pro o UDM SE. Podeu obtenir el fitxer de microprogramari des de [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) compte

______

## Establint la connexió SSH

Per actualitzar l'UDM Pro o l'UDM SE mitjançant SSH de línia d'ordres, seguiu aquests passos:

1. Assegureu-vos que el vostre ordinador o dispositiu estigui connectat a la mateixa xarxa que l'UDM Pro o l'UDM SE.
2. Obriu el vostre client SSH preferit i establiu una connexió SSH amb l'**UDM Pro o l'adreça IP d'UDM SE**. Per exemple, utilitzant el **client OpenSSH** a Linux o macOS, podeu utilitzar l'ordre següent:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Substituïu `<UDM_IP_ADDRESS>` amb l'adreça IP real del vostre UDM Pro o UDM SE.

3. Introduïu el **nom d'usuari** i la **contrasenya** quan se us demani. Les credencials predeterminades per als dispositius Ubiquiti solen ser `ubnt` tant per al nom d'usuari com per a la contrasenya.

______

## Actualització del firmware

Un cop hàgiu establert la connexió SSH, podeu continuar amb l'actualització del microprogramari:

1. Carregueu el fitxer de microprogramari a UDM Pro o UDM SE mitjançant **SCP (Copia segura)**. SCP permet la transferència segura de fitxers a través de SSH. Suposant que el fitxer del microprogramari es troba a la vostra màquina local, podeu utilitzar l'ordre següent:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Substituïu `<FIRMWARE_FILE_PATH>` amb el camí del fitxer de microprogramari a la vostra màquina local i `<UDM_IP_ADDRESS>` amb l'adreça IP del vostre UDM Pro o UDM SE.

2. Un cop carregat el fitxer del microprogramari, podeu iniciar el procés d'actualització del microprogramari. Executeu l'ordre següent:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. L'UDM Pro o l'UDM SE iniciaran el procés d'actualització del microprogramari. Això pot trigar uns quants minuts. **No interrompeu el procés** fins que s'hagi completat l'actualització.

4. Un cop finalitzada l'actualització, podeu verificar la versió del microprogramari iniciant sessió al controlador de xarxa UniFi o executant l'ordre següent:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Tingueu en compte que el procés anterior suposa que teniu el fitxer de microprogramari necessari per al vostre UDM Pro o UDM SE. Assegureu-vos que teniu el fitxer de microprogramari correcte per al vostre model i versió de dispositiu específics.

## Conclusió

L'actualització del microprogramari dels vostres dispositius Ubiquiti Unifi UDM Pro i UDM SE és un pas crucial per garantir un rendiment i una seguretat òptims. Tot i que el controlador de xarxa UniFi proporciona una manera còmoda d'actualitzar el microprogramari, realitzar una actualització fora de línia mitjançant SSH de línia d'ordres ofereix una solució viable quan no hi ha una connexió a Internet disponible o desitjable.

Seguint els passos descrits en aquest article, podeu actualitzar correctament el microprogramari dels vostres dispositius UDM Pro i UDM SE mitjançant SSH de línia d'ordres. Recordeu utilitzar sempre la darrera versió de microprogramari proporcionada per Ubiquiti Networks per aprofitar les correccions d'errors, les millores de rendiment i els pedaços de seguretat.

## Referències

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Pàgina oficial de descàrregues d'Ubiquiti per a fitxers de firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
