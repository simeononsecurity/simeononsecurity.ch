---
title: "通过命令行 SSH 为 Ubiquiti Unifi UDM Pro 和 UDM SE 进行离线固件更新"
draft: false
toc: true
date: 2023-05-28
description: "了解如何通过命令行 SSH 离线更新 Ubiquiti Unifi UDM Pro 和 UDM SE 的固件以获得最佳性能和安全性。"
tags: ["泛在固件更新", "UDM临", "UDM SE", "离线固件更新", "命令行 SSH", "网络管理", "网络安全", "固件升级", "SSH连接", "固件文件", "UniFi 网络控制器", "bug修复", "性能改进", "安全补丁", "联网", "网络设备", "技术", "资讯科技管理", "固件更新过程", "网络优化", "泛在网络固件更新", "UDM Pro 固件更新", "UDM SE 固件更新", "离线固件更新过程", "SSH 固件更新", "网络设备管理", "网络安全更新", "固件更新策略", "离线固件管理", "网络性能优化", "安全补丁管理", "网络技术更新"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "彩色插图描绘了一台计算机通过 SSH 连接到路由器，象征着 Ubiquiti Unifi UDM Pro 和 UDM SE 设备的离线固件更新过程。"
coverCaption: ""
---

**通过 SSH 离线更新 Ubiquiti Unifi UDM Pro 和 UDM SE**

在网络世界中，**Ubiquiti Networks** 因其创新的解决方案而获得认可。 **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** 和 **Unifi Dream Machine SE (UDM SE)** 是两款提供全面网络管理功能的热门产品。更新这些设备的固件对于确保最佳性能和安全性至关重要。在本文中，我们将探索如何使用命令行 SSH **离线**更新 UDM Pro 和 UDM SE 的固件。

______

## 为什么要更新固件？

固件更新对于任何网络设备都是必不可少的，因为它们通常包含错误修复、性能改进和安全补丁。定期更新 UDM Pro 和 UDM SE 的固件对于确保您的网络保持安全和平稳运行至关重要。

______

## 离线固件更新

可以通过 **UniFi Dashboard** 更新 UDM Pro 和 UDM SE 的固件。但是，在某些情况下，互联网连接可能不可用或不可取。在这种情况下，使用命令行 SSH 的离线更新提供了替代解决方案。

______

## 准备离线更新

在继续进行离线更新之前，请确保您满足以下先决条件：

1. 安装了 SSH 客户端的计算机或设备。
2. UDM Pro 或 UDM SE 的最新固件文件。您可以从以下位置获取固件文件 [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) 帐户

______

## 建立 SSH 连接

要通过命令行 SSH 更新 UDM Pro 或 UDM SE，请执行以下步骤：

1. 确保您的计算机或设备连接到与 UDM Pro 或 UDM SE 相同的网络。
2. 打开您首选的 SSH 客户端并与 **UDM Pro 或 UDM SE 的 IP 地址**建立 SSH 连接。例如，在 Linux 或 macOS 中使用 **OpenSSH 客户端**，您可以使用以下命令：

```bash
ssh root@<UDM_IP_ADDRESS>
```

代替 `<UDM_IP_ADDRESS>` 使用您的 UDM Pro 或 UDM SE 的实际 IP 地址。

3. 出现提示时输入**用户名**和**密码**。 Ubiquiti 设备的默认凭据通常是 `ubnt` 对于用户名和密码。

______

## 更新固件

建立 SSH 连接后，您可以继续进行固件更新：

1. 使用 **SCP（安全复制）** 将固件文件上传到 UDM Pro 或 UDM SE。 SCP 允许通过 SSH 进行安全的文件传输。假设固件文件位于您的本地机器上，您可以使用以下命令：

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

代替 `<FIRMWARE_FILE_PATH>` 使用本地计算机上固件文件的路径，以及 `<UDM_IP_ADDRESS>` 使用您的 UDM Pro 或 UDM SE 的 IP 地址。

2. 上传固件文件后，您可以启动固件更新过程。执行以下命令：

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. UDM Pro 或 UDM SE 将开始固件更新过程。这可能会需要几分钟。 **在更新完成之前不要中断进程**。

4. 更新完成后，您可以通过登录UniFi Network Controller 或执行以下命令来验证固件版本：

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
请注意，上述过程假设您拥有 UDM Pro 或 UDM SE 所需的固件文件。确保您拥有适用于特定设备型号和版本的正确固件文件。

＃＃ 结论

更新 Ubiquiti Unifi UDM Pro 和 UDM SE 设备的固件是确保最佳性能和安全性的关键步骤。虽然 UniFi 网络控制器提供了一种更新固件的便捷方式，但当互联网连接不可用或不需要时，通过命令行 SSH 执行离线更新提供了一种可行的解决方案。

按照本文概述的步骤，您可以使用命令行 SSH 成功更新 UDM Pro 和 UDM SE 设备的固件。请记住始终使用 Ubiquiti Networks 提供的最新固件版本，以利用错误修复、性能改进和安全补丁。

＃＃ 参考

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - 固件文件的官方 Ubiquiti 下载页面。
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
