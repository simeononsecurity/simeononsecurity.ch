---
title: "WMI-Filterung verstehen"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Erfahren Sie, wie WMI-Filterung die Zielauswahl für Gruppenrichtlinienobjekte (GPOs) verbessert. Mit praktischen Beispielen und bewährten Vorgehensweisen."
genre: ["Windows-Verwaltung", "Gruppenrichtlinien", "Systemadministration", "Netzwerkverwaltung", "IT-Infrastruktur", "Richtlinienverwaltung", "IT-Governance", "IT-Automatisierung", "Active Directory", "Sicherheitskonformität"]
tags: ["WMI-Filterung", "GPO", "Gruppenrichtlinienobjekte", "WMI-Filter", "Richtlinienzielauswahl", "WMI-Abfragen", "Windows Management Instrumentation", "GPO-Steuerung", "Gruppenrichtlinien-Verwaltungskonsole", "WMI-Abfragesprache", "Richtlinienanwendung", "WQL", "Richtlinien abstimmen", "Richtlinienverwaltung", "Systemressourcen", "Beispiele zur Richtlinienzielauswahl", "Systemadministration", "Netzwerkverwaltung", "Verwaltung der IT-Infrastruktur", "IT-Automatisierung", "Active-Directory-Verwaltung", "Sicherheitskonformität", "Techniken zur Richtliniensteuerung", "bewährte Vorgehensweisen zur Richtlinienverwaltung", "Richtlinienfilterung", "GPO-Steuerungsstrategien", "GPO-Sicherheit", "Vorteile der WMI-Filterung", "Implementierung der WMI-Filterung", "bewährte Vorgehensweisen für WMI-Filter"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Illustration einer Lupe, die ein Filtersymbol hervorhebt und die gezielte Anwendung von GPOs per WMI-Filterung darstellt."
coverCaption: "Mit WMI-Filterung GPOs effizient auf die passenden Ziele anwenden!"
---

## Einleitung

In Gruppenrichtlinienobjekten (GPOs) steuert die [**WMI-Filterung**](https://simeononsecurity.com/github/wmi-filters/), auf welche Computer oder Benutzer Richtlinien angewendet werden. Maßgeblich sind die Ergebnisse von WMI-Abfragen (Windows Management Instrumentation). Administratoren können damit die Richtlinienzielauswahl verfeinern und Richtlinien nur auf die vorgesehenen Ziele anwenden. Dieser Artikel erklärt die WMI-Filterung, ihre Funktionsweise in GPOs, das Erstellen von [WMI-Filtern](https://simeononsecurity.com/github/wmi-filters/) und praktische Beispiele.

## [Was ist WMI-Filterung?](https://simeononsecurity.com/github/wmi-filters/)

Die [**WMI-Filterung**](https://simeononsecurity.com/github/wmi-filters/) wendet Filter auf GPOs an, die sich nach den Ergebnissen von WMI-Abfragen richten. WMI ist eine in Windows integrierte Verwaltungsinfrastruktur. Administratoren können damit Verwaltungsdaten abrufen und programmgesteuert mit Systemressourcen interagieren. Über WMI-Filter lassen sich GPOs dynamisch anhand bestimmter Abfragekriterien auf Zielsysteme beschränken.

WMI-Filter verwenden die WMI Query Language (WQL), eine Teilmenge von SQL (Structured Query Language). Sie basieren üblicherweise auf Eigenschaften und Werten in einem WMI-Namespace. Administratoren kombinieren Bedingungen, logische Operatoren und Namespaces, um WMI-Abfragen für bestimmte Computer oder Benutzer zu erstellen.

## Wie funktioniert WMI-Filterung in GPOs?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Flussdiagramm eines WMI-Filters an einem Gruppenrichtlinienobjekt, der eine WQL-Abfrage als True oder False auswertet und so die Anwendung der GPO auf einen Zielcomputer bestimmt" >}}

In Gruppenrichtlinien ermöglicht die **WMI-Filterung**, GPOs abhängig von der Auswertung von **WMI-Abfragen** gezielt anzuwenden. Wird einer GPO ein **WMI-Filter** zugeordnet, entscheidet dessen Ergebnis **True** oder **False** darüber, ob die GPO angewendet wird.

WMI-Filter basieren auf der **WMI Query Language (WQL)**, einer Teilmenge von SQL (Structured Query Language). Mit WQL lassen sich komplexe Abfragen zu **Eigenschaften** und **Werten** in einem **WMI-Namespace** erstellen. So können bestimmte Computer oder Benutzer gezielt ausgewählt werden.

Ein Unternehmen möchte beispielsweise eine GPO nur auf Computer mit Windows 10 anwenden. Dazu kann ein WMI-Filter die Eigenschaft **OperatingSystem** der Klasse **Win32_OperatingSystem** prüfen. Die WMI-Abfrage könnte so aussehen:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

Die Abfrage prüft, ob die Betriebssystemversion mit „10.“ beginnt, was Windows 10 kennzeichnet. Ergibt die Abfrage **True**, wird die GPO auf den Zielcomputer angewendet. Andernfalls wird sie nicht angewendet.

WMI-Filter unterstützen auch Bedingungen und logische Operatoren wie **AND**, **OR** und **NOT**. Administratoren kombinieren mehrere Eigenschaften und Werte, um die Anwendung von GPOs genauer zu steuern.

Außerdem bieten verschiedene **WMI-Namespaces** Zugriff auf bestimmte Gruppen von WMI-Klassen und -Eigenschaften. So lassen sich GPOs etwa nach Hardwarekonfiguration, installierter Software, Netzwerkeinstellungen und weiteren Kriterien ausrichten.

Weitere Informationen zum Erstellen von WMI-Filtern und -Abfragen bietet die Microsoft-Dokumentation zur [WMI-Filterung für Gruppenrichtlinien](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

Mit WMI-Filterung können Administratoren GPOs anhand dynamischer Bedingungen auf bestimmte Computer oder Benutzer abstimmen und ihre IT-Umgebung gezielter verwalten.

## WMI-Filter für GPOs erstellen

So erstellen Sie einen WMI-Filter für eine GPO:

1. Öffnen Sie auf einem in die Domäne eingebundenen Windows-Computer die **Gruppenrichtlinien-Verwaltungskonsole** (GPMC).

2. Erweitern Sie die Domäne und öffnen Sie den Knoten **WMI-Filter**.

3. Klicken Sie mit der rechten Maustaste auf **WMI-Filter** und wählen Sie **Neu**.

4. Geben Sie dem Filter einen aussagekräftigen Namen und tragen Sie die WMI-Abfrage im Feld **Abfrage** ein. Verwenden Sie die WQL-Syntax.

5. Klicken Sie auf **OK**, um den WMI-Filter zu speichern.

Nach dem Erstellen lässt sich der Filter einer oder mehreren GPOs zuordnen. Gehen Sie dazu wie folgt vor:

1. Klicken Sie mit der rechten Maustaste auf die gewünschte GPO und wählen Sie **Eigenschaften**.

2. Öffnen Sie im Eigenschaftenfenster der GPO die Registerkarte **WMI-Filterung**.

3. Wählen Sie den gewünschten WMI-Filter aus der Liste aus.

4. Klicken Sie auf **OK**, um die Änderungen zu speichern.

Durch die Zuordnung von WMI-Filtern zu GPOs lässt sich die Richtlinienanwendung anhand der Ergebnisse von WMI-Abfragen genau steuern.

## Wie viele WMI-Filter lassen sich für eine GPO konfigurieren?

Administratoren können für eine GPO **mehrere WMI-Filter** konfigurieren, um die Zielauswahl präzise zu steuern. Eine feste Obergrenze für Filter pro GPO ist nicht vorgegeben. Dadurch sind auch komplexe Kombinationen möglich.

Beachten Sie jedoch die Auswirkungen auf die Verarbeitungszeit. Je mehr Filter ausgewertet werden, desto länger kann die Verarbeitung und Anwendung von GPOs dauern. Für eine effiziente Richtlinienanwendung sollte die Zahl der Filter daher angemessen bleiben.

Ein Unternehmen möchte etwa eine GPO nur auf Computer anwenden, auf denen Windows 10 und eine bestimmte Software installiert sind. Dafür erstellt es zwei getrennte WMI-Filter: einen für das **Betriebssystem** und einen für die **Softwareinstallation**. Zusammen zielen sie auf die gewünschten Computer.

Die Zahl der Filter sollte sowohl die konkreten Zielanforderungen erfüllen als auch die Verarbeitungszeit berücksichtigen. Administratoren sollten vorab die Komplexität der Umgebung, die Anzahl der Computer oder Benutzer sowie die möglichen Leistungsauswirkungen bewerten.

Mehrere WMI-Filter bieten Flexibilität bei der GPO-Zielauswahl. Eine angemessene Anzahl unterstützt zugleich eine effiziente Verarbeitung und Verwaltung der IT-Umgebung.

## Praktische Beispiele für WMI-Filterung in GPOs

WMI-Filterung ermöglicht die gezielte Anwendung von GPOs. Hier sind einige Beispiele:

1. **Bestimmte Betriebssysteme auswählen**: Soll eine GPO ausschließlich für **Windows 10** gelten, erstellen Sie einen Filter, der die Betriebssystemversion prüft, etwa mit `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Damit richten Sie die GPO auf Windows-10-Computer aus.

2. **Unterschiedliche Richtlinien für Desktop-PCs und Laptops**: Wenn die Richtlinien je nach Gerätetyp variieren, verwenden Sie zwei WMI-Filter. Ein Filter kann Desktop-PCs anhand von Hardwareattributen erkennen, etwa mit `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, während der andere Laptops identifiziert. So erhält jeder Gerätetyp passende Richtlinien.

3. **Richtlinien nach verfügbarem Speicherplatz auswählen**: Um ressourcenintensive Richtlinien nicht auf Computern mit wenig Speicherplatz anzuwenden, prüfen Sie den freien Speicherplatz mit einem WMI-Filter. Eine Abfrage wie `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` schließt Computer mit weniger als 10 GB freiem Speicherplatz aus.

Diese Beispiele zeigen die Flexibilität der **WMI-Filterung** in GPOs. Administratoren können Richtlinien anhand bestimmter Kriterien gezielt anwenden.

## Fazit

WMI-Filterung ist eine nützliche Funktion von Gruppenrichtlinienobjekten. Administratoren können Richtlinien abhängig von den Ergebnissen von WMI-Abfragen selektiv anwenden. WMI-Filter richten die Richtlinien genau auf bestimmte Computer oder Benutzer aus und ermöglichen eine effizientere, kontrollierte Verwaltung. Dieser Artikel hat die WMI-Filterung, ihre Funktionsweise in GPOs, das Erstellen von Filtern und praktische Beispiele erläutert.

Mit WMI-Filterung in der GPO-Verwaltung erhöhen Sie die Präzision der Richtlinienanwendung und stellen sicher, dass Richtlinien nur für die vorgesehenen Ziele gelten.

## Referenzen

- [Microsoft Docs: WMI-Filter für die GPO erstellen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Gruppenrichtlinien](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Gruppenrichtlinien-Verwaltungskonsole](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))
