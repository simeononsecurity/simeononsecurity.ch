---
title: "Windows Defender Application Control WDAC を使用して Windows を強化するための完全ガイド"
date: 2020-12-16
toc: true
draft: false
description: "Windows Defender Application Control WDAC を使用して、スクリプトとツールを使用して Windows オペレーティング システムを強化する方法を学びます。"
tags: ["Windows Defender アプリケーション コントロール WDAC の強化", "パワーシェル", "PowerShell スクリプト", "オートメーション", "コンプライアンス", "ブルーチーム", "Windows Defender STIG スクリプト", "Windows Defenderの強化", "Windows Defender STIG", "ディフェンダーSTIG", "Windows Defender エクスプロイト保護 WDEP", "Windows Defender の攻撃対象領域の削減 ASR", "Windows Server 2016 2019", "Windowsサーバーコア", "Microsoft WDAC ツールキット", "CI ポリシーを更新する", "Microsoft が推奨するブロック ルール", "Microsoft が推奨するドライバーのブロック ルール", "XMLポリシー", "BIN ポリシー", "グループポリシー", "Microsoft Intune"]
---

**Windows Defender Application Control WDAC で Windows を強化**

＃＃ ノート：
- Windows Server 2016/2019 またはバージョン 1903 より前のバージョンでは、一度に 1 つのレガシー ポリシーのみがサポートされます。
- Windows Server Core エディションは WDAC をサポートしていますが、AppLocker に依存する一部のコンポーネントは動作しません
- 必ずお読みください[Recommended Reading](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening#recommended-reading) 実装する前、あるいはテストする前に。

## このコレクションが使用するスクリプトとツールのリスト:

-[MicrosoftDocs - WDAC-Toolkit](https://github.com/MicrosoftDocs/WDAC-Toolkit)
-[Microsoft - Refresh CI Policy ](https://www.microsoft.com/en-us/download/details.aspx?id=102925)

## 追加の構成は以下から検討されました。

-[Microsoft - Recommended block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules)
-[Microsoft - Recommended driver block rules](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules)
-[Microsoft - Windows Defender Application Control](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control-design-guide)

＃＃ 説明：

### XML と BIN:

- 簡単に言えば、**"XML"** ポリシーはローカルのマシンに適用するためのものであり、**"BIN"** ファイルはそれらを次のいずれかで適用するためのものです。[Group Policy](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-group-policy) or [Microsoft Intune](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-windows-defender-application-control-policies-using-intune) ローカル展開では XML、BIN、または CIP ポリシーを使用できますが、一般的には、可能な限り XML を使用する必要があり、特に監査やトラブルシューティングを行う場合はそうしてください。

### ポリシーの説明:

- **デフォルト ポリシー:**
  - 「デフォルト」ポリシーは、WDAC ツールキットで利用可能なデフォルト機能のみを使用します。
- **推奨ポリシー:**
  - 「推奨」ポリシーでは、デフォルトの機能と Microsoft の推奨機能が使用されます。[blocks](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules) and [driver block](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules) ルール。
- **監査ポリシー:**
  - 「監査」ポリシーは、ルールの例外をログに記録するだけです。これは環境でのテスト用であり、環境のニーズに合わせてポリシーを自由に変更できます。
- **適用されるポリシー:**
  - 「強制」ポリシーではルールの例外は許可されず、準拠しない場合、アプリケーション、ドライバー、DLL などがブロックされます。

### 利用可能なポリシー:

- **XML:**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit_{バージョン}.xml`
    - `WDAC_V1_Recommend_Audit_{バージョン}.xml`
  - **強制:**
    - `WDAC_V1_Default_Enforced_{バージョン}.xml`
    - `WDAC_V1_Recommend_Enforced_{バージョン}.xml`
- **置き場：**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit_{バージョン}.bin`
    - `WDAC_V1_Recommend_Audit_{バージョン}.bin`
  - **強制:**
    - `WDAC_V1_Default_Enforced_{バージョン}.bin`
    - `WDAC_V1_Recommend_Enforced_{バージョン}.bin`
- **CIP:**
  - **監査のみ:**
    - `WDAC_V1_Default_Audit\{uid}.cip`
    - `WDAC_V1_Recommend_Audit\{uid}.cip`
  - **強制:**
    - `WDAC_V1_Default_Enforced\{uid}.cip`
    - `WDAC_V1_Recommended_Enforced\{uid}.cip`

スクリプト内の次の行を更新して、必要なポリシーをローカルで使用します。

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
