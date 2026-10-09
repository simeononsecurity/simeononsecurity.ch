---
title: "Guia de Hash de Fitxers Linux 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: Guia completa 2026 per a hash de fitxers Linux utilitzant les ordres sha256sum, md5sum, sha1sum. Apreneu la verificació de la integritat dels fitxers, la comparació de hash, l'automatització i les millors pràctiques per a la seguretat.
tags:
- Hashs de fitxers Linux
- Hash SHA256
- Hash MD5
- Hash SHA1
- Línia d'ordres Linux
- integritat del fitxer
- validació de dades
- seguretat Linux
- eines integrades
- verificació de fitxers
- autenticitat de dades
- algorismes de hash de fitxers
- administració del sistema Linux
- eines de línia d'ordres
- sumes de comprovació de fitxers
- utilitats Linux
- comprovacions d'integritat de fitxers
- verificació d'integritat de dades
- exemples de hash de fitxers
- comandes de hash Linux
- mètodes de hash de fitxers
- mesures de seguretat Linux
- protecció de dades Linux
- gestió de fitxers Linux
- verificació de fitxers Linux
- integritat de fitxers Linux
- seguretat de dades
- validació de dades Linux
- seguretat del sistema Linux
- tècniques de hash de fitxers
- assegurament de la integritat de fitxers
- validació segura de fitxers
- integritat de dades Linux
- sha256sum
- md5sum
- sha1sum
- hash de fitxer linux
- obtenir hash de fitxer linux
- linux obtenir hash de fitxer
- linux fer hash a un fitxer
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: Una il·lustració d'un terminal Linux futurista mostrant sortides de comandes de hash, envoltat de fitxers abstractes i símbols digitals sobre un fons fosc, amb accents vibrants en blau, verd i porpra.
coverCaption: ''
---

**Guia: Obtenir Hashs de Fitxers a Linux utilitzant Eines Integrades**

## Introducció

En el món dels sistemes Linux, obtenir hashs de fitxers és essencial per garantir la integritat de les dades i verificar l'autenticitat dels fitxers. Els hashs de fitxers serveixen com a identificadors únics que permeten als usuaris detectar intents de manipulació i validar la integritat de les dades. En aquesta guia completa, explorarem com obtenir hashs **SHA256**, **MD5** i **SHA1** de fitxers a Linux utilitzant eines integrades. Seguiu les instruccions pas a pas i apreneu amb exemples específics.

______

## Obtenir Hashs a Linux utilitzant Eines Integrades

Linux proporciona diverses eines integrades que permeten als usuaris calcular hashs de fitxers sense necessitat d'instal·lar programari addicional. Explorarem tres algorismes de hash àmpliament utilitzats: **SHA256**, **MD5** i **SHA1**.

### Obtenir el Hash SHA256

Per obtenir el **hash SHA256** d'un fitxer a Linux, podeu utilitzar la comanda `sha256sum`. Obriu un terminal i navegueu al directori on es troba el fitxer. A continuació, executeu la comanda següent:

```bash
sha256sum file_path
```
Substituïu `file_path` per la ruta real del vostre fitxer.

### Obtenir els Hashs MD5 i SHA1
També podeu obtenir els `MD5` i `SHA1 hashes` d'un fitxer a Linux utilitzant comandes similars:

- Per obtenir el `MD5 hash`:

```bash
md5sum file_path
```

- Per obtenir el `SHA1 hash`:

```bash
sha1sum file_path
```
Substituïu `file_path` per la ruta del vostre fitxer en ambdues comandes.

## Exemples
Anem a aprofundir en exemples específics per il·lustrar el procés d'obtenció de hashs utilitzant eines integrades a Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Exemple 1: Obtenir Hash SHA256
Imagineu que teniu un fitxer anomenat `document.pdf` situat al directori `/home/user/docs`. Per obtenir el `SHA256 hash` d'aquest fitxer a Linux, executeu la comanda següent:

```bash
sha256sum /home/user/docs/document.pdf
```

La sortida mostrarà el valor `SHA256 hash` del fitxer.

### Exemple 2: Obtenir Hash MD5

Suposem que teniu un fitxer anomenat `image.jpg` emmagatzemat al directori `/home/user/pictures`. Per obtenir el `MD5 hash` d'aquest fitxer a Linux, executeu la comanda següent:

```bash
md5sum /home/user/pictures/image.jpg
```

El terminal mostrarà el valor `MD5 hash` del fitxer.

## Exemple 3: Obtenir Hash SHA1

Considereu un escenari on teniu un fitxer anomenat `data.txt` situat al directori `/home/user/files`. Per obtenir el `SHA1 hash` d'aquest fitxer a Linux, executeu la comanda següent:

```bash
sha1sum /home/user/files/data.txt
```
La sortida mostrarà el valor `SHA1 hash` del fitxer.

