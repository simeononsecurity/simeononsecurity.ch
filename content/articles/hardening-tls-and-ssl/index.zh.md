---
title: "禁用 SSL 和 TLS 1.1 及更早版本以加固计算机安全"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "停用 SSL 和旧版 TLS，同时保留 TLS 1.2 或更新版本。本文介绍 Windows Schannel、.NET 和 Linux 服务。"
tags: ['加固计算机安全', '禁用 SSL 和 TLS', '数据安全', 'POODLE', 'BEAST', 'Heartbleed', 'Windows 注册表编辑器', 'Linux OpenSSL 配置', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "带有挂锁图标、象征数据安全的计算机"
coverCaption: ""
---

## 简介:

计算机已成为日常生活的重要部分，数据安全需求也随之增长。SSL（安全套接层）和 TLS（传输层安全）常用于保护传输中的数据。随着技术发展，这些协议的旧版本容易受到网络攻击。本文说明如何停用 SSL 和 TLS 1.0、1.1，同时保留 TLS 1.2 或 TLS 1.3。

*TLS 1.2 并非过时协议。当前最低基线为 TLS 1.2 或更新版本。[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) 定义了 TLS 1.3，[RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) 则正式弃用 TLS 1.0 和 TLS 1.1。*

### 为什么要禁用 SSL 和 TLS 1.1 及更早版本？

旧版 SSL 和 TLS 容易受到 POODLE（降级遗留加密填充预言攻击）、BEAST（针对 SSL/TLS 的浏览器漏洞利用）和 Heartbleed 等安全威胁影响。这些攻击可能泄露敏感信息，因此应停用旧协议。Heartbleed 影响的是存在漏洞的 OpenSSL 实现，本身并非协议版本。请修补该库，并轮换可能已泄露的凭据。

Microsoft 当前的 [Schannel 注册表指南](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings)列出了受支持 Windows 版本的协议设置。Microsoft 建议在可用时使用组策略或其他受支持的管理工具。只有在没有更合适控制方式时才直接编辑注册表。

### 在 Windows 中禁用 SSL 和 TLS 1.1 及更早版本：

在 Windows 中，可通过注册表编辑器禁用这些协议。以下 PowerShell 脚本会更改 Schannel 的客户端和服务器设置，也会将 .NET 配置为使用操作系统的 TLS 默认值和强加密。

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### 在 Linux 中禁用 SSL 和 TLS 1.1 及更早版本：

在 Linux 中，禁用旧协议的方式取决于应用程序和库。修改 `/etc/ssl/openssl.cnf` 不会覆盖每个守护进程或捆绑 TLS 库的设置。请按以下步骤操作：

1. 打开终端并以 root 身份登录。
2. 找到 OpenSSL 配置文件，通常位于 /etc/ssl/openssl.cnf。
3. 使用 nano 或 vim 等文本编辑器打开文件。
4. 找到服务的协议指令，并将最低版本设为 TLS 1.2。旧的 `-TLSv1.2` 指令会禁用 TLS 1.2，因此不要将其用作现代基线。
5. 保存文件并关闭文本编辑器。
6. 重启使用 OpenSSL 的服务，例如 Apache 或 Nginx，使更改生效。

## 结论：

禁用 SSL 和 TLS 1.1 及更早版本可加固计算机安全，同时兼容现代 TLS 客户端。正确的设置位于协商 TLS 的服务中。请逐个测试应用程序，不要假设一个 OpenSSL 文件能够控制所有守护进程。

禁用这些旧版本可能影响与部分旧系统的兼容性。全面实施前请充分测试变更，并确认系统没有受到不利影响。

请按照本文步骤保护敏感信息并降低攻击风险。先确认每项服务协商使用的协议，再记录临时例外。

## 当前验证清单

- **确认协商的协议。** 使用 TLS 扫描器或获批的内部测试，在连接两端分别测试客户端和服务器。
- **保持 TLS 1.2 启用。** 部分旧应用仍需要它，而 TLS 1.3 的支持取决于操作系统和库。
- **单独检查 DTLS。** RFC 8996 弃用 DTLS 1.0，并未定义 DTLS 1.1 协议。
- **重启受影响的服务。** Schannel 和应用设置通常需要重启服务或系统才能应用新策略。
- **记录例外。** 记录仍需临时兼容设置的旧端点，并指定移除日期。
