---
title: "PowerShellによるActive Directory管理"
date: 2023-07-25
toc: true
draft: false
description: PowerShell用のActive Directoryモジュールを効果的にインストールし、使用する方法を学び、Windows Active Directoryの管理作業を簡素化しましょう。
genre:
- テクノロジー
- Windows
- PowerShell
- Active Directory
- 管理
- スクリプティング
- IT
- 自動化
- Windows Server
- Microsoft
tags:
- PowerShell用Active Directoryモジュール
- PowerShellでActive Directoryモジュールをインポート
- Windows PowerShell用Active Directoryモジュール
- Active Directory PowerShellインストール
- Active Directory PowerShellをインストール
- Windows 10でPowerShellにActive Directoryモジュールをインストール
- Windows 10でActive Directory PowerShellモジュールをインストール
- Active Directory PowerShellモジュールを取得
- AD管理
- Windows Active Directory
- PowerShellコマンドレット
- AD情報を取得
- ADオブジェクトを作成
- ADオブジェクトを変更
- ADセキュリティを管理
- ADユーザー管理
- ADグループ管理
- AD OU管理
- PowerShellスクリプティング
- Windows Server管理
- Microsoft PowerShell
- ADタスクを自動化
- PowerShellモジュールのインストール
- AD管理ガイド
- Active Directory管理
- ADセキュリティ管理
- PowerShell自動化
- Active Directory PowerShellコマンド
- PowerShellコマンドレットリファレンス
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: カラフルなコマンドレットが表示されたPowerShellコンソールのコンピュータ画面のイラスト。ユーザーアカウントやグループを抽象的に表現したものに囲まれ、暗い背景に配置されています。
coverCaption: PowerShellでActive Directory管理の力を解き放つ。
lastmod: 2026-10-08
---

## はじめに

今日、Windows Active Directory（AD）環境でユーザーアカウント、セキュリティグループ、その他のリソースを管理・維持するには、効率的で簡素化されたプロセスが必要です。Microsoftが開発した強力なスクリプト言語であるPowerShellは、AD管理作業を支援する**Active Directoryモジュール**を提供しています。このモジュールは、多くのコマンドレットを備えており、管理者がさまざまな操作を自動化し、ADを効果的に管理できるようにします。本記事では、PowerShell用Active Directoryモジュールのインストールと使用方法を探ります。

## PowerShell用Active Directoryモジュールのインストール

PowerShell用Active Directoryモジュールを使用開始するには、システムにインストールされていることを確認する必要があります。インストール手順はOSによって異なる場合があります。以下は**Windows 10**、**Windows 11**、および**Windows Server**でのモジュールインストール手順です。

### Windows 10およびWindows 11 - PowerShell
1. 管理者権限で**Windows PowerShell**を開きます。
2. 次のコマンドを実行してモジュールをインストールします。

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. インストールが完了するまで待ちます。完了後、Active Directoryモジュールを使用開始できます。

### Windows Server 
1. 管理者権限で**Windows PowerShell**を開きます。
2. 次のコマンドを実行してモジュールをインストールします。

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. インストールが完了するまで待ちます。完了後、Active Directoryモジュールを使用開始できます。

### オフラインシステム

オフラインシステムは少し複雑です。いくつか方法がありますが、推奨するのは以下のスクリプトを使用する方法です。
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## PowerShellでのActive Directoryモジュールのインポート

PowerShellでActive Directoryモジュールを使用する前に、現在のセッションにインポートする必要があります。以下の手順でモジュールをインポートしてください。

1. 管理者権限で**Windows PowerShell**を起動します。
2. 次のコマンドを実行してモジュールをインポートします。

```powershell
Import-Module ActiveDirectory
```

3. Active Directoryモジュールがインポートされ、コマンドレットや関数にアクセスできるようになります。

## PowerShell用Active Directoryモジュールの使用

Active Directoryモジュールをインポートしたら、その豊富なコマンドレットを活用してさまざまな管理作業を行えます。以下はよく使われるコマンドレットとその機能の一例です。

### Active Directory情報の取得

Active Directory（AD）環境を効果的に管理するには、ユーザー、グループ、組織単位（OU）などのADオブジェクトに関する情報を取得する必要があります。PowerShellは取得作業を簡素化する強力なコマンドレットを提供します。

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): このコマンドレットはADユーザーの詳細情報を取得できます。ユーザー名、表示名、メールアドレスなどの属性を取得可能です。例えば、ユーザー名が「johndoe」で始まるすべてのユーザーを取得するには、次のコマンドを実行します。

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  このコマンドは指定したフィルターに一致するユーザーオブジェクトの一覧を返します。

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): Get-ADGroupコマンドレットを使うと、ADグループの情報を取得できます。グループ名、メンバー、説明などの詳細にアクセス可能です。例えば、AD環境内のすべてのセキュリティグループを取得するには、次のコマンドを実行します。

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  これによりActive Directory内のセキュリティグループの一覧が表示されます。

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): Get-ADOrganizationalUnitコマンドレットはADのOU情報を取得するために使用します。OU名、説明、親OUなどのプロパティにアクセス可能です。ドメイン内のすべてのOUを取得するには、次のコマンドを使用します。

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  このコマンドを実行するとActive Directory内のすべてのOUの一覧が表示されます。

これらの強力なコマンドレットを使うことで、ADユーザー、グループ、OUに関する特定の情報を簡単に取得でき、Active Directory環境の効率的な管理が可能になります。


これらのコマンドレットは特定の属性を取得したり、結果をフィルターしたり、高度なクエリを実行して必要な情報を取得できます。

### Active Directoryオブジェクトの作成と管理

