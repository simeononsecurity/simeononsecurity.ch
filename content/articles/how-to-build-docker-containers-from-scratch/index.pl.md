---
title: "Budowanie wydajnych i bezpiecznych kontenerów Docker: Przewodnik dla początkujących"
date: 2023-02-24
toc: true
draft: false
description: "Dowiedz się, jak tworzyć wydajne i bezpieczne kontenery Docker za pomocą najlepszych praktyk, wskazówek i instrukcji krok po kroku w tym kompleksowym przewodniku."
tags: ["docker", "pojemniki", "konteneryzacja", "devops", "wdrożenie", "przenośność", "efektywność", "bezpieczeństwo", "najlepsze praktyki", "Dockerfile", "obrazy bazowe", "zmienne środowiskowe", "uchwyty na woluminy", "użytkownik root", "aktualne obrazy", "rozwój oprogramowania", "obrazy kontenerów", "Docker Hub", "orkiestracja kontenerów", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.png"
coverAlt: "Animowany obraz 3D bezpiecznego, dobrze zorganizowanego kontenera z umieszczonym na nim logo Docker, w otoczeniu różnych narzędzi i urządzeń związanych z inżynierią oprogramowania i DevOps."
coverCaption: ""
---

**Jak zbudować kontenery Docker**.

Docker to potężne narzędzie, które można wykorzystać do tworzenia przenośnych i łatwo wdrażanych aplikacji. W tym przewodniku omówimy podstawowe kroki tworzenia i budowania kontenerów Docker. Omówimy również kilka najlepszych praktyk i wskazówek, aby zapewnić, że kontenery Docker są wydajne, bezpieczne i łatwe w użyciu.

## Zrozumieć Dockera

Zanim zaczniemy budować kontenery Docker, ważne jest, aby zrozumieć, czym jest Docker i jak działa.

Docker jest narzędziem, które pozwala spakować aplikację i jej zależności do kontenera, który może być uruchomiony na dowolnym systemie. Kontener jest odizolowany od systemu hosta i zawiera wszystko, co jest potrzebne do uruchomienia aplikacji, w tym kod, runtime, narzędzia systemowe, biblioteki i ustawienia.

Kontenery są lekkie i łatwe do wdrożenia, co czyni je popularnym wyborem do budowania i wdrażania aplikacji. Dzięki Dockerowi można tworzyć, zarządzać i uruchamiać kontenery za pomocą prostego interfejsu wiersza poleceń.

## Budowanie obrazu Dockera

Aby zbudować kontener Dockera, musisz najpierw stworzyć obraz Dockera. Obraz Dockera to migawka kontenera, która zawiera wszystkie pliki, biblioteki i zależności potrzebne do uruchomienia aplikacji.

Oto podstawowe kroki tworzenia obrazu Dockera:

1. **Utwórz plik Dockerfile**.
2. **Zbuduj obraz**.
3. **Uruchomić kontener**

### Krok 1: Utworzenie pliku Dockerfile

Pierwszym krokiem do zbudowania obrazu Dockera jest stworzenie pliku Dockerfile. Dockerfile to plik tekstowy, który zawiera instrukcje potrzebne do zbudowania obrazu. Oto przykład prostego pliku Dockerfile:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Rozbijmy ten plik Dockerfile:

-`FROM ubuntu:latest` określa obraz bazowy, który ma być użyty dla kontenera. W tym przypadku używamy najnowszej wersji Ubuntu.
-`RUN apt-get update && apt-get install -y nginx` aktualizuje listę pakietów i instaluje serwer WWW nginx.
-`COPY index.html /var/www/html/` kopiuje plik index.html do katalogu głównego kontenera.
-`EXPOSE 80` wystawia port 80 na działanie systemu hosta.
-`CMD ["nginx", "-g", "daemon off;"]` uruchamia serwer nginx i uruchamia go na pierwszym planie.

### Krok 2: Zbudowanie obrazu

Po utworzeniu pliku Dockerfile, możesz zbudować obraz używając polecenia`docker build` polecenie. Oto przykład:

```bash
docker run -d -p 80:80 my-nginx-image
```

Rozłóżmy to polecenie na czynniki pierwsze:

-`docker run` mówi Dockerowi, aby uruchomił kontener.
-`-d` uruchamia kontener w trybie odłączonym, co oznacza, że działa w tle.
-`-p 80:80` mapuje port 80 w systemie hosta na port 80 w kontenerze.
-`my-nginx-image` określa nazwę obrazu Docker, który ma być użyty dla kontenera.

## Najlepsze praktyki

Teraz, gdy już wiesz, jak budować kontenery Docker, przejdźmy do kilku najlepszych praktyk, aby upewnić się, że twoje kontenery Docker są wydajne, bezpieczne i łatwe w użyciu.

### Używaj małych obrazów bazowych

Aby kontenery Docker były małe i szybkie do wdrożenia, najlepiej jest używać małych obrazów bazowych, które zawierają tylko zależności, których potrzebuje Twoja aplikacja. Na przykład, zamiast używać pełnego systemu operacyjnego, takiego jak Ubuntu lub CentOS, można użyć mniejszego obrazu, takiego jak Alpine Linux lub BusyBox.

### Minimalizuj warstwy

Każda linia w pliku Dockerfile tworzy nową warstwę w obrazie Docker, a każda warstwa zwiększa rozmiar obrazu. Aby utrzymać obrazy Docker tak małe jak to możliwe, powinieneś spróbować zminimalizować liczbę warstw w swoim obrazie. Jednym ze sposobów na to jest grupowanie podobnych poleceń w jednej linii w pliku Dockerfile. Na przykład, zamiast używać dwóch osobnych`RUN` aby zaktualizować listę pakietów i zainstalować pakiet, możesz użyć jednego polecenia`RUN` polecenie, aby wykonać obie czynności w tym samym czasie.

Ex:
```dockerfile
RUN apt update 
RUN apt install apache -y
```
vs
```dockerfile
RUN apt update && apt install apache -y
```

### Użycie zmiennych środowiskowych

Używanie zmiennych środowiskowych w pliku Dockerfile zamiast twardego kodowania wartości ułatwia dostosowanie kontenera w czasie pracy i zapewnia, że plik Dockerfile jest przenośny. Na przykład, możesz użyć zmiennych środowiskowych do określenia portu, na którym działa Twoja aplikacja lub lokalizacji pliku konfiguracyjnego.

Ex:
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the application code to the container
COPY . .

# Expose the application port
EXPOSE $PORT

# Start the application
CMD ["yarn", "start"]
```


### Używanie uchwytów objętościowych

Mocowania wolumenów są sposobem na dzielenie danych pomiędzy systemem hosta a kontenerem Docker. Ułatwia to zarządzanie danymi i zmniejsza rozmiar kontenera Docker. Na przykład, możesz użyć montowania woluminu do współdzielenia pliku bazy danych między systemem hosta a kontenerem.

Ex:
```bash
docker run -v /home/user/app/data:/app/data my-app
```

```Dockerfile
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and yarn.lock files to the container
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the rest of the application code to the container
COPY . .

# Expose the application port
EXPOSE 3000

# Start the application
CMD ["yarn", "start"]

# Mount a volume for the application data
VOLUME ["/app/data"]
```

### Unikaj uruchamiania jako root

Uruchamianie kontenera Docker jako użytkownik root może stanowić zagrożenie bezpieczeństwa. Zamiast tego, powinieneś stworzyć nowego użytkownika w swoim pliku Docker i uruchomić kontener jako ten użytkownik. Na przykład, możesz użyć`USER` polecenie w swoim pliku Dockerfile, aby utworzyć nowego użytkownika, a następnie przełączyć się na niego podczas uruchamiania kontenera.

Ex:
```Dockerfile
FROM node:14

# Create a new user to run the container
RUN useradd --user-group --create-home --shell /bin/false app

# Change the working directory to the app user's home directory
WORKDIR /home/app

# Install dependencies as the app user
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# Copy the application code as the app user
COPY --chown=app:app . .

# Expose the port
EXPOSE 3000

# Start the application as the app user
CMD ["yarn", "start"]
```

### Keep Images Up to Date

Aby zapewnić, że kontenery Docker są bezpieczne i wolne od luk, ważne jest, aby obrazy Docker były aktualne. Oznacza to regularne aktualizowanie obrazu bazowego i wszelkich zależności, na których opiera się Twoja aplikacja. Na przykład, możesz użyć`apt-get update` oraz`apt-get upgrade` w swoim pliku Dockerfile, aby utrzymać kontener na bieżąco z najnowszymi łatami bezpieczeństwa i poprawkami błędów.

Ex:
```Dockerfile
FROM ubuntu:latest

# Update the package list and install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Install the nginx web server
RUN apt-get install -y nginx

# Copy the application code to the container
COPY . /var/www/html/

# Expose port 80 to the host system
EXPOSE 80

# Start the nginx server
CMD ["nginx", "-g", "daemon off;"]

```
## Further Your Studies
### Dokumentacja Docker
[Docker](https://www.docker.com/) to platforma open-source do budowania, wysyłania i uruchamiania aplikacji w kontenerach. Strona internetowa z dokumentacją Dockera zawiera szczegółowe informacje o tym, jak zainstalować, skonfigurować i używać Dockera w różnych systemach operacyjnych i przypadkach użycia. Strona zawiera również informacje na temat interfejsów API Dockera, poleceń Docker CLI oraz wskazówki dotyczące rozwiązywania problemów.

Niektóre przydatne sekcje dokumentacji Dockera obejmują:

-[Get started with Docker](https://docs.docker.com/get-started/)
-[Docker CLI reference](https://docs.docker.com/engine/reference/commandline/cli/)
-[Docker API reference](https://docs.docker.com/engine/api/v1.41/)
-[Docker-compose reference](https://docs.docker.com/compose/compose-file/)
-[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

Dokumentacja Dockera jest doskonałym źródłem wiedzy na temat używania Dockera i rozwiązywania wszelkich problemów, które możesz napotkać.

### Docker Hub
[Docker Hub](https://hub.docker.com/) to oparte na chmurze repozytorium, które umożliwia przechowywanie, udostępnianie i zarządzanie obrazami Dockera. Docker Hub obejmuje publiczne i prywatne repozytoria, a także zautomatyzowane kompilacje i przepływy pracy. Możesz użyć Docker Hub do przechowywania własnych obrazów Docker, jak również do znalezienia wstępnie zbudowanych obrazów dla popularnych aplikacji i narzędzi.

Niektóre przydatne funkcje Docker Hub obejmują:

-[Search for Docker images](https://hub.docker.com/search?type=image)
-[Store and manage Docker images in repositories](https://hub.docker.com/repositories)
-[Automate builds and testing with Docker Hub workflows](https://docs.docker.com/docker-hub/builds/)

Docker Hub to podstawowe narzędzie do pracy z Dockerem, które może zaoszczędzić wiele czasu i wysiłku, jeśli chodzi o zarządzanie i udostępnianie obrazów Docker.


## Wnioski.

Docker to potężne narzędzie, które może pomóc uczynić Twoje aplikacje bardziej przenośnymi, wydajnymi i łatwymi do wdrożenia. Stosując się do tych najlepszych praktyk i wskazówek, można tworzyć kontenery Dockera, które są bezpieczne, łatwe w użyciu i szybkie do wdrożenia. Niezależnie od tego, czy budujesz nową aplikację, czy migrujesz istniejącą do Dockera, te kroki pomogą Ci rozpocząć tworzenie kontenerów Dockera.

