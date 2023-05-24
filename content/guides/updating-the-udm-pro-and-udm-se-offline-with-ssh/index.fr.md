---
title: "Mise à jour hors ligne du micrologiciel pour Ubiquiti Unifi UDM Pro et UDM SE via la ligne de commande SSH"
draft: false
toc: true
date: 2023-05-28
description: "Apprenez à mettre à jour le micrologiciel d'Ubiquiti Unifi UDM Pro et UDM SE hors ligne via la ligne de commande SSH pour des performances et une sécurité optimales."
tags: ["Mise à jour du micrologiciel Ubiquiti", "UDMPro", "UDM SE", "mise à jour du firmware hors ligne", "SSH en ligne de commande", "la gestion du réseau", "sécurité Internet", "mise à jour du firmware", "Connexion SSH", "fichier du micrologiciel", "Contrôleur de réseau UniFi", "corrections de bogues", "Amélioration des performances", "correctifs de sécurité", "la mise en réseau", "Périphériques réseau", "technologie", "gestion IT", "processus de mise à jour du micrologiciel", "optimisation du réseau", "Mise à jour du micrologiciel Ubiquiti Networks", "Mise à jour du micrologiciel UDM Pro", "Mise à jour du micrologiciel UDM SE", "processus de mise à jour du firmware hors ligne", "Mise à jour du micrologiciel SSH", "gestion des périphériques réseau", "mises à jour de sécurité réseau", "stratégies de mise à jour du firmware", "gestion du micrologiciel hors ligne", "optimisation des performances du réseau", "gestion des correctifs de sécurité", "mises à jour de la technologie réseau"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Une illustration colorée représentant un ordinateur se connectant à un routeur via SSH symbolisant le processus de mise à jour du micrologiciel hors ligne pour les appareils Ubiquiti Unifi UDM Pro et UDM SE."
coverCaption: ""
---

** Mettre à jour Ubiquiti Unifi UDM Pro et UDM SE hors ligne via SSH **

Dans le monde du réseautage, **Ubiquiti Networks** est reconnu pour ses solutions innovantes. **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** et **Unifi Dream Machine SE (UDM SE)** sont deux produits populaires qui offrent des fonctionnalités complètes de gestion de réseau. La mise à jour du micrologiciel de ces appareils est cruciale pour garantir des performances et une sécurité optimales. Dans cet article, nous allons explorer comment mettre à jour le micrologiciel de l'UDM Pro et de l'UDM SE **hors ligne** à l'aide de la ligne de commande SSH.

______

## Pourquoi mettre à jour le micrologiciel ?

Les mises à jour du micrologiciel sont essentielles pour tout périphérique réseau, car elles contiennent souvent des correctifs de bogues, des améliorations de performances et des correctifs de sécurité. La mise à jour régulière du micrologiciel de votre UDM Pro et UDM SE est cruciale pour garantir la sécurité et le bon fonctionnement de votre réseau.

______

## Mise à jour du micrologiciel hors ligne

La mise à jour du micrologiciel de l'UDM Pro et de l'UDM SE peut être effectuée via le **tableau de bord UniFi**. Cependant, dans certains scénarios, une connexion Internet peut ne pas être disponible ou souhaitable. Dans de tels cas, une mise à jour hors ligne à l'aide de la ligne de commande SSH fournit une solution alternative.

______

## Préparation de la mise à jour hors ligne

Avant de procéder à la mise à jour hors ligne, assurez-vous que vous disposez des prérequis suivants :

1. Un ordinateur ou un appareil avec un client SSH installé.
2. Le dernier fichier de firmware pour votre UDM Pro ou UDM SE. Vous pouvez obtenir le fichier du micrologiciel à partir du [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) compte

______

## Établissement de la connexion SSH

Pour mettre à jour UDM Pro ou UDM SE via la ligne de commande SSH, procédez comme suit :

1. Assurez-vous que votre ordinateur ou appareil est connecté au même réseau que l'UDM Pro ou l'UDM SE.
2. Ouvrez votre client SSH préféré et établissez une connexion SSH à l'**adresse IP de l'UDM Pro ou de l'UDM SE**. Par exemple, en utilisant le **client OpenSSH** sous Linux ou macOS, vous pouvez utiliser la commande suivante :

```bash
ssh root@<UDM_IP_ADDRESS>
```

Remplacer `<UDM_IP_ADDRESS>` avec l'adresse IP réelle de votre UDM Pro ou UDM SE.

3. Entrez le **nom d'utilisateur** et le **mot de passe** lorsque vous y êtes invité. Les informations d'identification par défaut pour les appareils Ubiquiti sont généralement `ubnt` pour le nom d'utilisateur et le mot de passe.

______

## Mise à jour du micrologiciel

Une fois que vous avez établi la connexion SSH, vous pouvez procéder à la mise à jour du firmware :

1. Téléchargez le fichier du micrologiciel sur l'UDM Pro ou l'UDM SE à l'aide de **SCP (Secure Copy)**. SCP permet le transfert de fichiers sécurisé via SSH. En supposant que le fichier du micrologiciel se trouve sur votre ordinateur local, vous pouvez utiliser la commande suivante :

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Remplacer `<FIRMWARE_FILE_PATH>` avec le chemin d'accès au fichier du micrologiciel sur votre machine locale, et `<UDM_IP_ADDRESS>` avec l'adresse IP de votre UDM Pro ou UDM SE.

2. Une fois le fichier du micrologiciel téléchargé, vous pouvez lancer le processus de mise à jour du micrologiciel. Exécutez la commande suivante :

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. L'UDM Pro ou l'UDM SE démarre le processus de mise à jour du micrologiciel. Cela peut prendre plusieurs minutes. **N'interrompez pas le processus** tant que la mise à jour n'est pas terminée.

4. Une fois la mise à jour terminée, vous pouvez vérifier la version du micrologiciel en vous connectant au contrôleur de réseau UniFi ou en exécutant la commande suivante :

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Veuillez noter que le processus ci-dessus suppose que vous disposez du fichier de micrologiciel nécessaire pour votre UDM Pro ou UDM SE. Assurez-vous que vous disposez du fichier de micrologiciel correct pour le modèle et la version de votre appareil spécifique.

## Conclusion

La mise à jour du micrologiciel de vos appareils Ubiquiti Unifi UDM Pro et UDM SE est une étape cruciale pour garantir des performances et une sécurité optimales. Bien que le contrôleur de réseau UniFi offre un moyen pratique de mettre à jour le micrologiciel, effectuer une mise à jour hors ligne via la ligne de commande SSH offre une solution viable lorsqu'une connexion Internet n'est pas disponible ou souhaitable.

En suivant les étapes décrites dans cet article, vous pouvez mettre à jour avec succès le micrologiciel de vos appareils UDM Pro et UDM SE à l'aide de la ligne de commande SSH. N'oubliez pas de toujours utiliser la dernière version du micrologiciel fournie par Ubiquiti Networks pour profiter des corrections de bogues, des améliorations de performances et des correctifs de sécurité.

## Les références

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Page de téléchargement officielle d'Ubiquiti pour les fichiers de firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)
