---
title: "掌握 VMware 安全"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "本指南介绍如何使用 PowerCLI 应用 VMware STIG 并保护 VMware 环境。"
genre: ["网络安全", "虚拟化", "IT 基础设施", "自动化", "PowerShell", "VMware", "STIG", "合规", "脚本", "数据中心"]
tags: ["PowerCLI", "VMware STIG", "VMware 安全", "自动化", "脚本", "PowerShell", "ESXi", "虚拟化", "合规", "网络安全", "如何使用 PowerCLI 应用 VMware STIG", "使用 PowerCLI 自动化 VMware 安全", "用于实施 VMware STIG 的 PowerCLI 脚本", "用于 ESXi 安全的 PowerCLI 自动化", "使用 PowerCLI 保护 VMware 环境"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "一台由挂锁保护的计算机服务器插图，象征安全的 VMware 基础设施。"
coverCaption: "使用 PowerCLI 保护 VMware 环境"
---

**如何使用 PowerCLI 应用 VMware STIG**

PowerCLI 是一种自动化和脚本工具，可通过 PowerShell 管理和配置 VMware 环境。本文介绍如何使用 PowerCLI 将 VMware STIG（Security Technical Implementation Guide）应用到 ESXi 和虚拟机。

## 简介

**VMware STIG** 提供安全配置和管理 VMware 基础设施的指导与建议。遵循这些要求有助于组织加强 VMware 部署的安全，并满足适用的政府要求，例如 **Defense Information Systems Agency (DISA) STIG**。

## 什么是 PowerCLI？

**PowerCLI** 是用于管理 VMware 环境的命令行界面和脚本工具。它基于 PowerShell，提供大量专为 VMware 管理设计的 cmdlet。管理员可用它自动执行重复任务、修改配置，并收集 VMware 基础设施信息。

### 安装和要求

开始使用 PowerCLI 和 VMware STIG 前，请确认满足以下条件：

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)：从 PowerShell Gallery 安装 PowerCLI，运行命令 `Install-Module VMware.PowerCLI -force`。
- [**PowerShell 5 或更高版本**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)：确认已安装 PowerShell 5 或更高版本。
- [**ESXi 6.7 U2 或更高版本**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)：使用 ESXi 6.7 U2 或更高版本。

## 自动化 VMware VCSA STIG

VMware ESXi STIG 提供保护 ESXi 主机的指导。自动应用 STIG 控制项可简化流程，并让多台主机保持一致配置。

### 注意事项

开始自动化前，请考虑以下事项：

- **确认 ESXi 主机或集群上的虚拟机和来宾系统均不需要 CD、USB 或软盘功能。**
- **对所有连接到 vCenter 的 ESXi 主机和来宾系统应用 STIG。**
- **准备好故障排除技能，以处理过程中可能出现的问题。**

### 脚本：自动化 VMware VCSA STIG

以下 PowerCLI 脚本用于自动应用适用于 VCSA 的部分 STIG 控制项：

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#连接到每台 vCenter 服务器
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#自动化

Write-Host "漏洞 ID: V-243098 规则 ID: SV-243098r719537_rule STIG ID: VCTR-67-000036"
Write-Host "如果 'config.log.level' 的值未设为 "info" 或不存在，则属于发现项。"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "漏洞 ID: V-243090 规则 ID: SV-243090r719513_rule STIG ID: VCTR-67-000024"
Write-Host "如果 'config.vpxd.hostPasswordLength' 的值不是 "32"，则属于发现项。
如果此设置不存在，则不属于发现项。"
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "漏洞 ID: V-243089 规则 ID: SV-243089r719510_rule STIG ID: VCTR-67-000023"
Write-Host "如果 'VirtualCenter.VimPasswordExpirationInDays' 的值不是 "30" 或不存在，则属于发现项。"
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "漏洞 ID: V-243084 规则 ID: SV-243085r719498_rule STIG ID: VCTR-67-000016"
Write-Host "如果已配置 NetFlow，但收集器 IP 未知且未记录，则属于发现项。"
$pgs = Get-VDPortgroup | Get-View
ForEach ($pg in $pgs) {
    $spec = New-Object VMware.Vim.DVPortgroupConfigSpec
    $spec.configversion = $pg.Config.ConfigVersion
    $spec.defaultPortConfig = New-Object VMware.Vim.VMwareDVSPortSetting
    $spec.defaultPortConfig.ipfixEnabled = New-Object VMware.Vim.BoolPolicy
    $spec.defaultPortConfig.ipfixEnabled.inherited = $false
    $spec.defaultPortConfig.ipfixEnabled.value = $false
    $pg.ReconfigureDVPortgroup_Task($spec)
}
Get-VDPortgroup | Select-Object Name, VirtualSwitch, @{N = "NetFlowEnabled"; E = { $_.Extensiondata.Config.defaultPortConfig.ipfixEnabled.Value } }

