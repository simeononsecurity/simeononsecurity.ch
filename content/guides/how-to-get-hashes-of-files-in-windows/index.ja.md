---
title: "完全ガイド：PowerShellを使ったWindowsでのファイルハッシュ"
draft: false
toc: true
date: 2023-05-25
description: "PowerShellを使用して、SHA256、MD5、SHA1などのファイルハッシュをWindows上で取得する方法を、ステップバイステップの手順と例で紹介します。"
tags: ["ファイルハッシュ", "パワーシェル", "SHA256ハッシュ", "MD5ハッシュ", "SHA1ハッシュ", "ファイルの完全性", "データ認証", "ファイル検証", "ハッシュアルゴリズム", "Windows オペレーティングシステム", "スクリプト言語", "コマンドラインシェル", "データ機密保護", "デジタルフォレンジック", "サイバーセキュリティ", "ハッシュ計算", "ファイル改ざん", "データの完全性", "ファイルしんようせい", "Windowsのセキュリティ", "ファイル識別", "サイバーディフェンス", "ファイルセキュリティ", "データ保護", "データ検証", "ファイルバリデーション", "Windows PowerShell", "ハッシュ生成", "ハッシュアルゴリズム", "ハッシュ関数"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "ファイルのハッシュ認証とセキュリティを表現した、ロックマークと虫眼鏡を持つファイルを示す漫画のイラスト。"
coverCaption: ""
---

**PowerShellを使用してWindows上のファイルのハッシュを取得する方法**。

コンピュータセキュリティの領域では、ファイルのハッシュを取得することは、データの整合性を確保し、ファイルの真正性を検証する上で重要なステップです。ハッシュは、ファイルに対して生成される一意の識別子であり、ユーザーは改ざんの試みを検出し、データの整合性を検証することができます。この包括的なガイドでは、強力なスクリプト言語である**PowerShell**を使用して、Windows上のファイルの**SHA256**、**MD5**、**SHA1**ハッシュを取得するプロセスについて説明します。ステップバイステップの指示に従いながら、具体的な例を深く掘り下げていきます。さあ、はじめましょう！

______

## PowerShell を使って Windows でハッシュを取得する。

Windows用の汎用スクリプト言語およびコマンドラインシェルであるPowerShellは、**Get-FileHash**コマンドレットを提供し、ユーザーが簡単にファイルのハッシュを計算することを可能にします。

### SHA256 ハッシュを取得する

PowerShellを使用してファイルの**SHA256ハッシュ**を取得するには、次の簡単な手順に従います：

1.1.スタートメニューからPowerShellを起動し、PowerShellを検索し、Windows PowerShellを選択します。
2.2.ファイルのあるディレクトリに移動します。を使用します。 `cd`コマンドの後に、ディレクトリへのパスを入力します。
3.以下のコマンドを実行し、ファイルのSHA256ハッシュを取得します：
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### MD5 と SHA1 のハッシュを取得する。
を取得することもできます。 `MD5`と `SHA1`PowerShellを使用して、ファイルのハッシュを取得します。以下のコマンドを活用する：

- ハッシュ値を取得するには `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- を得るために `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

どちらのコマンドも、"file_path "をファイルへのパスに置き換えることを忘れないでください。

## 例
WindowsのPowerShellでハッシュを取得する手順を、具体的な例で説明します。

{{< youtube id="UrHhsF1q3rU" >}}

### 例1：SHA256ハッシュを取得する
という名前のファイルがあるとします。 `document.pdf`ディレクトリにある `C:\Files`を得るために `SHA256 hash`このファイルのPowerShellを使用する場合は、以下のコマンドを実行します：

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

出力には、ファイルのSHA256ハッシュ値が表示されます。

### 例2：MD5ハッシュを取得する

例えば、以下のような名前のファイルを所有しているとします。 `image.jpg`ディレクトリに格納されている `C:\Photos`を得るために `MD5 hash`このファイルのPowerShellを使用して、次のコマンドを実行します：

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

端末には、ファイルのMD5ハッシュ値が表示されます。

### 例3：SHA1ハッシュの取得

という名前のファイルを持っている場合を考えてみましょう。 `data.txt`ディレクトリにある `C:\Documents`を得るために `SHA1 hash`このファイルのPowerShellを使用する場合は、以下のコマンドを実行します：

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

出力には、ファイルのSHA1ハッシュ値が表示されます。