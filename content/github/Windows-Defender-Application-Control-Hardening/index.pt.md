---
title: "Guia completo para proteger o Windows com o Windows Defender Application Control WDAC"
date: 2020-12-16
toc: true
draft: false
description: "Aprenda a usar o Windows Defender Application Control WDAC para fortalecer seu sistema operacional Windows com scripts e ferramentas."
tags: ["Proteção de WDAC de controle de aplicativos do Windows Defender", "PowerShell", "Script do PowerShell", "Automação", "Conformidade", "Time azul", "Script STIG do Windows Defender", "Endurecimento do Windows Defender", "Windows Defender STIG", "Defensor STIG", "Windows Defender Exploit Protection WDEP", "ASR de redução da superfície de ataque do Windows Defender", "WindowsServer 2016 2019", "Núcleo do Windows Server", "Microsoft WDAC-Toolkit", "Atualizar política de IC", "Regras de bloqueio recomendadas pela Microsoft", "Regras de bloqueio de driver recomendadas pela Microsoft", "políticas XML", "Políticas de BIN", "Política de grupo", "Microsoft Intune"]
---

**Proteja o Windows com o Windows Defender Application Control WDAC**

## Notas:
- O Windows Server 2016/2019 ou qualquer versão anterior à 1903 oferece suporte apenas a uma única política herdada por vez.
- A edição Windows Server Core suporta WDAC, mas alguns componentes que dependem do AppLocker não funcionarão
- Por favor, leia o[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) antes de implementar ou mesmo testar.

## Uma lista de scripts e ferramentas que esta coleção utiliza:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## Foram consideradas configurações adicionais de:

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

## Explicação:

### XML vs. BIN:

- Simplificando, as políticas **"XML"** são para aplicar a uma máquina localmente e os arquivos **"BIN"** são para aplicá-los com[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) Embora você possa usar políticas XML, BIN ou CIP em uma implantação local, em geral, você deve se ater ao XML sempre que possível e especialmente durante a auditoria ou solução de problemas.

### Descrições da política:

- **Políticas Padrão:**
  - As políticas "Padrão" usam apenas os recursos padrão disponíveis no WDAC-Toolkit.
- **Políticas recomendadas:**
  - As políticas "Recomendado" usam os recursos padrão, bem como os recomendados pela Microsoft[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) regras.
- **Políticas de Auditoria:**
  - As políticas de "Auditoria", apenas registram exceções às regras. Isso é para teste em seu ambiente, para que você possa modificar as políticas, à vontade, para atender às necessidades de seus ambientes.
- **Políticas aplicadas:**
  - As políticas "Aplicadas" não permitirão nenhuma exceção às regras, aplicativos, drivers, dlls, etc. serão bloqueados se não cumprirem.

### Políticas Disponíveis:

- **XML:**
  - **Somente auditoria:**
    - `WDAC_V1_Default_Audit_{versão}.xml`
    - `WDAC_V1_Recommended_Audit_{versão}.xml`
  - **Aplicado:**
    - `WDAC_V1_Default_Enforced_{versão}.xml`
    - `WDAC_V1_Recommended_Enforced_{versão}.xml`
- **BIN:**
  - **Somente auditoria:**
    - `WDAC_V1_Default_Audit_{versão}.bin`
    - `WDAC_V1_Recommended_Audit_{versão}.bin`
  - **Aplicado:**
    - `WDAC_V1_Default_Enforced_{versão}.bin`
    - `WDAC_V1_Recommended_Enforced_{versão}.bin`
- **CIP:**
  - **Somente auditoria:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommended_Audit\{uid}.cip`
  - **Aplicado:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

Atualize a seguinte linha no script para usar a política que você deseja localmente:

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

Alternatively, you may use [Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) to enforce the WDAC policies.

## Auditing:

You can view the WDAC event logs in event viewer under:

`Applications and Services Logs\Microsoft\Windows\CodeIntegrity\Operational`

## Recommended Reading:

- [Argonsys - Deploying Windows 10 Application Control Policy](https://argonsys.com/microsoft-cloud/library/deploying-windows-10-application-control-policy/)
- [Microsoft - Audit Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/audit-windows-defender-application-control-policies)
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy)
- [Microsoft - Deploy Windows Defender Application Control policies by using Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Enforce Windows Defencer Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/enforce-windows-defender-application-control-policies)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

## How to run the script:

### Manual Install:

If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening/archive/main.zip)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-wdachardening.ps1
```
