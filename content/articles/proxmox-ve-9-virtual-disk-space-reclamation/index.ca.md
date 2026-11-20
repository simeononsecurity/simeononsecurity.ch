---
title: "Proxmox VE 9: redueix l'ús dels discos virtuals i recupera espai"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Redueix l'emmagatzematge de les VM i els contenidors LXC a Proxmox VE 9. Compara formats i backends, activa discard, executa trim i revisa les instantànies abans de recuperar espai."
genre: ["Virtualització", "Administració de Linux", "plataforma Proxmox VE", "Emmagatzematge", "Laboratori domèstic"]
tags: ["espai de disc Proxmox VE 9", "assignació fina Proxmox", "notificacions discard Proxmox", "ordre TRIM Proxmox", "Windows ReTrim a Proxmox", "Linux fstrim a Proxmox", "ús de disc LXC Proxmox", "assignació fina LVM Proxmox", "zvol dispers ZFS Proxmox", "dispositius de blocs Ceph RBD Proxmox", "format qcow2 Proxmox", "disc raw Proxmox", "instantànies Proxmox", "recuperació d espai del disc virtual", "tipus d emmagatzematge Proxmox", "controlador VirtIO SCSI", "detecció d escriptures de zeros Proxmox", "emmagatzematge de còpies Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Dues graelles de blocs unides amb una fletxa mostren els blocs ocupats d'un disc virtual i la capacitat lliure d'un grup d'emmagatzematge."
coverCaption: "Esborrar dades del guest, enviar discard i recuperar espai són passos diferents."
---

**Un sistema de fitxers del guest més petit no sempre redueix l'espai utilitzat a Proxmox.** Per alliberar espai a l'amfitrió, cal un disc compatible amb thin provisioning, una ruta discard operativa per a les VM i un emmagatzematge de suport sense blocs retinguts per instantànies. Aquesta guia cobreix els ajustos i les comprovacions de les VM i els contenidors LXC de Proxmox VE 9.

<!--more-->

## Idees clau

- **Tria primer l'emmagatzematge de suport.** La mida anunciada d'un disc virtual només difereix de l'espai assignat a l'amfitrió si el format de la imatge o el backend admet thin provisioning.
- **Activa discard a la VM i després executa trim al guest.** Windows ReTrim i Linux `fstrim` envien sol·licituds per als blocs no utilitzats a través del disc virtual.
- **Comprova les instantànies i les còpies per separat.** Els blocs antics continuen assignats mentre una instantània hi fa referència. Els fitxers de còpia i els blocs PBS segueixen les seves pròpies regles de retenció.
- **Classifica els muntatges LXC pel tipus.** Els volums rootfs i els punts de muntatge gestionats, els bind mounts i els muntatges de dispositius tenen propietaris i comportaments de còpia diferents.

## Abans de començar

Necessites **accés d'administrador a Proxmox VE 9**, una còpia de seguretat verificada de cada guest afectat i prou espai lliure al grup per fer l'operació. Anota l'ID del guest, el bus del disc, l'ID del volum, l'ID de l'emmagatzematge, les instantànies i l'assignació actual abans de canviar res. Fes el [simulacre de restauració de VM](/articles/proxmox-vm-backup-restore-drill/) per provar la recuperació.

**Temps estimat:** de 20 a 60 minuts per guest, més qualsevol tasca llarga de trim o neteja. **Dificultat:** Mitjana. Comença amb una VM de baix risc i compara l'ús de l'emmagatzematge abans i després.

> **Avís:** Un grup thin ple provoca errors d'E/S als guests i posa en risc els sistemes de fitxers. No sobreassignis capacitat sense vigilar l'espai lliure de dades i metadades del grup. [Documentació d'emmagatzematge de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Segueix la cadena d'assignació

**L'esborrament**, **discard** i la **recuperació** passen en capes diferents. El guest esborra un fitxer i marca lliures els blocs del sistema de fitxers. El sistema de fitxers envia TRIM o UNMAP per a aquests blocs. QEMU reenvia la sol·licitud si discard està activat al disc virtual. El backend allibera l'assignació física si el format i el grup admeten l'operació. [Documentació de discos VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Capa | Què cal comprovar | Evidència útil |
|---|---|---|
| **Fitxers del guest** | Espai lliure del sistema de fitxers | Propietats del volum de Windows o Linux `df -h` |
| **Disc virtual** | Bus, discard, emulació SSD, format d'imatge | Pestanya **Hardware** de la VM o `qm config VMID` |
| **Volum PVE** | Propietari i mida configurada | Pestanya **Content** de l'emmagatzematge o `pvesm list STORAGE_ID` |
| **Grup d'emmagatzematge** | Dades i metadades lliures, blocs retinguts | `pvesm status` i eines específiques del backend |

**Un disc virtual de 100 GiB fixa un límit de capacitat, no garanteix 100 GiB assignats.** A la inversa, que el guest indiqui 20 GiB en ús no demostra que l'amfitrió n'utilitzi 20. Les metadades, les instantànies, les còpies i els blocs escrits anteriorment alteren el valor. [Documentació d'emmagatzematge de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Estructura dels fitxers de disc

**El backend d'emmagatzematge determina quins formats d'imatge ofereix Proxmox.** Els zvol de ZFS i Ceph RBD utilitzen discos virtuals raw. LVM normalment utilitza raw, amb una excepció de cadena de volums de Proxmox VE 9 que s'explica més avall. Els backends de fitxers com directory i NFS admeten raw o qcow2. Raw no proporciona thin provisioning ni instantànies per si sol. L'emmagatzematge subjacent ha d'oferir aquestes funcions. Qcow2 proporciona assignació copy-on-write i instantànies a la capa de la imatge. [Documentació de discos VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Format | Mecanisme d'assignació | Cost en espai |
|---|---|---|
| **qcow2 en emmagatzematge de fitxers** | Qcow2 assigna clústers quan s'escriuen | Les metadades de la imatge i les cadenes d'instantànies consumeixen espai |
| **Fitxer raw en emmagatzematge de fitxers** | Fitxer dispers del sistema de fitxers, si s'admet | Raw tot sol no ofereix thin provisioning ni instantànies |
| **Volum de blocs raw** | LVM thin, ZFS, Ceph RBD o un altre suport | L'assignació del grup i les instantànies depenen del backend |

**Proxmox VE 9 thick LVM té un mode especial d'instantànies.** `snapshot-as-volume-chain` utilitza relacions qcow2 de backing entre volums lògics thick LVM. No utilitza instantànies internes de qcow2. L'opció només afecta discos VM nous i continua sent una vista prèvia tecnològica a la documentació actual de Proxmox. PVE mostra cada instantània com si estigués completament assignada. L'assignació real a la SAN només és menor si l'emmagatzematge subjacent admet thin provisioning i discard. [Documentació d'emmagatzematge LVM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**No converteixis un disc només perquè l'extensió sigui `.raw`.** Comprova primer el connector d'emmagatzematge i els blocs assignats. Un disc raw a `local-lvm` té un comportament diferent d'un fitxer raw completament assignat a l'emmagatzematge directory normal.

## Compara tipus d'emmagatzematge

Proxmox separa **emmagatzematge de fitxers** i **emmagatzematge de blocs**. El connector també controla les instantànies, els clons, l'ús compartit i els tipus de contingut acceptats per cada grup. Revisa l'entrada **Datacenter > Storage** abans de confiar en un format o una funció. [Taula de tipus d'emmagatzematge de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Emmagatzematge | Comportament del disc VM | Comprovació de recuperació |
|---|---|---|
| **Directory, ext4, XFS** | Fitxers raw o qcow2 | Compara els bytes assignats per `du` amb la mida virtual de la imatge. Comprova les instantànies si les ofereix una altra capa. |
| **NFS, CIFS** | Fitxers raw o qcow2 en emmagatzematge compartit | Comprova l'espai assignat al servidor. El resultat trim del guest no demostra que el servidor hagi alliberat espai. |
| **LVM amb assignació fina (`local-lvm`)** | Volums lògics raw thin, només locals | Vigila amb `lvs` els percentatges de dades i metadades del thin pool. |
| **LVM thick** | LV raw o cadenes de volums qcow2 VE 9 | Esborrar dades al guest no redueix la reserva fixa del LV. Comprova per separat l'assignació thin de la SAN. |
| **Emmagatzematge ZFS (`local-zfs`)** | zvol raw o subvolums de contenidors | Comprova `sparse`, les propietats del conjunt de dades, l'ús del grup i les instantànies. |
| **Ceph RBD** | Imatges RBD raw thin en emmagatzematge compartit | Comprova la capacitat del grup Ceph, l'ús de la imatge, les instantànies i discard. |
| **Btrfs** | Volums basats en fitxers amb subvolums Btrfs per a imatges raw | Tracta el connector Btrfs de PVE com una vista prèvia tecnològica i examina les instantànies i l'ús del sistema de fitxers. |

**Altres connectors d'emmagatzematge serveixen per a altres funcions.** CephFS ofereix emmagatzematge de fitxers compartit. iSCSI i Fibre Channel exposen dispositius de blocs compartits, sovint dividits en volums VM amb LVM. ZFS over iSCSI utilitza emmagatzematge remot de blocs recolzat per ZFS. Proxmox Backup Server (PBS) emmagatzema còpies, no discos VM actius. Comprova els tipus de **Content** habilitats abans de desar-hi dades `images`, `rootdir`, `backup` o `iso`. [Taula de tipus d'emmagatzematge de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**Els indicadors d'assignació de l'emmagatzematge de fitxers importen quan es crea el disc.** El valor `format` de l'emmagatzematge tria `raw`, `qcow2` o `vmdk` quan s'admeten. `preallocation` per a fitxers raw i qcow2 accepta `off`, `metadata`, `falloc` o `full`. El valor predeterminat és `metadata`, tractat com `off` per a raw. `full` reserva tot l'espai del fitxer per avançat i elimina la petita ocupació inicial habitual. Revisa la configuració abans de crear un disc gran. L'indicador `shared` només declara un accés compartit existent. No converteix l'emmagatzematge local en compartit. [Propietats comunes d'emmagatzematge de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**`sparse` de ZFS és l'ajust d'emmagatzematge per crear zvol thin.** Sense zvol sparse, la creació reserva capacitat segons el comportament configurat del volum. Inspecciona la configuració real de l'emmagatzematge i el grup abans de canviar un desplegament existent. [Documentació d'emmagatzematge ZFS de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**L'emmagatzematge directory requereix una segona comprovació.** La longitud lògica d'un fitxer qcow2 no és la capacitat virtual visible per al guest. `du -h` mostra els blocs del sistema de fitxers assignats a la imatge. `ls -lh` mostra la longitud lògica del fitxer. Per a una VM aturada, `qemu-img info` indica la capacitat virtual i la mida a l'amfitrió. A NFS, confia en la comptabilitat del servidor per a les decisions finals de capacitat. [Referència de QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS té un altre límit d'assignació.** Que qcow2 reutilitzi un clúster buit dins del seu fitxer no vol dir que el servidor NFS alliberi blocs del fitxer. Hole punching necessita compatibilitat del client, el protocol negociat, el servidor i el seu sistema de fitxers. NFSv4.2 defineix `DEALLOCATE`, però el número de versió no demostra que el servidor hagi retornat espai. Inspecciona el muntatge NFS negociat i mesura l'assignació al servidor. [Especificació NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Configura els indicadors del disc VM

A la interfície de Proxmox, obre **VM > Hardware > Hard Disk > Edit**. Inspecciona el bus del disc i les opcions avançades. Els indicadors següents afecten l'assignació o determinen si una optimització és útil. La [referència oficial d'opcions `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) indica la disponibilitat segons el bus.

| Bus | Opció relacionada amb l'espai |
|---|---|
| **IDE** | Compatibilitat antiga. Utilitza'l només si al guest li falta un controlador més recent. |
| **SATA** | Emulació molt compatible. Verifica trim del guest i les opcions del disc abans de confiar en la recuperació. |
| **SCSI amb VirtIO SCSI** | Ruta moderna preferida per a discard i ajustos per disc. Windows necessita el controlador VirtIO. |
| **VirtIO Block** | Disc paravirtualitzat. Discard a Linux requereix kernel 5.0 o posterior. No admet emulació SSD. |

| Ajust | Efecte | Orientació |
|---|---|---|
| **Habilita discard (`on`)** | Reenvia TRIM o UNMAP del guest | Necessari per recuperar espai des del guest en un backend thin compatible. El valor predeterminat `ignore` bloqueja el reenviament. |
| **Emulació SSD `ssd=1`** | Presenta el disc al guest com un SSD | Alguns guests necessiten aquesta identitat abans d'enviar trim. No accelera l'emmagatzematge físic. VirtIO Block no té aquest indicador. |
| **Detect zeroes `detect_zeroes=1`** | Detecta i intenta optimitzar les escriptures de zeros | Optimització d'E/S opcional. No substitueix trim ni garanteix espai recuperat. |
| **Bus: SCSI / VirtIO SCSI single** | Exposa un disc SCSI mitjançant el controlador VirtIO | Opció pràctica per a guests Windows i Linux moderns. Instal·la els controladors VirtIO de Windows. |
| **Bus: VirtIO Block** | Utilitza el dispositiu de blocs VirtIO | Discard a Linux requereix kernel 5.0 o posterior. No admet emulació SSD. |
| **Fil d'E/S `iothread=1`** | Assigna l'E/S del disc a un altre fil | Utilitza'l amb VirtIO Block o SCSI en un controlador VirtIO SCSI single. És un ajust de rendiment, no de recuperació. |
| **Memòria cau i AIO** | Canvien el buffer d'E/S i l'E/S asíncrona | Ajusta'ls segons la càrrega i el backend. Cap dels dos redueix un disc. |
| **Còpia `backup=0`** | Exclou el disc de les còpies VM | Redueix l'abast de la còpia i exclou les dades del disc de la recuperació de la VM. Documenta una altra còpia. |
| **Rèplica `replicate=0`** | Exclou el disc de la rèplica d'emmagatzematge | Redueix les dades replicades i exclou el disc de la rèplica. |

**Altres opcions d'unitat descriuen comportaments, no recuperació.** `format` s'aplica quan s'assigna un disc en un backend amb diversos formats d'imatge. `size` és la capacitat virtual, no els bytes assignats. `ro=1` marca el disc com a només lectura. `snapshot=1` activa el mode d'instantània temporal de QEMU, que descarta els canvis quan s'apaga la VM. No és l'opció per incloure un disc en les instantànies VM de Proxmox. Evita-la per a dades persistents. Comprova la cobertura de recuperació abans d'utilitzar `backup=0` o `replicate=0`. [Opcions de disc VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**No enganxis una ordre `qm set --scsi0` abreujada sobre una unitat existent.** Inspecciona **`qm config VMID`** i conserva l'ID de volum complet i les opcions existents quan l'edites. Una assignació abreujada pot eliminar altres ajustos per disc. A la interfície, verifica les opcions desades després de cada canvi.

```bash
qm config 100
pvesm status
```

`100` és un ID de VM d'exemple. Per a un disc SCSI **nou** de 64 GiB en una VM existent amb controlador **VirtIO SCSI single** i el controlador necessari al guest, aquesta ordre mostra la sintaxi d'assignació. Substitueix els ID de VM i d'emmagatzematge pels teus.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Comprova si `scsi0` ja existeix abans de fer servir l'exemple.** L'ordre canvia aquesta ranura. Per a un disc existent, utilitza la interfície si és més fàcil preservar la cadena exacta d'opcions. Consulta la [referència de l'ordre `qm` de Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Neteja els fitxers del sistema convidat

**Allibera primer fitxers del guest.** Revisa la configuració d'emmagatzematge de Windows, els fitxers temporals, els instal·ladors antics, les memòries cau d'aplicacions i la paperera. Neteja les bases de dades i els entorns de contenidors des de la seva pròpia interfície. Esborrar dades actives de l'aplicació només per reduir l'assignació posa les dades en risc.

**Confirma que el volum utilitza un disc virtual compatible amb discard** i executa una sessió de PowerShell elevada a la VM Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indica que Windows ha activat les notificacions d'esborrament per al sistema de fitxers reportat. **ReTrim** torna a enviar sol·licituds trim per a les regions del volum que ara no s'utilitzen. Si l'ordre s'executa correctament, el guest ha enviat l'operació, però això no indica quants bytes ha recuperat l'amfitrió. Comprova l'amfitrió quan acabi la tasca. [Referència de Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) i [documentació de discos VM de Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**No confonguis QEMU guest agent amb TRIM.** L'agent permet controlar el guest i ofereix funcions de coherència de còpies. Les notificacions d'esborrament del sistema de fitxers passen pel disc virtual. Instal·lar només l'agent no recupera blocs. [Documentació de Proxmox sobre guest agent VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Marca els blocs no utilitzats del sistema de fitxers

**Comprova la ruta de blocs i el sistema de fitxers abans de trim.** Una distribució moderna sovint executa periòdicament `fstrim.timer`. Inspecciona'n l'estat i després aplica trim als sistemes muntats després d'esborrar les dades innecessàries del guest.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** informa de la granularitat i els límits de discard dels dispositius de blocs visibles. **`fstrim -av`** aplica trim als sistemes muntats compatibles i informa dels intervals enviats. Els bytes enviats no equivalen als bytes retornats al grup. Els dispositius xifrats, LVM, RAID i altres capes apilades necessiten compatibilitat discard a cada capa. [Guia de Red Hat sobre blocs no utilitzats](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Utilitza trim programat o una política discard en línia deliberada. **No activis `discard` continu a tots els sistemes de fitxers com a substitut de comprovar la ruta d'emmagatzematge.** Després de trim al guest, inspecciona el volum i el grup PVE. Comprova la política de compactació pròpia d'una base de dades o servei si els registres esborrats encara ocupen els fitxers.

## Separa les regles d'emmagatzematge dels contenidors

**LXC no té un bus de disc VM emulat per al sistema de fitxers root.** Comença amb `pct config CTID` i identifica cada entrada `rootfs` i `mpN`. Proxmox defineix muntatges recolzats per emmagatzematge, bind mounts i muntatges de dispositius. Un camí visible al contenidor no indica quin volum de l'amfitrió és propietari dels blocs. [Punts de muntatge de contenidors Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Per a un **rootfs o punt de muntatge gestionat**, elimina fitxers des del contenidor o la seva aplicació i després inspecciona el volum subjacent i les instantànies a l'amfitrió. **No executis ordres `qm` de discard VM contra un CT.** Als subvolums ZFS, les instantànies retenen blocs esborrats. A l'emmagatzematge directory i LVM thin, comprova l'assignació real del backend, no la mida configurada del CT.

Executa **`pct fstrim` a l'amfitrió Proxmox** després de netejar el CT quan l'emmagatzematge subjacent admeti discard. Proxmox aplica trim al rootfs del CT i als punts de muntatge gestionats compatibles. Omet els bind mounts i els muntatges de només lectura. Utilitza `--ignore-mountpoints` per aplicar trim només al rootfs. Compara l'ús de l'emmagatzematge abans i després. [Referència de Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

Les ordres mostren **abasts alternatius** per a l'ID de CT d'exemple `101`. Executa l'abast adequat a la teva estructura d'emmagatzematge. Una execució correcta de trim no garanteix els mateixos bytes alliberats si les instantànies retenen blocs antics.

**Proxmox no gestiona els bind mounts ni els muntatges de dispositius.** Les seves dades d'origen romanen a l'amfitrió o en un dispositiu extern. Les còpies `vzdump` del contenidor n'exclouen el contingut. Els punts de muntatge addicionals recolzats per emmagatzematge també s'exclouen per defecte, tret que l'opció `backup` els inclogui. Comprova la política real de còpia abans de netejar. [Documentació de còpies de Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Per a Docker imbricat, inspecciona les capes d'imatge, els volums i els registres dins del propietari real de l'emmagatzematge abans d'utilitzar ordres de neteja de Docker. La [guia de fiabilitat de Docker en LXC](/articles/docker-in-lxc-proxmox-reliability/) cobreix els límits de muntatge i còpia. Esborrar una imatge de contenidor no elimina un volum persistent per defecte.

## Mesura correctament l'amfitrió

**Registra les mateixes mesures abans i després de netejar.** L'espai lliure del grup és l'indicador final de capacitat. Utilitza dades per volum per trobar el guest responsable del creixement.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventaria volums gestionats i mides configurades. No mesura els bytes assignats en emmagatzematge thin. Per a l'emmagatzematge **directory**, inspecciona el camí de muntatge exacte i un fitxer d'imatge conegut. Substitueix els camins pels de **Datacenter > Storage** i la configuració de la VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Per a una VM **aturada**, compara la capacitat virtual de la imatge amb l'assignació a l'amfitrió sense modificar el fitxer:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Per a **LVM thin**, vigila les dades i metadades del grup:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Per a **ZFS**, separa les dades actives del conjunt de dades de les retingudes per les instantànies:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** informa dels blocs retinguts per totes les instantànies d'un conjunt de dades. Els valors `used` de les instantànies no se sumen perquè comparteixen blocs. Un fitxer esborrat pot deixar igual l'ús del grup fins que caduqui o s'elimini, segons la política de retenció, cada instantània que faci referència als blocs. [Instantànies i clons d'OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Per a **Ceph RBD**, associa l'ID de volum de Proxmox abans d'executar ordres de Ceph. **`qm config VMID`** mostra `STORAGE_ID:IMAGE`. Obre l'entrada RBD a **Datacenter > Storage** per trobar-ne el **grup** i l'**espai de noms** opcional. L'ID d'emmagatzematge no ha de coincidir amb el nom del grup. Construeix `POOL/IMAGE` amb els valors del grup i de la imatge. Executa aquestes ordres en un client configurat per al clúster Ceph previst i amb credencials vàlides. [Documentació d'emmagatzematge RBD de Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** informa de l'ús aprovisionat i real de la imatge, incloses les instantànies associades. Sense la funció d'imatge `fast-diff`, consulta els OSD per trobar objectes possibles i requereix més feina. **`ceph df`** mostra la capacitat del grup i del clúster. La replicació, la codificació d'esborrament i les instantànies afecten l'ús brut del clúster, de manera que els bytes de la imatge i del grup difereixen. [Referència d'ordres de Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) i [guia d'ús dels grups Ceph](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Si l'emmagatzematge RBD utilitza un espai de noms, afegeix **`--namespace NAMESPACE`** a cada ordre `rbd`. Utilitza l'espai de noms configurat a l'entrada d'emmagatzematge de Proxmox, no l'ID d'emmagatzematge Proxmox.

## Tingues en compte les instantànies i les còpies

**Les instantànies conserven versions antigues dels blocs.** Si l'ús no baixa després de trim, revisa la pestanya **Snapshots** de la VM o del CT i l'inventari d'instantànies del backend. Inspecciona'n el propietari i les dependències abans d'esborrar-ne cap. Una còpia és una còpia separada i segueix la retenció de l'emmagatzematge de còpies, no el resultat actual de `df` del guest.

**La deduplicació de PBS canvia la comptabilitat.** El datastore conté blocs compartits entre còpies. Pruning elimina les metadades d'instantània de les còpies. Després, la recollida d'escombraries elimina els blocs sense referències, un cop passat el període de gràcia. Comprova totes dues tasques abans d'afirmar que s'ha recuperat capacitat de còpia. [Documentació de manteniment de PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Avís:** No esborris mai un fitxer de volum gestionat per Proxmox, un zvol o una instantània basant-te només en el nom. Identifica primer el guest i la política de retenció. Una tasca de neteja ha de preservar la còpia i el camí de reversió.

## Reconstrueix el fitxer de disc amb la màquina aturada

**Utilitza una conversió fora de línia només quan el trim habitual del guest i la ruta del backend no resolguin un problema d'assignació qcow2.** Atura la VM, verifica la còpia, identifica les relacions d'instantànies i de backing chain i escriu una imatge de destinació separada. QEMU adverteix que no s'ha de modificar una imatge que utilitza un altre procés. [Documentació de QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Prefereix un trasllat gestionat per Proxmox o un flux de còpia i restauració** quan el disc tingui instantànies o sigui en emmagatzematge de blocs gestionat. Un `qemu-img convert` independent sobre una imatge propietat de PVE no actualitza la configuració de VM, la propietat del volum ni les referències a instantànies. No utilitzis `qemu-img resize --shrink` per recuperar fitxers esborrats. Reduir la capacitat visible pel guest pot truncar dades si les particions i els sistemes de fitxers no s'han reduït abans.

## Resol un error de recuperació

| Símptoma | Comprovació probable | Acció següent |
|---|---|---|
| **Baixa `df` del guest, l'amfitrió es manté** | Indicador discard de VM, trim del guest, instantànies | Verifica tota la ruta discard i les instantànies retingudes. |
| **`fstrim` diu que no és compatible** | Bus de disc del guest, dispositius apilats, backend | Inspecciona `lsblk -D`, el kernel del guest i cada capa intermèdia. |
| **Windows ReTrim acaba, l'amfitrió es manté** | Assignació del backend, instantànies, comptabilitat del servidor | Compara el volum i el grup. Confirma que el disc utilitza emmagatzematge thin. |
| **`ls -lh` i `du -h` difereixen** | Fitxer dispers o qcow2 | Utilitza `du` per als blocs assignats del sistema de fitxers. |
| **El thin pool LVM continua alt** | Dades, metadades, instantànies | Comprova `lvs` i les instantànies PVE abans d'eliminar res. |
| **El grup ZFS continua alt** | Blocs retinguts per instantànies i reserves | Comprova `usedbysnapshots`, els ajustos del zvol i la capacitat del grup. |
| **`df` del CT i del grup no coincideixen** | Bind mounts, punts de muntatge, instantànies | Associa `rootfs` i cada `mpN` al propietari de l'amfitrió. |

**Torna a comprovar-ho quan acabin les tasques en segon pla.** La comptabilitat de l'emmagatzematge pot anar amb retard després de trim, l'eliminació d'instantànies o la recollida d'escombraries del backend. Compara l'espai lliure mesurat al grup amb el valor inicial. No dedueixis l'èxit només del codi de sortida d'una ordre del guest.

## Passos següents

**Crea un registre d'emmagatzematge per a cada guest:** mida virtual, bytes assignats, backend, bus, indicador discard, nombre d'instantànies, cobertura de còpies i espai lliure del grup. Tria una VM, activa la ruta discard compatible, executa trim al guest i compara els valors registrats. Repeteix-ho només si el resultat de la primera VM coincideix amb el comportament previst del backend.

Per planificar millor la recuperació, segueix el [simulacre de còpia i restauració de Proxmox](/articles/proxmox-vm-backup-restore-drill/) i la [guia d'actualització de Proxmox VE 8 a 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Referències

- [Administració d'emmagatzematge de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), tipus d'emmagatzematge, thin provisioning i riscos de capacitat.
- [Emmagatzematge LVM de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), cadenes de volums d'instantània VE 9 i assignació.
- [Emmagatzematge RBD de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configuració de grups i espais de noms.
- [Màquines virtuals de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), busos de disc, formats, discard i guest agent.
- [Opcions de disc VM de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), indicadors segons el bus.
- [Contenidors de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), sistemes de fitxers root i propietat dels punts de muntatge.
- [Ordres de contenidor de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim de contenidor des de l'amfitrió.
- [Còpia i restauració de Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), cobertura de còpies de VM i CT.
- [documentació de Microsoft per a `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), sintaxi de Windows ReTrim.
- [Guia de Red Hat sobre blocs no utilitzats](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportament de Linux `fstrim`.
- [Instantànies i clons d'OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocs retinguts per instantànies.
- [Referència d'ordres de Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), ús d'imatges i instantànies.
- [Especificació NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), desassignació d'espai al servidor.
- [Documentació de manteniment de PBS](https://pbs.proxmox.com/docs/maintenance.html), pruning i recollida d'escombraries.
- [Utilitat d'imatges de disc QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), seguretat de conversió fora de línia.
