---
title: "Pythonのためのセキュアコーディングスタンダード：ベストプラクティス"
date: 2023-02-26
toc: true
draft: false
description: "セキュリティ侵害のリスクを最小限に抑え、機密データを保護するために、Pythonでセキュアコーディングするためのベストプラクティスを学びます。"
tags: ["パイソン", "セキュアコーディング", "セキュリティリスク", "入力バリデーション", "暗号化ライブラリ", "最小限の特権", "スタティックコードアナライザー", "ウェブアプリケーション", "Pythonフレームワーク", "ジャンゴ", "フラッシュ", "認証システム", "パスワードハッシュ化", "テンプレートシステム", "セッション管理", "マークアップセーフ", "WTForms（ワフフォームズ", "ブリンカー", "データ保護", "脆弱性（ぜいじゃくせい"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "セキュアなコーディング基準を表す、Pythonと書かれた漫画の盾"
coverCaption: ""
---
Python**におけるセキュアコーディングスタンダードのためのプラクティス

### 1.入力の妥当性確認

### 入力の妥当性確認

ユーザー入力は、しばしばセキュリティリスクの重要な原因となっています。**入力の検証**とは、ユーザー入力が期待される基準を満たし、アプリケーションで使用しても安全であることを検証するプロセスです。

例えば、ユーザーがクレジットカードの番号を入力する場合、その入力は数字のみで、特殊文字は含まれてはいけません。入力の検証を行うために、開発者は以下のような組み込み関数を使用することができます。`isdigit()`や正規表現を使って、入力が期待される条件を満たしていることを確認します。

```python
import re

def validate_input(input_string):
    """
    Function to validate input using regular expressions.
    """
    pattern = r"^[0-9]+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False
```

### 2.安全でない関数を使用しないようにする

Python には、注意深く使用しないとセキュリティ上の問題が発生する可能性がある関数がいくつかあります。以下のような関数があります。`exec()``eval()`と`pickle`は、攻撃者に悪意のあるコードを実行させる可能性があります。開発者は、これらの関数の使用を避ける**か、入力パラメータを制限し、必要な場合にのみ使用するなどして、慎重に使用する必要があります。

例えば`eval()`関数を使って文字列を整数に変換する場合、開発者はこの関数を使用する必要があります。`int()`関数を使用します。
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```

### 3.暗号ライブラリの利用

**以下のような暗号化ライブラリ**を使用します。[`cryptography`](https://pypi.org/project/cryptography/) and [`pycryptodome`](https://pypi.org/project/pycryptodome/)は、暗号化および復号化処理を安全に実行するための方法を提供します。これらのライブラリは、脆弱性がある可能性のあるカスタム暗号化メソッドを作成する代わりに使用してください。

例えば、パスワードを暗号化する場合は、以下のライブラリを使用します。[`cryptography`](https://pypi.org/project/cryptography/)を以下のようにライブラリ化しました：
```py
from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Function to encrypt password using cryptography library.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password

password = "mypassword"
encrypted_password = encrypt_password(password)
```
のことです。`Fernet`オブジェクトはキーを生成し、そのキーを使ってパスワードを暗号化します。`encrypt()`メソッドを使用します。

### 4.最小特権の原則に従う

**最小特権の原則**とは、セキュリティのベストプラクティスで、ユーザーやプロセスを、その機能を実行するために必要な最小レベルのアクセスに制限することです。開発者は、セキュリティ侵害の影響を最小限にするために、コードを書くときにこの原則に従うべきです。

例えば、あるアプリケーションがデータベースへの読み取り専用アクセスを必要とする場合、完全な権限を持つアカウントではなく、読み取り専用権限を持つデータベースアカウントを使用する必要があります。これにより、攻撃者がアプリケーションを悪用してデータを変更したり削除したりするリスクを減らすことができます。

### 5.ライブラリやフレームワークを常に更新する

ライブラリやフレームワークには、攻撃者に悪用される可能性のあるセキュリティ脆弱性が含まれていることがあります。開発者は、潜在的なセキュリティ問題を回避するために、**ライブラリやフレームワークを最新バージョンに更新**しておく必要があります。

例えば、アプリケーションがサードパーティのライブラリを使用している場合、次のようになります。[`Requests`](https://pypi.org/project/requests/)セキュリティの脆弱性があるライブラリの場合、開発者はその脆弱性に対応した最新バージョンにアップデートする必要があります。

### 6.スタティックコードアナライザーを使用する

**静的コード解析ツール**は、コードが実行される前に、コードの潜在的なセキュリティ脆弱性を特定することができるツールです。などのツールを使用します。[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/)で、コード内のセキュリティ問題を検出し、デプロイ前に修正することができます。

例えば、以下のようなものです、[`bandit`](https://pypi.org/project/bandit/)は、Pythonのコードに潜在的なセキュリティ脆弱性がないか調べる、人気の静的コードアナライザです。ハードコードされたパスワード、SQLインジェクション、安全でない関数の使用などの問題を検出することができます。

### 7.ウェブアプリケーションに安全なコーディングの実践を用いる

ウェブアプリケーションは、クロスサイトスクリプティング、SQLインジェクション、コマンドインジェクションなど、いくつかのセキュリティリスクに対して脆弱である。開発者は、Web アプリケーションの安全性を確保するために、入力検証、出力エンコード、パラメータ化されたクエリなど、**セキュアコーディングプラクティス**に従わなければなりません。

例えば、SQLクエリを書くときは、ユーザー入力をクエリに連結するのではなく、**パラメータ化されたクエリ**を使用します。パラメータ化されたクエリは、ユーザー入力を実行可能なコードではなく、データとして扱うことで、SQLインジェクション攻撃を防ぎます。

```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
また、開発者は、すべてのユーザー入力を検証し**、出力を暗号化し、ネットワーク上で送信されるデータを暗号化するために HTTPS を使用する必要があります。

## Python フレームワークの安全なコーディング基準

以下のようなPythonフレームワークがあります。[Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/)には、セキュアコーディングの基準があります。開発者は、これらのフレームワークを使用したアプリケーションを開発する際に、これらの標準に従うべきです。ここでは、Pythonフレームワークのセキュアコーディング標準をいくつか紹介します：

### 1.[Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a popular web framework for Python. Here are some secure coding standards for [Django](https://www.djangoproject.com/)

- 使用する[Django](https://www.djangoproject.com/)カスタム認証システムを作成する代わりに、組み込みの**認証システム**を使用します。
- 使用する[Django](https://www.djangoproject.com/)パスワードハッシュのカスタムメソッドを作成する代わりに、組み込みの **パスワードハッシュ関数** を使用します。
- 使用する[Django](https://www.djangoproject.com/)**template system** は、クロスサイトスクリプティングの脆弱性を排除した安全な出力を保証するものです。

例えば、以下のように使用します。[Django](https://www.djangoproject.com/)'s built-in password hashing function, use the `make_password()` function from the `モジュールになります。

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```

### 2.[Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) is a micro web framework for Python. Here are some secure coding standards for [Flask](https://flask.palletsprojects.com/)

- 使用する[Flask](https://flask.palletsprojects.com/)を内蔵し、安全なセッションの取り扱いを保証します。
- 使用する[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/)ライブラリを使用することで、クロスサイトスクリプティングの脆弱性を排除した安全な出力が可能です。
- 使用方法[Flask](https://flask.palletsprojects.com/)'s [`WTForms`](https://pypi.org/project/WTForms/)ライブラリを使用して、ユーザーの入力検証を処理し、入力がセキュリティリスクから解放されることを保証します。
- 使用する[Flask](https://flask.palletsprojects.com/)'s [`Blinker`](https://pypi.org/project/blinker/)ライブラリで、安全な信号処理を行うことができます。

例えば[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/)ライブラリをインポートして、出力からHTMLタグをエスケープするために使用します。
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```
______

## 知識の活用と今やるべきことは？

1.セキュリティ侵害のリスクを最小化し、機密データを保護するために、**今日からあなたのPythonコードにこれらのベストプラクティスを実装してください**。まず、入力検証、パスワードハッシュ、セッション管理など、セキュリティリスクの影響を受けやすい部分を特定することから始めましょう。そして、この記事で取り上げたようなベストプラクティスを実装して、コードの安全性を確保することができます。例えば、Pythonに内蔵されている正規表現を使ってユーザーの入力を検証したり、以下のような安全なパスワードハッシュライブラリを使用することができます。[`bcrypt`](https://pypi.org/project/bcrypt/)

2.**既存のコードベースに潜在的なセキュリティ脆弱性がないかどうかを確認し、以下のような静的コードアナライザーを使用します。[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/)を使用して、問題を検出して修正します。また、静的コードアナライザーが検出できないようなセキュリティ問題を特定するために、手動コードレビューを使用することもできます。SQLインジェクション、クロスサイトスクリプティング、入力検証の問題など、一般的な脆弱性を探します。潜在的なセキュリティの脆弱性を特定したら、ベストプラクティスを使用して問題を修正することができます。

3.**最新のセキュリティベストプラクティスとツール**を入手し、あなたのコードが脆弱性から解放され、安全であることを確認することができます。セキュリティに関するブログをフォローしたり、カンファレンスに参加したり、オンラインコミュニティに参加したりして、最新のセキュリティトレンドやプラクティスを身につけましょう。ライブラリやフレームワークを常に最新の状態に保ち、最新の安全なバージョンを使用するようにする。

4.**Pythonの安全なコーディングの実践について、専門家や他の開発者から学ぶことができます。他の開発者とセキュリティの問題について議論したり、新しいセキュリティの傾向を学んだり、自分の知識を共有したりできるオンラインコミュニティやフォーラムを探しましょう。カンファレンス、ウェビナー、ミートアップなどのイベントに参加し、セキュリティの専門家や他の開発者から学ぶ。

5.5. **これらのベストプラクティスをあなたのチームや同僚と共有しましょう** セキュリティを意識する文化を促進し、他の人がPythonプロジェクトで安全なコーディング手法を採用することを奨励します。セキュリティトレーニングセッションを開催し、セキュアコーディングプラクティスに関する記事やリソースを共有し、自分のコードにこれらのベストプラクティスを実装することで模範となる。セキュリティ意識の文化を促進することで、チームのコードが安全で脆弱性のないものであることを保証することができます。


## 結論

セキュアコーディング標準は、コードが安全で信頼性が高く、脆弱性のないものであることを保証するために不可欠です。Pythonは人気のあるプログラミング言語で、セキュリティリスクを防ぐために、開発者はセキュアコーディング標準に従うことを要求されます。入力検証、安全でない関数の回避、暗号化ライブラリの使用、ライブラリやフレームワークの更新などのベストプラクティスに従うことで、開発者はコードが安全で脆弱性がないことを保証することができます。Pythonフレームワークを使用する場合、開発者はフレームワークが推奨するセキュアコーディング標準に従う必要があります。

セキュアコーディング標準の採用は継続的なプロセスであり、開発者は最新のセキュリティベストプラクティスとツールを常にアップデートしておく必要があります。セキュアコーディングスタンダードを開発プロセスに組み込むことで、開発者はセキュリティ侵害のリスクを最小化し、機密データを保護することができます。

