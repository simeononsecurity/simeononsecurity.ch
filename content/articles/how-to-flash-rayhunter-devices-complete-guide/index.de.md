---
title: "Rayhunter-Geräte flashen: vollständige Anleitung"
draft: false
toc: true
date: 2026-03-09
lastmod: 2026-11-15
description: "Installiere und konfiguriere Rayhunter zur Erkennung von IMSI-Catchern. Prüfe unterstützte Geräte, installiere die Firmware, verifiziere den Betrieb und behebe häufige Fehler."
tags: ["Rayhunter", "IMSI-Catcher", "Mobilfunkzellen-Simulator", "mobile Sicherheit", "Überwachungserkennung", "Datenschutz", "Orbic RC400L", "TP-Link M7350", "mobiler Hotspot", "Geräte flashen", "Cybersicherheit", "WLAN-Sicherheit", "Maßnahmen gegen Überwachung", "EFF", "Datenschutz-Tools", "Rayhunter kaufen", "Installationsanleitung", "Konfiguration", "unterstützte Geräte", "Netzwerksicherheit"]
cover: "/img/cover/rayhunter.webp"
coverAlt: "Ein Rayhunter-Gerät erkennt Funksignale und IMSI-Catcher, umgeben von Schutzschilden"
coverCaption: "Rayhunter-System zur Erkennung von IMSI-Catchern und zum Schutz mobiler Kommunikation vor Überwachung"
---

**Vollständige Anleitung zum Flashen und Konfigurieren von Rayhunter, dem Erkennungssystem für IMSI-Catcher.**

## Kurzfassung

**Rayhunter** ist ein quelloffenes System zur Erkennung von IMSI-Catchern, das auf modifizierten mobilen Hotspots läuft. Es warnt dich, wenn Überwachungsgeräte versuchen, Mobilfunkkommunikation abzufangen. Diese Anleitung behandelt die vollständige Installation auf Orbic RC400L- und TP-Link-M7350-Geräten, Konfigurationsoptionen, Bedrohungsanalysen und die Wirksamkeit in 5G-Netzen. Du benötigst ein kompatibles Gerät mit Qualcomm-Modem. Das System erkennt Überwachung in 2G-, 3G- und 4G-Netzen anhand mehrerer Heuristiken. Trotz der Verbreitung von 5G bleibt es nützlich, da Angriffe, die Geräte auf ältere Netzgenerationen zurückstufen, weiterhin möglich sind. Es bietet Journalistinnen und Journalisten, Aktivistinnen und Aktivisten sowie datenschutzbewussten Menschen wichtigen Schutz vor staatlicher, krimineller und unternehmerischer Überwachung.

**Rayhunter** erkennt IMSI-Catcher, auch als Mobilfunkzellen-Simulatoren bezeichnet, die mobile Kommunikation abfangen können. Wenn du **Rayhunter kaufen** oder erfahren möchtest, wie du diese Geräte flashst und konfigurierst, findest du in dieser umfassenden Anleitung Informationen zu Installation, Konfiguration und Nutzung des **Rayhunter**-Systems.

