---
title: "Esegui una prova di ripristino dei backup dell'homelab con Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifica se un backup dell'homelab ripristina file utilizzabili. Definisci un obiettivo di ripristino, recupera i dati con Restic in un'altra posizione, controllali e registra il risultato."
genre: ["Homelab", "Backup", "Ripristino di emergenza"]
tags: ["backup homelab", "prova di ripristino", "ripristino Restic", "verifica backup", "test di ripristino", "ripristino di emergenza", "RPO", "RTO", "repository di backup", "controllo Restic", "backup NAS", "backup server", "ripristino VM", "ripristino file", "crittografia backup", "monitoraggio backup", "piano di ripristino", "test backup", "backup offsite", "integrità dei dati"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Un server homelab e un NAS salvano i dati su un'unità separata, con una cartella di ripristino verificata su un computer di test isolato e un cronometro."
coverCaption: "Ripristina su una destinazione separata, controlla i dati e misura il tempo necessario."
---

Un processo di backup che segnala il successo non dimostra che tu possa recuperare un file utilizzabile. Una **prova di ripristino** verifica il percorso dai dati archiviati a dati funzionanti senza sostituire i file attivi. Questa guida mostra un ripristino di file con Restic e offre un registro da ripetere dopo le modifiche al laboratorio.

<!--more-->

Restic è un programma di backup. Un **repository** è l'area di archiviazione protetta che contiene i dati salvati. Uno **snapshot** è un punto di backup memorizzato.

## Punti chiave

- **Scegli un obiettivo:** Seleziona i file o il servizio da recuperare e definisci un punto e un tempo di ripristino accettabili.
- **Ripristina separatamente:** Usa una destinazione di test vuota per evitare di sovrascrivere i dati attivi.
- **Controlla il risultato:** Apri i file ripristinati, verifica i dati dell'applicazione quando possibile e misura il tempo trascorso.
- **Registra gli errori:** Annota l'ID dello snapshot, gli elementi mancanti, le autorizzazioni e le riparazioni nel piano di ripristino.

## Prima di iniziare

Servono un repository di backup funzionante, la relativa password o chiave, una destinazione con spazio libero sufficiente e i permessi di lettura per il backup e la posizione di test. L'esempio presuppone che Restic sia installato e che il repository contenga un backup recente di file. La [guida rapida di Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) descrive la creazione di un repository e dei primi backup. La [guida alle copie di backup 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) del sito tratta la posizione delle copie. La [panoramica homelab](/articles/what-is-a-homelab-and-should-you-have-one/) include una breve lista di controllo per i backup.

Questa prova controlla i file di uno snapshot. Un database, una macchina virtuale o un'applicazione richiedono anche procedure di ripristino specifiche. Isola il sistema di test se avviare il servizio ripristinato può interferire con quello attivo. Una copia di file riuscita non dimostra che tutti i servizi si avvieranno.

> **Avviso:** Al primo test, non ripristinare su un percorso attivo. Usa una directory di test vuota su un filesystem o host separato. Non inserire la password del repository in schermate, ticket o cronologia della shell.

## Definisci l'obiettivo di ripristino

Annota cosa ti serve dopo un guasto. L'**obiettivo del punto di ripristino (RPO)** è il momento fino al quale i dati devono essere recuperati dopo un'interruzione. Rappresenta la perdita massima di dati accettabile. L'**obiettivo del tempo di ripristino (RTO)** indica per quanto tempo il servizio può restare indisponibile. NIST definisce entrambi nella sua [guida alla pianificazione di emergenza](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). I tuoi obiettivi devono riflettere la frequenza delle modifiche ai dati e il tempo di ripristino sul tuo hardware.

| Elemento | Obiettivo illustrativo | Dati da registrare |
|---|---|---|
| **Documenti di famiglia** | Ultimo backup notturno | Ora dell'ultimo snapshot e file aperti |
| **Configurazione del servizio domestico** | Ultima modifica nota come valida | Versione della configurazione e segreti richiesti |
| **Libreria multimediale su storage collegato alla rete (NAS)** | Backup settimanale | Riproduzione di un campione e tempo di ripristino |

Gli obiettivi sopra sono esempi, non risultati misurati. Nel piano di ripristino, annota la posizione del backup e come una persona autorizzata recupera la password del repository o la chiave di crittografia. Non inserire valori segreti nel piano o nel registro della prova. Conserva i segreti tramite un percorso protetto e indipendente dall'host guasto. Un repository che sopravvive ma perde la sua unica password non è recuperabile.

Scegli un **insieme di file critici** per questa prova. Includi un piccolo file che sai dovrebbe essere nello snapshot più recente. Per un servizio, elenca anche configurazione, esportazione del database, certificati e versione dell'applicazione necessari per avviarlo. Verifica che il metodo di backup acquisisca dati applicativi coerenti prima di affidarti a una copia di file di un database in esecuzione.

## Trova uno snapshot

Usa l'accesso al repository autorizzato per la prova. Restic usa un blocco temporaneo del repository durante la lettura o la modifica dei dati di backup. I comandi seguenti presuppongono che il repository consenta questa operazione. Tieni separati la fonte attiva e la destinazione di test. Sostituisci `/path/to/repository` con il percorso effettivo del repository Restic, poi elenca gli snapshot:

```bash
restic -r /path/to/repository snapshots
```

Restic richiede la password del repository se non l'hai fornita tramite un metodo di gestione dei segreti configurato. La [lista degli snapshot](https://restic.readthedocs.io/en/stable/010_introduction.html) mostra ID, data, host e percorsi sorgente. Registra ID e data e ora dello snapshot da provare. Confronta il timestamp con il tuo RPO. Il registro recente di un processo non sostituisce questo controllo: lo snapshot necessario potrebbe essere più vecchio del previsto.

Se lo snapshot atteso non è presente, interrompi la prova e verifica pianificazione, selezione della fonte e percorso del repository. Non scegliere in silenzio uno snapshot meno recente e dichiarare raggiunto l'obiettivo di ripristino.

## Ripristina in una destinazione vuota

Crea una **directory di destinazione vuota** su un filesystem di test con spazio sufficiente per lo snapshot. Non indicare come destinazione a Restic la fonte originale, una condivisione di produzione montata o una cartella esistente con dati da conservare. Sostituisci `SNAPSHOT_ID` e i due percorsi di esempio prima di eseguire il comando:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

La [guida al ripristino di Restic](https://restic.readthedocs.io/en/stable/050_restore.html) descrive l'ID dello snapshot e il percorso `--target`. L'albero ripristinato conserva il percorso sorgente sotto la directory di destinazione, quindi individua i file effettivi prima di valutare il risultato. Se ti serve solo un piccolo sottoinsieme, usa i [filtri di inclusione documentati](https://restic.readthedocs.io/en/stable/050_restore.html) e registra ciò che escludi. Non usare `--delete` durante una prova. Restic spiega che questa opzione elimina dalla destinazione i file assenti nello snapshot.

Avvia un timer quando inizia il ripristino. Fermalo quando i file richiesti sono presenti e utilizzabili, non quando il comando mostra il primo avanzamento. Registra posizione del repository, collegamento di rete, dimensione dei dati e host di test: queste condizioni incidono sul ripristino futuro.

> **Risultato atteso:** Lo snapshot scelto viene ripristinato in una destinazione separata senza modificare la fonte attiva.

## Verifica dati e servizio

Apri alcuni file ripristinati con l'applicazione che li legge normalmente. Includi un file recente, uno più vecchio e uno in una directory annidata. Confronta dimensioni o checksum noti, se li hai registrati prima del backup. Su Linux controlla proprietario e permessi: un file leggibile dall'account di test potrebbe non esserlo dall'account del servizio.

Per un servizio, ripristina in un'istanza di test isolata. Verifica configurazione, segreti necessari, coerenza del database, avvio e un'azione rappresentativa dell'utente. Un ripristino di file che omette un database o un segreto non è un ripristino completo del servizio. Non avviare l'istanza di test con il database attivo o un indirizzo di produzione senza un piano controllato di passaggio.

Dopo il ripristino del campione, esegui il controllo del repository di Restic:

```bash
restic -r /path/to/repository check
```

Per leggere tutti i dati del repository, usa `check --read-data` durante una finestra di manutenzione. Restic avverte che il comando legge l'intero repository e può scaricare molti dati da un backend remoto. La [guida alla risoluzione dei problemi di Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) descrive il controllo e il suo costo. Un controllo senza errori aumenta la fiducia, ma non sostituisce l'apertura dei file ripristinati o l'avvio del servizio.

```bash
restic -r /path/to/repository check --read-data
```

Confronta l'età dello snapshot con il tuo RPO e il tempo di ripristino misurato con il tuo RTO. Se non raggiungi uno dei due obiettivi, la prova è fallita anche se Restic è terminato senza errori. Modifica frequenza dei backup, posizione dello storage, larghezza di banda o procedura di ripristino e riprova.

## Tieni un registro

Dopo ogni prova, scrivi un breve resoconto. Il [controllo dei backup SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) di NIST include il ripristino di funzioni di sistema campionate come metodo per testare il ripristino. Un registro ripetibile mostra se il piano migliora.

| Campo | Risultato da inserire |
|---|---|
| **Data e operatore** | Quando si è svolta la prova e chi l'ha eseguita |
| **Repository e snapshot** | Posizione, ID, timestamp e percorsi sorgente |
| **Obiettivo di ripristino** | File o servizio testato, con RPO e RTO |
| **Risultato misurato** | Età dello snapshot, tempo di ripristino e controlli su file o servizio |
| **Errori** | Dati mancanti, accesso alle chiavi, permessi, rete o problemi di avvio |
| **Prossima azione** | Responsabile, correzione e data del prossimo test |

Non inserire nel registro la password del repository, la chiave di ripristino o contenuti sensibili dei file. Conservali in un archivio protetto di segreti e documenta come una persona autorizzata li recupera durante un'interruzione.

## Risoluzione dei problemi

- **Password non disponibile:** Controlla il percorso indipendente di custodia della chiave. Non presumere che l'host guasto possa recuperare la propria chiave.
- **Snapshot troppo vecchio:** Controlla pianificazione, processi non riusciti, percorsi sorgente e se l'host previsto abbia salvato in un altro repository.
- **Ripristino troppo lento:** Misura velocità di lettura dello storage, collegamento di rete e volume dei dati. Prova un sottoinsieme critico più piccolo, poi rivedi RTO o progetto di ripristino.
- **File presente ma servizio non funziona:** Controlla esportazioni del database, versione dell'applicazione, proprietario, permessi, certificati e segreti mancanti.
- **Il controllo del repository segnala errori:** Conserva l'output e, se possibile, una copia del repository. Segui la guida Restic per [diagnosticare i danni](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) prima di tentare riparazioni.
- **Il test ha modificato dati attivi:** Arresta il servizio di test, verifica i dati di produzione e correggi il piano di isolamento prima di ripetere la prova.

## Prossimi passi

Ripeti questa prova dopo aver modificato software di backup, storage, chiavi di crittografia o servizi critici. Alterna diversi insiemi di file e ripristini completi di servizi nel tempo. Conserva una copia indipendente secondo il tuo [piano 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). L'obiettivo è una procedura di ripristino misurata e ripetibile quando l'host originale non è più disponibile.
