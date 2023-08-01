---
title: "今天我学到了创建自定义 Windows 映像的知识"
date: 2023-01-30
toc: true
draft: false
description: "今天我学习了自定义 Windows 映像创建、Sysprep 和通用化"
genre: ["Windows 映像管理", "定制", "Windows 部署", "Sysprep", "一般化", "Windows 10", "视窗 11", "图像捕捉", "图像部署", "NTLite", "Windows 优化"]
tags: ["Sysprep", "NTLite", "一般化", "自定义图片", "自定义窗口图像", "视窗 11", "去浮", "定制", "图像采集", "图像部署", "Windows 映像管理", "Windows 部署工具", "Windows 映像定制", "Windows 图像优化", "微软学习", "WinCustom 存储库"]
---

**SimeonOnSecurity 今天了解到的有趣内容**

今天，SimeonOnSecurity 学习了使用 DISM 捕捉和应用 Windows 10 镜像的过程，DISM 是用于管理 Windows 镜像的命令行工具。要捕获映像，可以使用 Sysprep 工具对安装进行概括，从而移除特定于硬件的信息，为在多个设备上部署映像做好准备。

我们向 SimeonOnSecurity 介绍了提供捕获和应用 Windows 映像信息的各种资源，包括微软的 Learn 网站和 GitHub 上的 WinCustom 资源库。微软的资源涵盖了使用单个 .WIM 文件捕获和应用 Windows 映像、创建可启动 Windows PE 介质以及使用 Sysprep 实现 Windows 安装通用化的基础知识。

此外，SimeonOnSecurity 还了解了 NTLite，这是一款允许自定义和优化 Windows 映像的软件。NTLite 可用于删除 Windows 映像中不必要的组件，从而节省磁盘空间并提高性能。

总之，SimeonOnSecurity 今天的研究让我们全面了解了捕获和应用 Windows 映像的过程。

## Repos 已创建/更新：
- 无/不适用

## 学习资源：
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## 讨论和/或使用的软件：
- [NTLite](https://www.ntlite.com/)