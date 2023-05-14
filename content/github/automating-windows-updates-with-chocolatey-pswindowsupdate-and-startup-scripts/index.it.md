---
title: "Semplifica gli aggiornamenti di Windows con l'automazione utilizzando Chocolatey, PSWindowsUpdate e gli script di avvio"
date: 2020-07-22
---
 Aggiornamenti di Windows con Chocolatey, PSWindowsUpdate e script di avvio**

Nel frenetico ambiente aziendale odierno, il tempo è essenziale per gli amministratori di sistema. L'aggiornamento delle macchine Windows, un aspetto critico dell'amministrazione dei sistemi, può essere un'attività estremamente dispendiosa in termini di tempo che può richiedere fino a una settimana, con un numero sufficiente di sistemi. Tuttavia, con l'assistenza di Chocolatey, PSWindowsUpdates e Startup Scripts, è ora possibile distribuire gli aggiornamenti con un solo riavvio di ciascuna macchina, riducendo significativamente il tempo necessario per eseguire gli aggiornamenti.

## Razionalizzazione degli aggiornamenti di Windows con l'automazione

Gli aggiornamenti di Windows sono fondamentali per mantenere la stabilità e la sicurezza delle macchine Windows. L'esecuzione di aggiornamenti su un numero elevato di computer può richiedere molto tempo, in particolare per gli amministratori di sistema con risorse limitate. Tuttavia, con l'uso di strumenti di automazione come Chocolatey, PSWindowsUpdate e Startup Scripts, questo processo può essere semplificato per consentire agli amministratori di eseguire gli aggiornamenti con il minimo sforzo.

### Cioccolatoso

[Chocolatey](https://chocolatey.org/) è un gestore di pacchetti per Windows che può essere utilizzato per automatizzare l'installazione di software su macchine Windows. È simile a apt-get su Ubuntu o homebrew su macOS e può essere utilizzato per installare e gestire un'ampia gamma di pacchetti software. Chocolatey può essere utilizzato per installare i pacchetti in modo silenzioso, il che significa che possono essere installati senza l'intervento dell'utente.

### PSWindows Update

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) è un modulo PowerShell che può essere utilizzato per automatizzare l'installazione degli aggiornamenti di Windows. Fornisce cmdlet che possono essere utilizzati per installare, disinstallare ed elencare gli aggiornamenti di Windows. PSWindowsUpdate è un potente strumento che può essere utilizzato per gestire gli aggiornamenti di Windows su più macchine, rendendolo ideale per gli amministratori di sistema che devono gestire un gran numero di macchine.

### Script di avvio

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) sono script che possono essere utilizzati per automatizzare le attività che devono essere eseguite quando una macchina si avvia o si spegne. Questi script possono essere utilizzati per eseguire attività quali l'installazione di software, la configurazione delle impostazioni e la gestione degli aggiornamenti di Windows.

## Automazione degli aggiornamenti di Windows con un singolo riavvio

Per automatizzare gli aggiornamenti di Windows utilizzando Chocolatey, PSWindowsUpdate e gli script di avvio, gli amministratori possono seguire la guida dettagliata di seguito.

### Impostazione dello script di spegnimento
Scarica tutti i file di supporto dal file[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Apri l'Editor Criteri di gruppo locali premendo **"Win + R"** e digitando **"gpedit.msc"** seguito da **"Ctrl + Maiusc + Invio"**.
2. Accedere a Computer **Configurazione\Impostazioni di Windows\Script (avvio/arresto)**.
3. Nel riquadro dei risultati, fare doppio clic su Arresto.
4. Selezionare la scheda PowerShell.
5. Nella finestra di dialogo Proprietà di arresto, fare clic su Aggiungi.
6. Nella casella Nome script, digitare il percorso dello script o fare clic su Sfoglia per cercare "*chocoautomatewindowsupdates.ps1*" nella cartella condivisa Netlogon sul controller di dominio.
7. Riavvia.

Ora, tutto ciò che un amministratore deve fare è riavviare il computer per eseguire gli aggiornamenti di Windows.

### Comprendere il copione

Lo script utilizzato per automatizzare gli aggiornamenti di Windows è intitolato "*chocoautomatewindowsupdates.ps1*". Svolge i seguenti compiti:

1. Installa il gestore di pacchetti Chocolatey.
2. Abilita un paio di modifiche alla configurazione di Chocolatey preferite.
3. Aggiorna tutti i pacchetti Chocolatey installati.
4. Installa il modulo PSWindowsUpdate PowerShell.
5. Aggiunge il gestore del servizio Windows Update.
6. Installa tutti gli aggiornamenti di Windows disponibili.
7. Installa eventuali driver o aggiornamenti mancanti richiesti dagli aggiornamenti installati in precedenza.

### Vantaggi dell'automazione degli aggiornamenti di Windows

L'automazione degli aggiornamenti di Windows utilizzando Chocolatey, PSWindowsUpdate e gli script di avvio offre diversi vantaggi per gli amministratori di sistema. Questi vantaggi includono:

- **Risparmio di tempo**: l'automazione degli aggiornamenti di Windows riduce notevolmente il tempo necessario per eseguire gli aggiornamenti. Gli amministratori non devono più installare manualmente gli aggiornamenti su ogni macchina.
- **Coerenza**: l'automazione degli aggiornamenti di Windows garantisce che gli aggiornamenti vengano installati in modo coerente su tutte le macchine. Ciò riduce la probabilità di errori e vulnerabilità di sicurezza.
- **Gestione centralizzata**: l'automazione degli aggiornamenti di Windows consente agli amministratori di gestire gli aggiornamenti da una posizione centrale, semplificando il monitoraggio degli aggiornamenti installati e delle macchine che necessitano di aggiornamenti.
- **Maggiore sicurezza**: l'automazione degli aggiornamenti di Windows garantisce che le macchine siano mantenute aggiornate con le patch di sicurezza più recenti, riducendo il rischio di violazioni della sicurezza.

### Conclusione

L'automazione degli aggiornamenti di Windows utilizzando Chocolatey, PSWindowsUpdate e gli script di avvio è uno strumento potente che può far risparmiare molto tempo e fatica agli amministratori di sistema. Consente di installare gli aggiornamenti in modo coerente ed efficiente, assicurando che le macchine siano aggiornate con le patch di sicurezza più recenti. Seguendo i passaggi descritti in questo tutorial, gli amministratori possono automatizzare gli aggiornamenti di Windows con un solo riavvio, rendendo il processo di aggiornamento dei computer Windows molto più rapido e semplice.
