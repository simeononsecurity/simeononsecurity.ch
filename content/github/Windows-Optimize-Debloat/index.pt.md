---
title: "Otimize seu PC Windows com o Windows-Optimize-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Melhore o desempenho e a privacidade do seu sistema operacional Windows com o Windows-Optimize-Debloat, um script abrangente que ajuda a remover bloatware e otimizar as configurações do sistema."
tags: ["Windows-Optimize-Debloat", "Otimização do Windows", "Desinchando janelas", "Acelerar o Windows", "Otimize o desempenho do Windows", "Aumento de desempenho do Windows", "Otimização do Sistema Windows", "Microsoft", "Privacidade", "Remoção de Bloatware", "Windows 10", "Windows 11", "Windows Defender", "atualização do Windows", "Cortona", "Objetos de política de grupo", "Telemetria", "Loja do Windows", "Windows 10 Profissional", "Início do Windows 10"]
---


[![Test script against windows docker container](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Optimize-Debloat/actions/workflows/test-with-docker.yml)

*Para aqueles que procuram minimizar as instalações do Windows 10 e 11.*

**Observação:** Este script deve funcionar para a maioria, se não todos, os sistemas sem problemas. Enquanto[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensivly, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Não execute este script se você não entender o que ele faz.

## Introdução:
O Windows 10 e 11 são sistemas operacionais invasivos e inseguros prontos para uso.
Organizações como[Microsoft](https://microsoft.com), [PrivacyTools.io](https://PrivacyTools.io) e outros recomendaram alterações de configuração para otimizar e desinchar o sistema operacional Windows 10. Essas alterações incluem bloqueio de telemetria, exclusão de logs e remoção de bloatware, para citar alguns. Este script visa automatizar as configurações recomendadas por essas organizações.

## Notas:
- Este script foi projetado para operação principalmente em ambientes de **uso pessoal**.
- Este script foi projetado de forma que as otimizações, ao contrário de alguns outros scripts, não interrompam a funcionalidade principal do Windows.
 - Recursos como Windows Update, Windows Defender, Windows Store e Cortona foram restritos, mas não estão em um estado disfuncional como a maioria dos outros scripts de privacidade do Windows 10.
- Se você busca um script minimizado direcionado apenas para ambientes comerciais, consulte este[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

## Requisitos:
- [X] Windows 10/11 Enterprise, Windows 10 Professional ou Windows 10 Home
  - O Windows Home não permite configurações de GPO.
    - O script ainda funcionará, mas nem todas as configurações serão aplicadas.
  - As edições do Windows "N" não são testadas.
  - Execute o[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para atualizar e verificar a versão principal mais recente.

## Corrigindo conta da Microsoft ou serviços do Xbox:
Isso ocorre porque bloqueamos o login em contas da Microsoft. A associação de telemetria e identidade da Microsoft é desaprovada.
No entanto, se você ainda deseja usar esses serviços, consulte os seguintes tickets de emissão para a resolução:
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

## Uma lista de scripts e ferramentas que esta coleção utiliza:
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Foram consideradas configurações adicionais de:
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

## Como executar o script:
### Instalação automatizada:
O script pode ser iniciado a partir do download extraído do GitHub assim:
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

