---
title: "PowerShellでActive Directory管理をマスターする：インストールと使用ガイド"
date: 2023-07-25
toc: true
draft: false
description: "PowerShellのActive Directoryモジュールを効果的にインストールし、活用することで、Windows Active Directoryの管理タスクを効率化する方法をご紹介します。"
genre: ["テクノロジー", "ウィンドウズ", "パワーシェル", "アクティブディレクトリ", "管理部門", "スクリプト", "IT", "オートメーション", "Windowsサーバー", "マイクロソフト"]
tags: ["PowerShell用アクティブ・ディレクトリ・モジュール", "PowerShellでモジュール・アクティブ・ディレクトリをインポートする", "Windows PowerShell用アクティブ・ディレクトリ・モジュール", "アクティブディレクトリPowerShellインストール", "アクティブディレクトリをインストール PowerShell", "PowerShellのインストールアクティブディレクトリモジュールWindows 10", "アクティブディレクトリをインストール PowerShellモジュール Windows 10", "アクティブディレクトリを取得する PowerShellモジュール", "AD管理", "Windows Active Directory", "PowerShellコマンドレット", "AD情報を検索する", "ADオブジェクトの作成", "ADオブジェクトを変更する", "ADのセキュリティを管理する", "ADユーザー管理", "ADグループ管理", "AD OR マネジメント", "PowerShellスクリプティング", "Windowsサーバー管理", "Microsoft PowerShell", "ADタスクの自動化", "PowerShellモジュールのインストール", "AD管理ガイド", "Active Directoryの管理", "ADセキュリティ管理", "PowerShellオートメーション", "Active Directory PowerShellコマンド", "PowerShellコマンドレットのリファレンス"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Active Directoryの管理と自動化を象徴する、相互接続されたサーバーとユーザーアイコンのネットワークを描いたイメージ。"
coverCaption: "PowerShellでActive Directory管理のパワーを解き放つ。"
---

#はじめに

今日のデジタル環境では、Windows Active Directory (AD)環境でユーザーアカウント、セキュリティグループ、その他のリソースを管理・維持するには、効率的で合理的なプロセスが必要です。Microsoftによって開発された強力なスクリプト言語であるPowerShellは、AD管理タスクを容易にするために**Active Directoryモジュール**を提供しています。このモジュールには、管理者がさまざまな操作を自動化し、ADを効率的に管理できるようにするさまざまなコマンドレットが用意されています。今回は、PowerShellのActive Directoryモジュールのインストールと使用方法について説明します。

## PowerShell 用 Active Directory モジュールのインストール

PowerShellのActive Directoryモジュールを使い始めるには、システムにActive Directoryモジュールがインストールされていることを確認する必要があります。インストール方法はOSによって異なります。以下は、**Windows 10**, **Windows 11**, **Windows Server** へのモジュールのインストール手順です：

### Windows 10 および Windows 11 - PowerShell
1.Windows PowerShell**を管理者権限で開きます。
2.以下のコマンドを実行して、モジュールをインストールする：

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1.インストールが完了するまで待ちます。完了したら、Active Directoryモジュールの使用を開始できます。

### Windows Server
1.Windows PowerShell**を管理者権限で開きます。
2.以下のコマンドを実行して、モジュールをインストールします：

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3.インストールが完了するまで待ちます。完了したら、Active Directoryモジュールの使用を開始できます。

### オフラインシステム

オフラインシステムは少し複雑になります。いくつかの方法がありますが、お勧めは以下のスクリプトを使用する方法です：
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## PowerShellでActive Directoryモジュールをインポートする

PowerShellでActive Directoryモジュールを利用する前に、現在のセッションにインポートする必要があります。以下の手順でモジュールをインポートしてください：

1.Windows PowerShell**を管理者権限で起動します。
2.以下のコマンドを実行して、モジュールをインポートします：

```powershell
Import-Module ActiveDirectory
```

3.Active Directoryモジュールがインポートされ、そのコマンドレットと関数にアクセスできるようになります。

## PowerShell の Active Directory モジュールを使う

Active Directoryモジュールがインポートされると、豊富なコマンドレットを活用して様々な管理タスクを実行できるようになります。ここでは、よく使用されるコマンドレットとその機能について説明します：

### Active Directory情報の取得

Active Directory (AD) 環境を効果的に管理するには、ユーザー、グループ、組織単位 (OU) など、さまざまな AD オブジェクトに関する情報を取得することが重要です。PowerShell には、検索プロセスを簡素化する強力なコマンドレットが用意されています。

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps)このコマンドレットを使用すると、AD ユーザーの詳細情報を取得することができます。ユーザー名、表示名、電子メールアドレスなどの属性を取得することができます。例えば、ユーザー名が "johndoe" で始まるすべてのユーザーを取得するには、以下のコマンドを実行します：

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  このコマンドは、指定されたフィルターに一致するユーザー・オブジェクトのリストを返す。

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps)Get-ADGroup コマンドレットを使用すると、AD グループに関する情報を取得できます。これは、グループ名、メンバー、説明などの詳細へのアクセスを提供します。たとえば、AD 環境内のすべてのセキュリティ グループを取得するには、次のコマンドを実行します：

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Active Directoryのセキュリティグループのリストが表示されます。

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps)Get-ADOrganizationalUnit コマンドレットは、AD OU に関する情報を取得するために使用されます。OU 名、説明、親 OU などのプロパティにアクセスすることができます。ドメイン内のすべての OU を取得するには、次のコマンドを使用します：

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  このコマンドを実行すると、Active Directory内のすべてのOUのリストが表示される。

