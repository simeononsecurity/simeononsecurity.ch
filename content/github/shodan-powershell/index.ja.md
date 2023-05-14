---
title: "Shodan PowerShell モジュールを使用して OSINT を自動化する"
date: 2020-11-14
---

Shodan API と対話するための PowerShell モジュールのコレクション

**ノート：**
- Shodan API キーが必要になります。[Shodan Account](https://account.shodan.io/)
- モジュールで使用される API の例は、[Shodan Developers Page](https://developer.shodan.io/api)
- 特定のモジュールはスキャン クレジットまたはクエリ クレジットを使用する場合があります。クエリ クレジットは、Web サイト、CLI、または API (これらのスクリプトの機能) 経由でデータをダウンロードするときに使用されます。
  API を使用しているため、次の場合にはクエリ クレジットが差し引かれることに注意することが重要です。
  1. 検索フィルターを使用する
  2. 2ページ目以降をご希望の場合
      クレジットは月初めに更新され、1 クレジットで 100 件の結果をダウンロードできます。
      スキャン クレジットについては、1 スキャン クレジットで 1 つの IP をスキャンでき、これも月初めに更新されます。
      Shodan ヘルプセンターをご覧ください。[HERE](https://help.shodan.io/the-basics/credit-types-explained) 詳細については、

＃＃ 目次
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **モジュール**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - 指定された API キーに属する API プランに関する情報を返します。
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Web サーバーに接続するときにクライアントが送信する HTTP ヘッダーを表示します。
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - インターネットから見える現在の IP アドレスを取得します。
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - 指定されたドメインのすべてのサブドメインとその他の DNS エントリを取得します
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - 指定された IP アドレスのリストに対して定義されているホスト名を検索します。
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - エクスプロイトを検索しますが、検索用語に関連する一致の総数に関する情報のみを返します。オプションでエクスプロイトの作成者、プラットフォーム、ポート、ソース、またはタイプも返します。
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - 「/shodan/host/search」の検索結果の総数を返します。
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - IPアドレスでShodanを検索します。
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Web サイトと同じクエリ構文を使用して Shodan を検索し、ファセットを使用してさまざまなプロパティの概要情報を取得します。
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - このモジュールは、検索クエリで使用できる検索フィルターのリストを返します。
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - このモジュールは、検索クエリで使用できる検索フィルターのリストを返します。
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Shodan がインターネット上でクロールしているすべてのポートをリストします。
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - この API キーにリンクされた Shodan アカウントに関する情報を返します
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - 以前に送信されたスキャン要求の進行状況を確認する
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Shodan 経由でオンデマンド インターネット スキャンを実行するときに使用できるすべてのプロトコルをリストします。
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- このモジュールを使用して、Shodan にネットワークのクロールを要求します。<a name="Download"></a> ## ダウンロード スクリプトをコンピュータに複製するか、ダウンロードする必要があります。このリポジトリ ページの [コード] ドロップダウン メニューを使用するには、上にスクロールするか、次のリンクをコピーして貼り付けます。[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

！[On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

この例では、Git Bash 内でリポジトリのクローンを作成します。上記のようにクリップボード アイコンをクリックした後、「git clone」と入力し、Git Bash ウィンドウを右クリックしてドロップダウン メニューから [貼り付け] を選択します。

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

For detailed instructions on cloning please view [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

You can use the Code dropdown menu on this repo page by scrolling up, or just click on the following link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Unzip main.zip by right clicking on the file and selecting extract here from the dropdown menu.

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Install"></a>

To install the modules You will need to run a PowerShell window as administrator.
There are two ways of doing this:

The first way is by right clicking the PowerShell icon on the Desktop and selecting Run as Administrator from the dropdown menu.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

By typing p (or however many characters it takes PowerShell to show up) into the search bar and clicking on Run as Administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

You will need to be in the directory that you copied the scripts to.
Run the following command to change your working directory:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

On Windows client computers we need to change the PowerShell execution policy which is Restricted by default.

For more information please read this [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Run the following command to set the policy to RemoteSigned and enter y to select that Yes you want to change the policy.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Once the execution policy has been changed, you can run the following command to Import the modules.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

これで、PowerShell を介して任意のスクリプトをモジュールとして実行できるようになります。
