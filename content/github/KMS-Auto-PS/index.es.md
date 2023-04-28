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

 Script de instalación automática de GLVK para la activación de KMS  ## Lectura recomendada: - [Microsoft - Claves de cliente KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)  ##ejecutar cómo el script: ### Manual de instalación: Si se descarga manualmente, el script debe iniciarse desde un powershell administrativo en el directorio que contiene todos los archivos del [repositorio de GitHub] (https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)