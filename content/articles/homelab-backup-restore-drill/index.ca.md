---
title: "Fes una prova de restauració de còpies de seguretat del homelab amb Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Comprova si una còpia de seguretat del homelab restaura fitxers utilitzables. Defineix un objectiu de recuperació, restaura amb Restic en una altra ubicació, revisa les dades i registra el resultat."
genre: ["Homelab", "Còpia de seguretat", "Recuperació de desastres"]
tags: ["còpia de seguretat homelab", "prova de restauració", "restauració Restic", "verificació de còpia", "prova de recuperació", "recuperació de desastres", "RPO", "RTO", "repositori de còpies", "comprovació Restic", "còpia NAS", "còpia del servidor", "recuperació de VM", "restauració de fitxers", "xifratge de còpies", "monitoratge de còpies", "pla de recuperació", "prova de còpia", "còpia externa", "integritat de dades"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Un servidor homelab i un NAS fan una còpia en una unitat separada, amb una carpeta de restauració verificada en un ordinador de proves aïllat i un cronòmetre."
coverCaption: "Restaura en una destinació separada, comprova les dades i mesura el temps necessari."
---

Que una tasca de còpia informi que ha acabat correctament no demostra que puguis recuperar un fitxer utilitzable. Una **prova de restauració** verifica el camí des de la còpia emmagatzemada fins a les dades funcionals sense substituir els fitxers actius. Aquesta guia fa servir Restic per a un exemple de restauració de fitxers i proporciona un registre que pots repetir després de modificar el laboratori.

<!--more-->

Restic és un programa de còpies de seguretat. Un **repositori** és l'espai d'emmagatzematge protegit que conté les dades copiades. Una **instantània** és un punt de còpia desat.

## Punts clau

- **Tria un objectiu:** Selecciona els fitxers o el servei que cal recuperar i defineix un punt i un temps de recuperació acceptables.
- **Restaura per separat:** Fes servir una destinació de proves buida perquè la prova no sobreescrigui dades actives.
- **Comprova el resultat:** Obre els fitxers restaurats, verifica les dades de l'aplicació quan sigui possible i mesura el temps transcorregut.
- **Registra els errors:** Anota l'ID de la instantània, els elements absents, els permisos i les reparacions al pla de recuperació.

## Abans de començar

Necessites un repositori de còpies funcional, la seva contrasenya o clau, una destinació amb prou espai lliure i permís de lectura tant a la còpia com a la ubicació de prova. Aquest exemple pressuposa que Restic és instal·lat i que el repositori conté una còpia recent de fitxers. La [guia d'inici ràpid de Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) explica com crear un repositori i fer les primeres còpies. La [guia de còpies 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) del lloc tracta la ubicació de les còpies. La [visió general de homelab](/articles/what-is-a-homelab-and-should-you-have-one/) inclou una breu llista per provar-les.

Aquesta prova comprova els fitxers d'una instantània. Una base de dades, màquina virtual o aplicació també necessita els seus propis passos de recuperació. Mantén el sistema de proves aïllat si iniciar el servei restaurat pot interferir amb l'actiu. Una còpia de fitxers correcta no demostra que tots els serveis s'iniciïn.

> **Avís:** No restauris sobre una ruta activa durant la primera prova. Fes servir un directori de proves buit en un sistema de fitxers o host separat. No incloguis la contrasenya del repositori en captures, tiquets ni historial del shell.

## Defineix l'objectiu de recuperació

Anota què necessites després d'una fallada. L'**objectiu de punt de recuperació (RPO)** és el punt temporal fins al qual cal recuperar les dades després d'una interrupció. Representa la pèrdua màxima de dades acceptable. L'**objectiu de temps de recuperació (RTO)** indica quant de temps pot estar indisponible el servei. NIST defineix tots dos a la seva [guia de planificació de contingències](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Els teus objectius han de reflectir la freqüència amb què canvien les dades i el temps de restauració al teu maquinari.

| Element | Objectiu il·lustratiu | Què cal registrar |
|---|---|---|
| **Documents familiars** | Darrera còpia nocturna | Hora de l'última instantània i fitxers oberts |
| **Configuració del servei domèstic** | Darrer canvi conegut com a correcte | Versió de configuració i secrets requerits |
| **Biblioteca multimèdia en emmagatzematge connectat a la xarxa (NAS)** | Còpia setmanal | Reproducció de mostra i temps de restauració |

Els objectius anteriors són exemples, no resultats mesurats. Al pla de recuperació, registra on s'emmagatzema la còpia i com una persona autoritzada obté la contrasenya del repositori o la clau de xifratge. No posis valors secrets al pla ni al registre de la prova. Desa els secrets mitjançant una via protegida i independent de l'host fallit. Un repositori que sobreviu però perd la seva única contrasenya no és recuperable.

Tria un **conjunt de fitxers crítics** per a aquesta prova. Inclou un fitxer petit que saps que hauria de ser a la instantània més recent. Per a un servei, enumera també la configuració, l'exportació de la base de dades, els certificats i la versió de l'aplicació necessaris per iniciar-lo. Confirma que el mètode de còpia captura dades coherents de l'aplicació abans de confiar en una còpia de fitxers d'una base de dades en execució.

## Troba una instantània

Fes servir l'accés al repositori autoritzat per a la prova. Restic utilitza un bloqueig temporal del repositori mentre llegeix o modifica dades de còpia. Les ordres següents pressuposen que el repositori permet aquesta operació. Mantén separats l'origen actiu i la destinació de prova. Substitueix `/path/to/repository` pel camí real del repositori Restic i llista les instantànies:

```bash
restic -r /path/to/repository snapshots
```

Restic demana la contrasenya del repositori si no l'has proporcionat mitjançant un mètode de secrets configurat. La [llista d'instantànies](https://restic.readthedocs.io/en/stable/010_introduction.html) mostra l'ID, la data, l'host i els camins d'origen. Registra l'ID i la marca temporal de la instantània que vols provar. Compara-la amb el teu RPO. El registre recent d'una tasca no substitueix aquesta comprovació, ja que la instantània necessària podria ser més antiga del que penses.

Si falta la instantània esperada, atura la prova i investiga la planificació de còpies, la selecció de l'origen i el camí del repositori. No triïs d'amagat una instantània antiga i declaris assolit l'objectiu de recuperació.

## Restaura en una destinació buida

Crea un **directori de destinació buit** en un sistema de fitxers de prova amb prou espai per a la instantània. No indiquis a Restic l'origen original, una compartició de producció muntada o una carpeta existent amb dades que vulguis conservar. Substitueix `SNAPSHOT_ID` i els dos camins d'exemple abans d'executar l'ordre:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

La [guia de restauració de Restic](https://restic.readthedocs.io/en/stable/050_restore.html) descriu l'ID de la instantània i el camí `--target`. L'arbre restaurat manté el camí d'origen sota el directori de destinació, així que localitza els fitxers reals abans d'avaluar el resultat. Si només necessites un subconjunt petit, utilitza els [filtres d'inclusió documentats](https://restic.readthedocs.io/en/stable/050_restore.html) i registra què has exclòs. No utilitzis `--delete` en una prova. Restic indica que aquesta opció elimina de la destinació els fitxers absents de la instantània.

Engega un cronòmetre quan comenci la restauració. Atura'l quan els fitxers requerits siguin presents i utilitzables, no quan l'ordre mostri el primer progrés. Registra la ubicació del repositori, la connexió de xarxa, la mida de les dades i l'host de prova, perquè aquestes condicions afecten una recuperació posterior.

> **Resultat esperat:** La instantània triada es restaura en una destinació separada sense modificar l'origen actiu.

## Verifica les dades i el servei

Obre alguns fitxers restaurats amb l'aplicació que els llegeix normalment. Inclou un fitxer recent, un d'antic i un d'un directori niat. Compara mides o sumes de comprovació conegudes si les vas registrar abans de la còpia. A Linux, revisa el propietari i els permisos, ja que un fitxer llegible pel compte de prova encara pot fallar amb el compte del servei.

Per a un servei, restaura en una instància de prova aïllada. Comprova la configuració, els secrets requerits, la coherència de la base de dades, l'inici i una acció representativa d'un usuari. Una restauració de fitxers que omet una base de dades o un secret no és una recuperació completa del servei. No iniciïs mai la instància de prova amb la base de dades activa ni una adreça de producció sense un pla de canvi controlat.

Després de restaurar la mostra, executa la comprovació del repositori de Restic:

```bash
restic -r /path/to/repository check
```

Per llegir totes les dades del repositori, utilitza `check --read-data` durant una finestra de manteniment. Restic adverteix que l'ordre llegeix tot el repositori i pot descarregar moltes dades d'un backend remot. La [guia de resolució de problemes de Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) descriu la comprovació i el seu cost. Una comprovació neta aporta confiança, però no substitueix obrir els fitxers restaurats ni iniciar el servei.

```bash
restic -r /path/to/repository check --read-data
```

Compara l'antiguitat de la instantània amb el teu RPO i el temps de recuperació mesurat amb el teu RTO. Si falla qualsevol objectiu, la prova ha fallat encara que Restic hagi acabat sense errors. Ajusta la freqüència de les còpies, la ubicació de l'emmagatzematge, l'amplada de banda o el procediment de recuperació i torna-ho a provar.

## Desa un registre de restauració

Escriu un registre breu després de cada prova. El [control de còpies SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) de NIST inclou la restauració de funcions de sistema de mostra com a manera de provar la recuperació. Un registre repetible permet veure si el pla millora.

| Camp | Resultat que cal introduir |
|---|---|
| **Data i operador** | Quan s'ha fet la prova i qui l'ha executada |
| **Repositori i instantània** | Ubicació, ID, marca temporal i camins d'origen |
| **Objectiu de recuperació** | Fitxers o servei provat, i RPO i RTO |
| **Resultat mesurat** | Antiguitat de la instantània, temps de restauració i comprovacions de fitxers o servei |
| **Errors** | Dades absents, accés a claus, permisos, xarxa o problemes d'inici |
| **Acció següent** | Responsable, reparació i data de la prova següent |

No posis al registre la contrasenya del repositori, la clau de recuperació ni contingut sensible dels fitxers. Desa'ls en un magatzem protegit de secrets i documenta com els obté una persona autoritzada durant una interrupció.

## Resolució de problemes

- **No hi ha la contrasenya:** Comprova la via independent de custòdia de claus. No suposis que l'host fallit estarà disponible per recuperar la seva pròpia clau.
- **La instantània és massa antiga:** Revisa la planificació, les tasques fallides, els camins d'origen i si l'host esperat va copiar a un altre repositori.
- **La restauració és massa lenta:** Mesura la velocitat de lectura de l'emmagatzematge, la connexió de xarxa i el volum de dades. Prova un subconjunt crític més petit i revisa el RTO o el disseny de recuperació.
- **El fitxer hi és però el servei falla:** Revisa exportacions de bases de dades, versió de l'aplicació, propietari, permisos, certificats i secrets absents.
- **La comprovació del repositori informa d'errors:** Conserva la sortida i una còpia del repositori si és possible. Segueix la guia de Restic sobre [investigació de danys](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) abans d'intentar reparar-lo.
- **La prova ha canviat dades actives:** Atura el servei de prova, verifica les dades de producció i revisa el pla d'aïllament abans de repetir la prova.

## Passos següents

Repeteix la prova després de canviar el programari de còpies, l'emmagatzematge, les claus de xifratge o els serveis crítics. Alterna diversos conjunts de fitxers i recuperacions completes de serveis amb el temps. Conserva una còpia independent segons el teu [pla 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). L'objectiu és una restauració mesurada i repetible quan l'host original ja no hi sigui.
