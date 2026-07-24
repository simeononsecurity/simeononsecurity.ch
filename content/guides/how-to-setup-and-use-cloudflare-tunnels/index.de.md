---
title: "Cloudflare Tunnels einrichten: Netzwerktraffic vereinfachen und absichern"
draft: false
toc: true
date: 2023-05-26
lastmod: 2026-05-24
description: "Erfahren Sie, wie Sie Cloudflare Tunnels einrichten, um Ihren Netzwerktraffic zu vereinfachen und zu schützen – für mehr Leistung und Sicherheit."
tags: ["Cloudflare Tunnels", "Netzwerksicherheit", "Website-Performance", "Proxy-Server", "Webtraffic", "Netzwerkkonfiguration", "Ubuntu Server", "Cloudflare-Konto", "Authentifizierung", "Tunnel erstellen", "Traffic-Routing", "DNS-Einträge", "sichere Verbindung", "Website-Hosting", "Proxy-Dienst", "Netzwerkschutz", "Performance-Optimierung", "Cloudflare-Integration", "Serverkonfiguration", "Traffic-Verschlüsselung", "cloudflared", "Tunnel-Technologie", "Websicherheit", "Ubuntu Setup"]
cover: "/img/cover/An_illustration_showing_a_network_tunnel_connecting_a_local.png"
coverAlt: "Eine Illustration, die einen Netzwerktunnel zeigt, der einen lokalen Server mit dem Cloudflare-Logo verbindet und den sicheren sowie vereinfachten Netzwerktraffic symbolisiert."
coverCaption: ""
---

**Anleitung zur Einrichtung von Cloudflare Tunnels**

## Einführung

Cloudflare Tunnels bieten eine sichere Möglichkeit, Websites zu hosten, indem eine direkte Verbindung zwischen Ihrem lokalen Netzwerk und Cloudflare hergestellt wird. Diese Anleitung führt Sie durch den Prozess der Einrichtung von Cloudflare Tunnels, um die Sicherheit und Leistung Ihrer Website zu verbessern.

______

## Warum Cloudflare Tunnels?

Cloudflare Tunnels bieten mehrere Vorteile, darunter die Reduzierung von Angriffsvektoren und die Vereinfachung von Netzwerkkonfigurationen. Durch die Nutzung von Cloudflare als Proxy können Sie externe Ports schließen und sicherstellen, dass der gesamte Traffic über Cloudflares sicheres Netzwerk läuft. Dies bietet eine zusätzliche Schutzschicht für Ihre Website.

______

## Voraussetzungen

Vor der Einrichtung von Cloudflare Tunnels stellen Sie sicher, dass Sie Folgendes haben:

1. Ein aktives Cloudflare-Konto.
2. Einen Server mit Ubuntu.

______

## Schritt 1: Installation

Zunächst müssen Sie das Cloudflare Tunnels-Paket auf Ihrem Ubuntu-Server installieren. Gehen Sie wie folgt vor:

1. Öffnen Sie das Terminal auf Ihrem Ubuntu-Server.
2. Laden Sie die neueste Version des Cloudflare Tunnels-Pakets herunter:

```shell
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
```

## Schritt 2: Authentifizierung

Als nächstes müssen Sie Ihr Cloudflare-Konto mit dem Cloudflare Tunnels-Dienst authentifizieren:

1. Führen Sie im Terminal folgenden Befehl aus:

```shell
cloudflared tunnel login
```

2. Klicken Sie auf die Website, die Sie mit Ihrem Tunnel verwenden möchten, um den Authentifizierungsprozess abzuschließen.

## Schritt 3: Tunnel erstellen

Jetzt ist es Zeit, Ihren Cloudflare Tunnel zu erstellen:

1. Führen Sie folgenden Befehl aus, um einen Tunnel zu erstellen:

```shell
cloudflared tunnel create name_of_tunnel
```

2. Wählen Sie einen einprägsamen und beschreibenden Namen für Ihren Tunnel. Beachten Sie, dass der Tunnelname später nicht geändert werden kann.

3. Nach dem Erstellen des Tunnels erhalten Sie wichtige Informationen, einschließlich der UUID Ihres Tunnels. Notieren Sie diese UUID, da sie für die weitere Konfiguration benötigt wird.

