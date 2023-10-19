---
title: "Optimiza tu PC Windows con Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Mejora el rendimiento y la privacidad de tu sistema operativo Windows con Windows-Optimize-Debloat, un completo script que ayuda a eliminar el bloatware y a optimizar la configuración del sistema."
tags: ["Windows-Optimize-Debloat", "Optimización de Windows", "Ventanas de flotación", "Acelerar Windows", "Optimizar el rendimiento de Windows", "Aumento del rendimiento de Windows", "Optimización del sistema Windows", "Microsoft", "Privacidad", "Eliminación de Bloatware", "Windows 10", "Windows 11", "Windows Defender", "Actualización de Windows", "Cortona", "Objetos de directiva de grupo", "Telemetría", "Tienda Windows", "Windows 10 Profesional", "Windows 10 Hogar"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Para quienes buscan minimizar sus instalaciones de Windows 10 y 11.*

**Nota:** Este script debería funcionar para la mayoría, si no todos, los sistemas sin problemas. Mientras [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No ejecute este script si no entiende lo que hace.

## Introducción:
Windows 10 y 11 es un sistema operativo invasivo e inseguro fuera de la caja.
Organizaciones como [Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) y otros han recomendado cambios en la configuración para optimizar y depurar el sistema operativo Windows 10. Estos cambios incluyen el bloqueo de la telemetría, la eliminación de registros y la eliminación de bloatware, por nombrar algunos. Este script pretende automatizar las configuraciones recomendadas por esas organizaciones.

## Notas:
- Este script está diseñado para operar principalmente en entornos de **Uso Personal**.
- Este script está diseñado de tal manera que las optimizaciones, a diferencia de otros scripts, no romperán la funcionalidad principal de Windows.
 - Características como Windows Update, Windows Defender, la Tienda Windows, y Cortona han sido restringidas, pero no están en un estado disfuncional como la mayoría de otros scripts de Privacidad de Windows 10.
- Si usted busca un script minimizado dirigido sólo a entornos comerciales, por favor vea esto [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisitos:
- [X] Windows 10/11 Enterprise, Windows 10 Professional o Windows 10 Home
  - Windows Home no permite configuraciones GPO.
    - El script seguirá funcionando, pero no se aplicarán todas las configuraciones.
  - Las ediciones "N" de Windows no se han probado.
  - Ejecute el script [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para actualizar y verificar la última versión principal.

## Arreglar cuenta Microsoft o servicios Xbox:
Esto se debe a que bloqueamos el inicio de sesión en cuentas de microsoft. La telemetría de Microsoft y la asociación de identidades están mal vistas.
Sin embargo, si usted todavía desea utilizar estos servicios ver los siguientes tickets de incidencia para la resolución:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Una lista de scripts y herramientas que utiliza esta colección:
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Se consideraron configuraciones adicionales de:
- [BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
- [MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
- [Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
- [UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
- [Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
- [The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
- [TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
- [W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

### Cómo ejecutar el script:
### Instalación automatizada:
El script puede ser lanzado desde la descarga extraída de GitHub así:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Instalación manual:
Si se descarga manualmente, el script debe ser lanzado desde un powershell administrativo en el directorio que contiene todos los archivos del [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

El script "sos-optimize-windows.ps1" incluye varios parámetros que permiten personalizar el proceso de optimización. Cada parámetro es un valor booleano que por defecto es true si no se especifica.

- **$cleargpos**: Borra la configuración de los objetos de directiva de grupo.
- **$installupdates**: Instala actualizaciones en el sistema.
- **$removebloatware**: Elimina programas y características innecesarias del sistema.
- **$disabletelemetry**: Desactiva la recogida de datos y la telemetría.
- **$privacy**: Realiza cambios para mejorar la privacidad.
- **$imagecleanup**: Limpia los archivos innecesarios del sistema.
- **$diskcompression**: Comprime el disco del sistema.
- **$updatemanagement**: Cambia la forma de gestionar y mejorar las actualizaciones en el sistema.
- **$sosbrowsers**: Optimiza los navegadores web del sistema.

Un ejemplo de cómo lanzar el script con parámetros específicos sería:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

