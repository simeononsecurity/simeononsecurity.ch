---
title: "Branding automatizzato per sistemi Windows: controlla facilmente il desktop, la schermata di blocco e altro ancora"
date: 2020-08-14
---


Molte organizzazioni hanno la necessità o desiderano controllare il marchio di un sistema Windows.
Ciò include lo sfondo del desktop, l'avatar degli utenti, la schermata di blocco di Windows e talvolta il logo OEM.
In Windows 10, Windows Server 2016 e Windows Server 2019 questo non è particolarmente facile.
Ma, con l'aiuto dello script collegato, possiamo parzialmente automatizzarlo e rendere il processo molto più semplice.

## Scarica i file richiesti

**Scarica i file richiesti dal file[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Come impostare i file di branding

- [X] Sostituisci tutte le immagini con le tue immagini di branding
  - [X] Il logo OEM deve essere 95x95 o 120x20 e in formato ".bmp"
  - [X] Genera l'immagine dell'utente insieme alle varianti 32x32, 40x40, 48x48, 192x192.
  - [X] Genera o copia l'immagine dell'utente per l'immagine dell'ospite.

## Come eseguire lo script
```
.\sos-copybranding.ps1
```

## Questo script utilizza il seguente strumento:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
