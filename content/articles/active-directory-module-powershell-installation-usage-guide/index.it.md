---
title: "Padroneggiare l'amministrazione di Active Directory con PowerShell: Guida all'installazione e all'uso"
date: 2023-07-25
toc: true
draft: false
description: "Scoprite come installare e utilizzare efficacemente il modulo Active Directory per PowerShell per semplificare le attività di amministrazione di Windows Active Directory."
genre: ["Tecnologia", "Finestre", "PowerShell", "Active Directory", "Amministrazione", "Scripting", "IT", "Automazione", "Server Windows", "Microsoft"]
tags: ["modulo Active Directory per PowerShell", "importare il modulo active directory in PowerShell", "modulo Active Directory per Windows PowerShell", "directory attiva Installazione di PowerShell", "installare la directory attiva PowerShell", "PowerShell installare modulo directory attiva Windows 10", "installare directory attiva Modulo PowerShell Windows 10", "ottenere il modulo PowerShell della directory attiva", "Amministrazione AD", "Windows Active Directory", "I cmdlet di PowerShell", "recuperare le informazioni su AD", "creare oggetti AD", "modificare gli oggetti AD", "gestire la sicurezza di AD", "Gestione utenti AD", "Gestione dei gruppi AD", "Gestione delle sale operatorie", "Scripting PowerShell", "Amministrazione di Windows Server", "Microsoft PowerShell", "automatizzare le attività di AD", "Installazione del modulo PowerShell", "Guida all'amministrazione AD", "Gestione di Active Directory", "Gestione della sicurezza AD", "Automazione PowerShell", "Comandi PowerShell di Active Directory", "Riferimento al cmdlet PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "Un'immagine che raffigura una rete di server interconnessi e icone di utenti, che simboleggia la gestione e l'automazione di Active Directory."
coverCaption: "Sbloccare la potenza dell'amministrazione di Active Directory con PowerShell."
---

## Introduzione

Nell'attuale panorama digitale, la gestione e la manutenzione degli account utente, dei gruppi di sicurezza e di altre risorse in un ambiente Windows Active Directory (AD) richiede processi efficienti e semplificati. PowerShell, un potente linguaggio di scripting sviluppato da Microsoft, offre il modulo **Active Directory** per facilitare le attività di amministrazione di AD. Questo modulo fornisce un'ampia gamma di cmdlet che consentono agli amministratori di automatizzare varie operazioni e gestire AD in modo efficace. In questo articolo esploreremo l'installazione e l'utilizzo del modulo Active Directory per PowerShell.

## Installazione del modulo Active Directory per PowerShell

Per iniziare a usare il modulo Active Directory per PowerShell, è necessario assicurarsi che sia installato sul sistema. Il processo di installazione può variare a seconda del sistema operativo in uso. Di seguito sono riportati i passaggi per l'installazione del modulo su **Windows 10**, **Windows 11** e **Windows Server**:

### Windows 10 e Windows 11 - PowerShell
1. Aprire **Windows PowerShell** con privilegi amministrativi.
2. Eseguite il seguente comando per installare il modulo:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Attendere il completamento dell'installazione. Al termine, è possibile iniziare a utilizzare il modulo Active Directory.

### Windows Server
1. Aprite **Windows PowerShell** con privilegi amministrativi.
2. Eseguite il seguente comando per installare il modulo:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Attendere il completamento dell'installazione. Al termine, è possibile iniziare a utilizzare il modulo Active Directory.

### Sistemi offline

I sistemi offline sono un po' più complicati. Esistono diversi metodi, ma quello consigliato è l'uso del seguente script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importazione del modulo Active Directory in PowerShell

Prima di poter utilizzare il modulo Active Directory in PowerShell, è necessario importarlo nella sessione corrente. Seguite questi passaggi per importare il modulo:

1. Avviate **Windows PowerShell** con diritti amministrativi.
2. Eseguite il seguente comando per importare il modulo:

```powershell
Import-Module ActiveDirectory
```

3. Il modulo Active Directory viene importato ed è ora possibile accedere alle sue cmdlet e funzioni.

## Utilizzo del modulo Active Directory per PowerShell

Una volta importato il modulo Active Directory, è possibile sfruttare il suo ricco set di cmdlet per eseguire diverse attività amministrative. Esploriamo alcuni cmdlet comunemente usati e le loro funzionalità:

### Recupero di informazioni su Active Directory

Per gestire efficacemente un ambiente Active Directory (AD), è fondamentale recuperare informazioni su vari oggetti AD, come utenti, gruppi e unità organizzative (UO). PowerShell offre potenti cmdlet che semplificano il processo di recupero.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Questo cmdlet consente di recuperare informazioni dettagliate sugli utenti AD. È possibile ottenere attributi come nome utente, nome visualizzato, indirizzo e-mail e altro ancora. Ad esempio, per recuperare tutti gli utenti il cui nome utente inizia con "johndoe", è possibile eseguire il seguente comando:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Questo comando restituisce un elenco di oggetti utente che corrispondono al filtro specificato.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Con il cmdlet Get-ADGroup è possibile ottenere informazioni sui gruppi AD. Fornisce l'accesso a dettagli quali il nome del gruppo, i membri, la descrizione e altro ancora. Ad esempio, per recuperare tutti i gruppi di sicurezza nell'ambiente AD, è possibile eseguire il seguente comando:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Questo fornirà un elenco di gruppi di sicurezza in Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) Il cmdlet Get-ADOrganizationalUnit è utilizzato per recuperare informazioni sulle UO di AD. Consente di accedere a proprietà come il nome dell'OU, la descrizione, l'OU padre e altro ancora. Per recuperare tutte le OU nel dominio, è possibile utilizzare il seguente comando:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  L'esecuzione di questo comando visualizza un elenco di tutte le UO di Active Directory.

