---
title: "Estàndards de codificació segura per a Python: bones pràctiques"
date: 2023-02-26
lastmod: 2026-11-19
toc: true
draft: false
description: "Aprèn les bones pràctiques de codificació segura en Python per reduir el risc d'intrusions i protegir les dades sensibles."
tags: ["Python", "Codificació segura", "Riscos de seguretat", "Validació d'entrades", "Biblioteques criptogràfiques", "Mínim privilegi", "Analitzador estàtic de codi", "Aplicacions web", "Frameworks de Python", "Django", "Flask", "Sistema d'autenticació", "Hash de contrasenyes", "Sistema de plantilles", "Gestió de sessions", "MarkupSafe", "WTForms", "Blinker", "Protecció de dades", "Vulnerabilitats", "Codificació segura", "Python", "Riscos de seguretat", "Validació d'entrades", "Biblioteques criptogràfiques", "Mínim privilegi", "Analitzador estàtic de codi", "Aplicacions web", "Frameworks de Python", "Django", "Flask", "Sistema d'autenticació", "Hash de contrasenyes", "Sistema de plantilles", "Gestió de sessions", "MarkupSafe", "WTForms", "Blinker", "Protecció de dades", "Vulnerabilitats", "Seguretat del codi Python", "Revisió de codi", "Eines d'anàlisi estàtica", "Desenvolupament web segur", "Pràctiques de codificació segura", "Vulnerabilitats de seguretat", "Bones pràctiques de seguretat del codi", "Xifratge de dades", "Principi del mínim privilegi", "Anàlisi de codi", "Seguretat web"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.webp"
coverAlt: "Un escut de dibuixos animats amb la paraula Python per representar els estàndards de codificació segura"
coverCaption: ""
---
**Bones pràctiques dels estàndards de codificació segura en Python**

### 1. Valida les entrades

Les entrades de l'usuari sovint són una font important de riscos de seguretat. **La validació d'entrades** comprova que les dades introduïdes per l'usuari compleixen els criteris previstos i són segures per a l'aplicació.

Per exemple, quan l'usuari introdueix un número de targeta de crèdit, l'entrada només hauria de contenir dígits, sense caràcters especials. Els desenvolupadors poden validar-la amb funcions integrades com `isdigit()` o amb expressions regulars.

```python
import re

def validate_input(input_string):
    """
    Funció per validar l'entrada amb expressions regulars.
    """
    pattern = r"^[0-9]+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False
```

### 2. Evita les funcions insegures

Python inclou funcions que poden causar problemes de seguretat si no s'utilitzen amb cura. Funcions com `exec()`, `eval()` i `pickle` permeten que un atacant executi codi maliciós. Els desenvolupadors haurien **d'evitar-les** o fer-les servir amb cautela, limitant els paràmetres d'entrada i només quan calgui.

Per exemple, per convertir una cadena en un enter, fes servir `int()` en lloc de `eval()`.

```py
# En lloc de fer servir eval
x = eval('10')

# Fes servir int
x = int('10')
```

### 3. Fes servir biblioteques criptogràfiques

Les **biblioteques criptogràfiques**, com [cryptography](https://pypi.org/project/cryptography/) i [PyCryptodome](https://pypi.org/project/pycryptodome/), ofereixen una manera segura de xifrar i desxifrar. Fes-les servir en comptes de crear mètodes de xifratge propis, que poden tenir vulnerabilitats.

Per exemple, per xifrar una contrasenya, fes servir la biblioteca [cryptography](https://pypi.org/project/cryptography/) així:

```py
from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Funció per xifrar una contrasenya amb la biblioteca cryptography.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password

password = "contrasenyaExemple"
encrypted_password = encrypt_password(password)
```
L'objecte `Fernet` genera una clau que s'utilitza per xifrar la contrasenya amb el mètode `encrypt()`.

### 4. Segueix el principi del mínim privilegi

**El principi del mínim privilegi** limita els usuaris o processos als permisos mínims necessaris per fer la seva feina. Els desenvolupadors l'han de seguir per reduir l'impacte de les intrusions.

Per exemple, si una aplicació només necessita llegir una base de dades, fes servir un compte amb permisos de només lectura en lloc d'un compte amb permisos complets. Així es redueix el risc que un atacant modifiqui o esborri dades aprofitant l'aplicació.

### 5. Mantén actualitzats les biblioteques i els frameworks

Les biblioteques i els frameworks poden contenir vulnerabilitats que els atacants poden explotar. Els desenvolupadors haurien de **mantenir-los actualitzats** a l'última versió per evitar possibles problemes de seguretat.

Per exemple, si una biblioteca de tercers com [requests](https://pypi.org/project/requests/) té una vulnerabilitat, actualitza-la a una versió que la corregeixi.

### 6. Fes servir un analitzador estàtic de codi

**Un analitzador estàtic de codi** detecta possibles vulnerabilitats abans d'executar el programa. Fes servir eines com [Bandit](https://pypi.org/project/bandit/), [Pylint](https://pypi.org/project/pylint/) i [Pyflakes](https://pypi.org/project/pyflakes/) per trobar i corregir problemes abans del desplegament.

Per exemple, [Bandit](https://pypi.org/project/bandit/) examina el codi Python per trobar vulnerabilitats com contrasenyes incrustades al codi, injecció SQL i ús de funcions insegures.

### 7. Aplica pràctiques de codificació segura a les aplicacions web

Les aplicacions web estan exposades a riscos com els scripts entre llocs, la injecció SQL i la injecció d'ordres. Els desenvolupadors haurien **d'aplicar pràctiques de codificació segura**, com validar les entrades, codificar les sortides i fer servir consultes parametritzades.

Per exemple, en escriure consultes SQL, fes servir **consultes parametritzades** en lloc de concatenar-hi l'entrada de l'usuari. Així l'entrada es tracta com a dada, no com a codi executable, i es prevenen les injeccions SQL.

```py
# En lloc d'això
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Fes servir una consulta parametritzada
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
Els desenvolupadors també haurien **de validar totes les entrades**, codificar les sortides i fer servir HTTPS per xifrar les dades transmeses per la xarxa.

## Estàndards de codificació segura per als frameworks de Python

Frameworks de Python com [Django](https://www.djangoproject.com/) i [Flask](https://flask.palletsprojects.com/) tenen els seus propis estàndards de codificació segura. Cal seguir-los quan es desenvolupen aplicacions amb aquests frameworks. Aquests són alguns estàndards:

### 1. [Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) és un framework web popular per a Python. Per fer-lo servir de manera segura per a [Django](https://www.djangoproject.com/):

- Fes servir el **sistema d'autenticació** integrat de [Django](https://www.djangoproject.com/) en lloc de crear-ne un de propi.
- Fes servir les **funcions integrades de hash de contrasenyes** de [Django](https://www.djangoproject.com/) en comptes de crear mètodes propis.
- Fes servir el **sistema de plantilles** de [Django](https://www.djangoproject.com/) per protegir la sortida contra vulnerabilitats de scripts entre llocs.

Per exemple, per fer servir la funció integrada de hash de contrasenyes, importa `make_password()` del mòdul `django.contrib.auth.hashers` [Django](https://www.djangoproject.com/).

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "contrasenyaExemple"
hashed_password = make_password(password)
```

### 2. [Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) és un framework web lleuger per a Python. Segueix aquests estàndards [Flask](https://flask.palletsprojects.com/):

- Fes servir el **sistema integrat de gestió de sessions** de [Flask](https://flask.palletsprojects.com/) per gestionar-les de manera segura.
- Fes servir [Flask](https://flask.palletsprojects.com/) amb [MarkupSafe](https://pypi.org/project/MarkupSafe/) per protegir la sortida contra vulnerabilitats de scripts entre llocs.
- Fes servir [Flask](https://flask.palletsprojects.com/) amb [WTForms](https://pypi.org/project/WTForms/) per validar les entrades i reduir els riscos de seguretat.
- Fes servir [Flask](https://flask.palletsprojects.com/) amb [Blinker](https://pypi.org/project/blinker/) per gestionar els senyals de manera segura.

Per exemple, fes servir [Flask](https://flask.palletsprojects.com/) amb [MarkupSafe](https://pypi.org/project/MarkupSafe/) i fes-la servir per escapar les etiquetes HTML de la sortida.

```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hola, ' + escape(name)
```
______

## Com aplicar aquests coneixements i què fer ara?

1. **Comença avui a aplicar aquestes pràctiques al teu codi Python** per reduir el risc d'intrusions i protegir les dades sensibles. Identifica les àrees exposades, com la validació d'entrades, el hash de contrasenyes i la gestió de sessions. Després, valida les entrades amb les expressions regulars integrades de Python o fes servir una biblioteca segura de hash com [bcrypt](https://pypi.org/project/bcrypt/).

2. **Revisa el codi existent per detectar possibles vulnerabilitats** i fes servir analitzadors com [Bandit](https://pypi.org/project/bandit/), [Pylint](https://pypi.org/project/pylint/) i [Pyflakes](https://pypi.org/project/pyflakes/) per trobar-les i corregir-les. Una revisió manual també pot detectar problemes que aquestes eines no troben. Busca injecció SQL, scripts entre llocs i errors de validació d'entrades.

3. **Estigues al dia de les pràctiques i eines de seguretat**. Segueix blogs, assisteix a conferències i participa en comunitats en línia. Mantén actualitzats les biblioteques i els frameworks per fer servir versions segures recents.

4. **Uneix-te a comunitats en línia i assisteix a esdeveniments** per aprendre de desenvolupadors i experts en codificació segura per a Python. Participa en fòrums sobre seguretat, comparteix coneixements i assisteix a conferències, seminaris web i trobades.

5. **Comparteix aquestes pràctiques amb el teu equip o companys** per promoure la conscienciació sobre seguretat i animar-los a aplicar codificació segura als seus projectes Python. Organitza sessions de formació, comparteix recursos i dona exemple aplicant-les al teu codi.

## Conclusió

Els estàndards de codificació segura són essencials perquè el codi sigui segur, fiable i lliure de vulnerabilitats. Python és un llenguatge popular, i els desenvolupadors han de seguir aquests estàndards per prevenir riscos. Validar les entrades, evitar funcions insegures, fer servir biblioteques criptogràfiques i mantenir actualitzats les biblioteques i els frameworks ajuda a protegir el codi. Quan facis servir frameworks de Python, segueix els estàndards de seguretat que recomanen.

Adoptar aquests estàndards és un procés continu que exigeix estar al dia de les pràctiques i eines de seguretat. Integrar-los al procés de desenvolupament redueix el risc d'intrusions i protegeix les dades sensibles.
