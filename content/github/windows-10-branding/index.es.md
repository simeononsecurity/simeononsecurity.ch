---
title: "Automated Branding for Windows Systems - Easily Control Desktop, Lock Screen, and More"
date: 2020-08-14T14:37:16-05:00
toc: true
draft: false
description: "Control desktop wallpaper, users avatar, lock screen, and OEM logo with ease on Windows 10 and Server systems using a partially automated script."
tags: ["Automation", "Branding", "Windows Branding", "Customization", "Windows Customization", "Windows 10", "Windows Server 2016", "Windows Server 2019", "Powershell", "Script", "Windows System Branding", "Desktop Wallpaper", "Users Avatar", "Windows Lock Screen", "OEM Logo", "Microsoft Security Compliance Toolkit 1.0", "Organization Branding", "System Customization", "IT Automation", "Security Compliance"]
---
```
.\sos-copybranding.ps1
```

  Muchas organizaciones necesitan o desean controlar la marca de un sistema Windows. Esto incluye el fondo de escritorio, el avatar de los usuarios, la pantalla de bloqueo de Windows y, a veces, el logotipo de OEM. En Windows 10, Windows Server 2016 y Windows Server 2019, esto no es particularmente fácil. Pero, con la ayuda del script vinculado, podemos automatizarlo parcialmente y hacer que el proceso sea mucho más fácil.  ## Descarga los archivos requeridos  **Descargue los archivos requeridos del [Repositorio de GitHub](https://github.com/simeononsecurity/Windows-Branding-Script)**  ## Cómo configurar los archivos de marca  - [X] Reemplazar todas las imágenes con sus imágenes de marca   - [X] El logotipo OEM debe ser de 95x95 o 120x20 y en formato ".bmp"   - [X] Genere la imagen de usuario junto con las variantes de 32x32, 40x40, 48x48, 192x192.   - [X] Generar o copiar imagen de usuario para imagen de invitado.  ##ejecutar cómo el script  ## Este script utiliza la siguiente herramienta:  - [Kit de herramientas de cumplimiento de seguridad de Microsoft 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)