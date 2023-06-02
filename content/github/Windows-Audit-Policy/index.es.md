---
title: "Maximice la Auditoría de Windows con el Script de Políticas de Auditoría de Windows"
date: 2021-05-10
toc: true
draft: false
description: "Aprenda a maximizar la auditoría de Windows implementando la secuencia de comandos de la directiva de auditoría de Windows para mejorar la seguridad y la supervisión."
tags: ["Política de auditoría de Windows", "Auditoría de Windows", "seguridad", "control", "auditpol", "Comandos de Windows", "Seguridad de Windows", "configuración de auditoría", "políticas de seguridad", "registros de eventos", "supervisión del sistema", "Servidor Windows", "buenas prácticas de seguridad", "ciberseguridad", "análisis de registros", "cumplimiento de las normas de seguridad", "respuesta a incidentes", "herramientas de supervisión de la seguridad", "acceso privilegiado", "Administración de Windows", "scripting", "administración del sistema", "seguridad de la información", "auditoría de conformidad", "Endurecimiento de Windows", "controles de seguridad", "automatización de la seguridad", "gestión de registros", "Configuración de seguridad de Windows"]
---

## Política de auditoría de Windows

[![VirusTotal Scan](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml/badge.svg)](https://github.com/simeononsecurity/Windows-Audit-Policy/actions/workflows/virustotal.yml)

Maximizar la auditoría de Windows

## Material de lectura recomendado:
  - [auditpol](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol)
  - [auditpol clear](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-clear)
  - [auditpol backup](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-backup)
  - [auditpol restore](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-restore)
  - [auditpol list](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/auditpol-list)

## Cómo ejecutar el script
### Instalación manual:
Si se descarga manualmente, el script debe lanzarse desde el directorio que contiene todos los demás archivos del archivo [GitHub Repository](https://github.com/simeononsecurity/Windows-Audit-Policy)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-auditpolicy.ps1
```