Write-Host "漏洞 ID: V-243084 规则 ID: SV-243084r719495_rule STIG ID: VCTR-67-000015"
Write-Host "vCenter Server 必须将分布式端口组的 Promiscuous Mode 策略设为拒绝。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "漏洞 ID: V-243083 规则 ID: SV-243083r719492_rule STIG ID: VCTR-67-000014"
Write-Host "vCenter Server 必须将分布式端口组的 MAC Address Change 策略设为拒绝。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "漏洞 ID: V-243082 规则 ID: SV-243082r719489_rule STIG ID: VCTR-67-000013"
Write-Host "vCenter Server 必须将分布式端口组的 Forged Transmits 策略设为拒绝。"
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "漏洞 ID: V-243081 规则 ID: SV-243081r719486_rule STIG ID: VCTR-67-000012"
Write-Host "vCenter Server 必须禁用分布式虚拟交换机运行状况检查。"
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "漏洞 ID: V-243077 规则 ID: SV-243077r719474_rule STIG ID: VCTR-67-00000"
Write-Host "vCenter Server 必须启用 Network I/O Control (NIOC)，管理过量容量、带宽或其他冗余，以限制信息洪泛类拒绝服务 (DoS) 攻击的影响。"
Write-Host "如果未创建并启用 syslog 故障告警，则属于发现项。"
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#手动审查

Write-Host "漏洞 ID: V-243076 规则 ID: SV-243076r719471_rule STIG ID: VCTR-67-000005"
Write-Host "必须为 vCenter Server 用户分配正确的角色。"
Write-Host "必须记录应用服务帐户和用户所需的权限。
如果用户或服务帐户拥有超出需要的权限，则属于发现项。"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "漏洞 ID: V-243119 规则 ID: SV-243119r719600_rule STIG ID: VCTR-67-000064"
Write-Host "如果 Administrator 以外的任何角色或站点特定组拥有这些权限，则属于发现项。"
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role 拥有加密权限"
    }
}

Write-Host "漏洞 ID: V-243118 规则 ID: SV-243118r719597_rule STIG ID: VCTR-67-000063"
Write-Host "如果 Solution Users 以外的用户拥有 "Administrator" 角色，且未被明确指定执行加密操作，则属于发现项。"
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "漏洞 ID: V-243111 规则 ID: SV-243111r719576_rule STIG ID: VCTR-67-000055"
Write-Host "如果没有启用 vSAN 集群，则不适用。"
Write-host "如果已启用 vSAN，且数据存储名称为 'vsanDatastore'，则属于发现项。"
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "发现已启用的 vSAN 集群"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "未启用 vSAN，此发现项不适用"
}

Write-Host "如果用户或服务帐户拥有超出需要的权限，则属于发现项。"
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "漏洞 ID: V-243088 规则 ID: SV-243088r719507_rule STIG ID: VCTR-67-000020"
Write-Host "检查端口组 VLAN 标签，确认未使用保留的 VLAN ID。"
Write-Host "某些物理交换机会为内部用途保留特定 VLAN ID，并通常禁止配置为这些值的流量。例如，Cisco Catalyst 通常保留 VLAN 1001–1024 和 4094，Nexus 通常保留 3968–4047 和 4094。"
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "漏洞 ID: V-243087 规则 ID: SV-243087r719504_rule STIG ID: VCTR-67-000019"
Write-Host "如果端口组配置为 'VLAN Trunk'，且没有记录所需的例外（例如 NSX 设备），则属于发现项。
如果允许 VLAN 中继，但未限制为所需的最小范围，则属于发现项。"
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "漏洞 ID: V-243078 规则 ID: SV-243078r719644_rule STIG ID: VCTR-67-000008"
Write-Host "vCenter Server 必须至少实时向 SA 和 ISSO 立即告警所有审计失败事件。"
Write-Host "如果未创建并启用 syslog 故障告警，则属于发现项。"
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

该脚本执行以下操作：

- **首先配置 PowerCLI、关闭证书验证，并退出客户体验改进计划 (CEIP)。**
- **随后连接到 `$vcenters` 变量中指定的 vCenter 服务器。**
- **使用 PowerCLI cmdlet 处理各项 STIG 控制。例如，将指定 vCenter 服务器的 `config.log.level` 设为 info。**
- **还会处理 `config.vpxd.hostPasswordLength` 和 `VirtualCenter.VimPasswordExpirationInDays` 等控制项。**
- **最后检查并配置安全策略及其他设置。**
- **这只是示例脚本，请根据环境和 STIG 要求调整。**

