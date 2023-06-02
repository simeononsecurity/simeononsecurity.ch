---
title: "Maximiser l'audit de Windows avec le script de politique d'audit de Windows"
date: 2021-05-10
toc: true
draft: false
description: "Apprenez à maximiser l'audit de Windows en mettant en œuvre le script de stratégie d'audit de Windows pour améliorer la sécurité et la surveillance."
tags: ["Windows Audit Policy", "Audit Windows", "sécurité", "contrôle", "auditpol", "Windows commands", "Sécurité Windows", "audit configuration", "politiques de sécurité", "event logs", "surveillance du système", "Serveur Windows", "meilleures pratiques en matière de sécurité", "cybersécurité", "analyse du journal", "conformité en matière de sécurité", "incident response", "outils de contrôle de la sécurité", "accès privilégié", "Administration de Windows", "écriture", "l'administration du système", "la sécurité de l'information", "l'audit de conformité", "Durcissement des fenêtres", "contrôles de sécurité", "automatisation de la sécurité", "gestion des journaux", "Paramètres de sécurité de Windows"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Maximiser l'audit de Windows

## Lectures recommandées :
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Comment exécuter le script
### Installation manuelle :
S'il est téléchargé manuellement, le script doit être lancé à partir du répertoire contenant tous les autres fichiers du fichier [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
