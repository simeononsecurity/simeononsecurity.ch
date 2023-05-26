---
title: "Kompletny przewodnik: Skróty plików w systemie Windows przy użyciu PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Dowiedz się, jak uzyskać skróty plików w systemie Windows za pomocą PowerShell, w tym SHA256, MD5 i SHA1, z instrukcjami krok po kroku i przykładami."
tags: ["skróty plików", "PowerShell", "SHA256 hash", "Skrót MD5", "SHA1 hash", "integralność plików", "uwierzytelnianie danych", "weryfikacja plików", "algorytmy haszujące", "System operacyjny Windows", "język skryptowy", "powłoka wiersza poleceń", "bezpieczeństwo danych", "informatyka śledcza", "cyberbezpieczeństwo", "Obliczanie skrótu", "manipulowanie plikami", "integralność danych", "autentyczność pliku", "Bezpieczeństwo systemu Windows", "identyfikacja pliku", "cyberobrona", "bezpieczeństwo plików", "ochrona danych", "weryfikacja danych", "walidacja plików", "Windows PowerShell", "generowanie skrótu", "algorytmy skrótu", "funkcje skrótu"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Ilustracja rysunkowa przedstawiająca plik z symbolem kłódki i lupą, reprezentująca weryfikację skrótu pliku i bezpieczeństwo."
coverCaption: ""
---

**Jak uzyskać skróty plików w systemie Windows za pomocą PowerShell**

W dziedzinie bezpieczeństwa komputerowego uzyskiwanie skrótów plików jest kluczowym krokiem w zapewnianiu integralności danych i weryfikacji autentyczności plików. Hasła są unikalnymi identyfikatorami generowanymi dla plików, umożliwiającymi użytkownikom wykrywanie prób manipulacji i sprawdzanie integralności danych. W tym kompleksowym przewodniku zbadamy proces uzyskiwania **SHA256**, **MD5** i **SHA1** hashy plików w systemie Windows przy użyciu potężnego języka skryptowego **PowerShell**. Postępuj zgodnie z instrukcjami krok po kroku i zapoznaj się z konkretnymi przykładami. Zaczynajmy!

______

## Uzyskiwanie hashy w systemie Windows przy użyciu PowerShell

PowerShell, wszechstronny język skryptowy i powłoka wiersza poleceń dla systemu Windows, oferuje polecenie cmdlet **Get-FileHash**, umożliwiające użytkownikom łatwe obliczanie skrótu pliku.

### Uzyskiwanie skrótu SHA256

Aby uzyskać **SHA256 hash** pliku za pomocą PowerShell, wykonaj następujące proste kroki:

1. Uruchom PowerShell, otwierając **Menu Start**, wyszukując **PowerShell** i wybierając **Windows PowerShell**.
2. Przejdź do katalogu, w którym znajduje się plik. Użyj `cd` po którym następuje ścieżka do katalogu.
3. Wykonaj następujące polecenie, aby uzyskać skrót SHA256 pliku:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Uzyskiwanie skrótów MD5 i SHA1
Można również uzyskać `MD5` oraz `SHA1` skróty pliku przy użyciu PowerShell. Wykorzystaj następujące polecenia:

- Aby uzyskać `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Aby uzyskać `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Pamiętaj, aby zastąpić "file_path" ścieżką do pliku w obu poleceniach.

## Przykłady
Przejdźmy do konkretnych przykładów, aby zilustrować proces uzyskiwania hashy za pomocą PowerShell w systemie Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Przykład 1: Uzyskiwanie skrótu SHA256
Wyobraź sobie, że masz plik o nazwie `document.pdf` znajdujący się w katalogu `C:\Files` Aby uzyskać `SHA256 hash` tego pliku za pomocą PowerShell, wykonaj następujące polecenie:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

Na wyjściu zostanie wyświetlona wartość skrótu SHA256 pliku.

### Przykład 2: Uzyskiwanie skrótu MD5

Załóżmy, że posiadasz plik o nazwie `image.jpg` przechowywane w katalogu `C:\Photos` Aby uzyskać `MD5 hash` tego pliku za pomocą PowerShell, uruchom następujące polecenie:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

Terminal wyświetli wartość skrótu MD5 pliku.

### Przykład 3: Uzyskanie skrótu SHA1

Rozważmy scenariusz, w którym masz plik o nazwie `data.txt` znajdujący się w katalogu `C:\Documents` Aby uzyskać `SHA1 hash` tego pliku za pomocą PowerShell, wykonaj następujące polecenie:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

Na wyjściu zostanie wyświetlona wartość skrótu SHA1 pliku.