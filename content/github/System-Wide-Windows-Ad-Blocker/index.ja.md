---
title: "プライバシーとセキュリティを向上させる Windows 10 システム全体の広告ブロッカー スクリプト"
date: 2021-04-02
toc: true
draft: false
description: "システム全体の広告ブロックにホスト ファイルと Windows ファイアウォールを利用するこの強力な PowerShell スクリプトを使用して、Windows 10 で広告、トラッカー、テレメトリをブロックします。"
tags: ["ウィンドウズ10", "広告ブロッカー", "テレメトリのブロック", "PowerShell スクリプト", "システム全体の広告ブロック", "プライバシー", "安全", "イージーリスト", "簡単なプライバシー", "NoCoinフィルターリスト", "AdGuard DNS フィルター", "ヨーヨーリスト", "Peter Lowe の広告追跡マルウェア サーバー", "Windowsファイアウォール", "ドメインリスト", "Windows トラッカーをブロックする", "ブロックトラッカー", "広告をブロックする", "ブロック追跡"]
---

＃＃ 説明：
このスクリプトは、ホスト ファイルを介してテレメトリ関連のドメインをブロックし、Windows ファイアウォールを介して関連 IP をブロックします。

**ノート：**
- これらのドメインを追加すると、iTunes や Skype などの特定のソフトウェアが動作しなくなる可能性があります。
- Akamai に関連するエントリが Widevine DRM で問題を引き起こすことが報告されています

### 使用されるリスト:
-[EasyList](https://easylist.to/easylist/easylist.txt) / [JustDomains - EasyList](https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt)
-[Easy Privacy](https://easylist.to/easylist/easyprivacy.txt) / [JustDomains - EasyPrivacy](https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt)
-[NoCoin Filter List](https://github.com/hoshsadiq/adblock-nocoin-list/) / [JustDomains - NoCoin Filter List](https://justdomains.github.io/blocklists/lists/nocoin-justdomains.txt)
-[AdGuard DNS filter](https://github.com/AdguardTeam/AdguardSDNSFilter) / [JustDomains - AdGuard Simplified Domain Names Filter](https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt)
-[YoYo Lists](https://pgl.yoyo.org/adservers/serverlist.php)
-[Peter Lowe’s ad/tracking/malware servers](https://pgl.yoyo.org/adservers/policy.php)

＃＃＃ 例：

最新バージョンのスクリプトを自動的に実行します。
```powershell
iwr -useb 'https://raw.githubusercontent.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/main/sos-system-wide-windows-ad-block.ps1' | iex
```
