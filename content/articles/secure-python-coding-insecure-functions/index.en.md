---
title: "Secure Python Coding: Avoiding Unsafe Functions for Robust Applications"
date: 2023-09-26
toc: true
draft: false
description: "Learn how to write secure Python code by avoiding unsafe functions and adopting best practices for robust and reliable applications."
genre: ["Programming", "Cybersecurity", "Software Development", "Python", "Coding", "Web Development", "Secure Coding", "Technology", "Computer Science", "Data Security"]
tags: ["Python programming", "secure coding", "safe Python functions", "code security", "Python alternatives", "programming best practices", "cybersecurity", "coding tips", "software development", "web development", "avoiding unsafe Python functions", "secure Python applications", "coding security measures", "secure code practices", "programming security tips"]
cover: "/img/cover/secure-python-coding-wall.png"
coverAlt: "A cartoon-style illustration of a developer securely building a wall of code blocks, representing safe Python programming practices."
coverCaption: "Build Securely, Code Confidently!"
---

## **Unsafe Python Functions and Their Alternatives**

Python, a versatile and widely adopted programming language, grants developers a toolbox brimming with functions to tackle an array of tasks. Yet, the equal footing of all functions is a misconception; a subset of these functions harbors security vulnerabilities and a propensity for unintended repercussions if wielded imprudently. This segment of the article casts a spotlight on these **unsafe Python functions** that warrant a discerning eye. We'll journey through concrete examples, highlighting the associated risks, and then chart a course towards secure alternatives that ensure functionality parity, all while fortifying the bedrock of **security** and **stability**.

### **Introduction: Safeguarding Your Python Odyssey**

In the sprawling landscape of programming languages, Python's allure stems from its expansive library and intuitive syntax. However, beneath this veil of simplicity lie certain functions that, if mishandled, can unravel the very fabric of security and reliability that developers strive to weave. Our voyage into this realm is not one of alarm but of enlightenment. By acclimating ourselves to these potential pitfalls and embracing alternative methodologies, we empower ourselves to construct code that stands resolute against adversity.

___________


## **Unsafe Python Functions and Their Risks**

### Using `eval()` for Dynamic Code Execution

The `eval()` function allows dynamic execution of Python code from a string. While powerful, it can lead to **code injection attacks** if user inputs are not properly sanitized. Instead of using `eval()`, consider using **`ast.literal_eval()`** or **`exec()`** for controlled and secure code execution.

#### Using eval() for Dynamic Code Execution:

```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### Safer alternative using `ast.literal_eval()`:

```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### String Concatenation with Unsanitized Data

Concatenating strings with unsanitized user inputs can result in **SQL injection** or **cross-site scripting (XSS)** vulnerabilities. Utilize **f-strings** or the **`str.format()`** method along with **input validation** to prevent these security issues.

#### Unsafe string concatenation:

```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```
#### Using f-strings (formatted string literals):

```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** for Object Serialization

The `pickle` module can serialize and deserialize Python objects, but it's **not secure against erroneous or maliciously constructed data**. To safely serialize data, opt for libraries like **`json`** or **`marshal`** that adhere to safer serialization practices.

#### Using pickle (unsafe):
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### Safer alternative using json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### Insufficiently Escaped HTML with `mark_safe()`

The **`mark_safe()`** function in Django allows developers to mark a string as safe HTML, potentially exposing applications to **cross-site scripting (XSS) attacks**. Instead, utilize template escaping and the **`safe`** filter to ensure secure rendering of HTML content.

#### Unsafe use of mark_safe() in Django template:

```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Safer approach with template escaping:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Using **`os.system()`** for System Commands

The `os.system()` function can execute system commands, but it's prone to **command injection attacks**. Employ the **`subprocess`** module for a more secure way to execute system commands and handle their outputs.

#### Unsafe use of os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Safer alternative using subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### Inadequate Password Hashing with `hash()`

The `hash()` function is not suitable for securely hashing passwords due to its speed and vulnerability to **brute force attacks**. Implement robust password hashing using libraries like **`bcrypt`** or **`Argon2`** to enhance password security.

#### Unsafe password hashing with hash():

```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### Safer approach using bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **Safer Alternatives and Best Practices**

### Utilizing **`requests`** Instead of `urllib`

When making HTTP requests, favor the **`requests`** library over the outdated `urllib`. `requests` provides a more user-friendly and secure interface for sending HTTP requests and handling responses.

#### Using requests library for HTTP requests:

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

### Secure File Handling with **`with`** Statement

To avoid resource leaks and ensure proper file handling, use the **`with`** statement when working with files. It automatically handles file closure, reducing the risk of errors and vulnerabilities.

#### Using with statement for file handling:

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

### Sanitizing Inputs with **`html.escape()`**

To prevent **XSS attacks**, sanitize user inputs using the **`html.escape()`** function. This ensures that any potentially harmful HTML content is properly escaped before rendering.

#### Sanitizing user input to prevent XSS attacks:

```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### Parameterized Queries with **`sqlite3`**

When interacting with databases, employ parameterized queries with the **`sqlite3`** library. This guards against **SQL injection attacks** by automatically escaping user inputs within queries.

#### Using parameterized queries with sqlite3:

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

### Securely Managing Environment Variables

Instead of exposing sensitive information directly in code, use environment variables with the **`os.environ`** dictionary or a package like **`python-decouple`** for better security and configuration management.

#### Using os.environ for managing environment variables:

```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### Using python-decouple for managing environment variables:

```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### Strong Randomness with **`secrets`**

For generating cryptographically secure random values, rely on the **`secrets`** module instead of the `random` module. This ensures a higher level of randomness and is suitable for security-sensitive operations.

#### Generating secure random tokens with secrets:

```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```



## Conclusion

Python's vast ecosystem empowers developers to create powerful and feature-rich applications. However, using certain functions recklessly can introduce security vulnerabilities and compromise the integrity of your code. By following best practices and opting for safer alternatives, developers can build more secure and reliable software.

______

## References

- Python Documentation: [https://docs.python.org](https://docs.python.org)
- Django Documentation: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP Cross-Site Scripting (XSS) Prevention Cheat Sheet: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP SQL Injection Prevention Cheat Sheet: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests Library: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3 Documentation: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python `secrets` Module: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decouple Package: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)
