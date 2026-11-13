---
title: "Sicheres Programmieren mit Python"
date: 2023-09-26
lastmod: 2026-11-13
toc: true
draft: false
description: "Erfahren Sie, wie Sie sicheren Python-Code schreiben, unsichere Funktionen vermeiden und robuste, zuverlässige Anwendungen entwickeln."
genre: ["Programmierung", "Cybersicherheit", "Softwareentwicklung", "Python", "Codierung", "Webentwicklung", "Sicheres Programmieren", "Technologie", "Informatik", "Datensicherheit"]
tags: ["Python-Programmierung", "sicheres Programmieren", "sichere Python-Funktionen", "Codesicherheit", "Python-Alternativen", "bewährte Programmierpraktiken", "Cybersicherheit", "Programmiertipps", "Softwareentwicklung", "Webentwicklung", "unsichere Python-Funktionen vermeiden", "sichere Python-Anwendungen", "Maßnahmen zur Codesicherheit", "sichere Codepraktiken", "Tipps zur Programmiersicherheit"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Eine Illustration im Cartoonstil zeigt eine Entwicklerin, die sicher eine Mauer aus Codeblöcken baut. Das steht für sichere Python-Programmierpraktiken."
coverCaption: "Sicher bauen, selbstbewusst programmieren!"
---

## **Unsichere Python-Funktionen und ihre Alternativen**

Python ist eine vielseitige und weit verbreitete Programmiersprache mit Funktionen für viele Aufgaben. Doch nicht alle Funktionen sind gleich sicher. Einige bergen Sicherheitsrisiken und können bei unvorsichtiger Verwendung unbeabsichtigte Folgen haben. Dieser Abschnitt zeigt **unsichere Python-Funktionen**, konkrete Risiken und sicherere Alternativen mit vergleichbarem Nutzen. So stärken Sie **Sicherheit** und **Stabilität**.

### **Einleitung: Ihre Python-Anwendungen schützen**

Python ist wegen seiner umfangreichen Bibliothek und intuitiven Syntax beliebt. Einige Funktionen können bei falscher Verwendung jedoch Sicherheit und Zuverlässigkeit gefährden. Dieser Überblick soll keine Angst machen. Wenn Sie die Risiken kennen und andere Vorgehensweisen wählen, schreiben Sie Code, der Angriffen besser standhält.

___________

## **Unsichere Python-Funktionen und ihre Risiken**

### Dynamische Codeausführung mit `eval()`

`eval()` führt Python-Code aus einem String dynamisch aus. Das ist leistungsfähig, kann aber **Code-Injection-Angriffe** ermöglichen, wenn Benutzereingaben nicht richtig bereinigt werden. Verwenden Sie stattdessen **`ast.literal_eval()`** oder **`exec()`** für kontrollierte und sichere Codeausführung.

#### Dynamische Codeausführung mit eval():
```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### Sicherere Alternative mit `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### Stringverkettung mit ungeprüften Daten

Wenn Sie Strings mit ungeprüften Benutzereingaben verketten, entstehen möglicherweise **SQL-Injection-** oder **Cross-Site-Scripting-(XSS-)Schwachstellen**. Verwenden Sie **f-Strings** oder **`str.format()`** zusammen mit **Eingabevalidierung**, um diese Risiken zu vermeiden.

#### Unsichere Stringverkettung:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-Strings (formatierte Zeichenfolgenliterale):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** zur Objektserialisierung

Das Modul `pickle` serialisiert und deserialisiert Python-Objekte, ist aber **gegen fehlerhafte oder bösartig erstellte Daten nicht sicher**. Verwenden Sie zum sicheren Serialisieren Bibliotheken wie **`json`** oder **`marshal`**, die sicherere Serialisierungsverfahren unterstützen.

#### Unsichere Verwendung von pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### Sicherere Alternative mit json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### HTML mit `mark_safe()` unzureichend maskieren

Die Django-Funktion **`mark_safe()`** kennzeichnet einen String als sicheres HTML. Dadurch können Anwendungen **Cross-Site-Scripting-(XSS-)Angriffen** ausgesetzt werden. Verwenden Sie stattdessen Template-Escaping und den **`safe`**-Filter, damit HTML-Inhalte sicher ausgegeben werden.

#### Unsichere Verwendung von mark_safe() in einem Django-Template:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Sichererer Ansatz mit Template-Escaping:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### **`os.system()`** für Systembefehle verwenden

`os.system()` führt Systembefehle aus, ist aber anfällig für **Befehlseinschleusung**. Verwenden Sie das Modul **`subprocess`**, um Befehle sicherer auszuführen und ihre Ausgaben zu verarbeiten.

#### Unsichere Verwendung von os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Sicherere Alternative mit subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### Unzureichendes Passwort-Hashing mit `hash()`

`hash()` eignet sich wegen seiner Geschwindigkeit und Anfälligkeit für **Brute-Force-Angriffe** nicht zum sicheren Hashen von Passwörtern. Verwenden Sie robuste Passwort-Hashing-Bibliotheken wie **`bcrypt`** oder **`Argon2`**, um Passwörter besser zu schützen.

#### Unsicheres Passwort-Hashing mit hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### Sichererer Ansatz mit bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **Sicherere Alternativen und bewährte Praktiken**

### **`requests`** statt **`urllib`** verwenden

Verwenden Sie für HTTP-Anfragen bevorzugt die Bibliothek **`requests`** statt des veralteten `urllib`. `requests` bietet eine benutzerfreundlichere und sicherere Schnittstelle zum Senden von HTTP-Anfragen und Verarbeiten von Antworten.

#### HTTP-Anfragen mit der requests-Bibliothek:
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

### Dateien sicher mit der **`with`**-Anweisung verarbeiten

Verwenden Sie beim Arbeiten mit Dateien die **`with`**-Anweisung, um Ressourcenlecks zu vermeiden und Dateien korrekt zu verarbeiten. Sie schließt Dateien automatisch und senkt so das Risiko von Fehlern und Schwachstellen.

#### Dateiverarbeitung mit with:
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

### Eingaben mit **`html.escape()`** bereinigen

Um **XSS-Angriffe** zu verhindern, bereinigen Sie Benutzereingaben mit **`html.escape()`**. Die Funktion maskiert potenziell schädliche HTML-Inhalte vor der Ausgabe.

#### Benutzereingaben zum Schutz vor XSS bereinigen:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### Parametrisierte Abfragen mit **`sqlite3`**

Verwenden Sie beim Zugriff auf Datenbanken parametrisierte Abfragen mit **`sqlite3`**. So schützen Sie sich vor **SQL-Injection-Angriffen**, weil Benutzereingaben in Abfragen sicher als Werte übergeben werden.

#### Parametrisierte Abfragen mit sqlite3:
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

### Umgebungsvariablen sicher verwalten

Legen Sie vertrauliche Informationen nicht direkt im Code ab. Verwenden Sie Umgebungsvariablen über das Wörterbuch **`os.environ`** oder ein Paket wie **`python-decouple`** für sicherere Konfiguration.

#### Umgebungsvariablen mit os.environ verwalten:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### Umgebungsvariablen mit python-decouple verwalten:
```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### Starke Zufallswerte mit **`secrets`**

Verwenden Sie zum Erzeugen kryptografisch sicherer Zufallswerte das Modul **`secrets`** statt `random`. Es liefert Zufallswerte, die sich für sicherheitskritische Aufgaben eignen.

#### Sichere Zufallstoken mit secrets erzeugen:
```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```

## Fazit

Mit dem umfangreichen Python-Ökosystem entwickeln Sie leistungsfähige Anwendungen. Unvorsichtiger Umgang mit bestimmten Funktionen führt jedoch zu Sicherheitslücken und gefährdet die Integrität Ihres Codes. Mit bewährten Praktiken und sichereren Alternativen erstellen Sie zuverlässigere und sicherere Software.

______

## Quellen

- Python-Dokumentation: [https://docs.python.org](https://docs.python.org)
- Django-Dokumentation: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP-Leitfaden zur Vermeidung von Cross-Site-Scripting (XSS): [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP-Leitfaden zur Vermeidung von SQL-Injection: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests-Bibliothek: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3-Dokumentation: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python-Modul `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Paket python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

