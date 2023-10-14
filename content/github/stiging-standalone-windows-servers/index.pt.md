---
title: "Automatizando a conformidade do Windows Server STIG com scripts STIG"
date: 2020-09-09
---

**Baixe todos os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Observação:** Este script deve funcionar para a maioria, se não todos, os sistemas sem problemas. Enquanto[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues) Não execute este script se você não entender o que ele faz. É sua responsabilidade revisar e testar o script antes de executá-lo.

## Ansible:
Agora oferecemos uma coleção de manuais para este script. Consulte o seguinte:
-[Github Repo](https://github.com/simeononsecurity/Windows_STIG_Ansible)
-[Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Introdução:

O Windows 10 é um sistema operacional inseguro pronto para uso e requer muitas alterações para garantir[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) conformidade.
Organizações como[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) recomendaram e exigiram alterações de configuração para bloquear, fortalecer e proteger o sistema operacional e garantir a conformidade do governo. Essas alterações abrangem uma ampla gama de mitigações, incluindo bloqueio de telemetria, macros, remoção de bloatware e prevenção de muitos ataques físicos em um sistema.

Os sistemas autônomos são alguns dos sistemas mais difíceis e irritantes de proteger. Quando não automatizados, requerem alterações manuais de cada STIG/SRG. Totalizando mais de 1.000 alterações de configuração em uma implantação típica e uma média de 5 minutos por alteração, o que equivale a 3,5 dias de trabalho. Este script visa acelerar significativamente esse processo.

## Notas:

- Este script foi projetado para operação em ambientes **Enterprise** e pressupõe que você tenha suporte de hardware para todos os requisitos.
  - Para sistemas pessoais, consulte isto[GitHub Repository](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)
- Este script não foi projetado para levar um sistema a 100% de conformidade, mas deve ser usado como um trampolim para concluir a maioria, se não todas, as alterações de configuração que podem ser roteirizadas.
  - Menos a documentação do sistema, esta coleção deve trazer até cerca de 95% de conformidade em todos os STIGS/SRGs aplicados.

## Requisitos:
- [X] Windows 10 Enterprise é necessário por STIG.
-[X] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para um dispositivo Windows 10 altamente seguro
-[X] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Execute o[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para atualizar e verificar a versão principal mais recente.
- [X] Bitlocker deve ser suspenso ou desligado antes de implementar este script, ele pode ser ativado novamente após a reinicialização.
  - As execuções de acompanhamento deste script podem ser executadas sem desabilitar o bitlocker.
- [X] Requisitos de hardware
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

## Uma lista de scripts e ferramentas que esta coleção utiliza:
-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

## Foram consideradas configurações adicionais de:
-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)
-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)
-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)
-[NSACyber - Windows Secure Host Baseline](https://github.com/nsacyber/Windows-Secure-Host-Baseline)

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
-[Windows Firewall V1R7](https://public.cyber.mil/stigs/downloads/)

## Editando políticas na Política de Grupo Local após o fato:
- Importe as definições de política ADMX deste[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) em *C:\windows\PolicyDefinitions* no sistema que você está tentando modificar.
- Abrir```gpedit.msc``` on on the system you're trying to modify. 


## How to run the script:
### Automated Install:
The script may be launched from the extracted GitHub download like this:
```powershell
iex ((New-Object System.Net.WebClient).DownloadString('https://simeononsecurity.com/scripts/standalonewindows.ps1'))
```

### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

All of the parameters in the "secure-standalone.ps1" script are optional, with a default value of $true. This means that if no value is specified for a parameter when the script is run, it will be treated as if it were set to $true.

The script takes the following parameters, all of which are optional and default to $true if not specified:

- **cleargpos**: (Boolean) Clear GPOs not being used
- **installupdates**: (Boolean) Install updates and reboot if necessary
- **adobe**: (Boolean) STIG Adobe Reader
- **firefox**: (Boolean) STIG Firefox
- **chrome**: (Boolean) STIG Chrome
- **IE11**: (Boolean) STIG Internet Explorer 11
- **edge**: (Boolean) STIG Edge
- **dotnet**: (Boolean) STIG .NET Framework
- **office**: (Boolean) STIG Office
- **onedrive**: (Boolean) STIG OneDrive
- **java**: (Boolean) STIG Java
- **windows**: (Boolean) STIG Windows
- **defender**: (Boolean) STIG Windows Defender
- **firewall**: (Boolean) STIG Windows Firewall
- **mitigations**: (Boolean) STIG Mitigations
- **nessusPID**: (Boolean) Resolve Unquoted Strings in Path
- **horizon**: (Boolean) STIG VMware Horizon
- **sosoptional**: (Boolean) Optional STIG/Hardening items

An example of how to run the script with all default parameters would be:

```powershell
.\secure-standalone.ps1
```
If you want to specify a different value for one or more of the parameters, you can include them in the command along with their desired value. For example, if you wanted to run the script and set the $firefox parameter to $false, the command would be:

```powershell
.\secure-standalone.ps1 -firefox $false
```

You can also specify multiple parameters in the command like this:

```powershell
.\secure-standalone.ps1 -firefox $false -chrome $false
```

Observe que, neste exemplo, os parâmetros Firefox e Chrome estão definidos como $false.



