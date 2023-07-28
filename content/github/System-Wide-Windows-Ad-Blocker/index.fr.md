---
title: "Script de blocage des publicités pour l'ensemble du système Windows 10 pour une meilleure protection de la vie privée et de la sécurité"
date: 2021-04-02
toc: true
draft: false
description: "Bloquez les publicités, les traqueurs et la télémétrie sur Windows 10 à l'aide de ce puissant script PowerShell qui utilise le fichier hosts et le pare-feu Windows pour bloquer les publicités à l'échelle du système."
tags: ["Windows 10", "bloqueur de publicité", "blocage de la télémétrie", "Script PowerShell", "blocage des publicités à l'échelle du système", "vie privée", "sécurité", "EasyList", "Protection de la vie privée", "Liste de filtres NoCoin", "Filtre DNS AdGuard", "Listes YoYo", "Les serveurs malveillants de Peter Lowe pour le suivi des publicités", "Pare-feu Windows", "listes de domaines", "Bloquer les traqueurs Windows", "traqueurs de blocs", "bloquer les publicités", "suivi des blocs"]
---

**Système-Wide-Windows-Ad-Blocker**

[![VirusTotal Scan](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/actions/workflows/virustotal.yml)

Ce script est un script Windows PowerShell qui télécharge et applique le fichier "StevenBlack/hosts" au fichier "hosts" du système, qui peut être utilisé pour bloquer certains domaines/sites web en les faisant correspondre à une adresse IP de votre choix (généralement l'adresse IP de la machine locale). Le script vérifie la connexion internet et les paramètres du proxy, et tente de télécharger la dernière version du fichier "hosts" à partir de deux sources différentes : "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" et "http://sbc.io/hosts/hosts". Si le téléchargement échoue, le script continue avec une copie locale du fichier "hosts". Le script nécessite des privilèges élevés pour s'exécuter et modifie la clé de registre ".NETFramework" afin de n'utiliser que la dernière version de .NET framework.

*Nous sommes à la recherche de tous les commentaires et de toutes les préoccupations concernant ce repo. Veuillez soumettre un [issue](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues) avec toute information que vous pourriez avoir.*

### Listes utilisées :
- [StevenBlack/hosts - adware + malware](https://github.com/StevenBlack/hosts)

### Exemple :
#### Installation manuelle :
**Le script peut être lancé à partir du téléchargement GitHub extrait comme ceci:**
```powershell
.\sos-system-wide-windows-ad-block.ps1
```
#### Installation automatisée :
Exécutez automatiquement la dernière version du script :
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/soswindowsadblocker.ps1' | iex
```

