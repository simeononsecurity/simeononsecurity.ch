---
title: "Standarde de codare securizată pentru Python: Cele mai bune practici"
date: 2023-02-26
toc: true
draft: false
description: "Învățați cele mai bune practici de codare securizată în Python pentru a minimiza riscul de breșe de securitate și pentru a proteja datele sensibile."
tags: ["Python", "Codare securizată", "Riscuri de securitate", "Validarea intrărilor", "Biblioteci de criptografie", "Cel mai mic privilegiu", "Analizator de cod static", "Aplicații web", "Cadre Python", "Django", "Flash", "Sistem de autentificare", "Hashing de parole", "Sistem de șabloane", "Gestionarea sesiunii", "MarkupSafe", "WTForms", "Blinker", "Protecția datelor", "Vulnerabilități", "Codare securizată", "Python", "Riscuri de securitate", "Validarea intrărilor", "Biblioteci de criptografie", "Cel mai mic privilegiu", "Analizator de cod static", "Aplicații web", "Cadre Python", "Django", "Flash", "Sistem de autentificare", "Hashing de parole", "Sistem de șabloane", "Gestionarea sesiunii", "MarkupSafe", "WTForms", "Blinker", "Protecția datelor", "Vulnerabilități", "Securitatea codului Python", "Revizuirea codului", "Instrumente de analiză statică", "Dezvoltare web securizată", "Practici de codare securizată", "Vulnerabilități de securitate", "Cele mai bune practici de securitate a codului", "Criptarea datelor", "Principiul celui mai mic privilegiu", "Analiza codului", "Securitate web"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "Un scut de desen animat cu cuvântul Python scris pe el pentru a reprezenta standardele de codare sigură"
coverCaption: ""
---
 Practici pentru standarde de codare securizată în Python**

### 1. Validarea intrărilor

### Validarea intrărilor

Datele introduse de utilizator reprezintă adesea o sursă semnificativă de riscuri de securitate. **Validarea intrărilor** este procesul de verificare a faptului că datele introduse de utilizator îndeplinesc criteriile așteptate și că pot fi utilizate în siguranță în aplicație.

De exemplu, atunci când un utilizator introduce un număr de card de credit, datele introduse trebuie să conțină numai cifre și niciun caracter special. Pentru a valida datele de intrare, dezvoltatorii pot utiliza funcții încorporate, cum ar fi `isdigit()` sau expresii regulate pentru a se asigura că datele de intrare corespund criteriilor așteptate.

```python
import re

def validate_input(input_string):
    """
    Function to validate input using regular expressions.
    """
    pattern = r"^[0-9]+$"
    if re.match(pattern, input_string):
        return True
    else:
        return False
```

### 2. Evitați utilizarea funcțiilor nesigure

Python are mai multe funcții care pot fi vulnerabile la probleme de securitate dacă nu sunt utilizate cu atenție. Funcții precum `exec()` `eval()` și `pickle` poate permite atacatorilor să execute coduri malițioase. Dezvoltatorii ar trebui să **evitați utilizarea acestor funcții** sau să le utilizați cu prudență prin restricționarea parametrilor de intrare și prin utilizarea lor numai atunci când este necesar.

De exemplu, în loc de a utiliza `eval()` pentru a converti un șir de caractere într-un număr întreg, dezvoltatorii ar trebui să utilizeze funcția `int()` funcție.
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```

### 3. Utilizarea bibliotecilor de criptografie

**Bibliotecile de criptografie**, cum ar fi [`cryptography`](https://pypi.org/project/cryptography/) and [`pycryptodome`](https://pypi.org/project/pycryptodome/) oferă o modalitate sigură de a efectua operațiuni de criptare și decriptare. Utilizați aceste biblioteci în loc să creați metode de criptare personalizate, care pot fi predispuse la vulnerabilități.

De exemplu, pentru a cripta o parolă, utilizați bibliotecile [`cryptography`](https://pypi.org/project/cryptography/) bibliotecă, după cum urmează:
```py
from cryptography.fernet import Fernet

def encrypt_password(password):
    """
    Function to encrypt password using cryptography library.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password

password = "mypassword"
encrypted_password = encrypt_password(password)
```
The `Fernet` generează o cheie, care este utilizată pentru a cripta parola folosind protocolul `encrypt()` metoda.

### 4. Respectați principiul privilegiului cel mai mic

**Principiul celui mai mic privilegiu** este o bună practică de securitate care restricționează utilizatorii sau procesele la nivelul minim de acces necesar pentru a-și îndeplini funcțiile. Dezvoltatorii ar trebui să urmeze acest principiu atunci când scriu codul pentru a minimiza impactul încălcărilor de securitate.

De exemplu, dacă o aplicație necesită acces doar pentru citire la o bază de date, ar trebui să utilizeze un cont de bază de date cu permisiuni de doar citire în loc de un cont cu permisiuni complete. Acest lucru reduce riscul ca un atacator să exploateze aplicația pentru a modifica sau șterge date.

### 5. Păstrați bibliotecile și cadrele actualizate

Bibliotecile și cadrele pot conține vulnerabilități de securitate care pot fi exploatate de atacatori. Dezvoltatorii ar trebui să **păstreze bibliotecile și cadrele de lucru actualizate** la cea mai recentă versiune pentru a evita eventualele probleme de securitate.

De exemplu, dacă aplicația utilizează o bibliotecă terță parte, cum ar fi [`Requests`](https://pypi.org/project/requests/) care prezintă o vulnerabilitate de securitate, dezvoltatorul ar trebui să actualizeze la cea mai recentă versiune a bibliotecii care rezolvă vulnerabilitatea.

### 6. Utilizați un analizor de cod static

**Un analizor de cod static** este un instrument care poate identifica potențiale vulnerabilități de securitate în cod înainte ca acesta să fie executat. Utilizați instrumente precum [`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) pentru a detecta problemele de securitate din cod și a le remedia înainte de implementare.

De exemplu, [`bandit`](https://pypi.org/project/bandit/) este un popular analizor de cod static care examinează codul Python pentru a detecta potențiale vulnerabilități de securitate. Acesta poate detecta probleme precum parolele codate în mod greșit, injectarea SQL și utilizarea de funcții nesigure.

### 7. Utilizați practici de codare securizată pentru aplicațiile web

Aplicațiile web sunt vulnerabile la mai multe riscuri de securitate, cum ar fi scriptingul cross-site, injecția SQL și injecția de comenzi. Dezvoltatorii ar trebui să **folosească practici de codare sigură**, cum ar fi validarea intrărilor, codificarea ieșirilor și interogările parametrizate pentru a se asigura că aplicațiile web sunt sigure.

De exemplu, atunci când scrieți interogări SQL, utilizați **interogări parametrizate** în loc să concatenați datele de intrare ale utilizatorului cu interogarea. Interogările parametrizate previn atacurile de injecție SQL prin tratarea datelor introduse de utilizator ca date și nu ca cod executabil.

```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
De asemenea, dezvoltatorii ar trebui să **valideze toate datele introduse de utilizatori**, să codifice datele de ieșire și să utilizeze HTTPS pentru a cripta datele transmise prin rețea.

## Standarde de codare securizată pentru cadrele Python

Cadrele Python, cum ar fi [Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) au standardele lor de codare sigură. Dezvoltatorii ar trebui să respecte aceste standarde atunci când dezvoltă aplicații utilizând aceste cadre. Iată câteva standarde de codare sigură pentru cadrele Python:

### 1. [Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a popular web framework for Python. Here are some secure coding standards for [Django](https://www.djangoproject.com/)

- Utilizare [Django](https://www.djangoproject.com/) built-in **sistem de autentificare** în loc să creați un sistem de autentificare personalizat.
- Utilizați [Django](https://www.djangoproject.com/) funcțiile încorporate **funcții de hașurare a parolelor** în loc să creați metode personalizate de hașurare a parolelor.
- Utilizați [Django](https://www.djangoproject.com/) **sistemul de modele** pentru a se asigura că rezultatul este sigur și fără vulnerabilități de scripting cross-site.

De exemplu, pentru a utiliza [Django](https://www.djangoproject.com/)'s built-in password hashing function, use the `make_password()` function from the ` modul.

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```

### 2. [Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) is a micro web framework for Python. Here are some secure coding standards for [Flask](https://flask.palletsprojects.com/)

- Utilizare [Flask](https://flask.palletsprojects.com/) **sistem de gestionare a sesiunilor** încorporat pentru a asigura gestionarea securizată a sesiunilor.
- Utilizați [Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) pentru a se asigura că rezultatul este sigur și nu prezintă vulnerabilități de scripting cross-site.
- Utilizați [Flask](https://flask.palletsprojects.com/)'s [`WTForms`](https://pypi.org/project/WTForms/) pentru a gestiona validarea intrărilor utilizatorilor și pentru a se asigura că acestea nu prezintă riscuri de securitate.
- Utilizați [Flask](https://flask.palletsprojects.com/)'s [`Blinker`](https://pypi.org/project/blinker/) pentru gestionarea sigură a semnalelor.

De exemplu, pentru a utiliza [Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) importați-o și folosiți-o pentru a scăpa etichetele HTML de la ieșire.
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```
______

## Utilizarea cunoștințelor și ce trebuie să faceți acum?

1. **Începeți să implementați de astăzi aceste bune practici în codul dvs. Python** pentru a minimiza riscul de breșe de securitate și pentru a proteja datele sensibile. Puteți începe prin a identifica zonele din codul dvs. care sunt susceptibile la riscuri de securitate, cum ar fi validarea intrărilor, hashing-ul parolei și gestionarea sesiunilor. Apoi puteți implementa cele mai bune practici, precum cele discutate în acest articol, pentru a vă securiza codul. De exemplu, puteți utiliza expresiile regulate încorporate în Python pentru a valida datele introduse de utilizator sau puteți utiliza o bibliotecă de hashing securizată pentru parole, cum ar fi [`bcrypt`](https://pypi.org/project/bcrypt/)

2. **Revizuiți baza de cod existentă pentru a găsi potențiale vulnerabilități de securitate** și utilizați analizatori de cod static, cum ar fi [`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) pentru a detecta și a remedia orice problemă. De asemenea, puteți utiliza revizuirea manuală a codului pentru a identifica problemele de securitate pe care analizatorii de cod static nu le pot detecta. Căutați vulnerabilitățile comune, cum ar fi injecția SQL, scriptingul cross-site și problemele de validare a intrărilor. Odată ce ați identificat potențialele vulnerabilități de securitate, puteți utiliza cele mai bune practici pentru a remedia problemele.

3. ** Rămâneți la curent cu cele mai recente bune practici și instrumente de securitate** pentru a vă asigura că codul dvs. rămâne sigur și lipsit de vulnerabilități. Urmăriți blogurile de securitate, participați la conferințe și participați la comunități online pentru a fi la curent cu cele mai recente tendințe și practici de securitate. Păstrați bibliotecile și cadrele de lucru actualizate pentru a vă asigura că utilizați cele mai recente versiuni sigure.

4. **Inscrieți-vă în comunitățile online și participați la evenimente** unde puteți învăța de la experți și de la alți dezvoltatori despre practicile de codare securizată pentru Python. Căutați comunități și forumuri online unde puteți discuta probleme de securitate cu alți dezvoltatori, puteți afla despre noile tendințe în materie de securitate și vă puteți împărtăși propriile cunoștințe. Participați la evenimente precum conferințe, seminarii web și întâlniri pentru a învăța de la experți în securitate și de la alți dezvoltatori.

5. **Părtășiți aceste bune practici cu echipa sau cu colegii dvs. pentru a promova o cultură a conștientizării securității și pentru a-i încuraja pe alții să adopte practici de codare sigure în proiectele lor Python. Organizați sesiuni de formare în domeniul securității, partajați articole și resurse privind practicile de codare sigură și dați un exemplu prin implementarea acestor bune practici în propriul cod. Prin promovarea unei culturi de conștientizare a securității, puteți contribui la asigurarea faptului că codul echipei dvs. este sigur și lipsit de vulnerabilități.


## Concluzie

Standardele de codare securizată sunt esențiale pentru a garanta că codul este sigur, fiabil și lipsit de vulnerabilități. Python este un limbaj de programare popular care impune dezvoltatorilor să respecte standardele de codare sigură pentru a preveni riscurile de securitate. Urmând cele mai bune practici, cum ar fi validarea intrărilor, evitarea funcțiilor nesigure, utilizarea bibliotecilor de criptografie și actualizarea bibliotecilor și a cadrelor, dezvoltatorii se pot asigura că codul lor este sigur și lipsit de vulnerabilități. Atunci când utilizează cadre Python, dezvoltatorii ar trebui să respecte standardele de codare securizată recomandate de cadrul respectiv.

Adoptarea standardelor de codare sigură este un proces continuu care necesită ca dezvoltatorii să rămână la curent cu cele mai recente bune practici și instrumente de securitate. Prin încorporarea standardelor de codare securizată în procesul de dezvoltare, dezvoltatorii pot minimiza riscul de breșe de securitate și pot proteja datele sensibile.

