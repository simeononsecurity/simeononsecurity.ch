---
title: "Script bloqueador de anuncios en todo el sistema de Windows 10 para una mejor privacidad y seguridad"
date: 2021-04-02
toc: true
draft: false
description: "Bloquee anuncios, rastreadores y telemetría en Windows 10 con este potente script de PowerShell que utiliza el archivo hosts y el Firewall de Windows para bloquear anuncios en todo el sistema."
tags: ["Windows 10", "bloqueador de anuncios", "bloqueo de telemetría", "Script PowerShell", "bloqueo de anuncios en todo el sistema", "privacidad", "seguridad", "EasyList", "Privacidad fácil", "Lista de filtros NoCoin", "Filtro DNS AdGuard", "Listas de YoYos", "Servidores de malware de seguimiento de anuncios de Peter Lowe", "Cortafuegos de Windows", "listas de dominios", "bloquear los rastreadores de Windows", "rastreadores de bloques", "bloquear anuncios", "seguimiento en bloque"]
---

**Bloqueador de publicidad de Windows para todo el sistema

[![VirusTotal Scan](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml)

Este script es un script de Windows PowerShell que descarga y aplica el archivo "StevenBlack/hosts" al archivo "hosts" del sistema, que puede utilizarse para bloquear determinados dominios/sitios web asignándolos a una dirección IP de su elección (normalmente la dirección IP de la máquina local). El script comprueba la conexión a Internet y la configuración del proxy, e intenta descargar la última versión del archivo "hosts" de dos fuentes diferentes: "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" y "http://sbc.io/hosts/hosts". Si la descarga falla, el script continúa con una copia local del archivo "hosts". El script requiere privilegios elevados para ejecutarse y modifica la clave de registro ".NETFramework" para utilizar únicamente la última versión de .NET framework.

*Estamos buscando todos los comentarios e inquietudes para este repo. Por favor, envíe un [issue](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues) con cualquier información que pueda tener.

### Lists Used:
- [StevenBlack/hosts - adware + malware](https://github.com/StevenBlack/hosts)

### Ejemplo:
#### Instalación manual:
**El script puede iniciarse desde la descarga extraída de GitHub así:**
```powershell
.\sos-system-wide-windows-ad-block.ps1
```
#### Instalación automática:
Ejecuta automáticamente la última versión del script:
```powershell
iwr -useb 'https://simeononsecurity.com/scripts/soswindowsadblocker.ps1' | iex
```

