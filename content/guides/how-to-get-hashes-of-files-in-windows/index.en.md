---
title: "Complete Guide: File Hashes on Windows using PowerShell"
draft: false
toc: true
date: 2023-05-25
description: "Learn how to obtain file hashes on Windows using PowerShell, including SHA256, MD5, and SHA1, with step-by-step instructions and examples."
tags: ["file hashes", "PowerShell", "SHA256 hash", "MD5 hash", "SHA1 hash", "file integrity", "data authentication", "file verification", "hashing algorithms", "Windows operating system", "scripting language", "command-line shell", "data security", "digital forensics", "cybersecurity", "hash computation", "file tampering", "data integrity", "file authenticity", "Windows security", "file identification", "cyber defense", "file security", "data protection", "data verification", "file validation", "Windows PowerShell", "hash generation", "hash algorithms", "hash functions"]
cover: "/img/cover/A_cartoon_illustration_showing_a_file_with_a_lock_symbol.png"
coverAlt: "A cartoon illustration showing a file with a lock symbol and a magnifying glass, representing file hash verification and security."
coverCaption: ""
---

**How to Get Hashes of Files on Windows using PowerShell**

In the realm of computer security, obtaining file hashes is a crucial step in ensuring data integrity and verifying file authenticity. Hashes are unique identifiers generated for files, allowing users to detect tampering attempts and validate the integrity of data. In this comprehensive guide, we will explore the process of obtaining **SHA256**, **MD5**, and **SHA1** hashes of files on Windows using the powerful scripting language, **PowerShell**. Follow the step-by-step instructions and take a deep dive into specific examples. Let's get started!

______

## Obtaining Hashes on Windows using PowerShell

PowerShell, a versatile scripting language and command-line shell for Windows, offers the **Get-FileHash** cmdlet, enabling users to compute the hash of a file effortlessly.

### Obtaining the SHA256 Hash

To obtain the **SHA256 hash** of a file using PowerShell, follow these simple steps:

1. Launch PowerShell by opening the **Start menu**, searching for **PowerShell**, and selecting **Windows PowerShell**.
2. Navigate to the directory where the file is located. Use the `cd` command followed by the path to the directory.
3. Execute the following command to get the SHA256 hash of the file:
```powershell
   Get-FileHash -Algorithm SHA256 -Path "file_path"
```
### Obtaining the MD5 and SHA1 Hashes
You can also obtain the `MD5` and `SHA1` hashes of a file using PowerShell. Utilize the following commands:

- To obtain the `MD5 hash`:
  
```powershell
Get-FileHash -Algorithm MD5 -Path "file_path"
```

- To obtain the `SHA1 hash`:

```powershell
Get-FileHash -Algorithm SHA1 -Path "file_path"
```

Remember to replace "file_path" with the path to your file in both commands.

## Examples
Let's delve into specific examples to illustrate the process of obtaining hashes using PowerShell on Windows.

{{< youtube id="UrHhsF1q3rU" >}}

### Example 1: Obtaining SHA256 Hash
Imagine you have a file named `document.pdf` located in the directory `C:\Files`. To obtain the `SHA256 hash` of this file using PowerShell, execute the following command:

```powershell
Get-FileHash -Algorithm SHA256 -Path "C:\Files\document.pdf"
```

The output will display the SHA256 hash value of the file.

### Example 2: Obtaining MD5 Hash

Suppose you possess a file named `image.jpg` stored in the directory `C:\Photos`. To obtain the `MD5 hash` of this file using PowerShell, run the following command:

```powershell
Get-FileHash -Algorithm MD5 -Path "C:\Photos\image.jpg"
```

The terminal will display the MD5 hash value of the file.

### Example 3: Obtaining SHA1 Hash

Consider a scenario where you have a file named `data.txt` located in the directory `C:\Documents`. To obtain the `SHA1 hash` of this file using PowerShell, execute the following command:

```powershell
Get-FileHash -Algorithm SHA1 -Path "C:\Documents\data.txt"
```

The output will display the SHA1 hash value of the file.