---
title: "Marca automatitzada per a sistemes Windows: controleu fàcilment l'escriptori, la pantalla de bloqueig i molt més"
date: 2020-08-14
---


Moltes organitzacions tenen la necessitat o volen controlar la marca d'un sistema Windows.
Això inclou el fons de pantalla de l'escriptori, l'avatar dels usuaris, la pantalla de bloqueig de Windows i, de vegades, el logotip de l'OEM.
A Windows 10, Windows Server 2016 i Windows Server 2019 això no és especialment fàcil.
Però, amb l'ajuda de l'script enllaçat, podem automatitzar-lo parcialment i fer el procés molt més fàcil.

## Baixeu els fitxers necessaris

** Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Com configurar els fitxers de marca

- [X] Substituïu totes les imatges per les vostres imatges de marca
  - [X] El logotip de l'OEM ha de ser de 95 x 95 o 120 x 20 i en format ".bmp".
  - [X] Genereu la imatge de l'usuari juntament amb les variants de 32x32, 40x40, 48x48 i 192x192.
  - [X] Genera o copia la imatge d'usuari per a la imatge de convidat.

## Com executar l'script
```
.\sos-copybranding.ps1
```

## Aquest script utilitza l'eina següent:

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
