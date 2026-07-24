---
title: "终极指南：在 Google Pixel 设备上安装 GrapheneOS"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "学习如何使用网页安装器或命令行（CLI）方法在 Google Pixel 设备上安装 GrapheneOS，以增强隐私和安全性。"
tags: ["GrapheneOS", "Google Pixel", "隐私", "安全", "Android", "移动设备", "操作系统", "安装指南", "自定义ROM", "隐私保护", "数据保护", "安全操作系统", "开源", "设备安全", "fastboot", "引导加载程序", "验证启动", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "一幅抽象数字插图，展示一部 Google Pixel 智能手机通过 USB-C 数据线连接到电脑，周围环绕着代表数据传输和安全的彩色图形元素。"
coverCaption: ""
---

**如何在 Google Pixel 设备上安装 GrapheneOS**

GrapheneOS 是一款基于 Android 的开源、注重隐私的操作系统。它提供了大幅增强的安全加固和隐私保护功能，是任何关注数据隐私和安全的用户的绝佳选择。如果您拥有受支持的 Google Pixel 设备并希望切换到 GrapheneOS，本指南涵盖了推荐的**网页安装器**方法和传统的**命令行（CLI）**方法。

> **提示：** 如果在安装过程中遇到问题，请在 [GrapheneOS 官方聊天频道](https://grapheneos.org/contact#community)寻求帮助。在寻求帮助之前，请先尝试自行按照指南操作，然后针对卡住的地方提问。

## 前提条件

### 硬件与系统要求

- 一台至少有 **2 GB 空闲内存**和 **32 GB 空闲存储空间**的电脑。
- 设备随附的**高质量 USB-C 数据线**（如需要也可使用 USB-C 转 USB-A 线）。避免使用 USB 集线器，直接连接到台式机后面板端口或笔记本端口。
- 由于 USB 直通不可靠，**不建议**从虚拟机进行安装。

> 在安装 GrapheneOS 之前，建议先更新 Pixel 设备以获取最新固件。无论如何，GrapheneOS 在安装过程初期会刷入最新固件。

### 官方支持的操作系统

#### 网页安装器

- Windows 10 / Windows 11
- macOS Sonoma (14)、macOS Sequoia (15)、macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm)、Debian 13 (trixie)
- Ubuntu 22.04 LTS、Ubuntu 24.04 LTS、Ubuntu 25.04
- Linux Mint 21（按 Ubuntu 22.04 LTS 说明操作）、Linux Mint 22（按 Ubuntu 24.04 LTS 说明操作）
- Linux Mint Debian Edition 6（按 Debian 12 说明操作）
- ChromeOS
- GrapheneOS
- 具有 Play Protect 认证的 Android 13、14、15 和 16

#### CLI 方法

除 ChromeOS、GrapheneOS 和 Android（只能使用网页安装器）外，上述所有系统均可使用。

也可以使用这些平台的旧版本，但不提供官方支持。**在继续之前，请确保您的操作系统是最新版本。**

### 官方支持的浏览器（仅限网页安装器）

- **Chromium**（Ubuntu 以外，Ubuntu 的 Snap 包缺少可用的 WebUSB）
- **Vanadium**（GrapheneOS）
- **Google Chrome**
- **Microsoft Edge**
- **Brave**（需禁用 Brave Shields，否则为防止指纹识别会限制存储使用量）

> - 在 Android 上，请**禁用浏览器的桌面模式**。桌面模式会阻止网页安装器检测到 Android 并在重启后请求重新连接权限。在 8 GB 以上内存的大型平板电脑（如 Pixel Tablet）上，该模式默认启用。
> - 避免使用 Flatpak 和 Snap 版本的浏览器，它们会在安装过程中造成问题。
> - **不要**使用无痕/私密浏览模式，这些模式会限制解压下载版本所需的存储空间。

### 支持的设备

您需要一台[官方支持的 Pixel 设备](https://grapheneos.org/faq#supported-devices)。**避免购买运营商定制版**，运营商版 Pixel 在出厂时写入了非零运营商 ID，会禁用引导加载程序解锁和运营商解锁。请购买通用（解锁）版设备。

---

## 启用 OEM 解锁

在继续操作之前，必须在操作系统内部启用 OEM 解锁。

1. 进入**设置 → 关于手机/平板**，连续点按**版本号**直到开发者模式被启用。
2. 进入**设置 → 系统 → 开发者选项**，打开 **OEM 解锁**。在部分运营商版 SKU 上，此操作需要活跃的网络连接，以便原厂系统验证设备未以运营商锁定方式销售。

> **Pixel 6a 注意事项：** 使用出厂系统版本时 OEM 解锁无效。通过 OTA 更新至 **2022 年 6 月**或更新版本，然后执行出厂重置以修复 OEM 解锁问题。

---

## 安装方法一：网页安装器（推荐）

[GrapheneOS 网页安装器](https://grapheneos.org/install/web)是大多数用户的推荐方法。它直接在浏览器中使用 WebUSB，无需安装任何软件。

### 第 1 步：绕过 fwupd 错误（仅 Linux）

在 Linux 上，`fwupd` 已知会错误地使用 fastboot 协议连接设备，阻止安装器运行。在连接设备之前停止它：

```bash
sudo systemctl stop fwupd.service
```

此操作在重启后不会持续。

### 第 2 步：设置 udev 规则（仅 Linux）

Arch Linux 上：

```bash
sudo pacman -S android-udev
```

Debian 和 Ubuntu 上：

```bash
sudo apt install android-sdk-platform-tools-common
```

### 第 3 步：进入引导加载程序界面

在设备启动时按住**音量减**按钮（关机状态下按住音量减后开机，或重启时按住）。设备必须显示**红色警告三角形**和文字 **"Fastboot Mode"**——不要按电源键激活"Start"。

### 第 4 步：连接您的设备

通过 USB 将设备连接到电脑。在 Linux 上，如果第一次连接前未设置 udev 规则，请重新插拔数据线。

> **Pixel Tablet：** 通过 USB 连接之前，请先将平板从底座上取下——平板无法同时使用两者。

> **Windows：** 当前 Windows 10/11 内置了适用于 Pixel 4a (5G) 及更新型号的通用 fastboot 驱动程序。对于更旧的 Pixel 或旧版 Windows，请通过 Windows 更新安装驱动程序（在"查看可选更新"→"LeMobile Android Device"下查找）。

### 第 5 步：解锁引导加载程序

访问 [https://grapheneos.org/install/web](https://grapheneos.org/install/web) 并点击 **Unlock the bootloader** 按钮。在设备上使用音量键切换选择，使用电源键确认。**这将清除所有数据。**

### 第 6 步：获取并刷入出厂镜像

1. 点击 **Download release** 下载您设备的出厂镜像。
2. 点击 **Flash factory images** 并等待完成。系统会自动刷入固件，重启进入引导加载程序界面，然后刷入操作系统。**在完成之前请不要操作设备。**

### 第 7 步：锁定引导加载程序

刷写完成后，在网页安装器中点击 **Lock the bootloader**。在设备上确认。**这将再次清除所有数据** — 锁定引导加载程序会启用完整的验证启动。

---

## 安装方法二：命令行（CLI）

### 第 1 步：打开终端

在 Windows 上，打开一个**普通（非管理员）PowerShell** 窗口。移除旧版 `curl` 别名：

```powershell
Remove-Item Alias:Curl
```

### 第 2 步：安装 fastboot

您需要 **≥ 35.0.1** 版本的 fastboot。

**Arch Linux：**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — 其软件包已过时。使用独立发行版：

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS：**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows：**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

验证版本：

```bash
fastboot --version
# 预期输出：fastboot version 35.0.2-12147458
```

### 第 3 步：设置 udev 规则（仅 Linux）

Arch Linux：

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu：

```bash
sudo apt install android-sdk-platform-tools-common
```

### 第 4 步：绕过 fwupd 错误（仅 Linux）

```bash
sudo systemctl stop fwupd.service
```

### 第 5 步：进入引导加载程序界面

启动时按住**音量减**，直到设备显示带红色警告三角形的 **"Fastboot Mode"**。

### 第 6 步：连接并解锁引导加载程序

通过 USB 连接后运行：

```bash
fastboot flashing unlock
```

在设备上确认（音量键切换选择，电源键确认）。**这将清除所有数据。**

### 第 7 步：安装 OpenSSH（用于镜像验证）

macOS 和 Windows 默认包含 OpenSSH。

Arch Linux：

```bash
sudo pacman -S openssh
```

Debian / Ubuntu：

```bash
sudo apt install openssh-client
```

### 第 8 步：下载并验证出厂镜像

下载签名密钥：

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

预期内容：

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

下载出厂镜像（将 `DEVICE_NAME` 和 `VERSION` 替换为实际值）：

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

验证签名（Linux / macOS）：

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows：

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

预期输出：

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### 第 9 步：刷入出厂镜像

解压镜像：

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

进入目录并运行刷写脚本：

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

等待完成。该过程会自动处理固件刷写、引导加载程序重启和操作系统刷写。**在完成之前请不要操作设备。**

> **Linux tmpfs 问题排查：** 如果 `/tmp` 空间不足，请使用：
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### 第 10 步：锁定引导加载程序

```bash
fastboot flashing lock
```

在设备上确认。**这将再次清除所有数据。** 锁定会启用完整的验证启动，防止 fastboot 修改分区。

---

## 安装后操作

### 启动

在引导加载程序界面选中默认的 **Start** 选项后按电源键启动 GrapheneOS。

### 禁用 OEM 解锁

首次设置时，最后一个界面包含 OEM 解锁的开关（默认选中——保持选中状态会**禁用** OEM 解锁）。建议保持此设置。您可以稍后在**开发者选项**中更改。

### 验证安装

GrapheneOS 利用验证启动和硬件证明。验证启动在每次启动时针对烧入 SoC 熔丝的密钥检查所有固件和系统镜像。GrapheneOS 将其自己的验证启动公钥刷入安全元件——每次启动时，该密钥会对操作系统进行验证。

#### 验证启动密钥哈希值

加载替代操作系统时，设备会显示**黄色提示**，包含操作系统标识符（验证启动密钥的 sha256）。第 4 代和第 5 代 Pixel 仅显示前 32 位；**第 6 代及更新的 Pixel 显示完整哈希值**。请与官方哈希值对比：

| 设备 | 验证启动密钥哈希值 |
|------|-----------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### 使用 Auditor 进行基于硬件的证明

GrapheneOS 提供 [Auditor 应用](https://attestation.app/)，使用验证启动和远程证明来验证硬件、固件和操作系统的完整性。结果显示在运行 Auditor 的另一台 Android 设备上（而非被验证的设备上），或通过可选的[设备完整性监控服务](https://attestation.app/)进行自动定期验证并发送电子邮件提醒。

---

## 将 GrapheneOS 替换为原厂系统

通过 Google 的[网页刷写工具](https://flash.android.com/)安装原厂系统的流程与上述类似。但在刷写和锁定之前，您必须擦除 GrapheneOS 的验证启动密钥以完全恢复到原厂系统：

**网页安装器：** 使用 GrapheneOS 网页安装器上的"Erase non-stock key"按钮。

**CLI：**

```bash
fastboot erase avb_custom_key
```

然后刷入原厂系统镜像并锁定引导加载程序。

---

## 总结

在 Google Pixel 设备上安装 GrapheneOS 可提供业界领先的隐私和安全功能。使用 [grapheneos.org/install/web](https://grapheneos.org/install/web) 上的**网页安装器**获得最简便的体验，或按照上述 CLI 步骤进行传统方式安装。刷写完成后务必锁定引导加载程序以启用完整的验证启动，并可选择使用 Auditor 应用确认安装的完整性。

## 参考资料

1. [GrapheneOS 官方网站](https://grapheneos.org/)
2. [GrapheneOS 网页安装器](https://grapheneos.org/install/web)
3. [GrapheneOS CLI 安装指南](https://grapheneos.org/install/cli)
4. [GrapheneOS 发布版本](https://grapheneos.org/releases)
5. [GrapheneOS 使用指南](https://grapheneos.org/usage)
6. [GrapheneOS FAQ](https://grapheneos.org/faq)
7. [Auditor 应用](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)
