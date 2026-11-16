---
title: "Trova la chiave di ripristino BitLocker prima di reinstallare Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Trova e verifica la chiave di ripristino BitLocker corretta, proteggi una copia separata e scegli il percorso di ripristino o reinstallazione di Windows prima di cancellare un'unità."
genre: ["Sicurezza di Windows", "Recupero dati", "Amministrazione di sistema"]
tags: ["chiave di ripristino BitLocker", "reinstallare Windows 11", "reinstallare Windows 10", "crittografia dispositivo", "ID chiave di ripristino", "chiave di ripristino account Microsoft", "chiave di ripristino account aziendale o scolastico", "backup della chiave di ripristino", "unità crittografata", "installazione pulita", "ripristino Windows", "backup BitLocker", "chiave di ripristino a 48 cifre", "supporto di installazione Windows", "backup dei dati", "crittografia unità", "lista di controllo ripristino", "installazione di Windows", "risoluzione problemi BitLocker", "preparazione alla reinstallazione"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Un portatile con un'unità bloccata, una scheda separata con la chiave di ripristino, un backup USB e una lista di controllo spuntata."
coverCaption: "Verifica la chiave di ripristino prima di cancellare l'unità."
---

Un'installazione pulita di Windows cancella l'unità selezionata. Se la vecchia unità usa **BitLocker** o **Crittografia dispositivo**, trova la chiave di ripristino e copia i file prima di iniziare l'installazione. La chiave consente di accedere ai vecchi dati crittografati. Una nuova installazione di Windows non ripristina i file cancellati dall'unità.

<!--more-->

## Punti principali

- **Trova la chiave giusta:** confronta l'ID della chiave mostrato da Windows con quello salvato nell'account, su una stampa o su un backup USB.
- **Verifica l'accesso:** esamina il backup, confronta l'ID e sblocca un'unità bloccata prima di cancellare le partizioni.
- **Proteggi il backup:** conserva la chiave a 48 cifre separata dal computer e dalla chiavetta di installazione.
- **Scegli il percorso:** usa le opzioni di ripristino se ti serve la vecchia installazione. Scegli l'installazione pulita solo dopo aver verificato una copia separata dei file.

## Prima di iniziare

Ti servono l'accesso al computer interessato, un secondo dispositivo per controllare l'account o il backup e un'unità esterna o un servizio cloud affidabile per i file importanti. **Tempo:** trovare la chiave dipende dall'accesso all'account. Copiare i file dipende dalla quantità di dati. **Difficoltà:** base per controllare un account, intermedia per gli strumenti di ripristino. Questa guida copre preparazione e scelte di ripristino per Windows 10 e Windows 11. La [guida all'installazione pulita di Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) descrive il supporto di installazione e la procedura.

*Il supporto standard di Windows 10 è terminato il 14 ottobre 2025. Se il dispositivo soddisfa i requisiti, pianifica l'installazione di Windows 11 con supporto attivo. Microsoft elenca il [ciclo di vita di Windows 10 e le opzioni di supporto esteso](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Avviso:** non eliminare una partizione per risolvere una richiesta di ripristino BitLocker se ti servono ancora i file della vecchia installazione. Microsoft specifica che il ripristino senza chiave elimina quei file. Consulta le [indicazioni Microsoft sulla chiave di ripristino](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Verifica se la crittografia è attiva

**Crittografia dispositivo** e **BitLocker** crittografano un'unità per impedire a chi non possiede le credenziali corrette di leggerne il contenuto. Se Windows si avvia ancora, in Windows 11 apri **Impostazioni > Privacy e sicurezza > Crittografia dispositivo**. Nelle edizioni con gestione BitLocker, cerca nel menu Start **Gestisci BitLocker**. Annota la lettera dell'unità crittografata e l'account usato per configurare il dispositivo. Per un dispositivo aziendale o scolastico gestito, spesso l'organizzazione conserva la chiave.

Puoi controllare lo stato anche dal prompt dei comandi. Cerca **Prompt dei comandi** nel menu Start, scegli **Esegui come amministratore** e inserisci questi comandi. Sostituisci `C:` se Windows usa un'altra lettera. Un **protector** è un metodo usato da Windows per sbloccare un'unità crittografata.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

