---
title: "Guía Completa para Endurecer Windows con Windows Defender..."
date: 2020-12-16
toc: true
draft: false
description: Aprenda a usar Windows Defender Application Control WDAC para endurecer su sistema operativo Windows con scripts y herramientas.
tags:
- Endurecimiento de Windows Defender Application Control WDAC
- PowerShell
- Script de PowerShell
- Automatización
- Cumplimiento
- Equipo Azul
- Script STIG de Windows Defender
- Endurecimiento de Windows Defender
- STIG de Windows Defender
- STIG de Defender
- Protección contra Explotaciones de Windows Defender WDEP
- Reducción de Superficie de Ataque de Windows Defender ASR
- Windows Server 2016 2019
- Windows Server Core
- Microsoft WDAC-Toolkit
- Actualizar Política CI
- Reglas de bloqueo recomendadas por Microsoft
- Reglas de bloqueo de controladores recomendadas por Microsoft
- Políticas XML
- Políticas BIN
- Directiva de Grupo
- Microsoft Intune
cover: /img/cover/Windows-Defender-Application-Control-Hardening.webp
coverAlt: Una ilustración de una sala de servidores futurista con pantallas brillantes que muestran estructuras de archivos XML y BIN relacionadas con Windows Defender Application Control. El fondo oscuro realza los colores vibrantes.
coverCaption: ''
lastmod: 2026-10-08
---

**Endurecer Windows con Windows Defender Application Control WDAC**

## Notas:
- Windows Server 2016/2019 o cualquier versión anterior a la 1903 solo soporta una política heredada a la vez.
- La edición Windows Server Core soporta [WDAC](https://simeononsecurity.com/til/2022-05-18/) pero algunos componentes que dependen de AppLocker no funcionarán
- Por favor lea la [Lectura Recomendada](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) antes de implementar o incluso probar.

## Una lista de scripts y herramientas que utiliza esta colección:

- [MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
- [Microsoft - Actualizar Política CI](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Configuraciones adicionales consideradas de:

- [Microsoft - Reglas de bloqueo recomendadas](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
- [Microsoft - Reglas de bloqueo de controladores recomendadas](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
- [Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explicación:

### XML vs. BIN:

- En pocas palabras, las políticas **"XML"** son para aplicar localmente en una máquina y los archivos **"BIN"** son para hacerlas cumplir mediante [Directiva de Grupo](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) o [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune). Aunque puede usar políticas XML, BIN o CIP en una implementación local, generalmente debería usar XML cuando sea posible y especialmente durante auditorías o solución de problemas.

### Descripciones de Políticas:

- **Políticas Predeterminadas**
  - Las políticas "Predeterminadas" usan solo las funciones predeterminadas disponibles en WDAC-Toolkit.
- **Políticas Recomendadas**
  - Las políticas "Recomendadas" usan las funciones predeterminadas, además de las [reglas de bloqueo](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) y [bloqueo de controladores](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) recomendadas por Microsoft.
- **Políticas de Auditoría**
  - Las políticas "Auditoría" solo registran excepciones a las reglas. Esto es para pruebas en su entorno, lo que le permite modificar las políticas libremente según las necesidades de su entorno.
- **Políticas Aplicadas**
  - Las políticas "Aplicadas" no permiten excepciones a las reglas. Aplicaciones, controladores, dlls y otros elementos serán bloqueados si no cumplen.

### Políticas Disponibles:

- **XML:**
  - **Solo Auditoría:**
    - `WDAC_V1_Default_Audit_{version}.xml`
    - `WDAC_V1_Recommended_Audit_{version}.xml`
  - **Aplicadas:**
    - `WDAC_V1_Default_Enforced_{version}.xml`
    - `WDAC_V1_Recommended_Enforced_{version}.xml`
- **BIN:**
  - **Solo Auditoría:**
    - `WDAC_V1_Default_Audit_{version}.bin`
    - `WDAC_V1_Recommended_Audit_{version}.bin`
  - **Aplicadas:**
    - `WDAC_V1_Default_Enforced_{version}.bin`
    - `WDAC_V1_Recommended_Enforced_{version}.bin`
- **CIP:**
  - **Solo Auditoría:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Aplicadas:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Actualice la siguiente línea en el script para usar la política que desee localmente:

```powershell
$PolicyPath = "C:\temp\Windows Defender\CIP\WDAC_V1_Recommended_Enforced\*.cip"
#https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script
ForEach ($Policy in (Get-ChildItem -Recurse $PolicyPath).Fullname) {
  $PolicyBinary = "$Policy"
  $DestinationFolder = $env:windir+"\System32\CodeIntegrity\CIPolicies\Active\"
  $RefreshPolicyTool = "./Files/EXECUTABLES/RefreshPolicy(AMD64).exe"
  Copy-Item -Path $PolicyBinary -Destination $DestinationFolder -Force
  & $RefreshPolicyTool
}
```

Alternativamente, puede usar [Directiva de Grupo](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) o [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) para aplicar las políticas WDAC.

## Auditoría:

Puede ver los registros de eventos WDAC en el visor de eventos bajo:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Lectura Recomendada:

- [Argonsys - Implementación de la Política de Control de Aplicaciones de Windows 10](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Auditar Políticas de Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Crear una política WDAC para dispositivos de carga fija usando un equipo de referencia](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Implementar políticas de Windows Defender Application Control usando Directiva de Grupo](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Implementar políticas de Windows Defender Application Control usando Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Implementar políticas WDAC usando script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Aplicar Políticas de Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guía para Crear Políticas de Denegación WDAC](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Usar múltiples Políticas de Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## Cómo ejecutar el script:

### Instalación Manual:

Si se descarga manualmente, el script debe ejecutarse desde un PowerShell con privilegios administrativos en el directorio que contenga todos los archivos del [Repositorio GitHub](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
