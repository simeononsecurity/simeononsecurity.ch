---
title: "Heute habe ich etwas über die Erstellung benutzerdefinierter Windows-Abbilder gelernt"
date: 2023-01-30
toc: true
draft: false
description: "Heute habe ich etwas über die Erstellung benutzerdefinierter Windows-Abbilder, Sysprep und Generalisierung gelernt"
genre: ["Windows Image Management", "Personalisierung", "Windows-Bereitstellung", "Sysprep", "Verallgemeinerung", "Windows 10", "Fenster 11", "Bildeinzug", "Image-Bereitstellung", "NTLite", "Windows-Optimierung"]
tags: ["Sysprep", "NTLite", "Verallgemeinerung", "Benutzerdefinierte Bilder", "Custom Windows Images", "Fenster 11", "Debloat", "Personalisierung", "Bilderfassung", "Image-Bereitstellung", "Windows Bildverwaltung", "Windows-Bereitstellungswerkzeuge", "Windows-Bildanpassung", "Windows-Bildoptimierung", "Microsoft Lernen", "WinCustom-Repository"]
---

**Was SimeonOnSecurity heute erfahren und interessant gefunden hat**

Heute lernte SimeonOnSecurity den Prozess der Erfassung und Anwendung von Windows 10-Images mit DISM kennen, einem Befehlszeilen-Tool zur Verwaltung von Windows-Images. Um ein Image zu erfassen, kann man das Sysprep-Tool verwenden, um die Installation zu verallgemeinern, wodurch hardwarespezifische Informationen entfernt werden und das Image für die Bereitstellung auf mehreren Geräten vorbereitet wird.

SimeonOnSecurity hat verschiedene Ressourcen kennengelernt, die Informationen zum Erstellen und Anwenden von Windows-Images bereitstellen, darunter die Learn-Website von Microsoft und das WinCustom-Repository auf GitHub. Die Microsoft-Ressourcen behandeln die Grundlagen des Erfassens und Anwendens eines Windows-Abbilds mit einer einzelnen WIM-Datei, das Erstellen bootfähiger Windows PE-Medien und die Verallgemeinerung einer Windows-Installation mit Sysprep.

Außerdem lernte SimeonOnSecurity NTLite kennen, eine Software, die die Anpassung und Optimierung von Windows-Images ermöglicht. NTLite kann verwendet werden, um unnötige Komponenten aus einem Windows-Image zu entfernen, um Speicherplatz zu sparen und die Leistung zu verbessern.

Insgesamt vermittelte die heutige Recherche von SimeonOnSecurity ein umfassendes Verständnis für den Prozess der Erfassung und Anwendung von Windows-Images.

## Repos erstellt/aktualisiert:
- Keine / N/A

## Lernressourcen:
- [Learn How to Sysprep Capture Windows 10 Image using DISM](https://www.anoopcnair.com/sysprep-capture-windows-10-image-using-dism/)
- [Microsoft - Capture and apply a Windows image using a single .WIM file](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11)
- [Microsoft - Create bootable Windows PE media](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-create-usb-bootable-drive?view=windows-11)
- [Microsoft - Sysprep (Generalize) a Windows installation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
- [WinTenDev/WinCustom](https://github.com/WinTenDev/WinCustom)

## Besprochene und/oder eingesetzte Software:
- [NTLite](https://www.ntlite.com/)