---
title: "PowerShell Scripting: Una guida passo a passo per i principianti per automatizzare le attività"
draft: false
toc: true
date: 2023-02-25
description: "Imparate le basi dello scripting PowerShell e automatizzate le attività con questa guida passo passo per principianti, che comprende cmdlet, loop, funzioni e altro ancora."
genre: ["Tecnologia", "Programmazione", "Automazione", "Finestre", "Scripting", "IT", "Compiti amministrativi", "Gestione del computer", "Sviluppo di software", "Codifica"]
tags: ["Scripting PowerShell", "Automazione PowerShell", "Scripting per Windows", "I cmdlet di PowerShell", "Moduli PowerShell", "Loop di PowerShell", "Dichiarazioni condizionali di PowerShell", "Funzioni PowerShell", "Le migliori pratiche di PowerShell", "Debug di PowerShell", "Test di PowerShell", "Variabili PowerShell", "PowerShell ISE", "Remoting PowerShell", "Tecnologie Microsoft", "Automazione IT", "gestione del computer", "codifica per principianti", "compiti amministrativi", "Idee di script PowerShell", "backup automatici", "gestione dei file", "informazioni sul sistema", "gestione degli utenti", "installazione del software", "configurazione di rete", "automazione della sicurezza", "programmazione dei task", "manipolazione del registro", "amministrazione remota"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Un personaggio dei cartoni animati con in mano uno script e in piedi davanti a un computer con il prompt di PowerShell, che indica la facilità di scripting di PowerShell per i principianti"
coverCaption: ""
---
 Scripting PowerShell per principianti**

PowerShell è un potente linguaggio di scripting e shell a riga di comando sviluppato da Microsoft. Offre una vasta gamma di comandi e funzioni per la gestione e l'automazione di vari aspetti del sistema operativo Windows e di altre tecnologie Microsoft. In questo articolo tratteremo le basi dello scripting PowerShell per i principianti e forniremo una guida passo passo per iniziare.

## Introduzione a PowerShell

**PowerShell** è una shell a riga di comando che consente agli utenti di automatizzare e gestire il sistema operativo Windows e altre tecnologie Microsoft. Fornisce una serie completa di comandi e funzioni che consentono agli utenti di eseguire varie attività amministrative, come la gestione di file e directory, la configurazione di rete e la gestione del sistema. PowerShell supporta anche un linguaggio di scripting che consente agli utenti di creare script complessi e automatizzare varie attività ripetitive.

## Iniziare con PowerShell

### Installazione di PowerShell

PowerShell è preinstallato nella maggior parte delle versioni del sistema operativo Windows. Tuttavia, se si utilizza una versione precedente di Windows o se si necessita di una versione più recente di PowerShell, è possibile scaricarla dal sito Web di Microsoft. Per scaricare e installare PowerShell, procedere come segue:

1. Andare al sito [Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) e selezionare la versione di PowerShell che si desidera installare.
2. Scaricare il file di installazione ed eseguirlo.
3. Seguire le istruzioni sullo schermo per completare il processo di installazione.

### Avvio di PowerShell

Una volta installato PowerShell, è possibile avviarlo seguendo i seguenti passaggi:

1. Fate clic sul menu Start e digitate "PowerShell" nella barra di ricerca.
2. Selezionate "Windows PowerShell" dai risultati della ricerca.
3. PowerShell si aprirà in una nuova finestra.

### Nozioni di base di PowerShell

PowerShell fornisce un'interfaccia a riga di comando che consente agli utenti di interagire con il sistema operativo. I comandi di PowerShell sono chiamati cmdlets e sono organizzati in moduli. Per visualizzare un elenco dei moduli disponibili, utilizzare il comando Get-Module:

```powershell
Get-Module
```

Per visualizzare un elenco di cmdlet disponibili in un modulo, utilizzare il comando Get-Command:
```powershell
Get-Command -Module <module name>
```

Per ottenere una guida su un cmdlet, utilizzare il comando Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell supporta anche gli alias, che sono nomi più brevi per le cmdlet. Per visualizzare un elenco degli alias disponibili, utilizzare il comando Get-Alias:
```powershell
Get-Alias
```

### Scripting PowerShell
Lo scripting di PowerShell è una potente funzione che consente agli utenti di automatizzare varie attività amministrative. Lo scripting di PowerShell supporta variabili, loop, dichiarazioni condizionali e funzioni, rendendolo un potente strumento di automazione.

#### Variabili
Le variabili sono utilizzate per memorizzare i dati negli script PowerShell. Le variabili in PowerShell iniziano con il segno del dollaro ($). Per assegnare un valore a una variabile, utilizzare la seguente sintassi:
```powershell
$variable_name = value
```
Ad esempio:
```powershell
$name = "John"
```
#### Loops
I loop vengono utilizzati per ripetere un blocco di codice un certo numero di volte. PowerShell supporta i seguenti tipi di loop:

- **For loop**: ripete un blocco di codice per un numero specifico di volte.
- **Ciclo While**: ripete un blocco di codice finché una condizione è vera.
- **Ciclo Do-While**: ripete un blocco di codice almeno una volta e poi finché una condizione è vera.
- **orEach loop**: ripete un blocco di codice per ogni elemento di un insieme.
  
Ad esempio, il codice seguente utilizza un ciclo For per stampare i numeri da 1 a 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Dichiarazioni condizionali

Dichiarazioni condizionali

Le dichiarazioni condizionali vengono utilizzate per eseguire un blocco di codice se una certa condizione è vera. PowerShell supporta i seguenti tipi di istruzioni condizionali:

- **Indicazione If**: esegue un blocco di codice se una condizione è vera.
- **If-Else**: esegue un blocco di codice se una condizione è vera e un altro blocco di codice se la condizione è falsa.
- **Esercizio switch**: confronta un valore con un insieme di possibili corrispondenze ed esegue un blocco di codice per la prima corrispondenza trovata.

Ad esempio, il codice seguente utilizza un'istruzione If per verificare se un numero è superiore a 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Funzioni
Le funzioni sono blocchi di codice riutilizzabili che eseguono un compito specifico. Le funzioni accettano parametri di ingresso e restituiscono valori di uscita. PowerShell supporta i seguenti tipi di funzioni:

- **Blocco di script**: un blocco di codice che può essere eseguito.
- Funzione avanzata**: una funzione che include metadati e convalida dei parametri.

Ad esempio, il codice seguente definisce una funzione che aggiunge due numeri:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "The result is $result"
```
### PowerShell ISE
PowerShell ISE (Integrated Scripting Environment) è un'interfaccia grafica per lo scripting PowerShell. PowerShell ISE fornisce un editor di testo ricco, strumenti di debug e altre funzioni che facilitano la scrittura e il test degli script PowerShell. Per aprire PowerShell ISE, procedere come segue:

1. Fare clic sul menu Start e digitare "PowerShell ISE" nella barra di ricerca.
2. Selezionate "Windows PowerShell ISE" dai risultati della ricerca.
3. PowerShell ISE si aprirà in una nuova finestra.

### PowerShell Remoting
PowerShell Remoting consente agli utenti di eseguire comandi e script PowerShell su computer remoti. PowerShell Remoting richiede che il servizio WinRM sia in esecuzione sia sul computer locale che su quello remoto. Per abilitare PowerShell Remoting, procedere come segue:

1. Aprire un prompt di PowerShell con privilegi di amministratore.
2. Eseguite il seguente comando per abilitare PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Eseguire il seguente comando per aggiungere il computer remoto all'elenco TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Riavviare il servizio WinRM
```powershell
Restart-Service WinRM
```

Per eseguire un comando PowerShell su un computer remoto, utilizzare il cmdlet Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Moduli PowerShell
I moduli PowerShell sono raccolte di cmdlet, funzioni e script progettati per eseguire compiti specifici. I moduli PowerShell possono essere installati e gestiti utilizzando la PowerShell Gallery, che è un repository centrale per i moduli PowerShell.

Per installare un modulo PowerShell dalla PowerShell Gallery, utilizzare il seguente comando:
```powershell
Install-Module <module name>
```

Per visualizzare un elenco dei moduli PowerShell installati, utilizzare il comando Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Migliori pratiche per lo scripting di PowerShell

Quando si scrivono script **PowerShell**, è importante seguire le best practice per garantire che gli script siano **sicuri**, **affidabili** e **mantenibili**. Ecco alcune best practice da tenere a mente:

- **Utilizzare nomi di variabili descrittivi**: Utilizzare nomi di variabili che indichino chiaramente il loro scopo.
- Usare commenti**: Utilizzare commenti per spiegare lo scopo del codice.
- **Utilizzare la gestione degli errori**: Usare la gestione degli errori per gestire con grazia gli errori e le eccezioni. Il `Try...Catch...Finally` in PowerShell consente di gestire le eccezioni e di intraprendere azioni appropriate. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Testare accuratamente gli script**: Testate accuratamente gli script per assicurarvi che funzionino come previsto. È possibile utilizzare **Pester**, un framework di test per PowerShell, per scrivere ed eseguire test unitari per gli script. [Pester Documentation](https://pester.dev/)
- **Utilizzare funzioni e moduli**: Usare funzioni e moduli per organizzare il codice e migliorarne la riusabilità. Le funzioni consentono di suddividere il codice in parti più piccole e gestibili, mentre i moduli forniscono un modo per impacchettare e distribuire il codice. [About Functions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [About Modules](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Evitare la codifica dei valori**: Evitate di codificare i valori nello script e utilizzate invece parametri o variabili. Questo rende gli script più flessibili e riutilizzabili. È possibile passare parametri agli script utilizzando l'opzione `param` parola chiave. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Usa l'output verboso**: Utilizzare l'output verboso per fornire ulteriori informazioni sull'avanzamento dello script. È possibile utilizzare l'opzione `Write-Verbose` per visualizzare i messaggi verbosi durante l'esecuzione dello script. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

Seguire queste best practice vi aiuterà a scrivere script PowerShell più efficienti e manutenibili, migliorando la vostra produttività e garantendo la stabilità delle vostre attività di automazione.

### Elaborazione delle migliori pratiche per lo scripting PowerShell

#### Utilizzare la gestione degli errori
La gestione degli errori è un aspetto critico dello scripting PowerShell, in quanto garantisce che lo script gestisca con grazia errori ed eccezioni. PowerShell offre diversi modi per gestire gli errori, tra cui l'istruzione Try-Catch, l'istruzione Trap e il parametro ErrorAction. L'istruzione Try-Catch viene utilizzata per catturare e gestire le eccezioni, mentre l'istruzione Trap viene utilizzata per catturare e gestire gli errori. Il parametro ErrorAction viene utilizzato per controllare il modo in cui lo script gestisce gli errori.

Ecco un esempio di utilizzo dell'istruzione Try-Catch per gestire con grazia un errore:
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Script di test accurati

Testare gli script PowerShell è essenziale per garantire che funzionino come previsto. PowerShell offre diversi strumenti e framework di test, come Pester, che consentono agli utenti di scrivere ed eseguire test per i loro script. Questi strumenti aiutano a identificare e isolare i problemi nel codice e a garantire che lo script soddisfi i requisiti desiderati.

Ecco un esempio di utilizzo di Pester per testare uno script PowerShell:
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # some code that should return the expected result
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### Utilizzare funzioni e moduli
Le funzioni e i moduli sono essenziali per organizzare il codice e migliorare la riusabilità dello scripting PowerShell. Le funzioni consentono agli utenti di raggruppare il codice in blocchi riutilizzabili, mentre i moduli permettono agli utenti di impacchettare e condividere il codice con altri. Utilizzando funzioni e moduli, gli script PowerShell possono essere resi più modulari, efficienti e manutenibili.

Ecco un esempio di utilizzo di una funzione in PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "There are $count processes running."
```

#### Evitare la codifica rigida dei valori
La codifica rigida dei valori in uno script PowerShell lo rende meno flessibile e più difficile da mantenere. Invece di codificare i valori, è meglio utilizzare parametri o variabili, che consentono agli utenti di passare valori allo script in fase di esecuzione. Utilizzando parametri o variabili, lo script può essere reso più riutilizzabile e adattabile a condizioni mutevoli.

Ecco un esempio di utilizzo di un parametro in PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Utilizzare l'output Verbose
L'output verboso fornisce informazioni aggiuntive sull'avanzamento dello script, che possono essere utili per il debug e la risoluzione dei problemi. PowerShell mette a disposizione il cmdlet Write-Verbose, che consente di inviare informazioni verbose alla console. Utilizzando l'output verboso, gli script PowerShell possono essere resi più informativi e più facili da debuggare.

Ecco un esempio di utilizzo dell'output verboso in PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "There are $count processes running."
```

### Dieci idee di script PowerShell per principianti

Se siete principianti nello scripting PowerShell, ecco dieci idee di script per iniziare:

- **Backup automatizzati**: Create uno script che automatizzi il processo di backup di file e directory importanti su un disco rigido esterno o su un servizio di cloud storage. È possibile utilizzare la funzione `Copy-Item` per copiare i file e il comando `Start-Job` per eseguire il processo di backup in background. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Gestione dei file**: Creare uno script che organizzi i file e le directory ordinandoli in cartelle diverse in base al tipo di file, alle dimensioni o ad altri criteri. È possibile utilizzare l'opzione `Get-ChildItem` per recuperare i file e il cmdlet `Move-Item` per spostarli nella posizione desiderata. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informazioni sul sistema**: Creare uno script che recuperi le informazioni di sistema, come l'utilizzo della CPU e della memoria, lo spazio su disco e le impostazioni di rete, e le visualizzi in un formato di facile lettura. È possibile utilizzare l'opzione `Get-WmiObject` per raccogliere le informazioni di sistema e formattarle utilizzando `Format-Table` o `Out-GridView` [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gestione degli utenti**: Creare uno script che automatizzi il processo di aggiunta, modifica o eliminazione di utenti e gruppi nel sistema operativo Windows. È possibile utilizzare il file `New-LocalUser` `Set-LocalUser` e `Remove-LocalUser` per gestire gli utenti e i comandi `New-LocalGroup` `Add-LocalGroupMember` e `Remove-LocalGroup` per gestire i gruppi. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Installazione software**: Creare uno script che installi e configuri il software su più computer contemporaneamente, risparmiando tempo e fatica. È possibile utilizzare il file `Invoke-Command` per eseguire i comandi di installazione sui computer remoti. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Configurazione di rete**: Creare uno script che automatizzi il processo di configurazione delle impostazioni di rete, come indirizzo IP, maschera di sottorete e gateway predefinito. È possibile utilizzare il file `Set-NetIPAddress` `Set-NetIPInterface` e `Set-DnsClientServerAddress` per configurare le impostazioni di rete. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Sicurezza**: Creare uno script che verifichi e monitori le impostazioni di sicurezza e avvisi l'utente se vengono rilevate modifiche. È possibile utilizzare l'opzione `Get-AuditPolicy` per recuperare i criteri di audit e il file `Send-MailMessage` per inviare notifiche via e-mail. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Pianificazione delle attività**: Creare uno script che pianifichi e automatizzi le attività ricorrenti, come backup, aggiornamenti e scansioni del sistema. È possibile utilizzare l'opzione `Register-ScheduledTask` per creare attività pianificate e il comando `Start-ScheduledTask` per eseguirli. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Manipolazione del registro**: Creare uno script che modifichi o recuperi i valori del registro per chiavi o valori specifici. È possibile utilizzare l'opzione `Get-ItemProperty` e `Set-ItemProperty` per interagire con il registro. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Amministrazione remota**: Creare uno script che consenta l'amministrazione remota dei computer Windows, permettendo agli utenti di eseguire comandi e script sui computer remoti. È possibile utilizzare l'opzione `Enter-PSSession` o il comando `Invoke-Command` per eseguire comandi su computer remoti. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Iniziate a esplorare queste idee di script per acquisire esperienza pratica e ampliare le vostre competenze in PowerShell.

## Conclusione

PowerShell è un potente strumento per gestire e automatizzare il sistema operativo Windows e altre tecnologie Microsoft. In questo articolo abbiamo trattato le basi dello scripting PowerShell per i principianti, tra cui l'installazione e l'avvio di PowerShell, l'uso di cmdlet, variabili, loop, dichiarazioni condizionali e funzioni e l'uso di PowerShell ISE, PowerShell Remoting e dei moduli PowerShell. Seguendo le migliori pratiche, gli script PowerShell possono essere sicuri, affidabili e manutenibili. Con la pratica, è possibile diventare abili nello scripting PowerShell e automatizzare varie attività amministrative con facilità.
