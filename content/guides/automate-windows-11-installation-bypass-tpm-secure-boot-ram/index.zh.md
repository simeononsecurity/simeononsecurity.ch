---
title: "自动安装 Windows 11：绕过 TPM、安全启动和内存检查"
date: 2023-09-08
toc: true
draft: false
description: "使用 autounattend.xml 和 vTPM 绕过 TPM、安全启动和 RAM 检查，简化虚拟环境中的 Windows 11 安装。"
genre: ["技术", "视窗 11", "安装", "虚拟化", "自动化", "注册表密钥", "TPM 旁路", "安全启动旁路", "内存旁路", "vTPM"]
tags: ["视窗 11", "安装", "自动化", "虚拟化", "vTPM", "注册表密钥", "TPM 旁路", "安全启动旁路", "内存旁路", "Autounattend.xml", "VMware vSphere", "Windows Setup", "Windows 预装环境", "虚拟机", "Windows 安装解决方案", "注册表编辑器", "微软视窗设置", "系统要求", "视窗安全", "视窗性能", "政府法规", "符合 NIST 标准", "微软", "Windows 操作系统", "绕过检查", "Windows 部署", "设置自动化", "命令提示符", "技术指南", "自动安装 Windows 11", "VMware vSphere 中的 vTPM 配置", "绕过 Windows 11 要求"]
cover: "/img/cover/windows11-installation-cartoon.png"
coverAlt: "一幅卡通风格的图片，展示了虚拟机在虚拟化环境中安装 Windows 11 的过程，一位面带微笑的 IT 专业人员正在监督这一过程。"
coverCaption: "用微笑简化安装自动安装 Windows 11"
---

**在虚拟化环境中自动安装 Windows 11**

## **简介**

Windows 11 引入了新的系统要求，包括需要 TPM（可信平台模块）、安全启动和足够的 RAM。虽然这些要求增强了安全性和性能，但在没有本机 TPM 支持的虚拟化环境中安装 Windows 11 时，它们可能会带来挑战。不过，有一些变通方法可以绕过这些检查并成功安装 Windows 11。

### **绕过 Windows 11 中的 TPM、安全启动和内存检查**

VMware vSphere 等虚拟化环境可以利用虚拟 TPM (vTPM) 来模拟 TPM 2.0 设备，从而满足 Windows 11 安装的 TPM 要求。但是，在没有 vTPM 的情况下，可以使用以下**注册表密钥**来绕过安装过程中的检查：

- **BypassTPMCheck**：跳过 TPM 检查。
- **BypassSecureBootCheck**：绕过安全启动检查：跳过安全启动检查。
- **BypassRAMCheck**：跳过内存检查：跳过 RAM 检查。

```reg
[HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig]
"BypassTPMCheck"=dword:00000001
"BypassSecureBootCheck"=dword:00000001
"BypassRAMCheck"=dword:00000001
```

要在**手动安装**过程中手动绕过检查，请按照以下步骤操作：

1.遇到 "此电脑无法运行 Windows 11 "消息时，按 [Shift]+[F10] 键打开命令提示符。
2.使用**regedit**命令打开注册表编辑器。
3.在 **HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig** 下手动添加上述注册表值，值为 **dword:00000001**。
```powershell
# Create the LabConfig key if it doesn't exist
New-Item -Path "HKLM:\SYSTEM\Setup" -Name "LabConfig" -Force

# Set the registry values under LabConfig
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassTPMCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassSecureBootCheck" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SYSTEM\Setup\LabConfig" -Name "BypassRAMCheck" -Value 1 -Type DWord
```
4.退出命令提示符并关闭所有剩余对话框，继续设置。

### **使用 Autounattend.xml 自动安装**

对于虚拟化环境中的自动安装，可使用 **autounattend.xml** 文件指定配置设置。要在 autounattend.xml 文件中包含**旁路注册表密钥**，请使用**RunSynchronous**命令，如下所示：

```xml
<?xml version="1.0" encoding="utf-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
    <settings pass="windowsPE">
        <!-- Other settings -->
        <component name="Microsoft-Windows-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS" xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">            
            <RunSynchronous>
                <RunSynchronousCommand wcm:action="add">
                    <Order>1</Order>
                    <Description>BypassTPMCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassTPMCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>2</Order>
                    <Description>BypassSecureBootCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassSecureBootCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
                <RunSynchronousCommand wcm:action="add">
                    <Order>3</Order>
                    <Description>BypassRAMCheck</Description>
                    <Path>cmd /c reg add "HKLM\SYSTEM\Setup\LabConfig" /v "BypassRAMCheck" /t REG_DWORD /d 1</Path>
                </RunSynchronousCommand>
            </RunSynchronous>
            <!-- Other components and settings -->
        </component>
        <!-- Other settings -->
    </settings>
    <!-- Disk configurations and other sections -->
</unattend>
```

#### **谨慎使用并遵守法规**

**绕过**这些检查只能在特定情况下进行，例如在已采取适当安全措施的虚拟化环境中。必须**了解绕过这些要求的**影响，并评估潜在风险。

Windows 11 安装对 TPM 2.0 和安全启动的需求是基于 Microsoft 规定的系统要求。在某些情况下，例如在政府或监管环境中，绕过这些检查可能不符合特定的法规或安全标准。各组织应仔细考虑其要求，并咨询适用的法规，如**国家标准与技术研究院 (NIST)** 等政府机构的法规，以确保合规性。



## **结论**

按照本文概述的步骤，您可以在虚拟化环境中自动安装 Windows 11，并使用一个 `autounattend.xml`文件。不过，切记要谨慎行事，并了解绕过这些重要的安全和性能检查可能带来的后果。

## **参考资料**

1. [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
2. [Enable Virtual Trusted Platform Module for an Existing Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-4DBF65A4-4BA0-4667-9725-AE9F047DE00A.html)
3. [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)
4. [Windows 11 – autounattend.xml – BypassTPMCheck – BypassSecureBootCheck](https://iamroot.it/2021/10/06/windows-11-autounattend-xml-bypasstpmcheck-bypasssecurebootcheck/)
