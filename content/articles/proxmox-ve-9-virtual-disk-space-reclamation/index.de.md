---
title: "Proxmox VE 9: Virtuelle Festplatten verkleinern und Speicherplatz freigeben"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Reduzieren Sie den Speicherbedarf von VMs und LXC-Containern unter Proxmox VE 9. Vergleichen Sie Formate und Speicher-Backends, aktivieren Sie Discard, führen Sie Trim aus und prüfen Sie Snapshots."
genre: ["Virtualisierung", "Linux-Systemverwaltung", "Proxmox VE Plattform", "Speicher", "Heimlabor"]
tags: ["Proxmox VE 9 Festplattenspeicher", "dünne Bereitstellung Proxmox", "Proxmox discard-Meldungen", "Proxmox TRIM-Befehl", "Windows-ReTrim im Proxmox-Gast", "Linux-Werkzeug fstrim im Proxmox-Gast", "Proxmox LXC-Festplattenbelegung", "Proxmox Thin Provisioning mit LVM", "Proxmox Sparse-zvol in ZFS", "Proxmox Ceph-RBD-Blockgeräte", "Proxmox qcow2-Format", "Proxmox raw-Datenträger", "Proxmox-Schnappschüsse", "Speicherplatz virtueller Datenträger freigeben", "Proxmox-Speichertypen", "VirtIO-SCSI-Controller", "Proxmox-Erkennung von Nullschreibvorgängen", "Proxmox-Backup-Speicher"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Zwei durch einen Pfeil verbundene Blockraster zeigen belegte Blöcke eines virtuellen Datenträgers und freie Kapazität in einem Speicherpool."
coverCaption: "Löschen im Gast, Discard und Speicherfreigabe sind getrennte Schritte."
---

**Ein kleineres Gastdateisystem bedeutet nicht immer weniger belegten Proxmox-Speicher.** Freier Speicherplatz auf dem Host setzt einen Thin-fähigen Datenträger, einen funktionierenden Discard-Pfad für VMs und ein Backend ohne durch Snapshots gehaltene Blöcke voraus. Diese Anleitung beschreibt Einstellungen und Prüfungen für Proxmox VE 9 VMs und LXC-Container.

<!--more-->

## Wichtigste Erkenntnisse

- **Wählen Sie zuerst das Backend.** Die angegebene Größe eines virtuellen Datenträgers weicht nur dann vom Host-Speicher ab, wenn das Imageformat oder Backend Thin Provisioning unterstützt.
- **Aktivieren Sie Discard für die VM und führen Sie anschließend Trim im Gast aus.** Windows ReTrim und Linux `fstrim` senden Anforderungen für ungenutzte Blöcke durch den virtuellen Datenträger.
- **Prüfen Sie Snapshots und Sicherungen getrennt.** Alte Blöcke bleiben belegt, solange ein Snapshot darauf verweist. Sicherungsdateien und PBS-Chunks folgen eigenen Aufbewahrungsregeln.
- **Ordnen Sie LXC-Mounts nach Typ ein.** Verwaltete rootfs- und Mount-Point-Volumes, Bind-Mounts und Geräte-Mounts haben unterschiedliche Zuständigkeiten und Sicherungseigenschaften.

## Vor dem Start

Sie benötigen **Administratorzugriff auf Proxmox VE 9**, eine geprüfte Sicherung jedes betroffenen Gasts und genug freien Pool-Speicher für den Vorgang. Notieren Sie vor Änderungen die Gast-ID, den Disk-Bus, die Volume-ID, die Speicher-ID, Snapshots und die aktuelle Belegung. Führen Sie den [VM-Wiederherstellungstest](/articles/proxmox-vm-backup-restore-drill/) durch, um die Wiederherstellung zu prüfen.

**Geschätzte Dauer:** 20 bis 60 Minuten pro Gast, zuzüglich umfangreicher Trim- oder Bereinigungsaufgaben. **Schwierigkeit:** Mittel. Beginnen Sie mit einer risikoarmen VM und vergleichen Sie deren Speicherverbrauch vorher und nachher.

> **Warnung:** Ein voller Thin-Pool verursacht E/A-Fehler in Gästen und gefährdet Dateisysteme. Überbelegen Sie den Pool nicht, ohne freien Daten- und Metadatenspeicher zu überwachen. [Proxmox-Speicherdokumentation](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Der Belegungskette folgen

**Löschen**, **Discard** und **Speicherfreigabe** finden auf unterschiedlichen Ebenen statt. Ein Gast löscht eine Datei und markiert Dateisystemblöcke als frei. Das Dateisystem sendet TRIM oder UNMAP für diese Blöcke. QEMU leitet die Anforderung weiter, wenn Discard für den virtuellen Datenträger aktiv ist. Das Backend gibt physische Belegung frei, wenn Format und Pool den Vorgang unterstützen. [Proxmox-Dokumentation zu VM-Datenträgern](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Ebene | Zu prüfen | Nützlicher Nachweis |
|---|---|---|
| **Gastdateien** | Freier Dateisystemspeicher | Windows-Volume-Eigenschaften oder Linux `df -h` |
| **Virtueller Datenträger** | Bus, Discard, SSD-Emulation, Imageformat | VM-Register **Hardware** oder `qm config VMID` |
| **PVE-Volume** | Eigentümer und konfigurierte Größe | Register **Content** des Speichers oder `pvesm list STORAGE_ID` |
| **Speicherpool** | Freie Daten, Metadaten und gehaltene Blöcke | `pvesm status` und backend-spezifische Werkzeuge |

**Ein virtueller Datenträger mit 100 GiB ist eine Kapazitätsgrenze, keine Zusage für 100 GiB Belegung.** Umgekehrt beweisen 20 GiB gemeldete Gastnutzung nicht, dass der Host 20 GiB belegt. Metadaten, Snapshots, Sicherungskopien und zuvor geschriebene Blöcke verändern den Wert. [Proxmox-Speicherdokumentation](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Datenträgerformate vergleichen

**Das Speicher-Backend bestimmt, welche Imageformate Proxmox anbietet.** ZFS-zvols und Ceph RBD verwenden virtuelle raw-Datenträger. LVM nutzt normalerweise raw, mit einer weiter unten beschriebenen Proxmox VE 9-Ausnahme für Volume-Ketten. Datei-Backends wie directory und NFS unterstützen raw oder qcow2. Raw bietet selbst weder Thin-Belegung noch Snapshots. Der zugrunde liegende Speicher muss diese Funktionen bereitstellen. Qcow2 bietet Copy-on-Write-Belegung und Snapshots auf Image-Ebene. [Proxmox-Dokumentation zu VM-Datenträgern](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Belegungsmechanismus | Speicherkompromiss |
|---|---|---|
| **qcow2 auf Dateispeicher** | Qcow2 belegt Cluster beim Schreiben | Image-Metadaten und Snapshot-Ketten verbrauchen Speicher |
| **raw-Datei auf Dateispeicher** | Sparse-Dateien des Dateisystems, sofern unterstützt | Raw allein bietet weder Thin Provisioning noch Snapshots |
| **raw-Blockvolume** | LVM thin, ZFS, Ceph RBD oder ein anderes Backend | Pool-Belegung und Snapshots hängen vom Backend ab |

**Proxmox VE 9 thick LVM besitzt einen speziellen Snapshot-Modus.** `snapshot-as-volume-chain` verwendet qcow2-Backing-Beziehungen zwischen thick-LVM-Logical-Volumes. Es verwendet keine internen qcow2-Snapshots. Die Option betrifft nur neu erstellte VM-Datenträger und gilt in der aktuellen Proxmox-Dokumentation als Technologie-Vorschau. PVE zeigt jeden Snapshot als vollständig belegt an. Die tatsächliche SAN-Belegung ist nur kleiner, wenn das Backend Thin Provisioning und Discard unterstützt. [Proxmox-Dokumentation zum LVM-Speicher](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Konvertieren Sie einen Datenträger nicht allein wegen der Endung `.raw`.** Prüfen Sie zuerst das Speicher-Plugin und dessen belegte Blöcke. Ein raw-Datenträger auf `local-lvm` wird anders belegt als eine vollständig belegte raw-Datei auf normalem directory-Speicher.

## Speichertypen vergleichen

Proxmox trennt **Dateispeicher** von **Blockspeicher**. Das Speicher-Plugin steuert auch Snapshots, Klone, Freigaben und zulässige Inhaltstypen des Pools. Prüfen Sie den Eintrag **Datacenter > Storage**, bevor Sie sich auf ein Format oder eine Funktion verlassen. [Tabelle der Proxmox-Speichertypen](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Speicher | Verhalten des VM-Datenträgers | Prüfung der Freigabe |
|---|---|---|
| **Directory, ext4, XFS** | raw- oder qcow2-Dateien | Vergleichen Sie von `du` belegte Bytes mit der virtuellen Imagegröße. Prüfen Sie Snapshots, falls eine andere Speicherebene sie bereitstellt. |
| **NFS, CIFS** | raw- oder qcow2-Dateien auf gemeinsamem Speicher | Prüfen Sie den belegten Speicher auf dem Server. Ein Trim-Ergebnis im Gast beweist keine Freigabe auf dem Server. |
| **LVM mit dünner Bereitstellung (`local-lvm`)** | Lokale raw-Thin-Logical-Volumes | Überwachen Sie mit `lvs` die Daten- und Metadatenprozente des Thin-Pools. |
| **LVM thick** | raw-LVs oder VE 9 qcow2-Volume-Ketten | Das Löschen im Gast senkt die feste LV-Reservierung nicht. Prüfen Sie Thin-Belegung der SAN separat. |
| **ZFS-Speicher (`local-zfs`)** | raw-zvols oder Container-Subvolumes | Prüfen Sie `sparse`, Dataset-Eigenschaften, Pool-Belegung und Snapshots. |
| **Ceph RBD** | Thin-raw-RBD-Images auf gemeinsamem Speicher | Prüfen Sie Ceph-Poolkapazität, Image-Nutzung, Snapshots und Discard. |
| **Btrfs** | Datei-Volumes mit Btrfs-Subvolumes für raw-Images | Behandeln Sie das PVE-Btrfs-Plugin als Technologie-Vorschau und prüfen Sie Snapshots und Dateisystemnutzung. |

**Andere Speicher-Plugins erfüllen andere Aufgaben.** CephFS bietet gemeinsamen Dateispeicher. iSCSI und Fibre Channel stellen gemeinsam genutzte Blockgeräte bereit, oft mit LVM in VM-Volumes unterteilt. ZFS over iSCSI nutzt entfernten, von ZFS gestützten Blockspeicher. Proxmox Backup Server (PBS) speichert Sicherungen, keine aktiven VM-Datenträger. Prüfen Sie die aktivierten **Content**-Typen, bevor Sie `images`, `rootdir`, `backup` oder `iso` dort ablegen. [Tabelle der Proxmox-Speichertypen](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Belegungsoptionen für Dateispeicher sind beim Erstellen wichtig.** Der Speicherwert `format` wählt bei Unterstützung `raw`, `qcow2` oder `vmdk`. `preallocation` für raw- und qcow2-Dateien akzeptiert `off`, `metadata`, `falloc` oder `full`. Standard ist `metadata`, für raw als `off` behandelt. `full` reserviert den Dateispeicher im Voraus und verhindert den üblich kleinen Anfangsbedarf. Prüfen Sie die Speicherkonfiguration, bevor Sie einen großen Datenträger anlegen. Die Option `shared` deklariert nur einen bestehenden gemeinsamen Zugriff. Sie macht lokalen Speicher nicht gemeinsam nutzbar. [Allgemeine Proxmox-Speichereigenschaften](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` steuert die Erstellung dünn belegter zvols.** Ohne sparse-zvols reserviert die Erstellung Kapazität gemäß der konfigurierten Volume-Eigenschaft. Prüfen Sie die tatsächliche Speicherkonfiguration und den Pool, bevor Sie eine bestehende Umgebung ändern. [Proxmox-Dokumentation zum ZFS-Speicher](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory-Speicher erfordert eine zweite Prüfung.** Die logische Länge einer qcow2-Datei ist nicht ihre für den Gast sichtbare virtuelle Kapazität. `du -h` meldet dem Image zugeordnete Dateisystemblöcke. `ls -lh` zeigt die logische Dateilänge. Für eine angehaltene VM meldet `qemu-img info` virtuelle Kapazität und Host-Diskgröße. Bei NFS verwenden Sie für endgültige Kapazitätsentscheidungen die Abrechnung des Servers. [QEMU-Referenz zu `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS hat eine weitere Belegungsgrenze.** Dass qcow2 einen leeren Cluster in seiner Datei wiederverwendet, bedeutet nicht, dass der NFS-Server Dateiblöcke freigibt. Hole Punching erfordert Unterstützung durch Client, ausgehandeltes Protokoll, Server und dessen Dateisystem. NFSv4.2 definiert `DEALLOCATE`, aber eine Versionsnummer beweist nicht, dass der Server Speicher zurückgegeben hat. Prüfen Sie den ausgehandelten NFS-Mount und messen Sie die Belegung auf dem Server. [NFSv4.2-Spezifikation `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Optionen für VM-Datenträger festlegen

Öffnen Sie in der Proxmox-Oberfläche **VM > Hardware > Hard Disk > Edit**. Prüfen Sie den Disk-Bus und erweiterte Optionen. Die Flags beeinflussen die Belegung oder bestimmen, ob eine Optimierung sinnvoll ist. Die [offizielle Referenz der `qm`-Optionen](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) nennt die Verfügbarkeit je Bus.

| Bus | Speicherbezogene Wahl |
|---|---|
| **IDE** | Ältere Kompatibilität. Nur verwenden, wenn dem Gast ein neuerer Treiber fehlt. |
| **SATA** | Weit unterstützte Emulation. Prüfen Sie Gast-Trim und Disk-Optionen, bevor Sie auf Freigabe setzen. |
| **SCSI mit VirtIO SCSI** | Empfohlener moderner Pfad für Discard und Disk-Einstellungen. Windows benötigt den VirtIO-Treiber. |
| **VirtIO Block** | Paravirtualisierter Datenträger. Linux-Discard erfordert Kernel 5.0 oder neuer. SSD-Emulation fehlt. |

| Einstellung | Wirkung | Empfehlung |
|---|---|---|
| **Discard weiterleiten (`on`)** | Leitet TRIM oder UNMAP des Gasts weiter | Erforderlich für Gast-gesteuerte Freigabe auf einem unterstützten Thin-Backend. Der Standardwert `ignore` blockiert die Weiterleitung. |
| **SSD-Emulation `ssd=1`** | Meldet dem Gast den Datenträger als SSD | Manche Gäste benötigen diese Kennung vor Trim. Das Flag macht physischen Speicher nicht schneller. VirtIO Block bietet es nicht. |
| **Detect zeroes `detect_zeroes=1`** | Erkennt und optimiert nach Möglichkeit Null-Schreibvorgänge | Optionale E/A-Optimierung. Ersetzt Gast-Trim nicht und garantiert keine Freigabe. |
| **Bus: SCSI / VirtIO SCSI single** | Stellt einen SCSI-Datenträger über den VirtIO-Controller bereit | Praktischer Standard für moderne Windows- und Linux-Gäste. Installieren Sie Windows-VirtIO-Treiber. |
| **Bus: VirtIO Block** | Verwendet das VirtIO-Blockgerät | Linux-Discard erfordert Kernel 5.0 oder neuer. SSD-Emulation fehlt. |
| **E/A-Thread `iothread=1`** | Weist Laufwerks-E/A einem separaten Thread zu | Mit VirtIO Block oder SCSI an einem VirtIO SCSI single-Controller verwenden. Leistungsoption, kein Freigabe-Flag. |
| **Cache und AIO** | Ändern E/A-Pufferung und asynchrone E/A | An Workload und Backend anpassen. Keine Einstellung verkleinert einen Datenträger. |
| **Backup `backup=0`** | Schließt den Datenträger von VM-Sicherungen aus | Verkleinert den Sicherungsumfang und entfernt die Daten aus der VM-Wiederherstellung. Separate Sicherung dokumentieren. |
| **Replikation `replicate=0`** | Schließt den Datenträger von Speicherreplikation aus | Reduziert replizierte Daten und entfernt den Datenträger aus der Replik. |

**Andere Laufwerksoptionen beschreiben Verhalten statt Speicherfreigabe.** `format` gilt beim Anlegen auf einem Backend mit mehreren Imageformaten. `size` ist virtuelle Kapazität, nicht belegte Bytes. `ro=1` setzt den Datenträger auf schreibgeschützt. `snapshot=1` aktiviert QEMUs temporären Snapshot-Modus, der Änderungen beim Herunterfahren der VM verwirft. Damit wird kein Datenträger in Proxmox-VM-Snapshots aufgenommen. Nicht für persistente Daten verwenden. Prüfen Sie die Wiederherstellungsabdeckung vor `backup=0` oder `replicate=0`. [Proxmox-VM-Disk-Optionen](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Fügen Sie keine verkürzte `qm set --scsi0`-Zeile über einem vorhandenen Laufwerk ein.** Prüfen Sie **`qm config VMID`** und behalten Sie beim Bearbeiten die vollständige Volume-ID und vorhandene Optionen bei. Eine verkürzte Zuweisung kann weitere Disk-Einstellungen löschen. Prüfen Sie in der Oberfläche nach jeder Änderung die gespeicherten Disk-Optionen.

```bash
qm config 100
pvesm status
```

`100` ist eine Beispiel-VM-ID. Für einen **neuen** 64-GiB-SCSI-Datenträger auf einer vorhandenen VM mit Controller **VirtIO SCSI single** und erforderlichem Gasttreiber zeigt dieser Befehl die Zuweisungssyntax. Ersetzen Sie VM- und Speicher-ID durch Ihre Werte.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Prüfen Sie vor dem Beispiel, ob `scsi0` schon existiert.** Der Befehl ändert diesen Slot. Verwenden Sie bei einer vorhandenen Disk die Oberfläche, wenn sich damit die genaue Optionszeichenfolge leichter bewahren lässt. Siehe die [Proxmox-Referenz zum Befehl `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Dateien im Gastsystem bereinigen

**Geben Sie zuerst Gastdateien frei.** Prüfen Sie Windows-Speichereinstellungen, temporäre Dateien, alte Installationsprogramme, Anwendungscaches und Papierkorb. Bereinigen Sie Datenbanken und Container-Runtimes über deren eigene Oberfläche. Aktive Anwendungsdaten nur zur Verringerung der Belegung zu löschen, riskiert Datenverlust.

**Bestätigen Sie einen discard-fähigen virtuellen Datenträger für das Volume** und öffnen Sie eine PowerShell-Sitzung mit erhöhten Rechten in der Windows-VM:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` bedeutet, dass Windows Löschbenachrichtigungen für das gemeldete Dateisystem aktiviert hat. **ReTrim** sendet Trim-Anforderungen für derzeit ungenutzte Volume-Bereiche erneut. Ein erfolgreicher Befehl bestätigt, dass der Gast den Vorgang gesendet hat, nicht die Zahl der auf dem Host freigegebenen Bytes. Prüfen Sie den Host nach Abschluss. [Microsoft-Referenz zu `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) und [Proxmox-Dokumentation zu VM-Datenträgern](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Verwechseln Sie QEMU guest agent nicht mit TRIM.** Der Agent unterstützt Gaststeuerung und Sicherungskonsistenz. Dateisystem-Löschbenachrichtigungen laufen über den virtuellen Datenträger. Die Installation des Agents allein gibt keine Blöcke frei. [Proxmox-Dokumentation zum VM-Gast-Agent](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Nicht genutzte Blöcke im Gastsystem melden

**Prüfen Sie vor Trim den Blockpfad und das Dateisystem.** Eine moderne Distribution führt häufig regelmäßig `fstrim.timer` aus. Prüfen Sie dessen Status und trimmen Sie nach dem Löschen unnötiger Gastdaten die eingehängten Dateisysteme.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** meldet Discard-Granularität und -Grenzwerte sichtbarer Blockgeräte. **`fstrim -av`** trimmt unterstützte eingehängte Dateisysteme und meldet gesendete Bereiche. Gesendete Bytes entsprechen nicht den an den Pool zurückgegebenen Bytes. Verschlüsselte, LVM-, RAID- und andere gestapelte Geräte benötigen Discard-Unterstützung auf jeder Ebene. [Red-Hat-Anleitung zu ungenutzten Blöcken](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Verwenden Sie geplantes Trim oder eine gezielte Online-Discard-Richtlinie. **Aktivieren Sie nicht pauschal kontinuierliches `discard` auf jedem Dateisystem, statt den Speicherpfad zu prüfen.** Prüfen Sie nach dem Trim des Gasts PVE-Volume und -Pool. Prüfen Sie bei weiterhin belegten Datenbanken auch deren eigene Komprimierungsrichtlinie.

## Containerspeicher separat prüfen

**LXC hat für sein Root-Dateisystem keinen emulierten VM-Disk-Bus.** Starten Sie mit `pct config CTID` und ermitteln Sie jeden `rootfs`- und `mpN`-Eintrag. Proxmox unterscheidet speichergestützte Mounts, Bind-Mounts und Geräte-Mounts. Ein Pfad im Container verrät nicht, welchem Hostvolume dessen Blöcke gehören. [Proxmox-Einhängepunkte für Container](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Entfernen Sie bei einem **verwalteten rootfs oder Mount-Point** Dateien im Container oder in dessen Anwendung und prüfen Sie dann Host-Volume und Snapshots. **Führen Sie keine VM-`qm`-Discard-Befehle gegen einen CT aus.** Auf ZFS-Subvolumes behalten Snapshots gelöschte Blöcke. Prüfen Sie bei directory und LVM thin die tatsächliche Backend-Belegung statt der konfigurierten CT-Größe.

Führen Sie **`pct fstrim` auf dem Proxmox-Host** nach der CT-Bereinigung aus, wenn das Backend Discard unterstützt. Proxmox trimmt das CT-rootfs und geeignete verwaltete Mount-Points. Bind-Mounts und schreibgeschützte Mount-Points werden übersprungen. Verwenden Sie `--ignore-mountpoints`, um nur das rootfs zu trimmen. Vergleichen Sie die Speicherbelegung vorher und nachher. [Proxmox-Referenz zu `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Die Befehle zeigen **alternative Umfänge** für die Beispiel-CT-ID `101`. Führen Sie den Umfang aus, der zu Ihrem Speicherlayout passt. Erfolgreiches Trim gibt nicht zwingend gleich viele Bytes frei, wenn Snapshots alte Blöcke halten.

**Bind- und Geräte-Mounts verwaltet Proxmox nicht.** Ihre Quelldaten bleiben auf dem Host oder externen Gerät. `vzdump`-Sicherungen des Containers schließen deren Inhalte aus. Zusätzliche speichergestützte Mount-Points sind standardmäßig ebenfalls ausgeschlossen, sofern ihre `backup`-Option sie nicht einschließt. Prüfen Sie die tatsächliche Sicherungsrichtlinie vor der Bereinigung. [Proxmox-Sicherungsdokumentation](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Bei verschachteltem Docker prüfen Sie Image-Layer, Volumes und Protokolle beim tatsächlichen Speicherinhaber, bevor Sie Docker-Bereinigungsbefehle verwenden. Der [Zuverlässigkeitsleitfaden für Docker in LXC](/articles/docker-in-lxc-proxmox-reliability/) beschreibt Mount- und Sicherungsgrenzen. Ein gelöschtes Container-Image entfernt standardmäßig kein persistentes Volume.

## Messwerte des Servers erfassen

**Erheben Sie vor und nach der Bereinigung dieselben Messwerte.** Der freie Speicherplatz des Pools zeigt die endgültige Kapazität. Werte je Volume helfen, den für das Wachstum verantwortlichen Gast zu finden.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventarisiert verwaltete Volumes und konfigurierte Größen. Es misst keine zugewiesenen Bytes in Thin-Speicher. Prüfen Sie bei **directory** den exakten Mountpfad und ein bekanntes Image. Ersetzen Sie die Pfade mit den Werten aus **Datacenter > Storage** und der VM-Konfiguration.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Vergleichen Sie bei einer **angehaltenen VM** virtuelle Kapazität und Host-Belegung des Images, ohne die Datei zu ändern:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Überwachen Sie bei **LVM thin** Daten und Metadaten des Pools:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Trennen Sie bei **ZFS** aktive Dataset-Daten von Snapshot-Daten:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** meldet die über alle Snapshots eines Datasets gehaltenen Blöcke. Snapshot-`used`-Werte lassen sich nicht addieren, weil Snapshots Blöcke gemeinsam nutzen. Gelöschte Dateien können den Pool unverändert lassen, bis jeder Snapshot mit Verweisen auf ihre Blöcke gemäß der Aufbewahrungsrichtlinie abläuft oder gelöscht wird. [OpenZFS-Snapshots und Klone](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Ordnen Sie bei **Ceph RBD** zuerst die Proxmox-Volume-ID zu. **`qm config VMID`** zeigt `STORAGE_ID:IMAGE`. Öffnen Sie den RBD-Eintrag unter **Datacenter > Storage**, um **Pool** und optionalen **Namespace** zu finden. Speicher-ID und Poolname müssen nicht übereinstimmen. Erstellen Sie `POOL/IMAGE` aus Pool- und Imagewert. Führen Sie die Befehle auf einem Client aus, der für den gewünschten Ceph-Cluster konfiguriert ist und gültige Zugangsdaten hat. [Proxmox-Dokumentation zum RBD-Speicher](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** meldet bereitgestellte und tatsächliche Image-Nutzung einschließlich zugehöriger Snapshots. Ohne die Image-Funktion `fast-diff` fragt es OSDs nach möglichen Objekten ab und benötigt mehr Arbeit. **`ceph df`** zeigt Pool- und Clusterkapazität. Replikation, Erasure Coding und Snapshots verändern die Brutto-Clusterbelegung, daher unterscheiden sich Image- und Pool-Bytes. [Ceph-RBD-Befehlsreferenz](https://docs.ceph.com/en/squid/man/8/rbd/) und [Ceph-Anleitung zur Poolnutzung](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Verwendet der RBD-Speicher einen Namespace, ergänzen Sie jeden `rbd`-Befehl um **`--namespace NAMESPACE`**. Verwenden Sie den in Proxmox konfigurierten Namespace, nicht die Proxmox-Speicher-ID.

## Schnappschüsse und Sicherungen berücksichtigen

**Snapshots bewahren ältere Blockversionen.** Wenn die Belegung nach Trim nicht sinkt, prüfen Sie den Tab **Snapshots** der VM oder des CT und den Snapshot-Bestand des Backends. Ermitteln Sie Eigentümer und Abhängigkeiten vor dem Löschen. Eine Sicherung ist eine separate Kopie und folgt der Aufbewahrung des Sicherungsspeichers, nicht dem aktuellen Gast-`df`.

**PBS-Deduplizierung verändert die Abrechnung.** Der Datastore enthält Chunks, die Sicherungen gemeinsam verwenden. Pruning entfernt Snapshot-Metadaten der Sicherung. Garbage Collection löscht später nicht referenzierte Chunks, nach einer Karenzzeit. Prüfen Sie beide Aufgaben, bevor Sie freigegebenen Sicherungsspeicher melden. [PBS-Wartungsdokumentation](https://pbs.proxmox.com/docs/maintenance.html)

> **Warnung:** Löschen Sie niemals eine von Proxmox verwaltete Volume-Datei, ein zvol oder einen Snapshot allein anhand des Namens. Ermitteln Sie zuerst Gast und Aufbewahrungsrichtlinie. Eine Speicherbereinigung muss Sicherung und Rücksetzpfad bewahren.

## Datenträgerabbild bei ausgeschalteter VM neu erstellen

**Verwenden Sie eine Offline-Konvertierung nur, wenn normales Gast-Trim und der Backend-Pfad ein qcow2-Belegungsproblem nicht lösen.** Fahren Sie die VM herunter, prüfen Sie ihre Sicherung, ermitteln Sie alle Snapshot- und Backing-Chain-Beziehungen und schreiben Sie in ein separates Zielimage. QEMU warnt davor, ein von einem anderen Prozess verwendetes Image zu ändern. [QEMU-Dokumentation zu `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Bevorzugen Sie einen von Proxmox verwalteten Umzug oder den Sicherungs- und Wiederherstellungsablauf**, wenn der Datenträger Snapshots hat oder auf verwaltetem Blockspeicher liegt. Ein eigenständiges `qemu-img convert` für ein PVE-eigenes Image aktualisiert VM-Konfiguration, Volume-Eigentümer und Snapshot-Verweise nicht selbst. Verwenden Sie nicht `qemu-img resize --shrink`, um gelöschte Dateien zurückzugewinnen. Die für den Gast sichtbare Kapazität zu verringern riskiert Daten abzuschneiden, wenn Partitionen und Dateisysteme nicht zuerst verkleinert wurden.

## Fehlgeschlagene Freigabe beheben

| Symptom | Wahrscheinliche Prüfung | Nächster Schritt |
|---|---|---|
| **Gast-`df` sinkt, Host bleibt gleich** | VM-Discard-Flag, Gast-Trim, Snapshots | Prüfen Sie den kompletten Discard-Pfad und gehaltene Snapshots. |
| **`fstrim` meldet nicht unterstützt** | Gast-Disk-Bus, gestapelte Blockgeräte, Backend | Prüfen Sie `lsblk -D`, Gast-Kernel und jede Zwischenschicht. |
| **Windows ReTrim endet, Host bleibt gleich** | Backend-Belegung, Snapshots, Serverabrechnung | Vergleichen Sie Volume und Pool. Bestätigen Sie Thin-Speicher für den Datenträger. |
| **`ls -lh` und `du -h` weichen ab** | Sparse- oder qcow2-Datei | Verwenden Sie `du` für die belegten Dateisystemblöcke. |
| **LVM-Thin-Pool bleibt stark belegt** | Daten, Metadaten, Snapshots | Prüfen Sie `lvs` und PVE-Snapshots vor dem Löschen. |
| **ZFS-Pool bleibt stark belegt** | Snapshot-Blöcke und Reservierungen | Prüfen Sie `usedbysnapshots`, zvol-Einstellungen und Poolkapazität. |
| **CT-`df` und Pool widersprechen sich** | Bind-Mounts, Mount-Points, Snapshots | Ordnen Sie `rootfs` und jedes `mpN` dem Host-Eigentümer zu. |

**Prüfen Sie nach Abschluss der Hintergrundaufgaben erneut.** Die Speicherabrechnung kann nach Trim, Snapshot-Löschung oder Backend-Garbage-Collection verzögert sein. Vergleichen Sie den gemessenen freien Pool-Speicher mit dem Ausgangswert. Leiten Sie Erfolg nicht allein aus dem Exitcode eines Gastbefehls ab.

## Nächste Schritte

**Führen Sie für jeden Gast einen Speichernachweis:** virtuelle Größe, belegte Bytes, Backend, Bus, Discard-Flag, Snapshot-Anzahl, Sicherungsabdeckung und freier Pool-Speicher. Wählen Sie eine VM, aktivieren Sie den unterstützten Discard-Pfad, trimmen Sie im Gast und vergleichen Sie die Werte. Wiederholen Sie den Vorgang erst, wenn das Ergebnis dem erwarteten Backend-Verhalten entspricht.

Für eine breitere Wiederherstellungsplanung nutzen Sie den [Proxmox-Sicherungs- und Wiederherstellungstest](/articles/proxmox-vm-backup-restore-drill/) und die [Anleitung zum Upgrade von Proxmox VE 8 auf 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Quellen

- [Proxmox VE-Speicherverwaltung](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), Speichertypen, Thin Provisioning und Kapazitätsrisiken.
- [Proxmox VE LVM-Speicher](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9 Snapshot-Volume-Ketten und Belegung.
- [Proxmox VE RBD-Speicher](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), Pool- und Namespace-Konfiguration.
- [Proxmox VE virtuelle Maschinen](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), Disk-Busse, Formate, Discard und Gast-Agent.
- [Proxmox VE VM-Disk-Optionen](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), Bus-spezifische Flags.
- [Proxmox VE Container](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), Root-Dateisysteme und Eigentum von Mount-Points.
- [Proxmox VE Containerbefehle](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), Container-Trim vom Host.
- [Proxmox VE Sicherung und Wiederherstellung](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), VM- und CT-Sicherungsumfang.
- [Microsoft-Dokumentation zum Cmdlet `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows-ReTrim-Syntax.
- [Red-Hat-Anleitung zu ungenutzten Blöcken](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux-`fstrim`-Verhalten.
- [OpenZFS-Snapshots und Klone](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), durch Snapshots gehaltene Blöcke.
- [Ceph-RBD-Befehlsreferenz](https://docs.ceph.com/en/squid/man/8/rbd/), Image-Nutzung und Snapshots.
- [NFSv4.2-Spezifikation](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), Speicherfreigabe auf dem Server.
- [PBS-Wartungsdokumentation](https://pbs.proxmox.com/docs/maintenance.html), Pruning und Garbage Collection.
- [QEMU-Disk-Image-Werkzeug](https://www.qemu.org/docs/master/tools/qemu-img.html), sichere Offline-Image-Konvertierung.
