---
title: "PowerShell Scripting : Un guide pas à pas pour les débutants afin d'automatiser les tâches"
draft: false
toc: true
date: 2023-02-25
description: "Apprenez les bases de l'écriture de scripts PowerShell et automatisez des tâches grâce à ce guide pas à pas pour les débutants, qui couvre les cmdlets, les boucles, les fonctions et bien plus encore."
genre: ["Technologie", "Programmation", "Automatisation", "Fenêtres", "Scripting", "IT", "Tâches administratives", "Gestion informatique", "Développement de logiciels", "Codage"]
tags: ["Scripting PowerShell", "Automatisation PowerShell", "Scripting Windows", "Les cmdlets PowerShell", "Modules PowerShell", "Boucles PowerShell", "Instructions conditionnelles PowerShell", "Fonctions PowerShell", "Meilleures pratiques PowerShell", "Débogage de PowerShell", "Tests PowerShell", "Variables PowerShell", "PowerShell ISE", "Remoting PowerShell", "Technologies Microsoft", "Automatisation des technologies de l'information", "gestion informatique", "codage pour les débutants", "les tâches administratives", "Idées de scripts PowerShell", "sauvegardes automatisées", "gestion des fichiers", "informations sur le système", "gestion des utilisateurs", "installation du logiciel", "configuration du réseau", "automatisation de la sécurité", "planification des tâches", "manipulation du registre", "administration à distance"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.png"
coverAlt: "Un personnage de bande dessinée tenant un script et se tenant devant un ordinateur avec une invite PowerShell, indiquant la facilité d'utilisation des scripts PowerShell pour les débutants"
coverCaption: ""
---
 Les scripts PowerShell pour les débutants**

PowerShell est un puissant shell de ligne de commande et un langage de script développé par Microsoft. Il offre un large éventail de commandes et de fonctionnalités permettant de gérer et d'automatiser divers aspects du système d'exploitation Windows et d'autres technologies Microsoft. Dans cet article, nous aborderons les bases de l'écriture de scripts PowerShell pour les débutants et fournirons un guide étape par étape pour commencer.

## Introduction à PowerShell

**PowerShell** est un shell de ligne de commande qui permet aux utilisateurs d'automatiser et de gérer le système d'exploitation Windows et d'autres technologies Microsoft. Il fournit un ensemble complet de commandes et de fonctionnalités qui permettent aux utilisateurs d'effectuer diverses tâches administratives, telles que la gestion des fichiers et des répertoires, la configuration du réseau et la gestion du système. PowerShell prend également en charge un langage de script qui permet aux utilisateurs de créer des scripts complexes et d'automatiser diverses tâches répétitives.

## Premiers pas avec PowerShell

### Installer PowerShell

PowerShell est préinstallé dans la plupart des versions du système d'exploitation Windows. Toutefois, si vous utilisez une version plus ancienne de Windows ou si vous avez besoin d'une version plus récente de PowerShell, vous pouvez la télécharger à partir du site web de Microsoft. Pour télécharger et installer PowerShell, suivez les étapes suivantes :

1. Allez sur le site [Microsoft PowerShell website](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) et sélectionnez la version de PowerShell que vous souhaitez installer.
2. Téléchargez le fichier d'installation et exécutez-le.
3. Suivez les instructions à l'écran pour terminer le processus d'installation.

### Démarrage de PowerShell

Une fois PowerShell installé, vous pouvez le démarrer en suivant les étapes suivantes :

1. Cliquez sur le menu Démarrer et tapez "PowerShell" dans la barre de recherche.
2. Sélectionnez "Windows PowerShell" dans les résultats de la recherche.
3. PowerShell s'ouvre dans une nouvelle fenêtre.

### Les bases de PowerShell

PowerShell fournit une interface de ligne de commande qui permet aux utilisateurs d'interagir avec le système d'exploitation. Les commandes de PowerShell sont appelées cmdlets et sont organisées en modules. Pour afficher la liste des modules disponibles, utilisez la commande Get-Module :

```powershell
Get-Module
```

Pour afficher la liste des cmdlets disponibles dans un module, utilisez la commande Get-Command :
```powershell
Get-Command -Module <module name>
```

Pour obtenir de l'aide sur une cmdlet, utilisez la commande Get-Help :
```powershell
Get-Help <cmdlet name>
```

PowerShell prend également en charge les alias, qui sont des noms plus courts pour les cmdlets. Pour afficher la liste des alias disponibles, utilisez la commande Get-Alias :
```powershell
Get-Alias
```

### PowerShell Scripting
L'écriture de scripts PowerShell est une fonction puissante qui permet aux utilisateurs d'automatiser diverses tâches administratives. Les scripts PowerShell prennent en charge les variables, les boucles, les instructions conditionnelles et les fonctions, ce qui en fait un outil puissant pour l'automatisation.

#### Variables
Les variables sont utilisées pour stocker des données dans les scripts PowerShell. Dans PowerShell, les variables commencent par le signe du dollar ($). Pour attribuer une valeur à une variable, utilisez la syntaxe suivante :
```powershell
$variable_name = value
```
Par exemple :
```powershell
$name = "John"
```
#### Boucles
Les boucles sont utilisées pour répéter un bloc de code un certain nombre de fois. PowerShell prend en charge les types de boucles suivants :

- **For loop** : répète un bloc de code un certain nombre de fois.
- Boucle While** : répète un bloc de code tant qu'une condition est remplie.
- Boucle Do-While** : répète un bloc de code au moins une fois et ensuite tant qu'une condition est vraie.
- Boucle orEach** : répète un bloc de code pour chaque élément d'une collection.
  
Par exemple, le code suivant utilise une boucle For pour imprimer les nombres 1 à 5 :
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Déclarations conditionnelles

Déclarations conditionnelles

Les instructions conditionnelles sont utilisées pour exécuter un bloc de code si une certaine condition est vraie. PowerShell prend en charge les types d'instructions conditionnelles suivants :

- **If statement** : exécute un bloc de code si une condition est vraie.
- Instruction If-Else** : exécute un bloc de code si une condition est vraie, et un autre bloc de code si la condition est fausse.
- L'instruction Switch** : compare une valeur à un ensemble de correspondances possibles et exécute un bloc de code pour la première correspondance trouvée.

Par exemple, le code suivant utilise une instruction If pour vérifier si un nombre est supérieur à 5 :

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "The number is greater than 5"
}
```
#### Fonctions
Les fonctions sont des blocs de code réutilisables qui exécutent une tâche spécifique. Les fonctions prennent des paramètres en entrée et renvoient des valeurs en sortie. PowerShell prend en charge les types de fonctions suivants :

- Bloc de script** : bloc de code pouvant être exécuté.
- Fonction avancée : une fonction qui inclut des métadonnées et une validation des paramètres.

Par exemple, le code suivant définit une fonction qui additionne deux nombres :
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
PowerShell ISE (Integrated Scripting Environment) est une interface utilisateur graphique pour les scripts PowerShell. PowerShell ISE fournit un éditeur de texte riche, des outils de débogage et d'autres fonctionnalités qui facilitent l'écriture et le test des scripts PowerShell. Pour ouvrir PowerShell ISE, procédez comme suit :

1. Cliquez sur le menu Démarrer et tapez "PowerShell ISE" dans la barre de recherche.
2. Sélectionnez "Windows PowerShell ISE" dans les résultats de la recherche.
3. PowerShell ISE s'ouvre dans une nouvelle fenêtre.

### PowerShell Remoting
PowerShell Remoting permet aux utilisateurs d'exécuter des commandes et des scripts PowerShell sur des ordinateurs distants. PowerShell Remoting nécessite que le service WinRM soit exécuté à la fois sur l'ordinateur local et sur l'ordinateur distant. Pour activer PowerShell Remoting, procédez comme suit :

1. Ouvrez une invite PowerShell avec des privilèges d'administrateur.
2. Exécutez la commande suivante pour activer PowerShell Remoting :
```powershell
   Enable-PSRemoting -Force
