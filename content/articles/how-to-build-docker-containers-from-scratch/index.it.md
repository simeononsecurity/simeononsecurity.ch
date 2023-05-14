---
title: "Costruire contenitori Docker efficienti e sicuri: Una guida per principianti"
date: 2023-02-24
toc: true
draft: false
description: "Imparate a creare contenitori Docker efficienti e sicuri utilizzando le migliori pratiche, i suggerimenti e le istruzioni passo-passo di questa guida completa."
tags: ["docker", "contenitori", "containerizzazione", "devops", "dispiegamento", "portabilità", "efficienza", "sicurezza", "migliori pratiche", "Profilo Docker", "immagini di base", "variabili d'ambiente", "montaggi del volume", "utente root", "immagini aggiornate", "sviluppo software", "immagini del contenitore", "Hub Docker", "orchestrazione dei container", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.png"
coverAlt: "Un'immagine animata in 3D di un container sicuro e ben organizzato con il logo Docker, circondato da vari strumenti e attrezzature legati all'ingegneria del software e a DevOps."
coverCaption: ""
---

**Come costruire i contenitori Docker**

Docker è un potente strumento che può essere utilizzato per creare applicazioni portatili e facilmente distribuibili. In questa guida verranno illustrati i passi fondamentali per creare e costruire i contenitori Docker. Verranno inoltre illustrate alcune best practice e suggerimenti per garantire che i contenitori Docker siano efficienti, sicuri e facili da usare.

## Capire Docker

Prima di iniziare a costruire i contenitori Docker, è importante capire cos'è e come funziona Docker.

Docker è uno strumento che consente di impacchettare un'applicazione e le sue dipendenze in un contenitore che può essere eseguito su qualsiasi sistema. Il contenitore è isolato dal sistema host e include tutto ciò che serve per eseguire l'applicazione, compreso il codice, il runtime, gli strumenti di sistema, le librerie e le impostazioni.

I container sono leggeri e facili da distribuire, il che li rende una scelta popolare per la creazione e la distribuzione di applicazioni. Con Docker è possibile creare, gestire ed eseguire i container con una semplice interfaccia a riga di comando.

## Creare un'immagine Docker

Per creare un contenitore Docker, è necessario creare un'immagine Docker. Un'immagine Docker è un'istantanea di un contenitore che include tutti i file, le librerie e le dipendenze necessarie per eseguire l'applicazione.

Ecco i passi fondamentali per creare un'immagine Docker:

1. **Creare un file Docker**
2. **Creare l'immagine**
3. **Eseguire il contenitore**

### Passo 1: Creare un file Docker

Il primo passo per costruire un'immagine Docker è creare un Dockerfile. Un Dockerfile è un file di testo che contiene le istruzioni necessarie per costruire l'immagine. Ecco un esempio di un semplice file Docker:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Analizziamo questo file Docker:

-`FROM ubuntu:latest` specifica l'immagine di base da usare per il contenitore. In questo caso, usiamo l'ultima versione di Ubuntu.
-`RUN apt-get update && apt-get install -y nginx` aggiorna l'elenco dei pacchetti e installa il server web nginx.
-`COPY index.html /var/www/html/` copia il file index.html nella radice web del contenitore.
-`EXPOSE 80` espone la porta 80 al sistema host.
-`CMD ["nginx", "-g", "daemon off;"]` avvia il server nginx e lo esegue in primo piano.

### Passo 2: Creare l'immagine

Dopo aver creato il file Docker, si può costruire l'immagine usando il metodo`docker build` comando. Ecco un esempio:

```bash
docker run -d -p 80:80 my-nginx-image
```

Analizziamo questo comando:

-`docker run` indica a Docker di eseguire un container.
-`-d` esegue il contenitore in modalità distaccata, cioè in background.
-`-p 80:80` mappa la porta 80 del sistema host alla porta 80 del contenitore.
-`my-nginx-image` specifica il nome dell'immagine Docker da usare per il contenitore.

## Migliori pratiche

Ora che sapete come costruire i contenitori Docker, esaminiamo alcune best practice per garantire che i vostri contenitori Docker siano efficienti, sicuri e facili da usare.

### Usare immagini di base piccole

Per mantenere i contenitori Docker piccoli e veloci da distribuire, è meglio usare immagini di base piccole che contengano solo le dipendenze necessarie all'applicazione. Ad esempio, invece di usare un sistema operativo completo come Ubuntu o CentOS, si può usare un'immagine più piccola come Alpine Linux o BusyBox.

### Ridurre al minimo i livelli

Ogni riga del file Docker crea un nuovo livello nell'immagine Docker e ogni livello aumenta le dimensioni dell'immagine. Per mantenere le immagini Docker il più piccole possibile, si dovrebbe cercare di ridurre al minimo il numero di livelli nell'immagine. Un modo per farlo è raggruppare comandi simili in un'unica riga del file Docker. Per esempio, invece di usare due comandi separati`RUN` per aggiornare l'elenco dei pacchetti e installare un pacchetto, è possibile utilizzare un unico comando`RUN` per eseguire entrambe le operazioni contemporaneamente.

Es:
```dockerfile
RUN apt update 
RUN apt install apache -y
```
vs
```dockerfile
RUN apt update && apt install apache -y
```

### Utilizzare le variabili d'ambiente

L'uso di variabili d'ambiente nel file Docker, anziché la codifica dei valori, rende più facile la personalizzazione del contenitore in fase di esecuzione e garantisce la portabilità del file Docker. Ad esempio, si possono usare le variabili d'ambiente per specificare la porta su cui gira l'applicazione o la posizione di un file di configurazione.

Es:
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


### Utilizzare i montaggi di volume

I montaggi di volume sono un modo per condividere i dati tra il sistema host e il contenitore Docker. Questo facilita la gestione dei dati e riduce le dimensioni del contenitore Docker. Ad esempio, si può usare un montaggio di volume per condividere un file di database tra il sistema host e il contenitore.

Es:
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

### Evitare l'esecuzione come root

L'esecuzione del contenitore Docker come utente root può rappresentare un rischio per la sicurezza. Si dovrebbe invece creare un nuovo utente nel file Docker ed eseguire il contenitore come tale. Ad esempio, si può usare l'opzione`USER` nel file Docker per creare un nuovo utente e poi passare a quell'utente durante l'esecuzione del contenitore.

Es:
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

### Mantenere le immagini aggiornate

Per garantire che i contenitori Docker siano sicuri e privi di vulnerabilità, è importante mantenere le immagini Docker aggiornate. Ciò significa aggiornare regolarmente l'immagine di base e tutte le dipendenze su cui si basa l'applicazione. Ad esempio, è possibile utilizzare il file`apt-get update` e`apt-get upgrade` nel vostro file Docker per mantenere il vostro contenitore aggiornato con le ultime patch di sicurezza e correzioni di bug.

Es:
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
## Approfondisci i tuoi studi
### Documentazione Docker
[Docker](https://www.docker.com/) è una piattaforma open-source per la creazione, la spedizione e l'esecuzione di applicazioni in container. Il sito web della documentazione di Docker fornisce informazioni dettagliate su come installare, configurare e utilizzare Docker per una varietà di sistemi operativi e casi d'uso. Il sito include anche informazioni sulle API di Docker, sui comandi della CLI di Docker e suggerimenti per la risoluzione dei problemi.

Alcune sezioni utili della documentazione di Docker includono:

-[Get started with Docker](https://docs.docker.com/get-started/)
-[Docker CLI reference](https://docs.docker.com/engine/reference/commandline/cli/)
-[Docker API reference](https://docs.docker.com/engine/api/v1.41/)
-[Docker-compose reference](https://docs.docker.com/compose/compose-file/)
-[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

La documentazione di Docker è un'ottima risorsa per imparare a usare Docker e per risolvere i problemi che si possono incontrare.

### Hub Docker
[Docker Hub](https://hub.docker.com/) è un repository basato sul cloud che consente di archiviare, condividere e gestire immagini Docker. Docker Hub include repository pubblici e privati, nonché build e flussi di lavoro automatizzati. È possibile utilizzare Docker Hub per archiviare le proprie immagini Docker e per trovare immagini precostituite per le applicazioni e gli strumenti software più diffusi.

Alcune utili funzioni di Docker Hub includono:

-[Search for Docker images](https://hub.docker.com/search?type=image)
-[Store and manage Docker images in repositories](https://hub.docker.com/repositories)
-[Automate builds and testing with Docker Hub workflows](https://docs.docker.com/docker-hub/builds/)

Docker Hub è uno strumento essenziale per lavorare con Docker e può far risparmiare molto tempo e fatica quando si tratta di gestire e condividere immagini Docker.


## Conclusione

Docker è uno strumento potente che può aiutare a rendere le applicazioni più portatili, efficienti e facili da distribuire. Seguendo queste best practice e questi suggerimenti, è possibile creare contenitori Docker sicuri, facili da usare e veloci da distribuire. Sia che stiate costruendo una nuova applicazione o migrando una esistente a Docker, questi passaggi vi aiuteranno a iniziare a creare contenitori Docker.

