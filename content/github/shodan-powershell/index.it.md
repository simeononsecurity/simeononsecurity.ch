---
title: "Automatizzare OSINT con i moduli PowerShell di Shodan"
date: 2020-11-14
---

Una raccolta di moduli PowerShell per l'interazione con l'API di Shodan

> **Note:**
- È necessario disporre della chiave API di Shodan, che può essere trovata nella cartella [Shodan Account](https://account.shodan.io/)
- Esempi delle API utilizzate nei moduli possono essere consultati sul sito web [Shodan Developers Page](https://developer.shodan.io/api)
- Alcuni moduli possono utilizzare crediti di scansione o di query I crediti di query vengono utilizzati quando si scaricano i dati tramite il sito web, la CLI o l'API (ciò che fanno questi script).
  Poiché si utilizza l'API, è importante notare che i crediti di interrogazione vengono detratti se:
  1.  Viene utilizzato un filtro di ricerca
  2.  Viene richiesta la pagina 2 o oltre
      I crediti si rinnovano all'inizio del mese e 1 credito consente di scaricare 100 risultati.
      Per quanto riguarda i crediti di scansione, 1 credito di scansione consente di scansionare 1 IP e anch'essi si rinnovano all'inizio del mese.
      Si prega di consultare il Centro assistenza Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) per tutti i dettagli.

## Indice dei contenuti
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Moduli**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Restituisce informazioni sul piano API appartenente alla chiave API indicata.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Mostra le intestazioni HTTP che il client invia quando si connette a un server web.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Ottiene l'indirizzo IP corrente visto da Internet.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Ottiene tutti i sottodomini e le altre voci DNS per il dominio indicato.
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Cerca i nomi di host definiti per l'elenco di indirizzi IP indicato.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Cerca gli exploit, ma restituisce solo informazioni sul numero totale di corrispondenze relative al termine di ricerca e, facoltativamente, l'autore dell'exploit, la piattaforma, la porta, la fonte o il tipo.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Restituisce il numero totale di risultati di "/shodan/host/search".
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Cerca su Shodan con l'indirizzo IP.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Cercare su Shodan utilizzando la stessa sintassi di interrogazione del sito web e utilizzare le faccette per ottenere informazioni sintetiche su diverse proprietà.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Questo modulo restituisce un elenco di filtri di ricerca che possono essere utilizzati nella query di ricerca.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Questo modulo restituisce un elenco di filtri di ricerca che possono essere utilizzati nella query di ricerca.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Elenca tutte le porte che Shodan sta cercando su Internet.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Restituisce informazioni sull'account Shodan collegato a questa chiave API.
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Controllare l'avanzamento di una richiesta di scansione precedentemente inviata
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Elencare tutti i protocolli che possono essere utilizzati quando si eseguono scansioni Internet on-demand tramite Shodan.
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Utilizzare questo modulo per richiedere a Shodan di eseguire il crawling di una rete.

<a name="Scarica"></a>

## Scaricare

È necessario clonare o scaricare gli script sul proprio computer.

È possibile utilizzare il menu a discesa Codice su questa pagina repo, scorrendo verso l'alto, oppure copiare e incollare il seguente link: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Per questo esempio, cloneremo il repo all'interno di Git Bash; dopo aver fatto clic sull'icona degli appunti, come visto sopra, possiamo digitare git clone e fare clic con il pulsante destro del mouse sulla finestra di Git Bash per selezionare incolla dal menu a discesa:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Per istruzioni dettagliate sulla clonazione, vedere [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Una volta ottenuti i file, è necessario copiarli in C:\Program Files\WindowsPowerShell\Modules, in questo modo verrà visualizzata una finestra di dialogo che indica che l'accesso è negato; fare clic su continua per terminare la copia dei file in questa posizione e quindi procedere con le istruzioni di installazione. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**O...

È possibile utilizzare il menu a discesa Codice su questa pagina repo scorrendo verso l'alto, oppure fare semplicemente clic sul seguente link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Decomprimere main.zip facendo clic con il pulsante destro del mouse sul file e selezionando estrai qui dal menu a discesa.

Una volta ottenuti i file, è necessario copiarli in C:\Program Files\WindowsPowerShell\Modules, in questo modo verrà visualizzata una finestra di dialogo che indica che l'accesso è negato; fare clic su continua per terminare la copia dei file in questa posizione e quindi procedere con le istruzioni di installazione. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

## Installa

<a nome="Installa"></a>

Per installare i moduli è necessario eseguire una finestra PowerShell come amministratore.
Esistono due modi per farlo:

Il primo consiste nel fare clic con il tasto destro del mouse sull'icona PowerShell sul desktop e selezionare Esegui come amministratore dal menu a discesa.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**O...

Digitando p (o il numero di caratteri necessari a PowerShell per apparire) nella barra di ricerca e facendo clic su Esegui come amministratore.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

È necessario trovarsi nella directory in cui sono stati copiati gli script.
Eseguite il seguente comando per cambiare la directory di lavoro:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Nei computer client Windows è necessario modificare il criterio di esecuzione di PowerShell, che per impostazione predefinita è Limitato.

Per ulteriori informazioni, leggete questo [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Eseguire il seguente comando per impostare il criterio su RemoteSigned e immettere y per selezionare Sì, se si desidera modificare il criterio.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Una volta modificato il criterio di esecuzione, è possibile eseguire il seguente comando per importare i moduli.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Ora è possibile eseguire qualsiasi script come modulo tramite powershell.
