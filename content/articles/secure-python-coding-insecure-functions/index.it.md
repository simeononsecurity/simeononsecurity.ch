---
title: "Programmare in Python in modo sicuro"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Impara a scrivere codice Python sicuro evitando funzioni rischiose e seguendo buone pratiche per applicazioni robuste e affidabili."
genre: ["Programmazione", "Sicurezza informatica", "Sviluppo software", "Python", "Codifica", "Sviluppo web", "Codifica sicura", "Tecnologia", "Informatica", "Sicurezza dei dati"]
tags: ["programmazione Python", "codifica sicura", "funzioni Python sicure", "sicurezza del codice", "alternative Python", "buone pratiche di programmazione", "sicurezza informatica", "consigli di programmazione", "sviluppo software", "sviluppo web", "evitare funzioni Python rischiose", "applicazioni Python sicure", "misure di sicurezza del codice", "pratiche di codice sicuro", "consigli di sicurezza per la programmazione"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Illustrazione in stile cartone animato di uno sviluppatore che costruisce in sicurezza un muro di blocchi di codice, simbolo delle pratiche di programmazione Python sicura."
coverCaption: "Costruisci in sicurezza, programma con fiducia!"
---

## **Funzioni Python rischiose e alternative**

Python è un linguaggio versatile e diffuso, con strumenti per numerose attività. Alcune funzioni, però, comportano rischi e conseguenze impreviste se usate senza attenzione. Questa sezione presenta le **funzioni Python rischiose**, i pericoli associati e alternative più sicure con capacità equivalenti, per rafforzare **sicurezza** e **stabilità**.

### **Introduzione: proteggi i tuoi progetti Python**

Python è apprezzato per l'ampia libreria e la sintassi intuitiva. Se gestite male, alcune funzioni compromettono sicurezza e affidabilità. Conoscere i rischi e adottare altri metodi aiuta a creare codice più resistente.

___________

## **Funzioni Python rischiose e relativi pericoli**

### Esecuzione dinamica di codice con `eval()`

`eval()` esegue dinamicamente codice Python contenuto in una stringa. Può favorire **attacchi di code injection** se i dati inseriti dagli utenti non vengono ripuliti correttamente. Valuta **`ast.literal_eval()`** o **`exec()`** per un'esecuzione controllata e sicura.

#### Esecuzione dinamica con eval():
```python
# Non sicuro: uso di eval() per eseguire codice dinamico
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Risultato:", result)
```

#### Alternativa più sicura con `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Valore analizzato:", parsed_value)
except (ValueError, SyntaxError):
    print("Input non valido.")
```

### Concatenare stringhe con dati non ripuliti

Concatenare stringhe con input non ripuliti può causare vulnerabilità di **SQL injection** o **cross-site scripting (XSS)**. Usa **f-string** o **`str.format()`** insieme alla **convalida dell'input**.

#### Concatenazione rischiosa di stringhe:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Uso di f-string (stringhe letterali formattate):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** per serializzare oggetti

Il modulo `pickle` serializza e deserializza oggetti Python, ma **non è sicuro contro dati errati o costruiti in modo malevolo**. Per serializzare in modo più sicuro, scegli librerie come **`json`** o **`marshal`**.

#### Uso non sicuro di pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Memorizza o invia serialized_data
```

#### Alternativa più sicura con json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Memorizza o invia serialized_data
```

### Escape HTML insufficiente con `mark_safe()`

La funzione Django **`mark_safe()`** contrassegna una stringa come HTML sicuro, esponendo potenzialmente le applicazioni ad **attacchi XSS**. Usa invece l'escape dei template e il filtro **`safe`** per visualizzare HTML in modo sicuro.

#### Uso rischioso di mark_safe() in un template Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Approccio più sicuro con escape del template:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Usare **`os.system()`** per comandi di sistema

`os.system()` esegue comandi di sistema, ma è vulnerabile all'**iniezione di comandi**. Usa il modulo **`subprocess`** per eseguire comandi in modo più sicuro e gestirne i risultati.

#### Uso rischioso di os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternativa più sicura con subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Uscita:", result.stdout)
```

### Hash delle password inadeguato con `hash()`

La velocità di `hash()` e la sua vulnerabilità agli **attacchi brute force** lo rendono inadatto alla protezione delle password. Usa librerie robuste come **`bcrypt`** o **`Argon2`**.

#### Hash non sicuro con hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Memorizza hashed_password nel database
```

#### Approccio più sicuro con bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Memorizza hashed_password nel database
```

## **Alternative più sicure e buone pratiche**

### Preferisci **`requests`** a **`urllib`**

Per le richieste HTTP, preferisci **`requests`** al superato `urllib`. Offre un'interfaccia più semplice e sicura per inviare richieste e gestire risposte.

#### Richieste HTTP con requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Richiesta non riuscita.")
```

### Gestire i file in sicurezza con **`with`**

Usa l'istruzione **`with`** con i file per evitare perdite di risorse e gestire correttamente l'apertura e la chiusura. Riduce il rischio di errori e vulnerabilità.

#### Gestione dei file con with:
```python
filename = "example.txt"

# Non sicuro: senza usare with
file = open(filename, "r")
content = file.read()
file.close()

# Più sicuro: usa l’istruzione with
with open(filename, "r") as file:
    content = file.read()
```

### Ripulire gli input con **`html.escape()`**

Per prevenire gli **attacchi XSS**, ripulisci l'input con **`html.escape()`**, che esegue l'escape dell'HTML potenzialmente dannoso prima di mostrarlo.

#### Ripulire l'input per prevenire XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Input sanificato:", sanitized_input)
```

### Query parametrizzate con **`sqlite3`**

Usa query parametrizzate di **`sqlite3`** quando interagisci con database. Aiutano a prevenire **SQL injection** passando i dati degli utenti come valori della query.

#### Query parametrizzate con sqlite3:
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

### Gestire le variabili d'ambiente in modo sicuro

Non esporre informazioni sensibili direttamente nel codice. Usa variabili d'ambiente con **`os.environ`** o un pacchetto come **`python-decouple`**.

#### Variabili d'ambiente con os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Chiave API:", api_key)
else:
    print("Chiave API non impostata.")
```

#### Variabili d'ambiente con python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("Chiave API:", api_key)
```

### Valori casuali robusti con **`secrets`**

Per generare valori casuali crittograficamente sicuri, usa **`secrets`** anziché `random`. È indicato per le operazioni sensibili alla sicurezza.

#### Generare token sicuri con secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Token sicuro:", token)
```

## Conclusione

L'ecosistema Python consente di sviluppare applicazioni ricche di funzionalità. L'uso imprudente di alcune funzioni può introdurre vulnerabilità e compromettere l'integrità del codice. Buone pratiche e alternative più sicure aiutano a realizzare software affidabile.

______

## Riferimenti

- Documentazione Python: [https://docs.python.org](https://docs.python.org)
- Documentazione Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Guida OWASP per prevenire XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Guida OWASP per prevenire SQL injection: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Libreria Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentazione SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Modulo Python `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Pacchetto python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

