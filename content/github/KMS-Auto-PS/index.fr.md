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

 Script d'installation automatique GLVK pour l'activation KMS  ## Conférence recommandée : - [Microsoft - Clés client KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)  ## Commentez le script : ### Installation manuelle : S'il est téléchargé manuellement, le script doit être lancé à partir d'un powershell administratif dans le répertoire contenant tous les fichiers du [GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/ principal.zip)