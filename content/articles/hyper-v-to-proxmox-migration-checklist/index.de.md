---
title: "Eine Hyper-V-VM zu Proxmox VE migrieren: Reversible Checkliste"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Migrieren Sie eine Hyper-V-VM mit einem Export bei ausgeschalteter Quelle, passender Firmware, importierten Datenträgern, isoliertem Starttest und Rückfallplan zu Proxmox VE."
genre: ["Virtualisierung", "Systemadministration", "Heimlabor"]
tags: ["Wechsel von Hyper-V zu Proxmox", "Umstieg von Hyper-V", "Umstieg auf Proxmox VE", "Einlesen von VHDX", "qm disk import", "VM-Umschaltung", "VM-Export aus Hyper-V", "Windows-VM auf Proxmox", "VirtIO unter Proxmox", "VM-Wiederherstellung", "UEFI-Wechsel", "Hyper-V-Prüfpunkte", "virtuelles TPM", "BitLocker-Wiederherstellung", "Heimlabor-Umzug"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Ein Datenträger überquert eine Brücke von einem blauen zu einem orangefarbenen Serverrack. Ein separater Rückweg und ein Schutzschild markieren das Ziel."
coverCaption: "Lassen Sie die Quell-VM verfügbar, bis der neue Gast seine Umstellungsprüfungen bestanden hat."
---

Ein **Hyper-V-Export** bewahrt die Dateien einer virtuellen Maschine. Proxmox VE benötigt dagegen eine neue Gastkonfiguration und importierte virtuelle VHDX-Datenträger. Eine erfolgreiche Kopie beweist nicht, dass der Gast startet oder Dienste bereitstellt. Diese Checkliste führt eine VM durch einen Export bei ausgeschalteter Quelle, einen kontrollierten Starttest und eine Umstellung mit klarer Rückkehrmöglichkeit.

<!--more-->

## Wichtigste Punkte

- **Quelle dokumentieren:** Erfassen Sie Firmwaregeneration, Datenträgerpfade, Prüfpunkte, Netzwerkeinstellungen und Verschlüsselung vor dem Export.
- **Schreibzugriffe stoppen:** Fahren Sie die Hyper-V-VM vor dem abschließenden Export herunter und lassen Sie sie während des Proxmox-Tests ausgeschaltet.
- **Startpfad anpassen:** Hyper-V Generation 1 verwendet ein klassisches BIOS. Generation 2 verwendet UEFI.
- **Dienst prüfen:** Kontrollieren Sie Daten, Netzwerkzugriff, Sicherungen und Gastzustand, bevor Sie die Quelle außer Betrieb nehmen.

## Vorbereitungen

Planen Sie ein Wartungsfenster und testen Sie den Ablauf zuerst mit einer entbehrlichen VM. Sie benötigen Administratorzugriff auf Hyper-V und Proxmox VE, Speicherplatz für den Export sowie eine geprüfte Sicherung außerhalb der Migrationskopie. Planen Sie genug Zeit ein, um alle virtuellen Datenträger zu übertragen und die Gastanwendung zu testen. Datenträgergröße und Übertragungsgeschwindigkeit bestimmen die Ausfallzeit.

Dieses Verfahren gilt für eine übliche VM mit virtuellen Datenträgern. **Abgeschirmte VMs, Passthrough-Datenträger, gemeinsam genutzte Datenträger, Cluster-Workloads und hardwaregebundene Lizenzen** erfordern einen workload-spezifischen Plan. Legen Sie fest, wer die Umstellung freigibt und bis wann ein Rückfall erfolgen muss. Starten Sie nicht beide Kopien mit derselben Rechneridentität im Produktionsnetz.

| Quelldetail | Warum es benötigt wird |
|---|---|
| **VM-Generation und Firmware** | SeaBIOS oder OVMF in Proxmox auswählen |
| **Secure-Boot-Zustand und Vorlage** | Startrichtlinie anpassen und kompatible Schlüssel registrieren |
| **Boot- und Datendatenträger** | Jede benötigte virtuelle VHDX-Datei in der richtigen Reihenfolge importieren |
| **Prüfpunkte und AVHDX-Dateien** | Eine Differenzplatte nicht als unabhängige Basisplatte behandeln |
| **IP, DNS, MAC und VLAN** | Erreichbarkeit wiederherstellen, ohne eine Identität zu duplizieren |
| **vTPM und BitLocker** | Wiederherstellung vor Änderungen an der virtuellen Hardware vorbereiten |
| **Dienste und Datenprüfungen** | Nachweise für Erfolg und Rückfall festlegen |

Generation 1 verwendet ein klassisches BIOS. Generation 2 verwendet die Unified Extensible Firmware Interface (UEFI). Eine **AVHDX-Datei** ist eine Hyper-V-Differenzplatte, die mit einer VHDX-Basisplatte verknüpft ist. Ein **vTPM** ist ein virtuelles Trusted Platform Module, das BitLocker und andere Sicherheitsfunktionen verwenden. Ein **VLAN** ist ein getrenntes logisches Netzwerk, das über gemeinsam genutzte Netzwerkhardware übertragen wird.

**SeaBIOS** stellt klassische BIOS-Firmware bereit. **OVMF** stellt UEFI-Firmware bereit. **VirtIO** ist eine schnelle Schnittstelle für virtuelle Geräte, für die Gasttreiber erforderlich sind. Ein **initramfs** ist das frühe Linux-Dateisystem, das Treiber lädt, bevor das Hauptsystem startet.

## Einstellungen der virtuellen Maschine in Hyper-V erfassen

Führen Sie diese schreibgeschützten Befehle in einer erhöhten PowerShell-Sitzung auf dem Hyper-V-Host aus. Es handelt sich um ungetestete Beispiele. Prüfen Sie jeden Befehl anhand des installierten Hyper-V-Moduls und Ihres Änderungsverfahrens. Geben Sie den VM-Namen ein, wenn die Eingabeaufforderung erscheint:

```powershell
$vmName = Read-Host "Name der Hyper-V-VM"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

Das [PowerShell-Modul für Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) dokumentiert diese Inventarbefehle. Vergleichen Sie die Datenträgerpfade mit den VM-Einstellungen. Erfassen Sie angehängte ISO-Dateien, Datendatenträger, virtuelle Switches, statische Adressen und DHCP-Reservierungen. Notieren Sie Betriebssystem und Anwendungsversionen des Gasts. Prüfen Sie die Sicherung, indem Sie eine Testkopie wiederherstellen oder ein aktuelles dokumentiertes Wiederherstellungsergebnis kontrollieren. Eine Dateikopie ohne Wiederherstellungstest ist ein schwächerer Nachweis.

Erfassen Sie bei einer **Generation-2-VM** auch Firmware- und Sicherheitseinstellungen:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Notieren Sie den **Secure-Boot**-Zustand, die Vorlage und die vTPM-Einstellung. Die Microsoft-Referenz zu [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) beschränkt den Befehl auf Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) meldet die Sicherheitskonfiguration der VM. Führen Sie **`Get-VMFirmware`** nicht für einen Gast der Generation 1 aus. Eine **MAC-Adresse** kennzeichnet eine Netzwerkschnittstelle. **DNS** ordnet Namen Adressen zu. **DHCP** weist Netzwerkeinstellungen zu. Ein **EFI-Datenträger** speichert UEFI-Einstellungen.

**Lösen Sie Prüfpunkte vor dem abschließenden Export auf.** Laut Microsoft erfasst ein Hyper-V-Export auch Prüfpunktdateien und VHDX-Datenträger. Das Löschen eines Prüfpunkts über Hyper-V führt seine Differenzplatte zusammen. Löschen Sie niemals eine **`.avhdx`**-Datei im Dateisystem, um einen Prüfpunkt zu entfernen. Schlägt eine Zusammenführung fehl oder scheint die Datenträgerkette unvollständig, halten Sie an und folgen Sie Microsofts [Anleitung zur Wiederherstellung von Prüfpunkten](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). Der [Microsoft-Leitfaden zu Prüfpunkten](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) erklärt das übliche Löschen und Zusammenführen.

Beschaffen und prüfen Sie bei einem Windows-Gast mit **BitLocker** oder **vTPM** den Wiederherstellungsschlüssel, bevor Sie die virtuelle Hardware ändern. Hyper-Vs [Sicherheitsdokumentation für Generation 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) beschreibt die vTPM-gestützte Verschlüsselung. Microsofts [Häufige Fragen zu BitLocker](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) erklärt, warum Änderungen am Startvorgang die Wiederherstellung auslösen. Ein neues Proxmox-TPM-Gerät übernimmt nicht den alten TPM-Zustand. Bewahren Sie den Schlüssel außerhalb der exportierten VM auf.

## Ausgeschaltete VM exportieren

Fahren Sie den Gast ordnungsgemäß herunter. Prüfen Sie, dass Hyper-V **Off** (ausgeschaltet) und nicht Saved (gespeichert) anzeigt. Warten Sie, bis jede Prüfpunktzusammenführung abgeschlossen ist. Exportieren Sie die VM anschließend an einen Speicherort mit ausreichend freiem Platz. Klicken Sie im Hyper-V-Manager mit der rechten Maustaste auf die VM, wählen Sie **Export** (exportieren) und legen Sie das Ziel fest. Das PowerShell-Äquivalent lautet:

```powershell
$vmName = Read-Host "Name der ausgeschalteten Hyper-V-VM"
$exportPath = Read-Host "Exportzielverzeichnis"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Fahren Sie die VM herunter und warten Sie, bis Hyper-V Off (ausgeschaltet) anzeigt, bevor Sie exportieren." }
Export-VM -Name $vmName -Path $exportPath
```

Microsofts [Exportanleitung](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) erklärt, dass ein Export virtuelle Datenträger, Konfiguration und Prüfpunktdateien enthält. Die Referenz zu [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) beschreibt den Befehl. Prüfen Sie am Ziel die erwarteten Datenträgerdateien und ihre Größen. Lassen Sie die Quell-VM ausgeschaltet und behalten Sie ihre unabhängige Sicherung. **Ändern Sie die exportierten Dateien während des Imports nicht.**

Übertragen Sie die VHDX-Dateien an einen Pfad, auf den der Proxmox-Host zugreifen kann. Behandeln Sie den Export als vertrauliche Gastdaten. Verwenden Sie einen verschlüsselten Übertragungsweg, beschränken Sie den Zugriff auf Übertragungsort und Zielspeicher und entfernen Sie temporäre Kopien nach der Prüfung. Kontrollieren Sie die verfügbare Kapazität am Übertragungsort und im Zielspeicher. Bewahren Sie einen unveränderten Export für den Rückfall auf. Enthält der Export **`.avhdx`**-Dateien, wählen Sie nicht anhand des Dateinamens eine Basis-**`.vhdx`** aus und nehmen Sie an, sie enthalte die neuesten Schreibvorgänge. Lösen Sie die Datenträgerkette in Hyper-V auf, bevor Sie fortfahren.

## Zielmaschine in Proxmox erstellen

Legen Sie in der Proxmox-Weboberfläche eine neue VM mit dem zuvor erfassten Gastbetriebssystemtyp, Prozessor und Arbeitsspeicher an. Wählen Sie eine noch nicht verwendete VM-ID. Installieren Sie kein neues Betriebssystem. Entfernen Sie den leeren Datenträger des Assistenten, bevor Sie den Quelldatenträger importieren. Lassen Sie den Netzwerkadapter beim ersten Start von der Produktionsbrücke getrennt oder verbinden Sie ihn mit einem isolierten Testnetz.

| Hyper-V-Quelle | Proxmox-Ziel |
|---|---|
| **Generation 1, klassisches BIOS** | SeaBIOS |
| **Generation 2, UEFI** | OVMF mit EFI-Datenträger und passender Secure-Boot-Richtlinie |
| **Windows-Bootdatenträger ohne VirtIO-Speichertreiber** | Zunächst als SATA anschließen |
| **Windows mit vTPM oder BitLocker** | Bei Bedarf ein neues TPM-Zustandsgerät, Wiederherstellungsschlüssel vor dem ersten Start bereithalten |

Microsofts [Leitfaden zu VM-Generationen](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) ordnet Generation 1 dem klassischen BIOS und Generation 2 UEFI zu. Proxmox' [VM-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschreibt SeaBIOS, OVMF und den EFI-Datenträger, der UEFI-Einstellungen speichert. **Passen Sie den Startmodus der Quelle an.** Eine Änderung während der Migration schafft ein zusätzliches Startproblem.

Passen Sie bei einer Generation-2-Quelle an, ob **Secure Boot** aktiviert war. Prüfen Sie die Quellvorlage und wählen Sie kompatible, registrierte Schlüssel für den Gast. Hyper-V-Vorlagennamen werden nicht zu Proxmox übertragen. Proxmox' 4-MB-EFI-Datenträger und die Option **Pre-Enroll keys** (Schlüssel vorab registrieren) stellen Secure-Boot-Schlüssel bereit und aktivieren Secure Boot standardmäßig. Prüfen Sie das Startverhalten des Ziels vor der Umstellung. Microsofts [Firmware-Referenz](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) beschreibt die erforderliche Quellvorlage. Proxmox' [Dokumentation zum EFI-Datenträger](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschreibt die Zielschlüssel.

Prüfen Sie vor einer Änderung der EFI-Schlüssel, ob der Wiederherstellungsschlüssel sicher hinterlegt ist, und notieren Sie die aktuellen Protector-IDs. Folgen Sie der installierten Proxmox-VE- und OVMF-Dokumentation zur Registrierung von EFI-Schlüsseln. Bestätigen Sie den Wiederherstellungsschlüssel erneut und prüfen Sie `manage-bde -status` vor dem ersten Start. Setzen Sie Protectoren nicht pauschal aus und deaktivieren oder löschen Sie sie nicht als allgemeinen Migrationsschritt. Notieren Sie die Firmwarepaketversion, den Secure-Boot-Zustand, die Firmwareversion und den BitLocker-Zustand.

Verwendet die Quelle ein **vTPM**, fügen Sie vor dem ersten Start im Proxmox-Bereich Hardware (Geräte) die Option **TPM State** (TPM-Zustand) hinzu. Wählen Sie **Version 2.0**, außer für den Gast besteht eine dokumentierte Anforderung für Version 1.2. Dadurch entsteht ein neuer TPM-Zustand, keine Kopie des Hyper-V-vTPM. Für einen BitLocker-Gast muss beim ersten Start der geprüfte Wiederherstellungsschlüssel bereitliegen. Proxmox' [TPM-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschreibt die Hardwareaktion und die Versionen.

Starten Sie Windows zunächst von einem SATA-Bootdatenträger, sofern der Gast nicht bereits über den benötigten VirtIO-Speichertreiber verfügt. Installieren Sie nach einem erfolgreichen Start die unterstützten VirtIO-Treiber und ändern Sie jeweils nur ein virtuelles Gerät. Proxmox empfiehlt VirtIO SCSI wegen der Leistung. Fehlt der Boottreiber, kann Windows jedoch nicht auf den Systemdatenträger zugreifen. Prüfen Sie bei Linux, ob das initramfs den Zielspeichertreiber enthält, bevor Sie den Bus wechseln. Proxmox' [VM-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschreibt die Datenträgercontroller.

## Datenträger importieren und anschließen

Prüfen Sie auf dem Proxmox-Host den Pfad der kopierten VHDX-Datei. Der folgende Befehl zeigt einen Import für die VM-ID **230** in einen Speicher mit der ID **`local-lvm`**. Ersetzen Sie alle drei Werte durch Ihre eigenen:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Laut Proxmox-Referenz zu [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) wird das Quellabbild als **unbenutzter Datenträger** importiert. QEMUs [Abbilddokumentation](https://www.qemu.org/docs/master/system/images) führt VHDX als unterstütztes Konvertierungsformat. Importieren Sie jeden zusätzlichen Datendatenträger einzeln. Warten Sie, bis jeder Import abgeschlossen ist, und vergleichen Sie die importierten Größen mit dem Quellinventar.

Schließen Sie im Bereich **Hardware** (Geräte) der VM den unbenutzten Bootdatenträger für den ersten Windows-Start als **SATA** an. Schließen Sie Datendatenträger in der dokumentierten Reihenfolge an. Wählen Sie unter **Options > Boot Order** (Optionen > Startreihenfolge) den Bootdatenträger aus. Prüfen Sie bei einem Gast der Generation 2 **OVMF** und den EFI-Datenträger. Lassen Sie Importdateien und Quell-VM unverändert, bis die Validierung bestanden ist.

## Vor der Umstellung testen

Starten Sie den Proxmox-Gast im isolierten Netzwerk. Prüfen Sie über die Konsole den Startbildschirm, die Betriebssystemanmeldung, Datenträgervolumes, Anwendungsdaten und Dienstprotokolle. Eine Anmeldeaufforderung allein beweist keinen erfolgreichen Umzug. Verwenden Sie die vor dem Export festgelegten Prüfungen, einschließlich einer repräsentativen Transaktion oder eines Lesezugriffs auf aktuelle Daten.

Entsperren Sie einen BitLocker-Gast bei entsprechender Aufforderung mit dem Wiederherstellungsschlüssel. Prüfen Sie nach dem Start von Windows in einer erhöhten Eingabeaufforderung den Schutzstatus und die Protectoren des Betriebssystemvolumes:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

Microsofts [Leitfaden zu BitLocker-Vorgängen](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) beschreibt das Prüfen von Protectoren und das Sichern des Wiederherstellungsschlüssels. Die Ausgabe enthält vertrauliche Wiederherstellungsdaten. Fügen Sie sie nicht in ein Ticket oder ein öffentliches Protokoll ein. Prüfen Sie den vorgesehenen Protector und hinterlegen Sie entsprechend Ihrer Richtlinie eine aktuelle Wiederherstellungsmethode. Starten Sie den Gast neu und bestätigen Sie vor der Umstellung, dass keine erneute Wiederherstellungsaufforderung erscheint. Eine wiederholte Aufforderung bedeutet, dass die Migrationsprüfung fehlgeschlagen ist. Sie ist kein Grund, den ursprünglichen Schlüssel zu verwerfen.

| Prüfung | Erfolgskriterium |
|---|---|
| **Start und Datenträger** | Gast startet und alle erwarteten Volumes werden eingebunden |
| **Secure Boot und BitLocker** | Die vorgesehene Startrichtlinie gilt und der verschlüsselte Gast startet ohne wiederholte Wiederherstellung neu |
| **Anwendung** | Ein repräsentativer Lesezugriff oder eine Transaktion gelingt |
| **Netzwerk** | Erforderliche Gegenstellen erreichen den Testgast über die vorgesehenen Ports |
| **Wiederherstellung** | Proxmox-Sicherung und isolierter Wiederherstellungstest gelingen vor dem Entfernen der Quelle |
| **Betrieb** | Überwachung, Zeitsynchronisierung, Herunterfahren und Gast-Agent funktionieren wie vorgesehen |

Schalten Sie nach bestandenen Anwendungstests den Produktionsnetzwerkpfad oder die Adresse im Wartungsfenster um. Lassen Sie Hyper-V ausgeschaltet. Eine geänderte virtuelle Netzwerkkarte kann eine neue DHCP-Reservierung oder eine korrigierte statische Adresse im Gast erfordern. Prüfen Sie DNS, Firewallregeln und abhängige Dienste von einem separaten Client aus. Proxmox' [VM-Dokumentation](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschreibt Netzwerkgeräte und Gast-Agent.

## Fehler suchen und zurückrollen

| Symptom | Erste Prüfung |
|---|---|
| **Kein Bootgerät** | Bootreihenfolge, importierter Bootdatenträger, BIOS- oder UEFI-Modus und Secure-Boot-Schlüssel |
| **Windows-Speicherfehler** | SATA-Anschluss und fehlender VirtIO-Speichertreiber |
| **BitLocker-Wiederherstellung erscheint erneut** | Neuer TPM-Zustand, Secure-Boot-Richtlinie, Startmessungen und Protectoren |
| **Gast startet ohne Netzwerk** | Neue virtuelle Netzwerkkarte, Bridge, VLAN, DHCP-Reservierung und statische Adresse |
| **Daten sind veraltet oder fehlen** | Falsche VHDX-Datei, unvollständiger Export, Prüfpunktkette oder fehlender Datendatenträger |

Schlägt ein erforderlicher Test vor Ablauf der Rückfallfrist fehl, stoppen Sie die Proxmox-VM und trennen Sie ihr Produktionsnetzwerk. Stellen Sie den Netzwerkpfad der Quelle wieder her und starten Sie anschließend die ursprüngliche Hyper-V-VM. **Führen Sie niemals beide Kopien mit derselben Produktionsidentität aus.** Erfassen Sie alle Schreibvorgänge, die die Proxmox-Kopie vor der Rückkehr zu Hyper-V angenommen hat. Diese Schreibvorgänge müssen separat wiederhergestellt oder abgeglichen werden, da sie nicht auf dem Quelldatenträger angekommen sind.

Behalten Sie Quell-VM und Export, bis der Proxmox-Gast die Dienstprüfungen, eine neue Sicherung, einen isolierten Wiederherstellungstest und eine vereinbarte Beobachtungszeit bestanden hat. Der [Virtualisierungsvergleich der Website](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) unterstützt die Plattformwahl. Der [Proxmox-Upgrade-Leitfaden](/articles/proxmox-ve-8-to-9-upgrade-guide/) behandelt eine spätere Wartungsaufgabe. **Eine Migration ist abgeschlossen, wenn Workload und Wiederherstellungspfad auf dem neuen Host funktionieren, nicht wenn der Datenträgerimport beendet ist.**

## Nächste Schritte

Behalten Sie Quell-VM und Export, bis Workload-, Sicherungs- und Rückfallprüfungen während der vereinbarten Beobachtungszeit bestanden sind. Prüfen Sie vor dem Entfernen der Quelle den [Wiederherstellungstest für Proxmox-VM-Sicherungen](/articles/proxmox-vm-backup-restore-drill/).
