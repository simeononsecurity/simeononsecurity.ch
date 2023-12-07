---
title: "Beherrschen der Active Directory-Verwaltung mit PowerShell: Handbuch zur Installation und Verwendung"
date: 2023-07-25
toc: true
draft: false
description: "Erfahren Sie, wie Sie das Active Directory-Modul für PowerShell effektiv installieren und verwenden, um Ihre Windows Active Directory-Verwaltungsaufgaben zu rationalisieren."
genre: ["Technologie", "Windows", "PowerShell", "Aktives Verzeichnis", "Verwaltung", "Skripting", "IT", "Automatisierung", "Windows-Server", "Microsoft"]
tags: ["Active Directory-Modul für PowerShell", "Importmodul aktives Verzeichnis in PowerShell", "Active Directory-Modul für Windows PowerShell", "Active Directory PowerShell-Installation", "Active Directory PowerShell installieren", "PowerShell installieren Active Directory-Modul Windows 10", "Active Directory PowerShell-Modul installieren Windows 10", "get active directory PowerShell-Modul", "AD-Verwaltung", "Windows Active Directory", "PowerShell-Cmdlets", "Abrufen von AD-Informationen", "AD-Objekte erstellen", "AD-Objekte ändern", "AD-Sicherheit verwalten", "AD-Benutzerverwaltung", "AD-Gruppenverwaltung", "AD ODER Management", "PowerShell-Skripterstellung", "Verwaltung von Windows Server", "Microsoft PowerShell", "AD-Aufgaben automatisieren", "Installation des PowerShell-Moduls", "AD-Verwaltungshandbuch", "Active Directory-Verwaltung", "AD-Sicherheitsmanagement", "PowerShell-Automatisierung", "Active Directory PowerShell-Befehle", "PowerShell Cmdlet-Referenz"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Ein Bild, das ein Netzwerk aus miteinander verbundenen Servern und Benutzersymbolen darstellt und die Verwaltung und Automatisierung von Active Directory symbolisiert."
coverCaption: "Erschließen Sie die Möglichkeiten der Active Directory-Verwaltung mit PowerShell."
---

## Einleitung

In der heutigen digitalen Landschaft erfordert die Verwaltung und Pflege von Benutzerkonten, Sicherheitsgruppen und anderen Ressourcen in einer Windows Active Directory (AD)-Umgebung effiziente und rationalisierte Prozesse. PowerShell, eine leistungsstarke, von Microsoft entwickelte Skriptsprache, bietet das **Active Directory-Modul**, um AD-Verwaltungsaufgaben zu erleichtern. Dieses Modul bietet eine breite Palette von Cmdlets, mit denen Administratoren verschiedene Vorgänge automatisieren und AD effektiv verwalten können. In diesem Artikel werden wir die Installation und Verwendung des Active Directory-Moduls für PowerShell untersuchen.

## Installation des Active Directory-Moduls für PowerShell

Um mit der Verwendung des Active Directory-Moduls für PowerShell zu beginnen, müssen Sie sicherstellen, dass es auf Ihrem System installiert ist. Der Installationsprozess kann je nach Betriebssystem variieren. Im Folgenden werden die Schritte zur Installation des Moduls unter **Windows 10**, **Windows 11** und **Windows Server** beschrieben:

### Windows 10 und Windows 11 - PowerShell
1. Öffnen Sie **Windows PowerShell** mit administrativen Rechten.
2. Führen Sie den folgenden Befehl aus, um das Modul zu installieren:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Warten Sie, bis die Installation abgeschlossen ist. Sobald die Installation abgeschlossen ist, können Sie das Active Directory-Modul verwenden.

### Windows Server
1. Öffnen Sie **Windows PowerShell** mit administrativen Rechten.
2. Führen Sie den folgenden Befehl aus, um das Modul zu installieren:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Warten Sie, bis die Installation abgeschlossen ist. Sobald die Installation abgeschlossen ist, können Sie das Active Directory-Modul verwenden.

### Offline-Systeme

Offline-Systeme sind ein wenig komplizierter. Es gibt mehrere Methoden, aber die von uns empfohlene ist die Verwendung des folgenden Skripts:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importieren des Active Directory-Moduls in PowerShell

Bevor Sie das Active Directory-Modul in PowerShell verwenden können, müssen Sie es in Ihre aktuelle Sitzung importieren. Führen Sie die folgenden Schritte aus, um das Modul zu importieren:

1. Starten Sie **Windows PowerShell** mit Administratorrechten.
2. Führen Sie den folgenden Befehl aus, um das Modul zu importieren:

```powershell
Import-Module ActiveDirectory
```

3. Das Active Directory-Modul wird importiert, und Sie können nun auf seine Cmdlets und Funktionen zugreifen.

## Verwenden des Active Directory-Moduls für PowerShell

Nachdem Sie das Active Directory-Modul importiert haben, können Sie die zahlreichen Cmdlets nutzen, um verschiedene Verwaltungsaufgaben auszuführen. Sehen wir uns einige häufig verwendete Cmdlets und ihre Funktionen an:

### Abrufen von Active Directory-Informationen

Um eine Active Directory (AD)-Umgebung effektiv zu verwalten, ist es wichtig, Informationen über verschiedene AD-Objekte, wie Benutzer, Gruppen und Organisationseinheiten (OUs), abzurufen. PowerShell bietet leistungsstarke Cmdlets, die den Abrufprozess vereinfachen.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Mit diesem Cmdlet können Sie detaillierte Informationen über AD-Benutzer abrufen. Sie können Attribute wie Benutzernamen, Anzeigenamen, E-Mail-Adressen und mehr abrufen. Um beispielsweise alle Benutzer abzurufen, deren Benutzernamen mit "johndoe" beginnen, können Sie den folgenden Befehl ausführen:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Dieser Befehl gibt eine Liste der Benutzerobjekte zurück, die dem angegebenen Filter entsprechen.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Mit dem Cmdlet "Get-ADGroup" können Sie Informationen über AD-Gruppen abrufen. Es bietet Zugriff auf Details wie Gruppenname, Mitglieder, Beschreibung und mehr. Um zum Beispiel alle Sicherheitsgruppen in der AD-Umgebung abzurufen, können Sie den folgenden Befehl ausführen:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Dadurch wird eine Liste der Sicherheitsgruppen im Active Directory angezeigt.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) Das Cmdlet "Get-ADOrganizationalUnit" wird zum Abrufen von Informationen über AD OUs verwendet. Es ermöglicht Ihnen den Zugriff auf Eigenschaften wie OU-Name, Beschreibung, übergeordnete OU und mehr. Um alle OUs in der Domäne abzurufen, können Sie den folgenden Befehl verwenden:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Wenn Sie diesen Befehl ausführen, wird eine Liste aller OUs im Active Directory angezeigt.

