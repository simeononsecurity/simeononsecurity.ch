---
title: "Prova di ripristino di una VM Proxmox: verifica che il sistema guest funzioni"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Verifica un backup di una VM Proxmox con un ripristino isolato. Controlla i dischi inclusi, la modalità di backup, i dati del guest, lo stato del servizio e i tempi di ripristino senza toccare la produzione."
genre: ["Virtualizzazione", "Backup e ripristino", "Laboratorio domestico"]
tags: ["prova di ripristino Proxmox", "backup di VM Proxmox", "esercitazione di ripristino Proxmox", "qmrestore", "vzdump", "verifica di Proxmox Backup Server", "backup snapshot Proxmox", "prova di ripristino VM", "RPO e RTO dei backup", "ripristino isolato VM", "modalità backup Proxmox", "backup con guest agent"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Un backup passa da una VM di produzione arancione attraverso un deposito fino a una VM di test isolata blu. Vengono controllati dischi, servizi e tempi."
coverCaption: "Il completamento di un'attività di backup segna l'inizio di una prova di ripristino."
---

Un'attività di backup verde indica che Proxmox ha scritto un backup. Non mostra se il guest si avvia, se i dati sono aggiornati o se il servizio principale funziona. **Ripristina una copia con un nuovo ID VM su una rete isolata.** Il risultato fornisce una prova del ripristino prima che un'interruzione ti costringa a fare il test.

<!--more-->

Questa esercitazione riguarda una **macchina virtuale Proxmox VE**. I container seguono regole di backup diverse, soprattutto per i mount bind e i mount dei dispositivi. La [prova di backup e ripristino dell'homelab](/articles/homelab-backup-restore-drill/) del sito tratta un recupero di file più ampio. Qui verificherai un backup di una VM Proxmox e il relativo carico di lavoro.

Un **guest** è il sistema operativo in esecuzione all'interno di una macchina virtuale. I **mount bind** e i **mount dei dispositivi** espongono risorse dell'host al guest. Verifica queste risorse con un piano di ripristino separato.

## Punti chiave

- **Definisci prima il successo:** scegli un elemento di dati, un controllo del servizio e un tempo di ripristino accettabile.
- **Controlla la copertura:** il backup di una VM ignora i dischi contrassegnati **No backup** e non ricrea servizi esterni o dati esclusi.
- **Ripristina separatamente:** usa un ID VM libero e mantieni la rete ripristinata isolata dalla produzione.
- **Registra le prove:** misura l'età del backup, il tempo di ripristino, l'avvio, la presenza dei dischi e un controllo reale dell'applicazione.

## Prima di iniziare

Scegli una VM il cui backup sia sicuro da testare. Ti servono accesso amministrativo a Proxmox, un backup completato su file storage o Proxmox Backup Server (PBS), spazio sufficiente per una seconda VM e un bridge isolato o un dispositivo di rete scollegato. Un bridge isolato è una rete virtuale Proxmox senza route verso la LAN di produzione. Se non ne hai uno, usa un adattatore scollegato o una VLAN di test. Lascia accesa la VM di produzione. Riserva un nuovo ID VM, per esempio **920**, dopo aver verificato se un altro guest lo usa. Prevedi abbastanza tempo per un ripristino completo e un test del carico di lavoro.

Scrivi i criteri di superamento prima del ripristino. Per un file server, scegli un file recente e il checksum o contenuto previsto. Per un database, scegli una query di sola lettura sicura e un record scritto prima del backup. Per un servizio web, scegli un controllo di stato locale e una pagina rappresentativa. Registra la data più recente accettabile dei dati, il tuo **obiettivo del punto di ripristino (RPO)**, e il tempo consentito per ripristinare il servizio, il tuo **obiettivo del tempo di ripristino (RTO)**. Una schermata di avvio da sola non soddisfa questi controlli.

| Dato registrato | Esempio di prova |
|---|---|
| **Punto di backup** | Ora dello snapshot e ultimo dato previsto |
| **Destinazione del ripristino** | ID VM libero, storage di destinazione, bridge isolato |
| **Test del carico** | Accesso, mount del volume e lettura dell'applicazione |
| **Limite di tempo** | Ora di inizio e fine del ripristino e del controllo del servizio |

Non collegare il guest ripristinato alla rete di produzione prima di averne controllato nome, indirizzo IP, indirizzo MAC, attività pianificate e integrazioni esterne. Un'identità copiata potrebbe entrare in conflitto con la VM attiva o inviare attività duplicate.

## Controlla cosa copre la copia di sicurezza

**Ambito delle versioni:** gli esempi non sono stati eseguiti durante la preparazione dell'articolo. Prima del test registra l'output di `pveversion --verbose`. Usa la documentazione relativa alla versione installata di Proxmox VE. Registra nel verbale del test il backend di storage, il tipo di guest e l'output dei comandi.

Su un nodo Proxmox, il seguente comando in sola lettura mostra la configurazione della VM di origine. Sostituisci **120** con l'ID della VM di origine:

```bash
qm config 120
```

Elenca ogni disco virtuale e la relativa impostazione di backup. La [documentazione Proxmox sui dischi delle VM](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) spiega che l'opzione **No backup** esclude un disco dal backup della VM. Controlla se i dati dell'applicazione risiedono su un disco escluso, un mount dell'host, hardware passato direttamente o un servizio remoto. Registra la procedura di ripristino separata. Un test di avvio della VM non dimostra che i dati esclusi siano protetti.

Controlla timestamp, dimensioni, registro dell'attività e storage dell'ultimo backup. Nell'interfaccia Proxmox apri la vista **Backups** dello storage di backup oppure la scheda **Backup** della VM. Verifica che l'attività sia terminata senza errori. La [documentazione Proxmox sui backup](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) distingue i normali file di backup dallo storage PBS, che conserva blocchi e metadati deduplicati.

| Modalità di backup | Comportamento della VM | Scelta per questa prova |
|---|---|---|
| **Snapshot** | Esegue il backup di una VM attiva con poco downtime. Le scritture del guest introducono un rischio limitato di incoerenza. | Adatta ai test di routine se il carico tollera questo punto di ripristino. |
| **Stop** | Arresta il guest all'inizio del backup e offre la maggiore coerenza. | Usala se il carico richiede un arresto pulito e il downtime è accettabile. |
| **Suspend** | Sospende il guest prima della modalità snapshot e aggiunge downtime senza un vantaggio generale di coerenza. | Non scegliere suspend come miglioramento predefinito rispetto a snapshot. |

Questi compromessi sono descritti nella [guida Proxmox alle modalità di backup](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Un **QEMU Guest Agent** è un servizio nel guest che permette a Proxmox di chiedere azioni come il congelamento e lo scongelamento del file system. Un guest attivo con il proprio agent abilitato e funzionante supporta queste azioni durante un backup snapshot. Il congelamento del file system migliora la coerenza, ma non sostituisce un controllo di ripristino specifico del database. Registra la modalità effettiva e lo stato del guest agent invece di presumere che un'attività pianificata usi le impostazioni che preferisci.

## Crea o seleziona un punto di ripristino

Usa un backup pianificato recente e riuscito se la prova verifica il ripristino di routine. Se serve un nuovo backup una tantum, apri la scheda **Backup** della VM, scegli **Backup now**, imposta lo storage di destinazione e la modalità e attendi che il registro dell'attività indichi il successo. Da una shell Proxmox, questo esempio esegue il backup della VM **120** sullo storage ID **backup-nfs** in modalità snapshot:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Sostituisci entrambi gli ID con i tuoi. Esegui il comando solo dopo aver confermato che lo storage accetta backup e ha spazio sufficiente. La [documentazione Proxmox di `vzdump`](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) descrive le opzioni di modalità e storage. Controlla il registro dell'attività al termine del comando. Non considerare un backup vecchio come punto di ripristino attuale solo perché il nome del file sembra recente.

Se la destinazione è **PBS**, esegui o controlla un'attività di verifica per il datastore selezionato. La [documentazione PBS sulla verifica](https://pbs.proxmox.com/docs/maintenance.html) spiega come verificare l'integrità dei dati e pianificare controlli ripetuti. La verifica rileva blocchi di backup danneggiati. **Un esito positivo non dimostra che un sistema operativo ripristinato, un'applicazione o una dipendenza esterna funzionino.** Continua comunque con la prova di ripristino.

## Ripristina su una VM isolata

Nell'interfaccia Proxmox seleziona il backup dalla vista **Backups** dello storage e scegli **Restore**. Inserisci un ID VM libero e lo storage di destinazione previsto. Lascia disattivato **Start after restore**. Controlla l'opzione per generare un nuovo indirizzo MAC. La [sinossi ufficiale di `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) definisce un ID VM univoco, la scelta dello storage, `--unique` per un indirizzo Ethernet casuale e l'impostazione predefinita che non avvia la VM ripristinata.

Per un archivio `vzdump` basato su file, questo comando shell mostra lo schema equivalente. Sostituisci percorso dell'archivio, nuovo ID VM e ID dello storage con i valori del tuo ambiente:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

La [descrizione del ripristino Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) dice che senza uno storage di destinazione il ripristino prova a usare quello originale. Imposta **`--storage`** se lo storage precedente non esiste sul nodo di test. Non usare **`--force`** per una prova. L'opzione permette di sovrascrivere una VM esistente, mentre questa procedura richiede un ID libero. I backup PBS si ripristinano anche dall'interfaccia Proxmox. Seleziona la voce dello snapshot PBS invece di trattarlo come un file `.vma.zst` locale.

Prima del primo avvio controlla ogni interfaccia di rete ripristinata, incluse quelle secondarie e passate direttamente. Un **indirizzo MAC** identifica un'interfaccia di rete. **DNS** associa nomi e indirizzi. **DHCP** assegna le impostazioni di rete. Una **VLAN** è una rete logica trasportata su hardware condiviso. Un **TPM virtuale** memorizza lo stato di sicurezza del guest. Scollega ogni interfaccia oppure collegala solo a un segmento di test isolato. Verifica che non siano raggiungibili route di produzione, percorsi DNS, servizi DHCP, reti di gestione o integrazioni esterne. Se il carico richiede un altro servizio di test, prepara una copia di test sulla rete isolata. Confronta con l'origine le mappature dei dischi, il firmware, i requisiti del TPM virtuale e i dispositivi speciali. Dischi esterni, dispositivi passati direttamente e segreti fuori dalla VM richiedono piani separati.

## Verifica il sistema ospite e il carico di lavoro

Avvia la VM ripristinata e usa prima la console. Verifica che il sistema operativo si avvii, che tutti i volumi previsti siano montati, che l'orologio sia corretto e che l'applicazione parta. Poi esegui il criterio di successo definito prima. Confronta un dato noto con il valore e il timestamp precedenti al backup. Una schermata di accesso o un processo attivo non dimostra da solo che il servizio contenga i dati giusti.

| Prova | Criterio di superamento |
|---|---|
| **Avvio** | Il guest raggiunge una schermata di accesso normale senza modalità di riparazione o richieste di ripristino ripetute. |
| **Dischi** | Ogni disco incluso nel backup appare, si monta e contiene i dati previsti. |
| **Servizio** | Una richiesta o lettura locale rappresentativa riesce. |
| **Punto di ripristino** | I dati ripristinati soddisfano l'RPO registrato. |
| **Tempo di ripristino** | Ripristino, avvio e verifica del servizio rispettano l'RTO registrato. |
| **Isolamento** | Nessun indirizzo, attività o integrazione di produzione riceve traffico duplicato. |

Mantieni isolato il guest mentre controlli attività pianificate, hook di notifica, agent di backup e credenziali dell'applicazione. Non eseguire un test che invii messaggi reali ai clienti o scriva nei servizi di produzione. Se un controllo fallisce, registra la fase esatta. Distingui **errore di integrità del backup**, **errore di avvio della VM**, **dati mancanti** e **errore dell'applicazione**. Ognuno richiede una correzione diversa.

| Categoria di errore | Prova di conferma | Prima correzione | Nuovo test |
|---|---|---|---|
| **Integrità del backup** | L'attività di verifica o ripristino segnala dati danneggiati | Seleziona un altro punto di ripristino verificato e controlla lo stato dello storage | Ripeti verifica e ripristino |
| **Avvio della VM** | La console mostra errori di firmware, disco o ripristino | Confronta firmware, mappatura dei dischi e ordine di avvio con l'origine | Avvia la copia isolata e registra il risultato della console |
| **Dati mancanti** | Manca il file, volume o record del database previsto | Controlla dischi esclusi, mount, snapshot e dipendenze esterne | Ripeti il controllo del file o dei dati indicati |
| **Applicazione** | Il guest si avvia ma il controllo del servizio fallisce | Esamina log del servizio, credenziali, dipendenze e passaggi di ripristino | Esegui lo stesso controllo locale e test del carico |

Proxmox offre il [ripristino di singoli file per i backup PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Usalo per testare un percorso di recupero dei file se il carico ne richiede uno. Un file recuperato non sostituisce l'avvio completo della VM e il test del servizio. Proxmox offre anche il ripristino live da PBS. La documentazione afferma che, se un ripristino live fallisce, la VM resta in uno stato indefinito. Per questa prova pianificata usa un ripristino normale e completato.

## Registra il risultato e chiudi l'esercitazione

Registra ID della VM sorgente, storage del backup, timestamp, modalità di backup, nuovo ID VM, storage di destinazione, isolamento di rete, orari di inizio e fine del ripristino, test dell'applicazione, timestamp dei dati ed eventuali controlli falliti. Confronta punto e tempo di ripristino misurati con i tuoi obiettivi. Un errore è una prova utile solo se modifichi il piano di backup e ripeti il test.

Spegni la VM ripristinata al termine delle prove. Rimuovi la copia di test solo dopo aver salvato il risultato e aver verificato che la VM di produzione funzioni ancora come previsto. Conserva il backup secondo la normale policy di retention. Non modificare la retention per far riuscire una sola prova.

Ripeti il test dopo modifiche importanti a storage, guest o configurazione di backup. Alterna le VM importanti, incluse quelle con dischi esclusi o dipendenze esterne. La [guida alla migrazione da Hyper-V a Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) richiede questa prova prima di dismettere la VM di origine. **Un backup utilizzabile ha un percorso di ripristino noto, un carico testato e un punto di ripristino misurato.**

## Passi successivi

Ripeti la prova dopo modifiche allo storage, al guest o al backup. Consulta la [prova di backup e ripristino dell'homelab](/articles/homelab-backup-restore-drill/) per il recupero dei file.
