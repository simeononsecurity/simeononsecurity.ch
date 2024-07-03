---
title: "Shodan PowerShellモジュールでOSINTを自動化する。"
date: 2020-11-14
---

Shodan APIと連動するためのPowerShellモジュールの集大成

**注意事項：**。
- Shodan APIキーが必要です。 [Shodan Account](https://account.shodan.io/)
- モジュールで使用されているAPIの例は、以下のページで見ることができます。 [Shodan Developers Page](https://developer.shodan.io/api)
- モジュールによっては、スキャンまたはクエリクレジットを使用する場合があります クエリクレジットは、ウェブサイト、CLIまたはAPI（これらのスクリプトが行うもの）を介してデータをダウンロードするときに使用されます。
  私たちはAPIを使用しているので、クエリクレジットは以下の場合に差し引かれることに注意することが重要です：
  1.  検索フィルタを使用した場合
  2.  2ページ目以降のページが要求された場合
      クレジットは月初に更新され、1クレジットで100件の結果をダウンロードできます。
      スキャンクレジットは、1クレジットで1IPのスキャンが可能で、こちらも月初に更新されます。
      初段ヘルプセンターでご確認ください。 [HERE](https://help.shodan.io/the-basics/credit-types-explained)をご覧ください。

## 目次
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- モジュール
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo)- 与えられたAPIキーに属するAPIプランに関する情報を返す。
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders)- クライアントがWebサーバーに接続する際に送信するHTTPヘッダーを表示します。
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP)- インターネットから見た現在の IP アドレスを取得します。
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain)- 指定されたドメインのすべてのサブドメインとその他のDNSエントリーを取得します。
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse)- 与えられたIPアドレスのリストに対して定義されたホスト名を検索する。
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount)- エクスプロイトを検索しますが、検索語に関連するマッチの総数に関する情報のみを返し、オプションでエクスプロイトの作者、プラットフォーム、ポート、ソース、タイプも返します。
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount)- shodan/host/search "の検索結果の総件数を返します。
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP)- IPアドレスで初段を検索してください。
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch)- ウェブサイトと同じクエリ構文を使用して初段を検索し、ファセットを使用してさまざまなプロパティの概要情報を取得することができます。
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets)- このモジュールは、検索クエリで使用可能な検索フィルタのリストを返す。
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters)- このモジュールは、検索クエリで使用可能な検索フィルタのリストを返す。
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts)- Shodan がインターネット上でクロールしているポートをすべてリストアップします。
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile)- この API キーに紐づく Shodan アカウントに関する情報を返します。
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID)- 過去に送信したスキャンリクエストの進捗状況を確認する
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols)- Shodan を介してオンデマンドのインターネットスキャンを実行する際に使用できるプロトコルをすべてリストアップする。
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- このモジュールを使って、Shodanにネットワークのクロールを依頼します。

<a name="ダウンロード"></a>。

## ダウンロード

スクリプトをコンピュータにクローンまたはダウンロードする必要があります。

このレポのページで上にスクロールして、コードのドロップダウンメニューを使用するか、次のリンクをコピーして貼り付けることができます： [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

この例では、Git Bash でリポジトリのクローンを作成します。上の図のようにクリップボードのアイコンをクリックしたら、git clone と入力して Git Bash のウィンドウを右クリックし、ドロップダウンメニューから貼り付けを選択できます：

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

クローン作成に関する詳しい説明は、こちらをご覧ください。 [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

ファイルを入手したら、ファイルをC:◆Program FilesWindowsPowerShell◆Modulesにコピーする必要があります。この作業を行うと、アクセスが拒否されたというダイアログが表示されますので、続けるをクリックしてこの場所へのファイルのコピーを完了し、インストール手順に進んでください。 [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

このレポページのCodeドロップダウンメニューを上にスクロールして使うか、以下のリンクをクリックするだけでもOKです：
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

main.zipを右クリックし、ドロップダウンメニューから「ここに解凍」を選択して解凍します。

ファイルを入手したら、ファイルをC:˶‾Program FilesWindowsPowerShell‾Modulesにコピーする必要があります。この作業を行うと、アクセスが拒否されたというダイアログが表示されます。 [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

## インストール

<a name="Install"></a>となります。

モジュールをインストールするためには、PowerShellウィンドウを管理者として実行する必要があります。
これには、2つの方法があります：

最初の方法は、デスクトップ上のPowerShellアイコンを右クリックし、ドロップダウンメニューから「管理者として実行」を選択する方法です。

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

検索バーにp（またはPowerShellが表示されるまでの文字数）を入力し、「管理者として実行」をクリックすることで、表示されます。

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

スクリプトをコピーしたディレクトリにいる必要があります。
以下のコマンドを実行し、作業ディレクトリを変更してください：

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Windowsクライアントコンピュータでは、PowerShellの実行ポリシー（デフォルトでは制限されている）を変更する必要があります。

詳しくは、こちらをご覧ください。 [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

以下のコマンドを実行して、ポリシーをRemoteSignedに設定し、yを入力して、ポリシーを変更することをYesと選択します。

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

実行ポリシーを変更したら、以下のコマンドを実行してモジュールをImportすることができます。

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

これで、どのスクリプトもpowershellでモジュールとして実行できるようになりました。
