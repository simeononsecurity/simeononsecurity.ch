---
title: "利用 Shodan PowerShell 模块实现 OSINT 自动化"
date: 2020-11-14
---

用于与 Shodan API 交互的 PowerShell 模块集

**注：**
- 您需要 Shodan API 密钥，该密钥可在您的 [Shodan Account](https://account.shodan.io/)
- 模块中使用的应用程序接口示例可在 [Shodan Developers Page](https://developer.shodan.io/api)
- 某些模块可能会使用扫描或查询信用点数 当您通过网站、CLI 或 API（这些脚本的作用）下载数据时，会使用查询信用点数。
  由于我们使用的是 API，因此必须注意在以下情况下会扣除查询信用点数：
  1.  使用了搜索过滤器
  2.  请求第 2 页或更高页面
      信用点数在月初更新，1 个信用点数可下载 100 个结果。
      至于扫描信用点数，1 个扫描信用点数可扫描 1 个 IP，它们也在月初更新。
      请查看 Shodan 帮助中心 [HERE](https://help.shodan.io/the-basics/credit-types-explained)了解详情。

## 目录
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- 模块**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo)- 返回属于给定 API 密钥的 API 计划的信息。
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders)- 显示客户端连接到网络服务器时发送的 HTTP 头信息。
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP)- 获取从互联网上看到的当前 IP 地址。
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain)- 获取给定域名的所有子域和其他 DNS 条目
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse)- 为给定的 IP 地址列表查找已定义的主机名。
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount)- 搜索漏洞，但只返回与搜索词相关的匹配总数信息，以及可选的漏洞作者、平台、端口、来源或类型。
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount)- 返回"/shodan/host/search "结果的总数。
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP)- 使用 IP 地址搜索 Shodan。
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch)- 使用与网站相同的查询语法搜索 Shodan，并使用切面获取不同属性的摘要信息。
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets)- 该模块返回可用于搜索查询的搜索筛选器列表。
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters)- 该模块返回可用于搜索查询的搜索筛选器列表。
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts)- 列出 Shodan 正在互联网上抓取的所有端口。
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile)- 返回与此 API 密钥关联的 Shodan 帐户的信息
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID)- 检查先前提交的扫描请求的进度
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols)- 列出通过 Shodan 执行按需互联网扫描时可使用的所有协议
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- 使用此模块请求 Shodan 抓取网络。

<a name="Download"></a>

## 下载

您需要克隆或下载脚本到您的电脑。

你可以使用本版本库页面上的代码下拉菜单向上滚动，或者直接复制并粘贴以下链接： [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

在本例中，我们将在 Git Bash 中克隆 repo，点击剪贴板图标（如上图所示）后，输入 git clone，然后右击 Git Bash 窗口，从下拉菜单中选择粘贴：

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

有关克隆的详细说明，请查看 [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

获得文件后，您需要将文件复制到 C:/Program Files\WindowsPowerShell\Modules 下，这样做会弹出拒绝访问的对话框，点击继续完成将文件复制到该位置，然后继续执行安装说明。 [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**或***

您可以向上滚动使用此版本库页面上的代码下拉菜单，或直接点击以下链接：
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

右键单击文件并从下拉菜单中选择在此解压缩，即可解压缩 main.zip。

拿到文件后，你需要将文件复制到 C:\Program Files\WindowsPowerShell\Modules 下，这样做会弹出拒绝访问的对话框，点击继续完成文件复制到该位置，然后继续执行安装说明。 [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

## 安装

<a name="Install"></a> 安装

要安装模块，您需要以管理员身份运行 PowerShell 窗口。
有两种方法：

第一种方法是右键单击桌面上的 PowerShell 图标，然后从下拉菜单中选择以管理员身份运行。

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**或***

在搜索栏中输入 p（或 PowerShell 需要显示的字符数），然后单击 "以管理员身份运行"。

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

您需要进入复制脚本的目录。
运行以下命令更改工作目录：

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

在 Windows 客户端计算机上，我们需要更改 PowerShell 的执行策略（默认为 "受限"）。

有关详细信息，请阅读 [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

运行以下命令将策略设置为 RemoteSigned，并输入 y 以选择 "是的，您要更改策略"。

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

更改执行策略后，可以运行以下命令导入模块。

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

现在，您可以通过 powershell 将任何脚本作为模块运行。
