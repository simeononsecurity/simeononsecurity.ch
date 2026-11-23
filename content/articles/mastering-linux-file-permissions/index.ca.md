---
title: "Permisos de fitxers a Linux: una guia completa"
draft: false
toc: true
date: 2023-05-22
lastmod: 2026-11-23
description: "Aprèn a gestionar els permisos de fitxers a Linux per protegir el sistema de fitxers, controlar-ne la propietat i aplicar bones pràctiques."
tags: ["permisos de fitxers Linux", "sistema de fitxers segur", "control d'accés", "propietat", "guia de permisos de fitxers", "seguretat de Linux", "seguretat del sistema de fitxers", "ordre chmod", "ordre chown", "auditoria de permisos", "Principi del mínim privilegi", "compliment normatiu", "GDPR", "HIPAA", "auditoria de permisos de fitxers", "documentació de normatives", "seguretat del sistema", "seguretat de xarxa", "xifratge", "gestió d'usuaris"]
cover: "/img/cover/A_cartoon-style_image_depicting_a_locked_file_cabinet.webp"
coverAlt: "Il·lustració d'un arxivador tancat amb clau i claus que representen els permisos de l'usuari, el grup i la resta de persones."
coverCaption: ""
---

**Dominar els permisos de fitxers a **Linux**: una guia completa per protegir el sistema de fitxers**

Linux és un sistema operatiu potent i versàtil que ofereix funcions de seguretat robustes, entre les quals hi ha els **permisos de fitxers**. Entendre'ls i configurar-los correctament és essencial per mantenir un **sistema de fitxers segur**. Aquesta guia explica els permisos de fitxers de Linux i t'ajuda a dominar aquest aspecte clau de la seguretat del sistema.

## Introducció als permisos de fitxers de Linux

Linux és un sistema operatiu **multiusuari** en què diverses persones poden accedir al sistema alhora. Els permisos controlen l'accés als fitxers i directoris perquè només les persones autoritzades puguin **llegir**, **escriure** o **executar** accions concretes.

Cada fitxer i directori de Linux té tres conjunts de permisos: **usuari**, **grup** i **altres**. Els permisos d'**usuari** s'apliquen al propietari del fitxer, els de **grup** al grup associat i els d'**altres** a tothom més.

### Entendre els tipus de permisos

Els permisos de Linux tenen tres tipus: **lectura**, **escriptura** i **execució**, representats amb aquests símbols:

- **r**: el permís de lectura permet veure el contingut d'un fitxer o llistar el contingut d'un directori.
- **w**: el permís d'escriptura permet modificar un fitxer o afegir, eliminar o canviar el nom dels fitxers d'un directori.
- **x**: el permís d'execució permet executar un fitxer com a programa o accedir al contingut d'un directori.

Cada tipus de permís es pot concedir o denegar a cadascun dels tres conjunts: **usuari**, **grup** i **altres**.

### Representació numèrica dels permisos

A més de la representació simbòlica, els permisos de Linux també es poden expressar amb nombres. Cada tipus té un valor: **lectura (4)**, **escriptura (2)** i **execució (1)**. Si sumem els valors, obtenim un nombre octal de tres xifres que representa els permisos d'un fitxer o directori.

Per exemple, si un fitxer permet que l'usuari el llegeixi i l'escrigui, que el grup el llegeixi i no dona cap permís a la resta, la representació numèrica és **640**.

## Modificar els permisos dels fitxers

Per modificar els permisos a Linux, fem servir l'ordre **chmod**. Aquesta ordre permet canviar per separat els permisos dels conjunts d'usuari, grup i altres.

### Canviar permisos amb notació simbòlica

La notació simbòlica permet modificar els permisos amb símbols fàcils de llegir. La sintaxi bàsica és:

```shell
chmod <permissions> <file>
```

El valor <permissions> pot fer servir símbols com u (usuari), g (grup), o (altres), + (afegir permís), - (treure permís) i = (definir el permís).

Per exemple, per donar permisos de lectura i escriptura a l'usuari, fem servir:

```bash
chmod u+rw file.txt
```
### Canviar permisos amb notació numèrica

La notació numèrica ofereix una manera concisa de modificar permisos amb nombres octals. Com s'ha explicat abans, cada tipus de permís té un valor numèric.

Per donar lectura, escriptura i execució a l'usuari, lectura i execució al grup i cap permís a la resta, fem servir:

```bash
chmod 750 file.txt
```
## Propietat dels fitxers i grups

A més dels permisos, Linux conserva informació sobre la propietat de cada fitxer i directori. La propietat determina quin usuari i quin grup controlen el fitxer.

### Propietat de l'usuari

L'usuari que crea un fitxer n'és el propietari. Pot controlar-lo i canviar-ne els permisos, el nom, la ubicació o eliminar-lo. L'ordre `chown` canvia el propietari d'un fitxer o directori.

La sintaxi bàsica de `chown` és:

```shell
chown <user> <file>
```

El valor <user> pot ser un nom d'usuari o un identificador d'usuari (UID). Per exemple, per assignar el fitxer a johndoe, fem servir:

```bash
chown johndoe file.txt
```

### Propietat del grup
Cada fitxer i directori també està associat a un grup. Per defecte, és el grup principal de l'usuari que ha creat el fitxer. L'ordre chgrp permet canviar el grup propietari.

