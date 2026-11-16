---
title: "Trouver la clé de récupération BitLocker avant de réinstaller Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Trouvez et vérifiez la bonne clé de récupération BitLocker, protégez-en une copie distincte et choisissez la bonne méthode de récupération ou de réinstallation Windows avant d'effacer un lecteur."
genre: ["Sécurité Windows", "Récupération de données", "Administration système"]
tags: ["clé de récupération BitLocker", "réinstaller Windows 11", "réinstaller Windows 10", "chiffrement de l’appareil", "ID de clé de récupération", "clé de récupération du compte Microsoft", "clé du compte professionnel ou scolaire", "sauvegarde de clé de récupération", "lecteur chiffré", "installation propre", "récupération Windows", "sauvegarde BitLocker", "clé de récupération à 48 chiffres", "support d’installation Windows", "sauvegarde des données", "chiffrement du lecteur", "liste de contrôle de récupération", "installation Windows", "dépannage BitLocker", "préparation à la réinstallation"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Un ordinateur portable avec un lecteur verrouillé, une carte séparée portant la clé de récupération, une sauvegarde USB et une liste de contrôle cochée."
coverCaption: "Vérifiez la clé de récupération avant d'effacer le lecteur."
---

Une installation propre de Windows efface le lecteur sélectionné. Si l'ancien lecteur utilise **BitLocker** ou le **chiffrement de l'appareil**, trouvez la clé de récupération et copiez vos fichiers avant de commencer. La clé permet d'accéder aux anciennes données chiffrées. Une nouvelle installation de Windows ne restaure pas les fichiers effacés du lecteur.

<!--more-->

## Points clés

- **Trouvez la bonne clé :** comparez l'ID affiché par Windows à la clé enregistrée dans votre compte, sur une impression ou sur une sauvegarde USB.
- **Vérifiez l'accès :** examinez la sauvegarde, comparez l'ID et déverrouillez le lecteur avant d'effacer des partitions.
- **Protégez la sauvegarde :** gardez la clé à 48 chiffres séparée de l'ordinateur et de la clé USB d'installation.
- **Choisissez la bonne méthode :** utilisez les options de récupération si vous avez besoin de l'ancienne installation. Choisissez une installation propre uniquement après avoir vérifié une copie distincte de vos fichiers.

## Avant de commencer

Vous avez besoin d'un accès à l'ordinateur concerné, d'un deuxième appareil pour vérifier votre compte ou votre sauvegarde, ainsi que d'un lecteur externe ou d'un stockage cloud fiable pour les fichiers importants. **Durée :** la recherche de la clé dépend de l'accès au compte. La copie dépend du volume de données. **Difficulté :** élémentaire pour vérifier un compte, intermédiaire pour les outils de récupération. Ce guide couvre la préparation et les choix de récupération sous Windows 10 et Windows 11. Le [guide d'installation propre de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) traite du support d'installation et de la configuration.

*Le support standard de Windows 10 a pris fin le 14 octobre 2025. Si votre appareil répond aux exigences, planifiez l'installation d'une version prise en charge de Windows 11. Microsoft répertorie le [cycle de vie de Windows 10 et les options de support étendu](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Avertissement :** ne supprimez pas une partition pour résoudre une demande de récupération BitLocker si vous avez encore besoin des fichiers de l'ancienne installation. Microsoft indique qu'une réinitialisation sans clé de récupération supprime ces fichiers. Consultez les [conseils Microsoft sur les clés de récupération](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Vérifier si le chiffrement est actif

Le **chiffrement de l'appareil** et **BitLocker** chiffrent un lecteur pour empêcher toute personne sans les bons identifiants d'en lire le contenu. Si Windows démarre encore, ouvrez **Paramètres > Confidentialité et sécurité > Chiffrement de l'appareil** sous Windows 11. Dans les éditions qui gèrent BitLocker, recherchez **Gérer BitLocker** dans le menu Démarrer. Notez la lettre du lecteur chiffré et le compte utilisé pour configurer l'appareil. Pour un appareil professionnel ou scolaire géré, l'organisation détient souvent la clé.

Vous pouvez aussi vérifier l'état en ligne de commande. Recherchez **Invite de commandes** dans le menu Démarrer, sélectionnez **Exécuter en tant qu'administrateur** et saisissez ces commandes. Remplacez `C:` si Windows utilise une autre lettre. Un **protecteur** est une méthode que Windows utilise pour déverrouiller un lecteur chiffré.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

La première commande indique l'état du chiffrement, de la protection et du verrouillage. La seconde répertorie les types et les ID des protecteurs et peut afficher le mot de passe de récupération. Microsoft documente ces contrôles dans son [guide des opérations BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) et la [référence de la commande d'état](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Ne collez pas la sortie dans une demande d'aide et ne la partagez pas en capture d'écran.** Si l'appareil est déjà verrouillé, utilisez l'ID affiché sur l'écran de récupération. Ses huit premiers chiffres aident à sélectionner la clé correspondante.

## Où trouver la clé de récupération BitLocker

L'**ID de clé de récupération** identifie une clé enregistrée. La **clé de récupération** est le nombre distinct de 48 chiffres à saisir pour déverrouiller le lecteur. Ne saisissez pas l'ID dans le champ du mot de passe de récupération.

| Appareil ou sauvegarde | Où chercher |
|---|---|
| **Compte Microsoft personnel** | Sur un deuxième appareil, connectez-vous par le [portail Microsoft des clés de récupération](https://aka.ms/myrecoverykey). Comparez l'ID avant d'utiliser la clé à 48 chiffres. |
| **Appareil professionnel ou scolaire** | Vérifiez le compte de l'organisation via le [portail Microsoft pour les comptes professionnels ou scolaires](https://aka.ms/aadrecoverykey), ou demandez à votre équipe informatique. |
| **Impression ou sauvegarde USB** | Retrouvez l'impression ou le fichier texte créé lors de l'activation du chiffrement. Comparez son ID à celui affiché. |

Microsoft répertorie ces emplacements dans [Trouver votre clé de récupération BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Commencez par la clé dont l'ID correspond à la demande. Une clé d'un autre appareil ou d'un protecteur supprimé peut ne pas déverrouiller ce volume. Si une autre personne a configuré l'appareil, sa clé peut se trouver dans son compte.

## Créer une sauvegarde séparée de la clé

Si Windows démarre encore sur une édition Pro, Enterprise ou Education, recherchez **Gérer BitLocker**. Sélectionnez **Sauvegarder votre clé de récupération** à côté du lecteur chiffré. Microsoft propose une sauvegarde dans un compte, sur un lecteur USB, dans un fichier texte ou sur papier. Si vous choisissez un fichier texte ou une clé USB, stockez-la uniquement sur un support chiffré avec contrôle d'accès, séparé de l'ordinateur. N'utilisez pas d'emplacement non chiffré. Consultez [Sauvegarder votre clé de récupération BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) pour connaître l'interface et les options actuelles.

Sous Windows Home, **Gérer BitLocker** n'est pas disponible. Sous Windows 11, vérifiez **Paramètres > Confidentialité et sécurité > Chiffrement de l'appareil**, puis contrôlez la clé dans le compte Microsoft utilisé lors de la configuration. Microsoft explique que le [chiffrement de l'appareil](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) enregistre la clé dans le compte Microsoft ou professionnel associé lors de l'activation. Enregistrez une autre copie protégée si la configuration propose une méthode d'exportation.

Ouvrez une sauvegarde numérique sur un deuxième appareil. Pour une impression, comparez-la à l'entrée du compte ou à l'écran de récupération. Faites correspondre l'**ID de clé de récupération** à celui de l'écran ou de la liste des protecteurs. Vérifiez que les 48 chiffres de la clé correspondante sont présents. Gardez une copie papier ou amovible à l'écart de l'ordinateur chiffré. Un voleur possédant l'ordinateur et la clé pourrait contourner la protection du lecteur, avertit Microsoft dans ses [conseils de sauvegarde](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Ne joignez pas la clé à un ticket d'assistance.

> **Résultat attendu :** vous avez accès à une clé de récupération correspondante depuis l'extérieur de l'ordinateur.

## Déverrouiller un ordinateur qui ne démarre pas

Si l'**écran de récupération BitLocker** apparaît, saisissez la clé à 48 chiffres correspondant à son ID. Si Windows démarre, copiez vos fichiers avant de modifier les partitions. Si la clé déverrouille le lecteur mais que Windows ne démarre toujours pas, ouvrez l'[environnement de récupération Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) et essayez **Réparation du démarrage** avant une réinitialisation. Certains outils de récupération exigent la clé tant que le lecteur est chiffré.

Pour sauvegarder des fichiers depuis les outils de récupération, ouvrez **Dépannage > Options avancées > Invite de commandes** dans l'environnement de récupération Windows. Utilisez `manage-bde -status` et `dir` pour repérer le volume Windows chiffré et un lecteur externe distinct pour la sauvegarde. **Les lettres de lecteur peuvent différer de celles utilisées normalement.** Ne copiez pas les fichiers sur la clé USB d'installation ni sur le lecteur source chiffré.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

Les lettres ci-dessus sont des exemples. Après avoir repéré les bons volumes, déverrouillez le volume Windows avec la clé correspondante. Remplacez la lettre et le texte fictifs par vos propres valeurs. Saisissez la vraie clé à 48 chiffres localement. Ne publiez ni ne partagez la sortie.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

L'option documentée `-recoverypassword` prend la clé à 48 chiffres comme argument de ligne de commande. La clé devient visible dans l'historique du shell, les transcriptions et l'inspection des processus. Utilisez l'écran de récupération Windows si vous voulez saisir la clé sans argument de commande. Si vous avez enregistré un fichier de clé `.bek` séparé, `-recoverykey <path-to-external-bek>` évite de saisir les 48 chiffres. Gardez la clé hors des captures d'écran et des tickets.

Microsoft documente la [commande de déverrouillage](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). Ses [conseils de récupération](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) décrivent aussi la copie de fichiers utilisateur vers un autre lecteur après le déverrouillage. Pour illustrer la copie du dossier Documents, confirmez d'abord le nom du compte Windows et la lettre du lecteur externe, puis remplacez les deux chemins :

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

Les options **`/S /E`** incluent les sous-dossiers, même vides. **`/I`** traite la destination comme un dossier, **`/H`** inclut les fichiers masqués et **`/V`** vérifie chaque fichier écrit. Microsoft documente ces options dans la [référence xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Répétez l'opération pour les autres dossiers nécessaires. Ouvrez les fichiers copiés sur un autre appareil avant d'effacer le lecteur Windows. Si vous ne pouvez pas identifier les volumes ou si la copie échoue, arrêtez-vous et contactez un spécialiste de récupération de confiance.

## Décider de réinstaller Windows

**Une sauvegarde de clé n'est pas une sauvegarde de fichiers.** Suivez cet ordre avant de choisir une méthode de réinstallation :

1. Identifiez le lecteur chiffré et son ID de clé de récupération.
2. Récupérez la clé correspondante à 48 chiffres depuis votre compte, une impression ou une sauvegarde USB.
3. Si le lecteur est verrouillé, déverrouillez-le depuis l'écran ou les outils de récupération.
4. Copiez Bureau, Documents, Images et les autres dossiers locaux vers un lecteur externe ou un cloud fiable. Ajoutez si nécessaire les exportations du navigateur, les données des applications et les informations de licence.
5. Ouvrez plusieurs fichiers copiés sur un deuxième appareil.
6. Choisissez une réparation, une réinitialisation ou une réinstallation seulement après avoir vérifié la sauvegarde.

> **Résultat attendu :** la clé correspondante et les fichiers importants sont accessibles en dehors de l'ancienne installation Windows.

Microsoft présente les [options de récupération Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), dont les effets sur les fichiers et les applications diffèrent. De nombreuses options de l'environnement de récupération Windows demandent la clé lorsque BitLocker protège le lecteur. Si le volume y est verrouillé, **Conserver mes fichiers** ne le déverrouille pas sans la clé.

**Réparation du démarrage** et **Restauration du système** tentent de réparer l'installation existante. **Réinitialiser ce PC** propose **Conserver mes fichiers**, mais supprime les applications et paramètres. **Tout supprimer** efface les fichiers personnels. Lancer **`setup.exe` depuis une session Windows active** permet une réinstallation sur place avec des options de conservation des données. Choisir **Installer Windows** après avoir démarré depuis une clé USB lance une installation propre qui supprime fichiers, applications et paramètres de l'installation sélectionnée. Le même support propose aussi une méthode de réparation. Lisez l'option affichée et vérifiez le disque cible avant de confirmer une réinitialisation ou une installation. Microsoft explique les deux méthodes dans ses [instructions de réinstallation](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Cas de figure | Action suivante |
|---|---|
| **Windows démarre et vous avez besoin des fichiers** | Sauvegardez les fichiers, vérifiez la clé, puis choisissez une réparation ou une réinstallation. |
| **Windows demande la clé** | Faites correspondre l'ID affiché à une clé enregistrée avant de modifier le lecteur. |
| **Aucune clé correspondante et aucune sauvegarde de fichiers** | Arrêtez-vous avant d'effacer le lecteur. Vérifiez chaque compte, impression, sauvegarde USB et contactez votre équipe informatique. |
| **Les fichiers sont sauvegardés et vous voulez repartir de zéro** | Suivez les [instructions de réinstallation de Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) et choisissez soigneusement le disque cible. |

Microsoft indique que son assistance ne peut pas recréer une clé perdue. Si vous ne la trouvez pas, cessez de modifier les paramètres du micrologiciel et vérifiez tous les emplacements de sauvegarde. Demandez de l'aide à l'administrateur pour un appareil géré. Une réinitialisation sans la clé nécessaire supprime les anciens fichiers. Une installation propre supprime aussi les fichiers personnels, les applications, les personnalisations de l'appareil et les paramètres de l'installation sélectionnée. Prenez cette décision après avoir vérifié la sauvegarde.

## Dépannage

- **La clé ne fonctionne pas :** revérifiez l'ID et le compte. Un appareil peut avoir plusieurs clés de récupération enregistrées.
- **Gérer BitLocker est absent :** Windows Home utilise le chiffrement de l'appareil sur les appareils compatibles. Vérifiez Paramètres et le compte Microsoft utilisé lors de la configuration.
- **Plusieurs clés apparaissent dans le compte :** comparez les huit premiers chiffres de l'ID affiché aux entrées enregistrées. Ne choisissez pas une clé uniquement d'après le nom de l'appareil.
- **La clé déverrouille le lecteur mais Windows ne démarre pas :** essayez Réparation du démarrage dans l'environnement de récupération Windows. Sauvegardez les fichiers accessibles avant une réinitialisation ou une installation propre.
- **La clé est détenue par l'entreprise ou l'école :** contactez l'administrateur de l'appareil avant de le réinitialiser ou de le réinstaller.
- **Le fichier de clé est sur l'ordinateur verrouillé :** cherchez un compte séparé, une impression ou une sauvegarde amovible. Une copie uniquement sur le lecteur chiffré n'aide pas lorsqu'il est verrouillé.
- **La demande est apparue après une modification du micrologiciel :** notez le changement et n'en faites pas d'autres. Trouvez la clé correspondante ou contactez l'administrateur.

## Étapes suivantes

Après avoir vérifié la clé et les fichiers, suivez le [guide d'installation propre de Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) si cela correspond à votre objectif. Une fois Windows démarré, vérifiez **Paramètres > Confidentialité et sécurité > Chiffrement de l'appareil** ou recherchez **Gérer BitLocker**. Sur Pro, Enterprise ou Education, sélectionnez **Sauvegarder votre clé de récupération** dans Gérer BitLocker. Sur Home, vérifiez que le compte associé contient la clé actuelle et enregistrez-en une copie séparée si Windows propose une exportation. Ne supposez pas que l'ancienne clé correspond à une nouvelle installation chiffrée.
