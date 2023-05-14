---
title: "Schutz von Windows vor Seitenkanalangriffen mit spekulativer Ausführung"
date: 2020-06-18
toc: true
draft: false
description: "Erfahren Sie, wie Sie Ihr Windows-System mit Microsofts Mitigationsskript und Firmware-Updates vor Seitenkanalangriffen mit spekulativer Ausführung schützen können"
tags: ["Windows Spectre Meltdown Mitigation Script", "Seitenkanalangriffe auf spekulative Ausführung", "Microsoft", "Intel", "AMD", "VIA", "ARM", "Android", "Chrom", "iOS", "macOS", "Zweigzielinjektion", "Bounds Check Bypass", "Rogue Data Cache Load", "Spekulative Speicherumgehung", "Mikroarchitektonische Datenabtastung", "CVEs", "Firmware-Aktualisierungen", "GitHub-Repository", "PowerShell"]
---
 https://support.microsoft.com/en-us/help/4073119/protect-against-speculative-execution-side-channel-vulnerabilities-in
**Einfaches Skript zur Implementierung von Schutzmaßnahmen gegen Seitenkanal-Schwachstellen bei spekulativer Ausführung in Windows-Systemen**.

Microsoft ist sich einer neuen, öffentlich bekannt gewordenen Klasse von Sicherheitsanfälligkeiten bewusst, die als "Seitenkanalangriffe bei spekulativer Ausführung" bezeichnet werden und viele moderne Prozessoren einschließlich Intel, AMD, VIA und ARM betreffen.

**Hinweis:** Dieses Problem betrifft auch andere Betriebssysteme, wie Android, Chrome, iOS und macOS. Daher raten wir unseren Kunden, sich bei diesen Anbietern zu informieren.

Wir haben mehrere Updates veröffentlicht, um diese Schwachstellen zu entschärfen. Außerdem haben wir Maßnahmen ergriffen, um unsere Cloud-Dienste zu sichern. In den folgenden Abschnitten finden Sie weitere Einzelheiten.

Wir haben bisher keine Informationen erhalten, die darauf hindeuten, dass diese Sicherheitslücken für Angriffe auf Kunden genutzt wurden. Wir arbeiten eng mit Industriepartnern zusammen, darunter Chip-Hersteller, Hardware-OEMs und Anwendungsanbieter, um unsere Kunden zu schützen. Um alle verfügbaren Schutzmaßnahmen zu erhalten, sind Firmware- (Mikrocode) und Software-Updates erforderlich. Dazu gehören Mikrocode von Geräte-OEMs und in einigen Fällen auch Updates für Antiviren-Software.

**Dieser Artikel befasst sich mit den folgenden Sicherheitslücken:**
- CVE-2017-5715 - "Zweigziel-Injektion"
- CVE-2017-5753 - "Umgehung der Grenzprüfung"
- CVE-2017-5754 - "Schurkenhaftes Laden des Daten-Caches"
- CVE-2018-3639 - "Umgehung des spekulativen Speichers".
- CVE-2018-11091 - "Nicht zwischenspeicherfähiger Speicher mit mikroarchitektonischer Datenabtastung (MDSUM)"
- CVE-2018-12126 - "Mikroarchitektonische Speicherpuffer-Datenabtastung (MSBDS)"
- CVE-2018-12127 - "Mikroarchitektonische Datenabtastung des Füllpuffers (MFBDS)"
- CVE-2018-12130 - "Mikroarchitektonische Ladeport-Datenabtastung (MLPDS)"

**AKTUALISIERT AM 6. AUGUST 2019** Am 6. August 2019 veröffentlichte Intel Details zu einer Windows-Kernel-Informationsoffenlegungsschwachstelle. Diese Schwachstelle ist eine Variante der Spectre-Variante-1-Seitenkanalschwachstelle für spekulative Ausführung und wurde CVE-2019-1125 zugeordnet.

**AKTUALISIERT AM 12. NOVEMBER 2019** Am 12. November 2019 veröffentlichte Intel einen technischen Hinweis zur Intel® Transactional Synchronization Extensions (Intel® TSX) Transaction Asynchronous Abort-Schwachstelle, die CVE-2019-11135 zugeordnet ist. Microsoft hat Updates veröffentlicht, um diese Sicherheitsanfälligkeit zu entschärfen, und die Schutzmaßnahmen des Betriebssystems sind standardmäßig für Windows Client OS Editions aktiviert.

## Empfohlene Maßnahmen
Kunden sollten die folgenden Maßnahmen ergreifen, um sich vor den Sicherheitslücken zu schützen:

- Installieren Sie alle verfügbaren Windows-Betriebssystem-Updates, einschließlich der monatlichen Windows-Sicherheitsupdates.
- Wenden Sie das entsprechende Firmware-Update (Microcode) an, das vom Gerätehersteller bereitgestellt wird.
- Bewerten Sie das Risiko für Ihre Umgebung anhand der Informationen, die in den Microsoft-Sicherheitshinweisen enthalten sind: ADV180002, ADV180012, ADV190013 und den Informationen in diesem Knowledge Base-Artikel.
- Ergreifen Sie die erforderlichen Maßnahmen, indem Sie die in diesem Knowledge Base-Artikel bereitgestellten Hinweise und Registrierungsschlüsselinformationen verwenden.

## Laden Sie die erforderlichen Dateien herunter:

Laden Sie die erforderlichen Dateien von der Seite[GitHub Repository](https://github.com/simeononsecurity/Windows-Spectre-Meltdown-Mitigation-Script)

## So führen Sie das Skript aus:

**Das Skript kann aus dem extrahierten GitHub-Download wie folgt gestartet werden:**
```
.\sos-spectre-meltdown-mitigations.ps1
```
