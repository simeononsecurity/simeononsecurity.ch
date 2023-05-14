---
title: "Standard di codifica sicura per Python: Migliori pratiche"
date: 2023-02-26
toc: true
draft: false
description: "Imparate le migliori pratiche di codifica sicura in Python per ridurre al minimo il rischio di violazioni della sicurezza e proteggere i dati sensibili."
tags: ["Pitone", "Codifica sicura", "Rischi per la sicurezza", "Convalida dell'ingresso", "Librerie di crittografia", "Privilegio minimo", "Analizzatore di codice statico", "Applicazioni web", "Quadri Python", "Django", "Flash", "Sistema di autenticazione", "Hashing della password", "Sistema di template", "Gestione della sessione", "MarkupSafe", "WTForms", "Lampeggiante", "Protezione dei dati", "Vulnerabilità"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "Uno scudo a fumetti con la parola Python scritta sopra per rappresentare gli standard di codifica sicuri."
coverCaption: ""
---
 Pratiche per gli standard di codifica sicura in Python**

### 1. Convalida dell'input

### Convalida dell'ingresso

L'input dell'utente è spesso una fonte significativa di rischi per la sicurezza. La **convalida dell'input** è il processo di verifica che l'input dell'utente soddisfi i criteri previsti e sia sicuro da usare nell'applicazione.

Ad esempio, quando un utente inserisce un numero di carta di credito, l'input deve contenere solo cifre e nessun carattere speciale. Per convalidare l'input, gli sviluppatori possono utilizzare funzioni integrate come`isdigit()` o espressioni regolari per garantire che l'input soddisfi i criteri previsti.

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

### 2. Evitare l'uso di funzioni non sicure

Python ha diverse funzioni che possono essere vulnerabili a problemi di sicurezza se non vengono utilizzate con attenzione. Funzioni come`exec()` `eval()` e`pickle` possono consentire agli aggressori di eseguire codice dannoso. Gli sviluppatori dovrebbero **evitare l'uso di queste funzioni** o usarle con cautela, limitando i parametri di input e usandole solo quando necessario.

Per esempio, invece di usare`eval()` per convertire una stringa in un numero intero, gli sviluppatori dovrebbero utilizzare la funzione`int()` funzione.
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```

### 3. Utilizzare le librerie di crittografia

**Le librerie di crittografia**, come ad esempio[`cryptography`](https://pypi.org/project/cryptography/) and [`pycryptodome`](https://pypi.org/project/pycryptodome/) forniscono un modo sicuro per eseguire operazioni di crittografia e decrittografia. Utilizzate queste librerie invece di creare metodi di crittografia personalizzati, che potrebbero essere soggetti a vulnerabilità.

Ad esempio, per crittografare una password, si può usare la libreria[`cryptography`](https://pypi.org/project/cryptography/) come segue:
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
Il`Fernet` genera una chiave, che viene utilizzata per crittografare la password utilizzando il metodo`encrypt()` metodo.

### 4. Seguire il principio del minor privilegio

**Il principio del minimo privilegio** è una best practice di sicurezza che limita gli utenti o i processi al livello minimo di accesso necessario per svolgere le loro funzioni. Gli sviluppatori dovrebbero seguire questo principio quando scrivono il codice per ridurre al minimo l'impatto delle violazioni della sicurezza.

Ad esempio, se un'applicazione richiede l'accesso in sola lettura a un database, dovrebbe utilizzare un account del database con permessi di sola lettura invece di un account con permessi completi. In questo modo si riduce il rischio che un utente malintenzionato possa sfruttare l'applicazione per modificare o cancellare i dati.

### 5. Mantenere aggiornate le librerie e i framework

Le librerie e i framework possono contenere vulnerabilità di sicurezza che possono essere sfruttate dagli aggressori. Gli sviluppatori dovrebbero **mantenere le loro librerie e framework aggiornati** all'ultima versione per evitare potenziali problemi di sicurezza.

Ad esempio, se l'applicazione utilizza una libreria di terze parti, come ad esempio[`Requests`](https://pypi.org/project/requests/) che presenta una vulnerabilità di sicurezza, lo sviluppatore deve aggiornare alla versione più recente della libreria che risolve la vulnerabilità.

### 6. Utilizzare un analizzatore di codice statico

**Un analizzatore di codice statico** è uno strumento in grado di identificare potenziali vulnerabilità di sicurezza nel codice prima che venga eseguito. Utilizzate strumenti come[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) per individuare i problemi di sicurezza nel codice e risolverli prima della distribuzione.

Ad esempio,[`bandit`](https://pypi.org/project/bandit/) è un popolare analizzatore di codice statico che esamina il codice Python alla ricerca di potenziali vulnerabilità di sicurezza. È in grado di rilevare problemi come le password hard-coded, l'iniezione di SQL e l'uso di funzioni non sicure.

### 7. Utilizzare pratiche di codifica sicure per le applicazioni web

Le applicazioni Web sono vulnerabili a diversi rischi per la sicurezza, quali cross-site scripting, SQL injection e command injection. Gli sviluppatori devono **seguire pratiche di codifica sicure** come la convalida degli input, la codifica degli output e le query parametrizzate per garantire la sicurezza delle applicazioni web.

Ad esempio, quando si scrivono query SQL, utilizzare **query parametrizzate** invece di concatenare l'input dell'utente con la query. Le query parametrizzate prevengono gli attacchi di SQL injection trattando l'input dell'utente come dati e non come codice eseguibile.

```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
Gli sviluppatori dovrebbero anche **convalidare tutti gli input dell'utente**, codificare l'output e utilizzare HTTPS per criptare i dati trasmessi in rete.

## Standard di codifica sicura per i framework Python

I framework Python come[Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) hanno i loro standard di codifica sicura. Gli sviluppatori dovrebbero seguire questi standard quando sviluppano applicazioni utilizzando questi framework. Ecco alcuni standard di codifica sicura per i framework Python:

### 1.[Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a popular web framework for Python. Here are some secure coding standards for [Django](https://www.djangoproject.com/)

- Utilizzo[Django](https://www.djangoproject.com/) sistema di **autenticazione** integrato, invece di creare un sistema di autenticazione personalizzato.
- Utilizzare[Django](https://www.djangoproject.com/) funzioni di hashing delle password** integrate, invece di creare metodi di hashing delle password personalizzati.
- Utilizzare[Django](https://www.djangoproject.com/) **sistema di template** per garantire che l'output sia sicuro e privo di vulnerabilità di cross-site scripting.

Ad esempio, per utilizzare[Django](https://www.djangoproject.com/)'s built-in password hashing function, use the `make_password()` function from the ` modulo.

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```

### 2.[Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) is a micro web framework for Python. Here are some secure coding standards for [Flask](https://flask.palletsprojects.com/)

- Utilizzo[Flask](https://flask.palletsprojects.com/) sistema di gestione delle sessioni** integrato per garantire una gestione sicura delle sessioni.
- Utilizzo[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) per garantire che l'output sia sicuro e privo di vulnerabilità cross-site scripting.
- Utilizzo[Flask](https://flask.palletsprojects.com/)'s [`WTForms`](https://pypi.org/project/WTForms/) per gestire la convalida dell'input dell'utente e garantire che l'input sia privo di rischi per la sicurezza.
- Utilizzare[Flask](https://flask.palletsprojects.com/)'s [`Blinker`](https://pypi.org/project/blinker/) per la gestione sicura dei segnali.

Ad esempio, per utilizzare[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) importarla e usarla per eliminare i tag HTML dall'output.
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```
______

## Utilizzo delle conoscenze e cosa fare ora?

1. **Iniziate oggi stesso a implementare queste best practice nel vostro codice Python** per ridurre al minimo il rischio di violazioni della sicurezza e proteggere i dati sensibili. Potete iniziare identificando le aree del vostro codice che sono suscettibili di rischi per la sicurezza, come la validazione degli input, l'hashing delle password e la gestione delle sessioni. Per proteggere il vostro codice potete quindi implementare le migliori pratiche, come quelle discusse in questo articolo. Ad esempio, si possono usare le espressioni regolari integrate in Python per convalidare l'input dell'utente o utilizzare una libreria sicura per l'hashing delle password come[`bcrypt`](https://pypi.org/project/bcrypt/)

2. **Esaminare la base di codice esistente per individuare potenziali vulnerabilità di sicurezza** e utilizzare analizzatori di codice statici come[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) per individuare e risolvere eventuali problemi. È inoltre possibile utilizzare la revisione manuale del codice per identificare i problemi di sicurezza che gli analizzatori statici di codice potrebbero non rilevare. Cercate le vulnerabilità più comuni, come l'iniezione SQL, il cross-site scripting e i problemi di convalida degli input. Una volta identificate le potenziali vulnerabilità di sicurezza, è possibile utilizzare le best practice per risolvere i problemi.

3. **Rimanete aggiornati sulle migliori pratiche e sugli strumenti di sicurezza più recenti** per garantire che il vostro codice rimanga sicuro e privo di vulnerabilità. Seguite i blog sulla sicurezza, frequentate le conferenze e partecipate alle comunità online per rimanere aggiornati sulle ultime tendenze e pratiche di sicurezza. Mantenete aggiornate le librerie e i framework per assicurarvi di utilizzare le ultime versioni sicure.

4. **Partecipate alle comunità online e agli eventi** dove potete imparare da esperti e altri sviluppatori le pratiche di codifica sicura per Python. Cercate comunità e forum online dove potete discutere di problemi di sicurezza con altri sviluppatori, conoscere le nuove tendenze della sicurezza e condividere le vostre conoscenze. Partecipate a eventi come conferenze, webinar e meetup per imparare da esperti di sicurezza e altri sviluppatori.

5. **Condividete queste best practice con il vostro team o i vostri colleghi** per promuovere una cultura della sicurezza e incoraggiare gli altri ad adottare pratiche di codifica sicure nei loro progetti Python. Organizzate sessioni di formazione sulla sicurezza, condividete articoli e risorse sulle pratiche di codifica sicura e date l'esempio implementando queste best practice nel vostro codice. Promuovendo una cultura di consapevolezza della sicurezza, potete contribuire a garantire che il codice del vostro team sia sicuro e privo di vulnerabilità.


## Conclusione

Gli standard di codifica sicura sono essenziali per garantire che il codice sia sicuro, affidabile e privo di vulnerabilità. Python è un linguaggio di programmazione molto diffuso che richiede agli sviluppatori di seguire standard di codifica sicuri per prevenire i rischi di sicurezza. Seguendo le migliori pratiche, come la convalida degli input, evitando funzioni non sicure, utilizzando librerie di crittografia e mantenendo aggiornate librerie e framework, gli sviluppatori possono garantire che il loro codice sia sicuro e privo di vulnerabilità. Quando si utilizzano i framework Python, gli sviluppatori devono seguire gli standard di codifica sicura raccomandati dal framework.

L'adozione di standard di codifica sicuri è un processo continuo che richiede agli sviluppatori di rimanere aggiornati con le migliori pratiche e gli strumenti di sicurezza più recenti. Incorporando gli standard di codifica sicura nel processo di sviluppo, gli sviluppatori possono ridurre al minimo il rischio di violazioni della sicurezza e proteggere i dati sensibili.

