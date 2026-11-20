---
title: "Een Hyper-V-VM naar Proxmox VE migreren: een omkeerbare checklist"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Verplaats een Hyper-V-VM naar Proxmox VE met een export terwijl de bron uitstaat, passende firmware, geïmporteerde schijven, een geïsoleerde opstarttest en een terugdraaiplan."
genre: ["Virtualisatie", "Systeembeheer", "Thuislab"]
tags: ["Overstap van Hyper-V naar Proxmox", "Overstap vanaf Hyper-V", "Overstap naar Proxmox VE", "VHDX-invoer", "qm disk import", "VM-omschakeling", "VM-export vanuit Hyper-V", "Windows-VM op Proxmox", "VirtIO op Proxmox", "VM-terugrol", "UEFI-overstap", "Hyper-V-controlepunten", "virtuele TPM", "BitLocker-herstel", "Thuislabmigratie"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Een schijf steekt een brug over tussen een blauw en een oranje serverrek. Een apart terugpad en een schild markeren het doel."
coverCaption: "Houd de bron-VM beschikbaar totdat de nieuwe gast de omschakelcontroles doorstaat."
---

Een **Hyper-V-export** bewaart de bestanden van een virtuele machine. Proxmox VE heeft echter een nieuwe gastconfiguratie en geïmporteerde VHDX-schijfbestanden nodig. Een geslaagde kopie bewijst niet dat de gast opstart of gebruikers bedient. Deze checklist leidt één VM door een export met een uitgeschakelde bron, een gecontroleerde opstarttest en een omschakeling met een duidelijke terugweg.

<!--more-->

## Belangrijkste punten

- **Leg de bron vast:** noteer firmwaregeneratie, schijfpaden, controlepunten, netwerkinstellingen en versleuteling vóór de export.
- **Stop schrijfacties:** sluit de Hyper-V-VM af vóór de laatste export en houd de VM uitgeschakeld tijdens de Proxmox-test.
- **Pas het opstartpad aan:** Hyper-V Generation 1 gebruikt legacy BIOS. Generation 2 gebruikt UEFI.
- **Valideer de dienst:** controleer gegevens, netwerktoegang, back-ups en de gezondheid van de gast vóór u de bron buiten gebruik stelt.

## Voor u begint

Plan een onderhoudsvenster en test eerst op een wegwerp-VM. U hebt beheerdersrechten voor Hyper-V en Proxmox VE nodig, opslag voor de export en een gecontroleerde back-up die losstaat van de migratiekopie. Reserveer tijd om elke virtuele schijf over te zetten en de gasttoepassing te testen. Schijfgrootte en overdrachtssnelheid bepalen de uitvaltijd.

Deze procedure behandelt een gebruikelijke VM met virtuele schijven. **Shielded VM's, passthrough-schijven, gedeelde schijven, geclusterde workloads en hardwaregebonden licenties** vereisen een plan voor de specifieke workload. Leg vast wie de omschakeling goedkeurt en wat de uiterste tijd voor terugdraaien is. Start beide kopieën niet met dezelfde machine-identiteit op het productienetwerk.

| Broninformatie | Waarom u deze nodig hebt |
|---|---|
| **VM-generatie en firmware** | SeaBIOS of OVMF kiezen in Proxmox |
| **Secure Boot-status en sjabloon** | Opstartbeleid afstemmen en compatibele sleutels inschrijven |
| **Opstart- en gegevensschijven** | Elk benodigd VHDX-bestand in de juiste volgorde importeren |
| **Controlepunten en AVHDX-bestanden** | Een differencing-schijf niet behandelen als zelfstandige basisschijf |
| **IP, DNS, MAC en VLAN** | Bereikbaarheid herstellen zonder een identiteit te dupliceren |
| **vTPM en BitLocker** | Herstel voorbereiden vóór wijzigingen aan virtuele hardware |
| **Diensten en gegevenscontroles** | Bewijs voor succes en terugdraaien vastleggen |

Generation 1 gebruikt legacy BIOS. Generation 2 gebruikt Unified Extensible Firmware Interface (UEFI). Een **AVHDX-bestand** is een Hyper-V-differencing-schijf die aan een VHDX-basisschijf is gekoppeld. Een **vTPM** is een virtuele Trusted Platform Module die BitLocker en andere beveiligingsfuncties gebruiken. Een **VLAN** is een afzonderlijk logisch netwerk over gedeelde netwerkhardware.

**SeaBIOS** levert legacy BIOS-firmware. **OVMF** levert UEFI-firmware. **VirtIO** is een snelle virtuele apparaatinterface waarvoor gaststuurprogramma's nodig zijn. Een **initramfs** is het vroege Linux-bestandssysteem dat stuurprogramma's laadt voordat het hoofdsysteem start.

## De virtuele machine in Hyper-V inventariseren

Voer deze alleen-lezenopdrachten uit in een verhoogde PowerShell-sessie op de Hyper-V-host. Dit zijn niet-geteste voorbeelden. Controleer elke opdracht met de geïnstalleerde Hyper-V-module en uw wijzigingsprocedure. Voer de VM-naam in wanneer daarom wordt gevraagd:

```powershell
$vmName = Read-Host "Naam van Hyper-V-VM"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

De [PowerShell-module voor Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documenteert deze inventarisatieopdrachten. Vergelijk de schijfpaden met de VM-instellingen. Noteer gekoppelde ISO-bestanden, gegevensschijven, virtuele switches, statische adressen en DHCP-reserveringen. Leg de versies van het gastbesturingssysteem en de toepassing vast. Controleer de back-up door een testkopie terug te zetten of een recent gedocumenteerd herstelresultaat te bekijken. Een bestandskopie zonder hersteltest levert zwakker bewijs.

Leg bij een **Generation 2**-VM ook firmware- en beveiligingsinstellingen vast:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Noteer de **Secure Boot**-status, het sjabloon en de vTPM-instelling. De Microsoft-referentie voor [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) beperkt de opdracht tot Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) toont de beveiligingsconfiguratie van de VM. Voer **`Get-VMFirmware`** niet uit voor een Generation 1-gast. Een **MAC-adres** identificeert een netwerkinterface. **DNS** koppelt namen aan adressen. **DHCP** wijst netwerkinstellingen toe. Een **EFI-schijf** bewaart UEFI-instellingen.

**Los controlepunten op vóór de laatste export.** Microsoft vermeldt dat een Hyper-V-export ook controlepuntbestanden en VHDX-schijven verzamelt. Een controlepunt verwijderen via Hyper-V voegt de differencing-schijf samen. Verwijder nooit een **`.avhdx`**-bestand uit het bestandssysteem om een controlepunt te wissen. Als samenvoegen mislukt of de schijfketen onvolledig lijkt, stop en volg de [Microsoft-instructies voor herstel van controlepunten](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). De [Microsoft-gids voor controlepunten](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) beschrijft normaal verwijderen en samenvoegen.

Vraag bij een Windows-gast met **BitLocker** of een **vTPM** de herstelsleutel op en controleer deze vóór wijzigingen aan virtuele hardware. De [Hyper-V-beveiligingsdocumentatie voor Generation 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) beschrijft versleuteling op basis van vTPM. De [Veelgestelde vragen over BitLocker van Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) legt uit waarom wijzigingen aan het opstarten herstel activeren. Een nieuw Proxmox-TPM-apparaat neemt de oude TPM-status niet over. Bewaar de sleutel buiten de geëxporteerde VM.

## Een uitgeschakelde VM exporteren

Sluit de gast netjes af. Controleer dat Hyper-V **Off** (uitgeschakeld) toont en niet Saved (opgeslagen). Wacht tot elke samenvoeging van controlepunten is voltooid. Exporteer de VM daarna naar een locatie met voldoende vrije ruimte. Klik in Hyper-V Manager met de rechtermuisknop op de VM, kies **Export** (exporteren) en selecteer de bestemming. Het PowerShell-equivalent is:

```powershell
$vmName = Read-Host "Naam van uitgeschakelde Hyper-V-VM"
$exportPath = Read-Host "Exportbestemmingsmap"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Schakel de VM uit en wacht tot Hyper-V Off (uitgeschakeld) toont voordat u exporteert." }
Export-VM -Name $vmName -Path $exportPath
```

De [exportgids van Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) zegt dat een export virtuele schijven, configuratie en controlepuntbestanden bevat. De referentie voor [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) beschrijft de opdracht. Controleer op de bestemming de verwachte schijfbestanden en hun grootte. Houd de bron-VM uitgeschakeld en bewaar de onafhankelijke back-up. **Wijzig de geëxporteerde bestanden niet tijdens het importeren.**

Zet de VHDX-bestanden over naar een pad dat bereikbaar is vanaf de Proxmox-host. Behandel de export als gevoelige gastgegevens. Gebruik versleuteld transport, beperk toegang tot de overdrachtslocatie en doelopslag en verwijder tijdelijke kopieën na validatie. Controleer de beschikbare capaciteit op beide locaties. Bewaar een ongewijzigde export voor terugdraaien. Bevat de export **`.avhdx`**-bestanden, kies dan niet op basis van de naam een basis-**`.vhdx`** en neem niet aan dat deze de nieuwste schrijfacties bevat. Los de schijfketen op Hyper-V op voordat u verdergaat.

## De doelmachine in Proxmox maken

Maak in de Proxmox-webinterface een nieuwe VM met het eerder vastgelegde gastbesturingssysteemtype, de CPU en het geheugen. Kies een nieuwe, ongebruikte VM-ID. Installeer geen nieuw besturingssysteem. Verwijder de lege schijf die de wizard maakte voordat u de bronschijf importeert. Laat de netwerkadapter tijdens de eerste start losgekoppeld van de productiebridge of koppel deze aan een geïsoleerd testnetwerk.

| Hyper-V-bron | Proxmox-doel |
|---|---|
| **Generation 1, legacy BIOS** | SeaBIOS |
| **Generation 2, UEFI** | OVMF met EFI-schijf en passend Secure Boot-beleid |
| **Windows-opstartschijf zonder VirtIO-opslagstuurprogramma** | Eerst aansluiten als SATA |
| **Windows met vTPM of BitLocker** | Indien nodig nieuw TPM-statusapparaat, herstelsleutel klaar vóór eerste start |

De [VM-generatiegids van Microsoft](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) koppelt Generation 1 aan legacy BIOS en Generation 2 aan UEFI. De [Proxmox-VM-documentatie](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschrijft SeaBIOS, OVMF en de EFI-schijf die UEFI-instellingen bewaart. **Stem de opstartmodus af op de bron.** Wijziging tijdens de migratie veroorzaakt een extra opstartprobleem.

Stem bij een Generation 2-bron af of **Secure Boot** ingeschakeld was. Controleer het bronsjabloon en kies compatibele ingeschreven sleutels voor de gast. Hyper-V-sjabloonnamen worden niet naar Proxmox overgezet. De 4 MB EFI-schijf van Proxmox en de optie **Pre-Enroll keys** (sleutels vooraf registreren) leveren Secure Boot-sleutels en schakelen Secure Boot standaard in. Controleer het opstartgedrag vóór de omschakeling. De [firmwarereferentie van Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) beschrijft de bronvereiste. De [EFI-schijfdocumentatie van Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschrijft de doelsleutels.

Controleer vóór wijzigingen aan EFI-sleutels dat de herstelsleutel veilig is opgeslagen en noteer de huidige protector-ID's. Volg de geïnstalleerde Proxmox VE- en OVMF-documentatie voor het inschrijven van EFI-sleutels. Bevestig de herstelsleutel opnieuw en controleer `manage-bde -status` vóór de eerste start. Pauzeer, schakel protectors niet uit en verwijder ze niet als algemene migratiestap. Noteer de firmwarepakketversie, Secure Boot-status en firmwareversie, en de BitLocker-status.

Gebruikt de bron een **vTPM**, voeg dan vóór de eerste start **TPM State** (TPM-status) toe in het Proxmox-paneel Hardware (apparaten). Kies **versie 2.0**, tenzij de gast aantoonbaar versie 1.2 vereist. Dit maakt een nieuwe TPM-status, geen kopie van de Hyper-V-vTPM. Een BitLocker-gast heeft de gecontroleerde herstelsleutel nodig bij de eerste start. De [TPM-documentatie van Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschrijft de hardwareactie en versies.

Start Windows eerst vanaf een SATA-opstartschijf, tenzij de gast al het vereiste VirtIO-opslagstuurprogramma heeft. Installeer na een geslaagde start ondersteunde VirtIO-stuurprogramma's en wijzig telkens één virtueel apparaat. Proxmox raadt VirtIO SCSI aan voor prestaties, maar zonder opstartstuurprogramma heeft Windows geen toegang tot de systeemschijf. Controleer voor Linux of de initramfs het doelopslagstuurprogramma bevat voordat u de bus wijzigt. De [Proxmox-VM-documentatie](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschrijft schijfcontrollers.

## Schijven importeren en aansluiten

Controleer op de Proxmox-host het pad van de gekopieerde VHDX. De volgende opdracht toont een import voor VM-ID **230** naar opslag met ID **`local-lvm`**. Vervang alle drie waarden door uw eigen waarden:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

De [**`qm disk import`**-referentie van Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) zegt dat de broninstallatie als **ongebruikte schijf** wordt geïmporteerd. De [QEMU-documentatie voor schijfimages](https://www.qemu.org/docs/master/system/images) noemt VHDX als ondersteund conversieformaat. Importeer elke extra gegevensschijf afzonderlijk. Wacht tot elke importtaak is voltooid en vergelijk de geïmporteerde schijfgrootte met de broninventaris.

Koppel in het paneel **Hardware** (apparaten) de ongebruikte opstartschijf voor de eerste Windows-start aan als **SATA**. Sluit gegevensschijven aan in de gedocumenteerde volgorde. Kies de opstartschijf onder **Options > Boot Order** (opties > opstartvolgorde). Controleer bij een Generation 2-gast **OVMF** en de EFI-schijf. Laat importbestanden en bron-VM intact totdat validatie slaagt.

## Testen vóór omschakeling

Start de Proxmox-gast op het geïsoleerde netwerk. Controleer via de console het opstartscherm, aanmelden bij het besturingssysteem, schijfvolumes, toepassingsgegevens en servicelogboeken. Een aanmeldprompt bewijst geen geslaagde migratie. Voer de vooraf vastgelegde controles uit, waaronder een representatieve transactie of het lezen van recente gegevens.

Ontgrendel een BitLocker-gast met de herstelsleutel als daarom wordt gevraagd. Controleer na het starten van Windows in een verhoogde opdrachtprompt de beveiligingsstatus en protectors van het systeemvolume:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

De [BitLocker-bewerkingsgids van Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) beschrijft het bekijken van protectors en het veiligstellen van herstelsleutels. De uitvoer bevat gevoelige herstelgegevens. Plak deze niet in een ticket of openbaar logboek. Controleer de bedoelde protector en bewaar volgens uw beleid een actuele herstelmethode. Start de gast opnieuw en bevestig vóór omschakeling dat geen nieuwe herstelprompt verschijnt. Herhaald herstel betekent een mislukte migratiecontrole, niet dat u de oorspronkelijke sleutel moet weggooien.

| Controle | Voorwaarde voor slagen |
|---|---|
| **Opstarten en schijven** | De gast start en alle verwachte volumes worden gekoppeld |
| **Secure Boot en BitLocker** | Het gewenste opstartbeleid geldt en de versleutelde gast herstart zonder herhaald herstel |
| **Toepassing** | Een representatieve leesactie of transactie slaagt |
| **Netwerk** | Benodigde peers bereiken de testgast op de bedoelde poorten |
| **Herstel** | Proxmox-back-up en geïsoleerde hersteltest slagen vóór verwijdering van de bron |
| **Beheer** | Monitoring, tijdsynchronisatie, afsluiten en gastagent werken zoals bedoeld |

Schakel na geslaagde toepassingstests tijdens het onderhoudsvenster het productie-netwerkpad of adres om. Houd Hyper-V uitgeschakeld. Een andere virtuele NIC vereist mogelijk een nieuwe DHCP-reservering of een aangepast statisch adres in de gast. Controleer DNS, firewallregels en afhankelijke diensten vanaf een aparte client. De [Proxmox-VM-documentatie](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) beschrijft netwerkapparaten en gastagentopties.

## Problemen oplossen en terugdraaien

| Symptoom | Eerste controle |
|---|---|
| **Geen opstartapparaat** | Opstartvolgorde, geïmporteerde opstartschijf, BIOS- of UEFI-modus en Secure Boot-sleutels |
| **Windows-opslagfout** | SATA-aansluiting en ontbrekend VirtIO-opslagstuurprogramma |
| **BitLocker vraagt herhaaldelijk om herstel** | Nieuwe TPM-status, Secure Boot-beleid, opstartmetingen en protectors |
| **Gast start zonder netwerk** | Nieuwe virtuele NIC, bridge, VLAN, DHCP-reservering en statisch adres |
| **Gegevens zijn oud of ontbreken** | Verkeerde VHDX, onvolledige export, controlepuntketen of ontbrekende gegevensschijf |

Als een vereiste test vóór de uiterste terugdraaitijd mislukt, stop de Proxmox-VM en ontkoppel het productienetwerk. Herstel het netwerkpad van de bron en start daarna de oorspronkelijke Hyper-V-VM. **Voer nooit beide kopieën met dezelfde productie-identiteit uit.** Leg schrijfacties vast die de Proxmox-kopie accepteerde voordat u terugkeert naar Hyper-V. Deze vereisen apart herstel of afstemming, omdat de bronschijf ze niet ontving.

Bewaar de bron-VM en export totdat de Proxmox-gast de dienstcontroles, een nieuwe back-up, een geïsoleerde hersteltest en een afgesproken observatieperiode heeft doorstaan. De [virtualisatievergelijking van de website](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) helpt bij platformkeuze. De [Proxmox-upgradegids](/articles/proxmox-ve-8-to-9-upgrade-guide/) behandelt later onderhoud. **De migratie is klaar wanneer de workload en het herstelpad op de nieuwe host werken, niet zodra de schijfimport eindigt.**

## Volgende stappen

Houd de bron-VM en export totdat workload-, back-up- en terugdraaicontroles tijdens de afgesproken observatieperiode slagen. Bekijk de [Proxmox VM-back-uphersteltest](/articles/proxmox-vm-backup-restore-drill/) voordat u de bron verwijdert.
