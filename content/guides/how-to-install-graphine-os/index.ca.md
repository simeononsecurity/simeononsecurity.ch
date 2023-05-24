---
title: "Guia definitiva: instal·lació de Graphene OS al vostre dispositiu Google Pixel"
draft: false
toc: true
date: 2023-05-21
description: "Obteniu informació sobre com instal·lar Graphene OS al vostre dispositiu Google Pixel per millorar la privadesa i la seguretat."
tags: ["Graphene OS", "Google Pixel", "privadesa", "seguretat", "Android", "dispositius mòbils", "sistema operatiu", "guia d'instal·lació", "ROM personalitzada", "centrat en la privadesa", "protecció de dades", "sistema operatiu segur", "codi obert", "seguretat del dispositiu", "funcions de privadesa", "dades personals", "privadesa mòbil", "privadesa de dades", "personalització del dispositiu", "tecnologia", "Instal·lació de píxels", "sistema operatiu centrat en la privadesa", "Instal·lació del sistema operatiu Graphene", "seguretat mòbil", "privadesa i seguretat", "Personalització del dispositiu Pixel", "millores de privadesa", "guia de protecció de dades", "sistema operatiu segur", "Funcions de privadesa de píxels", "privadesa de dades mòbils"]
cover: "/img/cover/A_colorful_cartoon_illustration_showcasing_a_Google_Pixel.png"
coverAlt: "Una il·lustració de dibuixos animats acolorits que mostra un dispositiu Google Pixel amb un escut que simbolitza funcions de privadesa i seguretat millorades."
coverCaption: ""
---

**Com instal·lar Graphene OS al vostre dispositiu Google Pixel**

Graphene OS és un sistema operatiu de codi obert centrat en la privadesa basat en la plataforma Android. Ofereix funcions de seguretat millorades i proteccions de privadesa, la qual cosa la converteix en una opció excel·lent per a persones preocupades per la privadesa i la seguretat de les dades. Si teniu un dispositiu Google Pixel i voleu canviar a Graphene OS, aquest article us guiarà pas a pas pel procés d'instal·lació.

## Requisits previs

Abans de començar el procés d'instal·lació, hi ha uns quants requisits previs que heu de complir:

1. **Feu una còpia de seguretat de les vostres dades**: la instal·lació de Graphene OS esborrarà totes les dades del vostre dispositiu. Assegureu-vos que heu fet una còpia de seguretat de tots els fitxers, fotos, contactes i altres dades importants en una ubicació segura.

2. **Desbloquegeu el carregador d'arrencada**: el carregador d'arrencada és un programari que inicialitza el sistema quan engegueu el dispositiu. Desbloquejar el carregador d'arrencada us permet instal·lar programari personalitzat com ara Graphene OS. Cada dispositiu Google Pixel té un procés específic per desbloquejar el carregador d'arrencada. Consulteu la documentació oficial del vostre model de dispositiu per saber com desbloquejar-lo.

- [Enabling OEM unlocking](https://grapheneos.org/install/cli#enabling-oem-unlocking)
- [How to unlock the Google Pixel 3 bootloader](https://www.androidauthority.com/unlock-pixel-3-bootloader-915961/)

3. **Carrega el teu dispositiu**: assegureu-vos que el vostre dispositiu tingui una càrrega de bateria suficient abans d'iniciar el procés d'instal·lació. Una bateria esgotada durant la instal·lació pot provocar errors o interrupcions.

## Instal·lant el sistema operatiu Graphene

Seguiu els passos següents per instal·lar Graphene OS al vostre dispositiu Google Pixel:

______

### Pas 1: Baixeu la imatge del sistema operatiu Graphene

Visiteu el lloc web oficial de Graphene OS a [https://grapheneos.org](https://grapheneos.org) and navigate to the [**Releases section**](https://grapheneos.org/releases) Trieu el fitxer d'imatge adequat per al vostre model de Google Pixel específic i descarregueu-lo a l'ordinador.

______

### Pas 2: verifiqueu la imatge

Per garantir la integritat de la imatge descarregada, heu de verificar la seva signatura criptogràfica. La documentació oficial de Graphene OS proporciona instruccions detallades sobre com verificar la imatge amb diferents sistemes operatius. Podeu trobar la documentació [here](https://grapheneos.org/usage#verify-grapheneos-image)

______

### Pas 3: habiliteu les opcions de desenvolupador i la depuració USB

1. Al dispositiu Google Pixel, aneu a l'aplicació Configuració.
2. Desplaceu-vos cap avall i toqueu "Quant al telèfon".
3. Toqueu "Número de compilació" set vegades per activar les Opcions de desenvolupador.
4. Torneu a la pàgina principal de configuració i toqueu "Opcions de desenvolupador".
5. Activa la depuració USB.

______

### Pas 4: connecteu el vostre dispositiu a l'ordinador

Utilitzeu un cable USB per connectar el vostre dispositiu Google Pixel a l'ordinador.

______

### Pas 5: engegueu el vostre dispositiu en mode Fastboot

Hauries de tenir el [android development tools](https://www.xda-developers.com/install-adb-windows-macos-linux/) ja instal·lat a la vostra màquina.

1. Obriu un indicador d'ordres o una finestra de terminal a l'ordinador.
2. Introduïu l'ordre següent per arrencar el dispositiu en mode d'arrencada ràpida:

```bash
adb reboot bootloader
```

______

### Pas 6: Flasheu la imatge del sistema operatiu Graphene

1. Un cop el dispositiu estigui en mode d'arrencada ràpida, utilitzeu l'ordre següent per mostrar la imatge del sistema operatiu Graphene al dispositiu:

```bash
fastboot flashall
```

Aquesta ordre esborrarà totes les dades existents al vostre dispositiu i instal·larà Graphene OS.

2. Espereu que finalitzi el procés de parpelleig.

______

### Pas 7: reinicieu el vostre dispositiu

Un cop finalitzat el procés d'instal·lació, reinicieu el dispositiu introduint l'ordre següent:

```bash
fastboot reboot
```

______

### Pas 8: Configura el sistema operatiu Graphene

Seguiu les instruccions a la pantalla per configurar Graphene OS al vostre dispositiu Google Pixel. Preneu-vos el temps per configurar la configuració segons les vostres preferències.

## Conclusió

La instal·lació de Graphene OS al dispositiu Google Pixel us pot oferir funcions de privadesa i seguretat millorades. Si seguiu els passos descrits en aquesta guia, podeu prendre el control del vostre dispositiu i protegir la vostra informació personal de possibles amenaces. Recordeu fer una còpia de seguretat de les vostres dades abans de continuar amb la instal·lació i seguiu amb cura cada pas per garantir una instal·lació correcta. Gaudeix dels avantatges de privadesa i seguretat que ofereix Graphene OS!

## Referències

1. [Graphene OS Website](https://grapheneos.org/)
2. [Android Developer Website](https://developer.android.com/)
3. [Android Debug Bridge (ADB) Documentation](https://developer.android.com/studio/command-line/adb)
4. [Fastboot Documentation](https://developer.android.com/studio/releases/platform-tools#fastboot)
5. [Google Pixel Device Compatibility List](https://grapheneos.org/#devices)
6. [Google Developer Documentation - Unlocking the Bootloader](https://source.android.com/setup/build/running#unlocking-the-bootloader)
7. [Google Developer Documentation - Factory Images](https://developers.google.com/android/images)
