---
title: "PowerShellで読み取り専用のActive Directoryインベントリを作成する"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "範囲を限定したPowerShellクエリでActive DirectoryのOU、ユーザー、コンピューターを一覧化します。ディレクトリオブジェクトを変更せず、確認可能なCSVファイルへエクスポートします。"
genre: ["Active Directory", "PowerShell", "システム管理"]
tags: ["Active Directoryインベントリ", "PowerShell ADインベントリ", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "読み取り専用AD", "ADユーザーのエクスポート", "ADコンピューターのエクスポート", "AD OUのエクスポート", "Export-Csv", "RSAT", "ディレクトリ監査", "ADレポート", "OUインベントリ", "Windows Server", "PowerShellスクリプト", "ADモジュール", "ディレクトリ衛生"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Active Directoryのツリーからユーザー、コンピューター、組織単位の記録が3つの確認用ファイルへ流れる図。"
coverCaption: "クエリの範囲を限定し、確認に必要なフィールドだけをエクスポートします。"
---
Active Directoryの整理は、存在するオブジェクトを正確に把握することから始まります。この**読み取り専用インベントリ**は、選択した範囲の組織単位、ユーザー、コンピューターを収集します。ディレクトリオブジェクトを変更せず、確認用のCSV（カンマ区切り値）ファイルを3つエクスポートします。名前やデバイス情報から環境の一部が分かるため、ファイルの保護も必要です。

<!--more-->

## 主なポイント

- **範囲を選ぶ:** ドメイン全体に広げる前に、1つの組織単位をクエリします。
- **読み取りコマンドを使う:** `Get-ADOrganizationalUnit`、`Get-ADUser`、`Get-ADComputer`でオブジェクトを取得します。
- **フィールドを選ぶ:** 作業に必要なプロパティだけをエクスポートします。
- **出力を確認する:** レポートを信頼する前に、件数とサンプル行を比較します。

## 開始前の準備

Windows管理用ホスト、正常なDNS、ドメインコントローラーへのネットワークアクセス、PowerShellの**ActiveDirectory**モジュール、選択したオブジェクトの読み取りを許可されたアカウント、CSV出力用の保護されたフォルダーが必要です。Windowsクライアントでは、モジュールはRemote Server Administration Tools（RSAT）のActive Directoryツールに含まれます。インストール方法は[Active Directoryモジュールガイド](/articles/active-directory-module-powershell-installation-usage-guide/)を参照してください。Microsoftはモジュールの[コマンドレットリファレンス](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)と[RSATのインストール方法](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools)を掲載しています。このガイドではWindows PowerShell構文を使い、ディレクトリオブジェクトを変更しません。

ディレクトリのアクセス許可は引き続き適用されます。Microsoftの[特権アカウントに関するガイダンス](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory)によると、アクセス制御リストは認証済みユーザーに一般情報の読み取りを許可し、機密フィールドや変更を制限する場合がよくあります。まず承認済みアカウントとテスト用OUを使ってください。インベントリを成功させるためにDomain Adminへ権限を昇格しないでください。

> **警告:** CSVファイルにはアカウント名とコンピューター名が含まれます。承認された場所に保存し、アクセスを制限し、確認後に余分なコピーを削除してください。生のエクスポートを公開したり、公開Issueに添付したりしないでください。

## 検索ベースを選ぶ

**組織単位（OU）**はディレクトリオブジェクトをグループ化します。その**識別名（DN）**はディレクトリツリー内の位置を示します。`-SearchBase`パラメーターは、選択したDNにクエリを限定します。範囲を意図的に指定しないと、広いフィルターが確認に必要な数を大きく超えるオブジェクトを返す場合があります。

まずモジュールを読み込み、現在のドメインDNを確認します:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoftは[Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain)と、コマンドレットが返すドメイン情報を説明しています。検索ベースを設定する前に、確認対象のOUを見つけます:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

結果から正確なDNをコピーします。以降の例では、この説明用の値を自分のOUのDNに置き換えてください:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com`は説明用のドメインです。実際のクエリにこのDNをコピーしないでください。意図的にドメイン全体のインベントリを作成する場合は、`$SearchBase`にドメインDNを設定し、レポートに広い範囲を記録します。Microsoftの[Get-ADOrganizationalUnitリファレンス](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit)では、`-Filter`と`-SearchBase`を説明しています。

## OU、ユーザー、コンピューターを一覧化する

最初にオブジェクト数を確認します。検索ベースの誤りや予期しない空の結果をすぐに見つける手掛かりになります:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *`は検索ベース内の一致するオブジェクトをすべて取得する指定です。Microsoftは[Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser)と[Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer)を取得コマンドとして説明しています。件数が0でも正しい場合はありますが、インベントリが完全だと判断する前にDN、アクセス許可、対象ドメインを確認してください。

次に、コンソールで数行をプレビューします。選択したフィールドを保存すると、プレビューと後のCSVエクスポートで同じ列を使えます:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

コンピューターの追加のオペレーティングシステム属性は、確認に必要な場合だけ要求します:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

`-Properties`パラメーターは、コマンドレットの既定セットにないプロパティを要求します。Microsoftの[コンピューター用コマンドレットリファレンス](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer)で説明されています。オペレーティングシステム名はディレクトリデータとして扱い、現在インストールされているバージョンの証明と見なさないでください。コンピューターオブジェクトが古い場合や、属性が未更新の場合があります。

## 確認用CSVをエクスポートする

十分な空き容量があり、承認された出力フォルダーを選びます。次のコマンドは**ローカルCSVファイル**を書き込みますが、ディレクトリオブジェクトは変更しません。このフォルダーで実行してください。`-NoClobber`は既存ファイルの上書きを防ぎます。実行ごとに新しいフォルダーまたはファイル名を使ってください。

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Microsoftの[Export-Csvリファレンス](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1)では、`-NoTypeInformation`、`-Encoding`、`-NoClobber`を説明しています。各CSVをテキストエディターまたは承認済みの表計算ツールで開きます。ヘッダー、数行、先ほど数えたレコード数を確認してください。コマンドの失敗や0バイトのファイルは、完全なレポートの証拠になりません。

> **期待される結果:** 選択したディレクトリ範囲に含まれるOU、ユーザー、コンピューターの3つのCSVファイルができます。行数とサンプル値が選択範囲と一致します。

## オブジェクトを変更せずに確認する

インベントリを使って、コンピューターを担当するOU、無効なユーザーアカウント、所有者が必要なデバイス名など、具体的な質問に答えます。所見は別の確認メモに記録します。`Enabled`の値だけでアカウントが不要だと判断しないでください。エクスポートだけを根拠にオブジェクトを削除または無効化しないでください。

定期レポートでは、クエリ日、ドメイン、OUのDN、選択したプロパティ、実行者、CSVの保存場所を記録します。2つのエクスポートを比較する場合は、同じ範囲とフィールドを使ったことを確認してください。そうしないと、差分がディレクトリの実際の変更ではなく、クエリの違いから生じる場合があります。

これは**インベントリ**であり、特権アカウント監査やログイン活動レポートではありません。Microsoftは、Active Directoryのプロパティとアクセス許可がオブジェクトや環境によって異なると説明しています。オペレーティングシステム属性や表示名に基づいて行動する前に、システム所有者へ確認してください。より広いセキュリティ対策は[Active Directoryセキュリティガイド](/articles/active-directory-security-best-practices/)を参照してください。

## トラブルシューティング

- **モジュールをインポートできない:** ホストにRSATのActive DirectoryツールまたはWindows Server管理ツールがインストールされているか確認します。[モジュール設定ガイド](/articles/active-directory-module-powershell-installation-usage-guide/)を参照してください。
- **クエリがオブジェクトを返さない:** 正確なDN、現在のドメイン、OUの内容、読み取り権限を確認します。範囲を広げる前に、既知の小さなOUを試してください。
- **プロパティが空:** 属性が存在し、アカウントに読み取り権限があるか確認します。不足項目を推測で埋めないでください。
- **エクスポートでファイルが既に存在すると表示される:** `-NoClobber`が前のレポートを保護しました。新しいファイル名またはフォルダーを選んで再実行します。
- **件数が想定と異なる:** ユーザーやコンピューターが別のOUにあるか、範囲が変わったか、クエリ中にディレクトリが変更されたか確認します。

## 次のステップ

合意した確認期間中、生のCSVファイルを保護された場所に保管します。確認者に共有するのは必要なフィールドだけにしてください。担当者が所見を確認した後、通常の承認とロールバック手順に従って変更を計画します。承認済みの変更後、同じ範囲で同じインベントリを再実行し、結果を確認してください。