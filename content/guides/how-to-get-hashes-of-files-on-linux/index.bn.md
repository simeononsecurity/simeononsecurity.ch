---
title: "লিনাক্স ফাইল হ্যাশ গাইড ২০২৬"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: sha256sum, md5sum, sha1sum কমান্ড ব্যবহার করে লিনাক্স ফাইল হ্যাশিংয়ের সম্পূর্ণ ২০২৬ গাইড। ফাইল ইন্টিগ্রিটি যাচাই, হ্যাশ তুলনা, অটোমেশন এবং নিরাপত্তার জন্য সেরা অনুশীলন শিখুন।
tags:
- লিনাক্স ফাইল হ্যাশ
- SHA256 হ্যাশ
- MD5 হ্যাশ
- SHA1 হ্যাশ
- লিনাক্স কমান্ড লাইন
- ফাইল ইন্টিগ্রিটি
- ডেটা যাচাই
- লিনাক্স নিরাপত্তা
- অন্তর্নির্মিত সরঞ্জাম
- ফাইল যাচাই
- ডেটা প্রামাণিকতা
- ফাইল হ্যাশিং অ্যালগরিদম
- লিনাক্স সিস্টেম প্রশাসন
- কমান্ড লাইন সরঞ্জাম
- ফাইল চেকসাম
- লিনাক্স ইউটিলিটি
- ফাইল ইন্টিগ্রিটি পরীক্ষা
- ডেটা ইন্টিগ্রিটি যাচাই
- ফাইল হ্যাশ উদাহরণ
- লিনাক্স হ্যাশ কমান্ড
- ফাইল হ্যাশিং পদ্ধতি
- লিনাক্স নিরাপত্তা ব্যবস্থা
- লিনাক্স ডেটা সুরক্ষা
- লিনাক্স ফাইল ব্যবস্থাপনা
- লিনাক্স ফাইল যাচাই
- লিনাক্স ফাইল ইন্টিগ্রিটি
- ডেটা নিরাপত্তা
- লিনাক্স ডেটা যাচাই
- লিনাক্স সিস্টেম নিরাপত্তা
- ফাইল হ্যাশিং কৌশল
- ফাইল ইন্টিগ্রিটি নিশ্চয়তা
- নিরাপদ ফাইল যাচাই
- লিনাক্স ডেটা ইন্টিগ্রিটি
- sha256sum
- md5sum
- sha1sum
- লিনাক্স হ্যাশ ফাইল
- লিনাক্সে ফাইলের হ্যাশ পান
- লিনাক্সে ফাইলের হ্যাশ পান
- লিনাক্সে একটি ফাইল হ্যাশ করুন
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: একটি ভবিষ্যতবাণীমূলক লিনাক্স টার্মিনালের চিত্র যা হ্যাশ কমান্ড আউটপুট দেখাচ্ছে, চারপাশে বিমূর্ত ফাইল এবং ডিজিটাল প্রতীকগুলি একটি অন্ধকার পটভূমিতে, উজ্জ্বল নীল, সবুজ এবং বেগুনি রঙের আলোকসজ্জা সহ।
coverCaption: ''
---

**গাইড: অন্তর্নির্মিত সরঞ্জাম ব্যবহার করে লিনাক্সে ফাইলের হ্যাশ পাওয়া**

## পরিচিতি

লিনাক্স সিস্টেমের জগতে, ডেটা ইন্টিগ্রিটি নিশ্চিত করা এবং ফাইলের প্রামাণিকতা যাচাই করার জন্য ফাইল হ্যাশ পাওয়া অপরিহার্য। ফাইল হ্যাশগুলি অনন্য শনাক্তকারী হিসেবে কাজ করে যা ব্যবহারকারীদের ছিনতাইয়ের প্রচেষ্টা সনাক্ত করতে এবং ডেটার অখণ্ডতা যাচাই করতে সাহায্য করে। এই বিস্তৃত গাইডে, আমরা অন্তর্নির্মিত সরঞ্জাম ব্যবহার করে লিনাক্সে ফাইলের **SHA256**, **MD5**, এবং **SHA1** হ্যাশ কীভাবে পাওয়া যায় তা অন্বেষণ করব। ধাপে ধাপে নির্দেশাবলী অনুসরণ করুন এবং নির্দিষ্ট উদাহরণের মাধ্যমে শিখুন।

