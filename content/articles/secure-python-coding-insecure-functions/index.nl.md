---
title: "Veilig programmeren in Python"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Leer veilige Python-code schrijven door onveilige functies te vermijden en goede praktijken voor robuuste, betrouwbare toepassingen te volgen."
genre: ["Programmeren", "Cyberbeveiliging", "Softwareontwikkeling", "Python", "Coderen", "Webontwikkeling", "Veilig coderen", "Technologie", "Informatica", "Gegevensbeveiliging"]
tags: ["Python-programmeren", "veilig coderen", "veilige Python-functies", "codebeveiliging", "Python-alternatieven", "goede programmeerpraktijken", "cyberbeveiliging", "programmeertips", "softwareontwikkeling", "webontwikkeling", "onveilige Python-functies vermijden", "veilige Python-toepassingen", "maatregelen voor codebeveiliging", "veilige codepraktijken", "tips voor programmeerbeveiliging"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Een illustratie in cartoonstijl toont een ontwikkelaar die veilig een muur van codeblokken bouwt, als symbool voor veilige Python-programmeerpraktijken."
coverCaption: "Bouw veilig, codeer met vertrouwen!"
---

## **Onveilige Python-functies en alternatieven**

Python is veelzijdig en wordt veel gebruikt. Het biedt functies voor allerlei taken, maar sommige functies brengen beveiligingsrisico's en onverwachte gevolgen mee als je ze onvoorzichtig gebruikt. Dit artikel bespreekt **onveilige Python-functies**, hun risico's en veiligere alternatieven met vergelijkbare functionaliteit, zodat je de **beveiliging** en **stabiliteit** van je code verbetert.

### **Inleiding: bescherm je Python-projecten**

Python is populair door de uitgebreide bibliotheek en intuïtieve syntaxis. Verkeerd gebruik van sommige functies kan de beveiliging en betrouwbaarheid ondermijnen. Leer de risico's herkennen en kies andere methoden om code te bouwen die beter tegen aanvallen bestand is.

___________

## **Onveilige Python-functies en hun risico's**

### Dynamische code-uitvoering met `eval()`

`eval()` voert Python-code uit een tekenreeks dynamisch uit. De functie is krachtig, maar kan **code-injectieaanvallen** mogelijk maken als invoer niet goed wordt opgeschoond. Kies **`ast.literal_eval()`** of **`exec()`** voor gecontroleerde en veilige code-uitvoering.

#### Dynamische code-uitvoering met eval():
```python
# Onveilig: eval() gebruiken voor dynamische code-uitvoering
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Resultaat:", result)
```

#### Veiliger alternatief met `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Geparseerde waarde:", parsed_value)
except (ValueError, SyntaxError):
    print("Ongeldige invoer.")
```

### Tekenreeksen samenvoegen met onbewerkte invoer

Tekenreeksen samenvoegen met niet-opgeschoonde gebruikersinvoer kan leiden tot **SQL-injectie** of **cross-site scripting (XSS)**. Gebruik **f-strings** of **`str.format()`** in combinatie met **invoervalidatie**.

#### Onveilige samenvoeging van tekenreeksen:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-strings gebruiken (opgemaakte tekenreeksliteralen):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** voor objectserialisatie

De module `pickle` kan Python-objecten serialiseren en deserialiseren, maar is **niet veilig voor foutieve of kwaadwillig samengestelde gegevens**. Gebruik voor veiligere serialisatie bibliotheken zoals **`json`** of **`marshal`**.

#### Onveilig gebruik van pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# serialized_data opslaan of verzenden
```

#### Veiliger alternatief met json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# serialized_data opslaan of verzenden
```

### HTML onvoldoende escapen met `mark_safe()`

Django's functie **`mark_safe()`** markeert een tekenreeks als veilige HTML, waardoor toepassingen mogelijk kwetsbaar zijn voor **XSS-aanvallen**. Gebruik template-escaping en het filter **`safe`** om HTML veilig weer te geven.

#### Onveilig gebruik van mark_safe() in een Django-template:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Veiliger aanpak met template-escaping:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### **`os.system()`** voor systeemopdrachten

`os.system()` voert systeemopdrachten uit, maar is gevoelig voor **opdrachtinjectie**. Gebruik **`subprocess`** om opdrachten veiliger uit te voeren en de uitvoer af te handelen.

#### Onveilig gebruik van os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Veiliger alternatief met subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Uitvoer:", result.stdout)
```

### Onvoldoende wachtwoordhashing met `hash()`

`hash()` is door zijn snelheid en kwetsbaarheid voor **bruteforceaanvallen** ongeschikt voor het veilig hashen van wachtwoorden. Gebruik robuuste bibliotheken zoals **`bcrypt`** of **`Argon2`**.

#### Onveilige wachtwoordhashing met hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# hashed_password in de database opslaan
```

#### Veiliger aanpak met bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# hashed_password in de database opslaan
```

## **Veiligere alternatieven en goede praktijken**

### Gebruik **`requests`** in plaats van **`urllib`**

Geef voor HTTP-verzoeken de voorkeur aan **`requests`** boven het verouderde `urllib`. `requests` biedt een gebruiksvriendelijkere en veiligere interface om verzoeken te versturen en reacties te verwerken.

#### HTTP-verzoeken met de requests-bibliotheek:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Verzoek mislukt.")
```

### Bestanden veilig verwerken met de **`with`**-instructie

Gebruik **`with`** voor bestandsbewerkingen om resourcelekken te voorkomen en bestanden goed af te handelen. De instructie sluit bestanden automatisch en vermindert het risico op fouten en kwetsbaarheden.

#### Bestandsverwerking met with:
```python
filename = "example.txt"

# Onveilig: zonder with te gebruiken
file = open(filename, "r")
content = file.read()
file.close()

# Veiliger: de with-instructie gebruiken
with open(filename, "r") as file:
    content = file.read()
```

### Invoer opschonen met **`html.escape()`**

Voorkom **XSS-aanvallen** door invoer op te schonen met **`html.escape()`**. Deze functie escaped mogelijk schadelijke HTML voordat je die weergeeft.

#### Gebruikersinvoer opschonen tegen XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Geschoonde invoer:", sanitized_input)
```

### Geparametriseerde query's met **`sqlite3`**

Gebruik bij databasebewerkingen geparametriseerde query's met **`sqlite3`**. Ze helpen **SQL-injectieaanvallen** voorkomen door invoer als querywaarden door te geven.

#### Geparametriseerde query's met sqlite3:
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

### Omgevingsvariabelen veilig beheren

Zet gevoelige informatie niet rechtstreeks in code. Gebruik omgevingsvariabelen via **`os.environ`** of een pakket zoals **`python-decouple`** voor veiliger configuratiebeheer.

#### Omgevingsvariabelen beheren met os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API-sleutel:", api_key)
else:
    print("API-sleutel is niet ingesteld.")
```

#### Omgevingsvariabelen beheren met python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("API-sleutel:", api_key)
```

### Sterke willekeur met **`secrets`**

Gebruik **`secrets`** in plaats van `random` om cryptografisch veilige willekeurige waarden te genereren. Dit past bij beveiligingsgevoelige taken.

#### Veilige tokens genereren met secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Beveiligd token:", token)
```

## Conclusie

Het Python-ecosysteem helpt ontwikkelaars krachtige toepassingen te bouwen. Onzorgvuldig gebruik van bepaalde functies kan echter kwetsbaarheden veroorzaken en de integriteit van code aantasten. Met goede praktijken en veiligere alternatieven bouw je betrouwbaardere software.

______

## Bronnen

- Python-documentatie: [https://docs.python.org](https://docs.python.org)
- Django-documentatie: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP-gids voor preventie van cross-site scripting (XSS): [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP-gids voor preventie van SQL-injectie: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests-bibliotheek: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3-documentatie: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python-module `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decouple-pakket: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

