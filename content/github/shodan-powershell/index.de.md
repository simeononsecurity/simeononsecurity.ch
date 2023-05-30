---
title: "OSINT mit Shodan PowerShell-Modulen automatisieren"
date: 2020-11-14
---

Eine Sammlung von PowerShell-Modulen für die Interaktion mit der Shodan-API

**Anmerkungen:**
- Sie benötigen Ihren Shodan-API-Schlüssel, den Sie in Ihrem [Shodan Account](https://account.shodan.io/)
- Beispiele für die in den Modulen verwendeten APIs finden Sie auf der Website [Shodan Developers Page](https://developer.shodan.io/api)
- Bestimmte Module können Scan- oder Query-Credits verwenden. Query-Credits werden verwendet, wenn Sie Daten über die Website, CLI oder API herunterladen (was diese Skripte tun).
  Da wir die API verwenden, ist es wichtig zu wissen, dass Abfrage-Credits abgezogen werden, wenn:
  1.  ein Suchfilter verwendet wird
  2.  Seite 2 oder mehr angefordert wird
      Das Guthaben wird zu Beginn des Monats erneuert und mit 1 Guthaben können Sie 100 Ergebnisse herunterladen.
      Was die Scan-Credits betrifft, so können Sie mit 1 Scan-Credit 1 IP scannen, und auch sie werden zu Beginn des Monats erneuert.
      Bitte besuchen Sie das Shodan Help Center [HERE](https://help.shodan.io/the-basics/credit-types-explained) für alle Einzelheiten.

## Inhaltsverzeichnis
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Module**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Gibt Informationen über den API-Plan zurück, der zu dem angegebenen API-Schlüssel gehört.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Zeigt die HTTP-Header an, die Ihr Client bei der Verbindung mit einem Webserver sendet.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Ermittelt Ihre aktuelle IP-Adresse, wie sie vom Internet aus gesehen wird.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Ruft alle Subdomains und andere DNS-Einträge für die angegebene Domain ab
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Sucht nach den Hostnamen, die für die angegebene Liste von IP-Adressen definiert wurden.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Sucht nach Exploits, gibt aber nur Informationen über die Gesamtzahl der Treffer in Bezug auf den Suchbegriff und optional den Autor, die Plattform, den Port, die Quelle oder den Typ des Exploits zurück.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Liefert die Gesamtzahl der Ergebnisse von "/shodan/host/search" zurück.
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Shodan mit IP-Adresse durchsuchen.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Suchen Sie in Shodan mit der gleichen Abfragesyntax wie auf der Website und verwenden Sie Facetten, um zusammenfassende Informationen für verschiedene Eigenschaften zu erhalten.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Dieses Modul liefert eine Liste von Suchfiltern, die in der Suchabfrage verwendet werden können.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Dieses Modul liefert eine Liste von Suchfiltern, die in der Suchabfrage verwendet werden können.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Listen Sie alle Ports auf, die Shodan im Internet durchsucht.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Gibt Informationen über das mit diesem API-Schlüssel verknüpfte Shodan-Konto zurück
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Überprüfen des Fortschritts eines zuvor eingereichten Scanauftrags
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Liste aller Protokolle, die bei der Durchführung von On-Demand-Internet-Scans über Shodan verwendet werden können
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Verwenden Sie dieses Modul, um Shodan aufzufordern, ein Netzwerk zu crawlen.

<a name="Download"></a>

## Herunterladen

Sie müssen die Skripte klonen oder auf Ihren Computer herunterladen.

Sie können das Code-Dropdown-Menü auf dieser Repo-Seite verwenden, indem Sie nach oben scrollen, oder einfach den folgenden Link kopieren und einfügen: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Für dieses Beispiel klonen wir den Projektnamen in Git Bash. Nachdem wir auf das Klemmbrett-Symbol geklickt haben (siehe oben), können wir git clone eingeben und mit der rechten Maustaste auf das Git Bash-Fenster klicken, um aus dem Dropdown-Menü die Option paste auszuwählen:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Eine ausführliche Anleitung zum Klonen finden Sie unter [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Sobald Sie die Dateien haben, müssen Sie sie nach C:\Programme\WindowsPowerShell\Modules kopieren. Dies führt zu einem Dialog, der besagt, dass der Zugriff verweigert wird, klicken Sie auf "Weiter", um das Kopieren der Dateien an diesen Ort zu beenden, und fahren Sie dann mit den Installationsanweisungen fort [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Sie können das Code-Dropdown-Menü auf dieser Repo-Seite verwenden, indem Sie nach oben scrollen, oder klicken Sie einfach auf den folgenden Link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Entpacken Sie die Datei main.zip, indem Sie mit der rechten Maustaste auf die Datei klicken und im Dropdown-Menü die Option Hier entpacken wählen.

Sobald Sie die Dateien haben, müssen Sie sie nach C:\Programme\WindowsPowerShell\Modules kopieren. Dabei wird ein Dialog angezeigt, der besagt, dass der Zugriff verweigert wird. Klicken Sie auf "Weiter", um das Kopieren der Dateien an diesen Ort zu beenden, und fahren Sie dann mit den Installationsanweisungen fort [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Installieren

<a name="Installieren"></a>

Um die Module zu installieren, müssen Sie ein PowerShell-Fenster als Administrator ausführen.
Es gibt zwei Möglichkeiten, dies zu tun:

Die erste Möglichkeit besteht darin, mit der rechten Maustaste auf das PowerShell-Symbol auf dem Desktop zu klicken und im Dropdown-Menü Als Administrator ausführen auszuwählen.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Geben Sie p (oder so viele Zeichen, wie PowerShell benötigt, um anzuzeigen) in die Suchleiste ein und klicken Sie auf Als Administrator ausführen.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Sie müssen sich in dem Verzeichnis befinden, in das Sie die Skripte kopiert haben.
Führen Sie den folgenden Befehl aus, um Ihr Arbeitsverzeichnis zu ändern:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Auf Windows-Client-Computern müssen wir die PowerShell-Ausführungsrichtlinie ändern, die standardmäßig auf "Eingeschränkt" eingestellt ist.

Für weitere Informationen lesen Sie bitte dies [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Führen Sie den folgenden Befehl aus, um die Richtlinie auf RemoteSigned zu setzen, und geben Sie y ein, um zu bestätigen, dass Sie die Richtlinie ändern möchten.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Sobald die Ausführungsrichtlinie geändert wurde, können Sie den folgenden Befehl ausführen, um die Module zu importieren.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Jetzt können Sie jedes der Skripte als Modul über die Powershell ausführen.
