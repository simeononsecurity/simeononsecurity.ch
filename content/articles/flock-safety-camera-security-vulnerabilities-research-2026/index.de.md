---
title: "Schwachstellen in Flock-Safety-Kameras: Über 50 Fehler entdeckt"
date: 2026-05-24
lastmod: 2026-11-15
toc: true
draft: false
description: "Die Untersuchung der Schwachstellen in Flock-Safety-Kameras behandelt offengelegte Zugangsdaten, schwache Schutzmaßnahmen, physischen Zugriff und Grenzen der Offenlegung."
genre: ["Sicherheitsforschung", "Schwachstellenanalyse", "Überwachungstechnologie", "IT-Sicherheit", "Datenschutz", "IoT-Sicherheit", "Physische Sicherheit", "Netzwerksicherheit", "Kritische Infrastruktur", "Behördentechnologie"]
tags: ["Flock-Safety-Schwachstellen", "ALPR-Sicherheit", "Kamerahacking", "IoT-Sicherheitslücken", "Fest kodierte Passwörter", "Android-Things-Schwachstellen", "Angriff mit physischem Zugriff", "Netzwerksicherheit", "Verschlüsselungsfehler", "Datenschutzverletzungen", "CVE-Veröffentlichungen", "Sicherheitsforschung", "GainSec-Forschung", "Ben-Jordan-Ermittlung", "Sicherheit von Überwachungskameras", "Fehler in Behördentechnologie", "Kritische Schwachstellen", "Verantwortungsvolle Offenlegung", "IT-Sicherheitsanalyse", "Technik für Strafverfolgungsbehörden", "Sicherheit der Öffentlichkeit", "WLAN-Zugangspunkt", "Umgehung der Authentifizierung", "Klartext-Zugangsdaten", "HF-Abstrahlung", "TEMPEST-Angriff", "Informationsweitergabe", "Root-Shell-Zugriff", "Remote-Codeausführung", "Sicherheitsaudit", "Schwachstellenbewertung", "Risiko für die nationale Sicherheit", "Untersuchung des Senats", "Bug-Bounty-Programm", "Zero-Day-Schwachstelle", "Exploit-Entwicklung", "Penetrationstest", "Sicherheits-Whitepaper", "Berichterstattung von 404 Media", "Unabhängige Forschung", "Hardwaresicherheit", "Firmwareanalyse", "Systemausnutzung"]
cover: "/img/cover/flock-safety-camera-security-vulnerabilities-research-2026.webp"
coverAlt: "Eine moderne Überwachungskamera mit blauen und grünen Lichtakzenten vor dunklem Hintergrund. Abstrakte Formen und Linien umgeben sie und stehen für digitale Sicherheitslücken."
coverCaption: "Kritische Sicherheitslücken setzen mehr als 80.000 Überwachungskameras unbefugtem Zugriff aus"
canonical: "https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/"
---

**Mehr als 50 kritische Sicherheitslücken gefährden das größte private Überwachungsnetz des Landes**

## Einleitung: Eine Krise der nationalen Sicherheit

Ende 2024 und während des gesamten Jahres 2025 entdeckten unabhängige Sicherheitsforscher möglicherweise **das schwerwiegendste Sicherheitsversagen in der Überwachungstechnik der US-Strafverfolgungsbehörden**. In den Kamerasystemen von Flock Safety wurden **mehr als 50 kritische Schwachstellen** gefunden. Dieselben Kameras fotografieren und verfolgen landesweit täglich mehr als **150 Millionen Fahrzeuge** an über **80.000 Standorten**.

Dieser Artikel analysiert die Schwachstellen umfassend und technisch. Er stützt sich auf:
- **Das formelle GainSec-Whitepaper** „Examining the Security Posture of an Anti-Crime Ecosystem“ (51 Befunde, 22 zugewiesene CVEs, 8 noch offen)
- **Ben Jordans investigative Berichte** und praktische Sicherheitstests
- **Die Berichterstattung von 404 Media** über öffentlich zugängliche Kamerabilder
- **Offizielle Stellungnahmen** von Flock Safety und US-Senatoren
- **Veröffentlichte Einträge** in der National Vulnerability Database (NVD)
- **Das Dateisystemabbild vom September 2026**, veröffentlicht von Distributed Denial of Secrets, mit einer technischen Detailanalyse von Micah Lee sowie einer gemeinsamen Untersuchung von WIRED und 404 Media

