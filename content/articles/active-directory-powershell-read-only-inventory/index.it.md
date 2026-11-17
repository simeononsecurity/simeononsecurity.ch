---
title: "Creare un inventario di Active Directory in sola lettura con PowerShell"
date: 2026-10-10
lastmod: 2026-11-07
toc: true
draft: false
description: "Inventaria le OU, gli utenti e i computer di Active Directory con query PowerShell circoscritte. Esporta file CSV verificabili senza modificare gli oggetti della directory."
genre: ["Active Directory", "PowerShell", "System Administration"]
tags: ["inventario Active Directory", "inventario AD PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "base di ricerca", "AD in sola lettura", "esportazione utenti AD", "esportazione computer AD", "esportazione OU AD", "Export-Csv", "RSAT", "audit della directory", "report AD", "inventario OU", "Windows Server", "script PowerShell", "modulo AD", "igiene della directory"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Un albero di Active Directory con record di utenti, computer e unità organizzative che confluiscono in tre file da esaminare."
coverCaption: "Definisci l'ambito della query, poi esporta solo i campi necessari per l'analisi."
---

La pulizia di Active Directory inizia da un elenco affidabile degli oggetti esistenti. Questo **inventario in sola lettura** raccoglie unità organizzative, utenti e computer da un unico ambito scelto. Esporta tre file CSV, cioè con valori separati da virgole, da esaminare senza modificare gli oggetti della directory. Proteggi questi file, perché i nomi e i dettagli dei dispositivi rivelano parte del tuo ambiente.

<!--more-->

## Punti chiave

- **Scegli un ambito:** Interroga una sola unità organizzativa prima di estendere la query a tutto il dominio.
- **Usa comandi di lettura:** `Get-ADOrganizationalUnit`, `Get-ADUser` e `Get-ADComputer` recuperano gli oggetti.
- **Seleziona i campi:** Esporta solo le proprietà necessarie per l'attività.
- **Controlla l'output:** Confronta il numero di record e alcune righe di esempio prima di affidarti al report.

## Prima di iniziare

Ti serve un host di amministrazione Windows con DNS funzionante e accesso di rete a un controller di dominio, il modulo PowerShell **ActiveDirectory**, un account autorizzato a leggere gli oggetti selezionati e una cartella protetta per l'output CSV. Su un client Windows, il modulo è incluso negli strumenti Active Directory di Remote Server Administration Tools (RSAT). La [guida al modulo Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) del sito descrive l'installazione. Microsoft fornisce il [riferimento dei cmdlet](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) del modulo e le [opzioni di installazione di RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Questa guida usa la sintassi di Windows PowerShell e non modifica gli oggetti della directory.

Le autorizzazioni della directory restano valide. Nelle indicazioni sugli [account privilegiati](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), Microsoft spiega che gli elenchi di controllo degli accessi agli oggetti spesso consentono agli utenti autenticati di leggere le informazioni generali, limitando però i campi sensibili e le modifiche. Inizia con un account autorizzato e una OU di test. Non elevare i privilegi a Domain Admin per far funzionare l'inventario.

> **Avviso:** I file CSV contengono nomi di account e computer. Salvali in una posizione approvata, limita l'accesso ed elimina le copie aggiuntive dopo l'analisi. Non pubblicare un'esportazione grezza e non allegarla a una segnalazione pubblica.

## Scegli la base di ricerca

Un'**unità organizzativa (OU)** raggruppa gli oggetti della directory. Il suo **distinguished name (DN)** ne indica la posizione nell'albero della directory. Il parametro `-SearchBase` limita una query al DN scelto. Senza un ambito preciso, un filtro ampio potrebbe restituire molti più oggetti di quelli necessari.

Per prima cosa, carica il modulo e visualizza il DN del dominio corrente:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documenta [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) e l'output relativo al dominio. Prima di impostare la base di ricerca, individua l'OU da esaminare:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copia il DN esatto dal risultato. Negli esempi successivi, sostituisci questo valore dimostrativo con il DN della tua OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` è un dominio riservato alla documentazione. Non copiare il suo DN in una query attiva. Se ti serve intenzionalmente un inventario dell'intero dominio, imposta `$SearchBase` sul DN del dominio e annota l'ambito più ampio nel report. Il [riferimento di Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) di Microsoft documenta `-Filter` e `-SearchBase`.

## Inventaria OU, utenti e computer

Inizia contando gli oggetti. È un modo rapido per individuare una base di ricerca errata o un risultato vuoto inatteso:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` indica tutti gli oggetti corrispondenti nella base di ricerca. Microsoft descrive [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) e [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) come comandi di recupero. Un conteggio pari a zero potrebbe essere legittimo, ma controlla il DN, le autorizzazioni e il dominio di destinazione prima di considerare completo l'inventario.

Ora visualizza alcune righe nella console. Memorizza i campi selezionati, così l'anteprima e la successiva esportazione CSV useranno le stesse colonne:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Per i computer, richiedi il campo aggiuntivo del sistema operativo solo se serve all'analisi:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Il parametro `-Properties` richiede proprietà che non fanno parte dell'insieme predefinito del cmdlet. La [documentazione del cmdlet per i computer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) di Microsoft descrive il parametro. Considera i nomi dei sistemi operativi come dati di directory, non come prova della versione attualmente installata. Un oggetto computer potrebbe essere obsoleto oppure il suo attributo potrebbe non essere stato aggiornato.

## Esporta un CSV verificabile

Scegli una cartella di output approvata con spazio sufficiente. I comandi seguenti scrivono **file CSV locali** e non modificano gli oggetti della directory. Eseguili in quella cartella. `-NoClobber` impedisce di sovrascrivere un file esistente. Per ogni esecuzione usa una nuova cartella o un nuovo nome file.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Il [riferimento di Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) di Microsoft spiega `-NoTypeInformation`, `-Encoding` e `-NoClobber`. Apri ogni CSV in un editor di testo o in un foglio di calcolo approvato. Controlla l'intestazione, alcune righe e il numero di record rispetto ai conteggi precedenti. Un comando non riuscito o un file da zero byte non dimostra che il report sia completo.

> **Risultato previsto:** Hai tre file CSV circoscritti con record di OU, utenti e computer. Il numero di righe e i record di esempio corrispondono all'ambito scelto.

## Esamina senza modificare gli oggetti

Usa l'inventario per rispondere a domande specifiche: quale OU contiene un computer? Quali utenti sono disabilitati? Quali dispositivi hanno bisogno di un proprietario? Registra i risultati in una nota di revisione separata. Non dedurre dal valore `Enabled` se un account sia ancora necessario. Non eliminare né disabilitare un oggetto basandoti solo su un'esportazione.

Per un report ricorrente, annota la data della query, il dominio, il DN dell'OU, le proprietà selezionate, l'operatore e la posizione del CSV. Quando confronti due esportazioni, verifica che usino lo stesso ambito e gli stessi campi. Altrimenti la differenza potrebbe dipendere dalla query anziché da un cambiamento nella directory.

Questo è un **inventario**, non un audit degli account privilegiati né un report delle attività di accesso. Microsoft osserva che le proprietà e le autorizzazioni di Active Directory variano in base all'oggetto e all'ambiente. Prima di agire, verifica con il proprietario del sistema un attributo del sistema operativo o un nome visualizzato. La [guida alla sicurezza di Active Directory](/articles/active-directory-security-best-practices/) del sito illustra i controlli di sicurezza più ampi.

## Risoluzione dei problemi

- **Impossibile importare il modulo:** Verifica che sull'host siano installati gli strumenti Active Directory di RSAT o gli strumenti di amministrazione di Windows Server. Segui la [guida di installazione del modulo](/articles/active-directory-module-powershell-installation-usage-guide/).
- **La query non restituisce oggetti:** Controlla il DN esatto, il dominio corrente, il contenuto dell'OU e le autorizzazioni di lettura. Prova una OU piccola e nota prima di ampliare l'ambito.
- **Una proprietà è vuota:** Verifica che l'attributo esista e che il tuo account possa leggerlo. Non inventare i valori mancanti.
- **L'esportazione segnala che il file esiste:** `-NoClobber` ha protetto il report precedente. Scegli un nuovo nome file o una nuova cartella e ripeti l'esecuzione.
- **I conteggi differiscono dalle attese:** Controlla se utenti o computer si trovano in un'altra OU, se l'ambito è cambiato e se la directory è stata modificata durante la query.

## Passaggi successivi

Conserva il CSV grezzo in una posizione protetta per il periodo di revisione concordato. Condividi solo i campi necessari al revisore. Dopo che i responsabili hanno verificato i risultati, pianifica le modifiche seguendo il normale processo di approvazione e ripristino. Dopo le modifiche approvate, ripeti l'inventario con lo stesso ambito per confermare il risultato.
