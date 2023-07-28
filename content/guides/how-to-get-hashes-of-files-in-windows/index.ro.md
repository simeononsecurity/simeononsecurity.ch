---
title: "Ghid complet: Hașuri de fișiere pe Windows utilizând PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Aflați cum să obțineți hașuri de fișiere în Windows utilizând PowerShell, inclusiv SHA256, MD5 și SHA1, cu instrucțiuni pas cu pas și exemple."
tags: ["hașuri de fișiere", "PowerShell", "Hash SHA256", "Hash MD5", "Hash SHA1", "integritatea fișierelor", "autentificarea datelor", "verificarea fișierelor", "algoritmi de hashing", "Sistem de operare Windows", "limbaj de scripting", "shell cu linie de comandă", "securitatea datelor", "criminalistică digitală", "securitate cibernetică", "calculul hash", "falsificarea fișierelor", "integritatea datelor", "autenticitatea fișierelor", "Securitatea Windows", "identificarea fișierelor", "apărare cibernetică", "securitatea fișierelor", "protecția datelor", "verificarea datelor", "validarea fișierelor", "Windows PowerShell", "generarea hașurilor", "algoritmi de hash", "funcții hash"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "O ilustrație de desen animat care arată un fișier cu un simbol de blocare și o lupă, reprezentând verificarea și securitatea hash-ului unui fișier."
coverCaption: ""
---

**Cum să obțineți hash-uri de fișiere pe Windows utilizând PowerShell**

În domeniul securității calculatoarelor, obținerea hașurilor de fișiere este un pas crucial în asigurarea integrității datelor și verificarea autenticității fișierelor. Hashurile sunt identificatori unici generați pentru fișiere, permițând utilizatorilor să detecteze încercările de manipulare și să valideze integritatea datelor. În acest ghid cuprinzător, vom explora procesul de obținere a hașurilor **SHA256**, **MD5** și **SHA1** ale fișierelor pe Windows utilizând puternicul limbaj de scripting, **PowerShell**. Urmați instrucțiunile pas cu pas și pătrundeți în profunzime în exemple specifice. Haideți să începem!

______

## Obținerea hașurilor pe Windows folosind PowerShell

PowerShell, un limbaj de scripting versatil și un shell cu linie de comandă pentru Windows, oferă cmdlet-ul **Get-FileHash**, care permite utilizatorilor să calculeze hash-ul unui fișier fără efort.

### Obținerea hash-ului SHA256

Pentru a obține **SHA256 hash** al unui fișier folosind PowerShell, urmați acești pași simpli:

1. Lansați PowerShell deschizând **Meniu Start**, căutând **PowerShell** și selectând **Windows PowerShell**.
2. Navigați în directorul în care se află fișierul. 3. Utilizați opțiunea `cd` urmată de calea către director.
3. Executați următoarea comandă pentru a obține hash-ul SHA256 al fișierului:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Obținerea hașurilor MD5 și SHA1
De asemenea, puteți obține `MD5` și `SHA1` hașuri ale unui fișier utilizând PowerShell. Utilizați următoarele comenzi:

- Pentru a obține `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Pentru a obține `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Nu uitați să înlocuiți "file_path" cu calea de acces la fișierul dvs. în ambele comenzi.

## Exemple
Să ne adâncim în exemple specifice pentru a ilustra procesul de obținere a hașurilor folosind PowerShell pe Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Exemplul 1: Obținerea hașurii SHA256
Imaginați-vă că aveți un fișier numit `document.pdf` aflat în directorul `C:\Files` Pentru a obține `SHA256 hash` a acestui fișier utilizând PowerShell, executați următoarea comandă:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

La ieșire va fi afișată valoarea hash SHA256 a fișierului.

### Exemplul 2: Obținerea hash-ului MD5

Să presupunem că dețineți un fișier numit `image.jpg` stocate în directorul `C:\Photos` Pentru a obține `MD5 hash` a acestui fișier utilizând PowerShell, rulați următoarea comandă:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

Terminalul va afișa valoarea hash MD5 a fișierului.

### Exemplul 3: Obținerea hash-ului SHA1

Luați în considerare un scenariu în care aveți un fișier numit `data.txt` aflat în directorul `C:\Documents` Pentru a obține `SHA1 hash` a acestui fișier utilizând PowerShell, executați următoarea comandă:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

La ieșire va fi afișată valoarea hash SHA1 a fișierului.