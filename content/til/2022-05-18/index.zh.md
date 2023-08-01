---
title: "今天我学到了更多关于 WDAC 政策制定和实施的知识"
date: 2022-05-18
toc: true
draft: false
description: "今天，我学到了更多有关 Ansible 条件和变量管理的知识"
genre: ["自动化", "视窗安全", "应用控制", "Windows Defender", "WDAC", "Powershell", "威胁防护", "Windows Server 2019", "企业安全", "政策管理", "安全最佳做法"]
tags: ["自动化", "WDAC", "应用控制", "Windows Defender 应用程序控制", "Windows Defender", "Powershell", "微软文档", "制定 WDAC 政策", "政策部署", "基于脚本的部署", "多项 WDAC 政策", "定负荷装置", "可信应用", "拒绝政策", "安全措施", "政策管理", "企业安全", "威胁防护", "Windows 服务器", "视窗安全", "应用程序白名单"]
---

**SimeonOnSecurity 今天了解到的有趣内容**

今天，SimeonOnSecurity 更新了他的存储库 Windows-Defender-Application-Control-Hardening 并了解了 Windows Defender Application Control (WDAC)，这是 Windows 10 Enterprise 和 Windows Server 2019 的一项功能，通过控制设备上执行的内容来提供安全性。

SimeonOnSecurity 深入研究了有关 WDAC 的微软文档，发现了创建和部署策略的几个关键资源。他了解到如何使用参考计算机为固定工作量设备创建 WDAC 策略，如何使用脚本部署 WDAC 策略，以及如何针对不同场景使用多个策略。

此外，SimeonOnSecurity 还深入了解了创建 WDAC 拒绝策略的指南，使他能够更好地理解只允许受信任的应用程序在设备上运行，同时拒绝所有其他应用程序的概念。

总之，SimeonOnSecurity 对 Windows Defender 应用程序控制的探索进一步巩固了他对现代安全实践中应用程序控制重要性的理解。

## Repos 已更新：
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## WDAC 读数：
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)
