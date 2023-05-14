---
title: "OSINT automatiseren met Shodan PowerShell-modules"
date: 2020-11-14
---

Een verzameling PowerShell-modules voor interactie met de Shodan API

**Noten:**
- Je hebt je Shodan API sleutel nodig, die je kunt vinden op je[Shodan Account](https://account.shodan.io/)
- Voorbeelden van de in de modules gebruikte API's zijn te vinden op de[Shodan Developers Page](https://developer.shodan.io/api)
- Bepaalde modules kunnen scan- of querycredits gebruiken Querycredits worden gebruikt wanneer u gegevens downloadt via de website, CLI of API (wat deze scripts doen).
  Aangezien wij de API gebruiken, is het belangrijk op te merken dat query credits worden afgetrokken als:
  1.  Een zoekfilter wordt gebruikt
  2.  Pagina 2 of verder wordt opgevraagd
      De credits worden aan het begin van de maand vernieuwd en met 1 credit kunt u 100 resultaten downloaden.
      Met 1 scankrediet kunt u 1 IP scannen en ook deze worden aan het begin van de maand vernieuwd.
      Bekijk het Shodan Helpcentrum[HERE](https://help.shodan.io/the-basics/credit-types-explained) voor alle details.

## Inhoudsopgave
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Modules**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Geeft informatie over het API-plan dat bij de gegeven API-sleutel hoort.
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Toont de HTTP-headers die uw cliënt verstuurt wanneer hij verbinding maakt met een webserver.
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Geeft uw huidige IP-adres zoals gezien vanaf het internet.
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Krijgt alle subdomeinen en andere DNS-vermeldingen voor het opgegeven domein.
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Zoekt de hostnamen op die zijn gedefinieerd voor de gegeven lijst met IP-adressen.
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Zoekt naar exploits, maar geeft alleen informatie over het totale aantal overeenkomsten met betrekking tot de zoekterm, en optioneel de exploit-auteur, het platform, de poort, de bron of het type.
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Geeft het totale aantal resultaten van "/shodan/host/search".
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Zoek Shodan met IP-adres.
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Doorzoek Shodan met dezelfde zoeksyntaxis als de website en gebruik facetten om samenvattende informatie te krijgen voor verschillende eigenschappen.
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Deze module geeft een lijst van zoekfilters die in de zoekopdracht kunnen worden gebruikt.
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Deze module geeft een lijst van zoekfilters die in de zoekopdracht kunnen worden gebruikt.
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Lijst van alle poorten die Shodan crawlt op het internet.
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Geeft informatie over de Shodan account gekoppeld aan deze API sleutel.
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - De voortgang van een eerder ingediend scanverzoek controleren
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Lijst van alle protocollen die kunnen worden gebruikt bij het uitvoeren van on-demand internetscans via Shodan
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Gebruik deze module om Shodan te vragen een netwerk te crawlen.

<a name="Download"></a>

## Downloaden

U moet de scripts klonen of downloaden naar uw computer.

U kunt het Code dropdown menu op deze repo pagina gebruiken door naar boven te scrollen, of gewoon de volgende link kopiëren en plakken:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Voor dit voorbeeld zullen we de repo klonen binnen Git Bash, na het klikken op het klembord icoontje zoals hierboven te zien is, kunnen we git clone typen en rechts klikken in het Git Bash venster om plakken te selecteren uit het dropdown menu:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Voor gedetailleerde instructies over het klonen zie[the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Als je de bestanden eenmaal hebt, moet je ze kopiëren naar C:\Program Files\WindowsPowerShell\Modules, als je dit doet krijg je de melding dat de toegang is geweigerd, klik op doorgaan om de bestanden naar deze locatie te kopiëren en ga dan verder met de installatie instructies.[here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

U kunt het Code dropdown menu op deze repo pagina gebruiken door naar boven te scrollen, of klik gewoon op de volgende link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Unzip main.zip door rechts te klikken op het bestand en hier uitpakken te selecteren in het dropdown menu.

Zodra je de bestanden hebt, moet je ze kopiëren naar C:\Program Files\WindowsPowerShell\Modules, als je dit doet krijg je de melding dat de toegang is geweigerd, klik op doorgaan om de bestanden naar deze locatie te kopiëren en ga dan verder met de installatie instructies.[here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Installeren

<a name="Installeren"></a>

Om de modules te installeren moet u een PowerShell-venster uitvoeren als beheerder.
Er zijn twee manieren om dit te doen:

De eerste manier is door rechts te klikken op het PowerShell-pictogram op het bureaublad en uitvoeren als beheerder te selecteren in het keuzemenu.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

Door p (of hoeveel tekens PowerShell ook nodig heeft om te verschijnen) in de zoekbalk te typen en te klikken op Uitvoeren als beheerder.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

U moet in de map zijn waarnaar u de scripts hebt gekopieerd.
Voer het volgende commando uit om uw werkdirectory te veranderen:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Op Windows-clientcomputers moeten we het PowerShell-uitvoeringsbeleid wijzigen, dat standaard beperkt is.

Lees voor meer informatie dit[Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Voer het volgende commando uit om het beleid in te stellen op RemoteSigned en voer y in om aan te geven dat u het beleid wilt wijzigen.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Zodra het uitvoeringsbeleid is gewijzigd, kunt u het volgende commando uitvoeren om de modules te importeren.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Nu kunt u elk van de scripts uitvoeren als een module via powershell.