Warum es **diese Kameras gibt** und welche **Folgen sie für den Datenschutz haben**, erfährst du in unserem Artikel: **[Flock-Safety-Überwachungskameras: Verbreitung, Datenschutzbedenken und Schutzmaßnahmen](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**

Wie du **diese Kameras erkennst**, beschreibt unser Artikel: **[Flock-You-Erkennungsprojekt: Hardwareleitfaden zur Gegenüberwachung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**

______

## Das Ausmaß des Problems

### Umfang der anfälligen Infrastruktur

Stand Mai 2026:
- **Mehr als 80.000 Flock-Safety-Kameras** in den USA installiert
- **Mehr als 5.000 Städte und Gemeinden** verwenden Flock-Dienste
- **Mehr als 3.500 Strafverfolgungsbehörden** haben Systemzugriff
- **Mehr als 22.000 Nutzer bei Strafverfolgungsbehörden** greifen auf Datenbanken zu
- **Milliarden Datenpunkte** in durchsuchbaren Datenbanken gespeichert

### Zeitverlauf der Schwachstellen

- **Ende 2024**: Der Sicherheitsforscher Jon „GainSec“ Gaines entdeckt erste Schwachstellen
- **Februar 2025**: Die verantwortungsvolle Meldung an Flock Safety beginnt
- **April 2025**: Erste CVE-Zuweisungen werden veröffentlicht
- **November 2025**: Veröffentlichung eines formellen Whitepapers mit 51 Befunden
- **Dezember 2025**: Ben Jordan demonstriert Schwachstellen in einem Video
- **Januar 2026**: 404 Media findet mehr als 60 öffentlich erreichbare Kamerafeeds
- **Februar 2026**: US-Senatoren fordern die FTC zu einer Untersuchung auf
- **Mai 2026**: Das Offenlegungsverfahren läuft weiter

### Kategorien der Schwachstellen

Die über 50 Schwachstellen gehören zu mehreren Kategorien:
1. **Authentifizierung und Autorisierung** (fest kodierte Passwörter, fehlendes MFA)
2. **Kryptografie und Verschlüsselung** (Daten im Ruhezustand und bei der Übertragung unverschlüsselt)
3. **Netzwerksicherheit** (offene WLAN-Zugangspunkte, Zugangsdaten im Klartext)
4. **Physische Sicherheit** (Angriffe über Tastendruck, offene USB-Anschlüsse)
5. **Datenschutz** (unbefugte Datenerfassung, lange Aufbewahrung)
6. **Systemdesign** (veraltete Software, unzureichende Zugriffskontrollen)
7. **Offenlegung von Informationen** (offene API-Schlüssel, öffentliche Kamerafeeds)

______

## Das Dateisystemabbild vom September 2026

**Im September 2026 veröffentlichte die Transparenzorganisation Distributed Denial of Secrets vollständige Dateisystemabbilder einer im Einsatz befindlichen Flock-Kamera.** Eine Gruppe namens **stegan0gram** schraubte die Hardware vom Mast, kopierte den internen Speicher und veröffentlichte die Abbilder. **404 Media** und **WIRED** führten gemeinsam eine Untersuchung durch. Der Sicherheitsforscher **Micah Lee** veröffentlichte eine technische Analyse der Inhalte.

Alle früheren Befunde in diesem Artikel stammten von Laborgeräten oder gekauften Einheiten. Dieser Datensatz stammt von einer Kamera im aktiven kommunalen Einsatz und ist damit der bislang stärkste veröffentlichte Nachweis.

*Die Kamera wurde nicht über das Netzwerk gehackt. Sie wurde physisch abmontiert.*

### Inhalt des Abbilds

Die Veröffentlichung enthält Abbilder von drei Partitionen. Jede zeigt einen anderen Teil des Problems.

| Partition | Größe | Bedeutung |
|-----------|-------|-----------|
| **system** | 1,5 GB | Android-Systemabbild mit **19 von Flock entwickelten Apps**, darunter `flock-sambuca`, `flock-collins` und `flock-phone-home` |
| **persist** | 32 MB | Gerätezugangsdaten unter `flock/auth0/auth0_cred` auf einer **unverschlüsselten Partition, die einen Werksreset übersteht** |
| **media** | 18 GB | Protokolle und Bilder in einem Container, dessen **Entschlüsselungsschlüssel auf derselben Partition gespeichert ist** |

### Das Problem mit den Zugangsdaten ist bestätigt

Das Abbild klärt, ob fest kodierte Zugangsdaten nur theoretisch waren oder auch in der Produktion eingesetzt werden. Sie werden eingesetzt.

**Ein API-Schlüssel für den Zugriff auf das Backend von Flock ist in den App-Binärdateien fest kodiert.** Der Wert befindet sich in einer Klasse namens `CameraSettings` in `com.flocksafety.android.common.lib`. Flock bindet die gemeinsame Bibliothek in alle 19 Apps ein, daher enthält jede den Schlüssel. Die App `flock-sambuca` verwendet ihn während der Bereitstellung.

**Der Authentifizierungsablauf funktioniert so:**

1. Jede Kamera fordert Zugangsdaten von einem Flock-Server an und identifiziert sich über ihre **MAC-Adresse**
2. Flocks **Okta-Auth0**-Anmeldedienst gibt ein kurzlebiges `FlockAuth0Token` zurück
3. Die Kamera speichert die erhaltenen Zugangsdaten **im Klartext**

Die Auth0-Client-ID und das Client-Secret liegen auf der **unverschlüsselten `/persist`-Partition** in einer Datei, die einen Werksreset überstehen soll. Ein Angreifer liest zuerst die persist-Partition aus, weil sie ungeschützt ist.

Das breitere Muster fest kodierter Geheimnisse beschreibt [Kritische Schwachstelle Nr. 4](#critical-vulnerability-4-hardcoded-credentials-throughout-system).

### Der Verschlüsselungsschlüssel liegt neben dem Schloss

Flock erklärt, dass die Kameras durch **Verschlüsselung auf dem Gerät** geschützt seien. Das Abbild zeigt, wie die Umsetzung tatsächlich aussieht.

Die 18-GB-Medienpartition liegt in einem verschlüsselten Container. Der Entschlüsselungsschlüssel befindet sich auf derselben Partition, in einer Datei mit der Endung `.key`. Die Gruppe stegan0gram fand den Schlüssel, entsperrte den Container und las die Inhalte. **Die Bilder sind so verschlüsselt wie eine verschlossene Kiste, deren Schlüssel am Deckel klebt.**

Wiederhergestellte Protokolle enthüllten auch den Standort der Kamera. GPS-Koordinaten erscheinen **155-mal** in den Protokollen und liegen innerhalb von ungefähr 100 Metern, eine normale Abweichung für einen an einem Mast befestigten Empfänger. Die Koordinaten zeigen auf **Wauwatosa, Wisconsin**, einen Vorort von Milwaukee, wo die Kamera an der N Mayfair Road montiert war. Micah Lee verglich die Protokolle mit Google Street View und identifizierte das konkrete Gerät anhand der Seriennummer und MAC-Adresse.

*Verschlüsselung im Ruhezustand hilft nicht, wenn der Schlüssel neben dem Chiffretext liegt.*

### Was Flock sagte

Flocks Stellungnahme wiederholte die Position des Unternehmens zu den früheren GainSec-Befunden. Ein Sprecher erklärte:

> „Flock nimmt Sicherheit ernst und unterhält eine öffentliche Richtlinie zur Offenlegung von Schwachstellen, über die Sicherheitsforscher mögliche Schwachstellen direkt melden können. Wir haben über dieses Verfahren keine Meldung erhalten. Auf Grundlage der begrenzten Informationen verfügen wir nicht über genügend Details, um die Behauptungen zu beurteilen.“

Diese Antwort lässt sich nur schwer mit dem Zeitverlauf vereinbaren. Schwachstellen im Betriebssystem der Kamera wurden **2018 und 2021 öffentlich behoben**. Die Standards für die Speicherung von Zugangsdaten und die Schlüsselverwaltung sind seit langem unverändert, noch bevor die Kamera ausgeliefert wurde. **Für die Prüfung einer zehnjährigen öffentlichen Schwachstellenhistorie ist keine externe Meldung erforderlich.**

Flock bezeichnete außerdem das Entfernen und Analysieren der Kamera als illegal, was nach geltendem Recht zutrifft. Die Sicherheitsbefunde stehen unabhängig davon, wie die Hardware beschafft wurde.

### Warum das wichtiger ist als die frühere Forschung

Das GainSec-Whitepaper dokumentierte 51 Befunde zu legal beschafften Geräten. Flock bestritt deren Schwere und argumentierte, dass physische Nähe erforderlich sei.

Dieses Abbild räumt diese Einwände aus. Eine unveränderte Kamera im Produktionseinsatz enthält Zugangsdaten zur Infrastruktur im Klartext, Schlüssel neben den geschützten Daten und ein Betriebssystem ohne Sicherheitsupdates seit acht Jahren. **Es war kein Exploit nötig. Ein Schraubenschlüssel genügte.**

______

## Die Geräteflotte

Flock verkauft eine Produktlinie statt einer einzelnen Kamera, und die Sicherheitsmerkmale unterscheiden sich je nach Gerät. Die folgenden Angaben stammen aus GainSec-Teardowns und Firmwareanalysen der Erkennungsgemeinschaft bei **[WiFi Mothership](https://wifimothership.com/flock)**.

| Gerät | Aufgabe | Plattform | Betriebssystem |
|--------|---------|-----------|----------------|
| **Falcon** | Solarbetriebene ALPR-Kamera | Qualcomm MSM8953 (Snapdragon 625) / OpenQ 624A SoM | Android 8.1 |
| **Sparrow** | Kabelbetriebene ALPR-Kamera | Wie Falcon | Android 8.1 |
| **Raven** | Audioerkennung von Schüssen und Hilferufen | ESP32-WROOM-32D mit Syntiant-NDP120-B0-DSP | FreeRTOS / ESP-IDF |
| **Bravo** | Edge-AI-Computer | Qualcomm QCS6490 / TurboX QCS6490-U8B | **Android 13, Kernel 5.4.180** |
| **Picard** | Älterer Computer | Durch Bravo ersetzt | |
| **Condor** | PTZ-Kamera | Nicht vollständig dokumentiert | |
| **Alpha** | Autonome Drohne | Von Flock entwickelt, NDAA-konform | Proprietärer Autopilot |
| **Aerodome M350** | Ältere Drohne | DJI Matrice M350 / M300 RTK | DJI-Firmware |
| **LPR-Anhänger (ATS-5)** | Mobile ALPR-Plattform | All-Traffic-Solutions-Fahrgestell mit Flock-Kamera | Wie Falcon |
| **Wing** | Softwarebrücke zu Kameras anderer Anbieter | Keine, bindet vorhandene IP-Kameras ein | |

*Der Generationsunterschied fällt sofort auf. Der Computer läuft mit Android 13, während die Kameras, die er bedient, Android 8.1 verwenden, ein Betriebssystem aus dem Jahr 2017.*

**Falcon ist das Gerät, das besondere Aufmerksamkeit verdient.** Es verarbeitet ALPR, läuft weiterhin mit Android 8.1 und speichert Daten auf **32 GB unverschlüsseltem eMMC-Speicher**. Auf demselben eMMC lagen die Mediendateien und Protokolle, die stegan0gram wiederherstellte. Sparrow verwendet dieselbe Plattform mit Kabelversorgung.

**Bravo ist das Gegenbeispiel.** Ein moderner Computer mit Android 13 und KI-Inferenz für Kamerafeeds zeigt, dass das Unternehmen aktuelle Software einsetzen kann, wenn es das möchte.

## Verifizierte CVE-Kennungen

Fünfzehn CVEs wurden den Gerätefamilien Falcon, Sparrow, Raven und Bravo zugewiesen. Jede Kennung unten wurde im September 2026 im **CVE.org-Register** geprüft und nicht aus einer Sekundärquelle übernommen.

### Schusserkennung und Audiogeräte

| CVE | Befund | CVSS |
|-----|--------|------|
| **CVE-2025-47818** | Fest kodiertes Passwort für eine Verbindung | 2.2 |
| **CVE-2025-47819** | Debug-Schnittstelle auf dem Chip ohne angemessene Zugriffskontrolle | 6.4 |
| **CVE-2025-47820** | Klartextspeicherung von Code | 2.0 |
| **CVE-2025-47821** | Fest kodiertes Passwort für ein System | 2.2 |

Alle vier betreffen Geräte zur Schusserkennung **vor Version 1.3**.

### Kennzeichenerkennung

| CVE | Befund | CVSS |
|-----|--------|------|
| **CVE-2025-47822** | Debug-Schnittstelle auf dem Chip ohne angemessene Zugriffskontrolle | 6.4 |
| **CVE-2025-47823** | Fest kodiertes Passwort für ein System | 2.2 |
| **CVE-2025-47824** | Klartextspeicherung von Code | 2.0 |

Diese drei Schwachstellen betreffen die Firmware der Kennzeichenerkennung **bis einschließlich Version 2.2**.

### Anwendungsfehler in der gesamten Flotte

| CVE | Befund | CVSS |
|-----|--------|------|
| **CVE-2025-59403** | Die Collins-App stellt administrative Endpunkte auf **Port 8080 ohne Authentifizierung** bereit: `/reboot`, `/logs`, `/crashpack` und `/adb/enable`. Der letzte startet ADB über TCP ohne Debugging-Bestätigung. Damit erhält ein Angreifer im selben Netzwerk eine Shell | **9.8 KRITISCH** |
| **CVE-2025-59407** | Die DetectionProcessing-App enthält einen Java-Keystore zusammen mit seinem **fest kodierten Passwort**. Der Keystore enthält einen privaten Schlüssel | **9.8 KRITISCH** |
| **CVE-2025-59405** | Die Peripheral-App enthält einen DataDog-API-Schlüssel im Klartext | 7.5 |
| **CVE-2025-59409** | Die Falcon- und Sparrow-Produktionsfirmware enthält **Entwicklungs-WLAN-Zugangsdaten im Klartext** | 7.5 |
| **CVE-2025-59406** | Die Pisco-App enthält ein **Auth0-Client-Secret im Klartext** | 6.2 |

### Bravo-Computer

| CVE | Befund | CVSS |
|-----|--------|------|
| **CVE-2025-59402** | Akzeptiert den standardmäßigen Thundercomm-TurboX-6490-Firehose-Loader und ermöglicht Firmware-Flashen sowie Partitionsabbilder | 5.4 |
| **CVE-2025-59404** | Wird mit entsperrtem Bootloader ausgeliefert und umgeht Android Verified Boot | 7.5 |
| **CVE-2025-59408** | Wird mit deaktiviertem Secure Boot ausgeliefert | 7.3 |

**Vier dieser Schwachstellen haben einen Netzwerk-Angriffsvektor und eine Bewertung von mindestens 7,5. Sie erfordern keinen physischen Zugriff.** CVE-2025-59403 bezeichnet den zugewiesenen Identifikator für den nicht authentifizierten API-Pfad. Er umfasst den Aufruf `/adb/enable`, auf dem [Kritische Schwachstelle Nr. 1](#critical-vulnerability-1-button-press-wireless-access-point) für den Zugriff auf eine Root-Shell beruht.

*Die CVE-Einträge sind noch aus einem zweiten Grund wichtig. Sie bestätigen das Klartextproblem durch unabhängige Register. Außerdem wird Flocks eigene Sicherheitswarnungsseite bei den Raven- und LPR-Einträgen als Quelle aufgeführt.*

______

## Kritische Schwachstelle Nr. 1: WLAN-Zugangspunkt per Tastendruck {#critical-vulnerability-1-button-press-wireless-access-point}

### CVE-2025-59403

**Schweregrad**: KRITISCH (CVSS 9.8)

### Der Exploit

Die alarmierendste Schwachstelle ermöglicht es **jeder Person mit physischem Zugriff** auf eine Flock-Safety-Kamera, innerhalb von weniger als 60 Sekunden die vollständige Kontrolle zu übernehmen:

**Schritt 1**: Drücke **dreimal** die Taste auf der Rückseite der Falcon-/Sparrow-Kamera
**Schritt 2**: Das Gerät erstellt einen offenen WLAN-Zugangspunkt
**Schritt 3**: Verbinde dich mit dem WLAN (das fest kodierte Passwort ist im GainSec-Whitepaper dokumentiert)
**Schritt 4**: Sende den Befehl zum Aktivieren von ADB (Android Debug Bridge)
**Schritt 5**: Stelle über ADB eine Verbindung her und erhalte Root-Shell-Zugriff

### Technische Details

```
Gerät: Flock-Safety-ALPR-Kamera Falcon/Sparrow
Hardware: Android Things 8.0/8.1 (Supportende 2021)
Angriffsvektor: Abfolge physischer Tastendrücke
Authentifizierung: fest codiertes WiFi-Passwort (auf allen Geräten gleich)
Auswirkung: vollständige Übernahme des Geräts, Datenabfluss und Installation von Schadsoftware
```

### Was damit möglich wird

Mit Shell-Zugriff kann ein Angreifer:
- **Alle gespeicherten Bilder auslesen** (auch von Personen, nicht nur Fahrzeugen)
- **Auf dem Gerät gespeicherte Beweise verändern oder löschen**
- **Dauerhafte Malware installieren** (übersteht Neustarts)
- Die **Geräteidentität klonen**, um sie vorzutäuschen
- Videostreams **abfangen und verändern**
- Das Gerät als **Botnet-Client** für DDoS-Angriffe nutzen
- **WLAN-Zugangsdaten in der Nähe erfassen** (Honeypot-Angriffe)
- Die Kamera **deaktivieren** oder einen Denial-of-Service auslösen

### Demonstration

Der Sicherheitsforscher Ben Jordan führte den Angriff auf YouTube vor. Er zeigte:
- Verbindung mit dem WLAN-Zugangspunkt in **unter 30 Sekunden**
- Root-Shell-Zugriff in **insgesamt weniger als 60 Sekunden**
- Vollständigen Zugriff auf Dateisystem, gespeicherte Bilder und Systemspeicher
- Installation beliebiger Android-Apps

**Zitat aus der Demonstration**:
> „Das Passwort für diesen Zugangspunkt ist [REDACTED], komplett in Kleinbuchstaben. Jede Kamera, die wir getestet haben, hat dasselbe fest kodierte Passwort. Dann sendest du einen Befehl zum Aktivieren von ADB ... in weniger als 30 Sekunden erhältst du wahrscheinlich eine vollständige Shell und uneingeschränkten Zugriff auf das Gerät.“

### Reaktion des Anbieters

Flock Safety behauptete zunächst, die Schwachstelle beträfe nur **nicht mit der Cloud verbundene Geräte**, und verglich sie mit **„einem Lkw, aus dem ein iPhone gestohlen wurde, bevor es verbunden war“**.

*Diese Behauptung wurde widerlegt.* Forscher reproduzierten die Schwachstelle **auf mit der Cloud verbundenen Geräten**, bei mehreren Kameramodellen mit **identischer Schwachstelle** und bei Geräten aus **verschiedenen Quellen**. Alle wiesen denselben Fehler auf.

______

## Kritische Schwachstelle Nr. 2: Veraltetes Android-Betriebssystem

### CVE-2025-47822 bis CVE-2025-47824

**Schweregrad**: MITTEL bis NIEDRIG (CVSS 6.4, 2.2 und 2.0)

### Das Problem

Flock-Safety-Kameras verwenden **Android Things 8.0 oder 8.1**. Dieses Betriebssystem:
- Wurde von Google **2021 eingestellt**
- Erhält **seit 2021 keine Sicherheitsupdates**
- Verzeichnet **mehr als 900 veröffentlichte Schwachstellen** (Stand 2026)
- Ist **seit über fünf Jahren ohne Support**

### Technische Analyse

**Betriebssystem**: Android Things 8.0/8.1
**Supportende**: Januar 2021
**Bekannte Schwachstellen**: Über 900
**Sicherheitspatches**: Keine seit dem Supportende
**Betroffene Geräte**: Falcon, Sparrow, Condor und Bravo-Computer

### Was das Dateisystemabbild vom September 2026 zeigt

Die im September 2026 veröffentlichten Dateisystemabbilder zeigen genaue Versionsstände einer Kamera im aktiven Einsatz und nicht eines Laborgeräts.

| Komponente | Version auf der Kamera | Zustand |
|-----------|------------------------|--------|
| **Android** | 8.1, Build vom 5. Juni 2025 | Sicherheitspatch-Level **2018-06-05** |
| **Linux-Kernel** | 3.18.71 | 2017 veröffentlicht; die Reihe 3.18 endete im Mai 2019 bei Version 3.18.140 |
| **Aktuelle Android-Version** | Android 17, Juni 2026 | Neun Hauptversionen neuer |

Der Kamera-Build selbst ist neu. **Das darunterliegende Betriebssystem ist es nicht**. Das Patch-Level zeigt, dass das Gerät seit **acht Jahren** keine Android-Sicherheitsupdates erhalten hat. Dem Kernel fehlen **69 Patchversionen** gegenüber dem Ende seines eigenen Wartungszweigs, also mehr als neun Jahre an Korrekturen.

### Zwei Schwachstellen in diesem Build

Micah Lee identifizierte zwei öffentlich bekannte Fehler in Komponenten der Kamera. Die Patchdaten belegen, dass die Firmware vor allen Korrekturen erstellt wurde.

| CVE | Komponente | Auswirkung | Gepatcht |
|-----|-----------|------------|---------|
| **CVE-2021-1905** | Qualcomm-Adreno-GPU-Treiber | Ein Use-after-free ermöglicht **jedem Code auf dem Gerät, auch Apps ohne Berechtigungen, den Kernel-Speicher zu beschädigen und die volle Kontrolle zu übernehmen** | Mai 2021 |
| **CVE-2018-9568** „WrongZone“ | Socket-Verarbeitung im Linux-Kernel | Type Confusion über IPv6 ermöglicht einem Programm, **seine Rechte auf Root zu erhöhen**. Öffentlicher Exploit-Code ist verfügbar | Dezember 2018 |

Beide Schwachstellen wurden Jahre vor dem Bau der Kamera-Firmware behoben. **Keine erfordert physischen Zugriff, da sie durch Software auf dem Gerät erreichbar sind.** Der Nähe-Einwand, mit dem Flock die GainSec-Befunde herunterspielte, gilt für keine der beiden.

### Vergleich mit Verbrauchergeräten

Zum Vergleich:
- **Smartphones** erhalten nach etwa fünf Jahren oft keine Updates mehr, und Hersteller **nehmen sie aus dem Verkauf**
- Eine **Heimüberwachungskamera** mit fünf Jahre alter Software gälte als **kritisch unsicher**
- Behörden verlangen bei sensiblen Systemen **aktuelle, unterstützte Software**

*Dennoch setzt Flock Safety weiterhin Kameras mit nicht unterstützter Software ein und verkauft sie. Sie erhalten keine Sicherheitsupdates, enthalten Hunderte bekannter Exploits und verarbeiten sensible Daten der Strafverfolgung.*

### Warum das wichtig ist

Der Einsatz von **Software ohne Support** in Überwachungsgeräten bedeutet:
- **Jede veröffentlichte Android-8.x-Schwachstelle** funktioniert auf diesen Kameras
- Für viele Schwachstellen ist **Exploit-Code öffentlich verfügbar**
- Neu entdeckte Probleme lassen sich **niemals durch Patches beheben**
- Die Einhaltung von Vorschriften (**FISMA, NIST, CMMC**) ist unmöglich

______

## Kritische Schwachstelle Nr. 3: Fehlende Verschlüsselung zur Laufzeit

### CVE-2025-47824 und CVE-2025-59407

**Schweregrad**: HOCH bis KRITISCH (CVSS 2.0 bis 9.8)

### Flocks Aussagen und die Realität

**Auf der Flock-Safety-Website steht**:
> „Daten und Aufnahmen sind über ihren gesamten Lebenszyklus verschlüsselt.“

**Ergebnisse unabhängiger Forschung** (GainSec und Ben Jordan):
> „Bei unserer gesamten Forschung haben wir nichts entschlüsselt oder geknackt. Alles lag zur Laufzeit unverschlüsselt vor.“

*Die Lücke zwischen der Werbeaussage und der technischen Realität ist vollständig.*

### Welche Daten unverschlüsselt sind

Bei der Untersuchung der Geräte fanden Forscher folgende **unverschlüsselte** Daten:
1. **Gespeicherte Videoaufnahmen und Bilder**
2. **Kennzeichendaten und Metadaten**
3. **WLAN-Zugangsdaten und API-Schlüssel**
4. **Datenbankdateien mit Erkennungsprotokollen**
5. **Netzwerkverkehr** (siehe Schwachstelle Nr. 6)
6. **Systemprotokolle mit sensiblen Informationen**

### Widerspruch bei der Datenspeicherung

**Aussage von Flock Safety**: Daten werden nach sieben Tagen automatisch entfernt
**Befund der Forschung**: Bilder stammten noch aus der **Herstellung des Geräts** (Monate oder Jahre alt)

Auszug aus dem GainSec-Whitepaper:
> „Wir fanden Bilder, die älter als sieben Tage waren. Gespeicherte Bilder waren entstanden, als die Kamera bei der Herstellung im Werk ausgelöst wurde.“

*Das bedeutet, dass die angegebenen Datenschutzrichtlinien auf dem Gerät nicht durchgesetzt werden.*

### Folgen für den Datenschutz

Die fehlende Verschlüsselung bedeutet:
- **Physischer Diebstahl des Geräts** führt sofort zu einem Datenleck
- **Abfangen des Netzwerks** legt Klartextdaten offen
- **Insider** können Daten leicht abschöpfen
- Der **Schutz durch richterliche Anordnung** gilt möglicherweise nicht für unverschlüsselte Daten
- **Verstöße gegen zahlreiche Vorschriften** sind möglich (HIPAA, CCPA usw.)

______

## Kritische Schwachstelle Nr. 4: Fest kodierte Zugangsdaten im gesamten System {#critical-vulnerability-4-hardcoded-credentials-throughout-system}

### CVE-2025-47818, CVE-2025-47821, CVE-2025-47823, CVE-2025-59407 und CVE-2025-59409

**Schweregrad**: KRITISCH (CVSS bis 9.8)

### Kategorien fest kodierter Geheimnisse

Sicherheitsforscher fanden **zahlreiche fest kodierte Zugangsdaten**:

#### 1. Passwörter für WLAN-Zugangspunkte
- **Ein universelles Passwort** für alle Falcon-/Sparrow-Kameras
- **Nutzer und Administratoren können es nicht ändern**
- Forschern **bekannt und im Whitepaper veröffentlicht** (mit geschwärzten Abschnitten)
- **Durch CVE-2025-59409 bestätigt**: Falcon- und Sparrow-Produktionsfirmware (Build `OPM1.171019.026`) enthält **Entwicklungs-WLAN-Zugangsdaten im Klartext**

#### 2. API-Schlüssel und Tokens
- **Fest in Firmware und Anwendungscode hinterlegt**
- **Gewähren Backend-Zugriff** auf verschiedene Dienste
- Durch **Reverse Engineering von Android-APKs gefunden**
- **Durch das Dateisystemabbild vom September 2026 bestätigt**: Ein Backend-API-Schlüssel liegt fest in `CameraSettings` in `com.flocksafety.android.common.lib`, einer gemeinsamen Bibliothek, die allen **19 Flock-Apps** auf dem Gerät hinzugefügt wird
- **Auth0-Client-ID und -Secret liegen auf der unverschlüsselten `/persist`-Partition** unter `flock/auth0/auth0_cred`, einem Speicherort, der einen Werksreset übersteht
- **Zurückgegebene Zugangsdaten werden im Klartext gespeichert**, nachdem sich die Kamera mit ihrer MAC-Adresse beim Okta-Auth0-Dienst von Flock authentifiziert hat

#### 3. Datenbankzugangsdaten
- **SQLite-Datenbanken** ohne Passwortschutz
- **MySQL-/PostgreSQL-Zugangsdaten** in Konfigurationsdateien
- **Direkter Datenbankzugriff** über eine lokale Shell

#### 4. Kryptografische Keystores
- **Durch CVE-2025-59407 bestätigt**: Die DetectionProcessing-App bündelt einen Java-Keystore mit dem fest kodierten Passwort. Der Keystore enthält einen **privaten Schlüssel**
- **Schweregrad**: KRITISCH (CVSS 9.8), weil das Schlüsselmaterial zusammen mit der Binärdatei ausgeliefert wird, die es schützen soll

#### 5. WLAN-Netzwerknamen
- Liste bevorzugter Netze **fest in der Firmware hinterlegt**
- Ermöglicht Angriffe über **gefälschte Zugangspunkte** (siehe Schwachstelle Nr. 6)

#### 6. Zugangsdaten für Cloud-Dienste
- **AWS-/Azure-Tokens** im Code eingebettet
- **API-Schlüssel für Drittanbieter** (ArcGIS, Kartendienste)
- **OAuth-Tokens**, die nie erneuert werden

### Angriffsszenario: Gefälschtes Netzwerk

Mit fest kodierten WLAN-Netzwerknamen demonstrierten Forscher folgenden Angriff:

1. Der Angreifer richtet ein **gefälschtes WLAN mit derselben fest kodierten SSID** ein
2. Die Kamera **verbindet sich automatisch** und bevorzugt fest kodierte Netze
3. Der Angreifer fängt **den gesamten Netzwerkverkehr** als Man-in-the-Middle ab
4. Zugangsdaten werden im Klartext aus dem Datenverkehr ausgelesen
5. Der Angreifer erhält **Zugriff auf Backend-Systeme**

**Kein physischer Zugriff auf die Kamera erforderlich.** WLAN-Reichweite genügt.

______

{{< figure src="flock-safety-hardcoded-credentials-attack-vectors-diagram.webp" alt="Diagramm mit fünf Angriffswegen über fest kodierte Zugangsdaten in Flock-Safety-Kameras: WLAN-Passwörter, API-Schlüssel, Datenbankzugänge und Cloud-Tokens" >}}

______

## Kritische Schwachstelle Nr. 5: Keine Mehr-Faktor-Authentifizierung

### Versagen der Organisationsrichtlinien

**Schweregrad**: HOCH (organisatorisch)

### Die Enthüllung

**Flock Safety verlangt bei einigen Strafverfolgungsbehörden keine 2FA/MFA**. *Dieselben Behörden greifen täglich auf Standortdaten von 150 Millionen Fahrzeugen zu.*

Zitat eines Sicherheitsforschers:
> „Als ich davon erfuhr, konnte ich es kaum glauben. Der Sicherheitsprozess bei der Anmeldung bei Disney Plus ist manchen Polizeibehörden schon zu viel, wenn sie vertrauliche Informationen und die Standorte von praktisch jedem abrufen.“

### Warum das wichtig ist

Ohne MFA/2FA gilt:
- **Ein einziges gestohlenes Passwort** gewährt vollen Systemzugriff
- **Phishing-Angriffe** sind sehr effektiv
- **Credential Stuffing** mit Daten aus anderen Sicherheitsverletzungen funktioniert
- **Insider-Bedrohungen** lassen sich leichter umsetzen
- **Gestohlene Geräte** verschaffen sofortigen Zugriff

### Vergleich

Sicherheitsanforderungen für **weniger sensible** Systeme:
- **Disney+**: 2FA verfügbar
- **Gmail**: 2FA bei neuen Konten standardmäßig aktiviert
- **Banken**: 2FA gesetzlich vorgeschrieben
- **Soziale Medien**: 2FA ist Standard

Sicherheitsanforderungen für **täglich über 150 Millionen Fahrzeugabfragen**:
- **Flock Safety**: 2FA optional (einige Behörden verwenden sie nicht)

### Stellungnahme eines US-Senators

Dieser Befund wurde besonders im **Schreiben von Senator Wyden** hervorgehoben, der eine FTC-Untersuchung beantragte. Darin hieß es, Flock Safety habe:
> „die sensiblen persönlichen Daten von Amerikanern unnötig dem Diebstahl durch Hacker und ausländische Spione ausgesetzt“

### Einfache Lösung

**USB-/NFC-Sicherheitsschlüssel** kosten **10 bis 25 US-Dollar** und bieten:
- **Phishing-resistente** Authentifizierung
- **Keine zusätzlichen Apps** oder Codes erforderlich
- Konformität mit **FIDO2/WebAuthn**
- **Einfache Bedienung** (einstecken oder antippen)

*Wenn das für Strafverfolgungsbeamte „zu umständlich“ ist, **sollten sie keinen Zugriff** auf nationale Überwachungssysteme erhalten.*

______

## Kritische Schwachstelle Nr. 6: Netzwerkverkehr im Klartext

### Zuweisung einer Kennung steht aus

**Schweregrad**: HOCH (von Forschern auf CVSS 7.8 geschätzt)

**Für diese Kategorie wurde keine CVE-Kennung vergeben.** Der ähnlichste zugewiesene Eintrag, CVE-2025-59406, enthält die CWE-319-Klassifizierung für Klartextübertragung, betrifft jedoch ein eingebettetes Auth0-Secret und nicht das Abfangen von Daten während der Übertragung. Die Befunde in diesem Abschnitt beruhen weiterhin auf den oben genannten Forschungsberichten.

### Die Schwachstelle

Wenn Kameras eine Verbindung zu Netzwerken (LTE oder WLAN) herstellen, übertragen sie Daten **ohne ausreichende Verschlüsselung**:

**Betroffener Datenverkehr**:
- Kennzeichenbilder und -texte
- Erkennungsmetadaten
- Systemprotokolle
- Konfigurationsdaten
- Zugangsdaten (in manchen Fällen)

### Angriffsweg Nr. 1: Gefälschtes WLAN

Forscher demonstrierten:
1. SIM-Karte aus der Kamera entfernen **oder** ein gefälschtes Netz mit der fest kodierten SSID einrichten
2. Kamera verbindet sich mit dem gefälschten WLAN
3. Datenverkehr mit **Wireshark** oder einem ähnlichen Paketanalysator erfassen
4. Mit Tools wie **NetworkMiner** oder **Unblo** analysieren
5. **Zugangsdaten im Klartext** und sensible Daten auslesen

Zitat aus der GainSec-Forschung:
> „Ich habe eine Weile die von einer dieser Kameras übertragenen pcap-Daten aufgezeichnet und mit Wireshark und Unblo analysiert ... und tatsächlich waren Zugangsdaten im Klartext enthalten.“

### Angriffsweg Nr. 2: IMSI-Catcher / Stingray

Ein ausgefeilterer Angriff erfordert keine physische Nähe:
1. **IMSI-Catcher** (selbst gebautes Stingray-Gerät) oder professionellen SDR verwenden
2. **LTE-Verbindung kapern**, indem ein Mobilfunkmast vorgetäuscht wird
3. Kamera verbindet sich mit einer **gefälschten Basisstation**
4. Den gesamten Datenverkehr als **Man-in-the-Middle** abfangen
5. Zugangsdaten, Bilder und Metadaten auslesen

**Physischer Zugriff ist nicht erforderlich.** Der Angriff funktioniert aus **mehreren hundert Fuß** Entfernung.

### Potenzial moderner Tempest-Angriffe

Die Klartextübertragung ermöglicht auch **Tempest-ähnliche Angriffe**, bei denen:
- HF-Abstrahlungen der Kamera erfasst werden können
- Der Videostream **aus der Ferne rekonstruiert** werden kann
- Die Methode an **CIA-Techniken aus dem Kalten Krieg** erinnert
- Moderne SDR-Geräte dies **für Hobbyanwender zugänglich** machen

______

## Kritische Schwachstelle Nr. 7: Öffentlich zugängliche Kamerafeeds

### Entdeckung im Januar 2026

**Schweregrad**: KRITISCH (CVSS 10.0 – vollständige Systemoffenlegung)

### Die Entdeckung

Im Januar 2026 stellten Ben Jordan und **404 Media** fest, dass sich mit **einfachen Google-Suchen** Folgendes finden ließ:
- **Mehr als 60 vollständig offengelegte Verwaltungsoberflächen** von Flock-Safety-Kameras
- **Keine Anmeldung mit Benutzername oder Passwort erforderlich**
- **Live-Videostreams** und 30 Tage archivierte Aufnahmen
- Zugriff auf das Bedienfeld zur **vollständigen Kamerasteuerung**

### Was zugänglich war

Über diese offengelegten Oberflächen konnte jeder:
- **Live-Feeds ansehen**
- **30 Tage archivierte Aufnahmen** prüfen
- **Videodateien herunterladen**
- **PTZ-Kameras** (Schwenken/Neigen/Zoomen) von Condor steuern
- **Dateipfade und Hashes** von Beweismitteln sehen
- Beweismittel mit einem Klick **löschen**
- **Kameraeinstellungen ändern**
- **Seriennummern und Standorte der Geräte anzeigen**

### Beobachtete Datenschutzverletzungen

Ben Jordan dokumentierte Aufnahmen von:
- **Einer Familie, die ein Kleinkind ins Auto setzte** auf einem Lowe’s-Parkplatz
- **Einem Mann, der morgens sein Haus verließ** in New York
- **Einer allein joggenden Frau** auf einem Waldweg in Georgia
- **Einem streitenden Paar** auf einem Straßenmarkt in Atlanta (die KI zoomte automatisch auf Gesichter)
- **Einem Polizisten und einem Krankenwagen**, die während einer psychischen Krise in Iowa halfen
- **Kindern beim Spielen** auf einem Spielplatz in der San Francisco Bay Area
- **Einem Mann auf einer Schaukel** in einem leeren Park, in einem privaten Moment

Zitat von Ben Jordan:
> „Schon beim lauten Aussprechen wird mir übel. Ich versuche, euch nur einen Bruchteil der Informationen zu zeigen, die jeder Mensch mit Zugang zu einer kommerziellen Suchmaschine über alle Personen finden konnte, die in den vergangenen 31 Tagen auf diesem Markt waren oder auf diesem Weg spazierten.“

### Verfolgungsfunktionen

Die offengelegten Condor-PTZ-Kameras verfügen über **KI-gestützte Verfolgung**:
- **Zoomen automatisch auf Personen**
- **Verfolgen Personen** bei Bewegungen
- **Erkennen und fokussieren Smartphones** (um Bildschirme zu lesen)
- **Verfolgen mehrere Ziele gleichzeitig**
- **Zeichnen ununterbrochen auf**, ohne Aufsicht

### Doxxing-Potenzial

Ben Jordan zeigte, wie leicht sich Personen anhand offengelegter Aufnahmen identifizieren lassen:
> „Mit zwei Minuten Open-Source-Aufklärung über eine kommerzielle Gesichtserkennungsplattform fand ich heraus, dass eine Person gerade ihr Medizinstudium abgeschlossen hatte und die andere an chronischem Reizdarmsyndrom litt. Das Paar hatte im vergangenen Jahr ein Kind bekommen ... Außerdem wusste ich, dass die beiden mehr als 45 Minuten von ihrer Adresse in einem Vorort gefahren waren.“

Durch Abgleich mit:
- **Gesichtserkennungsdiensten**
- Profilen in **sozialen Medien**
- Datenbanken mit **öffentlichen Registern**
- Informationen aus **Datenlecks** (etwa Park Mobile)
- **Notrufprotokollen** (viele Städte veröffentlichen diese)

Ergebnis: **vollständige Deanonymisierung innerhalb weniger Minuten**

______

{{< figure src="flock-exposed-camera-feed-ptz-ai-tracking-privacy-violation-overview.webp" alt="Übersicht, wie offene Flock-Safety-PTZ-Kameras mit KI-Tracking öffentlichen Zugriff auf Livebilder von Menschen in Parks, auf Wegen und Parkplätzen ermöglichten" >}}

______

## Kritische Schwachstelle Nr. 8: Unbefugte Datenerfassung

### Widerspruch zu öffentlichen Aussagen

**Schweregrad**: HOCH (Datenschutz und rechtliche Folgen)

### Flocks Aussagen

**Aussage auf der offiziellen Website**:
> „Flock Safety erfasst oder speichert keine Daten über Personen, sondern nur über Fahrzeuge.“

### Befunde unabhängiger Forscher

**Was die Kameras tatsächlich tun**:
1. **Bewegungserkennung** löst die Kamera **bei jeder Bewegung** aus, nicht nur bei Fahrzeugen
2. Die **KI sucht im Bild nach einem Kennzeichen**
3. **Wird kein Kennzeichen gefunden**, wird das Bild **trotzdem gespeichert** und nicht gelöscht
4. **Ein separater Ordner** speichert Bilder ohne Kennzeichen
5. Bilder von **Personen, Fußgängern und Radfahrern** werden aufgenommen und behalten

*Die Aussage „nur Fahrzeuge“ ist falsch. Die Kamera speichert Bilder von jedem, der an ihr vorbeigeht.*

### Verifizierte Beobachtungen

Forscher dokumentierten Kameras, die Folgendes erfassten:
- **Eine Person, die vor der Kamera vorbeiging** (gespeichertes Bild)
- **Eine winkende Hand** vor dem Objektiv (gespeichertes Bild)
- **Einen Tisch oder Gegenstand, der in der Nähe der Kamera bewegt wurde** (gespeichertes Bild)
- **Fabrikarbeiter** am Produktionsstandort (monatelang gespeichert)

Zitat von GainSec:
> „Als ich vor die Kamera trat, löste das Radarmodul die Kamerakomponente aus, um ein Bild von mir aufzunehmen. Danach suchte die KI an Bord nach einem Kennzeichen, fand keines, speicherte das Bild aber trotzdem in einem separaten Ordner.“

### Rechtliche Folgen

Diese unbefugte Datenerfassung könnte:
- **Angegebene Datenschutzrichtlinien verletzen** (irreführende Praktiken)
- **Beschaffungsverträge brechen** (wenn Städte „nur Fahrzeuge“ verlangten)
- **GDPR-/CCPA-Verstöße auslösen** (EU-Bürger, Einwohner Kaliforniens)
- **Einwilligungsvereinbarungen ungültig machen**
- Das Unternehmen wegen falscher Werbung **Klagen aussetzen**

### Ausweitung der Überwachung

Die **Condor-PTZ-Kameras** (2025–2026 installiert) wurden **ausdrücklich zur Verfolgung von Personen entwickelt**:
- **KI-gestützte Personenerkennung**
- **Automatisches Zoomen** auf Gesichter
- **Verfolgen von Personen** bei Bewegung
- **Keine Widerspruchsmöglichkeit**
- Häufiger Einsatz in **Parks, auf Wegen und an Verkehrsstationen**

*Damit wird der Einsatz von Kennzeichenlesern auf eine allgemeine Bevölkerungsüberwachung ausgeweitet, ohne Richtlinien zu ändern, neue Verträge abzuschließen oder die Öffentlichkeit zu informieren.*

______

## Kritische Schwachstelle Nr. 9: Offene USB-Anschlüsse für Rubber-Ducky-Angriffe

### Ausnutzung physischen Zugriffs

**Schweregrad**: HOCH (bei physischem Zugriff)

### Die Schwachstelle

**Bravo-Computer** und einige Kameramodelle besitzen:
- **Offene USB-C-Anschlüsse** an der Außenseite
- **Keine physische Sicherung** (Gehäuseplomben)
- **Automatische Ausführung** von USB-Geräten
- **Keine erforderliche Authentifizierung**

### Rubber-Ducky-/BadUSB-Angriff

Ein **BadUSB-Gerät** (Kosten: 5 bis 15 US-Dollar):
- Gibt sich gegenüber dem System als **USB-Tastatur** aus
- **Führt vorprogrammierte Skripte** (Payloads) aus
- Startet **automatisch** beim Einstecken
- **Benötigt keine Benutzeraktion**

### Angriffsszenario

GainSec demonstrierte:
1. Sich einem installierten Flock-Gerät nähern
2. Ein **BadUSB-Gerät** in den offenen Anschluss stecken
3. Das Gerät führt die Payload (das Skript) aus
4. Die Payload installiert **dauerhafte Malware**
5. Der Angreifer **geht weg**
6. Die Malware **meldet sich über LTE/WLAN beim Server**

**Gesamtdauer**: unter 30 Sekunden

### Was Payloads tun können

Automatisierte Skripte können:
- Einen drahtlosen Zugangspunkt **aktivieren** (ohne Tastendruckfolge)
- Eine **Hintertür für Fernzugriff installieren**
- Daten an einen entfernten Server **ausleiten**
- Aufnahmen oder Beweismittel **verändern**
- Die Kamera **deaktivieren** oder einen DoS-Angriff auslösen
- Das Gerät für DDoS-Angriffe einem **Botnetz hinzufügen**
- Zugangsdaten anderer Systeme **erfassen**

### Warum das wichtig ist

Bei **mehr als 80.000 Kameras**, die oft an **halbländlichen Standorten** mit **eingeschränkter Sicht** stehen:
- Ist **physischer Zugriff** relativ einfach
- Gibt es **keine Wachposten** oder ständige Überwachung
- Sind die Geräte mit **einfachen Schlauchschellen** befestigt
- Hängen sie häufig **etwa 2,1 Meter über dem Boden** (mit einem Tritt erreichbar)

Zitat von Ben Jordan:
> „Diese Kameras sind keine uneinnehmbaren Festungen. Es sind Android-Kameras und Computerboxen aus Kunststoff, die mit Schlauchschellen etwa 2,1 Meter über dem Boden befestigt sind.“

______

{{< figure src="badusb-rubber-ducky-flock-camera-usb-exploit-attack-chain.webp" alt="Angriffskette: Ein BadUSB-Gerät wird an einen offenen USB-Anschluss einer Flock-Safety-Kamera gesteckt und installiert in weniger als 30 Sekunden dauerhafte Malware" >}}

______

## Kritische Schwachstelle Nr. 10: Öffentlich offengelegte API-Schlüssel

### Entdeckung durch einen OSINT-Forscher

**Schweregrad**: KRITISCH (CVSS 9.5)

### Die Entdeckung

2025 fand der **OSINT-Forscher Joshua Michael**:
- Eine über Google-Dorking auffindbare **offene Flock-Safety-Demowebsite**
- **5.000 Zeilen sichtbaren Quellcode**
- Einen **aktiven API-Schlüssel** im Code
- Zugriff auf **mehr als 50 private Geodaten-Layer**

### Welche Zugriffe der API-Schlüssel ermöglichte

Der offengelegte **ArcGIS-API-Schlüssel** gab Zugriff auf:

**1. Registrierungsdaten**
- Kundennamen
- E-Mail-Adressen
- Kamerazahl an jedem Standort
- Möglichkeit, Dateien anzuhängen

**2. Live-Standorte von Streifenwagen** (mehrere Polizeibehörden)
- GPS-Ortung von Polizeifahrzeugen in Echtzeit
- Installationen in Aurora, Colorado
- Carrollton Police Department
- **Risiko für die nationale Sicherheit**

**3. Persönliche Informationen von Beamten**
- Namen und Telefonnummern
- E-Mail-Adressen
- Geplante Streifengebiete
- Zuständige Behördenbezirke

**4. Datenbank mit Fahndungslistenwarnungen** (Dallas, Texas)
- **6.000 Datensätze** markierter Fahrzeuge
- Kennzeichen und Gründe für die Markierung
- Erkennungsorte und Zeitstempel
- IDs der Kameras, die Fahrzeuge erfassten
- **Fünf Monate Bewegungsverfolgung**

Zitat von Joshua Michael:
> „Jeder konnte diese Karte bei Google finden und die Bewegungsmuster dieser Personen fünf Monate lang verfolgen. Außerdem ist als Grund bei einer Person nur ‚verdächtig‘ eingetragen, und viele andere haben gar keinen Grund oder ein leeres Feld.“

### Angriffsfläche

Offengelegte API-Schlüssel ermöglichen:
- **Gezieltes Verfolgen bestimmter Fahrzeuge**
- Gefährdung der **Sicherheit von Beamten** (Wohnadressen, Streifenmuster)
- Verletzung der **operativen Sicherheit** (wo Polizei ist oder nicht ist)
- **Einschüchterung von Zeugen** (Verfolgung von Personen, die Straftaten meldeten)
- Sammlung kriminalitätsbezogener Informationen durch **organisierte Kriminalität**

### Kontext des Sicherheitsvorfalls: Flax Typhoon

Nur wenige Wochen vor dieser Entdeckung kompromittierte die **vom chinesischen Staat unterstützte** Hackergruppe **Flax Typhoon** ArcGIS, so die Sicherheitsforscher Alexa Feminina und James Zhang.

Zitat aus dem InfoSecurity Magazine:
> „Die Hacker sollen eine legitime, öffentlich zugängliche ArcGIS-Anwendung angegriffen haben ... die für Katastrophenhilfe, Notfallmanagement und andere kritische Funktionen genutzt wird.“

**Das bedeutet, dass feindliche Staaten möglicherweise auf** Standorte von Streifenwagen, Identitäten von Beamten, Positionen von Überwachungskameras und Notfallmaßnahmen zugreifen konnten.

______

## Weitere Schwachstellen (Zusammenfassung der über 50 Fehler)

### Schwachstellen 11 bis 51

Das GainSec-Whitepaper dokumentiert **41 weitere Befunde**, darunter:

**Fehler im Systemdesign**:
- Debug-Modus in Produktionsfirmware aktiviert
- Unsicherer Startvorgang ermöglicht Übernahme des Bootloaders
- Kein Secure Element oder TPM zur Schlüsselaufbewahrung
- Vorhersehbarer Firmware-Update-Mechanismus

**Authentifizierungsprobleme**:
- Sitzungstokens laufen nie ab
- Keine IP-basierten Zugriffsbeschränkungen
- Gemeinsame Zugangsdaten für die Geräteflotte
- Kein Zertifikats-Pinning

**Netzwerksicherheit**:
- Offene Ports mit Debugdiensten
- Telnet auf manchen Geräten aktiviert
- FTP-Server mit schwachen Zugangsdaten
- DNS-Rebinding-Schwachstellen

**Datenschutz und Aufbewahrung**:
- Bilder länger als angegeben gespeichert
- Metadaten nie gelöscht
- Gesichtserkennungsdaten erfasst
- Standortverfolgung auch abseits von Fahrzeugen

**Physische Sicherheit**:
- Gehäuse leicht zu zerlegen
- Serielle Schnittstellen offengelegt
- JTAG-Debugging-Ports zugänglich
- Keine manipulationssicheren Siegel

**Kryptografische Fehler**:
- Schwache Zufallszahlenerzeugung
- Fest kodierte Verschlüsselungsschlüssel
- MD5 weiterhin in Hashketten verwendet
- Zertifikatsprüfung deaktiviert

**Offenlegung von Informationen**:
- Ausführliche Fehlermeldungen geben interne Details preis
- Verzeichnisauflistung auf Webservern aktiviert
- Zugangsdaten in Quellcodekommentaren
- Konfigurationssicherungen weltweit lesbar

### CVE-Status

Stand Mai 2026:
- **22 CVEs zugewiesen** und veröffentlicht
- **8 CVEs warten** auf Zuweisung durch MITRE
- **21 Befunde** wurden nach Ermessen der Forscher nicht als CVE eingereicht
- **Alle Befunde** sind im GainSec-Whitepaper dokumentiert

Vollständige technische Details: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)

______

## Reaktion von Flock Safety

### Offizielle Stellungnahmen

**Blogbeitrag vom November 2025**:
> „Flock setzt sich für die kontinuierliche Verbesserung der Sicherheit ein ... Keine der im Bericht beschriebenen Schwachstellen beeinträchtigt die Fähigkeit unserer Kunden, ihre Ziele für die öffentliche Sicherheit zu erreichen.“

**Behauptung**: Schwachstellen erforderten physischen Zugriff und „detaillierte Kenntnisse“

**Gegenbelege**:
- Für offene Kamerafeeds reichte eine **Google-Suche**
- Bei Funkangriffen genügte **Nähe**
- Der offengelegte API-Schlüssel ließ sich **vollständig aus der Ferne** ausnutzen
- Fest kodierte Passwörter waren nach der Offenlegung **allgemein bekannt**

### Abwertung der Forschungsgeräte

Flock behauptete zunächst, die Forschungsgeräte seien:
> „Nicht mit der Cloud verbunden ... wie ein Lkw, aus dem ein iPhone gestohlen wurde, bevor es jemals verbunden war“

*Das erwies sich als falsch.* Forscher testeten **mit der Cloud verbundene Geräte** und erzielten identische Ergebnisse. Öffentliche Kameras hatten **dieselben Schwachstellen**, und 404 Media fand **mehr als 60 exponierte Produktivkameras**.

### Umgang mit den Forschern

GainSec berichtete, dass Versuche verantwortungsvoller Offenlegung auf Folgendes stießen:
- **Bug-Bounty-Programm mit NDA**, das die Offenlegung unterband
- **Keine Bestätigung**, dass Fehler behoben wurden
- **PR-Stellungnahme vor Ablauf der 90-Tage-Frist**
- **Keine Erwähnung** des Forschers in der Pressemitteilung
- **Verlust des Arbeitsplatzes** innerhalb von 48 Stunden nach Veröffentlichung des Videos

Ben Jordan berichtete von:
- **Polizeibesuchen** auf seinem Grundstück
- **Mutmaßlichen Privatdetektiven**, die sein Haus fotografierten
- **Belästigung durch Nachbarn**
- **Unterlassungsaufforderungen** von Flock Safety

Zitat von Ben:
> „Ich betrachte diese Dinge nicht als Folgen oder Bestrafung für die Untersuchung von Sicherheitslücken. Ich betrachte sie als Folgen und Bestrafung dafür, dass ich ethisch und transparent vorgegangen bin.“

### Weiterer Einsatz

*Trotz alledem*:
- **Verkauft Flock Safety** weiterhin anfällige Geräte
- Gibt es **keine Firmwareupdates**, die Ursachen beheben
- Läuft weiterhin **Android Things 8.x** (Supportende 2021)
- Ist **MFA für Strafverfolgungsbehörden nicht verpflichtend**

______

## Gesetzliche und politische Reaktionen

### Forderung des US-Senats nach einer Untersuchung

**Februar 2026**: Die Senatoren **Ron Wyden** (Oregon) und **Raja Krishnamoorthi** (Illinois) baten die FTC in einem formellen Schreiben um eine Untersuchung.

**Auszug aus dem Schreiben**:
> „Flock hat die sensiblen persönlichen Daten von Amerikanern unnötig dem Diebstahl durch Hacker und ausländische Spione ausgesetzt.“

**Genannte Gründe**:
- Risiken für die nationale Sicherheit
- Irreführende Datenschutzaussagen
- Unzureichende Sicherheitsmaßnahmen
- Fehlende MFA-Pflicht

### Maßnahmen von Stadträten

**Denver, Colorado**:
- Stadtrat **stimmte gegen** die Verlängerung des Flock-Vertrags (Dezember 2025)
- Verurteilte Flocks **„Missachtung von Ehrlichkeit und Rechenschaftspflicht“**
- Bürgermeister **setzte sich darüber hinweg** durch einen „Hinterzimmerdeal“ (Januar 2026)
- Öffentlicher Protest hält an

**Evanston, Illinois**:
- Entdeckte, dass **ICE die Kameras ohne Zustimmung nutzte**
- Stimmte dafür, die Kameras **zu entfernen**
- *Flock installierte sie ohne Erlaubnis erneut*
- Die Stadt gibt Steuergeld aus, um Kameras mit Planen **abzudecken und rechtlich dagegen vorzugehen**

**Oakland, Kalifornien**:
- Verschob die Abstimmung über eine **Erweiterung um 2,25 Millionen US-Dollar**
- Beauftragte ein unabhängiges Sicherheitsaudit
- Bewertete Flocks Wirksamkeitsbehauptungen als **irreführend**

### Anfragen zu öffentlichen Unterlagen

Mehrere Städte führen Untersuchungen durch, gestützt auf:
- Öffentlich verfügbare Sicherheitsforschung
- FOIA-Anfragen zu Flock-Verträgen
- Anforderungen an unabhängige Audits
- Druck aus der Zivilgesellschaft

______

## Technische Analyse: Angriffsszenarien in der Praxis

### Szenario 1: Überwachung durch einen Nationalstaat

**Bedrohungsakteur**: Ausländischer Nachrichtendienst

**Ziel**: Regierungsbeamte verfolgen

**Vorgehen**:
1. IMSI-Catcher einsetzen und LTE-Verkehr der Kamera abfangen
2. Zugangsdaten im Klartext aus dem Stream auslesen
3. Mit kompromittierten API-Schlüsseln (oder dem früher offengelegten ArcGIS-Layer) auf das Backend zugreifen
4. Datenbank nach Fahrzeugen durchsuchen, die bei Regierungseinrichtungen registriert sind
5. Bewegungen von Beamten und Militärangehörigen verfolgen

**Zeitaufwand**: Tage (nach Aufbau der Infrastruktur)
**Wahrscheinlichkeit der Erkennung**: gering (verschlüsseltes C2 imitiert legitimen Datenverkehr)

### Szenario 2: Gegenüberwachung durch organisierte Kriminalität

**Bedrohungsakteur**: Drogenhandelsorganisation

**Ziel**: Streifenmuster der Polizei erkennen

**Vorgehen**:
1. BadUSB-Gerät kaufen (15 US-Dollar)
2. Kameras im eigenen Einsatzgebiet anfahren
3. BadUSB in offenen USB-Anschluss stecken (30 Sekunden)
4. Payload deaktiviert die Kamera oder verändert Aufnahmen
5. Alternativ: Payload leitet Standortdaten von Polizeifahrzeugen an einen entfernten Server aus

**Zeitaufwand**: 30 Sekunden je Kamera
**Wahrscheinlichkeit der Erkennung**: gering (sieht wie legitime Geräteaktivität aus)

### Szenario 3: Stalker / häusliche Gewalt

**Bedrohungsakteur**: Missbräuchlicher Ex-Partner

**Ziel**: Bewegungen des Opfers verfolgen

**Vorgehen**:
1. Kennzeichen des Opfers beschaffen (öffentliche Information)
2. Im Januar 2026 bekannt gewordene offene Flock-Kameraoberfläche über Google suchen
3. 30 Tage Filmmaterial nach dem Fahrzeug durchsuchen
4. Mit öffentlichen Datenbanken abgleichen (Arbeitsadresse, Wohnort usw.)
5. Bewegungsmuster und Zeiten ableiten

**Zeitaufwand**: Minuten bis Stunden
**Wahrscheinlichkeit der Erkennung**: null (es gibt keine Authentifizierungsprotokolle)

### Szenario 4: Beweismanipulation

**Bedrohungsakteur**: Angeklagter in einem Strafverfahren

**Ziel**: Beweise vor der Verhandlung vernichten

**Vorgehen**:
1. Kamerastandort aus der Beweisaufnahme zum Durchsuchungsbefehl erfahren
2. Kamera physisch erreichen (Tastendruckfolge)
3. Root-Shell erlangen
4. Zum Beweisordner navigieren
5. Bestimmte Bilder/Videos löschen oder Zeitstempel verändern

**Zeitaufwand**: unter fünf Minuten
**Wahrscheinlichkeit der Erkennung**: gering (außer die Kamera wird vor dem Zugriff der Verteidigung forensisch untersucht)

### Szenario 5: Datenschutzaktivist oder Journalist

**Bedrohungsakteur**: Für Transparenz eintretende Person

**Ziel**: Übergriffe durch Überwachung dokumentieren

**Vorgehen**:
1. Erkennungsgeräte verwenden (siehe unseren [Flock-You-Hardwareleitfaden](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. Kamerastandorte in der Gemeinde kartieren
3. FOIA-Anfragen zu den Regeln für Filmmaterial stellen
4. Schwachstellen dem Stadtrat demonstrieren
5. Entfernung oder Aufsicht fordern

**Zeitaufwand**: laufend
**Wahrscheinlichkeit der Erkennung**: hoch (öffentliche Aktivität)

______

{{< figure src="flock-camera-attack-scenario-threat-actor-matrix-nation-state-crime.webp" alt="Matrix mit fünf realen Angriffsszenarien gegen Flock-Safety-Kameras: staatliche Überwachung, Gegenüberwachung durch organisierte Kriminalität, Stalking, Beweismanipulation und Datenschutzaktivismus" >}}

______

## Schutz vor diesen Schwachstellen

### Für Strafverfolgungsbehörden

**Sofortmaßnahmen**:
1. **MFA/2FA für alle Nutzer verlangen** (USB-Sicherheitsschlüssel)
2. **Zugriffsprotokolle monatlich prüfen**, um unerlaubte Abfragen zu finden
3. **Freigaben auf notwendige Zuständigkeitsbereiche begrenzen**
4. **Netzwerk isolieren** – Kameras in dedizierte VLANs aufnehmen
5. **Physische Sicherheit** – manipulationssichere Siegel und Überwachung der Kameras
6. **Reaktionsplan** für eine Kompromittierung vorbereiten

**Vertragliche Anforderungen**:
1. **Regelmäßige Sicherheitsaudits** durch unabhängige Unternehmen
2. **Firmwareupdates innerhalb von 30 Tagen** nach Veröffentlichung eines Patches verpflichtend machen
3. **CVE-Meldung innerhalb von 24 Stunden**
4. **Verschlüsselte Speicherung von Beweismitteln** mit kundenseitig verwalteten Schlüsseln
5. **SLA-Strafen** bei Sicherheitsverletzungen
6. **Auditrecht** für Einrichtungen und Quellcode des Anbieters

**Langfristige Strategie**:
1. **Ausstiegsplan** für Betriebssysteme ohne Support
2. **Selbst gehostete Infrastruktur** (weniger Cloud-Abhängigkeit)
3. **Open-Source-Alternativen prüfen**
4. **Transparenz gegenüber der Gemeinde** zu Kamerastandorten und Richtlinien

### Für Flock Safety (Empfehlungen)

**Kritische Priorität** (sofort):
1. Drahtlose Zugangspunkte nach **Tastendruck deaktivieren**
2. **MFA für alle Konten erzwingen**, ohne Ausnahmen
3. Alle fest kodierten Zugangsdaten **systemweit erneuern**
4. **Notfallpatch** für öffentliche Schnittstellen bereitstellen
5. **Daten im Ruhezustand verschlüsseln** und Schlüssel korrekt verwalten

**Hohe Priorität** (30 Tage):
1. Auf ein **unterstütztes Betriebssystem migrieren** (Android 12+ oder Linux)
2. **Bug-Bounty-Programm ohne NDAs** anbieten
3. **Sicherheitsaudit durch Dritte** durchführen und Ergebnisse veröffentlichen
4. **Netzwerkverkehr Ende-zu-Ende verschlüsseln**
5. **Physische Sicherheit verbessern** (offene USB-Anschlüsse entfernen, Gehäuse verstärken)

**Mittlere Priorität** (90 Tage):
1. **Authentifizierungssystem vollständig neu entwickeln**
2. **Secure Boot** mit verifizierter Firmware einführen
3. **Hardware-Sicherheitsmodul** integrieren
4. **Konformitätszertifizierungen** (FedRAMP, SOC 2, ISO 27001) erlangen
5. **Sicherheitsdashboard für Kunden** mit Meldungen zu Sicherheitsverletzungen bereitstellen

**Langfristig** (1 Jahr):
1. **Sicherheitskomponenten als Open Source veröffentlichen** (Vertrauen schaffen)
2. **Adversarial-Testing-Programm** (Red Team) einführen
3. Anforderungen an **Sicherheitsingenieurstellen** festlegen
4. Sicherheitspraktiken in den **SDLC** integrieren (DevSecOps)
5. An **Branchenstandards** mitwirken (OWASP, CIS)

### Für Einzelpersonen

**Schutzmaßnahmen**:
1. **Erkennungsgeräte verwenden** (siehe unseren [Hardwareleitfaden](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))
2. **Kamerastandorte in der Umgebung kartieren**
3. **Routen und Zeiten variieren**, um Musteranalysen zu erschweren
4. Beim Stadtrat **Aufsicht und Transparenz fordern**
5. **FOIA-Anfragen zu eigenen Daten stellen** (soweit gesetzlich zulässig)
6. **Datenschutzgesetze** auf Landes- und Bundesebene unterstützen

**OpSec-Maßnahmen**:
1. **Ungewöhnliche Fahrzeuge vermeiden** (gängige Marke, Modell und Farbe)
2. Bei sensiblen Aktivitäten **andere Fahrzeuge verwenden** (soweit legal)
3. **Alternative Verkehrsmittel** nutzen (Fahrrad, öffentlicher Verkehr, zu Fuß)
4. **Datenschutz-Kennzeichenabdeckungen** verwenden (nur, wenn sie vor Ort legal sind)
5. Bei Korrelationsrisiken **Faraday-Taschen** für Telefone verwenden

{{< stscollective-ad "flockyou" >}}

______

{{< figure src="flock-safety-security-remediation-priority-roadmap.webp" alt="Priorisierte Roadmap mit sofortigen, 30- und 90-Tage- sowie langfristigen Sicherheitsmaßnahmen, die Flock Safety zur Behebung kritischer Schwachstellen umsetzen sollte" >}}

______

## Das Forschungsteam

### GainSec (Jon „GainSec“ Gaines)

**Hintergrund**: Fachkraft für offensive Sicherheit mit mehr als zehn Jahren Erfahrung

**Beitrag**:
- Entdeckte **47 von 51 Schwachstellen**
- Veröffentlichte ein **formelles Whitepaper** mit technischen Details
- Koordinierte die **verantwortungsvolle Offenlegung** mit Flock Safety
- Registrierte **30 CVEs** (22 veröffentlicht, 8 ausstehend)
- Erstellte eine **Defender-Checkliste** für Sicherheitspraktiker

**Kontakt**: whitepaper@gainsecmail.com
**Forschung**: [github.com/GainSec/anti-crime-ecosystem-research](https://github.com/GainSec/anti-crime-ecosystem-research)
**Blog**: [gainsec.com](https://gainsec.com)

### Ben Jordan (Benn Jordan)

**Hintergrund**: Journalist, Musiker und Technologieermittler

**Beitrag**:
- **Videodokumentation** der Schwachstellen
- **Öffentliche Vorführungen** für Journalisten (The Guardian, 404 Media)
- Entdeckte über Google **mehr als 60 offene Kamerafeeds**
- **Aufklärung und Bildung der Öffentlichkeit**
- **Gesetzliche Abstimmung** mit den Büros von Senatoren

**Kontakt**: über den YouTube-Kanal
**Arbeiten**: YouTube – Benn Jordan

### Joshua Michael (Next AI)

**Hintergrund**: OSINT-Spezialist und Datenschutzforscher

**Beitrag**:
- Entdeckte **offengelegte API-Schlüssel** durch Google-Dorking
- Dokumentierte **offene ArcGIS-Layer**
- Entwickelte **OSINT-Methoden** für die Forschung
- **Datenabgleich** mit öffentlichen Datenlecks

**Organisation**: Next AI – Informationsdienstleister aus allen Quellen

### Weitere Mitwirkende

- **404 Media** – investigative Berichterstattung und Offenlegung
- **The Guardian** – internationale Berichterstattung
- **Lucy Parsons Labs** – jahrelange ALPR-Forschung und Interessenvertretung
- **Sassy South** – Organisation in der Gemeinde
- **DeFlock / Will Freeman** – Projekt zur Kartierung von Kamerastandorten
- **Ed Vogel** – rechtliche und politische Analyse

______

## Ethische Überlegungen

### Zeitplan der verantwortungsvollen Offenlegung

Die Sicherheitsgemeinschaft hielt sich an bewährte Verfahren der **verantwortungsvollen Offenlegung**:

**Standardablauf**:
1. Schwachstelle entdecken
2. Anbieter **90 Tage zuvor vertraulich informieren**
3. Anbieter entwickelt und veröffentlicht einen Patch
4. **Öffentliche Offenlegung** nach dem Patch oder nach 90 Tagen (je nachdem, was zuerst eintritt)
5. Detaillierte Analyse zur Unterstützung der Verteidigung

**Was tatsächlich geschah**:
1. GainSec entdeckte Schwachstellen (Ende 2024)
2. **Wiederholte Kontaktaufnahme** mit Flock Safety (ab Februar 2025)
3. Flock bot ein **Bug-Bounty-Programm mit NDA** an (um die Offenlegung zu unterbinden)
4. Flock veröffentlichte **vorzeitig eine PR-Stellungnahme**, ohne den Forscher zu nennen
5. **Keine Bestätigung**, dass Patches installiert wurden
6. GainSec machte die Befunde nach Ablauf der 90-Tage-Fristen **öffentlich**
7. Ben Jordan und 404 Media **überprüften die Befunde unabhängig** an Produktionssystemen

### Vergeltungsmaßnahmen gegen Forscher

GainSec und Ben Jordan berichteten über:
- **Arbeitsplatzverlust** oder berufliche Schwierigkeiten
- **Polizeibesuche** an Privatadressen
- **Mutmaßliche Überwachung** von Häusern und Grundstücken
- **Belästigung durch Nachbarn**
- **Unterlassungsaufforderungen**
- **Angriffe in sozialen Medien** (der Flock-CEO nannte sie „Terroristen“)

Diese **abschreckende Wirkung** auf die Sicherheitsforschung:
- Entmutigt die Offenlegung von Schwachstellen
- Verzögert wichtige Sicherheitskorrekturen
- Schadet der öffentlichen Sicherheit
- Verletzt ethische Normen der Sicherheitsgemeinschaft

*Flocks Umgang mit Forschern, die Offenlegungsprotokolle befolgten, setzt einen gefährlichen Präzedenzfall für die gesamte Sicherheitsforschung.*

Zitat von Ben Jordan:
> „Ich kann es mir nicht leisten, weitere Monate einer weiteren Flock-Safety-Schwachstelle zu widmen. Wie du siehst, ist diese dringend, und ehrlich gesagt befürchte ich, dass sie bereits ausgenutzt wird.“

### Öffentliches Interesse

Die Forscher handelten **im öffentlichen Interesse**, indem sie:
- Verfahren zur **verantwortungsvollen Offenlegung befolgten**
- Den Anbieter **vor der Veröffentlichung benachrichtigten**
- Sensible Angaben **schwärzten**, die einen Angriff erleichtern könnten
- Sicherheitspraktikern **Empfehlungen zur Abwehr gaben**
- Über geeignete Kanäle **Änderungen der Richtlinien forderten**
- **Ein persönliches Risiko eingingen**, um die Öffentlichkeit zu informieren

Ohne ihre Arbeit:
- **Mehr als 80.000 anfällige Kameras** wären weiterhin ungeschützt
- **Über 150 Millionen tägliche Fahrzeugscans** blieben ungeschützt
- **Millionen Amerikaner** wären unwissentlich gefährdet
- Die **nationale Sicherheit** wäre beeinträchtigt
- Es gäbe **keine gesetzgeberischen Schritte**

______

## Fazit: Der Weg nach vorn

{{< figure src="flock-safety-vulnerability-disclosure-timeline-2026.webp" alt="Zeitachse zur Offenlegung von Flock-Safety-Schwachstellen 2024 bis 2026: von der ersten Entdeckung über die verantwortungsvolle Offenlegung bis zum weiterhin ungepatchten Risiko" >}}

### Aktueller Stand (Mai 2026)

- **Mehr als 50 kritische Schwachstellen** dokumentiert und teilweise offengelegt
- **Mehr als 80.000 Kameras** mit ungepatchten Fehlern weiterhin im Einsatz
- Keine **umfassende Fehlerbehebung** durch den Anbieter
- **Begrenzte behördliche Maßnahmen** (FTC-Untersuchung beantragt, aber nicht eingeleitet)
- **Anhaltendes Ausnutzungsrisiko** für nationale Sicherheit und Privatsphäre

### Was geschehen muss

**Branchenweit**:
1. **Verpflichtende Sicherheitsaudits** vor dem Einsatz in Behörden
2. **Unabhängige Tests** durch qualifizierte Dritte
3. **Veröffentlichung von Auditergebnissen**
4. **Haftung der Anbieter** bei Sicherheitsversagen
5. **Einhaltung von Standards** (NIST, ISO usw.)

**Konkret für Flock Safety**:
1. **Sofortige Notfallpatches** für kritische Schwachstellen
2. **Umstieg auf ein unterstütztes Betriebssystem**
3. **Öffentliche Anerkennung des Umfangs**
4. **Entschädigung** der betroffenen Forscher
5. **Transparenzberichte** zum Sicherheitsstatus

**Für Strafverfolgungsbehörden**:
1. **Sicherheitsanforderungen** in Beschaffungsverträgen
2. **Regelmäßige Audits** der eingesetzten Systeme
3. **MFA für alle Nutzer verpflichtend machen**
4. **Pläne zur Reaktion auf Vorfälle**
5. **Transparenz gegenüber der Gemeinde** zu Überwachungsprogrammen

**Gesetzgebung**:
1. **Bundesstandards** für Überwachungstechnik
2. **Meldepflicht für Schwachstellen** gegenüber betroffenen Parteien
3. **Schutz für Hinweisgeber** und Sicherheitsforscher
4. **Zivilrechtliche Ansprüche** bei Datenschutzverletzungen
5. **Aufsichtsmechanismen** für Überwachungssysteme

### Das größere Bild

Dieser Fall steht für **mehr als nur Flock Safety**. Er veranschaulicht:
- Eine **Überwachungsbranche**, die Wachstum über Sicherheit stellt
- **Behördliche Beschaffung** ohne ausreichendes technisches Fachwissen
- Ungeprüfte und unwidersprochene **Anbieterversprechen**
- **Finanzielle Anreize**, die nicht mit der öffentlichen Sicherheit übereinstimmen
- **Regelungslücken** bei der Aufsicht neuer Technologien

*Jede Stadt, die ohne unabhängige Sicherheitsprüfung einen Flock-Vertrag abschließt, trägt diese Risiken ihren Einwohnern auf.*

### Aufruf zum Handeln

**Für Sicherheitsfachleute**:
- Bemühungen um **verantwortungsvolle Offenlegung unterstützen**
- An **Open-Source-Sicherheitswerkzeugen mitarbeiten**
- **Schutz für Forscher fordern**

**Für Strafverfolgungsbehörden**:
- Von Anbietern **Rechenschaft verlangen**
- **Sicherheitsaudits vor dem Einsatz** fordern
- **MFA sofort einführen**
- Die Sicherheitsgemeinschaft **beratend einbeziehen**

**Für politische Entscheidungsträger**:
- Gesetze mit **verbindlichen Sicherheitsstandards verabschieden**
- **Unabhängige Audits** von Überwachungstechnik finanzieren
- Hinweisgeber und Forscher **schützen**
- Aufsichtsstellen mit **technischem Fachwissen schaffen**

**Für die Öffentlichkeit**:
- Sich über Überwachung in der eigenen Gemeinde **informieren**
- An **Stadtratssitzungen teilnehmen**, wenn Verträge besprochen werden
- **Organisationen für Transparenz unterstützen**
- Abgeordnete zu Bedenken **kontaktieren**
- Mit Erkennungstools Überwachung **kartieren** (siehe unseren [Hardwareleitfaden](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/))

### Verwandte Artikel

- **[Flock-Safety-Überwachungskameras: Verbreitung, Datenschutzbedenken und Schutzmaßnahmen](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** – Einordnung der Überwachung
- **[Flock-You-Erkennungsprojekt: Hardwareleitfaden zur Gegenüberwachung](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** – Baue dein eigenes Erkennungsgerät

Darauf zu warten, dass die Branche diese Fehler behebt, ist keine Schutzstrategie. **[FlockYou-Erkennungsgeräte](https://stscollective.com/collections/flockyou-alpr-flock-safety-awareness-devices)** von STS Collective funktionieren bereits. Mit dem Lesercode **SIMEONONSECURITY** erhältst du bis zu 20 % Rabatt.

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  FlockYou-Erkennungsgeräte kaufen und 20 % sparen
{{< /centerbutton >}}

______

## Quellen

1. [GainSec-Forschung zum Anti-Crime-Ökosystem – GitHub](https://github.com/GainSec/anti-crime-ecosystem-research)
2. [GainSec-Whitepaper – Zenodo DOI: 10.5281/zenodo.17529423](https://zenodo.org/records/17584876)
3. [GainSec-Blog – informelle technische Analysen](https://gainsec.com/)
4. [Offizielle Antwort von Flock Safety – November 2025](https://www.flocksafety.com/blog/response-to-compiled-security-research-on-flock-safety-devices)
5. [404 Media – offene Flock-Kamerafeeds](https://www.404media.co/)
6. [Ben Jordan auf YouTube – Demonstrationen von Schwachstellen](https://www.youtube.com/@BennJordan)
7. [National Vulnerability Database](https://nvd.nist.gov/)
8. [MITRE-CVE-Datenbank](https://cve.mitre.org/)
9. [Electronic Frontier Foundation – ALPR-Überwachung](https://www.eff.org/issues/automated-license-plate-readers)
10. [Schreiben von Senator Wyden an die FTC](https://www.wyden.senate.gov/)
11. [Lucy Parsons Labs – ALPR-Forschung](https://lucyparsonslabs.com/)
12. [DeFlock-Projekt – Kamerakartierung](https://deflockproject.org/)
13. [Distributed Denial of Secrets – Dateisystemabbilder einer Flock-ALPR-Kamera](https://ddosecrets.org/article/flock-alpr-camera)
14. [Micah Lee – Flock-Kameras weisen zahlreiche Sicherheitslücken und fest kodierte Zugangsdaten auf](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
15. [WIRED und 404 Media – Hacker drangen in eine Flock-Kamera ein](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
16. [Hackaday – diese Woche in der Sicherheit: Flock-Kameras sind alt](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
17. [NVD – CVE-2021-1905, Use-after-free im Qualcomm-Adreno-GPU-Treiber](https://nvd.nist.gov/vuln/detail/CVE-2021-1905)
18. [NVD – CVE-2018-9568, Type Confusion in Linux-Kernel-Sockets](https://nvd.nist.gov/vuln/detail/CVE-2018-9568)
19. [WiFi Mothership – Erkennung und Geräteübersicht zu Flock-Safety-ALPR](https://wifimothership.com/flock)
20. [CVE.org – Suche nach Einträgen des CVE-Programms](https://www.cve.org/)
21. [Sicherheitswarnung von Flock Safety – Schusserkennung und Kennzeichenerkennung](https://www.flocksafety.com/articles/gunshot-detection-and-license-plate-reader-security-alert)
22. [GainSec – Fly By Device 2: drahtlose RCE bei Falcon und Sparrow](https://gainsec.com/2025/09/27/fly-by-device-2-the-falcon-sparrow-gated-wireless-rce-camera-feed-dos-information-disclosure-and-more/)
23. [GainSec – Root from the Coop Device 3: Root-Shell auf dem Bravo-Computer von Flock Safety](https://gainsec.com/2025/09/19/root-from-the-coop-device-3-root-shell-on-flock-safetys-bravo-compute-box/)
