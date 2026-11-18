---
title: "Programação segura em Python"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Aprenda a escrever código Python seguro, evitar funções inseguras e adotar boas práticas para criar aplicações robustas e confiáveis."
genre: ["Programação", "Cibersegurança", "Desenvolvimento de software", "Python", "Codificação", "Desenvolvimento web", "Codificação segura", "Tecnologia", "Ciência da computação", "Segurança de dados"]
tags: ["programação Python", "codificação segura", "funções seguras do Python", "segurança do código", "alternativas Python", "boas práticas de programação", "cibersegurança", "dicas de programação", "desenvolvimento de software", "desenvolvimento web", "evitar funções inseguras do Python", "aplicações Python seguras", "medidas de segurança do código", "práticas de código seguro", "dicas de segurança na programação"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Ilustração em estilo cartoon de uma pessoa desenvolvedora construindo com segurança um muro de blocos de código, símbolo das práticas seguras de programação em Python."
coverCaption: "Construa com segurança, programe com confiança!"
---

## **Funções inseguras do Python e alternativas**

Python é uma linguagem versátil e amplamente usada, com recursos para muitas tarefas. Algumas funções, porém, trazem riscos e efeitos inesperados quando usadas sem cuidado. Esta seção apresenta **funções inseguras do Python**, seus riscos e alternativas mais seguras com finalidade semelhante para fortalecer a **segurança** e a **estabilidade**.

### **Introdução: proteja seus projetos em Python**

Python é popular por sua biblioteca extensa e sintaxe intuitiva. O uso incorreto de certas funções pode comprometer a segurança e a confiabilidade. Conhecer os riscos e escolher outros métodos ajuda a criar código mais resistente.

___________

## **Funções inseguras do Python e seus riscos**

### Execução dinâmica de código com `eval()`

`eval()` executa dinamicamente código Python a partir de uma string. Apesar de poderosa, pode permitir **ataques de injeção de código** se entradas do usuário não forem sanitizadas corretamente. Considere **`ast.literal_eval()`** ou **`exec()`** para execução controlada e segura.

#### Execução dinâmica com eval():
```python
# Inseguro: usar eval() para executar código dinâmico
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Resultado:", result)
```

#### Alternativa mais segura com `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Valor analisado:", parsed_value)
except (ValueError, SyntaxError):
    print("Entrada inválida.")
```

### Concatenação de strings com dados não sanitizados

Concatenar strings com entradas não sanitizadas pode causar **injeção de SQL** ou vulnerabilidades de **script entre sites (XSS)**. Use **f-strings** ou **`str.format()`** junto com **validação de entrada**.

#### Concatenação insegura de strings:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Uso de f-strings (literais de string formatadas):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** para serialização de objetos

O módulo `pickle` serializa e desserializa objetos Python, mas **não é seguro contra dados incorretos ou construídos de forma maliciosa**. Para uma serialização mais segura, escolha bibliotecas como **`json`** ou **`marshal`**.

#### Uso inseguro de pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Armazenar ou enviar serialized_data
```

#### Alternativa mais segura com json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Armazenar ou enviar serialized_data
```

### Escape HTML insuficiente com `mark_safe()`

A função Django **`mark_safe()`** marca uma string como HTML seguro, o que pode expor aplicações a **ataques XSS**. Use o escape de templates e o filtro **`safe`** para renderizar HTML com segurança.

#### Uso inseguro de mark_safe() em um template Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Abordagem mais segura com escape de template:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Uso de **`os.system()`** para comandos do sistema

`os.system()` executa comandos do sistema, mas é vulnerável à **injeção de comandos**. Use o módulo **`subprocess`** para executar comandos com mais segurança e tratar seus resultados.

#### Uso inseguro de os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternativa mais segura com subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Saída:", result.stdout)
```

### Hash de senha inadequado com `hash()`

A velocidade de `hash()` e sua vulnerabilidade a **ataques de força bruta** tornam a função inadequada para proteger senhas. Use bibliotecas robustas como **`bcrypt`** ou **`Argon2`**.

#### Hash inseguro de senha com hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Armazenar hashed_password no banco de dados
```

#### Abordagem mais segura com bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Armazenar hashed_password no banco de dados
```

## **Alternativas mais seguras e boas práticas**

### Use **`requests`** em vez de **`urllib`**

Para solicitações HTTP, prefira **`requests`** ao antigo `urllib`. A biblioteca oferece uma interface mais simples e segura para enviar solicitações e tratar respostas.

#### Solicitações HTTP com requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("A solicitação falhou.")
```

### Manipulação segura de arquivos com **`with`**

Use a instrução **`with`** ao trabalhar com arquivos para evitar vazamentos de recursos e gerenciá-los corretamente. Ela fecha arquivos automaticamente e reduz o risco de erros e vulnerabilidades.

#### Manipulação de arquivos com with:
```python
filename = "example.txt"

# Inseguro: sem usar with
file = open(filename, "r")
content = file.read()
file.close()

# Mais seguro: usar a instrução with
with open(filename, "r") as file:
    content = file.read()
```

### Sanitização de entradas com **`html.escape()`**

Para prevenir **ataques XSS**, sanitize entradas de usuário com **`html.escape()`**. A função escapa HTML potencialmente perigoso antes da renderização.

#### Sanitização de entrada para prevenir XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Entrada sanitizada:", sanitized_input)
```

### Consultas parametrizadas com **`sqlite3`**

Use consultas parametrizadas do **`sqlite3`** ao interagir com bancos de dados. Elas ajudam a prevenir **injeção de SQL** passando entradas como valores da consulta.

#### Consultas parametrizadas com sqlite3:
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

### Gerenciamento seguro de variáveis de ambiente

Não exponha informações confidenciais diretamente no código. Use variáveis de ambiente por meio de **`os.environ`** ou um pacote como **`python-decouple`**.

#### Gerenciamento com os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Chave de API:", api_key)
else:
    print("Chave de API não definida.")
```

#### Gerenciamento com python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("Chave de API:", api_key)
```

### Aleatoriedade forte com **`secrets`**

Use **`secrets`** em vez de `random` para gerar valores aleatórios criptograficamente seguros. O módulo atende a operações sensíveis à segurança.

#### Geração de tokens seguros com secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Token seguro:", token)
```

## Conclusão

O amplo ecossistema Python ajuda a criar aplicações poderosas e completas. O uso descuidado de algumas funções pode introduzir vulnerabilidades e comprometer a integridade do código. Boas práticas e alternativas mais seguras ajudam a criar software confiável.

______

## Referências

- Documentação do Python: [https://docs.python.org](https://docs.python.org)
- Documentação do Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Guia OWASP de prevenção a XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Guia OWASP de prevenção a SQL injection: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Biblioteca Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentação do SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Módulo `secrets` do Python: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Pacote python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

