---
title: "Windows 系统的自动化品牌化 - 轻松控制桌面、锁屏等"
date: 2020-08-14
---


许多组织需要或想要控制 Windows 系统的品牌。
这包括桌面墙纸、用户头像、Windows 锁定屏幕，有时还包括 OEM 徽标。
在 Windows 10、Windows Server 2016 和 Windows Server 2019 中，这并不是特别容易。
但是，在链接脚本的帮助下，我们可以部分自动化它并使过程更加容易。

## 下载需要的文件

**从下载所需的文件[GitHub Repository](https://github.com/simeononsecurity/Windows-Branding-Script)

## 如何设置品牌文件

- [X] 用您的品牌图片替换所有图片
  - [X] OEM 徽标必须为 95x95 或 120x20 且格式为“.bmp”
  - [X] 生成用户图像以及 32x32、40x40、48x48、192x192 变体。
  - [X] 为访客图像生成或复制用户图像。

## 如何运行脚本
```
.\sos-copybranding.ps1
```

## 此脚本使用以下工具：

-[Microsoft Security Compliance Toolkit 1.0 - LGPO](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
