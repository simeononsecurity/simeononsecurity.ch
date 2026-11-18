---
title: "Programació segura amb Python"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Aprèn a escriure codi Python segur, evitar funcions insegures i aplicar bones pràctiques per crear aplicacions robustes i fiables."
genre: ["Programació", "Ciberseguretat", "Desenvolupament de programari", "Python", "Codificació", "Desenvolupament web", "Codificació segura", "Tecnologia", "Informàtica", "Seguretat de dades"]
tags: ["programació amb Python", "codificació segura", "funcions Python segures", "seguretat del codi", "alternatives de Python", "bones pràctiques de programació", "ciberseguretat", "consells de programació", "desenvolupament de programari", "desenvolupament web", "evitar funcions Python insegures", "aplicacions Python segures", "mesures de seguretat del codi", "pràctiques de codi segur", "consells de seguretat de programació"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Il·lustració de dibuixos animats d'una persona desenvolupadora que construeix amb seguretat un mur de blocs de codi, símbol de les pràctiques segures de programació amb Python."
coverCaption: "Construeix amb seguretat, programa amb confiança!"
---

## **Funcions insegures de Python i les seves alternatives**

Python és un llenguatge versàtil i molt utilitzat, amb funcions per a moltes tasques. Algunes, però, comporten riscos i efectes imprevistos si es fan servir sense cura. Aquest article presenta **funcions insegures de Python**, els seus riscos i alternatives més segures amb una funcionalitat semblant per reforçar la **seguretat** i l'**estabilitat**.

### **Introducció: protegeix els teus projectes Python**

Python és popular per les seves biblioteques extenses i la sintaxi intuïtiva. Si es gestionen malament, algunes funcions posen en perill la seguretat i la fiabilitat. Conèixer els riscos i escollir altres mètodes ajuda a escriure codi més resistent.

___________

## **Funcions insegures de Python i els seus riscos**

### Execució dinàmica de codi amb `eval()`

`eval()` executa dinàmicament codi Python des d'una cadena. Pot permetre **atacs d'injecció de codi** si no es netegen bé les entrades. Considera **`ast.literal_eval()`** o **`exec()`** per a una execució controlada i segura.

#### Execució dinàmica amb eval():
```python
# Insegur: ús d’eval() per executar codi dinàmic
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Resultat:", result)
```

#### Alternativa més segura amb `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Valor analitzat:", parsed_value)
except (ValueError, SyntaxError):
    print("Entrada no vàlida.")
```

### Concatenació de cadenes amb dades no netejades

Concatenar cadenes amb entrades d'usuari no netejades pot provocar **injecció SQL** o vulnerabilitats de **seqüències d'ordres entre llocs (XSS)**. Fes servir **f-strings** o **`str.format()`** amb **validació de l'entrada**.

#### Concatenació insegura de cadenes:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Ús de f-strings (cadenes literals formatades):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** per serialitzar objectes

El mòdul `pickle` serialitza i deserialitza objectes de Python, però **no és segur davant de dades incorrectes o creades amb intenció maliciosa**. Per serialitzar amb més seguretat, fes servir biblioteques com **`json`** o **`marshal`**.

#### Ús insegur de pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Desa o envia serialized_data
```

#### Alternativa més segura amb json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Desa o envia serialized_data
```

### Escapat HTML insuficient amb `mark_safe()`

La funció de Django **`mark_safe()`** marca una cadena com a HTML segur, fet que pot exposar aplicacions a **atacs XSS**. Fes servir l'escapat de plantilles i el filtre **`safe`** per representar HTML de manera segura.

#### Ús insegur de mark_safe() en una plantilla Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Enfocament més segur amb escapat de plantilles:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Ús de **`os.system()`** per executar ordres del sistema

`os.system()` executa ordres del sistema, però és vulnerable a la **injecció d'ordres**. Fes servir el mòdul **`subprocess`** per executar-les amb més seguretat i gestionar-ne la sortida.

#### Ús insegur de os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternativa més segura amb subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Sortida:", result.stdout)
```

### Hashing de contrasenyes insuficient amb `hash()`

`hash()` és massa ràpid i vulnerable als **atacs de força bruta**, per això no serveix per protegir contrasenyes. Fes servir biblioteques robustes com **`bcrypt`** o **`Argon2`**.

#### Hashing insegur de contrasenyes amb hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Desa hashed_password a la base de dades
```

#### Enfocament més segur amb bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Desa hashed_password a la base de dades
```

## **Alternatives més segures i bones pràctiques**

### Fes servir **`requests`** en lloc de **`urllib`**

Per a les peticions HTTP, prefereix **`requests`** a l'antic `urllib`. Ofereix una interfície més còmoda i segura per enviar peticions i gestionar respostes.

#### Peticions HTTP amb la biblioteca requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("La sol·licitud ha fallat.")
```

### Gestiona fitxers de manera segura amb **`with`**

Fes servir la instrucció **`with`** quan treballis amb fitxers per evitar fuites de recursos i gestionar-los bé. Tanca automàticament el fitxer i redueix el risc d'errors i vulnerabilitats.

#### Gestió de fitxers amb with:
```python
filename = "example.txt"

# Insegur: sense fer servir with
file = open(filename, "r")
content = file.read()
file.close()

# Més segur: fent servir la instrucció with
with open(filename, "r") as file:
    content = file.read()
```

### Neteja les entrades amb **`html.escape()`**

Per prevenir els **atacs XSS**, neteja les entrades d'usuari amb **`html.escape()`**, que escapa l'HTML potencialment perjudicial abans de mostrar-lo.

#### Neteja de l'entrada per prevenir XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Entrada sanejada:", sanitized_input)
```

### Consultes parametritzades amb **`sqlite3`**

Fes servir consultes parametritzades de **`sqlite3`** quan treballis amb bases de dades. Ajuden a prevenir **injeccions SQL** passant les entrades com a valors de consulta.

#### Consultes parametritzades amb sqlite3:
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

### Gestió segura de variables d'entorn

No exposis informació sensible directament al codi. Fes servir variables d'entorn amb **`os.environ`** o amb un paquet com **`python-decouple`**.

#### Gestió de variables amb os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Clau d’API:", api_key)
else:
    print("La clau d’API no està definida.")
```

#### Gestió de variables amb python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("Clau d’API:", api_key)
```

### Aleatorietat forta amb **`secrets`**

Fes servir **`secrets`** en lloc de `random` per generar valors aleatoris criptogràficament segurs. És adequat per a operacions sensibles a la seguretat.

#### Generació de tokens segurs amb secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Token segur:", token)
```

## Conclusió

L'ecosistema Python permet crear aplicacions potents i completes. L'ús imprudent d'algunes funcions pot introduir vulnerabilitats i comprometre la integritat del codi. Amb bones pràctiques i alternatives més segures pots crear programari més fiable.

______

## Referències

- Documentació de Python: [https://docs.python.org](https://docs.python.org)
- Documentació de Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Guia OWASP per prevenir XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Guia OWASP per prevenir injeccions SQL: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Biblioteca Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentació de SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Mòdul `secrets` de Python: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Paquet python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

