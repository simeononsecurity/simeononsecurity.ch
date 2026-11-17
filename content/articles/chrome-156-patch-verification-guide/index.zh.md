---
title: "Chrome 156 安全更新：验证 10 月补丁"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "检查 Windows、macOS、Linux 和 Android 上 10 月 27 日发布的 Chrome 156 安全版本。对比已安装的构建版本，完成待处理的重启，并单独检查受管理设备。"
genre: ["浏览器", "安全", "补丁管理"]
tags: ["Chrome 156", "Chrome 安全更新", "Chrome 补丁验证", "Chrome 版本检查", "Windows 版 Chrome 156", "macOS 版 Chrome 156", "Linux 版 Chrome 156", "Android 版 Chrome 156", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "浏览器补丁", "Chrome Enterprise Core", "受管理的浏览器", "Chromium 安全", "浏览器更新", "重启 Chrome", "chrome://version", "chrome://settings/help", "Android Chrome 更新", "Brave 安全更新", "Edge 安全更新"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "象征安全更新的挂锁和盾牌插图，不是 Chrome 版本界面"
coverCaption: ""
---

**2026 年 10 月 27 日发布的 Chrome 安全版本**包含 52 项修复。要检查你的安装，请将完整版本号与适用于你操作系统的版本进行比较，然后重启 Chrome 以完成待处理的更新。版本已发布的公告并不能证明你的设备已收到更新。([Chrome 桌面版发布公告](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## 应该看到哪个版本？

Google 于 2026 年 10 月 27 日发布了以下 Stable 渠道版本。桌面版公告分别列出适用于 Windows 和 macOS 的构建版本，以及适用于 Linux 的构建版本。[Android 版公告](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html)列出了自己的构建版本，并说明 Android 版本包含与相应桌面版相同的安全修复，“另有说明的情况除外”。

| 平台 | Google 10 月 27 日公告中的构建版本 |
|---|---|
| **Windows** | 156.0.8078.73 或 156.0.8078.74 |
| **macOS** | 156.0.8078.73 或 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*此表仅适用于 10 月 27 日的版本，不是永久目标版本。后续安全更新请查看当前的 [Chrome Releases 信息流](https://chromereleases.googleblog.com/)。* Google 表示，桌面版推出需要“未来几天或几周”，Android 构建版本将在接下来几天内进入 Google Play。即使更新正在分阶段推出，版本低于表中编号的设备仍需检查。([桌面版通知](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)，[Android 通知](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

[桌面版安全修复列表](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)将四个已报告的问题标为 **Critical**：FileSystem 内存损坏 [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306)、FileAPI 输入验证不当 CVE-2026-118331、Skia 输入验证不当 CVE-2026-118348，以及 Layout use-after-free CVE-2026-118344。同一通知还列出了其他 **High** 和 **Medium** 级 CVE。52 表示此版本包含的安全修复数量，并不表示有 52 起经独立验证的漏洞利用报告。([NVD 记录](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**版本通知没有声称所列漏洞正遭到主动利用。**警告针对的是信息披露时间：“在大多数用户收到修复之前，问题详情和链接的访问权限可能会受到限制。”不要把问题详情访问受限当作漏洞遭到利用的证据。([桌面版通知](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## 检查并完成桌面更新

1. 在你使用的 Chrome 安装中打开 **`chrome://version`**。记录完整版本和操作系统，不要只记录主版本号 156。其他渠道或其他位置安装的 Chrome 窗口需要单独检查。
2. 打开 **`chrome://settings/help`**，或选择 **更多 > 帮助 > 关于 Google Chrome**。Google 表示，Chrome 会在此页面检查更新。等待检查完成。([Google 桌面更新说明](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. 如果页面提供 **重新启动**，请选择该选项。先保存未完成的工作。关闭其他 Chrome 窗口，重新打开浏览器，再次检查 **`chrome://version`**。将重启后显示的版本与平台表格进行比较。
4. 如果版本仍低于公告中的构建版本，请再次检查是否有可用更新。如果组织管理此浏览器，或更新程序报告错误，请联系管理员。下载成功并不能证明正在运行的浏览器版本已更改。

> **预期结果：**重启后，正在运行的 Chrome Stable 构建版本应达到 10 月 27 日公告中适用于该平台的版本，或供应商后来公告的更高版本。仍在等待点击的“重新启动”按钮并不代表更新已完成。

在 **Android** 上，打开 Play Store > 个人资料图标 > 管理应用和设备，然后在“可用更新”下更新 Chrome（如果出现）。在 Chrome 中，打开“更多”>“设置”>“关于 Chrome”以查看已安装版本。应用更新完成后，将其与 Android 表格行进行比较。这些菜单路径遵循 [Google 的 Android 说明](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en)。

## 检查受管理的设备群

对于已注册的浏览器，请使用 Google 管理控制台中的 **Chrome versions report**，按操作系统查找较旧的构建版本。打开 Browser Versions 视图，选择相关组织单位，检查完整的次版本号；如果需要逐台处理清单，请导出 CSV。Google 表示，该报告包含过去 28 天内提交过报告的浏览器。Google 还提示报告可能延迟，尤其是在大型设备群中。([查看 Chrome 版本详情](https://support.google.com/chrome/a/answer/10025748?hl=en))

**将报告的清单与实时验证分开。**检查每台设备的最后报告时间和渠道，然后直接在浏览器中或通过受管理终端清单确认异常情况。Google 会分别统计 Stable 和 Beta 等不同的 Chrome 安装。浏览器报告需要先注册，并启用[受管理浏览器报告](https://support.google.com/chrome/a/answer/9301421?hl=en)。设备未出现在报告中，并不能证明它已安装补丁。

## 单独检查 Chromium 衍生浏览器

**Chrome 版本表适用于 Google Chrome。**Microsoft Edge、Brave 和其他基于 Chromium 的浏览器拥有各自的软件包、版本号和更新计划。Chrome 公告不能确认这些浏览器的补丁状态。请检查每个浏览器的已安装版本，以及其自身针对相关 Chromium 修复发布的安全公告或版本说明。不要将 Edge 或 Brave 的产品版本直接与 Chrome 156.0.8078.73 比较后就断定已修复。

对于每个衍生浏览器，记录产品名称、渠道、已安装构建版本、供应商公告 URL，以及供应商指出的已修复构建版本。如果供应商尚未确认修复，请将状态标记为**未验证**，并遵循指定供应商的更新说明。在清单中将 Chrome 和衍生浏览器的结果分开记录。

## 来源和参考资料

- [Chrome Releases：2026 年 10 月 27 日桌面 Stable Channel 更新](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)。桌面构建版本、52 项修复、CVE 以及供应商关于信息披露的表述。
- [Chrome Releases：2026 年 10 月 27 日 Android Chrome 更新](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html)。Android 构建版本及关于相应桌面修复的说明。
- [Chromium 问题跟踪器：M156 安全修复查询](https://issues.chromium.org/issues?q=customfield1223088:1-M156)。链接来自桌面版通知。能否访问单个问题详情取决于披露限制。
- [NVD：CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) 和 [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331)。漏洞说明和受影响的 Chrome 版本。上文严重级别依据 Google 通知，并非 NVD 的 CVSS 评估。
- [Google Chrome 帮助：在计算机上更新 Chrome](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) 及[在 Android 上更新](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en)。更新检查方式和版本菜单路径。
- [Chrome Enterprise 帮助：查看 Chrome 版本详情](https://support.google.com/chrome/a/answer/10025748?hl=en) 及[启用受管理浏览器报告](https://support.google.com/chrome/a/answer/9301421?hl=en)。设备群报告的前提条件和限制。
