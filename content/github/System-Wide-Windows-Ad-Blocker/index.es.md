---
title: "Script bloqueador de anuncios en todo el sistema de Windows 10 para una mejor privacidad y seguridad"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Bloquea en Windows los dominios de la lista StevenBlack con un script de PowerShell que conserva las entradas personalizadas del archivo hosts."
tags: ["Windows 10", "bloqueador de anuncios", "bloqueo de telemetría", "Script PowerShell", "bloqueo de anuncios en todo el sistema", "privacidad", "seguridad"]
---

Bloquea en Windows los dominios de la lista StevenBlack con un script de PowerShell que conserva las entradas personalizadas del archivo hosts.

## Preparación y vista previa

Descarga y extrae el repositorio completo. Revisa el [README de GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) y el script antes de ejecutarlo. Abre Windows PowerShell 5.1 o PowerShell 7 como administrador en la carpeta extraída. Prueba primero el DNS y las aplicaciones necesarias en un sistema Windows de pruebas que puedas descartar.

Revisa primero los cambios previstos. Ejecuta el segundo comando por separado solo cuando quieras aplicarlos.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restaurar el archivo hosts original

Revisa primero la vista previa de la restauración. Ejecuta el segundo comando por separado solo cuando quieras restaurar el archivo.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Mantén intacta la copia de seguridad hasta que termine la restauración. Si alguien o alguna aplicación modifica el archivo hosts después de aplicar los cambios, la restauración se detiene. Guarda y concilia esos cambios antes de volver a intentarlo.

## Lista de bloqueo

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Informar de un problema](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
