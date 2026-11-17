---
title: "Ein schreibgeschütztes Active-Directory-Inventar mit PowerShell erstellen"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Erfasse OUs, Benutzer und Computer in Active Directory mit gezielten PowerShell-Abfragen. Exportiere prüfbare CSV-Dateien, ohne Verzeichnisobjekte zu ändern."
genre: ["Active Directory", "PowerShell", "Systemadministration"]
tags: ["Active-Directory-Inventar", "PowerShell-AD-Inventar", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "schreibgeschütztes AD", "AD-Benutzerexport", "AD-Computerexport", "AD-OU-Export", "Export-Csv", "RSAT", "Verzeichnisprüfung", "AD-Berichte", "OU-Inventar", "Windows Server", "PowerShell-Skript", "AD-Modul", "Verzeichnishygiene"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Ein Active-Directory-Baum, aus dem Benutzer-, Computer- und Organisationseinheitendatensätze in drei Prüfdateien fließen."
coverCaption: "Grenze die Abfrage ein und exportiere dann nur die für die Prüfung benötigten Felder."
---
Eine Bereinigung von Active Directory beginnt mit einer verlässlichen Liste der vorhandenen Objekte. Dieses **schreibgeschützte Inventar** erfasst Organisationseinheiten, Benutzer und Computer in einem ausgewählten Bereich. Es exportiert drei CSV-Dateien (comma-separated values) zur Prüfung, ohne Verzeichnisobjekte zu ändern. Schütze die Dateien trotzdem, denn Namen und Gerätedetails geben Einblick in deine Umgebung.

<!--more-->

## Wichtigste Erkenntnisse

- **Bereich festlegen:** Frage zunächst eine Organisationseinheit ab, bevor du die ganze Domäne einbeziehst.
- **Nur lesende Befehle verwenden:** `Get-ADOrganizationalUnit`, `Get-ADUser` und `Get-ADComputer` rufen Objekte ab.
- **Felder auswählen:** Exportiere nur die für die Aufgabe benötigten Eigenschaften.
- **Ausgabe prüfen:** Vergleiche die Anzahl und einige Beispielzeilen, bevor du dich auf einen Bericht verlässt.

## Vor dem Start

Du benötigst einen Windows-Administrationshost mit funktionierendem DNS und Netzwerkzugriff auf einen Domänencontroller, das PowerShell-Modul **ActiveDirectory**, ein Konto mit Leseberechtigung für die ausgewählten Objekte und einen geschützten Ordner für die CSV-Ausgabe. Auf einem Windows-Client stammt das Modul aus den Active-Directory-Tools der Remote Server Administration Tools (RSAT). Die [Anleitung zum Active-Directory-Modul](/articles/active-directory-module-powershell-installation-usage-guide/) erklärt die Installation. Microsoft stellt die [Cmdlet-Referenz](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) des Moduls und die [Installationsoptionen für RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools) bereit. Diese Anleitung verwendet die Windows-PowerShell-Syntax und ändert keine Verzeichnisobjekte.

Die Berechtigungen im Verzeichnis gelten weiterhin. Microsoft erklärt in den [Hinweisen zu privilegierten Konten](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), dass Zugriffssteuerungslisten authentifizierten Benutzern häufig Lesezugriff auf allgemeine Informationen gewähren und sensible Felder sowie Änderungen einschränken. Verwende zuerst ein genehmigtes Konto und eine Test-OU. Erhöhe nicht die Rechte auf Domain Admin, nur damit das Inventar erfolgreich läuft.

> **Warnung:** Die CSV-Dateien enthalten Konto- und Computernamen. Speichere sie an einem genehmigten Ort, beschränke den Zugriff und entferne zusätzliche Kopien nach der Prüfung. Veröffentliche keinen Rohdatenexport und hänge ihn nicht an ein öffentliches Issue an.

## Suchbasis auswählen

Eine **Organisationseinheit (OU)** gruppiert Verzeichnisobjekte. Ihr **distinguished name (DN)** bezeichnet ihre Position im Verzeichnisbaum. Der Parameter `-SearchBase` beschränkt eine Abfrage auf einen ausgewählten DN. Ohne eine bewusst festgelegte Suchbasis kann ein breiter Filter deutlich mehr Objekte zurückgeben, als du prüfen musst.

Lade zuerst das Modul und zeige den aktuellen DN der Domäne an:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft dokumentiert [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) und die Domäneninformationen, die das Cmdlet zurückgibt. Ermittle die zu prüfende OU, bevor du die Suchbasis festlegst:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Kopiere den exakten DN aus dem Ergebnis. Ersetze in den folgenden Beispielen diesen Dokumentationswert durch den DN deiner OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` ist eine Beispieldomäne. Kopiere ihren DN nicht in eine Live-Abfrage. Wenn du bewusst ein Inventar für die ganze Domäne erstellen willst, setze `$SearchBase` auf den Domänen-DN und vermerke den größeren Suchbereich im Bericht. Die [Referenz zu Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) von Microsoft beschreibt `-Filter` und `-SearchBase`.

## OUs, Benutzer und Computer erfassen

Beginne mit den Objektzahlen. So erkennst du schnell eine falsche Suchbasis oder ein unerwartet leeres Ergebnis:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` bedeutet, dass alle passenden Objekte innerhalb der Suchbasis abgerufen werden. Microsoft dokumentiert [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) und [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) als Abrufbefehle. Eine Anzahl von null kann korrekt sein. Prüfe aber den DN, die Berechtigungen und die Zieldomäne, bevor du das Inventar als vollständig ansiehst.

Zeige nun einige Zeilen in der Konsole an. Speichere die ausgewählten Felder, damit Vorschau und späterer CSV-Export dieselben Spalten verwenden:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Fordere die zusätzliche Betriebssystemeigenschaft für Computer nur an, wenn du sie für die Prüfung benötigst:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Mit dem Parameter `-Properties` forderst du Eigenschaften an, die nicht zum Standardsatz des Cmdlets gehören. Die [Referenz zum Computer-Cmdlet](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) von Microsoft beschreibt den Parameter. Behandle Betriebssystemnamen als Verzeichnisdaten, nicht als Beleg für die aktuell installierte Version. Ein Computerobjekt kann veraltet sein oder ein Attribut kann noch nicht aktualisiert worden sein.

## Prüfbare CSV-Dateien exportieren

Wähle einen genehmigten Ausgabeordner mit ausreichend Speicherplatz. Die folgenden Befehle schreiben **lokale CSV-Dateien** und lassen Verzeichnisobjekte unverändert. Führe sie in diesem Ordner aus. `-NoClobber` verhindert das Überschreiben vorhandener Dateien. Verwende für jeden Lauf einen neuen Ordner oder Dateinamen.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Die [Referenz zu Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) von Microsoft erläutert `-NoTypeInformation`, `-Encoding` und `-NoClobber`. Öffne jede CSV-Datei in einem Texteditor oder einer genehmigten Tabellenkalkulation. Prüfe die Kopfzeile, einige Zeilen und die Anzahl der Datensätze anhand der vorherigen Zählung. Ein fehlgeschlagener Befehl oder eine Datei mit null Bytes ist kein vollständiger Bericht.

> **Erwartetes Ergebnis:** Du hast drei CSV-Dateien mit OU-, Benutzer- und Computerdatensätzen für den ausgewählten Bereich. Zeilenanzahl und Beispielwerte stimmen mit dem Verzeichnisbereich überein.

## Prüfen, ohne Objekte zu ändern

Nutze das Inventar, um gezielte Fragen zu beantworten: Welche OU ist für einen Computer zuständig? Welche Benutzerkonten sind deaktiviert? Für welche Gerätenamen fehlt ein Verantwortlicher? Halte die Ergebnisse in einer separaten Prüfnotiz fest. Setze den Wert `Enabled` nicht mit der Frage gleich, ob ein Konto noch benötigt wird. Lösche oder deaktiviere kein Objekt allein aufgrund eines Exports.

Vermerke bei wiederkehrenden Berichten das Abfragedatum, die Domäne, den OU-DN, die ausgewählten Eigenschaften, die ausführende Person und den CSV-Speicherort. Wenn du zwei Exporte vergleichst, vergewissere dich, dass beide denselben Bereich und dieselben Felder verwenden. Andernfalls kann ein Unterschied aus der Abfrage statt aus einer tatsächlichen Verzeichnisänderung stammen.

Dies ist ein **Inventar**, keine Prüfung privilegierter Konten und kein Bericht über Anmeldeaktivitäten. Microsoft weist darauf hin, dass sich Eigenschaften und Berechtigungen in Active Directory je nach Objekt und Umgebung unterscheiden. Prüfe ein Betriebssystemattribut oder einen Anzeigenamen beim Systemverantwortlichen, bevor du darauf basierend handelst. Die [Anleitung zur Active-Directory-Sicherheit](/articles/active-directory-security-best-practices/) behandelt weitergehende Sicherheitskontrollen.

## Fehlerbehebung

- **Modul lässt sich nicht importieren:** Stelle sicher, dass die Active-Directory-Tools aus RSAT oder die Windows-Server-Verwaltungstools auf dem Host installiert sind. Folge der [Anleitung zur Moduleinrichtung](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Abfrage gibt keine Objekte zurück:** Prüfe den exakten DN, die aktuelle Domäne, den OU-Inhalt und die Leseberechtigungen. Teste zuerst eine bekannte kleine OU, bevor du den Bereich erweiterst.
- **Eine Eigenschaft ist leer:** Prüfe, ob das Attribut vorhanden ist und ob dein Konto es lesen darf. Ergänze fehlende Felder nicht durch Vermutungen.
- **Beim Export heißt es, die Datei existiert bereits:** `-NoClobber` hat den früheren Bericht geschützt. Wähle einen neuen Dateinamen oder Ordner und führe den Befehl erneut aus.
- **Die Anzahl weicht von den Erwartungen ab:** Prüfe, ob sich Benutzer oder Computer in einer anderen OU befinden, ob du den Suchbereich geändert hast und ob sich das Verzeichnis während der Abfrage verändert hat.

## Nächste Schritte

Bewahre die Roh-CSV-Dateien für den vereinbarten Prüfzeitraum an einem geschützten Ort auf. Teile nur die Felder, die der Prüfer benötigt. Nachdem die Verantwortlichen die Ergebnisse bestätigt haben, plane Änderungen nach deinem üblichen Genehmigungs- und Rollback-Verfahren. Führe nach genehmigten Änderungen dasselbe Inventar mit demselben Suchbereich erneut aus, um das Ergebnis zu bestätigen.