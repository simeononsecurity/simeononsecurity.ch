---
title: "Chrome 156 セキュリティ更新: 10月の修正を確認する"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Windows、macOS、Linux、Android で10月27日の Chrome 156 セキュリティリリースを確認します。インストール済みのビルドを比較し、保留中の再起動を完了して、管理対象端末を個別に確認します。"
genre: ["ブラウザー", "セキュリティ", "パッチ管理"]
tags: ["Chrome 156", "Chrome セキュリティ更新", "Chrome パッチ確認", "Chrome バージョン確認", "Windows 版 Chrome 156", "macOS 版 Chrome 156", "Linux 版 Chrome 156", "Android 版 Chrome 156", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "ブラウザーパッチ", "Chrome Enterprise Core", "管理対象ブラウザー", "Chromium セキュリティ", "ブラウザー更新", "Chrome の再起動", "chrome://version", "chrome://settings/help", "Android 版 Chrome の更新", "Brave セキュリティ更新", "Edge セキュリティ更新"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "セキュリティ更新を表す南京錠と盾のイラスト。Chrome のバージョン画面ではありません"
coverCaption: ""
---

**2026年10月27日の Chrome セキュリティリリース**には52件の修正が含まれます。インストールを確認するには、完全なバージョン番号をお使いの OS 向けリリースと比較し、Chrome を再起動して保留中の更新を完了します。バージョンが発表されても、端末に更新が届いた証拠にはなりません。([Chrome デスクトップ版リリース](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## 表示されるべきバージョン

Google は2026年10月27日に、次の Stable チャネル版を公開しました。デスクトップ版リリースには Windows と macOS 用のビルド、および Linux 用のビルドが記載されています。[Android 版リリース](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html)には個別のビルドが記載され、Android 版にも、特に明記されない限り、対応するデスクトップ版と同じセキュリティ修正が含まれると説明されています。

| プラットフォーム | 10月27日の Google 発表に記載されたビルド |
|---|---|
| **Windows** | 156.0.8078.73 または 156.0.8078.74 |
| **macOS** | 156.0.8078.73 または 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*この表は10月27日リリースの確認に使い、恒久的な目標バージョンとして扱わないでください。今後のセキュリティ更新は、最新の[Chrome リリースフィード](https://chromereleases.googleblog.com/)で確認してください。* Google は、デスクトップ版の展開に「今後数日から数週間」かかり、Android 版ビルドは数日以内に Google Play に届くと説明しました。段階的な展開中でも、表のバージョンより古い端末は確認が必要です。([デスクトップ版の告知](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)、[Android 版の告知](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

[デスクトップ版のセキュリティ修正一覧](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)では、報告された4件の不具合が **Critical** に分類されています。FileSystem のメモリ破損 [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306)、FileAPI の不適切な入力検証 CVE-2026-118331、Skia の不適切な入力検証 CVE-2026-118348、Layout の use-after-free CVE-2026-118344 です。同じ告知には **High** と **Medium** の CVE も記載されています。52という数字はリリースに含まれるセキュリティ修正数を示し、独立して検証された悪用報告が52件あるという意味ではありません。([NVD の記録](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**リリース告知は、列挙された脆弱性が現在悪用されているとは述べていません。**注意事項は情報公開の時期に関するものです。「大半のユーザーが修正を受け取るまで、バグの詳細やリンクへのアクセスが制限される場合があります。」詳細へのアクセス制限を悪用の証拠と見なさないでください。([デスクトップ版の告知](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## デスクトップ更新を確認して完了する

1. 使用している Chrome のインストールで **`chrome://version`** を開きます。メジャーバージョン 156 だけでなく、完全なバージョンと OS を記録してください。別のチャネルや別の場所にインストールされた Chrome のウィンドウは個別に確認します。
2. **`chrome://settings/help`** を開くか、**その他 > ヘルプ > Google Chrome について**を選択します。Google によると、このページで Chrome が更新を確認します。確認が終わるまで待ちます。([Google のデスクトップ更新手順](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. ページに表示されたら **再起動**を選択します。先に未保存の作業を保存してください。残っている Chrome ウィンドウを閉じ、ブラウザーを再度開いてから、もう一度 **`chrome://version`** を確認します。再起動後に表示されたバージョンを表と比較してください。
4. バージョンが発表されたビルドより古い場合は、再度更新を確認します。組織がブラウザーを管理している場合や、更新ツールがエラーを報告した場合は、管理者に連絡してください。ダウンロードが成功しても、実行中のブラウザーバージョンが変わった証拠にはなりません。

> **期待される結果:** 再起動後、実行中の Chrome Stable ビルドが10月27日の告知に記載されたプラットフォーム別バージョン、またはベンダーが後日発表したバージョンになります。再起動ボタンが保留中の状態は、完了の証拠ではありません。

**Android** では Play ストア > プロフィール アイコン > アプリとデバイスの管理を開き、利用可能なアップデートに Chrome があれば更新します。Chrome でその他 > 設定 > Chrome についてを開くと、インストール済みのバージョンを確認できます。アプリの更新完了後に表の Android 行と比較してください。これらのメニュー経路は[Google の Android 向け手順](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en)に基づきます。

## 管理対象の端末群を確認する

登録済みブラウザーについては、Google 管理コンソールの **Chrome バージョン レポート**を使い、OS ごとに古いビルドを探します。Browser Versions ビューを開き、対象の組織部門を選択して、完全なマイナーバージョンを確認します。端末ごとの作業一覧が必要な場合は CSV をエクスポートします。Google によると、このレポートには過去28日間にレポートを送信したブラウザーが含まれます。大規模な端末群では特に報告が遅れる可能性があります。([Chrome バージョンの詳細を表示](https://support.google.com/chrome/a/answer/10025748?hl=en))

**レポート上のインベントリと稼働中の確認を分けてください。**各端末の最終レポート時刻とチャネルを確認し、例外はブラウザーまたは管理対象エンドポイントのインベントリで直接確認します。Google は Stable や Beta など別々の Chrome インストールを個別に数えます。ブラウザーレポートには登録と[管理対象ブラウザー レポート](https://support.google.com/chrome/a/answer/9301421?hl=en)の有効化が必要です。レポートにない端末を、修正済みと判断する根拠にはできません。

## Chromium 派生ブラウザーを個別に確認する

**Chrome のバージョン表は Google Chrome に適用されます。**Microsoft Edge、Brave、その他の Chromium ベースのブラウザーには、独自のパッケージ、リリース番号、更新スケジュールがあります。Chrome の発表から、これらのパッチ適用状況は確認できません。各ブラウザーのインストール済みバージョンと、関連する Chromium 修正についての独自のセキュリティ勧告またはリリースノートを確認してください。Edge や Brave のバージョンを Chrome 156.0.8078.73 と直接比較して、修正済みと判断しないでください。

派生ブラウザーごとに、製品名、チャネル、インストール済みビルド、ベンダー勧告の URL、ベンダーが修正済みと示すビルドを記録します。ベンダーが修正を確認していない場合は、状態を **未確認** とし、指定されたベンダーの更新手順に従います。Chrome と派生ブラウザーの結果は、インベントリの別々の行に記録してください。

## 情報源と参考資料

- [Chrome Releases: デスクトップ版 Stable Channel 更新、2026年10月27日](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html)。デスクトップ版ビルド、52件の修正、CVE、情報公開に関するベンダーの文言。
- [Chrome Releases: Android 版 Chrome 更新、2026年10月27日](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html)。Android 版ビルドと対応するデスクトップ版修正についての注記。
- [Chromium Issue Tracker: M156 セキュリティ修正の検索](https://issues.chromium.org/issues?q=customfield1223088:1-M156)。デスクトップ版の告知からリンクされています。個別の不具合詳細へのアクセスは情報公開の制限によります。
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) と [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331)。脆弱性の説明と影響を受ける Chrome バージョン。上記の深刻度は Google の告知に基づき、NVD の CVSS 評価ではありません。
- [Google Chrome ヘルプ: パソコンで Chrome を更新](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) と[Android での更新](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en)。更新確認とバージョン表示のメニュー経路。
- [Chrome Enterprise ヘルプ: Chrome バージョンの詳細を表示](https://support.google.com/chrome/a/answer/10025748?hl=en) と[管理対象ブラウザー レポートを有効にする](https://support.google.com/chrome/a/answer/9301421?hl=en)。端末群のレポートに関する前提条件と制限。