これらの強力なコマンドレットを使用することで、ADユーザー、グループ、OUに関する特定の情報を簡単に取得することができ、Active Directory環境の効率的な管理・運用が可能になります。


これらのコマンドレットを使用すると、特定の属性を取得したり、結果をフィルタリングしたり、必要な情報を取得するための高度なクエリを実行したりすることができます。

### Active Directory オブジェクトの作成と管理

Active Directory (AD) を使用する場合、PowerShell の Active Directory モジュールには、AD オブジェクトを作成および管理するための強力なコマンドレットが用意されています。ここでは、AD ユーザー、グループ、および組織単位 (OU) の作成に不可欠なコマンドレットについて説明します。

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps)このコマンドレットは、新しい AD ユーザーを作成することができます。ユーザー名、パスワード、電子メールアドレスなどの属性を指定することができます。例えば、ユーザー名「john.doe」、表示名「John Doe」で新規ユーザーを作成するには、以下のコマンドを使用します：

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  このコマンドはActive Directoryに新しいユーザーを作成する。

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps)New-ADGroup コマンドレットを使用すると、新しい AD グループを作成できます。グループ名、説明、グループ スコープなどのプロパティを設定することができます。説明付きの「Marketing」という名前の新しいグループを作成するには、以下のコマンドを実行します：

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  このコマンドはActive Directoryに新しいグループを作成する。

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps)New-ADOrganizationalUnit コマンドレットを使用すると、新しい AD OU を作成できます。OU 名、親 OU などのプロパティを指定することができます。例えば、「Departments」OUの下に「Sales」という新しいOUを作成するには、以下のコマンドを実行します：

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  このコマンドは、Active Directory階層に新しいOUを作成する。

これらのコマンドレットを活用することで、必要なプロパティや設定を持つ新しいADユーザー、グループ、OUを簡単に作成することができ、Active Directory環境の効率的な管理が可能になります。


### Active Directoryオブジェクトの変更

