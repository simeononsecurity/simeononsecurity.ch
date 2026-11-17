---
title: "Rayhunter 设备刷写完整指南"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "刷写并配置 Rayhunter 以检测 IMSI 捕获器。了解兼容设备、安装固件、验证运行状态并排查常见故障。"
tags: ["Rayhunter", "IMSI 捕获器", "蜂窝基站模拟器", "移动安全", "监控检测", "隐私保护", "Orbic RC400L", "TP-Link M7350", "移动热点", "设备刷写", "网络安全", "无线安全", "反监控措施", "EFF", "隐私工具", "购买 Rayhunter", "安装指南", "配置", "兼容设备", "网络安全"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Rayhunter 设备检测无线信号和 IMSI 捕获器，周围有安全盾牌"
coverCaption: "Rayhunter IMSI 捕获器检测系统，保护移动通信免受监控"
---

**Rayhunter 刷写与配置完整指南，介绍这款 IMSI 捕获器检测系统。**

## 内容摘要

**Rayhunter** 是一款开源 IMSI 捕获器检测系统，运行在经过改装的移动热点上。当监控设备试图拦截蜂窝通信时，它会向用户发出警报。本指南介绍如何在 Orbic RC400L 和 TP-Link M7350 设备上完整安装、配置选项、威胁行为者分析，以及该工具在 5G 网络中的有效性。你需要兼容的 Qualcomm 设备。它通过多种启发式方法检测 2G、3G 和 4G 监控。即使 5G 普及，降级攻击仍在发生，因此 Rayhunter 仍有用。它为记者、活动人士和重视隐私的人士提供重要防护，帮助应对政府、犯罪组织和企业监控。

**Rayhunter** 是一款开源工具，用于检测可能拦截移动通信的 IMSI 捕获器（蜂窝基站模拟器）。如果你想**购买 Rayhunter**，或了解如何正确刷写和配置设备，本指南将介绍 **Rayhunter** 系统的安装、配置和使用。

**赞助披露：** 本文由 [STS Collective](https://stscollective.com) 赞助，该公司是 Rayhunter 兼容设备的主要供应商。尽管本文获得赞助，指南中的技术信息、分析和建议仍保持客观，并仅依据 Rayhunter 官方文档、社区反馈和技术评估。

> 💰 **读者专属优惠：** 购买 Rayhunter 设备和 STS Collective 的所有产品，最高可享 20% 折扣。结账时使用代码 **SIMEONONSECURITY**，或[直接购买已应用折扣的商品](https://stscollective.com/discount/SIMEONONSECURITY)。

## Rayhunter 简介

**Rayhunter** 是由 **Electronic Frontier Foundation (EFF)** 开发的高级 IMSI 捕获器检测系统。EFF 是一家致力于维护数字世界公民自由的重要非营利组织。自 1990 年以来，EFF 通过影响力诉讼、政策分析、基层行动和技术开发，持续捍卫数字隐私、言论自由与创新。

此工具在兼容的移动热点上运行，持续监测蜂窝网络中的可疑活动，这些活动可能说明用于监控的蜂窝基站模拟器或“Stingray”正在附近运行。**Rayhunter** 体现了 EFF 的承诺，为需要防范监控的个人和组织提供实用的隐私保护工具。

检测到可能恶意的蜂窝网络行为时，**Rayhunter** 会实时告警。记者、活动人士、安全专业人员和重视隐私的人士都可使用它保护隐私。你可以通过 STS Collective（这类专用设备的主要供应商）购买兼容设备：[购买 **Rayhunter** 设备](https://stscollective.com/collections/rayhunter)。

### 支持 Rayhunter 项目

**Rayhunter** 是受益于社区支持的开源项目。你可以通过以下方式帮助项目持续发展：

- **通过 STS Collective 购买：** STS Collective 会将每台 **Rayhunter** 设备部分利润捐给 EFF，支持 **Rayhunter** 的持续开发和隐私研究。
- **直接捐赠：** 通过 [EFF 捐赠页面](https://supporters.eff.org/donate/donate)直接支持 EFF 的隐私倡导工作和 **Rayhunter** 开发。
- **参与社区：** 在官方 GitHub 仓库参与讨论、文档编写和测试。

你的支持有助于保持 **Rayhunter** 免费、开源，并持续改进，以应对不断变化的监控威胁。

## 支持、反馈和社区

**Rayhunter** 得到安全研究人员、隐私倡导者和关心此议题的公众组成的活跃社区支持。你可以通过不同渠道寻求帮助并为项目作出贡献：

- **官方文档：** [Rayhunter 文档](https://efforg.github.io/rayhunter/introduction.html)，涵盖安装、配置和使用。
- **GitHub 仓库：** [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **社区讨论：** 在 GitHub 发起讨论，交流设备兼容性和故障排查。
- **安全研究：** 与研究人员合作，改进 **Rayhunter** 的检测能力。

如需购买兼容设备，可通过 STS Collective 查看[在售 **Rayhunter** 设备](https://stscollective.com/collections/rayhunter)。

## 常见问题

### 使用 Rayhunter 需要有效的 SIM 卡吗？

**Rayhunter** 要求设备中插入 SIM 卡，但 SIM 卡不需要有效的服务套餐。设备需要 SIM 卡才能连接蜂窝网络并监测可疑活动。如果你还想在运行 **Rayhunter** 时把设备用作热点，则需要有效套餐。

### 如何测试 Rayhunter 设备是否正常工作？

你可以在 **Rayhunter** 配置中启用 Test Heuristic（测试启发式）。设备每次检测到蜂窝基站时都会触发警报，便于你确认系统工作正常。测试模式会产生大量告警，测试后请将其关闭。

### 应该购买锁网还是解锁设备？

为确保兼容 **Rayhunter**，通常优先选择解锁设备，尤其是你计划使用非 Verizon SIM 卡时。许多 Verizon 品牌的 Orbic 设备实际上已解锁，但购买前仍应核实兼容性。你可以通过 STS Collective 购买已验证兼容的 [**Rayhunter** 设备](https://stscollective.com/collections/rayhunter)。

{{< stscollective-ad "rayhunter" >}}

## 安装指南

### 从最新版本安装

**Rayhunter** 已在 macOS 和 Ubuntu 24.04 上完成安装测试。如果预构建版本无法使用，你可能需要从源代码安装。

#### 前提条件

安装 **Rayhunter** 前，请确认设备兼容。对于 TP-Link 设备，请插入 FAT 格式的 SD 卡以存储录制文件。

#### 下载和设置

1. **下载最新版本：** 从官方发布页面下载对应的 `rayhunter-vX.X.X-PLATFORM.zip`：
   - Linux x64：`linux-x64`
   - Linux ARM64：`linux-aarch64`
   - Linux ARM v7/v8：`linux-armv7`
   - macOS Intel：`macos-intel`
   - macOS ARM (M1/M2)：`macos-arm`
   - Windows：`windows-x86_64`

2. **解压并进入目录：**
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **连接设备：** 打开设备，通过 WiFi 或 USB 网络共享连接。你应能访问以下地址：
   - Orbic 设备：`http://192.168.1.1`
   - TP-Link 设备：`http://192.168.0.1`

#### 按设备安装

**Orbic RC400L 设备**（[购买 **Rayhunter**](https://stscollective.com)）：

**Rayhunter** 支持两种 Orbic RC400L 安装方式。大多数用户建议使用 WiFi 方法，USB 方法则提供更多调试功能。

**WiFi 安装方法（推荐）：**
```bash
# macOS 用户需要先运行此命令：
xattr -d com.apple.quarantine installer

# Verizon RC400L（管理员密码与 WiFi 密码相同）：
./installer orbic --admin-password 'YourWiFiPassword'

# Kajeet/Smartspot RC400L：
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Moxee 设备（密码格式：12$ + WiFi 密码末尾 3 位）：
./installer orbic --admin-password='12$XXX'
```

**USB 安装方法（高级用户）：**
```bash
# 警告：大多数用途不建议使用 USB 安装程序
./installer orbic-usb
```

此方法会强制设备进入调试模式以启用 ADB，然后安装 rootshell 和 **Rayhunter**，最后重启设备。只有在其他用途需要 ADB 时才使用此方法。

**TP-Link M7350 设备**（[购买 Rayhunter](https://stscollective.com)）：
```bash
./installer tplink
```

安装程序会完成 **Rayhunter** 刷写并重启设备。设备屏幕上出现绿色横线，表示 **Rayhunter** 已成功运行。

### 从源代码安装

开发者或需要从源代码构建 **Rayhunter** 的用户会用到项目中的以下组件：

- **前端：** JavaScript SvelteKit 应用 (`./daemon/web/`)
- **后端：** Rust 二进制程序 `rayhunter-daemon` (`./daemon/`)
- **安装程序：** 集成所有组件的 Rust 二进制程序 (`./installer`)

#### 构建依赖

请安装以下依赖：
- Rust 编程语言
- Node.js/npm
- C 编译器工具（Linux 上为 `build-essential`，macOS 上为 `xcode-select --install`）

#### 构建过程

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # 将 'orbic' 替换成你的设备类型
```

启用热重载进行前端开发：
```bash
cd daemon/web
npm run dev
# 或指定自定义目标：
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### 更新 Rayhunter

更新 **Rayhunter** 的步骤与安装相同。使用最新版本重复安装步骤，即可将设备更新到最新 **Rayhunter** 版本。

## 配置

你可以通过 Web 界面配置 **Rayhunter**，也可以直接在设备上编辑 `/data/rayhunter/config.toml`。

### Web 界面配置

连接到设备网络后，访问以下地址打开 **Rayhunter** Web 界面：
- Orbic：`http://192.168.1.1:8080`
- TP-Link：`http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Rayhunter Web 界面仪表板" caption="Rayhunter Web 界面提供全面的监控和配置选项" >}}

#### 主要配置选项

**设备界面级别：** 控制 **Rayhunter** 在设备屏幕上的显示内容：
- **隐身模式：** 不显示内容。
- **低调模式：** 显示彩色指示线（绿色=安全，红色=告警，白色=暂停）。
- **演示模式：** 显示 orca 图形和状态行。
- **EFF 标志：** 显示 EFF 标志和状态行。
- **高可见度：** 全屏显示颜色。

**设备输入模式：** 配置电源按钮行为：
- **禁用按钮控制：** 禁止通过电源按钮控制 **Rayhunter**。
- **双击以重启录制：** 重置告警并重新开始监控。

**通知设置：** 配置远程告警的 ntfy URL，并启用或禁用警告和低电量通知。

**分析器启发式：** 根据使用环境和威胁模型启用或禁用特定 **Rayhunter** 检测算法。

## 卸载 Rayhunter

### Orbic 设备

要从 Orbic 设备移除 **Rayhunter**：

```bash
./installer util orbic-shell --admin-password mypassword
```

进入 shell 后：

> **警告：** 以下命令会永久删除 Rayhunter 文件及其启动钩子。确认当前进入的是目标设备 shell，先复制需要保留的录制文件或配置，并准备好安装程序和兼容固件。操作后请确认文件已删除，设备重启时 Rayhunter 服务未启动。如需回滚，请从官方仓库重新安装匹配版本。

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### TP-Link 设备

卸载 TP-Link 设备上的 Rayhunter：

> **警告：** 以下命令会从 TP-Link 设备删除 Rayhunter 文件和启动钩子。请先导出录制文件和配置。仅在设备 shell 中运行这些命令，然后确认相应路径已不存在且设备能正常启动。如需回滚，请从官方仓库重新安装匹配版本。

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

请在 TP-Link 管理界面的 Settings > NAT Settings > Port Triggers 中删除所有遗留的端口触发规则。

## 使用 Rayhunter

安装后，**Rayhunter** 会自动运行并持续监测蜂窝网络中的可疑活动。设备显示屏在正常运行时显示绿色线条；检测到潜在 IMSI 捕获器时则会显示黄色圆点、橙色短划线或红色实线。

### Rayhunter 检测启发式

**Rayhunter** 使用多种高级检测算法识别潜在 IMSI 捕获器活动：

#### IMSI 请求检测

此启发式检测一种可疑情况：蜂窝基站请求设备身份（IMSI，即国际移动用户识别码），却未遵循适当的身份验证流程。**Rayhunter** 会监测这些请求的时机和上下文，并标记可能表明监控设备存在的异常模式。

合法蜂窝网络在请求敏感标识符前会遵循标准化身份验证程序。IMSI 捕获器通常绕过这些程序，以便快速收集设备身份，从而在身份验证序列中留下可检测的异常。这种检测方式尤其适用于基本的“被动式”IMSI 捕获器，它们只收集设备信息。

#### 连接释放/降级至 2G 检测

**Rayhunter** 会持续监测可疑操作，识别是否有人试图强制移动设备从安全的 4G/5G 网络断开，再重新连接到安全性较低的 2G 网络。IMSI 捕获器常用此降级攻击，因为 2G 加密较弱，更容易被拦截。

系统会分析连接释放模式，寻找异常频率、时机或上下文指标，以区分恶意意图和正常网络优化。合法网络有时也会因覆盖范围或容量原因建议降级，但 **Rayhunter** 能区分常规网络行为和潜在监控活动。

#### LTE SIB6/7 降级检测

系统信息块（SIB）是蜂窝网络向移动设备发送配置数据的广播消息。**Rayhunter** 会特别监测 SIB6 和 SIB7 消息，其中包含邻近蜂窝和频率重定向信息。

恶意行为者可能广播伪造的 SIB6/7 消息，诱使设备放弃安全的 4G 连接并接入攻击者控制的 2G 网络。**Rayhunter** 会分析这些广播是否存在不一致、异常重定向模式或其他迹象，以识别企图降级设备连接并拦截通信的恶意基站。

#### 空加密检测

此关键检测方法用于发现蜂窝网络建议在通信中完全不加密（空加密）的情况。合法商业蜂窝网络不应提出未加密连接，否则将违反安全标准和法规要求。

如果网络建议使用空加密，**Rayhunter** 就会将其标记为高度可疑。*合法网络绝不会建议使用空加密。* 这清楚地表明监控设备试图以明文拦截通信。对于优先收集数据而不在意伪装成合法网络的 IMSI 捕获器，此启发式尤其有效。

#### 不完整 SIB 检测

合法蜂窝基站会广播完整的系统信息块，其中包含必要的网络配置数据。**Rayhunter** 会监测提供不完整或缺失系统信息的基站，这往往说明监控设备部署仓促或配置不当。

IMSI 捕获器通常无法实现完整的蜂窝网络功能，只提供设备连接和数据拦截所需的最低限度功能。通过检测此类不完整实现，**Rayhunter** 能识别缺少合法蜂窝基础设施应有完整功能的潜在恶意基站。

{{< figure src="rayhunter-heuristics-overview.webp" alt="图示总结 Rayhunter 的五种检测启发式：未验证即请求 IMSI、2G 降级攻击、LTE SIB6/7 重定向、提出空加密和系统信息广播不完整" >}}

## 威胁行为者与潜在目标

了解谁会部署 IMSI 捕获器以及他们针对哪些对象，有助于评估个人威胁模型并确定适当的 **Rayhunter** 配置。不同威胁行为者的技术水平各异，其目标策略也决定了 **Rayhunter** 旨在检测的监控活动类型。

### 政府和执法机构

**威胁能力：** 高级到专业级
**主要目标：**
- 正在接受调查的犯罪嫌疑人
- 国家安全案件中的关注对象
- 示威期间的抗议者和活动人士
- 高安全区域的一般人群监控
- 外国公民和外交人员

**检测模式：** 政府运营的 IMSI 捕获器可能采用先进设备，从而避免触发基础检测启发式。但它们仍常使用 **2G 降级攻击**和**连接释放模式**，将设备强制转入安全性较低的网络以便拦截。针对执法监控技术，**Rayhunter** 的 LTE SIB6/7 降级检测和连接释放监测尤其有效。

**常见情境：**
- 在抗议、集会或公众活动期间进行事件驱动监控
- 在政府设施或敏感基础设施附近进行位置监控
- 针对特定受调查人员的监控
- 边境和机场监控行动

### 情报机构（国内和国外）

**威胁能力：** 专业级到军事级
**主要目标：**
- 外国情报人员及其资产
- 政府官员和外交人员
- 国防承包商和研究人员
- 战略行业的企业高管
- 报道国家安全议题的记者
- 从事敏感政治议题工作的活动人士

**检测模式：** 情报级设备力求隐蔽，但 **Rayhunter** 的空加密检测和不完整 SIB 监测仍能发现某些先进监控行动。情报机构在针对特定对象的行动中，常使用请求 **IMSI 信息**的设备，从而触发 **Rayhunter** 的 IMSI 请求检测算法。

**常见情境：**
- 对高价值情报目标进行长期监控
- 在企业总部附近开展工业间谍活动
- 监控外交机构和大使馆
- 反情报行动
- 外国情报机构针对本国人员开展行动

### 犯罪组织

**威胁能力：** 基础到中级
**主要目标：**
- 可能遭到绑架或勒索的富裕人士
- 通过商业情报手段针对竞争对手的企业
- 正在调查有组织犯罪的执法人员
- 刑事案件中的证人和线人
- 跟踪骚扰、骚扰或家庭暴力的受害者

**检测模式：** 犯罪组织通常使用成本较低的商用 IMSI 捕获器，这些设备会同时触发多种 **Rayhunter** 启发式。由于技术水平有限，它们往往存在**不完整 SIB 实现**、使用**空加密**以最大化数据收集，并采用激进的 **2G 降级攻击**。

**常见情境：**
- 跟踪可能成为绑架或抢劫目标的人
- 犯罪行动期间监控执法人员的通信
- 工业间谍和竞争情报收集
- 跟踪与骚扰
- 恐吓证人和跟踪位置

### 企业间谍和私人情报

**威胁能力：** 中级到高级
**主要目标：**
- 竞争企业的高层管理人员
- 研发团队
- 并购谈判人员
- 知识产权所有者
- 商业机密保管人员
- 企业举报人和内部威胁信息来源

**检测模式：** 企业监控行动常使用兼顾成本与能力的中档设备。在商业谈判或产品开发期间针对特定人士时，这些设备经常触发**连接释放检测**和 **IMSI 请求告警**。

**常见情境：**
- 在并购谈判期间实施监控
- 在贸易展会和会议上收集竞争情报
- 盗窃知识产权
- 员工监控和内部威胁检测
- 收集客户数据以取得竞争优势

### 私人调查员和监控公司

**威胁能力：** 基础到中级
**主要目标：**
- 因保险欺诈调查而被监控的个人
- 离婚诉讼中的配偶
- 被怀疑行为不当的员工
- 涉及法律纠纷的个人
- 名人和公众人物

**检测模式：** 私人监控行动通常使用定制能力有限的商用设备。受成本和技术限制影响，这些系统经常触发 **Rayhunter** 的基础检测启发式，尤其是**空加密检测**和**不完整 SIB 监测**。

**常见情境：**
- 离婚和监护权调查
- 保险欺诈监控
- 员工行为不当调查
- 跟踪名人和狗仔队行动
- 法律案件调查和证据收集

### 恶意个人和黑客行动主义者

**威胁能力：** 基础到中级
**主要目标：**
- 个人仇敌或恋爱对象
- 公众人物和名人
- 公共场所的随机受害者
- 特定活动或地点的参与者
- 被针对的社区或群体成员

**检测模式：** 个人行为者通常使用基础甚至临时搭建的 IMSI 捕获器，同时触发多种 **Rayhunter** 检测算法。这类部署通常使用**空加密**、广播**不完整 SIB**，并尝试粗糙的 **2G 降级攻击**。

**常见情境：**
- 跟踪和骚扰
- 身份盗窃和金融欺诈
- 政治行动和干扰抗议
- 一般网络犯罪活动
- 在公共活动期间伺机监控

### 威胁评估与 Rayhunter 配置

**高风险人士**（记者、活动人士、政府官员、企业高管）应启用所有 **Rayhunter** 启发式，并使用**高可见度**显示模式，以获得最大检测能力。

**中等风险人士**（一般重视隐私的用户）可使用**低调模式**，并启用核心检测启发式，兼顾日常防护与不引人注意。

**针对特定活动的防护**（抗议、敏感会议、旅行）应临时启用所有检测方法和通知系统，以全面掌握监控风险。

了解自己的威胁模型，有助于根据具体风险优化 **Rayhunter** 配置，并确保能检测最可能针对你或你所参与活动的威胁行为者。

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="图示展示政府机构、犯罪组织和企业间谍人员等 IMSI 捕获器威胁行为者针对移动设备" >}}

## 5G 时代的 Rayhunter 有效性

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="图示展示支持 5G 的手机被降级攻击强制切换到受监控的 4G 或 3G 网络，这也是 Rayhunter 在 5G 时代仍能检测的技术" >}}

随着蜂窝网络转向 5G，人们开始关注 **Rayhunter** 是否仍有效，因为它支持 2G、3G 和 4G/LTE 检测，却不支持原生 5G 监控技术。理解 **Rayhunter** 在 5G 环境中的当前局限和持续价值，有助于制定长期监控检测策略。

### Rayhunter 为何在 5G 网络中仍有效

#### 降级攻击仍在持续

**Rayhunter** 检测的核心攻击方式，即强制设备连接安全性较低的网络，在 5G 部署中仍然相关。**IMSI 捕获器继续依赖 2G 和 3G 降级攻击**，原因包括：

- **实现成本较低：** 为旧协议构建监控设备的投资远低于开发支持 5G 的设备。
- **设备兼容范围更广：** 以 2G/3G 为目标，可监控不支持 5G 的旧设备。
- **攻击方法成熟：** 2G/3G 网络监控技术已有充分文档和测试。
- **监管优势：** 相比先进的 5G 拦截方法，一些旧监控技术可能受到较少法律限制。

#### 网络向后兼容

5G 网络仍与 **4G/LTE 向后兼容**，大多数移动设备也同时支持多个网络世代。此兼容性为 **Rayhunter** 擅长检测的降级攻击提供了持续机会：

- **自动回退机制：** 5G 覆盖较弱时，设备会自然回退到 4G，监控设备可趁机拦截这种切换。
- **协议协商漏洞：** 不同网络世代之间的握手过程可能被先进的 IMSI 捕获器操纵。
- **利用覆盖盲区：** 监控设备可部署在 5G 覆盖不完整的区域，迫使设备连接到受监控的 4G/LTE 网络。

#### 5G 部署进度缓慢

**全面 5G 覆盖的缓慢部署**确保 **Rayhunter** 在未来多年仍有实际价值：

- **城乡差异：** 许多地区仍主要使用 4G/LTE 网络，**Rayhunter** 的检测功能仍适用。
- **室内覆盖限制：** 5G 信号穿透建筑物的能力通常较弱，导致设备回退到 **Rayhunter** 能监测的 4G 网络。
- **国际旅行因素：** 各国 5G 部署进度差异很大，旅行者仍需关注 4G/LTE 监控。

#### 威胁行为者技术更新滞后

**监控设备的采购与部署周期**往往落后于商业网络技术：

- **政府采购周期：** 5G 部署数年后，执法和情报机构仍可能继续使用现有的 4G 监控设备。
- **成本效益分析：** 许多监控行动使用价格较低的 4G/LTE 拦截技术即可达成目的，降低升级到 5G 设备的动机。
- **培训和专业知识要求：** 操作 5G 监控设备需要专门知识，监控组织可能需要一段时间才能掌握。

### Rayhunter 在真正的 5G 环境中的局限

#### 原生 5G 监控盲区

*这是 Rayhunter 的主要局限。* **Rayhunter 无法检测不依赖降级攻击的原生 5G IMSI 捕获行动：**

- **5G 独立组网 (SA)：** 设备若连接到不会回退到 4G 的纯 5G 网络，**Rayhunter** 就无法监测这些通信。
- **先进的 5G 监控设备：** 获得先进技术的复杂威胁行为者可能在不触发 **Rayhunter** 检测启发式的情况下拦截 5G 通信。
- **网络切片滥用：** 5G 网络切片功能可能被用于 **Rayhunter** 无法检测的监控活动。

#### 增强的 5G 安全功能

5G 网络引入了**改进的安全措施**，可能降低传统监控技术的有效性：

- **更强加密协议：** 5G 使用比前几代网络更强的加密标准，更难破解。
- **增强的身份验证流程：** 5G 改进设备身份验证，使 IMSI 收集更困难。
- **网络安全监测：** 5G 基础设施包含更先进的入侵检测功能，可能发现并阻止监控尝试。

#### 设备行为变化

随着 5G 日益普及，**移动设备行为可能会改变**，进而影响 **Rayhunter** 检测能力：

- **更不愿降级：** 未来设备软件更新可能增强对降级攻击的抵御能力。
- **优先连接 5G：** 设备可能越来越优先使用 5G，并对连接旧网络的请求更加警惕。
- **提高安全意识：** 移动操作系统可能采用更好的方法来检测可疑网络行为。

### Rayhunter 部署的策略考量

#### 当前部署建议

对于近期部署，**Rayhunter** 提供**全面的监控检测能力**：

- **城市部署：** 即使主要城市具有广泛 5G 覆盖，**Rayhunter** 仍能检测针对 4G/LTE 网络的监控行动。
- **关键活动保护：** 抗议、敏感会议或高风险活动中，无论是否有 5G 覆盖，**Rayhunter** 都能提供重要检测能力。
- **旅行安全：** **Rayhunter** 仍能有效检测国内外旅行期间的监控活动。

#### 面向未来的策略

计划长期监控检测的组织和个人应考虑：

- **混合检测方法：** 将 **Rayhunter** 与其他安全工具和监测方法结合，可覆盖更多威胁途径。
- **定期更新威胁评估：** 关注监控技术发展，以决定何时需要补充或替换 **Rayhunter** 的功能。
- **支持社区开发：** 支持 **Rayhunter** 开源开发，有助于未来版本增加 5G 检测能力。

#### 监测技术演进

**Rayhunter** 社区和 EFF 持续研究 **5G 监控检测能力**：

- **协议分析研究：** 对 5G 协议开展研究，可能会为未来 **Rayhunter** 版本带来新的检测方式。
- **硬件兼容性研究：** 评估现有 **Rayhunter** 兼容设备能否升级以检测 5G 监控尝试。
- **威胁态势监测：** 跟踪具备 5G 能力的监控设备的开发和部署，为未来 **Rayhunter** 开发提供依据。

随着 5G 逐步部署，威胁行为者仍依赖成熟的降级攻击方法，**Rayhunter** 在当前电信环境中仍是**重要的监控检测工具**，预计未来数年仍有用处。

### 重新分析录制文件

**Rayhunter** 持续改进检测能力。你可以在 Web 界面点击“N warnings”，选择“re-analyze”，用更新后的启发式重新分析旧录制文件。

### 桌面分析

高级用户可使用 **Rayhunter** 提供的命令行工具 `rayhunter-check`，在桌面系统上分析 PCAP 和 QMDL 文件：

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # 调试模式
```

## 兼容设备

**Rayhunter** 支持多种配备 Qualcomm 调制解调器的移动热点，这些调制解调器需提供 `/dev/diag` 接口。

{{< figure src="/img/rayhunter-device-regions.svg" alt="按地区划分的 Rayhunter 设备兼容性" caption="Rayhunter 安装的设备兼容性和地区建议" >}}

### 推荐设备

以下设备已经过广泛测试，并在 **Rayhunter** 社区中常用：

#### Orbic RC400L（有时以 Kajeet RC400L 品牌销售）
- **推荐地区：** 美洲
- **支持频段：**
  - 5G：n260/n261、n77、n2/5/48/66
  - 4G：2/4/5/12/13/48/66
  - 全球和漫游：n257/n78
- **购买渠道：** [全新 **Rayhunter** **Orbic RC400L**](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822) 和 [Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)，均为兼容设备。
- **价格范围：** 可通过 STS Collective 购买专业型号。

#### TP-Link M7350
- **推荐地区：** 非洲、欧洲、中东（也可在美洲使用，但通常价格较高）。
- **特殊要求：** 录制文件需要 FAT 格式的 SD 卡。
- **购买渠道：** [TP-Link M7350 **Rayhunter**](https://stscollective.com/collections/rayhunter)，有已验证兼容的型号。

### 已确认可用的设备

**Rayhunter** 也已确认可用于以下设备：

- **Wingtech CT2MHS01**（美洲），[购买 **Rayhunter**](https://stscollective.com/collections/rayhunter)
- **Tmobile TMOHS1**（美洲），[购买 **Rayhunter**](https://stscollective.com/collections/rayhunter)
- **TP-Link M7310**（非洲、欧洲、中东），[购买 **Rayhunter**](https://stscollective.com)
- **PinePhone 和 PinePhone Pro**（全球），[购买 **Rayhunter**](https://stscollective.com)
- **FY UZ801**（亚洲、欧洲），[购买 **Rayhunter**](https://stscollective.com)
- **Moxee 热点**（美洲），[Moxee K779HSDL **Rayhunter**](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)

### 特定设备安装说明

#### Orbic/Kajeet RC400L

Orbic RC400L 是开发 **Rayhunter** 时使用的原始设备。可通过 STS Collective [购买 **Rayhunter**](https://stscollective.com)。

**安装方式：**
- **网络安装：** `./installer orbic`（推荐，通过 WiFi 安装）
- **USB 安装：** `./installer orbic-usb`（可启用 ADB 和 root shell）

**默认密码：**
- **Verizon RC400L：** 管理员密码始终与 WiFi 密码相同（可在设备菜单中查看）。
- **Kajeet/Smartspot RC400L：** `$m@rt$p0tc0nf!g`
- **Moxee 设备：** 密码格式为 `12$XXX`，其中 XXX 是 WiFi 密码的最后 3 位数字（在电池下方查看 WiFi 密码）。

**Shell 访问：** 安装后使用 `./installer util orbic-shell`。

#### TP-Link M7350/M7310

这些设备可稳定运行 **Rayhunter**，并可通过 STS Collective [购买 **Rayhunter**](https://stscollective.com)。

**安装：** `./installer tplink`（不需要管理员密码）
**存储：** 安装前插入 FAT 格式的 SD 卡
**Shell 访问：** `./installer util tplink-shell`

#### 专用设备

**PinePhone 和 PinePhone Pro：** 全球兼容，可通过 STS Collective [购买 **Rayhunter**](https://stscollective.com)
**UZ801：** 常用于亚洲和欧洲地区，可通过 STS Collective [购买 **Rayhunter**](https://stscollective.com)
**Wingtech CT2MHS01：** 面向美洲的设备，可通过 STS Collective [购买 **Rayhunter**](https://stscollective.com)

### 添加新设备

**Rayhunter** 有望支持任何采用 Qualcomm 调制解调器并提供 `/dev/diag` 的设备。如果你希望 **Rayhunter** 支持某款设备，请在官方 GitHub 仓库发起讨论。

## REST API 文档

**Rayhunter** 提供完整的 REST API，可通过程序访问设备状态、录制文件和配置。你可以借此将它集成到其他安全工具和自动监测系统。

### 官方 API 文档

完整 API 参考资料包括详细的端点说明、请求和响应示例，以及身份验证方法。请参阅[官方 **Rayhunter** REST API 文档](https://efforg.github.io/rayhunter/api-docs/)。

### API 端点

**Rayhunter** API 的访问地址为 `http://[device-ip]:8080/api/`，并提供以下端点：

- **系统状态：** 监测设备运行状况和 **Rayhunter** 运行状态
- **录制文件管理：** 开始、停止和下载录制文件
- **告警查询：** 获取检测告警和分析结果
- **配置：** 通过程序更新 **Rayhunter** 设置
- **启发式控制：** 启用或禁用特定检测算法
- **设备信息：** 获取设备规格和功能
- **网络监测：** 访问实时蜂窝网络数据
- **事件日志：** 查询历史检测事件和告警

### 身份验证

API 使用与 Web 界面相同的身份验证。请确保 **Rayhunter** 设备受到妥善保护，且仅授权用户可以访问。

### 集成示例

**Rayhunter** **REST API** 可集成到各种安全监测平台、SIEM 系统和自定义自动化工具。请参阅[官方 API 文档](https://efforg.github.io/rayhunter/api-docs/)获取完整实现示例和最佳实践。

## 故障排查

### 常见安装问题

**USB 连接问题：** 尝试更换 USB 线缆或端口。USB 连接故障经常导致安装失败。*这是安装失败最常见的原因。*

**macOS 安全问题：** 如果看到“No Orbic device found”，请在安全设置中暂时将“允许配件连接”改成“始终”。

**设备检测：** 安装后启用测试启发式，确认 **Rayhunter** 正常运行。

### 获取帮助

安装支持和故障排查资源：
- 查看 **Rayhunter** 官方文档。
- 使用 `./installer --help` 和 `./installer util --help` 查看命令选项。
- 在 GitHub 讨论区寻求社区支持。
- 如有设备兼容性问题，请联系 **[STS Collective](https://stscollective.com)**。

## 常见问题解答（FAQ）

### 一般问题

#### 什么是 IMSI 捕获器，它如何工作？

IMSI 捕获器（也称为 StingRay、蜂窝基站模拟器或伪基站）是一种模拟合法蜂窝基站以拦截移动设备通信的监控设备。它会迫使附近设备连接恶意设备而非合法基站，使操作人员得以收集设备标识符（IMSI 号码）和位置数据、通话元数据，甚至拦截通信。**Rayhunter** 通过识别异常蜂窝网络行为模式检测此类设备。

#### Rayhunter 能检测所有类型的监控设备吗？

**Rayhunter** 专门检测运行在 2G、3G 和 4G/LTE 网络上的 IMSI 捕获器和蜂窝基站模拟器。它无法检测其他类型的监控，例如 WiFi 监控、GPS 跟踪设备、实体监视，或不依赖降级攻击的原生 5G 监控。**Rayhunter** 是全面隐私保护策略的一部分。

#### 使用 Rayhunter 合法吗？

在大多数司法辖区，使用 **Rayhunter** 完全合法，因为它是被动监测工具，不会干扰蜂窝网络或其他设备。它只会分析设备自然接收到的蜂窝信号。但各地法律不同，用户应确认当地法规是否允许使用。EFF 将 **Rayhunter** 开发为合法的隐私保护工具。

### 技术问题

#### Rayhunter 为什么需要 SIM 卡，却不要求有效服务？

SIM 卡提供国际移动用户识别码（IMSI），设备需要该识别码才能向蜂窝网络进行身份验证，并参与 **Rayhunter** 所监测的蜂窝协议交换。如果没有 SIM 卡，设备就无法连接蜂窝网络，**Rayhunter** 也没有网络活动可供分析，以识别可疑模式。

#### Rayhunter 正常运行时会使用多少数据？

**Rayhunter** 的基础监测几乎不消耗数据，因为它主要分析蜂窝协议信息，而非互联网流量。但如果启用 ntfy 远程通知，或同时将设备用作热点，数据用量就会相应增加。监测本身几乎不占用带宽。

#### 我能在将设备用作移动热点时运行 Rayhunter 吗？

可以，**Rayhunter** 可以与移动热点功能同时运行，但需要有效的蜂窝服务套餐。**Rayhunter** 监测功能独立于热点功能，不过同时使用这两项功能会增加电池消耗。

#### WiFi 和 USB 安装方法有什么区别？

多数用户推荐使用 **WiFi 方法**，通过设备无线接口安装 **Rayhunter** 并提供标准功能。**USB 方法**会启用 Android Debug Bridge (ADB) 访问，适合需要调试功能的高级用户，但步骤更复杂，普通安装不需要使用此方法。

### 设备和兼容性问题

#### Rayhunter 为什么只支持部分设备？

**Rayhunter** 需要使用能够提供 `/dev/diag` 接口的 Qualcomm 调制解调器，以访问蜂窝协议信息。出于安全原因，大多数消费级设备不会开放此接口。已支持的设备都经过专门测试，确认符合 **Rayhunter** 的要求。

#### 我可以在普通智能手机上安装 Rayhunter 吗？

不可以。**Rayhunter** 无法安装在普通智能手机上。它需要配备特定 Qualcomm 调制解调器、并开放诊断接口的专用移动热点设备。支持的设备包括 Orbic RC400L、TP-Link M7350 和其他一些移动热点型号。

#### 如果在不兼容的设备上尝试安装 Rayhunter，会发生什么？

**Rayhunter** 安装程序包含设备检测功能，通常会拒绝在不兼容硬件上安装。强行安装到不受支持的设备上可能损坏设备或导致设备无法运行。安装前务必确认设备兼容。

#### 不同地区需要不同设备吗？

需要。各地区蜂窝频段不同。Orbic RC400L 针对美洲网络优化，而 TP-Link M7350 适用于欧洲、非洲和中东地区。**Rayhunter** 设备兼容性信息包含地区建议，可帮助你根据所在地选择合适设备。

### 使用和配置问题

#### 如何确认 Rayhunter 设备运行正常？

在 **Rayhunter** 配置中启用 Test Heuristic。每次设备检测到蜂窝基站时都会触发告警，以确认系统运行正常。正常情况下设备屏幕应显示绿色线条。验证后请记得关闭测试启发式，因为它会产生大量告警。

#### Rayhunter 发出告警时，我应该怎么做？

当 **Rayhunter** 检测到可疑活动时，先记录你所在位置和当时情况。网络优化或设备问题可能造成误报。如果在同一地点或敏感活动期间持续收到告警，可考虑换地点，并在 Web 界面查看告警详情，了解检测到的内容。

#### Rayhunter 应多久更新一次？

**建议每月更新。** 请查看发布页面，了解新的启发式方法和兼容性改进。新的检测启发式和设备兼容性经常更新。EFF 持续根据不断变化的监控技术改进 **Rayhunter** 功能。更新方法与首次安装相同。

#### Rayhunter 可以同时保护多个人吗？

**Rayhunter** 能检测周围区域内的 IMSI 捕获器，因此可能保护范围内的多个人（根据信号强度，通常为数百米）。不过，重视监控检测的每个人都应考虑使用自己的 **Rayhunter** 设备，以获得最佳保护和配置控制。

### 安全和隐私问题

#### 使用 Rayhunter 会让我更容易被监控者注意到吗？

**Rayhunter** 以被动方式运行，不会发出可让监控设备识别其身份的信号。但使用任何安全工具都会表明你重视隐私。对于记者和活动人士等高风险人士，检测收益通常大于风险。

#### 监控设备能发现我正在使用 Rayhunter 吗？

Rayhunter 是被动监测系统，不会传输可识别身份的信号。监控人员无法从蜂窝协议层面检测到 **Rayhunter** 的使用。如果启用了 **Rayhunter** 远程通知，实体观察设备或分析网络流量仍可能发现你在使用 **Rayhunter**。

#### Rayhunter 会收集我的哪些信息？

**Rayhunter** 分析蜂窝协议信息，并在本地设备上保存检测告警。除了检测算法必要的信息，它不会收集个人信息、通信内容或位置数据。除非你主动启用远程通知，所有数据都保存在设备本地。

### 高级问题

#### 我可以在电脑上分析 Rayhunter 数据吗？

可以。**Rayhunter** 提供命令行工具 `rayhunter-check`，用于在桌面系统上分析录制的 PCAP 和 QMDL 文件。高级用户可利用完整的计算机资源详细分析检测事件和调查可疑活动。

#### Rayhunter 在人口密集的城市环境中表现如何？

人口密集的城市中，合法蜂窝基站较多，网络优化和基站切换也更频繁，因此误报率可能增加。**Rayhunter** 算法旨在区分正常网络行为和监控活动，但在人口稠密地区，用户可能需要调整灵敏度设置。

#### Rayhunter 在国际旅行期间有效吗？

旅行期间 **Rayhunter** 的有效性取决于设备与当地蜂窝频段及漫游协议的兼容性。检测算法在全球均可工作，但请确认设备支持目的地使用的频段。完整使用功能可能需要国际漫游。

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="一名使用笔记本电脑查看 **Rayhunter** 告警的人士，身旁放着移动热点设备，周围可见城市蜂窝基站" >}}

______

**Rayhunter** 是个人隐私保护和监控检测领域的重要进展。通过在兼容设备上正确刷写和配置 **Rayhunter**，你便可使用有效功能检测 **IMSI 捕获器**，并保护移动通信免遭未经授权的监控。

无论你是记者、活动人士、安全专业人员，还是重视隐私的人士，**Rayhunter** 都能帮助你在监控日益普遍的环境中维护移动安全。如需购买已验证兼容的设备，请查看可信安全设备供应商提供的[在售 Rayhunter 设备](https://stscollective.com)。

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  购买 Rayhunter 设备，享受 20% 折扣
{{< /centerbutton >}}

## 参考资料

- [Rayhunter 官方 GitHub 仓库](https://github.com/EFForg/rayhunter)
- [Rayhunter 最新版本](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective，Rayhunter 设备供应商](https://stscollective.com)
