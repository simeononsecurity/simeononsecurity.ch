---
title: "Einrichten von Cloudflare-Tunneln: Rationalisieren und sichern Sie Ihren Netzwerkverkehr"
draft: false
toc: true
date: 2023-05-26
description: "Erfahren Sie, wie Sie Cloudflare-Tunnel einrichten, um Ihren Netzwerkverkehr zu rationalisieren und zu schützen und so die Leistung und Sicherheit zu verbessern."
tags: ["Cloudflare-Tunnel", "Netzwerksicherheit", "Leistung der Website", "Proxy-Server", "Web-Verkehr", "Netzwerk-Konfiguration", "Ubuntu-Server", "Cloudflare-Konto", "Authentifizierung", "Erstellung von Tunneln", "Verkehrslenkung", "DNS-Einträge", "Sichere Verbindung", "Website-Hosting", "Proxy-Dienst", "Netzwerkschutz", "Optimierung der Leistung", "Cloudflare-Integration", "Server-Konfiguration", "Verkehrsverschlüsselung", "Verwaltung des Netzverkehrs", "Sicheres Webhosting", "Sicherheit der Website", "Ubuntu-Einrichtung", "Tunnelbau-Technologie", "Cloudflare-Dienste", "Leistung des Netzes", "Web Security", "Server-Sicherheit", "Verkehrsmanagement", "Cloudflare Proxy"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Eine Illustration, die einen Netzwerktunnel zeigt, der einen lokalen Server mit dem Cloudflare-Logo verbindet und den sicheren und optimierten Netzwerkverkehr symbolisiert."
coverCaption: ""
---

**Ein Leitfaden zur Einrichtung von Cloudflare-Tunneln**

## Einleitung
Cloudflare Tunnels bieten eine sichere Möglichkeit, Websites zu hosten, indem sie eine direkte Verbindung zwischen Ihrem lokalen Netzwerk und Cloudflare herstellen. Diese Anleitung führt Sie durch den Prozess der Einrichtung von Cloudflare-Tunneln, um die Sicherheit und Leistung Ihrer Website zu verbessern.

______

## Warum Cloudflare Tunnels?
Cloudflare Tunnels bieten mehrere Vorteile, einschließlich der Reduzierung von Angriffsvektoren und der Vereinfachung von Netzwerkkonfigurationen. Durch die Nutzung von Cloudflare als Proxy können Sie externe Ports sperren und sicherstellen, dass der gesamte Datenverkehr durch das sichere Netzwerk von Cloudflare läuft. Dies bietet eine zusätzliche Schutzebene für Ihre Website.

______

## Voraussetzungen
Bevor Sie Cloudflare Tunnels einrichten, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

1. Ein aktives Cloudflare-Konto.
2. Einen Server, auf dem Ubuntu läuft.

______

## Schritt 1: Installation
Um zu beginnen, müssen Sie das Cloudflare Tunnels-Paket auf Ihrem Ubuntu-Server installieren. Folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal auf Ihrem Ubuntu-Server.
2. Laden Sie die neueste Version des Cloudflare Tunnels-Pakets herunter, indem Sie den folgenden Befehl ausführen:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Schritt 2: Authentifizierung
Als Nächstes müssen Sie Ihr Cloudflare-Konto mit dem Cloudflare Tunnels Service authentifizieren. Folgen Sie diesen Schritten:

1. Führen Sie den folgenden Befehl im Terminal aus:

```shell
cloudflared tunnel login
```

2. Klicken Sie auf die Website, die Sie mit Ihrem Tunnel verwenden möchten, um den Authentifizierungsprozess abzuschließen.

## Schritt 3: Einen Tunnel erstellen

Nun ist es an der Zeit, Ihren Cloudflare-Tunnel zu erstellen. Folgen Sie diesen Schritten:

1. Führen Sie den folgenden Befehl im Terminal aus, um einen Tunnel zu erstellen:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Wählen Sie einen Namen für Ihren Tunnel, der einprägsam und aussagekräftig ist. Beachten Sie, dass der Tunnelname später nicht mehr geändert werden kann.

Nach der Erstellung des Tunnels erhalten Sie wichtige Informationen, darunter die UUID Ihres Tunnels. Notieren Sie sich diese UUID, da sie für die weitere Konfiguration benötigt wird.

4. Um eine Liste aller aktiven Tunnel anzuzeigen, verwenden Sie den Befehl:

```shell
cloudflared tunnel list
```

Hier werden die Namen und UUIDs Ihrer Tunnel angezeigt.

### Schritt 4: Konfiguration des Tunnels

Führen Sie die folgenden Schritte aus, um Ihren Tunnel zu konfigurieren und den Datenverkehr zu routen:

1. Navigieren Sie zum Verzeichnis Cloudflare Tunnels auf Ihrem Server. Der Standardspeicherort ist `/etc/cloudflared`

2. Erstellen Sie in diesem Verzeichnis eine neue Datei mit dem Namen `config.yml` mit einem Texteditor Ihrer Wahl.

3. Füllen Sie die Datei config.yml mit dem folgenden Inhalt:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Stellen Sie sicher, dass Sie die `<your_tunnels_uuid>` mit der UUID Ihres Tunnels, und aktualisieren Sie gegebenenfalls den Pfad zur Anmeldedatei.

## Schritt 5: Verkehr routen

Führen Sie die folgenden Schritte aus, um die internen Dienste festzulegen, die Sie über Ihren Tunnel bereitstellen möchten:

1. `Open the ` Datei wieder.

2. Fügen Sie der Datei die Ingress-Parameter hinzu, um die Dienste zu definieren, die Sie über Cloudflare leiten möchten. Zum Beispiel:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json

ingress:
  - hostname: example.com
    service: http://10.10.10.123:1234
  - hostname: subdomain.example.com
    service: http://10.10.10.123:8888
  - service: http_status:404

```

Ersetzen Sie `<your_tunnels_uuid>` mit der UUID Ihres Tunnels und aktualisieren Sie den Hostnamen und die Dienstdetails entsprechend Ihrer Konfiguration.

3. Speichern Sie die Datei config.yml.


## Schritt 6: DNS-Einträge erstellen

Um DNS-Einträge für den Hostnamen und die Dienste Ihres Tunnels zu erstellen, gehen Sie folgendermaßen vor:

1. Öffnen Sie das Terminal.

2. Verwenden Sie den folgenden Befehl, um einen DNS-Eintrag zu erstellen:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```
Ersetzen Sie `<UUID or NAME of tunnel>` mit der UUID oder dem Namen Ihres Tunnels, und `<hostname>` mit dem gewünschten Hostnamen für Ihren Dienst.

3. Um zum Beispiel einen DNS-Eintrag für example.com zu erstellen, führen Sie den Befehl aus:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Bitte beachten Sie, dass sich die Änderungen im DNS-Bereich Ihres Cloudflare-Dashboards widerspiegeln werden.

## Schritt 7: Starten des Tunnels

Um Ihren Cloudflare-Tunnel zu testen und zu starten, folgen Sie diesen Schritten:

1. Öffnen Sie das Terminal.

2. Führen Sie den folgenden Befehl aus, um den Tunnel zu starten:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Ersetzen Sie `<UUID or NAME of tunnel>` mit der UUID oder dem Namen Ihres Tunnels.

3. Cloudflared wird nun Ihren Tunnel einrichten und Informationen zu seinem Status anzeigen. Sobald der Tunnel erfolgreich eingerichtet ist und läuft, können Sie mit dem nächsten Schritt fortfahren.

4. Um zu verhindern, dass der Tunnel geschlossen wird, wenn Sie das Terminal verlassen, müssen Sie Cloudflared als systemd-Dienst starten. Verwenden Sie den folgenden Befehl:

```shell
cloudflared --config /path/to/config.yml service install
```

Ersetzen Sie `/path/to/config.yml` mit dem Pfad zu Ihrem `config.yml` Datei.

## Schlussfolgerung

In dieser Anleitung haben wir die Schritte zur Einrichtung von Cloudflare-Tunneln unter Ubuntu beschrieben. Wenn Sie diese Anweisungen befolgen, können Sie die Sicherheit und Leistung Ihrer Website verbessern, indem Sie das Netzwerk von Cloudflare nutzen. Denken Sie daran, Ihre Tunnel regelmäßig zu überwachen und die Konfiguration nach Bedarf anzupassen.

Wenn Sie auf Probleme stoßen oder weitere Hilfe benötigen, lesen Sie die [official Cloudflare Tunnels documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)


## Referenzen
- [Cloudflare Tunnels Documentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub Repository](https://github.com/cloudflare/cloudflared)
- [tcude - How to Set Up Cloudflare Tunnels on Ubuntu](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)