---
title: "システムセキュリティのためのWindows Defender PowerShellコマンド"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Windows Defender PowerShellコマンドのパワーを発見し、コマンドライン制御でシステムセキュリティを強化する方法を学びましょう。"
genre: ["Windows Defender", "PowerShellコマンド", "システムセキュリティ", "コマンドライン制御", "アンチウイルス", "Windowsオペレーティングシステム", "マルウェアプロテクション", "高度なセキュリティ設定", "セキュリティ運用の自動化", "Windows PowerShell"]
tags: ["テクノロジー", "サイバーセキュリティ", "オペレーティング・システム", "Windows", "コマンドラインツール", "システム・セキュリティ", "PowerShell", "アンチウイルス", "マルウェア対策", "スクリプト"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "さまざまなサイバー脅威からコンピュータシステムを守るシールドを描いたアニメーションイラスト。"
coverCaption: "Windows Defender PowerShell コマンドでシステムのセキュリティを強化。"
---

## はじめに

マイクロソフトによって開発されたWindows Defenderは、Windowsオペレーティングシステム用の統合されたアンチウイルスとセキュリティソリューションです。セキュリティ設定を効果的に管理するためのユーザーフレンドリーなインターフェイスを提供する。しかし、コマンドライン制御を好む上級ユーザーのために、Windows Defenderは強力なPowerShellコマンドのセットを提供します。この記事では、**Windows Defender PowerShell コマンド** の世界を掘り下げ、それらがどのようにシステムセキュリティを強化し、Windows 環境をよりコントロールできるかを探ります。

## Windows Defender PowerShell コマンドの威力

Windows Defender PowerShell コマンドは、コマンドラインインターフェイスを使って高度なセキュリティ操作を実行する能力をユーザーに与えます。これらのコマンドは、マルウェアのスキャンのような単純な操作から、高度なセキュリティ設定の構成のような複雑なタスクまで、幅広い機能を提供します。PowerShellを利用することで、ユーザーはセキュリティ操作を自動化し、カスタムスクリプトを作成し、Windows Defenderを既存のワークフローにシームレスに統合することができます。

## Windows Defender PowerShell入門

Windows Defender PowerShellコマンドにアクセスするには、管理者権限でPowerShellセッションを開く必要があります。ここでは、その方法を説明します：

1. `Win + X`を押し、メニューから **Windows PowerShell (Admin)**（管理者として）を選択します。
2. プロンプトが表示されたら、**Yes**（はい）をクリックして、アプリがデバイスに変更を加えることを許可します。

PowerShellセッションを開いたら、Windows Defender PowerShellコマンドを使用することができます。

## 一般的な Windows Defender PowerShell コマンド

### 1. **Get-MpComputerStatus**: Windows Defender の状態を確認する

`Get-MpComputerStatus` コマンドは、ウイルス対策エンジンのバージョン、前回のスキャン時刻、リアルタイム保護の状態など、現在の Windows Defender の状態を表示します。このコマンドを実行すると、Windows Defender が正常に動作しているかをすばやく確認できます。

Windows Defenderの状態を確認するには、管理者権限でPowerShellセッションを開き、以下のコマンドを実行します：

```powershell
Get-MpComputerStatus
```

このコマンドは以下のような情報を表示する：

- **AntivirusEngineVersion**：Windows Defender が使用するウイルス対策エンジンのバージョン番号。
- **LastFullScanTime**：Windows Defenderによって実行された最後のフルスキャンの日時。
- **LastQuickScanTime**：Windows Defenderが最後にクイックスキャンを実行した日時。
- **RealTimeProtectionEnabled**：リアルタイム保護が有効か無効かを示します。

`Get-MpComputerStatus` で Windows Defender の状態を定期的に確認すると、システムの保護状況を把握できます。

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

`Update-MpSignature` コマンドを使うと、Windows Defender のウイルス対策シグネチャを手動で更新できます。シグネチャには既知のマルウェアに関する情報が含まれており、脅威の検出とブロックに役立ちます。このコマンドを実行すると最新のシグネチャを取得でき、新たな脅威への保護を強化できます。

Windows Defender のシグネチャを手動で更新するには、管理者権限で PowerShell セッションを開き、以下のコマンドを実行します：

```powershell
Update-MpSignature
```
このコマンドは、**Windows Defender**が**Microsoftサーバー**に接続して最新の**アンチウイルス署名**をダウンロードする更新プロセスをトリガーします。更新が完了すると、Windows Defenderは既知のマルウェアに関する最新の情報を持つようになり、脅威を特定して排除する能力が強化されます。

Windows Defender のシグネチャを最新の状態に保つことは、変化する **マルウェア** や **サイバー脅威** からシステムを守るうえで重要です。`Update-MpSignature` で定期的に更新すると、Windows Defender による保護を維持できます。

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

`Set-MpPreference` コマンドを使うと、**Windows Defender** の各種設定をカスタマイズし、必要なセキュリティ要件に合わせられます。**リアルタイム保護**、**クラウド保護**、**ネットワーク検査システムの設定**などを調整できます。

たとえば、`Set-MpPreference` コマンドでリアルタイム保護を有効または無効にできます。リアルタイム保護はシステム上の不審な動作を監視し、脅威にすばやく対応します。有効にするには、次のコマンドを実行します：

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

さらに、このコマンドを活用してクラウドベースの保護設定を調整することもできます。クラウドベースの保護は、クラウドのリソースを利用して脅威の検出を強化し、新たな脅威への対応を迅速化します。クラウドベースの保護を有効にするには、次のコマンドを使用します：

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

さらに `Set-MpPreference`コマンドを使用すると、ネットワーク検査システムの設定をカスタマイズできます。ネットワーク検査システムは、疑わしいアクティビティや潜在的な脅威についてネットワーク・トラフィックを分析します。ネットワーク検査システムの設定を調整するには、次のコマンドを実行します：

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

`Set-MpPreference` でこれらの設定を調整すると、**Windows Defender** をセキュリティ要件に合わせ、マルウェアなどからシステムを保護できます。

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

`Start-MpScan` コマンドは、システム上のマルウェアをスキャンし、悪意のあるファイルの特定と除去に役立ちます。**クイックスキャン**、**フルスキャン**、特定のパスを対象とする **カスタムスキャン**を実行できます。

`Start-MpScan` で **クイックスキャン**を実行するには、次の PowerShell コマンドを実行します：

```powershell
Start-MpScan -ScanType QuickScan
```

クイックスキャンは、マルウェアがよく見つかるシステムの重要な領域に焦点を当て、潜在的な脅威を迅速に評価します。

システム上のすべてのファイルとディレクトリを調べるには、**フルスキャン**を実行します。`Start-MpScan` で次のコマンドを実行します：

```powershell
Start-MpScan -ScanType FullScan
```

フルスキャンは、システムからマルウェアを徹底的に検出して除去することを確実にしますが、クイックスキャンに比べて完了までに時間がかかる場合があります。

定義済みのスキャン種類に加えて、`Start-MpScan` では対象のパスやファイルを指定したカスタムスキャンも実行できます。たとえば、次のコマンドで特定のディレクトリをスキャンできます：

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

このコマンドは、指定されたディレクトリに対してカスタムスキャンを開始し、マルウェア検出のためにシステムの特定の領域をターゲットにすることができます。

`Start-MpScan` を活用すると、スキャンの実行を計画し、セキュリティ作業を自動化して、マルウェアを定期的に検出できます。

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

`Get-MpThreatCatalog` コマンドを使うと、既知の脅威とその属性に関する詳細を取得できます。脅威の重大度、関連するファイル名、推奨される対処方法などを含むカタログを参照できます。

`Get-MpThreatCatalog` で特定の脅威に関する情報を取得するには、次の手順に従います：

1. 管理者権限でPowerShellセッションを開きます。
2. 以下のコマンドを実行する：

```powershell
   Get-MpThreatCatalog
```
このコマンドは、既知の脅威のリストを、対応する詳細とともに表示する。

`Get-MpThreatCatalog` の出力には、次のような情報が含まれます：

- **ThreatID**：脅威を識別する一意の ID。
- **Severity**：脅威の重大度。Low から Severe までの値が示されます。
- **Name**：脅威の名前または説明。
- **Path**：脅威に関連するファイルのパス。
- **RecommendedAction**：脅威を軽減するために推奨される対処方法。

`Get-MpThreatCatalog` の情報を使うと、脅威を把握し、適切な対処を判断できます。脅威の隔離、削除、監視などを検討でき、詳細なカタログはセキュリティインシデントへの対応に役立ちます。

`Get-MpThreatCatalog` の使用方法と結果の解釈については、Microsoft の公式ドキュメントを参照してください。

`Get-MpThreatCatalog` を定期的に確認し、変化する脅威を把握してシステムのセキュリティを高めましょう。

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

`Add-MpPreference` コマンドを使うと、Windows Defender に除外対象を追加し、スキャンとリアルタイム保護の動作を調整できます。セキュリティスキャンやリアルタイム保護で無視するファイル、フォルダー、プロセスを指定できます。

`Add-MpPreference` で除外対象を追加するには、除外するファイル、フォルダー、またはプロセスのパスか名前を指定します。次の例ではフォルダーを除外します：

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

このコマンドは、Windows Defenderが指定されたフォルダのスキャンをスキップすることを保証し、不必要なアラートとワークフローへの潜在的な中断を減らします。

除外は、信頼できるアプリケーション、開発環境、誤検知を起こす可能性があるファイルなどに使えます。`Add-MpPreference` を使って Windows Defender を要件に合わせて調整し、性能を最適化できます。

`Add-MpPreference` の除外機能を使ってシステムを保護し、誤検知や不要なスキャン中断を減らしましょう。

## 2026年版 Defender コマンドの確認

タスクで昇格が必要な場合に限り、管理者権限のセッションから Defender コマンドを実行します。パラメーターを使う前に、対象の Windows バージョンでモジュールの最新ヘルプを確認します。現在の設定を記録し、設定を一度に1つ変更して結果を検証し、ロールバック用コマンドを記録します。

保護状態、シグネチャの経過時間、除外、設定、スキャン履歴、最近の検出結果を確認します。除外範囲を狭く保ち、担当者と期限を記録します。最新のコマンドレットと動作は、[Microsoft Defender PowerShell モジュールのドキュメント](https://learn.microsoft.com/en-us/powershell/module/defender/)および[Microsoft Defender ウイルス対策のドキュメント](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows)で確認してください。

## 結論

Windows Defender PowerShell コマンドは、Windows システムのセキュリティを管理・強化するための **強力なツールセット** を提供します。これらのコマンドを活用することで、*セキュリティ操作の自動化*、*高度な設定の構成*、およびWindows Defenderをワークフローにシームレスに組み込むことができます。あなたが**システム管理者**であろうと**パワーユーザー**であろうと、Windows Defender PowerShellコマンドの機能を探求することは、あなたのシステムのセキュリティ体制を大幅に改善することができます。

大きな力には大きな責任が伴うことを忘れないでください。PowerShellコマンドを使用するときは、コマンドを実行する前に、コマンドの影響を理解するように注意してください。Windows Defender PowerShell コマンドのパワーと知識を組み合わせることで、進化する脅威からシステムを保護するためのプロアクティブな対策を講じることができます。

## 参考文献

1. マイクロソフトドキュメント [Windows PowerShell の Windows Defender コマンドレット](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. マイクロソフト・ドキュメント [Windows PowerShell の概要](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
