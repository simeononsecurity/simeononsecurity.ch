---
title: 'Rollback von Home Assistant Core 2026.11 auf 2026.10.4: HTTP-Speicherversion 3 beheben'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Behebe den Fehler zur HTTP-Speicherversion 3, nachdem Home Assistant Core 2026.11 auf Yellow auf 2026.10.4 zurückgesetzt
  wurde. Mit abgesicherten Befehlen und geprüften Ausgaben.
genre:
- Hausautomatisierung
- Fehlerbehebung
tags:
- Home Assistant Yellow
- Home Assistant OS
- Rollback von Core 2026.11
- Core 2026.10.4
- HTTP-Speicherversion 3
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Illustration eines gelben Computerboards, einer unterbrochenen Konfigurationsverbindung und eines wiederhergestellten
  Web-Dashboards
coverCaption: ''
---

Ein fehlgeschlagenes Update von Home Assistant Core 2026.11 setzte mein Yellow CM4 auf 2026.10.4 zurück. Yellow blieb im Netzwerk erreichbar, zeigte aber das Dashboard nicht mehr an. Der Rollback hinterließ eine HTTP-Einstellungsdatei mit Speicherversion 3.1, während Core 2026.10.4 Version 2.2 unterstützt. Ich sicherte die Datei, wandelte eine Kopie mit strengen Prüfungen um, stellte den HTTP-Zugriff wieder her und aktualisierte Core anschließend auf 2026.11.1.

<!--more-->

## Wichtigste Punkte

- **Prüfe den Versionskonflikt.** Vergleiche die Core-Logmeldung mit der installierten Version und der HTTP-Speicherversion.
- **Sichere die Datei.** Bewahre vor der Wiederherstellung eine unveränderte Kopie und eine Sicherung außerhalb des Geräts auf.
- **Prüfe das Ergebnis.** Kontrolliere den Core-Status, den gespeicherten Listener, das Dashboard und die installierte Version.

