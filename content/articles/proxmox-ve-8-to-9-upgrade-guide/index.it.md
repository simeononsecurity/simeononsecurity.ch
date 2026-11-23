---
title: "Guida all'aggiornamento da Proxmox VE 8 a 9"
date: 2026-07-22
lastmod: 2026-11-23
toc: true
draft: false
description: "Aggiorna Proxmox VE 8 alla versione 9 con controlli preliminari, passaggi manuali, automazione, modifiche incompatibili e indicazioni per il ripristino."
genre: ["Virtualizzazione", "Amministrazione Linux", "Proxmox", "Gestione dei server", "Software a codice sorgente aperto", "Laboratorio domestico"]
tags: ["Proxmox VE versione 9", "aggiornamento Proxmox", "PVE da 8 a 9", "Debian Trixie", "Debian versione 13", "apt dist-upgrade", "pve8to9", "Ceph in Proxmox", "proxmox-boot-tool", "grub-efi", "aggiornamento LVM", "aggiornamento ZFS", "NVIDIA vGPU", "cgroupv2", "automazione Proxmox", "script di aggiornamento bash", "aggiornamento cluster Proxmox", "aggiornamento in-place", "pve8to9-upgrade.sh", "Proxmox VE versione 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Una moderna sala server con icone luminose che rappresentano macchine virtuali sui monitor. Un tecnico lavora al portatile, circondato da apparecchiature blu scuro con accenti vivaci blu, verdi e viola."
coverCaption: "Aggiornamento di Proxmox VE 8 alla versione 9: procedura in-place passo dopo passo con uno script assistente automatizzato."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9.0 è stato rilasciato con Debian 13 Trixie, kernel 6.14, QEMU 10, LXC 6 e ZFS 2.3.** Questa guida illustra sia il percorso manuale di aggiornamento in-place sia uno script Bash automatizzato che rileva la configurazione e gestisce ogni modifica ai repository, i problemi noti e i controlli preliminari.

## Novità di Proxmox VE 9

Proxmox VE 9 (rilasciato ad agosto 2025) è un aggiornamento di versione principale. Le modifiche principali sono:

| Componente | PVE 8 | PVE 9.0 |
|-----------|--------|--------|
| **Base Debian** | Bookworm (12) | Trixie (13) |
| **Kernel predefinito** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (19.2) |
| **cgroup** | cgroupv2 (v1 ancora possibile) | Solo cgroupv2 |

[Proxmox VE versione 9.2](https://forum.proxmox.com/threads/proxmox-virtual-environment-9-2-available.183742/) include invece il kernel 7.0, QEMU 11, LXC 7 e ZFS 2.4 come impostazione predefinita. Ceph Tentacle è la versione predefinita in 9.2, mentre Squid resta disponibile. Il passaggio a Squid prima di aggiornare un cluster Ceph su VE 8 è un prerequisito separato.

**Tra le principali novità di PVE 9.0 e versioni successive figurano:**
- Snapshot delle macchine virtuali su LVM con provisioning thick tramite catene di volumi (anteprima tecnica → produzione in 9.1)
- Regole di affinità High Availability al posto dei gruppi HA
- SDN Fabrics per reti Ceph full-mesh con OpenFabric e OSPF
- Nuova interfaccia Web mobile (Rust/Yew)
- Espansione dei dispositivi ZFS RAIDZ senza interruzioni
- Bilanciamento dinamico del carico con Cluster Resource Scheduler (PVE 9.2)
- WireGuard e BGP come protocolli SDN fabric (PVE 9.2)
- `/tmp` ora è montato come `tmpfs` (modifica di Debian Trixie: i file vengono ripuliti periodicamente)

{{< figure src="proxmox-ve-8-to-9-component-changes.webp" alt="Diagramma comparativo affiancato di Proxmox VE 8 e VE 9 con le modifiche di versione per kernel, QEMU, LXC, ZFS e Ceph" >}}

______

## Prima di iniziare: prerequisiti

**Devi soddisfare tutti questi requisiti prima di modificare i repository.** Consulta la checklist completa nella [wiki ufficiale sull'aggiornamento — Prerequisiti](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 minimo

```bash
pveversion
```

L'output deve indicare `pve-manager/8.4.x` o una versione successiva. In caso contrario:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph deve essere su Squid (19.x), solo hyper-converged

```bash
ceph --version
```

L'output deve indicare la versione 19.x (Squid). Se usi Reef (18.x) o Quincy (17.x), aggiorna prima Ceph. Il percorso di aggiornamento prevede sempre un passaggio alla volta:

- Quincy (17) → Reef (18) → Squid (19)

*Non iniziare l'aggiornamento a PVE 9 finché tutti i nodi Ceph non eseguono Squid.*

### 3. Proxmox Backup Server installato sullo stesso nodo

Se PBS 3.4 e PVE 8.4 condividono un nodo, segui le [istruzioni per l'installazione sullo stesso nodo](https://pbs.proxmox.com/wiki/Upgrade_from_3_to_4#Installed_alongside_Proxmox_VE) e coordina entrambi gli aggiornamenti in un'unica operazione APT. Verifica che i backup siano ripristinabili ed esegui `pve8to9 --full` e `pbs3to4 --full` prima di modificare i repository. Risolvi i problemi segnalati prima di continuare.

### 4. Requisiti di accesso

- **Consigliato**: accesso alla console tramite IPMI, iKVM o tastiera fisica. La sessione SSH si interromperà al riavvio dei servizi.
- **SSH**: usa `tmux` o `screen` per consentire all'aggiornamento di proseguire se la connessione cade:
  ```bash
  tmux new -s upgrade
  ```

### 5. Spazio su disco

```bash
df -h /
```

Servono almeno **5 GB liberi**, idealmente 10 GB o più.

### 6. Backup validi

Prima di procedere, esegui il backup di tutte le VM e dei container su uno spazio di archiviazione esterno. Verifica un ripristino. Un backup valido è obbligatorio.

______

## Modifiche incompatibili da conoscere

Leggi queste informazioni prima di aggiornare. Alcune modifiche richiedono interventi prima o dopo l'aggiornamento.

### cgroup V1 non è più disponibile

PVE 9 non supporta più l'ambiente cgroupv1 precedente. Se lo avevi abilitato:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Se il comando restituisce un risultato, rimuovi il parametro del kernel da `/etc/default/grub` ed esegui `update-grub` prima dell'aggiornamento.

**Impatto sui container**: i container che eseguono systemd 230 o versioni precedenti (CentOS 7, Ubuntu 16.04) non si avvieranno su PVE 9. Migra questi carichi di lavoro prima di passare a PVE 9. Il supporto del fornitore per Proxmox VE 8.4 è terminato ad agosto 2026.

### Gruppi HA deprecati

Le regole HA sostituiscono i gruppi HA. La migrazione avviene automaticamente quando tutti i nodi del cluster sono su PVE 9. Non serve intervenire manualmente, ma verifica il risultato dopo aver aggiornato l'ultimo nodo.

### Privilegio VM.Monitor rimosso

Devi aggiornare i ruoli personalizzati che fanno riferimento a `VM.Monitor`. Usa `Sys.Audit` per l'accesso di base al monitor KVM. Lo script `pve8to9` rileva i ruoli interessati.

### Nuovo privilegio: VM.Replicate

Per creare o modificare lavori di replica dello storage serve ora `VM.Replicate` su `/vms/<vmid>`. Se necessario, modifica i ruoli personalizzati.

### I container LXC privilegiati richiedono Sys.Modify

La creazione di nuovi container privilegiati richiede ora `Sys.Modify`. Il ripristino in-place di un container privilegiato esistente non lo richiede.

### systemd-sysctl non legge più /etc/sysctl.conf

Dopo l'aggiornamento, le impostazioni personalizzate in `/etc/sysctl.conf` verranno ignorate senza avvisi. Prima del riavvio, spostale in `/etc/sysctl.d/<NN>-name.conf`.

```bash
# Controlla il contenuto di sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp ora è tmpfs

Debian Trixie monta `/tmp` come tmpfs, fino al 50% della RAM. I file vengono ripuliti periodicamente mentre il sistema è in esecuzione. Se usi `/tmp` per file temporanei di grandi dimensioni, sposta il lavoro in `/var/tmp` o su un mount dedicato.

### Compatibilità di Veeam Backup and Restore {#veeam-backup-broken-for-qemu-machine-version--100}

Prima dell'aggiornamento, controlla le [build del plug-in Veeam Backup & Replication e Proxmox](https://helpcenter.veeam.com/docs/vbr/userguide/pve_system_requirements.html). I requisiti attuali elencano Proxmox VE dalla versione 8.2 alla 9.2 su host x86-64 installati con l'ISO ufficiale di Proxmox. Le build Veeam precedenti hanno intervalli di supporto propri.

Le attuali [limitazioni di Veeam](https://helpcenter.veeam.com/docs/vbr/userguide/pve_limitations.html) supportano i backup delle VM da storage basato su LVM con Snapshots as Volume Chains (SAVC) abilitato. Questo non rende SAVC una posizione supportata per i file dei worker Veeam o per una destinazione Instant Recovery. Un problema di ripristino separato, descritto nella [KB4773](https://www.veeam.com/kb4773), interessa i tipi di macchina QEMU precedenti alla versione 10 con dischi QCOW2 ripristinati su storage SAVC in PVE 9. Usa una destinazione senza SAVC oppure ripristina il disco come RAW seguendo la documentazione. Sono soluzioni per il ripristino, non motivi per mantenere lo stesso tipo di macchina nell'intero parco. Prima di affidarti all'aggiornamento, prova un backup e un ripristino sullo storage previsto.

### I nomi delle interfacce di rete potrebbero cambiare

Il kernel 6.14 riconosce più funzioni NIC rispetto alla versione 6.8. Alcune schede ricevono suffissi aggiuntivi nei nomi. Lo strumento `pve-network-interface-pinning` permette di assegnare nomi stabili `nicX` a tutte le interfacce prima dell'aggiornamento:

```bash
pve-network-interface-pinning --help
```

______

## Opzione A: aggiornamento manuale in-place

Segui i passaggi ufficiali nella [guida di aggiornamento Proxmox VE](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Passaggio 1: esegui la checklist pve8to9

```bash
pve8to9 --full
```

Risolvi ogni elemento `FAIL` prima di continuare. Ripeti il controllo dopo ogni correzione.

### Passaggio 2: migra le VM in esecuzione, se il nodo è in un cluster

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Passaggio 3: aggiorna completamente PVE 8

```bash
apt update && apt dist-upgrade
pveversion   # deve mostrare la versione 8.4.1 o successiva
```

### Passaggio 4: aggiorna i repository di base Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Commenta o rimuovi tutte le righe di repository specifiche per Bookworm rimaste.

### Passaggio 5: aggiungi il repository dei pacchetti PVE 9

**Enterprise, abbonamento richiesto:**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Senza abbonamento:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Verifica con `apt update && apt policy` che il nuovo repository compaia senza errori. Poi rimuovi o commenta il vecchio file `.list`.

### Passaggio 6: aggiorna il repository Ceph, solo hyper-converged

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Per le installazioni senza abbonamento, usa `http://download.proxmox.com/debian/ceph-squid` con `pve-no-subscription`.

### Passaggio 7: aggiorna l'indice dei pacchetti

```bash
apt update
```

Verifica che non ci siano errori.

### Passaggio 8: esegui dist-upgrade

```bash
apt dist-upgrade
```

L'operazione dura da 5 a oltre 60 minuti, a seconda della velocità dello storage. Durante l'aggiornamento:

- **`/etc/issue`**: mantieni la versione corrente (sicuro)
- **`/etc/lvm/lvm.conf`**: installa la versione del manutentore (consigliato)
- **`/etc/ssh/sshd_config`**: installa la versione del manutentore se non hai personalizzato il file
- **`/etc/default/grub`**: mantieni la versione corrente se hai personalizzato il file
- **`/etc/chrony/chrony.conf`**: installa la versione del manutentore se non hai personalizzato il file

### Passaggio 9: riavvia

```bash
reboot
```

È necessario riavviare anche se il kernel 6.14 era già installato come opzione in PVE 8. Il kernel viene ricostruito con le toolchain di PVE 9.

### Passaggio 10: attività dopo l'aggiornamento

```bash
# Svuota la cache del browser: Ctrl+Shift+R (o ⌘+Alt+R su macOS)
# Verifica tutti i nodi del cluster:
pvesh get /nodes

# Nei cluster: i gruppi HA migrano automaticamente alle regole HA quando tutti i nodi usano PVE 9
journalctl -eu pve-ha-crm  # controlla la presenza di errori
```

______

## Opzione B: script automatizzato (pve8to9-upgrade.sh)

La procedura manuale comprende molti passaggi condizionati dalla configurazione. Lo script `pve8to9-upgrade.sh` li automatizza tutti.

**Fonte dello script:** [repository Gist dello script](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Cosa fa lo script

Lo script gestisce automaticamente l'intero aggiornamento, inclusi:

| Rilevamento | Azione |
|-----------|--------|
| Repository Enterprise o senza abbonamento | Usa il tipo di repository **attualmente abilitato**, senza abilitare Enterprise sui nodi senza abbonamento |
| Versione di Ceph | Blocca Quincy o Reef e mostra la guida dettagliata per l'aggiornamento di Ceph |
| Tipo di repository Ceph | Scrive un nuovo `ceph.sources` coerente con il tipo di repository esistente |
| Driver NVIDIA vGPU | Blocca i driver precedenti alla versione 570 (GRID 18.3 minimo) |
| Passthrough GPU NVIDIA | Mostra un avviso e crea un promemoria per il test successivo all'aggiornamento |
| Repository CUDA | Aggiorna `debian12` a `debian13` nei percorsi URI |
| Metapacchetto systemd-boot | Lo rimuove (corregge il bug Debian #1110177 che interrompe dist-upgrade) |
| Impostazioni personalizzate sysctl.conf | Le migra in `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Deadlock FRR dopo il riavvio | Corregge `/etc/network/interfaces` prima del riavvio |
| `systemd-journald-audit.socket` | Lo disabilita per evitare un eccesso di log durante l'aggiornamento |
| Problema GRUB con UEFI e LVM | Installa `grub-efi-amd64` e scrive una scheda di ripristino in `/root/` |
| Repository di terze parti `bookworm` | Li commenta aggiungendo un promemoria per aggiornarli |
| Conflitto `linux-image-amd64` | Rimuove il pacchetto se presente |
| Attivazione automatica LVM | Esegue lo script di migrazione prima e dopo l'aggiornamento |
| Proxmox Backup Server (server di backup Proxmox) | Esegue il controllo `pbs3to4 --full` e aggiorna i repository PBS per Trixie |
| Root su ZFS | Rileva la configurazione e la conferma; non servono interventi speciali |

Tutte le modifiche vengono registrate in `/var/log/pve8to9-upgrade-<timestamp>.log`. I backup dei repository APT vengono scritti in `/root/pve8to9-apt-backups/`. Non vengono mai copiati come file `.bak` in `/etc/apt/sources.list.d/`, perché la Web UI li segnalerebbe con errori "invalid extension".

### Installazione e utilizzo

```bash
# Scarica lo script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Rendi eseguibile il file
chmod +x pve8to9-upgrade.sh

# Esaminalo prima di eseguirlo (leggi sempre gli script prima di eseguirli come root)
less pve8to9-upgrade.sh
```

**Modalità di esecuzione:**

```bash
# Modalità interattiva completa (consigliata)
./pve8to9-upgrade.sh

# Approva automaticamente le correzioni sicure e non distruttive
./pve8to9-upgrade.sh --yes

# Esecuzione di prova: mostra ogni modifica senza applicarla
./pve8to9-upgrade.sh --dry-run

# Salta il controllo preliminare pve8to9 --full (opzione sconsigliata)
./pve8to9-upgrade.sh --skip-preflight
```

*Se ti connetti tramite SSH, esegui lo script in `tmux` o `screen`.*

### Esempio di output dello script

Prima di chiederti di procedere, lo script riepiloga la configurazione rilevata:

```
══════════════════════════════════════════
  SUMMARY of detected configuration
══════════════════════════════════════════

  PVE version      : pve-manager/8.4.3/...
  Debian           : bookworm
  Subscription     : true (status: Active)
  PVE repo type    : enterprise  (enterprise was active: true)
  Ceph             : YES (v19.2.3, enterprise repos)
  ZFS root         : false
  UEFI boot        : true
  LVM root         : true
  NVIDIA           : NO
  CUDA repos       : NO
  systemd-boot     : meta=true efi=true
  sysctl.conf      : custom=false (0 lines)
  cgroupv1         : false (must be false for PVE 9)
  FRR post-up      : false (broken pattern)
  LVM autoact.     : false
  PBS co-install   : NO
  3rd-party bookwm : none
```

### Controlli di sicurezza che bloccano lo script

Lo script **rifiuta di proseguire** se si verifica una delle condizioni seguenti:

- cgroup V1 è esplicitamente abilitato nella riga di comando del kernel
- Ceph è ancora su Quincy (17.x) o Reef (18.x): vengono mostrate le istruzioni esatte per aggiornare Ceph
- Il driver NVIDIA vGPU è precedente alla versione 570 (GRID 18.3)
- La versione PVE è precedente alla 8.4

Per ogni problema bloccante, lo script stampa i comandi esatti per risolverlo prima di ripetere il controllo.

______

## Problemi noti durante l'aggiornamento

### GRUB non avvia LVM in modalità UEFI

**Interessa**: sistemi con root su LVM, avviati in modalità UEFI e aggiornati da PVE 7.x.

```bash
# Correzione (eseguila sul sistema attivo dopo l'aggiornamento):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

Lo script `pve8to9-upgrade.sh` rileva UEFI e LVM e installa automaticamente il pacchetto. Scrive anche una scheda di ripristino in `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Se il nodo è già bloccato** su `grub rescue>` o sul messaggio "disk 'lvmid/...' not found":

1. Avvia l'ISO di PVE → Advanced → **Rescue Boot**
2. In alternativa, segui sul wiki ufficiale i [passaggi per ripristinare GRUB su LVM](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)

### Il metapacchetto systemd-boot interrompe dist-upgrade

Il metapacchetto `systemd-boot` viene installato automaticamente dai sistemi PVE 8.1–8.4 installati tramite ISO. In Trixie contiene hook che si attivano quando si aggiornano altri pacchetti e possono interrompere `dist-upgrade` a metà se l'ESP non è montata (bug Debian #1110177).

```bash
# Rimuovilo prima di eseguire dist-upgrade:
apt remove systemd-boot
# NON rimuovere systemd-boot-efi o systemd-boot-tools: devono restare installati
```

Lo script `pve8to9-upgrade.sh` gestisce questa situazione automaticamente e ne spiega in dettaglio il motivo.

### Il passthrough PCI potrebbe non funzionare con il kernel 6.14

Alcuni utenti segnalano che le VM con passthrough PCI non si avviano con il kernel 6.14. Se succede:

```bash
# Blocca temporaneamente il kernel precedente:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Le configurazioni Ceph full-mesh si bloccano al riavvio

Se `/etc/network/interfaces` contiene:

```
post-up /usr/bin/systemctl restart frr.service
```

Sostituiscilo con:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Esegui questa modifica **prima del riavvio**. Lo script rileva e corregge automaticamente questo schema.

### Il thin pool LVM richiede una riparazione

Dopo l'aggiornamento, in alcuni sistemi compare:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Correzione:

```bash
lvconvert --repair pve/data
```

### Versione minima del driver NVIDIA vGPU

Prima dell'aggiornamento serve almeno il **driver 570.158.02** (GRID 18.3). I driver precedenti non sono compatibili con il kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Ordine di aggiornamento del cluster

Aggiorna un nodo alla volta. Verifica che ciascun nodo sia in buono stato prima di iniziare il successivo.

```bash
# Controlla lo stato del cluster prima di aggiornare ogni nodo:
pvecm status
ceph -s   # se Ceph è in uso
```

**Regole di migrazione durante un aggiornamento parziale:**

- VM/CT da PVE 8 a PVE 9: sempre supportata
- VM/CT da PVE 9 a PVE 8: in genere non supportata

Dopo aver aggiornato tutti i nodi a PVE 9, i gruppi HA migrano automaticamente alle regole di affinità HA. Controlla eventuali errori:

```bash
journalctl -eu pve-ha-crm
```

______

## Risoluzione dei problemi

### L'aggiornamento si blocca o mostra "proxmox-ve would be removed"

Se vedi:

```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Uno o più pacchetti non si aggiornano perché è ancora configurato un repository Bookworm. Trova le voci Bookworm residue:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Commentale, poi esegui:

```bash
apt update && apt dist-upgrade
```

Se l'aggiornamento è stato completato solo in parte:

```bash
apt -f install
```

### Il sistema non si avvia dopo l'aggiornamento ZFS

Se usi ZFS come root e l'avvio avviene tramite BIOS legacy, consulta [ZFS: passare dall'avvio legacy a Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). Sui sistemi ZFS, `proxmox-boot-tool` deve gestire l'avvio, non GRUB direttamente, per mantenere l'avvio dopo gli aggiornamenti delle funzioni ZFS.

______

## Checklist dopo l'aggiornamento

Dopo aver riavviato ogni nodo:

- [ ] Svuota la cache del browser (`Ctrl+Shift+R` / `⌘+Alt+R`)
- [ ] `pveversion` mostra la versione 9.x
- [ ] `uname -r` mostra la versione 6.14.x o successiva
- [ ] Tutte le VM e i container si avviano correttamente
- [ ] Stato Ceph: `ceph -s` mostra HEALTH_OK
- [ ] Se UEFI e LVM: verifica che `grubx64.efi` abbia una data di modifica recente
- [ ] Se usi passthrough NVIDIA: prova una VM non di produzione
- [ ] Aggiorna i repository di terze parti commentati durante l'aggiornamento
- [ ] Sposta le impostazioni personalizzate di `/etc/sysctl.conf` in `/etc/sysctl.d/`

## Verifica dopo l'aggiornamento

Dopo l'aggiornamento, controlla la configurazione dei repository, il quorum del cluster, lo stato dello storage, l'avvio delle macchine guest, i backup, le regole firewall e l'accesso amministrativo. Esamina i log di sistema prima di dichiarare concluso l'aggiornamento. Se il cluster lo permette, prova il ripristino di un guest su un host separato.

Per i comandi specifici di una versione, consulta la [guida di amministrazione Proxmox VE](https://pve.proxmox.com/pve-docs/) e le [note di rilascio](https://pve.proxmox.com/wiki/Roadmap) aggiornate. Non copiare un comando da una versione precedente senza controllare la versione di destinazione e lo stato dei backup.

## Riferimenti

1. [Ufficiale: aggiornamento di Proxmox VE da 8 a 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Ufficiale: aggiornamento da 8 a 9 — Prerequisiti](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script di automazione pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Problemi noti di Proxmox VE 9.0 (Roadmap)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Ripristino di GRUB — errore LVM "disk not found"](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: passare dall'avvio legacy a Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Guida per aggiornare Ceph da Reef a Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Pinning delle interfacce di rete Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Note di rilascio Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)
