---
title: "Chocolatey、PSWindowsUpdate、スタートアップスクリプトを使った自動化でWindows Updateを効率化する"
date: 2020-07-22
---
Chocolatey、PSWindowsUpdate、スタートアップスクリプトによるWindowsアップデート**。

現代のビジネス環境では、システム管理者にとって、時間が最も重要です。システム管理の重要な要素であるWindowsマシンのアップデートは、非常に時間のかかる作業で、十分な数のシステムがあれば、1週間かかることもあります。しかし、Chocolatey、PSWindowsUpdates、およびスタートアップスクリプトの支援により、各マシンのわずか1回の再起動で更新を展開することが可能になり、更新に必要な時間を大幅に短縮することができます。

## 自動化によるWindowsアップデートの効率化

Windowsのアップデートは、Windowsマシンの安定性と安全性を維持するために重要です。特にリソースが限られているシステム管理者にとっては、多数のマシンに対してアップデートを実行することは時間のかかる作業となります。しかし、Chocolatey、PSWindowsUpdate、Startup Scriptsなどの自動化ツールを使用することで、このプロセスを合理化し、管理者が最小限の労力で更新を実行できるようにすることができる。

### Chocolatey

[Chocolatey](https://chocolatey.org/)は、Windowsマシンへのソフトウェアのインストールを自動化するために使用できる、Windows用のパッケージマネージャです。Ubuntuのapt-getやmacOSのhomebrewに似ており、様々なソフトウェアパッケージのインストールや管理に使用することができます。Chocolateyは、パッケージのサイレントインストール、つまりユーザーの介入なしにパッケージをインストールするために使用することができます。

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4)は、Windows更新プログラムのインストールを自動化するために使用することができるPowerShellモジュールです。Windowsアップデートのインストール、アンインストール、リストアップに使用できるコマンドレットを提供します。PSWindowsUpdateは、複数のマシンのWindowsアップデートを管理するために使用できる強力なツールであり、大量のマシンを管理する必要があるシステム管理者に最適です。

### スタートアップスクリプト

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11))は、マシンの起動やシャットダウン時に実行する必要があるタスクを自動化するために使用できるスクリプトです。このスクリプトは、ソフトウェアのインストール、設定、Windowsの更新管理などのタスクを実行するために使用されます。

## 一度の再起動でWindowsの更新を自動化する

Chocolatey、PSWindowsUpdate、およびStartup Scriptsを使用してWindowsアップデートを自動化するには、管理者は以下のステップバイステップのガイドに従うことができます。

### シャットダウンスクリプトのセットアップ
以下のサイトからすべてのサポートファイルをダウンロードします。 [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1.1.ローカルグループポリシーエディターを開きます。**"Win + R "**を押し、**"gpedit.msc "**と入力し、**"Ctrl + Shift + Enter "**と入力します。
2.Computer **ConfigurationWindows Settings **Scripts (Startup/Shutdown)** に移動する。
3.結果ペインで、「Shutdown」をダブルクリックします。
4.PowerShellタブを選択します。
5.シャットダウンのプロパティ］ダイアログボックスで、［追加］をクリックします。
6.スクリプト名］ボックスにスクリプトのパスを入力するか、［参照］をクリックしてドメインコントローラのNetlogon共有フォルダの「*chocoautomatewindowsupdates.ps1*」を検索します。
7.リブートします。

これで、管理者が行うべきことは、Windowsアップデートを実行するためにコンピュータを再起動することです。

### スクリプトを理解する

Windowsの更新を自動化するためのスクリプトのタイトルは「*chocoautomatewindowsupdates.ps1*」です。このスクリプトは、以下のタスクを実行します：

1.1.Chocolateyパッケージマネージャーをインストールする。
2.2.Chocolateyの設定変更に必要ないくつかの項目を有効にする。
3.インストールされているすべてのChocolateyパッケージをアップグレードする。
4.PSWindowsUpdate PowerShellモジュールがインストールされます。
5.Windows Updateサービスマネージャーを追加します。
6.利用可能なすべてのWindowsアップデートをインストールします。
7.不足しているドライバーや、以前にインストールした更新プログラムが必要とする更新プログラムをインストールする。

### Windows Updateを自動化するメリット

Chocolatey、PSWindowsUpdate、およびスタートアップスクリプトを使用してWindowsの更新を自動化することは、システム管理者にとっていくつかの利点があります。これらの利点は以下の通りです：

- 時間の節約**：Windowsアップデートの自動化により、アップデートの実行に必要な時間が大幅に短縮されます。管理者は、各マシンに手動で更新プログラムをインストールする必要がなくなります。
- 一貫性**：Windowsアップデートの自動化により、すべてのマシンに一貫してアップデートがインストールされるようになります。これにより、エラーやセキュリティの脆弱性が発生する可能性が低くなります。
- 集中管理**：Windowsアップデートの自動化により、管理者はアップデートを一元的に管理できるようになり、どのアップデートがインストールされたか、どのマシンにアップデートが必要かを容易に把握できるようになります。
- セキュリティの強化**：Windowsアップデートの自動化により、マシンに最新のセキュリティパッチを適用することができ、セキュリティ侵害のリスクを低減することができます。

### 結論

Chocolatey、PSWindowsUpdate、および Startup Scripts を使用して Windows の更新を自動化することは、システム管理者の時間と労力を大幅に削減する強力なツールです。更新プログラムを一貫して効率的にインストールできるため、マシンを最新のセキュリティパッチに対応させることができます。このチュートリアルで説明する手順に従うことで、管理者は1回の再起動でWindowsの更新を自動化でき、Windowsマシンの更新プロセスをより迅速かつ容易にすることができます。
