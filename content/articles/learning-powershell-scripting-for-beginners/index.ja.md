---
title: "PowerShellスクリプティング：タスクを自動化するための初心者のためのステップバイステップガイド"
draft: false
toc: true
date: 2023-02-25
description: "PowerShellスクリプトの基本を学び、タスクを自動化するための初心者向けステップバイステップガイドです。コマンドレット、ループ、関数などを網羅しています。"
genre: ["技術情報", "プログラミング", "オートメーション", "ウィンドウズ", "スクリプト", "インフォメーション", "アドミニストレーティブタスク", "コンピュータ管理", "ソフトウェア開発", "コーディング"]
tags: ["PowerShellスクリプティング", "PowerShellによる自動化", "ウィンドウズスクリプト", "PowerShellコマンドレット", "PowerShellモジュール", "PowerShellのループ", "PowerShellの条件文", "PowerShell関数", "PowerShellのベストプラクティス", "PowerShellのデバッギング", "PowerShellのテスト", "PowerShellの変数", "PowerShell ISE", "PowerShellリモーティング", "マイクロソフトテクノロジー", "ITオートメーション", "けいさんきかんり", "ビギナーズコーディング", "管理業務", "PowerShellスクリプトのアイデア", "自動バックアップ", "ファイル管理", "システム情報", "ユーザー管理", "ソフトウェアインストール", "ネットワーク構成", "セキュリティオートメーション", "タスクスケジューリング", "レジストリ操作", "リモート管理"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "スクリプトを持ち、PowerShellプロンプトのあるPCの前に立つ漫画のキャラクターは、初心者のためのPowerShellスクリプトの容易さを示しています。"
coverCaption: ""
---
初心者のためのPowerShellスクリプティング**」を開催します。

PowerShellは、Microsoft社が開発した強力なコマンドラインシェルとスクリプト言語です。Windowsオペレーティングシステムやその他のMicrosoftテクノロジーの様々な側面を管理し、自動化するための膨大な数のコマンドと機能を提供します。今回は、初心者向けにPowerShellスクリプトの基本を説明し、始めるためのステップバイステップのガイドを提供します。

## PowerShell入門

**PowerShell**は、Windowsオペレーティングシステムやその他のMicrosoftテクノロジーを自動化し、管理することを可能にするコマンドラインシェルです。PowerShell は、ファイルやディレクトリの管理、ネットワーク設定、システム管理など、さまざまな管理タスクを実行するための包括的なコマンドと機能のセットを提供します。また、PowerShellはスクリプト言語もサポートしており、複雑なスクリプトを作成したり、様々な反復作業を自動化することができます。

## PowerShell 入門

### PowerShell のインストール

PowerShellは、ほとんどのバージョンのWindowsオペレーティングシステムにプリインストールされています。ただし、古いバージョンのWindowsを使用している場合や、より新しいバージョンのPowerShellが必要な場合は、Microsoftのウェブサイトからダウンロードすることができます。PowerShellのダウンロードとインストールは、以下の手順で行います：

1.にアクセスします。 [Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2)をクリックし、インストールするPowerShellのバージョンを選択します。
2.インストールファイルをダウンロードし、実行する。
3.画面の指示に従って、インストールを完了します。

### PowerShell の起動

PowerShellのインストールが完了したら、以下の手順でPowerShellを起動することができます：

1.スタート」メニューをクリックし、検索バーに「PowerShell」と入力します。
2.検索結果から "Windows PowerShell "を選択します。
3.PowerShellが新しいウィンドウで開きます。

### PowerShell の基礎知識

PowerShell は、ユーザーがオペレーティングシステムと対話できるようにするコマンドラインインターフェイスを提供します。PowerShell のコマンドは cmdlet と呼ばれ、モジュールに整理されています。利用可能なモジュールの一覧を表示するには、Get-Module コマンドを使用します：

```powershell
Get-Module
```

モジュールで使用可能なコマンドレットの一覧を表示するには、Get-Commandコマンドを使用します：
```powershell
Get-Command -Module <module name>
```

コマンドレットに関するヘルプを得るには、Get-Help コマンドを使用します：
```powershell
Get-Help <cmdlet name>
```

PowerShellは、コマンドレットの短い名前であるエイリアスもサポートしています。利用可能なエイリアスのリストを表示するには、Get-Aliasコマンドを使用します：
```powershell
Get-Alias
```

### PowerShell スクリプティング
PowerShell スクリプトは、さまざまな管理タスクを自動化するための強力な機能です。PowerShell スクリプトは、変数、ループ、条件文、関数をサポートしており、自動化のための強力なツールとなっています。

#### 変数
変数は、PowerShellスクリプトでデータを保存するために使用されます。PowerShellの変数は、ドル記号（$）で始まります。変数に値を割り当てるには、次の構文を使用します：
```powershell
$variable_name = value
```
例えば、こんな感じです：
```powershell
$name = "John"
```
#### ループ
ループは、あるコードのブロックを一定回数繰り返すために使用されます。PowerShellでは、以下のようなループの種類をサポートしています：

- For ループ**：コードのブロックを特定の回数だけ繰り返します。
- For ループ**：コードのブロックを特定の回数だけ繰り返します。
- Do-Whileループ**：少なくとも1回、そして条件が真である限り、コードのブロックを繰り返します。
- orEachループ**：コレクション内の各アイテムに対して、コードのブロックを繰り返します。
  
例えば、次のコードは、Forループを使って1から5までの数字を表示します：
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### 条件付きステートメント

条件付きステートメント（Conditional Statements

条件文は、特定の条件が真である場合にコードブロックを実行するために使用されます。PowerShellでは、次のようなタイプの条件文をサポートしています：

- If文**：ある条件が真である場合に、コードのブロックを実行する。
- If文**：条件が真である場合にコードのブロックを実行します。
- Switch文**：ある値とマッチする可能性のあるセットを比較し、最初に見つかったマッチのためにコードのブロックを実行する。

例えば、次のコードは、If文を使用して、ある数値が5より大きいかどうかをチェックしています：

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### ファンクション
関数は、特定のタスクを実行する再利用可能なコードブロックです。関数は、入力パラメータを受け取り、出力値を返します。PowerShellでは、以下の種類の関数をサポートしています：

- スクリプトブロック**：実行可能なコードのブロックです。
- アドバンスド関数**：メタデータとパラメータ検証を含む関数です。

たとえば、次のコードは、2つの数値を加算する関数を定義しています：
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "The result is $result"
```
### PowerShell ISE
PowerShell ISE (Integrated Scripting Environment) は、PowerShell スクリプトのためのグラフィカルユーザーインターフェイスです。PowerShell ISE は、リッチテキストエディタ、デバッグツール、および PowerShell スクリプトの作成とテストを容易にするその他の機能を提供します。PowerShell ISEを開くには、次の手順に従います：

1.スタートメニューをクリックし、検索バーに「PowerShell ISE」と入力します。
2.検索結果から "Windows PowerShell ISE "を選択します。
3.PowerShell ISEが新しいウィンドウで開きます。

### PowerShell Remoting
PowerShell Remoting を使用すると、ユーザーはリモートコンピューター上で PowerShell コマンドやスクリプトを実行することができます。PowerShell Remoting を使用するには、ローカルコンピュータとリモートコンピュータの両方で WinRM サービスが実行されている必要があります。PowerShell Remotingを有効にするには、次の手順に従います：

1.管理者権限でPowerShellプロンプトを開きます。
2.以下のコマンドを実行し、PowerShell Remotingを有効にします：
```powershell
   Enable-PSRemoting -Force
```
3.以下のコマンドを実行し、リモートコンピュータをTrustedHostsリストに追加します：
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4.WinRMサービスを再起動する
```powershell
Restart-Service WinRM
```

リモートコンピューターでPowerShellコマンドを実行するには、Invoke-Commandコマンドレットを使用します：
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### PowerShell モジュール
PowerShell モジュールは、特定のタスクを実行するように設計されたコマンドレット、関数、およびスクリプトの集合体です。PowerShell モジュールは、PowerShell モジュールの中央リポジトリである PowerShell ギャラリーを使用してインストールおよび管理することができます。

PowerShell ギャラリーから PowerShell モジュールをインストールするには、次のコマンドを使用します：
```powershell
Install-Module <module name>
```

インストールされているPowerShellモジュールの一覧を表示するには、Get-InstalledModuleコマンドを使用します：
```powershell
Get-InstalledModule
```

### PowerShell スクリプティングのベストプラクティス

PowerShellスクリプト**を作成する場合、スクリプトが**安全**、*信頼性**、*保守性**であることを保証するために、ベストプラクティスに従うことが重要である。ここでは、覚えておくべきベストプラクティスをいくつか紹介します：

- 説明的な変数名を使用する**：説明的な変数名**：目的を明確に示す変数名を使用する。
- コメントを使用する**：コメントの使用**：コードの目的を説明するためにコメントを使用します。
- エラー処理**を使用するエラーハンドリングを使用して、エラーや例外を優雅に処理する。その `Try...Catch...Finally`PowerShellのコンストラクトを使用すると、例外を処理し、適切なアクションを実行することができます。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Test scripts thoroughly**：スクリプトを徹底的にテストして、期待通りに動作することを確認します。PowerShellのテストフレームワークである**Pester**を使って、スクリプトのユニットテストを書き、実行することができます。 [Pester Documentation](https://pester.dev/)
- **関数とモジュールを使う**：コードを整理し、再利用性を高めるために、関数とモジュールを使用します。関数はコードをより小さく、管理しやすい断片に分解することを可能にし、モジュールはコードをパッケージ化して配布する方法を提供します。 [About Functions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [About Modules](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Avoid hardcoding values**：スクリプト内で値をハードコードすることは避け、代わりにパラメータや変数を使用します。これにより、スクリプトはより柔軟で再利用しやすくなります。スクリプトにパラメータを渡すには、次のようにします。 `param`のキーワードを使用します。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Use verbose output**：スクリプトの進行状況について追加情報を提供するために、冗長出力を使用します。を使用することができます。 `Write-Verbose`スクリプトの実行中に冗長なメッセージを表示するコマンドレットです。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

これらのベストプラクティスに従うことで、より効率的で保守性の高いPowerShellスクリプトを書くことができ、生産性を向上させ、自動化タスクの安定性を確保することができます。

### PowerShell スクリプトのベストプラクティスを詳しく説明します。

#### エラー処理を使用する
エラー処理は、スクリプトがエラーや例外を優雅に処理することを保証するため、PowerShellスクリプトの重要な側面です。PowerShellには、Try-Catch文、Trap文、ErrorActionパラメータなど、エラーを処理する方法がいくつかあります。Try-Catch文は例外の捕捉と処理に使用され、Trap文はエラーの捕捉と処理に使用されます。ErrorActionパラメータは、スクリプトがエラーを処理する方法を制御するために使用されます。

以下は、Try-Catchステートメントを使用して、エラーを優雅に処理する例である：
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### スクリプトのテストは徹底して行う

PowerShell スクリプトのテストは、期待通りに動作することを確認するために不可欠です。PowerShell には、Pester などのテスト ツールやフレームワークがいくつか用意されており、ユーザーはスクリプトのテストを作成および実行することが可能です。これらのツールは、コード内の問題の特定と切り分けに役立ち、スクリプトが必要な要件を満たしていることを確認します。

ここでは、Pesterを使用してPowerShellスクリプトをテストする例を紹介します：
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # some code that should return the expected result
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### 関数とモジュールを使う
PowerShell スクリプトでコードを整理し、再利用性を高めるには、関数とモジュールが不可欠です。関数を使用すると、コードを再利用可能なブロックにまとめることができ、モジュールを使用すると、コードをパッケージ化して他の人と共有することができます。関数とモジュールを使用することで、PowerShellスクリプトをよりモジュール化し、効率的で保守性の高いものにすることができます。

以下は、PowerShellで関数を使用する例です：
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "There are $count processes running."
```

#### 値のハードコード化を避ける
PowerShellスクリプトで値をハードコードすると、柔軟性が低下し、保守が難しくなります。値をハードコードする代わりに、実行時にスクリプトに値を渡すことができるパラメータまたは変数を使用するのが最善です。パラメータや変数を使用することで、スクリプトをより再利用しやすくし、状況の変化に対応できるようにすることができます。

以下は、PowerShellでパラメータを使用する例です：
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Verbose出力を使用する
Verbose 出力は、スクリプトの進捗に関する追加情報を提供し、デバッグやトラブルシューティングに役立つことがあります。PowerShell には Write-Verbose コマンドレットがあり、冗長な情報をコンソールに出力することが可能です。冗長出力を使用することで、PowerShellスクリプトをより有益なものにし、デバッグを容易にすることができる。

ここでは、PowerShellで冗長出力を使用する例について説明します：
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "There are $count processes running."
```

### 初心者のためのPowerShellスクリプトのアイデア10選

PowerShellスクリプトの初心者の方向けに、スクリプトのアイデアを10個ご紹介します：

- バックアップの自動化**：重要なファイルやディレクトリを外付けハードドライブやクラウドストレージサービスにバックアップするプロセスを自動化するスクリプトを作成します。を使用することができます。 `Copy-Item`コマンドレットでファイルをコピーし `Start-Job`コマンドレットを使用すると、バックグラウンドでバックアップ処理を実行することができます。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **ファイル管理**：ファイルやディレクトリを、ファイルの種類やサイズなどの条件に基づいて別のフォルダに分類して整理するスクリプトを作成します。を使用することができます。 `Get-ChildItem`コマンドレットでファイルを取得し `Move-Item`コマンドレットを使用して、目的の場所に移動させることができます。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **システム情報**：CPUやメモリの使用量、ディスク容量、ネットワーク設定などのシステム情報を取得し、見やすく表示するスクリプトを作成します。を使用することができます。 `Get-WmiObject`コマンドレットを使用して、システム情報を収集し、フォーマットすることができます。 `Format-Table`または `Out-GridView` [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **User management**：Windowsオペレーティングシステムのユーザーとグループの追加、変更、削除のプロセスを自動化するスクリプトを作成します。を使用することができます。 `New-LocalUser` `Set-LocalUser`と `Remove-LocalUser`ユーザーを管理するためのコマンドレットと `New-LocalGroup` `Add-LocalGroupMember`と `Remove-LocalGroup`コマンドレットを使用して、グループを管理します。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **ソフトウエアのインストール**：複数のコンピューターに一度にソフトウェアをインストールし、設定するスクリプトを作成し、時間と手間を省くことができます。を使用することができます。 `Invoke-Command`コマンドレットを使用して、リモートコンピューターでインストールコマンドを実行します。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **ネットワーク設定**：IPアドレス、サブネットマスク、デフォルトゲートウェイなど、ネットワーク設定のプロセスを自動化するスクリプトを作成します。を使用することができます。 `Set-NetIPAddress` `Set-NetIPInterface`と `Set-DnsClientServerAddress`コマンドレットを使用して、ネットワーク設定を行います。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Security**：セキュリティ設定を監査・監視し、変更が検出された場合はユーザーに警告するスクリプトを作成します。このスクリプトでは `Get-AuditPolicy`コマンドレットを使用して、監査ポリシーを取得し `Send-MailMessage`コマンドレットを使用して、電子メール通知を送信します。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **タスクスケジューリング**：バックアップ、アップデート、システムスキャンなど、定期的なタスクをスケジュールして自動化するスクリプトを作成します。を使用することができます。 `Register-ScheduledTask`コマンドレットでスケジュールタスクを作成し `Start-ScheduledTask`コマンドレットで実行します。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **レジストリ操作**：特定のキーや値のレジストリ値を変更したり、取得したりするスクリプトを作成します。を使用することができます。 `Get-ItemProperty`と `Set-ItemProperty`レジストリと対話するためのコマンドレットです。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Remote administration**：Windowsコンピュータのリモート管理を可能にするスクリプトを作成し、ユーザーがリモートマシンでコマンドやスクリプトを実行できるようにします。を使用することができます。 `Enter-PSSession`コマンドレットまたは `Invoke-Command`コマンドレットを使用して、リモートコンピューター上でコマンドを実行することができます。 [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

これらのスクリプトのアイデアを探求して、実践的な経験を積み、PowerShellのスキルを拡大することを始めましょう。

## まとめ

PowerShellは、Windowsオペレーティングシステムやその他のMicrosoftテクノロジーを管理し、自動化するための強力なツールです。この記事では、PowerShellのインストールと起動、コマンドレット、変数、ループ、条件文、関数の使用、PowerShell ISE、PowerShell Remoting、PowerShellモジュールの使用など、初心者向けのPowerShellスクリプトの基本を説明しました。ベストプラクティスに従うことで、PowerShellスクリプトは安全で信頼性が高く、保守しやすいものになります。練習すれば、PowerShellスクリプトに習熟し、さまざまな管理タスクを簡単に自動化できるようになります。
