---
title: "Logre el cumplimiento de las STIG: Refuerce la seguridad de los dominios y garantice los requisitos normativos"
date: 2020-09-08
---
 Introducción

En el panorama actual de la ciberseguridad, en rápida evolución, garantizar la seguridad y el cumplimiento de su dominio es de suma importancia. **Cumplir con las STIG (Guías Técnicas de Implementación de Seguridad) y las SRG (Guías de Requisitos de Seguridad) es crucial** para mantener una infraestructura de TI robusta y bien protegida**. En este artículo, exploraremos cómo **la guía completa de SimeonOnSecurity puede ayudarle a lograr el cumplimiento de las STIG** para su dominio, proporcionándole las herramientas y conocimientos necesarios para mejorar su **postura de seguridad**.

## Razonamiento

Con el **número creciente de ciberamenazas y requisitos normativos**, las organizaciones necesitan establecer una sólida **base de seguridad en sus dominios**. Las STIG y SRG ofrecen un conjunto de **directrices y mejores prácticas** para asegurar diversos programas y sistemas. Mediante la aplicación de estas normas, las organizaciones pueden **mitigar los riesgos, proteger los datos sensibles** y garantizar que sus sistemas están **configurados de forma segura**. **El script de preparación de dominios de SimeonOnSecurity reúne una colección de GPO (objetos de directiva de grupo) y configuraciones de fuentes de confianza**, ayudando a las organizaciones a agilizar el proceso de cumplimiento de las STIG.

## Métodos

**El script de preparación de dominios de SimeonOnSecurity proporciona un enfoque completo** para hacer que su dominio cumpla con las STIGs y SRGs aplicables. La guía incluye un script que puede ser ejecutado dentro de un entorno empresarial para aplicar las configuraciones necesarias. Siguiendo estos pasos, puede **automatizar el proceso y ahorrar un valioso tiempo**.

El script importa los GPOs proporcionados por **SimeonOnSecurity**, que han sido **exhaustivamente revisados y probados**. Estos GPOs cubren una amplia gama de software y sistemas, incluyendo **Adobe Acrobat, navegadores web como Firefox y Chrome, Microsoft Office, sistemas operativos Windows**, y más. El script garantiza que las configuraciones se ajusten a las **últimas directrices STIG y SRG**, lo que le ayudará a cumplir las normas de seguridad necesarias.

Además, el script incorpora configuraciones adicionales procedentes de organizaciones acreditadas como **CERT, Microsoft y NSA Cyber**. Estas configuraciones abordan consideraciones de seguridad específicas como **corrupción de memoria, refuerzo de SSL, gestión de telemetría, listas blancas de aplicaciones y seguridad de hardware/firmware**, entre otras.

Al aprovechar el script de preparación de dominios de SimeonOnSecurity, las organizaciones pueden **mejorar la postura de seguridad de sus dominios, reducir las vulnerabilidades** y demostrar el cumplimiento de los reglamentos y normas pertinentes.
________


**Preparación de dominio conforme a STIG
*Importe todos los GPOs proporcionados por SimeonOnSecurity para ayudar a que su dominio cumpla con todos los STIGs y SRGs aplicables.

[![VirusTotal Scan](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/actions/workflows/virustotal.yml)

**Nota:** Este script debería funcionar en la mayoría, si no en todos, los sistemas sin problemas. Aunque [@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) No ejecute este script si no entiende lo que hace.

## Notas:

**Este script está diseñado para su uso en entornos empresariales**

## Ansible:
Ahora ofrecemos una colección de playbooks para este script. Consulte lo siguiente:
- [Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Se consideraron configuraciones adicionales de:
- [CERT - IE Scripting Engine Memory Corruption](https://kb.cert.org/vuls/id/573168/)
- [Dirteam - SSL Hardening](https://dirteam.com/sander/2019/07/30/howto-disable-weak-protocols-cipher-suites-and-hashing-algorithms-on-web-application-proxies-ad-fs-servers-and-windows-servers-running-azure-ad-connect/)
- [Microsoft - Managing Windows 10 Telemetry and Callbacks](https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services)
- [Microsoft - Specture and Meltdown Mitigations](https://support.microsoft.com/en-us/help/4072698/windows-server-speculative-execution-side-channel-vulnerabilities)
- [Microsoft - Windows 10 Privacy](https://docs.microsoft.com/en-us/windows/privacy/)
- [Microsoft - Windows 10 VDI Recomendations](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds_vdi-recommendations-1909)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
- [NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
- [NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
- [Whonix - Disable TCP Timestamps](https://www.whonix.org/wiki/Disable_TCP_and_ICMP_Timestamps)

## STIGS/SRGs Applied:
- [Adobe Acrobat Pro DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Adobe Acrobat Reader DC Continuous V2R1](https://public.cyber.mil/stigs/downloads/)
- [Firefox V5R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
- [Google Chrome V2R4](https://public.cyber.mil/stigs/downloads/)
- [Internet Explorer 11 V1R19](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Edge V1R2](https://public.cyber.mil/stigs/downloads/)
- [Microsoft .Net Framework 4 V1R9](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/.NET-STIG-Script)
- [Microsoft Office 2013 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2016 V2R1](https://public.cyber.mil/stigs/downloads/)
- [Microsoft Office 2019/Office 365 Pro Plus V2R3](https://public.cyber.mil/stigs/downloads/)
- [Microsoft OneDrive STIG V2R1](https://public.cyber.mil/stigs/downloads/)
- [Oracle JRE 8 V1R5](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Oracle-JRE-8-STIG-Script)
- [Windows 10 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Defender Antivirus V2R2](https://public.cyber.mil/stigs/downloads/) - **[Requires Separate Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
- [Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2012(R2) V3R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2016 V2R2](https://public.cyber.mil/stigs/downloads/)
- [Windows Server 2019 V2R2](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Agent V1R1](https://public.cyber.mil/stigs/downloads/)
- [VMWare Horizon Client V1R1](https://public.cyber.mil/stigs/downloads/)


## Uso:
### Script PowerShell:

**El script puede ser lanzado desde la descarga extraída de GitHub así:**
```
.\sos-stig-compliant-domain-prep.ps1
```
El script que vamos a utilizar debe lanzarse desde el directorio que contiene todos los demás archivos de la carpeta [GitHub Repository](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep)


