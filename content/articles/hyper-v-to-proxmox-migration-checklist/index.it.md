---
title: "Migrare una VM Hyper-V a Proxmox VE: checklist reversibile"
date: 2026-10-11
lastmod: 2026-11-19
toc: true
draft: false
description: "Sposta una macchina virtuale Hyper-V su Proxmox VE con un'esportazione a sorgente spenta, firmware corrispondente, importazione dei dischi, avvio di prova isolato e piano di rollback."
genre: ["Virtualizzazione", "Amministrazione di sistema", "Laboratorio domestico"]
tags: ["Migrazione da Hyper-V a Proxmox", "Migrazione Hyper-V", "Migrazione Proxmox VE", "Importazione VHDX", "qm disk import", "Passaggio di VM", "Esportazione Hyper-V", "VM Windows su Proxmox", "VirtIO su Proxmox", "Ripristino VM", "Migrazione UEFI", "Checkpoint Hyper-V", "TPM virtuale", "Ripristino BitLocker", "Migrazione del laboratorio domestico"]
cover: "/img/cover/hyper-v-to-proxmox-migration-checklist.webp"
coverAlt: "Un disco attraversa un ponte tra un rack server blu e uno arancione. Un percorso di ritorno separato e uno scudo indicano la destinazione."
coverCaption: "Mantieni disponibile la VM sorgente finché il nuovo guest non supera i controlli di cutover."
---

Un'**esportazione Hyper-V** conserva i file di una macchina virtuale, mentre Proxmox VE richiede una nuova configurazione del guest e file di disco virtuale VHDX importati. Una copia riuscita non dimostra che il guest si avvierà o fornirà il servizio. Questa checklist guida una VM attraverso un'esportazione con la sorgente spenta, un avvio di prova controllato e un cutover con una chiara procedura di ritorno.

<!--more-->

## Punti chiave

- **Registra la sorgente:** annota generazione del firmware, percorsi dei dischi, checkpoint, rete e crittografia prima dell'esportazione.
- **Ferma le scritture:** spegni la VM Hyper-V prima dell'esportazione finale e mantienila spenta durante la prova su Proxmox.
- **Allinea il percorso di avvio:** Hyper-V Generation 1 usa il BIOS legacy. Generation 2 usa UEFI.
- **Convalida il servizio:** controlla dati, accesso di rete, backup e stato del guest prima di ritirare la sorgente.

## Prima di iniziare

Pianifica una finestra di manutenzione e prova prima la procedura su una VM eliminabile. Servono accesso amministrativo a Hyper-V e Proxmox VE, spazio per l'esportazione e un backup verificato separato dalla copia di migrazione. Prevedi tempo per trasferire ogni disco virtuale e provare l'applicazione del guest. Dimensione dei dischi e velocità di trasferimento determinano il tempo di inattività.

La procedura copre una VM convenzionale con dischi virtuali. **VM schermate, dischi pass-through, dischi condivisi, workload in cluster e licenze vincolate all'hardware** richiedono piani specifici. Registra chi decide il cutover e l'ora limite per il rollback. Non avviare entrambe le copie sulla rete di produzione con la stessa identità macchina.

| Dettaglio sorgente | Perché serve |
|---|---|
| **Generazione e firmware VM** | Scegliere SeaBIOS o OVMF in Proxmox |
| **Stato e modello Secure Boot** | Allineare la policy di avvio e registrare chiavi compatibili |
| **Dischi di avvio e dati** | Importare ogni file VHDX necessario nell'ordine corretto |
| **Checkpoint e file AVHDX** | Non trattare un disco differenziale come disco base indipendente |
| **IP, DNS, MAC e VLAN** | Ripristinare la raggiungibilità senza duplicare un'identità |
| **vTPM e BitLocker** | Preparare il ripristino prima di modificare l'hardware virtuale |
| **Servizi e controlli dei dati** | Definire le prove di riuscita e rollback |

