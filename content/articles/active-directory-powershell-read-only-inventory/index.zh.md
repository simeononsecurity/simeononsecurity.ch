---
title: "使用 PowerShell 创建只读 Active Directory 清单"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "使用范围明确的 PowerShell 查询盘点 Active Directory 组织单位、用户和计算机。在不更改目录对象的情况下导出可供审查的 CSV 文件。"
genre: ["Active Directory", "PowerShell", "系统管理"]
tags: ["Active Directory 清单", "PowerShell AD 清单", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "只读 AD", "AD 用户导出", "AD 计算机导出", "AD OU 导出", "Export-Csv", "RSAT", "目录审计", "AD 报告", "OU 清单", "Windows Server", "PowerShell 脚本", "AD 模块", "目录卫生"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Active Directory 树中的用户、计算机和组织单位记录分别流向三个审查文件。"
coverCaption: "限定查询范围，然后只导出审查所需的字段。"
---
清理 Active Directory 时，先建立一份可信的现有对象清单。此**只读清单**会收集所选范围内的组织单位、用户和计算机。它会导出三个 CSV（逗号分隔值）文件供审查，并且不会更改目录对象。仍需保护这些文件，因为名称和设备详情会暴露环境中的部分信息。

<!--more-->

## 要点

- **选择范围：**先查询一个组织单位，再考虑扩展到整个域。
- **使用读取命令：**`Get-ADOrganizationalUnit`、`Get-ADUser` 和 `Get-ADComputer` 用于检索对象。
- **选择字段：**只导出任务所需的属性。
- **检查输出：**依赖报告之前，先比较对象数量和几行样例。

## 开始之前

你需要一台 DNS 正常且能通过网络访问域控制器的 Windows 管理主机、PowerShell **ActiveDirectory** 模块、一个获准读取所选对象的账户，以及一个用于保存 CSV 的受保护文件夹。在 Windows 客户端上，该模块属于 Remote Server Administration Tools (RSAT) 中的 Active Directory 工具。[Active Directory 模块指南](/articles/active-directory-module-powershell-installation-usage-guide/)介绍安装步骤。Microsoft 提供模块的[cmdlet 参考](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)和[RSAT 安装选项](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools)。本指南使用 Windows PowerShell 语法，不会更改目录对象。

目录权限仍然生效。Microsoft 在[特权账户指南](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory)中说明，访问控制列表通常允许经过身份验证的用户读取一般信息，同时限制敏感字段和更改权限。先使用获批账户和测试 OU。不要为了让清单成功而提升到 Domain Admin。

> **警告：**CSV 文件包含账户名和计算机名。请将文件保存在获批位置，限制访问，并在审查后删除多余副本。不要发布原始导出文件，也不要将其附加到公开 issue。

## 选择搜索基准

**组织单位 (OU)** 用于对目录对象分组。它的**可分辨名称 (DN)** 标识其在目录树中的位置。`-SearchBase` 参数会将查询限制在指定 DN 内。如果没有有意设定范围，宽泛的筛选器可能返回远多于审查所需的对象。

先加载模块，然后查看当前域的 DN：

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft 记录了 [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) 及其返回的域信息。设置搜索基准之前，先找到要审查的 OU：

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

从结果中复制准确的 DN。在后续示例中，将这个文档示例值替换为你的 OU DN：

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` 是文档示例域。不要把它的 DN 复制到实际查询中。如果确实要盘点整个域，请将 `$SearchBase` 设为域 DN，并在报告中记录这个更大的范围。Microsoft 的 [Get-ADOrganizationalUnit 参考](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit)介绍了 `-Filter` 和 `-SearchBase`。

## 盘点 OU、用户和计算机

先统计对象数量。这样有助于快速发现搜索基准错误或意外的空结果：

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` 表示检索搜索基准内所有匹配对象。Microsoft 将 [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) 和 [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer)列为检索命令。数量为零也可能是正确结果，但在认定清单完整之前，请检查 DN、权限和目标域。

现在在控制台预览几行。保存所选字段，让预览和后续 CSV 导出使用相同列：

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

只有审查需要时，才为计算机请求额外的操作系统属性：

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

`-Properties` 参数用于请求不在 cmdlet 默认属性集中的属性。Microsoft 在[计算机 cmdlet 参考](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer)中介绍了此参数。操作系统名称属于目录数据，不能证明当前安装的版本。计算机对象可能已过期，或者其属性尚未更新。

## 导出可审查的 CSV 文件

选择空间充足的获批输出文件夹。以下命令会写入**本地 CSV 文件**，不会更改目录对象。请在该文件夹中运行。`-NoClobber` 可阻止覆盖现有文件。每次运行都使用新的文件夹或文件名。

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Microsoft 的 [Export-Csv 参考](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1)介绍了 `-NoTypeInformation`、`-Encoding` 和 `-NoClobber`。使用文本编辑器或获批的电子表格工具打开每个 CSV。检查表头、几行记录，并将记录数量与之前的统计结果比较。命令失败或生成零字节文件，都不能证明报告完整。

> **预期结果：**你会得到三个 CSV 文件，分别包含所选目录范围内的 OU、用户和计算机记录。行数及样例值应与所选目录范围相符。

## 在不更改对象的情况下审查

使用清单回答具体问题：哪一个 OU 负责某台计算机？哪些用户账户已禁用？哪些设备名称需要指定负责人？将发现记录在单独的审查备注中。不要仅凭 `Enabled` 值判断账户是否仍有必要。不要只根据导出结果删除或禁用对象。

定期生成报告时，请记录查询日期、域、OU DN、所选属性、操作人员和 CSV 存放位置。比较两份导出文件时，确认它们使用了相同范围和字段。否则，差异可能来自查询条件，而非目录中的实际变化。

这是**清单**，不是特权账户审计，也不是登录活动报告。Microsoft 指出，Active Directory 的属性和权限因对象及环境而异。根据操作系统属性或显示名称采取行动之前，请向系统负责人核实。[Active Directory 安全指南](/articles/active-directory-security-best-practices/)介绍了更广泛的安全控制。

## 故障排除

- **无法导入模块：**确认主机已安装 RSAT 中的 Active Directory 工具或 Windows Server 管理工具。按照[模块设置指南](/articles/active-directory-module-powershell-installation-usage-guide/)操作。
- **查询未返回对象：**检查准确 DN、当前域、OU 内容和读取权限。扩大范围之前，先测试一个已知的小型 OU。
- **某个属性为空：**确认该属性存在，而且你的账户有权读取。不要猜测缺失字段。
- **导出提示文件已存在：**`-NoClobber` 保护了之前的报告。选择新的文件名或文件夹，然后重新运行命令。
- **数量与预期不符：**检查用户或计算机是否位于其他 OU、范围是否变化，以及查询期间目录是否发生变化。

## 后续步骤

在约定的审查期限内，将原始 CSV 文件保存在受保护位置。只分享审查者需要的字段。负责人确认发现后，按照常规审批和回退流程规划更改。获批更改完成后，使用相同范围重新运行同一清单以确认结果。