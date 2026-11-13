---
title: "Безопасное программирование на Python"
date: 2023-09-26
lastmod: 2026-11-13
toc: true
draft: false
description: "Узнайте, как писать безопасный код на Python, избегать небезопасных функций и создавать надежные приложения."
genre: ["Программирование", "Кибербезопасность", "Разработка ПО", "Python", "Кодирование", "Веб-разработка", "Безопасное программирование", "Технологии", "Информатика", "Защита данных"]
tags: ["программирование на Python", "безопасное кодирование", "безопасные функции Python", "безопасность кода", "альтернативы Python", "лучшие практики программирования", "кибербезопасность", "советы по программированию", "разработка ПО", "веб-разработка", "как избегать небезопасных функций Python", "безопасные приложения Python", "меры защиты кода", "практики безопасного кода", "советы по безопасности программирования"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Мультяшная иллюстрация разработчика, который безопасно строит стену из блоков кода, символизирующую безопасные практики программирования на Python."
coverCaption: "Создавайте безопасно, программируйте уверенно!"
---

## **Небезопасные функции Python и их альтернативы**

Python представляет собой универсальный и широко используемый язык с функциями для самых разных задач. Некоторые функции при неосторожном применении несут риски и приводят к неожиданным последствиям. В этом разделе рассмотрены **небезопасные функции Python**, связанные с ними угрозы и более безопасные альтернативы с сопоставимыми возможностями, которые помогают укрепить **безопасность** и **стабильность**.

### **Введение: защитите свои проекты на Python**

Python привлекает обширной библиотекой и понятным синтаксисом. Неправильное применение отдельных функций может поставить под угрозу безопасность и надежность. Знание рисков и выбор других методов помогает писать код, лучше устойчивый к угрозам.

___________

## **Небезопасные функции Python и связанные с ними риски**

### Динамическое выполнение кода с `eval()`

`eval()` динамически выполняет код Python из строки. Эта функция мощная, но при недостаточной очистке пользовательского ввода может открыть путь для **атак с внедрением кода**. Рассмотрите **`ast.literal_eval()`** или **`exec()`** для контролируемого и безопасного выполнения.

#### Динамическое выполнение кода с eval():
```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### Более безопасная альтернатива с `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### Объединение строк с неочищенными данными

Объединение строк с неочищенным пользовательским вводом может привести к **SQL-инъекции** или уязвимостям **межсайтового скриптинга (XSS)**. Используйте **f-строки** или **`str.format()`** вместе с **проверкой входных данных**.

#### Небезопасное объединение строк:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-строки (форматированные строковые литералы):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** для сериализации объектов

Модуль `pickle` сериализует и десериализует объекты Python, но **не защищает от ошибочных или вредоносно созданных данных**. Для более безопасной сериализации используйте, например, **`json`** или **`marshal`**.

#### Небезопасное использование pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### Более безопасная альтернатива с json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### Недостаточное экранирование HTML с помощью `mark_safe()`

Функция Django **`mark_safe()`** помечает строку как безопасный HTML и тем самым может подвергнуть приложение **XSS-атакам**. Вместо нее применяйте экранирование шаблонов и фильтр **`safe`** для безопасного вывода HTML.

#### Небезопасное использование mark_safe() в шаблоне Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Более безопасный подход с экранированием шаблона:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Использование **`os.system()`** для системных команд

`os.system()` запускает системные команды, но уязвима для **внедрения команд**. Используйте модуль **`subprocess`** для более безопасного запуска команд и обработки результатов.

#### Небезопасное использование os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Более безопасная альтернатива с subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### Ненадежное хеширование паролей с `hash()`

Из-за высокой скорости и уязвимости к **атакам перебором** `hash()` не подходит для безопасного хеширования паролей. Используйте надежные библиотеки, например **`bcrypt`** или **`Argon2`**.

#### Небезопасное хеширование пароля с hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### Более безопасный подход с bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **Более безопасные альтернативы и лучшие практики**

### Используйте **`requests`** вместо **`urllib`**

Для HTTP-запросов отдавайте предпочтение библиотеке **`requests`**, а не устаревшему `urllib`. Она предоставляет более удобный и безопасный интерфейс для отправки запросов и обработки ответов.

#### HTTP-запросы с библиотекой requests:
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

### Безопасная работа с файлами при помощи **`with`**

При работе с файлами используйте инструкцию **`with`**, чтобы избежать утечек ресурсов и правильно управлять файлами. Она автоматически закрывает файл и снижает риск ошибок и уязвимостей.

#### Работа с файлами при помощи with:
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

### Очистка ввода с помощью **`html.escape()`**

Чтобы предотвратить **XSS-атаки**, очищайте пользовательский ввод с помощью **`html.escape()`**. Эта функция экранирует потенциально опасный HTML перед его отображением.

#### Очистка пользовательского ввода для защиты от XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### Параметризованные запросы с **`sqlite3`**

При работе с базами данных применяйте параметризованные запросы **`sqlite3`**. Передача ввода как значений запроса помогает защититься от **SQL-инъекций**.

#### Параметризованные запросы с sqlite3:
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

### Безопасное управление переменными среды

Не храните конфиденциальные сведения непосредственно в коде. Используйте переменные среды через словарь **`os.environ`** или пакет **`python-decouple`** для более безопасного управления конфигурацией.

#### Управление переменными среды через os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### Управление переменными среды через python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### Надежная случайность с **`secrets`**

Для криптографически стойких случайных значений используйте модуль **`secrets`** вместо `random`. Он подходит для операций, где важна безопасность.

#### Создание безопасных токенов с secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```

## Заключение

Экосистема Python позволяет создавать мощные и функциональные приложения. Неосторожное использование некоторых функций может привести к уязвимостям и нарушить целостность кода. Соблюдение лучших практик и выбор более безопасных альтернатив помогают создавать надежное программное обеспечение.

______

## Источники

- Документация Python: [https://docs.python.org](https://docs.python.org)
- Документация Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Руководство OWASP по предотвращению XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Руководство OWASP по предотвращению SQL-инъекций: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Библиотека Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Документация SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Модуль Python `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Пакет python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

