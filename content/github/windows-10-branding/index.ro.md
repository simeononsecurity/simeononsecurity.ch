---
title: "Branding automatizat pentru sistemele Windows - Controlați cu ușurință desktopul, ecranul de blocare și multe altele"
date: 2020-08-14
---


Multe organizații au nevoie sau doresc să controleze branding-ul unui sistem Windows.
Aceasta include imaginea de fundal de pe desktop, avatarul utilizatorilor, ecranul de blocare Windows și, uneori, sigla OEM.
În Windows 10, Windows Server 2016 și Windows Server 2019, acest lucru nu este deosebit de ușor.
Dar, cu ajutorul scriptului legat, îl putem automatiza parțial și face procesul mult mai ușor.

## Descărcați fișierele necesare

**Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Cum se configurează fișierele de branding

- [X] Înlocuiește toate imaginile cu imaginile de branding
  - [X] Sigla OEM trebuie să fie de 95x95 sau 120x20 și în format „.bmp”
  - [X] Generați imaginea utilizatorului împreună cu variantele 32x32, 40x40, 48x48, 192x192.
  - [X] Generați sau copiați imaginea utilizatorului pentru imaginea invitatului.

## Cum se rulează scriptul
```
.\sos-copybranding.ps1
```

## Acest script folosește următorul instrument:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
