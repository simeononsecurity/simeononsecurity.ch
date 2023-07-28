---
title: "Automatizați OSINT cu modulele Shodan PowerShell"
date: 2020-11-14
---

O colecție de module PowerShell pentru interacțiunea cu API-ul Shodan

**Note:**
- Veți avea nevoie de cheia API Shodan, care poate fi găsită pe contul dvs. [Shodan Account](https://account.shodan.io/)
- Exemple de API-uri utilizate în module pot fi găsite pe site-ul [Shodan Developers Page](https://developer.shodan.io/api)
- Anumite module pot utiliza credite de scanare sau de interogare Creditele de interogare sunt utilizate atunci când descărcați date prin intermediul site-ului web, CLI sau API (ceea ce fac aceste scripturi).
  Deoarece folosim API, este important să rețineți că creditele de interogare sunt deduse dacă:
  1.  Se utilizează un filtru de căutare
  2.  Se solicită pagina 2 sau mai mult
      Creditele se reînnoiesc la începutul lunii, iar 1 credit vă permite să descărcați 100 de rezultate.
      În ceea ce privește creditele de scanare, 1 credit de scanare vă permite să scanați 1 IP, iar acestea se reînnoiesc, de asemenea, la începutul lunii.
      Vă rugăm să consultați Centrul de asistență Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) pentru detalii complete.

## Cuprins
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Module**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Returnează informații despre planul API care aparține cheii API date.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Afișează anteturile HTTP pe care le trimite clientul dvs. atunci când se conectează la un server web.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Obține adresa IP actuală, așa cum este văzută de pe internet.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obține toate subdomeniile și alte intrări DNS pentru domeniul dat
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Caută numele de gazdă care au fost definite pentru lista de adrese IP dată.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Caută exploatări, dar returnează numai informații despre numărul total de rezultate legate de termenul de căutare și, opțional, autorul, platforma, portul, sursa sau tipul exploatării.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Returnează numărul total de rezultate pe care le oferă "/shodan/host/search".
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Căutați Shodan cu adresa IP.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Căutați în Shodan folosind aceeași sintaxă de interogare ca și pe site-ul web și utilizați fațete pentru a obține informații sumare pentru diferite proprietăți.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Acest modul returnează o listă de filtre de căutare care pot fi utilizate în interogarea de căutare.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Acest modul returnează o listă de filtre de căutare care pot fi utilizate în interogarea de căutare.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Enumerați toate porturile pe care Shodan le accesează pe Internet.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Returnează informații despre contul Shodan legat de această cheie API
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Verificarea progresului unei cereri de scanare depuse anterior
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Enumerați toate protocoalele care pot fi utilizate atunci când se efectuează scanări la cerere pe Internet prin Shodan
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Utilizați acest modul pentru a solicita Shodan să cerceteze o rețea.

<a name="Download"></a>

## Download

Va trebui să clonați sau să descărcați scripturile pe calculatorul dumneavoastră.

Puteți folosi meniul derulant Code (Cod) de pe această pagină repo, derulând în sus, sau puteți copia și lipi următorul link: [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Pentru acest exemplu vom clona repo-ul în Git Bash, după ce facem clic pe pictograma clipboard, așa cum se vede mai sus, putem tasta git clone și facem clic dreapta pe fereastra Git Bash pentru a selecta paste din meniul derulant:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Pentru instrucțiuni detaliate privind clonarea, vă rugăm să consultați [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Odată ce aveți fișierele, trebuie să copiați fișierele în C:\Program Files\WindowsPowerShell\Modules, făcând acest lucru va apărea un dialog care va spune că accesul este refuzat, faceți clic pe Continue pentru a termina copierea fișierelor în această locație și apoi treceți la instrucțiunile de instalare. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Puteți utiliza meniul derulant Code de pe această pagină repo, derulând în sus, sau pur și simplu faceți clic pe următorul link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Descompuneți main.zip făcând clic dreapta pe fișier și selectând extrageți aici din meniul derulant.

După ce ați obținut fișierele, trebuie să le copiați în C:\Program Files\WindowsPowerShell\Modules, dacă faceți acest lucru, se va afișa o fereastră de dialog care va spune că accesul este refuzat, faceți clic pe Continue pentru a termina copierea fișierelor în această locație și apoi treceți la instrucțiunile de instalare. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Instalați

<a name="Install"></a>

Pentru a instala modulele Va trebui să rulați o fereastră PowerShell ca administrator.
Există două modalități de a face acest lucru:

Prima modalitate este făcând clic dreapta pe pictograma PowerShell de pe desktop și selectând Run as Administrator din meniul derulant.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Tastând p (sau oricâte caractere îi trebuie lui PowerShell pentru a apărea) în bara de căutare și făcând clic pe Execută ca administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Va trebui să vă aflați în directorul în care ați copiat scripturile.
Rulați următoarea comandă pentru a schimba directorul de lucru:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Pe computerele client Windows trebuie să modificăm politica de execuție PowerShell, care este restricționată în mod implicit.

Pentru mai multe informații, vă rugăm să citiți următoarele [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Rulați următoarea comandă pentru a seta politica la RemoteSigned și introduceți y pentru a selecta că da, doriți să modificați politica.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

După ce politica de execuție a fost modificată, puteți rula următoarea comandă pentru a importa modulele.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Acum puteți rula oricare dintre scripturi ca un modul prin intermediul powershell.
