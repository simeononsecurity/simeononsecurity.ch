---
title: "理解 WMI 筛选"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "了解如何使用 WMI 筛选将组策略对象 (GPO) 应用于目标计算机，并查看实用示例和最佳实践。"
genre: ["Windows 管理", "组策略", "系统管理", "网络管理", "IT 基础设施", "策略管理", "IT 治理", "IT 自动化", "Active Directory", "安全合规"]
tags: ["WMI 筛选", "GPO", "组策略对象", "WMI 筛选器", "策略目标选择", "WMI 查询", "Windows Management Instrumentation", "GPO 控制", "组策略管理控制台", "WMI 查询语言", "策略应用", "WQL", "精细调整策略", "策略管理", "系统资源", "策略目标选择示例", "系统管理", "网络管理", "IT 基础设施管理", "IT 自动化", "Active Directory 管理", "安全合规", "策略控制技术", "策略管理最佳实践", "策略筛选", "GPO 控制策略", "GPO 安全", "WMI 筛选的优点", "实施 WMI 筛选", "WMI 筛选最佳实践"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "放大镜聚焦于筛选图标的插图，表示通过 WMI 筛选选择 GPO 的应用目标。"
coverCaption: "使用 WMI 筛选，高效地将 GPO 策略应用于目标系统。"
---

## 简介

在组策略对象 (GPO) 中，[**WMI 筛选**](https://simeononsecurity.com/github/wmi-filters/)根据 WMI (Windows Management Instrumentation) 查询结果，控制策略应用于哪些计算机或用户。管理员借此细化目标选择，只向预期对象应用策略。本文介绍 WMI 筛选的概念、它在 GPO 中的工作方式、如何创建 [WMI 筛选器](https://simeononsecurity.com/github/wmi-filters/)，以及实际示例。

## [什么是 WMI 筛选？](https://simeononsecurity.com/github/wmi-filters/)

[**WMI 筛选**](https://simeononsecurity.com/github/wmi-filters/)是根据 WMI 查询结果对 GPO 应用筛选条件。WMI 是 Windows 操作系统内置的管理基础设施，可帮助管理员检索管理数据，并以编程方式与系统资源交互。使用 WMI 筛选，管理员可以根据查询所定义的条件动态选择 GPO 的目标。

WMI 筛选器使用 WMI 查询语言 (WQL) 编写。WQL 是 SQL (Structured Query Language) 的子集，通常依据 WMI 命名空间中的属性和值构建。管理员可以组合条件、逻辑运算符和命名空间，创建用于选择特定计算机或用户的复杂 WMI 查询。

## WMI 筛选如何在 GPO 中工作？

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="流程图展示附加到组策略对象的 WMI 筛选器将 WQL 查询评估为 True 或 False，并据此决定是否将 GPO 应用于目标计算机" >}}

在组策略中，**WMI 筛选**根据 **WMI 查询**的评估结果有选择地应用 GPO。将 **WMI 筛选器**关联到 GPO 后，筛选结果为 **True** 或 **False**，决定 GPO 是否应用。

WMI 筛选器使用 **WMI 查询语言 (WQL)**，它是 SQL 的子集。WQL 可根据 **WMI 命名空间**中的各种**属性**和**值**创建复杂查询，从而精确选择特定计算机或用户。

例如，组织可能只想将某个 GPO 应用于运行 Windows 10 的计算机。为此，可以创建 WMI 筛选器来检查 **Win32_OperatingSystem** 类的 **OperatingSystem** 属性。WMI 查询示例如下：

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

此查询检查操作系统版本是否以“10.”开头，这表示 Windows 10。如果查询结果为 **True**，GPO 就会应用于目标计算机，否则不会应用。

WMI 筛选还支持 **AND**、**OR** 和 **NOT** 等条件与逻辑运算符。管理员可以组合多个属性和值，更精细地控制 GPO 的应用。

不同的 **WMI 命名空间**可用于访问特定的 WMI 类和属性集合。因此，管理员能够根据硬件配置、已安装软件、网络设置等条件选择 GPO 目标。

有关创建 WMI 筛选器和查询的更多信息，请参阅 Microsoft 关于[组策略 WMI 筛选](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo)的文档。

借助 WMI 筛选，管理员可以根据动态条件，将 GPO 调整为应用于特定计算机或用户，从而更好地管理 IT 环境。

## 为 GPO 创建 WMI 筛选器

创建 GPO 的 WMI 筛选器，请按以下步骤操作：

1. 在已加入域的 Windows 计算机上打开**组策略管理控制台** (GPMC)。

2. 展开域，然后转到 **WMI Filters** 节点。

3. 右键单击 **WMI Filters**，再选择 **New**。

4. 为筛选器输入有意义的名称，并在 **Query** 字段中输入 WMI 查询。查询须使用 WQL 语法。

5. 单击 **OK** 保存 WMI 筛选器。

创建筛选器后，可以将其关联到一个或多个 GPO。关联方法如下：

1. 右键单击目标 GPO，然后选择 **Properties**。

2. 在 GPO 属性窗口中，打开 **WMI Filtering** 选项卡。

3. 从列表中选择所需的 WMI 筛选器。

4. 单击 **OK** 保存更改。

将 WMI 筛选器关联到 GPO 后，即可根据 WMI 查询结果精确控制策略的应用范围。

## 一个 GPO 可以配置多少个 WMI 筛选器？

管理员可以为一个 GPO 配置**多个 WMI 筛选器**，实现精细的策略目标选择。单个 GPO 关联的筛选器没有固定数量上限，因此可以组合多个条件。

不过，筛选器数量会影响 GPO 处理时间。筛选器越多，评估和应用 GPO 可能需要越久。为确保策略高效应用，应将筛选器数量控制在合理范围内。

例如，组织可能只想将某个 GPO 应用于运行 Windows 10 且安装了特定软件的计算机。可以分别创建两个 WMI 筛选器，一个用于**操作系统**，另一个用于**软件安装情况**。组合这两个条件即可选择目标计算机。

应在满足目标选择要求与控制处理时间之间取得平衡。决定筛选器数量前，管理员应评估环境复杂度、计算机或用户数量，以及对性能的潜在影响。

多个 WMI 筛选器有助于优化 GPO 目标选择，同时保持 IT 环境处理和管理的效率。

## GPO 中 WMI 筛选的实际示例

WMI 筛选可以帮助有针对性地应用 GPO。以下是一些示例：

1. **选择特定操作系统**：若要只向 **Windows 10** 计算机应用 GPO，可创建检查操作系统版本的筛选器，例如 `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`。这样即可选择 Windows 10 计算机。

2. **为台式机和笔记本电脑应用不同策略**：如果两类设备需要不同策略，可使用两个 WMI 筛选器。一个筛选器可根据硬件属性识别台式机，例如 `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`，另一个则识别笔记本电脑。这样可为每类设备应用适合的策略。

3. **根据磁盘空间选择策略**：为避免向磁盘空间不足的计算机应用资源密集型策略，可以创建检查可用磁盘空间的筛选器。例如，查询 `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` 会排除可用空间少于 10 GB 的计算机。

这些示例展现了 GPO 中 **WMI 筛选**的灵活性，管理员可以根据特定条件选择策略的应用对象。

## 结论

WMI 筛选是组策略对象的一项实用功能。管理员可根据 WMI 查询结果，有选择地向特定计算机或用户应用策略。WMI 筛选器有助于精确定位策略目标，让策略管理更加高效且可控。本文介绍了 WMI 筛选的概念、它在 GPO 中的工作方式、筛选器创建方法及实用示例。

将 WMI 筛选用于 GPO 管理，可以提高策略应用的准确性，确保策略只应用于预期目标。

## 参考资料

- [Microsoft Docs：为 GPO 创建 WMI 筛选器](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs：about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs：组策略](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs：组策略管理控制台](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