```
3. Exécutez la commande suivante pour ajouter l'ordinateur distant à la liste TrustedHosts :
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Redémarrer le service WinRM
```powershell
Restart-Service WinRM
```

Pour exécuter une commande PowerShell sur un ordinateur distant, utilisez la cmdlet Invoke-Command :
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Modules PowerShell
Les modules PowerShell sont des collections de cmdlets, de fonctions et de scripts conçus pour effectuer des tâches spécifiques. Les modules PowerShell peuvent être installés et gérés à l'aide de la galerie PowerShell, qui est un référentiel central pour les modules PowerShell.

Pour installer un module PowerShell à partir de la galerie PowerShell, utilisez la commande suivante :
```powershell
Install-Module <module name>
```

Pour afficher la liste des modules PowerShell installés, utilisez la commande Get-InstalledModule :
```powershell
Get-InstalledModule
```

### Meilleures pratiques pour les scripts PowerShell

Lorsque vous écrivez des **scripts PowerShell**, il est important de suivre les meilleures pratiques pour garantir que les scripts sont **sécurisés**, **fiables** et **maintenables**. Voici quelques bonnes pratiques à garder à l'esprit :

- **Utiliser des noms de variables descriptifs** : Utilisez des noms de variables qui indiquent clairement leur objectif.
- Utilisez des commentaires** : Utilisez des commentaires pour expliquer l'objectif du code.
- Utiliser la gestion des erreurs** : Utilisez la gestion des erreurs pour traiter les erreurs et les exceptions de manière élégante. Les `Try...Catch...Finally` de PowerShell vous permet de gérer les exceptions et de prendre les mesures qui s'imposent. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Tester les scripts de manière approfondie** : Testez soigneusement les scripts pour vous assurer qu'ils fonctionnent comme prévu. Vous pouvez utiliser **Pester**, un cadre de test pour PowerShell, pour écrire et exécuter des tests unitaires pour vos scripts. [Pester Documentation](https://pester.dev/)
- Utiliser des fonctions et des modules** : Utilisez les fonctions et les modules pour organiser le code et améliorer sa réutilisation. Les fonctions vous permettent de décomposer votre code en éléments plus petits et plus faciles à gérer, tandis que les modules fournissent un moyen d'empaqueter et de distribuer votre code. [About Functions](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [About Modules](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Éviter le codage en dur des valeurs** : Évitez de coder des valeurs en dur dans le script et utilisez plutôt des paramètres ou des variables. Cela rend vos scripts plus flexibles et réutilisables. Vous pouvez passer des paramètres à vos scripts à l'aide de la fonction `param` mot-clé. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Utiliser la sortie verbeuse** : Utilisez la sortie verbeuse pour fournir des informations supplémentaires sur la progression du script. Vous pouvez utiliser l'option `Write-Verbose` cmdlet pour afficher des messages verbeux lors de l'exécution du script. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

Le respect de ces bonnes pratiques vous aidera à écrire des scripts PowerShell plus efficaces et plus faciles à maintenir, ce qui améliorera votre productivité et garantira la stabilité de vos tâches d'automatisation.

### Élaboration des meilleures pratiques pour les scripts PowerShell

#### Utiliser la gestion des erreurs
La gestion des erreurs est un aspect essentiel des scripts PowerShell, car elle permet de s'assurer que le script gère les erreurs et les exceptions de manière élégante. PowerShell propose plusieurs façons de gérer les erreurs, notamment l'instruction Try-Catch, l'instruction Trap et le paramètre ErrorAction. L'instruction Try-Catch est utilisée pour attraper et gérer les exceptions, tandis que l'instruction Trap est utilisée pour attraper et gérer les erreurs. Le paramètre ErrorAction permet de contrôler la manière dont le script gère les erreurs.

Voici un exemple d'utilisation de l'instruction Try-Catch pour gérer une erreur de manière élégante :
```powershell
try {
    # some code that might throw an error
}
catch {
    Write-Error "An error occurred: $_"
}
```

#### Les scripts de test sont minutieux

Il est essentiel de tester les scripts PowerShell pour s'assurer qu'ils fonctionnent comme prévu. PowerShell fournit plusieurs outils et cadres de test, tels que Pester, qui permettent aux utilisateurs d'écrire et d'exécuter des tests pour leurs scripts. Ces outils permettent d'identifier et d'isoler les problèmes dans le code et de s'assurer que le script répond aux exigences souhaitées.

Voici un exemple d'utilisation de Pester pour tester un script PowerShell :
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # some code that should return the expected result
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### Utiliser les fonctions et les modules
Les fonctions et les modules sont essentiels pour organiser le code et améliorer la réutilisation des scripts PowerShell. Les fonctions permettent aux utilisateurs de regrouper le code en blocs réutilisables, tandis que les modules permettent aux utilisateurs d'empaqueter et de partager le code avec d'autres. L'utilisation de fonctions et de modules permet de rendre les scripts PowerShell plus modulaires, plus efficaces et plus faciles à maintenir.

Voici un exemple d'utilisation d'une fonction dans PowerShell :
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "There are $count processes running."
```

