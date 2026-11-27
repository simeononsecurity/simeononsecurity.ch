---
title: "PowerShell 脚本编写"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "通过这份面向初学者的分步指南，学习 PowerShell 脚本基础知识并自动执行任务，内容涵盖 cmdlet、循环、函数等。"
genre: ["技术", "编程", "自动化", "Windows", "脚本编写", "IT", "管理任务", "计算机管理", "软件开发", "编码"]
tags: ["PowerShell 脚本编写", "PowerShell 自动化", "Windows 脚本", "PowerShell cmdlets", "PowerShell 模块", "PowerShell 循环", "PowerShell 条件语句", "PowerShell 函数", "PowerShell 最佳实践", "PowerShell 调试", "PowerShell 测试", "PowerShell 变量", "PowerShell ISE", "PowerShell Remoting", "Microsoft 技术", "IT 自动化", "计算机管理", "初学者编程", "管理任务", "PowerShell 脚本创意", "自动备份", "文件管理", "系统信息", "用户管理", "软件安装", "网络配置", "安全自动化", "任务计划", "注册表操作", "远程管理"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "卡通人物手持脚本，站在显示 PowerShell 提示符的计算机前，说明初学者也能轻松学习 PowerShell 脚本编写"
coverCaption: ""
---
**PowerShell 脚本编写入门**

PowerShell 是 Microsoft 开发的命令行 shell 和脚本语言。它提供大量命令和功能，可用于管理和自动化 Windows 操作系统以及其他 Microsoft 技术。本文介绍 PowerShell 脚本编写基础，并提供循序渐进的入门指南。

## PowerShell 简介

**PowerShell** 是一种命令行 shell，可帮助用户自动化和管理 Windows 操作系统及其他 Microsoft 技术。它提供一套全面的命令和功能，用于执行各种管理任务，例如管理文件和目录、配置网络以及管理系统。PowerShell 还支持脚本语言，用户可以借此创建复杂脚本并自动执行重复任务。

## 开始使用 PowerShell

### 安装 PowerShell

大多数 Windows 版本都预装了 PowerShell。如果使用较旧的 Windows 版本，或需要更新版本的 PowerShell，可以从 Microsoft 网站下载。请按以下步骤下载并安装 PowerShell：

1. 访问 [Microsoft PowerShell 网站](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2)，并选择要安装的 PowerShell 版本。
2. 下载并运行安装文件。
3. 按照屏幕上的说明完成安装。

### 启动 PowerShell

安装 PowerShell 后，请按以下步骤启动：

1. 打开“开始”菜单，在搜索栏中输入“PowerShell”。
2. 从搜索结果中选择“Windows PowerShell”。
3. PowerShell 将在新窗口中打开。

### 在 Visual Studio Code 中编写 PowerShell 脚本

若要获得更完善的脚本编写体验，可以使用常见的集成开发环境 Visual Studio Code (VS Code)。VS Code 提供语法突出显示、代码补全、调试和集成终端支持，是编写 PowerShell 脚本的合适选择。请按以下步骤在 VS Code 中开始编写 PowerShell 脚本：

1. 从[官方网站](https://code.visualstudio.com/)安装 Visual Studio Code。
2. 在 VS Code 扩展市场中安装 Microsoft 发布的“PowerShell”扩展。
3. 在 VS Code 中打开 PowerShell 脚本文件 (.ps1)，即可开始编写脚本。

### 使用 PowerShell 管理系统

PowerShell 是一款适用于系统管理任务的多用途工具。从简单的单行命令到复杂的自动化工作流，PowerShell 都能简化原本需要手动处理的任务。它为 Windows、Linux 和 macOS 提供统一的脚本平台，让管理员能够使用一致的工具集管理不同环境。

### 从命令提示符过渡到 Windows PowerShell

如果熟悉命令提示符并希望转用 Windows PowerShell，学习过程会比较顺畅。Windows PowerShell 脚本以命令提示符的概念为基础，同时提供更高级的功能。你可以先利用已有知识，再逐步了解 PowerShell 提供的其他功能和 cmdlet。

### PowerShell 基础知识

PowerShell 提供命令行界面，让用户能够与操作系统交互。PowerShell 命令称为 cmdlet，并按模块组织。若要查看可用模块，请使用 Get-Module 命令：

```powershell
Get-Module
```

若要查看某个模块中可用的 cmdlet，请使用 Get-Command：
```powershell
Get-Command -Module <module name>
```

若要查看 cmdlet 的帮助，请使用 Get-Help：
```powershell
Get-Help <cmdlet name>
```

PowerShell 还支持别名，也就是 cmdlet 的较短名称。若要查看可用别名，请使用 Get-Alias：
```powershell
Get-Alias
```

## 脚本文件和执行策略

PowerShell 脚本文件使用 .ps1 扩展名。运行脚本前，你可能需要设置执行策略。执行策略决定是否允许运行脚本以及允许运行哪些类型的脚本。若要设置执行策略，请使用 Set-ExecutionPolicy 命令。例如，若要允许运行脚本，请执行：

```powershell
Set-ExecutionPolicy RemoteSigned
```

或者（仅用于测试）

```powershell
Set-ExecutionPolicy Undefined
```

### PowerShell 脚本编写

PowerShell 脚本编写可自动执行各种管理任务。PowerShell 脚本支持变量、循环、条件语句和函数，因此适合用于自动化。

#### 变量

变量用于在 PowerShell 脚本中存储数据。PowerShell 变量以美元符号 ($) 开头。若要为变量赋值，请使用以下语法：
```powershell
$variable_name = value
```
例如：
```powershell
$name = "John"
```
#### 循环

循环会按指定次数重复执行代码块。PowerShell 支持以下循环类型：

- **For 循环**：按指定次数重复执行代码块。
- **While 循环**：只要条件为真，就重复执行代码块。
- **Do-While 循环**：至少执行一次代码块，然后在条件为真时继续重复。
- **ForEach 循环**：为集合中的每个项目重复执行代码块。

例如，以下代码使用 For 循环打印数字 1 到 5：
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### 条件语句

条件语句

条件语句在满足指定条件时执行代码块。PowerShell 支持以下条件语句：

- **If 语句**：条件为真时执行代码块。
- **If-Else 语句**：条件为真时执行一个代码块，为假时执行另一个代码块。
- **Switch 语句**：将某个值与一组可能的匹配项比较，并执行第一个匹配项对应的代码块。

例如，以下代码使用 If 语句检查某个数字是否大于 5：

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "该数字大于 5"
}
```
#### 函数

函数是可重复使用的代码块，用于执行特定任务。函数接收输入参数并返回输出值。PowerShell 支持以下函数类型：

- **脚本块**：可执行的代码块。
- **高级函数**：包含元数据和参数验证的函数。

例如，以下代码定义了一个用于相加两个数字的函数：
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "结果为 $result"
```
### PowerShell ISE

PowerShell ISE（集成脚本环境）是用于 PowerShell 脚本编写的图形界面。它提供富文本编辑器、调试工具及其他功能，让编写和测试 PowerShell 脚本更容易。请按以下步骤打开 PowerShell ISE：

1. 打开“开始”菜单，在搜索栏中输入“PowerShell ISE”。
2. 从搜索结果中选择“Windows PowerShell ISE”。
3. PowerShell ISE 将在新窗口中打开。

### PowerShell Remoting

PowerShell Remoting 可让用户在远程计算机上运行 PowerShell 命令和脚本。此功能要求本地和远程计算机上的 WinRM 服务均处于运行状态。请按以下步骤启用 PowerShell Remoting：

1. 使用管理员权限打开 PowerShell 提示符。
2. 运行以下命令启用 PowerShell Remoting：
```powershell
   Enable-PSRemoting -Force
```
3. 运行以下命令，将远程计算机添加到 TrustedHosts 列表：
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. 重启 WinRM 服务。
```powershell
Restart-Service WinRM
```

若要在远程计算机上运行 PowerShell 命令，请使用 Invoke-Command：
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell 模块

PowerShell 模块是为特定任务设计的 cmdlet、函数和脚本集合。你可以通过 PowerShell Gallery 安装和管理这些模块。PowerShell Gallery 是 PowerShell 模块的中央存储库。

若要从 PowerShell Gallery 安装模块，请运行：
```powershell
Install-Module <module name>
```

若要查看已安装的 PowerShell 模块，请使用 Get-InstalledModule：
```powershell
Get-InstalledModule
```

### PowerShell 脚本编写的最佳实践

编写 **PowerShell 脚本**时，应遵循最佳实践，让脚本更加**安全**、**可靠**且**易于维护**。以下是一些建议：

- **使用描述性变量名**：选择能够清楚说明用途的变量名。
- **添加注释**：说明代码的用途。
- **处理错误**：妥善处理错误和异常。PowerShell 的 `Try...Catch...Finally` 结构可用于捕获异常并采取适当措施。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **全面测试脚本**：确认脚本按预期运行。你可以使用 PowerShell 测试框架 **Pester** 编写并运行单元测试。[Pester 文档](https://pester.dev/)
- **使用函数和模块**：整理代码并提高复用性。函数可将代码拆分为较小且易管理的部分，模块则可用于打包和分发代码。[函数说明](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1)，[模块说明](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **避免硬编码值**：使用参数或变量代替固定值，让脚本更灵活且易于复用。可以通过 `param` 关键字向脚本传递参数。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **使用详细输出**：显示脚本运行进度的其他信息。使用 `Write-Verbose` 输出详细消息。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### PowerShell 脚本最佳实践详解

#### 处理错误

错误处理对于 PowerShell 脚本至关重要，因为它能帮助脚本妥善处理错误和异常。PowerShell 提供多种错误处理方式，包括 Try-Catch 语句、Trap 语句和 ErrorAction 参数。Try-Catch 用于捕获和处理异常，Trap 用于捕获和处理错误，ErrorAction 则控制脚本如何处理错误。

下面是使用 Try-Catch 妥善处理错误的示例：
```powershell
try {
    # 可能引发错误的代码
}
catch {
    Write-Error "发生错误：$_"
}
```

#### 全面测试脚本

测试 PowerShell 脚本可确认它们按预期运行。Pester 等测试工具和框架支持编写及执行测试，帮助查找和隔离代码问题，并验证脚本是否满足要求。

下面是使用 Pester 测试 PowerShell 脚本的示例：
```powershell
Describe "我的 PowerShell 脚本" {
    It "执行指定操作" {
        # 应返回预期结果的代码
        $result = Do-Something
        $result | Should -Be "预期结果"
    }
}
```

#### 使用函数和模块

函数和模块对于整理代码和提高复用性很重要。函数可将代码组织为可复用的代码块，模块则可用于打包并与他人共享代码。使用函数和模块后，脚本会更加模块化、高效且易于维护。

下面是 PowerShell 函数示例：
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "当前有 $count 个进程正在运行。"
```

#### 避免硬编码值

在 PowerShell 脚本中硬编码值会降低灵活性并增加维护难度。应改用参数或变量，以便用户在运行时传入值。这样脚本更易复用，也更能适应变化。

下面是 PowerShell 参数示例：
```powershell
param (
    [string]$name
)

Write-Host "你好，$name！"
```

#### 使用详细输出

详细输出会提供脚本进度信息，有助于调试和排查问题。PowerShell 的 Write-Verbose 可将详细信息输出到控制台，让脚本更易理解和调试。

下面是 PowerShell 详细输出示例：
```powershell
function Get-ProcessCount {
    Write-Verbose "正在获取进程..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "当前有 $count 个进程正在运行。"
```

### 十个适合初学者的 PowerShell 脚本创意

如果你刚开始学习 PowerShell 脚本编写，可以尝试以下十个项目：

- **自动备份**：创建脚本，将重要文件和目录备份到外置硬盘或云存储服务。使用 `Copy-Item` cmdlet 复制文件，并用 `Start-Job` cmdlet 在后台运行备份任务。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **文件管理**：创建脚本，根据文件类型、大小或其他条件将文件和目录整理到不同文件夹。使用 `Get-ChildItem` cmdlet 查找文件，再用 `Move-Item` cmdlet 将其移到指定位置。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **系统信息**：创建脚本，获取 CPU 和内存使用率、磁盘空间、网络设置等系统信息，并以易读格式显示。使用 `Get-WmiObject` 收集信息，再用 `Format-Table` 或 `Out-GridView` 格式化。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **用户管理**：创建脚本，自动添加、修改或删除 Windows 用户和组。使用 `New-LocalUser`、`Set-LocalUser` 和 `Remove-LocalUser` 管理用户，使用 `New-LocalGroup`、`Add-LocalGroupMember` 和 `Remove-LocalGroup` 管理组。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **软件安装**：创建脚本，在多台计算机上同时安装和配置软件，以节省时间和精力。使用 `Invoke-Command` 在远程计算机上执行安装命令。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **网络配置**：创建脚本，自动配置 IP 地址、子网掩码和默认网关。使用 `Set-NetIPAddress`、`Set-NetIPInterface` 和 `Set-DnsClientServerAddress` 配置网络设置。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **安全**：创建脚本，审计和监控安全设置，并在发现变化时提醒用户。使用 `Get-AuditPolicy` 获取审核策略，使用 `Send-MailMessage` 发送电子邮件通知。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **任务计划**：创建脚本，安排并自动执行备份、更新和系统扫描等定期任务。使用 `Register-ScheduledTask` 创建计划任务，并用 `Start-ScheduledTask` 执行任务。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **注册表操作**：创建脚本，修改或读取指定注册表项的值。使用 `Get-ItemProperty` 和 `Set-ItemProperty` 操作注册表。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **远程管理**：创建脚本，启用 Windows 计算机的远程管理，让用户能够在远程计算机上运行命令和脚本。使用 `Enter-PSSession` 或 `Invoke-Command` 在远程计算机上运行命令。[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1)，[Microsoft 文档](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

通过这些脚本创意积累实践经验，并进一步学习 PowerShell 脚本编写。

## 总结

PowerShell 是管理和自动化 Windows 及其他 Microsoft 技术的强大工具。本文介绍了面向初学者的脚本基础，包括安装和启动 PowerShell、使用 cmdlet、变量、循环、条件语句和函数，以及使用 PowerShell ISE、PowerShell Remoting 和 PowerShell 模块。遵循最佳实践有助于创建安全、可靠且易于维护的脚本。通过练习，你可以熟练使用 PowerShell 并轻松自动执行各种管理任务。
