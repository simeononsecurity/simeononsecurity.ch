---
title: "Programación segura en Python"
date: 2023-09-26
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprende a escribir código seguro en Python, evitar funciones inseguras y crear aplicaciones robustas y fiables."
genre: ["Programación", "Ciberseguridad", "Desarrollo de software", "Python", "Codificación", "Desarrollo web", "Programación segura", "Tecnología", "Informática", "Seguridad de datos"]
tags: ["programación en Python", "codificación segura", "funciones seguras de Python", "seguridad del código", "alternativas de Python", "buenas prácticas de programación", "ciberseguridad", "consejos de programación", "desarrollo de software", "desarrollo web", "evitar funciones inseguras de Python", "aplicaciones seguras de Python", "medidas de seguridad del código", "prácticas de código seguro", "consejos de seguridad en programación"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Ilustración de estilo caricatura de una persona desarrolladora que construye de forma segura un muro de bloques de código, símbolo de las prácticas seguras de programación en Python."
coverCaption: "Construye de forma segura, programa con confianza."
---

## **Funciones inseguras de Python y sus alternativas**

Python es un lenguaje versátil y muy usado, con funciones para muchas tareas. Sin embargo, no todas las funciones son igual de seguras. Algunas presentan vulnerabilidades y efectos inesperados si se usan sin cuidado. Esta sección examina **funciones inseguras de Python**, sus riesgos y alternativas más seguras con una funcionalidad equivalente para reforzar la **seguridad** y la **estabilidad**.

### **Introducción: protege tus proyectos de Python**

Python destaca por su amplia biblioteca y sintaxis intuitiva. Algunas funciones, si se manejan mal, ponen en riesgo la seguridad y la fiabilidad. Este recorrido no busca alarmar, sino ayudar a reconocer esos peligros y elegir otros métodos para escribir código más resistente.

___________

## **Funciones inseguras de Python y sus riesgos**

### Ejecución dinámica de código con `eval()`

`eval()` ejecuta dinámicamente código Python desde una cadena. Aunque es potente, puede permitir **ataques de inyección de código** si las entradas del usuario no se depuran correctamente. En lugar de `eval()`, considera **`ast.literal_eval()`** o **`exec()`** para una ejecución controlada y segura.

#### Ejecución dinámica de código con eval():
```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### Alternativa más segura con `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### Concatenación de cadenas con datos sin depurar

Concatenar cadenas con entradas de usuario sin depurar puede causar vulnerabilidades de **inyección SQL** o **secuencias de comandos en sitios cruzados (XSS)**. Usa **f-strings** o **`str.format()`** junto con la **validación de entradas** para evitar estos problemas.

#### Concatenación insegura de cadenas:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Uso de f-strings (literales de cadena formateados):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** para serializar objetos

El módulo `pickle` serializa y deserializa objetos de Python, pero **no es seguro ante datos erróneos o creados con fines maliciosos**. Para serializar datos con mayor seguridad, elige bibliotecas como **`json`** o **`marshal`**, que siguen prácticas de serialización más seguras.

#### Uso inseguro de pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### Alternativa más segura con json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### Escapado insuficiente de HTML con `mark_safe()`

La función **`mark_safe()`** de Django marca una cadena como HTML seguro, lo que puede exponer aplicaciones a **ataques XSS**. En su lugar, usa el escapado de plantillas y el filtro **`safe`** para representar el contenido HTML de forma segura.

#### Uso inseguro de mark_safe() en una plantilla de Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Enfoque más seguro con escapado de plantillas:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Uso de **`os.system()`** para ejecutar comandos

`os.system()` ejecuta comandos del sistema, pero es vulnerable a **ataques de inyección de comandos**. Usa el módulo **`subprocess`** para ejecutar comandos de forma más segura y gestionar sus resultados.

#### Uso inseguro de os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternativa más segura con subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### Hashing de contraseñas inadecuado con `hash()`

`hash()` no es adecuado para proteger contraseñas por su velocidad y vulnerabilidad a los **ataques de fuerza bruta**. Usa bibliotecas robustas de hashing de contraseñas, como **`bcrypt`** o **`Argon2`**, para reforzar su seguridad.

#### Hashing inseguro de contraseñas con hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### Enfoque más seguro con bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **Alternativas más seguras y buenas prácticas**

### Usa **`requests`** en lugar de **`urllib`**

Para realizar solicitudes HTTP, prefiere la biblioteca **`requests`** frente al obsoleto `urllib`. `requests` ofrece una interfaz más sencilla y segura para enviar solicitudes HTTP y procesar respuestas.

#### Solicitudes HTTP con la biblioteca requests:
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

### Manejo seguro de archivos con la instrucción **`with`**

Usa la instrucción **`with`** al trabajar con archivos para evitar fugas de recursos y gestionarlos correctamente. Cierra los archivos automáticamente y reduce el riesgo de errores y vulnerabilidades.

#### Manejo de archivos con with:
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

### Depura entradas con **`html.escape()`**

Para prevenir **ataques XSS**, depura las entradas del usuario con **`html.escape()`**. La función escapa el HTML potencialmente dañino antes de mostrarlo.

#### Depuración de entradas para prevenir XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### Consultas parametrizadas con **`sqlite3`**

Al trabajar con bases de datos, usa consultas parametrizadas de **`sqlite3`**. Esto ayuda a evitar **ataques de inyección SQL** al pasar las entradas como valores de consulta.

#### Consultas parametrizadas con sqlite3:
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

### Gestión segura de variables de entorno

No expongas información confidencial directamente en el código. Usa variables de entorno mediante el diccionario **`os.environ`** o un paquete como **`python-decouple`** para gestionar la configuración de forma más segura.

#### Gestión de variables con os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### Gestión de variables con python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### Aleatoriedad robusta con **`secrets`**

Usa el módulo **`secrets`** en vez de `random` para generar valores aleatorios criptográficamente seguros. Es adecuado para operaciones sensibles a la seguridad.

#### Generación de tokens seguros con secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```

## Conclusión

El amplio ecosistema de Python ayuda a crear aplicaciones potentes y completas. Pero usar ciertas funciones sin cuidado introduce vulnerabilidades y pone en riesgo la integridad del código. Con buenas prácticas y alternativas más seguras puedes crear software más fiable y seguro.

______

## Referencias

- Documentación de Python: [https://docs.python.org](https://docs.python.org)
- Documentación de Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Guía de OWASP para prevenir XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Guía de OWASP para prevenir inyección SQL: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Biblioteca Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentación de SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Módulo `secrets` de Python: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Paquete python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