Mithilfe dieser leistungsstarken Cmdlets können Sie ganz einfach spezifische Informationen über AD-Benutzer, -Gruppen und -OUs abrufen und so eine effiziente Verwaltung Ihrer Active Directory-Umgebung ermöglichen.


Mit diesen Cmdlets können Sie bestimmte Attribute abrufen, Ergebnisse filtern und erweiterte Abfragen durchführen, um die gewünschten Informationen abzurufen.

### Erstellen und Verwalten von Active Directory-Objekten

Bei der Arbeit mit Active Directory (AD) bietet das Active Directory-Modul in PowerShell leistungsstarke Cmdlets zum Erstellen und Verwalten von AD-Objekten. Im Folgenden werden einige wichtige Cmdlets zum Erstellen von AD-Benutzern, Gruppen und Organisationseinheiten (OUs) vorgestellt.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Mit diesem Cmdlet können Sie einen neuen AD-Benutzer erstellen. Sie können Attribute wie den Benutzernamen, das Kennwort, die E-Mail-Adresse und mehr angeben. Um zum Beispiel einen neuen Benutzer mit dem Benutzernamen "john.doe" und dem Anzeigenamen "John Doe" zu erstellen, können Sie den folgenden Befehl verwenden:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Mit diesem Befehl wird ein neuer Benutzer im Active Directory erstellt.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) Mit dem Cmdlet "New-ADGroup" können Sie eine neue AD-Gruppe erstellen. Sie können Eigenschaften wie Gruppenname, Beschreibung, Gruppenumfang und mehr festlegen. Um eine neue Gruppe mit dem Namen "Marketing" und einer Beschreibung zu erstellen, können Sie den folgenden Befehl ausführen:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Mit diesem Befehl wird eine neue Gruppe im Active Directory erstellt.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Mit dem Cmdlet New-ADOrganizationalUnit können Sie eine neue AD OU erstellen. Sie können Eigenschaften wie den OU-Namen, die übergeordnete OU und mehr angeben. Um beispielsweise eine neue OU mit dem Namen "Vertrieb" unter der OU "Abteilungen" zu erstellen, können Sie den folgenden Befehl ausführen:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Mit diesem Befehl wird eine neue OU in der Active Directory-Hierarchie erstellt.

Mithilfe dieser Cmdlets können Sie problemlos neue AD-Benutzer, -Gruppen und -OUs mit den gewünschten Eigenschaften und Konfigurationen erstellen und so eine effiziente Verwaltung Ihrer Active Directory-Umgebung ermöglichen.


### Ändern von Active Directory-Objekten

