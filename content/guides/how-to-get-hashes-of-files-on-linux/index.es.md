---
title: "Guía de Hash de Archivos en Linux 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: Guía completa 2026 para el hash de archivos en Linux usando los comandos sha256sum, md5sum, sha1sum. Aprende verificación de integridad de archivos, comparación de hashes, automatización y mejores prácticas para seguridad.
tags:
- Hashes de archivos en Linux
- Hash SHA256
- Hash MD5
- Hash SHA1
- Línea de comandos de Linux
- integridad de archivos
- validación de datos
- seguridad en Linux
- herramientas integradas
- verificación de archivos
- autenticidad de datos
- algoritmos de hash de archivos
- administración de sistemas Linux
- herramientas de línea de comandos
- sumas de verificación de archivos
- utilidades de Linux
- chequeos de integridad de archivos
- verificación de integridad de datos
- ejemplos de hash de archivos
- comandos de hash en Linux
- métodos de hash de archivos
- medidas de seguridad en Linux
- protección de datos en Linux
- gestión de archivos en Linux
- verificación de archivos en Linux
- integridad de archivos en Linux
- seguridad de datos
- validación de datos en Linux
- seguridad del sistema Linux
- técnicas de hash de archivos
- garantía de integridad de archivos
- validación segura de archivos
- integridad de datos en Linux
- sha256sum
- md5sum
- sha1sum
- hash de archivo linux
- obtener hash de archivo linux
- linux obtener hash de archivo
- linux hacer hash a un archivo
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: Una ilustración de un terminal Linux futurista mostrando salidas de comandos de hash, rodeado de archivos abstractos y símbolos digitales sobre un fondo oscuro, con acentos vibrantes en azul, verde y púrpura.
coverCaption: ''
---

**Guía: Obtención de Hashes de Archivos en Linux usando Herramientas Integradas**

## Introducción

En el mundo de los sistemas Linux, obtener hashes de archivos es esencial para asegurar la integridad de los datos y verificar la autenticidad de los archivos. Los hashes de archivos sirven como identificadores únicos que permiten a los usuarios detectar intentos de manipulación y validar la integridad de los datos. En esta guía completa, exploraremos cómo obtener hashes **SHA256**, **MD5** y **SHA1** de archivos en Linux usando herramientas integradas. Sigue las instrucciones paso a paso y aprende con ejemplos específicos.

______

## Obtención de Hashes en Linux usando Herramientas Integradas

Linux proporciona varias herramientas integradas que permiten a los usuarios calcular hashes de archivos sin necesidad de instalar software adicional. Exploraremos tres algoritmos de hash ampliamente usados: **SHA256**, **MD5** y **SHA1**.

### Obtención del Hash SHA256

Para obtener el **hash SHA256** de un archivo en Linux, puedes usar el comando `sha256sum`. Abre una terminal y navega al directorio donde se encuentra el archivo. Luego, ejecuta el siguiente comando:

```bash
sha256sum file_path
```
Reemplaza `file_path` con la ruta real de tu archivo.

### Obtención de los Hashes MD5 y SHA1
También puedes obtener los `MD5` y `SHA1 hashes` de un archivo en Linux usando comandos similares:

- Para obtener el `MD5 hash`:

```bash
md5sum file_path
```

- Para obtener el `SHA1 hash`:

```bash
sha1sum file_path
```
Reemplaza `file_path` con la ruta a tu archivo en ambos comandos.

## Ejemplos
Vamos a profundizar en ejemplos específicos para ilustrar el proceso de obtención de hashes usando herramientas integradas en Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Ejemplo 1: Obtención del Hash SHA256
Imagina que tienes un archivo llamado `document.pdf` ubicado en el directorio `/home/user/docs`. Para obtener el `SHA256 hash` de este archivo en Linux, ejecuta el siguiente comando:

```bash
sha256sum /home/user/docs/document.pdf
```

La salida mostrará el valor `SHA256 hash` del archivo.

### Ejemplo 2: Obtención del Hash MD5

