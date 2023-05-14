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
---
 HP t740 瘦客户机上的 pfSense、OPNsense 或 HardenedBSD**

如果您正在寻找一款功能强大的设备来运行 pfSense、OPNsense 或 HardenedBSD，HP t740 瘦客户机可能是您的合适选择。

## 更强大、更紧凑的家庭服务器

HP t740 瘦客户机是一款紧凑型设备，可用作功能强大的 pfSense 盒或紧凑型家庭服务器。它比 t730 或 t620 Plus 提供更多功率，这使其成为运行 PPPoE 的合适选择，尤其是在您有光纤互联网时。它还可以提供升级到 10 Gigabit 网络的路径。

## PS/2 冻结

但是，如果您计划在裸机上运行 FreeBSD 或其衍生产品，如 pfSense、OPNsense 或 HardenedBSD（而不是在 ESXi 或 Proxmox 内部），您可能会遇到系统在启动时冻结并显示消息 atkbd0 的问题：[巨型锁定]`。幸运的是，这个问题可以通过在引导提示符下输入以下命令来解决：

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Note that you need to unset both, otherwise, it will still lock up at boot.*

After you install the OS, open a post-installation shell and run the following command:

```bash
vi /boot/loader.conf.local
```
Then, add these two lines:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persist Changes using VI
For those not familiar with vi, you can add the line by doing the following :

Adding the lines `hint.uart.0.disabled="1"` and `hint.uart.1.disabled="1"` to the `/boot/loader.conf.local` file using the vi editor can be done with the following steps:

1. Open the terminal on your FreeBSD system.

2. Type `vi /boot/loader.conf.local` and press Enter to open the file in the vi editor.

3. Press the `i` key to enter insert mode.

4. Move the cursor to the bottom of the file using the arrow keys.

5. Type `hint.uart.0.disabled="1"` without the quotes.

6. Press Enter to start a new line.

7. Type `hint.uart.1.disabled="1"` without the quotes.

8. Press the `Esc` key to exit insert mode.

9. Type `:wq` and press Enter to save and exit the file.

This will add the two lines to the `/boot/loader.conf.local` file, which will disable the UARTs and fix the freezing issue during boot on certain HP t740 "Thin Client" devices when running FreeBSD or its derivatives like pfSense, OPNsense, or HardenedBSD.

This will fix the issue across reboots and firmware upgrades on pfSense/OPNsense. 

## SSD

If you're using the HP M.2 eMMC, it will not be detected on an out-of-the-box FreeBSD installation. In that case, you will need a third-party M.2 SSD. Any M.2 SSD can work, SATA or NVMe. 

If you are looking for a third-party M.2 SSD for your HP t740 thin client, we recommend considering the [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V). Both of these options are reliable and should work well with your device. If you want to take advantage of both slots, you'll need both. You'll sacrifice the speeds of the NVME, but you'll gain some redundancy that's oh so important.

Note that the author of this article has successfully run pfSense CE 2.5.2 and OPNsense 22.1 on their t740 without any issues after following the above steps. 

## Troubleshooting and Post Install

After installation, if you encounter any issues with editing files, you can install the nano editor using `pkg update` and `pkg install nano`. This will help you edit text files with ease.

To ensure that the changes made to the `/boot/loader.conf.local` file persist across pfSense version upgrades, you need to add the following lines to `/boot/loader.conf` and `/etc/rc.conf.local`: 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

However, sometimes the editing of `/boot/loader.conf.local` file before rebooting doesn't fix the issue. In such cases, it may be necessary to add the following lines at the beginning of the first boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

这些步骤应该可以解决安装过程中和之后可能出现的大多数问题。

＃＃＃ 参考：
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)