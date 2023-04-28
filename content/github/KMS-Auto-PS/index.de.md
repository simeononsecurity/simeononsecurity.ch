---
title: "Automate Windows KMS Activation with GLVK Script"
date: 2020-12-18
toc: true
draft: false
description: "Simplify the Windows 10 KMS activation process using SimeonOnSecurity's GLVK Auto Install Script, and learn more about KMS and GLVK client keys from Microsoft's recommended reading."
tags: ["Windows Activation", "KMS Client Keys", "GLVK", "Windows Updates", "Compliance", "Powershell Script", "Key Management Service", "Volume Licensing", "Enterprise Activation", "Key Management Server", "Automation", "Microsoft Products", "Operating System", "Software", "Enterprise Environments", "Administrative Powershell", "GitHub Repository", "Scripting", "Cybersecurity", "SimeonOnSecurity"]
---
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

 Automatisches GLVK-Installationsskript für die KMS-Aktivierung  ## Empfohlene Vorlesungen: - [Microsoft – KMS-Clientschlüssel (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)  ## So führen Sie das Skript aus: ### Manuelle Installation: Wenn es manuell heruntergeladen wird, muss das Skript von einer administrativen Powershell in dem Verzeichnis gestartet werden, das alle Dateien aus dem [GitHub-Repository] (https://github.com/simeononsecurity/KMS-Auto-PS/archive/main. zip) enthält.