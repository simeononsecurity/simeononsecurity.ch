---
title: "Powershell スクリプトによる Windows 10 STIG 準拠の自動化"
date: 2020-08-26
---

**必要なファイルをすべて次の場所からダウンロードします。[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)

**私たちは次のような支援を求めています[.Net issue](https://github.com/simeononsecurity/W10-Optimize-and-Harden/issues/3) 

＃＃ 序章：

Windows 10 は、そのままでは安全ではないオペレーティング システムであり、安全性を確保するには多くの変更が必要です。[FISMA](https://www.cisa.gov/federal-information-security-modernization-act) コンプライアンス。
のような組織[Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) オペレーティング システムをロックダウン、強化、保護し、政府のコンプライアンスを確保するために、構成変更を推奨および要求しています。これらの変更は、テレメトリ、マクロのブロック、ブロートウェアの削除、システムに対する多くの物理攻撃の防止など、幅広い緩和策をカバーしています。

スタンドアロン システムは、セキュリティを確保するのが最も困難で面倒なシステムの 1 つです。自動化されていない場合は、各 STIG/SRG を手動で変更する必要があります。一般的な展開では合計 1,000 件を超える構成変更があり、変更ごとに平均 5 分、つまり 3.5 日分の作業に相当します。このスクリプトは、そのプロセスを大幅に高速化することを目的としています。

＃＃ ノート：

- このスクリプトは **エンタープライズ** 環境で動作するように設計されており、すべての要件に対するハードウェア サポートがあることを前提としています。
  - 個人向けシステムについては、こちらを参照してください。[GitHub Repository](https://github.com/simeononsecurity/W10-Optimize-and-Harden)
- このスクリプトは、システムを 100% 準拠させるように設計されたものではなく、スクリプト化できる構成変更のすべてではないにしても、ほとんどを完了するための足がかりとして使用する必要があります。
  - システム ドキュメントを除くと、このコレクションでは、適用されるすべての STIGS/SRG に対して最大約 95% の準拠が得られます。

＃＃ 要件：
- [X] Windows 10 Enterprise は STIG ごとに **必須** です。
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) 安全性の高い Windows 10 デバイスの場合
-[x] System is [fully up to date](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - 現在、Windows 10 **v1909** または **v2004**。
  - を実行します[Windows 10 Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 最新のメジャー リリースを更新して確認します。
- [X] ハードウェア要件
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections) 
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)
  
## 推奨される書籍:
  -[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
  -[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
  -[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
  -[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
  -[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
  -[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## このコレクションが使用するスクリプトとツールのリスト:

-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)

-[NSACyber - Bitlocker Guidance](https://github.com/nsacyber/BitLocker-Guidance)

## 追加の構成は以下から検討されました。

-[NSACyber - Hardware-and-Firmware-Security-Guidance](https://github.com/nsacyber/Hardware-and-Firmware-Security-Guidance)

-[NSACyber - Application Whitelisting Using Microsoft AppLocker](https://apps.nsa.gov/iad/library/ia-guidance/tech-briefs/application-whitelisting-using-microsoft-applocker.cfm)

## STIGS/SRG が適用されました:
 
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

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip) - **作業中**

-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## スクリプトの実行方法

**スクリプトは、次のように抽出された GitHub ダウンロードから起動できます:**
```
.\secure-standalone.ps1
```
使用するスクリプトは、他のすべてのファイルを含むディレクトリから起動する必要があります。[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
