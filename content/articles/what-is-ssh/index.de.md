---
title: "Die Macht von SSH: Sicherer Fernzugriff und Verwaltung leicht gemacht"
date: 2023-06-14
toc: true
draft: false
description: "Entdecken Sie die Vorteile von SSH, lernen Sie, wie man SSH-Schlüssel erzeugt, sich mit entfernten Servern verbindet, Dateien sicher überträgt und SSH-Konfigurationen anpasst."
tags: ["SSH", "Sichere Shell", "Fernzugriff", "Fernverwaltung", "Verschlüsselung", "Authentifizierung", "Datenintegrität", "Tragbarkeit", "Dateiübertragung", "SCP", "SSH-Schlüssel", "SSH-Konfiguration", "Netzwerkprotokoll", "Remote-Befehlsausführung", "OpenSSH", "Zwei-Faktor-Authentifizierung", "Public-Key-Kryptographie", "IP-Adresse", "Domain-Name", "Terminal", "Eingabeaufforderung", "Sicherheit", "Systembetreuer", "Entwickler", "Vielseitigkeit", "Authentifizierungsverfahren", "Hash-Funktionen", "Tunnelbau", "kundenspezifische Optionen"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.png"
coverAlt: "Eine Karikatur einer Person, die sich mit Hilfe von SSH sicher mit einem Server verbindet."
coverCaption: ""
---

**Was ist SSH und wie benutzt man es?

SSH (Secure Shell) ist ein Netzwerkprotokoll, das eine sichere und verschlüsselte Methode für den Zugriff auf entfernte Computer und Server bietet. Es ermöglicht Benutzern, über ein ungesichertes Netzwerk, wie z. B. das Internet, eine sichere Verbindung zu entfernten Systemen herzustellen und diese zu verwalten. Dieser Artikel gibt einen Überblick über SSH, seine Vorteile und seine effektive Nutzung.

{{< youtube id="Atbl7D_yPug" >}}

## Vorteile von SSH

Die Verwendung von SSH für den Fernzugriff bietet mehrere Vorteile, darunter:

1. **Sicherheit**: SSH verwendet starke Verschlüsselungsalgorithmen, um die Kommunikation zwischen dem Client und dem Server zu sichern. Dadurch wird sichergestellt, dass die über das Netzwerk übertragenen Daten nicht von böswilligen Organisationen abgefangen oder manipuliert werden können.

2. **Authentifizierung**: SSH verwendet verschiedene Authentifizierungsmethoden wie Passwörter, Public-Key-Kryptographie und Zwei-Faktor-Authentifizierung, um die Identität von Benutzern zu überprüfen, die sich mit entfernten Systemen verbinden. Dies trägt dazu bei, unbefugten Zugriff zu verhindern.

3. **Datenintegrität**: SSH gewährleistet die Integrität der zwischen dem Client und dem Server übertragenen Daten. Es verwendet kryptografische Hash-Funktionen, um Änderungen oder Manipulationen während der Übertragung zu erkennen.

4. **Portabilität**: SSH wird von einer Vielzahl von Betriebssystemen und Geräten unterstützt, was es zu einer vielseitigen Wahl für den Fernzugriff über verschiedene Plattformen macht.

5. **Flexibilität**: SSH kann für verschiedene Zwecke verwendet werden, einschließlich der Ausführung von Remote-Befehlen, der Dateiübertragung und der Tunnelung anderer Protokolle wie FTP und VNC.

## Wie man SSH benutzt

### SSH-Schlüssel generieren

Bevor Sie SSH verwenden können, müssen Sie ein SSH-Schlüsselpaar erzeugen. Das Schlüsselpaar besteht aus einem öffentlichen Schlüssel und einem privaten Schlüssel. Der öffentliche Schlüssel befindet sich auf dem Remote-Server, während der private Schlüssel sicher auf Ihrem lokalen Rechner aufbewahrt wird. Gehen Sie folgendermaßen vor, um ein SSH-Schlüsselpaar zu erzeugen:

1. Installieren Sie **OpenSSH** auf Ihrem lokalen Rechner, falls es nicht bereits installiert ist. Die Installationsanweisungen finden Sie in der offiziellen Dokumentation Ihres Betriebssystems.

2. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und führen Sie den folgenden Befehl aus, um das Schlüsselpaar zu erzeugen:

```shell
ssh-keygen -t rsa -b 4096
```

3. Sie werden aufgefordert, einen Dateinamen für das Schlüsselpaar und eine optionale Passphrase einzugeben. Drücken Sie die Eingabetaste, um den Standarddateinamen zu akzeptieren, und lassen Sie die Passphrase leer, wenn Sie keine verwenden möchten.

4. Das Schlüsselpaar wird erzeugt, und der öffentliche Schlüssel wird in einer Datei mit einem `.pub` Erweiterung. Der private Schlüssel wird in einer Datei ohne Erweiterung gespeichert.

### Verbindung zu einem entfernten Server herstellen

Gehen Sie folgendermaßen vor, um eine Verbindung zu einem entfernten Server über SSH herzustellen:

1. Ermitteln Sie die **IP-Adresse** oder den Domänennamen des Remote-Servers, mit dem Sie sich verbinden möchten.

2. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und verwenden Sie den folgenden Befehl, um eine SSH-Verbindung zu initiieren:

```shell
ssh username@remote_server_ip
```

Ersetzen Sie `username` mit Ihrem Benutzernamen auf dem entfernten Server und `remote_server_ip` mit der tatsächlichen IP-Adresse oder dem Domänennamen des Servers.

3. Wenn Sie sich zum ersten Mal mit dem Server verbinden, wird möglicherweise eine Warnung bezüglich der Authentizität des Hosts angezeigt. Überprüfen Sie den Fingerabdruck des Servers anhand einer vertrauenswürdigen Quelle, bevor Sie fortfahren.

4. Wenn Sie dazu aufgefordert werden, geben Sie Ihr Passwort ein oder geben Sie den Pfad zu Ihrem privaten Schlüssel an, wenn Sie die schlüsselbasierte Authentifizierung verwenden. Wenn die Authentifizierung erfolgreich war, werden Sie bei dem entfernten Server angemeldet.

### Dateiübertragung mit SSH

SSH kann auch für die sichere Dateiübertragung zwischen Ihrem lokalen Rechner und einem Remote-Server verwendet werden. Das gängigste Tool für die SSH-Dateiübertragung ist **SCP** (Secure Copy). Folgen Sie diesen Schritten, um Dateien mit SCP zu übertragen:

1. Öffnen Sie ein Terminal oder eine Eingabeaufforderung auf Ihrem lokalen Rechner.

2. Verwenden Sie den folgenden Befehl, um eine Datei von Ihrem lokalen Rechner auf den Remote-Server zu kopieren:

```shell
scp /path/to/local/file username@remote_server_ip:/path/to/remote/location
```


Ersetzen Sie `/path/to/local/file` durch den tatsächlichen Pfad und Dateinamen der Datei auf Ihrem lokalen Rechner. Ersetzen Sie in ähnlicher Weise `username@remote_server_ip:/path/to/remote/location` mit dem entsprechenden Benutzernamen, der Server-IP oder -Domäne und dem Speicherort der Remote-Datei.

3. Wenn Sie sich zum ersten Mal mit dem Server verbinden, wird möglicherweise eine Warnung über die Authentizität des Hosts angezeigt. Überprüfen Sie den Fingerabdruck des Servers, bevor Sie fortfahren.

4. Geben Sie Ihr Passwort ein oder geben Sie den Pfad zu Ihrem privaten Schlüssel an, wenn Sie dazu aufgefordert werden. Die Datei wird sicher auf den Remote-Server kopiert.

### SSH-Konfiguration

Mit Hilfe von SSH-Konfigurationsdateien können Sie das Verhalten Ihres SSH-Clients anpassen und feinabstimmen. Die Hauptkonfigurationsdatei befindet sich normalerweise unter `/etc/ssh/sshd_config` auf der Server-Seite und `~/.ssh/config` auf der Client-Seite. Durch die Bearbeitung dieser Dateien können Sie benutzerdefinierte Optionen wie Standardbenutzernamen, Portnummern und Verbindungseinstellungen festlegen.

## Fazit

SSH ist ein leistungsstarkes und sicheres Protokoll für den Fernzugriff und die Verwaltung von Servern und Computern. Seine starke Verschlüsselung, seine Authentifizierungsmechanismen und seine Vielseitigkeit machen es zu einem unverzichtbaren Werkzeug für Systemadministratoren, Entwickler und Einzelpersonen, die einen sicheren Fernzugriff benötigen. Wenn Sie die in diesem Artikel beschriebenen Schritte befolgen, können Sie SSH effektiv einsetzen und die Vorteile seiner Funktionen nutzen.

______

## Referenzen

- [SSH on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [SCP Documentation](https://man.openbsd.org/scp)
- [SSH Configuration File Documentation](https://man.openbsd.org/sshd_config)
