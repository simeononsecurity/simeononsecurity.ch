---
title: "Mejora de sistemas Windows y servidores: Guía de configuración de marcas personalizadas"
date: 2020-08-13
toc: true
draft: false
description: "Learn how to set up custom branding on Windows 10 and Server 2016/2019/2022 systems to personalize your user experience."
tags: ["Marca Windows", "Marca del servidor", "marca personalizada", "personalización del sistema", "configuración de marca", "Windows 10", "Servidor 2016", "Servidor 2019", "Servidor 2022", "experiencia del usuario", "guía de personalización del sistema", "personalización", "marca del sistema", "Personalización de Windows", "Personalización del servidor", "Logotipo OEM", "imagen de usuario", "imagen invitada", "guión de marca", "Kit de herramientas de cumplimiento de seguridad de Microsoft", "Configuración de la marca Windows", "Configuración de la marca del servidor", "guía de marca personalizada", "marca personalizada", "tutorial de personalización del sistema", "Personalización del sistema Windows", "Personalización del sistema de servidores", "imágenes de marca", "buenas prácticas de marca", "Consejos de personalización de Windows", "Técnicas de personalización del servidor"]
---

**Marca de configuración en sistemas Windows 10 y Server 2016/2019/2022**.

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Branding-Script/actions/workflows/virustotal.yml)

## Cómo configurar los archivos de marca
- X] Sustituya todas las imágenes por las de su marca.
  - X] El logotipo OEM debe ser de 95x95 o 120x20 y estar en formato ".bmp
  - X] Genere la imagen de usuario junto con las variantes 32x32, 40x40, 48x48, 192x192.
  - X] Genere o copie la imagen de usuario para la imagen de invitado.
  
## Este script utiliza la siguiente herramienta:
- [Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Cómo ejecutar el script
### Instalación manual:
Si se descarga manualmente, el script debe lanzarse desde un powershell administrativo en el directorio que contiene todos los archivos del archivo [GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-copybranding.ps1
```
### Instalación automatizada:
El script puede ser lanzado desde la descarga extraída de GitHub así:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/sosbranding.ps1'|iex
```

