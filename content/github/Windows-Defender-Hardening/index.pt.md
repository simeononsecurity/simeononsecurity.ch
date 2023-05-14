---
title: "Aprimorando a segurança do Windows 10 com o script Defender Hardening"
date: 2020-11-15
toc: true
draft: false
description: "Saiba como aprimorar a segurança do Windows 10 com um script do PowerShell que protege o Windows Defender Antivirus, implementando todos os requisitos do Windows Defender Antivirus STIG V2R1."
tags: ["Windows Defender", "Windows 10", "Segurança do Windows 10", "Script do PowerShell", "Endurecimento", "Endurecimento Defensor", "Automação de segurança", "Conformidade", "Acesso a pastas controladas", "Sistema de Prevenção de Intrusão", "Controle de aplicativos", "Redução da Superfície de Ataque", "Proteções contra exploits", "Proteções fornecidas na nuvem", "Proteções de rede", "Script STIG do Windows Defender", "Windows Defender STIG", "Windows Defender Antivírus STIG V2R1", "WDAC", "ASR"]
---


## O que esse script faz?
- Habilita proteções fornecidas pela nuvem
- Habilita o acesso a pastas controladas
- Habilita proteções de rede
- Habilita o Sistema de Prevenção de Intrusão
-[Enables Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control)
-[Enables Windows Defender Attack Surface Reduction Rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction)
-[Enables Windows Defender Exploit Protections](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-exploit-protection?view=o365-worldwide#powershell)
- Implementa todos os requisitos listados no[Windows Defender Antivirus STIG V2R1](https://dl.cyber.mil/stigs/zip/U_MS_Windows_Defender_Antivirus_V2R1_STIG.zip)

## Requisitos:
- [x] Windows 10 Enterprise (**Preferencial**) ou Windows 10 Professional
  - O Windows 10 Home não permite configurações de GPO ou[ASR](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/attack-surface-reduction) 
Embora a maioria dessas configurações ainda se aplique.
  - As edições do Windows 10 "N" não são testadas.

## Baixe os arquivos necessários:

Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)

## Como executar o script:

**O script pode ser iniciado a partir do download extraído do GitHub assim:**
```
.\sos-windowsdefenderhardening.ps1
```
