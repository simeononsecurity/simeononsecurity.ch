---
title: "C#開発者のためのセキュアコーディングスタンダード"
date: 2023-02-28
toc: true
draft: false
description: "C#でセキュアコーディングのベストプラクティスを学び、セキュリティ侵害のリスクを最小化し、機密データを保護します。"
tags: ["シーシャープ", "えんぎ", "セキュリティ", "プログラミング", "ASP.NET", ".NET Core", "認証", "パスワードハッシュ", "にゅうりょくじゅり", "あんごうぎじゅつ", "おことわり", "スタティックコードアナライザ", "ウェブアプリケーション", "SQLインジェクション", "クロスサイトスクリプティング", "データ保護", "ヘルスチェック", "セッション管理", "オワスプ"]
cover: "/img/cover/A_cartoon_developer_with_a_lock_icon_as_the_head_surrounded.png"
coverAlt: "ロックアイコンを頭にした漫画の開発者が、コードに囲まれ、ファイアウォールに遮られている。"
coverCaption: ""
---

セキュアコーディングは、コードが安全で信頼性が高く、脆弱性のないものであることを保証するために不可欠です。C#は人気のあるプログラミング言語で、セキュリティリスクを防ぐために、開発者はセキュアコーディングの標準に従うことを要求されます。入力検証、安全でない関数の回避、暗号化ライブラリの使用、ライブラリやフレームワークの更新などのベストプラクティスに従うことで、開発者はコードが安全で脆弱性がないことを保証することができます。

_____

## 入力バリデーション

ユーザー入力は、しばしばセキュリティリスクの重大な原因となっています。入力検証とは、ユーザー入力が期待される条件を満たし、アプリケーションで使用しても安全であることを検証するプロセスです。例えば、ユーザーがクレジットカードの番号を入力する場合、入力されるのは数字のみで、特殊文字は含まれてはいけません。入力の検証を行うために、開発者は、以下のような組み込みのクラスを使用することができます。`Regex`で、入力が期待される条件を満たしていることを確認します。

```csharp
public static bool ValidateInput(string inputString)
{
    bool isValid = false;
    // Check if input string contains only digits
    if (Regex.IsMatch(inputString, @"^\d+$"))
    {
        isValid = true;
    }
    return isValid;
}
```

このメソッドは、正規表現を使用して、入力文字列が数字のみを含むかどうかをチェックします。入力が有効かどうかを示すブーリアン値を返します。

## 安全でない関数の使用を避ける
C#には、注意深く使用しないとセキュリティ上の問題が発生する可能性がある関数がいくつかあります。以下のような関数があります。`Process.Start()``Reflection`と`Deserialization`は、攻撃者に悪意のあるコードを実行させる可能性があります。開発者は、これらの関数の使用を避けるか、入力パラメータを制限して必要なときだけ使用するなどして、慎重に使用する必要があります。

例えば`Process.Start()`関数を使用して外部プロセスを開始する場合、開発者は、この関数を使用する必要があります。`Process.StartInfo`プロパティを使用して、引数やセキュリティの制限を提供します。
```csharp
ProcessStartInfo startInfo = new ProcessStartInfo
{
    FileName = "notepad.exe",
    Arguments = "example.txt",
    UseShellExecute = false,
    RedirectStandardOutput = true,
    CreateNoWindow = true
};

using (Process process = new Process())
{
    process.StartInfo = startInfo;
    process.Start();
    string output = process.StandardOutput.ReadToEnd();
    process.WaitForExit();
}
```
## 暗号化ライブラリの使用
Bouncy Castleや.NET FrameworkのCryptography APIなどの暗号化ライブラリは、暗号化および復号化処理を安全に実行する方法を提供します。これらのライブラリは、脆弱性がある可能性のあるカスタム暗号化メソッドを作成する代わりに使用してください。

例えば、パスワードを暗号化するためには`Rfc2898DeriveBytes`クラスを、.NET FrameworkのCryptography APIsから以下のように変更します：
```csharp
public static string EncryptPassword(string password)
{
    byte[] salt = new byte[16];
    using (var rng = new RNGCryptoServiceProvider())
    {
        rng.GetBytes(salt);
    }

    var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 10000);
    byte[] hash = pbkdf2.GetBytes(20);

    byte[] hashBytes = new byte[36];
    Array.Copy(salt, 0, hashBytes, 0, 16);
    Array.Copy(hash, 0, hashBytes, 16, 20);

    return Convert.ToBase64String(hashBytes);
}
```
のことです。`Rfc2898DeriveBytes`クラスは、ソルトを生成し、それを使ってパスワードから鍵を導出します。得られた鍵は、パスワードの暗号化に使用されます。

