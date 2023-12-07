---
title: "使用 vTPM 提高虚拟机安全性：分步指南"
date: 2023-09-02
toc: true
draft: false
description: "通过我们全面的分步指南，使用 vTPM 增强虚拟机安全性，提供平台验证和 BitLocker 加密支持。"
genre: ["网络安全", "虚拟化", "虚拟软件", "vSphere", "安全", "可信平台模块", "vTPM", "访客操作系统", "加密", "平台认证"]
tags: ["虚拟可信平台模块", "vTPM 指南", "增强虚拟机安全", "平台认证", "比特锁加密", "VMware vSphere", "虚拟化安全", "网络安全", "访客操作系统保护", "虚拟机硬件", "TPM 2.0", "安全启动", "密码操作", "虚拟机安全最佳实践", "vCenter 服务器", "ESXi 主机", "EFI 固件", "主要提供商", "VMware 文档", "Windows 服务器", "Windows 7", "Linux 操作系统", "安全虚拟机配置", "安全功能", "vSphere 客户端", "虚拟芯片", "数据保护", "篡改检测", "虚拟机完整性验证", "VMware 安全"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "象征性插图显示了一个带有闪亮锁的虚拟机，代表通过 vTPM 增强的安全性。"
coverCaption: "开启前所未有的虚拟机安全性！"
---

## 为现有虚拟机启用虚拟可信平台模块

虚拟可信平台模块 (vTPM) 是一项重要的安全功能，可增强在虚拟机上运行的客户操作系统的安全性。本文将指导您完成在 VMware vSphere 环境中为现有虚拟机添加 vTPM 的过程，并提供分步说明和重要注意事项，以确保无缝实施。

______

## 先决条件

在继续向虚拟机添加 vTPM 之前，请确保满足以下先决条件：

1.**带有密钥提供程序的 vSphere 环境：** 确保 vSphere 环境已配置密钥提供程序。此步骤对于安全管理加密操作至关重要。请参阅 [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)以获得详细指导。

2.**支持的客户操作系统：** 确认客户操作系统与 vTPM 兼容。VMware vTPM 与 TPM 2.0 兼容，支持 Windows Server 2008 及更高版本、Windows 7 及更高版本和各种 Linux 发行版。

3.**虚拟机状态：** 在继续添加 vTPM 之前，确保要修改的虚拟机已关闭。

4.**ESXi 主机版本：** 环境中的 ESXi 主机必须运行 ESXi 6.7 或更高版本（适用于 Windows 客户操作系统）或 ESXi 7.0 Update 2（适用于 Linux 客户操作系统）。

5.**EFI 固件：** 虚拟机必须使用 EFI 固件才能支持 vTPM。

6.**所需的权限：** 验证您是否拥有添加和管理 vTPM 所需的加密操作权限。所需权限包括
   - 加密操作.克隆
   - 加密操作.加密
   - 加密操作.新建加密
   - 加密操作.迁移
   - 加密操作.注册虚拟机



## 添加虚拟可信平台模块（vTPM）

按照以下步骤将 vTPM 添加到现有虚拟机：

1.**连接到 vCenter Server：** 启动 vSphere Client 并登录 vCenter Server。

2.**打开虚拟机设置：** 在 vSphere Client 左侧的清单中找到要修改的虚拟机。右键单击虚拟机名称并选择 "编辑设置"。

3.**添加可信平台模块：** 在 "编辑设置 "对话框中，单击 "添加新设备 "按钮。从设备类型列表中选择 "可信平台模块"（vTPM）。

4.**确认选择：** 单击 "确定 "按钮将 vTPM 设备添加到虚拟机。

5.**验证添加：** 成功添加 vTPM 后，虚拟机的 "摘要 "选项卡将在 "虚拟机硬件 "窗格中显示 "虚拟可信平台模块"。

______

## 虚拟可信平台模块（vTPM）的优势

为虚拟机启用 vTPM 有几大好处：

1.**增强安全性：** vTPM 可为虚拟机创建虚拟化 TPM 2.0 芯片，提供基于硬件的安全功能，如安全启动和加密操作。这就加强了客户操作系统的安全态势。

2.**平台认证：** vTPM 允许虚拟机生成其自身状态的加密测量值，从而实现平台认证。该功能有助于验证虚拟机的完整性，确保其未被篡改。

3.**支持 BitLocker 加密：** 如果运行的是 Windows 客户操作系统，启用 vTPM 是在虚拟机磁盘上使用 BitLocker 加密的先决条件。这又增加了一层数据保护。



## 结论

为现有虚拟机实施虚拟可信平台模块（vTPM）是增强虚拟化基础架构安全性的关键一步。按照概述的步骤并确保满足所有先决条件，您就可以为客户操作系统启用增强的安全功能、平台验证和 BitLocker 加密支持。

有关 vSphere 版本和配置的具体细节，请务必参阅 VMware 官方文档。

______

## 参考资料

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