**Sponsorhinweis:** Dieser Artikel wird von [STS Collective](https://stscollective.com) gesponsert, dem wichtigsten Anbieter Rayhunter-kompatibler Geräte. Trotz dieser Förderung beruhen alle technischen Angaben, Analysen und Empfehlungen in diesem Artikel ausschließlich auf der offiziellen Rayhunter-Dokumentation, Rückmeldungen aus der Community und einer objektiven technischen Einschätzung.

> 💰 **Exklusiver Leserrabatt:** Spare bis zu 20 % auf Rayhunter-Geräte und Produkte von STS Collective. Verwende beim Bezahlen den Code **SIMEONONSECURITY** oder [kaufe direkt mit angewendetem Rabatt](https://stscollective.com/discount/SIMEONONSECURITY).

## Einführung in Rayhunter

**Rayhunter** ist ein fortschrittliches System zur Erkennung von IMSI-Catchern, entwickelt von der **Electronic Frontier Foundation (EFF)**, einer führenden gemeinnützigen Organisation zur Verteidigung der Bürgerrechte in der digitalen Welt. Seit 1990 setzt sich die EFF durch strategische Gerichtsverfahren, politische Analysen, Basisaktivismus und Technologieentwicklung für digitale Privatsphäre, freie Meinungsäußerung und Innovation ein.

Das Tool läuft auf kompatiblen mobilen Hotspots und überwacht Mobilfunknetze kontinuierlich auf verdächtige Aktivitäten, die auf Mobilfunkzellen-Simulatoren oder für Überwachung eingesetzte Stingrays hindeuten können. **Rayhunter** steht für das Engagement der EFF, praktische Datenschutz-Tools für Einzelpersonen und Organisationen bereitzustellen, die Schutz vor Überwachung benötigen.

Das **Rayhunter**-System sendet Echtzeitwarnungen, wenn potenziell schädliches Verhalten im Mobilfunknetz erkannt wird. Damit ist es ein wichtiges Datenschutz-Tool für Journalistinnen und Journalisten, Aktivistinnen und Aktivisten, Sicherheitsfachkräfte und datenschutzbewusste Menschen. Kompatible Geräte mit **[Rayhunter kaufen](https://stscollective.com/collections/rayhunter)** erhältst du bei STS Collective, dem wichtigsten Anbieter dieser Spezialgeräte.

### Das Rayhunter-Projekt unterstützen

**Rayhunter** ist ein quelloffenes Projekt, das von der Unterstützung der Community profitiert. Du kannst auf verschiedene Weise zur Weiterentwicklung beitragen:

- **Kauf bei STS Collective**: STS Collective spendet einen Teil des Gewinns jedes verkauften Rayhunter-Geräts an die EFF, um die weitere Entwicklung von **Rayhunter** und die Datenschutzforschung zu unterstützen.
- **Direkte Spenden**: Unterstütze die umfassendere Datenschutzarbeit der EFF und die Entwicklung von **Rayhunter** direkt unter **[An die EFF spenden](https://supporters.eff.org/donate/donate)**.
- **An der Community teilnehmen**: Beteilige dich über das offizielle GitHub-Repository an Diskussionen, Dokumentation und Tests.

Deine Unterstützung trägt dazu bei, dass **Rayhunter** kostenlos, quelloffen und laufend verbessert bleibt, um neuen Überwachungsbedrohungen entgegenzuwirken.

## Unterstützung, Rückmeldungen und Gemeinschaft

**Rayhunter** wird von einer aktiven Community aus Sicherheitsforschenden, Datenschutzaktivisten und engagierten Bürgern unterstützt. Über verschiedene Kanäle erhältst du Hilfe und kannst zum Projekt beitragen:

- **Offizielle Dokumentation**: [Rayhunter-Dokumentation](https://efforg.github.io/rayhunter/introduction.html) mit vollständigen Anleitungen zu Installation, Konfiguration und Nutzung
- **GitHub-Repository**: [EFForg/rayhunter](https://github.com/EFForg/rayhunter)
- **Community-Diskussionen**: Starte Diskussionen auf GitHub zur Gerätekompatibilität und Fehlerbehebung
- **Sicherheitsforschung**: Arbeite mit Forschenden zusammen, um die Erkennungsfunktionen von **Rayhunter** zu verbessern

Kompatible Geräte mit **[Rayhunter kaufen](https://stscollective.com/collections/rayhunter)** sind bei STS Collective erhältlich.

## Häufig gestellte Fragen

### Benötige ich eine aktive SIM-Karte für Rayhunter?

**Rayhunter** benötigt eine SIM-Karte im Gerät, aber keinen aktiven Mobilfunktarif. Die SIM-Karte ist erforderlich, damit sich das Gerät mit Mobilfunknetzen verbinden und auf verdächtige Aktivitäten prüfen kann. Wenn du das Gerät gleichzeitig mit **Rayhunter** als Hotspot nutzen möchtest, brauchst du einen aktiven Tarif.

### Wie teste ich, ob mein Rayhunter-Gerät funktioniert?

Aktiviere die Testheuristik in den Konfigurationseinstellungen von **Rayhunter**. Dadurch werden jedes Mal Warnungen ausgelöst, wenn dein Gerät eine Mobilfunkzelle erkennt. So kannst du prüfen, ob das System funktioniert. Dieser Testmodus erzeugt viele Meldungen. Deaktiviere ihn nach dem Test.

### Sollte ich ein gesperrtes oder entsperrtes Gerät kaufen?

Für **Rayhunter** sind entsperrte Geräte in der Regel besser geeignet, insbesondere wenn du SIM-Karten anderer Anbieter als Verizon verwenden möchtest. Die meisten Orbic-Geräte mit Verizon-Marke sind tatsächlich entsperrt. Prüfe die Kompatibilität dennoch vor dem Kauf. Verifizierte kompatible Geräte mit **[Rayhunter kaufen](https://stscollective.com/collections/rayhunter)** gibt es bei STS Collective.

{{< stscollective-ad "rayhunter" >}}

## Installationsanleitung

### Installation aus der neuesten Version

Die Installation von **Rayhunter** wurde unter macOS und Ubuntu 24.04 getestet. Falls es mit vorkompilierten Versionen Probleme gibt, musst du möglicherweise aus dem Quellcode installieren.

#### Voraussetzungen

Stelle vor der Installation von **Rayhunter** sicher, dass du ein kompatibles Gerät hast. Lege bei TP-Link-Geräten eine FAT-formatierte SD-Karte zur Speicherung von Aufzeichnungen ein.

#### Herunterladen und Einrichten

1. **Lade die neueste Version herunter**: Lade die passende Datei `rayhunter-vX.X.X-PLATFORM.zip` von der offiziellen Release-Seite herunter:
   - Linux x64: `linux-x64`
   - Linux ARM64: `linux-aarch64`
   - Linux ARM v7/v8: `linux-armv7`
   - macOS Intel: `macos-intel`
   - macOS ARM (M1/M2): `macos-arm`
   - Windows: `windows-x86_64`

2. **Entpacke das Archiv und wechsle in den Ordner**:
   ```bash
   unzip ~/Downloads/rayhunter-vX.X.X-PLATFORM.zip
   cd ~/Downloads/rayhunter-vX.X.X-PLATFORM
   ```

3. **Verbinde dich mit dem Gerät**: Schalte es ein und verbinde dich per WiFi oder USB-Tethering. Diese Adressen sollten erreichbar sein:
   - Orbic-Geräte: `http://192.168.1.1`
   - TP-Link-Geräte: `http://192.168.0.1`

#### Installation für bestimmte Geräte

**Für Orbic RC400L-Geräte** (erhältlich **[mit Rayhunter](https://stscollective.com)**):

**Rayhunter** unterstützt zwei Installationsmethoden für Orbic-RC400L-Geräte. Die WiFi-Methode wird den meisten Nutzern empfohlen. Die USB-Methode bietet zusätzliche Möglichkeiten zur Fehlersuche.

**Installation per WiFi (empfohlen)**:
```bash
# macOS-Nutzer müssen diesen Befehl zuerst ausführen:
xattr -d com.apple.quarantine installer

# Für Verizon RC400L (das Admin-Passwort entspricht dem WiFi-Passwort):
./installer orbic --admin-password 'YourWiFiPassword'

# Für Kajeet/Smartspot RC400L:
./installer orbic --admin-password='$m@rt$p0tc0nf!g'

# Für Moxee-Geräte (Passwortformat: 12$ + die letzten 3 Ziffern des WiFi-Passworts):
./installer orbic --admin-password='12$XXX'
```

**Installation per USB (für fortgeschrittene Nutzer)**:
Die USB-Methode ermöglicht ADB-Zugriff (Android Debug Bridge) zur erweiterten Fehlersuche, wird für normale Installationen jedoch nicht empfohlen:

```bash
# WARNUNG: Der USB-Installer wird für die meisten Anwendungsfälle nicht empfohlen
./installer orbic-usb
```

Diese Methode versetzt das Gerät in den Debug-Modus, um ADB-Zugriff zu ermöglichen, installiert rootshell und **Rayhunter** und startet das Gerät anschließend neu. Verwende sie nur, wenn du ADB für andere Zwecke benötigst.

**Für TP-Link-M7350-Geräte** (erhältlich **[mit Rayhunter](https://stscollective.com)**):
```bash
./installer tplink
```

Der Installer schließt das Flashen von **Rayhunter** ab und startet das Gerät neu. Eine grüne Linie auf dem Display zeigt an, dass **Rayhunter** erfolgreich läuft.

### Installation aus dem Quellcode

Für Entwickler und Nutzer, die **Rayhunter** selbst aus dem Quellcode erstellen möchten, enthält das Projekt:

- **Frontend**: JavaScript-SvelteKit-Anwendung (`./daemon/web/`)
- **Backend**: Rust-Binärdatei `rayhunter-daemon` (`./daemon/`)
- **Installer**: Rust-Binärdatei mit allen Komponenten (`./installer`)

#### Abhängigkeiten zum Kompilieren

Installiere die folgenden Abhängigkeiten:
- Programmiersprache Rust
- Node.js/npm
- C-Compiler-Werkzeuge (`build-essential` unter Linux, `xcode-select --install` unter macOS)

#### Kompilierungsprozess

```bash
./scripts/build-dev.sh
./scripts/install-dev.sh orbic  # Ersetze 'orbic' durch deinen Gerätetyp
```

Für die Frontend-Entwicklung mit automatischem Neuladen:
```bash
cd daemon/web
npm run dev
# Oder mit einem benutzerdefinierten Ziel:
API_TARGET=http://192.168.1.1:8080 npm run dev
```

### Rayhunter aktualisieren

Die Aktualisierung von **Rayhunter** läuft genauso ab wie die Installation. Wiederhole die Installationsschritte mit der neuesten Version, um dein Gerät auf die aktuellste **Rayhunter**-Version zu aktualisieren.

## Konfiguration

Du kannst **Rayhunter** über die Weboberfläche konfigurieren oder `/data/rayhunter/config.toml` direkt auf dem Gerät bearbeiten.

### Konfiguration über die Weboberfläche

Verbinde dich mit dem Netzwerk deines Geräts und rufe die **Rayhunter**-Weboberfläche unter folgender Adresse auf:
- Orbic: `http://192.168.1.1:8080`
- TP-Link: `http://192.168.0.1:8080`

{{< figure src="rayhunter-dashboard.webp" alt="Dashboard der Rayhunter-Weboberfläche" caption="Die Rayhunter-Weboberfläche bietet umfassende Überwachungs- und Konfigurationsoptionen" >}}

#### Wichtige Konfigurationsoptionen

**Geräte-UI-Stufe**: Legt fest, was **Rayhunter** auf dem Gerätedisplay anzeigt:
- **Unsichtbarer Modus**: keine Anzeige
- **Dezenter Modus**: farbige Linie (grün = sicher, rot = Warnung, weiß = pausiert)
- **Demomodus**: Orca-Grafik mit Statuszeile
- **EFF-Logo**: EFF-Logo mit Statuszeile
- **Hohe Sichtbarkeit**: farbige Vollbildanzeige

**Eingabemodus des Geräts**: Konfiguriere das Verhalten der Einschalttaste:
- **Tastensteuerung deaktivieren**: Die Einschalttaste ist für **Rayhunter** deaktiviert
- **Doppeltippen zum Neustart der Aufzeichnung**: Setzt Warnungen zurück und startet die Überwachung neu

**Benachrichtigungseinstellungen**: Konfiguriere die ntfy-URL für Remote-Warnungen und aktiviere oder deaktiviere Meldungen bei Warnungen und niedrigem Akkustand.

**Analyzer-Heuristiken**: Aktiviere oder deaktiviere bestimmte **Rayhunter**-Erkennungsalgorithmen passend zu Umgebung und Bedrohungsmodell.

## Rayhunter deinstallieren

### Orbic-Geräte

Entferne **Rayhunter** von Orbic-Geräten mit diesem Befehl:

```bash
./installer util orbic-shell --admin-password mypassword
```

Führe in der Shell Folgendes aus:

> **Warnung:** Die folgenden Befehle löschen Rayhunter-Dateien und Start-Hooks dauerhaft. Prüfe, ob du dich in der Shell des vorgesehenen Geräts befindest. Sichere benötigte Aufzeichnungen oder Konfigurationen und halte den Installer sowie kompatible Firmware bereit, bevor du fortfährst. Prüfe danach, ob die Dateien fehlen und das Gerät ohne Rayhunter-Dienst neu startet. Installiere die passende Version aus dem offiziellen Repository erneut, falls du die Änderungen rückgängig machen musst.

```bash
echo 3 > /usrdata/mode.cfg
rm -rf /data/rayhunter /etc/init.d/rayhunter_daemon /bin/rootshell
reboot
```

### TP-Link-Geräte

So deinstallierst du Rayhunter von TP-Link-Geräten:

> **Warnung:** Diese Befehle entfernen Rayhunter-Dateien und den zugehörigen Start-Hook vom TP-Link-Gerät. Exportiere zuerst Aufzeichnungen und Konfigurationen. Führe die Befehle nur in der Geräteshell aus. Prüfe anschließend, ob die Pfade fehlen und das Gerät normal startet. Installiere zum Zurücksetzen die passende Version aus dem offiziellen Repository erneut.

```bash
./installer util tplink-shell
rm /data/rayhunter /etc/init.d/rayhunter_daemon
update-rc.d rayhunter_daemon remove
```

Entferne verbleibende Port-Trigger in der TP-Link-Verwaltungsoberfläche unter Settings > NAT Settings > Port Triggers.

## Rayhunter verwenden

Nach der Installation startet **Rayhunter** automatisch und überwacht Mobilfunknetze kontinuierlich auf verdächtige Aktivitäten. Im Normalbetrieb zeigt das Gerätedisplay eine grüne Linie. Bei potenziellen IMSI-Catchern wechselt sie zu gelben Punkten, orangefarbenen Strichen oder einer durchgezogenen roten Linie.

### Rayhunters Erkennungsheuristiken

**Rayhunter** verwendet mehrere fortschrittliche Erkennungsalgorithmen, um mögliche Aktivitäten von IMSI-Catchern festzustellen:

#### Erkennung angeforderter IMSI
Diese Heuristik erkennt verdächtige Abläufe, bei denen Mobilfunkzellen die Geräteidentität (IMSI, International Mobile Subscriber Identity) ohne ordnungsgemäße Authentifizierungsverfahren anfordern. **Rayhunter** überwacht Zeitpunkt und Kontext dieser Anfragen und markiert ungewöhnliche Muster, die auf Überwachungsgeräte hindeuten.

Legitime Mobilfunknetze halten standardisierte Authentifizierungsverfahren ein, bevor sie sensible Kennungen anfordern. IMSI-Catcher umgehen diese Verfahren häufig, um Geräteidentitäten schnell zu erfassen. Dadurch entstehen erkennbare Auffälligkeiten im Authentifizierungsablauf. Diese Methode eignet sich besonders zur Erkennung einfacher „passiver“ IMSI-Catcher, die lediglich Gerätedaten sammeln.

#### Erkennung von Verbindungsabbrüchen und Rückstufung auf 2G
**Rayhunter** überwacht kontinuierlich verdächtige Versuche, mobile Geräte von sicheren 4G-/5G-Netzen zu trennen und wieder mit weniger sicheren 2G-Netzen zu verbinden. IMSI-Catcher verwenden diesen Rückstufungsangriff häufig, weil 2G-Netze schwächer verschlüsselt und leichter abzufangen sind.

Das System analysiert Muster bei Verbindungsabbrüchen und achtet auf ungewöhnliche Häufigkeit, Zeitpunkte und Zusammenhänge, die eher auf böswillige Absichten als auf normale Netzwerkoptimierung hindeuten. Legitime Netze schlagen aus Gründen der Abdeckung oder Kapazität gelegentlich einen Wechsel zu älteren Netzen vor. **Rayhunter** kann normales Netzwerkverhalten jedoch von möglicher Überwachung unterscheiden.

#### Erkennung von LTE-SIB6/7-Rückstufungen
System Information Blocks (SIB) sind Broadcast-Nachrichten, mit denen Mobilfunknetze Konfigurationsinformationen an Mobilgeräte senden. **Rayhunter** überwacht speziell SIB6- und SIB7-Nachrichten, die Angaben zu Nachbarzellen und zur Umleitung von Frequenzen enthalten.

Böswillige Akteure können gefälschte SIB6/7-Nachrichten senden, um Geräte dazu zu bringen, sichere 4G-Verbindungen zu verlassen und sich mit kontrollierten 2G-Netzen zu verbinden. **Rayhunter** analysiert diese Aussendungen auf Widersprüche, ungewöhnliche Umleitungsmuster und weitere Anzeichen für gefälschte Basisstationen, die Geräte zur Überwachung auf ein älteres Netz zwingen.

#### Erkennung von Nullverschlüsselung
Diese wichtige Erkennungsmethode stellt fest, wenn Mobilfunknetze eine Kommunikation ohne Verschlüsselung, also mit einer Nullverschlüsselung, vorschlagen. Legitime kommerzielle Mobilfunknetze sollten niemals unverschlüsselte Verbindungen vorschlagen, da dies Sicherheitsstandards und regulatorische Anforderungen verletzen würde.

**Rayhunter** kennzeichnet jedes Netz, das Nullverschlüsselung vorschlägt, als höchst verdächtig. *Ein legitimes Netz wird niemals Nullverschlüsselung vorschlagen.* Das ist ein klarer Hinweis auf Überwachungsgeräte, die Kommunikation im Klartext abfangen wollen. Diese Heuristik eignet sich besonders zur Erkennung von IMSI-Catchern, denen die Datenerfassung wichtiger ist als der Anschein eines legitimen Netzes.

#### Erkennung unvollständiger SIBs
Legitime Mobilfunkbasisstationen senden vollständige System Information Blocks mit den wesentlichen Netzwerkkonfigurationsdaten. **Rayhunter** überwacht Basisstationen, die unvollständige oder fehlende Systeminformationen bereitstellen. Das deutet häufig auf hastig eingesetzte oder falsch konfigurierte Überwachungsgeräte hin.

IMSI-Catcher implementieren oft nicht die vollständige Funktionalität eines Mobilfunknetzes, sondern nur das Mindestmaß, das zum Verbinden von Geräten und Abfangen von Daten nötig ist. Indem **Rayhunter** solche unvollständigen Implementierungen erkennt, kann es potenziell bösartige Basisstationen identifizieren, denen der Funktionsumfang legitimer Mobilfunkinfrastruktur fehlt.

{{< figure src="rayhunter-heuristics-overview.webp" alt="Diagramm der fünf Rayhunter-Erkennungsheuristiken: IMSI-Anfrage ohne Authentifizierung, Rückstufung auf 2G, LTE-SIB6/7-Umleitung, Vorschlag einer Nullverschlüsselung und unvollständige Systeminformationsaussendung" >}}
## Bedrohungsakteure und potenzielle Ziele

Es ist wichtig zu verstehen, wer IMSI-Catcher einsetzt und wen sie ins Visier nehmen. So kannst du dein persönliches Bedrohungsmodell einschätzen und eine passende **Rayhunter**-Konfiguration bestimmen. Bedrohungsakteure verfügen über unterschiedliche technische Fähigkeiten. Ihre Zielauswahl beeinflusst, welche Überwachungsaktivitäten **Rayhunter** erkennen soll.

### Behörden und Strafverfolgungsbehörden

**Technische Ausgereiftheit der Bedrohung**: fortgeschritten bis professionell
**Hauptziele**:
- Kriminelle Verdächtige unter Ermittlung
- Personen von Interesse in Fällen der nationalen Sicherheit
- Demonstrierende und Aktivisten bei Protesten
- Überwachung der Bevölkerung in Hochsicherheitsbereichen
- Ausländische Staatsangehörige und diplomatisches Personal

**Erkennungsmuster**: Von Behörden betriebene IMSI-Catcher verwenden häufig ausgefeilte Geräte, die einfache Erkennungsheuristiken umgehen können. Sie nutzen jedoch oft **Angriffe zur Rückstufung auf 2G** und **Muster von Verbindungsabbrüchen**, um Geräte in weniger sichere Netze zu zwingen und so das Abfangen zu erleichtern. Die Erkennung von LTE-SIB6/7-Rückstufungen und die Überwachung von Verbindungsabbrüchen durch **Rayhunter** sind besonders wirksam gegen Überwachungstechniken der Strafverfolgungsbehörden.

**Typische Szenarien**:
- Anlassbezogene Überwachung bei Protesten, Kundgebungen oder öffentlichen Versammlungen
- Standortbezogene Überwachung in der Nähe von Behörden oder sensibler Infrastruktur
- Gezielte Überwachung bestimmter Personen unter Ermittlung
- Überwachung an Grenzen und Flughäfen

### Inlands- und Auslandsnachrichtendienste

**Technische Ausgereiftheit der Bedrohung**: professionell bis militärisch
**Hauptziele**:
- Ausländische Agenten und Quellen von Nachrichtendiensten
- Regierungsvertreter und diplomatisches Personal
- Verteidigungsauftragnehmer und Forschende
- Führungskräfte in strategischen Industrien
- Journalisten zu Themen der nationalen Sicherheit
- Aktivisten, die sich mit politisch sensiblen Themen befassen

**Erkennungsmuster**: Geräte für Nachrichtendienste sind auf unauffälligen Betrieb ausgelegt, doch **Rayhunter** kann mit der Erkennung von Nullverschlüsselung und unvollständigen SIBs auch ausgefeilte Überwachungsoperationen erkennen. Nachrichtendienste setzen bei gezielten Operationen oft Geräte ein, die **IMSI-Informationen** anfordern. Dadurch werden die IMSI-Erkennungsalgorithmen von **Rayhunter** ausgelöst.

**Typische Szenarien**:
- Langfristige Überwachung wichtiger nachrichtendienstlicher Ziele
- Industriespionage in der Nähe von Unternehmenszentralen
- Überwachung diplomatischer Einrichtungen und Botschaften
- Gegenspionageoperationen
- Ausländische Nachrichtendienste nehmen inländische Quellen ins Visier

### Kriminelle Organisationen

**Technische Ausgereiftheit der Bedrohung**: einfach bis mittel
**Hauptziele**:
- Vermögende Personen für Entführungen oder Erpressungen
- Geschäftskonkurrenten zur Informationsbeschaffung
- Strafverfolgungsbehörden bei Ermittlungen gegen organisierte Kriminalität
- Zeugen und Informanten in Strafverfahren
- Betroffene von Stalking, Belästigung oder häuslicher Gewalt

**Erkennungsmuster**: Kriminelle Organisationen nutzen meist kostengünstige, kommerziell erhältliche IMSI-Catcher, die mehrere **Rayhunter**-Heuristiken gleichzeitig auslösen. Diese Geräte zeigen häufig **unvollständige SIB-Implementierungen**, verwenden **Nullverschlüsselung** zur Maximierung der Datenerfassung und führen wegen begrenzter technischer Fähigkeiten aggressive **2G-Rückstufungsangriffe** aus.

**Typische Szenarien**:
- Mögliche Entführungs- oder Raubopfer verfolgen
- Kommunikation der Strafverfolgungsbehörden bei kriminellen Einsätzen überwachen
- Industriespionage und Erfassung von Wettbewerbsinformationen
- Stalking und Belästigung
- Zeugen einschüchtern und ihren Standort verfolgen

### Unternehmensspionage und unabhängige Nachrichtendienste

**Technische Ausgereiftheit der Bedrohung**: mittel bis fortgeschritten
**Hauptziele**:
- Führungskräfte konkurrierender Unternehmen
- Forschungs- und Entwicklungsteams
- Verhandelnde bei Fusionen und Übernahmen
- Inhaber geistigen Eigentums
- Verantwortliche für Geschäftsgeheimnisse
- Unternehmens-Whistleblower und Quellen interner Bedrohungen

**Erkennungsmuster**: Unternehmensüberwachung setzt häufig Geräte der mittleren Preisklasse ein, die Kosten und Fähigkeiten ausbalancieren. Bei gezielten Aktivitäten gegen einzelne Personen während Geschäftsverhandlungen oder Produktentwicklungszyklen lösen diese Installationen oft **Erkennung von Verbindungsabbrüchen** und **Warnungen bei IMSI-Anfragen** aus.

**Typische Szenarien**:
- Überwachung bei Verhandlungen zu Fusionen und Übernahmen
- Wettbewerbsinformationen auf Fachmessen und Konferenzen sammeln
- Diebstahl geistigen Eigentums
- Mitarbeitende überwachen und interne Bedrohungen erkennen
- Kundendaten zum Wettbewerbsvorteil sammeln

### Privatdetektive und Überwachungsfirmen

**Technische Ausgereiftheit der Bedrohung**: einfach bis mittel
**Hauptziele**:
- Personen unter Ermittlung wegen Versicherungsbetrugs
- Ehepartner in Scheidungsverfahren
- Mitarbeitende bei Verdacht auf Fehlverhalten
- Personen in Rechtsstreitigkeiten
- Prominente und andere öffentlich bekannte Ziele

**Erkennungsmuster**: Private Überwachungsoperationen nutzen in der Regel kommerziell erhältliche Geräte mit begrenzten Anpassungsmöglichkeiten. Aufgrund von Kosten und technischen Einschränkungen lösen diese Systeme häufig die Basisheuristiken von **Rayhunter** aus, insbesondere die **Erkennung von Nullverschlüsselung** und die **Überwachung unvollständiger SIBs**.

**Typische Szenarien**:
- Ermittlungen bei Scheidung und Sorgerechtsstreitigkeiten
- Überwachung bei Versicherungsbetrug
- Untersuchungen wegen Fehlverhaltens von Mitarbeitenden
- Stalking von Prominenten und Paparazzi-Aktivitäten
- Rechtliche Ermittlungen und Beweissicherung

### Böswillige Einzelpersonen und Hacktivisten

**Technische Ausgereiftheit der Bedrohung**: einfach bis mittel
**Hauptziele**:
- Persönliche Feinde oder Beziehungspartner
- Personen des öffentlichen Lebens und Prominente
- Zufällige Betroffene an öffentlichen Orten
- Teilnehmende an bestimmten Veranstaltungen oder Personen an ausgewählten Orten
- Mitglieder gezielter Gemeinschaften oder Gruppen

**Erkennungsmuster**: Einzelne Akteure verwenden üblicherweise einfache, oft improvisierte IMSI-Catcher-Setups, die mehrere Erkennungsalgorithmen von **Rayhunter** gleichzeitig auslösen. Diese zeigen häufig **Nullverschlüsselung**, **unvollständige SIB-Aussendungen** und grobe **Versuche einer Rückstufung auf 2G**.

**Typische Szenarien**:
- Stalking und Belästigung
- Identitätsdiebstahl und Finanzbetrug
- Politischen Aktivismus und Proteste stören
- Allgemeine Cyberkriminalität
- Gelegenheitsüberwachung bei öffentlichen Veranstaltungen

### Bedrohungsbewertung und Rayhunter-Konfiguration

**Personen mit hohem Risiko** (Journalisten, Aktivisten, Regierungsvertreter und Führungskräfte) sollten alle **Rayhunter**-Heuristiken aktivieren und für maximale Erkennung die Anzeigemodi **hohe Sichtbarkeit** verwenden.

**Personen mit moderatem Risiko** (allgemein datenschutzbewusste Nutzer) können für den täglichen Schutz den **dezenten Modus** mit den zentralen Erkennungsheuristiken verwenden, ohne Aufmerksamkeit zu erregen.

**Schutz bei Veranstaltungen** (Proteste, sensible Treffen, Reisen) spricht dafür, vorübergehend alle Erkennungsmethoden und Benachrichtigungssysteme zu aktivieren, um Überwachungsaktivitäten umfassend wahrzunehmen.

Wenn du dein Bedrohungsmodell kennst, kannst du die **Rayhunter**-Konfiguration auf dein konkretes Risikoprofil abstimmen und eine angemessene Erkennung gegen Akteure sicherstellen, die dich oder deine Aktivitäten wahrscheinlich ins Visier nehmen.

{{< figure src="imsi-catcher-threat-actors-surveillance.webp" alt="Diagramm verschiedener Bedrohungsakteure mit IMSI-Catchern, darunter Behörden, kriminelle Organisationen und Akteure der Unternehmensspionage, die Mobilgeräte ins Visier nehmen" >}}

## Rayhunters Wirksamkeit im 5G-Zeitalter

{{< figure src="rayhunter-5g-downgrade-attack-persistence.webp" alt="Diagramm eines 5G-fähigen Telefons, das durch einen Rückstufungsangriff in ein überwachtes 4G- oder 3G-Netz gezwungen wird, eine Technik, die Rayhunter auch im 5G-Zeitalter erkennt" >}}

Beim Übergang der Mobilfunknetze zu 5G stellt sich die Frage, wie wirksam **Rayhunter** angesichts seiner Erkennung von 2G-, 3G- und 4G/LTE-Netzen, aber nicht nativer 5G-Überwachungsmethoden bleibt. Um langfristige Strategien zur Überwachungserkennung zu planen, musst du die aktuellen Einschränkungen und die anhaltende Relevanz von **Rayhunter** im 5G-Zeitalter verstehen.

### Warum Rayhunter in 5G-Netzen wirksam bleibt

#### Rückstufungsangriffe bleiben bestehen
Der grundlegende Angriffsvektor, den **Rayhunter** erkennt, also Geräte zu Verbindungen mit weniger sicheren Netzen zu zwingen, bleibt bei der Einführung von 5G relevant. **IMSI-Catcher setzen weiterhin Rückstufungsangriffe auf 2G und 3G ein**, weil:

- **Geringere Umsetzungskosten**: Überwachungsgeräte für ältere Protokolle zu bauen erfordert deutlich weniger Investitionen als die Entwicklung 5G-fähiger Systeme.
- **Breitere Gerätekompatibilität**: Angriffe auf 2G/3G funktionieren auch gegen ältere Geräte ohne 5G-Unterstützung.
- **Etablierte Angriffsmethoden**: Überwachungstechniken für 2G/3G-Netze sind gut dokumentiert und erprobt.
- **Regulatorische Vorteile**: Für ältere Überwachungstechnologien können weniger rechtliche Einschränkungen gelten als für fortschrittliche 5G-Abhörmethoden.

#### Rückwärtskompatibilität der Netze
5G-Netze behalten die **Rückwärtskompatibilität mit 4G/LTE**, und die meisten Mobilgeräte unterstützen mehrere Generationen gleichzeitig. Dadurch bestehen weiterhin Möglichkeiten für Rückstufungsangriffe, auf die **Rayhunter** spezialisiert ist:

- **Automatische Rückstufung**: Bei schlechter 5G-Abdeckung wechseln Geräte automatisch zu 4G. Überwachungsgeräte können diesen Wechsel abfangen.
- **Schwachstellen bei der Protokollverhandlung**: Ausgefeilte IMSI-Catcher können den Handshake zwischen verschiedenen Netzgenerationen manipulieren.
- **Ausnutzen von Abdeckungslücken**: Strategisch in Gebieten mit unvollständiger 5G-Abdeckung eingesetzte Überwachungsgeräte können Geräte in kontrollierte 4G/LTE-Netze zwingen.

#### Schrittweiser 5G-Ausbau
Der **langsame Ausbau einer flächendeckenden 5G-Abdeckung** sorgt dafür, dass **Rayhunter** noch jahrelang relevant bleibt:

- **Stadt-Land-Unterschiede**: Viele Regionen sind weiterhin vorwiegend auf 4G/LTE angewiesen, wo die Erkennungsfunktionen von **Rayhunter** unmittelbar anwendbar sind.
- **Eingeschränkter Empfang in Gebäuden**: 5G-Signale dringen oft schlecht durch Gebäude. Geräte wechseln daher zu 4G-Netzen, die **Rayhunter** wirksam überwachen kann.
- **Internationale Reisen**: Der weltweite 5G-Ausbau unterscheidet sich deutlich je nach Land. Überwachung über 4G/LTE bleibt deshalb für Reisende ein Thema.

#### Technologischer Rückstand von Bedrohungsakteuren
Die Zyklen für **Beschaffung und Einsatz von Überwachungsgeräten** hinken kommerzieller Netzwerktechnik häufig hinterher:

- **Zeitpläne für staatliche Beschaffung**: Strafverfolgungs- und Nachrichtendienste verwenden möglicherweise noch Jahre nach dem 5G-Ausbau vorhandene 4G-Überwachungsgeräte.
- **Kosten-Nutzen-Analyse**: Viele Überwachungsoperationen erreichen ihre Ziele mit günstigerem 4G/LTE-Abfangen. Das verringert den Anreiz für einen Wechsel zu 5G-Systemen.
- **Schulungs- und Fachkenntnisse**: Der Betrieb von 5G-Überwachungsgeräten erfordert Spezialwissen, das Überwachungsorganisationen erst erwerben müssen.

### Einschränkungen von Rayhunter in echten 5G-Umgebungen

#### Erkennungslücken bei nativer 5G-Überwachung
*Dies ist die wichtigste Einschränkung von Rayhunter.* **Rayhunter kann native 5G-IMSI-Catcher-Operationen nicht erkennen**, wenn diese keine Rückstufungsangriffe verwenden:

- **Eigenständige 5G-Netze (SA)**: Wenn Geräte ohne Rückfall auf 4G eine reine 5G-Verbindung nutzen, kann **Rayhunter** diese Kommunikation nicht überwachen.
- **Fortschrittliche 5G-Überwachungsgeräte**: Ausgefeilte Bedrohungsakteure mit Zugriff auf moderne Technik könnten 5G-Kommunikation abfangen, ohne Erkennungsheuristiken von **Rayhunter** auszulösen.
- **Ausnutzen von Network Slicing**: Funktionen zur Netzaufteilung in 5G könnten für Überwachung missbraucht werden, die **Rayhunter** nicht erkennt.

#### Verbesserte 5G-Sicherheitsfunktionen
5G-Netze enthalten **verbesserte Sicherheitsmaßnahmen**, die herkömmliche Überwachungstechniken weniger wirksam machen könnten:

- **Stärkere Verschlüsselungsprotokolle**: 5G verwendet robustere Standards, die schwerer zu knacken sind als bei früheren Generationen.
- **Verbesserte Authentifizierung**: Eine bessere Geräteauthentifizierung in 5G-Netzen könnte das Sammeln von IMSI erschweren.
- **Überwachung der Netzwerksicherheit**: 5G-Infrastruktur bietet bessere Funktionen zur Angriffserkennung, die Überwachungsversuche identifizieren und abwehren können.

#### Veränderungen im Geräteverhalten
Mit der Verbreitung von 5G **kann sich das Verhalten mobiler Geräte ändern** und so die Erkennungsfunktionen von **Rayhunter** beeinflussen:

- **Weniger Bereitschaft zur Rückstufung**: Künftige Softwareupdates könnten Geräte angesichts besserer 5G-Abdeckung widerstandsfähiger gegen Rückstufungsangriffe machen.
- **Bevorzugung von 5G-Verbindungen**: Geräte priorisieren möglicherweise zunehmend 5G-Verbindungen und reagieren misstrauischer auf Anfragen zur Nutzung älterer Protokolle.
- **Besseres Sicherheitsbewusstsein**: Mobile Betriebssysteme könnten verdächtiges Netzwerkverhalten besser erkennen.

### Strategische Überlegungen zum Einsatz von Rayhunter

#### Aktuelle Empfehlungen
Für den sofortigen und nahen Einsatz bietet **Rayhunter** **umfassende Funktionen zur Überwachungserkennung**:

- **Einsatz in Städten**: Selbst in Großstädten mit umfassender 5G-Abdeckung erkennt **Rayhunter** Überwachungsversuche in 4G/LTE-Netzen.
- **Schutz bei wichtigen Veranstaltungen**: Bei Protesten, vertraulichen Treffen oder Aktivitäten mit hohem Risiko bietet **Rayhunter** wichtige Erkennungsfunktionen unabhängig von der 5G-Verfügbarkeit.
- **Reisesicherheit**: **Rayhunter** erkennt Überwachung auf nationalen und internationalen Reisen weiterhin sehr wirksam.

#### Strategien zur Zukunftssicherheit
Organisationen und Einzelpersonen, die eine langfristige Überwachungserkennung planen, sollten Folgendes berücksichtigen:

- **Hybride Erkennungsansätze**: Die Kombination von **Rayhunter** mit anderen Sicherheits-Tools und Überwachungsmethoden bietet umfassende Abdeckung mehrerer Bedrohungsvektoren.
- **Regelmäßige Aktualisierung der Bedrohungsbewertung**: Die Entwicklung von Überwachungstechnologie zu verfolgen hilft bei der Entscheidung, wann die Funktionen von **Rayhunter** ergänzt oder ersetzt werden sollten.
- **Community-Entwicklung unterstützen**: Die Unterstützung der quelloffenen Entwicklung von **Rayhunter** erhöht die Wahrscheinlichkeit, dass künftige Versionen 5G-Erkennung ergänzen.

#### Technologische Entwicklung beobachten
Die **Rayhunter**-Community und die EFF erforschen weiterhin **Funktionen zur Erkennung von 5G-Überwachung**:

- **Forschung zur Protokollanalyse**: Laufende Forschung zu 5G-Protokollen könnte neue Erkennungsmöglichkeiten für künftige **Rayhunter**-Versionen aufzeigen.
- **Studien zur Hardwarekompatibilität**: Es wird untersucht, ob aktuelle **Rayhunter**-kompatible Geräte für die Erkennung von 5G-Überwachungsversuchen erweitert werden können.
- **Bedrohungslandschaft beobachten**: Die Entwicklung und Verbreitung 5G-fähiger Überwachungsgeräte zu verfolgen hilft, künftige Entwicklungsprioritäten für **Rayhunter** festzulegen.

**Rayhunter** bleibt ein **wichtiges Tool zur Überwachungserkennung** in der aktuellen Telekommunikationslandschaft. Es dürfte noch mehrere Jahre relevant bleiben, während 5G schrittweise ausgebaut wird und Bedrohungsakteure weiterhin bewährte Rückstufungsangriffe einsetzen.

### Aufzeichnungen erneut analysieren

**Rayhunter** verbessert seine Erkennungsfunktionen laufend. Du kannst ältere Aufzeichnungen mit aktuellen Heuristiken erneut analysieren. Klicke dazu in der Weboberfläche auf "N warnings" und wähle "re-analyze".

### Analyse am Computer

Für fortgeschrittene Nutzer enthält **Rayhunter** das CLI-Tool `rayhunter-check` zur Analyse von PCAP- und QMDL-Dateien auf Desktop-Systemen:

```bash
rayhunter-check -p ~/Downloads/myfile.qmdl
rayhunter-check -p ~/Downloads/myfile.pcap
rayhunter-check -d -p ~/Downloads/myfile.qmdl  # Debug-Modus
```

## Unterstützte Geräte

**Rayhunter** unterstützt verschiedene mobile Hotspots mit Qualcomm-Modems, die die Schnittstelle `/dev/diag` bereitstellen.

{{< figure src="/img/rayhunter-device-regions.svg" alt="Kompatibilität von Rayhunter-Geräten nach Region" caption="Gerätekompatibilität und regionale Empfehlungen für Rayhunter-Installationen" >}}
### Empfohlene Geräte

Diese Geräte wurden umfassend getestet und werden in der **Rayhunter**-Community häufig verwendet:

#### Orbic RC400L (manchmal als Kajeet RC400L vermarktet)
- **Empfohlene Region**: Amerika
- **Unterstützte Bänder**:
  - 5G: n260/n261, n77, n2/5/48/66
  - 4G: 2/4/5/12/13/48/66
  - Weltweit und Roaming: n257/n78
- **Verfügbarkeit**: Kompatible Geräte sind erhältlich, darunter **[neuer Orbic RC400L mit Rayhunter](https://stscollective.com/products/new-rayhunter-orbic-rc400l-imsi-catcher-detector-premium?variant=51361976811822)** und **[Kajeet RC400L](https://stscollective.com/products/rayhunter-imsi-catcher-detector-kajeet-rc400lx-4g-lte-hotspot?variant=51411271844142)**
- **Preisspanne**: Professionelle Modelle sind bei STS Collective erhältlich

#### TP-Link M7350
- **Empfohlene Region**: Afrika, Europa und Naher Osten (funktioniert auch in Amerika, ist dort aber in der Regel teurer)
- **Besondere Anforderungen**: Für Aufzeichnungen wird eine FAT-formatierte SD-Karte benötigt
- **Verfügbarkeit**: Verifizierte kompatible Modelle sind als **[TP-Link M7350 mit Rayhunter](https://stscollective.com/collections/rayhunter)** erhältlich

### Funktionsfähige Geräte

Es wurde bestätigt, dass **Rayhunter** auch auf diesen Geräten funktioniert:

- **Wingtech CT2MHS01** (Amerika), **[mit Rayhunter erhältlich](https://stscollective.com/collections/rayhunter)**
- **Tmobile TMOHS1** (Amerika), **[mit Rayhunter erhältlich](https://stscollective.com/collections/rayhunter)**
- **TP-Link M7310** (Afrika, Europa, Naher Osten), **[mit Rayhunter erhältlich](https://stscollective.com)**
- **PinePhone und PinePhone Pro** (weltweit), **[mit Rayhunter erhältlich](https://stscollective.com)**
- **FY UZ801** (Asien, Europa), **[mit Rayhunter erhältlich](https://stscollective.com)**
- **Moxee-Hotspot** (Amerika), **[Moxee K779HSDL mit Rayhunter](https://stscollective.com/products/rayhunter-imsi-catcher-stingray-detector-moxee-k779hsdl-hotspot-professionally-refurbished-pre-installed-4g-lte-cellular-threat-detection-device?variant=51309010420014)**

### Installationshinweise für bestimmte Geräte

#### Orbic/Kajeet RC400L

Der Orbic RC400L ist das ursprüngliche Gerät, für das **Rayhunter** entwickelt wurde. Er ist **[mit Rayhunter erhältlich](https://stscollective.com)** bei STS Collective.

**Installationsmethoden**:
- **Per Netzwerk**: `./installer orbic` (empfohlen, funktioniert über WiFi)
- **Per USB**: `./installer orbic-usb` (ermöglicht ADB-Zugriff und eine Root-Shell)

**Standardpasswörter**:
- **Verizon RC400L**: Das Admin-Passwort ist immer identisch mit dem WiFi-Passwort (im Gerätemenü zu finden)
- **Kajeet/Smartspot RC400L**: `$m@rt$p0tc0nf!g`
- **Moxee-Geräte**: Passwortformat `12$XXX`, wobei XXX die letzten 3 Ziffern des WiFi-Passworts angibt (unter dem Akku zu finden)

**Shell-Zugriff**: Verwende nach der Installation `./installer util orbic-shell`.

#### TP-Link M7350/M7310

Diese Geräte funktionieren zuverlässig mit **Rayhunter** und sind **[mit Rayhunter erhältlich](https://stscollective.com)**.

**Installation**: `./installer tplink` (kein Admin-Passwort erforderlich)
**Speicher**: Lege vor der Installation eine FAT-formatierte SD-Karte ein
**Shell-Zugriff**: `./installer util tplink-shell`

#### Spezialisierte Geräte

**PinePhone und PinePhone Pro**: weltweit kompatibel und **[mit Rayhunter erhältlich](https://stscollective.com)**
**UZ801**: beliebt in Asien und Europa und **[mit Rayhunter erhältlich](https://stscollective.com)**
**Wingtech CT2MHS01**: Gerät für Amerika und **[mit Rayhunter erhältlich](https://stscollective.com)**

### Neue Geräte hinzufügen

**Rayhunter** kann möglicherweise jedes Gerät mit Qualcomm-Modem unterstützen, das die Schnittstelle `/dev/diag` bereitstellt. Wenn du ein Gerät hast, das von **Rayhunter** unterstützt werden soll, starte eine Diskussion im offiziellen GitHub-Repository.

## REST-API-Dokumentation

**Rayhunter** bietet eine umfassende REST-API für den programmatischen Zugriff auf Gerätestatus, Aufzeichnungen und Konfiguration. Die API ermöglicht die Integration mit anderen Sicherheits-Tools und automatisierten Überwachungssystemen.

### Offizielle API-Dokumentation

Die vollständige API-Referenz mit detaillierten Angaben zu Endpunkten, Beispielen für Anfragen und Antworten sowie Authentifizierungsmethoden findest du in der **[offiziellen Rayhunter-REST-API-Dokumentation](https://efforg.github.io/rayhunter/api-docs/)**.

### API-Endpunkte

Die **Rayhunter**-API ist unter `http://[device-ip]:8080/api/` erreichbar und bietet Endpunkte für:

- **Systemstatus**: Gerätezustand und Betrieb von **Rayhunter** überwachen
- **Aufzeichnungsverwaltung**: Aufzeichnungen starten, beenden und herunterladen
- **Warnungen abrufen**: Erkennungswarnungen und Analyseergebnisse aufrufen
- **Konfiguration**: **Rayhunter**-Einstellungen programmatisch aktualisieren
- **Heuristiken steuern**: Bestimmte Erkennungsalgorithmen aktivieren oder deaktivieren
- **Geräteinformationen**: Gerätespezifikationen und Funktionen abrufen
- **Netzwerküberwachung**: Auf Echtzeitdaten des Mobilfunknetzes zugreifen
- **Ereignisprotokoll**: Frühere Erkennungsereignisse und Warnungen abfragen

### Authentifizierung

Für den API-Zugriff gilt dieselbe Authentifizierung wie für die Weboberfläche. Sichere dein **Rayhunter**-Gerät und gewähre nur autorisierten Personen Zugriff.

### Integrationsbeispiele

Die **Rayhunter**-REST-API lässt sich in verschiedene Sicherheitsüberwachungsplattformen, SIEM-Systeme und individuelle Automatisierungstools integrieren. Ausführliche Implementierungsbeispiele und bewährte Vorgehensweisen findest du in der **[offiziellen API-Dokumentation](https://efforg.github.io/rayhunter/api-docs/)**.

## Fehlerbehebung

### Häufige Installationsprobleme

**Probleme mit der USB-Verbindung**: Probiere andere USB-Kabel oder Anschlüsse. Fehlerhafte USB-Verbindungen verursachen häufig Installationsfehler. *Das ist die häufigste Ursache für fehlgeschlagene Installationen.*

**macOS-Sicherheitsprobleme**: Wenn die Meldung "No Orbic device found" erscheint, ändere vorübergehend die Einstellung "Allow accessories to connect" in den Sicherheitseinstellungen auf "Always".

**Geräteerkennung**: Aktiviere nach der Installation die Testheuristik, um zu prüfen, ob **Rayhunter** ordnungsgemäß funktioniert.

### Hilfe erhalten

Unterstützung bei Installation und Fehlerbehebung:
- Lies die offizielle **Rayhunter**-Dokumentation
- Verwende `./installer --help` und `./installer util --help`, um die Befehlsoptionen anzuzeigen
- Stelle Fragen in den GitHub-Diskussionen der Community
- Wende dich bei Fragen zur Gerätekompatibilität an **[STS Collective](https://stscollective.com)**

## Häufig gestellte Fragen (FAQ)

### Allgemeine Fragen

#### Was genau ist ein IMSI-Catcher und wie funktioniert er?
Ein IMSI-Catcher, auch StingRay, Mobilfunkzellen-Simulator oder gefälschter Mobilfunkmast genannt, ist ein Überwachungsgerät, das legitime Mobilfunkzellen nachahmt, um mobile Kommunikation abzufangen. Es zwingt Geräte in der Nähe, sich statt mit legitimen Mobilfunkzellen mit dem schädlichen Gerät zu verbinden. Dadurch können Betreiber Gerätekennungen (IMSI-Nummern), Standortdaten, Anrufmetadaten und möglicherweise Kommunikationsinhalte erfassen. **Rayhunter** erkennt diese Geräte anhand ungewöhnlicher Verhaltensmuster im Mobilfunknetz.

#### Kann Rayhunter alle Arten von Überwachungsgeräten erkennen?
**Rayhunter** erkennt speziell IMSI-Catcher und Mobilfunkzellen-Simulatoren in 2G-, 3G- und 4G/LTE-Netzen. Andere Überwachungsarten wie WLAN-Überwachung, GPS-Tracker, physische Überwachung oder native 5G-Überwachung ohne Rückstufungsangriffe kann es nicht erkennen. **Rayhunter** ist eine Komponente einer umfassenden Datenschutzstrategie.

#### Ist die Nutzung von Rayhunter rechtmäßig?
In den meisten Ländern ist die Nutzung von **Rayhunter** als passives Überwachungs-Tool legal. Es greift nicht in Mobilfunknetze oder andere Geräte ein, sondern analysiert nur Mobilfunksignale, die dein Gerät normal empfängt. Die örtlichen Gesetze unterscheiden sich. Prüfe daher die für dich geltenden Vorschriften. Die EFF hat **Rayhunter** als legitimes Datenschutz-Tool entwickelt.

### Technische Fragen

#### Warum benötigt Rayhunter eine SIM-Karte, wenn kein aktiver Tarif erforderlich ist?
Die SIM-Karte enthält die International Mobile Subscriber Identity (IMSI), die zur Authentifizierung des Geräts im Mobilfunknetz und zur Teilnahme an den von **Rayhunter** überwachten Protokollaustauschen benötigt wird. Ohne SIM-Karte kann sich das Gerät nicht mit Mobilfunknetzen verbinden, sodass **Rayhunter** keine Netzwerkaktivität auf verdächtige Muster analysieren kann.

#### Wie viele Daten verbraucht Rayhunter im Normalbetrieb?
**Rayhunter** verbraucht bei der Basisüberwachung nur wenige Daten, da es hauptsächlich Mobilfunkprotokollinformationen statt Internetverkehr analysiert. Wenn du jedoch Remote-Benachrichtigungen über ntfy aktivierst oder das Gerät gleichzeitig als Hotspot verwendest, steigt der Datenverbrauch. Die Überwachung allein benötigt kaum Bandbreite.

#### Kann ich Rayhunter verwenden, während das Gerät als mobiler Hotspot dient?
Ja, **Rayhunter** kann parallel zur Hotspot-Funktion laufen. Dafür ist ein aktiver Mobilfunktarif erforderlich. Die Überwachung durch **Rayhunter** ist von der Hotspot-Funktion unabhängig. Wenn du beides gleichzeitig nutzt, verbraucht das Gerät jedoch mehr Akku.

#### Was ist der Unterschied zwischen einer Installation per WiFi und per USB?
Bei der **WiFi-Methode** (für die meisten Nutzer empfohlen) wird **Rayhunter** über die drahtlose Schnittstelle des Geräts installiert und bietet Standardfunktionen. Die **USB-Methode** ermöglicht fortgeschrittenen Nutzern den Zugriff auf Android Debug Bridge (ADB), ist aber komplizierter und für normale Installationen nicht erforderlich.

### Fragen zu Geräten und Kompatibilität

#### Warum werden nur bestimmte Geräte von Rayhunter unterstützt?
**Rayhunter** benötigt Geräte mit Qualcomm-Modems, die die Schnittstelle `/dev/diag` bereitstellen. Sie ermöglicht den Zugriff auf Mobilfunkprotokollinformationen. Die meisten Geräte für Verbraucher stellen diese Schnittstelle aus Sicherheitsgründen nicht bereit. Die unterstützten Geräte wurden gezielt getestet und erfüllen nachweislich die Anforderungen von **Rayhunter**.

#### Kann ich Rayhunter auf meinem normalen Smartphone installieren?
Nein, **Rayhunter** lässt sich nicht auf normalen Smartphones installieren. Es erfordert spezielle mobile Hotspots mit bestimmten Qualcomm-Modems, die Diagnoseschnittstellen bereitstellen. Zu den unterstützten Geräten zählen Orbic RC400L, TP-Link M7350 und verschiedene weitere mobile Hotspot-Modelle.

#### Was passiert, wenn ich Rayhunter auf einem inkompatiblen Gerät installiere?
Der **Rayhunter**-Installer erkennt das Gerät und verweigert die Installation auf inkompatibler Hardware normalerweise. Eine erzwungene Installation auf nicht unterstützten Geräten kann das Gerät beschädigen oder unbrauchbar machen. Prüfe vor der Installation stets die Gerätekompatibilität.

#### Benötige ich für verschiedene Regionen unterschiedliche Geräte?
Ja, die Mobilfunkfrequenzbänder unterscheiden sich je nach geografischer Region. Orbic RC400L ist für Netze in Amerika optimiert, TP-Link M7350 funktioniert gut in Europa, Afrika und im Nahen Osten. Die Kompatibilitätsinformationen für **Rayhunter** enthalten regionale Empfehlungen, damit du ein passendes Gerät für deinen Standort wählen kannst.

### Fragen zu Nutzung und Konfiguration

#### Woher weiß ich, ob mein Rayhunter-Gerät ordnungsgemäß funktioniert?
Aktiviere die Testheuristik in den Konfigurationseinstellungen von **Rayhunter**. Sie löst jedes Mal eine Warnung aus, wenn das Gerät eine Mobilfunkzelle erkennt, und bestätigt damit die Funktion des Systems. Im Normalbetrieb sollte das Display eine grüne Linie zeigen. Deaktiviere die Testheuristik nach der Prüfung, da sie viele Warnungen erzeugt.

#### Was soll ich tun, wenn Rayhunter eine Warnung auslöst?
Wenn **Rayhunter** verdächtige Aktivitäten erkennt, notiere zuerst deinen Standort und die Umstände. Netzwerkoptimierung oder Geräteprobleme können zu Fehlalarmen führen. Wiederholen sich Warnungen am selben Ort oder bei sensiblen Aktivitäten, solltest du einen Standortwechsel erwägen und die Warnungsdetails in der Weboberfläche prüfen.

#### Wie oft sollte ich Rayhunter aktualisieren?
**Aktualisiere Rayhunter monatlich.** Prüfe die Release-Seite auf neue Heuristiken und Kompatibilitätsverbesserungen, die regelmäßig ergänzt werden. Die EFF verbessert die Funktionen von **Rayhunter** kontinuierlich als Reaktion auf neue Überwachungstechniken. Die Aktualisierung erfolgt wie die Erstinstallation.

#### Kann Rayhunter mehrere Personen gleichzeitig schützen?
**Rayhunter** erkennt IMSI-Catcher in der Umgebung und kann dadurch mehrere Personen im Empfangsbereich schützen, typischerweise mehrere hundert Meter, abhängig von der Signalstärke. Wer Überwachung ernsthaft erkennen möchte, sollte ein eigenes **Rayhunter**-Gerät in Betracht ziehen, um maximalen Schutz und Kontrolle über die Konfiguration zu erhalten.

### Fragen zu Sicherheit und Datenschutz

#### Mache ich mich durch die Nutzung von Rayhunter für Überwachung sichtbarer?
**Rayhunter** arbeitet passiv und sendet keine Signale, durch die Überwachungsgeräte es identifizieren könnten. Die Nutzung eines Sicherheits-Tools zeigt allerdings ein Bewusstsein für Datenschutz. Die Vorteile der Erkennung überwiegen gewöhnlich die Risiken, besonders für Personen mit hohem Risiko wie Journalisten und Aktivisten.

#### Können Überwachungsgeräte erkennen, dass ich Rayhunter verwende?
**Rayhunter** ist ein passives Überwachungssystem und sendet keine identifizierenden Signale. Überwachungsbetreiber können die Nutzung von **Rayhunter** nicht auf der Ebene des Mobilfunkprotokolls erkennen. Eine physische Beobachtung des Geräts oder eine Analyse des Netzwerkverkehrs könnte die Nutzung von **Rayhunter** jedoch aufdecken, wenn Remote-Benachrichtigungen aktiviert sind.

#### Welche Informationen sammelt Rayhunter über mich?
**Rayhunter** analysiert Mobilfunkprotokollinformationen und speichert Erkennungswarnungen lokal auf dem Gerät. Es sammelt keine persönlichen Informationen, Kommunikationsinhalte oder Standortdaten über das für die Erkennungsalgorithmen notwendige Maß hinaus. Alle Daten bleiben auf deinem Gerät, sofern du keine Remote-Benachrichtigungen aktivierst.

### Fortgeschrittene Fragen

#### Kann ich Rayhunter-Daten auf meinem Computer analysieren?
Ja, **Rayhunter** enthält das Befehlszeilen-Tool `rayhunter-check` zur Analyse aufgezeichneter PCAP- und QMDL-Dateien auf Desktop-Systemen. Fortgeschrittene Nutzer können damit Erkennungsereignisse detailliert untersuchen und verdächtige Aktivitäten mit den Ressourcen eines Computers analysieren.

#### Wie funktioniert Rayhunter in dicht besiedelten Städten?
In dicht besiedelten Gebieten gibt es viele legitime Mobilfunkzellen. Häufige Netzwerkoptimierungen und Wechsel zwischen Basisstationen können dadurch mehr Fehlalarme verursachen. Die Algorithmen von **Rayhunter** unterscheiden normales Netzwerkverhalten von Überwachungsaktivitäten. In dicht besiedelten Gebieten müssen Nutzer möglicherweise die Empfindlichkeit anpassen.

#### Funktioniert Rayhunter auf Auslandsreisen?
Die Wirksamkeit von **Rayhunter** auf Reisen hängt von der Kompatibilität des Geräts mit lokalen Mobilfunkbändern und Roamingvereinbarungen ab. Die Erkennungsalgorithmen funktionieren weltweit. Stelle jedoch sicher, dass dein Gerät die Frequenzbänder am Reiseziel unterstützt. Für den vollen Funktionsumfang ist möglicherweise internationales Roaming erforderlich.

{{< figure src="rayhunter-faq-privacy-protection.webp" alt="Eine Person prüft Rayhunter-Warnungen auf einem Laptop und trägt einen mobilen Hotspot in einer Stadt mit nahegelegenen Mobilfunkmasten" >}}

______

**Rayhunter** ist ein wichtiger Fortschritt beim Schutz persönlicher Daten und bei der Erkennung von Überwachung. Wenn du **Rayhunter** korrekt auf kompatiblen Geräten flashst und konfigurierst, erhältst du wirksame Möglichkeiten, IMSI-Catcher zu erkennen und deine mobile Kommunikation vor unbefugter Überwachung zu schützen.

Ob du Journalist, Aktivist, Sicherheitsfachkraft oder datenschutzbewusst bist: **Rayhunter** bietet Werkzeuge, mit denen du die mobile Sicherheit in einer zunehmend überwachten Welt erhältst. Verifizierte kompatible Geräte findest du bei vertrauenswürdigen Anbietern von Sicherheitsausrüstung, **[Rayhunter kaufen](https://stscollective.com)**.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Kaufe Rayhunter-Geräte und spare 20 %
{{< /centerbutton >}}

## Quellen

- [Offizielles Rayhunter-GitHub-Repository](https://github.com/EFForg/rayhunter)
- [Neueste Rayhunter-Version](https://github.com/EFForg/rayhunter/releases/tag/v0.10.2)
- [Electronic Frontier Foundation](https://www.eff.org/)
- [STS Collective, Anbieter von Rayhunter-Geräten](https://stscollective.com)
