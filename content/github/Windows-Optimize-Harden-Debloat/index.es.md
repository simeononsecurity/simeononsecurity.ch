---
title: "Optimice y endurezca su sistema Windows con el script Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Esta completa guía brinda instrucciones paso a paso sobre cómo optimizar, fortalecer y eliminar la carga de su sistema Windows para mejorar el rendimiento, la seguridad y la privacidad."
tags: ["optimización de Windows", "Endurecimiento de ventanas", "Deshinchamiento de Windows", "seguridad de windows", "Rendimiento de Windows", "Privacidad de Windows", "actualizaciones de windows", "Objetos de directiva de grupo", "lector Adobe Acrobat", "Firefox", "Google Chrome", "explorador de Internet", "Borde de cromo de Microsoft", "red de puntos 4", "oficina de microsoft", "Onedrive", "Oracle Java JRE 8", "firewall de Windows", "Defensor de Windows", "bloqueador de aplicaciones"]
---
 Introducción:

Windows 10 y Windows 11 son sistemas operativos invasivos e inseguros listos para usar.
Organizaciones como[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) tienen cambios de configuración recomendados para bloquear, fortalecer y proteger el sistema operativo. Estos cambios cubren una amplia gama de mitigaciones, incluido el bloqueo de telemetría, macros, la eliminación de bloatware y la prevención de muchos ataques digitales y físicos en un sistema. Este script tiene como objetivo automatizar las configuraciones recomendadas por esas organizaciones.

## Notas, advertencias y consideraciones:

**ADVERTENCIA:**

