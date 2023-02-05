---
title: "KMS Activation Automation with GLVK Auto Install Script - SimeonOnSecurity"
date: 2020-12-18
toc: true
draft: false
description: "Get Windows 10 KMS Activation with ease using SimeonOnSecurity's GLVK Auto Install Script. Download the script from GitHub and launch it from an administrative PowerShell for a hassle-free setup. Learn more about Windows Key Management Service (KMS) and GLVK client keys with recommended reading from Microsoft."
tags: ["Automation", "Windows Activation", "Windows Updates", "Compliance", "Windows 10 KMS", "GLVK", "Powershell Script", "Key Management Service", "Volume Licensing", "Enterprise Activation", "Key Management Server"]
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
