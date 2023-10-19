---
title: "使用 PowerShell 脚本自动化 .NET STIG 合规性"
date: 2020-08-20
---
 .NET 框架 STIG

应用 .NET STIG 绝非易事。对于许多管理员来说，在单个系统上完全实施可能需要数小时。此脚本应用所需的注册表更改并修改 machine.config 文件以根据需要实施 FIPS 和其他控制。

## 注意事项：

此脚本不能也永远不会使 .NET stig 达到 100% 的合规性。现在，按原样，它将完成大约 75% 的检查，并返回并完成对所有先前 .NET 版本的适用检查。

任何 .NET 应用程序或 IIS 站点都需要手动干预。

＃＃ 要求：
- [X] Windows 7、Windows Server 2008 或更新版本
- [X] 在生产系统上运行之前在您的环境中进行测试。

## STIGS/SRGs 应用：

-[Microsoft .Net Framework 4 V1R9](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_MS_DotNet_Framework_4-0_V1R9_STIG.zip)

## 来源：

-[Add from one XML data to another existing XML file](http://www.maxtblog.com/2012/11/add-from-one-xml-data-to-another-existing-xml-file/)
-[Caspol.exe (Code Access Security Policy Tool)](https://docs.microsoft.com/en-us/dotnet/framework/tools/caspol-exe-code-access-security-policy-tool)
-[Microsoft .NET Framework Documentation](https://docs.microsoft.com/en-us/dotnet/framework/)
-[PowerShell $PSScriptRoot](https://riptutorial.com/powershell/example/27231/-psscriptroot)
-[PowerShell: Run command from script's directory](https://stackoverflow.com/questions/4724290/powershell-run-command-from-scripts-directory)
-[Powershell XML importnode from different file](https://stackoverflow.com/questions/9944885/powershell-xml-importnode-from-different-file)

## 下载需要的文件

您可以从以下网址下载所需的文件[GitHub Repository](https://raw.githubusercontent.com/simeononsecurity/.NET-STIG-Script/)

## 如何运行脚本

**脚本可以像这样从提取的 GitHub 下载启动：**

## 如何运行脚本
### 手动安装：
如果手动下载，脚本必须从包含所有文件的目录中的管理 powershell 启动[GitHub Repository](https://github.com/simeononsecurity/.NET-STIG-Script)
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
