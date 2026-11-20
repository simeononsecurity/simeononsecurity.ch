---
title: "将 Hyper-V 虚拟机迁移到 Proxmox VE：可回退检查清单"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "通过停机源导出、匹配固件、导入磁盘、隔离启动测试和回滚方案，将一台 Hyper-V 虚拟机迁移到 Proxmox VE。"
genre: ["虚拟化", "系统管理", "家庭实验室"]
tags: ["Hyper-V 到 Proxmox 迁移", "Hyper-V 迁移", "Proxmox VE 迁移", "VHDX 导入", "qm disk import", "虚拟机切换", "Hyper-V 导出", "Proxmox 上的 Windows 虚拟机", "Proxmox 上的 VirtIO", "虚拟机回滚", "UEFI 迁移", "Hyper-V 检查点", "虚拟 TPM", "BitLocker 恢复", "家庭实验室迁移"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "一块磁盘沿桥从蓝色服务器机架移向橙色机架，旁边有一条独立返回路径和目标端的盾牌。"
coverCaption: "在新虚拟机通过切换检查前，保留源虚拟机可用。"
---

**Hyper-V 导出** 会保留虚拟机文件，而 Proxmox VE 需要新的客户机配置并导入 VHDX 虚拟磁盘文件。文件复制成功并不能证明客户机可以启动或提供服务。本清单通过源机停机导出、受控启动测试和有明确返回路径的切换来迁移一台虚拟机。

<!--more-->

## 关键要点

- **记录源配置：** 导出前记录固件代数、磁盘路径、检查点、网络设置和加密状态。
- **停止写入：** 最终导出前关闭 Hyper-V 虚拟机，并在 Proxmox 测试期间保持关机。
- **匹配启动路径：** Hyper-V 第 1 代使用传统 BIOS，第 2 代使用 UEFI。
- **验证服务：** 退役源机前检查数据、网络访问、备份和客户机健康状况。

## 开始前

安排维护窗口，并先用可丢弃的虚拟机测试。你需要 Hyper-V 和 Proxmox VE 管理员权限、导出存储空间，以及一份与迁移副本分开的已验证备份。留出传输全部虚拟磁盘和测试客户机应用的时间。停机时长取决于磁盘大小和传输速度。

本流程适用于带虚拟磁盘的普通虚拟机。 **受保护虚拟机、直通磁盘、共享磁盘、集群工作负载和硬件绑定许可** 需要专门计划。记录切换负责人和最晚回滚时间。不要在生产网络上同时启动具有相同机器身份的两份副本。

| 源端信息 | 用途 |
|---|---|
| **虚拟机代数和固件** | 在 Proxmox 中选择 SeaBIOS 或 OVMF |
| **安全启动状态和模板** | 匹配启动策略并注册兼容密钥 |
| **启动盘和数据盘** | 按正确顺序导入所有必需的 VHDX 虚拟磁盘文件 |
| **检查点和 AVHDX 文件** | 避免把差异磁盘当作独立基础磁盘 |
| **IP、DNS、MAC 和 VLAN** | 恢复连接且不产生重复身份 |
| **vTPM 和 BitLocker** | 更改虚拟硬件前准备恢复方式 |
| **服务和数据检查** | 定义成功和回滚所需证据 |

第 1 代使用传统 BIOS。第 2 代使用统一可扩展固件接口（UEFI）。 **AVHDX 文件** 是链接到基础 VHDX 的 Hyper-V 差异磁盘。 **vTPM** 是供 BitLocker 等功能使用的虚拟可信平台模块。 **VLAN** 是在共享网络硬件上承载的独立逻辑网络。

**SeaBIOS** 提供传统 BIOS 固件。 **OVMF** 提供 UEFI 固件。 **VirtIO** 是一种快速虚拟设备接口，需要客户机驱动程序。 **initramfs** 是 Linux 的早期启动文件系统，会在主系统启动前加载驱动程序。

## 盘点 Hyper-V 中的虚拟机

在 Hyper-V 主机上以提升权限的 PowerShell 会话运行以下只读命令。这些示例尚未实测。使用前，请根据已安装的 Hyper-V 模块和变更流程确认每条命令。按提示输入虚拟机名称：

```powershell
$vmName = Read-Host "Hyper-V 虚拟机名称"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

[Hyper-V PowerShell 模块文档](https://learn.microsoft.com/en-us/powershell/module/hyper-v/)介绍这些盘点命令。将磁盘路径与虚拟机设置核对，并列出已连接的 ISO、数据盘、虚拟交换机、静态地址或 DHCP 保留。记录客户机操作系统和应用版本。通过恢复测试副本或检查近期有记录的恢复结果来验证备份。仅复制文件而不测试恢复，证据较弱。

对 **第 2 代** 虚拟机，也记录固件和安全设置：

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

记录 **安全启动** 状态、模板和 vTPM 设置。Microsoft 的[**`Get-VMFirmware`** 参考](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware)说明该命令只适用于第 2 代。 [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity)会报告虚拟机安全配置。不要对第 1 代客户机运行 **`Get-VMFirmware`** 。 **MAC 地址** 标识网络接口。 **DNS** 将名称映射到地址。 **DHCP** 分配网络设置。 **EFI 磁盘** 保存 UEFI 设置。

**最终导出前先处理检查点。** Microsoft 说明 Hyper-V 导出会收集检查点文件和 VHDX 磁盘。通过 Hyper-V 删除检查点会合并其差异磁盘。不要在文件系统中删除 **`.avhdx`** 文件来清除检查点。如果合并失败或磁盘链不完整，请停止并遵循 [Microsoft 检查点恢复指南](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks)。[Microsoft 检查点指南](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints)说明常规删除和合并流程。

对于使用 **BitLocker** 或 **虚拟 TPM** 的 Windows 客户机，更改虚拟硬件前先取得并验证恢复密钥。Hyper-V 的[第 2 代安全文档](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features)介绍由 vTPM 支持的加密。Microsoft 的 [BitLocker 常见问题](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq)说明启动变更为何会触发恢复。新的 Proxmox TPM 设备不会复制旧 TPM 状态。将密钥保存在导出的虚拟机之外。

## 导出已停止的虚拟机

正常关闭客户机。确认 Hyper-V 显示 **Off** (已关闭)，而不是 Saved (已保存)。等待检查点合并完成，再将虚拟机导出到可用空间充足的位置。在 Hyper-V Manager 中右键单击虚拟机，选择 **Export** (导出)，再选择目标位置。PowerShell 等效命令如下：

```powershell
$vmName = Read-Host "已停止的 Hyper-V 虚拟机名称"
$exportPath = Read-Host "导出目标目录"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "请停止虚拟机，并等待 Hyper-V 显示 Off (已关闭) 后再导出。" }
Export-VM -Name $vmName -Path $exportPath
```

[Microsoft 导出指南](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines)说明导出内容包括虚拟磁盘、配置和检查点文件。[**`Export-VM`** 参考](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm)定义此命令。确认目标位置包含预期磁盘文件且容量正确。保留已停止的源虚拟机和独立备份。 **导入期间不要修改导出文件。**

将 VHDX 文件传到 Proxmox 主机可访问的路径。把导出内容视为敏感客户机数据。使用加密传输，限制传输位置和目标存储的访问，并在验证后删除临时副本。检查传输位置和目标存储的可用容量。保留未经修改的导出文件以便回滚。如果导出中有 **`.avhdx`** 文件，不要仅凭文件名选择基础 **`.vhdx`**，并假设其含有最新写入。继续前先在 Hyper-V 解决磁盘链。

## 创建目标 Proxmox 虚拟机

在 Proxmox 网页界面创建新虚拟机，使用此前记录的客户机操作系统类型、CPU 和内存。选择一个未使用的新虚拟机 ID。不要安装全新的操作系统。导入源磁盘前，移除向导创建的空磁盘。首次启动时让网卡与生产网桥断开，或接入隔离测试网络。

| Hyper-V 源配置 | Proxmox 目标配置 |
|---|---|
| **第 1 代，传统 BIOS** | SeaBIOS |
| **第 2 代，UEFI** | OVMF、EFI 磁盘和匹配的安全启动策略 |
| **没有 VirtIO 存储驱动的 Windows 启动盘** | 初始以 SATA 连接 |
| **带 vTPM 或 BitLocker 的 Windows** | 必要时添加新的 TPM 状态设备，并在首次启动前备好恢复密钥 |

[Microsoft 虚拟机代数指南](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V)将第 1 代映射到传统 BIOS、第 2 代映射到 UEFI。Proxmox 的[虚拟机文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)介绍 SeaBIOS、OVMF 以及用于保存 UEFI 设置的 EFI 磁盘。 **匹配源端启动模式。** 迁移期间更改模式会引入新的启动问题。

若源端是第 2 代，请匹配 **安全启动** 是否已启用。检查源端模板，并为客户机选择兼容且已注册的密钥。Hyper-V 模板名称不会迁移到 Proxmox。Proxmox 的 4 MB EFI 磁盘和 **Pre-Enroll keys**（预先注册密钥）选项提供安全启动密钥，且默认启用安全启动。切换前验证目标端启动行为。[Microsoft 固件参考](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware)说明源端模板要求。[Proxmox EFI 磁盘文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)说明目标端密钥。

更改 EFI 密钥前，确认恢复密钥已托管，并记录当前保护器 ID。按已安装的 Proxmox VE 和 OVMF 文档注册 EFI 密钥。再次核对恢复密钥，并在首次启动前验证 `manage-bde -status`。不要把暂停、禁用或删除保护器作为通用迁移步骤。记录固件包版本、安全启动状态和固件版本，以及 BitLocker 状态。

若源端使用 **vTPM**，首次启动前在 Proxmox 的 Hardware (硬件) 面板添加 **TPM State** (TPM 状态) 。除非客户机有记录在案的 1.2 版本要求，否则选择 **版本 2.0** 。这会创建新的 TPM 状态，不会复制 Hyper-V 中原有的虚拟 TPM 状态。启用 BitLocker 的客户机首次启动时需要已验证的恢复密钥。[Proxmox TPM 文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)介绍 Hardware (硬件) 操作和版本。

Windows 启动盘先使用 SATA，除非客户机已有必需的 VirtIO 存储驱动。成功启动后安装受支持的 VirtIO 驱动，每次只更改一个虚拟设备。Proxmox 推荐使用 VirtIO SCSI 以提升性能，但缺少启动驱动会导致 Windows 无法访问系统盘。Linux 切换总线前，检查 initramfs 是否包含目标存储驱动。[Proxmox 虚拟机文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)介绍磁盘控制器。

## 导入并连接磁盘

在 Proxmox 主机检查已复制的 VHDX 路径。以下示例将磁盘导入虚拟机 ID **230**，并存入 ID 为 **`local-lvm`** 的存储。将三个值替换为实际值：

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Proxmox 的[**`qm disk import`** 参考](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc)说明源映像会作为 **未使用磁盘** 导入。[QEMU 映像文档](https://www.qemu.org/docs/master/system/images)将 VHDX 列为支持的转换格式。分别导入每个数据盘。等待每项导入任务完成，并将导入后的磁盘大小与源端盘点结果比较。

在虚拟机的 **Hardware** (硬件) 面板中，首次启动 Windows 时将未使用的启动盘连接为 **SATA** 。按记录的顺序连接数据盘。在 **Options > Boot Order** (选项 > 启动顺序) 中选择启动盘。对于第 2 代客户机，确认使用 **OVMF** 和 EFI 磁盘。验证通过前保留导入文件和源虚拟机。

## 切换前测试

在隔离网络上启动 Proxmox 客户机。通过控制台检查启动画面、操作系统登录、磁盘卷、应用数据和服务日志。看到登录提示并不能证明迁移成功。执行导出前记录的检查，包括代表性事务或近期数据读取。

若客户机启用了 BitLocker，出现提示时用恢复密钥解锁。Windows 启动后，在提升权限的命令提示符中检查系统卷保护状态和保护器：

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

Microsoft 的 [BitLocker 操作指南](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide)介绍保护器检查和恢复密钥备份。输出包含敏感恢复材料。不要将其粘贴到工单或公开日志。按策略确认所需保护器，并托管当前恢复方式。重启客户机，确认切换前不会再次出现恢复提示。反复触发恢复意味着迁移检查失败，并不表示应丢弃原密钥。

| 测试 | 通过条件 |
|---|---|
| **启动和磁盘** | 客户机启动，所有预期卷均已挂载 |
| **安全启动和 BitLocker** | 启动策略符合预期，加密客户机重启时不再重复恢复 |
| **应用** | 代表性读取或事务成功 |
| **网络** | 所需对等端能通过预期端口访问测试客户机 |
| **恢复** | 退役源机前，Proxmox 备份和隔离恢复测试成功 |
| **运维** | 监控、时间同步、关机和客户机代理按预期工作 |

应用检查通过后，在维护窗口切换生产网络路径或地址。保持 Hyper-V 关闭。更换虚拟网卡可能需要新的 DHCP 保留，或在客户机中修正静态地址。从另一台客户端检查 DNS、防火墙规则和依赖服务。Proxmox 的[虚拟机文档](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)介绍网络设备和客户机代理选项。

## 故障排查和回滚

| 症状 | 首要检查 |
|---|---|
| **没有启动设备** | 启动顺序、导入的启动盘、BIOS 或 UEFI 模式，以及安全启动密钥 |
| **Windows 存储错误** | SATA 连接和缺失的 VirtIO 存储驱动 |
| **BitLocker 反复要求恢复** | 新 TPM 状态、安全启动策略、启动测量和保护器 |
| **客户机启动后没有网络** | 新虚拟网卡、网桥、VLAN、DHCP 保留和静态地址 |
| **数据陈旧或缺失** | VHDX 选错、导出不完整、检查点链或数据盘缺失 |

若必要测试在回滚截止时间前失败，停止 Proxmox 虚拟机并断开其生产网络。恢复源端网络路径，再启动原 Hyper-V 虚拟机。 **绝不要让两份副本以相同生产身份同时运行。** 返回 Hyper-V 前记录 Proxmox 副本接收的写入。这些写入需要单独恢复或协调，因为源磁盘没有收到它们。

保留源虚拟机和导出文件，直到 Proxmox 客户机通过服务检查、完成新备份和隔离恢复测试，并经过约定的观察期。网站的[虚拟化平台比较](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/)有助于选择平台。[Proxmox VE 升级指南](/articles/proxmox-ve-8-to-9-upgrade-guide/)介绍后续维护。 **只有工作负载和恢复路径都能在新主机上正常工作，迁移才算结束，磁盘导入完成并不代表结束。**

## 后续步骤

在工作负载、备份和回滚检查于约定观察期内全部通过前，保留源虚拟机和导出文件。退役源机前，查看 [Proxmox 虚拟机备份恢复演练](/articles/proxmox-vm-backup-restore-drill/)。
