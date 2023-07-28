---
title: "Automatización del cumplimiento de las STIG de Windows 10 con un script de Powershell"
date: 2020-08-26
---

**Descargue todos los archivos necesarios de la página [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Buscamos ayuda para lo siguiente [.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introducción:

Windows 10 es inseguro sistema operativo fuera de la caja y requiere muchos cambios para asegurar [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) cumplimiento.
Organizaciones como [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) han recomendado y exigido cambios de configuración para bloquear, endurecer y asegurar el sistema operativo y garantizar el cumplimiento de la normativa gubernamental. Estos cambios abarcan una amplia gama de mitigaciones, como el bloqueo de la telemetría, las macros, la eliminación del bloatware y la prevención de muchos ataques físicos a un sistema.

Los sistemas autónomos son algunos de los más difíciles y molestos de proteger. Cuando no están automatizados, requieren cambios manuales de cada STIG/SRG. Un total de más de 1000 cambios de configuración en un despliegue típico y una media de 5 minutos por cambio equivalen a 3,5 días de trabajo. Este script pretende acelerar ese proceso significativamente.

## Notas:

- Este script está diseñado para operar en entornos **Empresariales** y asume que usted tiene soporte de hardware para todos los requerimientos.
  - Para sistemas personales por favor vea esto [GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Este script no está diseñado para llevar un sistema al 100% de cumplimiento, más bien debe ser utilizado como un trampolín para completar la mayoría, si no todos, los cambios de configuración que pueden ser guionizados.
  - Menos la documentación del sistema, esta colección debería llevarle a un 95% de cumplimiento en todos los STIGS/SRGs aplicados.

## Requisitos:
- [X] Windows 10 Enterprise es **Requerido** por STIG.
- [x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para un dispositivo Windows 10 altamente seguro
- [x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Actualmente Windows 10 **v1909** o **v2004**.
  - Ejecute el [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para actualizar y verificar la última versión principal.
- Requisitos de hardware
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  - [Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## Material de lectura recomendado:
  - [System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  - [System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  - [Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  - [Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  - [Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  - [Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Una lista de scripts y herramientas que utiliza esta colección:

- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

- [NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Se consideraron configuraciones adicionales de:

- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs Aplicados:
 
- [Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

- [Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

- [Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

- [Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

- [Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

- [Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

- [Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

- [Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

- [Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

- [Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

- [Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - Trabajo en curso

- [Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Cómo ejecutar el script

**El script puede ser descargado desde GitHub de la siguiente manera
```
.\secure-standalone.ps1
```
El script que vamos a utilizar debe lanzarse desde el directorio que contiene todos los demás archivos de la carpeta [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
