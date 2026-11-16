---
title: "BitLocker-Wiederherstellungsschlüssel vor der Windows-Neuinstallation finden"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Finde und prüfe den passenden BitLocker-Wiederherstellungsschlüssel, sichere eine separate Kopie und wähle vor dem Löschen des Laufwerks den passenden Windows-Wiederherstellungs- oder Neuinstallationsweg."
genre: ["Windows-Sicherheit", "Datenwiederherstellung", "Systemverwaltung"]
tags: ["BitLocker-Wiederherstellungsschlüssel", "Windows 11 neu installieren", "Windows 10 neu installieren", "Geräteverschlüsselung", "Wiederherstellungsschlüssel-ID", "Wiederherstellungsschlüssel im Microsoft-Konto", "Wiederherstellungsschlüssel für Arbeits- oder Schulkonto", "Wiederherstellungsschlüssel sichern", "verschlüsseltes Laufwerk", "saubere Installation", "Windows-Wiederherstellung", "BitLocker-Sicherung", "48-stelliger Wiederherstellungsschlüssel", "Windows-Installationsmedium", "Datensicherung", "Laufwerksverschlüsselung", "Wiederherstellungs-Checkliste", "Windows-Installation", "BitLocker-Fehlerbehebung", "Vorbereitung auf Neuinstallation"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Ein Laptop mit gesperrtem Laufwerk, einer separaten Karte mit Wiederherstellungsschlüssel, USB-Sicherung und abgehakter Wiederherstellungs-Checkliste."
coverCaption: "Prüfe den Wiederherstellungsschlüssel, bevor du das Laufwerk löschst."
---

Eine saubere Windows-Installation löscht das ausgewählte Laufwerk. Wenn das alte Laufwerk **BitLocker** oder **Geräteverschlüsselung** verwendet, suche zuerst den Wiederherstellungsschlüssel und kopiere deine Dateien. Der Schlüssel ermöglicht den Zugriff auf die alten verschlüsselten Daten. Eine neue Windows-Installation stellt gelöschte Dateien nicht wieder her.

<!--more-->

## Wichtigste Punkte

- **Finde den richtigen Schlüssel:** Vergleiche die von Windows angezeigte ID mit dem Schlüssel in deinem Konto, auf einem Ausdruck oder auf einem USB-Backup.
- **Prüfe den Zugriff:** Öffne das Backup, gleiche die ID ab und entsperre ein gesperrtes Laufwerk, bevor du Partitionen löschst.
- **Schütze das Backup:** Bewahre den 48-stelligen Schlüssel getrennt vom Computer und Installations-USB auf.
- **Wähle den passenden Weg:** Nutze Wiederherstellungsoptionen, wenn du die alte Installation benötigst. Führe eine saubere Installation erst aus, nachdem du eine separate Dateikopie geprüft hast.

## Vor Beginn

Du brauchst Zugriff auf den betroffenen Computer, ein zweites Gerät zum Prüfen deines Kontos oder Backups und ein externes Laufwerk oder vertrauenswürdigen Cloud-Speicher für wichtige Dateien. **Zeit:** Das Auffinden des Schlüssels hängt vom Kontozugriff ab. Die Kopierzeit hängt von der Datenmenge ab. **Schwierigkeit:** einfach für die Kontoprüfung, mittel für Wiederherstellungstools. Dieser Leitfaden behandelt Vorbereitung und Wiederherstellungsentscheidungen für Windows 10 und Windows 11. Der [Leitfaden zur sauberen Windows-Installation](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) beschreibt Installationsmedien und Setup.

*Der reguläre Support für Windows 10 endete am 14. Oktober 2025. Plane eine unterstützte Windows-11-Installation, wenn dein Gerät die Anforderungen erfüllt. Microsoft nennt den [Windows-10-Lebenszyklus und Optionen für erweiterten Support](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Warnung:** Lösche keine Partition, um eine BitLocker-Wiederherstellungsabfrage zu beheben, wenn du noch Dateien aus der alten Installation brauchst. Microsoft weist darauf hin, dass ein Zurücksetzen ohne Wiederherstellungsschlüssel diese Dateien entfernt. Siehe [Microsofts Hinweise zu Wiederherstellungsschlüsseln](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Prüfen, ob die Verschlüsselung aktiv ist

**Geräteverschlüsselung** und **BitLocker** verschlüsseln ein Laufwerk, damit Personen ohne passende Zugangsdaten den Inhalt nicht lesen können. Wenn Windows noch startet, öffne unter Windows 11 **Einstellungen > Datenschutz und Sicherheit > Geräteverschlüsselung**. Suche in Editionen mit BitLocker-Verwaltung im Startmenü nach **BitLocker verwalten**. Notiere den Laufwerksbuchstaben des verschlüsselten Laufwerks und das Konto, mit dem das Gerät eingerichtet wurde. Bei einem verwalteten Arbeits- oder Schulgerät speichert oft die Organisation den Schlüssel.

Optional kannst du den Status über die Eingabeaufforderung prüfen. Suche im Startmenü nach **Eingabeaufforderung**, wähle **Als Administrator ausführen** und gib die folgenden Befehle ein. Ersetze `C:`, wenn Windows einen anderen Laufwerksbuchstaben verwendet. Ein **Protektor** ist eine Methode, mit der Windows ein verschlüsseltes Laufwerk entsperrt.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

Der erste Befehl zeigt Verschlüsselungs-, Schutz- und Sperrstatus. Der zweite listet Protektortypen und IDs auf und kann das Wiederherstellungskennwort offenlegen. Microsoft dokumentiert beide Prüfungen im [BitLocker-Betriebshandbuch](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) und in der [Referenz zum Statusbefehl](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Füge die Ausgabe weder in eine Supportanfrage noch in einen Screenshot ein.** Ist das Gerät bereits gesperrt, verwende die ID auf dem Wiederherstellungsbildschirm. Die ersten acht Ziffern der ID helfen bei der Auswahl des passenden Schlüssels.

## Wo du den BitLocker-Wiederherstellungsschlüssel findest

Die **Wiederherstellungsschlüssel-ID** kennzeichnet einen gespeicherten Schlüssel. Der **Wiederherstellungsschlüssel** ist die separate 48-stellige Zahl, die du zum Entsperren des Laufwerks eingibst. Gib die ID nicht in das Feld für das Wiederherstellungskennwort ein.

| Gerät oder Backup | Wo du suchen solltest |
|---|---|
| **Persönliches Microsoft-Konto** | Melde dich auf einem zweiten Gerät über Microsofts [Seite für Wiederherstellungsschlüssel](https://aka.ms/myrecoverykey) an. Gleiche die ID ab, bevor du den 48-stelligen Schlüssel verwendest. |
| **Arbeits- oder Schulgerät** | Prüfe das Organisationskonto über Microsofts [Seite für Arbeits- und Schulkonten](https://aka.ms/aadrecoverykey), oder frage dein IT-Team. |
| **Ausdruck oder USB-Backup** | Suche den Ausdruck oder die Textdatei, die beim Aktivieren der Verschlüsselung erstellt wurde. Vergleiche die Schlüssel-ID mit der Anzeige. |

Microsoft nennt diese Speicherorte unter [BitLocker-Wiederherstellungsschlüssel finden](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Beginne mit dem Schlüssel, dessen ID zur Abfrage passt. Ein Schlüssel eines anderen Geräts oder eines entfernten Protektors entsperrt dieses Volume möglicherweise nicht. Wenn eine andere Person das Gerät eingerichtet hat, kann sich der Schlüssel laut Microsoft in deren Konto befinden.

## Eine eigenständige Schlüsselsicherung erstellen

Wenn Windows in einer Pro-, Enterprise- oder Education-Edition noch startet, suche nach **BitLocker verwalten**. Wähle neben dem verschlüsselten Laufwerk **Wiederherstellungsschlüssel sichern**. Microsoft bietet eine Sicherung in einem Konto, auf einem USB-Laufwerk, als Textdatei oder als Ausdruck an. Speichere Textdatei oder USB nur auf verschlüsselten Medien mit Zugriffskontrolle und getrennt vom Computer. Verwende keinen unverschlüsselten Speicherort. Die aktuelle Oberfläche und Optionen beschreibt [BitLocker-Wiederherstellungsschlüssel sichern](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key).

Unter Windows Home fehlt **BitLocker verwalten**. Prüfe unter Windows 11 **Einstellungen > Datenschutz und Sicherheit > Geräteverschlüsselung** und kontrolliere dann den Schlüssel im Microsoft-Konto, das bei der Einrichtung verwendet wurde. Microsoft erklärt, dass [Geräteverschlüsselung](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) den Schlüssel bei der Aktivierung im verknüpften Microsoft- oder Arbeitskonto speichert. Erstelle eine separate geschützte Kopie, wenn dein Setup einen Export anbietet.

Öffne ein digitales Backup auf einem zweiten Gerät. Vergleiche einen Ausdruck mit dem Kontoeintrag oder dem Wiederherstellungsbildschirm. Gleiche die **Wiederherstellungsschlüssel-ID** mit der ID auf dem Bildschirm oder in der Protektorliste ab. Prüfe, ob alle 48 Ziffern des zugehörigen Schlüssels vorhanden sind. Bewahre Ausdruck oder Wechseldatenträger getrennt vom verschlüsselten Computer auf. Ein Dieb mit Computer und Schlüssel könnte den Laufwerksschutz umgehen, warnt Microsoft in den [Sicherungshinweisen](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Hänge den Schlüssel nicht an ein Supportticket an.

> **Erwartetes Ergebnis:** Du kannst außerhalb des Computers auf einen passenden Wiederherstellungsschlüssel zugreifen.

## Einen nicht startenden PC entsperren

Wenn der **BitLocker-Wiederherstellungsbildschirm** erscheint, gib den 48-stelligen Schlüssel ein, der zu dessen ID passt. Wenn Windows startet, kopiere deine Dateien, bevor du Partitionen änderst. Entsperrt der Schlüssel das Laufwerk, Windows startet aber weiterhin nicht, öffne die [Windows-Wiederherstellungsumgebung](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) und probiere vor dem Zurücksetzen **Starthilfe**. Einige Wiederherstellungstools benötigen den Schlüssel, solange das Laufwerk verschlüsselt ist.

Für eine Dateisicherung über Wiederherstellungstools öffne in der Windows-Wiederherstellungsumgebung **Problembehandlung > Erweiterte Optionen > Eingabeaufforderung**. Verwende `manage-bde -status` und `dir`, um das verschlüsselte Windows-Volume und ein separates externes Backup-Laufwerk zu finden. **Laufwerksbuchstaben können von den üblichen Windows-Buchstaben abweichen.** Kopiere Dateien nicht auf den Installations-USB oder das verschlüsselte Quelllaufwerk.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Die Buchstaben sind Beispiele. Entsperre nach der Identifizierung der richtigen Volumes das Windows-Volume mit dem passenden Schlüssel. Ersetze Beispielbuchstaben und Platzhalter durch deine Werte. Gib den echten 48-stelligen Schlüssel nur lokal ein. Veröffentliche oder teile die Ausgabe nicht.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

Die dokumentierte Option `-recoverypassword` erwartet den 48-stelligen Schlüssel als Befehlszeilenargument. Dadurch kann er im Shell-Verlauf, in Transkripten und bei der Prozessinspektion sichtbar werden. Verwende den Windows-Wiederherstellungsbildschirm, wenn du den Schlüssel ohne Befehlszeilenargument eingeben möchtest. Wenn du eine separate `.bek`-Schlüsseldatei gespeichert hast, erspart `-recoverykey <path-to-external-bek>` die Eingabe der 48 Ziffern. Halte den Schlüssel aus Screenshots und Tickets heraus.

Microsoft dokumentiert den [Entsperrbefehl](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). Die [Wiederherstellungshinweise](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) beschreiben auch das Kopieren von Benutzerdateien auf ein anderes Laufwerk nach dem Entsperren. Für eine beispielhafte Kopie des Ordners „Dokumente“ bestätige zuerst den Windows-Kontonamen und den Laufwerksbuchstaben des externen Laufwerks. Ersetze dann beide Pfade:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Die Optionen **`/S /E`** schließen Unterordner einschließlich leerer Ordner ein. **`/I`** behandelt das Ziel als Ordner, **`/H`** schließt versteckte Dateien ein und **`/V`** prüft jede geschriebene Datei. Microsoft beschreibt diese Optionen in der [xcopy-Referenz](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Wiederhole den Vorgang für andere benötigte Ordner. Öffne kopierte Dateien auf einem anderen Gerät, bevor du das Windows-Laufwerk löschst. Kannst du die Volumes nicht bestimmen oder schlägt das Kopieren fehl, stoppe und wende dich an einen vertrauenswürdigen Datenrettungsdienst.

## Entscheiden, ob du Windows neu installierst

**Eine Schlüsselsicherung ist keine Dateisicherung.** Gehe vor der Auswahl einer Neuinstallationsmethode in dieser Reihenfolge vor:

1. Identifiziere das verschlüsselte Laufwerk und seine Wiederherstellungsschlüssel-ID.
2. Rufe den passenden 48-stelligen Schlüssel aus deinem Konto, Ausdruck oder USB-Backup ab.
3. Entsperre ein gesperrtes Laufwerk über den Wiederherstellungsbildschirm oder die Wiederherstellungstools.
4. Kopiere Desktop, Dokumente, Bilder und andere lokale Ordner auf ein externes Laufwerk oder in einen vertrauenswürdigen Cloud-Speicher. Sichere bei Bedarf Browserexporte, Anwendungsdaten und Lizenznachweise.
5. Öffne mehrere kopierte Dateien auf einem zweiten Gerät.
6. Wähle Reparatur, Zurücksetzen oder Neuinstallation erst nach der Prüfung des Backups.

> **Erwartetes Ergebnis:** Der passende Schlüssel und wichtige Dateien sind außerhalb der alten Windows-Installation erreichbar.

Microsoft führt [Windows-Wiederherstellungsoptionen](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows) mit unterschiedlichen Folgen für Dateien und Apps auf. Viele Optionen der Windows-Wiederherstellungsumgebung verlangen den Wiederherstellungsschlüssel, wenn BitLocker das Laufwerk schützt. Ist das Volume dort gesperrt, entsperrt **Eigene Dateien beibehalten** es nicht ohne Schlüssel.

**Starthilfe** und **Systemwiederherstellung** sollen die vorhandene Installation reparieren. **Diesen PC zurücksetzen** bietet **Eigene Dateien beibehalten**, entfernt aber Apps und Einstellungen. **Alles entfernen** löscht persönliche Dateien. Das Starten von **`setup.exe` in einer laufenden Windows-Sitzung** ermöglicht eine Inplace-Neuinstallation mit Optionen zum Beibehalten von Daten. **Windows installieren** nach dem Start von Installations-USB beginnt eine saubere Installation, die Dateien, Apps und Einstellungen der ausgewählten Windows-Installation entfernt. Dasselbe Medium bietet auch einen Reparaturweg. Lies die angezeigte Option und das Ziellaufwerk, bevor du Reset oder Installation bestätigst. Microsoft erklärt beide Wege in den [Anweisungen zur Neuinstallation](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Ausgangslage | Nächster Schritt |
|---|---|
| **Windows startet und du brauchst die Dateien** | Sichere die Dateien, prüfe den Wiederherstellungsschlüssel und wähle dann Reparatur oder Neuinstallation. |
| **Windows verlangt den Schlüssel** | Gleiche die Bildschirm-ID mit einem gespeicherten Schlüssel ab, bevor du das Laufwerk änderst. |
| **Kein passender Schlüssel und kein Datei-Backup** | Stoppe, bevor du das Laufwerk löschst. Prüfe alle Konten, Ausdrucke und USB-Backups und frage dein IT-Team. |
| **Dateien sind gesichert und du willst neu anfangen** | Folge Microsofts [Neuinstallationsanweisungen](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) und wähle das Ziellaufwerk sorgfältig. |

Microsoft erklärt, dass der Support einen verlorenen Wiederherstellungsschlüssel nicht rekonstruieren kann. Wenn du ihn nicht findest, ändere keine Firmwareeinstellungen mehr und prüfe alle Speicherorte der Backups. Bitte bei einem verwalteten Gerät die Geräteverwaltung um Hilfe. Ein Zurücksetzen ohne erforderlichen Schlüssel entfernt die alten Dateien. Eine saubere Installation entfernt außerdem persönliche Dateien, Apps, Geräteanpassungen und Einstellungen der ausgewählten Installation. Triff diese Entscheidung bewusst, nachdem du das Backup geprüft hast.

## Fehlerbehebung

- **Der Schlüssel funktioniert nicht:** Prüfe Schlüssel-ID und Konto erneut. Ein Gerät kann mehrere gespeicherte Wiederherstellungsschlüssel haben.
- **BitLocker verwalten ist nicht verfügbar:** Windows Home verwendet auf geeigneten Geräten Geräteverschlüsselung. Prüfe Einstellungen und das Microsoft-Konto aus der Einrichtung.
- **Im Konto erscheinen mehrere Schlüssel:** Vergleiche die ersten acht Ziffern der ID auf dem Wiederherstellungsbildschirm mit den gespeicherten Einträgen. Wähle keinen Schlüssel nur anhand des Gerätenamens.
- **Der Schlüssel entsperrt das Laufwerk, aber Windows startet nicht:** Probiere Starthilfe in der Windows-Wiederherstellungsumgebung. Sichere erreichbare Dateien vor Reset oder sauberer Installation.
- **Der Schlüssel liegt bei Arbeit oder Schule:** Kontaktiere vor dem Zurücksetzen oder der Neuinstallation die Geräteverwaltung.
- **Die Schlüsseldatei liegt auf dem gesperrten Computer:** Suche ein separates Konto, einen Ausdruck oder ein Wechseldatenträger-Backup. Eine Kopie nur auf dem verschlüsselten Laufwerk hilft im gesperrten Zustand nicht.
- **Die Wiederherstellungsabfrage erschien nach einer Firmwareänderung:** Notiere die Änderung und nimm keine weiteren vor. Suche den passenden Schlüssel oder kontaktiere die Geräteverwaltung.

## Nächste Schritte

Nachdem du Schlüssel und Dateien geprüft hast, folge dem [Leitfaden zur sauberen Windows-Installation](/articles/how-to-install-windows-10-and-windows-11-from-scratch/), wenn eine Neuinstallation zu deinem Ziel passt. Prüfe nach dem Start von Windows **Einstellungen > Datenschutz und Sicherheit > Geräteverschlüsselung** oder suche nach **BitLocker verwalten**. Wähle in Pro, Enterprise oder Education dort **Wiederherstellungsschlüssel sichern**. Prüfe unter Home, ob das verknüpfte Konto den aktuellen Schlüssel enthält, und speichere eine separate Kopie, wenn Windows einen Export anbietet. Gehe nicht davon aus, dass der alte Schlüssel zu einer neu verschlüsselten Installation gehört.
