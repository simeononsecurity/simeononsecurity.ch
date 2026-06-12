---
title: "PowerShell Get File Hash: Complete 2026 Guide to SHA256, MD5, SHA1 on Windows"
draft: false
toc: true
date: 2023-05-25
lastmod: 2026-05-24
description: "Complete guide to obtaining file hashes on Windows using PowerShell Get-FileHash. Learn SHA256, MD5, SHA1 hash verification, comparison, and automation for security and integrity checks in 2026."
tags: ["file hashes", "PowerShell", "SHA256 hash", "MD5 hash", "SHA1 hash", "file integrity", "data authentication", "file verification", "hashing algorithms", "Windows operating system", "scripting language", "command-line shell", "data security", "digital forensics", "cybersecurity", "hash computation", "file tampering", "data integrity", "file authenticity", "Windows security", "file identification", "cyber defense", "file security", "data protection", "data verification", "file validation", "Windows PowerShell", "hash generation", "hash algorithms", "hash functions", "PowerShell Get-FileHash", "Get-FileHash cmdlet", "PowerShell file hash", "verify file integrity", "hash comparison", "automate hash checks"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "A cartoon illustration showing a file with a lock symbol and a magnifying glass, representing file hash verification and security."
coverCaption: ""
---

**How to Get Hashes of Files on Windows using PowerShell: Complete 2026 Guide**

File hashes are cryptographic fingerprints that uniquely identify files, serving as essential tools for ensuring **data integrity** and **verifying file authenticity** in cybersecurity, digital forensics, and system administration. In this comprehensive guide, we'll explore how to use **PowerShell's Get-FileHash cmdlet** to obtain **SHA256**, **MD5**, and **SHA1** hashes on Windows systems, along with practical examples, automation techniques, and best practices for 2026.

## Introduction: Why File Hashes Matter

In computer security, **file hashes** (also called checksums or digests) are unique identifiers generated using cryptographic algorithms. They allow you to:

- **Verify file integrity**: Detect unauthorized modifications or corruption
- **Authenticate downloads**: Confirm software hasn't been tampered with
- **Track changes**: Identify when files have been modified
- **Digital forensics**: Create evidence chains for investigations
- **Malware detection**: Compare suspicious files against known malicious hashes

______

## Understanding Hashing Algorithms

### SHA256 (Recommended for Security)

**SHA-256** (Secure Hash Algorithm 256-bit) is the current industry standard for cryptographic hashing, producing a 256-bit (64-character hexadecimal) hash value. It's part of the SHA-2 family and is considered highly secure as of 2026.

**Use SHA-256 when:**
- Verifying software downloads
- Creating security-critical checksums
- Implementing digital signatures
- Meeting compliance requirements (NIST, FIPS 140-2)

### MD5 (Legacy, Not Recommended for Security)

**MD5** (Message Digest Algorithm 5) produces a 128-bit (32-character hexadecimal) hash. While fast to compute, MD5 is **cryptographically broken** and shouldn't be used for security purposes due to collision vulnerabilities discovered in 2004.

**MD5 is acceptable only for:**
- Non-security applications (file deduplication)
- Legacy system compatibility
- Quick integrity checks where security isn't critical

### SHA1 (Deprecated for Security)

**SHA-1** produces a 160-bit (40-character hexadecimal) hash. While more secure than MD5, SHA-1 is also **deprecated for security use** due to practical collision attacks demonstrated in 2017.

**Recommendation**: Use SHA-256 or SHA-512 instead of SHA-1 or MD5 for all security-related purposes.

______

## PowerShell Get-FileHash: The Essential Tool

PowerShell, Microsoft's powerful scripting language and command-line shell, includes the **Get-FileHash** cmdlet specifically designed for computing file hashes.

### Get-FileHash Syntax

```powershell
Get-FileHash [-Path] <String[]> [-Algorithm <String>] [<CommonParameters>]
```

**Parameters:**
- **-Path**: File path (required)
- **-Algorithm**: Hash algorithm to use (optional; default is SHA-256)
  - Available algorithms: SHA1, SHA256, SHA384, SHA512, MD5

### Launching PowerShell

1. Press **Win + X** and select **Windows PowerShell** or **Windows Terminal**
2. Alternatively, press **Win + R**, type `powershell`, and press Enter
3. For elevated privileges (if needed), right-click and select **Run as Administrator**

______

## Obtaining SHA256 Hash (Recommended Method)

**SHA-256 is the default and recommended algorithm** for Get-FileHash in PowerShell.

### Basic SHA256 Hash

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

### Example Output

```plaintext
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855   C:\Files\document.pdf
```

### SHA256 with Pipeline

You can pipe file objects to Get-FileHash:

```powershell
Get-Item "C:\Files\document.pdf" | Get-FileHash -Algorithm SHA256
```

### Getting Only the Hash Value

To display only the hash (useful for scripts):

```powershell
(Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf").Hash
```

Output:
```
E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855
```

______

## Obtaining MD5 Hash

### Basic MD5 Command

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

### Example Output

```plaintext
Algorithm       Hash                             Path
---------       ----                             ----
MD5             D41D8CD98F00B204E9800998ECF8427E C:\Photos\image.jpg
```

### Extract MD5 Hash Only

```powershell
(Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg").Hash
```

______

## Obtaining SHA1 Hash

### Basic SHA1 Command

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

### Example Output

```plaintext
Algorithm       Hash                                     Path
---------       ----                                     ----
SHA1            DA39A3EE5E6B4B0D3255BFEF95601890AFD80709 C:\Documents\data.txt
```

______

## Advanced PowerShell Hash Operations

### Hash Multiple Files

Process multiple files in a directory:

```powershell
Get-ChildItem "C:\Files\*.pdf" | Get-FileHash -Algorithm SHA256
```

### Export Hashes to CSV

Create a hash manifest for all files:

```powershell
Get-ChildItem "C:\ImportantFiles" -Recurse | 
    Get-FileHash -Algorithm SHA256 | 
    Export-Csv -Path "C:\Hashes\file-hashes.csv" -NoTypeInformation
```

### Format Output in Table

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\File.exe" | Format-Table -Property Algorithm, Hash, @{Label="FileName";Expression={Split-Path $_.Path -Leaf}}
```

### Compare File Hash Against Expected Value

```powershell
$expectedHash = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
$actualHash = (Get-FileHash -Algorithm SHA256 -Path "C:\Downloads\file.exe").Hash

if ($actualHash -eq $expectedHash) {
    Write-Host "✓ File integrity verified - Hash matches!" -ForegroundColor Green
} else {
    Write-Host "✗ WARNING: Hash mismatch - File may be compromised!" -ForegroundColor Red
    Write-Host "Expected: $expectedHash"
    Write-Host "Actual:   $actualHash"
}
```

### Hash All Files in Directory Tree

```powershell
Get-ChildItem "C:\ProjectFolder" -Recurse -File | 
    Get-FileHash -Algorithm SHA256 | 
    Select-Object Hash, Path | 
    Format-Table -AutoSize
```

______

## Practical Use Cases for File Hashes

### 1. Verifying Downloaded Software

When downloading software, publishers often provide hash values to verify authenticity:

```powershell
# Download hash from publisher's website (example)
$publishedHash = "A1B2C3D4E5F6..."

# Calculate hash of downloaded file
$downloadedHash = (Get-FileHash -Path "C:\Downloads\software-installer.exe").Hash

# Verify
if ($downloadedHash -eq $publishedHash) {
    Write-Host "Download verified - safe to install" -ForegroundColor Green
} else {
    Write-Host "DANGER: File has been modified - do not install!" -ForegroundColor Red
}
```

### 2. Detecting File Changes

Monitor critical system files for unauthorized modifications:

```powershell
# Create baseline
$baseline = Get-FileHash "C:\Windows\System32\drivers\etc\hosts"
$baseline.Hash | Out-File "C:\Baseline\hosts-hash.txt"

# Later, verify integrity
$currentHash = (Get-FileHash "C:\Windows\System32\drivers\etc\hosts").Hash
$baselineHash = Get-Content "C:\Baseline\hosts-hash.txt"

if ($currentHash -ne $baselineHash) {
    Write-Warning "hosts file has been modified!"
}
```

### 3. Digital Forensics

Create hash manifests for evidence preservation:

```powershell
# Hash all files in evidence directory
$evidencePath = "E:\CaseEvidence\2026-05-24"
Get-ChildItem $evidencePath -Recurse -File | 
    Get-FileHash -Algorithm SHA256 | 
    Select-Object Algorithm, Hash, Path, @{Name='Timestamp';Expression={Get-Date}} |
    Export-Csv "$evidencePath\evidence-hashes.csv" -NoTypeInformation

Write-Host "Evidence manifest created with $($(Get-ChildItem $evidencePath -Recurse -File).Count) file hashes"
```

### 4. Automated Malware Scanning

Compare files against known malware hashes (example with dummy hash database):

```powershell
# Load known malware hashes from file
$malwareHashes = Get-Content "C:\Security\malware-hashes.txt"

# Scan directory
$suspiciousFiles = Get-ChildItem "C:\Users\*\Downloads" -Recurse -File | 
    Get-FileHash -Algorithm SHA256 | 
    Where-Object { $malwareHashes -contains $_.Hash }

if ($suspiciousFiles) {
    Write-Host "⚠ MALWARE DETECTED:" -ForegroundColor Red
    $suspiciousFiles | Format-Table Path, Hash
} else {
    Write-Host "✓ No known malware detected" -ForegroundColor Green
}
```

______

## Automation: PowerShell Scripts for Hash Management

### Script 1: Batch Hash Generator

```powershell
# Generate-FileHashes.ps1
param(
    [Parameter(Mandatory=$true)]
    [string]$Path,
    
    [ValidateSet('SHA1','SHA256','SHA384','SHA512','MD5')]
    [string]$Algorithm = 'SHA256',
    
    [string]$OutputFile = "hashes-$(Get-Date -Format 'yyyyMMdd-HHmmss').csv"
)

Write-Host "Generating $Algorithm hashes for files in: $Path" -ForegroundColor Cyan

$hashes = Get-ChildItem -Path $Path -Recurse -File | 
    Get-FileHash -Algorithm $Algorithm |
    Select-Object Algorithm, Hash, @{Name='FileName';Expression={$_.Path}}

$hashes | Export-Csv -Path $OutputFile -NoTypeInformation
Write-Host "✓ Exported $($hashes.Count) hashes to: $OutputFile" -ForegroundColor Green
```

Usage:
```powershell
.\Generate-FileHashes.ps1 -Path "C:\ImportantData" -Algorithm SHA256
```

### Script 2: Hash Verification Tool

```powershell
# Verify-FileHashes.ps1
param(
    [Parameter(Mandatory=$true)]
    [string]$ManifestFile,
    
    [Parameter(Mandatory=$true)]
    [string]$Directory
)

$manifest = Import-Csv $ManifestFile
$mismatches = @()

Write-Host "Verifying $($manifest.Count) files..." -ForegroundColor Cyan

foreach ($entry in $manifest) {
    if (Test-Path $entry.Path) {
        $currentHash = (Get-FileHash -Path $entry.Path -Algorithm $entry.Algorithm).Hash
        if ($currentHash -ne $entry.Hash) {
            $mismatches += [PSCustomObject]@{
                Path = $entry.Path
                ExpectedHash = $entry.Hash
                ActualHash = $currentHash
            }
        }
    } else {
        Write-Warning "File not found: $($entry.Path)"
    }
}

if ($mismatches.Count -eq 0) {
    Write-Host "✓ All files verified successfully!" -ForegroundColor Green
} else {
    Write-Host "⚠ $($mismatches.Count) file(s) modified:" -ForegroundColor Red
    $mismatches | Format-Table -AutoSize
}
```

______

## Performance Considerations

### Hashing Large Files

For large files (>1 GB), hashing can take significant time:

- **SHA-256**: ~200-400 MB/s (depends on CPU)
- **MD5**: ~500-800 MB/s (faster but insecure)
- **SHA-512**: ~300-500 MB/s

### Optimize for Multiple Files

When hashing many files, use pipeline for efficiency:

```powershell
# Efficient: Single pipeline
Get-ChildItem "C:\Data" -Recurse | Get-FileHash -Algorithm SHA256

# Inefficient: Loop with individual calls
foreach ($file in Get-ChildItem "C:\Data" -Recurse) {
    Get-FileHash $file.FullName -Algorithm SHA256
}
```

______

## Best Practices for 2026

1. **Use SHA-256 as default**: It's the current security standard
2. **Never use MD5 or SHA-1 for security**: Only for legacy compatibility
3. **Store hashes securely**: Separate from the files themselves
4. **Automate verification**: Create scheduled tasks for critical files
5. **Document hash sources**: Record where published hashes came from
6. **Use digital signatures when available**: Hashes alone don't prove authenticity
7. **Consider SHA-512**: For highly sensitive data requiring extra security margin

______

## Troubleshooting

### "Get-FileHash: Cannot find path"

**Solution**: Use quotes around paths with spaces:
```powershell
Get-FileHash -Path "C:\Program Files\App\file.exe"
```

### Permission Denied Errors

**Solution**: Run PowerShell as Administrator or check file permissions:
```powershell
# Check if you can read the file
Test-Path -Path "C:\System\file.sys" -PathType Leaf
```

### Very Slow Performance

**Solution**: Close unnecessary applications and consider using faster algorithms for non-security purposes.

______

## Conclusion

PowerShell's Get-FileHash cmdlet provides a powerful, built-in solution for calculating file hashes on Windows. Whether you're verifying downloads, monitoring file integrity, conducting forensics, or automating security checks, mastering Get-FileHash is essential for modern Windows administration and cybersecurity in 2026.

**main points:**
- Use **SHA-256** for all security-related hashing
- Automate hash verification with PowerShell scripts
- Create baseline manifests for critical files
- Never trust files with mismatched hashes
- Combine hashes with digital signatures for complete verification

## Further Resources

1. [Microsoft PowerShell Documentation - Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash)
2. [NIST Hash Algorithms](https://csrc.nist.gov/projects/hash-functions)
3. [PowerShell Security Best Practices](https://learn.microsoft.com/en-us/powershell/scripting/security/overview)
