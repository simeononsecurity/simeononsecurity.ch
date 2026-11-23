---
title: "Script do bloqueador de anúncios em todo o sistema do Windows 10 para melhor privacidade e segurança"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Bloqueie domínios da lista StevenBlack no Windows com um script PowerShell que preserva as entradas personalizadas do arquivo hosts."
tags: ["Windows 10", "bloqueador de anúncios", "bloqueio de telemetria", "script do PowerShell", "bloqueio de anúncios em todo o sistema", "privacidade", "segurança"]
---

Bloqueie domínios da lista StevenBlack no Windows com um script PowerShell que preserva as entradas personalizadas do arquivo hosts.

## Preparação e prévia

Baixe e extraia o repositório completo. Leia o [README do GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) e revise o script antes de executá-lo. Na pasta extraída, abra o Windows PowerShell 5.1 ou o PowerShell 7 como administrador. Teste primeiro o DNS e os aplicativos necessários em um ambiente Windows descartável.

Confira primeiro a prévia das alterações. Execute o segundo comando separadamente só quando quiser aplicá-las.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restaurar o arquivo hosts original

Confira primeiro a prévia da restauração. Execute o segundo comando separadamente só quando quiser restaurar o arquivo.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Mantenha o backup intacto até a restauração terminar. Se alguém ou algum aplicativo editar o arquivo hosts depois da aplicação, a restauração será interrompida. Salve e concilie essas alterações antes de tentar novamente.

## Lista de bloqueio

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Relatar um problema](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