______

## Operacions Avançades de Hash a Linux

### Hash de Múltiples Fitxers alhora

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### Crear un Fitxer Manifest de Hash

Genereu un fitxer que contingui hashs per a la verificació posterior:

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

Sortida quan els fitxers coincideixen:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### Comparar Hash amb Valor Esperat

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

### Hash des de l'Entrada Estàndard

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

## Casos d'Ús Pràctics

### 1. Verificar ISOs descarregats

Les distribucions Linux proporcionen sumes de comprovació per verificar les descàrregues:

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. Detectar Manipulació de Fitxers

Superviseu fitxers crítics del sistema:

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

### 3. Deduplificar Fitxers

Trobeu fitxers duplicats utilitzant hashs:

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. Verificar la Integritat de Còpies de Seguretat

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## Scripts d'Automatització

### Script 1: Generador Recursiu de Hash

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

### Script 2: Eina de Verificació de Hash

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

### Script 3: Verificació de Descàrregues

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

## Optimització del Rendiment

### Hash de Fitxers Grans de Forma Eficaç

Per a fitxers molt grans, podeu monitoritzar el progrés:

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### Hash en Paral·lel

Hash de múltiples fitxers en paral·lel utilitzant GNU Parallel:

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### Benchmark d'Algorismes de Hash

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

## Comparació de Seguretat d'Algorismes de Hash

| Algorisme | Longitud del Hash | Estat 2026 | Cas d'Ús |
|-----------|-------------------|------------|----------|
| **SHA-256** | 256 bits (64 caràcters) | ✅ Segur | Recomanat per a tots els usos de seguretat |
| **SHA-512** | 512 bits (128 caràcters) | ✅ Segur | Seguretat extra per a dades sensibles |
| **SHA-1** | 160 bits (40 caràcters) | ⚠️ Obsolet | Només per compatibilitat antiga |
| **MD5** | 128 bits (32 caràcters) | ❌ Trencat | Només per usos no segurs |

**Recomanació 2026**: Utilitzeu sempre SHA-256 o SHA-512 per a aplicacions crítiques de seguretat.

______

## Integració amb Gestors de Paquets

### Verificar Paquets APT (Debian/Ubuntu)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### Verificar Paquets RPM (Fedora/RHEL)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## Millors Pràctiques per a 2026

1. **Utilitzeu SHA-256 per defecte**: És l'estàndard de seguretat actual
2. **Eviteu MD5 i SHA-1 per seguretat**: Només per compatibilitat antiga
3. **Utilitzeu sempre la bandera `-c` per a la verificació**: `sha256sum -c checksums.txt`
4. **Emmagatzemeu les sumes de comprovació per separat**: No guardeu els hashs amb els fitxers que verifiquen
5. **Utilitzeu `-b` per al mode binari**: `sha256sum -b file.bin` (important en alguns sistemes)
6. **Automatitzeu la verificació**: Creeu tasques cron per a la supervisió de fitxers crítics
7. **Utilitzeu `--quiet` en scripts**: Suprimiu missatges OK amb `sha256sum -c --quiet`

______

## Resolució de Problemes

### "No existeix el fitxer o directori"

**Solució**: Utilitzeu cometes per a rutes amb espais:
```bash
sha256sum "/path/with spaces/file.txt"
```

### "AVÍS: X línies estan mal formatades"

**Solució**: El fitxer de suma de comprovació ha de tenir el format:
```
hash_value  filename
```
Fixeu-vos en els dos espais entre el hash i el nom del fitxer.

### Permís Denegat

**Solució**: Utilitzeu sudo per a fitxers del sistema:
```bash
sudo sha256sum /etc/shadow
```

______

## Verificació Multiplataforma

### Verificar Hashs Linux a Windows

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### Verificar Hashs Linux a macOS

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## Conclusió

Linux proporciona potents eines integrades (`sha256sum`, `md5sum`, `sha1sum`) per al hash de fitxers. Tant si verifiqueu descàrregues, superviseu la integritat dels fitxers, detecteu duplicats o assegureu la validesa de còpies de seguretat, dominar aquestes comandes és essencial per a l'administració del sistema i la seguretat el 2026.

**punts principals:**
- Utilitzeu **sha256sum** per a totes les funcions de hash relacionades amb la seguretat
- Creeu manifestos de hash amb `sha256sum * > checksums.txt`
- Verifiqueu fitxers amb `sha256sum -c checksums.txt`
- Automatitzeu la comprovació de hash en scripts per a fitxers crítics
- Eviteu MD5 i SHA-1 per a finalitats de seguretat

## Referències

1. [sha256sum - pàgina man de Linux](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - pàgina man de Linux](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - pàgina man de Linux](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - Sumes de comprovació](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [NIST Funcions de hash](https://csrc.nist.gov/projects/hash-functions)
