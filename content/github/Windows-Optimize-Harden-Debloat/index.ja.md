---
title: "Windows-Optimize-Harden-Debloat スクリプトを使用して Windows システムを最適化および強化する"
date: 2020-12-29
toc: true
draft: false
description: "この包括的なガイドでは、パフォーマンス、セキュリティ、およびプライバシーを向上させるために、Windows システムを最適化、強化、および肥大化させる方法について段階的に説明します。"
tags: ["Windowsの最適化", "Windowsの強化", "Windows の膨張", "Windowsのセキュリティ", "Windowsのパフォーマンス", "Windows のプライバシー", "Windows アップデート", "グループポリシーオブジェクト", "Adobe Acrobat Reader", "Firefox", "グーグルクローム", "インターネットエクスプローラ", "Microsoft クロムエッジ", "ドットネット4", "マイクロソフトオフィス", "ワンドライブ", "オラクル Java JRE 8", "Windowsファイアウォール", "Windows ディフェンダー", "アプリロッカー"]
---
 序章：

Windows 10 および Windows 11 は、そのままでは侵略的で安全ではないオペレーティング システムです。
のような組織[PrivacyTools.io](https://PrivacyTools.io), [Microsoft](https://microsoft.com), [Cyber.mil](https://public.cyber.mil), the [Department of Defense](https://www.defense.gov/), and the [National Security Agency](https://www.nsa.gov/) オペレーティング システムをロックダウン、強化、セキュリティ保護するための構成変更を推奨しています。これらの変更は、テレメトリ、マクロのブロック、ブロートウェアの削除、システムに対する多くのデジタル攻撃や物理攻撃の防止など、幅広い緩和策をカバーしています。このスクリプトは、これらの組織が推奨する構成を自動化することを目的としています。

## 注、警告、および考慮事項:

**警告：**

このスクリプトは、すべてではないにしても、ほとんどのシステムで問題なく動作するはずです。その間[@SimeonOnSecurity](https://github.com/simeononsecurity) creates, reviews, and tests each repo intensively, we can not test every possible configuration nor does [@SimeonOnSecurity](https://github.com/simeononsecurity) take any responsibility for breaking your system. If something goes wrong, be prepared to submit an [issue](../../issues)

- このスクリプトは、主に **個人使用** 環境での動作を目的として設計されています。これを念頭に置いて、特定のエンタープライズ構成設定は実装されていません。このスクリプトは、システムを 100% 準拠させるように設計されていません。むしろ、すべてではないにしても、ほとんどの構成変更を完了するための足がかりとして使用する必要があります。ブランディングやバナーなど、たとえ厳格な個人使用環境であっても実装すべきではない過去の問題をスキップしながら、スクリプトを作成することができます。
- このスクリプトは、他のスクリプトとは異なり、最適化によって Windows のコア機能が損なわれないように設計されています。
- Windows Update、Windows Defender、Windows ストア、Cortona などの機能は制限されていますが、他のほとんどの Windows 10 プライバシー スクリプトのような機能不全状態にはありません。
- 商用環境のみを対象とした最小化されたスクリプトをお探しの場合は、これを参照してください。[GitHub Repository](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)


**このスクリプトの動作が理解できない場合は、実行しないでください。スクリプトを実行する前に、スクリプトを確認してテストするのはあなたの責任です。**

**たとえば、予防措置を講じずにこれを実行すると、次のような問題が発生します:**

- 「Administrator」という名前のデフォルトの管理者アカウントの使用は無効になり、国防総省 STIG に従って名前が変更されます

  - 作成されたデフォルトのアカウントには適用されませんが、Enterprise、IOT、および Windows Server バージョンでよく見られるデフォルトの管理者アカウントの使用には適用されます

  - 必要に応じて、[コンピュータの管理] で新しいアカウントを作成し、管理者として設定します。次に、スクリプトを実行する前に、新しいユーザーに初めてサインインした後、以前のユーザー フォルダーの内容を新しいフォルダーにコピーして、この問題を回避します。

- Microsoft アカウントを使用したサインインは、国防総省 STIG に従って無効になっています。

  - 安全性とプライバシーを確保したい場合、Microsoft アカウント経由でローカル アカウントにサインインすることはお勧めできません。これはこのリポジトリによって強制されます。

  - 必要に応じて、[コンピュータの管理] で新しいアカウントを作成し、管理者として設定します。次に、スクリプトを実行する前に、新しいユーザーに初めてサインインした後、以前のユーザー フォルダーの内容を新しいフォルダーにコピーして、この問題を回避します。

- アカウント PIN は国防総省 STIG に従って無効になっています

  - PIN はパスワードの代わりにのみ使用すると安全ではなく、数時間、場合によっては数秒、数分で簡単に回避されてしまう可能性があります。

  - スクリプトの実行後、アカウントから PIN を削除するか、パスワードを使用してサインインします。

- Bitlocker のデフォルトは、国防総省 STIG により変更され、強化されています。

  - bitlocker の実装方法により、この変更が発生すると、すでに bitlocker が有効になっている場合、bitlocker の実装が中断されます。

  - この問題を回避するには、bitlocker を無効にし、スクリプトを実行してから、bitlocker を再度有効にします。

＃＃ 要件：

- [x] Windows 10/11 Enterprise (**推奨**) または Professional
  - Windows 10/11 Home エディションは GPO 構成をサポートしていないため、テストされていません。
  - Windows "N" エディションはテストされていません。
-[x] [Standards](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure) 安全性の高い Windows 10 デバイスの場合
-[x] System is [fully up to date and supported](https://support.microsoft.com/en-gb/help/4027667/windows-10-update)
  - を実行します[Windows Upgrade Assistant](https://support.microsoft.com/en-us/help/3159635/windows-10-update-assistant) 最新のメジャー リリースを更新して確認します。
- [x] このスクリプトを実装する前に、Bitlocker を一時停止するかオフにする必要があります。再起動後に再び有効にすることができます。
  - このスクリプトのフォローアップ実行は、bitlocker を無効にせずに実行できます。
- [x] ハードウェア要件
  -[Hardware Requirements for Memory Integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/requirements-and-deployment-planning-guidelines-for-virtualization-based-protection-of-code-integrity#baseline-protections)
  -[Hardware Requirements for Virtualization-Based Security](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs)
  -[Hardware Requirements for Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/reqs-wd-app-guard)
  -[Hardware Requirements for Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-requirements)

## 推奨される書籍:

-[System Guard Secure Launch](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-secure-launch-and-smm-protection#requirements-met-by-system-guard-enabled-machines)
-[System Guard Root of Trust](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)
-[Hardware-based Isolation](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/overview-hardware-based-isolation)
-[Memory integrity](https://docs.microsoft.com/en-us/windows/security/threat-protection/device-guard/memory-integrity)
-[Windows Defender Application Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-guard/wd-app-guard-overview)
-[Windows Defender Credential Guard](https://docs.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard-how-it-works)

## 追加、注目すべき変更、バグ修正:

**このスクリプトは、システム上の設定を追加、削除、および変更します。スクリプトを実行する前に確認してください。**

### ブラウザ:

- ブラウザには、プライバシーとセキュリティを強化するために追加の拡張機能がインストールされます。
  - 見る[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/11) 追加情報については。
- ブラウザーに実装された国防総省 STIG により、拡張機能管理およびその他のエンタープライズ設定が設定されます。これらのオプションを確認する方法については、以下の GPO の手順を参照する必要があります。

### Powershell モジュール:

- Windows Update の自動化を支援するための PowerShell[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) モジュールがシステムに追加されます。

### Microsoft アカウント、ストア、または Xbox サービスの修正:

これは、Microsoft アカウントへのサインインがブロックされているためです。 Microsoft のテレメトリと ID の関連付けは眉をひそめています。
ただし、これらのサービスを引き続き使用したい場合は、次の問題チケットを参照して解決策を確認してください。

- https://github.com/simeononsecurity/Windows-Optimize-Debloat/issues/1
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/16
- https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat/issues/22

### 事後的にローカル グループ ポリシーでポリシーを編集する:

設定を修正または変更する必要がある場合は、ほとんどの場合、GPO を介して構成できます。

- ここから ADMX ポリシー定義をインポートします[repo](https://github.com/simeononsecurity/STIG-Compliant-Domain-Prep/tree/master/Files/PolicyDefinitions) 変更しようとしているシステム上の _C:\windows\PolicyDefinitions_ に変更します。

- 変更しようとしているシステム上で「gpedit.msc」を開きます。

## このコレクションが使用するスクリプトとツールのリスト:

＃＃＃ 最初のパーティ：

-[.NET-STIG-Script](https://github.com/simeononsecurity/.NET-STIG-Script)
-[Automate-Sysmon](https://github.com/simeononsecurity/Automate-Sysmon)
-[FireFox-STIG-Script](https://github.com/simeononsecurity/FireFox-STIG-Script)
-[JAVA-STIG-Script](https://github.com/simeononsecurity/JAVA-STIG-Script)
-[Standalone-Windows-STIG-Script](https://github.com/simeononsecurity/Standalone-Windows-STIG-Script)
-[Windows-Defender-STIG-Script](https://github.com/simeononsecurity/Windows-Defender-STIG-Script)
-[Windows-Optimize-Debloat](https://github.com/simeononsecurity/Windows-Optimize-Debloat)

＃＃＃ 第三者：

-[Cyber.mil - Group Policy Objects](https://public.cyber.mil/stigs/gpo/)
-[Microsoft Security Compliance Toolkit 1.0](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
-[Microsoft Sysinternals - Sysmon](https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon)

## STIGS/SRG が適用されました:

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

## 追加の構成は以下から検討されました。

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

## スクリプトの実行方法:
### GUI - ガイド付きインストール:

最新リリースをダウンロードする[here](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat-GUI/releases/)必要なオプションを選択し、「実行」をクリックします。 <img src="https://raw.githubusercontent.com/simeononsecurity/Windows-Optimize-Harden-Debloat/master/.github/images/WOHD-GUI.gif" alt="Windows-Optimize-Harden-Debloat GUI ベースのガイド付きインストールの例"> ### 自動インストール: このワンライナーを使用して、すべてのサポート ファイルを自動的にダウンロード、解凍し、最新バージョンのスクリプトを実行します。```powershell
iwr -useb 'https://simeononsecurity.com/scripts/windowsoptimizeandharden.ps1'|iex
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