#### Éviter le codage en dur des valeurs
Le codage en dur de valeurs dans un script PowerShell le rend moins flexible et plus difficile à maintenir. Au lieu de coder des valeurs en dur, il est préférable d'utiliser des paramètres ou des variables, qui permettent aux utilisateurs de transmettre des valeurs au script au moment de l'exécution. L'utilisation de paramètres ou de variables permet de rendre le script plus réutilisable et de l'adapter à des conditions changeantes.

Voici un exemple d'utilisation d'un paramètre dans PowerShell :
```powershell
param (
    [string]$name
)

Write-Host "Hello, $name!"
```

#### Utiliser la sortie Verbose
La sortie verbeuse fournit des informations supplémentaires sur la progression du script, ce qui peut s'avérer utile pour le débogage et le dépannage. PowerShell propose la cmdlet Write-Verbose, qui permet aux utilisateurs d'afficher des informations détaillées sur la console. L'utilisation de la sortie verbose permet de rendre les scripts PowerShell plus informatifs et plus faciles à déboguer.

Voici un exemple d'utilisation de la sortie verbeuse dans PowerShell :
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

### Dix idées de scripts PowerShell pour les débutants

Si vous êtes un débutant en matière de scripts PowerShell, voici dix idées de scripts pour vous aider à démarrer :

