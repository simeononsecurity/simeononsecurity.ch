---
title: "Thunderbird 153.6：Windows NTLM 凭据泄露与更新方法（2026）"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "显示特制邮件时，Thunderbird 的两项严重漏洞可能泄露 Windows NTLM 身份验证数据。本文介绍两种触发路径、版本检查方法，以及更新期间限制出站 SMB 的措施。"
genre: ["网络安全", "电子邮件安全", "Windows 安全"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "Thunderbird 安全更新", "Thunderbird Windows 漏洞", "Thunderbird NTLM 泄露", "Thunderbird SMB 身份验证", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "OpenPGP 密钥附件", "外部附件", "阻止远程内容", "mailbox URL", "扩展长度 UNC 路径", "Windows 帐户名", "NTLM 身份验证数据", "SMB 凭据泄露", "出站 SMB", "TCP 端口 445", "电子邮件安全", "Windows 邮件客户端", "检查 Thunderbird 版本", "更新 Thunderbird", "NTLM 中继", "离线密码破解"]
cover: ""
coverAlt: ""
coverCaption: ""
---

Mozilla 在 Thunderbird 153.6 中修复了两项**可能泄露 Windows 凭据的严重漏洞**。只需显示一封特制邮件，就可能触发 [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/) 描述的网络请求之一。该公告说明的是 NTLM 数据可能泄露，并未确认每位收件人的凭据都遭到入侵。

<!--more-->

## 要点

- **CVE-2026-118174** 涉及托管在外部的 OpenPGP 密钥附件。即使已阻止远程内容，显示邮件仍会在无需用户操作的情况下发出请求。
- **CVE-2026-118176** 涉及使用扩展长度 UNC 路径的特殊 `mailbox:` URL。显示邮件会连接到发件人指定的 SMB 服务器。
- **更新 Windows 上的 Thunderbird**，并核实已安装版本。公告将 Thunderbird 153.6 列为修复版本。Thunderbird 发行说明指出对应的 153.6.0esr 构建。

## 邮件会触发什么

**这两项漏洞的入口不同。** 根据 Mozilla 的说明，两者都不要求收件人点击邮件中的链接。Windows 凭据风险取决于网络请求是否到达攻击者控制的共享资源，以及后续是否发生身份验证交换。Mozilla 的公告没有报告正在发生的利用活动。

| 问题 | 显示邮件时的触发操作 | Windows 凭据风险 |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbird 加载 OpenPGP 密钥附件的内容，以提供密钥导入选项。发件人将其标记为外部附件，并指定攻击者选择的 URL。 | 如果指向网络共享的请求到达该共享，用户的 NTLM 凭据就会泄露。 |
| **CVE-2026-118176** | 扩展长度 UNC 路径绕过 Thunderbird 对 `mailbox:` URL 中远程共享的限制。 | Thunderbird 连接到攻击者指定的 SMB 服务器，并泄露 Windows 帐户名和 NTLM 身份验证数据。 |

对于 **OpenPGP 附件**路径，Mozilla 明确表示该请求绕过了远程内容阻止设置，且无需用户操作。在非 Windows 系统上，此问题也会违反远程内容设置发出远程请求，但 Mozilla 将 NTLM 凭据泄露限定为 Windows。对于 **`mailbox:` URL**路径，Mozilla 表示其他操作系统不受影响。请参阅 [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) 和 [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176) 的单独条目。

**NTLM 身份验证数据不是明文密码。** Mozilla 表示，通过 SMB 路径泄露的数据会带来离线密码破解或中继攻击风险。仅仅收到一封特制邮件，并不能证明攻击成功。公告还列出 Thunderbird 的其他漏洞，包括日历和 RSS 的独立路径。本文讨论上述两种由显示邮件触发的路径，不把该版本的所有问题混为一谈。

## 检查并更新 Thunderbird

受影响的操作是修复发布前在 Windows 上**使用 Thunderbird 阅读邮件**。Mozilla 将 **Thunderbird 153.6** 列为修复版本，但没有给出这两项问题完整的最早受影响版本范围。[153.6.0esr 发行说明](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)指出 ESR 构建于 2026 年 10 月 27 日发布。不要仅凭版本标签推断其他发布渠道、分支或重新打包版本是否已包含补丁。

1. 在 Windows 中打开 **Help > About Thunderbird**。查看 About 窗口显示的版本。该窗口也会检查更新。Mozilla 的[更新说明](https://support.mozilla.org/en-US/kb/updating-thunderbird)介绍了此操作。
2. 如果有更新，让 Thunderbird 下载，然后选择 **Restart Thunderbird to Update**。重新启动后，再次打开 **Help > About Thunderbird**，确认已安装的版本。
3. 对于 **153 ESR 系列**，将当前版本与 Thunderbird 发行说明中的 **153.6.0esr** 对照。如果组织统一管理更新，请让管理员核实厂商修复是否已部署，不要假设更新已经安装。

> **版本说明：** 153.6.0esr 发行说明确认该版本已发布。MFSA 2026-122 将安全修复关联到 Thunderbird 153.6。发行说明没有逐一描述这两项 CVE。漏洞细节请以安全公告为准。

## 更新期间降低风险

**先安装厂商修复。** 仅关闭远程内容无法阻止 CVE-2026-118174，因为相关请求绕过了此设置。“不要点击”不足以解决问题。Mozilla 描述的请求会在显示邮件时触发。

作为**纵深防御措施**，在企业防火墙或受管理终端上限制 Windows 客户端发往互联网的 SMB 流量，包括 **TCP 端口 445**。Microsoft 的 [SMB 流量指南](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)建议阻止发往互联网的出站 TCP 445，并限制对必要文件服务器的访问。实施规则前先盘点所需共享资源，尤其是环境使用云文件服务或有边界外远程员工时。此网络控制能够限制上述 SMB 路径，但无法修复 Thunderbird，也不能解决公告中的所有远程请求问题。

如果运行旧版 Thunderbird 的 Windows 计算机显示过可疑邮件，**应将潜在暴露视为待调查事项，而非遭到入侵的证据**。与安全团队一起检查可用的出站 SMB 连接记录和身份验证日志。厂商公告没有提供暴露检测工具，也没有要求一律更改所有密码。

## 来源

- [Mozilla Foundation Security Advisory 2026-122：Thunderbird 153.6 修复的安全漏洞](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Thunderbird Desktop 发行说明：153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support：将 Thunderbird 更新到最新版本](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn：保护 Windows Server 中的 SMB 流量](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
