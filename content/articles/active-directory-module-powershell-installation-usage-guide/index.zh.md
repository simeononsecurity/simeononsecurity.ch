---
title: "使用 PowerShell 掌握 Active Directory 管理：安装和使用指南"
date: 2023-07-25
toc: true
draft: false
description: "了解如何有效安装和使用 PowerShell 的 Active Directory 模块来简化 Windows Active Directory 管理任务。"
genre: ["技术", "视窗", "PowerShell", "活动目录", "行政部门", "脚本", "信息技术", "自动化", "Windows 服务器", "微软"]
tags: ["PowerShell 的活动目录模块", "在 PowerShell 中导入活动目录模块", "Windows PowerShell 的活动目录模块", "活动目录 PowerShell 安装", "安装活动目录 PowerShell", "PowerShell 安装活动目录模块 Windows 10", "安装活动目录 PowerShell 模块 Windows 10", "获取活动目录 PowerShell 模块", "AD 管理", "Windows 活动目录", "PowerShell cmdlets", "检索 AD 信息", "创建 AD 对象", "修改 AD 对象", "管理 AD 安全", "AD 用户管理", "AD 组管理", "AD OR 管理", "PowerShell 脚本", "Windows 服务器管理", "微软 PowerShell", "自动执行 AD 任务", "安装 PowerShell 模块", "AD 管理指南", "活动目录管理", "AD 安全管理", "PowerShell 自动化", "活动目录 PowerShell 命令", "PowerShell cmdlet 参考"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "该图片描绘了一个由相互连接的服务器和用户图标组成的网络，象征着 Active Directory 管理和自动化。"
coverCaption: "用 PowerShell 释放 Active Directory 管理的威力。"
---

## 简介

在当今的数字化环境中，管理和维护 Windows Active Directory（AD）环境中的用户账户、安全组和其他资源需要高效、简化的流程。PowerShell 是微软开发的一种功能强大的脚本语言，它提供了**活动目录模块**，以促进活动目录管理任务。该模块提供了大量 cmdlet，使管理员能够自动执行各种操作并有效管理 AD。本文将探讨 PowerShell Active Directory 模块的安装和使用。

## PowerShell Active Directory 模块的安装

要开始使用 PowerShell 的 Active Directory 模块，需要确保已将其安装到系统上。安装过程可能因操作系统而异。以下是在**Windows 10**、**Windows 11**和**Windows Server**上安装模块的步骤：

### Windows 10 和 Windows 11 - PowerShell
1.以管理权限打开 **Windows PowerShell**。
2.运行以下命令安装模块：

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1.等待安装完成。完成后，即可开始使用 Active Directory 模块。

### Windows 服务器
1.以管理权限打开 **Windows PowerShell**。
2.运行以下命令安装模块：

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3.等待安装完成。完成后，即可开始使用 Active Directory 模块。

#### 离线系统

离线系统比较复杂。有几种方法，但我们推荐使用以下脚本：
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## 在 PowerShell 中导入 Active Directory 模块

在 PowerShell 中使用 Active Directory 模块之前，需要将其导入当前会话。请按照以下步骤导入模块：

1.以管理权限启动 **Windows PowerShell**。
2.执行以下命令导入模块：

```powershell
Import-Module ActiveDirectory
```

3.Active Directory 模块将被导入，现在可以访问其 cmdlets 和功能。

## 使用 PowerShell 的 Active Directory 模块

导入 Active Directory 模块后，就可以利用其丰富的 cmdlet 执行各种管理任务。让我们来了解一些常用的 cmdlet 及其功能：

#### 检索活动目录信息

要有效管理 Active Directory (AD) 环境，检索有关各种 AD 对象（如用户、组和组织单位 (OU)）的信息至关重要。PowerShell 提供了功能强大的 cmdlet，可简化检索过程。

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps)通过此 cmdlet，您可以检索 AD 用户的详细信息。您可以获取用户名、显示名、电子邮件地址等属性。例如，要检索用户名以 "johndoe "开头的所有用户，可以运行以下命令：

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  该命令将返回与指定过滤器匹配的用户对象列表。

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps)使用 Get-ADGroup cmdlet 可以获取有关 AD 组的信息。它提供了对组名称、成员、描述等详细信息的访问。例如，要检索 AD 环境中的所有安全组，可以执行以下命令：

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  这将提供 Active Directory 中的安全组列表。

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps)Get-ADOrganizationalUnit cmdlet 用于检索有关 AD OU 的信息。它允许你访问 OU 名称、描述、父 OU 等属性。要获取域中的所有 OU，可以使用以下命令：

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  运行此命令将显示 Active Directory 中所有 OU 的列表。

通过使用这些功能强大的 cmdlet，您可以轻松检索有关 AD 用户、组和 OU 的特定信息，从而实现 Active Directory 环境的高效管理。

{{< inarticle-dark >}}


通过这些 cmdlet，您可以检索特定属性、过滤结果并执行高级查询，以获取所需的信息。

### 创建和管理活动目录对象

