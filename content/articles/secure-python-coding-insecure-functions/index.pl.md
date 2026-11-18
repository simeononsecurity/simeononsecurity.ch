---
title: "Bezpieczne programowanie w Pythonie"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Dowiedz się, jak pisać bezpieczny kod w Pythonie, unikać niebezpiecznych funkcji i tworzyć niezawodne aplikacje."
genre: ["Programowanie", "Cyberbezpieczeństwo", "Tworzenie oprogramowania", "Python", "Kodowanie", "Tworzenie stron internetowych", "Bezpieczne kodowanie", "Technologia", "Informatyka", "Bezpieczeństwo danych"]
tags: ["programowanie w Pythonie", "bezpieczne kodowanie", "bezpieczne funkcje Pythona", "bezpieczeństwo kodu", "alternatywy dla Pythona", "dobre praktyki programowania", "cyberbezpieczeństwo", "porady programistyczne", "tworzenie oprogramowania", "tworzenie stron internetowych", "unikanie niebezpiecznych funkcji Pythona", "bezpieczne aplikacje Python", "środki ochrony kodu", "praktyki bezpiecznego kodowania", "porady dotyczące bezpieczeństwa programowania"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Ilustracja w stylu kreskówkowym przedstawia programistę bezpiecznie budującego mur z bloków kodu, symbolizujący bezpieczne praktyki programowania w Pythonie."
coverCaption: "Buduj bezpiecznie, koduj z pewnością!"
---

## **Niebezpieczne funkcje Pythona i ich alternatywy**

Python to wszechstronny i popularny język z funkcjami do wielu zadań. Nie wszystkie funkcje są jednak równie bezpieczne. Niektóre niosą ryzyko i mogą powodować niezamierzone skutki przy nieostrożnym użyciu. W tej części omawiamy **niebezpieczne funkcje Pythona**, związane z nimi zagrożenia oraz bezpieczniejsze zamienniki o podobnym zastosowaniu, które wspierają **bezpieczeństwo** i **stabilność**.

### **Wprowadzenie: chroń swoje projekty w Pythonie**

Python przyciąga rozbudowaną biblioteką i intuicyjną składnią. Niewłaściwe użycie niektórych funkcji może jednak osłabić bezpieczeństwo i niezawodność. Poznaj zagrożenia i wybieraj inne metody, by tworzyć kod odporniejszy na problemy.

___________

## **Niebezpieczne funkcje Pythona i związane z nimi ryzyko**

### Dynamiczne wykonywanie kodu za pomocą `eval()`

`eval()` dynamicznie wykonuje kod Pythona z ciągu znaków. Ta funkcja może umożliwić **ataki polegające na wstrzyknięciu kodu**, jeśli dane użytkownika nie zostaną prawidłowo oczyszczone. Zamiast `eval()` rozważ **`ast.literal_eval()`** lub **`exec()`** do kontrolowanego i bezpiecznego wykonywania kodu.

#### Dynamiczne wykonywanie kodu za pomocą eval():
```python
# Niebezpieczne: użycie eval() do dynamicznego wykonywania kodu
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Wynik:", result)
```

#### Bezpieczniejsza alternatywa z `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Przetworzona wartość:", parsed_value)
except (ValueError, SyntaxError):
    print("Nieprawidłowe dane wejściowe.")
```

### Łączenie ciągów znaków z nieoczyszczonymi danymi

Łączenie ciągów z nieoczyszczonymi danymi użytkownika może prowadzić do **wstrzyknięcia SQL** lub podatności na **cross-site scripting (XSS)**. Używaj **f-stringów** lub **`str.format()`** wraz z **walidacją danych wejściowych**.

#### Niebezpieczne łączenie ciągów:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-stringi (formatowane literały ciągów):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** do serializacji obiektów

Moduł `pickle` serializuje i deserializuje obiekty Pythona, ale **nie chroni przed błędnymi ani złośliwie przygotowanymi danymi**. Do bezpieczniejszej serializacji wybieraj biblioteki takie jak **`json`** lub **`marshal`**.

#### Niebezpieczne użycie pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Zapisz lub wyślij serialized_data
```

#### Bezpieczniejsza alternatywa z json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Zapisz lub wyślij serialized_data
```

### Niewystarczające escapowanie HTML za pomocą `mark_safe()`

Funkcja Django **`mark_safe()`** oznacza ciąg jako bezpieczny HTML, co może narazić aplikację na **ataki XSS**. Zamiast tego używaj escapowania szablonów i filtra **`safe`**, aby bezpiecznie wyświetlać HTML.

#### Niebezpieczne użycie mark_safe() w szablonie Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Bezpieczniejsze podejście z escapowaniem szablonu:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Używanie **`os.system()`** do poleceń systemowych

`os.system()` wykonuje polecenia systemowe, ale jest podatne na **wstrzykiwanie poleceń**. Użyj modułu **`subprocess`**, aby bezpieczniej uruchamiać polecenia i obsługiwać ich wyniki.

#### Niebezpieczne użycie os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### Bezpieczniejsza alternatywa z subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Wyjście:", result.stdout)
```

### Niewłaściwe haszowanie haseł za pomocą `hash()`

Ze względu na szybkość i podatność na **ataki siłowe** funkcja `hash()` nie nadaje się do bezpiecznego haszowania haseł. Zastosuj solidne biblioteki, takie jak **`bcrypt`** lub **`Argon2`**.

#### Niebezpieczne haszowanie hasła funkcją hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Zapisz hashed_password w bazie danych
```

#### Bezpieczniejsze podejście z bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Zapisz hashed_password w bazie danych
```

## **Bezpieczniejsze alternatywy i dobre praktyki**

### Używaj **`requests`** zamiast **`urllib`**

Do żądań HTTP wybieraj bibliotekę **`requests`** zamiast przestarzałego `urllib`. Zapewnia ona wygodniejszy i bezpieczniejszy interfejs do wysyłania żądań i obsługi odpowiedzi.

#### Żądania HTTP z biblioteką requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Żądanie nie powiodło się.")
```

### Bezpieczna obsługa plików z instrukcją **`with`**

Używaj **`with`** podczas pracy z plikami, aby uniknąć wycieków zasobów i prawidłowo je obsługiwać. Instrukcja automatycznie zamyka plik, ograniczając ryzyko błędów i podatności.

#### Obsługa plików z with:
```python
filename = "example.txt"

# Niebezpieczne: bez użycia with
file = open(filename, "r")
content = file.read()
file.close()

# Bezpieczniej: użyj instrukcji with
with open(filename, "r") as file:
    content = file.read()
```

### Oczyszczanie danych przez **`html.escape()`**

Aby zapobiegać **atakom XSS**, oczyszczaj dane użytkownika funkcją **`html.escape()`**. Escapuje ona potencjalnie szkodliwy HTML przed wyświetleniem.

#### Oczyszczanie danych wejściowych w celu ochrony przed XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Oczyszczone dane wejściowe:", sanitized_input)
```

### Parametryzowane zapytania w **`sqlite3`**

Podczas pracy z bazami danych używaj parametryzowanych zapytań biblioteki **`sqlite3`**. Pomaga to zapobiegać **atakom SQL injection**, przekazując dane użytkownika jako wartości.

#### Parametryzowane zapytania w sqlite3:
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

### Bezpieczne zarządzanie zmiennymi środowiskowymi

Nie umieszczaj poufnych informacji bezpośrednio w kodzie. Używaj zmiennych środowiskowych przez słownik **`os.environ`** lub pakiet taki jak **`python-decouple`**.

#### Zarządzanie zmiennymi przez os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Klucz API:", api_key)
else:
    print("Klucz API nie jest ustawiony.")
```

#### Zarządzanie zmiennymi przez python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("Klucz API:", api_key)
```

### Silne wartości losowe dzięki **`secrets`**

Do generowania kryptograficznie bezpiecznych wartości losowych używaj modułu **`secrets`** zamiast `random`. Nadaje się on do operacji wymagających bezpieczeństwa.

#### Generowanie bezpiecznych tokenów za pomocą secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Bezpieczny token:", token)
```

## Podsumowanie

Rozbudowany ekosystem Pythona pozwala tworzyć zaawansowane aplikacje. Nieostrożne użycie niektórych funkcji może jednak wprowadzić podatności i zagrozić integralności kodu. Dobre praktyki i bezpieczniejsze alternatywy pomagają tworzyć niezawodne oprogramowanie.

______

## Źródła

- Dokumentacja Pythona: [https://docs.python.org](https://docs.python.org)
- Dokumentacja Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Poradnik OWASP dotyczący zapobiegania XSS: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Poradnik OWASP dotyczący zapobiegania SQL injection: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Biblioteka Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- Dokumentacja SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Moduł Pythona `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Pakiet python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

