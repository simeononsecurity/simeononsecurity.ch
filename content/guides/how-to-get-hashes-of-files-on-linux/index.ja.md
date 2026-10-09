---
title: "Linuxファイルハッシュガイド 2026"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-10-08
description: sha256sum、md5sum、sha1sumコマンドを使ったLinuxファイルハッシュの完全ガイド2026。ファイルの整合性検証、ハッシュ比較、自動化、セキュリティのベストプラクティスを学びます。
tags:
- Linuxファイルハッシュ
- SHA256ハッシュ
- MD5ハッシュ
- SHA1ハッシュ
- Linuxコマンドライン
- ファイル整合性
- データ検証
- Linuxセキュリティ
- 組み込みツール
- ファイル検証
- データ真正性
- ファイルハッシュアルゴリズム
- Linuxシステム管理
- コマンドラインツール
- ファイルチェックサム
- Linuxユーティリティ
- ファイル整合性チェック
- データ整合性検証
- ファイルハッシュ例
- Linuxハッシュコマンド
- ファイルハッシュ方法
- Linuxセキュリティ対策
- Linuxデータ保護
- Linuxファイル管理
- Linuxファイル検証
- Linuxファイル整合性
- データセキュリティ
- Linuxデータ検証
- Linuxシステムセキュリティ
- ファイルハッシュ技術
- ファイル整合性保証
- 安全なファイル検証
- Linuxデータ整合性
- sha256sum
- md5sum
- sha1sum
- linuxハッシュファイル
- linuxでファイルのハッシュを取得
- linuxでファイルのハッシュを取得する
- linuxでファイルをハッシュ化する
cover: /img/cover/how-to-get-hashes-of-files-on-linux.webp
coverAlt: 未来的なLinuxターミナルがハッシュコマンドの出力を表示し、暗い背景に抽象的なファイルやデジタル記号が囲むイラスト。鮮やかな青、緑、紫のアクセント付き。
coverCaption: ''
---

**ガイド：組み込みツールを使ったLinuxでのファイルハッシュ取得方法**

## はじめに

Linuxシステムの世界では、ファイルハッシュの取得はデータ整合性の確保とファイルの真正性検証に不可欠です。ファイルハッシュは固有の識別子として機能し、改ざんの検出やデータ整合性の検証を可能にします。この包括的なガイドでは、組み込みツールを使ってLinux上でファイルの**SHA256**、**MD5**、**SHA1**ハッシュを取得する方法を探ります。ステップバイステップの手順に従い、具体的な例で学びましょう。

______

## 組み込みツールを使ったLinuxでのハッシュ取得

Linuxは追加ソフトウェアのインストールなしでファイルハッシュを計算できる複数の組み込みツールを提供しています。ここでは広く使われている3つのハッシュアルゴリズム、**SHA256**、**MD5**、**SHA1**を紹介します。

### SHA256ハッシュの取得

Linuxでファイルの**SHA256ハッシュ**を取得するには`sha256sum`コマンドを使用します。ターミナルを開き、ファイルがあるディレクトリに移動してください。次に以下のコマンドを実行します。

```bash
sha256sum file_path
```
`file_path`は実際のファイルパスに置き換えてください。

### MD5およびSHA1ハッシュの取得
同様のコマンドでLinux上のファイルの`MD5`と`SHA1 hashes`も取得できます。

- `MD5 hash`を取得するには:

```bash
md5sum file_path
```

- `SHA1 hash`を取得するには:

```bash
sha1sum file_path
```
両方のコマンドで`file_path`をファイルのパスに置き換えてください。

## 例
Linuxの組み込みツールを使ったハッシュ取得の具体例を見てみましょう。

{{< youtube id="3aX9zK88X9M" >}}

### 例1：SHA256ハッシュの取得
`document.pdf`というファイルが`/home/user/docs`ディレクトリにあるとします。このファイルの`SHA256 hash`をLinuxで取得するには、次のコマンドを実行します。

```bash
sha256sum /home/user/docs/document.pdf
```

出力にはファイルの`SHA256 hash`値が表示されます。

### 例2：MD5ハッシュの取得

`image.jpg`というファイルが`/home/user/pictures`ディレクトリに保存されているとします。このファイルの`MD5 hash`をLinuxで取得するには、次のコマンドを実行してください。

```bash
md5sum /home/user/pictures/image.jpg
```

ターミナルにファイルの`MD5 hash`値が表示されます。

## 例3：SHA1ハッシュの取得

`data.txt`というファイルが`/home/user/files`ディレクトリにある場合、このファイルの`SHA1 hash`をLinuxで取得するには、次のコマンドを実行します。

```bash
sha1sum /home/user/files/data.txt
```
出力にはファイルの`SHA1 hash`値が表示されます。

______

## 高度なLinuxハッシュ操作

### 複数ファイルの一括ハッシュ取得

```bash
# Hash all PDF files in directory
sha256sum /home/user/docs/*.pdf

# Hash all files recursively
find /home/user/data -type f -exec sha256sum {} \;
```

### ハッシュマニフェストファイルの作成

後で検証するためのハッシュを含むファイルを生成します。

```bash
# Create checksum file
sha256sum /home/user/important/* > checksums.txt

# Verify files against checksum file
sha256sum -c checksums.txt
```

ファイルが一致した場合の出力:
```
file1.txt: OK
file2.pdf: OK
file3.jpg: OK
```

### 期待値とのハッシュ比較

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

### 標準入力からのハッシュ取得

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

## 実用的なユースケース

### 1. ダウンロードしたISOの検証

Linuxディストリビューションはダウンロード検証用のハッシュチェックサムを提供しています。

