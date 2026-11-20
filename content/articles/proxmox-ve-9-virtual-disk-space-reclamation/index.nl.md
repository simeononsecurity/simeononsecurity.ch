---
title: "Proxmox VE 9: gebruik van virtuele schijven beperken en ruimte terugwinnen"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Beperk het opslaggebruik van VM's en LXC-containers in Proxmox VE 9. Vergelijk formaten en backends, schakel discard in, voer trim uit en controleer snapshots voordat je ruimte terugwint."
genre: ["Virtualisatie", "Linux-beheer", "Proxmox VE-platform", "Opslag", "Thuislab"]
tags: ["Proxmox VE 9 schijfruimte", "dunne toewijzing van Proxmox", "discard-meldingen van Proxmox", "TRIM-opdracht van Proxmox", "Windows ReTrim op Proxmox", "Linux fstrim op Proxmox", "Proxmox LXC-schijfgebruik", "thin provisioning met LVM op Proxmox", "ZFS sparse-zvol op Proxmox", "Ceph RBD-blokapparaten op Proxmox", "qcow2-indeling op Proxmox", "raw-schijf op Proxmox", "Proxmox-momentopnamen", "ruimte op virtuele schijf terugwinnen", "Proxmox-opslagtypen", "VirtIO SCSI-controller", "nulschrijfdetectie van Proxmox", "back-upopslag van Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Twee blokrasters met een pijl ertussen tonen gebruikte blokken op een virtuele schijf en vrije capaciteit in een opslagpool."
coverCaption: "Bestanden in de gast verwijderen, discard sturen en opslagruimte terugwinnen zijn afzonderlijke stappen."
---

**Een kleiner bestandssysteem in de gast betekent niet altijd minder gebruikte Proxmox-opslag.** Om ruimte op de host vrij te maken, heb je een schijf nodig die thin provisioning ondersteunt, een werkende discard-route voor VM's en een backend zonder blokken die door snapshots worden vastgehouden. Deze gids behandelt instellingen en controles voor Proxmox VE 9-VM's en LXC-containers.

<!--more-->

## Belangrijkste punten

- **Kies eerst de backend.** De opgegeven grootte van een virtuele schijf verschilt alleen van de toegewezen hostruimte als het imageformaat of de opslagbackend thin provisioning ondersteunt.
- **Schakel discard in voor de VM en voer daarna trim uit in de gast.** Windows ReTrim en Linux `fstrim` sturen verzoeken voor ongebruikte blokken via de virtuele schijf.
- **Controleer snapshots en back-ups apart.** Oude blokken blijven toegewezen zolang een snapshot ernaar verwijst. Back-upbestanden en PBS-chunks volgen hun eigen bewaartermijnen.
- **Behandel LXC-mounts op basis van hun type.** Beheerde rootfs- en mountpoint-volumes, bind mounts en apparaatmounts verschillen in eigenaarschap en back-upgedrag.

## Voor je begint

Je hebt **beheerderstoegang tot Proxmox VE 9** nodig, een gecontroleerde back-up van elke betrokken gast en voldoende vrije ruimte in de pool. Noteer vóór wijzigingen de gast-ID, diskbus, volume-ID, opslag-ID, snapshots en huidige toewijzing. Gebruik de [VM-hersteltest](/articles/proxmox-vm-backup-restore-drill/) om herstel te testen.

**Geschatte tijd:** 20 tot 60 minuten per gast, plus grote trim- of opschoontaken. **Moeilijkheid:** Gemiddeld. Begin met een VM met weinig risico en vergelijk het opslaggebruik voor en na de wijziging.

> **Waarschuwing:** Een volle thin pool veroorzaakt I/O-fouten bij gasten en brengt bestandssystemen in gevaar. Wijs niet meer capaciteit toe dan beschikbaar is zonder de vrije data- en metadataruimte van de pool te bewaken. [Proxmox-opslagdocumentatie](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Volg de toewijzingsketen

**Verwijderen**, **discard** en **ruimte terugwinnen** gebeuren op verschillende lagen. Een gast verwijdert een bestand en markeert bestandssysteemblokken als vrij. Het bestandssysteem stuurt TRIM of UNMAP voor die blokken. QEMU stuurt het verzoek door als discard is ingeschakeld op de virtuele schijf. De opslagbackend geeft fysieke toewijzing vrij als het formaat en de pool dit ondersteunen. [Proxmox-documentatie over VM-schijven](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Laag | Wat je controleert | Nuttig bewijs |
|---|---|---|
| **Gastbestanden** | Vrije ruimte in het bestandssysteem | Volumeeigenschappen van Windows of Linux `df -h` |
| **Virtuele schijf** | Bus, discard, SSD-emulatie, imageformaat | VM-tabblad **Hardware** of `qm config VMID` |
| **PVE-volume** | Eigenaar en ingestelde grootte | Tabblad **Content** van de opslag of `pvesm list STORAGE_ID` |
| **Opslagpool** | Vrije data en metadata, vastgehouden blokken | `pvesm status` en hulpmiddelen voor de backend |

**Een virtuele schijf van 100 GiB stelt een capaciteitslimiet in, maar garandeert geen toewijzing van 100 GiB.** Omgekeerd bewijst 20 GiB gebruik in de gast niet dat de host 20 GiB gebruikt. Metadata, snapshots, back-upkopieën en eerder geschreven blokken beïnvloeden de uitkomst. [Proxmox-opslagdocumentatie](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Vergelijk schijfformaten

**De opslagbackend bepaalt welke imageformaten Proxmox aanbiedt.** ZFS-zvols en Ceph RBD gebruiken virtuele raw-schijven. LVM gebruikt meestal raw, met de verderop beschreven uitzondering voor volumeketens in Proxmox VE 9. Bestandsopslag zoals directory en NFS ondersteunt raw of qcow2. Raw biedt zelf geen thin provisioning of snapshots. De onderliggende opslag moet die functies leveren. Qcow2 biedt copy-on-write-toewijzing en snapshots op imageniveau. [Proxmox-documentatie over VM-schijven](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Formaat | Toewijzingsmethode | Afweging voor ruimte |
|---|---|---|
| **qcow2 op bestandsopslag** | Qcow2 wijst clusters toe wanneer ze worden geschreven | Imagemetadata en snapshotketens gebruiken ruimte |
| **raw-bestand op bestandsopslag** | Sparse-bestandsgedrag van het bestandssysteem, indien ondersteund | Raw biedt op zichzelf geen thin provisioning of snapshots |
| **raw-blokvolume** | LVM thin, ZFS, Ceph RBD of andere backend | Pooltoewijzing en snapshots hangen af van de backend |

**Proxmox VE 9 thick LVM heeft een speciale snapshotmodus.** `snapshot-as-volume-chain` gebruikt qcow2-backingrelaties tussen thick LVM-logical volumes. Deze modus gebruikt geen interne qcow2-snapshots. De optie geldt alleen voor nieuw aangemaakte VM-schijven en is volgens de huidige Proxmox-documentatie nog een technologiepreview. PVE toont elke snapshot als volledig toegewezen. De werkelijke SAN-toewijzing is alleen kleiner als de achterliggende opslag thin provisioning en discard ondersteunt. [Proxmox-documentatie over LVM-opslag](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Converteer een schijf niet alleen omdat de extensie `.raw` is.** Controleer eerst de opslagplugin en de toegewezen blokken. Een raw-schijf op `local-lvm` wordt anders toegewezen dan een volledig toegewezen raw-bestand op gewone directory-opslag.

## Opslagsoorten vergelijken

Proxmox onderscheidt **bestandsopslag** en **blokopslag**. De opslagplugin bepaalt ook snapshots, klonen, delen en de inhoudstypen die een pool accepteert. Controleer **Datacenter > Storage** voordat je op een formaat of functie vertrouwt. [Tabel met Proxmox-opslagtypen](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Opslag | Gedrag van VM-schijf | Controle voor ruimteherstel |
|---|---|---|
| **Directory, ext4, XFS** | Raw- of qcow2-bestanden | Vergelijk de door `du` toegewezen bytes met de virtuele imagegrootte. Controleer snapshots als een andere opslaglaag die levert. |
| **NFS, CIFS** | Raw- of qcow2-bestanden op gedeelde opslag | Controleer toegewezen ruimte op de server. Een trimresultaat van de gast bewijst niet dat de server ruimte vrijgaf. |
| **LVM met dunne toewijzing (`local-lvm`)** | Lokale thin raw-logical volumes | Volg met `lvs` de data- en metadatapercentages van de thin pool. |
| **LVM thick** | Raw-LV's of VE 9 qcow2-volumeketens | Bestanden verwijderen in de gast verkleint de vaste LV-reservering niet. Controleer SAN-thintoewijzing apart. |
| **ZFS-opslag (`local-zfs`)** | Raw-zvols of containersubvolumes | Controleer `sparse`, dataset-eigenschappen, poolgebruik en snapshots. |
| **Ceph RBD** | Thin raw-RBD-images op gedeelde opslag | Controleer Ceph-poolcapaciteit, imagegebruik, snapshots en discard. |
| **Btrfs** | Bestandsvolumes met Btrfs-subvolumes voor raw-images | Beschouw de PVE Btrfs-plugin als technologiepreview en controleer snapshots en bestandssysteemgebruik. |

**Andere opslagplugins hebben andere functies.** CephFS biedt gedeelde bestandsopslag. iSCSI en Fibre Channel bieden gedeelde blokapparaten, vaak verdeeld in VM-volumes met LVM. ZFS over iSCSI gebruikt externe ZFS-blokopslag. Proxmox Backup Server (PBS) bewaart back-ups, geen actieve VM-schijven. Controleer de ingeschakelde typen **Content** voordat je er `images`, `rootdir`, `backup` of `iso` plaatst. [Tabel met Proxmox-opslagtypen](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Toewijzingsvlaggen voor bestandsopslag zijn belangrijk bij het aanmaken.** De opslaginstelling `format` kiest `raw`, `qcow2` of `vmdk` waar ondersteund. `preallocation` voor raw- en qcow2-bestanden accepteert `off`, `metadata`, `falloc` of `full`. De standaardwaarde is `metadata`, die voor raw als `off` geldt. `full` reserveert bestandsruimte vooraf en haalt het voordeel van een kleine beginvoetafdruk weg. Controleer de opslagconfiguratie voordat je een grote schijf maakt. De vlag `shared` verklaart alleen bestaande gedeelde toegang. Deze maakt lokale opslag niet gedeeld. [Algemene Proxmox-opslageigenschappen](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` is de opslaginstelling voor thin-zvols.** Zonder sparse-zvols reserveert aanmaken capaciteit volgens het ingestelde volumeformaat. Controleer de opslagconfiguratie en pool voordat je een bestaande omgeving wijzigt. [Proxmox-documentatie over ZFS-opslag](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Directory-opslag vraagt om een tweede controle.** De logische lengte van een qcow2-bestand is niet de virtuele capaciteit die de gast ziet. `du -h` meldt bestandssysteemblokken die aan het imagebestand zijn toegewezen. `ls -lh` toont de logische bestandslengte. Voor een gestopte VM meldt `qemu-img info` de virtuele capaciteit en de grootte op de host. Vertrouw bij NFS op de administratie van de server voor definitieve capaciteitsbesluiten. [QEMU-referentie voor `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS heeft nog een toewijzingsgrens.** Dat qcow2 een lege cluster in het bestand hergebruikt, betekent niet dat de NFS-server bestandsblokken vrijgeeft. Hole punching vereist ondersteuning van de client, het onderhandelde protocol, de server en het serverbestandssysteem. NFSv4.2 definieert `DEALLOCATE`, maar een versienummer bewijst niet dat de server ruimte teruggaf. Controleer de onderhandelde NFS-mount en meet de toewijzing op de server. [NFSv4.2-specificatie voor `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Stel VM-schijfvlaggen in

Open in de Proxmox-interface **VM > Hardware > Hard Disk > Edit**. Controleer de bus en geavanceerde opties van de schijf. De volgende vlaggen beïnvloeden toewijzing of bepalen of een optimalisatie nut heeft. De [officiële referentie voor `qm`-opties](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) vermeldt beschikbaarheid per bus.

| Bus | Keuze voor schijfruimte |
|---|---|
| **IDE** | Compatibiliteit met oude systemen. Alleen gebruiken als de gast geen nieuwere driver heeft. |
| **SATA** | Breed ondersteunde emulatie. Controleer trim in de gast en schijfopties voordat je op herstel vertrouwt. |
| **SCSI met VirtIO SCSI** | Voorkeursroute voor moderne discard- en schijfinstellingen. Windows heeft de VirtIO-driver nodig. |
| **VirtIO Block** | Geparavirtualiseerde schijf. Linux-discard vereist kernel 5.0 of nieuwer. SSD-emulatie ontbreekt. |

| Instelling | Effect | Richtlijn |
|---|---|---|
| **discard doorgeven (`on`)** | Stuurt TRIM of UNMAP van de gast door | Vereist voor herstel vanuit de gast op een ondersteunde thin-backend. De standaardwaarde `ignore` blokkeert het doorsturen. |
| **SSD-emulatie `ssd=1`** | Presenteert de schijf aan de gast als SSD | Sommige gasten hebben deze aanduiding nodig voordat ze trim sturen. De fysieke opslag wordt hierdoor niet sneller. VirtIO Block heeft deze vlag niet. |
| **Detect zeroes `detect_zeroes=1`** | Detecteert en probeert nulschrijfacties te optimaliseren | Optionele I/O-optimalisatie. Vervangt trim niet en garandeert geen ruimteherstel. |
| **Bus: SCSI / VirtIO SCSI single** | Biedt een SCSI-schijf via de VirtIO-controller | Praktische standaard voor moderne Windows- en Linux-gasten. Installeer de Windows VirtIO-drivers. |
| **Bus: VirtIO Block** | Gebruikt het VirtIO-blokapparaat | Linux-discard vereist kernel 5.0 of nieuwer. SSD-emulatie ontbreekt. |
| **I/O-thread `iothread=1`** | Wijst schijf-I/O toe aan een aparte thread | Gebruik met VirtIO Block of SCSI op een VirtIO SCSI single-controller. Prestatie-instelling, geen hersteloptie. |
| **Cache en AIO** | Wijzigen I/O-buffering en asynchrone I/O | Stem af op workload en backend. Geen van beide verkleint een schijf. |
| **Back-up `backup=0`** | Sluit de schijf uit van VM-back-ups | Verkleint de back-upomvang en verwijdert de data uit VM-herstel. Leg een aparte back-up vast. |
| **Replicatie `replicate=0`** | Sluit de schijf uit van opslagreplicatie | Verkleint gerepliceerde data en sluit de schijf uit van de replica. |

**Andere schijfopties beschrijven gedrag, geen ruimteherstel.** `format` geldt wanneer een backend meerdere imageformaten ondersteunt. `size` is virtuele capaciteit, niet toegewezen bytes. `ro=1` maakt de schijf alleen-lezen. `snapshot=1` schakelt QEMU's tijdelijke snapshotmodus in, die schijfwijzigingen bij het afsluiten van de VM weggooit. Dit is niet de instelling om een schijf in Proxmox VM-snapshots op te nemen. Vermijd dit voor persistente data. Controleer de hersteldekking voordat je `backup=0` of `replicate=0` gebruikt. [Proxmox VM-schijfopties](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Plak geen verkorte `qm set --scsi0`-regel over een bestaande schijf.** Bekijk **`qm config VMID`** en behoud de volledige volume-ID en bestaande opties bij het wijzigen. Een verkorte toewijzing kan andere schijfinstellingen verwijderen. Controleer in de interface na iedere wijziging de opgeslagen opties.

```bash
qm config 100
pvesm status
```

`100` is een voorbeeld-VM-ID. Voor een **nieuwe** SCSI-schijf van 64 GiB op een bestaande VM met controller **VirtIO SCSI single** en de vereiste driver in de gast laat dit commando de toewijzingssyntaxis zien. Vervang de VM-ID en opslag-ID door je eigen waarden.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Controleer of `scsi0` al bestaat voordat je het voorbeeld gebruikt.** Het commando wijzigt die sleuf. Gebruik voor een bestaande schijf de interface als het behouden van de exacte optiestring daar eenvoudiger is. Bekijk de [Proxmox-referentie voor de `qm`-opdracht](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Bestanden in het gastsysteem opruimen

**Maak eerst gastbestanden vrij.** Controleer Windows Opslaginstellingen, tijdelijke bestanden, oude installatieprogramma's, applicatiecaches en de prullenbak. Ruim databases en container-runtimes op via hun eigen interface. Actieve applicatiedata verwijderen om toewijzing te verlagen brengt gegevensverlies met zich mee.

**Controleer of het volume een discard-geschikte virtuele schijf gebruikt** en start een verhoogde PowerShell-sessie in de Windows-VM:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` geeft aan dat Windows verwijdermeldingen heeft ingeschakeld voor het gerapporteerde bestandssysteem. **ReTrim** verstuurt trimverzoeken voor ongebruikte delen van het volume opnieuw. Een geslaagde opdracht bevestigt dat de gast de bewerking heeft verzonden, niet hoeveel bytes de host terugwon. Controleer de host na afloop. [Microsoft-referentie voor `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) en [Proxmox-documentatie over VM-schijven](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Verwar QEMU guest agent niet met TRIM.** De agent ondersteunt gastbeheer en consistente back-ups. Verwijdermeldingen van het bestandssysteem lopen via de virtuele schijf. Alleen de agent installeren geeft geen blokken vrij. [Proxmox-documentatie over de VM guest agent](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Ongebruikte blokken in het bestandssysteem melden

**Controleer het blokpad en bestandssysteem voordat je trim uitvoert.** Een moderne distributie voert vaak periodiek `fstrim.timer` uit. Controleer de status en trim daarna aangekoppelde bestandssystemen nadat je onnodige gastdata hebt verwijderd.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** meldt discard-granulariteit en -limieten voor zichtbare blokapparaten. **`fstrim -av`** trimt ondersteunde aangekoppelde bestandssystemen en meldt verzonden bereiken. Verzonden bytes zijn niet gelijk aan bytes die naar de pool teruggaan. Versleutelde, LVM-, RAID- en andere gestapelde apparaten hebben discard-ondersteuning op elke laag nodig. [Red Hat-richtlijn voor ongebruikte blokken](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Gebruik geplande trim of een bewuste online discard-instelling. **Schakel niet op elk bestandssysteem voortdurend `discard` in als vervanging voor controle van het opslagpad.** Controleer na trim in de gast het PVE-volume en de pool. Controleer het eigen compactiebeleid van een database of service als verwijderde records nog ruimte in bestanden gebruiken.

## Containeropslag apart controleren

**LXC heeft geen geëmuleerde VM-schijfbus voor het rootbestandssysteem.** Begin met `pct config CTID` en zoek alle `rootfs`- en `mpN`-regels. Proxmox onderscheidt opslaggedragen mounts, bind mounts en apparaatmounts. Een pad in de container toont niet welk hostvolume eigenaar is van de blokken. [Proxmox-container-mountpoints](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Verwijder bij een **beheerd rootfs of mountpoint** bestanden vanuit de container of applicatie en controleer daarna het achterliggende volume en snapshots op de host. **Gebruik geen VM-`qm`-discardopdrachten op een CT.** Op ZFS-subvolumes houden snapshots verwijderde blokken vast. Controleer op directory- en LVM thin-opslag de werkelijke backendtoewijzing, niet de ingestelde CT-grootte.

Voer na opschoning van de CT **`pct fstrim` uit op de Proxmox-host** als de backend discard ondersteunt. Proxmox trimt het rootfs van de CT en geschikte beheerde mountpoints. Bind mounts en alleen-lezen mountpoints worden overgeslagen. Gebruik `--ignore-mountpoints` om alleen het rootfs te trimmen. Vergelijk het opslaggebruik voor en na. [Proxmox-referentie voor `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

De opdrachten tonen **alternatieve scopes** voor voorbeeld-CT-ID `101`. Gebruik de scope die bij je opslagindeling past. Een geslaagde trim garandeert geen gelijk aantal vrijgekomen bytes als snapshots oude blokken vasthouden.

**Proxmox beheert bind mounts en apparaatmounts niet.** De brondata blijft op de host of een extern apparaat. `vzdump`-back-ups van de container sluiten de inhoud uit. Extra opslaggedragen mountpoints zijn standaard ook uitgesloten, tenzij de optie `backup` ze insluit. Controleer het werkelijke back-upbeleid voordat je opschoont. [Proxmox-back-updocumentatie](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Controleer bij geneste Docker image-lagen, volumes en logs bij de werkelijke opslaghouder voordat je Docker-opruimopdrachten uitvoert. De [gids over Docker-betrouwbaarheid in LXC](/articles/docker-in-lxc-proxmox-reliability/) beschrijft grenzen voor mounts en back-ups. Een containerimage verwijderen verwijdert standaard geen blijvend volume.

## Meet de serverwaarden

**Leg voor en na de opschoning dezelfde metingen vast.** Vrije poolruimte is het uiteindelijke capaciteitsgegeven. Gebruik volumegegevens om te bepalen welke gast de groei veroorzaakte.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventariseert beheerde volumes en ingestelde groottes. Het meet geen toegewezen bytes op thin-opslag. Controleer voor **directory-opslag** het exacte mountpad en één bekend imagebestand. Vervang de paden door waarden uit **Datacenter > Storage** en de VM-configuratie.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Vergelijk voor een **gestopte VM** virtuele capaciteit en hosttoewijzing zonder het bestand te wijzigen:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Houd voor **LVM thin** zowel data als metadata van de pool in de gaten:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Splits voor **ZFS** actieve datasetdata en data die door snapshots wordt vastgehouden:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** meldt blokken die door alle snapshots van een dataset worden vastgehouden. Snapshotwaarden voor `used` zijn niet optelbaar omdat snapshots blokken delen. Verwijderde bestanden laten het poolgebruik mogelijk ongewijzigd totdat elke snapshot die naar hun blokken verwijst verloopt of volgens het bewaarbeleid wordt verwijderd. [OpenZFS-snapshots en klonen](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Koppel bij **Ceph RBD** eerst de Proxmox-volume-ID aan de image voordat je Ceph-opdrachten uitvoert. **`qm config VMID`** toont `STORAGE_ID:IMAGE`. Open de RBD-regel onder **Datacenter > Storage** voor de **pool** en eventuele **namespace**. De opslag-ID hoeft niet gelijk te zijn aan de poolnaam. Stel `POOL/IMAGE` samen uit de pool- en imagewaarden. Voer deze opdrachten uit op een client die voor het bedoelde Ceph-cluster is ingericht en geldige gegevens heeft. [Proxmox-documentatie over RBD-opslag](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** meldt toegewezen en werkelijk imagegebruik, inclusief bijbehorende snapshots. Zonder de imagefunctie `fast-diff` vraagt het OSD's op naar mogelijke objecten en kost het meer werk. **`ceph df`** toont pool- en clustercapaciteit. Replicatie, erasure coding en snapshots beïnvloeden het ruwe clustergebruik, zodat imagebytes en poolbytes verschillen. [Ceph RBD-opdrachtreferentie](https://docs.ceph.com/en/squid/man/8/rbd/) en [Ceph-richtlijn voor poolgebruik](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Voeg bij een RBD-opslag met namespace **`--namespace NAMESPACE`** toe aan elke `rbd`-opdracht. Gebruik de namespace die in Proxmox-opslag staat, niet de Proxmox-opslag-ID.

## Houd rekening met momentopnamen en back-ups

**Snapshots bewaren oudere versies van blokken.** Controleer het tabblad **Snapshots** van de VM of CT en de snapshotinventaris van de backend als gebruik na trim niet daalt. Controleer eigenaarschap en afhankelijkheden voordat je een snapshot verwijdert. Een back-up is een afzonderlijke kopie en volgt de bewaartermijn van back-upopslag, niet de huidige `df`-uitkomst van de gast.

**PBS-deduplicatie verandert de administratie.** De datastore bevat chunks die door back-ups worden gedeeld. Pruning verwijdert snapshotmetadata van back-ups. Garbage collection verwijdert later niet-verwezen chunks, na een respijtperiode. Controleer beide taken voordat je claimt dat back-upruimte is vrijgekomen. [PBS-onderhoudsdocumentatie](https://pbs.proxmox.com/docs/maintenance.html)

> **Waarschuwing:** Verwijder nooit een door Proxmox beheerd volumebestand, zvol of snapshot op basis van alleen de naam. Stel eerst de gast en het bewaarbeleid vast. Een opschoontaak moet de back-up- en terugvalroute behouden.

## Schijfbestand opnieuw maken terwijl de VM uitstaat

**Gebruik offlineconversie alleen als gewone trim in de gast en het backendpad een qcow2-toewijzingsprobleem niet oplossen.** Schakel de VM uit, controleer de back-up, stel alle snapshot- en backing-chainrelaties vast en schrijf een afzonderlijk doelimage. QEMU waarschuwt tegen het wijzigen van een image dat een ander proces gebruikt. [QEMU-documentatie over `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Kies liever een door Proxmox beheerde verplaatsing of back-up-en-herstel** als de schijf snapshots heeft of op beheerde blokopslag staat. Een losse `qemu-img convert` op een PVE-image werkt VM-configuratie, volume-eigenaarschap of snapshotverwijzingen niet vanzelf bij. Gebruik `qemu-img resize --shrink` niet om verwijderde bestanden terug te winnen. De zichtbare capaciteit verkleinen kan data afkappen als partities en bestandssystemen niet eerst zijn verkleind.

## Los mislukte ruimteherstel op

| Symptoom | Waarschijnlijke controle | Volgende stap |
|---|---|---|
| **`df` in gast daalt, host blijft gelijk** | VM-discardvlag, gasttrim, snapshots | Controleer de hele discard-route en vastgehouden snapshots. |
| **`fstrim` meldt niet ondersteund** | Schijfbus van gast, gestapelde blokapparaten, backend | Controleer `lsblk -D`, gastkernel en elke tussenlaag. |
| **Windows ReTrim eindigt, host blijft gelijk** | Backendtoewijzing, snapshots, serveradministratie | Vergelijk volume en pool. Controleer dat de schijf thin-opslag gebruikt. |
| **`ls -lh` en `du -h` verschillen** | Sparse- of qcow2-bestand | Gebruik `du` voor toegewezen bestandssysteemblokken. |
| **LVM thin pool blijft vol** | Data, metadata, snapshots | Controleer `lvs` en PVE-snapshots voordat je iets verwijdert. |
| **ZFS-pool blijft vol** | Snapshotblokken en reserveringen | Controleer `usedbysnapshots`, zvol-instellingen en poolcapaciteit. |
| **CT-`df` en pool verschillen** | Bind mounts, mountpoints, snapshots | Koppel `rootfs` en elk `mpN` aan de eigenaar op de host. |

**Controleer opnieuw nadat achtergrondtaken zijn afgerond.** Opslagadministratie kan achterlopen na trim, snapshotverwijdering of garbage collection van de backend. Vergelijk de gemeten vrije poolruimte met de beginwaarde. Leid succes niet alleen af uit de exitcode van een gastopdracht.

## Volgende stappen

**Houd voor elke gast een opslagoverzicht bij:** virtuele grootte, toegewezen bytes, backend, bus, discardvlag, aantal snapshots, back-updekking en vrije poolruimte. Kies één VM, schakel de ondersteunde discard-route in, trim in de gast en vergelijk de vastgelegde waarden. Herhaal dit pas als het resultaat overeenkomt met het verwachte gedrag van de backend.

Voor bredere herstelplanning volg je de [Proxmox-back-up- en hersteltest](/articles/proxmox-vm-backup-restore-drill/) en de [upgradegids van Proxmox VE 8 naar 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Bronnen

- [Proxmox VE-opslagbeheer](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), opslagtypen, thin provisioning en capaciteitsrisico's.
- [Proxmox VE LVM-opslag](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), VE 9-snapshotvolumeketens en toewijzing.
- [Proxmox VE RBD-opslag](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), pool- en namespaceconfiguratie.
- [Proxmox VE-virtuele machines](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), schijfbus, formaten, discard en gastagent.
- [Proxmox VE VM-schijfopties](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), busgebonden vlaggen.
- [containers van Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), rootbestandssystemen en eigenaarschap van mountpoints.
- [Proxmox VE-containeropdrachten](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim van containers op de host.
- [Proxmox VE-back-up en herstel](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), back-updekking van VM en CT.
- [Microsoft-documentatie voor `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), Windows ReTrim-syntaxis.
- [Red Hat-richtlijn voor ongebruikte blokken](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), Linux `fstrim`-gedrag.
- [OpenZFS-snapshots en klonen](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blokken die snapshots vasthouden.
- [Ceph RBD-opdrachtreferentie](https://docs.ceph.com/en/squid/man/8/rbd/), imagegebruik en snapshots.
- [NFSv4.2-specificatie](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), server-side ruimte vrijgeven.
- [PBS-onderhoudsdocumentatie](https://pbs.proxmox.com/docs/maintenance.html), pruning en garbage collection.
- [QEMU-hulpmiddel voor disk-images](https://www.qemu.org/docs/master/tools/qemu-img.html), veilige offline imageconversie.
