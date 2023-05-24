---
title: "Meilleures pratiques pour la gestion des sources de temps dans les domaines Windows et les machines autonomes"
draft: false
toc: true
date: 2023-05-23
description: "Découvrez comment définir et gérer efficacement les sources de temps dans les domaines Windows et les machines autonomes pour assurer une synchronisation précise de l'heure et éviter les problèmes potentiels."
tags: ["sources de temps", "Domaine Windows", "machines autonomes", "synchronisation de l'heure", "chronométrage précis", "Serveurs NTP", "contrôleurs de domaine", "Service de temps Windows", "échecs d'authentification", "incohérences du fichier journal", "problèmes de réplication", "configuration de la source horaire", "gestion des sources de temps", "Synchronisation de l'heure Windows", "bonnes pratiques de chronométrage", "configuration de la source horaire", "synchronisation de l'heure système", "Synchronisation de l'heure du domaine Windows", "synchronisation de l'heure de la machine autonome", "sélection de la source horaire", "dépannage de la source de temps", "erreurs de source de temps", "problèmes de source de temps", "commandes de configuration de la source horaire", "instructions de configuration de la source horaire", "défis de la synchronisation de l'heure", "conséquences de la perte de temps", "prévention de la dérive temporelle", "résolution d'échec de synchronisation de l'heure", "dépannage de la synchronisation de l'heure", "gestion des sources de temps dans les domaines Windows", "gestion des sources de temps dans des machines Windows autonomes", "prévention des pertes de temps dans les environnements Windows", "conséquences des échecs de synchronisation de l'heure", "meilleures pratiques pour un chronométrage précis"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Image représentant une horloge synchronisée avec un contrôleur de domaine et une machine autonome, symbolisant la gestion de la source horaire et la synchronisation précise de l'heure dans les environnements Windows."
coverCaption: ""
---

**Comment définir et gérer les sources de temps dans un domaine Windows et sur des machines Windows autonomes**

La synchronisation de l'heure est cruciale pour maintenir des horodatages précis et garantir le bon fonctionnement des systèmes dans un domaine Windows ou des machines Windows autonomes. Dans cet article, nous discuterons des meilleures pratiques pour définir et gérer les sources de temps dans les deux scénarios, en soulignant l'importance des membres de domaine pointant vers des contrôleurs de domaine. Nous explorerons également différentes options pour les sources de temps, en mettant l'accent sur l'utilisation de pools NTP externes ou de serveurs de temps basés sur GPS pour une précision optimale.

______

## Définition des sources de temps dans un domaine Windows

Dans un domaine Windows, il est essentiel d'avoir une synchronisation de l'heure cohérente sur tous les membres du domaine. La meilleure pratique consiste à configurer les contrôleurs de domaine comme source de temps principale pour les membres du domaine. Ce faisant, vous vous assurez que tous les systèmes du domaine disposent d'une heure synchronisée, ce qui est essentiel pour l'authentification, la journalisation et diverses opérations de domaine.

### Options de source horaire pour les contrôleurs de domaine

Les contrôleurs de domaine peuvent obtenir leur heure à partir de différentes sources, notamment l'horloge du BIOS, VMware Tools (dans les environnements virtualisés) ou des serveurs de temps externes. Bien que l'utilisation de l'horloge du BIOS ou de VMware Tools puisse être pratique, il est recommandé d'utiliser une **source de strate 0 ou 1** comme un pool NTP externe ou un serveur de temps basé sur GPS pour une précision accrue.

#### Pools NTP externes

Les pools NTP externes sont des sources mondialement distribuées et fiables pour la synchronisation de l'heure. Ils se composent d'un grand nombre de serveurs NTP gérés par des organisations et des institutions du monde entier. En configurant les contrôleurs de domaine pour qu'ils se synchronisent avec les pools NTP externes, vous pouvez garantir un chronométrage précis au sein du domaine Windows.

Pour configurer des contrôleurs de domaine pour utiliser un pool NTP externe, procédez comme suit :

1. Ouvrez une invite de commande élevée sur le contrôleur de domaine.
2. Exécutez la commande suivante :

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Cette commande configure le contrôleur de domaine pour qu'il se synchronise avec le pool NTP pool.ntp.org. Ajustez la commande pour utiliser un pool NTP différent ou plusieurs sources si vous le souhaitez.

3. Redémarrez le service de temps Windows pour appliquer les modifications :

```shell
net stop w32time && net start w32time
```


#### Serveurs de temps basés sur GPS

Une autre option pour les contrôleurs de domaine consiste à utiliser des serveurs de temps basés sur le GPS. Ces serveurs s'appuient sur des signaux GPS pour fournir des informations temporelles très précises. En configurant un serveur de temps basé sur GPS hébergé localement et en configurant les contrôleurs de domaine pour qu'ils se synchronisent avec lui, vous pouvez obtenir une synchronisation précise de l'heure au sein du domaine Windows.

### Configuration des membres du domaine

Les membres du domaine, tels que les machines clientes et autres serveurs, doivent être configurés pour synchroniser leur heure avec les contrôleurs de domaine. Cela garantit que tous les systèmes du domaine restent synchronisés et évitent tout problème lié au temps.

Pour configurer les membres du domaine afin qu'ils synchronisent l'heure avec les contrôleurs de domaine, aucune étape supplémentaire n'est généralement requise. Par défaut, les membres du domaine synchronisent automatiquement leur heure avec les contrôleurs de domaine.

______

## Définition des sources de temps sur des machines Windows autonomes

Sur les machines Windows autonomes qui ne font pas partie d'un domaine, le processus de définition des sources de temps peut varier en fonction de la version de Windows et des paramètres régionaux. Par défaut, les machines Windows autonomes utilisent généralement **time.windows.com** comme source de temps principale. Cependant, il convient de noter que le comportement par défaut peut être modifié.

### Modification de la source de temps sur les machines autonomes

Si vous souhaitez modifier la source horaire sur une machine Windows autonome, vous pouvez suivre ces étapes :

1. Ouvrez une invite de commande élevée sur la machine.
2. Exécutez la commande suivante pour configurer le serveur NTP :

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Cette commande définit time.windows.com comme source de temps pour la machine autonome. Ajustez la commande pour utiliser une source de temps différente si vous le souhaitez.

3. Redémarrez le service de temps Windows pour que les modifications prennent effet :

```shell
net stop w32time && net start w32time
```


En exécutant ces commandes, vous pouvez configurer une machine Windows autonome pour synchroniser son heure avec la source de temps souhaitée.

______

## Conclusion

Une bonne synchronisation de l'heure est vitale pour les domaines Windows et les machines autonomes. Dans un domaine Windows, il est crucial de configurer les membres du domaine pour qu'ils pointent vers les contrôleurs de domaine pour la synchronisation de l'heure. Les contrôleurs de domaine peuvent obtenir leur temps à partir de diverses sources, l'utilisation de pools NTP externes ou de serveurs de temps basés sur GPS étant la pratique recommandée pour une précision accrue.

Sur les machines Windows autonomes, la source de temps par défaut est généralement time.windows.com. Cependant, vous pouvez modifier la source horaire à l'aide des commandes fournies.

En suivant ces meilleures pratiques et en configurant des sources de temps appropriées, vous garantissez un chronométrage précis, une authentification fiable et une journalisation cohérente dans votre environnement Windows.

______

## Les références

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)

