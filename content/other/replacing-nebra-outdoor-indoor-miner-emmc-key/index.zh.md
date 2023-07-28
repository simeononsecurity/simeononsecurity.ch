---
title: "更换 Nebra Helium Miner SD 卡：分步指南"
draft: false
toc: true
date: 2022-02-13
description: "通过本指南了解如何更换或重新刷新 Nebra 室内和室外版、第一代和第二代 EMMC Key SD 卡，并修复 Helium Miner 同步问题。"
genre: ["技术", "加密货币", "硬件", "氦气开采", "故障排除", "更换 SD 卡", "同步问题", "树莓派", "Balena Etcher", "Nebra 氦气采矿机"]
tags: ["Nebra 氦气采矿机", "更换 SD 卡", "同步问题", "氦气开采", "故障排除", "树莓派", "Balena Etcher", "硬件指南", "SD 卡升级", "解决同步问题", "分步指南", "氦气矿工同步修复", "Nebra 室内采矿机", "Nebra 户外采矿机", "树莓派计算模块 3", "Balena Raspberry Pi CM3 图像", "氦气矿工的故障排除", "内布拉采矿设备公司", "Balena Etcher 软件", "更换 Nebra 矿工机上的 EMMC 密钥", "氦气矿工的 SD 卡修复", "修复氦气矿工同步问题", "更换 Nebra Miner SD 卡", "Nebra 氦气开采器故障排除指南", "氦气开采技巧", "升级 Nebra Helium Miner SD 卡", "如何重新映像 Nebra Miner SD 卡", "解决 Nebra Helium Miner 同步问题"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_holding_a_Nebra_Helium_M.png"
coverAlt: "这是一幅卡通插图，描绘了一个手持 Nebra Helium Miner 的人，打开的面板上显示出 SD 卡插槽，指南的步骤以指南的形式浮现在设备上方。"
coverCaption: "轻松解决同步问题并升级您的氦气矿工机。"
---

**更换和重新映像 Nebra 室内和室外 EMMC 密钥/SD 卡**

本综合指南将指导您完成更换或重新刷新 Nebra 室内和室外 EMMC 密钥/SD 卡的过程。按照这些步骤，您可以解决 Helium Miner 的同步问题，并确保顺利运行。本指南详细说明了您需要的工具和软件，以及获取 config.json 文件、使用 Balena Raspberry Pi CM3 Image 闪存新 SD 卡和将原始配置文件传输到新 SD 卡的必要步骤。

### 简介

Nebra 氦气矿机上的室内和室外型号都依靠 EMMC 密钥/SD 卡运行。随着时间的推移，可能需要更换或重新刷新该卡，以解决同步问题并保持最佳性能。本指南将为您提供有效执行此任务所需的知识和说明。

要成功更换 Nebra Helium Miner 的 SD 卡，您需要特定的工具和软件。工具包括十字头螺丝刀或 [Allen Key Set](https://amzn.to/34SlnOS) (depending on the model), a [Micro SD Card Reader](https://amzn.to/3Jl3U0w), a [64GB A2 micro SD card](https://amzn.to/3oJtTqs) (or larger), and a [Micro USB 2.0 Cable](https://amzn.to/3LxXYmA). The essential software needed for this process includes [Balena Etcher](https://www.balena.io/etcher/), Balena Raspberry Pi Image, and [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)有了这些资源，您就可以继续更换或重新刷新 SD 卡了。

## 所需工具：
- 十字螺丝刀或 [plastic pry bar](https://amzn.to/3rLXVfc) for the Nebra Indoor Miner or [allen key set](https://amzn.to/34SlnOS)用于 Nebra Outdoor Miner
- 坚固的指甲、镊子或尖嘴钳，用于取出旧 SD 卡
 [A Micro SD Card Reader](https://amzn.to/3Jl3U0w)
- [A 64gb (or larger) A2 micro sd card](https://amzn.to/3oJtTqs)
- [A Micro USB 2.0 Cable](https://amzn.to/3LxXYmA)
## 所需软件：
- [Balena Etcher](https://www.balena.io/etcher/)
- [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)
- 适用于您的特定设备的最新 Nebra 图像：
*如果您不知道您使用的是哪种设备，请查阅 [nebra documentatio](https://support.nebra.com/support/home)如果是旧版本，则可以认为您使用的是第一代设备。
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)

### Nebra氦气采矿器内部：
### Nebra 室内采矿器的内容：
{{< figure src="Indoor-internal-lights.png" alt="Nebra Indoor Miner" >}}
### Nebra Outdoor Miner 的内容：
{{< figure src="Inside-Interfaces.jpg" alt="Nebra Outdoor Miner" >}}
 - 1.) 9-16V @ 15W DC 6.5MMx2.0MM 管状插孔
 - 2.)以太网连接器
 - 3.)LED 指示灯
 - 4.)接口按钮
 - 5.)4G / LTE 模块连接器
 - 6.)SIM 卡插槽

## 如何更换 SD 卡
### 步骤 1：可选择从 EMMC Key 获取 config.json 文件：
- 下载并安装 [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)将计算模块作为 USB 文件系统启动时需要此功能
- 识别并调整 CM3 子板上的跳线引脚，以实现编程模式
 - {{< figure src="daughterboardBreakdown.png" alt="Nebra Daughterboard Overview" >}}
   - 5.)用于成像的微型 USB 端口
   - 7.)JP4 USB 跳线 - 用于在正常操作和闪存模式之间切换，确保处于 1-2 位置为正常操作，2-3 位置为编程模式。
   - 8.)JP3 电源跳线 - 允许通过微型 USB 接口为模块供电。仅在从 PC 编程时连接，并确保主板未连接。
 - 将 JP4 跳线移至 2+3 位置
 - 插入 USB 电缆并运行 [Raspberry Pi USB Boot](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe)实用程序
 - 打开文件资源管理器，你会看到一个名为 "resin-boot "的驱动器。从目录中读取 "config.json "文件，你以后可能会用到它，而且它应该已经备份。
 - 拔下 USB 电缆，将 JP4 跳线重置到 1+2 位置。
### 第 2 步：用 Balena Raspberry Pi CM3 映像闪存新的 SD 卡：
- 下载并解压缩相应的映像
  - [Nebra Outdoor 2](https://github.com/NebraLtd/helium-nebra-outdoor2/releases/)
  - [Nebra Indoor 2](https://github.com/NebraLtd/helium-nebra-indoor2/releases/)
  - [Nebra Outdoor 1](https://github.com/NebraLtd/helium-nebra-outdoor1/releases)
  - [Nebra Indoor 1](https://github.com/NebraLtd/helium-nebra-indoor1/releases)
- 使用 [Balena Etcher](https://www.balena.io/etcher/)选择最近提取的 .img 文件和新的 microSD 卡作为目标设备
- 选择闪存
### 第三步：安装新的 SD 卡并重新组装 Nebra Miner：
 - 将 SD 卡安装到先前安装 EMMC 密钥的插槽中。
 - 重新组装矿机
 - 首次为新刷新的 Nebra 矿机供电时，先用以太网插上 20-30 分钟，然后再重新设置 Wifi 连接。
### 第四步：获利？




