---
title: "System-Wide Windows Ad Blocker: Preview, Apply, and Restore"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Block domains from the StevenBlack list on Windows with a PowerShell script that preserves your custom hosts entries."
tags: ["Windows 10", "ad-blocker", "telemetry blocking", "PowerShell script", "system-wide ad-blocking", "privacy", "security"]
cover: "/img/cover/System-Wide-Windows-Ad-Blocker.webp"
coverAlt: "A Windows 10 desktop with a PowerShell window showing ad-blocking script code, surrounded by abstract data packets being filtered, set against a dark background with vibrant colors."
coverCaption: ""
---

Block domains from the StevenBlack list on Windows with a PowerShell script that preserves your custom hosts entries.

## Set up and preview

Download and extract the complete repository. Review the [GitHub README](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) and script before running it. Open Windows PowerShell 5.1 or PowerShell 7 as administrator in the extracted folder. Test DNS and required apps on a disposable Windows system first.

Preview the change first. Run the second command separately only when ready to apply.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restore the original hosts file

Preview the restore first. Run the second command separately only when ready to restore.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Keep the backup intact until restore succeeds. If someone or another app edited the hosts file after the script applied changes, restore stops. Preserve and reconcile those edits before retrying.

## Block list

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Report a problem](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
