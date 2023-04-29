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

**Cómo construir contenedores Docker

Docker es una poderosa herramienta que se puede utilizar para crear aplicaciones portátiles y fácilmente desplegables. En esta guía, cubriremos los pasos básicos para crear y construir contenedores Docker. También repasaremos algunas de las mejores prácticas y consejos para asegurar que tus contenedores Docker sean eficientes, seguros y fáciles de usar.

## Entendiendo Docker

Antes de empezar a construir contenedores Docker, es importante entender qué es Docker y cómo funciona.

Docker es una herramienta que te permite empaquetar una aplicación y sus dependencias en un contenedor que puede ejecutarse en cualquier sistema. El contenedor está aislado del sistema anfitrión e incluye todo lo necesario para ejecutar la aplicación, incluido el código, el tiempo de ejecución, las herramientas del sistema, las bibliotecas y la configuración.

Los contenedores son ligeros y fáciles de desplegar, lo que los convierte en una opción popular para crear y desplegar aplicaciones. Con Docker, puede crear, gestionar y ejecutar contenedores con una sencilla interfaz de línea de comandos.

## Creación de una imagen Docker

Para construir un contenedor Docker, primero necesitas crear una imagen Docker. Una imagen Docker es una instantánea de un contenedor que incluye todos los archivos, librerías y dependencias necesarias para ejecutar la aplicación.

Estos son los pasos básicos para crear una imagen Docker:

1. **Crear un archivo Docker**.
2. **Construir la imagen**.
3. **Ejecutar el contenedor

### Paso 1: Crear un Dockerfile

El primer paso para construir una imagen Docker es crear un Dockerfile. Un Dockerfile es un archivo de texto que contiene las instrucciones necesarias para construir la imagen. Aquí tienes un ejemplo de un Dockerfile sencillo:

```bash
FROM ubuntu:latest
EJECUTAR apt-get update && apt-get install -y nginx
COPIAR index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Vamos a desglosar este Dockerfile:

- `FROM ubuntu:latest` especifica la imagen base a utilizar para el contenedor. En este caso, estamos usando la última versión de Ubuntu.
- `RUN apt-get update && apt-get install -y nginx` actualiza la lista de paquetes e instala el servidor web nginx.
- `COPY index.html /var/www/html/` copia el archivo index.html a la raíz web del contenedor.
- EXPOSE 80` expone el puerto 80 al sistema anfitrión.
- `CMD ["nginx", "-g", "daemon off;"]` inicia el servidor nginx y lo ejecuta en primer plano.

### Paso 2: Construir la imagen

Después de haber creado el Dockerfile, puedes construir la imagen usando el comando `docker build`. Aquí tienes un ejemplo:

```bash
docker run -d -p 80:80 my-nginx-image
```

Vamos a desglosar este comando:

- `docker run` le dice a Docker que ejecute un contenedor.
- `-d` ejecuta el contenedor en modo separado, lo que significa que se ejecuta en segundo plano.
- `-p 80:80` asigna el puerto 80 en el sistema anfitrión al puerto 80 en el contenedor.
- `my-nginx-image` especifica el nombre de la imagen Docker a utilizar para el contenedor.

## Mejores prácticas

Ahora que sabes cómo construir contenedores Docker, vamos a repasar algunas de las mejores prácticas para asegurar que tus contenedores Docker son eficientes, seguros y fáciles de usar.

### Use Imágenes Base Pequeñas

Para mantener tus contenedores Docker pequeños y rápidos de desplegar, es mejor utilizar imágenes base pequeñas que sólo contengan las dependencias que tu aplicación necesita. Por ejemplo, en lugar de utilizar un sistema operativo completo como Ubuntu o CentOS, puede utilizar una imagen más pequeña como Alpine Linux o BusyBox.

### Minimizar Capas

Cada línea en tu Dockerfile crea una nueva capa en tu imagen Docker, y cada capa aumenta el tamaño de la imagen. Para mantener tus imágenes Docker tan pequeñas como sea posible, deberías intentar minimizar el número de capas en tu imagen. Una forma de hacerlo es agrupar comandos similares en una sola línea en tu Dockerfile. Por ejemplo, en lugar de utilizar dos comandos `RUN` separados para actualizar la lista de paquetes e instalar un paquete, puedes utilizar un único comando `RUN` para hacer ambas cosas al mismo tiempo.

Ej:
``archivocker
RUN apt update
RUN apt install apache -y
```
vs
Archivo apcker
RUN apt update && apt install apache -y
```

### Usar Variables de Entorno

El uso de variables de entorno en tu Dockerfile en lugar de valores codificados hace que sea más fácil personalizar tu contenedor en tiempo de ejecución y asegura que tu Dockerfile es portable. Por ejemplo, puede utilizar variables de entorno para especificar el puerto en el que se ejecuta su aplicación o la ubicación de un archivo de configuración.

