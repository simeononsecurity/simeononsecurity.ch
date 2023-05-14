---
title: "Optimice su PC con Windows con Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Mejore el rendimiento y la privacidad de su sistema operativo Windows con Windows-Optimize-Debloat, un script integral que ayuda a eliminar el bloatware y optimizar la configuración del sistema."
tags: ["Windows-Optimizar-Desbloquear", "Optimización de Windows", "Deshinchar Windows", "Acelera Windows", "Optimizar el rendimiento de Windows", "Aumento del rendimiento de Windows", "Optimización del sistema de Windows", "microsoft", "Privacidad", "Eliminación de bloatware", "ventanas 10", "ventanas 11", "Defensor de Windows", "actualizacion de Windows", "Cortona", "Objetos de directiva de grupo", "Telemetría", "Tienda Windows", "profesional de Windows 10", "Inicio de Windows 10"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Para aquellos que buscan minimizar sus instalaciones de Windows 10 y 11.*

**Nota:** Este script debería funcionar para la mayoría de los sistemas, si no todos, sin problemas. Mientras[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No ejecute este script si no comprende lo que hace.

## Introducción:
Windows 10 y 11 son sistemas operativos invasivos e inseguros listos para usar.
Organizaciones como[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) y otros han recomendado cambios de configuración para optimizar y desbloquear el sistema operativo Windows 10. Estos cambios incluyen el bloqueo de la telemetría, la eliminación de registros y la eliminación de bloatware, por nombrar algunos. Este script tiene como objetivo automatizar las configuraciones recomendadas por esas organizaciones.

## Notas:
- Este script está diseñado para funcionar principalmente en entornos de **Uso personal**.
- Este script está diseñado de tal manera que las optimizaciones, a diferencia de otros scripts, no interrumpirán la funcionalidad principal de Windows.
 - Funciones como Windows Update, Windows Defender, Windows Store y Cortona se han restringido, pero no se encuentran en un estado disfuncional como la mayoría de los otros scripts de privacidad de Windows 10.
- Si busca una secuencia de comandos minimizada dirigida solo a entornos comerciales, consulte esto[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisitos:
- [X] Windows 10/11 Enterprise, Windows 10 Professional o Windows 10 Home
  - Windows Home no permite configuraciones de GPO.
    - El script seguirá funcionando, pero no se aplicarán todas las configuraciones.
  - Las ediciones de Windows "N" no se prueban.
  - Ejecutar el[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para actualizar y verificar la última versión principal.

## Reparación de la cuenta de Microsoft o los servicios de Xbox:
Esto se debe a que bloqueamos el inicio de sesión en las cuentas de Microsoft. La asociación de telemetría e identidad de Microsoft está mal vista.
Sin embargo, si aún desea utilizar estos servicios, consulte los siguientes tickets de emisión para la resolución:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Una lista de scripts y herramientas que utiliza esta colección:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Se consideraron configuraciones adicionales de:
-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[UnderGroundWires - Privacy.S**Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)

## Cómo ejecutar el script:
### Instalación automática:
El script se puede iniciar desde la descarga de GitHub extraída de esta manera:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeanddebloat.ps1'|iex
```
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **$cleargpos**: Clears Group Policy Objects settings.
- **$installupdates**: Installs updates to the system.
- **$removebloatware**: Removes unnecessary programs and features from the system.
- **$disabletelemetry**: Disables data collection and telemetry.
- **$privacy**: Makes changes to improve privacy.
- **$imagecleanup**: Cleans up unneeded files from the system.
- **$diskcompression**: Compresses the system disk.
- **$updatemanagement**: Changes the way updates are managed and improved on the system.
- **$sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```

