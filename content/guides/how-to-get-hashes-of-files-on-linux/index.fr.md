---
title: "Guide du Hachage de Fichiers Linux 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: Guide complet 2026 du hachage de fichiers Linux utilisant les commandes sha256sum, md5sum, sha1sum. Apprenez la vérification de l'intégrité des fichiers, la comparaison des hachages, l'automatisation et les meilleures pratiques pour la sécurité.
tags:
- Hachages de fichiers Linux
- Hachage SHA256
- Hachage MD5
- Hachage SHA1
- Ligne de commande Linux
- intégrité des fichiers
- validation des données
- sécurité Linux
- outils intégrés
- vérification de fichiers
- authenticité des données
- algorithmes de hachage de fichiers
- administration système Linux
- outils en ligne de commande
- somme de contrôle de fichiers
- utilitaires Linux
- contrôles d'intégrité des fichiers
- vérification de l'intégrité des données
- exemples de hachage de fichiers
- commandes de hachage Linux
- méthodes de hachage de fichiers
- mesures de sécurité Linux
- protection des données Linux
- gestion des fichiers Linux
- vérification des fichiers Linux
- intégrité des fichiers Linux
- sécurité des données
- validation des données Linux
- sécurité système Linux
- techniques de hachage de fichiers
- assurance d'intégrité des fichiers
- validation sécurisée des fichiers
- intégrité des données Linux
- sha256sum
- md5sum
- sha1sum
- hachage de fichier linux
- obtenir le hachage d'un fichier linux
- linux obtenir le hachage d'un fichier
- linux hacher un fichier
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: Une illustration d'un terminal Linux futuriste affichant les sorties des commandes de hachage, entouré de fichiers abstraits et de symboles numériques sur un fond sombre, avec des accents vibrants bleus, verts et violets.
coverCaption: ''
---

**Guide : Obtenir les Hachages des Fichiers sur Linux avec les Outils Intégrés**

## Introduction

Dans l'univers des systèmes Linux, obtenir les hachages des fichiers est essentiel pour garantir l'intégrité des données et vérifier l'authenticité des fichiers. Les hachages de fichiers servent d'identifiants uniques permettant aux utilisateurs de détecter les tentatives de falsification et de valider l'intégrité des données. Dans ce guide complet, nous explorerons comment obtenir les hachages **SHA256**, **MD5** et **SHA1** des fichiers sur Linux en utilisant les outils intégrés. Suivez les instructions étape par étape et apprenez à travers des exemples spécifiques.

______

## Obtenir les Hachages sur Linux avec les Outils Intégrés

Linux fournit plusieurs outils intégrés qui permettent aux utilisateurs de calculer les hachages de fichiers sans nécessiter d'installation de logiciels supplémentaires. Nous allons explorer trois algorithmes de hachage largement utilisés : **SHA256**, **MD5** et **SHA1**.

### Obtenir le Hachage SHA256

Pour obtenir le **hachage SHA256** d'un fichier sur Linux, vous pouvez utiliser la commande `sha256sum`. Ouvrez un terminal et naviguez jusqu'au répertoire où se trouve le fichier. Ensuite, exécutez la commande suivante :

```bash
sha256sum file_path
```
Remplacez `file_path` par le chemin réel vers votre fichier.

### Obtenir les Hachages MD5 et SHA1
Vous pouvez également obtenir les `MD5` et `SHA1 hashes` d'un fichier sur Linux en utilisant des commandes similaires :

- Pour obtenir le `MD5 hash` :

```bash
md5sum file_path
```

- Pour obtenir le `SHA1 hash` :

```bash
sha1sum file_path
```
Remplacez `file_path` par le chemin vers votre fichier dans les deux commandes.

## Exemples
Examinons des exemples spécifiques pour illustrer le processus d'obtention des hachages avec les outils intégrés sur Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Exemple 1 : Obtenir le Hachage SHA256
Imaginez que vous avez un fichier nommé `document.pdf` situé dans le répertoire `/home/user/docs`. Pour obtenir le `SHA256 hash` de ce fichier sur Linux, exécutez la commande suivante :

```bash
sha256sum /home/user/docs/document.pdf
```

La sortie affichera la valeur `SHA256 hash` du fichier.

### Exemple 2 : Obtenir le Hachage MD5

Supposons que vous avez un fichier nommé `image.jpg` stocké dans le répertoire `/home/user/pictures`. Pour obtenir le `MD5 hash` de ce fichier sur Linux, lancez la commande suivante :

```bash
md5sum /home/user/pictures/image.jpg
```

Le terminal affichera la valeur `MD5 hash` du fichier.

## Exemple 3 : Obtenir le Hachage SHA1

Considérez un scénario où vous avez un fichier nommé `data.txt` situé dans le répertoire `/home/user/files`. Pour obtenir le `SHA1 hash` de ce fichier sur Linux, exécutez la commande suivante :

```bash
sha1sum /home/user/files/data.txt
```
La sortie affichera la valeur `SHA1 hash` du fichier.