Supongamos que tienes un archivo llamado `image.jpg` almacenado en el directorio `/home/user/pictures`. Para obtener el `MD5 hash` de este archivo en Linux, ejecuta el siguiente comando:

```bash
md5sum /home/user/pictures/image.jpg
```

El terminal mostrará el valor `MD5 hash` del archivo.

## Ejemplo 3: Obtención del Hash SHA1

Considera un escenario donde tienes un archivo llamado `data.txt` ubicado en el directorio `/home/user/files`. Para obtener el `SHA1 hash` de este archivo en Linux, ejecuta el siguiente comando:

```bash
sha1sum /home/user/files/data.txt
```
La salida mostrará el valor `SHA1 hash` del archivo.

______

## Operaciones Avanzadas de Hash en Linux

### Hashear Múltiples Archivos a la Vez

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### Crear un Archivo Manifiesto de Hashes

Genera un archivo que contenga hashes para verificación posterior:

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

Salida cuando los archivos coinciden:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### Comparar Hash contra Valor Esperado

```bash
# Method 1: Manual comparison
expected_hash="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
actual_hash=$(sha256sum /path/to/file | awk '{print $1}')

if [ "$actual_hash" == "$expected_hash" ]; then
    echo "✓ File verified - hash matches"
else
    echo "✗ WARNING: Hash mismatch!"
fi
```

``` bash
# Method 2: Using echo and checking
echo "$expected_hash  /path/to/file" | sha256sum -c -
```

### Hash desde Entrada Estándar

```bash
# Hash text directly
echo -n "Hello World" | sha256sum

# Hash command output
cat /etc/passwd | sha256sum

# Hash without trailing newline (important!)
echo -n "text" | sha256sum  # Correct
echo "text" | sha256sum     # Different hash (includes newline)
```

______

## Casos Prácticos

### 1. Verificar ISOs Descargados

Las distribuciones Linux proporcionan sumas de verificación para validar descargas:

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. Detectar Manipulación de Archivos

Monitorea archivos críticos del sistema:

```bash
# Create baseline
sudo sha256sum /etc/passwd /etc/shadow /etc/sudoers > /secure/baseline-hashes.txt

# Later, check for changes
sudo sha256sum -c /secure/baseline-hashes.txt

# Script for monitoring
#!/bin/bash
if ! sudo sha256sum -c /secure/baseline-hashes.txt > /dev/null 2>&1; then
    echo "ALERT: System files modified!" | mail -s "Security Alert" admin@example.com
fi
```

### 3. Deduplificar Archivos

Encuentra archivos duplicados usando hashes:

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. Verificar Integridad de Copias de Seguridad

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## Scripts de Automatización

### Script 1: Generador Recursivo de Hashes

```bash
#!/bin/bash
# hash-directory.sh
# Usage: ./hash-directory.sh /path/to/directory

if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"
output="hashes-$(date +%Y%m%d-%H%M%S).txt"

echo "Generating SHA256 hashes for: $directory"
find "$directory" -type f -exec sha256sum {} \; > "$output"
echo "✓ Saved $(wc -l < "$output") file hashes to: $output"
```

### Script 2: Herramienta de Verificación de Hashes

```bash
#!/bin/bash
# verify-hashes.sh
# Usage: ./verify-hashes.sh checksums.txt

if [ ! -f "$1" ]; then
    echo "Error: Checksum file not found"
    exit 1
fi

echo "Verifying file integrity..."
if sha256sum -c "$1" 2>/dev/null; then
    echo "✓ All files verified successfully"
    exit 0
else
    echo "✗ Some files failed verification"
    exit 1
fi
```

### Script 3: Verificación de Descargas

```bash
#!/bin/bash
# verify-download.sh <file> <expected-sha256>

file="$1"
expected="$2"

if [ ! -f "$file" ]; then
    echo "Error: File not found"
    exit 1
fi

actual=$(sha256sum "$file" | awk '{print $1}')

if [ "$actual" == "$expected" ]; then
    echo "✓ Download verified - SHA256 matches"
    exit 0
else
    echo "✗ DANGER: SHA256 mismatch!"
    echo "Expected: $expected"
    echo "Actual:   $actual"
    exit 1
fi
```

