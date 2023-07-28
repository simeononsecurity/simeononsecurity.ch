---
title: "PowerShell DSC: Ein Einstiegshandbuch"
date: 2023-04-02
toc: true
draft: false
description: "Entdecken Sie die Leistungsfähigkeit von PowerShell Desired State Configuration (DSC) zur Automatisierung und Verwaltung von Systemkonfigurationen für eine sichere und konforme Umgebung."
tags: ["PowerShell", "DSC", "Konfigurationsmanagement", "Automatisierung", "Windows", "Systemverwaltung", "Bewährte Praktiken", "Einhaltung der Vorschriften", "Sicherheit", "Infrastruktur", "DevOps", "Server-Konfiguration", "Prüfung", "Git", "Quellenkontrolle", "Staatliche Vorschriften", "NIST", "CIS", "Konfiguration Drift", "Benutzerdefinierte Ressourcen"]
cover: "/img/cover/A_cartoon_image_of_a_confident_system_administrator.png"
coverAlt: "Ein Cartoon-Bild eines selbstbewussten Systemadministrators mit einem Superhelden-Umhang, der neben einem gut organisierten Server-Rack steht, ein PowerShell DSC-Skript in der einen und ein Schild mit dem Windows-Logo in der anderen Hand hält und die Server vor Konfigurationsabweichungen und Sicherheitsbedrohungen schützt."
coverCaption: ""
---

**Ein Leitfaden zur Verwendung von PowerShell Desired State Configuration (DSC) für die Konfigurationsverwaltung**

______

## Einführung

PowerShell Desired State Configuration (**DSC**) ist ein leistungsstarkes und **unverzichtbares Tool** für IT-Administratoren und DevOps-Experten, mit dem sie die Bereitstellung und Konfiguration von Windows- und Linux-Systemen automatisieren können. Dieser Artikel bietet eine umfassende Anleitung zur Verwendung von PowerShell DSC für die Konfigurationsverwaltung, einschließlich bewährter Verfahren, gesetzlicher Vorschriften und nützlicher Referenzen.

______

## Erste Schritte mit PowerShell Desired State Configuration

### Was ist PowerShell Desired State Configuration?

PowerShell Desired State Configuration (**DSC**) ist eine in PowerShell integrierte **Erklärungssprache**, mit der Administratoren die Konfiguration von Systemen, Anwendungen und Diensten automatisieren können. Sie bietet eine **standardisierte und konsistente** Möglichkeit, Konfigurationen zu verwalten und sicherzustellen, dass Systeme im gewünschten Zustand bleiben.

### Installieren von PowerShell DSC

Um mit PowerShell DSC beginnen zu können, müssen Sie das **Windows Management Framework (WMF)** installieren. WMF ist ein Paket, das PowerShell, DSC und andere wichtige Verwaltungstools enthält. Sie können die neueste Version von WMF von der [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=54616)

______

## Erstellen und Anwenden von DSC-Konfigurationen

### DSC-Konfigurationen schreiben

Eine DSC-Konfiguration ist ein **PowerShell-Skript**, das den gewünschten Zustand eines Systems beschreibt. Sie besteht aus einer oder mehreren **DSC-Ressourcen**, die die für die Komponenten des Systems erforderlichen Einstellungen und Eigenschaften definieren. Im Folgenden finden Sie ein Beispiel für eine einfache DSC-Konfiguration, die die Webserver (IIS)-Rolle auf einem Windows-Server installiert:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### Anwenden von DSC-Konfigurationen
Sobald Sie eine DSC-Konfiguration geschrieben haben, können Sie sie mit dem Cmdlet **Start-DscConfiguration** auf ein Zielsystem anwenden. Kompilieren Sie zunächst das Konfigurationsskript, indem Sie es in PowerShell ausführen:

```powershell
InstallIIS
```

