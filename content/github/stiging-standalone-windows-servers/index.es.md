---
title: "Automatización del cumplimiento de las STIG de Windows Server con scripts de STIG"
date: 2020-09-09
---

**Descargue todos los archivos necesarios de la página [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Nota:** Este script debería funcionar en la mayoría, si no en todos, los sistemas sin problemas. Aunque [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No ejecute este script si no entiende lo que hace. Es su responsabilidad revisar y probar el script antes de ejecutarlo.

## Ansible:
Ahora ofrecemos una colección de playbooks para este script. Consulte lo siguiente:
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introducción:

Windows 10 es inseguro sistema operativo fuera de la caja y requiere muchos cambios para asegurar [FISMA](https://www.cisa.gov/federal-information-security-modernization-act) cumplimiento.
Organizaciones como [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) han recomendado y exigido cambios de configuración para bloquear, endurecer y asegurar el sistema operativo y garantizar el cumplimiento de la normativa gubernamental. Estos cambios abarcan una amplia gama de mitigaciones, como el bloqueo de la telemetría, las macros, la eliminación del bloatware y la prevención de muchos ataques físicos a un sistema.

Los sistemas autónomos son algunos de los más difíciles y molestos de proteger. Cuando no están automatizados, requieren cambios manuales de cada STIG/SRG. Un total de más de 1000 cambios de configuración en un despliegue típico y una media de 5 minutos por cambio equivalen a 3,5 días de trabajo. Este script pretende acelerar ese proceso significativamente.

## Notas:

- Este script está diseñado para operar en entornos **Empresariales** y asume que usted tiene soporte de hardware para todos los requerimientos.
  - Para sistemas personales por favor vea esto [GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Este script no está diseñado para llevar un sistema al 100% de cumplimiento, más bien debe ser utilizado como un trampolín para completar la mayoría, si no todos, los cambios de configuración que pueden ser guionizados.
  - Menos la documentación del sistema, esta colección debería llevarle a un 95% de cumplimiento en todos los STIGS/SRGs aplicados.

## Requisitos:
- [X] Se requiere Windows 10 Enterprise por STIG.
- [X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para un dispositivo Windows 10 altamente seguro
- [X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Ejecute el [Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para actualizar y verificar la última versión mayor.
- X] Bitlocker debe ser suspendido o desactivado antes de implementar este script, puede ser activado de nuevo después de reiniciar.
  - Las siguientes ejecuciones de este script pueden realizarse sin desactivar bitlocker.
- X] Requisitos de hardware
  - [Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  - [Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
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
- [Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
- [Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Se consideraron configuraciones adicionales de:
- [Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

## STIGS/SRGs Applied:
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Editar políticas en la Política de Grupo Local después del hecho:
- Importar las definiciones de políticas ADMX desde [repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) en *C:\windows\PolicyDefinitions* en el sistema que está intentando modificar.
- Abrir ```gpedit.msc``` en el sistema que intentas modificar.


## Cómo ejecutar el script:
### Instalación automatizada:
El script puede ser lanzado desde la descarga extraída de GitHub así:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Instalación manual:
Si se descarga manualmente, la secuencia de comandos debe iniciarse desde el directorio que contiene todos los demás archivos de la [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

Todos los parámetros del script "secure-standalone.ps1" son opcionales, con un valor por defecto de $true. Esto significa que si no se especifica ningún valor para un parámetro cuando se ejecuta el script, se tratará como si estuviera establecido en $true.

El script toma los siguientes parámetros, todos ellos opcionales y por defecto $true si no se especifican:

- **cleargpos**: (Boolean) Borrar los GPO que no se estén utilizando.
- instalaractualizaciones**: (Booleano) Instalar actualizaciones y reiniciar si es necesario.
- **adobe**: (Booleano) STIG Adobe Reader
- **firefox**: (Booleano) STIG Firefox
- **chrome**: (Booleano) STIG Chrome
- **IE11**: (Booleano) STIG Internet Explorer 11
- **edge**: (booleano) STIG Edge
- **dotnet**: (Booleano) STIG .NET Framework
- **office**: (booleano) STIG Office
- **onedrive**: (booleano) STIG OneDrive
- java**: (booleano) STIG Java
- Windows**: (booleano) STIG Windows
- **defender**: (Booleano) STIG Windows Defender
- cortafuegos**: (Booleano) STIG Windows Firewall
- **mitigaciones**: (Booleano) Mitigaciones STIG
- **nessusPID**: (Booleano) Resolver cadenas no entrecomilladas en ruta
- **horizon**: (Booleano) STIG VMware Horizon
- **sosopcional**: (Booleano) Elementos opcionales de STIG/Hardening

Un ejemplo de cómo ejecutar el script con todos los parámetros por defecto sería:

```powershell
.\secure-standalone.ps1
```
Si desea especificar un valor diferente para uno o más de los parámetros, puede incluirlos en el comando junto con su valor deseado. Por ejemplo, si desea ejecutar el script y establecer el parámetro $firefox en $false, el comando sería:

```powershell
.\secure-standalone.ps1 -firefox $false
```

También puede especificar varios parámetros en el comando de la siguiente manera:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Tenga en cuenta que, en este ejemplo, tanto los parámetros de Firefox como los de Chrome tienen el valor $false.



