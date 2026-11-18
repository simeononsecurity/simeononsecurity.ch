---
title: "SSL と TLS 1.1 以前を無効にしてコンピューターのセキュリティを強化する"
date: 2023-02-08
lastmod: 2026-11-14
toc: true
draft: false
description: "TLS 1.2 以降を維持しながら、SSL と古い TLS バージョンを無効にします。Windows の Schannel、.NET、Linux サービスを扱います。"
tags: ['コンピューターのセキュリティ強化', 'SSL と TLS の無効化', 'データセキュリティ', 'POODLE', 'BEAST', 'Heartbleed', 'Windows レジストリエディター', 'Linux の OpenSSL 設定', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "データセキュリティを表す南京錠のマークが付いたコンピューター"
coverCaption: ""
---

## はじめに:

コンピューターは日常生活に欠かせないものとなり、データを保護する必要性も高まっています。SSL（Secure Socket Layer）と TLS（Transport Layer Security）は、通信中のデータを保護するために広く使われています。古いバージョンはサイバー攻撃に対して脆弱です。この記事では、TLS 1.2 または TLS 1.3 を利用可能な状態に保ちつつ、SSL と TLS 1.0、1.1 を無効にする方法を説明します。

*TLS 1.2 は廃止されたプロトコルではありません。現在の最低基準は TLS 1.2 以降です。[RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) は TLS 1.3 を定義し、[RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) は TLS 1.0 と TLS 1.1 を正式に非推奨としています。*

### SSL と TLS 1.1 以前を無効にする理由

古い SSL と TLS には、POODLE（Padding Oracle On Downgraded Legacy Encryption）、BEAST（Browser Exploit Against SSL/TLS）、Heartbleed などの脅威があります。これらの攻撃は機密情報を漏えいさせる恐れがあります。Heartbleed は脆弱な OpenSSL 実装に影響したもので、プロトコルのバージョンではありません。ライブラリに修正を適用し、漏えいした可能性のある認証情報を変更してください。

Microsoft の最新の [Schannel レジストリ設定ガイダンス](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings)には、サポート対象 Windows のプロトコル設定が記載されています。Microsoft は、利用可能な場合、グループポリシーなどのサポート対象管理ツールを推奨しています。より適切な制御手段がない場合に限り、レジストリを直接編集してください。

### Windows で SSL と TLS 1.1 以前を無効にする：

Windows ではレジストリエディターでこれらのプロトコルを無効にできます。次の PowerShell スクリプトは、Schannel のクライアントとサーバーの設定を変更します。また、.NET が OS の TLS 既定値と強力な暗号化を使うように設定します。

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
# SSL v2 を無効化
Disable-Protocol -Protocol "SSL 2.0"
# SSL v3 を無効化
Disable-Protocol -Protocol "SSL 3.0"
# TLS 1.0 を無効化
Disable-Protocol -Protocol "TLS 1.0"
# DTLS 1.0 を無効化
Disable-Protocol -Protocol "DTLS 1.0"
# TLS 1.1 を無効化
Disable-Protocol -Protocol "TLS 1.1"
# DTLS 1.1 プロトコルはありません。RFC 8996 は DTLS 1.0 を非推奨とし、DTLS 1.2 を維持しています。

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

#### Linux で SSL と TLS 1.1 以前を無効にする：

Linux で古いプロトコルを無効にする方法は、アプリケーションとライブラリによって異なります。`/etc/ssl/openssl.cnf` を変更しても、すべてのデーモンや同梱 TLS ライブラリの設定が上書きされるわけではありません。次の手順に従います。

1. 端末を開き、root としてログインします。
2. OpenSSL の設定ファイルに移動します。通常は /etc/ssl/openssl.cnf にあります。
3. nano や vim などのテキストエディターでファイルを開きます。
4. サービスのプロトコル指示を探し、最低バージョンを TLS 1.2 に設定します。古い `-TLSv1.2` 指示は TLS 1.2 を無効にするため、現在の最低基準として使わないでください。
5. ファイルを保存し、エディターを閉じます。
6. 変更を反映するため、Apache や Nginx など OpenSSL を使うサービスを再起動します。

## 結論

SSL と TLS 1.1 以前を無効にすると、最新の TLS クライアントとの互換性を保ちながらコンピューターの安全性を高められます。設定する場所は TLS 接続をネゴシエートするサービスです。1 つの OpenSSL ファイルですべてのデーモンを制御できると考えず、各アプリケーションをテストしてください。

古いバージョンを無効にすると、一部の旧システムとの互換性に影響する場合があります。全面導入の前に変更を十分にテストし、悪影響がないことを確認してください。

機密情報を守り、攻撃のリスクを抑えるため、各サービスがネゴシエートするプロトコルを確認し、一時的な例外を記録してください。

## 現在の確認リスト

- **ネゴシエートされたプロトコルを確認します。** TLS スキャナーまたは承認済みの内部テストを使い、接続の両端でクライアントとサーバーをテストします。
- **TLS 1.2 を有効のままにします。** 古いアプリケーションの中には依然として必要とするものがあります。TLS 1.3 の対応状況は OS とライブラリによって異なります。
- **DTLS は別に確認します。** RFC 8996 は DTLS 1.0 を非推奨としています。DTLS 1.1 は定義していません。
- **影響を受けるサービスを再起動します。** Schannel やアプリケーションの設定は、サービスまたはシステムの再起動後に反映される場合があります。
- **例外を記録します。** 一時的な互換設定が必要な旧エンドポイントを記録し、廃止日を決めます。
