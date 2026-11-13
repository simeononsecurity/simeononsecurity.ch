---
title: "Open WebUI v0.12.4: Checkliste für Upgrade und Zugriffskontrolle 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Sichern Sie Open WebUI und aktualisieren Sie auf v0.12.4. Testen Sie anschließend Chatfreigaben, Exportberechtigungen, Ressourcenfreigaben, Konten und Netzwerkzugriff."
genre: ["Selbst gehostete KI", "Cybersicherheit", "Systemadministration"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "Open-WebUI-Upgrade", "Open-WebUI-Sicherheit", "Open-WebUI-Zugriffskontrolle", "selbst gehostete KI", "Docker-Upgrade", "pip-Upgrade", "Open-WebUI-Backup", "Open-WebUI-Berechtigungen", "Open-WebUI-Rollen", "Open-WebUI-Gruppen", "Chat-Exportberechtigung", "geteilte Chats", "archivierte Chats", "Wissensdatenbankzugriff", "Modellzugriff", "Werkzeugberechtigungen", "API-Schlüsselsicherheit", "Administratorkontosicherheit", "Registrierung deaktivieren", "Reverse-Proxy-Authentifizierung", "VPN-Zugriff", "Container-Image-Pinning"]
---

**Open WebUI v0.12.4 enthält Sicherheitskorrekturen, die die Maintainer noch nicht im Einzelnen aufgeführt haben.** Die Versionshinweise empfehlen eine zeitnahe Aktualisierung und kündigen Sicherheitshinweise nach der CVE-Zuweisung an. Die unten genannten Änderungen zu Chatfreigaben und Berechtigungen sind die sichtbaren Einträge der Versionshinweise. Sie bilden keine vollständige Liste der noch nicht offengelegten Sicherheitskorrekturen. [Versionshinweise zu Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Wichtigste Punkte

- **Erstellen Sie zuerst ein Backup.** Bewahren Sie eine wiederherstellbare Kopie des Datenvolumes oder der Datenbank sowie der Uploads auf, bevor Sie die Anwendung ändern.
- **Fixieren Sie das offizielle Release.** Verwenden Sie `ghcr.io/open-webui/open-webui:v0.12.4` für das Standard-Docker-Image oder `open-webui==0.12.4` für pip.
- **Testen Sie Berechtigungen mit echten Benutzerrollen.** Eine ausgeblendete Schaltfläche beweist keine Autorisierungsprüfung auf API-Seite.
- **Halten Sie den Zugriff privat.** Erfordern Sie die Anwendungsauthentifizierung und beschränken Sie den Netzwerkzugriff über ein VPN oder einen authentifizierten Reverse Proxy.

## Vor dem Upgrade

**Voraussetzungen:** Ermitteln Sie die aktuelle Installationsmethode, die Container-Image-Variante, den Speicherort der dauerhaften Daten, die externe Datenbank, den Reverse Proxy und den Authentifizierungsanbieter. Planen Sie ein Wartungsfenster und bewahren Sie die vorhandene Containerkonfiguration oder Service-Definition auf. Planen Sie Zeit für einen Wiederherstellungstest auf einer separaten Instanz ein. Die folgenden Befehle sind vom Anbieter dokumentierte Muster, angepasst an dieses festgelegte Release. Sie stammen nicht aus einem für diesen Leitfaden durchgeführten Live-Upgrade. [Open WebUI aktualisieren](https://docs.openwebui.com/getting-started/updating/)

1. **Erfassen Sie den Speicher.** Beim Standard-Docker-Setup wird `open-webui` unter `/app/backend/data` eingebunden. Notieren Sie Bind-Mounts, externe Datenbank, Objektspeicher und benutzerdefinierte Umgebungsvariablen. Suchen Sie bei pip vor der Änderung der Umgebung das aktive Anwendungsdatenverzeichnis und die Datenbank. Gehen Sie nicht davon aus, dass ein Chat-Export ein vollständiges Backup ist.
2. **Sichern Sie bei gestoppten Schreibvorgängen.** Stoppen Sie die Anwendung oder erstellen Sie einen konsistenten Datenbank-Snapshot. Kopieren Sie anschließend das Volume, alle externen Datenbanken und Uploads auf einen getrennten Speicher. Der Anbieter dokumentiert ein Docker-Volume-Archiv. Passen Sie Volume-Namen und Backup-Pfad an Ihre Bereitstellung an. Prüfen Sie, ob sich das Archiv öffnen lässt, und testen Sie die Wiederherstellung auf einer separaten Instanz, bevor Sie sich darauf verlassen. [Backup und Wiederherstellung](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Lesen Sie Versionshinweise und Migrationsanleitung.** Die v0.12.4-Hinweise führen die ausstehenden Sicherheitskorrekturen nicht auf und nennen keine betroffenen Versionen. Ordnen Sie diesen Korrekturen keine CVE zu und nehmen Sie nicht an, dass jede Version vor v0.12.4 von einem bestimmten Fehler betroffen ist. Die Aktualisierungsanleitung warnt vor Migrationen, die sich nicht rückgängig machen lassen, und vor Replikaten mit gemischten Versionen. Wenn mehrere Worker oder Replikate dieselbe Datenbank verwenden, stoppen Sie sie gemeinsam und befolgen Sie das [Migrationsverfahren für mehrere Replikate](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Für ein Rollback ist möglicherweise das Datenbank-Backup vor dem Upgrade erforderlich.

## Installiertes Paket aktualisieren

**Docker, Anbieterverfahren mit festgelegtem Tag:** Laden Sie nach dem Backup das offizielle Standard-Image herunter und erstellen Sie den Container mit demselben dauerhaften Volume, derselben Konfiguration und demselben `WEBUI_SECRET_KEY` neu. Das Beispiel setzt das standardmäßige benannte Volume und einen lokal gebundenen Proxy-Upstream voraus. Fügen Sie Ihren echten Schlüssel nicht in den Shell-Verlauf ein. Stellen Sie ihn über Ihre vorhandene geschützte Umgebung oder Ihr Geheimnisverwaltungssystem bereit. Übernehmen Sie GPU-, Ollama-, benutzerdefinierte Netzwerk-, Datenbank- und weitere Optionen Ihrer aktuellen Bereitstellung. [Open WebUI aktualisieren](https://docs.openwebui.com/getting-started/updating/) · [Offizielle Image-Tags](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Prüfen Sie `./open-webui.env` vor dem Start:** Die Datei muss bereits vorhanden sein, restriktive Berechtigungen haben und Ihren vorhandenen `WEBUI_SECRET_KEY` sowie die erforderliche Konfiguration enthalten. Die Loopback-Bindung eignet sich für einen Proxy auf demselben Host, nicht für einen Proxy auf einem anderen Rechner. Ändern Sie bei Compose nur das Service-Image auf den festgelegten Tag. Führen Sie dann im vorhandenen Projekt `docker compose pull open-webui` und `docker compose up -d open-webui` aus. Behalten Sie dasselbe Volume und dieselbe Umgebungskonfiguration bei. Dies sind empfohlene Befehle, kein getestetes Upgrade Ihrer Bereitstellung.

**pip, Anbieter-Update mit fester Version:** Stoppen Sie im vorhandenen virtuellen Environment den Dienst, installieren Sie genau diese Paketversion und starten Sie ihn mit demselben Datenverzeichnis und derselben Umgebung neu. Vermeiden Sie ein zweites Python-Environment oder eine neue leere Datenbank. Die allgemeine Update-Anweisung des Anbieters verwendet `pip install -U open-webui`. Die Versionsvorgabe unten fixiert diese Checkliste auf v0.12.4. [Open WebUI aktualisieren](https://docs.openwebui.com/getting-started/updating/) · [Schnellstart](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Prüfen Sie den laufenden Dienst, nicht nur das installierte Artefakt.** Lesen Sie die Startversion in `docker logs open-webui` oder den pip-Serviceprotokollen und vergleichen Sie sie nach der Anmeldung mit der in der Anwendung angezeigten Version. Die Update-Anleitung des Anbieters empfiehlt, die Containerprotokolle zu prüfen und die Anmeldeseite aufzurufen. Zeigt die Oberfläche veraltete Ressourcen, laden Sie den Browser mit einem erzwungenen Refresh neu. Meldet der Start einen Migrationsfehler, lassen Sie den Dienst offline, bis Sie die Ursache untersucht haben. Installieren Sie keinen älteren Binärstand über eine migrierte Datenbank, ohne die Wiederherstellungsanforderungen zu prüfen. [Prüfungen nach dem Update](https://docs.openwebui.com/getting-started/updating/)

## Zugriff nach dem Neustart prüfen

**Vom Anbieter beschriebenes Verhalten:** v0.12.4 blendet den Ordnerexport, den Export archivierter Chats und das Kopieren von Chats für Benutzer ohne **Allow Chat Export** aus. Für Benutzer ohne die jeweilige Freigabeberechtigung werden auch die Zugriffskontrollen für Modelle, Prompts, Tools, Wissen, Skills, Notizen und Ordner ausgeblendet. Betrachter eines geteilten Ordners erhalten keine Live-Chat-Aktualisierungen mehr, nachdem der Besitzer einen Chat archiviert hat. Betrachter eines Freigabelinks erhalten keine Live-Aktualisierungen mehr, nachdem der Besitzer die Freigabe aller Chats beendet hat. Ausgeblendete Steuerelemente sind ein Verhalten der Oberfläche und kein Beleg für eine serverseitige Korrektur einer nicht näher bezeichneten Schwachstelle. [Versionshinweise](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Empfohlene Prüfung durch Betreiber:** Prüfen Sie mit einem Testkonto ohne Export- und Freigabeberechtigungen, ob die genannten Aktionen fehlen. Bestätigen Sie mit einem berechtigten Konto, dass die vorgesehenen Aktionen weiterhin funktionieren. Erstellen Sie einen nicht sensiblen Testchat in einem geteilten Ordner, rufen Sie ihn mit einem anderen Konto auf, archivieren Sie ihn als Besitzer und prüfen Sie, ob neue Aktualisierungen den Betrachter nicht mehr erreichen. Wiederholen Sie den Test mit einem Freigabelink und **Unshare All Chats**. Prüfen Sie gespeicherte Freigaben und alte Links erneut. Gehen Sie nicht davon aus, dass archivierte Inhalte oder frühere Kopien gelöscht wurden.

| Prüfbereich | Zu prüfen |
|---|---|
| **Rollen und Gruppen** | Entfernen Sie veraltete Mitglieder und Administratorzuweisungen. Prüfen Sie die wirksamen Berechtigungen eines neu zugelassenen und eines eingeschränkten Benutzers. |
| **Modelle und Tools** | Prüfen Sie die Zugriffsfreigaben der einzelnen Modelle, angehängte Tools, Rechte zum Erstellen von Tools und Anbieterzugangsdaten. Testen Sie mit einem Nicht-Admin-Konto. |
| **Wissen und Dateien** | Prüfen Sie Mitwirkende der Wissensdatenbank, Ressourcenfreigaben, Anhänge und Freigabeeinstellungen. Testen Sie ein Konto, dem der Zugriff entzogen wurde. |
| **Chats und Exporte** | Prüfen Sie geteilte Ordner, Freigabelinks, archivierte Chats und Zuweisungen von Allow Chat Export. Widerrufen Sie nicht mehr benötigte Links. |

Diese Inventarprüfungen sind **Empfehlungen für Betreiber**, keine neuen Zusicherungen von v0.12.4. Der [Hardening-Leitfaden](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) des Anbieters beschreibt mehrstufige Rollen, Gruppen, Ressourcenfreigaben, Workspace-Berechtigungen, API-Schlüssel und Netzwerkplatzierung.

## Lücken bei Konten und Netzwerk schließen

- **Registrierung, Anbietereinstellung:** Deaktivieren Sie die offene Registrierung, wenn ein Administrator oder Identitätsanbieter Konten bereitstellt. Prüfen Sie `ENABLE_SIGNUP` und dauerhafte Admin-Einstellungen anhand des [Hardening-Leitfadens](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Halten Sie Genehmigungsregeln für neue Konten restriktiv.
- **API-Schlüssel, Prüfung durch Betreiber:** Erfassen Sie ausgegebene Schlüssel, löschen Sie nicht verwendete Schlüssel und beschränken Sie Erstellung sowie Endpunktzugriff auf benötigte Rollen und Routen. Laut Hardening-Leitfaden des Anbieters gelten für einen Schlüssel die Berechtigungen seines Erstellers. Bewahren Sie Schlüssel außerhalb von Artikelbeispielen und Anwendungsprotokollen auf.
- **Administratoren, Prüfung durch Betreiber:** Entfernen Sie aufgegebene Administratorkonten, erzwingen Sie starke Anmeldekontrollen, prüfen Sie die Verfügbarkeit von MFA und untersuchen Sie unerwartete Kontoänderungen. Testen Sie den Wiederherstellungsweg für Konten, bevor Sie einen überflüssigen Admin deaktivieren.
- **Netzwerkgrenze, Anbieterrichtlinie:** Platzieren Sie den Dienst hinter einem VPN, Access-Proxy oder Reverse Proxy mit Authentifizierung und IP-Allowlist. Stellen Sie ihn nicht ohne Authentifizierung öffentlich bereit. Vermeiden Sie `WEBUI_AUTH=False` bei einem erreichbaren Dienst. Ein Reverse Proxy ohne eigene Authentifizierung ersetzt die Anmeldung an der Anwendung nicht. [Open WebUI absichern](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Geltungsbereich:** Diese Checkliste betrifft das offizielle Open-WebUI-Release und die dokumentierten Standardinstallationspfade. Sie prüft keine Forks, abgeleiteten Images oder Drittanbieterpakete. Die v0.12.4-Hinweise melden keine aktive Ausnutzung. Prüfen Sie die [Sicherheitshinweise des Projekts](https://github.com/open-webui/open-webui/security/advisories) auf spätere Offenlegungen und deren eigene betroffene und behobene Versionen. Ordnen Sie v0.12.4 nicht die Korrektur eines früheren Hinweises zu, ohne dessen Versionsbereich zu lesen.

## Quellen und Referenzen

- [Versionshinweise zu Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Sicherheitshinweise zu Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Open WebUI aktualisieren, einschließlich Backup, Rollback und Migrationen](https://docs.openwebui.com/getting-started/updating/)
- [Open-WebUI-Schnellstart und offizielle Image-Tags](https://docs.openwebui.com/getting-started/quick-start/)
- [Open WebUI absichern](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Updates und Migrationen mit mehreren Replikaten](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)
