---
title: "Automatitzeu OSINT amb els mòduls Shodan PowerShell"
date: 2020-11-14
---

Una col·lecció de mòduls de PowerShell per interactuar amb l'API Shodan

**Notes:**
- Necessitareu la vostra clau de l'API Shodan, que es pot trobar al vostre[Shodan Account](https://account.shodan.io/)
- Es poden trobar exemples de les API utilitzades en els mòduls a[Shodan Developers Page](https://developer.shodan.io/api)
- Alguns mòduls poden utilitzar crèdits d'escaneig o consulta. Els crèdits de consulta s'utilitzen quan baixeu dades mitjançant el lloc web, la CLI o l'API (el que fan aquests scripts).
  Com que estem utilitzant l'API, és important tenir en compte que els crèdits de consulta es dedueixen si:
  1. S'utilitza un filtre de cerca
  2. Se sol·licita una pàgina 2 o més
      Els crèdits es renoven a principis de mes i 1 crèdit us permet descarregar 100 resultats.
      Pel que fa als crèdits d'escaneig, 1 crèdit d'escaneig us permet escanejar 1 IP, i també es renoven a principis de mes.
      Consulteu el Centre d'ajuda de Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) per a tots els detalls.

## Taula de continguts
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Mòduls**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Retorna informació sobre el pla d'API que pertany a la clau d'API donada.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Mostra les capçaleres HTTP que envia el vostre client quan es connecta a un servidor web.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Obté la vostra adreça IP actual tal com es veu des d'Internet.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obté tots els subdominis i altres entrades DNS per al domini donat
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Busca els noms d'amfitrió que s'han definit per a la llista donada d'adreces IP.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Cerca exploits, però només retorna informació sobre el nombre total de coincidències relacionades amb el terme de cerca i, opcionalment, l'autor, la plataforma, el port, la font o el tipus de l'explotació.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Retorna el nombre total de resultats de "/shodan/host/search" que proporciona.
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Cerca Shodan amb adreça IP.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Cerqueu Shodan utilitzant la mateixa sintaxi de consulta que el lloc web i utilitzeu facetes per obtenir informació resumida de diferents propietats.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Aquest mòdul retorna una llista de filtres de cerca que es poden utilitzar en la consulta de cerca.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Aquest mòdul retorna una llista de filtres de cerca que es poden utilitzar en la consulta de cerca.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Llista tots els ports que Shodan rastreja a Internet.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Retorna informació sobre el compte de Shodan enllaçat a aquesta clau de l'API
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Comproveu el progrés d'una sol·licitud d'escaneig enviada prèviament
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Llista tots els protocols que es poden utilitzar quan es realitzen exploracions d'Internet sota demanda mitjançant Shodan
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- Utilitzeu aquest mòdul per demanar a Shodan que rastregi una xarxa.<a name="Download"></a> ## Baixa Haureu de clonar o descarregar els scripts al vostre ordinador. Podeu utilitzar el menú desplegable Codi d&#39;aquesta pàgina de repo desplaçant-vos cap amunt, o simplement copieu i enganxeu l&#39;enllaç següent:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Per a aquest exemple, clonarem el repo dins de Git Bash, després de fer clic a la icona del porta-retalls tal com es veu més amunt, podem escriure git clone i fer clic amb el botó dret a la finestra de Git Bash per seleccionar enganxar al menú desplegable:

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

Ara podeu executar qualsevol dels scripts com a mòdul mitjançant Powershell.
