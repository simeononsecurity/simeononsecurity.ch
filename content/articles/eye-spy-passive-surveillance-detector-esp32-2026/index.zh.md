---
title: "Eye Spy：ESP32被动监控与追踪器检测器"
date: 2026-06-07
lastmod: 2026-11-22
toc: true
draft: false
description: "Eye Spy v1.1技术参考。这是一款基于ESP32的BLE与WiFi被动检测器，可识别摄像头、追踪器、无人机及相关信号。"
genre: ["隐私工具", "反监控", "物联网安全", "嵌入式系统", "安全研究", "WiFi安全", "蓝牙安全", "ESP32项目", "硬件安全", "开源安全"]
tags: ["Eye Spy", "ESP32", "M5Stack Atom Lite", "监控检测", "反监控", "BLE检测", "WiFi扫描", "AirTag检测", "ALPR检测", "Flock Safety", "执法记录仪检测", "无人机检测", "OpenDroneID", "NimBLE", "NeoPixel", "SK6812", "PlatformIO", "C++", "开源", "隐私", "被动BLE", "监视器模式", "OUI检测", "追踪器检测", "Axon执法记录仪", "Ray-Ban Meta", "Samsung SmartTag", "Tile追踪器", "隐藏摄像头", "simeononsecurity"]
canonical: "https://simeononsecurity.com/articles/eye-spy-passive-surveillance-detector-esp32-2026/"
cover: "/img/cover/eye-spy-passive-surveillance-detector-esp32-2026.webp"
coverAlt: "深蓝色背景上的小型M5Stack Atom Lite插画，周围环绕着彩色信号波，代表通过蓝牙和WiFi检测监控设备。"
coverCaption: ""
---

**一款拇指大小的被动传感器，可在有设备观察你时发出提示**

## 引言：看不见的监控环境

物理环境中安装的观察、录制和跟踪设备越来越多，包括路口的车牌读取器、执法人员佩戴的执法记录仪、出租房内的摄像头、藏在包或汽车里的商用AirTag类追踪器，以及商店入口处的监控摄像头。大多数设备通过**Bluetooth LE**或**WiFi**进行无线通信。*其中许多通信会向周围开放广播，拥有合适接收器的人都能检测到。*

