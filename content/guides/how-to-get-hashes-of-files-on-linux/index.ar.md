---
title: "دليل تجزئة الملفات في لينكس 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: الدليل الكامل لعام 2026 لتجزئة الملفات في لينكس باستخدام أوامر sha256sum و md5sum و sha1sum. تعلّم التحقق من سلامة الملفات، مقارنة التجزئات، الأتمتة، وأفضل الممارسات للأمان.
tags:
- تجزئات ملفات لينكس
- تجزئة SHA256
- تجزئة MD5
- تجزئة SHA1
- سطر أوامر لينكس
- سلامة الملف
- التحقق من البيانات
- أمان لينكس
- أدوات مدمجة
- التحقق من الملفات
- أصالة البيانات
- خوارزميات تجزئة الملفات
- إدارة نظام لينكس
- أدوات سطر الأوامر
- مجموعات التحقق من الملفات
- أدوات لينكس
- فحوصات سلامة الملفات
- التحقق من سلامة البيانات
- أمثلة على تجزئة الملفات
- أوامر تجزئة لينكس
- طرق تجزئة الملفات
- إجراءات أمان لينكس
- حماية بيانات لينكس
- إدارة ملفات لينكس
- التحقق من ملفات لينكس
- سلامة ملفات لينكس
- أمان البيانات
- التحقق من بيانات لينكس
- أمان نظام لينكس
- تقنيات تجزئة الملفات
- ضمان سلامة الملفات
- التحقق الآمن من الملفات
- سلامة بيانات لينكس
- sha256sum
- md5sum
- sha1sum
- تجزئة ملف لينكس
- الحصول على تجزئة ملف في لينكس
- لينكس الحصول على تجزئة ملف
- لينكس تجزئة ملف
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: رسم توضيحي لجهاز طرفية لينكس مستقبلي يعرض مخرجات أوامر التجزئة، محاط بملفات مجردة ورموز رقمية على خلفية داكنة مع لمسات زرقاء وخضراء وأرجوانية زاهية.
coverCaption: ''
---

**الدليل: الحصول على تجزئات الملفات في لينكس باستخدام الأدوات المدمجة**

## المقدمة

في عالم أنظمة لينكس، الحصول على تجزئات الملفات أمر ضروري لضمان سلامة البيانات والتحقق من أصالة الملفات. تعمل تجزئات الملفات كمعرفات فريدة تسمح للمستخدمين بالكشف عن محاولات التلاعب والتحقق من سلامة البيانات. في هذا الدليل الشامل، سنستعرض كيفية الحصول على تجزئات **SHA256** و **MD5** و **SHA1** للملفات على لينكس باستخدام الأدوات المدمجة. اتبع التعليمات خطوة بخطوة وتعلم من خلال أمثلة محددة.

______

## الحصول على التجزئات في لينكس باستخدام الأدوات المدمجة

يوفر لينكس عدة أدوات مدمجة تمكن المستخدمين من حساب تجزئات الملفات دون الحاجة لتثبيت برامج إضافية. سنستعرض ثلاث خوارزميات تجزئة مستخدمة على نطاق واسع: **SHA256** و **MD5** و **SHA1**.

### الحصول على تجزئة SHA256

للحصول على **تجزئة SHA256** لملف في لينكس، يمكنك استخدام الأمر `sha256sum`. افتح الطرفية وانتقل إلى الدليل الذي يحتوي الملف. ثم نفذ الأمر التالي:

```bash
sha256sum file_path
```
استبدل `file_path` بالمسار الفعلي لملفك.

### الحصول على تجزئتي MD5 و SHA1
يمكنك أيضًا الحصول على `MD5` و `SHA1 hashes` لملف في لينكس باستخدام أوامر مماثلة:

- للحصول على `MD5 hash`:

```bash
md5sum file_path
```

- للحصول على `SHA1 hash`:

```bash
sha1sum file_path
```
استبدل `file_path` بمسار ملفك في كلا الأمرين.

## أمثلة
لنغص في أمثلة محددة لتوضيح عملية الحصول على التجزئات باستخدام الأدوات المدمجة في لينكس.

{{< youtube id="3aX9zK88X9M" >}}

### المثال 1: الحصول على تجزئة SHA256
تخيل أن لديك ملفًا اسمه `document.pdf` موجود في الدليل `/home/user/docs`. للحصول على `SHA256 hash` لهذا الملف على لينكس، نفذ الأمر التالي:

```bash
sha256sum /home/user/docs/document.pdf
```

سيعرض الناتج قيمة `SHA256 hash` للملف.

### المثال 2: الحصول على تجزئة MD5

افترض أن لديك ملفًا اسمه `image.jpg` مخزنًا في الدليل `/home/user/pictures`. للحصول على `MD5 hash` لهذا الملف على لينكس، شغّل الأمر التالي:

```bash
md5sum /home/user/pictures/image.jpg
```

ستعرض الطرفية قيمة `MD5 hash` للملف.

## المثال 3: الحصول على تجزئة SHA1

اعتبر سيناريو حيث لديك ملف اسمه `data.txt` موجود في الدليل `/home/user/files`. للحصول على `SHA1 hash` لهذا الملف على لينكس، نفذ الأمر التالي:

```bash
sha1sum /home/user/files/data.txt
```
سيعرض الناتج قيمة `SHA1 hash` للملف.

______

## عمليات تجزئة متقدمة في لينكس

### تجزئة عدة ملفات دفعة واحدة

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### إنشاء ملف سجل التجزئات

أنشئ ملفًا يحتوي على التجزئات للتحقق لاحقًا:

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

الناتج عند تطابق الملفات:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### مقارنة التجزئة بالقيمة المتوقعة

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

### التجزئة من الإدخال القياسي

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

## حالات استخدام عملية

### 1. التحقق من ملفات ISO المحملة

تقدم توزيعات لينكس مجموعات تحقق من التجزئة للتحقق من التنزيلات:

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. كشف التلاعب بالملفات

راقب ملفات النظام الحرجة:

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

### 3. إزالة التكرار من الملفات

ابحث عن الملفات المكررة باستخدام التجزئات:

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. التحقق من سلامة النسخ الاحتياطية

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## سكربتات الأتمتة

### السكربت 1: مولد التجزئة التكراري

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

### السكربت 2: أداة التحقق من التجزئة

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

### السكربت 3: التحقق من التنزيل

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

## تحسين الأداء

### تجزئة الملفات الكبيرة بكفاءة

لملفات كبيرة جدًا، يمكنك مراقبة التقدم:

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### التجزئة المتوازية

جزء عدة ملفات بالتوازي باستخدام GNU Parallel:

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### قياس أداء خوارزميات التجزئة

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

## مقارنة أمان خوارزميات التجزئة

| الخوارزمية | طول التجزئة | الحالة 2026 | حالة الاستخدام |
|-----------|-------------|-------------|----------|
| **SHA-256** | 256-بت (64 حرف) | ✅ آمن | موصى به لجميع أغراض الأمان |
| **SHA-512** | 512-بت (128 حرف) | ✅ آمن | أمان إضافي للبيانات الحساسة |
| **SHA-1** | 160-بت (40 حرف) | ⚠️ مهمل | للتوافق مع الأنظمة القديمة فقط |
| **MD5** | 128-بت (32 حرف) | ❌ مكسور | لأغراض غير أمنية فقط |

**توصية 2026**: استخدم دائمًا SHA-256 أو SHA-512 للتطبيقات الحرجة أمنيًا.

______

## التكامل مع مديري الحزم

### التحقق من حزم APT (ديبيان/أوبونتو)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### التحقق من حزم RPM (فيدورا/ريل)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## أفضل الممارسات لعام 2026

1. **استخدم SHA-256 كإعداد افتراضي**: إنه المعيار الأمني الحالي
2. **تجنب MD5 و SHA-1 للأمان**: فقط للتوافق مع الأنظمة القديمة
3. **استخدم دائمًا علم `-c` للتحقق**: `sha256sum -c checksums.txt`
4. **خزن مجموعات التحقق بشكل منفصل**: لا تخزن التجزئات مع الملفات التي تتحقق منها
5. **استخدم `-b` للوضع الثنائي**: `sha256sum -b file.bin` (مهم في بعض الأنظمة)
6. **قم بأتمتة التحقق**: أنشئ مهام كرون لمراقبة الملفات الحرجة
7. **استخدم `--quiet` في السكربتات**: لكتم رسائل OK باستخدام `sha256sum -c --quiet`

______

## استكشاف الأخطاء وإصلاحها

### "لا يوجد ملف أو دليل بهذا الاسم"

**الحل**: استخدم علامات الاقتباس للمسارات التي تحتوي على فراغات:
```bash
sha256sum "/path/with spaces/file.txt"
```

### "تحذير: X أسطر بتنسيق غير صحيح"

**الحل**: يجب أن يكون تنسيق ملف مجموعات التحقق:
```
hash_value  filename
```
لاحظ وجود مسافتين بين التجزئة واسم الملف.

### رفض الإذن

**الحل**: استخدم sudo للملفات النظامية:
```bash
sudo sha256sum /etc/shadow
```

______

## التحقق عبر الأنظمة

### التحقق من تجزئات لينكس على ويندوز

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### التحقق من تجزئات لينكس على macOS

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## الخاتمة

يوفر لينكس أدوات مدمجة قوية (`sha256sum`، `md5sum`، `sha1sum`) لتجزئة الملفات. سواء كنت تتحقق من التنزيلات، تراقب سلامة الملفات، تكشف التكرارات، أو تضمن صلاحية النسخ الاحتياطية، فإن إتقان هذه الأوامر ضروري لإدارة النظام والأمان في 2026.

**النقاط الرئيسية:**
- استخدم **sha256sum** لجميع عمليات التجزئة المتعلقة بالأمان
- أنشئ قوائم تجزئة باستخدام `sha256sum * > checksums.txt`
- تحقق من الملفات باستخدام `sha256sum -c checksums.txt`
- أتمتة فحص التجزئة في السكربتات للملفات الحرجة
- تجنب استخدام MD5 و SHA-1 لأغراض الأمان

## المراجع

1. [sha256sum - صفحة دليل لينكس](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - صفحة دليل لينكس](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - صفحة دليل لينكس](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - مجموعات التحقق](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [دوال التجزئة في NIST](https://csrc.nist.gov/projects/hash-functions)
