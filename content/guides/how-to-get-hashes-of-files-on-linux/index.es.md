---
title: "Hashes de Archivos Linux: Guía para la obtención de hashes SHA256, MD5 y SHA1 mediante herramientas integradas"
draft: false
toc: true
date: 2023-05-25
description: "Aprenda a obtener hashes SHA256, MD5 y SHA1 de archivos en Linux utilizando herramientas integradas, garantizando la integridad de los datos y la autenticidad de los archivos."
tags: ["Hashes de archivos de Linux", "hash SHA256", "hash MD5", "hash SHA1", "Línea de comandos Linux", "integridad de los archivos", "validación de datos", "Seguridad en Linux", "herramientas integradas", "verificación de archivos", "autenticidad de los datos", "algoritmos hash de archivos", "Administración de sistemas Linux", "herramientas de línea de comandos", "sumas de comprobación de archivos", "Utilidades Linux", "comprobación de la integridad de los archivos", "verificación de la integridad de los datos", "ejemplos de hash de archivos", "Comandos hash de Linux", "métodos hash de archivos", "Medidas de seguridad de Linux", "Protección de datos en Linux", "Gestión de archivos en Linux", "Verificación de archivos en Linux", "Integridad de archivos en Linux", "seguridad de los datos", "Validación de datos en Linux", "Seguridad del sistema Linux", "técnicas de hashing de archivos", "garantía de integridad de los archivos", "validación segura de archivos", "Integridad de datos en Linux"]
cover: "/img/cover/A_digital_representation_of_file_hashes_being_calculated.png"
coverAlt: "Representación digital de hashes de archivos calculados en la pantalla de un terminal Linux, que simboliza la integridad y seguridad de los datos."
coverCaption: ""
---

**Guía: Obteniendo Hashes de Archivos en Linux usando Herramientas Integradas**

## Introducción

En el mundo de los sistemas Linux, obtener hashes de archivos es esencial para asegurar la integridad de los datos y verificar la autenticidad de los archivos. Los hashes de archivos sirven como identificadores únicos que permiten a los usuarios detectar intentos de manipulación y validar la integridad de los datos. En esta completa guía, exploraremos cómo obtener los hashes **SHA256**, **MD5** y **SHA1** de archivos en Linux utilizando herramientas integradas. Siga las instrucciones paso a paso y aprenda a través de ejemplos concretos.

______

## Obteniendo Hashes en Linux usando Herramientas Integradas

Linux proporciona varias herramientas integradas que permiten a los usuarios calcular hashes de archivos sin necesidad de instalar software adicional. Exploraremos tres algoritmos hash ampliamente utilizados: **SHA256**, **MD5**, y **SHA1**.

### Obtención del hash SHA256

Para obtener el hash **SHA256** de un archivo en Linux, puedes usar el comando `sha256sum` comando. Abra un terminal y navegue hasta el directorio donde se encuentra el archivo. A continuación, ejecute el siguiente comando:

```bash
sha256sum file_path
```
Sustituir `file_path` con la ruta real a su archivo.

### Obtención de los hash MD5 y SHA1
También puede obtener los `MD5` y `SHA1 hashes` de un archivo en Linux utilizando comandos similares:

- Para obtener el `MD5 hash`

```bash
md5sum file_path
```

- Para obtener el `SHA1 hash`

```bash
sha1sum file_path
```
Sustituir `file_path` con la ruta a su archivo en ambos comandos.

## Ejemplos
Profundicemos en ejemplos específicos para ilustrar el proceso de obtención de hashes utilizando herramientas integradas en Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Ejemplo 1: Obtención del hash SHA256
Imagine que tiene un fichero llamado `document.pdf` situado en el directorio `/home/user/docs` Para obtener el `SHA256 hash` de este archivo en Linux, ejecute el siguiente comando:

```bash
sha256sum /home/user/docs/document.pdf
```

La salida mostrará el `SHA256 hash` del archivo.

### Ejemplo 2: Obtención del hash MD5

Suponga que tiene un fichero llamado `image.jpg` almacenados en el directorio `/home/user/pictures` Para obtener el `MD5 hash` de este archivo en Linux, ejecute el siguiente comando:

```bash
md5sum /home/user/pictures/image.jpg
```

El terminal mostrará el `MD5 hash` del archivo.

## Ejemplo 3: Obtención del hash SHA1

Considere un escenario en el que tiene un fichero llamado `data.txt` situado en el directorio `/home/user/files` Para obtener el `SHA1 hash` de este archivo en Linux, ejecute el siguiente comando:

```bash
sha1sum /home/user/files/data.txt
```
La salida mostrará el `SHA1 hash` del archivo.

## Conclusión
Obtener hashes de archivos en Linux utilizando herramientas integradas es un método sencillo pero potente para garantizar la integridad de los datos y validar la autenticidad de los archivos. Siguiendo las instrucciones proporcionadas en esta guía, puede calcular con confianza hashes SHA256, MD5 y SHA1 de sus archivos en sistemas Linux.

## Referencias

1. [sha256sum - Linux man page](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linux man page](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linux man page](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