______

## Optimización de Rendimiento

### Hashear Archivos Grandes Eficientemente

Para archivos muy grandes, puedes monitorear el progreso:

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### Hash en Paralelo

Hashea múltiples archivos en paralelo usando GNU Parallel:

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### Benchmark de Algoritmos de Hash

```bash
# Compare speed of different algorithms
time sha256sum large-file.bin
time sha1sum large-file.bin
time md5sum large-file.bin

# Typical results (1GB file):
# MD5:    ~1-2 seconds (fastest, insecure)
# SHA1:   ~2-3 seconds (deprecated)
# SHA256: ~3-5 seconds (recommended)
```

______

## Comparación de Seguridad de Algoritmos de Hash

| Algoritmo | Longitud del Hash | Estado 2026 | Caso de Uso |
|-----------|-------------------|-------------|-------------|
| **SHA-256** | 256 bits (64 caracteres) | ✅ Seguro | Recomendado para todos los fines de seguridad |
| **SHA-512** | 512 bits (128 caracteres) | ✅ Seguro | Seguridad extra para datos sensibles |
| **SHA-1** | 160 bits (40 caracteres) | ⚠️ Obsoleto | Solo para compatibilidad heredada |
| **MD5** | 128 bits (32 caracteres) | ❌ Roto | Solo para fines no relacionados con seguridad |

**Recomendación 2026**: Usa siempre SHA-256 o SHA-512 para aplicaciones críticas de seguridad.

______

## Integración con Gestores de Paquetes

### Verificar Paquetes APT (Debian/Ubuntu)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### Verificar Paquetes RPM (Fedora/RHEL)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## Mejores Prácticas para 2026

1. **Usa SHA-256 por defecto**: Es el estándar actual de seguridad
2. **Evita MD5 y SHA-1 para seguridad**: Solo para compatibilidad heredada
3. **Usa siempre la bandera `-c` para verificación**: `sha256sum -c checksums.txt`
4. **Almacena sumas de verificación por separado**: No guardes hashes junto con los archivos que verifican
5. **Usa `-b` para modo binario**: `sha256sum -b file.bin` (importante en algunos sistemas)
6. **Automatiza la verificación**: Crea tareas cron para monitoreo crítico de archivos
7. **Usa `--quiet` en scripts**: Suprime mensajes OK con `sha256sum -c --quiet`

______

## Solución de Problemas

### "No existe el archivo o directorio"

**Solución**: Usa comillas para rutas con espacios:
```bash
sha256sum "/path/with spaces/file.txt"
```

### "ADVERTENCIA: X líneas están mal formateadas"

**Solución**: El formato del archivo de suma debe ser:
```
hash_value  filename
```
Nota las dos espacios entre el hash y el nombre del archivo.

### Permiso Denegado

**Solución**: Usa sudo para archivos del sistema:
```bash
sudo sha256sum /etc/shadow
```

______

## Verificación Multiplataforma

### Verificar Hashes de Linux en Windows

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### Verificar Hashes de Linux en macOS

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## Conclusión

Linux ofrece potentes herramientas integradas (`sha256sum`, `md5sum`, `sha1sum`) para el hash de archivos. Ya sea que estés verificando descargas, monitoreando integridad de archivos, detectando duplicados o asegurando la validez de copias de seguridad, dominar estos comandos es esencial para la administración del sistema y la seguridad en 2026.

**puntos principales:**
- Use **sha256sum** para todos los hash relacionados con la seguridad
- Cree manifiestos de hash con `sha256sum * > checksums.txt`
- Verifique archivos con `sha256sum -c checksums.txt`
- Automatice la verificación de hash en scripts para archivos críticos
- Evite MD5 y SHA-1 para propósitos de seguridad

## Referencias

1. [sha256sum - página man de Linux](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - página man de Linux](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - página man de Linux](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - Checksums](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [Funciones Hash de NIST](https://csrc.nist.gov/projects/hash-functions)
