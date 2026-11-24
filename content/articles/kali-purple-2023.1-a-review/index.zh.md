---
title: "Kali Purple 2023.1：更新与核心功能"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "回顾 Kali Purple 2023.1 的历史功能、工具与改进，并提供适用于当前安全实验室的参考链接。"
tags: ["Kali Linux", "Kali Purple", "2023.1", "道德黑客", "渗透测试", "网络安全", "工具", "漏洞利用框架", "Kali ARM 更新", "Kali NetHunter", "Kali 文档", "内核支持", "蓝牙支持", "LineageOS", "OneUI", "Radxa Zero", "单板计算机", "内核补丁", "社区贡献", "Kali Discord", "Linux 更新", "道德黑客发行版", "新功能", "改进", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "新工具和软件包", "ARM 设备支持", "Kali 文档", "政府法规"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Kali Linux 的三维龙形吉祥物坐在盾牌上，周围环绕着网络安全工具。"
coverCaption: ""
---

**Kali Purple 2023.1：评测**

Kali Purple 2023.1 是 Kali 防御性安全方向的首个技术预览版。它已不是最新的 Kali 版本。本文记录最初的发布内容，并补充当前参考资料，避免将 2023.1 的软件包版本误认为当前版本。

## Kali 当前状态

Kali 官方发布历史将 2026 年 6 月 29 日发布的 Kali 2026.2 列为 2026 年第二个滚动版本。该版本使用 Linux 内核 6.19 和 Xfce 4.20.7。[Kali 2026.2 发布说明](https://www.kali.org/blog/kali-linux-2026-2-release/)还介绍了 GNOME 50、KDE Plasma 6.6、从 `sources.list` 迁移到 `sources.list.d/kali.source`，以及虚拟机启动方面的变化。

Kali Purple 代表 Kali 中的防御方向和紫队实践。2023.1 公告将其描述为技术预览版，包含 SOC-in-a-box 参考架构、防御工具，以及按 NIST 网络安全框架划分的菜单类别。这些内容属于当时的历史范围。选择当前软件包时，请查看 Kali 的[元软件包文档](https://www.kali.org/docs/general-use/metapackages/)，只安装实验室所需的工具组。

*所有攻防安全练习都应在隔离且获准的实验室中进行。安装 Kali 并不代表你获准测试自己不拥有或不管理的系统。*

______

## Kali 壁纸和桌面更新

Kali Purple 2023.1 推出名为 Kali Sticker 的**新默认壁纸**，采用紫色背景并带有多个 Kali 主题贴纸。设计灵感来自 /u/Albert-III- 和 TJ_Null 的作品。

除了新壁纸，Kali Purple 2023.1 还更新了三种主要桌面环境：**Xfce、KDE 和 GNOME**。更新包括新功能、性能改进和错误修复。

______

## Xfce 4.18

**Xfce 4.18** 带来多项改进，包括：

- 改进界面缩放支持
- 更新 Thunar 文件管理器
- 便于自定义的面板配置

______

## KDE Plasma 5.27

**KDE Plasma 5.27** 更新包括：

- 新的窗口平铺系统
- 更美观的应用主题
- 更清晰、更实用的工具和小部件

______

## GNOME 更新

在 GNOME 中，Kali Purple 2023.1 改进了易用性。例如，按 F4 键即可在文件管理器的当前文件夹中快速打开终端。

______

## 默认内核设置和已知问题

Kali Purple 2023.1 更新了部分内核默认值，以提升易用性。

______

## 新工具和软件包

Kali Purple 2023.1 新增多种工具和软件包，增强其**渗透测试**和**道德黑客**能力。新增内容包括：

- **Rizin 0.3.0**: 现代化的逆向工程框架
- **Ghidra 10.1**: 开源软件逆向工程套件
- **Python 3.10**: 常用编程语言的最新版本

这些工具和现有软件包的更新扩展了 2023.1 预览版，为安全专业人员提供了更多选择。本节的版本号对应 2023.1 发布版，不代表 Kali 2026.2 中的软件包版本。

______

## ARM 设备支持

Kali Purple 2023.1 持续扩展对 ARM 设备的支持，新增对 **Radxa Zero** 等设备的兼容性，并改进对 **LG V20** 等现有设备的支持。因此，Kali 可运行在多种硬件上，从小型单板计算机到高性能智能手机。

______

## 文档与社区

Kali 团队更新了**文档**，增加指南、教程和故障排查提示，帮助用户充分使用 Kali Purple 2023.1。团队还表彰了为 Kali 作出贡献的社区成员，展现开源协作的价值和 Kali 社区的凝聚力。

______

## 政府法规

本文不讨论道德黑客或渗透测试相关的具体政府法规，但这些活动在许多司法辖区都受到监管。开展安全评估时，请先取得适当授权并遵守适用法律。相关资料包括：

- [《计算机欺诈和滥用法》（Computer Fraud and Abuse Act，CFAA）](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [《通用数据保护条例》（GDPR）](https://gdpr.eu/)

______

## 结论

**Kali Purple 2023.1** 是 Kali 防御性安全方向的首个预览版。它扩充了工具集、改进 ARM 设备支持并完善了文档。部署当前版本前，请查看 Kali 发布说明，并按实验室需求选择软件包。遵守适用法规，只在获得明确授权后测试系统。

______

## 参考资料

1. [Kali Linux 官方网站](https://www.kali.org/)
2. [Kali Linux 文档](https://www.kali.org/docs/)
3. [Kali Linux 下载](https://www.kali.org/get-kali/)
4. [《计算机欺诈和滥用法》（CFAA）](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [《通用数据保护条例》（GDPR）](https://gdpr.eu/)

______

## 更多资源

- [Kali Linux 官方论坛](https://forums.kali.org/)
- [Kali Linux 博客](https://www.kali.org/blog/)
- [Kali Linux 培训与认证](https://www.offensive-security.com/)

______

## 更新检查清单

- **查看发布历史.** 下载镜像前，请阅读 [Kali 当前发布历史](https://www.kali.org/releases/)。
- **使用官方镜像.** 从 [Get Kali](https://www.kali.org/get-kali/) 下载，并核对官方公布的校验和。
- **更新滚动安装.** 遵循 Kali 的[当前更新文档](https://www.kali.org/docs/general-use/updating-kali/)，不要未经检查就照搬 2023.1 的仓库示例。
- **谨慎选择元软件包.** 标准实验室或 Purple 实验室无需安装 Kali 的所有软件包。
- **记录实验室范围.** 运行工具前，明确获准测试的系统、测试时间段、日志记录和清理步骤。
