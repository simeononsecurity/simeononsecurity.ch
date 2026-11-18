---
title: "Python 安全编码"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "学习如何编写安全的 Python 代码，避免不安全函数，并采用最佳实践构建稳健可靠的应用程序。"
genre: ["编程", "网络安全", "软件开发", "Python", "编码", "Web 开发", "安全编码", "技术", "计算机科学", "数据安全"]
tags: ["Python 编程", "安全编码", "安全的 Python 函数", "代码安全", "Python 替代方案", "编程最佳实践", "网络安全", "编程技巧", "软件开发", "Web 开发", "避免不安全的 Python 函数", "安全的 Python 应用", "代码安全措施", "安全代码实践", "编程安全技巧"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "卡通风格插图中，一名开发者正在安全地搭建代码块墙，代表安全的 Python 编程实践。"
coverCaption: "安全构建，自信编码！"
---

## **不安全的 Python 函数及其替代方案**

Python 是一种用途广泛、应用普遍的编程语言，提供了许多实用函数。但并非所有函数都同样安全。部分函数使用不当会带来漏洞和意外后果。本节介绍这些**不安全的 Python 函数**、相关风险，以及功能相近的更安全替代方案，帮助加强**安全性**和**稳定性**。

### **引言：保护你的 Python 项目**

Python 凭借丰富的库和直观语法广受欢迎。但一些函数处理不当会损害安全性和可靠性。了解潜在问题并采用其他方法，有助于编写更能抵御威胁的代码。

___________

## **不安全的 Python 函数及其风险**

### 使用 `eval()` 动态执行代码

`eval()` 会动态执行字符串中的 Python 代码。它功能强大，但如果没有妥善清理用户输入，就可能引发**代码注入攻击**。可以考虑使用 **`ast.literal_eval()`** 或 **`exec()`** 实现受控、安全的代码执行。

#### 使用 eval() 动态执行代码：
```python
# 不安全：使用 eval() 执行动态代码
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("结果：", result)
```

#### 使用 `ast.literal_eval()` 的更安全替代方案：
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("解析后的值：", parsed_value)
except (ValueError, SyntaxError):
    print("输入无效。")
```

### 拼接未经清理的数据

将未经清理的用户输入拼接到字符串中，可能导致 **SQL 注入**或**跨站脚本攻击（XSS）**。结合**输入验证**使用 **f-string** 或 **`str.format()`**，以降低这些风险。

#### 不安全的字符串拼接：
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### 使用 f-string（格式化字符串字面量）：
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### 使用 **Pickle** 序列化对象

`pickle` 模块能序列化和反序列化 Python 对象，但**无法安全处理错误或恶意构造的数据**。如需更安全地序列化数据，可选用 **`json`** 或 **`marshal`** 等库。

#### 不安全地使用 pickle：
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# 存储或发送 serialized_data
```

#### 使用 json 的更安全替代方案：
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# 存储或发送 serialized_data
```

### 使用 `mark_safe()` 时 HTML 转义不足

Django 的 **`mark_safe()`** 会将字符串标记为安全 HTML，可能使应用遭受 **XSS 攻击**。应改用模板转义和 **`safe`** 过滤器，以安全呈现 HTML 内容。

#### 在 Django 模板中不安全地使用 mark_safe()：
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### 使用模板转义的更安全方法：
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### 使用 **`os.system()`** 执行系统命令

`os.system()` 可执行系统命令，但容易受到**命令注入攻击**。使用 **`subprocess`** 模块以更安全地执行命令并处理输出。

#### 不安全地使用 os.system()：
```python
command = input("Enter a command: ")
os.system(command)
```

#### 使用 subprocess 的更安全替代方案：
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("输出：", result.stdout)
```

### 使用 `hash()` 进行不充分的密码哈希

`hash()` 速度快，且容易受到**暴力破解攻击**，因此不适合安全地哈希密码。应使用 **`bcrypt`** 或 **`Argon2`** 等可靠的密码哈希库。

#### 使用 hash() 不安全地哈希密码：
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# 将 hashed_password 存入数据库
```

#### 使用 bcrypt 的更安全方法：
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# 将 hashed_password 存入数据库
```

## **更安全的替代方案和最佳实践**

### 使用 **`requests`** 代替 **`urllib`**

发送 HTTP 请求时，优先使用 **`requests`**，而不是已过时的 `urllib`。`requests` 提供了更易用、更安全的请求发送与响应处理接口。

#### 使用 requests 库发送 HTTP 请求：
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("请求失败。")
```

### 使用 **`with`** 语句安全处理文件

操作文件时使用 **`with`** 语句，避免资源泄漏并妥善管理文件。它会自动关闭文件，降低出错和产生漏洞的风险。

#### 使用 with 处理文件：
```python
filename = "example.txt"

# 不安全：不使用 with
file = open(filename, "r")
content = file.read()
file.close()

# 更安全：使用 with 语句
with open(filename, "r") as file:
    content = file.read()
```

### 使用 **`html.escape()`** 清理输入

为了防止 **XSS 攻击**，使用 **`html.escape()`** 清理用户输入。它会在呈现之前转义可能有害的 HTML 内容。

#### 清理用户输入以防止 XSS：
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("已清理的输入：", sanitized_input)
```

### 使用 **`sqlite3`** 参数化查询

操作数据库时，使用 **`sqlite3`** 参数化查询。将用户输入作为查询参数传递，有助于防止 **SQL 注入攻击**。

#### 使用 sqlite3 参数化查询：
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

### 安全管理环境变量

不要在代码中直接暴露敏感信息。使用 **`os.environ`** 字典或 **`python-decouple`** 等包管理环境变量和配置。

#### 使用 os.environ 管理环境变量：
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API 密钥：", api_key)
else:
    print("未设置 API 密钥。")
```

#### 使用 python-decouple 管理环境变量：
```python
from decouple import config

api_key = config("API_KEY")
print("API 密钥：", api_key)
```

### 使用 **`secrets`** 获取强随机值

生成密码学安全的随机值时，使用 **`secrets`** 而不是 `random`。它适用于对安全性敏感的操作。

#### 使用 secrets 生成安全令牌：
```python
import secrets

token = secrets.token_hex(16)
print("安全令牌：", token)
```

## 结论

Python 丰富的生态系统有助于开发功能强大的应用程序。但不谨慎地使用某些函数会引入漏洞并损害代码完整性。遵循最佳实践并选择更安全的替代方案，可以构建更安全可靠的软件。

______

## 参考资料

- Python 文档：[https://docs.python.org](https://docs.python.org)
- Django 文档：[https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP 跨站脚本（XSS）防护指南：[https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP SQL 注入防护指南：[https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests 库：[https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3 文档：[https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python `secrets` 模块：[https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decouple 包：[https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

