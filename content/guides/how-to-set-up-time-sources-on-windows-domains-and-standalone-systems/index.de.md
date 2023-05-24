---
title: "Best Practices für die Zeitquellenverwaltung in Windows-Domänen und eigenständigen Maschinen"
draft: false
toc: true
date: 2023-05-23
description: "Erfahren Sie, wie Sie Zeitquellen in Windows-Domänen und eigenständigen Computern effektiv festlegen und verwalten, um eine genaue Zeitsynchronisierung sicherzustellen und potenzielle Probleme zu vermeiden."
tags: ["Zeitquellen", "Windows-Domäne", "eigenständige Maschinen", "Zeitsynchronization", "genaue Zeitmessung", "NTP-Server", "Domänencontroller", "Windows-Zeitdienst", "Authentifizierungsfehler", "Inkonsistenzen in der Protokolldatei", "Replikationsprobleme", "Konfiguration der Zeitquelle", "Zeitquellenmanagement", "Windows-Zeitsynchronisierung", "Best Practices für die Zeitmessung", "Einrichtung der Zeitquelle", "Systemzeit synchronisieren", "Zeitsynchronisierung der Windows-Domäne", "eigenständige Maschinenzeitsynchronisation", "Auswahl der Zeitquelle", "Fehlerbehebung bei Zeitquellen", "Zeitquellenfehler", "Zeitquellenprobleme", "Befehle zur Konfiguration der Zeitquelle", "Anweisungen zur Einrichtung der Zeitquelle", "Herausforderungen bei der Zeitsynchronisation", "Folgen von Zeitverlust", "Verhinderung von Zeitverschiebungen", "Fehlerbehebung bei Zeitsynchronisationsfehlern", "Fehlerbehebung bei der Zeitsynchronisation", "Zeitquellenverwaltung in Windows-Domänen", "Umgang mit Zeitquellen auf eigenständigen Windows-Maschinen", "Vermeidung von Zeitverlusten in Windows-Umgebungen", "Folgen von Zeitsynchronisationsfehlern", "Best Practices für eine genaue Zeitmessung"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Ein Bild, das eine Uhr zeigt, die mit einem Domänencontroller und einem eigenständigen Computer synchronisiert wird. Es symbolisiert die Verwaltung von Zeitquellen und die genaue Zeitsynchronisierung in Windows-Umgebungen."
coverCaption: ""
---

**So legen Sie Zeitquellen in einer Windows-Domäne und auf eigenständigen Windows-Maschinen fest und verwalten sie**

Die Zeitsynchronisierung ist entscheidend für die Aufrechterhaltung genauer Zeitstempel und die Gewährleistung des ordnungsgemäßen Funktionierens von Systemen in einer Windows-Domäne oder eigenständigen Windows-Computern. In diesem Artikel besprechen wir die Best Practices für die Einstellung und Handhabung von Zeitquellen in beiden Szenarien und heben die Bedeutung hervor, dass Domänenmitglieder auf Domänencontroller verweisen. Wir werden auch verschiedene Optionen für Zeitquellen untersuchen und dabei den Schwerpunkt auf die Verwendung externer NTP-Pools oder GPS-basierter Zeitserver für optimale Genauigkeit legen.

______

## Zeitquellen in einer Windows-Domäne festlegen

In einer Windows-Domäne ist eine konsistente Zeitsynchronisierung aller Domänenmitglieder unerlässlich. Die beste Vorgehensweise besteht darin, Domänencontroller als primäre Zeitquelle für Domänenmitglieder zu konfigurieren. Auf diese Weise stellen Sie sicher, dass alle Systeme innerhalb der Domäne über eine synchronisierte Zeit verfügen, was für die Authentifizierung, Protokollierung und verschiedene Domänenvorgänge von entscheidender Bedeutung ist.

### Zeitquellenoptionen für Domänencontroller

Domänencontroller können ihre Zeit aus verschiedenen Quellen beziehen, einschließlich der BIOS-Uhr, VMware Tools (in virtualisierten Umgebungen) oder externen Zeitservern. Die Verwendung der BIOS-Uhr oder von VMware Tools kann zwar praktisch sein, es wird jedoch empfohlen, für eine höhere Genauigkeit eine **Stratum 0- oder 1-Quelle** wie einen externen NTP-Pool oder einen GPS-basierten Zeitserver zu verwenden.

#### Externe NTP-Pools

Externe NTP-Pools sind weltweit verteilte und zuverlässige Quellen zur Zeitsynchronisation. Sie bestehen aus einer großen Anzahl von NTP-Servern, die von Organisationen und Institutionen weltweit verwaltet werden. Indem Sie Domänencontroller für die Synchronisierung mit externen NTP-Pools konfigurieren, können Sie eine genaue Zeitmessung innerhalb der Windows-Domäne sicherstellen.

Gehen Sie folgendermaßen vor, um Domänencontroller für die Verwendung eines externen NTP-Pools einzurichten:

1. Öffnen Sie eine Eingabeaufforderung mit erhöhten Rechten auf dem Domänencontroller.
2. Führen Sie den folgenden Befehl aus:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Dieser Befehl konfiguriert den Domänencontroller für die Synchronisierung mit dem NTP-Pool pool.ntp.org. Passen Sie den Befehl an, um einen anderen NTP-Pool oder bei Bedarf mehrere Quellen zu verwenden.

3. Starten Sie den Windows-Zeitdienst neu, um die Änderungen zu übernehmen:

```shell
net stop w32time && net start w32time
```


#### GPS-basierte Zeitserver

Eine weitere Option für Domänencontroller ist die Verwendung von GPS-basierten Zeitservern. Diese Server sind auf GPS-Signale angewiesen, um hochpräzise Zeitinformationen bereitzustellen. Indem Sie einen lokal gehosteten GPS-basierten Zeitserver einrichten und Domänencontroller für die Synchronisierung damit konfigurieren, können Sie eine präzise Zeitsynchronisierung innerhalb der Windows-Domäne erreichen.

### Domänenmitglieder konfigurieren

Domänenmitglieder wie Clientcomputer und andere Server sollten so konfiguriert werden, dass sie ihre Zeit mit den Domänencontrollern synchronisieren. Dadurch wird sichergestellt, dass alle Systeme in der Domäne synchron bleiben und zeitbezogene Probleme vermieden werden.

Um Domänenmitglieder so zu konfigurieren, dass sie ihre Zeit mit Domänencontrollern synchronisieren, sind normalerweise keine zusätzlichen Schritte erforderlich. Standardmäßig synchronisieren Domänenmitglieder ihre Zeit automatisch mit den Domänencontrollern.

______

## Zeitquellen auf eigenständigen Windows-Rechnern festlegen

Auf eigenständigen Windows-Computern, die nicht Teil einer Domäne sind, kann das Festlegen von Zeitquellen je nach Windows-Version und regionalen Einstellungen variieren. Standalone-Windows-Computer verwenden standardmäßig **time.windows.com** als primäre Zeitquelle. Es ist jedoch zu beachten, dass das Standardverhalten geändert werden kann.

### Ändern der Zeitquelle auf eigenständigen Maschinen

Wenn Sie die Zeitquelle auf einem eigenständigen Windows-Computer ändern möchten, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie eine Eingabeaufforderung mit erhöhten Rechten auf dem Computer.
2. Führen Sie den folgenden Befehl aus, um den NTP-Server zu konfigurieren:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Dieser Befehl legt time.windows.com als Zeitquelle für den eigenständigen Computer fest. Passen Sie den Befehl bei Bedarf an, um eine andere Zeitquelle zu verwenden.

3. Starten Sie den Windows-Zeitdienst neu, damit die Änderungen wirksam werden:

```shell
net stop w32time && net start w32time
```


Durch Ausführen dieser Befehle können Sie einen eigenständigen Windows-Computer so konfigurieren, dass er seine Zeit mit der gewünschten Zeitquelle synchronisiert.

______

## Abschluss

Eine ordnungsgemäße Zeitsynchronisierung ist sowohl für Windows-Domänen als auch für eigenständige Computer von entscheidender Bedeutung. In einer Windows-Domäne ist es wichtig, Domänenmitglieder so zu konfigurieren, dass sie zur Zeitsynchronisierung auf Domänencontroller verweisen. Domänencontroller können ihre Zeit aus verschiedenen Quellen beziehen, wobei für eine höhere Genauigkeit die Verwendung externer NTP-Pools oder GPS-basierter Zeitserver empfohlen wird.

Auf eigenständigen Windows-Computern ist die Standardzeitquelle normalerweise time.windows.com. Sie können die Zeitquelle jedoch mit den bereitgestellten Befehlen ändern.

Indem Sie diese Best Practices befolgen und geeignete Zeitquellen konfigurieren, stellen Sie eine genaue Zeiterfassung, zuverlässige Authentifizierung und konsistente Protokollierung in Ihrer Windows-Umgebung sicher.

______

## Verweise

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)

