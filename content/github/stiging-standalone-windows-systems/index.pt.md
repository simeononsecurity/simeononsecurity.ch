---
title: "Automatizando a conformidade do Windows 10 STIG com o script Powershell"
date: 2020-08-26
---

**Baixe todos os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**Estamos buscando ajuda com o seguinte[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

## Introdução:

O Windows 10 é um sistema operacional inseguro pronto para uso e requer muitas alterações para garantir[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) conformidade.
Organizações como[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://dod.gov), and the [National Security Agency](https://www.nsa.gov/) recomendaram e exigiram alterações de configuração para bloquear, fortalecer e proteger o sistema operacional e garantir a conformidade do governo. Essas alterações abrangem uma ampla gama de mitigações, incluindo bloqueio de telemetria, macros, remoção de bloatware e prevenção de muitos ataques físicos em um sistema.

Os sistemas autônomos são alguns dos sistemas mais difíceis e irritantes de proteger. Quando não automatizados, requerem alterações manuais de cada STIG/SRG. Totalizando mais de 1.000 alterações de configuração em uma implantação típica e uma média de 5 minutos por alteração, o que equivale a 3,5 dias de trabalho. Este script visa acelerar significativamente esse processo.

## Notas:

- Este script foi projetado para operação em ambientes **Enterprise** e pressupõe que você tenha suporte de hardware para todos os requisitos.
  - Para sistemas pessoais, consulte isto[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- Este script não foi projetado para levar um sistema a 100% de conformidade, mas deve ser usado como um trampolim para concluir a maioria, se não todas, as alterações de configuração que podem ser roteirizadas.
  - Menos a documentação do sistema, esta coleção deve trazer até cerca de 95% de conformidade em todos os STIGS/SRGs aplicados.

## Requisitos:
- [X] Windows 10 Enterprise é **Obrigatório** por STIG.
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) para um dispositivo Windows 10 altamente seguro
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - Atualmente Windows 10 **v1909** ou **v2004**.
  - Execute o[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) para ser atualizado e verificar a versão principal mais recente.
- [X] Requisitos de hardware
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
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

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## Foram consideradas configurações adicionais de:

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRGs aplicados:
 
-[Windows 10 V1R23](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_10_V1R23_STIG.zip)

-[Windows Defender Antivirus V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Windows_Defender_Antivirus_V1R9_STIG.zip)

-[Windows Firewall V1R7](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Windows_Firewall_V1R7_STIG.zip)

-[Internet Explorer 11 V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_IE11_V1R19_STIG.zip)

-[Adobe Reader Pro DC Continous V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Adobe_Acrobat_Pro_DC_Continuous_V1R2_STIG.zip)

-[Microsoft Office 2019/Office 365 Pro Plus V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_Office_365_ProPlus_V1R2_STIG.zip)

-[Microsoft Office 2016 V1R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/pdf/U_Microsoft_Office_2016_V1R2_Overview.pdf)

-[Microsoft Office 2013 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MicrosoftOffice2013_V1R5_Overview.zip)

-[Google Chrome V1R19](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Google_Chrome_V1R19_STIG.zip)

-[Firefox V4R29](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MOZ_FireFox_V4R29_STIG.zip)

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **Trabalho em progresso**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Como executar o script

**O script pode ser iniciado a partir do download extraído do GitHub assim:**
```
.\secure-standalone.ps1
```
O script que usaremos deve ser iniciado a partir do diretório que contém todos os outros arquivos do[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