**Lösung für genau diesen Fall:** [Sichere die HTTP-Datei](#preserve-recovery-options), [erstelle und prüfe einen Kandidaten für Version 2.2](#apply-the-tested-fix-for-version-31), [installiere ihn nach dem Stoppen von Core](#apply-the-tested-fix-for-version-31) und [prüfe das Update-Ergebnis](#verify-the-update-outcome). Die Umwandlung prüft die ursprünglichen Felder und bricht bei Abweichungen ab. Wende sie nicht auf eine ungeprüfte HTTP-Datei an.

## Vor dem Start

Du brauchst physischen Zugriff auf ein Yellow CM4, ein USB-C-Datenkabel, eine funktionierende serielle Konsole und ein brauchbares Backup oder eine gesicherte Konfiguration. Der manuelle Weg erfordert Zugriff auf die Host-Shell und eine sorgfältige JSON-Prüfung. Plane mindestens 30 Minuten für Diagnose und Reparatur ein. Core-Start und Backup-Wiederherstellung dauern bei großen Installationen länger.

## Fehler erkennen

Die entscheidende Fehlermeldung stand im Core-Log:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

Die ältere Core-Version konnte `http` nicht laden. Auch das Frontend und andere von HTTP abhängige Komponenten fielen aus. Eine Router-Lease und eine erreichbare Observer-Seite bewiesen nicht, dass das Dashboard verfügbar war. [Home Assistant Core-Problem Nr. 190583](https://github.com/home-assistant/core/issues/190583) dokumentiert denselben Rollback-Fehler bei mehreren Installationen, darunter Yellow. [Mein Kommentar zum Issue](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) hält die getestete Wiederherstellung auf diesem Yellow und den endgültigen Core-Status fest.

**Ursache des Webausfalls:** Core 2026.11 schrieb `.storage/http` im Format 3.1. Der Rollback stellte Core 2026.10.4 wieder her, aber keine kompatible HTTP-Datei. Core 2026.10.4 lehnt Speicherversion 3 ab. Auch das gespeicherte Profil `intermediate_v6` dieses Yellow passt nicht zum älteren Schema. Warum das erste Update fehlschlug und den Rollback auslöste, ist unbekannt. Am 2026-11-15 war das verknüpfte Issue offen und die Diskussion enthielt keine von Maintainer bestätigte Lösung.

Prüfe die installierte Core-Version und den HTTP-Speicher, bevor du Dateien änderst:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

Die folgende Ausgabe zeigt diesen Fall ohne Zeitstempel und private Angaben:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

Die Wiederherstellungsbefehle vergleichen den gespeicherten Listener von Supervisor mit der HTTP-Datei, ohne einen der beiden Werte auszugeben. Bei einer Abweichung prüfe den tatsächlichen Core-Listener, bevor du Dateien änderst.

| Signal | Bedeutung |
| --- | --- |
| Core unterstützt Speicherversion 2, die Datei meldet Version 3 | Die ältere Version kann die gespeicherten HTTP-Einstellungen nicht laden |
| HTTP-Datei und Supervisor-Liste nennen verschiedene Listener | Prüfe den tatsächlichen Core-Listener, bevor du die Ursache festlegst |
| Die Startseite antwortet, Core steht aber noch auf STARTING | Eine Antwort des Frontends beweist keinen abgeschlossenen Start |

## Wiederherstellungsoptionen sichern {#preserve-recovery-options}

Bewahre vor einem weiteren Update ein brauchbares Backup außerhalb von Yellow auf. [Die Backup-Anleitung von Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) beschreibt Cloud- und externe Speicherorte. Für ein verschlüsseltes Backup brauchst du den zugehörigen Wiederherstellungsschlüssel. Lösche die NVMe-Datendisk nicht, während du diesen Speicherkonflikt untersuchst.

Kopiere die HTTP-Datei, bevor du sie bearbeitest:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Brich ab, wenn der Befehl fehlschlägt. Eine vorhandene Wiederherstellungskopie mit demselben Namen bleibt unverändert. Wähle einen neuen Namen und wiederhole die Prüfung, bevor du fortfährst.

Wenn das Dashboard nicht erreichbar ist, nutze die serielle Konsole des Yellow. [Die Nabu-Casa-Anleitung für Linux und macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) zeigt den USB-C-Anschluss und die Position des JP1-UART. Folge den CM4-Anweisungen für deine Hardware.

## Die getestete Korrektur für Speicherformat 3.1 anwenden {#apply-the-tested-fix-for-version-31}

Am besten verwendest du eine kompatible HTTP-Datei von vor dem Update. Stelle das Backup über den dokumentierten Home-Assistant-Prozess wieder her, wenn eine vollständige Wiederherstellung passt. Wenn du eine einzelne Datei extrahierst, prüfe deren Speicherversion und gespeicherten Listener, bevor du die aktive Datei ersetzt. Die folgenden Befehle sind die direkte Korrektur, die ich auf diesem Yellow getestet habe, als keine kompatible HTTP-Datei verfügbar war.

Der [ursprüngliche Workaround im Issue](https://github.com/home-assistant/core/issues/190583) verschiebt `.storage/http` und lässt die ältere Core-Version eine neue Datei erstellen. Ein späterer [Bericht zu Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) zeigt einen anderen Listener in der neu erstellten Datei. Prüfe die neue Datei und `ha core info`, bevor du annimmst, dass die Weboberfläche wieder funktioniert.

Meine Installation hatte keinen YAML-Block `http:`, keine ausstehende HTTP-Konfiguration und kein TLS-Zertifikat oder -Schlüssel in den stabilen Einstellungen. Das gespeicherte Profil war `intermediate_v6`. In diesem eng begrenzten Fall erstellte ich einen separaten Kandidaten der Version 2.2 und behielt den vorhandenen Listener bei:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Alle obigen Befehle müssen erfolgreich sein, bevor du die aktive Datei ersetzt. Wenn `jq` fehlschlägt, prüfe die Kandidatendatei, bevor du sie löschst und es erneut versuchst. [Der HTTP-Quellcode von Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) definiert Speicherversion 2.2 und akzeptiert das Profil `intermediate`. [Der Quellcode von Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) verwendet Version 3.1 und versionierte Profilnamen. Vor der Installation prüfte ich den Kandidaten außerdem mit `HTTP_STORAGE_SCHEMA` der installierten älteren Core-Version.

Führe die Schemaprüfung der installierten älteren Core-Version aus, solange der Container noch läuft:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

Brich ab, wenn das Schema den Kandidaten ablehnt. Dieser Schritt prüft nicht jede Integration oder jede ungetestete Form des HTTP-Speichers.

Die Schemaprüfung gab für diesen Kandidaten `Schema accepted` aus. Jedes andere Ergebnis beendet diesen Wiederherstellungspfad.

Diese manuelle Umwandlung wurde mit den genannten Feldern getestet. Eine Datei mit TLS-Einstellungen, vertrauenswürdigen Proxies oder einer ausstehenden Konfiguration braucht eine eigene Prüfung. Wenn du nur die oberste Versionsnummer änderst, bleibt ein Profil übrig, das die ältere Core-Version nicht akzeptiert.

Supervisor hatte einen aktiven Core-Auftrag und lehnte `ha core stop` in meinem Fall ab. Ich stoppte den Core-Container über die Hostkonsole, installierte den geprüften Kandidaten und startete ihn:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Wenn nach dem Stoppen ein Befehl fehlschlägt, prüfe die aktive HTTP-Datei, bevor du `docker start homeassistant` ausführst. Eine geänderte Datei braucht einen neuen Kandidaten auf Basis des aktuellen Inhalts. Nach diesem Schritt antwortete die HTTP-Seite wieder. Eine HTTP-Antwort allein bewies nicht, dass Core vollständig gestartet war. Deshalb prüfte ich den Supervisor-Status, bevor ich das System als wiederhergestellt betrachtete.

Auf diesem Yellow gab `docker inspect -f '{{.State.Status}}' homeassistant` anschließend `running` aus. Prüfe `ha core info` und das Dashboard, bevor du ein weiteres Update startest.

## Ergebnis der Aktualisierung prüfen {#verify-the-update-outcome}

Nach der Wiederherstellung des HTTP-Zugriffs aktualisierte ich Core auf 2026.11.1. So forderst du diese Version an:

```bash
ha core update --version 2026.11.1
```

Nach einem langen Start meldete der Befehl einen Fehler. Supervisor protokollierte Core anschließend als RUNNING und meldete `Successfully started Home Assistant 2026.11.1`. Eine Statusabfrage zeigte, dass die installierte Version aktuell war, die HTTP-Datei wieder auf Version 3.1 migriert worden war und der Container während der Beobachtung nicht neu gestartet hatte. Das authentifizierte Dashboard lud. **Prüfe das Ergebnis auch dann, wenn der Update-Befehl einen Fehler meldet.**

Prüfe nach einem langen Update auf deinem System die Version, den Supervisor-Zustand und den Containerstatus:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

Der erste und der dritte Befehl lieferten in diesem Fall folgende bereinigte Ergebnisse:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Öffne danach das Dashboard über deine übliche lokale Adresse und prüfe, ob aktuelle Zustände geladen werden. Bewahre die gespeicherte HTTP-Datei auf, bis ein weiteres Backup abgeschlossen und der normale Betrieb bestätigt ist.

Die Belege von meinem Yellow klärten die Ursache des ersten Update-Fehlers nicht. Auch die spätere Fehlermeldung des Auftrags nannte keine Ursache. Eine installierte Version und ein funktionierendes Dashboard belegen den resultierenden Zustand besser als die CLI-Meldung allein, erklären aber nicht, warum Supervisor den Auftrag als fehlgeschlagen markierte.

## Nächste Schritte

Wenn der HTTP-Speicherfehler bleibt, prüfe die gesicherte Datei und stelle ein kompatibles Backup wieder her oder starte eine Core-Version, die ihre Speicherversion lesen kann. Die gesicherte Version-3-Datei unter der älteren Core-Version wiederherzustellen, verursacht denselben Ausfall erneut. Wenn Core RUNNING erreicht, aber einzelne Geräte nicht verfügbar bleiben, untersuche diese Integrationen getrennt. Bewahre die Wiederherstellungskopie und das Cloud-Backup auf, bis das nächste Backup abgeschlossen ist und das Dashboard weiter reagiert.
