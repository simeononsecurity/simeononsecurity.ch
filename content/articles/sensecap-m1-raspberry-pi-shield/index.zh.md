---
title: "SenseCAP M1 Raspberry Pi Shield：引脚图与 LoRaWAN 再利用"
date: 2026-09-12
lastmod: 2026-11-07
toc: true
draft: false
description: "了解 SenseCAP M1 shield，比较相互冲突的 GPIO 映射，检查 ATECC608，并使用新版 Raspberry Pi OS 规划 LoRaWAN 网关。"
genre: ["Raspberry Pi", "IoT", "硬件安全"]
tags: ["SenseCAP M1", "SenseCAP M1 shield", "SenseCAP M1 引脚图", "Raspberry Pi shield", "Raspberry Pi HAT", "LoRaWAN 网关", "WM1302", "WM1303", "SX1302", "SX1303", "Seeed Studio", "Helium hotspot 再利用", "LoRa 集中器", "SPI GPIO", "GPIO17", "GPIO22 LED", "libgpiod", "Raspberry Pi OS", "ATECC608", "CryptoAuthLib", "I2C 诊断", "STTS751", "LoRa Basics Station", "ChirpStack", "The Things Stack", "硬件逆向工程"]
cover: "/img/cover/sensecap-wm1302-shield-hardware.webp"
coverAlt: "SenseCAP M1 shield，配有 Seeed WM1302 模块、Raspberry Pi 排针、天线线缆、USB-C 插座和风扇接口"
coverCaption: "电路板照片：Clockwork Bird，2023 年。来源和署名见文末。"
coverCredit: "Clockwork Bird"
coverCreditURL: "https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/"
---

**SenseCAP M1 shield 可用作 LoRaWAN 网关硬件，但其布线需要比通用 Raspberry Pi HAT 教程更仔细的检查。** 本指南在 [Clockwork Bird 2023 年的调查](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)基础上，补充了制造商文档、上游驱动检查和当前 GPIO 指引。你将识别硬件，区分已确认事实和不完整的引脚图证据，并建立可重复的启动记录。

> **范围：** 这是基于文档的硬件指南。本文中的命令和板卡映射没有在实体 M1 上测试。

## 要点

- **识别两块板：** M1 载板和可拆卸集中器有各自的型号与修订信息。
- **审查复位脚本：** CoreCell 默认值与已发布 M1 引脚图中的一些信号冲突。
- **检查系统接口：** SPI 设备文件、GPIO 编号和 GPIO 工具版本回答不同问题。
- **保护安全元件配置：** 读取设备信息与配置设备或生成密钥不是同一操作。
- **验证完整链路：** 检测到集中器不代表传感器数据已送达。

## 开始前

**难度：中级。** 盘点设备、准备系统和检查文档约需一到两小时。电气验证、驱动适配和网络服务器部署还需要额外工作，尤其是在板卡修订未知时。

| 项目 | 用途 |
|---|---|
| **M1 shield 和集中器** | 读取载板修订信息和模块完整标签 |
| **Raspberry Pi 4** | 从原 M1 设计使用的主机开始 |
| **备用 microSD 卡** | 保留原安装，同时准备单独的操作系统 |
| **合适的电源和天线** | 匹配组装硬件和模块的 RF 频段 |
| **SSH 或本地控制台** | 记录诊断信息并编辑配置 |
| **LoRaWAN 传感器和服务器** | 硬件启动后验证应用数据是否实际送达 |
| **万用表和硬件经验** | 驱动未知连接前先查明情况 |

拆卸前，给断电状态下的组装件两面拍照。记录连接器方向、螺丝、垫片和天线路径。在新安装通过验收检查前，保留原卡和配置。

## 识别三个层次