## 最小特権の原則に従え

最小特権の原則とは、セキュリティのベストプラクティスで、ユーザーやプロセスを、その機能を実行するために必要な最小レベルのアクセスに制限することです。開発者は、セキュリティ侵害の影響を最小限に抑えるために、コードを書くときにこの原則に従うべきです。

例えば、あるアプリケーションがデータベースへの読み取り専用アクセスを必要とする場合、完全な権限を持つアカウントではなく、読み取り専用権限を持つデータベースアカウントを使用する必要があります。これにより、攻撃者がアプリケーションを悪用してデータを変更したり削除したりするリスクを減らすことができます。

## ライブラリやフレームワークの更新を怠らない

ライブラリやフレームワークには、攻撃者に悪用される可能性のあるセキュリティ脆弱性が含まれていることがあります。開発者は、潜在的なセキュリティ問題を回避するために、ライブラリやフレームワークを常に最新版に更新しておく必要があります。

例えば、アプリケーションがサードパーティのライブラリを使用している場合、次のようになります。`Newtonsoft.Json`セキュリティの脆弱性があるライブラリの場合、開発者はその脆弱性に対応した最新バージョンにアップデートする必要があります。

## スタティックコードアナライザーを利用する

静的コード解析ツールは、コードが実行される前に、コードの潜在的なセキュリティ脆弱性を特定することができるツールである。Visual StudioのCodeのようなツールを使用します。`Analysis``ReSharper`と`SonarQube`で、コード内のセキュリティ問題を検出し、デプロイ前に修正することができます。

例えば、Visual Studioのコード解析は、C#のコードに潜在的なセキュリティの脆弱性がないか調べる、人気の静的コード解析ツールです。SQLインジェクション、クロスサイトスクリプティング、安全でない関数の使用などの問題を検出することができます。

## ウェブアプリケーションに安全なコーディングの習慣を用いる

Webアプリケーションは、クロスサイトスクリプティング、SQLインジェクション、コマンドインジェクションなど、いくつかのセキュリティリスクに対して脆弱である。開発者は、入力検証、出力エンコーディング、パラメータ化されたクエリなどのセキュアコーディングプラクティスに従って、Webアプリケーションの安全性を確保する必要があります。

例えば、SQLクエリを記述する場合、ユーザー入力をクエリに連結するのではなく、パラメタライズドクエリを使用します。パラメータ化されたクエリは、ユーザー入力を実行可能なコードではなく、データとして扱うことで、SQLインジェクション攻撃を防ぐことができます。

```csharp
string query = "SELECT * FROM Users WHERE Username = @Username";
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using (SqlCommand command = new SqlCommand(query, connection))
    {
        command.Parameters.AddWithValue("@Username", username);
        connection.Open();
        SqlDataReader reader = command.ExecuteReader();
        // process the data
    }
}
```

また、開発者は、すべてのユーザー入力を検証し、出力を暗号化し、HTTPSを使用してネットワーク上で送信されるデータを暗号化する必要があります。

_____

## C# フレームワークのセキュアコーディング基準

ASP.NETや.NET CoreなどのC#フレームワークには、それぞれセキュアコーディング標準があります。これらのフレームワークを使用してアプリケーションを開発する場合、開発者はこれらの標準に従う必要があります。

### ASP.NET
ASP.NETは、C#用の一般的なWebフレームワークです。ここでは、ASP.NET のセキュアコーディング標準をいくつか紹介します：

- カスタム認証システムを作成する代わりに、ASP.NETの組み込み認証システムを使用します。たとえば、ASP.NETの`Identity`システムを使用して、ユーザー認証と認可を管理します。
- カスタムパスワードのハッシュメソッドを作成する代わりに、ASP.NETの組み込みパスワードハッシュ関数を使用します。たとえば、ASP.NETの`PasswordHasher`クラスを使用して、パスワードを安全にハッシュ化し、検証します。
- ASP.NETの組み込みの`AntiForgeryToken`を使用して、クロスサイトリクエストフォージェリ（CSRF）攻撃を防止することができます。例えば`ValidateAntiForgeryToken`属性を使用して、POST リクエストのアンチフォージェリ・トークンを検証します。
- ASP.NETの組み込みの`OutputCacheAttribute`を使用して、機密データのキャッシュを防止することができます。例えば`OutputCacheAttribute`を使用して、Webページのキャッシュポリシーを設定し、機密データがキャッシュされないようにします。