______

## অন্তর্নির্মিত সরঞ্জাম ব্যবহার করে লিনাক্সে হ্যাশ পাওয়া

লিনাক্স কয়েকটি অন্তর্নির্মিত সরঞ্জাম প্রদান করে যা ব্যবহারকারীদের অতিরিক্ত সফটওয়্যার ইনস্টলেশন ছাড়াই ফাইল হ্যাশ গণনা করতে সক্ষম করে। আমরা তিনটি ব্যাপকভাবে ব্যবহৃত হ্যাশিং অ্যালগরিদম অন্বেষণ করব: **SHA256**, **MD5**, এবং **SHA1**।

### SHA256 হ্যাশ পাওয়া

লিনাক্সে একটি ফাইলের **SHA256 হ্যাশ** পেতে, আপনি `sha256sum` কমান্ড ব্যবহার করতে পারেন। একটি টার্মিনাল খুলুন এবং ফাইলটি যেখানে অবস্থিত সেই ডিরেক্টরিতে যান। তারপর নিম্নলিখিত কমান্ডটি চালান:

```bash
sha256sum file_path
```
`file_path`-কে আপনার ফাইলের প্রকৃত পথ দিয়ে প্রতিস্থাপন করুন।

### MD5 এবং SHA1 হ্যাশ পাওয়া
আপনি একই রকম কমান্ড ব্যবহার করে লিনাক্সে একটি ফাইলের `MD5` এবং `SHA1 hashes` পেতে পারেন:

- `MD5 hash` পেতে:

```bash
md5sum file_path
```

- `SHA1 hash` পেতে:

```bash
sha1sum file_path
```
উভয় কমান্ডে `file_path`-কে আপনার ফাইলের পথ দিয়ে প্রতিস্থাপন করুন।

## উদাহরণ
চলুন নির্দিষ্ট উদাহরণের মাধ্যমে লিনাক্সে অন্তর্নির্মিত সরঞ্জাম ব্যবহার করে হ্যাশ পাওয়ার প্রক্রিয়া ব্যাখ্যা করি।

{{< youtube id="3aX9zK88X9M" >}}

### উদাহরণ ১: SHA256 হ্যাশ পাওয়া
ধরা যাক আপনার কাছে `document.pdf` নামে একটি ফাইল আছে যা `/home/user/docs` ডিরেক্টরিতে অবস্থিত। এই ফাইলের `SHA256 hash` পেতে লিনাক্সে নিম্নলিখিত কমান্ডটি চালান:

```bash
sha256sum /home/user/docs/document.pdf
```

আউটপুটে ফাইলটির `SHA256 hash` মান প্রদর্শিত হবে।

### উদাহরণ ২: MD5 হ্যাশ পাওয়া

ধরা যাক আপনার কাছে `image.jpg` নামে একটি ফাইল আছে যা `/home/user/pictures` ডিরেক্টরিতে সংরক্ষিত। এই ফাইলের `MD5 hash` পেতে লিনাক্সে নিম্নলিখিত কমান্ডটি চালান:

```bash
md5sum /home/user/pictures/image.jpg
```

টার্মিনাল ফাইলটির `MD5 hash` মান প্রদর্শন করবে।

## উদাহরণ ৩: SHA1 হ্যাশ পাওয়া

একটি পরিস্থিতি বিবেচনা করুন যেখানে আপনার কাছে `data.txt` নামে একটি ফাইল আছে যা `/home/user/files` ডিরেক্টরিতে অবস্থিত। এই ফাইলের `SHA1 hash` পেতে লিনাক্সে নিম্নলিখিত কমান্ডটি চালান:

