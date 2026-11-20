---
title: "Proxmox VE 9: reducerea spațiului ocupat de discurile virtuale și recuperarea spațiului"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Reduceți spațiul folosit de VM-uri și containere LXC în Proxmox VE 9. Comparați formatele și backendurile, activați discard, rulați trim și verificați snapshoturile înainte de recuperarea spațiului."
genre: ["Virtualizare", "Administrare Linux", "platforma Proxmox VE", "Stocare", "Laborator de acasă"]
tags: ["spațiu pe disc Proxmox VE 9", "alocare thin Proxmox", "notificări discard Proxmox", "comandă TRIM Proxmox", "Windows ReTrim pe Proxmox", "Linux fstrim pe Proxmox", "utilizarea discului LXC Proxmox", "alocare thin LVM Proxmox", "zvol sparse ZFS Proxmox", "dispozitive bloc Ceph RBD Proxmox", "format qcow2 Proxmox", "disc raw Proxmox", "instantanee Proxmox", "recuperarea spațiului de pe discul virtual", "tipuri de stocare Proxmox", "controler VirtIO SCSI", "detectarea scrierilor zero Proxmox", "stocare de backup Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Două grile de blocuri unite printr-o săgeată arată blocurile folosite de un disc virtual și capacitatea liberă dintr-un pool de stocare."
coverCaption: "Ștergerea din guest, discard și recuperarea spațiului sunt etape separate."
---

**Un sistem de fișiere mai mic în guest nu reduce întotdeauna spațiul folosit în Proxmox.** Pentru a elibera spațiu pe host, aveți nevoie de un disc compatibil cu thin provisioning, de un traseu discard funcțional pentru VM-uri și de un backend fără blocuri păstrate de snapshoturi. Acest ghid prezintă setările și verificările pentru VM-uri și containere LXC în Proxmox VE 9.

<!--more-->

## Idei principale

- **Alegeți mai întâi backendul.** Dimensiunea declarată a unui disc virtual diferă de spațiul alocat pe host numai dacă formatul imaginii sau backendul acceptă thin provisioning.
- **Activați discard pentru VM, apoi rulați trim în guest.** Windows ReTrim și Linux `fstrim` trimit cereri pentru blocurile neutilizate prin discul virtual.
- **Verificați separat snapshoturile și backupurile.** Blocurile vechi rămân alocate cât timp un snapshot face referire la ele. Fișierele de backup și chunk-urile PBS au propriile reguli de retenție.
- **Clasificați mount-urile LXC după tip.** Volumele rootfs și punctele de montare gestionate, bind mount-urile și montările de dispozitive au proprietari și comportamente de backup diferite.

## Înainte de a începe

Aveți nevoie de **acces de administrator la Proxmox VE 9**, de un backup verificat pentru fiecare guest afectat și de suficient spațiu liber în pool pentru operație. Notați ID-ul guestului, magistrala discului, ID-ul volumului, ID-ul stocării, snapshoturile și alocarea curentă înainte de a schimba setări. Folosiți [testul de restaurare VM](/articles/proxmox-vm-backup-restore-drill/) pentru a verifica recuperarea.

**Timp estimat:** 20–60 de minute pentru fiecare guest, plus orice operație amplă de trim sau curățare. **Dificultate:** Intermediară. Începeți cu o VM cu risc redus și comparați utilizarea stocării înainte și după.

> **Avertisment:** Un thin pool plin produce erori I/O în guesturi și poate deteriora sistemele de fișiere. Nu supralocați capacitatea fără să monitorizați spațiul liber pentru date și metadate din pool. [Documentația de stocare Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Urmăriți lanțul de alocare

**Ștergerea**, **discard** și **recuperarea** au loc la niveluri diferite. Guestul șterge un fișier și marchează blocurile sistemului de fișiere ca libere. Sistemul de fișiere trimite TRIM sau UNMAP pentru aceste blocuri. QEMU transmite cererea mai departe dacă discard este activat pe discul virtual. Backendul eliberează alocarea fizică dacă formatul și poolul acceptă operația. [Documentația Proxmox despre discurile VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Nivel | Ce verificați | Dovadă utilă |
|---|---|---|
| **Fișierele guestului** | Spațiul liber din sistemul de fișiere | Proprietățile volumului Windows sau Linux `df -h` |
| **Disc virtual** | Magistrală, discard, emulare SSD, format imagine | Fila VM **Hardware** sau `qm config VMID` |
| **Volum PVE** | Proprietar și dimensiune configurată | Fila **Content** a stocării sau `pvesm list STORAGE_ID` |
| **Pool de stocare** | Date și metadate libere, blocuri păstrate | `pvesm status` și utilitare specifice backendului |

**Un disc virtual de 100 GiB stabilește o limită de capacitate, nu garantează o alocare de 100 GiB.** În schimb, faptul că guestul raportează 20 GiB utilizați nu dovedește că hostul folosește 20 GiB. Metadatele, snapshoturile, copiile de backup și blocurile scrise anterior modifică valoarea. [Documentația de stocare Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Comparați formatele de disc

**Backendul de stocare decide ce formate de imagine oferă Proxmox.** zvol-urile ZFS și Ceph RBD folosesc discuri virtuale raw. LVM folosește de regulă raw, cu o excepție Proxmox VE 9 pentru lanțurile de volume descrisă mai jos. Backendurile de fișiere precum directory și NFS acceptă raw sau qcow2. Raw nu oferă singur alocare thin sau snapshoturi. Stocarea subiacentă trebuie să furnizeze aceste funcții. Qcow2 oferă alocare copy-on-write și snapshoturi la nivelul imaginii. [Documentația Proxmox despre discurile VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Mecanism de alocare | Compromis de spațiu |
|---|---|---|
| **qcow2 pe stocare de fișiere** | Qcow2 alocă clustere când sunt scrise | Metadatele imaginii și lanțurile de snapshoturi ocupă spațiu |
| **fișier raw pe stocare de fișiere** | Comportament de fișier rar al sistemului de fișiere, dacă este acceptat | Raw nu oferă singur thin provisioning sau snapshoturi |
| **volum bloc raw** | LVM thin, ZFS, Ceph RBD sau alt backend | Alocarea poolului și snapshoturile depind de backend |

**Proxmox VE 9 thick LVM are un mod special de snapshot.** `snapshot-as-volume-chain` folosește relații qcow2 de backing între volume logice thick LVM. Nu utilizează snapshoturi interne qcow2. Opțiunea afectează doar discurile VM create ulterior și este încă o previzualizare tehnologică în documentația Proxmox curentă. PVE afișează fiecare snapshot ca fiind alocat integral. Alocarea SAN reală este mai mică numai când stocarea subiacentă acceptă thin provisioning și discard. [Documentația de stocare LVM Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Nu convertiți un disc doar pentru că extensia este `.raw`.** Verificați mai întâi pluginul de stocare și blocurile alocate. Un disc raw pe `local-lvm` se alocă diferit de un fișier raw alocat integral pe stocare directory obișnuită.

## Comparați tipurile de stocare

Proxmox separă **stocarea de fișiere** de **stocarea bloc**. Pluginul de stocare controlează și snapshoturile, clonele, partajarea și tipurile de conținut acceptate de fiecare pool. Verificați intrarea **Datacenter > Storage** înainte să vă bazați pe un format sau o funcție. [Tabelul tipurilor de stocare Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Stocare | Comportamentul discului VM | Verificare pentru recuperare |
|---|---|---|
| **Directory, ext4, XFS** | Fișiere raw sau qcow2 | Comparați octeții alocați de `du` cu dimensiunea virtuală a imaginii. Verificați snapshoturile dacă o altă stocare le furnizează. |
| **NFS, CIFS** | Fișiere raw sau qcow2 pe stocare partajată | Verificați spațiul alocat pe server. Rezultatul trim al guestului nu dovedește că serverul a eliberat spațiu. |
| **LVM cu alocare thin (`local-lvm`)** | Volume logice raw thin, numai local | Urmăriți cu `lvs` procentele de date și metadate ale thin poolului. |
| **LVM thick** | LV-uri raw sau lanțuri de volume qcow2 VE 9 | Ștergerea din guest nu reduce rezervarea fixă a LV-ului. Verificați separat alocarea thin SAN. |
| **Stocare ZFS (`local-zfs`)** | zvol-uri raw sau subvolume de containere | Verificați `sparse`, proprietățile datasetului, utilizarea poolului și snapshoturile. |
| **Ceph RBD** | Imagini RBD raw thin pe stocare partajată | Verificați capacitatea poolului Ceph, utilizarea imaginii, snapshoturile și discard. |
| **Btrfs** | Volume bazate pe fișiere, cu subvolume Btrfs pentru imagini raw | Tratați pluginul Btrfs PVE ca previzualizare tehnologică și verificați snapshoturile și utilizarea sistemului de fișiere. |

**Alte pluginuri de stocare au roluri diferite.** CephFS oferă stocare de fișiere partajată. iSCSI și Fibre Channel expun dispozitive bloc partajate, adesea împărțite în volume VM cu LVM. ZFS over iSCSI folosește stocare bloc la distanță susținută de ZFS. Proxmox Backup Server (PBS) stochează backupuri, nu discuri VM active. Verificați tipurile **Content** activate înainte să plasați acolo date `images`, `rootdir`, `backup` sau `iso`. [Tabelul tipurilor de stocare Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Opțiunile de alocare pentru stocarea de fișiere contează la crearea discului.** Setarea `format` a stocării alege `raw`, `qcow2` sau `vmdk` dacă sunt acceptate. `preallocation` pentru fișiere raw și qcow2 acceptă `off`, `metadata`, `falloc` sau `full`. Valoarea implicită este `metadata`, tratată ca `off` pentru raw. `full` rezervă spațiul fișierului în avans și elimină amprenta inițială mică obișnuită. Verificați configurația înainte de a crea un disc mare. Indicatorul `shared` declară doar accesul partajat existent. Nu face stocarea locală partajată. [Proprietăți comune de stocare Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` este setarea de stocare pentru crearea zvol-urilor thin.** Fără zvol-uri sparse, crearea rezervă capacitate conform comportamentului configurat al volumului. Inspectați configurația stocării și poolului înainte de a schimba un mediu existent. [Documentația Proxmox pentru stocarea ZFS](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Stocarea directory necesită o a doua verificare.** Lungimea logică a unui fișier qcow2 nu este capacitatea virtuală vizibilă pentru guest. `du -h` raportează blocurile sistemului de fișiere alocate imaginii. `ls -lh` arată lungimea logică a fișierului. Pentru o VM oprită, `qemu-img info` raportează capacitatea virtuală și dimensiunea pe host. Pentru NFS, bazați deciziile finale pe evidența serverului. [Referința QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS are încă o limită de alocare.** Faptul că qcow2 reutilizează un cluster gol din fișierul său nu înseamnă că serverul NFS eliberează blocurile fișierului. Eliberarea spațiilor necesită suportul clientului, protocolului negociat, serverului și sistemului său de fișiere. NFSv4.2 definește `DEALLOCATE`, dar numărul versiunii nu dovedește că serverul a returnat spațiu. Verificați montarea NFS negociată și măsurați alocarea pe server. [Specificația NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Configurați indicatorii discului VM

În interfața Proxmox, deschideți **VM > Hardware > Hard Disk > Edit**. Verificați magistrala discului și opțiunile avansate. Acești indicatori influențează alocarea sau arată dacă o optimizare este utilă. [Referința oficială pentru opțiunile `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) enumeră disponibilitatea pe magistrale.

| Magistrală | Alegere legată de spațiu |
|---|---|
| **IDE** | Compatibilitate veche. Folosiți-o doar când guestul nu are un driver mai nou. |
| **SATA** | Emulare acceptată pe scară largă. Verificați trim în guest și opțiunile discului înainte de recuperare. |
| **SCSI cu VirtIO SCSI** | Calea modernă preferată pentru discard și setări per disc. Windows are nevoie de driverul VirtIO. |
| **VirtIO Block** | Disc paravirtualizat. Discard pe Linux necesită kernel 5.0 sau mai nou. Emularea SSD nu este disponibilă. |

| Setare | Efect | Recomandare |
|---|---|---|
| **Transmite discard (`on`)** | Transmite TRIM sau UNMAP din guest | Necesară pentru recuperare inițiată de guest pe un backend thin compatibil. Valoarea implicită `ignore` blochează transmiterea. |
| **Emulare SSD `ssd=1`** | Prezintă discul ca SSD către guest | Unii guesturi au nevoie de această identitate înainte să trimită trim. Indicatorul nu accelerează stocarea fizică. VirtIO Block nu oferă acest indicator. |
| **Detect zeroes `detect_zeroes=1`** | Detectează și încearcă să optimizeze scrierile cu zerouri | Optimizare I/O opțională. Nu înlocuiește trim și nu garantează spațiu recuperat. |
| **Magistrală: SCSI / VirtIO SCSI single** | Expune un disc SCSI prin controlerul VirtIO | Setare practică pentru guesturi moderne Windows și Linux. Instalați driverele VirtIO pentru Windows. |
| **Magistrală: VirtIO Block** | Folosește dispozitivul bloc VirtIO | Discard pe Linux necesită kernel 5.0 sau mai nou. Emularea SSD nu este disponibilă. |
| **Thread I/O `iothread=1`** | Alocă I/O-ul discului unui thread separat | Folosiți cu VirtIO Block sau SCSI pe controler VirtIO SCSI single. Este o setare de performanță, nu de recuperare. |
| **Cache și AIO** | Schimbă bufferingul I/O și I/O-ul asincron | Ajustați-le la sarcină și backend. Niciuna nu micșorează un disc. |
| **Backup `backup=0`** | Exclude discul din backupurile VM | Reduce aria backupului și scoate datele discului din recuperarea VM. Documentați un backup separat. |
| **Replicare `replicate=0`** | Exclude discul din replicarea stocării | Reduce datele replicate și scoate discul din replică. |

**Alte opțiuni ale unității descriu comportamentul, nu recuperarea.** `format` se aplică alocării pe un backend cu mai multe formate de imagine. `size` este capacitatea virtuală, nu octeții alocați. `ro=1` face discul doar pentru citire. `snapshot=1` activează modul de snapshot temporar QEMU, care renunță la modificările discului la închiderea VM-ului. Nu este opțiunea pentru includerea unui disc în snapshoturile VM Proxmox. Evitați-o pentru date persistente. Verificați acoperirea restaurării înainte de a folosi `backup=0` sau `replicate=0`. [Opțiuni de disc VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Nu lipiți o comandă `qm set --scsi0` prescurtată peste o unitate existentă.** Inspectați **`qm config VMID`** și păstrați ID-ul complet al volumului și opțiunile existente când editați. O atribuire prescurtată poate elimina alte setări ale discului. În interfață, verificați opțiunile salvate după fiecare modificare.

```bash
qm config 100
pvesm status
```

`100` este un ID VM de exemplu. Pentru un disc SCSI **nou** de 64 GiB pe o VM existentă cu controler **VirtIO SCSI single** și cu driverul necesar în guest, această comandă arată sintaxa de alocare. Înlocuiți ID-ul VM și ID-ul stocării cu valorile proprii.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Verificați dacă `scsi0` există înainte de a folosi exemplul.** Comanda modifică slotul. Pentru un disc existent, folosiți interfața dacă păstrarea șirului exact de opțiuni este mai ușoară. Consultați [referința comenzii Proxmox `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Curățați fișierele sistemului invitat

**Eliberați mai întâi fișierele guestului.** Verificați setările Storage din Windows, fișierele temporare, instalatoarele vechi, cache-urile aplicațiilor și coșul de reciclare. Curățați bazele de date și runtime-urile de containere din interfața lor. Ștergerea datelor active ale aplicației doar pentru reducerea alocării poate pierde date.

**Confirmați că volumul folosește un disc virtual compatibil cu discard**, apoi porniți o sesiune PowerShell elevată în VM-ul Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indică faptul că Windows a activat notificările de ștergere pentru sistemul de fișiere raportat. **ReTrim** retrimite cereri pentru regiunile volumului neutilizate în prezent. Finalizarea cu succes confirmă că guestul a trimis operația, nu câți octeți a recuperat hostul. Verificați hostul după terminarea lucrării. [Referința Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) și [documentația Proxmox despre discurile VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Nu confundați QEMU guest agent cu TRIM.** Agentul acceptă controlul guestului și funcții de consistență a backupurilor. Notificările de ștergere ale sistemului de fișiere circulă prin discul virtual. Instalarea agentului singură nu recuperează blocuri. [Documentația Proxmox pentru guest agent VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Raportați blocurile neutilizate ale sistemului de fișiere

**Verificați calea blocurilor și sistemul de fișiere înainte de trim.** O distribuție modernă rulează adesea periodic `fstrim.timer`. Verificați starea, apoi rulați trim pe sistemele montate după ștergerea datelor guest inutile.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** raportează granularitatea și limitele discard pentru dispozitivele bloc vizibile. **`fstrim -av`** execută trim pe sistemele montate compatibile și raportează intervalele trimise. Octeții trimiși nu sunt egali cu octeții returnați poolului. Dispozitivele criptate, LVM, RAID și alte straturi necesită discard la fiecare nivel. [Ghid Red Hat pentru blocuri neutilizate](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Folosiți trim programat sau o politică online discard deliberată. **Nu activați `discard` continuu pe fiecare sistem de fișiere în loc să verificați calea de stocare.** După trim în guest, inspectați volumul și poolul PVE. Verificați politica de compactare proprie a unei baze de date sau unui serviciu dacă înregistrările șterse încă ocupă fișiere.

## Verificați separat stocarea containerelor

**LXC nu are o magistrală de disc VM emulată pentru sistemul de fișiere root.** Începeți cu `pct config CTID` și identificați fiecare intrare `rootfs` și `mpN`. Proxmox definește mount-uri bazate pe stocare, bind mount-uri și mount-uri de dispozitive. O cale vizibilă în container nu indică volumul host care deține blocurile. [Puncte de montare pentru containere Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Pentru un **rootfs sau punct de montare gestionat**, eliminați fișierele din container sau aplicație, apoi inspectați pe host volumul subiacent și snapshoturile. **Nu rulați comenzi `qm` de discard VM pe un CT.** Pe subvolume ZFS, snapshoturile păstrează blocurile șterse. Pe stocare directory și LVM thin, verificați alocarea backendului, nu dimensiunea configurată a CT-ului.

Rulați **`pct fstrim` pe hostul Proxmox** după curățarea CT-ului când stocarea subiacentă acceptă discard. Proxmox execută trim pe rootfs-ul CT-ului și pe punctele de montare gestionate eligibile. Omite bind mount-urile și punctele montate doar pentru citire. Folosiți `--ignore-mountpoints` pentru trim doar pe rootfs. Comparați utilizarea stocării înainte și după. [Referința Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Comenzile arată **domenii alternative** pentru ID-ul CT exemplu `101`. Rulați domeniul potrivit pentru structura stocării. Un trim reușit nu garantează același număr de octeți eliberați dacă snapshoturile păstrează blocuri vechi.

**Bind mount-urile și mount-urile de dispozitive nu sunt gestionate de Proxmox.** Datele lor sursă rămân pe host sau pe dispozitiv extern. Backupurile `vzdump` ale containerului le exclud conținutul. Punctele de montare suplimentare bazate pe stocare sunt și ele excluse implicit, dacă opțiunea `backup` nu le include. Verificați politica reală de backup înainte de curățare. [Documentația de backup Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Pentru Docker imbricat, inspectați straturile imaginii, volumele și jurnalele la proprietarul real al stocării înainte să folosiți comenzile de curățare Docker. [Ghidul de fiabilitate Docker în LXC](/articles/docker-in-lxc-proxmox-reliability/) explică limitele mounturilor și backupurilor. Ștergerea unei imagini de container nu șterge implicit un volum persistent.

## Măsurați corect serverul

**Înregistrați aceleași măsurători înainte și după curățare.** Spațiul liber din pool este indicatorul final de capacitate. Folosiți valorile pe volume pentru a găsi guestul care a generat creșterea.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventariază volumele gestionate și dimensiunile configurate. Nu măsoară octeții alocați în stocarea thin. Pentru stocarea **directory**, inspectați calea montată exactă și un fișier imagine cunoscut. Înlocuiți căile cu cele din **Datacenter > Storage** și configurația VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Pentru o VM **oprită**, comparați capacitatea virtuală și alocarea pe host a imaginii fără să modificați fișierul:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Pentru **LVM thin**, urmăriți datele și metadatele poolului:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Pentru **ZFS**, separați datele active ale datasetului de cele păstrate de snapshoturi:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** raportează blocurile reținute de toate snapshoturile datasetului. Valorile `used` ale snapshoturilor nu se adună pentru că acestea partajează blocuri. Un fișier șters poate lăsa neschimbată utilizarea poolului până expiră sau este eliminat, conform politicii de retenție, fiecare snapshot care face referire la blocurile lui. [Snapshoturi și clone OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Pentru **Ceph RBD**, mapați ID-ul volumului Proxmox înainte de comenzile Ceph. **`qm config VMID`** afișează `STORAGE_ID:IMAGE`. Deschideți intrarea RBD din **Datacenter > Storage** ca să găsiți **poolul** și **namespace-ul** opțional. ID-ul stocării poate fi diferit de numele poolului. Construiți `POOL/IMAGE` din valorile poolului și imaginii. Rulați comenzile de pe un client configurat pentru clusterul Ceph dorit, cu acreditări valide. [Documentația Proxmox pentru stocarea RBD](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** raportează utilizarea provizionată și reală a imaginii, inclusiv snapshoturile asociate. Fără funcția de imagine `fast-diff`, interoghează OSD-urile pentru posibile obiecte și necesită mai mult lucru. **`ceph df`** arată capacitatea poolului și clusterului. Replicarea, codarea cu ștergere și snapshoturile afectează utilizarea brută a clusterului, deci octeții imaginii și poolului diferă. [Referința comenzilor Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) și [ghidul Ceph despre utilizarea poolului](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Dacă stocarea RBD folosește un namespace, adăugați **`--namespace NAMESPACE`** la fiecare comandă `rbd`. Folosiți namespace-ul configurat în intrarea de stocare Proxmox, nu ID-ul de stocare Proxmox.

## Luați în calcul snapshoturile și backupurile

**Snapshoturile păstrează versiuni vechi ale blocurilor.** Dacă utilizarea nu scade după trim, verificați fila **Snapshots** a VM-ului sau CT-ului și inventarul de snapshoturi al backendului. Inspectați proprietarul și dependențele înainte să ștergeți ceva. Un backup este o copie separată și respectă retenția stocării de backup, nu valoarea curentă `df` din guest.

**Deduplicarea PBS modifică evidența spațiului.** Datastore-ul conține chunk-uri partajate între backupuri. Pruning elimină metadatele snapshoturilor de backup. Garbage collection elimină ulterior chunk-urile nereferențiate, după o perioadă de așteptare. Verificați ambele sarcini înainte să afirmați că s-a recuperat capacitate de backup. [Documentația PBS pentru mentenanță](https://pbs.proxmox.com/docs/maintenance.html)

> **Avertisment:** Nu ștergeți niciodată un fișier de volum gestionat de Proxmox, un zvol sau un snapshot doar pe baza numelui. Identificați mai întâi guestul și politica de retenție. Curățarea stocării trebuie să păstreze backupul și calea de revenire.

## Reconstruiți imaginea discului cu VM oprită

**Folosiți conversia offline doar dacă trim normal în guest și calea backendului nu rezolvă problema de alocare qcow2.** Opriți VM-ul, verificați backupul, identificați toate relațiile snapshot și backing chain și scrieți într-o imagine de destinație separată. QEMU avertizează să nu modificați o imagine folosită de alt proces. [Documentația QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Preferați o mutare gestionată de Proxmox sau fluxul backup și restaurare** când discul are snapshoturi sau se află pe stocare bloc gestionată. Un `qemu-img convert` separat asupra unei imagini deținute de PVE nu actualizează singur configurația VM, proprietatea volumului sau referințele snapshot. Nu folosiți `qemu-img resize --shrink` pentru recuperarea fișierelor șterse. Reducerea capacității vizibile pentru guest poate trunchia date dacă partițiile și sistemele de fișiere nu au fost micșorate mai întâi.

## Depanați o recuperare eșuată

| Simptom | Verificare probabilă | Următoarea acțiune |
|---|---|---|
| **`df` în guest scade, hostul rămâne la fel** | Flag discard VM, trim guest, snapshoturi | Verificați întregul traseu discard și snapshoturile păstrate. |
| **`fstrim` raportează că nu este acceptat** | Magistrală disc guest, dispozitive suprapuse, backend | Verificați `lsblk -D`, kernelul guestului și fiecare strat intermediar. |
| **Windows ReTrim se termină, hostul rămâne la fel** | Alocare backend, snapshoturi, contabilitatea serverului | Comparați volumul și poolul. Confirmați că discul folosește stocare thin. |
| **`ls -lh` și `du -h` diferă** | Fișier sparse sau qcow2 | Folosiți `du` pentru blocurile alocate în sistemul de fișiere. |
| **Thin pool LVM rămâne plin** | Date, metadate, snapshoturi | Verificați `lvs` și snapshoturile PVE înainte de eliminări. |
| **Poolul ZFS rămâne plin** | Blocuri păstrate de snapshoturi și rezervări | Verificați `usedbysnapshots`, setările zvol și capacitatea poolului. |
| **`df` CT și poolul diferă** | Bind mount-uri, puncte de montare, snapshoturi | Asociați `rootfs` și fiecare `mpN` cu proprietarul de pe host. |

**Verificați din nou după finalizarea lucrărilor în fundal.** Evidența stocării poate întârzia după trim, ștergerea unui snapshot sau garbage collection în backend. Comparați spațiul liber măsurat în pool cu valoarea inițială. Nu deduceți succesul doar din codul de ieșire al unei comenzi din guest.

## Pașii următori

**Creați o evidență a stocării pentru fiecare guest:** dimensiune virtuală, octeți alocați, backend, magistrală, flag discard, număr de snapshoturi, acoperirea backupului și spațiul liber din pool. Alegeți o VM, activați traseul discard acceptat, rulați trim în guest și comparați valorile înregistrate. Repetați doar dacă rezultatul primei VM corespunde comportamentului backendului.

Pentru un plan mai amplu de recuperare, urmați [testul Proxmox de backup și restaurare](/articles/proxmox-vm-backup-restore-drill/) și [ghidul de upgrade Proxmox VE 8 la 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Surse

- [Administrarea stocării Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), tipuri de stocare, thin provisioning și riscuri de capacitate.
- [Stocarea LVM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), lanțuri de volume snapshot VE 9 și alocare.
- [Stocarea RBD Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configurarea poolurilor și namespace-urilor.
- [Mașini virtuale Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), magistrale de disc, formate, discard și guest agent.
- [Opțiuni disc VM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), flaguri specifice magistralei.
- [Containere Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), sisteme de fișiere root și proprietatea punctelor de montare.
- [Comenzi containere Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim pentru containere de pe host.
- [Backup și restaurare Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), acoperirea backupurilor VM și CT.
- [documentația Microsoft pentru `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), sintaxa Windows ReTrim.
- [Ghid Red Hat pentru blocuri neutilizate](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportamentul Linux `fstrim`.
- [Snapshoturi și clone OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocuri păstrate de snapshoturi.
- [Referința comenzilor Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), utilizarea imaginilor și snapshoturile.
- [Specificația NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), dezalocarea spațiului pe server.
- [Documentația PBS pentru mentenanță](https://pbs.proxmox.com/docs/maintenance.html), pruning și garbage collection.
- [Utilitarul pentru imagini de disc QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), siguranța conversiei offline.