______

## Opérations Avancées de Hachage Linux

### Hacher Plusieurs Fichiers à la Fois

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### Créer un Fichier de Manifestes de Hachage

Générez un fichier contenant les hachages pour une vérification ultérieure :

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

Sortie lorsque les fichiers correspondent :
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### Comparer un Hachage avec une Valeur Attendue

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

### Hachage depuis l'Entrée Standard

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

## Cas d'Utilisation Pratiques

### 1. Vérifier les ISOs Téléchargés

Les distributions Linux fournissent des sommes de contrôle pour vérifier les téléchargements :

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. Détecter la Falsification de Fichiers

Surveillez les fichiers système critiques :

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

### 3. Dédupliquer les Fichiers

Trouvez les fichiers en double en utilisant les hachages :

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. Vérifier l'Intégrité des Sauvegardes

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## Scripts d'Automatisation

### Script 1 : Générateur de Hachage Récursif

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

### Script 2 : Outil de Vérification de Hachage

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

### Script 3 : Vérification de Téléchargement

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

## Optimisation des Performances

### Hacher Efficacement les Gros Fichiers

Pour les fichiers très volumineux, vous pouvez surveiller la progression :

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### Hachage en Parallèle

Hachez plusieurs fichiers en parallèle avec GNU Parallel :

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### Benchmark des Algorithmes de Hachage

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

## Comparaison de la Sécurité des Algorithmes de Hachage

| Algorithme | Longueur du Hachage | Statut 2026 | Cas d'Usage |
|-----------|---------------------|-------------|-------------|
| **SHA-256** | 256 bits (64 caractères) | ✅ Sécurisé | Recommandé pour toutes les applications de sécurité |
| **SHA-512** | 512 bits (128 caractères) | ✅ Sécurisé | Sécurité renforcée pour les données sensibles |
| **SHA-1** | 160 bits (40 caractères) | ⚠️ Obsolète | Compatibilité héritée uniquement |
| **MD5** | 128 bits (32 caractères) | ❌ Compromis | Usage non sécurisé uniquement |

**Recommandation 2026** : Utilisez toujours SHA-256 ou SHA-512 pour les applications critiques en sécurité.

______

## Intégration avec les Gestionnaires de Paquets

### Vérifier les Paquets APT (Debian/Ubuntu)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### Vérifier les Paquets RPM (Fedora/RHEL)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## Meilleures Pratiques pour 2026

1. **Utilisez SHA-256 par défaut** : C'est la norme de sécurité actuelle
2. **Évitez MD5 et SHA-1 pour la sécurité** : Seulement pour la compatibilité héritée
3. **Utilisez toujours le flag `-c` pour la vérification** : `sha256sum -c checksums.txt`
4. **Stockez les sommes de contrôle séparément** : Ne stockez pas les hachages avec les fichiers qu'ils vérifient
5. **Utilisez `-b` pour le mode binaire** : `sha256sum -b file.bin` (important sur certains systèmes)
6. **Automatisez la vérification** : Créez des tâches cron pour la surveillance des fichiers critiques
7. **Utilisez `--quiet` dans les scripts** : Supprimez les messages OK avec `sha256sum -c --quiet`

______

## Dépannage

### « Aucun fichier ou répertoire de ce type »

**Solution** : Utilisez des guillemets pour les chemins contenant des espaces :
```bash
sha256sum "/path/with spaces/file.txt"
```

### « AVERTISSEMENT : X lignes sont mal formatées »

**Solution** : Le format du fichier de somme de contrôle doit être :
```
hash_value  filename
```
Notez les deux espaces entre le hachage et le nom du fichier.

### Permission Refusée

**Solution** : Utilisez sudo pour les fichiers système :
```bash
sudo sha256sum /etc/shadow
```

______

## Vérification Multi-Plateforme

### Vérifier les Hachages Linux sous Windows

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### Vérifier les Hachages Linux sous macOS

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## Conclusion

Linux fournit des outils intégrés puissants (`sha256sum`, `md5sum`, `sha1sum`) pour le hachage de fichiers. Que vous vérifiiez des téléchargements, surveilliez l'intégrité des fichiers, détectiez des doublons ou assuriez la validité des sauvegardes, maîtriser ces commandes est essentiel pour l'administration système et la sécurité en 2026.

**points principaux :**
- Utilisez **sha256sum** pour tous les hachages liés à la sécurité
- Créez des manifestes de hachage avec `sha256sum * > checksums.txt`
- Vérifiez les fichiers avec `sha256sum -c checksums.txt`
- Automatisez la vérification des hachages dans les scripts pour les fichiers critiques
- Évitez MD5 et SHA-1 pour des raisons de sécurité

## Références

1. [sha256sum - page de manuel Linux](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - page de manuel Linux](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - page de manuel Linux](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - Sommes de contrôle](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [Fonctions de hachage NIST](https://csrc.nist.gov/projects/hash-functions)
