---
title: "重新安装 Windows 前先找到 BitLocker 恢复密钥"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "找到并核对正确的 BitLocker 恢复密钥，另存安全副本，并在清除磁盘前选择合适的 Windows 恢复或重装方式。"
genre: ["Windows 安全", "数据恢复", "系统管理"]
tags: ["BitLocker 恢复密钥", "重装 Windows 11", "重装 Windows 10", "设备加密", "恢复密钥 ID", "Microsoft 帐户恢复密钥", "工作或学校帐户密钥", "恢复密钥备份", "加密磁盘", "全新安装", "Windows 恢复", "BitLocker 备份", "48 位恢复密钥", "Windows 安装介质", "数据备份", "磁盘加密", "恢复检查清单", "Windows 安装", "BitLocker 故障排除", "重装准备"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "一台带有锁定磁盘的笔记本电脑、一张单独保存恢复密钥的卡片、USB 备份和已勾选的恢复清单。"
coverCaption: "清除磁盘前先核对恢复密钥。"
---

全新安装 Windows 会清除所选磁盘。如果旧磁盘使用 **BitLocker** 或**设备加密**，请先找到恢复密钥并复制文件，再开始安装。恢复密钥用于访问旧的加密数据。重新安装 Windows 不会恢复已从磁盘删除的文件。

<!--more-->

## 要点

- **找到正确的密钥：** 将 Windows 显示的密钥 ID 与帐户、打印件或 USB 备份中保存的密钥核对。
- **验证访问能力：** 检查备份并核对 ID，在删除分区前解锁被锁定的磁盘。
- **保护备份：** 将 48 位密钥与电脑和安装 USB 分开保存。
- **选择合适的方式：** 需要旧系统时使用恢复选项。确认文件已有单独副本后，再选择全新安装。

## 开始之前

你需要访问受影响的电脑，准备另一台设备来检查帐户或备份，并准备外置磁盘或可信的云存储来保存重要文件。**用时：** 查找密钥的时间取决于帐户访问情况。复制文件的时间取决于数据量。**难度：** 检查帐户较简单，使用恢复工具为中等。本指南介绍 Windows 10 和 Windows 11 的准备工作与恢复选择。[Windows 全新安装指南](/articles/how-to-install-windows-10-and-windows-11-from-scratch/)介绍安装介质和安装过程。

*Windows 10 标准支持已于 2025 年 10 月 14 日结束。如果设备符合要求，请计划安装受支持的 Windows 11。Microsoft 列出了 [Windows 10 生命周期和扩展支持选项](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support)。*

> **警告：** 如果仍需要旧系统中的文件，不要为了处理 BitLocker 恢复提示而删除分区。Microsoft 指出，没有恢复密钥就重置会删除这些文件。请参阅 [Microsoft 的恢复密钥说明](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key)。

## 检查加密是否已启用

**设备加密**和 **BitLocker** 会加密磁盘，防止没有正确凭据的人读取内容。如果 Windows 仍能启动，请在 Windows 11 中打开**设置 > 隐私和安全性 > 设备加密**。在支持 BitLocker 管理的版本中，从“开始”菜单搜索**管理 BitLocker**。记录加密磁盘的盘符，以及设置设备时使用的帐户。由组织管理的工作或学校设备通常由组织保管密钥。

你也可以通过命令行检查状态。从“开始”菜单搜索**命令提示符**，选择**以管理员身份运行**，然后输入以下命令。如果 Windows 使用其他盘符，请替换 `C:`。**保护器**是 Windows 用来解锁加密磁盘的方式。

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

第一条命令显示加密、保护和锁定状态。第二条列出保护器类型和 ID，并可能显示恢复密码。Microsoft 在 [BitLocker 操作指南](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide)和[状态命令参考](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status)中说明了这两种检查方法。

**不要把输出粘贴到求助请求中，也不要在截图中分享。**

如果设备已锁定，请使用恢复屏幕上的 ID。ID 的前八位数字有助于选择匹配的密钥。

## 在哪里查找 BitLocker 恢复密钥

**恢复密钥 ID**用于标识已保存的密钥。**恢复密钥**是用于解锁磁盘的另一个 48 位数字。不要把 ID 输入恢复密码框。

| 设备或备份 | 查找位置 |
|---|---|
| **个人 Microsoft 帐户** | 在另一台设备上，通过 [Microsoft 恢复密钥页面](https://aka.ms/myrecoverykey)登录。使用 48 位密钥前先核对 ID。 |
| **工作或学校设备** | 通过 [Microsoft 工作或学校帐户页面](https://aka.ms/aadrecoverykey)检查组织帐户，或联系 IT 团队。 |
| **打印件或 USB 备份** | 查找启用加密时创建的打印件或文本文件。将其中的密钥 ID 与屏幕显示的 ID 核对。 |

Microsoft 在[查找 BitLocker 恢复密钥](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key)中列出了这些位置。先使用 ID 与提示匹配的密钥。其他设备的密钥或已移除保护器的密钥可能无法解锁此卷。如果设备由其他人设置，密钥可能保存在对方的帐户中。

## 单独备份密钥

如果 Pro、Enterprise 或 Education 版 Windows 仍能启动，请搜索**管理 BitLocker**。在加密磁盘旁选择**备份恢复密钥**。Microsoft 支持将密钥备份到帐户、USB 磁盘、文本文件或打印件。如果选择文本文件或 USB，请仅将其保存在有访问控制的加密介质上，并与电脑分开。不要使用未加密的位置。当前界面和选项请参阅[备份 BitLocker 恢复密钥](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key)。

Windows Home 没有**管理 BitLocker**。在 Windows 11 中检查**设置 > 隐私和安全性 > 设备加密**，然后在设置设备时使用的 Microsoft 帐户中核对密钥。Microsoft 说明，[设备加密](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows)启用时会将密钥保存在关联的 Microsoft 或工作帐户中。如果当前设置提供导出方式，请另存一份受保护的副本。

在另一台设备上打开数字备份。若为打印件，请与帐户记录或恢复屏幕进行比较。将**恢复密钥 ID**与恢复屏幕或保护器列表中的 ID 核对。确认对应密钥的 48 位数字完整无误。将纸质或可移动副本存放在加密电脑之外。Microsoft 在[备份说明](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key)中提醒，如果窃贼同时拿到电脑和密钥，便可能绕过磁盘保护。不要把密钥附在支持工单中。

> **预期结果：** 你可以在电脑之外找到匹配的恢复密钥。

## 解锁无法启动的电脑

如果出现 **BitLocker 恢复屏幕**，请输入与屏幕 ID 匹配的 48 位密钥。Windows 启动后，先复制文件，再修改分区。如果密钥能解锁磁盘但 Windows 仍无法启动，请打开 [Windows 恢复环境](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment)，并在重置前尝试**启动修复**。磁盘仍处于加密状态时，某些恢复工具需要密钥。

要通过恢复工具备份文件，请在 Windows 恢复环境中打开**疑难解答 > 高级选项 > 命令提示符**。使用 `manage-bde -status` 和 `dir` 找到加密的 Windows 卷以及另一块用于备份的外置磁盘。

**盘符可能与正常 Windows 中不同。**

不要把文件复制到安装 USB 或加密的源磁盘。

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

以上盘符仅为示例。找到正确卷后，用匹配的密钥解锁 Windows 卷。将示例盘符和占位符替换为你的值。在本机输入真实的 48 位密钥。不要发布或分享命令输出。

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

文档中的 `-recoverypassword` 选项会将 48 位密钥作为命令行参数。这可能让密钥出现在 shell 历史记录、会话记录和进程检查结果中。如果不想把密钥作为命令行参数输入，请使用 Windows 恢复屏幕。如果另存了 `.bek` 密钥文件，`-recoverykey <path-to-external-bek>` 可避免输入 48 位数字。不要在截图或工单中暴露密钥。

Microsoft 介绍了[解锁命令](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock)。其[恢复说明](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues)也介绍了解锁后如何将用户文件复制到另一块磁盘。要示例性地复制“文档”文件夹，请先确认 Windows 帐户名和外置磁盘盘符，然后替换两个路径：

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

“**`/S /E`**”会包含子文件夹，包括空文件夹。“**`/I`**”将目标视为文件夹，“**`/H`**”包含隐藏文件，“**`/V`**”检查每个写入的文件。Microsoft 在 [xcopy 参考](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy)中说明了这些选项。对其他需要的文件夹重复操作。清除 Windows 磁盘前，请在另一台设备上打开复制的文件。如果无法识别卷或复制失败，请停止操作并联系可信的数据恢复专家。

## 决定是否重新安装

**密钥备份不等于文件备份。**

选择重装方式前，按以下顺序操作：

1. 确认加密磁盘及其恢复密钥 ID。
2. 从帐户、打印件或 USB 备份中取出匹配的 48 位密钥。
3. 如果磁盘已锁定，通过恢复屏幕或恢复工具解锁。
4. 将桌面、文档、图片和其他本地文件夹复制到外置磁盘或可信的云存储。必要时也保存浏览器导出数据、应用数据和许可证记录。
5. 在另一台设备上打开几份复制的文件。
6. 检查备份后，再选择修复、重置或重新安装。

> **预期结果：** 你可以在旧 Windows 安装之外访问匹配的密钥和重要文件。

Microsoft 列出了[Windows 恢复选项](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows)，它们对文件和应用的影响不同。如果 BitLocker 保护磁盘，Windows 恢复环境中的许多选项都需要恢复密钥。如果卷在此处被锁定，没有密钥时**保留我的文件**也无法解锁它。

“**启动修复**”和“**系统还原**”尝试修复现有安装。“**重置此电脑**”提供“**保留我的文件**”选项，但会删除应用和设置。“**删除所有内容**”会清除个人文件。在运行中的 Windows 会话里启动“**`setup.exe`**”，即可进行带有保留数据选项的就地重装。从安装 USB 启动后，选择“**安装 Windows**”，便会开始全新安装，并删除所选 Windows 安装中的文件、应用和设置。同一介质也提供修复方式。确认重置或安装前，请阅读显示的选项并检查目标磁盘。Microsoft 在[重新安装说明](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media)中介绍了这两种方式。

| 情况 | 下一步 |
|---|---|
| **Windows 能启动且你需要文件** | 备份文件，核对恢复密钥，然后选择修复或重装。 |
| **Windows 要求输入密钥** | 修改磁盘前，将屏幕 ID 与已保存的密钥核对。 |
| **没有匹配的密钥，也没有文件备份** | 清除磁盘前先停止。检查所有帐户、打印件、USB 备份，并联系 IT 团队。 |
| **文件已备份且你想重新开始** | 按照 Microsoft 的[重装说明](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media)操作，并谨慎选择目标磁盘。 |

Microsoft 表示，支持人员无法重新创建丢失的恢复密钥。如果找不到密钥，请停止更改固件设置，并检查所有备份位置。对于受管理的设备，请联系管理员。没有所需密钥就重置会删除旧文件。全新安装还会删除所选安装中的个人文件、应用、设备自定义项和设置。核对备份后再做决定。

## 故障排除

- **密钥无效：** 重新核对 ID 和帐户。设备可能保存了多个恢复密钥。
- **找不到“管理 BitLocker”：** 符合条件的 Windows Home 设备使用设备加密。请检查“设置”和设置设备时使用的 Microsoft 帐户。
- **帐户中有多个密钥：** 将恢复屏幕 ID 的前八位与保存的记录核对。不要只根据设备名称选择密钥。
- **密钥解锁了磁盘但 Windows 无法启动：** 在 Windows 恢复环境中尝试启动修复。重置或全新安装前，先复制可访问的文件。
- **密钥由工作单位或学校保管：** 重置或重新安装前联系设备管理员。
- **密钥文件在被锁定的电脑上：** 查找单独的帐户、打印件或可移动备份。只有加密磁盘上有副本时，磁盘锁定状态下无法使用。
- **更改固件后出现恢复提示：** 记录更改内容，不要继续修改固件。查找匹配的密钥或联系设备管理员。

## 后续步骤

确认密钥和文件后，如果全新安装符合你的目标，请按照 [Windows 全新安装指南](/articles/how-to-install-windows-10-and-windows-11-from-scratch/)操作。Windows 启动后，检查**设置 > 隐私和安全性 > 设备加密**，或搜索**管理 BitLocker**。在 Pro、Enterprise 或 Education 版中，选择**备份恢复密钥**。在 Home 版中，确认关联帐户里有当前密钥；如果 Windows 提供导出功能，再保存一份单独副本。不要认为旧密钥一定适用于新加密的安装。