Il primo comando mostra crittografia, protezione e stato di blocco. Il secondo elenca tipi e ID dei protector e potrebbe mostrare la password di ripristino. Microsoft documenta entrambi i controlli nella [guida operativa BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) e nel [riferimento del comando di stato](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Non incollare l'output in una richiesta di assistenza e non condividerlo in uno screenshot.** Se il dispositivo è già bloccato, usa l'ID mostrato nella schermata di ripristino. Le prime otto cifre dell'ID aiutano a scegliere la chiave corrispondente.

## Dove trovare la chiave di ripristino BitLocker

L'**ID della chiave di ripristino** identifica una chiave salvata. La **chiave di ripristino** è il numero separato di 48 cifre da inserire per sbloccare l'unità. Non inserire l'ID nel campo della password di ripristino.

| Dispositivo o backup | Dove cercare |
|---|---|
| **Account Microsoft personale** | Da un secondo dispositivo, accedi tramite la [pagina Microsoft delle chiavi di ripristino](https://aka.ms/myrecoverykey). Confronta l'ID prima di usare la chiave a 48 cifre. |
| **Dispositivo aziendale o scolastico** | Controlla l'account dell'organizzazione tramite la [pagina Microsoft per account aziendali o scolastici](https://aka.ms/aadrecoverykey), oppure chiedi al team IT. |
| **Stampa o backup USB** | Trova la stampa o il file di testo creato quando è stata attivata la crittografia. Confronta l'ID con quello sullo schermo. |

Microsoft elenca queste posizioni in [Trova la chiave di ripristino BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Inizia dalla chiave il cui ID corrisponde alla richiesta. Una chiave di un altro dispositivo o di un protector rimosso potrebbe non sbloccare questo volume. Se ha configurato il dispositivo un'altra persona, la chiave potrebbe essere nel suo account.

## Crea una copia di sicurezza separata della chiave

Se Windows si avvia ancora in un'edizione Pro, Enterprise o Education, cerca **Gestisci BitLocker**. Seleziona **Esegui backup della chiave di ripristino** accanto all'unità crittografata. Microsoft offre il backup su un account, un'unità USB, un file di testo o una stampa. Se scegli un file di testo o USB, conservalo solo su un supporto crittografato e con accesso controllato, separato dal computer. Non usare una posizione non crittografata. L'interfaccia e le opzioni aggiornate sono descritte in [Esegui il backup della chiave di ripristino BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key).

In Windows Home **Gestisci BitLocker** non è disponibile. In Windows 11 controlla **Impostazioni > Privacy e sicurezza > Crittografia dispositivo**, poi verifica la chiave nell'account Microsoft usato durante la configurazione. Microsoft spiega che [Crittografia dispositivo](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) salva la chiave nell'account Microsoft o aziendale collegato quando si attiva. Salva una copia protetta separata se la configurazione offre un metodo di esportazione.

Apri un backup digitale da un secondo dispositivo. Per una stampa, confrontala con l'account o la schermata di ripristino. Abbina l'**ID della chiave di ripristino** a quello mostrato nella schermata o nell'elenco dei protector. Verifica che siano presenti tutte le 48 cifre della chiave associata. Conserva la copia cartacea o rimovibile lontano dal computer crittografato. Un ladro con il computer e la chiave potrebbe aggirare la protezione dell'unità, avverte Microsoft nelle [istruzioni di backup](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Non allegare la chiave a un ticket di assistenza.

> **Risultato atteso:** hai una chiave di ripristino corrispondente disponibile fuori dal computer.

## Sblocca un PC che non si avvia

Se appare la **schermata di ripristino BitLocker**, inserisci la chiave a 48 cifre corrispondente all'ID. Se Windows si avvia, copia i file prima di modificare le partizioni. Se la chiave sblocca l'unità ma Windows continua a non avviarsi, usa l'[Ambiente ripristino Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) e prova **Ripristino all'avvio** prima di eseguire un reset. Alcuni strumenti di ripristino richiedono la chiave mentre l'unità è crittografata.

Per copiare file dagli strumenti di ripristino, nell'Ambiente ripristino Windows apri **Risoluzione dei problemi > Opzioni avanzate > Prompt dei comandi**. Usa `manage-bde -status` e `dir` per identificare il volume Windows crittografato e un'unità esterna separata per il backup. **Le lettere delle unità potrebbero essere diverse da quelle usate normalmente.** Non copiare sulla chiavetta di installazione o sull'unità sorgente crittografata.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Le lettere sono esempi. Dopo aver identificato i volumi corretti, sblocca il volume Windows con la chiave corrispondente. Sostituisci la lettera e il segnaposto con i tuoi valori. Digita localmente la vera chiave a 48 cifre. Non pubblicare né condividere l'output.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

L'opzione documentata `-recoverypassword` prende la chiave di 48 cifre come argomento della riga di comando. Questo espone la chiave alla cronologia della shell, alle trascrizioni e all'ispezione dei processi. Usa la schermata di ripristino di Windows se vuoi inserire la chiave senza un argomento di comando. Se hai salvato un file chiave `.bek` separato, `-recoverykey <path-to-external-bek>` evita di digitare le 48 cifre. Tieni la chiave fuori da screenshot e ticket.

Microsoft documenta il [comando di sblocco](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). Le [indicazioni di ripristino](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) descrivono anche la copia dei file utente su un'altra unità dopo lo sblocco. Per copiare a titolo di esempio la cartella Documenti, verifica prima il nome dell'account Windows e la lettera dell'unità esterna, poi sostituisci entrambi i percorsi:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Le opzioni **`/S /E`** includono le sottocartelle, anche vuote. **`/I`** tratta la destinazione come cartella, **`/H`** include i file nascosti e **`/V`** controlla ogni file scritto. Microsoft documenta queste opzioni nel [riferimento xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Ripeti per le altre cartelle necessarie. Apri i file copiati da un altro dispositivo prima di cancellare l'unità Windows. Se non riesci a identificare i volumi o la copia fallisce, fermati e rivolgiti a uno specialista di recupero dati affidabile.

## Decidi se reinstallare Windows

**Il backup della chiave non è un backup dei file.** Prima di scegliere un percorso di reinstallazione, segui questo ordine:

1. Identifica l'unità crittografata e il relativo ID della chiave di ripristino.
2. Recupera la chiave a 48 cifre corrispondente dall'account, dalla stampa o dal backup USB.
3. Se l'unità è bloccata, sbloccala dalla schermata o dagli strumenti di ripristino.
4. Copia Desktop, Documenti, Immagini e altre cartelle locali su un'unità esterna o in un cloud affidabile. Includi, se serve, esportazioni del browser, dati delle applicazioni e registrazioni delle licenze.
5. Apri alcuni file copiati da un secondo dispositivo.
6. Scegli riparazione, reset o reinstallazione solo dopo aver controllato il backup.

> **Risultato atteso:** la chiave corrispondente e i file importanti sono accessibili fuori dalla vecchia installazione Windows.

Microsoft elenca [le opzioni di ripristino di Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), con effetti diversi su file e applicazioni. Molte opzioni nell'Ambiente ripristino Windows richiedono la chiave quando BitLocker protegge l'unità. Se il volume è bloccato lì, **Mantieni i miei file** non lo sblocca senza chiave.

**Ripristino all'avvio** e **Ripristino configurazione di sistema** tentano di riparare l'installazione esistente. **Reimposta il PC** offre **Mantieni i miei file**, ma rimuove applicazioni e impostazioni. **Rimuovi tutto** cancella i file personali. Avviare **`setup.exe` da una sessione Windows funzionante** consente una reinstallazione sul posto con opzioni per conservare i dati. Scegliere **Installa Windows** dopo l'avvio dal supporto USB avvia un percorso di installazione pulita che rimuove file, applicazioni e impostazioni dell'installazione selezionata. Lo stesso supporto offre anche un percorso di riparazione. Leggi l'opzione mostrata e controlla il disco di destinazione prima di confermare un reset o un'installazione. Microsoft descrive entrambi i percorsi nelle [istruzioni di reinstallazione](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situazione | Azione successiva |
|---|---|
| **Windows si avvia e ti servono i file** | Esegui il backup dei file, verifica la chiave e poi scegli una riparazione o reinstallazione. |
| **Windows chiede la chiave** | Abbina l'ID sullo schermo a una chiave salvata prima di modificare l'unità. |
| **Nessuna chiave corrispondente e nessun backup dei file** | Fermati prima di cancellare l'unità. Controlla ogni account, stampa, backup USB e il team IT. |
| **I file sono salvati e vuoi ricominciare** | Segui le [istruzioni di reinstallazione Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) e scegli con attenzione il disco di destinazione. |

Microsoft afferma che il personale di supporto non può ricreare una chiave di ripristino persa. Se non la trovi, smetti di modificare il firmware e controlla tutte le posizioni dei backup. Per un dispositivo gestito, chiedi aiuto all'amministratore. Un reset senza la chiave necessaria elimina i vecchi file. Un'installazione pulita rimuove anche file personali, applicazioni, personalizzazioni del dispositivo e impostazioni dell'installazione selezionata. Fai questa scelta dopo aver verificato il backup.

## Risoluzione dei problemi

- **La chiave non funziona:** ricontrolla l'ID e l'account. Un dispositivo può avere più chiavi di ripristino salvate.
- **Gestisci BitLocker non è disponibile:** Windows Home usa Crittografia dispositivo sui dispositivi idonei. Controlla Impostazioni e l'account Microsoft usato per la configurazione.
- **Nell'account compaiono più chiavi:** confronta le prime otto cifre dell'ID nella schermata con le voci salvate. Non scegliere la chiave solo in base al nome del dispositivo.
- **La chiave sblocca l'unità ma Windows non si avvia:** prova Ripristino all'avvio dall'Ambiente ripristino Windows. Copia i file accessibili prima di un reset o un'installazione pulita.
- **La chiave è custodita da lavoro o scuola:** contatta l'amministratore del dispositivo prima di reimpostarlo o reinstallarlo.
- **Il file della chiave si trova sul computer bloccato:** cerca un account separato, una stampa o un backup rimovibile. Una copia solo sull'unità crittografata non aiuta quando è bloccata.
- **La richiesta è apparsa dopo una modifica del firmware:** annota la modifica e non effettuare altri cambiamenti. Trova la chiave corrispondente o contatta l'amministratore.

## Passaggi successivi

Dopo aver verificato chiave e file, segui la [guida all'installazione pulita di Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) se corrisponde al tuo obiettivo. Quando Windows si avvia, controlla **Impostazioni > Privacy e sicurezza > Crittografia dispositivo** oppure cerca **Gestisci BitLocker**. In Pro, Enterprise o Education, seleziona **Esegui backup della chiave di ripristino** in Gestisci BitLocker. In Home, verifica che l'account collegato contenga la chiave corrente e salva una copia separata se Windows offre l'esportazione. Non presumere che la vecchia chiave valga per una nuova installazione crittografata.
