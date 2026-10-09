---
title: "Руководство по хешированию файлов в Linux 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: Полное руководство 2026 года по хешированию файлов в Linux с использованием команд sha256sum, md5sum, sha1sum. Узнайте о проверке целостности файлов, сравнении хешей, автоматизации и лучших практиках безопасности.
tags:
- Хеши файлов Linux
- Хеш SHA256
- Хеш MD5
- Хеш SHA1
- Командная строка Linux
- целостность файла
- проверка данных
- безопасность Linux
- встроенные инструменты
- проверка файла
- аутентичность данных
- алгоритмы хеширования файлов
- администрирование системы Linux
- инструменты командной строки
- контрольные суммы файлов
- утилиты Linux
- проверка целостности файлов
- проверка целостности данных
- примеры хешей файлов
- команды хеширования Linux
- методы хеширования файлов
- меры безопасности Linux
- защита данных Linux
- управление файлами Linux
- проверка файлов Linux
- целостность файлов Linux
- безопасность данных
- проверка данных Linux
- безопасность системы Linux
- техники хеширования файлов
- гарантия целостности файлов
- безопасная проверка файлов
- целостность данных Linux
- sha256sum
- md5sum
- sha1sum
- хеш файла linux
- получить хеш файла linux
- linux получить хеш файла
- linux хешировать файл
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: Иллюстрация футуристического терминала Linux, отображающего вывод команд хеширования, окружённого абстрактными файлами и цифровыми символами на тёмном фоне с яркими синими, зелёными и пурпурными акцентами.
coverCaption: ''
---

**Руководство: Получение хешей файлов в Linux с помощью встроенных инструментов**

## Введение

В мире систем Linux получение хешей файлов необходимо для обеспечения целостности данных и проверки подлинности файлов. Хеши файлов служат уникальными идентификаторами, позволяющими пользователям обнаруживать попытки подделки и подтверждать целостность данных. В этом полном руководстве мы рассмотрим, как получить **SHA256**, **MD5** и **SHA1** хеши файлов в Linux с помощью встроенных инструментов. Следуйте пошаговым инструкциям и учитесь на конкретных примерах.

______

## Получение хешей в Linux с помощью встроенных инструментов

Linux предоставляет несколько встроенных инструментов, позволяющих вычислять хеши файлов без необходимости установки дополнительного программного обеспечения. Мы рассмотрим три широко используемых алгоритма хеширования: **SHA256**, **MD5** и **SHA1**.

### Получение хеша SHA256

Чтобы получить **SHA256 хеш** файла в Linux, вы можете использовать команду `sha256sum`. Откройте терминал и перейдите в каталог, где находится файл. Затем выполните следующую команду:

```bash
sha256sum file_path
```
Замените `file_path` на фактический путь к вашему файлу.

### Получение хешей MD5 и SHA1
Вы также можете получить `MD5` и `SHA1 hashes` файла в Linux с помощью похожих команд:

- Чтобы получить `MD5 hash`:

```bash
md5sum file_path
```

- Чтобы получить `SHA1 hash`:

```bash
sha1sum file_path
```
Замените `file_path` на путь к вашему файлу в обеих командах.

## Примеры
Рассмотрим конкретные примеры, иллюстрирующие процесс получения хешей с помощью встроенных инструментов в Linux.

{{< youtube id="3aX9zK88X9M" >}}

### Пример 1: Получение хеша SHA256
Предположим, у вас есть файл с именем `document.pdf`, расположенный в каталоге `/home/user/docs`. Чтобы получить `SHA256 hash` этого файла в Linux, выполните следующую команду:

```bash
sha256sum /home/user/docs/document.pdf
```

В выводе будет отображено значение `SHA256 hash` файла.

### Пример 2: Получение хеша MD5

Предположим, у вас есть файл с именем `image.jpg`, хранящийся в каталоге `/home/user/pictures`. Чтобы получить `MD5 hash` этого файла в Linux, выполните следующую команду:

```bash
md5sum /home/user/pictures/image.jpg
```

В терминале будет показано значение `MD5 hash` файла.

## Пример 3: Получение хеша SHA1

Рассмотрим ситуацию, когда у вас есть файл с именем `data.txt`, расположенный в каталоге `/home/user/files`. Чтобы получить `SHA1 hash` этого файла в Linux, выполните следующую команду:

```bash
sha1sum /home/user/files/data.txt
```
В выводе будет показано значение `SHA1 hash` файла.

______

## Расширенные операции хеширования в Linux

