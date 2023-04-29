---
title: "Construyendo contenedores Docker eficientes y seguros: Guía para principiantes"
date: 2023-02-24
toc: true
draft: false
descripción: "Aprende a crear contenedores Docker eficientes y seguros utilizando las mejores prácticas, consejos e instrucciones paso a paso en esta completa guía."
tags: ["docker", "containers", "containerization", "devops", "deployment", "portability", "efficiency", "security", "best practices", "Dockerfile", "base images", "environment variables", "volume mounts", "root user", "up-to-date images", "software development", "container images", "Docker Hub", "container orchestration", "Kubernetes"].
cover: "/img/cover/A_3D_imagen_animada_de_un_contenedor_seguro_bien_organizado.png"
coverAlt: "Imagen animada en 3D de un contenedor seguro y bien organizado con el logotipo de Docker sobre él, rodeado de diversas herramientas y equipos relacionados con la ingeniería de software y DevOps."
coverCaption: ""
---
```bash
FROM ubuntu:latest
EJECUTAR apt-get update && apt-get install -y nginx
COPIAR index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```
```bash
docker run -d -p 80:80 my-nginx-image
```
``dockerfile
RUN apt update
RUN apt install apache -y
```
``dockerfile
RUN apt update && apt install apache -y
```
``bash
docker run -e PORT=3000 my-app
```
``Dockerfile
DESDE nodo:14

# Establecer el directorio de trabajo
directorio de trabajo /app

# Copiar package.json y yarn.lock al contenedor
COPIAR package.json yarn.lock ./

# Instalar dependencias
EJECUTAR yarn install --frozen-lockfile

# Copiar el código de la aplicación al contenedor
COPIAR . .

# Exponer el puerto de la aplicación
EXPONER $PUERTO

# Iniciar la aplicación
CMD ["yarn", "start"]
```
```bash
docker run -v /home/user/app/data:/app/data my-app
```
```Dockerfile
DESDE nodo:14

# Establecer el directorio de trabajo
directorio de trabajo /app

# Copia los ficheros package.json y yarn.lock al contenedor
COPIAR package.json yarn.lock ./

# Instale las dependencias
EJECUTAR yarn install --frozen-lockfile

# Copiar el resto del código de la aplicación al contenedor
COPIAR . .

# Exponer el puerto de la aplicación
EXPONER 3000

# Iniciar la aplicación
CMD ["yarn", "start"]

# Montar un volumen para los datos de la aplicación
VOLUMEN ["/app/data"]
```
```Dockerfile
DESDE nodo:14

# Crear un nuevo usuario para ejecutar el contenedor
RUN useradd --user-group --create-home --shell /bin/false app

# Cambia el directorio de trabajo al directorio home del usuario app
WORKDIR /home/app

# Instalar dependencias como usuario de app
COPIAR package.json yarn.lock ./
EJECUTAR chown -R app:app /home/app
USUARIO app
EJECUTAR yarn install --frozen-lockfile --production

# Copiar el código de la aplicación como usuario de app
COPIAR --chown=app:app . .

# Exponer el puerto
EXPONER 3000

# Iniciar la aplicación como usuario
CMD ["yarn", "start"]
```
```Dockerfile
FROM ubuntu:latest

# Actualizar la lista de paquetes e instalar las actualizaciones de seguridad
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Instalar el servidor web nginx
RUN apt-get install -y nginx

# Copia el código de la aplicación al contenedor
COPIAR . /var/www/html/

# Exponer el puerto 80 al sistema anfitrión
EXPONER 80

# Iniciar el servidor nginx
CMD ["nginx", "-g", "daemon off;"]

```


 **Para crear un contenedor Docker**
 
 Docker es una herramienta muy fácil de usar, con la que puedes crear aplicaciones sencillas y fáciles de usar. En este artículo describimos los sencillos pasos para crear y gestionar contenedores Docker. También nos centraremos en algunas buenas prácticas y consejos para asegurarnos de que su contenedor Docker es eficaz, seguro y beneficioso.
 
 ## Docker verstehen
 
 Antes de comenzar con la creación de contenedores Docker, es importante saber qué es Docker y cómo funciona.
 
 Docker es una herramienta que permite empaquetar una aplicación y sus características en un contenedor, que se puede instalar en cualquier sistema. El contenedor está aislado del sistema anfitrión y contiene todo lo necesario para el uso de la aplicación, como código, duración, herramientas del sistema, bibliotecas e instalaciones.
 
 Los contenedores son fáciles de instalar, lo que los convierte en una herramienta ideal para la creación y el almacenamiento de aplicaciones. Con Docker puede crear, desplegar y gestionar contenedores con una sencilla interfaz de usuario.
 
 ## Crear una imagen Docker
 
 Para crear un contenedor Docker, primero debe crear una imagen Docker. Una Docker-Image es una instantánea de un contenedor, que contiene todos los datos, bibliotecas y características necesarias para el funcionamiento de la aplicación.
 
 Estos son algunos sencillos pasos para crear una imagen Docker:
 
 1. 1. **Estale una date Docker**.
 2. 2. **Imprimir imagen**
 3. **Solicitar contenedor**
 
 ### Schritt 1: Dockerfile erstellen
 
 El primer paso para crear una imagen Docker es crear un archivo Docker. Un archivo Docker es un archivo de texto que contiene información necesaria para la creación de imágenes. Este es un ejemplo de un archivo Docker sencillo:
 
 
 Déjanos completar este archivo Docker:
 
 - `FROM ubuntu:latest` contiene la imagen base que se utilizará para el contenedor. En este caso utilizamos la última versión de Ubuntu.
 - RUN apt-get update && apt-get install -y nginx` actualiza la lista de paquetes e instala el servidor web nginx.
 - COPIAR index.html /var/www/html/` incluye el archivo index.html en el directorio web del contenedor.
 - EXPOSE 80` habilita el puerto 80 para el sistema anfitrión.
 - CMD ["nginx", "-g", "daemon off;"]` inicia el servidor nginx y lo ejecuta en segundo plano.
 
 ### Schritt 2: Bild erstellen
 
 Una vez que haya creado el fichero Dockerfile, puede crear la imagen con "docker build". Este es un ejemplo:
 
 
 Por favor, comprueba este error:
 
 - "docker run" lleva a Docker a crear un contenedor.
 - El comando `-d` ejecuta el contenedor en el modo seleccionado, lo que significa que se encuentra en el interior.
 - `-p 80:80` ordnet Port 80 dem Hostsystem Port 80 im Container zu.
 - my-nginx-image" es el nombre de la imagen Docker que se utilizará en el contenedor.
 
 ## Configuración estándar
 
 Aunque ahora ya sabe cómo se crean los contenedores Docker, vamos a seguir una serie de buenas prácticas para asegurarle que sus contenedores Docker son eficientes, seguros y útiles.
 
 ### Verwenden Sie kleine Basisbilder
 
 Para preparar su contenedor Docker de forma rápida y sencilla, utilice, en la medida de lo posible, pequeñas imágenes de base que sólo contengan las características que su aplicación requiere. Por ejemplo, si desea utilizar un sistema operativo completo como Ubuntu o CentOS, SIE puede utilizar una imagen pequeña como Alpine Linux o BusyBox.
 
 ### Ebenen minimieren
 
 Cada elemento de su fichero Docker crea una nueva capa en su imagen Docker, y cada capa aumenta el tamaño de la imagen. Para que sus imágenes Docker sean lo más pequeñas posible, debe intentar minimizar el número de campos de su imagen. Una forma de conseguirlo es agrupar diferentes elementos de su archivo Docker en una única zona. Por ejemplo, para actualizar la lista de paquetes e instalar un paquete, puede utilizar dos veces la opción "Ejecutar", para que ambas se actualicen al mismo tiempo.
 
 Ej:
 vs
 
 ### Umgebungsvariablen verwenden
 
 El uso de variables de entorno en su archivo Docker en lugar de valores predeterminados impide que sus contenedores pasen el tiempo de espera y garantiza que su archivo Docker es seguro. En todos los casos, SIE puede utilizar variables de configuración para determinar el puerto en el que se ejecutará su aplicación, o la dirección de una base de datos de configuración.
 
 Ej:
 
 
 ### Volume-Mounts verwenden
 
 Los montajes de volumen son una forma de facilitar el intercambio de datos entre el sistema anfitrión y el contenedor Docker. Esto mejora la gestión de datos y reduce el tamaño de sus contenedores Docker. Por ejemplo, SIE puede montar un volumen para crear un banco de datos entre el sistema host y el contenedor.
 
 Ej:
 
 
 ### Verhindern Sie die Ausführung als Root
 
 El uso de sus contenedores Docker como directorio raíz puede suponer un riesgo de seguridad. En este caso, SIE debe crear un nombre de usuario en su archivo Docker y convertir el contenedor en dicho nombre de usuario. Por ejemplo, SIE puede usar el valor "USER" en su archivo Docker para crear un nuevo contenedor y luego cambiarlo por el contenedor.
 
 Ej:
 
 ### Bilder aktuell halten
 
 Para asegurarse de que sus contenedores Docker son seguros y están libres de errores, es importante mantener sus imágenes Docker en el soporte más reciente. Esto significa que la. Basisimage y todas las características que su uso requiera se actualicen periódicamente. Por ejemplo, puede utilizar las funciones "apt-get update" y "apt-get upgrade" en su base de datos para mantener su contenedor con los últimos parches de seguridad y errores.
 
 Ej:
 ## Vertiefen Sie Ihr Studium
 ### Documentación de Docker
 [Docker](https://www.docker.com/) es una plataforma de código abierto para crear, distribuir y utilizar aplicaciones en contenedores. El sitio web de documentación de Docker ofrece información detallada sobre la instalación, configuración y uso de Docker en una gran variedad de sistemas operativos y campos de aplicación. El sitio web también contiene información sobre Docker-APIs, Docker-CLI-Befehlen y consejos para solucionar problemas.
 
 Se incluyen algunos fragmentos interesantes de la documentación de Docker:
 
 - Primeros pasos con Docker](https://docs.docker.com/get-started/)
 - Referencia Docker-CLI] (https://docs.docker.com/engine/reference/commandline/cli/)
 - Referencia Docker-API](https://docs.docker.com/engine/api/v1.41/)
 - Referencia de Docker-Compose] (https://docs.docker.com/compose/compose-file/)
 - Dockerfile-Referenz](https://docs.docker.com/engine/reference/builder/)
 
 La documentación de Docker es un recurso muy útil para entender el uso de Docker y resolver los problemas que puedan surgir.
 
 ### Docker-Hub
 [Docker Hub](https://hub.docker.com/) es un repositorio basado en la nube, con el que puedes seleccionar, liberar y descargar imágenes Docker. Docker Hub ofrece repositorios independientes y privados, así como compilaciones y flujos de trabajo automatizados. Puede utilizar Docker Hub para seleccionar sus propias imágenes Docker y para encontrar imágenes disponibles para sus aplicaciones de software y herramientas.
 
 Algunas funciones útiles de Docker Hub son:
 
 - [Ir a Imágenes Docker](https://hub.docker.com/search?type=image)
 - Docker-Images in Repositories speichern and verwalten](https://hub.docker.com/repositories)
 - Builds and Tests with Docker Hub-Workflows automatisieren](https://docs.docker.com/docker-hub/builds/)
 
 Docker Hub es una herramienta única para el trabajo con Docker que le ahorrará mucho tiempo y dinero a la hora de gestionar y utilizar conjuntamente imágenes Docker.
 
 
 ## Inicio
 
 Docker es una herramienta muy sencilla con la que podrá gestionar sus aplicaciones de forma más fácil, eficiente y sencilla. Si sigue estos consejos y buenas prácticas, podrá crear contenedores Docker seguros, fáciles de usar y rápidos de instalar. Independientemente de si está creando una nueva aplicación o migrando una existente a Docker, le ayudamos a crear sus propios contenedores Docker.
 