______

## 自动化 VMware VM STIG

除了保护 ESXi 主机，还要对 VMware 基础设施中的虚拟机应用 STIG 控制。PowerCLI 可根据 STIG 指导自动配置虚拟机。

## 脚本：自动化 VMware VM STIG

以下 PowerCLI 脚本演示了如何为虚拟机自动应用部分 STIG 控制项：

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#来源： https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #加固/STIG 设置
    vmAdvSettings       = @{
        "isolation.tools.copy.disable"          = $true
        "isolation.tools.dnd.disable"           = $true
        "isolation.tools.paste.disable"         = $true
        "isolation.tools.diskShrink.disable"    = $true
        "isolation.tools.diskWiper.disable"     = $true
        "isolation.tools.hgfsServerSet.disable" = $true
        "RemoteDisplay.maxConnections"          = "1"
        "RemoteDisplay.vnc.enabled"             = $false
        "tools.setinfo.sizeLimit"               = "1048576"
        "isolation.device.connectable.disable"  = $true
        "tools.guestlib.enableHostInfo"         = $false
        "tools.guest.desktop.autolock"          = $true
        "mks.enable3d"                          = $false
    }
    vmAdvSettingsRemove = ("sched.mem.pshare.salt")
    vmotionEncryption   = "opportunistic" #disabled, required, opportunistic
}

ForEach ($vm in (Get-VM -Location $cluster | Where-Object { (Get-VM -Location $folder) -contains $_ } )) {
    Write-Output "...正在修复 $vcenter 上 $vm 的高级设置"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #获取每项指定设置的值
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...$vm 上的 $settingname 已正确设为 $settingvalue"
            }
            else {
                Write-Output "...$vm 上的 $settingname 原值 $($asetting.value) 不正确，正在设为 $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...$vm 上不存在 $settingname，正在创建设置..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...必要时移除 $vcenter 上 $vm 的高级设置"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #检查当前设置是否存在
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...$vm 上存在 $setting...正在移除设置"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...$vm 上不存在 $setting"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...$vm 的 vMotion 加密已正确设为 $($vmconfig.vmotionEncryption)"
        }
        else {
            $vmv = $vm | get-view
            $config = new-object VMware.Vim.VirtualMachineConfigSpec
            $config.MigrateEncryption = New-object VMware.Vim.VirtualMachineConfigSpecEncryptedVMotionModes
            $config.MigrateEncryption = "$($vmconfig.vmotionEncryption)"
            $vmv.ReconfigVM($config)
        }
    }
}
```

该脚本执行以下操作：

- **与 VMware VCSA STIG 脚本类似，先配置 PowerCLI 环境。**
- **连接到 vCenter，并选择包含目标虚拟机的集群和文件夹。**
- **`$vmconfig` 变量包含虚拟机的 STIG 设置，包括禁用复制和粘贴、限制远程显示连接等高级设置。**
- **遍历所选集群和文件夹中的每台虚拟机，并应用 STIG 设置。**
- **同时配置虚拟机的 vMotion 加密。**

此脚本仅作示例。请根据环境和适用的 STIG 要求进行修改。

_____

## 其他资源

- **DoD STIG VIB过去曾[提供给 5.0 至 6.7 版本](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)，目前已不再提供。**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey)提供了一些在 VMware 上实施 DoD STIG 的实用指导，建议阅读。
    - [VMware vSphere 8 STIG](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [VMware vSphere 7 STIG](https://core.vmware.com/vsphere-7-stig)
    - [VMware vSphere 6.7 STIG](https://core.vmware.com/vmware-vsphere-67-stig)
    - [VMware STIG PowerCLI](https://github.com/rlakey/vmware-stig-powercli)
        - [VMware VCSA 6.7 STIG 基线](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [VMware VM 6.7 STIG 基线](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## 结论

**应用 VMware STIG 有助于保护 VMware 基础设施并满足相关要求。PowerCLI 可自动化并简化对 ESXi 主机和虚拟机应用 STIG 控制项的过程。**

本文介绍了如何使用 PowerCLI 自动化 VMware ESXi STIG 和 VM STIG，说明了安装要求，提供了示例脚本，并强调应根据具体环境进行调整。

**借助 PowerCLI 和 STIG 指导，管理员可以高效保护 VMware 部署、减少手动工作，并保持配置一致。**

## 参考资料

- [DoD STIG VIB](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 或更高版本](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 或更高版本](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)
