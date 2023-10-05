---
title: "在 HP t740 瘦客户机上运行 pfSense：提示和故障排除指南"
draft: false
toc: true
date: 2023-04-29
description: "了解如何在 HP t740 瘦客户机上设置 pfSense，以及如何解决冻结和 SSD 检测问题等潜在问题。"
tags: ["感知", "OPNsense", "强化BSD", "惠普t740", "瘦客户端", "家庭服务器", "PPPoE", "FreeBSD", "开机提示", "loader.conf.local", "纳米编辑器", "SSD检测", "M.2固态硬盘", "西部数据", "故障排除", "安装后", "串口", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "一幅卡通画，画的是巫师施咒修复冻结的计算机，并带有一个对话泡泡，上面写着“问题已解决”"
coverCaption: ""
canonical: "https://simeononsecurity.ch/guides/installing-pfsense-on-hp-t740-thin-client/"
---
 HP t740 瘦客户机上的 pfSense、OPNsense 或 HardenedBSD**

如果您正在寻找一款功能强大的设备来运行 pfSense、OPNsense 或 HardenedBSD，HP t740 瘦客户机可能是您的合适选择。

## 更强大、更紧凑的家庭服务器

HP t740 瘦客户机是一款紧凑型设备，可用作功能强大的 pfSense 盒或紧凑型家庭服务器。它提供比 t730 或 t620 Plus 更强大的功能，这使其成为运行 PPPoE 的合适选择，尤其是在您拥有光纤互联网的情况下。它还可以提供升级到 10 Gigabit 网络的路径。

## PS/2 冻结

但是，如果您计划在裸机上（而不是在 ESXi 或 Proxmox 内部）运行 FreeBSD 或其衍生产品，如 pfSense、OPNsense 或 HardenedBSD，您可能会遇到系统在启动时冻结并显示消息的问题 `atkbd0: [GIANT-LOCKED]` 幸运的是，这个问题可以通过在引导提示符下输入以下命令来解决：

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*请注意，您需要同时取消设置，否则，它仍会在启动时锁定。*

安装操作系统后，打开安装后 shell 并运行以下命令：

```bash
vi /boot/loader.conf.local
```
然后，添加这两行：
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### 使用 VI 保存更改
对于那些不熟悉 vi 的人，您可以通过执行以下操作来添加该行：

添加行 `hint.uart.0.disabled="1"` 和 `hint.uart.1.disabled="1"` 到 `/boot/loader.conf.local` 使用 vi 编辑器可以通过以下步骤完成文件：

1. 在您的 FreeBSD 系统上打开终端。

2.类型 `vi /boot/loader.conf.local` 然后按 Enter 在 vi 编辑器中打开文件。

3. 按 `i` 键进入插入模式。

4. 使用箭头键将光标移至文件底部。

5.类型 `hint.uart.0.disabled="1"` 没有引号。

6. 按 Enter 开始新的一行。

7.类型 `hint.uart.1.disabled="1"` 没有引号。

8. 按 `Esc` 键退出插入模式。

9.类型 `:wq` 然后按 Enter 保存并退出文件。

这会将这两行添加到 `/boot/loader.conf.local` 文件，这将在运行 FreeBSD 或其衍生产品（如 pfSense、OPNsense 或 HardenedBSD）时禁用 UART 并修复某些 HP t740“瘦客户端”设备启动期间的冻结问题。

这将解决 pfSense/OPNsense 上重启和固件升级的问题。

## 固态硬盘

如果您使用的是 HP M.2 eMMC，则在开箱即用的 FreeBSD 安装中不会检测到它。在这种情况下，您将需要第三方 M.2 SSD。任何 M.2 SSD 都可以工作，SATA 或 NVMe。

如果您正在为您的 HP t740 瘦客户机寻找第三方 M.2 SSD，我们建议您考虑 [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) 这两个选项都是可靠的，应该可以很好地与您的设备配合使用。如果您想利用这两个插槽，则两者都需要。您将牺牲 NVME 的速度，但您将获得一些非常重要的冗余。

请注意，本文作者在执行上述步骤后，已在其 t740 上成功运行 pfSense CE 2.5.2 和 OPNsense 22.1，没有出现任何问题。

## 故障排除和安装后

安装后，如果您在编辑文件时遇到任何问题，可以使用安装 nano 编辑器 `pkg update` 和 `pkg install nano` 这将帮助您轻松编辑文本文件。

以确保对 `/boot/loader.conf.local` 文件在 pfSense 版本升级中保持不变，您需要将以下行添加到 `/boot/loader.conf` 和 `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

但是，有时编辑 `/boot/loader.conf.local` 重新启动前的文件不能解决问题。在这种情况下，可能需要在第一次引导开始时添加以下行：

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

这些步骤应该可以解决安装过程中和之后可能出现的大多数问题。

＃＃＃ 参考：
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)