---
title: "Guía completa: Hashes de Archivos en Windows usando PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Aprenda a obtener hashes de archivos en Windows mediante PowerShell, incluidos SHA256, MD5 y SHA1, con instrucciones paso a paso y ejemplos."
tags: ["hash de archivos", "PowerShell", "hash SHA256", "hash MD5", "hash SHA1", "integridad de los archivos", "autenticación de datos", "verificación de archivos", "algoritmos hash", "Sistema operativo Windows", "lenguaje de programación", "shell de línea de comandos", "seguridad de los datos", "informática forense", "ciberseguridad", "cálculo de hash", "manipulación de archivos", "integridad de los datos", "autenticidad del expediente", "Seguridad de Windows", "identificación de ficheros", "ciberdefensa", "seguridad de archivos", "protección de datos", "verificación de datos", "validación de archivos", "Windows PowerShell", "generación de hash", "algoritmos hash", "funciones hash"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "Ilustración de dibujos animados que muestra un archivo con el símbolo de un candado y una lupa, representando la verificación y seguridad del hash de un archivo."
coverCaption: ""
---

**Cómo obtener hash de archivos en Windows usando PowerShell**

En el ámbito de la seguridad informática, la obtención de hashes de archivos es un paso crucial para garantizar la integridad de los datos y verificar la autenticidad de los archivos. Los hash son identificadores únicos generados para archivos, que permiten a los usuarios detectar intentos de manipulación y validar la integridad de los datos. En esta completa guía, exploraremos el proceso de obtención de hashes **SHA256**, **MD5** y **SHA1** de archivos en Windows utilizando el potente lenguaje de scripting **PowerShell**. Siga las instrucciones paso a paso y profundice en ejemplos específicos. ¡Vamos a empezar!

______

## Obteniendo Hashes en Windows usando PowerShell

PowerShell, un versátil lenguaje de scripting y shell de línea de comandos para Windows, ofrece el cmdlet **Get-FileHash**, que permite a los usuarios calcular el hash de un archivo sin esfuerzo.

### Obtención del hash SHA256

Para obtener el **hash SHA256** de un archivo mediante PowerShell, siga estos sencillos pasos:

1. Inicie PowerShell abriendo el **menú Inicio**, buscando **PowerShell** y seleccionando **Windows PowerShell**.
2. Navegue hasta el directorio donde se encuentra el archivo. Utilice el botón `cd` seguido de la ruta al directorio.
3. Ejecute el siguiente comando para obtener el hash SHA256 del archivo:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Obtención de los hash MD5 y SHA1
También puede obtener los hash `MD5` y `SHA1` hashes de un archivo utilizando PowerShell. Utilice los siguientes comandos:

- Para obtener el `MD5 hash`
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- Para obtener el `SHA1 hash`

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Recuerde sustituir "ruta_archivo" por la ruta de su archivo en ambos comandos.

## Ejemplos
Profundicemos en ejemplos concretos para ilustrar el proceso de obtención de hashes mediante PowerShell en Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Ejemplo 1: Obtención del hash SHA256
Imagine que tiene un fichero llamado `document.pdf` situado en el directorio `C:\Files` Para obtener el `SHA256 hash` de este archivo mediante PowerShell, ejecute el siguiente comando:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

La salida mostrará el valor hash SHA256 del archivo.

### Ejemplo 2: Obtención del hash MD5

Suponga que posee un fichero llamado `image.jpg` almacenados en el directorio `C:\Photos` Para obtener el `MD5 hash` de este archivo mediante PowerShell, ejecute el siguiente comando:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

El terminal mostrará el valor hash MD5 del archivo.

### Ejemplo 3: Obtención del hash SHA1

Considere un escenario en el que tiene un fichero llamado `data.txt` situado en el directorio `C:\Documents` Para obtener el `SHA1 hash` de este archivo mediante PowerShell, ejecute el siguiente comando:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

La salida mostrará el valor hash SHA1 del archivo.