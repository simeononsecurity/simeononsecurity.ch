---
title: "Flock Finder：绘制 Flock Safety ALPR 摄像头地图"
date: 2026-07-22
toc: true
draft: false
description: "Flock Finder 是一款开源工具，利用 WiGLE WiFi 数据和 OUI 指纹识别，绘制全球 40,000 多台 Flock Safety ALPR 摄像头的地图。了解其工作原理、局限性以及用于实时检测的硬件工具。"
genre: ["隐私技术", "反监控", "开源项目", "数字权利", "网络安全", "隐私工具", "硬件黑客", "安全研究"]
tags: ["Flock Finder", "Flock Safety", "ALPR", "车牌识别仪", "OUI 指纹识别", "WiGLE", "WiFi 监控", "反监控", "STS Collective", "FlockYou", "ESP32", "隐私工具", "NitekryDPaul", "DeFlockJoplin", "ALPR 检测", "开源安全", "监控地图", "大规模监控", "WiFi OUI", "隐私保护", "MAC 地址", "混杂模式", "802.11", "实时检测", "战地驾驶", "数字权利", "公民自由", "监控意识", "GitHub", "Python"]
cover: "/img/cover/flock-finder-open-source-alpr-camera-map.webp"
coverAlt: "交互式地图显示彩色标记，指示 Flock Safety ALPR 摄像头的位置，抽象的 WiFi 信号从标记处向外辐射，背景为深色。"
coverCaption: "Flock Finder 利用 WiGLE WiFi 数据和 OUI 指纹识别，绘制了 40,000 多台疑似 Flock Safety ALPR 摄像头的地图。"
canonical: "https://simeononsecurity.com/articles/flock-finder-alpr-surveillance-mapping-tool/"
---

**一款利用众包 WiFi 数据绘制 Flock Safety ALPR 摄像头地图的开源监控感知工具。**

## 什么是 Flock Finder？

