---
title: "Rationaliser les mises à jour de Windows grâce à l'automatisation avec Chocolatey, PSWindowsUpdate et les scripts de démarrage"
date: 2020-07-22
---
 Mises à jour de Windows avec Chocolatey, PSWindowsUpdate et les scripts de démarrage**.

Dans l'environnement professionnel actuel, qui évolue rapidement, le temps est un facteur essentiel pour les administrateurs de systèmes. La mise à jour des machines Windows, un aspect critique de l'administration des systèmes, peut être une tâche extrêmement fastidieuse qui peut prendre jusqu'à une semaine, si le nombre de systèmes est suffisant. Cependant, avec l'aide de Chocolatey, PSWindowsUpdates et Startup Scripts, il est désormais possible de déployer des mises à jour en ne redémarrant qu'une seule fois chaque machine, ce qui réduit considérablement le temps nécessaire à l'exécution des mises à jour.

## Rationalisation des mises à jour de Windows grâce à l'automatisation

Les mises à jour de Windows sont essentielles au maintien de la stabilité et de la sécurité des machines Windows. Effectuer des mises à jour sur un grand nombre de machines peut être une tâche fastidieuse, en particulier pour les administrateurs système dont les ressources sont limitées. Cependant, grâce à l'utilisation d'outils d'automatisation tels que Chocolatey, PSWindowsUpdate et Startup Scripts, ce processus peut être rationalisé pour permettre aux administrateurs d'effectuer les mises à jour avec un minimum d'efforts.

### Chocolatey

[Chocolatey](https://chocolatey.org/) est un gestionnaire de paquets pour Windows qui peut être utilisé pour automatiser l'installation de logiciels sur les machines Windows. Il est similaire à apt-get sur Ubuntu ou à homebrew sur macOS, et il peut être utilisé pour installer et gérer un large éventail de paquets logiciels. Chocolatey peut être utilisé pour installer des paquets de manière silencieuse, ce qui signifie qu'ils peuvent être installés sans intervention de l'utilisateur.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) est un module PowerShell qui peut être utilisé pour automatiser l'installation des mises à jour de Windows. Il fournit des cmdlets qui peuvent être utilisés pour installer, désinstaller et répertorier les mises à jour de Windows. PSWindowsUpdate est un outil puissant qui peut être utilisé pour gérer les mises à jour de Windows sur plusieurs machines, ce qui le rend idéal pour les administrateurs système qui doivent gérer un grand nombre de machines.

### Scripts de démarrage

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) sont des scripts qui peuvent être utilisés pour automatiser les tâches qui doivent être exécutées lorsqu'une machine démarre ou s'éteint. Ces scripts peuvent être utilisés pour effectuer des tâches telles que l'installation de logiciels, la configuration des paramètres et la gestion des mises à jour de Windows.

## Automatiser les mises à jour de Windows avec un seul redémarrage

Pour automatiser les mises à jour de Windows à l'aide de Chocolatey, PSWindowsUpdate et Startup Scripts, les administrateurs peuvent suivre le guide étape par étape ci-dessous.

### Configuration du script d'arrêt
Téléchargez tous les fichiers de support à partir du site [GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Ouvrez l'éditeur de stratégie de groupe local en appuyant sur **"Win + R "** et en tapant **"gpedit.msc "** suivi de **"Ctrl + Shift + Enter "**.
2. Naviguez jusqu'à Ordinateur **Configuration\NParamètres Windows\Scripts (Démarrage/Arrêt)**.
3. Dans le volet des résultats, double-cliquez sur Arrêter.
4. Sélectionner l'onglet PowerShell.
5. Dans la boîte de dialogue Propriétés de l'arrêt, cliquez sur Ajouter.
6. Dans la zone Nom du script, saisissez le chemin d'accès au script ou cliquez sur Parcourir pour rechercher "*chocoautomatewindowsupdates.ps1*" dans le dossier partagé Netlogon sur le contrôleur de domaine.
7. Redémarrez.

Il ne reste plus à l'administrateur qu'à redémarrer l'ordinateur pour effectuer les mises à jour de Windows.

### Comprendre le script

Le script utilisé pour automatiser les mises à jour de Windows est intitulé "*chocoautomatewindowsupdates.ps1*". Il exécute les tâches suivantes :

1. Installe le gestionnaire de paquets Chocolatey.
2. Active quelques changements de configuration préférés de Chocolatey.
3. Met à jour tous les paquets Chocolatey installés.
4. Installe le module PowerShell PSWindowsUpdate.
5. Ajoute le gestionnaire de service Windows Update.
6. Installe toutes les mises à jour Windows disponibles.
7. Installe les pilotes manquants ou les mises à jour requises par les mises à jour précédemment installées.

### Avantages de l'automatisation des mises à jour de Windows

L'automatisation des mises à jour de Windows à l'aide de Chocolatey, PSWindowsUpdate et des scripts de démarrage présente plusieurs avantages pour les administrateurs système. Ces avantages sont les suivants :

- **Gain de temps** : L'automatisation des mises à jour de Windows réduit considérablement le temps nécessaire pour effectuer les mises à jour. Les administrateurs n'ont plus à installer manuellement les mises à jour sur chaque machine.
- Cohérence** : L'automatisation des mises à jour de Windows garantit que les mises à jour sont installées de manière cohérente sur toutes les machines. Cela réduit la probabilité d'erreurs et de failles de sécurité.
- Gestion centralisée** : L'automatisation des mises à jour de Windows permet aux administrateurs de gérer les mises à jour à partir d'un emplacement central, ce qui facilite le suivi des mises à jour installées et des machines nécessitant des mises à jour.
- Sécurité accrue** : L'automatisation des mises à jour de Windows garantit que les machines disposent des derniers correctifs de sécurité, ce qui réduit le risque de failles de sécurité.

### Conclusion

L'automatisation des mises à jour de Windows à l'aide de Chocolatey, PSWindowsUpdate et Startup Scripts est un outil puissant qui peut faire gagner beaucoup de temps et d'efforts aux administrateurs système. Elle permet d'installer les mises à jour de manière cohérente et efficace, en veillant à ce que les machines soient dotées des derniers correctifs de sécurité. En suivant les étapes décrites dans ce tutoriel, les administrateurs peuvent automatiser les mises à jour de Windows avec un simple redémarrage, ce qui rend le processus de mise à jour des machines Windows beaucoup plus rapide et facile.
