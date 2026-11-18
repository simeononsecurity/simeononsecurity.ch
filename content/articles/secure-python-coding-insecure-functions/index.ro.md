---
title: "Programare sigură în Python"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Învață să scrii cod Python sigur, să eviți funcțiile riscante și să aplici bune practici pentru aplicații robuste și fiabile."
genre: ["Programare", "Securitate cibernetică", "Dezvoltare software", "Python", "Codare", "Dezvoltare web", "Codare sigură", "Tehnologie", "Informatică", "Securitatea datelor"]
tags: ["programare Python", "codare sigură", "funcții Python sigure", "securitatea codului", "alternative Python", "bune practici de programare", "securitate cibernetică", "sfaturi de programare", "dezvoltare software", "dezvoltare web", "evitarea funcțiilor Python riscante", "aplicații Python sigure", "măsuri de securitate pentru cod", "practici de cod sigure", "sfaturi de securitate în programare"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Ilustrație în stil de desen animat cu un dezvoltator care construiește în siguranță un zid din blocuri de cod, simbolizând practicile sigure de programare Python."
coverCaption: "Construiește în siguranță, programează cu încredere!"
---

## **Funcții Python riscante și alternativele lor**

Python este un limbaj versatil și răspândit, cu funcții pentru multe sarcini. Unele funcții prezintă riscuri de securitate și pot produce efecte neașteptate dacă sunt folosite fără grijă. Această secțiune prezintă **funcții Python riscante**, pericolele asociate și alternative mai sigure cu utilizare similară, pentru a consolida **securitatea** și **stabilitatea**.

### **Introducere: protejează-ți proiectele Python**

Python este apreciat pentru biblioteca extinsă și sintaxa intuitivă. Folosirea greșită a unor funcții poate afecta securitatea și fiabilitatea. Înțelegerea riscurilor și alegerea altor metode ajută la scrierea unui cod mai rezistent.

___________

## **Funcții Python riscante și pericolele lor**

### Executarea dinamică a codului cu `eval()`

`eval()` execută dinamic cod Python dintr-un șir. Poate permite **atacuri prin injectare de cod** dacă intrările utilizatorilor nu sunt curățate corespunzător. Ia în considerare **`ast.literal_eval()`** sau **`exec()`** pentru executare controlată și sigură.

#### Executarea dinamică a codului cu eval():
```python
# Nesigur: utilizarea eval() pentru executarea codului dinamic
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Rezultat:", result)
```

#### Alternativă mai sigură cu `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Valoare analizată:", parsed_value)
except (ValueError, SyntaxError):
    print("Intrare nevalidă.")
```

### Concatenarea șirurilor cu date necurățate

Concatenarea șirurilor cu intrări necurățate poate produce **injecții SQL** sau vulnerabilități de **cross-site scripting (XSS)**. Folosește **f-string-uri** sau **`str.format()`** împreună cu **validarea intrărilor**.

#### Concatenare nesigură a șirurilor:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Folosirea f-string-urilor (șiruri formatate literale):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** pentru serializarea obiectelor

Modulul `pickle` serializează și deserialează obiecte Python, dar **nu este sigur împotriva datelor greșite sau construite cu intenții malițioase**. Pentru o serializare mai sigură, alege biblioteci precum **`json`** sau **`marshal`**.

#### Folosirea nesigură a pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Stochează sau trimite serialized_data
```

#### Alternativă mai sigură cu json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Stochează sau trimite serialized_data
```

### Escaparea insuficientă a HTML cu `mark_safe()`

Funcția Django **`mark_safe()`** marchează un șir drept HTML sigur și poate expune aplicațiile la **atacuri XSS**. Folosește escaparea șabloanelor și filtrul **`safe`** pentru afișarea sigură a conținutului HTML.

#### Folosirea nesigură a mark_safe() într-un șablon Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Abordare mai sigură cu escaparea șablonului:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Folosirea **`os.system()`** pentru comenzi de sistem

`os.system()` execută comenzi de sistem, dar este vulnerabilă la **injectarea comenzilor**. Folosește modulul **`subprocess`** pentru executarea mai sigură a comenzilor și gestionarea rezultatelor.

#### Folosirea nesigură a os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternativă mai sigură cu subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Ieșire:", result.stdout)
```

### Hashing insuficient al parolelor cu `hash()`

`hash()` nu este potrivită pentru protejarea parolelor din cauza vitezei și vulnerabilității la **atacuri prin forță brută**. Folosește biblioteci robuste precum **`bcrypt`** sau **`Argon2`**.

#### Hashing nesigur al parolei cu hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Stochează hashed_password în baza de date
```

#### Abordare mai sigură cu bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Stochează hashed_password în baza de date
```

## **Alternative mai sigure și bune practici**

### Folosește **`requests`** în loc de **`urllib`**

Pentru solicitări HTTP, preferă **`requests`** în locul bibliotecii învechite `urllib`. Oferă o interfață mai comodă și mai sigură pentru trimiterea solicitărilor și procesarea răspunsurilor.

#### Solicitări HTTP cu biblioteca requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Cererea a eșuat.")
```

### Gestionarea sigură a fișierelor cu instrucțiunea **`with`**

Folosește **`with`** când lucrezi cu fișiere pentru a evita pierderile de resurse și a le gestiona corect. Instrucțiunea închide automat fișierele și reduce riscul de erori și vulnerabilități.

#### Gestionarea fișierelor cu with:
```python
filename = "example.txt"

# Nesigur: fără utilizarea lui with
file = open(filename, "r")
content = file.read()
file.close()

# Mai sigur: utilizează instrucțiunea with
with open(filename, "r") as file:
    content = file.read()
```

### Curățarea intrărilor cu **`html.escape()`**

Pentru a preveni **atacurile XSS**, curăță intrările utilizatorilor cu **`html.escape()`**. Funcția escapează HTML-ul potențial periculos înainte de afișare.

#### Curățarea intrării utilizatorului pentru prevenirea XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Intrare igienizată:", sanitized_input)
```

### Interogări parametrizate cu **`sqlite3`**

Folosește interogări parametrizate **`sqlite3`** pentru operațiile cu baze de date. Acestea ajută la prevenirea **injecțiilor SQL**, transmițând intrările drept valori ale interogării.

#### Interogări parametrizate cu sqlite3:
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

### Gestionarea sigură a variabilelor de mediu

Nu expune informații sensibile direct în cod. Folosește variabile de mediu prin dicționarul **`os.environ`** sau un pachet precum **`python-decouple`**.

#### Gestionarea variabilelor cu os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Cheie API:", api_key)
else:
    print("Cheia API nu este setată.")
```

#### Gestionarea variabilelor cu python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("Cheie API:", api_key)
```

### Valori aleatoare puternice cu **`secrets`**

Folosește **`secrets`** în loc de `random` pentru valori aleatoare sigure criptografic. Modulul este potrivit pentru operații sensibile la securitate.

#### Generarea de tokenuri sigure cu secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Token securizat:", token)
```

## Concluzie

Ecosistemul Python ajută dezvoltatorii să creeze aplicații puternice și complexe. Folosirea neatentă a unor funcții poate introduce vulnerabilități și compromite integritatea codului. Bunele practici și alternativele mai sigure ajută la crearea unui software mai fiabil.

______

## Referințe

- Documentația Python: [https://docs.python.org](https://docs.python.org)
- Documentația Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Ghidul OWASP pentru prevenirea XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Ghidul OWASP pentru prevenirea injecțiilor SQL: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Biblioteca Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentația SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Modulul Python `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Pachetul python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