**[Flock Finder](https://simeononsecurity.github.io/flock-finder/)** 是一个开源项目，用于绘制美国及其他 108 个国家的 **Flock Safety ALPR（自动车牌识别）摄像头**地图。它将 **31 个已知的 Flock Safety WiFi OUI（组织唯一标识符）前缀**与 **WiGLE 众包 WiFi 数据库**相结合，在交互式地图上识别并标注疑似摄像头位置。

该项目托管于 **[github.com/simeononsecurity/flock-finder](https://github.com/simeononsecurity/flock-finder)**，通过 GitHub Actions 每日自动更新。截至 2026 年 7 月，已在全球 964 个地区绘制了**超过 40,000 台疑似摄像头**。

| 指标 | 数值 |
|--------|-------|
| **已绘制摄像头数** | 40,026+ |
| **已知 OUI 前缀数** | 31 |
| **覆盖国家数** | 109 |
| **覆盖地区数** | 964 |
| **数据保留期** | 730 天（2 年） |
| **自动更新频率** | 每日 |

*这是一款通用感知工具，而非权威清单。在根据数据得出结论之前，请阅读局限性部分。*

有关 Flock Safety ALPR 监控对隐私的重要性背景，请阅读**[Flock Safety 摄像头监控：普及程度、隐私问题与保护策略](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**。

______

## 工作原理：通过 WiGLE 进行 OUI 指纹识别

### 核心思路

Flock Safety 摄像头内置 **WiFi 收发器**，会定期从休眠状态唤醒，将采集到的车牌数据上传至云端。在这些短暂的活跃窗口期内，摄像头会广播包含其 **MAC 地址**的 WiFi 帧——每个 MAC 地址的前三个字节标识制造商，这就是 **OUI（组织唯一标识符）**。

安全研究员 **@NitekryDPaul** 通过 **2.4 GHz 混杂模式分析**，发现了 **30 个 OUI 前缀**，它们与 Flock Safety 摄像头硬件持续相关联。第 31 个前缀（`82:6B:F2`）由 **Michael / DeFlockJoplin** 在密苏里州乔普林进行现场测试期间贡献。

Flock Finder 获取这 31 个 OUI，查询 WiGLE 中与这些前缀匹配的任何已记录 WiFi 网络，并将结果绘制在地图上。

### 31 个已知的 Flock Safety OUI 前缀

| # | OUI 前缀 | 来源 | # | OUI 前缀 | 来源 |
|---|-----------|--------|---|-----------|--------|
| 1 | **70:C9:4E** | @NitekryDPaul | 17 | **D0:39:57** | @NitekryDPaul |
| 2 | **3C:91:80** | @NitekryDPaul | 18 | **E8:D0:FC** | @NitekryDPaul |
| 3 | **D8:F3:BC** | @NitekryDPaul | 19 | **E0:4F:43** | @NitekryDPaul |
| 4 | **80:30:49** | @NitekryDPaul | 20 | **B8:1E:A4** | @NitekryDPaul |
| 5 | **B8:35:32** | @NitekryDPaul | 21 | **70:08:94** | @NitekryDPaul |
| 6 | **14:5A:FC** | @NitekryDPaul | 22 | **58:8E:81** | @NitekryDPaul |
| 7 | **74:4C:A1** | @NitekryDPaul | 23 | **EC:1B:BD** | @NitekryDPaul |
| 8 | **08:3A:88** | @NitekryDPaul | 24 | **3C:71:BF** | @NitekryDPaul |
| 9 | **9C:2F:9D** | @NitekryDPaul | 25 | **58:00:E3** | @NitekryDPaul |
| 10 | **C0:35:32** | @NitekryDPaul | 26 | **90:35:EA** | @NitekryDPaul |
| 11 | **94:08:53** | @NitekryDPaul | 27 | **5C:93:A2** | @NitekryDPaul |
| 12 | **E4:AA:EA** | @NitekryDPaul | 28 | **64:6E:69** | @NitekryDPaul |
| 13 | **F4:6A:DD** | @NitekryDPaul | 29 | **48:27:EA** | @NitekryDPaul |
| 14 | **F8:A2:D6** | @NitekryDPaul | 30 | **A4:CF:12** | @NitekryDPaul |
| 15 | **24:B2:B9** | @NitekryDPaul | 31 | **82:6B:F2** | DeFlockJoplin |
| 16 | **00:F4:8D** | @NitekryDPaul | | | |

### addr1 检测技术

@NitekryDPaul 的关键发现不止于简单匹配发射端 MAC 地址。Flock 摄像头大部分工作周期处于**休眠状态**。当附近的接入点向摄像头发送帧时，摄像头的 MAC 地址会作为 **addr1（接收方地址）**出现在 802.11 帧中——即使摄像头本身并未主动发射。

结合**通配符探测请求检测**（802.11 管理帧类型=0，子类型=4，空 SSID），这产生了非常精准的检测特征。在密苏里州乔普林进行的现场测试中，**12 台摄像头中检测到 11 台，仅有 2 个误报**。

> ⚠️ **重要说明**：基于 WiGLE 的 Flock Finder 地图**不**实现 addr1 技术。WiGLE 是一个历史性的被动收集数据集——它只记录发射方，不记录接收方。要使用 @NitekryDPaul 方法进行实时检测，需要在现场运行专用硬件。

______

## 使用实时地图

交互式地图可在 **[simeononsecurity.github.io/flock-finder/](https://simeononsecurity.github.io/flock-finder/)** 访问。它显示：

- **按 OUI 前缀颜色编码的聚类摄像头标记**
- **按城市、州或 BSSID 搜索**
- **OUI 数据表**，包含每个前缀的摄像头数量
- **统计面板**，显示摄像头总数、地区数和最后更新时间戳
- **关于 ALPR 的页面**，包含有记录的隐私危害、法律背景和社区资源

地图数据导出也可直接获取：

- `data/flock_cameras.geojson` — 可在 QGIS、Leaflet 或其他工具中使用的 GeoJSON
- `data/flock_cameras.csv` — 电子表格友好格式
- `data/scan_stats.json` — 扫描统计和计数

### 主要局限性

**请审慎看待地图数据。** WiGLE 是一个众包的、不定期更新的数据集，而非实时数据流。

- **Flock 摄像头不会持续广播。** 它们短暂唤醒以上传数据，因此 WiGLE 记录完全取决于战地驾驶员是否恰好在正确时机出现在附近。
- **数据可能已有数月或数年之久。** 已被移位或拆除的摄像头可能仍会显示。
- **OUI 匹配是一种启发式方法。** OUI 可能被共享、重新分配或伪造。每个结果都是*疑似* Flock 设备，而非确认设备。
- **覆盖范围不均匀。** 密集都市区的 WiGLE 数据更多；农村地区则少得多。

*使用地图了解您所在地区监控密度的总体情况。有关基于实地的实时检测，请参阅下面的硬件选项。*

______

## 自行运行 Flock Finder

### 前提条件

- Python 3.8+
- 免费的 [WiGLE](https://wigle.net/account) 账户及 API 凭证

### 设置

```bash
# Clone the repository
git clone https://github.com/simeononsecurity/flock-finder.git
cd flock-finder

# Install dependencies
pip install -r requirements.txt

# Set up your WiGLE API credentials
cp .env.example .env
# Edit .env with your WiGLE API Name and Token
```

### 运行扫描器

```bash
# Full scan — all 31 OUI prefixes, worldwide
python3 scripts/wigle_query.py

# Single OUI test
python3 scripts/wigle_query.py --oui 70:C9:4E

# US only
python3 scripts/wigle_query.py --country US

# Specific bounding box (lat1,lon1,lat2,lon2)
python3 scripts/wigle_query.py --bbox 37,-97,39,-94

# Dry run — verify auth, no API queries
python3 scripts/wigle_query.py --dry-run
```

### 本地查看地图

```bash
python3 -m http.server 8080 --directory docs/
# Open http://localhost:8080 in your browser
```

### 通过 GitHub Actions 自动每日更新

Fork 该仓库并将您的 WiGLE 凭证添加为**仓库密钥**（`WIGLE_API_NAME` 和 `WIGLE_API_TOKEN`）。包含的工作流每天 UTC 时间早上 6 点运行，每当发现新摄像头时自动提交更新的数据文件。

______

## 实时检测：STS Collective 的 FlockYou 硬件

WiGLE 地图告诉您摄像头*曾被观测到*的位置。要在驾驶时进行实时检测——使用 @NitekryDPaul 的实际 OUI 匹配方法对实时 WiFi 流量进行检测——您需要专用硬件。

**[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY)** 生产基于 ESP32 的便携式检测器，能够扫描 Flock OUI 特征，并在检测到匹配特征时立即提醒您。

### FlockYou 设备阵容

| 设备 | 描述 |
|--------|-------------|
| **[FlockYou — M5 Atom Lite](https://stscollective.com/products/flockyou-m5-atom-lite-flock-camera-detector)** | 紧凑型口袋尺寸 Flock 检测器。预先烧录，即插即用。检测到时 LED 提示。 |
| **FlockYou Pro — LED + 音频** | 在 LED 指示灯基础上增加音频提示。驾驶时不会错过任何摄像头。 |
| **FlockYou Atom VoiceS3R** | 具有语音提示的检测器，实现免持、眼不离路的操作。 |

所有设备：
- **预先烧录**，开箱即用
- 扫描实时 WiFi 流量，覆盖所有 31 个已知 Flock OUI
- 紧凑便携——可放入杯架或口袋
- 通过 USB-C 供电（车载适配器、移动电源或笔记本电脑）

> 💰 **独家折扣**：使用代码 **FLOCKFINDER** 可享 STS Collective 所有 FlockYou 设备 **8 折优惠**——或使用代码 **SIMEONONSECURITY** 可享整个订单最高 8 折优惠。[在 stscollective.com/discount/SIMEONONSECURITY 购物](https://stscollective.com/discount/SIMEONONSECURITY)。

有关这些设备和 DIY 替代方案的完整技术分析，请阅读**[Flock-You 检测项目：完整的反监控硬件与设置指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**。

______

## 项目结构

```
flock-finder/
├── scripts/
│   └── wigle_query.py        # WiGLE API query and data pipeline
├── data/
│   ├── flock_ouis.csv         # 31 known Flock Safety OUI prefixes
│   ├── flock_cameras.geojson  # Camera locations (GeoJSON)
│   ├── flock_cameras.csv      # Camera locations (CSV)
│   └── scan_stats.json        # Scan statistics
├── docs/
│   └── index.html             # Interactive Leaflet map
└── .github/workflows/
    └── update-data.yml        # Daily auto-update workflow
```

______

## 常见问题

### 这合法吗？

是的。**Flock Finder 仅使用来自 WiGLE 数据库的公开可用数据**，该数据库汇集了自愿贡献的 WiFi 调查数据。不涉及任何黑客行为、未经授权的访问或专有系统。在美国，对 OUI 特征进行被动 WiFi 监控是合法的。

### 地图上每台摄像头都一定是 Flock 摄像头吗？

不是。OUI 匹配是一种**启发式方法**。OUI 前缀可能由多个制造商共享、被重新分配或伪造。数据库中的每条记录都是*疑似* Flock 设备——而非已确认的设备。有关如何请求更正的详细信息，请阅读[数据政策](https://github.com/simeononsecurity/flock-finder/blob/main/docs/data-policy.md)。

### 为什么某些 OUI 前缀没有显示摄像头？

WiGLE 的覆盖范围不均匀。如果没有战地驾驶员在该特定 OUI 活跃时扫描某个区域，就不会有任何记录。*数据缺失不代表摄像头不存在。*

### 数据有多新？

GitHub Actions 工作流每天运行并获取最新的 WiGLE 结果。但是，WiGLE 本身对于任何给定位置的记录可能从几天到几年不等。请检查 `scan_stats.json` 文件以获取最近一次扫描的时间戳。

### 我可以贡献自己的战地驾驶数据吗？

可以。将您的战地驾驶数据上传至 [WiGLE](https://wigle.net)——它将自动输入 Flock Finder 的下一次每日扫描。您也可以通过[贡献指南](https://github.com/simeononsecurity/flock-finder/blob/main/CONTRIBUTING.md)贡献 OUI 前缀或代码改进。

______

## 社区与相关项目

Flock Finder 并非孤立存在。一个不断壮大的工具和组织生态系统正在努力记录和对抗 ALPR 监控：

- **[DeFlock.org](https://deflockjoplin.org/)** — 社区驱动的 ALPR 追踪、记录与倡导
- **[Have I Been Flocked?](https://haveibeenflocked.com/)** — 检查您的车牌是否曾被 Flock 系统搜索
- **[FlockHopper](https://flockhopper.com/)** — 规避已知 ALPR 摄像头的路线规划
- **[Atlas of Surveillance (EFF)](https://atlasofsurveillance.org/)** — EFF 关于执法部门使用监控技术的数据库
- **[NoALPRs.com](https://noalprs.com/)** — 为抵制 ALPR 部署的社区提供资源
- **[DeFlockJoplin](https://deflockjoplin.org/)** — 开源固件与现场研究；贡献了第 31 个 OUI 前缀

______

## 致谢

- **OUI 研究**：@NitekryDPaul — 全部 30 个原始 OUI 前缀以及 addr1/混杂模式检测策略
- **现场测试**：Michael / DeFlockJoplin — 第 31 个 OUI 前缀（`82:6B:F2`）及通配符探测优化
- **数据来源**：[WiGLE](https://wigle.net) — 众包 WiFi/蜂窝网络数据库
- **灵感来源**：[DeFlock](https://deflockjoplin.org/) 和 track-openroaming-passpoint
- **硬件合作伙伴**：[STS Collective](https://stscollective.com/discount/SIMEONONSECURITY) — FlockYou ESP32 检测器

______

## 结语

**Flock Finder** 让任何人都能快速、直观地了解 Flock Safety ALPR 摄像头的部署规模——在 109 个国家有超过 40,000 个估计位置，每天自动从众包 WiFi 数据更新。

它是一款**透明度工具**，而非实时追踪器。其数据具有历史性、不完整性和概率性。但它以摘要和报告所无法做到的方式，将 ALPR 监控的规模直观呈现出来。

要在穿越受监控区域时获得真正的实时保护，请将地图与专用硬件结合使用。**[STS Collective 的 FlockYou 设备](https://stscollective.com/discount/SIMEONONSECURITY)**直接在 ESP32 上实现了 @NitekryDPaul 的检测方法，并在检测到实时摄像头特征时立即提醒您——可在 **[stscollective.com](https://stscollective.com/discount/SIMEONONSECURITY)** 使用代码 **FLOCKFINDER** 或 **SIMEONONSECURITY** 享受最高 8 折优惠。

### 相关文章

| 文章 | 内容 |
|---------|---------------|
| **[Flock Safety 摄像头监控：隐私与保护](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | 完整图景：普及统计、公民自由问题、ACLU 工具包、DeFlock 统计、FOIA 指南和保护策略 |
| **[Flock-You 检测项目：反监控硬件指南](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | 基于 ESP32 的 Flock 检测器完整技术指南——OUI-SPY、M5 Atom Lite、DIY 构建、分步固件设置 |
| **[如何烧录 Rayhunter 设备：完整指南](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | 检测 IMSI 拦截器（伪基站）与 ALPR 摄像头，实现全面的反监控意识 |
| **[Orbic RCL400 的 DagShell 自定义固件](/articles/dagshell-orbic-rcl400-custom-firmware-guide-2026/)** | 将移动热点变为安全研究平台——与 Flock 检测硬件完美搭配 |
| **[2026 年 Rayhunter 设备对比](/articles/rayhunter-device-comparison-2026-complete-review/)** | 在 ALPR 和蜂窝监控威胁类别中比较检测硬件选项 |

______

## 参考资料

1. [Flock Finder GitHub 仓库](https://github.com/simeononsecurity/flock-finder)
2. [Flock Finder 交互式地图](https://simeononsecurity.github.io/flock-finder/)
3. [STS Collective — FlockYou 设备](https://stscollective.com/discount/SIMEONONSECURITY)
4. [WiGLE — 无线网络地图](https://wigle.net)
5. [DeFlock — 社区 ALPR 意识](https://deflockjoplin.org/)
6. [DeFlockJoplin — 开源检测固件](https://deflockjoplin.org/)
7. [电子前哨基金会 — ALPR](https://www.eff.org/issues/automated-license-plate-readers)
8. [ACLU — 你正在被追踪](https://www.aclu.org/issues/privacy-technology/location-tracking/you-are-being-tracked)
