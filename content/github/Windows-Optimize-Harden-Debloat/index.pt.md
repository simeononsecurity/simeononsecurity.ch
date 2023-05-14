---
title: "Otimize e proteja seu sistema Windows com o script Windows-Optimize-Harden-Debloat"
date: 2020-12-29
toc: true
draft: false
description: "Este guia abrangente fornece instruções passo a passo sobre como otimizar, proteger e desinchar seu sistema Windows para melhorar o desempenho, a segurança e a privacidade."
tags: ["Otimização do Windows", "Endurecimento do Windows", "Desinchaço do Windows", "Segurança do Windows", "Desempenho do Windows", "Privacidade do Windows", "atualizações do Windows", "Objetos de política de grupo", "Adobe acrobat reader", "Raposa de fogo", "Google Chrome", "Internet Explorer", "Microsoft Chromium Edge", "Ponto Net 4", "Microsoft Office", "Onedrive", "OracleJava JRE 8", "Firewall do Windows", "Windows Defender", "AppLocker"]
---
 Introdução:

O Windows 10 e o Windows 11 são sistemas operacionais invasivos e inseguros prontos para uso.
Organizações como[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) recomendaram alterações de configuração para bloquear, fortalecer e proteger o sistema operacional. Essas alterações abrangem uma ampla gama de mitigações, incluindo bloqueio de telemetria, macros, remoção de bloatware e prevenção de muitos ataques físicos e digitais em um sistema. Este script visa automatizar as configurações recomendadas por essas organizações.

## Notas, Advertências e Considerações:

**AVISO:**

Este script deve funcionar para a maioria dos sistemas, se não todos, sem problemas. Enquanto[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- Este script foi projetado para operação principalmente em ambientes de **uso pessoal**. Com isso em mente, certas definições de configuração corporativa não são implementadas. Este script não foi projetado para levar um sistema a 100% de conformidade. Em vez disso, deve ser usado como um trampolim para concluir a maioria, se não todas, as alterações de configuração que podem ser roteirizadas, ignorando problemas anteriores como branding e banners, nos quais não devem ser implementados, mesmo em um ambiente de uso pessoal rígido.
- Este script foi projetado de forma que as otimizações, ao contrário de alguns outros scripts, não interrompam a funcionalidade principal do Windows.
- Recursos como Windows Update, Windows Defender, Windows Store e Cortona foram restritos, mas não estão em um estado disfuncional como a maioria dos outros scripts de privacidade do Windows 10.
- Se você busca um script minimizado direcionado apenas para ambientes comerciais, consulte este[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**Não execute este script se você não entender o que ele faz. É sua responsabilidade revisar e testar o script antes de executá-lo.**

** POR EXEMPLO, O SEGUINTE QUEBRARÁ SE VOCÊ EXECUTAR ISSO SEM TOMAR MEDIDAS PREVENTIVAS: **

- O uso da conta de administrador padrão chamada "Administrador" é desativado e renomeado por DoD STIG

  - Não se aplica à conta padrão criada, mas se aplica ao uso da conta de administrador padrão frequentemente encontrada nas versões Enterprise, IOT e Windows Server

  - Crie uma nova conta em Gerenciamento do computador e defina-a como administrador, se desejar. Em seguida, copie o conteúdo da pasta de usuários anterior para a nova depois de entrar no novo usuário pela primeira vez para contornar isso antes de executar o script.

- Entrar usando uma conta da Microsoft está desabilitado por DoD STIG.

  - Ao tentar ser seguro e privado, não é recomendável entrar em sua conta local por meio de uma conta da Microsoft. Isso é imposto por este repositório.

  - Crie uma nova conta em Gerenciamento do computador e defina-a como administrador, se desejar. Em seguida, copie o conteúdo da pasta de usuários anterior para a nova depois de entrar no novo usuário pela primeira vez para contornar isso antes de executar o script.

- Os PINs da conta estão desabilitados por DoD STIG

  - Os PINs são inseguros quando usados apenas no lugar de uma senha e podem ser facilmente ignorados em questão de horas ou até mesmo segundos ou minutos

  - Remova o pin da conta e/ou entre usando a senha após executar o script.

- Os padrões do Bitlocker foram alterados e reforçados devido ao DoD STIG.

  - Devido à forma como o bitlocker é implementado, quando essas alterações ocorrerem e se você já tiver o bitlocker ativado, isso interromperá a implementação do bitlocker.

  - Desative o bitlocker, execute o script e reative o bitlocker para solucionar esse problema.

## Requisitos:

- [x] Windows 10/11 Enterprise (**Preferred**) ou Professional
  - As edições do Windows 10/11 Home não oferecem suporte a configurações de GPO e não foram testadas.
  - As edições Window "N" não são testadas.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para um dispositivo Windows 10 altamente seguro
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Execute o[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para atualizar e verificar a versão principal mais recente.
- [x] Bitlocker deve ser suspenso ou desligado antes de implementar este script, ele pode ser ativado novamente após a reinicialização.
  - As execuções de acompanhamento deste script podem ser executadas sem desabilitar o bitlocker.
- [x] Requisitos de Hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## Material de leitura recomendado:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## Adições, mudanças notáveis e correções de bugs:

**Este script adiciona, remove e altera as configurações do seu sistema. Revise o script antes de executá-lo.**

### Navegadores:

- Os navegadores terão extensões adicionais instaladas para auxiliar na privacidade e segurança.
  - Ver[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) para informações adicionais.
- Devido aos STIGs do DoD implementados para navegadores, o gerenciamento de extensões e outras configurações corporativas são definidas. Para obter instruções sobre como ver essas opções, você precisará consultar as instruções do GPO abaixo.

### Módulos Powershell:

- Para auxiliar na automatização das atualizações do Windows, o PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) módulo será adicionado ao seu sistema.

### Consertando conta, loja ou serviços do Xbox da Microsoft:

Isso ocorre porque bloqueamos o login em contas da Microsoft. A associação de telemetria e identidade da Microsoft é desaprovada.
No entanto, se você ainda deseja usar esses serviços, consulte os seguintes tickets de emissão para a resolução:

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### Editando políticas na Política de Grupo Local após o fato:

Se você precisar modificar ou alterar uma configuração, eles provavelmente podem ser configurados via GPO:

- Importe as definições de política ADMX deste[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) em _C:\windows\PolicyDefinitions_ no sistema que você está tentando modificar.

- Abra `gpedit.msc` no sistema que você está tentando modificar.

## Uma lista de scripts e ferramentas que esta coleção utiliza:

### Primeira festa:

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

### Terceiro:

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRGs aplicados:

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

## Foram consideradas configurações adicionais de:

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

## Como executar o script:
### GUI - Instalação guiada:

Baixe a versão mais recente[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)escolha as opções desejadas e clique em executar. <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Exemplo de instalação guiada baseada em Windows-Optimize-Harden-Debloat GUI"> ### Instalação automatizada: use este one-liner para baixar automaticamente, descompactar todos os arquivos de suporte e executar a versão mais recente do script.```powershell
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
