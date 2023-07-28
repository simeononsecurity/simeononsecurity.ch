---
title: "Hash-uri de fișiere Linux: Un ghid pentru obținerea hașurilor SHA256, MD5 și SHA1 utilizând instrumentele încorporate"
draft: false
toc: true
date: 2023-05-25
description: "Aflați cum să obțineți hașuri SHA256, MD5 și SHA1 ale fișierelor pe Linux utilizând instrumente integrate, asigurând integritatea datelor și autenticitatea fișierelor."
tags: ["Hașuri de fișiere Linux", "Hash SHA256", "Hash MD5", "Hash SHA1", "Linia de comandă Linux", "integritatea fișierelor", "validarea datelor", "Securitate Linux", "instrumente încorporate", "verificarea fișierelor", "autenticitatea datelor", "algoritmi de hashing de fișiere", "Administrarea sistemului Linux", "instrumente de linie de comandă", "sume de verificare a fișierelor", "Utilități Linux", "verificări ale integrității fișierelor", "verificarea integrității datelor", "exemple de fișiere hash", "Comenzi hash Linux", "metode de hashing de fișiere", "Măsuri de securitate Linux", "Protecția datelor Linux", "Gestionarea fișierelor Linux", "Verificarea fișierelor Linux", "Integritatea fișierelor Linux", "securitatea datelor", "Validarea datelor Linux", "Securitatea sistemului Linux", "tehnici de hashing de fișiere", "asigurarea integrității fișierelor", "validarea securizată a fișierelor", "Integritatea datelor Linux"]
cover: "/img/cover/A_digital_representation_of_file_hashes_being_calculated.png"
coverAlt: "O reprezentare digitală a hașurilor de fișiere în curs de calcul pe ecranul unui terminal Linux, simbolizând integritatea și securitatea datelor."
coverCaption: ""
---

**Ghid: Obținerea de hașuri de fișiere pe Linux utilizând instrumente încorporate**

## Introducere

În lumea sistemelor Linux, obținerea hașurilor de fișiere este esențială pentru asigurarea integrității datelor și verificarea autenticității fișierelor. Hașurile fișierelor servesc ca identificatori unici care permit utilizatorilor să detecteze încercările de manipulare și să valideze integritatea datelor. În acest ghid cuprinzător, vom explora modul de obținere a hașurilor **SHA256**, **MD5** și **SHA1** ale fișierelor pe Linux, utilizând instrumentele încorporate. Urmați instrucțiunile pas cu pas și învățați prin exemple specifice.

______

## Obținerea hașurilor pe Linux folosind instrumente încorporate

Linux oferă mai multe instrumente încorporate care permit utilizatorilor să calculeze hașurile fișierelor fără a fi nevoie de instalarea de software suplimentar. Vom explora trei algoritmi de hashing utilizați pe scară largă: **SHA256**, **MD5** și **SHA1**.

### Obținerea hash-ului SHA256

Pentru a obține hash-ul **SHA256** al unui fișier pe Linux, puteți utiliza comanda `sha256sum` comandă. Deschideți un terminal și navigați în directorul în care se află fișierul. Apoi, executați următoarea comandă:

```bash
sha256sum file_path
```
Înlocuiți `file_path` cu calea reală către fișierul dvs.

### Obținerea hașurilor MD5 și SHA1
De asemenea, puteți obține `MD5` și `SHA1 hashes` a unui fișier pe Linux folosind comenzi similare:

- Pentru a obține valoarea `MD5 hash`

```bash
md5sum file_path
```

- Pentru a obține `SHA1 hash`

```bash
sha1sum file_path
```
Înlocuiți `file_path` cu calea de acces la fișierul dvs. în ambele comenzi.

## Exemple
Să ne adâncim în exemple specifice pentru a ilustra procesul de obținere a hașurilor folosind instrumentele încorporate pe Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Exemplul 1: Obținerea hașurii SHA256
Imaginați-vă că aveți un fișier numit `document.pdf` aflat în directorul `/home/user/docs` Pentru a obține `SHA256 hash` a acestui fișier pe Linux, executați următoarea comandă:

```bash
sha256sum /home/user/docs/document.pdf
```

La ieșire se va afișa `SHA256 hash` valoarea fișierului.

### Exemplul 2: Obținerea hașurii MD5

Să presupunem că aveți un fișier numit `image.jpg` stocate în directorul `/home/user/pictures` Pentru a obține `MD5 hash` a acestui fișier pe Linux, rulați următoarea comandă:

```bash
md5sum /home/user/pictures/image.jpg
```

Terminalul va afișa `MD5 hash` valoarea fișierului.

## Exemplul 3: Obținerea hașurii SHA1

Luați în considerare un scenariu în care aveți un fișier numit `data.txt` aflat în directorul `/home/user/files` Pentru a obține `SHA1 hash` a acestui fișier pe Linux, executați următoarea comandă:

```bash
sha1sum /home/user/files/data.txt
```
La ieșire se va afișa `SHA1 hash` valoarea fișierului.

## Concluzie
Obținerea de hash-uri de fișiere pe Linux utilizând instrumentele încorporate este o metodă simplă, dar puternică, de asigurare a integrității datelor și de validare a autenticității fișierelor. Urmând instrucțiunile furnizate în acest ghid, puteți calcula cu încredere hașurile SHA256, MD5 și SHA1 ale fișierelor dvs. pe sistemele Linux.

## Referințe

1. [sha256sum - Linux man page](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linux man page](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linux man page](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
