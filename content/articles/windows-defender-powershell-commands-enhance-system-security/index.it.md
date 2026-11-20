---
title: "Comandi PowerShell di Windows Defender per la sicurezza del sistema"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Scoprite la potenza dei comandi PowerShell di Windows Defender e imparate a migliorare la sicurezza del vostro sistema con il controllo della riga di comando."
genre: ["Windows Defender", "Comandi PowerShell", "sicurezza del sistema", "controllo a riga di comando", "antivirus", "Sistemi operativi Windows", "protezione da malware", "impostazioni di sicurezza avanzate", "automatizzare le operazioni di sicurezza", "Windows PowerShell"]
tags: ["Tecnologia", "Sicurezza informatica", "Sistemi operativi", "Windows", "Strumenti a riga di comando", "Sicurezza del sistema", "PowerShell", "Antivirus", "Protezione da malware", "Sviluppo di script"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Un'illustrazione animata che raffigura uno scudo che protegge un sistema informatico da varie minacce informatiche."
coverCaption: "Potenziare la sicurezza del sistema con i comandi PowerShell di Windows Defender."
---

## Introduzione

Windows Defender, sviluppato da Microsoft, è una soluzione antivirus e di sicurezza integrata per i sistemi operativi Windows. Offre un'interfaccia facile da usare per gestire efficacemente le impostazioni di sicurezza. Tuttavia, per gli utenti avanzati che preferiscono il controllo da riga di comando, Windows Defender offre una serie di potenti comandi PowerShell. In questo articolo ci addentreremo nel mondo dei **comandi PowerShell di Windows Defender** e scopriremo come possono migliorare la sicurezza del sistema e fornire un maggiore controllo sull'ambiente Windows.

## Il potere dei comandi PowerShell di Windows Defender

I comandi PowerShell di Windows Defender consentono agli utenti di eseguire operazioni di sicurezza avanzate tramite un'interfaccia a riga di comando. Questi comandi offrono un'ampia gamma di funzionalità, da operazioni semplici come la scansione alla ricerca di malware a compiti complessi come la configurazione di impostazioni di sicurezza avanzate. Utilizzando PowerShell, gli utenti possono automatizzare le operazioni di sicurezza, creare script personalizzati e integrare Windows Defender nei flussi di lavoro esistenti senza problemi.

## Come iniziare con Windows Defender PowerShell

Per accedere ai comandi PowerShell di Windows Defender, è necessario aprire una sessione PowerShell con privilegi amministrativi. Ecco come iniziare:

1. Premete `Win + X` e selezionate **Windows PowerShell (Admin)** (come amministratore) dal menu.
2. Se richiesto, fate clic su **Yes** (Sì) per consentire all'applicazione di apportare modifiche al dispositivo.

Una volta aperta una sessione PowerShell, è possibile iniziare a utilizzare i comandi PowerShell di Windows Defender.

## Comandi comuni di Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Controlla lo stato di Windows Defender

Il comando `Get-MpComputerStatus` mostra una panoramica dello stato attuale di Windows Defender sul sistema, inclusi la versione del motore antivirus, l’ora dell’ultima scansione e lo stato della protezione in tempo reale. Eseguendolo, è possibile controllare rapidamente che Windows Defender funzioni correttamente.

Per controllare lo stato di Windows Defender, aprite una sessione PowerShell con privilegi amministrativi ed eseguite il seguente comando:

```powershell
Get-MpComputerStatus
```

Questo comando visualizza informazioni quali:

- **AntivirusEngineVersion**: Il numero di versione del motore antivirus utilizzato da Windows Defender.
- **LastFullScanTime**: La data e l'ora dell'ultima scansione completa eseguita da Windows Defender.
- **LastQuickScanTime**: Data e ora dell'ultima scansione rapida eseguita da Windows Defender.
- **RealTimeProtectionEnabled**: Indica se la protezione in tempo reale è attivata o disattivata.

Monitorare regolarmente lo stato di Windows Defender utilizzando `Get-MpComputerStatus` vi assicura di essere sempre informati sul livello di protezione del vostro sistema contro le potenziali minacce.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Il comando `Update-MpSignature` consente di aggiornare manualmente le firme antivirus usate da Windows Defender. Queste firme contengono informazioni importanti sui malware noti e aiutano Windows Defender a rilevare e bloccare le minacce. Eseguendo il comando, il sistema scarica le firme più recenti e migliora la protezione dalle nuove minacce.

Per aggiornare manualmente le firme di Windows Defender, aprite una sessione PowerShell con privilegi amministrativi ed eseguite il seguente comando:

```powershell
Update-MpSignature
```
Questo comando attiva il processo di aggiornamento, in cui **Windows Defender** si connette ai **server Microsoft** per scaricare le ultime **firme antivirus**. Una volta completato l'aggiornamento, Windows Defender disporrà delle informazioni più aggiornate sul malware conosciuto, rafforzando la sua capacità di identificare ed eliminare le minacce.

Mantenere aggiornate le firme di Windows Defender è essenziale per mantenere il massimo livello di protezione contro il panorama in continua evoluzione del **malware** e delle **minacce informatiche**. Aggiornando regolarmente le firme utilizzando `Update-MpSignature` si assicura che Windows Defender sia in grado di proteggere efficacemente il sistema.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Il comando `Set-MpPreference` consente di personalizzare varie impostazioni di **Windows Defender** in base alle proprie esigenze di sicurezza. Offre opzioni per configurare la **protezione in tempo reale**, la **protezione basata sul cloud** e le **impostazioni del sistema di ispezione della rete**.

Ad esempio, è possibile attivare o disattivare la protezione in tempo reale con `Set-MpPreference`. La protezione in tempo reale monitora il sistema per rilevare attività dannose e risponde subito alle minacce. Per attivarla, eseguire il comando seguente:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Inoltre, è possibile utilizzare il comando per regolare le impostazioni della protezione basata sul cloud. La protezione basata sul cloud utilizza le risorse del cloud per migliorare il rilevamento delle minacce e fornire risposte più rapide alle minacce emergenti. Per attivare la protezione basata sul cloud, utilizzare il seguente comando:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

È inoltre possibile usare `Set-MpPreference` per personalizzare le impostazioni del sistema di ispezione della rete. Il sistema analizza il traffico di rete alla ricerca di attività sospette e potenziali minacce. Per modificarne le impostazioni, eseguire il comando seguente:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Regolando con precisione queste impostazioni con `Set-MpPreference` è possibile ottimizzare **Windows Defender** per allinearsi alle vostre specifiche esigenze di sicurezza e garantire una solida protezione contro il malware e altre attività dannose.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Il comando `Start-MpScan` avvia scansioni antimalware sul sistema, consentendo di individuare e rimuovere in modo proattivo i file dannosi. Supporta diversi tipi di scansione, tra cui **scansioni rapide**, **scansioni complete** e **scansioni personalizzate** di percorsi specifici.

Per eseguire una **scansione rapida** con `Start-MpScan`, eseguire il comando PowerShell seguente:

```powershell
Start-MpScan -ScanType QuickScan
```

Una scansione rapida si concentra sulle aree critiche del sistema in cui è comunemente presente il malware, fornendo una rapida valutazione delle potenziali minacce.

Per esaminare tutti i file e le directory del sistema, è possibile avviare una **scansione completa** con `Start-MpScan`. Eseguire il comando seguente:

```powershell
Start-MpScan -ScanType FullScan
```

Una scansione completa garantisce il rilevamento e la rimozione completa del malware dal sistema, ma potrebbe richiedere più tempo rispetto a una scansione rapida.

Oltre ai tipi di scansione predefiniti, `Start-MpScan` consente di specificare percorsi o file per una scansione personalizzata. Ad esempio, è possibile analizzare una directory specifica con il comando seguente:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Questo comando avvia una scansione personalizzata della directory specificata, consentendo di individuare aree specifiche del sistema per il rilevamento di malware.

Sfruttando la versatilità del comando `Start-MpScan` è possibile pianificare le scansioni, automatizzare i processi di sicurezza e garantire il rilevamento e la mitigazione delle minacce informatiche sul sistema.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Il comando `Get-MpThreatCatalog` fornisce informazioni dettagliate sulle minacce note e sui relativi attributi. Il catalogo comprende dati sulla gravità, sui nomi dei file associati e sulle azioni consigliate per mitigare le minacce.

Per recuperare informazioni su minacce specifiche con `Get-MpThreatCatalog`, seguire questi passaggi:

1. Aprite una sessione PowerShell con privilegi amministrativi.
2. Eseguite il seguente comando:

```powershell
   Get-MpThreatCatalog
```
Questo comando visualizza un elenco di minacce conosciute con i relativi dettagli.

L’output del comando `Get-MpThreatCatalog` include informazioni essenziali come:

- **ThreatID**: Un identificatore univoco della minaccia.
- **Severity**: Indica la gravità della minaccia, da Low a Severe.
- **Name**: Nome o descrizione della minaccia.
- **Path**: Percorso del file associato alla minaccia.
- **RecommendedAction**: Indica l’azione consigliata per mitigare la minaccia.

Le informazioni di `Get-MpThreatCatalog` aiutano a valutare le potenziali minacce e a decidere come gestirle. È possibile isolare, rimuovere o monitorare una minaccia. Il catalogo dettagliato supporta una risposta efficace agli incidenti di sicurezza.

Per ulteriori informazioni sull'utilizzo di `Get-MpThreatCatalog` e l'interpretazione dei risultati, consultare la documentazione ufficiale di Microsoft.

Usare regolarmente `Get-MpThreatCatalog` per restare aggiornati sulle minacce e migliorare la sicurezza del sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Il comando `Add-MpPreference` consente di aggiungere esclusioni a Windows Defender e personalizzare il comportamento delle scansioni e della protezione in tempo reale. È possibile indicare i file, le cartelle o i processi che Windows Defender deve ignorare durante le scansioni o la protezione in tempo reale.

Per aggiungere un’esclusione con `Add-MpPreference`, specificare il percorso o il nome del file, della cartella o del processo da escludere. Ecco un esempio per una cartella:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Questo comando assicura che Windows Defender salti la scansione della cartella specificata, riducendo gli avvisi inutili e le potenziali interruzioni del flusso di lavoro.

Le esclusioni possono essere utili in vari scenari, come l'esclusione di applicazioni affidabili, ambienti di sviluppo o file specifici che possono generare falsi positivi. Sfruttando la flessibilità di `Add-MpPreference` è possibile mettere a punto Windows Defender in base alle proprie esigenze di sicurezza e ottimizzarne le prestazioni.

Proteggere il sistema e ridurre falsi positivi e interruzioni inutili delle scansioni con le funzioni di esclusione di `Add-MpPreference`.

## Verifiche dei comandi Defender nel 2026

Eseguite i comandi Defender da una sessione con privilegi elevati solo quando l’attività richiede l’elevazione. Prima di usare un parametro, consultate la guida aggiornata del modulo per la versione di Windows di destinazione. Registrate la configurazione attuale, modificate una sola impostazione per volta, verificate il risultato e annotate il comando di ripristino.

Tra i controlli utili rientrano lo stato della protezione, l’età delle firme, le esclusioni, le preferenze, la cronologia delle scansioni e i rilevamenti recenti. Limitate le esclusioni e registrate il responsabile e la data di scadenza. Consultate la [documentazione del modulo PowerShell di Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) e la [documentazione di Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) per i cmdlet e il comportamento attuali.

## Conclusione

I comandi PowerShell di Windows Defender forniscono una serie di **strumenti** per gestire e migliorare la sicurezza del sistema Windows. Sfruttando questi comandi, è possibile *automatizzare le operazioni di sicurezza*, *configurare le impostazioni avanzate* e incorporare Windows Defender senza soluzione di continuità nei propri flussi di lavoro. Sia che siate un **amministratore di sistema** o un **utente esperto**, esplorare le capacità dei comandi PowerShell di Windows Defender può migliorare significativamente la sicurezza del vostro sistema.

Ricordate che da un grande potere derivano grandi responsabilità. Quando si utilizzano i comandi PowerShell, occorre essere cauti e assicurarsi di averne compreso l'impatto prima di eseguirli. Combinando le vostre conoscenze con la potenza dei comandi PowerShell di Windows Defender, potrete adottare misure proattive per proteggere il vostro sistema dalle minacce in evoluzione.

## Riferimenti

1. Microsoft Docs - [Cmdlet di Windows Defender in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduzione a Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
