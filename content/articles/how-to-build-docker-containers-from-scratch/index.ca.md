---
title: "Crear contenidors Docker eficients i segurs"
date: 2023-02-24
lastmod: 2026-11-27
toc: true
draft: false
description: "Aprèn a crear contenidors Docker eficients i segurs amb bones pràctiques, consells i instruccions pas a pas en aquesta guia completa."
tags: ["Docker", "contenidors", "contenidorització", "DevOps", "desplegament", "portabilitat", "eficiència", "seguretat", "bones pràctiques", "Dockerfile", "imatges base", "variables d'entorn", "muntatges de volums", "usuari root", "imatges actualitzades", "desenvolupament de programari", "imatges de contenidor", "Docker Hub", "orquestració de contenidors", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.webp"
coverAlt: "Imatge animada en 3D d'un contenidor segur i ben organitzat amb el logotip de Docker, envoltat de diverses eines i equips relacionats amb l'enginyeria de programari i DevOps."
coverCaption: ""
---

**Com crear contenidors Docker**

Docker és una eina potent que permet crear aplicacions portables i fàcils de desplegar. En aquesta guia explicarem els passos bàsics per crear i construir contenidors Docker. També repassarem bones pràctiques i consells perquè els contenidors Docker siguin eficients, segurs i fàcils d'utilitzar.

## Entendre Docker

Abans de començar a construir contenidors Docker, és important entendre què és Docker i com funciona.

Docker és una eina que permet empaquetar una aplicació i les seves dependències en un contenidor que es pot executar en qualsevol sistema. El contenidor està aïllat del sistema amfitrió i inclou tot el necessari per executar l'aplicació, com ara el codi, l'entorn d'execució, les eines del sistema, les biblioteques i la configuració.

Els contenidors són lleugers i fàcils de desplegar, per això són una opció popular per crear i desplegar aplicacions. Amb Docker, pots crear, gestionar i executar contenidors amb una interfície de línia d'ordres senzilla.

## Construir una imatge Docker

Per construir un contenidor Docker, primer has de crear una imatge Docker. Una imatge Docker és una instantània d'un contenidor que inclou tots els fitxers, les biblioteques i les dependències necessàries per executar l'aplicació.

Aquests són els passos bàsics per crear una imatge Docker:

1. **Crea un Dockerfile**
2. **Construeix la imatge**
3. **Executa el contenidor**

### Pas 1: Crea un Dockerfile

El primer pas per construir una imatge Docker és crear un Dockerfile. Un Dockerfile és un fitxer de text amb les instruccions necessàries per construir la imatge. Aquest és un exemple de Dockerfile senzill:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Desglossem aquest Dockerfile:

- `FROM ubuntu:latest` especifica la imatge base que s'utilitzarà per al contenidor. En aquest cas, utilitzem l'última versió d'Ubuntu.
- `RUN apt-get update && apt-get install -y nginx` actualitza la llista de paquets i instal·la el servidor web nginx.
- `COPY index.html /var/www/html/` copia el fitxer index.html a l'arrel web del contenidor.
- `EXPOSE 80` exposa el port 80 al sistema amfitrió.
- `CMD ["nginx", "-g", "daemon off;"]` inicia el servidor nginx i l'executa en primer pla.

### Pas 2: Construeix la imatge

Després de crear el Dockerfile, pots construir la imatge amb l'ordre `docker build`. Aquest n'és un exemple:

```bash
docker run -d -p 80:80 my-nginx-image
```

Desglossem aquesta ordre:

- `docker run` indica a Docker que executi un contenidor.
- `-d` executa el contenidor en mode deslligat, és a dir, en segon pla.
- `-p 80:80` associa el port 80 del sistema amfitrió amb el port 80 del contenidor.
- `my-nginx-image` especifica el nom de la imatge Docker que s'utilitzarà per al contenidor.

## Bones pràctiques

Ara que saps com construir contenidors Docker, repassem algunes bones pràctiques perquè siguin eficients, segurs i fàcils d'utilitzar.

### Utilitza imatges base petites

Per mantenir petits els contenidors Docker i desplegar-los ràpidament, és millor utilitzar imatges base petites que només incloguin les dependències que necessita l'aplicació. Per exemple, en lloc d'utilitzar un sistema operatiu complet com Ubuntu o CentOS, pots fer servir una imatge més petita com Alpine Linux o BusyBox.

### Redueix el nombre de capes

Cada línia del Dockerfile crea una capa nova a la imatge Docker, i cada capa n'augmenta la mida. Per mantenir les imatges Docker tan petites com sigui possible, intenta reduir el nombre de capes. Una manera de fer-ho és agrupar ordres semblants en una sola línia del Dockerfile. Per exemple, en lloc d'utilitzar dues ordres `RUN` separades per actualitzar la llista de paquets i instal·lar-ne un, pots fer servir una sola ordre `RUN` per fer totes dues coses alhora.

Exemple:
```dockerfile
RUN apt update
RUN apt install apache -y
```
en lloc de
```dockerfile
RUN apt update && apt install apache -y
```

### Utilitza variables d'entorn

Si utilitzes variables d'entorn al Dockerfile en lloc de valors fixos, és més fàcil personalitzar el contenidor en temps d'execució i el Dockerfile és més portable. Per exemple, pots fer servir variables d'entorn per especificar el port de l'aplicació o la ubicació d'un fitxer de configuració.

Exemple:
```bash
docker run -e PORT=3000 my-app
```
```Dockerfile
FROM node:14

# Estableix el directori de treball
WORKDIR /app

# Copia package.json i yarn.lock al contenidor
COPY package.json yarn.lock ./

# Instal·la les dependències
RUN yarn install --frozen-lockfile

# Copia el codi de l'aplicació al contenidor
COPY . .

# Exposa el port de l'aplicació
EXPOSE $PORT

# Inicia l'aplicació
CMD ["yarn", "start"]
```


### Utilitza muntatges de volums

Els muntatges de volums permeten compartir dades entre el sistema amfitrió i el contenidor Docker. Això facilita la gestió de les dades i redueix la mida del contenidor Docker. Per exemple, pots muntar un volum per compartir un fitxer de base de dades entre el sistema amfitrió i el contenidor.

Exemple:
```bash
docker run -v /home/user/app/data:/app/data my-app
```

```Dockerfile
FROM node:14

# Estableix el directori de treball
WORKDIR /app

# Copia els fitxers package.json i yarn.lock al contenidor
COPY package.json yarn.lock ./

# Instal·la les dependències
RUN yarn install --frozen-lockfile

# Copia la resta del codi de l'aplicació al contenidor
COPY . .

# Exposa el port de l'aplicació
EXPOSE 3000

# Inicia l'aplicació
CMD ["yarn", "start"]

# Munta un volum per a les dades de l'aplicació
VOLUME ["/app/data"]
```

### Evita executar-lo com a root

Executar un contenidor Docker com a usuari root pot representar un risc de seguretat. En lloc d'això, crea un usuari nou al Dockerfile i executa el contenidor amb aquest usuari. Per exemple, pots utilitzar l'ordre `USER` al Dockerfile per crear un usuari nou i després canviar a aquest usuari quan executis el contenidor.

Exemple:
```Dockerfile
FROM node:14

# Crea un usuari nou per executar el contenidor
RUN useradd --user-group --create-home --shell /bin/false app

# Canvia el directori de treball al directori personal de l'usuari app
WORKDIR /home/app

# Instal·la les dependències com a usuari app
COPY package.json yarn.lock ./
RUN chown -R app:app /home/app
USER app
RUN yarn install --frozen-lockfile --production

# Copia el codi de l'aplicació com a usuari app
COPY --chown=app:app . .

# Exposa el port
EXPOSE 3000

# Inicia l'aplicació com a usuari app
CMD ["yarn", "start"]
```

### Mantén les imatges actualitzades

Per garantir que els contenidors Docker siguin segurs i no tinguin vulnerabilitats, és important mantenir les imatges Docker actualitzades. Això vol dir actualitzar regularment la imatge base i les dependències de l'aplicació. Per exemple, pots utilitzar les ordres `apt-get update` i `apt-get upgrade` al Dockerfile per mantenir el contenidor al dia amb els últims pegats de seguretat i correccions d'errors.

Exemple:
```Dockerfile
FROM ubuntu:latest

# Actualitza la llista de paquets i instal·la actualitzacions de seguretat
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Instal·la el servidor web nginx
RUN apt-get install -y nginx

# Copia el codi de l'aplicació al contenidor
COPY . /var/www/html/

# Exposa el port 80 al sistema amfitrió
EXPOSE 80

# Inicia el servidor nginx
CMD ["nginx", "-g", "daemon off;"]

```
## Continua aprenent
### Documentació de Docker
[Docker](https://www.docker.com/) és una plataforma de codi obert per construir, distribuir i executar aplicacions en contenidors. El lloc web de documentació de Docker ofereix informació detallada sobre com instal·lar, configurar i utilitzar Docker en diversos sistemes operatius i casos d'ús. També inclou informació sobre les API de Docker, les ordres del Docker CLI i consells per resoldre problemes.

Aquestes són algunes seccions útils de la documentació de Docker:

- [Comença amb Docker](https://docs.docker.com/get-started/)
- [Referència del Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/)
- [Referència de l'API de Docker](https://docs.docker.com/engine/api/v1.41/)
- [Referència de Docker Compose](https://docs.docker.com/compose/compose-file/)
- [Referència de Dockerfile](https://docs.docker.com/engine/reference/builder/)

La documentació de Docker és un bon recurs per aprendre a utilitzar Docker i resoldre els problemes que puguis trobar.

### Docker Hub

[Docker Hub](https://hub.docker.com/) és un repositori al núvol que permet emmagatzemar, compartir i gestionar imatges Docker. Inclou repositoris públics i privats, així com compilacions automatitzades i fluxos de treball. Pots utilitzar Docker Hub per desar les teves imatges Docker i també per trobar imatges ja construïdes per a aplicacions i eines de programari populars.

Algunes funcions útils de Docker Hub són:

- [Cerca imatges Docker](https://hub.docker.com/search?type=image)
- [Emmagatzema i gestiona imatges en repositoris](https://hub.docker.com/repositories)
- [Automatitza les compilacions i les proves amb els fluxos de treball de Docker Hub](https://docs.docker.com/docker-hub/builds/)

Docker Hub és una eina essencial per treballar amb Docker i pot estalviar molt de temps i esforç en gestionar i compartir imatges.

## Conclusió

Docker és una eina potent que pot fer que les aplicacions siguin més portables, eficients i fàcils de desplegar. Si segueixes aquestes bones pràctiques i consells, pots crear contenidors Docker segurs, fàcils d'utilitzar i ràpids de desplegar. Tant si crees una aplicació nova com si migres una d'existent a Docker, aquests passos t'ajudaran a començar a construir contenidors Docker.
