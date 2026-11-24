---
title: "Kali Purple 2023.1：更新点と主な機能"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Kali Purple 2023.1の機能とツールを振り返り、現在のセキュリティラボ向け情報も紹介します。"
tags: ["Kali Linux", "Kali Purple", "2023.1", "倫理的ハッキング", "ペネトレーションテスト", "サイバーセキュリティ", "ツール", "エクスプロイトフレームワーク", "Kali ARMの更新", "Kali NetHunter", "Kaliのドキュメント", "カーネルのサポート", "Bluetoothのサポート", "LineageOS", "OneUI", "Radxa Zero", "シングルボードコンピューター", "カーネルパッチ", "コミュニティの貢献", "Kali Discord", "Linuxの更新", "倫理的ハッキング向けディストリビューション", "新機能", "改善点", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "新しいツールとパッケージ", "ARMデバイスのサポート", "Kaliのドキュメント", "政府の規制"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Kali Linuxの3Dアニメーションのドラゴンが、セキュリティツールに囲まれて盾の上に座っています。"
coverCaption: ""
---

**Kali Purple 2023.1：レビュー**

Kali Purple 2023.1は、Kaliの防御的セキュリティ方針を示す最初の技術プレビューでした。現在の最新リリースではありません。この記事では当時のリリースを記録し、2023.1のパッケージ版を現行版と誤解しないよう、現在の情報も示します。

## 現在のKaliの状況

Kaliの公式リリース履歴では、2026年6月29日に公開されたKali 2026.2が、2026年2番目のローリングリリースです。Linuxカーネル6.19とXfce 4.20.7を採用しています。[Kali 2026.2のリリースノート](https://www.kali.org/blog/kali-linux-2026-2-release/)では、GNOME 50、KDE Plasma 6.6、`sources.list`から`sources.list.d/kali.source`への移行、仮想マシンの起動変更についても説明しています。

Kali Purpleは、Kaliの中で防御とパープルチーム活動を重視する方向性です。2023.1の発表は、SOC-in-a-boxの参照アーキテクチャ、防御ツール、NIST Cybersecurity Frameworkに基づくメニュー分類を備えた技術プレビューとして紹介しました。これは当時の範囲を示す情報です。現在のパッケージを選ぶときは、Kaliの[メタパッケージ資料](https://www.kali.org/docs/general-use/metapackages/)を確認し、ラボに必要なツール群だけを選んでください。

*攻撃・防御を問わず、セキュリティ演習は隔離された許可済みのラボで行ってください。Kaliをインストールしても、所有または管理していないシステムをテストする許可は得られません。*

______

## Kali の壁紙とデスクトップの更新

Kali Purple 2023.1では、Kali Stickerという**新しいデフォルト壁紙**が導入され、紫の背景と様々なKali関連のステッカーが特徴です。この新しい壁紙は、/u/Albert-III-とTJ_Nullの作品にインスパイアされています。

新しい壁紙に加えて、Kali Purple 2023.1は、3つの主要なデスクトップ環境も更新します：**Xfce、KDE、およびGNOME**です。これらのアップデートには、新機能、パフォーマンスの向上、バグ修正が含まれています。

______

## Xfce 4.18

**Xfce 4.18**では、以下のようないくつかの注目すべき改良がなされています：

- UI のスケーリングのサポートが改善されました。
- Thunar ファイルマネージャの更新
- カスタマイズを容易にするパネルプロファイル

______

## KDE Plasma 5.27

**KDE Plasma 5.27** アップデートでは、以下を紹介します：

- 新しいウィンドウタイルシステム
- よりスタイリッシュなアプリテーマ
- よりクリーンでより使いやすいツールやウィジェット

______

## GNOME のアップデート

GNOMEについては、Kali Purple 2023.1では、F4キーを押すことでファイルマネージャのカレントフォルダにあるターミナルを素早く開くことができるなど、いくつかの使い勝手が向上しています。

______

## デフォルトのカーネル設定と既知の問題点

Kali Purple 2023.1 は、いくつかのカーネルのデフォルト値を更新し、より使いやすくしました。

______

## 新しいツールとパッケージ

Kali Purple 2023.1では、**ペネトレーションテスト**と**倫理的ハッキング**向けのツールやパッケージが追加されました。主な追加項目は次のとおりです。

- **Rizin 0.3.0**：最新のリバースエンジニアリングフレームワーク
- **Ghidra 10.1**：オープンソースのソフトウェアリバースエンジニアリングスイート
- **Python 3.10**：人気のプログラミング言語の最新版

これらのツールと既存パッケージの更新により、2023.1プレビューはセキュリティ専門家向けに拡張されました。この節のバージョンは2023.1のリリースを示し、Kali 2026.2に含まれるバージョンではありません。

______

## ARM デバイスのサポート

Kali Purple 2023.1は、ARMデバイスのサポートを拡大し続け、**Radxa Zero**のような新しいデバイスの互換性を追加し、**LG V20**のようなデバイスの既存のサポートを向上させました。この幅広いサポートにより、小さなシングルボードコンピュータから強力なスマートフォンまで、さまざまなハードウェアでKaliを使用することができます。

______

## ドキュメンテーションとコミュニティ

Kali チームは、ユーザーが Kali Purple 2023.1 を最大限に活用できるように、新しいガイド、チュートリアル、トラブルシューティングのヒントで **ドキュメント** を更新しました。また、オープンソースのコラボレーションとKaliコミュニティの強さを示すために、Kaliへの貢献のためにいくつかのコミュニティメンバーを認定しました。

______

## 政府規制

この記事では、倫理的ハッキングや侵入テストに関連する特定の政府規制は取り上げていませんが、これらの活動は多くの法域で規制されていることに留意することが重要です。セキュリティ評価を実施する際には、常に適切な許可を得ていることを確認し、適用される法律に従ってください。関連する規制の詳細については、以下のリソースを参照することを検討してください：

- [コンピュータ不正行為防止法（Computer Fraud and Abuse Act、CFAA）](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [一般データ保護規則（GDPR）](https://gdpr.eu/)

______

## 結論

**Kali Purple 2023.1**は、Kaliの防御的セキュリティ方針を示す最初のプレビューでした。ツール群の追加、ARM対応の改善、ドキュメントの拡充が行われました。現在の環境を構築する場合は、Kaliの最新リリースノートを確認し、ラボに合うパッケージを選んでください。適用される法律を守り、明示的な許可を得たシステムだけをテストしてください。

______

## 参考文献

1. [Kali Linux公式サイト](https://www.kali.org/)
2. [Kali Linux公式ドキュメント](https://www.kali.org/docs/)
3. [Kali Linuxダウンロード](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [General Data Protection Regulation (GDPR)](https://gdpr.eu/)

______

## 追加リソース

- [Kali Linux公式フォーラム](https://forums.kali.org/)
- [Kali Linuxブログ](https://www.kali.org/blog/)
- [Kali Linuxのトレーニングと認定](https://www.offensive-security.com/)

______

## 更新チェックリスト

- **リリース履歴を確認する。** イメージをダウンロードする前に、Kaliの[現在のリリース履歴](https://www.kali.org/releases/)を読みます。
- **公式イメージを使う。** [Get Kali](https://www.kali.org/get-kali/)からダウンロードし、公開されたチェックサムを検証します。
- **ローリングインストールを更新する。** 2023.1のリポジトリ例をそのまま使わず、Kaliの[最新の更新手順](https://www.kali.org/docs/general-use/updating-kali/)に従います。
- **メタパッケージを選ぶ。** 標準またはPurple向けのラボでも、Kaliの全パッケージは必要ありません。
- **ラボの範囲を記録する。** ツールを使う前に、許可されたシステム、テスト時間、ログ記録、後片付けを決めます。