```bash
# Download Ubuntu ISO hash
wget https://releases.ubuntu.com/SHA256SUMS

# Verify your downloaded ISO
sha256sum ubuntu-26.04-desktop-amd64.iso

# Compare against published hash
grep ubuntu-26.04-desktop-amd64.iso SHA256SUMS
```

### 2. ファイル改ざんの検出

重要なシステムファイルを監視します。

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

### 3. ファイルの重複排除

ハッシュを使って重複ファイルを見つけます。

```bash
# Find duplicates in directory
find /home/user/photos -type f -exec sha256sum {} \; | sort | uniq -w 64 -D
```

### 4. バックアップ整合性の検証

```bash
# Create hash manifest before backup
find /data -type f -exec sha256sum {} \; > /backup/manifest-$(date +%Y%m%d).txt

# After restore, verify
sha256sum -c /backup/manifest-20260524.txt
```

______

## 自動化スクリプト

### スクリプト1：再帰的ハッシュ生成器

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

### スクリプト2：ハッシュ検証ツール

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

### スクリプト3：ダウンロード検証

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

## パフォーマンス最適化

### 大容量ファイルの効率的なハッシュ化

非常に大きなファイルの場合、進行状況を監視できます。

```bash
# Using pv (pipe viewer) to show progress
pv large-file.iso | sha256sum

# Install pv if needed
sudo apt install pv  # Debian/Ubuntu
sudo dnf install pv  # Fedora
```

### 並列ハッシュ化

GNU Parallelを使って複数ファイルを並列でハッシュ化します。

```bash
# Install parallel
sudo apt install parallel

# Hash files in parallel (4 jobs)
find /data -type f | parallel -j 4 sha256sum {} > hashes.txt
```

### ハッシュアルゴリズムのベンチマーク

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

## ハッシュアルゴリズムのセキュリティ比較

| アルゴリズム | ハッシュ長 | 2026年の状態 | 用途 |
|-----------|-------------|-------------|----------|
| **SHA-256** | 256ビット (64文字) | ✅ 安全 | すべてのセキュリティ目的に推奨 |
| **SHA-512** | 512ビット (128文字) | ✅ 安全 | 機密データ向けの追加セキュリティ |
| **SHA-1** | 160ビット (40文字) | ⚠️ 非推奨 | レガシー互換性のみ |
| **MD5** | 128ビット (32文字) | ❌ 脆弱 | セキュリティ目的以外のみ |

**2026年の推奨**：セキュリティが重要な用途では常にSHA-256またはSHA-512を使用してください。

______

## パッケージマネージャとの統合

### APTパッケージの検証（Debian/Ubuntu）

```bash
# Check package integrity
debsums -c

# Verify specific package
debsums openssh-server
```

### RPMパッケージの検証（Fedora/RHEL）

```bash
# Check all packages
rpm -Va

# Verify specific package
rpm -V openssh-server
```

______

## 2026年のベストプラクティス

1. **SHA-256をデフォルトで使用**：現在のセキュリティ標準です
2. **MD5とSHA-1はセキュリティ目的で避ける**：レガシー互換性のみ
3. **検証には常に`-c`フラグを使う**：`sha256sum -c checksums.txt`
4. **チェックサムは別に保存する**：検証対象ファイルと一緒にハッシュを保存しない
5. **バイナリモードには`-b`を使う**：`sha256sum -b file.bin`（一部システムで重要）
6. **検証を自動化する**：重要ファイル監視用にcronジョブを作成
7. **スクリプトでは`--quiet`を使う**：OKメッセージを`sha256sum -c --quiet`で抑制

______

## トラブルシューティング

### 「No such file or directory」

**解決策**：スペースを含むパスは引用符で囲む:
```bash
sha256sum "/path/with spaces/file.txt"
```

### 「WARNING: X lines are improperly formatted」

**解決策**：チェックサムファイルの形式は以下の通りである必要があります:
```
hash_value  filename
```
ハッシュとファイル名の間に2つのスペースがあることに注意してください。

### Permission Denied

**解決策**：システムファイルにはsudoを使う:
```bash
sudo sha256sum /etc/shadow
```

______

## クロスプラットフォーム検証

### WindowsでLinuxハッシュを検証

```powershell
# PowerShell on Windows
Get-FileHash -Algorithm SHA256 file.txt
```

### macOSでLinuxハッシュを検証

```bash
# macOS uses shasum
shasum -a 256 file.txt
```

______

## 結論

Linuxはファイルハッシュ用に強力な組み込みツール（`sha256sum`、`md5sum`、`sha1sum`）を提供しています。ダウンロード検証、ファイル整合性監視、重複検出、バックアップの有効性確認など、これらのコマンドを習得することは2026年のシステム管理とセキュリティに不可欠です。

**主なポイント:**
- セキュリティ関連のハッシュには**sha256sum**を使用する
- `sha256sum * > checksums.txt`でハッシュマニフェストを作成する
- `sha256sum -c checksums.txt`でファイルを検証する
- 重要なファイルのハッシュチェックをスクリプトで自動化する
- セキュリティ目的でMD5とSHA-1は避ける

## 参考文献

1. [sha256sum - Linuxマニュアルページ](https://man7.org/linux/man-pages/man1/sha256sum.1.html)
2. [md5sum - Linuxマニュアルページ](https://man7.org/linux/man-pages/man1/md5sum.1.html)
3. [sha1sum - Linuxマニュアルページ](https://man7.org/linux/man-pages/man1/sha1sum.1.html)
4. [GNU Coreutils - チェックサム](https://www.gnu.org/software/coreutils/manual/html_node/Summarizing-files.html)
5. [NIST ハッシュ関数](https://csrc.nist.gov/projects/hash-functions)