Utilizzando queste potenti cmdlet, è possibile recuperare facilmente informazioni specifiche su utenti, gruppi e OU di AD, consentendo un'amministrazione e una gestione efficienti dell'ambiente Active Directory.


Queste cmdlet consentono di recuperare attributi specifici, filtrare i risultati ed eseguire query avanzate per ottenere le informazioni desiderate.

### Creazione e gestione degli oggetti di Active Directory

Quando si lavora con Active Directory (AD), il modulo Active Directory di PowerShell offre potenti cmdlet per creare e gestire oggetti AD. Esploriamo alcuni cmdlet essenziali per la creazione di utenti, gruppi e unità organizzative (UO) di AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Questo cmdlet consente di creare un nuovo utente AD. È possibile specificare attributi quali nome utente, password, indirizzo e-mail e altro. Ad esempio, per creare un nuovo utente con il nome utente "john.doe" e il nome visualizzato "John Doe", è possibile utilizzare il seguente comando:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Questo comando crea un nuovo utente in Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) Il cmdlet New-ADGroup consente di creare un nuovo gruppo AD. È possibile impostare proprietà come il nome del gruppo, la descrizione, l'ambito del gruppo e altro ancora. Per creare un nuovo gruppo denominato "Marketing" con una descrizione, è possibile eseguire il seguente comando:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Questo comando crea un nuovo gruppo in Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Con il cmdlet New-ADOrganizationalUnit è possibile creare una nuova OU AD. È possibile specificare proprietà come il nome dell'OU, l'OU padre e altro ancora. Ad esempio, per creare una nuova OU denominata "Vendite" sotto l'OU "Reparti", è possibile eseguire il seguente comando:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Questo comando crea una nuova OU nella gerarchia di Active Directory.

Sfruttando queste cmdlet, è possibile creare facilmente nuovi utenti, gruppi e OU di AD con le proprietà e le configurazioni desiderate, consentendo una gestione efficiente dell'ambiente Active Directory.


### Modifica degli oggetti di Active Directory