在使用活动目录（AD）时，PowerShell 中的活动目录模块提供了功能强大的 cmdlet，用于创建和管理活动目录对象。让我们来探索一些用于创建 AD 用户、组和组织单位 (OU) 的基本 cmdlet。

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps)通过此 cmdlet，您可以创建一个新的 AD 用户。您可以指定用户名、密码、电子邮件地址等属性。例如，要创建一个用户名为 "john.doe"、显示名为 "John Doe "的新用户，可以使用以下命令：

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  该命令将在 Active Directory 中创建一个新用户。

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps)使用 New-ADGroup cmdlet 可以创建一个新的 AD 组。您可以设置组名称、描述、组范围等属性。要创建一个名为 "Marketing "并带有说明的新组，可以执行以下命令：

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  该命令将在 Active Directory 中创建一个新组。

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps)使用 New-ADOrganizationalUnit cmdlet，可以创建一个新的 AD OU。你可以指定 OU 名称、父 OU 等属性。例如，要在 "部门 "OU 下创建名为 "销售 "的新 OU，可以运行以下命令：

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  该命令将在 Active Directory 层次结构中创建一个新的 OU。

利用这些 cmdlet，您可以轻松创建具有所需属性和配置的新 AD 用户、组和 OU，从而实现对 Active Directory 环境的高效管理。

{{< inarticle-dark >}}


### 修改活动目录对象

在修改现有 Active Directory (AD) 对象的属性和属性时，PowerShell 中的 Active Directory 模块提供了几个有用的 cmdlet。让我们来了解一下这些用于修改 AD 用户、组和组织单位 (OU) 的 cmdlet。

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps)Set-ADUser cmdlet 允许您修改 AD 用户的属性。您可以更新显示名称、电子邮件地址、电话号码等属性。例如，要更改用户名为 "john.doe "的用户的电话号码，可以使用以下命令：

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  此命令将修改 Active Directory 中指定用户的电话号码。

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps)使用 Set-ADGroup cmdlet 可以修改 AD 组的属性。你可以更新组描述、成员资格、组范围等属性。要将名为 "Marketing "的组的描述更改为 "Marketing Team"，可以执行以下命令：

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  此命令将更新 Active Directory 中指定组的描述。

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps)Set-ADOrganizationalUnit cmdlet 允许您修改 AD OU 的属性。您可以更改 OU 名称、描述等属性。例如，要将名为 "销售 "的 OU 的描述修改为 "销售部"，可以运行以下命令：

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  此命令将更新 Active Directory 层次结构中指定 OU 的描述。

利用这些 cmdlet，您可以轻松修改 AD 对象的属性和属性，进行必要的更新和调整，以满足组织的要求。

{{< inarticle-dark >}}


### 管理活动目录安全

除了管理 Active Directory (AD) 对象外，PowerShell 中的 Active Directory 模块还提供了专门用于处理 AD 安全相关方面的 cmdlet。这些 cmdlet 使管理员能够在 AD 环境中有效地管理用户访问、组成员资格和密码相关任务。

下面是一些常用的安全相关 cmdlet：

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps)通过此 cmdlet，您可以向 AD 组添加成员。通过指定 AD 组和要添加的用户账户或组，可以轻松管理访问控制。例如，要将名为 "JohnDoe "的用户添加到 "经理 "组，可以使用以下命令：

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps)使用此 cmdlet，可以删除 AD 组中的成员。通过指定 AD 组和要删除的用户账户或组，可以有效地管理组成员。例如，要从 "开发人员 "组中移除名为 "JaneSmith "的用户，可以使用以下命令：

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps)通过此 cmdlet，您可以为 AD 用户设置密码。通过指定用户账户并提供新密码，可以执行密码策略并确保安全的用户身份验证。下面是一个为名为 "AmyJohnson "的用户设置新密码的示例：

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

通过使用这些与安全相关的 cmdlet，管理员可以在 Active Directory 环境中有效地管理用户访问、组成员资格和密码策略。

## PowerShell 的活动目录模块脚本示例
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## 结论

总之，PowerShell 的**活动目录模块**是一个功能强大的工具，可以高效、便捷地管理 Windows 活动目录。通过安装和导入该模块，您可以访问一整套**cmdlets**，从而简化各种与活动目录相关的任务。

使用活动目录模块，您可以执行各种操作，如检索有关活动目录对象的信息、创建新对象、修改属性和管理安全性。该模块使管理员能够自动执行管理任务、简化工作流程并确保 Active Directory 环境的顺利运行。

利用**PowerShell**和**活动目录模块**，您可以增强您的活动目录管理能力，提高活动目录管理流程的效率。无论您是系统管理员、IT 专业人员还是活动目录经理，活动目录模块都能为您提供有效管理活动目录基础架构的必要工具。

利用**PowerShell**和**活动目录模块**的强大功能，简化您的活动目录管理任务，提高工作效率，并维护一个安全、有序的活动目录环境。

{{< inarticle-dark >}}

## 参考文献

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