Este script debería funcionar para la mayoría de los sistemas, si no todos, sin problemas. Mientras[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Este script está diseñado para funcionar principalmente en entornos de **Uso personal**. Con eso en mente, ciertas opciones de configuración empresarial no están implementadas. Este script no está diseñado para llevar un sistema al 100% de cumplimiento. Más bien, debe usarse como un trampolín para completar la mayoría, si no todos, los cambios de configuración que se pueden programar mientras se saltan problemas pasados como la marca y los banners que no deben implementarse incluso en un entorno de uso personal reforzado.
- Este script está diseñado de tal manera que las optimizaciones, a diferencia de otros scripts, no interrumpirán la funcionalidad principal de Windows.
- Funciones como Windows Update, Windows Defender, Windows Store y Cortona se han restringido, pero no se encuentran en un estado disfuncional como la mayoría de los otros scripts de privacidad de Windows 10.
- Si busca una secuencia de comandos minimizada dirigida solo a entornos comerciales, consulte esto[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**No ejecute este script si no entiende lo que hace. Es su responsabilidad revisar y probar el script antes de ejecutarlo.**

**POR EJEMPLO, LO SIGUIENTE SE ROMPERÁ SI UTILIZA ESTO SIN TOMAR MEDIDAS PREVENTIVAS:**

- El uso de la cuenta de administrador predeterminada llamada "Administrador" está deshabilitado y renombrado por DoD STIG

  - No se aplica a la cuenta predeterminada creada, pero sí se aplica al uso de la cuenta de administrador predeterminada que se encuentra a menudo en las versiones Enterprise, IOT y Windows Server

  - Cree una nueva cuenta en Administración de equipos y configúrela como administrador si lo desea. Luego, copie el contenido de la carpeta de usuarios anteriores en la nueva después de iniciar sesión en el nuevo usuario por primera vez para solucionar esto antes de ejecutar el script.

- El inicio de sesión con una cuenta de Microsoft está deshabilitado por DoD STIG.

  - Cuando intente ser seguro y privado, no se recomienda iniciar sesión en su cuenta local a través de una cuenta de Microsoft. Esto se aplica mediante este repositorio.

  - Cree una nueva cuenta en Administración de equipos y configúrela como administrador si lo desea. Luego, copie el contenido de la carpeta de usuarios anteriores en la nueva después de iniciar sesión en el nuevo usuario por primera vez para solucionar esto antes de ejecutar el script.

- Los PIN de cuenta están deshabilitados por DoD STIG

  - Los PIN son inseguros cuando se usan únicamente en lugar de una contraseña y se pueden eludir fácilmente en cuestión de horas o incluso segundos o minutos.

  - Elimine el pin de la cuenta y/o inicie sesión con la contraseña después de ejecutar el script.

- Los valores predeterminados de Bitlocker se cambiaron y endurecieron debido a DoD STIG.

  - Debido a cómo se implementa BitLocker, cuando se produzcan estos cambios y si ya tiene habilitado BitLocker, se romperá la implementación de BitLocker.

  - Deshabilite BitLocker, ejecute el script y luego vuelva a habilitar BitLocker para solucionar este problema.

## Requisitos:

- [x] Windows 10/11 Enterprise (**Preferido**) o Profesional
  - Las ediciones de Windows 10/11 Home no admiten configuraciones de GPO y no se han probado.
  - Las ediciones de la ventana "N" no se prueban.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para un dispositivo Windows 10 altamente seguro
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Ejecutar el[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para actualizar y verificar la última versión importante.
- [x] Bitlocker debe suspenderse o apagarse antes de implementar este script, se puede volver a habilitar después de reiniciar.
  - Las ejecuciones de seguimiento de este script se pueden ejecutar sin deshabilitar BitLocker.
- [x] Requisitos de hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Material de lectura recomendado:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Adiciones, cambios notables y correcciones de errores:

**Este script agrega, elimina y cambia la configuración de su sistema. Revise el script antes de ejecutarlo.**

### Navegadores:

- Los navegadores tendrán extensiones adicionales instaladas para ayudar en la privacidad y la seguridad.
  - Ver[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) para informacion adicional.
- Debido a las STIG del Departamento de Defensa implementadas para los navegadores, se establecen la administración de extensiones y otras configuraciones empresariales. Para obtener instrucciones sobre cómo ver estas opciones, deberá consultar las instrucciones de GPO a continuación.

### Módulos Powershell:

- Para ayudar a automatizar las actualizaciones de Windows, PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) El módulo se agregará a su sistema.

### Corrección de la cuenta de Microsoft, la tienda o los servicios de Xbox:

Esto se debe a que bloqueamos el inicio de sesión en las cuentas de Microsoft. La asociación de telemetría e identidad de Microsoft está mal vista.
Sin embargo, si aún desea utilizar estos servicios, consulte los siguientes tickets de emisión para la resolución:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Edición de políticas en la Política de grupo local después del hecho:

Si necesita modificar o cambiar una configuración, lo más probable es que se pueda configurar a través de GPO:

- Importe las definiciones de la política ADMX de este[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) en _C:\windows\PolicyDefinitions_ en el sistema que está tratando de modificar.

- Abra `gpedit.msc` en el sistema que está tratando de modificar.

## Una lista de scripts y herramientas que utiliza esta colección:

### Primera fiesta:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Tercero:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG aplicados:

-[Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
-[Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
-[Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
-[Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
-[Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
-[Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
-[Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
-[Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
-[Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/)
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Se consideraron configuraciones adicionales de:

-[BuiltByBel - PrivateZilla](https://github.com/builtbybel/privatezilla)
-[CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
-[Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
-[MelodysTweaks - Basic Tweaks](https://sites.google.com/view/melodystweaks/basictweaks)
-[Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
-[Microsoft - Reduce attack surfaces with attack surface reduction rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
-[Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
-[Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[Mirinsoft - SharpApp](https://github.com/builtbybel/sharpapp)
-[Mirinsoft - debotnet](https://github.com/builtbybel/debotnet)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)
-[UnderGroundWires - Privacy.S\*\*Y](https://github.com/undergroundwires/privacy.sexy)
-[Sycnex - Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
-[The-Virtual-Desktop-Team - Virtual-Desktop-Optimization-Tool](https://github.com/The-Virtual-Desktop-Team/Virtual-Desktop-Optimization-Tool)
-[TheVDIGuys - Windows 10 VDI Optimize](https://github.com/TheVDIGuys/Windows_10_VDI_Optimize)
-[VectorBCO - windows-path-enumerate](https://github.com/VectorBCO/windows-path-enumerate)
-[W4H4WK - Debloat Windows 10](https://github.com/W4RH4WK/Debloat-Windows-10/tree/master/scripts)
-[Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## Cómo ejecutar el script:
### GUI - Instalación guiada:

Descargar la última versión[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)elige las opciones que quieras y presiona ejecutar. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Ejemplo de instalación guiada basada en GUI de Windows-Optimize-Harden-Debloat"> ### Instalación automatizada: utilice este resumen para descargar automáticamente, descomprimir todos los archivos compatibles y ejecutar la última versión del script.```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/windowsoptimizeandharden.ps1'|iex
```

<img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/w10automatic.gif" alt="Example of 
Windows-Optimize-Harden-Debloat automatic install">

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

The script "sos-optimize-windows.ps1" includes several parameters that allow for customization of the optimization process. Each parameter is a boolean value that defaults to true if not specified.

- **cleargpos**: Clears Group Policy Objects settings.
- **installupdates**: Installs updates to the system.
- **adobe**: Implements the Adobe Acrobat Reader STIGs.
- **firefox**: Implements the FireFox STIG.
- **chrome**: Implements the Google Chrome STIG.
- **IE11**: Implements the Internet Explorer 11 STIG.
- **edge**: Implements the Microsoft Chromium Edge STIG.
- **dotnet**: Implements the Dot Net 4 STIG.
- **office**: Implements the Microsoft Office Related STIGs.
- **onedrive**: Implements the Onedrive STIGs.
- **java**: Implements the Oracle Java JRE 8 STIG.
- **windows**: Implements the Windows Desktop STIGs.
- **defender**: Implements the Windows Defender STIG.
- **firewall**: Implements the Windows Firewall STIG.
- **mitigations**: Implements General Best Practice Mitigations.
- **defenderhardening**: Implements and Hardens Windows Defender Beyond STIG Requirements.
- **pshardening**: Implements PowerShell Hardening and Logging.
- **sslhardening**: Implements SSL Hardening.
- **smbhardening**: Hardens SMB Client and Server Settings.
- **applockerhardening**: Installs and Configures Applocker (In Audit Only Mode).
- **bitlockerhardening**: Harden Bitlocker Implementation.
- **removebloatware**: Removes unnecessary programs and features from the system.
- **disabletelemetry**: Disables data collection and telemetry.
- **privacy**: Makes changes to improve privacy.
- **imagecleanup**: Cleans up unneeded files from the system.
- **nessusPID**: Resolves Unquoted System Strings in Path.
- **sysmon**: Installs and configures sysmon to improve auditing capabilities.
- **diskcompression**: Compresses the system disk.
- **emet**: Implements STIG Requirements and Hardening for EMET on Windows 7 Systems.
- **updatemanagement**: Changes the way updates are managed and improved on the system.
- **deviceguard**: Enables Device Guard Hardening.
- **sosbrowsers**: Optimizes the system's web browsers.

An example of how to launch the script with specific parameters would be:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
powershell.exe -ExecutionPolicy ByPass -File .\sos-optimize-windows.ps1 -cleargpos:$false -installupdates:$false
```
