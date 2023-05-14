---
title: "Standardy bezpiecznego kodowania dla Pythona: Najlepsze praktyki"
date: 2023-02-26
toc: true
draft: false
description: "Poznaj najlepsze praktyki bezpiecznego kodowania w Pythonie, aby zminimalizować ryzyko naruszenia bezpieczeństwa i chronić wrażliwe dane."
tags: ["Python", "Bezpieczne kodowanie", "Zagrożenia bezpieczeństwa", "Walidacja wejścia", "Biblioteki kryptograficzne", "Najmniejszy przywilej", "Statyczny analizator kodu", "Aplikacje internetowe", "Struktury Pythona", "Django", "Flash", "System uwierzytelniania", "Haszowanie hasła", "System szablonów", "Zarządzanie sesją", "MarkupSafe", "WTForms", "Blinker", "Ochrona danych", "Podatności"]
cover: "/img/cover/A_cartoon_shield_with_the_word_Python.png"
coverAlt: "Kreskówkowa tarcza z napisem Python, reprezentująca bezpieczne standardy kodowania"
coverCaption: ""
---
 Praktyki dotyczące standardów bezpiecznego kodowania w Pythonie**.

### 1. Walidacja wejść

### Walidacja wejść

Dane wejściowe użytkownika są często istotnym źródłem zagrożeń bezpieczeństwa. **Weryfikacja wejścia** to proces sprawdzania, czy dane wejściowe użytkownika spełniają oczekiwane kryteria i są bezpieczne do użycia w aplikacji.

Na przykład, kiedy użytkownik wprowadza numer karty kredytowej, dane wejściowe powinny zawierać tylko cyfry i żadnych znaków specjalnych. Aby sprawdzić poprawność danych wejściowych, programiści mogą użyć wbudowanych funkcji, takich jak`isdigit()` lub wyrażeń regularnych, aby upewnić się, że dane wejściowe spełniają oczekiwane kryteria.

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

### 2. Unikaj używania niebezpiecznych funkcji

Python posiada kilka funkcji, które mogą być podatne na problemy bezpieczeństwa, jeśli nie są używane ostrożnie. Funkcje takie jak`exec()` `eval()` oraz`pickle` może pozwolić atakującym na wykonanie złośliwego kodu. Programiści powinni **uniknąć używania tych funkcji** lub używać ich z ostrożnością, ograniczając parametry wejściowe i używając ich tylko w razie potrzeby.

Na przykład, zamiast używać`eval()` aby przekonwertować ciąg znaków na liczbę całkowitą, programiści powinni użyć funkcji`int()` funkcja.
```py
# Instead of using eval function
x = eval('10')

# Use int function
x = int('10')
```

### 3. Używanie bibliotek kryptograficznych