Active Directory（AD）を操作する際、PowerShellのActive DirectoryモジュールはADオブジェクトの作成と管理に強力なコマンドレットを提供します。ここではADユーザー、グループ、組織単位（OU）を作成するための主要なコマンドレットを紹介します。

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): このコマンドレットは新しいADユーザーを作成します。ユーザー名、パスワード、メールアドレスなどの属性を指定可能です。例えば、ユーザー名「john.doe」、表示名「John Doe」の新規ユーザーを作成するには、次のコマンドを使用します。

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  このコマンドはActive Directoryに新しいユーザーを作成します。

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): New-ADGroupコマンドレットは新しいADグループを作成します。グループ名、説明、グループスコープなどのプロパティを設定可能です。例えば、「Marketing」という名前で説明付きの新規グループを作成するには、次のコマンドを実行します。

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  このコマンドはActive Directoryに新しいグループを作成します。

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): New-ADOrganizationalUnit コマンドレットを使用すると、新しい AD OU を作成できます。OU 名、親 OU などのプロパティを指定できます。例えば、「Departments」OU の下に「Sales」という名前の新しい OU を作成するには、次のコマンドを実行します。

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  このコマンドは、Active Directory 階層に新しい OU を作成します。

これらのコマンドレットを使用することで、必要なプロパティや設定を持つ新しい AD ユーザー、グループ、OU を簡単に作成でき、Active Directory 環境の効率的な管理が可能になります。


### Active Directory オブジェクトの変更

既存の Active Directory (AD) オブジェクトのプロパティや属性を変更する場合、PowerShell の Active Directory モジュールには便利なコマンドレットがいくつか用意されています。ここでは、AD ユーザー、グループ、組織単位 (OU) を変更するためのコマンドレットを紹介します。

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): Set-ADUser コマンドレットを使うと、AD ユーザーのプロパティを変更できます。表示名、メールアドレス、電話番号などの属性を更新可能です。例えば、ユーザー名が「john.doe」のユーザーの電話番号を変更するには、次のコマンドを使用します。

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  このコマンドは、指定したユーザーの電話番号を Active Directory 内で変更します。

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): Set-ADGroup コマンドレットを使うと、AD グループのプロパティを変更できます。グループの説明、メンバーシップ、グループのスコープなどの属性を更新可能です。例えば、「Marketing」というグループの説明を「Marketing Team」に変更するには、次のコマンドを実行します。

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  このコマンドは、指定したグループの説明を Active Directory 内で更新します。

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): Set-ADOrganizationalUnit コマンドレットを使うと、AD OU のプロパティを変更できます。OU 名、説明などの属性を変更可能です。例えば、「Sales」という OU の説明を「Sales Department」に変更するには、次のコマンドを実行します。

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  このコマンドは、指定した OU の説明を Active Directory 階層内で更新します。

これらのコマンドレットを使用することで、AD オブジェクトのプロパティや属性を簡単に変更でき、組織の要件に合わせた必要な更新や調整が可能になります。


### Active Directory セキュリティの管理

Active Directory (AD) オブジェクトの管理・運用に加え、PowerShell の Active Directory モジュールには AD のセキュリティ関連の管理に特化したコマンドレットも用意されています。これらのコマンドレットは、管理者が AD 環境内のユーザーアクセス、グループメンバーシップ、パスワード関連のタスクを効率的に管理するのに役立ちます。

以下はよく使われるセキュリティ関連のコマンドレットです。

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): このコマンドレットは、AD グループにメンバーを追加できます。AD グループと追加したいユーザーアカウントやグループを指定することで、アクセス制御を簡単に管理可能です。例えば、「Managers」グループに「JohnDoe」というユーザーを追加するには、次のコマンドを使用します。

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): このコマンドレットは、AD グループからメンバーを削除できます。AD グループと削除したいユーザーアカウントやグループを指定することで、グループメンバーシップを効果的に管理可能です。例えば、「Developers」グループから「JaneSmith」というユーザーを削除するには、次のコマンドを使用します。

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): このコマンドレットは、AD ユーザーのパスワードを設定できます。ユーザーアカウントを指定し、新しいパスワードを提供することで、パスワードポリシーを適用し、安全なユーザー認証を確保します。例えば、「AmyJohnson」というユーザーの新しいパスワードを設定する例は以下の通りです。

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

これらのセキュリティ関連コマンドレットを使用することで、管理者は Active Directory 環境内のユーザーアクセス、グループメンバーシップ、パスワードポリシーを効果的に管理できます。

## PowerShell 用 Active Directory モジュールの例スクリプト
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## 結論

まとめると、**PowerShell 用 Active Directory モジュール** は、Windows Active Directory の効率的かつ便利な管理を可能にする強力なツールです。モジュールをインストールしてインポートすることで、さまざまな AD 関連タスクを簡素化する包括的な **コマンドレット** にアクセスできます。

Active Directory モジュールを使えば、AD オブジェクトの情報取得、新規作成、プロパティの変更、セキュリティ管理など多くの操作を実行できます。このモジュールは管理者が管理タスクを自動化し、ワークフローを簡素化し、Active Directory 環境の円滑な運用を支援します。

**PowerShell** と **Active Directory モジュール** を活用することで、AD 管理能力を向上させ、AD 管理プロセスの効率化が図れます。システム管理者、IT プロフェッショナル、Active Directory 管理者のいずれであっても、このモジュールは AD インフラを効果的に管理するための必要なツールを提供します。

**PowerShell** と **Active Directory モジュール** の力を活用して、AD 管理タスクを簡素化し、生産性を高め、安全で整然とした Active Directory 環境を維持しましょう。

## 参考文献

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