Ej:
```bash
docker run -e PUERTO=3000 mi-aplicación
```
```Dockerfile
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


### Utilizar montajes por volumen

Los montajes de volumen son una forma de compartir datos entre tu sistema anfitrión y tu contenedor Docker. Esto facilita la gestión de datos y reduce el tamaño de su contenedor Docker. Por ejemplo, puede utilizar un montaje de volumen para compartir un archivo de base de datos entre su sistema host y su contenedor.

Ej:
```bash
docker run -v /home/usuario/app/data:/app/data mi-app
```

```Dockerfile
DESDE nodo:14

# Establece el directorio de trabajo
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
CMD ["hilo", "iniciar"]

# Montar un volumen para los datos de la aplicación
VOLUMEN ["/app/data"]
```

### Evitar Ejecutar como Root

Ejecutar tu contenedor Docker como usuario root puede suponer un riesgo de seguridad. En su lugar, debe crear un nuevo usuario en su Dockerfile y ejecutar el contenedor como ese usuario. Por ejemplo, puede utilizar el comando `USER` en su Dockerfile para crear un nuevo usuario y luego cambiar a ese usuario al ejecutar el contenedor.

Ej:
```Dockerfile
FROM nodo:14

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

### Mantener imágenes actualizadas

Para asegurar que tus contenedores Docker son seguros y libres de vulnerabilidades, es importante mantener tus imágenes Docker actualizadas. Esto significa actualizar regularmente la imagen base y cualquier dependencia de la que dependa tu aplicación. Por ejemplo, puedes utilizar los comandos `apt-get update` y `apt-get upgrade` en tu Dockerfile para mantener tu contenedor actualizado con los últimos parches de seguridad y correcciones de errores.

Ej:
```Dockerfile
FROM ubuntu:latest

# Actualizar la lista de paquetes e instalar las actualizaciones de seguridad
EJECUTE apt-get update && apt-get upgrade -y && apt-get clean

# Instalar el servidor web nginx
EJECUTAR apt-get install -y nginx

# Copia el código de la aplicación al contenedor
COPIAR . /var/www/html/

# Exponer el puerto 80 al sistema anfitrión
EXPONER 80

# Iniciar el servidor nginx
CMD ["nginx", "-g", "daemon off;"]

```
## Profundiza en tus estudios
### Documentación de Docker
[Docker](https://www.docker.com/) es una plataforma de código abierto para construir, enviar y ejecutar aplicaciones en contenedores. El sitio web de documentación de Docker proporciona información detallada sobre cómo instalar, configurar y utilizar Docker para una variedad de sistemas operativos y casos de uso. El sitio web también incluye información sobre las API de Docker, los comandos de la CLI de Docker y consejos para la resolución de problemas.

Algunas secciones útiles de la documentación de Docker incluyen:

- Introducción a Docker](https://docs.docker.com/get-started/)
- Referencia de la CLI de Docker](https://docs.docker.com/engine/reference/commandline/cli/)
- Referencia de la API de Docker](https://docs.docker.com/engine/api/v1.41/)
- Referencia de Docker-compose](https://docs.docker.com/compose/compose-file/)
- Referencia de Dockerfile](https://docs.docker.com/engine/reference/builder/)

La documentación de Docker es un gran recurso para aprender a usar Docker y para solucionar cualquier problema que puedas encontrar.

### Docker Hub
[Docker Hub](https://hub.docker.com/) es un repositorio basado en la nube que permite almacenar, compartir y gestionar imágenes Docker. Docker Hub incluye repositorios públicos y privados, así como compilaciones y flujos de trabajo automatizados. Puedes utilizar Docker Hub para almacenar tus propias imágenes Docker, así como para encontrar imágenes pre-construidas para aplicaciones de software y herramientas populares.

Algunas características útiles de Docker Hub incluyen:

- Búsqueda de imágenes Docker](https://hub.docker.com/search?type=image)
- Almacenar y gestionar imágenes Docker en repositorios](https://hub.docker.com/repositories)
- Automatizar compilaciones y pruebas con flujos de trabajo de Docker Hub](https://docs.docker.com/docker-hub/builds/)

Docker Hub es una herramienta esencial para trabajar con Docker, y puede ahorrarte mucho tiempo y esfuerzo a la hora de gestionar y compartir imágenes Docker.


## Conclusión

Docker es una poderosa herramienta que puede ayudar a que sus aplicaciones sean más portátiles, eficientes y fáciles de implementar. Siguiendo estas mejores prácticas y consejos, puedes crear contenedores Docker que sean seguros, fáciles de usar y rápidos de desplegar. Tanto si estás creando una nueva aplicación como migrando una existente a Docker, estos pasos te ayudarán a empezar a crear contenedores Docker.