**完整 M1、载板 shield 和集中器是不同组件。** Seeed 将完整热点描述为 Raspberry Pi 4 搭配 WM1302/SX1302 或 WM1303/SX1303 集中器。标题写着“SenseCAP M1 shield”的商品信息无法说明载板附带哪种组件。[Seeed Studio 的 M1 概览](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

**载板**在 Pi 和模块之间连接电源与外围信号。**集中器**负责无线接收和发射。主机上的**数据包转发器**与服务器交换接收的无线数据包和已安排的下行数据。[Semtech 的 SX1302 HAL 概览](https://github.com/Lora-net/sx1302_hal)

例如，货架温度传感器通过无线发送上行数据。集中器接收，主机转发，网络和应用服务再处理。Linux 成功启动只能证明这条链路中的主机部分。

Clockwork Bird 的照片展示了 M1 v1.1 载板，上面装有明确标注为 `WM1302-SPI-EU868` 的模块。用照片查找自己硬件上的标签。序列号标识照片中的设备，不是其他网关的配置值。

{{< figure src="m1-carrier-wm1302-board.webp" alt="绿色 M1 载板上装有带标签的 WM1302 SPI EU868 模块，旁边有 USB-C、按钮、风扇插座和天线线缆" caption="Clockwork Bird 拍摄的 M1 v1.1 硬件，也用于本文封面" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## 电源和无线连接

**将 M1 的 USB-C 接口视为电源输入。** 制造商为整台网关指定 DC 5 V、3 A，并将 USB-C 定义为电源接口。称其为充电口会让人误以为设备有电池，而这些规格没有提到电池。[SenseCAP M1 规格](https://www.sensecapmx.com/docs/sensecap-m1/overview/)

制造商框图将 5 V 电源与模块的稳压 3.3 V 电源轨分开。排查问题时，这一区别很重要：Pi 运行时，集中器仍可能没有供电。不要向信号引脚注入 5 V，也不要假设两个电源输入彼此隔离。

**SPI 和 USB 模块变体需要不同的主机连接。** Seeed 的 WM1302 文档说明，SPI 型号直接使用 SPI，USB 型号使用 STM32L4 USB bridge。mini-PCIe 外形描述模块形态，文档中列出的电气接口则是 SPI 或 USB。形状适合笔记本插槽不足以证明兼容。[Seeed 的 WM1302 文档](https://github.com/seeed-lora/WM1302-doc)

给组装件上电前，先断电安装模块并连接合适的天线。确保 RF 硬件、天线和计划使用的区域频段一致。更改配置文件名不会改变 RF 元件，M1 电源接口也无法证明它支持 USB 集中器变体。

{{< figure src="m1-power-spi-system-diagram.webp" alt="通过电源、SPI、GPIO 和 I2C 总线连接 Raspberry Pi 4 与 M1 shield 的框图" caption="Clockwork Bird 原文转载的 SenseCAP 制造商框图，展示 WM1302 设计" credit="Seeed Studio / SenseCAP, via Clockwork Bird" attr="Seeed Studio / SenseCAP, via Clockwork Bird" attrlink="https://www.sensecapmx.com/docs/sensecap-m1/overview/" >}}

## 仔细读取引脚图

**在记录中将 BCM GPIO 编号和排针物理编号分成两列。** 例如，BCM GPIO17 对应 Pi 排针的物理 11 号脚。模块边缘连接器采用第三种编号体系，因此它的复位脚编号不是 Raspberry Pi GPIO 编号。

下表转录了 Clockwork Bird 标注的排针图片中的连接。它是**社区参考资料**，不是制造商发布的完整原理图，也不是对所有 M1 修订版的测量。图中还使用 `SX1262` 标签，而 Semtech 通用复位脚本使用 `SX1261` 名称。

| 图中的信号 | BCM / 物理引脚 | 解释 |
|---|---|---|
| **I2C SDA / SCL** | GPIO2 / 3、GPIO3 / 5 | 共享管理总线 |
| **SX1302 复位** | GPIO17 / 11 | 集中器复位候选引脚 |
| **用户 LED** | GPIO22 / 15 | M1 标注 |
| **SPI MOSI / MISO** | GPIO10 / 19、GPIO9 / 21 | SPI 数据信号 |
| **SPI 时钟** | GPIO11 / 23 | SPI 时钟信号 |
| **SX1302 片选** | GPIO8 / 24 | SPI0 CE0 |
| **SX1262 复位** | GPIO5 / 29 | 辅助无线复位候选引脚 |
| **SX1262 片选** | GPIO6 / 31 | GPIO6，与 SPI0 CE1 不同 |
| **SX1262 BUSY** | GPIO18 / 12 | 辅助无线状态输出 |
| **SX1262 IO1 / IO2** | GPIO23 / 16、GPIO24 / 18 | 使用前应验证的辅助信号 |

划掉的 GPS/UART 标注不能证明 M1 配有 GPS。如果你的设备没有 GPS，就不要添加 GPS 专用配置。已发布的图也没有说明用户按钮和风扇控制方式。[Clockwork Bird 的引脚图调查](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)

{{< figure src="m1-community-header-pinout.webp" alt="标注的 Raspberry Pi 排针图，显示 M1 LED、集中器复位、SPI 信号和划掉的 GPS 连接" caption="社区标注参考，修订版覆盖不完整，不是完整的 M1 原理图" credit="Clockwork Bird" attr="Clockwork Bird, 2023-05-03" attrlink="https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/" >}}

## 解决复位脚本冲突

**复位脚本选择的是电气输出，不只是软件偏好。** Semtech 上游的 `reset_lgw.sh` 面向 CoreCell 参考设计。默认值包括：集中器复位 GPIO23、电源使能 GPIO18、辅助复位 GPIO22，以及 AD5338R 复位 GPIO13。[Semtech 复位脚本源代码](https://github.com/Lora-net/sx1302_hal/blob/master/tools/reset_lgw.sh)

Seeed 的旧版设置说明将两个复位分配改为 GPIO17 和 GPIO5，但保留了参考设计的其他项目。照着示例操作前，先将这些值与 M1 标注图比较。[Seeed WM1302 设置说明](https://github.com/seeed-lora/WM1302-doc)

| 分配 | 冲突证据 | 需要做出的决定 |
|---|---|---|
| **GPIO22 作为辅助复位** | M1 图将它标为用户 LED | 启用 LED 前移除这一假设 |
| **GPIO18 作为电源使能** | M1 图将它标为辅助 BUSY | 驱动前确认网络和信号方向 |
| **GPIO13 作为 DAC 复位** | 通用脚本名称指向另一个参考设计 | 确认电路是否存在 |
| **辅助 SPI 设备** | M1 图选择 GPIO6，而非 CE1 | 确认片选走线和驱动支持 |

**推断：** 如果 GPIO18 按图连接到辅助无线输出，将 Pi 端配置为输出会产生电气争用风险。这一分歧说明需要验证，但不能证明发生了损坏，也不能证明所有 M1 都采用相同布线。

断开所有电源后，追踪排针与模块连接器之间可接触的线路。记录板卡修订版和线路两端。导通结果证明存在连接，信号方向和电气限制则要查阅组件文档。

使用下方的模块图，避免将边缘连接器引脚与 Pi 排针引脚混淆。辅助无线标签描述的是已发布的模块参考设计，不能证明各修订版采用相同芯片或支持相同功能。[Seeed WM1302 模块引脚图](https://github.com/seeed-lora/WM1302-doc/blob/master/pinout.jpg)

{{< figure src="wm1302-module-edge-connector.webp" alt="Seeed 图示 WM1302 模块边缘连接器两侧的电源、SPI、I2C 和辅助无线信号" caption="模块边缘连接器编号不同于 Raspberry Pi 排针编号" credit="Seeed Studio" attr="Seeed Studio, WM1302-doc" attrlink="https://github.com/seeed-lora/WM1302-doc" >}}

## 准备 Raspberry Pi OS

在备用系统中记录主机环境：

```bash
cat /etc/os-release
uname -r
tr -d '\0' < /proc/device-tree/model
```

系统版本、内核和 Pi 型号构成可复现的起点。与旧教程比较结果前，先记录这些信息。

安装检查和构建工具：

```bash
sudo apt update
sudo apt install git build-essential i2c-tools gpiod
sudo raspi-config
```

在 **Interface Options** 中启用 SPI 和 I2C，然后重启。SPI 用于集中器链路，I2C 用于后文介绍的管理设备。不要从其他 HAT 教程中照搬无关的 GPS 串口改动。

检查已公开的接口：

```bash
ls -l /dev/spidev* /dev/i2c-*
i2cdetect -l
gpiodetect
gpioinfo
gpioset --version
```

这些命令会列出设备节点、适配器、GPIO 控制器、线路和已安装 GPIO 工具的版本。**`i2cdetect -l` 只列出适配器，不扫描地址。** `/dev/spidev0.0` 文件证明 SPI 接口已公开，不能证明它与正常工作的集中器通信。[i2c-tools 手册](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)、[Raspberry Pi GPIO 指引](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

### 考虑 GPIO 版本

**不要复制其他机器的全局 GPIO 编号。** 旧脚本通过 `/sys/class/gpio` 操作，这是内核文档已弃用的接口。新的用户空间集成应使用 GPIO character device 接口，并选择正确的控制器和线路偏移。[Linux GPIO 文档](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)

改编脚本前也要检查 `gpioset --help`。版本 1 和版本 2 的语法及进程行为不同。当前工具默认保持所请求的线路，但可移植的接口约定不保证进程退出后的线路状态。[libgpiod gpioset 文档](https://libgpiod.readthedocs.io/en/master/gpioset.html)

Raspberry Pi 文档说明了内核中的输出保持行为，并提供更改选项。记录实际内核配置，不要假设所有 Linux 系统行为相同。更新编号或换用新版 GPIO 工具都不能修复错误的电气映射。[Raspberry Pi GPIO 使用指南](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)

## 测试用户 LED

确认 GPIO22 连接到 LED，并移除冲突的 GPIO 使用者后，编辑启动配置：

```bash
sudoedit /boot/firmware/config.txt
```

新版 Raspberry Pi OS 将启动配置挂载在 **`/boot/firmware/config.txt`**。旧版镜像使用 2023 年文章中的路径 `/boot/config.txt`。编辑前备份当前生效的文件。[Raspberry Pi config.txt 文档](https://www.raspberrypi.com/documentation/computers/config_txt.html)

在适用于 Pi 的段落下添加 LED overlay，例如 `[all]`：

```ini
dtoverlay=gpio-led,gpio=22,label=lorawan,trigger=heartbeat
```

**`gpio`** 参数使用 BCM 编号。**`label`** 为 Linux LED 设备命名，**`trigger=heartbeat`** 则指定内核 heartbeat 触发器。Clockwork Bird 报告 M1 使用此分配，Raspberry Pi overlay 参考文档也说明了这些参数。[原始 LED 观察](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)、[gpio-led overlay 参考](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README)

重启后检查已注册的 LED：

```bash
ls -l /sys/class/leds/
cat /sys/class/leds/lorawan/trigger
```

预期结果是出现 `lorawan` LED 项，并且 `[heartbeat]` 为选中状态。LED 闪烁说明 GPIO/驱动链路正常，但不能说明 LoRaWAN 已注册、无线已接收或 Helium 状态正常。

## 检查 I2C 设备

**I2C 地址是线索，不是设备身份。** Clockwork Bird 观察到 `0x60` 和 `0x39` 有响应，随后通过加密库读取 ATECC608 信息。原文对温度传感器的识别仍是暂定结论。

从前一节的适配器列表开始。广泛的 `i2cdetect` 扫描会发送探测事务，而非被动观察总线；上游手册还警告它可能造成干扰。不要定期扫描正在运行的网关或未知外接设备。[i2c-tools 探测行为](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)

| 观察 | 有证据支持的结论 | 未解决的问题 |
|---|---|---|
| **`0x60` 有响应** | 某个设备确认了探测 | 它是预期的安全元件吗？ |
| **`0x39` 有响应** | 某个设备确认了探测 | 哪个组件和修订版响应？ |
| **扫描结果为 `UU`** | 地址由驱动占用，因此跳过了探测 | 哪个驱动占用了地址？ |
| **没有响应** | 探测没有收到确认 | 是电源、总线、占用还是设备协议问题？ |

### 进一步确认温度传感器线索

**STTS751 是有来源支持的 `0x39` 候选设备。** Semtech 温度驱动头文件明确将 `0x39` 与 `STTS751-0DP3F` 关联。这增强了原文假设，但不能识别所有使用该地址的板卡元件。[Semtech STTS751 驱动头文件](https://github.com/Lora-net/sx1302_hal/blob/master/libloragw/inc/loragw_stts751.h)

确认组件兼容，并确认没有其他进程占用后，读取其识别寄存器：

```bash
sudo i2cget 1 0x39 0xfd b
sudo i2cget 1 0x39 0xfe b
```

这里，**`1`** 选择已验证的总线，**`0x39`** 选择设备，**`b`** 请求 SMBus byte-data 读取。对于 STTS751-0，文档指出 `0xFD` 处的产品 ID 为 `0x00`，`0xFE` 处的制造商 ID 为 `0x53`。这些事务选择寄存器地址，不会写入配置值。[STTS751 数据手册，寄存器映射与识别寄存器](https://www.st.com/resource/en/datasheet/stts751.pdf)

将读数与芯片标记和文档比较。两个值匹配会增加识别依据；如有错误，应先检查总线和占用情况，再更改硬件配置。该传感器测量自身附近的温度，与 Pi CPU 温度不同。

## 检查安全元件

**ATECC608 是独立的身份验证组件。** 将其配置、序列号、公钥和受保护密钥材料视为不同概念。读取公钥不会泄露对应的私钥。

Microchip 的 **CryptoAuthLib** 提供设备接口。**cryptoauthtools** 仓库包含基于该库的示例。运行示例前，按这两个项目的说明为目标系统准备原生库和 Python bindings。安装无关的 Python 包或只复制一个脚本，都不能证明 I2C 后端已正常工作。[Microchip CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib)、[Microchip cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)

在准备好的 `cryptoauthtools/python/examples` 目录中运行原文的检查命令：

```bash
sudo python3 info.py -i i2c
```

**`-i i2c`** 参数用于选择接口。在虚拟环境中，使用该环境明确指定的 Python 解释器，并确保它能找到匹配的原生库。很多安装环境下，`sudo python3` 会选择系统解释器，这也是部分模块导入错误的原因。

经过检查的 `info.py` 会读取修订信息、序列号、配置和锁定状态。如果数据区已锁定，它会尝试读取 slot 0 的公钥。该脚本不会运行示例中的配置流程。仅 slot 0 公钥读取失败，不能证明设备损坏。[Microchip info.py 源代码](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/info.py)

| 输出或操作 | 含义 |
|---|---|
| **Configuration locked** | 配置限制已生效 |
| **Data zone locked** | 按已配置的 slot 策略解释访问权限 |
| **显示公钥** | 已读取公开信息，不是导出私钥 |
| **运行 `config.py`** | 包含配置、锁定和密钥生成操作的 provision 示例 |

**不要运行 `config.py` 来修复检查错误。** 源码包含配置写入、锁定区域和生成密钥的调用。对于已配置设备，其默认密钥生成路径也需要考虑。[Microchip config.py 源代码](https://github.com/MicrochipTech/cryptoauthtools/blob/master/python/examples/config.py)

Microchip 的 provision 配置文件说明，锁定数据区不代表每个 slot 都有相同的访问权限。这些配置文件不能证明 M1 的具体设置。保留现有配置；计划复用密钥前，先查阅对应器件的文档。[Microchip 内存和 slot 访问策略](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html)

## 查明风扇和按钮的未知信息

**三针风扇接口不能说明它的电压、极性或控制方式。** 拍下引脚编号并读取风扇标签。接入替换风扇或选择 GPIO overlay 前，先确认电源和控制连接。

原调查也没有确定按钮的 GPIO。查找适用于当前板卡修订版的驱动或配置，然后在断电状态下验证连通性。不要将所有看似空闲的 GPIO 设为输出，以此寻找按钮。

| 外设 | 需要收集的证据 | 验收条件 |
|---|---|---|
| **风扇电源** | 风扇额定值、接口地线和供电 | 测得电源符合风扇规格 |
| **风扇控制** | 驱动/配置或已追踪的控制电路 | 启动和高温时的行为明确 |
| **用户按钮** | 触点布线、GPIO 映射、输入极性 | 有意按下一次会产生预期事件 |

新安装的操作系统不会自动恢复原设备的散热策略。首次长时间测试时，同时观察风扇和温度。保持机箱气流通道畅通，若组装件失去必要散热就停止测试。

## 选择网关软件栈

**将板卡支持与服务器协议分开考虑。** 兼容的 LoRaWAN 服务器无法修复错误的复位流程或 RF 校准。先选择支持该集中器、载板布线、操作系统和区域配置的软件。

| 软件路径 | 用途 | 部署前检查 |
|---|---|---|
| **Semtech SX1302 HAL** | 源码级启动和诊断工具 | 板卡复位流程与模块配置 |
| **LoRa Basics Station** | 网关与服务器之间的身份验证连接 | 可用的板卡集成和服务器凭证 |
| **ChirpStack Concentratord** | 专用集中器服务 | 支持的型号、校准和 GPIO 映射 |

ChirpStack 列出了 SPI **`seeed_wm1302`** 型号。这证明模块受支持，但不代表有完整 M1 镜像，也不保证支持每个 M1 修订版。不要把单独的 SenseCAP M2 安装说明当成 M1 固件说明。[ChirpStack 硬件支持](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html)、[ChirpStack Seeed 安装目标](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html)

对于 The Things Stack，其文档推荐使用 **LoRa Basics Station**，而非旧版 Semtech UDP 转发器。Station 提供 TLS、令牌身份验证和集中配置功能。现有 UDP 示例有助于理解数据包转发，但服务器地址设置不提供这些保护。[The Things Stack UDP 指引](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)、[LoRa Basics Station 文档](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)

### 准备上游工具

在目标 Pi 的新工作目录中构建：

```bash
git clone https://github.com/Lora-net/sx1302_hal.git
cd sx1302_hal
git rev-parse HEAD
make
```

将 commit ID 与构建输出一起保存。构建成功只说明与编译器兼容；无线功能还需要经过验证的复位实现和正确配置。Semtech 文档说明了 HAL 和辅助程序的作用。[SX1302 HAL 构建和工具文档](https://github.com/Lora-net/sx1302_hal)

运行硬件访问工具前先检查复位文件：

```bash
sed -n '1,180p' tools/reset_lgw.sh
```

不要未经修改就把该文件复制到运行目录。Semtech 文档指出，其硬件访问程序（包括识别工具）可能自动调用复位脚本。检查时应涵盖所有分配的引脚、信号方向、GPIO API、启动和关闭状态。

验证板卡后，按照选定软件栈的说明读取集中器 EUI 并注册网关。添加服务器配置时，保留模块校准和 RF 设置。在 Semtech UDP 配置中，`gateway_ID` 表示 EUI；The Things Stack 控制台中的 Gateway ID 是用于注册的可读名称。[The Things Stack 网关配置](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)

## 验证传感器数据送达

**分阶段收集证据，以定位第一个故障层。** 网关显示在线只能证明它连接了服务器。验收测试还需要一个已知传感器、匹配的频率计划和已解码的应用数据。

以下是建议的测试顺序，不是 M1 实测结果：

| 检查点 | 保存的证据 | 含义 |
|---|---|---|
| **主机就绪** | 系统、内核、电源和接口清单 | Linux 准备完成 |
| **集中器响应** | EUI 和初始化成功日志 | 主机与集中器通信正常 |
| **无线接收** | 预期传感器数据包和接收元数据 | 配置的接收链路正常 |
| **服务器接受** | 与传感器相关的网关事件 | 转发和服务器路由正常 |
| **应用解码** | 预期测量值和时间戳 | 应用链路正常 |
| **重启恢复** | 重启后的相同检查 | 启动配置可重复 |

对于 **OTAA** 传感器，还要确认激活交换和后续上行。OTAA 是 over-the-air activation（空中激活），即建立会话的入网过程。收到入网请求不等于入网成功，也不能证明下行链路正常。[The Things Stack 激活文档](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/)

**诊断示例：** 网关已连接服务器并报告 EUI，但传感器没有出现。优先检查传感器发送配置、选定接收信道、天线路径和无线日志。在这种情况下重新编程 ATECC608 不会补上缺失的证据。

**另一个诊断示例：** 传感器数据包在本地出现，却没有到达应用。将数据包时间与网关、服务器事件对照，再检查路由、设备注册和解码。服务器接受事件之前，仅凭日志中的 RF 数据包不足以认定是 payload 解码器的问题。

## 按症状排查

| 症状 | 先检查 | 下一步 |
|---|---|---|
| **没有 SPI 设备文件** | 当前启动配置和接口设置 | 启用目标接口并重启 |
| **SPI 存在，无线失败** | 电源、插接、复位顺序和片选 | 更改服务器前先验证电气链路 |
| **GPIO export 错误** | 旧 sysfs 假设和已安装内核 | 使用针对 GPIO API 审查过的实现 |
| **GPIO 已占用** | `gpioinfo` 显示的使用者 | 重试前先解决占用关系 |
| **设置后 LED 不工作** | overlay 是否应用和 GPIO22 冲突 | 检查已注册 LED 设备和复位脚本 |
| **I2C 设备缺失** | 总线编号、电源和现有占用 | 避免反复大范围扫描，继续调查 |
| **加密库导入失败** | 解释器、bindings 和原生库路径 | 修复软件环境 |
| **公钥读取失败** | slot 策略和之前成功的读取 | 不做 provision，先检查配置 |
| **风扇不转** | 已验证电源和散热控制实现 | 长时间测试前恢复散热 |
| **上行到达但入网失败** | 下行链路和区域/设备设置 | 追踪入网响应和接收窗口 |

每次只把一个修复作为一次实验。保存旧配置，只更改一个变量，重复同一项检查，并记录预期证据是否出现。

## 创建硬件记录

使用此模板，将调查结果整理成可重复交接的记录：

```text
载板修订版和照片：
集中器型号、接口和 RF 频段：
主机型号 / OS / 内核 / GPIO 工具版本：
电源 / 天线 / 散热布置：
已验证的引脚映射和证据：
未解决线路和排除的功能：
软件仓库和 commit：
复位实现和 GPIO 占用者：
网关 EUI / 服务器 / 频率计划：
传感器激活和已解码上行证据：
重启恢复结果：
原卡位置和回滚流程：
```

**决策练习：** 你有一个价格低但没有模块标签的裸载板，以及一个价格较高、标签清晰且运行情况有文档记录的组装件。比较时还要计入缺少的 Pi、集中器、天线、电源和验证时间，再决定哪种适合项目。更好的选择取决于总成本和目标服务所需的证据，而非载板标价。

**预期思路：** 如果有测量工具和时间，学习项目可以接受未解决的布线问题。为运行中的传感器提供服务的网关则需要可重复启动、有效散热、软件支持和已验证的数据送达。记录哪项未解决条件会阻止部署。

## 后续步骤

先完成硬件记录并解决复位脚本差异。然后启动一个已知传感器，在增加更多设备前保存从接收直到应用解码的证据。

**验收记录：** 保存板卡修订版、模块标签、无线频段、电源测量值、活动 SPI 设备、GPIO 线路名称、复位顺序、集中器日志、服务器连接和一条已解码上行。将每个值标注为“已观察”“有文档依据”或“仍是假设”。进程启动成功不能证明 RF 性能或应用数据已送达。

如果你的目标是 mesh 消息传递，先阅读我们的 [Meshtastic、MeshCore 和 Reticulum 对比指南](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)，了解这些协议的角色。使用相同 LoRa 无线技术不代表固件兼容。部署消息系统时，请查阅 [MeshtasticD 支持的硬件文档](https://meshtastic.org/docs/meshtasticd/)，不要将此 LoRaWAN 流程视为 Meshtastic 转换方法。

## 来源和图片署名

研究核查日期：2026 年 9 月 12 日。没有日期的文档和仓库链接指向本文审阅的版本。本地图片保留原始标签和来源署名。

| 发布方 | 来源和日期 |
|---|---|
| **Clockwork Bird** | [SenseCAP M1 Raspberry Pi Shield](https://clockworkbird9.wordpress.com/2023/05/03/sensecap-m1-raspberry-pi-shield/)，2023-05-03。板卡照片、标注的排针和转载的制造商框图 |
| **Seeed Studio / SenseCAP** | [M1 概览和规格](https://www.sensecapmx.com/docs/sensecap-m1/overview/)，无日期。原始框图署名 |
| **Seeed Studio** | [WM1302 文档和模块引脚图](https://github.com/seeed-lora/WM1302-doc)，仓库 |
| **Semtech** | [SX1302/SX1303 HAL](https://github.com/Lora-net/sx1302_hal)，包括链接的复位脚本和温度驱动源代码 |
| **Raspberry Pi** | [启动配置](https://www.raspberrypi.com/documentation/computers/config_txt.html)、[GPIO 使用指南](https://pip-assets.raspberrypi.com/categories/685-app-notes-guides-whitepapers/documents/RP-006553-WP/A-history-of-GPIO-usage-on-Raspberry-Pi-devices-and-current-best-practices)和 [overlay 参考](https://github.com/raspberrypi/linux/blob/rpi-6.12.y/arch/arm/boot/dts/overlays/README) |
| **Linux / libgpiod** | [已弃用的 GPIO sysfs 接口](https://www.kernel.org/doc/html/next/admin-guide/gpio/sysfs.html)和 [gpioset 手册](https://libgpiod.readthedocs.io/en/master/gpioset.html)，后者发布于 2026 年 8 月 |
| **i2c-tools** | [i2cdetect 手册](https://kernel.googlesource.com/pub/scm/utils/i2c-tools/i2c-tools/+/refs/tags/v4.3/tools/i2cdetect.8)，v4.3 源码 |
| **STMicroelectronics** | [STTS751 数据手册](https://www.st.com/resource/en/datasheet/stts751.pdf)，修订版 7 |
| **Microchip** | [CryptoAuthLib](https://github.com/MicrochipTech/cryptoauthlib)、[cryptoauthtools](https://github.com/MicrochipTech/cryptoauthtools)和 [slot 访问策略文档](https://onlinedocs.microchip.com/oxy/GUID-8F01540E-14A9-479E-9D27-FFFB14DE474E-en-US-2/GUID-92031846-201F-42DA-831D-FA3B6CF79B9B.html) |
| **ChirpStack** | [Concentratord 硬件支持](https://www.chirpstack.io/docs/chirpstack-concentratord/hardware-support.html)和 [Seeed 安装目标](https://www.chirpstack.io/docs/chirpstack-gateway-os/install/seeed.html) |
| **The Things Industries** | [UDP 转发器](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/udp/)、[LoRa Basics Station](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/)和 [设备激活](https://www.thethingsindustries.com/docs/hardware/devices/concepts/abp-vs-otaa/) |
| **Meshtastic** | [MeshtasticD 文档](https://meshtastic.org/docs/meshtasticd/)，无日期 |
