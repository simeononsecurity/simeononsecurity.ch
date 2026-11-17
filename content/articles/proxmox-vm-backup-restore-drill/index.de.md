---
title: "Proxmox-VM-Wiederherstellungstest: Nachweisen, dass das Gastsystem funktioniert"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Prüfen Sie ein Proxmox-VM-Backup durch eine isolierte Wiederherstellung. Kontrollieren Sie Festplattenabdeckung, Backup-Modus, Gastdaten, Dienststatus und Wiederherstellungszeit, ohne die Produktion zu berühren."
genre: ["Virtualisierung", "Sicherung und Wiederherstellung", "Heimlabor"]
tags: ["Proxmox-Sicherungswiederherstellungstest", "Proxmox-VM-Sicherung", "Proxmox-Wiederherstellungsübung", "qmrestore", "vzdump", "Prüfung von Proxmox Backup Server", "Proxmox-Snapshot-Sicherung", "VM-Wiederherstellungstest", "Sicherungs-RPO und -RTO", "isolierte VM-Wiederherstellung", "Proxmox-Sicherungsmodus", "Sicherung mit Gast-Agent"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Ein Backup wird von einer orangefarbenen Produktions-VM über einen Speichertresor zu einer blauen isolierten Test-VM übertragen. Dabei werden Festplatten, Dienste und Zeiten geprüft."
coverCaption: "Ein abgeschlossener Backup-Auftrag ist der Anfang eines Wiederherstellungstests."
---

Ein grüner Backup-Auftrag zeigt, dass Proxmox ein Backup geschrieben hat. Daraus geht nicht hervor, ob das Gastsystem startet, seine Daten aktuell sind oder sein wichtigster Dienst funktioniert. **Stellen Sie eine Kopie mit einer neuen VM-ID in einem isolierten Netzwerk wieder her.** Das Ergebnis liefert Ihnen einen Nachweis für die Wiederherstellung, bevor ein Ausfall den Test erzwingt.

<!--more-->

Dieser Test behandelt eine **virtuelle Maschine unter Proxmox VE**. Für Container gelten andere Backup-Regeln, besonders für Bind- und Geräte-Mounts. Der [Backup- und Wiederherstellungstest fürs Homelab](/articles/homelab-backup-restore-drill/) auf dieser Website behandelt eine umfassendere Dateiwiederherstellung. Hier testen Sie ein Proxmox-VM-Backup und dessen Arbeitslast.

Ein **Gast** ist das Betriebssystem, das innerhalb einer virtuellen Maschine läuft. **Bind-Mounts** und **Geräte-Mounts** stellen einem Gast Hostressourcen bereit. Testen Sie diese Ressourcen mit einem eigenen Wiederherstellungsplan.

## Wichtigste Erkenntnisse

- **Legen Sie zuerst Erfolgskriterien fest:** Benennen Sie ein Datenelement, eine Dienstprüfung und eine akzeptable Wiederherstellungszeit.
- **Prüfen Sie den Umfang:** Ein VM-Backup überspringt Festplatten mit der Einstellung **No backup** und kann weder externe Dienste noch ausgelassene Daten wiederherstellen.
- **Stellen Sie getrennt wieder her:** Verwenden Sie eine ungenutzte VM-ID und halten Sie das wiederhergestellte Netzwerk von der Produktion isoliert.
- **Dokumentieren Sie Nachweise:** Messen Sie das Alter des Backups, die Wiederherstellungszeit, den Start, vorhandene Festplatten und eine echte Anwendungsprüfung.

## Vor dem Start

Wählen Sie eine VM, deren Backup sich gefahrlos testen lässt. Sie benötigen Proxmox-Administratorzugriff, ein abgeschlossenes Backup auf Dateispeicher oder einem Proxmox Backup Server (PBS), genügend Speicherplatz für eine zweite VM und eine isolierte Bridge oder ein getrenntes Netzwerkgerät. Eine isolierte Bridge ist ein virtuelles Proxmox-Netzwerk ohne Route zu Ihrem Produktions-LAN. Verwenden Sie einen getrennten Adapter oder ein Test-VLAN, wenn Ihnen keine solche Bridge zur Verfügung steht. Lassen Sie die Produktions-VM eingeschaltet. Reservieren Sie eine neue VM-ID, zum Beispiel **920**, nachdem Sie geprüft haben, ob ein anderer Gast diese ID verwendet. Planen Sie genügend Zeit für eine vollständige Wiederherstellung und einen Arbeitslasttest ein.

Notieren Sie die Erfolgskriterien vor der Wiederherstellung. Wählen Sie für einen Dateiserver eine aktuelle Datei und ihren erwarteten Prüfsummenwert oder Inhalt. Wählen Sie für eine Datenbank eine sichere Leseabfrage und einen Datensatz, der vor dem Backup geschrieben wurde. Wählen Sie für einen Webdienst eine lokale Zustandsprüfung und eine repräsentative Seite. Notieren Sie den neuesten akzeptablen Datenzeitpunkt, Ihr **Recovery Point Objective (RPO)**, und die erlaubte Zeit bis zur Wiederherstellung des Dienstes, Ihr **Recovery Time Objective (RTO)**. Ein Startbildschirm allein erfüllt diese Prüfungen nicht.

| Aufzeichnung | Beispielnachweis |
|---|---|
| **Backup-Zeitpunkt** | Snapshot-Zeit und letztes erwartetes Datenelement |
| **Wiederherstellungsziel** | Ungenutzte VM-ID, Zielspeicher, isolierte Bridge |
| **Arbeitslasttest** | Anmeldung, Volume-Einhängung und Anwendungslesevorgang |
| **Zeitlimit** | Start und Ende der Wiederherstellung sowie Dienstprüfung |

Verbinden Sie den wiederhergestellten Gast erst dann mit dem Produktionsnetzwerk, wenn Sie seinen Namen, seine IP-Adresse, MAC-Adresse, geplante Aufgaben und externen Integrationen geprüft haben. Eine kopierte Identität könnte mit der laufenden VM kollidieren oder doppelte Aufträge senden.

## Prüfen, was die Sicherung abdeckt

**Versionsumfang:** Diese Beispiele wurden während der Artikelerstellung nicht ausgeführt. Notieren Sie vor dem Test die Ausgabe von `pveversion --verbose`. Verwenden Sie Dokumentation, die zur installierten Proxmox-VE-Version passt. Halten Sie das Speicher-Backend, den Gasttyp und die Befehlsausgabe im Testprotokoll fest.

Auf einem Proxmox-Knoten zeigt der folgende schreibgeschützte Befehl die Konfiguration der Quell-VM. Ersetzen Sie **120** durch die VM-ID Ihrer Quelle:

```bash
qm config 120
```

Listen Sie alle virtuellen Festplatten und ihre Backup-Einstellung auf. Proxmox' [Dokumentation zu VM-Festplatten](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) erklärt, dass die Option **No backup** eine Festplatte von VM-Backups ausschließt. Prüfen Sie, ob Anwendungsdaten auf einer ausgeschlossenen Festplatte, einem Host-Mount, durchgereichter Hardware oder einem Remote-Dienst liegen. Notieren Sie das separate Wiederherstellungsverfahren. Ein VM-Starttest belegt nicht, dass ausgeschlossene Daten geschützt sind.

Prüfen Sie Zeitstempel, Größe, Aufgabenprotokoll und Speicherort des letzten Backups. Öffnen Sie in der Proxmox-Oberfläche die Ansicht **Backups** des Backup-Speichers oder den Reiter **Backup** der VM. Vergewissern Sie sich, dass der Auftrag ohne Fehler endete. Proxmox' [Backup-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) unterscheidet reguläre Backup-Dateien von PBS-Speicher, der deduplizierte Blöcke und Metadaten aufbewahrt.

| Backup-Modus | Verhalten der VM | Entscheidung für diesen Test |
|---|---|---|
| **Snapshot** | Sichert eine laufende VM mit kurzer Unterbrechung. Schreibvorgänge des Gasts bergen ein geringes Konsistenzrisiko. | Für Routinetests geeignet, wenn die Arbeitslast diesen Wiederherstellungspunkt verträgt. |
| **Stop** | Fährt den Gast zum Start des Backups herunter und bietet die höchste Konsistenz. | Verwenden, wenn die Arbeitslast ein sauberes Herunterfahren verlangt und die Ausfallzeit akzeptabel ist. |
| **Suspend** | Hält den Gast vor dem Snapshot-Modus an und verursacht zusätzliche Ausfallzeit ohne allgemeinen Konsistenzgewinn. | Suspend nicht standardmäßig als Verbesserung gegenüber Snapshot auswählen. |

Diese Abwägungen der Modi stammen aus Proxmox' [Referenz zu Backup-Modi](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Ein **QEMU Guest Agent** ist ein Dienst innerhalb des Gasts, über den Proxmox Aktionen wie das Einfrieren und Auftauen des Dateisystems anfordern kann. Ein laufender Gast mit aktiviertem und funktionsfähigem Guest Agent unterstützt solche Aktionen während eines Snapshot-Backups. Das Einfrieren des Dateisystems verbessert die Konsistenz, ersetzt aber keine datenbankspezifische Wiederherstellungsprüfung. Notieren Sie den tatsächlichen Modus und den Zustand des Guest Agent, statt anzunehmen, dass ein geplanter Auftrag Ihre bevorzugten Einstellungen verwendet.

## Einen Wiederherstellungspunkt erstellen oder auswählen

Verwenden Sie ein aktuelles, erfolgreiches geplantes Backup, wenn der Test die Routinenwiederherstellung prüft. Wenn Sie ein neues einmaliges Backup benötigen, öffnen Sie den Reiter **Backup** der VM, wählen Sie **Backup now**, legen Sie Zielspeicher und Modus fest und warten Sie, bis das Aufgabenprotokoll Erfolg meldet. Von einer Proxmox-Shell aus sichert dieses Beispiel VM **120** im Snapshot-Modus auf eine Speicher-ID namens **backup-nfs**:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Ersetzen Sie beide IDs durch Ihre eigenen Werte. Führen Sie den Befehl erst aus, nachdem Sie bestätigt haben, dass der Speicher Backups annimmt und genug Platz für den Auftrag bietet. Die [Proxmox-Referenz zu `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) beschreibt die Optionen für Modus und Speicher. Prüfen Sie das Aufgabenprotokoll nach der Rückkehr des Befehls. Behandeln Sie ein altes Backup nicht als aktuellen Wiederherstellungspunkt, nur weil sein Dateiname aktuell aussieht.

Wenn das Ziel **PBS** ist, führen Sie einen Prüfauftrag für den ausgewählten Datastore aus oder prüfen Sie ihn. Die PBS-[Dokumentation zur Verifizierung](https://pbs.proxmox.com/docs/maintenance.html) erklärt, wie Sie die Integrität von Backup-Daten prüfen und wiederholte Kontrollen planen. Die Prüfung erkennt beschädigte Backup-Blöcke. **Eine erfolgreiche Prüfung belegt nicht, dass ein wiederhergestelltes Betriebssystem, eine Anwendung oder eine externe Abhängigkeit funktioniert.** Fahren Sie auch nach einem erfolgreichen Prüfergebnis mit dem Wiederherstellungstest fort.

## Auf einer isolierten VM wiederherstellen

Wählen Sie in der Proxmox-Oberfläche das Backup in der Ansicht **Backups** des Speichers aus und wählen Sie **Restore**. Geben Sie eine ungenutzte VM-ID und den vorgesehenen Zielspeicher ein. Lassen Sie **Start after restore** ausgeschaltet. Prüfen Sie die Option zum Erzeugen einer neuen MAC-Adresse. Die offizielle [`qmrestore`-Kurzreferenz](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) definiert eine eindeutige VM-ID, die Speicherauswahl, `--unique` für eine zufällige Ethernet-Adresse und den Standard, die wiederhergestellte VM nicht zu starten.

Für ein dateibasiertes `vzdump`-Archiv zeigt dieser Shell-Befehl das entsprechende Muster. Ersetzen Sie Archivpfad, neue VM-ID und Speicher-ID durch Werte aus Ihrer Umgebung:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

Die [Proxmox-Beschreibung der Wiederherstellung](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) besagt, dass eine Wiederherstellung ohne Zielspeicher den ursprünglichen Speicher verwendet. Setzen Sie **`--storage`**, wenn der alte Speicher auf dem Testknoten nicht existiert. Verwenden Sie **`--force`** nicht für einen Test. Diese Option erlaubt das Überschreiben einer vorhandenen VM, während dieses Verfahren eine ungenutzte ID voraussetzt. PBS-Backups werden ebenfalls über die Proxmox-Oberfläche wiederhergestellt. Wählen Sie den Speichereintrag für den PBS-Snapshot, statt den Snapshot als lokale `.vma.zst`-Datei zu behandeln.

Prüfen Sie vor dem ersten Start jede wiederhergestellte Netzwerkschnittstelle, einschließlich sekundärer Schnittstellen und durchgereichter Interfaces. Eine **MAC-Adresse** identifiziert eine Netzwerkschnittstelle. **DNS** ordnet Namen Adressen zu. **DHCP** weist Netzwerkeinstellungen zu. Ein **VLAN** ist ein logisches Netzwerk, das über gemeinsam genutzte Hardware übertragen wird. Ein **virtuelles TPM** speichert Sicherheitszustand für einen Gast. Trennen Sie jede Schnittstelle oder verbinden Sie sie ausschließlich mit einem isolierten Testsegment. Vergewissern Sie sich, dass keine Produktionsroute, kein DNS-Pfad, DHCP-Dienst, Verwaltungsnetz oder externe Integration erreichbar bleibt. Wenn die Arbeitslast einen weiteren Testdienst benötigt, stellen Sie eine Testkopie im isolierten Netzwerk bereit. Vergleichen Sie Festplattenzuordnungen, Firmware, Anforderungen an das virtuelle TPM und spezielle Geräte mit der Quelle. Externe Festplatten, durchgereichte Geräte und außerhalb der VM gespeicherte Geheimnisse benötigen eigene Pläne.

## Gast und Arbeitslast testen

Starten Sie die wiederhergestellte VM und verwenden Sie zuerst ihre Konsole. Prüfen Sie, ob das Betriebssystem startet, alle erwarteten Volumes eingebunden werden, die Uhrzeit plausibel ist und die Anwendung startet. Führen Sie dann die zuvor festgelegten Erfolgskriterien aus. Vergleichen Sie ein bekanntes Datenelement mit seinem Wert und Zeitstempel vor dem Backup. Eine Anmeldeaufforderung oder ein laufender Prozess allein zeigt nicht, dass der Dienst die richtigen Daten enthält.

| Prüfung | Erfolgskriterium |
|---|---|
| **Start** | Der Gast erreicht eine normale Anmeldung ohne Reparaturmodus oder wiederholte Wiederherstellungsaufforderungen. |
| **Festplatten** | Jede im Backup enthaltene Festplatte ist sichtbar, eingebunden und enthält die erwarteten Daten. |
| **Dienst** | Eine repräsentative lokale Anfrage oder ein Lesevorgang ist erfolgreich. |
| **Wiederherstellungspunkt** | Die wiederhergestellten Daten erfüllen das festgehaltene RPO. |
| **Wiederherstellungszeit** | Wiederherstellung, Start und Dienstprüfung erfüllen das festgehaltene RTO. |
| **Isolation** | Keine Produktionsadresse, Aufgabe oder Integration empfängt doppelten Datenverkehr. |

Halten Sie den wiederhergestellten Gast isoliert, während Sie geplante Aufgaben, Benachrichtigungs-Hooks, Backup-Agenten und Anmeldeinformationen der Anwendung prüfen. Führen Sie keinen Test aus, der echte Kundennachrichten sendet oder in Produktionsdienste schreibt. Wenn eine Prüfung fehlschlägt, notieren Sie den genauen Schritt. Unterscheiden Sie **Fehler der Backup-Integrität**, **VM-Startfehler**, **fehlende Daten** und **Anwendungsfehler**. Jeder weist auf eine andere Behebung hin.

| Fehlerklasse | Nachweis | Erste Korrektur | Erneuter Test |
|---|---|---|---|
| **Backup-Integrität** | Prüf- oder Wiederherstellungsauftrag meldet beschädigte Daten | Wählen Sie einen anderen verifizierten Wiederherstellungspunkt und prüfen Sie den Zustand des Speichers | Prüfung und Wiederherstellung wiederholen |
| **VM-Start** | Konsole zeigt Firmware-, Festplatten- oder Wiederherstellungsfehler | Vergleichen Sie Firmware, Festplattenzuordnung und Startreihenfolge mit der Quelle | Isolierte Kopie starten und Konsolenergebnis notieren |
| **Fehlende Daten** | Erwartete Datei, Volume oder Datenbankzeile fehlt | Prüfen Sie ausgeschlossene Festplatten, Mounts, Snapshots und externe Abhängigkeiten | Benannte Datei- oder Datenprüfung wiederholen |
| **Anwendung** | Gast startet, doch die Dienstprüfung schlägt fehl | Prüfen Sie Dienstprotokolle, Anmeldeinformationen, Abhängigkeiten und Wiederherstellungsschritte | Dieselbe lokale Zustandsprüfung und Arbeitslastprüfung ausführen |

Proxmox bietet eine [Wiederherstellung einzelner Dateien für PBS-Backups](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Verwenden Sie sie, um einen Dateiwiederherstellungspfad zu testen, wenn Ihre Arbeitslast eine einzelne Datei benötigt. Eine wiederhergestellte Datei ersetzt keinen vollständigen VM-Start und Diensttest. Proxmox bietet auch eine Live-Wiederherstellung aus PBS. Laut Dokumentation befindet sich die VM nach einer fehlgeschlagenen Live-Wiederherstellung in einem undefinierten Zustand. Verwenden Sie für diesen geplanten Test deshalb eine normale, abgeschlossene Wiederherstellung.

## Ergebnis dokumentieren und Prüfung abschließen

Notieren Sie Quell-VM-ID, Backup-Speicher, Backup-Zeitstempel, Backup-Modus, neue VM-ID, Zielspeicher, Netzwerkisolation, Start- und Endzeit der Wiederherstellung, Anwendungsprüfung, Datenzeitstempel und alle fehlgeschlagenen Prüfungen. Vergleichen Sie den gemessenen Wiederherstellungspunkt und die Zeit mit Ihren Zielwerten. Ein Fehler ist nur dann ein nützlicher Nachweis, wenn Sie den Backup-Plan ändern und den Test wiederholen.

Fahren Sie die wiederhergestellte VM nach Abschluss des Tests herunter. Entfernen Sie die Testkopie erst, nachdem Sie das Ergebnis gespeichert haben, und prüfen Sie, ob die Produktions-VM weiterhin erwartungsgemäß läuft. Halten Sie sich an Ihre normale Aufbewahrungsrichtlinie für Backups. Ändern Sie die Aufbewahrung nicht, nur damit ein einzelner Test besteht.

Wiederholen Sie den Test nach größeren Änderungen an Speicher, Gast oder Backup-Konfiguration. Wechseln Sie zwischen wichtigen VMs, auch zwischen Gästen mit ausgeschlossenen Festplatten oder externen Abhängigkeiten. Der [Migrationsleitfaden von Hyper-V zu Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) verlangt diesen Wiederherstellungsnachweis, bevor eine Quell-VM außer Betrieb genommen wird. **Ein brauchbares Backup hat einen bekannten Wiederherstellungspfad, eine getestete Arbeitslast und einen gemessenen Wiederherstellungspunkt.**

## Nächste Schritte

Wiederholen Sie den Test nach Änderungen an Speicher, Gast oder Backup. Lesen Sie den [Backup- und Wiederherstellungstest fürs Homelab](/articles/homelab-backup-restore-drill/) zur Wiederherstellung einzelner Dateien.
