---
title: "保护 Windows 免受推测执行边信道攻击"
date: 2020-06-18
toc: true
draft: false
description: "了解如何使用 Microsoft 的缓解脚本和固件更新来保护您的 Windows 系统免受推测执行边信道攻击"
tags: ["Windows 幽灵崩溃缓解脚本", "推测执行侧通道攻击", "微软", "英特尔", "超微", "通过", "手臂", "安卓", "铬合金", "苹果系统", "苹果系统", "分支目标注入", "边界检查绕过", "流氓数据缓存加载", "投机商店旁路", "微架构数据采样", "CVE", "固件更新", "GitHub 资料库", "电源外壳"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**用于针对 Windows 系统中的推测执行侧通道漏洞实施保护的简单脚本。**

Microsoft 注意到一类新的公开披露的漏洞，称为“推测执行侧信道攻击”，它会影响许多现代处理器，包括 Intel、AMD、VIA 和 ARM。

**注意：**此问题还会影响其他操作系统，例如 Android、Chrome、iOS 和 macOS。因此，我们建议客户向这些供应商寻求指导。

我们已经发布了多个更新来帮助缓解这些漏洞。我们还采取了措施来保护我们的云服务。有关详细信息，请参阅以下部分。

我们尚未收到任何信息表明这些漏洞被用来攻击客户。我们正在与包括芯片制造商、硬件 OEM 和应用程序供应商在内的行业合作伙伴密切合作，以保护客户。要获得所有可用的保护，需要固件（微码）和软件更新。这包括来自设备 OEM 的微代码，在某些情况下，还包括防病毒软件的更新。

**本文解决了以下漏洞：**
- CVE-2017-5715 – “分支目标注入”
- CVE-2017-5753 – “绕过边界检查”
- CVE-2017-5754 – “流氓数据缓存加载”
- CVE-2018-3639 – “投机商店旁路”
- CVE-2018-11091 – “微架构数据采样不可缓存内存 (MDSUM)”
- CVE-2018-12126 – “微架构存储缓冲区数据采样 (MSBDS)”
- CVE-2018-12127 – “微架构填充缓冲区数据采样 (MFBDS)”
- CVE-2018-12130 – “微架构加载端口数据采样 (MLPDS)”

**更新于 2019 年 8 月 6 日** 2019 年 8 月 6 日，英特尔发布了有关 Windows 内核信息泄露漏洞的详细信息。此漏洞是 Spectre Variant 1 推测执行侧信道漏洞的变体，已分配为 CVE-2019-1125。

**于 2019 年 11 月 12 日更新** 2019 年 11 月 12 日，英特尔发布了一份关于英特尔® 事务同步扩展（英特尔® TSX）事务异步中止漏洞的技术公告，该漏洞被分配为 CVE-2019-11135。 Microsoft 已发布更新以帮助缓解此漏洞，并且默认情况下为 Windows 客户端操作系统版本启用操作系统保护。

## 建议措施
客户应采取以下措施来帮助防范漏洞：

- 应用所有可用的 Windows 操作系统更新，包括每月的 Windows 安全更新。
- 应用设备制造商提供的适用固件（微码）更新。
- 根据 Microsoft 安全公告中提供的信息评估您的环境的风险：ADV180002、ADV180012、ADV190013 以及本知识库文章中提供的信息。
- 根据需要使用本知识库文章中提供的建议和注册表项信息采取措施。

## 下载所需文件：

从中下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## 如何运行脚本：

**脚本可以从提取的 GitHub 下载中启动，如下所示：**
```
.\sos-spectre-meltdown-mitigations.ps1
```
