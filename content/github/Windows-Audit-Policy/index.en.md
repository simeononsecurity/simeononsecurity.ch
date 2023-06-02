---
title: "Maximize Windows Auditing with Windows Audit Policy Script"
date: 2021-05-10
toc: true
draft: false
description: "Learn how to maximize Windows auditing by implementing the Windows Audit Policy script to enhance security and monitoring."
tags: ["Windows Audit Policy", "Windows auditing", "security", "monitoring", "auditpol", "Windows commands", "Windows security", "audit configuration", "security policies", "event logs", "system monitoring", "Windows server", "security best practices", "cybersecurity", "log analysis", "security compliance", "incident response", "security monitoring tools", "privileged access", "Windows administration", "scripting", "system administration", "information security", "compliance auditing", "Windows hardening", "security controls", "security automation", "log management", "Windows security settings"]
---

## Windows-Audit-Policy

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Max out Windows Auditing

## Recommended reading material:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## How to run the script
### Manual Install:
If manually downloaded, the script must be launched from the directory containing all the other files from the [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
