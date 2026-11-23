---
title: "ESP32 WiFi Canary：被动检测 2.4 GHz 威胁"
date: 2026-06-06
lastmod: 2026-11-22
toc: true
draft: false
description: "ESP32 WiFi Canary 技术解析。这款 2.4 GHz 被动传感器可检测 邪恶双胞胎攻击、解除认证、安全降级和信标泛洪。"
genre: ["网络安全", "WiFi 安全", "物联网安全", "安全研究", "嵌入式系统", "隐私工具", "ESP32 项目", "硬件安全", "无线安全", "开源安全"]
tags: ["ESP32", "WiFi Canary", "M5Stack Atom Lite", "解除认证检测", "Evil twin 检测", "WiFi 安全", "WiFi 被动监控", "802.11 管理帧", "网络安全", "物联网安全", "NeoPixel", "SK6812", "PlatformIO", "C++", "开源", "安全传感器", "无线威胁检测", "BSSID 监控", "SSID 监控", "安全降级检测", "信标泛洪检测", "WiFi 监控", "RGB LED", "混杂模式", "嵌入式安全", "旅行安全", "酒店 WiFi 安全", "咖啡馆 WiFi", "安全意识", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/"
cover: "/img/cover/esp32-wifi-canary-passive-wifi-threat-detection-2026.webp"
coverAlt: "插入 USB 端口的 ESP32 WiFi Canary 风格小型设备插图。RGB LED 发出多种颜色，表示设备具备威胁检测能力。"
coverCaption: ""
---

**拇指大小、从不发射信号的 WiFi 被动威胁传感器**

## 公共 WiFi 的问题

每次连接酒店、咖啡馆或机场的 WiFi，你都在信任眼前的接入点是真实的。问题在于，负责通告网络、管理连接和协调客户端的 **802.11 管理帧**，在大多数部署中 *完全没有经过身份验证*。只需普通设备，任何人都能克隆 SSID、向客户端发送大量解除认证帧，或在合法 WPA2 网络旁设立开放诱饵网络。

[**ESP32 WiFi Canary**](https://github.com/simeononsecurity/esp32-wifi-canary) 是一款被动感知传感器，以很小的体积应对这一现实问题。设备可装入 M5Stack Atom Lite，大小约如方糖，连接任意 USB 端口后学习周围环境，并在检测到疑似无线威胁的模式时点亮 RGB LED。

它不连接任何网络，不收集凭据，也不发送任何帧。它只观察、计分，并通过颜色告诉你当前状况。

本文是该项目的完整技术参考，介绍检测内容、置信度模型、构建和刷写步骤，以及实际使用中的限制。

---

## ESP32 WiFi Canary 的功能与非功能

### 始终被动

WiFi Canary 使用两种无线模式，但不会同时运行：

1. **混杂模式**：不加入任何网络，接收并检查解除认证、解除关联等 802.11 管理帧。
2. **扫描模式**：主动扫描附近接入点，并与已学习的基线比较。

设备绝不会：
- 关联或连接任何网络
- 捕获数据帧或凭据
- 发送任何 802.11 帧
- 将信息写入持久闪存
- 与互联网通信

**所有学习到的信息都保存在 RAM 中，并在重启后清除。** 这是有意的设计：Canary 是一个**传感器**，不是捕获设备。

### LED 就是接口

设备没有显示屏、应用或 Web 界面。唯一输出是连接到 M5Stack Atom Lite GPIO 27 的 **SK6812 RGB NeoPixel**。LED 用四种状态传达信息：

| LED 状态 | 含义 |
|---|---|
| 🔵 蓝色（慢速脉冲） | 启动中，正在建立基线 |
| 🟢 绿色（常亮） | 正常，没有高置信度问题 |
| 🟡 黄色（常亮） | 注意，检测到可疑模式 |
| 🔴 红色（快速脉冲） | 警报，检测到置信度更高的威胁 |

启动约需 **24 秒**（3 次扫描，每次 8 秒）。LED 从蓝色切换后，基线已可用，设备开始主动监控。

---

## 硬件

### 首选目标：M5Stack Atom Lite

本项目面向 M5Stack Atom Lite 设计。这是一款完整的 ESP32 开发平台，外壳尺寸为 24 × 24 mm。

| 组件 | 详细信息 |
|---|---|
| MCU | ESP32-PICO-D4 |
| LED | 单个 SK6812 RGB NeoPixel（GPIO 27） |
| 按钮 | GPIO 39，低电平有效 |
| USB | CP2104 UART 桥接器 |
| 电源 | USB-C，扫描期间约 80–120 mA |

**无需面包板、外部组件或焊接。** 接入 USB 电源即可运行。

### 通用 ESP32 DevKit（用于开发和测试）

项目还提供第二个 PlatformIO 构建环境（`esp32dev`），面向标准 ESP32 开发板。此配置中：

- 使用 GPIO 2 上的板载 LED，而不是 NeoPixel
- 启用完整串口调试输出
- 所有检测逻辑与 Atom Lite 构建相同

因此，使用 5 美元的 ESP32 DevKit 也能运行项目，并可在没有目标硬件的情况下测试检测逻辑。

---

## 基线学习过程

### 基线为何重要

如果 Canary 对城市里的每个开放网络都报警，就毫无用处。ESP32 WiFi Canary 会先学习环境，再给威胁计分。运行的第一阶段会建立周围合法存在的接入点**参考表**。

### 三次扫描，24 秒

启动后，设备依次执行三次 WiFi 扫描，每次之间会暂停。全部完成后，设备将学习到的接入点集合保存为基线，包括 SSID、BSSID、加密类型和信号强度。

此阶段的串口输出示例：

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 18 APs
[canary] baseline scan 2/3
[canary] baseline scan start (aps=18 score=0)
[canary] scan found 19 APs
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
  ...
[canary] STARTUP → NORMAL  (score=0  "")
```

LED 从蓝色变为绿色后，设备便进入完整运行状态。

---

## 检测内容：威胁类别

WiFi Canary 监控六种威胁模式。每种模式都会为决定 LED 状态的**置信度分数**加分。*不会将任何单一指标视为确凿证据，只有累积多个相互印证的信号后才会升级状态。*

### 1. 解除认证或解除关联突发

**802.11 管理帧子类型 10（解除关联）和 12（解除认证）**是常见 WiFi 攻击手段。任何设备都能发送这些帧，接收帧的客户端会与接入点断开连接。

Canary 在**混杂模式**下监控这些帧，并在**5 秒滚动窗口**内按源 MAC 地址计数。

| 条件 | 加分 |
|---|---|
| 5 秒内同一来源发送 ≥ 8 帧 | +2 |
| 5 秒内同一来源发送 ≥ 20 帧 | +4 |
| 广播解除认证帧 ≥ 5 个 | +1 |

**阈值为何重要**：客户端在接入点之间漫游时，会产生少量合法的解除认证或解除关联帧。*攻击工具生成的模式明显不同*，它们会针对目标持续每秒发送数百帧。5 秒窗口和 8 帧下限可过滤普通漫游噪声，同时捕获 `aireplay-ng` 等工具产生的持续突发。

### 2. 已知加密网络的开放克隆（邪恶双胞胎攻击）

**这是置信度最高的检测。** 邪恶双胞胎攻击 攻击通常会：

1. 建立已知 WPA2 SSID 的开放副本（无需密码）。
2. 提高它的信号强度，让客户端自动连接，而不是连接真实 AP。

完成基线学习后，如果扫描发现原本仅使用 WPA、WPA2 或 WPA3 的 SSID 现在变成 **OPEN**：

| 条件 | 加分 |
|---|---|
| 同一 SSID 以前加密，现在开放 | +3 |
| BSSID 未出现在基线中 | +1 |
| 克隆信号比已知 AP 强 ≥ 10 dB | +1 |

若酒店 WiFi SSID 的开放克隆信号比真实 AP 强 10 dB，这几乎是典型案例。*此组合会在一次扫描周期内将分数推至 5（注意）。*

**串口示例**：

```
[canary] OPEN CLONE: SSID='MyHomeWifi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'MyHomeWifi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'MyHomeWifi'")
```

### 3. 原加密 AP 消失，同时出现开放克隆

更高级的攻击会利用更强的克隆网络吸引客户端，同时通过解除认证使真实 AP 离线。

| 条件 | 加分 |
|---|---|
| 基线中的加密 AP 消失，且出现匹配的开放网络 | +3 |

此检测涵盖真实 AP 仍在广播、但在信号强度竞争中落败的场景，也涵盖 AP 正被主动干扰的情况。

### 4. 安全降级

发现与基线中 SSID 相同、但加密强度更弱的网络。

| 条件 | 加分 |
|---|---|
| WPA3 → WPA2 | +1 |
| WPA2 → WPA | +1 |
| 加密等级下降 2 级或更多 | +3 |

*降级为开放网络的情况由 邪恶双胞胎攻击 检测处理，并获得更高分数。* 本类别关注纯粹比较开放和加密时容易漏掉的部分降级。

### 5. 来自意外厂商的重复 SSID

SSID 和安全类型与基线 AP 相同，但 BSSID 的**厂商 OUI**（MAC 地址前 3 个字节）不同。

| 条件 | 加分 |
|---|---|
| 同一 SSID 的基线 AP 与当前 AP 的 OUI 不同 | +1 |
| 克隆信号也强 ≥ 10 dB | +2 |

*此项刻意只给低分。* 企业网络、网状系统和 ISP 部署的 AP 可能会合法地使用不同厂商、但 SSID 相同的多个 BSSID。该信号应与其他证据累计，而不是单独触发警报。

### 6. 信标 / SSID 泛洪

统计**30 秒滚动窗口**内出现的新增 SSID，即基线中不存在的 SSID。

| 条件 | 加分 |
|---|---|
| 30 秒内新增 SSID ≥ 15 个 | +2 |
| 30 秒内新增 SSID ≥ 30 个 | +3 |

**信标泛洪攻击**通过广播成千上万个假 SSID，干扰客户端扫描表或阻止合法信标正常工作。对大多数环境来说，30 秒内出现 15 个陌生 SSID 都很反常。

---

## 置信度计分模型

所有检测信号都会汇总为一个整数**威胁分数**，并决定 LED 状态：

| 分数范围 | LED 状态 |
|---|---|
| 0–2 | 正常（绿色） |
| 3–5 | 注意（黄色） |
| 6 及以上 | 警报（红色，快速脉冲） |

### 分数衰减

如果没有新触发事件，分数会**每 60 秒减少 1 分**。这是项目中最重要的实用设计之一：

- 一次解除认证突发会将状态推至注意，但攻击停止后会在几分钟内自动回到正常。
- 持续攻击不断产生事件，会使警报状态一直维持。
- 无需用户操作或重启，设备便会自行恢复。

因此：
- **短暂异常**（漫游事件、邻近网络的短暂变化）会自行消失。
- **持续攻击**会一直被标记。
- 不重复的单次事件不会造成**警报疲劳**。

### 按钮重置

按下 Atom Lite 上的 GPIO 39 按钮会执行两项操作：

1. 将当前完整 AP 表输出到串口，方便核查设备确切检测到的内容。
2. 将威胁分数重置为 0，立即恢复绿色状态，以便从新一轮扫描开始观察。

---

## 构建与刷写

### 所需条件

- **PlatformIO**（CLI 或 VS Code 扩展）
- **M5Stack Atom Lite**（也可使用 ESP32 DevKit 测试）
- USB-C 线缆

### 刷写到 M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/esp32-wifi-canary.git
cd esp32-wifi-canary

# 构建并刷写
pio run -e atom-lite --target upload

# 以 115200 baud 打开串口监视器
pio device monitor -b 115200
```

### 刷写到通用 ESP32 DevKit

```bash
pio run -e esp32dev --target upload
```

DevKit 构建使用 GPIO 2（板载 LED）并输出完整串口日志。它不会驱动 NeoPixel。检测逻辑与 Atom Lite 构建完全相同。

### 项目结构

```
esp32-wifi-canary/
├── main.cpp              # 所有固件逻辑
├── platformio.ini        # 构建环境 (atom-lite, esp32dev)
├── partitions_4mb.csv    # 4MB 闪存分区表
└── README.md
```

全部固件都位于**一个 C++ 源文件**中。检测逻辑不依赖外部库，只使用 ESP32 Arduino 框架执行 WiFi 扫描、混杂模式回调和 NeoPixel 控制。

### platformio.ini 环境

```ini
[env:atom-lite]
platform = espressif32
board = m5stick-c
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

`atom-lite` 环境使用 `m5stick-c` 开发板定义（采用相同的 ESP32-PICO-D4 芯片，并使用与 GPIO 27 NeoPixel 兼容的引脚映射）。

---

## 串口输出参考

设备以 **115200 baud** 输出详细日志。所有日志行都带有 `[canary]` 前缀，便于筛选。

### 启动序列

```
==============================================
 Travel WiFi Canary v1.0
 Passive 2.4 GHz awareness sensor
==============================================
[canary] setup done - starting baseline learning
[canary] baseline scan start (aps=0 score=0)
[canary] scan found 18 APs
[canary] baseline scan 1/3
...
[canary] baseline complete: 19 APs learned
  [00] MyHomeWifi                    aa:bb:cc:dd:ee:ff ch06 WPA2     -52 dBm
  [01] XFINITY                       11:22:33:44:55:66 ch01 WPA2     -71 dBm
[canary] STARTUP → NORMAL  (score=0  "")
```

### 检测事件

```
[canary] normal scan start (aps=19 score=0)
[canary] scan found 21 APs
[canary] OPEN CLONE: SSID='HotelWiFi' baseline=WPA2 clone=OPEN bssid=de:ad:be:ef:00:01 rssi=-48/-52
[canary] score +4 → 4  "open clone of encrypted SSID 'HotelWiFi'"
[canary] NORMAL → CAUTION  (score=4  "open clone of encrypted SSID 'HotelWiFi'")
```

### 分数转换

```
[canary] CAUTION → NORMAL  (score=2  "score decay")
[canary] NORMAL → ALERT    (score=6  "sustained deauth burst + open clone")
```

串口日志足以说明设备看到了什么、何时看到，以及分数为何变化。即使你不看 LED，它也能用作**被动审计日志**。

---

## 检测说明与实际限制

README 对设备的能力限制说明得很坦诚，值得在此详细重述。

### 误报的可能原因

**企业网络和网状网络**是误报的主要来源。大型企业部署、拥有许多 AP 的酒店，或 Eero、Google WiFi 等网状系统都可能合法地表现为：
- 同一 SSID 对应多个不同厂商 OUI 的 BSSID（厂商检测）
- 不同频段采用不同安全配置（安全降级检测）
- 网状网络调整时，接入点出现或消失

具有多个频段 SSID 的**Airbnb 和 SOHO 路由器**也可能出现厂商 OUI 不匹配，例如 2.4 GHz 和 5 GHz 无线电从不同地址块使用连续 MAC 地址。

*邻近网络的短暂变化*：加密网络可能暂时从扫描中消失，之后以不同参数重新出现（固件升级、重启或重新配置），从而短暂触发检测。

置信度计分和衰减机制旨在*减少误报，而不是完全消除误报*。

### 漏报的可能原因

精心构造的 **邪恶双胞胎攻击 攻击**若同时满足以下条件：
- 欺骗合法 AP 的完全相同 BSSID，使 OUI 匹配
- 安全类型完全相同（IE 配置正确的 WPA2）
- 信号强度与真实 AP 相差不超过 10 dB

*分数可能不足以达到注意阈值。* 解除认证部分会增加分数，因为它需要把客户端从真实 AP 上赶走；但若攻击者很老练并尽量减少解除认证帧，分数仍可能低于阈值。

### 无线模式切换间隙

**ESP32 WiFi 无线电无法同时处于混杂模式并执行主动 AP 扫描。** 固件会在模式间切换，因此**约 3 秒的扫描期间到达的解除认证帧不会被捕获**。*攻击者若将突发时间精确安排在扫描窗口内，理论上能绕过检测*，但这需要掌握设备的扫描时间表。

### 仅支持 2.4 GHz

ESP32 无线电仅支持 2.4 GHz。**不会扫描或监控 5 GHz 和 6 GHz 网络。** *若攻击使用 5 GHz 邪恶双胞胎攻击，此设备无法检测。*

### 被动检测范围

检测解除认证需要设备位于相关帧的接收范围内。*距离很远、使用高度定向天线的攻击者，或专门攻击远离 Canary 的客户端的攻击者，可能无法发出足以触发计数器的信号。*

---

## 使用场景

### 携带敏感工作出行

Canary 主要用于旅行。将它插入笔记本 USB 端口、酒店房间 USB 插座或移动电源，让它学习酒店或会议中心的环境。之后若出现酒店 SSID 的开放克隆这一常见攻击，设备至少会进入注意状态。

### 咖啡馆和公共 WiFi

开放 WiFi 环境是 邪恶双胞胎攻击 最常见的攻击面。Canary 到达时会学习合法咖啡馆 AP，然后监视是否出现竞争 SSID。

### 安全意识与教育

串口输出会以易读格式详细记录所见内容。安全培训中，实时展示解除认证突发，并观察 LED 变色，通常比幻灯片更有效。

### 实验室被动监控

在家庭实验室或小型办公室，Canary 可作为常驻环境监视器。LED 无需主动监控即可显示状态。按下按钮后，设备会输出当前看到的网络表。

---

## 架构说明

### 为什么使用单一分数，而不是分别报警

置信度模型将不同信号汇总为一个数字，而不是提供多个告警类别。这是有意的用户体验设计：输出接口只有一个三状态 LED。每类检测单独告警需要显示屏或应用。*计分模型把嘈杂、部分相关的信号转换成一个可采取行动的指标。*

### 为什么分数会衰减

没有衰减时，一次误报就需要手动按按钮清除。每 60 秒衰减一次后，短暂异常会在几分钟内自行消失。**Canary 因此能无人看管运行**，例如放在包里、酒店房间或汽车中，并在瞬态事件过去后恢复基线状态。

### 为什么基线扫描三次

单次扫描可能漏掉当时没有广播的 AP（例如 AP 刚好处于扫描间隙或暂时断电）。*在约 24 秒内扫描三次，能在开始监控前更完整地了解稳定环境。*

---

## 参与贡献与项目状态

项目采用被动使用许可，托管在 [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)。代码只有一个 `main.cpp`，便于阅读、审计和扩展。

如果你使用 PlatformIO 和 ESP32，该项目无需修改即可为 Atom Lite 和标准 DevKit 环境编译。

---

## 与其他 WiFi 监控方式比较

| 方式 | 被动？ | 不需要凭据 | 单 LED 输出 | 便携外形 |
|---|---|---|---|---|
| ESP32 WiFi Canary | ✅ | ✅ | ✅ | ✅ |
| Kismet（笔记本） | ✅ | ✅ | ❌（需要显示屏） | ❌（笨重） |
| WiFi Pineapple | ❌（主动） | ❌ | ❌ | 部分满足 |
| 无线 IDS（企业级） | ✅ | ✅ | ❌（需要基础设施） | ❌ |
| 手动扫描（手机应用） | 部分 | ✅ | ❌ | ✅ |

Canary 填补了一个具体空缺：**无需交互、无需联网、持续运行的环境感知**，体积小到可以常驻钥匙扣或笔记本包中。

---

## 结论

ESP32 WiFi Canary 是一款功能范围明确的工具：监视周围 2.4 GHz 环境，在发现异常时改变颜色。它不打算成为完整的无线入侵检测系统、数据包捕获工具或取证分析器。它是一只“金丝雀”，用被动传感器提醒你环境可能已经变得危险。

**置信度计分模型**、**分数衰减**和**三阶段基线方法**体现了对安全环境传感器常见误报问题的认真考虑。设备可在酒店或会议中心无人看管运行，可靠标示有意义的异常，同时避免对正常网络变化频繁反应。

如果你在构建便携安全工具包、需要在不可信 WiFi 环境中工作，或在寻找有实际用途的 ESP32 项目，WiFi Canary 值得你花一个下午和 15 美元购买 M5Stack Atom Lite。

**GitHub**: [github.com/simeononsecurity/esp32-wifi-canary](https://github.com/simeononsecurity/esp32-wifi-canary)

---
