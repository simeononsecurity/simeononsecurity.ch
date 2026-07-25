---
title: "Proxmox VE 8 auf 9 Upgrade-Anleitung: In-Place-Upgrade mit automatisiertem Skript"
date: 2026-07-22
lastmod: 2026-07-22
toc: true
draft: false
description: "Vollständige Anleitung zum Upgrade von Proxmox VE 8 (Debian Bookworm) auf Proxmox VE 9 (Debian Trixie). Behandelt Voraussetzungen, schrittweises manuelles Upgrade, das Automatisierungsskript pve8to9-upgrade.sh, grundlegende Änderungen und bekannte Probleme."
genre: ["Virtualisierung", "Linux-Administration", "Proxmox", "Serververwaltung", "Open Source", "Homelab"]
tags: ["Proxmox VE 9", "Proxmox Upgrade", "PVE 8 auf 9", "Debian Trixie", "Debian 13", "apt Dist-Upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "LVM Upgrade", "ZFS Upgrade", "NVIDIA vGPU", "cgroupv2", "Proxmox Automatisierung", "Bash Upgrade Skript", "Proxmox Cluster Upgrade", "In-Place-Upgrade", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Ein moderner Serverraum mit leuchtenden Symbolen virtueller Maschinen auf Bildschirmen. Ein Techniker arbeitet an einem Laptop, umgeben von dunkelblauer Ausstattung mit kräftigen blauen, grünen und lila Akzenten."
coverCaption: "Proxmox VE 8 auf 9 upgraden: schrittweises In-Place-Upgrade mit einem automatisierten Hilfsskript."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9 basiert auf Debian 13 Trixie und wird mit Kernel 6.14, QEMU 10, LXC 6 und ZFS 2.3 ausgeliefert.** Diese Anleitung behandelt sowohl den manuellen In-Place-Upgrade-Pfad als auch ein automatisiertes Bash-Skript, das Ihre Konfiguration erkennt und alle Repository-Änderungen, bekannten Probleme und Vorab-Prüfungen erledigt.

## Was ist neu in Proxmox VE 9

Proxmox VE 9 (veröffentlicht August 2025) ist ein großes Versions-Upgrade. Wichtige Änderungen:

| Komponente | PVE 8 | PVE 9 |
|-----------|--------|--------|
| **Debian-Basis** | Bookworm (12) | Trixie (13) |
| **Standardkernel** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (erforderlich) / Tentacle (optional) |
| **cgroup** | cgroupv2 (v1 noch möglich) | nur cgroupv2 |

**Wichtige neue Funktionen in PVE 9.0+:**
- VM-Snapshots auf dick bereitgestellten LVM über Volume-Ketten (Technologievorschau in 9.1 als Produktion)
- Hochverfügbarkeits-Affinitätsregeln ersetzen HA-Gruppen
- SDN Fabrics für OpenFabric und OSPF Full-Mesh-Ceph-Netzwerke
- Neue mobile Weboberfläche (Rust/Yew)
- ZFS RAIDZ-Geräteerweiterung ohne Ausfallzeit
- Dynamischer Lastausgleich mit dem Cluster Resource Scheduler (PVE 9.2)
- WireGuard und BGP als SDN-Fabric-Protokolle (PVE 9.2)
- `/tmp` ist jetzt ein `tmpfs` (Debian Trixie-Änderung: Dateien werden regelmäßig bereinigt)

______

## Vor dem Start: Voraussetzungen

**Sie müssen alle diese Punkte erfüllen, bevor Sie Repositories ändern.** Siehe die vollständige Checkliste der Voraussetzungen im [offiziellen Upgrade-Wiki](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 mindestens

```bash
pveversion
```

Die Ausgabe muss `pve-manager/8.4.x` oder höher anzeigen. Falls nicht:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph muss bei Squid (19.x) sein (nur Hyper-Converged)

```bash
ceph --version
```

Die Ausgabe muss Version 19.x (Squid) anzeigen. Wenn Sie auf Reef (18.x) oder Quincy (17.x) sind, upgraden Sie zuerst Ceph. Der Upgrade-Pfad erfolgt immer Schritt für Schritt:

- Quincy (17) → Reef (18) → Squid (19)

*Fahren Sie mit dem PVE 9-Upgrade erst fort, wenn alle Ceph-Knoten auf Squid sind.*

### 3. Co-installierter Proxmox Backup Server

Wenn PBS auf demselben Knoten installiert ist, upgraden Sie PBS 3 → 4, bevor Sie die PVE-Repositories anfassen. Führen Sie `pbs3to4 --full` aus und beheben Sie alle Probleme zuerst.

### 4. Zugriffsanforderungen

- **Bevorzugt**: Konsolenzugang über IPMI, iKVM oder physische Tastatur. Die SSH-Sitzung wird beim Neustart von Diensten unterbrochen.
- **SSH**: Verwenden Sie `tmux` oder `screen`, damit das Upgrade bei einem Verbindungsabbruch weiterläuft:
  ```bash
  tmux new -s upgrade
  ```

### 5. Festplattenspeicher

```bash
df -h /
```

Mindestens **5 GB frei**, idealerweise 10+ GB.

### 6. Gültige Backups

Sichern Sie alle VMs und Container auf externen Speicher, bevor Sie fortfahren. Testen Sie eine Wiederherstellung. Ein gültiges Backup ist keine Option.

______

## Grundlegende Änderungen, die Sie kennen müssen

Lesen Sie diese vor dem Upgrade. Mehrere erfordern Maßnahmen vor oder nach dem Upgrade.

### cgroup V1 ist weg

PVE 9 unterstützt die veraltete cgroupv1-Umgebung überhaupt nicht mehr. Wenn Sie diese zuvor aktiviert hatten:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Wenn das etwas zurückgibt, entfernen Sie den Kernel-Parameter aus `/etc/default/grub` und führen Sie `update-grub` vor dem Upgrade aus.

**Auswirkung auf Container**: Container, die systemd 230 oder älter ausführen (CentOS 7, Ubuntu 16.04), starten unter PVE 9 nicht. Migrieren Sie diese Workloads während des PVE 8-Supportfensters (EOL Juli 2026).

### HA-Gruppen veraltet

HA-Gruppen werden durch HA-Regeln ersetzt. Sie migrieren automatisch, sobald alle Clusterknoten auf PVE 9 sind. Keine manuelle Aktion erforderlich, aber nach dem Upgrade des letzten Knotens überprüfen.

### VM.Monitor-Berechtigung entfernt

Benutzerdefinierte Rollen, die auf `VM.Monitor` verwiesen haben, müssen aktualisiert werden. Verwenden Sie stattdessen `Sys.Audit` für grundlegenden KVM-Monitor-Zugriff. Das `pve8to9`-Skript erkennt betroffene Rollen.

### Neue Berechtigung: VM.Replicate

Das Erstellen oder Bearbeiten von Speicherreplikationsjobs erfordert jetzt `VM.Replicate` für `/vms/<vmid>`. Benutzerdefinierte Rollen bei Bedarf anpassen.

### Privilegierte LXC-Container erfordern Sys.Modify

Das Erstellen neuer privilegierter Container erfordert jetzt `Sys.Modify`. Das Wiederherstellen eines vorhandenen privilegierten Containers an Ort und Stelle hingegen nicht.

### systemd-sysctl liest /etc/sysctl.conf nicht mehr

Benutzerdefinierte Einstellungen in `/etc/sysctl.conf` werden nach dem Upgrade stillschweigend ignoriert. Migrieren Sie diese vor dem Neustart nach `/etc/sysctl.d/<NN>-name.conf`.

```bash
# Prüfen, was in sysctl.conf steht
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp ist jetzt tmpfs

Debian Trixie hängt `/tmp` als tmpfs ein (bis zu 50 % des RAM). Dateien werden regelmäßig bereinigt, während das System läuft. Wenn Sie `/tmp` für große temporäre Dateien verwenden, verschieben Sie diese Arbeit nach `/var/tmp` oder einen dedizierten Einhängepunkt.

### Veeam Backup für QEMU-Maschinenversion >= 10.0 defekt

Proxmox hat geändert, wie Datenträger für Maschinenversion 10.0+ intern an QEMU angehängt werden. Veeam hat sich noch nicht angepasst. Entweder fixieren Sie betroffene VMs vor dem Upgrade auf Maschinenversion `9.2+pve1`, oder verschieben Sie das Upgrade, wenn Veeam kritisch ist.

### Netzwerkschnittstellennamen können sich ändern

Kernel 6.14 erkennt mehr NIC-Funktionen als 6.8. Einige NICs erhalten zusätzliche Benennungssuffixe. Das Tool `pve-network-interface-pinning` kann alle Schnittstellen vor dem Upgrade auf stabile `nicX`-Namen fixieren:

```bash
pve-network-interface-pinning --help
```

______

## Option A: Manuelles In-Place-Upgrade

Folgen Sie den offiziellen Schritten von [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Schritt 1: Führen Sie die pve8to9-Checkliste aus

```bash
pve8to9 --full
```

Beheben Sie jeden `FAIL`-Punkt, bevor Sie fortfahren. Führen Sie nach jeder Behebung erneut aus.

### Schritt 2: Laufende VMs migrieren (falls in einem Cluster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Schritt 3: PVE 8 vollständig aktualisieren

```bash
apt update && apt dist-upgrade
pveversion   # muss 8.4.1 oder neuer anzeigen
```

### Schritt 4: Debian-Basis-Repositories aktualisieren

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Kommentieren Sie verbleibende Bookworm-spezifische Repo-Zeilen aus oder entfernen Sie diese.

### Schritt 5: PVE 9-Paket-Repository hinzufügen

**Enterprise (Abonnement erforderlich):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Kein Abonnement:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Überprüfen Sie mit `apt update && apt policy`, dass das neue Repo ohne Fehler erscheint. Dann entfernen oder kommentieren Sie die alte `.list`-Datei aus.

### Schritt 6: Ceph-Repository aktualisieren (nur Hyper-Converged)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Verwenden Sie `http://download.proxmox.com/debian/ceph-squid` mit `pve-no-subscription` für Konfigurationen ohne Abonnement.

### Schritt 7: Paketindex aktualisieren

```bash
apt update
```

Keine Fehler prüfen.

### Schritt 8: Dist-Upgrade ausführen

```bash
apt dist-upgrade
```

Dies dauert je nach Speichergeschwindigkeit 5 bis über 60 Minuten. Während des Upgrades:

- **`/etc/issue`**: aktuelle Version behalten (sicher)
- **`/etc/lvm/lvm.conf`**: Maintainer-Version installieren (empfohlen)
- **`/etc/ssh/sshd_config`**: Maintainer-Version installieren, wenn Sie sie nicht angepasst haben
- **`/etc/default/grub`**: aktuelle Version behalten, wenn Sie sie angepasst haben
- **`/etc/chrony/chrony.conf`**: Maintainer-Version installieren, wenn nicht angepasst

### Schritt 9: Neustart

```bash
reboot
```

Auch wenn Kernel 6.14 bereits als optionaler Kernel auf PVE 8 installiert war, ist ein Neustart erforderlich. Der Kernel wird mit PVE 9-Toolchains neu erstellt.

### Schritt 10: Schritte nach dem Upgrade

```bash
# Browser-Cache leeren: Strg+Umschalt+R (oder ⌘+Alt+R auf macOS)
# Alle Knoten im Cluster prüfen:
pvesh get /nodes

# Für Cluster: HA-Gruppen migrieren automatisch zu HA-Regeln, wenn alle Knoten auf PVE 9 sind
journalctl -eu pve-ha-crm  # auf Fehler prüfen
```

______

## Option B: Automatisiertes Skript (pve8to9-upgrade.sh)

Der manuelle Prozess hat viele bedingte Schritte, die je nach Konfiguration variieren. Das `pve8to9-upgrade.sh`-Skript automatisiert alle davon.

**Skript-Quelle:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Was das Skript tut

Das Skript führt das vollständige Upgrade automatisch durch, einschließlich:

| Erkennung | Aktion |
|-----------|--------|
| Enterprise- vs. No-Subscription-Repos | Verwendet den Repo-Typ, der **aktiv aktiviert** war. Aktiviert kein Enterprise auf No-Sub-Knoten. |
| Ceph-Version | Blockiert bei Quincy oder Reef, zeigt die schrittweise Ceph-Upgrade-Anleitung |
| Ceph-Repo-Typ | Schreibt eine neue `ceph.sources`, die Ihrem vorhandenen Repo-Typ entspricht |
| NVIDIA vGPU-Treiber | Blockiert bei Treiber < 570.158.02 (GRID 18.3 Minimum) |
| NVIDIA GPU Passthrough | Warnt; erstellt Erinnerung für Post-Upgrade-Test |
| CUDA-Repos | Aktualisiert `debian12` → `debian13` in URI-Pfaden |
| systemd-boot Meta-Paket | Entfernt es (behebt Debian Bug #1110177, der dist-upgrade abbricht) |
| Benutzerdefinierte `sysctl.conf`-Einstellungen | Migriert nach `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| FRR post-up-Deadlock | Behebt `/etc/network/interfaces` vor dem Neustart |
| `systemd-journald-audit.socket` | Deaktiviert, um Log-Überflutung während des Upgrades zu verhindern |
| UEFI + LVM grub-Problem | Installiert `grub-efi-amd64` und schreibt ein Cheat-Sheet nach `/root/` |
| Drittanbieter `bookworm`-Repos | Kommentiert diese mit einer Erinnerung zum Aktualisieren aus |
| `linux-image-amd64`-Konflikt | Entfernt es, wenn vorhanden |
| LVM-Autoaktivierung | Führt das Migrationsskript vor und nach dem Upgrade aus |
| Proxmox Backup Server | Führt `pbs3to4 --full`-Prüfung aus; aktualisiert PBS-Repos für Trixie |
| ZFS root | Erkennt und quittiert (keine besondere Aktion erforderlich) |

Alle Änderungen werden vollständig in `/var/log/pve8to9-upgrade-<Zeitstempel>.log` protokolliert. APT-Repo-Backups werden nach `/root/pve8to9-apt-backups/` geschrieben.

### Installation und Verwendung

```bash
# Skript herunterladen
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Ausführbar machen
chmod +x pve8to9-upgrade.sh

# Vor dem Ausführen überprüfen (lesen Sie immer Skripte, bevor Sie sie als root ausführen)
less pve8to9-upgrade.sh
```

**Ausführungsmodi:**

```bash
# Vollständiger interaktiver Modus (empfohlen)
./pve8to9-upgrade.sh

# Alle sicheren, nicht-destruktiven Korrekturen automatisch genehmigen
./pve8to9-upgrade.sh --yes

# Trockenlauf: alle Änderungen anzeigen ohne etwas anzuwenden
./pve8to9-upgrade.sh --dry-run

# pve8to9 --full-Preflight überspringen (nicht empfohlen)
./pve8to9-upgrade.sh --skip-preflight
```

*Innerhalb von `tmux` oder `screen` ausführen, wenn Sie via SSH verbunden sind.*

### Blockierende Sicherheitsprüfungen des Skripts

Das Skript **weigert sich fortzufahren**, wenn eine dieser Bedingungen zutrifft:

- cgroup V1 ist explizit in der Kernel-Kommandozeile aktiviert
- Ceph ist noch bei Quincy (17.x) oder Reef (18.x). Das Skript zeigt die genauen Ceph-Upgrade-Befehle.
- NVIDIA vGPU-Treiber ist unter Version 570 (GRID 18.3)
- PVE-Version ist unter 8.4

Für jedes blockierende Problem druckt das Skript die genauen Befehle, um es zu beheben, bevor es erneut ausgeführt wird.

______

## Bekannte Upgrade-Probleme

### GRUB startet nicht von LVM im UEFI-Modus

**Betroffen**: Systeme mit Root auf LVM, die im UEFI-Modus booten, von PVE 7.x upgegraded

```bash
# Behebung (auf dem Live-System nach dem Upgrade ausführen):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Das `pve8to9-upgrade.sh`-Skript erkennt UEFI+LVM und installiert dies automatisch. Es schreibt auch ein Wiederherstellungs-Cheat-Sheet nach `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Wenn der Knoten bereits bei `grub rescue>` feststeckt** oder "disk 'lvmid/...' not found":

1. PVE-ISO booten → Erweitert → **Rescue Boot**
2. Oder folgen Sie dem [Recover From Grub Failure — LVM-Abschnitt](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) im offiziellen Wiki

### systemd-boot Meta-Paket bricht dist-upgrade ab

Das `systemd-boot`-Meta-Paket wurde auf allen PVE 8.1-8.4 ISO-Systemen automatisch installiert. In Trixie enthält es Hooks, die beim Upgrade anderer Pakete ausgelöst werden und `dist-upgrade` abbrechen können, wenn das ESP nicht eingehängt ist (Debian Bug #1110177).

```bash
# Vor dem dist-upgrade entfernen:
apt remove systemd-boot
# systemd-boot-efi oder systemd-boot-tools NICHT entfernen. Diese bleiben.
```

Das `pve8to9-upgrade.sh`-Skript behandelt dies automatisch.

### PCI-Passthrough manchmal mit Kernel 6.14 defekt

Einige Benutzer berichten, dass VMs mit PCI-Passthrough mit Kernel 6.14 nicht starten. Bei Betroffen:

```bash
# Alten Kernel vorübergehend fixieren:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Ceph Full-Mesh-Setups sperren sich bei Neustart

Wenn Ihre `/etc/network/interfaces` enthält:

```
post-up /usr/bin/systemctl restart frr.service
```

Ändern Sie es zu:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Tun Sie dies **vor dem Neustart**. Das Skript erkennt dieses Muster und behebt es automatisch.

### LVM Thin Pool benötigt Reparatur

Auf einigen Systemen nach dem Upgrade:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Behebung:

```bash
lvconvert --repair pve/data
```

### NVIDIA vGPU Mindest-Treiberversion

Muss mindestens **Treiber 570.158.02** (GRID 18.3) sein, bevor das Upgrade durchgeführt wird. Ältere Treiber sind mit Kernel 6.x inkompatibel.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Cluster-Upgrade-Reihenfolge

Upgraden Sie Knoten einzeln nacheinander. Überprüfen Sie die Gesundheit jedes Knotens, bevor Sie den nächsten beginnen.

```bash
# Cluster-Gesundheit vor jedem Knoten-Upgrade prüfen:
pvecm status
ceph -s   # wenn Ceph bereitgestellt ist
```

**Migrationsregeln während partieller Upgrades:**

- VM/CT von PVE 8 → PVE 9: funktioniert immer
- VM/CT von PVE 9 → PVE 8: generell nicht unterstützt

Nachdem alle Knoten auf PVE 9 sind, migrieren HA-Gruppen automatisch zu HA-Affinitätsregeln. Auf Fehler prüfen:

```bash
journalctl -eu pve-ha-crm
```

______

## Fehlerbehebung

### Upgrade steckt fest / "proxmox-ve würde entfernt"

Wenn Sie sehen:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Ein oder mehrere Pakete können nicht upgegraded werden, weil noch ein Bookworm-Repo konfiguriert ist. Verstreute Bookworm-Einträge finden:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Diese auskommentieren, dann:

```bash
apt update && apt dist-upgrade
```

Falls teilweise abgeschlossen:

```bash
apt -f install
```

### Start nach ZFS-Upgrade schlägt fehl

Wenn Sie ZFS-Root mit Legacy-BIOS-Boot verwenden, siehe [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). Das `proxmox-boot-tool` muss den Boot auf ZFS-Systemen verwalten, nicht GRUB direkt, um ZFS-Feature-Upgrades zu überleben.

______

## Checkliste nach dem Upgrade

Nach dem Neustart jedes Knotens:

- [ ] Browser-Cache leeren (`Strg+Umschalt+R` / `⌘+Alt+R`)
- [ ] `pveversion` zeigt 9.x
- [ ] `uname -r` zeigt 6.14.x oder neuer
- [ ] Alle VMs und CTs starten korrekt
- [ ] Ceph-Gesundheit: `ceph -s` zeigt HEALTH_OK
- [ ] Bei UEFI+LVM: `grubx64.efi`-Mtime ist aktuell prüfen
- [ ] Bei NVIDIA Passthrough: eine Nicht-Produktions-VM testen
- [ ] Drittanbieter-Repos aktualisieren, die während des Upgrades auskommentiert wurden
- [ ] Benutzerdefinierte `/etc/sysctl.conf`-Einstellungen nach `/etc/sysctl.d/` verschieben

______

## Referenzen

1. [Offiziell: Proxmox VE Upgrade von 8 auf 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Offiziell: Upgrade von 8 auf 9 — Voraussetzungen](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [pve8to9-upgrade.sh Automatisierungsskript](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Proxmox VE 9.0 Bekannte Probleme (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Grub-Fehler beheben — LVM "disk not found"-Fehler](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: Legacy-Boot auf Proxmox Boot Tool umstellen](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Ceph Reef auf Squid Upgrade-Anleitung](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Proxmox Netzwerkschnittstellen-Pinning](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Debian 13 Trixie Versionshinweise](https://www.debian.org/releases/trixie/releasenotes)
