---
title: "Pythonの安全なコーディング"
date: 2023-09-26
lastmod: 2026-11-13
toc: true
draft: false
description: "危険な関数を避け、堅牢で信頼できるアプリケーションを作るための実践方法を学び、安全なPythonコードを書きましょう。"
genre: ["プログラミング", "サイバーセキュリティ", "ソフトウェア開発", "Python", "コーディング", "ウェブ開発", "セキュアコーディング", "テクノロジー", "コンピューターサイエンス", "データセキュリティ"]
tags: ["Pythonプログラミング", "安全なコーディング", "安全なPython関数", "コードセキュリティ", "Pythonの代替手段", "プログラミングのベストプラクティス", "サイバーセキュリティ", "コーディングのヒント", "ソフトウェア開発", "ウェブ開発", "危険なPython関数を避ける", "安全なPythonアプリケーション", "コードのセキュリティ対策", "安全なコードの実践", "プログラミングセキュリティのヒント"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "開発者がコードブロックの壁を安全に築く漫画風イラスト。安全なPythonプログラミングの実践を表しています。"
coverCaption: "安全に築き、自信を持ってコードを書く。"
---

## **危険なPython関数と代替手段**

Pythonは多くのタスクに使える、汎用性の高い人気言語です。ただし、すべての関数が同じように安全とは限らず、慎重に扱わないと脆弱性や予期しない結果を招くものがあります。ここでは**危険なPython関数**のリスクと、同様の機能を持つより安全な代替手段を紹介し、**安全性**と**安定性**を高めます。

### **はじめに: Pythonプロジェクトを守る**

Pythonは豊富なライブラリと分かりやすい構文で広く使われています。一部の関数を誤って使うと、安全性と信頼性が損なわれます。潜在的な問題を理解し、別の方法を選ぶことで、脅威に強いコードを書けます。

___________

## **危険なPython関数とそのリスク**

### `eval()` による動的コード実行

`eval()` は文字列からPythonコードを動的に実行します。強力ですが、ユーザー入力を適切に検証しないと**コードインジェクション攻撃**につながります。制御された安全な実行には **`ast.literal_eval()`** または **`exec()`** を検討してください。

#### eval() による動的コード実行:
```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### `ast.literal_eval()` を使うより安全な方法:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### 未検証データを使った文字列連結

未検証の入力を文字列と連結すると、**SQLインジェクション**や**クロスサイトスクリプティング（XSS）**の脆弱性につながることがあります。**f-string** または **`str.format()`** と**入力検証**を併用してください。

#### 危険な文字列連結:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-string（書式付き文字列リテラル）の使用:
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### オブジェクトのシリアライズに使う **Pickle**

`pickle` モジュールはPythonオブジェクトをシリアライズ、逆シリアライズしますが、**不正なデータや悪意を持って作られたデータに対して安全ではありません**。より安全な方法として **`json`** や **`marshal`** などを選びます。

#### pickleの危険な使用:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### jsonを使うより安全な方法:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### `mark_safe()` によるHTMLエスケープ不足

Djangoの **`mark_safe()`** は文字列を安全なHTMLとして扱うため、アプリケーションが**XSS攻撃**にさらされるおそれがあります。テンプレートのエスケープと **`safe`** フィルターを使い、HTMLを安全に表示してください。

#### Djangoテンプレートでのmark_safe()の危険な使用:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### テンプレートエスケープを使うより安全な方法:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### システムコマンドに **`os.system()`** を使う

`os.system()` はシステムコマンドを実行しますが、**コマンドインジェクション攻撃**に弱い関数です。より安全な実行と出力処理には **`subprocess`** を使います。

#### os.system()の危険な使用:
```python
command = input("Enter a command: ")
os.system(command)
```

#### subprocessを使うより安全な方法:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### `hash()` による不十分なパスワードハッシュ化

`hash()` は処理が速く、**総当たり攻撃**に弱いため、パスワードの安全なハッシュ化には適しません。**`bcrypt`** や **`Argon2`** などの堅牢なライブラリを使います。

#### hash()による危険なパスワードハッシュ化:
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### bcryptを使うより安全な方法:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **より安全な代替手段とベストプラクティス**

### **`urllib`** の代わりに **`requests`** を使う

HTTPリクエストには、古くなった `urllib` より **`requests`** を推奨します。リクエストの送信や応答の処理に、使いやすく安全なインターフェースを提供します。

#### requestsによるHTTPリクエスト:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed.")
```

### **`with`** 文でファイルを安全に扱う

ファイルを扱うときは **`with`** 文を使い、リソース漏れを防いで適切に管理します。自動的にファイルを閉じるため、エラーや脆弱性のリスクを減らします。

#### with文によるファイル処理:
```python
filename = "example.txt"

# Unsafe: Without using `with`
file = open(filename, "r")
content = file.read()
file.close()

# Safer: Using `with` statement
with open(filename, "r") as file:
    content = file.read()
```

### **`html.escape()`** で入力をサニタイズする

**XSS攻撃**を防ぐため、**`html.escape()`** でユーザー入力をサニタイズします。表示前に有害な可能性があるHTMLをエスケープします。

#### XSS防止のための入力サニタイズ:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### **`sqlite3`** のプレースホルダー付きクエリ

データベースには **`sqlite3`** のパラメーター化クエリを使います。ユーザー入力をクエリ値として渡し、**SQLインジェクション攻撃**を防ぎます。

#### sqlite3のパラメーター化クエリ:
```python
import sqlite3

db_connection = sqlite3.connect("database.db")
cursor = db_connection.cursor()

name = input("Enter a name: ")
age = input("Enter an age: ")

query = "INSERT INTO users (name, age) VALUES (?, ?)"
cursor.execute(query, (name, age))

db_connection.commit()
db_connection.close()
```

### 環境変数を安全に管理する

機密情報をコードに直接記述しないでください。**`os.environ`** 辞書や **`python-decouple`** などのパッケージで環境変数を管理し、設定を保護します。

#### os.environによる環境変数の管理:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### python-decoupleによる環境変数の管理:
```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### **`secrets`** による強い乱数

暗号学的に安全な乱数値には `random` の代わりに **`secrets`** を使います。セキュリティが重要な処理に適しています。

#### secretsによる安全なトークンの生成:
```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```

## まとめ

Pythonの豊富なエコシステムで、多機能なアプリケーションを作れます。一方、一部の関数を不用意に使うと脆弱性が生じ、コードの完全性を損なうおそれがあります。ベストプラクティスを守り、より安全な方法を選ぶことで、信頼性の高いソフトウェアを作成できます。

______

## 参考資料

- Pythonドキュメント: [https://docs.python.org](https://docs.python.org)
- Djangoドキュメント: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASPクロスサイトスクリプティング（XSS）防止チートシート: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP SQLインジェクション防止チートシート: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requestsライブラリ: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3ドキュメント: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python `secrets` モジュール: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decoupleパッケージ: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

