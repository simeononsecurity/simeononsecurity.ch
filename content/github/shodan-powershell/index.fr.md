---
title: "Automatiser l'OSINT avec les modules PowerShell de Shodan"
date: 2020-11-14
---

Une collection de modules PowerShell pour interagir avec l'API Shodan

**Notes:**
- Vous aurez besoin de votre clé API Shodan, qui peut être trouvée sur votre [Shodan Account](https://account.shodan.io/)
- Des exemples d'API utilisées dans les modules peuvent être trouvés sur le site Web de la Commission européenne. [Shodan Developers Page](https://developer.shodan.io/api)
- Certains modules peuvent utiliser des crédits de balayage ou de requête Les crédits de requête sont utilisés lorsque vous téléchargez des données via le site web, le CLI ou l'API (ce que font ces scripts).
  Comme nous utilisons l'API, il est important de noter que les crédits d'interrogation sont déduits si :
  1.  Un filtre de recherche est utilisé
  2.  La page 2 ou plus est demandée
      Les crédits sont renouvelés au début du mois et 1 crédit vous permet de télécharger 100 résultats.
      Quant aux crédits de numérisation, 1 crédit de numérisation vous permet de numériser 1 IP, et ils se renouvellent également au début du mois.
      Veuillez consulter le Centre d'aide Shodan [HERE](https://help.shodan.io/the-basics/credit-types-explained) pour plus de détails.

## Table des matières
- [Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
- [Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **Modules**
  - [Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - Renvoie des informations sur le plan d'API appartenant à la clé d'API donnée.
  - [Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - Affiche les en-têtes HTTP que votre client envoie lorsqu'il se connecte à un serveur web.
  - [Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - Permet d'obtenir votre adresse IP actuelle telle qu'elle est perçue sur Internet.
  - [Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - Obtient tous les sous-domaines et autres entrées DNS pour le domaine donné
  - [Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  - [Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - Recherche les noms d'hôtes qui ont été définis pour la liste d'adresses IP donnée.
  - [Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - Recherche des exploits mais ne renvoie que des informations sur le nombre total de correspondances liées au terme de recherche, et éventuellement l'auteur de l'exploit, la plate-forme, le port, la source ou le type.
  - [Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  - [Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - Renvoie le nombre total de résultats de "/shodan/host/search" fournit.
  - [Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - Recherchez Shodan avec l'adresse IP.
  - [Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - Effectuez une recherche sur Shodan en utilisant la même syntaxe de requête que le site web et utilisez les facettes pour obtenir des informations sommaires sur les différentes propriétés.
  - [Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - Ce module renvoie une liste de filtres de recherche qui peuvent être utilisés dans la requête de recherche.
  - [Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - Ce module renvoie une liste de filtres de recherche qui peuvent être utilisés dans la requête de recherche.
  - [Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - Listez tous les ports que Shodan explore sur Internet.
  - [Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - Renvoie des informations sur le compte Shodan lié à cette clé API
  - [Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - Vérifier l'état d'avancement d'une demande d'analyse précédemment soumise
  - [Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - Dressez la liste de tous les protocoles qui peuvent être utilisés pour effectuer des analyses Internet à la demande via Shodan.
  - [Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP) - Utilisez ce module pour demander à Shodan de parcourir un réseau.

<a name="Download"></a>

## Télécharger

Vous devrez cloner ou télécharger les scripts sur votre ordinateur.

Vous pouvez utiliser le menu déroulant Code sur la page de ce repo en défilant vers le haut, ou simplement copier et coller le lien suivant : [https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

Pour cet exemple, nous allons cloner le repo dans Git Bash, après avoir cliqué sur l'icône du presse-papiers comme indiqué ci-dessus, nous pouvons taper git clone et faire un clic droit sur la fenêtre de Git Bash pour sélectionner coller dans le menu déroulant :

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

Pour des instructions détaillées sur le clonage, veuillez consulter [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Une fois que vous avez les fichiers, vous devez les copier dans C:\NProgram Files\NWindowsPowerShell\NModules, ce qui provoquera une boîte de dialogue indiquant que l'accès est refusé, cliquez sur continuer pour terminer la copie des fichiers à cet emplacement, puis passez aux instructions d'installation. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

Vous pouvez utiliser le menu déroulant Code sur la page de ce repo en défilant vers le haut, ou simplement cliquer sur le lien suivant :
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Décompressez le fichier main.zip en cliquant avec le bouton droit de la souris sur le fichier et en sélectionnant Extraire ici dans le menu déroulant.

Une fois que vous avez les fichiers, vous devez les copier dans C:\NProgram Files\NWindowsPowerShell\NModules, ce qui provoquera une boîte de dialogue indiquant que l'accès est refusé, cliquez sur continuer pour terminer la copie des fichiers à cet emplacement, puis passez aux instructions d'installation. [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Installer

<a name="Install"></a>

Pour installer les modules, vous devez lancer une fenêtre PowerShell en tant qu'administrateur.
Il y a deux façons de procéder :

La première consiste à cliquer avec le bouton droit de la souris sur l'icône PowerShell du bureau et à sélectionner Exécuter en tant qu'administrateur dans le menu déroulant.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

En tapant p (ou le nombre de caractères qu'il faut à PowerShell pour s'afficher) dans la barre de recherche et en cliquant sur Exécuter en tant qu'administrateur.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

Vous devez vous trouver dans le répertoire dans lequel vous avez copié les scripts.
Exécutez la commande suivante pour changer de répertoire de travail :

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

Sur les ordinateurs clients Windows, nous devons modifier la stratégie d'exécution de PowerShell, qui est restreinte par défaut.

Pour plus d'informations, veuillez lire ce qui suit [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Exécutez la commande suivante pour définir la stratégie sur RemoteSigned et entrez y pour indiquer que vous souhaitez modifier la stratégie.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Une fois la politique d'exécution modifiée, vous pouvez exécuter la commande suivante pour importer les modules.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

Vous pouvez maintenant exécuter n'importe lequel des scripts en tant que module via powershell.
