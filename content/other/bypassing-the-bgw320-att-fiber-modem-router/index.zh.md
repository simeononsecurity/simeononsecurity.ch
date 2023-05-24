---
title: "绕过 BGW-320：使用 Azores COTS ONT - 分步指南"
draft: false
toc: true
date: 2023-04-30
description: "通过这份易于遵循的指南，了解如何绕过 BGW-320 并使用 Azores 制造的 COTS ONT 连接到您的 ISP 网络。"
tags: ["科茨安大略省", "BGW-320", "亚速尔群岛", "纤维", "网络", "XGS-PON", "以太网", "IP透传", "定制", "网络服务提供商", "手机号", "MAC地址", "设备编号", "图像版本", "硬件版本", "远程登录", "CLI 应用程序", "网页界面", "出厂配置模式", "兼容性问题"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "一位卡通技术人员手持 COTS ONT，背景中有一根光缆。"
coverCaption: ""
---

## 如何绕过 BGW-320 并使用 Azores WAG-D20

大多数使用光纤的人有两种连接到互联网的方式——光纤连接到 ONT、以太网连接到网关或光纤直接连接到网关。在本文中，我们将重点介绍如何绕过 BGW-320 并使用 Azores 制造的 COTS ONT。

### 技术方面

这 [Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### 设备访问

设备的默认 IP 地址为 192.168.1.1，其网关地址有一个使用公共 IP 地址的出厂拼写错误，即它显示 192.162.1.1 而不是 192.168.1.1。

启动后，您需要按回车键以在 TTL 串行接口 (115200 8N1) 上获得登录提示。该设备有一个 A/B 图像系统，带有一个覆盖分区，其中包含您自定义的任何文件。
 
＃＃＃ 证书

- `admin``ADMIN123!@#` - Web GUI 的管理员登录
- `Guest``welcome` - 访客登录
- `test``default` - 工厂登录

###以太网接口

将您的客户端连接到 10G 以太网端口，并使用 192.168.1.x/24 网络中的地址配置它，例如 - 192.168.1.2/255.255.255.0。

从 1-65535 运行端口扫描后，您会注意到一些打开的端口：

- 端口 `23` & `8009` - Telnet，需要登录，运行 CLI 应用程序。
- 港口 `10002` - 未知
- 港口 `80` - WebUI，只有两个功能

###自定义ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

现在是重要的部分，即更改一些设备信息以使其与您的 ISP 网络兼容。

首先，从您的 ISP 网关或 ONT 获取以下信息：

1. **ONT ID**
2. **MAC地址**
3. **设备ID**
4. **图片版**
5. **硬件版本**

注意：这些是 OMCI 值，而不是来自 Web UI 的值。

Telnet 到您的个人 ONT（telnet 192.168.1.1），登录为 **`test` 使用 **`default` 密码并运行命令“test”以进入工厂配置模式。

使用“show”命令显示当前设置的值：

- `show gpon mac`
- `show sn`
- `show equipment id`

完成后，使用以下命令自定义设置，将 x 替换为您的设备值：

- `set gpon mac xx:xx:xx:xx:xx:xx`
- `set sn <insert ONT ID here>`

对于数码士：

- `set equipment id “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

对于诺基亚：

- `set equipment id “iONT320505G”`
- `config ONU-G_Version "BGW320-505_2.2”`

注意：最后两个命令应从以 ** 身份登录的 telnet 应用`test` 用户。

### 重启并享受真正的 IP 直通

定制完成后，重启ONT，即可享受真正的IP直通。

### 故障排除和其他步骤
有关此主题的更多信息，请查看 [8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

＃＃＃ 结论

通过执行这些步骤，可以成功绕过 BGW-320 并使用 Azores 制造的 COTS ONT 连接到其 ISP 的网络。但是，在输入命令时要小心，并确保将“x”正确替换为您的设备值，否则，您可能会遇到可能导致连接失败的兼容性问题。