Generation 1 usa il BIOS legacy. Generation 2 usa l'Unified Extensible Firmware Interface (UEFI). Un **file AVHDX** è un disco differenziale Hyper-V collegato a un VHDX base. Un **vTPM** è un Trusted Platform Module virtuale usato da BitLocker e da altre funzioni di sicurezza. Una **VLAN** è una rete logica separata che usa hardware di rete condiviso.

**SeaBIOS** fornisce firmware BIOS legacy. **OVMF** fornisce firmware UEFI. **VirtIO** è un'interfaccia veloce per dispositivi virtuali che richiede driver nel guest. Un **initramfs** è il filesystem di avvio iniziale di Linux che carica i driver prima del sistema principale.

## Raccogliere i dati della macchina virtuale in Hyper-V

Esegui questi comandi di sola lettura in una sessione PowerShell elevata sull'host Hyper-V. Sono esempi non testati. Verifica ogni comando con il modulo Hyper-V installato e con la tua procedura di modifica. Inserisci il nome della VM quando richiesto:

```powershell
$vmName = Read-Host "Nome VM Hyper-V"
Get-VM -Name $vmName | Select-Object Name, State, Generation, ProcessorCount, MemoryAssigned
Get-VMHardDiskDrive -VMName $vmName | Select-Object ControllerType, ControllerNumber, ControllerLocation, Path
Get-VMSnapshot -VMName $vmName | Select-Object Name, CreationTime
Get-VMNetworkAdapter -VMName $vmName | Select-Object Name, SwitchName, MacAddress
```

