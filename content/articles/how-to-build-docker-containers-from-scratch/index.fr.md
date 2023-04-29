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


 **Crear contenedores Docker**
 
 Docker es una potente herramienta que puede utilizarse para crear aplicaciones portátiles y fácilmente desplegables. En esta guía, cubriremos los pasos básicos para crear y construir contenedores Docker. También repasamos algunas buenas prácticas y consejos para asegurarte de que tus contenedores Docker son eficaces, seguros y fáciles de usar.
 
 ## Comprender Docker
 
 Antes de empezar a crear contenedores Docker, es importante entender qué es Docker y cómo funciona.
 
 Docker es una herramienta que te permite agrupar una aplicación y sus dependencias en un contenedor que puede ejecutarse en cualquier sistema. El contenedor está aislado del sistema huésped e incluye todo lo necesario para ejecutar la aplicación, incluyendo el código, el entorno de ejecución, las herramientas del sistema, las bibliotecas y los parámetros.
 
 Los contenedores son grandes y fáciles de manejar, lo que los convierte en una opción popular para crear y gestionar aplicaciones. Con Docker, puede crear, administrar y ejecutar contenedores con una sencilla interfaz de línea de comandos.
 
 ## Construir una imagen Docker
 
 Para crear un contenedor Docker, primero debes crear una imagen Docker. Una imagen Docker es una copia instantánea de un contenedor que incluye todos los archivos, bibliotecas y dependencias necesarias para ejecutar la aplicación.
 
 Estas son las etapas básicas para crear una imagen Docker :
 
 1. **Crear un archivo Docker**.
 2. **Construir la imagen
 3. **Ejecutar el contenedor**
 
 ### Étape 1 : Créer un fichier Dockerfile
 
 La primera etapa para crear una imagen Docker consiste en crear un Dockerfile. Un Dockerfile es un archivo de texto que contiene las instrucciones necesarias para crear una imagen. Vea un ejemplo de Dockerfile simple :
 
 
 Componemos este Dockerfile :
 
 - `FROM ubuntu:latest` especifica la imagen base a utilizar para el contenedor. En este caso, utilizamos la última versión de Ubuntu.
 - `RUN apt-get update && apt-get install -y nginx` actualiza la lista de paquetes e instala el servidor Web nginx.
 - COPIAR index.html /var/www/html/` copia el fichero index.html a la ruta web del navegador.
 - Expone el puerto 80 al servidor.
 - CMD ["nginx", "-g", "daemon off;"]` elimina el servidor nginx y lo ejecuta en primer plano.
 
 ### Étape 2 : Créer l'image
 
 Después de crear el fichero Docker, puedes crear la imagen con la ayuda del comando `docker build`. Vea un ejemplo :
 
 
 Componga este comando :
 
 - `docker run` indica a Docker que ejecute un contenedor.
 - d` ejecuta el contenedor en modo separado, lo que significa que se ejecuta en el plano frontal.
 - p 80:80` asigna el puerto 80 del sistema huésped al puerto 80 del navegador.
 - `my-nginx-image` especifica el nombre de la imagen Docker que se utilizará en el contenedor.
 
 ## Las mejores prácticas
 
 Ahora que ya sabes cómo crear contenedores Docker, revisa algunas buenas prácticas para asegurarte de que tus contenedores Docker son eficientes, seguros y fáciles de usar.
 
 ### Utilizar pequeñas imágenes de base
 
 Para que tus contenedores Docker sean pequeños y rápidos de usar, es preferible que utilices pequeñas imágenes de base que sólo contengan los recursos que tu aplicación necesita. Por ejemplo, en lugar de utilizar un sistema de explotación completo como Ubuntu o CentOS, puedes utilizar una imagen más pequeña como Alpine Linux o BusyBox.
 
 ### Réduire les calques
 
 Cada línea de tu Dockerfile crea una nueva clave en tu imagen Docker, y cada clave aumenta el tamaño de la imagen. Para mantener tus imágenes Docker lo más pequeñas posible, debes minimizar el número de calcos en tu imagen. Una forma de hacerlo consiste en agrupar comandos similares en una única línea de tu archivo Docker. Por ejemplo, en lugar de utilizar dos comandos "RUN" distintos para actualizar la lista de paquetes e instalar un paquete, puedes utilizar un único comando "RUN" para hacer las dos cosas a la vez.
 
 Ej:
 contra
 
 ### Utilizar variables de entorno
 
 El uso de variables de entorno en tu Dockerfile en lugar de valores de codificación facilita la personalización de tu contenedor durante la ejecución y garantiza que tu Dockerfile sea portable. Por ejemplo, puedes utilizar variables de entorno para especificar el puerto en el que se ejecutará tu aplicación o la ubicación de un archivo de configuración.
 
 Ej:
 
 
 ### Utilizar los montajes de volumen
 
 Los montajes de volumen son una forma de compartir datos entre tu sistema host y tu contador Docker. Esto facilita la gestión de datos y reduce el tamaño de su contenedor Docker. Por ejemplo, puedes utilizar un montaje de volumen para compartir un archivo de base de datos entre tu servidor y tu contador.
 
 Ej:
 
 
 ### Évitez d'exécuter en tant que root
 
 La ejecución de su contenedor Docker como usuario root puede suponer un riesgo de seguridad. En lugar de esto, debes crear un nuevo usuario en tu archivo Docker y ejecutar el controlador como usuario. Por ejemplo, puedes usar el comando "USER" en tu Dockerfile para crear un nuevo usuario, y luego pasar a este usuario durante la ejecución del contador.
 
 Ej:
 
 ### Gardez les images à jour
 
 Para asegurarte de que tus contenidos Docker están seguros y libres de vulnerabilidades, es importante mantener al día tus imágenes Docker. Esto significa poner al día regularmente la imagen de base y todas las dependencias que requieran el reposicionamiento de su aplicación. Por ejemplo, puede utilizar los comandos "apt-get update" y "apt-get upgrade" en su archivo Docker para mantener su contenedor actualizado con las últimas correcciones de seguridad y errores.
 
 Ej:
 ## Poursuivez vos études
 ### Docker de documentación
 [Docker](https://www.docker.com/) es una plataforma de código abierto que permite crear, probar y ejecutar aplicaciones en contenedores. El sitio web de documentación de Docker ofrece información detallada sobre la instalación, configuración y uso de Docker para una gran variedad de sistemas operativos y casos de uso. El sitio web también incluye información sobre la API de Docker, los comandos CLI de Docker y consejos de instalación.
 
 Algunas secciones útiles de la documentación de Docker incluyen :
 
 - Comenzando con Docker](https://docs.docker.com/get-started/)
 - Referencia de la CLI de Docker](https://docs.docker.com/engine/reference/commandline/cli/)
 - Referencia a la API de Docker](https://docs.docker.com/engine/api/v1.41/)
 - Referencia Docker-compose](https://docs.docker.com/compose/compose-file/)
 - Referencia Dockerfile](https://docs.docker.com/engine/reference/builder/)
 
 La documentación de Docker es un excelente recurso para aprender a utilizar Docker y para resolver los problemas con los que te puedas encontrar.
 
 ### Estación de acceso al concentrador
 [Docker Hub](https://hub.docker.com/) es una referencia basada en la nube que te permite almacenar, compartir y administrar imágenes Docker. Docker Hub incluye referencias públicas y privadas, así como compilaciones y flujos de trabajo automatizados. Puedes utilizar Docker Hub para almacenar tus propias imágenes Docker, así como para encontrar imágenes predefinidas para aplicaciones logísticas y herramientas populares.
 
 Algunas funcionalidades útiles de Docker Hub incluyen :
 
 - Buscar imágenes Docker](https://hub.docker.com/search?type=image)
 - Almacenamiento y gestión de imágenes Docker en referencias](https://hub.docker.com/repositories)
 - Automatizar compilaciones y pruebas con los flujos de trabajo de Docker Hub](https://docs.docker.com/docker-hub/builds/)
 
 Docker Hub es una herramienta esencial para trabajar con Docker, y puede ahorrarte mucho tiempo y esfuerzo cuando se trata de gestionar y compartir imágenes Docker.
 
 
 ## Conclusión
 
 Docker es una poderosa herramienta que puede ayudarte a hacer tus aplicaciones más portables, eficientes y fáciles de manejar. Siguiendo estas buenas prácticas y estos consejos, puedes crear contenedores Docker seguros, fáciles de usar y rápidos de prevenir. Ya sea que crees una nueva aplicación o que migres una aplicación existente a Docker, estos pasos te permitirán avanzar en la creación de contenedores Docker.
 
