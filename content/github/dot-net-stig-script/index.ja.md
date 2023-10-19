---
title: "PowerShell スクリプトを使用した .NET STIG 準拠の自動化"
date: 2020-08-20
---
 .NET Framework STIG

.NET STIG の適用は決して簡単ではありません。多くの管理者にとって、単一システムに完全に実装するには何時間もかかる場合があります。このスクリプトは、必要なレジストリ変更を適用し、必要に応じて FIPS およびその他の制御を実装するように machine.config ファイルを変更します。

＃＃ ノート：

このスクリプトでは、.NET stig を 100% 準拠させることはできませんし、今後も実現することはありません。現時点では、チェックの約 75% が完了しており、以前のすべての .NET バージョンに遡って該当するチェックを完了しています。

.NET アプリケーションまたは IIS サイトでは手動介入が必要です。

＃＃ 要件：
- [X] Windows 7、Windows Server 2008 以降
- [X] 運用システムで実行する前に環境でテストします。

## STIGS/SRG が適用されました:

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## 出典:

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## 必要なファイルをダウンロードします

必要なファイルは次の場所からダウンロードできます。[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## スクリプトの実行方法

**スクリプトは、次のように抽出された GitHub ダウンロードから起動できます:**

## スクリプトの実行方法
### 手動インストール:
手動でダウンロードした場合、スクリプトは、[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-.net-4-stig.ps1
```
### Automated Install:
Use this one-liner to automatically download, unzip all supporting files, and run the latest version of the script.
```
iwr -useb 'https://simeononsecurity.com/scripts/sosdotnet.ps1'|iex
```
