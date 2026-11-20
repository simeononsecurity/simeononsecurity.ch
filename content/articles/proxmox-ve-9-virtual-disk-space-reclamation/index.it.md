---
title: "Proxmox VE 9: ridurre l'uso dei dischi virtuali e recuperare spazio"
date: 2026-11-09
lastmod: 2026-11-20
toc: true
draft: false
description: "Riduci lo spazio usato da VM e container LXC in Proxmox VE 9. Confronta formati e backend, abilita discard, esegui trim e controlla gli snapshot prima di recuperare spazio."
genre: ["Virtualizzazione", "Amministrazione Linux", "piattaforma Proxmox VE", "Archiviazione", "Laboratorio domestico"]
tags: ["spazio disco Proxmox VE 9", "allocazione dinamica Proxmox", "notifiche discard Proxmox", "comando TRIM Proxmox", "Windows ReTrim su Proxmox", "Linux fstrim su Proxmox", "uso disco LXC Proxmox", "thin provisioning LVM Proxmox", "zvol sparse ZFS Proxmox", "dispositivi a blocchi Ceph RBD Proxmox", "formato qcow2 Proxmox", "disco raw Proxmox", "snapshot Proxmox", "recupero spazio disco virtuale", "tipi di archiviazione Proxmox", "controller VirtIO SCSI", "rilevamento scritture zero Proxmox", "archiviazione backup Proxmox"]
cover: "/img/cover/proxmox-ve-9-virtual-disk-space-reclamation.webp"
coverAlt: "Due griglie di blocchi collegate da una freccia mostrano i blocchi usati di un disco virtuale e la capacità libera di un pool di archiviazione."
coverCaption: "Eliminazione nel guest, discard e recupero dello spazio sono passaggi distinti."
---

**Un filesystem guest più piccolo non riduce sempre lo spazio di archiviazione usato da Proxmox.** Per liberare spazio sull'host servono un disco compatibile con il thin provisioning, un percorso discard funzionante per le VM e uno storage backend senza blocchi trattenuti dagli snapshot. Questa guida descrive impostazioni e controlli per VM e container LXC in Proxmox VE 9.

<!--more-->

## Punti chiave

- **Scegli prima lo storage backend.** La dimensione dichiarata di un disco virtuale differisce dallo spazio allocato sull'host solo se il formato o il backend supporta il thin provisioning.
- **Abilita discard sulla VM, poi esegui trim nel guest.** Windows ReTrim e Linux `fstrim` inviano richieste per i blocchi inutilizzati attraverso il disco virtuale.
- **Controlla separatamente snapshot e backup.** I blocchi vecchi restano allocati finché uno snapshot li referenzia. I file di backup e i chunk PBS seguono regole di conservazione proprie.
- **Classifica i mount LXC in base al tipo.** Volumi rootfs e mount point gestiti, bind mount e mount di dispositivi hanno proprietà e comportamento di backup diversi.

## Prima di iniziare

Servono **accesso amministrativo a Proxmox VE 9**, un backup verificato per ogni guest interessato e spazio libero sufficiente nel pool per l'operazione. Prima di modificare impostazioni, annota ID del guest, bus del disco, ID del volume, ID dello storage, snapshot e allocazione corrente. Usa il [test di ripristino di una VM](/articles/proxmox-vm-backup-restore-drill/) per verificare il recupero.

**Tempo stimato:** da 20 a 60 minuti per guest, oltre alle operazioni di trim o pulizia più lunghe. **Difficoltà:** Intermedia. Inizia con una VM a basso rischio e confronta l'uso dello storage prima e dopo.

