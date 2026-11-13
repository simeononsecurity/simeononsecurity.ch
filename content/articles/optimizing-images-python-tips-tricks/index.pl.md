---
title: "Optymalizacja obrazów za pomocą Pythona"
date: 2023-07-04
lastmod: 2026-11-13
toc: true
draft: false
description: "Optymalizuj obrazy w Pythonie przez zmianę rozmiaru, kompresję i konwersję formatów w powtarzalnych procesach Pillow."
genre: ["Technologia", "Tworzenie stron internetowych", "Programowanie w Pythonie", "Optymalizacja obrazów", "SEO", "Wydajność witryn", "Doświadczenie użytkownika", "Tworzenie oprogramowania", "Automatyzacja", "Programowanie"]
tags: ["optymalizacja obrazów", "Python", "optymalizacja grafiki", "tworzenie stron internetowych", "wydajność witryny", "doświadczenie użytkownika", "kompresja", "zmiana rozmiaru", "konwersja formatu", "przetwarzanie obrazów", "biblioteka Pillow", "biblioteka Tinify", "automatyzacja", "skrypt Python", "optymalizacja wydajności witryn", "optymalizacja SEO", "tworzenie oprogramowania", "projektowanie stron", "kompresja obrazów", "zmniejszanie rozmiaru plików", "leniwe ładowanie", "formaty obrazów", "format WebP", "integracja API", "proces tworzenia", "przykład kodu", "techniki optymalizacji obrazów", "optymalizacja wydajności", "samouczek programowania"]
cover: "/img/cover/An_illustration_of_a_Python_script_optimizing.webp"
coverAlt: "Ilustracja skryptu Python optymalizującego obrazy; lupa pokazuje skompresowany obraz."
coverCaption: "Zmieniaj rozmiar, kompresuj i ulepszaj obrazy za pomocą Pythona."
---

**Wprowadzenie**

Rozmiar plików graficznych wpływa na szybkość witryny i wygodę odwiedzających. Duże pliki wydłużają ładowanie strony i mogą skłaniać użytkowników do jej opuszczenia. **Python** i biblioteka Pillow pomagają zmniejszać pliki i poprawiać sposób wyświetlania obrazów w sieci. W tym artykule przedstawiono praktyczne metody i narzędzia **optymalizacji obrazów** w Pythonie.

______

## Dlaczego optymalizacja obrazów ma znaczenie

**Optymalizacja** zmniejsza rozmiar plików bez widocznego pogorszenia jakości obrazu. Przynosi kilka korzyści:

1. **Strony ładują się szybciej**: duże pliki graficzne spowalniają witrynę i wpływają na SEO oraz doświadczenie użytkownika.

2. **Mniejsze zużycie przepustowości**: zoptymalizowane obrazy przesyłają mniej danych, więc witryna działa lepiej przy ograniczonym połączeniu.

3. **Lepsze działanie na urządzeniach mobilnych**: połączenia mobilne bywają wolniejsze. Optymalizacja pomaga płynnie wyświetlać strony na telefonach i tabletach.

4. **Wsparcie dla SEO**: wyszukiwarki uwzględniają szybkość witryny przy ustalaniu pozycji. Szybkie strony mogą zajmować wyższe miejsca w wynikach.

______

## Techniki optymalizacji obrazów

### **1. Kompresja obrazów**

Kompresja zmniejsza rozmiar pliku. Biblioteka Python **Pillow** udostępnia metody i ustawienia, które pomagają zachować równowagę między rozmiarem pliku a jakością obrazu. Zainstaluj Pillow za pomocą pip:

```python
pip install Pillow
```

Przykład kompresji obrazu:

```python
from PIL import Image

# Otwórz obraz
image = Image.open("input_image.jpg")

# Skompresuj i zapisz obraz
image.save("compressed_image.jpg", optimize=True, quality=85)
```

### **2. Zmiana rozmiaru obrazów**

Dopasuj wymiary obrazu do miejsca, w którym będzie wyświetlany. Duży obraz zmniejszony przez HTML lub CSS nadal może spowalniać stronę, ponieważ przeglądarka pobiera cały plik. Pillow ułatwia zmianę rozmiaru:

