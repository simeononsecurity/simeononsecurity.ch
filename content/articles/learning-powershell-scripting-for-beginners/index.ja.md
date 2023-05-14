---
title: "初心者のためのPowerShellスクリプト：ステップバイステップガイド"
draft: false
toc: true
date: 2023-02-25
description: "PowerShellスクリプトの基本を学び、このステップバイステップガイドを使って自動化を始めましょう。"
tags: ["パワーシェル", "スクリプト", "ウィンドウズ", "オートメーション", "コマンドレット", "モジュール", "ループス", "条件付き文", "機能", "さいぜんのそち", "デバッギング", "テスティング", "変数", "PowerShell ISE", "PowerShellリモーティング", "マイクロソフトテクノロジー", "インフォメーション", "けいさんきかんり", "コーディング", "管理業務"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "スクリプトを持ち、PowerShellプロンプトのあるPCの前に立つ漫画のキャラクターは、初心者のためのPowerShellスクリプトの容易さを示しています。"
coverCaption: ""
---
初心者のためのPowerShellスクリプティング**」を開催します。

PowerShellは、Microsoft社が開発した強力なコマンドラインシェルとスクリプト言語です。Windowsオペレーティングシステムやその他のMicrosoftテクノロジーの様々な側面を管理し、自動化するための膨大な数のコマンドと機能を提供します。今回は、初心者向けにPowerShellスクリプトの基本を説明し、始めるためのステップバイステップのガイドを提供します。

## PowerShell入門

PowerShellは、Windowsオペレーティングシステムやその他のMicrosoftテクノロジーを自動化し、管理することを可能にするコマンドラインシェルです。ファイルやディレクトリの管理、ネットワーク設定、システム管理など、さまざまな管理タスクを実行するための包括的なコマンドと機能を提供します。また、PowerShellはスクリプト言語もサポートしており、複雑なスクリプトを作成したり、様々な反復作業を自動化することができます。

## PowerShell 入門

### PowerShell のインストール

PowerShellは、ほとんどのバージョンのWindowsオペレーティングシステムにプリインストールされています。ただし、古いバージョンのWindowsを使用している場合や、より新しいバージョンのPowerShellが必要な場合は、Microsoftのウェブサイトからダウンロードすることができます。PowerShellのダウンロードとインストールは、以下の手順で行います：

1.にアクセスします。[Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2)をクリックし、インストールするPowerShellのバージョンを選択します。
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
PowerShell ISE (Integrated Scripting Environment) は、PowerShell スクリプトのためのグラフィカルユーザーインターフェイスです。PowerShell ISEは、リッチテキストエディタ、デバッグツール、およびPowerShellスクリプトの作成とテストを容易にするその他の機能を提供します。PowerShell ISEを開くには、次の手順に従います：

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
PowerShell スクリプトを記述する場合、スクリプトの安全性、信頼性、および保守性を確保するために、ベストプラクティスに従うことが重要である。ここでは、留意すべきベストプラクティスをいくつか紹介します：

説明的な変数名を使用する：目的を明確に示す変数名を使用する。
コメントを使用する：コメントの使用：コードの目的を説明するためにコメントを使用します。
- エラー処理**を使用する：エラーハンドリングを使用して、エラーや例外を優雅に処理する。
- スクリプトを徹底的にテストする**：スクリプトを徹底的にテストし、期待通りに動作することを確認する。
- 関数とモジュールを使用する：関数とモジュールを使用する**：コードを整理し、再利用性を向上させるために関数とモジュールを使用する。
- 値のハードコーディングは避ける**：スクリプト内の値のハードコーディングは避け、代わりにパラメータや変数を使用する。
- 冗長出力を使用する**：スクリプトの進行に関する追加情報を提供するために冗長出力を使用します。

### PowerShell スクリプティングのベストプラクティスを詳しく説明します。

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

### 初心者のためのPowershellスクリプトの10のアイデア

- **バックアップの自動化**：重要なファイルやディレクトリを外付けハードドライブやクラウドストレージサービスにバックアップするプロセスを自動化するスクリプトを作成します。
- ファイル管理**：ファイル管理**：ファイルやディレクトリを、ファイルの種類やサイズなどの条件に基づいて異なるフォルダーに分類し、整理するスクリプトを作成します。
- システム情報**：CPUやメモリの使用量、ディスク容量、ネットワーク設定などのシステム情報を取得し、見やすく表示するスクリプトを作成します。
- ユーザー管理**：ユーザー管理**：Windows オペレーティングシステムのユーザーやグループの追加、変更、削除を自動化するスクリプトを作成する。
- ソフトウエアのインストール**：ソフトウェアのインストール**：一度に複数のコンピューターにソフトウェアをインストールし、設定するスクリプトを作成し、時間と労力を節約する。
- ネットワーク設定**：ネットワーク設定**：IPアドレス、サブネットマスク、デフォルトゲートウェイなどのネットワーク設定のプロセスを自動化するスクリプトを作成することができます。
- **セキュリティ**：セキュリティ**：セキュリティ設定の監査と監視を行い、変更が検出された場合にユーザーに警告を発するスクリプトを作成します。
- タスクスケジューリング**：バックアップ、アップデート、システムスキャンなどの定期的なタスクをスケジュールし、自動化するスクリプトを作成します。
- レジストリ操作**：レジストリ操作**：特定のキーや値のレジストリ値を変更または取得するスクリプトを作成します。
- リモート管理**：Windows コンピュータのリモート管理を可能にするスクリプトを作成し、ユーザーがリモートマシン上でコマンドやスクリプトを実行できるようにします。

## 結論

PowerShell は、Windows オペレーティングシステムやその他の Microsoft テクノロジーを管理し、自動化するための強力なツールです。この記事では、PowerShellのインストールと起動、コマンドレット、変数、ループ、条件文、関数の使用、PowerShell ISE、PowerShell Remoting、PowerShellモジュールの使用など、初心者向けのPowerShellスクリプトの基本を説明しました。ベストプラクティスに従うことで、PowerShellスクリプトは安全で信頼性が高く、保守しやすいものになります。練習すれば、PowerShellスクリプトに習熟し、さまざまな管理タスクを簡単に自動化できるようになります。
