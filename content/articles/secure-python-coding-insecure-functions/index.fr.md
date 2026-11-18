---
title: "Coder en Python de manière sécurisée"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "Apprenez à écrire du code Python sûr en évitant les fonctions risquées et en adoptant des pratiques pour créer des applications robustes et fiables."
genre: ["Programmation", "Cybersécurité", "Développement logiciel", "Python", "Codage", "Développement web", "Programmation sécurisée", "Technologie", "Informatique", "Sécurité des données"]
tags: ["programmation Python", "codage sécurisé", "fonctions Python sûres", "sécurité du code", "alternatives Python", "bonnes pratiques de programmation", "cybersécurité", "conseils de programmation", "développement logiciel", "développement web", "éviter les fonctions Python risquées", "applications Python sécurisées", "mesures de sécurité du code", "pratiques de code sécurisé", "conseils de sécurité en programmation"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "Illustration de style bande dessinée représentant une développeuse qui construit en sécurité un mur de blocs de code, symbole des pratiques de programmation Python sûres."
coverCaption: "Construisez en sécurité, codez en confiance !"
---

## **Fonctions Python risquées et leurs alternatives**

Python est un langage polyvalent et très répandu, doté de fonctions adaptées à de nombreuses tâches. Pourtant, toutes ne présentent pas le même niveau de sûreté. Certaines comportent des failles et peuvent produire des effets inattendus si elles sont utilisées sans précaution. Cette partie présente des **fonctions Python risquées**, leurs dangers et des alternatives plus sûres offrant une fonction équivalente pour renforcer la **sécurité** et la **stabilité**.

### **Introduction : protégez vos projets Python**

Python séduit par sa vaste bibliothèque et sa syntaxe intuitive. Une mauvaise utilisation de certaines fonctions peut pourtant compromettre la sécurité et la fiabilité. L'objectif est de repérer ces risques et d'adopter d'autres méthodes afin d'écrire du code plus résistant.

___________

## **Fonctions Python risquées et leurs risques**

### Exécution dynamique de code avec `eval()`

`eval()` exécute dynamiquement du code Python contenu dans une chaîne. Cette fonction puissante peut permettre des **attaques par injection de code** si les entrées utilisateur ne sont pas correctement assainies. Préférez **`ast.literal_eval()`** ou **`exec()`** pour une exécution contrôlée et sûre.

#### Exécution dynamique de code avec eval() :
```python
# Dangereux : utiliser eval() pour exécuter du code dynamique
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Résultat :", result)
```

#### Alternative plus sûre avec `ast.literal_eval()` :
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Valeur analysée :", parsed_value)
except (ValueError, SyntaxError):
    print("Entrée invalide.")
```

### Concaténation de chaînes avec des données non assainies

La concaténation de chaînes avec des entrées utilisateur non assainies peut provoquer des failles d'**injection SQL** ou de **script intersites (XSS)**. Utilisez des **f-strings** ou **`str.format()`** avec une **validation des entrées** pour éviter ces problèmes.

#### Concaténation de chaînes risquée :
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### Utilisation de f-strings (littéraux de chaîne formatés) :
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** pour sérialiser des objets

Le module `pickle` sérialise et désérialise des objets Python, mais **ne protège pas contre les données erronées ou conçues de façon malveillante**. Pour sérialiser des données en sécurité, optez pour des bibliothèques telles que **`json`** ou **`marshal`**, qui suivent des pratiques plus sûres.

#### Utilisation risquée de pickle :
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Stocker ou envoyer serialized_data
```

#### Alternative plus sûre avec json :
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Stocker ou envoyer serialized_data
```

### Échappement HTML insuffisant avec `mark_safe()`

La fonction **`mark_safe()`** de Django marque une chaîne comme HTML sûr. Cette opération peut exposer les applications à des **attaques XSS**. Utilisez plutôt l'échappement des modèles et le filtre **`safe`** pour afficher le contenu HTML en sécurité.

#### Utilisation risquée de mark_safe() dans un modèle Django :
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### Approche plus sûre avec l'échappement du modèle :
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### Utilisation de **`os.system()`** pour les commandes système

`os.system()` exécute des commandes système, mais reste vulnérable aux **attaques par injection de commande**. Utilisez le module **`subprocess`** pour exécuter les commandes de manière plus sûre et traiter leurs résultats.

#### Utilisation risquée de os.system() :
```python
command = input("Enter a command: ")
os.system(command)
```

#### Alternative plus sûre avec subprocess :
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Sortie :", result.stdout)
```

### Hachage de mots de passe insuffisant avec `hash()`

`hash()` ne convient pas au hachage sécurisé des mots de passe en raison de sa rapidité et de sa vulnérabilité aux **attaques par force brute**. Utilisez des bibliothèques robustes comme **`bcrypt`** ou **`Argon2`** pour mieux protéger les mots de passe.

#### Hachage risqué avec hash() :
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Stocker hashed_password dans la base de données
```

#### Approche plus sûre avec bcrypt :
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Stocker hashed_password dans la base de données
```

## **Alternatives plus sûres et bonnes pratiques**

### Préférez **`requests`** à **`urllib`**

Pour envoyer des requêtes HTTP, privilégiez la bibliothèque **`requests`** plutôt que `urllib`, qui est dépassée. `requests` fournit une interface plus simple et sûre pour envoyer des requêtes HTTP et traiter les réponses.

#### Requêtes HTTP avec la bibliothèque requests :
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Échec de la requête.")
```

### Gérer les fichiers en sécurité avec l'instruction **`with`**

Utilisez l'instruction **`with`** pour éviter les fuites de ressources et gérer correctement les fichiers. Elle les ferme automatiquement et réduit les risques d'erreurs et de failles.

#### Gestion de fichiers avec with :
```python
filename = "example.txt"

# Dangereux : sans utiliser with
file = open(filename, "r")
content = file.read()
file.close()

# Plus sûr : utiliser l’instruction with
with open(filename, "r") as file:
    content = file.read()
```

### Assainir les entrées avec **`html.escape()`**

Pour prévenir les **attaques XSS**, assainissez les entrées utilisateur avec **`html.escape()`**. Cette fonction échappe le contenu HTML potentiellement dangereux avant son affichage.

#### Assainir les entrées utilisateur contre XSS :
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Entrée assainie :", sanitized_input)
```

### Requêtes paramétrées avec **`sqlite3`**

Lors des échanges avec une base de données, utilisez les requêtes paramétrées de **`sqlite3`**. Elles contribuent à prévenir les **attaques par injection SQL** en transmettant les entrées comme valeurs.

#### Requête paramétrée avec sqlite3 :
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

### Gérer les variables d'environnement en sécurité

N'exposez pas de données sensibles directement dans le code. Utilisez des variables d'environnement via le dictionnaire **`os.environ`** ou un paquet tel que **`python-decouple`** pour une configuration plus sûre.

#### Gérer les variables avec os.environ :
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("Clé API :", api_key)
else:
    print("Clé API non définie.")
```

#### Gérer les variables avec python-decouple :
```python
from decouple import config

api_key = config("API_KEY")
print("Clé API :", api_key)
```

### Valeurs aléatoires robustes avec **`secrets`**

Pour générer des valeurs aléatoires cryptographiquement sûres, utilisez le module **`secrets`** plutôt que `random`. Il convient aux opérations sensibles pour la sécurité.

#### Générer des jetons sûrs avec secrets :
```python
import secrets

token = secrets.token_hex(16)
print("Jeton sécurisé :", token)
```

## Conclusion

Le vaste écosystème Python aide les développeurs à créer des applications riches en fonctionnalités. Toutefois, une utilisation imprudente de certaines fonctions peut introduire des failles et compromettre l'intégrité du code. En suivant de bonnes pratiques et en choisissant des alternatives plus sûres, vous produirez des logiciels plus fiables et sécurisés.

______

## Références

- Documentation Python : [https://docs.python.org](https://docs.python.org)
- Documentation Django : [https://docs.djangoproject.com](https://docs.djangoproject.com)
- Guide OWASP de prévention des scripts intersites (XSS) : [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Guide OWASP de prévention des injections SQL : [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Bibliothèque Python Requests : [https://docs.python-requests.org](https://docs.python-requests.org)
- Documentation SQLite3 : [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Module Python `secrets` : [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- Paquet python-decouple : [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)

