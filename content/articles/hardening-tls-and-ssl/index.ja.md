---
title: "SSLとTLS 1.2以下を無効にして、コンピュータのセキュリティを強化する"
date: 2023-02-08
toc: true
draft: false
description: "POODLE、BEAST、Heartbleedなどのサイバー脅威に弱い旧バージョンのSSLおよびTLSプロトコルをWindowsおよびLinuxシステムで無効化し、データセキュリティを向上する手順について説明します。"
tags: ["コンピュータセキュリティの強化", "SSLおよびTLSの無効化", "データセキュリティ", "ポードル", "ビースト", "ハートブリード", "Windowsレジストリエディタ", "LinuxのOpenSSL設定", "アパッチ", "エヌジンクス"]
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.png"
coverAlt: "データの安全性を表す南京錠のマークが描かれたパソコン"
coverCaption: ""
---

## はじめに

コンピューターは私たちの日常生活に欠かせないものとなり、それに伴い、データセキュリティの必要性も大きく高まっています。転送中のデータを保護するために使用される様々な方法の中で、SSL（Secure Socket Layer）とTLS（Transport Layer Security）は広く使われているプロトコルです。しかし、技術の進化に伴い、これらのプロトコルの古いバージョンはサイバー攻撃に対して脆弱になりつつあります。今回は、データの安全性を保つために、SSLとすべてのTLSバージョン1.2以下を無効にしてコンピューターを堅牢化する手順について説明します。

### なぜSSLとTLS 1.2以下を無効化するのか？

古いバージョンのSSLとTLSは、POODLE（Padding Oracle On Downgraded Legacy Encryption）、BEAST（Browser Exploit Against SSL/TLS）、Heartbleedなどのセキュリティ脅威に対して脆弱性がある。これらの攻撃は、機密情報の漏洩につながる可能性があるため、古いプロトコルの使用を無効にすることが重要です。

### Windows で SSL および TLS 1.2 以下を無効にする：

Windowsでは、SSLとTLS 1.2以下を無効にするプロセスは、レジストリエディタで実現できます。以下は、このタスクを実行するためのpowershellスクリプトです：

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
# Disable DTLS 1.1
Disable-Protocol -Protocol "DTLS 1.1"

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

#### Linux で SSL および TLS 1.2 以下を無効化する：

Linuxでは、OpenSSLの設定ファイルを変更することで、SSLおよびTLS 1.2以下を無効にするプロセスを実現できます。以下はその手順です：

1.ターミナルを開き、rootでログインします。
2.OpenSSLの設定ファイルに移動します。通常、/etc/ssl/openssl.cnfに配置されています。
3.nano や vim などのテキストエディタを使用してファイルを開きます。
4.SSLProtocolディレクティブを探し、その値を-TLSv1.2に設定します。
5.5.ファイルを保存し、テキストエディタを閉じます。
6.6.変更を有効にするために、ApacheやNginxなどのOpenSSLを使用するサービスを再起動します。

## 結論

SSLとすべてのTLSバージョン1.2以下を無効にすることで、コンピュータのセキュリティを強化し、潜在的なサイバー脅威から機密情報を保護することができます。このプロセスは簡単で、最小限の労力で達成できるため、コンピュータのセキュリティを維持する上で重要な要素になります。この記事で紹介した手順を実行することで、データの安全性を保ち、サイバー攻撃を防ぐことができ、機密情報が漏洩するリスクを低減することができます。

ただし、これらの旧バージョンのSSLおよびTLSプロトコルを無効にすると、コンピュータのセキュリティが向上する一方で、一部の旧システムとの互換性に影響を与える可能性があることに注意してください。そのため、変更を完全に実行する前に、変更内容を十分にテストし、システムに悪影響がないことを確認することが重要です。

結論として、SSLとすべてのTLSバージョン1.2以下を無効にしてコンピュータを強化することは、機密情報のセキュリティを維持し、サイバー攻撃を防ぐための重要なステップとなります。この記事で紹介した手順は、コンピュータのセキュリティを確保するためのわかりやすいガイドであり、個人や組織が必要なセキュリティ対策を簡単に実施することができます。