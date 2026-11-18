---
title: "Efficiënte en veilige Docker-containers bouwen: Een gids voor beginners"
date: 2023-02-24
lastmod: 2026-11-13
toc: true
draft: false
description: "Leer hoe u efficiënte en veilige Docker-containers maakt met behulp van best practices, tips en stapsgewijze instructies in deze uitgebreide gids."
tags: ["docker", "containers", "containerisatie", "devops", "inzet", "draagbaarheid", "efficiëntie", "beveiliging", "beste praktijken", "Dockerfile", "basisbeelden", "omgevingsvariabelen", "volumekoppelingen", "root-gebruiker", "actuele beelden", "softwareontwikkeling", "containerbeelden", "Docker Hub", "container orkestratie", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.webp"
coverAlt: "Een 3D-geanimeerde afbeelding van een veilige, goed georganiseerde container met het Docker-logo erop, omringd door verschillende gereedschappen en apparatuur die te maken hebben met software engineering en DevOps."
coverCaption: ""
---

**Hoe bouw je Docker Containers**

Docker is een krachtig hulpmiddel dat kan worden gebruikt om draagbare en gemakkelijk inzetbare toepassingen te maken. In deze gids behandelen we de basisstappen voor het maken en bouwen van Docker-containers. We bespreken ook enkele best practices en tips om ervoor te zorgen dat uw Docker-containers efficiënt, veilig en gebruiksvriendelijk zijn.

## Docker begrijpen

Voordat we beginnen met het bouwen van Docker-containers, is het belangrijk om te begrijpen wat Docker is en hoe het werkt.

Docker is een hulpmiddel waarmee je een applicatie en zijn afhankelijkheden kunt verpakken in een container die op elk systeem kan draaien. De container is geïsoleerd van het hostsysteem en bevat alles wat nodig is om de applicatie te draaien, inclusief de code, runtime, systeemtools, bibliotheken en instellingen.

Containers zijn licht en gemakkelijk te implementeren, waardoor ze een populaire keuze zijn voor het bouwen en implementeren van toepassingen. Met Docker kunt u containers maken, beheren en uitvoeren met een eenvoudige opdrachtregelinterface.

## Een Docker Image bouwen

Om een Docker container te bouwen, moet je eerst een Docker image maken. Een Docker image is een snapshot van een container die alle bestanden, bibliotheken en afhankelijkheden bevat die nodig zijn om de applicatie te draaien.

Hier zijn de basisstappen om een Docker image te maken:

1. **Maak een Dockerfile**
2. **Bouw de image**
3. **Run de container**

### Stap 1: Maak een Dockerfile aan

De eerste stap om een Docker image te bouwen is het maken van een Dockerfile. Een Dockerfile is een tekstbestand dat de instructies bevat die nodig zijn om de image te bouwen. Hier is een voorbeeld van een eenvoudige Dockerfile:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Laten we deze Dockerfile uit elkaar halen:

-`FROM ubuntu:latest` specificeert het basisimage dat voor de container moet worden gebruikt. In dit geval gebruiken we de laatste versie van Ubuntu.
-`RUN apt-get update && apt-get install -y nginx` werkt de pakketlijst bij en installeert de nginx webserver.
-`COPY index.html /var/www/html/` kopieert het index.html bestand naar de web root van de container.
-`EXPOSE 80` stelt poort 80 bloot aan het host systeem.
-`CMD ["nginx", "-g", "daemon off;"]` start de nginx server en draait deze op de voorgrond.

### Stap 2: Bouw de afbeelding

Nadat u de Dockerfile hebt gemaakt, kunt u de image bouwen met de`docker build` commando. Hier is een voorbeeld:

```bash
docker run -d -p 80:80 my-nginx-image
```

Laten we dit commando afbreken:

-`docker run` vertelt Docker om een container te draaien.
-`-d` draait de container in vrijstaande modus, wat betekent dat hij op de achtergrond draait.
-`-p 80:80` koppelt poort 80 op het hostsysteem aan poort 80 in de container.
-`my-nginx-image` specificeert de naam van de Docker image die moet worden gebruikt voor de container.

## Beste Praktijken

Nu je weet hoe je Docker-containers bouwt, laten we enkele best practices doornemen om ervoor te zorgen dat je Docker-containers efficiënt, veilig en gemakkelijk te gebruiken zijn.

### Gebruik kleine basisafbeeldingen

Om uw Docker containers klein en snel te implementeren te houden, gebruikt u best kleine base images die enkel de afhankelijkheden bevatten die uw applicatie nodig heeft. Bijvoorbeeld, in plaats van een volledig besturingssysteem zoals Ubuntu of CentOS te gebruiken, kunt u een kleiner image zoals Alpine Linux of BusyBox gebruiken.

### Lagen minimaliseren

Elke lijn in uw Dockerfile creëert een nieuwe laag in uw Docker image, en elke laag vergroot de grootte van de image. Om uw Docker-images zo klein mogelijk te houden, moet u proberen het aantal lagen in uw image te minimaliseren. Een manier om dit te doen is om gelijkaardige commando's te groeperen in een enkele lijn in uw Dockerfile. Bijvoorbeeld, in plaats van twee afzonderlijke`RUN` commando's om de pakketlijst bij te werken en een pakket te installeren, kunt u één enkel`RUN` commando om beide tegelijk te doen.

Ex:
```dockerfile
RUN apt update
RUN apt install apache -y
```
vs
```dockerfile
RUN apt update && apt install apache -y
```

### Omgevingsvariabelen gebruiken

Het gebruik van omgevingsvariabelen in uw Dockerfile in plaats van hardcoding waarden maakt het gemakkelijker om uw container tijdens runtime aan te passen en zorgt ervoor dat uw Dockerfile draagbaar is. U kunt bijvoorbeeld omgevingsvariabelen gebruiken om de poort waarop uw applicatie draait of de locatie van een configuratiebestand op te geven.

Voorbeeld:
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# De werkmap instellen
WORKDIR /app

# package.json en yarn.lock naar de container kopiëren
COPY package.json yarn.lock ./

# Afhankelijkheden installeren
RUN yarn install --frozen-lockfile

# Applicatiecode naar de container kopiëren
COPY . .

# De applicatiepoort beschikbaar maken
EXPOSE $PORT

# De applicatie starten
CMD ["yarn", "start"]
```


### Volumekoppelingen gebruiken

Volume mounts zijn een manier om gegevens te delen tussen uw hostsysteem en uw Docker-container. Dit maakt het gemakkelijker om gegevens te beheren en vermindert de grootte van je Docker-container. U kunt bijvoorbeeld een volume mount gebruiken om een databasebestand te delen tussen uw hostsysteem en uw container.

Ex:
```bash
docker run -v /home/user/app/data:/app/data my-app
```

```Dockerfile
FROM node:14

# De werkmap instellen
WORKDIR /app

# De bestanden package.json en yarn.lock naar de container kopiëren
COPY package.json yarn.lock ./

# Afhankelijkheden installeren
RUN yarn install --frozen-lockfile

# Overige applicatiecode naar de container kopiëren
COPY . .

# De applicatiepoort beschikbaar maken
EXPOSE 3000

# De applicatie starten
CMD ["yarn", "start"]

# Een volume koppelen voor applicatiegegevens
VOLUME ["/app/data"]
```

### Vermijd rennen als root

Uw Docker-container draaien als de root-gebruiker kan een veiligheidsrisico vormen. Maak in plaats daarvan een nieuwe gebruiker aan in uw Dockerfile en draai de container als die gebruiker. U kunt bijvoorbeeld de`USER` commando in uw Dockerfile om een nieuwe gebruiker aan te maken en vervolgens naar die gebruiker over te schakelen bij het uitvoeren van de container.

Ex:
```Dockerfile
FROM node:14

# Een gebruiker maken om de container uit te voeren
RUN useradd --user-group --create-home --shell /bin/false app

# De werkmap wijzigen naar de thuismap van de app-gebruiker
WORKDIR /home/app

# Afhankelijkheden installeren als app-gebruiker
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# Applicatiecode kopiëren als app-gebruiker
COPY --chown=app:app . .

# De poort beschikbaar maken
EXPOSE 3000

# De applicatie starten als app-gebruiker
CMD ["yarn", "start"]
```

### Afbeeldingen actueel houden

Om ervoor te zorgen dat uw Docker-containers veilig en vrij van kwetsbaarheden zijn, is het belangrijk om uw Docker-images up-to-date te houden. Dit betekent het regelmatig bijwerken van de basisimage en alle afhankelijkheden waar uw applicatie van afhankelijk is. U kunt bijvoorbeeld de`apt-get update` en`apt-get upgrade` commando's in uw Dockerfile om uw container up-to-date te houden met de laatste beveiligingspatches en bugfixes.

Ex:
```Dockerfile
FROM ubuntu:latest

# De pakketlijst bijwerken en beveiligingsupdates installeren
RUN apt-get update && apt-get upgrade -y && apt-get clean

# De nginx-webserver installeren
RUN apt-get install -y nginx

# Applicatiecode naar de container kopiëren
COPY . /var/www/html/

# Poort 80 beschikbaar maken voor het hostsysteem
EXPOSE 80

# De nginx-server starten
CMD ["nginx", "-g", "daemon off;"]

```
## Verder leren
### Docker Documentatie
[Docker](https://www.docker.com/) is een open-source platform voor het bouwen, verschepen en draaien van applicaties in containers. De Docker-documentatiewebsite biedt gedetailleerde informatie over de installatie, configuratie en het gebruik van Docker voor verschillende besturingssystemen en gebruikssituaties. De website bevat ook informatie over Docker API's, Docker CLI-commando's en tips voor probleemoplossing.

Enkele nuttige secties van de Docker-documentatie zijn:

- [Aan de slag met Docker](https://docs.docker.com/get-started/)
- [Docker CLI-referentie](https://docs.docker.com/engine/reference/commandline/cli/)
- [Docker API-referentie](https://docs.docker.com/engine/api/v1.41/)
- [Docker Compose-referentie](https://docs.docker.com/compose/compose-file/)
- [Dockerfile-referentie](https://docs.docker.com/engine/reference/builder/)

De Docker-documentatie is een geweldige bron om te leren hoe Docker te gebruiken en om problemen op te lossen die u kunt tegenkomen.

### Docker Hub
[Docker Hub](https://hub.docker.com/) is een cloud-gebaseerde repository waarmee u Docker-images kunt opslaan, delen en beheren. Docker Hub bevat publieke en private repositories, evenals geautomatiseerde builds en workflows. U kunt Docker Hub gebruiken om uw eigen Docker-images op te slaan, maar ook om vooraf gebouwde images te vinden voor populaire softwaretoepassingen en tools.

Enkele nuttige functies van Docker Hub zijn:

- [Docker-images zoeken](https://hub.docker.com/search?type=image)
- [Docker-images in repositories opslaan en beheren](https://hub.docker.com/repositories)
- [Builds en tests automatiseren met Docker Hub-workflows](https://docs.docker.com/docker-hub/builds/)

Docker Hub is een essentieel hulpmiddel voor het werken met Docker, en het kan u veel tijd en moeite besparen bij het beheren en delen van Docker-images.


## Conclusie

Docker is een krachtig hulpmiddel dat kan helpen uw toepassingen draagbaarder, efficiënter en gemakkelijker te implementeren te maken. Door deze best practices en tips te volgen, kunt u Docker-containers maken die veilig, gebruiksvriendelijk en snel te implementeren zijn. Of u nu een nieuwe applicatie bouwt of een bestaande naar Docker migreert, deze stappen helpen u op weg met het bouwen van Docker-containers.