- **Sauvegardes automatisées** : Créez un script qui automatise le processus de sauvegarde des fichiers et répertoires importants sur un disque dur externe ou un service de stockage en nuage. Vous pouvez utiliser le script `Copy-Item` pour copier des fichiers et la cmdlet `Start-Job` pour exécuter le processus de sauvegarde en arrière-plan. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Gestion de fichiers** : Créez un script qui organise les fichiers et les répertoires en les classant dans différents dossiers en fonction du type de fichier, de la taille ou d'autres critères. Vous pouvez utiliser la fonction `Get-ChildItem` pour récupérer des fichiers et la cmdlet `Move-Item` pour les déplacer à l'endroit souhaité. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informations système** : Créez un script qui récupère les informations système, telles que l'utilisation du processeur et de la mémoire, l'espace disque et les paramètres réseau, et qui les affiche dans un format facile à lire. Vous pouvez utiliser la fonction `Get-WmiObject` cmdlet pour recueillir des informations sur le système et les formater à l'aide de `Format-Table` ou `Out-GridView` [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gestion des utilisateurs** : Créez un script qui automatise le processus d'ajout, de modification ou de suppression d'utilisateurs et de groupes dans le système d'exploitation Windows. Vous pouvez utiliser l'outil `New-LocalUser` `Set-LocalUser` et `Remove-LocalUser` pour gérer les utilisateurs, et les cmdlets `New-LocalGroup` `Add-LocalGroupMember` et `Remove-LocalGroup` pour gérer les groupes. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Installation de logiciels** : Créez un script qui installe et configure des logiciels sur plusieurs ordinateurs à la fois, ce qui permet de gagner du temps et d'économiser des efforts. Vous pouvez utiliser le script `Invoke-Command` pour exécuter des commandes d'installation sur des ordinateurs distants. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Configuration du réseau** : Créez un script qui automatise le processus de configuration des paramètres réseau, tels que l'adresse IP, le masque de sous-réseau et la passerelle par défaut. Vous pouvez utiliser le script `Set-NetIPAddress` `Set-NetIPInterface` et `Set-DnsClientServerAddress` pour configurer les paramètres du réseau. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Sécurité** : Créez un script qui vérifie et contrôle les paramètres de sécurité et alerte l'utilisateur si des changements sont détectés. Vous pouvez utiliser le script `Get-AuditPolicy` pour récupérer les politiques d'audit et la cmdlet `Send-MailMessage` pour envoyer des notifications par courrier électronique. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Planification des tâches** : Créez un script qui planifie et automatise les tâches récurrentes, telles que les sauvegardes, les mises à jour et les analyses du système. Vous pouvez utiliser la fonction `Register-ScheduledTask` pour créer des tâches planifiées et la cmdlet `Start-ScheduledTask` pour les exécuter. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Manipulation du registre** : Créer un script qui modifie ou récupère les valeurs du registre pour des clés ou des valeurs spécifiques. Vous pouvez utiliser la fonction `Get-ItemProperty` et `Set-ItemProperty` pour interagir avec le registre. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Administration à distance** : Créez un script qui permet l'administration à distance des ordinateurs Windows, permettant aux utilisateurs d'exécuter des commandes et des scripts sur des machines distantes. Vous pouvez utiliser le script `Enter-PSSession` ou la cmdlet `Invoke-Command` pour exécuter des commandes sur des ordinateurs distants. [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Microsoft Documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Commencez à explorer ces idées de script pour acquérir une expérience pratique et développer vos compétences en PowerShell.

## Conclusion

PowerShell est un outil puissant pour gérer et automatiser le système d'exploitation Windows et d'autres technologies Microsoft. Dans cet article, nous avons abordé les bases de l'écriture de scripts PowerShell pour les débutants, notamment l'installation et le démarrage de PowerShell, l'utilisation des cmdlets, des variables, des boucles, des instructions conditionnelles et des fonctions, ainsi que l'utilisation de PowerShell ISE, de PowerShell Remoting et des modules PowerShell. En respectant les meilleures pratiques, les scripts PowerShell peuvent être sécurisés, fiables et faciles à maintenir. Avec de l'entraînement, vous pourrez maîtriser les scripts PowerShell et automatiser facilement diverses tâches administratives.