既存の Active Directory (AD) オブジェクトのプロパティや属性を変更する場合、PowerShell の Active Directory モジュールには便利なコマンドレットがいくつか用意されています。ここでは、AD ユーザー、グループ、および組織単位 (OU) を変更するためのこれらのコマンドレットについて説明します。

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps)Set-ADUser コマンドレットは、AD ユーザーのプロパティを変更することができます。表示名、電子メール アドレス、電話番号などの属性を更新することができます。たとえば、ユーザー名「john.doe」のユーザーの電話番号を変更するには、次のコマンドを使用します：

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  このコマンドは、Active Directory内の指定したユーザーの電話番号を変更する。

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps)Set-ADGroup コマンドレットを使用すると、AD グループのプロパティを変更できます。グループの説明、メンバーシップ、グループ スコープなどの属性を更新することができます。Marketing」という名前のグループの説明を「Marketing Team」に変更するには、以下のコマンドを実行します：

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  このコマンドは、Active Directoryの指定されたグループの説明を更新します。

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps)Set-ADOrganizationalUnit コマンドレットは、AD OU のプロパティを変更することができます。OU 名、説明などの属性を変更することができます。たとえば、"Sales" という名前の OU の説明を "Sales Department" に変更するには、次のコマンドを実行します：

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  このコマンドは、Active Directory階層内の指定されたOUの説明を更新します。

これらのコマンドレットを使用することで、ADオブジェクトのプロパティや属性を簡単に変更し、組織の要件に合わせて必要な更新や調整を行うことができます。


### Active Directoryセキュリティの管理

PowerShell の Active Directory モジュールには、Active Directory (AD) オブジェクトの管理・運用に加え、AD のセキュリティ関連に特化したコマンドレットが用意されています。これらのコマンドレットを使用すると、管理者は、AD 環境内のユーザー アクセス、グループ メンバーシップ、およびパスワード関連のタスクを効率的に管理できます。

以下は、よく使用されるセキュリティ関連のコマンドレットです：

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps)このコマンドレットを使用すると、AD グループにメンバーを追加することができます。AD グループと追加したいユーザー アカウントまたはグループを指定することで、簡単にアクセス制御を管理することができます。例えば、「JohnDoe」というユーザーを「Managers」グループに追加するには、以下のコマンドを使用します：

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps)このコマンドレットを使用すると、AD グループからメンバーを削除することができます。AD グループと、削除したいユーザー アカウントまたはグループを指定することで、グループ メンバーシップを効率的に管理することができます。例えば、「Developers」グループから「JaneSmith」というユーザーを削除するには、以下のコマンドを使用します：

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps)このコマンドレットを使用すると、AD ユーザーのパスワードを設定することができます。ユーザー アカウントを指定し、新しいパスワードを提供することで、パスワード ポリシーを実施し、安全なユーザー認証を確保することができます。以下は、「AmyJohnson」という名前のユーザーに新しいパスワードを設定する例です：

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

これらのセキュリティ関連コマンドレットを利用することで、管理者はActive Directory環境内のユーザーアクセス、グループメンバーシップ、パスワードポリシーを効果的に管理することができる。

## PowerShell 用 Active Directory モジュールスクリプトの例
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

結論として、**Active Directory module for PowerShell**は、Windows Active Directoryを効率的かつ便利に管理できる強力なツールである。このモジュールをインストールし、インポートすることで、AD関連の様々なタスクを簡素化する**コマンドレット**の包括的なセットにアクセスできるようになります。

Active Directoryモジュールを使用すると、ADオブジェクトに関する情報の取得、新しいオブジェクトの作成、プロパティの変更、セキュリティの管理など、幅広い操作を実行できます。このモジュールにより、管理者は管理タスクを自動化し、ワークフローを合理化し、Active Directory環境を円滑に機能させることができます。

PowerShell**と**Active Directoryモジュール**を活用することで、AD管理能力を強化し、AD管理プロセスの効率を向上させることができます。システム管理者、ITプロフェッショナル、Active Directory管理者のいずれであっても、Active DirectoryモジュールはADインフラストラクチャを効果的に管理するために必要なツールを提供します。

PowerShell**と**Active Directoryモジュール**のパワーで、AD管理作業を効率化し、生産性を向上させ、安全で整ったActive Directory環境を維持しましょう。

## 参考文献

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