**Biblioteki kryptograficzne** takie jak np.[`cryptography`](https://pypi.org/project/cryptography/) and [`pycryptodome`](https://pypi.org/project/pycryptodome/) zapewniają bezpieczny sposób wykonywania operacji szyfrowania i deszyfrowania. Użyj tych bibliotek zamiast tworzenia własnych metod szyfrowania, które mogą być podatne na luki.

Na przykład, aby zaszyfrować hasło, należy użyć biblioteki[`cryptography`](https://pypi.org/project/cryptography/) biblioteka w następujący sposób:
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
Na stronie`Fernet` Obiekt generuje klucz, który służy do zaszyfrowania hasła za pomocą`encrypt()` metoda.

### 4. Postępuj zgodnie z zasadą najmniejszego przywileju

**Zasada najmniejszego przywileju** jest najlepszą praktyką bezpieczeństwa, która ogranicza użytkowników lub procesy do minimalnego poziomu dostępu niezbędnego do wykonywania ich funkcji. Programiści powinni przestrzegać tej zasady podczas pisania kodu, aby zminimalizować wpływ naruszenia bezpieczeństwa.

Na przykład, jeśli aplikacja wymaga dostępu tylko do odczytu do bazy danych, powinna używać konta bazy danych z uprawnieniami tylko do odczytu zamiast konta z pełnymi uprawnieniami. Zmniejsza to ryzyko wykorzystania aplikacji przez napastnika do modyfikacji lub usunięcia danych.

### 5. Aktualizuj biblioteki i frameworki

Biblioteki i frameworki mogą zawierać luki bezpieczeństwa, które mogą być wykorzystane przez napastników. Deweloperzy powinni **utrzymywać swoje biblioteki i frameworki zaktualizowane** do najnowszej wersji, aby uniknąć potencjalnych problemów z bezpieczeństwem.

Na przykład, jeśli aplikacja używa biblioteki innej firmy, takiej jak[`Requests`](https://pypi.org/project/requests/) która posiada lukę w zabezpieczeniach, programista powinien zaktualizować ją do najnowszej wersji biblioteki, która likwiduje tę lukę.

### 6. Używaj statycznego analizatora kodu

**Statystyczny analizator kodu** to narzędzie, które może zidentyfikować potencjalne luki bezpieczeństwa w kodzie, zanim zostanie on wykonany. Należy używać takich narzędzi jak np.[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) aby wykryć błędy bezpieczeństwa w kodzie i naprawić je przed wdrożeniem.

Na przykład,[`bandit`](https://pypi.org/project/bandit/) jest popularnym statycznym analizatorem kodu, który bada kod Pythona pod kątem potencjalnych luk bezpieczeństwa. Potrafi wykryć takie problemy, jak twardo zakodowane hasła, wstrzykiwanie kodu SQL i używanie niebezpiecznych funkcji.

### 7. Używaj bezpiecznych praktyk kodowania dla aplikacji internetowych

Aplikacje internetowe są podatne na kilka zagrożeń bezpieczeństwa, takich jak cross-site scripting, SQL injection i command injection. Programiści powinni **stosować bezpieczne praktyki kodowania**, takie jak walidacja danych wejściowych, kodowanie danych wyjściowych i parametryzowane zapytania, aby zapewnić bezpieczeństwo aplikacji internetowych.

Na przykład, podczas pisania zapytań SQL, używaj **parametrycznych zapytań** zamiast konkatenacji danych wejściowych użytkownika z zapytaniem. Zapytania parametryzowane zapobiegają atakom typu SQL injection poprzez traktowanie danych wejściowych użytkownika jako danych, a nie kodu wykonywalnego.

```py
# Instead of this
query = "SELECT * FROM users WHERE username = '" + username + "';"

# Use parameterized query
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))
```
Programiści powinni również **walidować wszystkie dane wejściowe użytkownika**, kodować dane wyjściowe i używać HTTPS do szyfrowania danych przesyłanych przez sieć.

## Standardy bezpiecznego kodowania dla frameworków Pythona

Frameworki Pythona, takie jak np.[Django](https://www.djangoproject.com/) and [Flask](https://flask.palletsprojects.com/) mają swoje standardy bezpiecznego kodowania. Deweloperzy powinni przestrzegać tych standardów podczas tworzenia aplikacji wykorzystujących te frameworki. Oto kilka standardów bezpiecznego kodowania dla frameworków Pythona:

### 1.[Django](https://www.djangoproject.com/)

[Django](https://www.djangoproject.com/) is a popular web framework for Python. Here are some secure coding standards for [Django](https://www.djangoproject.com/)

- Zastosowanie[Django](https://www.djangoproject.com/) wbudowany **system uwierzytelniania** zamiast tworzenia niestandardowego systemu uwierzytelniania.
- Użycie[Django](https://www.djangoproject.com/) wbudowane **funkcje haszowania haseł** zamiast tworzenia niestandardowych metod haszowania haseł.
- Użycie[Django](https://www.djangoproject.com/) **systemu szablonów**, aby zapewnić, że dane wyjściowe są bezpieczne i wolne od podatności na cross-site scripting.

Na przykład, aby użyć[Django](https://www.djangoproject.com/)'s built-in password hashing function, use the `make_password()` function from the ` moduł.

```python
from [Django](https://www.djangoproject.com/).contrib.auth.hashers import make_password

password = "mypassword"
hashed_password = make_password(password)
```

### 2.[Flask](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/) is a micro web framework for Python. Here are some secure coding standards for [Flask](https://flask.palletsprojects.com/)

- Zastosowanie[Flask](https://flask.palletsprojects.com/) wbudowany **system zarządzania sesjami** zapewniający bezpieczną obsługę sesji.
- Zastosowanie[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) aby zapewnić, że dane wyjściowe są bezpieczne i wolne od podatności na cross-site scripting.
- Użycie[Flask](https://flask.palletsprojects.com/)'s [`WTForms`](https://pypi.org/project/WTForms/) biblioteka do obsługi walidacji danych wejściowych użytkownika i zapewnienia, że dane wejściowe są wolne od zagrożeń bezpieczeństwa.
- Użycie[Flask](https://flask.palletsprojects.com/)'s [`Blinker`](https://pypi.org/project/blinker/) biblioteka do bezpiecznej obsługi sygnałów.

Na przykład, aby użyć[Flask](https://flask.palletsprojects.com/)'s [`MarkupSafe`](https://pypi.org/project/MarkupSafe/) zaimportuj ją i użyj do ucieczki znaczników HTML z wyjścia.
```py
from markupsafe import escape

@app.route('/')
def hello():
    name = "<script>alert('xss');</script>"
    return 'Hello, ' + escape(name)
```
______

## Wykorzystanie wiedzy i co teraz zrobić?

1. **Zacznij już dziś wdrażać te najlepsze praktyki w swoim kodzie Pythona**, aby zminimalizować ryzyko naruszenia bezpieczeństwa i chronić wrażliwe dane. Możesz zacząć od zidentyfikowania obszarów w swoim kodzie, które są podatne na zagrożenia bezpieczeństwa, takich jak walidacja danych wejściowych, haszowanie haseł i zarządzanie sesjami. Następnie można wdrożyć najlepsze praktyki, takie jak te omówione w tym artykule, aby zabezpieczyć swój kod. Na przykład można użyć wbudowanych w Pythona wyrażeń regularnych do sprawdzania poprawności danych wejściowych użytkownika lub użyć bezpiecznej biblioteki do haszowania haseł, takiej jak[`bcrypt`](https://pypi.org/project/bcrypt/)

2. **Przejrzyj istniejącą bazę kodu pod kątem potencjalnych luk bezpieczeństwa** i użyj statycznych analizatorów kodu, np.[`bandit`](https://pypi.org/project/bandit/), [`Pylint`](https://pypi.org/project/pylint/), and [`Pyflakes`](https://pypi.org/project/pyflakes/) aby wykryć i naprawić wszelkie problemy. Możesz również użyć ręcznego przeglądu kodu, aby zidentyfikować problemy bezpieczeństwa, których statyczne analizatory kodu mogą nie wykryć. Szukaj typowych błędów, takich jak wstrzykiwanie kodu SQL, cross-site scripting oraz błędy walidacji danych wejściowych. Po zidentyfikowaniu potencjalnych luk w bezpieczeństwie, możesz użyć najlepszych praktyk, aby je naprawić.

3. **Bądź na bieżąco z najnowszymi najlepszymi praktykami i narzędziami bezpieczeństwa**, aby mieć pewność, że Twój kod pozostanie bezpieczny i wolny od luk. Śledź blogi o bezpieczeństwie, bierz udział w konferencjach i uczestnicz w społecznościach internetowych, aby być na bieżąco z najnowszymi trendami i praktykami bezpieczeństwa. Aktualizuj swoje biblioteki i frameworki, aby mieć pewność, że używasz najnowszych bezpiecznych wersji.

4. **Dołącz do społeczności internetowych i bierz udział w wydarzeniach**, gdzie możesz uczyć się od ekspertów i innych programistów na temat bezpiecznych praktyk kodowania w Pythonie. Poszukaj społeczności internetowych i forów, na których możesz omawiać kwestie bezpieczeństwa z innymi programistami, poznawać nowe trendy w dziedzinie bezpieczeństwa i dzielić się własną wiedzą. Uczestnicz w wydarzeniach takich jak konferencje, webinaria i spotkania, aby uczyć się od ekspertów ds. bezpieczeństwa i innych programistów.

5. **Podziel się tymi najlepszymi praktykami ze swoim zespołem lub kolegami**, aby promować kulturę świadomości bezpieczeństwa i zachęcić innych do przyjęcia bezpiecznych praktyk kodowania w swoich projektach Python. Organizuj sesje szkoleniowe z zakresu bezpieczeństwa, udostępniaj artykuły i zasoby dotyczące praktyk bezpiecznego kodowania i dawaj przykład, wdrażając te najlepsze praktyki w swoim własnym kodzie. Promując kulturę świadomości bezpieczeństwa, możesz pomóc zapewnić, że kod Twojego zespołu jest bezpieczny i wolny od luk.


## Zakończenie

Standardy bezpiecznego kodowania są niezbędne do zapewnienia, że kod jest bezpieczny, niezawodny i wolny od podatności. Python jest popularnym językiem programowania, który wymaga od programistów przestrzegania standardów bezpiecznego kodowania, aby zapobiec zagrożeniom bezpieczeństwa. Poprzez stosowanie najlepszych praktyk, takich jak sprawdzanie poprawności danych wejściowych, unikanie niebezpiecznych funkcji, używanie bibliotek kryptograficznych oraz utrzymywanie bibliotek i frameworków w stanie aktualnym, programiści mogą zapewnić, że ich kod jest bezpieczny i wolny od luk. Podczas korzystania z frameworków Pythona, programiści powinni przestrzegać standardów bezpiecznego kodowania zalecanych przez dany framework.

Przyjmowanie standardów bezpiecznego kodowania jest procesem ciągłym, który wymaga od programistów bycia na bieżąco z najnowszymi najlepszymi praktykami i narzędziami bezpieczeństwa. Włączając standardy bezpiecznego kodowania do procesu rozwoju, programiści mogą zminimalizować ryzyko naruszenia bezpieczeństwa i chronić wrażliwe dane.

