---
title: "Effiziente und sichere Docker-Container bauen: Ein Leitfaden für Einsteiger"
date: 2023-02-24
toc: true
draft: false
description: "In diesem umfassenden Leitfaden erfahren Sie, wie Sie mithilfe von Best Practices, Tipps und Schritt-für-Schritt-Anleitungen effiziente und sichere Docker-Container erstellen können."
tags: ["Docker", "Container", "Containerisierung", "devops", "Bereitstellung", "Tragbarkeit", "efficiency", "Sicherheit", "beste Praktiken", "Dockerdatei", "Basisbilder", "Umgebungsvariablen", "Volumenhalterungen", "Stammbenutzer", "aktuelle Bilder", "Software-Entwicklung", "Container-Bilder", "Docker-Hub", "Container-Orchestrierung", "Kubernetes"]
cover: "/img/cover/A_3D_animated_image_of_a_secure_well-organized_container.png"
coverAlt: "Ein animiertes 3D-Bild eines sicheren, gut organisierten Containers mit dem Docker-Logo darauf, umgeben von verschiedenen Werkzeugen und Geräten aus den Bereichen Software-Engineering und DevOps."
coverCaption: ""
---

**Wie man Docker-Container baut**

Docker ist ein leistungsfähiges Tool zur Erstellung portabler und einfach zu implementierender Anwendungen. In diesem Leitfaden werden wir die grundlegenden Schritte zum Erstellen und Erstellen von Docker-Containern behandeln. Wir gehen auch auf einige bewährte Verfahren und Tipps ein, um sicherzustellen, dass Ihre Docker-Container effizient, sicher und einfach zu verwenden sind.

## Docker verstehen

Bevor wir mit der Erstellung von Docker-Containern beginnen, ist es wichtig zu verstehen, was Docker ist und wie es funktioniert.

Docker ist ein Tool, mit dem Sie eine Anwendung und ihre Abhängigkeiten in einen Container packen können, der auf jedem System ausgeführt werden kann. Der Container ist vom Hostsystem isoliert und enthält alles, was zur Ausführung der Anwendung benötigt wird, einschließlich Code, Laufzeit, Systemtools, Bibliotheken und Einstellungen.

Container sind leichtgewichtig und einfach zu implementieren, was sie zu einer beliebten Wahl für die Erstellung und Implementierung von Anwendungen macht. Mit Docker können Sie Container über eine einfache Befehlszeilenschnittstelle erstellen, verwalten und ausführen.

## Erstellen eines Docker-Images

Um einen Docker-Container zu erstellen, müssen Sie zunächst ein Docker-Abbild erstellen. Ein Docker-Image ist ein Snapshot eines Containers, der alle Dateien, Bibliotheken und Abhängigkeiten enthält, die für die Ausführung der Anwendung erforderlich sind.

Im Folgenden werden die grundlegenden Schritte zur Erstellung eines Docker-Abbilds beschrieben:

1. **Erstellen einer Dockerdatei**
2. **Erstellen des Images**
3. **Starten Sie den Container**

### Schritt 1: Erstellen einer Dockerdatei

Der erste Schritt zur Erstellung eines Docker-Abbilds ist die Erstellung einer Dockerdatei. Ein Dockerfile ist eine Textdatei, die die Anweisungen enthält, die zum Erstellen des Images benötigt werden. Hier ist ein Beispiel für ein einfaches Dockerfile:

```bash
FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Lassen Sie uns dieses Dockerfile aufschlüsseln:

- `FROM ubuntu:latest` gibt das Basis-Image an, das für den Container verwendet werden soll. In diesem Fall verwenden wir die neueste Version von Ubuntu.
- `RUN apt-get update && apt-get install -y nginx` aktualisiert die Paketliste und installiert den nginx-Webserver.
- `COPY index.html /var/www/html/` kopiert die Datei index.html in das Web-Root des Containers.
- `EXPOSE 80` gibt Port 80 für das Hostsystem frei.
- `CMD ["nginx", "-g", "daemon off;"]` startet den nginx-Server und führt ihn im Vordergrund aus.

### Schritt 2: Erstellen Sie das Image

Nachdem Sie die Dockerdatei erstellt haben, können Sie das Image mit dem Befehl `docker build` Befehl. Hier ist ein Beispiel:

```bash
docker run -d -p 80:80 my-nginx-image
```

Wir wollen diesen Befehl aufschlüsseln:

- `docker run` weist Docker an, einen Container zu starten.
- `-d` führt den Container im Detached Mode aus, d.h. er läuft im Hintergrund.
- `-p 80:80` ordnet Port 80 auf dem Hostsystem dem Port 80 im Container zu.
- `my-nginx-image` gibt den Namen des Docker-Images an, das für den Container verwendet werden soll.

## Beste Praktiken

Nachdem Sie nun wissen, wie man Docker-Container erstellt, wollen wir nun einige Best Practices durchgehen, um sicherzustellen, dass Ihre Docker-Container effizient, sicher und einfach zu verwenden sind.

### Kleine Basis-Images verwenden

Damit Ihre Docker-Container klein bleiben und schnell bereitgestellt werden können, verwenden Sie am besten kleine Basis-Images, die nur die für Ihre Anwendung erforderlichen Abhängigkeiten enthalten. Anstelle eines vollständigen Betriebssystems wie Ubuntu oder CentOS können Sie beispielsweise ein kleineres Image wie Alpine Linux oder BusyBox verwenden.

### Ebenen minimieren

Jede Zeile in Ihrer Dockerdatei erzeugt eine neue Schicht in Ihrem Docker-Image, und jede Schicht erhöht die Größe des Images. Um Ihre Docker-Images so klein wie möglich zu halten, sollten Sie versuchen, die Anzahl der Schichten in Ihrem Image zu minimieren. Eine Möglichkeit, dies zu erreichen, besteht darin, ähnliche Befehle in einer einzigen Zeile in Ihrem Dockerfile zusammenzufassen. Anstatt zum Beispiel zwei separate `RUN` Befehle, um die Paketliste zu aktualisieren und ein Paket zu installieren, können Sie mit einem einzigen `RUN` Befehl, um beides gleichzeitig zu tun.

Bsp:
```dockerfile
RUN apt update 
RUN apt install apache -y
```
gegen
```dockerfile
RUN apt update && apt install apache -y
```

### Umgebungsvariablen verwenden

Die Verwendung von Umgebungsvariablen in Ihrer Dockerdatei anstelle von fest codierten Werten erleichtert die Anpassung Ihres Containers zur Laufzeit und stellt sicher, dass Ihre Dockerdatei portabel ist. Sie können zum Beispiel Umgebungsvariablen verwenden, um den Port, auf dem Ihre Anwendung läuft, oder den Speicherort einer Konfigurationsdatei anzugeben.

Beispiel:
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


### Volume Mounts verwenden

Volume Mounts sind eine Möglichkeit, Daten zwischen Ihrem Hostsystem und Ihrem Docker-Container zu teilen. Dies erleichtert die Datenverwaltung und verringert die Größe Ihres Docker-Containers. Sie können zum Beispiel eine Volume-Einhängung verwenden, um eine Datenbankdatei zwischen Ihrem Host-System und Ihrem Container zu teilen.

Beispiel:
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

### Vermeiden Sie die Ausführung als Root

Wenn Sie Ihren Docker-Container als Root-Benutzer ausführen, kann dies ein Sicherheitsrisiko darstellen. Stattdessen sollten Sie einen neuen Benutzer in Ihrer Dockerdatei anlegen und den Container als diesen Benutzer ausführen. Zum Beispiel können Sie die `USER` in Ihrem Dockerfile einen neuen Benutzer anlegen und dann beim Ausführen des Containers zu diesem Benutzer wechseln.

Bsp:
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

### Bilder auf dem neuesten Stand halten

Um sicherzustellen, dass Ihre Docker-Container sicher und frei von Schwachstellen sind, ist es wichtig, dass Sie Ihre Docker-Images auf dem neuesten Stand halten. Das bedeutet, dass Sie das Basis-Image und alle Abhängigkeiten, auf die Ihre Anwendung angewiesen ist, regelmäßig aktualisieren müssen. Sie können zum Beispiel das `apt-get update` und `apt-get upgrade` Befehle in Ihrem Dockerfile, um Ihren Container mit den neuesten Sicherheitspatches und Fehlerbehebungen auf dem neuesten Stand zu halten.

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
## Weitere Studien
### Docker-Dokumentation
[Docker](https://www.docker.com/) ist eine Open-Source-Plattform für die Erstellung, den Versand und die Ausführung von Anwendungen in Containern. Die Docker-Dokumentationswebsite bietet detaillierte Informationen zur Installation, Konfiguration und Verwendung von Docker für eine Vielzahl von Betriebssystemen und Anwendungsfällen. Die Website enthält auch Informationen über Docker-APIs, Docker-CLI-Befehle und Tipps zur Fehlerbehebung.

Einige nützliche Abschnitte der Docker-Dokumentation umfassen:

- [Get started with Docker](https://docs.docker.com/get-started/)
- [Docker CLI reference](https://docs.docker.com/engine/reference/commandline/cli/)
- [Docker API reference](https://docs.docker.com/engine/api/v1.41/)
- [Docker-compose reference](https://docs.docker.com/compose/compose-file/)
- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

Die Docker-Dokumentation ist eine großartige Ressource, um die Verwendung von Docker zu erlernen und Probleme zu beheben, auf die Sie stoßen könnten.

### Docker Hub
[Docker Hub](https://hub.docker.com/) ist ein Cloud-basiertes Repository, mit dem Sie Docker-Images speichern, freigeben und verwalten können. Docker Hub umfasst öffentliche und private Repositories sowie automatisierte Builds und Workflows. Sie können Docker Hub verwenden, um Ihre eigenen Docker-Images zu speichern und um vorgefertigte Images für beliebte Softwareanwendungen und Tools zu finden.

Einige nützliche Funktionen von Docker Hub sind:

- [Search for Docker images](https://hub.docker.com/search?type=image)
- [Store and manage Docker images in repositories](https://hub.docker.com/repositories)
- [Automate builds and testing with Docker Hub workflows](https://docs.docker.com/docker-hub/builds/)

Docker Hub ist ein unverzichtbares Tool für die Arbeit mit Docker und kann Ihnen viel Zeit und Mühe bei der Verwaltung und Freigabe von Docker-Images ersparen.

## Fazit

Docker ist ein leistungsstarkes Tool, mit dem Sie Ihre Anwendungen portabler, effizienter und einfacher bereitstellen können. Wenn Sie diese bewährten Verfahren und Tipps befolgen, können Sie Docker-Container erstellen, die sicher, einfach zu verwenden und schnell zu implementieren sind. Unabhängig davon, ob Sie eine neue Anwendung erstellen oder eine bestehende Anwendung auf Docker migrieren, werden Ihnen diese Schritte den Einstieg in die Erstellung von Docker-Containern erleichtern.