### .NET Core
.NET Core は、最新のクラウドベースアプリケーションを構築するためのクロスプラットフォーム、オープンソースのフレームワークです。ここでは、.NET Coreの安全なコーディング標準を紹介します：

- カスタム認証システムを作成する代わりに、.NET Coreの組み込み認証システムを使用します。たとえば、.NET Coreの`Identity`システムを使用して、ユーザー認証と認可を管理します。
- カスタムパスワードのハッシュメソッドを作成する代わりに、.NET Coreの組み込みパスワードハッシュ関数を使用します。たとえば、.NET Coreの`PasswordHasher`クラスを使用して、パスワードを安全にハッシュ化し、検証します。
- .NET Coreの組み込みデータ保護APIを使用して、接続文字列や秘密などの機密データを保護します。たとえば`DataProtectionProvider`クラスを使用して、機密データをキーで保護します。
- .NET Coreの組み込みヘルスチェックを使用して、アプリケーションの健全性を監視します。たとえば`HealthCheck`ミドルウェアで、アプリケーションの健全性を定期的にチェックし、問題があれば警告を発します。


## まとめ
セキュアコーディング標準は、コードが安全で信頼性が高く、脆弱性がないことを保証するために不可欠です。C#は人気のあるプログラミング言語で、セキュリティリスクを防ぐために、開発者はセキュアコーディング標準に従うことを要求されます。入力検証、安全でない関数の回避、暗号化ライブラリの使用、ライブラリやフレームワークの更新などのベストプラクティスに従うことで、開発者はコードが安全で脆弱性がないことを保証することができます。C#のフレームワークを使用する場合、開発者はフレームワークが推奨するセキュアコーディング標準に従う必要があります。

セキュアコーディング標準の採用は継続的なプロセスであり、開発者は最新のセキュリティベストプラクティスとツールを常に更新する必要があります。開発プロセスにセキュアコーディング標準を取り入れることで、開発者はセキュリティ侵害のリスクを最小化し、機密データを保護することができます。

C#でセキュアコーディングを始めるには、まず、この記事で取り上げたベストプラクティスに慣れることから始めましょう。コードの中で、入力検証、パスワードハッシュ、セッション管理など、セキュリティリスクの影響を受けやすい部分を特定する必要があります。そして、この記事で取り上げたようなベストプラクティスを実施することで、コードの安全性を確保することができます。

また、開発者は、セキュリティに関するブログを読んだり、カンファレンスに参加したり、オンラインコミュニティーに参加したりして、最新のセキュリティトレンドやプラクティスを常に把握する必要があります。常に最新の情報を得ることで、コードを脆弱性から守り、安全な状態に保つことができます。

最後に、開発者は、チームや同僚とベストプラクティスを共有することによって、セキュリティに対する意識の文化を促進する必要があります。開発者は、セキュリティに関するトレーニングセッションを開催し、安全なコーディングの実践に関する記事やリソースを共有し、自分たちのコードにこれらのベストプラクティスを実装して、模範を示すべきです。セキュリティ意識の文化を促進することで、チームのコードが安全で脆弱性のないものであることを保証することができます。

これらのベストプラクティスに従うことで、開発者は自分のC#コードの安全性と信頼性を確保することができ、セキュリティ侵害を防ぎ、機密データを保護することができるようになります。

## 参考文献

C#におけるセキュアコーディングの実践について、より詳しく知ることができる有用なリソースを紹介します：

-[Microsoft's Secure Coding Guidelines for C# and .NET](https://learn.microsoft.com/en-us/dotnet/standard/security/secure-coding-guidelines)
-[OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
-[NIST's Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf)
-[CIS Microsoft .NET Framework 4.5 Benchmark](https://www.cisecurity.org/benchmark/microsoft_net_framework_4-5_benchmark/)
-[Security Code Scan - .NET Security Guard](https://security-code-scan.github.io/#NET-Security-Guard)

これらのリソースに従うことで、開発者はC#におけるセキュアコーディングプラクティスと、それをプロジェクトに実装する方法について、より深く学ぶことができます。
