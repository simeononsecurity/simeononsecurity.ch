---
title: "掌握用于 vSphere 管理的 PowerCLI"
date: 2023-08-02
lastmod: 2026-11-14
toc: true
draft: false
description: "了解如何使用 PowerCLI 管理 VMware vSphere、自动执行任务并提高效率。"
genre: ["技术", "虚拟化", "VMware", "IT 管理", "自动化", "命令行界面", "脚本编写", "系统管理", "云计算", "数据中心管理"]
tags: ["PowerCLI", "VMware PowerCLI", "安装 PowerCLI", "PowerCLI 安装", "下载 PowerCLI", "PowerCLI 下载", "PowerCLI 连接 vCenter", "vSphere 管理", "虚拟机管理", "主机管理", "自动化", "脚本编写", "虚拟化", "vCenter Server", "ESXi 主机", "数据存储管理", "网络适配器管理", "创建虚拟机", "删除虚拟机", "虚拟机设置", "主机资源管理", "CPU 分配", "内存分配", "存储设置", "PowerCLI 示例", "PowerCLI 文档", "IT 管理", "系统管理", "云计算"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "插图中，一名用户通过 PowerCLI 命令管理 vSphere 环境中的虚拟机和主机。"
coverCaption: "使用 PowerCLI 提升 vSphere 管理效率"
---

## 简介

**PowerCLI** 是 **VMware** 提供的**命令行界面（CLI）**工具，可帮助管理员**管理和自动化** **VMware vSphere 环境**。无论你是新手还是有经验的用户，丰富的 **cmdlet** 都能简化管理任务并提高效率。本文介绍安装 PowerCLI、连接 vCenter，以及有效使用其功能的方法。

______

## 安装 PowerCLI

先在计算机上安装 PowerCLI：

1. 从 VMware 官方网站**下载** PowerCLI 安装程序。链接位于 [PowerCLI 文档](https://code.vmware.com/web/dp/tool/vmware-powercli)。请选择适用于操作系统的版本。
2. **运行**安装程序并按屏幕提示操作。选择安装位置和其他选项。
3. 单击“Finish”完成安装。随后即可使用 PowerCLI。

______

## 使用 PowerCLI 连接 vCenter

安装后，连接 vCenter Server，即可使用 PowerCLI cmdlet 管理虚拟基础设施。

1. 从“开始”菜单或桌面快捷方式启动 PowerCLI。
2. 运行以下命令连接 vCenter：

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

将 `<vCenter IP or hostname>` 替换为 vCenter Server 的实际 IP 地址或主机名。

3. 按提示输入具有足够 vCenter 管理权限的账户凭据。
4. 使用 **Get-VMHost** 等简单命令验证连接。如果显示 ESXi 主机列表，说明连接成功。

______

## 使用 PowerCLI 管理 vSphere

连接 vCenter 后，可以执行以下常见任务。

### 获取信息

PowerCLI 提供许多 cmdlet 来查询 vSphere 环境：

- **Get-VM**：获取虚拟机信息。
- **Get-VMHost**：获取 ESXi 主机信息。
- **Get-Datastore**：获取数据存储信息。
- **Get-NetworkAdapter**：获取网络适配器信息。

使用参数筛选结果并设置输出格式。

### 自动执行任务

PowerCLI 的一项主要优势是自动执行重复任务。几行代码即可同时对多个对象执行复杂操作。

#### 为文件夹中的所有虚拟机创建快照

```PowerShell
## 关闭指定主机上的所有虚拟机
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## 为指定文件夹中的所有虚拟机创建快照
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

此脚本展示如何使用 PowerCLI 关闭指定主机上的虚拟机，并为指定文件夹中的虚拟机创建快照。

#### 安全关闭文件夹中的所有虚拟机

```PowerShell
## 获取包含待关闭虚拟机的文件夹
$folder = Get-Folder -Name "MyFolder"

## 获取指定文件夹中的所有虚拟机
$vms = Get-VM -Location $folder

## 正常关闭所有虚拟机
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

此脚本可正常关闭指定文件夹中的所有虚拟机。`Get-Folder` 先查找文件夹，`Get-VM` 再获取其中的虚拟机。`foreach` 循环逐一检查虚拟机。如果电源状态为“PoweredOn”，`Shutdown-VMGuest` 会执行正常关机；参数 `-Confirm:$false` 会跳过确认提示。

使用此脚本可以有序关闭文件夹中的虚拟机。PowerCLI 脚本功能也能帮助你创建符合需求的自动化工作流。

### 管理虚拟机和主机

PowerCLI 可执行多种虚拟机与主机管理任务：

- **创建和移除虚拟机**：使用 **`New-VM`** 和 **`Remove-VM`** 等 cmdlet。创建时，**[命令 New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** 支持 CPU、内存、磁盘和网络参数。
- **修改虚拟机设置**：调整 CPU、内存、磁盘和网络配置。**[命令 Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** 可更改 CPU 和内存分配。
- **管理主机资源**：管理 CPU、内存、网络和存储。**[命令 Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** 可修改主机网络和存储配置。

以上只是 PowerCLI 管理 vSphere 的部分示例。丰富的 cmdlet 让你能够自动执行并简化各种管理任务。

## 结论

**PowerCLI** 是管理和自动化 VMware vSphere 环境的实用工具。其丰富的 cmdlet 能简化管理任务并提高效率。安装并连接 vCenter 后，你可以查询信息、自动执行任务，并高效管理虚拟机和主机。

现在就开始探索 PowerCLI，简化 vSphere 管理。


## 参考资料
- [PowerCLI 文档](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer：VMware PowerCLI cmdlet 参考](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM：VMware PowerCLI cmdlet 参考](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)
