---
title: "Windows Defender PowerShellコマンドでシステムセキュリティを強化する"
date: 2023-07-27
toc: true
draft: false
description: "Windows Defender PowerShellコマンドのパワーを発見し、コマンドライン制御でシステムセキュリティを強化する方法を学びましょう。"
genre: ["ウィンドウズ・ディフェンダー", "PowerShellコマンド", "システムセキュリティ", "コマンドライン制御", "アンチウイルス", "Windowsオペレーティングシステム", "マルウェアプロテクション", "高度なセキュリティ設定", "セキュリティ運用の自動化", "Windows PowerShell"]
tags: ["テクノロジー", "サイバーセキュリティ", "オペレーティング・システム", "ウィンドウズ", "コマンドラインツール", "システム・セキュリティ", "パワーシェル", "アンチウイルス", "マルウェア対策", "スクリプト"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "さまざまなサイバー脅威からコンピュータシステムを守るシールドを描いたアニメーションイラスト。"
coverCaption: "Windows Defender PowerShell コマンドでシステムのセキュリティを強化。"
---

#はじめに

マイクロソフトによって開発されたWindows Defenderは、Windowsオペレーティングシステム用の統合されたアンチウイルスとセキュリティソリューションです。セキュリティ設定を効果的に管理するためのユーザーフレンドリーなインターフェイスを提供する。しかし、コマンドライン制御を好む上級ユーザーのために、Windows Defenderは強力なPowerShellコマンドのセットを提供します。この記事では、**Windows Defender PowerShell コマンド** の世界を掘り下げ、それらがどのようにシステムセキュリティを強化し、Windows 環境をよりコントロールできるかを探ります。

## Windows Defender PowerShell コマンドの威力

Windows Defender PowerShell コマンドは、コマンドラインインターフェイスを使って高度なセキュリティ操作を実行する能力をユーザーに与えます。これらのコマンドは、マルウェアのスキャンのような単純な操作から、高度なセキュリティ設定の構成のような複雑なタスクまで、幅広い機能を提供します。PowerShellを利用することで、ユーザーはセキュリティ操作を自動化し、カスタムスクリプトを作成し、Windows Defenderを既存のワークフローにシームレスに統合することができます。

## Windows Defender PowerShell入門

Windows Defender PowerShellコマンドにアクセスするには、管理者権限でPowerShellセッションを開く必要があります。ここでは、その方法を説明します：

1.を押します。 `Win + X`を選択し、メニューから**Windows PowerShell (Admin)**を選択します。
2.プロンプトが表示されたら、**Yes**をクリックして、アプリがデバイスに変更を加えることを許可します。

PowerShellセッションを開いたら、Windows Defender PowerShellコマンドを使用することができます。

## 一般的な Windows Defender PowerShell コマンド

### 1.1. **Get-MpComputerStatus**：Windows Defender のステータスを確認する

Windows Defender のステータスを確認します。 `Get-MpComputerStatus`コマンドは、ウイルス対策エンジンのバージョン、最後のスキャン時間、リアルタイムの保護ステータスなど、システム上の現在の Windows Defender ステータスの概要を提供します。このコマンドを実行することで、Windows Defenderの全体的な健康状態を素早く評価し、最適に機能していることを確認することができます。

Windows Defenderの状態を確認するには、管理者権限でPowerShellセッションを開き、以下のコマンドを実行します：

```powershell
Get-MpComputerStatus
```

このコマンドは以下のような情報を表示する：

- AntivirusEngineVersion**：AntivirusEngineVersion**: Windows Defender が使用するウイルス対策エンジンのバージョン番号。
- LastFullScanTime**：Windows Defenderによって実行された最後のフルスキャンの日時。
- LastQuickScanTime**：Windows Defenderが最後にクイックスキャンを実行した日時。
- **RealTimeProtectionEnabled**：リアルタイム保護が有効か無効かを示します。

を使用して定期的にWindows Defenderの状態を監視します。 `Get-MpComputerStatus`これにより、潜在的な脅威に対するシステムの保護レベルについて常に情報を得ることができます。

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

について `Update-MpSignature`コマンドはWindows Defenderが使用するウイルス対策シグネチャを手動で更新する機能を提供します。ウイルス対策シグネチャには既知のマルウェアに関する重要な情報が含まれており、Windows Defenderが脅威を効果的に検出しブロックできるようにします。このコマンドを実行することで、システムが最新のシグネチャを持つようになり、新たな脅威に対する保護が強化されます。

Windows Defender のシグネチャを手動で更新するには、管理者権限で PowerShell セッションを開き、以下のコマンドを実行します：

```powershell
Update-MpSignature
```
このコマンドは、**Windows Defender**が**Microsoftサーバー**に接続して最新の**アンチウイルス署名**をダウンロードする更新プロセスをトリガーします。更新が完了すると、Windows Defenderは既知のマルウェアに関する最新の情報を持つようになり、脅威を特定して排除する能力が強化されます。

Windows Defenderのシグネチャを常に最新の状態に保つことは、日々進化する**マルウェア**や**サイバー脅威**に対する最高レベルの保護を維持するために不可欠です。シグネチャを定期的に更新することで `Update-MpSignature`Windows Defenderが効果的にシステムを保護できるようにします。

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

について `Set-MpPreference`コマンドを使用すると、さまざまな **Windows Defender** 設定をカスタマイズできるため、特定のセキュリティ要件に合わせて動作を調整できます。このコマンドは、**リアルタイム保護**、**クラウドベースの保護**、*ネットワーク検査システム設定**などのオプションを柔軟に構成することができます。

たとえば、リアルタイム保護は `Set-MpPreference`コマンドを使用します。リアルタイム保護は、悪意のあるアクティビティがないかシステムをアクティブに監視し、脅威に即座に対応します。リアルタイム保護を有効にするには、次のコマンドを実行します：

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

でこれらの設定を微調整する。 `Set-MpPreference`Windows Defender**をお客様固有のセキュリティニーズに合わせて最適化し、マルウェアやその他の悪意のある活動から確実に保護することができます。

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

について `Start-MpScan`コマンドは、システム上でマルウェアのスキャンを開始するための強力なツールであり、悪意のあるファイルを積極的に特定し、除去することができます。このコマンドは、**クイックスキャン**、**フルスキャン**、特定のパスを使用した**カスタムスキャン**など、さまざまな種類のスキャンを柔軟に実行できます。

を使用して**クイック スキャン**を実行するには、次の手順に従います。 `Start-MpScan`コマンドを実行した後、以下のPowerShellコマンドを実行する：

```powershell
Start-MpScan -ScanType QuickScan
```

クイックスキャンは、マルウェアがよく見つかるシステムの重要な領域に焦点を当て、潜在的な脅威を迅速に評価します。

システム上のすべてのファイルとディレクトリを調べる、より包括的なスキャンを行うには、**フルスキャン**を開始します。を使用してフルスキャンを実行するには、次のコマンドを実行します。 `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

フルスキャンは、システムからマルウェアを徹底的に検出して除去することを確実にしますが、クイックスキャンに比べて完了までに時間がかかる場合があります。

定義済みのスキャンタイプに加えて `Start-MpScan`コマンドを使用すると、スキャンする特定のパスまたはファイルを指定してカスタム スキャンを実行できる。例えば、以下のコマンドを使って、システム上の特定のディレクトリをスキャンすることができる：

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

このコマンドは、指定されたディレクトリに対してカスタムスキャンを開始し、マルウェア検出のためにシステムの特定の領域をターゲットにすることができます。

このコマンドは `Start-MpScan`コマンドを使用することで、スキャンをスケジュールし、セキュリティ・プロセスを自動化し、システム上で定期的にマルウェアを検出および軽減することができます。

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

について `Get-MpThreatCatalog`コマンドは、既知の脅威とその属性に関する詳細情報を得るための貴重なリソースです。このコマンドを実行すると、脅威の重大度、関連ファイル名、および緩和のための推奨アクションに関するデータを含む、脅威の包括的なカタログにアクセスできます。

特定の脅威に関する情報を取得するには `Get-MpThreatCatalog`以下の手順に従ってください：

1.管理者権限でPowerShellセッションを開きます。
2.以下のコマンドを実行する：

```powershell
   Get-MpThreatCatalog
```
このコマンドは、既知の脅威のリストを、対応する詳細とともに表示する。

コマンドの出力は `Get-MpThreatCatalog`コマンドには次のような重要な情報が含まれている：

- 脅威ID**：脅威の一意の識別子。
- 重大度**：Severity**：脅威の深刻度レベルを示す。
- 名前**：脅威の名前または説明：脅威の名前または説明。
- パス脅威に関連付けられているファイルのパス。
- RecommendedAction**：脅威を緩和するために推奨されるアクションに関するガイダンスを提供します。

から取得した情報を活用することで、脅威を軽減することができます。 `Get-MpThreatCatalog`は、潜在的な脅威に関する貴重な洞察を得るとともに、脅威を軽減するための適切なアクションに関して情報に基づいた意思決定を行うことができます。特定の脅威の隔離、除去、監視のいずれにおいても、詳細なカタログにより、セキュリティ・インシデントに効果的に対応できるようになります。

使用方法の詳細 `Get-MpThreatCatalog`その結果の解釈については、マイクロソフト社の公式文書を参照されたい。

用心深く、定期的に `Get-MpThreatCatalog`コマンドを使用することで、進化する脅威の状況を常に把握し、システムのセキュリティを強化することができます。

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

について `Add-MpPreference`コマンドは、Windows Defenderに除外項目を追加し、スキャンとリアルタイム保護の動作をカスタマイズできるようにします。除外項目を追加することで、Windows Defenderがセキュリティスキャンまたはリアルタイム保護中に無視したいファイル、フォルダ、またはプロセスを指定することができます。

除外を追加するには `Add-MpPreference`には、除外したいファイル、フォルダー、またはプロセスのパスまたは名前を指定する必要があります。以下は、フォルダーの除外を追加する例です：

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

このコマンドは、Windows Defenderが指定されたフォルダのスキャンをスキップすることを保証し、不必要なアラートとワークフローへの潜在的な中断を減らします。

除外は、信頼できるアプリケーション、開発環境、または誤検出を引き起こす可能性のある特定のファイルを除外するなど、さまざまなシナリオで役立ちます。の柔軟性を活用することで `Add-MpPreference`を使えば、Windows Defenderを特定のセキュリティニーズに合わせて微調整し、そのパフォーマンスを最適化することができます。

が提供する強力な除外機能を利用することで、誤検出や不要なスキャンの中断を最小限に抑えながら、システムを効果的に保護します。 `Add-MpPreference`

## 結論

Windows Defender PowerShell コマンドは、Windows システムのセキュリティを管理・強化するための **強力なツールセット** を提供します。これらのコマンドを活用することで、*セキュリティ操作の自動化*、*高度な設定の構成*、およびWindows Defenderをワークフローにシームレスに組み込むことができます。あなたが**システム管理者**であろうと**パワーユーザー**であろうと、Windows Defender PowerShellコマンドの機能を探求することは、あなたのシステムのセキュリティ体制を大幅に改善することができます。

大きな力には大きな責任が伴うことを忘れないでください。PowerShellコマンドを使用するときは、コマンドを実行する前に、コマンドの影響を理解するように注意してください。Windows Defender PowerShell コマンドのパワーと知識を組み合わせることで、進化する脅威からシステムを保護するためのプロアクティブな対策を講じることができます。

## 参考文献

1.マイクロソフトドキュメント [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2.マイクロソフト・ドキュメント [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