La sintaxi bàsica de chgrp és:

```bash
chgrp <group> <file>
```

El valor <group> pot ser un nom de grup o un identificador de grup (GID). Per exemple, per assignar el fitxer al grup developers, fem servir:

```bash
chgrp developers file.txt
```

## Permisos especials dels fitxers
A més dels permisos estàndard de lectura, escriptura i execució, Linux ofereix permisos especials que poden millorar la seguretat i afegir funcions.

### Establiment de l'identificador d'usuari (SUID)
El permís d'establiment de l'identificador d'usuari (SUID) permet executar un fitxer amb els permisos del propietari, en lloc dels de qui l'executa. Pot ser útil quan una tasca requereix privilegis superiors als disponibles per a l'usuari.

Per establir SUID en un fitxer, fem servir chmod amb notació numèrica:

```bash
chmod 4755 file.txt
```

El primer dígit, 4, estableix el permís SUID per a l'usuari.

### Establiment de l'identificador de grup (SGID)
El permís d'establiment de l'identificador de grup (SGID) és semblant al SUID, però s'aplica als grups. Quan s'executa un fitxer amb SGID, ho fa amb els permisos del grup propietari.

Per establir SGID en un fitxer, fem servir chmod amb notació numèrica:

```bash
chmod 2755 file.txt
```
El primer dígit, 2, estableix el permís SGID per al grup.

### Bit sticky
El bit sticky és una funció de seguretat que protegeix els directoris contra eliminacions no autoritzades. Quan s'estableix en un directori, només el propietari d'un fitxer el pot eliminar d'aquell directori.

Per establir el bit sticky en un directori, fem servir chmod amb notació numèrica:

```bash
chmod 1755 directory/
```

El primer dígit, 1, estableix el bit sticky.

## Bones pràctiques per als permisos de fitxers
Per mantenir un sistema de fitxers segur, segueix aquestes bones pràctiques quan configuris permisos a Linux:

### Principi del mínim privilegi
El principi del mínim privilegi recomana donar als usuaris i processos només el nivell d'accés mínim necessari per fer la seva feina. En configurar permisos, assegura't que cada usuari i grup tingui només els permisos necessaris.

### Auditar els permisos periòdicament

Auditar periòdicament els permisos és essencial per mantenir la seguretat del sistema de fitxers. Les auditories ajuden a detectar accessos no autoritzats i possibles vulnerabilitats. Segueix aquests passos:

1. **Identifica els fitxers i directoris crítics**: determina quins contenen dades sensibles o importants i necessiten permisos més estrictes.

2. **Revisa els permisos**: fes servir l'ordre `ls` amb l'opció `-l` per mostrar informació detallada dels fitxers i directoris, inclosos els permisos. Busca elements amb permisos massa amplis que puguin representar un risc.

3. **Corregeix els permisos**: si trobes permisos incorrectes o insegurs, fes servir l'ordre `chmod` per modificar-los. Assegura't que només els usuaris o grups autoritzats tinguin els permisos necessaris.

4. **Estableix un calendari d'auditoria**: planifica auditories periòdiques, setmanals, mensuals o segons la política de seguretat de l'organització. Les auditories regulars ajuden a protegir la integritat del sistema i a resoldre ràpidament els problemes de permisos.

### Documentar els permisos i les normatives

És important documentar els permisos dels fitxers i les polítiques de control d'accés de l'organització. Aquesta documentació serveix de referència per als administradors i usuaris i hauria d'incloure:

- Explicacions dels tipus de permisos de fitxers i el seu significat.
- Instruccions per definir i modificar permisos.
- Bones pràctiques per assignar permisos a usuaris i grups.
- Requisits normatius o estàndards del sector aplicables a l'organització, com ara el **Reglament general de protecció de dades (GDPR)** o la **Llei de portabilitat i responsabilitat de les assegurances mèdiques (HIPAA)**.

Documentar les normes i oferir indicacions clares ajuda a mantenir la coherència i millora la consciència de seguretat dins l'organització.

## Conclusió

Dominar els permisos de fitxers a Linux és essencial per mantenir un sistema de fitxers segur. Entendre'n els conceptes, modificar correctament els permisos i seguir bones pràctiques millora la seguretat dels sistemes Linux. Les auditories periòdiques i la documentació de les normes protegeixen la integritat del sistema i garanteixen que només les persones autoritzades accedeixin a dades sensibles.

Els permisos són només un aspecte de la seguretat general del sistema. Considera també altres mesures, com ara el xifratge, la gestió d'usuaris i la seguretat de xarxa, per crear una estratègia completa i robusta.

Si segueixes les indicacions d'aquesta guia, podràs gestionar els permisos de fitxers a Linux i protegir el teu sistema de fitxers.

## Referències

- [Linux File Permissions Explained](https://www.digitalocean.com/community/tutorials/linux-permissions-101-an-introduction-to-chmod-and-chown) - Tutorial de la comunitat DigitalOcean
- [Understanding File Permissions](https://www.redhat.com/sysadmin/understanding-linux-permissions) - Article de l'equip d'administració de sistemes de Red Hat
- [General Data Protection Regulation (GDPR)](https://gdpr.eu/) - Lloc web oficial del GDPR
- [Health Insurance Portability and Accountability Act (HIPAA)](https://www.hhs.gov/hipaa/index.html) - Lloc web oficial de HIPAA