[**Eye Spy**](https://github.com/simeononsecurity/eye-spy)是一款利用这一特点的被动监控检测工具。它运行在**M5Stack Atom Lite**上。这是一块ESP32-PICO-D4开发板，大小约等于一颗方糖。Eye Spy持续监控BLE和WiFi频段，寻找录制设备、监控摄像头、**ALPR**（自动车牌识别）系统、无人机和个人追踪器的电子特征。发现信号时，它会改变RGB LED的颜色。

*它不连接任何设备，也不发送数据。* 它只监听、评分并亮灯提示。

本文是一份完整的技术参考，介绍Eye Spy能检测什么、置信度评分模型如何工作、各检测引擎的设计、如何组装并刷写设备，以及实际使用中的限制。

**不想自己组装？** STS Collective提供预刷写、开箱即用的**[Eye Spy检测器](https://stscollective.com/collections/eye-spy-passive-surveillance-detectors)**。读者优惠码**SIMEONONSECURITY**可享最高20%折扣。

{{< stscollective-ad "eyespy" >}}

---

## LED指示灯：完整的用户界面

与[ESP32 WiFi Canary：2.4 GHz被动威胁检测器](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/)类似，Eye Spy的全部输出来自一个连接到M5Stack Atom Lite GPIO 27的SK6812 RGB NeoPixel。LED始终显示四种威胁等级之一：

| 颜色 | 含义 | 分数范围 |
|-------|-------------|---------------------|
| 🔵 蓝色脉冲 | 启动 / 首次扫描 | -- |
| 🟢 常亮绿色 | 未发现设备 | 0–2 |
| 🟡 常亮黄色 | 注意：附近可能有录制设备 | 3–5 |
| 🔴 红色闪烁 | 警报：发现监控或追踪设备 | 6+ |

**一次高置信度检测（Axon执法记录仪、Flock Safety摄像头、匹配的ALPR OUI或AirTag）就足以在一个检测周期内将分数推至红色警报。** 多次中等置信度检测会累积至黄色，也可能合并达到红色。

---

## 硬件

### 主要目标：M5Stack Atom Lite

| 组件 | 详情 |
|-----------|--------|
| 开发板 | M5Stack Atom Lite |
| MCU | ESP32-PICO-D4 |
| LED | GPIO 27上的SK6812 NeoPixel |
| 按钮 | GPIO 39（仅输入） |
| 闪存 | 4 MB |

Atom Lite是一套完整的独立平台。**无需焊接、面包板或外接组件。** 接上USB即可运行。

### 通用ESP32 DevKit

第二个PlatformIO构建环境（`esp32dev`）适用于任何带有GPIO 2板载LED的标准ESP32 DevKit。所有检测逻辑都以相同方式运行。若不需要Atom Lite的小型外形，这个构建环境适合开发、测试检测逻辑或部署使用。

---

## 评分系统

Eye Spy采用**置信度评分模型**，将所有检测引擎的信号汇总为一个整数。分数决定LED状态（绿色、黄色或红色），并通过两种自动机制进行管理：

### 分数衰减

没有新检测时，分数会**每60秒降低1分**。离开检测到的设备后，无需用户操作，LED会在几分钟内恢复绿色。

### 再次计分的冷却时间

每种检测*类型*都有**120秒冷却时间**，同一来源在此期间无法再次加分。*这可避免单个持续存在的设备无限累积分数。* 仍在范围内的Flock Safety摄像头先加+5分，然后等待120秒才能再次贡献分数。

这两种机制结合起来意味着：

- **短暂检测**（例如一辆装有AirTag的汽车驶过）会自动消退。
- **持续监控**（例如固定部署的执法记录仪）会在你处于范围内时持续保持警报状态。
- **单台设备反复出现**不会导致分数失控增长。

---

## 检测引擎

{{< figure src="eye-spy-ble-wifi-detection-engines-overview.webp" alt="Eye Spy并行BLE与WiFi检测引擎示意图。它们扫描AirTag、执法记录仪、ALPR系统和无人机，并将结果送入置信度评分威胁模型" >}}

Eye Spy持续轮换三个扫描阶段：

**BLE被动扫描（9秒）→ WiFi扫描（约3秒）→ 混杂模式嗅探（5秒）→ 重复**

为正确共享ESP32射频，Eye Spy会在任何WiFi操作前明确停止BLE，并在每个新周期开始时重新启动BLE。

---

### 引擎1：BLE被动扫描

BLE扫描使用**NimBLE，且不会发送扫描请求**。设备监听BLE广播数据包，不发送任何响应。*因此，Eye Spy在电子层面不会被它要检测的设备发现，被动扫描器不会向目标暴露自身。*

为减少密集环境中的误报，信号低于**−90 dBm**的设备会被忽略。

#### BLE检测表

| # | 目标 | 检测方法 | 分数 |
|---|--------|-----------------|-------|
| 1 | **Axon执法记录仪** | BLE MAC OUI `00:25:df`（Axon执法记录仪、Taser设备及执法装备） | +5 🔴 |
| 2 | **Ray-Ban Meta智能眼镜** | BLE服务UUID `0xFD5F` | +5 🔴 |
| 3 | **Flock Safety BLE设备** | BLE设备名包含`Flock`、`Penguin`、`Pigvision`或`FS Ext Battery` | +5 🔴 |
| 4 | **读卡器撇取设备（HC-03/05/06）** | BLE设备名完全匹配，这些蓝牙模块常见于支付终端撇取设备 | +5 🔴 |
| 5 | **Apple AirTag** | 厂商数据`0x004C`的子类型`0x12`/`0x1E`，或原始负载`1E FF 4C 00` / `4C 00 12` | +4 🔴 |
| 6 | **无人机（OpenDroneID BLE）** | BLE服务UUID `0xFFFA`，或应用代码`0x0D`出现在AD服务数据负载中 | +4 🔴 |
| 7 | **Samsung SmartTag** | BLE服务UUID `0xFD5A` | +3 🟡 |
| 8 | **Tile追踪器** | BLE服务UUID `0xFEED`或`0xFEEC` | +3 🟡 |
| 9 | **MeshCore节点** | BLE设备名以前缀`MeshCore-`开头 | +2 🟡 |
| 10 | **iBeacon（零售和场馆追踪）** | 厂商数据`0x004C 0x02 0x15`，用于商店、机场和体育场馆的移动追踪 | +2 🟡 |
| 11 | **未知的持续性设备** | 未分类BLE MAC在至少5分钟内出现至少3次（探查或跟随检测） | +2 🟡 |

#### 重要BLE检测详解

**Axon执法记录仪（+5）**：Axon（原TASER International）生产了美国执法部门广泛部署的执法记录仪系统。OUI `00:25:df`注册给Axon，并用于其可穿戴设备。**检测到一次即可达到警报阈值。**

**Ray-Ban Meta智能眼镜（+5）**：Ray-Ban Meta合作产品包括能够录制视频和拍照的消费级智能眼镜。BLE服务UUID `0xFD5F`是此类设备的特征广播。*这是消费类产品，在人流密集的公共场所也可能出现。* 无论佩戴者的意图如何，都应留意这一等级的检测。

**撇取设备中的蓝牙模块（+5）**：HC-03、HC-05和HC-06是廉价蓝牙串行模块，常见于支付终端覆盖装置和ATM撇取设备。检测逻辑会将设备名与这些模块已知的默认固件名称精确匹配。**出现红色警报时，应立即检查附近的支付终端。**

**Apple AirTag（+4）**：AirTag使用Apple专有的**Nearby Interaction**协议广播。检测逻辑会检查厂商专用数据头（`0x004C` = Apple）和AirTag专用子类型（标准广播为`0x12`，失物广播为`0x1E`）。原始负载模式提供了冗余检测方式。

**OpenDroneID BLE（+4）**：**ASTM F3411 Remote ID**标准也被美国FAA用于商业无人机，定义了无人机广播身份和位置的协议。Eye Spy查找GATT服务UUID `0xFFFA`（指定的Remote ID服务），以及AD服务数据负载中的应用代码`0x0D`。*附近符合标准的商用无人机将触发此检测。*

**未知的持续性设备（+2）**：这是**跟随检测**引擎。它跟踪未被上述特定检测分类的所有BLE MAC。如果相同的未分类MAC在至少五分钟内出现三次或更多次，就会加分。持续性设备跟踪器最多同时监控50个未知MAC，设备离开30分钟后会删除记录。**这样可以发现不符合已知服务UUID或厂商模式的定制或改装追踪器。**

**iBeacon（+2）**：零售商、机场和体育场馆使用Apple iBeacon格式（`0x4C 0x00 0x02 0x15`）跟踪物理空间中的设备移动。无论UUID为何，只要出现标准广播格式就会触发检测。这针对的是部署类型，而非特定UUID。*检测到iBeacon通常表示所在地点正在主动跟踪蓝牙设备是否出现。*

---

### 引擎2：WiFi扫描，主动信道搜索

WiFi扫描引擎使用ESP32标准AP扫描接口枚举附近的接入点，并将其BSSID和SSID与已知监控设备特征进行比较。

#### WiFi检测表

| # | 目标 | 检测方法 | 分数 |
|---|--------|-----------------|-------|
| 12 | **Flock Safety摄像头（OUI）** | BSSID匹配Flock Safety的22项OUI表（`d4:bb:e6`、`3c:61:05`及FS-Ext-Battery前缀） | +5 🔴 |
| 13 | **ALPR / LPR摄像头（OUI）** | BSSID匹配Motorola Solutions / Vigilant Solutions的OUI `00:0e:58` | +5 🔴 |
| 14 | **包含Flock关键词的SSID** | SSID包含`flock`、`flocksafety`、`fs ext`、`penguin`或`pigvision` | +5 🔴 |
| 15 | **包含ALPR关键词的SSID** | SSID包含`alpr`、`lpr`、`vigilant`、`plateread`、`licenseplat`、`motorola`或`automate` | +4 🔴 |
| 16 | **监控摄像头厂商（OUI）** | BSSID匹配31项摄像头OUI表，包括Hikvision、Dahua、Axis、Ring、Nest、Arlo、Wyze、Reolink、FLIR、Amcrest、Vivotek、Hanwha、Mobotix和Ubiquiti UniFi | +3 🟡 |
| 17 | **包含摄像头关键词的SSID** | SSID包含`cam`、`ipcam`、`cctv`、`nvr`、`dvr`、`doorbell`、`surv`、`blink`、`lorex`、`protect`、`genetec`等 | +2 🟡 |

#### Flock Safety OUI表

包含22个条目的`FLOCK_OUIS`表是项目中最详细的查找表，包含：

- `d4:bb:e6`：IEEE注册的Flock Safety OUI。
- `3c:61:05`：IEEE注册的Flock Safety OUI。
- 另外20个在现场Flock FS-Ext-Battery电池和Flock WiFi摄像头上观察到的MAC前缀。

这22个条目代表了已部署Flock Safety ALPR摄像头系统中观察到的硬件MAC地址范围。**OUI检测独立于SSID**：即使Flock摄像头使用不含关键词的SSID，只要BSSID OUI匹配，仍会加+5分。

Flock Safety和Vigilant Solutions的OUI位于不同表中，因此两类设备可以在同一扫描周期中分别计分。*同时部署两家厂商设备的地点，一次WiFi扫描最多可能累计+10分。*

#### 监控摄像头厂商OUI表

31项监控摄像头表涵盖了可能出现在商店、商业场所和住宅中的主要IP摄像头厂商：

- **企业和商业用途**：Hikvision、Dahua、Axis、Vivotek、Hanwha（Samsung Techwin）、Mobotix和Genetec。
- **消费级和小型办公室**：Ring、Nest、Arlo、Wyze、Reolink、Blink、Lorex和Amcrest。
- **基础设施**：Ubiquiti UniFi（接入点和摄像头使用重叠的OUI范围）以及FLIR。

即使没有关键词确认，匹配也会增加+3分，进入注意等级。如果SSID关键词也匹配，同一摄像头网络会先因OUI增加+3分，再因SSID增加+2分，在一个扫描周期内达到警报等级。

---

### 引擎3：WiFi混杂模式，被动帧嗅探

混杂模式引擎将ESP32无线电切换到**监视器模式**并捕获原始802.11管理帧。这样可以检测不广播SSID的设备，尤其是通过**WiFi邻近感知网络（NaN）**使用**Remote ID**协议的无人机。

在混杂模式阶段，无线电每400 ms在`{1, 6, 11, 3, 8, 13}`之间**切换信道**，以扩大无人机NaN帧广播信道的覆盖范围。

#### 混杂模式检测表

| # | 目标 | 检测方法 | 分数 |
|---|--------|-----------------|-------|
| 18 | **无人机（OpenDroneID WiFi NaN）** | 发送至`51:6f:9a:01:00:00`的802.11管理帧：ASTM F3411 Remote ID广播 | +4 🔴 |

**OpenDroneID WiFi NaN（+4）**：ASTM F3411标准为所有Remote ID WiFi NaN帧定义了组播目的地址`51:6f:9a:01:00:00`。通过WiFi广播位置和身份的受监管商用无人机会将帧发送到此地址。Eye Spy只需监听目的MAC为此组播地址的管理帧，检测方式被动且可靠。*无人机操作员若想阻止检测，只能完全关闭Remote ID，而这本身会违反适用法规。*

此检测补充BLE OpenDroneID引擎（检测#6）。*根据硬件和配置，无人机可能通过BLE、WiFi或两者进行广播。* Eye Spy两种方式都能检测。

---

## 阶段计划与无线电管理

```
BLE被动扫描（9秒）→ WiFi扫描（约3秒）→ 混杂模式嗅探（5秒）→ 重复
```

ESP32-PICO-D4有**一台共享的2.4 GHz无线电**同时处理BLE和WiFi。Eye Spy按以下方式管理：

1. **BLE阶段**（9秒）：NimBLE协议栈运行并进行被动扫描，不发送扫描请求。
2. **停止BLE**：使用WiFi前明确停止BLE协议栈。
3. **WiFi扫描**（约3秒）：在所有信道主动扫描AP并匹配OUI与SSID。
4. **混杂模式嗅探**（5秒）：被动捕获802.11帧并切换信道。
5. **停止WiFi**：停止WiFi并重启BLE，进入下一轮循环。

这种明确的阶段管理可避免无线电冲突，并确保BLE和WiFi引擎在每个周期内有序访问无线电。

---

## 串口输出

所有输出行都以`[eyespy]`开头，便于筛选。串口监视器速率为**115200波特**。

### 启动

```
[eyespy] Eye Spy v1.1 starting
[eyespy] init OK
```

### 正常周期

```
[eyespy] BLE scan start
[eyespy] WiFi scan
[eyespy] WiFi done  score=0
[eyespy] promisc ON
[eyespy] status  score=0  CLEAR  phase=PROMISC  tracked=3
```

### 检测事件

```
[eyespy] Flock-cam OUI d4:bb:e6  "Flock_CAM_0032"
[eyespy] +5 (Flock-cam-OUI)  score=5
[eyespy] WiFi done  score=5
[eyespy] promisc ON
[eyespy] status  score=5  CAUTION  phase=PROMISC  tracked=12
[eyespy] Axon-cam  RSSI=-62
[eyespy] +5 (Axon-cam)  score=10
[eyespy] status  score=10  ALERT  phase=BLE  tracked=12
[eyespy] decay  score=9
```

`tracked=N`字段显示持续性追踪器中当前记录的唯一BLE MAC数量，有助于了解BLE环境的密集程度。

### 分数字段

每条状态行包含：

- **score**：当前威胁分数。
- **state**：`CLEAR` / `CAUTION` / `ALERT`。
- **phase**：当前活动引擎（`BLE` / `WIFI` / `PROMISC`）。
- **tracked**：持续性表中的唯一BLE MAC数量。

---

## 构建与刷写

### 要求

- **PlatformIO**（CLI或VS Code扩展）。
- **M5Stack Atom Lite**或任意ESP32 DevKit。
- USB-C线缆。

### 依赖项

PlatformIO会自动安装：

```ini
lib_deps =
    adafruit/Adafruit NeoPixel @ ^1.15.1
    h2zero/NimBLE-Arduino @ ^1.4.3
```

**Adafruit NeoPixel**用于驱动SK6812 RGB LED。**NimBLE-Arduino**提供BLE被动扫描协议栈。与ESP32默认BLE库相比，它更适合此用途，因为它能可靠支持被动扫描模式、避免发送扫描请求数据包，并且内存开销更低。

### 刷写到M5Stack Atom Lite

```bash
git clone https://github.com/simeononsecurity/eye-spy.git
cd eye-spy

# 为Atom Lite构建并刷写
pio run -e atom-lite -t upload

# 以115200波特打开串口监视器
pio device monitor -b 115200
```

### 刷写到通用ESP32 DevKit

```bash
pio run -e esp32dev -t upload
```

### 项目结构

```
eye-spy/
├── src/
│   └── main.cpp          # 全部固件逻辑
├── platformio.ini         # 构建环境（atom-lite、esp32dev）
├── partitions_4mb.csv     # 4 MB闪存分区表
└── README.md
```

### platformio.ini

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

*`atom-lite`环境使用`m5stick-c`开发板定义，两者采用相同的ESP32-PICO-D4芯片，并兼容GPIO 27 NeoPixel引脚映射。*

---

## 检测说明与实际限制

{{< figure src="eye-spy-m5stack-atom-lite-pocket-size.webp" alt="照片风格的Eye Spy与M5Stack Atom Lite插画，设备约为方糖大小，由两根手指夹住以展示其紧凑尺寸" >}}

### Eye Spy无法做到什么

**5 GHz WiFi**：ESP32是**仅支持2.4 GHz**的设备。仅在5 GHz频段运行的监控摄像头、ALPR系统或接入点不会被WiFi扫描或混杂模式引擎发现。*许多现代IP摄像头虽然也支持5 GHz，但仍兼容2.4 GHz。只运行5 GHz的部署则无法检测。*

**加密BLE**：一些高端监控产品会加密或混淆BLE广播。Eye Spy能检测以明文广播可识别特征（例如OUI、服务UUID、厂商数据）的设备。*会轮换MAC地址的设备（这是消费级追踪器日益常见的隐私功能）能够避开基于MAC的检测。* 如果其轮换间隔长于5分钟，持续性追踪器仍可能发现它们。

**有线摄像头**：**通过以太网连接且未启用WiFi无线电的IP摄像头不会发出Eye Spy能够检测的无线信号。** 不接入网络、仅在本地录像的隐藏摄像头同样不会产生RF特征。

**范围限制**：在室内，ESP32天线接收强信号的实际范围为**20–40米**，弱信号或受遮挡的信号更短。*处于覆盖边缘或被显著RF屏蔽的设备可能得不到分数，或低于−90 dBm的RSSI过滤阈值。*

### 可能出现的误报

**邻居家中的消费级摄像头**：Ring、Nest、Wyze、Arlo和Reolink摄像头在住宅区十分常见，其OUI已列入31项摄像头表。*在住宅环境中，邻居的门铃摄像头可能带来一些黄色注意提示（+3）。* 从技术角度看，这不算误报，因为设备*确实检测到了摄像头*，但需要结合环境判断。

**零售场所部署的iBeacon**：大型零售商几乎在每家门店都部署了iBeacon基础设施。*前往购物中心或超市时，很可能触发iBeacon检测（+2）。* 设备执行正常，因为零售追踪设施确实存在。

**Ubiquiti UniFi基础设施**：由于Ubiquiti生产网络设备和安全摄像头，且两者的OUI范围有重叠，UniFi接入点也会出现在监控摄像头OUI表中。*使用UniFi网络设备的部署可能在WiFi扫描中因OUI匹配得到+3分。*

**Samsung SmartTag与消费设备**：SmartTag UUID（`0xFD5A`）是Samsung注册的服务。*Samsung SmartTag是有正当个人用途的消费级追踪器。* 附近存在SmartTag时就会触发检测。

### 各分数等级在实际中的含义

| 分数 | 可能的现实情况 |
|-------|-----------------------------|
| 6–10（🔴） | 高置信度的可信检测：约30米内的Axon摄像头、OUI匹配的Flock Safety摄像头、确认存在跟随模式的AirTag，或正在广播Remote ID的无人机 |
| 3–5（🟡） | 多个消费级追踪器、邻居摄像头累积分数、可能存在Flock摄像头，或单次OpenDroneID检测 |
| 0–2（🟢） | 未发现重要监控特征；存在普通消费设备通信，但分数低于阈值 |

---

## 与相关项目的比较

Eye Spy针对环境中的物理监控；[ESP32 WiFi Canary：2.4 GHz被动威胁检测器](https://simeononsecurity.com/articles/esp32-wifi-canary-passive-wifi-threat-detection-2026/)则检测针对你自己设备的网络层WiFi攻击。*两者互为补充，针对不同的威胁模型。*

| 功能 | Eye Spy | ESP32 WiFi Canary |
|------------|---------|------------------|
| AirTag与追踪器检测 | ✅ | ❌ |
| ALPR / Flock摄像头检测 | ✅ | ❌ |
| 执法记录仪检测 | ✅ | ❌ |
| 无人机（Remote ID）检测 | ✅ | ❌ |
| 恶意双胞胎接入点检测 | ❌ | ✅ |
| 取消认证攻击检测 | ❌ | ✅ |
| 安全降级检测 | ❌ | ✅ |
| 基线学习 | ❌ | ✅ |
| 被动BLE | ✅ | ❌ |
| 相同硬件平台 | ✅ | ✅ |

两个项目都运行在相同的M5Stack Atom Lite硬件上，使用相同的LED指示灯和PlatformIO构建系统。若要兼顾物理与网络监控，可以将两个项目分别刷写到两台Atom Lite上并同时携带。

对于特别关注ALPR监控基础设施的用户，Eye Spy也可与[Flock You检测项目](https://simeononsecurity.com/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)配合使用。

---

## 使用场景

### 了解周边监控情况

Eye Spy主要面向想了解周边监控基础设施的人。无论是在街区步行、驾车经过路口，还是参加公共活动，Eye Spy都能将复杂的RF分析转化为**一个实时LED状态**。

### 检测AirTag跟踪

利用AirTag跟踪他人是有记录的问题。Eye Spy的**跟随设备检测引擎**会查找在至少5分钟内出现至少3次的未知持续性BLE MAC，目标是发现不符合Apple已知广播格式的定制或改装追踪器。结合直接的AirTag检测，它提供了**两条独立路径来发现跟随你的追踪器**。

### 检查出租房或酒店客房

进入新的酒店房间或出租房并运行Eye Spy，可初步识别意料之外的BLE和WiFi设备。WiFi扫描若发现包含摄像头关键词的SSID或监控OUI，就会增加注意等级分数。*这不能替代正规的RF扫描*，但能为物理检查增加一层被动环境监测。

### ALPR部署与隐私研究

记录监控基础设施的研究人员、在受监控环境中工作的记者，以及隐私倡导者，可以使用价格低廉、便于携带的Eye Spy进行现场检测。串口输出会记录每项检测及其RSSI，因此也适合简单的数据采集。

### 旅行安全

和WiFi Canary一样，Eye Spy采用便于旅行的外形。Atom Lite可放入口袋或挂在包上。在机场、火车站或监控密集的公共活动场所，它无需交互即可持续进行被动监测。

---

## 架构说明

### 被动BLE为何重要

选择不发送扫描请求包的BLE被动扫描方式具有重要安全意义。在标准BLE扫描中，扫描器会发送**SCAN_REQ**数据包，向每个广播设备请求额外广告数据。*因此，BLE主动扫描对双方都可见*，被扫描设备能从请求中看到扫描器的地址。

NimBLE被动模式只监听非定向广播包（ADV_IND、ADV_NONCONN_IND、ADV_SCAN_IND），从不发送SCAN_REQ。**Eye Spy在扫描阶段不会通过BLE发射任何内容。** 被检测到的Axon执法记录仪、Flock设备或AirTag无法观察扫描器，也无法对它的存在作出响应。

### 持续性追踪器设计

未知设备持续性追踪器最多保存**50个BLE MAC地址**及首次和末次检测时间。当同一个MAC在至少五分钟内出现三次或更多次时，就会触发检测。

50项上限和30分钟清除窗口是在检测灵敏度与ESP32 RAM限制之间进行平衡的工程选择。*在公交、会议或商场等BLE设备密集环境中，表格可能很快被消费设备填满。* −90 dBm的RSSI阈值会过滤远处设备，使追踪器重点关注附近持续存在的信号源。

### 分数衰减与冷却时间的交互

**120秒的重新计分冷却时间**可防止始终处于范围内的设备在每个9秒BLE周期不断累积分数。若没有冷却时间，单个Flock摄像头会每15秒增加+5分，几分钟内就能达到数百分。

**每60秒降低1分**意味着设备离开范围且冷却时间结束后，只要未再次触发，分数就会下降。*一次没有再次触发的+5分检测会在5分钟内降至零。* 这样，在正常移动场景中，设备会自然恢复到无警报状态。

---

## 贡献与项目状态

Eye Spy以Apache-2.0许可证发布，地址为[github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)。

可能的扩展方向包括：

- **添加OUI条目**：在现场记录到新的硬件MAC后，扩展Flock Safety和摄像头OUI表。
- **添加BLE服务UUID**：新款智能眼镜、摄像头或追踪器会带来新的UUID。
- **调整持续性追踪器**：50项上限、3次观测阈值和5分钟窗口都是可调整常量。
- **记录串行数据**：串口输出格式适合程序解析。外部记录器可汇总多台Eye Spy的检测事件。

固件位于`src/`目录下的单个`main.cpp`文件中，因此易于阅读、审查和修改。

---

## 结论

Eye Spy解决了一个范围有限但重要的问题：你周围的物理环境安装了越来越多的监控设备，其中大多数会广播可检测的RF特征。**一台售价15美元、运行Eye Spy固件的M5Stack Atom Lite可以成为持续工作的环境扫描器**，将复杂的BLE数据包分析和WiFi OUI查询转化为一个RGB LED信号。

置信度评分模型反映了实际威胁权重：执法活动附近的Axon执法记录仪加+5并立即点亮红灯；零售iBeacon加+2，有助于了解情况，但不会单独触发误报。分数衰减和再计分冷却机制可避免设备对短暂或低等级的持续信号反应过度。

无论是进行反监控、旅行安全、AirTag检测，还是单纯想了解附近是否有设备在观察你，Eye Spy都是一款实用、开源且被动运行的工具，值得安全从业者纳入装备。

**GitHub**: [github.com/simeononsecurity/eye-spy](https://github.com/simeononsecurity/eye-spy)

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  购买Eye Spy检测器，节省20%
{{< /centerbutton >}}
