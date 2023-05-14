---
title: "Automatizza OSINT con i moduli Shodan PowerShell"
date: 2020-11-14
---

Una raccolta di moduli PowerShell per l'interazione con l'API Shodan

**Appunti:**
- Avrai bisogno della tua chiave API Shodan, che puoi trovare sul tuo[Shodan Account](https://account.shodan.io/)
- Esempi di API utilizzate nei moduli possono essere trovati su[Shodan Developers Page](https://developer.shodan.io/api)
- Alcuni moduli possono utilizzare crediti di scansione o interrogazione I crediti di interrogazione vengono utilizzati quando si scaricano dati tramite il sito Web, la CLI o l'API (cosa fanno questi script).
  Poiché utilizziamo l'API, è importante notare che i crediti di query vengono detratti se:
  1. Viene utilizzato un filtro di ricerca
  2. È richiesta la pagina 2 o successiva
      I crediti si rinnovano all'inizio del mese e 1 credito ti consente di scaricare 100 risultati.
      Per quanto riguarda i crediti di scansione, 1 credito di scansione ti consente di scansionare 1 IP e si rinnovano anche all'inizio del mese.
      Consulta il Centro assistenza Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) per tutti i dettagli.

## Sommario
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Moduli**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Restituisce informazioni sul piano API appartenente alla chiave API specificata.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Mostra le intestazioni HTTP che il tuo client invia quando si connette a un server web.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Ottiene il tuo attuale indirizzo IP visto da Internet.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Ottiene tutti i sottodomini e altre voci DNS per il dominio specificato
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Cerca i nomi host che sono stati definiti per l'elenco di indirizzi IP specificato.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Cerca gli exploit ma restituisce solo informazioni sul numero totale di corrispondenze relative al termine di ricerca e, facoltativamente, all'autore, alla piattaforma, alla porta, alla fonte o al tipo dell'exploit.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Restituisce il numero totale di risultati forniti da "/shodan/host/search".
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Cerca Shodan con l'indirizzo IP.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Cerca Shodan utilizzando la stessa sintassi di query del sito Web e utilizza i facet per ottenere informazioni di riepilogo per diverse proprietà.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Questo modulo restituisce un elenco di filtri di ricerca che possono essere utilizzati nella query di ricerca.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Questo modulo restituisce un elenco di filtri di ricerca che possono essere utilizzati nella query di ricerca.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Elenca tutte le porte che Shodan sta scansionando su Internet.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Restituisce informazioni sull'account Shodan collegato a questa chiave API
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Controllare lo stato di avanzamento di una richiesta di scansione inviata in precedenza
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Elenca tutti i protocolli che possono essere utilizzati durante l'esecuzione di scansioni Internet su richiesta tramite Shodan
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- Usa questo modulo per richiedere a Shodan di scansionare una rete.<a name="Download"></a> ## Download Dovrai clonare o scaricare gli script sul tuo computer. Puoi utilizzare il menu a discesa Codice in questa pagina del repository scorrendo verso l&#39;alto o semplicemente copiando e incollando il seguente link:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Per questo esempio cloneremo il repository all'interno di Git Bash, dopo aver fatto clic sull'icona degli appunti come visto sopra, possiamo digitare git clone e fare clic con il pulsante destro del mouse sulla finestra di Git Bash per selezionare incolla dal menu a discesa:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

For detailed instructions on cloning please view [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

You can use the Code dropdown menu on this repo page by scrolling up, or just click on the following link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Unzip main.zip by right clicking on the file and selecting extract here from the dropdown menu.

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Install"></a>

To install the modules You will need to run a PowerShell window as administrator.
There are two ways of doing this:

The first way is by right clicking the PowerShell icon on the Desktop and selecting Run as Administrator from the dropdown menu.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

By typing p (or however many characters it takes PowerShell to show up) into the search bar and clicking on Run as Administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

You will need to be in the directory that you copied the scripts to.
Run the following command to change your working directory:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

On Windows client computers we need to change the PowerShell execution policy which is Restricted by default.

For more information please read this [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Run the following command to set the policy to RemoteSigned and enter y to select that Yes you want to change the policy.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Once the execution policy has been changed, you can run the following command to Import the modules.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Ora puoi eseguire qualsiasi script come modulo tramite PowerShell.