```bash
sha1sum /home/user/files/data.txt
```
আউটপুটে ফাইলটির `SHA1 hash` মান প্রদর্শিত হবে।

______

## উন্নত লিনাক্স হ্যাশিং অপারেশন

### একসাথে একাধিক ফাইলের হ্যাশ করা

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### হ্যাশ ম্যানিফেস্ট ফাইল তৈরি করা

পরবর্তীতে যাচাইয়ের জন্য হ্যাশ সহ একটি ফাইল তৈরি করুন:

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

ফাইলগুলি মিলে গেলে আউটপুট:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### প্রত্যাশিত মানের সাথে হ্যাশ তুলনা করা

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

### স্ট্যান্ডার্ড ইনপুট থেকে হ্যাশ

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

## ব্যবহারিক ব্যবহার ক্ষেত্র

### ১. ডাউনলোড করা ISO যাচাই করা

লিনাক্স ডিস্ট্রিবিউশনগুলি ডাউনলোড যাচাইয়ের জন্য হ্যাশ চেকসাম প্রদান করে:

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### ২. ফাইল ছিনতাই সনাক্ত করা

গুরুত্বপূর্ণ সিস্টেম ফাইল পর্যবেক্ষণ করুন:

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

### ৩. ফাইল ডুপ্লিকেট খুঁজে বের করা

হ্যাশ ব্যবহার করে ডুপ্লিকেট ফাইল খুঁজুন:

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### ৪. ব্যাকআপ ইন্টিগ্রিটি যাচাই করা

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## অটোমেশন স্ক্রিপ্ট

### স্ক্রিপ্ট ১: রিকার্সিভ হ্যাশ জেনারেটর

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

### স্ক্রিপ্ট ২: হ্যাশ যাচাই সরঞ্জাম

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

### স্ক্রিপ্ট ৩: ডাউনলোড যাচাই

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

## কর্মক্ষমতা অপ্টিমাইজেশন

### বড় ফাইল দক্ষতার সাথে হ্যাশ করা

খুব বড় ফাইলের জন্য, আপনি অগ্রগতি পর্যবেক্ষণ করতে পারেন:

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### সমান্তরাল হ্যাশিং

GNU Parallel ব্যবহার করে একাধিক ফাইল সমান্তরালে হ্যাশ করুন:

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### হ্যাশ অ্যালগরিদমের বেঞ্চমার্ক

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

## হ্যাশ অ্যালগরিদম নিরাপত্তা তুলনা

| অ্যালগরিদম | হ্যাশ দৈর্ঘ্য | ২০২৬ অবস্থা | ব্যবহার ক্ষেত্র |
|-----------|-------------|-------------|----------|
| **SHA-256** | ২৫৬-বিট (৬৪ অক্ষর) | ✅ নিরাপদ | সকল নিরাপত্তা উদ্দেশ্যে সুপারিশকৃত |
| **SHA-512** | ৫১২-বিট (১২৮ অক্ষর) | ✅ নিরাপদ | সংবেদনশীল ডেটার জন্য অতিরিক্ত নিরাপত্তা |
| **SHA-1** | ১৬০-বিট (৪০ অক্ষর) | ⚠️ অব্যবহৃত | শুধুমাত্র পুরনো সামঞ্জস্যতার জন্য |
| **MD5** | ১২৮-বিট (৩২ অক্ষর) | ❌ ভঙ্গুর | শুধুমাত্র অ-নিরাপত্তা উদ্দেশ্যে |

**২০২৬ সুপারিশ**: নিরাপত্তা-গুরুত্বপূর্ণ অ্যাপ্লিকেশনের জন্য সর্বদা SHA-256 বা SHA-512 ব্যবহার করুন।

______

## প্যাকেজ ম্যানেজারগুলোর সাথে ইন্টিগ্রেশন

### APT প্যাকেজ যাচাই (ডেবিয়ান/উবুন্টু)

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### RPM প্যাকেজ যাচাই (ফেডোরা/আরএইচইএল)

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## ২০২৬ সালের সেরা অনুশীলন