```python
from PIL import Image

# Otwórz obraz
image = Image.open("input_image.jpg")

# Zmień rozmiar obrazu
resized_image = image.resize((800, 600))

# Zapisz obraz po zmianie rozmiaru
resized_image.save("resized_image.jpg")
```

### **3. Konwersja formatu obrazu**

Konwersja do wydajniejszych formatów, takich jak WebP, zmniejsza plik przy zachowaniu odpowiedniej jakości. Większość nowoczesnych przeglądarek obsługuje WebP, a Pillow pozwala zapisywać obrazy w tym formacie:

```python
from PIL import Image

# Otwórz obraz
image = Image.open("input_image.jpg")

# Konwertuj obraz do formatu WebP
image.save("output_image.webp")
```

## Automatyzacja optymalizacji obrazów w Pythonie


### Przykład skryptu Python: użycie API TinyPNG

Automatyzacja oszczędza czas i pracę, gdy trzeba przetworzyć wiele obrazów. Biblioteki Pythona pozwalają zautomatyzować te zadania. Tinify to wrapper Pythona dla API TinyPNG.

Tinify kompresuje i optymalizuje obrazy za pomocą zaawansowanych algorytmów, zmniejszając pliki bez utraty jakości. Aby go użyć, załóż konto w serwisie Tinify i uzyskaj klucz API.

Przykład kompresji obrazu za pomocą **Tinify**:

```python
import tinify

# Skonfiguruj Tinify za pomocą klucza API
tinify.key = "YOUR_API_KEY"

# Skompresuj obraz
source = tinify.from_file("input_image.jpg")
source.to_file("compressed_image.jpg")
```

### Przykład skryptu Python: optymalizacja obrazów w folderze

Poniższy skrypt obsługuje różne typy obrazów, takie jak JPEG i PNG, a następnie eksportuje zoptymalizowane pliki WebP:

```python
import os
from PIL import Image

# Funkcja konwertująca obraz do formatu WebP
def convert_to_webp(input_path, output_path, quality=85):
    image = Image.open(input_path)
    image = image.convert("RGB")
    image.save(output_path, "webp", optimize=True, quality=quality)

# Funkcja iterująca po obrazach w folderze i konwertująca je do WebP
def optimize_images(folder_path, output_folder, quality=85):
    # Utwórz folder wyjściowy, jeśli nie istnieje
    os.makedirs(output_folder, exist_ok=True)
    
    # Iteruj po każdym pliku w folderze
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Utwórz ścieżki wejściowe i wyjściowe
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Konwertuj obraz do formatu WebP
            convert_to_webp(input_path, output_path, quality=quality)

# Przykład użycia
folder_path = "input_images"
output_folder = "optimized_images"
optimize_images(folder_path, output_folder, quality=80)
```

Przykład używa Python Imaging Library (PIL) do otwierania obrazów i konwersji do WebP. Funkcja `convert_to_webp` otrzymuje ścieżkę wejściową, ścieżkę wyjściową oraz opcjonalną wartość jakości, domyślnie 85. Funkcja `optimize_images` przechodzi przez pliki folderu, sprawdza ich rozszerzenia i wywołuje `convert_to_webp`. Zoptymalizowane obrazy WebP zapisuje w określonym folderze wyjściowym.

Dostosuj wartości `folder_path`, `output_folder` i `quality` do swoich potrzeb.

## Podsumowanie

Optymalizacja obrazów przyspiesza witryny, poprawia doświadczenie użytkowników i wspiera widoczność w wynikach wyszukiwania. Ekosystem Pythona oferuje narzędzia do kompresji, zmiany rozmiaru i konwersji obrazów oraz automatyzacji tych zadań. Pillow i Tinify przetwarzają pojedyncze obrazy lub całe zestawy, zachowując użyteczną jakość wizualną. Najpierw wybierz odpowiednie wymiary i jakość, a następnie zastosuj te ustawienia w swoim procesie.


## Źródła
- https://pillow.readthedocs.io/en/stable/
- https://developers.google.com/speed/webp
- https://tinypng.com/developers
