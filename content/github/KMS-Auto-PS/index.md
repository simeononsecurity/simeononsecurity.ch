---
title: "Automate Windows KMS Activation with GLVK Script"
date: 2020-12-18
toc: true
draft: false
description: "Simplify the Windows 10 KMS activation process using SimeonOnSecurity's GLVK Auto Install Script, and learn more about KMS and GLVK client keys from Microsoft's recommended reading."
tags: ["Windows Activation", "KMS Client Keys", "GLVK", "Windows Updates", "Compliance", "Powershell Script", "Key Management Service", "Volume Licensing", "Enterprise Activation", "Key Management Server", "Automation", "Microsoft Products", "Operating System", "Software", "Enterprise Environments", "Administrative Powershell", "GitHub Repository", "Scripting", "Cybersecurity", "SimeonOnSecurity"]
---

# SimeonOnSecurity - KMS-Auto-PS
GLVK Auto Install Script for KMS Activation

## Recommened Reading:
- [Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## How to run the script:
### Manual Install:
If manually downloaded, the script must be launched from an administrative powershell in the directory containing all the files from the [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```
