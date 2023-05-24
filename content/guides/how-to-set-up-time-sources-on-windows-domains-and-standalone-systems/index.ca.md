---
title: "Bones pràctiques per a la gestió de fonts de temps en dominis de Windows i màquines autònomes"
draft: false
toc: true
date: 2023-05-23
description: "Apreneu a configurar i gestionar de manera eficaç les fonts de temps als dominis de Windows i a les màquines autònomes per garantir una sincronització horària precisa i evitar possibles problemes."
tags: ["fonts de temps", "Domini Windows", "màquines autònomes", "sincronització horària", "cronometratge precís", "Servidors NTP", "controladors de domini", "Servei d'hora de Windows", "errors d'autenticació", "inconsistències del fitxer de registre", "problemes de replicació", "configuració de la font de temps", "gestió de la font de temps", "Sincronització horària de Windows", "bones pràctiques de cronometratge", "configuració de la font de temps", "sincronització de l'hora del sistema", "Sincronització horària del domini Windows", "sincronització horària de la màquina autònoma", "selecció de la font del temps", "resolució de problemes de la font de temps", "errors de font de temps", "problemes de la font del temps", "ordres de configuració de la font de temps", "instruccions de configuració de la font de temps", "reptes de sincronització horària", "conseqüències de la pèrdua de temps", "prevenció de la deriva del temps", "Resolució de fallades de sincronització horària", "resolució de problemes de sincronització horària", "gestió de fonts de temps en dominis de Windows", "manejar fonts de temps en màquines Windows autònomes", "evitant la pèrdua de temps en entorns Windows", "conseqüències dels errors de sincronització horària", "bones pràctiques per a una cronometratge precisa"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Una imatge que representa un rellotge que es sincronitza amb un controlador de domini i una màquina autònoma, que simbolitza la gestió de la font del temps i la sincronització de l'hora precisa en entorns Windows."
coverCaption: ""
---

**Com configurar i gestionar les fonts de temps en un domini de Windows i en màquines Windows autònomes**

La sincronització de l'hora és crucial per mantenir les marques de temps precises i garantir el bon funcionament dels sistemes en un domini Windows o màquines Windows autònomes. En aquest article, parlarem de les millors pràctiques per configurar i gestionar les fonts de temps en ambdós escenaris, destacant la importància que els membres del domini apuntin als controladors de domini. També explorarem diferents opcions per a les fonts de temps, posant èmfasi en l'ús de grups NTP externs o servidors de temps basats en GPS per a una precisió òptima.

______

## Configuració de fonts de temps en un domini de Windows

En un domini de Windows, és essencial tenir una sincronització horària coherent entre tots els membres del domini. La millor pràctica és configurar els controladors de domini com a font de temps principal per als membres del domini. En fer-ho, us assegureu que tots els sistemes del domini tinguin l'hora sincronitzada, la qual cosa és fonamental per a l'autenticació, el registre i diverses operacions del domini.

### Opcions de font de temps per als controladors de domini

Els controladors de domini poden obtenir el seu temps de diferents fonts, inclòs el rellotge de la BIOS, VMware Tools (en entorns virtualitzats) o servidors de temps externs. Tot i que pot ser convenient utilitzar el rellotge de la BIOS o VMware Tools, es recomana utilitzar una font **estrat 0 o 1** com un grup NTP extern o un servidor de temps basat en GPS per obtenir una precisió millorada.

#### Grups NTP externs

Els grups NTP externs són fonts fiables i distribuïdes globalment per a la sincronització de l'hora. Consten d'un gran nombre de servidors NTP mantinguts per organitzacions i institucions d'arreu del món. Si configureu els controladors de domini per sincronitzar-los amb grups NTP externs, podeu garantir una cronometratge precisa dins del domini de Windows.

Per configurar controladors de domini per utilitzar un grup NTP extern, seguiu aquests passos:

1. Obriu un indicador d'ordres elevat al controlador de domini.
2. Executeu l'ordre següent:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Aquesta ordre configura el controlador de domini perquè es sincronitzi amb el grup NTP pool.ntp.org. Ajusteu l'ordre per utilitzar un grup NTP diferent o diverses fonts si ho voleu.

3. Reinicieu el servei d'hora de Windows per aplicar els canvis:

```shell
net stop w32time && net start w32time
```


#### Servidors de temps basats en GPS

Una altra opció per als controladors de domini és utilitzar servidors de temps basats en GPS. Aquests servidors es basen en senyals GPS per proporcionar informació horària molt precisa. Si configureu un servidor d'hora basat en GPS allotjat localment i configureu els controladors de domini per sincronitzar-lo, podeu aconseguir una sincronització horària precisa dins del domini de Windows.

### Configuració dels membres del domini

Els membres del domini, com ara les màquines client i altres servidors, s'han de configurar per sincronitzar el seu temps amb els controladors de domini. Això garanteix que tots els sistemes del domini romanguin sincronitzats i s'evita qualsevol problema relacionat amb el temps.

Per configurar els membres del domini perquè sincronitzin l'hora amb els controladors de domini, normalment no calen passos addicionals. De manera predeterminada, els membres del domini sincronitzen automàticament la seva hora amb els controladors de domini.

______

## Configuració de fonts de temps en màquines Windows autònomes

A les màquines Windows autònomes que no formen part d'un domini, el procés de configuració de fonts d'hora pot variar segons la versió de Windows i la configuració regional. De manera predeterminada, les màquines Windows autònomes solen utilitzar **time.windows.com** com a font de temps principal. Tanmateix, val la pena assenyalar que el comportament predeterminat es pot modificar.

### Canviar la font del temps en màquines autònomes

Si voleu canviar l'origen de l'hora en una màquina Windows autònoma, podeu seguir aquests passos:

1. Obriu un indicador d'ordres elevat a la màquina.
2. Executeu l'ordre següent per configurar el servidor NTP:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Aquesta ordre estableix time.windows.com com a font de temps per a la màquina autònoma. Ajusteu l'ordre per utilitzar una font de temps diferent si voleu.

3. Reinicieu el servei d'hora de Windows perquè els canvis tinguin efecte:

```shell
net stop w32time && net start w32time
```


En executar aquestes ordres, podeu configurar una màquina autònoma de Windows per sincronitzar el seu temps amb la font d'hora desitjada.

______

## Conclusió

La sincronització horària adequada és vital tant per als dominis de Windows com per a les màquines autònomes. En un domini de Windows, és crucial configurar els membres del domini perquè apuntin als controladors de domini per a la sincronització de l'hora. Els controladors de domini poden obtenir el seu temps de diverses fonts, amb l'ús de grups NTP externs o servidors d'hora basats en GPS com la pràctica recomanada per augmentar la precisió.

A les màquines Windows autònomes, la font d'hora predeterminada sol ser time.windows.com. Tanmateix, podeu canviar la font del temps mitjançant les ordres proporcionades.

Si seguiu aquestes pràctiques recomanades i configureu les fonts de temps adequades, assegureu una cronometratge precisa, una autenticació fiable i un registre coherent al vostre entorn Windows.

______

## Referències

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)

