---
title: "Automatizați OSINT cu modulele Shodan PowerShell"
date: 2020-11-14
---

O colecție de module PowerShell pentru interacțiunea cu API-ul Shodan

**Note:**
- Veți avea nevoie de cheia dvs. API Shodan, care poate fi găsită pe dvs[Shodan Account](https://account.shodan.io/)
- Exemple de API-uri utilizate în module pot fi găsite pe[Shodan Developers Page](https://developer.shodan.io/api)
- Anumite module pot utiliza credite de scanare sau de interogare. Creditele de interogare sunt folosite atunci când descărcați date prin intermediul site-ului web, CLI sau API (ceea ce fac aceste scripturi).
  Deoarece utilizăm API-ul, este important să rețineți că creditele de interogare sunt deduse dacă:
  1. Se folosește un filtru de căutare
  2. Pagina 2 sau mai departe este solicitată
      Creditele se reînnoiesc la începutul lunii și 1 credit vă permite să descărcați 100 de rezultate.
      În ceea ce privește creditele de scanare, 1 credit de scanare vă permite să scanați 1 IP și, de asemenea, se reînnoiesc la începutul lunii.
      Vă rugăm să consultați Centrul de ajutor Shodan[HERE](https://help.shodan.io/the-basics/credit-types-explained) pentru detalii complete.

## Cuprins
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Module**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Returnați informații despre planul API care aparține cheii API date.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Afișează anteturile HTTP pe care clientul dvs. le trimite atunci când se conectează la un server web.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Obține adresa IP actuală așa cum este văzută de pe Internet.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obține toate subdomeniile și alte intrări DNS pentru domeniul dat
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Caută numele de gazdă care au fost definite pentru lista dată de adrese IP.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Caută exploatări, dar returnează doar informații despre numărul total de potriviri legate de termenul de căutare și, opțional, autorul, platforma, portul, sursa sau tipul exploatării.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Returnează numărul total de rezultate oferite de „/shodan/host/search”.
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Căutați Shodan cu adresa IP.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Căutați Shodan folosind aceeași sintaxă de interogare ca site-ul web și folosiți fațete pentru a obține informații rezumate pentru diferite proprietăți.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Acest modul returnează o listă de filtre de căutare care pot fi utilizate în interogarea de căutare.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Acest modul returnează o listă de filtre de căutare care pot fi utilizate în interogarea de căutare.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Listați toate porturile pe care Shodan le accesează cu crawlere pe Internet.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Returnează informații despre contul Shodan conectat la această cheie API
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Verificați progresul unei cereri de scanare trimise anterior
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Listați toate protocoalele care pot fi utilizate atunci când se efectuează scanări de internet la cerere prin Shodan
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- Utilizați acest modul pentru a solicita lui Shodan să acceseze cu crawlere o rețea.<a name="Download"></a> ## Descărcare Va trebui să clonați sau să descărcați scripturile pe computer. Puteți folosi meniul drop-down Cod de pe această pagină repo derulând în sus sau pur și simplu copiați și lipiți următorul link:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Pentru acest exemplu, vom clona repo-ul în Git Bash, după ce facem clic pe pictograma clipboard așa cum se vede mai sus, putem tasta git clone și facem clic dreapta pe fereastra Git Bash pentru a selecta paste din meniul drop-down:

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

Acum puteți rula oricare dintre scripturi ca modul prin powershell.