Dadurch wird eine **MOF**-Datei (Managed Object Format) erzeugt, die die kompilierte Konfiguration enthält. Als Nächstes wenden Sie die Konfiguration mit dem folgenden Befehl auf das Zielsystem an:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## Bewährte Praktiken für die Verwendung von PowerShell DSC

## Modularisieren Sie Ihre Konfigurationen

Erstellen Sie **modulare und wiederverwendbare** Konfigurationen, indem Sie die verschiedenen Komponenten Ihrer Infrastruktur in **einzelne DSC-Ressourcen** aufteilen. Mit diesem Ansatz können Sie Ihre Konfigurationen leicht **verwalten und skalieren**, wenn Ihre Umgebung wächst.

### Source Control verwenden

Speichern Sie Ihre DSC-Konfigurationen und benutzerdefinierten Ressourcen immer in einem **Source Control System** wie Git. Auf diese Weise können Sie Änderungen nachverfolgen, mit Ihrem Team zusammenarbeiten und bei Bedarf einfach auf frühere Versionen Ihrer Konfigurationen zurückgreifen.

### Testen Sie Ihre Konfigurationen

**Testen** ist ein wichtiger Aspekt des Konfigurationsmanagements. Bevor Sie eine DSC-Konfiguration bereitstellen, sollten Sie sie in einer **nicht-produktiven Umgebung** testen, um sicherzustellen, dass sie wie erwartet funktioniert und keine unbeabsichtigten Folgen hat. Sie können auch Tools verwenden wie [Pester](https://github.com/pester/Pester) für automatisierte Tests Ihrer DSC-Konfigurationen.

______

## Staatliche Vorschriften und Richtlinien

### NIST-Richtlinien

Das National Institute of Standards and Technology (NIST) bietet Richtlinien für das Systemkonfigurationsmanagement. Insbesondere die [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) publication contains a section (CM-2) über Basiskonfigurationen, die für die Verwendung von DSC relevant ist. Die Richtlinien betonen die Bedeutung der Pflege, Überwachung und Kontrolle von Änderungen an Systemkonfigurationen. PowerShell DSC kann Unternehmen dabei helfen, diese Richtlinien einzuhalten, indem es eine konsistente und automatisierte Methode zur Verwaltung von Systemkonfigurationen bietet.

### Federal Information Security Management Act (FISMA)

Der Federal Information Security Management Act (Gesetz zur Verwaltung der Informationssicherheit) [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) verlangt von Bundesbehörden die Implementierung eines umfassenden Rahmens zur Gewährleistung der Wirksamkeit ihrer Informationssicherheitskontrollen. Die Konfigurationsverwaltung ist eine Schlüsselkomponente der FISMA-Konformität, und PowerShell DSC kann eine wichtige Rolle dabei spielen, Organisationen bei der Erfüllung dieser Anforderungen zu unterstützen.
______

## Schlussfolgerung

PowerShell Desired State Configuration (DSC) ist ein leistungsstarkes und flexibles Tool zur Automatisierung der Bereitstellung und Verwaltung von Systemkonfigurationen. Durch die Befolgung von Best Practices und die Einhaltung gesetzlicher Vorschriften können Sie sicherstellen, dass die Systeme Ihres Unternehmens im gewünschten Zustand bleiben und gleichzeitig die Compliance eingehalten wird. Vergessen Sie nicht, die in diesem Artikel bereitgestellten Ressourcen zu nutzen, um Ihr Verständnis von PowerShell DSC zu erweitern und Ihre Konfigurationsverwaltungsprozesse zu verbessern.
______

## Referenzen

- [PowerShell Desired State Configuration (DSC) official documentation](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - Security and Privacy Controls for Federal Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - PowerShell Testing Framework](https://github.com/pester/Pester)
- [A Beginner's Guide to Using Encryption for Data Protection](https://simeononsecurity.ch/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Best Practices for Installing Security Patches on Windows](https://simeononsecurity.ch/articles/best-practices-for-installing-security-patches-on-windows/)




