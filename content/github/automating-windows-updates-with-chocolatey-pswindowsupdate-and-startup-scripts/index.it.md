---
title: "Semplificate gli aggiornamenti di Windows con l'automazione grazie a Chocolatey, PSWindowsUpdate e agli script di avvio"
date: 2020-07-22
---
 Aggiornamenti di Windows con Chocolatey, PSWindowsUpdate e script di avvio**

Nel frenetico ambiente aziendale di oggi, il tempo è fondamentale per gli amministratori di sistema. L'aggiornamento dei computer Windows, un aspetto critico dell'amministrazione dei sistemi, può essere un'attività estremamente dispendiosa che può richiedere anche una settimana, se il numero di sistemi è sufficiente. Tuttavia, con l'aiuto di Chocolatey, PSWindowsUpdates e Startup Scripts, è ora possibile eseguire gli aggiornamenti con un solo riavvio di ogni macchina, riducendo in modo significativo il tempo necessario per eseguire gli aggiornamenti.

## Semplificare gli aggiornamenti di Windows con l'automazione

Gli aggiornamenti di Windows sono fondamentali per mantenere la stabilità e la sicurezza dei computer Windows. L'esecuzione degli aggiornamenti su un gran numero di macchine può richiedere molto tempo, soprattutto per gli amministratori di sistema con risorse limitate. Tuttavia, con l'uso di strumenti di automazione come Chocolatey, PSWindowsUpdate e Startup Scripts, questo processo può essere semplificato per consentire agli amministratori di eseguire gli aggiornamenti con il minimo sforzo.

### Chocolatey

[Chocolatey](https://chocolatey.org/) è un gestore di pacchetti per Windows che può essere utilizzato per automatizzare l'installazione di software su macchine Windows. È simile ad apt-get su Ubuntu o a homebrew su macOS e può essere utilizzato per installare e gestire un'ampia gamma di pacchetti software. Chocolatey può essere usato per installare i pacchetti in modo silenzioso, cioè senza l'intervento dell'utente.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) è un modulo PowerShell che può essere utilizzato per automatizzare l'installazione degli aggiornamenti di Windows. Fornisce cmdlet che possono essere utilizzati per installare, disinstallare ed elencare gli aggiornamenti di Windows. PSWindowsUpdate è uno strumento potente che può essere utilizzato per gestire gli aggiornamenti di Windows su più macchine, il che lo rende ideale per gli amministratori di sistema che devono gestire un gran numero di macchine.

### Script di avvio

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) sono script che possono essere utilizzati per automatizzare le attività che devono essere eseguite all'avvio o allo spegnimento di una macchina. Questi script possono essere utilizzati per eseguire attività quali l'installazione di software, la configurazione delle impostazioni e la gestione degli aggiornamenti di Windows.

## Automatizzazione degli aggiornamenti di Windows con un singolo riavvio

Per automatizzare gli aggiornamenti di Windows utilizzando Chocolatey, PSWindowsUpdate e gli script di avvio, gli amministratori possono seguire la seguente guida passo passo.

### Impostazione dello script di arresto
Scaricate tutti i file di supporto dal sito [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Aprire l'Editor Criteri di gruppo locali premendo **"Win + R "** e digitando **"gpedit.msc "** seguito da **"Ctrl + Shift + Invio "**.
2. Spostarsi su Computer **Configurazione/Impostazioni di Windows/Scripts (Avvio/Spegnimento)**.
3. Nel riquadro dei risultati, fare doppio clic su Arresto.
4. Selezionare la scheda PowerShell.
5. Nella finestra di dialogo Proprietà shutdown, fare clic su Aggiungi.
6. Nella casella Nome script, digitare il percorso dello script oppure fare clic su Sfoglia per cercare "*chocoautomatewindowsupdates.ps1*" nella cartella condivisa Netlogon del controller di dominio.
7. Riavviare.

Ora l'amministratore deve solo riavviare il computer per eseguire gli aggiornamenti di Windows.

### Comprensione dello script

Lo script utilizzato per automatizzare gli aggiornamenti di Windows è intitolato "*chocoautomatewindowsupdates.ps1*". Esegue le seguenti operazioni:

1. Installa il gestore di pacchetti Chocolatey.
2. Abilita un paio di modifiche alla configurazione di Chocolatey.
3. Aggiorna tutti i pacchetti Chocolatey installati.
4. Installa il modulo PowerShell PSWindowsUpdate.
5. Aggiunge il gestore del servizio Windows Update.
6. Installa tutti gli aggiornamenti di Windows disponibili.
7. Installa tutti i driver mancanti o gli aggiornamenti richiesti dagli aggiornamenti precedentemente installati.

### Vantaggi dell'automazione degli aggiornamenti di Windows

L'automazione degli aggiornamenti di Windows mediante Chocolatey, PSWindowsUpdate e gli script di avvio offre diversi vantaggi agli amministratori di sistema. Questi vantaggi includono:

- **Risparmio di tempo**: L'automazione degli aggiornamenti di Windows riduce significativamente il tempo necessario per eseguire gli aggiornamenti. Gli amministratori non devono più installare manualmente gli aggiornamenti su ogni computer.
- **Consistenza**: L'automazione degli aggiornamenti di Windows garantisce che gli aggiornamenti vengano installati in modo coerente su tutti i computer. Ciò riduce la probabilità di errori e vulnerabilità di sicurezza.
- Gestione centralizzata**: L'automazione degli aggiornamenti di Windows consente agli amministratori di gestire gli aggiornamenti da una posizione centrale, rendendo più facile tenere traccia di quali aggiornamenti sono stati installati e di quali macchine devono essere aggiornate.
- **Maggiore sicurezza**: L'automazione degli aggiornamenti di Windows garantisce che i computer siano aggiornati con le ultime patch di sicurezza, riducendo il rischio di violazioni della sicurezza.

### Conclusione

L'automazione degli aggiornamenti di Windows tramite Chocolatey, PSWindowsUpdate e gli script di avvio è uno strumento potente che può far risparmiare agli amministratori di sistema molto tempo e fatica. Consente di installare gli aggiornamenti in modo coerente ed efficiente, assicurando che i computer siano aggiornati con le ultime patch di sicurezza. Seguendo i passaggi descritti in questa esercitazione, gli amministratori possono automatizzare gli aggiornamenti di Windows con un solo riavvio, rendendo il processo di aggiornamento dei computer Windows molto più rapido e semplice.
