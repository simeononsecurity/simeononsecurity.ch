---
title: "Meilleures pratiques de base de durcissement de Windows pour sécuriser Windows 10 et Windows 11"
date: 2023-07-27
toc: true
draft: false
description: "Découvrez des stratégies efficaces pour renforcer la sécurité de vos systèmes Windows 10 et Windows 11 grâce à des techniques complètes de durcissement et à des pratiques exemplaires."
genre: ["Durcissement des fenêtres", "Sécurité Windows", "Durcissement de Windows 10", "Durcissement de Windows 11", "Meilleures pratiques en matière de sécurité Windows", "Conseils de sécurité pour Windows", "Directives de sécurité pour Windows", "Sécurisation des systèmes d'exploitation Windows", "Durcissement du système Windows", "Mesures de sécurité pour Windows"]
tags: ["Durcissement des fenêtres", "Sécurité Windows", "Windows 10", "Windows 11", "la sécurité des systèmes d'exploitation", "Windows Defender", "Contrôle du compte d'utilisateur", "Cryptage BitLocker", "configuration du pare-feu", "Politiques d'AppLocker", "Mises à jour de Windows", "des mots de passe forts", "sauvegarde des données", "Windows Hello", "Amorçage sécurisé", "TPM", "Antivirus Microsoft Defender", "Bac à sable Windows", "Microsoft Defender Application Guard", "Accès contrôlé aux dossiers", "Meilleures pratiques pour sécuriser Windows 10 et Windows 11", "Comment renforcer les systèmes d'exploitation Windows", "Mesures de sécurité Windows pour les particuliers et les organisations", "Renforcer la sécurité du système Windows", "Protéger les données avec le chiffrement BitLocker", "Isolement des sessions de navigation avec Microsoft Defender Application Guard", "Conseils et directives de sécurité pour Windows 10", "Mise en œuvre des fonctions de sécurité de Windows", "Sécuriser Windows avec l'isolation matérielle", "Garantir l'intégrité du système Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.png"
coverAlt: "Illustration en bande dessinée d'un bouclier protégeant le logo Windows de diverses cybermenaces."
coverCaption: "Sécurisez votre forteresse Windows grâce à des techniques de durcissement efficaces."
---

## Introduction

Les systèmes d'exploitation Windows sont largement utilisés par les particuliers et les organisations du monde entier. Pour garantir la sécurité et l'intégrité de ces systèmes, il est essentiel de mettre en œuvre les **meilleures pratiques de durcissement de Windows**. Le durcissement consiste à sécuriser le système d'exploitation en réduisant sa surface d'attaque et en atténuant les vulnérabilités potentielles. Cet article explore les meilleures pratiques de durcissement des systèmes d'exploitation **Windows 10** et **Windows 11**, plus récents, et fournit des informations précieuses pour renforcer la sécurité de votre environnement Windows.

______

## Comprendre le durcissement de Windows

Le durcissement de Windows est le processus de renforcement de la sécurité d'un système d'exploitation Windows. Il s'agit de configurer divers paramètres et de mettre en œuvre des mesures de sécurité pour se protéger contre les accès non autorisés, les logiciels malveillants et d'autres menaces. En renforçant votre système Windows, vous pouvez minimiser les risques associés aux cyberattaques et garantir la confidentialité, l'intégrité et la disponibilité de vos données.

### [Hardening Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 10 est l'un des systèmes d'exploitation les plus utilisés au monde. Pour renforcer votre environnement Windows 10, tenez compte des meilleures pratiques suivantes :

#### 1. [**Enable Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

Windows Defender est une **solution antivirus robuste** incluse dans Windows 10. Il offre une gamme de fonctions de sécurité pour protéger votre système contre divers types de **malwares**, y compris **les virus, les logiciels espions et les ransomwares**. En activant Windows Defender, vous pouvez améliorer considérablement la sécurité de votre environnement Windows 10.

Pour activer Windows Defender, procédez comme suit :

- Ouvrez l'application **Windows Security** en cliquant sur l'icône Windows Security dans la barre des tâches ou en recherchant "Windows Security" dans le menu Démarrer.
- Dans l'application Sécurité Windows, cliquez sur "**Protection contre les virus et les menaces**" dans le volet de navigation de gauche.
- Cliquez sur "**Gérer les paramètres**" dans la section "Paramètres de protection contre les virus et les menaces".
- Assurez-vous que l'interrupteur à bascule "**Protection en temps réel**" est positionné sur "**On**". Cela permet à Windows Defender d'analyser et de protéger activement votre système en temps réel.
- En outre, vous pouvez personnaliser les options d'analyse et les exclusions en cliquant sur "**Options d'analyse**" et "**Ajouter ou supprimer des exclusions**", respectivement.

Il est essentiel de mettre à jour **régulièrement** Windows Defender pour s'assurer qu'il dispose des dernières **définitions de logiciels malveillants** et **améliorations de sécurité**. Microsoft publie régulièrement des mises à jour pour répondre aux nouvelles menaces et vulnérabilités. Pour mettre à jour Windows Defender, vous pouvez suivre les étapes suivantes :

- Ouvrez l'application Windows Security.
- Allez dans "**Protection contre les virus et les menaces**" dans le volet de navigation de gauche.
- Cliquez sur "**Vérifier les mises à jour**" dans la section "Mises à jour de la protection contre les virus et les menaces".
- Windows recherchera les mises à jour disponibles et les téléchargera/installera si nécessaire.

En activant Windows Defender et en le maintenant à jour, vous pouvez protéger de manière proactive votre système Windows 10 contre les logiciels malveillants et autres menaces de sécurité. Il est également recommandé d'effectuer **des analyses régulières du système** à l'aide de Windows Defender pour garantir la détection et la suppression de toute menace potentielle.

N'oubliez pas que si Windows Defender offre un niveau de protection solide, il est essentiel de le compléter par **des habitudes de navigation sûres**, **des mises à jour logicielles régulières** et d'autres mesures de sécurité pour maintenir un environnement Windows 10 sécurisé.

#### 2. [**Keep Windows 10 Updated**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)
L'installation régulière des mises à jour de Windows est un aspect essentiel de la **maintenance de Windows 10**. Ces mises à jour comprennent des **rattrapages de sécurité**, des corrections de bogues et des améliorations de performances qui aident à **rattraper les vulnérabilités de sécurité** et à améliorer la stabilité du système.

Microsoft publie **des mises à jour régulières** pour Windows 10 afin de résoudre les problèmes de sécurité récemment découverts et d'améliorer l'expérience globale de l'utilisateur. En gardant votre système à jour, vous vous assurez que votre système d'exploitation dispose des dernières **améliorations de sécurité** pour se défendre contre les menaces émergentes.

Pour maintenir Windows 10 à jour, vous pouvez suivre les étapes suivantes :

1. **Activer les mises à jour automatiques** : Par défaut, Windows 10 est configuré pour télécharger et installer automatiquement les mises à jour. Cela garantit que votre système reçoit les mises à jour nécessaires sans intervention manuelle. Pour vérifier si les mises à jour automatiques sont activées, procédez comme suit :
   - Allez dans **Paramètres** en cliquant sur le menu Démarrer et en sélectionnant l'icône en forme d'engrenage.
   - Cliquez sur **Mise à jour et sécurité**.
   - Dans le volet de navigation de gauche, cliquez sur **Mise à jour Windows**.
   - Assurez-vous que l'option **"Automatique "** est sélectionnée sous **"Paramètres de Windows Update "**. Si elle n'est pas sélectionnée, cliquez sur le lien **"Modifier les heures actives "** pour personnaliser les heures actives pendant lesquelles Windows doit éviter d'installer les mises à jour.

2. **Installer manuellement les mises à jour** : Si vous préférez avoir plus de contrôle sur le processus de mise à jour, vous pouvez installer manuellement les mises à jour sur votre système Windows 10. Voici comment procéder :
   - Allez dans **Paramètres** > **Mise à jour et sécurité** > **Mise à jour Windows**.
   - Cliquez sur **"Rechercher des mises à jour "** pour voir si des mises à jour sont disponibles pour votre système.
   - Si des mises à jour sont trouvées, cliquez sur **"Télécharger "** et **"Installer "** pour lancer le processus d'installation.

Il est essentiel de souligner l'importance de **redémarrer régulièrement votre système** après l'installation des mises à jour. Certaines mises à jour peuvent nécessiter un redémarrage du système pour appliquer complètement les changements et garantir leur efficacité.

En **maintenant votre système Windows 10 à jour**, vous renforcez non seulement sa sécurité, mais vous bénéficiez également des dernières fonctionnalités, des améliorations de performance et des correctifs de compatibilité. Il s'agit d'une mesure proactive visant à garantir que votre système reste résilient face aux menaces de sécurité potentielles.

#### 3. [**Configure User Account Control (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)
Le contrôle de compte d'utilisateur (UAC) est une fonction de sécurité de Windows 10 qui aide à prévenir les modifications non autorisées de votre système en demandant l'approbation de l'administrateur lorsque cela est nécessaire. Il sert de protection contre les logiciels malveillants ou les utilisateurs non autorisés qui tentent d'apporter des modifications susceptibles d'avoir un impact sur la sécurité ou la stabilité du système.

La configuration des paramètres UAC à un niveau approprié est cruciale pour **durcir Windows 10**. Il s'agit de trouver un équilibre entre la sécurité et la convivialité pour s'assurer que l'UAC protège efficacement votre système sans causer d'interruptions inutiles.

Pour configurer les paramètres UAC dans Windows 10, vous pouvez suivre les étapes suivantes :

1. Ouvrez le **Panneau de configuration** en tapant "Panneau de configuration" dans la barre de recherche et en le sélectionnant dans les résultats de la recherche.

2. Dans le Panneau de configuration, cliquez sur **"Comptes d'utilisateurs "**.

3. Cliquez sur **"Modifier les paramètres du contrôle de compte d'utilisateur "**.

4. Vous verrez un curseur avec différents niveaux de paramètres UAC. Voici les options disponibles :
   - **"Toujours notifier "** : Il s'agit du niveau de sécurité UAC le plus élevé, dans lequel vous êtes invité à donner votre accord pour toute modification du système, même pour des tâches simples.
   - Notifier uniquement lorsque des applications tentent d'apporter des modifications à mon ordinateur (par défaut) "** : Il s'agit du paramètre recommandé qui offre un équilibre entre la sécurité et la convivialité. Vous êtes invité à donner votre accord lorsque des applications effectuent des modifications, mais pas pour les changements de paramètres de Windows.
   - Notifiez-moi uniquement lorsque des applications tentent d'apporter des modifications à mon ordinateur (sans assombrir mon bureau) "** : Semblable à l'option précédente, mais le bureau n'est pas assombri lorsque des invites de l'UAC apparaissent.
   - **"Ne jamais notifier "** : Il s'agit du niveau de sécurité le plus bas de l'UAC : aucune modification du système ne vous est demandée.

5. Choisissez le niveau de sécurité UAC qui vous convient en déplaçant le curseur jusqu'à la position souhaitée.

6. Cliquez sur **"OK "** pour enregistrer les modifications.

Il est recommandé de laisser l'UAC activé et de le régler à un niveau qui offre un bon équilibre entre la sécurité et la convivialité. La désactivation complète de l'UAC peut rendre votre système plus vulnérable aux modifications non autorisées et compromettre sa sécurité.

En configurant les paramètres de l'UAC, vous renforcez la sécurité de votre système Windows 10 en veillant à ce que des privilèges administratifs soient requis pour les modifications critiques du système, ce qui réduit le risque d'accès non autorisé et d'infections par des logiciels malveillants.

#### 4. [**Use Strong Passwords**](https://simeononsecurity.ch/articles/how-to-create-strong-passwords/)
L'utilisation de mots de passe forts est essentielle pour maintenir la sécurité de votre système Windows 10 et le protéger contre les accès non autorisés. Des mots de passe faibles ou faciles à deviner peuvent rendre votre système vulnérable aux attaques, telles que les attaques par force brute ou le craquage de mots de passe.

Pour vous assurer que tous les comptes d'utilisateur de votre système Windows 10 disposent de mots de passe forts, suivez ces bonnes pratiques en matière de mots de passe :

1. **Complexité** : Encouragez les utilisateurs à créer des mots de passe complexes et difficiles à deviner. Un mot de passe solide doit comprendre une combinaison de lettres majuscules et minuscules, de chiffres et de caractères spéciaux. Évitez d'utiliser des mots communs ou des schémas prévisibles.

2. **Longueur** : Les mots de passe longs sont généralement plus sûrs. Encouragez les utilisateurs à créer des mots de passe d'au moins 8 caractères, mais de préférence plus longs. Plus il y a de caractères dans un mot de passe, plus il est difficile à décrypter.

3. **Unicité** : Chaque compte d'utilisateur doit avoir un mot de passe unique. L'utilisation du même mot de passe pour plusieurs comptes augmente le risque de violation de la sécurité. Encouragez les utilisateurs à utiliser des mots de passe différents pour des comptes différents.

4. **Éviter les informations personnelles** : Conseillez aux utilisateurs de ne pas utiliser d'informations personnelles telles que des noms, des dates de naissance ou des adresses dans leurs mots de passe. Ces informations peuvent être facilement obtenues ou devinées par des pirates.

5. **Gestionnaire de mots de passe** : Envisagez d'utiliser un gestionnaire de mots de passe pour stocker et gérer les mots de passe en toute sécurité. Les gestionnaires de mots de passe peuvent générer des mots de passe forts et uniques pour chaque compte et les stocker dans une base de données cryptée.

6. **Changer régulièrement les mots de passe** : Encouragez les utilisateurs à changer régulièrement leurs mots de passe pour maintenir la sécurité. Définissez une politique d'expiration des mots de passe et sensibilisez les utilisateurs à l'importance d'une mise à jour régulière de leurs mots de passe.

En mettant en œuvre des pratiques strictes en matière de mots de passe, vous renforcez considérablement la sécurité de votre système Windows 10 et réduisez le risque d'accès non autorisé ou d'atteinte à la protection des données. Sensibilisez régulièrement les utilisateurs à la sécurité des mots de passe et fournissez-leur des ressources, telles que des indicateurs de force de mot de passe ou des directives de création de mot de passe, pour les aider à créer des mots de passe forts.

Pour obtenir des informations plus détaillées sur la création de mots de passe forts et les meilleures pratiques, vous pouvez consulter le document suivant [article](https://simeononsecurity.ch/articles/how-to-create-strong-passwords/) Il fournit des conseils complets sur la sécurité des mots de passe et propose des astuces pour créer des mots de passe forts et mémorables.

N'oubliez pas que l'utilisation de mots de passe forts est un aspect fondamental de la sécurité du système et qu'il faut en faire une priorité pour protéger les données sensibles et garantir l'intégrité de votre environnement Windows 10.

#### 5. [**Enable BitLocker Encryption**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
L'un des moyens les plus efficaces de protéger les données sensibles sur votre système Windows 10 est d'activer le chiffrement BitLocker. BitLocker fournit un chiffrement intégral du disque, garantissant que même si votre appareil est perdu ou volé, vos données restent sécurisées et inaccessibles aux personnes non autorisées.

Pour activer le cryptage BitLocker et protéger vos informations sensibles, procédez comme suit :

1. **Vérifiez la configuration requise** : Assurez-vous que votre édition de Windows 10 prend en charge le chiffrement BitLocker. BitLocker est disponible dans les éditions Pro, Entreprise et Éducation de Windows 10.

2. **Activer BitLocker** : Ouvrez le Panneau de configuration et accédez à la catégorie "Système et sécurité". Cliquez sur "BitLocker Drive Encryption" et sélectionnez le(s) lecteur(s) que vous souhaitez crypter. Suivez les instructions à l'écran pour lancer le processus de cryptage.

3. **Choisissez les options de cryptage** : Lors de l'installation de BitLocker, vous aurez la possibilité de choisir entre différentes méthodes de cryptage, telles que l'utilisation d'un mot de passe, d'une carte à puce ou des deux. Sélectionnez la méthode appropriée en fonction de vos exigences et préférences en matière de sécurité.

4. **Clé de récupération de la sauvegarde** : Il est essentiel de sauvegarder la clé de récupération BitLocker. Cette clé sert de sécurité en cas d'oubli du mot de passe ou de problème d'accès au disque crypté. Conservez la clé de récupération dans un endroit sûr, séparé de votre appareil.

5. **Gérer les paramètres BitLocker** : Après avoir activé BitLocker, vous pouvez personnaliser des paramètres supplémentaires, tels que le déverrouillage automatique pour des lecteurs spécifiques ou la configuration de l'utilisation du TPM (Trusted Platform Module) pour une sécurité accrue. Ces paramètres sont accessibles via l'interface de gestion de BitLocker.

En activant le chiffrement BitLocker, vous ajoutez une couche de protection supplémentaire à votre système Windows 10, garantissant que même si votre appareil tombe entre de mauvaises mains, vos données restent en sécurité et inaccessibles. Il est important de mettre à jour et d'entretenir régulièrement vos paramètres BitLocker pour rester au fait des meilleures pratiques en matière de sécurité.

Pour obtenir des informations plus détaillées sur l'activation et la gestion du chiffrement BitLocker, vous pouvez vous référer au document officiel [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) Il fournit des conseils complets sur le chiffrement BitLocker, y compris les fonctions avancées et les options de configuration.

N'oubliez pas que l'activation du chiffrement BitLocker contribue à la protection de vos données sensibles et vous apporte la tranquillité d'esprit de savoir que vos informations sont en sécurité, même en cas de perte ou de vol.

#### 6. **Désactiver les services et fonctionnalités inutiles**
Pour renforcer la sécurité de votre système Windows 10, il est essentiel de passer en revue et de désactiver tous les services et fonctionnalités inutiles. Ce faisant, vous réduisez la surface d'attaque et minimisez le potentiel d'exploitation par des acteurs malveillants.

Voici les étapes à suivre pour désactiver les services et fonctionnalités inutiles sur votre système Windows 10 :

1. **Identifier les services inutiles** : Commencez par identifier les services en cours d'exécution sur votre système. Ouvrez la console de gestion "Services" en appuyant sur **Touche Windows + R**, en tapant **services.msc** et en appuyant sur **Entrée**. Examinez la liste des services et recherchez leur utilité afin de déterminer ceux qui sont essentiels au bon fonctionnement de votre système.

2. **Désactivez les services inutiles** : Une fois que vous avez identifié les services inutiles, cliquez avec le bouton droit de la souris sur chaque service et sélectionnez **Propriétés**. Dans la fenêtre Propriétés, modifiez le **Type de démarrage** en **Désactivé**. Cela empêche le service de se lancer automatiquement lorsque votre système démarre. Soyez prudent et assurez-vous que vous ne désactivez que les services qui ne sont pas nécessaires au fonctionnement normal de votre système.

3. **Désactiver les fonctionnalités inutiles** : En plus des services, Windows 10 inclut également diverses fonctionnalités qui peuvent ne pas être nécessaires à votre système. Ouvrez le **Panneau de configuration**, naviguez jusqu'à **Programmes** ou **Programmes et fonctionnalités**, et cliquez sur **Activer ou désactiver les fonctionnalités de Windows**. Décochez toutes les fonctions dont vous n'avez pas besoin. Cette étape permet de réduire davantage la surface d'attaque et de minimiser les ressources consommées par les fonctionnalités inutiles.

4. **Passez régulièrement en revue et mettez à jour** : Il est crucial de revoir régulièrement la liste des services et fonctionnalités activés sur votre système Windows 10. Les exigences de votre système évoluant au fil du temps, il se peut que vous deviez réévaluer les services et fonctionnalités nécessaires. Restez vigilant et mettez à jour votre configuration si nécessaire.

En désactivant les services et fonctionnalités inutiles, vous limitez les points d'entrée potentiels pour les attaquants et réduisez la surface d'attaque globale de votre système Windows 10. Cette pratique améliore la posture de sécurité de votre système et atténue le risque d'exploitation.

Pour plus d'informations sur la gestion des services et des fonctionnalités dans Windows 10, vous pouvez consulter les documents suivants [article](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20) pour des conseils détaillés.

N'oubliez pas qu'il est essentiel de faire preuve de prudence lorsque vous désactivez des services et des fonctionnalités, car la désactivation de composants essentiels peut avoir un impact négatif sur le fonctionnement de votre système. Il convient de toujours rechercher et comprendre l'objectif d'un service ou d'une fonctionnalité avant de procéder à des modifications.

#### 7. **Mettre en place des règles de pare-feu**
Le pare-feu intégré à Windows 10 constitue une ligne de défense cruciale contre le trafic réseau non autorisé. En configurant les règles du pare-feu, vous pouvez contrôler les connexions entrantes et sortantes autorisées, ce qui renforce la sécurité de votre système.

Suivez ces étapes pour mettre en place des règles de pare-feu sur votre système Windows 10 :

1. **Accéder aux paramètres du pare-feu** : Pour accéder aux paramètres du pare-feu, ouvrez le **Panneau de configuration**, recherchez **Windows Defender Firewall**, et cliquez sur le résultat correspondant. Vous pouvez également cliquer avec le bouton droit de la souris sur le bouton **Démarrer**, sélectionner **Paramètres**, et naviguer jusqu'à **Réseau et Internet > Pare-feu Windows**.

2. **Configurez les règles d'entrée** : Les règles de réception contrôlent les connexions réseau entrantes vers votre système. Cliquez sur **Paramètres avancés** dans la fenêtre Pare-feu Windows Defender. Dans la nouvelle fenêtre, sélectionnez **Règles entrantes** et cliquez sur **Nouvelle règle**. Suivez les instructions à l'écran pour créer des règles qui n'autorisent que les connexions entrantes nécessaires. Tenez compte des services et des applications qui nécessitent un accès au réseau et créez des règles en conséquence.

3. **Configurez les règles de sortie** : Les règles de sortie contrôlent les connexions réseau sortantes de votre système. Suivez les mêmes étapes que ci-dessus, mais sélectionnez **Règles de sortie** à la place. Créez des règles pour autoriser les connexions sortantes pour les services et applications essentiels, tout en bloquant les connexions suspectes ou inutiles.

4. **Réviser et mettre à jour régulièrement** : Il est important de revoir et de mettre à jour régulièrement les règles de votre pare-feu pour s'assurer qu'elles correspondent aux exigences de votre système. Au fur et à mesure que votre environnement réseau et vos habitudes d'utilisation changent, vous devrez peut-être modifier les règles ou en créer de nouvelles. Restez vigilant et gardez vos règles à jour pour maintenir une configuration de pare-feu efficace.

En mettant en œuvre et en maintenant des règles de pare-feu, vous pouvez réduire considérablement le risque d'accès non autorisé au réseau et renforcer la sécurité de votre système Windows 10. En outre, envisagez d'activer l'option **Mode furtif** dans les paramètres du pare-feu afin de rendre votre système moins visible pour les attaquants potentiels.

Pour obtenir des informations plus détaillées sur la configuration des règles de pare-feu dans Windows 10, vous pouvez vous référer au document officiel [Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring) pour obtenir des instructions pas à pas.

N'oubliez pas qu'un pare-feu bien configuré est un élément essentiel d'une stratégie de sécurité globale, mais qu'il doit être utilisé en conjonction avec d'autres mesures de sécurité pour assurer une protection solide de votre système.

#### 8. [**Use AppLocker**](https://github.com/simeononsecurity/AppLocker)
AppLocker est une fonctionnalité puissante de Windows 10 qui vous permet de contrôler les applications qui peuvent s'exécuter sur votre système. En mettant en œuvre des stratégies AppLocker, vous pouvez restreindre l'exécution d'applications non autorisées ou potentiellement malveillantes, ce qui renforce la sécurité de votre environnement Windows 10.

Suivez ces étapes pour utiliser AppLocker sur votre système Windows 10 :

1. **Accéder aux paramètres d'AppLocker** : Pour accéder aux paramètres d'AppLocker, ouvrez l'**Éditeur de stratégie de groupe local** en appuyant sur **touche Windows + R**, en tapant **gpedit.msc** et en cliquant **OK**. Vous pouvez également rechercher **Éditeur de stratégie de groupe** dans le menu **Démarrer**.

2. **Configurez les stratégies AppLocker : Dans l'éditeur de stratégie de groupe local, accédez à **Configuration de l'ordinateur > Paramètres Windows > Paramètres de sécurité > Stratégies de contrôle des applications > AppLocker**. Ici, vous pouvez configurer diverses politiques telles que **Règles pour les exécutables**, **Règles pour le programme d'installation de Windows**, **Règles pour les scripts**, et **Règles pour les applications packagées**.

3. **Créer des règles AppLocker** : Pour créer une règle AppLocker, cliquez avec le bouton droit de la souris sur le dossier de politique souhaité (par exemple, **Règles exécutables**) et sélectionnez **Créer une nouvelle règle**. Suivez les instructions à l'écran pour spécifier les conditions et les exceptions de la règle. Vous pouvez créer des règles basées sur le chemin d'accès au fichier, l'éditeur, le hachage du fichier ou d'autres attributs afin d'autoriser ou de refuser l'exécution de l'application.

4. **Testez et affinez les règles** : Après avoir créé les règles AppLocker, il est important de les tester pour s'assurer qu'elles fonctionnent comme prévu. Déployez les règles sur un groupe ou un système de test et vérifiez que seules les applications autorisées peuvent s'exécuter. Apportez les améliorations nécessaires aux règles en fonction des résultats des tests.

5. **Réviser et mettre à jour régulièrement** : Au fur et à mesure que votre paysage applicatif évolue, il est essentiel de revoir et de mettre à jour régulièrement vos politiques AppLocker. De nouvelles applications peuvent nécessiter une autorisation d'exécution, tandis que d'autres peuvent devenir obsolètes ou présenter des risques de sécurité. Restez proactif et gardez vos politiques à jour pour maintenir un mécanisme de contrôle des applications efficace.

AppLocker offre un contrôle granulaire sur l'exécution des applications, vous aidant à empêcher les logiciels non autorisés ou malveillants de s'exécuter sur votre système Windows 10. En utilisant AppLocker, vous pouvez réduire le risque d'infections par des logiciels malveillants, d'installations de logiciels non autorisés et d'autres incidents de sécurité.

Pour obtenir des informations plus détaillées sur la mise en œuvre des politiques AppLocker, vous pouvez vous référer au document officiel [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) or visit our [AppLocker GitHub repository](https://github.com/simeononsecurity/AppLocker) pour obtenir des ressources et des exemples supplémentaires.

N'oubliez pas de revoir et de mettre à jour régulièrement vos politiques AppLocker pour vous adapter aux exigences changeantes des applications et aux menaces de sécurité émergentes. AppLocker est un outil précieux dans votre défense contre les applications non autorisées et potentiellement nuisibles sur votre système Windows 10.

#### 9. [**Regularly Backup Your Data**](https://simeononsecurity.ch/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)
La sauvegarde régulière de vos données est une pratique essentielle pour vous protéger contre la perte de données causée par des incidents de sécurité, des pannes de matériel ou d'autres événements inattendus. En créant des sauvegardes régulières et en vérifiant leur intégrité, vous pouvez vous assurer que vos données importantes restent en sécurité et peuvent être restaurées en cas de sinistre.

Suivez ces étapes pour sauvegarder régulièrement vos données sur un système Windows 10 :

1. **Identifier les données critiques** : Commencez par identifier les données critiques qui doivent être sauvegardées. Il peut s'agir de documents importants, de fichiers personnels, de configurations système, de paramètres d'application et de toute autre donnée que vous considérez comme précieuse.

2. **Choisir une solution de sauvegarde** : Sélectionnez une solution de sauvegarde fiable qui répond à vos besoins. Windows 10 propose des outils de sauvegarde intégrés tels que **Historique des fichiers** et **Sauvegarde et restauration Windows**. Vous pouvez également opter pour un logiciel de sauvegarde tiers qui offre des fonctionnalités et une flexibilité supplémentaires.

3. **Définir la fréquence des sauvegardes** : Déterminez la fréquence des sauvegardes en fonction de la criticité de vos données et de la fréquence des changements. Certaines données peuvent nécessiter des sauvegardes quotidiennes, tandis que d'autres peuvent être sauvegardées sur une base hebdomadaire ou mensuelle.

4. **Sélectionner le stockage de la sauvegarde** : Choisissez un support de stockage approprié pour stocker vos sauvegardes. Il peut s'agir de disques durs externes, de périphériques de stockage en réseau (NAS), de services de stockage en nuage ou d'une combinaison de plusieurs options de stockage. Assurez-vous que le support de stockage est sûr et fiable.

5. **Configurer les paramètres de sauvegarde** : Configurez la solution de sauvegarde en fonction de vos préférences. Spécifiez les données à sauvegarder, la destination de la sauvegarde et les paramètres supplémentaires tels que le cryptage ou la compression.

6. **Exécuter des restaurations de test** : Testez régulièrement le processus de restauration en effectuant des restaurations de test à partir de vos sauvegardes. Cela permet de s'assurer que vos sauvegardes fonctionnent correctement et que vous pouvez récupérer vos données en cas de besoin.

7. **Surveillez et mettez à jour** : Surveillez régulièrement le processus de sauvegarde pour vous assurer qu'il se déroule comme prévu. Mettez à jour votre solution de sauvegarde et ajustez les paramètres de sauvegarde en fonction de l'évolution de vos données et de vos besoins.

En suivant ces étapes et en adhérant à une routine de sauvegarde régulière, vous pouvez minimiser l'impact de la perte de données et maintenir la disponibilité de vos informations importantes. N'oubliez pas de stocker vos sauvegardes en toute sécurité, à l'écart des données d'origine, et envisagez de mettre en œuvre la règle de sauvegarde **3-2-1** en disposant d'au moins trois copies de vos données, stockées sur deux supports de stockage différents, avec une copie stockée hors site.

Pour des informations plus détaillées sur les meilleures pratiques en matière de sauvegarde et la règle **3-2-1**, vous pouvez consulter l'article sur le site suivant [What is the 3-2-1 Backup Rule and Why You Should Use It](https://simeononsecurity.ch/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) Il fournit des informations et des recommandations précieuses pour la mise en œuvre d'une stratégie de sauvegarde efficace.

N'oubliez pas que des sauvegardes régulières sont essentielles pour sauvegarder vos données et garantir leur disponibilité en cas d'événements imprévus. Faites de la sauvegarde des données une partie intégrante de vos efforts de durcissement de Windows 10 pour protéger vos informations précieuses.

______

{{< inarticle-dark >}}


### [Hardening Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

Windows 11 est la dernière version du système d'exploitation Windows, qui offre des fonctionnalités et une sécurité améliorées. Pour renforcer votre environnement Windows 11, tenez compte des meilleures pratiques suivantes :

#### 1. **Secure Boot et TPM**
Secure Boot et TPM (Trusted Platform Module) sont des fonctions de sécurité essentielles disponibles dans Windows 11 qui aident à protéger contre les accès non autorisés et à garantir l'intégrité du système d'exploitation. En activant Secure Boot et TPM, vous pouvez renforcer la sécurité de votre système Windows 11.

Suivez ces étapes pour activer Secure Boot et TPM sur votre appareil Windows 11 :

1. **Vérifiez la compatibilité** : Avant d'activer Secure Boot et TPM, assurez-vous que votre appareil prend en charge ces fonctionnalités. Vérifiez que le matériel et le micrologiciel de votre système répondent aux exigences de la fonctionnalité Secure Boot et TPM.

2. **Accéder aux paramètres UEFI/BIOS** : Redémarrez votre appareil Windows 11 et accédez aux paramètres UEFI (Unified Extensible Firmware Interface) ou BIOS (Basic Input/Output System). La touche spécifique ou la combinaison de touches permettant d'accéder à ces paramètres peut varier en fonction de votre appareil. Les touches les plus courantes sont Del, F2, F10 ou Esc. Reportez-vous à la documentation de votre appareil ou au site web du fabricant pour obtenir des instructions détaillées.

3. **Activer le démarrage sécurisé** : Une fois dans les paramètres UEFI/BIOS, naviguez jusqu'aux paramètres Secure Boot. Activez Secure Boot pour vous assurer que seuls les systèmes d'exploitation et les composants de confiance sont autorisés à s'exécuter pendant le processus de démarrage. Cela empêche le chargement de logiciels non autorisés ou malveillants qui pourraient compromettre la sécurité du système.

4. **Activer le TPM** : Localisez les paramètres TPM dans l'UEFI/BIOS et activez la TPM. La TPM est une puce dédiée sur la carte mère de l'appareil qui fournit des fonctions de sécurité matérielles. L'activation de la TPM permet à Windows 11 d'exploiter ses capacités pour améliorer la sécurité du système.

5. **Configurer la sécurité TPM** : Après avoir activé le TPM, vous pouvez disposer d'options supplémentaires pour configurer ses paramètres de sécurité. En fonction de votre appareil et de votre micrologiciel, vous pouvez définir un mot de passe TPM, activer les mises à jour du micrologiciel TPM ou ajuster d'autres paramètres connexes. Examinez les options disponibles et configurez-les en fonction de vos besoins en matière de sécurité.

6. **Sauvegarder et quitter** : Une fois que vous avez activé Secure Boot et TPM et effectué toutes les configurations nécessaires, enregistrez les modifications dans les paramètres UEFI/BIOS et quittez. Le système redémarre et les nouveaux paramètres prennent effet.

L'activation de Secure Boot et de TPM dans Windows 11 permet de protéger votre appareil contre les modifications non autorisées, les rootkits et autres menaces de sécurité. Ces fonctionnalités établissent une base de confiance pour le système d'exploitation et contribuent à un environnement informatique plus sûr.

Notez que la disponibilité et les étapes spécifiques pour activer Secure Boot et TPM peuvent varier en fonction du fabricant et de la version du micrologiciel de votre appareil. Il est recommandé de consulter la documentation de votre appareil ou le site web du fabricant pour obtenir des instructions précises adaptées à votre système.

En activant Secure Boot et TPM sur votre appareil Windows 11, vous améliorez la posture de sécurité globale et renforcez la protection de votre système d'exploitation et de vos données sensibles.

#### 2. [**Enable Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
Windows 11 est livré avec une protection antivirus intégrée appelée **Microsoft Defender Antivirus**. Il offre une sécurité complète contre divers types de **malwares**, notamment les virus, les ransomwares et les spywares. En **activant** et en **mettant régulièrement à jour** Microsoft Defender Antivirus, vous pouvez garantir **la détection et la prévention des menaces en temps réel** sur votre système Windows 11.

Suivez ces étapes pour activer et mettre à jour Microsoft Defender Antivirus sur votre appareil Windows 11 :

1. **Vérifier l'état de l'antivirus** : Tout d'abord, vérifiez l'état de Microsoft Defender Antivirus sur votre système. Ouvrez l'application **Windows Security** en cliquant sur le menu Démarrer, en recherchant "Windows Security" et en sélectionnant l'application dans les résultats de la recherche. Une fois l'application ouverte, accédez à la section **"Protection contre les virus et les menaces "** pour vérifier l'état de Microsoft Defender Antivirus. Il devrait être **activé** par défaut sur une nouvelle installation de Windows 11.

2. **Activer la protection en temps réel** : Dans l'application Sécurité Windows, assurez-vous que la **protection en temps réel** est activée pour Microsoft Defender Antivirus. La protection en temps réel surveille en permanence votre système à la recherche de logiciels malveillants et d'autres activités malveillantes, en fournissant une **réponse immédiate** et en **bloquant les menaces** en temps réel. Si la protection en temps réel n'est pas activée, cliquez sur l'**interrupteur à bascule** pour l'activer.

3. **Mettre à jour les définitions** : La mise à jour régulière des **définitions de virus** est essentielle pour garantir que Microsoft Defender Antivirus puisse détecter et protéger contre les menaces les plus récentes. Dans l'application Windows Security, accédez à la section **"Protection contre les virus et les menaces "** et cliquez sur le bouton **"Rechercher les mises à jour "** pour mettre à jour les définitions de l'antivirus. Ce processus garantit que votre système est équipé des **dernières signatures** et **capacités de détection**.

4. **Planifier les analyses** : Microsoft Defender Antivirus vous permet de planifier des **analyses régulières du système** afin de détecter et de supprimer de manière proactive toute menace potentielle. Dans l'application Windows Security, accédez à la section **"Protection contre les virus et les menaces "** et cliquez sur l'option **"Analyse rapide "** ou **"Analyse complète "** pour lancer une analyse. Vous pouvez également cliquer sur le lien **"Options d'analyse "** pour personnaliser les paramètres d'analyse et programmer des analyses régulières selon vos préférences.

5. **Configurer des paramètres supplémentaires** : Microsoft Defender Antivirus propose des paramètres et des fonctionnalités supplémentaires que vous pouvez configurer en fonction de vos besoins en matière de sécurité. Dans l'application Sécurité Windows, explorez les différentes sections telles que **"Contrôle des applications et du navigateur", "Sécurité des appareils "** et **"Pare-feu et protection du réseau "** pour personnaliser les paramètres de l'antivirus et tirer parti des fonctions de protection avancées.

L'activation et la mise à jour régulière de Microsoft Defender Antivirus dans Windows 11 sont essentielles pour maintenir une défense solide contre les logiciels malveillants et les autres menaces de sécurité. En suivant ces étapes et en gardant Microsoft Defender Antivirus à jour, vous pouvez vous assurer que votre système Windows 11 est bien protégé.

Bien que Microsoft Defender Antivirus offre une protection solide, il est toujours recommandé d'adopter des **habitudes de navigation sûres**, de faire preuve de prudence lors du **téléchargement de fichiers** ou de l'**ouverture de pièces jointes à des courriels**, et de maintenir votre **système d'exploitation et vos applications à jour** afin d'améliorer davantage votre position de sécurité globale.

#### 3. **Appliquer l'isolation matérielle par défaut**
Windows 11 exploite des fonctions d'isolation matérielle telles que **Virtualization-based Security (VBS)** et **Hypervisor-protected Code Integrity (HVCI)** pour fournir une sécurité accrue et protéger les composants critiques du système.

En activant et en appliquant ces fonctions d'isolation matérielle par défaut, vous pouvez établir des limites de sécurité solides et atténuer les différents vecteurs d'attaque. Voici quelques étapes clés pour garantir une configuration correcte :

1. **Activer la technologie de virtualisation** : Tout d'abord, vous devez vérifier si votre système prend en charge la technologie de virtualisation et s'assurer qu'elle est activée dans les paramètres **BIOS** ou **UEFI firmware** du système. Les étapes pour accéder à la technologie de virtualisation et l'activer peuvent varier selon le fabricant de la carte mère ou du micrologiciel. Consultez la documentation de votre système ou le site web du fabricant pour obtenir des instructions spécifiques.

2. **Activez la sécurité basée sur la virtualisation (VBS)** : Windows 11 intègre VBS, qui utilise les capacités de virtualisation du matériel pour créer des conteneurs isolés appelés **Virtual Secure Mode (VSM)**. Le VSM fournit un environnement d'exécution sécurisé pour les composants critiques du système, les protégeant ainsi des attaques potentielles. Pour activer VBS, procédez comme suit :

   - Appuyez sur la **touche Windows + R** pour ouvrir la boîte de dialogue Exécuter.
   - Tapez "**gpedit.msc**" et appuyez sur **Entrée** pour ouvrir l'éditeur de stratégie de groupe local.
   - Naviguez jusqu'à **Configuration de l'ordinateur -> Modèles d'administration -> Système -> Device Guard**.
   - Double-cliquez sur la stratégie **"Activer la sécurité basée sur la virtualisation "**.
   - Sélectionnez **"Activé "** et cliquez sur **OK** pour appliquer les modifications.

   L'activation de VBS peut nécessiter un matériel compatible et certaines exigences système. Reportez-vous à la **documentation officielle de Microsoft** pour plus d'informations.

3. **Activer l'intégrité du code protégée par l'hyperviseur (HVCI)** : HVCI est une fonctionnalité qui utilise l'hyperviseur pour appliquer les politiques d'intégrité du code, empêchant ainsi l'exécution de code non autorisé et améliorant la posture de sécurité globale. Pour activer HVCI, procédez comme suit :

   - Appuyez sur la **touche Windows + R** pour ouvrir la boîte de dialogue Exécuter.
   - Tapez "**msconfig**" et appuyez sur **Entrée** pour ouvrir l'utilitaire de configuration du système.
   - Naviguez jusqu'à l'onglet **"Boot "**.
   - Cliquez sur **"Options avancées "**.
   - Cochez l'option **"Activer l'intégrité du code protégée par l'hyperviseur "**.
   - Cliquez sur **OK** pour enregistrer les modifications et redémarrer votre système.

   L'activation de HVCI nécessite un matériel compatible et certaines exigences système. Reportez-vous à la **documentation officielle de Microsoft** pour plus de détails.

En appliquant les fonctions d'isolation matérielle par défaut, telles que VBS et HVCI, vous pouvez améliorer de manière significative la sécurité de votre système Windows 11. Ces fonctionnalités permettent de protéger les composants critiques du système contre diverses attaques, y compris celles qui tentent de modifier ou d'exploiter le code et les configurations du système.

Veillez à mettre régulièrement à jour votre système avec les derniers correctifs de sécurité et les dernières mises à jour du micrologiciel afin de bénéficier des améliorations de sécurité les plus récentes et des mesures d'atténuation offertes par ces fonctions d'isolation matérielle.

Notez que la disponibilité et les exigences des fonctions d'isolation matérielle peuvent varier en fonction de la configuration de votre système et de l'édition de Windows 11. Il est recommandé de consulter la documentation officielle **Microsoft** et d'effectuer des contrôles de compatibilité pour garantir la mise en œuvre correcte de ces fonctions de sécurité.

#### 4. [**Use Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)
**Windows Sandbox** est un outil précieux qui vous permet d'exécuter des applications non fiables ou de tester des logiciels dans un environnement isolé, offrant ainsi une couche de sécurité supplémentaire à votre système. En utilisant l'Environnement de test de Windows, vous pouvez atténuer les risques potentiels associés à l'exécution de programmes non fiables.

L'Environnement de test de Windows crée un environnement de bureau léger et temporaire qui est complètement séparé de votre système d'exploitation principal. Toutes les modifications effectuées dans l'Environnement de test sont supprimées dès que vous le fermez, ce qui garantit que votre système principal n'est pas affecté.

Pour utiliser l'Environnement de test de Windows, procédez comme suit :

1. **Vérifier la configuration requise** : Avant de poursuivre, assurez-vous que votre système répond aux exigences requises pour l'exécution de l'Environnement de test Windows. En général, vous avez besoin d'une édition Windows 10 Pro ou Enterprise et d'un processeur dont les capacités de virtualisation sont activées dans le micrologiciel BIOS/UEFI. Consultez le site officiel de l [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) pour les exigences spécifiques du système.

2. **Activer Windows Sandbox** : Windows Sandbox est une fonctionnalité intégrée dans les éditions Pro et Enterprise de Windows 10. Pour activer l'Environnement de test de Windows, procédez comme suit :

   - Appuyez sur la **touche Windows + R** pour ouvrir la boîte de dialogue Exécuter.
   - Tapez "**appwiz.cpl**" et appuyez sur **Entrée** pour ouvrir la fenêtre Programmes et fonctionnalités.
   - Cliquez sur **"Activer ou désactiver des fonctionnalités de Windows "** sur le côté gauche.
   - Faites défiler vers le bas et localisez **"Windows Sandbox "** dans la liste des fonctionnalités.
   - Cochez la case située à côté de **"Windows Sandbox "** et cliquez sur **OK** pour l'activer.
   - Windows installera les composants nécessaires et vous devrez peut-être redémarrer votre système pour que les modifications soient prises en compte.

3. **Lancez l'Environnement de test Windows** : Une fois que Windows Sandbox est activé, vous pouvez le lancer en suivant les étapes suivantes :

   - Ouvrez le menu **Démarrer** et recherchez **"Windows Sandbox "**.
   - Cliquez sur l'application **"Windows Sandbox "** pour l'ouvrir.
   - L'Environnement de test sera lancé dans une fenêtre séparée, vous offrant un environnement sécurisé pour exécuter des applications non fiables ou tester des logiciels.

Lorsque vous exécutez des applications dans l'Environnement de test Windows, gardez à l'esprit que l'Environnement de test est isolé et conçu pour ignorer toutes les modifications qui y sont apportées. Il est donc essentiel de sauvegarder vos fichiers ou vos données en dehors de l'Environnement de test si vous devez les conserver.

L'Environnement de test de Windows est un outil efficace pour tester des logiciels inconnus, ouvrir des fichiers suspects ou explorer des sites web potentiellement risqués. Il ajoute une couche supplémentaire de protection en garantissant que toute activité malveillante ou modification indésirable est confinée dans l'Environnement de test et n'a pas d'impact sur le système d'exploitation principal.

En intégrant le bac à sable de Windows dans vos pratiques de sécurité, vous pouvez réduire considérablement les risques associés à l'exécution d'applications non fiables, protégeant ainsi votre système contre les menaces potentielles.

Pour plus d'informations sur l'Environnement de sable de Windows et son utilisation, consultez le site officiel de l'Environnement de sable de Windows. [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

#### 5. [**Implement Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)
Microsoft Defender Application Guard est une fonction de sécurité puissante qui isole les sessions du navigateur Microsoft Edge du système d'exploitation sous-jacent. En exécutant Edge dans un environnement sécurisé et isolé, Application Guard contribue à protéger votre système contre les attaques basées sur le navigateur et les sites web malveillants.

Pour mettre en œuvre Microsoft Defender Application Guard et renforcer la sécurité de votre navigateur, procédez comme suit :

1. **Vérifier la compatibilité** : Avant de poursuivre, assurez-vous que votre système répond à la configuration requise pour l'exécution de Microsoft Defender Application Guard. En règle générale, vous avez besoin de Windows 10 Pro ou Enterprise, d'un processeur compatible avec des capacités de virtualisation et d'au moins 8 Go de RAM. Reportez-vous à la documentation officielle de Microsoft Defender Application Guard. [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) pour les exigences spécifiques du système.

2. **Activer Application Guard** : Application Guard est disponible en tant que fonctionnalité optionnelle dans Windows 10. Pour activer Microsoft Defender Application Guard, procédez comme suit :

   - Appuyez sur la **touche Windows + R** pour ouvrir la boîte de dialogue Exécuter.
   - Tapez "**appwiz.cpl**" et appuyez sur **Entrée** pour ouvrir la fenêtre Programmes et fonctionnalités.
   - Cliquez sur **"Activer ou désactiver des fonctionnalités de Windows "** sur le côté gauche.
   - Faites défiler vers le bas et localisez **"Microsoft Defender Application Guard "** dans la liste des fonctionnalités.
   - Cochez la case en regard de **"Microsoft Defender Application Guard "** et cliquez sur **OK** pour l'activer.
   - Windows installera les composants nécessaires et vous devrez peut-être redémarrer votre système pour que les modifications soient prises en compte.

3. **Configurez Application Guard** : Une fois l'Application Guard activé, vous pouvez configurer ses paramètres en fonction de vos besoins en matière de sécurité. Application Guard vous permet de définir le niveau d'isolation et de contrôler la manière dont il traite les sites web et les fichiers non fiables. Vous pouvez ajuster ces paramètres via l'application **Windows Security** ou les paramètres de stratégie de groupe.

4. **Tester et vérifier** : Après avoir activé et configuré Microsoft Defender Application Guard, il est essentiel de tester et de vérifier son fonctionnement. Ouvrez Microsoft Edge et visitez un site web malveillant connu ou un site présentant des risques potentiels pour vérifier si Application Guard réussit à isoler la session du navigateur et à empêcher toute attaque potentielle.

En mettant en œuvre Microsoft Defender Application Guard, vous ajoutez une couche supplémentaire de protection à votre système en isolant les sessions du navigateur et en contenant toutes les menaces potentielles dans un environnement sécurisé. Cela permet de protéger votre système et vos données contre les attaques basées sur le navigateur, telles que les téléchargements "drive-by", les scripts malveillants et les exploits "zero-day".

Pour plus d'informations sur la configuration et l'utilisation de Microsoft Defender Application Guard, reportez-vous au document officiel [**Microsoft documentation**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard)

#### 6. [**Controlled Folder Access**](https://github.com/simeononsecurity/Windows-Defender-Hardening)
L'accès contrôlé aux dossiers est une puissante fonction de sécurité disponible dans Windows 11 qui permet de protéger les dossiers importants contre les modifications non autorisées par les ransomwares et autres logiciels malveillants. En activant l'accès contrôlé aux dossiers et en ajoutant les dossiers nécessaires à la liste des dossiers protégés, vous pouvez renforcer la sécurité de votre système et prévenir les pertes de données potentielles.

Pour mettre en œuvre l'accès contrôlé aux dossiers et protéger vos dossiers importants, procédez comme suit :

1. **Ouvrez Windows Security** : Appuyez sur la **touche Windows** de votre clavier, tapez "**Windows Security**" et sélectionnez l'application **Windows Security** dans les résultats de la recherche.

2. **Naviguez jusqu'à Paramètres de protection contre les virus et les menaces** : Dans l'application Windows Security, cliquez sur l'onglet **"Protection contre les virus et les menaces "** dans le menu de gauche.

3. **Configurez l'accès contrôlé aux dossiers** : Dans la section **"Protection contre les ransomwares "**, cliquez sur **"Gérer la protection contre les ransomwares "** pour accéder aux paramètres de l'accès contrôlé aux dossiers.

4. **Activer l'accès aux dossiers contrôlés** : Dans les paramètres de l'accès contrôlé aux dossiers, basculez le commutateur sur **"On "** pour activer la fonctionnalité. Windows affiche un avertissement indiquant que seules les applications de confiance peuvent accéder aux dossiers protégés.

5. **Ajouter des dossiers protégés** : Pour spécifier les dossiers à protéger, cliquez sur **"Dossiers protégés "**, puis sélectionnez **"Ajouter un dossier protégé "**. Choisissez les dossiers que vous souhaitez protéger et cliquez sur **"OK "**.

   - Il est recommandé d'ajouter les dossiers importants tels que les documents, les images, les vidéos et tout autre répertoire contenant des données précieuses.

6. **Autoriser ou bloquer des applications** : Par défaut, l'accès contrôlé aux dossiers permet aux applications de confiance d'accéder aux dossiers protégés. Toutefois, vous pouvez personnaliser ce comportement en cliquant sur **"Autoriser une application via l'accès contrôlé aux dossiers "**. À partir de là, vous pouvez autoriser ou bloquer des applications spécifiques pour qu'elles accèdent aux dossiers protégés.

7. **Surveiller et examiner** : Après avoir activé l'accès contrôlé aux dossiers, Windows surveille et consigne en permanence toute tentative d'accès aux dossiers protégés par des applications non autorisées. Vous pouvez consulter ces journaux en cliquant sur **"Consulter "** dans la section **"Applications récemment bloquées "** des paramètres de l'accès aux dossiers contrôlés.

En mettant en œuvre l'accès contrôlé aux dossiers, vous ajoutez une couche supplémentaire de protection à vos dossiers importants, en réduisant le risque de modifications non autorisées et de perte potentielle de données causée par des attaques de ransomware. Revoyez régulièrement les paramètres d'accès contrôlé aux dossiers pour vous assurer que les dossiers protégés correspondent à vos exigences de sécurité.

Pour plus d'informations sur la configuration et l'utilisation de l'accès contrôlé aux dossiers, consultez le document officiel intitulé [**Microsoft documentation**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide)


#### 7. **Activer la maintenance automatique de Windows**
Windows 11 comprend une fonction pratique appelée Maintenance automatique qui permet de maintenir votre système optimisé et protégé en effectuant des tâches de maintenance régulières. En activant la maintenance automatique, vous vous assurez que votre système fonctionne correctement et reste sécurisé.

Pour activer la maintenance automatique de Windows, procédez comme suit :

1. **Ouvrez les paramètres de Windows** : Appuyez sur la **touche Windows** de votre clavier, tapez "**Paramètres**" et sélectionnez l'application **Paramètres** dans les résultats de la recherche.

2. **Accédez aux paramètres de maintenance** : Dans l'application Paramètres, cliquez sur la catégorie **"Système "**, puis sélectionnez **"À propos "** dans le menu de gauche. Faites défiler la page jusqu'en bas et cliquez sur le lien **"Infos système "**.

3. **Ouvrez les paramètres de maintenance : Dans la fenêtre "System Information", cliquez sur le lien **"Maintenance "** situé en bas de la page.

4. **Activer la maintenance automatique** : Dans les paramètres de maintenance, basculez l'interrupteur situé à côté de **"Maintenance automatique "** sur la position **"On "**.

5. **Configurer les paramètres de maintenance** : Par défaut, Windows planifie automatiquement les tâches de maintenance pour qu'elles s'exécutent tous les jours à 2 heures du matin. Si vous préférez une programmation différente, cliquez sur **"Modifier les paramètres de maintenance "** et personnalisez les options souhaitées, telles que l'heure de début de la maintenance et la fréquence des tâches de maintenance.

6. **Réviser les paramètres supplémentaires** : Sous l'interrupteur à bascule de la maintenance automatique, vous trouverez d'autres paramètres liés à la maintenance, tels que **"Autoriser la maintenance programmée à réveiller mon ordinateur à l'heure prévue "** et **"Autoriser la maintenance programmée à s'exécuter même lorsque je suis sur batterie "**. Ajustez ces paramètres en fonction de vos préférences et de vos besoins.

7. **Surveiller les activités de maintenance** : Lorsque la maintenance automatique est activée, Windows exécute automatiquement des tâches de maintenance en arrière-plan à l'heure prévue. Vous pouvez surveiller ces activités en consultant la section **"Maintenance "** dans l'application **"Sécurité Windows "** ou en examinant les journaux **"Maintenance "** dans l'observateur d'événements.

L'activation de la maintenance automatique de Windows garantit que votre système reste optimisé et protégé en effectuant régulièrement des tâches de maintenance essentielles telles que les mises à jour logicielles, l'optimisation du disque et les analyses de sécurité. En maintenant votre système en bonne santé, vous pouvez profiter d'une expérience informatique plus fluide et plus sûre.

Pour plus d'informations sur la maintenance automatique de Windows et ses options de configuration, reportez-vous à la documentation officielle sur la maintenance automatique de Windows. [**Microsoft documentation**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence)

______

{{< inarticle-dark >}}

## Conclusion

La mise en œuvre de ces **bonnes pratiques de durcissement de Windows** est essentielle pour garantir la sécurité de vos systèmes Windows. En **mettant régulièrement à jour votre système d'exploitation**, vous pouvez corriger les failles de sécurité et améliorer la stabilité du système. L'activation de fonctions de sécurité telles que **antivirus** et **chiffrement** ajoute une couche supplémentaire de protection à vos données. La configuration de **contrôles d'accès** appropriés permet d'empêcher les modifications non autorisées et de restreindre l'accès aux ressources sensibles.

En respectant ces bonnes pratiques, vous pouvez renforcer la sécurité de votre **environnement Windows**, protéger vos données et maintenir l'intégrité de votre **infrastructure numérique**. Il est important de rester **proactif** et de revoir et mettre à jour régulièrement vos mesures de sécurité afin de rester à l'affût des menaces potentielles.

Rappelez-vous que le **durcissement de Windows** est un processus continu et qu'il est essentiel de rester informé des dernières mises à jour et pratiques en matière de sécurité. En restant proactif et en mettant en œuvre ces meilleures pratiques, vous pouvez atténuer efficacement les risques de sécurité et garantir la sécurité de vos systèmes Windows.

Pour plus d'informations sur le durcissement de Windows et les meilleures pratiques, consultez des sources fiables telles que la **documentation de Microsoft**, les **forums de sécurité** et les **sites web de confiance consacrés à la cybersécurité**.

______

## Références :

- [Microsoft Windows Security](https://www.microsoft.com/en-us/security)
- [NIST Special Publication 800-171: Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [CIS Microsoft Windows 10 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [CIS Microsoft Windows 11 Benchmark](https://www.cisecurity.org/benchmark/microsoft_windows_11/)