### Хеширование нескольких файлов одновременно

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### Создание файла манифеста хешей

Создайте файл, содержащий хеши для последующей проверки:

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

Вывод при совпадении файлов:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### Сравнение хеша с ожидаемым значением

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

### Хеширование из стандартного ввода

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

## Практические случаи использования

### 1. Проверка загруженных ISO

Дистрибутивы Linux предоставляют контрольные суммы для проверки загрузок:

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. Обнаружение подделки файлов

Мониторинг критически важных системных файлов:

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

### 3. Удаление дубликатов файлов

Поиск дубликатов файлов с помощью хешей:

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. Проверка целостности резервных копий

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## Скрипты автоматизации

### Скрипт 1: Рекурсивный генератор хешей

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

### Скрипт 2: Инструмент проверки хешей

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

### Скрипт 3: Проверка загрузок

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

## Оптимизация производительности

### Эффективное хеширование больших файлов

Для очень больших файлов можно отслеживать прогресс:

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### Параллельное хеширование

Хеширование нескольких файлов параллельно с помощью GNU Parallel:

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### Тестирование производительности алгоритмов хеширования

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

## Сравнение безопасности алгоритмов хеширования

| Алгоритм | Длина хеша | Статус 2026 | Случай использования |
|-----------|-------------|-------------|---------------------|
| **SHA-256** | 256 бит (64 символа) | ✅ Безопасен | Рекомендуется для всех целей безопасности |
| **SHA-512** | 512 бит (128 символов) | ✅ Безопасен | Дополнительная безопасность для чувствительных данных |
| **SHA-1** | 160 бит (40 символов) | ⚠️ Устарел | Только для совместимости с наследием |
| **MD5** | 128 бит (32 символа) | ❌ Взломан | Только для незащитных целей |

**Рекомендация 2026**: Всегда используйте SHA-256 или SHA-512 для критически важных с точки зрения безопасности приложений.

______

## Интеграция с менеджерами пакетов

### Проверка пакетов APT (Debian/Ubuntu)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### Проверка пакетов RPM (Fedora/RHEL)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## Лучшие практики на 2026 год

1. **Используйте SHA-256 по умолчанию**: Это текущий стандарт безопасности
2. **Избегайте MD5 и SHA-1 для безопасности**: Только для совместимости с наследием
3. **Всегда используйте флаг `-c` для проверки**: `sha256sum -c checksums.txt`
4. **Храните контрольные суммы отдельно**: Не храните хеши вместе с проверяемыми файлами
5. **Используйте `-b` для бинарного режима**: `sha256sum -b file.bin` (важно на некоторых системах)
6. **Автоматизируйте проверку**: Создавайте задания cron для мониторинга критических файлов
7. **Используйте `--quiet` в скриптах**: Подавляйте сообщения OK с помощью `sha256sum -c --quiet`

______

## Устранение неполадок

### «Нет такого файла или каталога»

**Решение**: Используйте кавычки для путей с пробелами:
```bash
sha256sum "/path/with spaces/file.txt"
```

### «WARNING: X строк имеют неправильный формат»

**Решение**: Формат файла контрольных сумм должен быть:
```
hash_value  filename
```
Обратите внимание на два пробела между хешем и именем файла.

### Отказано в доступе

**Решение**: Используйте sudo для системных файлов:
```bash
sudo sha256sum /etc/shadow
```

______

## Кроссплатформенная проверка

### Проверка хешей Linux в Windows

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### Проверка хешей Linux в macOS

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## Заключение

Linux предоставляет мощные встроенные инструменты (`sha256sum`, `md5sum`, `sha1sum`) для хеширования файлов. Независимо от того, проверяете ли вы загрузки, контролируете целостность файлов, обнаруживаете дубликаты или обеспечиваете валидность резервных копий, освоение этих команд является необходимым для администрирования систем и безопасности в 2026 году.

**основные моменты:**
- Используйте **sha256sum** для всех задач, связанных с безопасностью хеширования
- Создавайте манифесты хешей с помощью `sha256sum * > checksums.txt`
- Проверяйте файлы с помощью `sha256sum -c checksums.txt`
- Автоматизируйте проверку хешей в скриптах для критически важных файлов
- Избегайте использования MD5 и SHA-1 для целей безопасности

## Ссылки

1. [sha256sum - страница руководства Linux](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - страница руководства Linux](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - страница руководства Linux](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - Контрольные суммы](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [NIST Функции хеширования](https://csrc.nist.gov/projects/hash-functions)