১. **ডিফল্ট হিসেবে SHA-256 ব্যবহার করুন**: এটি বর্তমান নিরাপত্তা মানদণ্ড
২. **নিরাপত্তার জন্য MD5 এবং SHA-1 এড়িয়ে চলুন**: শুধুমাত্র পুরনো সামঞ্জস্যতার জন্য
৩. **যাচাইয়ের জন্য সর্বদা `-c` ফ্ল্যাগ ব্যবহার করুন**: `sha256sum -c checksums.txt`
৪. **চেকসাম আলাদাভাবে সংরক্ষণ করুন**: যাচাই করা ফাইলের সাথে হ্যাশ সংরক্ষণ করবেন না
৫. **বাইনারি মোডের জন্য `-b` ব্যবহার করুন**: `sha256sum -b file.bin` (কিছু সিস্টেমে গুরুত্বপূর্ণ)
৬. **যাচাই অটোমেট করুন**: গুরুত্বপূর্ণ ফাইল পর্যবেক্ষণের জন্য ক্রন জব তৈরি করুন
৭. **স্ক্রিপ্টে `--quiet` ব্যবহার করুন**: `sha256sum -c --quiet` দিয়ে OK বার্তা দমন করুন

______

## সমস্যা সমাধান

### "এমন কোনো ফাইল বা ডিরেক্টরি নেই"

**সমাধান**: স্পেস সহ পথের জন্য উদ্ধৃতি ব্যবহার করুন:
```bash
sha256sum "/path/with spaces/file.txt"
```

### "WARNING: X লাইন ভুল ফরম্যাটে আছে"

**সমাধান**: চেকসাম ফাইলের ফরম্যাট অবশ্যই হওয়া উচিত:
```
hash_value  filename
```
হ্যাশ এবং ফাইলনামের মধ্যে দুটি স্পেস লক্ষ্য করুন।

### অনুমতি অস্বীকার

**সমাধান**: সিস্টেম ফাইলের জন্য sudo ব্যবহার করুন:
```bash
sudo sha256sum /etc/shadow
```

______

## ক্রস-প্ল্যাটফর্ম যাচাই

### উইন্ডোজে লিনাক্স হ্যাশ যাচাই

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### macOS-এ লিনাক্স হ্যাশ যাচাই

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## উপসংহার

লিনাক্স শক্তিশালী অন্তর্নির্মিত সরঞ্জাম (`sha256sum`, `md5sum`, `sha1sum`) প্রদান করে ফাইল হ্যাশিংয়ের জন্য। আপনি ডাউনলোড যাচাই করুন, ফাইল ইন্টিগ্রিটি পর্যবেক্ষণ করুন, ডুপ্লিকেট সনাক্ত করুন বা ব্যাকআপ বৈধতা নিশ্চিত করুন, এই কমান্ডগুলি দক্ষতার সাথে ব্যবহার করা ২০২৬ সালে সিস্টেম প্রশাসন এবং নিরাপত্তার জন্য অপরিহার্য।

**মূল পয়েন্টসমূহ:**
- সমস্ত নিরাপত্তা-সম্পর্কিত হ্যাশিংয়ের জন্য **sha256sum** ব্যবহার করুন
- `sha256sum * > checksums.txt` দিয়ে হ্যাশ ম্যানিফেস্ট তৈরি করুন
- `sha256sum -c checksums.txt` দিয়ে ফাইল যাচাই করুন
- গুরুত্বপূর্ণ ফাইলের জন্য স্ক্রিপ্টে হ্যাশ চেকিং স্বয়ংক্রিয় করুন
- নিরাপত্তার জন্য MD5 এবং SHA-1 এড়িয়ে চলুন

## রেফারেন্সসমূহ

1. [sha256sum - লিনাক্স ম্যান পৃষ্ঠা](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - লিনাক্স ম্যান পৃষ্ঠা](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - লিনাক্স ম্যান পৃষ্ঠা](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - চেকসাম](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [NIST হ্যাশ ফাংশনসমূহ](https://csrc.nist.gov/projects/hash-functions)
