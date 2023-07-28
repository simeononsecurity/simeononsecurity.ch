---
title: "Marca automatizada para sistemas Windows: controle fácilmente el escritorio, la pantalla de bloqueo y mucho más"
date: 2020-08-14
---


Muchas organizaciones necesitan o desean controlar la imagen de marca de un sistema Windows.
Esto incluye el fondo de escritorio, el avatar del usuario, la pantalla de bloqueo de Windows y, a veces, el logotipo OEM.
En Windows 10, Windows Server 2016 y Windows Server 2019 esto no es particularmente fácil.
Pero, con la ayuda del script vinculado, podemos automatizarlo parcialmente y hacer que el proceso sea mucho más fácil.

## Descarga los archivos necesarios

**Descarga los archivos necesarios desde la página [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## Cómo configurar los archivos de marca

- X] Sustituya todas las imágenes por las de su marca.
  - X] El logotipo OEM debe ser de 95x95 o 120x20 y estar en formato ".bmp
  - X] Genere la imagen de usuario junto con las variantes 32x32, 40x40, 48x48, 192x192.
  - X] Genere o copie la imagen de usuario para la imagen de invitado.

## Cómo ejecutar el script
```
.\sos-copybranding.ps1
```

## Este script utiliza la siguiente herramienta:

- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