Für die Änderung der Eigenschaften und Attribute vorhandener Active Directory (AD)-Objekte bietet das Active Directory-Modul in PowerShell mehrere nützliche Cmdlets. Im Folgenden werden diese Cmdlets zum Ändern von AD-Benutzern, -Gruppen und -Organisationseinheiten (OUs) erläutert.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) Mit dem Cmdlet "Set-ADUser" können Sie die Eigenschaften eines AD-Benutzers ändern. Sie können Attribute wie Anzeigename, E-Mail-Adresse, Telefonnummer und mehr aktualisieren. Um zum Beispiel die Telefonnummer eines Benutzers mit dem Benutzernamen "john.doe" zu ändern, können Sie den folgenden Befehl verwenden:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Mit diesem Befehl wird die Telefonnummer des angegebenen Benutzers im Active Directory geändert.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Mit dem Cmdlet "Set-ADGroup" können Sie die Eigenschaften einer AD-Gruppe ändern. Sie können Attribute wie Gruppenbeschreibung, Mitgliedschaft, Gruppenumfang und mehr aktualisieren. Um die Beschreibung einer Gruppe namens "Marketing" in "Marketing Team" zu ändern, können Sie den folgenden Befehl ausführen:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Mit diesem Befehl wird die Beschreibung der angegebenen Gruppe im Active Directory aktualisiert.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) Mit dem Cmdlet Set-ADOrganizationalUnit können Sie die Eigenschaften einer AD OU ändern. Sie können Attribute wie den OU-Namen, die Beschreibung und mehr ändern. Um beispielsweise die Beschreibung einer OU mit dem Namen "Vertrieb" in "Vertriebsabteilung" zu ändern, können Sie den folgenden Befehl ausführen:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Mit diesem Befehl wird die Beschreibung der angegebenen OU in der Active Directory-Hierarchie aktualisiert.

Mithilfe dieser Cmdlets können Sie die Eigenschaften und Attribute von AD-Objekten leicht ändern und die erforderlichen Aktualisierungen und Anpassungen vornehmen, um die Anforderungen Ihres Unternehmens zu erfüllen.


### Active Directory-Sicherheit verwalten

Neben der Verwaltung und Administration von Active Directory (AD)-Objekten bietet das Active Directory-Modul in PowerShell Cmdlets, die speziell für sicherheitsbezogene Aspekte von AD entwickelt wurden. Diese Cmdlets ermöglichen Administratoren die effiziente Verwaltung von Benutzerzugriff, Gruppenmitgliedschaften und kennwortbezogenen Aufgaben innerhalb der AD-Umgebung.

Hier sind einige häufig verwendete sicherheitsbezogene Cmdlets:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Mit diesem Cmdlet können Sie Mitglieder zu einer AD-Gruppe hinzufügen. Durch Angabe der AD-Gruppe und der Benutzerkonten oder Gruppen, die Sie hinzufügen möchten, können Sie die Zugriffskontrolle einfach verwalten. Um zum Beispiel einen Benutzer namens "JohnDoe" zur Gruppe "Managers" hinzuzufügen, können Sie den folgenden Befehl verwenden:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Mit diesem Cmdlet können Sie Mitglieder aus einer AD-Gruppe entfernen. Durch Angabe der AD-Gruppe und der Benutzerkonten oder Gruppen, die Sie entfernen möchten, können Sie Gruppenmitgliedschaften effektiv verwalten. Um zum Beispiel einen Benutzer namens "JaneSmith" aus der Gruppe "Developers" zu entfernen, können Sie den folgenden Befehl verwenden:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Mit diesem Cmdlet können Sie das Kennwort für einen AD-Benutzer festlegen. Durch Angabe des Benutzerkontos und eines neuen Kennworts können Sie Kennwortrichtlinien durchsetzen und eine sichere Benutzerauthentifizierung gewährleisten. Hier ist ein Beispiel für das Festlegen eines neuen Kennworts für einen Benutzer namens "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Mit diesen sicherheitsrelevanten Cmdlets können Administratoren den Benutzerzugriff, Gruppenmitgliedschaften und Kennwortrichtlinien innerhalb der Active Directory-Umgebung effektiv verwalten.

## Beispiel für ein Active Directory-Modulscript für PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Schlussfolgerung

Zusammenfassend lässt sich sagen, dass das **Active Directory-Modul für PowerShell** ein leistungsstarkes Tool ist, das eine effiziente und bequeme Verwaltung von Windows Active Directory ermöglicht. Durch die Installation und den Import des Moduls erhalten Sie Zugriff auf einen umfassenden Satz von **Cmdlets**, die verschiedene AD-bezogene Aufgaben vereinfachen.

Mit dem Active Directory-Modul können Sie eine Vielzahl von Operationen durchführen, wie z. B. das Abrufen von Informationen über AD-Objekte, das Erstellen neuer Objekte, das Ändern von Eigenschaften und die Verwaltung der Sicherheit. Mit diesem Modul können Administratoren administrative Aufgaben automatisieren, Arbeitsabläufe rationalisieren und das reibungslose Funktionieren von Active Directory-Umgebungen sicherstellen.

Durch die Nutzung von **PowerShell** und dem **Active Directory-Modul** können Sie Ihre AD-Verwaltungsfähigkeiten erweitern und die Effizienz der AD-Verwaltungsprozesse verbessern. Ganz gleich, ob Sie Systemadministrator, IT-Fachmann oder Active Directory-Manager sind, das Active Directory-Modul stattet Sie mit den erforderlichen Tools für die effektive Verwaltung Ihrer AD-Infrastruktur aus.

Nutzen Sie die Leistungsfähigkeit von **PowerShell** und dem **Active Directory-Modul**, um Ihre AD-Verwaltungsaufgaben zu rationalisieren, die Produktivität zu steigern und eine sichere und gut organisierte Active Directory-Umgebung zu erhalten.

## Referenzen

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
