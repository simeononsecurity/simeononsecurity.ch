---
title: "Script de blocage des publicités pour l'ensemble du système Windows 10 pour une meilleure protection de la vie privée et de la sécurité"
date: 2021-04-02
lastmod: 2026-11-23
toc: true
draft: false
description: "Bloquez les domaines de la liste StevenBlack sous Windows avec un script PowerShell qui conserve vos entrées personnalisées dans le fichier hosts."
tags: ["Windows 10", "bloqueur de publicité", "blocage de la télémétrie", "Script PowerShell", "blocage des publicités à l'échelle du système", "vie privée", "sécurité"]
---

Bloquez les domaines de la liste StevenBlack sous Windows avec un script PowerShell qui conserve vos entrées personnalisées dans le fichier hosts.

## Préparer et prévisualiser

Téléchargez et extrayez le dépôt complet. Lisez le [README de GitHub](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/blob/main/README.md) et relisez le script avant de l’exécuter. Ouvrez Windows PowerShell 5.1 ou PowerShell 7 en tant qu’administrateur dans le dossier extrait. Testez d’abord le DNS et les applications nécessaires sur un système Windows de test que vous pouvez supprimer.

Prévisualisez les changements. Exécutez la seconde commande séparément lorsque vous êtes prêt à les appliquer.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1
```

## Restaurer le fichier hosts d’origine

Prévisualisez la restauration. Exécutez la seconde commande séparément lorsque vous êtes prêt à restaurer le fichier.

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore -WhatIf
```

```powershell
.\sos-system-wide-windows-ad-block.ps1 -Mode Restore
```

Gardez la sauvegarde intacte jusqu’à la réussite de la restauration. Si une personne ou une application modifie le fichier hosts après l’application des changements, la restauration s’arrête. Sauvegardez ces modifications et rapprochez-les du contenu à restaurer avant de réessayer.

## Liste de blocage

- [StevenBlack/hosts](https://github.com/StevenBlack/hosts)
- [Signaler un problème](https://github.com/simeononsecurity/System-Wide-Windows-Ad-Blocker/issues)