Il [modulo PowerShell Hyper-V](https://learn.microsoft.com/en-us/powershell/module/hyper-v/) documenta questi comandi di inventario. Confronta i percorsi dei dischi con le impostazioni della VM. Registra ISO, dischi dati, switch virtuali, indirizzi statici e prenotazioni DHCP collegati. Annota sistema operativo guest e versioni delle applicazioni. Verifica il backup ripristinando una copia di prova o controllando un recente risultato documentato del ripristino. Una copia di file senza prova di ripristino offre evidenze più deboli.

Per una VM **Generation 2**, registra anche firmware e impostazioni di sicurezza:

```powershell
Get-VMFirmware -VMName $vmName | Format-List *
Get-VMSecurity -VMName $vmName | Format-List *
```

Registra stato di **Secure Boot**, modello e impostazione vTPM. La documentazione Microsoft di [**`Get-VMFirmware`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmfirmware) limita il comando a Generation 2. [**`Get-VMSecurity`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/get-vmsecurity) mostra la configurazione di sicurezza della VM. Non eseguire **`Get-VMFirmware`** su un guest Generation 1. Un **indirizzo MAC** identifica un'interfaccia di rete. **DNS** associa nomi a indirizzi. **DHCP** assegna impostazioni di rete. Un **disco EFI** memorizza le impostazioni UEFI.

**Risolvi i checkpoint prima dell'esportazione finale.** Microsoft afferma che un'esportazione Hyper-V raccoglie anche i file dei checkpoint e i dischi VHDX. Eliminare un checkpoint da Hyper-V unisce il suo disco differenziale. Non eliminare mai un file **`.avhdx`** dal filesystem per rimuovere un checkpoint. Se l'unione fallisce o la catena dei dischi sembra incompleta, fermati e segui le [istruzioni Microsoft per il ripristino dei checkpoint](https://learn.microsoft.com/en-us/troubleshoot/windows-server/virtualization/hyper-v-snapshots-checkpoints-differencing-disks). La [guida Microsoft ai checkpoint](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/checkpoints) spiega eliminazione e unione normali.

Per un guest Windows con **BitLocker** o **vTPM**, ottieni e verifica la chiave di ripristino prima di cambiare l'hardware virtuale. La [documentazione di sicurezza Hyper-V Generation 2](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/generation-2-virtual-machine-security-features) descrive la crittografia basata su vTPM. Le [FAQ BitLocker Microsoft](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-key-management-faq) spiegano perché i cambiamenti di avvio attivano il ripristino. Un nuovo dispositivo TPM Proxmox non replica il vecchio stato TPM. Conserva la chiave fuori dalla VM esportata.

## Esportare una VM spenta

Arresta il guest in modo ordinato. Verifica che Hyper-V mostri **Off** (spenta), non Saved (salvata). Attendi il completamento di qualsiasi unione di checkpoint, quindi esporta la VM in una posizione con spazio libero sufficiente. In Hyper-V Manager fai clic destro sulla VM, scegli **Export** (esporta) e seleziona la destinazione. L'equivalente PowerShell è:

```powershell
$vmName = Read-Host "Nome della VM Hyper-V spenta"
$exportPath = Read-Host "Directory di destinazione dell'esportazione"
$vm = Get-VM -Name $vmName -ErrorAction Stop
if ($vm.State -ne 'Off') { throw "Spegni la VM e attendi che Hyper-V mostri Off (spenta) prima di esportare." }
Export-VM -Name $vmName -Path $exportPath
```

La [guida Microsoft all'esportazione](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/export-and-import-virtual-machines) indica che un'esportazione contiene dischi virtuali, configurazione e file dei checkpoint. Il riferimento [**`Export-VM`**](https://learn.microsoft.com/en-us/powershell/module/hyper-v/export-vm) definisce il comando. Verifica i file di disco previsti e le relative dimensioni nella destinazione. Mantieni spenta la VM sorgente e conserva il backup indipendente. **Non modificare i file esportati durante l'importazione.**

Trasferisci i file VHDX in un percorso accessibile dall'host Proxmox. Considera l'esportazione come dati sensibili del guest. Usa un trasporto cifrato, limita l'accesso alla posizione di trasferimento e allo storage di destinazione, quindi rimuovi le copie temporanee dopo la convalida. Controlla la capacità disponibile in entrambe le posizioni. Conserva un'esportazione intatta per il rollback. Se l'esportazione contiene file **`.avhdx`**, non scegliere un **`.vhdx`** base dal nome pensando che contenga le scritture più recenti. Risolvi la catena dei dischi in Hyper-V prima di proseguire.

## Preparare la macchina virtuale di destinazione in Proxmox

Crea una nuova VM nell'interfaccia Web Proxmox con tipo di sistema operativo guest, CPU e memoria registrati in precedenza. Scegli un nuovo ID VM inutilizzato. Non installare un nuovo sistema operativo. Rimuovi il disco vuoto creato dalla procedura guidata prima di importare il disco sorgente. Lascia l'adattatore di rete scollegato dal bridge di produzione per il primo avvio oppure collegalo a una rete di prova isolata.

| Sorgente Hyper-V | Destinazione Proxmox |
|---|---|
| **Generation 1, BIOS legacy** | SeaBIOS |
| **Generation 2, UEFI** | OVMF con disco EFI e policy Secure Boot corrispondente |
| **Disco di avvio Windows senza driver storage VirtIO** | Collegalo inizialmente come SATA |
| **Windows con vTPM o BitLocker** | Nuovo dispositivo di stato TPM quando serve, chiave di ripristino pronta prima del primo avvio |

La [guida Microsoft alle generazioni delle VM](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/Should-I-create-a-generation-1-or-2-virtual-machine-in-Hyper-V) associa Generation 1 al BIOS legacy e Generation 2 a UEFI. La [documentazione VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrive SeaBIOS, OVMF e il disco EFI che conserva le impostazioni UEFI. **Allinea la modalità di avvio alla sorgente.** Cambiarla durante la migrazione crea un ulteriore problema da diagnosticare.

Per una sorgente Generation 2, riproduci lo stato abilitato o disabilitato di **Secure Boot**. Controlla il modello sorgente e seleziona chiavi registrate compatibili con il guest. I nomi dei modelli Hyper-V non vengono trasferiti a Proxmox. Il disco EFI Proxmox da 4 MB e l'opzione **Pre-Enroll keys** (registrazione preventiva delle chiavi) forniscono chiavi Secure Boot e lo abilitano per impostazione predefinita. Verifica l'avvio della destinazione prima del cutover. Il [riferimento firmware Microsoft](https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmfirmware) descrive il requisito del modello sorgente. La [documentazione Proxmox del disco EFI](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrive le chiavi di destinazione.

Prima di cambiare le chiavi EFI, verifica che la chiave di ripristino sia custodita e registra gli ID dei protector correnti. Segui la documentazione Proxmox VE e OVMF installata per registrare le chiavi EFI. Conferma di nuovo la chiave e verifica `manage-bde -status` prima del primo avvio. Non sospendere, disabilitare o eliminare i protector come passaggio generico di migrazione. Registra versione del pacchetto firmware, stato Secure Boot e versione firmware, e stato BitLocker.

Se la sorgente usa un **vTPM**, aggiungi **TPM State** (stato del TPM) nel pannello Hardware (componenti) di Proxmox prima del primo avvio. Scegli la **versione 2.0**, salvo requisito documentato del guest per la versione 1.2. Questo crea un nuovo stato TPM, non una copia del vTPM Hyper-V. Un guest BitLocker deve avere la chiave di ripristino verificata al primo avvio. La [documentazione TPM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrive l'azione Hardware (componenti) e le versioni.

Per Windows, inizia con il disco di avvio SATA, a meno che il guest non abbia già il driver storage VirtIO necessario. Dopo l'avvio riuscito, installa i driver VirtIO supportati e cambia un solo dispositivo virtuale alla volta. Proxmox consiglia VirtIO SCSI per le prestazioni, ma senza un driver di avvio Windows non può accedere al disco di sistema. Per Linux, controlla che initramfs includa il driver storage di destinazione prima di cambiare bus. La [documentazione VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) descrive i controller dei dischi.

## Importare e collegare i dischi

Sull'host Proxmox, controlla il percorso VHDX copiato. Il comando seguente illustra un'importazione per l'ID VM **230** in uno storage con ID **`local-lvm`**. Sostituisci tutti e tre i valori con i tuoi:

```bash
qm disk import 230 /path/to/exported/boot.vhdx local-lvm
```

Il riferimento Proxmox a [**`qm disk import`**](https://github.com/proxmox/pve-docs/blob/master/generated/qm.1-synopsis.adoc) indica che l'immagine sorgente viene importata come **disco inutilizzato**. La [documentazione immagini QEMU](https://www.qemu.org/docs/master/system/images) elenca VHDX come formato di conversione supportato. Importa separatamente ogni disco dati aggiuntivo. Attendi il completamento di ciascuna importazione e confronta le dimensioni importate con l'inventario sorgente.

Nel pannello **Hardware** (componenti) della VM, collega il disco di avvio inutilizzato come **SATA** per il primo avvio Windows. Collega i dischi dati nell'ordine documentato. In **Options > Boot Order** (opzioni > ordine di avvio), seleziona il disco di avvio. Per un guest Generation 2, verifica **OVMF** e il disco EFI. Mantieni intatti i file importati e la VM sorgente finché la convalida non è superata.

## Testare prima della commutazione

Avvia il guest Proxmox sulla rete isolata. Usa la console per verificare schermata di avvio, accesso al sistema operativo, volumi, dati applicativi e log dei servizi. La sola schermata di login non dimostra la riuscita della migrazione. Esegui i controlli definiti prima dell'esportazione, inclusa una transazione rappresentativa o la lettura di dati recenti.

Per un guest BitLocker, sbloccalo con la chiave di ripristino se richiesto. Dopo l'avvio di Windows, controlla lo stato di protezione del volume di sistema e i protector da un prompt elevato:

```powershell
manage-bde -status C:
manage-bde -protectors -get C:
```

La [guida operativa BitLocker Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) documenta l'ispezione dei protector e il backup della chiave. L'output contiene informazioni di recupero sensibili. Non incollarlo in un ticket o in un log pubblico. Verifica il protector previsto e conserva un metodo di recupero aggiornato secondo la policy. Riavvia il guest e conferma che non compaia un'altra richiesta di recupero prima del cutover. Una richiesta ripetuta indica un controllo di migrazione fallito, non la necessità di scartare la chiave originale.

| Prova | Condizione di superamento |
|---|---|
| **Avvio e dischi** | Il guest si avvia e monta ogni volume previsto |
| **Secure Boot e BitLocker** | La policy di avvio prevista resta attiva e il guest cifrato si riavvia senza ripetere il recupero |
| **Applicazione** | Una lettura o transazione rappresentativa riesce |
| **Rete** | I peer necessari raggiungono il guest di prova sulle porte previste |
| **Ripristino** | Backup Proxmox e test di ripristino isolato riescono prima del ritiro della sorgente |
| **Operazioni** | Monitoraggio, sincronizzazione oraria, arresto e guest agent funzionano come previsto |

Quando i controlli applicativi riescono, cambia il percorso o l'indirizzo di rete di produzione durante la finestra di manutenzione. Mantieni spento Hyper-V. Una NIC virtuale diversa può richiedere una nuova prenotazione DHCP o la correzione di un indirizzo statico nel guest. Da un client separato, controlla DNS, regole firewall e servizi dipendenti. La [documentazione VM Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) tratta i dispositivi di rete e le opzioni del guest agent.

## Risolvere i problemi e tornare indietro

| Sintomo | Primo controllo |
|---|---|
| **Nessun dispositivo di avvio** | Ordine di avvio, disco importato, modalità BIOS o UEFI e chiavi Secure Boot |
| **Errore storage Windows** | Collegamento SATA e driver storage VirtIO mancante |
| **Richiesta BitLocker ripetuta** | Nuovo stato TPM, policy Secure Boot, misurazioni di avvio e protector |
| **Il guest avvia senza rete** | Nuova NIC virtuale, bridge, VLAN, prenotazione DHCP e indirizzo statico |
| **Dati vecchi o mancanti** | VHDX errato, esportazione incompleta, catena checkpoint o disco dati mancante |

Se un test richiesto fallisce prima della scadenza per il rollback, arresta la VM Proxmox e scollegala dalla rete di produzione. Ripristina il percorso di rete sorgente, quindi avvia la VM Hyper-V originale. **Non eseguire mai entrambe le copie con la stessa identità di produzione.** Registra le scritture accettate dalla copia Proxmox prima di tornare a Hyper-V. Richiedono un ripristino o una riconciliazione separata perché il disco sorgente non le ha ricevute.

Conserva VM sorgente ed esportazione finché il guest Proxmox non supera i controlli del servizio, un nuovo backup, un test di ripristino isolato e un periodo di osservazione concordato. Il [confronto di virtualizzazione del sito](/articles/vmware-esxi-citrix-xenserver-hyper-v-comparison/) aiuta a scegliere la piattaforma. La [guida all'aggiornamento Proxmox](/articles/proxmox-ve-8-to-9-upgrade-guide/) copre una manutenzione successiva. **La migrazione termina quando workload e percorso di ripristino funzionano sul nuovo host, non quando termina l'importazione del disco.**

## Passaggi successivi

Conserva VM sorgente ed esportazione finché i controlli del workload, dei backup e del rollback non superano il periodo di osservazione concordato. Consulta la [prova di ripristino del backup VM Proxmox](/articles/proxmox-vm-backup-restore-drill/) prima di ritirare la sorgente.