> **Avviso:** Un thin pool pieno provoca errori di I/O nei guest e rischia di danneggiare i filesystem. Non sovra-allocare la capacità senza monitorare lo spazio libero per dati e metadati del pool. [Documentazione storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Segui la catena di allocazione

**Eliminazione**, **discard** e **recupero** avvengono a livelli diversi. Il guest elimina un file e marca come liberi i blocchi del filesystem. Il filesystem invia TRIM o UNMAP per quei blocchi. QEMU inoltra la richiesta se discard è abilitato sul disco virtuale. Il backend libera l'allocazione fisica se formato e pool supportano l'operazione. [Documentazione dischi VM di Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Livello | Controllo | Evidenza utile |
|---|---|---|
| **File del guest** | Spazio libero del filesystem | Proprietà del volume Windows o `df -h` su Linux |
| **Disco virtuale** | Bus, discard, emulazione SSD, formato immagine | Scheda **Hardware** della VM o `qm config VMID` |
| **Volume PVE** | Proprietario e dimensione configurata | Scheda **Content** dello storage o `pvesm list STORAGE_ID` |
| **Pool di archiviazione** | Dati e metadati liberi, blocchi trattenuti | `pvesm status` e strumenti specifici del backend |

**Un disco virtuale da 100 GiB definisce un limite di capacità, non garantisce 100 GiB allocati.** Al contrario, se il guest segnala 20 GiB usati, non significa che l'host ne usi 20. Metadati, snapshot, copie di backup e blocchi già scritti modificano il valore. [Documentazione storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

## Confronta i formati dei dischi

**Il backend di archiviazione determina i formati immagine offerti da Proxmox.** Gli zvol ZFS e Ceph RBD usano dischi virtuali raw. LVM usa normalmente raw, con l'eccezione di Proxmox VE 9 per le catene di volumi descritta sotto. Gli storage basati su file, come directory e NFS, supportano raw o qcow2. Raw da solo non offre allocazione thin né snapshot. Queste funzioni dipendono dallo storage sottostante. Qcow2 offre allocazione copy-on-write e snapshot a livello di immagine. [Documentazione dischi VM di Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

| Formato | Meccanismo di allocazione | Compromesso di spazio |
|---|---|---|
| **qcow2 su storage file** | Qcow2 alloca i cluster quando vengono scritti | Metadati immagine e catene di snapshot consumano spazio |
| **file raw su storage file** | File sparso del filesystem, se supportato | Raw da solo non offre thin provisioning né snapshot |
| **volume a blocchi raw** | LVM thin, ZFS, Ceph RBD o altro storage | Allocazione del pool e snapshot dipendono dal backend |

**Proxmox VE 9 thick LVM offre una modalità speciale per gli snapshot.** `snapshot-as-volume-chain` usa relazioni qcow2 di backing tra volumi logici thick LVM. Non usa snapshot interni qcow2. L'opzione riguarda solo i nuovi dischi VM e nella documentazione Proxmox attuale è un'anteprima tecnologica. PVE visualizza ogni snapshot come completamente allocato. L'allocazione SAN effettiva è inferiore solo se lo storage sottostante supporta thin provisioning e discard. [Documentazione LVM storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc)

**Non convertire un disco solo perché termina con `.raw`.** Controlla prima il plugin di storage e i blocchi allocati. Un disco raw su `local-lvm` si comporta diversamente da un file raw completamente allocato su uno storage directory normale.

## Tipi di archiviazione a confronto

Proxmox distingue **storage file** e **storage a blocchi**. Il plugin controlla anche snapshot, cloni, condivisione e tipi di contenuto accettati da ciascun pool. Controlla la voce **Datacenter > Storage** prima di fare affidamento su un formato o una funzione. [Tabella dei tipi di storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

| Storage | Comportamento disco VM | Controllo del recupero |
|---|---|---|
| **Directory, ext4, XFS** | File raw o qcow2 | Confronta i byte allocati di `du` con la dimensione virtuale dell'immagine. Controlla gli snapshot se li offre un altro livello di storage. |
| **NFS, CIFS** | File raw o qcow2 su storage condiviso | Controlla lo spazio allocato sul server. Il risultato di trim nel guest non dimostra che il server abbia liberato spazio. |
| **LVM con allocazione fine (`local-lvm`)** | Volumi logici raw thin, solo locali | Controlla con `lvs` le percentuali di dati e metadati del thin pool. |
| **LVM thick** | LV raw o catene di volumi qcow2 VE 9 | L'eliminazione nel guest non riduce la prenotazione fissa del LV. Controlla a parte l'allocazione thin SAN. |
| **Archiviazione ZFS (`local-zfs`)** | zvol raw o subvolume di container | Controlla `sparse`, proprietà del dataset, uso del pool e snapshot. |
| **Ceph RBD** | Immagini RBD raw thin su storage condiviso | Controlla capacità del pool Ceph, uso immagine, snapshot e discard. |
| **Btrfs** | Volumi basati su file con subvolume Btrfs per immagini raw | Considera il plugin Btrfs di PVE un'anteprima tecnologica e verifica snapshot e uso del filesystem. |

**Altri plugin di storage hanno ruoli diversi.** CephFS fornisce storage file condiviso. iSCSI e Fibre Channel espongono dispositivi a blocchi condivisi, spesso suddivisi in volumi VM con LVM. ZFS over iSCSI usa storage remoto a blocchi basato su ZFS. Proxmox Backup Server (PBS) conserva backup, non dischi VM attivi. Controlla i tipi di **Content** abilitati prima di archiviare lì dati `images`, `rootdir`, `backup` o `iso`. [Tabella dei tipi di storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**I flag di allocazione dello storage file contano quando si crea il disco.** Il valore `format` dello storage sceglie `raw`, `qcow2` o `vmdk` quando supportati. `preallocation` per file raw e qcow2 accetta `off`, `metadata`, `falloc` o `full`. Il valore predefinito è `metadata`, trattato come `off` per raw. `full` riserva subito lo spazio del file e annulla la consueta impronta iniziale ridotta. Controlla la configurazione prima di creare un disco grande. Il flag `shared` dichiara solo un accesso condiviso già esistente. Non rende condiviso uno storage locale. [Proprietà comuni storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc)

**ZFS `sparse` è l'impostazione di storage per creare zvol thin.** Senza zvol sparse, la creazione riserva capacità in base al comportamento configurato del volume. Verifica la configurazione effettiva dello storage e del pool prima di cambiare un'installazione esistente. [Documentazione ZFS storage Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-zfspool.adoc)

**Lo storage directory richiede un secondo controllo.** La lunghezza logica di un file qcow2 non è la capacità virtuale visibile al guest. `du -h` segnala i blocchi del filesystem allocati all'immagine. `ls -lh` mostra la lunghezza logica del file. Per una VM arrestata, `qemu-img info` riporta capacità virtuale e dimensione su host. Su NFS, usa il conteggio del server per le decisioni finali sulla capacità. [Riferimento QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**NFS ha un altro confine di allocazione.** Il riutilizzo da parte di qcow2 di un cluster vuoto nel file non significa che il server NFS liberi i blocchi del file. Il rilascio dei buchi richiede supporto da client, protocollo negoziato, server e filesystem del server. NFSv4.2 definisce `DEALLOCATE`, ma il numero di versione da solo non prova che il server abbia restituito spazio. Controlla il mount NFS negoziato e misura l'allocazione sul server. [Specifiche NFSv4.2 `DEALLOCATE`](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2)

## Imposta i flag del disco VM

Nell'interfaccia Proxmox, apri **VM > Hardware > Hard Disk > Edit**. Controlla il bus del disco e le opzioni avanzate. I flag seguenti influiscono sull'allocazione o determinano se un'ottimizzazione è utile. Il [riferimento ufficiale alle opzioni `qm`](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc) elenca la disponibilità per bus.

| Bus | Scelta legata allo spazio |
|---|---|
| **IDE** | Compatibilità legacy. Usalo solo se il guest non ha un driver più recente. |
| **SATA** | Emulazione ampiamente supportata. Verifica trim del guest e opzioni disco prima di fare affidamento sul recupero. |
| **SCSI con VirtIO SCSI** | Percorso moderno consigliato per discard e impostazioni per disco. Windows richiede il driver VirtIO. |
| **VirtIO Block** | Disco paravirtualizzato. Discard Linux richiede kernel 5.0 o successivo. Non supporta emulazione SSD. |

| Impostazione | Effetto | Indicazioni |
|---|---|---|
| **Inoltra discard (`on`)** | Inoltra TRIM o UNMAP del guest | Necessario per recuperare spazio dal guest su un backend thin compatibile. Il valore predefinito `ignore` blocca l'inoltro. |
| **Emulazione SSD `ssd=1`** | Presenta il disco al guest come SSD | Alcuni guest richiedono questa identità prima di inviare trim. Non rende più veloce lo storage fisico. VirtIO Block non offre questo flag. |
| **Detect zeroes `detect_zeroes=1`** | Rileva e prova a ottimizzare le scritture di zeri | Ottimizzazione I/O facoltativa. Non sostituisce trim del guest e non garantisce spazio recuperato. |
| **Bus: SCSI / VirtIO SCSI single** | Espone un disco SCSI tramite il controller VirtIO | Scelta pratica per guest Windows e Linux moderni. Installa i driver VirtIO di Windows. |
| **Bus: VirtIO Block** | Usa il dispositivo a blocchi VirtIO | Discard Linux richiede kernel 5.0 o successivo. Non supporta emulazione SSD. |
| **Thread I/O `iothread=1`** | Assegna l'I/O del disco a un thread separato | Usalo con VirtIO Block o SCSI su un controller VirtIO SCSI single. È un'impostazione prestazionale, non di recupero. |
| **Cache e AIO** | Cambiano buffering I/O e I/O asincrono | Configurali in base al carico e al backend. Nessuna delle due impostazioni riduce un disco. |
| **Backup `backup=0`** | Esclude il disco dai backup VM | Riduce l'ambito del backup e rimuove i dati dal ripristino della VM. Documenta un backup separato. |
| **Replica `replicate=0`** | Esclude il disco dalla replica storage | Riduce i dati replicati ed esclude il disco dalla replica. |

**Altre opzioni dell'unità descrivono il comportamento, non il recupero.** `format` vale quando si crea un disco su un backend con più formati. `size` è la capacità virtuale, non i byte allocati. `ro=1` rende il disco di sola lettura. `snapshot=1` abilita la modalità snapshot temporanea di QEMU, che scarta le modifiche allo spegnimento della VM. Non è l'opzione per includere un disco negli snapshot VM di Proxmox. Evitala per i dati persistenti. Controlla la copertura del ripristino prima di usare `backup=0` o `replicate=0`. [Opzioni dischi VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc)

**Non incollare una stringa abbreviata `qm set --scsi0` sopra un'unità esistente.** Controlla **`qm config VMID`** e conserva ID volume completo e opzioni esistenti quando modifichi il disco. Un'assegnazione abbreviata rischia di eliminare altre impostazioni. Nell'interfaccia, verifica le opzioni salvate dopo ogni modifica.

```bash
qm config 100
pvesm status
```

`100` è un ID VM di esempio. Per un disco SCSI **nuovo** da 64 GiB su una VM esistente con controller **VirtIO SCSI single** e driver richiesto nel guest, questo comando mostra la sintassi di allocazione. Sostituisci ID VM e storage con i tuoi valori.

```bash
qm set 100 --scsi0 local-lvm:64,discard=on,ssd=1,iothread=1
```

**Controlla se `scsi0` esiste già prima di usare l'esempio.** Il comando modifica quello slot. Per un disco esistente, usa l'interfaccia se permette di conservare più facilmente la stringa precisa delle opzioni. Consulta il [riferimento ai comandi `qm` di Proxmox](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc).

## Pulisci i file del sistema guest

**Libera prima i file del guest.** Controlla le impostazioni Archiviazione di Windows, file temporanei, vecchi programmi di installazione, cache delle applicazioni e cestino. Esegui la pulizia di database e runtime dei container dalla loro interfaccia. Eliminare dati attivi di un'applicazione solo per ridurre l'allocazione rischia di perderli.

**Verifica che il volume usi un disco virtuale compatibile con discard**, poi avvia una sessione PowerShell elevata nella VM Windows:

```powershell
fsutil behavior query DisableDeleteNotify
Optimize-Volume -DriveLetter C -ReTrim -Verbose
```

`DisableDeleteNotify = 0` indica che Windows ha abilitato le notifiche di eliminazione per il filesystem segnalato. **ReTrim** invia di nuovo richieste trim per le aree del volume attualmente inutilizzate. Il completamento corretto conferma che il guest ha inviato l'operazione, non il numero di byte recuperati dall'host. Controlla l'host al termine. [Riferimento Microsoft `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps) e [documentazione dischi VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

**Non confondere QEMU guest agent con TRIM.** L'agent supporta il controllo del guest e le funzioni di coerenza dei backup. Le notifiche di eliminazione del filesystem passano attraverso il disco virtuale. Installare solo l'agent non recupera blocchi. [Documentazione Proxmox del guest agent VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc)

## Segnala i blocchi inutilizzati del file system

**Controlla percorso a blocchi e filesystem prima di trim.** Una distribuzione moderna spesso esegue periodicamente `fstrim.timer`. Verificane lo stato, poi esegui trim sui filesystem montati dopo aver eliminato i dati guest non necessari.

```bash
lsblk -D
systemctl status fstrim.timer
sudo fstrim -av
```

**`lsblk -D`** mostra granularità e limiti discard dei dispositivi a blocchi visibili. **`fstrim -av`** esegue trim sui filesystem montati compatibili e segnala gli intervalli inviati. I byte inviati non equivalgono ai byte restituiti al pool. Dispositivi cifrati, LVM, RAID e altri livelli impilati richiedono supporto discard su ogni livello. [Guida Red Hat sui blocchi inutilizzati](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems)

Usa trim pianificato o una politica online discard deliberata. **Non abilitare `discard` continuo su tutti i filesystem al posto di controllare il percorso di storage.** Dopo il trim nel guest, ispeziona volume e pool PVE. Se i record eliminati occupano ancora i file, controlla la politica di compattazione propria del database o servizio.

## Verifica separatamente lo spazio dei container

**LXC non ha un bus disco VM emulato per il filesystem root.** Inizia con `pct config CTID` e individua ogni voce `rootfs` e `mpN`. Proxmox distingue mount supportati da storage, bind mount e mount di dispositivi. Un percorso visibile nel container non rivela quale volume host possiede i blocchi. [Mount point dei container Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

```bash
pct config 101
pct exec 101 -- df -h
pvesm status
```

Per un **rootfs o mount point gestito**, elimina i file dal container o dalla sua applicazione, poi controlla il volume backend e gli snapshot sull'host. **Non eseguire comandi discard `qm` per VM su un CT.** Sugli subvolume ZFS gli snapshot trattengono blocchi eliminati. Su directory e LVM thin, controlla l'allocazione effettiva del backend anziché la dimensione configurata del CT.

Esegui **`pct fstrim` sull'host Proxmox** dopo la pulizia del CT se lo storage backend supporta discard. Proxmox esegue trim sul rootfs del CT e sui mount point gestiti idonei. Salta bind mount e mount point in sola lettura. Usa `--ignore-mountpoints` per eseguire trim solo sul rootfs. Confronta l'uso dello storage prima e dopo. [Riferimento Proxmox `pct fstrim`](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc)

```bash
pct fstrim 101
pct fstrim 101 --ignore-mountpoints 1
```

I comandi mostrano **ambiti alternativi** per il CT di esempio con ID `101`. Scegli l'ambito adatto al layout dello storage. Un trim riuscito non garantisce lo stesso numero di byte liberati se gli snapshot trattengono blocchi vecchi.

**Proxmox non gestisce bind mount e mount di dispositivi.** I loro dati sorgente restano sull'host o su un dispositivo esterno. I backup `vzdump` del container escludono quei contenuti. Anche i mount point aggiuntivi basati su storage sono esclusi per impostazione predefinita, a meno che l'opzione `backup` li includa. Controlla la politica di backup effettiva prima della pulizia. [Documentazione backup Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

Per Docker annidato, controlla layer delle immagini, volumi e log nel proprietario effettivo dello storage prima di usare comandi di pulizia Docker. La [guida all'affidabilità di Docker in LXC](/articles/docker-in-lxc-proxmox-reliability/) descrive i confini di mount e backup. Eliminare un'immagine container non elimina per impostazione predefinita un volume persistente.

## Misura correttamente il server

**Registra le stesse misure prima e dopo la pulizia.** Lo spazio libero del pool è il segnale finale di capacità. Usa i dati a livello di volume per individuare il guest che ha causato la crescita.

```bash
pvesm status
pvesm list local-lvm
qm config 100
pct config 101
```

**`pvesm list`** inventaria i volumi gestiti e le dimensioni configurate. Non misura i byte allocati sullo storage thin. Per lo storage **directory**, controlla il percorso montato esatto e un file immagine noto. Sostituisci i percorsi con quelli indicati da **Datacenter > Storage** e dalla configurazione VM.

```bash
df -hT /var/lib/vz
du -h /var/lib/vz/images/100/vm-100-disk-0.qcow2
ls -lh /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Per una VM **arrestata**, confronta capacità virtuale e allocazione host dell'immagine senza modificare il file:

```bash
qemu-img info /var/lib/vz/images/100/vm-100-disk-0.qcow2
```

Per **LVM thin**, controlla dati e metadati del pool:

```bash
lvs -a -o lv_name,vg_name,lv_size,data_percent,metadata_percent,segtype
```

Per **ZFS**, distingui i dati attivi del dataset da quelli trattenuti dagli snapshot:

```bash
zpool list
zfs list -o name,used,available,referenced,usedbysnapshots -r POOL_OR_DATASET
zfs list -t snapshot -o name,used,referenced,written -r DATASET
```

**`usedbysnapshots`** mostra i blocchi trattenuti da tutti gli snapshot di un dataset. I valori `used` degli snapshot non sono cumulabili perché condividono i blocchi. Un file eliminato può lasciare invariato l'uso del pool finché tutti gli snapshot che referenziano i suoi blocchi non scadono o vengono eliminati in base alla politica di conservazione. [Snapshot e cloni OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html)

Per **Ceph RBD**, mappa l'ID volume Proxmox prima di eseguire comandi Ceph. **`qm config VMID`** mostra `STORAGE_ID:IMAGE`. Apri la voce RBD in **Datacenter > Storage** per trovare il **pool** e l'eventuale **namespace**. L'ID storage potrebbe non corrispondere al nome del pool. Crea `POOL/IMAGE` usando i valori del pool e dell'immagine. Esegui questi comandi su un client configurato per il cluster Ceph previsto con credenziali valide. [Documentazione storage RBD Proxmox](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc)

```bash
ceph df
rbd du POOL/IMAGE
rbd snap ls POOL/IMAGE
```

**`rbd du`** mostra uso provisioned ed effettivo dell'immagine, inclusi gli snapshot associati. Senza la funzione immagine `fast-diff`, interroga gli OSD per gli oggetti potenziali e richiede più lavoro. **`ceph df`** mostra capacità del pool e del cluster. Replica, erasure coding e snapshot incidono sull'uso grezzo del cluster, quindi i byte immagine e pool differiscono. [Riferimento comandi Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/) e [guida all'uso dei pool Ceph](https://docs.ceph.com/en/squid/rados/operations/monitoring/)

Se lo storage RBD usa un namespace, aggiungi **`--namespace NAMESPACE`** a ogni comando `rbd`. Usa il namespace configurato nella voce storage di Proxmox, non l'ID storage Proxmox.

## Considera snapshot e backup

**Gli snapshot conservano versioni precedenti dei blocchi.** Se l'uso non cala dopo trim, controlla la scheda **Snapshots** della VM o CT e l'inventario snapshot del backend. Verifica proprietario e dipendenze prima di eliminarne uno. Un backup è una copia separata e segue la conservazione dello storage di backup, non il risultato corrente di `df` nel guest.

**La deduplicazione PBS cambia il conteggio.** Il datastore conserva chunk condivisi tra i backup. Il pruning rimuove i metadati degli snapshot di backup. In seguito il garbage collection elimina i chunk non referenziati, rispettato un periodo di grazia. Controlla entrambi i task prima di dichiarare recuperata capacità di backup. [Documentazione manutenzione PBS](https://pbs.proxmox.com/docs/maintenance.html)

> **Avviso:** Non eliminare mai file di volume gestiti da Proxmox, zvol o snapshot basandoti solo sul nome. Identifica prima guest e politica di conservazione. La pulizia deve preservare il backup e il percorso di rollback.

## Ricrea il file disco a VM spenta

**Usa una conversione offline solo se trim normale del guest e percorso backend non risolvono un problema di allocazione qcow2.** Arresta la VM, verifica il backup, identifica relazioni tra snapshot e backing chain e scrivi in un'immagine di destinazione separata. QEMU sconsiglia di modificare un'immagine usata da un altro processo. [Documentazione QEMU `qemu-img`](https://www.qemu.org/docs/master/tools/qemu-img.html)

**Preferisci uno spostamento gestito da Proxmox o il flusso backup e ripristino** quando il disco ha snapshot o si trova su storage a blocchi gestito. Un `qemu-img convert` autonomo su un'immagine di proprietà PVE non aggiorna da solo configurazione VM, proprietà del volume o riferimenti snapshot. Non usare `qemu-img resize --shrink` per recuperare file eliminati. Ridurre la capacità visibile dal guest rischia di troncare dati se prima non riduci partizioni e filesystem.

## Risolvi un recupero non riuscito

| Sintomo | Controllo probabile | Azione successiva |
|---|---|---|
| **`df` guest scende, host invariato** | Flag discard VM, trim guest, snapshot | Verifica tutto il percorso discard e gli snapshot trattenuti. |
| **`fstrim` indica non supportato** | Bus disco guest, dispositivi impilati, backend | Controlla `lsblk -D`, kernel guest e ogni livello intermedio. |
| **Windows ReTrim termina, host invariato** | Allocazione backend, snapshot, conteggio server | Confronta volume e pool. Verifica che il disco usi storage thin. |
| **`ls -lh` e `du -h` differiscono** | File sparse o qcow2 | Usa `du` per i blocchi filesystem allocati. |
| **Thin pool LVM resta pieno** | Dati, metadati, snapshot | Controlla `lvs` e snapshot PVE prima di rimuovere qualcosa. |
| **Pool ZFS resta pieno** | Blocchi trattenuti dagli snapshot e riserve | Controlla `usedbysnapshots`, impostazioni zvol e capacità pool. |
| **`df` CT e pool non coincidono** | Bind mount, mount point, snapshot | Associa `rootfs` e ogni `mpN` al proprietario host. |

**Ricontrolla quando terminano le attività in background.** Il conteggio dello storage può aggiornarsi in ritardo dopo trim, eliminazione di snapshot o garbage collection del backend. Confronta lo spazio libero misurato nel pool con il valore iniziale. Non dedurre il successo dal solo codice di uscita di un comando guest.

## Passi successivi

**Crea un registro storage per ogni guest:** dimensione virtuale, byte allocati, backend, bus, flag discard, numero di snapshot, copertura dei backup e spazio libero del pool. Scegli una VM, abilita il percorso discard supportato, esegui trim nel guest e confronta i valori registrati. Ripeti solo se il primo risultato corrisponde al comportamento atteso del backend.

Per pianificare il recupero, segui il [test di backup e ripristino Proxmox](/articles/proxmox-vm-backup-restore-drill/) e la [guida all'aggiornamento da Proxmox VE 8 a 9](/articles/proxmox-ve-8-to-9-upgrade-guide/).

## Fonti

- [Amministrazione storage Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), tipi di storage, thin provisioning e rischi di capacità.
- [Storage LVM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), catene di volumi snapshot VE 9 e allocazione.
- [Storage RBD Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pve-storage-rbd.adoc), configurazione pool e namespace.
- [Macchine virtuali Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/qm.adoc), bus disco, formati, discard e guest agent.
- [Opzioni disco VM Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/qm.conf.5-opts.adoc), flag specifici per bus.
- [Container Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), filesystem root e proprietà dei mount point.
- [Comandi container Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/generated/pct.1-synopsis.adoc), trim container dall'host.
- [Backup e ripristino Proxmox VE](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc), copertura backup VM e CT.
- [documentazione Microsoft per `Optimize-Volume`](https://learn.microsoft.com/en-us/powershell/module/storage/optimize-volume?view=windowsserver2025-ps), sintassi ReTrim Windows.
- [Guida Red Hat sui blocchi inutilizzati](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/discarding-unused-blocks_managing-file-systems), comportamento Linux `fstrim`.
- [Snapshot e cloni OpenZFS](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/Datasets/Snapshots%20and%20Clones.html), blocchi trattenuti dagli snapshot.
- [Riferimento comandi Ceph RBD](https://docs.ceph.com/en/squid/man/8/rbd/), uso immagini e snapshot.
- [Specifiche NFSv4.2](https://www.rfc-editor.org/rfc/rfc7862.html#section-6.2.2), deallocazione dello spazio lato server.
- [Documentazione manutenzione PBS](https://pbs.proxmox.com/docs/maintenance.html), pruning e garbage collection.
- [Utility immagini disco QEMU](https://www.qemu.org/docs/master/tools/qemu-img.html), sicurezza della conversione offline.