Quando si tratta di modificare le proprietà e gli attributi degli oggetti Active Directory (AD) esistenti, il modulo Active Directory di PowerShell fornisce diversi cmdlet utili. Esploriamo queste cmdlet per modificare utenti, gruppi e unità organizzative (UO) di AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) Il cmdlet Set-ADUser consente di modificare le proprietà di un utente AD. È possibile aggiornare attributi quali il nome visualizzato, l'indirizzo e-mail, il numero di telefono e altro ancora. Ad esempio, per modificare il numero di telefono di un utente con il nome utente "john.doe", è possibile utilizzare il seguente comando:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Questo comando modifica il numero di telefono dell'utente specificato in Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Con il cmdlet Set-ADGroup è possibile modificare le proprietà di un gruppo AD. È possibile aggiornare attributi come la descrizione del gruppo, l'appartenenza, l'ambito del gruppo e altro ancora. Per modificare la descrizione di un gruppo denominato "Marketing" in "Marketing Team", è possibile eseguire il seguente comando:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Questo comando aggiorna la descrizione del gruppo specificato in Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) Il cmdlet Set-ADOrganizationalUnit consente di modificare le proprietà di una OU AD. È possibile modificare attributi come il nome dell'OU, la descrizione e altro ancora. Ad esempio, per modificare la descrizione di una OU denominata "Vendite" in "Reparto vendite", è possibile eseguire il seguente comando:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Questo comando aggiorna la descrizione della OU specificata nella gerarchia di Active Directory.

Utilizzando queste cmdlet, è possibile modificare facilmente le proprietà e gli attributi degli oggetti AD, apportando gli aggiornamenti e le regolazioni necessarie per soddisfare i requisiti dell'organizzazione.


### Gestione della sicurezza di Active Directory

Oltre alla gestione e all'amministrazione degli oggetti di Active Directory (AD), il modulo Active Directory di PowerShell fornisce cmdlets specificamente progettati per gestire gli aspetti di sicurezza di AD. Questi cmdlet consentono agli amministratori di gestire in modo efficiente l'accesso degli utenti, l'appartenenza ai gruppi e le attività relative alle password nell'ambiente AD.

Ecco alcuni cmdlet comunemente utilizzati per la sicurezza:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Questo cmdlet consente di aggiungere membri a un gruppo AD. Specificando il gruppo AD e gli account utente o i gruppi che si desidera aggiungere, è possibile gestire facilmente il controllo degli accessi. Ad esempio, per aggiungere un utente chiamato "JohnDoe" al gruppo "Manager", è possibile utilizzare il seguente comando:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Con questo cmdlet è possibile rimuovere i membri da un gruppo AD. Specificando il gruppo AD e gli account utente o i gruppi che si desidera rimuovere, è possibile gestire efficacemente le appartenenze ai gruppi. Ad esempio, per rimuovere un utente chiamato "JaneSmith" dal gruppo "Developers", è possibile utilizzare il seguente comando:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Questo cmdlet consente di impostare la password di un utente AD. Specificando l'account utente e fornendo una nuova password, è possibile applicare i criteri di password e garantire l'autenticazione sicura degli utenti. Ecco un esempio di impostazione di una nuova password per un utente chiamato "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Utilizzando queste cmdlet relative alla sicurezza, gli amministratori possono gestire efficacemente l'accesso degli utenti, le appartenenze ai gruppi e i criteri delle password all'interno dell'ambiente Active Directory.

## Esempio di script del modulo Active Directory per PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Conclusione

In conclusione, il modulo **Active Directory per PowerShell** è un potente strumento che consente una gestione efficiente e conveniente di Windows Active Directory. Installando e importando il modulo, si accede a una serie completa di **cmdlets** che semplificano varie attività legate ad AD.

Con il modulo Active Directory è possibile eseguire un'ampia gamma di operazioni, come il recupero di informazioni sugli oggetti AD, la creazione di nuovi oggetti, la modifica delle proprietà e la gestione della sicurezza. Questo modulo consente agli amministratori di automatizzare le attività amministrative, di semplificare i flussi di lavoro e di garantire il buon funzionamento degli ambienti Active Directory.

Sfruttando **PowerShell** e il modulo **Active Directory**, è possibile potenziare le capacità di amministrazione di AD e migliorare l'efficienza dei processi di gestione di AD. Che siate amministratori di sistema, professionisti IT o manager di Active Directory, il modulo Active Directory vi fornisce gli strumenti necessari per gestire efficacemente la vostra infrastruttura AD.

Sfruttate la potenza di **PowerShell** e del modulo **Active Directory** per semplificare le vostre attività di amministrazione AD, aumentare la produttività e mantenere un ambiente Active Directory sicuro e ben organizzato.

## Riferimenti

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)
