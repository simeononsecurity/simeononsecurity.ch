---
title: "Mejora de la seguridad de Windows 10 con Defender Hardening Script"
date: 2020-11-15
toc: true
draft: false
description: "Aprenda a mejorar la seguridad de Windows 10 con un script de PowerShell que fortalece Windows Defender Antivirus, implementando todos los requisitos de Windows Defender Antivirus STIG V2R1."
tags: ["Defensor de Windows", "ventanas 10", "Seguridad de Windows 10", "Guión de PowerShell", "Endurecimiento", "Endurecimiento del defensor", "Automatización de seguridad", "Cumplimiento", "Acceso controlado a carpetas", "Sistema de Prevención de Intrusión", "Control de aplicaciones", "Reducción de superficie de ataque", "Protecciones contra exploits", "Protecciones entregadas en la nube", "Protecciones de red", "Secuencia de comandos STIG de Windows Defender", "STIG de Windows Defender", "Antivirus de Windows Defender STIG V2R1", "WDAC", "ASR"]
---


## ¿Qué hace este script?
- Habilita las protecciones entregadas en la nube
- Habilita el acceso controlado a carpetas
- Habilita las protecciones de red
- Habilita el Sistema de Prevención de Intrusos
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implementa todos los requisitos enumerados en el[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Requisitos:
- [x] Windows 10 Enterprise (**Preferido**) o Windows 10 Professional
  - Windows 10 Home no permite configuraciones GPO o[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Aunque la mayoría de estas configuraciones aún se aplicarán.
  - Las ediciones "N" de Windows 10 no se prueban.

## Descargue los archivos necesarios:

Descargue los archivos necesarios de la[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Cómo ejecutar el script:

**El script se puede iniciar desde la descarga de GitHub extraída de esta manera:**
```
.\sos-windowsdefenderhardening.ps1
```
