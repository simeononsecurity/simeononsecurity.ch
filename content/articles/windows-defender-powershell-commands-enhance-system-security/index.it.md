---
title: "Migliorate la sicurezza del sistema con i comandi PowerShell di Windows Defender"
date: 2023-07-27
toc: true
draft: false
description: "Scoprite la potenza dei comandi PowerShell di Windows Defender e imparate a migliorare la sicurezza del vostro sistema con il controllo della riga di comando."
genre: ["Windows Defender", "Comandi PowerShell", "sicurezza del sistema", "controllo a riga di comando", "antivirus", "Sistemi operativi Windows", "protezione da malware", "impostazioni di sicurezza avanzate", "automatizzare le operazioni di sicurezza", "Windows PowerShell"]
tags: ["Tecnologia", "Sicurezza informatica", "Sistemi operativi", "Finestre", "Strumenti a riga di comando", "Sicurezza del sistema", "PowerShell", "Antivirus", "Protezione da malware", "Scripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "Un'illustrazione animata che raffigura uno scudo che protegge un sistema informatico da varie minacce informatiche."
coverCaption: "Potenziare la sicurezza del sistema con i comandi PowerShell di Windows Defender."
---

## Introduzione

Windows Defender, sviluppato da Microsoft, è una soluzione antivirus e di sicurezza integrata per i sistemi operativi Windows. Offre un'interfaccia facile da usare per gestire efficacemente le impostazioni di sicurezza. Tuttavia, per gli utenti avanzati che preferiscono il controllo da riga di comando, Windows Defender offre una serie di potenti comandi PowerShell. In questo articolo ci addentreremo nel mondo dei **comandi PowerShell di Windows Defender** e scopriremo come possono migliorare la sicurezza del sistema e fornire un maggiore controllo sull'ambiente Windows.

## Il potere dei comandi PowerShell di Windows Defender

I comandi PowerShell di Windows Defender consentono agli utenti di eseguire operazioni di sicurezza avanzate tramite un'interfaccia a riga di comando. Questi comandi offrono un'ampia gamma di funzionalità, da operazioni semplici come la scansione alla ricerca di malware a compiti complessi come la configurazione di impostazioni di sicurezza avanzate. Utilizzando PowerShell, gli utenti possono automatizzare le operazioni di sicurezza, creare script personalizzati e integrare Windows Defender nei flussi di lavoro esistenti senza problemi.

## Come iniziare con Windows Defender PowerShell

Per accedere ai comandi PowerShell di Windows Defender, è necessario aprire una sessione PowerShell con privilegi amministrativi. Ecco come iniziare:

1. Premete `Win + X` e selezionare **Windows PowerShell (Admin)** dal menu.
2. Se richiesto, fare clic su **Sì** per consentire all'applicazione di apportare modifiche al dispositivo.

Una volta aperta una sessione PowerShell, è possibile iniziare a utilizzare i comandi PowerShell di Windows Defender.

## Comandi comuni di Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: Controlla lo stato di Windows Defender

Il `Get-MpComputerStatus` fornisce una panoramica dello stato attuale di Windows Defender sul sistema, compresa la versione del motore antivirus, l'ora dell'ultima scansione e lo stato della protezione in tempo reale. Eseguendo questo comando, è possibile valutare rapidamente la salute complessiva di Windows Defender e assicurarsi che funzioni in modo ottimale.

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

Il `Update-MpSignature` consente di aggiornare manualmente le firme antivirus utilizzate da Windows Defender. Le firme antivirus contengono informazioni cruciali sul malware conosciuto, consentendo a Windows Defender di rilevare e bloccare efficacemente le minacce. Eseguendo questo comando, ci si assicura che il sistema disponga delle firme più recenti, garantendo una maggiore protezione contro le minacce emergenti.

Per aggiornare manualmente le firme di Windows Defender, aprite una sessione PowerShell con privilegi amministrativi ed eseguite il seguente comando:

```powershell
Update-MpSignature
```
Questo comando attiva il processo di aggiornamento, in cui **Windows Defender** si connette ai **server Microsoft** per scaricare le ultime **firme antivirus**. Una volta completato l'aggiornamento, Windows Defender disporrà delle informazioni più aggiornate sul malware conosciuto, rafforzando la sua capacità di identificare ed eliminare le minacce.

Mantenere aggiornate le firme di Windows Defender è essenziale per mantenere il massimo livello di protezione contro il panorama in continua evoluzione del **malware** e delle **minacce informatiche**. Aggiornando regolarmente le firme utilizzando `Update-MpSignature` si assicura che Windows Defender sia in grado di proteggere efficacemente il sistema.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Il `Set-MpPreference` consente di personalizzare varie impostazioni di **Windows Defender**, permettendo di adattare il suo comportamento ai requisiti di sicurezza specifici. Questo comando offre flessibilità nella configurazione di opzioni quali **protezione in tempo reale**, **protezione basata su cloud** e **impostazioni del sistema di ispezione di rete**.

Ad esempio, è possibile attivare o disattivare la protezione in tempo reale utilizzando il comando `Set-MpPreference` comando. La protezione in tempo reale monitora attivamente il sistema alla ricerca di attività dannose e fornisce una risposta immediata alle minacce. Per attivare la protezione in tempo reale, eseguire il seguente comando:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Inoltre, è possibile utilizzare il comando per regolare le impostazioni della protezione basata sul cloud. La protezione basata sul cloud utilizza le risorse del cloud per migliorare il rilevamento delle minacce e fornire risposte più rapide alle minacce emergenti. Per attivare la protezione basata sul cloud, utilizzare il seguente comando:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Inoltre, il `Set-MpPreference` consente di personalizzare le impostazioni del sistema di ispezione di rete. Il sistema di ispezione di rete analizza il traffico di rete alla ricerca di attività sospette e potenziali minacce. Per regolare le impostazioni del sistema di ispezione di rete, eseguire il seguente comando:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Regolando con precisione queste impostazioni con `Set-MpPreference` è possibile ottimizzare **Windows Defender** per allinearsi alle vostre specifiche esigenze di sicurezza e garantire una solida protezione contro il malware e altre attività dannose.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Il `Start-MpScan` è un potente strumento per avviare scansioni di malware sul sistema, consentendo di identificare ed eliminare in modo proattivo i file dannosi. Questo comando offre flessibilità nell'esecuzione di diversi tipi di scansioni, tra cui **scansioni rapide**, **scansioni complete** e **scansioni personalizzate** con percorsi specifici.

Per eseguire una **scansione rapida** utilizzando il comando `Start-MpScan` eseguire il seguente comando PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

Una scansione rapida si concentra sulle aree critiche del sistema in cui è comunemente presente il malware, fornendo una rapida valutazione delle potenziali minacce.

Per una scansione più completa che esamini tutti i file e le directory del sistema, è possibile avviare una **scansione completa**. Eseguire il seguente comando per eseguire una scansione completa utilizzando `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

Una scansione completa garantisce il rilevamento e la rimozione completa del malware dal sistema, ma potrebbe richiedere più tempo rispetto a una scansione rapida.

Oltre ai tipi di scansione predefiniti, l'opzione `Start-MpScan` consente di eseguire scansioni personalizzate specificando percorsi o file specifici da analizzare. Ad esempio, è possibile eseguire la scansione di una directory specifica del sistema utilizzando il seguente comando:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Questo comando avvia una scansione personalizzata della directory specificata, consentendo di individuare aree specifiche del sistema per il rilevamento di malware.

Sfruttando la versatilità del comando `Start-MpScan` è possibile pianificare le scansioni, automatizzare i processi di sicurezza e garantire il rilevamento e la mitigazione delle minacce informatiche sul sistema.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Il `Get-MpThreatCatalog` è una risorsa preziosa per ottenere informazioni dettagliate sulle minacce note e sui loro attributi. Eseguendo questo comando, è possibile accedere a un catalogo completo di minacce, compresi i dati sulla loro gravità, i nomi dei file associati e le azioni consigliate per la mitigazione.

Per recuperare informazioni su minacce specifiche utilizzando `Get-MpThreatCatalog` seguire questi passaggi:

1. Aprite una sessione PowerShell con privilegi amministrativi.
2. Eseguite il seguente comando:

```powershell
   Get-MpThreatCatalog
```
Questo comando visualizza un elenco di minacce conosciute con i relativi dettagli.

L'output del comando `Get-MpThreatCatalog` Il comando include informazioni essenziali quali:

- **ThreatID**: Un identificatore univoco della minaccia.
- **Severità**: Indica il livello di gravità della minaccia, da Basso a Grave.
- **Nome**: Il nome o la descrizione della minaccia.
- **Percorso**: Il percorso del file associato alla minaccia.
- **Azione consigliata**: Fornisce indicazioni sull'azione consigliata da intraprendere per mitigare la minaccia.

Sfruttando le informazioni ottenute da `Get-MpThreatCatalog` è possibile ottenere informazioni preziose sulle minacce potenziali e prendere decisioni informate sulle azioni appropriate per ridurle. Che si tratti di isolare, rimuovere o monitorare una minaccia specifica, il catalogo dettagliato consente di rispondere efficacemente agli incidenti di sicurezza.

Per ulteriori informazioni sull'utilizzo di `Get-MpThreatCatalog` e l'interpretazione dei risultati, consultare la documentazione ufficiale di Microsoft.

Rimanete vigili e utilizzate regolarmente il `Get-MpThreatCatalog` per rimanere informati sull'evoluzione del panorama delle minacce e migliorare la sicurezza del vostro sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Il `Add-MpPreference` consente di aggiungere esclusioni a Windows Defender, permettendo di personalizzare il comportamento della scansione e della protezione in tempo reale. Aggiungendo esclusioni, è possibile specificare file, cartelle o processi che si desidera che Windows Defender ignori durante le scansioni di sicurezza o la protezione in tempo reale.

Per aggiungere un'esclusione utilizzando `Add-MpPreference` è necessario fornire il percorso o il nome del file, della cartella o del processo che si desidera escludere. Ecco un esempio di aggiunta di un'esclusione per una cartella:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Questo comando assicura che Windows Defender salti la scansione della cartella specificata, riducendo gli avvisi inutili e le potenziali interruzioni del flusso di lavoro.

Le esclusioni possono essere utili in vari scenari, come l'esclusione di applicazioni affidabili, ambienti di sviluppo o file specifici che possono generare falsi positivi. Sfruttando la flessibilità di `Add-MpPreference` è possibile mettere a punto Windows Defender in base alle proprie esigenze di sicurezza e ottimizzarne le prestazioni.

Proteggete il vostro sistema in modo efficace, riducendo al minimo i falsi positivi e le interruzioni inutili della scansione, utilizzando le potenti funzionalità di esclusione fornite da `Add-MpPreference`

## Conclusione

I comandi PowerShell di Windows Defender forniscono una serie di strumenti** per gestire e migliorare la sicurezza del sistema Windows. Sfruttando questi comandi, è possibile *automatizzare le operazioni di sicurezza*, *configurare le impostazioni avanzate* e incorporare Windows Defender senza soluzione di continuità nei propri flussi di lavoro. Sia che siate un **amministratore di sistema** o un **utente esperto**, esplorare le capacità dei comandi PowerShell di Windows Defender può migliorare significativamente la sicurezza del vostro sistema.

Ricordate che da un grande potere derivano grandi responsabilità. Quando si utilizzano i comandi PowerShell, occorre essere cauti e assicurarsi di averne compreso l'impatto prima di eseguirli. Combinando le vostre conoscenze con la potenza dei comandi PowerShell di Windows Defender, potrete adottare misure proattive per proteggere il vostro sistema dalle minacce in evoluzione.

## Riferimenti

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)
