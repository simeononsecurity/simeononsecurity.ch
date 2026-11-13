---
title: "Thunderbird 153.6: WindowsでのNTLM認証情報漏えいと更新方法 (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "細工されたメールを表示すると、2つの重大なThunderbirdの脆弱性によりWindowsのNTLM認証データが漏えいするおそれがあります。2つの仕組み、バージョンの確認方法、更新中に送信SMBを制限する方法を説明します。"
genre: ["サイバーセキュリティ", "メールセキュリティ", "Windowsセキュリティ"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "Thunderbirdセキュリティ更新", "Thunderbird Windows脆弱性", "Thunderbird NTLM漏えい", "Thunderbird SMB認証", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "OpenPGP鍵添付ファイル", "外部添付ファイル", "リモートコンテンツのブロック", "mailbox URL", "拡張長UNCパス", "Windowsアカウント名", "NTLM認証データ", "SMB認証情報漏えい", "送信SMB", "TCPポート445", "メールセキュリティ", "Windowsメールクライアント", "Thunderbirdバージョン確認", "Thunderbird更新", "NTLMリレー", "オフラインパスワード解析"]
cover: ""
coverAlt: ""
coverCaption: ""
---

MozillaはThunderbird 153.6で、**Windowsの認証情報を漏えいさせる重大な脆弱性**を2件修正しました。細工されたメールを表示するだけで、[MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)に記載されたネットワークリクエストのいずれかが発生する可能性がありました。この勧告が述べているのはNTLMデータが漏えいする可能性であり、すべての受信者の認証情報が侵害されたという確認ではありません。

<!--more-->

## 要点

- **CVE-2026-118174**は、外部ホストされたOpenPGP鍵の添付ファイルに関する問題です。リモートコンテンツをブロックしていても、メッセージを表示するとユーザー操作なしでリクエストが発生しました。
- **CVE-2026-118176**は、拡張長UNCパスを使う特殊な`mailbox:` URLに関する問題です。メッセージを表示すると、送信者が指定したサーバーへのSMB接続が発生しました。
- **Windows版Thunderbirdを更新**し、インストール済みのバージョンを確認してください。勧告は修正済みバージョンとしてThunderbird 153.6を挙げています。Thunderbirdのリリースノートには対応する153.6.0esrビルドが記載されています。

## メールを表示すると何が起きるか

**2つの脆弱性は入口が異なります。** Mozillaの説明によると、どちらも受信者がメール内のリンクをクリックする必要はありません。Windows認証情報のリスクは、ネットワークリクエストが攻撃者の管理する共有先に届き、その後の認証交換が行われるかどうかに左右されます。Mozillaは勧告で実際の悪用を報告していません。

| 問題 | メール表示時のトリガー | Windows認証情報へのリスク |
| --- | --- | --- |
| **CVE-2026-118174** | Thunderbirdが鍵のインポートを提示するため、OpenPGP鍵添付ファイルの内容を読み込みます。送信者は攻撃者が選んだURLを持つ外部添付ファイルとして指定します。 | ネットワーク共有を指すURLへのリクエストが共有先に届くと、ユーザーのNTLM認証情報が漏えいします。 |
| **CVE-2026-118176** | 拡張長UNCパスが、`mailbox:` URL内のリモート共有に対するThunderbirdの制限を回避します。 | Thunderbirdは攻撃者が選んだSMBサーバーに接続し、Windowsアカウント名とNTLM認証データを開示します。 |

**OpenPGP添付ファイル**の経路について、Mozillaはリクエストがリモートコンテンツのブロックを回避し、ユーザー操作も不要だったと明記しています。Windows以外のシステムでも、リモートコンテンツ設定に反してリモートリクエストが発生する問題はありましたが、MozillaがNTLM認証情報の漏えいを示しているのはWindowsに限られます。**`mailbox:` URL**の経路では、Mozillaによると他のOSは影響を受けません。[CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174)と[CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176)の各項目を参照してください。

**NTLM認証データは平文のパスワードではありません。** Mozillaによると、SMB経路で開示されたデータにはオフラインでのパスワード解析やリレー攻撃のリスクがあります。細工されたメッセージを受信しただけで攻撃成功が確定するわけではありません。勧告には、カレンダーやRSSに関する別経路など、Thunderbirdの他の脆弱性も記載されています。この記事は上記2つのメール表示経路を扱い、リリース内のすべての問題を同一視しません。

## Thunderbirdの確認と更新

影響を受けるのは、修正が適用される前に**Windows上のThunderbirdでメールを読む操作**です。Mozillaは修正済みとして**Thunderbird 153.6**を挙げていますが、この2件について最も古い影響対象バージョンの完全な範囲は示していません。[153.6.0esrのリリースノート](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)には、2026年10月27日に公開されたESRビルドが記載されています。別のチャンネル、フォーク、再パッケージ版のバージョン表記だけから、修正の適用状況を推測しないでください。

1. Windowsで**Help > About Thunderbird**を開きます。Aboutウィンドウに表示されたバージョンを確認してください。この画面は更新も確認します。Mozillaの[更新手順](https://support.mozilla.org/en-US/kb/updating-thunderbird)に、この方法が記載されています。
2. 更新が提示されたらThunderbirdにダウンロードさせ、**Restart Thunderbird to Update**を選びます。再起動後にもう一度**Help > About Thunderbird**を開き、インストール済みバージョンを確認します。
3. **153 ESR系列**では、表示されたバージョンをThunderbirdのリリースノートにある**153.6.0esr**と比較します。組織が更新を管理している場合は、すでに更新済みと決めつけず、管理者にベンダー修正の適用状況を確認してもらいます。

> **バージョンに関する注意:** 153.6.0esrのリリースノートは、このリリースが存在することを確認できます。MFSA 2026-122はセキュリティ修正をThunderbird 153.6に結び付けています。リリースノートはこの2件のCVEを個別には説明していません。脆弱性の詳細は勧告を参照してください。

## 更新中のリスクを抑える

**まずベンダーの修正をインストールしてください。** CVE-2026-118174ではリクエストが設定を回避したため、リモートコンテンツを無効にするだけでは止められません。「クリックしない」という助言だけでは不十分です。Mozillaの説明では、メッセージの表示時にリクエストが発生します。

**多層防御**として、企業ファイアウォールまたは管理対象端末で、**TCPポート445**を含むWindowsクライアントからインターネットへの送信SMBを制限します。Microsoftの[SMBトラフィックに関するガイダンス](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)は、インターネット向けの送信TCP 445をブロックし、必要なファイルサーバーへのアクセスを限定するよう推奨しています。ルールを適用する前に、必要な共有先を確認してください。クラウドファイルサービスや社外で働く利用者がいる環境では特に重要です。このネットワーク制御は説明されたSMB経路を制限しますが、Thunderbirdを修復するものではなく、勧告にあるすべてのリモートリクエストの問題を解決するものでもありません。

古いThunderbirdを実行するWindows端末で不審なメッセージを表示した場合、**漏えいは調査すべき可能性として扱い、侵害の証拠と決めつけないでください。** セキュリティチームとともに、利用可能な送信SMB接続記録や認証ログを確認します。ベンダー勧告には、露出を検査するテストも、すべてのパスワードを変更する一律の指示もありません。

## 出典

- [Mozilla Foundation Security Advisory 2026-122: Thunderbird 153.6で修正されたセキュリティ脆弱性](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Thunderbird Desktopリリースノート: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: Thunderbirdを最新バージョンに更新する](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: Windows ServerでSMBトラフィックを保護する](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