4. Um eine Liste aller aktiven Tunnel anzuzeigen, verwenden Sie:

```shell
cloudflared tunnel list
```

Dies zeigt Namen und UUIDs Ihrer Tunnel an.

### Schritt 4: Tunnel konfigurieren

Um Ihren Tunnel zu konfigurieren und Traffic zu routen, gehen Sie wie folgt vor:

1. Navigieren Sie zum Cloudflare Tunnels-Verzeichnis auf Ihrem Server. Der Standardpfad ist `/etc/cloudflared`.

2. Erstellen Sie in diesem Verzeichnis eine neue Datei namens `config.yml` mit einem Texteditor Ihrer Wahl.

3. Füllen Sie die config.yml-Datei mit folgendem Inhalt:

```yaml
tunnel: <your_tunnels_uuid>
credentials-file: /path/to/credentials/<UUID>.json
```

Ersetzen Sie `<your_tunnels_uuid>` durch die UUID Ihres Tunnels und aktualisieren Sie den Pfad zur Anmeldedatei falls nötig.

## Schritt 5: Traffic routen

Um die internen Dienste festzulegen, die über Ihren Tunnel bereitgestellt werden sollen:

1. Öffnen Sie die `config.yml`-Datei erneut.

2. Fügen Sie die Ingress-Parameter hinzu, um die Dienste zu definieren, die Sie über Cloudflare routen möchten:

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

Ersetzen Sie `<your_tunnels_uuid>` durch Ihre Tunnel-UUID und aktualisieren Sie Hostname und Dienstdetails entsprechend Ihrer Konfiguration.

3. Speichern Sie die config.yml-Datei.

## Schritt 6: DNS-Einträge erstellen

Um DNS-Einträge für den Hostnamen und die Dienste Ihres Tunnels zu erstellen:

1. Öffnen Sie das Terminal.

2. Verwenden Sie folgenden Befehl, um einen DNS-Eintrag zu erstellen:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> <hostname>
```

Ersetzen Sie `<UUID or NAME of tunnel>` durch die UUID oder den Namen Ihres Tunnels und `<hostname>` durch den gewünschten Hostnamen für Ihren Dienst.

3. Um beispielsweise einen DNS-Eintrag für example.com zu erstellen:

```shell
cloudflared tunnel route dns <UUID or NAME of tunnel> example.com
```

Beachten Sie, dass die Änderungen im DNS-Bereich Ihres Cloudflare-Dashboards angezeigt werden.

## Schritt 7: Tunnel starten

Um Ihren Cloudflare Tunnel zu testen und zu starten:

1. Öffnen Sie das Terminal.

2. Führen Sie folgenden Befehl aus, um den Tunnel zu starten:

```shell
cloudflared tunnel run <UUID or NAME of tunnel>
```

Ersetzen Sie `<UUID or NAME of tunnel>` durch die UUID oder den Namen Ihres Tunnels.

3. Cloudflared richtet nun Ihren Tunnel ein und zeigt Informationen über seinen Status an. Sobald der Tunnel erfolgreich läuft, können Sie mit dem nächsten Schritt fortfahren.

4. Um zu verhindern, dass der Tunnel beim Verlassen des Terminals geschlossen wird, müssen Sie Cloudflared als systemd-Dienst ausführen:

```shell
cloudflared --config /path/to/config.yml service install
```

Ersetzen Sie `/path/to/config.yml` durch den Pfad zu Ihrer `config.yml`-Datei.

## Fazit

In dieser Anleitung haben wir die Schritte zur Einrichtung von Cloudflare Tunnels unter Ubuntu behandelt. Durch Befolgen dieser Anweisungen können Sie die Sicherheit und Leistung Ihrer Website durch Cloudflares Netzwerk verbessern. Überwachen Sie regelmäßig Ihre Tunnel und passen Sie die Konfiguration nach Bedarf an.

Bei Problemen oder für weitere Unterstützung lesen Sie die [offizielle Cloudflare Tunnels-Dokumentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/).

## Referenzen

- [Cloudflare Tunnels-Dokumentation](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/)
- [Cloudflare Tunnels GitHub-Repository](https://github.com/cloudflare/cloudflared)
- [tcude - Cloudflare Tunnels unter Ubuntu einrichten](https://tcude.net/creating-cloudflare-tunnels-on-ubuntu/)
